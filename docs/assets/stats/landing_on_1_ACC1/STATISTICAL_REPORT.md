# Statistical Analysis Report: tables

**Generated:** 2025-10-14 02:12:07

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
| 2 to 1 | 17 | 180.71 ms | 12.18 | 2.96 | [160.00, 208.00] |
| 3 to 1 | 20 | 183.80 ms | 14.71 | 3.29 | [156.00, 208.00] |
| 4 to 1 | 20 | 187.00 ms | 11.81 | 2.64 | [168.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | -4.97 µV | 2.74 | 0.67 | [-10.79, -0.76] |
| 3 to 1 | 20 | -4.82 µV | 2.66 | 0.60 | [-10.41, -1.40] |
| 4 to 1 | 20 | -4.11 µV | 2.05 | 0.46 | [-9.44, -0.51] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 123.11 ms | 12.08 | 2.85 | [100.00, 140.00] |
| 3 to 1 | 20 | 122.00 ms | 12.88 | 2.88 | [100.00, 144.00] |
| 4 to 1 | 16 | 121.50 ms | 10.42 | 2.60 | [108.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 4.93 µV | 2.36 | 0.56 | [1.50, 9.13] |
| 3 to 1 | 20 | 4.27 µV | 1.86 | 0.42 | [1.64, 9.14] |
| 4 to 1 | 16 | 5.91 µV | 2.60 | 0.65 | [2.46, 13.38] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 488.95 ms | 27.65 | 6.03 | [432.00, 524.00] |
| 3 to 1 | 20 | 477.80 ms | 21.38 | 4.78 | [444.00, 520.00] |
| 4 to 1 | 20 | 486.80 ms | 30.58 | 6.84 | [432.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 5.72 µV | 3.28 | 0.72 | [1.47, 11.08] |
| 3 to 1 | 20 | 6.09 µV | 3.19 | 0.71 | [2.44, 16.27] |
| 4 to 1 | 20 | 6.42 µV | 3.21 | 0.72 | [1.12, 12.03] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 4.51, *p* = 0.021, η²_G = 0.058
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -0.60 | 13 | = 0.557 | -0.09 [-0.85, 0.24] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -2.27 | 13 | = 0.061 | -0.55 [-1.28, -0.06] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -2.43 | 13 | = 0.061 | -0.46 [-0.92, 0.12] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 434.17, BIC = 444.39
- Condition effect: *β* = 3.51, *SE* = 2.337, *z* = 1.503, *p* = 0.133

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.69, *p* = 0.204, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -0.52 | 13 | = 0.609 | -0.12 [-0.55, 0.51] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -2.11 | 13 | = 0.164 | -0.50 [-1.06, 0.11] | small | n.s. |
| 3 to 1 vs 4 to 1 | -1.10 | 13 | = 0.435 | -0.33 [-0.88, 0.15] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 256.96, BIC = 267.18
- Condition effect: *β* = 0.00, *SE* = 0.540, *z* = 0.002, *p* = 0.999


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.20, *p* = 0.823, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -0.24 | 14 | = 0.815 | -0.07 [-0.46, 0.53] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.72 | 14 | = 0.815 | -0.17 [-0.74, 0.37] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.36 | 14 | = 0.815 | -0.10 [-0.69, 0.38] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 417.36, BIC = 427.30
- Condition effect: *β* = -0.77, *SE* = 2.687, *z* = -0.285, *p* = 0.776

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 5.07, *p* = 0.013, η²_G = 0.106
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.77 | 14 | = 0.453 | 0.24 [-0.31, 0.69] | small | n.s. |
| 2 to 1 vs 4 to 1 | -2.56 | 14 | = 0.034 | -0.53 [-1.27, -0.05] | medium | * |
| 3 to 1 vs 4 to 1 | -3.13 | 14 | = 0.022 | -0.80 [-1.31, -0.12] | large | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 238.09, BIC = 248.03
- Condition effect: *β* = -0.52, *SE* = 0.525, *z* = -0.993, *p* = 0.321


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.47, *p* = 0.626, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.05 | 16 | = 0.750 | 0.36 [-0.18, 0.81] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.30 | 16 | = 0.765 | 0.10 [-0.45, 0.52] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.69 | 16 | = 0.750 | -0.20 [-0.75, 0.26] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 581.02, BIC = 591.57
- Condition effect: *β* = -11.06, *SE* = 7.867, *z* = -1.406, *p* = 0.160

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.41, *p* = 0.664, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.10 | 16 | = 0.918 | 0.03 [-0.54, 0.43] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.86 | 16 | = 0.725 | -0.21 [-0.71, 0.26] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.72 | 16 | = 0.725 | -0.23 [-0.63, 0.37] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 315.40, BIC = 325.96
- Condition effect: *β* = 0.32, *SE* = 0.779, *z* = 0.408, *p* = 0.683


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.021) (no significant pairwise comparisons)
**P1 amplitude:** Significant main effect of condition (*p* = 0.013). Post-hoc tests revealed:
  - 2 to 1 showed smaller amplitude than 4 to 1 (*d* = -0.53)
  - 3 to 1 showed smaller amplitude than 4 to 1 (*d* = -0.80)

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
