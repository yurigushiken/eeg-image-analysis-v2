# Statistical Analysis Report: tables

**Generated:** 2025-10-13 23:13:29

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
| 1 to 2 | 22 | 171.45 ms | 17.47 | 3.72 | [144.00, 204.00] |
| 2 to 3 | 21 | 168.57 ms | 18.03 | 3.94 | [136.00, 204.00] |
| 3 to 4 | 23 | 166.78 ms | 18.15 | 3.78 | [140.00, 204.00] |
| 4 to 5 | 22 | 167.09 ms | 19.75 | 4.21 | [136.00, 196.00] |
| 5 to 6 | 12 | 169.67 ms | 24.57 | 7.09 | [136.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | -5.80 µV | 2.14 | 0.46 | [-10.03, -2.38] |
| 2 to 3 | 21 | -5.64 µV | 1.80 | 0.39 | [-10.61, -2.59] |
| 3 to 4 | 23 | -5.92 µV | 2.07 | 0.43 | [-10.53, -2.95] |
| 4 to 5 | 22 | -7.36 µV | 3.59 | 0.76 | [-16.53, -2.59] |
| 5 to 6 | 12 | -7.26 µV | 2.89 | 0.83 | [-12.77, -1.43] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 97.23 ms | 13.60 | 3.77 | [84.00, 116.00] |
| 2 to 3 | 11 | 102.18 ms | 13.07 | 3.94 | [84.00, 116.00] |
| 3 to 4 | 15 | 102.13 ms | 10.78 | 2.78 | [84.00, 116.00] |
| 4 to 5 | 15 | 100.53 ms | 9.18 | 2.37 | [84.00, 116.00] |
| 5 to 6 | 13 | 100.62 ms | 10.56 | 2.93 | [84.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 2.26 µV | 1.26 | 0.35 | [0.62, 4.29] |
| 2 to 3 | 11 | 3.61 µV | 1.78 | 0.54 | [1.63, 6.87] |
| 3 to 4 | 15 | 3.39 µV | 1.92 | 0.50 | [1.27, 7.39] |
| 4 to 5 | 15 | 5.60 µV | 5.16 | 1.33 | [1.25, 19.20] |
| 5 to 6 | 13 | 5.69 µV | 4.08 | 1.13 | [1.02, 16.40] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 488.00 ms | 34.41 | 8.35 | [440.00, 536.00] |
| 2 to 3 | 18 | 474.00 ms | 33.13 | 7.81 | [440.00, 536.00] |
| 3 to 4 | 16 | 499.25 ms | 34.39 | 8.60 | [440.00, 536.00] |
| 4 to 5 | 16 | 507.00 ms | 26.31 | 6.58 | [456.00, 536.00] |
| 5 to 6 | 9 | 498.22 ms | 38.01 | 12.67 | [440.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 5.69 µV | 2.95 | 0.72 | [1.78, 11.52] |
| 2 to 3 | 18 | 6.11 µV | 3.49 | 0.82 | [1.82, 13.70] |
| 3 to 4 | 16 | 6.90 µV | 3.00 | 0.75 | [2.27, 12.86] |
| 4 to 5 | 16 | 7.49 µV | 3.86 | 0.97 | [1.17, 13.88] |
| 5 to 6 | 9 | 8.09 µV | 3.98 | 1.33 | [5.11, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 856.35, BIC = 874.59
- Condition effect: *β* = -1.55, *SE* = 4.200, *z* = -0.370, *p* = 0.711

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 458.53, BIC = 476.77
- Condition effect: *β* = 0.33, *SE* = 0.587, *z* = 0.563, *p* = 0.573


### 3.2 P1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 520.75, BIC = 536.18
- Condition effect: *β* = 4.33, *SE* = 3.839, *z* = 1.128, *p* = 0.259

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 339.29, BIC = 354.72
- Condition effect: *β* = 0.94, *SE* = 0.852, *z* = 1.098, *p* = 0.272


### 3.3 P3b Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 754.89, BIC = 771.20
- Condition effect: *β* = -13.75, *SE* = 10.349, *z* = -1.328, *p* = 0.184

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 403.62, BIC = 419.94
- Condition effect: *β* = 0.60, *SE* = 0.963, *z* = 0.622, *p* = 0.534


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
