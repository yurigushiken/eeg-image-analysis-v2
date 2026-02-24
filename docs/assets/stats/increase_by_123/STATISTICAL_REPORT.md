# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:22:56

---

## 1. Analysis Overview

**Total Measurements:** 288
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
| Increase by 1 | 24 | 98.83 ms | 8.63 | 1.76 | [88.00, 108.00] |
| Increase by 2 | 24 | 100.00 ms | 7.46 | 1.52 | [88.00, 108.00] |
| Increase by 3 | 24 | 100.00 ms | 8.42 | 1.72 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | -0.97 µV | 1.00 | 0.20 | [-3.28, 0.89] |
| Increase by 2 | 24 | -0.86 µV | 1.16 | 0.24 | [-4.17, 0.73] |
| Increase by 3 | 24 | -0.97 µV | 1.36 | 0.28 | [-3.87, 2.23] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 170.83 ms | 20.51 | 4.19 | [136.00, 208.00] |
| Increase by 2 | 24 | 168.17 ms | 19.96 | 4.08 | [136.00, 208.00] |
| Increase by 3 | 24 | 170.50 ms | 20.32 | 4.15 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | -5.02 µV | 2.18 | 0.44 | [-9.51, -1.04] |
| Increase by 2 | 24 | -5.43 µV | 2.36 | 0.48 | [-10.65, -0.86] |
| Increase by 3 | 24 | -6.06 µV | 2.45 | 0.50 | [-12.86, -1.94] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 96.83 ms | 11.68 | 2.38 | [80.00, 108.00] |
| Increase by 2 | 24 | 96.17 ms | 11.53 | 2.35 | [80.00, 108.00] |
| Increase by 3 | 24 | 95.50 ms | 11.93 | 2.44 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 1.08 µV | 1.28 | 0.26 | [-1.10, 3.90] |
| Increase by 2 | 24 | 1.11 µV | 1.39 | 0.28 | [-1.41, 4.70] |
| Increase by 3 | 24 | 1.36 µV | 1.50 | 0.31 | [-0.77, 5.72] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 477.83 ms | 40.77 | 8.32 | [392.00, 532.00] |
| Increase by 2 | 24 | 476.33 ms | 38.13 | 7.78 | [392.00, 532.00] |
| Increase by 3 | 24 | 470.67 ms | 43.67 | 8.91 | [392.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 2.44 µV | 3.35 | 0.68 | [-3.42, 8.79] |
| Increase by 2 | 24 | 3.80 µV | 3.39 | 0.69 | [-2.45, 9.72] |
| Increase by 3 | 24 | 3.85 µV | 2.59 | 0.53 | [0.31, 9.96] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 490.98, BIC = 504.64
- **Increase by 2 vs Increase by 1**: *β* = 1.60, *SE* = 1.495, *z* = 1.068, *p* = 0.285
- **Increase by 3 vs Increase by 1**: *β* = 1.37, *SE* = 1.479, *z* = 0.926, *p* = 0.354
- **SNR**: *β* = 0.80, *SE* = 0.454, *z* = 1.756, *p* = 0.079

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -1.60 | 1.50 | -1.07 | 0.285 | 0.635 | n.s. |
| Increase by 1 - Increase by 3 | -1.37 | 1.48 | -0.93 | 0.354 | 0.635 | n.s. |
| Increase by 2 - Increase by 3 | 0.23 | 1.48 | 0.15 | 0.878 | 0.878 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.689, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.61 | 23 | = 0.819 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.91 | 23 | = 0.819 | -0.14 [-0.61, 0.24] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 220.56, BIC = 234.22
- **Increase by 2 vs Increase by 1**: *β* = -0.00, *SE* = 0.262, *z* = -0.016, *p* = 0.987
- **Increase by 3 vs Increase by 1**: *β* = -0.05, *SE* = 0.259, *z* = -0.205, *p* = 0.838
- **SNR**: *β* = -0.22, *SE* = 0.075, *z* = -2.897, *p* = 0.004

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.00 | 0.26 | 0.02 | 0.987 | 0.996 | n.s. |
| Increase by 1 - Increase by 3 | 0.05 | 0.26 | 0.20 | 0.838 | 0.996 | n.s. |
| Increase by 2 - Increase by 3 | 0.05 | 0.26 | 0.19 | 0.851 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.11, *p* = 0.893, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.48 | 23 | = 0.993 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.01 | 23 | = 0.993 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.36 | 23 | = 0.993 | 0.09 [-0.35, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 573.96, BIC = 587.62
- **Increase by 2 vs Increase by 1**: *β* = -3.82, *SE* = 2.200, *z* = -1.737, *p* = 0.082
- **Increase by 3 vs Increase by 1**: *β* = -1.65, *SE* = 2.223, *z* = -0.744, *p* = 0.457
- **SNR**: *β* = -0.57, *SE* = 0.285, *z* = -2.010, *p* = 0.044

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 3.82 | 2.20 | 1.74 | 0.082 | 0.227 | n.s. |
| Increase by 1 - Increase by 3 | 1.65 | 2.22 | 0.74 | 0.457 | 0.521 | n.s. |
| Increase by 2 - Increase by 3 | -2.17 | 2.13 | -1.02 | 0.308 | 0.521 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.85, *p* = 0.435, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.16 | 23 | = 0.385 | 0.13 [-0.19, 0.67] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.13 | 23 | = 0.894 | 0.02 [-0.39, 0.45] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.24 | 23 | = 0.385 | -0.12 [-0.68, 0.18] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 272.29, BIC = 285.95
- **Increase by 2 vs Increase by 1**: *β* = -0.65, *SE* = 0.296, *z* = -2.190, *p* = 0.029
- **Increase by 3 vs Increase by 1**: *β* = -1.31, *SE* = 0.299, *z* = -4.397, *p* < .001
- **SNR**: *β* = -0.12, *SE* = 0.038, *z* = -3.042, *p* = 0.002

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.65 | 0.30 | 2.19 | 0.029 | 0.039 | * |
| Increase by 1 - Increase by 3 | 1.31 | 0.30 | 4.40 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.67 | 0.29 | 2.33 | 0.020 | 0.039 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.05, *p* = 0.005, η²_G = 0.034
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.39 | 23 | = 0.179 | 0.18 [-0.15, 0.71] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 3.31 | 23 | = 0.009 | 0.45 [0.21, 1.14] | small | ** |
| Increase by 2 vs Increase by 3 | 2.15 | 23 | = 0.063 | 0.26 [-0.00, 0.88] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 545.53, BIC = 559.19
- **Increase by 2 vs Increase by 1**: *β* = -0.49, *SE* = 2.207, *z* = -0.224, *p* = 0.823
- **Increase by 3 vs Increase by 1**: *β* = -1.36, *SE* = 2.194, *z* = -0.622, *p* = 0.534
- **SNR**: *β* = 0.58, *SE* = 0.827, *z* = 0.705, *p* = 0.481

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.49 | 2.21 | 0.22 | 0.823 | 0.906 | n.s. |
| Increase by 1 - Increase by 3 | 1.37 | 2.19 | 0.62 | 0.534 | 0.899 | n.s. |
| Increase by 2 - Increase by 3 | 0.87 | 2.21 | 0.39 | 0.694 | 0.906 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.18, *p* = 0.838, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.25 | 23 | = 0.807 | 0.06 [-0.37, 0.47] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.71 | 23 | = 0.807 | 0.11 [-0.28, 0.57] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.33 | 23 | = 0.807 | 0.06 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 219.42, BIC = 233.08
- **Increase by 2 vs Increase by 1**: *β* = 0.13, *SE* = 0.222, *z* = 0.569, *p* = 0.570
- **Increase by 3 vs Increase by 1**: *β* = 0.26, *SE* = 0.220, *z* = 1.198, *p* = 0.231
- **SNR**: *β* = 0.33, *SE* = 0.085, *z* = 3.867, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.13 | 0.22 | -0.57 | 0.570 | 0.784 | n.s. |
| Increase by 1 - Increase by 3 | -0.26 | 0.22 | -1.20 | 0.231 | 0.545 | n.s. |
| Increase by 2 - Increase by 3 | -0.14 | 0.22 | -0.62 | 0.535 | 0.784 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.80, *p* = 0.455, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.10 | 23 | = 0.923 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -1.15 | 23 | = 0.391 | -0.20 [-0.66, 0.19] | small | n.s. |
| Increase by 2 vs Increase by 3 | -1.35 | 23 | = 0.391 | -0.17 [-0.71, 0.15] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 745.65, BIC = 759.31
- **Increase by 2 vs Increase by 1**: *β* = -1.45, *SE* = 10.904, *z* = -0.133, *p* = 0.894
- **Increase by 3 vs Increase by 1**: *β* = -8.86, *SE* = 11.005, *z* = -0.805, *p* = 0.421
- **SNR**: *β* = -0.97, *SE* = 0.855, *z* = -1.134, *p* = 0.257

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 1.45 | 10.90 | 0.13 | 0.894 | 0.894 | n.s. |
| Increase by 1 - Increase by 3 | 8.86 | 11.01 | 0.80 | 0.421 | 0.806 | n.s. |
| Increase by 2 - Increase by 3 | 7.41 | 11.01 | 0.67 | 0.501 | 0.806 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.23, *p* = 0.795, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.15 | 23 | = 0.884 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.56 | 23 | = 0.879 | 0.17 [-0.31, 0.54] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.55 | 23 | = 0.879 | 0.14 [-0.31, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.45, BIC = 316.11
- **Increase by 2 vs Increase by 1**: *β* = 1.37, *SE* = 0.317, *z* = 4.307, *p* < .001
- **Increase by 3 vs Increase by 1**: *β* = 1.46, *SE* = 0.323, *z* = 4.503, *p* < .001
- **SNR**: *β* = 0.02, *SE* = 0.036, *z* = 0.577, *p* = 0.564

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -1.37 | 0.32 | -4.31 | < .001 | < .001 | *** |
| Increase by 1 - Increase by 3 | -1.46 | 0.32 | -4.50 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | -0.09 | 0.32 | -0.28 | 0.782 | 0.782 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 12.48, *p* < .001, η²_G = 0.044
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -4.63 | 23 | < .001 | -0.41 [-1.45, -0.44] | small | *** |
| Increase by 1 vs Increase by 3 | -4.45 | 23 | < .001 | -0.47 [-1.41, -0.41] | small | *** |
| Increase by 2 vs Increase by 3 | -0.15 | 23 | = 0.882 | -0.02 [-0.45, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.45)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.41)
  - Increase by 1 showed smaller amplitude than Increase by 3 (*d* = -0.47)

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
