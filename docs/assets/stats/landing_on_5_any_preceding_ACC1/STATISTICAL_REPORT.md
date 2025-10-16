# Statistical Analysis Report: tables

**Generated:** 2025-10-16 00:51:46

---

## 1. Analysis Overview

**Total Measurements:** 264
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
| 2 to 5 | 24 | -3.72 µV | 2.21 | 0.45 | [-9.99, 0.02] |
| 3 to 5 | 22 | -3.47 µV | 2.25 | 0.48 | [-9.70, -0.40] |
| 4 to 5 | 22 | -4.49 µV | 3.01 | 0.64 | [-11.95, -1.12] |
| 6 to 5 | 15 | -4.18 µV | 1.40 | 0.36 | [-6.30, -1.98] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 174.10 ms | 14.31 | 2.92 | [149.15, 203.98] |
| 3 to 5 | 22 | 167.84 ms | 12.81 | 2.73 | [145.38, 198.22] |
| 4 to 5 | 22 | 169.95 ms | 12.54 | 2.67 | [145.16, 194.79] |
| 6 to 5 | 15 | 171.77 ms | 14.46 | 3.73 | [149.00, 195.23] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 12 | 1.59 µV | 1.84 | 0.53 | [0.05, 6.77] |
| 3 to 5 | 13 | 1.73 µV | 1.37 | 0.38 | [0.29, 4.47] |
| 4 to 5 | 16 | 3.35 µV | 3.94 | 0.98 | [-0.06, 13.16] |
| 6 to 5 | 4 | 1.55 µV | 0.96 | 0.48 | [0.64, 2.89] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 12 | 95.42 ms | 7.08 | 2.04 | [84.09, 107.27] |
| 3 to 5 | 13 | 96.77 ms | 6.28 | 1.74 | [86.45, 105.91] |
| 4 to 5 | 16 | 97.65 ms | 5.58 | 1.40 | [87.58, 107.78] |
| 6 to 5 | 4 | 98.15 ms | 6.20 | 3.10 | [91.45, 105.34] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 21 | 3.11 µV | 2.12 | 0.46 | [0.00, 7.81] |
| 3 to 5 | 16 | 3.48 µV | 2.45 | 0.61 | [0.25, 9.03] |
| 4 to 5 | 15 | 4.05 µV | 2.66 | 0.69 | [0.05, 9.86] |
| 6 to 5 | 12 | 2.27 µV | 1.61 | 0.46 | [0.49, 5.14] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 21 | 467.39 ms | 27.56 | 6.02 | [404.16, 508.46] |
| 3 to 5 | 16 | 479.58 ms | 38.82 | 9.71 | [390.44, 559.09] |
| 4 to 5 | 15 | 501.48 ms | 27.94 | 7.21 | [456.96, 558.74] |
| 6 to 5 | 12 | 501.16 ms | 49.84 | 14.39 | [398.39, 562.12] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.90, *p* = 0.016, η²_G = 0.108
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.86 | 13 | = 0.487 | -0.15 [-0.74, 0.16] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 2.68 | 13 | = 0.056 | 0.61 [-0.16, 0.75] | medium | n.s. |
| 2 to 5 vs 6 to 5 | 0.53 | 13 | = 0.604 | 0.16 [-0.34, 0.78] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 2.73 | 13 | = 0.056 | 0.77 [-0.03, 0.93] | medium | n.s. |
| 3 to 5 vs 6 to 5 | 1.26 | 13 | = 0.344 | 0.37 [-0.26, 0.93] | small | n.s. |
| 4 to 5 vs 6 to 5 | -1.61 | 13 | = 0.264 | -0.56 [-1.03, 0.17] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 363.59, BIC = 378.10
- Condition effect: *β* = 0.37, *SE* = 0.482, *z* = 0.774, *p* = 0.439

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.07, *p* = 0.374, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.50 | 13 | = 0.472 | 0.28 [0.00, 0.93] | small | n.s. |
| 2 to 5 vs 4 to 5 | 2.04 | 13 | = 0.374 | 0.41 [-0.24, 0.66] | small | n.s. |
| 2 to 5 vs 6 to 5 | 0.69 | 13 | = 0.644 | 0.16 [-0.30, 0.83] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 0.41 | 13 | = 0.691 | 0.10 [-0.58, 0.33] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -0.63 | 13 | = 0.644 | -0.12 [-0.75, 0.41] | negligible | n.s. |
| 4 to 5 vs 6 to 5 | -0.72 | 13 | = 0.644 | -0.23 [-0.78, 0.39] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 649.26, BIC = 663.77
- Condition effect: *β* = -5.58, *SE* = 2.652, *z* = -2.104, *p* = 0.035


### 3.2 P1 Component

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

**Pairwise Comparisons:**

_Pairwise tests could not be computed (insufficient paired samples)._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 223.07, BIC = 233.91
- Condition effect: *β* = 0.03, *SE* = 0.938, *z* = 0.029, *p* = 0.977

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

**Pairwise Comparisons:**

_Pairwise tests could not be computed (insufficient paired samples)._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 299.92, BIC = 310.76
- Condition effect: *β* = 1.31, *SE* = 2.187, *z* = 0.599, *p* = 0.549


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.03, *p* = 0.140, η²_G = 0.176
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.01 | 7 | = 0.463 | 0.49 [-0.51, 0.64] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.02 | 7 | = 0.983 | -0.01 [-0.76, 0.40] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 2.91 | 7 | = 0.137 | 1.19 [0.18, 1.84] | large | n.s. |
| 3 to 5 vs 4 to 5 | -0.92 | 7 | = 0.463 | -0.41 [-0.70, 0.58] | small | n.s. |
| 3 to 5 vs 6 to 5 | 1.14 | 7 | = 0.463 | 0.71 [-0.36, 1.02] | medium | n.s. |
| 4 to 5 vs 6 to 5 | 2.00 | 7 | = 0.257 | 0.97 [-0.28, 1.23] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 289.79, BIC = 302.75
- Condition effect: *β* = 0.24, *SE* = 0.641, *z* = 0.369, *p* = 0.712

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 9.24, *p* < .001, η²_G = 0.346
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -2.70 | 7 | = 0.046 | -0.46 [-1.28, -0.01] | small | * |
| 2 to 5 vs 4 to 5 | -4.88 | 7 | = 0.008 | -1.95 [-1.42, -0.10] | large | ** |
| 2 to 5 vs 6 to 5 | -2.79 | 7 | = 0.046 | -1.10 [-1.81, -0.17] | large | * |
| 3 to 5 vs 4 to 5 | -4.56 | 7 | = 0.008 | -1.80 [-1.31, 0.08] | large | ** |
| 3 to 5 vs 6 to 5 | -2.19 | 7 | = 0.077 | -0.84 [-1.83, -0.18] | large | n.s. |
| 4 to 5 vs 6 to 5 | 0.81 | 7 | = 0.442 | 0.30 [-0.42, 1.04] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 646.14, BIC = 659.09
- Condition effect: *β* = 11.84, *SE* = 10.996, *z* = 1.077, *p* = 0.282


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.016) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 5 showed smaller latency than 3 to 5 (*d* = -0.46)
  - 2 to 5 showed smaller latency than 4 to 5 (*d* = -1.95)
  - 2 to 5 showed smaller latency than 6 to 5 (*d* = -1.10)
  - 3 to 5 showed smaller latency than 4 to 5 (*d* = -1.80)

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
