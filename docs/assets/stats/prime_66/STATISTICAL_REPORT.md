# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:32:20

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
| 6a | 24 | 102.17 ms | 15.24 | 3.11 | [84.00, 124.00] |
| 6b | 24 | 103.33 ms | 13.94 | 2.85 | [84.00, 124.00] |
| 6c | 24 | 105.67 ms | 14.44 | 2.95 | [84.00, 124.00] |
| 6d | 24 | 104.17 ms | 12.23 | 2.50 | [84.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 24 | -2.54 µV | 4.10 | 0.84 | [-10.55, 7.23] |
| 6b | 24 | -3.33 µV | 3.65 | 0.75 | [-8.93, 5.22] |
| 6c | 24 | -6.21 µV | 6.73 | 1.37 | [-30.56, 3.46] |
| 6d | 24 | -2.37 µV | 3.66 | 0.75 | [-7.66, 8.74] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 24 | 171.83 ms | 19.22 | 3.92 | [140.00, 208.00] |
| 6b | 24 | 172.50 ms | 18.77 | 3.83 | [140.00, 208.00] |
| 6c | 24 | 174.00 ms | 20.97 | 4.28 | [140.00, 204.00] |
| 6d | 24 | 172.83 ms | 19.20 | 3.92 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 24 | -5.94 µV | 3.22 | 0.66 | [-14.98, 1.07] |
| 6b | 24 | -6.45 µV | 3.79 | 0.77 | [-16.39, -1.58] |
| 6c | 24 | -5.98 µV | 6.91 | 1.41 | [-19.77, 12.17] |
| 6d | 24 | -6.15 µV | 3.69 | 0.75 | [-14.62, -0.53] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 24 | 92.00 ms | 24.09 | 4.92 | [56.00, 120.00] |
| 6b | 24 | 83.17 ms | 23.26 | 4.75 | [52.00, 120.00] |
| 6c | 24 | 89.17 ms | 23.28 | 4.75 | [52.00, 120.00] |
| 6d | 24 | 92.00 ms | 22.16 | 4.52 | [52.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 24 | 3.15 µV | 3.75 | 0.77 | [-3.49, 14.16] |
| 6b | 24 | 3.69 µV | 3.60 | 0.74 | [-5.78, 9.80] |
| 6c | 24 | 7.17 µV | 6.08 | 1.24 | [-2.78, 30.19] |
| 6d | 24 | 3.55 µV | 2.85 | 0.58 | [-1.50, 9.15] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 24 | 371.67 ms | 19.27 | 3.93 | [344.00, 396.00] |
| 6b | 24 | 374.17 ms | 18.46 | 3.77 | [344.00, 396.00] |
| 6c | 24 | 367.67 ms | 19.05 | 3.89 | [344.00, 396.00] |
| 6d | 24 | 373.00 ms | 19.57 | 3.99 | [344.00, 396.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 24 | 2.24 µV | 3.06 | 0.62 | [-3.72, 10.53] |
| 6b | 24 | 2.20 µV | 2.65 | 0.54 | [-2.97, 8.83] |
| 6c | 24 | 2.79 µV | 4.53 | 0.93 | [-3.99, 16.75] |
| 6d | 24 | 3.36 µV | 3.05 | 0.62 | [-4.20, 8.28] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 787.45, BIC = 805.40
- **6b vs 6a**: *β* = 1.70, *SE* = 3.799, *z* = 0.448, *p* = 0.654
- **6c vs 6a**: *β* = 4.17, *SE* = 3.816, *z* = 1.093, *p* = 0.274
- **6d vs 6a**: *β* = 2.77, *SE* = 3.831, *z* = 0.724, *p* = 0.469
- **SNR**: *β* = 1.20, *SE* = 1.065, *z* = 1.128, *p* = 0.259

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -1.70 | 3.80 | -0.45 | 0.654 | 0.959 | n.s. |
| 6a - 6c | -4.17 | 3.82 | -1.09 | 0.274 | 0.854 | n.s. |
| 6a - 6d | -2.77 | 3.83 | -0.72 | 0.469 | 0.958 | n.s. |
| 6b - 6c | -2.47 | 3.77 | -0.65 | 0.512 | 0.958 | n.s. |
| 6b - 6d | -1.07 | 3.78 | -0.28 | 0.776 | 0.959 | n.s. |
| 6c - 6d | 1.40 | 3.77 | 0.37 | 0.711 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.839, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | -0.30 | 23 | = 0.820 | -0.08 [-0.48, 0.36] | negligible | n.s. |
| 6a vs 6c | -0.81 | 23 | = 0.820 | -0.24 [-0.59, 0.26] | small | n.s. |
| 6a vs 6d | -0.56 | 23 | = 0.820 | -0.14 [-0.54, 0.31] | negligible | n.s. |
| 6b vs 6c | -0.54 | 23 | = 0.820 | -0.16 [-0.53, 0.31] | negligible | n.s. |
| 6b vs 6d | -0.23 | 23 | = 0.820 | -0.06 [-0.47, 0.38] | negligible | n.s. |
| 6c vs 6d | 0.40 | 23 | = 0.820 | 0.11 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 580.78, BIC = 598.73
- **6b vs 6a**: *β* = -1.10, *SE* = 1.346, *z* = -0.821, *p* = 0.412
- **6c vs 6a**: *β* = -4.07, *SE* = 1.351, *z* = -3.010, *p* = 0.003
- **6d vs 6a**: *β* = -0.29, *SE* = 1.356, *z* = -0.211, *p* = 0.833
- **SNR**: *β* = -0.71, *SE* = 0.346, *z* = -2.067, *p* = 0.039

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 1.10 | 1.35 | 0.82 | 0.412 | 0.796 | n.s. |
| 6a - 6c | 4.07 | 1.35 | 3.01 | 0.003 | 0.016 | * |
| 6a - 6d | 0.29 | 1.36 | 0.21 | 0.833 | 0.833 | n.s. |
| 6b - 6c | 2.96 | 1.34 | 2.21 | 0.027 | 0.103 | n.s. |
| 6b - 6d | -0.82 | 1.34 | -0.61 | 0.541 | 0.796 | n.s. |
| 6c - 6d | -3.78 | 1.34 | -2.83 | 0.005 | 0.023 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.52, *p* = 0.020, η²_G = 0.101
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | 0.61 | 23 | = 0.657 | 0.20 [-0.30, 0.55] | small | n.s. |
| 6a vs 6c | 2.48 | 23 | = 0.074 | 0.66 [0.06, 0.95] | medium | n.s. |
| 6a vs 6d | -0.17 | 23 | = 0.863 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| 6b vs 6c | 1.83 | 23 | = 0.160 | 0.53 [-0.06, 0.81] | medium | n.s. |
| 6b vs 6d | -0.99 | 23 | = 0.499 | -0.26 [-0.63, 0.22] | small | n.s. |
| 6c vs 6d | -2.40 | 23 | = 0.074 | -0.71 [-0.94, -0.04] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 841.35, BIC = 859.30
- **6b vs 6a**: *β* = 0.64, *SE* = 4.580, *z* = 0.139, *p* = 0.889
- **6c vs 6a**: *β* = 1.81, *SE* = 4.606, *z* = 0.393, *p* = 0.695
- **6d vs 6a**: *β* = 0.57, *SE* = 4.618, *z* = 0.123, *p* = 0.902
- **SNR**: *β* = -0.67, *SE* = 0.914, *z* = -0.736, *p* = 0.462

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -0.64 | 4.58 | -0.14 | 0.889 | 1.000 | n.s. |
| 6a - 6c | -1.81 | 4.61 | -0.39 | 0.695 | 0.999 | n.s. |
| 6a - 6d | -0.57 | 4.62 | -0.12 | 0.902 | 1.000 | n.s. |
| 6b - 6c | -1.17 | 4.60 | -0.25 | 0.799 | 1.000 | n.s. |
| 6b - 6d | 0.07 | 4.61 | 0.02 | 0.988 | 1.000 | n.s. |
| 6c - 6d | 1.24 | 4.58 | 0.27 | 0.786 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.08, *p* = 0.973, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | -0.14 | 23 | = 0.933 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| 6a vs 6c | -0.41 | 23 | = 0.933 | -0.11 [-0.51, 0.34] | negligible | n.s. |
| 6a vs 6d | -0.22 | 23 | = 0.933 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| 6b vs 6c | -0.33 | 23 | = 0.933 | -0.08 [-0.49, 0.35] | negligible | n.s. |
| 6b vs 6d | -0.08 | 23 | = 0.933 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 6c vs 6d | 0.24 | 23 | = 0.933 | 0.06 [-0.37, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 538.24, BIC = 556.19
- **6b vs 6a**: *β* = -0.55, *SE* = 0.910, *z* = -0.603, *p* = 0.547
- **6c vs 6a**: *β* = -0.49, *SE* = 0.916, *z* = -0.530, *p* = 0.596
- **6d vs 6a**: *β* = -0.75, *SE* = 0.918, *z* = -0.813, *p* = 0.416
- **SNR**: *β* = -0.84, *SE* = 0.185, *z* = -4.557, *p* < .001

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 0.55 | 0.91 | 0.60 | 0.547 | 0.981 | n.s. |
| 6a - 6c | 0.49 | 0.92 | 0.53 | 0.596 | 0.981 | n.s. |
| 6a - 6d | 0.75 | 0.92 | 0.81 | 0.416 | 0.960 | n.s. |
| 6b - 6c | -0.06 | 0.91 | -0.07 | 0.945 | 0.989 | n.s. |
| 6b - 6d | 0.20 | 0.92 | 0.22 | 0.829 | 0.989 | n.s. |
| 6c - 6d | 0.26 | 0.91 | 0.29 | 0.774 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.11, *p* = 0.957, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.888 (ε = 0.623)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | 0.62 | 23 | = 0.977 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| 6a vs 6c | 0.03 | 23 | = 0.977 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 6a vs 6d | 0.29 | 23 | = 0.977 | 0.06 [-0.36, 0.48] | negligible | n.s. |
| 6b vs 6c | -0.35 | 23 | = 0.977 | -0.09 [-0.49, 0.35] | negligible | n.s. |
| 6b vs 6d | -0.52 | 23 | = 0.977 | -0.08 [-0.53, 0.32] | negligible | n.s. |
| 6c vs 6d | 0.15 | 23 | = 0.977 | 0.03 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 878.73, BIC = 896.68
- **6b vs 6a**: *β* = -9.48, *SE* = 5.801, *z* = -1.635, *p* = 0.102
- **6c vs 6a**: *β* = -1.92, *SE* = 5.820, *z* = -0.330, *p* = 0.742
- **6d vs 6a**: *β* = 0.43, *SE* = 5.790, *z* = 0.075, *p* = 0.940
- **SNR**: *β* = 2.53, *SE* = 1.861, *z* = 1.360, *p* = 0.174

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 9.48 | 5.80 | 1.63 | 0.102 | 0.429 | n.s. |
| 6a - 6c | 1.92 | 5.82 | 0.33 | 0.742 | 0.969 | n.s. |
| 6a - 6d | -0.43 | 5.79 | -0.08 | 0.940 | 0.969 | n.s. |
| 6b - 6c | -7.56 | 5.89 | -1.28 | 0.199 | 0.589 | n.s. |
| 6b - 6d | -9.92 | 5.84 | -1.70 | 0.089 | 0.429 | n.s. |
| 6c - 6d | -2.35 | 5.79 | -0.41 | 0.684 | 0.969 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.405, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | 1.38 | 23 | = 0.601 | 0.37 [-0.15, 0.71] | small | n.s. |
| 6a vs 6c | 0.59 | 23 | = 0.782 | 0.12 [-0.30, 0.54] | negligible | n.s. |
| 6a vs 6d | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 6b vs 6c | -1.06 | 23 | = 0.601 | -0.26 [-0.64, 0.21] | small | n.s. |
| 6b vs 6d | -1.28 | 23 | = 0.601 | -0.39 [-0.69, 0.17] | small | n.s. |
| 6c vs 6d | -0.46 | 23 | = 0.782 | -0.12 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 558.83, BIC = 576.78
- **6b vs 6a**: *β* = 0.53, *SE* = 1.145, *z* = 0.466, *p* = 0.641
- **6c vs 6a**: *β* = 4.03, *SE* = 1.148, *z* = 3.510, *p* < .001
- **6d vs 6a**: *β* = 0.41, *SE* = 1.143, *z* = 0.362, *p* = 0.717
- **SNR**: *β* = 0.03, *SE* = 0.358, *z* = 0.077, *p* = 0.939

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -0.53 | 1.14 | -0.47 | 0.641 | 0.954 | n.s. |
| 6a - 6c | -4.03 | 1.15 | -3.51 | < .001 | 0.003 | ** |
| 6a - 6d | -0.41 | 1.14 | -0.36 | 0.717 | 0.954 | n.s. |
| 6b - 6c | -3.50 | 1.16 | -3.01 | 0.003 | 0.010 | * |
| 6b - 6d | 0.12 | 1.15 | 0.10 | 0.917 | 0.954 | n.s. |
| 6c - 6d | 3.62 | 1.14 | 3.16 | 0.002 | 0.008 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.13, *p* = 0.003, η²_G = 0.131
- Greenhouse-Geisser corrected: *p* = 0.009 (ε = 0.698)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | -0.51 | 23 | = 0.761 | -0.15 [-0.53, 0.32] | negligible | n.s. |
| 6a vs 6c | -3.15 | 23 | = 0.027 | -0.80 [-1.11, -0.18] | medium | * |
| 6a vs 6d | -0.48 | 23 | = 0.761 | -0.12 [-0.52, 0.32] | negligible | n.s. |
| 6b vs 6c | -2.53 | 23 | = 0.046 | -0.70 [-0.97, -0.07] | medium | * |
| 6b vs 6d | 0.17 | 23 | = 0.868 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| 6c vs 6d | 2.43 | 23 | = 0.046 | 0.76 [0.05, 0.94] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 848.20, BIC = 866.15
- **6b vs 6a**: *β* = 2.36, *SE* = 5.292, *z* = 0.446, *p* = 0.656
- **6c vs 6a**: *β* = -4.11, *SE* = 5.289, *z* = -0.777, *p* = 0.437
- **6d vs 6a**: *β* = 1.05, *SE* = 5.321, *z* = 0.198, *p* = 0.843
- **SNR**: *β* = 0.53, *SE* = 1.190, *z* = 0.441, *p* = 0.659

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -2.36 | 5.29 | -0.45 | 0.656 | 0.959 | n.s. |
| 6a - 6c | 4.11 | 5.29 | 0.78 | 0.437 | 0.900 | n.s. |
| 6a - 6d | -1.05 | 5.32 | -0.20 | 0.843 | 0.962 | n.s. |
| 6b - 6c | 6.47 | 5.28 | 1.22 | 0.221 | 0.776 | n.s. |
| 6b - 6d | 1.31 | 5.29 | 0.25 | 0.805 | 0.962 | n.s. |
| 6c - 6d | -5.16 | 5.30 | -0.97 | 0.330 | 0.865 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.650, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | -0.45 | 23 | = 0.800 | -0.13 [-0.51, 0.33] | negligible | n.s. |
| 6a vs 6c | 0.63 | 23 | = 0.800 | 0.21 [-0.30, 0.55] | small | n.s. |
| 6a vs 6d | -0.33 | 23 | = 0.800 | -0.07 [-0.49, 0.36] | negligible | n.s. |
| 6b vs 6c | 1.24 | 23 | = 0.800 | 0.35 [-0.18, 0.68] | small | n.s. |
| 6b vs 6d | 0.26 | 23 | = 0.800 | 0.06 [-0.37, 0.47] | negligible | n.s. |
| 6c vs 6d | -0.86 | 23 | = 0.800 | -0.28 [-0.60, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 501.93, BIC = 519.88
- **6b vs 6a**: *β* = -0.18, *SE* = 0.795, *z* = -0.223, *p* = 0.823
- **6c vs 6a**: *β* = 0.44, *SE* = 0.794, *z* = 0.557, *p* = 0.577
- **6d vs 6a**: *β* = 0.85, *SE* = 0.801, *z* = 1.060, *p* = 0.289
- **SNR**: *β* = 0.50, *SE* = 0.205, *z* = 2.439, *p* = 0.015

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 0.18 | 0.80 | 0.22 | 0.823 | 0.925 | n.s. |
| 6a - 6c | -0.44 | 0.79 | -0.56 | 0.577 | 0.925 | n.s. |
| 6a - 6d | -0.85 | 0.80 | -1.06 | 0.289 | 0.818 | n.s. |
| 6b - 6c | -0.62 | 0.79 | -0.78 | 0.434 | 0.898 | n.s. |
| 6b - 6d | -1.03 | 0.80 | -1.29 | 0.197 | 0.731 | n.s. |
| 6c - 6d | -0.41 | 0.80 | -0.51 | 0.610 | 0.925 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.87, *p* = 0.461, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | 0.06 | 23 | = 0.952 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 6a vs 6c | -0.58 | 23 | = 0.678 | -0.14 [-0.54, 0.30] | negligible | n.s. |
| 6a vs 6d | -1.36 | 23 | = 0.559 | -0.37 [-0.71, 0.15] | small | n.s. |
| 6b vs 6c | -0.73 | 23 | = 0.678 | -0.16 [-0.57, 0.28] | negligible | n.s. |
| 6b vs 6d | -1.52 | 23 | = 0.559 | -0.41 [-0.74, 0.12] | small | n.s. |
| 6c vs 6d | -0.63 | 23 | = 0.678 | -0.15 [-0.55, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.020) (no significant pairwise comparisons)
**P1 amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 6a showed smaller amplitude than 6c (*d* = -0.80)
  - 6b showed smaller amplitude than 6c (*d* = -0.70)
  - 6c showed greater amplitude than 6d (*d* = 0.76)

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
