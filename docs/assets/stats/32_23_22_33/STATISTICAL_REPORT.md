# Statistical Analysis Report: tables

**Generated:** 2025-10-13 23:12:17

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

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 790.52, BIC = 805.52
- Condition effect: *β* = -5.61, *SE* = 4.737, *z* = -1.184, *p* = 0.236

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 380.92, BIC = 395.92
- Condition effect: *β* = 0.39, *SE* = 0.458, *z* = 0.843, *p* = 0.399


### 3.2 P1 Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 379.72, BIC = 391.54
- Condition effect: *β* = -0.23, *SE* = 2.962, *z* = -0.076, *p* = 0.939

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 227.39, BIC = 239.21
- Condition effect: *β* = 0.15, *SE* = 0.649, *z* = 0.227, *p* = 0.820


### 3.3 P3b Component

#### Latency (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 650.14, BIC = 663.18
- Condition effect: *β* = 2.44, *SE* = 11.230, *z* = 0.217, *p* = 0.828

#### Amplitude (Peak)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 333.98, BIC = 347.02
- Condition effect: *β* = 0.77, *SE* = 0.947, *z* = 0.815, *p* = 0.415


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
