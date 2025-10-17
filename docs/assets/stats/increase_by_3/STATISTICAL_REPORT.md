# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:53:06

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
| 1 to 4 | 21 | -4.21 µV | 2.23 | 0.49 | [-9.08, -0.83] |
| 2 to 5 | 24 | -3.39 µV | 2.01 | 0.41 | [-9.78, 0.07] |
| 3 to 6 | 23 | -4.38 µV | 2.29 | 0.48 | [-10.16, -1.49] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 21 | 173.16 ms | 12.04 | 2.63 | [151.09, 201.28] |
| 2 to 5 | 24 | 173.42 ms | 14.13 | 2.88 | [152.79, 205.91] |
| 3 to 6 | 23 | 172.67 ms | 12.42 | 2.59 | [153.07, 199.64] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 14 | 1.67 µV | 0.97 | 0.26 | [0.32, 3.11] |
| 2 to 5 | 13 | 1.28 µV | 1.47 | 0.41 | [0.16, 5.61] |
| 3 to 6 | 12 | 1.89 µV | 1.72 | 0.50 | [0.13, 6.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 14 | 90.79 ms | 7.36 | 1.97 | [75.38, 99.65] |
| 2 to 5 | 13 | 88.07 ms | 10.01 | 2.78 | [73.94, 102.56] |
| 3 to 6 | 12 | 89.45 ms | 9.24 | 2.67 | [73.76, 101.03] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 3.67 µV | 2.74 | 0.61 | [0.42, 10.22] |
| 2 to 5 | 22 | 2.95 µV | 1.95 | 0.42 | [0.08, 6.83] |
| 3 to 6 | 18 | 2.74 µV | 1.68 | 0.40 | [0.47, 6.64] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 443.59 ms | 33.85 | 7.57 | [381.85, 507.35] |
| 2 to 5 | 22 | 442.92 ms | 36.64 | 7.81 | [374.34, 522.06] |
| 3 to 6 | 18 | 448.99 ms | 20.76 | 4.89 | [412.02, 482.72] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.98, *p* = 0.152, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -1.32 | 20 | = 0.301 | -0.23 [-0.75, 0.18] | small | n.s. |
| 1 to 4 vs 3 to 6 | 0.84 | 20 | = 0.412 | 0.18 [-0.28, 0.64] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 1.83 | 20 | = 0.245 | 0.42 [-0.02, 0.89] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 283.79, BIC = 294.88
- Condition effect: *β* = 0.59, *SE* = 0.413, *z* = 1.426, *p* = 0.154

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.20, *p* = 0.816, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.08 | 20 | = 0.935 | 0.01 [-0.44, 0.47] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.56 | 20 | = 0.898 | 0.09 [-0.33, 0.58] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 0.53 | 20 | = 0.898 | 0.07 [-0.50, 0.36] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 510.84, BIC = 521.94
- Condition effect: *β* = -0.62, *SE* = 1.941, *z* = -0.322, *p* = 0.748


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.99, *p* = 0.424, η²_G = 0.150
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.45 | 3 | = 0.682 | -0.38 [-1.30, 0.83] | small | n.s. |
| 1 to 4 vs 3 to 6 | -1.26 | 3 | = 0.445 | -1.04 [-1.23, 0.50] | large | n.s. |
| 2 to 5 vs 3 to 6 | -1.91 | 3 | = 0.445 | -0.45 [-1.67, 0.37] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 143.30, BIC = 151.61
- Condition effect: *β* = -0.33, *SE* = 0.506, *z* = -0.654, *p* = 0.513

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.92, *p* = 0.450, η²_G = 0.167
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 1.32 | 3 | = 0.571 | 0.86 [-0.51, 1.79] | large | n.s. |
| 1 to 4 vs 3 to 6 | 0.72 | 3 | = 0.571 | 0.69 [-0.96, 0.72] | medium | n.s. |
| 2 to 5 vs 3 to 6 | -0.63 | 3 | = 0.571 | -0.36 [-0.88, 0.97] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 285.61, BIC = 293.93
- Condition effect: *β* = -2.17, *SE* = 2.909, *z* = -0.747, *p* = 0.455


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.95, *p* = 0.067, η²_G = 0.059
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 1.32 | 16 | = 0.307 | 0.32 [-0.29, 0.69] | small | n.s. |
| 1 to 4 vs 3 to 6 | 2.46 | 16 | = 0.077 | 0.56 [0.04, 1.16] | medium | n.s. |
| 2 to 5 vs 3 to 6 | 1.05 | 16 | = 0.309 | 0.29 [-0.27, 0.78] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 259.60, BIC = 270.07
- Condition effect: *β* = -0.61, *SE* = 0.485, *z* = -1.251, *p* = 0.211

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.46, *p* = 0.636, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.07 | 16 | = 0.941 | 0.02 [-0.39, 0.57] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | -0.75 | 16 | = 0.700 | -0.26 [-0.70, 0.34] | small | n.s. |
| 2 to 5 vs 3 to 6 | -0.95 | 16 | = 0.700 | -0.32 [-0.75, 0.29] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 591.79, BIC = 602.27
- Condition effect: *β* = -0.95, *SE* = 9.184, *z* = -0.104, *p* = 0.917


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.067)

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
