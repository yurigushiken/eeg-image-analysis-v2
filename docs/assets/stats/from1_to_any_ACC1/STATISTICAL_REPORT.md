# Statistical Analysis Report: tables

**Generated:** 2025-10-14 00:15:00

---

## 1. Analysis Overview

**Total Measurements:** 216
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| 1 to 2 | 22 | 171.64 ms | 17.84 | 3.80 | [144.00, 208.00] |
| 1 to 3 | 24 | 170.00 ms | 24.57 | 5.02 | [136.00, 216.00] |
| 1 to 4 | 21 | 171.62 ms | 20.74 | 4.53 | [136.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | -5.81 µV | 2.14 | 0.46 | [-10.03, -2.38] |
| 1 to 3 | 24 | -6.37 µV | 2.63 | 0.54 | [-12.53, -2.34] |
| 1 to 4 | 21 | -7.07 µV | 2.85 | 0.62 | [-13.14, -2.90] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 87.33 ms | 10.76 | 3.11 | [68.00, 100.00] |
| 1 to 3 | 9 | 84.00 ms | 11.49 | 3.83 | [72.00, 100.00] |
| 1 to 4 | 15 | 92.00 ms | 8.28 | 2.14 | [80.00, 100.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 2.58 µV | 1.32 | 0.38 | [0.62, 4.29] |
| 1 to 3 | 9 | 3.15 µV | 2.00 | 0.67 | [1.64, 7.47] |
| 1 to 4 | 15 | 2.72 µV | 1.22 | 0.32 | [0.81, 4.28] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 448.75 ms | 55.35 | 13.84 | [368.00, 536.00] |
| 1 to 3 | 20 | 451.00 ms | 44.18 | 9.88 | [368.00, 516.00] |
| 1 to 4 | 20 | 461.80 ms | 57.09 | 12.77 | [376.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 6.10 µV | 2.84 | 0.71 | [2.09, 11.99] |
| 1 to 3 | 20 | 6.49 µV | 3.60 | 0.81 | [1.71, 14.25] |
| 1 to 4 | 20 | 6.17 µV | 3.19 | 0.71 | [2.01, 13.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.97, *p* = 0.387, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.88 | 18 | = 0.588 | 0.18 [-0.40, 0.49] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.51 | 18 | = 0.613 | -0.12 [-0.60, 0.37] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.41 | 18 | = 0.525 | -0.27 [-0.78, 0.16] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 585.79, BIC = 596.81
- Condition effect: *β* = -1.03, *SE* = 3.935, *z* = -0.262, *p* = 0.793

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.71, *p* = 0.195, η²_G = 0.021
- Greenhouse-Geisser corrected: *p* = 0.204 (ε = 0.716)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 1.66 | 18 | = 0.171 | 0.21 [-0.12, 0.79] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.73 | 18 | = 0.171 | 0.35 [-0.10, 0.90] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.66 | 18 | = 0.518 | 0.14 [-0.30, 0.61] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 292.81, BIC = 303.83
- Condition effect: *β* = -0.47, *SE* = 0.423, *z* = -1.121, *p* = 0.262


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 5.83, *p* = 0.065, η²_G = 0.604
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.52 | 2 | = 0.191 | 1.37 [-0.70, 1.48] | large | n.s. |
| 1 to 2 vs 1 to 4 | -0.76 | 2 | = 0.525 | -0.67 [-1.60, 0.41] | medium | n.s. |
| 1 to 3 vs 1 to 4 | -6.05 | 2 | = 0.079 | -4.62 [-1.67, 0.58] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 274.70, BIC = 282.62
- Condition effect: *β* = -3.27, *SE* = 4.211, *z* = -0.778, *p* = 0.437

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.18, *p* = 0.229, η²_G = 0.140
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.84 | 2 | = 0.312 | -0.41 [-1.59, 0.63] | small | n.s. |
| 1 to 2 vs 1 to 4 | -2.23 | 2 | = 0.312 | -0.75 [-1.70, 0.35] | medium | n.s. |
| 1 to 3 vs 1 to 4 | -0.83 | 2 | = 0.493 | -0.44 [-1.75, 0.54] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 137.01, BIC = 144.93
- Condition effect: *β* = 0.61, *SE* = 0.616, *z* = 0.982, *p* = 0.326


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.89, *p* = 0.422, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.97 | 13 | = 0.527 | -0.35 [-0.85, 0.33] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.22 | 13 | = 0.527 | -0.41 [-0.72, 0.39] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.35 | 13 | = 0.733 | -0.12 [-0.70, 0.28] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 608.85, BIC = 618.98
- Condition effect: *β* = 2.37, *SE* = 16.658, *z* = 0.142, *p* = 0.887

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.33, *p* = 0.281, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.39 | 13 | = 0.422 | -0.35 [-0.97, 0.23] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.97 | 13 | = 0.422 | -0.21 [-0.82, 0.31] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.83 | 13 | = 0.422 | 0.14 [-0.34, 0.63] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 273.59, BIC = 283.72
- Condition effect: *β* = 0.92, *SE* = 0.637, *z* = 1.444, *p* = 0.149


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Marginal trend toward condition differences (*p* = 0.065)

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
