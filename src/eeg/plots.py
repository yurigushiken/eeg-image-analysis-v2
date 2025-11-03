from __future__ import annotations

from typing import Dict, Iterable, Optional, Mapping, Tuple, List

import matplotlib

# Use non-interactive backend suitable for CI and headless runs
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def _generate_acronym_footnote(
    subtitle: str = "",
    caption: str = "",
    latency_annotation_label: str = "FAL"
) -> str:
    """
    Generate acronym definitions footnote based on what appears in the plot.

    Only includes acronyms that actually appear in the subtitle or caption text.
    This ensures plots are self-documenting without unnecessary clutter.

    Parameters
    ----------
    subtitle : str
        The subtitle text containing potential acronyms
    caption : str
        The caption text containing potential acronyms
    latency_annotation_label : str
        The latency measure being used ("FAL" or "Peak")

    Returns
    -------
    str
        Footnote string with relevant acronym definitions, or empty string

    Examples
    --------
    >>> _generate_acronym_footnote("ROI-derived FWHM window", "ERP ROI electrodes", "FAL")
    'ROI = Region of Interest; FWHM = Full Width at Half Maximum; FAL = 50% Fractional Area Latency; ERP = Event-Related Potential'

    >>> _generate_acronym_footnote("GFP-derived FWHM window", "", "Peak")
    'GFP = Global Field Power; FWHM = Full Width at Half Maximum'
    """
    combined_text = f"{subtitle} {caption}".upper()

    acronyms = []

    # Check which acronyms appear in this plot
    if "ROI" in combined_text:
        acronyms.append("ROI = Region of Interest")

    if "FWHM" in combined_text:
        acronyms.append("FWHM = Full Width at Half Maximum")

    if "FAL" in combined_text and latency_annotation_label == "FAL":
        acronyms.append("FAL = 50% Fractional Area Latency")

    if "GFP" in combined_text:
        acronyms.append("GFP = Global Field Power")

    if "ERP" in combined_text:
        acronyms.append("ERP = Event-Related Potential")

    # Return formatted footnote or empty string
    if acronyms:
        return "; ".join(acronyms)
    else:
        return ""


def make_erp_figure(
    curves_by_label: Dict[str, Iterable[float]],
    times_ms,
    title: str,
    subtitle: Optional[str] = None,
    annotate_fallback: bool = False,
    colors: Optional[Mapping[str, str]] = None,
    linestyles: Optional[Mapping[str, str]] = None,
    xlim_ms: Optional[Tuple[float, float]] = None,
    ylimit_uv: Optional[float] = None,
    epochs_by_label: Optional[Mapping[str, int]] = None,
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
    # Increased height for better vertical visibility
    fig, ax = plt.subplots(figsize=(6.9, 5.5), constrained_layout=True)
    # Increase padding between suptitle and axes to avoid overlap
    try:
        fig.set_constrained_layout_pads(h_pad=0.35, hspace=0.35, w_pad=0.14, wspace=0.22)
    except Exception:
        pass
    for label, y in curves_by_label.items():
        kw = {}
        if colors and label in colors:
            kw["color"] = colors[label]
        if linestyles and label in linestyles:
            kw["linestyle"] = linestyles[label]
        legend_label = label
        try:
            if epochs_by_label and label in epochs_by_label:
                legend_label = f"{legend_label} [{int(epochs_by_label[label])} epochs]"
        except Exception:
            pass
        ax.plot(times_ms, y, label=legend_label, **kw)
    ax.axvline(0, color="#999", linewidth=1, alpha=0.6)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude (µV)")
    # Use figure-level title to keep consistent placement across figures
    if title:
        try:
            fig.suptitle(title, fontsize=12, fontweight="bold", y=0.98)
        except Exception:
            pass

    # Set x-axis limits if requested (e.g., start from baseline onset)
    if xlim_ms is not None:
        ax.set_xlim(xlim_ms)

    # Set fixed y-axis limits if requested (e.g., ±6 µV)
    if ylimit_uv is not None:
        try:
            ax.set_ylim((-float(ylimit_uv), float(ylimit_uv)))
        except Exception:
            pass

    # Light gridlines to aid visual alignment
    try:
        from matplotlib.ticker import MultipleLocator, AutoMinorLocator
        ax.xaxis.set_major_locator(MultipleLocator(100))  # 100 ms major ticks
        ax.xaxis.set_minor_locator(MultipleLocator(50))   # 50 ms minor ticks
        ax.yaxis.set_major_locator(MultipleLocator(1))    # 1 µV major ticks (all integers labeled)
    except Exception:
        pass
    ax.grid(True, which="major", linestyle=":", linewidth=0.5, alpha=0.3)
    ax.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.15)

    # Avoid overlapping text at the top; use figure-level subtitle instead
    if subtitle:
        # Place subtitle just below the main title at figure level
        try:
            fig.text(0.5, 0.90, subtitle, ha="center", fontsize=9)
        except Exception:
            pass
    if annotate_fallback:
        ax.text(0.99, 0.02, "Fallback window used", transform=ax.transAxes, fontsize=8, va="bottom", ha="right")
    ax.legend(loc="upper left", fontsize=7, frameon=True, framealpha=0.9)
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
    latencies_by_label: Optional[Dict[str, float]] = None,
    peak_amplitudes_by_label: Optional[Dict[str, float]] = None,
    legend_peak_latencies_by_label: Optional[Dict[str, float]] = None,
    ylimit_uv: Optional[float] = None,
    exclude_non_scalp: bool = True,
    non_scalp_labels: Optional[List[str]] = None,
    highlight_channels: Optional[List[str]] = None,
    latency_annotation_label: Optional[str] = "FAL",
    epochs_by_label: Optional[Mapping[str, int]] = None,
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
        latencies_by_label: Optional dict mapping condition names to fractional area latencies (ms).
                           If provided, thin colored vertical lines will be drawn at each condition's
                           FAL to show the temporal midpoint of each waveform.

    Returns:
        matplotlib Figure object
    """
    import mne  # local import for plotting

    n_cols = max(1, len(topomap_by_label) or 1)
    # Make the composite figure wider and taller for better vertical visibility
    # Turn OFF constrained_layout to allow manual control of spacing
    fig = plt.figure(figsize=(7.475, 7.0))

    # Increase waveform panel height ratio for better vertical visibility
    # Reserve space for colorbar: add one extra column with narrow width
    width_ratios = [1.0] * n_cols + [0.15]  # Colorbar gets 15% width

    # Dynamic vertical spacing: when there are few topomaps (1–2),
    # their titles can crowd the overlay. Increase inter-row spacing
    # and slightly favor the overlay height in those cases.
    is_sparse = n_cols <= 2
    if is_sparse:
        height_ratios = [2.9, 1.6]
        hspace = 0.40
    else:
        height_ratios = [2.5, 1.9]
        hspace = 0.18

    gs = fig.add_gridspec(
        2,
        n_cols + 1,
        height_ratios=height_ratios,
        width_ratios=width_ratios,
        hspace=hspace,
        left=0.08,
        right=0.95,
        top=0.92,
        bottom=0.08,
    )

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

        # Append peak legend info if available: (123ms, 4.5 µV)
        try:
            peak_ms_val = None
            if legend_peak_latencies_by_label and label in legend_peak_latencies_by_label:
                peak_ms_val = legend_peak_latencies_by_label[label]
            peak_amp_val = None
            if peak_amplitudes_by_label and label in peak_amplitudes_by_label:
                peak_amp_val = peak_amplitudes_by_label[label]
            if peak_ms_val is not None and not np.isnan(peak_ms_val) and peak_amp_val is not None and not np.isnan(peak_amp_val):
                display_label = f"{display_label} ({float(peak_ms_val):.0f}ms, {float(peak_amp_val):.1f} µV)"
        except Exception:
            # If any formatting fails, keep the base label
            pass
        # Append total epochs if provided
        try:
            if epochs_by_label and label in epochs_by_label:
                display_label = f"{display_label} [{int(epochs_by_label[label])} epochs]"
        except Exception:
            pass
        ax_overlay.plot(times_ms, y, label=display_label, **kw)

    ax_overlay.axvline(0, color="#999", linewidth=1, alpha=0.6)

    # Removed dashed peak lines to simplify: only show selected latency annotations (colored solid lines)

    # === NEW: Mark per-condition fractional area latencies (FAL) ===
    # These show the measured temporal midpoint (50% area) for each condition
    # Thin solid lines matching each waveform color
    if latencies_by_label:
        for label, fal_ms in latencies_by_label.items():
            if colors and label in colors:
                color = colors[label]
            else:
                color = "#444"  # Default dark gray

            # Match the condition's linestyle from config for the latency line
            ls = linestyles.get(label, "-") if linestyles else "-"

            ax_overlay.axvline(
                fal_ms,
                color=color,
                alpha=0.7,
                linestyle=ls,
                linewidth=0.8,
                zorder=5
            )

    # === NEW: Draw per-condition horizontal lines at peak amplitude ===
    # These provide a quick visual reference for the peak amplitude level per condition.
    # Light, dotted lines color-matched to the condition.
    if peak_amplitudes_by_label:
        for label, peak_amp in peak_amplitudes_by_label.items():
            try:
                amp_val = float(peak_amp)
            except Exception:
                continue
            if colors and label in colors:
                color = colors[label]
            else:
                color = "#666"

            # Match the condition's linestyle from config for the amplitude line
            ls = linestyles.get(label, "-") if linestyles else "-"

            ax_overlay.axhline(
                y=amp_val,
                color=color,
                linestyle=ls,
                linewidth=0.8,
                alpha=0.6,
                zorder=3
            )

    # Figure-level main title
    if title:
        try:
            # Adjusted for manual layout (was y=0.985 for constrained_layout)
            t = fig.suptitle(title, fontsize=11, fontweight="bold", y=0.97, va="bottom")
        except Exception:
            pass
    ax_overlay.set_xlabel("Time (ms)")
    ax_overlay.set_ylabel("Amplitude (µV)")

    # Set x-axis limits if requested (e.g., start from baseline onset)
    if xlim_ms is not None:
        ax_overlay.set_xlim(xlim_ms)

    # Set fixed y-axis limits if requested (e.g., ±6 µV)
    if ylimit_uv is not None:
        try:
            ax_overlay.set_ylim((-float(ylimit_uv), float(ylimit_uv)))
        except Exception:
            pass

    # Light gridlines for overlay
    try:
        from matplotlib.ticker import MultipleLocator, AutoMinorLocator
        ax_overlay.xaxis.set_major_locator(MultipleLocator(100))
        ax_overlay.xaxis.set_minor_locator(MultipleLocator(50))
        ax_overlay.yaxis.set_major_locator(MultipleLocator(1))  # 1 µV major ticks (all integers labeled)
    except Exception:
        pass
    ax_overlay.grid(True, which="major", linestyle=":", linewidth=0.5, alpha=0.3)
    ax_overlay.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.15)

    # Add asterisk note to legend if any fallback used
    legend_title = "* = fallback window used" if any_fallback else None
    ax_overlay.legend(loc="upper left", fontsize=7, title=legend_title, title_fontsize=7, frameon=True, framealpha=0.9)

    # Figure-level subtitle to avoid occlusion
    if subtitle:
        try:
            # Enhance subtitle to explain vertical latency lines
            enhanced_subtitle = subtitle
            if latencies_by_label:
                label = latency_annotation_label or "FAL"
                enhanced_subtitle += f" | Vertical lines = {label} Latency"
            # Subtitle slightly below the figure title, anchored by its top edge
            # Adjusted for manual layout (was y=0.955 for constrained_layout)
            fig.text(0.5, 0.94, enhanced_subtitle, ha="center", va="top", fontsize=9)
        except Exception:
            pass

    # Bottom row: topomaps per condition set
    # Use fixed ±5µV color scale across all topomaps for direct visual comparison
    vlim_range = 5.0  # microvolts

    # Store the first topomap image for colorbar reference
    first_topomap_im = None

    # Determine channel picks for scalp-only plotting if requested
    picks = None
    if exclude_non_scalp:
        try:
            # Build a name -> index map from info
            ch_names = [ch.get('ch_name') for ch in info.get('chs', [])]
            # Default HydroCel 128 non-scalp set if not provided
            default_non_scalp = {
                "E1", "E8", "E14", "E17", "E21", "E25", "E32", "E38", "E43", "E44",
                "E48", "E49", "E113", "E114", "E119", "E120", "E121", "E125", "E126", "E127", "E128"
            }
            exclude_set = set((non_scalp_labels or [])) or default_non_scalp
            picks = [idx for idx, nm in enumerate(ch_names) if nm not in exclude_set]
            # Safety: fall back to None if picks would exclude all channels
            if not picks:
                picks = None
        except Exception:
            picks = None

    for idx, (label, tup) in enumerate(sorted(topomap_by_label.items())):
        vec, peak_ms, half_win = tup[0], tup[1], tup[2]
        used_fallback = tup[3] if len(tup) > 3 else False

        # NEW: Use FAL for display if available, otherwise use peak_ms
        display_latency = latencies_by_label.get(label, peak_ms) if latencies_by_label else peak_ms

        ax = fig.add_subplot(gs[1, idx])
        # Fixed symmetric color scaling ensures amplitude differences are visually comparable
        # Subset data and info for scalp-only plotting if picks are defined
        if picks is not None:
            try:
                sub_vec = vec[picks]
                sub_info = mne.pick_info(info, picks, copy=True)
            except Exception:
                sub_vec = vec
                sub_info = info
        else:
            sub_vec = vec
            sub_info = info

        # Prepare optional mask to highlight ROI channels used for ERP overlay
        mask = None
        mask_params = None
        try:
            if highlight_channels:
                highlight_set = set(highlight_channels)
                sub_ch_names = [ch.get('ch_name') for ch in sub_info.get('chs', [])]
                mask = np.array([nm in highlight_set for nm in sub_ch_names], dtype=bool)
                if mask.any():
                    # Smaller, subtler highlight markers (slight transparency)
                    mask_params = dict(
                        marker='o',
                        markerfacecolor=(1.0, 1.0, 0.0, 0.7),  # semi-transparent yellow
                        markeredgecolor='k',
                        linewidth=0,
                        markersize=4,
                    )
                else:
                    mask = None  # do not pass empty mask
        except Exception:
            mask = None
            mask_params = None

        im, cn = mne.viz.plot_topomap(
            sub_vec, sub_info, axes=ax,
            contours=6,  # Add contour lines for better spatial reading
            vlim=(-vlim_range, vlim_range),  # Fixed ±5µV across all conditions
            show=False,
            cmap='RdBu_r',  # Diverging colormap (red=positive, blue=negative)
            mask=mask,
            mask_params=mask_params,
        )

        # Store first topomap image for colorbar reference
        if first_topomap_im is None:
            first_topomap_im = im

        # NEW: Show FAL in title instead of collapsed peak
        title_suffix = "*" if used_fallback else ""
        title_color = None
        try:
            if colors and label in colors:
                title_color = colors[label]
        except Exception:
            title_color = None
        # Compact title to reduce vertical footprint for small condition sets
        if is_sparse:
            title_text = (
                f"{label}{title_suffix}\n"
                f"{(latency_annotation_label or 'FAL')} {display_latency:.1f} ms (±{half_win:.0f} ms)"
            )
            title_size = 7
            title_pad = 0.5
        else:
            title_text = (
                f"{label}{title_suffix}\n{(latency_annotation_label or 'FAL')} {display_latency:.1f} ms\n(±{half_win:.0f} ms)"
            )
            title_size = 8
            title_pad = 1.0

        ax.set_title(
            title_text,
            fontsize=title_size,
            color=title_color,
            pad=title_pad,
        )

    # Add colorbar to rightmost column of topomap row
    if first_topomap_im is not None:
        try:
            # Use the extra column reserved for colorbar (n_cols position, 0-indexed)
            cbar_ax = fig.add_subplot(gs[1, n_cols])  # Colorbar column, bottom row
            cbar = fig.colorbar(first_topomap_im, cax=cbar_ax, label="Amplitude (µV)")
            # Set ticks at key values for clarity
            cbar.set_ticks([-5, -2.5, 0, 2.5, 5])
        except Exception as e:
            # Print error for debugging (won't show in normal runs due to Agg backend)
            import sys
            print(f"Colorbar creation failed: {e}", file=sys.stderr)

    # Add small caption listing highlighted electrodes (if provided)
    electrode_caption = ""
    try:
        if highlight_channels:
            roi_text = ", ".join(highlight_channels)
            electrode_caption = f"Yellow sensors = ERP ROI electrodes: {roi_text}"
            fig.text(0.5, 0.01, electrode_caption, ha="center", va="bottom", fontsize=7, color="#444")
            try:
                fig.set_constrained_layout_pads(h_pad=0.70, hspace=0.04, w_pad=0.14, wspace=0.22)
            except Exception:
                pass
    except Exception:
        pass

    # Add acronym definitions footnote
    try:
        acronym_footnote = _generate_acronym_footnote(
            subtitle=subtitle or "",
            caption=electrode_caption,
            latency_annotation_label=latency_annotation_label or "FAL"
        )
        if acronym_footnote:
            # Position below electrode caption if it exists, otherwise at bottom
            # Increased from 0.005 to 0.025 to avoid overlap with yellow sensor caption
            y_pos = 0.025 if highlight_channels else 0.01
            fig.text(0.5, y_pos, acronym_footnote, ha="center", va="bottom",
                     fontsize=6, color="#666", style="italic")
    except Exception:
        pass

    return fig


def make_collapsed_localizer_figure(
    localizer_results: Dict[str, Dict],
    title: str = "Collapsed Localizer",
    subtitle: Optional[str] = None,
    xlim_ms: Optional[Tuple[float, float]] = None,
):
    """
    Create collapsed localizer figure (GFP or ROI-based).

    This plot provides scientific justification for time window selection by showing:
    - Localizer trace (GFP across channels or ROI mean), labeled accordingly
    - Detected peak within a priori search range (red dashed line)
    - FWHM window (shaded region) - data-driven window width
    - Search range boundaries (dotted lines)

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
        # Extract trace (supports GFP or ROI)
        if 'gfp' in result:
            trace = result['gfp']
            trace_label = "GFP (all channels)"
            y_label = "GFP (µV)"
        else:
            trace = result.get('trace')
            trace_label = result.get('trace_label', 'Localizer')
            y_label = result.get('trace_units', 'µV')
        times_ms = result['times_ms']
        peak_lat = result['peak_latency_ms']
        window_start = result['window_start_ms']
        window_end = result['window_end_ms']
        fwhm = result['fwhm_ms']
        search_range = result['search_range_ms']

        ax = axes[idx]

        # Plot localizer trace
        ax.plot(times_ms, trace, label=trace_label, color="#2c7bb6", linewidth=2.0, zorder=3)

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
        ax.set_ylabel(y_label, fontsize=10)
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
        fig.text(0.5, 0.02, subtitle, ha="center", fontsize=9, style="italic")

    # Add acronym definitions footnote
    try:
        # For collapsed localizer, subtitle typically contains GFP and FWHM
        acronym_footnote = _generate_acronym_footnote(
            subtitle=subtitle or "",
            caption=title or "",  # Title might have relevant acronyms too
            latency_annotation_label=""  # No FAL in collapsed localizer
        )
        if acronym_footnote:
            fig.text(0.5, 0.005, acronym_footnote, ha="center", va="bottom",
                     fontsize=6, color="#666", style="italic")
    except Exception:
        pass

    return fig



def make_peak_to_peak_figure(
    *,
    curves_by_label: Dict[str, Iterable[float]],
    times_ms,
    p2p_by_label: Dict[str, float],
    p1_lat_by_label: Dict[str, float],
    n1_lat_by_label: Dict[str, float],
    title: str,
    subtitle: Optional[str] = None,
    colors: Optional[Mapping[str, str]] = None,
    linestyles: Optional[Mapping[str, str]] = None,
    xlim_ms: Optional[Tuple[float, float]] = None,
    ylimit_uv: Optional[float] = None,
    hline_color: str = "#000000",
    hline_style: str = ":",
    p1_amp_by_label: Optional[Dict[str, float]] = None,
    n1_amp_by_label: Optional[Dict[str, float]] = None,
    epochs_by_label: Optional[Mapping[str, int]] = None,
):
    """
    Create a P1↔N1 peak-to-peak figure using N1 ROI waveforms.

    - Overlays per-condition ROI curves
    - Vertical lines at P1 and N1 latencies per condition (color-matched)
    - Black dotted horizontal lines at P1 and N1 amplitudes per condition
    - ΔµV annotation per condition
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6.9, 5.0), constrained_layout=True)
    try:
        fig.set_constrained_layout_pads(h_pad=0.35, hspace=0.35, w_pad=0.14, wspace=0.22)
    except Exception:
        pass

    # Plot waveforms
    for label, y in curves_by_label.items():
        kw = {}
        if colors and label in colors:
            kw["color"] = colors[label]
        if linestyles and label in linestyles:
            kw["linestyle"] = linestyles[label]
        ax.plot(times_ms, y, label=label, **kw)

    # Zero line and axes labels
    ax.axvline(0, color="#999", linewidth=1, alpha=0.6)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude (µV)")

    # Limits
    if xlim_ms is not None:
        ax.set_xlim(xlim_ms)
    if ylimit_uv is not None:
        try:
            ax.set_ylim((-float(ylimit_uv), float(ylimit_uv)))
        except Exception:
            pass

    # Grid
    try:
        from matplotlib.ticker import MultipleLocator
        ax.xaxis.set_major_locator(MultipleLocator(100))
        ax.xaxis.set_minor_locator(MultipleLocator(50))
        ax.yaxis.set_major_locator(MultipleLocator(1))
    except Exception:
        pass
    ax.grid(True, which="major", linestyle=":", linewidth=0.5, alpha=0.3)
    ax.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.15)

    # Title/subtitle
    if title:
        try:
            fig.suptitle(title, fontsize=12, fontweight="bold", y=0.98)
        except Exception:
            pass
    if subtitle:
        try:
            # Place a bit below the title; leave room above the axes
            fig.text(0.5, 0.93, subtitle, ha="center", fontsize=9)
        except Exception:
            pass

    # No latency vertical lines in P2P plot (only stimulus onset at 0 remains)

    # Draw horizontal peak amplitude lines (use condition color if provided)
    if p1_amp_by_label:
        for label, amp in p1_amp_by_label.items():
            color = colors[label] if colors and label in colors else hline_color
            ax.axhline(amp, color=color, linestyle=hline_style, linewidth=0.9, alpha=0.9)
    if n1_amp_by_label:
        for label, amp in n1_amp_by_label.items():
            color = colors[label] if colors and label in colors else hline_color
            ax.axhline(amp, color=color, linestyle=hline_style, linewidth=0.9, alpha=0.9)

    # Build a compact custom legend-like box with per-row styling using OffsetBox
    from matplotlib.offsetbox import AnchoredOffsetbox, HPacker, VPacker, DrawingArea, TextArea
    from matplotlib.lines import Line2D
    rows = []
    for label in curves_by_label.keys():
        if label not in p2p_by_label:
            continue
        color = colors[label] if colors and label in colors else hline_color
        ls = linestyles.get(label, '-') if linestyles else '-'

        # Small line sample (no triangle) to match waveform style
        da = DrawingArea(22, 8, 0, 0)
        sample = Line2D([2, 20], [4, 4], color=color, linestyle=ls, linewidth=1.6)
        da.add_artist(sample)

        # Condition name (black) with epoch count if available, and colored delta text
        if epochs_by_label and label in epochs_by_label:
            name_text = f"{label} ({int(epochs_by_label[label])} epochs)"
        else:
            name_text = f"{label}"
        name_t = TextArea(name_text, textprops={"color": "#000", "fontsize": 8})
        delta_t = TextArea(f"  Δ = {float(p2p_by_label[label]):.1f} µV", textprops={"color": color, "fontsize": 8})

        row = HPacker(children=[da, name_t, delta_t], align="left", pad=0, sep=2)
        rows.append(row)

    if rows:
        legend_box = VPacker(children=rows, align="left", pad=0, sep=2)
        anchored = AnchoredOffsetbox(loc='upper right', child=legend_box, pad=0.3, borderpad=0.3, frameon=True)
        ax.add_artist(anchored)

    return fig