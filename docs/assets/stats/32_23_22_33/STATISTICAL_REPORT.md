# Statistical Analysis Report: tables

**Generated:** 2025-10-14 18:32:39

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
| Cardinality2 | 22 | 174.36 ms | 21.86 | 4.66 | [140.00, 208.00] |
| Cardinality3 | 22 | 167.82 ms | 16.54 | 3.53 | [140.00, 200.00] |
| Decreasing 3 to 2 | 24 | 175.33 ms | 22.28 | 4.55 | [140.00, 208.00] |
| Increasing 2 to 3 | 22 | 171.45 ms | 19.33 | 4.12 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 22 | -5.75 µV | 2.52 | 0.54 | [-10.78, -1.57] |
| Cardinality3 | 22 | -5.19 µV | 2.03 | 0.43 | [-10.83, -1.55] |
| Decreasing 3 to 2 | 24 | -5.77 µV | 2.55 | 0.52 | [-10.33, -1.35] |
| Increasing 2 to 3 | 22 | -5.27 µV | 1.96 | 0.42 | [-10.61, -0.91] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 13 | 111.69 ms | 8.40 | 2.33 | [100.00, 120.00] |
| Cardinality3 | 15 | 111.47 ms | 7.98 | 2.06 | [100.00, 120.00] |
| Decreasing 3 to 2 | 11 | 108.36 ms | 6.80 | 2.05 | [100.00, 120.00] |
| Increasing 2 to 3 | 14 | 111.14 ms | 8.76 | 2.34 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 13 | 3.04 µV | 1.79 | 0.50 | [1.11, 7.57] |
| Cardinality3 | 15 | 3.02 µV | 2.39 | 0.62 | [0.79, 8.96] |
| Decreasing 3 to 2 | 11 | 2.54 µV | 1.70 | 0.51 | [0.54, 5.61] |
| Increasing 2 to 3 | 14 | 2.77 µV | 1.86 | 0.50 | [0.49, 6.63] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 12 | 461.33 ms | 24.97 | 7.21 | [420.00, 496.00] |
| Cardinality3 | 16 | 467.00 ms | 31.45 | 7.86 | [420.00, 528.00] |
| Decreasing 3 to 2 | 19 | 481.68 ms | 33.02 | 7.58 | [432.00, 528.00] |
| Increasing 2 to 3 | 18 | 478.44 ms | 44.55 | 10.50 | [420.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 12 | 4.50 µV | 2.29 | 0.66 | [1.28, 10.57] |
| Cardinality3 | 16 | 4.51 µV | 2.20 | 0.55 | [1.80, 9.60] |
| Decreasing 3 to 2 | 19 | 6.30 µV | 4.09 | 0.94 | [1.68, 17.81] |
| Increasing 2 to 3 | 18 | 5.85 µV | 3.54 | 0.83 | [1.42, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.67, *p* = 0.577, η²_G = 0.018
- Greenhouse-Geisser corrected: *p* = 0.535 (ε = 0.744)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 1.36 | 19 | = 0.565 | 0.31 [-0.17, 0.78] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -0.09 | 19 | = 0.928 | -0.03 [-0.50, 0.39] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.57 | 19 | = 0.694 | 0.13 [-0.34, 0.60] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.52 | 19 | = 0.565 | -0.35 [-0.69, 0.21] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.65 | 19 | = 0.694 | -0.19 [-0.62, 0.27] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.59 | 19 | = 0.694 | 0.16 [-0.41, 0.48] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 790.52, BIC = 805.52
- Condition effect: *β* = -5.61, *SE* = 4.737, *z* = -1.184, *p* = 0.236

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.90, *p* = 0.445, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.78 | 19 | = 0.621 | -0.16 [-0.65, 0.30] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.79 | 19 | = 0.621 | 0.15 [-0.36, 0.53] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.18 | 19 | = 0.856 | -0.04 [-0.51, 0.43] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 1.67 | 19 | = 0.621 | 0.31 [-0.14, 0.77] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.66 | 19 | = 0.621 | 0.14 [-0.41, 0.48] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -0.97 | 19 | = 0.621 | -0.21 [-0.70, 0.20] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 380.92, BIC = 395.92
- Condition effect: *β* = 0.39, *SE* = 0.458, *z* = 0.843, *p* = 0.399


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.04, *p* = 0.987, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.00 | 5 | = 1.000 | 0.00 [-0.56, 0.88] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.00 | 5 | = 1.000 | 0.00 [-0.88, 0.97] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.29 | 5 | = 1.000 | -0.18 [-0.68, 0.86] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.00 | 5 | = 1.000 | 0.00 [-0.34, 1.28] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.32 | 5 | = 1.000 | -0.16 [-0.72, 0.81] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -0.34 | 5 | = 1.000 | -0.17 [-0.99, 0.86] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 379.72, BIC = 391.54
- Condition effect: *β* = -0.23, *SE* = 2.962, *z* = -0.076, *p* = 0.939

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.22, *p* = 0.884, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.24 | 5 | = 0.822 | -0.13 [-0.96, 0.49] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.40 | 5 | = 0.822 | 0.26 [-0.92, 0.93] | small | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.28 | 5 | = 0.822 | 0.17 [-0.56, 1.00] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.81 | 5 | = 0.822 | 0.33 [-0.58, 0.97] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.59 | 5 | = 0.822 | 0.27 [-0.53, 1.03] | small | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -0.29 | 5 | = 0.822 | -0.11 [-1.34, 0.57] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 227.39, BIC = 239.21
- Condition effect: *β* = 0.15, *SE* = 0.649, *z* = 0.227, *p* = 0.820


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.07, *p* = 0.381, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.16 | 8 | = 0.879 | -0.07 [-0.75, 0.60] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -1.79 | 8 | = 0.482 | -0.80 [-1.21, 0.15] | large | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.42 | 8 | = 0.879 | -0.15 [-0.84, 0.60] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.55 | 8 | = 0.482 | -0.63 [-1.04, 0.13] | medium | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.18 | 8 | = 0.879 | -0.08 [-0.95, 0.29] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 1.20 | 8 | = 0.530 | 0.45 [-0.57, 0.49] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 650.14, BIC = 663.18
- Condition effect: *β* = 2.44, *SE* = 11.230, *z* = 0.217, *p* = 0.828

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 3.70, *p* = 0.025, η²_G = 0.172
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -1.46 | 8 | = 0.256 | -0.41 [-0.99, 0.38] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -2.53 | 8 | = 0.109 | -0.95 [-1.32, 0.07] | large | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -2.51 | 8 | = 0.109 | -0.97 [-1.80, -0.08] | large | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.59 | 8 | = 0.256 | -0.70 [-0.95, 0.20] | medium | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -1.35 | 8 | = 0.256 | -0.64 [-0.84, 0.38] | medium | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 1.11 | 8 | = 0.300 | 0.22 [-0.18, 0.92] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 333.98, BIC = 347.02
- Condition effect: *β* = 0.77, *SE* = 0.947, *z* = 0.815, *p* = 0.415


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.025) (no significant pairwise comparisons)

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
