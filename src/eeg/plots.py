from __future__ import annotations

from typing import Dict, Iterable, Optional, Mapping, Tuple

import matplotlib

# Use non-interactive backend suitable for CI and headless runs
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def make_erp_figure(
    curves_by_label: Dict[str, Iterable[float]],
    times_ms,
    title: str,
    subtitle: Optional[str] = None,
    annotate_fallback: bool = False,
    colors: Optional[Mapping[str, str]] = None,
    linestyles: Optional[Mapping[str, str]] = None,
    xlim_ms: Optional[Tuple[float, float]] = None,
):
    """
    Create an ERP overlay figure.

    Args:
        curves_by_label: Dict mapping condition name to ERP curve array
        times_ms: Time points array in milliseconds
        title: Figure title
        subtitle: Optional subtitle
        annotate_fallback: Add fallback annotation text
        colors: Optional color mapping per condition
        linestyles: Optional linestyle mapping per condition
        xlim_ms: Optional (min, max) tuple to limit x-axis display range.
                 If None, shows full epoch range. If provided (e.g., from baseline_ms),
                 only shows time range from xlim_ms[0] to end of epoch.

    Returns:
        matplotlib Figure object
    """
    # Widen the ERP overlay by ~15% for better latency granularity
    fig, ax = plt.subplots(figsize=(6.9, 3.5), constrained_layout=True)
    for label, y in curves_by_label.items():
        kw = {}
        if colors and label in colors:
            kw["color"] = colors[label]
        if linestyles and label in linestyles:
            kw["linestyle"] = linestyles[label]
        ax.plot(times_ms, y, label=label, **kw)
    ax.axvline(0, color="#999", linewidth=1, alpha=0.6)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude (a.u.)")
    ax.set_title(title)

    # Set x-axis limits if requested (e.g., start from baseline onset)
    if xlim_ms is not None:
        ax.set_xlim(xlim_ms)

    # Avoid overlapping text at the top; use figure-level subtitle instead
    if subtitle:
        fig.suptitle(f"\n{subtitle}", fontsize=9, y=0.98)
    if annotate_fallback:
        ax.text(0.99, 0.02, "Fallback window used", transform=ax.transAxes, fontsize=8, va="bottom", ha="right")
    ax.legend(loc="best", fontsize=8)
    return fig


def make_component_figure(
    curves_by_label: Dict[str, Iterable[float]],
    times_ms,
    topomap_by_label: Dict[str, Tuple],  # Can be (vec, peak_ms, half_win) or (vec, peak_ms, half_win, used_fallback)
    info,
    title: str,
    subtitle: Optional[str] = None,
    colors: Optional[Mapping[str, str]] = None,
    linestyles: Optional[Mapping[str, str]] = None,
    xlim_ms: Optional[Tuple[float, float]] = None,
):
    """
    Create a composite figure with ERP overlay (top) and topomaps (bottom).

    Args:
        curves_by_label: Dict mapping condition name to ERP curve array
        times_ms: Time points array in milliseconds
        topomap_by_label: Dict mapping condition name to tuple:
            - (vec, peak_ms, half_win) for backward compatibility
            - (vec, peak_ms, half_win, used_fallback) for fallback annotation
        info: MNE Info object for topomap layout
        title: Figure title
        subtitle: Optional subtitle
        colors: Optional color mapping per condition
        linestyles: Optional linestyle mapping per condition
        xlim_ms: Optional (min, max) tuple to limit x-axis display range.
                 If None, shows full epoch range. If provided (e.g., from baseline_ms),
                 only shows time range from xlim_ms[0] to end of epoch.

    Returns:
        matplotlib Figure object
    """
    import mne  # local import for plotting

    n_cols = max(1, len(topomap_by_label) or 1)
    # Make the composite figure wider while keeping height the same
    fig = plt.figure(figsize=(7.475, 5.5), constrained_layout=True)
    gs = fig.add_gridspec(2, n_cols, height_ratios=[2.2, 1.8])

    # Check if any condition used fallback (for overlay annotation)
    any_fallback = False
    for tup in topomap_by_label.values():
        if len(tup) > 3 and tup[3]:  # Fourth element exists and is True
            any_fallback = True
            break

    # Overlay spanning top row
    ax_overlay = fig.add_subplot(gs[0, :])
    for label, y in curves_by_label.items():
        kw = {}
        if colors and label in colors:
            kw["color"] = colors[label]
        if linestyles and label in linestyles:
            kw["linestyle"] = linestyles[label]
        # If this specific label used fallback, add asterisk to legend
        display_label = label
        if label in topomap_by_label:
            tup = topomap_by_label[label]
            if len(tup) > 3 and tup[3]:  # used_fallback=True
                display_label = f"{label}*"
        ax_overlay.plot(times_ms, y, label=display_label, **kw)

    ax_overlay.axvline(0, color="#999", linewidth=1, alpha=0.6)

    # Mark peaks with light vertical lines using topomap peak times
    for label, tup in topomap_by_label.items():
        peak_ms = tup[1]  # Second element is always peak_ms
        vkw = {"color": (colors.get(label) if colors and label in colors else "#666"), "alpha": 0.25, "linestyle": "--"}
        ax_overlay.axvline(peak_ms, **vkw)

    ax_overlay.set_title(title)
    ax_overlay.set_xlabel("Time (ms)")
    ax_overlay.set_ylabel("Amplitude (a.u.)")

    # Set x-axis limits if requested (e.g., start from baseline onset)
    if xlim_ms is not None:
        ax_overlay.set_xlim(xlim_ms)

    # Add asterisk note to legend if any fallback used
    legend_title = "* = fallback window used" if any_fallback else None
    ax_overlay.legend(loc="best", fontsize=8, title=legend_title, title_fontsize=7)

    # Figure-level subtitle to avoid occlusion
    if subtitle:
        fig.suptitle(f"\n{subtitle}", fontsize=9, y=0.98)

    # Bottom row: topomaps per condition set
    for idx, (label, tup) in enumerate(sorted(topomap_by_label.items())):
        vec, peak_ms, half_win = tup[0], tup[1], tup[2]
        used_fallback = tup[3] if len(tup) > 3 else False

        ax = fig.add_subplot(gs[1, idx])
        mne.viz.plot_topomap(vec, info, axes=ax, contours=0, show=False)

        # Add asterisk to title if fallback was used and break long text into lines
        title_suffix = "*" if used_fallback else ""
        ax.set_title(f"{label}{title_suffix}\nPeak {peak_ms} ms\n(±{half_win} ms)", fontsize=8)

    return fig


def make_collapsed_localizer_figure(
    localizer_results: Dict[str, Dict],
    title: str = "Collapsed Localizer (GFP-based)",
    subtitle: Optional[str] = None,
    xlim_ms: Optional[Tuple[float, float]] = None,
):
    """
    Create collapsed localizer figure using Global Field Power (GFP) approach.

    This plot provides scientific justification for time window selection by showing:
    - GFP trace (standard deviation across ALL channels)
    - Detected peak within a priori search range (red dashed line)
    - FWHM window (shaded region) - data-driven window width
    - Search range boundaries (dotted lines)

    This approach is unbiased, transparent, and prevents circular analysis.

    Args:
        localizer_results: Dict mapping component name to GFP analysis results dict:
            - 'gfp': GFP array (n_times,)
            - 'times_ms': Time points in milliseconds
            - 'peak_latency_ms': Peak latency
            - 'window_start_ms': FWHM window start
            - 'window_end_ms': FWHM window end
            - 'fwhm_ms': FWHM duration
            - 'search_range_ms': A priori search range tuple
        title: Figure title
        subtitle: Optional subtitle explaining baseline and parameters
        xlim_ms: Optional (min, max) tuple to limit x-axis display range

    Returns:
        matplotlib Figure object

    Example:
        >>> results = compute_all_collapsed_localizers(evokeds_by_set, components_config)
        >>> fig = make_collapsed_localizer_figure(results)
        >>> fig.savefig('collapsed_localizer.png', dpi=300)
    """
    import numpy as np

    n_components = len(localizer_results)
    if n_components == 0:
        raise ValueError("No localizer results to plot")

    # Create subplots: one per component
    fig, axes = plt.subplots(
        n_components, 1,
        figsize=(8.5, 2.8 * n_components),
        constrained_layout=True,
        squeeze=False  # Always return 2D array
    )
    axes = axes.flatten()

    for idx, (comp, result) in enumerate(sorted(localizer_results.items())):
        # Extract GFP results
        gfp = result['gfp']
        times_ms = result['times_ms']
        peak_lat = result['peak_latency_ms']
        window_start = result['window_start_ms']
        window_end = result['window_end_ms']
        fwhm = result['fwhm_ms']
        search_range = result['search_range_ms']

        ax = axes[idx]

        # Plot GFP trace
        ax.plot(times_ms, gfp, label="GFP (all channels)", color="#2c7bb6", linewidth=2.0, zorder=3)

        # Shade FWHM window
        ax.axvspan(window_start, window_end, alpha=0.2, color="#d7191c",
                   label=f"FWHM window ({fwhm:.1f} ms)", zorder=1)

        # Mark stimulus onset
        ax.axvline(0, color="#666", linewidth=1, alpha=0.5, linestyle="-",
                   label="Stimulus onset", zorder=2)

        # Mark detected peak
        ax.axvline(peak_lat, color="#d7191c", linewidth=2, linestyle="--",
                   label=f"Peak: {peak_lat} ms", zorder=4)

        # Mark a priori search range boundaries
        ax.axvline(search_range[0], color="#999", linewidth=1, alpha=0.4, linestyle=":",
                   zorder=2)
        ax.axvline(search_range[1], color="#999", linewidth=1, alpha=0.4, linestyle=":",
                   label=f"Search range: [{search_range[0]}, {search_range[1]}] ms", zorder=2)

        # Styling
        ax.set_xlabel("Time (ms)", fontsize=10)
        ax.set_ylabel("GFP (µV)", fontsize=10)
        ax.set_title(f"{comp} Component", fontsize=11, loc="left", fontweight="bold")

        if xlim_ms is not None:
            ax.set_xlim(xlim_ms)

        ax.legend(loc="best", fontsize=8, framealpha=0.9)
        ax.grid(True, alpha=0.3, linewidth=0.5)

        # Add annotation box with key metrics
        metrics_text = (
            f"Peak GFP: {result['peak_amplitude']:.2f} µV\n"
            f"FWHM: {fwhm:.1f} ms\n"
            f"Window: [{window_start:.1f}, {window_end:.1f}] ms"
        )
        ax.text(0.98, 0.97, metrics_text,
                transform=ax.transAxes,
                fontsize=7,
                va="top", ha="right",
                bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                         edgecolor="#2c7bb6", alpha=0.8))

    # Overall title
    fig.suptitle(title, fontsize=13, fontweight="bold")

    # Subtitle at bottom
    if subtitle:
        fig.text(0.5, 0.01, subtitle, ha="center", fontsize=9, style="italic")

    return fig


