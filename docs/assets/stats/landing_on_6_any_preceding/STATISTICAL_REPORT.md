# Statistical Analysis Report: tables

**Generated:** 2025-10-16 03:47:07

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
| 3 to 6 | 23 | -4.63 µV | 2.41 | 0.50 | [-10.45, -1.42] |
| 4 to 6 | 22 | -4.02 µV | 2.10 | 0.45 | [-8.66, -1.11] |
| 5 to 6 | 22 | -4.03 µV | 2.07 | 0.44 | [-8.42, -0.99] |
| Cardinality6 | 22 | -3.48 µV | 2.13 | 0.45 | [-7.46, -0.37] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | 171.88 ms | 11.11 | 2.32 | [153.66, 196.77] |
| 4 to 6 | 22 | 169.93 ms | 10.22 | 2.18 | [146.28, 188.99] |
| 5 to 6 | 22 | 173.46 ms | 10.77 | 2.30 | [142.43, 194.03] |
| Cardinality6 | 22 | 173.41 ms | 12.91 | 2.75 | [154.01, 204.78] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 11 | 2.12 µV | 1.87 | 0.56 | [0.34, 6.64] |
| 4 to 6 | 13 | 1.67 µV | 1.18 | 0.33 | [0.22, 3.71] |
| 5 to 6 | 12 | 1.67 µV | 0.78 | 0.23 | [0.47, 3.21] |
| Cardinality6 | 13 | 1.45 µV | 1.19 | 0.33 | [-0.03, 3.45] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 11 | 91.63 ms | 7.20 | 2.17 | [78.68, 99.69] |
| 4 to 6 | 13 | 93.94 ms | 7.55 | 2.09 | [77.89, 105.14] |
| 5 to 6 | 12 | 92.60 ms | 5.88 | 1.70 | [82.30, 105.10] |
| Cardinality6 | 13 | 92.49 ms | 8.35 | 2.32 | [78.15, 106.97] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 3.11 µV | 2.03 | 0.47 | [0.29, 9.00] |
| 4 to 6 | 18 | 3.68 µV | 2.51 | 0.59 | [0.17, 7.42] |
| 5 to 6 | 8 | 3.23 µV | 3.10 | 1.09 | [0.45, 8.22] |
| Cardinality6 | 14 | 3.13 µV | 2.19 | 0.58 | [0.49, 8.39] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 471.24 ms | 12.67 | 2.91 | [446.16, 500.22] |
| 4 to 6 | 18 | 472.30 ms | 11.94 | 2.81 | [446.00, 500.49] |
| 5 to 6 | 8 | 470.78 ms | 13.76 | 4.86 | [448.67, 495.17] |
| Cardinality6 | 14 | 472.66 ms | 9.66 | 2.58 | [455.56, 495.04] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.70, *p* = 0.054, η²_G = 0.049
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.48 | 20 | = 0.277 | -0.34 [-0.76, 0.15] | small | n.s. |
| 3 to 6 vs 5 to 6 | -1.24 | 20 | = 0.277 | -0.32 [-0.72, 0.18] | small | n.s. |
| 3 to 6 vs Cardinality6 | -3.12 | 20 | = 0.032 | -0.59 [-1.19, -0.18] | medium | * |
| 4 to 6 vs 5 to 6 | 0.11 | 20 | = 0.910 | 0.03 [-0.44, 0.45] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | -1.68 | 20 | = 0.277 | -0.27 [-0.84, 0.10] | small | n.s. |
| 5 to 6 vs Cardinality6 | -1.32 | 20 | = 0.277 | -0.30 [-0.75, 0.18] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 372.16, BIC = 387.09
- Condition effect: *β* = 0.66, *SE* = 0.443, *z* = 1.496, *p* = 0.135

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.01, *p* = 0.395, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 1.01 | 20 | = 0.652 | 0.19 [-0.17, 0.74] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -0.54 | 20 | = 0.741 | -0.11 [-0.55, 0.34] | negligible | n.s. |
| 3 to 6 vs Cardinality6 | -0.51 | 20 | = 0.741 | -0.09 [-0.57, 0.35] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -1.72 | 20 | = 0.301 | -0.30 [-0.89, 0.03] | small | n.s. |
| 4 to 6 vs Cardinality6 | -1.86 | 20 | = 0.301 | -0.25 [-0.88, 0.07] | small | n.s. |
| 5 to 6 vs Cardinality6 | 0.06 | 20 | = 0.956 | 0.01 [-0.44, 0.47] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 645.40, BIC = 660.33
- Condition effect: *β* = -2.36, *SE* = 1.903, *z* = -1.242, *p* = 0.214


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.65, *p* = 0.603, η²_G = 0.138
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.73 | 3 | = 0.779 | 0.45 [-0.53, 1.03] | small | n.s. |
| 3 to 6 vs 5 to 6 | 0.93 | 3 | = 0.779 | 0.90 [-0.81, 1.32] | large | n.s. |
| 3 to 6 vs Cardinality6 | 1.62 | 3 | = 0.779 | 0.89 [-0.65, 1.55] | large | n.s. |
| 4 to 6 vs 5 to 6 | 0.39 | 3 | = 0.867 | 0.32 [-0.91, 0.94] | small | n.s. |
| 4 to 6 vs Cardinality6 | 0.74 | 3 | = 0.779 | 0.31 [-0.38, 1.64] | small | n.s. |
| 5 to 6 vs Cardinality6 | -0.00 | 3 | = 0.997 | -0.00 [-1.37, 0.55] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 170.44, BIC = 181.79
- Condition effect: *β* = -0.39, *SE* = 0.466, *z* = -0.842, *p* = 0.400

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.07, *p* = 0.175, η²_G = 0.274
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.60 | 3 | = 0.325 | -0.92 [-0.93, 0.62] | large | n.s. |
| 3 to 6 vs 5 to 6 | -2.25 | 3 | = 0.325 | -1.28 [-2.09, 0.37] | large | n.s. |
| 3 to 6 vs Cardinality6 | 0.20 | 3 | = 0.851 | 0.13 [-1.16, 0.95] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -0.25 | 3 | = 0.851 | -0.20 [-1.15, 0.72] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | 1.56 | 3 | = 0.325 | 0.89 [-0.60, 1.30] | large | n.s. |
| 5 to 6 vs Cardinality6 | 3.06 | 3 | = 0.325 | 1.17 [-0.65, 1.24] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 340.70, BIC = 352.05
- Condition effect: *β* = 2.21, *SE* = 2.656, *z* = 0.834, *p* = 0.404


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.75, *p* = 0.537, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.84 | 5 | = 0.719 | -0.30 [-0.87, 0.22] | small | n.s. |
| 3 to 6 vs 5 to 6 | -0.64 | 5 | = 0.719 | -0.29 [-0.67, 1.01] | small | n.s. |
| 3 to 6 vs Cardinality6 | 0.56 | 5 | = 0.719 | 0.29 [-0.77, 0.45] | small | n.s. |
| 4 to 6 vs 5 to 6 | -0.21 | 5 | = 0.841 | -0.05 [-0.56, 1.15] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | 1.08 | 5 | = 0.719 | 0.46 [-0.26, 1.06] | small | n.s. |
| 5 to 6 vs Cardinality6 | 1.23 | 5 | = 0.719 | 0.43 [-0.61, 1.62] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 262.60, BIC = 275.06
- Condition effect: *β* = 0.59, *SE* = 0.534, *z* = 1.106, *p* = 0.269

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.15, *p* = 0.362, η²_G = 0.163
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.63 | 5 | = 0.668 | 0.44 [-0.72, 0.35] | small | n.s. |
| 3 to 6 vs 5 to 6 | 1.52 | 5 | = 0.593 | 0.98 [-0.96, 0.72] | large | n.s. |
| 3 to 6 vs Cardinality6 | -0.35 | 5 | = 0.740 | -0.23 [-0.75, 0.46] | small | n.s. |
| 4 to 6 vs 5 to 6 | 0.93 | 5 | = 0.593 | 0.52 [-0.68, 1.00] | medium | n.s. |
| 4 to 6 vs Cardinality6 | -0.97 | 5 | = 0.593 | -0.47 [-0.78, 0.50] | small | n.s. |
| 5 to 6 vs Cardinality6 | -1.30 | 5 | = 0.593 | -0.88 [-1.65, 0.59] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 463.96, BIC = 476.42
- Condition effect: *β* = 1.63, *SE* = 3.204, *z* = 0.507, *p* = 0.612


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.054)

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
