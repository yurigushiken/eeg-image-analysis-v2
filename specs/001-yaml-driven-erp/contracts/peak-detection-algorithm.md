# Peak Detection Algorithm Contract

**Feature**: YAML-Driven ERP Analysis
**Component**: Peak Detection (src/eeg/measures.py)
**Version**: 1.0
**Date**: 2025-10-11

## Overview

This document specifies the exact algorithm for detecting ERP component peaks to avoid circular analysis ("double dipping") per Kriegeskorte et al. (2009).

## The Problem: Circular Analysis

**Traditional approach** (❌ INCORRECT):
1. Create grand average from ALL subjects
2. Find peak in grand average at time T
3. Measure ALL subjects in window centered at time T
4. Run statistics

**Issue**: Subject i's data influences the window used to measure Subject i → artificial inflation of effect size.

## The Solution: Leave-One-Participant-Out (LOPO)

**Our approach** (✅ CORRECT):
1. For each subject i:
   a. Create grand average from subjects ≠ i
   b. Find peak in that leave-one-out grand average
   c. Measure subject i in window centered on that peak
2. Run statistics on measurements

**Guarantee**: Subject i is measured using a window that is independent of Subject i's data.

---

## Algorithm Specification

### Step 1: Define A Priori Search Window

```python
# From literature, NOT from data
search_window = {
    'P1': {'tmin': 0.060, 'tmax': 0.120},  # 60-120ms
    'N1': {'tmin': 0.125, 'tmax': 0.200},  # 125-200ms
    'P3b': {'tmin': 0.300, 'tmax': 0.600}  # 300-600ms
}
```

**Rationale**: Based on published ERP literature (e.g., Hyde & Spelke 2009, 2012; Tang-Lonardo 2023).

### Step 2: Define Polarity and Measurement Window

```python
component_config = {
    'P1': {
        'search_window': [0.060, 0.120],
        'polarity': 'pos',  # Find maximum
        'window_half_width_ms': 20  # ±20ms around peak for mean amplitude
    },
    'N1': {
        'search_window': [0.125, 0.200],
        'polarity': 'neg',  # Find minimum
        'window_half_width_ms': 20
    },
    'P3b': {
        'search_window': [0.300, 0.600],
        'polarity': 'pos',  # Find maximum
        'window_half_width_ms': 50  # ±50ms (configurable via YAML)
    }
}
```

### Step 3: LOPO Peak Detection Loop

```python
def extract_erp_measures_lopo(subjects_evokeds, conditions, roi_electrodes, component_config):
    """
    Extract ERP measures using LOPO to avoid circular analysis.

    Args:
        subjects_evokeds: Dict[condition -> List[Evoked per subject]]
        conditions: List[str] - condition names (e.g., ["Increasing", "Decreasing"])
        roi_electrodes: List[str] - electrode names for ROI (e.g., ["E65", "E66", "E67"])
        component_config: Dict with:
            - search_window: [tmin, tmax] in seconds
            - polarity: 'pos' or 'neg'
            - window_half_width_ms: ±width in milliseconds

    Returns:
        subject_means: Dict[condition -> List[float]] - mean amplitude in µV per subject
        analysis_windows: List[Tuple[float, float]] - (tmin, tmax) per subject for QC
        peak_times: List[float] - peak time per subject for QC
    """
    import mne
    import numpy as np

    n_subjects = len(subjects_evokeds[conditions[0]])
    subject_means = {cond: [] for cond in conditions}
    analysis_windows = []
    peak_times = []

    # LOPO loop: for each subject i
    for i in range(n_subjects):
        # Step 3a: Create leave-one-out grand averages (all subjects except i)
        loo_grand_averages = {}
        for cond in conditions:
            loo_evokeds = [subjects_evokeds[cond][j] for j in range(n_subjects) if j != i]
            if len(loo_evokeds) == 0:
                raise ValueError(f"No subjects remaining for condition {cond} when leaving out subject {i}")
            loo_grand_averages[cond] = mne.grand_average(loo_evokeds)

        # Step 3b: Collapse across conditions (unbiased peak)
        collapsed = mne.combine_evoked(list(loo_grand_averages.values()), weights='equal')

        # Step 3c: Apply optional smoothing before peak detection
        if 'smoothing' in component_config and component_config['smoothing']['method'] != 'none':
            collapsed_data = collapsed.copy().pick(roi_electrodes).data.mean(axis=0)
            smoothed_data = smooth_timeseries(
                collapsed_data,
                sfreq=collapsed.info['sfreq'],
                window_ms=component_config['smoothing']['window_ms'],
                mode='reflect'
            )
            # Temporarily replace data for peak detection
            collapsed_smooth = collapsed.copy()
            collapsed_smooth._data[0] = smoothed_data
            search_evoked = collapsed_smooth
        else:
            search_evoked = collapsed

        # Step 3d: Find peak from collapsed grand average
        _, peak_time = search_evoked.copy().pick(roi_electrodes).get_peak(
            tmin=component_config['search_window'][0],
            tmax=component_config['search_window'][1],
            mode=component_config['polarity']
        )
        peak_times.append(peak_time)

        # Step 3e: Create analysis window around peak
        half_width_s = component_config['window_half_width_ms'] / 1000.0
        analysis_tmin = peak_time - half_width_s
        analysis_tmax = peak_time + half_width_s
        analysis_windows.append((analysis_tmin, analysis_tmax))

        # Step 3f: Extract mean amplitude from subject i in that window
        for cond in conditions:
            subject_evoked = subjects_evokeds[cond][i]
            # Use ORIGINAL unsmoothed data for measurement
            mean_amp = subject_evoked.copy().pick(roi_electrodes).crop(
                analysis_tmin, analysis_tmax
            ).data.mean()
            subject_means[cond].append(mean_amp * 1e6)  # Convert to µV

    return subject_means, analysis_windows, peak_times


def smooth_timeseries(data, sfreq, window_ms=10, mode='reflect'):
    """
    Apply moving average smoothing for peak detection.

    Args:
        data: 1D array (time series)
        sfreq: Sampling frequency (Hz)
        window_ms: Window size in milliseconds (default 10)
        mode: Edge padding mode ('reflect', 'constant', etc.)

    Returns:
        smoothed: 1D array (same shape as data)

    Implementation:
        - Uses boxcar (rectangular) window
        - Window size = window_ms / (1000.0 / sfreq), rounded to nearest odd integer
        - scipy.ndimage.uniform_filter1d with reflection padding
    """
    from scipy.ndimage import uniform_filter1d
    import numpy as np

    window_samples = int(np.round(window_ms / (1000.0 / sfreq)))
    if window_samples % 2 == 0:  # Ensure odd window for symmetry
        window_samples += 1

    smoothed = uniform_filter1d(data, size=window_samples, mode=mode)
    return smoothed
```

---

## Key Principles

### 1. A Priori Search Window
- Defined from **literature**, not data
- Based on previous ERP studies (Hyde & Spelke 2009, 2012; Tang-Lonardo 2023)
- Same window used for all conditions and subjects

### 2. Condition-Collapsed Peak
- Use `mne.combine_evoked(..., weights='equal')` to create unbiased average
- Prevents bias toward any specific condition
- Peak represents "consensus" response across all conditions

### 3. LOPO Independence
- Subject i measured using window defined by subjects ≠ i
- Guarantees no circular dependency
- Reduces effect size inflation

### 4. Consistent Measurement
- All subjects measured with **mean amplitude** in ±window
- Window width configurable via YAML (default ±20ms for N1/P1, ±50ms for P3b)
- Use **original unsmoothed data** for measurement (smoothing only for peak detection)

### 5. Smoothing (Optional)
- Applied **only** for peak detection, not measurement
- Default: 10ms moving average (boxcar window with reflection padding)
- Configurable via YAML: `plots.smoothing: {method: 'moving_average', window_ms: 10}`
- Set `method: 'none'` to disable smoothing

---

## Edge Cases

### Peak Not Found (Flat/Noisy Signal)
If `get_peak()` fails or returns NaN:
1. Fall back to **component window center**: `peak_time = (tmin + tmax) / 2.0`
2. Log warning: `"Peak not found for subject {i} in component {name}; using window center {peak_time*1000:.1f}ms"`
3. Mark case in QC report: `qc_flags['peak_fallback'] = True`
4. Continue with mean amplitude measurement

### Insufficient Subjects for LOO
If only 1 subject exists for a condition:
- Cannot perform LOPO (need at least 2 subjects)
- Fall back to traditional approach (use all subjects to find peak)
- Log warning and mark in QC

### ROI Channels Partially Missing
- Peak detection uses only available channels in ROI
- If fewer than `roi.min_channels` available, exclude subject from analysis
- Document exclusion in QC report

---

## References

1. **Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S. F., & Baker, C. I. (2009)**. "Circular analysis in systems neuroscience: the dangers of double dipping." *Nature Neuroscience*, 12(5), 535-540.
   - Seminal paper on circular analysis bias
   - Demonstrates how double-dipping inflates statistical strength

2. **Hyde, D. C., & Spelke, E. S. (2009)**. "All numbers are not equal: An electrophysiological investigation of small and large number representations." *Journal of Cognitive Neuroscience*, 21(6), 1039-1053.
   - Established N1/P2p/P3b components for numerical processing

3. **Tang-Lonardo, J. E. (2023)**. *The Neurobehavioral Basis of the Parallel Individuation (PI) and Approximation Number System (ANS) Study*. Columbia University doctoral dissertation.
   - Time windows used in this project: N1 (125-200ms), P3b (435-535ms)
   - Current study replicates with 24 participants

4. **Luck, S. J. (2014)**. *An Introduction to the Event-Related Potential Technique* (2nd ed.). MIT Press.
   - Best practices for ERP analysis
   - Chapter on avoiding analysis pitfalls

---

## Implementation Checklist

- [ ] Implement `extract_erp_measures_lopo()` in src/eeg/measures.py
- [ ] Implement `smooth_timeseries()` in src/eeg/measures.py
- [ ] Add YAML config validation for component search windows
- [ ] Add QC reporting for peak detection fallbacks
- [ ] Add unit tests for LOPO algorithm (mock data)
- [ ] Add smoke tests with real data (verify independence)
- [ ] Document in FR-016: "Peak detection MUST use LOPO approach per Kriegeskorte et al. (2009)"
- [ ] Update quickstart.md with example YAML for peak detection config

---

**Status**: ✅ Specification Complete
**Next Step**: Implement in Phase 2 (Foundational) - Task T015
