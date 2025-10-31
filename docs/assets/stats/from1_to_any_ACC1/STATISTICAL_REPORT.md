# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:20:16

---

## 1. Analysis Overview

**Total Measurements:** 216
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
| 1 to 2 | 22 | -3.10 µV | 1.59 | 0.34 | [-5.90, -0.56] |
| 1 to 3 | 24 | -3.72 µV | 1.79 | 0.36 | [-7.87, -0.73] |
| 1 to 4 | 21 | -4.38 µV | 2.51 | 0.55 | [-9.98, -0.67] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | 174.41 ms | 15.38 | 3.28 | [150.32, 209.78] |
| 1 to 3 | 24 | 175.70 ms | 13.30 | 2.71 | [150.40, 206.73] |
| 1 to 4 | 21 | 174.63 ms | 12.64 | 2.76 | [152.99, 206.92] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 1.46 µV | 1.25 | 0.36 | [0.19, 3.62] |
| 1 to 3 | 9 | 1.77 µV | 1.02 | 0.34 | [0.21, 3.63] |
| 1 to 4 | 15 | 1.63 µV | 1.13 | 0.29 | [0.05, 3.66] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 85.53 ms | 7.63 | 2.20 | [73.21, 96.58] |
| 1 to 3 | 9 | 85.46 ms | 7.27 | 2.42 | [77.58, 98.89] |
| 1 to 4 | 15 | 86.56 ms | 6.83 | 1.76 | [76.72, 99.51] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 3.46 µV | 2.74 | 0.68 | [0.20, 10.38] |
| 1 to 3 | 20 | 4.10 µV | 3.30 | 0.74 | [0.41, 12.29] |
| 1 to 4 | 20 | 3.79 µV | 2.83 | 0.63 | [0.43, 10.61] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 456.25 ms | 35.84 | 8.96 | [390.52, 532.17] |
| 1 to 3 | 20 | 454.86 ms | 23.55 | 5.27 | [398.45, 485.46] |
| 1 to 4 | 20 | 453.78 ms | 29.32 | 6.56 | [394.98, 508.73] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 249.04, BIC = 262.27
- **1 to 3 vs 1 to 2**: *β* = -0.27, *SE* = 0.359, *z* = -0.746, *p* = 0.456
- **1 to 4 vs 1 to 2**: *β* = -0.87, *SE* = 0.372, *z* = -2.329, *p* = 0.020
- **SNR**: *β* = -0.41, *SE* = 0.076, *z* = -5.416, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.27 | 0.36 | 0.75 | 0.456 | 0.456 | n.s. |
| 1 to 2 - 1 to 4 | 0.87 | 0.37 | 2.33 | 0.020 | 0.058 | n.s. |
| 1 to 3 - 1 to 4 | 0.60 | 0.36 | 1.66 | 0.097 | 0.184 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.133, η²_G = 0.036
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 1.68 | 18 | = 0.166 | 0.34 [-0.09, 0.82] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.81 | 18 | = 0.166 | 0.43 [-0.09, 0.92] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.77 | 18 | = 0.450 | 0.17 [-0.27, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 518.28, BIC = 531.51
- **1 to 3 vs 1 to 2**: *β* = 1.15, *SE* = 2.178, *z* = 0.528, *p* = 0.598
- **1 to 4 vs 1 to 2**: *β* = 1.87, *SE* = 2.265, *z* = 0.824, *p* = 0.410
- **SNR**: *β* = 0.38, *SE* = 0.529, *z* = 0.723, *p* = 0.469

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -1.15 | 2.18 | -0.53 | 0.598 | 0.838 | n.s. |
| 1 to 2 - 1 to 4 | -1.87 | 2.26 | -0.82 | 0.410 | 0.795 | n.s. |
| 1 to 3 - 1 to 4 | -0.72 | 2.20 | -0.33 | 0.744 | 0.838 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.678, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.09 | 18 | = 0.929 | 0.02 [-0.55, 0.34] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.77 | 18 | = 0.674 | -0.12 [-0.66, 0.31] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -0.94 | 18 | = 0.674 | -0.16 [-0.64, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 91.78, BIC = 101.28
- **1 to 3 vs 1 to 2**: *β* = 0.62, *SE* = 0.326, *z* = 1.890, *p* = 0.059
- **1 to 4 vs 1 to 2**: *β* = 0.43, *SE* = 0.290, *z* = 1.491, *p* = 0.136
- **SNR**: *β* = 0.51, *SE* = 0.076, *z* = 6.700, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.62 | 0.33 | -1.89 | 0.059 | 0.166 | n.s. |
| 1 to 2 - 1 to 4 | -0.43 | 0.29 | -1.49 | 0.136 | 0.253 | n.s. |
| 1 to 3 - 1 to 4 | 0.19 | 0.31 | 0.59 | 0.553 | 0.553 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.50, *p* = 0.642, η²_G = 0.088
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.30 | 2 | = 0.789 | -0.74 [-1.47, 0.70] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -0.76 | 2 | = 0.789 | -0.39 [-1.04, 0.81] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.17 | 2 | = 0.881 | 0.14 [-1.40, 0.75] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 252.18, BIC = 261.68
- **1 to 3 vs 1 to 2**: *β* = -0.31, *SE* = 2.821, *z* = -0.110, *p* = 0.913
- **1 to 4 vs 1 to 2**: *β* = 0.62, *SE* = 2.498, *z* = 0.247, *p* = 0.805
- **SNR**: *β* = -0.53, *SE* = 0.682, *z* = -0.772, *p* = 0.440

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.31 | 2.82 | 0.11 | 0.913 | 0.981 | n.s. |
| 1 to 2 - 1 to 4 | -0.62 | 2.50 | -0.25 | 0.805 | 0.981 | n.s. |
| 1 to 3 - 1 to 4 | -0.93 | 2.70 | -0.34 | 0.732 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.44, *p* = 0.135, η²_G = 0.356
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 3.12 | 2 | = 0.240 | 1.22 [-0.62, 1.60] | large | n.s. |
| 1 to 2 vs 1 to 4 | -0.54 | 2 | = 0.646 | -0.30 [-1.18, 0.69] | small | n.s. |
| 1 to 3 vs 1 to 4 | -2.19 | 2 | = 0.240 | -1.53 [-1.06, 1.04] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 226.90, BIC = 239.05
- **1 to 3 vs 1 to 2**: *β* = 0.36, *SE* = 0.449, *z* = 0.795, *p* = 0.427
- **1 to 4 vs 1 to 2**: *β* = 0.17, *SE* = 0.437, *z* = 0.391, *p* = 0.696
- **SNR**: *β* = 0.58, *SE* = 0.089, *z* = 6.505, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.36 | 0.45 | -0.79 | 0.427 | 0.812 | n.s. |
| 1 to 2 - 1 to 4 | -0.17 | 0.44 | -0.39 | 0.696 | 0.869 | n.s. |
| 1 to 3 - 1 to 4 | 0.19 | 0.39 | 0.47 | 0.638 | 0.869 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.11, *p* = 0.141, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.84 | 13 | = 0.267 | -0.41 [-1.10, 0.12] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.37 | 13 | = 0.293 | -0.31 [-0.90, 0.23] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.70 | 13 | = 0.498 | 0.12 [-0.29, 0.68] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 546.69, BIC = 558.84
- **1 to 3 vs 1 to 2**: *β* = -1.31, *SE* = 9.337, *z* = -0.140, *p* = 0.889
- **1 to 4 vs 1 to 2**: *β* = -2.21, *SE* = 9.301, *z* = -0.237, *p* = 0.812
- **SNR**: *β* = 0.09, *SE* = 1.406, *z* = 0.061, *p* = 0.952

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 1.31 | 9.34 | 0.14 | 0.889 | 0.993 | n.s. |
| 1 to 2 - 1 to 4 | 2.21 | 9.30 | 0.24 | 0.812 | 0.993 | n.s. |
| 1 to 3 - 1 to 4 | 0.90 | 8.69 | 0.10 | 0.918 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.31, *p* = 0.735, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.79 | 13 | = 0.714 | -0.28 [-0.79, 0.37] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.38 | 13 | = 0.714 | -0.17 [-0.54, 0.57] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.47 | 13 | = 0.714 | 0.13 [-0.57, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


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
