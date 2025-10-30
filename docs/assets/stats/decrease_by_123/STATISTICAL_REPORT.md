# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:50:33

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
| Decrease by 1 | 24 | -3.25 µV | 1.73 | 0.35 | [-7.20, -0.57] |
| Decrease by 2 | 24 | -3.33 µV | 1.73 | 0.35 | [-7.57, -0.45] |
| Decrease by 3 | 24 | -3.45 µV | 1.70 | 0.35 | [-7.03, -0.67] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 178.11 ms | 9.78 | 2.00 | [163.12, 202.83] |
| Decrease by 2 | 24 | 178.14 ms | 9.15 | 1.87 | [161.64, 202.34] |
| Decrease by 3 | 24 | 178.42 ms | 8.65 | 1.77 | [161.10, 202.90] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 13 | 1.79 µV | 1.63 | 0.45 | [0.02, 4.57] |
| Decrease by 2 | 17 | 1.75 µV | 1.06 | 0.26 | [0.39, 4.68] |
| Decrease by 3 | 17 | 2.11 µV | 1.72 | 0.42 | [0.59, 7.31] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 13 | 112.08 ms | 4.27 | 1.18 | [100.15, 116.79] |
| Decrease by 2 | 17 | 113.17 ms | 2.73 | 0.66 | [107.92, 117.75] |
| Decrease by 3 | 17 | 112.61 ms | 3.45 | 0.84 | [104.90, 118.33] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 18 | 3.30 µV | 2.00 | 0.47 | [0.17, 6.83] |
| Decrease by 2 | 19 | 3.45 µV | 1.76 | 0.40 | [0.66, 6.57] |
| Decrease by 3 | 20 | 3.69 µV | 2.71 | 0.61 | [-0.02, 10.28] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 18 | 480.38 ms | 17.40 | 4.10 | [431.28, 514.81] |
| Decrease by 2 | 19 | 476.37 ms | 11.30 | 2.59 | [457.03, 493.33] |
| Decrease by 3 | 20 | 481.79 ms | 18.10 | 4.05 | [453.02, 535.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 219.30, BIC = 232.96
- **Decrease by 2 vs Decrease by 1**: *β* = -0.08, *SE* = 0.196, *z* = -0.396, *p* = 0.692
- **Decrease by 3 vs Decrease by 1**: *β* = -0.17, *SE* = 0.196, *z* = -0.863, *p* = 0.388
- **SNR**: *β* = -0.12, *SE* = 0.022, *z* = -5.199, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.08 | 0.20 | 0.40 | 0.692 | 0.871 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.17 | 0.20 | 0.86 | 0.388 | 0.771 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.09 | 0.20 | 0.47 | 0.641 | 0.871 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.689, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.36 | 23 | = 0.724 | 0.05 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.87 | 23 | = 0.724 | 0.12 [-0.25, 0.60] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.49 | 23 | = 0.724 | 0.07 [-0.32, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 467.86, BIC = 481.52
- **Decrease by 2 vs Decrease by 1**: *β* = 0.03, *SE* = 1.036, *z* = 0.032, *p* = 0.974
- **Decrease by 3 vs Decrease by 1**: *β* = 0.33, *SE* = 1.037, *z* = 0.321, *p* = 0.748
- **SNR**: *β* = -0.07, *SE* = 0.117, *z* = -0.574, *p* = 0.566

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.03 | 1.04 | -0.03 | 0.974 | 0.984 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.33 | 1.04 | -0.32 | 0.748 | 0.984 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.30 | 1.04 | -0.29 | 0.773 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.05, *p* = 0.949, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.03 | 23 | = 0.975 | -0.00 [-0.43, 0.42] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.26 | 23 | = 0.975 | -0.03 [-0.48, 0.37] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.28 | 23 | = 0.975 | -0.03 [-0.48, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 139.04, BIC = 150.14
- **Decrease by 2 vs Decrease by 1**: *β* = 0.23, *SE* = 0.291, *z* = 0.788, *p* = 0.431
- **Decrease by 3 vs Decrease by 1**: *β* = 0.55, *SE* = 0.295, *z* = 1.872, *p* = 0.061
- **SNR**: *β* = 0.25, *SE* = 0.052, *z* = 4.863, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.23 | 0.29 | -0.79 | 0.431 | 0.431 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.55 | 0.30 | -1.87 | 0.061 | 0.172 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.32 | 0.27 | -1.21 | 0.228 | 0.404 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.285, η²_G = 0.031
- Greenhouse-Geisser corrected: *p* = 0.281 (ε = 0.649)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.65 | 10 | = 0.532 | -0.19 [-0.78, 0.50] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.61 | 10 | = 0.079 | -0.36 [-1.55, -0.02] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.77 | 10 | = 0.532 | -0.26 [-0.79, 0.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 244.65, BIC = 255.75
- **Decrease by 2 vs Decrease by 1**: *β* = 1.35, *SE* = 0.806, *z* = 1.679, *p* = 0.093
- **Decrease by 3 vs Decrease by 1**: *β* = 1.16, *SE* = 0.824, *z* = 1.411, *p* = 0.158
- **SNR**: *β* = 0.21, *SE* = 0.130, *z* = 1.626, *p* = 0.104

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -1.35 | 0.81 | -1.68 | 0.093 | 0.254 | n.s. |
| Decrease by 1 - Decrease by 3 | -1.16 | 0.82 | -1.41 | 0.158 | 0.291 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.19 | 0.74 | 0.26 | 0.799 | 0.799 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.32, *p* = 0.290, η²_G = 0.032
- Greenhouse-Geisser corrected: *p* = 0.284 (ε = 0.629)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.98 | 10 | = 0.422 | -0.28 [-1.02, 0.29] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.34 | 10 | = 0.422 | -0.37 [-1.10, 0.30] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.84 | 10 | = 0.422 | -0.14 [-0.60, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 200.76, BIC = 213.02
- **Decrease by 2 vs Decrease by 1**: *β* = 0.43, *SE* = 0.294, *z* = 1.471, *p* = 0.141
- **Decrease by 3 vs Decrease by 1**: *β* = 0.62, *SE* = 0.291, *z* = 2.134, *p* = 0.033
- **SNR**: *β* = 0.22, *SE* = 0.041, *z* = 5.366, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.43 | 0.29 | -1.47 | 0.141 | 0.263 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.62 | 0.29 | -2.13 | 0.033 | 0.095 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.19 | 0.29 | -0.65 | 0.513 | 0.513 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.68, *p* = 0.084, η²_G = 0.026
- Greenhouse-Geisser corrected: *p* = 0.105 (ε = 0.702)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.73 | 16 | = 0.477 | -0.09 [-0.69, 0.34] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.05 | 16 | = 0.170 | -0.34 [-1.04, 0.05] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.43 | 16 | = 0.257 | -0.28 [-0.77, 0.24] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 476.66, BIC = 488.92
- **Decrease by 2 vs Decrease by 1**: *β* = -7.07, *SE* = 3.397, *z* = -2.080, *p* = 0.038
- **Decrease by 3 vs Decrease by 1**: *β* = -3.62, *SE* = 3.439, *z* = -1.052, *p* = 0.293
- **SNR**: *β* = -0.05, *SE* = 0.424, *z* = -0.120, *p* = 0.905

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 7.07 | 3.40 | 2.08 | 0.038 | 0.108 | n.s. |
| Decrease by 1 - Decrease by 3 | 3.62 | 3.44 | 1.05 | 0.293 | 0.500 | n.s. |
| Decrease by 2 - Decrease by 3 | -3.45 | 3.30 | -1.04 | 0.296 | 0.500 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.11, *p* = 0.058, η²_G = 0.075
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 2.40 | 16 | = 0.086 | 0.65 [0.03, 1.14] | medium | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.82 | 16 | = 0.131 | 0.49 [-0.10, 0.98] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.53 | 16 | = 0.604 | -0.15 [-0.68, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.084)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.058)

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
