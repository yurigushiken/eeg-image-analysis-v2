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
) -> Tuple[float, int]:
    mask = _window_mask(times_ms, window_ms)
    if not np.any(mask):
        raise ValueError("Window has no samples within provided times")

    working = signal.copy()
    if smoothing and smoothing.get("method") == "moving_average":
        window_ms_span = int(smoothing.get("window_ms", 0))
        if window_ms_span > 0:
            # Estimate points per ms using median diff
            diffs = np.diff(times_ms)
            ms_per_sample = np.median(diffs)
            points = max(1, int(round(window_ms_span / ms_per_sample)))
            working = _moving_average(working, points)

    window_idx = np.where(mask)[0]
    segment = working[window_idx]
    if polarity == "pos":
        i = int(np.argmax(segment))
    elif polarity == "neg":
        i = int(np.argmin(segment))
    else:
        raise ValueError("polarity must be 'pos' or 'neg'")
    amp = float(segment[i])
    lat = int(times_ms[window_idx[i]])
    return amp, lat


