# Statistical Analysis Report: tables

**Generated:** 2025-10-14 00:15:24

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
| 2 to 1 | 16 | 180.50 ms | 11.85 | 2.96 | [160.00, 204.00] |
| 3 to 1 | 22 | 181.64 ms | 13.50 | 2.88 | [160.00, 204.00] |
| 4 to 1 | 20 | 184.80 ms | 11.06 | 2.47 | [168.00, 204.00] |
| Cardinality1 | 16 | 181.75 ms | 13.70 | 3.42 | [160.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | -4.98 µV | 2.67 | 0.67 | [-10.79, -1.30] |
| 3 to 1 | 22 | -4.16 µV | 2.53 | 0.54 | [-10.41, -1.36] |
| 4 to 1 | 20 | -3.95 µV | 1.85 | 0.41 | [-8.09, -0.51] |
| Cardinality1 | 16 | -4.44 µV | 2.20 | 0.55 | [-9.64, -0.89] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 125.05 ms | 13.59 | 3.12 | [100.00, 144.00] |
| 3 to 1 | 22 | 120.00 ms | 14.02 | 2.99 | [100.00, 144.00] |
| 4 to 1 | 16 | 122.25 ms | 10.43 | 2.61 | [108.00, 144.00] |
| Cardinality1 | 18 | 123.56 ms | 12.11 | 2.85 | [100.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 4.81 µV | 2.24 | 0.51 | [2.23, 9.13] |
| 3 to 1 | 22 | 4.02 µV | 1.91 | 0.41 | [1.37, 9.14] |
| 4 to 1 | 16 | 5.65 µV | 2.75 | 0.69 | [1.45, 13.38] |
| Cardinality1 | 18 | 5.04 µV | 2.87 | 0.68 | [1.65, 13.50] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 496.20 ms | 26.80 | 5.99 | [432.00, 532.00] |
| 3 to 1 | 20 | 480.40 ms | 24.93 | 5.57 | [448.00, 532.00] |
| 4 to 1 | 21 | 486.67 ms | 30.47 | 6.65 | [432.00, 532.00] |
| Cardinality1 | 10 | 480.40 ms | 36.49 | 11.54 | [432.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 5.63 µV | 2.80 | 0.63 | [1.47, 11.08] |
| 3 to 1 | 20 | 5.75 µV | 3.05 | 0.68 | [0.90, 14.34] |
| 4 to 1 | 21 | 5.97 µV | 3.03 | 0.66 | [1.64, 12.03] |
| Cardinality1 | 10 | 3.98 µV | 1.76 | 0.56 | [1.31, 7.06] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.64, *p* = 0.201, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.66 | 10 | = 0.632 | 0.14 [-0.40, 0.71] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.91 | 10 | = 0.255 | -0.27 [-1.26, -0.04] | small | n.s. |
| 2 to 1 vs Cardinality1 | -1.04 | 10 | = 0.487 | -0.22 [-0.81, 0.47] | small | n.s. |
| 3 to 1 vs 4 to 1 | -2.78 | 10 | = 0.118 | -0.43 [-1.05, -0.02] | small | n.s. |
| 3 to 1 vs Cardinality1 | -1.22 | 10 | = 0.487 | -0.37 [-0.83, 0.30] | small | n.s. |
| 4 to 1 vs Cardinality1 | 0.24 | 10 | = 0.816 | 0.06 [-0.47, 0.64] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 561.48, BIC = 575.30
- Condition effect: *β* = -0.02, *SE* = 2.567, *z* = -0.008, *p* = 0.993

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.16, *p* = 0.342, η²_G = 0.055
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -1.13 | 10 | = 0.571 | -0.30 [-0.69, 0.42] | small | n.s. |
| 2 to 1 vs 4 to 1 | -2.08 | 10 | = 0.384 | -0.65 [-1.01, 0.15] | medium | n.s. |
| 2 to 1 vs Cardinality1 | -1.66 | 10 | = 0.384 | -0.50 [-1.22, 0.14] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -0.83 | 10 | = 0.638 | -0.28 [-0.71, 0.27] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.37 | 10 | = 0.794 | -0.16 [-0.59, 0.51] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.27 | 10 | = 0.794 | 0.11 [-0.50, 0.61] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 332.73, BIC = 346.55
- Condition effect: *β* = 0.62, *SE* = 0.610, *z* = 1.024, *p* = 0.306


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.35, *p* = 0.791, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.77 | 14 | = 0.844 | 0.24 [-0.34, 0.63] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.21 | 14 | = 1.000 | 0.07 [-0.48, 0.59] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 0.73 | 14 | = 0.844 | 0.24 [-0.33, 0.67] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.67 | 14 | = 0.844 | -0.20 [-0.71, 0.37] | small | n.s. |
| 3 to 1 vs Cardinality1 | 0.00 | 14 | = 1.000 | 0.00 [-0.46, 0.54] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.59 | 14 | = 0.844 | 0.20 [-0.40, 0.71] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 587.78, BIC = 601.68
- Condition effect: *β* = -3.43, *SE* = 2.915, *z* = -1.178, *p* = 0.239

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.70, *p* = 0.057, η²_G = 0.051
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.31 | 14 | = 0.316 | 0.34 [-0.23, 0.75] | small | n.s. |
| 2 to 1 vs 4 to 1 | -1.67 | 14 | = 0.249 | -0.35 [-0.98, 0.13] | small | n.s. |
| 2 to 1 vs Cardinality1 | -0.48 | 14 | = 0.635 | -0.09 [-0.56, 0.43] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -2.79 | 14 | = 0.086 | -0.66 [-1.25, -0.07] | medium | n.s. |
| 3 to 1 vs Cardinality1 | -1.63 | 14 | = 0.249 | -0.36 [-0.84, 0.18] | small | n.s. |
| 4 to 1 vs Cardinality1 | 0.96 | 14 | = 0.425 | 0.22 [-0.31, 0.81] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 327.66, BIC = 341.56
- Condition effect: *β* = -0.67, *SE* = 0.503, *z* = -1.329, *p* = 0.184


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.93, *p* = 0.441, η²_G = 0.075
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 2.04 | 9 | = 0.430 | 1.04 [0.07, 1.16] | large | n.s. |
| 2 to 1 vs 4 to 1 | 0.98 | 9 | = 0.529 | 0.32 [-0.26, 0.69] | small | n.s. |
| 2 to 1 vs Cardinality1 | 1.16 | 9 | = 0.529 | 0.54 [-0.37, 1.11] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -1.05 | 9 | = 0.529 | -0.43 [-0.64, 0.33] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.24 | 9 | = 0.814 | -0.11 [-0.79, 0.64] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.43 | 9 | = 0.814 | 0.22 [-0.58, 0.85] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 687.10, BIC = 700.67
- Condition effect: *β* = -15.80, *SE* = 8.883, *z* = -1.779, *p* = 0.075

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 6.50, *p* = 0.002, η²_G = 0.221
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.39 | 9 | = 0.239 | 0.42 [-0.53, 0.47] | small | n.s. |
| 2 to 1 vs 4 to 1 | -0.49 | 9 | = 0.638 | -0.13 [-0.73, 0.22] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 4.14 | 9 | = 0.012 | 1.30 [0.33, 2.29] | large | * |
| 3 to 1 vs 4 to 1 | -1.59 | 9 | = 0.219 | -0.52 [-0.58, 0.39] | medium | n.s. |
| 3 to 1 vs Cardinality1 | 2.07 | 9 | = 0.137 | 0.89 [-0.13, 1.44] | large | n.s. |
| 4 to 1 vs Cardinality1 | 3.84 | 9 | = 0.012 | 1.31 [0.27, 2.16] | large | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 337.40, BIC = 350.97
- Condition effect: *β* = 0.14, *SE* = 0.609, *z* = 0.228, *p* = 0.820


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.057)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than Cardinality1 (*d* = 1.30)
  - 4 to 1 showed greater amplitude than Cardinality1 (*d* = 1.31)

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
