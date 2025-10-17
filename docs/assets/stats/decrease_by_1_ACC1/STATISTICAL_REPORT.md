# Statistical Analysis Report: tables

**Generated:** 2025-10-16 21:43:25

---

## 1. Analysis Overview

**Total Measurements:** 336
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 2 to 1 | 16 | -2.80 µV | 2.07 | 0.52 | [-8.56, -0.10] |
| 3 to 2 | 22 | -4.04 µV | 2.08 | 0.44 | [-8.11, -0.72] |
| 4 to 3 | 23 | -3.53 µV | 1.79 | 0.37 | [-7.41, -0.90] |
| 5 to 4 | 22 | -4.08 µV | 2.30 | 0.49 | [-8.57, -0.83] |
| 6 to 5 | 15 | -4.59 µV | 1.71 | 0.44 | [-7.11, -1.79] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 178.08 ms | 7.12 | 1.78 | [161.55, 186.09] |
| 3 to 2 | 22 | 171.34 ms | 8.07 | 1.72 | [158.57, 193.74] |
| 4 to 3 | 23 | 170.44 ms | 10.06 | 2.10 | [146.84, 197.14] |
| 5 to 4 | 22 | 176.45 ms | 8.67 | 1.85 | [163.05, 196.79] |
| 6 to 5 | 15 | 172.62 ms | 10.64 | 2.75 | [155.99, 190.83] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 3.57 µV | 2.54 | 0.62 | [1.07, 8.49] |
| 3 to 2 | 9 | 2.06 µV | 1.50 | 0.50 | [0.01, 4.07] |
| 4 to 3 | 13 | 2.37 µV | 2.06 | 0.57 | [0.05, 6.33] |
| 5 to 4 | 16 | 2.06 µV | 1.81 | 0.45 | [0.02, 5.16] |
| 6 to 5 | 4 | 1.92 µV | 1.07 | 0.53 | [0.91, 2.93] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 111.04 ms | 2.05 | 0.50 | [106.76, 114.36] |
| 3 to 2 | 9 | 109.04 ms | 3.00 | 1.00 | [102.34, 113.00] |
| 4 to 3 | 13 | 110.00 ms | 4.62 | 1.28 | [101.50, 119.68] |
| 5 to 4 | 16 | 110.07 ms | 4.57 | 1.14 | [100.12, 118.16] |
| 6 to 5 | 4 | 112.99 ms | 3.67 | 1.84 | [110.29, 118.33] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 4.08 µV | 3.02 | 0.66 | [0.38, 9.98] |
| 3 to 2 | 17 | 4.67 µV | 3.10 | 0.75 | [0.98, 12.94] |
| 4 to 3 | 17 | 4.21 µV | 2.45 | 0.59 | [0.17, 8.40] |
| 5 to 4 | 21 | 3.75 µV | 2.79 | 0.61 | [0.76, 9.16] |
| 6 to 5 | 11 | 3.10 µV | 1.69 | 0.51 | [0.18, 5.69] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 503.80 ms | 17.46 | 3.81 | [463.71, 541.51] |
| 3 to 2 | 17 | 499.69 ms | 13.04 | 3.16 | [474.50, 532.81] |
| 4 to 3 | 17 | 503.16 ms | 19.39 | 4.70 | [462.60, 546.64] |
| 5 to 4 | 21 | 498.13 ms | 16.93 | 3.69 | [462.25, 530.48] |
| 6 to 5 | 11 | 510.36 ms | 26.70 | 8.05 | [469.21, 550.35] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.91, *p* = 0.035, η²_G = 0.160
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 5.19 | 9 | = 0.006 | 1.05 [0.37, 1.76] | large | ** |
| 2 to 1 vs 4 to 3 | 3.50 | 9 | = 0.022 | 1.05 [-0.11, 1.00] | large | * |
| 2 to 1 vs 5 to 4 | 2.11 | 9 | = 0.159 | 1.03 [0.03, 1.24] | large | n.s. |
| 2 to 1 vs 6 to 5 | 3.86 | 9 | = 0.019 | 1.45 [0.34, 2.13] | large | * |
| 3 to 2 vs 4 to 3 | -0.17 | 9 | = 0.872 | -0.05 [-0.68, 0.22] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.19 | 9 | = 0.872 | 0.08 [-0.41, 0.50] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.59 | 9 | = 0.872 | 0.20 [-0.23, 0.96] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 0.28 | 9 | = 0.872 | 0.13 [-0.25, 0.67] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.10 | 9 | = 0.596 | 0.27 [0.08, 1.31] | small | n.s. |
| 5 to 4 vs 6 to 5 | 0.21 | 9 | = 0.872 | 0.09 [-0.38, 0.78] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 411.18, BIC = 429.27
- Condition effect: *β* = -1.44, *SE* = 0.539, *z* = -2.665, *p* = 0.008

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.42, *p* = 0.066, η²_G = 0.101
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.82 | 9 | = 0.329 | 0.66 [-0.01, 1.20] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 5.00 | 9 | = 0.007 | 0.98 [0.23, 1.47] | large | ** |
| 2 to 1 vs 5 to 4 | 0.49 | 9 | = 0.709 | 0.13 [-0.41, 0.70] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 1.51 | 9 | = 0.329 | 0.45 [-0.21, 1.22] | small | n.s. |
| 3 to 2 vs 4 to 3 | 0.69 | 9 | = 0.634 | 0.29 [-0.25, 0.64] | small | n.s. |
| 3 to 2 vs 5 to 4 | -1.14 | 9 | = 0.454 | -0.45 [-0.85, 0.09] | small | n.s. |
| 3 to 2 vs 6 to 5 | -0.33 | 9 | = 0.747 | -0.14 [-0.49, 0.67] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -3.44 | 9 | = 0.037 | -0.73 [-1.45, -0.37] | medium | * |
| 4 to 3 vs 6 to 5 | -1.58 | 9 | = 0.329 | -0.41 [-0.64, 0.47] | small | n.s. |
| 5 to 4 vs 6 to 5 | 1.06 | 9 | = 0.454 | 0.29 [-0.05, 1.20] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 692.68, BIC = 710.78
- Condition effect: *β* = -5.01, *SE* = 2.163, *z* = -2.318, *p* = 0.020


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.59, *p* = 0.122, η²_G = 0.701
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.11 | 1 | = 0.704 | 2.97 [0.01, 2.48] | large | n.s. |
| 2 to 1 vs 4 to 3 | 14.24 | 1 | = 0.446 | 2.64 [-0.28, 1.37] | large | n.s. |
| 2 to 1 vs 5 to 4 | 5.90 | 1 | = 0.454 | 2.40 [0.01, 1.44] | large | n.s. |
| 2 to 1 vs 6 to 5 | 4.60 | 1 | = 0.454 | 4.19 [-3.37, 11.14] | large | n.s. |
| 3 to 2 vs 4 to 3 | 0.24 | 1 | = 0.933 | 0.33 [-0.94, 0.91] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.47 | 1 | = 0.932 | 0.62 [-0.97, 0.88] | medium | n.s. |
| 3 to 2 vs 6 to 5 | 0.42 | 1 | = 0.932 | 0.46 [-2.07, 3.50] | small | n.s. |
| 4 to 3 vs 5 to 4 | 1.34 | 1 | = 0.819 | 0.33 [-0.45, 1.01] | small | n.s. |
| 4 to 3 vs 6 to 5 | -0.11 | 1 | = 0.933 | -0.10 [-2.32, 2.70] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.49 | 1 | = 0.932 | -0.47 [-1.30, 1.97] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 251.86, BIC = 266.40
- Condition effect: *β* = -1.75, *SE* = 0.670, *z* = -2.620, *p* = 0.009

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.63, *p* = 0.665, η²_G = 0.278
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.49 | 1 | = 0.941 | 2.03 [-0.17, 2.06] | large | n.s. |
| 2 to 1 vs 4 to 3 | 0.20 | 1 | = 0.941 | 0.22 [-0.50, 1.07] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.80 | 1 | = 0.941 | 0.83 [-0.39, 0.90] | large | n.s. |
| 2 to 1 vs 6 to 5 | 0.57 | 1 | = 0.941 | 0.78 [-2.92, 2.20] | medium | n.s. |
| 3 to 2 vs 4 to 3 | -0.21 | 1 | = 0.941 | -0.17 [-1.51, 0.47] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.71 | 1 | = 0.941 | 0.66 [-0.83, 1.02] | medium | n.s. |
| 3 to 2 vs 6 to 5 | -18.79 | 1 | = 0.338 | -1.09 [-3.57, 2.06] | large | n.s. |
| 4 to 3 vs 5 to 4 | 1.29 | 1 | = 0.941 | 0.67 [-0.62, 0.81] | medium | n.s. |
| 4 to 3 vs 6 to 5 | -0.09 | 1 | = 0.941 | -0.08 [-3.23, 2.11] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.82 | 1 | = 0.941 | -0.77 [-2.95, 0.95] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 322.48, BIC = 337.02
- Condition effect: *β* = -2.31, *SE* = 1.187, *z* = -1.943, *p* = 0.052


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.31, *p* = 0.024, η²_G = 0.224
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.17 | 7 | = 0.870 | 0.09 [-0.55, 0.48] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 1.29 | 7 | = 0.395 | 0.45 [-0.36, 0.72] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.98 | 7 | = 0.515 | 0.51 [-0.44, 0.53] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 3.28 | 7 | = 0.046 | 1.74 [-0.03, 1.47] | large | * |
| 3 to 2 vs 4 to 3 | 0.81 | 7 | = 0.552 | 0.32 [-0.25, 1.00] | small | n.s. |
| 3 to 2 vs 5 to 4 | 1.30 | 7 | = 0.395 | 0.40 [-0.21, 0.88] | small | n.s. |
| 3 to 2 vs 6 to 5 | 3.26 | 7 | = 0.046 | 1.48 [0.11, 2.04] | large | * |
| 4 to 3 vs 5 to 4 | 0.48 | 7 | = 0.716 | 0.15 [-0.41, 0.66] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 3.38 | 7 | = 0.046 | 1.39 [0.06, 1.76] | large | * |
| 5 to 4 vs 6 to 5 | 1.74 | 7 | = 0.313 | 0.84 [-0.14, 1.32] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 404.29, BIC = 421.55
- Condition effect: *β* = 0.42, *SE* = 0.611, *z* = 0.685, *p* = 0.493

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 3.73, *p* = 0.015, η²_G = 0.312
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.22 | 7 | = 0.832 | -0.11 [-0.26, 0.79] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | -0.40 | 7 | = 0.832 | -0.19 [-0.80, 0.28] | negligible | n.s. |
| 2 to 1 vs 5 to 4 | -0.84 | 7 | = 0.791 | -0.40 [-0.22, 0.76] | small | n.s. |
| 2 to 1 vs 6 to 5 | -2.90 | 7 | = 0.196 | -1.52 [-1.35, 0.12] | large | n.s. |
| 3 to 2 vs 4 to 3 | -0.25 | 7 | = 0.832 | -0.11 [-0.73, 0.48] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.76 | 7 | = 0.791 | -0.27 [-0.53, 0.53] | small | n.s. |
| 3 to 2 vs 6 to 5 | -2.53 | 7 | = 0.196 | -1.40 [-1.47, 0.21] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.22 | 7 | = 0.832 | -0.08 [-0.45, 0.62] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | -1.96 | 7 | = 0.248 | -1.09 [-1.27, 0.25] | large | n.s. |
| 5 to 4 vs 6 to 5 | -1.90 | 7 | = 0.248 | -1.20 [-1.19, 0.23] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 755.90, BIC = 773.17
- Condition effect: *β* = -4.90, *SE* = 5.038, *z* = -0.973, *p* = 0.331


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.035). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 1.05)
  - 2 to 1 showed greater amplitude than 4 to 3 (*d* = 1.05)
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 1.45)
**N1 latency:** Marginal trend toward condition differences (*p* = 0.066)
**P3b amplitude:** Significant main effect of condition (*p* = 0.024). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 1.74)
  - 3 to 2 showed greater amplitude than 6 to 5 (*d* = 1.48)
  - 4 to 3 showed greater amplitude than 6 to 5 (*d* = 1.39)
**P3b latency:** Significant main effect of condition (*p* = 0.015) (no significant pairwise comparisons)

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
