# Statistical Analysis Report: tables

**Generated:** 2025-10-17 04:51:46

---

## 1. Analysis Overview

**Total Measurements:** 192
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
| 3 to 6 | 23 | -4.64 µV | 2.45 | 0.51 | [-10.40, -1.15] |
| 4 to 6 | 22 | -4.17 µV | 2.72 | 0.58 | [-12.25, -0.08] |
| 5 to 6 | 12 | -3.23 µV | 2.95 | 0.85 | [-8.92, 0.14] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | 171.79 ms | 12.13 | 2.53 | [152.64, 195.63] |
| 4 to 6 | 22 | 169.23 ms | 13.22 | 2.82 | [132.77, 190.71] |
| 5 to 6 | 12 | 172.38 ms | 22.74 | 6.56 | [133.84, 206.05] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 9 | 2.72 µV | 2.01 | 0.67 | [0.41, 6.89] |
| 4 to 6 | 13 | 2.25 µV | 1.30 | 0.36 | [0.79, 4.74] |
| 5 to 6 | 13 | 3.29 µV | 2.81 | 0.78 | [0.49, 8.65] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 9 | 93.01 ms | 6.31 | 2.10 | [82.43, 101.59] |
| 4 to 6 | 13 | 96.61 ms | 6.29 | 1.75 | [83.32, 106.71] |
| 5 to 6 | 13 | 98.20 ms | 6.63 | 1.84 | [87.05, 109.49] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 18 | 3.23 µV | 1.97 | 0.46 | [0.57, 8.91] |
| 4 to 6 | 18 | 4.23 µV | 2.83 | 0.67 | [0.23, 9.06] |
| 5 to 6 | 9 | 4.90 µV | 2.80 | 0.93 | [2.16, 11.55] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 18 | 493.70 ms | 9.24 | 2.18 | [469.58, 505.95] |
| 4 to 6 | 18 | 496.93 ms | 11.19 | 2.64 | [468.93, 520.21] |
| 5 to 6 | 9 | 498.50 ms | 7.90 | 2.63 | [491.95, 513.44] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 234.26, BIC = 246.52
- Effect 1 effect: *β* = 0.94, *SE* = 0.509, *z* = 1.853, *p* = 0.064
- Effect 2 effect: *β* = -0.21, *SE* = 0.580, *z* = -0.354, *p* = 0.723
- Effect 3 effect: *β* = -0.83, *SE* = 0.076, *z* = -10.879, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.245, η²_G = 0.077
- Greenhouse-Geisser corrected: *p* = 0.249 (ε = 0.591)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -2.36 | 11 | = 0.113 | -0.63 [-0.67, 0.22] | medium | n.s. |
| 3 to 6 vs 5 to 6 | -1.26 | 11 | = 0.352 | -0.56 [-1.02, 0.29] | medium | n.s. |
| 4 to 6 vs 5 to 6 | -0.38 | 11 | = 0.708 | -0.15 [-0.75, 0.53] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 461.10, BIC = 473.36
- Effect 1 effect: *β* = -3.38, *SE* = 2.689, *z* = -1.259, *p* = 0.208
- Effect 2 effect: *β* = 1.63, *SE* = 3.679, *z* = 0.444, *p* = 0.657
- Effect 3 effect: *β* = 0.88, *SE* = 0.723, *z* = 1.216, *p* = 0.224

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.857, η²_G = 0.003
- Greenhouse-Geisser corrected: *p* = 0.751 (ε = 0.616)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.99 | 11 | = 0.988 | 0.16 [-0.12, 0.79] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -0.02 | 11 | = 0.988 | -0.00 [-0.64, 0.63] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -0.40 | 11 | = 0.988 | -0.11 [-0.75, 0.52] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 122.14, BIC = 131.47
- Effect 1 effect: *β* = 0.45, *SE* = 0.504, *z* = 0.892, *p* = 0.372
- Effect 2 effect: *β* = 1.03, *SE* = 0.504, *z* = 2.034, *p* = 0.042
- Effect 3 effect: *β* = 1.04, *SE* = 0.118, *z* = 8.794, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.08, *p* = 0.920, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.09 | 4 | = 0.930 | -0.06 [-0.69, 1.19] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -0.30 | 4 | = 0.930 | -0.24 [-1.38, 1.11] | small | n.s. |
| 4 to 6 vs 5 to 6 | -0.36 | 4 | = 0.930 | -0.18 [-0.82, 0.85] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 225.68, BIC = 235.02
- Effect 1 effect: *β* = 2.63, *SE* = 1.514, *z* = 1.736, *p* = 0.082
- Effect 2 effect: *β* = 4.58, *SE* = 1.572, *z* = 2.910, *p* = 0.004
- Effect 3 effect: *β* = 0.43, *SE* = 0.431, *z* = 0.999, *p* = 0.318

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.56, *p* = 0.138, η²_G = 0.098
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.35 | 4 | = 0.338 | -0.49 [-1.37, 0.55] | small | n.s. |
| 3 to 6 vs 5 to 6 | -1.95 | 4 | = 0.338 | -0.65 [-2.33, 0.59] | medium | n.s. |
| 4 to 6 vs 5 to 6 | -1.09 | 4 | = 0.338 | -0.28 [-1.37, 0.40] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 189.40, BIC = 200.24
- Effect 1 effect: *β* = 0.17, *SE* = 0.485, *z* = 0.348, *p* = 0.728
- Effect 2 effect: *β* = 2.00, *SE* = 0.584, *z* = 3.418, *p* = 0.001
- Effect 3 effect: *β* = 0.60, *SE* = 0.111, *z* = 5.396, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.33, *p* = 0.129, η²_G = 0.112
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -2.81 | 8 | = 0.069 | -0.89 [-1.21, -0.05] | large | n.s. |
| 3 to 6 vs 5 to 6 | -1.48 | 8 | = 0.267 | -0.64 [-1.31, 0.32] | medium | n.s. |
| 4 to 6 vs 5 to 6 | 0.41 | 8 | = 0.694 | 0.15 [-0.64, 0.91] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 342.26, BIC = 353.10
- Effect 1 effect: *β* = 2.82, *SE* = 3.187, *z* = 0.886, *p* = 0.376
- Effect 2 effect: *β* = 4.75, *SE* = 4.224, *z* = 1.125, *p* = 0.261
- Effect 3 effect: *β* = 0.29, *SE* = 0.619, *z* = 0.468, *p* = 0.640

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.525, η²_G = 0.059
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.21 | 8 | = 0.592 | -0.58 [-0.89, 0.21] | medium | n.s. |
| 3 to 6 vs 5 to 6 | -0.90 | 8 | = 0.592 | -0.39 [-1.09, 0.49] | small | n.s. |
| 4 to 6 vs 5 to 6 | 0.29 | 8 | = 0.779 | 0.17 [-0.67, 0.87] | negligible | n.s. |

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
