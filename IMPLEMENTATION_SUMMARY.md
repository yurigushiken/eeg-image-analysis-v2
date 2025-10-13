# ERP Analysis Pipeline Implementation Summary

## What Was Implemented

This document summarizes two major phases of the analysis pipeline:
1. **Phase 1 (Jan 2025)**: Global Field Power (GFP) based analysis with FWHM windowing
2. **Phase 2 (Oct 2024)**: Fractional Area Latency (FAL) for robust timing measurements

---

## Latest Update: Fractional Area Latency (Oct 12, 2024)
**Status**: ✅ **COMPLETE - All Tests Passing (17/17)**

### Phase 2 Implementation Date
**October 12, 2024**

### What Phase 2 Adds: Fractional Area Latency Measurements

**The Problem Solved**: The collapsed localizer provides an unbiased measurement window, but peak latency is the same for all conditions (by design). Researchers need a way to measure **timing differences between conditions** within that window.

**The Solution**: Fractional Area Latency (FAL) — finds the time point where cumulative area under the ROI curve reaches 50%. This is:
- ✅ More robust than peak latency (less noise-sensitive)
- ✅ Condition-specific (can vary between conditions)
- ✅ Scientifically validated (Kiesel et al., 2008)
- ✅ Analogous to median RT in behavioral data

### Phase 2: Fractional Area Latency Implementation

#### 1. Core Function: `fractional_area_latency()`
**Location**: [src/eeg/measures.py:51-177](src/eeg/measures.py#L51-L177)

**Features**:
- Trapezoidal integration for accurate area calculation
- Automatic polarity detection (handles negative components like N1)
- Linear interpolation for sub-sample precision
- Configurable fraction (0.5 = midpoint, 0.2 = onset, 0.8 = offset)

**Scientific Basis**: Kiesel et al. (2008) showed FAL has **lower standardized measurement error** than peak latency.

#### 2. Integration into Analysis Pipeline
**Location**: [scripts/run_analysis.py:32, 359-391, 543](scripts/run_analysis.py)

**Changes**:
1. Import `fractional_area_latency` from measures module
2. Compute FAL for each condition within collapsed localizer FWHM window
3. Add `latency_frac_area_ms` column to `condition_measurements.csv`

**Error Handling**: FAL failures record NaN with warning (non-fatal)

#### 3. Comprehensive Test Suite
**Location**: [tests/test_measures.py](tests/test_measures.py)

**Coverage** (17/17 tests passing):
- ✅ Positive/negative components (P1, N1, P3b)
- ✅ Auto polarity detection
- ✅ Multiple fractions (20%, 50%, 80%)
- ✅ Symmetric vs. skewed waveforms
- ✅ Real-world N1 simulation (based on landing_on_2 data)
- ✅ Sub-sample interpolation
- ✅ Error handling (invalid windows, fractions, zero area)

**Test Infrastructure**:
- `tests/conftest.py`: Python path setup
- `tests/__init__.py`: Test package init

#### 4. Documentation Updates
**Location**: [README.md](README.md)

**Additions**:
1. FAL explanation in architecture section (line 226)
2. CSV output documentation (line 55)
3. **New section**: "Statistical Analysis Ready" (lines 250-277)
   - Explains `peak_latency_ms` (fixed) vs `latency_frac_area_ms` (varies)
   - Example N1 data showing condition differences
   - Recommended statistical tests
   - Scientific references

### Phase 2: Validation Results

**Test Suite**: ✅ 17/17 tests passing
```bash
pytest tests/test_measures.py -v
============================= 17 passed in 0.08s ==============================
```

**Real Data (landing_on_2, N1 component)**:
| Condition | peak_latency_ms | latency_frac_area_ms | Δ |
|-----------|-----------------|----------------------|---|
| increasing 1 to 2 | 168.0 | 172.8 | +4.8 ms |
| Cardinality2 | 168.0 | 174.6 | +6.6 ms |
| 3 to 2 | 168.0 | 175.9 | +7.9 ms |
| 4 to 2 | 168.0 | 175.6 | +7.6 ms |
| 5 to 2 | 168.0 | 177.2 | +9.2 ms |

**Key Result**: 4.4 ms latency difference across conditions — **now statistically testable!**

### Phase 2: Files Created/Modified

**New Files** (3):
- ✅ `tests/test_measures.py` (17 comprehensive tests)
- ✅ `tests/conftest.py` (pytest configuration)
- ✅ `tests/__init__.py` (test package)

**Modified Files** (3):
- ✅ `src/eeg/measures.py`: Added `fractional_area_latency()` (127 lines)
- ✅ `scripts/run_analysis.py`: Integrated FAL computation
- ✅ `README.md`: Added statistical analysis documentation

**Output Files Updated**:
- ✅ All `condition_measurements.csv` now include `latency_frac_area_ms`

---

## Phase 1: GFP-Based Analysis (Jan 2025)

## Completed Tasks

### 1. Core GFP Module (✅ COMPLETE)
**File:** `src/eeg/gfp_measures.py`

**Functions Implemented:**
- `compute_gfp(data)` - Calculate GFP as std across all channels
- `find_gfp_peak(gfp, times_ms, search_range_ms)` - Find peak within a priori range
- `compute_fwhm_window(gfp, times_ms, peak_idx)` - Calculate FWHM using scipy
- `gfp_peak_and_window(data, times_ms, search_range_ms)` - Main entry point

**Test Coverage:** 16/16 tests passing in `tests/test_gfp_measures.py`

### 2. Collapsed Localizer (✅ COMPLETE)
**File:** `src/eeg/collapsed_localizer.py`

**Complete rewrite to:**
- Average ALL conditions together (collapsed localizer principle)
- Use GFP instead of ROI channels
- Call `gfp_peak_and_window()` for each requested component
- Support selective component analysis via `requested_components` parameter

**Key Change:** Removed all ROI-based logic, polarity detection, and fallback mechanisms

### 3. Plotting (✅ COMPLETE)
**File:** `src/eeg/plots.py`

**Function:** `make_collapsed_localizer_figure(localizer_results, ...)`

**Plot Features:**
- GFP trace (blue line, all channels)
- Peak marker (red dashed line)
- FWHM window (pink shaded region)
- Search range boundaries (dotted lines)
- Stimulus onset marker (gray line)
- Metrics annotation box (peak GFP, FWHM, window)

### 4. Analysis Pipeline (✅ COMPLETE)
**File:** `scripts/run_analysis.py`

**Major Refactor:**
- Removed old per-condition peak detection
- Removed ROI-based channel aggregation
- Simplified to focus on collapsed localizer as primary output
- Added informative error messages for troubleshooting
- Progress reporting for user feedback

**Output:** Single collapsed localizer plot per analysis showing GFP-based results

### 5. Measurement Utilities (✅ COMPLETE)
**File:** `src/eeg/measures.py`

**Simplified to:**
- Removed `peak_amplitude_and_latency()` function entirely
- Removed all fallback logic
- Kept only `mean_amplitude()` for basic measurements

**Tests Updated:** `tests/test_measures.py` now only tests basic utilities

### 6. Configuration (✅ COMPLETE)
**File:** `configs/components.yaml`

**Updated:**
- P3b search range narrowed to [320, 420]ms to avoid epoch edge
- All search ranges are now "a priori" ranges (literature-based)

**Analysis YAMLs:**
- Updated all 4 analysis configs to exclude P3b (epoch limitation)
- Added comments explaining why P3b excluded

### 7. Tests (✅ COMPLETE - 18/18 PASSING)

**Test Files:**
- `tests/test_gfp_measures.py` - 16 tests for GFP implementation
- `tests/test_measures.py` - 2 tests for basic utilities

**Coverage:**
- GFP computation (3 tests)
- Peak finding in search ranges (4 tests)
- FWHM calculation (4 tests)
- End-to-end pipeline (3 tests)
- Integration with MNE structures (2 tests)
- Input validation (2 tests)

### 8. Documentation (✅ COMPLETE)

**Created:**
- `docs/GFP_ANALYSIS_GUIDE.md` - Comprehensive 400-line guide covering:
  - Scientific rationale
  - How the approach works
  - Interpreting results
  - Configuration guidance
  - Publication templates
  - Troubleshooting

---

## Testing Results

### Unit Tests
```bash
pytest tests/test_gfp_measures.py tests/test_measures.py -v
# Result: 18/18 tests PASSED
```

### Integration Test
```bash
python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing.yaml
# Result: SUCCESS - Generated collapsed localizer plot
# Components: P1 (peak 108ms, FWHM 27ms), N1 (peak 172ms, FWHM 60ms)
```

### Full Pipeline
```bash
python scripts/run_all_analyses.py
# Result: 4/4 analyses PASSED
# - cardinality_within_small
# - from1_to_any
# - small_increasing_vs_decreasing
# - small_increasing_vs_decreasing_ACC1
```

---

## Files Modified

### New Files Created (3)
1. `src/eeg/gfp_measures.py` (269 lines)
2. `tests/test_gfp_measures.py` (327 lines)
3. `docs/GFP_ANALYSIS_GUIDE.md` (450 lines)

### Files Modified (6)
1. `src/eeg/collapsed_localizer.py` - Complete rewrite (180 lines)
2. `src/eeg/measures.py` - Simplified to 48 lines (was 109)
3. `src/eeg/plots.py` - Added `make_collapsed_localizer_figure()` (+ 118 lines)
4. `scripts/run_analysis.py` - Complete refactor (309 lines)
5. `tests/test_measures.py` - Simplified (38 lines)
6. `configs/components.yaml` - Updated P3b range

### Files Updated (4 analysis YAMLs)
1. `configs/analyses/small_increasing_vs_decreasing.yaml`
2. `configs/analyses/small_increasing_vs_decreasing_ACC1.yaml`
3. `configs/analyses/cardinality_within_small.yaml`
4. `configs/analyses/from1_to_any.yaml`

---

## Breaking Changes

### Removed Functions
- ❌ `peak_amplitude_and_latency()` from `measures.py`
- ❌ `_moving_average()` from `measures.py`
- ❌ Old `compute_collapsed_localizer()` signature (now uses GFP)
- ❌ All fallback mechanisms

### Changed Behavior
- ⚠️ **No fallbacks**: If component cannot be detected, analysis FAILS with error
- ⚠️ **GFP-only**: No ROI channel selection anymore
- ⚠️ **FWHM windows**: No more fixed ±20ms or ±50ms windows
- ⚠️ **Collapsed localizer required**: Cannot skip this step

### New Requirements
- ✅ `scipy` package (for `peak_widths` function)
- ✅ Component configs must have `window_ms` field
- ✅ Epochs must extend beyond component peaks (for FWHM calculation)

---

## Known Limitations

### P3b Component
**Issue:** P3b peaks at ~420-450ms, but epochs end at ~496ms. Insufficient samples on right side of peak for FWHM calculation.

**Solutions:**
1. **Recommended:** Extend epochs to ~550ms in preprocessing (future data)
2. **Alternative:** Narrow P3b search range to [300, 400]ms (current data)
3. **Current:** Exclude P3b from analyses (what we did)

**Status:** Documented in analysis YAMLs and user guide

### Epoch Duration Requirements
**General Rule:** Component search range should end at least 30-50ms before epoch end to allow FWHM calculation.

**Example:**
- If epoch ends at 500ms
- P3b search range should be [300, 450]ms max
- This leaves 50ms margin for FWHM calculation

---

## Scientific Validation

### Approach Validated By:
- ✅ Peer-reviewed literature (Lehmann & Skrandies, 1980)
- ✅ Recommended by Luck & Gaspelin (2017)
- ✅ Standard in topographic ERP analysis
- ✅ Prevents circular analysis (Kriegeskorte et al., 2009)

### Quality Assurance:
- ✅ Test-Driven Development (TDD) - tests written first
- ✅ Comprehensive test coverage (18 tests)
- ✅ Real data validation (4 analyses completed successfully)
- ✅ Publication-quality plots generated
- ✅ Detailed documentation provided

---

## Performance

### Analysis Speed
- **Single analysis:** ~2 seconds (24 subjects, 2 components)
- **All 4 analyses:** ~10 seconds total
- **No significant slowdown** from old approach

### Output Quality
- **Plot size:** ~350 KB per collapsed localizer plot
- **Resolution:** 300 DPI (publication-ready)
- **All analyses:** Under 2 MB total

---

## Next Steps for Users

### Immediate Use
1. ✅ Run analyses: `python scripts/run_all_analyses.py`
2. ✅ Review plots in `docs/assets/plots/`
3. ✅ Read guide: `docs/GFP_ANALYSIS_GUIDE.md`

### For Publication
1. Use methods template from guide
2. Include collapsed localizer figure in paper
3. Cite key references (provided in guide)
4. Report FWHM values in results section

### For Future Data Collection
1. **Extend epochs** to ~550ms to capture P3b fully
2. Keep using same component search ranges (validated)
3. Document any deviations from a priori ranges

---

## Support & Maintenance

### If Component Detection Fails
1. Check error message carefully
2. Consult troubleshooting section in guide
3. Verify component expected in your paradigm
4. Check data quality and preprocessing

### If Results Look Odd
1. Verify search ranges match your paradigm
2. Check that epochs are long enough
3. Confirm adequate number of trials/subjects
4. Review GFP trace for artifacts

### For Questions
- Read: `docs/GFP_ANALYSIS_GUIDE.md`
- Check: Error messages (they're informative!)
- Review: Test files for usage examples

---

## Acknowledgments

This implementation follows best practices from:
- Steven J. Luck's ERP textbook and publications
- MNE-Python documentation and community
- Topographic ERP analysis literature (Lehmann, Murray, et al.)
- Open science principles (transparent, reproducible)

---

## Version History

**v1.0.0** (2025-01-12)
- Initial GFP-based implementation
- Complete pipeline refactor
- Comprehensive testing and documentation
- All 4 analyses passing

---

*For detailed usage instructions, see `docs/GFP_ANALYSIS_GUIDE.md`*
