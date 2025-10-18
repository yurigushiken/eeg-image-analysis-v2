# Statistical Analysis Report: landing_on_1_ACC1

**Generated:** 2025-10-18 13:05:50

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
| 1 to 1 | 16 | -2.62 µV | 2.41 | 0.60 | [-8.67, 0.02] |
| 2 to 1 | 17 | -3.15 µV | 2.20 | 0.53 | [-8.83, -0.14] |
| 3 to 1 | 21 | -3.02 µV | 2.47 | 0.54 | [-8.63, 0.02] |
| 4 to 1 | 20 | -2.39 µV | 1.60 | 0.36 | [-6.03, -0.22] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 16 | 180.55 ms | 10.69 | 2.67 | [161.47, 201.34] |
| 2 to 1 | 17 | 180.04 ms | 5.51 | 1.34 | [168.30, 188.16] |
| 3 to 1 | 21 | 181.25 ms | 7.69 | 1.68 | [165.34, 196.33] |
| 4 to 1 | 20 | 183.63 ms | 6.88 | 1.54 | [170.47, 194.25] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 18 | 3.11 µV | 2.65 | 0.63 | [0.42, 10.97] |
| 2 to 1 | 18 | 3.34 µV | 2.20 | 0.52 | [0.49, 6.86] |
| 3 to 1 | 20 | 2.21 µV | 1.38 | 0.31 | [0.14, 6.21] |
| 4 to 1 | 16 | 3.84 µV | 2.23 | 0.56 | [0.43, 9.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 18 | 122.88 ms | 9.09 | 2.14 | [105.02, 141.27] |
| 2 to 1 | 18 | 122.52 ms | 8.08 | 1.90 | [106.89, 136.60] |
| 3 to 1 | 20 | 121.95 ms | 9.37 | 2.09 | [102.25, 138.29] |
| 4 to 1 | 16 | 120.91 ms | 7.51 | 1.88 | [105.91, 131.80] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 10 | 1.76 µV | 1.47 | 0.46 | [0.01, 3.90] |
| 2 to 1 | 21 | 3.95 µV | 3.06 | 0.67 | [0.21, 10.01] |
| 3 to 1 | 20 | 4.30 µV | 2.56 | 0.57 | [0.84, 11.20] |
| 4 to 1 | 21 | 4.44 µV | 3.06 | 0.67 | [0.05, 9.35] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 10 | 470.35 ms | 22.58 | 7.14 | [432.68, 507.36] |
| 2 to 1 | 21 | 483.14 ms | 14.95 | 3.26 | [452.86, 520.57] |
| 3 to 1 | 20 | 478.82 ms | 9.61 | 2.15 | [463.98, 501.15] |
| 4 to 1 | 21 | 482.53 ms | 15.62 | 3.41 | [457.17, 526.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 268.03, BIC = 284.16
- **2 to 1 vs 1 to 1**: *β* = -0.87, *SE* = 0.400, *z* = -2.170, *p* = 0.030
- **3 to 1 vs 1 to 1**: *β* = -1.22, *SE* = 0.385, *z* = -3.167, *p* = 0.002
- **4 to 1 vs 1 to 1**: *β* = -0.35, *SE* = 0.385, *z* = -0.905, *p* = 0.366
- **Subject variance**: *β* = -0.48, *SE* = 0.050, *z* = -9.647, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.380, η²_G = 0.058
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 1.17 | 10 | = 0.499 | 0.43 [-0.31, 0.92] | small | n.s. |
| 1 to 1 vs 3 to 1 | 1.02 | 10 | = 0.499 | 0.41 [-0.33, 0.79] | small | n.s. |
| 1 to 1 vs 4 to 1 | -0.07 | 10 | = 0.949 | -0.03 [-0.54, 0.57] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | 0.11 | 10 | = 0.949 | 0.03 [-0.44, 0.63] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.95 | 10 | = 0.482 | -0.57 [-1.08, 0.09] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -1.33 | 10 | = 0.499 | -0.52 [-0.77, 0.21] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 511.32, BIC = 527.45
- **Effect 1**: *β* = -1.22, *SE* = 2.088, *z* = -0.585, *p* = 0.559
- **Effect 2**: *β* = 0.46, *SE* = 2.003, *z* = 0.228, *p* = 0.819
- **Effect 3**: *β* = 2.91, *SE* = 2.004, *z* = 1.453, *p* = 0.146
- **Effect 4**: *β* = 0.28, *SE* = 0.259, *z* = 1.094, *p* = 0.274

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.49, *p* = 0.689, η²_G = 0.021
- Greenhouse-Geisser corrected: *p* = 0.540 (ε = 0.428)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 0.61 | 10 | = 0.785 | 0.20 [-0.47, 0.75] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 0.32 | 10 | = 0.785 | 0.11 [-0.58, 0.53] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.28 | 10 | = 0.785 | -0.11 [-0.65, 0.46] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | -0.81 | 10 | = 0.785 | -0.13 [-0.91, 0.19] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.81 | 10 | = 0.301 | -0.45 [-1.20, -0.00] | small | n.s. |
| 3 to 1 vs 4 to 1 | -2.01 | 10 | = 0.301 | -0.35 [-0.92, 0.08] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 279.28, BIC = 295.22
- **Effect 1**: *β* = -0.09, *SE* = 0.462, *z* = -0.202, *p* = 0.840
- **Effect 2**: *β* = -0.62, *SE* = 0.446, *z* = -1.382, *p* = 0.167
- **Effect 3**: *β* = 0.38, *SE* = 0.482, *z* = 0.782, *p* = 0.434
- **Effect 4**: *β* = 0.45, *SE* = 0.072, *z* = 6.207, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.84, *p* = 0.050, η²_G = 0.086
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -0.08 | 13 | = 0.937 | -0.02 [-0.67, 0.37] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 1.61 | 13 | = 0.252 | 0.40 [-0.11, 0.92] | small | n.s. |
| 1 to 1 vs 4 to 1 | -1.32 | 13 | = 0.252 | -0.36 [-0.95, 0.24] | small | n.s. |
| 2 to 1 vs 3 to 1 | 1.45 | 13 | = 0.252 | 0.53 [-0.10, 0.94] | medium | n.s. |
| 2 to 1 vs 4 to 1 | -1.46 | 13 | = 0.252 | -0.41 [-0.95, 0.20] | small | n.s. |
| 3 to 1 vs 4 to 1 | -3.33 | 13 | = 0.032 | -1.03 [-1.26, -0.08] | large | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 508.22, BIC = 524.15
- **Effect 1**: *β* = 0.50, *SE* = 2.058, *z* = 0.243, *p* = 0.808
- **Effect 2**: *β* = 0.08, *SE* = 1.991, *z* = 0.042, *p* = 0.966
- **Effect 3**: *β* = 0.24, *SE* = 2.179, *z* = 0.110, *p* = 0.912
- **Effect 4**: *β* = -0.04, *SE* = 0.320, *z* = -0.114, *p* = 0.909

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.926, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -0.07 | 13 | = 0.948 | -0.02 [-0.59, 0.44] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 0.21 | 13 | = 0.948 | 0.08 [-0.52, 0.48] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.39 | 13 | = 0.948 | -0.14 [-0.68, 0.47] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | 0.31 | 13 | = 0.948 | 0.10 [-0.42, 0.57] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.42 | 13 | = 0.948 | -0.13 [-0.65, 0.46] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.69 | 13 | = 0.948 | -0.23 [-0.63, 0.44] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 335.51, BIC = 351.44
- **Effect 1**: *β* = 1.89, *SE* = 0.855, *z* = 2.210, *p* = 0.027
- **Effect 2**: *β* = 1.57, *SE* = 0.894, *z* = 1.755, *p* = 0.079
- **Effect 3**: *β* = 1.89, *SE* = 0.884, *z* = 2.140, *p* = 0.032
- **Effect 4**: *β* = 0.20, *SE* = 0.042, *z* = 4.736, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.93, *p* = 0.003, η²_G = 0.299
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -4.05 | 9 | = 0.009 | -1.64 [-2.24, -0.32] | large | ** |
| 1 to 1 vs 3 to 1 | -2.04 | 9 | = 0.143 | -1.12 [-1.43, 0.14] | large | n.s. |
| 1 to 1 vs 4 to 1 | -4.42 | 9 | = 0.009 | -1.65 [-2.40, -0.39] | large | ** |
| 2 to 1 vs 3 to 1 | 1.36 | 9 | = 0.247 | 0.51 [-0.52, 0.45] | medium | n.s. |
| 2 to 1 vs 4 to 1 | -0.37 | 9 | = 0.720 | -0.15 [-0.63, 0.31] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.52 | 9 | = 0.245 | -0.63 [-0.55, 0.41] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 604.80, BIC = 620.74
- **Effect 1**: *β* = 12.51, *SE* = 5.473, *z* = 2.287, *p* = 0.022
- **Effect 2**: *β* = 8.45, *SE* = 5.684, *z* = 1.487, *p* = 0.137
- **Effect 3**: *β* = 12.41, *SE* = 5.588, *z* = 2.220, *p* = 0.026
- **Effect 4**: *β* = -0.05, *SE* = 0.262, *z* = -0.199, *p* = 0.843

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.63, *p* = 0.205, η²_G = 0.100
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -1.51 | 9 | = 0.493 | -0.62 [-1.23, 0.28] | medium | n.s. |
| 1 to 1 vs 3 to 1 | -1.13 | 9 | = 0.579 | -0.48 [-1.09, 0.38] | small | n.s. |
| 1 to 1 vs 4 to 1 | -1.70 | 9 | = 0.493 | -0.63 [-1.30, 0.23] | medium | n.s. |
| 2 to 1 vs 3 to 1 | 0.82 | 9 | = 0.620 | 0.26 [0.00, 1.03] | small | n.s. |
| 2 to 1 vs 4 to 1 | -0.26 | 9 | = 0.799 | -0.11 [-0.55, 0.39] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.67 | 9 | = 0.620 | -0.30 [-0.71, 0.27] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.050)
**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 1 to 1 showed smaller amplitude than 2 to 1 (*d* = -1.64)
  - 1 to 1 showed smaller amplitude than 4 to 1 (*d* = -1.65)

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
