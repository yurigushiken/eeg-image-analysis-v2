# Statistical Analysis Report: tables

**Generated:** 2025-10-14 11:33:21

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 3 to 2 | 22 | 174.91 ms | 25.03 | 5.34 | [140.00, 216.00] |
| 4 to 2 | 24 | 178.50 ms | 15.33 | 3.13 | [148.00, 212.00] |
| 5 to 2 | 24 | 174.33 ms | 18.72 | 3.82 | [148.00, 216.00] |
| increasing 1 to 2 | 22 | 171.64 ms | 17.84 | 3.80 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 22 | -6.18 µV | 2.54 | 0.54 | [-10.33, -1.71] |
| 4 to 2 | 24 | -6.17 µV | 3.05 | 0.62 | [-12.20, -2.20] |
| 5 to 2 | 24 | -7.00 µV | 3.00 | 0.61 | [-11.72, -1.41] |
| increasing 1 to 2 | 22 | -5.81 µV | 2.14 | 0.46 | [-10.03, -2.38] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 9 | 111.56 ms | 6.77 | 2.26 | [104.00, 120.00] |
| 4 to 2 | 14 | 116.00 ms | 5.66 | 1.51 | [104.00, 120.00] |
| 5 to 2 | 16 | 113.00 ms | 7.23 | 1.81 | [104.00, 120.00] |
| increasing 1 to 2 | 11 | 112.73 ms | 7.34 | 2.21 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 9 | 2.74 µV | 1.87 | 0.62 | [0.51, 6.10] |
| 4 to 2 | 14 | 2.76 µV | 1.19 | 0.32 | [0.45, 4.59] |
| 5 to 2 | 16 | 3.08 µV | 1.56 | 0.39 | [0.75, 6.20] |
| increasing 1 to 2 | 11 | 1.75 µV | 0.80 | 0.24 | [0.48, 3.14] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 490.00 ms | 32.12 | 7.57 | [432.00, 540.00] |
| 4 to 2 | 18 | 484.44 ms | 36.11 | 8.51 | [420.00, 536.00] |
| 5 to 2 | 18 | 477.78 ms | 37.85 | 8.92 | [420.00, 540.00] |
| increasing 1 to 2 | 17 | 481.41 ms | 43.45 | 10.54 | [420.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 6.73 µV | 4.05 | 0.96 | [2.10, 17.81] |
| 4 to 2 | 18 | 6.00 µV | 3.62 | 0.85 | [0.66, 14.41] |
| 5 to 2 | 18 | 5.90 µV | 2.71 | 0.64 | [3.15, 13.53] |
| increasing 1 to 2 | 17 | 5.80 µV | 2.98 | 0.72 | [1.85, 11.52] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.88, *p* = 0.459, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -1.27 | 19 | = 0.441 | -0.32 [-0.53, 0.36] | small | n.s. |
| 3 to 2 vs 5 to 2 | -0.03 | 19 | = 0.975 | -0.01 [-0.42, 0.46] | negligible | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.31 | 19 | = 0.914 | 0.07 [-0.40, 0.54] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.28 | 19 | = 0.441 | 0.38 [-0.24, 0.61] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.69 | 19 | = 0.441 | 0.48 [-0.07, 0.85] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.32 | 19 | = 0.914 | 0.10 [-0.44, 0.44] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 805.37, BIC = 820.50
- Condition effect: *β* = 2.98, *SE* = 4.679, *z* = 0.637, *p* = 0.524

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.58, *p* = 0.062, η²_G = 0.039
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.76 | 19 | = 0.458 | 0.16 [-0.34, 0.55] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.95 | 19 | = 0.197 | 0.40 [0.01, 0.94] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.84 | 19 | = 0.458 | -0.13 [-0.66, 0.28] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.04 | 19 | = 0.458 | 0.22 [-0.13, 0.74] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | -1.33 | 19 | = 0.400 | -0.28 [-0.66, 0.24] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -2.98 | 19 | = 0.046 | -0.55 [-1.00, -0.06] | medium | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 412.78, BIC = 427.91
- Condition effect: *β* = -0.19, *SE* = 0.492, *z* = -0.382, *p* = 0.702


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.20, *p* = 0.351, η²_G = 0.098
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -0.49 | 4 | = 0.749 | -0.28 [-1.36, 0.56] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.20 | 4 | = 0.596 | 0.57 [-0.45, 1.54] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.34 | 4 | = 0.749 | 0.11 [-0.91, 1.20] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.87 | 4 | = 0.596 | 0.84 [0.10, 1.69] | large | n.s. |
| 4 to 2 vs increasing 1 to 2 | 0.65 | 4 | = 0.749 | 0.35 [-0.43, 1.16] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -1.37 | 4 | = 0.596 | -0.40 [-2.20, -0.19] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 325.84, BIC = 337.31
- Condition effect: *β* = 2.80, *SE* = 1.798, *z* = 1.558, *p* = 0.119

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.98, *p* = 0.170, η²_G = 0.229
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -0.44 | 4 | = 0.684 | -0.34 [-0.89, 0.96] | small | n.s. |
| 3 to 2 vs 5 to 2 | -2.17 | 4 | = 0.288 | -0.62 [-1.71, 0.35] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.68 | 4 | = 0.317 | 0.63 [-0.72, 1.44] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -0.61 | 4 | = 0.684 | -0.40 [-1.10, 0.30] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.49 | 4 | = 0.317 | 1.24 [-0.29, 1.35] | large | n.s. |
| 5 to 2 vs increasing 1 to 2 | 2.71 | 4 | = 0.288 | 1.31 [0.17, 2.17] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 180.81, BIC = 192.28
- Condition effect: *β* = 0.04, *SE* = 0.519, *z* = 0.083, *p* = 0.934


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.34, *p* = 0.280, η²_G = 0.069
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.05 | 10 | = 0.965 | 0.01 [-0.42, 0.65] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.09 | 10 | = 0.451 | 0.39 [-0.26, 0.82] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.71 | 10 | = 0.435 | 0.59 [-0.33, 0.90] | medium | n.s. |
| 4 to 2 vs 5 to 2 | 1.14 | 10 | = 0.451 | 0.39 [-0.20, 0.89] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.58 | 10 | = 0.435 | 0.59 [-0.34, 0.89] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.46 | 10 | = 0.786 | 0.22 [-0.55, 0.61] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 717.02, BIC = 730.60
- Condition effect: *β* = -4.22, *SE* = 10.144, *z* = -0.416, *p* = 0.677

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.78, *p* = 0.058, η²_G = 0.068
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 1.32 | 10 | = 0.430 | 0.35 [-0.28, 0.80] | small | n.s. |
| 3 to 2 vs 5 to 2 | 3.07 | 10 | = 0.035 | 0.50 [-0.13, 0.98] | medium | * |
| 3 to 2 vs increasing 1 to 2 | 3.33 | 10 | = 0.035 | 0.71 [-0.29, 0.96] | medium | * |
| 4 to 2 vs 5 to 2 | 0.39 | 10 | = 0.702 | 0.11 [-0.38, 0.70] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 0.96 | 10 | = 0.430 | 0.31 [-0.36, 0.87] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 1.00 | 10 | = 0.430 | 0.24 [-0.47, 0.69] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 354.24, BIC = 367.82
- Condition effect: *β* = -0.53, *SE* = 0.701, *z* = -0.762, *p* = 0.446


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.062)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.058)

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
