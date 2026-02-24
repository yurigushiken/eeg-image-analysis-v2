# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:32:44

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
| a | 24 | 103.67 ms | 10.28 | 2.10 | [88.00, 120.00] |
| b | 24 | 106.00 ms | 11.25 | 2.30 | [88.00, 120.00] |
| c | 24 | 105.83 ms | 9.43 | 1.93 | [88.00, 120.00] |
| d | 24 | 107.17 ms | 10.74 | 2.19 | [88.00, 120.00] |
| e | 24 | 104.17 ms | 11.76 | 2.40 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | -1.95 µV | 1.58 | 0.32 | [-7.18, 0.32] |
| b | 24 | -2.01 µV | 1.38 | 0.28 | [-4.86, 0.79] |
| c | 24 | -2.16 µV | 1.50 | 0.31 | [-5.30, 0.39] |
| d | 24 | -1.59 µV | 1.29 | 0.26 | [-3.97, 1.14] |
| e | 24 | -1.92 µV | 1.20 | 0.25 | [-4.38, 0.48] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 176.00 ms | 17.46 | 3.56 | [152.00, 212.00] |
| b | 24 | 174.67 ms | 14.81 | 3.02 | [148.00, 204.00] |
| c | 24 | 174.50 ms | 17.00 | 3.47 | [140.00, 212.00] |
| d | 24 | 174.50 ms | 17.84 | 3.64 | [144.00, 204.00] |
| e | 24 | 176.00 ms | 16.34 | 3.34 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | -4.80 µV | 2.03 | 0.41 | [-9.95, -1.34] |
| b | 24 | -4.67 µV | 2.20 | 0.45 | [-9.46, -0.65] |
| c | 24 | -4.41 µV | 2.10 | 0.43 | [-8.73, -0.70] |
| d | 24 | -4.56 µV | 1.72 | 0.35 | [-8.75, -1.50] |
| e | 24 | -5.17 µV | 2.19 | 0.45 | [-9.92, -0.83] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 102.17 ms | 12.54 | 2.56 | [88.00, 120.00] |
| b | 24 | 110.00 ms | 11.38 | 2.32 | [88.00, 120.00] |
| c | 24 | 106.67 ms | 11.17 | 2.28 | [88.00, 120.00] |
| d | 24 | 106.67 ms | 12.69 | 2.59 | [88.00, 120.00] |
| e | 24 | 104.00 ms | 13.29 | 2.71 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 2.05 µV | 1.78 | 0.36 | [-0.52, 6.98] |
| b | 24 | 1.93 µV | 1.92 | 0.39 | [-0.70, 6.43] |
| c | 24 | 2.22 µV | 1.82 | 0.37 | [-0.63, 7.04] |
| d | 24 | 1.60 µV | 1.68 | 0.34 | [-1.36, 5.56] |
| e | 24 | 1.87 µV | 1.63 | 0.33 | [-0.69, 5.49] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 470.33 ms | 11.43 | 2.33 | [452.00, 484.00] |
| b | 24 | 462.33 ms | 10.81 | 2.21 | [452.00, 484.00] |
| c | 24 | 469.00 ms | 10.83 | 2.21 | [452.00, 484.00] |
| d | 24 | 473.17 ms | 11.03 | 2.25 | [452.00, 484.00] |
| e | 24 | 467.50 ms | 12.94 | 2.64 | [452.00, 484.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 2.73 µV | 2.09 | 0.43 | [-0.71, 6.13] |
| b | 24 | 3.06 µV | 2.21 | 0.45 | [-0.30, 7.23] |
| c | 24 | 2.86 µV | 1.76 | 0.36 | [-0.02, 6.81] |
| d | 24 | 2.75 µV | 1.92 | 0.39 | [-0.79, 6.43] |
| e | 24 | 2.85 µV | 2.11 | 0.43 | [-0.11, 6.72] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 888.42, BIC = 910.72
- **b vs a**: *β* = 2.32, *SE* = 2.275, *z* = 1.020, *p* = 0.308
- **c vs a**: *β* = 2.17, *SE* = 2.275, *z* = 0.956, *p* = 0.339
- **d vs a**: *β* = 3.76, *SE* = 2.285, *z* = 1.647, *p* = 0.100
- **e vs a**: *β* = 0.95, *SE* = 2.304, *z* = 0.413, *p* = 0.679
- **SNR**: *β* = 0.49, *SE* = 0.397, *z* = 1.226, *p* = 0.220

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -2.32 | 2.27 | -1.02 | 0.308 | 0.947 | n.s. |
| a - c | -2.17 | 2.27 | -0.96 | 0.339 | 0.947 | n.s. |
| a - d | -3.76 | 2.28 | -1.65 | 0.100 | 0.650 | n.s. |
| a - e | -0.95 | 2.30 | -0.41 | 0.679 | 0.982 | n.s. |
| b - c | 0.15 | 2.27 | 0.06 | 0.949 | 0.982 | n.s. |
| b - d | -1.44 | 2.29 | -0.63 | 0.528 | 0.982 | n.s. |
| b - e | 1.37 | 2.31 | 0.59 | 0.553 | 0.982 | n.s. |
| c - d | -1.59 | 2.28 | -0.69 | 0.487 | 0.982 | n.s. |
| c - e | 1.22 | 2.30 | 0.53 | 0.596 | 0.982 | n.s. |
| d - e | 2.81 | 2.28 | 1.23 | 0.218 | 0.891 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.76, *p* = 0.554, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.89 | 23 | = 0.728 | -0.22 [-0.61, 0.24] | small | n.s. |
| a vs c | -0.90 | 23 | = 0.728 | -0.22 [-0.61, 0.24] | small | n.s. |
| a vs d | -1.73 | 23 | = 0.521 | -0.33 [-0.79, 0.08] | small | n.s. |
| a vs e | -0.23 | 23 | = 0.912 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| b vs c | 0.06 | 23 | = 0.953 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| b vs d | -0.43 | 23 | = 0.835 | -0.11 [-0.51, 0.33] | negligible | n.s. |
| b vs e | 0.87 | 23 | = 0.728 | 0.16 [-0.25, 0.60] | negligible | n.s. |
| c vs d | -0.69 | 23 | = 0.728 | -0.13 [-0.57, 0.28] | negligible | n.s. |
| c vs e | 0.67 | 23 | = 0.728 | 0.16 [-0.29, 0.56] | negligible | n.s. |
| d vs e | 1.69 | 23 | = 0.521 | 0.27 [-0.09, 0.78] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 327.09, BIC = 349.39
- **b vs a**: *β* = -0.05, *SE* = 0.205, *z* = -0.251, *p* = 0.802
- **c vs a**: *β* = -0.21, *SE* = 0.205, *z* = -1.024, *p* = 0.306
- **d vs a**: *β* = 0.23, *SE* = 0.206, *z* = 1.119, *p* = 0.263
- **e vs a**: *β* = -0.19, *SE* = 0.208, *z* = -0.895, *p* = 0.371
- **SNR**: *β* = -0.24, *SE* = 0.038, *z* = -6.311, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.05 | 0.21 | 0.25 | 0.802 | 0.961 | n.s. |
| a - c | 0.21 | 0.21 | 1.02 | 0.306 | 0.888 | n.s. |
| a - d | -0.23 | 0.21 | -1.12 | 0.263 | 0.882 | n.s. |
| a - e | 0.19 | 0.21 | 0.90 | 0.371 | 0.901 | n.s. |
| b - c | 0.16 | 0.21 | 0.77 | 0.439 | 0.901 | n.s. |
| b - d | -0.28 | 0.21 | -1.37 | 0.171 | 0.778 | n.s. |
| b - e | 0.14 | 0.21 | 0.65 | 0.517 | 0.901 | n.s. |
| c - d | -0.44 | 0.21 | -2.14 | 0.032 | 0.281 | n.s. |
| c - e | -0.02 | 0.21 | -0.11 | 0.909 | 0.961 | n.s. |
| d - e | 0.42 | 0.21 | 2.03 | 0.043 | 0.325 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.208, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.25 | 23 | = 0.892 | 0.04 [-0.37, 0.47] | negligible | n.s. |
| a vs c | 0.74 | 23 | = 0.670 | 0.13 [-0.27, 0.58] | negligible | n.s. |
| a vs d | -1.39 | 23 | = 0.446 | -0.25 [-0.71, 0.15] | small | n.s. |
| a vs e | -0.12 | 23 | = 0.907 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| b vs c | 0.87 | 23 | = 0.659 | 0.10 [-0.25, 0.60] | negligible | n.s. |
| b vs d | -2.01 | 23 | = 0.281 | -0.31 [-0.85, 0.03] | small | n.s. |
| b vs e | -0.39 | 23 | = 0.872 | -0.07 [-0.50, 0.34] | negligible | n.s. |
| c vs d | -2.31 | 23 | = 0.281 | -0.40 [-0.92, -0.03] | small | n.s. |
| c vs e | -1.07 | 23 | = 0.590 | -0.18 [-0.65, 0.21] | negligible | n.s. |
| d vs e | 1.43 | 23 | = 0.446 | 0.26 [-0.14, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 917.13, BIC = 939.43
- **b vs a**: *β* = -1.43, *SE* = 2.238, *z* = -0.637, *p* = 0.524
- **c vs a**: *β* = -1.67, *SE* = 2.248, *z* = -0.741, *p* = 0.459
- **d vs a**: *β* = -1.46, *SE* = 2.234, *z* = -0.653, *p* = 0.514
- **e vs a**: *β* = 0.28, *SE* = 2.275, *z* = 0.122, *p* = 0.903
- **SNR**: *β* = -0.10, *SE* = 0.149, *z* = -0.641, *p* = 0.522

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 1.43 | 2.24 | 0.64 | 0.524 | 0.995 | n.s. |
| a - c | 1.67 | 2.25 | 0.74 | 0.459 | 0.995 | n.s. |
| a - d | 1.46 | 2.23 | 0.65 | 0.514 | 0.995 | n.s. |
| a - e | -0.28 | 2.28 | -0.12 | 0.903 | 1.000 | n.s. |
| b - c | 0.24 | 2.24 | 0.11 | 0.915 | 1.000 | n.s. |
| b - d | 0.03 | 2.24 | 0.01 | 0.988 | 1.000 | n.s. |
| b - e | -1.70 | 2.31 | -0.74 | 0.460 | 0.995 | n.s. |
| c - d | -0.21 | 2.26 | -0.09 | 0.927 | 1.000 | n.s. |
| c - e | -1.94 | 2.34 | -0.83 | 0.406 | 0.995 | n.s. |
| d - e | -1.74 | 2.26 | -0.77 | 0.443 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.24, *p* = 0.914, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.859 (ε = 0.720)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.73 | 23 | = 0.985 | 0.08 [-0.28, 0.57] | negligible | n.s. |
| a vs c | 0.63 | 23 | = 0.985 | 0.09 [-0.29, 0.55] | negligible | n.s. |
| a vs d | 0.66 | 23 | = 0.985 | 0.08 [-0.29, 0.56] | negligible | n.s. |
| a vs e | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| b vs c | 0.08 | 23 | = 1.000 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| b vs d | 0.07 | 23 | = 1.000 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| b vs e | -0.57 | 23 | = 0.985 | -0.09 [-0.54, 0.31] | negligible | n.s. |
| c vs d | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| c vs e | -0.94 | 23 | = 0.985 | -0.09 [-0.62, 0.23] | negligible | n.s. |
| d vs e | -0.54 | 23 | = 0.985 | -0.09 [-0.53, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 386.15, BIC = 408.45
- **b vs a**: *β* = 0.06, *SE* = 0.243, *z* = 0.239, *p* = 0.811
- **c vs a**: *β* = 0.26, *SE* = 0.245, *z* = 1.071, *p* = 0.284
- **d vs a**: *β* = 0.28, *SE* = 0.243, *z* = 1.131, *p* = 0.258
- **e vs a**: *β* = -0.14, *SE* = 0.248, *z* = -0.579, *p* = 0.562
- **SNR**: *β* = -0.07, *SE* = 0.016, *z* = -4.585, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.06 | 0.24 | -0.24 | 0.811 | 0.964 | n.s. |
| a - c | -0.26 | 0.24 | -1.07 | 0.284 | 0.908 | n.s. |
| a - d | -0.27 | 0.24 | -1.13 | 0.258 | 0.908 | n.s. |
| a - e | 0.14 | 0.25 | 0.58 | 0.562 | 0.940 | n.s. |
| b - c | -0.20 | 0.24 | -0.84 | 0.402 | 0.940 | n.s. |
| b - d | -0.22 | 0.24 | -0.89 | 0.375 | 0.940 | n.s. |
| b - e | 0.20 | 0.25 | 0.80 | 0.422 | 0.940 | n.s. |
| c - d | -0.01 | 0.25 | -0.05 | 0.958 | 0.964 | n.s. |
| c - e | 0.41 | 0.25 | 1.59 | 0.111 | 0.654 | n.s. |
| d - e | 0.42 | 0.25 | 1.70 | 0.089 | 0.608 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.29, *p* = 0.065, η²_G = 0.016
- Greenhouse-Geisser corrected: *p* = 0.089 (ε = 0.718)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.76 | 23 | = 0.572 | -0.06 [-0.58, 0.27] | negligible | n.s. |
| a vs c | -1.68 | 23 | = 0.267 | -0.19 [-0.78, 0.09] | negligible | n.s. |
| a vs d | -1.26 | 23 | = 0.402 | -0.13 [-0.69, 0.17] | negligible | n.s. |
| a vs e | 1.18 | 23 | = 0.402 | 0.17 [-0.19, 0.67] | negligible | n.s. |
| b vs c | -1.10 | 23 | = 0.402 | -0.12 [-0.65, 0.20] | negligible | n.s. |
| b vs d | -0.49 | 23 | = 0.631 | -0.06 [-0.52, 0.32] | negligible | n.s. |
| b vs e | 1.75 | 23 | = 0.267 | 0.22 [-0.08, 0.79] | small | n.s. |
| c vs d | 0.52 | 23 | = 0.631 | 0.08 [-0.32, 0.53] | negligible | n.s. |
| c vs e | 2.04 | 23 | = 0.267 | 0.35 [-0.02, 0.86] | small | n.s. |
| d vs e | 1.96 | 23 | = 0.267 | 0.31 [-0.04, 0.84] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 893.11, BIC = 915.41
- **b vs a**: *β* = 7.70, *SE* = 2.195, *z* = 3.509, *p* < .001
- **c vs a**: *β* = 4.23, *SE* = 2.227, *z* = 1.900, *p* = 0.057
- **d vs a**: *β* = 4.44, *SE* = 2.188, *z* = 2.028, *p* = 0.043
- **e vs a**: *β* = 1.63, *SE* = 2.210, *z* = 0.736, *p* = 0.462
- **SNR**: *β* = 0.23, *SE* = 0.359, *z* = 0.630, *p* = 0.529

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -7.70 | 2.19 | -3.51 | < .001 | 0.004 | ** |
| a - c | -4.23 | 2.23 | -1.90 | 0.057 | 0.339 | n.s. |
| a - d | -4.44 | 2.19 | -2.03 | 0.043 | 0.294 | n.s. |
| a - e | -1.63 | 2.21 | -0.74 | 0.462 | 0.710 | n.s. |
| b - c | 3.47 | 2.20 | 1.58 | 0.114 | 0.516 | n.s. |
| b - d | 3.27 | 2.19 | 1.49 | 0.135 | 0.517 | n.s. |
| b - e | 6.08 | 2.19 | 2.78 | 0.005 | 0.048 | * |
| c - d | -0.20 | 2.21 | -0.09 | 0.926 | 0.926 | n.s. |
| c - e | 2.60 | 2.19 | 1.19 | 0.234 | 0.592 | n.s. |
| d - e | 2.81 | 2.20 | 1.28 | 0.201 | 0.592 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.58, *p* = 0.009, η²_G = 0.047
- Greenhouse-Geisser corrected: *p* = 0.022 (ε = 0.679)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -2.87 | 23 | = 0.086 | -0.65 [-1.04, -0.13] | medium | n.s. |
| a vs c | -2.39 | 23 | = 0.112 | -0.38 [-0.93, -0.04] | small | n.s. |
| a vs d | -1.77 | 23 | = 0.179 | -0.36 [-0.80, 0.07] | small | n.s. |
| a vs e | -0.74 | 23 | = 0.521 | -0.14 [-0.57, 0.27] | negligible | n.s. |
| b vs c | 1.52 | 23 | = 0.227 | 0.30 [-0.12, 0.74] | small | n.s. |
| b vs d | 1.39 | 23 | = 0.227 | 0.28 [-0.15, 0.72] | small | n.s. |
| b vs e | 2.12 | 23 | = 0.112 | 0.49 [-0.01, 0.87] | small | n.s. |
| c vs d | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| c vs e | 1.38 | 23 | = 0.227 | 0.22 [-0.15, 0.71] | small | n.s. |
| d vs e | 2.23 | 23 | = 0.112 | 0.21 [0.01, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 343.59, BIC = 365.89
- **b vs a**: *β* = -0.20, *SE* = 0.202, *z* = -0.979, *p* = 0.328
- **c vs a**: *β* = 0.01, *SE* = 0.206, *z* = 0.059, *p* = 0.953
- **d vs a**: *β* = -0.49, *SE* = 0.202, *z* = -2.420, *p* = 0.016
- **e vs a**: *β* = -0.30, *SE* = 0.204, *z* = -1.489, *p* = 0.136
- **SNR**: *β* = 0.13, *SE* = 0.035, *z* = 3.703, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.20 | 0.20 | 0.98 | 0.328 | 0.831 | n.s. |
| a - c | -0.01 | 0.21 | -0.06 | 0.953 | 0.953 | n.s. |
| a - d | 0.49 | 0.20 | 2.42 | 0.016 | 0.133 | n.s. |
| a - e | 0.30 | 0.20 | 1.49 | 0.136 | 0.642 | n.s. |
| b - c | -0.21 | 0.20 | -1.04 | 0.299 | 0.831 | n.s. |
| b - d | 0.29 | 0.20 | 1.44 | 0.151 | 0.642 | n.s. |
| b - e | 0.11 | 0.20 | 0.52 | 0.601 | 0.841 | n.s. |
| c - d | 0.50 | 0.20 | 2.45 | 0.014 | 0.133 | n.s. |
| c - e | 0.32 | 0.20 | 1.57 | 0.117 | 0.632 | n.s. |
| d - e | -0.18 | 0.20 | -0.91 | 0.363 | 0.831 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.27, *p* = 0.067, η²_G = 0.014
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.70 | 23 | = 0.547 | 0.07 [-0.28, 0.57] | negligible | n.s. |
| a vs c | -0.79 | 23 | = 0.547 | -0.09 [-0.59, 0.26] | negligible | n.s. |
| a vs d | 2.18 | 23 | = 0.197 | 0.26 [0.00, 0.89] | small | n.s. |
| a vs e | 0.72 | 23 | = 0.547 | 0.11 [-0.28, 0.57] | negligible | n.s. |
| b vs c | -1.44 | 23 | = 0.328 | -0.15 [-0.72, 0.14] | negligible | n.s. |
| b vs d | 1.72 | 23 | = 0.328 | 0.18 [-0.08, 0.79] | negligible | n.s. |
| b vs e | 0.26 | 23 | = 0.800 | 0.03 [-0.37, 0.47] | negligible | n.s. |
| c vs d | 3.24 | 23 | = 0.036 | 0.35 [0.20, 1.13] | small | * |
| c vs e | 1.48 | 23 | = 0.328 | 0.20 [-0.13, 0.73] | small | n.s. |
| d vs e | -1.21 | 23 | = 0.397 | -0.16 [-0.68, 0.18] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 901.04, BIC = 923.34
- **b vs a**: *β* = -8.03, *SE* = 2.362, *z* = -3.399, *p* = 0.001
- **c vs a**: *β* = -1.33, *SE* = 2.358, *z* = -0.565, *p* = 0.572
- **d vs a**: *β* = 2.80, *SE* = 2.363, *z* = 1.186, *p* = 0.236
- **e vs a**: *β* = -2.85, *SE* = 2.360, *z* = -1.209, *p* = 0.227
- **SNR**: *β* = 0.04, *SE* = 0.208, *z* = 0.212, *p* = 0.832

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 8.03 | 2.36 | 3.40 | < .001 | 0.006 | ** |
| a - c | 1.33 | 2.36 | 0.56 | 0.572 | 0.769 | n.s. |
| a - d | -2.80 | 2.36 | -1.19 | 0.236 | 0.642 | n.s. |
| a - e | 2.85 | 2.36 | 1.21 | 0.227 | 0.642 | n.s. |
| b - c | -6.70 | 2.36 | -2.83 | 0.005 | 0.036 | * |
| b - d | -10.83 | 2.36 | -4.59 | < .001 | < .001 | *** |
| b - e | -5.18 | 2.36 | -2.19 | 0.028 | 0.158 | n.s. |
| c - d | -4.13 | 2.36 | -1.75 | 0.080 | 0.342 | n.s. |
| c - e | 1.52 | 2.36 | 0.64 | 0.519 | 0.769 | n.s. |
| d - e | 5.66 | 2.36 | 2.40 | 0.016 | 0.110 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.55, *p* < .001, η²_G = 0.093
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 2.86 | 23 | = 0.029 | 0.72 [0.13, 1.04] | medium | * |
| a vs c | 0.53 | 23 | = 0.600 | 0.12 [-0.32, 0.53] | negligible | n.s. |
| a vs d | -1.21 | 23 | = 0.327 | -0.25 [-0.68, 0.18] | small | n.s. |
| a vs e | 1.15 | 23 | = 0.327 | 0.23 [-0.19, 0.66] | small | n.s. |
| b vs c | -2.75 | 23 | = 0.029 | -0.62 [-1.01, -0.11] | medium | * |
| b vs d | -4.65 | 23 | = 0.001 | -0.99 [-1.46, -0.44] | large | ** |
| b vs e | -2.06 | 23 | = 0.085 | -0.43 [-0.86, 0.02] | small | n.s. |
| c vs d | -2.16 | 23 | = 0.084 | -0.38 [-0.88, 0.00] | small | n.s. |
| c vs e | 0.58 | 23 | = 0.600 | 0.13 [-0.31, 0.54] | negligible | n.s. |
| d vs e | 2.74 | 23 | = 0.029 | 0.47 [0.10, 1.01] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 321.97, BIC = 344.27
- **b vs a**: *β* = 0.23, *SE* = 0.183, *z* = 1.265, *p* = 0.206
- **c vs a**: *β* = 0.14, *SE* = 0.182, *z* = 0.760, *p* = 0.447
- **d vs a**: *β* = -0.09, *SE* = 0.183, *z* = -0.483, *p* = 0.629
- **e vs a**: *β* = 0.05, *SE* = 0.182, *z* = 0.280, *p* = 0.779
- **SNR**: *β* = 0.15, *SE* = 0.018, *z* = 8.365, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.23 | 0.18 | -1.27 | 0.206 | 0.874 | n.s. |
| a - c | -0.14 | 0.18 | -0.76 | 0.447 | 0.971 | n.s. |
| a - d | 0.09 | 0.18 | 0.48 | 0.629 | 0.977 | n.s. |
| a - e | -0.05 | 0.18 | -0.28 | 0.779 | 0.977 | n.s. |
| b - c | 0.09 | 0.18 | 0.51 | 0.612 | 0.977 | n.s. |
| b - d | 0.32 | 0.18 | 1.75 | 0.080 | 0.564 | n.s. |
| b - e | 0.18 | 0.18 | 0.99 | 0.323 | 0.935 | n.s. |
| c - d | 0.23 | 0.18 | 1.24 | 0.215 | 0.874 | n.s. |
| c - e | 0.09 | 0.18 | 0.48 | 0.632 | 0.977 | n.s. |
| d - e | -0.14 | 0.18 | -0.76 | 0.445 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.640, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -1.35 | 23 | = 0.908 | -0.15 [-0.70, 0.16] | negligible | n.s. |
| a vs c | -0.72 | 23 | = 0.908 | -0.07 [-0.57, 0.28] | negligible | n.s. |
| a vs d | -0.09 | 23 | = 0.958 | -0.01 [-0.44, 0.40] | negligible | n.s. |
| a vs e | -0.52 | 23 | = 0.908 | -0.06 [-0.53, 0.32] | negligible | n.s. |
| b vs c | 0.82 | 23 | = 0.908 | 0.10 [-0.26, 0.59] | negligible | n.s. |
| b vs d | 1.26 | 23 | = 0.908 | 0.15 [-0.17, 0.69] | negligible | n.s. |
| b vs e | 0.99 | 23 | = 0.908 | 0.10 [-0.22, 0.63] | negligible | n.s. |
| c vs d | 0.48 | 23 | = 0.908 | 0.06 [-0.33, 0.52] | negligible | n.s. |
| c vs e | 0.05 | 23 | = 0.958 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| d vs e | -0.35 | 23 | = 0.908 | -0.05 [-0.50, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.065)
**P1 latency:** Significant main effect of condition (*p* = 0.009) (no significant pairwise comparisons)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.067)
**P3b latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - a showed greater latency than b (*d* = 0.72)
  - b showed smaller latency than c (*d* = -0.62)
  - b showed smaller latency than d (*d* = -0.99)
  - d showed greater latency than e (*d* = 0.47)

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
