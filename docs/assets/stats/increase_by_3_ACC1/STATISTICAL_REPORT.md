# Statistical Analysis Report: tables

**Generated:** 2025-10-20 22:52:03

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
| 1 to 4 | 21 | -4.38 µV | 2.51 | 0.55 | [-9.98, -0.67] |
| 2 to 5 | 24 | -3.71 µV | 2.17 | 0.44 | [-10.03, -0.13] |
| 3 to 6 | 23 | -4.61 µV | 2.42 | 0.51 | [-10.48, -1.16] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 21 | 174.63 ms | 12.64 | 2.76 | [152.99, 206.92] |
| 2 to 5 | 24 | 175.63 ms | 13.69 | 2.79 | [149.83, 205.26] |
| 3 to 6 | 23 | 173.66 ms | 12.11 | 2.53 | [154.54, 199.39] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 2.00 µV | 1.03 | 0.29 | [0.21, 3.25] |
| 2 to 5 | 11 | 1.48 µV | 1.56 | 0.47 | [-0.04, 5.47] |
| 3 to 6 | 10 | 2.50 µV | 1.84 | 0.58 | [0.23, 6.64] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 93.46 ms | 5.63 | 1.56 | [83.65, 100.47] |
| 2 to 5 | 11 | 89.97 ms | 8.57 | 2.58 | [76.25, 101.78] |
| 3 to 6 | 10 | 89.37 ms | 7.30 | 2.31 | [78.68, 99.56] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 3.80 µV | 2.81 | 0.63 | [0.45, 10.48] |
| 2 to 5 | 23 | 3.05 µV | 2.09 | 0.44 | [0.09, 6.95] |
| 3 to 6 | 18 | 2.70 µV | 1.74 | 0.41 | [0.48, 7.48] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 448.02 ms | 30.48 | 6.82 | [393.69, 507.04] |
| 2 to 5 | 23 | 446.07 ms | 36.27 | 7.56 | [377.85, 520.11] |
| 3 to 6 | 18 | 456.66 ms | 19.14 | 4.51 | [419.80, 487.53] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 274.93, BIC = 288.25
- **2 to 5 vs 1 to 4**: *β* = 0.02, *SE* = 0.422, *z* = 0.049, *p* = 0.961
- **3 to 6 vs 1 to 4**: *β* = -0.53, *SE* = 0.418, *z* = -1.267, *p* = 0.205
- **SNR**: *β* = -0.53, *SE* = 0.101, *z* = -5.258, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.02 | 0.42 | -0.05 | 0.961 | 0.961 | n.s. |
| 1 to 4 - 3 to 6 | 0.53 | 0.42 | 1.27 | 0.205 | 0.441 | n.s. |
| 2 to 5 - 3 to 6 | 0.55 | 0.41 | 1.35 | 0.176 | 0.441 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.23, *p* = 0.303, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.61 | 20 | = 0.551 | -0.12 [-0.59, 0.32] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.87 | 20 | = 0.551 | 0.20 [-0.27, 0.65] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 1.69 | 20 | = 0.322 | 0.34 [-0.04, 0.87] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 518.45, BIC = 531.77
- **2 to 5 vs 1 to 4**: *β* = 0.47, *SE* = 2.132, *z* = 0.218, *p* = 0.827
- **3 to 6 vs 1 to 4**: *β* = -0.68, *SE* = 2.102, *z* = -0.324, *p* = 0.746
- **SNR**: *β* = 0.21, *SE* = 0.540, *z* = 0.382, *p* = 0.702

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.47 | 2.13 | -0.22 | 0.827 | 0.935 | n.s. |
| 1 to 4 - 3 to 6 | 0.68 | 2.10 | 0.32 | 0.746 | 0.935 | n.s. |
| 2 to 5 - 3 to 6 | 1.15 | 2.05 | 0.56 | 0.576 | 0.924 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.72, *p* = 0.491, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.44 | 20 | = 0.663 | -0.07 [-0.55, 0.36] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.67 | 20 | = 0.663 | 0.13 [-0.31, 0.60] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 1.33 | 20 | = 0.596 | 0.21 [-0.36, 0.50] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 96.78, BIC = 105.94
- **2 to 5 vs 1 to 4**: *β* = 0.11, *SE* = 0.302, *z* = 0.368, *p* = 0.713
- **3 to 6 vs 1 to 4**: *β* = 0.01, *SE* = 0.303, *z* = 0.019, *p* = 0.985
- **SNR**: *β* = 0.77, *SE* = 0.124, *z* = 6.207, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.11 | 0.30 | -0.37 | 0.713 | 0.976 | n.s. |
| 1 to 4 - 3 to 6 | -0.01 | 0.30 | -0.02 | 0.985 | 0.985 | n.s. |
| 2 to 5 - 3 to 6 | 0.11 | 0.34 | 0.31 | 0.760 | 0.976 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 1.25 | 1 | = 0.519 | 1.43 [-0.72, 1.45] | large | n.s. |
| 1 to 4 vs 3 to 6 | 1.16 | 1 | = 0.519 | 0.55 [-1.36, 1.13] | medium | n.s. |
| 2 to 5 vs 3 to 6 | -0.94 | 1 | = 0.519 | -1.19 [-2.03, 1.27] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 228.40, BIC = 237.56
- **2 to 5 vs 1 to 4**: *β* = -1.37, *SE* = 2.521, *z* = -0.542, *p* = 0.588
- **3 to 6 vs 1 to 4**: *β* = -4.60, *SE* = 2.410, *z* = -1.908, *p* = 0.056
- **SNR**: *β* = 2.51, *SE* = 0.995, *z* = 2.520, *p* = 0.012

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 1.37 | 2.52 | 0.54 | 0.588 | 0.588 | n.s. |
| 1 to 4 - 3 to 6 | 4.60 | 2.41 | 1.91 | 0.056 | 0.160 | n.s. |
| 2 to 5 - 3 to 6 | 3.23 | 2.95 | 1.09 | 0.274 | 0.473 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 23.85 | 1 | = 0.080 | 1.74 [-0.45, 1.91] | large | n.s. |
| 1 to 4 vs 3 to 6 | 0.33 | 1 | = 0.795 | 0.41 [-0.57, 2.37] | small | n.s. |
| 2 to 5 vs 3 to 6 | -1.59 | 1 | = 0.537 | -1.91 [-1.85, 1.38] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 221.35, BIC = 234.01
- **2 to 5 vs 1 to 4**: *β* = -0.07, *SE* = 0.350, *z* = -0.196, *p* = 0.844
- **3 to 6 vs 1 to 4**: *β* = -0.05, *SE* = 0.390, *z* = -0.119, *p* = 0.906
- **SNR**: *β* = 0.62, *SE* = 0.074, *z* = 8.413, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 0.07 | 0.35 | 0.20 | 0.844 | 0.996 | n.s. |
| 1 to 4 - 3 to 6 | 0.05 | 0.39 | 0.12 | 0.906 | 0.996 | n.s. |
| 2 to 5 - 3 to 6 | -0.02 | 0.36 | -0.06 | 0.951 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.59, *p* = 0.039, η²_G = 0.073
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 1.14 | 16 | = 0.270 | 0.26 [-0.32, 0.65] | small | n.s. |
| 1 to 4 vs 3 to 6 | 2.82 | 16 | = 0.037 | 0.63 [0.11, 1.26] | medium | * |
| 2 to 5 vs 3 to 6 | 1.46 | 16 | = 0.246 | 0.45 [-0.18, 0.84] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 595.38, BIC = 608.05
- **2 to 5 vs 1 to 4**: *β* = -4.69, *SE* = 8.425, *z* = -0.556, *p* = 0.578
- **3 to 6 vs 1 to 4**: *β* = 4.55, *SE* = 9.200, *z* = 0.495, *p* = 0.621
- **SNR**: *β* = -1.97, *SE* = 1.550, *z* = -1.270, *p* = 0.204

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 4.69 | 8.42 | 0.56 | 0.578 | 0.822 | n.s. |
| 1 to 4 - 3 to 6 | -4.55 | 9.20 | -0.49 | 0.621 | 0.822 | n.s. |
| 2 to 5 - 3 to 6 | -9.24 | 8.61 | -1.07 | 0.283 | 0.632 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.60, *p* = 0.217, η²_G = 0.058
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.49 | 16 | = 0.632 | 0.14 [-0.29, 0.68] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | -1.15 | 16 | = 0.398 | -0.43 [-0.80, 0.24] | small | n.s. |
| 2 to 5 vs 3 to 6 | -1.88 | 16 | = 0.236 | -0.61 [-0.89, 0.14] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.039). Post-hoc tests revealed:
  - 1 to 4 showed greater amplitude than 3 to 6 (*d* = 0.63)

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

- Python 3.12.4
- MNE-Python 1.9.0
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
