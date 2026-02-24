# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:19:31

---

## 1. Analysis Overview

**Total Measurements:** 384
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| Crossover (with 1) | 24 | 108.33 ms | 9.79 | 2.00 | [92.00, 120.00] |
| Crossover (without 1) | 24 | 107.00 ms | 9.45 | 1.93 | [92.00, 120.00] |
| Small (with 1) | 24 | 109.67 ms | 11.00 | 2.24 | [92.00, 120.00] |
| Small (without 1) | 24 | 105.83 ms | 11.79 | 2.41 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | -1.41 µV | 1.49 | 0.30 | [-5.75, 1.25] |
| Crossover (without 1) | 24 | -1.37 µV | 1.39 | 0.28 | [-5.22, 1.43] |
| Small (with 1) | 24 | -1.27 µV | 1.12 | 0.23 | [-4.34, 0.48] |
| Small (without 1) | 24 | -1.48 µV | 2.14 | 0.44 | [-5.62, 2.81] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 174.50 ms | 14.24 | 2.91 | [152.00, 208.00] |
| Crossover (without 1) | 24 | 172.83 ms | 14.92 | 3.05 | [148.00, 208.00] |
| Small (with 1) | 24 | 181.67 ms | 14.87 | 3.04 | [156.00, 212.00] |
| Small (without 1) | 24 | 177.83 ms | 25.46 | 5.20 | [144.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | -5.32 µV | 1.84 | 0.37 | [-8.96, -2.04] |
| Crossover (without 1) | 24 | -5.88 µV | 1.98 | 0.40 | [-9.79, -2.32] |
| Small (with 1) | 24 | -4.12 µV | 2.52 | 0.51 | [-9.67, -0.98] |
| Small (without 1) | 24 | -5.95 µV | 2.55 | 0.52 | [-10.33, -1.71] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 112.50 ms | 9.39 | 1.92 | [100.00, 124.00] |
| Crossover (without 1) | 24 | 111.50 ms | 9.82 | 2.00 | [100.00, 124.00] |
| Small (with 1) | 24 | 116.33 ms | 7.99 | 1.63 | [100.00, 124.00] |
| Small (without 1) | 24 | 113.17 ms | 9.69 | 1.98 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 1.52 µV | 1.88 | 0.38 | [-2.16, 5.67] |
| Crossover (without 1) | 24 | 1.26 µV | 1.75 | 0.36 | [-2.63, 4.70] |
| Small (with 1) | 24 | 2.15 µV | 1.84 | 0.37 | [-0.58, 7.19] |
| Small (without 1) | 24 | 0.67 µV | 2.26 | 0.46 | [-2.71, 6.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 478.83 ms | 26.96 | 5.50 | [436.00, 536.00] |
| Crossover (without 1) | 24 | 473.67 ms | 24.74 | 5.05 | [436.00, 536.00] |
| Small (with 1) | 24 | 482.00 ms | 26.08 | 5.32 | [432.00, 536.00] |
| Small (without 1) | 24 | 488.17 ms | 33.85 | 6.91 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 4.04 µV | 3.23 | 0.66 | [-1.73, 10.69] |
| Crossover (without 1) | 24 | 4.00 µV | 3.28 | 0.67 | [-1.77, 10.85] |
| Small (with 1) | 24 | 4.55 µV | 3.12 | 0.64 | [-1.23, 12.20] |
| Small (without 1) | 24 | 5.29 µV | 4.42 | 0.90 | [-1.20, 17.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 691.61, BIC = 709.56
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -1.58, *SE* = 1.867, *z* = -0.846, *p* = 0.397
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.62, *SE* = 1.980, *z* = 0.313, *p* = 0.754
- **Small (without 1) vs Crossover (with 1)**: *β* = -3.15, *SE* = 1.959, *z* = -1.608, *p* = 0.108
- **SNR**: *β* = -0.56, *SE* = 0.550, *z* = -1.013, *p* = 0.311

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 1.58 | 1.87 | 0.85 | 0.397 | 0.781 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.62 | 1.98 | -0.31 | 0.754 | 0.781 | n.s. |
| Crossover (with 1) - Small (without 1) | 3.15 | 1.96 | 1.61 | 0.108 | 0.435 | n.s. |
| Crossover (without 1) - Small (with 1) | -2.20 | 1.91 | -1.15 | 0.249 | 0.681 | n.s. |
| Crossover (without 1) - Small (without 1) | 1.57 | 1.89 | 0.83 | 0.407 | 0.781 | n.s. |
| Small (with 1) - Small (without 1) | 3.77 | 1.85 | 2.04 | 0.042 | 0.226 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.222, η²_G = 0.019
- Greenhouse-Geisser corrected: *p* = 0.234 (ε = 0.627)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.56 | 23 | = 0.267 | 0.14 [-0.12, 0.75] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.86 | 23 | = 0.480 | -0.13 [-0.60, 0.25] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 1.05 | 23 | = 0.457 | 0.23 [-0.21, 0.64] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.62 | 23 | = 0.267 | -0.26 [-0.76, 0.10] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.48 | 23 | = 0.635 | 0.11 [-0.33, 0.52] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 1.80 | 23 | = 0.267 | 0.34 [-0.07, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 341.74, BIC = 359.69
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.02, *SE* = 0.319, *z* = 0.052, *p* = 0.958
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.07, *SE* = 0.337, *z* = 0.217, *p* = 0.828
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.13, *SE* = 0.334, *z* = -0.401, *p* = 0.688
- **SNR**: *β* = -0.06, *SE* = 0.092, *z* = -0.609, *p* = 0.542

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.02 | 0.32 | -0.05 | 0.958 | 0.995 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.07 | 0.34 | -0.22 | 0.828 | 0.995 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.13 | 0.33 | 0.40 | 0.688 | 0.994 | n.s. |
| Crossover (without 1) - Small (with 1) | -0.06 | 0.33 | -0.17 | 0.862 | 0.995 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.15 | 0.32 | 0.47 | 0.641 | 0.994 | n.s. |
| Small (with 1) - Small (without 1) | 0.21 | 0.32 | 0.66 | 0.512 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.927, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.797 (ε = 0.501)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -0.52 | 23 | = 0.875 | -0.03 [-0.53, 0.32] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.64 | 23 | = 0.875 | -0.11 [-0.55, 0.29] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.16 | 23 | = 0.875 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.43 | 23 | = 0.875 | -0.08 [-0.51, 0.33] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.25 | 23 | = 0.875 | 0.06 [-0.37, 0.47] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 0.58 | 23 | = 0.875 | 0.12 [-0.30, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 811.66, BIC = 829.61
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -1.96, *SE* = 3.725, *z* = -0.526, *p* = 0.599
- **Small (with 1) vs Crossover (with 1)**: *β* = 5.04, *SE* = 4.361, *z* = 1.155, *p* = 0.248
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.17, *SE* = 4.380, *z* = 0.267, *p* = 0.790
- **SNR**: *β* = -0.37, *SE* = 0.401, *z* = -0.931, *p* = 0.352

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 1.96 | 3.72 | 0.53 | 0.599 | 0.842 | n.s. |
| Crossover (with 1) - Small (with 1) | -5.04 | 4.36 | -1.15 | 0.248 | 0.760 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.17 | 4.38 | -0.27 | 0.790 | 0.842 | n.s. |
| Crossover (without 1) - Small (with 1) | -6.99 | 4.20 | -1.66 | 0.096 | 0.455 | n.s. |
| Crossover (without 1) - Small (without 1) | -3.13 | 4.22 | -0.74 | 0.459 | 0.842 | n.s. |
| Small (with 1) - Small (without 1) | 3.87 | 3.71 | 1.04 | 0.297 | 0.760 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.14, *p* = 0.103, η²_G = 0.036
- Greenhouse-Geisser corrected: *p* = 0.152 (ε = 0.404)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 2.63 | 23 | = 0.030 | 0.11 [0.09, 0.99] | negligible | * |
| Crossover (with 1) vs Small (with 1) | -3.88 | 23 | = 0.002 | -0.49 [-1.27, -0.31] | small | ** |
| Crossover (with 1) vs Small (without 1) | -0.64 | 23 | = 0.530 | -0.16 [-0.55, 0.29] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -4.32 | 23 | = 0.002 | -0.59 [-1.38, -0.38] | medium | ** |
| Crossover (without 1) vs Small (without 1) | -0.92 | 23 | = 0.489 | -0.24 [-0.61, 0.24] | small | n.s. |
| Small (with 1) vs Small (without 1) | 0.84 | 23 | = 0.489 | 0.18 [-0.25, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 357.15, BIC = 375.10
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.69, *SE* = 0.313, *z* = -2.224, *p* = 0.026
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.22, *SE* = 0.376, *z* = 0.581, *p* = 0.561
- **Small (without 1) vs Crossover (with 1)**: *β* = -1.63, *SE* = 0.378, *z* = -4.301, *p* < .001
- **SNR**: *β* = -0.17, *SE* = 0.037, *z* = -4.655, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.70 | 0.31 | 2.22 | 0.026 | 0.052 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.22 | 0.38 | -0.58 | 0.561 | 0.561 | n.s. |
| Crossover (with 1) - Small (without 1) | 1.63 | 0.38 | 4.30 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.91 | 0.36 | -2.53 | 0.011 | 0.040 | * |
| Crossover (without 1) - Small (without 1) | 0.93 | 0.36 | 2.57 | 0.010 | 0.040 | * |
| Small (with 1) - Small (without 1) | 1.84 | 0.31 | 5.93 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 11.61, *p* < .001, η²_G = 0.100
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.620)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 7.05 | 23 | < .001 | 0.29 [0.84, 2.04] | small | *** |
| Crossover (with 1) vs Small (with 1) | -3.47 | 23 | = 0.003 | -0.54 [-1.18, -0.24] | medium | ** |
| Crossover (with 1) vs Small (without 1) | 1.56 | 23 | = 0.159 | 0.28 [-0.11, 0.75] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -4.53 | 23 | < .001 | -0.78 [-1.43, -0.42] | medium | *** |
| Crossover (without 1) vs Small (without 1) | 0.16 | 23 | = 0.874 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 5.10 | 23 | < .001 | 0.72 [0.52, 1.57] | medium | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 647.03, BIC = 664.98
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -1.08, *SE* = 1.405, *z* = -0.770, *p* = 0.441
- **Small (with 1) vs Crossover (with 1)**: *β* = 3.65, *SE* = 1.424, *z* = 2.564, *p* = 0.010
- **Small (without 1) vs Crossover (with 1)**: *β* = 0.25, *SE* = 1.523, *z* = 0.163, *p* = 0.870
- **SNR**: *β* = -0.20, *SE* = 0.286, *z* = -0.698, *p* = 0.485

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 1.08 | 1.41 | 0.77 | 0.441 | 0.749 | n.s. |
| Crossover (with 1) - Small (with 1) | -3.65 | 1.42 | -2.56 | 0.010 | 0.051 | n.s. |
| Crossover (with 1) - Small (without 1) | -0.25 | 1.52 | -0.16 | 0.870 | 0.870 | n.s. |
| Crossover (without 1) - Small (with 1) | -4.73 | 1.41 | -3.36 | < .001 | 0.005 | ** |
| Crossover (without 1) - Small (without 1) | -1.33 | 1.48 | -0.90 | 0.369 | 0.749 | n.s. |
| Small (with 1) - Small (without 1) | 3.40 | 1.44 | 2.36 | 0.018 | 0.071 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.23, *p* = 0.008, η²_G = 0.038
- Greenhouse-Geisser corrected: *p* = 0.020 (ε = 0.669)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.45 | 23 | = 0.243 | 0.10 [-0.14, 0.73] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -2.60 | 23 | = 0.048 | -0.44 [-0.98, -0.08] | small | * |
| Crossover (with 1) vs Small (without 1) | -0.46 | 23 | = 0.647 | -0.07 [-0.52, 0.33] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -2.61 | 23 | = 0.048 | -0.54 [-0.98, -0.08] | medium | * |
| Crossover (without 1) vs Small (without 1) | -1.19 | 23 | = 0.296 | -0.17 [-0.67, 0.19] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 2.11 | 23 | = 0.093 | 0.36 [-0.01, 0.87] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 356.51, BIC = 374.46
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.22, *SE* = 0.324, *z* = -0.669, *p* = 0.504
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.73, *SE* = 0.329, *z* = 2.220, *p* = 0.026
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.63, *SE* = 0.353, *z* = -1.786, *p* = 0.074
- **SNR**: *β* = 0.10, *SE* = 0.068, *z* = 1.511, *p* = 0.131

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.22 | 0.32 | 0.67 | 0.504 | 0.504 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.73 | 0.33 | -2.22 | 0.026 | 0.102 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.63 | 0.35 | 1.79 | 0.074 | 0.206 | n.s. |
| Crossover (without 1) - Small (with 1) | -0.95 | 0.32 | -2.92 | 0.004 | 0.018 | * |
| Crossover (without 1) - Small (without 1) | 0.41 | 0.34 | 1.21 | 0.227 | 0.403 | n.s. |
| Small (with 1) - Small (without 1) | 1.36 | 0.33 | 4.09 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.01, *p* < .001, η²_G = 0.073
- Greenhouse-Geisser corrected: *p* = 0.003 (ε = 0.599)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 2.62 | 23 | = 0.031 | 0.14 [0.08, 0.99] | negligible | * |
| Crossover (with 1) vs Small (with 1) | -2.49 | 23 | = 0.031 | -0.34 [-0.96, -0.06] | small | * |
| Crossover (with 1) vs Small (without 1) | 2.06 | 23 | = 0.061 | 0.41 [-0.02, 0.86] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -3.07 | 23 | = 0.016 | -0.50 [-1.09, -0.17] | medium | * |
| Crossover (without 1) vs Small (without 1) | 1.43 | 23 | = 0.166 | 0.29 [-0.14, 0.72] | small | n.s. |
| Small (with 1) vs Small (without 1) | 3.82 | 23 | = 0.005 | 0.72 [0.30, 1.26] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 891.74, BIC = 909.69
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -4.91, *SE* = 5.485, *z* = -0.895, *p* = 0.371
- **Small (with 1) vs Crossover (with 1)**: *β* = 3.92, *SE* = 5.685, *z* = 0.689, *p* = 0.491
- **Small (without 1) vs Crossover (with 1)**: *β* = 10.68, *SE* = 6.154, *z* = 1.735, *p* = 0.083
- **SNR**: *β* = 0.20, *SE* = 0.419, *z* = 0.473, *p* = 0.636

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 4.91 | 5.48 | 0.90 | 0.371 | 0.604 | n.s. |
| Crossover (with 1) - Small (with 1) | -3.92 | 5.69 | -0.69 | 0.491 | 0.604 | n.s. |
| Crossover (with 1) - Small (without 1) | -10.68 | 6.15 | -1.73 | 0.083 | 0.351 | n.s. |
| Crossover (without 1) - Small (with 1) | -8.83 | 5.56 | -1.59 | 0.112 | 0.379 | n.s. |
| Crossover (without 1) - Small (without 1) | -15.59 | 5.92 | -2.63 | 0.009 | 0.050 | * |
| Small (with 1) - Small (without 1) | -6.76 | 5.60 | -1.21 | 0.227 | 0.539 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.36, *p* = 0.079, η²_G = 0.035
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.29 | 23 | = 0.315 | 0.20 [-0.17, 0.69] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.56 | 23 | = 0.578 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -1.42 | 23 | = 0.315 | -0.31 [-0.72, 0.14] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.74 | 23 | = 0.284 | -0.33 [-0.79, 0.08] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | -2.49 | 23 | = 0.122 | -0.49 [-0.96, -0.06] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.97 | 23 | = 0.408 | -0.20 [-0.63, 0.23] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 407.60, BIC = 425.55
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.04, *SE* = 0.366, *z* = 0.106, *p* = 0.915
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.76, *SE* = 0.382, *z* = 1.980, *p* = 0.048
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.70, *SE* = 0.421, *z* = 4.040, *p* < .001
- **SNR**: *β* = 0.07, *SE* = 0.031, *z* = 2.127, *p* = 0.033

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.04 | 0.37 | -0.11 | 0.915 | 0.915 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.76 | 0.38 | -1.98 | 0.048 | 0.136 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.70 | 0.42 | -4.04 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.72 | 0.37 | -1.93 | 0.053 | 0.136 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.66 | 0.40 | -4.13 | < .001 | < .001 | *** |
| Small (with 1) - Small (without 1) | -0.94 | 0.38 | -2.51 | 0.012 | 0.047 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.12, *p* = 0.003, η²_G = 0.022
- Greenhouse-Geisser corrected: *p* = 0.013 (ε = 0.591)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.56 | 23 | = 0.584 | 0.01 [-0.31, 0.54] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -1.62 | 23 | = 0.177 | -0.16 [-0.77, 0.10] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -2.75 | 23 | = 0.034 | -0.32 [-1.02, -0.11] | small | * |
| Crossover (without 1) vs Small (with 1) | -1.75 | 23 | = 0.177 | -0.17 [-0.79, 0.08] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -3.01 | 23 | = 0.034 | -0.33 [-1.08, -0.15] | small | * |
| Small (with 1) vs Small (without 1) | -1.47 | 23 | = 0.187 | -0.19 [-0.73, 0.13] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Crossover (with 1) showed greater amplitude than Crossover (without 1) (*d* = 0.29)
  - Crossover (with 1) showed smaller amplitude than Small (with 1) (*d* = -0.54)
  - Crossover (without 1) showed smaller amplitude than Small (with 1) (*d* = -0.78)
  - Small (with 1) showed greater amplitude than Small (without 1) (*d* = 0.72)
**P1 latency:** Significant main effect of condition (*p* = 0.008). Post-hoc tests revealed:
  - Crossover (with 1) showed smaller latency than Small (with 1) (*d* = -0.44)
  - Crossover (without 1) showed smaller latency than Small (with 1) (*d* = -0.54)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Crossover (with 1) showed greater amplitude than Crossover (without 1) (*d* = 0.14)
  - Crossover (with 1) showed smaller amplitude than Small (with 1) (*d* = -0.34)
  - Crossover (without 1) showed smaller amplitude than Small (with 1) (*d* = -0.50)
  - Small (with 1) showed greater amplitude than Small (without 1) (*d* = 0.72)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.079)
**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - Crossover (with 1) showed smaller amplitude than Small (without 1) (*d* = -0.32)
  - Crossover (without 1) showed smaller amplitude than Small (without 1) (*d* = -0.33)

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
