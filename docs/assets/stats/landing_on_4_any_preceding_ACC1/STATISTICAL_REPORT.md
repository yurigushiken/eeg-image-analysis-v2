# Statistical Analysis Report: tables

**Generated:** 2025-10-15 22:45:43

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
| 1 to 4 | 22 | -4.69 µV | 2.82 | 0.60 | [-10.85, -0.31] |
| 2 to 4 | 21 | -4.37 µV | 2.10 | 0.46 | [-10.88, -1.48] |
| 3 to 4 | 23 | -3.53 µV | 1.79 | 0.37 | [-7.41, -0.90] |
| 5 to 4 | 22 | -4.08 µV | 2.30 | 0.49 | [-8.57, -0.83] |
| 6 to 4 | 23 | -3.74 µV | 2.20 | 0.46 | [-9.80, -0.48] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | 173.27 ms | 9.00 | 1.92 | [158.31, 195.92] |
| 2 to 4 | 21 | 171.85 ms | 7.11 | 1.55 | [154.05, 183.51] |
| 3 to 4 | 23 | 170.44 ms | 10.06 | 2.10 | [146.84, 197.14] |
| 5 to 4 | 22 | 176.45 ms | 8.67 | 1.85 | [163.05, 196.79] |
| 6 to 4 | 23 | 174.75 ms | 10.70 | 2.23 | [158.72, 199.51] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 2.14 µV | 1.65 | 0.46 | [0.05, 5.24] |
| 2 to 4 | 17 | 1.74 µV | 1.43 | 0.35 | [0.00, 5.30] |
| 3 to 4 | 14 | 1.96 µV | 2.00 | 0.53 | [0.07, 6.16] |
| 5 to 4 | 14 | 2.06 µV | 1.62 | 0.43 | [-0.07, 4.48] |
| 6 to 4 | 16 | 2.35 µV | 1.46 | 0.37 | [0.56, 5.94] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 103.90 ms | 6.09 | 1.69 | [92.84, 115.61] |
| 2 to 4 | 17 | 105.75 ms | 7.01 | 1.70 | [93.65, 118.57] |
| 3 to 4 | 14 | 105.62 ms | 7.36 | 1.97 | [93.48, 119.04] |
| 5 to 4 | 14 | 107.09 ms | 5.02 | 1.34 | [95.91, 113.95] |
| 6 to 4 | 16 | 108.19 ms | 5.90 | 1.47 | [94.68, 115.00] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 3.94 µV | 2.91 | 0.65 | [0.48, 10.44] |
| 2 to 4 | 19 | 4.68 µV | 3.29 | 0.75 | [0.11, 10.40] |
| 3 to 4 | 16 | 4.38 µV | 2.28 | 0.57 | [0.42, 7.40] |
| 5 to 4 | 21 | 3.76 µV | 2.76 | 0.60 | [0.66, 8.70] |
| 6 to 4 | 18 | 3.89 µV | 2.31 | 0.54 | [0.86, 8.86] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 485.35 ms | 13.47 | 3.01 | [461.91, 503.73] |
| 2 to 4 | 19 | 491.45 ms | 17.85 | 4.10 | [450.50, 531.73] |
| 3 to 4 | 16 | 492.15 ms | 13.20 | 3.30 | [459.00, 513.88] |
| 5 to 4 | 21 | 492.48 ms | 17.01 | 3.71 | [454.76, 524.39] |
| 6 to 4 | 18 | 493.34 ms | 16.30 | 3.84 | [465.95, 531.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.75, *p* = 0.149, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.53 | 18 | = 0.359 | -0.31 [-0.74, 0.21] | small | n.s. |
| 1 to 4 vs 3 to 4 | -3.14 | 18 | = 0.057 | -0.61 [-0.94, -0.01] | medium | n.s. |
| 1 to 4 vs 5 to 4 | -1.03 | 18 | = 0.450 | -0.23 [-0.74, 0.19] | small | n.s. |
| 1 to 4 vs 6 to 4 | -1.17 | 18 | = 0.430 | -0.29 [-0.70, 0.22] | small | n.s. |
| 2 to 4 vs 3 to 4 | -1.40 | 18 | = 0.359 | -0.35 [-0.92, 0.04] | small | n.s. |
| 2 to 4 vs 5 to 4 | 0.31 | 18 | = 0.896 | 0.09 [-0.46, 0.47] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 0.08 | 18 | = 0.940 | 0.02 [-0.53, 0.41] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | 1.43 | 18 | = 0.359 | 0.42 [-0.25, 0.67] | small | n.s. |
| 3 to 4 vs 6 to 4 | 1.48 | 18 | = 0.359 | 0.38 [-0.32, 0.57] | small | n.s. |
| 5 to 4 vs 6 to 4 | -0.25 | 18 | = 0.896 | -0.06 [-0.52, 0.39] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 484.83, BIC = 503.79
- Condition effect: *β* = 0.36, *SE* = 0.537, *z* = 0.664, *p* = 0.507

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 3.42, *p* = 0.013, η²_G = 0.066
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.29 | 18 | = 0.864 | 0.08 [-0.44, 0.50] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 2.38 | 18 | = 0.085 | 0.41 [0.03, 0.97] | small | n.s. |
| 1 to 4 vs 5 to 4 | -2.38 | 18 | = 0.085 | -0.40 [-1.14, -0.14] | small | n.s. |
| 1 to 4 vs 6 to 4 | -0.03 | 18 | = 0.974 | -0.01 [-0.48, 0.43] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 1.47 | 18 | = 0.225 | 0.35 [-0.25, 0.67] | small | n.s. |
| 2 to 4 vs 5 to 4 | -2.30 | 18 | = 0.085 | -0.51 [-1.01, -0.01] | medium | n.s. |
| 2 to 4 vs 6 to 4 | -0.41 | 18 | = 0.857 | -0.09 [-0.65, 0.29] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -3.82 | 18 | = 0.013 | -0.81 [-1.45, -0.37] | large | * |
| 3 to 4 vs 6 to 4 | -1.94 | 18 | = 0.137 | -0.40 [-1.01, -0.06] | small | n.s. |
| 5 to 4 vs 6 to 4 | 1.54 | 18 | = 0.225 | 0.38 [-0.10, 0.84] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 762.45, BIC = 781.42
- Condition effect: *β* = -1.09, *SE* = 1.702, *z* = -0.643, *p* = 0.520


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.29, *p* = 0.316, η²_G = 0.118
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -2.25 | 4 | = 0.292 | -0.49 [-0.70, 0.64] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.46 | 4 | = 0.883 | 0.23 [-0.46, 1.12] | small | n.s. |
| 1 to 4 vs 5 to 4 | 0.12 | 4 | = 0.911 | 0.07 [-0.63, 0.92] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -1.24 | 4 | = 0.555 | -0.45 [-0.91, 0.45] | small | n.s. |
| 2 to 4 vs 3 to 4 | 2.44 | 4 | = 0.292 | 1.02 [-0.80, 0.64] | large | n.s. |
| 2 to 4 vs 5 to 4 | 1.28 | 4 | = 0.555 | 0.64 [-0.64, 0.70] | medium | n.s. |
| 2 to 4 vs 6 to 4 | 0.28 | 4 | = 0.883 | 0.08 [-1.03, 0.35] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -0.32 | 4 | = 0.883 | -0.17 [-0.63, 1.06] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | -3.78 | 4 | = 0.194 | -1.05 [-1.75, -0.06] | large | n.s. |
| 5 to 4 vs 6 to 4 | -1.10 | 4 | = 0.555 | -0.62 [-0.98, 0.47] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 282.17, BIC = 298.30
- Condition effect: *β* = -0.40, *SE* = 0.492, *z* = -0.811, *p* = 0.418

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.94, *p* = 0.467, η²_G = 0.063
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.85 | 4 | = 0.738 | -0.34 [-1.47, 0.03] | small | n.s. |
| 1 to 4 vs 3 to 4 | -1.49 | 4 | = 0.738 | -0.57 [-1.38, 0.27] | medium | n.s. |
| 1 to 4 vs 5 to 4 | -0.80 | 4 | = 0.738 | -0.47 [-1.16, 0.43] | small | n.s. |
| 1 to 4 vs 6 to 4 | -1.15 | 4 | = 0.738 | -0.40 [-1.47, 0.04] | small | n.s. |
| 2 to 4 vs 3 to 4 | -1.64 | 4 | = 0.738 | -0.35 [-0.97, 0.48] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.52 | 4 | = 0.738 | -0.19 [-0.92, 0.44] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.47 | 4 | = 0.738 | -0.12 [-0.65, 0.69] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | 0.52 | 4 | = 0.738 | 0.16 [-0.60, 1.10] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 1.26 | 4 | = 0.738 | 0.18 [-0.93, 0.52] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 0.13 | 4 | = 0.906 | 0.04 [-0.76, 0.67] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 479.34, BIC = 495.47
- Condition effect: *β* = 2.66, *SE* = 1.805, *z* = 1.472, *p* = 0.141


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.63, *p* = 0.182, η²_G = 0.059
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.42 | 12 | = 0.441 | -0.32 [-0.88, 0.14] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.35 | 12 | = 0.810 | 0.09 [-0.59, 0.52] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | 0.46 | 12 | = 0.810 | 0.09 [-0.44, 0.49] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 1.17 | 12 | = 0.441 | 0.40 [-0.38, 0.65] | small | n.s. |
| 2 to 4 vs 3 to 4 | 1.42 | 12 | = 0.441 | 0.48 [-0.37, 0.79] | small | n.s. |
| 2 to 4 vs 5 to 4 | 1.32 | 12 | = 0.441 | 0.42 [-0.20, 0.78] | small | n.s. |
| 2 to 4 vs 6 to 4 | 1.83 | 12 | = 0.441 | 0.78 [-0.22, 0.83] | medium | n.s. |
| 3 to 4 vs 5 to 4 | 0.04 | 12 | = 0.965 | 0.01 [-0.44, 0.68] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 1.24 | 12 | = 0.441 | 0.37 [-0.30, 0.88] | small | n.s. |
| 5 to 4 vs 6 to 4 | 0.99 | 12 | = 0.488 | 0.30 [-0.47, 0.52] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 436.39, BIC = 454.19
- Condition effect: *β* = 0.75, *SE* = 0.608, *z* = 1.227, *p* = 0.220

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.39, *p* = 0.818, η²_G = 0.024
- Greenhouse-Geisser corrected: *p* = 0.724 (ε = 0.612)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.34 | 12 | = 0.968 | -0.44 [-0.96, 0.08] | small | n.s. |
| 1 to 4 vs 3 to 4 | -0.99 | 12 | = 0.968 | -0.32 [-0.95, 0.20] | small | n.s. |
| 1 to 4 vs 5 to 4 | -0.87 | 12 | = 0.968 | -0.39 [-0.69, 0.25] | small | n.s. |
| 1 to 4 vs 6 to 4 | -0.98 | 12 | = 0.968 | -0.38 [-0.81, 0.24] | small | n.s. |
| 2 to 4 vs 3 to 4 | 0.17 | 12 | = 0.968 | 0.07 [-0.69, 0.47] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.03 | 12 | = 0.980 | -0.01 [-0.50, 0.46] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.18 | 12 | = 0.968 | -0.06 [-0.50, 0.53] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -0.19 | 12 | = 0.968 | -0.07 [-0.64, 0.47] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | -0.23 | 12 | = 0.968 | -0.11 [-0.64, 0.51] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.17 | 12 | = 0.968 | -0.05 [-0.56, 0.44] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 793.98, BIC = 811.78
- Condition effect: *β* = 6.11, *SE* = 4.912, *z* = 1.243, *p* = 0.214


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.013). Post-hoc tests revealed:
  - 3 to 4 showed smaller latency than 5 to 4 (*d* = -0.81)

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
