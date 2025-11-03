# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:52:48

---

## 1. Analysis Overview

**Total Measurements:** 480
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| a | 15 | 105.33 ms | 9.15 | 2.36 | [92.00, 116.00] |
| b | 19 | 106.53 ms | 8.56 | 1.96 | [92.00, 116.00] |
| c | 17 | 103.76 ms | 8.66 | 2.10 | [92.00, 116.00] |
| d | 14 | 108.57 ms | 5.84 | 1.56 | [96.00, 116.00] |
| e | 14 | 103.43 ms | 8.13 | 2.17 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 15 | -2.02 µV | 1.54 | 0.40 | [-6.81, -0.77] |
| b | 19 | -1.69 µV | 0.95 | 0.22 | [-3.89, -0.35] |
| c | 17 | -2.08 µV | 1.22 | 0.30 | [-4.89, -0.38] |
| d | 14 | -1.47 µV | 0.97 | 0.26 | [-3.86, -0.48] |
| e | 14 | -2.04 µV | 1.11 | 0.30 | [-4.10, -0.73] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 175.33 ms | 16.67 | 3.40 | [144.00, 208.00] |
| b | 23 | 174.09 ms | 16.88 | 3.52 | [148.00, 208.00] |
| c | 23 | 175.13 ms | 16.93 | 3.53 | [144.00, 208.00] |
| d | 24 | 172.50 ms | 18.21 | 3.72 | [144.00, 208.00] |
| e | 24 | 175.50 ms | 16.69 | 3.41 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | -5.21 µV | 2.07 | 0.42 | [-9.32, -1.56] |
| b | 23 | -5.45 µV | 2.39 | 0.50 | [-11.91, -2.05] |
| c | 23 | -5.01 µV | 1.90 | 0.40 | [-8.73, -1.93] |
| d | 24 | -5.12 µV | 1.78 | 0.36 | [-9.19, -2.51] |
| e | 24 | -5.53 µV | 2.26 | 0.46 | [-11.22, -2.04] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 14 | 108.86 ms | 8.76 | 2.34 | [92.00, 116.00] |
| b | 14 | 108.57 ms | 7.66 | 2.05 | [96.00, 116.00] |
| c | 17 | 105.18 ms | 7.32 | 1.77 | [96.00, 116.00] |
| d | 11 | 108.00 ms | 8.00 | 2.41 | [96.00, 116.00] |
| e | 15 | 105.60 ms | 8.79 | 2.27 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 14 | 2.51 µV | 1.64 | 0.44 | [0.34, 5.69] |
| b | 14 | 2.28 µV | 1.56 | 0.42 | [0.35, 5.47] |
| c | 17 | 2.44 µV | 1.72 | 0.42 | [0.21, 7.09] |
| d | 11 | 1.96 µV | 1.28 | 0.39 | [0.52, 4.40] |
| e | 15 | 2.13 µV | 1.38 | 0.36 | [0.48, 5.26] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 19 | 478.95 ms | 32.85 | 7.54 | [428.00, 536.00] |
| b | 17 | 480.71 ms | 33.20 | 8.05 | [428.00, 536.00] |
| c | 22 | 475.45 ms | 27.80 | 5.93 | [436.00, 536.00] |
| d | 19 | 493.68 ms | 28.04 | 6.43 | [436.00, 536.00] |
| e | 18 | 480.89 ms | 33.62 | 7.92 | [436.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 19 | 4.48 µV | 2.39 | 0.55 | [0.95, 8.24] |
| b | 17 | 5.80 µV | 2.87 | 0.70 | [1.39, 12.30] |
| c | 22 | 4.13 µV | 2.23 | 0.47 | [1.29, 8.06] |
| d | 19 | 4.54 µV | 2.54 | 0.58 | [0.82, 10.23] |
| e | 18 | 5.44 µV | 2.59 | 0.61 | [2.03, 11.35] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 549.87, BIC = 568.83
- **b vs a**: *β* = 2.02, *SE* = 2.118, *z* = 0.955, *p* = 0.339
- **c vs a**: *β* = -1.23, *SE* = 2.193, *z* = -0.559, *p* = 0.576
- **d vs a**: *β* = 3.10, *SE* = 2.248, *z* = 1.378, *p* = 0.168
- **e vs a**: *β* = -0.50, *SE* = 2.250, *z* = -0.223, *p* = 0.824
- **SNR**: *β* = 0.29, *SE* = 0.352, *z* = 0.838, *p* = 0.402

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -2.02 | 2.12 | -0.96 | 0.339 | 0.874 | n.s. |
| a - c | 1.23 | 2.19 | 0.56 | 0.576 | 0.968 | n.s. |
| a - d | -3.10 | 2.25 | -1.38 | 0.168 | 0.724 | n.s. |
| a - e | 0.50 | 2.25 | 0.22 | 0.824 | 0.968 | n.s. |
| b - c | 3.25 | 2.01 | 1.61 | 0.107 | 0.637 | n.s. |
| b - d | -1.07 | 2.22 | -0.48 | 0.628 | 0.968 | n.s. |
| b - e | 2.52 | 2.12 | 1.19 | 0.235 | 0.799 | n.s. |
| c - d | -4.32 | 2.31 | -1.87 | 0.062 | 0.471 | n.s. |
| c - e | -0.72 | 2.21 | -0.33 | 0.743 | 0.968 | n.s. |
| d - e | 3.60 | 2.33 | 1.55 | 0.122 | 0.646 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.40, *p* = 0.804, η²_G = 0.041
- Greenhouse-Geisser corrected: *p* = 0.650 (ε = 0.429)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.87 | 5 | = 0.981 | -0.51 [-1.12, 0.21] | medium | n.s. |
| a vs c | -0.16 | 5 | = 0.981 | -0.09 [-0.67, 0.67] | negligible | n.s. |
| a vs d | -0.67 | 5 | = 0.981 | -0.20 [-1.07, 0.32] | negligible | n.s. |
| a vs e | -0.44 | 5 | = 0.981 | -0.17 [-0.72, 0.62] | negligible | n.s. |
| b vs c | 1.54 | 5 | = 0.981 | 0.45 [-0.15, 1.01] | small | n.s. |
| b vs d | 0.61 | 5 | = 0.981 | 0.39 [-0.62, 0.81] | small | n.s. |
| b vs e | 1.35 | 5 | = 0.981 | 0.35 [-0.29, 0.95] | small | n.s. |
| c vs d | -0.15 | 5 | = 0.981 | -0.11 [-1.05, 0.51] | negligible | n.s. |
| c vs e | -0.24 | 5 | = 0.981 | -0.09 [-0.62, 0.72] | negligible | n.s. |
| d vs e | 0.00 | 5 | = 1.000 | 0.00 [-0.52, 0.93] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 206.57, BIC = 225.52
- **b vs a**: *β* = 0.45, *SE* = 0.249, *z* = 1.821, *p* = 0.069
- **c vs a**: *β* = 0.23, *SE* = 0.257, *z* = 0.894, *p* = 0.372
- **d vs a**: *β* = 0.51, *SE* = 0.266, *z* = 1.920, *p* = 0.055
- **e vs a**: *β* = 0.12, *SE* = 0.265, *z* = 0.474, *p* = 0.636
- **SNR**: *β* = -0.23, *SE* = 0.043, *z* = -5.448, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.45 | 0.25 | -1.82 | 0.069 | 0.473 | n.s. |
| a - c | -0.23 | 0.26 | -0.89 | 0.372 | 0.882 | n.s. |
| a - d | -0.51 | 0.27 | -1.92 | 0.055 | 0.431 | n.s. |
| a - e | -0.13 | 0.26 | -0.47 | 0.636 | 0.952 | n.s. |
| b - c | 0.22 | 0.24 | 0.94 | 0.348 | 0.882 | n.s. |
| b - d | -0.06 | 0.26 | -0.23 | 0.822 | 0.952 | n.s. |
| b - e | 0.33 | 0.25 | 1.31 | 0.191 | 0.773 | n.s. |
| c - d | -0.28 | 0.27 | -1.04 | 0.299 | 0.881 | n.s. |
| c - e | 0.10 | 0.26 | 0.40 | 0.688 | 0.952 | n.s. |
| d - e | 0.39 | 0.27 | 1.42 | 0.156 | 0.744 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.820, η²_G = 0.028
- Greenhouse-Geisser corrected: *p* = 0.624 (ε = 0.346)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.38 | 5 | = 0.983 | -0.17 [-0.83, 0.45] | negligible | n.s. |
| a vs c | -0.67 | 5 | = 0.983 | -0.17 [-1.01, 0.37] | negligible | n.s. |
| a vs d | -1.07 | 5 | = 0.983 | -0.42 [-1.35, 0.12] | small | n.s. |
| a vs e | -0.33 | 5 | = 0.983 | -0.19 [-0.73, 0.61] | negligible | n.s. |
| b vs c | -0.08 | 5 | = 0.983 | -0.02 [-0.12, 1.05] | negligible | n.s. |
| b vs d | -1.41 | 5 | = 0.983 | -0.40 [-1.52, 0.09] | small | n.s. |
| b vs e | -0.14 | 5 | = 0.983 | -0.04 [-0.36, 0.86] | negligible | n.s. |
| c vs d | -0.90 | 5 | = 0.983 | -0.31 [-1.36, 0.29] | small | n.s. |
| c vs e | -0.02 | 5 | = 0.983 | -0.01 [-0.64, 0.71] | negligible | n.s. |
| d vs e | 0.90 | 5 | = 0.983 | 0.34 [-0.39, 1.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 933.81, BIC = 955.98
- **b vs a**: *β* = -0.36, *SE* = 2.679, *z* = -0.136, *p* = 0.892
- **c vs a**: *β* = 0.74, *SE* = 2.680, *z* = 0.276, *p* = 0.782
- **d vs a**: *β* = -2.80, *SE* = 2.642, *z* = -1.061, *p* = 0.289
- **e vs a**: *β* = 0.70, *SE* = 2.717, *z* = 0.259, *p* = 0.796
- **SNR**: *β* = -0.19, *SE* = 0.223, *z* = -0.841, *p* = 0.400

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.37 | 2.68 | 0.14 | 0.892 | 0.999 | n.s. |
| a - c | -0.74 | 2.68 | -0.28 | 0.782 | 0.999 | n.s. |
| a - d | 2.80 | 2.64 | 1.06 | 0.289 | 0.935 | n.s. |
| a - e | -0.70 | 2.72 | -0.26 | 0.796 | 0.999 | n.s. |
| b - c | -1.11 | 2.70 | -0.41 | 0.682 | 0.999 | n.s. |
| b - d | 2.44 | 2.68 | 0.91 | 0.363 | 0.957 | n.s. |
| b - e | -1.07 | 2.75 | -0.39 | 0.698 | 0.999 | n.s. |
| c - d | 3.54 | 2.68 | 1.32 | 0.186 | 0.872 | n.s. |
| c - e | 0.04 | 2.74 | 0.01 | 0.989 | 0.999 | n.s. |
| d - e | -3.50 | 2.71 | -1.29 | 0.196 | 0.872 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.641, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.567 (ε = 0.615)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.34 | 22 | = 0.918 | 0.05 [-0.36, 0.50] | negligible | n.s. |
| a vs c | -0.08 | 22 | = 1.000 | -0.01 [-0.45, 0.42] | negligible | n.s. |
| a vs d | 0.97 | 22 | = 0.918 | 0.21 [-0.27, 0.58] | small | n.s. |
| a vs e | 0.48 | 22 | = 0.918 | 0.05 [-0.44, 0.41] | negligible | n.s. |
| b vs c | -0.37 | 22 | = 0.918 | -0.06 [-0.51, 0.36] | negligible | n.s. |
| b vs d | 0.97 | 22 | = 0.918 | 0.16 [-0.23, 0.64] | negligible | n.s. |
| b vs e | 0.00 | 22 | = 1.000 | 0.00 [-0.43, 0.43] | negligible | n.s. |
| c vs d | 1.16 | 22 | = 0.918 | 0.22 [-0.20, 0.68] | small | n.s. |
| c vs e | 0.67 | 22 | = 0.918 | 0.06 [-0.29, 0.57] | negligible | n.s. |
| d vs e | -0.85 | 22 | = 0.918 | -0.17 [-0.62, 0.23] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 414.71, BIC = 436.88
- **b vs a**: *β* = -0.12, *SE* = 0.296, *z* = -0.391, *p* = 0.696
- **c vs a**: *β* = 0.35, *SE* = 0.296, *z* = 1.200, *p* = 0.230
- **d vs a**: *β* = 0.10, *SE* = 0.292, *z* = 0.348, *p* = 0.728
- **e vs a**: *β* = -0.05, *SE* = 0.301, *z* = -0.172, *p* = 0.863
- **SNR**: *β* = -0.09, *SE* = 0.025, *z* = -3.735, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.12 | 0.30 | 0.39 | 0.696 | 0.991 | n.s. |
| a - c | -0.36 | 0.30 | -1.20 | 0.230 | 0.877 | n.s. |
| a - d | -0.10 | 0.29 | -0.35 | 0.728 | 0.991 | n.s. |
| a - e | 0.05 | 0.30 | 0.17 | 0.863 | 0.991 | n.s. |
| b - c | -0.47 | 0.30 | -1.58 | 0.114 | 0.703 | n.s. |
| b - d | -0.22 | 0.30 | -0.73 | 0.463 | 0.976 | n.s. |
| b - e | -0.06 | 0.30 | -0.21 | 0.834 | 0.991 | n.s. |
| c - d | 0.25 | 0.30 | 0.86 | 0.391 | 0.969 | n.s. |
| c - e | 0.41 | 0.30 | 1.35 | 0.179 | 0.830 | n.s. |
| d - e | 0.15 | 0.30 | 0.51 | 0.609 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.17, *p* = 0.330, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.30 | 22 | = 0.770 | 0.04 [-0.37, 0.49] | negligible | n.s. |
| a vs c | -1.29 | 22 | = 0.524 | -0.18 [-0.71, 0.17] | negligible | n.s. |
| a vs d | -0.62 | 22 | = 0.616 | -0.07 [-0.51, 0.34] | negligible | n.s. |
| a vs e | 0.83 | 22 | = 0.616 | 0.14 [-0.24, 0.61] | negligible | n.s. |
| b vs c | -1.33 | 22 | = 0.524 | -0.20 [-0.72, 0.16] | small | n.s. |
| b vs d | -0.66 | 22 | = 0.616 | -0.10 [-0.57, 0.30] | negligible | n.s. |
| b vs e | 0.60 | 22 | = 0.616 | 0.09 [-0.31, 0.56] | negligible | n.s. |
| c vs d | 0.76 | 22 | = 0.616 | 0.12 [-0.28, 0.59] | negligible | n.s. |
| c vs e | 1.68 | 22 | = 0.524 | 0.32 [-0.09, 0.80] | small | n.s. |
| d vs e | 1.31 | 22 | = 0.524 | 0.22 [-0.17, 0.69] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 483.21, BIC = 501.31
- **b vs a**: *β* = 1.38, *SE* = 2.068, *z* = 0.669, *p* = 0.503
- **c vs a**: *β* = -2.41, *SE* = 1.953, *z* = -1.235, *p* = 0.217
- **d vs a**: *β* = -1.01, *SE* = 2.134, *z* = -0.472, *p* = 0.637
- **e vs a**: *β* = -2.06, *SE* = 1.956, *z* = -1.051, *p* = 0.293
- **SNR**: *β* = 0.17, *SE* = 0.278, *z* = 0.616, *p* = 0.538

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -1.38 | 2.07 | -0.67 | 0.503 | 0.970 | n.s. |
| a - c | 2.41 | 1.95 | 1.23 | 0.217 | 0.859 | n.s. |
| a - d | 1.01 | 2.13 | 0.47 | 0.637 | 0.970 | n.s. |
| a - e | 2.06 | 1.96 | 1.05 | 0.293 | 0.909 | n.s. |
| b - c | 3.80 | 1.95 | 1.95 | 0.052 | 0.412 | n.s. |
| b - d | 2.39 | 2.26 | 1.06 | 0.290 | 0.909 | n.s. |
| b - e | 3.44 | 2.05 | 1.68 | 0.093 | 0.584 | n.s. |
| c - d | -1.40 | 2.16 | -0.65 | 0.516 | 0.970 | n.s. |
| c - e | -0.36 | 1.91 | -0.19 | 0.852 | 0.970 | n.s. |
| d - e | 1.05 | 2.13 | 0.49 | 0.623 | 0.970 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.60, *p* = 0.668, η²_G = 0.027
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -1.63 | 4 | = 0.693 | -0.33 [-1.05, 0.42] | small | n.s. |
| a vs c | 1.00 | 4 | = 0.935 | 0.14 [-0.41, 0.81] | negligible | n.s. |
| a vs d | 0.00 | 4 | = 1.000 | 0.00 [-0.30, 1.20] | negligible | n.s. |
| a vs e | 0.53 | 4 | = 0.973 | 0.12 [-0.50, 0.78] | negligible | n.s. |
| b vs c | 2.45 | 4 | = 0.693 | 0.45 [0.11, 1.59] | small | n.s. |
| b vs d | 0.78 | 4 | = 0.953 | 0.33 [-0.92, 0.92] | small | n.s. |
| b vs e | 1.50 | 4 | = 0.693 | 0.38 [0.08, 1.98] | small | n.s. |
| c vs d | -0.30 | 4 | = 0.973 | -0.14 [-1.10, 0.37] | negligible | n.s. |
| c vs e | 0.00 | 4 | = 1.000 | 0.00 [-0.24, 1.01] | negligible | n.s. |
| d vs e | 0.30 | 4 | = 0.973 | 0.12 [-0.94, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 186.19, BIC = 204.29
- **b vs a**: *β* = -0.21, *SE* = 0.242, *z* = -0.876, *p* = 0.381
- **c vs a**: *β* = -0.26, *SE* = 0.227, *z* = -1.160, *p* = 0.246
- **d vs a**: *β* = -0.68, *SE* = 0.251, *z* = -2.718, *p* = 0.007
- **e vs a**: *β* = -0.40, *SE* = 0.229, *z* = -1.729, *p* = 0.084
- **SNR**: *β* = 0.26, *SE* = 0.033, *z* = 7.774, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.21 | 0.24 | 0.88 | 0.381 | 0.853 | n.s. |
| a - c | 0.26 | 0.23 | 1.16 | 0.246 | 0.816 | n.s. |
| a - d | 0.68 | 0.25 | 2.72 | 0.007 | 0.064 | n.s. |
| a - e | 0.40 | 0.23 | 1.73 | 0.084 | 0.517 | n.s. |
| b - c | 0.05 | 0.23 | 0.23 | 0.821 | 0.853 | n.s. |
| b - d | 0.47 | 0.27 | 1.76 | 0.078 | 0.517 | n.s. |
| b - e | 0.18 | 0.24 | 0.76 | 0.448 | 0.853 | n.s. |
| c - d | 0.42 | 0.25 | 1.65 | 0.099 | 0.518 | n.s. |
| c - e | 0.13 | 0.22 | 0.59 | 0.557 | 0.853 | n.s. |
| d - e | -0.29 | 0.25 | -1.15 | 0.251 | 0.816 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.319, η²_G = 0.133
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.36 | 4 | = 0.761 | 0.12 [-0.79, 0.64] | negligible | n.s. |
| a vs c | -0.90 | 4 | = 0.712 | -0.35 [-0.73, 0.49] | small | n.s. |
| a vs d | 3.70 | 4 | = 0.209 | 0.71 [0.45, 2.52] | medium | n.s. |
| a vs e | 0.48 | 4 | = 0.761 | 0.32 [-0.35, 0.95] | small | n.s. |
| b vs c | -1.15 | 4 | = 0.712 | -0.47 [-0.76, 0.52] | small | n.s. |
| b vs d | 2.55 | 4 | = 0.212 | 0.58 [0.04, 2.54] | medium | n.s. |
| b vs e | 0.33 | 4 | = 0.761 | 0.19 [-0.55, 1.01] | negligible | n.s. |
| c vs d | 2.90 | 4 | = 0.212 | 1.07 [0.17, 1.97] | large | n.s. |
| c vs e | 0.88 | 4 | = 0.712 | 0.69 [-0.29, 0.95] | medium | n.s. |
| d vs e | -0.67 | 4 | = 0.761 | -0.43 [-1.07, 0.50] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 909.76, BIC = 930.19
- **b vs a**: *β* = 0.45, *SE* = 7.781, *z* = 0.057, *p* = 0.954
- **c vs a**: *β* = -4.01, *SE* = 7.214, *z* = -0.556, *p* = 0.578
- **d vs a**: *β* = 12.35, *SE* = 7.394, *z* = 1.671, *p* = 0.095
- **e vs a**: *β* = 2.86, *SE* = 7.692, *z* = 0.372, *p* = 0.710
- **SNR**: *β* = 0.00, *SE* = 0.501, *z* = 0.002, *p* = 0.998

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.45 | 7.78 | -0.06 | 0.954 | 0.982 | n.s. |
| a - c | 4.01 | 7.21 | 0.56 | 0.578 | 0.982 | n.s. |
| a - d | -12.35 | 7.39 | -1.67 | 0.095 | 0.592 | n.s. |
| a - e | -2.86 | 7.69 | -0.37 | 0.710 | 0.982 | n.s. |
| b - c | 4.45 | 7.47 | 0.60 | 0.551 | 0.982 | n.s. |
| b - d | -11.91 | 7.76 | -1.53 | 0.125 | 0.657 | n.s. |
| b - e | -2.42 | 7.74 | -0.31 | 0.755 | 0.982 | n.s. |
| c - d | -16.36 | 7.24 | -2.26 | 0.024 | 0.214 | n.s. |
| c - e | -6.87 | 7.39 | -0.93 | 0.353 | 0.926 | n.s. |
| d - e | 9.49 | 7.79 | 1.22 | 0.223 | 0.830 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.541, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.56 | 15 | = 0.806 | 0.17 [-0.40, 0.68] | negligible | n.s. |
| a vs c | 0.96 | 15 | = 0.806 | 0.25 [-0.37, 0.60] | small | n.s. |
| a vs d | -0.58 | 15 | = 0.806 | -0.15 [-0.84, 0.18] | negligible | n.s. |
| a vs e | 0.53 | 15 | = 0.806 | 0.12 [-0.54, 0.46] | negligible | n.s. |
| b vs c | 0.25 | 15 | = 0.812 | 0.07 [-0.43, 0.60] | negligible | n.s. |
| b vs d | -1.32 | 15 | = 0.806 | -0.33 [-0.82, 0.23] | small | n.s. |
| b vs e | -0.24 | 15 | = 0.812 | -0.05 [-0.59, 0.47] | negligible | n.s. |
| c vs d | -2.43 | 15 | = 0.282 | -0.45 [-1.09, -0.05] | small | n.s. |
| c vs e | -0.47 | 15 | = 0.806 | -0.13 [-0.73, 0.28] | negligible | n.s. |
| d vs e | 1.19 | 15 | = 0.806 | 0.28 [-0.24, 0.81] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 344.01, BIC = 364.44
- **b vs a**: *β* = 0.76, *SE* = 0.339, *z* = 2.249, *p* = 0.025
- **c vs a**: *β* = -0.17, *SE* = 0.318, *z* = -0.549, *p* = 0.583
- **d vs a**: *β* = 0.09, *SE* = 0.321, *z* = 0.265, *p* = 0.791
- **e vs a**: *β* = 0.47, *SE* = 0.335, *z* = 1.402, *p* = 0.161
- **SNR**: *β* = 0.10, *SE* = 0.024, *z* = 4.042, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.76 | 0.34 | -2.25 | 0.025 | 0.200 | n.s. |
| a - c | 0.17 | 0.32 | 0.55 | 0.583 | 0.856 | n.s. |
| a - d | -0.08 | 0.32 | -0.26 | 0.791 | 0.856 | n.s. |
| a - e | -0.47 | 0.34 | -1.40 | 0.161 | 0.651 | n.s. |
| b - c | 0.94 | 0.33 | 2.87 | 0.004 | 0.041 | * |
| b - d | 0.68 | 0.34 | 2.01 | 0.045 | 0.307 | n.s. |
| b - e | 0.29 | 0.34 | 0.87 | 0.384 | 0.856 | n.s. |
| c - d | -0.26 | 0.32 | -0.81 | 0.416 | 0.856 | n.s. |
| c - e | -0.64 | 0.32 | -2.00 | 0.046 | 0.307 | n.s. |
| d - e | -0.39 | 0.34 | -1.13 | 0.257 | 0.773 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.81, *p* = 0.033, η²_G = 0.030
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -2.15 | 15 | = 0.211 | -0.39 [-1.11, 0.03] | small | n.s. |
| a vs c | 0.26 | 15 | = 0.797 | 0.03 [-0.50, 0.46] | negligible | n.s. |
| a vs d | -0.30 | 15 | = 0.797 | -0.04 [-0.52, 0.48] | negligible | n.s. |
| a vs e | -1.50 | 15 | = 0.257 | -0.27 [-0.98, 0.06] | small | n.s. |
| b vs c | 2.51 | 15 | = 0.211 | 0.43 [0.03, 1.14] | small | n.s. |
| b vs d | 2.01 | 15 | = 0.211 | 0.35 [-0.03, 1.06] | small | n.s. |
| b vs e | 0.69 | 15 | = 0.715 | 0.12 [-0.36, 0.71] | negligible | n.s. |
| c vs d | -0.48 | 15 | = 0.797 | -0.07 [-0.48, 0.48] | negligible | n.s. |
| c vs e | -1.62 | 15 | = 0.253 | -0.31 [-1.00, 0.05] | small | n.s. |
| d vs e | -1.84 | 15 | = 0.214 | -0.23 [-1.08, 0.02] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.033) (no significant pairwise comparisons)

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
