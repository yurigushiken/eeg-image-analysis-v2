# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:51:10

---

## 1. Analysis Overview

**Total Measurements:** 360
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
| 4 to 1 | 20 | -1.74 µV | 1.47 | 0.33 | [-4.84, 0.01] |
| 4 to 2 | 24 | -4.06 µV | 2.52 | 0.52 | [-9.35, -0.51] |
| 4 to 3 | 23 | -4.04 µV | 1.96 | 0.41 | [-8.55, -0.80] |
| 4 to 5 | 22 | -4.70 µV | 3.12 | 0.66 | [-13.05, -1.07] |
| 4 to 6 | 22 | -4.49 µV | 2.81 | 0.60 | [-12.83, -0.72] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 182.56 ms | 12.72 | 2.84 | [148.70, 201.04] |
| 4 to 2 | 24 | 178.11 ms | 9.29 | 1.90 | [161.53, 202.22] |
| 4 to 3 | 23 | 174.46 ms | 10.11 | 2.11 | [157.54, 203.60] |
| 4 to 5 | 22 | 172.76 ms | 9.86 | 2.10 | [152.07, 193.23] |
| 4 to 6 | 22 | 174.73 ms | 10.01 | 2.13 | [154.94, 199.42] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 3.41 µV | 2.73 | 0.66 | [0.47, 10.41] |
| 4 to 2 | 14 | 1.70 µV | 1.26 | 0.34 | [0.16, 4.01] |
| 4 to 3 | 12 | 1.70 µV | 1.30 | 0.38 | [0.29, 4.76] |
| 4 to 5 | 13 | 4.57 µV | 4.90 | 1.36 | [0.17, 15.16] |
| 4 to 6 | 13 | 2.39 µV | 1.76 | 0.49 | [0.19, 5.91] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 107.80 ms | 2.77 | 0.67 | [99.58, 112.61] |
| 4 to 2 | 14 | 109.01 ms | 3.04 | 0.81 | [103.66, 114.77] |
| 4 to 3 | 12 | 105.54 ms | 3.65 | 1.05 | [99.06, 113.00] |
| 4 to 5 | 13 | 106.05 ms | 3.72 | 1.03 | [98.21, 112.31] |
| 4 to 6 | 13 | 105.63 ms | 4.80 | 1.33 | [97.31, 113.59] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 4.54 µV | 2.89 | 0.65 | [0.10, 8.59] |
| 4 to 2 | 18 | 3.79 µV | 2.72 | 0.64 | [0.30, 8.72] |
| 4 to 3 | 20 | 3.95 µV | 2.82 | 0.63 | [0.14, 9.37] |
| 4 to 5 | 15 | 4.72 µV | 2.69 | 0.70 | [0.36, 10.21] |
| 4 to 6 | 20 | 3.69 µV | 2.71 | 0.61 | [0.09, 7.97] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 485.55 ms | 15.66 | 3.50 | [449.31, 511.89] |
| 4 to 2 | 18 | 482.67 ms | 18.69 | 4.40 | [437.65, 506.08] |
| 4 to 3 | 20 | 483.91 ms | 18.54 | 4.15 | [433.89, 525.01] |
| 4 to 5 | 15 | 500.10 ms | 15.74 | 4.06 | [474.03, 531.48] |
| 4 to 6 | 20 | 491.23 ms | 23.53 | 5.26 | [437.45, 539.01] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 6.04, *p* < .001, η²_G = 0.199
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 4.37 | 14 | = 0.005 | 1.40 [0.37, 1.49] | large | ** |
| 4 to 1 vs 4 to 3 | 4.12 | 14 | = 0.005 | 1.51 [0.38, 1.54] | large | ** |
| 4 to 1 vs 4 to 5 | 3.64 | 14 | = 0.007 | 1.26 [0.43, 1.66] | large | ** |
| 4 to 1 vs 4 to 6 | 3.82 | 14 | = 0.006 | 1.21 [0.33, 1.52] | large | ** |
| 4 to 2 vs 4 to 3 | -0.58 | 14 | = 0.887 | -0.16 [-0.41, 0.45] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 0.01 | 14 | = 0.989 | 0.00 [-0.33, 0.55] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | -0.08 | 14 | = 0.989 | -0.02 [-0.31, 0.59] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 0.51 | 14 | = 0.887 | 0.15 [-0.26, 0.66] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | 0.57 | 14 | = 0.887 | 0.12 [-0.26, 0.66] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -0.06 | 14 | = 0.989 | -0.02 [-0.49, 0.45] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 493.68, BIC = 512.64
- Condition effect: *β* = -2.28, *SE* = 0.537, *z* = -4.253, *p* < .001

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 4.41, *p* = 0.004, η²_G = 0.134
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.22 | 14 | = 0.304 | 0.42 [-0.11, 0.86] | small | n.s. |
| 4 to 1 vs 4 to 3 | 2.18 | 14 | = 0.117 | 0.68 [0.10, 1.15] | medium | n.s. |
| 4 to 1 vs 4 to 5 | 2.74 | 14 | = 0.053 | 0.88 [0.17, 1.28] | large | n.s. |
| 4 to 1 vs 4 to 6 | 2.79 | 14 | = 0.053 | 0.79 [0.10, 1.20] | medium | n.s. |
| 4 to 2 vs 4 to 3 | 1.52 | 14 | = 0.253 | 0.40 [0.11, 1.04] | small | n.s. |
| 4 to 2 vs 4 to 5 | 3.02 | 14 | = 0.053 | 0.69 [-0.06, 0.86] | medium | n.s. |
| 4 to 2 vs 4 to 6 | 2.03 | 14 | = 0.124 | 0.55 [0.11, 1.07] | medium | n.s. |
| 4 to 3 vs 4 to 5 | 1.23 | 14 | = 0.304 | 0.32 [-0.47, 0.44] | small | n.s. |
| 4 to 3 vs 4 to 6 | 0.81 | 14 | = 0.481 | 0.17 [-0.36, 0.55] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -0.61 | 14 | = 0.551 | -0.16 [-0.65, 0.30] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 814.04, BIC = 833.01
- Condition effect: *β* = -5.03, *SE* = 2.281, *z* = -2.204, *p* = 0.028


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.56, *p* = 0.232, η²_G = 0.215
- Greenhouse-Geisser corrected: *p* = 0.267 (ε = 0.496)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 2.05 | 4 | = 0.524 | 1.12 [-0.14, 1.22] | large | n.s. |
| 4 to 1 vs 4 to 3 | 2.21 | 4 | = 0.524 | 0.88 [-0.03, 1.61] | large | n.s. |
| 4 to 1 vs 4 to 5 | 0.50 | 4 | = 0.712 | 0.28 [-0.45, 1.13] | small | n.s. |
| 4 to 1 vs 4 to 6 | 1.07 | 4 | = 0.524 | 0.78 [-0.51, 0.94] | medium | n.s. |
| 4 to 2 vs 4 to 3 | -1.01 | 4 | = 0.524 | -0.42 [-0.70, 0.64] | small | n.s. |
| 4 to 2 vs 4 to 5 | -1.60 | 4 | = 0.524 | -0.95 [-1.45, 0.13] | large | n.s. |
| 4 to 2 vs 4 to 6 | -1.08 | 4 | = 0.524 | -0.73 [-1.34, 0.30] | medium | n.s. |
| 4 to 3 vs 4 to 5 | -0.99 | 4 | = 0.524 | -0.67 [-1.71, 0.19] | medium | n.s. |
| 4 to 3 vs 4 to 6 | -0.27 | 4 | = 0.798 | -0.22 [-0.91, 0.76] | small | n.s. |
| 4 to 5 vs 4 to 6 | 0.90 | 4 | = 0.524 | 0.54 [-0.56, 1.00] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 344.11, BIC = 359.75
- Condition effect: *β* = -1.76, *SE* = 0.953, *z* = -1.850, *p* = 0.064

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.64, *p* = 0.642, η²_G = 0.113
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.70 | 4 | = 0.746 | 0.21 [-0.98, 0.32] | small | n.s. |
| 4 to 1 vs 4 to 3 | 0.97 | 4 | = 0.746 | 0.79 [-0.05, 1.57] | medium | n.s. |
| 4 to 1 vs 4 to 5 | 1.61 | 4 | = 0.746 | 0.60 [-0.43, 1.16] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 0.96 | 4 | = 0.746 | 0.74 [-0.25, 1.27] | medium | n.s. |
| 4 to 2 vs 4 to 3 | 0.89 | 4 | = 0.746 | 0.63 [-0.24, 1.18] | medium | n.s. |
| 4 to 2 vs 4 to 5 | 2.53 | 4 | = 0.645 | 0.40 [-0.15, 1.42] | small | n.s. |
| 4 to 2 vs 4 to 6 | 0.83 | 4 | = 0.746 | 0.58 [-0.23, 1.44] | medium | n.s. |
| 4 to 3 vs 4 to 5 | -0.39 | 4 | = 0.807 | -0.29 [-0.80, 0.87] | small | n.s. |
| 4 to 3 vs 4 to 6 | -0.06 | 4 | = 0.954 | -0.03 [-0.90, 0.77] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 0.38 | 4 | = 0.807 | 0.25 [-0.50, 1.07] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 381.36, BIC = 397.00
- Condition effect: *β* = 1.08, *SE* = 1.249, *z* = 0.867, *p* = 0.386


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.37, *p* = 0.831, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.32 | 9 | = 0.993 | 0.07 [-0.38, 0.69] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | -0.01 | 9 | = 0.993 | -0.00 [-0.49, 0.54] | negligible | n.s. |
| 4 to 1 vs 4 to 5 | 0.70 | 9 | = 0.993 | 0.27 [-0.41, 0.75] | small | n.s. |
| 4 to 1 vs 4 to 6 | 0.03 | 9 | = 0.993 | 0.01 [-0.23, 0.82] | negligible | n.s. |
| 4 to 2 vs 4 to 3 | -0.35 | 9 | = 0.993 | -0.07 [-0.64, 0.43] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 0.65 | 9 | = 0.993 | 0.19 [-0.75, 0.47] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | -0.33 | 9 | = 0.993 | -0.07 [-0.41, 0.66] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 0.71 | 9 | = 0.993 | 0.27 [-0.45, 0.71] | small | n.s. |
| 4 to 3 vs 4 to 6 | 0.03 | 9 | = 0.993 | 0.01 [-0.30, 0.67] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -1.30 | 9 | = 0.993 | -0.30 [-0.70, 0.46] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 422.26, BIC = 439.99
- Condition effect: *β* = -0.61, *SE* = 0.573, *z* = -1.068, *p* = 0.286

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 5.62, *p* = 0.001, η²_G = 0.258
- Greenhouse-Geisser corrected: *p* = 0.011 (ε = 0.524)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.44 | 9 | = 0.744 | 0.16 [-0.47, 0.60] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | -0.06 | 9 | = 0.953 | -0.02 [-0.47, 0.55] | negligible | n.s. |
| 4 to 1 vs 4 to 5 | -2.84 | 9 | = 0.054 | -1.44 [-1.47, -0.14] | large | n.s. |
| 4 to 1 vs 4 to 6 | -2.07 | 9 | = 0.098 | -0.93 [-0.73, 0.31] | large | n.s. |
| 4 to 2 vs 4 to 3 | -1.00 | 9 | = 0.429 | -0.16 [-0.83, 0.26] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | -2.93 | 9 | = 0.054 | -1.32 [-1.61, -0.18] | large | n.s. |
| 4 to 2 vs 4 to 6 | -2.64 | 9 | = 0.054 | -0.87 [-0.96, 0.15] | large | n.s. |
| 4 to 3 vs 4 to 5 | -2.74 | 9 | = 0.054 | -1.16 [-1.41, -0.10] | large | n.s. |
| 4 to 3 vs 4 to 6 | -2.09 | 9 | = 0.098 | -0.69 [-0.87, 0.13] | medium | n.s. |
| 4 to 5 vs 4 to 6 | 2.82 | 9 | = 0.054 | 0.65 [-0.06, 1.18] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 816.53, BIC = 834.26
- Condition effect: *β* = -2.90, *SE* = 5.599, *z* = -0.518, *p* = 0.605


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 2 (*d* = 1.40)
  - 4 to 1 showed greater amplitude than 4 to 3 (*d* = 1.51)
  - 4 to 1 showed greater amplitude than 4 to 5 (*d* = 1.26)
  - 4 to 1 showed greater amplitude than 4 to 6 (*d* = 1.21)
**N1 latency:** Significant main effect of condition (*p* = 0.004) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.001) (no significant pairwise comparisons)

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
