# Statistical Analysis Report: tables

**Generated:** 2025-10-16 03:46:22

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
| 2 to 5 | 24 | -3.67 µV | 2.22 | 0.45 | [-10.37, 0.03] |
| 3 to 5 | 22 | -3.34 µV | 2.35 | 0.50 | [-9.83, -0.49] |
| 4 to 5 | 23 | -3.67 µV | 2.37 | 0.49 | [-8.46, -0.52] |
| 6 to 5 | 24 | -3.64 µV | 1.83 | 0.37 | [-8.32, -0.05] |
| Cardinality5 | 23 | -3.76 µV | 2.32 | 0.48 | [-9.01, -0.42] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 171.16 ms | 13.03 | 2.66 | [153.26, 202.93] |
| 3 to 5 | 22 | 166.99 ms | 13.83 | 2.95 | [140.33, 195.88] |
| 4 to 5 | 23 | 168.71 ms | 12.60 | 2.63 | [143.65, 192.63] |
| 6 to 5 | 24 | 171.09 ms | 12.08 | 2.47 | [153.45, 201.31] |
| Cardinality5 | 23 | 170.86 ms | 12.59 | 2.63 | [141.58, 194.82] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 13 | 1.42 µV | 1.92 | 0.53 | [0.05, 7.23] |
| 3 to 5 | 15 | 1.78 µV | 1.31 | 0.34 | [0.29, 4.47] |
| 4 to 5 | 14 | 2.19 µV | 2.28 | 0.61 | [0.01, 8.63] |
| 6 to 5 | 14 | 1.92 µV | 2.24 | 0.60 | [0.06, 8.06] |
| Cardinality5 | 13 | 1.78 µV | 1.22 | 0.34 | [0.22, 3.87] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 13 | 95.50 ms | 6.51 | 1.81 | [84.09, 106.98] |
| 3 to 5 | 15 | 97.97 ms | 5.37 | 1.39 | [87.18, 105.91] |
| 4 to 5 | 14 | 98.94 ms | 4.41 | 1.18 | [92.55, 107.78] |
| 6 to 5 | 14 | 96.57 ms | 5.78 | 1.54 | [86.90, 104.60] |
| Cardinality5 | 13 | 97.54 ms | 3.40 | 0.94 | [92.16, 103.48] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 22 | 2.87 µV | 1.97 | 0.42 | [0.09, 6.73] |
| 3 to 5 | 16 | 3.60 µV | 2.26 | 0.57 | [0.84, 9.10] |
| 4 to 5 | 16 | 2.83 µV | 2.84 | 0.71 | [0.36, 11.12] |
| 6 to 5 | 12 | 2.30 µV | 2.00 | 0.58 | [0.29, 5.87] |
| Cardinality5 | 12 | 1.42 µV | 0.98 | 0.28 | [0.27, 3.44] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 22 | 444.74 ms | 39.38 | 8.40 | [365.91, 524.09] |
| 3 to 5 | 16 | 453.91 ms | 26.08 | 6.52 | [398.61, 498.83] |
| 4 to 5 | 16 | 482.77 ms | 24.77 | 6.19 | [438.04, 520.99] |
| 6 to 5 | 12 | 457.78 ms | 49.06 | 14.16 | [361.04, 526.22] |
| Cardinality5 | 12 | 441.35 ms | 54.39 | 15.70 | [361.74, 525.22] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.59, *p* = 0.673, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.64 | 21 | = 0.816 | -0.26 [-0.81, 0.11] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.29 | 21 | = 0.988 | -0.06 [-0.50, 0.37] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.28 | 21 | = 0.988 | -0.06 [-0.44, 0.40] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.02 | 21 | = 0.988 | -0.00 [-0.45, 0.42] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 1.08 | 21 | = 0.816 | 0.19 [-0.22, 0.68] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 1.00 | 21 | = 0.816 | 0.22 [-0.23, 0.66] | small | n.s. |
| 3 to 5 vs Cardinality5 | 1.23 | 21 | = 0.816 | 0.25 [-0.19, 0.71] | small | n.s. |
| 4 to 5 vs 6 to 5 | 0.02 | 21 | = 0.988 | 0.01 [-0.42, 0.44] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 0.23 | 21 | = 0.988 | 0.05 [-0.39, 0.47] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 0.25 | 21 | = 0.988 | 0.05 [-0.40, 0.47] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 471.07, BIC = 490.35
- Condition effect: *β* = 0.50, *SE* = 0.417, *z* = 1.208, *p* = 0.227

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.59, *p* = 0.673, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.32 | 21 | = 0.844 | 0.24 [-0.17, 0.73] | small | n.s. |
| 2 to 5 vs 4 to 5 | 0.55 | 21 | = 0.955 | 0.10 [-0.32, 0.55] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 0.04 | 21 | = 0.991 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | 0.06 | 21 | = 0.991 | 0.01 [-0.55, 0.32] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.60 | 21 | = 0.955 | -0.14 [-0.57, 0.32] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.18 | 21 | = 0.844 | -0.23 [-0.70, 0.20] | small | n.s. |
| 3 to 5 vs Cardinality5 | -1.31 | 21 | = 0.844 | -0.23 [-0.73, 0.17] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.43 | 21 | = 0.955 | -0.09 [-0.57, 0.30] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | -0.44 | 21 | = 0.955 | -0.09 [-0.60, 0.27] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | -0.01 | 21 | = 0.991 | -0.00 [-0.47, 0.39] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 879.73, BIC = 899.01
- Condition effect: *β* = -3.27, *SE* = 2.425, *z* = -1.347, *p* = 0.178


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.09, *p* = 0.983, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.12 | 4 | = 0.983 | 0.05 [-0.98, 0.47] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -0.02 | 4 | = 0.983 | -0.01 [-1.25, 0.36] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.17 | 4 | = 0.983 | -0.02 [-1.14, 0.44] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.32 | 4 | = 0.983 | -0.17 [-0.90, 0.65] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.21 | 4 | = 0.983 | -0.08 [-1.18, 0.42] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -0.18 | 4 | = 0.983 | -0.07 [-0.95, 0.50] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | -1.04 | 4 | = 0.983 | -0.37 [-0.52, 0.83] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.07 | 4 | = 0.983 | -0.02 [-0.83, 0.70] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | -0.41 | 4 | = 0.983 | -0.24 [-1.01, 0.67] | small | n.s. |
| 6 to 5 vs Cardinality5 | -0.25 | 4 | = 0.983 | -0.13 [-0.58, 0.85] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 274.31, BIC = 289.95
- Condition effect: *β* = 0.50, *SE* = 0.530, *z* = 0.948, *p* = 0.343

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.38, *p* = 0.817, η²_G = 0.063
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.34 | 4 | = 0.941 | 0.17 [-1.00, 0.45] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 1.22 | 4 | = 0.941 | 0.39 [-0.98, 0.57] | small | n.s. |
| 2 to 5 vs 6 to 5 | -0.12 | 4 | = 0.987 | -0.07 [-1.32, 0.31] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | 0.83 | 4 | = 0.941 | 0.51 [-0.97, 0.59] | medium | n.s. |
| 3 to 5 vs 4 to 5 | 0.35 | 4 | = 0.941 | 0.25 [-0.66, 0.88] | small | n.s. |
| 3 to 5 vs 6 to 5 | -0.46 | 4 | = 0.941 | -0.29 [-0.59, 0.84] | small | n.s. |
| 3 to 5 vs Cardinality5 | 0.40 | 4 | = 0.941 | 0.34 [-0.62, 0.72] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.80 | 4 | = 0.941 | -0.53 [-0.59, 0.96] | medium | n.s. |
| 4 to 5 vs Cardinality5 | 0.02 | 4 | = 0.987 | 0.01 [-0.50, 1.23] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 1.40 | 4 | = 0.941 | 0.81 [-0.31, 1.19] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 421.96, BIC = 437.60
- Condition effect: *β* = 2.37, *SE* = 1.514, *z* = 1.568, *p* = 0.117


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.46, *p* = 0.078, η²_G = 0.319
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.73 | 5 | = 0.552 | 0.53 [-0.60, 0.47] | medium | n.s. |
| 2 to 5 vs 4 to 5 | 1.52 | 5 | = 0.400 | 0.89 [-0.44, 0.67] | large | n.s. |
| 2 to 5 vs 6 to 5 | 1.37 | 5 | = 0.400 | 0.86 [-0.28, 1.12] | large | n.s. |
| 2 to 5 vs Cardinality5 | 4.16 | 5 | = 0.044 | 2.74 [0.12, 1.61] | large | * |
| 3 to 5 vs 4 to 5 | 0.73 | 5 | = 0.552 | 0.51 [-0.27, 1.05] | medium | n.s. |
| 3 to 5 vs 6 to 5 | 0.79 | 5 | = 0.552 | 0.47 [-0.30, 1.20] | small | n.s. |
| 3 to 5 vs Cardinality5 | 6.36 | 5 | = 0.014 | 2.16 [0.20, 2.03] | large | * |
| 4 to 5 vs 6 to 5 | -0.07 | 5 | = 0.948 | -0.04 [-0.52, 1.05] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 1.33 | 5 | = 0.400 | 0.87 [-0.56, 0.99] | large | n.s. |
| 6 to 5 vs Cardinality5 | 1.35 | 5 | = 0.400 | 0.94 [-0.46, 1.51] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 337.37, BIC = 353.87
- Condition effect: *β* = 0.43, *SE* = 0.550, *z* = 0.780, *p* = 0.436

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.05, *p* = 0.126, η²_G = 0.254
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -2.45 | 5 | = 0.281 | -0.51 [-1.20, -0.04] | medium | n.s. |
| 2 to 5 vs 4 to 5 | -1.75 | 5 | = 0.281 | -1.09 [-1.49, -0.20] | large | n.s. |
| 2 to 5 vs 6 to 5 | -1.78 | 5 | = 0.281 | -1.02 [-1.11, 0.29] | large | n.s. |
| 2 to 5 vs Cardinality5 | 0.54 | 5 | = 0.682 | 0.38 [-0.67, 0.60] | small | n.s. |
| 3 to 5 vs 4 to 5 | -0.83 | 5 | = 0.560 | -0.60 [-1.14, 0.20] | medium | n.s. |
| 3 to 5 vs 6 to 5 | -0.82 | 5 | = 0.560 | -0.53 [-1.07, 0.40] | medium | n.s. |
| 3 to 5 vs Cardinality5 | 1.07 | 5 | = 0.553 | 0.76 [-0.65, 0.78] | medium | n.s. |
| 4 to 5 vs 6 to 5 | 0.30 | 5 | = 0.778 | 0.07 [-0.30, 1.33] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 2.30 | 5 | = 0.281 | 1.18 [0.06, 1.95] | large | n.s. |
| 6 to 5 vs Cardinality5 | 2.13 | 5 | = 0.281 | 1.13 [-0.33, 1.73] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 801.68, BIC = 818.17
- Condition effect: *β* = 9.17, *SE* = 12.403, *z* = 0.740, *p* = 0.459


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.078)

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
