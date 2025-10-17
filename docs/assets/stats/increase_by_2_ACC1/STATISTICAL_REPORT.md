# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:52:58

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
| 1 to 3 | 24 | -3.84 µV | 1.90 | 0.39 | [-8.57, -0.57] |
| 2 to 4 | 22 | -3.85 µV | 2.26 | 0.48 | [-10.63, -0.11] |
| 3 to 5 | 22 | -3.61 µV | 2.30 | 0.49 | [-10.14, -0.59] |
| 4 to 6 | 22 | -4.35 µV | 2.79 | 0.59 | [-12.58, 0.01] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 173.16 ms | 12.10 | 2.47 | [150.22, 202.92] |
| 2 to 4 | 22 | 172.28 ms | 11.72 | 2.50 | [150.36, 207.84] |
| 3 to 5 | 22 | 168.27 ms | 11.53 | 2.46 | [148.43, 196.84] |
| 4 to 6 | 22 | 172.61 ms | 12.07 | 2.57 | [150.60, 206.91] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 12 | 1.47 µV | 1.16 | 0.33 | [0.03, 4.24] |
| 2 to 4 | 16 | 1.43 µV | 1.05 | 0.26 | [-0.04, 3.73] |
| 3 to 5 | 13 | 1.41 µV | 1.10 | 0.30 | [0.16, 3.88] |
| 4 to 6 | 15 | 1.68 µV | 1.34 | 0.34 | [-0.01, 3.91] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 12 | 92.93 ms | 10.86 | 3.14 | [78.55, 107.87] |
| 2 to 4 | 16 | 88.25 ms | 10.97 | 2.74 | [69.59, 104.95] |
| 3 to 5 | 13 | 87.54 ms | 10.99 | 3.05 | [71.31, 104.71] |
| 4 to 6 | 15 | 90.80 ms | 11.54 | 2.98 | [68.35, 106.31] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 4.24 µV | 3.46 | 0.77 | [0.56, 12.22] |
| 2 to 4 | 19 | 4.57 µV | 3.50 | 0.80 | [0.50, 11.96] |
| 3 to 5 | 16 | 3.64 µV | 2.20 | 0.55 | [0.18, 8.05] |
| 4 to 6 | 18 | 3.77 µV | 2.42 | 0.57 | [0.34, 7.73] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 461.35 ms | 20.62 | 4.61 | [404.70, 487.79] |
| 2 to 4 | 19 | 470.87 ms | 28.77 | 6.60 | [408.76, 516.90] |
| 3 to 5 | 16 | 461.97 ms | 23.02 | 5.76 | [405.85, 499.34] |
| 4 to 6 | 18 | 469.16 ms | 26.21 | 6.18 | [414.21, 522.82] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.74, *p* = 0.535, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.38 | 18 | = 0.757 | -0.11 [-0.54, 0.34] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.79 | 18 | = 0.757 | -0.21 [-0.67, 0.22] | small | n.s. |
| 1 to 3 vs 4 to 6 | 0.66 | 18 | = 0.757 | 0.16 [-0.21, 0.69] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -0.31 | 18 | = 0.757 | -0.08 [-0.51, 0.40] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 0.93 | 18 | = 0.757 | 0.23 [-0.35, 0.59] | small | n.s. |
| 3 to 5 vs 4 to 6 | 2.28 | 18 | = 0.210 | 0.30 [0.08, 1.09] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 395.81, BIC = 410.81
- Condition effect: *β* = 0.09, *SE* = 0.506, *z* = 0.177, *p* = 0.860

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.86, *p* = 0.468, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.90 | 18 | = 0.762 | -0.23 [-0.51, 0.38] | small | n.s. |
| 1 to 3 vs 3 to 5 | 0.42 | 18 | = 0.819 | 0.09 [-0.18, 0.72] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.03 | 18 | = 0.977 | -0.00 [-0.32, 0.57] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.42 | 18 | = 0.762 | 0.29 [-0.07, 0.88] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.09 | 18 | = 0.762 | 0.22 [-0.37, 0.57] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.48 | 18 | = 0.819 | -0.09 [-0.54, 0.40] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 665.30, BIC = 680.30
- Condition effect: *β* = 0.04, *SE* = 2.041, *z* = 0.021, *p* = 0.983


### 3.2 P1 Component

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

**Pairwise Comparisons:**

_Pairwise tests could not be computed (insufficient paired samples)._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 181.41, BIC = 193.56
- Condition effect: *β* = 0.02, *SE* = 0.392, *z* = 0.040, *p* = 0.968

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

**Pairwise Comparisons:**

_Pairwise tests could not be computed (insufficient paired samples)._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 433.60, BIC = 445.75
- Condition effect: *β* = -4.39, *SE* = 3.702, *z* = -1.187, *p* = 0.235


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.19, *p* = 0.327, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.27 | 14 | = 0.791 | -0.07 [-0.53, 0.46] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | 1.21 | 14 | = 0.474 | 0.38 [-0.19, 0.91] | small | n.s. |
| 1 to 3 vs 4 to 6 | 0.75 | 14 | = 0.561 | 0.21 [-0.30, 0.71] | small | n.s. |
| 2 to 4 vs 3 to 5 | 1.84 | 14 | = 0.474 | 0.47 [-0.06, 1.07] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.13 | 14 | = 0.474 | 0.30 [-0.24, 0.81] | small | n.s. |
| 3 to 5 vs 4 to 6 | -1.04 | 14 | = 0.474 | -0.23 [-0.83, 0.30] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 356.66, BIC = 370.40
- Condition effect: *β* = 0.20, *SE* = 0.676, *z* = 0.294, *p* = 0.769

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.96, *p* = 0.421, η²_G = 0.047
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.84 | 14 | = 0.522 | -0.60 [-0.80, 0.21] | medium | n.s. |
| 1 to 3 vs 3 to 5 | -0.82 | 14 | = 0.577 | -0.29 [-0.68, 0.39] | small | n.s. |
| 1 to 3 vs 4 to 6 | -0.94 | 14 | = 0.577 | -0.35 [-0.76, 0.25] | small | n.s. |
| 2 to 4 vs 3 to 5 | 0.72 | 14 | = 0.577 | 0.32 [-0.28, 0.80] | small | n.s. |
| 2 to 4 vs 4 to 6 | 0.78 | 14 | = 0.577 | 0.25 [-0.57, 0.46] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.22 | 14 | = 0.830 | -0.07 [-0.61, 0.50] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 684.12, BIC = 697.87
- Condition effect: *β* = 9.52, *SE* = 7.740, *z* = 1.230, *p* = 0.219


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
