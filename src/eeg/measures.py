"""ERP measurement utilities.

This module provides basic ERP measurements. For component peak detection,
use gfp_measures.py which implements the scientifically rigorous GFP-based
approach with FWHM windowing.
"""
from __future__ import annotations

from typing import Tuple
import numpy as np


def _window_mask(times_ms: np.ndarray, window_ms: Tuple[int, int]) -> np.ndarray:
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
