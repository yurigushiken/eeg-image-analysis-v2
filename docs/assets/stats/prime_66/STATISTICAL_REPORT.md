# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:28:46

---

## 1. Analysis Overview

**Total Measurements:** 255
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
| 6a | 22 | -4.64 µV | 2.35 | 0.50 | [-10.73, -0.22] |
| 6b | 18 | -3.66 µV | 2.51 | 0.59 | [-9.84, -0.31] |
| 6c | 12 | -5.64 µV | 4.42 | 1.27 | [-16.13, -0.22] |
| 6d | 19 | -4.41 µV | 2.78 | 0.64 | [-9.33, -0.06] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 22 | 171.37 ms | 8.93 | 1.90 | [146.44, 183.86] |
| 6b | 18 | 171.42 ms | 10.85 | 2.56 | [157.86, 190.84] |
| 6c | 12 | 174.21 ms | 11.53 | 3.33 | [151.92, 188.97] |
| 6d | 19 | 172.14 ms | 9.37 | 2.15 | [158.22, 194.33] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 7 | 2.39 µV | 2.10 | 0.80 | [0.13, 5.81] |
| 6b | 15 | 2.57 µV | 2.41 | 0.62 | [0.37, 8.23] |
| 6c | 10 | 2.92 µV | 2.37 | 0.75 | [0.93, 8.61] |
| 6d | 12 | 1.71 µV | 1.60 | 0.46 | [0.31, 5.72] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 7 | 88.40 ms | 17.59 | 6.65 | [56.54, 106.93] |
| 6b | 15 | 82.85 ms | 15.03 | 3.88 | [60.56, 108.21] |
| 6c | 10 | 92.44 ms | 13.83 | 4.37 | [65.41, 107.23] |
| 6d | 12 | 95.66 ms | 17.28 | 4.99 | [57.78, 113.02] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 12 | 3.07 µV | 2.59 | 0.75 | [0.37, 8.25] |
| 6b | 11 | 2.79 µV | 1.71 | 0.51 | [0.30, 5.71] |
| 6c | 5 | 3.28 µV | 1.30 | 0.58 | [1.37, 4.49] |
| 6d | 14 | 3.96 µV | 1.74 | 0.46 | [1.19, 7.66] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 12 | 375.30 ms | 13.20 | 3.81 | [345.45, 392.23] |
| 6b | 11 | 381.64 ms | 11.12 | 3.35 | [366.17, 401.56] |
| 6c | 5 | 367.87 ms | 15.21 | 6.80 | [349.42, 380.20] |
| 6d | 14 | 376.04 ms | 10.69 | 2.86 | [359.46, 395.06] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 324.72, BIC = 340.56
- **6b vs 6a**: *β* = 1.41, *SE* = 0.592, *z* = 2.374, *p* = 0.018
- **6c vs 6a**: *β* = -0.79, *SE* = 0.690, *z* = -1.138, *p* = 0.255
- **6d vs 6a**: *β* = 0.07, *SE* = 0.583, *z* = 0.112, *p* = 0.911
- **SNR**: *β* = -0.71, *SE* = 0.125, *z* = -5.726, *p* < .001

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -1.41 | 0.59 | -2.37 | 0.018 | 0.085 | n.s. |
| 6a - 6c | 0.79 | 0.69 | 1.14 | 0.255 | 0.536 | n.s. |
| 6a - 6d | -0.07 | 0.58 | -0.11 | 0.911 | 0.911 | n.s. |
| 6b - 6c | 2.19 | 0.73 | 3.02 | 0.003 | 0.015 | * |
| 6b - 6d | 1.34 | 0.61 | 2.19 | 0.028 | 0.109 | n.s. |
| 6c - 6d | -0.85 | 0.70 | -1.21 | 0.226 | 0.536 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.59, *p* = 0.625, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | -1.08 | 8 | = 0.709 | -0.51 [-0.93, 0.14] | medium | n.s. |
| 6a vs 6c | 0.30 | 8 | = 0.770 | 0.14 [-0.65, 0.69] | negligible | n.s. |
| 6a vs 6d | -0.59 | 8 | = 0.709 | -0.21 [-0.65, 0.35] | small | n.s. |
| 6b vs 6c | 1.15 | 8 | = 0.709 | 0.44 [-0.41, 1.18] | small | n.s. |
| 6b vs 6d | 0.56 | 8 | = 0.709 | 0.24 [-0.30, 0.74] | small | n.s. |
| 6c vs 6d | -0.71 | 8 | = 0.709 | -0.26 [-0.91, 0.53] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 527.57, BIC = 543.41
- **6b vs 6a**: *β* = 0.39, *SE* = 2.443, *z* = 0.161, *p* = 0.872
- **6c vs 6a**: *β* = 3.55, *SE* = 2.834, *z* = 1.253, *p* = 0.210
- **6d vs 6a**: *β* = 0.95, *SE* = 2.397, *z* = 0.398, *p* = 0.691
- **SNR**: *β* = 0.11, *SE* = 0.514, *z* = 0.213, *p* = 0.831

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -0.39 | 2.44 | -0.16 | 0.872 | 0.970 | n.s. |
| 6a - 6c | -3.55 | 2.83 | -1.25 | 0.210 | 0.758 | n.s. |
| 6a - 6d | -0.95 | 2.40 | -0.40 | 0.691 | 0.970 | n.s. |
| 6b - 6c | -3.16 | 2.99 | -1.06 | 0.291 | 0.820 | n.s. |
| 6b - 6d | -0.56 | 2.52 | -0.22 | 0.824 | 0.970 | n.s. |
| 6c - 6d | 2.60 | 2.90 | 0.90 | 0.370 | 0.843 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.839, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | 0.84 | 8 | = 0.879 | 0.36 [-0.51, 0.51] | small | n.s. |
| 6a vs 6c | 0.16 | 8 | = 0.879 | 0.09 [-0.81, 0.54] | negligible | n.s. |
| 6a vs 6d | 0.78 | 8 | = 0.879 | 0.29 [-0.68, 0.33] | small | n.s. |
| 6b vs 6c | -0.58 | 8 | = 0.879 | -0.23 [-0.97, 0.58] | small | n.s. |
| 6b vs 6d | -0.22 | 8 | = 0.879 | -0.08 [-0.55, 0.48] | negligible | n.s. |
| 6c vs 6d | 0.51 | 8 | = 0.879 | 0.16 [-0.42, 1.05] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 178.36, BIC = 190.84
- **6b vs 6a**: *β* = -0.21, *SE* = 0.714, *z* = -0.301, *p* = 0.763
- **6c vs 6a**: *β* = 0.97, *SE* = 0.767, *z* = 1.263, *p* = 0.207
- **6d vs 6a**: *β* = -0.12, *SE* = 0.746, *z* = -0.156, *p* = 0.876
- **SNR**: *β* = 1.62, *SE* = 0.296, *z* = 5.487, *p* < .001

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 0.22 | 0.71 | 0.30 | 0.763 | 0.987 | n.s. |
| 6a - 6c | -0.97 | 0.77 | -1.26 | 0.207 | 0.604 | n.s. |
| 6a - 6d | 0.12 | 0.75 | 0.16 | 0.876 | 0.987 | n.s. |
| 6b - 6c | -1.18 | 0.65 | -1.82 | 0.068 | 0.347 | n.s. |
| 6b - 6d | -0.10 | 0.62 | -0.16 | 0.874 | 0.987 | n.s. |
| 6c - 6d | 1.08 | 0.67 | 1.63 | 0.104 | 0.422 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 371.50, BIC = 383.99
- **6b vs 6a**: *β* = -1.69, *SE* = 5.650, *z* = -0.299, *p* = 0.765
- **6c vs 6a**: *β* = 5.64, *SE* = 5.853, *z* = 0.963, *p* = 0.335
- **6d vs 6a**: *β* = 10.10, *SE* = 5.788, *z* = 1.745, *p* = 0.081
- **SNR**: *β* = 0.43, *SE* = 2.426, *z* = 0.176, *p* = 0.860

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 1.69 | 5.65 | 0.30 | 0.765 | 0.765 | n.s. |
| 6a - 6c | -5.64 | 5.85 | -0.96 | 0.335 | 0.707 | n.s. |
| 6a - 6d | -10.10 | 5.79 | -1.75 | 0.081 | 0.344 | n.s. |
| 6b - 6c | -7.32 | 5.20 | -1.41 | 0.159 | 0.500 | n.s. |
| 6b - 6d | -11.79 | 4.84 | -2.44 | 0.015 | 0.086 | n.s. |
| 6c - 6d | -4.46 | 5.37 | -0.83 | 0.406 | 0.707 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 169.08, BIC = 181.25
- **6b vs 6a**: *β* = -0.33, *SE* = 0.662, *z* = -0.498, *p* = 0.618
- **6c vs 6a**: *β* = 0.36, *SE* = 0.832, *z* = 0.435, *p* = 0.664
- **6d vs 6a**: *β* = 0.14, *SE* = 0.633, *z* = 0.214, *p* = 0.831
- **SNR**: *β* = 0.63, *SE* = 0.143, *z* = 4.407, *p* < .001

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 0.33 | 0.66 | 0.50 | 0.618 | 0.979 | n.s. |
| 6a - 6c | -0.36 | 0.83 | -0.43 | 0.664 | 0.979 | n.s. |
| 6a - 6d | -0.14 | 0.63 | -0.21 | 0.831 | 0.979 | n.s. |
| 6b - 6c | -0.69 | 0.83 | -0.83 | 0.404 | 0.955 | n.s. |
| 6b - 6d | -0.46 | 0.69 | -0.67 | 0.502 | 0.969 | n.s. |
| 6c - 6d | 0.23 | 0.86 | 0.26 | 0.793 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 338.34, BIC = 350.50
- **6b vs 6a**: *β* = 6.32, *SE* = 4.925, *z* = 1.283, *p* = 0.200
- **6c vs 6a**: *β* = -7.36, *SE* = 6.388, *z* = -1.152, *p* = 0.249
- **6d vs 6a**: *β* = 0.37, *SE* = 4.768, *z* = 0.077, *p* = 0.938
- **SNR**: *β* = 0.31, *SE* = 1.046, *z* = 0.300, *p* = 0.764

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -6.32 | 4.92 | -1.28 | 0.200 | 0.672 | n.s. |
| 6a - 6c | 7.36 | 6.39 | 1.15 | 0.249 | 0.672 | n.s. |
| 6a - 6d | -0.37 | 4.77 | -0.08 | 0.938 | 0.938 | n.s. |
| 6b - 6c | 13.67 | 6.86 | 1.99 | 0.046 | 0.247 | n.s. |
| 6b - 6d | 5.95 | 5.17 | 1.15 | 0.250 | 0.672 | n.s. |
| 6c - 6d | -7.73 | 6.23 | -1.24 | 0.215 | 0.672 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
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
