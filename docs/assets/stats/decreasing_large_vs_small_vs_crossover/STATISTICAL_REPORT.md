# Statistical Analysis Report: tables

**Generated:** 2025-10-20 21:49:46

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
| Decreasing Crossover | 24 | -3.72 µV | 1.65 | 0.34 | [-7.49, -0.68] |
| Decreasing Large | 24 | -3.63 µV | 1.71 | 0.35 | [-7.33, -0.90] |
| Decreasing Small | 21 | -2.61 µV | 2.04 | 0.45 | [-7.35, 0.07] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 177.68 ms | 7.82 | 1.60 | [164.59, 203.37] |
| Decreasing Large | 24 | 177.44 ms | 8.67 | 1.77 | [162.89, 200.21] |
| Decreasing Small | 21 | 177.88 ms | 8.93 | 1.95 | [162.37, 203.72] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 16 | 1.58 µV | 1.35 | 0.34 | [0.05, 4.69] |
| Decreasing Large | 13 | 2.09 µV | 1.57 | 0.43 | [0.38, 4.71] |
| Decreasing Small | 19 | 1.92 µV | 1.62 | 0.37 | [0.13, 6.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 16 | 113.58 ms | 5.17 | 1.29 | [104.02, 123.07] |
| Decreasing Large | 13 | 112.12 ms | 3.42 | 0.95 | [105.02, 116.72] |
| Decreasing Small | 19 | 113.16 ms | 3.88 | 0.89 | [103.38, 118.08] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 20 | 3.47 µV | 2.41 | 0.54 | [0.17, 9.09] |
| Decreasing Large | 18 | 2.74 µV | 2.16 | 0.51 | [0.23, 6.23] |
| Decreasing Small | 20 | 3.71 µV | 2.41 | 0.54 | [0.61, 8.10] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 20 | 483.32 ms | 16.35 | 3.66 | [451.80, 533.77] |
| Decreasing Large | 18 | 486.75 ms | 21.14 | 4.98 | [447.09, 527.81] |
| Decreasing Small | 20 | 485.41 ms | 13.33 | 2.98 | [455.35, 505.97] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 245.17, BIC = 258.57
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.41, *SE* = 0.318, *z* = -1.276, *p* = 0.202
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.50, *SE* = 0.363, *z* = 1.377, *p* = 0.168
- **SNR**: *β* = -0.10, *SE* = 0.028, *z* = -3.691, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.41 | 0.32 | 1.28 | 0.202 | 0.309 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.50 | 0.36 | -1.38 | 0.168 | 0.309 | n.s. |
| Decreasing Large - Decreasing Small | -0.91 | 0.31 | -2.93 | 0.003 | 0.010 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.92, *p* < .001, η²_G = 0.099
- Greenhouse-Geisser corrected: *p* = 0.003 (ε = 0.665)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -0.37 | 20 | = 0.715 | -0.05 [-0.51, 0.33] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -3.74 | 20 | = 0.004 | -0.68 [-1.34, -0.29] | medium | ** |
| Decreasing Large vs Decreasing Small | -2.79 | 20 | = 0.017 | -0.64 [-1.10, -0.11] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 429.77, BIC = 443.17
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.67, *SE* = 0.952, *z* = -0.703, *p* = 0.482
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.09, *SE* = 1.096, *z* = 0.085, *p* = 0.933
- **SNR**: *β* = -0.09, *SE* = 0.088, *z* = -1.024, *p* = 0.306

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.67 | 0.95 | 0.70 | 0.482 | 0.794 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.09 | 1.10 | -0.08 | 0.933 | 0.933 | n.s. |
| Decreasing Large - Decreasing Small | -0.76 | 0.92 | -0.82 | 0.410 | 0.794 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.65, *p* = 0.528, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.33 | 20 | = 0.746 | 0.03 [-0.36, 0.48] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.96 | 20 | = 0.559 | -0.09 [-0.67, 0.25] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -0.91 | 20 | = 0.559 | -0.12 [-0.66, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 137.18, BIC = 148.40
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.54, *SE* = 0.245, *z* = 2.198, *p* = 0.028
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.66, *SE* = 0.228, *z* = 2.900, *p* = 0.004
- **SNR**: *β* = 0.19, *SE* = 0.045, *z* = 4.278, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.54 | 0.25 | -2.20 | 0.028 | 0.055 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.66 | 0.23 | -2.90 | 0.004 | 0.011 | * |
| Decreasing Large - Decreasing Small | -0.12 | 0.24 | -0.51 | 0.607 | 0.607 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.217, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.66 | 11 | = 0.188 | -0.26 [-1.15, 0.19] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.78 | 11 | = 0.188 | -0.34 [-1.20, 0.04] | small | n.s. |
| Decreasing Large vs Decreasing Small | -0.44 | 11 | = 0.666 | -0.10 [-0.76, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 279.21, BIC = 290.44
- **Decreasing Large vs Decreasing Crossover**: *β* = -1.84, *SE* = 1.164, *z* = -1.580, *p* = 0.114
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.39, *SE* = 1.149, *z* = 0.337, *p* = 0.736
- **SNR**: *β* = -0.17, *SE* = 0.175, *z* = -1.000, *p* = 0.317

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 1.84 | 1.16 | 1.58 | 0.114 | 0.215 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.39 | 1.15 | -0.34 | 0.736 | 0.736 | n.s. |
| Decreasing Large - Decreasing Small | -2.23 | 1.21 | -1.84 | 0.066 | 0.185 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.50, *p* = 0.048, η²_G = 0.125
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 2.12 | 11 | = 0.086 | 0.56 [-0.08, 1.30] | medium | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.58 | 11 | = 0.575 | -0.21 [-0.94, 0.25] | small | n.s. |
| Decreasing Large vs Decreasing Small | -2.59 | 11 | = 0.076 | -1.02 [-1.40, -0.04] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 222.79, BIC = 235.16
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.19, *SE* = 0.409, *z* = 0.465, *p* = 0.642
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.95, *SE* = 0.371, *z* = 2.564, *p* = 0.010
- **SNR**: *β* = 0.16, *SE* = 0.028, *z* = 5.731, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.19 | 0.41 | -0.47 | 0.642 | 0.642 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.95 | 0.37 | -2.56 | 0.010 | 0.031 | * |
| Decreasing Large - Decreasing Small | -0.76 | 0.36 | -2.09 | 0.036 | 0.071 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.76, *p* = 0.033, η²_G = 0.052
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.83 | 17 | = 0.128 | 0.43 [-0.09, 0.95] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.73 | 17 | = 0.474 | -0.11 [-0.61, 0.36] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -2.38 | 17 | = 0.087 | -0.54 [-1.10, -0.03] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 499.54, BIC = 511.91
- **Decreasing Large vs Decreasing Crossover**: *β* = 2.11, *SE* = 5.187, *z* = 0.407, *p* = 0.684
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.97, *SE* = 4.808, *z* = 0.201, *p* = 0.840
- **SNR**: *β* = -0.26, *SE* = 0.328, *z* = -0.777, *p* = 0.437

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -2.11 | 5.19 | -0.41 | 0.684 | 0.968 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.97 | 4.81 | -0.20 | 0.840 | 0.968 | n.s. |
| Decreasing Large - Decreasing Small | 1.14 | 4.77 | 0.24 | 0.810 | 0.968 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.36, *p* = 0.700, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -0.65 | 17 | = 0.785 | -0.21 [-0.65, 0.35] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.23 | 17 | = 0.821 | -0.06 [-0.62, 0.35] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | 0.65 | 17 | = 0.785 | 0.18 [-0.35, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller amplitude than Decreasing Small (*d* = -0.68)
  - Decreasing Large showed smaller amplitude than Decreasing Small (*d* = -0.64)
**P1 latency:** Significant main effect of condition (*p* = 0.048) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.033) (no significant pairwise comparisons)

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
