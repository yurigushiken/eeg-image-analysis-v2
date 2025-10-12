"""Collapsed localizer using Global Field Power (GFP) for unbiased component detection.

This module implements the "collapsed localizer" approach using Global Field Power:
- Averages across ALL experimental conditions to create one grand average per component
- Computes GFP (standard deviation across all channels at each timepoint)
- Finds component peaks within a priori search ranges
- Calculates FWHM windows data-adaptively

This prevents circular analysis and ensures time window selection is independent from
condition-specific effects.

Scientific Rationale:
--------------------
Traditional ERP analysis often suffers from "double-dipping": using the same data to both
select analysis windows and test hypotheses. The collapsed localizer solves this by:

1. **Independence**: Peak detection uses data collapsed across all conditions
2. **Objectivity**: GFP uses all channels, not hand-picked electrodes
3. **Data-driven windows**: FWHM adapts to actual component duration
4. **Transparency**: All decisions are algorithmic and documented

References:
-----------
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any
  ERP experiment (and why you shouldn't). Psychophysiology, 54(1), 146-157.
- Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S., & Baker, C. I. (2009). Circular
  analysis in systems neuroscience: the dangers of double dipping. Nature Neuroscience,
  12(5), 535-540.
"""
from __future__ import annotations

from typing import Dict, List, Any
import numpy as np
import mne

from .gfp_measures import gfp_peak_and_window


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
