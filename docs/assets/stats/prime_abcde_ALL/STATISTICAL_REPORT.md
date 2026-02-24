# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:33:09

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
| a | 24 | 102.83 ms | 10.65 | 2.17 | [88.00, 120.00] |
| b | 24 | 105.67 ms | 10.81 | 2.21 | [88.00, 120.00] |
| c | 24 | 107.00 ms | 8.28 | 1.69 | [88.00, 120.00] |
| d | 24 | 105.33 ms | 10.92 | 2.23 | [88.00, 120.00] |
| e | 24 | 103.83 ms | 10.58 | 2.16 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | -1.73 µV | 1.47 | 0.30 | [-6.16, 0.87] |
| b | 24 | -1.94 µV | 1.40 | 0.29 | [-5.02, 0.94] |
| c | 24 | -2.00 µV | 1.46 | 0.30 | [-5.31, 0.39] |
| d | 24 | -1.51 µV | 1.32 | 0.27 | [-3.97, 1.39] |
| e | 24 | -1.69 µV | 1.22 | 0.25 | [-4.38, 0.42] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 177.50 ms | 17.53 | 3.58 | [148.00, 208.00] |
| b | 24 | 173.00 ms | 15.12 | 3.09 | [148.00, 204.00] |
| c | 24 | 174.67 ms | 16.71 | 3.41 | [140.00, 208.00] |
| d | 24 | 174.83 ms | 17.98 | 3.67 | [140.00, 204.00] |
| e | 24 | 175.83 ms | 16.78 | 3.43 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | -4.59 µV | 1.99 | 0.41 | [-9.33, -1.14] |
| b | 24 | -4.59 µV | 2.16 | 0.44 | [-9.17, -0.64] |
| c | 24 | -4.15 µV | 2.06 | 0.42 | [-9.00, -0.76] |
| d | 24 | -4.51 µV | 1.76 | 0.36 | [-9.14, -2.34] |
| e | 24 | -5.11 µV | 2.10 | 0.43 | [-9.79, -1.49] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 102.50 ms | 12.42 | 2.53 | [88.00, 120.00] |
| b | 24 | 108.33 ms | 12.70 | 2.59 | [88.00, 120.00] |
| c | 24 | 108.83 ms | 10.28 | 2.10 | [88.00, 120.00] |
| d | 24 | 107.17 ms | 12.03 | 2.46 | [88.00, 120.00] |
| e | 24 | 103.83 ms | 13.16 | 2.69 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 1.84 µV | 1.73 | 0.35 | [-0.64, 6.18] |
| b | 24 | 1.85 µV | 1.93 | 0.39 | [-1.14, 6.46] |
| c | 24 | 2.15 µV | 1.77 | 0.36 | [-0.46, 6.64] |
| d | 24 | 1.54 µV | 1.68 | 0.34 | [-1.56, 5.48] |
| e | 24 | 1.77 µV | 1.52 | 0.31 | [-0.56, 5.07] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 467.33 ms | 10.72 | 2.19 | [452.00, 484.00] |
| b | 24 | 462.00 ms | 11.00 | 2.25 | [452.00, 484.00] |
| c | 24 | 466.67 ms | 12.85 | 2.62 | [452.00, 484.00] |
| d | 24 | 471.50 ms | 10.70 | 2.18 | [452.00, 484.00] |
| e | 24 | 465.17 ms | 11.65 | 2.38 | [452.00, 484.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 2.35 µV | 1.95 | 0.40 | [-0.79, 5.32] |
| b | 24 | 2.72 µV | 2.25 | 0.46 | [-0.83, 6.76] |
| c | 24 | 2.51 µV | 1.73 | 0.35 | [-0.63, 6.30] |
| d | 24 | 2.33 µV | 1.80 | 0.37 | [-0.71, 5.40] |
| e | 24 | 2.70 µV | 2.02 | 0.41 | [-0.38, 6.21] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 865.25, BIC = 887.55
- **b vs a**: *β* = 2.96, *SE* = 2.006, *z* = 1.476, *p* = 0.140
- **c vs a**: *β* = 4.33, *SE* = 2.022, *z* = 2.142, *p* = 0.032
- **d vs a**: *β* = 2.50, *SE* = 1.982, *z* = 1.262, *p* = 0.207
- **e vs a**: *β* = 0.91, *SE* = 1.994, *z* = 0.456, *p* = 0.648
- **SNR**: *β* = -0.16, *SE* = 0.395, *z* = -0.412, *p* = 0.680

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -2.96 | 2.01 | -1.48 | 0.140 | 0.700 | n.s. |
| a - c | -4.33 | 2.02 | -2.14 | 0.032 | 0.279 | n.s. |
| a - d | -2.50 | 1.98 | -1.26 | 0.207 | 0.803 | n.s. |
| a - e | -0.91 | 1.99 | -0.46 | 0.648 | 0.899 | n.s. |
| b - c | -1.37 | 1.98 | -0.69 | 0.489 | 0.899 | n.s. |
| b - d | 0.46 | 2.01 | 0.23 | 0.819 | 0.899 | n.s. |
| b - e | 2.05 | 2.05 | 1.00 | 0.317 | 0.899 | n.s. |
| c - d | 1.83 | 2.02 | 0.91 | 0.365 | 0.899 | n.s. |
| c - e | 3.42 | 2.08 | 1.65 | 0.099 | 0.610 | n.s. |
| d - e | 1.59 | 1.99 | 0.80 | 0.425 | 0.899 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.283, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -1.22 | 23 | = 0.595 | -0.26 [-0.68, 0.18] | small | n.s. |
| a vs c | -1.84 | 23 | = 0.595 | -0.44 [-0.81, 0.06] | small | n.s. |
| a vs d | -1.18 | 23 | = 0.595 | -0.23 [-0.67, 0.19] | small | n.s. |
| a vs e | -0.58 | 23 | = 0.647 | -0.09 [-0.54, 0.31] | negligible | n.s. |
| b vs c | -0.56 | 23 | = 0.647 | -0.14 [-0.54, 0.31] | negligible | n.s. |
| b vs d | 0.22 | 23 | = 0.831 | 0.03 [-0.38, 0.47] | negligible | n.s. |
| b vs e | 1.07 | 23 | = 0.595 | 0.17 [-0.21, 0.64] | negligible | n.s. |
| c vs d | 0.83 | 23 | = 0.607 | 0.17 [-0.26, 0.59] | negligible | n.s. |
| c vs e | 1.44 | 23 | = 0.595 | 0.33 [-0.14, 0.73] | small | n.s. |
| d vs e | 0.81 | 23 | = 0.607 | 0.14 [-0.26, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 308.30, BIC = 330.60
- **b vs a**: *β* = -0.01, *SE* = 0.188, *z* = -0.044, *p* = 0.965
- **c vs a**: *β* = -0.01, *SE* = 0.190, *z* = -0.069, *p* = 0.945
- **d vs a**: *β* = 0.23, *SE* = 0.186, *z* = 1.221, *p* = 0.222
- **e vs a**: *β* = -0.10, *SE* = 0.187, *z* = -0.536, *p* = 0.592
- **SNR**: *β* = -0.25, *SE* = 0.038, *z* = -6.651, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.01 | 0.19 | 0.04 | 0.965 | 1.000 | n.s. |
| a - c | 0.01 | 0.19 | 0.07 | 0.945 | 1.000 | n.s. |
| a - d | -0.23 | 0.19 | -1.22 | 0.222 | 0.874 | n.s. |
| a - e | 0.10 | 0.19 | 0.54 | 0.592 | 0.995 | n.s. |
| b - c | 0.00 | 0.19 | 0.03 | 0.979 | 1.000 | n.s. |
| b - d | -0.24 | 0.19 | -1.25 | 0.211 | 0.874 | n.s. |
| b - e | 0.09 | 0.19 | 0.48 | 0.633 | 0.995 | n.s. |
| c - d | -0.24 | 0.19 | -1.27 | 0.206 | 0.874 | n.s. |
| c - e | 0.09 | 0.20 | 0.45 | 0.655 | 0.995 | n.s. |
| d - e | 0.33 | 0.19 | 1.75 | 0.080 | 0.566 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.63, *p* = 0.175, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.88 | 23 | = 0.485 | 0.14 [-0.25, 0.61] | negligible | n.s. |
| a vs c | 0.97 | 23 | = 0.485 | 0.18 [-0.23, 0.62] | negligible | n.s. |
| a vs d | -0.94 | 23 | = 0.485 | -0.16 [-0.62, 0.23] | negligible | n.s. |
| a vs e | -0.15 | 23 | = 0.881 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| b vs c | 0.37 | 23 | = 0.791 | 0.04 [-0.35, 0.50] | negligible | n.s. |
| b vs d | -2.41 | 23 | = 0.138 | -0.32 [-0.94, -0.04] | small | n.s. |
| b vs e | -1.05 | 23 | = 0.485 | -0.19 [-0.64, 0.21] | negligible | n.s. |
| c vs d | -2.35 | 23 | = 0.138 | -0.36 [-0.93, -0.03] | small | n.s. |
| c vs e | -1.56 | 23 | = 0.441 | -0.23 [-0.75, 0.11] | small | n.s. |
| d vs e | 1.03 | 23 | = 0.485 | 0.15 [-0.22, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 917.29, BIC = 939.59
- **b vs a**: *β* = -4.23, *SE* = 2.250, *z* = -1.879, *p* = 0.060
- **c vs a**: *β* = -3.07, *SE* = 2.247, *z* = -1.368, *p* = 0.171
- **d vs a**: *β* = -2.58, *SE* = 2.240, *z* = -1.151, *p* = 0.250
- **e vs a**: *β* = -1.03, *SE* = 2.297, *z* = -0.449, *p* = 0.653
- **SNR**: *β* = -0.22, *SE* = 0.176, *z* = -1.242, *p* = 0.214

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 4.23 | 2.25 | 1.88 | 0.060 | 0.463 | n.s. |
| a - c | 3.07 | 2.25 | 1.37 | 0.171 | 0.785 | n.s. |
| a - d | 2.58 | 2.24 | 1.15 | 0.250 | 0.866 | n.s. |
| a - e | 1.03 | 2.30 | 0.45 | 0.653 | 0.955 | n.s. |
| b - c | -1.15 | 2.28 | -0.51 | 0.612 | 0.955 | n.s. |
| b - d | -1.65 | 2.24 | -0.74 | 0.462 | 0.955 | n.s. |
| b - e | -3.20 | 2.26 | -1.42 | 0.157 | 0.785 | n.s. |
| c - d | -0.50 | 2.25 | -0.22 | 0.826 | 0.955 | n.s. |
| c - e | -2.04 | 2.35 | -0.87 | 0.384 | 0.945 | n.s. |
| d - e | -1.55 | 2.28 | -0.68 | 0.498 | 0.955 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.391, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.375 (ε = 0.666)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 2.78 | 23 | = 0.107 | 0.27 [0.11, 1.02] | small | n.s. |
| a vs c | 1.66 | 23 | = 0.556 | 0.17 [-0.10, 0.77] | negligible | n.s. |
| a vs d | 0.96 | 23 | = 0.594 | 0.15 [-0.23, 0.62] | negligible | n.s. |
| a vs e | 0.89 | 23 | = 0.594 | 0.10 [-0.24, 0.61] | negligible | n.s. |
| b vs c | -0.79 | 23 | = 0.594 | -0.10 [-0.59, 0.26] | negligible | n.s. |
| b vs d | -0.75 | 23 | = 0.594 | -0.11 [-0.58, 0.27] | negligible | n.s. |
| b vs e | -1.20 | 23 | = 0.594 | -0.18 [-0.67, 0.18] | negligible | n.s. |
| c vs d | -0.06 | 23 | = 0.956 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| c vs e | -0.73 | 23 | = 0.594 | -0.07 [-0.57, 0.28] | negligible | n.s. |
| d vs e | -0.35 | 23 | = 0.810 | -0.06 [-0.49, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 372.43, BIC = 394.73
- **b vs a**: *β* = 0.09, *SE* = 0.229, *z* = 0.381, *p* = 0.703
- **c vs a**: *β* = 0.36, *SE* = 0.228, *z* = 1.583, *p* = 0.113
- **d vs a**: *β* = 0.11, *SE* = 0.228, *z* = 0.484, *p* = 0.628
- **e vs a**: *β* = -0.32, *SE* = 0.234, *z* = -1.374, *p* = 0.169
- **SNR**: *β* = -0.07, *SE* = 0.018, *z* = -3.747, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.09 | 0.23 | -0.38 | 0.703 | 0.949 | n.s. |
| a - c | -0.36 | 0.23 | -1.58 | 0.113 | 0.570 | n.s. |
| a - d | -0.11 | 0.23 | -0.48 | 0.628 | 0.949 | n.s. |
| a - e | 0.32 | 0.23 | 1.37 | 0.169 | 0.671 | n.s. |
| b - c | -0.27 | 0.23 | -1.19 | 0.236 | 0.740 | n.s. |
| b - d | -0.02 | 0.23 | -0.10 | 0.919 | 0.949 | n.s. |
| b - e | 0.41 | 0.23 | 1.78 | 0.075 | 0.465 | n.s. |
| c - d | 0.25 | 0.23 | 1.10 | 0.273 | 0.740 | n.s. |
| c - e | 0.68 | 0.24 | 2.85 | 0.004 | 0.042 | * |
| d - e | 0.43 | 0.23 | 1.86 | 0.063 | 0.444 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.03, *p* = 0.005, η²_G = 0.024
- Greenhouse-Geisser corrected: *p* = 0.014 (ε = 0.672)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.01 | 23 | = 0.996 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| a vs c | -2.15 | 23 | = 0.109 | -0.22 [-0.88, 0.00] | small | n.s. |
| a vs d | -0.48 | 23 | = 0.790 | -0.04 [-0.52, 0.32] | negligible | n.s. |
| a vs e | 2.05 | 23 | = 0.109 | 0.26 [-0.02, 0.86] | small | n.s. |
| b vs c | -2.14 | 23 | = 0.109 | -0.21 [-0.88, 0.01] | small | n.s. |
| b vs d | -0.38 | 23 | = 0.790 | -0.04 [-0.50, 0.35] | negligible | n.s. |
| b vs e | 1.86 | 23 | = 0.126 | 0.25 [-0.06, 0.82] | small | n.s. |
| c vs d | 1.55 | 23 | = 0.192 | 0.19 [-0.12, 0.75] | negligible | n.s. |
| c vs e | 2.81 | 23 | = 0.100 | 0.46 [0.12, 1.03] | small | n.s. |
| d vs e | 2.03 | 23 | = 0.109 | 0.31 [-0.03, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 897.44, BIC = 919.74
- **b vs a**: *β* = 5.90, *SE* = 2.269, *z* = 2.600, *p* = 0.009
- **c vs a**: *β* = 6.43, *SE* = 2.302, *z* = 2.792, *p* = 0.005
- **d vs a**: *β* = 4.70, *SE* = 2.247, *z* = 2.093, *p* = 0.036
- **e vs a**: *β* = 1.38, *SE* = 2.252, *z* = 0.612, *p* = 0.541
- **SNR**: *β* = -0.06, *SE* = 0.313, *z* = -0.175, *p* = 0.861

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -5.90 | 2.27 | -2.60 | 0.009 | 0.081 | n.s. |
| a - c | -6.43 | 2.30 | -2.79 | 0.005 | 0.051 | n.s. |
| a - d | -4.70 | 2.25 | -2.09 | 0.036 | 0.228 | n.s. |
| a - e | -1.38 | 2.25 | -0.61 | 0.541 | 0.906 | n.s. |
| b - c | -0.53 | 2.24 | -0.24 | 0.814 | 0.906 | n.s. |
| b - d | 1.20 | 2.24 | 0.53 | 0.594 | 0.906 | n.s. |
| b - e | 4.52 | 2.24 | 2.02 | 0.044 | 0.235 | n.s. |
| c - d | 1.72 | 2.26 | 0.76 | 0.446 | 0.906 | n.s. |
| c - e | 5.05 | 2.26 | 2.24 | 0.025 | 0.184 | n.s. |
| d - e | 3.33 | 2.24 | 1.49 | 0.137 | 0.522 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.03, *p* = 0.022, η²_G = 0.043
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -2.42 | 23 | = 0.087 | -0.46 [-0.94, -0.05] | small | n.s. |
| a vs c | -2.45 | 23 | = 0.087 | -0.56 [-0.95, -0.05] | medium | n.s. |
| a vs d | -2.02 | 23 | = 0.137 | -0.38 [-0.85, 0.03] | small | n.s. |
| a vs e | -0.65 | 23 | = 0.649 | -0.10 [-0.56, 0.29] | negligible | n.s. |
| b vs c | -0.22 | 23 | = 0.831 | -0.04 [-0.47, 0.38] | negligible | n.s. |
| b vs d | 0.44 | 23 | = 0.740 | 0.09 [-0.33, 0.51] | negligible | n.s. |
| b vs e | 1.68 | 23 | = 0.179 | 0.35 [-0.09, 0.78] | small | n.s. |
| c vs d | 1.04 | 23 | = 0.439 | 0.15 [-0.21, 0.64] | negligible | n.s. |
| c vs e | 2.38 | 23 | = 0.087 | 0.42 [0.04, 0.93] | small | n.s. |
| d vs e | 1.71 | 23 | = 0.179 | 0.26 [-0.09, 0.78] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 326.36, BIC = 348.66
- **b vs a**: *β* = -0.10, *SE* = 0.187, *z* = -0.513, *p* = 0.608
- **c vs a**: *β* = 0.16, *SE* = 0.190, *z* = 0.829, *p* = 0.407
- **d vs a**: *β* = -0.36, *SE* = 0.185, *z* = -1.939, *p* = 0.052
- **e vs a**: *β* = -0.14, *SE* = 0.186, *z* = -0.775, *p* = 0.438
- **SNR**: *β* = 0.09, *SE* = 0.027, *z* = 3.312, *p* = 0.001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.10 | 0.19 | 0.51 | 0.608 | 0.877 | n.s. |
| a - c | -0.16 | 0.19 | -0.83 | 0.407 | 0.877 | n.s. |
| a - d | 0.36 | 0.19 | 1.94 | 0.052 | 0.384 | n.s. |
| a - e | 0.14 | 0.19 | 0.77 | 0.438 | 0.877 | n.s. |
| b - c | -0.25 | 0.18 | -1.37 | 0.170 | 0.691 | n.s. |
| b - d | 0.26 | 0.18 | 1.42 | 0.155 | 0.691 | n.s. |
| b - e | 0.05 | 0.18 | 0.26 | 0.796 | 0.877 | n.s. |
| c - d | 0.52 | 0.19 | 2.77 | 0.006 | 0.055 | n.s. |
| c - e | 0.30 | 0.19 | 1.62 | 0.105 | 0.588 | n.s. |
| d - e | -0.22 | 0.18 | -1.17 | 0.243 | 0.751 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.55, *p* = 0.045, η²_G = 0.013
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.07 | 23 | = 0.944 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| a vs c | -1.63 | 23 | = 0.254 | -0.18 [-0.77, 0.10] | negligible | n.s. |
| a vs d | 1.57 | 23 | = 0.254 | 0.17 [-0.11, 0.75] | negligible | n.s. |
| a vs e | 0.37 | 23 | = 0.803 | 0.04 [-0.35, 0.50] | negligible | n.s. |
| b vs c | -1.54 | 23 | = 0.254 | -0.16 [-0.75, 0.12] | negligible | n.s. |
| b vs d | 1.48 | 23 | = 0.254 | 0.17 [-0.13, 0.73] | negligible | n.s. |
| b vs e | 0.36 | 23 | = 0.803 | 0.05 [-0.35, 0.50] | negligible | n.s. |
| c vs d | 3.86 | 23 | = 0.008 | 0.36 [0.30, 1.27] | small | ** |
| c vs e | 2.02 | 23 | = 0.254 | 0.23 [-0.03, 0.85] | small | n.s. |
| d vs e | -1.26 | 23 | = 0.314 | -0.14 [-0.69, 0.17] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 919.11, BIC = 941.41
- **b vs a**: *β* = -5.40, *SE* = 2.679, *z* = -2.015, *p* = 0.044
- **c vs a**: *β* = -0.67, *SE* = 2.674, *z* = -0.251, *p* = 0.802
- **d vs a**: *β* = 4.08, *SE* = 2.683, *z* = 1.521, *p* = 0.128
- **e vs a**: *β* = -2.20, *SE* = 2.675, *z* = -0.821, *p* = 0.412
- **SNR**: *β* = 0.07, *SE* = 0.180, *z* = 0.379, *p* = 0.705

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 5.40 | 2.68 | 2.01 | 0.044 | 0.302 | n.s. |
| a - c | 0.67 | 2.67 | 0.25 | 0.802 | 0.814 | n.s. |
| a - d | -4.08 | 2.68 | -1.52 | 0.128 | 0.497 | n.s. |
| a - e | 2.20 | 2.67 | 0.82 | 0.412 | 0.796 | n.s. |
| b - c | -4.73 | 2.68 | -1.76 | 0.078 | 0.427 | n.s. |
| b - d | -9.48 | 2.67 | -3.54 | < .001 | 0.004 | ** |
| b - e | -3.20 | 2.68 | -1.20 | 0.231 | 0.651 | n.s. |
| c - d | -4.75 | 2.68 | -1.77 | 0.076 | 0.427 | n.s. |
| c - e | 1.53 | 2.67 | 0.57 | 0.569 | 0.814 | n.s. |
| d - e | 6.28 | 2.68 | 2.34 | 0.019 | 0.159 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.20, *p* = 0.017, η²_G = 0.071
- Greenhouse-Geisser corrected: *p* = 0.031 (ε = 0.714)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 1.87 | 23 | = 0.167 | 0.49 [-0.05, 0.82] | small | n.s. |
| a vs c | 0.19 | 23 | = 0.852 | 0.06 [-0.38, 0.46] | negligible | n.s. |
| a vs d | -1.81 | 23 | = 0.167 | -0.39 [-0.81, 0.07] | small | n.s. |
| a vs e | 0.86 | 23 | = 0.500 | 0.19 [-0.25, 0.60] | negligible | n.s. |
| b vs c | -1.47 | 23 | = 0.223 | -0.39 [-0.73, 0.13] | small | n.s. |
| b vs d | -3.40 | 23 | = 0.025 | -0.88 [-1.16, -0.22] | large | * |
| b vs e | -1.47 | 23 | = 0.223 | -0.28 [-0.73, 0.13] | small | n.s. |
| c vs d | -2.29 | 23 | = 0.106 | -0.41 [-0.91, -0.02] | small | n.s. |
| c vs e | 0.47 | 23 | = 0.717 | 0.12 [-0.33, 0.52] | negligible | n.s. |
| d vs e | 2.85 | 23 | = 0.045 | 0.57 [0.13, 1.04] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 345.75, BIC = 368.05
- **b vs a**: *β* = 0.29, *SE* = 0.202, *z* = 1.419, *p* = 0.156
- **c vs a**: *β* = 0.15, *SE* = 0.202, *z* = 0.745, *p* = 0.456
- **d vs a**: *β* = -0.12, *SE* = 0.203, *z* = -0.608, *p* = 0.543
- **e vs a**: *β* = 0.31, *SE* = 0.202, *z* = 1.538, *p* = 0.124
- **SNR**: *β* = 0.09, *SE* = 0.016, *z* = 5.363, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.29 | 0.20 | -1.42 | 0.156 | 0.695 | n.s. |
| a - c | -0.15 | 0.20 | -0.74 | 0.456 | 0.938 | n.s. |
| a - d | 0.12 | 0.20 | 0.61 | 0.543 | 0.938 | n.s. |
| a - e | -0.31 | 0.20 | -1.54 | 0.124 | 0.653 | n.s. |
| b - c | 0.14 | 0.20 | 0.68 | 0.499 | 0.938 | n.s. |
| b - d | 0.41 | 0.20 | 2.03 | 0.042 | 0.321 | n.s. |
| b - e | -0.02 | 0.20 | -0.12 | 0.907 | 0.938 | n.s. |
| c - d | 0.27 | 0.20 | 1.35 | 0.177 | 0.695 | n.s. |
| c - e | -0.16 | 0.20 | -0.79 | 0.427 | 0.938 | n.s. |
| d - e | -0.43 | 0.20 | -2.15 | 0.032 | 0.277 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.30, *p* = 0.275, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -1.70 | 23 | = 0.414 | -0.17 [-0.78, 0.09] | negligible | n.s. |
| a vs c | -1.02 | 23 | = 0.571 | -0.08 [-0.63, 0.22] | negligible | n.s. |
| a vs d | 0.06 | 23 | = 0.949 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| a vs e | -1.94 | 23 | = 0.414 | -0.18 [-0.83, 0.04] | negligible | n.s. |
| b vs c | 0.86 | 23 | = 0.571 | 0.11 [-0.25, 0.60] | negligible | n.s. |
| b vs d | 1.60 | 23 | = 0.414 | 0.19 [-0.11, 0.76] | negligible | n.s. |
| b vs e | 0.08 | 23 | = 0.949 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| c vs d | 0.70 | 23 | = 0.617 | 0.10 [-0.28, 0.57] | negligible | n.s. |
| c vs e | -0.95 | 23 | = 0.571 | -0.10 [-0.62, 0.23] | negligible | n.s. |
| d vs e | -1.32 | 23 | = 0.501 | -0.19 [-0.70, 0.16] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.005) (no significant pairwise comparisons)
**P1 latency:** Significant main effect of condition (*p* = 0.022) (no significant pairwise comparisons)
**P1 amplitude:** Significant main effect of condition (*p* = 0.045). Post-hoc tests revealed:
  - c showed greater amplitude than d (*d* = 0.36)
**P3b latency:** Significant main effect of condition (*p* = 0.017). Post-hoc tests revealed:
  - b showed smaller latency than d (*d* = -0.88)
  - d showed greater latency than e (*d* = 0.57)

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
