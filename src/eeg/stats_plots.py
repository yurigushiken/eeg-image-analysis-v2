"""
Statistical visualization functions for ERP data (Phase 2C).

Provides publication-ready plots with measurement window context:
- Boxplots
- Violin plots
- Effect size forest plots with confidence intervals

All plots can include measurement window information to link
visualizations back to the collapsed localizer decisions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Union, Optional, List, Tuple


# Set publication-ready defaults
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.2)


def format_window_caption(
    component: str,
    dv: str,
    window_start_ms: float,
    window_end_ms: float,
    peak_latency_ms: float,
    fwhm_ms: Optional[float] = None
) -> str:
    """
    Format measurement window caption for plots.

    Parameters
    ----------
    component : str
        Component name (e.g., 'N1', 'P3b').
    dv : str
        Dependent variable name.
    window_start_ms : float
        Measurement window start time (ms).
    window_end_ms : float
        Measurement window end time (ms).
    peak_latency_ms : float
        Collapsed localizer peak latency (ms).
    fwhm_ms : float, optional
        Full Width at Half Maximum (ms).

    Returns
    -------
    str
        Formatted caption text.

    Examples
    --------
    >>> caption = format_window_caption(
    ...     component='N1',
    ...     dv='latency_frac_area_ms',
    ...     window_start_ms=140.2,
    ...     window_end_ms=212.6,
    ...     peak_latency_ms=168.0,
    ...     fwhm_ms=72.4
    ... )
    """
    measure_name = "Latency" if "latency" in dv.lower() else "Amplitude"

    caption = (
        f"{component} {measure_name} measured in collapsed localizer FWHM window: "
        f"[{window_start_ms:.1f}, {window_end_ms:.1f}] ms "
        f"(peak @ {peak_latency_ms:.1f} ms"
    )

    if fwhm_ms:
        caption += f", FWHM = {fwhm_ms:.1f} ms"

    caption += ")."

    return caption


def _auto_label(dv: str, ylabel: Optional[str] = None) -> str:
    """Auto-generate axis label with units from dependent variable name."""
    if ylabel:
        return ylabel

    if 'latency' in dv.lower():
        return 'Latency (ms)'
    elif 'amplitude' in dv.lower():
        return 'Amplitude (µV)'
    else:
        return dv.replace('_', ' ').title()


def plot_boxplot(
    data: pd.DataFrame,
    dv: str,
    groupby: str,
    title: str,
    output_path: Union[str, Path],
    # Measurement window context (optional)
    component: Optional[str] = None,
    window_start_ms: Optional[float] = None,
    window_end_ms: Optional[float] = None,
    peak_latency_ms: Optional[float] = None,
    fwhm_ms: Optional[float] = None,
    include_window_context: bool = False,
    # Styling options
    ylabel: Optional[str] = None,
    xlabel: Optional[str] = None,
    show_points: bool = True,
    show_mean: bool = True,
    dpi: int = 300,
    figsize: Tuple[float, float] = (8, 6)
):
    """
    Create publication-ready boxplot.

    Parameters
    ----------
    data : pd.DataFrame
        Data to plot.
    dv : str
        Dependent variable column name.
    groupby : str
        Grouping variable column name.
    title : str
        Plot title.
    output_path : str or Path
        Output file path.
    component : str, optional
        Component name for caption.
    window_start_ms : float, optional
        Measurement window start (ms).
    window_end_ms : float, optional
        Measurement window end (ms).
    peak_latency_ms : float, optional
        Collapsed localizer peak (ms).
    fwhm_ms : float, optional
        Full Width at Half Maximum (ms).
    include_window_context : bool, default=False
        Whether to include measurement window in caption.
    ylabel : str, optional
        Y-axis label (auto-generated if None).
    xlabel : str, optional
        X-axis label (defaults to groupby).
    show_points : bool, default=True
        Show individual data points.
    show_mean : bool, default=True
        Show mean as red diamond.
    dpi : int, default=300
        Plot resolution.
    figsize : tuple, default=(8, 6)
        Figure size (width, height) in inches.

    Examples
    --------
    >>> plot_boxplot(
    ...     data=n1_data,
    ...     dv='latency_frac_area_ms',
    ...     groupby='condition',
    ...     title='N1 Latency by Condition',
    ...     output_path='n1_latency.png',
    ...     component='N1',
    ...     window_start_ms=140.2,
    ...     window_end_ms=212.6,
    ...     peak_latency_ms=168.0,
    ...     include_window_context=True
    ... )
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Drop NaN values
    plot_data = data[[groupby, dv]].dropna()

    fig, ax = plt.subplots(figsize=figsize)

    # Create boxplot
    box_parts = ax.boxplot(
        [plot_data[plot_data[groupby] == grp][dv].values
         for grp in plot_data[groupby].unique()],
        labels=plot_data[groupby].unique(),
        patch_artist=True,
        showmeans=False
    )

    # Style boxes
    for patch in box_parts['boxes']:
        patch.set_facecolor('#3498db')
        patch.set_alpha(0.7)

    # Add individual points if requested
    if show_points:
        for i, grp in enumerate(plot_data[groupby].unique(), 1):
            grp_data = plot_data[plot_data[groupby] == grp][dv].values
            x = np.random.normal(i, 0.04, size=len(grp_data))
            ax.scatter(x, grp_data, alpha=0.4, s=20, color='black')

    # Add mean markers if requested
    if show_mean:
        means = [plot_data[plot_data[groupby] == grp][dv].mean()
                 for grp in plot_data[groupby].unique()]
        ax.scatter(range(1, len(means) + 1), means,
                   color='red', marker='D', s=60, zorder=3,
                   label='Mean')
        ax.legend()

    # Labels
    ax.set_xlabel(xlabel if xlabel else groupby.replace('_', ' ').title())
    ax.set_ylabel(_auto_label(dv, ylabel))
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add caption if window context provided
    if include_window_context and all([component, window_start_ms, window_end_ms, peak_latency_ms]):
        caption = format_window_caption(
            component=component,
            dv=dv,
            window_start_ms=window_start_ms,
            window_end_ms=window_end_ms,
            peak_latency_ms=peak_latency_ms,
            fwhm_ms=fwhm_ms
        )
        fig.text(0.5, 0.01, caption, ha='center', fontsize=8,
                 style='italic', wrap=True)
        plt.subplots_adjust(bottom=0.12)

    plt.tight_layout()
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    print(f"Boxplot saved to: {output_path}")


def plot_violin(
    data: pd.DataFrame,
    dv: str,
    groupby: str,
    title: str,
    output_path: Union[str, Path],
    # Measurement window context (optional)
    component: Optional[str] = None,
    window_start_ms: Optional[float] = None,
    window_end_ms: Optional[float] = None,
    peak_latency_ms: Optional[float] = None,
    fwhm_ms: Optional[float] = None,
    include_window_context: bool = False,
    # Styling options
    ylabel: Optional[str] = None,
    xlabel: Optional[str] = None,
    inner: str = "box",
    dpi: int = 300,
    figsize: Tuple[float, float] = (8, 6)
):
    """
    Create publication-ready violin plot.

    Parameters
    ----------
    data : pd.DataFrame
        Data to plot.
    dv : str
        Dependent variable column name.
    groupby : str
        Grouping variable column name.
    title : str
        Plot title.
    output_path : str or Path
        Output file path.
    component : str, optional
        Component name for caption.
    window_start_ms : float, optional
        Measurement window start (ms).
    window_end_ms : float, optional
        Measurement window end (ms).
    peak_latency_ms : float, optional
        Collapsed localizer peak (ms).
    fwhm_ms : float, optional
        Full Width at Half Maximum (ms).
    include_window_context : bool, default=False
        Whether to include measurement window in caption.
    ylabel : str, optional
        Y-axis label (auto-generated if None).
    xlabel : str, optional
        X-axis label (defaults to groupby).
    inner : str, default="box"
        Inner plot representation ("box", "quartile", "point", or None).
    dpi : int, default=300
        Plot resolution.
    figsize : tuple, default=(8, 6)
        Figure size (width, height) in inches.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Drop NaN values
    plot_data = data[[groupby, dv]].dropna()

    fig, ax = plt.subplots(figsize=figsize)

    # Create violin plot
    sns.violinplot(
        data=plot_data,
        x=groupby,
        y=dv,
        hue=groupby,  # Explicitly assign hue to satisfy seaborn v0.14+
        inner=inner,
        ax=ax,
        palette="muted",
        legend=False  # Don't show redundant legend since x already labels groups
    )

    # Labels
    ax.set_xlabel(xlabel if xlabel else groupby.replace('_', ' ').title())
    ax.set_ylabel(_auto_label(dv, ylabel))
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add caption if window context provided
    if include_window_context and all([component, window_start_ms, window_end_ms, peak_latency_ms]):
        caption = format_window_caption(
            component=component,
            dv=dv,
            window_start_ms=window_start_ms,
            window_end_ms=window_end_ms,
            peak_latency_ms=peak_latency_ms,
            fwhm_ms=fwhm_ms
        )
        fig.text(0.5, 0.01, caption, ha='center', fontsize=8,
                 style='italic', wrap=True)
        plt.subplots_adjust(bottom=0.12)

    plt.tight_layout()
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    print(f"Violin plot saved to: {output_path}")


def plot_effect_sizes(
    pairwise_results: pd.DataFrame,
    output_path: Union[str, Path],
    title: str = 'Effect Sizes',
    effect_size_col: Optional[str] = None,
    ci_lower_col: str = 'ci_lower',
    ci_upper_col: str = 'ci_upper',
    show_ci: bool = True,
    threshold_lines: Optional[List[float]] = None,
    threshold_labels: Optional[List[str]] = None,
    dpi: int = 300,
    figsize: Tuple[float, float] = (8, 6)
):
    """
    Create effect size forest plot with confidence intervals.

    Parameters
    ----------
    pairwise_results : pd.DataFrame
        Pairwise test results containing effect sizes and CIs.
    output_path : str or Path
        Output file path.
    title : str, default='Effect Sizes'
        Plot title.
    effect_size_col : str, optional
        Column containing effect sizes (auto-detected if None).
    ci_lower_col : str, default='ci_lower'
        Column containing lower CI bounds.
    ci_upper_col : str, default='ci_upper'
        Column containing upper CI bounds.
    show_ci : bool, default=True
        Show confidence intervals.
    threshold_lines : list of float, optional
        Effect size threshold values (e.g., [0.2, 0.5, 0.8] for Cohen's d).
    threshold_labels : list of str, optional
        Labels for thresholds (e.g., ['Small', 'Medium', 'Large']).
    dpi : int, default=300
        Plot resolution.
    figsize : tuple, default=(8, 6)
        Figure size (width, height) in inches.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Auto-detect effect size column
    if effect_size_col is None:
        if 'cohen' in pairwise_results.columns:
            effect_size_col = 'cohen'
        elif 'hedges' in pairwise_results.columns:
            effect_size_col = 'hedges'
        else:
            raise ValueError("Could not auto-detect effect size column. Specify effect_size_col parameter.")

    # Create comparison labels
    if 'comparison' in pairwise_results.columns:
        labels = pairwise_results['comparison']
    elif 'A' in pairwise_results.columns and 'B' in pairwise_results.columns:
        labels = pairwise_results['A'] + ' vs ' + pairwise_results['B']
    else:
        labels = [f"Comparison {i+1}" for i in range(len(pairwise_results))]

    effect_sizes = pairwise_results[effect_size_col].values

    # Dynamically scale height by number of comparisons to avoid large empty space
    base_width, base_height = figsize
    dynamic_height = max(2.5, min(10.0, 0.6 * max(1, len(labels)) + 1.6))
    fig, ax = plt.subplots(figsize=(base_width, dynamic_height), constrained_layout=True)

    # Plot effect sizes
    y_positions = np.arange(len(labels))
    ax.scatter(effect_sizes, y_positions, s=80, color='#2c3e50', zorder=3)

    # Add confidence intervals if requested
    if show_ci and ci_lower_col in pairwise_results.columns and ci_upper_col in pairwise_results.columns:
        ci_lower = pairwise_results[ci_lower_col].values
        ci_upper = pairwise_results[ci_upper_col].values

        for i, (lower, upper) in enumerate(zip(ci_lower, ci_upper)):
            ax.plot([lower, upper], [i, i], color='#34495e', linewidth=2, zorder=2)

    # Add threshold lines if provided
    if threshold_lines:
        for threshold in threshold_lines:
            ax.axvline(threshold, color='gray', linestyle='--', alpha=0.5, linewidth=1)
            ax.axvline(-threshold, color='gray', linestyle='--', alpha=0.5, linewidth=1)

    # Add threshold labels if provided
    if threshold_labels and threshold_lines:
        y_max = len(labels) - 1
        for threshold, label in zip(threshold_lines, threshold_labels):
            ax.text(threshold, y_max + 0.3, label, ha='center', fontsize=8, color='gray')

    # Zero line
    ax.axvline(0, color='black', linestyle='-', linewidth=1, alpha=0.7)

    # Labels
    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Effect Size (Cohen's d)", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)

    # Use constrained_layout and bbox_inches tight to reduce whitespace
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    print(f"Effect size plot saved to: {output_path}")
