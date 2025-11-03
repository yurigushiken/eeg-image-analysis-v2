# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:50:08

---

## 1. Analysis Overview

**Total Measurements:** 190
**Number of Subjects:** 24
**Number of Conditions:** 5

**Components Analyzed:** Fz, N1, P1, P3b
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

### 2.1 Fz Component

#### Latency (Peak)

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 18 | 179.33 ms | 11.25 | 2.65 | [160.00, 196.00] |
| 2b | 15 | 175.73 ms | 8.48 | 2.19 | [160.00, 192.00] |
| 2c | 13 | 176.00 ms | 12.86 | 3.57 | [160.00, 200.00] |
| 2d | 11 | 184.00 ms | 14.20 | 4.28 | [164.00, 200.00] |
| 2e | 12 | 177.00 ms | 15.83 | 4.57 | [156.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 18 | -6.90 µV | 3.83 | 0.90 | [-14.22, -1.29] |
| 2b | 15 | -5.22 µV | 4.65 | 1.20 | [-20.22, -1.03] |
| 2c | 13 | -6.07 µV | 1.85 | 0.51 | [-8.72, -2.02] |
| 2d | 11 | -9.27 µV | 3.56 | 1.07 | [-15.68, -3.83] |
| 2e | 12 | -6.52 µV | 3.85 | 1.11 | [-15.21, -1.25] |


### 2.3 P1 Component

#### Latency (Peak)

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 19 | 509.26 ms | 43.88 | 10.07 | [444.00, 564.00] |
| 2b | 15 | 512.00 ms | 39.94 | 10.31 | [444.00, 564.00] |
| 2c | 12 | 515.00 ms | 41.29 | 11.92 | [460.00, 564.00] |
| 2d | 9 | 515.11 ms | 43.72 | 14.57 | [444.00, 564.00] |
| 2e | 14 | 498.86 ms | 39.61 | 10.59 | [444.00, 564.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 19 | 10.36 µV | 3.24 | 0.74 | [5.20, 20.64] |
| 2b | 15 | 8.35 µV | 4.95 | 1.28 | [1.66, 16.89] |
| 2c | 12 | 7.88 µV | 3.02 | 0.87 | [4.12, 13.43] |
| 2d | 9 | 10.77 µV | 3.86 | 1.29 | [5.44, 16.63] |
| 2e | 14 | 9.84 µV | 4.72 | 1.26 | [2.19, 17.72] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 546.50, BIC = 564.37
- **2b vs 2a**: *β* = -3.33, *SE* = 3.528, *z* = -0.944, *p* = 0.345
- **2c vs 2a**: *β* = -2.62, *SE* = 3.748, *z* = -0.698, *p* = 0.485
- **2d vs 2a**: *β* = 4.62, *SE* = 3.942, *z* = 1.173, *p* = 0.241
- **2e vs 2a**: *β* = -4.11, *SE* = 3.770, *z* = -1.089, *p* = 0.276
- **SNR**: *β* = -0.00, *SE* = 0.547, *z* = -0.006, *p* = 0.995

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 3.33 | 3.53 | 0.94 | 0.345 | 0.879 | n.s. |
| 2a - 2c | 2.62 | 3.75 | 0.70 | 0.485 | 0.930 | n.s. |
| 2a - 2d | -4.63 | 3.94 | -1.17 | 0.241 | 0.854 | n.s. |
| 2a - 2e | 4.11 | 3.77 | 1.09 | 0.276 | 0.856 | n.s. |
| 2b - 2c | -0.71 | 3.91 | -0.18 | 0.855 | 0.979 | n.s. |
| 2b - 2d | -7.96 | 4.06 | -1.96 | 0.050 | 0.369 | n.s. |
| 2b - 2e | 0.77 | 4.03 | 0.19 | 0.848 | 0.979 | n.s. |
| 2c - 2d | -7.24 | 4.36 | -1.66 | 0.097 | 0.557 | n.s. |
| 2c - 2e | 1.49 | 4.20 | 0.35 | 0.723 | 0.979 | n.s. |
| 2d - 2e | 8.73 | 4.31 | 2.03 | 0.043 | 0.354 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.78, *p* = 0.113, η²_G = 0.478
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | nan | 1 | n/a | 0.00 [-0.37, 0.92] | negligible | n.s. |
| 2a vs 2c | 1.00 | 1 | = 0.643 | 0.73 [-0.77, 0.67] | medium | n.s. |
| 2a vs 2d | 0.33 | 1 | = 0.795 | 0.24 [-0.76, 0.91] | small | n.s. |
| 2a vs 2e | 7.00 | 1 | = 0.271 | 3.13 [-0.18, 1.17] | large | n.s. |
| 2b vs 2c | 1.00 | 1 | = 0.643 | 0.73 [-0.80, 0.74] | medium | n.s. |
| 2b vs 2d | 0.33 | 1 | = 0.795 | 0.24 [-1.26, 0.48] | small | n.s. |
| 2b vs 2e | 7.00 | 1 | = 0.271 | 3.13 [-0.71, 0.96] | large | n.s. |
| 2c vs 2d | -inf | 1 | < .001 | -0.35 [-2.77, 0.99] | small | *** |
| 2c vs 2e | 2.00 | 1 | = 0.531 | 0.89 [-1.08, 1.02] | large | n.s. |
| 2d vs 2e | 3.00 | 1 | = 0.461 | 1.34 [-0.16, 2.07] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 333.78, BIC = 351.66
- **2b vs 2a**: *β* = 1.94, *SE* = 0.703, *z* = 2.763, *p* = 0.006
- **2c vs 2a**: *β* = -0.10, *SE* = 0.748, *z* = -0.133, *p* = 0.894
- **2d vs 2a**: *β* = -2.36, *SE* = 0.792, *z* = -2.979, *p* = 0.003
- **2e vs 2a**: *β* = -0.82, *SE* = 0.746, *z* = -1.096, *p* = 0.273
- **SNR**: *β* = -1.02, *SE* = 0.108, *z* = -9.451, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -1.94 | 0.70 | -2.76 | 0.006 | 0.039 | * |
| 2a - 2c | 0.10 | 0.75 | 0.13 | 0.894 | 0.894 | n.s. |
| 2a - 2d | 2.36 | 0.79 | 2.98 | 0.003 | 0.023 | * |
| 2a - 2e | 0.82 | 0.75 | 1.10 | 0.273 | 0.616 | n.s. |
| 2b - 2c | 2.04 | 0.78 | 2.62 | 0.009 | 0.051 | n.s. |
| 2b - 2d | 4.30 | 0.81 | 5.30 | < .001 | < .001 | *** |
| 2b - 2e | 2.76 | 0.80 | 3.43 | < .001 | 0.005 | ** |
| 2c - 2d | 2.26 | 0.88 | 2.57 | 0.010 | 0.051 | n.s. |
| 2c - 2e | 0.72 | 0.83 | 0.86 | 0.388 | 0.625 | n.s. |
| 2d - 2e | -1.54 | 0.86 | -1.79 | 0.074 | 0.265 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.558, η²_G = 0.396
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 1.29 | 1 | = 0.785 | 0.78 [-0.79, 0.49] | medium | n.s. |
| 2a vs 2c | -0.49 | 1 | = 0.787 | -0.69 [-1.07, 0.40] | medium | n.s. |
| 2a vs 2d | 2.19 | 1 | = 0.785 | 1.02 [-0.02, 2.04] | large | n.s. |
| 2a vs 2e | -0.19 | 1 | = 0.882 | -0.22 [-0.49, 0.78] | small | n.s. |
| 2b vs 2c | -0.90 | 1 | = 0.785 | -1.10 [-0.74, 0.79] | large | n.s. |
| 2b vs 2d | -0.51 | 1 | = 0.787 | -0.42 [-0.34, 1.46] | small | n.s. |
| 2b vs 2e | -0.85 | 1 | = 0.785 | -0.91 [-0.69, 0.99] | large | n.s. |
| 2c vs 2d | 1.61 | 1 | = 0.785 | 2.23 [-0.90, 3.19] | large | n.s. |
| 2c vs 2e | 1.10 | 1 | = 0.785 | 0.84 [-1.06, 1.03] | large | n.s. |
| 2d vs 2e | -2.07 | 1 | = 0.785 | -2.64 [-1.72, 0.34] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 721.52, BIC = 739.40
- **2b vs 2a**: *β* = 2.75, *SE* = 13.172, *z* = 0.209, *p* = 0.835
- **2c vs 2a**: *β* = 5.76, *SE* = 13.053, *z* = 0.441, *p* = 0.659
- **2e vs 2a**: *β* = -10.40, *SE* = 12.455, *z* = -0.835, *p* = 0.404

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -2.75 | 13.17 | -0.21 | 0.835 | 1.000 | n.s. |
| 2a - 2c | -5.76 | 13.05 | -0.44 | 0.659 | 0.999 | n.s. |
| 2a - 2d | -5.85 | nan | 0.00 | 1.000 | 1.000 | n.s. |
| 2a - 2e | 10.40 | 12.46 | 0.83 | 0.404 | 0.985 | n.s. |
| 2b - 2c | -3.01 | 10.25 | -0.29 | 0.769 | 1.000 | n.s. |
| 2b - 2d | -3.10 | nan | 0.00 | 1.000 | 1.000 | n.s. |
| 2b - 2e | 13.15 | 14.76 | 0.89 | 0.373 | 0.985 | n.s. |
| 2c - 2d | -0.08 | 15.02 | -0.01 | 0.996 | 1.000 | n.s. |
| 2c - 2e | 16.16 | 7.34 | 2.20 | 0.028 | 0.246 | n.s. |
| 2d - 2e | 16.24 | nan | 0.00 | 1.000 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 367.96, BIC = 385.83
- **2b vs 2a**: *β* = -1.62, *SE* = 0.886, *z* = -1.829, *p* = 0.067
- **2c vs 2a**: *β* = -0.83, *SE* = 0.994, *z* = -0.831, *p* = 0.406
- **2d vs 2a**: *β* = 1.07, *SE* = 1.062, *z* = 1.006, *p* = 0.315
- **2e vs 2a**: *β* = -0.17, *SE* = 0.909, *z* = -0.181, *p* = 0.856
- **SNR**: *β* = 0.71, *SE* = 0.160, *z* = 4.471, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 1.62 | 0.89 | 1.83 | 0.067 | 0.467 | n.s. |
| 2a - 2c | 0.83 | 0.99 | 0.83 | 0.406 | 0.875 | n.s. |
| 2a - 2d | -1.07 | 1.06 | -1.01 | 0.315 | 0.860 | n.s. |
| 2a - 2e | 0.16 | 0.91 | 0.18 | 0.856 | 0.875 | n.s. |
| 2b - 2c | -0.79 | 1.06 | -0.75 | 0.452 | 0.875 | n.s. |
| 2b - 2d | -2.69 | 1.14 | -2.35 | 0.019 | 0.171 | n.s. |
| 2b - 2e | -1.46 | 0.97 | -1.51 | 0.132 | 0.637 | n.s. |
| 2c - 2d | -1.89 | 1.22 | -1.56 | 0.119 | 0.637 | n.s. |
| 2c - 2e | -0.66 | 1.06 | -0.63 | 0.530 | 0.875 | n.s. |
| 2d - 2e | 1.23 | 1.14 | 1.08 | 0.279 | 0.860 | n.s. |

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

### 5.1 Fz Component

#### Latency

#### Amplitude

### 5.2 N1 Component

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

### 5.3 P1 Component

#### Latency

#### Amplitude

### 5.4 P3b Component

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
