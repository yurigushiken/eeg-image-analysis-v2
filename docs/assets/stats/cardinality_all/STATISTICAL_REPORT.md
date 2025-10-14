# Statistical Analysis Report: tables

**Generated:** 2025-10-13 19:59:26

---

## 1. Analysis Overview

**Total Measurements:** 87
**Number of Subjects:** 18
**Number of Conditions:** 6

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Latency (50% Fractional Area), Mean Amplitude (ROI)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ 2.0
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases after applying an SNR filter >= 2.0. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 1 | 162.24 ms | n/a | n/a | [162.24, 162.24] |
| Cardinality2 | 1 | 166.37 ms | n/a | n/a | [166.37, 166.37] |
| Cardinality3 | 3 | 167.27 ms | 6.96 | 4.02 | [159.35, 172.39] |
| Cardinality4 | 5 | 166.36 ms | 4.48 | 2.01 | [159.02, 171.31] |
| Cardinality5 | 4 | 166.71 ms | 2.40 | 1.20 | [163.49, 168.59] |
| Cardinality6 | 5 | 167.17 ms | 2.18 | 0.98 | [164.23, 169.99] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 1 | -4.00 µV | n/a | n/a | [-4.00, -4.00] |
| Cardinality2 | 1 | -2.97 µV | n/a | n/a | [-2.97, -2.97] |
| Cardinality3 | 3 | -4.30 µV | 0.73 | 0.42 | [-4.90, -3.49] |
| Cardinality4 | 5 | -3.84 µV | 1.13 | 0.51 | [-4.57, -1.86] |
| Cardinality5 | 4 | -6.04 µV | 2.19 | 1.09 | [-9.31, -4.62] |
| Cardinality6 | 5 | -5.15 µV | 2.57 | 1.15 | [-8.47, -1.90] |


### 2.2 P1 Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 1 | 111.68 ms | n/a | n/a | [111.68, 111.68] |
| Cardinality4 | 2 | 113.62 ms | 4.73 | 3.34 | [110.28, 116.96] |
| Cardinality5 | 1 | 109.59 ms | n/a | n/a | [109.59, 109.59] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 1 | 3.86 µV | n/a | n/a | [3.86, 3.86] |
| Cardinality4 | 2 | 2.65 µV | 2.40 | 1.70 | [0.96, 4.35] |
| Cardinality5 | 1 | 1.36 µV | n/a | n/a | [1.36, 1.36] |


### 2.3 P3b Component

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 1 | 349.78 ms | n/a | n/a | [349.78, 349.78] |
| Cardinality2 | 1 | 350.81 ms | n/a | n/a | [350.81, 350.81] |
| Cardinality3 | 3 | 352.62 ms | 0.54 | 0.31 | [352.11, 353.18] |
| Cardinality5 | 1 | 354.49 ms | n/a | n/a | [354.49, 354.49] |
| Cardinality6 | 1 | 351.67 ms | n/a | n/a | [351.67, 351.67] |

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 1 | 3.22 µV | n/a | n/a | [3.22, 3.22] |
| Cardinality2 | 1 | 2.93 µV | n/a | n/a | [2.93, 2.93] |
| Cardinality3 | 3 | 3.27 µV | 1.69 | 0.98 | [1.90, 5.16] |
| Cardinality5 | 1 | 2.06 µV | n/a | n/a | [2.06, 2.06] |
| Cardinality6 | 1 | 1.43 µV | n/a | n/a | [1.43, 1.43] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 101.12, BIC = 108.68
- Condition effect: *β* = -6.52, *SE* = 0.679, *z* = -9.601, *p* < .001

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 87.14, BIC = 94.70
- Condition effect: *β* = 1.03, *SE* = 2.164, *z* = 0.478, *p* = 0.633


### 3.2 P1 Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 28.23, BIC = 25.16
- Condition effect: *β* = 1.94, *SE* = 1.671, *z* = 1.161, *p* = 0.246

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 22.81, BIC = 19.74
- Condition effect: *β* = -1.21, *SE* = 1.397, *z* = -0.865, *p* = 0.387


### 3.3 P3b Component

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = -2.07, BIC = -2.45
- Condition effect: *β* = 1.03, *SE* = 0.406, *z* = 2.531, *p* = 0.011

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 13.98, BIC = 13.60
- Condition effect: *β* = -0.29, *SE* = 1.279, *z* = -0.228, *p* = 0.820


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

**Boxplot:**

![N1 Latency Boxplot](plots/boxplot_N1_latency_frac_area_ms.png)

**Violin Plot:**

![N1 Latency Violin](plots/violin_N1_latency_frac_area_ms.png)

#### Amplitude

**Boxplot:**

![N1 Amplitude Boxplot](plots/boxplot_N1_mean_amplitude_roi.png)

**Violin Plot:**

![N1 Amplitude Violin](plots/violin_N1_mean_amplitude_roi.png)

### 5.2 P1 Component

#### Latency

**Boxplot:**

![P1 Latency Boxplot](plots/boxplot_P1_latency_frac_area_ms.png)

**Violin Plot:**

![P1 Latency Violin](plots/violin_P1_latency_frac_area_ms.png)

#### Amplitude

**Boxplot:**

![P1 Amplitude Boxplot](plots/boxplot_P1_mean_amplitude_roi.png)

**Violin Plot:**

![P1 Amplitude Violin](plots/violin_P1_mean_amplitude_roi.png)

### 5.3 P3b Component

#### Latency

**Boxplot:**

![P3b Latency Boxplot](plots/boxplot_P3b_latency_frac_area_ms.png)

**Violin Plot:**

![P3b Latency Violin](plots/violin_P3b_latency_frac_area_ms.png)

#### Amplitude

**Boxplot:**

![P3b Amplitude Boxplot](plots/boxplot_P3b_mean_amplitude_roi.png)

**Violin Plot:**

![P3b Amplitude Violin](plots/violin_P3b_mean_amplitude_roi.png)

---

## 6. Methods Summary (for Publication)

### ERP Measurement

ERP components were measured using a collapsed localizer approach, where component peaks were identified from the grand average of all conditions combined to avoid circular analysis (Luck & Gaspelin, 2017). Measurement windows were defined as the full-width at half-maximum (FWHM) around each peak. Component latency was quantified using the 50% fractional area latency (FAL), which represents the time point at which the cumulative area under the curve reaches 50% of its total value within the measurement window. This metric provides a robust estimate of component timing with lower measurement error than peak latency (Kiesel et al., 2008). Mean amplitude was computed as the average voltage within the FWHM window across predefined regions of interest (ROI).

Quality control filtering excluded subject-component measurements with signal-to-noise ratio (SNR) below 2.0.

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
