# Statistical Analysis Report: tables

**Generated:** 2025-10-16 21:42:56

---

## 1. Analysis Overview

**Total Measurements:** 144
**Number of Subjects:** 24
**Number of Conditions:** 3

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
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

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | -2.55 µV | 2.40 | 0.62 | [-8.45, -0.12] |
| Cardinality2 | 22 | -3.25 µV | 1.94 | 0.41 | [-7.74, -0.22] |
| Cardinality3 | 23 | -3.28 µV | 1.86 | 0.39 | [-8.03, -0.07] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | 177.77 ms | 14.70 | 3.80 | [151.65, 202.90] |
| Cardinality2 | 22 | 175.22 ms | 10.84 | 2.31 | [157.41, 192.22] |
| Cardinality3 | 23 | 175.47 ms | 10.19 | 2.13 | [158.74, 203.81] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 18 | 3.39 µV | 2.91 | 0.69 | [0.22, 12.02] |
| Cardinality2 | 12 | 2.24 µV | 1.67 | 0.48 | [0.46, 5.83] |
| Cardinality3 | 14 | 2.20 µV | 1.95 | 0.52 | [0.26, 6.33] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 18 | 116.62 ms | 4.83 | 1.14 | [105.80, 124.75] |
| Cardinality2 | 12 | 116.02 ms | 4.48 | 1.29 | [106.05, 122.70] |
| Cardinality3 | 14 | 115.99 ms | 5.13 | 1.37 | [107.83, 125.03] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

_No descriptive statistics available._

#### Latency (50% Fractional Area)

_No descriptive statistics available._


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.83, *p* = 0.449, η²_G = 0.029
- Greenhouse-Geisser corrected: *p* = 0.416 (ε = 0.714)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.86 | 13 | = 0.608 | 0.33 [-0.30, 0.82] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.12 | 13 | = 0.608 | 0.35 [-0.29, 0.89] | small | n.s. |
| Cardinality2 vs Cardinality3 | 0.17 | 13 | = 0.871 | 0.04 [-0.39, 0.52] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 259.07, BIC = 269.54
- Condition effect: *β* = -0.73, *SE* = 0.585, *z* = -1.252, *p* = 0.211

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.07, *p* = 0.930, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.25 | 13 | = 0.958 | 0.08 [-0.41, 0.70] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 0.45 | 13 | = 0.958 | 0.09 [-0.46, 0.70] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.05 | 13 | = 0.958 | 0.02 [-0.47, 0.44] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 465.95, BIC = 476.42
- Condition effect: *β* = -2.44, *SE* = 3.123, *z* = -0.781, *p* = 0.435


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 3.50, *p* = 0.059, η²_G = 0.174
- Greenhouse-Geisser corrected: *p* = 0.095 (ε = 0.576)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 3.60 | 7 | = 0.026 | 0.89 [-0.03, 1.78] | large | * |
| Cardinality1 vs Cardinality3 | 1.62 | 7 | = 0.222 | 0.78 [-0.03, 1.37] | medium | n.s. |
| Cardinality2 vs Cardinality3 | -0.19 | 7 | = 0.853 | -0.08 [-0.92, 0.62] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 200.89, BIC = 209.81
- Condition effect: *β* = -1.55, *SE* = 0.708, *z* = -2.194, *p* = 0.028

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.34, *p* = 0.716, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.73 | 7 | = 0.808 | 0.39 [-0.90, 0.64] | small | n.s. |
| Cardinality1 vs Cardinality3 | 0.65 | 7 | = 0.808 | 0.30 [-0.44, 0.85] | small | n.s. |
| Cardinality2 vs Cardinality3 | 0.13 | 7 | = 0.900 | 0.05 [-0.73, 0.81] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 270.48, BIC = 279.40
- Condition effect: *β* = -0.60, *SE* = 1.797, *z* = -0.335, *p* = 0.737


### 3.3 P3b Component

#### Mean Amplitude (ROI)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

_LMM results not available._

#### Latency (50% Fractional Area)

_ANOVA results not available (may require pingouin library)._

_Pairwise test results not available._

_LMM results not available._


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.059)

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
