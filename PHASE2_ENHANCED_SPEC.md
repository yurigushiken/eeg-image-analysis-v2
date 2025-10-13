# Phase 2 Enhanced Specification: Consultant Refinements Integrated

**Date**: October 12, 2024
**Status**: READY FOR IMPLEMENTATION

---

## Consultant Refinements Summary

### Refinement 1: Enhanced QC Metrics (Phase 2A)
**What**: Add quality control columns to `subject_measurements.csv`
**Why**: Transparency in data quality → identify outliers, justify exclusions
**Columns to add**:
- `n_epochs`: Number of trials included for this subject-condition
- `baseline_noise_uv`: Baseline noise level (std dev in baseline period)
- `signal_to_noise_ratio`: Peak amplitude / baseline noise
- `measurement_window_ms`: Document the exact window used (from collapsed localizer)

### Refinement 2: Enhanced Statistics YAML (Phase 2B)
**What**: More detailed statistical configuration
**Why**: Full control over correction strategies and model specifications
**Additions**:
- `correction_family`: Apply correction within component (safer) or across all tests (stricter)
- Enhanced `linear_mixed_model` section with explicit random effects
- `primary` flag for dependent variables (primary vs exploratory analyses)

### Refinement 3: Contextualized Plots (Phase 2C)
**What**: Include measurement window info in figure captions
**Why**: Links statistical results directly to collapsed localizer decisions
**Implementation**: Auto-generate captions like "N1 latencies measured within FWHM window [140.2, 212.6] ms centered at 168 ms"

---

## Phase 2A: Enhanced Subject-Level Data Collection

### Updated CSV Schema: `subject_measurements.csv`

```csv
subject_id,component,condition,latency_frac_area_ms,mean_amplitude_roi,n_epochs,baseline_noise_uv,snr,peak_latency_ms,window_start_ms,window_end_ms,fwhm_ms
sub-02,N1,Cardinality1,171.2,-2.5,45,0.32,7.8,168.0,140.2,212.6,72.4
sub-02,N1,Cardinality2,173.8,-2.3,42,0.28,8.2,168.0,140.2,212.6,72.4
sub-02,N1,Cardinality3,175.1,-3.1,40,0.35,8.9,168.0,140.2,212.6,72.4
...
```

**New Columns Explained**:
- `n_epochs`: Trial count (QC: subjects with <8 epochs might be unreliable)
- `baseline_noise_uv`: Std dev in baseline period [-100, 0] ms (QC: >1.0 µV = noisy)
- `snr`: Signal-to-noise ratio = |mean_amplitude_roi| / baseline_noise (QC: <3.0 = poor)
- `peak_latency_ms`, `window_start_ms`, `window_end_ms`, `fwhm_ms`: Document collapsed localizer results

**Benefits**:
- ✅ Transparent QC → justify subject exclusions in publications
- ✅ Post-hoc filtering → re-run stats with different SNR thresholds
- ✅ Reviewer-ready → "We excluded subjects with SNR < 3.0..."
- ✅ Diagnostic → identify why a subject might be an outlier

### Implementation Code (Enhanced)

```python
# Inside subject loop in run_analysis.py
for item in sets:
    # ... existing condition selection ...

    evk = sub.average()  # Subject-level evoked
    subj_id = extract_subject_id(epochs, fif)

    for comp in cfg.components:
        comp_result = collapsed_results.get(comp)
        if comp_result is None:
            continue

        # Get collapsed localizer parameters
        peak_lat = comp_result['peak_latency_ms']
        window_start = comp_result['window_start_ms']
        window_end = comp_result['window_end_ms']
        fwhm = comp_result['fwhm_ms']

        # Get ROI channels
        comp_cfg = components_cfg.get(comp, {})
        roi_names = comp_cfg.get('rois', [])
        roi_channels = []
        for roi_name in roi_names:
            if roi_name in electrodes_cfg:
                roi_channels.extend(electrodes_cfg[roi_name])

        if not roi_channels:
            continue

        try:
            # Extract subject ROI curve
            roi_data = evk.copy().pick_channels(roi_channels, ordered=False)
            roi_curve = roi_data.data.mean(axis=0) * 1e6
            times_ms_subj = evk.times * 1000.0

            # === QC Metric 1: Baseline Noise ===
            baseline_mask = (times_ms_subj >= baseline[0]) & (times_ms_subj <= baseline[1])
            baseline_noise_uv = float(np.std(roi_curve[baseline_mask]))

            # === Measurement 1: Mean Amplitude ===
            subj_mean_amp = float(np.mean(
                roi_curve[(times_ms_subj >= window_start) & (times_ms_subj <= window_end)]
            ))

            # === QC Metric 2: Signal-to-Noise Ratio ===
            snr = abs(subj_mean_amp) / baseline_noise_uv if baseline_noise_uv > 0 else float('nan')

            # === Measurement 2: Fractional Area Latency ===
            comp_polarity = "negative" if comp.upper().startswith("N") else "positive"
            subj_fal = fractional_area_latency(
                signal=roi_curve,
                times_ms=times_ms_subj,
                window_ms=(window_start, window_end),
                fraction=0.5,
                polarity=comp_polarity
            )

            # Record subject measurement with QC metrics
            subject_measurements.append({
                "subject_id": subj_id,
                "component": comp,
                "condition": item['name'],
                "latency_frac_area_ms": subj_fal,
                "mean_amplitude_roi": subj_mean_amp,
                "n_epochs": epoch_count,
                "baseline_noise_uv": baseline_noise_uv,
                "snr": snr,
                "peak_latency_ms": float(peak_lat),
                "window_start_ms": float(window_start),
                "window_end_ms": float(window_end),
                "fwhm_ms": float(fwhm),
            })

        except Exception as e:
            print(f"    Warning: Subject {subj_id} {comp} {item['name']} measurement failed: {e}")
            # Record NaN for failed measurement but preserve QC info where possible
            subject_measurements.append({
                "subject_id": subj_id,
                "component": comp,
                "condition": item['name'],
                "latency_frac_area_ms": float('nan'),
                "mean_amplitude_roi": float('nan'),
                "n_epochs": epoch_count,
                "baseline_noise_uv": float('nan'),
                "snr": float('nan'),
                "peak_latency_ms": float(peak_lat),
                "window_start_ms": float(window_start),
                "window_end_ms": float(window_end),
                "fwhm_ms": float(fwhm),
            })

# Save with expanded fieldnames
fieldnames = [
    "subject_id", "component", "condition",
    "latency_frac_area_ms", "mean_amplitude_roi",
    "n_epochs", "baseline_noise_uv", "snr",
    "peak_latency_ms", "window_start_ms", "window_end_ms", "fwhm_ms"
]
```

---

## Phase 2B: Enhanced Statistics YAML

### Enhanced Schema: `configs/statistics/default.yaml`

```yaml
# Statistical Analysis Configuration (Enhanced with Consultant Recommendations)

analysis_id: "cardinality_within_small"

# Dependent Variables (with primary/exploratory designation)
dependent_variables:
  - name: "latency_frac_area_ms"
    label: "Fractional Area Latency"
    units: "ms"
    primary: true  # Primary hypothesis (stricter α correction)

  - name: "mean_amplitude_roi"
    label: "Mean Amplitude"
    units: "µV"
    primary: false  # Exploratory (reported but less stringent)

# Components to analyze
components: ["N1", "P1", "P3b"]

# Independent variables
factors:
  - name: "condition"
    type: "categorical"
    levels: null  # Auto-detect from data

# Quality Control Filters (applied before statistical tests)
qc_filters:
  min_epochs: 8  # Exclude subjects with fewer epochs
  min_snr: 3.0  # Exclude subjects with SNR < 3.0
  max_baseline_noise_uv: 1.5  # Exclude subjects with excessive noise
  exclude_subjects: []  # Manual exclusion list (e.g., ["sub-05", "sub-12"])

# Multiple Comparison Correction Strategy
correction_family: "component"  # "component", "analysis", or "global"
# - "component": Correct within each component separately (recommended)
# - "analysis": Correct across all DVs within this analysis
# - "global": Correct across all tests in all analyses (most conservative)

# Statistical Tests
tests:
  # Test 1: Repeated-Measures ANOVA
  repeated_measures_anova:
    enabled: true
    method: "pingouin"
    within: "condition"
    subject: "subject_id"
    correction: "auto"  # GG or HF sphericity correction
    effect_size: "ng2"  # Use generalized eta-squared (recommended)
    # Options: "np2" (partial), "n2" (eta-squared), "ng2" (generalized)

    # Save detailed results
    save_sphericity_test: true  # Mauchly's test results
    save_epsilon: true  # GG/HF epsilon values
    save_posthoc_power: false  # Requires statsmodels

  # Test 2: Pairwise Comparisons
  pairwise_tests:
    enabled: true
    method: "pingouin"
    parametric: true
    padjust: "fdr_bh"  # FDR Benjamini-Hochberg (recommended)
    # Options: "none", "bonf", "holm", "fdr_bh", "fdr_by"
    tail: "two-sided"
    alpha: 0.05
    effect_size: "cohen"  # Cohen's d

    # Confidence intervals
    confidence_level: 0.95

  # Test 3: Linear Mixed-Effects Model
  linear_mixed_model:
    enabled: true
    method: "statsmodels"

    # Model specification
    formula: "latency_frac_area_ms ~ C(condition)"  # Fixed effects
    groups: "subject_id"  # Random effects grouping

    # Random effects structure
    re_formula: "1"  # Random intercept only (simplest)
    # Options:
    #   "1" = random intercept
    #   "~1 + condition" = random intercept + random slopes
    #   "~0 + condition" = random slopes only (no intercept)

    # Fitting options
    method_fit: "lbfgs"  # Optimization algorithm
    reml: true  # Use REML (vs ML) - recommended for small samples

    # Model comparison (optional)
    compare_models:
      enabled: false
      null_model: "latency_frac_area_ms ~ 1"  # Intercept-only model

    # Diagnostics
    check_convergence: true
    save_residuals: false  # For diagnostic plots

# Output Options
outputs:
  save_json: true  # Full results
  save_txt: true  # Human-readable APA summary
  save_csv: true  # Tables (ANOVA, pairwise, etc.)
  save_filtered_data: true  # CSV of data after QC filters
  plots: true

# Plot Configurations (Enhanced with measurement window info)
plots:
  boxplot:
    enabled: true
    show_points: true
    show_mean: true
    show_measurement_window: true  # Add window info to caption

  violin:
    enabled: true
    inner: "box"
    show_measurement_window: true

  raincloud:
    enabled: false  # Requires ptitprince

  effect_size:
    enabled: true
    show_ci: true
    threshold_lines: [0.2, 0.5, 0.8]  # Small, medium, large

  diagnostic:
    qq_plot: false  # Normality check
    residual_plot: false  # LMM diagnostics

# Reporting Options
reporting:
  alpha: 0.05
  report_all: true  # Include non-significant results
  apa_style: true
  decimal_places: 3
  include_bayes_factors: false  # Requires pingouin >=0.5

  # Auto-generate summary statements
  auto_summary: true  # "N1 latencies differed significantly across conditions..."

  # Include effect size interpretation
  interpret_effect_sizes: true  # "large effect", "medium effect", etc.
```

### Key Enhancements Explained

**1. `correction_family`**: Controls correction scope
- `"component"`: Safer, tests N1 separately from P1 (recommended)
- `"analysis"`: Stricter, corrects across all DVs in this analysis
- `"global"`: Most conservative, corrects across everything

**2. Enhanced LMM specification**:
- Explicit `re_formula` for random effects structure
- Model comparison options
- Convergence checking

**3. `primary` flag for DVs**:
- Primary hypotheses get full correction
- Exploratory analyses reported but flagged

**4. QC filters**:
- Applied before stats run
- Documented in output
- Reproducible exclusion criteria

---

## Phase 2C: Enhanced Visualization with Context

### Updated Plot Function Signature

```python
def plot_condition_comparison(
    data: pd.DataFrame,
    dv: str,
    component: str,
    title: str,
    output_path: Path,
    plot_type: str = "boxplot",
    measurement_window: Optional[Tuple[float, float]] = None,  # NEW
    peak_latency: Optional[float] = None,  # NEW
    dpi: int = 300
):
    """
    Create condition comparison plot with measurement window context.

    Args:
        measurement_window: (start, end) in ms from collapsed localizer
        peak_latency: Peak latency in ms
        ... (other args)
    """
    # ... plotting code ...

    # Add caption with measurement window
    if measurement_window and peak_latency:
        caption = (
            f"{component} {dv} measured within FWHM window "
            f"[{measurement_window[0]:.1f}, {measurement_window[1]:.1f}] ms "
            f"centered at {peak_latency:.0f} ms (collapsed localizer)"
        )

        # Add as figure text below plot
        fig.text(
            0.5, 0.02, caption,
            ha='center', fontsize=9, style='italic',
            wrap=True, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3)
        )
```

**Example Output Caption**:
> "N1 Fractional Area Latency measured within FWHM window [140.2, 212.6] ms centered at 168 ms (collapsed localizer)"

**Benefits**:
- ✅ Links stats plot directly to collapsed localizer figure
- ✅ Reviewer transparency → "How did you choose this window?"
- ✅ Publication-ready → copy caption to figure legend

---

## Phase 2A: TDD Test Specification

### Test File: `tests/test_subject_measurements.py`

```python
"""Tests for subject-level measurement collection (Phase 2A)."""
import pytest
import numpy as np
import pandas as pd
from pathlib import Path


class TestSubjectMeasurementCollection:
    """Test suite for Phase 2A subject-level data collection."""

    def test_csv_has_required_columns(self):
        """Test that subject_measurements.csv has all required columns."""
        # After running analysis, check CSV structure
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first to generate subject data")

        df = pd.read_csv(csv_path)

        required_cols = [
            "subject_id", "component", "condition",
            "latency_frac_area_ms", "mean_amplitude_roi",
            "n_epochs", "baseline_noise_uv", "snr",
            "peak_latency_ms", "window_start_ms", "window_end_ms", "fwhm_ms"
        ]

        for col in required_cols:
            assert col in df.columns, f"Missing required column: {col}"

    def test_subject_level_granularity(self):
        """Test that data is at subject × component × condition level."""
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first")

        df = pd.read_csv(csv_path)

        # Each subject-component-condition should appear once
        grouped = df.groupby(['subject_id', 'component', 'condition']).size()
        assert all(grouped == 1), "Duplicate subject-component-condition rows found"

    def test_qc_metrics_reasonable(self):
        """Test that QC metrics are in reasonable ranges."""
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first")

        df = pd.read_csv(csv_path)

        # Baseline noise should be positive and reasonable
        assert (df['baseline_noise_uv'] > 0).all(), "Baseline noise must be positive"
        assert (df['baseline_noise_uv'] < 10.0).all(), "Baseline noise unreasonably high"

        # SNR should be positive
        assert (df['snr'] > 0).all(), "SNR must be positive"

        # n_epochs should be reasonable
        assert (df['n_epochs'] >= 1).all(), "Must have at least 1 epoch"
        assert (df['n_epochs'] <= 500).all(), "Too many epochs (check data)"

    def test_measurement_window_consistency(self):
        """Test that measurement window is consistent within component."""
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first")

        df = pd.read_csv(csv_path)

        # Within each component, window should be identical for all subjects
        for comp in df['component'].unique():
            comp_data = df[df['component'] == comp]

            peak_lats = comp_data['peak_latency_ms'].unique()
            assert len(peak_lats) == 1, f"{comp}: peak_latency varies across subjects"

            window_starts = comp_data['window_start_ms'].unique()
            assert len(window_starts) == 1, f"{comp}: window_start varies across subjects"

    def test_latency_within_window(self):
        """Test that FAL is within the measurement window."""
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first")

        df = pd.read_csv(csv_path)

        # Remove NaN rows
        df_clean = df.dropna(subset=['latency_frac_area_ms'])

        # FAL should be between window_start and window_end
        within_window = (
            (df_clean['latency_frac_area_ms'] >= df_clean['window_start_ms']) &
            (df_clean['latency_frac_area_ms'] <= df_clean['window_end_ms'])
        )

        assert within_window.all(), "Some FAL values outside measurement window"

    def test_latency_varies_by_condition(self):
        """Test that latency varies across conditions (sanity check for stats)."""
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first")

        df = pd.read_csv(csv_path)

        # For N1, compute mean latency per condition
        n1_data = df[df['component'] == 'N1'].dropna(subset=['latency_frac_area_ms'])

        if len(n1_data) == 0:
            pytest.skip("No N1 data")

        condition_means = n1_data.groupby('condition')['latency_frac_area_ms'].mean()

        # Latencies should vary (not all identical)
        assert condition_means.std() > 0.1, "Latencies don't vary across conditions"

    def test_snr_correlates_with_n_epochs(self):
        """Test that SNR improves with more epochs (sanity check)."""
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first")

        df = pd.read_csv(csv_path).dropna(subset=['snr', 'n_epochs'])

        if len(df) < 10:
            pytest.skip("Not enough data for correlation test")

        # Compute correlation
        corr = df['snr'].corr(df['n_epochs'])

        # SNR should generally improve with more epochs (positive correlation)
        assert corr > 0, f"SNR vs n_epochs correlation is negative ({corr:.3f})"

    def test_no_duplicate_subject_ids(self):
        """Test that subject IDs are unique per condition-component."""
        csv_path = Path("docs/assets/tables/landing_on_2/subject_measurements.csv")

        if not csv_path.exists():
            pytest.skip("Run analysis first")

        df = pd.read_csv(csv_path)

        # Group by subject-component-condition and check for duplicates
        dup_check = df.groupby(['subject_id', 'component', 'condition']).size()
        duplicates = dup_check[dup_check > 1]

        assert len(duplicates) == 0, f"Found duplicate entries: {duplicates.to_dict()}"


class TestQCMetricCalculation:
    """Test QC metric calculation logic."""

    def test_baseline_noise_calculation(self):
        """Test baseline noise is computed correctly."""
        # Synthetic baseline data
        baseline_data = np.random.randn(100) * 0.5  # 0.5 µV noise

        noise = np.std(baseline_data)

        assert 0.3 < noise < 0.7, f"Baseline noise should be ~0.5 µV, got {noise:.3f}"

    def test_snr_calculation(self):
        """Test SNR calculation."""
        signal_amplitude = -3.0  # µV (N1 amplitude)
        baseline_noise = 0.5  # µV

        snr = abs(signal_amplitude) / baseline_noise

        assert snr == 6.0, f"SNR should be 6.0, got {snr:.1f}"

    def test_snr_handles_zero_noise(self):
        """Test SNR returns NaN for zero baseline noise (edge case)."""
        signal_amplitude = -3.0
        baseline_noise = 0.0

        snr = abs(signal_amplitude) / baseline_noise if baseline_noise > 0 else float('nan')

        assert np.isnan(snr), "SNR should be NaN when baseline noise is zero"
```

---

## Implementation Checklist for Phase 2A

### Pre-Implementation
- [x] ✅ Design enhanced CSV schema with QC metrics
- [x] ✅ Plan TDD test suite
- [x] ✅ Document consultant refinements

### Implementation
- [ ] Modify `run_analysis.py` to collect subject measurements
- [ ] Add QC metric calculations (baseline noise, SNR)
- [ ] Add measurement window documentation
- [ ] Update CSV export with new columns
- [ ] Create `tests/test_subject_measurements.py`
- [ ] Run tests (fail-first, then pass after implementation)

### Validation
- [ ] Run on `landing_on_2` analysis
- [ ] Verify CSV structure
- [ ] Check QC metrics are reasonable
- [ ] Confirm all tests pass
- [ ] Inspect data quality

---

## Ready to Implement Phase 2A!

With consultant refinements integrated, we now have:
✅ **Enhanced QC metrics** for data transparency
✅ **TDD test suite** (8 comprehensive tests)
✅ **Documented measurement windows** linking to collapsed localizer
✅ **Publication-ready data structure**

**Estimated time**: 30-40 minutes (implementation + testing)

Shall I proceed with the full Phase 2A implementation?
