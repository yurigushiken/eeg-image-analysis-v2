#!/usr/bin/env python
"""Compute P1–N1 peak-to-peak amplitudes using bilateral POT (N1 ROI) only.

This utility:
- Loads an existing analysis YAML to reuse dataset, selection, baseline, etc.
- Builds a collapsed localizer using the N1 ROI for BOTH P1 and N1
  to obtain FWHM windows within their a priori time ranges.
- For each subject × condition, extracts the N1 ROI waveform and measures:
  * P1 peak amplitude (positive) within P1 window
  * N1 peak amplitude (negative) within N1 window
  * Peak-to-peak amplitude = P1_peak - N1_peak (µV)
- Saves a subject-level CSV and an ERP overlay plot (no topomaps).
"""
from __future__ import annotations

import argparse
import os
import sys
from typing import Dict, List

import numpy as np

# Ensure src/ on path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(REPO_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from eeg.config import load_config, load_components_config, load_electrodes_config
from eeg.io import (
    discover_epoch_files,
    read_epochs,
    apply_montage,
    validate_baseline_window,
    extract_subject_id,
    filter_by_response,
    select_conditions,
)
from eeg.collapsed_localizer import compute_collapsed_localizer_roi
from eeg.measures import peak_amplitude, peak_latency
from eeg.plots import make_erp_figure
import matplotlib.pyplot as plt


def _get_n1_roi_channels(electrodes_cfg: Dict[str, List[str]]) -> List[str]:
    left = electrodes_cfg.get("N1_L", [])
    right = electrodes_cfg.get("N1_R", [])
    return list(left) + list(right)


def main() -> int:
    ap = argparse.ArgumentParser(description="P1–N1 peak-to-peak using N1 (POT) ROI only")
    ap.add_argument("--config", required=True, help="Path to an existing analysis YAML")
    args = ap.parse_args()

    cfg = load_config(args.config)

    # I/O destinations (under peak_to_peak/output/<analysis_id>/)
    analysis_id = os.path.splitext(os.path.basename(cfg.outputs.get("page", "analysis")))[0]
    base_out = os.path.join(REPO_ROOT, "peak_to_peak", "output", analysis_id)
    plots_dir = os.path.join(base_out, "plots")
    tables_dir = os.path.join(base_out, "tables")
    os.makedirs(plots_dir, exist_ok=True)
    os.makedirs(tables_dir, exist_ok=True)

    # Load component/electrode configs
    components_cfg = load_components_config(REPO_ROOT)
    electrodes_cfg = load_electrodes_config(REPO_ROOT)
    n1_roi_channels = _get_n1_roi_channels(electrodes_cfg)
    if not n1_roi_channels:
        raise SystemExit("No N1 ROI channels found (N1_L/N1_R) in configs/electrodes.yaml")

    # Discover data
    fif_files = discover_epoch_files(
        root=os.path.join(REPO_ROOT, cfg.dataset.get("root", "data")),
        pattern=cfg.dataset.get("pattern", "**/*.fif"),
    )
    if not fif_files:
        print("No FIF files found; nothing to do.")
        return 1

    baseline = tuple(cfg.preprocessing.get("baseline_ms", [-100, 0]))
    response = str(cfg.selection.get("response", "ALL")).upper()
    sets = cfg.selection.get("condition_sets", [])

    # Collect subject evokeds by condition set
    set_name_to_evokeds: Dict[str, List] = {s["name"]: [] for s in sets}
    subject_entries: List[dict] = []

    for fif in fif_files:
        epochs = read_epochs(fif)
        apply_montage(epochs, cfg.dataset.get("montage_sfp"))
        # baseline
        validate_baseline_window(epochs, baseline)
        epochs.apply_baseline((baseline[0] / 1000.0, baseline[1] / 1000.0))
        subj_id = extract_subject_id(epochs, fif)

        for item in sets:
            name = item["name"]
            codes = [str(c) for c in item.get("conditions", [])]
            set_response = str(item.get("response") or response).upper()
            try:
                epochs_for_set = filter_by_response(epochs, set_response)
                sub = select_conditions(epochs_for_set, codes, item.get("metadata_filters") or {}, name)
            except Exception:
                continue

            n_epochs = int(len(sub))
            if n_epochs < int(cfg.selection.get("min_epochs_per_set", 1)):
                continue
            evk = sub.average()
            set_name_to_evokeds[name].append(evk)
            subject_entries.append({
                "subject_id": subj_id,
                "condition": name,
                "evoked": evk,
                "n_epochs": n_epochs,
            })

    # Collapsed localizer windows using N1 ROI for P1 and N1
    # Use a priori ranges from components.yaml
    def _localize(comp: str, polarity: str) -> dict:
        sr = components_cfg.get(comp, {}).get("window_ms")
        if not sr or len(sr) != 2:
            raise ValueError(f"Missing or invalid window_ms for {comp} in components.yaml")
        return compute_collapsed_localizer_roi(
            evokeds_by_set=set_name_to_evokeds,
            roi_channels=n1_roi_channels,
            component_name=comp,
            search_range_ms=tuple(sr),
            polarity=polarity,
        )

    p1_loc = _localize("P1", polarity="positive")
    n1_loc = _localize("N1", polarity="negative")

    p1_window = (float(p1_loc["window_start_ms"]), float(p1_loc["window_end_ms"]))
    n1_window = (float(n1_loc["window_start_ms"]), float(n1_loc["window_end_ms"]))

    # Subject-level measurements
    rows: List[dict] = []
    # For plotting overlay, collect condition curves (averaged across subjects for visualization)
    curves_by_label: Dict[str, np.ndarray] = {}
    times_ms_for_plot = None

    for entry in subject_entries:
        evk = entry["evoked"]
        subj_id = entry["subject_id"]
        condition = entry["condition"]
        n_epochs = entry["n_epochs"]

        # Extract N1 ROI waveform in µV
        evk_roi = evk.copy().pick_channels(n1_roi_channels, ordered=False)
        roi_curve = evk_roi.data.mean(axis=0) * 1e6
        times_ms = (evk_roi.times * 1000.0).astype(float)

        # Measure P1 peak (positive) and N1 peak (negative)
        p1_amp = peak_amplitude(roi_curve, times_ms, p1_window, polarity="positive")
        p1_lat = peak_latency(roi_curve, times_ms, p1_window, polarity="positive")
        n1_amp = peak_amplitude(roi_curve, times_ms, n1_window, polarity="negative")
        n1_lat = peak_latency(roi_curve, times_ms, n1_window, polarity="negative")

        p2p = float(p1_amp - n1_amp)

        rows.append({
            "subject_id": subj_id,
            "condition": condition,
            "p1_peak_uv": float(p1_amp),
            "p1_latency_ms": float(p1_lat),
            "n1_peak_uv": float(n1_amp),
            "n1_latency_ms": float(n1_lat),
            "p2p_amplitude_uv": p2p,
            "n_epochs": int(n_epochs),
            "window_p1_start_ms": p1_window[0],
            "window_p1_end_ms": p1_window[1],
            "window_n1_start_ms": n1_window[0],
            "window_n1_end_ms": n1_window[1],
        })

        # For plotting: accumulate per-condition grand average over subjects (N1 ROI only)
        try:
            if times_ms_for_plot is None:
                times_ms_for_plot = times_ms
            if condition not in curves_by_label:
                curves_by_label[condition] = []
            curves_by_label[condition].append(roi_curve)
        except Exception:
            pass

    # Save subject-level CSV
    if rows:
        import csv
        out_csv = os.path.join(tables_dir, "subject_peak_to_peak.csv")
        fieldnames = [
            "subject_id", "condition",
            "p1_peak_uv", "p1_latency_ms",
            "n1_peak_uv", "n1_latency_ms",
            "p2p_amplitude_uv",
            "n_epochs",
            "window_p1_start_ms", "window_p1_end_ms",
            "window_n1_start_ms", "window_n1_end_ms",
        ]
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        print(f"Saved: {out_csv}")

    # Make overlay plot (N1 ROI only), annotate P1/N1 peaks and P2P
    if curves_by_label and times_ms_for_plot is not None:
        # Convert per-condition list of curves into grand averages
        gav_curves = {k: np.mean(np.stack(v, axis=0), axis=0) for k, v in curves_by_label.items()}
        xlim_ms = (baseline[0], float(times_ms_for_plot[-1]))

        # Colors from YAML condition_sets first, then cfg.plots.colors fallback
        condition_config_map = {item["name"]: item for item in sets}
        color_list = cfg.plots.get("colors") or []
        def _color_for(label: str, default_color: str) -> str:
            if label in condition_config_map and "color" in condition_config_map[label]:
                return condition_config_map[label]["color"]
            return default_color
        if color_list:
            base_colors = {label: color_list[i % len(color_list)] for i, label in enumerate(sorted(gav_curves.keys()))}
            colors = {label: _color_for(label, base_colors[label]) for label in base_colors}
        else:
            colors = {label: _color_for(label, "#1f77b4") for label in gav_curves.keys()}

        linestyles_cfg = cfg.plots.get("linestyles") or {}
        linestyles = {label: linestyles_cfg.get(label, "-") for label in gav_curves.keys()}

        fig = make_erp_figure(
            curves_by_label=gav_curves,
            times_ms=times_ms_for_plot,
            title=f"{analysis_id}: N1 ROI (POT) overlay",
            subtitle=f"baseline {baseline} ms; windows: P1 [{p1_window[0]:.1f},{p1_window[1]:.1f}] ms, N1 [{n1_window[0]:.1f},{n1_window[1]:.1f}] ms",
            colors=colors,
            linestyles=linestyles,
            xlim_ms=xlim_ms,
            ylimit_uv=float(cfg.plots.get("ylimit_uv", 6.0)),
            epochs_by_label=None,
        )
        # Annotate horizontal amplitude levels per condition (no vertical latency lines)
        try:
            ax = fig.axes[0] if fig.axes else None
        except Exception:
            ax = None

        summary_lines = []
        if ax is not None:
            for label in sorted(gav_curves.keys()):
                curve = gav_curves[label]
                try:
                    p1_amp_c = peak_amplitude(curve, times_ms_for_plot, p1_window, polarity="positive")
                    p1_lat_c = peak_latency(curve, times_ms_for_plot, p1_window, polarity="positive")
                    n1_amp_c = peak_amplitude(curve, times_ms_for_plot, n1_window, polarity="negative")
                    n1_lat_c = peak_latency(curve, times_ms_for_plot, n1_window, polarity="negative")
                except Exception:
                    continue

                delta_uv = float(p1_amp_c - n1_amp_c)
                summary_lines.append(f"{label}: Δ(P1–N1)={delta_uv:.2f} µV")

                color = colors.get(label, "#444") if colors else "#444"
                ls = linestyles.get(label, "-")

                # Horizontal amplitude levels: P1 (solid), N1 (dotted)
                try:
                    ax.axhline(y=p1_amp_c, color=color, linestyle=ls, linewidth=0.8, alpha=0.55, zorder=3)
                    ax.axhline(y=n1_amp_c, color=color, linestyle=":", linewidth=0.8, alpha=0.55, zorder=3)
                except Exception:
                    pass
                # No vertical latency lines or arrows (per request)

            # Add a small summary textbox
            if summary_lines:
                try:
                    ax.text(0.995, 0.02, "\n".join(summary_lines), transform=ax.transAxes,
                            ha="right", va="bottom", fontsize=8, color="#444")
                except Exception:
                    pass
        out_png = os.path.join(plots_dir, f"{analysis_id}-N1.png")
        fig.savefig(out_png, dpi=int(cfg.plots.get("dpi", 300)), bbox_inches="tight")
        plt.close(fig)
        print(f"Saved: {out_png}")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
