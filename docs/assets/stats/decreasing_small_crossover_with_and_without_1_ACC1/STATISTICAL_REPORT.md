# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:39:12

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
| Crossover (with 1) | 17 | 108.00 ms | 8.83 | 2.14 | [96.00, 120.00] |
| Crossover (without 1) | 17 | 105.65 ms | 8.84 | 2.14 | [92.00, 120.00] |
| Small (with 1) | 15 | 110.13 ms | 10.68 | 2.76 | [92.00, 120.00] |
| Small (without 1) | 13 | 105.23 ms | 10.76 | 2.98 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 17 | -2.02 µV | 1.26 | 0.31 | [-5.75, -0.62] |
| Crossover (without 1) | 17 | -1.98 µV | 1.07 | 0.26 | [-5.22, -0.38] |
| Small (with 1) | 15 | -1.85 µV | 0.99 | 0.26 | [-4.34, -0.93] |
| Small (without 1) | 13 | -2.96 µV | 1.60 | 0.44 | [-5.62, -0.69] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 174.50 ms | 14.24 | 2.91 | [152.00, 208.00] |
| Crossover (without 1) | 24 | 172.83 ms | 14.92 | 3.05 | [148.00, 208.00] |
| Small (with 1) | 20 | 180.20 ms | 13.33 | 2.98 | [156.00, 212.00] |
| Small (without 1) | 23 | 176.35 ms | 24.95 | 5.20 | [144.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | -5.32 µV | 1.84 | 0.37 | [-8.96, -2.04] |
| Crossover (without 1) | 24 | -5.88 µV | 1.98 | 0.40 | [-9.79, -2.32] |
| Small (with 1) | 20 | -4.58 µV | 2.51 | 0.56 | [-9.67, -0.98] |
| Small (without 1) | 23 | -6.04 µV | 2.57 | 0.54 | [-10.33, -1.71] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 15 | 115.47 ms | 7.84 | 2.02 | [104.00, 124.00] |
| Crossover (without 1) | 14 | 114.86 ms | 8.80 | 2.35 | [100.00, 124.00] |
| Small (with 1) | 19 | 117.05 ms | 6.65 | 1.52 | [104.00, 124.00] |
| Small (without 1) | 8 | 113.00 ms | 8.75 | 3.09 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 15 | 2.56 µV | 1.46 | 0.38 | [1.10, 5.67] |
| Crossover (without 1) | 14 | 2.37 µV | 1.20 | 0.32 | [0.96, 4.70] |
| Small (with 1) | 19 | 2.64 µV | 1.72 | 0.40 | [0.60, 7.19] |
| Small (without 1) | 8 | 3.07 µV | 1.86 | 0.66 | [0.74, 6.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 21 | 481.90 ms | 26.49 | 5.78 | [436.00, 536.00] |
| Crossover (without 1) | 20 | 476.20 ms | 25.05 | 5.60 | [436.00, 536.00] |
| Small (with 1) | 20 | 484.00 ms | 22.52 | 5.03 | [432.00, 512.00] |
| Small (without 1) | 18 | 489.56 ms | 31.41 | 7.40 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 21 | 4.71 µV | 2.82 | 0.62 | [0.94, 10.69] |
| Crossover (without 1) | 20 | 4.88 µV | 2.77 | 0.62 | [0.59, 10.85] |
| Small (with 1) | 20 | 5.33 µV | 2.73 | 0.61 | [2.17, 12.20] |
| Small (without 1) | 18 | 6.70 µV | 4.08 | 0.96 | [1.91, 17.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 431.83, BIC = 446.72
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -2.31, *SE* = 1.733, *z* = -1.330, *p* = 0.183
- **Small (with 1) vs Crossover (with 1)**: *β* = 1.14, *SE* = 2.092, *z* = 0.546, *p* = 0.585
- **Small (without 1) vs Crossover (with 1)**: *β* = -2.24, *SE* = 2.062, *z* = -1.088, *p* = 0.277
- **SNR**: *β* = 0.10, *SE* = 0.619, *z* = 0.156, *p* = 0.876

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 2.30 | 1.73 | 1.33 | 0.183 | 0.555 | n.s. |
| Crossover (with 1) - Small (with 1) | -1.14 | 2.09 | -0.55 | 0.585 | 0.828 | n.s. |
| Crossover (with 1) - Small (without 1) | 2.24 | 2.06 | 1.09 | 0.277 | 0.622 | n.s. |
| Crossover (without 1) - Small (with 1) | -3.45 | 1.97 | -1.75 | 0.081 | 0.397 | n.s. |
| Crossover (without 1) - Small (without 1) | -0.06 | 1.98 | -0.03 | 0.975 | 0.975 | n.s. |
| Small (with 1) - Small (without 1) | 3.38 | 1.98 | 1.71 | 0.087 | 0.397 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.355, η²_G = 0.027
- Greenhouse-Geisser corrected: *p* = 0.338 (ε = 0.530)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 2.83 | 8 | = 0.133 | 0.32 [-0.02, 1.07] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.57 | 8 | = 0.703 | -0.17 [-0.76, 0.52] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.35 | 8 | = 0.738 | 0.09 [-0.37, 1.01] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.44 | 8 | = 0.438 | -0.42 [-1.21, 0.15] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.77 | 8 | = 0.698 | -0.18 [-0.59, 0.76] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 1.33 | 8 | = 0.438 | 0.23 [-0.40, 0.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 185.59, BIC = 200.48
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.12, *SE* = 0.281, *z* = -0.423, *p* = 0.673
- **Small (with 1) vs Crossover (with 1)**: *β* = -0.07, *SE* = 0.332, *z* = -0.211, *p* = 0.833
- **Small (without 1) vs Crossover (with 1)**: *β* = -1.10, *SE* = 0.333, *z* = -3.292, *p* = 0.001
- **SNR**: *β* = -0.32, *SE* = 0.090, *z* = -3.539, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.12 | 0.28 | 0.42 | 0.673 | 0.965 | n.s. |
| Crossover (with 1) - Small (with 1) | 0.07 | 0.33 | 0.21 | 0.833 | 0.972 | n.s. |
| Crossover (with 1) - Small (without 1) | 1.10 | 0.33 | 3.29 | < .001 | 0.006 | ** |
| Crossover (without 1) - Small (with 1) | -0.05 | 0.32 | -0.15 | 0.877 | 0.972 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.98 | 0.32 | 3.05 | 0.002 | 0.009 | ** |
| Small (with 1) - Small (without 1) | 1.03 | 0.32 | 3.24 | 0.001 | 0.006 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.327, η²_G = 0.065
- Greenhouse-Geisser corrected: *p* = 0.320 (ε = 0.544)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -0.88 | 8 | = 0.484 | -0.11 [-0.61, 0.42] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -1.25 | 8 | = 0.484 | -0.35 [-1.12, 0.22] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.68 | 8 | = 0.516 | 0.31 [-0.47, 0.88] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.90 | 8 | = 0.484 | -0.27 [-0.99, 0.32] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 1.01 | 8 | = 0.484 | 0.45 [-0.39, 0.99] | small | n.s. |
| Small (with 1) vs Small (without 1) | 1.53 | 8 | = 0.484 | 0.72 [-0.06, 1.44] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 771.18, BIC = 788.75
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -1.98, *SE* = 3.777, *z* = -0.524, *p* = 0.600
- **Small (with 1) vs Crossover (with 1)**: *β* = 4.41, *SE* = 4.601, *z* = 0.958, *p* = 0.338
- **Small (without 1) vs Crossover (with 1)**: *β* = 0.51, *SE* = 4.482, *z* = 0.114, *p* = 0.909
- **SNR**: *β* = -0.40, *SE* = 0.400, *z* = -0.999, *p* = 0.318

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 1.98 | 3.78 | 0.52 | 0.600 | 0.917 | n.s. |
| Crossover (with 1) - Small (with 1) | -4.41 | 4.60 | -0.96 | 0.338 | 0.870 | n.s. |
| Crossover (with 1) - Small (without 1) | -0.51 | 4.48 | -0.11 | 0.909 | 0.917 | n.s. |
| Crossover (without 1) - Small (with 1) | -6.39 | 4.45 | -1.43 | 0.152 | 0.627 | n.s. |
| Crossover (without 1) - Small (without 1) | -2.49 | 4.33 | -0.58 | 0.565 | 0.917 | n.s. |
| Small (with 1) - Small (without 1) | 3.89 | 4.04 | 0.96 | 0.335 | 0.870 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.33, *p* = 0.275, η²_G = 0.038
- Greenhouse-Geisser corrected: *p* = 0.268 (ε = 0.379)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 2.11 | 18 | = 0.098 | 0.11 [0.09, 0.99] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -3.21 | 18 | = 0.015 | -0.54 [-1.27, -0.21] | medium | * |
| Crossover (with 1) vs Small (without 1) | -0.14 | 18 | = 0.891 | -0.05 [-0.56, 0.31] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -3.70 | 18 | = 0.010 | -0.64 [-1.39, -0.30] | medium | ** |
| Crossover (without 1) vs Small (without 1) | -0.36 | 18 | = 0.864 | -0.12 [-0.62, 0.25] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 1.15 | 18 | = 0.399 | 0.32 [-0.23, 0.75] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 340.32, BIC = 357.90
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.70, *SE* = 0.312, *z* = -2.235, *p* = 0.025
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.01, *SE* = 0.394, *z* = 0.022, *p* = 0.982
- **Small (without 1) vs Crossover (with 1)**: *β* = -1.72, *SE* = 0.382, *z* = -4.509, *p* < .001
- **SNR**: *β* = -0.17, *SE* = 0.037, *z* = -4.747, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.70 | 0.31 | 2.23 | 0.025 | 0.074 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.01 | 0.39 | -0.02 | 0.982 | 0.982 | n.s. |
| Crossover (with 1) - Small (without 1) | 1.72 | 0.38 | 4.51 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.71 | 0.38 | -1.86 | 0.063 | 0.121 | n.s. |
| Crossover (without 1) - Small (without 1) | 1.03 | 0.37 | 2.80 | 0.005 | 0.020 | * |
| Small (with 1) - Small (without 1) | 1.73 | 0.34 | 5.17 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.85, *p* < .001, η²_G = 0.097
- Greenhouse-Geisser corrected: *p* = 0.002 (ε = 0.584)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 7.17 | 18 | < .001 | 0.31 [0.84, 2.04] | small | *** |
| Crossover (with 1) vs Small (with 1) | -2.73 | 18 | = 0.021 | -0.52 [-1.10, -0.09] | medium | * |
| Crossover (with 1) vs Small (without 1) | 1.32 | 18 | = 0.243 | 0.29 [-0.10, 0.79] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -3.74 | 18 | = 0.003 | -0.76 [-1.34, -0.26] | medium | ** |
| Crossover (without 1) vs Small (without 1) | 0.14 | 18 | = 0.894 | 0.03 [-0.39, 0.48] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 4.45 | 18 | < .001 | 0.69 [0.43, 1.62] | medium | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 381.72, BIC = 395.90
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.81, *SE* = 1.811, *z* = -0.449, *p* = 0.653
- **Small (with 1) vs Crossover (with 1)**: *β* = 3.64, *SE* = 1.791, *z* = 2.035, *p* = 0.042
- **Small (without 1) vs Crossover (with 1)**: *β* = 0.77, *SE* = 2.592, *z* = 0.295, *p* = 0.768
- **SNR**: *β* = 0.14, *SE* = 0.358, *z* = 0.387, *p* = 0.699

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.81 | 1.81 | 0.45 | 0.653 | 0.895 | n.s. |
| Crossover (with 1) - Small (with 1) | -3.64 | 1.79 | -2.03 | 0.042 | 0.193 | n.s. |
| Crossover (with 1) - Small (without 1) | -0.77 | 2.59 | -0.30 | 0.768 | 0.895 | n.s. |
| Crossover (without 1) - Small (with 1) | -4.46 | 1.81 | -2.47 | 0.014 | 0.079 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.58 | 2.50 | -0.63 | 0.528 | 0.895 | n.s. |
| Small (with 1) - Small (without 1) | 2.88 | 2.31 | 1.25 | 0.213 | 0.616 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.474, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.58 | 5 | = 0.591 | 0.16 [0.07, 1.37] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -1.17 | 5 | = 0.591 | -0.31 [-1.12, 0.11] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.28 | 5 | = 0.793 | -0.09 [-1.17, 0.94] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.39 | 5 | = 0.591 | -0.45 [-1.17, 0.12] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.81 | 5 | = 0.684 | -0.24 [-1.41, 0.75] | small | n.s. |
| Small (with 1) vs Small (without 1) | 0.60 | 5 | = 0.691 | 0.20 [-0.45, 1.29] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 169.71, BIC = 183.88
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.03, *SE* = 0.295, *z* = 0.093, *p* = 0.926
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.56, *SE* = 0.284, *z* = 1.989, *p* = 0.047
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.09, *SE* = 0.406, *z* = 2.680, *p* = 0.007
- **SNR**: *β* = 0.36, *SE* = 0.055, *z* = 6.475, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.03 | 0.29 | -0.09 | 0.926 | 0.926 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.57 | 0.28 | -1.99 | 0.047 | 0.174 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.09 | 0.41 | -2.68 | 0.007 | 0.040 | * |
| Crossover (without 1) - Small (with 1) | -0.54 | 0.29 | -1.87 | 0.061 | 0.174 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.06 | 0.39 | -2.70 | 0.007 | 0.040 | * |
| Small (with 1) - Small (without 1) | -0.52 | 0.37 | -1.40 | 0.160 | 0.295 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.54, *p* = 0.246, η²_G = 0.084
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.94 | 5 | = 0.467 | 0.36 [-0.07, 1.16] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.94 | 5 | = 0.467 | -0.32 [-0.93, 0.26] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.96 | 5 | = 0.467 | 0.35 [-0.70, 1.48] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.64 | 5 | = 0.467 | -0.68 [-1.19, 0.10] | medium | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.18 | 5 | = 0.861 | 0.05 [-0.98, 1.13] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 1.31 | 5 | = 0.467 | 0.62 [-0.63, 1.06] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 724.09, BIC = 740.67
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -5.21, *SE* = 5.364, *z* = -0.971, *p* = 0.332
- **Small (with 1) vs Crossover (with 1)**: *β* = 4.59, *SE* = 5.540, *z* = 0.829, *p* = 0.407
- **Small (without 1) vs Crossover (with 1)**: *β* = 9.56, *SE* = 6.259, *z* = 1.528, *p* = 0.127
- **SNR**: *β* = 0.35, *SE* = 0.416, *z* = 0.833, *p* = 0.405

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 5.21 | 5.36 | 0.97 | 0.332 | 0.701 | n.s. |
| Crossover (with 1) - Small (with 1) | -4.59 | 5.54 | -0.83 | 0.407 | 0.701 | n.s. |
| Crossover (with 1) - Small (without 1) | -9.56 | 6.26 | -1.53 | 0.127 | 0.418 | n.s. |
| Crossover (without 1) - Small (with 1) | -9.80 | 5.54 | -1.77 | 0.077 | 0.329 | n.s. |
| Crossover (without 1) - Small (without 1) | -14.77 | 6.12 | -2.42 | 0.016 | 0.091 | n.s. |
| Small (with 1) - Small (without 1) | -4.97 | 5.81 | -0.86 | 0.393 | 0.701 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.43, *p* = 0.246, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.39 | 16 | = 0.364 | 0.33 [-0.18, 0.78] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.26 | 16 | = 0.795 | -0.08 [-0.58, 0.36] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.66 | 16 | = 0.782 | -0.16 [-0.72, 0.29] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.71 | 16 | = 0.317 | -0.47 [-0.85, 0.14] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | -2.23 | 16 | = 0.244 | -0.46 [-1.13, -0.05] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.39 | 16 | = 0.795 | -0.10 [-0.61, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 323.32, BIC = 339.90
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.14, *SE* = 0.368, *z* = 0.393, *p* = 0.694
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.82, *SE* = 0.383, *z* = 2.154, *p* = 0.031
- **Small (without 1) vs Crossover (with 1)**: *β* = 2.41, *SE* = 0.442, *z* = 5.461, *p* < .001
- **SNR**: *β* = 0.11, *SE* = 0.031, *z* = 3.471, *p* = 0.001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.14 | 0.37 | -0.39 | 0.694 | 0.694 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.82 | 0.38 | -2.15 | 0.031 | 0.091 | n.s. |
| Crossover (with 1) - Small (without 1) | -2.41 | 0.44 | -5.46 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.68 | 0.38 | -1.78 | 0.075 | 0.144 | n.s. |
| Crossover (without 1) - Small (without 1) | -2.27 | 0.43 | -5.30 | < .001 | < .001 | *** |
| Small (with 1) - Small (without 1) | -1.59 | 0.40 | -3.94 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.51, *p* = 0.002, η²_G = 0.047
- Greenhouse-Geisser corrected: *p* = 0.010 (ε = 0.643)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.08 | 16 | = 0.938 | 0.00 [-0.43, 0.50] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.71 | 16 | = 0.583 | -0.11 [-0.75, 0.21] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -2.91 | 16 | = 0.031 | -0.47 [-1.25, -0.14] | small | * |
| Crossover (without 1) vs Small (with 1) | -0.75 | 16 | = 0.583 | -0.12 [-0.72, 0.25] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -3.03 | 16 | = 0.031 | -0.47 [-1.29, -0.17] | small | * |
| Small (with 1) vs Small (without 1) | -2.27 | 16 | = 0.075 | -0.38 [-1.10, 0.00] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Crossover (with 1) showed greater amplitude than Crossover (without 1) (*d* = 0.31)
  - Crossover (with 1) showed smaller amplitude than Small (with 1) (*d* = -0.52)
  - Crossover (without 1) showed smaller amplitude than Small (with 1) (*d* = -0.76)
  - Small (with 1) showed greater amplitude than Small (without 1) (*d* = 0.69)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Crossover (with 1) showed smaller amplitude than Small (without 1) (*d* = -0.47)
  - Crossover (without 1) showed smaller amplitude than Small (without 1) (*d* = -0.47)

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
