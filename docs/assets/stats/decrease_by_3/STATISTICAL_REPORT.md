# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:17:13

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
| 4 to 1 | 18 | -1.84 µV | 1.51 | 0.36 | [-5.32, -0.25] |
| 5 to 2 | 24 | -4.29 µV | 2.42 | 0.49 | [-9.05, -0.37] |
| 6 to 3 | 24 | -4.02 µV | 1.94 | 0.40 | [-8.26, -0.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 18 | 183.11 ms | 13.12 | 3.09 | [162.61, 207.59] |
| 5 to 2 | 24 | 178.49 ms | 9.77 | 2.00 | [158.83, 196.24] |
| 6 to 3 | 24 | 181.59 ms | 12.07 | 2.46 | [163.43, 217.21] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 3.71 µV | 2.60 | 0.63 | [0.67, 10.85] |
| 5 to 2 | 15 | 2.03 µV | 1.52 | 0.39 | [0.14, 4.79] |
| 6 to 3 | 12 | 1.66 µV | 1.59 | 0.46 | [0.03, 5.33] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 114.76 ms | 3.45 | 0.84 | [108.83, 119.94] |
| 5 to 2 | 15 | 113.05 ms | 6.94 | 1.79 | [98.47, 125.15] |
| 6 to 3 | 12 | 110.56 ms | 8.42 | 2.43 | [98.24, 122.79] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 21 | 3.78 µV | 2.61 | 0.57 | [0.27, 8.86] |
| 5 to 2 | 18 | 3.52 µV | 2.42 | 0.57 | [0.23, 9.86] |
| 6 to 3 | 19 | 3.96 µV | 2.60 | 0.60 | [1.27, 11.02] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 21 | 468.96 ms | 21.98 | 4.80 | [439.26, 513.40] |
| 5 to 2 | 18 | 462.16 ms | 24.52 | 5.78 | [405.96, 518.66] |
| 6 to 3 | 19 | 458.05 ms | 24.05 | 5.52 | [402.54, 502.28] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 250.61, BIC = 263.75
- **5 to 2 vs 4 to 1**: *β* = -1.84, *SE* = 0.412, *z* = -4.467, *p* < .001
- **6 to 3 vs 4 to 1**: *β* = -1.56, *SE* = 0.413, *z* = -3.770, *p* < .001
- **SNR**: *β* = -0.40, *SE* = 0.067, *z* = -6.002, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.84 | 0.41 | 4.47 | < .001 | < .001 | *** |
| 4 to 1 - 6 to 3 | 1.56 | 0.41 | 3.77 | < .001 | < .001 | *** |
| 5 to 2 - 6 to 3 | -0.28 | 0.35 | -0.82 | 0.414 | 0.414 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 20.40, *p* < .001, η²_G = 0.338
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 5.99 | 17 | < .001 | 1.68 [0.71, 2.11] | large | *** |
| 4 to 1 vs 6 to 3 | 3.97 | 17 | = 0.001 | 1.31 [0.34, 1.53] | large | ** |
| 5 to 2 vs 6 to 3 | -1.96 | 17 | = 0.067 | -0.37 [-0.57, 0.28] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 504.82, BIC = 517.96
- **5 to 2 vs 4 to 1**: *β* = -4.64, *SE* = 2.714, *z* = -1.709, *p* = 0.087
- **6 to 3 vs 4 to 1**: *β* = -1.55, *SE* = 2.720, *z* = -0.570, *p* = 0.569
- **SNR**: *β* = 0.24, *SE* = 0.446, *z* = 0.531, *p* = 0.596

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 4.64 | 2.71 | 1.71 | 0.087 | 0.240 | n.s. |
| 4 to 1 - 6 to 3 | 1.55 | 2.72 | 0.57 | 0.569 | 0.569 | n.s. |
| 5 to 2 - 6 to 3 | -3.09 | 2.30 | -1.34 | 0.179 | 0.326 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.87, *p* = 0.428, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.16 | 17 | = 0.506 | 0.31 [-0.23, 0.78] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.45 | 17 | = 0.661 | 0.09 [-0.39, 0.60] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -0.99 | 17 | = 0.506 | -0.20 [-0.72, 0.15] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 167.78, BIC = 178.49
- **5 to 2 vs 4 to 1**: *β* = -0.67, *SE* = 0.517, *z* = -1.295, *p* = 0.195
- **6 to 3 vs 4 to 1**: *β* = -0.88, *SE* = 0.577, *z* = -1.519, *p* = 0.129
- **SNR**: *β* = 0.64, *SE* = 0.110, *z* = 5.834, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.67 | 0.52 | 1.29 | 0.195 | 0.353 | n.s. |
| 4 to 1 - 6 to 3 | 0.88 | 0.58 | 1.52 | 0.129 | 0.339 | n.s. |
| 5 to 2 - 6 to 3 | 0.21 | 0.54 | 0.39 | 0.698 | 0.698 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.39, *p* = 0.018, η²_G = 0.233
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.07 | 7 | = 0.116 | 0.91 [-0.05, 1.35] | large | n.s. |
| 4 to 1 vs 6 to 3 | 3.42 | 7 | = 0.034 | 1.04 [0.03, 1.72] | large | * |
| 5 to 2 vs 6 to 3 | 0.51 | 7 | = 0.628 | 0.21 [-0.47, 1.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 295.35, BIC = 306.05
- **5 to 2 vs 4 to 1**: *β* = -1.53, *SE* = 2.129, *z* = -0.718, *p* = 0.473
- **6 to 3 vs 4 to 1**: *β* = -3.33, *SE* = 2.357, *z* = -1.412, *p* = 0.158
- **SNR**: *β* = 0.39, *SE* = 0.506, *z* = 0.763, *p* = 0.445

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.53 | 2.13 | 0.72 | 0.473 | 0.682 | n.s. |
| 4 to 1 - 6 to 3 | 3.33 | 2.36 | 1.41 | 0.158 | 0.403 | n.s. |
| 5 to 2 - 6 to 3 | 1.80 | 2.31 | 0.78 | 0.436 | 0.682 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.48, *p* = 0.261, η²_G = 0.119
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.28 | 7 | = 0.171 | 1.03 [-0.08, 1.30] | large | n.s. |
| 4 to 1 vs 6 to 3 | 1.48 | 7 | = 0.275 | 0.72 [-0.21, 1.33] | medium | n.s. |
| 5 to 2 vs 6 to 3 | 0.12 | 7 | = 0.907 | 0.06 [-0.80, 0.74] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 236.87, BIC = 249.24
- **5 to 2 vs 4 to 1**: *β* = -0.19, *SE* = 0.398, *z* = -0.485, *p* = 0.628
- **6 to 3 vs 4 to 1**: *β* = 0.37, *SE* = 0.404, *z* = 0.927, *p* = 0.354
- **SNR**: *β* = 0.17, *SE* = 0.045, *z* = 3.876, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.19 | 0.40 | 0.49 | 0.628 | 0.628 | n.s. |
| 4 to 1 - 6 to 3 | -0.37 | 0.40 | -0.93 | 0.354 | 0.582 | n.s. |
| 5 to 2 - 6 to 3 | -0.57 | 0.40 | -1.41 | 0.159 | 0.406 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.550, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 0.72 | 16 | = 0.723 | 0.15 [-0.29, 0.72] | negligible | n.s. |
| 4 to 1 vs 6 to 3 | -0.24 | 16 | = 0.815 | -0.04 [-0.57, 0.46] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -1.32 | 16 | = 0.621 | -0.20 [-0.85, 0.21] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 530.72, BIC = 543.09
- **5 to 2 vs 4 to 1**: *β* = -7.89, *SE* = 5.637, *z* = -1.400, *p* = 0.162
- **6 to 3 vs 4 to 1**: *β* = -9.44, *SE* = 5.750, *z* = -1.643, *p* = 0.100
- **SNR**: *β* = -0.64, *SE* = 0.561, *z* = -1.149, *p* = 0.251

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 7.89 | 5.64 | 1.40 | 0.162 | 0.297 | n.s. |
| 4 to 1 - 6 to 3 | 9.44 | 5.75 | 1.64 | 0.100 | 0.272 | n.s. |
| 5 to 2 - 6 to 3 | 1.55 | 5.83 | 0.27 | 0.790 | 0.790 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.65, *p* = 0.207, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.79 | 16 | = 0.279 | 0.46 [-0.22, 0.80] | small | n.s. |
| 4 to 1 vs 6 to 3 | 1.23 | 16 | = 0.357 | 0.31 [-0.23, 0.82] | small | n.s. |
| 5 to 2 vs 6 to 3 | -0.57 | 16 | = 0.579 | -0.16 [-0.65, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 1.68)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.31)
**P1 amplitude:** Significant main effect of condition (*p* = 0.018). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.04)

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
