# Statistical Analysis Report: tables

**Generated:** 2025-10-18 13:29:02

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
| 1 to 2 | 21 | -3.44 µV | 1.75 | 0.38 | [-7.52, -0.39] |
| 1 to 3 | 24 | -4.27 µV | 1.79 | 0.36 | [-9.11, -0.98] |
| 1 to 4 | 22 | -4.42 µV | 2.53 | 0.54 | [-10.14, 0.09] |
| Cardinality1 | 14 | -2.41 µV | 2.34 | 0.63 | [-7.96, -0.17] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | 172.72 ms | 10.94 | 2.39 | [153.94, 202.06] |
| 1 to 3 | 24 | 173.43 ms | 9.77 | 1.99 | [152.60, 198.67] |
| 1 to 4 | 22 | 172.55 ms | 9.39 | 2.00 | [155.77, 192.64] |
| Cardinality1 | 14 | 179.54 ms | 16.76 | 4.48 | [152.87, 206.40] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 1.17 µV | 1.04 | 0.29 | [0.04, 3.79] |
| 1 to 3 | 11 | 1.84 µV | 1.54 | 0.46 | [0.14, 5.83] |
| 1 to 4 | 12 | 2.09 µV | 1.54 | 0.44 | [0.04, 4.87] |
| Cardinality1 | 18 | 2.28 µV | 2.30 | 0.54 | [0.20, 9.22] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 102.59 ms | 6.93 | 1.92 | [91.02, 115.13] |
| 1 to 3 | 11 | 107.28 ms | 5.93 | 1.79 | [100.60, 118.07] |
| 1 to 4 | 12 | 104.10 ms | 6.03 | 1.74 | [96.21, 114.34] |
| Cardinality1 | 18 | 108.95 ms | 7.41 | 1.75 | [95.61, 118.40] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 3.41 µV | 2.69 | 0.67 | [0.03, 10.14] |
| 1 to 3 | 19 | 3.85 µV | 3.02 | 0.69 | [0.55, 12.40] |
| 1 to 4 | 20 | 3.65 µV | 2.74 | 0.61 | [0.38, 10.25] |
| Cardinality1 | 11 | 1.56 µV | 1.32 | 0.40 | [0.17, 3.65] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 449.18 ms | 37.26 | 9.31 | [383.98, 535.93] |
| 1 to 3 | 19 | 455.62 ms | 22.70 | 5.21 | [393.40, 482.51] |
| 1 to 4 | 20 | 448.23 ms | 32.89 | 7.35 | [379.00, 508.75] |
| Cardinality1 | 11 | 437.39 ms | 47.60 | 14.35 | [366.48, 526.82] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 300.89, BIC = 317.65
- **1 to 3 vs 1 to 2**: *β* = -0.34, *SE* = 0.381, *z* = -0.903, *p* = 0.367
- **1 to 4 vs 1 to 2**: *β* = -0.84, *SE* = 0.384, *z* = -2.195, *p* = 0.028
- **Cardinality1 vs 1 to 2**: *β* = 0.66, *SE* = 0.448, *z* = 1.474, *p* = 0.141
- **SNR**: *β* = -0.42, *SE* = 0.052, *z* = -8.185, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.24, *p* = 0.034, η²_G = 0.126
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.36 | 11 | = 0.114 | 0.60 [0.05, 1.02] | medium | n.s. |
| 1 to 2 vs 1 to 4 | 0.58 | 11 | = 0.572 | 0.12 [-0.08, 0.89] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -1.27 | 11 | = 0.277 | -0.48 [-1.02, 0.29] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.67 | 11 | = 0.248 | -0.42 [-0.49, 0.40] | small | n.s. |
| 1 to 3 vs Cardinality1 | -2.46 | 11 | = 0.114 | -1.01 [-1.45, -0.13] | large | n.s. |
| 1 to 4 vs Cardinality1 | -1.43 | 11 | = 0.269 | -0.55 [-1.14, 0.14] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 599.00, BIC = 615.76
- **1 to 3 vs 1 to 2**: *β* = 0.37, *SE* = 2.062, *z* = 0.178, *p* = 0.859
- **1 to 4 vs 1 to 2**: *β* = 0.52, *SE* = 2.071, *z* = 0.253, *p* = 0.800
- **Cardinality1 vs 1 to 2**: *β* = 5.18, *SE* = 2.455, *z* = 2.111, *p* = 0.035
- **SNR**: *β* = -0.23, *SE* = 0.311, *z* = -0.753, *p* = 0.452

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.90, *p* = 0.050, η²_G = 0.060
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.84 | 11 | = 0.503 | 0.24 [-0.41, 0.50] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.06 | 11 | = 0.951 | -0.01 [-0.50, 0.44] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -1.86 | 11 | = 0.181 | -0.38 [-1.22, 0.14] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.24 | 11 | = 0.359 | -0.29 [-0.56, 0.33] | small | n.s. |
| 1 to 3 vs Cardinality1 | -2.50 | 11 | = 0.177 | -0.69 [-1.18, 0.06] | medium | n.s. |
| 1 to 4 vs Cardinality1 | -1.86 | 11 | = 0.181 | -0.41 [-0.92, 0.32] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 167.67, BIC = 181.60
- **1 to 3 vs 1 to 2**: *β* = 0.42, *SE* = 0.399, *z* = 1.066, *p* = 0.286
- **1 to 4 vs 1 to 2**: *β* = 0.29, *SE* = 0.396, *z* = 0.724, *p* = 0.469
- **Cardinality1 vs 1 to 2**: *β* = 0.77, *SE* = 0.355, *z* = 2.157, *p* = 0.031
- **SNR**: *β* = 0.84, *SE* = 0.090, *z* = 9.320, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.81, *p* = 0.077, η²_G = 0.413
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.52 | 2 | = 0.657 | 0.41 [-1.26, 0.63] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.71 | 2 | = 0.300 | -0.88 [-2.43, 0.00] | large | n.s. |
| 1 to 2 vs Cardinality1 | -1.66 | 2 | = 0.300 | -1.22 [-1.34, 0.12] | large | n.s. |
| 1 to 3 vs 1 to 4 | -3.50 | 2 | = 0.300 | -1.36 [-1.52, 0.67] | large | n.s. |
| 1 to 3 vs Cardinality1 | -2.83 | 2 | = 0.300 | -1.48 [-1.04, 0.42] | large | n.s. |
| 1 to 4 vs Cardinality1 | -1.61 | 2 | = 0.300 | -0.67 [-1.48, 0.11] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 368.65, BIC = 382.57
- **1 to 3 vs 1 to 2**: *β* = 4.71, *SE* = 2.638, *z* = 1.787, *p* = 0.074
- **1 to 4 vs 1 to 2**: *β* = 1.70, *SE* = 2.602, *z* = 0.652, *p* = 0.515
- **Cardinality1 vs 1 to 2**: *β* = 6.44, *SE* = 2.349, *z* = 2.741, *p* = 0.006
- **SNR**: *β* = -0.29, *SE* = 0.580, *z* = -0.502, *p* = 0.616

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.781, η²_G = 0.146
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.04 | 2 | = 0.971 | 0.03 [-1.43, 0.52] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 0.73 | 2 | = 0.971 | 0.79 [-1.01, 0.85] | medium | n.s. |
| 1 to 2 vs Cardinality1 | -0.14 | 2 | = 0.971 | -0.08 [-1.09, 0.31] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.53 | 2 | = 0.971 | 0.56 [-0.47, 1.86] | medium | n.s. |
| 1 to 3 vs Cardinality1 | -0.08 | 2 | = 0.971 | -0.06 [-0.93, 0.51] | negligible | n.s. |
| 1 to 4 vs Cardinality1 | -1.02 | 2 | = 0.971 | -0.91 [-1.56, 0.06] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 257.85, BIC = 273.18
- **1 to 3 vs 1 to 2**: *β* = 0.08, *SE* = 0.450, *z* = 0.184, *p* = 0.854
- **1 to 4 vs 1 to 2**: *β* = 0.11, *SE* = 0.441, *z* = 0.257, *p* = 0.797
- **Cardinality1 vs 1 to 2**: *β* = -0.49, *SE* = 0.561, *z* = -0.876, *p* = 0.381
- **SNR**: *β* = 0.66, *SE* = 0.080, *z* = 8.324, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.68, *p* = 0.002, η²_G = 0.225
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.72 | 9 | = 0.143 | -0.44 [-0.86, 0.32] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.90 | 9 | = 0.135 | -0.44 [-0.91, 0.23] | small | n.s. |
| 1 to 2 vs Cardinality1 | 2.37 | 9 | = 0.084 | 0.96 [-0.06, 1.56] | large | n.s. |
| 1 to 3 vs 1 to 4 | 0.18 | 9 | = 0.862 | 0.03 [-0.42, 0.54] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | 2.84 | 9 | = 0.059 | 1.34 [0.09, 1.67] | large | n.s. |
| 1 to 4 vs Cardinality1 | 3.28 | 9 | = 0.057 | 1.48 [0.18, 1.82] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 664.00, BIC = 679.33
- **1 to 3 vs 1 to 2**: *β* = 6.76, *SE* = 11.357, *z* = 0.596, *p* = 0.551
- **1 to 4 vs 1 to 2**: *β* = -0.78, *SE* = 11.206, *z* = -0.069, *p* = 0.945
- **Cardinality1 vs 1 to 2**: *β* = -13.22, *SE* = 13.667, *z* = -0.967, *p* = 0.333
- **SNR**: *β* = -0.57, *SE* = 1.602, *z* = -0.359, *p* = 0.720

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.766, η²_G = 0.033
- Greenhouse-Geisser corrected: *p* = 0.694 (ε = 0.689)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.94 | 9 | = 0.849 | -0.48 [-0.92, 0.27] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.74 | 9 | = 0.849 | -0.41 [-0.62, 0.49] | small | n.s. |
| 1 to 2 vs Cardinality1 | -0.16 | 9 | = 0.912 | -0.08 [-0.77, 0.67] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.11 | 9 | = 0.912 | 0.03 [-0.32, 0.65] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | 0.66 | 9 | = 0.849 | 0.29 [-0.35, 1.03] | small | n.s. |
| 1 to 4 vs Cardinality1 | 0.60 | 9 | = 0.849 | 0.25 [-0.39, 0.98] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.034) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* = 0.050) (no significant pairwise comparisons)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.077)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002) (no significant pairwise comparisons)

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
