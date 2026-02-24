# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:30:26

---

## 1. Analysis Overview

**Total Measurements:** 336
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
| 2a | 23 | 120.70 ms | 19.66 | 4.10 | [80.00, 144.00] |
| 2b | 23 | 115.13 ms | 22.59 | 4.71 | [80.00, 144.00] |
| 2c | 24 | 115.83 ms | 20.00 | 4.08 | [80.00, 144.00] |
| 2d | 20 | 114.80 ms | 21.33 | 4.77 | [80.00, 144.00] |
| 2e | 22 | 106.18 ms | 21.58 | 4.60 | [80.00, 136.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 23 | -3.90 µV | 4.59 | 0.96 | [-15.96, 4.29] |
| 2b | 23 | -4.02 µV | 4.25 | 0.89 | [-13.19, 5.05] |
| 2c | 24 | -5.36 µV | 5.23 | 1.07 | [-19.91, 3.71] |
| 2d | 20 | -4.74 µV | 6.06 | 1.36 | [-16.00, 13.55] |
| 2e | 22 | -5.95 µV | 4.80 | 1.02 | [-16.50, 0.24] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 23 | 174.09 ms | 11.18 | 2.33 | [156.00, 192.00] |
| 2b | 23 | 180.52 ms | 14.39 | 3.00 | [156.00, 204.00] |
| 2c | 24 | 184.33 ms | 14.59 | 2.98 | [156.00, 204.00] |
| 2d | 20 | 180.20 ms | 17.09 | 3.82 | [156.00, 204.00] |
| 2e | 22 | 178.18 ms | 17.49 | 3.73 | [156.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 23 | -5.95 µV | 3.83 | 0.80 | [-15.94, 1.94] |
| 2b | 23 | -3.60 µV | 4.09 | 0.85 | [-17.52, 2.31] |
| 2c | 24 | -3.56 µV | 4.13 | 0.84 | [-11.11, 5.36] |
| 2d | 20 | -5.95 µV | 6.04 | 1.35 | [-17.06, 5.52] |
| 2e | 22 | -3.75 µV | 5.43 | 1.16 | [-16.40, 12.83] |


### 2.3 P1 Component

#### Latency (Peak)

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 23 | 473.39 ms | 8.49 | 1.77 | [464.00, 484.00] |
| 2b | 23 | 472.52 ms | 7.66 | 1.60 | [464.00, 484.00] |
| 2c | 24 | 477.33 ms | 7.88 | 1.61 | [464.00, 484.00] |
| 2d | 20 | 473.80 ms | 8.46 | 1.89 | [464.00, 484.00] |
| 2e | 22 | 474.91 ms | 9.17 | 1.96 | [464.00, 484.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 23 | 3.86 µV | 4.91 | 1.02 | [-12.04, 10.50] |
| 2b | 23 | 4.12 µV | 4.16 | 0.87 | [-5.86, 13.26] |
| 2c | 24 | 2.96 µV | 6.23 | 1.27 | [-14.22, 12.68] |
| 2d | 20 | 4.54 µV | 6.93 | 1.55 | [-9.41, 15.10] |
| 2e | 22 | 3.53 µV | 5.16 | 1.10 | [-7.38, 14.94] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1006.35, BIC = 1028.09
- **2b vs 2a**: *β* = -5.38, *SE* = 5.583, *z* = -0.964, *p* = 0.335
- **2c vs 2a**: *β* = -4.85, *SE* = 5.488, *z* = -0.883, *p* = 0.377
- **2d vs 2a**: *β* = -4.95, *SE* = 5.809, *z* = -0.852, *p* = 0.394
- **2e vs 2a**: *β* = -14.30, *SE* = 5.678, *z* = -2.518, *p* = 0.012
- **SNR**: *β* = 0.46, *SE* = 1.187, *z* = 0.391, *p* = 0.696

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 5.38 | 5.58 | 0.96 | 0.335 | 0.914 | n.s. |
| 2a - 2c | 4.85 | 5.49 | 0.88 | 0.377 | 0.914 | n.s. |
| 2a - 2d | 4.95 | 5.81 | 0.85 | 0.394 | 0.914 | n.s. |
| 2a - 2e | 14.30 | 5.68 | 2.52 | 0.012 | 0.112 | n.s. |
| 2b - 2c | -0.53 | 5.51 | -0.10 | 0.923 | 1.000 | n.s. |
| 2b - 2d | -0.43 | 5.86 | -0.07 | 0.941 | 1.000 | n.s. |
| 2b - 2e | 8.92 | 5.79 | 1.54 | 0.123 | 0.610 | n.s. |
| 2c - 2d | 0.10 | 5.75 | 0.02 | 0.986 | 1.000 | n.s. |
| 2c - 2e | 9.45 | 5.62 | 1.68 | 0.093 | 0.584 | n.s. |
| 2d - 2e | 9.35 | 5.87 | 1.59 | 0.111 | 0.610 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.249, η²_G = 0.054
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | -0.13 | 16 | = 0.901 | -0.05 [-0.31, 0.58] | negligible | n.s. |
| 2a vs 2c | 1.11 | 16 | = 0.451 | 0.27 [-0.14, 0.74] | small | n.s. |
| 2a vs 2d | 1.26 | 16 | = 0.451 | 0.32 [-0.33, 0.64] | small | n.s. |
| 2a vs 2e | 1.68 | 16 | = 0.451 | 0.59 [-0.00, 0.96] | medium | n.s. |
| 2b vs 2c | 1.04 | 16 | = 0.451 | 0.30 [-0.41, 0.45] | small | n.s. |
| 2b vs 2d | 1.27 | 16 | = 0.451 | 0.35 [-0.44, 0.50] | small | n.s. |
| 2b vs 2e | 1.84 | 16 | = 0.451 | 0.61 [-0.04, 0.91] | medium | n.s. |
| 2c vs 2d | 0.28 | 16 | = 0.871 | 0.07 [-0.51, 0.42] | negligible | n.s. |
| 2c vs 2e | 1.05 | 16 | = 0.451 | 0.35 [-0.09, 0.83] | small | n.s. |
| 2d vs 2e | 0.71 | 16 | = 0.614 | 0.26 [-0.27, 0.74] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 676.78, BIC = 698.53
- **2b vs 2a**: *β* = 0.27, *SE* = 1.306, *z* = 0.205, *p* = 0.838
- **2c vs 2a**: *β* = -1.47, *SE* = 1.286, *z* = -1.145, *p* = 0.252
- **2d vs 2a**: *β* = -1.32, *SE* = 1.359, *z* = -0.974, *p* = 0.330
- **2e vs 2a**: *β* = -2.68, *SE* = 1.329, *z* = -2.017, *p* = 0.044
- **SNR**: *β* = -0.88, *SE* = 0.271, *z* = -3.243, *p* = 0.001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -0.27 | 1.31 | -0.20 | 0.838 | 0.974 | n.s. |
| 2a - 2c | 1.47 | 1.29 | 1.15 | 0.252 | 0.862 | n.s. |
| 2a - 2d | 1.32 | 1.36 | 0.97 | 0.330 | 0.862 | n.s. |
| 2a - 2e | 2.68 | 1.33 | 2.02 | 0.044 | 0.331 | n.s. |
| 2b - 2c | 1.74 | 1.29 | 1.35 | 0.177 | 0.790 | n.s. |
| 2b - 2d | 1.59 | 1.37 | 1.16 | 0.246 | 0.862 | n.s. |
| 2b - 2e | 2.95 | 1.35 | 2.18 | 0.029 | 0.256 | n.s. |
| 2c - 2d | -0.15 | 1.34 | -0.11 | 0.912 | 0.974 | n.s. |
| 2c - 2e | 1.21 | 1.32 | 0.92 | 0.359 | 0.862 | n.s. |
| 2d - 2e | 1.36 | 1.37 | 0.99 | 0.322 | 0.862 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.53, *p* = 0.714, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.34 | 16 | = 0.835 | 0.10 [-0.44, 0.44] | negligible | n.s. |
| 2a vs 2c | 0.89 | 16 | = 0.835 | 0.32 [-0.19, 0.69] | small | n.s. |
| 2a vs 2d | 0.70 | 16 | = 0.835 | 0.23 [-0.32, 0.65] | small | n.s. |
| 2a vs 2e | 1.22 | 16 | = 0.835 | 0.46 [-0.15, 0.79] | small | n.s. |
| 2b vs 2c | 0.82 | 16 | = 0.835 | 0.23 [-0.19, 0.69] | small | n.s. |
| 2b vs 2d | 0.46 | 16 | = 0.835 | 0.15 [-0.40, 0.54] | negligible | n.s. |
| 2b vs 2e | 1.32 | 16 | = 0.835 | 0.37 [-0.06, 0.89] | small | n.s. |
| 2c vs 2d | -0.15 | 16 | = 0.882 | -0.05 [-0.50, 0.44] | negligible | n.s. |
| 2c vs 2e | 0.32 | 16 | = 0.835 | 0.12 [-0.40, 0.49] | negligible | n.s. |
| 2d vs 2e | 0.53 | 16 | = 0.835 | 0.16 [-0.35, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 933.83, BIC = 955.58
- **2b vs 2a**: *β* = 6.51, *SE* = 4.139, *z* = 1.574, *p* = 0.115
- **2c vs 2a**: *β* = 10.22, *SE* = 4.080, *z* = 2.505, *p* = 0.012
- **2d vs 2a**: *β* = 6.29, *SE* = 4.284, *z* = 1.469, *p* = 0.142
- **2e vs 2a**: *β* = 4.00, *SE* = 4.243, *z* = 0.942, *p* = 0.346
- **SNR**: *β* = 0.13, *SE* = 0.785, *z* = 0.170, *p* = 0.865

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -6.52 | 4.14 | -1.57 | 0.115 | 0.669 | n.s. |
| 2a - 2c | -10.22 | 4.08 | -2.50 | 0.012 | 0.116 | n.s. |
| 2a - 2d | -6.29 | 4.28 | -1.47 | 0.142 | 0.682 | n.s. |
| 2a - 2e | -4.00 | 4.24 | -0.94 | 0.346 | 0.922 | n.s. |
| 2b - 2c | -3.70 | 4.07 | -0.91 | 0.363 | 0.922 | n.s. |
| 2b - 2d | 0.22 | 4.28 | 0.05 | 0.958 | 0.958 | n.s. |
| 2b - 2e | 2.52 | 4.18 | 0.60 | 0.547 | 0.922 | n.s. |
| 2c - 2d | 3.93 | 4.24 | 0.93 | 0.354 | 0.922 | n.s. |
| 2c - 2e | 6.22 | 4.15 | 1.50 | 0.133 | 0.682 | n.s. |
| 2d - 2e | 2.29 | 4.37 | 0.52 | 0.600 | 0.922 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.23, *p* = 0.305, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | -1.67 | 16 | = 0.380 | -0.43 [-0.84, 0.08] | small | n.s. |
| 2a vs 2c | -2.77 | 16 | = 0.136 | -0.73 [-1.14, -0.19] | medium | n.s. |
| 2a vs 2d | -1.94 | 16 | = 0.351 | -0.61 [-0.80, 0.19] | medium | n.s. |
| 2a vs 2e | -0.86 | 16 | = 0.646 | -0.33 [-0.63, 0.29] | small | n.s. |
| 2b vs 2c | -1.02 | 16 | = 0.646 | -0.27 [-0.61, 0.26] | small | n.s. |
| 2b vs 2d | -1.02 | 16 | = 0.646 | -0.21 [-0.53, 0.41] | small | n.s. |
| 2b vs 2e | 0.12 | 16 | = 0.904 | 0.04 [-0.35, 0.57] | negligible | n.s. |
| 2c vs 2d | 0.14 | 16 | = 0.904 | 0.04 [-0.39, 0.55] | negligible | n.s. |
| 2c vs 2e | 0.73 | 16 | = 0.646 | 0.28 [-0.20, 0.71] | small | n.s. |
| 2d vs 2e | 0.66 | 16 | = 0.646 | 0.23 [-0.38, 0.62] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 659.31, BIC = 681.05
- **2b vs 2a**: *β* = 1.78, *SE* = 1.212, *z* = 1.473, *p* = 0.141
- **2c vs 2a**: *β* = 2.01, *SE* = 1.195, *z* = 1.683, *p* = 0.092
- **2d vs 2a**: *β* = -0.14, *SE* = 1.257, *z* = -0.111, *p* = 0.912
- **2e vs 2a**: *β* = 1.35, *SE* = 1.243, *z* = 1.083, *p* = 0.279
- **SNR**: *β* = -0.91, *SE* = 0.233, *z* = -3.882, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -1.79 | 1.21 | -1.47 | 0.141 | 0.657 | n.s. |
| 2a - 2c | -2.01 | 1.20 | -1.68 | 0.092 | 0.582 | n.s. |
| 2a - 2d | 0.14 | 1.26 | 0.11 | 0.912 | 0.978 | n.s. |
| 2a - 2e | -1.35 | 1.24 | -1.08 | 0.279 | 0.815 | n.s. |
| 2b - 2c | -0.23 | 1.19 | -0.19 | 0.850 | 0.978 | n.s. |
| 2b - 2d | 1.93 | 1.26 | 1.53 | 0.125 | 0.657 | n.s. |
| 2b - 2e | 0.44 | 1.23 | 0.36 | 0.720 | 0.978 | n.s. |
| 2c - 2d | 2.15 | 1.24 | 1.73 | 0.083 | 0.580 | n.s. |
| 2c - 2e | 0.66 | 1.21 | 0.55 | 0.584 | 0.970 | n.s. |
| 2d - 2e | -1.49 | 1.28 | -1.16 | 0.245 | 0.815 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.33, *p* = 0.267, η²_G = 0.058
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | -1.97 | 16 | = 0.379 | -0.56 [-0.97, -0.03] | medium | n.s. |
| 2a vs 2c | -1.67 | 16 | = 0.379 | -0.62 [-0.91, -0.00] | medium | n.s. |
| 2a vs 2d | -0.09 | 16 | = 0.932 | -0.03 [-0.56, 0.41] | negligible | n.s. |
| 2a vs 2e | -1.34 | 16 | = 0.379 | -0.56 [-0.74, 0.19] | medium | n.s. |
| 2b vs 2c | -0.15 | 16 | = 0.932 | -0.05 [-0.47, 0.39] | negligible | n.s. |
| 2b vs 2d | 1.36 | 16 | = 0.379 | 0.39 [-0.20, 0.75] | small | n.s. |
| 2b vs 2e | -0.37 | 16 | = 0.932 | -0.11 [-0.46, 0.45] | negligible | n.s. |
| 2c vs 2d | 1.25 | 16 | = 0.379 | 0.44 [-0.21, 0.75] | small | n.s. |
| 2c vs 2e | -0.21 | 16 | = 0.932 | -0.06 [-0.44, 0.45] | negligible | n.s. |
| 2d vs 2e | -1.49 | 16 | = 0.379 | -0.43 [-0.92, 0.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 803.21, BIC = 824.96
- **2b vs 2a**: *β* = -0.77, *SE* = 2.402, *z* = -0.319, *p* = 0.750
- **2c vs 2a**: *β* = 4.05, *SE* = 2.378, *z* = 1.704, *p* = 0.088
- **2d vs 2a**: *β* = 0.64, *SE* = 2.509, *z* = 0.254, *p* = 0.800
- **2e vs 2a**: *β* = 1.43, *SE* = 2.429, *z* = 0.589, *p* = 0.556
- **SNR**: *β* = -0.24, *SE* = 0.350, *z* = -0.686, *p* = 0.492

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 0.77 | 2.40 | 0.32 | 0.750 | 0.984 | n.s. |
| 2a - 2c | -4.05 | 2.38 | -1.70 | 0.088 | 0.565 | n.s. |
| 2a - 2d | -0.64 | 2.51 | -0.25 | 0.800 | 0.984 | n.s. |
| 2a - 2e | -1.43 | 2.43 | -0.59 | 0.556 | 0.983 | n.s. |
| 2b - 2c | -4.82 | 2.37 | -2.03 | 0.042 | 0.351 | n.s. |
| 2b - 2d | -1.40 | 2.49 | -0.56 | 0.574 | 0.983 | n.s. |
| 2b - 2e | -2.20 | 2.44 | -0.90 | 0.368 | 0.937 | n.s. |
| 2c - 2d | 3.41 | 2.47 | 1.38 | 0.167 | 0.768 | n.s. |
| 2c - 2e | 2.62 | 2.42 | 1.08 | 0.278 | 0.898 | n.s. |
| 2d - 2e | -0.79 | 2.56 | -0.31 | 0.757 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.64, *p* = 0.636, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.69 | 16 | = 0.812 | 0.23 [-0.37, 0.52] | small | n.s. |
| 2a vs 2c | -0.72 | 16 | = 0.812 | -0.29 [-0.73, 0.15] | small | n.s. |
| 2a vs 2d | 0.42 | 16 | = 0.812 | 0.11 [-0.36, 0.61] | negligible | n.s. |
| 2a vs 2e | -0.16 | 16 | = 0.874 | -0.05 [-0.66, 0.26] | negligible | n.s. |
| 2b vs 2c | -1.44 | 16 | = 0.812 | -0.55 [-0.88, 0.02] | medium | n.s. |
| 2b vs 2d | -0.35 | 16 | = 0.812 | -0.12 [-0.59, 0.35] | negligible | n.s. |
| 2b vs 2e | -0.86 | 16 | = 0.812 | -0.28 [-0.63, 0.28] | small | n.s. |
| 2c vs 2d | 1.21 | 16 | = 0.812 | 0.40 [-0.18, 0.78] | small | n.s. |
| 2c vs 2e | 0.63 | 16 | = 0.812 | 0.22 [-0.25, 0.65] | small | n.s. |
| 2d vs 2e | -0.50 | 16 | = 0.812 | -0.16 [-0.58, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 705.63, BIC = 727.38
- **2b vs 2a**: *β* = 0.12, *SE* = 1.508, *z* = 0.077, *p* = 0.939
- **2c vs 2a**: *β* = -1.08, *SE* = 1.490, *z* = -0.722, *p* = 0.470
- **2d vs 2a**: *β* = 0.29, *SE* = 1.579, *z* = 0.184, *p* = 0.854
- **2e vs 2a**: *β* = -0.07, *SE* = 1.523, *z* = -0.048, *p* = 0.962
- **SNR**: *β* = 0.48, *SE* = 0.238, *z* = 2.011, *p* = 0.044

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -0.12 | 1.51 | -0.08 | 0.939 | 1.000 | n.s. |
| 2a - 2c | 1.08 | 1.49 | 0.72 | 0.470 | 0.994 | n.s. |
| 2a - 2d | -0.29 | 1.58 | -0.18 | 0.854 | 1.000 | n.s. |
| 2a - 2e | 0.07 | 1.52 | 0.05 | 0.962 | 1.000 | n.s. |
| 2b - 2c | 1.19 | 1.49 | 0.80 | 0.422 | 0.993 | n.s. |
| 2b - 2d | -0.18 | 1.56 | -0.11 | 0.911 | 1.000 | n.s. |
| 2b - 2e | 0.19 | 1.53 | 0.12 | 0.902 | 1.000 | n.s. |
| 2c - 2d | -1.37 | 1.55 | -0.88 | 0.378 | 0.991 | n.s. |
| 2c - 2e | -1.00 | 1.51 | -0.66 | 0.508 | 0.994 | n.s. |
| 2d - 2e | 0.36 | 1.61 | 0.23 | 0.821 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.817, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.07 | 16 | = 0.943 | 0.02 [-0.53, 0.36] | negligible | n.s. |
| 2a vs 2c | 1.00 | 16 | = 0.912 | 0.27 [-0.32, 0.54] | small | n.s. |
| 2a vs 2d | -0.23 | 16 | = 0.912 | -0.08 [-0.60, 0.37] | negligible | n.s. |
| 2a vs 2e | 0.62 | 16 | = 0.912 | 0.15 [-0.39, 0.52] | negligible | n.s. |
| 2b vs 2c | 1.14 | 16 | = 0.912 | 0.27 [-0.16, 0.72] | small | n.s. |
| 2b vs 2d | -0.24 | 16 | = 0.912 | -0.10 [-0.49, 0.44] | negligible | n.s. |
| 2b vs 2e | 0.49 | 16 | = 0.912 | 0.15 [-0.40, 0.51] | negligible | n.s. |
| 2c vs 2d | -0.82 | 16 | = 0.912 | -0.31 [-0.68, 0.27] | small | n.s. |
| 2c vs 2e | -0.43 | 16 | = 0.912 | -0.14 [-0.53, 0.36] | negligible | n.s. |
| 2d vs 2e | 0.58 | 16 | = 0.912 | 0.21 [-0.44, 0.56] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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

#### Amplitude

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
