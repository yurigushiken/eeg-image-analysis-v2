#!/usr/bin/env python
from __future__ import annotations

import argparse
import os
import sys
import numpy as np
import json
import time

# Ensure src/ is on the import path when run from repo root
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(REPO_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from eeg.config import load_config, load_electrodes_config, load_components_config
from eeg.plots import make_erp_figure, make_component_figure
from eeg.report import write_analysis_page, ensure_index_template, update_index_grid
from eeg.io import discover_epoch_files, read_epochs, apply_montage, validate_baseline_window, extract_subject_id
from eeg.measures import peak_amplitude_and_latency
import matplotlib.pyplot as plt
import mne


def main() -> int:
    parser = argparse.ArgumentParser(description="Run YAML-driven ERP analysis")
    parser.add_argument("--config", required=True, help="Path to analysis YAML")
    args = parser.parse_args()

    # Determinism: ensure any incidental randomness is fixed for reproducibility
    np.random.seed(0)
    t_start = time.perf_counter()

    cfg = load_config(args.config)

    # Minimal smoke behavior: ensure output directories and page exist
    plots_dir = cfg.outputs.get("plots_dir")
    tables_dir = cfg.outputs.get("tables_dir")
    page_path = cfg.outputs.get("page")

    if not plots_dir or not tables_dir or not page_path:
        raise SystemExit("Config outputs must include plots_dir, tables_dir, and page")

    os.makedirs(plots_dir, exist_ok=True)
    os.makedirs(tables_dir, exist_ok=True)
    os.makedirs(os.path.dirname(page_path), exist_ok=True)

    # Try to discover data files; if none, generate placeholder ERP overlay for each component
    repo_root = REPO_ROOT
    _ = load_electrodes_config(repo_root)
    components_cfg = load_components_config(repo_root)
    fif_files = discover_epoch_files(
        root=os.path.join(repo_root, cfg.dataset.get("root", "data")),
        pattern=cfg.dataset.get("pattern", "**/*.fif"),
    )

    saved_figs = []
    analysis_id = os.path.splitext(os.path.basename(page_path))[0]
    if len(fif_files) == 0:
        # Placeholder: simple synthetic curves for each component
        times_ms = np.linspace(-100, 400, 256)
        for comp in cfg.components:
            curves = {
                "Small_Increasing": np.sin(times_ms / 80.0),
                "Small_Decreasing": np.cos(times_ms / 90.0),
            }
            fig = make_erp_figure(
                curves_by_label=curves,
                times_ms=times_ms,
                title=f"{analysis_id}: {comp}",
                subtitle=f"baseline {tuple(cfg.preprocessing.get('baseline_ms', [-100,0]))} ms; synthetic",
                annotate_fallback=False,
            )
            out_path = os.path.join(plots_dir, f"{comp}_overlay.png")
            fig.savefig(out_path, dpi=int(cfg.plots.get("dpi", 150)))
            saved_figs.append(out_path)
    else:
        # Real pipeline (simplified): compute per-set grand average ROI curves and topomaps
        baseline = tuple(cfg.preprocessing.get("baseline_ms", [-100, 0]))
        topomap_half_win = int(cfg.plots.get("topomap_peak_window_ms", 50))
        roi_min = int(cfg.roi.get("min_channels", 4))
        response = str(cfg.selection.get("response", "ALL")).upper()

        # Prepare per-set subject evokeds and QC rows
        sets = cfg.selection.get("condition_sets", [])
        set_name_to_evokeds = {s["name"]: [] for s in sets}
        qc_rows = []

        # ROI lists from electrodes config
        electrodes = load_electrodes_config(repo_root)

        empty_sets = set()
        for fif in fif_files:
            epochs = read_epochs(fif)
            apply_montage(epochs, cfg.dataset.get("montage_sfp"))
            # Baseline correction (ms to seconds)
            bl = (baseline[0] / 1000.0, baseline[1] / 1000.0)
            validate_baseline_window(epochs, baseline)
            if response == "ACC1":
                if getattr(epochs, "metadata", None) is None or "Target.ACC" not in epochs.metadata.columns:
                    continue
                epochs = epochs[epochs.metadata["Target.ACC"] == 1]
            epochs.apply_baseline(bl)
            subj_id = extract_subject_id(epochs, fif)

            # For each set, subset and average if threshold satisfied
            for item in sets:
                name = item["name"]
                codes = [str(c) for c in item.get("conditions", [])]
                if getattr(epochs, "metadata", None) is not None and "Condition" in epochs.metadata.columns:
                    mask = epochs.metadata["Condition"].astype(str).isin(codes)
                    sub = epochs[mask]
                else:
                    # Fallback using event labels
                    sub = None
                    for code in codes:
                        try:
                            part = epochs[str(code)]
                        except Exception:
                            continue
                        sub = part if sub is None else sub + part
                    if sub is None:
                        empty_sets.add(name)
                        qc_rows.append({
                            "subject": subj_id,
                            "set": name,
                            "included": False,
                            "epoch_count": 0,
                            "exclusion_reason": "no_matching_conditions",
                            "roi_available_vs_required": None,
                        })
                        continue
                epoch_count = int(len(sub))
                min_epochs = int(cfg.selection.get("min_epochs_per_set", 1))
                if epoch_count < min_epochs:
                    empty_sets.add(name)
                    qc_rows.append({
                        "subject": subj_id,
                        "set": name,
                        "included": False,
                        "epoch_count": epoch_count,
                        "exclusion_reason": f"insufficient_epochs(<{min_epochs})",
                        "roi_available_vs_required": None,
                    })
                    continue
                evk = sub.average()
                set_name_to_evokeds[name].append(evk)
                # ROI availability per subject (unique union of ROI channels across configured components)
                # Build union of channels from electrodes config for all components used in this run
                roi_union = []
                for c in cfg.components:
                    if c == "P1":
                        names = ["P1"]
                    elif c == "N1":
                        names = ["N1_L", "N1_R"]
                    else:
                        names = ["P3B"]
                    for rn in names:
                        roi_union.extend(electrodes.get(rn, []))
                roi_union = list(dict.fromkeys(roi_union))
                available = sum(1 for ch in roi_union if ch in epochs.ch_names)
                qc_rows.append({
                    "subject": subj_id,
                    "set": name,
                    "included": True,
                    "epoch_count": epoch_count,
                    "exclusion_reason": "",
                    "roi_available_vs_required": f"{available}/{roi_min}",
                })

        # Plot overlays and topomaps per component
        components_cfg = load_components_config(repo_root)
        for comp in cfg.components:
            comp_cfg = components_cfg.get(comp, {})
            window = tuple(comp_cfg.get("window_ms", [0, 0]))
            # Determine ROI channels for this component
            if comp == "P1":
                roi_names = ["P1"]
            elif comp == "N1":
                roi_names = ["N1_L", "N1_R"]
            else:  # P3b
                roi_names = ["P3B"]

            curves_by_label = {}
            topomap_by_label = {}
            times_ms = None
            for item in sets:
                name = item["name"]
                evokeds = set_name_to_evokeds.get(name, [])
                if not evokeds:
                    continue
                # Combine evokeds equally
                gav = mne.combine_evoked(evokeds, weights="equal")
                # ROI aggregation: average selected channels
                roi_chs = []
                for rn in roi_names:
                    roi_chs.extend(electrodes.get(rn, []))
                roi_chs = list(dict.fromkeys(roi_chs))
                pick = [ch for ch in roi_chs if ch in gav.ch_names]
                if len(pick) < roi_min:
                    continue
                data = gav.copy().pick_channels(pick).data
                roi_curve = data.mean(axis=0)
                times_ms = (gav.times * 1000.0).astype(float)
                # Detect peak
                polarity = "pos" if comp in ("P1", "P3b") else "neg"
                amp, lat, used_fallback = peak_amplitude_and_latency(roi_curve, times_ms, window_ms=window, polarity=polarity)
                # Build overlay curves
                curves_by_label[name] = roi_curve

                # Topomap around peak (capture vectors for composite figure)
                tmin = (lat - topomap_half_win) / 1000.0
                tmax = (lat + topomap_half_win) / 1000.0
                evk_win = gav.copy().crop(tmin=tmin, tmax=tmax)
                mean_vec = evk_win.data.mean(axis=1)
                # Store topomap with fallback flag for annotation
                topomap_by_label[name] = (mean_vec, int(lat), int(topomap_half_win), used_fallback)

            if curves_by_label and times_ms is not None:
                # Prepare styles if specified
                color_list = cfg.plots.get("colors") or []
                colors = {label: color_list[i % len(color_list)] for i, label in enumerate(sorted(curves_by_label.keys()))} if color_list else None
                styles_cfg = cfg.plots.get("linestyles") or {}
                linestyles = {k: v for k, v in styles_cfg.items()}

                # Set x-axis limits to start from baseline onset (user-configurable)
                # This makes the plot match the YAML configuration more clearly
                xlim_ms = (baseline[0], times_ms[-1])  # From baseline start to end of epoch

                fig = make_component_figure(
                    curves_by_label=curves_by_label,
                    times_ms=times_ms,
                    topomap_by_label=topomap_by_label,
                    info=gav.info,
                    title=f"{analysis_id}: {comp} ({response})",
                    subtitle=f"baseline {baseline} ms; ±{topomap_half_win} ms topomap; roi.min={roi_min}",
                    colors=colors,
                    linestyles=linestyles,
                    xlim_ms=xlim_ms,
                )
                out_path = os.path.join(plots_dir, f"{comp}.png")
                fig.savefig(out_path, dpi=int(cfg.plots.get("dpi", 150)))
                saved_figs.append(out_path)
    # Write a minimal analysis page and ensure index template exists
    notes = []
    if len(fif_files) == 0:
        notes.append("No FIF files found; synthetic curves rendered for demonstration.")
    if 'empty_sets' in locals() and empty_sets:
        for s in sorted(empty_sets):
            notes.append(f"Set {s}: No subjects met inclusion criteria (min_epochs_per_set={cfg.selection.get('min_epochs_per_set', 1)})")
    write_analysis_page(page_path, title=os.path.splitext(os.path.basename(page_path))[0], figure_paths=saved_figs, notes=notes)
    index_path = os.path.join(repo_root, "docs", "index.md")
    ensure_index_template(index_path)
    # Map component to relative path from docs/
    comp_to_img = {}
    for p in saved_figs:
        comp = os.path.splitext(os.path.basename(p))[0].split("_")[0]
        rel = os.path.relpath(p, os.path.join(repo_root, "docs")).replace("\\", "/")
        comp_to_img[comp] = rel
    update_index_grid(index_path, analysis_id, comp_to_img)

    # Metrics: runtime and asset sizes
    duration_s = time.perf_counter() - t_start
    tables_dir = cfg.outputs.get("tables_dir")
    if tables_dir:
        os.makedirs(tables_dir, exist_ok=True)
        sizes = {os.path.basename(p): os.path.getsize(p) for p in saved_figs if os.path.isfile(p)}
        largest = (max(sizes.values()) if sizes else 0)
        total = int(sum(sizes.values())) if sizes else 0
        # Performance thresholds per US3 T304
        largest_limit = 2 * 1024 * 1024  # 2 MB
        total_limit = 20 * 1024 * 1024   # 20 MB
        metrics = {
            "analysis_id": analysis_id,
            "duration_seconds": round(duration_s, 3),
            "num_figures": len(saved_figs),
            "largest_png_bytes": largest,
            "total_png_bytes": total,
            "largest_png_ok": bool(largest <= largest_limit),
            "cumulative_png_ok": bool(total <= total_limit),
            "largest_png_limit_bytes": largest_limit,
            "total_png_limit_bytes": total_limit,
            "figures": sizes,
        }
        with open(os.path.join(tables_dir, "run_metrics.json"), "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2)
        # QC CSV
        if 'qc_rows' in locals() and qc_rows:
            import csv
            with open(os.path.join(tables_dir, "qc_summary.csv"), "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["subject", "set", "included", "epoch_count", "exclusion_reason", "roi_available_vs_required"])
                writer.writeheader()
                writer.writerows(qc_rows)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


