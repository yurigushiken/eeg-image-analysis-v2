# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:50:39

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
| Decrease by 1 | 23 | -3.24 µV | 1.69 | 0.35 | [-7.59, -0.16] |
| Decrease by 2 | 24 | -3.34 µV | 1.73 | 0.35 | [-7.40, -0.61] |
| Decrease by 3 | 24 | -3.49 µV | 1.68 | 0.34 | [-6.76, -0.62] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 23 | 178.16 ms | 11.47 | 2.39 | [162.35, 211.06] |
| Decrease by 2 | 24 | 178.92 ms | 9.33 | 1.91 | [162.83, 203.97] |
| Decrease by 3 | 24 | 179.25 ms | 8.97 | 1.83 | [161.48, 203.36] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 14 | 1.69 µV | 1.48 | 0.39 | [0.16, 4.45] |
| Decrease by 2 | 17 | 1.79 µV | 1.05 | 0.25 | [0.18, 4.87] |
| Decrease by 3 | 17 | 2.12 µV | 1.71 | 0.42 | [0.49, 7.24] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 14 | 112.74 ms | 4.09 | 1.09 | [103.50, 118.35] |
| Decrease by 2 | 17 | 112.74 ms | 3.49 | 0.85 | [103.42, 117.27] |
| Decrease by 3 | 17 | 112.82 ms | 3.70 | 0.90 | [104.90, 118.33] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 20 | 3.49 µV | 2.34 | 0.52 | [0.07, 7.33] |
| Decrease by 2 | 19 | 3.61 µV | 1.72 | 0.39 | [0.80, 6.64] |
| Decrease by 3 | 20 | 3.84 µV | 2.68 | 0.60 | [0.10, 10.31] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 20 | 482.59 ms | 20.52 | 4.59 | [431.05, 532.72] |
| Decrease by 2 | 19 | 477.92 ms | 11.05 | 2.53 | [455.80, 493.72] |
| Decrease by 3 | 20 | 482.42 ms | 15.43 | 3.45 | [454.10, 521.85] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 220.18, BIC = 233.76
- **Decrease by 2 vs Decrease by 1**: *β* = -0.02, *SE* = 0.214, *z* = -0.106, *p* = 0.915
- **Decrease by 3 vs Decrease by 1**: *β* = -0.12, *SE* = 0.215, *z* = -0.579, *p* = 0.563
- **SNR**: *β* = -0.15, *SE* = 0.025, *z* = -6.092, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.02 | 0.21 | 0.11 | 0.915 | 0.916 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.12 | 0.22 | 0.58 | 0.563 | 0.916 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.10 | 0.21 | 0.49 | 0.627 | 0.916 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.69, *p* = 0.506, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.80 | 22 | = 0.648 | 0.13 [-0.27, 0.60] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.23 | 22 | = 0.648 | 0.19 [-0.18, 0.70] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.36 | 22 | = 0.725 | 0.06 [-0.31, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 485.88, BIC = 499.45
- **Decrease by 2 vs Decrease by 1**: *β* = 0.20, *SE* = 1.313, *z* = 0.153, *p* = 0.878
- **Decrease by 3 vs Decrease by 1**: *β* = 0.53, *SE* = 1.321, *z* = 0.404, *p* = 0.686
- **SNR**: *β* = 0.01, *SE* = 0.156, *z* = 0.037, *p* = 0.970

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.20 | 1.31 | -0.15 | 0.878 | 0.969 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.53 | 1.32 | -0.40 | 0.686 | 0.969 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.33 | 1.28 | -0.26 | 0.796 | 0.969 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.10, *p* = 0.906, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.04 | 22 | = 0.967 | -0.01 [-0.44, 0.42] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.36 | 22 | = 0.967 | -0.05 [-0.51, 0.36] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.46 | 22 | = 0.967 | -0.06 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 139.66, BIC = 150.89
- **Decrease by 2 vs Decrease by 1**: *β* = 0.03, *SE* = 0.270, *z* = 0.111, *p* = 0.912
- **Decrease by 3 vs Decrease by 1**: *β* = 0.46, *SE* = 0.269, *z* = 1.698, *p* = 0.089
- **SNR**: *β* = 0.29, *SE* = 0.052, *z* = 5.478, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.03 | 0.27 | -0.11 | 0.912 | 0.912 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.46 | 0.27 | -1.70 | 0.089 | 0.240 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.43 | 0.25 | -1.71 | 0.087 | 0.240 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.266, η²_G = 0.038
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.88 | 10 | = 0.491 | -0.25 [-0.88, 0.41] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.13 | 10 | = 0.178 | -0.41 [-1.38, 0.03] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.72 | 10 | = 0.491 | -0.25 [-0.75, 0.36] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 247.47, BIC = 258.70
- **Decrease by 2 vs Decrease by 1**: *β* = -0.05, *SE* = 0.694, *z* = -0.067, *p* = 0.947
- **Decrease by 3 vs Decrease by 1**: *β* = 0.30, *SE* = 0.686, *z* = 0.445, *p* = 0.656
- **SNR**: *β* = 0.13, *SE* = 0.148, *z* = 0.887, *p* = 0.375

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.05 | 0.69 | 0.07 | 0.947 | 0.947 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.31 | 0.69 | -0.45 | 0.656 | 0.925 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.35 | 0.63 | -0.56 | 0.579 | 0.925 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.45, *p* = 0.645, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.20 | 10 | = 0.849 | 0.05 [-0.61, 0.66] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.61 | 10 | = 0.833 | -0.15 [-0.87, 0.42] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.40 | 10 | = 0.576 | -0.22 [-0.65, 0.46] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 217.95, BIC = 230.41
- **Decrease by 2 vs Decrease by 1**: *β* = -0.03, *SE* = 0.312, *z* = -0.086, *p* = 0.931
- **Decrease by 3 vs Decrease by 1**: *β* = 0.18, *SE* = 0.311, *z* = 0.591, *p* = 0.554
- **SNR**: *β* = 0.17, *SE* = 0.046, *z* = 3.784, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.03 | 0.31 | 0.09 | 0.931 | 0.931 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.18 | 0.31 | -0.59 | 0.554 | 0.877 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.21 | 0.31 | -0.67 | 0.503 | 0.877 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.74, *p* = 0.192, η²_G = 0.015
- Greenhouse-Geisser corrected: *p* = 0.203 (ε = 0.685)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 1.24 | 16 | = 0.303 | 0.15 [-0.30, 0.70] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.07 | 16 | = 0.303 | -0.15 [-0.76, 0.25] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.46 | 16 | = 0.303 | -0.29 [-0.76, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 487.99, BIC = 500.45
- **Decrease by 2 vs Decrease by 1**: *β* = -5.17, *SE* = 3.088, *z* = -1.673, *p* = 0.094
- **Decrease by 3 vs Decrease by 1**: *β* = -3.46, *SE* = 3.111, *z* = -1.113, *p* = 0.266
- **SNR**: *β* = 0.31, *SE* = 0.392, *z* = 0.781, *p* = 0.435

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 5.17 | 3.09 | 1.67 | 0.094 | 0.257 | n.s. |
| Decrease by 1 - Decrease by 3 | 3.46 | 3.11 | 1.11 | 0.266 | 0.461 | n.s. |
| Decrease by 2 - Decrease by 3 | -1.70 | 3.12 | -0.55 | 0.585 | 0.585 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.07, *p* = 0.143, η²_G = 0.051
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 1.93 | 16 | = 0.214 | 0.53 [-0.14, 0.89] | medium | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.54 | 16 | = 0.215 | 0.39 [-0.11, 0.93] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.45 | 16 | = 0.658 | -0.13 [-0.65, 0.35] | negligible | n.s. |

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
