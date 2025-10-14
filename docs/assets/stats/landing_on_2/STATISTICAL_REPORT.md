# Statistical Analysis Report: tables

**Generated:** 2025-10-14 18:34:48

---

## 1. Analysis Overview

**Total Measurements:** 360
**Number of Subjects:** 24
**Number of Conditions:** 5

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Latency (Peak), Amplitude (Peak)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** Peak latency within FWHM window
- **Amplitude Measure:** Peak amplitude within FWHM window
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

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 24 | 176.17 ms | 23.07 | 4.71 | [144.00, 212.00] |
| 4 to 2 | 24 | 174.83 ms | 15.22 | 3.11 | [148.00, 212.00] |
| 5 to 2 | 24 | 174.17 ms | 17.61 | 3.60 | [148.00, 212.00] |
| Cardinality2 | 22 | 175.09 ms | 21.91 | 4.67 | [144.00, 212.00] |
| increasing 1 to 2 | 21 | 168.00 ms | 15.18 | 3.31 | [144.00, 196.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 24 | -5.79 µV | 2.54 | 0.52 | [-10.33, -1.35] |
| 4 to 2 | 24 | -6.14 µV | 3.05 | 0.62 | [-11.92, -1.89] |
| 5 to 2 | 24 | -6.56 µV | 3.01 | 0.61 | [-11.17, -1.41] |
| Cardinality2 | 22 | -5.73 µV | 2.50 | 0.53 | [-10.50, -1.57] |
| increasing 1 to 2 | 21 | -5.63 µV | 2.29 | 0.50 | [-9.95, -2.19] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 11 | 110.55 ms | 6.52 | 1.96 | [104.00, 120.00] |
| 4 to 2 | 14 | 116.29 ms | 5.08 | 1.36 | [108.00, 120.00] |
| 5 to 2 | 16 | 113.00 ms | 7.23 | 1.81 | [104.00, 120.00] |
| Cardinality2 | 13 | 112.62 ms | 7.09 | 1.97 | [104.00, 120.00] |
| increasing 1 to 2 | 13 | 112.92 ms | 7.69 | 2.13 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 11 | 2.49 µV | 1.65 | 0.50 | [0.51, 5.61] |
| 4 to 2 | 14 | 2.57 µV | 1.03 | 0.28 | [1.28, 4.31] |
| 5 to 2 | 16 | 3.13 µV | 1.56 | 0.39 | [0.75, 6.20] |
| Cardinality2 | 13 | 2.97 µV | 1.81 | 0.50 | [1.11, 7.57] |
| increasing 1 to 2 | 13 | 1.69 µV | 1.27 | 0.35 | [0.48, 5.23] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 486.00 ms | 33.92 | 8.00 | [432.00, 540.00] |
| 4 to 2 | 19 | 474.74 ms | 38.07 | 8.73 | [420.00, 536.00] |
| 5 to 2 | 19 | 476.63 ms | 37.03 | 8.49 | [420.00, 540.00] |
| Cardinality2 | 11 | 465.82 ms | 33.53 | 10.11 | [420.00, 536.00] |
| increasing 1 to 2 | 17 | 483.06 ms | 44.17 | 10.71 | [420.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 6.50 µV | 4.11 | 0.97 | [2.10, 17.81] |
| 4 to 2 | 19 | 5.47 µV | 3.07 | 0.70 | [1.15, 11.62] |
| 5 to 2 | 19 | 5.67 µV | 2.78 | 0.64 | [2.00, 13.53] |
| Cardinality2 | 11 | 4.56 µV | 2.39 | 0.72 | [1.28, 10.57] |
| increasing 1 to 2 | 17 | 5.58 µV | 3.12 | 0.76 | [1.70, 11.52] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.83, *p* = 0.510, η²_G = 0.023
- Greenhouse-Geisser corrected: *p* = 0.481 (ε = 0.735)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -0.46 | 18 | = 0.811 | -0.11 [-0.36, 0.48] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | -0.11 | 18 | = 0.912 | -0.04 [-0.34, 0.51] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | -0.81 | 18 | = 0.729 | -0.21 [-0.38, 0.51] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.79 | 18 | = 0.729 | 0.21 [-0.30, 0.61] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.35 | 18 | = 0.811 | 0.08 [-0.39, 0.46] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | -0.50 | 18 | = 0.811 | -0.13 [-0.48, 0.41] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.38 | 18 | = 0.729 | 0.38 [-0.11, 0.83] | small | n.s. |
| 5 to 2 vs Cardinality2 | -1.09 | 18 | = 0.729 | -0.20 [-0.42, 0.47] | negligible | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.83 | 18 | = 0.729 | 0.27 [-0.33, 0.58] | small | n.s. |
| Cardinality2 vs increasing 1 to 2 | 1.86 | 18 | = 0.729 | 0.44 [-0.08, 0.93] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 995.81, BIC = 1015.03
- Condition effect: *β* = -1.33, *SE* = 4.408, *z* = -0.302, *p* = 0.762

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.01, *p* = 0.102, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.96 | 18 | = 0.496 | 0.19 [-0.28, 0.57] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.31 | 18 | = 0.414 | 0.27 [-0.12, 0.75] | small | n.s. |
| 3 to 2 vs Cardinality2 | -1.05 | 18 | = 0.496 | -0.21 [-0.55, 0.34] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.53 | 18 | = 0.670 | -0.09 [-0.63, 0.28] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.39 | 18 | = 0.702 | 0.07 [-0.24, 0.61] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | -1.73 | 18 | = 0.337 | -0.40 [-0.65, 0.25] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | -1.33 | 18 | = 0.414 | -0.29 [-0.80, 0.13] | small | n.s. |
| 5 to 2 vs Cardinality2 | -2.21 | 18 | = 0.337 | -0.47 [-0.81, 0.10] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -1.88 | 18 | = 0.337 | -0.37 [-0.94, 0.01] | small | n.s. |
| Cardinality2 vs increasing 1 to 2 | 0.87 | 18 | = 0.496 | 0.15 [-0.29, 0.69] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 509.38, BIC = 528.60
- Condition effect: *β* = -0.35, *SE* = 0.484, *z* = -0.720, *p* = 0.472


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.79, *p* = 0.551, η²_G = 0.073
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -0.21 | 4 | = 0.941 | -0.13 [-1.32, 0.32] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.20 | 4 | = 0.745 | 0.57 [-0.66, 1.03] | medium | n.s. |
| 3 to 2 vs Cardinality2 | 0.00 | 4 | = 1.000 | 0.00 [-0.67, 1.22] | negligible | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.34 | 4 | = 0.941 | 0.11 [-0.80, 1.06] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.63 | 4 | = 0.745 | 0.69 [0.06, 1.63] | medium | n.s. |
| 4 to 2 vs Cardinality2 | 0.41 | 4 | = 0.941 | 0.15 [-0.21, 1.33] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 0.39 | 4 | = 0.941 | 0.22 [-0.37, 1.01] | small | n.s. |
| 5 to 2 vs Cardinality2 | -2.24 | 4 | = 0.745 | -0.63 [-0.84, 0.51] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | -1.37 | 4 | = 0.745 | -0.40 [-1.93, -0.15] | small | n.s. |
| Cardinality2 vs increasing 1 to 2 | 0.25 | 4 | = 0.941 | 0.12 [-0.79, 0.64] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 435.51, BIC = 450.94
- Condition effect: *β* = 4.11, *SE* = 1.844, *z* = 2.227, *p* = 0.026

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.51, *p* = 0.246, η²_G = 0.235
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.09 | 4 | = 0.934 | 0.07 [-0.64, 0.90] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | -2.17 | 4 | = 0.413 | -0.62 [-1.93, 0.07] | medium | n.s. |
| 3 to 2 vs Cardinality2 | -1.02 | 4 | = 0.470 | -0.67 [-0.95, 0.90] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.70 | 4 | = 0.413 | 0.69 [-0.43, 1.55] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -1.21 | 4 | = 0.470 | -0.80 [-1.43, 0.06] | medium | n.s. |
| 4 to 2 vs Cardinality2 | -1.22 | 4 | = 0.470 | -0.78 [-0.81, 0.62] | medium | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.00 | 4 | = 0.470 | 0.87 [-0.28, 1.12] | large | n.s. |
| 5 to 2 vs Cardinality2 | -0.23 | 4 | = 0.921 | -0.17 [-0.71, 0.64] | negligible | n.s. |
| 5 to 2 vs increasing 1 to 2 | 2.63 | 4 | = 0.413 | 1.38 [0.04, 1.72] | large | n.s. |
| Cardinality2 vs increasing 1 to 2 | 1.80 | 4 | = 0.413 | 1.19 [-0.03, 1.60] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 251.40, BIC = 266.83
- Condition effect: *β* = 0.08, *SE* = 0.563, *z* = 0.136, *p* = 0.892


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.45, *p* = 0.771, η²_G = 0.046
- Greenhouse-Geisser corrected: *p* = 0.649 (ε = 0.504)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.38 | 6 | = 0.895 | 0.14 [-0.26, 0.79] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 0.43 | 6 | = 0.895 | 0.18 [-0.29, 0.76] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | 1.42 | 6 | = 0.895 | 0.48 [-0.19, 1.36] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.11 | 6 | = 0.895 | 0.53 [-0.51, 0.65] | medium | n.s. |
| 4 to 2 vs 5 to 2 | 0.03 | 6 | = 0.974 | 0.01 [-0.43, 0.60] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | 1.04 | 6 | = 0.895 | 0.29 [-0.68, 0.75] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 0.57 | 6 | = 0.895 | 0.35 [-0.56, 0.55] | small | n.s. |
| 5 to 2 vs Cardinality2 | 0.56 | 6 | = 0.895 | 0.32 [-0.50, 0.95] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.57 | 6 | = 0.895 | 0.38 [-0.61, 0.50] | small | n.s. |
| Cardinality2 vs increasing 1 to 2 | 0.21 | 6 | = 0.935 | 0.09 [-0.89, 0.65] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 851.90, BIC = 868.91
- Condition effect: *β* = -10.71, *SE* = 10.605, *z* = -1.010, *p* = 0.312

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 5.21, *p* = 0.004, η²_G = 0.174
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 2.18 | 6 | = 0.162 | 0.35 [-0.17, 0.89] | small | n.s. |
| 3 to 2 vs 5 to 2 | 3.01 | 6 | = 0.079 | 0.77 [-0.16, 0.90] | medium | n.s. |
| 3 to 2 vs Cardinality2 | 4.08 | 6 | = 0.033 | 1.26 [-0.12, 1.46] | large | * |
| 3 to 2 vs increasing 1 to 2 | 4.56 | 6 | = 0.033 | 1.06 [-0.20, 0.99] | large | * |
| 4 to 2 vs 5 to 2 | 1.53 | 6 | = 0.252 | 0.30 [-0.43, 0.60] | small | n.s. |
| 4 to 2 vs Cardinality2 | 2.01 | 6 | = 0.162 | 0.72 [-0.18, 1.37] | medium | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.96 | 6 | = 0.162 | 0.55 [-0.36, 0.76] | medium | n.s. |
| 5 to 2 vs Cardinality2 | 1.17 | 6 | = 0.359 | 0.52 [-0.19, 1.36] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | 1.03 | 6 | = 0.382 | 0.31 [-0.47, 0.64] | small | n.s. |
| Cardinality2 vs increasing 1 to 2 | -0.61 | 6 | = 0.567 | -0.22 [-1.16, 0.43] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 404.84, BIC = 421.85
- Condition effect: *β* = -0.81, *SE* = 0.644, *z* = -1.255, *p* = 0.210


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - 3 to 2 showed greater amplitude than Cardinality2 (*d* = 1.26)
  - 3 to 2 showed greater amplitude than increasing 1 to 2 (*d* = 1.06)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

#### Latency

#### Amplitude

### 5.2 P1 Component

#### Latency

#### Amplitude

### 5.3 P3b Component

#### Latency

#### Amplitude

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
