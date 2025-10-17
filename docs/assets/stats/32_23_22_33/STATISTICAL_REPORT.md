# Statistical Analysis Report: tables

**Generated:** 2025-10-17 04:43:53

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
| Cardinality2 | 22 | -3.11 µV | 1.83 | 0.39 | [-7.37, -0.14] |
| Cardinality3 | 22 | -3.22 µV | 1.65 | 0.35 | [-7.54, -0.94] |
| Decreasing 3 to 2 | 24 | -3.66 µV | 2.11 | 0.43 | [-7.98, -0.23] |
| Increasing 2 to 3 | 22 | -3.28 µV | 1.41 | 0.30 | [-5.74, -0.32] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 22 | 173.03 ms | 13.87 | 2.96 | [147.33, 195.55] |
| Cardinality3 | 22 | 172.31 ms | 10.44 | 2.23 | [151.69, 197.41] |
| Decreasing 3 to 2 | 24 | 174.19 ms | 11.00 | 2.25 | [158.22, 206.45] |
| Increasing 2 to 3 | 22 | 171.96 ms | 7.69 | 1.64 | [154.28, 186.90] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 13 | 2.01 µV | 1.83 | 0.51 | [0.25, 6.70] |
| Cardinality3 | 15 | 2.14 µV | 2.15 | 0.55 | [0.03, 7.32] |
| Decreasing 3 to 2 | 11 | 1.80 µV | 1.41 | 0.43 | [0.01, 4.07] |
| Increasing 2 to 3 | 14 | 1.80 µV | 1.36 | 0.36 | [-0.04, 4.27] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 13 | 111.24 ms | 4.00 | 1.11 | [104.71, 119.13] |
| Cardinality3 | 15 | 110.45 ms | 4.65 | 1.20 | [101.43, 119.90] |
| Decreasing 3 to 2 | 11 | 108.71 ms | 3.20 | 0.97 | [102.34, 112.90] |
| Increasing 2 to 3 | 14 | 110.33 ms | 4.46 | 1.19 | [100.35, 117.09] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 12 | 2.48 µV | 1.83 | 0.53 | [0.30, 7.32] |
| Cardinality3 | 16 | 2.36 µV | 2.03 | 0.51 | [0.06, 6.61] |
| Decreasing 3 to 2 | 19 | 3.98 µV | 3.28 | 0.75 | [0.04, 11.98] |
| Increasing 2 to 3 | 18 | 3.93 µV | 2.94 | 0.69 | [0.09, 9.80] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 12 | 464.74 ms | 13.25 | 3.83 | [441.62, 480.57] |
| Cardinality3 | 16 | 465.80 ms | 24.91 | 6.23 | [423.68, 525.48] |
| Decreasing 3 to 2 | 19 | 480.47 ms | 23.59 | 5.41 | [426.83, 524.17] |
| Increasing 2 to 3 | 18 | 472.30 ms | 20.80 | 4.90 | [428.70, 520.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 285.57, BIC = 303.07
- Effect 1 effect: *β* = -0.02, *SE* = 0.284, *z* = -0.065, *p* = 0.948
- Effect 2 effect: *β* = 0.01, *SE* = 0.285, *z* = 0.027, *p* = 0.979
- Effect 3 effect: *β* = 0.09, *SE* = 0.285, *z* = 0.303, *p* = 0.762
- Effect 4 effect: *β* = -0.44, *SE* = 0.048, *z* = -9.203, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.94, *p* = 0.134, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.72 | 19 | = 0.573 | 0.16 [-0.31, 0.63] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 2.26 | 19 | = 0.213 | 0.48 [-0.10, 0.82] | small | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.87 | 19 | = 0.573 | 0.24 [-0.28, 0.67] | small | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 1.80 | 19 | = 0.262 | 0.37 [-0.06, 0.86] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.29 | 19 | = 0.775 | 0.08 [-0.41, 0.48] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -1.32 | 19 | = 0.404 | -0.33 [-0.77, 0.14] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 682.72, BIC = 700.22
- Effect 1 effect: *β* = -0.41, *SE* = 2.582, *z* = -0.159, *p* = 0.873
- Effect 2 effect: *β* = 1.25, *SE* = 2.595, *z* = 0.483, *p* = 0.629
- Effect 3 effect: *β* = -0.67, *SE* = 2.596, *z* = -0.256, *p* = 0.798
- Effect 4 effect: *β* = -0.26, *SE* = 0.429, *z* = -0.611, *p* = 0.541

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.09, *p* = 0.966, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.11 | 19 | = 0.969 | 0.02 [-0.44, 0.49] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -0.30 | 19 | = 0.969 | -0.08 [-0.48, 0.40] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.04 | 19 | = 0.969 | 0.01 [-0.46, 0.48] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -0.50 | 19 | = 0.969 | -0.15 [-0.55, 0.34] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.10 | 19 | = 0.969 | -0.02 [-0.41, 0.48] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.49 | 19 | = 0.969 | 0.14 [-0.31, 0.58] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 178.41, BIC = 192.20
- Effect 1 effect: *β* = 0.06, *SE* = 0.390, *z* = 0.143, *p* = 0.886
- Effect 2 effect: *β* = -0.24, *SE* = 0.427, *z* = -0.562, *p* = 0.574
- Effect 3 effect: *β* = -0.23, *SE* = 0.398, *z* = -0.576, *p* = 0.564
- Effect 4 effect: *β* = 0.80, *SE* = 0.113, *z* = 7.114, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.26, *p* = 0.850, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.08 | 5 | = 0.941 | -0.04 [-0.90, 0.54] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.52 | 5 | = 0.939 | 0.32 [-0.85, 1.01] | small | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.63 | 5 | = 0.939 | 0.37 [-0.58, 0.97] | small | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.65 | 5 | = 0.939 | 0.30 [-0.59, 0.96] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.69 | 5 | = 0.939 | 0.34 [-0.54, 1.01] | small | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.08 | 5 | = 0.941 | 0.04 [-1.19, 0.69] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 311.64, BIC = 325.43
- Effect 1 effect: *β* = -0.90, *SE* = 1.476, *z* = -0.612, *p* = 0.541
- Effect 2 effect: *β* = -2.43, *SE* = 1.608, *z* = -1.511, *p* = 0.131
- Effect 3 effect: *β* = -1.00, *SE* = 1.494, *z* = -0.670, *p* = 0.503
- Effect 4 effect: *β* = 0.11, *SE* = 0.407, *z* = 0.267, *p* = 0.789

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.77, *p* = 0.530, η²_G = 0.096
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 1.04 | 5 | = 0.838 | 0.65 [-0.29, 1.22] | medium | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.28 | 5 | = 0.967 | 0.18 [-0.79, 1.06] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.24 | 5 | = 0.967 | 0.16 [-0.65, 0.89] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.23 | 5 | = 0.838 | -0.55 [-0.70, 0.84] | medium | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.88 | 5 | = 0.838 | -0.50 [-0.84, 0.70] | small | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.04 | 5 | = 0.967 | 0.02 [-1.20, 0.68] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 256.91, BIC = 272.13
- Effect 1 effect: *β* = -0.04, *SE* = 0.504, *z* = -0.087, *p* = 0.931
- Effect 2 effect: *β* = 0.92, *SE* = 0.497, *z* = 1.851, *p* = 0.064
- Effect 3 effect: *β* = -0.05, *SE* = 0.535, *z* = -0.087, *p* = 0.931
- Effect 4 effect: *β* = 0.66, *SE* = 0.072, *z* = 9.159, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.99, *p* = 0.051, η²_G = 0.159
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -1.56 | 8 | = 0.278 | -0.48 [-0.92, 0.44] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -2.01 | 8 | = 0.236 | -0.87 [-1.21, 0.15] | large | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -2.42 | 8 | = 0.236 | -1.08 [-1.75, -0.05] | large | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.29 | 8 | = 0.282 | -0.55 [-0.99, 0.16] | medium | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -1.45 | 8 | = 0.278 | -0.68 [-0.92, 0.32] | medium | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.15 | 8 | = 0.886 | 0.03 [-0.29, 0.79] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 593.87, BIC = 609.09
- Effect 1 effect: *β* = 0.88, *SE* = 8.065, *z* = 0.110, *p* = 0.913
- Effect 2 effect: *β* = 15.16, *SE* = 7.835, *z* = 1.935, *p* = 0.053
- Effect 3 effect: *β* = 6.35, *SE* = 8.228, *z* = 0.771, *p* = 0.440
- Effect 4 effect: *β* = 0.51, *SE* = 1.015, *z* = 0.502, *p* = 0.616

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.22, *p* = 0.324, η²_G = 0.097
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.70 | 8 | = 0.605 | -0.37 [-0.73, 0.62] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -1.61 | 8 | = 0.605 | -0.72 [-1.09, 0.24] | medium | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.70 | 8 | = 0.605 | -0.39 [-0.96, 0.49] | small | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.28 | 8 | = 0.605 | -0.45 [-1.29, -0.06] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.08 | 8 | = 0.941 | 0.03 [-0.87, 0.36] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 1.03 | 8 | = 0.605 | 0.50 [-0.29, 0.79] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.051)

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
