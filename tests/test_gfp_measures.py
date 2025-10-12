"""Tests for GFP-based peak detection with FWHM window calculation.

This module tests the scientifically rigorous approach to ERP component analysis:
1. Compute Global Field Power (GFP) across all channels
2. Find peak within a priori search range
3. Calculate Full Width at Half Maximum (FWHM) for data-driven window sizing

These tests follow Test-Driven Development (TDD) - they will FAIL until implementation is complete.
"""
import os
import sys
import numpy as np
import pytest

CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from eeg.gfp_measures import (
    compute_gfp,
    find_gfp_peak,
    compute_fwhm_window,
    gfp_peak_and_window,
)


class TestComputeGFP:
    """Test GFP computation from multi-channel EEG data."""

    def test_gfp_single_timepoint(self):
        """GFP at a single timepoint is the standard deviation across channels."""
        # 4 channels, 1 timepoint
        data = np.array([[1.0], [2.0], [3.0], [4.0]])  # shape (4, 1)
        gfp = compute_gfp(data)

        expected_std = np.std(data[:, 0], ddof=1)  # Sample std (unbiased estimator)
        assert gfp.shape == (1,)
        assert np.isclose(gfp[0], expected_std)

    def test_gfp_multiple_timepoints(self):
        """GFP computes std across channels for each timepoint independently."""
        # 3 channels, 5 timepoints
        data = np.array([
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [2.0, 3.0, 4.0, 5.0, 6.0],
            [3.0, 4.0, 5.0, 6.0, 7.0],
        ])
        gfp = compute_gfp(data)

        assert gfp.shape == (5,)
        # GFP should be constant (std = 1.0) since all channels increase uniformly
        for i in range(5):
            expected_std = np.std(data[:, i], ddof=1)  # Sample std
            assert np.isclose(gfp[i], expected_std)

    def test_gfp_with_realistic_erp(self):
        """GFP should peak where the spatial topography is strongest."""
        times_ms = np.linspace(-100, 500, 150)
        n_channels = 64

        # Simulate ERP: all channels have a peak at 100ms, but with different amplitudes
        data = np.zeros((n_channels, len(times_ms)))
        for ch in range(n_channels):
            # Each channel has different amplitude (simulating spatial distribution)
            amplitude = np.sin(ch / n_channels * np.pi)  # Varies 0-1 across channels
            # Peak at 100ms
            peak_idx = np.argmin(np.abs(times_ms - 100))
            data[ch, :] = amplitude * np.exp(-((times_ms - 100)**2) / (2 * 30**2))

        gfp = compute_gfp(data)

        # GFP should peak around 100ms where spatial variance is highest
        peak_idx = np.argmax(gfp)
        peak_time = times_ms[peak_idx]
        assert 80 <= peak_time <= 120  # Within reasonable range of true peak


class TestFindGFPPeak:
    """Test finding GFP peak within a priori search range."""

    def test_find_peak_in_search_range(self):
        """Peak detection should only consider samples within search range."""
        times_ms = np.arange(-100, 501, 4)  # 250 Hz ~ 4ms resolution
        gfp = np.zeros(len(times_ms))

        # Create peaks at 50ms, 100ms, and 300ms
        gfp[times_ms == 48] = 2.0  # Outside typical N1 range
        gfp[times_ms == 100] = 3.0  # In N1 range (not this)
        gfp[times_ms == 160] = 5.0  # In N1 range (should find this!)
        gfp[times_ms == 300] = 10.0  # Outside N1 range

        # Search for N1 peak in typical range
        peak_lat, peak_amp = find_gfp_peak(gfp, times_ms, search_range_ms=(125, 200))

        assert peak_lat == 160
        assert np.isclose(peak_amp, 5.0)

    def test_peak_exactly_at_boundary(self):
        """Peak at search range boundary should be found."""
        times_ms = np.arange(-100, 501, 4)
        gfp = np.zeros(len(times_ms))

        # Peak exactly at lower boundary
        gfp[times_ms == 60] = 5.0

        peak_lat, peak_amp = find_gfp_peak(gfp, times_ms, search_range_ms=(60, 120))
        assert peak_lat == 60
        assert np.isclose(peak_amp, 5.0)

    def test_no_samples_in_search_range_raises_error(self):
        """Should raise error if search range has no samples."""
        times_ms = np.arange(-100, 200, 4)
        gfp = np.ones(len(times_ms))

        # Search range completely outside data
        with pytest.raises(ValueError, match="No samples found in search range"):
            find_gfp_peak(gfp, times_ms, search_range_ms=(300, 400))

    def test_flat_gfp_in_range_raises_error(self):
        """Should raise error if GFP is completely flat (no meaningful peak)."""
        times_ms = np.arange(-100, 501, 4)
        # Create GFP with global max outside search range, and tiny peak inside
        gfp = np.ones(len(times_ms)) * 1.0
        gfp[times_ms == 100] = 1.05  # Tiny peak in search range (5% of baseline)
        gfp[times_ms == 300] = 15.0  # Large peak outside search range

        # Should raise error - peak in range is not meaningful (< 10% of global max)
        with pytest.raises(ValueError, match="No meaningful GFP peak found"):
            find_gfp_peak(gfp, times_ms, search_range_ms=(60, 120))


class TestComputeFWHMWindow:
    """Test FWHM window calculation around GFP peak."""

    def test_fwhm_symmetric_gaussian(self):
        """FWHM should correctly measure width of symmetric Gaussian peak."""
        times_ms = np.linspace(-100, 500, 600)

        # Create Gaussian peak at 100ms with sigma=20ms
        sigma = 20.0
        gfp = np.exp(-((times_ms - 100)**2) / (2 * sigma**2))
        peak_idx = np.argmin(np.abs(times_ms - 100))

        # Theoretical FWHM for Gaussian: FWHM = 2.355 * sigma
        expected_fwhm = 2.355 * sigma  # ~47 ms

        window_start, window_end = compute_fwhm_window(gfp, times_ms, peak_idx)
        measured_fwhm = window_end - window_start

        # Should be within 10% of theoretical value
        assert np.isclose(measured_fwhm, expected_fwhm, rtol=0.1)
        # Window should be centered on peak
        assert np.isclose((window_start + window_end) / 2, 100, atol=2)

    def test_fwhm_asymmetric_peak(self):
        """FWHM should handle asymmetric peaks."""
        times_ms = np.linspace(-100, 500, 600)
        peak_time = 150
        peak_idx = np.argmin(np.abs(times_ms - peak_time))

        # Create asymmetric peak: fast rise, slow fall
        gfp = np.zeros(len(times_ms))
        for i, t in enumerate(times_ms):
            if t < peak_time:
                gfp[i] = np.exp(-((t - peak_time)**2) / (2 * 10**2))
            else:
                gfp[i] = np.exp(-((t - peak_time)**2) / (2 * 30**2))

        window_start, window_end = compute_fwhm_window(gfp, times_ms, peak_idx)

        # Window should still be centered reasonably close to peak
        assert window_start < peak_time < window_end
        # Width should be positive
        assert window_end > window_start

    def test_fwhm_peak_at_edge_raises_error(self):
        """Should raise error if peak is too close to data edge for FWHM calculation."""
        times_ms = np.linspace(-100, 500, 100)
        gfp = np.zeros(len(times_ms))

        # Peak at the very start
        peak_idx = 0
        gfp[peak_idx] = 10.0

        with pytest.raises(ValueError, match="Cannot compute FWHM"):
            compute_fwhm_window(gfp, times_ms, peak_idx)

    def test_fwhm_handles_sharp_peak(self):
        """FWHM should handle even very sharp peaks (scipy handles interpolation)."""
        times_ms = np.linspace(-100, 500, 100)

        # Create a sharp spike in middle
        gfp = np.ones(len(times_ms)) * 1.0
        peak_idx = 50  # Middle of array
        gfp[peak_idx] = 100.0  # Extremely sharp spike
        gfp[peak_idx-1] = 1.0  # Immediately drops back down
        gfp[peak_idx+1] = 1.0  # No gradual descent

        # scipy.signal.peak_widths handles this with interpolation
        window_start, window_end = compute_fwhm_window(gfp, times_ms, peak_idx)

        # Should return a very narrow window (sharp peak)
        assert window_start < times_ms[peak_idx] < window_end
        assert (window_end - window_start) < 20  # Very narrow for sharp peak


class TestGFPPeakAndWindow:
    """Test integrated GFP peak detection and FWHM window calculation."""

    def test_end_to_end_p1_component(self):
        """Full pipeline for P1 component detection."""
        times_ms = np.linspace(-100, 500, 600)
        n_channels = 32

        # Simulate P1: positive peak at ~88ms
        data = np.zeros((n_channels, len(times_ms)))
        for ch in range(n_channels):
            amplitude = 0.5 + 0.5 * np.sin(ch / n_channels * np.pi)
            data[ch, :] = amplitude * np.exp(-((times_ms - 88)**2) / (2 * 15**2))

        result = gfp_peak_and_window(
            data,
            times_ms,
            search_range_ms=(60, 120),
            component_name="P1"
        )

        assert 70 <= result['peak_latency_ms'] <= 106
        assert result['window_start_ms'] < result['peak_latency_ms'] < result['window_end_ms']
        assert result['fwhm_ms'] > 0
        assert result['component_name'] == "P1"
        assert 'gfp' in result
        assert len(result['gfp']) == len(times_ms)

    def test_end_to_end_n1_component(self):
        """Full pipeline for N1 component detection."""
        times_ms = np.linspace(-100, 500, 600)
        n_channels = 32

        # Simulate N1: negative peak at ~160ms (but GFP sees magnitude)
        data = np.zeros((n_channels, len(times_ms)))
        for ch in range(n_channels):
            amplitude = -1.0 * (0.5 + 0.5 * np.sin(ch / n_channels * np.pi))
            data[ch, :] = amplitude * np.exp(-((times_ms - 160)**2) / (2 * 25**2))

        result = gfp_peak_and_window(
            data,
            times_ms,
            search_range_ms=(125, 200),
            component_name="N1"
        )

        assert 140 <= result['peak_latency_ms'] <= 180
        assert result['window_start_ms'] < result['peak_latency_ms'] < result['window_end_ms']

    def test_end_to_end_p3b_component(self):
        """Full pipeline for P3b component detection."""
        times_ms = np.linspace(-100, 500, 600)
        n_channels = 64

        # Simulate P3b: broad positive peak at ~396ms
        data = np.zeros((n_channels, len(times_ms)))
        for ch in range(n_channels):
            amplitude = 1.0 + 0.5 * np.sin(ch / n_channels * np.pi)
            data[ch, :] = amplitude * np.exp(-((times_ms - 396)**2) / (2 * 50**2))

        result = gfp_peak_and_window(
            data,
            times_ms,
            search_range_ms=(300, 496),
            component_name="P3b"
        )

        assert 350 <= result['peak_latency_ms'] <= 450
        # P3b should have wider FWHM than P1/N1
        assert result['fwhm_ms'] > 60

    def test_multichannel_input_validation(self):
        """Should raise error for invalid input shapes."""
        times_ms = np.linspace(-100, 500, 100)

        # 1D data (should be 2D)
        data_1d = np.ones(100)
        with pytest.raises(ValueError, match="must be 2D"):
            gfp_peak_and_window(data_1d, times_ms, search_range_ms=(60, 120))

        # Mismatched time dimension
        data_wrong = np.ones((32, 50))  # 50 samples, but times has 100
        with pytest.raises(ValueError, match="mismatch"):
            gfp_peak_and_window(data_wrong, times_ms, search_range_ms=(60, 120))


class TestGFPWithRealMNEStructure:
    """Test GFP computation with MNE-like Evoked objects (integration test)."""

    def test_gfp_from_evoked_like_structure(self):
        """Simulate realistic MNE Evoked object with proper structure."""
        # Create mock evoked data structure
        n_channels = 64
        n_times = 175  # ~700ms at 250Hz
        times = np.linspace(-0.2, 0.5, n_times)
        times_ms = times * 1000

        # Simulate realistic ERP with multiple components
        data = np.zeros((n_channels, n_times))
        for ch in range(n_channels):
            spatial_weight = np.sin(ch / n_channels * np.pi)
            # P1 at 88ms
            p1_idx = np.argmin(np.abs(times_ms - 88))
            data[ch, :] += spatial_weight * np.exp(-((times_ms - 88)**2) / (2 * 15**2)) * 2
            # N1 at 160ms
            n1_idx = np.argmin(np.abs(times_ms - 160))
            data[ch, :] -= spatial_weight * np.exp(-((times_ms - 160)**2) / (2 * 20**2)) * 3
            # P3b at 380ms
            p3b_idx = np.argmin(np.abs(times_ms - 380))
            data[ch, :] += spatial_weight * np.exp(-((times_ms - 380)**2) / (2 * 60**2)) * 4

        # Test that we can find all three components
        p1_result = gfp_peak_and_window(data, times_ms, search_range_ms=(60, 120), component_name="P1")
        n1_result = gfp_peak_and_window(data, times_ms, search_range_ms=(125, 200), component_name="N1")
        p3b_result = gfp_peak_and_window(data, times_ms, search_range_ms=(300, 496), component_name="P3b")

        # Peaks should be in expected ranges
        assert 70 <= p1_result['peak_latency_ms'] <= 110
        assert 140 <= n1_result['peak_latency_ms'] <= 180
        assert 340 <= p3b_result['peak_latency_ms'] <= 420

        # P3b should have widest window (broader component)
        assert p3b_result['fwhm_ms'] > n1_result['fwhm_ms']
        assert p3b_result['fwhm_ms'] > p1_result['fwhm_ms']
