# Statistical Analysis Report: tables

**Generated:** 2025-10-17 04:46:38

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

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 240.23, BIC = 253.36
- Effect 1 effect: *β* = -0.43, *SE* = 0.356, *z* = -1.223, *p* = 0.221
- Effect 2 effect: *β* = -0.89, *SE* = 0.359, *z* = -2.492, *p* = 0.013
- Effect 3 effect: *β* = -0.38, *SE* = 0.067, *z* = -5.640, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.46, *p* = 0.100, η²_G = 0.045
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.48 | 18 | = 0.070 | 0.55 [0.10, 1.09] | medium | n.s. |
| 1 to 2 vs 1 to 4 | 1.92 | 18 | = 0.106 | 0.41 [-0.06, 0.95] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.13 | 18 | = 0.900 | -0.03 [-0.47, 0.44] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 503.19, BIC = 516.32
- Effect 1 effect: *β* = 0.84, *SE* = 2.294, *z* = 0.366, *p* = 0.714
- Effect 2 effect: *β* = 1.07, *SE* = 2.300, *z* = 0.467, *p* = 0.640
- Effect 3 effect: *β* = -0.17, *SE* = 0.467, *z* = -0.373, *p* = 0.709

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.36, *p* = 0.702, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.51 | 18 | = 0.784 | 0.12 [-0.46, 0.45] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.28 | 18 | = 0.784 | -0.04 [-0.55, 0.42] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -0.84 | 18 | = 0.784 | -0.18 [-0.62, 0.29] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 85.62, BIC = 94.95
- Effect 1 effect: *β* = 0.17, *SE* = 0.323, *z* = 0.535, *p* = 0.593
- Effect 2 effect: *β* = 0.25, *SE* = 0.290, *z* = 0.850, *p* = 0.395
- Effect 3 effect: *β* = 0.51, *SE* = 0.080, *z* = 6.387, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.60, *p* = 0.580, η²_G = 0.151
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.49 | 3 | = 0.664 | 0.47 [-0.78, 1.36] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.58 | 3 | = 0.636 | 1.03 [-0.59, 2.32] | large | n.s. |
| 1 to 3 vs 1 to 4 | 0.48 | 3 | = 0.664 | 0.38 [-1.08, 0.62] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 245.05, BIC = 254.39
- Effect 1 effect: *β* = -0.43, *SE* = 3.107, *z* = -0.138, *p* = 0.890
- Effect 2 effect: *β* = 0.68, *SE* = 2.800, *z* = 0.243, *p* = 0.808
- Effect 3 effect: *β* = 0.15, *SE* = 0.788, *z* = 0.193, *p* = 0.847

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.88, *p* = 0.232, η²_G = 0.163
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 1.08 | 3 | = 0.529 | 0.57 [-0.42, 1.97] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -0.71 | 3 | = 0.529 | -0.42 [-1.96, 0.74] | small | n.s. |
| 1 to 3 vs 1 to 4 | -2.04 | 3 | = 0.403 | -0.79 [-0.85, 0.83] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 216.62, BIC = 228.55
- Effect 1 effect: *β* = 0.16, *SE* = 0.440, *z* = 0.372, *p* = 0.710
- Effect 2 effect: *β* = 0.16, *SE* = 0.427, *z* = 0.366, *p* = 0.714
- Effect 3 effect: *β* = 0.56, *SE* = 0.094, *z* = 5.958, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.03, *p* = 0.372, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.08 | 13 | = 0.447 | -0.25 [-0.88, 0.30] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.27 | 13 | = 0.447 | -0.27 [-0.90, 0.24] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.03 | 13 | = 0.978 | 0.00 [-0.38, 0.58] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 518.28, BIC = 530.21
- Effect 1 effect: *β* = 12.68, *SE* = 9.173, *z* = 1.382, *p* = 0.167
- Effect 2 effect: *β* = 6.66, *SE* = 9.041, *z* = 0.737, *p* = 0.461
- Effect 3 effect: *β* = 0.27, *SE* = 1.300, *z* = 0.205, *p* = 0.838

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.93, *p* = 0.408, η²_G = 0.049
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.22 | 13 | = 0.543 | -0.46 [-0.92, 0.27] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.95 | 13 | = 0.543 | -0.45 [-0.67, 0.44] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.08 | 13 | = 0.938 | 0.02 [-0.37, 0.60] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


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
