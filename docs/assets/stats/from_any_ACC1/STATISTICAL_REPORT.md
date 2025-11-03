# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:41:24

---

## 1. Analysis Overview

**Total Measurements:** 576
**Number of Subjects:** 24
**Number of Conditions:** 6

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
| from 1 | 11 | 105.82 ms | 8.83 | 2.66 | [92.00, 116.00] |
| from 2 | 16 | 103.75 ms | 8.70 | 2.17 | [92.00, 116.00] |
| from 3 | 13 | 103.38 ms | 7.81 | 2.16 | [92.00, 116.00] |
| from 4 | 16 | 106.00 ms | 7.30 | 1.83 | [92.00, 116.00] |
| from 5 | 21 | 104.19 ms | 8.34 | 1.82 | [92.00, 116.00] |
| from 6 | 19 | 105.68 ms | 8.57 | 1.97 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 11 | -1.62 µV | 0.63 | 0.19 | [-2.86, -0.38] |
| from 2 | 16 | -1.63 µV | 1.07 | 0.27 | [-4.40, -0.19] |
| from 3 | 13 | -2.01 µV | 1.02 | 0.28 | [-4.15, -0.85] |
| from 4 | 16 | -1.72 µV | 1.36 | 0.34 | [-5.63, -0.31] |
| from 5 | 21 | -2.25 µV | 1.23 | 0.27 | [-6.01, -0.40] |
| from 6 | 19 | -2.23 µV | 1.49 | 0.34 | [-6.83, -0.38] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 173.67 ms | 20.53 | 4.19 | [144.00, 208.00] |
| from 2 | 22 | 171.82 ms | 15.24 | 3.25 | [144.00, 208.00] |
| from 3 | 22 | 170.91 ms | 17.60 | 3.75 | [144.00, 208.00] |
| from 4 | 24 | 175.50 ms | 16.10 | 3.29 | [144.00, 208.00] |
| from 5 | 23 | 168.35 ms | 13.69 | 2.86 | [144.00, 196.00] |
| from 6 | 24 | 173.50 ms | 17.37 | 3.55 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | -5.75 µV | 2.35 | 0.48 | [-11.42, -1.92] |
| from 2 | 22 | -5.02 µV | 1.60 | 0.34 | [-8.63, -2.88] |
| from 3 | 22 | -5.14 µV | 1.98 | 0.42 | [-8.94, -1.98] |
| from 4 | 24 | -4.99 µV | 2.07 | 0.42 | [-9.86, -2.11] |
| from 5 | 23 | -5.83 µV | 2.27 | 0.47 | [-9.50, -1.21] |
| from 6 | 24 | -5.96 µV | 2.12 | 0.43 | [-10.13, -3.03] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 13 | 104.92 ms | 9.82 | 2.72 | [96.00, 120.00] |
| from 2 | 16 | 110.50 ms | 9.34 | 2.33 | [96.00, 120.00] |
| from 3 | 14 | 110.57 ms | 8.82 | 2.36 | [96.00, 120.00] |
| from 4 | 12 | 112.67 ms | 5.61 | 1.62 | [104.00, 120.00] |
| from 5 | 15 | 111.20 ms | 8.44 | 2.18 | [96.00, 120.00] |
| from 6 | 15 | 111.73 ms | 7.92 | 2.05 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 13 | 2.10 µV | 1.09 | 0.30 | [0.53, 4.79] |
| from 2 | 16 | 2.30 µV | 1.75 | 0.44 | [0.42, 5.42] |
| from 3 | 14 | 2.00 µV | 1.58 | 0.42 | [0.21, 4.88] |
| from 4 | 12 | 2.65 µV | 1.52 | 0.44 | [0.89, 5.46] |
| from 5 | 15 | 2.76 µV | 1.05 | 0.27 | [1.04, 4.84] |
| from 6 | 15 | 2.89 µV | 1.83 | 0.47 | [1.09, 7.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 19 | 486.53 ms | 33.89 | 7.78 | [428.00, 536.00] |
| from 2 | 19 | 484.42 ms | 36.56 | 8.39 | [424.00, 536.00] |
| from 3 | 19 | 484.00 ms | 29.75 | 6.83 | [432.00, 536.00] |
| from 4 | 20 | 490.40 ms | 33.30 | 7.45 | [436.00, 536.00] |
| from 5 | 18 | 481.56 ms | 28.16 | 6.64 | [432.00, 536.00] |
| from 6 | 19 | 488.21 ms | 34.70 | 7.96 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 19 | 4.91 µV | 3.02 | 0.69 | [1.06, 12.24] |
| from 2 | 19 | 5.04 µV | 2.48 | 0.57 | [1.22, 8.81] |
| from 3 | 19 | 4.69 µV | 2.64 | 0.61 | [1.38, 9.87] |
| from 4 | 20 | 4.75 µV | 2.82 | 0.63 | [0.74, 8.97] |
| from 5 | 18 | 5.08 µV | 2.36 | 0.56 | [2.17, 10.98] |
| from 6 | 19 | 4.97 µV | 2.46 | 0.56 | [0.61, 9.98] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 659.72, BIC = 682.80
- **from 2 vs from 1**: *β* = -2.59, *SE* = 2.296, *z* = -1.129, *p* = 0.259
- **from 3 vs from 1**: *β* = -2.78, *SE* = 2.368, *z* = -1.176, *p* = 0.240
- **from 4 vs from 1**: *β* = 0.23, *SE* = 2.278, *z* = 0.103, *p* = 0.918
- **from 5 vs from 1**: *β* = -1.62, *SE* = 2.269, *z* = -0.713, *p* = 0.476
- **from 6 vs from 1**: *β* = 0.24, *SE* = 2.242, *z* = 0.109, *p* = 0.913
- **SNR**: *β* = -0.05, *SE* = 0.375, *z* = -0.144, *p* = 0.886

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 2.59 | 2.30 | 1.13 | 0.259 | 0.951 | n.s. |
| from 1 - from 3 | 2.78 | 2.37 | 1.18 | 0.240 | 0.951 | n.s. |
| from 1 - from 4 | -0.24 | 2.28 | -0.10 | 0.918 | 1.000 | n.s. |
| from 1 - from 5 | 1.62 | 2.27 | 0.71 | 0.476 | 0.989 | n.s. |
| from 1 - from 6 | -0.24 | 2.24 | -0.11 | 0.913 | 1.000 | n.s. |
| from 2 - from 3 | 0.19 | 2.18 | 0.09 | 0.930 | 1.000 | n.s. |
| from 2 - from 4 | -2.83 | 2.06 | -1.37 | 0.169 | 0.908 | n.s. |
| from 2 - from 5 | -0.98 | 1.94 | -0.50 | 0.615 | 0.994 | n.s. |
| from 2 - from 6 | -2.84 | 1.99 | -1.42 | 0.154 | 0.908 | n.s. |
| from 3 - from 4 | -3.02 | 2.15 | -1.40 | 0.161 | 0.908 | n.s. |
| from 3 - from 5 | -1.17 | 2.05 | -0.57 | 0.570 | 0.994 | n.s. |
| from 3 - from 6 | -3.03 | 2.09 | -1.45 | 0.147 | 0.908 | n.s. |
| from 4 - from 5 | 1.85 | 1.93 | 0.96 | 0.336 | 0.966 | n.s. |
| from 4 - from 6 | -0.01 | 1.95 | -0.00 | 0.996 | 1.000 | n.s. |
| from 5 - from 6 | -1.86 | 1.84 | -1.01 | 0.313 | 0.966 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.373, η²_G = 0.084
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 1.51 | 4 | = 0.605 | 0.76 [-0.56, 0.99] | medium | n.s. |
| from 1 vs from 3 | 1.09 | 4 | = 0.633 | 0.42 [-0.43, 1.15] | small | n.s. |
| from 1 vs from 4 | 0.58 | 4 | = 0.802 | 0.37 [-0.77, 0.77] | small | n.s. |
| from 1 vs from 5 | 1.18 | 4 | = 0.633 | 0.71 [-0.25, 1.41] | medium | n.s. |
| from 1 vs from 6 | 0.69 | 4 | = 0.802 | 0.35 [-0.68, 1.00] | small | n.s. |
| from 2 vs from 3 | -1.50 | 4 | = 0.605 | -0.32 [-1.24, 0.37] | small | n.s. |
| from 2 vs from 4 | -2.14 | 4 | = 0.497 | -0.50 [-1.09, 0.31] | medium | n.s. |
| from 2 vs from 5 | -0.41 | 4 | = 0.802 | -0.12 [-0.82, 0.40] | negligible | n.s. |
| from 2 vs from 6 | -1.37 | 4 | = 0.605 | -0.48 [-1.33, 0.06] | small | n.s. |
| from 3 vs from 4 | -0.34 | 4 | = 0.802 | -0.12 [-1.01, 0.45] | negligible | n.s. |
| from 3 vs from 5 | 0.67 | 4 | = 0.802 | 0.23 [-0.76, 0.52] | small | n.s. |
| from 3 vs from 6 | -0.34 | 4 | = 0.802 | -0.12 [-1.28, 0.16] | negligible | n.s. |
| from 4 vs from 5 | 2.45 | 4 | = 0.497 | 0.42 [-0.23, 0.91] | small | n.s. |
| from 4 vs from 6 | 0.00 | 4 | = 1.000 | 0.00 [-0.44, 0.78] | negligible | n.s. |
| from 5 vs from 6 | -2.45 | 4 | = 0.497 | -0.40 [-0.80, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 255.41, BIC = 278.48
- **from 2 vs from 1**: *β* = -0.07, *SE* = 0.292, *z* = -0.241, *p* = 0.809
- **from 3 vs from 1**: *β* = -0.22, *SE* = 0.299, *z* = -0.735, *p* = 0.463
- **from 4 vs from 1**: *β* = -0.25, *SE* = 0.290, *z* = -0.851, *p* = 0.395
- **from 5 vs from 1**: *β* = -0.62, *SE* = 0.291, *z* = -2.124, *p* = 0.034
- **from 6 vs from 1**: *β* = -0.90, *SE* = 0.285, *z* = -3.152, *p* = 0.002
- **SNR**: *β* = -0.25, *SE* = 0.049, *z* = -5.152, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.07 | 0.29 | 0.24 | 0.809 | 0.964 | n.s. |
| from 1 - from 3 | 0.22 | 0.30 | 0.73 | 0.463 | 0.955 | n.s. |
| from 1 - from 4 | 0.25 | 0.29 | 0.85 | 0.395 | 0.951 | n.s. |
| from 1 - from 5 | 0.62 | 0.29 | 2.12 | 0.034 | 0.290 | n.s. |
| from 1 - from 6 | 0.90 | 0.28 | 3.15 | 0.002 | 0.022 | * |
| from 2 - from 3 | 0.15 | 0.28 | 0.54 | 0.590 | 0.955 | n.s. |
| from 2 - from 4 | 0.18 | 0.26 | 0.68 | 0.497 | 0.955 | n.s. |
| from 2 - from 5 | 0.55 | 0.24 | 2.25 | 0.025 | 0.241 | n.s. |
| from 2 - from 6 | 0.83 | 0.25 | 3.31 | < .001 | 0.014 | * |
| from 3 - from 4 | 0.03 | 0.27 | 0.10 | 0.921 | 0.964 | n.s. |
| from 3 - from 5 | 0.40 | 0.26 | 1.52 | 0.129 | 0.705 | n.s. |
| from 3 - from 6 | 0.68 | 0.26 | 2.56 | 0.010 | 0.118 | n.s. |
| from 4 - from 5 | 0.37 | 0.24 | 1.53 | 0.127 | 0.705 | n.s. |
| from 4 - from 6 | 0.65 | 0.25 | 2.65 | 0.008 | 0.101 | n.s. |
| from 5 - from 6 | 0.28 | 0.23 | 1.19 | 0.232 | 0.843 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.196, η²_G = 0.097
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 0.53 | 4 | = 0.722 | 0.24 [-0.54, 1.02] | small | n.s. |
| from 1 vs from 3 | 0.92 | 4 | = 0.587 | 0.46 [-0.31, 1.32] | small | n.s. |
| from 1 vs from 4 | 1.14 | 4 | = 0.587 | 0.52 [-0.36, 1.26] | medium | n.s. |
| from 1 vs from 5 | 1.77 | 4 | = 0.454 | 0.82 [0.11, 2.05] | large | n.s. |
| from 1 vs from 6 | 1.85 | 4 | = 0.454 | 0.88 [-0.11, 1.85] | large | n.s. |
| from 2 vs from 3 | 0.23 | 4 | = 0.830 | 0.10 [-0.54, 1.02] | negligible | n.s. |
| from 2 vs from 4 | 0.95 | 4 | = 0.587 | 0.25 [-0.59, 0.75] | small | n.s. |
| from 2 vs from 5 | 3.39 | 4 | = 0.207 | 0.48 [-0.12, 1.17] | small | n.s. |
| from 2 vs from 6 | 1.79 | 4 | = 0.454 | 0.58 [-0.18, 1.16] | medium | n.s. |
| from 3 vs from 4 | 0.45 | 4 | = 0.722 | 0.19 [-0.69, 0.74] | negligible | n.s. |
| from 3 vs from 5 | 0.88 | 4 | = 0.587 | 0.44 [0.05, 1.50] | small | n.s. |
| from 3 vs from 6 | 1.22 | 4 | = 0.587 | 0.55 [-0.08, 1.41] | medium | n.s. |
| from 4 vs from 5 | 1.05 | 4 | = 0.587 | 0.21 [0.12, 1.38] | small | n.s. |
| from 4 vs from 6 | 3.66 | 4 | = 0.207 | 0.32 [0.30, 1.80] | small | n.s. |
| from 5 vs from 6 | 0.53 | 4 | = 0.722 | 0.13 [-0.53, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1107.64, BIC = 1134.05
- **from 2 vs from 1**: *β* = -0.03, *SE* = 2.907, *z* = -0.011, *p* = 0.991
- **from 3 vs from 1**: *β* = -1.54, *SE* = 2.932, *z* = -0.525, *p* = 0.600
- **from 4 vs from 1**: *β* = 1.71, *SE* = 2.828, *z* = 0.606, *p* = 0.544
- **from 5 vs from 1**: *β* = -4.19, *SE* = 2.866, *z* = -1.463, *p* = 0.143
- **from 6 vs from 1**: *β* = 0.01, *SE* = 2.828, *z* = 0.004, *p* = 0.997
- **SNR**: *β* = 0.42, *SE* = 0.222, *z* = 1.892, *p* = 0.058

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.03 | 2.91 | 0.01 | 0.991 | 1.000 | n.s. |
| from 1 - from 3 | 1.54 | 2.93 | 0.52 | 0.600 | 0.999 | n.s. |
| from 1 - from 4 | -1.71 | 2.83 | -0.61 | 0.544 | 0.999 | n.s. |
| from 1 - from 5 | 4.19 | 2.87 | 1.46 | 0.143 | 0.885 | n.s. |
| from 1 - from 6 | -0.01 | 2.83 | -0.00 | 0.997 | 1.000 | n.s. |
| from 2 - from 3 | 1.51 | 3.01 | 0.50 | 0.617 | 0.999 | n.s. |
| from 2 - from 4 | -1.75 | 2.91 | -0.60 | 0.548 | 0.999 | n.s. |
| from 2 - from 5 | 4.16 | 2.95 | 1.41 | 0.158 | 0.885 | n.s. |
| from 2 - from 6 | -0.04 | 2.90 | -0.02 | 0.988 | 1.000 | n.s. |
| from 3 - from 4 | -3.25 | 2.92 | -1.11 | 0.266 | 0.967 | n.s. |
| from 3 - from 5 | 2.65 | 2.94 | 0.90 | 0.367 | 0.990 | n.s. |
| from 3 - from 6 | -1.55 | 2.95 | -0.53 | 0.599 | 0.999 | n.s. |
| from 4 - from 5 | 5.91 | 2.86 | 2.06 | 0.039 | 0.451 | n.s. |
| from 4 - from 6 | 1.70 | 2.83 | 0.60 | 0.547 | 0.999 | n.s. |
| from 5 - from 6 | -4.20 | 2.87 | -1.46 | 0.143 | 0.885 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.822, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.685 (ε = 0.481)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.36 | 20 | = 0.955 | -0.09 [-0.52, 0.37] | negligible | n.s. |
| from 1 vs from 3 | -0.13 | 20 | = 0.955 | -0.02 [-0.47, 0.42] | negligible | n.s. |
| from 1 vs from 4 | -0.80 | 20 | = 0.906 | -0.22 [-0.52, 0.33] | small | n.s. |
| from 1 vs from 5 | 0.21 | 20 | = 0.955 | 0.04 [-0.20, 0.68] | negligible | n.s. |
| from 1 vs from 6 | -0.56 | 20 | = 0.906 | -0.09 [-0.41, 0.44] | negligible | n.s. |
| from 2 vs from 3 | 0.27 | 20 | = 0.955 | 0.07 [-0.40, 0.51] | negligible | n.s. |
| from 2 vs from 4 | -1.12 | 20 | = 0.906 | -0.15 [-0.69, 0.21] | negligible | n.s. |
| from 2 vs from 5 | 0.53 | 20 | = 0.906 | 0.14 [-0.34, 0.57] | negligible | n.s. |
| from 2 vs from 6 | -0.06 | 20 | = 0.955 | -0.01 [-0.46, 0.43] | negligible | n.s. |
| from 3 vs from 4 | -0.89 | 20 | = 0.906 | -0.20 [-0.58, 0.31] | small | n.s. |
| from 3 vs from 5 | 0.54 | 20 | = 0.906 | 0.06 [-0.23, 0.67] | negligible | n.s. |
| from 3 vs from 6 | -0.78 | 20 | = 0.906 | -0.07 [-0.49, 0.40] | negligible | n.s. |
| from 4 vs from 5 | 1.12 | 20 | = 0.906 | 0.28 [-0.11, 0.78] | small | n.s. |
| from 4 vs from 6 | 0.57 | 20 | = 0.906 | 0.13 [-0.29, 0.56] | negligible | n.s. |
| from 5 vs from 6 | -1.08 | 20 | = 0.906 | -0.14 [-0.80, 0.09] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 464.81, BIC = 491.22
- **from 2 vs from 1**: *β* = 0.87, *SE* = 0.281, *z* = 3.085, *p* = 0.002
- **from 3 vs from 1**: *β* = 1.00, *SE* = 0.283, *z* = 3.523, *p* < .001
- **from 4 vs from 1**: *β* = 0.80, *SE* = 0.273, *z* = 2.922, *p* = 0.003
- **from 5 vs from 1**: *β* = 0.01, *SE* = 0.277, *z* = 0.032, *p* = 0.974
- **from 6 vs from 1**: *β* = -0.26, *SE* = 0.273, *z* = -0.961, *p* = 0.337
- **SNR**: *β* = -0.12, *SE* = 0.022, *z* = -5.449, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.87 | 0.28 | -3.09 | 0.002 | 0.020 | * |
| from 1 - from 3 | -1.00 | 0.28 | -3.52 | < .001 | 0.005 | ** |
| from 1 - from 4 | -0.80 | 0.27 | -2.92 | 0.003 | 0.028 | * |
| from 1 - from 5 | -0.01 | 0.28 | -0.03 | 0.974 | 0.974 | n.s. |
| from 1 - from 6 | 0.26 | 0.27 | 0.96 | 0.337 | 0.908 | n.s. |
| from 2 - from 3 | -0.13 | 0.29 | -0.45 | 0.653 | 0.958 | n.s. |
| from 2 - from 4 | 0.07 | 0.28 | 0.24 | 0.807 | 0.963 | n.s. |
| from 2 - from 5 | 0.86 | 0.29 | 3.01 | 0.003 | 0.023 | * |
| from 2 - from 6 | 1.13 | 0.28 | 4.02 | < .001 | < .001 | *** |
| from 3 - from 4 | 0.20 | 0.28 | 0.71 | 0.479 | 0.927 | n.s. |
| from 3 - from 5 | 0.99 | 0.28 | 3.48 | < .001 | 0.006 | ** |
| from 3 - from 6 | 1.26 | 0.28 | 4.43 | < .001 | < .001 | *** |
| from 4 - from 5 | 0.79 | 0.28 | 2.85 | 0.004 | 0.030 | * |
| from 4 - from 6 | 1.06 | 0.27 | 3.88 | < .001 | 0.001 | ** |
| from 5 - from 6 | 0.27 | 0.28 | 0.98 | 0.328 | 0.908 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.18, *p* < .001, η²_G = 0.064
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -3.82 | 20 | = 0.008 | -0.59 [-1.26, -0.26] | medium | ** |
| from 1 vs from 3 | -3.41 | 20 | = 0.008 | -0.45 [-1.12, -0.15] | small | ** |
| from 1 vs from 4 | -3.48 | 20 | = 0.008 | -0.47 [-0.98, -0.08] | small | ** |
| from 1 vs from 5 | 0.02 | 20 | = 0.984 | 0.00 [-0.42, 0.44] | negligible | n.s. |
| from 1 vs from 6 | -0.02 | 20 | = 0.984 | -0.00 [-0.31, 0.54] | negligible | n.s. |
| from 2 vs from 3 | 0.78 | 20 | = 0.663 | 0.11 [-0.29, 0.63] | negligible | n.s. |
| from 2 vs from 4 | 0.43 | 20 | = 0.912 | 0.08 [-0.37, 0.51] | negligible | n.s. |
| from 2 vs from 5 | 3.79 | 20 | = 0.008 | 0.62 [0.30, 1.35] | medium | ** |
| from 2 vs from 6 | 3.45 | 20 | = 0.008 | 0.59 [0.21, 1.21] | medium | ** |
| from 3 vs from 4 | -0.21 | 20 | = 0.984 | -0.03 [-0.44, 0.45] | negligible | n.s. |
| from 3 vs from 5 | 2.83 | 20 | = 0.022 | 0.47 [0.10, 1.06] | small | * |
| from 3 vs from 6 | 2.42 | 20 | = 0.047 | 0.45 [0.09, 1.04] | small | * |
| from 4 vs from 5 | 2.96 | 20 | = 0.020 | 0.49 [0.04, 0.95] | small | * |
| from 4 vs from 6 | 2.36 | 20 | = 0.047 | 0.46 [0.09, 0.99] | small | * |
| from 5 vs from 6 | -0.05 | 20 | = 0.984 | -0.01 [-0.30, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 599.43, BIC = 621.41
- **from 2 vs from 1**: *β* = 5.57, *SE* = 2.442, *z* = 2.280, *p* = 0.023
- **from 3 vs from 1**: *β* = 5.98, *SE* = 2.554, *z* = 2.341, *p* = 0.019
- **from 4 vs from 1**: *β* = 7.23, *SE* = 2.675, *z* = 2.703, *p* = 0.007
- **from 5 vs from 1**: *β* = 5.61, *SE* = 2.447, *z* = 2.291, *p* = 0.022
- **from 6 vs from 1**: *β* = 7.15, *SE* = 2.513, *z* = 2.845, *p* = 0.004
- **SNR**: *β* = 0.51, *SE* = 0.438, *z* = 1.172, *p* = 0.241

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -5.57 | 2.44 | -2.28 | 0.023 | 0.234 | n.s. |
| from 1 - from 3 | -5.98 | 2.55 | -2.34 | 0.019 | 0.223 | n.s. |
| from 1 - from 4 | -7.23 | 2.67 | -2.70 | 0.007 | 0.092 | n.s. |
| from 1 - from 5 | -5.61 | 2.45 | -2.29 | 0.022 | 0.234 | n.s. |
| from 1 - from 6 | -7.15 | 2.51 | -2.84 | 0.004 | 0.065 | n.s. |
| from 2 - from 3 | -0.41 | 2.40 | -0.17 | 0.863 | 1.000 | n.s. |
| from 2 - from 4 | -1.66 | 2.54 | -0.66 | 0.512 | 0.999 | n.s. |
| from 2 - from 5 | -0.04 | 2.35 | -0.02 | 0.987 | 1.000 | n.s. |
| from 2 - from 6 | -1.58 | 2.36 | -0.67 | 0.503 | 0.999 | n.s. |
| from 3 - from 4 | -1.25 | 2.56 | -0.49 | 0.626 | 0.999 | n.s. |
| from 3 - from 5 | 0.37 | 2.45 | 0.15 | 0.878 | 1.000 | n.s. |
| from 3 - from 6 | -1.17 | 2.45 | -0.48 | 0.634 | 0.999 | n.s. |
| from 4 - from 5 | 1.62 | 2.55 | 0.64 | 0.524 | 0.999 | n.s. |
| from 4 - from 6 | 0.08 | 2.59 | 0.03 | 0.975 | 1.000 | n.s. |
| from 5 - from 6 | -1.54 | 2.44 | -0.63 | 0.527 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.77, *p* = 0.580, η²_G = 0.070
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.44 | 5 | = 0.802 | -0.28 [-1.06, 0.26] | small | n.s. |
| from 1 vs from 3 | -1.57 | 5 | = 0.680 | -0.67 [-1.23, 0.38] | medium | n.s. |
| from 1 vs from 4 | -1.23 | 5 | = 0.680 | -0.57 [-1.60, 0.25] | medium | n.s. |
| from 1 vs from 5 | -1.08 | 5 | = 0.702 | -0.31 [-1.31, 0.02] | small | n.s. |
| from 1 vs from 6 | -1.39 | 5 | = 0.680 | -0.39 [-1.72, -0.04] | small | n.s. |
| from 2 vs from 3 | -0.92 | 5 | = 0.753 | -0.43 [-0.55, 0.72] | small | n.s. |
| from 2 vs from 4 | -0.52 | 5 | = 0.802 | -0.29 [-0.88, 0.56] | small | n.s. |
| from 2 vs from 5 | 0.00 | 5 | = 1.000 | 0.00 [-0.63, 0.58] | negligible | n.s. |
| from 2 vs from 6 | -0.17 | 5 | = 0.934 | -0.09 [-1.07, 0.19] | negligible | n.s. |
| from 3 vs from 4 | 0.79 | 5 | = 0.775 | 0.22 [-0.51, 0.85] | small | n.s. |
| from 3 vs from 5 | 1.54 | 5 | = 0.680 | 0.52 [-0.67, 0.67] | medium | n.s. |
| from 3 vs from 6 | 1.35 | 5 | = 0.680 | 0.40 [-0.34, 1.04] | small | n.s. |
| from 4 vs from 5 | 1.46 | 5 | = 0.680 | 0.37 [-0.09, 1.51] | small | n.s. |
| from 4 vs from 6 | 0.60 | 5 | = 0.802 | 0.24 [-0.25, 1.27] | small | n.s. |
| from 5 vs from 6 | -0.42 | 5 | = 0.802 | -0.11 [-1.00, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 206.65, BIC = 228.64
- **from 2 vs from 1**: *β* = 0.22, *SE* = 0.213, *z* = 1.036, *p* = 0.300
- **from 3 vs from 1**: *β* = -0.25, *SE* = 0.223, *z* = -1.116, *p* = 0.265
- **from 4 vs from 1**: *β* = 0.20, *SE* = 0.234, *z* = 0.843, *p* = 0.399
- **from 5 vs from 1**: *β* = 0.47, *SE* = 0.211, *z* = 2.204, *p* = 0.028
- **from 6 vs from 1**: *β* = 0.92, *SE* = 0.220, *z* = 4.179, *p* < .001
- **SNR**: *β* = 0.32, *SE* = 0.042, *z* = 7.664, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.22 | 0.21 | -1.04 | 0.300 | 0.784 | n.s. |
| from 1 - from 3 | 0.25 | 0.22 | 1.12 | 0.265 | 0.784 | n.s. |
| from 1 - from 4 | -0.20 | 0.23 | -0.84 | 0.399 | 0.784 | n.s. |
| from 1 - from 5 | -0.47 | 0.21 | -2.20 | 0.028 | 0.222 | n.s. |
| from 1 - from 6 | -0.92 | 0.22 | -4.18 | < .001 | < .001 | *** |
| from 2 - from 3 | 0.47 | 0.21 | 2.25 | 0.025 | 0.222 | n.s. |
| from 2 - from 4 | 0.02 | 0.22 | 0.11 | 0.915 | 0.915 | n.s. |
| from 2 - from 5 | -0.25 | 0.21 | -1.19 | 0.232 | 0.784 | n.s. |
| from 2 - from 6 | -0.70 | 0.21 | -3.38 | < .001 | 0.009 | ** |
| from 3 - from 4 | -0.45 | 0.22 | -2.01 | 0.045 | 0.274 | n.s. |
| from 3 - from 5 | -0.71 | 0.21 | -3.36 | < .001 | 0.009 | ** |
| from 3 - from 6 | -1.17 | 0.21 | -5.47 | < .001 | < .001 | *** |
| from 4 - from 5 | -0.27 | 0.22 | -1.21 | 0.225 | 0.784 | n.s. |
| from 4 - from 6 | -0.72 | 0.23 | -3.20 | 0.001 | 0.015 | * |
| from 5 - from 6 | -0.46 | 0.21 | -2.13 | 0.034 | 0.239 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.82, *p* = 0.145, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.87 | 5 | = 0.709 | -0.23 [-0.93, 0.37] | small | n.s. |
| from 1 vs from 3 | -0.52 | 5 | = 0.786 | -0.17 [-0.63, 0.91] | negligible | n.s. |
| from 1 vs from 4 | -1.26 | 5 | = 0.563 | -0.42 [-1.15, 0.56] | small | n.s. |
| from 1 vs from 5 | -0.96 | 5 | = 0.709 | -0.40 [-1.29, 0.03] | small | n.s. |
| from 1 vs from 6 | -2.12 | 5 | = 0.435 | -0.80 [-1.42, 0.15] | large | n.s. |
| from 2 vs from 3 | 0.46 | 5 | = 0.786 | 0.07 [-0.11, 1.26] | negligible | n.s. |
| from 2 vs from 4 | -0.77 | 5 | = 0.711 | -0.13 [-0.79, 0.64] | negligible | n.s. |
| from 2 vs from 5 | -0.11 | 5 | = 0.913 | -0.05 [-0.78, 0.44] | negligible | n.s. |
| from 2 vs from 6 | -2.30 | 5 | = 0.435 | -0.47 [-1.29, 0.03] | small | n.s. |
| from 3 vs from 4 | -1.75 | 5 | = 0.487 | -0.22 [-1.78, -0.16] | small | n.s. |
| from 3 vs from 5 | -0.42 | 5 | = 0.786 | -0.15 [-1.41, 0.07] | negligible | n.s. |
| from 3 vs from 6 | -2.29 | 5 | = 0.435 | -0.59 [-1.62, -0.06] | medium | n.s. |
| from 4 vs from 5 | 0.36 | 5 | = 0.786 | 0.12 [-0.96, 0.49] | negligible | n.s. |
| from 4 vs from 6 | -1.64 | 5 | = 0.487 | -0.38 [-1.05, 0.41] | small | n.s. |
| from 5 vs from 6 | -1.34 | 5 | = 0.563 | -0.55 [-1.03, 0.35] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1116.74, BIC = 1141.37
- **from 2 vs from 1**: *β* = -1.93, *SE* = 8.758, *z* = -0.221, *p* = 0.825
- **from 3 vs from 1**: *β* = -2.66, *SE* = 8.742, *z* = -0.304, *p* = 0.761
- **from 4 vs from 1**: *β* = 2.00, *SE* = 8.747, *z* = 0.228, *p* = 0.820
- **from 5 vs from 1**: *β* = -4.75, *SE* = 8.902, *z* = -0.534, *p* = 0.593
- **from 6 vs from 1**: *β* = 0.90, *SE* = 8.763, *z* = 0.102, *p* = 0.919
- **SNR**: *β* = 0.11, *SE* = 0.623, *z* = 0.179, *p* = 0.858

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 1.93 | 8.76 | 0.22 | 0.825 | 1.000 | n.s. |
| from 1 - from 3 | 2.66 | 8.74 | 0.30 | 0.761 | 1.000 | n.s. |
| from 1 - from 4 | -2.00 | 8.75 | -0.23 | 0.820 | 1.000 | n.s. |
| from 1 - from 5 | 4.75 | 8.90 | 0.53 | 0.593 | 1.000 | n.s. |
| from 1 - from 6 | -0.89 | 8.76 | -0.10 | 0.919 | 1.000 | n.s. |
| from 2 - from 3 | 0.72 | 8.79 | 0.08 | 0.935 | 1.000 | n.s. |
| from 2 - from 4 | -3.93 | 8.75 | -0.45 | 0.653 | 1.000 | n.s. |
| from 2 - from 5 | 2.82 | 8.91 | 0.32 | 0.752 | 1.000 | n.s. |
| from 2 - from 6 | -2.83 | 8.81 | -0.32 | 0.748 | 1.000 | n.s. |
| from 3 - from 4 | -4.65 | 8.69 | -0.54 | 0.592 | 1.000 | n.s. |
| from 3 - from 5 | 2.10 | 8.91 | 0.24 | 0.814 | 1.000 | n.s. |
| from 3 - from 6 | -3.55 | 8.82 | -0.40 | 0.687 | 1.000 | n.s. |
| from 4 - from 5 | 6.75 | 8.81 | 0.77 | 0.444 | 1.000 | n.s. |
| from 4 - from 6 | 1.10 | 8.74 | 0.13 | 0.900 | 1.000 | n.s. |
| from 5 - from 6 | -5.65 | 8.87 | -0.64 | 0.524 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.13, *p* = 0.984, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.02 | 16 | = 0.980 | -0.01 [-0.46, 0.53] | negligible | n.s. |
| from 1 vs from 3 | 0.17 | 16 | = 0.978 | 0.05 [-0.42, 0.54] | negligible | n.s. |
| from 1 vs from 4 | -0.33 | 16 | = 0.978 | -0.07 [-0.58, 0.42] | negligible | n.s. |
| from 1 vs from 5 | 0.41 | 16 | = 0.978 | 0.14 [-0.41, 0.62] | negligible | n.s. |
| from 1 vs from 6 | 0.26 | 16 | = 0.978 | 0.09 [-0.44, 0.56] | negligible | n.s. |
| from 2 vs from 3 | 0.17 | 16 | = 0.978 | 0.06 [-0.55, 0.45] | negligible | n.s. |
| from 2 vs from 4 | -0.21 | 16 | = 0.978 | -0.06 [-0.56, 0.44] | negligible | n.s. |
| from 2 vs from 5 | 0.46 | 16 | = 0.978 | 0.14 [-0.40, 0.63] | negligible | n.s. |
| from 2 vs from 6 | 0.39 | 16 | = 0.978 | 0.09 [-0.42, 0.61] | negligible | n.s. |
| from 3 vs from 4 | -0.54 | 16 | = 0.978 | -0.13 [-0.73, 0.28] | negligible | n.s. |
| from 3 vs from 5 | 0.36 | 16 | = 0.978 | 0.09 [-0.43, 0.60] | negligible | n.s. |
| from 3 vs from 6 | 0.11 | 16 | = 0.978 | 0.04 [-0.56, 0.44] | negligible | n.s. |
| from 4 vs from 5 | 1.02 | 16 | = 0.978 | 0.22 [-0.35, 0.65] | small | n.s. |
| from 4 vs from 6 | 0.56 | 16 | = 0.978 | 0.16 [-0.48, 0.49] | negligible | n.s. |
| from 5 vs from 6 | -0.17 | 16 | = 0.978 | -0.05 [-0.61, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 412.84, BIC = 437.46
- **from 2 vs from 1**: *β* = 0.14, *SE* = 0.343, *z* = 0.408, *p* = 0.684
- **from 3 vs from 1**: *β* = -0.42, *SE* = 0.342, *z* = -1.227, *p* = 0.220
- **from 4 vs from 1**: *β* = -0.30, *SE* = 0.344, *z* = -0.873, *p* = 0.382
- **from 5 vs from 1**: *β* = -0.03, *SE* = 0.349, *z* = -0.079, *p* = 0.937
- **from 6 vs from 1**: *β* = 0.17, *SE* = 0.343, *z* = 0.483, *p* = 0.629
- **SNR**: *β* = 0.17, *SE* = 0.028, *z* = 6.038, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.14 | 0.34 | -0.41 | 0.684 | 0.998 | n.s. |
| from 1 - from 3 | 0.42 | 0.34 | 1.23 | 0.220 | 0.935 | n.s. |
| from 1 - from 4 | 0.30 | 0.34 | 0.87 | 0.382 | 0.987 | n.s. |
| from 1 - from 5 | 0.03 | 0.35 | 0.08 | 0.937 | 0.998 | n.s. |
| from 1 - from 6 | -0.17 | 0.34 | -0.48 | 0.629 | 0.998 | n.s. |
| from 2 - from 3 | 0.56 | 0.34 | 1.62 | 0.105 | 0.788 | n.s. |
| from 2 - from 4 | 0.44 | 0.34 | 1.28 | 0.200 | 0.931 | n.s. |
| from 2 - from 5 | 0.17 | 0.35 | 0.48 | 0.632 | 0.998 | n.s. |
| from 2 - from 6 | -0.03 | 0.35 | -0.07 | 0.941 | 0.998 | n.s. |
| from 3 - from 4 | -0.12 | 0.34 | -0.35 | 0.728 | 0.998 | n.s. |
| from 3 - from 5 | -0.39 | 0.35 | -1.12 | 0.262 | 0.952 | n.s. |
| from 3 - from 6 | -0.58 | 0.35 | -1.69 | 0.091 | 0.761 | n.s. |
| from 4 - from 5 | -0.27 | 0.35 | -0.79 | 0.430 | 0.989 | n.s. |
| from 4 - from 6 | -0.47 | 0.34 | -1.36 | 0.175 | 0.918 | n.s. |
| from 5 - from 6 | -0.19 | 0.35 | -0.56 | 0.577 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.977, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.20 | 16 | = 0.990 | -0.03 [-0.61, 0.39] | negligible | n.s. |
| from 1 vs from 3 | 0.49 | 16 | = 0.990 | 0.09 [-0.37, 0.60] | negligible | n.s. |
| from 1 vs from 4 | -0.01 | 16 | = 0.990 | -0.00 [-0.50, 0.49] | negligible | n.s. |
| from 1 vs from 5 | 0.23 | 16 | = 0.990 | 0.04 [-0.46, 0.57] | negligible | n.s. |
| from 1 vs from 6 | -0.09 | 16 | = 0.990 | -0.02 [-0.52, 0.47] | negligible | n.s. |
| from 2 vs from 3 | 1.17 | 16 | = 0.990 | 0.13 [-0.18, 0.84] | negligible | n.s. |
| from 2 vs from 4 | 0.23 | 16 | = 0.990 | 0.03 [-0.49, 0.51] | negligible | n.s. |
| from 2 vs from 5 | 0.66 | 16 | = 0.990 | 0.08 [-0.36, 0.68] | negligible | n.s. |
| from 2 vs from 6 | 0.09 | 16 | = 0.990 | 0.02 [-0.49, 0.54] | negligible | n.s. |
| from 3 vs from 4 | -0.87 | 16 | = 0.990 | -0.10 [-0.75, 0.26] | negligible | n.s. |
| from 3 vs from 5 | -0.39 | 16 | = 0.990 | -0.06 [-0.61, 0.42] | negligible | n.s. |
| from 3 vs from 6 | -0.52 | 16 | = 0.990 | -0.12 [-0.64, 0.36] | negligible | n.s. |
| from 4 vs from 5 | 0.24 | 16 | = 0.990 | 0.04 [-0.52, 0.47] | negligible | n.s. |
| from 4 vs from 6 | -0.07 | 16 | = 0.990 | -0.01 [-0.53, 0.44] | negligible | n.s. |
| from 5 vs from 6 | -0.28 | 16 | = 0.990 | -0.06 [-0.52, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed smaller amplitude than from 2 (*d* = -0.59)
  - from 1 showed smaller amplitude than from 3 (*d* = -0.45)
  - from 1 showed smaller amplitude than from 4 (*d* = -0.47)
  - from 2 showed greater amplitude than from 5 (*d* = 0.62)
  - from 2 showed greater amplitude than from 6 (*d* = 0.59)
  - from 3 showed greater amplitude than from 5 (*d* = 0.47)
  - from 3 showed greater amplitude than from 6 (*d* = 0.45)
  - from 4 showed greater amplitude than from 5 (*d* = 0.49)
  - from 4 showed greater amplitude than from 6 (*d* = 0.46)

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
