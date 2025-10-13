# Statistical Analysis Workflow Guide

This guide explains how to run statistical analyses (Phase 2B & 2C) for your ERP data.

## Pipeline Overview

Your ERP analysis pipeline has **two separate stages**:

### Stage 1: ERP Analysis (Phase 1 & 2A)
- **Script**: `scripts/run_analysis.py` or `scripts/run_all_analyses.py`
- **Input**: Raw `.fif` epoch files
- **Output**: `docs/assets/tables/ANALYSIS_NAME/`
  - `subject_measurements.csv` ← **Input for statistics**
  - `collapsed_localizer_results.json`
  - `condition_measurements.csv`
  - Plots in `docs/assets/plots/`

### Stage 2: Statistical Analysis (Phase 2B & 2C)
- **Script**: `scripts/run_statistics.py` or `scripts/run_all_statistics.py`
- **Input**: `subject_measurements.csv` (from Stage 1)
- **Output**: `docs/assets/stats/ANALYSIS_NAME/`
  - `statistical_summary.json` (includes `fal_fraction: 0.5`)
  - ANOVA results (`.csv`)
  - Pairwise t-tests (`.csv`)
  - LMM results (`.json`)
  - Descriptive statistics (`.csv`)
  - Plots in `plots/` subdirectory

---

## Quick Start

### Option 1: Run Statistics for All Analyses (Recommended)

```bash
# Run statistics for all analyses automatically
python scripts/run_all_statistics.py
```

This will:
- Automatically find all `subject_measurements.csv` files
- Run statistics for each analysis using `configs/statistics/default.yaml` settings
- Output results to `docs/assets/stats/ANALYSIS_NAME/`

**Advantages**:
- Fast and convenient
- Consistent settings across all analyses
- No manual config file creation

---

### Option 2: Run Statistics for One Analysis

```bash
# Edit the config to point to your analysis
# Edit line 16 in configs/statistics/default.yaml:
#   input_csv: "docs/assets/tables/YOUR_ANALYSIS/subject_measurements.csv"

# Run statistics
python scripts/run_statistics.py --config configs/statistics/default.yaml
```

---

### Option 3: Create Individual Configs (Advanced)

If you need **different statistical settings for each analysis**, create individual config files:

```bash
# Step 1: Generate config files for each analysis
python scripts/create_stat_configs.py

# This creates:
#   configs/statistics/landing_on_2.yaml
#   configs/statistics/increase_by_1.yaml
#   etc.

# Step 2: Edit individual configs as needed
# (e.g., change SNR threshold, disable certain tests, etc.)

# Step 3a: Run one analysis
python scripts/run_statistics.py --config configs/statistics/landing_on_2.yaml

# Step 3b: Or run all (will use individual configs if they exist)
python scripts/run_all_statistics.py
```

---

## Configuration Options

The statistics configuration (`configs/statistics/default.yaml`) controls:

### Data Filtering
```yaml
filters:
  min_snr: 2.0      # Minimum signal-to-noise ratio
  dropna: true      # Drop rows with missing values
```

### Statistical Tests
```yaml
tests:
  anova:
    enabled: true
    correction: fdr_bh  # Multiple comparison correction

  pairwise:
    enabled: true
    effsize: cohen      # Effect size measure

  lmm:
    enabled: true
    fixed: condition    # Fixed effects formula
```

### Components & Measures
```yaml
components:
  - N1
  - P1
  - P3b

dependent_variables:
  - latency_frac_area_ms
  - mean_amplitude_roi
```

### Plots
```yaml
plots:
  enabled: true
  boxplot:
    enabled: true
    show_points: true
    include_window_context: true  # Show measurement window info

  violin:
    enabled: true

  effect_size:
    enabled: true
    show_ci: true  # Show 95% confidence intervals
```

---

## Understanding Your Analyses

You currently have **13 analyses**:

| Analysis ID | Description |
|-------------|-------------|
| `32_23` | Specific cardinality comparison |
| `32_23_22_33` | Multiple cardinality conditions |
| `cardinality_all` | All cardinality conditions |
| `cardinality_within_small` | Small number cardinalities |
| `decrease_by_1` | Decreasing sequences |
| `from1_to_any` | Sequences starting from 1 |
| `increase_by_1` | Increasing sequences |
| `landing_on_1` | Sequences ending on 1 |
| `landing_on_2` | Sequences ending on 2 |
| `large_increasing_vs_decreasing` | Large number comparisons |
| `large_increasing_vs_decreasing_ACC1` | Accurate trials only |
| `small_increasing_vs_decreasing` | Small number comparisons |
| `small_increasing_vs_decreasing_ACC1` | Accurate trials only |

Each can have independent statistical analyses run on it.

---

## Full Workflow Example

Here's the complete workflow from raw data to statistics:

```bash
# 1. Run ERP analyses for all datasets (Phase 1 & 2A)
python scripts/run_all_analyses.py

# This generates:
#   docs/assets/tables/*/subject_measurements.csv
#   docs/assets/plots/*.png

# 2. Run statistical analyses for all (Phase 2B & 2C)
python scripts/run_all_statistics.py

# This generates:
#   docs/assets/stats/*/statistical_summary.json
#   docs/assets/stats/*/anova_*.csv
#   docs/assets/stats/*/pairwise_*.csv
#   docs/assets/stats/*/plots/*.png

# 3. Check results
# - ERP plots: docs/assets/plots/
# - Statistics: docs/assets/stats/
# - Summary JSON: docs/assets/stats/*/statistical_summary.json
```

---

## Troubleshooting

### Problem: "No subject_measurements.csv files found"

**Solution**: Run Phase 1 first:
```bash
python scripts/run_all_analyses.py
```

### Problem: "ERROR plotting P1: No effect size data"

**Cause**: Insufficient paired observations for P1 after quality filtering.

**Solution**: This is expected if P1 has low SNR. Options:
1. Lower SNR threshold in config: `min_snr: 1.5`
2. Report P1 with caveats: "Insufficient data for pairwise tests"
3. Focus on N1 and P3b (recommended)

See [Phase 2C documentation] for details on handling missing data.

### Problem: Seaborn FutureWarning

**Status**: Fixed in latest version. If you see this, pull latest changes.

---

## Output Files Explained

### `statistical_summary.json`
Contains all statistical results plus metadata:
- Library versions (reproducibility)
- Analysis settings (including `fal_fraction: 0.5`)
- Missing data policy
- ANOVA results
- Pairwise test summaries
- LMM results

### ANOVA Files (`anova_*.csv`)
Repeated-measures ANOVA results with:
- F-statistic
- p-values (uncorrected and GG-corrected)
- Effect sizes (generalized eta-squared)
- Degrees of freedom

### Pairwise Files (`pairwise_*.csv`)
Pairwise t-tests with:
- Cohen's d effect sizes
- 95% confidence intervals
- Multiple comparison corrections
- p-values (uncorrected and corrected)

### LMM Files (`lmm_*.json`)
Linear mixed-effects model results:
- Fixed effects estimates
- AIC/BIC model fit statistics
- Convergence status

### Plots
- **Boxplots**: Distribution with individual points
- **Violin plots**: Density distributions
- **Effect size plots**: Forest plots with confidence intervals

All plots include measurement window information (FWHM) in captions for transparency.

---

## Questions?

See also:
- `IMPLEMENTATION_SUMMARY.md` - Overall project documentation
- `PHASE2_ENHANCED_SPEC.md` - Detailed Phase 2 specifications
- `configs/statistics/default.yaml` - Configuration options with comments
