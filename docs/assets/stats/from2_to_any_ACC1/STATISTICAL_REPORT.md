# Statistical Analysis Report: tables

**Generated:** 2025-10-17 03:11:13

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
| 2 to 1 | 16 | -2.74 µV | 2.07 | 0.52 | [-8.34, 0.05] |
| 2 to 3 | 21 | -3.47 µV | 1.32 | 0.29 | [-5.73, -1.07] |
| 2 to 4 | 21 | -4.22 µV | 2.10 | 0.46 | [-10.62, -1.29] |
| 2 to 5 | 24 | -4.05 µV | 2.34 | 0.48 | [-10.98, -0.32] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 178.70 ms | 7.82 | 1.95 | [160.73, 188.13] |
| 2 to 3 | 21 | 173.17 ms | 7.96 | 1.74 | [156.98, 192.27] |
| 2 to 4 | 21 | 172.61 ms | 7.51 | 1.64 | [153.73, 184.40] |
| 2 to 5 | 24 | 176.24 ms | 10.81 | 2.21 | [155.10, 199.23] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 3.13 µV | 2.38 | 0.58 | [0.68, 7.96] |
| 2 to 3 | 13 | 1.91 µV | 1.22 | 0.34 | [0.18, 4.26] |
| 2 to 4 | 15 | 1.84 µV | 1.39 | 0.36 | [-0.09, 5.23] |
| 2 to 5 | 12 | 1.65 µV | 2.31 | 0.67 | [0.01, 8.46] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 109.94 ms | 4.81 | 1.17 | [101.46, 118.17] |
| 2 to 3 | 13 | 108.31 ms | 7.51 | 2.08 | [98.69, 121.48] |
| 2 to 4 | 15 | 107.64 ms | 8.67 | 2.24 | [90.58, 123.94] |
| 2 to 5 | 12 | 106.17 ms | 8.11 | 2.34 | [94.22, 121.64] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 3.71 µV | 2.80 | 0.63 | [0.39, 9.47] |
| 2 to 3 | 18 | 4.07 µV | 2.76 | 0.65 | [0.33, 9.59] |
| 2 to 4 | 19 | 4.58 µV | 3.61 | 0.83 | [0.15, 12.25] |
| 2 to 5 | 22 | 3.27 µV | 2.06 | 0.44 | [0.08, 7.61] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 475.60 ms | 15.73 | 3.52 | [451.93, 511.64] |
| 2 to 3 | 18 | 457.77 ms | 16.07 | 3.79 | [414.52, 482.43] |
| 2 to 4 | 19 | 472.42 ms | 26.08 | 5.98 | [415.60, 525.75] |
| 2 to 5 | 22 | 460.80 ms | 23.15 | 4.93 | [401.27, 500.13] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.44, BIC = 332.29
- Effect 1 effect: *β* = -0.32, *SE* = 0.460, *z* = -0.693, *p* = 0.488
- Effect 2 effect: *β* = -0.74, *SE* = 0.469, *z* = -1.589, *p* = 0.112
- Effect 3 effect: *β* = -1.00, *SE* = 0.449, *z* = -2.230, *p* = 0.026
- Effect 4 effect: *β* = -0.50, *SE* = 0.071, *z* = -6.982, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.03, *p* = 0.041, η²_G = 0.125
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.07 | 13 | = 0.118 | 0.70 [-0.15, 1.01] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 2.25 | 13 | = 0.118 | 0.78 [0.00, 1.21] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 3.17 | 13 | = 0.044 | 0.89 [-0.02, 1.12] | large | * |
| 2 to 3 vs 2 to 4 | 0.70 | 13 | = 0.596 | 0.27 [-0.20, 0.75] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.04 | 13 | = 0.476 | 0.39 [-0.09, 0.85] | small | n.s. |
| 2 to 4 vs 2 to 5 | 0.30 | 13 | = 0.767 | 0.10 [-0.39, 0.52] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 566.35, BIC = 583.20
- Effect 1 effect: *β* = -3.59, *SE* = 1.846, *z* = -1.943, *p* = 0.052
- Effect 2 effect: *β* = -3.85, *SE* = 1.886, *z* = -2.043, *p* = 0.041
- Effect 3 effect: *β* = -1.63, *SE* = 1.807, *z* = -0.902, *p* = 0.367
- Effect 4 effect: *β* = -0.55, *SE* = 0.308, *z* = -1.786, *p* = 0.074

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.02, *p* = 0.041, η²_G = 0.070
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.57 | 13 | = 0.140 | 0.71 [-0.02, 1.18] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 1.99 | 13 | = 0.203 | 0.62 [-0.04, 1.15] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 1.27 | 13 | = 0.272 | 0.30 [-0.34, 0.73] | small | n.s. |
| 2 to 3 vs 2 to 4 | -0.13 | 13 | = 0.896 | -0.03 [-0.45, 0.48] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | -1.61 | 13 | = 0.229 | -0.34 [-0.59, 0.32] | small | n.s. |
| 2 to 4 vs 2 to 5 | -1.52 | 13 | = 0.229 | -0.29 [-0.76, 0.17] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 203.73, BIC = 218.04
- Effect 1 effect: *β* = -0.18, *SE* = 0.523, *z* = -0.345, *p* = 0.730
- Effect 2 effect: *β* = -0.43, *SE* = 0.492, *z* = -0.870, *p* = 0.384
- Effect 3 effect: *β* = -0.13, *SE* = 0.558, *z* = -0.236, *p* = 0.813
- Effect 4 effect: *β* = 0.63, *SE* = 0.104, *z* = 6.085, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 13.90, *p* < .001, η²_G = 0.680
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 4.26 | 4 | = 0.027 | 3.51 [-0.09, 1.51] | large | * |
| 2 to 1 vs 2 to 4 | 4.24 | 4 | = 0.027 | 1.79 [-0.04, 1.76] | large | * |
| 2 to 1 vs 2 to 5 | 12.22 | 4 | = 0.002 | 4.48 [0.08, 1.80] | large | ** |
| 2 to 3 vs 2 to 4 | -0.60 | 4 | = 0.583 | -0.44 [-1.10, 0.76] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.76 | 4 | = 0.183 | 1.15 [-0.68, 0.86] | large | n.s. |
| 2 to 4 vs 2 to 5 | 2.72 | 4 | = 0.080 | 1.13 [-0.12, 1.63] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 398.16, BIC = 412.47
- Effect 1 effect: *β* = -1.74, *SE* = 2.826, *z* = -0.616, *p* = 0.538
- Effect 2 effect: *β* = -2.38, *SE* = 2.593, *z* = -0.920, *p* = 0.358
- Effect 3 effect: *β* = -3.90, *SE* = 2.910, *z* = -1.341, *p* = 0.180
- Effect 4 effect: *β* = -0.06, *SE* = 0.444, *z* = -0.139, *p* = 0.889

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.33, *p* = 0.126, η²_G = 0.308
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.61 | 4 | = 0.265 | 1.53 [0.17, 1.97] | large | n.s. |
| 2 to 1 vs 2 to 4 | -1.12 | 4 | = 0.407 | -0.66 [-0.65, 0.89] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 0.53 | 4 | = 0.625 | 0.33 [-0.23, 1.30] | small | n.s. |
| 2 to 3 vs 2 to 4 | -2.24 | 4 | = 0.265 | -1.42 [-1.11, 0.76] | large | n.s. |
| 2 to 3 vs 2 to 5 | -1.08 | 4 | = 0.407 | -0.75 [-0.96, 0.59] | medium | n.s. |
| 2 to 4 vs 2 to 5 | 1.11 | 4 | = 0.407 | 0.73 [-0.27, 1.38] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 325.55, BIC = 342.14
- Effect 1 effect: *β* = -0.27, *SE* = 0.484, *z* = -0.563, *p* = 0.573
- Effect 2 effect: *β* = 0.11, *SE* = 0.474, *z* = 0.228, *p* = 0.820
- Effect 3 effect: *β* = -0.19, *SE* = 0.451, *z* = -0.419, *p* = 0.675
- Effect 4 effect: *β* = 0.59, *SE* = 0.059, *z* = 10.025, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.72, *p* = 0.545, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | -0.01 | 15 | = 0.988 | -0.00 [-0.54, 0.53] | negligible | n.s. |
| 2 to 1 vs 2 to 4 | -0.64 | 15 | = 0.635 | -0.22 [-0.69, 0.31] | small | n.s. |
| 2 to 1 vs 2 to 5 | 0.77 | 15 | = 0.635 | 0.23 [-0.36, 0.58] | small | n.s. |
| 2 to 3 vs 2 to 4 | -0.83 | 15 | = 0.635 | -0.21 [-0.73, 0.31] | small | n.s. |
| 2 to 3 vs 2 to 5 | 0.85 | 15 | = 0.635 | 0.23 [-0.35, 0.68] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.35 | 15 | = 0.635 | 0.43 [-0.22, 0.76] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 710.91, BIC = 727.49
- Effect 1 effect: *β* = -15.33, *SE* = 6.096, *z* = -2.515, *p* = 0.012
- Effect 2 effect: *β* = -1.40, *SE* = 5.945, *z* = -0.235, *p* = 0.814
- Effect 3 effect: *β* = -14.65, *SE* = 5.625, *z* = -2.605, *p* = 0.009
- Effect 4 effect: *β* = -0.13, *SE* = 0.702, *z* = -0.180, *p* = 0.857

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.49, *p* = 0.023, η²_G = 0.138
- Greenhouse-Geisser corrected: *p* = 0.050 (ε = 0.594)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.85 | 15 | = 0.069 | 0.86 [0.12, 1.31] | large | n.s. |
| 2 to 1 vs 2 to 4 | 0.16 | 15 | = 0.876 | 0.04 [-0.58, 0.42] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | 2.53 | 15 | = 0.069 | 0.90 [0.14, 1.17] | large | n.s. |
| 2 to 3 vs 2 to 4 | -1.68 | 15 | = 0.171 | -0.64 [-0.89, 0.17] | medium | n.s. |
| 2 to 3 vs 2 to 5 | 0.58 | 15 | = 0.688 | 0.15 [-0.36, 0.67] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.77 | 15 | = 0.171 | 0.72 [-0.03, 0.99] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.041). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 0.89)
**N1 latency:** Significant main effect of condition (*p* = 0.041) (no significant pairwise comparisons)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 3 (*d* = 3.51)
  - 2 to 1 showed greater amplitude than 2 to 4 (*d* = 1.79)
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 4.48)
**P3b latency:** Significant main effect of condition (*p* = 0.023) (no significant pairwise comparisons)

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
