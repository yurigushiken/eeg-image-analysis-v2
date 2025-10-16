# Statistical Analysis Report: tables

**Generated:** 2025-10-16 03:43:21

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
| 3 to 2 | 22 | -3.79 µV | 1.97 | 0.42 | [-8.01, -0.43] |
| 4 to 2 | 24 | -3.76 µV | 2.45 | 0.50 | [-8.93, -0.56] |
| 5 to 2 | 24 | -4.58 µV | 2.58 | 0.53 | [-9.18, -0.23] |
| increasing 1 to 2 | 22 | -3.17 µV | 1.61 | 0.34 | [-6.09, -0.59] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 22 | 174.51 ms | 10.88 | 2.32 | [156.01, 200.50] |
| 4 to 2 | 24 | 179.09 ms | 11.08 | 2.26 | [159.35, 208.91] |
| 5 to 2 | 24 | 176.12 ms | 9.76 | 1.99 | [158.04, 197.82] |
| increasing 1 to 2 | 22 | 175.12 ms | 14.75 | 3.15 | [151.58, 208.98] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 9 | 2.08 µV | 1.57 | 0.52 | [-0.06, 4.37] |
| 4 to 2 | 14 | 2.23 µV | 1.19 | 0.32 | [0.29, 4.35] |
| 5 to 2 | 16 | 2.14 µV | 1.67 | 0.42 | [0.19, 5.35] |
| increasing 1 to 2 | 11 | 1.18 µV | 0.80 | 0.24 | [0.17, 2.68] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 9 | 110.94 ms | 2.75 | 0.92 | [104.24, 113.65] |
| 4 to 2 | 14 | 112.86 ms | 1.20 | 0.32 | [110.58, 114.35] |
| 5 to 2 | 16 | 112.08 ms | 3.37 | 0.84 | [105.01, 118.47] |
| increasing 1 to 2 | 11 | 111.96 ms | 3.02 | 0.91 | [106.47, 116.79] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 4.22 µV | 3.18 | 0.75 | [0.31, 12.11] |
| 4 to 2 | 18 | 3.73 µV | 2.61 | 0.62 | [0.17, 8.65] |
| 5 to 2 | 18 | 3.61 µV | 2.47 | 0.58 | [0.49, 10.08] |
| increasing 1 to 2 | 17 | 3.53 µV | 2.82 | 0.68 | [0.03, 10.36] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 486.67 ms | 20.69 | 4.88 | [441.16, 530.94] |
| 4 to 2 | 18 | 478.48 ms | 19.50 | 4.60 | [431.61, 509.82] |
| 5 to 2 | 18 | 477.93 ms | 20.13 | 4.74 | [426.64, 514.84] |
| increasing 1 to 2 | 17 | 485.13 ms | 25.19 | 6.11 | [436.18, 536.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.01, *p* = 0.037, η²_G = 0.061
- Greenhouse-Geisser corrected: *p* = 0.056 (ε = 0.724)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.81 | 19 | = 0.442 | 0.17 [-0.33, 0.56] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.66 | 19 | = 0.170 | 0.39 [-0.02, 0.91] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | -1.88 | 19 | = 0.170 | -0.31 [-0.91, 0.07] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.79 | 19 | = 0.442 | 0.21 [-0.14, 0.72] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | -1.72 | 19 | = 0.170 | -0.47 [-0.78, 0.13] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -3.39 | 19 | = 0.018 | -0.69 [-1.16, -0.18] | medium | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 390.78, BIC = 405.91
- Condition effect: *β* = -0.14, *SE* = 0.463, *z* = -0.304, *p* = 0.761

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.71, *p* = 0.175, η²_G = 0.033
- Greenhouse-Geisser corrected: *p* = 0.192 (ε = 0.714)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -2.07 | 19 | = 0.274 | -0.49 [-0.67, 0.23] | small | n.s. |
| 3 to 2 vs 5 to 2 | -1.75 | 19 | = 0.274 | -0.23 [-0.62, 0.27] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.03 | 19 | = 0.979 | 0.01 [-0.46, 0.47] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.10 | 19 | = 0.428 | 0.27 [-0.16, 0.70] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.55 | 19 | = 0.274 | 0.41 [-0.11, 0.80] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.79 | 19 | = 0.525 | 0.20 [-0.39, 0.49] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 696.83, BIC = 711.96
- Condition effect: *β* = 3.61, *SE* = 2.410, *z* = 1.500, *p* = 0.134


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.51, *p* = 0.262, η²_G = 0.200
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -0.48 | 4 | = 0.787 | -0.37 [-0.99, 0.86] | small | n.s. |
| 3 to 2 vs 5 to 2 | -1.78 | 4 | = 0.288 | -0.45 [-1.36, 0.56] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.75 | 4 | = 0.288 | 0.71 [-0.59, 1.65] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -0.22 | 4 | = 0.837 | -0.16 [-0.97, 0.40] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.57 | 4 | = 0.288 | 1.30 [-0.29, 1.36] | large | n.s. |
| 5 to 2 vs increasing 1 to 2 | 2.12 | 4 | = 0.288 | 1.15 [-0.09, 1.67] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 179.97, BIC = 191.45
- Condition effect: *β* = 0.12, *SE* = 0.523, *z* = 0.235, *p* = 0.814

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.16, *p* = 0.923, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -1.51 | 4 | = 0.916 | -0.49 [-1.56, 0.43] | small | n.s. |
| 3 to 2 vs 5 to 2 | -0.21 | 4 | = 0.916 | -0.13 [-0.67, 1.22] | negligible | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.58 | 4 | = 0.916 | -0.28 [-1.50, 0.69] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.33 | 4 | = 0.916 | 0.20 [-0.43, 0.94] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | -0.11 | 4 | = 0.916 | -0.07 [-0.68, 0.86] | negligible | n.s. |
| 5 to 2 vs increasing 1 to 2 | -0.36 | 4 | = 0.916 | -0.17 [-1.48, 0.21] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 239.32, BIC = 250.80
- Condition effect: *β* = 0.74, *SE* = 0.779, *z* = 0.950, *p* = 0.342


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.98, *p* = 0.017, η²_G = 0.073
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 1.77 | 10 | = 0.215 | 0.43 [-0.31, 0.76] | small | n.s. |
| 3 to 2 vs 5 to 2 | 3.27 | 10 | = 0.025 | 0.51 [-0.20, 0.90] | medium | * |
| 3 to 2 vs increasing 1 to 2 | 4.44 | 10 | = 0.008 | 0.71 [-0.25, 1.00] | medium | ** |
| 4 to 2 vs 5 to 2 | 0.24 | 10 | = 0.817 | 0.06 [-0.36, 0.71] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.13 | 10 | = 0.341 | 0.31 [-0.37, 0.86] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 1.41 | 10 | = 0.281 | 0.26 [-0.38, 0.78] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 316.25, BIC = 329.82
- Condition effect: *β* = -0.28, *SE* = 0.513, *z* = -0.552, *p* = 0.581

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.46, *p* = 0.710, η²_G = 0.022
- Greenhouse-Geisser corrected: *p* = 0.632 (ε = 0.653)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.76 | 10 | = 0.858 | 0.21 [-0.08, 1.04] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.37 | 10 | = 0.858 | 0.46 [-0.19, 0.91] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.37 | 10 | = 0.866 | 0.16 [-0.61, 0.60] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.70 | 10 | = 0.858 | 0.25 [-0.43, 0.64] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | -0.01 | 10 | = 0.989 | -0.00 [-0.57, 0.64] | negligible | n.s. |
| 5 to 2 vs increasing 1 to 2 | -0.58 | 10 | = 0.858 | -0.21 [-0.87, 0.30] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 624.24, BIC = 637.81
- Condition effect: *β* = -7.05, *SE* = 4.652, *z* = -1.516, *p* = 0.129


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.037). Post-hoc tests revealed:
  - 5 to 2 showed smaller amplitude than increasing 1 to 2 (*d* = -0.69)
**P3b amplitude:** Significant main effect of condition (*p* = 0.017). Post-hoc tests revealed:
  - 3 to 2 showed greater amplitude than 5 to 2 (*d* = 0.51)
  - 3 to 2 showed greater amplitude than increasing 1 to 2 (*d* = 0.71)

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
