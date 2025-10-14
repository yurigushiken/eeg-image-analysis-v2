# Statistical Analysis Report: tables

**Generated:** 2025-10-13 23:13:17

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
| 1 to 2 | 21 | 168.00 ms | 15.18 | 3.31 | [144.00, 196.00] |
| 2 to 3 | 22 | 171.09 ms | 18.64 | 3.97 | [140.00, 204.00] |
| 3 to 4 | 22 | 164.18 ms | 16.54 | 3.53 | [140.00, 204.00] |
| 4 to 5 | 23 | 166.78 ms | 19.24 | 4.01 | [140.00, 204.00] |
| 5 to 6 | 22 | 173.82 ms | 17.14 | 3.65 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | -5.63 µV | 2.29 | 0.50 | [-9.95, -2.19] |
| 2 to 3 | 22 | -5.26 µV | 1.96 | 0.42 | [-10.61, -0.91] |
| 3 to 4 | 22 | -5.67 µV | 2.24 | 0.48 | [-10.31, -2.95] |
| 4 to 5 | 23 | -5.78 µV | 2.73 | 0.57 | [-11.05, -1.20] |
| 5 to 6 | 22 | -6.17 µV | 2.42 | 0.52 | [-11.88, -2.32] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 99.38 ms | 11.18 | 3.10 | [84.00, 112.00] |
| 2 to 3 | 11 | 102.55 ms | 9.51 | 2.87 | [84.00, 112.00] |
| 3 to 4 | 16 | 97.75 ms | 11.68 | 2.92 | [84.00, 112.00] |
| 4 to 5 | 14 | 102.29 ms | 9.11 | 2.43 | [84.00, 112.00] |
| 5 to 6 | 12 | 96.00 ms | 9.50 | 2.74 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 2.14 µV | 1.54 | 0.43 | [0.56, 4.57] |
| 2 to 3 | 11 | 3.17 µV | 1.75 | 0.53 | [0.75, 6.87] |
| 3 to 4 | 16 | 3.26 µV | 1.82 | 0.45 | [0.56, 7.39] |
| 4 to 5 | 14 | 3.80 µV | 3.17 | 0.85 | [1.14, 13.41] |
| 5 to 6 | 12 | 2.67 µV | 1.18 | 0.34 | [0.84, 4.39] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 489.41 ms | 36.71 | 8.90 | [440.00, 536.00] |
| 2 to 3 | 18 | 483.56 ms | 42.06 | 9.91 | [432.00, 536.00] |
| 3 to 4 | 17 | 490.82 ms | 37.97 | 9.21 | [432.00, 536.00] |
| 4 to 5 | 16 | 495.25 ms | 36.05 | 9.01 | [436.00, 536.00] |
| 5 to 6 | 9 | 485.78 ms | 36.83 | 12.28 | [448.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 5.48 µV | 3.09 | 0.75 | [1.68, 11.52] |
| 2 to 3 | 18 | 5.84 µV | 3.58 | 0.84 | [1.73, 13.70] |
| 3 to 4 | 17 | 6.01 µV | 3.17 | 0.77 | [1.82, 12.86] |
| 4 to 5 | 16 | 6.00 µV | 3.96 | 0.99 | [1.66, 16.10] |
| 5 to 6 | 9 | 4.78 µV | 2.65 | 0.88 | [1.73, 9.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 918.94, BIC = 937.84
- Condition effect: *β* = 3.16, *SE* = 3.832, *z* = 0.824, *p* = 0.410

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 464.03, BIC = 482.93
- Condition effect: *β* = 0.49, *SE* = 0.468, *z* = 1.049, *p* = 0.294


### 3.2 P1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 502.77, BIC = 518.09
- Condition effect: *β* = 2.92, *SE* = 3.749, *z* = 0.778, *p* = 0.437

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 288.17, BIC = 303.50
- Condition effect: *β* = 0.99, *SE* = 0.734, *z* = 1.353, *p* = 0.176


### 3.3 P3b Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 788.33, BIC = 804.74
- Condition effect: *β* = -5.86, *SE* = 12.501, *z* = -0.468, *p* = 0.639

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 398.03, BIC = 414.43
- Condition effect: *β* = 0.68, *SE* = 0.846, *z* = 0.807, *p* = 0.420


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
