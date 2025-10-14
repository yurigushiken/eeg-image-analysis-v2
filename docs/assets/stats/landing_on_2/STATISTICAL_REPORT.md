# Statistical Analysis Report: tables

**Generated:** 2025-10-13 20:00:23

---

## 1. Analysis Overview

**Total Measurements:** 54
**Number of Subjects:** 13
**Number of Conditions:** 5

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Latency (50% Fractional Area), Mean Amplitude (ROI)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ 2.0
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases after applying an SNR filter >= 2.0. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 1 | 170.07 ms | n/a | n/a | [170.07, 170.07] |
| 4 to 2 | 3 | 175.66 ms | 5.83 | 3.37 | [169.70, 181.36] |
| 5 to 2 | 4 | 169.59 ms | 1.16 | 0.58 | [168.17, 170.75] |
| Cardinality2 | 1 | 167.76 ms | n/a | n/a | [167.76, 167.76] |
| increasing 1 to 2 | 3 | 164.42 ms | 4.75 | 2.74 | [160.35, 169.64] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 1 | -4.01 µV | n/a | n/a | [-4.01, -4.01] |
| 4 to 2 | 3 | -5.50 µV | 1.01 | 0.58 | [-6.45, -4.45] |
| 5 to 2 | 4 | -7.01 µV | 1.97 | 0.98 | [-9.94, -5.80] |
| Cardinality2 | 1 | -2.78 µV | n/a | n/a | [-2.78, -2.78] |
| increasing 1 to 2 | 3 | -4.03 µV | 0.65 | 0.37 | [-4.55, -3.31] |


### 2.2 P1 Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 2 | 1 | 120.56 ms | n/a | n/a | [120.56, 120.56] |
| increasing 1 to 2 | 1 | 104.81 ms | n/a | n/a | [104.81, 104.81] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 2 | 1 | 2.89 µV | n/a | n/a | [2.89, 2.89] |
| increasing 1 to 2 | 1 | 1.06 µV | n/a | n/a | [1.06, 1.06] |


### 2.3 P3b Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 2 | 487.01 ms | 2.53 | 1.79 | [485.22, 488.80] |
| 4 to 2 | 1 | 481.07 ms | n/a | n/a | [481.07, 481.07] |
| 5 to 2 | 2 | 481.48 ms | 2.23 | 1.57 | [479.90, 483.05] |
| increasing 1 to 2 | 1 | 453.85 ms | n/a | n/a | [453.85, 453.85] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 2 | 5.17 µV | 0.58 | 0.41 | [4.76, 5.57] |
| 4 to 2 | 1 | 3.21 µV | n/a | n/a | [3.21, 3.21] |
| 5 to 2 | 2 | 4.76 µV | 2.32 | 1.64 | [3.11, 6.40] |
| increasing 1 to 2 | 1 | 1.41 µV | n/a | n/a | [1.41, 1.41] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 17.88, BIC = 21.27
- Condition effect: *β* = 8.78, *SE* = 2.408, *z* = 3.645, *p* < .001

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = -6.83, BIC = -3.44
- Condition effect: *β* = -2.61, *SE* = 0.888, *z* = -2.938, *p* = 0.003


### 3.2 P1 Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

_LMM did not converge or had numerical issues._

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = -128.67, BIC = -133.89
- Condition effect: *β* = -1.83, *SE* = 0.000, *z* = -3895754945514835.000, *p* < .001


### 3.3 P3b Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 32.85, BIC = 31.60
- Condition effect: *β* = -5.93, *SE* = 1.579, *z* = -3.757, *p* < .001

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 28.75, BIC = 27.50
- Condition effect: *β* = -1.96, *SE* = 0.866, *z* = -2.262, *p* = 0.024


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

#### Latency

**Boxplot:**

![N1 Latency Boxplot](plots/boxplot_N1_latency_frac_area_ms.png)

**Violin Plot:**

![N1 Latency Violin](plots/violin_N1_latency_frac_area_ms.png)

#### Amplitude

**Boxplot:**

![N1 Amplitude Boxplot](plots/boxplot_N1_mean_amplitude_roi.png)

**Violin Plot:**

![N1 Amplitude Violin](plots/violin_N1_mean_amplitude_roi.png)

### 5.2 P1 Component

#### Latency

**Boxplot:**

![P1 Latency Boxplot](plots/boxplot_P1_latency_frac_area_ms.png)

**Violin Plot:**

![P1 Latency Violin](plots/violin_P1_latency_frac_area_ms.png)

#### Amplitude

**Boxplot:**

![P1 Amplitude Boxplot](plots/boxplot_P1_mean_amplitude_roi.png)

**Violin Plot:**

![P1 Amplitude Violin](plots/violin_P1_mean_amplitude_roi.png)

### 5.3 P3b Component

#### Latency

**Boxplot:**

![P3b Latency Boxplot](plots/boxplot_P3b_latency_frac_area_ms.png)

**Violin Plot:**

![P3b Latency Violin](plots/violin_P3b_latency_frac_area_ms.png)

#### Amplitude

**Boxplot:**

![P3b Amplitude Boxplot](plots/boxplot_P3b_mean_amplitude_roi.png)

**Violin Plot:**

![P3b Amplitude Violin](plots/violin_P3b_mean_amplitude_roi.png)

---

## 6. Methods Summary (for Publication)

### ERP Measurement

ERP components were measured using a collapsed localizer approach, where component peaks were identified from the grand average of all conditions combined to avoid circular analysis (Luck & Gaspelin, 2017). Measurement windows were defined as the full-width at half-maximum (FWHM) around each peak. Component latency was quantified using the 50% fractional area latency (FAL), which represents the time point at which the cumulative area under the curve reaches 50% of its total value within the measurement window. This metric provides a robust estimate of component timing with lower measurement error than peak latency (Kiesel et al., 2008). Mean amplitude was computed as the average voltage within the FWHM window across predefined regions of interest (ROI).

Quality control filtering excluded subject-component measurements with signal-to-noise ratio (SNR) below 2.0.

### Statistical Analysis

Within-subjects repeated-measures analyses were conducted using:
- Repeated-measures ANOVA with Greenhouse-Geisser correction for sphericity violations (ε < 0.75)
- Post-hoc pairwise t-tests with false discovery rate (FDR) correction for multiple comparisons
- Linear mixed-effects models (LMM) with random intercepts for subjects to handle missing data

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.11
- MNE-Python 1.10.1
- Statsmodels 0.14.5

### References

- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
