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
):
    fig, ax = plt.subplots(figsize=(6, 3.5), constrained_layout=True)
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

    Returns:
        matplotlib Figure object
    """
    import mne  # local import for plotting

    n_cols = max(1, len(topomap_by_label) or 1)
    fig = plt.figure(figsize=(6.5, 5.5), constrained_layout=True)
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

        # Add asterisk to title if fallback was used
        title_suffix = "*" if used_fallback else ""
        ax.set_title(f"{label}{title_suffix} – Peak {peak_ms} ms (±{half_win} ms)", fontsize=8)

    return fig


