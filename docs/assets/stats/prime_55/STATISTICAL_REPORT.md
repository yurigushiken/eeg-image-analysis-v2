# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:27:44

---

## 1. Analysis Overview

**Total Measurements:** 252
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
| 5a | 11 | -6.66 µV | 4.62 | 1.39 | [-17.53, -0.84] |
| 5b | 20 | -4.23 µV | 2.95 | 0.66 | [-10.28, -0.26] |
| 5c | 19 | -5.33 µV | 3.85 | 0.88 | [-14.70, -0.56] |
| 5d | 22 | -4.46 µV | 2.31 | 0.49 | [-10.03, -0.85] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 11 | 172.70 ms | 11.14 | 3.36 | [153.02, 197.99] |
| 5b | 20 | 171.58 ms | 14.13 | 3.16 | [142.57, 194.88] |
| 5c | 19 | 170.07 ms | 9.40 | 2.16 | [149.22, 185.89] |
| 5d | 22 | 170.30 ms | 9.24 | 1.97 | [144.85, 183.69] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 8 | 1.51 µV | 1.51 | 0.53 | [0.14, 4.72] |
| 5b | 13 | 3.30 µV | 3.22 | 0.89 | [0.43, 12.27] |
| 5c | 12 | 3.12 µV | 1.83 | 0.53 | [0.28, 6.39] |
| 5d | 13 | 3.10 µV | 2.34 | 0.65 | [0.09, 6.45] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 8 | 96.11 ms | 7.07 | 2.50 | [87.11, 107.50] |
| 5b | 13 | 95.31 ms | 5.77 | 1.60 | [85.80, 106.39] |
| 5c | 12 | 95.28 ms | 5.29 | 1.53 | [85.93, 103.90] |
| 5d | 13 | 97.22 ms | 3.49 | 0.97 | [89.45, 102.68] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 5 | 4.38 µV | 4.75 | 2.13 | [0.55, 12.11] |
| 5b | 12 | 2.58 µV | 1.24 | 0.36 | [0.94, 4.39] |
| 5c | 13 | 2.86 µV | 2.62 | 0.73 | [0.25, 9.33] |
| 5d | 14 | 2.35 µV | 1.24 | 0.33 | [0.42, 3.93] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 5 | 351.12 ms | 7.36 | 3.29 | [340.02, 360.58] |
| 5b | 12 | 353.13 ms | 6.99 | 2.02 | [341.00, 368.70] |
| 5c | 13 | 353.92 ms | 7.49 | 2.08 | [341.23, 371.31] |
| 5d | 14 | 352.29 ms | 8.71 | 2.33 | [334.81, 363.32] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 347.95, BIC = 363.88
- **5b vs 5a**: *β* = 2.22, *SE* = 0.829, *z* = 2.678, *p* = 0.007
- **5c vs 5a**: *β* = 0.65, *SE* = 0.834, *z* = 0.784, *p* = 0.433
- **5d vs 5a**: *β* = 1.61, *SE* = 0.819, *z* = 1.972, *p* = 0.049
- **SNR**: *β* = -0.87, *SE* = 0.149, *z* = -5.841, *p* < .001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -2.22 | 0.83 | -2.68 | 0.007 | 0.044 | * |
| 5a - 5c | -0.65 | 0.83 | -0.78 | 0.433 | 0.592 | n.s. |
| 5a - 5d | -1.62 | 0.82 | -1.97 | 0.049 | 0.181 | n.s. |
| 5b - 5c | 1.57 | 0.69 | 2.28 | 0.023 | 0.108 | n.s. |
| 5b - 5d | 0.60 | 0.66 | 0.91 | 0.361 | 0.592 | n.s. |
| 5c - 5d | -0.96 | 0.67 | -1.43 | 0.154 | 0.394 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.25, *p* = 0.117, η²_G = 0.138
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | -2.16 | 6 | = 0.251 | -0.59 [-1.87, -0.02] | medium | n.s. |
| 5a vs 5c | -0.49 | 6 | = 0.641 | -0.15 [-0.94, 0.51] | negligible | n.s. |
| 5a vs 5d | -1.68 | 6 | = 0.251 | -0.99 [-1.30, 0.33] | large | n.s. |
| 5b vs 5c | 1.91 | 6 | = 0.251 | 0.44 [0.03, 1.15] | small | n.s. |
| 5b vs 5d | -0.75 | 6 | = 0.579 | -0.44 [-0.47, 0.53] | small | n.s. |
| 5c vs 5d | -1.57 | 6 | = 0.251 | -0.85 [-0.62, 0.41] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 555.81, BIC = 571.75
- **5b vs 5a**: *β* = 0.53, *SE* = 3.556, *z* = 0.149, *p* = 0.881
- **5c vs 5a**: *β* = -2.08, *SE* = 3.544, *z* = -0.586, *p* = 0.558
- **5d vs 5a**: *β* = -1.44, *SE* = 3.498, *z* = -0.411, *p* = 0.681
- **SNR**: *β* = 0.24, *SE* = 0.667, *z* = 0.357, *p* = 0.721

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -0.53 | 3.56 | -0.15 | 0.881 | 0.969 | n.s. |
| 5a - 5c | 2.08 | 3.54 | 0.59 | 0.558 | 0.964 | n.s. |
| 5a - 5d | 1.44 | 3.50 | 0.41 | 0.681 | 0.968 | n.s. |
| 5b - 5c | 2.61 | 2.94 | 0.89 | 0.374 | 0.940 | n.s. |
| 5b - 5d | 1.97 | 2.82 | 0.70 | 0.486 | 0.964 | n.s. |
| 5c - 5d | -0.64 | 2.86 | -0.22 | 0.823 | 0.969 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.71, *p* = 0.560, η²_G = 0.086
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | -0.83 | 6 | = 0.877 | -0.46 [-1.25, 0.36] | small | n.s. |
| 5a vs 5c | 0.20 | 6 | = 0.924 | 0.12 [-0.55, 0.89] | negligible | n.s. |
| 5a vs 5d | 0.30 | 6 | = 0.924 | 0.17 [-0.45, 1.13] | negligible | n.s. |
| 5b vs 5c | 0.99 | 6 | = 0.877 | 0.60 [-0.35, 0.69] | medium | n.s. |
| 5b vs 5d | 1.96 | 6 | = 0.585 | 0.64 [-0.37, 0.63] | medium | n.s. |
| 5c vs 5d | 0.10 | 6 | = 0.924 | 0.07 [-0.74, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 188.98, BIC = 201.78
- **5b vs 5a**: *β* = 0.49, *SE* = 0.585, *z* = 0.831, *p* = 0.406
- **5c vs 5a**: *β* = -0.12, *SE* = 0.642, *z* = -0.187, *p* = 0.851
- **5d vs 5a**: *β* = 0.15, *SE* = 0.581, *z* = 0.259, *p* = 0.795
- **SNR**: *β* = 0.91, *SE* = 0.140, *z* = 6.510, *p* < .001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -0.49 | 0.58 | -0.83 | 0.406 | 0.926 | n.s. |
| 5a - 5c | 0.12 | 0.64 | 0.19 | 0.851 | 0.958 | n.s. |
| 5a - 5d | -0.15 | 0.58 | -0.26 | 0.795 | 0.958 | n.s. |
| 5b - 5c | 0.61 | 0.51 | 1.18 | 0.236 | 0.801 | n.s. |
| 5b - 5d | 0.34 | 0.50 | 0.67 | 0.501 | 0.938 | n.s. |
| 5c - 5d | -0.27 | 0.53 | -0.51 | 0.611 | 0.941 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 282.77, BIC = 295.57
- **5b vs 5a**: *β* = -2.44, *SE* = 1.657, *z* = -1.470, *p* = 0.142
- **5c vs 5a**: *β* = -2.61, *SE* = 1.832, *z* = -1.424, *p* = 0.154
- **5d vs 5a**: *β* = -0.69, *SE* = 1.661, *z* = -0.416, *p* = 0.677
- **SNR**: *β* = 0.16, *SE* = 0.383, *z* = 0.427, *p* = 0.670

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 2.44 | 1.66 | 1.47 | 0.142 | 0.600 | n.s. |
| 5a - 5c | 2.61 | 1.83 | 1.42 | 0.154 | 0.600 | n.s. |
| 5a - 5d | 0.69 | 1.66 | 0.42 | 0.677 | 0.896 | n.s. |
| 5b - 5c | 0.17 | 1.45 | 0.12 | 0.904 | 0.904 | n.s. |
| 5b - 5d | -1.74 | 1.41 | -1.24 | 0.215 | 0.600 | n.s. |
| 5c - 5d | -1.92 | 1.51 | -1.27 | 0.203 | 0.600 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 186.91, BIC = 199.40
- **5b vs 5a**: *β* = -2.38, *SE* = 0.909, *z* = -2.616, *p* = 0.009
- **5c vs 5a**: *β* = -1.26, *SE* = 0.879, *z* = -1.434, *p* = 0.151
- **5d vs 5a**: *β* = -2.27, *SE* = 0.871, *z* = -2.602, *p* = 0.009
- **SNR**: *β* = 0.75, *SE* = 0.145, *z* = 5.152, *p* < .001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 2.38 | 0.91 | 2.62 | 0.009 | 0.052 | n.s. |
| 5a - 5c | 1.26 | 0.88 | 1.43 | 0.151 | 0.355 | n.s. |
| 5a - 5d | 2.27 | 0.87 | 2.60 | 0.009 | 0.052 | n.s. |
| 5b - 5c | -1.12 | 0.69 | -1.63 | 0.104 | 0.355 | n.s. |
| 5b - 5d | -0.11 | 0.66 | -0.17 | 0.863 | 0.863 | n.s. |
| 5c - 5d | 1.00 | 0.65 | 1.55 | 0.120 | 0.355 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 314.87, BIC = 327.36
- **5b vs 5a**: *β* = 2.28, *SE* = 3.060, *z* = 0.746, *p* = 0.456
- **5c vs 5a**: *β* = 2.75, *SE* = 3.890, *z* = 0.706, *p* = 0.480
- **5d vs 5a**: *β* = 1.27, *SE* = 3.608, *z* = 0.351, *p* = 0.726
- **SNR**: *β* = -0.28, *SE* = 0.369, *z* = -0.757, *p* = 0.449

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -2.28 | 3.06 | -0.75 | 0.456 | 0.974 | n.s. |
| 5a - 5c | -2.75 | 3.89 | -0.71 | 0.480 | 0.974 | n.s. |
| 5a - 5d | -1.27 | 3.61 | -0.35 | 0.726 | 0.979 | n.s. |
| 5b - 5c | -0.46 | 1.59 | -0.29 | 0.771 | 0.979 | n.s. |
| 5b - 5d | 1.02 | nan | 0.00 | 1.000 | 1.000 | n.s. |
| 5c - 5d | 1.48 | 2.55 | 0.58 | 0.561 | 0.974 | n.s. |

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
