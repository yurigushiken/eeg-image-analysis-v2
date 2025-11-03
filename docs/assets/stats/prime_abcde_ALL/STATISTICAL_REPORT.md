# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:48:47

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
| a | 11 | 105.09 ms | 9.65 | 2.91 | [92.00, 112.00] |
| b | 5 | 103.20 ms | 8.67 | 3.88 | [92.00, 112.00] |
| c | 4 | 100.00 ms | 9.80 | 4.90 | [92.00, 112.00] |
| d | 11 | 100.73 ms | 9.60 | 2.90 | [92.00, 112.00] |
| e | 9 | 100.89 ms | 10.54 | 3.51 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 11 | 1.71 µV | 0.84 | 0.25 | [0.52, 3.03] |
| b | 5 | 1.16 µV | 0.98 | 0.44 | [0.28, 2.72] |
| c | 4 | 1.14 µV | 1.13 | 0.56 | [0.21, 2.75] |
| d | 11 | 1.49 µV | 1.05 | 0.32 | [0.31, 3.23] |
| e | 9 | 1.55 µV | 0.66 | 0.22 | [0.47, 2.81] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 174.67 ms | 16.87 | 3.44 | [144.00, 208.00] |
| b | 23 | 172.17 ms | 16.69 | 3.48 | [148.00, 208.00] |
| c | 23 | 174.61 ms | 15.75 | 3.28 | [144.00, 200.00] |
| d | 24 | 173.00 ms | 17.94 | 3.66 | [148.00, 204.00] |
| e | 24 | 174.67 ms | 16.46 | 3.36 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | -4.98 µV | 1.91 | 0.39 | [-9.00, -1.24] |
| b | 23 | -5.33 µV | 2.37 | 0.49 | [-11.61, -2.00] |
| c | 23 | -4.70 µV | 2.02 | 0.42 | [-8.21, -0.88] |
| d | 24 | -5.06 µV | 1.83 | 0.37 | [-9.42, -2.04] |
| e | 24 | -5.53 µV | 2.23 | 0.46 | [-11.34, -2.20] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 13 | 107.08 ms | 8.97 | 2.49 | [92.00, 116.00] |
| b | 16 | 111.00 ms | 7.08 | 1.77 | [96.00, 116.00] |
| c | 16 | 105.50 ms | 8.12 | 2.03 | [92.00, 116.00] |
| d | 11 | 107.27 ms | 7.76 | 2.34 | [96.00, 116.00] |
| e | 15 | 106.40 ms | 7.97 | 2.06 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 13 | 2.39 µV | 1.62 | 0.45 | [0.35, 5.47] |
| b | 16 | 2.19 µV | 1.58 | 0.40 | [0.14, 5.47] |
| c | 16 | 2.42 µV | 1.62 | 0.40 | [0.60, 6.89] |
| d | 11 | 2.01 µV | 1.25 | 0.38 | [0.32, 4.49] |
| e | 15 | 1.88 µV | 1.37 | 0.35 | [0.33, 4.92] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 18 | 476.22 ms | 34.37 | 8.10 | [428.00, 536.00] |
| b | 17 | 483.53 ms | 33.28 | 8.07 | [428.00, 536.00] |
| c | 20 | 472.60 ms | 30.22 | 6.76 | [424.00, 536.00] |
| d | 19 | 491.37 ms | 29.52 | 6.77 | [436.00, 536.00] |
| e | 19 | 485.68 ms | 32.40 | 7.43 | [436.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 18 | 4.26 µV | 2.28 | 0.54 | [0.98, 7.58] |
| b | 17 | 5.32 µV | 2.90 | 0.70 | [0.72, 11.68] |
| c | 20 | 3.75 µV | 1.96 | 0.44 | [1.17, 6.84] |
| d | 19 | 4.07 µV | 2.53 | 0.58 | [0.85, 8.97] |
| e | 19 | 4.91 µV | 2.53 | 0.58 | [1.06, 9.23] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 291.18, BIC = 304.69
- **b vs a**: *β* = -5.64, *SE* = 3.335, *z* = -1.691, *p* = 0.091
- **c vs a**: *β* = -3.48, *SE* = 3.608, *z* = -0.965, *p* = 0.335
- **d vs a**: *β* = -6.28, *SE* = 2.726, *z* = -2.303, *p* = 0.021
- **e vs a**: *β* = -3.96, *SE* = 2.670, *z* = -1.484, *p* = 0.138
- **SNR**: *β* = 0.85, *SE* = 0.612, *z* = 1.390, *p* = 0.165

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 5.64 | 3.34 | 1.69 | 0.091 | 0.575 | n.s. |
| a - c | 3.48 | 3.61 | 0.97 | 0.335 | 0.942 | n.s. |
| a - d | 6.28 | 2.73 | 2.30 | 0.021 | 0.193 | n.s. |
| a - e | 3.96 | 2.67 | 1.48 | 0.138 | 0.695 | n.s. |
| b - c | -2.16 | 4.17 | -0.52 | 0.605 | 0.976 | n.s. |
| b - d | 0.64 | 3.36 | 0.19 | 0.850 | 0.977 | n.s. |
| b - e | -1.68 | 3.34 | -0.50 | 0.615 | 0.976 | n.s. |
| c - d | 2.80 | 3.81 | 0.73 | 0.463 | 0.955 | n.s. |
| c - e | 0.48 | 3.88 | 0.12 | 0.902 | 0.977 | n.s. |
| d - e | -2.32 | 2.74 | -0.85 | 0.397 | 0.952 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 83.06, BIC = 96.57
- **b vs a**: *β* = -0.34, *SE* = 0.279, *z* = -1.204, *p* = 0.228
- **c vs a**: *β* = -0.30, *SE* = 0.292, *z* = -1.043, *p* = 0.297
- **d vs a**: *β* = -0.42, *SE* = 0.231, *z* = -1.845, *p* = 0.065
- **e vs a**: *β* = -0.09, *SE* = 0.225, *z* = -0.380, *p* = 0.704
- **SNR**: *β* = 0.29, *SE* = 0.050, *z* = 5.861, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.34 | 0.28 | 1.20 | 0.228 | 0.874 | n.s. |
| a - c | 0.30 | 0.29 | 1.04 | 0.297 | 0.915 | n.s. |
| a - d | 0.43 | 0.23 | 1.84 | 0.065 | 0.490 | n.s. |
| a - e | 0.09 | 0.23 | 0.38 | 0.704 | 0.991 | n.s. |
| b - c | -0.03 | 0.33 | -0.10 | 0.924 | 0.991 | n.s. |
| b - d | 0.09 | 0.27 | 0.33 | 0.740 | 0.991 | n.s. |
| b - e | -0.25 | 0.27 | -0.94 | 0.345 | 0.921 | n.s. |
| c - d | 0.12 | 0.30 | 0.40 | 0.689 | 0.991 | n.s. |
| c - e | -0.22 | 0.31 | -0.71 | 0.476 | 0.960 | n.s. |
| d - e | -0.34 | 0.22 | -1.57 | 0.117 | 0.675 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 914.84, BIC = 937.01
- **b vs a**: *β* = -1.50, *SE* = 2.441, *z* = -0.614, *p* = 0.539
- **c vs a**: *β* = 1.38, *SE* = 2.416, *z* = 0.571, *p* = 0.568
- **d vs a**: *β* = -1.50, *SE* = 2.393, *z* = -0.625, *p* = 0.532
- **e vs a**: *β* = 0.47, *SE* = 2.483, *z* = 0.187, *p* = 0.852
- **SNR**: *β* = -0.12, *SE* = 0.185, *z* = -0.653, *p* = 0.514

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 1.50 | 2.44 | 0.61 | 0.539 | 0.990 | n.s. |
| a - c | -1.38 | 2.42 | -0.57 | 0.568 | 0.990 | n.s. |
| a - d | 1.50 | 2.39 | 0.62 | 0.532 | 0.990 | n.s. |
| a - e | -0.46 | 2.48 | -0.19 | 0.852 | 0.990 | n.s. |
| b - c | -2.88 | 2.45 | -1.17 | 0.241 | 0.930 | n.s. |
| b - d | -0.00 | 2.41 | -0.00 | 0.999 | 0.999 | n.s. |
| b - e | -1.96 | 2.43 | -0.81 | 0.419 | 0.987 | n.s. |
| c - d | 2.87 | 2.41 | 1.19 | 0.234 | 0.930 | n.s. |
| c - e | 0.91 | 2.47 | 0.37 | 0.711 | 0.990 | n.s. |
| d - e | -1.96 | 2.42 | -0.81 | 0.418 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.592, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.538 (ε = 0.666)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.98 | 21 | = 0.672 | 0.16 [-0.23, 0.64] | negligible | n.s. |
| a vs c | -0.32 | 21 | = 0.836 | -0.05 [-0.56, 0.31] | negligible | n.s. |
| a vs d | 1.00 | 21 | = 0.672 | 0.16 [-0.29, 0.56] | negligible | n.s. |
| a vs e | 0.73 | 21 | = 0.791 | 0.10 [-0.42, 0.42] | negligible | n.s. |
| b vs c | -1.10 | 21 | = 0.672 | -0.21 [-0.68, 0.21] | small | n.s. |
| b vs d | 0.00 | 21 | = 1.000 | 0.00 [-0.41, 0.45] | negligible | n.s. |
| b vs e | -0.39 | 21 | = 0.836 | -0.08 [-0.51, 0.35] | negligible | n.s. |
| c vs d | 1.03 | 21 | = 0.672 | 0.20 [-0.23, 0.64] | small | n.s. |
| c vs e | 1.23 | 21 | = 0.672 | 0.15 [-0.28, 0.59] | negligible | n.s. |
| d vs e | -0.42 | 21 | = 0.836 | -0.07 [-0.56, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 398.98, BIC = 421.14
- **b vs a**: *β* = -0.03, *SE* = 0.277, *z* = -0.089, *p* = 0.929
- **c vs a**: *β* = 0.41, *SE* = 0.274, *z* = 1.517, *p* = 0.129
- **d vs a**: *β* = 0.04, *SE* = 0.271, *z* = 0.164, *p* = 0.869
- **e vs a**: *β* = -0.21, *SE* = 0.282, *z* = -0.756, *p* = 0.450
- **SNR**: *β* = -0.09, *SE* = 0.021, *z* = -3.984, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.02 | 0.28 | 0.09 | 0.929 | 0.992 | n.s. |
| a - c | -0.42 | 0.27 | -1.52 | 0.129 | 0.669 | n.s. |
| a - d | -0.04 | 0.27 | -0.16 | 0.869 | 0.992 | n.s. |
| a - e | 0.21 | 0.28 | 0.76 | 0.450 | 0.950 | n.s. |
| b - c | -0.44 | 0.28 | -1.58 | 0.113 | 0.662 | n.s. |
| b - d | -0.07 | 0.27 | -0.25 | 0.800 | 0.992 | n.s. |
| b - e | 0.19 | 0.28 | 0.68 | 0.494 | 0.950 | n.s. |
| c - d | 0.37 | 0.27 | 1.36 | 0.175 | 0.740 | n.s. |
| c - e | 0.63 | 0.28 | 2.24 | 0.025 | 0.224 | n.s. |
| d - e | 0.26 | 0.27 | 0.94 | 0.348 | 0.923 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.04, *p* = 0.096, η²_G = 0.020
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.78 | 21 | = 0.558 | 0.09 [-0.28, 0.59] | negligible | n.s. |
| a vs c | -1.25 | 21 | = 0.375 | -0.18 [-0.71, 0.17] | negligible | n.s. |
| a vs d | 0.40 | 21 | = 0.716 | 0.05 [-0.34, 0.50] | negligible | n.s. |
| a vs e | 1.52 | 21 | = 0.359 | 0.27 [-0.09, 0.78] | small | n.s. |
| b vs c | -1.70 | 21 | = 0.359 | -0.24 [-0.82, 0.10] | small | n.s. |
| b vs d | -0.37 | 21 | = 0.716 | -0.06 [-0.52, 0.34] | negligible | n.s. |
| b vs e | 0.95 | 21 | = 0.501 | 0.15 [-0.22, 0.65] | negligible | n.s. |
| c vs d | 1.58 | 21 | = 0.359 | 0.23 [-0.08, 0.82] | small | n.s. |
| c vs e | 2.22 | 21 | = 0.359 | 0.42 [0.04, 0.95] | small | n.s. |
| d vs e | 1.31 | 21 | = 0.375 | 0.23 [-0.13, 0.73] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 477.51, BIC = 495.61
- **b vs a**: *β* = 5.20, *SE* = 1.931, *z* = 2.692, *p* = 0.007
- **c vs a**: *β* = -1.09, *SE* = 1.979, *z* = -0.553, *p* = 0.580
- **d vs a**: *β* = 0.41, *SE* = 2.070, *z* = 0.197, *p* = 0.844
- **e vs a**: *β* = 0.16, *SE* = 1.914, *z* = 0.086, *p* = 0.932
- **SNR**: *β* = 0.23, *SE* = 0.202, *z* = 1.133, *p* = 0.257

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -5.20 | 1.93 | -2.69 | 0.007 | 0.062 | n.s. |
| a - c | 1.09 | 1.98 | 0.55 | 0.580 | 0.980 | n.s. |
| a - d | -0.41 | 2.07 | -0.20 | 0.844 | 0.996 | n.s. |
| a - e | -0.16 | 1.91 | -0.09 | 0.932 | 0.996 | n.s. |
| b - c | 6.29 | 1.83 | 3.44 | < .001 | 0.006 | ** |
| b - d | 4.79 | 2.07 | 2.32 | 0.021 | 0.135 | n.s. |
| b - e | 5.03 | 1.89 | 2.67 | 0.008 | 0.062 | n.s. |
| c - d | -1.50 | 2.11 | -0.71 | 0.477 | 0.980 | n.s. |
| c - e | -1.26 | 1.91 | -0.66 | 0.509 | 0.980 | n.s. |
| d - e | 0.24 | 2.03 | 0.12 | 0.905 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.613, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -1.46 | 5 | = 0.677 | -0.37 [-1.31, 0.15] | small | n.s. |
| a vs c | 0.00 | 5 | = 1.000 | 0.00 [-0.64, 0.64] | negligible | n.s. |
| a vs d | 0.00 | 5 | = 1.000 | 0.00 [-0.89, 0.65] | negligible | n.s. |
| a vs e | 0.00 | 5 | = 1.000 | 0.00 [-0.67, 0.67] | negligible | n.s. |
| b vs c | 2.24 | 5 | = 0.677 | 0.39 [0.19, 1.54] | small | n.s. |
| b vs d | 1.17 | 5 | = 0.739 | 0.45 [-0.34, 1.46] | small | n.s. |
| b vs e | 1.46 | 5 | = 0.677 | 0.34 [0.16, 1.94] | small | n.s. |
| c vs d | 0.00 | 5 | = 1.000 | 0.00 [-0.80, 0.63] | negligible | n.s. |
| c vs e | 0.00 | 5 | = 1.000 | 0.00 [-0.52, 0.76] | negligible | n.s. |
| d vs e | 0.00 | 5 | = 1.000 | 0.00 [-0.96, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 166.22, BIC = 184.32
- **b vs a**: *β* = -0.08, *SE* = 0.193, *z* = -0.399, *p* = 0.690
- **c vs a**: *β* = -0.34, *SE* = 0.198, *z* = -1.712, *p* = 0.087
- **d vs a**: *β* = -0.60, *SE* = 0.207, *z* = -2.923, *p* = 0.003
- **e vs a**: *β* = -0.48, *SE* = 0.191, *z* = -2.503, *p* = 0.012
- **SNR**: *β* = 0.17, *SE* = 0.021, *z* = 8.205, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.08 | 0.19 | 0.40 | 0.690 | 0.848 | n.s. |
| a - c | 0.34 | 0.20 | 1.71 | 0.087 | 0.420 | n.s. |
| a - d | 0.60 | 0.21 | 2.92 | 0.003 | 0.034 | * |
| a - e | 0.48 | 0.19 | 2.50 | 0.012 | 0.101 | n.s. |
| b - c | 0.26 | 0.18 | 1.43 | 0.152 | 0.562 | n.s. |
| b - d | 0.53 | 0.21 | 2.52 | 0.012 | 0.101 | n.s. |
| b - e | 0.40 | 0.19 | 2.10 | 0.035 | 0.223 | n.s. |
| c - d | 0.27 | 0.21 | 1.25 | 0.213 | 0.616 | n.s. |
| c - e | 0.14 | 0.19 | 0.73 | 0.467 | 0.848 | n.s. |
| d - e | -0.13 | 0.20 | -0.62 | 0.533 | 0.848 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.204, η²_G = 0.094
- Greenhouse-Geisser corrected: *p* = 0.242 (ε = 0.506)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.08 | 5 | = 0.939 | 0.02 [-0.95, 0.42] | negligible | n.s. |
| a vs c | -0.36 | 5 | = 0.812 | -0.14 [-0.79, 0.49] | negligible | n.s. |
| a vs d | 6.27 | 5 | = 0.015 | 0.73 [0.66, 3.32] | medium | * |
| a vs e | 0.97 | 5 | = 0.626 | 0.44 [-0.36, 1.02] | small | n.s. |
| b vs c | -0.43 | 5 | = 0.812 | -0.15 [-0.59, 0.56] | negligible | n.s. |
| b vs d | 3.35 | 5 | = 0.101 | 0.65 [0.25, 2.63] | medium | n.s. |
| b vs e | 1.15 | 5 | = 0.626 | 0.39 [-0.28, 1.23] | small | n.s. |
| c vs d | 2.37 | 5 | = 0.214 | 0.78 [0.02, 1.69] | medium | n.s. |
| c vs e | 0.97 | 5 | = 0.626 | 0.52 [-0.24, 1.08] | medium | n.s. |
| d vs e | -0.58 | 5 | = 0.812 | -0.24 [-1.05, 0.51] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 889.09, BIC = 909.35
- **b vs a**: *β* = 8.99, *SE* = 7.611, *z* = 1.181, *p* = 0.238
- **c vs a**: *β* = -3.27, *SE* = 7.196, *z* = -0.455, *p* = 0.649
- **d vs a**: *β* = 13.79, *SE* = 7.255, *z* = 1.900, *p* = 0.057
- **e vs a**: *β* = 11.94, *SE* = 7.447, *z* = 1.604, *p* = 0.109
- **SNR**: *β* = -0.43, *SE* = 0.530, *z* = -0.819, *p* = 0.413

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -8.99 | 7.61 | -1.18 | 0.238 | 0.742 | n.s. |
| a - c | 3.27 | 7.20 | 0.45 | 0.649 | 0.957 | n.s. |
| a - d | -13.79 | 7.26 | -1.90 | 0.057 | 0.377 | n.s. |
| a - e | -11.94 | 7.45 | -1.60 | 0.109 | 0.508 | n.s. |
| b - c | 12.26 | 7.37 | 1.66 | 0.096 | 0.508 | n.s. |
| b - d | -4.80 | 7.56 | -0.63 | 0.526 | 0.949 | n.s. |
| b - e | -2.95 | 7.44 | -0.40 | 0.691 | 0.957 | n.s. |
| c - d | -17.06 | 7.10 | -2.40 | 0.016 | 0.152 | n.s. |
| c - e | -15.21 | 7.18 | -2.12 | 0.034 | 0.267 | n.s. |
| d - e | 1.84 | 7.47 | 0.25 | 0.805 | 0.957 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.317, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.25 | 15 | = 0.895 | -0.07 [-0.60, 0.47] | negligible | n.s. |
| a vs c | 0.91 | 15 | = 0.746 | 0.27 [-0.39, 0.61] | small | n.s. |
| a vs d | -0.81 | 15 | = 0.746 | -0.20 [-0.89, 0.14] | small | n.s. |
| a vs e | -0.38 | 15 | = 0.883 | -0.10 [-0.80, 0.22] | negligible | n.s. |
| b vs c | 1.56 | 15 | = 0.465 | 0.36 [-0.13, 0.94] | small | n.s. |
| b vs d | -0.71 | 15 | = 0.746 | -0.13 [-0.67, 0.37] | negligible | n.s. |
| b vs e | -0.11 | 15 | = 0.916 | -0.02 [-0.56, 0.51] | negligible | n.s. |
| c vs d | -2.88 | 15 | = 0.115 | -0.54 [-1.18, -0.12] | medium | n.s. |
| c vs e | -2.24 | 15 | = 0.201 | -0.42 [-1.04, -0.01] | small | n.s. |
| d vs e | 0.66 | 15 | = 0.746 | 0.11 [-0.37, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 306.58, BIC = 326.84
- **b vs a**: *β* = 0.67, *SE* = 0.284, *z* = 2.346, *p* = 0.019
- **c vs a**: *β* = -0.34, *SE* = 0.268, *z* = -1.253, *p* = 0.210
- **d vs a**: *β* = 0.02, *SE* = 0.269, *z* = 0.090, *p* = 0.928
- **e vs a**: *β* = 0.44, *SE* = 0.279, *z* = 1.579, *p* = 0.114
- **SNR**: *β* = 0.10, *SE* = 0.022, *z* = 4.463, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.67 | 0.28 | -2.35 | 0.019 | 0.142 | n.s. |
| a - c | 0.34 | 0.27 | 1.25 | 0.210 | 0.533 | n.s. |
| a - d | -0.02 | 0.27 | -0.09 | 0.928 | 0.928 | n.s. |
| a - e | -0.44 | 0.28 | -1.58 | 0.114 | 0.517 | n.s. |
| b - c | 1.00 | 0.27 | 3.65 | < .001 | 0.003 | ** |
| b - d | 0.64 | 0.28 | 2.28 | 0.023 | 0.149 | n.s. |
| b - e | 0.23 | 0.28 | 0.81 | 0.417 | 0.660 | n.s. |
| c - d | -0.36 | 0.26 | -1.36 | 0.173 | 0.533 | n.s. |
| c - e | -0.78 | 0.27 | -2.91 | 0.004 | 0.032 | * |
| d - e | -0.42 | 0.28 | -1.49 | 0.137 | 0.522 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.87, *p* < .001, η²_G = 0.048
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -2.69 | 15 | = 0.042 | -0.40 [-1.26, -0.08] | small | * |
| a vs c | 1.47 | 15 | = 0.232 | 0.18 [-0.18, 0.85] | negligible | n.s. |
| a vs d | -0.04 | 15 | = 0.972 | -0.00 [-0.47, 0.53] | negligible | n.s. |
| a vs e | -2.30 | 15 | = 0.060 | -0.33 [-1.15, -0.07] | small | n.s. |
| b vs c | 3.59 | 15 | = 0.026 | 0.57 [0.15, 1.31] | medium | * |
| b vs d | 3.24 | 15 | = 0.026 | 0.38 [0.15, 1.31] | small | * |
| b vs e | 0.53 | 15 | = 0.671 | 0.09 [-0.40, 0.67] | negligible | n.s. |
| c vs d | -1.34 | 15 | = 0.249 | -0.17 [-0.68, 0.29] | negligible | n.s. |
| c vs e | -3.07 | 15 | = 0.026 | -0.51 [-1.34, -0.24] | medium | * |
| d vs e | -2.32 | 15 | = 0.060 | -0.31 [-1.17, -0.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.096)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - a showed smaller amplitude than b (*d* = -0.40)
  - b showed greater amplitude than c (*d* = 0.57)
  - b showed greater amplitude than d (*d* = 0.38)
  - c showed smaller amplitude than e (*d* = -0.51)

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
