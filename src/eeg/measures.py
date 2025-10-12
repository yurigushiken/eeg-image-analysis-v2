from __future__ import annotations

from typing import Iterable, Optional, Tuple

import numpy as np


def _window_mask(times_ms: np.ndarray, window_ms: Tuple[int, int]) -> np.ndarray:
    start, end = window_ms
    return (times_ms >= start) & (times_ms <= end)


def _moving_average(signal: np.ndarray, window_points: int) -> np.ndarray:
    if window_points <= 1:
        return signal
    kernel = np.ones(window_points, dtype=float) / float(window_points)
    return np.convolve(signal, kernel, mode="same")


def mean_amplitude(
    signal: np.ndarray, times_ms: np.ndarray, window_ms: Tuple[int, int]
) -> float:
    mask = _window_mask(times_ms, window_ms)
    if not np.any(mask):
        raise ValueError("Window has no samples within provided times")
    return float(np.mean(signal[mask]))


def peak_amplitude_and_latency(
    signal: np.ndarray,
    times_ms: np.ndarray,
    window_ms: Tuple[int, int],
    polarity: str = "pos",
    smoothing: Optional[dict] = None,
    fallback_to_center: bool = True,
) -> Tuple[float, int, bool]:
    """
    Detect peak amplitude and latency within a time window.

    Args:
        signal: 1D array of EEG data (e.g., microvolts)
        times_ms: 1D array of time points in milliseconds
        window_ms: (start, end) tuple defining search window in ms
        polarity: "pos" for maximum (P1, P3b) or "neg" for minimum (N1)
        smoothing: Optional dict with {"method": "moving_average", "window_ms": int}
        fallback_to_center: If True, use window center when peak detection fails

    Returns:
        (amplitude, latency_ms, used_fallback): Tuple where used_fallback=True
        indicates the fallback (window center) was used instead of detected peak.
        This happens when the signal is flat or noisy within the window.

    Note:
        When used_fallback=True, the calling code should:
        - Log a warning for QC records
        - Add on-figure annotation (e.g., asterisk in legend or "fallback" label)
        - Record in QC summary CSV
    """
    mask = _window_mask(times_ms, window_ms)
    if not np.any(mask):
        raise ValueError("Window has no samples within provided times")

    working = signal.copy()
    if smoothing and smoothing.get("method") == "moving_average":
        window_ms_span = int(smoothing.get("window_ms", 0))
        if window_ms_span > 0:
            # Estimate points per ms using median diff
            diffs = np.diff(times_ms)
            ms_per_sample = np.median(diffs) if len(diffs) > 0 else 1.0
            points = max(1, int(round(window_ms_span / ms_per_sample)))
            working = _moving_average(working, points)

    window_idx = np.where(mask)[0]
    segment = working[window_idx]

    # Detect peak within window
    if polarity == "pos":
        i = int(np.argmax(segment))
    elif polarity == "neg":
        i = int(np.argmin(segment))
    else:
        raise ValueError("polarity must be 'pos' or 'neg'")

    detected_amp = float(segment[i])
    detected_lat = int(times_ms[window_idx[i]])

    # Check for flat or noisy signal (fallback condition)
    # If signal variance in window is very low, the peak is not meaningful
    segment_std = np.std(segment)
    used_fallback = False

    # Fallback criteria: if std is effectively zero (flat signal < 0.1 microvolts)
    # This threshold is conservative - adjust based on your data characteristics
    if segment_std < 0.1:  # Flat signal detection
        if fallback_to_center:
            # Use window center as fallback
            center_lat = int((window_ms[0] + window_ms[1]) / 2)
            # Find closest time point to center
            center_idx = np.argmin(np.abs(times_ms - center_lat))
            detected_amp = float(signal[center_idx])
            detected_lat = int(times_ms[center_idx])
            used_fallback = True
        else:
            raise ValueError("Peak detection failed: signal is flat/noisy in window")

    return detected_amp, detected_lat, used_fallback


