# Statistical Analysis Report: tables

**Generated:** 2025-10-17 03:13:43

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
| 1 to 3 | 24 | -3.84 µV | 1.90 | 0.39 | [-8.57, -0.57] |
| 2 to 4 | 22 | -3.85 µV | 2.26 | 0.48 | [-10.63, -0.11] |
| 3 to 5 | 22 | -3.61 µV | 2.30 | 0.49 | [-10.14, -0.59] |
| 4 to 6 | 22 | -4.35 µV | 2.79 | 0.59 | [-12.58, 0.01] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 173.16 ms | 12.10 | 2.47 | [150.22, 202.92] |
| 2 to 4 | 22 | 172.28 ms | 11.72 | 2.50 | [150.36, 207.84] |
| 3 to 5 | 22 | 168.27 ms | 11.53 | 2.46 | [148.43, 196.84] |
| 4 to 6 | 22 | 172.61 ms | 12.07 | 2.57 | [150.60, 206.91] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 12 | 1.47 µV | 1.16 | 0.33 | [0.03, 4.24] |
| 2 to 4 | 16 | 1.43 µV | 1.05 | 0.26 | [-0.04, 3.73] |
| 3 to 5 | 13 | 1.41 µV | 1.10 | 0.30 | [0.16, 3.88] |
| 4 to 6 | 15 | 1.68 µV | 1.34 | 0.34 | [-0.01, 3.91] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 12 | 92.93 ms | 10.86 | 3.14 | [78.55, 107.87] |
| 2 to 4 | 16 | 88.25 ms | 10.97 | 2.74 | [69.59, 104.95] |
| 3 to 5 | 13 | 87.54 ms | 10.99 | 3.05 | [71.31, 104.71] |
| 4 to 6 | 15 | 90.80 ms | 11.54 | 2.98 | [68.35, 106.31] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 4.24 µV | 3.46 | 0.77 | [0.56, 12.22] |
| 2 to 4 | 19 | 4.57 µV | 3.50 | 0.80 | [0.50, 11.96] |
| 3 to 5 | 16 | 3.64 µV | 2.20 | 0.55 | [0.18, 8.05] |
| 4 to 6 | 18 | 3.77 µV | 2.42 | 0.57 | [0.34, 7.73] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 461.35 ms | 20.62 | 4.61 | [404.70, 487.79] |
| 2 to 4 | 19 | 470.87 ms | 28.77 | 6.60 | [408.76, 516.90] |
| 3 to 5 | 16 | 461.97 ms | 23.02 | 5.76 | [405.85, 499.34] |
| 4 to 6 | 18 | 469.16 ms | 26.21 | 6.18 | [414.21, 522.82] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 337.89, BIC = 355.39
- Effect 1 effect: *β* = -0.23, *SE* = 0.358, *z* = -0.632, *p* = 0.527
- Effect 2 effect: *β* = 0.09, *SE* = 0.358, *z* = 0.258, *p* = 0.797
- Effect 3 effect: *β* = -0.39, *SE* = 0.356, *z* = -1.085, *p* = 0.278
- Effect 4 effect: *β* = -0.52, *SE* = 0.056, *z* = -9.236, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.535, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.38 | 18 | = 0.757 | -0.11 [-0.54, 0.34] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.79 | 18 | = 0.757 | -0.21 [-0.67, 0.22] | small | n.s. |
| 1 to 3 vs 4 to 6 | 0.66 | 18 | = 0.757 | 0.16 [-0.21, 0.69] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -0.31 | 18 | = 0.757 | -0.08 [-0.51, 0.40] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 0.93 | 18 | = 0.757 | 0.23 [-0.35, 0.59] | small | n.s. |
| 3 to 5 vs 4 to 6 | 2.28 | 18 | = 0.210 | 0.30 [0.08, 1.09] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 666.13, BIC = 683.62
- Effect 1 effect: *β* = -0.20, *SE* = 2.047, *z* = -0.098, *p* = 0.922
- Effect 2 effect: *β* = -3.55, *SE* = 2.047, *z* = -1.733, *p* = 0.083
- Effect 3 effect: *β* = -1.30, *SE* = 2.033, *z* = -0.642, *p* = 0.521
- Effect 4 effect: *β* = -0.36, *SE* = 0.336, *z* = -1.084, *p* = 0.278

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.468, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.90 | 18 | = 0.762 | -0.23 [-0.51, 0.38] | small | n.s. |
| 1 to 3 vs 3 to 5 | 0.42 | 18 | = 0.819 | 0.09 [-0.18, 0.72] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.03 | 18 | = 0.977 | -0.00 [-0.32, 0.57] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.42 | 18 | = 0.762 | 0.29 [-0.07, 0.88] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.09 | 18 | = 0.762 | 0.22 [-0.37, 0.57] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.48 | 18 | = 0.819 | -0.09 [-0.54, 0.40] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 119.95, BIC = 134.13
- Effect 1 effect: *β* = -0.24, *SE* = 0.217, *z* = -1.121, *p* = 0.262
- Effect 2 effect: *β* = -0.28, *SE* = 0.234, *z* = -1.194, *p* = 0.232
- Effect 3 effect: *β* = 0.23, *SE* = 0.217, *z* = 1.085, *p* = 0.278
- Effect 4 effect: *β* = 1.04, *SE* = 0.096, *z* = 10.867, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 435.34, BIC = 449.52
- Effect 1 effect: *β* = -4.60, *SE* = 3.709, *z* = -1.239, *p* = 0.215
- Effect 2 effect: *β* = -5.54, *SE* = 3.930, *z* = -1.411, *p* = 0.158
- Effect 3 effect: *β* = -1.95, *SE* = 3.706, *z* = -0.526, *p* = 0.599
- Effect 4 effect: *β* = 0.82, *SE* = 1.616, *z* = 0.506, *p* = 0.613

_Note: LMM uses all available subject data via maximum likelihood estimation._

_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 290.66, BIC = 306.69
- Effect 1 effect: *β* = 0.01, *SE* = 0.421, *z* = 0.024, *p* = 0.980
- Effect 2 effect: *β* = 0.08, *SE* = 0.457, *z* = 0.171, *p* = 0.865
- Effect 3 effect: *β* = -0.29, *SE* = 0.425, *z* = -0.677, *p* = 0.498
- Effect 4 effect: *β* = 0.63, *SE* = 0.061, *z* = 10.333, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.19, *p* = 0.327, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.27 | 14 | = 0.791 | -0.07 [-0.53, 0.46] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | 1.21 | 14 | = 0.474 | 0.38 [-0.19, 0.91] | small | n.s. |
| 1 to 3 vs 4 to 6 | 0.75 | 14 | = 0.561 | 0.21 [-0.30, 0.71] | small | n.s. |
| 2 to 4 vs 3 to 5 | 1.84 | 14 | = 0.474 | 0.47 [-0.06, 1.07] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.13 | 14 | = 0.474 | 0.30 [-0.24, 0.81] | small | n.s. |
| 3 to 5 vs 4 to 6 | -1.04 | 14 | = 0.474 | -0.23 [-0.83, 0.30] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 685.77, BIC = 701.81
- Effect 1 effect: *β* = 9.75, *SE* = 7.733, *z* = 1.261, *p* = 0.207
- Effect 2 effect: *β* = -0.10, *SE* = 8.210, *z* = -0.012, *p* = 0.991
- Effect 3 effect: *β* = 7.62, *SE* = 7.839, *z* = 0.972, *p* = 0.331
- Effect 4 effect: *β* = -0.53, *SE* = 0.953, *z* = -0.561, *p* = 0.575

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.96, *p* = 0.421, η²_G = 0.047
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.84 | 14 | = 0.522 | -0.60 [-0.80, 0.21] | medium | n.s. |
| 1 to 3 vs 3 to 5 | -0.82 | 14 | = 0.577 | -0.29 [-0.68, 0.39] | small | n.s. |
| 1 to 3 vs 4 to 6 | -0.94 | 14 | = 0.577 | -0.35 [-0.76, 0.25] | small | n.s. |
| 2 to 4 vs 3 to 5 | 0.72 | 14 | = 0.577 | 0.32 [-0.28, 0.80] | small | n.s. |
| 2 to 4 vs 4 to 6 | 0.78 | 14 | = 0.577 | 0.25 [-0.57, 0.46] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.22 | 14 | = 0.830 | -0.07 [-0.61, 0.50] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


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
