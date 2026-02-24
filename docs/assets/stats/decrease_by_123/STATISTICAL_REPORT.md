# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:16:11

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
| Decrease by 1 | 24 | 106.17 ms | 9.80 | 2.00 | [92.00, 120.00] |
| Decrease by 2 | 24 | 108.50 ms | 9.53 | 1.95 | [92.00, 120.00] |
| Decrease by 3 | 24 | 106.50 ms | 10.20 | 2.08 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | -1.03 µV | 1.51 | 0.31 | [-5.36, 1.11] |
| Decrease by 2 | 24 | -1.42 µV | 1.30 | 0.26 | [-4.58, 2.04] |
| Decrease by 3 | 24 | -1.77 µV | 1.82 | 0.37 | [-6.67, 1.47] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 178.17 ms | 15.47 | 3.16 | [148.00, 208.00] |
| Decrease by 2 | 24 | 177.67 ms | 14.44 | 2.95 | [148.00, 208.00] |
| Decrease by 3 | 24 | 177.67 ms | 14.59 | 2.98 | [156.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | -4.83 µV | 2.03 | 0.41 | [-9.17, -1.44] |
| Decrease by 2 | 24 | -4.93 µV | 2.02 | 0.41 | [-9.37, -1.43] |
| Decrease by 3 | 24 | -5.07 µV | 1.98 | 0.40 | [-8.57, -1.48] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 111.33 ms | 9.03 | 1.84 | [100.00, 124.00] |
| Decrease by 2 | 24 | 113.83 ms | 7.91 | 1.61 | [100.00, 124.00] |
| Decrease by 3 | 24 | 112.83 ms | 9.51 | 1.94 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 1.08 µV | 2.09 | 0.43 | [-1.60, 5.89] |
| Decrease by 2 | 24 | 1.65 µV | 1.83 | 0.37 | [-2.14, 5.51] |
| Decrease by 3 | 24 | 2.09 µV | 2.14 | 0.44 | [-1.71, 8.21] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 489.00 ms | 32.91 | 6.72 | [424.00, 528.00] |
| Decrease by 2 | 24 | 471.83 ms | 27.77 | 5.67 | [432.00, 536.00] |
| Decrease by 3 | 24 | 479.00 ms | 34.66 | 7.07 | [424.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 3.42 µV | 3.06 | 0.63 | [-2.76, 8.87] |
| Decrease by 2 | 24 | 3.58 µV | 2.94 | 0.60 | [-1.65, 8.53] |
| Decrease by 3 | 24 | 4.21 µV | 3.52 | 0.72 | [-1.32, 12.38] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 529.58, BIC = 543.24
- **Decrease by 2 vs Decrease by 1**: *β* = 2.31, *SE* = 2.126, *z* = 1.089, *p* = 0.276
- **Decrease by 3 vs Decrease by 1**: *β* = -0.40, *SE* = 2.154, *z* = -0.184, *p* = 0.854
- **SNR**: *β* = 1.03, *SE* = 0.495, *z* = 2.084, *p* = 0.037

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -2.32 | 2.13 | -1.09 | 0.276 | 0.503 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.40 | 2.15 | 0.18 | 0.854 | 0.854 | n.s. |
| Decrease by 2 - Decrease by 3 | 2.71 | 2.15 | 1.26 | 0.208 | 0.503 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.540, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -1.18 | 23 | = 0.636 | -0.24 [-0.67, 0.19] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.14 | 23 | = 0.886 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.81 | 23 | = 0.636 | 0.20 [-0.26, 0.59] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 252.29, BIC = 265.95
- **Decrease by 2 vs Decrease by 1**: *β* = -0.39, *SE* = 0.292, *z* = -1.330, *p* = 0.184
- **Decrease by 3 vs Decrease by 1**: *β* = -0.66, *SE* = 0.297, *z* = -2.216, *p* = 0.027
- **SNR**: *β* = -0.12, *SE* = 0.075, *z* = -1.657, *p* = 0.098

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.39 | 0.29 | 1.33 | 0.184 | 0.333 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.66 | 0.30 | 2.22 | 0.027 | 0.078 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.27 | 0.30 | 0.91 | 0.364 | 0.364 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.17, *p* = 0.051, η²_G = 0.038
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 1.44 | 23 | = 0.244 | 0.28 [-0.14, 0.73] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | 2.64 | 23 | = 0.044 | 0.45 [0.09, 0.99] | small | * |
| Decrease by 2 vs Decrease by 3 | 1.07 | 23 | = 0.296 | 0.22 [-0.21, 0.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 568.35, BIC = 582.01
- **Decrease by 2 vs Decrease by 1**: *β* = -0.50, *SE* = 2.392, *z* = -0.209, *p* = 0.834
- **Decrease by 3 vs Decrease by 1**: *β* = -0.51, *SE* = 2.393, *z* = -0.212, *p* = 0.832
- **SNR**: *β* = 0.03, *SE* = 0.261, *z* = 0.103, *p* = 0.918

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.50 | 2.39 | 0.21 | 0.834 | 0.995 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.51 | 2.39 | 0.21 | 0.832 | 0.995 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.01 | 2.39 | 0.00 | 0.997 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.03, *p* = 0.973, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.30 | 23 | = 1.000 | 0.03 [-0.36, 0.48] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.18 | 23 | = 1.000 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 249.08, BIC = 262.74
- **Decrease by 2 vs Decrease by 1**: *β* = -0.09, *SE* = 0.241, *z* = -0.392, *p* = 0.695
- **Decrease by 3 vs Decrease by 1**: *β* = -0.20, *SE* = 0.241, *z* = -0.815, *p* = 0.415
- **SNR**: *β* = -0.11, *SE* = 0.027, *z* = -4.229, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.09 | 0.24 | 0.39 | 0.695 | 0.892 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.20 | 0.24 | 0.82 | 0.415 | 0.800 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.10 | 0.24 | 0.42 | 0.672 | 0.892 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.706, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.35 | 23 | = 0.726 | 0.05 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.78 | 23 | = 0.726 | 0.12 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.52 | 23 | = 0.726 | 0.07 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 484.33, BIC = 497.99
- **Decrease by 2 vs Decrease by 1**: *β* = 2.52, *SE* = 1.279, *z* = 1.967, *p* = 0.049
- **Decrease by 3 vs Decrease by 1**: *β* = 1.51, *SE* = 1.278, *z* = 1.183, *p* = 0.237
- **SNR**: *β* = 0.04, *SE* = 0.234, *z* = 0.185, *p* = 0.853

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -2.52 | 1.28 | -1.97 | 0.049 | 0.140 | n.s. |
| Decrease by 1 - Decrease by 3 | -1.51 | 1.28 | -1.18 | 0.237 | 0.417 | n.s. |
| Decrease by 2 - Decrease by 3 | 1.00 | 1.28 | 0.79 | 0.432 | 0.432 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.86, *p* = 0.166, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -1.97 | 23 | = 0.183 | -0.29 [-0.84, 0.04] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.18 | 23 | = 0.374 | -0.16 [-0.67, 0.19] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.73 | 23 | = 0.472 | 0.11 [-0.28, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 257.46, BIC = 271.12
- **Decrease by 2 vs Decrease by 1**: *β* = 0.60, *SE* = 0.259, *z* = 2.311, *p* = 0.021
- **Decrease by 3 vs Decrease by 1**: *β* = 1.03, *SE* = 0.259, *z* = 3.983, *p* < .001
- **SNR**: *β* = 0.10, *SE* = 0.050, *z* = 1.971, *p* = 0.049

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.60 | 0.26 | -2.31 | 0.021 | 0.041 | * |
| Decrease by 1 - Decrease by 3 | -1.03 | 0.26 | -3.98 | < .001 | < .001 | *** |
| Decrease by 2 - Decrease by 3 | -0.43 | 0.26 | -1.67 | 0.094 | 0.094 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.25, *p* = 0.002, η²_G = 0.041
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -2.05 | 23 | = 0.079 | -0.29 [-0.86, 0.02] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -4.60 | 23 | < .001 | -0.47 [-1.44, -0.43] | small | *** |
| Decrease by 2 vs Decrease by 3 | -1.50 | 23 | = 0.146 | -0.22 [-0.74, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 696.49, BIC = 710.15
- **Decrease by 2 vs Decrease by 1**: *β* = -17.46, *SE* = 6.568, *z* = -2.659, *p* = 0.008
- **Decrease by 3 vs Decrease by 1**: *β* = -9.74, *SE* = 6.566, *z* = -1.484, *p* = 0.138
- **SNR**: *β* = -0.71, *SE* = 0.772, *z* = -0.921, *p* = 0.357

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 17.46 | 6.57 | 2.66 | 0.008 | 0.023 | * |
| Decrease by 1 - Decrease by 3 | 9.74 | 6.57 | 1.48 | 0.138 | 0.257 | n.s. |
| Decrease by 2 - Decrease by 3 | -7.72 | 6.59 | -1.17 | 0.241 | 0.257 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.31, *p* = 0.045, η²_G = 0.048
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 3.11 | 23 | = 0.015 | 0.56 [0.17, 1.10] | medium | * |
| Decrease by 1 vs Decrease by 3 | 1.38 | 23 | = 0.270 | 0.30 [-0.15, 0.71] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.99 | 23 | = 0.331 | -0.23 [-0.63, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.95, BIC = 311.61
- **Decrease by 2 vs Decrease by 1**: *β* = 0.20, *SE* = 0.308, *z* = 0.658, *p* = 0.511
- **Decrease by 3 vs Decrease by 1**: *β* = 0.75, *SE* = 0.308, *z* = 2.420, *p* = 0.016
- **SNR**: *β* = 0.11, *SE* = 0.046, *z* = 2.447, *p* = 0.014

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.20 | 0.31 | -0.66 | 0.511 | 0.511 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.75 | 0.31 | -2.42 | 0.016 | 0.046 | * |
| Decrease by 2 - Decrease by 3 | -0.54 | 0.31 | -1.75 | 0.080 | 0.153 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.33, *p* = 0.044, η²_G = 0.012
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.61 | 23 | = 0.549 | -0.05 [-0.55, 0.30] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.31 | 23 | = 0.091 | -0.24 [-0.92, -0.03] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.75 | 23 | = 0.141 | -0.19 [-0.79, 0.08] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.051)
**P1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Decrease by 1 showed smaller amplitude than Decrease by 3 (*d* = -0.47)
**P3b latency:** Significant main effect of condition (*p* = 0.045). Post-hoc tests revealed:
  - Decrease by 1 showed greater latency than Decrease by 2 (*d* = 0.56)
**P3b amplitude:** Significant main effect of condition (*p* = 0.044) (no significant pairwise comparisons)

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
