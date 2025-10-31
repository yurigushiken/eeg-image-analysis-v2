# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:27:58

---

## 1. Analysis Overview

**Total Measurements:** 190
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 2a | 18 | -4.13 µV | 2.61 | 0.62 | [-7.95, 0.02] |
| 2b | 15 | -3.40 µV | 4.51 | 1.17 | [-18.02, 0.15] |
| 2c | 13 | -3.11 µV | 1.97 | 0.55 | [-7.02, -0.06] |
| 2d | 11 | -5.04 µV | 2.83 | 0.85 | [-8.61, -0.61] |
| 2e | 12 | -3.15 µV | 2.28 | 0.66 | [-8.78, 0.07] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 18 | 178.62 ms | 7.49 | 1.76 | [165.34, 191.03] |
| 2b | 15 | 174.90 ms | 8.72 | 2.25 | [157.31, 189.25] |
| 2c | 13 | 177.99 ms | 9.86 | 2.73 | [163.08, 199.58] |
| 2d | 11 | 179.87 ms | 10.35 | 3.12 | [160.91, 193.86] |
| 2e | 12 | 179.28 ms | 9.64 | 2.78 | [158.89, 191.88] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

_No descriptive statistics available._

#### Latency (50% Fractional Area)

_No descriptive statistics available._


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 19 | 6.24 µV | 2.58 | 0.59 | [1.81, 11.37] |
| 2b | 15 | 5.13 µV | 4.36 | 1.13 | [0.03, 12.44] |
| 2c | 12 | 3.96 µV | 3.34 | 0.97 | [0.33, 9.88] |
| 2d | 9 | 6.24 µV | 2.34 | 0.78 | [2.34, 9.09] |
| 2e | 14 | 5.96 µV | 3.79 | 1.01 | [0.31, 12.23] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 19 | 505.08 ms | 15.46 | 3.55 | [480.25, 532.35] |
| 2b | 15 | 513.10 ms | 28.07 | 7.25 | [453.24, 561.97] |
| 2c | 12 | 500.40 ms | 25.69 | 7.42 | [458.24, 559.48] |
| 2d | 9 | 504.36 ms | 18.45 | 6.15 | [472.10, 530.23] |
| 2e | 14 | 505.61 ms | 17.10 | 4.57 | [479.65, 546.68] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 273.01, BIC = 290.88
- **2b vs 2a**: *β* = 1.06, *SE* = 0.493, *z* = 2.159, *p* = 0.031
- **2c vs 2a**: *β* = 0.28, *SE* = 0.521, *z* = 0.547, *p* = 0.584
- **2d vs 2a**: *β* = -0.78, *SE* = 0.549, *z* = -1.421, *p* = 0.155
- **2e vs 2a**: *β* = 0.16, *SE* = 0.524, *z* = 0.306, *p* = 0.760
- **SNR**: *β* = -1.02, *SE* = 0.075, *z* = -13.601, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -1.06 | 0.49 | -2.16 | 0.031 | 0.246 | n.s. |
| 2a - 2c | -0.28 | 0.52 | -0.55 | 0.584 | 0.928 | n.s. |
| 2a - 2d | 0.78 | 0.55 | 1.42 | 0.155 | 0.561 | n.s. |
| 2a - 2e | -0.16 | 0.52 | -0.31 | 0.760 | 0.942 | n.s. |
| 2b - 2c | 0.78 | 0.54 | 1.43 | 0.152 | 0.561 | n.s. |
| 2b - 2d | 1.84 | 0.57 | 3.26 | 0.001 | 0.011 | * |
| 2b - 2e | 0.90 | 0.56 | 1.61 | 0.107 | 0.548 | n.s. |
| 2c - 2d | 1.06 | 0.60 | 1.76 | 0.078 | 0.477 | n.s. |
| 2c - 2e | 0.12 | 0.58 | 0.22 | 0.829 | 0.942 | n.s. |
| 2d - 2e | -0.94 | 0.60 | -1.57 | 0.117 | 0.548 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.89, *p* = 0.544, η²_G = 0.399
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 1.24 | 1 | = 0.713 | 0.76 [-0.57, 0.70] | medium | n.s. |
| 2a vs 2c | -0.63 | 1 | = 0.713 | -0.86 [-1.12, 0.36] | large | n.s. |
| 2a vs 2d | 1.32 | 1 | = 0.713 | 0.57 [-0.56, 1.15] | medium | n.s. |
| 2a vs 2e | -0.41 | 1 | = 0.750 | -0.52 [-0.81, 0.47] | medium | n.s. |
| 2b vs 2c | -0.96 | 1 | = 0.713 | -1.13 [-0.88, 0.67] | large | n.s. |
| 2b vs 2d | -0.70 | 1 | = 0.713 | -0.57 [-0.64, 1.05] | medium | n.s. |
| 2b vs 2e | -0.90 | 1 | = 0.713 | -0.99 [-1.04, 0.65] | large | n.s. |
| 2c vs 2d | 1.53 | 1 | = 0.713 | 2.17 [-0.99, 2.78] | large | n.s. |
| 2c vs 2e | 1.89 | 1 | = 0.713 | 0.69 [-1.02, 1.08] | medium | n.s. |
| 2d vs 2e | -1.44 | 1 | = 0.713 | -1.97 [-1.55, 0.44] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 508.89, BIC = 526.76
- **2b vs 2a**: *β* = -3.38, *SE* = 2.823, *z* = -1.199, *p* = 0.231
- **2c vs 2a**: *β* = -0.27, *SE* = 2.984, *z* = -0.091, *p* = 0.927
- **2d vs 2a**: *β* = 1.10, *SE* = 3.126, *z* = 0.351, *p* = 0.725
- **2e vs 2a**: *β* = -0.05, *SE* = 3.029, *z* = -0.017, *p* = 0.986
- **SNR**: *β* = 0.01, *SE* = 0.420, *z* = 0.035, *p* = 0.972

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 3.38 | 2.82 | 1.20 | 0.231 | 0.906 | n.s. |
| 2a - 2c | 0.27 | 2.98 | 0.09 | 0.927 | 1.000 | n.s. |
| 2a - 2d | -1.10 | 3.13 | -0.35 | 0.725 | 0.999 | n.s. |
| 2a - 2e | 0.05 | 3.03 | 0.02 | 0.986 | 1.000 | n.s. |
| 2b - 2c | -3.11 | 3.10 | -1.00 | 0.316 | 0.944 | n.s. |
| 2b - 2d | -4.48 | 3.24 | -1.38 | 0.166 | 0.838 | n.s. |
| 2b - 2e | -3.33 | 3.23 | -1.03 | 0.303 | 0.944 | n.s. |
| 2c - 2d | -1.37 | 3.44 | -0.40 | 0.691 | 0.999 | n.s. |
| 2c - 2e | -0.22 | 3.35 | -0.07 | 0.948 | 1.000 | n.s. |
| 2d - 2e | 1.15 | 3.42 | 0.34 | 0.737 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.475, η²_G = 0.405
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.75 | 1 | = 0.874 | 1.06 [-0.40, 0.89] | large | n.s. |
| 2a vs 2c | 1.00 | 1 | = 0.874 | 0.82 [-0.97, 0.48] | large | n.s. |
| 2a vs 2d | 0.51 | 1 | = 0.874 | 0.34 [-0.63, 1.06] | small | n.s. |
| 2a vs 2e | 7.68 | 1 | = 0.616 | 6.76 [-0.48, 0.80] | large | n.s. |
| 2b vs 2c | 0.52 | 1 | = 0.874 | 0.59 [-0.93, 0.62] | medium | n.s. |
| 2b vs 2d | -0.08 | 1 | = 0.951 | -0.10 [-0.95, 0.73] | negligible | n.s. |
| 2b vs 2e | 5.10 | 1 | = 0.616 | 5.68 [-0.97, 0.71] | large | n.s. |
| 2c vs 2d | -1.36 | 1 | = 0.874 | -0.57 [-4.34, 0.78] | medium | n.s. |
| 2c vs 2e | 0.28 | 1 | = 0.915 | 0.28 [-1.03, 1.07] | small | n.s. |
| 2d vs 2e | 1.84 | 1 | = 0.874 | 1.77 [-0.45, 1.53] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 328.64, BIC = 346.51
- **2b vs 2a**: *β* = -0.68, *SE* = 0.713, *z* = -0.947, *p* = 0.344
- **2c vs 2a**: *β* = -0.90, *SE* = 0.794, *z* = -1.128, *p* = 0.259
- **2d vs 2a**: *β* = 0.12, *SE* = 0.849, *z* = 0.148, *p* = 0.883
- **2e vs 2a**: *β* = 0.07, *SE* = 0.730, *z* = 0.090, *p* = 0.928
- **SNR**: *β* = 0.83, *SE* = 0.121, *z* = 6.835, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 0.68 | 0.71 | 0.95 | 0.344 | 0.946 | n.s. |
| 2a - 2c | 0.90 | 0.79 | 1.13 | 0.259 | 0.946 | n.s. |
| 2a - 2d | -0.13 | 0.85 | -0.15 | 0.883 | 0.998 | n.s. |
| 2a - 2e | -0.07 | 0.73 | -0.09 | 0.928 | 0.998 | n.s. |
| 2b - 2c | 0.22 | 0.84 | 0.26 | 0.793 | 0.998 | n.s. |
| 2b - 2d | -0.80 | 0.91 | -0.88 | 0.378 | 0.946 | n.s. |
| 2b - 2e | -0.74 | 0.77 | -0.96 | 0.339 | 0.946 | n.s. |
| 2c - 2d | -1.02 | 0.96 | -1.06 | 0.290 | 0.946 | n.s. |
| 2c - 2e | -0.96 | 0.84 | -1.14 | 0.253 | 0.946 | n.s. |
| 2d - 2e | 0.06 | 0.91 | 0.07 | 0.948 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 628.28, BIC = 646.15
- **2b vs 2a**: *β* = 7.67, *SE* = 7.107, *z* = 1.079, *p* = 0.280
- **2c vs 2a**: *β* = -5.51, *SE* = 7.655, *z* = -0.720, *p* = 0.471
- **2d vs 2a**: *β* = -0.62, *SE* = 8.389, *z* = -0.074, *p* = 0.941
- **2e vs 2a**: *β* = 0.26, *SE* = 7.210, *z* = 0.037, *p* = 0.971
- **SNR**: *β* = -0.78, *SE* = 1.021, *z* = -0.761, *p* = 0.447

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -7.67 | 7.11 | -1.08 | 0.280 | 0.948 | n.s. |
| 2a - 2c | 5.52 | 7.65 | 0.72 | 0.471 | 0.978 | n.s. |
| 2a - 2d | 0.62 | 8.39 | 0.07 | 0.941 | 0.999 | n.s. |
| 2a - 2e | -0.26 | 7.21 | -0.04 | 0.971 | 0.999 | n.s. |
| 2b - 2c | 13.19 | 7.94 | 1.66 | 0.097 | 0.639 | n.s. |
| 2b - 2d | 8.29 | 8.67 | 0.96 | 0.339 | 0.960 | n.s. |
| 2b - 2e | 7.41 | 7.63 | 0.97 | 0.331 | 0.960 | n.s. |
| 2c - 2d | -4.89 | 9.11 | -0.54 | 0.591 | 0.978 | n.s. |
| 2c - 2e | -5.78 | 8.11 | -0.71 | 0.476 | 0.978 | n.s. |
| 2d - 2e | -0.88 | 8.85 | -0.10 | 0.920 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


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

#### Amplitude

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
