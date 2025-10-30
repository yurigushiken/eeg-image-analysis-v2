# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:54:35

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
| Increase by 1 | 23 | -3.29 µV | 1.52 | 0.32 | [-5.84, -0.31] |
| Increase by 2 | 24 | -3.55 µV | 1.88 | 0.38 | [-8.61, -0.40] |
| Increase by 3 | 23 | -4.25 µV | 2.22 | 0.46 | [-9.94, -0.68] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 23 | 169.48 ms | 9.92 | 2.07 | [149.20, 193.25] |
| Increase by 2 | 24 | 172.68 ms | 11.43 | 2.33 | [151.69, 201.25] |
| Increase by 3 | 23 | 173.27 ms | 10.71 | 2.23 | [155.77, 197.32] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 14 | 1.20 µV | 1.18 | 0.32 | [0.18, 3.62] |
| Increase by 2 | 15 | 0.92 µV | 1.02 | 0.26 | [-0.04, 3.73] |
| Increase by 3 | 13 | 1.47 µV | 1.08 | 0.30 | [0.19, 4.04] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 14 | 95.51 ms | 5.98 | 1.60 | [82.36, 105.31] |
| Increase by 2 | 15 | 96.33 ms | 6.31 | 1.63 | [83.56, 107.16] |
| Increase by 3 | 13 | 96.51 ms | 5.31 | 1.47 | [87.86, 106.09] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 17 | 3.17 µV | 2.25 | 0.55 | [0.24, 7.45] |
| Increase by 2 | 18 | 4.10 µV | 2.44 | 0.57 | [0.83, 9.13] |
| Increase by 3 | 19 | 3.40 µV | 2.05 | 0.47 | [0.55, 8.10] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 17 | 471.19 ms | 21.86 | 5.30 | [408.43, 509.00] |
| Increase by 2 | 18 | 471.04 ms | 11.88 | 2.80 | [445.18, 490.49] |
| Increase by 3 | 19 | 463.52 ms | 15.83 | 3.63 | [431.83, 492.89] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 235.29, BIC = 248.78
- **Increase by 2 vs Increase by 1**: *β* = -0.40, *SE* = 0.240, *z* = -1.655, *p* = 0.098
- **Increase by 3 vs Increase by 1**: *β* = -1.06, *SE* = 0.242, *z* = -4.369, *p* < .001
- **SNR**: *β* = -0.10, *SE* = 0.028, *z* = -3.728, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.40 | 0.24 | 1.66 | 0.098 | 0.098 | n.s. |
| Increase by 1 - Increase by 3 | 1.06 | 0.24 | 4.37 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.66 | 0.24 | 2.74 | 0.006 | 0.012 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.85, *p* = 0.003, η²_G = 0.044
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.67 | 22 | = 0.109 | 0.23 [-0.10, 0.79] | small | n.s. |
| Increase by 1 vs Increase by 3 | 3.28 | 22 | = 0.010 | 0.50 [0.20, 1.16] | medium | * |
| Increase by 2 vs Increase by 3 | 2.25 | 22 | = 0.052 | 0.28 [0.01, 0.92] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 505.95, BIC = 519.44
- **Increase by 2 vs Increase by 1**: *β* = 2.22, *SE* = 1.693, *z* = 1.312, *p* = 0.190
- **Increase by 3 vs Increase by 1**: *β* = 3.57, *SE* = 1.703, *z* = 2.095, *p* = 0.036
- **SNR**: *β* = -0.23, *SE* = 0.180, *z* = -1.251, *p* = 0.211

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -2.22 | 1.69 | -1.31 | 0.190 | 0.343 | n.s. |
| Increase by 1 - Increase by 3 | -3.57 | 1.70 | -2.10 | 0.036 | 0.105 | n.s. |
| Increase by 2 - Increase by 3 | -1.35 | 1.70 | -0.79 | 0.427 | 0.427 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.43, *p* = 0.099, η²_G = 0.024
- Greenhouse-Geisser corrected: *p* = 0.123 (ε = 0.651)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.98 | 22 | = 0.340 | -0.20 [-0.64, 0.23] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -1.89 | 22 | = 0.108 | -0.37 [-0.84, 0.06] | small | n.s. |
| Increase by 2 vs Increase by 3 | -2.06 | 22 | = 0.108 | -0.18 [-0.88, 0.02] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 90.84, BIC = 101.27
- **Increase by 2 vs Increase by 1**: *β* = 0.05, *SE* = 0.230, *z* = 0.224, *p* = 0.823
- **Increase by 3 vs Increase by 1**: *β* = 0.04, *SE* = 0.235, *z* = 0.175, *p* = 0.861

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.05 | 0.23 | -0.22 | 0.823 | 0.994 | n.s. |
| Increase by 1 - Increase by 3 | -0.04 | 0.23 | -0.18 | 0.861 | 0.994 | n.s. |
| Increase by 2 - Increase by 3 | 0.01 | 0.23 | 0.05 | 0.964 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.254, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.75 | 8 | = 0.473 | 0.22 [-0.50, 0.95] | small | n.s. |
| Increase by 1 vs Increase by 3 | -0.87 | 8 | = 0.473 | -0.22 [-1.15, 0.34] | small | n.s. |
| Increase by 2 vs Increase by 3 | -2.10 | 8 | = 0.207 | -0.43 [-1.28, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.86, BIC = 286.28
- **Increase by 2 vs Increase by 1**: *β* = 0.42, *SE* = 1.964, *z* = 0.213, *p* = 0.831
- **Increase by 3 vs Increase by 1**: *β* = 0.69, *SE* = 1.988, *z* = 0.344, *p* = 0.730
- **SNR**: *β* = 0.01, *SE* = 0.378, *z* = 0.033, *p* = 0.974

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.42 | 1.96 | -0.21 | 0.831 | 0.980 | n.s. |
| Increase by 1 - Increase by 3 | -0.68 | 1.99 | -0.34 | 0.730 | 0.980 | n.s. |
| Increase by 2 - Increase by 3 | -0.27 | 1.99 | -0.13 | 0.894 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.00, *p* = 0.997, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.02 | 8 | = 0.982 | 0.01 [-0.61, 0.83] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.09 | 8 | = 0.982 | 0.03 [-0.78, 0.65] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.05 | 8 | = 0.982 | 0.02 [-0.63, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 185.88, BIC = 197.82
- **Increase by 2 vs Increase by 1**: *β* = 0.66, *SE* = 0.284, *z* = 2.329, *p* = 0.020
- **Increase by 3 vs Increase by 1**: *β* = 0.52, *SE* = 0.265, *z* = 1.970, *p* = 0.049
- **SNR**: *β* = 0.16, *SE* = 0.038, *z* = 4.250, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.66 | 0.28 | -2.33 | 0.020 | 0.058 | n.s. |
| Increase by 1 - Increase by 3 | -0.52 | 0.27 | -1.97 | 0.049 | 0.095 | n.s. |
| Increase by 2 - Increase by 3 | 0.14 | 0.28 | 0.49 | 0.621 | 0.621 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.46, *p* = 0.010, η²_G = 0.039
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -3.59 | 15 | = 0.008 | -0.45 [-1.53, -0.27] | small | ** |
| Increase by 1 vs Increase by 3 | -1.54 | 15 | = 0.144 | -0.24 [-0.89, 0.17] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.64 | 15 | = 0.144 | 0.25 [-0.11, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 462.92, BIC = 474.85
- **Increase by 2 vs Increase by 1**: *β* = -0.50, *SE* = 4.789, *z* = -0.104, *p* = 0.917
- **Increase by 3 vs Increase by 1**: *β* = -8.62, *SE* = 4.610, *z* = -1.870, *p* = 0.062
- **SNR**: *β* = -0.25, *SE* = 0.496, *z* = -0.512, *p* = 0.609

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.50 | 4.79 | 0.10 | 0.917 | 0.917 | n.s. |
| Increase by 1 - Increase by 3 | 8.62 | 4.61 | 1.87 | 0.062 | 0.173 | n.s. |
| Increase by 2 - Increase by 3 | 8.12 | 4.73 | 1.72 | 0.086 | 0.173 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.264, η²_G = 0.036
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.01 | 15 | = 0.993 | 0.00 [-0.53, 0.54] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.43 | 15 | = 0.259 | 0.36 [-0.10, 0.98] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.99 | 15 | = 0.194 | 0.51 [-0.11, 0.93] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.50)
**N1 latency:** Marginal trend toward condition differences (*p* = 0.099)
**P3b amplitude:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.45)

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
