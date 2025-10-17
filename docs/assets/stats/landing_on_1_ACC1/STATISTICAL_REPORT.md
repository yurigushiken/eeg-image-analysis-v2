# Statistical Analysis Report: tables

**Generated:** 2025-10-17 04:49:50

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
| 2 to 1 | 17 | -2.95 µV | 2.20 | 0.53 | [-8.59, 0.02] |
| 3 to 1 | 20 | -2.98 µV | 2.41 | 0.54 | [-8.43, -0.16] |
| 4 to 1 | 20 | -2.17 µV | 1.63 | 0.36 | [-5.91, -0.14] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 179.78 ms | 6.69 | 1.62 | [165.31, 189.00] |
| 3 to 1 | 20 | 182.38 ms | 8.71 | 1.95 | [167.85, 199.82] |
| 4 to 1 | 20 | 183.86 ms | 8.48 | 1.90 | [168.21, 195.94] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 3.34 µV | 2.20 | 0.52 | [0.49, 6.86] |
| 3 to 1 | 20 | 2.21 µV | 1.38 | 0.31 | [0.14, 6.21] |
| 4 to 1 | 16 | 3.84 µV | 2.23 | 0.56 | [0.43, 9.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 122.52 ms | 8.08 | 1.90 | [106.89, 136.60] |
| 3 to 1 | 20 | 121.95 ms | 9.37 | 2.09 | [102.25, 138.29] |
| 4 to 1 | 16 | 120.91 ms | 7.51 | 1.88 | [105.91, 131.80] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 3.96 µV | 3.07 | 0.67 | [0.17, 10.02] |
| 3 to 1 | 20 | 4.35 µV | 2.58 | 0.58 | [0.87, 11.25] |
| 4 to 1 | 20 | 4.69 µV | 2.98 | 0.67 | [0.25, 9.57] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 481.19 ms | 13.83 | 3.02 | [455.61, 518.99] |
| 3 to 1 | 20 | 477.73 ms | 9.00 | 2.01 | [463.99, 498.81] |
| 4 to 1 | 20 | 478.59 ms | 11.30 | 2.53 | [458.18, 503.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 195.92, BIC = 208.18
- Effect 1 effect: *β* = -0.47, *SE* = 0.297, *z* = -1.565, *p* = 0.118
- Effect 2 effect: *β* = 0.52, *SE* = 0.300, *z* = 1.717, *p* = 0.086
- Effect 3 effect: *β* = -0.54, *SE* = 0.060, *z* = -8.930, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.78, *p* = 0.188, η²_G = 0.046
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -0.12 | 13 | = 0.903 | -0.03 [-0.44, 0.62] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -2.22 | 13 | = 0.135 | -0.54 [-1.08, 0.10] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -1.26 | 13 | = 0.345 | -0.42 [-0.85, 0.17] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 390.43, BIC = 402.69
- Effect 1 effect: *β* = 3.06, *SE* = 1.654, *z* = 1.848, *p* = 0.065
- Effect 2 effect: *β* = 4.52, *SE* = 1.671, *z* = 2.703, *p* = 0.007
- Effect 3 effect: *β* = -0.04, *SE* = 0.331, *z* = -0.122, *p* = 0.903

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.55, *p* = 0.098, η²_G = 0.044
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -1.25 | 13 | = 0.233 | -0.25 [-0.94, 0.17] | small | n.s. |
| 2 to 1 vs 4 to 1 | -1.79 | 13 | = 0.233 | -0.50 [-1.15, 0.04] | small | n.s. |
| 3 to 1 vs 4 to 1 | -1.42 | 13 | = 0.233 | -0.26 [-0.76, 0.25] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 205.11, BIC = 217.04
- Effect 1 effect: *β* = -0.59, *SE* = 0.445, *z* = -1.328, *p* = 0.184
- Effect 2 effect: *β* = 0.49, *SE* = 0.464, *z* = 1.053, *p* = 0.292
- Effect 3 effect: *β* = 0.39, *SE* = 0.075, *z* = 5.274, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.07, *p* = 0.028, η²_G = 0.113
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.34 | 14 | = 0.201 | 0.46 [-0.10, 0.94] | small | n.s. |
| 2 to 1 vs 4 to 1 | -1.45 | 14 | = 0.201 | -0.36 [-0.95, 0.20] | small | n.s. |
| 3 to 1 vs 4 to 1 | -3.04 | 14 | = 0.026 | -0.90 [-1.26, -0.08] | large | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 381.37, BIC = 393.30
- Effect 1 effect: *β* = -0.42, *SE* = 1.920, *z* = -0.220, *p* = 0.826
- Effect 2 effect: *β* = -0.22, *SE* = 2.019, *z* = -0.111, *p* = 0.912
- Effect 3 effect: *β* = 0.01, *SE* = 0.332, *z* = 0.017, *p* = 0.986

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.857, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.20 | 14 | = 0.845 | 0.06 [-0.42, 0.57] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.38 | 14 | = 0.845 | -0.10 [-0.65, 0.46] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.53 | 14 | = 0.845 | -0.16 [-0.63, 0.44] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 290.58, BIC = 303.25
- Effect 1 effect: *β* = -0.26, *SE* = 0.708, *z* = -0.362, *p* = 0.717
- Effect 2 effect: *β* = 0.18, *SE* = 0.706, *z* = 0.259, *p* = 0.795
- Effect 3 effect: *β* = 0.19, *SE* = 0.045, *z* = 4.253, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.649, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.15 | 16 | = 0.882 | 0.04 [-0.53, 0.43] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.74 | 16 | = 0.705 | -0.22 [-0.68, 0.29] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.79 | 16 | = 0.705 | -0.27 [-0.64, 0.36] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 478.68, BIC = 491.34
- Effect 1 effect: *β* = -3.45, *SE* = 3.197, *z* = -1.079, *p* = 0.281
- Effect 2 effect: *β* = -2.23, *SE* = 3.189, *z* = -0.700, *p* = 0.484
- Effect 3 effect: *β* = 0.02, *SE* = 0.196, *z* = 0.120, *p* = 0.904

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.365, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.71 | 16 | = 0.321 | 0.44 [-0.07, 0.94] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.72 | 16 | = 0.546 | 0.24 [-0.44, 0.53] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.62 | 16 | = 0.546 | -0.20 [-0.56, 0.44] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Marginal trend toward condition differences (*p* = 0.098)
**P1 amplitude:** Significant main effect of condition (*p* = 0.028). Post-hoc tests revealed:
  - 3 to 1 showed smaller amplitude than 4 to 1 (*d* = -0.90)

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
