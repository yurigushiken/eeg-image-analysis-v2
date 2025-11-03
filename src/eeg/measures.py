"""ERP measurement utilities.

This module provides basic ERP measurements. For component peak detection,
use gfp_measures.py which implements the scientifically rigorous GFP-based
approach with FWHM windowing.
"""
from __future__ import annotations

from typing import Tuple
import numpy as np


def _window_mask(times_ms: np.ndarray, window_ms: Tuple[float, float]) -> np.ndarray:
    """Create boolean mask for samples within a time window."""
    start, end = window_ms
    return (times_ms >= start) & (times_ms <= end)


def mean_amplitude(
    signal: np.ndarray, times_ms: np.ndarray, window_ms: Tuple[int, int]
) -> float:
    """
    Calculate mean amplitude within a time window.

    This is a basic measurement utility. For ERP component analysis, use the
    GFP-based approach in gfp_measures.py instead.

    Args:
        signal: 1D array of EEG data (e.g., microvolts)
        times_ms: 1D array of time points in milliseconds
        window_ms: (start, end) tuple defining window in ms

    Returns:
        Mean amplitude within the window

    Raises:
        ValueError: If window has no samples within provided times

    Example:
        >>> mean_amp = mean_amplitude(roi_curve, times_ms, window_ms=(300, 400))
    """
    mask = _window_mask(times_ms, window_ms)
    if not np.any(mask):
        raise ValueError(
            f"Window [{window_ms[0]}, {window_ms[1]}] ms has no samples "
            f"within provided times [{times_ms[0]:.1f}, {times_ms[-1]:.1f}] ms"
        )
    return float(np.mean(signal[mask]))


def fractional_area_latency(
    signal: np.ndarray,
    times_ms: np.ndarray,
    window_ms: Tuple[float, float],
    fraction: float = 0.5,
    polarity: str = "auto"
) -> float:
    """
    Calculate fractional area latency within a time window.

    Finds the time point where the cumulative area under the curve reaches
    a specified fraction of the total area. This provides a robust measure
    of component timing that is less sensitive to noise than peak latency.

    The 50% fractional area latency (default) represents the temporal midpoint
    of a component and is more reliable than peak latency, especially for noisy
    data or components with variable morphology across conditions.

    NOTE: This pipeline uses fraction=0.5 throughout. This parameter is
    documented in the output JSON files (collapsed_localizer_results.json
    and statistical_summary.json) for scientific transparency.

    Args:
        signal: 1D array of EEG data (e.g., ROI-averaged, in microvolts)
        times_ms: 1D array of time points in milliseconds
        window_ms: (start, end) tuple defining window in ms
        fraction: Target fraction of area (default 0.5 for midpoint)
                 Use 0.2 for onset, 0.8 for offset estimation
        polarity: 'positive', 'negative', or 'auto' (infer from mean signal)
                 Determines how to handle signed area computation

    Returns:
        Latency in milliseconds where cumulative area reaches the target fraction

    Raises:
        ValueError: If window has no samples, fraction is invalid, or area
                   computation fails

    References:
        Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008).
        Measurement of ERP latency differences: A comparison of single-
        participant and jackknife-based scoring methods. Psychophysiology,
        45(2), 250-274.

        Luck, S. J. (2014). An Introduction to the Event-Related Potential
        Technique (2nd ed.). MIT Press. Chapter 10: Scoring and Statistical
        Analysis of ERP Amplitudes and Latencies.

    Example:
        >>> # N1 component: 50% area latency within FWHM window
        >>> latency = fractional_area_latency(
        ...     roi_curve, times_ms, window_ms=(140.2, 212.6), polarity='negative'
        ... )
        >>> print(f"N1 50% area latency: {latency:.1f} ms")
    """
    # Validate fraction
    if not 0.0 < fraction < 1.0:
        raise ValueError(
            f"fraction must be between 0 and 1 (exclusive), got {fraction}"
        )

    # Extract window
    mask = _window_mask(times_ms, window_ms)
    if not np.any(mask):
        raise ValueError(
            f"Window [{window_ms[0]}, {window_ms[1]}] ms has no samples "
            f"within provided times [{times_ms[0]:.1f}, {times_ms[-1]:.1f}] ms"
        )

    signal_windowed = signal[mask]
    times_windowed = times_ms[mask]

    # Determine polarity
    if polarity == "auto":
        mean_signal = np.mean(signal_windowed)
        polarity = "negative" if mean_signal < 0 else "positive"

    # Handle polarity: work with rectified signal for area calculation
    # For negative components (N1, N2), flip signal so area is positive
    if polarity == "negative":
        working_signal = -signal_windowed
    else:
        working_signal = signal_windowed

    # Compute cumulative area using trapezoidal integration
    # Area between consecutive points: avg_height * width
    dt = np.diff(times_windowed)  # Time steps (ms)
    avg_amplitudes = (working_signal[:-1] + working_signal[1:]) / 2.0
    incremental_areas = dt * avg_amplitudes

    # Cumulative sum of areas
    cumulative_area = np.cumsum(incremental_areas)

    # Prepend 0 for the starting point (no area before first sample)
    cumulative_area = np.concatenate([[0.0], cumulative_area])

    # Total area in the window
    total_area = cumulative_area[-1]

    if total_area <= 0:
        raise ValueError(
            f"Total area is non-positive ({total_area:.6f}). "
            f"Check that the window contains the component of interest and "
            f"polarity is correct. Mean signal: {np.mean(signal_windowed):.3f} uV"
        )

    # Target area
    target_area = fraction * total_area

    # Find the time point where cumulative area crosses the target
    # Use searchsorted for efficiency
    idx = np.searchsorted(cumulative_area, target_area)

    if idx == 0:
        # Target area is at or before first sample (edge case)
        return float(times_windowed[0])
    elif idx >= len(cumulative_area):
        # Target area at or after last sample (shouldn't happen with valid fraction)
        return float(times_windowed[-1])
    else:
        # Linear interpolation between idx-1 and idx for sub-sample precision
        area_before = cumulative_area[idx - 1]
        area_after = cumulative_area[idx]
        time_before = times_windowed[idx - 1]
        time_after = times_windowed[idx]

        # Interpolate: fraction of distance between samples
        frac_between = (target_area - area_before) / (area_after - area_before)
        latency_ms = time_before + frac_between * (time_after - time_before)

        return float(latency_ms)


def peak_latency(
    signal: np.ndarray,
    times_ms: np.ndarray,
    window_ms: Tuple[float, float],
    polarity: str = "auto"
) -> float:
    """
    Find the time of the signed peak within a window.

    - For positive components (e.g., P1, P3b), returns the time of the maximum.
    - For negative components (e.g., N1), returns the time of the minimum.

    Args:
        signal: 1D array (e.g., ROI-averaged, in microvolts)
        times_ms: 1D array of time points in milliseconds
        window_ms: (start, end) window in ms
        polarity: 'positive' | 'negative' | 'auto'

    Returns:
        Peak latency (ms) within the window.
    """
    mask = _window_mask(times_ms, window_ms)
    if not np.any(mask):
        raise ValueError(
            f"Window [{window_ms[0]}, {window_ms[1]}] ms has no samples "
            f"within provided times [{times_ms[0]:.1f}, {times_ms[-1]:.1f}] ms"
        )

    sig = signal[mask]
    tms = times_ms[mask]

    if polarity == "auto":
        polarity = "negative" if np.mean(sig) < 0 else "positive"

    idx = int(np.argmin(sig) if polarity == "negative" else np.argmax(sig))
    return float(tms[idx])


def peak_amplitude(
    signal: np.ndarray,
    times_ms: np.ndarray,
    window_ms: Tuple[float, float],
    polarity: str = "auto"
) -> float:
    """
    Measure the signed amplitude at the peak within a window.

    - For positive components: maximum value
    - For negative components: minimum value (more negative)
    """
    mask = _window_mask(times_ms, window_ms)
    if not np.any(mask):
        raise ValueError(
            f"Window [{window_ms[0]}, {window_ms[1]}] ms has no samples "
            f"within provided times [{times_ms[0]:.1f}, {times_ms[-1]:.1f}] ms"
        )

    sig = signal[mask]

    if polarity == "auto":
        polarity = "negative" if np.mean(sig) < 0 else "positive"

    return float(np.min(sig) if polarity == "negative" else np.max(sig))


def compute_peak_to_peak_metrics(
    signal: np.ndarray,
    times_ms: np.ndarray,
    p1_window_ms: Tuple[float, float],
    n1_window_ms: Tuple[float, float],
    p_polarity: str = "positive",
    n_polarity: str = "negative",
) -> dict:
    """
    Compute P1↔N1 peak-to-peak metrics from a single ROI waveform.

    This function is designed for the N1 ROI waveform, but measures both
    P1 (positive) and N1 (negative) peaks within their respective windows.

    Returns dict with keys:
      - p1_amp
      - n1_amp
      - p2p_amp (p1_amp - n1_amp)
      - p1_lat_ms
      - n1_lat_ms
    """
    # Validate windows have samples
    p1_mask = _window_mask(times_ms, p1_window_ms)
    n1_mask = _window_mask(times_ms, n1_window_ms)
    if not np.any(p1_mask):
        raise ValueError(
            f"P1 window [{p1_window_ms[0]}, {p1_window_ms[1]}] ms has no samples"
        )
    if not np.any(n1_mask):
        raise ValueError(
            f"N1 window [{n1_window_ms[0]}, {n1_window_ms[1]}] ms has no samples"
        )

    # Compute peak latencies
    p1_lat = peak_latency(
        signal=signal,
        times_ms=times_ms,
        window_ms=p1_window_ms,
        polarity=p_polarity,
    )
    n1_lat = peak_latency(
        signal=signal,
        times_ms=times_ms,
        window_ms=n1_window_ms,
        polarity=n_polarity,
    )

    # Compute peak amplitudes
    p1_amp = peak_amplitude(
        signal=signal,
        times_ms=times_ms,
        window_ms=p1_window_ms,
        polarity=p_polarity,
    )
    n1_amp = peak_amplitude(
        signal=signal,
        times_ms=times_ms,
        window_ms=n1_window_ms,
        polarity=n_polarity,
    )

    p2p = float(p1_amp - n1_amp)

    return {
        "p1_amp": float(p1_amp),
        "n1_amp": float(n1_amp),
        "p2p_amp": p2p,
        "p1_lat_ms": float(p1_lat),
        "n1_lat_ms": float(n1_lat),
    }