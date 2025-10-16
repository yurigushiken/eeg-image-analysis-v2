# Statistical Analysis Report: tables

**Generated:** 2025-10-16 03:44:42

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
| 4 to 3 | 23 | -4.05 µV | 1.92 | 0.40 | [-8.43, -0.80] |
| 5 to 3 | 24 | -3.70 µV | 2.30 | 0.47 | [-8.52, -0.14] |
| 6 to 3 | 23 | -4.26 µV | 1.88 | 0.39 | [-8.14, -0.89] |
| Cardinality3 | 23 | -3.06 µV | 1.76 | 0.37 | [-7.52, -0.40] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | 176.78 ms | 10.81 | 2.25 | [157.10, 207.20] |
| 5 to 3 | 24 | 176.27 ms | 10.94 | 2.23 | [153.65, 210.96] |
| 6 to 3 | 23 | 176.80 ms | 9.33 | 1.95 | [161.46, 203.24] |
| Cardinality3 | 23 | 175.90 ms | 12.73 | 2.65 | [151.93, 209.22] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 11 | 1.73 µV | 1.24 | 0.37 | [0.17, 4.40] |
| 5 to 3 | 17 | 1.81 µV | 1.17 | 0.28 | [0.25, 3.56] |
| 6 to 3 | 14 | 1.58 µV | 1.79 | 0.48 | [0.05, 6.60] |
| Cardinality3 | 13 | 2.24 µV | 1.94 | 0.54 | [0.09, 7.05] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 11 | 105.26 ms | 5.31 | 1.60 | [94.84, 112.76] |
| 5 to 3 | 17 | 108.07 ms | 4.34 | 1.05 | [98.40, 115.86] |
| 6 to 3 | 14 | 107.65 ms | 7.13 | 1.91 | [95.27, 119.64] |
| Cardinality3 | 13 | 106.75 ms | 5.04 | 1.40 | [95.89, 114.48] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 19 | 3.54 µV | 2.52 | 0.58 | [0.53, 8.69] |
| 5 to 3 | 20 | 3.39 µV | 1.64 | 0.37 | [0.40, 6.85] |
| 6 to 3 | 19 | 4.06 µV | 2.65 | 0.61 | [1.25, 11.29] |
| Cardinality3 | 15 | 2.61 µV | 1.92 | 0.50 | [0.28, 6.74] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 19 | 458.05 ms | 22.20 | 5.09 | [409.15, 495.67] |
| 5 to 3 | 20 | 460.14 ms | 20.30 | 4.54 | [407.46, 491.60] |
| 6 to 3 | 19 | 458.80 ms | 22.11 | 5.07 | [406.41, 502.51] |
| Cardinality3 | 15 | 448.46 ms | 20.38 | 5.26 | [410.44, 472.66] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.16, *p* = 0.031, η²_G = 0.056
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -1.22 | 20 | = 0.296 | -0.21 [-0.73, 0.15] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.45 | 20 | = 0.657 | 0.10 [-0.40, 0.49] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -2.64 | 20 | = 0.061 | -0.56 [-1.05, -0.09] | medium | n.s. |
| 5 to 3 vs 6 to 3 | 1.48 | 20 | = 0.296 | 0.30 [-0.24, 0.63] | small | n.s. |
| 5 to 3 vs Cardinality3 | -1.19 | 20 | = 0.296 | -0.28 [-0.75, 0.14] | small | n.s. |
| 6 to 3 vs Cardinality3 | -2.52 | 20 | = 0.061 | -0.66 [-1.04, -0.08] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 369.91, BIC = 385.11
- Condition effect: *β* = 0.37, *SE* = 0.391, *z* = 0.936, *p* = 0.349

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.33, *p* = 0.804, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.723 (ε = 0.673)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.14 | 20 | = 0.895 | 0.03 [-0.38, 0.48] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.78 | 20 | = 0.888 | -0.15 [-0.70, 0.20] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 0.21 | 20 | = 0.895 | 0.05 [-0.41, 0.48] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -1.03 | 20 | = 0.888 | -0.18 [-0.70, 0.18] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.13 | 20 | = 0.895 | 0.03 [-0.41, 0.46] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 1.09 | 20 | = 0.888 | 0.18 [-0.28, 0.61] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 665.46, BIC = 680.66
- Condition effect: *β* = -0.30, *SE* = 1.754, *z* = -0.170, *p* = 0.865


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.27, *p* = 0.846, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.77 | 5 | = 0.938 | 0.34 [-0.65, 0.78] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.08 | 5 | = 0.938 | 0.04 [-0.74, 0.94] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -0.48 | 5 | = 0.938 | -0.25 [-1.07, 0.63] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.24 | 5 | = 0.938 | -0.17 [-0.57, 0.70] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -0.66 | 5 | = 0.938 | -0.44 [-0.82, 0.53] | small | n.s. |
| 6 to 3 vs Cardinality3 | -0.90 | 5 | = 0.938 | -0.24 [-1.12, 0.28] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 208.15, BIC = 220.19
- Condition effect: *β* = 0.09, *SE* = 0.504, *z* = 0.176, *p* = 0.861

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.13, *p* = 0.942, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.12 | 5 | = 0.911 | 0.05 [-1.03, 0.43] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.41 | 5 | = 0.911 | -0.14 [-1.29, 0.46] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -0.41 | 5 | = 0.911 | -0.14 [-0.94, 0.74] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.39 | 5 | = 0.911 | -0.17 [-0.82, 0.46] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -0.51 | 5 | = 0.911 | -0.19 [-0.65, 0.69] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 0.15 | 5 | = 0.911 | 0.04 [-0.25, 1.17] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 341.06, BIC = 353.11
- Condition effect: *β* = 2.31, *SE* = 1.566, *z* = 1.476, *p* = 0.140


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.58, *p* = 0.211, η²_G = 0.058
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.07 | 13 | = 0.942 | -0.02 [-0.41, 0.59] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.69 | 13 | = 0.747 | -0.16 [-0.73, 0.28] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.54 | 13 | = 0.318 | 0.48 [-0.19, 1.01] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.50 | 13 | = 0.747 | -0.15 [-0.72, 0.26] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 1.49 | 13 | = 0.318 | 0.59 [-0.17, 0.98] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 1.83 | 13 | = 0.318 | 0.59 [-0.13, 1.03] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 321.92, BIC = 335.66
- Condition effect: *β* = -0.16, *SE* = 0.562, *z* = -0.277, *p* = 0.782

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.57, *p* = 0.211, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.45 | 13 | = 0.657 | -0.17 [-0.54, 0.46] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -1.03 | 13 | = 0.539 | -0.32 [-0.47, 0.52] | small | n.s. |
| 4 to 3 vs Cardinality3 | 0.95 | 13 | = 0.539 | 0.36 [-0.33, 0.84] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.46 | 13 | = 0.657 | -0.16 [-0.48, 0.48] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 1.94 | 13 | = 0.224 | 0.58 [-0.10, 1.07] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 2.05 | 13 | = 0.224 | 0.76 [-0.00, 1.20] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 658.14, BIC = 671.89
- Condition effect: *β* = 1.70, *SE* = 5.953, *z* = 0.285, *p* = 0.776


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.031) (no significant pairwise comparisons)

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
