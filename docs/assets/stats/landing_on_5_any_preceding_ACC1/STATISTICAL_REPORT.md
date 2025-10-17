# Statistical Analysis Report: tables

**Generated:** 2025-10-17 04:51:19

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

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 337.50, BIC = 354.43
- Effect 1 effect: *β* = 0.56, *SE* = 0.421, *z* = 1.342, *p* = 0.180
- Effect 2 effect: *β* = -0.46, *SE* = 0.423, *z* = -1.083, *p* = 0.279
- Effect 3 effect: *β* = -0.59, *SE* = 0.482, *z* = -1.216, *p* = 0.224
- Effect 4 effect: *β* = -0.41, *SE* = 0.072, *z* = -5.729, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.90, *p* = 0.016, η²_G = 0.108
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

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

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 651.09, BIC = 668.02
- Effect 1 effect: *β* = -5.49, *SE* = 2.662, *z* = -2.062, *p* = 0.039
- Effect 2 effect: *β* = -3.46, *SE* = 2.676, *z* = -1.295, *p* = 0.195
- Effect 3 effect: *β* = -2.81, *SE* = 3.059, *z* = -0.917, *p* = 0.359
- Effect 4 effect: *β* = -0.19, *SE* = 0.463, *z* = -0.411, *p* = 0.681

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.374, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

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


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 184.93, BIC = 197.58
- Effect 1 effect: *β* = -0.75, *SE* = 0.603, *z* = -1.240, *p* = 0.215
- Effect 2 effect: *β* = 0.69, *SE* = 0.595, *z* = 1.151, *p* = 0.250
- Effect 3 effect: *β* = 0.85, *SE* = 0.915, *z* = 0.927, *p* = 0.354
- Effect 4 effect: *β* = 1.88, *SE* = 0.234, *z* = 8.028, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 301.92, BIC = 314.56
- Effect 1 effect: *β* = 1.31, *SE* = 2.217, *z* = 0.589, *p* = 0.556
- Effect 2 effect: *β* = 1.44, *SE* = 2.324, *z* = 0.620, *p* = 0.535
- Effect 3 effect: *β* = 3.28, *SE* = 3.367, *z* = 0.974, *p* = 0.330
- Effect 4 effect: *β* = 0.01, *SE* = 0.861, *z* = 0.011, *p* = 0.991

_Note: LMM uses all available subject data via maximum likelihood estimation._

_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 256.71, BIC = 271.82
- Effect 1 effect: *β* = 0.41, *SE* = 0.486, *z* = 0.844, *p* = 0.399
- Effect 2 effect: *β* = 0.94, *SE* = 0.495, *z* = 1.910, *p* = 0.056
- Effect 3 effect: *β* = -0.23, *SE* = 0.543, *z* = -0.424, *p* = 0.671
- Effect 4 effect: *β* = 0.52, *SE* = 0.076, *z* = 6.770, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.03, *p* = 0.140, η²_G = 0.176
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

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

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 648.14, BIC = 663.25
- Effect 1 effect: *β* = 11.83, *SE* = 11.002, *z* = 1.075, *p* = 0.282
- Effect 2 effect: *β* = 35.14, *SE* = 11.248, *z* = 3.124, *p* = 0.002
- Effect 3 effect: *β* = 35.02, *SE* = 12.246, *z* = 2.859, *p* = 0.004
- Effect 4 effect: *β* = -0.05, *SE* = 1.641, *z* = -0.031, *p* = 0.975

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.24, *p* < .001, η²_G = 0.346
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

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
