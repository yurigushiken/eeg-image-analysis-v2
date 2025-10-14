# Statistical Analysis Report: tables

**Generated:** 2025-10-14 02:11:06

---

## 1. Analysis Overview

**Total Measurements:** 144
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
| Cardinality1 | 15 | 178.13 ms | 18.69 | 4.83 | [148.00, 204.00] |
| Cardinality2 | 22 | 174.91 ms | 19.91 | 4.25 | [148.00, 204.00] |
| Cardinality3 | 23 | 170.26 ms | 16.48 | 3.44 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | -4.87 µV | 1.87 | 0.48 | [-9.64, -2.66] |
| Cardinality2 | 22 | -5.56 µV | 2.42 | 0.52 | [-10.20, -1.57] |
| Cardinality3 | 23 | -5.13 µV | 2.00 | 0.42 | [-10.83, -1.55] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 18 | 119.56 ms | 8.77 | 2.07 | [104.00, 128.00] |
| Cardinality2 | 12 | 117.67 ms | 9.57 | 2.76 | [104.00, 128.00] |
| Cardinality3 | 14 | 115.71 ms | 9.21 | 2.46 | [104.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 18 | 4.78 µV | 2.94 | 0.69 | [1.39, 13.50] |
| Cardinality2 | 12 | 3.37 µV | 1.85 | 0.53 | [1.11, 7.57] |
| Cardinality3 | 14 | 3.23 µV | 2.35 | 0.63 | [0.94, 8.96] |


### 2.3 P3b Component

#### Latency (Peak)

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.95, *p* = 0.399, η²_G = 0.018
- Greenhouse-Geisser corrected: *p* = 0.372 (ε = 0.689)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.15 | 13 | = 0.882 | 0.04 [-0.45, 0.66] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 1.91 | 13 | = 0.234 | 0.33 [-0.10, 1.13] | small | n.s. |
| Cardinality2 vs Cardinality3 | 1.12 | 13 | = 0.425 | 0.25 [-0.16, 0.77] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 510.67, BIC = 521.15
- Condition effect: *β* = -2.25, *SE* = 4.116, *z* = -0.547, *p* = 0.584

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.39, *p* = 0.268, η²_G = 0.047
- Greenhouse-Geisser corrected: *p* = 0.266 (ε = 0.664)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.23 | 13 | = 0.359 | 0.49 [-0.27, 0.86] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.35 | 13 | = 0.359 | 0.41 [-0.24, 0.96] | small | n.s. |
| Cardinality2 vs Cardinality3 | -0.58 | 13 | = 0.574 | -0.12 [-0.66, 0.26] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 264.35, BIC = 274.82
- Condition effect: *β* = -0.85, *SE* = 0.607, *z* = -1.406, *p* = 0.160


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.86, *p* = 0.193, η²_G = 0.106
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.83 | 7 | = 0.435 | 0.36 [-0.81, 0.73] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.77 | 7 | = 0.358 | 0.79 [-0.14, 1.22] | medium | n.s. |
| Cardinality2 vs Cardinality3 | 1.18 | 7 | = 0.416 | 0.42 [-0.47, 1.11] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 325.25, BIC = 334.17
- Condition effect: *β* = -1.26, *SE* = 3.047, *z* = -0.415, *p* = 0.678

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 4.65, *p* = 0.028, η²_G = 0.196
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 4.96 | 7 | = 0.005 | 1.04 [0.07, 1.97] | large | ** |
| Cardinality1 vs Cardinality3 | 1.92 | 7 | = 0.145 | 0.81 [0.07, 1.54] | large | n.s. |
| Cardinality2 vs Cardinality3 | -0.40 | 7 | = 0.701 | -0.18 [-1.00, 0.55] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 206.52, BIC = 215.44
- Condition effect: *β* = -1.88, *SE* = 0.760, *z* = -2.479, *p* = 0.013


### 3.3 P3b Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

_LMM results not available._

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

_LMM results not available._


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.028). Post-hoc tests revealed:
  - Cardinality1 showed greater amplitude than Cardinality2 (*d* = 1.04)

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
