"""Tests for basic ERP measurement utilities.

NOTE: For GFP-based component detection tests, see test_gfp_measures.py
This module only tests basic utilities like mean_amplitude.
"""
import os
import sys
import numpy as np


CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from eeg.measures import mean_amplitude


def test_mean_amplitude_basic():
    """Test mean amplitude calculation within a window."""
    times_ms = np.arange(-100, 501, 4)  # e.g., 250 Hz ~ 4 ms resolution
    signal = np.zeros_like(times_ms, dtype=float)
    # Inject a bump 60..120 ms with amplitude 5
    window_mask = (times_ms >= 60) & (times_ms <= 120)
    signal[window_mask] = 5.0

    mean_val = mean_amplitude(signal, times_ms, window_ms=(60, 120))
    assert np.isclose(mean_val, 5.0)


def test_mean_amplitude_partial_window():
    """Test mean amplitude when window partially overlaps signal."""
    times_ms = np.arange(0, 100, 1)
    signal = np.ones_like(times_ms, dtype=float) * 3.0

    # Window from 20-80 ms
    mean_val = mean_amplitude(signal, times_ms, window_ms=(20, 80))
    assert np.isclose(mean_val, 3.0)
