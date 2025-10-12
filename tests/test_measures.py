import os
import sys
import numpy as np


CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from eeg.measures import mean_amplitude, peak_amplitude_and_latency


def test_mean_amplitude_basic():
    times_ms = np.arange(-100, 501, 4)  # e.g., 250 Hz ~ 4 ms resolution
    signal = np.zeros_like(times_ms, dtype=float)
    # Inject a bump 60..120 ms with amplitude 5
    window_mask = (times_ms >= 60) & (times_ms <= 120)
    signal[window_mask] = 5.0

    mean_val = mean_amplitude(signal, times_ms, window_ms=(60, 120))
    assert np.isclose(mean_val, 5.0)


def test_peak_amplitude_and_latency_within_window():
    times_ms = np.arange(-100, 501, 4)
    # Make a simple peak at 100 ms with amplitude 3
    signal = np.sin((times_ms - 100) / 10.0)
    signal += 3.0 * (times_ms == 100)

    amp, lat, used_fallback = peak_amplitude_and_latency(
        signal,
        times_ms,
        window_ms=(60, 120),
        polarity="pos",
        smoothing=None,
    )
    assert 60 <= lat <= 120
    assert amp == signal[times_ms == lat][0]
    assert used_fallback is False  # Should not use fallback for clear peak


def test_peak_fallback_for_flat_signal():
    """Test that fallback is triggered for flat signals"""
    times_ms = np.arange(-100, 501, 4)
    signal = np.zeros_like(times_ms, dtype=float)  # Completely flat signal

    amp, lat, used_fallback = peak_amplitude_and_latency(
        signal,
        times_ms,
        window_ms=(60, 120),
        polarity="pos",
        smoothing=None,
        fallback_to_center=True,
    )
    # Should use fallback and return window center
    expected_center = (60 + 120) // 2  # 90 ms
    assert used_fallback is True
    assert abs(lat - expected_center) <= 4  # Within one sample (4ms resolution)


