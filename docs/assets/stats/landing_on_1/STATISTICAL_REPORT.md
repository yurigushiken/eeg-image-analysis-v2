# Statistical Analysis Report: tables

**Generated:** 2025-10-13 23:13:37

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

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 561.48, BIC = 575.30
- Condition effect: *β* = -0.02, *SE* = 2.567, *z* = -0.008, *p* = 0.993

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 332.73, BIC = 346.55
- Condition effect: *β* = 0.62, *SE* = 0.610, *z* = 1.024, *p* = 0.306


### 3.2 P1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 587.78, BIC = 601.68
- Condition effect: *β* = -3.43, *SE* = 2.915, *z* = -1.178, *p* = 0.239

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 327.66, BIC = 341.56
- Condition effect: *β* = -0.67, *SE* = 0.503, *z* = -1.329, *p* = 0.184


### 3.3 P3b Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 687.10, BIC = 700.67
- Condition effect: *β* = -15.80, *SE* = 8.883, *z* = -1.779, *p* = 0.075

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 337.40, BIC = 350.97
- Condition effect: *β* = 0.14, *SE* = 0.609, *z* = 0.228, *p* = 0.820


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
