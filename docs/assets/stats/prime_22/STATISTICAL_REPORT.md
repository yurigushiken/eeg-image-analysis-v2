# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:58:43

---

## 1. Analysis Overview

**Total Measurements:** 172
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 2a | 14 | -5.11 µV | 3.95 | 1.06 | [-12.87, -0.48] |
| 2b | 19 | -4.32 µV | 2.15 | 0.49 | [-7.21, -1.11] |
| 2c | 16 | -3.40 µV | 2.37 | 0.59 | [-8.67, -0.47] |
| 2d | 18 | -3.17 µV | 2.18 | 0.51 | [-6.97, -0.24] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 14 | 176.37 ms | 15.10 | 4.04 | [142.39, 202.81] |
| 2b | 19 | 172.48 ms | 12.57 | 2.88 | [148.59, 195.99] |
| 2c | 16 | 177.48 ms | 12.43 | 3.11 | [156.92, 202.10] |
| 2d | 18 | 179.87 ms | 15.37 | 3.62 | [151.12, 205.35] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 12 | 1.85 µV | 1.52 | 0.44 | [0.20, 4.71] |
| 2b | 9 | 1.29 µV | 0.80 | 0.27 | [0.24, 2.53] |
| 2c | 10 | 3.45 µV | 1.91 | 0.60 | [1.04, 6.15] |
| 2d | 13 | 2.14 µV | 2.32 | 0.64 | [0.01, 7.59] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 12 | 98.20 ms | 16.39 | 4.73 | [71.24, 127.03] |
| 2b | 9 | 94.45 ms | 20.48 | 6.83 | [70.03, 125.29] |
| 2c | 10 | 102.70 ms | 12.64 | 4.00 | [78.07, 115.60] |
| 2d | 13 | 105.10 ms | 15.35 | 4.26 | [80.08, 124.58] |


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

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 285.71, BIC = 301.15
- **2b vs 2a**: *β* = 1.37, *SE* = 0.606, *z* = 2.260, *p* = 0.024
- **2c vs 2a**: *β* = 1.67, *SE* = 0.625, *z* = 2.680, *p* = 0.007
- **2d vs 2a**: *β* = 2.16, *SE* = 0.609, *z* = 3.555, *p* < .001
- **SNR**: *β* = -0.93, *SE* = 0.115, *z* = -8.119, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -1.37 | 0.61 | -2.26 | 0.024 | 0.092 | n.s. |
| 2a - 2c | -1.67 | 0.62 | -2.68 | 0.007 | 0.036 | * |
| 2a - 2d | -2.16 | 0.61 | -3.55 | < .001 | 0.002 | ** |
| 2b - 2c | -0.30 | 0.58 | -0.52 | 0.601 | 0.644 | n.s. |
| 2b - 2d | -0.79 | 0.56 | -1.42 | 0.155 | 0.396 | n.s. |
| 2c - 2d | -0.49 | 0.59 | -0.84 | 0.403 | 0.644 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.31, *p* = 0.818, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | -1.21 | 5 | = 0.993 | -0.50 [-1.10, 0.23] | small | n.s. |
| 2a vs 2c | -0.86 | 5 | = 0.993 | -0.43 [-0.95, 0.50] | small | n.s. |
| 2a vs 2d | -0.52 | 5 | = 0.993 | -0.30 [-1.08, 0.31] | small | n.s. |
| 2b vs 2c | 0.00 | 5 | = 0.996 | 0.00 [-0.61, 0.60] | negligible | n.s. |
| 2b vs 2d | 0.40 | 5 | = 0.993 | 0.21 [-1.15, 0.04] | small | n.s. |
| 2c vs 2d | 0.23 | 5 | = 0.993 | 0.18 [-0.57, 0.70] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 546.37, BIC = 561.81
- **2b vs 2a**: *β* = -4.06, *SE* = 4.092, *z* = -0.993, *p* = 0.321
- **2c vs 2a**: *β* = 0.33, *SE* = 4.268, *z* = 0.078, *p* = 0.938
- **2d vs 2a**: *β* = 2.42, *SE* = 4.163, *z* = 0.583, *p* = 0.560
- **SNR**: *β* = -0.36, *SE* = 0.858, *z* = -0.424, *p* = 0.671

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 4.06 | 4.09 | 0.99 | 0.321 | 0.787 | n.s. |
| 2a - 2c | -0.33 | 4.27 | -0.08 | 0.938 | 0.938 | n.s. |
| 2a - 2d | -2.43 | 4.16 | -0.58 | 0.560 | 0.915 | n.s. |
| 2b - 2c | -4.39 | 3.93 | -1.12 | 0.264 | 0.784 | n.s. |
| 2b - 2d | -6.49 | 3.78 | -1.71 | 0.086 | 0.419 | n.s. |
| 2c - 2d | -2.09 | 4.00 | -0.52 | 0.600 | 0.915 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.422, η²_G = 0.085
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 1.39 | 5 | = 0.643 | 0.75 [-0.53, 0.75] | medium | n.s. |
| 2a vs 2c | 0.53 | 5 | = 0.689 | 0.15 [-0.61, 0.82] | negligible | n.s. |
| 2a vs 2d | 0.67 | 5 | = 0.689 | 0.36 [-0.60, 0.75] | small | n.s. |
| 2b vs 2c | -1.10 | 5 | = 0.643 | -0.58 [-1.21, 0.09] | medium | n.s. |
| 2b vs 2d | -1.65 | 5 | = 0.643 | -0.45 [-1.17, 0.03] | small | n.s. |
| 2c vs 2d | 0.42 | 5 | = 0.689 | 0.20 [-0.88, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 126.58, BIC = 139.07
- **2b vs 2a**: *β* = -0.52, *SE* = 0.353, *z* = -1.462, *p* = 0.144
- **2c vs 2a**: *β* = 0.25, *SE* = 0.367, *z* = 0.686, *p* = 0.493
- **2d vs 2a**: *β* = -0.66, *SE* = 0.339, *z* = -1.942, *p* = 0.052
- **SNR**: *β* = 1.78, *SE* = 0.167, *z* = 10.639, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 0.52 | 0.35 | 1.46 | 0.144 | 0.372 | n.s. |
| 2a - 2c | -0.25 | 0.37 | -0.69 | 0.493 | 0.743 | n.s. |
| 2a - 2d | 0.66 | 0.34 | 1.94 | 0.052 | 0.235 | n.s. |
| 2b - 2c | -0.77 | 0.42 | -1.85 | 0.064 | 0.235 | n.s. |
| 2b - 2d | 0.14 | 0.37 | 0.39 | 0.698 | 0.743 | n.s. |
| 2c - 2d | 0.91 | 0.34 | 2.68 | 0.007 | 0.043 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.15, *p* = 0.273, η²_G = 0.682
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.34 | 1 | = 0.791 | 0.45 [-0.61, 1.62] | small | n.s. |
| 2a vs 2c | -1.09 | 1 | = 0.569 | -1.02 [-2.04, 0.18] | large | n.s. |
| 2a vs 2d | -1.19 | 1 | = 0.569 | -1.61 [-1.41, 0.75] | large | n.s. |
| 2b vs 2c | -2.88 | 1 | = 0.569 | -3.21 [-7.90, 2.62] | large | n.s. |
| 2b vs 2d | -33.97 | 1 | = 0.112 | -3.25 [-2.08, 0.37] | large | n.s. |
| 2c vs 2d | -1.34 | 1 | = 0.569 | -1.48 [-0.53, 1.41] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 376.48, BIC = 388.97
- **2b vs 2a**: *β* = -5.25, *SE* = 5.912, *z* = -0.888, *p* = 0.375
- **2c vs 2a**: *β* = 3.79, *SE* = 6.118, *z* = 0.620, *p* = 0.535
- **2d vs 2a**: *β* = 4.20, *SE* = 5.792, *z* = 0.725, *p* = 0.468
- **SNR**: *β* = 1.13, *SE* = 2.817, *z* = 0.400, *p* = 0.689

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 5.25 | 5.91 | 0.89 | 0.375 | 0.847 | n.s. |
| 2a - 2c | -3.79 | 6.12 | -0.62 | 0.535 | 0.850 | n.s. |
| 2a - 2d | -4.20 | 5.79 | -0.73 | 0.468 | 0.850 | n.s. |
| 2b - 2c | -9.04 | 6.95 | -1.30 | 0.193 | 0.658 | n.s. |
| 2b - 2d | -9.45 | 6.21 | -1.52 | 0.128 | 0.560 | n.s. |
| 2c - 2d | -0.41 | 5.66 | -0.07 | 0.942 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.33, *p* = 0.252, η²_G = 0.698
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 1.85 | 1 | = 0.473 | 2.32 [-0.83, 1.30] | large | n.s. |
| 2a vs 2c | 0.49 | 1 | = 0.855 | 0.66 [-0.81, 1.05] | medium | n.s. |
| 2a vs 2d | 0.19 | 1 | = 0.882 | 0.25 [-1.17, 0.94] | small | n.s. |
| 2b vs 2c | -7.65 | 1 | = 0.248 | -2.72 [-3.33, 2.09] | large | n.s. |
| 2b vs 2d | -24.06 | 1 | = 0.159 | -4.23 [-2.24, 0.30] | large | n.s. |
| 2c vs 2d | -3.69 | 1 | = 0.337 | -0.72 [-0.74, 1.13] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


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

#### Amplitude

---

## 6. Methods Summary (for Publication)

### ERP Measurement

ERP components were measured using a collapsed localizer approach, where component peaks were identified from the grand average of all conditions combined to avoid circular analysis (Luck & Gaspelin, 2017). Measurement windows were defined as the full-width at half-maximum (FWHM) around each peak. Component latency was quantified using the 50% fractional area latency (FAL), which represents the time point at which the cumulative area under the curve reaches 50% of its total value within the measurement window. This metric provides a robust estimate of component timing with lower measurement error than peak latency (Kiesel et al., 2008). Mean amplitude was computed as the average voltage within the FWHM window across predefined regions of interest (ROI).

### Statistical Analysis

Linear mixed-effects models (LMM) with random intercepts for subjects were used as the primary analysis, as they optimally handle missing data via maximum likelihood estimation (Baayen et al., 2008). 
For comparison with traditional approaches, repeated-measures ANOVA and pairwise t-tests were also performed on complete cases; however, power was substantially reduced by listwise deletion. Therefore, LMM results are emphasized in interpretation.

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.11
- MNE-Python 1.10.1
- Statsmodels 0.14.5
- Pingouin 0.5.5

### References

- Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects modeling with crossed random effects for subjects and items. *Journal of Memory and Language, 59*(4), 390-412.
- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
