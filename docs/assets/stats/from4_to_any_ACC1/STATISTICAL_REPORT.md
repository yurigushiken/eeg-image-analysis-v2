# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:21:07

---

## 1. Analysis Overview

**Total Measurements:** 432
**Number of Subjects:** 24
**Number of Conditions:** 6

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | -1.74 µV | 1.47 | 0.33 | [-4.84, 0.01] |
| 4 to 2 | 24 | -4.06 µV | 2.52 | 0.52 | [-9.35, -0.51] |
| 4 to 3 | 23 | -4.04 µV | 1.96 | 0.41 | [-8.55, -0.80] |
| 4 to 4 | 22 | -3.88 µV | 2.39 | 0.51 | [-9.94, -1.14] |
| 4 to 5 | 22 | -4.70 µV | 3.12 | 0.66 | [-13.05, -1.07] |
| 4 to 6 | 22 | -4.49 µV | 2.81 | 0.60 | [-12.83, -0.72] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 182.56 ms | 12.72 | 2.84 | [148.70, 201.04] |
| 4 to 2 | 24 | 178.11 ms | 9.29 | 1.90 | [161.53, 202.22] |
| 4 to 3 | 23 | 174.46 ms | 10.11 | 2.11 | [157.54, 203.60] |
| 4 to 4 | 22 | 175.42 ms | 10.06 | 2.14 | [155.55, 195.47] |
| 4 to 5 | 22 | 172.76 ms | 9.86 | 2.10 | [152.07, 193.23] |
| 4 to 6 | 22 | 174.73 ms | 10.01 | 2.13 | [154.94, 199.42] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 3.41 µV | 2.73 | 0.66 | [0.47, 10.41] |
| 4 to 2 | 14 | 1.70 µV | 1.26 | 0.34 | [0.16, 4.01] |
| 4 to 3 | 12 | 1.70 µV | 1.30 | 0.38 | [0.29, 4.76] |
| 4 to 4 | 12 | 2.16 µV | 1.45 | 0.42 | [0.42, 4.50] |
| 4 to 5 | 13 | 4.57 µV | 4.90 | 1.36 | [0.17, 15.16] |
| 4 to 6 | 13 | 2.39 µV | 1.76 | 0.49 | [0.19, 5.91] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 107.80 ms | 2.77 | 0.67 | [99.58, 112.61] |
| 4 to 2 | 14 | 109.01 ms | 3.04 | 0.81 | [103.66, 114.77] |
| 4 to 3 | 12 | 105.54 ms | 3.65 | 1.05 | [99.06, 113.00] |
| 4 to 4 | 12 | 106.32 ms | 3.63 | 1.05 | [101.00, 112.65] |
| 4 to 5 | 13 | 106.05 ms | 3.72 | 1.03 | [98.21, 112.31] |
| 4 to 6 | 13 | 105.63 ms | 4.80 | 1.33 | [97.31, 113.59] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 4.55 µV | 2.90 | 0.65 | [0.07, 8.70] |
| 4 to 2 | 18 | 3.79 µV | 2.68 | 0.63 | [0.23, 8.61] |
| 4 to 3 | 20 | 3.94 µV | 2.80 | 0.63 | [0.22, 9.37] |
| 4 to 4 | 12 | 2.42 µV | 2.15 | 0.62 | [0.37, 7.18] |
| 4 to 5 | 15 | 4.62 µV | 2.68 | 0.69 | [0.20, 9.98] |
| 4 to 6 | 20 | 3.68 µV | 2.74 | 0.61 | [0.07, 8.11] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 482.99 ms | 14.91 | 3.33 | [453.63, 509.20] |
| 4 to 2 | 18 | 480.33 ms | 18.34 | 4.32 | [435.99, 503.79] |
| 4 to 3 | 20 | 481.37 ms | 18.92 | 4.23 | [431.27, 525.07] |
| 4 to 4 | 12 | 484.01 ms | 21.68 | 6.26 | [458.09, 526.86] |
| 4 to 5 | 15 | 497.87 ms | 15.62 | 4.03 | [475.56, 532.59] |
| 4 to 6 | 20 | 488.33 ms | 23.33 | 5.22 | [434.73, 536.42] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 516.96, BIC = 542.97
- **4 to 2 vs 4 to 1**: *β* = -1.76, *SE* = 0.404, *z* = -4.360, *p* < .001
- **4 to 3 vs 4 to 1**: *β* = -1.28, *SE* = 0.419, *z* = -3.047, *p* = 0.002
- **4 to 4 vs 4 to 1**: *β* = -1.08, *SE* = 0.425, *z* = -2.544, *p* = 0.011
- **4 to 5 vs 4 to 1**: *β* = -1.87, *SE* = 0.423, *z* = -4.424, *p* < .001
- **4 to 6 vs 4 to 1**: *β* = -1.45, *SE* = 0.430, *z* = -3.383, *p* = 0.001
- **SNR**: *β* = -0.43, *SE* = 0.048, *z* = -8.966, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 1.76 | 0.40 | 4.36 | < .001 | < .001 | *** |
| 4 to 1 - 4 to 3 | 1.28 | 0.42 | 3.05 | 0.002 | 0.027 | * |
| 4 to 1 - 4 to 4 | 1.08 | 0.42 | 2.54 | 0.011 | 0.114 | n.s. |
| 4 to 1 - 4 to 5 | 1.87 | 0.42 | 4.42 | < .001 | < .001 | *** |
| 4 to 1 - 4 to 6 | 1.45 | 0.43 | 3.38 | < .001 | 0.009 | ** |
| 4 to 2 - 4 to 3 | -0.49 | 0.39 | -1.25 | 0.210 | 0.807 | n.s. |
| 4 to 2 - 4 to 4 | -0.68 | 0.39 | -1.74 | 0.083 | 0.540 | n.s. |
| 4 to 2 - 4 to 5 | 0.11 | 0.39 | 0.28 | 0.782 | 0.945 | n.s. |
| 4 to 2 - 4 to 6 | -0.31 | 0.40 | -0.78 | 0.437 | 0.899 | n.s. |
| 4 to 3 - 4 to 4 | -0.20 | 0.39 | -0.50 | 0.619 | 0.945 | n.s. |
| 4 to 3 - 4 to 5 | 0.59 | 0.39 | 1.51 | 0.131 | 0.676 | n.s. |
| 4 to 3 - 4 to 6 | 0.18 | 0.39 | 0.45 | 0.652 | 0.945 | n.s. |
| 4 to 4 - 4 to 5 | 0.79 | 0.40 | 1.98 | 0.048 | 0.387 | n.s. |
| 4 to 4 - 4 to 6 | 0.37 | 0.40 | 0.94 | 0.347 | 0.882 | n.s. |
| 4 to 5 - 4 to 6 | -0.42 | 0.40 | -1.04 | 0.298 | 0.880 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.51, *p* < .001, η²_G = 0.184
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 4.52 | 13 | = 0.004 | 1.51 [0.37, 1.49] | large | ** |
| 4 to 1 vs 4 to 3 | 4.48 | 13 | = 0.004 | 1.69 [0.38, 1.54] | large | ** |
| 4 to 1 vs 4 to 4 | 3.34 | 13 | = 0.016 | 1.13 [0.25, 1.41] | large | * |
| 4 to 1 vs 4 to 5 | 3.56 | 13 | = 0.013 | 1.32 [0.43, 1.66] | large | * |
| 4 to 1 vs 4 to 6 | 4.31 | 13 | = 0.004 | 1.34 [0.33, 1.52] | large | ** |
| 4 to 2 vs 4 to 3 | -0.49 | 13 | = 0.864 | -0.14 [-0.41, 0.45] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | -1.21 | 13 | = 0.528 | -0.28 [-0.54, 0.35] | small | n.s. |
| 4 to 2 vs 4 to 5 | -0.06 | 13 | = 0.953 | -0.02 [-0.33, 0.55] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | 0.10 | 13 | = 0.953 | 0.02 [-0.31, 0.59] | negligible | n.s. |
| 4 to 3 vs 4 to 4 | -0.79 | 13 | = 0.756 | -0.18 [-0.56, 0.35] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 0.33 | 13 | = 0.933 | 0.10 [-0.26, 0.66] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | 0.69 | 13 | = 0.756 | 0.15 [-0.26, 0.66] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | 0.71 | 13 | = 0.756 | 0.24 [-0.23, 0.72] | small | n.s. |
| 4 to 4 vs 4 to 6 | 1.44 | 13 | = 0.431 | 0.28 [-0.17, 0.76] | small | n.s. |
| 4 to 5 vs 4 to 6 | 0.12 | 13 | = 0.953 | 0.04 [-0.49, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 965.76, BIC = 991.77
- **4 to 2 vs 4 to 1**: *β* = -4.83, *SE* = 2.224, *z* = -2.170, *p* = 0.030
- **4 to 3 vs 4 to 1**: *β* = -8.71, *SE* = 2.306, *z* = -3.777, *p* < .001
- **4 to 4 vs 4 to 1**: *β* = -6.79, *SE* = 2.336, *z* = -2.907, *p* = 0.004
- **4 to 5 vs 4 to 1**: *β* = -9.05, *SE* = 2.326, *z* = -3.892, *p* < .001
- **4 to 6 vs 4 to 1**: *β* = -8.02, *SE* = 2.365, *z* = -3.390, *p* = 0.001
- **SNR**: *β* = -0.12, *SE* = 0.261, *z* = -0.439, *p* = 0.661

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 4.83 | 2.22 | 2.17 | 0.030 | 0.285 | n.s. |
| 4 to 1 - 4 to 3 | 8.71 | 2.31 | 3.78 | < .001 | 0.002 | ** |
| 4 to 1 - 4 to 4 | 6.79 | 2.34 | 2.91 | 0.004 | 0.043 | * |
| 4 to 1 - 4 to 5 | 9.05 | 2.33 | 3.89 | < .001 | 0.001 | ** |
| 4 to 1 - 4 to 6 | 8.02 | 2.37 | 3.39 | < .001 | 0.009 | ** |
| 4 to 2 - 4 to 3 | 3.88 | 2.13 | 1.82 | 0.069 | 0.472 | n.s. |
| 4 to 2 - 4 to 4 | 1.96 | 2.16 | 0.91 | 0.363 | 0.933 | n.s. |
| 4 to 2 - 4 to 5 | 4.23 | 2.16 | 1.96 | 0.050 | 0.401 | n.s. |
| 4 to 2 - 4 to 6 | 3.19 | 2.18 | 1.47 | 0.143 | 0.708 | n.s. |
| 4 to 3 - 4 to 4 | -1.92 | 2.17 | -0.88 | 0.377 | 0.933 | n.s. |
| 4 to 3 - 4 to 5 | 0.34 | 2.17 | 0.16 | 0.874 | 0.967 | n.s. |
| 4 to 3 - 4 to 6 | -0.69 | 2.17 | -0.32 | 0.751 | 0.967 | n.s. |
| 4 to 4 - 4 to 5 | 2.26 | 2.20 | 1.03 | 0.303 | 0.920 | n.s. |
| 4 to 4 - 4 to 6 | 1.23 | 2.19 | 0.56 | 0.575 | 0.967 | n.s. |
| 4 to 5 - 4 to 6 | -1.03 | 2.20 | -0.47 | 0.638 | 0.967 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.68, *p* = 0.005, η²_G = 0.132
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.21 | 13 | = 0.370 | 0.45 [-0.11, 0.86] | small | n.s. |
| 4 to 1 vs 4 to 3 | 2.24 | 13 | = 0.156 | 0.75 [0.10, 1.15] | medium | n.s. |
| 4 to 1 vs 4 to 4 | 2.09 | 13 | = 0.156 | 0.58 [0.02, 1.09] | medium | n.s. |
| 4 to 1 vs 4 to 5 | 2.68 | 13 | = 0.094 | 0.92 [0.17, 1.28] | large | n.s. |
| 4 to 1 vs 4 to 6 | 2.82 | 13 | = 0.094 | 0.86 [0.10, 1.20] | large | n.s. |
| 4 to 2 vs 4 to 3 | 1.59 | 13 | = 0.291 | 0.50 [0.11, 1.04] | medium | n.s. |
| 4 to 2 vs 4 to 4 | 0.75 | 13 | = 0.548 | 0.27 [-0.23, 0.66] | small | n.s. |
| 4 to 2 vs 4 to 5 | 2.89 | 13 | = 0.094 | 0.75 [-0.06, 0.86] | medium | n.s. |
| 4 to 2 vs 4 to 6 | 2.04 | 13 | = 0.156 | 0.66 [0.11, 1.07] | medium | n.s. |
| 4 to 3 vs 4 to 4 | -0.55 | 13 | = 0.618 | -0.12 [-0.65, 0.27] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 1.07 | 13 | = 0.414 | 0.33 [-0.47, 0.44] | small | n.s. |
| 4 to 3 vs 4 to 6 | 0.74 | 13 | = 0.548 | 0.19 [-0.36, 0.55] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | 1.34 | 13 | = 0.364 | 0.37 [-0.17, 0.79] | small | n.s. |
| 4 to 4 vs 4 to 6 | 1.29 | 13 | = 0.364 | 0.26 [-0.30, 0.62] | small | n.s. |
| 4 to 5 vs 4 to 6 | -0.51 | 13 | = 0.618 | -0.15 [-0.65, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 355.39, BIC = 376.94
- **4 to 2 vs 4 to 1**: *β* = -0.07, *SE* = 0.732, *z* = -0.098, *p* = 0.922
- **4 to 3 vs 4 to 1**: *β* = -0.80, *SE* = 0.743, *z* = -1.076, *p* = 0.282
- **4 to 4 vs 4 to 1**: *β* = -0.55, *SE* = 0.735, *z* = -0.745, *p* = 0.456
- **4 to 5 vs 4 to 1**: *β* = 1.99, *SE* = 0.724, *z* = 2.753, *p* = 0.006
- **4 to 6 vs 4 to 1**: *β* = 0.21, *SE* = 0.728, *z* = 0.287, *p* = 0.774
- **SNR**: *β* = 0.94, *SE* = 0.130, *z* = 7.236, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 0.07 | 0.73 | 0.10 | 0.922 | 0.992 | n.s. |
| 4 to 1 - 4 to 3 | 0.80 | 0.74 | 1.08 | 0.282 | 0.949 | n.s. |
| 4 to 1 - 4 to 4 | 0.55 | 0.73 | 0.75 | 0.456 | 0.974 | n.s. |
| 4 to 1 - 4 to 5 | -1.99 | 0.72 | -2.75 | 0.006 | 0.070 | n.s. |
| 4 to 1 - 4 to 6 | -0.21 | 0.73 | -0.29 | 0.774 | 0.992 | n.s. |
| 4 to 2 - 4 to 3 | 0.73 | 0.76 | 0.96 | 0.337 | 0.958 | n.s. |
| 4 to 2 - 4 to 4 | 0.48 | 0.76 | 0.62 | 0.534 | 0.978 | n.s. |
| 4 to 2 - 4 to 5 | -2.06 | 0.75 | -2.77 | 0.006 | 0.070 | n.s. |
| 4 to 2 - 4 to 6 | -0.28 | 0.74 | -0.38 | 0.704 | 0.992 | n.s. |
| 4 to 3 - 4 to 4 | -0.25 | 0.78 | -0.32 | 0.748 | 0.992 | n.s. |
| 4 to 3 - 4 to 5 | -2.79 | 0.77 | -3.64 | < .001 | 0.004 | ** |
| 4 to 3 - 4 to 6 | -1.01 | 0.77 | -1.31 | 0.191 | 0.880 | n.s. |
| 4 to 4 - 4 to 5 | -2.54 | 0.77 | -3.30 | < .001 | 0.013 | * |
| 4 to 4 - 4 to 6 | -0.76 | 0.77 | -0.98 | 0.327 | 0.958 | n.s. |
| 4 to 5 - 4 to 6 | 1.78 | 0.75 | 2.37 | 0.018 | 0.181 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.809, η²_G = 0.174
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.51 | 2 | = 0.899 | 1.09 [-0.14, 1.22] | large | n.s. |
| 4 to 1 vs 4 to 3 | 2.57 | 2 | = 0.899 | 0.79 [-0.03, 1.61] | medium | n.s. |
| 4 to 1 vs 4 to 4 | 1.51 | 2 | = 0.899 | 0.70 [-0.33, 1.29] | medium | n.s. |
| 4 to 1 vs 4 to 5 | 0.21 | 2 | = 0.940 | 0.22 [-0.45, 1.13] | small | n.s. |
| 4 to 1 vs 4 to 6 | 0.59 | 2 | = 0.899 | 0.64 [-0.51, 0.94] | medium | n.s. |
| 4 to 2 vs 4 to 3 | -0.47 | 2 | = 0.899 | -0.31 [-0.70, 0.64] | small | n.s. |
| 4 to 2 vs 4 to 4 | -1.46 | 2 | = 0.899 | -0.85 [-1.06, 0.50] | large | n.s. |
| 4 to 2 vs 4 to 5 | -0.86 | 2 | = 0.899 | -0.76 [-1.45, 0.13] | medium | n.s. |
| 4 to 2 vs 4 to 6 | -0.59 | 2 | = 0.899 | -0.54 [-1.34, 0.30] | medium | n.s. |
| 4 to 3 vs 4 to 4 | -0.84 | 2 | = 0.899 | -0.23 [-0.87, 0.98] | small | n.s. |
| 4 to 3 vs 4 to 5 | -0.48 | 2 | = 0.899 | -0.51 [-1.71, 0.19] | medium | n.s. |
| 4 to 3 vs 4 to 6 | -0.18 | 2 | = 0.940 | -0.19 [-0.91, 0.76] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | -0.41 | 2 | = 0.899 | -0.39 [-1.54, 0.66] | small | n.s. |
| 4 to 4 vs 4 to 6 | 0.00 | 2 | = 0.998 | 0.00 [-1.02, 0.83] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 0.49 | 2 | = 0.899 | 0.36 [-0.56, 1.00] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 446.32, BIC = 467.87
- **4 to 2 vs 4 to 1**: *β* = 0.83, *SE* = 1.218, *z* = 0.680, *p* = 0.496
- **4 to 3 vs 4 to 1**: *β* = -2.37, *SE* = 1.215, *z* = -1.947, *p* = 0.052
- **4 to 4 vs 4 to 1**: *β* = -2.12, *SE* = 1.243, *z* = -1.708, *p* = 0.088
- **4 to 5 vs 4 to 1**: *β* = -1.89, *SE* = 1.197, *z* = -1.582, *p* = 0.114
- **4 to 6 vs 4 to 1**: *β* = -2.62, *SE* = 1.218, *z* = -2.154, *p* = 0.031
- **SNR**: *β* = 0.01, *SE* = 0.232, *z* = 0.053, *p* = 0.957

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.83 | 1.22 | -0.68 | 0.496 | 0.992 | n.s. |
| 4 to 1 - 4 to 3 | 2.37 | 1.22 | 1.95 | 0.052 | 0.411 | n.s. |
| 4 to 1 - 4 to 4 | 2.12 | 1.24 | 1.71 | 0.088 | 0.562 | n.s. |
| 4 to 1 - 4 to 5 | 1.89 | 1.20 | 1.58 | 0.114 | 0.619 | n.s. |
| 4 to 1 - 4 to 6 | 2.62 | 1.22 | 2.15 | 0.031 | 0.295 | n.s. |
| 4 to 2 - 4 to 3 | 3.19 | 1.24 | 2.58 | 0.010 | 0.129 | n.s. |
| 4 to 2 - 4 to 4 | 2.95 | 1.28 | 2.31 | 0.021 | 0.240 | n.s. |
| 4 to 2 - 4 to 5 | 2.72 | 1.23 | 2.21 | 0.027 | 0.279 | n.s. |
| 4 to 2 - 4 to 6 | 3.45 | 1.23 | 2.82 | 0.005 | 0.070 | n.s. |
| 4 to 3 - 4 to 4 | -0.24 | 1.33 | -0.18 | 0.855 | 0.997 | n.s. |
| 4 to 3 - 4 to 5 | -0.47 | 1.27 | -0.37 | 0.709 | 0.997 | n.s. |
| 4 to 3 - 4 to 6 | 0.26 | 1.28 | 0.20 | 0.841 | 0.997 | n.s. |
| 4 to 4 - 4 to 5 | -0.23 | 1.31 | -0.18 | 0.860 | 0.997 | n.s. |
| 4 to 4 - 4 to 6 | 0.50 | 1.29 | 0.39 | 0.698 | 0.997 | n.s. |
| 4 to 5 - 4 to 6 | 0.73 | 1.25 | 0.59 | 0.558 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.36, *p* = 0.865, η²_G = 0.126
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.36 | 2 | = 0.946 | 0.35 [-0.98, 0.32] | small | n.s. |
| 4 to 1 vs 4 to 3 | 0.11 | 2 | = 0.981 | 0.11 [-0.05, 1.57] | negligible | n.s. |
| 4 to 1 vs 4 to 4 | 0.96 | 2 | = 0.943 | 0.96 [-0.07, 1.70] | large | n.s. |
| 4 to 1 vs 4 to 5 | 1.02 | 2 | = 0.943 | 1.15 [-0.43, 1.16] | large | n.s. |
| 4 to 1 vs 4 to 6 | -0.26 | 2 | = 0.946 | -0.27 [-0.25, 1.27] | small | n.s. |
| 4 to 2 vs 4 to 3 | -0.03 | 2 | = 0.981 | -0.02 [-0.24, 1.18] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 2.45 | 2 | = 0.943 | 1.25 [-0.12, 1.62] | large | n.s. |
| 4 to 2 vs 4 to 5 | 1.79 | 2 | = 0.943 | 1.25 [-0.15, 1.42] | large | n.s. |
| 4 to 2 vs 4 to 6 | -0.59 | 2 | = 0.946 | -0.48 [-0.23, 1.44] | small | n.s. |
| 4 to 3 vs 4 to 4 | 0.32 | 2 | = 0.946 | 0.24 [-0.78, 1.08] | small | n.s. |
| 4 to 3 vs 4 to 5 | 0.54 | 2 | = 0.946 | 0.39 [-0.80, 0.87] | small | n.s. |
| 4 to 3 vs 4 to 6 | -0.38 | 2 | = 0.946 | -0.27 [-0.90, 0.77] | small | n.s. |
| 4 to 4 vs 4 to 5 | 1.08 | 2 | = 0.943 | 0.56 [-1.11, 0.99] | medium | n.s. |
| 4 to 4 vs 4 to 6 | -1.08 | 2 | = 0.943 | -0.79 [-1.10, 0.76] | medium | n.s. |
| 4 to 5 vs 4 to 6 | -1.89 | 2 | = 0.943 | -0.95 [-0.50, 1.07] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 442.46, BIC = 466.35
- **4 to 2 vs 4 to 1**: *β* = 0.23, *SE* = 0.520, *z* = 0.440, *p* = 0.660
- **4 to 3 vs 4 to 1**: *β* = 0.07, *SE* = 0.495, *z* = 0.140, *p* = 0.888
- **4 to 4 vs 4 to 1**: *β* = -1.10, *SE* = 0.616, *z* = -1.792, *p* = 0.073
- **4 to 5 vs 4 to 1**: *β* = 0.57, *SE* = 0.555, *z* = 1.035, *p* = 0.301
- **4 to 6 vs 4 to 1**: *β* = -0.10, *SE* = 0.501, *z* = -0.196, *p* = 0.845
- **SNR**: *β* = 0.28, *SE* = 0.041, *z* = 6.838, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.23 | 0.52 | -0.44 | 0.660 | 0.995 | n.s. |
| 4 to 1 - 4 to 3 | -0.07 | 0.49 | -0.14 | 0.888 | 0.995 | n.s. |
| 4 to 1 - 4 to 4 | 1.10 | 0.62 | 1.79 | 0.073 | 0.598 | n.s. |
| 4 to 1 - 4 to 5 | -0.57 | 0.56 | -1.03 | 0.301 | 0.960 | n.s. |
| 4 to 1 - 4 to 6 | 0.10 | 0.50 | 0.20 | 0.845 | 0.995 | n.s. |
| 4 to 2 - 4 to 3 | 0.16 | 0.51 | 0.31 | 0.754 | 0.995 | n.s. |
| 4 to 2 - 4 to 4 | 1.33 | 0.60 | 2.24 | 0.025 | 0.301 | n.s. |
| 4 to 2 - 4 to 5 | -0.35 | 0.54 | -0.63 | 0.525 | 0.994 | n.s. |
| 4 to 2 - 4 to 6 | 0.33 | 0.50 | 0.65 | 0.517 | 0.994 | n.s. |
| 4 to 3 - 4 to 4 | 1.17 | 0.59 | 1.98 | 0.047 | 0.467 | n.s. |
| 4 to 3 - 4 to 5 | -0.51 | 0.54 | -0.94 | 0.350 | 0.968 | n.s. |
| 4 to 3 - 4 to 6 | 0.17 | 0.48 | 0.35 | 0.730 | 0.995 | n.s. |
| 4 to 4 - 4 to 5 | -1.68 | 0.61 | -2.75 | 0.006 | 0.086 | n.s. |
| 4 to 4 - 4 to 6 | -1.01 | 0.58 | -1.74 | 0.083 | 0.612 | n.s. |
| 4 to 5 - 4 to 6 | 0.67 | 0.53 | 1.26 | 0.208 | 0.903 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.24, *p* < .001, η²_G = 0.266
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.54 | 5 | = 0.654 | 0.17 [-0.38, 0.69] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | -0.09 | 5 | = 0.934 | -0.02 [-0.48, 0.55] | negligible | n.s. |
| 4 to 1 vs 4 to 4 | 2.69 | 5 | = 0.103 | 1.55 [0.20, 2.02] | large | n.s. |
| 4 to 1 vs 4 to 5 | 2.21 | 5 | = 0.147 | 0.87 [-0.37, 0.79] | large | n.s. |
| 4 to 1 vs 4 to 6 | 0.80 | 5 | = 0.626 | 0.22 [-0.22, 0.83] | small | n.s. |
| 4 to 2 vs 4 to 3 | -0.66 | 5 | = 0.652 | -0.19 [-0.62, 0.45] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 3.74 | 5 | = 0.101 | 1.52 [-0.21, 1.48] | large | n.s. |
| 4 to 2 vs 4 to 5 | 4.53 | 5 | = 0.093 | 0.76 [-0.71, 0.51] | medium | n.s. |
| 4 to 2 vs 4 to 6 | 0.62 | 5 | = 0.652 | 0.05 [-0.38, 0.69] | negligible | n.s. |
| 4 to 3 vs 4 to 4 | 2.79 | 5 | = 0.103 | 1.59 [0.05, 1.60] | large | n.s. |
| 4 to 3 vs 4 to 5 | 2.60 | 5 | = 0.103 | 0.90 [-0.43, 0.73] | large | n.s. |
| 4 to 3 vs 4 to 6 | 0.87 | 5 | = 0.626 | 0.24 [-0.30, 0.67] | small | n.s. |
| 4 to 4 vs 4 to 5 | -2.00 | 5 | = 0.170 | -0.62 [-1.73, 0.06] | medium | n.s. |
| 4 to 4 vs 4 to 6 | -3.08 | 5 | = 0.103 | -1.37 [-1.27, 0.11] | large | n.s. |
| 4 to 5 vs 4 to 6 | -3.31 | 5 | = 0.103 | -0.67 [-0.75, 0.42] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 923.36, BIC = 947.25
- **4 to 2 vs 4 to 1**: *β* = -3.20, *SE* = 5.628, *z* = -0.569, *p* = 0.570
- **4 to 3 vs 4 to 1**: *β* = -1.36, *SE* = 5.376, *z* = -0.253, *p* = 0.800
- **4 to 4 vs 4 to 1**: *β* = 2.09, *SE* = 6.558, *z* = 0.318, *p* = 0.750
- **4 to 5 vs 4 to 1**: *β* = 15.30, *SE* = 5.947, *z* = 2.573, *p* = 0.010
- **4 to 6 vs 4 to 1**: *β* = 5.86, *SE* = 5.432, *z* = 1.078, *p* = 0.281
- **SNR**: *β* = -0.16, *SE* = 0.405, *z* = -0.400, *p* = 0.689

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 3.20 | 5.63 | 0.57 | 0.570 | 0.991 | n.s. |
| 4 to 1 - 4 to 3 | 1.36 | 5.38 | 0.25 | 0.800 | 0.991 | n.s. |
| 4 to 1 - 4 to 4 | -2.09 | 6.56 | -0.32 | 0.750 | 0.991 | n.s. |
| 4 to 1 - 4 to 5 | -15.30 | 5.95 | -2.57 | 0.010 | 0.123 | n.s. |
| 4 to 1 - 4 to 6 | -5.86 | 5.43 | -1.08 | 0.281 | 0.929 | n.s. |
| 4 to 2 - 4 to 3 | -1.84 | 5.53 | -0.33 | 0.739 | 0.991 | n.s. |
| 4 to 2 - 4 to 4 | -5.29 | 6.44 | -0.82 | 0.412 | 0.976 | n.s. |
| 4 to 2 - 4 to 5 | -18.50 | 5.92 | -3.12 | 0.002 | 0.026 | * |
| 4 to 2 - 4 to 6 | -9.06 | 5.50 | -1.65 | 0.100 | 0.686 | n.s. |
| 4 to 3 - 4 to 4 | -3.45 | 6.35 | -0.54 | 0.587 | 0.991 | n.s. |
| 4 to 3 - 4 to 5 | -16.66 | 5.82 | -2.86 | 0.004 | 0.057 | n.s. |
| 4 to 3 - 4 to 6 | -7.22 | 5.31 | -1.36 | 0.174 | 0.821 | n.s. |
| 4 to 4 - 4 to 5 | -13.21 | 6.63 | -1.99 | 0.046 | 0.432 | n.s. |
| 4 to 4 - 4 to 6 | -3.77 | 6.26 | -0.60 | 0.548 | 0.991 | n.s. |
| 4 to 5 - 4 to 6 | 9.45 | 5.79 | 1.63 | 0.103 | 0.686 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.63, *p* = 0.188, η²_G = 0.212
- Greenhouse-Geisser corrected: *p* = 0.250 (ε = 0.328)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | -1.09 | 5 | = 0.485 | -0.46 [-0.47, 0.59] | small | n.s. |
| 4 to 1 vs 4 to 3 | -1.22 | 5 | = 0.485 | -0.70 [-0.48, 0.55] | medium | n.s. |
| 4 to 1 vs 4 to 4 | -0.98 | 5 | = 0.505 | -0.70 [-0.83, 0.61] | medium | n.s. |
| 4 to 1 vs 4 to 5 | -1.89 | 5 | = 0.485 | -1.31 [-1.56, -0.20] | large | n.s. |
| 4 to 1 vs 4 to 6 | -1.44 | 5 | = 0.485 | -0.97 [-0.72, 0.32] | large | n.s. |
| 4 to 2 vs 4 to 3 | -1.31 | 5 | = 0.485 | -0.40 [-0.84, 0.25] | small | n.s. |
| 4 to 2 vs 4 to 4 | -0.75 | 5 | = 0.606 | -0.51 [-0.91, 0.64] | medium | n.s. |
| 4 to 2 vs 4 to 5 | -1.76 | 5 | = 0.485 | -1.18 [-1.65, -0.20] | large | n.s. |
| 4 to 2 vs 4 to 6 | -1.10 | 5 | = 0.485 | -0.78 [-0.95, 0.16] | medium | n.s. |
| 4 to 3 vs 4 to 4 | -0.53 | 5 | = 0.665 | -0.35 [-0.84, 0.51] | small | n.s. |
| 4 to 3 vs 4 to 5 | -1.54 | 5 | = 0.485 | -0.98 [-1.47, -0.14] | large | n.s. |
| 4 to 3 vs 4 to 6 | -0.67 | 5 | = 0.616 | -0.47 [-0.86, 0.14] | small | n.s. |
| 4 to 4 vs 4 to 5 | -1.38 | 5 | = 0.485 | -0.42 [-1.39, 0.27] | small | n.s. |
| 4 to 4 vs 4 to 6 | 0.18 | 5 | = 0.862 | 0.08 [-0.32, 0.99] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 2.41 | 5 | = 0.485 | 0.63 [-0.01, 1.25] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 2 (*d* = 1.51)
  - 4 to 1 showed greater amplitude than 4 to 3 (*d* = 1.69)
  - 4 to 1 showed greater amplitude than 4 to 4 (*d* = 1.13)
  - 4 to 1 showed greater amplitude than 4 to 5 (*d* = 1.32)
  - 4 to 1 showed greater amplitude than 4 to 6 (*d* = 1.34)
**N1 latency:** Significant main effect of condition (*p* = 0.005) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* < .001) (no significant pairwise comparisons)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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
