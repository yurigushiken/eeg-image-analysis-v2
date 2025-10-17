# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:49:30

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
| 3 to 1 | 19 | -2.83 µV | 2.30 | 0.53 | [-7.70, 0.04] |
| 4 to 2 | 24 | -4.16 µV | 2.50 | 0.51 | [-9.30, -0.77] |
| 5 to 3 | 24 | -3.79 µV | 2.43 | 0.50 | [-8.62, -0.11] |
| 6 to 4 | 23 | -3.74 µV | 2.24 | 0.47 | [-9.81, -0.79] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 19 | 182.30 ms | 11.43 | 2.62 | [162.94, 203.39] |
| 4 to 2 | 24 | 178.90 ms | 8.32 | 1.70 | [163.75, 199.96] |
| 5 to 3 | 24 | 176.65 ms | 10.82 | 2.21 | [157.35, 207.52] |
| 6 to 4 | 23 | 176.87 ms | 10.45 | 2.18 | [161.10, 201.71] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 21 | 2.23 µV | 1.76 | 0.39 | [0.18, 7.32] |
| 4 to 2 | 14 | 2.13 µV | 1.11 | 0.30 | [0.51, 4.30] |
| 5 to 3 | 17 | 1.94 µV | 1.25 | 0.30 | [-0.13, 3.48] |
| 6 to 4 | 15 | 2.89 µV | 1.30 | 0.34 | [1.24, 5.12] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 21 | 115.26 ms | 6.79 | 1.48 | [100.88, 125.41] |
| 4 to 2 | 14 | 116.43 ms | 2.90 | 0.77 | [110.37, 120.87] |
| 5 to 3 | 17 | 113.01 ms | 5.61 | 1.36 | [102.40, 123.96] |
| 6 to 4 | 15 | 115.16 ms | 3.59 | 0.93 | [109.17, 123.37] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 4.19 µV | 2.52 | 0.56 | [0.72, 10.89] |
| 4 to 2 | 18 | 3.81 µV | 2.66 | 0.63 | [0.22, 8.65] |
| 5 to 3 | 17 | 4.14 µV | 1.75 | 0.42 | [1.03, 8.32] |
| 6 to 4 | 19 | 3.55 µV | 2.34 | 0.54 | [0.05, 8.53] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 479.78 ms | 11.22 | 2.51 | [462.26, 503.57] |
| 4 to 2 | 18 | 478.99 ms | 17.41 | 4.10 | [436.38, 501.95] |
| 5 to 3 | 17 | 476.88 ms | 12.41 | 3.01 | [449.55, 496.77] |
| 6 to 4 | 19 | 485.84 ms | 22.81 | 5.23 | [431.12, 531.78] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.45, *p* = 0.023, η²_G = 0.091
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 3.37 | 17 | = 0.022 | 0.86 [0.20, 1.29] | large | * |
| 3 to 1 vs 5 to 3 | 1.85 | 17 | = 0.169 | 0.64 [-0.16, 0.84] | medium | n.s. |
| 3 to 1 vs 6 to 4 | 1.83 | 17 | = 0.169 | 0.59 [-0.09, 0.95] | medium | n.s. |
| 4 to 2 vs 5 to 3 | -0.82 | 17 | = 0.511 | -0.20 [-0.57, 0.28] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.11 | 17 | = 0.421 | -0.26 [-0.58, 0.29] | small | n.s. |
| 5 to 3 vs 6 to 4 | -0.27 | 17 | = 0.787 | -0.06 [-0.48, 0.38] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 406.28, BIC = 421.28
- Condition effect: *β* = -1.55, *SE* = 0.581, *z* = -2.678, *p* = 0.007

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.83, *p* = 0.153, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.32 | 17 | = 0.409 | 0.35 [-0.17, 0.82] | small | n.s. |
| 3 to 1 vs 5 to 3 | 1.58 | 17 | = 0.396 | 0.38 [-0.13, 0.87] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.76 | 17 | = 0.396 | 0.42 [-0.10, 0.93] | small | n.s. |
| 4 to 2 vs 5 to 3 | 0.59 | 17 | = 0.672 | 0.10 [-0.15, 0.71] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.61 | 17 | = 0.672 | 0.13 [-0.18, 0.69] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.13 | 17 | = 0.901 | 0.02 [-0.47, 0.40] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 649.28, BIC = 664.28
- Condition effect: *β* = -2.90, *SE* = 2.063, *z* = -1.405, *p* = 0.160


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.83, *p* = 0.173, η²_G = 0.136
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.96 | 7 | = 0.550 | 0.50 [-0.55, 0.60] | medium | n.s. |
| 3 to 1 vs 5 to 3 | 1.12 | 7 | = 0.550 | 0.46 [-0.35, 0.73] | small | n.s. |
| 3 to 1 vs 6 to 4 | -0.57 | 7 | = 0.707 | -0.24 [-0.97, 0.23] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.02 | 7 | = 0.983 | -0.01 [-0.71, 0.63] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -3.00 | 7 | = 0.119 | -1.22 [-1.44, 0.14] | large | n.s. |
| 5 to 3 vs 6 to 4 | -2.01 | 7 | = 0.253 | -1.02 [-1.17, 0.18] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 243.70, BIC = 256.93
- Condition effect: *β* = -0.12, *SE* = 0.447, *z* = -0.257, *p* = 0.797

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.83, *p* = 0.493, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -0.26 | 7 | = 0.800 | -0.12 [-0.73, 0.44] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.93 | 7 | = 0.576 | 0.33 [-0.14, 0.97] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.95 | 7 | = 0.576 | 0.30 [-0.17, 1.04] | small | n.s. |
| 4 to 2 vs 5 to 3 | 1.14 | 7 | = 0.576 | 0.50 [-0.09, 1.39] | medium | n.s. |
| 4 to 2 vs 6 to 4 | 1.64 | 7 | = 0.576 | 0.76 [-0.11, 1.49] | medium | n.s. |
| 5 to 3 vs 6 to 4 | -0.38 | 7 | = 0.800 | -0.14 [-0.87, 0.41] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 416.26, BIC = 429.49
- Condition effect: *β* = 1.09, *SE* = 1.560, *z* = 0.702, *p* = 0.483


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.96, *p* = 0.421, η²_G = 0.043
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.30 | 13 | = 0.628 | 0.30 [-0.22, 0.83] | small | n.s. |
| 3 to 1 vs 5 to 3 | 0.76 | 13 | = 0.650 | 0.31 [-0.42, 0.65] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.33 | 13 | = 0.628 | 0.58 [-0.34, 0.66] | medium | n.s. |
| 4 to 2 vs 5 to 3 | -0.21 | 13 | = 0.839 | -0.06 [-0.67, 0.44] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.63 | 13 | = 0.650 | 0.20 [-0.36, 0.71] | small | n.s. |
| 5 to 3 vs 6 to 4 | 1.05 | 13 | = 0.628 | 0.35 [-0.21, 0.93] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 341.37, BIC = 355.19
- Condition effect: *β* = -0.40, *SE* = 0.672, *z* = -0.591, *p* = 0.555

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.48, *p* = 0.236, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -0.41 | 13 | = 0.857 | -0.11 [-0.38, 0.65] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | -0.02 | 13 | = 0.986 | -0.01 [-0.41, 0.66] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | -1.40 | 13 | = 0.368 | -0.51 [-0.73, 0.28] | medium | n.s. |
| 4 to 2 vs 5 to 3 | 0.37 | 13 | = 0.857 | 0.10 [-0.49, 0.62] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.56 | 13 | = 0.368 | -0.35 [-0.79, 0.29] | small | n.s. |
| 5 to 3 vs 6 to 4 | -1.43 | 13 | = 0.368 | -0.50 [-1.02, 0.14] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 624.59, BIC = 638.41
- Condition effect: *β* = -1.02, *SE* = 4.282, *z* = -0.239, *p* = 0.811


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.023). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 0.86)

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
