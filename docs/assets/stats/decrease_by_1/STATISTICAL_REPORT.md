# Statistical Analysis Report: tables

**Generated:** 2025-10-14 00:14:40

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
| 2 to 1 | 16 | 178.75 ms | 10.09 | 2.52 | [160.00, 200.00] |
| 3 to 2 | 23 | 169.04 ms | 17.73 | 3.70 | [144.00, 200.00] |
| 4 to 3 | 22 | 164.36 ms | 15.56 | 3.32 | [144.00, 200.00] |
| 5 to 4 | 23 | 173.04 ms | 18.50 | 3.86 | [144.00, 200.00] |
| 6 to 5 | 24 | 172.00 ms | 19.52 | 3.99 | [144.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | -4.83 µV | 2.80 | 0.70 | [-10.79, -1.30] |
| 3 to 2 | 23 | -5.74 µV | 2.60 | 0.54 | [-10.33, -1.35] |
| 4 to 3 | 22 | -5.64 µV | 2.19 | 0.47 | [-10.04, -2.95] |
| 5 to 4 | 23 | -5.99 µV | 2.77 | 0.58 | [-14.15, -1.72] |
| 6 to 5 | 24 | -5.89 µV | 2.13 | 0.43 | [-10.60, -2.05] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 114.67 ms | 7.51 | 1.77 | [96.00, 120.00] |
| 3 to 2 | 12 | 105.67 ms | 8.77 | 2.53 | [96.00, 120.00] |
| 4 to 3 | 13 | 109.85 ms | 9.18 | 2.55 | [96.00, 120.00] |
| 5 to 4 | 15 | 111.20 ms | 9.59 | 2.48 | [96.00, 120.00] |
| 6 to 5 | 12 | 108.33 ms | 8.94 | 2.58 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 4.27 µV | 2.22 | 0.52 | [2.23, 9.13] |
| 3 to 2 | 12 | 2.43 µV | 1.75 | 0.50 | [0.60, 5.61] |
| 4 to 3 | 13 | 3.50 µV | 2.21 | 0.61 | [0.37, 7.39] |
| 5 to 4 | 15 | 2.96 µV | 1.82 | 0.47 | [0.98, 7.17] |
| 6 to 5 | 12 | 3.26 µV | 2.65 | 0.77 | [0.58, 9.47] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 504.84 ms | 29.65 | 6.80 | [444.00, 544.00] |
| 3 to 2 | 18 | 493.33 ms | 32.58 | 7.68 | [444.00, 544.00] |
| 4 to 3 | 17 | 494.35 ms | 37.98 | 9.21 | [444.00, 544.00] |
| 5 to 4 | 18 | 498.22 ms | 30.96 | 7.30 | [444.00, 544.00] |
| 6 to 5 | 14 | 510.29 ms | 35.25 | 9.42 | [456.00, 544.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 5.98 µV | 2.67 | 0.61 | [1.72, 11.08] |
| 3 to 2 | 18 | 6.48 µV | 4.07 | 0.96 | [2.10, 17.81] |
| 4 to 3 | 17 | 6.04 µV | 3.21 | 0.78 | [1.82, 13.83] |
| 5 to 4 | 18 | 6.09 µV | 3.12 | 0.73 | [1.76, 11.49] |
| 6 to 5 | 14 | 4.52 µV | 2.44 | 0.65 | [1.25, 10.64] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.49, *p* = 0.052, η²_G = 0.076
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.17 | 15 | = 0.156 | 0.63 [-0.03, 1.11] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 3.89 | 15 | = 0.014 | 1.06 [0.33, 1.62] | large | * |
| 2 to 1 vs 5 to 4 | 1.23 | 15 | = 0.393 | 0.35 [-0.24, 0.85] | small | n.s. |
| 2 to 1 vs 6 to 5 | 1.86 | 15 | = 0.205 | 0.51 [-0.09, 1.03] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 1.12 | 15 | = 0.400 | 0.33 [-0.26, 0.63] | small | n.s. |
| 3 to 2 vs 5 to 4 | -0.56 | 15 | = 0.649 | -0.20 [-0.60, 0.27] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -0.11 | 15 | = 0.911 | -0.04 [-0.53, 0.33] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -2.43 | 15 | = 0.141 | -0.51 [-0.96, -0.02] | medium | n.s. |
| 4 to 3 vs 6 to 5 | -1.40 | 15 | = 0.362 | -0.34 [-0.80, 0.12] | small | n.s. |
| 5 to 4 vs 6 to 5 | 0.70 | 15 | = 0.622 | 0.14 [-0.36, 0.50] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 913.18, BIC = 931.95
- Condition effect: *β* = -10.04, *SE* = 4.552, *z* = -2.206, *p* = 0.027

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.63, *p* = 0.043, η²_G = 0.064
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.65 | 15 | = 0.126 | 0.61 [0.07, 1.25] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 2.49 | 15 | = 0.126 | 0.56 [0.04, 1.20] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 2.06 | 15 | = 0.169 | 0.63 [-0.05, 1.08] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 1.97 | 15 | = 0.169 | 0.59 [-0.07, 1.06] | medium | n.s. |
| 3 to 2 vs 4 to 3 | -0.44 | 15 | = 0.929 | -0.10 [-0.55, 0.34] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.15 | 15 | = 0.942 | 0.03 [-0.33, 0.53] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -0.33 | 15 | = 0.929 | -0.08 [-0.37, 0.50] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 0.55 | 15 | = 0.929 | 0.13 [-0.22, 0.68] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.07 | 15 | = 0.942 | 0.02 [-0.25, 0.65] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.52 | 15 | = 0.929 | -0.12 [-0.48, 0.39] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 474.29, BIC = 493.07
- Condition effect: *β* = -1.42, *SE* = 0.556, *z* = -2.544, *p* = 0.011


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.51, *p* = 0.731, η²_G = 0.051
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.74 | 4 | = 1.000 | 0.37 [-0.18, 1.37] | small | n.s. |
| 2 to 1 vs 4 to 3 | 0.56 | 4 | = 1.000 | 0.35 [-0.13, 1.33] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.41 | 4 | = 1.000 | 0.31 [-0.33, 0.98] | small | n.s. |
| 2 to 1 vs 6 to 5 | 1.04 | 4 | = 0.935 | 0.69 [-0.24, 1.29] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.00 | 4 | = 1.000 | 0.00 [-1.24, 0.37] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.00 | 4 | = 1.000 | 0.00 [-1.06, 0.51] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 1.00 | 4 | = 0.935 | 0.35 [-1.20, 0.68] | small | n.s. |
| 4 to 3 vs 5 to 4 | 0.00 | 4 | = 1.000 | 0.00 [-1.07, 0.62] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.50 | 4 | = 0.935 | 0.33 [-0.58, 1.12] | small | n.s. |
| 5 to 4 vs 6 to 5 | 1.50 | 4 | = 0.935 | 0.30 [-0.17, 1.38] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 506.58, BIC = 522.32
- Condition effect: *β* = -9.11, *SE* = 2.818, *z* = -3.232, *p* = 0.001

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.24, *p* = 0.335, η²_G = 0.141
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.71 | 4 | = 0.552 | 1.08 [0.09, 1.81] | large | n.s. |
| 2 to 1 vs 4 to 3 | 0.85 | 4 | = 0.552 | 0.40 [-0.19, 1.25] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.91 | 4 | = 0.552 | 0.62 [-0.21, 1.13] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 0.91 | 4 | = 0.552 | 0.41 [-0.07, 1.54] | small | n.s. |
| 3 to 2 vs 4 to 3 | -1.56 | 4 | = 0.552 | -0.97 [-1.61, 0.13] | large | n.s. |
| 3 to 2 vs 5 to 4 | -1.09 | 4 | = 0.552 | -0.57 [-1.13, 0.45] | medium | n.s. |
| 3 to 2 vs 6 to 5 | -1.14 | 4 | = 0.552 | -0.57 [-1.36, 0.56] | medium | n.s. |
| 4 to 3 vs 5 to 4 | 0.86 | 4 | = 0.552 | 0.32 [-0.55, 1.16] | small | n.s. |
| 4 to 3 vs 6 to 5 | 0.31 | 4 | = 0.794 | 0.11 [-0.55, 1.16] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.28 | 4 | = 0.794 | -0.13 [-0.78, 0.65] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 297.01, BIC = 312.75
- Condition effect: *β* = -2.07, *SE* = 0.597, *z* = -3.466, *p* = 0.001


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.63, *p* = 0.187, η²_G = 0.090
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.10 | 10 | = 0.598 | 0.28 [-0.24, 0.85] | small | n.s. |
| 2 to 1 vs 4 to 3 | 0.55 | 10 | = 0.860 | 0.23 [-0.35, 0.73] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.14 | 10 | = 0.959 | 0.06 [-0.44, 0.59] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | -2.12 | 10 | = 0.200 | -0.67 [-1.01, 0.25] | medium | n.s. |
| 3 to 2 vs 4 to 3 | -0.05 | 10 | = 0.959 | -0.02 [-0.60, 0.51] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.45 | 10 | = 0.860 | -0.20 [-0.75, 0.32] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -2.38 | 10 | = 0.194 | -0.84 [-1.22, 0.14] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.41 | 10 | = 0.860 | -0.16 [-0.71, 0.40] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | -2.47 | 10 | = 0.194 | -0.74 [-1.46, -0.08] | medium | n.s. |
| 5 to 4 vs 6 to 5 | -1.68 | 10 | = 0.312 | -0.65 [-1.07, 0.19] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 844.38, BIC = 861.56
- Condition effect: *β* = -12.27, *SE* = 8.875, *z* = -1.382, *p* = 0.167

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.32, *p* = 0.073, η²_G = 0.130
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.55 | 10 | = 0.832 | -0.23 [-0.68, 0.39] | small | n.s. |
| 2 to 1 vs 4 to 3 | 0.45 | 10 | = 0.832 | 0.14 [-0.44, 0.62] | negligible | n.s. |
| 2 to 1 vs 5 to 4 | 0.28 | 10 | = 0.876 | 0.11 [-0.54, 0.49] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 2.56 | 10 | = 0.142 | 1.16 [0.07, 1.44] | large | n.s. |
| 3 to 2 vs 4 to 3 | 0.89 | 10 | = 0.743 | 0.30 [-0.25, 0.88] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.79 | 10 | = 0.743 | 0.28 [-0.38, 0.69] | small | n.s. |
| 3 to 2 vs 6 to 5 | 2.32 | 10 | = 0.142 | 1.00 [-0.03, 1.38] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.08 | 10 | = 0.935 | -0.03 [-0.59, 0.51] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.68 | 10 | = 0.309 | 0.78 [-0.12, 1.18] | medium | n.s. |
| 5 to 4 vs 6 to 5 | 2.81 | 10 | = 0.142 | 0.84 [0.21, 1.66] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 432.34, BIC = 449.52
- Condition effect: *β* = 0.49, *SE* = 0.780, *z* = 0.629, *p* = 0.529


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Marginal trend toward condition differences (*p* = 0.052)
**N1 amplitude:** Significant main effect of condition (*p* = 0.043) (no significant pairwise comparisons)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.073)

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
