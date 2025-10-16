# Statistical Analysis Report: tables

**Generated:** 2025-10-16 03:45:04

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
| 4 to 3 | 23 | -3.78 µV | 1.84 | 0.38 | [-8.01, -0.64] |
| 5 to 3 | 24 | -3.42 µV | 2.26 | 0.46 | [-8.30, -0.20] |
| 6 to 3 | 23 | -4.15 µV | 2.05 | 0.43 | [-9.49, -0.82] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | 176.52 ms | 12.73 | 2.66 | [153.98, 210.92] |
| 5 to 3 | 24 | 177.19 ms | 13.54 | 2.76 | [149.19, 216.16] |
| 6 to 3 | 23 | 177.82 ms | 11.17 | 2.33 | [162.68, 208.58] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 1.61 µV | 1.28 | 0.37 | [0.16, 4.63] |
| 5 to 3 | 16 | 2.12 µV | 1.13 | 0.28 | [0.44, 3.80] |
| 6 to 3 | 14 | 1.72 µV | 1.84 | 0.49 | [0.07, 6.32] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 107.07 ms | 4.98 | 1.44 | [97.03, 115.73] |
| 5 to 3 | 16 | 109.44 ms | 2.71 | 0.68 | [105.56, 114.90] |
| 6 to 3 | 14 | 108.84 ms | 6.26 | 1.67 | [97.43, 118.94] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 20 | 3.77 µV | 2.75 | 0.61 | [0.11, 9.18] |
| 5 to 3 | 19 | 3.63 µV | 1.86 | 0.43 | [0.37, 7.76] |
| 6 to 3 | 19 | 4.29 µV | 2.78 | 0.64 | [0.50, 11.72] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 20 | 474.69 ms | 21.74 | 4.86 | [423.11, 529.59] |
| 5 to 3 | 19 | 465.98 ms | 21.21 | 4.87 | [418.41, 491.72] |
| 6 to 3 | 19 | 467.91 ms | 19.04 | 4.37 | [421.90, 507.55] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.46, *p* = 0.243, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -1.06 | 21 | = 0.455 | -0.20 [-0.69, 0.19] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.73 | 21 | = 0.471 | 0.16 [-0.29, 0.60] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 1.60 | 21 | = 0.376 | 0.34 [-0.17, 0.72] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 288.74, BIC = 299.98
- Condition effect: *β* = 0.38, *SE* = 0.404, *z* = 0.936, *p* = 0.349

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.32, *p* = 0.111, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.43 | 21 | = 0.674 | -0.07 [-0.55, 0.32] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -2.65 | 21 | = 0.045 | -0.32 [-1.04, -0.09] | small | * |
| 5 to 3 vs 6 to 3 | -1.35 | 21 | = 0.289 | -0.25 [-0.68, 0.20] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 510.99, BIC = 522.24
- Condition effect: *β* = 1.07, *SE* = 1.623, *z* = 0.658, *p* = 0.510


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.31, *p* = 0.741, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.84 | 5 | = 0.707 | -0.21 [-1.43, 0.24] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.23 | 5 | = 0.831 | 0.11 [-0.88, 0.79] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.78 | 5 | = 0.707 | 0.36 [-0.25, 1.16] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 148.85, BIC = 157.54
- Condition effect: *β* = 0.57, *SE* = 0.389, *z* = 1.474, *p* = 0.140

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.23, *p* = 0.798, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.82 | 5 | = 0.836 | -0.36 [-1.31, 0.32] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.42 | 5 | = 0.836 | -0.14 [-1.09, 0.60] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.22 | 5 | = 0.836 | 0.10 [-0.70, 0.65] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 249.90, BIC = 258.59
- Condition effect: *β* = 2.09, *SE* = 1.323, *z* = 1.581, *p* = 0.114


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.65, *p* = 0.529, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.66 | 16 | = 0.635 | 0.18 [-0.36, 0.68] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.48 | 16 | = 0.635 | -0.09 [-0.58, 0.42] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -1.07 | 16 | = 0.635 | -0.28 [-0.78, 0.24] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 264.66, BIC = 274.96
- Condition effect: *β* = -0.33, *SE* = 0.561, *z* = -0.585, *p* = 0.559

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.13, *p* = 0.135, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 1.90 | 16 | = 0.226 | 0.52 [-0.08, 1.00] | medium | n.s. |
| 4 to 3 vs 6 to 3 | 1.42 | 16 | = 0.264 | 0.34 [-0.16, 0.86] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.75 | 16 | = 0.463 | -0.21 [-0.67, 0.33] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 514.08, BIC = 524.39
- Condition effect: *β* = -9.94, *SE* = 4.997, *z* = -1.990, *p* = 0.047


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
