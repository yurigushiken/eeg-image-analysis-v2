"""Global Field Power (GFP) based ERP component detection with FWHM windowing.

This module implements the scientifically rigorous approach recommended for ERP analysis:

1. **Global Field Power (GFP)**: Compute the standard deviation across all channels at each
   timepoint. This gives an unbiased measure of overall scalp activity, independent of any
   single electrode or spatial hypothesis.

2. **A Priori Search Range**: Find the GFP peak within a literature-defined time window
   (e.g., 60-120ms for P1, 125-200ms for N1, 300-496ms for P3b). This prevents circular
   analysis while remaining data-driven within scientifically justified bounds.

3. **Full Width at Half Maximum (FWHM)**: Calculate the analysis window width based on
   where the GFP crosses half its peak value. This makes the window adaptive to the actual
   component duration in your data—sharp components get narrow windows, broad components
   get wide windows.

Scientific Rationale:
---------------------
This approach eliminates the three major sources of bias in traditional ERP analysis:

- **Channel selection bias**: GFP uses all channels, not hand-picked "interesting" ones
- **Circular analysis**: Peak is found in GFP (averaged across conditions), not individual
  conditions, preventing double-dipping
- **Arbitrary windows**: FWHM derives window width from the data, not researcher preference

References:
-----------
- Lehmann, D., & Skrandies, W. (1980). Reference-free identification of components of
  checkerboard-evoked multichannel potential fields. Electroencephalography and Clinical
  Neurophysiology, 48(6), 609-621.
- Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S., & Baker, C. I. (2009). Circular
  analysis in systems neuroscience: the dangers of double dipping. Nature Neuroscience,
  12(5), 535-540.
"""
from __future__ import annotations

from typing import Tuple, Dict, Any
import numpy as np
from scipy.signal import peak_widths, find_peaks


def compute_gfp(data: np.ndarray) -> np.ndarray:
    """
    Compute Global Field Power (GFP) from multi-channel EEG data.

    GFP is the standard deviation of the voltage across all channels at each timepoint.
    It provides a reference-independent measure of the strength of the scalp electric field.

    For EEG, GFP represents the spatial standard deviation—when the topography has strong
    positive/negative regions (high spatial variance), GFP peaks. This identifies moments
    of maximal brain activity regardless of reference choice.

    Args:
        data: EEG data array of shape (n_channels, n_times)
              Each row is a channel, each column is a timepoint

    Returns:
        GFP array of shape (n_times,) containing the standard deviation across channels
        at each timepoint

    Raises:
        ValueError: If data is not 2D or has invalid shape

    Example:
        >>> data = evoked.get_data()  # MNE Evoked object
        >>> gfp = compute_gfp(data)
        >>> plt.plot(evoked.times * 1000, gfp)
        >>> plt.xlabel('Time (ms)')
        >>> plt.ylabel('GFP (µV)')
    """
    if data.ndim != 2:
        raise ValueError(f"Data must be 2D (n_channels, n_times), got shape {data.shape}")

    if data.shape[0] < 2:
        raise ValueError(f"Need at least 2 channels for GFP, got {data.shape[0]}")

    # GFP = standard deviation across channels at each timepoint
    # axis=0 means compute std across the channel dimension
    gfp = np.std(data, axis=0, ddof=1)  # ddof=1 for sample std (unbiased estimator)

    return gfp


def find_gfp_peak(
    gfp: np.ndarray,
    times_ms: np.ndarray,
    search_range_ms: Tuple[int, int],
    min_gfp_ratio: float = 0.1,
) -> Tuple[int, float]:
    """
    Find the latency and amplitude of the GFP peak within an a priori search range.

    This implements the "a priori search range" principle: we only search for peaks within
    a time window justified by prior literature, preventing data snooping while remaining
    objective within scientifically reasonable bounds.

    Args:
        gfp: Global field power array (n_times,)
        times_ms: Time points in milliseconds (n_times,)
        search_range_ms: (start, end) tuple defining the a priori search window in ms
        min_gfp_ratio: Minimum GFP as fraction of overall maximum (default 0.1)
                       Ensures we find a real peak, not just noise

    Returns:
        Tuple of (peak_latency_ms, peak_amplitude) where:
            - peak_latency_ms: Time in ms where GFP peaks (int)
            - peak_amplitude: GFP value at peak (float)

    Raises:
        ValueError: If no samples fall in search range, or if no meaningful peak exists

    Example:
        >>> # Find N1 peak in typical range
        >>> peak_lat, peak_amp = find_gfp_peak(gfp, times_ms, search_range_ms=(125, 200))
        >>> print(f"N1 peaks at {peak_lat} ms with GFP = {peak_amp:.2f} µV")
    """
    # Find samples within search range
    start_ms, end_ms = search_range_ms
    mask = (times_ms >= start_ms) & (times_ms <= end_ms)

    if not np.any(mask):
        raise ValueError(
            f"No samples found in search range [{start_ms}, {end_ms}] ms. "
            f"Data spans [{times_ms[0]:.1f}, {times_ms[-1]:.1f}] ms"
        )

    # Extract GFP and times within range
    gfp_windowed = gfp[mask]
    times_windowed = times_ms[mask]

    # Find maximum GFP in this window
    peak_idx_in_window = np.argmax(gfp_windowed)
    peak_amplitude = float(gfp_windowed[peak_idx_in_window])
    peak_latency_ms = int(np.round(times_windowed[peak_idx_in_window]))

    # Validate that this is a meaningful peak (not just flat noise)
    global_max_gfp = np.max(gfp)
    if peak_amplitude < min_gfp_ratio * global_max_gfp:
        raise ValueError(
            f"No meaningful GFP peak found in search range [{start_ms}, {end_ms}] ms. "
            f"Peak GFP ({peak_amplitude:.3f}) is less than {min_gfp_ratio*100}% of "
            f"global maximum ({global_max_gfp:.3f}). This suggests the component may "
            f"not be present in your data, or the search range is incorrect."
        )

    return peak_latency_ms, peak_amplitude


def compute_fwhm_window(
    gfp: np.ndarray,
    times_ms: np.ndarray,
    peak_idx: int,
    min_width_samples: int = 5,
) -> Tuple[float, float]:
    """
    Calculate Full Width at Half Maximum (FWHM) window around a GFP peak.

    FWHM is the width of the peak at 50% of its maximum height. This provides a data-driven,
    objective measure of component duration. Sharp, transient components (like P1) will have
    narrow FWHM; slow, sustained components (like P3b) will have wide FWHM.

    The window is defined by finding where the GFP crosses half the peak value on both sides
    of the peak. This is interpolated for sub-sample precision.

    Args:
        gfp: Global field power array (n_times,)
        times_ms: Time points in milliseconds (n_times,)
        peak_idx: Index of the peak in the arrays
        min_width_samples: Minimum width in samples (default 5) to ensure valid peak

    Returns:
        Tuple of (window_start_ms, window_end_ms) in milliseconds

    Raises:
        ValueError: If peak is too close to edges, or FWHM cannot be computed

    Example:
        >>> peak_idx = np.argmax(gfp)
        >>> window_start, window_end = compute_fwhm_window(gfp, times_ms, peak_idx)
        >>> print(f"FWHM window: [{window_start:.1f}, {window_end:.1f}] ms")
        >>> fwhm_duration = window_end - window_start
        >>> print(f"Component duration (FWHM): {fwhm_duration:.1f} ms")
    """
    if peak_idx < min_width_samples or peak_idx >= len(gfp) - min_width_samples:
        # Peak too close to edge - provide informative error with time information
        peak_time = times_ms[peak_idx]
        epoch_start = times_ms[0]
        epoch_end = times_ms[-1]
        sample_duration = np.mean(np.diff(times_ms))
        required_margin = min_width_samples * sample_duration
        raise ValueError(
            f"Cannot compute FWHM: GFP peak at {peak_time:.1f} ms (index {peak_idx}) is too close to "
            f"epoch edge. Epoch spans [{epoch_start:.1f}, {epoch_end:.1f}] ms. "
            f"Need at least {min_width_samples} samples (~{required_margin:.1f} ms) on each side of peak. "
            f"\nSolutions: (1) Extend your epoch duration to at least {peak_time + required_margin + 50:.0f} ms, or "
            f"(2) Narrow the a priori search range in components.yaml to avoid edge effects."
        )

    # Use scipy's peak_widths to find FWHM
    # peak_widths returns (widths, width_heights, left_ips, right_ips)
    # where left_ips and right_ips are interpolated positions of half-maximum crossings
    try:
        widths, width_heights, left_ips, right_ips = peak_widths(
            gfp,
            [peak_idx],
            rel_height=0.5  # Full Width at Half Maximum
        )
    except Exception as e:
        raise ValueError(f"FWHM computation failed: {e}")

    # Convert interpolated indices to milliseconds using linear interpolation
    left_idx_float = float(left_ips[0])
    right_idx_float = float(right_ips[0])

    # Handle boundary cases
    if left_idx_float < 0 or right_idx_float >= len(times_ms):
        raise ValueError(
            "Cannot find half-maximum crossings within data bounds. "
            "The peak may be truncated or not well-defined."
        )

    # Interpolate to get precise time values
    # For index 2.7, we interpolate between times[2] and times[3]
    def interpolate_time(idx_float: float) -> float:
        idx_low = int(np.floor(idx_float))
        idx_high = int(np.ceil(idx_float))
        if idx_low == idx_high:
            return float(times_ms[idx_low])
        fraction = idx_float - idx_low
        return float(times_ms[idx_low] + fraction * (times_ms[idx_high] - times_ms[idx_low]))

    window_start_ms = interpolate_time(left_idx_float)
    window_end_ms = interpolate_time(right_idx_float)

    # Validate result
    if window_end_ms <= window_start_ms:
        raise ValueError(
            f"Invalid FWHM window: end ({window_end_ms:.1f}) <= start ({window_start_ms:.1f})"
        )

    return window_start_ms, window_end_ms


def gfp_peak_and_window(
    data: np.ndarray,
    times_ms: np.ndarray,
    search_range_ms: Tuple[int, int],
    component_name: str = "",
) -> Dict[str, Any]:
    """
    Complete GFP-based component analysis: compute GFP, find peak, calculate FWHM window.

    This is the main entry point for the GFP-based analysis pipeline. It:
    1. Computes GFP from multi-channel data
    2. Finds the peak within the a priori search range
    3. Calculates the FWHM window around that peak

    This gives you everything needed for unbiased ERP component quantification.

    Args:
        data: EEG data array of shape (n_channels, n_times)
        times_ms: Time points in milliseconds (n_times,)
        search_range_ms: (start, end) tuple for a priori peak search
        component_name: Optional name for QC/debugging (e.g., "P1", "N1")

    Returns:
        Dictionary containing:
            - 'gfp': The computed GFP array (n_times,)
            - 'peak_latency_ms': Peak latency in ms (int)
            - 'peak_amplitude': Peak GFP amplitude (float)
            - 'window_start_ms': FWHM window start in ms (float)
            - 'window_end_ms': FWHM window end in ms (float)
            - 'fwhm_ms': FWHM duration in ms (float)
            - 'component_name': Component name for reference
            - 'search_range_ms': The search range used

    Raises:
        ValueError: If input validation fails or component cannot be detected

    Example:
        >>> # Analyze P1 component
        >>> data = collapsed_evoked.get_data()  # shape (n_channels, n_times)
        >>> times_ms = collapsed_evoked.times * 1000
        >>> result = gfp_peak_and_window(data, times_ms, search_range_ms=(60, 120), component_name="P1")
        >>> print(f"P1 peaks at {result['peak_latency_ms']} ms")
        >>> print(f"Analysis window: [{result['window_start_ms']:.1f}, {result['window_end_ms']:.1f}] ms")
        >>> print(f"FWHM: {result['fwhm_ms']:.1f} ms")
    """
    # Validate input
    if data.ndim != 2:
        raise ValueError(f"Data must be 2D (n_channels, n_times), got shape {data.shape}")

    if data.shape[1] != len(times_ms):
        raise ValueError(
            f"Time dimension mismatch: data has {data.shape[1]} samples, "
            f"but times_ms has {len(times_ms)} points"
        )

    # Step 1: Compute GFP
    gfp = compute_gfp(data)

    # Step 2: Find peak in search range
    peak_latency_ms, peak_amplitude = find_gfp_peak(gfp, times_ms, search_range_ms)

    # Step 3: Calculate FWHM window
    peak_idx = np.argmin(np.abs(times_ms - peak_latency_ms))
    window_start_ms, window_end_ms = compute_fwhm_window(gfp, times_ms, peak_idx)

    fwhm_ms = window_end_ms - window_start_ms

    return {
        'gfp': gfp,
        'peak_latency_ms': peak_latency_ms,
        'peak_amplitude': peak_amplitude,
        'window_start_ms': window_start_ms,
        'window_end_ms': window_end_ms,
        'fwhm_ms': fwhm_ms,
        'component_name': component_name,
        'search_range_ms': search_range_ms,
    }
