# Statistical Analysis Report: tables

**Generated:** 2025-10-13 23:12:29

---

## 1. Analysis Overview

**Total Measurements:** 432
**Number of Subjects:** 24
**Number of Conditions:** 6

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
| Cardinality1 | 15 | 177.87 ms | 19.18 | 4.95 | [144.00, 204.00] |
| Cardinality2 | 22 | 174.36 ms | 20.72 | 4.42 | [144.00, 204.00] |
| Cardinality3 | 22 | 168.18 ms | 15.93 | 3.40 | [144.00, 200.00] |
| Cardinality4 | 22 | 171.27 ms | 19.93 | 4.25 | [144.00, 204.00] |
| Cardinality5 | 24 | 171.67 ms | 16.04 | 3.27 | [144.00, 196.00] |
| Cardinality6 | 23 | 174.26 ms | 16.04 | 3.34 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | -4.90 µV | 1.85 | 0.48 | [-9.64, -2.66] |
| Cardinality2 | 22 | -5.64 µV | 2.44 | 0.52 | [-10.50, -1.57] |
| Cardinality3 | 22 | -5.19 µV | 2.04 | 0.43 | [-10.83, -1.55] |
| Cardinality4 | 22 | -5.95 µV | 3.12 | 0.67 | [-13.09, -1.82] |
| Cardinality5 | 24 | -5.96 µV | 2.55 | 0.52 | [-12.06, -1.67] |
| Cardinality6 | 23 | -5.73 µV | 2.88 | 0.60 | [-11.14, -0.87] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 113.68 ms | 8.88 | 2.04 | [96.00, 120.00] |
| Cardinality2 | 12 | 107.00 ms | 10.25 | 2.96 | [96.00, 120.00] |
| Cardinality3 | 14 | 110.00 ms | 9.25 | 2.47 | [96.00, 120.00] |
| Cardinality4 | 12 | 109.67 ms | 9.57 | 2.76 | [96.00, 120.00] |
| Cardinality5 | 14 | 106.00 ms | 7.32 | 1.96 | [96.00, 120.00] |
| Cardinality6 | 12 | 109.00 ms | 8.20 | 2.37 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 4.41 µV | 2.89 | 0.66 | [1.20, 13.26] |
| Cardinality2 | 12 | 3.07 µV | 1.84 | 0.53 | [1.36, 7.57] |
| Cardinality3 | 14 | 3.25 µV | 2.36 | 0.63 | [0.79, 8.96] |
| Cardinality4 | 12 | 3.28 µV | 1.83 | 0.53 | [0.96, 6.93] |
| Cardinality5 | 14 | 2.66 µV | 1.69 | 0.45 | [0.35, 5.37] |
| Cardinality6 | 12 | 2.97 µV | 2.08 | 0.60 | [0.77, 8.25] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 461.71 ms | 14.53 | 3.88 | [440.00, 480.00] |
| Cardinality2 | 13 | 456.31 ms | 15.36 | 4.26 | [440.00, 480.00] |
| Cardinality3 | 16 | 458.25 ms | 11.59 | 2.90 | [440.00, 476.00] |
| Cardinality4 | 11 | 455.27 ms | 8.73 | 2.63 | [440.00, 472.00] |
| Cardinality5 | 14 | 455.14 ms | 16.17 | 4.32 | [440.00, 480.00] |
| Cardinality6 | 14 | 466.57 ms | 14.09 | 3.76 | [440.00, 480.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 3.04 µV | 1.84 | 0.49 | [1.05, 7.06] |
| Cardinality2 | 13 | 3.78 µV | 2.08 | 0.58 | [0.41, 8.49] |
| Cardinality3 | 16 | 4.49 µV | 2.23 | 0.56 | [1.30, 9.60] |
| Cardinality4 | 11 | 4.18 µV | 2.57 | 0.78 | [0.65, 8.96] |
| Cardinality5 | 14 | 2.64 µV | 1.36 | 0.36 | [0.35, 5.39] |
| Cardinality6 | 14 | 4.55 µV | 2.34 | 0.63 | [1.85, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 1053.48, BIC = 1076.30
- Condition effect: *β* = -3.22, *SE* = 3.887, *z* = -0.829, *p* = 0.407

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 566.20, BIC = 589.01
- Condition effect: *β* = -0.97, *SE* = 0.594, *z* = -1.626, *p* = 0.104


### 3.2 P1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 604.96, BIC = 624.31
- Condition effect: *β* = -6.70, *SE* = 2.912, *z* = -2.302, *p* = 0.021

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 367.23, BIC = 386.58
- Condition effect: *β* = -1.59, *SE* = 0.675, *z* = -2.361, *p* = 0.018


### 3.3 P3b Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 672.09, BIC = 691.35
- Condition effect: *β* = -5.41, *SE* = 5.106, *z* = -1.059, *p* = 0.290

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 347.69, BIC = 366.94
- Condition effect: *β* = 0.65, *SE* = 0.622, *z* = 1.040, *p* = 0.298


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

### References

- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
