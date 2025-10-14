# Statistical Analysis Report: tables

**Generated:** 2025-10-13 23:12:46

---

## 1. Analysis Overview

**Total Measurements:** 336
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
| 2 to 1 | 16 | 180.25 ms | 12.00 | 3.00 | [160.00, 204.00] |
| 3 to 2 | 22 | 171.82 ms | 20.56 | 4.38 | [144.00, 204.00] |
| 4 to 3 | 23 | 167.13 ms | 17.64 | 3.68 | [144.00, 204.00] |
| 5 to 4 | 22 | 174.73 ms | 18.74 | 3.99 | [144.00, 204.00] |
| 6 to 5 | 15 | 176.00 ms | 20.34 | 5.25 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | -5.20 µV | 2.57 | 0.64 | [-10.79, -1.72] |
| 3 to 2 | 22 | -6.05 µV | 2.55 | 0.54 | [-10.33, -1.67] |
| 4 to 3 | 23 | -5.90 µV | 2.05 | 0.43 | [-10.53, -2.95] |
| 5 to 4 | 22 | -6.21 µV | 2.96 | 0.63 | [-14.15, -1.51] |
| 6 to 5 | 15 | -7.51 µV | 2.06 | 0.53 | [-10.73, -4.01] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 115.53 ms | 6.62 | 1.60 | [100.00, 120.00] |
| 3 to 2 | 9 | 108.89 ms | 7.42 | 2.47 | [100.00, 120.00] |
| 4 to 3 | 13 | 110.15 ms | 7.94 | 2.20 | [100.00, 120.00] |
| 5 to 4 | 16 | 111.50 ms | 7.14 | 1.78 | [100.00, 120.00] |
| 6 to 5 | 4 | 115.00 ms | 3.83 | 1.91 | [112.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 4.46 µV | 2.44 | 0.59 | [1.50, 9.13] |
| 3 to 2 | 9 | 2.80 µV | 1.91 | 0.64 | [0.54, 6.10] |
| 4 to 3 | 13 | 3.55 µV | 2.03 | 0.56 | [1.27, 7.39] |
| 5 to 4 | 16 | 2.95 µV | 1.80 | 0.45 | [0.70, 6.01] |
| 6 to 5 | 4 | 3.72 µV | 1.85 | 0.93 | [1.90, 6.31] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 507.62 ms | 30.83 | 6.73 | [456.00, 552.00] |
| 3 to 2 | 17 | 497.88 ms | 32.25 | 7.82 | [448.00, 552.00] |
| 4 to 3 | 17 | 506.82 ms | 37.52 | 9.10 | [448.00, 552.00] |
| 5 to 4 | 21 | 500.00 ms | 32.79 | 7.16 | [448.00, 552.00] |
| 6 to 5 | 11 | 521.82 ms | 40.81 | 12.30 | [448.00, 552.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 21 | 6.16 µV | 3.11 | 0.68 | [1.72, 11.08] |
| 3 to 2 | 17 | 7.05 µV | 3.93 | 0.95 | [2.10, 17.81] |
| 4 to 3 | 17 | 6.64 µV | 3.27 | 0.79 | [1.64, 13.83] |
| 5 to 4 | 21 | 6.18 µV | 2.86 | 0.62 | [2.48, 11.69] |
| 6 to 5 | 11 | 6.65 µV | 2.21 | 0.67 | [2.47, 10.24] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 842.32, BIC = 860.41
- Condition effect: *β* = -6.84, *SE* = 4.858, *z* = -1.408, *p* = 0.159

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 441.98, BIC = 460.07
- Condition effect: *β* = -1.22, *SE* = 0.611, *z* = -1.997, *p* = 0.046


### 3.2 P1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 399.10, BIC = 413.65
- Condition effect: *β* = -7.14, *SE* = 2.314, *z* = -3.084, *p* = 0.002

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 254.21, BIC = 268.76
- Condition effect: *β* = -2.06, *SE* = 0.687, *z* = -2.995, *p* = 0.003


### 3.3 P3b Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 866.05, BIC = 883.32
- Condition effect: *β* = -11.41, *SE* = 9.707, *z* = -1.176, *p* = 0.240

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 430.15, BIC = 447.41
- Condition effect: *β* = 0.77, *SE* = 0.708, *z* = 1.083, *p* = 0.279


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
