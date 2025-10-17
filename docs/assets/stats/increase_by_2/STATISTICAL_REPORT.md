# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:52:49

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
| 1 to 3 | 24 | -4.20 µV | 1.77 | 0.36 | [-8.92, -0.90] |
| 2 to 4 | 22 | -4.00 µV | 2.19 | 0.47 | [-10.63, -0.76] |
| 3 to 5 | 22 | -3.32 µV | 2.34 | 0.50 | [-9.69, -0.59] |
| 4 to 6 | 22 | -4.02 µV | 2.10 | 0.45 | [-8.66, -1.11] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 172.28 ms | 10.50 | 2.14 | [150.22, 199.18] |
| 2 to 4 | 22 | 171.97 ms | 10.26 | 2.19 | [150.36, 197.29] |
| 3 to 5 | 22 | 168.87 ms | 13.54 | 2.89 | [143.35, 196.33] |
| 4 to 6 | 22 | 169.93 ms | 10.22 | 2.18 | [146.28, 188.99] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 10 | 1.42 µV | 1.39 | 0.44 | [0.18, 4.77] |
| 2 to 4 | 16 | 1.18 µV | 1.01 | 0.25 | [-0.04, 3.44] |
| 3 to 5 | 14 | 1.61 µV | 1.08 | 0.29 | [0.02, 3.97] |
| 4 to 6 | 13 | 1.58 µV | 1.12 | 0.31 | [0.21, 3.48] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 10 | 91.14 ms | 10.35 | 3.27 | [74.21, 107.03] |
| 2 to 4 | 16 | 93.02 ms | 9.44 | 2.36 | [76.91, 105.44] |
| 3 to 5 | 14 | 91.58 ms | 9.08 | 2.43 | [72.42, 104.36] |
| 4 to 6 | 13 | 93.32 ms | 8.53 | 2.37 | [76.37, 105.80] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 3.92 µV | 3.27 | 0.73 | [0.06, 12.67] |
| 2 to 4 | 18 | 4.46 µV | 3.22 | 0.76 | [0.25, 11.81] |
| 3 to 5 | 17 | 3.73 µV | 2.56 | 0.62 | [0.41, 10.61] |
| 4 to 6 | 18 | 3.34 µV | 2.19 | 0.52 | [0.10, 6.16] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 465.61 ms | 20.20 | 4.52 | [404.70, 494.31] |
| 2 to 4 | 18 | 466.01 ms | 30.96 | 7.30 | [392.38, 510.72] |
| 3 to 5 | 17 | 464.57 ms | 24.07 | 5.84 | [405.85, 513.27] |
| 4 to 6 | 18 | 472.71 ms | 24.78 | 5.84 | [440.50, 528.31] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.62, *p* = 0.194, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.63 | 19 | = 0.643 | -0.19 [-0.55, 0.34] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -1.87 | 19 | = 0.230 | -0.51 [-0.93, -0.00] | medium | n.s. |
| 1 to 3 vs 4 to 6 | -0.90 | 19 | = 0.571 | -0.21 [-0.62, 0.27] | small | n.s. |
| 2 to 4 vs 3 to 5 | -1.25 | 19 | = 0.450 | -0.30 [-0.72, 0.20] | small | n.s. |
| 2 to 4 vs 4 to 6 | -0.08 | 19 | = 0.937 | -0.02 [-0.49, 0.45] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 2.01 | 19 | = 0.230 | 0.29 [0.02, 0.99] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 374.92, BIC = 389.92
- Condition effect: *β* = 0.25, *SE* = 0.444, *z* = 0.567, *p* = 0.570

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.40, *p* = 0.756, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.691 (ε = 0.722)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.67 | 19 | = 0.882 | -0.15 [-0.50, 0.39] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | 0.31 | 19 | = 0.882 | 0.07 [-0.32, 0.57] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | 0.31 | 19 | = 0.882 | 0.06 [-0.31, 0.58] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 0.77 | 19 | = 0.882 | 0.18 [-0.23, 0.69] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 1.11 | 19 | = 0.882 | 0.19 [-0.23, 0.72] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -0.15 | 19 | = 0.882 | -0.02 [-0.46, 0.45] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 662.47, BIC = 677.47
- Condition effect: *β* = 0.27, *SE* = 2.073, *z* = 0.132, *p* = 0.895


### 3.2 P1 Component

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

**Pairwise Comparisons:**

_Pairwise tests could not be computed (insufficient paired samples)._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 168.46, BIC = 180.28
- Condition effect: *β* = -0.30, *SE* = 0.404, *z* = -0.737, *p* = 0.461

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

**Pairwise Comparisons:**

_Pairwise tests could not be computed (insufficient paired samples)._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 394.41, BIC = 406.23
- Condition effect: *β* = 2.41, *SE* = 3.611, *z* = 0.667, *p* = 0.505


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.77, *p* = 0.520, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.41 | 14 | = 0.830 | -0.12 [-0.57, 0.46] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | 0.58 | 14 | = 0.830 | 0.18 [-0.32, 0.72] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | 0.87 | 14 | = 0.797 | 0.24 [-0.24, 0.78] | small | n.s. |
| 2 to 4 vs 3 to 5 | 1.18 | 14 | = 0.768 | 0.33 [-0.21, 0.89] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.57 | 14 | = 0.768 | 0.40 [-0.15, 0.96] | small | n.s. |
| 3 to 5 vs 4 to 6 | 0.21 | 14 | = 0.838 | 0.05 [-0.47, 0.60] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 351.48, BIC = 365.22
- Condition effect: *β* = 0.31, *SE* = 0.669, *z* = 0.468, *p* = 0.640

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.16, *p* = 0.923, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.18 | 14 | = 0.954 | -0.07 [-0.51, 0.52] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.35 | 14 | = 0.954 | -0.11 [-0.55, 0.48] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.82 | 14 | = 0.954 | -0.26 [-0.75, 0.26] | small | n.s. |
| 2 to 4 vs 3 to 5 | -0.06 | 14 | = 0.954 | -0.03 [-0.48, 0.59] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | -0.54 | 14 | = 0.954 | -0.16 [-0.82, 0.26] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -0.43 | 14 | = 0.954 | -0.14 [-0.68, 0.39] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 686.07, BIC = 699.81
- Condition effect: *β* = 0.40, *SE* = 7.955, *z* = 0.050, *p* = 0.960


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
