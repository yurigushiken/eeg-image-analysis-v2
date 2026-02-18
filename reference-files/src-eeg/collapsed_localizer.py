"""Collapsed localizers for ERP component window selection.

This module provides two polarity-agnostic, collapsed-across-conditions localizer methods:

- GFP localizer (objective, reference-free):
  * Compute Global Field Power (std across channels) and locate the maximum within an
    a priori search range; compute FWHM window around that peak.

- ROI localizer (polarity-aware):
  * Average specified ROI channels from the grand average (collapsed across ALL conditions
    and subjects), detect the signed peak (positive or negative) within the a priori search
    range, and compute FWHM around that peak by operating on a positized series.

Both approaches avoid circularity by collapsing conditions before peak detection.

References:
-----------
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any
  ERP experiment (and why you shouldn't). Psychophysiology, 54(1), 146-157.
- Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S., & Baker, C. I. (2009). Circular
  analysis in systems neuroscience: the dangers of double dipping. Nature Neuroscience,
  12(5), 535-540.
"""
from __future__ import annotations

from typing import Dict, List, Any, Iterable
import numpy as np
import mne

from .gfp_measures import gfp_peak_and_window, compute_fwhm_window


def compute_collapsed_localizer(
    evokeds_by_set: Dict[str, List[mne.Evoked]],
    component_name: str,
    search_range_ms: tuple[int, int],
) -> Dict[str, Any]:
    """
    Compute collapsed localizer for a single component using GFP.

    This averages ALL condition sets together, computes GFP, finds the peak within
    the a priori search range, and calculates the FWHM window.

    Args:
        evokeds_by_set: Dict mapping condition set names to lists of Evoked objects
        component_name: Component name (e.g., "P1", "N1", "P3b")
        search_range_ms: (start, end) tuple for a priori peak search

    Returns:
        Dictionary with GFP analysis results including:
            - 'gfp': GFP array (n_times,)
            - 'times_ms': Time points in milliseconds
            - 'peak_latency_ms': Peak latency
            - 'peak_amplitude': Peak GFP amplitude
            - 'window_start_ms': FWHM window start
            - 'window_end_ms': FWHM window end
            - 'fwhm_ms': FWHM duration
            - 'component_name': Component name
            - 'n_subjects': Number of subjects included
            - 'n_conditions': Number of condition sets included

    Raises:
        ValueError: If no evoked data available or component cannot be detected

    Example:
        >>> result = compute_collapsed_localizer(
        ...     evokeds_by_set={'Cond1': [evoked1, evoked2], 'Cond2': [evoked3, evoked4]},
        ...     component_name="P1",
        ...     search_range_ms=(60, 120)
        ... )
        >>> print(f"P1 peaks at {result['peak_latency_ms']} ms")
        >>> print(f"FWHM window: [{result['window_start_ms']:.1f}, {result['window_end_ms']:.1f}] ms")
    """
    # Collect all evokeds across all condition sets (collapsed localizer principle)
    all_evokeds = []
    for set_name, evoked_list in evokeds_by_set.items():
        all_evokeds.extend(evoked_list)

    if not all_evokeds:
        raise ValueError(
            f"No evoked data available for collapsed localizer ({component_name})"
        )

    # Combine into grand average across ALL subjects and ALL conditions
    grand_avg = mne.combine_evoked(all_evokeds, weights="equal")

    # Get data and times
    data = grand_avg.get_data()  # Shape: (n_channels, n_times)
    times_ms = (grand_avg.times * 1000.0).astype(float)

    # Run GFP-based peak detection and FWHM windowing
    result = gfp_peak_and_window(
        data=data,
        times_ms=times_ms,
        search_range_ms=search_range_ms,
        component_name=component_name
    )

    # Add metadata about the collapsed localizer
    result['n_subjects'] = len(all_evokeds)
    result['n_conditions'] = len(evokeds_by_set)
    result['times_ms'] = times_ms

    return result


def compute_collapsed_localizer_roi(
    evokeds_by_set: Dict[str, List[mne.Evoked]],
    roi_channels: Iterable[str],
    component_name: str,
    search_range_ms: tuple[int, int],
    polarity: str = "positive",
) -> Dict[str, Any]:
    """
    Collapsed localizer using an ROI mean waveform.

    Steps:
    1) Combine ALL condition sets and subjects equally -> grand average
    2) Extract ROI channels and compute mean waveform
    3) Within a priori window, find signed peak according to 'polarity'
    4) Compute FWHM window around that peak using a positized series

    Returns a result dict analogous to the GFP method, but with a generic trace.
    """
    # Collect all evokeds across all condition sets
    all_evokeds: List[mne.Evoked] = []
    for evoked_list in evokeds_by_set.values():
        all_evokeds.extend(evoked_list)
    if not all_evokeds:
        raise ValueError(
            f"No evoked data available for collapsed localizer (ROI) ({component_name})"
        )

    grand_avg = mne.combine_evoked(all_evokeds, weights="equal")
    times_ms = (grand_avg.times * 1000.0).astype(float)

    # Extract ROI mean waveform
    try:
        roi_ev = grand_avg.copy().pick_channels(list(roi_channels), ordered=False)
    except Exception as e:
        raise ValueError(f"ROI localizer failed to pick channels: {e}")
    if roi_ev.data.size == 0:
        raise ValueError("ROI localizer has no data after picking channels")
    # Convert to microvolts for reporting/plotting
    roi_curve = roi_ev.data.mean(axis=0) * 1e6

    # Determine search mask
    start_ms, end_ms = search_range_ms
    mask = (times_ms >= start_ms) & (times_ms <= end_ms)
    if not np.any(mask):
        raise ValueError(
            f"No samples in ROI localizer search range [{start_ms}, {end_ms}] ms"
        )

    # Find signed peak index in full array using masked region
    positized = roi_curve if str(polarity).lower() == "positive" else -roi_curve
    window_indices = np.where(mask)[0]
    if window_indices.size == 0:
        raise ValueError("Invalid search mask for ROI localizer")
    peak_idx_in_window = int(np.argmax(positized[mask]))
    peak_idx = int(window_indices[peak_idx_in_window])

    # Compute FWHM window on positized series
    window_start_ms, window_end_ms = compute_fwhm_window(
        positized, times_ms, peak_idx
    )
    fwhm_ms = float(window_end_ms - window_start_ms)

    peak_latency_ms = int(np.round(times_ms[peak_idx]))
    peak_amplitude = float(roi_curve[peak_idx])  # signed amplitude in ROI waveform (µV)

    return {
        "trace": roi_curve,
        "trace_label": "ROI mean",
        "trace_units": "µV",
        "times_ms": times_ms,
        "peak_latency_ms": peak_latency_ms,
        "peak_amplitude": peak_amplitude,
        "window_start_ms": float(window_start_ms),
        "window_end_ms": float(window_end_ms),
        "fwhm_ms": fwhm_ms,
        "component_name": component_name,
        "n_subjects": len(all_evokeds),
        "n_conditions": len(evokeds_by_set),
        "search_range_ms": tuple(search_range_ms),
        "polarity": str(polarity).lower(),
        "method": "roi",
    }


def compute_all_collapsed_localizers(
    evokeds_by_set: Dict[str, List[mne.Evoked]],
    components_config: Dict[str, Dict[str, Any]],
    requested_components: List[str] = None,
) -> Dict[str, Dict[str, Any]]:
    """
    Compute collapsed localizers for requested components.

    This is the main entry point for the GFP-based collapsed localizer pipeline.
    It processes each component independently using its configured search range.

    Args:
        evokeds_by_set: Dict mapping condition set names to lists of Evoked objects
        components_config: Component configuration dict with search ranges
                          Format: {'P1': {'window_ms': [60, 120]}, ...}
        requested_components: List of component names to analyze. If None, analyzes all
                            components in components_config.

    Returns:
        Dict mapping component name to GFP analysis results

    Raises:
        ValueError: If components_config is missing or malformed

    Example:
        >>> components_config = {
        ...     'P1': {'window_ms': [60, 120]},
        ...     'N1': {'window_ms': [125, 200]},
        ...     'P3b': {'window_ms': [300, 496]}
        ... }
        >>> # Analyze only P1 and N1
        >>> results = compute_all_collapsed_localizers(
        ...     evokeds_by_set, components_config, requested_components=['P1', 'N1']
        ... )
        >>> for comp, result in results.items():
        ...     print(f"{comp}: peak at {result['peak_latency_ms']} ms, "
        ...           f"FWHM = {result['fwhm_ms']:.1f} ms")
    """
    if not components_config:
        raise ValueError("components_config cannot be empty")

    # Determine which components to analyze
    if requested_components is None:
        components_to_analyze = list(components_config.keys())
    else:
        components_to_analyze = requested_components

    results = {}

    for comp_name in components_to_analyze:
        if comp_name not in components_config:
            raise ValueError(
                f"Component '{comp_name}' requested but not found in components_config. "
                f"Available components: {list(components_config.keys())}"
            )

        comp_cfg = components_config[comp_name]
        # Get a priori search range from config
        search_range = comp_cfg.get('window_ms')
        if not search_range or len(search_range) != 2:
            raise ValueError(
                f"Component '{comp_name}' missing valid 'window_ms' in config. "
                f"Expected [start, end], got: {search_range}"
            )

        search_range_ms = tuple(search_range)

        try:
            result = compute_collapsed_localizer(
                evokeds_by_set=evokeds_by_set,
                component_name=comp_name,
                search_range_ms=search_range_ms,
            )
            results[comp_name] = result

            # Log success
            print(f"  {comp_name}: peak at {result['peak_latency_ms']} ms, "
                  f"FWHM window [{result['window_start_ms']:.1f}, {result['window_end_ms']:.1f}] ms "
                  f"(width: {result['fwhm_ms']:.1f} ms)")

        except ValueError as e:
            # If component detection fails, raise error (no fallbacks)
            raise ValueError(
                f"Failed to detect {comp_name} component in collapsed localizer: {e}"
            ) from e

    return results
