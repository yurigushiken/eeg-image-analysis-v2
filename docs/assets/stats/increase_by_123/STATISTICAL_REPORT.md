# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:22:03

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
| Increase by 1 | 23 | -3.36 µV | 1.54 | 0.32 | [-6.64, -0.20] |
| Increase by 2 | 24 | -3.53 µV | 1.80 | 0.37 | [-8.23, -0.19] |
| Increase by 3 | 23 | -4.16 µV | 2.12 | 0.44 | [-9.91, -0.74] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 23 | 170.93 ms | 8.34 | 1.74 | [148.91, 186.96] |
| Increase by 2 | 24 | 172.51 ms | 11.53 | 2.35 | [151.44, 200.48] |
| Increase by 3 | 23 | 172.65 ms | 9.93 | 2.07 | [157.01, 194.89] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 13 | 1.04 µV | 0.85 | 0.24 | [-0.02, 2.66] |
| Increase by 2 | 15 | 0.91 µV | 0.97 | 0.25 | [0.00, 3.73] |
| Increase by 3 | 12 | 1.42 µV | 1.23 | 0.36 | [0.19, 4.56] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 13 | 95.49 ms | 6.41 | 1.78 | [80.78, 105.93] |
| Increase by 2 | 15 | 96.26 ms | 6.79 | 1.75 | [83.56, 106.90] |
| Increase by 3 | 12 | 96.30 ms | 5.68 | 1.64 | [87.40, 106.46] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 16 | 2.85 µV | 2.10 | 0.52 | [0.15, 7.24] |
| Increase by 2 | 18 | 3.87 µV | 2.34 | 0.55 | [0.52, 8.48] |
| Increase by 3 | 19 | 3.31 µV | 1.96 | 0.45 | [0.57, 7.94] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 16 | 465.84 ms | 18.28 | 4.57 | [415.65, 493.39] |
| Increase by 2 | 18 | 467.92 ms | 11.99 | 2.83 | [442.14, 489.69] |
| Increase by 3 | 19 | 460.35 ms | 14.30 | 3.28 | [433.81, 484.99] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 228.35, BIC = 241.84
- **Increase by 2 vs Increase by 1**: *β* = -0.50, *SE* = 0.233, *z* = -2.151, *p* = 0.031
- **Increase by 3 vs Increase by 1**: *β* = -1.06, *SE* = 0.236, *z* = -4.484, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.030, *z* = -3.608, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.50 | 0.23 | 2.15 | 0.031 | 0.031 | * |
| Increase by 1 - Increase by 3 | 1.06 | 0.24 | 4.48 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.56 | 0.22 | 2.48 | 0.013 | 0.026 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.59, *p* = 0.007, η²_G = 0.033
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.32 | 22 | = 0.202 | 0.18 [-0.17, 0.71] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 3.24 | 22 | = 0.011 | 0.43 [0.20, 1.16] | small | * |
| Increase by 2 vs Increase by 3 | 1.98 | 22 | = 0.091 | 0.26 [-0.04, 0.86] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 463.88, BIC = 477.37
- **Increase by 2 vs Increase by 1**: *β* = 0.18, *SE* = 1.093, *z* = 0.168, *p* = 0.866
- **Increase by 3 vs Increase by 1**: *β* = 1.37, *SE* = 1.103, *z* = 1.243, *p* = 0.214
- **SNR**: *β* = -0.15, *SE* = 0.140, *z* = -1.064, *p* = 0.287

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.18 | 1.09 | -0.17 | 0.866 | 0.866 | n.s. |
| Increase by 1 - Increase by 3 | -1.37 | 1.10 | -1.24 | 0.214 | 0.514 | n.s. |
| Increase by 2 - Increase by 3 | -1.19 | 1.05 | -1.13 | 0.260 | 0.514 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.252, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.42 | 22 | = 0.682 | -0.04 [-0.52, 0.35] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -1.45 | 22 | = 0.373 | -0.19 [-0.74, 0.14] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.19 | 22 | = 0.373 | -0.14 [-0.69, 0.19] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 61.69, BIC = 71.82
- **Increase by 2 vs Increase by 1**: *β* = 0.30, *SE* = 0.152, *z* = 2.002, *p* = 0.045
- **Increase by 3 vs Increase by 1**: *β* = 0.40, *SE* = 0.154, *z* = 2.619, *p* = 0.009
- **SNR**: *β* = 0.50, *SE* = 0.053, *z* = 9.529, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.30 | 0.15 | -2.00 | 0.045 | 0.089 | n.s. |
| Increase by 1 - Increase by 3 | -0.40 | 0.15 | -2.62 | 0.009 | 0.026 | * |
| Increase by 2 - Increase by 3 | -0.10 | 0.15 | -0.66 | 0.512 | 0.512 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.83, *p* = 0.093, η²_G = 0.057
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.06 | 7 | = 0.954 | 0.02 [-0.75, 0.78] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -1.64 | 7 | = 0.218 | -0.51 [-1.55, 0.16] | medium | n.s. |
| Increase by 2 vs Increase by 3 | -3.19 | 7 | = 0.046 | -0.44 [-1.23, 0.20] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 265.97, BIC = 276.10
- **Increase by 2 vs Increase by 1**: *β* = -0.63, *SE* = 2.016, *z* = -0.312, *p* = 0.755
- **Increase by 3 vs Increase by 1**: *β* = -0.27, *SE* = 1.963, *z* = -0.137, *p* = 0.891
- **SNR**: *β* = -0.00, *SE* = 0.697, *z* = -0.003, *p* = 0.998

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.63 | 2.02 | 0.31 | 0.755 | 0.985 | n.s. |
| Increase by 1 - Increase by 3 | 0.27 | 1.96 | 0.14 | 0.891 | 0.985 | n.s. |
| Increase by 2 - Increase by 3 | -0.36 | 1.89 | -0.19 | 0.849 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.700, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.70 | 7 | = 0.781 | 0.31 [-0.47, 1.11] | small | n.s. |
| Increase by 1 vs Increase by 3 | 0.68 | 7 | = 0.781 | 0.27 [-0.61, 0.94] | small | n.s. |
| Increase by 2 vs Increase by 3 | -0.25 | 7 | = 0.811 | -0.08 [-0.74, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 185.27, BIC = 197.09
- **Increase by 2 vs Increase by 1**: *β* = 0.84, *SE* = 0.328, *z* = 2.560, *p* = 0.010
- **Increase by 3 vs Increase by 1**: *β* = 0.79, *SE* = 0.314, *z* = 2.514, *p* = 0.012
- **SNR**: *β* = 0.21, *SE* = 0.046, *z* = 4.641, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.84 | 0.33 | -2.56 | 0.010 | 0.031 | * |
| Increase by 1 - Increase by 3 | -0.79 | 0.31 | -2.51 | 0.012 | 0.031 | * |
| Increase by 2 - Increase by 3 | 0.05 | 0.31 | 0.16 | 0.870 | 0.870 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.38, *p* = 0.005, η²_G = 0.065
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -3.48 | 15 | = 0.010 | -0.59 [-1.49, -0.24] | medium | * |
| Increase by 1 vs Increase by 3 | -2.14 | 15 | = 0.073 | -0.43 [-1.11, 0.03] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.32 | 15 | = 0.207 | 0.21 [-0.17, 0.86] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 438.13, BIC = 449.95
- **Increase by 2 vs Increase by 1**: *β* = 2.08, *SE* = 3.932, *z* = 0.529, *p* = 0.597
- **Increase by 3 vs Increase by 1**: *β* = -5.56, *SE* = 3.834, *z* = -1.450, *p* = 0.147
- **SNR**: *β* = -0.26, *SE* = 0.430, *z* = -0.613, *p* = 0.540

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -2.08 | 3.93 | -0.53 | 0.597 | 0.597 | n.s. |
| Increase by 1 - Increase by 3 | 5.56 | 3.83 | 1.45 | 0.147 | 0.272 | n.s. |
| Increase by 2 - Increase by 3 | 7.64 | 3.80 | 2.01 | 0.044 | 0.127 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.94, *p* = 0.162, η²_G = 0.049
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.43 | 15 | = 0.672 | -0.13 [-0.64, 0.43] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.50 | 15 | = 0.232 | 0.36 [-0.18, 0.93] | small | n.s. |
| Increase by 2 vs Increase by 3 | 2.03 | 15 | = 0.181 | 0.60 [-0.10, 0.94] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.007). Post-hoc tests revealed:
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.43)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.093)
**P3b amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.59)

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
