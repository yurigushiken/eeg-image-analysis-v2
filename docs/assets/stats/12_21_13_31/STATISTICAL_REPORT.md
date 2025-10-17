# Statistical Analysis Report: tables

**Generated:** 2025-10-17 03:06:51

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
| Decreasing 2 to 1 | 16 | -2.47 µV | 2.16 | 0.54 | [-8.27, -0.09] |
| Decreasing 3 to 1 | 20 | -2.47 µV | 2.11 | 0.47 | [-7.74, 0.11] |
| Increasing 1 to 2 | 22 | -3.26 µV | 1.89 | 0.40 | [-7.76, -0.22] |
| Increasing 1 to 3 | 24 | -4.26 µV | 1.80 | 0.37 | [-8.92, -1.26] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 16 | 181.46 ms | 11.08 | 2.77 | [160.92, 206.99] |
| Decreasing 3 to 1 | 20 | 183.12 ms | 12.54 | 2.80 | [161.45, 205.19] |
| Increasing 1 to 2 | 22 | 177.48 ms | 13.20 | 2.81 | [157.81, 210.54] |
| Increasing 1 to 3 | 24 | 177.42 ms | 9.18 | 1.87 | [158.09, 199.77] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 19 | 3.12 µV | 2.31 | 0.53 | [0.06, 8.71] |
| Decreasing 3 to 1 | 21 | 2.17 µV | 1.55 | 0.34 | [0.33, 6.79] |
| Increasing 1 to 2 | 12 | 1.05 µV | 1.18 | 0.34 | [-0.02, 4.35] |
| Increasing 1 to 3 | 11 | 1.85 µV | 1.31 | 0.39 | [0.73, 4.50] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 19 | 114.49 ms | 5.56 | 1.27 | [104.92, 127.97] |
| Decreasing 3 to 1 | 21 | 114.97 ms | 6.12 | 1.34 | [104.42, 125.67] |
| Increasing 1 to 2 | 12 | 112.55 ms | 8.31 | 2.40 | [99.41, 124.39] |
| Increasing 1 to 3 | 11 | 110.55 ms | 4.43 | 1.34 | [105.26, 116.98] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 3.59 µV | 2.60 | 0.58 | [-0.05, 9.68] |
| Decreasing 3 to 1 | 20 | 3.89 µV | 2.33 | 0.52 | [0.32, 9.09] |
| Increasing 1 to 2 | 17 | 3.43 µV | 2.83 | 0.69 | [0.14, 10.35] |
| Increasing 1 to 3 | 20 | 4.11 µV | 3.41 | 0.76 | [-0.00, 13.08] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 483.86 ms | 16.69 | 3.73 | [448.34, 521.68] |
| Decreasing 3 to 1 | 20 | 479.27 ms | 13.67 | 3.06 | [458.78, 511.87] |
| Increasing 1 to 2 | 17 | 484.35 ms | 21.56 | 5.23 | [450.09, 533.53] |
| Increasing 1 to 3 | 20 | 476.54 ms | 16.49 | 3.69 | [420.55, 497.20] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 271.50, BIC = 288.35
- Effect 1 effect: *β* = -0.22, *SE* = 0.325, *z* = -0.680, *p* = 0.497
- Effect 2 effect: *β* = -0.49, *SE* = 0.333, *z* = -1.487, *p* = 0.137
- Effect 3 effect: *β* = -0.90, *SE* = 0.353, *z* = -2.561, *p* = 0.010
- Effect 4 effect: *β* = -0.39, *SE* = 0.048, *z* = -8.162, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.54, *p* < .001, η²_G = 0.159
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.33 | 14 | = 0.744 | 0.08 [-0.47, 0.64] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.76 | 14 | = 0.028 | 0.64 [0.09, 1.33] | medium | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 5.49 | 14 | < .001 | 1.05 [0.67, 2.18] | large | *** |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.94 | 14 | = 0.087 | 0.54 [-0.00, 0.99] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 4.40 | 14 | = 0.002 | 0.93 [0.48, 1.65] | large | ** |
| Increasing 1 to 2 vs Increasing 1 to 3 | 2.66 | 14 | = 0.028 | 0.45 [0.08, 1.03] | small | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 600.72, BIC = 617.57
- Effect 1 effect: *β* = 1.28, *SE* = 2.221, *z* = 0.575, *p* = 0.565
- Effect 2 effect: *β* = -3.36, *SE* = 2.263, *z* = -1.487, *p* = 0.137
- Effect 3 effect: *β* = -2.38, *SE* = 2.392, *z* = -0.995, *p* = 0.320
- Effect 4 effect: *β* = -0.56, *SE* = 0.321, *z* = -1.729, *p* = 0.084

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.38, *p* = 0.027, η²_G = 0.046
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.09 | 14 | = 0.929 | -0.02 [-0.58, 0.53] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 3.09 | 14 | = 0.048 | 0.44 [0.16, 1.43] | small | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 1.86 | 14 | = 0.127 | 0.40 [-0.15, 0.96] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.05 | 14 | = 0.120 | 0.44 [0.04, 1.04] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.19 | 14 | = 0.120 | 0.40 [0.11, 1.13] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.41 | 14 | = 0.827 | -0.08 [-0.44, 0.45] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 209.73, BIC = 224.73
- Effect 1 effect: *β* = -0.51, *SE* = 0.352, *z* = -1.446, *p* = 0.148
- Effect 2 effect: *β* = -1.11, *SE* = 0.432, *z* = -2.566, *p* = 0.010
- Effect 3 effect: *β* = -0.66, *SE* = 0.434, *z* = -1.524, *p* = 0.127
- Effect 4 effect: *β* = 0.48, *SE* = 0.064, *z* = 7.484, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.00, *p* = 0.024, η²_G = 0.257
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 1.22 | 6 | = 0.348 | 0.48 [-0.07, 1.01] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.61 | 6 | = 0.106 | 1.29 [0.21, 2.03] | large | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.80 | 6 | = 0.106 | 0.95 [0.01, 1.68] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.41 | 6 | = 0.106 | 1.02 [-0.00, 1.52] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.16 | 6 | = 0.348 | 0.57 [-0.27, 1.14] | medium | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.86 | 6 | = 0.421 | -0.53 [-1.20, 0.52] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 417.71, BIC = 432.71
- Effect 1 effect: *β* = 0.33, *SE* = 1.871, *z* = 0.176, *p* = 0.860
- Effect 2 effect: *β* = -2.37, *SE* = 2.255, *z* = -1.050, *p* = 0.294
- Effect 3 effect: *β* = -4.30, *SE* = 2.260, *z* = -1.904, *p* = 0.057
- Effect 4 effect: *β* = -0.19, *SE* = 0.321, *z* = -0.591, *p* = 0.554

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.67, *p* = 0.210, η²_G = 0.177
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.69 | 6 | = 0.622 | -0.48 [-0.72, 0.32] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.51 | 6 | = 0.626 | 0.31 [-0.39, 1.09] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.12 | 6 | = 0.235 | 0.97 [-0.32, 1.18] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.27 | 6 | = 0.500 | 0.63 [-0.30, 1.10] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.27 | 6 | = 0.235 | 1.46 [-0.01, 1.51] | large | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.84 | 6 | = 0.622 | 0.36 [-0.40, 1.37] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 350.34, BIC = 366.75
- Effect 1 effect: *β* = -0.54, *SE* = 0.613, *z* = -0.883, *p* = 0.377
- Effect 2 effect: *β* = -0.28, *SE* = 0.617, *z* = -0.449, *p* = 0.653
- Effect 3 effect: *β* = 0.32, *SE* = 0.601, *z* = 0.538, *p* = 0.590
- Effect 4 effect: *β* = 0.28, *SE* = 0.051, *z* = 5.407, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.65, *p* = 0.587, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.09 | 14 | = 0.928 | -0.03 [-0.58, 0.42] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.60 | 14 | = 0.672 | 0.20 [-0.41, 0.62] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | -0.66 | 14 | = 0.672 | -0.22 [-0.70, 0.34] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 0.65 | 14 | = 0.672 | 0.23 [-0.35, 0.73] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.66 | 14 | = 0.672 | -0.20 [-0.64, 0.36] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.73 | 14 | = 0.636 | -0.38 [-0.99, 0.12] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 660.89, BIC = 677.30
- Effect 1 effect: *β* = -4.35, *SE* = 4.787, *z* = -0.908, *p* = 0.364
- Effect 2 effect: *β* = 1.11, *SE* = 4.839, *z* = 0.229, *p* = 0.819
- Effect 3 effect: *β* = -6.70, *SE* = 4.686, *z* = -1.430, *p* = 0.153
- Effect 4 effect: *β* = -0.18, *SE* = 0.386, *z* = -0.463, *p* = 0.643

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.52, *p* = 0.670, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.92 | 14 | = 0.742 | 0.22 [-0.06, 0.98] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | -0.22 | 14 | = 0.832 | -0.08 [-0.63, 0.40] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 1.10 | 14 | = 0.742 | 0.31 [-0.29, 0.75] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | -0.61 | 14 | = 0.804 | -0.22 [-0.73, 0.34] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 0.44 | 14 | = 0.804 | 0.11 [-0.35, 0.65] | negligible | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.98 | 14 | = 0.742 | 0.30 [-0.21, 0.89] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 0.64)
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 1.05)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 0.93)
  - Increasing 1 to 2 showed greater amplitude than Increasing 1 to 3 (*d* = 0.45)
**N1 latency:** Significant main effect of condition (*p* = 0.027). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.44)
**P1 amplitude:** Significant main effect of condition (*p* = 0.024) (no significant pairwise comparisons)

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

Linear mixed-effects models (LMM) with random intercepts for subjects were used as the primary analysis, as they optimally handle missing data via maximum likelihood estimation (Baayen et al., 2008). 
For comparison with traditional approaches, repeated-measures ANOVA and pairwise t-tests were also performed on complete cases; however, power was substantially reduced by listwise deletion. Therefore, LMM results are emphasized in interpretation.

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.11
- MNE-Python 1.10.1
- Statsmodels 0.14.5
- Pingouin 0.5.5

### References

- Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects modeling with crossed random effects for subjects and items. *Journal of Memory and Language, 59*(4), 390-412.
- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
