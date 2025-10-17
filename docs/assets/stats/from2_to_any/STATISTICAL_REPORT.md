# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:50:20

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
| 2 to 1 | 15 | -2.63 µV | 2.21 | 0.57 | [-8.56, -0.03] |
| 2 to 3 | 22 | -3.41 µV | 1.41 | 0.30 | [-5.80, -0.33] |
| 2 to 4 | 22 | -4.32 µV | 2.17 | 0.46 | [-10.88, -0.76] |
| 2 to 5 | 24 | -3.91 µV | 2.23 | 0.45 | [-11.24, -0.68] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 15 | 179.23 ms | 9.02 | 2.33 | [161.55, 195.95] |
| 2 to 3 | 22 | 171.97 ms | 6.80 | 1.45 | [156.88, 186.39] |
| 2 to 4 | 22 | 173.11 ms | 8.52 | 1.82 | [154.05, 195.41] |
| 2 to 5 | 24 | 174.34 ms | 9.70 | 1.98 | [159.37, 196.90] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 2.89 µV | 2.20 | 0.52 | [1.14, 8.35] |
| 2 to 3 | 12 | 1.88 µV | 1.23 | 0.36 | [0.18, 4.26] |
| 2 to 4 | 16 | 1.52 µV | 1.27 | 0.32 | [0.10, 5.23] |
| 2 to 5 | 12 | 1.45 µV | 2.02 | 0.58 | [0.21, 7.34] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 110.27 ms | 4.92 | 1.16 | [103.44, 117.98] |
| 2 to 3 | 12 | 108.95 ms | 7.42 | 2.14 | [98.21, 121.48] |
| 2 to 4 | 16 | 108.10 ms | 8.18 | 2.05 | [90.58, 120.54] |
| 2 to 5 | 12 | 104.64 ms | 8.37 | 2.42 | [93.73, 121.64] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 3.46 µV | 2.42 | 0.56 | [0.42, 9.47] |
| 2 to 3 | 16 | 4.24 µV | 2.69 | 0.67 | [0.04, 9.71] |
| 2 to 4 | 18 | 4.48 µV | 3.27 | 0.77 | [0.11, 12.04] |
| 2 to 5 | 21 | 3.12 µV | 1.97 | 0.43 | [0.09, 7.05] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 478.32 ms | 18.62 | 4.27 | [450.32, 511.70] |
| 2 to 3 | 16 | 465.73 ms | 21.68 | 5.42 | [430.65, 530.06] |
| 2 to 4 | 18 | 467.14 ms | 28.97 | 6.83 | [397.56, 508.39] |
| 2 to 5 | 21 | 460.45 ms | 24.36 | 5.32 | [397.76, 515.87] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.38, *p* = 0.083, η²_G = 0.106
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 1.99 | 14 | = 0.132 | 0.70 [-0.07, 1.10] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 1.99 | 14 | = 0.132 | 0.77 [-0.07, 1.10] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 2.01 | 14 | = 0.132 | 0.73 [-0.07, 1.11] | medium | n.s. |
| 2 to 3 vs 2 to 4 | 0.76 | 14 | = 0.690 | 0.29 [-0.18, 0.75] | small | n.s. |
| 2 to 3 vs 2 to 5 | 0.57 | 14 | = 0.696 | 0.22 [-0.18, 0.72] | small | n.s. |
| 2 to 4 vs 2 to 5 | -0.24 | 14 | = 0.811 | -0.06 [-0.54, 0.35] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 358.67, BIC = 373.18
- Condition effect: *β* = -0.88, *SE* = 0.624, *z* = -1.417, *p* = 0.157

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 5.01, *p* = 0.005, η²_G = 0.109
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 3.73 | 14 | = 0.014 | 0.97 [0.29, 1.63] | large | * |
| 2 to 1 vs 2 to 4 | 2.02 | 14 | = 0.127 | 0.60 [-0.07, 1.11] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 2.61 | 14 | = 0.061 | 0.67 [0.06, 1.29] | medium | n.s. |
| 2 to 3 vs 2 to 4 | -0.96 | 14 | = 0.426 | -0.23 [-0.51, 0.40] | small | n.s. |
| 2 to 3 vs 2 to 5 | -1.27 | 14 | = 0.337 | -0.25 [-0.53, 0.36] | small | n.s. |
| 2 to 4 vs 2 to 5 | 0.03 | 14 | = 0.975 | 0.01 [-0.53, 0.36] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 578.05, BIC = 592.56
- Condition effect: *β* = -6.89, *SE* = 2.001, *z* = -3.442, *p* = 0.001


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 4.92, *p* = 0.014, η²_G = 0.375
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 1.83 | 5 | = 0.160 | 1.18 [-0.24, 1.29] | large | n.s. |
| 2 to 1 vs 2 to 4 | 2.39 | 5 | = 0.160 | 0.96 [-0.05, 1.45] | large | n.s. |
| 2 to 1 vs 2 to 5 | 3.97 | 5 | = 0.064 | 1.89 [0.19, 1.84] | large | n.s. |
| 2 to 3 vs 2 to 4 | -0.07 | 5 | = 0.949 | -0.04 [-0.94, 0.90] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 1.79 | 5 | = 0.160 | 1.19 [-0.76, 0.91] | large | n.s. |
| 2 to 4 vs 2 to 5 | 1.82 | 5 | = 0.160 | 0.80 [-0.11, 1.48] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 235.08, BIC = 247.44
- Condition effect: *β* = -1.15, *SE* = 0.572, *z* = -2.006, *p* = 0.045

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.26, *p* = 0.123, η²_G = 0.170
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.22 | 5 | = 0.232 | 0.83 [0.13, 1.90] | large | n.s. |
| 2 to 1 vs 2 to 4 | -1.21 | 5 | = 0.394 | -0.55 [-0.62, 0.72] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 1.08 | 5 | = 0.394 | 0.42 [-0.04, 1.46] | small | n.s. |
| 2 to 3 vs 2 to 4 | -2.30 | 5 | = 0.232 | -1.12 [-1.04, 0.82] | large | n.s. |
| 2 to 3 vs 2 to 5 | -0.50 | 5 | = 0.635 | -0.19 [-0.84, 0.84] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.31 | 5 | = 0.394 | 0.73 [-0.11, 1.48] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 400.27, BIC = 412.63
- Condition effect: *β* = -1.70, *SE* = 2.490, *z* = -0.682, *p* = 0.495


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.92, *p* = 0.440, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | -0.62 | 14 | = 0.652 | -0.19 [-0.72, 0.40] | negligible | n.s. |
| 2 to 1 vs 2 to 4 | -0.78 | 14 | = 0.652 | -0.27 [-0.80, 0.25] | small | n.s. |
| 2 to 1 vs 2 to 5 | 0.66 | 14 | = 0.652 | 0.19 [-0.43, 0.57] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -0.40 | 14 | = 0.698 | -0.10 [-0.60, 0.47] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 1.50 | 14 | = 0.516 | 0.39 [-0.22, 0.87] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.44 | 14 | = 0.516 | 0.45 [-0.21, 0.81] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 350.23, BIC = 364.05
- Condition effect: *β* = 0.73, *SE* = 0.712, *z* = 1.025, *p* = 0.306

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.95, *p* = 0.137, η²_G = 0.097
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 1.32 | 14 | = 0.332 | 0.49 [-0.23, 0.91] | small | n.s. |
| 2 to 1 vs 2 to 4 | 0.81 | 14 | = 0.518 | 0.23 [-0.35, 0.68] | small | n.s. |
| 2 to 1 vs 2 to 5 | 2.54 | 14 | = 0.142 | 0.95 [0.10, 1.19] | large | n.s. |
| 2 to 3 vs 2 to 4 | -0.49 | 14 | = 0.628 | -0.21 [-0.54, 0.53] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.28 | 14 | = 0.332 | 0.40 [-0.18, 0.92] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.38 | 14 | = 0.332 | 0.59 [-0.22, 0.80] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 686.44, BIC = 700.26
- Condition effect: *β* = -12.08, *SE* = 7.783, *z* = -1.552, *p* = 0.121


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.083)
**N1 latency:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - 2 to 1 showed greater latency than 2 to 3 (*d* = 0.97)
**P1 amplitude:** Significant main effect of condition (*p* = 0.014) (no significant pairwise comparisons)

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

Within-subjects repeated-measures analyses were conducted using:
- Repeated-measures ANOVA with Greenhouse-Geisser correction for sphericity violations (ε < 0.75)
- Post-hoc pairwise t-tests with false discovery rate (FDR) correction for multiple comparisons
- Linear mixed-effects models (LMM) with random intercepts for subjects to handle missing data

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.11
- MNE-Python 1.10.1
- Statsmodels 0.14.5
- Pingouin 0.5.5

### References

- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
