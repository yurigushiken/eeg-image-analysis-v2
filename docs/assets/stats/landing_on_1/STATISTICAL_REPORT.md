# Statistical Analysis Report: tables

**Generated:** 2025-10-15 16:21:10

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
| 2 to 1 | 16 | -3.03 µV | 2.22 | 0.55 | [-8.83, -0.60] |
| 3 to 1 | 22 | -2.69 µV | 2.30 | 0.49 | [-8.63, 0.06] |
| 4 to 1 | 20 | -2.32 µV | 1.53 | 0.34 | [-6.07, -0.22] |
| Cardinality1 | 16 | -2.62 µV | 2.41 | 0.60 | [-8.67, 0.02] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 181.13 ms | 7.55 | 1.89 | [168.30, 197.67] |
| 3 to 1 | 22 | 182.64 ms | 8.60 | 1.83 | [170.03, 203.49] |
| 4 to 1 | 20 | 183.61 ms | 7.34 | 1.64 | [170.47, 195.68] |
| Cardinality1 | 16 | 180.55 ms | 10.69 | 2.67 | [161.47, 201.34] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 3.20 µV | 2.07 | 0.47 | [0.24, 7.58] |
| 3 to 1 | 22 | 2.09 µV | 1.43 | 0.30 | [0.02, 6.21] |
| 4 to 1 | 16 | 3.78 µV | 2.22 | 0.56 | [0.48, 9.21] |
| Cardinality1 | 18 | 3.11 µV | 2.65 | 0.63 | [0.42, 10.97] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 123.51 ms | 7.58 | 1.74 | [106.89, 136.60] |
| 3 to 1 | 22 | 120.62 ms | 10.22 | 2.18 | [101.03, 138.29] |
| 4 to 1 | 16 | 121.23 ms | 6.20 | 1.55 | [105.91, 128.54] |
| Cardinality1 | 18 | 122.88 ms | 9.09 | 2.14 | [105.02, 141.27] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 3.77 µV | 2.68 | 0.60 | [0.11, 9.98] |
| 3 to 1 | 20 | 4.01 µV | 2.38 | 0.53 | [0.24, 9.51] |
| 4 to 1 | 21 | 4.14 µV | 2.78 | 0.61 | [0.04, 9.14] |
| Cardinality1 | 10 | 1.74 µV | 1.41 | 0.45 | [0.02, 3.73] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 484.48 ms | 15.06 | 3.37 | [449.26, 522.08] |
| 3 to 1 | 20 | 482.02 ms | 12.90 | 2.88 | [464.00, 517.00] |
| 4 to 1 | 21 | 483.84 ms | 14.11 | 3.08 | [460.20, 526.37] |
| Cardinality1 | 10 | 479.21 ms | 27.44 | 8.68 | [432.67, 524.59] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.58, *p* = 0.635, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.02 | 10 | = 0.981 | 0.01 [-0.47, 0.64] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.50 | 10 | = 0.837 | -0.43 [-0.93, 0.22] | small | n.s. |
| 2 to 1 vs Cardinality1 | -0.84 | 10 | = 0.837 | -0.28 [-0.89, 0.40] | small | n.s. |
| 3 to 1 vs 4 to 1 | -1.12 | 10 | = 0.837 | -0.40 [-0.78, 0.20] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.61 | 10 | = 0.837 | -0.27 [-0.70, 0.41] | small | n.s. |
| 4 to 1 vs Cardinality1 | 0.16 | 10 | = 0.981 | 0.07 [-0.55, 0.56] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 320.78, BIC = 334.60
- Condition effect: *β* = 0.13, *SE* = 0.571, *z* = 0.235, *p* = 0.814

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.27, *p* = 0.850, η²_G = 0.009
- Greenhouse-Geisser corrected: *p* = 0.673 (ε = 0.428)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.56 | 10 | = 0.837 | 0.10 [-0.52, 0.58] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.97 | 10 | = 0.837 | -0.18 [-0.99, 0.17] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | -0.21 | 10 | = 0.837 | -0.06 [-0.74, 0.54] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -2.21 | 10 | = 0.312 | -0.31 [-0.90, 0.11] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.38 | 10 | = 0.837 | -0.14 [-0.53, 0.58] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.23 | 10 | = 0.837 | 0.08 [-0.47, 0.64] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 519.12, BIC = 532.94
- Condition effect: *β* = 1.08, *SE* = 2.027, *z* = 0.533, *p* = 0.594


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.91, *p* = 0.046, η²_G = 0.067
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 2.07 | 14 | = 0.173 | 0.62 [-0.04, 0.98] | medium | n.s. |
| 2 to 1 vs 4 to 1 | -1.10 | 14 | = 0.349 | -0.24 [-0.81, 0.27] | small | n.s. |
| 2 to 1 vs Cardinality1 | 0.43 | 14 | = 0.676 | 0.09 [-0.41, 0.59] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -3.08 | 14 | = 0.049 | -0.82 [-1.30, -0.11] | large | * |
| 3 to 1 vs Cardinality1 | -1.47 | 14 | = 0.327 | -0.37 [-0.89, 0.14] | small | n.s. |
| 4 to 1 vs Cardinality1 | 1.10 | 14 | = 0.349 | 0.28 [-0.28, 0.85] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 313.11, BIC = 327.01
- Condition effect: *β* = -1.03, *SE* = 0.471, *z* = -2.189, *p* = 0.029

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.28, *p* = 0.839, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.79 | 14 | = 0.951 | 0.25 [-0.37, 0.60] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.23 | 14 | = 0.951 | 0.08 [-0.47, 0.60] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 0.74 | 14 | = 0.951 | 0.21 [-0.32, 0.68] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.62 | 14 | = 0.951 | -0.19 [-0.65, 0.42] | negligible | n.s. |
| 3 to 1 vs Cardinality1 | -0.06 | 14 | = 0.951 | -0.02 [-0.45, 0.54] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.48 | 14 | = 0.951 | 0.16 [-0.43, 0.68] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 526.16, BIC = 540.06
- Condition effect: *β* = -1.76, *SE* = 1.893, *z* = -0.927, *p* = 0.354


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 6.02, *p* = 0.003, η²_G = 0.275
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.10 | 9 | = 0.360 | 0.37 [-0.55, 0.45] | small | n.s. |
| 2 to 1 vs 4 to 1 | -0.44 | 9 | = 0.671 | -0.16 [-0.67, 0.28] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 3.85 | 9 | = 0.012 | 1.52 [0.27, 2.16] | large | * |
| 3 to 1 vs 4 to 1 | -1.43 | 9 | = 0.282 | -0.51 [-0.55, 0.42] | medium | n.s. |
| 3 to 1 vs Cardinality1 | 2.27 | 9 | = 0.099 | 1.20 [-0.09, 1.52] | large | n.s. |
| 4 to 1 vs Cardinality1 | 3.91 | 9 | = 0.012 | 1.56 [0.29, 2.19] | large | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 331.93, BIC = 345.51
- Condition effect: *β* = 0.22, *SE* = 0.639, *z* = 0.342, *p* = 0.732

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.28, *p* = 0.838, η²_G = 0.019
- Greenhouse-Geisser corrected: *p* = 0.714 (ε = 0.542)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.36 | 9 | = 0.874 | 0.38 [-0.13, 0.90] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.16 | 9 | = 0.874 | 0.06 [-0.47, 0.47] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 0.66 | 9 | = 0.874 | 0.27 [-0.51, 0.93] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.59 | 9 | = 0.874 | -0.25 [-0.64, 0.33] | small | n.s. |
| 3 to 1 vs Cardinality1 | 0.20 | 9 | = 0.874 | 0.09 [-0.65, 0.78] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.55 | 9 | = 0.874 | 0.22 [-0.55, 0.89] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 606.18, BIC = 619.76
- Condition effect: *β* = -2.68, *SE* = 4.775, *z* = -0.561, *p* = 0.575


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.046). Post-hoc tests revealed:
  - 3 to 1 showed smaller amplitude than 4 to 1 (*d* = -0.82)
**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than Cardinality1 (*d* = 1.52)
  - 4 to 1 showed greater amplitude than Cardinality1 (*d* = 1.56)

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
