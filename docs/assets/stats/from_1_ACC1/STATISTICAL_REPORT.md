# Statistical Analysis Report: tables

**Generated:** 2025-10-17 17:27:14

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
| 1 to 1 | 21 | -3.33 µV | 1.73 | 0.38 | [-7.40, -0.32] |
| 1 to 2 | 22 | -3.27 µV | 1.65 | 0.35 | [-6.11, -0.53] |
| 1 to 3 | 24 | -3.85 µV | 1.86 | 0.38 | [-8.34, -0.75] |
| 1 to 4 | 21 | -4.58 µV | 2.59 | 0.56 | [-10.30, -0.72] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 21 | 173.42 ms | 11.61 | 2.53 | [153.33, 203.86] |
| 1 to 2 | 22 | 174.46 ms | 14.03 | 2.99 | [152.58, 207.03] |
| 1 to 3 | 24 | 175.63 ms | 11.71 | 2.39 | [152.76, 204.19] |
| 1 to 4 | 21 | 174.68 ms | 11.27 | 2.46 | [155.48, 202.67] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 13 | 1.33 µV | 1.29 | 0.36 | [-0.05, 3.53] |
| 1 to 2 | 13 | 1.41 µV | 1.22 | 0.34 | [0.14, 3.53] |
| 1 to 3 | 10 | 1.48 µV | 0.93 | 0.29 | [0.25, 3.06] |
| 1 to 4 | 14 | 1.65 µV | 1.07 | 0.28 | [0.07, 3.86] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 13 | 79.51 ms | 9.35 | 2.59 | [65.02, 92.73] |
| 1 to 2 | 13 | 80.28 ms | 8.91 | 2.47 | [65.02, 92.73] |
| 1 to 3 | 10 | 78.62 ms | 8.42 | 2.66 | [64.79, 91.72] |
| 1 to 4 | 14 | 80.89 ms | 5.99 | 1.60 | [64.45, 92.95] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 15 | 3.76 µV | 2.70 | 0.70 | [0.21, 10.49] |
| 1 to 2 | 16 | 3.52 µV | 2.75 | 0.69 | [0.21, 10.49] |
| 1 to 3 | 20 | 4.16 µV | 3.37 | 0.75 | [0.48, 12.29] |
| 1 to 4 | 20 | 3.79 µV | 2.86 | 0.64 | [0.48, 10.75] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 15 | 449.94 ms | 26.97 | 6.96 | [394.01, 488.80] |
| 1 to 2 | 16 | 458.21 ms | 33.39 | 8.35 | [394.01, 528.22] |
| 1 to 3 | 20 | 457.14 ms | 22.24 | 4.97 | [401.27, 486.38] |
| 1 to 4 | 20 | 457.72 ms | 27.01 | 6.04 | [402.36, 509.19] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.67, BIC = 333.01
- Effect 1 effect: *β* = -0.12, *SE* = 0.339, *z* = -0.352, *p* = 0.725
- Effect 2 effect: *β* = -0.40, *SE* = 0.335, *z* = -1.180, *p* = 0.238
- Effect 3 effect: *β* = -1.01, *SE* = 0.346, *z* = -2.910, *p* = 0.004
- Effect 4 effect: *β* = -0.36, *SE* = 0.066, *z* = -5.465, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.35, *p* = 0.083, η²_G = 0.038
- Greenhouse-Geisser corrected: *p* = 0.118 (ε = 0.587)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -0.22 | 18 | = 0.831 | -0.02 [-0.38, 0.53] | negligible | n.s. |
| 1 to 1 vs 1 to 3 | 1.54 | 18 | = 0.243 | 0.27 [-0.08, 0.86] | small | n.s. |
| 1 to 1 vs 1 to 4 | 1.84 | 18 | = 0.243 | 0.41 [-0.08, 0.93] | small | n.s. |
| 1 to 2 vs 1 to 3 | 1.46 | 18 | = 0.243 | 0.29 [-0.13, 0.78] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.77 | 18 | = 0.243 | 0.42 [-0.10, 0.91] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.88 | 18 | = 0.467 | 0.19 [-0.25, 0.68] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 638.98, BIC = 656.32
- Effect 1 effect: *β* = -0.15, *SE* = 1.819, *z* = -0.081, *p* = 0.936
- Effect 2 effect: *β* = 0.98, *SE* = 1.801, *z* = 0.543, *p* = 0.587
- Effect 3 effect: *β* = 1.46, *SE* = 1.861, *z* = 0.785, *p* = 0.432
- Effect 4 effect: *β* = 0.31, *SE* = 0.380, *z* = 0.808, *p* = 0.419

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.32, *p* = 0.808, η²_G = 0.004
- Greenhouse-Geisser corrected: *p* = 0.680 (ε = 0.540)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.06 | 18 | = 0.777 | 0.03 [-0.16, 0.78] | negligible | n.s. |
| 1 to 1 vs 1 to 3 | 0.23 | 18 | = 0.965 | 0.05 [-0.54, 0.37] | negligible | n.s. |
| 1 to 1 vs 1 to 4 | -0.66 | 18 | = 0.777 | -0.10 [-0.64, 0.33] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | 0.04 | 18 | = 0.965 | 0.01 [-0.55, 0.34] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.82 | 18 | = 0.777 | -0.13 [-0.67, 0.30] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -0.92 | 18 | = 0.777 | -0.16 [-0.63, 0.29] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 122.12, BIC = 135.50
- Effect 1 effect: *β* = 0.00, *SE* = 0.262, *z* = 0.008, *p* = 0.994
- Effect 2 effect: *β* = 0.36, *SE* = 0.290, *z* = 1.254, *p* = 0.210
- Effect 3 effect: *β* = 0.39, *SE* = 0.266, *z* = 1.462, *p* = 0.144
- Effect 4 effect: *β* = 0.49, *SE* = 0.062, *z* = 7.894, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.383, η²_G = 0.343
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.42 | 2 | = 0.470 | 0.84 [-0.71, 0.56] | large | n.s. |
| 1 to 1 vs 1 to 3 | 1.70 | 2 | = 0.470 | 1.77 [-0.75, 1.40] | large | n.s. |
| 1 to 1 vs 1 to 4 | 1.40 | 2 | = 0.470 | 1.52 [-0.78, 0.89] | large | n.s. |
| 1 to 2 vs 1 to 3 | 0.65 | 2 | = 0.699 | 0.56 [-1.03, 0.82] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -0.14 | 2 | = 0.904 | -0.14 [-0.73, 0.95] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.34 | 2 | = 0.470 | -0.99 [-1.81, 0.50] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 354.52, BIC = 367.90
- Effect 1 effect: *β* = 1.16, *SE* = 2.365, *z* = 0.492, *p* = 0.623
- Effect 2 effect: *β* = -1.34, *SE* = 2.723, *z* = -0.492, *p* = 0.623
- Effect 3 effect: *β* = 3.25, *SE* = 2.509, *z* = 1.295, *p* = 0.195
- Effect 4 effect: *β* = 0.38, *SE* = 0.625, *z* = 0.612, *p* = 0.541

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.239, η²_G = 0.410
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -1.03 | 2 | = 0.615 | -0.60 [-1.08, 0.24] | medium | n.s. |
| 1 to 1 vs 1 to 3 | 1.28 | 2 | = 0.615 | 1.13 [-0.46, 1.89] | large | n.s. |
| 1 to 1 vs 1 to 4 | -0.02 | 2 | = 0.986 | -0.02 [-1.49, 0.32] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | 2.15 | 2 | = 0.615 | 1.34 [-0.38, 1.65] | large | n.s. |
| 1 to 2 vs 1 to 4 | 0.60 | 2 | = 0.731 | 0.61 [-1.19, 0.53] | medium | n.s. |
| 1 to 3 vs 1 to 4 | -1.20 | 2 | = 0.615 | -1.14 [-1.45, 0.72] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 276.75, BIC = 292.58
- Effect 1 effect: *β* = 0.07, *SE* = 0.426, *z* = 0.176, *p* = 0.860
- Effect 2 effect: *β* = 0.48, *SE* = 0.420, *z* = 1.136, *p* = 0.256
- Effect 3 effect: *β* = 0.28, *SE* = 0.410, *z* = 0.673, *p* = 0.501
- Effect 4 effect: *β* = 0.54, *SE* = 0.074, *z* = 7.300, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.72, *p* = 0.179, η²_G = 0.029
- Greenhouse-Geisser corrected: *p* = 0.205 (ε = 0.566)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.30 | 12 | = 0.393 | 0.04 [-0.42, 0.75] | negligible | n.s. |
| 1 to 1 vs 1 to 3 | -1.50 | 12 | = 0.393 | -0.37 [-1.04, 0.17] | small | n.s. |
| 1 to 1 vs 1 to 4 | -0.89 | 12 | = 0.393 | -0.20 [-0.89, 0.25] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | -1.69 | 12 | = 0.393 | -0.40 [-1.11, 0.11] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.01 | 12 | = 0.393 | -0.23 [-0.89, 0.25] | small | n.s. |
| 1 to 3 vs 1 to 4 | 1.00 | 12 | = 0.393 | 0.18 [-0.28, 0.70] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 680.08, BIC = 695.91
- Effect 1 effect: *β* = 7.68, *SE* = 9.158, *z* = 0.838, *p* = 0.402
- Effect 2 effect: *β* = 6.42, *SE* = 8.685, *z* = 0.739, *p* = 0.460
- Effect 3 effect: *β* = 7.23, *SE* = 8.643, *z* = 0.836, *p* = 0.403
- Effect 4 effect: *β* = 0.91, *SE* = 1.130, *z* = 0.808, *p* = 0.419

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.711, η²_G = 0.026
- Greenhouse-Geisser corrected: *p* = 0.575 (ε = 0.478)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 0.67 | 12 | = 0.665 | 0.05 [-0.38, 0.78] | negligible | n.s. |
| 1 to 1 vs 1 to 3 | -0.73 | 12 | = 0.665 | -0.30 [-0.85, 0.32] | small | n.s. |
| 1 to 1 vs 1 to 4 | -0.61 | 12 | = 0.665 | -0.29 [-0.68, 0.43] | small | n.s. |
| 1 to 2 vs 1 to 3 | -0.85 | 12 | = 0.665 | -0.33 [-0.80, 0.37] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.67 | 12 | = 0.665 | -0.32 [-0.58, 0.52] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.08 | 12 | = 0.935 | 0.03 [-0.63, 0.34] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.083)

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
