# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:49:18

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 4

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | -2.51 µV | 2.11 | 0.47 | [-7.70, 0.04] |
| 4 to 2 | 24 | -4.21 µV | 2.46 | 0.50 | [-9.25, -0.71] |
| 5 to 3 | 24 | -3.86 µV | 2.36 | 0.48 | [-8.62, -0.11] |
| 6 to 4 | 24 | -3.33 µV | 2.32 | 0.47 | [-9.81, -0.71] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 182.30 ms | 11.82 | 2.64 | [162.94, 203.39] |
| 4 to 2 | 24 | 178.15 ms | 8.25 | 1.68 | [163.75, 199.96] |
| 5 to 3 | 24 | 176.44 ms | 9.82 | 2.00 | [157.35, 207.52] |
| 6 to 4 | 24 | 176.26 ms | 11.27 | 2.30 | [158.77, 202.43] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 22 | 2.22 µV | 1.71 | 0.37 | [-0.18, 7.32] |
| 4 to 2 | 15 | 1.77 µV | 1.03 | 0.27 | [0.02, 3.57] |
| 5 to 3 | 17 | 1.81 µV | 1.23 | 0.30 | [-0.13, 3.48] |
| 6 to 4 | 15 | 2.45 µV | 1.54 | 0.40 | [0.23, 5.66] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 22 | 115.66 ms | 5.24 | 1.12 | [105.53, 125.41] |
| 4 to 2 | 15 | 116.76 ms | 4.12 | 1.06 | [110.37, 127.38] |
| 5 to 3 | 17 | 112.91 ms | 5.81 | 1.41 | [102.40, 123.96] |
| 6 to 4 | 15 | 114.14 ms | 4.96 | 1.28 | [104.05, 124.30] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 3.89 µV | 2.33 | 0.52 | [0.32, 9.09] |
| 4 to 2 | 19 | 3.38 µV | 2.45 | 0.56 | [0.11, 7.55] |
| 5 to 3 | 20 | 3.50 µV | 1.94 | 0.43 | [0.06, 8.03] |
| 6 to 4 | 19 | 3.31 µV | 2.44 | 0.56 | [0.07, 7.25] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 479.27 ms | 13.67 | 3.06 | [458.78, 511.87] |
| 4 to 2 | 19 | 475.55 ms | 17.42 | 4.00 | [431.97, 501.99] |
| 5 to 3 | 20 | 471.53 ms | 18.41 | 4.12 | [421.85, 495.70] |
| 6 to 4 | 19 | 481.96 ms | 23.94 | 5.49 | [434.31, 533.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 4.26, *p* = 0.009, η²_G = 0.103
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 3.84 | 19 | = 0.007 | 0.91 [0.31, 1.41] | large | ** |
| 3 to 1 vs 5 to 3 | 2.30 | 19 | = 0.098 | 0.72 [0.02, 1.01] | medium | n.s. |
| 3 to 1 vs 6 to 4 | 1.34 | 19 | = 0.263 | 0.43 [-0.18, 0.78] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.84 | 19 | = 0.411 | -0.19 [-0.58, 0.27] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.71 | 19 | = 0.208 | -0.44 [-0.77, 0.10] | small | n.s. |
| 5 to 3 vs 6 to 4 | -1.27 | 19 | = 0.263 | -0.26 [-0.68, 0.18] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 410.95, BIC = 426.08
- Condition effect: *β* = -1.88, *SE* = 0.558, *z* = -3.366, *p* = 0.001

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.44, *p* = 0.074, η²_G = 0.037
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.76 | 19 | = 0.189 | 0.41 [-0.09, 0.88] | small | n.s. |
| 3 to 1 vs 5 to 3 | 2.00 | 19 | = 0.189 | 0.43 [-0.04, 0.94] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.91 | 19 | = 0.189 | 0.42 [-0.06, 0.92] | small | n.s. |
| 4 to 2 vs 5 to 3 | 0.53 | 19 | = 0.800 | 0.08 [-0.20, 0.66] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.44 | 19 | = 0.800 | 0.09 [-0.22, 0.63] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.09 | 19 | = 0.932 | 0.01 [-0.40, 0.45] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 661.99, BIC = 677.12
- Condition effect: *β* = -3.54, *SE* = 1.997, *z* = -1.773, *p* = 0.076


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.71, *p* = 0.068, η²_G = 0.141
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.52 | 8 | = 0.327 | 0.74 [-0.31, 0.81] | medium | n.s. |
| 3 to 1 vs 5 to 3 | 1.14 | 8 | = 0.344 | 0.41 [-0.26, 0.83] | small | n.s. |
| 3 to 1 vs 6 to 4 | -0.43 | 8 | = 0.676 | -0.13 [-0.76, 0.41] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | -1.34 | 8 | = 0.327 | -0.48 [-0.90, 0.39] | small | n.s. |
| 4 to 2 vs 6 to 4 | -3.11 | 8 | = 0.087 | -1.15 [-1.65, -0.08] | large | n.s. |
| 5 to 3 vs 6 to 4 | -1.89 | 8 | = 0.285 | -0.69 [-0.95, 0.35] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 249.23, BIC = 262.64
- Condition effect: *β* = -0.52, *SE* = 0.413, *z* = -1.254, *p* = 0.210

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.57, *p* = 0.223, η²_G = 0.107
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -1.17 | 8 | = 0.552 | -0.65 [-0.72, 0.40] | medium | n.s. |
| 3 to 1 vs 5 to 3 | 0.11 | 8 | = 0.918 | 0.04 [-0.03, 1.12] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 0.82 | 8 | = 0.653 | 0.22 [-0.13, 1.09] | small | n.s. |
| 4 to 2 vs 5 to 3 | 1.55 | 8 | = 0.477 | 0.66 [-0.05, 1.34] | medium | n.s. |
| 4 to 2 vs 6 to 4 | 1.89 | 8 | = 0.477 | 1.15 [-0.06, 1.44] | large | n.s. |
| 5 to 3 vs 6 to 4 | 0.42 | 8 | = 0.819 | 0.16 [-0.64, 0.63] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 425.33, BIC = 438.73
- Condition effect: *β* = 1.00, *SE* = 1.479, *z* = 0.677, *p* = 0.498


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.66, *p* = 0.584, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.22 | 16 | = 0.739 | 0.23 [-0.17, 0.85] | small | n.s. |
| 3 to 1 vs 5 to 3 | 0.55 | 16 | = 0.739 | 0.17 [-0.36, 0.61] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 1.12 | 16 | = 0.739 | 0.36 [-0.34, 0.66] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.34 | 16 | = 0.739 | -0.09 [-0.64, 0.36] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.44 | 16 | = 0.739 | 0.12 [-0.41, 0.62] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.80 | 16 | = 0.739 | 0.22 [-0.45, 0.55] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 348.73, BIC = 362.87
- Condition effect: *β* = -0.53, *SE* = 0.588, *z* = -0.894, *p* = 0.371

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.91, *p* = 0.444, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.18 | 16 | = 0.415 | 0.35 [-0.17, 0.85] | small | n.s. |
| 3 to 1 vs 5 to 3 | 1.30 | 16 | = 0.415 | 0.35 [-0.12, 0.88] | small | n.s. |
| 3 to 1 vs 6 to 4 | -0.12 | 16 | = 0.970 | -0.04 [-0.56, 0.43] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | 0.04 | 16 | = 0.970 | 0.01 [-0.50, 0.49] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.26 | 16 | = 0.415 | -0.29 [-0.83, 0.22] | small | n.s. |
| 5 to 3 vs 6 to 4 | -1.13 | 16 | = 0.415 | -0.29 [-0.83, 0.19] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 673.22, BIC = 687.36
- Condition effect: *β* = -4.84, *SE* = 4.615, *z* = -1.048, *p* = 0.294


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.009). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 0.91)
**N1 latency:** Marginal trend toward condition differences (*p* = 0.074)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.068)

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
- Pingouin 0.5.5

### References

- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
