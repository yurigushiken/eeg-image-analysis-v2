# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:36:14

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
| Cardinality1 | 17 | 112.94 ms | 10.44 | 2.53 | [96.00, 124.00] |
| Cardinality2 | 15 | 110.93 ms | 9.50 | 2.45 | [96.00, 124.00] |
| Cardinality3 | 11 | 112.00 ms | 9.80 | 2.95 | [96.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 17 | -2.97 µV | 2.17 | 0.53 | [-9.03, -0.50] |
| Cardinality2 | 15 | -2.40 µV | 1.33 | 0.34 | [-5.94, -0.68] |
| Cardinality3 | 11 | -3.66 µV | 1.92 | 0.58 | [-8.81, -1.48] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | 178.13 ms | 18.69 | 4.83 | [148.00, 204.00] |
| Cardinality2 | 22 | 174.91 ms | 19.91 | 4.25 | [148.00, 204.00] |
| Cardinality3 | 23 | 170.26 ms | 16.48 | 3.44 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | -4.87 µV | 1.87 | 0.48 | [-9.64, -2.66] |
| Cardinality2 | 22 | -5.56 µV | 2.42 | 0.52 | [-10.20, -1.57] |
| Cardinality3 | 23 | -5.13 µV | 2.00 | 0.42 | [-10.83, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 18 | 119.56 ms | 8.77 | 2.07 | [104.00, 128.00] |
| Cardinality2 | 12 | 117.67 ms | 9.57 | 2.76 | [104.00, 128.00] |
| Cardinality3 | 14 | 115.71 ms | 9.21 | 2.46 | [104.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 18 | 4.78 µV | 2.94 | 0.69 | [1.39, 13.50] |
| Cardinality2 | 12 | 3.37 µV | 1.85 | 0.53 | [1.11, 7.57] |
| Cardinality3 | 14 | 3.23 µV | 2.35 | 0.63 | [0.94, 8.96] |


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
- AIC = 325.22, BIC = 335.79
- **Cardinality2 vs Cardinality1**: *β* = -0.30, *SE* = 3.263, *z* = -0.093, *p* = 0.926
- **Cardinality3 vs Cardinality1**: *β* = -0.69, *SE* = 3.732, *z* = -0.185, *p* = 0.853
- **SNR**: *β* = 1.83, *SE* = 1.652, *z* = 1.106, *p* = 0.269

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.30 | 3.26 | 0.09 | 0.926 | 0.997 | n.s. |
| Cardinality1 - Cardinality3 | 0.69 | 3.73 | 0.19 | 0.853 | 0.997 | n.s. |
| Cardinality2 - Cardinality3 | 0.39 | 3.81 | 0.10 | 0.919 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.23, *p* = 0.083, η²_G = 0.189
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.75 | 5 | = 0.212 | 0.69 [-0.81, 0.54] | medium | n.s. |
| Cardinality1 vs Cardinality3 | -0.52 | 5 | = 0.624 | -0.22 [-0.99, 0.86] | small | n.s. |
| Cardinality2 vs Cardinality3 | -2.89 | 5 | = 0.102 | -1.37 [-1.56, 0.16] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 159.60, BIC = 170.17
- **Cardinality2 vs Cardinality1**: *β* = -0.04, *SE* = 0.469, *z* = -0.082, *p* = 0.935
- **Cardinality3 vs Cardinality1**: *β* = -0.41, *SE* = 0.506, *z* = -0.802, *p* = 0.423
- **SNR**: *β* = -1.00, *SE* = 0.184, *z* = -5.426, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.04 | 0.47 | 0.08 | 0.935 | 0.935 | n.s. |
| Cardinality1 - Cardinality3 | 0.41 | 0.51 | 0.80 | 0.423 | 0.808 | n.s. |
| Cardinality2 - Cardinality3 | 0.37 | 0.51 | 0.71 | 0.476 | 0.808 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.11, *p* = 0.898, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.781 (ε = 0.560)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | -0.50 | 5 | = 0.838 | -0.17 [-1.03, 0.35] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | -0.24 | 5 | = 0.838 | -0.13 [-1.20, 0.68] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.21 | 5 | = 0.838 | 0.09 [-0.36, 1.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 510.74, BIC = 523.31
- **Cardinality2 vs Cardinality1**: *β* = -1.88, *SE* = 3.998, *z* = -0.470, *p* = 0.638
- **Cardinality3 vs Cardinality1**: *β* = -6.83, *SE* = 4.024, *z* = -1.697, *p* = 0.090
- **SNR**: *β* = 0.89, *SE* = 0.629, *z* = 1.409, *p* = 0.159

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 1.88 | 4.00 | 0.47 | 0.638 | 0.638 | n.s. |
| Cardinality1 - Cardinality3 | 6.83 | 4.02 | 1.70 | 0.090 | 0.245 | n.s. |
| Cardinality2 - Cardinality3 | 4.95 | 3.50 | 1.42 | 0.157 | 0.289 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.399, η²_G = 0.018
- Greenhouse-Geisser corrected: *p* = 0.372 (ε = 0.689)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.15 | 13 | = 0.882 | 0.04 [-0.45, 0.66] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 1.91 | 13 | = 0.234 | 0.33 [-0.10, 1.13] | small | n.s. |
| Cardinality2 vs Cardinality3 | 1.12 | 13 | = 0.425 | 0.25 [-0.16, 0.77] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 229.45, BIC = 242.02
- **Cardinality2 vs Cardinality1**: *β* = -1.03, *SE* = 0.468, *z* = -2.197, *p* = 0.028
- **Cardinality3 vs Cardinality1**: *β* = -0.48, *SE* = 0.466, *z* = -1.021, *p* = 0.307
- **SNR**: *β* = -0.45, *SE* = 0.063, *z* = -7.160, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 1.03 | 0.47 | 2.20 | 0.028 | 0.082 | n.s. |
| Cardinality1 - Cardinality3 | 0.48 | 0.47 | 1.02 | 0.307 | 0.325 | n.s. |
| Cardinality2 - Cardinality3 | -0.55 | 0.41 | -1.35 | 0.178 | 0.325 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.268, η²_G = 0.047
- Greenhouse-Geisser corrected: *p* = 0.266 (ε = 0.664)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.23 | 13 | = 0.359 | 0.49 [-0.27, 0.86] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.35 | 13 | = 0.359 | 0.41 [-0.24, 0.96] | small | n.s. |
| Cardinality2 vs Cardinality3 | -0.58 | 13 | = 0.574 | -0.12 [-0.66, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 324.90, BIC = 335.61
- **Cardinality2 vs Cardinality1**: *β* = -0.24, *SE* = 3.203, *z* = -0.076, *p* = 0.940
- **Cardinality3 vs Cardinality1**: *β* = -2.67, *SE* = 3.005, *z* = -0.889, *p* = 0.374
- **SNR**: *β* = 1.13, *SE* = 0.746, *z* = 1.512, *p* = 0.130

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.24 | 3.20 | 0.08 | 0.940 | 0.940 | n.s. |
| Cardinality1 - Cardinality3 | 2.67 | 3.01 | 0.89 | 0.374 | 0.755 | n.s. |
| Cardinality2 - Cardinality3 | 2.43 | 3.29 | 0.74 | 0.461 | 0.755 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.86, *p* = 0.193, η²_G = 0.106
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.83 | 7 | = 0.435 | 0.36 [-0.81, 0.73] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.77 | 7 | = 0.358 | 0.79 [-0.14, 1.22] | medium | n.s. |
| Cardinality2 vs Cardinality3 | 1.18 | 7 | = 0.416 | 0.42 [-0.47, 1.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 185.59, BIC = 196.30
- **Cardinality2 vs Cardinality1**: *β* = -0.96, *SE* = 0.605, *z* = -1.586, *p* = 0.113
- **Cardinality3 vs Cardinality1**: *β* = -0.90, *SE* = 0.547, *z* = -1.652, *p* = 0.099
- **SNR**: *β* = 0.71, *SE* = 0.131, *z* = 5.418, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.96 | 0.60 | 1.59 | 0.113 | 0.268 | n.s. |
| Cardinality1 - Cardinality3 | 0.90 | 0.55 | 1.65 | 0.099 | 0.268 | n.s. |
| Cardinality2 - Cardinality3 | -0.06 | 0.59 | -0.09 | 0.925 | 0.925 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.65, *p* = 0.028, η²_G = 0.196
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 4.96 | 7 | = 0.005 | 1.04 [0.07, 1.97] | large | ** |
| Cardinality1 vs Cardinality3 | 1.92 | 7 | = 0.145 | 0.81 [0.07, 1.54] | large | n.s. |
| Cardinality2 vs Cardinality3 | -0.40 | 7 | = 0.701 | -0.18 [-1.00, 0.55] | negligible | n.s. |

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

**Fz latency:** Marginal trend toward condition differences (*p* = 0.083)
**P1 amplitude:** Significant main effect of condition (*p* = 0.028). Post-hoc tests revealed:
  - Cardinality1 showed greater amplitude than Cardinality2 (*d* = 1.04)

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
