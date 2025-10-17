# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:52:14

---

## 1. Analysis Overview

**Total Measurements:** 360
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| from 2 | 22 | -3.79 µV | 1.47 | 0.31 | [-7.40, -1.06] |
| from 3 | 22 | -3.94 µV | 1.57 | 0.33 | [-8.12, -1.81] |
| from 4 | 24 | -3.90 µV | 2.16 | 0.44 | [-9.38, -0.11] |
| from 5 | 23 | -4.05 µV | 1.84 | 0.38 | [-7.56, -0.84] |
| from 6 | 24 | -3.83 µV | 1.82 | 0.37 | [-7.59, -0.72] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 22 | 173.60 ms | 9.81 | 2.09 | [153.78, 200.00] |
| from 3 | 22 | 170.48 ms | 6.87 | 1.46 | [155.51, 184.34] |
| from 4 | 24 | 173.46 ms | 10.29 | 2.10 | [155.89, 206.76] |
| from 5 | 23 | 173.65 ms | 7.08 | 1.48 | [159.09, 191.18] |
| from 6 | 24 | 174.42 ms | 10.63 | 2.17 | [157.63, 202.58] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 15 | 1.38 µV | 1.11 | 0.29 | [0.03, 3.57] |
| from 3 | 11 | 1.55 µV | 1.67 | 0.50 | [0.08, 5.35] |
| from 4 | 12 | 1.67 µV | 1.09 | 0.31 | [0.21, 3.16] |
| from 5 | 16 | 1.70 µV | 1.03 | 0.26 | [0.08, 3.39] |
| from 6 | 16 | 1.61 µV | 1.56 | 0.39 | [0.02, 6.57] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 15 | 105.40 ms | 3.26 | 0.84 | [98.74, 110.98] |
| from 3 | 11 | 105.72 ms | 3.90 | 1.18 | [98.09, 110.92] |
| from 4 | 12 | 107.09 ms | 2.24 | 0.65 | [102.70, 110.90] |
| from 5 | 16 | 106.59 ms | 3.67 | 0.92 | [99.12, 113.23] |
| from 6 | 16 | 107.16 ms | 4.71 | 1.18 | [96.05, 114.50] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 18 | 3.94 µV | 2.31 | 0.54 | [0.77, 8.20] |
| from 3 | 18 | 3.53 µV | 2.27 | 0.53 | [0.22, 8.37] |
| from 4 | 19 | 3.63 µV | 2.30 | 0.53 | [0.28, 7.31] |
| from 5 | 18 | 3.60 µV | 2.11 | 0.50 | [0.44, 8.92] |
| from 6 | 19 | 3.30 µV | 2.14 | 0.49 | [0.12, 7.42] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 18 | 477.74 ms | 11.92 | 2.81 | [457.53, 498.63] |
| from 3 | 18 | 481.85 ms | 10.17 | 2.40 | [465.89, 497.42] |
| from 4 | 19 | 486.65 ms | 12.44 | 2.85 | [461.94, 512.97] |
| from 5 | 18 | 480.74 ms | 11.51 | 2.71 | [452.30, 509.63] |
| from 6 | 19 | 482.82 ms | 16.81 | 3.86 | [450.72, 520.04] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.40, *p* = 0.807, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.31 | 20 | = 0.846 | 0.06 [-0.39, 0.52] | negligible | n.s. |
| from 2 vs from 4 | 0.77 | 20 | = 0.846 | 0.13 [-0.32, 0.58] | negligible | n.s. |
| from 2 vs from 5 | 1.32 | 20 | = 0.846 | 0.22 [-0.18, 0.75] | small | n.s. |
| from 2 vs from 6 | 0.64 | 20 | = 0.846 | 0.12 [-0.32, 0.57] | negligible | n.s. |
| from 3 vs from 4 | 0.59 | 20 | = 0.846 | 0.08 [-0.24, 0.65] | negligible | n.s. |
| from 3 vs from 5 | 0.85 | 20 | = 0.846 | 0.16 [-0.27, 0.63] | negligible | n.s. |
| from 3 vs from 6 | 0.33 | 20 | = 0.846 | 0.06 [-0.37, 0.52] | negligible | n.s. |
| from 4 vs from 5 | 0.33 | 20 | = 0.846 | 0.06 [-0.44, 0.43] | negligible | n.s. |
| from 4 vs from 6 | -0.12 | 20 | = 0.908 | -0.02 [-0.46, 0.38] | negligible | n.s. |
| from 5 vs from 6 | -0.62 | 20 | = 0.846 | -0.09 [-0.50, 0.36] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 389.15, BIC = 408.37
- Condition effect: *β* = -0.06, *SE* = 0.286, *z* = -0.197, *p* = 0.844

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.68, *p* = 0.037, η²_G = 0.018
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 2.01 | 20 | = 0.153 | 0.27 [-0.04, 0.91] | small | n.s. |
| from 2 vs from 4 | 1.07 | 20 | = 0.426 | 0.14 [-0.30, 0.60] | negligible | n.s. |
| from 2 vs from 5 | -0.83 | 20 | = 0.518 | -0.13 [-0.64, 0.28] | negligible | n.s. |
| from 2 vs from 6 | 0.38 | 20 | = 0.708 | 0.06 [-0.38, 0.50] | negligible | n.s. |
| from 3 vs from 4 | -1.50 | 20 | = 0.282 | -0.13 [-0.83, 0.09] | negligible | n.s. |
| from 3 vs from 5 | -3.75 | 20 | = 0.013 | -0.42 [-1.34, -0.31] | small | * |
| from 3 vs from 6 | -2.08 | 20 | = 0.153 | -0.21 [-0.96, -0.02] | small | n.s. |
| from 4 vs from 5 | -1.98 | 20 | = 0.153 | -0.28 [-0.79, 0.10] | small | n.s. |
| from 4 vs from 6 | -0.62 | 20 | = 0.600 | -0.08 [-0.62, 0.23] | negligible | n.s. |
| from 5 vs from 6 | 1.43 | 20 | = 0.282 | 0.19 [-0.35, 0.51] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 702.90, BIC = 722.11
- Condition effect: *β* = -2.12, *SE* = 1.012, *z* = -2.097, *p* = 0.036


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.55, *p* = 0.699, η²_G = 0.062
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.25 | 4 | = 0.907 | -0.12 [-0.69, 0.74] | negligible | n.s. |
| from 2 vs from 4 | 0.00 | 4 | = 0.999 | 0.00 [-0.90, 0.46] | negligible | n.s. |
| from 2 vs from 5 | -1.24 | 4 | = 0.763 | -0.64 [-1.17, 0.07] | medium | n.s. |
| from 2 vs from 6 | -1.03 | 4 | = 0.763 | -0.51 [-0.87, 0.36] | medium | n.s. |
| from 3 vs from 4 | 0.29 | 4 | = 0.907 | 0.13 [-1.10, 0.59] | negligible | n.s. |
| from 3 vs from 5 | -0.38 | 4 | = 0.907 | -0.23 [-1.24, 0.37] | small | n.s. |
| from 3 vs from 6 | -1.15 | 4 | = 0.763 | -0.32 [-1.17, 0.42] | small | n.s. |
| from 4 vs from 5 | -1.68 | 4 | = 0.763 | -0.95 [-1.84, -0.11] | large | n.s. |
| from 4 vs from 6 | -0.98 | 4 | = 0.763 | -0.54 [-0.79, 0.56] | medium | n.s. |
| from 5 vs from 6 | -0.34 | 4 | = 0.907 | -0.22 [-0.63, 0.57] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 210.49, BIC = 226.23
- Condition effect: *β* = -0.10, *SE* = 0.314, *z* = -0.323, *p* = 0.747

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 2.92, *p* = 0.054, η²_G = 0.086
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -1.49 | 4 | = 0.350 | -0.27 [-0.53, 0.92] | small | n.s. |
| from 2 vs from 4 | 0.79 | 4 | = 0.527 | 0.18 [-1.15, 0.26] | negligible | n.s. |
| from 2 vs from 5 | 0.89 | 4 | = 0.527 | 0.36 [-1.00, 0.20] | small | n.s. |
| from 2 vs from 6 | -2.19 | 4 | = 0.259 | -0.35 [-1.00, 0.25] | small | n.s. |
| from 3 vs from 4 | 4.18 | 4 | = 0.139 | 0.48 [-0.97, 0.71] | small | n.s. |
| from 3 vs from 5 | 2.54 | 4 | = 0.259 | 0.70 [-1.10, 0.47] | medium | n.s. |
| from 3 vs from 6 | -0.58 | 4 | = 0.592 | -0.11 [-0.88, 0.66] | negligible | n.s. |
| from 4 vs from 5 | 0.87 | 4 | = 0.527 | 0.18 [-0.76, 0.67] | negligible | n.s. |
| from 4 vs from 6 | -2.10 | 4 | = 0.259 | -0.54 [-0.71, 0.63] | medium | n.s. |
| from 5 vs from 6 | -1.77 | 4 | = 0.303 | -0.72 [-0.73, 0.48] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 365.41, BIC = 381.15
- Condition effect: *β* = 0.36, *SE* = 0.957, *z* = 0.375, *p* = 0.708


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.51, *p* = 0.732, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.658 (ε = 0.663)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 1.26 | 15 | = 0.751 | 0.17 [-0.23, 0.82] | negligible | n.s. |
| from 2 vs from 4 | 0.23 | 15 | = 0.995 | 0.04 [-0.48, 0.59] | negligible | n.s. |
| from 2 vs from 5 | 1.71 | 15 | = 0.751 | 0.17 [-0.05, 1.04] | negligible | n.s. |
| from 2 vs from 6 | 0.83 | 15 | = 0.882 | 0.18 [-0.26, 0.79] | negligible | n.s. |
| from 3 vs from 4 | -1.27 | 15 | = 0.751 | -0.14 [-0.91, 0.16] | negligible | n.s. |
| from 3 vs from 5 | -0.01 | 15 | = 0.995 | -0.00 [-0.53, 0.53] | negligible | n.s. |
| from 3 vs from 6 | 0.01 | 15 | = 0.995 | 0.00 [-0.52, 0.50] | negligible | n.s. |
| from 4 vs from 5 | 0.71 | 15 | = 0.882 | 0.14 [-0.45, 0.58] | negligible | n.s. |
| from 4 vs from 6 | 0.64 | 15 | = 0.882 | 0.15 [-0.34, 0.66] | negligible | n.s. |
| from 5 vs from 6 | 0.02 | 15 | = 0.995 | 0.00 [-0.39, 0.60] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 339.46, BIC = 357.12
- Condition effect: *β* = -0.43, *SE* = 0.350, *z* = -1.241, *p* = 0.215

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.32, *p* = 0.273, η²_G = 0.034
- Greenhouse-Geisser corrected: *p* = 0.282 (ε = 0.568)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -1.28 | 15 | = 0.548 | -0.35 [-0.94, 0.13] | small | n.s. |
| from 2 vs from 4 | -4.07 | 15 | = 0.010 | -0.53 [-1.67, -0.36] | medium | * |
| from 2 vs from 5 | -0.09 | 15 | = 0.930 | -0.02 [-0.65, 0.38] | negligible | n.s. |
| from 2 vs from 6 | -0.87 | 15 | = 0.661 | -0.17 [-0.80, 0.25] | negligible | n.s. |
| from 3 vs from 4 | -0.69 | 15 | = 0.713 | -0.19 [-0.74, 0.30] | negligible | n.s. |
| from 3 vs from 5 | 1.54 | 15 | = 0.484 | 0.36 [-0.17, 0.94] | small | n.s. |
| from 3 vs from 6 | 0.32 | 15 | = 0.836 | 0.10 [-0.45, 0.57] | negligible | n.s. |
| from 4 vs from 5 | 2.11 | 15 | = 0.258 | 0.55 [0.04, 1.15] | medium | n.s. |
| from 4 vs from 6 | 1.10 | 15 | = 0.576 | 0.24 [-0.23, 0.78] | small | n.s. |
| from 5 vs from 6 | -0.56 | 15 | = 0.727 | -0.16 [-0.66, 0.34] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 709.49, BIC = 727.14
- Condition effect: *β* = 5.26, *SE* = 2.894, *z* = 1.817, *p* = 0.069


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.037). Post-hoc tests revealed:
  - from 3 showed smaller latency than from 5 (*d* = -0.42)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.054)

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
