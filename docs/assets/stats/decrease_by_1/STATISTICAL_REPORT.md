# Statistical Analysis Report: tables

**Generated:** 2025-10-13 19:59:39

---

## 1. Analysis Overview

**Total Measurements:** 81
**Number of Subjects:** 15
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
| 2 to 1 | 3 | 178.24 ms | 4.41 | 2.55 | [174.96, 183.25] |
| 3 to 2 | 1 | 173.40 ms | n/a | n/a | [173.40, 173.40] |
| 4 to 3 | 6 | 176.81 ms | 4.29 | 1.75 | [171.83, 184.29] |
| 5 to 4 | 3 | 175.71 ms | 2.79 | 1.61 | [173.94, 178.92] |
| 6 to 5 | 4 | 175.83 ms | 6.69 | 3.35 | [165.94, 180.64] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 3 | -4.48 µV | 3.87 | 2.23 | [-8.86, -1.52] |
| 3 to 2 | 1 | -3.76 µV | n/a | n/a | [-3.76, -3.76] |
| 4 to 3 | 6 | -3.72 µV | 1.38 | 0.56 | [-5.87, -2.13] |
| 5 to 4 | 3 | -3.94 µV | 0.80 | 0.46 | [-4.67, -3.08] |
| 6 to 5 | 4 | -4.57 µV | 3.29 | 1.64 | [-8.95, -1.45] |


### 2.2 P1 Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 3 | 118.93 ms | 4.32 | 2.49 | [114.02, 122.13] |
| 4 to 3 | 3 | 115.09 ms | 6.74 | 3.89 | [107.42, 120.06] |
| 5 to 4 | 1 | 116.75 ms | n/a | n/a | [116.75, 116.75] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 3 | 4.39 µV | 3.66 | 2.11 | [1.79, 8.57] |
| 4 to 3 | 3 | 4.20 µV | 0.17 | 0.10 | [4.03, 4.37] |
| 5 to 4 | 1 | 5.99 µV | n/a | n/a | [5.99, 5.99] |


### 2.3 P3b Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 5 | 507.26 ms | 11.62 | 5.20 | [492.32, 523.58] |
| 3 to 2 | 2 | 507.26 ms | 9.80 | 6.93 | [500.33, 514.19] |
| 4 to 3 | 4 | 505.10 ms | 7.14 | 3.57 | [495.45, 512.52] |
| 5 to 4 | 4 | 506.78 ms | 5.75 | 2.87 | [499.68, 513.17] |
| 6 to 5 | 1 | 503.46 ms | n/a | n/a | [503.46, 503.46] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 5 | 5.28 µV | 3.46 | 1.55 | [2.09, 9.88] |
| 3 to 2 | 2 | 5.97 µV | 1.43 | 1.01 | [4.96, 6.98] |
| 4 to 3 | 4 | 5.20 µV | 1.68 | 0.84 | [2.71, 6.28] |
| 5 to 4 | 4 | 4.20 µV | 1.49 | 0.74 | [2.83, 6.09] |
| 6 to 5 | 1 | 3.02 µV | n/a | n/a | [3.02, 3.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 108.31, BIC = 114.14
- Condition effect: *β* = -4.10, *SE* = 3.399, *z* = -1.205, *p* = 0.228

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 82.85, BIC = 88.68
- Condition effect: *β* = -0.23, *SE* = 1.169, *z* = -0.200, *p* = 0.842


### 3.2 P1 Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 7.06, BIC = 6.79
- Condition effect: *β* = -6.61, *SE* = 0.000, *z* = -49542.180, *p* < .001

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

_LMM results not available._


### 3.3 P3b Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 120.10, BIC = 125.51
- Condition effect: *β* = 6.18, *SE* = 2.106, *z* = 2.935, *p* = 0.003

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 81.83, BIC = 87.24
- Condition effect: *β* = 0.69, *SE* = 1.706, *z* = 0.404, *p* = 0.686


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
