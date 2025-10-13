#!/usr/bin/env python
"""Run YAML-driven ERP analysis using GFP-based collapsed localizer.

This script implements scientifically rigorous ERP component analysis:
1. Collapsed localizer: Average ALL conditions to find component peaks
2. Global Field Power (GFP): Use all channels, not hand-picked ROIs
3. FWHM windows: Data-driven window widths from Full Width at Half Maximum
4. No fallbacks: Errors raised if components cannot be detected (transparency)

This prevents circular analysis and ensures reproducible, defensible results.
"""
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

from eeg.config import load_config, load_components_config, load_electrodes_config
from eeg.plots import make_collapsed_localizer_figure, make_component_figure, make_erp_figure
from eeg.report import write_analysis_page, ensure_index_template, update_index_grid
from eeg.io import discover_epoch_files, read_epochs, apply_montage, validate_baseline_window, extract_subject_id
from eeg.collapsed_localizer import compute_collapsed_localizer, compute_collapsed_localizer_roi
from eeg.measures import mean_amplitude, fractional_area_latency
import matplotlib.pyplot as plt
import mne


def main() -> int:
    parser = argparse.ArgumentParser(description="Run GFP-based ERP analysis")
    parser.add_argument("--config", required=True, help="Path to analysis YAML")
    args = parser.parse_args()

    # Determinism: ensure any incidental randomness is fixed for reproducibility
    np.random.seed(0)
    t_start = time.perf_counter()

    cfg = load_config(args.config)

    # Ensure output directories exist
    plots_dir = cfg.outputs.get("plots_dir")
    tables_dir = cfg.outputs.get("tables_dir")
    page_path = cfg.outputs.get("page")

    if not plots_dir or not tables_dir or not page_path:
        raise SystemExit("Config outputs must include plots_dir, tables_dir, and page")

    os.makedirs(plots_dir, exist_ok=True)
    os.makedirs(tables_dir, exist_ok=True)
    os.makedirs(os.path.dirname(page_path), exist_ok=True)

    # Load component and electrode configuration
    repo_root = REPO_ROOT
    components_cfg = load_components_config(repo_root)
    electrodes_cfg = load_electrodes_config(repo_root)

    # Discover data files
    fif_files = discover_epoch_files(
        root=os.path.join(repo_root, cfg.dataset.get("root", "data")),
        pattern=cfg.dataset.get("pattern", "**/*.fif"),
    )

    analysis_id = os.path.splitext(os.path.basename(page_path))[0]
    saved_figs = []

    # Handle no-data case with synthetic placeholder
    if len(fif_files) == 0:
        print(f"Warning: No FIF files found. Analysis '{analysis_id}' cannot proceed.")
        print("Please ensure data files are present in the configured location.")
        # Create empty page
        write_analysis_page(
            page_path,
            title=analysis_id,
            figure_paths=[],
            notes=["No FIF files found; analysis could not be completed."]
        )
        return 1

    # === Real Analysis Pipeline ===
    print(f"\n{'='*60}")
    print(f"Running GFP-based analysis: {analysis_id}")
    print(f"{'='*60}\n")

    baseline = tuple(cfg.preprocessing.get("baseline_ms", [-100, 0]))
    response = str(cfg.selection.get("response", "ALL")).upper()
    sets = cfg.selection.get("condition_sets", [])

    print(f"Configuration:")
    print(f"  Baseline: {baseline} ms")
    print(f"  Response filter: {response}")
    print(f"  Condition sets: {[s['name'] for s in sets]}")
    print(f"  Components: {cfg.components}")
    print(f"  Subjects found: {len(fif_files)}\n")

    # Collect subject-level evoked responses per condition set
    set_name_to_evokeds = {s["name"]: [] for s in sets}
    qc_rows = []

    # === Phase 2A: Subject-level measurements collection ===
    subject_measurements = []  # NEW: For statistical analysis

    print("Loading and preprocessing subjects...")
    for fif_idx, fif in enumerate(fif_files, 1):
        epochs = read_epochs(fif)
        apply_montage(epochs, cfg.dataset.get("montage_sfp"))

        # Baseline correction
        bl = (baseline[0] / 1000.0, baseline[1] / 1000.0)
        validate_baseline_window(epochs, baseline)

        # Response filtering (ACC1 or ALL)
        if response == "ACC1":
            if getattr(epochs, "metadata", None) is None or "Target.ACC" not in epochs.metadata.columns:
                continue
            epochs = epochs[epochs.metadata["Target.ACC"] == 1]

        epochs.apply_baseline(bl)
        subj_id = extract_subject_id(epochs, fif)

        # Process each condition set
        for item in sets:
            name = item["name"]
            codes = [str(c) for c in item.get("conditions", [])]

            # Select epochs by condition codes
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
                    qc_rows.append({
                        "subject": subj_id,
                        "set": name,
                        "included": False,
                        "epoch_count": 0,
                        "exclusion_reason": "no_matching_conditions",
                    })
                    continue

            # Check minimum epochs threshold
            epoch_count = int(len(sub))
            min_epochs = int(cfg.selection.get("min_epochs_per_set", 1))
            if epoch_count < min_epochs:
                qc_rows.append({
                    "subject": subj_id,
                    "set": name,
                    "included": False,
                    "epoch_count": epoch_count,
                    "exclusion_reason": f"insufficient_epochs(<{min_epochs})",
                })
                continue

            # Compute subject-level evoked and store
            evk = sub.average()
            set_name_to_evokeds[name].append(evk)

            qc_rows.append({
                "subject": subj_id,
                "set": name,
                "included": True,
                "epoch_count": epoch_count,
                "exclusion_reason": "",
            })

            # === Phase 2A: Store evoked and metadata for later subject-level measurements ===
            # We'll process these after collapsed localizer is computed
            # Store: (subject_id, condition_name, evoked, epoch_count)
            subject_measurements.append({
                'subject_id': subj_id,
                'condition': name,
                'evoked': evk,
                'n_epochs': epoch_count,
            })

        if fif_idx % 5 == 0:
            print(f"  Processed {fif_idx}/{len(fif_files)} subjects...")

    print(f"  Completed! Processed {len(fif_files)} subjects.\n")

    # Check if we have any data
    total_evokeds = sum(len(evks) for evks in set_name_to_evokeds.values())
    if total_evokeds == 0:
        print("ERROR: No subjects passed inclusion criteria.")
        print("Please check your condition codes and min_epochs_per_set settings.")
        write_analysis_page(
            page_path,
            title=analysis_id,
            figure_paths=[],
            notes=["No subjects met inclusion criteria."]
        )
        return 1

    # === Collapsed Localizer (ROI default) ===
    print("Computing collapsed localizer...")
    print("(Averaging ALL conditions to find unbiased component peaks)\n")

    # Compute collapsed localizer per component so failures don't abort the run
    collapsed_results = {}
    failed_components = []
    for comp in cfg.components:
        comp_cfg = components_cfg.get(comp, {})
        sr = comp_cfg.get("window_ms")
        if not sr or len(sr) != 2:
            print(f"  Skipping {comp}: invalid search range in components.yaml -> {sr}")
            failed_components.append(comp)
            continue
        try:
            # Determine localizer method (default ROI)
            loc_cfg = comp_cfg.get("localizer", {}) if isinstance(comp_cfg, dict) else {}
            method = str(loc_cfg.get("method", "roi")).lower()
            if method not in ("roi", "gfp"):
                method = "roi"

            if method == "roi":
                roi_names = loc_cfg.get("roi_names") or comp_cfg.get("rois") or []
                roi_channels = []
                for rn in roi_names:
                    if rn in electrodes_cfg:
                        roi_channels.extend(electrodes_cfg[rn])
                if not roi_channels:
                    raise ValueError(f"No ROI channels found for ROI localizer ({comp})")
                polarity = str(loc_cfg.get("polarity", ("negative" if comp.upper().startswith("N") else "positive")))
                res = compute_collapsed_localizer_roi(
                    evokeds_by_set=set_name_to_evokeds,
                    roi_channels=roi_channels,
                    component_name=comp,
                    search_range_ms=tuple(sr),
                    polarity=polarity,
                )
            else:
                res = compute_collapsed_localizer(
                    evokeds_by_set=set_name_to_evokeds,
                    component_name=comp,
                    search_range_ms=tuple(sr),
                )
            collapsed_results[comp] = res
            print(
                f"  {comp}: peak at {res['peak_latency_ms']} ms, FWHM window "
                f"[{res['window_start_ms']:.1f}, {res['window_end_ms']:.1f}] ms "
                f"(width: {res['fwhm_ms']:.1f} ms)"
            )
        except ValueError as e:
            print(f"  Warning: {comp} collapsed localizer failed: {e}")
            failed_components.append(comp)

    if collapsed_results:
        print(f"\nCollapsed localizer completed successfully for: {list(collapsed_results.keys())}\n")
    else:
        print("\nERROR: Collapsed localizer failed for all requested components; aborting.")
        return 1

    # Generate collapsed localizer plot
    first_evoked = list(set_name_to_evokeds.values())[0][0]
    epoch_end_ms = float(first_evoked.times[-1] * 1000.0)
    xlim_ms = (baseline[0], epoch_end_ms)

    cl_fig = make_collapsed_localizer_figure(
        localizer_results=collapsed_results,
        title=f"{analysis_id}: Collapsed Localizer",
        subtitle=f"baseline {baseline} ms; collapsed across all conditions; FWHM windows",
        xlim_ms=xlim_ms,
    )
    cl_out_path = os.path.join(plots_dir, f"{analysis_id}-collapsed_localizer.png")
    cl_fig.savefig(cl_out_path, dpi=int(cfg.plots.get("dpi", 300)))
    plt.close(cl_fig)
    saved_figs.append(cl_out_path)

    print(f"Saved collapsed localizer plot: {os.path.basename(cl_out_path)}\n")

    # === Phase 2A: Process Subject-Level Measurements ===
    print("Computing subject-level measurements (Phase 2A)...")
    subject_measurements_output = []  # Final output records

    for subj_data in subject_measurements:
        subj_id = subj_data['subject_id']
        condition = subj_data['condition']
        evoked = subj_data['evoked']
        n_epochs = subj_data['n_epochs']

        times_ms_subj = evoked.times * 1000.0

        # Extract baseline data for QC metrics
        baseline_mask = (times_ms_subj >= baseline[0]) & (times_ms_subj <= baseline[1])

        for comp in cfg.components:
            comp_result = collapsed_results.get(comp)
            if comp_result is None:
                continue  # Skip components that failed localizer

            # Get measurement window from collapsed localizer
            peak_lat = comp_result['peak_latency_ms']
            window_start = comp_result['window_start_ms']
            window_end = comp_result['window_end_ms']
            fwhm = comp_result['fwhm_ms']

            # Get ROI channels
            comp_cfg = components_cfg.get(comp, {})
            roi_names = comp_cfg.get('rois', [])
            roi_channels = []
            for roi_name in roi_names:
                if roi_name in electrodes_cfg:
                    roi_channels.extend(electrodes_cfg[roi_name])

            if not roi_channels:
                continue

            try:
                # Extract subject ROI curve
                roi_data = evoked.copy().pick_channels(roi_channels, ordered=False)
                roi_curve = roi_data.data.mean(axis=0) * 1e6  # Convert to µV

                # === QC Metric 1: Baseline Noise ===
                baseline_roi = roi_curve[baseline_mask]
                baseline_noise_uv = float(np.std(baseline_roi))

                # === Measurement 1: Mean Amplitude ===
                window_mask = (times_ms_subj >= window_start) & (times_ms_subj <= window_end)
                subj_mean_amp = float(np.mean(roi_curve[window_mask]))

                # === QC Metric 2: Signal-to-Noise Ratio ===
                snr = abs(subj_mean_amp) / baseline_noise_uv if baseline_noise_uv > 0 else float('nan')

                # === Measurement 2: Fractional Area Latency ===
                comp_polarity = "negative" if comp.upper().startswith("N") else "positive"
                try:
                    subj_fal = fractional_area_latency(
                        signal=roi_curve,
                        times_ms=times_ms_subj,
                        window_ms=(window_start, window_end),
                        fraction=0.5,
                        polarity=comp_polarity
                    )
                except Exception as e:
                    subj_fal = float('nan')

                # Record subject measurement with QC metrics
                subject_measurements_output.append({
                    "subject_id": subj_id,
                    "component": comp,
                    "condition": condition,
                    "latency_frac_area_ms": subj_fal,
                    "mean_amplitude_roi": subj_mean_amp,
                    "n_epochs": n_epochs,
                    "baseline_noise_uv": baseline_noise_uv,
                    "snr": snr,
                    "peak_latency_ms": float(peak_lat),
                    "window_start_ms": float(window_start),
                    "window_end_ms": float(window_end),
                    "fwhm_ms": float(fwhm),
                })

            except Exception as e:
                # Record NaN for failed measurement
                subject_measurements_output.append({
                    "subject_id": subj_id,
                    "component": comp,
                    "condition": condition,
                    "latency_frac_area_ms": float('nan'),
                    "mean_amplitude_roi": float('nan'),
                    "n_epochs": n_epochs,
                    "baseline_noise_uv": float('nan'),
                    "snr": float('nan'),
                    "peak_latency_ms": float(peak_lat),
                    "window_start_ms": float(window_start),
                    "window_end_ms": float(window_end),
                    "fwhm_ms": float(fwhm),
                })

    # Save subject-level measurements
    if subject_measurements_output:
        import csv
        subj_csv_path = os.path.join(tables_dir, "subject_measurements.csv")
        fieldnames = [
            "subject_id", "component", "condition",
            "latency_frac_area_ms", "mean_amplitude_roi",
            "n_epochs", "baseline_noise_uv", "snr",
            "peak_latency_ms", "window_start_ms", "window_end_ms", "fwhm_ms"
        ]
        with open(subj_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(subject_measurements_output)

        print(f"Saved subject-level measurements: {os.path.basename(subj_csv_path)}")
        print(f"  Recorded {len(subject_measurements_output)} subject-component-condition measurements\n")

    # === Per-Condition Analysis (using GFP-derived windows) ===
    print("Generating per-condition analyses...")
    print("(Using FWHM windows from collapsed localizer)\n")

    # For each component, generate ERP overlays with topomaps using GFP-derived windows
    saved_figs_map = {}  # component -> absolute path

    # Data recording for statistical analysis
    condition_measurements = []  # List of dicts for CSV export

    for comp in cfg.components:
        if comp not in collapsed_results:
            print(f"  {comp}: No GFP window detected; generating ERP overlay only (no topomaps).")

        # Get GFP-derived window for this component if available
        comp_result = collapsed_results.get(comp)
        if comp_result is not None:
            peak_lat = comp_result['peak_latency_ms']
            window_start = comp_result['window_start_ms']
            window_end = comp_result['window_end_ms']
            fwhm = comp_result['fwhm_ms']
            print(
                f"  Processing {comp}: peak {peak_lat} ms, FWHM window "
                f"[{window_start:.1f}, {window_end:.1f}] ms"
            )
        else:
            peak_lat = None
            window_start = None
            window_end = None
            fwhm = None

        # Get ROI channels for this component
        comp_cfg = components_cfg.get(comp, {})
        roi_names = comp_cfg.get('rois', [])

        # Collect all electrode labels for ROIs
        roi_channels = []
        for roi_name in roi_names:
            if roi_name in electrodes_cfg:
                roi_channels.extend(electrodes_cfg[roi_name])

        if not roi_channels:
            print(f"    Warning: No ROI channels found for {comp}, skipping component plot")
            continue

        # Compute grand average for each condition set
        curves_by_label = {}
        topomap_by_label = {}
        times_ms = None
        gav_info = None

        for set_name, evoked_list in set_name_to_evokeds.items():
            if len(evoked_list) == 0:
                continue

            # Grand average across subjects
            gav = mne.grand_average(evoked_list)

            if times_ms is None:
                times_ms = (gav.times * 1000.0).astype(float)
                gav_info = gav.info

            # Extract ROI channels and average in microvolts
            try:
                roi_data = gav.copy().pick_channels(roi_channels, ordered=False)
                roi_curve = roi_data.data.mean(axis=0) * 1e6
                curves_by_label[set_name] = roi_curve
            except Exception as e:
                print(f"    Warning: Could not extract ROI channels for {set_name}: {e}")
                continue

            if comp_result is not None:
                # === STEP 1: Compute FAL for this condition ===
                # This provides a robust measure of component timing, less sensitive to noise
                # than peak latency. The 50% fractional area represents the temporal midpoint.
                try:
                    # Determine polarity from component name (N* = negative, P* = positive)
                    comp_polarity = "negative" if comp.upper().startswith("N") else "positive"

                    roi_latency_frac_area = fractional_area_latency(
                        signal=roi_curve,
                        times_ms=times_ms,
                        window_ms=(window_start, window_end),
                        fraction=0.5,
                        polarity=comp_polarity
                    )
                except Exception as e:
                    # If FAL computation fails, use collapsed peak as fallback
                    print(f"    Warning: FAL failed for {set_name} {comp}, using collapsed peak: {e}")
                    roi_latency_frac_area = float(peak_lat)

                # === STEP 2: Extract topomap using FAL-centered window (±FWHM/2) ===
                half_win_ms = fwhm / 2.0
                topo_start = (roi_latency_frac_area - half_win_ms) / 1000.0
                topo_end = (roi_latency_frac_area + half_win_ms) / 1000.0

                try:
                    evk_win = gav.copy().crop(tmin=topo_start, tmax=topo_end)
                    # Topomap vector in microvolts (averaged over FAL-centered window)
                    mean_vec = evk_win.data.mean(axis=1) * 1e6
                    # Store: (vector, FAL_latency, half_window, used_fallback)
                    topomap_by_label[set_name] = (mean_vec, roi_latency_frac_area, int(half_win_ms), False)

                    # Record amplitude measurement for statistical analysis
                    roi_mean_amplitude = float(np.mean(roi_curve[(times_ms >= window_start) & (times_ms <= window_end)]))

                    condition_measurements.append({
                        "analysis_id": analysis_id,
                        "component": comp,
                        "condition": set_name,
                        "n_subjects": len(evoked_list),
                        "peak_latency_ms": float(peak_lat),
                        "window_start_ms": float(window_start),
                        "window_end_ms": float(window_end),
                        "fwhm_ms": float(fwhm),
                        "mean_amplitude_roi": roi_mean_amplitude,
                        "latency_frac_area_ms": roi_latency_frac_area,
                        "roi_channels": ";".join(roi_channels),
                    })
                except Exception as e:
                    print(f"    Warning: Could not extract topomap for {set_name}: {e}")
                    continue

        # Generate component figure
        if curves_by_label and topomap_by_label and times_ms is not None and gav_info is not None:
            # === NEW: Build condition_name -> config dict for easy lookup ===
            condition_config_map = {item["name"]: item for item in sets}

            # Prepare color configuration
            color_list = cfg.plots.get("colors") or []
            colors = {label: color_list[i % len(color_list)] for i, label in enumerate(sorted(curves_by_label.keys()))} if color_list else None

            # Apply semantic color rules: increasing=green, decreasing=red
            # (matplotlib default colors, colorblind-friendly)
            def _color_for(label: str, default_color: str) -> str:
                # PRIORITY 1: Explicit color in YAML config overrides everything
                if label in condition_config_map and "color" in condition_config_map[label]:
                    return condition_config_map[label]["color"]

                # PRIORITY 2: Semantic rules (increasing=green, decreasing=red)
                lower = label.lower()
                if "increasing" in lower:
                    return "#2ca02c"  # Green
                if "decreasing" in lower:
                    return "#d62728"  # Red

                # PRIORITY 3: Color list from cfg.plots.colors
                return default_color

            if colors:
                colors = {label: _color_for(label, colors[label]) for label in colors}

            # Dynamic linestyle rules by label text
            styles_cfg = cfg.plots.get("linestyles") or {}
            linestyles = {k: v for k, v in styles_cfg.items()}
            def _style_for(label: str) -> str:
                # PRIORITY 1: Explicit linestyle in YAML config overrides everything
                if label in condition_config_map and "linestyle" in condition_config_map[label]:
                    return condition_config_map[label]["linestyle"]

                # PRIORITY 2: Semantic rules
                lower = label.lower()
                if "cardinality" in lower:
                    return "-"
                if "decreasing" in lower:
                    return ":"
                if "increasing" in lower:
                    return "--"

                # PRIORITY 3: Fall back to cfg.plots.linestyles or solid
                return linestyles.get(label, "-")
            # Apply rules
            linestyles = {label: _style_for(label) for label in curves_by_label.keys()}

            # Set x-axis limits to start from baseline onset
            xlim_ms = (baseline[0], float(times_ms[-1]))

            # === NEW: Extract FAL values from condition_measurements for plotting ===
            latencies_by_label = {}
            for meas in condition_measurements:
                if meas['component'] == comp and not np.isnan(meas['latency_frac_area_ms']):
                    latencies_by_label[meas['condition']] = meas['latency_frac_area_ms']

            fig = make_component_figure(
                curves_by_label=curves_by_label,
                times_ms=times_ms,
                topomap_by_label=topomap_by_label,
                info=gav_info,
                title=f"{analysis_id}: {comp} ({response})",
                subtitle=f"baseline {baseline} ms; GFP-derived FWHM window: [{window_start:.1f}, {window_end:.1f}] ms",
                colors=colors,
                linestyles=linestyles,
                xlim_ms=xlim_ms,
                latencies_by_label=latencies_by_label,  # NEW: Pass FAL data to plotting
            )

            out_path = os.path.join(plots_dir, f"{analysis_id}-{comp}.png")
            fig.savefig(out_path, dpi=int(cfg.plots.get("dpi", 300)), bbox_inches="tight")
            plt.close(fig)
            saved_figs.append(out_path)
            saved_figs_map[comp] = out_path

            print(f"    Saved: {os.path.basename(out_path)}")
        elif curves_by_label and times_ms is not None:
            # Overlay-only ERP figure (no topomaps, no dashed GFP lines)
            # === NEW: Build condition_name -> config dict for easy lookup ===
            condition_config_map = {item["name"]: item for item in sets}

            color_list = cfg.plots.get("colors") or []
            colors = {label: color_list[i % len(color_list)] for i, label in enumerate(sorted(curves_by_label.keys()))} if color_list else None

            # Apply semantic color rules: increasing=green, decreasing=red
            # (matplotlib default colors, colorblind-friendly)
            def _color_for(label: str, default_color: str) -> str:
                # PRIORITY 1: Explicit color in YAML config overrides everything
                if label in condition_config_map and "color" in condition_config_map[label]:
                    return condition_config_map[label]["color"]

                # PRIORITY 2: Semantic rules
                lower = label.lower()
                if "increasing" in lower:
                    return "#2ca02c"  # Green
                if "decreasing" in lower:
                    return "#d62728"  # Red

                # PRIORITY 3: Color list
                return default_color

            if colors:
                colors = {label: _color_for(label, colors[label]) for label in colors}

            styles_cfg = cfg.plots.get("linestyles") or {}
            base_linestyles = {k: v for k, v in styles_cfg.items()}
            def _style_for(label: str) -> str:
                # PRIORITY 1: Explicit linestyle in YAML config overrides everything
                if label in condition_config_map and "linestyle" in condition_config_map[label]:
                    return condition_config_map[label]["linestyle"]

                # PRIORITY 2: Semantic rules
                lower = label.lower()
                if "cardinality" in lower:
                    return "-"
                if "decreasing" in lower:
                    return ":"
                if "increasing" in lower:
                    return "--"

                # PRIORITY 3: Fall back to cfg.plots.linestyles or solid
                return base_linestyles.get(label, "-")
            linestyles = {label: _style_for(label) for label in curves_by_label.keys()}
            xlim_ms = (baseline[0], float(times_ms[-1]))
            fig = make_erp_figure(
                curves_by_label=curves_by_label,
                times_ms=times_ms,
                title=f"{analysis_id}: {comp} ({response})",
                subtitle=f"baseline {baseline} ms; GFP window unavailable",
                colors=colors,
                linestyles=linestyles,
                xlim_ms=xlim_ms,
            )
            out_path = os.path.join(plots_dir, f"{analysis_id}-{comp}.png")
            fig.savefig(out_path, dpi=int(cfg.plots.get("dpi", 300)), bbox_inches="tight")
            plt.close(fig)
            saved_figs.append(out_path)
            saved_figs_map[comp] = out_path
            print(f"    Saved (ERP only): {os.path.basename(out_path)}")
        else:
            print(f"    Warning: Insufficient data to generate ERP for {comp}")

    print()

    # === Save Scientific Measurements ===
    # Save collapsed localizer results (component-level GFP measurements)
    import datetime
    collapsed_localizer_data = {
        "analysis_id": analysis_id,
        "date_analyzed": datetime.datetime.now().isoformat(),
        "baseline_ms": list(baseline),
        "response_filter": response,
        "fal_fraction": 0.5,  # Fractional area latency: 50% = temporal midpoint
        "n_subjects_total": len(fif_files),
        "n_evokeds_included": total_evokeds,
        "conditions": [s["name"] for s in sets],
        "components": {}
    }

    for comp, result in collapsed_results.items():
        collapsed_localizer_data["components"][comp] = {
            "peak_latency_ms": float(result['peak_latency_ms']),
            "peak_gfp_amplitude": float(result['peak_amplitude']),
            "fwhm_ms": float(result['fwhm_ms']),
            "window_start_ms": float(result['window_start_ms']),
            "window_end_ms": float(result['window_end_ms']),
            "search_range_ms": [float(x) for x in result['search_range_ms']],
            "method": "GFP_collapsed_localizer",
            "n_subjects": int(result['n_subjects']),
            "n_conditions": int(result['n_conditions']),
        }

    collapsed_json_path = os.path.join(tables_dir, "collapsed_localizer_results.json")
    with open(collapsed_json_path, "w", encoding="utf-8") as f:
        json.dump(collapsed_localizer_data, f, indent=2)

    print(f"Saved collapsed localizer results: {os.path.basename(collapsed_json_path)}")

    # Save per-condition measurements (for statistical analysis)
    if condition_measurements:
        import csv
        measurements_csv_path = os.path.join(tables_dir, "condition_measurements.csv")
        fieldnames = [
            "analysis_id", "component", "condition", "n_subjects",
            "peak_latency_ms", "window_start_ms", "window_end_ms", "fwhm_ms",
            "mean_amplitude_roi", "latency_frac_area_ms", "roi_channels"
        ]
        with open(measurements_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(condition_measurements)

        print(f"Saved condition measurements: {os.path.basename(measurements_csv_path)}")
        print(f"  Recorded {len(condition_measurements)} condition-component measurements\n")

    # Write analysis page
    notes = []
    notes.append(f"GFP-based collapsed localizer analysis with {total_evokeds} subject-condition combinations.")
    notes.append(f"Components analyzed: {', '.join(cfg.components)}")

    for comp, result in collapsed_results.items():
        notes.append(
            f"{comp}: Peak at {result['peak_latency_ms']} ms, "
            f"FWHM window [{result['window_start_ms']:.1f}, {result['window_end_ms']:.1f}] ms "
            f"(width: {result['fwhm_ms']:.1f} ms)"
        )

    write_analysis_page(page_path, title=analysis_id, figure_paths=saved_figs, notes=notes)

    # Update index
    index_path = os.path.join(repo_root, "docs", "index.md")
    ensure_index_template(index_path)

    # Map components to their figure paths (use per-component figures if available)
    comp_to_img = {}
    for comp in cfg.components:
        if comp in saved_figs_map:
            # Use per-component figure
            rel = os.path.relpath(saved_figs_map[comp], os.path.join(repo_root, "docs")).replace("\\", "/")
        else:
            # Fallback to collapsed localizer
            rel = os.path.relpath(cl_out_path, os.path.join(repo_root, "docs")).replace("\\", "/")
        comp_to_img[comp] = rel

    update_index_grid(index_path, analysis_id, comp_to_img)

    # Metrics
    duration_s = time.perf_counter() - t_start
    sizes = {os.path.basename(p): os.path.getsize(p) for p in saved_figs if os.path.isfile(p)}
    largest = max(sizes.values()) if sizes else 0
    total = int(sum(sizes.values())) if sizes else 0

    metrics = {
        "analysis_id": analysis_id,
        "duration_seconds": round(duration_s, 3),
        "num_figures": len(saved_figs),
        "largest_png_bytes": largest,
        "total_png_bytes": total,
        "largest_png_ok": bool(largest <= 2 * 1024 * 1024),
        "cumulative_png_ok": bool(total <= 20 * 1024 * 1024),
        "figures": sizes,
    }

    with open(os.path.join(tables_dir, "run_metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    # QC CSV
    if qc_rows:
        import csv
        with open(os.path.join(tables_dir, "qc_summary.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["subject", "set", "included", "epoch_count", "exclusion_reason"])
            writer.writeheader()
            writer.writerows(qc_rows)

    print(f"\n{'='*60}")
    print(f"Analysis completed in {duration_s:.2f} seconds")
    print(f"Output: {page_path}")
    print(f"Figures: {len(saved_figs)} plots ({total/1024:.1f} KB total)")
    print(f"{'='*60}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
