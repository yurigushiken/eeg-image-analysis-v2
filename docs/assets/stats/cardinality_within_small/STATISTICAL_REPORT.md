# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:15:48

---

## 1. Analysis Overview

**Total Measurements:** 216
**Number of Subjects:** 24
**Number of Conditions:** 3

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

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 111.83 ms | 11.47 | 2.34 | [96.00, 124.00] |
| Cardinality2 | 24 | 111.50 ms | 10.17 | 2.08 | [96.00, 124.00] |
| Cardinality3 | 24 | 110.33 ms | 11.49 | 2.35 | [96.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | -2.00 µV | 2.64 | 0.54 | [-9.03, 3.91] |
| Cardinality2 | 24 | -1.13 µV | 2.22 | 0.45 | [-5.94, 4.65] |
| Cardinality3 | 24 | -1.48 µV | 2.64 | 0.54 | [-8.81, 2.75] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 180.83 ms | 17.21 | 3.51 | [148.00, 204.00] |
| Cardinality2 | 24 | 174.83 ms | 19.11 | 3.90 | [148.00, 204.00] |
| Cardinality3 | 24 | 171.67 ms | 17.53 | 3.58 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | -3.22 µV | 2.66 | 0.54 | [-9.64, 0.56] |
| Cardinality2 | 24 | -5.17 µV | 2.65 | 0.54 | [-10.20, -0.87] |
| Cardinality3 | 24 | -5.09 µV | 1.97 | 0.40 | [-10.83, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 118.17 ms | 9.65 | 1.97 | [104.00, 128.00] |
| Cardinality2 | 24 | 115.33 ms | 9.41 | 1.92 | [104.00, 128.00] |
| Cardinality3 | 24 | 115.17 ms | 9.43 | 1.93 | [104.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 3.67 µV | 3.37 | 0.69 | [-3.41, 13.50] |
| Cardinality2 | 24 | 1.03 µV | 3.15 | 0.64 | [-7.98, 7.57] |
| Cardinality3 | 24 | 1.63 µV | 2.88 | 0.59 | [-3.74, 8.96] |


### 2.4 P3b Component

#### Latency (Peak)

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 555.72, BIC = 569.38
- **Cardinality2 vs Cardinality1**: *β* = -0.98, *SE* = 2.850, *z* = -0.344, *p* = 0.731
- **Cardinality3 vs Cardinality1**: *β* = -1.74, *SE* = 2.762, *z* = -0.629, *p* = 0.530
- **SNR**: *β* = -0.99, *SE* = 1.146, *z* = -0.861, *p* = 0.389

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.98 | 2.85 | 0.34 | 0.731 | 0.927 | n.s. |
| Cardinality1 - Cardinality3 | 1.74 | 2.76 | 0.63 | 0.530 | 0.896 | n.s. |
| Cardinality2 - Cardinality3 | 0.75 | 2.79 | 0.27 | 0.787 | 0.927 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.858, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.11 | 23 | = 0.912 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 0.56 | 23 | = 0.912 | 0.13 [-0.31, 0.54] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.41 | 23 | = 0.912 | 0.11 [-0.34, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 339.10, BIC = 352.76
- **Cardinality2 vs Cardinality1**: *β* = 0.76, *SE* = 0.615, *z* = 1.236, *p* = 0.216
- **Cardinality3 vs Cardinality1**: *β* = 0.48, *SE* = 0.595, *z* = 0.801, *p* = 0.423
- **SNR**: *β* = -0.18, *SE* = 0.254, *z* = -0.691, *p* = 0.490

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | -0.76 | 0.61 | -1.24 | 0.216 | 0.519 | n.s. |
| Cardinality1 - Cardinality3 | -0.48 | 0.59 | -0.80 | 0.423 | 0.667 | n.s. |
| Cardinality2 - Cardinality3 | 0.28 | 0.60 | 0.47 | 0.637 | 0.667 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.352, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | -1.60 | 23 | = 0.367 | -0.36 [-0.76, 0.11] | small | n.s. |
| Cardinality1 vs Cardinality3 | -0.73 | 23 | = 0.515 | -0.20 [-0.57, 0.28] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.66 | 23 | = 0.515 | 0.15 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 610.53, BIC = 624.19
- **Cardinality2 vs Cardinality1**: *β* = -6.18, *SE* = 3.489, *z* = -1.770, *p* = 0.077
- **Cardinality3 vs Cardinality1**: *β* = -9.57, *SE* = 3.507, *z* = -2.730, *p* = 0.006
- **SNR**: *β* = 0.64, *SE* = 0.627, *z* = 1.022, *p* = 0.307

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 6.18 | 3.49 | 1.77 | 0.077 | 0.147 | n.s. |
| Cardinality1 - Cardinality3 | 9.57 | 3.51 | 2.73 | 0.006 | 0.019 | * |
| Cardinality2 - Cardinality3 | 3.40 | 3.49 | 0.97 | 0.331 | 0.331 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.32, *p* = 0.045, η²_G = 0.045
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.51 | 23 | = 0.218 | 0.33 [-0.12, 0.74] | small | n.s. |
| Cardinality1 vs Cardinality3 | 2.84 | 23 | = 0.028 | 0.53 [0.12, 1.04] | medium | * |
| Cardinality2 vs Cardinality3 | 0.88 | 23 | = 0.389 | 0.17 [-0.25, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 291.07, BIC = 304.73
- **Cardinality2 vs Cardinality1**: *β* = -1.81, *SE* = 0.443, *z* = -4.080, *p* < .001
- **Cardinality3 vs Cardinality1**: *β* = -1.53, *SE* = 0.445, *z* = -3.440, *p* = 0.001
- **SNR**: *β* = -0.53, *SE* = 0.070, *z* = -7.627, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 1.81 | 0.44 | 4.08 | < .001 | < .001 | *** |
| Cardinality1 - Cardinality3 | 1.53 | 0.44 | 3.44 | < .001 | 0.001 | ** |
| Cardinality2 - Cardinality3 | -0.28 | 0.44 | -0.63 | 0.531 | 0.531 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.71, *p* = 0.001, η²_G = 0.124
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 2.88 | 23 | = 0.013 | 0.74 [0.13, 1.05] | medium | * |
| Cardinality1 vs Cardinality3 | 3.61 | 23 | = 0.004 | 0.80 [0.26, 1.21] | medium | ** |
| Cardinality2 vs Cardinality3 | -0.18 | 23 | = 0.855 | -0.04 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 525.48, BIC = 539.14
- **Cardinality2 vs Cardinality1**: *β* = -2.74, *SE* = 2.045, *z* = -1.340, *p* = 0.180
- **Cardinality3 vs Cardinality1**: *β* = -2.87, *SE* = 2.054, *z* = -1.396, *p* = 0.163
- **SNR**: *β* = 0.21, *SE* = 0.439, *z* = 0.483, *p* = 0.629

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 2.74 | 2.05 | 1.34 | 0.180 | 0.413 | n.s. |
| Cardinality1 - Cardinality3 | 2.87 | 2.05 | 1.40 | 0.163 | 0.413 | n.s. |
| Cardinality2 - Cardinality3 | 0.13 | 2.04 | 0.06 | 0.950 | 0.950 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.31, *p* = 0.279, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.27 | 23 | = 0.345 | 0.30 [-0.17, 0.69] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.23 | 23 | = 0.345 | 0.31 [-0.18, 0.68] | small | n.s. |
| Cardinality2 vs Cardinality3 | 0.11 | 23 | = 0.910 | 0.02 [-0.40, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 363.02, BIC = 376.68
- **Cardinality2 vs Cardinality1**: *β* = -2.64, *SE* = 0.645, *z* = -4.087, *p* < .001
- **Cardinality3 vs Cardinality1**: *β* = -2.03, *SE* = 0.648, *z* = -3.137, *p* = 0.002
- **SNR**: *β* = 0.01, *SE* = 0.141, *z* = 0.058, *p* = 0.954

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 2.64 | 0.65 | 4.09 | < .001 | < .001 | *** |
| Cardinality1 - Cardinality3 | 2.03 | 0.65 | 3.14 | 0.002 | 0.003 | ** |
| Cardinality2 - Cardinality3 | -0.60 | 0.64 | -0.94 | 0.348 | 0.348 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.91, *p* < .001, η²_G = 0.119
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 4.10 | 23 | = 0.001 | 0.81 [0.35, 1.33] | large | ** |
| Cardinality1 vs Cardinality3 | 3.05 | 23 | = 0.009 | 0.65 [0.16, 1.08] | medium | ** |
| Cardinality2 vs Cardinality3 | -0.92 | 23 | = 0.368 | -0.20 [-0.61, 0.24] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.045). Post-hoc tests revealed:
  - Cardinality1 showed greater latency than Cardinality3 (*d* = 0.53)
**N1 amplitude:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - Cardinality1 showed greater amplitude than Cardinality2 (*d* = 0.74)
  - Cardinality1 showed greater amplitude than Cardinality3 (*d* = 0.80)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality1 showed greater amplitude than Cardinality2 (*d* = 0.81)
  - Cardinality1 showed greater amplitude than Cardinality3 (*d* = 0.65)

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

**Boxplot:**

![P1 Latency Boxplot](plots/boxplot_P1_latency_frac_area_ms.png)

**Violin Plot:**

![P1 Latency Violin](plots/violin_P1_latency_frac_area_ms.png)

#### Amplitude

**Boxplot:**

![P1 Amplitude Boxplot](plots/boxplot_P1_mean_amplitude_roi.png)

**Violin Plot:**

![P1 Amplitude Violin](plots/violin_P1_mean_amplitude_roi.png)

### 5.4 P3b Component

#### Latency

#### Amplitude

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
