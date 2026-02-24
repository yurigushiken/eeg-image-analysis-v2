# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:18:50

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
| Decreasing Crossover | 24 | 108.67 ms | 9.26 | 1.89 | [96.00, 120.00] |
| Decreasing Large | 24 | 108.17 ms | 8.46 | 1.73 | [96.00, 120.00] |
| Decreasing Small | 24 | 110.33 ms | 9.93 | 2.03 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | -1.41 µV | 1.49 | 0.30 | [-5.75, 1.25] |
| Decreasing Large | 24 | -1.76 µV | 2.06 | 0.42 | [-7.59, 1.04] |
| Decreasing Small | 24 | -1.23 µV | 1.14 | 0.23 | [-4.34, 0.48] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 174.50 ms | 14.24 | 2.91 | [152.00, 208.00] |
| Decreasing Large | 24 | 177.50 ms | 18.46 | 3.77 | [148.00, 208.00] |
| Decreasing Small | 24 | 181.50 ms | 14.53 | 2.97 | [156.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | -5.32 µV | 1.84 | 0.37 | [-8.96, -2.04] |
| Decreasing Large | 24 | -5.74 µV | 2.36 | 0.48 | [-11.18, -2.00] |
| Decreasing Small | 24 | -4.11 µV | 2.52 | 0.51 | [-9.67, -0.98] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 112.50 ms | 9.39 | 1.92 | [100.00, 124.00] |
| Decreasing Large | 24 | 110.83 ms | 9.76 | 1.99 | [100.00, 124.00] |
| Decreasing Small | 24 | 116.33 ms | 7.99 | 1.63 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 1.52 µV | 1.88 | 0.38 | [-2.16, 5.67] |
| Decreasing Large | 24 | 1.50 µV | 2.57 | 0.52 | [-4.07, 6.60] |
| Decreasing Small | 24 | 2.15 µV | 1.84 | 0.37 | [-0.58, 7.19] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 479.00 ms | 27.34 | 5.58 | [436.00, 540.00] |
| Decreasing Large | 24 | 489.50 ms | 36.01 | 7.35 | [436.00, 540.00] |
| Decreasing Small | 24 | 482.33 ms | 26.13 | 5.33 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 4.05 µV | 3.22 | 0.66 | [-1.73, 10.69] |
| Decreasing Large | 24 | 3.75 µV | 3.43 | 0.70 | [-4.03, 9.67] |
| Decreasing Small | 24 | 4.56 µV | 3.11 | 0.63 | [-1.23, 12.20] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 506.36, BIC = 520.02
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.62, *SE* = 1.620, *z* = -0.386, *p* = 0.700
- **Decreasing Small vs Decreasing Crossover**: *β* = 1.36, *SE* = 1.685, *z* = 0.806, *p* = 0.420
- **SNR**: *β* = -0.25, *SE* = 0.420, *z* = -0.607, *p* = 0.544

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.63 | 1.62 | 0.39 | 0.700 | 0.700 | n.s. |
| Decreasing Crossover - Decreasing Small | -1.36 | 1.69 | -0.81 | 0.420 | 0.664 | n.s. |
| Decreasing Large - Decreasing Small | -1.98 | 1.63 | -1.21 | 0.225 | 0.534 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.94, *p* = 0.397, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.29 | 23 | = 0.777 | 0.06 [-0.36, 0.48] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.24 | 23 | = 0.374 | -0.17 [-0.68, 0.17] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.18 | 23 | = 0.374 | -0.23 [-0.67, 0.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 254.79, BIC = 268.45
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.52, *SE* = 0.325, *z* = -1.597, *p* = 0.110
- **Decreasing Small vs Decreasing Crossover**: *β* = -0.23, *SE* = 0.338, *z* = -0.696, *p* = 0.486
- **SNR**: *β* = -0.34, *SE* = 0.082, *z* = -4.085, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.52 | 0.33 | 1.60 | 0.110 | 0.295 | n.s. |
| Decreasing Crossover - Decreasing Small | 0.24 | 0.34 | 0.70 | 0.486 | 0.623 | n.s. |
| Decreasing Large - Decreasing Small | -0.28 | 0.33 | -0.87 | 0.386 | 0.623 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.329, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.89 | 23 | = 0.469 | 0.20 [-0.24, 0.61] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.74 | 23 | = 0.469 | -0.13 [-0.57, 0.27] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.30 | 23 | = 0.469 | -0.32 [-0.69, 0.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 574.58, BIC = 588.24
- **Decreasing Large vs Decreasing Crossover**: *β* = 3.20, *SE* = 2.722, *z* = 1.176, *p* = 0.240
- **Decreasing Small vs Decreasing Crossover**: *β* = 7.26, *SE* = 2.893, *z* = 2.510, *p* = 0.012
- **SNR**: *β* = 0.04, *SE* = 0.255, *z* = 0.171, *p* = 0.864

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -3.20 | 2.72 | -1.18 | 0.240 | 0.240 | n.s. |
| Decreasing Crossover - Decreasing Small | -7.26 | 2.89 | -2.51 | 0.012 | 0.036 | * |
| Decreasing Large - Decreasing Small | -4.06 | 2.48 | -1.64 | 0.102 | 0.193 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.91, *p* = 0.027, η²_G = 0.033
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.12 | 23 | = 0.275 | -0.18 [-0.66, 0.20] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -3.75 | 23 | = 0.003 | -0.49 [-1.24, -0.28] | small | ** |
| Decreasing Large vs Decreasing Small | -1.39 | 23 | = 0.265 | -0.24 [-0.72, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 296.12, BIC = 309.78
- **Decreasing Large vs Decreasing Crossover**: *β* = -1.00, *SE* = 0.429, *z* = -2.333, *p* = 0.020
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.45, *SE* = 0.454, *z* = 0.990, *p* = 0.322
- **SNR**: *β* = -0.13, *SE* = 0.039, *z* = -3.262, *p* = 0.001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 1.00 | 0.43 | 2.33 | 0.020 | 0.039 | * |
| Decreasing Crossover - Decreasing Small | -0.45 | 0.45 | -0.99 | 0.322 | 0.322 | n.s. |
| Decreasing Large - Decreasing Small | -1.45 | 0.39 | -3.69 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.25, *p* < .001, η²_G = 0.089
- Greenhouse-Geisser corrected: *p* = 0.003 (ε = 0.715)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.21 | 23 | = 0.239 | 0.20 [-0.18, 0.68] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -3.52 | 23 | = 0.006 | -0.55 [-1.19, -0.24] | medium | ** |
| Decreasing Large vs Decreasing Small | -3.06 | 23 | = 0.008 | -0.67 [-1.09, -0.16] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 509.44, BIC = 523.10
- **Decreasing Large vs Decreasing Crossover**: *β* = -1.75, *SE* = 1.732, *z* = -1.008, *p* = 0.313
- **Decreasing Small vs Decreasing Crossover**: *β* = 3.75, *SE* = 1.731, *z* = 2.169, *p* = 0.030
- **SNR**: *β* = -0.09, *SE* = 0.363, *z* = -0.238, *p* = 0.812

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 1.75 | 1.73 | 1.01 | 0.313 | 0.313 | n.s. |
| Decreasing Crossover - Decreasing Small | -3.75 | 1.73 | -2.17 | 0.030 | 0.059 | n.s. |
| Decreasing Large - Decreasing Small | -5.50 | 1.70 | -3.24 | 0.001 | 0.004 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.27, *p* = 0.009, η²_G = 0.063
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.11 | 23 | = 0.279 | 0.17 [-0.20, 0.65] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -2.60 | 23 | = 0.026 | -0.44 [-0.98, -0.08] | small | * |
| Decreasing Large vs Decreasing Small | -2.56 | 23 | = 0.026 | -0.62 [-0.97, -0.07] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 277.55, BIC = 291.21
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.10, *SE* = 0.324, *z* = 0.306, *p* = 0.760
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.75, *SE* = 0.324, *z* = 2.304, *p* = 0.021
- **SNR**: *β* = 0.12, *SE* = 0.078, *z* = 1.549, *p* = 0.121

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.10 | 0.32 | -0.31 | 0.760 | 0.760 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.75 | 0.32 | -2.30 | 0.021 | 0.062 | n.s. |
| Decreasing Large - Decreasing Small | -0.65 | 0.32 | -2.05 | 0.041 | 0.079 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.74, *p* = 0.075, η²_G = 0.021
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.04 | 23 | = 0.967 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -2.49 | 23 | = 0.062 | -0.34 [-0.96, -0.06] | small | n.s. |
| Decreasing Large vs Decreasing Small | -1.66 | 23 | = 0.165 | -0.29 [-0.77, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 688.47, BIC = 702.13
- **Decreasing Large vs Decreasing Crossover**: *β* = 9.23, *SE* = 6.721, *z* = 1.373, *p* = 0.170
- **Decreasing Small vs Decreasing Crossover**: *β* = 2.46, *SE* = 6.419, *z* = 0.383, *p* = 0.702
- **SNR**: *β* = -0.23, *SE* = 0.493, *z* = -0.465, *p* = 0.642

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -9.23 | 6.72 | -1.37 | 0.170 | 0.428 | n.s. |
| Decreasing Crossover - Decreasing Small | -2.46 | 6.42 | -0.38 | 0.702 | 0.702 | n.s. |
| Decreasing Large - Decreasing Small | 6.77 | 6.20 | 1.09 | 0.275 | 0.474 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.45, *p* = 0.244, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.83 | 23 | = 0.241 | -0.33 [-0.81, 0.06] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.58 | 23 | = 0.566 | -0.12 [-0.54, 0.30] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | 0.98 | 23 | = 0.503 | 0.23 [-0.23, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 331.64, BIC = 345.30
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.35, *SE* = 0.493, *z* = 0.715, *p* = 0.475
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.96, *SE* = 0.467, *z* = 2.047, *p* = 0.041
- **SNR**: *β* = 0.12, *SE* = 0.039, *z* = 3.063, *p* = 0.002

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.35 | 0.49 | -0.71 | 0.475 | 0.475 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.96 | 0.47 | -2.05 | 0.041 | 0.117 | n.s. |
| Decreasing Large - Decreasing Small | -0.60 | 0.45 | -1.35 | 0.178 | 0.324 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.45, *p* = 0.245, η²_G = 0.011
- Greenhouse-Geisser corrected: *p* = 0.246 (ε = 0.724)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.60 | 23 | = 0.552 | 0.09 [-0.30, 0.55] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.62 | 23 | = 0.268 | -0.16 [-0.76, 0.10] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.39 | 23 | = 0.268 | -0.25 [-0.71, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.027). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller latency than Decreasing Small (*d* = -0.49)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller amplitude than Decreasing Small (*d* = -0.55)
  - Decreasing Large showed smaller amplitude than Decreasing Small (*d* = -0.67)
**P1 latency:** Significant main effect of condition (*p* = 0.009). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller latency than Decreasing Small (*d* = -0.44)
  - Decreasing Large showed smaller latency than Decreasing Small (*d* = -0.62)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.075)

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
