# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:21:57

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
| from 1 | 24 | 103.67 ms | 10.00 | 2.04 | [92.00, 116.00] |
| from 2 | 24 | 103.17 ms | 9.06 | 1.85 | [92.00, 116.00] |
| from 3 | 24 | 103.00 ms | 9.45 | 1.93 | [92.00, 116.00] |
| from 4 | 24 | 106.00 ms | 8.83 | 1.80 | [92.00, 116.00] |
| from 5 | 24 | 103.50 ms | 8.69 | 1.77 | [92.00, 116.00] |
| from 6 | 24 | 106.00 ms | 8.75 | 1.79 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | -0.48 µV | 1.19 | 0.24 | [-2.86, 1.44] |
| from 2 | 24 | -1.10 µV | 1.20 | 0.24 | [-4.40, 0.73] |
| from 3 | 24 | -1.15 µV | 1.23 | 0.25 | [-4.15, 0.33] |
| from 4 | 24 | -0.97 µV | 1.60 | 0.33 | [-5.63, 1.43] |
| from 5 | 24 | -1.94 µV | 1.41 | 0.29 | [-6.01, 0.69] |
| from 6 | 24 | -1.79 µV | 1.58 | 0.32 | [-6.83, 0.37] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 173.67 ms | 20.53 | 4.19 | [144.00, 208.00] |
| from 2 | 24 | 173.67 ms | 16.13 | 3.29 | [144.00, 208.00] |
| from 3 | 24 | 174.00 ms | 19.81 | 4.04 | [144.00, 208.00] |
| from 4 | 24 | 175.50 ms | 16.10 | 3.29 | [144.00, 208.00] |
| from 5 | 24 | 170.00 ms | 15.65 | 3.19 | [144.00, 208.00] |
| from 6 | 24 | 173.50 ms | 17.37 | 3.55 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | -5.75 µV | 2.35 | 0.48 | [-11.42, -1.92] |
| from 2 | 24 | -4.59 µV | 2.10 | 0.43 | [-8.63, 0.67] |
| from 3 | 24 | -4.94 µV | 2.04 | 0.42 | [-8.94, -1.67] |
| from 4 | 24 | -4.99 µV | 2.07 | 0.42 | [-9.86, -2.11] |
| from 5 | 24 | -5.73 µV | 2.27 | 0.46 | [-9.50, -1.21] |
| from 6 | 24 | -5.96 µV | 2.12 | 0.43 | [-10.13, -3.03] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 105.00 ms | 9.96 | 2.03 | [96.00, 120.00] |
| from 2 | 24 | 108.33 ms | 10.07 | 2.06 | [96.00, 120.00] |
| from 3 | 24 | 107.17 ms | 9.43 | 1.93 | [96.00, 120.00] |
| from 4 | 24 | 110.17 ms | 8.42 | 1.72 | [96.00, 120.00] |
| from 5 | 24 | 109.83 ms | 9.06 | 1.85 | [96.00, 120.00] |
| from 6 | 24 | 109.50 ms | 9.78 | 2.00 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 0.82 µV | 2.05 | 0.42 | [-5.14, 4.79] |
| from 2 | 24 | 1.49 µV | 1.85 | 0.38 | [-0.91, 5.42] |
| from 3 | 24 | 1.07 µV | 1.70 | 0.35 | [-1.00, 4.88] |
| from 4 | 24 | 1.15 µV | 1.95 | 0.40 | [-1.80, 5.46] |
| from 5 | 24 | 1.54 µV | 1.93 | 0.39 | [-3.12, 4.84] |
| from 6 | 24 | 1.74 µV | 2.25 | 0.46 | [-2.13, 7.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 483.67 ms | 31.52 | 6.43 | [428.00, 536.00] |
| from 2 | 24 | 487.17 ms | 37.78 | 7.71 | [424.00, 536.00] |
| from 3 | 24 | 484.33 ms | 33.24 | 6.78 | [432.00, 536.00] |
| from 4 | 24 | 487.00 ms | 35.61 | 7.27 | [424.00, 536.00] |
| from 5 | 24 | 483.83 ms | 30.27 | 6.18 | [432.00, 536.00] |
| from 6 | 24 | 480.33 ms | 35.52 | 7.25 | [424.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 3.86 µV | 3.41 | 0.70 | [-0.94, 12.24] |
| from 2 | 24 | 4.05 µV | 2.99 | 0.61 | [-1.02, 8.81] |
| from 3 | 24 | 3.61 µV | 3.25 | 0.66 | [-2.85, 9.87] |
| from 4 | 24 | 4.00 µV | 3.12 | 0.64 | [-0.80, 8.97] |
| from 5 | 24 | 3.72 µV | 3.20 | 0.65 | [-2.34, 10.98] |
| from 6 | 24 | 3.82 µV | 3.23 | 0.66 | [-3.08, 9.98] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 977.66, BIC = 1004.39
- **from 2 vs from 1**: *β* = -0.58, *SE* = 1.603, *z* = -0.362, *p* = 0.717
- **from 3 vs from 1**: *β* = -0.82, *SE* = 1.604, *z* = -0.510, *p* = 0.610
- **from 4 vs from 1**: *β* = 2.40, *SE* = 1.603, *z* = 1.497, *p* = 0.134
- **from 5 vs from 1**: *β* = 0.23, *SE* = 1.615, *z* = 0.139, *p* = 0.889
- **from 6 vs from 1**: *β* = 2.05, *SE* = 1.609, *z* = 1.277, *p* = 0.202
- **SNR**: *β* = -0.60, *SE* = 0.305, *z* = -1.980, *p* = 0.048

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.58 | 1.60 | 0.36 | 0.717 | 0.996 | n.s. |
| from 1 - from 3 | 0.82 | 1.60 | 0.51 | 0.610 | 0.996 | n.s. |
| from 1 - from 4 | -2.40 | 1.60 | -1.50 | 0.134 | 0.795 | n.s. |
| from 1 - from 5 | -0.22 | 1.61 | -0.14 | 0.889 | 0.996 | n.s. |
| from 1 - from 6 | -2.05 | 1.61 | -1.28 | 0.202 | 0.868 | n.s. |
| from 2 - from 3 | 0.24 | 1.60 | 0.15 | 0.883 | 0.996 | n.s. |
| from 2 - from 4 | -2.98 | 1.60 | -1.86 | 0.063 | 0.599 | n.s. |
| from 2 - from 5 | -0.81 | 1.62 | -0.50 | 0.619 | 0.996 | n.s. |
| from 2 - from 6 | -2.63 | 1.61 | -1.64 | 0.101 | 0.721 | n.s. |
| from 3 - from 4 | -3.22 | 1.61 | -2.00 | 0.045 | 0.500 | n.s. |
| from 3 - from 5 | -1.04 | 1.63 | -0.64 | 0.521 | 0.994 | n.s. |
| from 3 - from 6 | -2.87 | 1.60 | -1.79 | 0.073 | 0.629 | n.s. |
| from 4 - from 5 | 2.17 | 1.61 | 1.35 | 0.177 | 0.857 | n.s. |
| from 4 - from 6 | 0.35 | 1.61 | 0.21 | 0.830 | 0.996 | n.s. |
| from 5 - from 6 | -1.83 | 1.64 | -1.12 | 0.264 | 0.914 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.40, *p* = 0.231, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 0.23 | 23 | = 0.998 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| from 1 vs from 3 | 0.37 | 23 | = 0.998 | 0.07 [-0.35, 0.50] | negligible | n.s. |
| from 1 vs from 4 | -1.18 | 23 | = 0.472 | -0.25 [-0.67, 0.19] | small | n.s. |
| from 1 vs from 5 | 0.09 | 23 | = 0.998 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| from 1 vs from 6 | -1.66 | 23 | = 0.274 | -0.25 [-0.77, 0.09] | small | n.s. |
| from 2 vs from 3 | 0.11 | 23 | = 0.998 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| from 2 vs from 4 | -1.98 | 23 | = 0.226 | -0.32 [-0.84, 0.04] | small | n.s. |
| from 2 vs from 5 | -0.19 | 23 | = 0.998 | -0.04 [-0.46, 0.38] | negligible | n.s. |
| from 2 vs from 6 | -1.45 | 23 | = 0.342 | -0.32 [-0.73, 0.13] | small | n.s. |
| from 3 vs from 4 | -1.85 | 23 | = 0.231 | -0.33 [-0.82, 0.06] | small | n.s. |
| from 3 vs from 5 | -0.30 | 23 | = 0.998 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| from 3 vs from 6 | -2.04 | 23 | = 0.226 | -0.33 [-0.86, 0.02] | small | n.s. |
| from 4 vs from 5 | 2.01 | 23 | = 0.226 | 0.29 [-0.03, 0.85] | small | n.s. |
| from 4 vs from 6 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| from 5 vs from 6 | -2.01 | 23 | = 0.226 | -0.29 [-0.85, 0.03] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 451.76, BIC = 478.49
- **from 2 vs from 1**: *β* = -0.63, *SE* = 0.270, *z* = -2.347, *p* = 0.019
- **from 3 vs from 1**: *β* = -0.69, *SE* = 0.270, *z* = -2.574, *p* = 0.010
- **from 4 vs from 1**: *β* = -0.48, *SE* = 0.270, *z* = -1.781, *p* = 0.075
- **from 5 vs from 1**: *β* = -1.39, *SE* = 0.272, *z* = -5.106, *p* < .001
- **from 6 vs from 1**: *β* = -1.37, *SE* = 0.271, *z* = -5.043, *p* < .001
- **SNR**: *β* = -0.12, *SE* = 0.052, *z* = -2.209, *p* = 0.027

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.63 | 0.27 | 2.35 | 0.019 | 0.108 | n.s. |
| from 1 - from 3 | 0.70 | 0.27 | 2.57 | 0.010 | 0.087 | n.s. |
| from 1 - from 4 | 0.48 | 0.27 | 1.78 | 0.075 | 0.322 | n.s. |
| from 1 - from 5 | 1.39 | 0.27 | 5.11 | < .001 | < .001 | *** |
| from 1 - from 6 | 1.37 | 0.27 | 5.04 | < .001 | < .001 | *** |
| from 2 - from 3 | 0.06 | 0.27 | 0.23 | 0.819 | 0.967 | n.s. |
| from 2 - from 4 | -0.15 | 0.27 | -0.57 | 0.571 | 0.921 | n.s. |
| from 2 - from 5 | 0.76 | 0.27 | 2.77 | 0.006 | 0.061 | n.s. |
| from 2 - from 6 | 0.73 | 0.27 | 2.71 | 0.007 | 0.065 | n.s. |
| from 3 - from 4 | -0.21 | 0.27 | -0.79 | 0.427 | 0.893 | n.s. |
| from 3 - from 5 | 0.69 | 0.27 | 2.53 | 0.011 | 0.087 | n.s. |
| from 3 - from 6 | 0.67 | 0.27 | 2.48 | 0.013 | 0.088 | n.s. |
| from 4 - from 5 | 0.91 | 0.27 | 3.35 | < .001 | 0.011 | * |
| from 4 - from 6 | 0.89 | 0.27 | 3.26 | 0.001 | 0.013 | * |
| from 5 - from 6 | -0.02 | 0.28 | -0.08 | 0.935 | 0.967 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.71, *p* < .001, η²_G = 0.119
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 2.24 | 23 | = 0.053 | 0.52 [0.01, 0.90] | medium | n.s. |
| from 1 vs from 3 | 3.15 | 23 | = 0.017 | 0.55 [0.18, 1.11] | medium | * |
| from 1 vs from 4 | 1.96 | 23 | = 0.085 | 0.35 [-0.04, 0.84] | small | n.s. |
| from 1 vs from 5 | 5.29 | 23 | < .001 | 1.12 [0.55, 1.61] | large | *** |
| from 1 vs from 6 | 4.36 | 23 | = 0.002 | 0.94 [0.39, 1.39] | large | ** |
| from 2 vs from 3 | 0.16 | 23 | = 0.871 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| from 2 vs from 4 | -0.42 | 23 | = 0.725 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| from 2 vs from 5 | 2.98 | 23 | = 0.020 | 0.64 [0.15, 1.07] | medium | * |
| from 2 vs from 6 | 2.31 | 23 | = 0.050 | 0.49 [0.03, 0.92] | small | n.s. |
| from 3 vs from 4 | -0.67 | 23 | = 0.626 | -0.12 [-0.56, 0.29] | negligible | n.s. |
| from 3 vs from 5 | 2.87 | 23 | = 0.022 | 0.60 [0.13, 1.04] | medium | * |
| from 3 vs from 6 | 2.44 | 23 | = 0.043 | 0.46 [0.05, 0.95] | small | * |
| from 4 vs from 5 | 3.33 | 23 | = 0.015 | 0.64 [0.21, 1.15] | medium | * |
| from 4 vs from 6 | 2.65 | 23 | = 0.031 | 0.51 [0.09, 0.99] | medium | * |
| from 5 vs from 6 | -0.62 | 23 | = 0.626 | -0.10 [-0.55, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1147.08, BIC = 1173.81
- **from 2 vs from 1**: *β* = 0.24, *SE* = 2.830, *z* = 0.086, *p* = 0.931
- **from 3 vs from 1**: *β* = -0.20, *SE* = 2.844, *z* = -0.070, *p* = 0.944
- **from 4 vs from 1**: *β* = 1.73, *SE* = 2.827, *z* = 0.612, *p* = 0.541
- **from 5 vs from 1**: *β* = -3.79, *SE* = 2.827, *z* = -1.342, *p* = 0.180
- **from 6 vs from 1**: *β* = -0.01, *SE* = 2.828, *z* = -0.004, *p* = 0.997
- **SNR**: *β* = 0.37, *SE* = 0.221, *z* = 1.655, *p* = 0.098

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.24 | 2.83 | -0.09 | 0.931 | 1.000 | n.s. |
| from 1 - from 3 | 0.20 | 2.84 | 0.07 | 0.944 | 1.000 | n.s. |
| from 1 - from 4 | -1.73 | 2.83 | -0.61 | 0.541 | 0.999 | n.s. |
| from 1 - from 5 | 3.79 | 2.83 | 1.34 | 0.180 | 0.924 | n.s. |
| from 1 - from 6 | 0.01 | 2.83 | 0.00 | 0.997 | 1.000 | n.s. |
| from 2 - from 3 | 0.44 | 2.86 | 0.16 | 0.877 | 1.000 | n.s. |
| from 2 - from 4 | -1.49 | 2.83 | -0.52 | 0.600 | 0.999 | n.s. |
| from 2 - from 5 | 4.04 | 2.83 | 1.42 | 0.154 | 0.904 | n.s. |
| from 2 - from 6 | 0.26 | 2.83 | 0.09 | 0.928 | 1.000 | n.s. |
| from 3 - from 4 | -1.93 | 2.84 | -0.68 | 0.496 | 0.999 | n.s. |
| from 3 - from 5 | 3.59 | 2.84 | 1.27 | 0.205 | 0.924 | n.s. |
| from 3 - from 6 | -0.19 | 2.86 | -0.07 | 0.947 | 1.000 | n.s. |
| from 4 - from 5 | 5.52 | 2.83 | 1.95 | 0.051 | 0.541 | n.s. |
| from 4 - from 6 | 1.74 | 2.83 | 0.62 | 0.538 | 0.999 | n.s. |
| from 5 - from 6 | -3.78 | 2.83 | -1.34 | 0.182 | 0.924 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.77, *p* = 0.574, η²_G = 0.009
- Greenhouse-Geisser corrected: *p* = 0.514 (ε = 0.596)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| from 1 vs from 3 | -0.13 | 23 | = 1.000 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| from 1 vs from 4 | -0.47 | 23 | = 1.000 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| from 1 vs from 5 | 1.14 | 23 | = 0.788 | 0.20 [-0.20, 0.66] | small | n.s. |
| from 1 vs from 6 | 0.06 | 23 | = 1.000 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| from 2 vs from 3 | -0.10 | 23 | = 1.000 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| from 2 vs from 4 | -1.03 | 23 | = 0.788 | -0.11 [-0.64, 0.22] | negligible | n.s. |
| from 2 vs from 5 | 1.08 | 23 | = 0.788 | 0.23 [-0.21, 0.65] | small | n.s. |
| from 2 vs from 6 | 0.06 | 23 | = 1.000 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| from 3 vs from 4 | -0.48 | 23 | = 1.000 | -0.08 [-0.52, 0.33] | negligible | n.s. |
| from 3 vs from 5 | 1.48 | 23 | = 0.762 | 0.22 [-0.13, 0.73] | small | n.s. |
| from 3 vs from 6 | 0.30 | 23 | = 1.000 | 0.03 [-0.36, 0.48] | negligible | n.s. |
| from 4 vs from 5 | 1.62 | 23 | = 0.762 | 0.35 [-0.10, 0.76] | small | n.s. |
| from 4 vs from 6 | 0.68 | 23 | = 1.000 | 0.12 [-0.29, 0.56] | negligible | n.s. |
| from 5 vs from 6 | -1.71 | 23 | = 0.762 | -0.21 [-0.78, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 486.97, BIC = 513.70
- **from 2 vs from 1**: *β* = 1.08, *SE* = 0.281, *z* = 3.830, *p* < .001
- **from 3 vs from 1**: *β* = 0.98, *SE* = 0.283, *z* = 3.487, *p* < .001
- **from 4 vs from 1**: *β* = 0.80, *SE* = 0.281, *z* = 2.844, *p* = 0.004
- **from 5 vs from 1**: *β* = 0.06, *SE* = 0.281, *z* = 0.209, *p* = 0.834
- **from 6 vs from 1**: *β* = -0.26, *SE* = 0.281, *z* = -0.936, *p* = 0.349
- **SNR**: *β* = -0.12, *SE* = 0.022, *z* = -5.358, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -1.08 | 0.28 | -3.83 | < .001 | 0.002 | ** |
| from 1 - from 3 | -0.99 | 0.28 | -3.49 | < .001 | 0.005 | ** |
| from 1 - from 4 | -0.80 | 0.28 | -2.84 | 0.004 | 0.035 | * |
| from 1 - from 5 | -0.06 | 0.28 | -0.21 | 0.834 | 0.937 | n.s. |
| from 1 - from 6 | 0.26 | 0.28 | 0.94 | 0.349 | 0.858 | n.s. |
| from 2 - from 3 | 0.09 | 0.28 | 0.32 | 0.749 | 0.937 | n.s. |
| from 2 - from 4 | 0.28 | 0.28 | 0.99 | 0.323 | 0.858 | n.s. |
| from 2 - from 5 | 1.02 | 0.28 | 3.61 | < .001 | 0.003 | ** |
| from 2 - from 6 | 1.34 | 0.28 | 4.77 | < .001 | < .001 | *** |
| from 3 - from 4 | 0.19 | 0.28 | 0.66 | 0.507 | 0.880 | n.s. |
| from 3 - from 5 | 0.93 | 0.28 | 3.29 | 0.001 | 0.009 | ** |
| from 3 - from 6 | 1.25 | 0.28 | 4.40 | < .001 | < .001 | *** |
| from 4 - from 5 | 0.74 | 0.28 | 2.64 | 0.008 | 0.057 | n.s. |
| from 4 - from 6 | 1.06 | 0.28 | 3.78 | < .001 | 0.002 | ** |
| from 5 - from 6 | 0.32 | 0.28 | 1.14 | 0.253 | 0.826 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.37, *p* < .001, η²_G = 0.055
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -4.11 | 23 | = 0.005 | -0.52 [-1.33, -0.35] | medium | ** |
| from 1 vs from 3 | -3.10 | 23 | = 0.019 | -0.37 [-1.09, -0.17] | small | * |
| from 1 vs from 4 | -2.58 | 23 | = 0.032 | -0.34 [-0.98, -0.08] | small | * |
| from 1 vs from 5 | -0.07 | 23 | = 0.946 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| from 1 vs from 6 | 0.56 | 23 | = 0.670 | 0.09 [-0.31, 0.54] | negligible | n.s. |
| from 2 vs from 3 | 1.26 | 23 | = 0.329 | 0.17 [-0.17, 0.69] | negligible | n.s. |
| from 2 vs from 4 | 1.10 | 23 | = 0.383 | 0.19 [-0.20, 0.65] | negligible | n.s. |
| from 2 vs from 5 | 3.85 | 23 | = 0.005 | 0.52 [0.30, 1.27] | medium | ** |
| from 2 vs from 6 | 3.79 | 23 | = 0.005 | 0.65 [0.29, 1.25] | medium | ** |
| from 3 vs from 4 | 0.20 | 23 | = 0.906 | 0.02 [-0.38, 0.46] | negligible | n.s. |
| from 3 vs from 5 | 2.58 | 23 | = 0.032 | 0.37 [0.08, 0.98] | small | * |
| from 3 vs from 6 | 2.97 | 23 | = 0.021 | 0.49 [0.15, 1.07] | small | * |
| from 4 vs from 5 | 2.25 | 23 | = 0.057 | 0.34 [0.01, 0.90] | small | n.s. |
| from 4 vs from 6 | 2.65 | 23 | = 0.032 | 0.47 [0.09, 0.99] | small | * |
| from 5 vs from 6 | 0.79 | 23 | = 0.549 | 0.10 [-0.26, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1008.37, BIC = 1035.10
- **from 2 vs from 1**: *β* = 3.46, *SE* = 1.848, *z* = 1.875, *p* = 0.061
- **from 3 vs from 1**: *β* = 2.20, *SE* = 1.846, *z* = 1.192, *p* = 0.233
- **from 4 vs from 1**: *β* = 4.99, *SE* = 1.849, *z* = 2.698, *p* = 0.007
- **from 5 vs from 1**: *β* = 5.00, *SE* = 1.849, *z* = 2.705, *p* = 0.007
- **from 6 vs from 1**: *β* = 4.79, *SE* = 1.854, *z* = 2.584, *p* = 0.010
- **SNR**: *β* = 0.65, *SE* = 0.371, *z* = 1.739, *p* = 0.082

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -3.47 | 1.85 | -1.88 | 0.061 | 0.529 | n.s. |
| from 1 - from 3 | -2.20 | 1.85 | -1.19 | 0.233 | 0.880 | n.s. |
| from 1 - from 4 | -4.99 | 1.85 | -2.70 | 0.007 | 0.098 | n.s. |
| from 1 - from 5 | -5.00 | 1.85 | -2.70 | 0.007 | 0.098 | n.s. |
| from 1 - from 6 | -4.79 | 1.85 | -2.58 | 0.010 | 0.120 | n.s. |
| from 2 - from 3 | 1.26 | 1.85 | 0.68 | 0.494 | 0.974 | n.s. |
| from 2 - from 4 | -1.52 | 1.85 | -0.82 | 0.411 | 0.974 | n.s. |
| from 2 - from 5 | -1.53 | 1.85 | -0.83 | 0.406 | 0.974 | n.s. |
| from 2 - from 6 | -1.32 | 1.85 | -0.72 | 0.474 | 0.974 | n.s. |
| from 3 - from 4 | -2.79 | 1.85 | -1.51 | 0.132 | 0.783 | n.s. |
| from 3 - from 5 | -2.80 | 1.85 | -1.51 | 0.130 | 0.783 | n.s. |
| from 3 - from 6 | -2.59 | 1.85 | -1.40 | 0.162 | 0.797 | n.s. |
| from 4 - from 5 | -0.01 | 1.86 | -0.01 | 0.995 | 0.999 | n.s. |
| from 4 - from 6 | 0.20 | 1.87 | 0.11 | 0.915 | 0.999 | n.s. |
| from 5 - from 6 | 0.21 | 1.85 | 0.11 | 0.909 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.15, *p* = 0.064, η²_G = 0.036
- Greenhouse-Geisser corrected: *p* = 0.095 (ε = 0.660)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.24 | 23 | = 0.482 | -0.33 [-0.68, 0.18] | small | n.s. |
| from 1 vs from 3 | -1.16 | 23 | = 0.482 | -0.22 [-0.67, 0.19] | small | n.s. |
| from 1 vs from 4 | -2.39 | 23 | = 0.266 | -0.56 [-0.93, -0.04] | medium | n.s. |
| from 1 vs from 5 | -2.04 | 23 | = 0.266 | -0.51 [-0.86, 0.02] | medium | n.s. |
| from 1 vs from 6 | -2.13 | 23 | = 0.266 | -0.46 [-0.88, 0.01] | small | n.s. |
| from 2 vs from 3 | 0.59 | 23 | = 0.651 | 0.12 [-0.30, 0.54] | negligible | n.s. |
| from 2 vs from 4 | -1.04 | 23 | = 0.518 | -0.20 [-0.64, 0.22] | negligible | n.s. |
| from 2 vs from 5 | -0.70 | 23 | = 0.651 | -0.16 [-0.57, 0.28] | negligible | n.s. |
| from 2 vs from 6 | -0.62 | 23 | = 0.651 | -0.12 [-0.55, 0.30] | negligible | n.s. |
| from 3 vs from 4 | -1.79 | 23 | = 0.323 | -0.34 [-0.80, 0.07] | small | n.s. |
| from 3 vs from 5 | -1.46 | 23 | = 0.475 | -0.29 [-0.73, 0.13] | small | n.s. |
| from 3 vs from 6 | -1.30 | 23 | = 0.482 | -0.24 [-0.69, 0.17] | small | n.s. |
| from 4 vs from 5 | 0.32 | 23 | = 0.807 | 0.04 [-0.36, 0.49] | negligible | n.s. |
| from 4 vs from 6 | 0.70 | 23 | = 0.651 | 0.07 [-0.28, 0.57] | negligible | n.s. |
| from 5 vs from 6 | 0.23 | 23 | = 0.819 | 0.04 [-0.38, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 489.08, BIC = 515.80
- **from 2 vs from 1**: *β* = 0.70, *SE* = 0.286, *z* = 2.452, *p* = 0.014
- **from 3 vs from 1**: *β* = 0.26, *SE* = 0.285, *z* = 0.903, *p* = 0.367
- **from 4 vs from 1**: *β* = 0.29, *SE* = 0.286, *z* = 1.015, *p* = 0.310
- **from 5 vs from 1**: *β* = 0.75, *SE* = 0.286, *z* = 2.632, *p* = 0.008
- **from 6 vs from 1**: *β* = 0.97, *SE* = 0.287, *z* = 3.395, *p* = 0.001
- **SNR**: *β* = 0.13, *SE* = 0.061, *z* = 2.185, *p* = 0.029

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.70 | 0.29 | -2.45 | 0.014 | 0.158 | n.s. |
| from 1 - from 3 | -0.26 | 0.29 | -0.90 | 0.367 | 0.892 | n.s. |
| from 1 - from 4 | -0.29 | 0.29 | -1.02 | 0.310 | 0.892 | n.s. |
| from 1 - from 5 | -0.75 | 0.29 | -2.63 | 0.008 | 0.113 | n.s. |
| from 1 - from 6 | -0.97 | 0.29 | -3.40 | < .001 | 0.010 | * |
| from 2 - from 3 | 0.44 | 0.29 | 1.55 | 0.121 | 0.644 | n.s. |
| from 2 - from 4 | 0.41 | 0.29 | 1.43 | 0.153 | 0.687 | n.s. |
| from 2 - from 5 | -0.05 | 0.29 | -0.18 | 0.856 | 0.979 | n.s. |
| from 2 - from 6 | -0.27 | 0.29 | -0.96 | 0.339 | 0.892 | n.s. |
| from 3 - from 4 | -0.03 | 0.29 | -0.11 | 0.909 | 0.979 | n.s. |
| from 3 - from 5 | -0.49 | 0.29 | -1.73 | 0.083 | 0.581 | n.s. |
| from 3 - from 6 | -0.72 | 0.29 | -2.50 | 0.012 | 0.150 | n.s. |
| from 4 - from 5 | -0.46 | 0.29 | -1.61 | 0.108 | 0.641 | n.s. |
| from 4 - from 6 | -0.68 | 0.29 | -2.37 | 0.018 | 0.181 | n.s. |
| from 5 - from 6 | -0.22 | 0.29 | -0.77 | 0.439 | 0.892 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.73, *p* = 0.023, η²_G = 0.026
- Greenhouse-Geisser corrected: *p* = 0.042 (ε = 0.691)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -2.25 | 23 | = 0.128 | -0.35 [-0.90, -0.02] | small | n.s. |
| from 1 vs from 3 | -0.82 | 23 | = 0.523 | -0.13 [-0.59, 0.26] | negligible | n.s. |
| from 1 vs from 4 | -0.93 | 23 | = 0.493 | -0.16 [-0.62, 0.24] | negligible | n.s. |
| from 1 vs from 5 | -3.15 | 23 | = 0.039 | -0.36 [-1.11, -0.18] | small | * |
| from 1 vs from 6 | -3.09 | 23 | = 0.039 | -0.42 [-1.09, -0.17] | small | * |
| from 2 vs from 3 | 1.70 | 23 | = 0.258 | 0.24 [-0.09, 0.78] | small | n.s. |
| from 2 vs from 4 | 1.10 | 23 | = 0.480 | 0.18 [-0.20, 0.65] | negligible | n.s. |
| from 2 vs from 5 | -0.16 | 23 | = 0.875 | -0.02 [-0.45, 0.39] | negligible | n.s. |
| from 2 vs from 6 | -0.98 | 23 | = 0.493 | -0.12 [-0.63, 0.23] | negligible | n.s. |
| from 3 vs from 4 | -0.42 | 23 | = 0.728 | -0.04 [-0.51, 0.34] | negligible | n.s. |
| from 3 vs from 5 | -1.45 | 23 | = 0.343 | -0.26 [-0.73, 0.14] | small | n.s. |
| from 3 vs from 6 | -2.58 | 23 | = 0.083 | -0.33 [-0.98, -0.08] | small | n.s. |
| from 4 vs from 5 | -1.09 | 23 | = 0.480 | -0.20 [-0.65, 0.21] | small | n.s. |
| from 4 vs from 6 | -1.84 | 23 | = 0.235 | -0.28 [-0.81, 0.06] | small | n.s. |
| from 5 vs from 6 | -0.58 | 23 | = 0.651 | -0.09 [-0.54, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1404.65, BIC = 1431.38
- **from 2 vs from 1**: *β* = 3.42, *SE* = 7.597, *z* = 0.450, *p* = 0.653
- **from 3 vs from 1**: *β* = 1.34, *SE* = 7.636, *z* = 0.176, *p* = 0.860
- **from 4 vs from 1**: *β* = 4.36, *SE* = 7.687, *z* = 0.567, *p* = 0.571
- **from 5 vs from 1**: *β* = 0.43, *SE* = 7.602, *z* = 0.057, *p* = 0.955
- **from 6 vs from 1**: *β* = -3.11, *SE* = 7.600, *z* = -0.409, *p* = 0.682
- **SNR**: *β* = -0.50, *SE* = 0.574, *z* = -0.868, *p* = 0.385

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -3.42 | 7.60 | -0.45 | 0.653 | 1.000 | n.s. |
| from 1 - from 3 | -1.34 | 7.64 | -0.18 | 0.860 | 1.000 | n.s. |
| from 1 - from 4 | -4.36 | 7.69 | -0.57 | 0.571 | 1.000 | n.s. |
| from 1 - from 5 | -0.43 | 7.60 | -0.06 | 0.955 | 1.000 | n.s. |
| from 1 - from 6 | 3.11 | 7.60 | 0.41 | 0.682 | 1.000 | n.s. |
| from 2 - from 3 | 2.07 | 7.65 | 0.27 | 0.786 | 1.000 | n.s. |
| from 2 - from 4 | -0.94 | 7.70 | -0.12 | 0.903 | 1.000 | n.s. |
| from 2 - from 5 | 2.98 | 7.61 | 0.39 | 0.695 | 1.000 | n.s. |
| from 2 - from 6 | 6.53 | 7.60 | 0.86 | 0.391 | 0.999 | n.s. |
| from 3 - from 4 | -3.01 | 7.61 | -0.40 | 0.692 | 1.000 | n.s. |
| from 3 - from 5 | 0.91 | 7.61 | 0.12 | 0.905 | 1.000 | n.s. |
| from 3 - from 6 | 4.45 | 7.61 | 0.59 | 0.559 | 1.000 | n.s. |
| from 4 - from 5 | 3.92 | 7.65 | 0.51 | 0.608 | 1.000 | n.s. |
| from 4 - from 6 | 7.47 | 7.65 | 0.98 | 0.329 | 0.997 | n.s. |
| from 5 - from 6 | 3.54 | 7.60 | 0.47 | 0.641 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.21, *p* = 0.957, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.45 | 23 | = 0.984 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| from 1 vs from 3 | -0.07 | 23 | = 0.984 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| from 1 vs from 4 | -0.59 | 23 | = 0.984 | -0.10 [-0.54, 0.30] | negligible | n.s. |
| from 1 vs from 5 | -0.02 | 23 | = 0.984 | -0.01 [-0.43, 0.42] | negligible | n.s. |
| from 1 vs from 6 | 0.39 | 23 | = 0.984 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| from 2 vs from 3 | 0.31 | 23 | = 0.984 | 0.08 [-0.36, 0.49] | negligible | n.s. |
| from 2 vs from 4 | 0.02 | 23 | = 0.984 | 0.00 [-0.42, 0.43] | negligible | n.s. |
| from 2 vs from 5 | 0.46 | 23 | = 0.984 | 0.10 [-0.33, 0.52] | negligible | n.s. |
| from 2 vs from 6 | 1.06 | 23 | = 0.984 | 0.19 [-0.21, 0.64] | negligible | n.s. |
| from 3 vs from 4 | -0.32 | 23 | = 0.984 | -0.08 [-0.49, 0.36] | negligible | n.s. |
| from 3 vs from 5 | 0.07 | 23 | = 0.984 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| from 3 vs from 6 | 0.44 | 23 | = 0.984 | 0.12 [-0.33, 0.51] | negligible | n.s. |
| from 4 vs from 5 | 0.57 | 23 | = 0.984 | 0.10 [-0.31, 0.54] | negligible | n.s. |
| from 4 vs from 6 | 0.79 | 23 | = 0.984 | 0.19 [-0.26, 0.59] | negligible | n.s. |
| from 5 vs from 6 | 0.50 | 23 | = 0.984 | 0.11 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 540.83, BIC = 567.56
- **from 2 vs from 1**: *β* = 0.21, *SE* = 0.319, *z* = 0.645, *p* = 0.519
- **from 3 vs from 1**: *β* = -0.42, *SE* = 0.321, *z* = -1.323, *p* = 0.186
- **from 4 vs from 1**: *β* = -0.13, *SE* = 0.324, *z* = -0.390, *p* = 0.696
- **from 5 vs from 1**: *β* = -0.21, *SE* = 0.319, *z* = -0.651, *p* = 0.515
- **from 6 vs from 1**: *β* = -0.10, *SE* = 0.319, *z* = -0.321, *p* = 0.748
- **SNR**: *β* = 0.13, *SE* = 0.027, *z* = 4.720, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.21 | 0.32 | -0.64 | 0.519 | 0.996 | n.s. |
| from 1 - from 3 | 0.42 | 0.32 | 1.32 | 0.186 | 0.944 | n.s. |
| from 1 - from 4 | 0.13 | 0.32 | 0.39 | 0.696 | 0.997 | n.s. |
| from 1 - from 5 | 0.21 | 0.32 | 0.65 | 0.515 | 0.996 | n.s. |
| from 1 - from 6 | 0.10 | 0.32 | 0.32 | 0.748 | 0.997 | n.s. |
| from 2 - from 3 | 0.63 | 0.32 | 1.96 | 0.050 | 0.537 | n.s. |
| from 2 - from 4 | 0.33 | 0.32 | 1.02 | 0.306 | 0.988 | n.s. |
| from 2 - from 5 | 0.41 | 0.32 | 1.29 | 0.196 | 0.944 | n.s. |
| from 2 - from 6 | 0.31 | 0.32 | 0.96 | 0.335 | 0.988 | n.s. |
| from 3 - from 4 | -0.30 | 0.32 | -0.93 | 0.350 | 0.988 | n.s. |
| from 3 - from 5 | -0.22 | 0.32 | -0.68 | 0.498 | 0.996 | n.s. |
| from 3 - from 6 | -0.32 | 0.32 | -1.01 | 0.314 | 0.988 | n.s. |
| from 4 - from 5 | 0.08 | 0.32 | 0.25 | 0.800 | 0.997 | n.s. |
| from 4 - from 6 | -0.02 | 0.32 | -0.07 | 0.941 | 0.997 | n.s. |
| from 5 - from 6 | -0.11 | 0.32 | -0.33 | 0.741 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.818, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.745 (ε = 0.673)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.59 | 23 | = 0.887 | -0.06 [-0.54, 0.30] | negligible | n.s. |
| from 1 vs from 3 | 0.64 | 23 | = 0.887 | 0.08 [-0.29, 0.56] | negligible | n.s. |
| from 1 vs from 4 | -0.39 | 23 | = 0.887 | -0.04 [-0.50, 0.34] | negligible | n.s. |
| from 1 vs from 5 | 0.38 | 23 | = 0.887 | 0.04 [-0.35, 0.50] | negligible | n.s. |
| from 1 vs from 6 | 0.13 | 23 | = 0.895 | 0.01 [-0.40, 0.45] | negligible | n.s. |
| from 2 vs from 3 | 1.77 | 23 | = 0.887 | 0.14 [-0.07, 0.80] | negligible | n.s. |
| from 2 vs from 4 | 0.18 | 23 | = 0.895 | 0.02 [-0.39, 0.46] | negligible | n.s. |
| from 2 vs from 5 | 1.18 | 23 | = 0.887 | 0.10 [-0.19, 0.67] | negligible | n.s. |
| from 2 vs from 6 | 0.59 | 23 | = 0.887 | 0.07 [-0.30, 0.54] | negligible | n.s. |
| from 3 vs from 4 | -1.59 | 23 | = 0.887 | -0.12 [-0.76, 0.11] | negligible | n.s. |
| from 3 vs from 5 | -0.38 | 23 | = 0.887 | -0.03 [-0.50, 0.34] | negligible | n.s. |
| from 3 vs from 6 | -0.45 | 23 | = 0.887 | -0.06 [-0.52, 0.33] | negligible | n.s. |
| from 4 vs from 5 | 0.72 | 23 | = 0.887 | 0.09 [-0.28, 0.57] | negligible | n.s. |
| from 4 vs from 6 | 0.42 | 23 | = 0.887 | 0.06 [-0.34, 0.51] | negligible | n.s. |
| from 5 vs from 6 | -0.24 | 23 | = 0.895 | -0.03 [-0.47, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed greater amplitude than from 3 (*d* = 0.55)
  - from 1 showed greater amplitude than from 5 (*d* = 1.12)
  - from 1 showed greater amplitude than from 6 (*d* = 0.94)
  - from 2 showed greater amplitude than from 5 (*d* = 0.64)
  - from 3 showed greater amplitude than from 5 (*d* = 0.60)
  - from 3 showed greater amplitude than from 6 (*d* = 0.46)
  - from 4 showed greater amplitude than from 5 (*d* = 0.64)
  - from 4 showed greater amplitude than from 6 (*d* = 0.51)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed smaller amplitude than from 2 (*d* = -0.52)
  - from 1 showed smaller amplitude than from 3 (*d* = -0.37)
  - from 1 showed smaller amplitude than from 4 (*d* = -0.34)
  - from 2 showed greater amplitude than from 5 (*d* = 0.52)
  - from 2 showed greater amplitude than from 6 (*d* = 0.65)
  - from 3 showed greater amplitude than from 5 (*d* = 0.37)
  - from 3 showed greater amplitude than from 6 (*d* = 0.49)
  - from 4 showed greater amplitude than from 6 (*d* = 0.47)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.064)
**P1 amplitude:** Significant main effect of condition (*p* = 0.023). Post-hoc tests revealed:
  - from 1 showed smaller amplitude than from 5 (*d* = -0.36)
  - from 1 showed smaller amplitude than from 6 (*d* = -0.42)

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
