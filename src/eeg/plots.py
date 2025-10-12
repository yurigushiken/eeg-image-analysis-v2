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
    topomap_by_label: Dict[str, Tuple[Iterable[float], int, int]],
    info,
    title: str,
    subtitle: Optional[str] = None,
    colors: Optional[Mapping[str, str]] = None,
    linestyles: Optional[Mapping[str, str]] = None,
):
    import mne  # local import for plotting

    n_cols = max(1, len(topomap_by_label) or 1)
    fig = plt.figure(figsize=(6.5, 5.5), constrained_layout=True)
    gs = fig.add_gridspec(2, n_cols, height_ratios=[2.2, 1.8])

    # Overlay spanning top row
    ax_overlay = fig.add_subplot(gs[0, :])
    for label, y in curves_by_label.items():
        kw = {}
        if colors and label in colors:
            kw["color"] = colors[label]
        if linestyles and label in linestyles:
            kw["linestyle"] = linestyles[label]
        ax_overlay.plot(times_ms, y, label=label, **kw)
    ax_overlay.axvline(0, color="#999", linewidth=1, alpha=0.6)
    # Mark peaks with light vertical lines using topomap peak times
    for label, (_vec, peak_ms, _halfwin) in topomap_by_label.items():
        vkw = {"color": (colors.get(label) if colors and label in colors else "#666"), "alpha": 0.25, "linestyle": "--"}
        ax_overlay.axvline(peak_ms, **vkw)
    ax_overlay.set_title(title)
    ax_overlay.set_xlabel("Time (ms)")
    ax_overlay.set_ylabel("Amplitude (a.u.)")
    ax_overlay.legend(loc="best", fontsize=8)

    # Figure-level subtitle to avoid occlusion
    if subtitle:
        fig.suptitle(f"\n{subtitle}", fontsize=9, y=0.98)

    # Bottom row: topomaps per condition set
    for idx, (label, (vec, peak_ms, half_win)) in enumerate(sorted(topomap_by_label.items())):
        ax = fig.add_subplot(gs[1, idx])
        mne.viz.plot_topomap(vec, info, axes=ax, contours=0, show=False)
        ax.set_title(f"{label} – Peak {peak_ms} ms (±{half_win} ms)", fontsize=8)

    return fig


