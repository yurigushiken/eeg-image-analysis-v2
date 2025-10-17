# Statistical Analysis Report: tables

**Generated:** 2025-10-16 21:43:33

---

## 1. Analysis Overview

**Total Measurements:** 216
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| 1 to 2 | 21 | -3.16 µV | 1.69 | 0.37 | [-7.08, 0.01] |
| 1 to 3 | 24 | -4.07 µV | 1.69 | 0.34 | [-8.33, -1.07] |
| 1 to 4 | 21 | -4.32 µV | 2.29 | 0.50 | [-9.44, -0.91] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | 173.22 ms | 12.51 | 2.73 | [150.64, 203.14] |
| 1 to 3 | 24 | 174.66 ms | 11.91 | 2.43 | [150.40, 203.06] |
| 1 to 4 | 21 | 173.89 ms | 11.58 | 2.53 | [152.99, 199.31] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 10 | 1.67 µV | 1.31 | 0.41 | [0.03, 3.62] |
| 1 to 3 | 10 | 1.26 µV | 1.06 | 0.33 | [0.21, 3.63] |
| 1 to 4 | 15 | 1.50 µV | 0.90 | 0.23 | [-0.00, 2.54] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 10 | 84.93 ms | 6.31 | 1.99 | [73.21, 94.25] |
| 1 to 3 | 10 | 84.36 ms | 9.05 | 2.86 | [71.59, 98.89] |
| 1 to 4 | 15 | 85.51 ms | 6.01 | 1.55 | [75.94, 98.17] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 15 | 3.72 µV | 2.67 | 0.69 | [0.25, 10.38] |
| 1 to 3 | 19 | 3.97 µV | 3.10 | 0.71 | [0.54, 12.57] |
| 1 to 4 | 20 | 3.68 µV | 2.80 | 0.63 | [0.43, 10.61] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 15 | 446.97 ms | 28.14 | 7.27 | [390.52, 488.12] |
| 1 to 3 | 19 | 459.74 ms | 21.79 | 5.00 | [398.45, 487.95] |
| 1 to 4 | 20 | 453.62 ms | 30.52 | 6.82 | [383.28, 508.73] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.46, *p* = 0.100, η²_G = 0.045
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.48 | 18 | = 0.070 | 0.55 [0.10, 1.09] | medium | n.s. |
| 1 to 2 vs 1 to 4 | 1.92 | 18 | = 0.106 | 0.41 [-0.06, 0.95] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.13 | 18 | = 0.900 | -0.03 [-0.47, 0.44] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 264.39, BIC = 275.34
- Condition effect: *β* = -0.91, *SE* = 0.394, *z* = -2.301, *p* = 0.021

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.36, *p* = 0.702, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.51 | 18 | = 0.784 | 0.12 [-0.46, 0.45] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.28 | 18 | = 0.784 | -0.04 [-0.55, 0.42] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -0.84 | 18 | = 0.784 | -0.18 [-0.62, 0.29] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 501.33, BIC = 512.27
- Condition effect: *β* = 0.63, *SE* = 2.225, *z* = 0.281, *p* = 0.778


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.60, *p* = 0.580, η²_G = 0.151
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.49 | 3 | = 0.664 | 0.47 [-0.78, 1.36] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.58 | 3 | = 0.636 | 1.03 [-0.59, 2.32] | large | n.s. |
| 1 to 3 vs 1 to 4 | 0.48 | 3 | = 0.664 | 0.38 [-1.08, 0.62] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 111.01, BIC = 118.79
- Condition effect: *β* = -0.41, *SE* = 0.484, *z* = -0.853, *p* = 0.394

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.88, *p* = 0.232, η²_G = 0.163
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 1.08 | 3 | = 0.529 | 0.57 [-0.42, 1.97] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -0.71 | 3 | = 0.529 | -0.42 [-1.96, 0.74] | small | n.s. |
| 1 to 3 vs 1 to 4 | -2.04 | 3 | = 0.403 | -0.79 [-0.85, 0.83] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 243.09, BIC = 250.87
- Condition effect: *β* = -0.60, *SE* = 2.992, *z* = -0.200, *p* = 0.842


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.03, *p* = 0.372, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.08 | 13 | = 0.447 | -0.25 [-0.88, 0.30] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.27 | 13 | = 0.447 | -0.27 [-0.90, 0.24] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.03 | 13 | = 0.978 | 0.00 [-0.38, 0.58] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 246.48, BIC = 256.42
- Condition effect: *β* = 0.72, *SE* = 0.532, *z* = 1.358, *p* = 0.174

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.93, *p* = 0.408, η²_G = 0.049
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.22 | 13 | = 0.543 | -0.46 [-0.92, 0.27] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.95 | 13 | = 0.543 | -0.45 [-0.67, 0.44] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.08 | 13 | = 0.938 | 0.02 [-0.37, 0.60] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 516.32, BIC = 526.27
- Condition effect: *β* = 12.77, *SE* = 9.141, *z* = 1.397, *p* = 0.162


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.100)

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
