# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:46:02

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
| 1 to 4 | 12 | 107.67 ms | 9.72 | 2.81 | [96.00, 116.00] |
| 2 to 4 | 9 | 111.11 ms | 8.67 | 2.89 | [96.00, 116.00] |
| 3 to 4 | 9 | 110.67 ms | 8.72 | 2.91 | [96.00, 116.00] |
| 4 to 4 | 10 | 105.60 ms | 9.65 | 3.05 | [96.00, 116.00] |
| 5 to 4 | 7 | 106.29 ms | 9.48 | 3.58 | [96.00, 116.00] |
| 6 to 4 | 6 | 108.00 ms | 9.80 | 4.00 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 12 | 2.44 µV | 1.59 | 0.46 | [0.42, 6.01] |
| 2 to 4 | 9 | 1.65 µV | 1.12 | 0.37 | [0.48, 4.01] |
| 3 to 4 | 9 | 2.47 µV | 1.64 | 0.55 | [1.03, 5.81] |
| 4 to 4 | 10 | 1.88 µV | 1.29 | 0.41 | [0.58, 4.79] |
| 5 to 4 | 7 | 3.46 µV | 1.12 | 0.42 | [1.78, 5.14] |
| 6 to 4 | 6 | 3.35 µV | 0.68 | 0.28 | [2.29, 4.21] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | 172.73 ms | 16.41 | 3.50 | [144.00, 204.00] |
| 2 to 4 | 21 | 169.52 ms | 14.78 | 3.22 | [144.00, 196.00] |
| 3 to 4 | 23 | 167.13 ms | 17.64 | 3.68 | [144.00, 204.00] |
| 4 to 4 | 22 | 171.27 ms | 19.93 | 4.25 | [144.00, 204.00] |
| 5 to 4 | 22 | 174.73 ms | 18.74 | 3.99 | [144.00, 204.00] |
| 6 to 4 | 23 | 174.26 ms | 20.53 | 4.28 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | -6.84 µV | 2.96 | 0.63 | [-13.14, -2.67] |
| 2 to 4 | 21 | -6.78 µV | 2.60 | 0.57 | [-15.66, -3.83] |
| 3 to 4 | 23 | -5.90 µV | 2.05 | 0.43 | [-10.53, -2.95] |
| 4 to 4 | 22 | -5.95 µV | 3.12 | 0.67 | [-13.09, -1.82] |
| 5 to 4 | 22 | -6.21 µV | 2.96 | 0.63 | [-14.15, -1.51] |
| 6 to 4 | 23 | -6.02 µV | 2.84 | 0.59 | [-12.20, -1.79] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 103.69 ms | 9.16 | 2.54 | [92.00, 120.00] |
| 2 to 4 | 17 | 106.82 ms | 10.66 | 2.58 | [92.00, 120.00] |
| 3 to 4 | 14 | 106.86 ms | 9.34 | 2.50 | [92.00, 120.00] |
| 4 to 4 | 12 | 109.33 ms | 10.14 | 2.93 | [92.00, 120.00] |
| 5 to 4 | 14 | 108.86 ms | 10.07 | 2.69 | [92.00, 120.00] |
| 6 to 4 | 16 | 110.00 ms | 9.91 | 2.48 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 3.29 µV | 1.83 | 0.51 | [1.06, 6.92] |
| 2 to 4 | 17 | 3.23 µV | 2.03 | 0.49 | [1.12, 7.56] |
| 3 to 4 | 14 | 3.46 µV | 2.00 | 0.53 | [1.27, 7.39] |
| 4 to 4 | 12 | 3.32 µV | 1.89 | 0.55 | [0.96, 6.93] |
| 5 to 4 | 14 | 3.21 µV | 1.80 | 0.48 | [0.70, 6.01] |
| 6 to 4 | 16 | 4.02 µV | 1.79 | 0.45 | [1.39, 7.45] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 492.00 ms | 31.84 | 7.12 | [444.00, 540.00] |
| 2 to 4 | 19 | 496.63 ms | 33.82 | 7.76 | [436.00, 540.00] |
| 3 to 4 | 16 | 500.00 ms | 36.75 | 9.19 | [436.00, 540.00] |
| 4 to 4 | 12 | 484.33 ms | 31.98 | 9.23 | [436.00, 524.00] |
| 5 to 4 | 21 | 493.90 ms | 32.41 | 7.07 | [440.00, 540.00] |
| 6 to 4 | 18 | 493.78 ms | 32.96 | 7.77 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 5.67 µV | 3.12 | 0.70 | [1.76, 11.88] |
| 2 to 4 | 19 | 7.01 µV | 4.24 | 0.97 | [1.60, 17.43] |
| 3 to 4 | 16 | 6.99 µV | 3.08 | 0.77 | [2.36, 13.58] |
| 4 to 4 | 12 | 4.21 µV | 2.43 | 0.70 | [2.14, 8.96] |
| 5 to 4 | 21 | 6.21 µV | 2.91 | 0.63 | [2.03, 11.69] |
| 6 to 4 | 18 | 6.06 µV | 2.80 | 0.66 | [3.08, 13.11] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 390.99, BIC = 408.72
- **2 to 4 vs 1 to 4**: *β* = 4.87, *SE* = 3.411, *z* = 1.427, *p* = 0.154
- **3 to 4 vs 1 to 4**: *β* = 2.28, *SE* = 3.269, *z* = 0.697, *p* = 0.486
- **4 to 4 vs 1 to 4**: *β* = -2.04, *SE* = 3.105, *z* = -0.655, *p* = 0.512
- **5 to 4 vs 1 to 4**: *β* = -0.89, *SE* = 3.551, *z* = -0.252, *p* = 0.801
- **6 to 4 vs 1 to 4**: *β* = 0.77, *SE* = 3.715, *z* = 0.207, *p* = 0.836
- **SNR**: *β* = 0.01, *SE* = 1.010, *z* = 0.011, *p* = 0.991

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -4.87 | 3.41 | -1.43 | 0.154 | 0.886 | n.s. |
| 1 to 4 - 3 to 4 | -2.28 | 3.27 | -0.70 | 0.486 | 0.997 | n.s. |
| 1 to 4 - 4 to 4 | 2.03 | 3.11 | 0.66 | 0.512 | 0.997 | n.s. |
| 1 to 4 - 5 to 4 | 0.89 | 3.55 | 0.25 | 0.801 | 0.997 | n.s. |
| 1 to 4 - 6 to 4 | -0.77 | 3.71 | -0.21 | 0.836 | 0.997 | n.s. |
| 2 to 4 - 3 to 4 | 2.59 | 3.57 | 0.72 | 0.469 | 0.997 | n.s. |
| 2 to 4 - 4 to 4 | 6.90 | 3.42 | 2.02 | 0.044 | 0.489 | n.s. |
| 2 to 4 - 5 to 4 | 5.76 | 3.83 | 1.51 | 0.132 | 0.863 | n.s. |
| 2 to 4 - 6 to 4 | 4.10 | 3.91 | 1.05 | 0.294 | 0.978 | n.s. |
| 3 to 4 - 4 to 4 | 4.31 | 3.38 | 1.28 | 0.202 | 0.933 | n.s. |
| 3 to 4 - 5 to 4 | 3.17 | 3.76 | 0.84 | 0.399 | 0.994 | n.s. |
| 3 to 4 - 6 to 4 | 1.51 | 3.93 | 0.38 | 0.701 | 0.997 | n.s. |
| 4 to 4 - 5 to 4 | -1.14 | 3.77 | -0.30 | 0.762 | 0.997 | n.s. |
| 4 to 4 - 6 to 4 | -2.81 | 3.89 | -0.72 | 0.471 | 0.997 | n.s. |
| 5 to 4 - 6 to 4 | -1.66 | 4.19 | -0.40 | 0.692 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 154.90, BIC = 172.63
- **2 to 4 vs 1 to 4**: *β* = -0.25, *SE* = 0.380, *z* = -0.651, *p* = 0.515
- **3 to 4 vs 1 to 4**: *β* = 0.26, *SE* = 0.368, *z* = 0.717, *p* = 0.474
- **4 to 4 vs 1 to 4**: *β* = -0.10, *SE* = 0.357, *z* = -0.281, *p* = 0.779
- **5 to 4 vs 1 to 4**: *β* = 1.00, *SE* = 0.400, *z* = 2.491, *p* = 0.013
- **6 to 4 vs 1 to 4**: *β* = 1.16, *SE* = 0.424, *z* = 2.733, *p* = 0.006
- **SNR**: *β* = 0.77, *SE* = 0.111, *z* = 6.922, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 0.25 | 0.38 | 0.65 | 0.515 | 0.960 | n.s. |
| 1 to 4 - 3 to 4 | -0.26 | 0.37 | -0.72 | 0.474 | 0.960 | n.s. |
| 1 to 4 - 4 to 4 | 0.10 | 0.36 | 0.28 | 0.779 | 0.974 | n.s. |
| 1 to 4 - 5 to 4 | -1.00 | 0.40 | -2.49 | 0.013 | 0.120 | n.s. |
| 1 to 4 - 6 to 4 | -1.16 | 0.42 | -2.73 | 0.006 | 0.073 | n.s. |
| 2 to 4 - 3 to 4 | -0.51 | 0.40 | -1.29 | 0.197 | 0.784 | n.s. |
| 2 to 4 - 4 to 4 | -0.15 | 0.39 | -0.38 | 0.703 | 0.974 | n.s. |
| 2 to 4 - 5 to 4 | -1.24 | 0.43 | -2.89 | 0.004 | 0.052 | n.s. |
| 2 to 4 - 6 to 4 | -1.41 | 0.44 | -3.18 | 0.001 | 0.022 | * |
| 3 to 4 - 4 to 4 | 0.36 | 0.38 | 0.95 | 0.343 | 0.920 | n.s. |
| 3 to 4 - 5 to 4 | -0.73 | 0.42 | -1.74 | 0.082 | 0.495 | n.s. |
| 3 to 4 - 6 to 4 | -0.89 | 0.44 | -2.01 | 0.044 | 0.333 | n.s. |
| 4 to 4 - 5 to 4 | -1.10 | 0.43 | -2.56 | 0.010 | 0.110 | n.s. |
| 4 to 4 - 6 to 4 | -1.26 | 0.45 | -2.81 | 0.005 | 0.062 | n.s. |
| 5 to 4 - 6 to 4 | -0.16 | 0.47 | -0.34 | 0.732 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1101.14, BIC = 1127.16
- **2 to 4 vs 1 to 4**: *β* = -2.42, *SE* = 3.585, *z* = -0.674, *p* = 0.500
- **3 to 4 vs 1 to 4**: *β* = -6.57, *SE* = 3.509, *z* = -1.871, *p* = 0.061
- **4 to 4 vs 1 to 4**: *β* = -2.56, *SE* = 3.553, *z* = -0.722, *p* = 0.470
- **5 to 4 vs 1 to 4**: *β* = 1.89, *SE* = 3.539, *z* = 0.535, *p* = 0.593
- **6 to 4 vs 1 to 4**: *β* = -0.12, *SE* = 3.505, *z* = -0.034, *p* = 0.973
- **SNR**: *β* = 0.12, *SE* = 0.370, *z* = 0.314, *p* = 0.753

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 2.42 | 3.58 | 0.67 | 0.500 | 0.994 | n.s. |
| 1 to 4 - 3 to 4 | 6.57 | 3.51 | 1.87 | 0.061 | 0.588 | n.s. |
| 1 to 4 - 4 to 4 | 2.57 | 3.55 | 0.72 | 0.470 | 0.994 | n.s. |
| 1 to 4 - 5 to 4 | -1.89 | 3.54 | -0.53 | 0.593 | 0.994 | n.s. |
| 1 to 4 - 6 to 4 | 0.12 | 3.51 | 0.03 | 0.973 | 0.999 | n.s. |
| 2 to 4 - 3 to 4 | 4.15 | 3.56 | 1.17 | 0.243 | 0.943 | n.s. |
| 2 to 4 - 4 to 4 | 0.15 | 3.59 | 0.04 | 0.967 | 0.999 | n.s. |
| 2 to 4 - 5 to 4 | -4.31 | 3.59 | -1.20 | 0.230 | 0.943 | n.s. |
| 2 to 4 - 6 to 4 | -2.30 | 3.56 | -0.65 | 0.518 | 0.994 | n.s. |
| 3 to 4 - 4 to 4 | -4.00 | 3.52 | -1.14 | 0.256 | 0.943 | n.s. |
| 3 to 4 - 5 to 4 | -8.46 | 3.51 | -2.41 | 0.016 | 0.216 | n.s. |
| 3 to 4 - 6 to 4 | -6.45 | 3.48 | -1.85 | 0.064 | 0.588 | n.s. |
| 4 to 4 - 5 to 4 | -4.46 | 3.55 | -1.26 | 0.209 | 0.940 | n.s. |
| 4 to 4 - 6 to 4 | -2.45 | 3.50 | -0.70 | 0.485 | 0.994 | n.s. |
| 5 to 4 - 6 to 4 | 2.01 | 3.51 | 0.57 | 0.566 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.25, *p* = 0.293, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.75 | 17 | = 0.696 | 0.23 [-0.39, 0.55] | small | n.s. |
| 1 to 4 vs 3 to 4 | 1.94 | 17 | = 0.516 | 0.49 [-0.05, 0.88] | small | n.s. |
| 1 to 4 vs 4 to 4 | 0.98 | 17 | = 0.637 | 0.23 [-0.24, 0.71] | small | n.s. |
| 1 to 4 vs 5 to 4 | -0.49 | 17 | = 0.731 | -0.09 [-0.65, 0.27] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.16 | 17 | = 0.931 | 0.04 [-0.40, 0.51] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 1.30 | 17 | = 0.637 | 0.28 [-0.18, 0.75] | small | n.s. |
| 2 to 4 vs 4 to 4 | 0.09 | 17 | = 0.931 | 0.03 [-0.40, 0.53] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -1.05 | 17 | = 0.637 | -0.30 [-0.66, 0.28] | small | n.s. |
| 2 to 4 vs 6 to 4 | -0.60 | 17 | = 0.696 | -0.16 [-0.64, 0.31] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | -0.79 | 17 | = 0.696 | -0.22 [-0.67, 0.25] | small | n.s. |
| 3 to 4 vs 5 to 4 | -2.38 | 17 | = 0.441 | -0.54 [-1.03, -0.05] | medium | n.s. |
| 3 to 4 vs 6 to 4 | -1.60 | 17 | = 0.637 | -0.39 [-0.87, 0.05] | small | n.s. |
| 4 to 4 vs 5 to 4 | -1.23 | 17 | = 0.637 | -0.30 [-0.79, 0.17] | small | n.s. |
| 4 to 4 vs 6 to 4 | -1.05 | 17 | = 0.637 | -0.17 [-0.59, 0.32] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 0.60 | 17 | = 0.696 | 0.12 [-0.31, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 571.44, BIC = 597.46
- **2 to 4 vs 1 to 4**: *β* = 0.09, *SE* = 0.497, *z* = 0.190, *p* = 0.849
- **3 to 4 vs 1 to 4**: *β* = 0.53, *SE* = 0.486, *z* = 1.099, *p* = 0.272
- **4 to 4 vs 1 to 4**: *β* = 0.76, *SE* = 0.492, *z* = 1.544, *p* = 0.123
- **5 to 4 vs 1 to 4**: *β* = 0.45, *SE* = 0.491, *z* = 0.908, *p* = 0.364
- **6 to 4 vs 1 to 4**: *β* = 0.73, *SE* = 0.486, *z* = 1.505, *p* = 0.132
- **SNR**: *β* = -0.36, *SE* = 0.051, *z* = -7.104, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.09 | 0.50 | -0.19 | 0.849 | 0.997 | n.s. |
| 1 to 4 - 3 to 4 | -0.53 | 0.49 | -1.10 | 0.272 | 0.970 | n.s. |
| 1 to 4 - 4 to 4 | -0.76 | 0.49 | -1.54 | 0.123 | 0.859 | n.s. |
| 1 to 4 - 5 to 4 | -0.45 | 0.49 | -0.91 | 0.364 | 0.989 | n.s. |
| 1 to 4 - 6 to 4 | -0.73 | 0.49 | -1.51 | 0.132 | 0.863 | n.s. |
| 2 to 4 - 3 to 4 | -0.44 | 0.49 | -0.89 | 0.372 | 0.989 | n.s. |
| 2 to 4 - 4 to 4 | -0.67 | 0.50 | -1.34 | 0.181 | 0.925 | n.s. |
| 2 to 4 - 5 to 4 | -0.35 | 0.50 | -0.71 | 0.481 | 0.995 | n.s. |
| 2 to 4 - 6 to 4 | -0.64 | 0.49 | -1.29 | 0.196 | 0.928 | n.s. |
| 3 to 4 - 4 to 4 | -0.23 | 0.49 | -0.46 | 0.644 | 0.995 | n.s. |
| 3 to 4 - 5 to 4 | 0.09 | 0.49 | 0.18 | 0.855 | 0.997 | n.s. |
| 3 to 4 - 6 to 4 | -0.20 | 0.48 | -0.41 | 0.684 | 0.995 | n.s. |
| 4 to 4 - 5 to 4 | 0.31 | 0.49 | 0.64 | 0.522 | 0.995 | n.s. |
| 4 to 4 - 6 to 4 | 0.03 | 0.49 | 0.06 | 0.952 | 0.997 | n.s. |
| 5 to 4 - 6 to 4 | -0.29 | 0.49 | -0.59 | 0.556 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.37, *p* = 0.245, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.49 | 17 | = 0.467 | -0.30 [-0.61, 0.33] | small | n.s. |
| 1 to 4 vs 3 to 4 | -3.62 | 17 | = 0.032 | -0.65 [-0.88, 0.04] | medium | * |
| 1 to 4 vs 4 to 4 | -2.24 | 17 | = 0.291 | -0.32 [-1.06, -0.05] | small | n.s. |
| 1 to 4 vs 5 to 4 | -1.79 | 17 | = 0.405 | -0.32 [-0.74, 0.19] | small | n.s. |
| 1 to 4 vs 6 to 4 | -1.16 | 17 | = 0.520 | -0.26 [-0.62, 0.30] | small | n.s. |
| 2 to 4 vs 3 to 4 | -1.17 | 17 | = 0.520 | -0.34 [-0.84, 0.10] | small | n.s. |
| 2 to 4 vs 4 to 4 | -0.28 | 17 | = 0.966 | -0.06 [-0.68, 0.27] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.21 | 17 | = 0.966 | -0.05 [-0.59, 0.35] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 0.09 | 17 | = 0.992 | 0.03 [-0.54, 0.40] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | 1.04 | 17 | = 0.520 | 0.24 [-0.35, 0.57] | small | n.s. |
| 3 to 4 vs 5 to 4 | 1.10 | 17 | = 0.520 | 0.24 [-0.26, 0.66] | small | n.s. |
| 3 to 4 vs 6 to 4 | 1.70 | 17 | = 0.405 | 0.36 [-0.34, 0.55] | small | n.s. |
| 4 to 4 vs 5 to 4 | 0.01 | 17 | = 0.992 | 0.00 [-0.43, 0.51] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | 0.37 | 17 | = 0.966 | 0.08 [-0.44, 0.47] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 0.32 | 17 | = 0.966 | 0.08 [-0.45, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 624.47, BIC = 646.56
- **2 to 4 vs 1 to 4**: *β* = 3.63, *SE* = 2.638, *z* = 1.375, *p* = 0.169
- **3 to 4 vs 1 to 4**: *β* = 3.75, *SE* = 2.789, *z* = 1.346, *p* = 0.178
- **4 to 4 vs 1 to 4**: *β* = 4.78, *SE* = 2.836, *z* = 1.684, *p* = 0.092
- **5 to 4 vs 1 to 4**: *β* = 5.64, *SE* = 2.773, *z* = 2.036, *p* = 0.042
- **6 to 4 vs 1 to 4**: *β* = 6.33, *SE* = 2.642, *z* = 2.394, *p* = 0.017
- **SNR**: *β* = 0.56, *SE* = 0.607, *z* = 0.926, *p* = 0.355

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -3.63 | 2.64 | -1.38 | 0.169 | 0.892 | n.s. |
| 1 to 4 - 3 to 4 | -3.75 | 2.79 | -1.35 | 0.178 | 0.892 | n.s. |
| 1 to 4 - 4 to 4 | -4.78 | 2.84 | -1.68 | 0.092 | 0.716 | n.s. |
| 1 to 4 - 5 to 4 | -5.64 | 2.77 | -2.04 | 0.042 | 0.450 | n.s. |
| 1 to 4 - 6 to 4 | -6.32 | 2.64 | -2.39 | 0.017 | 0.223 | n.s. |
| 2 to 4 - 3 to 4 | -0.12 | 2.62 | -0.05 | 0.962 | 0.996 | n.s. |
| 2 to 4 - 4 to 4 | -1.15 | 2.76 | -0.42 | 0.677 | 0.996 | n.s. |
| 2 to 4 - 5 to 4 | -2.02 | 2.59 | -0.78 | 0.436 | 0.990 | n.s. |
| 2 to 4 - 6 to 4 | -2.70 | 2.55 | -1.06 | 0.290 | 0.967 | n.s. |
| 3 to 4 - 4 to 4 | -1.02 | 2.91 | -0.35 | 0.726 | 0.996 | n.s. |
| 3 to 4 - 5 to 4 | -1.89 | 2.76 | -0.69 | 0.493 | 0.991 | n.s. |
| 3 to 4 - 6 to 4 | -2.57 | 2.68 | -0.96 | 0.337 | 0.975 | n.s. |
| 4 to 4 - 5 to 4 | -0.87 | 2.87 | -0.30 | 0.762 | 0.996 | n.s. |
| 4 to 4 - 6 to 4 | -1.55 | 2.69 | -0.58 | 0.565 | 0.993 | n.s. |
| 5 to 4 - 6 to 4 | -0.68 | 2.67 | -0.25 | 0.799 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.465, η²_G = 0.096
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.92 | 2 | = 0.494 | 0.46 [-1.06, 0.33] | small | n.s. |
| 1 to 4 vs 3 to 4 | -1.00 | 2 | = 0.494 | -0.20 [-1.47, 0.21] | small | n.s. |
| 1 to 4 vs 4 to 4 | 1.00 | 2 | = 0.494 | 0.22 [-1.04, 0.53] | small | n.s. |
| 1 to 4 vs 5 to 4 | nan | 2 | n/a | 0.00 [-1.37, 0.28] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -1.00 | 2 | = 0.494 | -0.20 [-1.25, 0.19] | small | n.s. |
| 2 to 4 vs 3 to 4 | -1.39 | 2 | = 0.494 | -0.57 [-0.85, 0.59] | medium | n.s. |
| 2 to 4 vs 4 to 4 | -0.58 | 2 | = 0.622 | -0.35 [-0.98, 0.70] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.92 | 2 | = 0.494 | -0.46 [-0.85, 0.51] | small | n.s. |
| 2 to 4 vs 6 to 4 | -1.39 | 2 | = 0.494 | -0.57 [-0.79, 0.55] | medium | n.s. |
| 3 to 4 vs 4 to 4 | 1.00 | 2 | = 0.494 | 0.41 [-1.28, 0.84] | small | n.s. |
| 3 to 4 vs 5 to 4 | 1.00 | 2 | = 0.494 | 0.20 [-0.84, 0.84] | small | n.s. |
| 3 to 4 vs 6 to 4 | nan | 2 | n/a | 0.00 [-0.95, 0.50] | negligible | n.s. |
| 4 to 4 vs 5 to 4 | -1.00 | 2 | = 0.494 | -0.22 [-1.13, 0.73] | small | n.s. |
| 4 to 4 vs 6 to 4 | -1.00 | 2 | = 0.494 | -0.41 [-1.06, 0.33] | small | n.s. |
| 5 to 4 vs 6 to 4 | -1.00 | 2 | = 0.494 | -0.20 [-0.82, 0.62] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 283.09, BIC = 305.18
- **2 to 4 vs 1 to 4**: *β* = 0.35, *SE* = 0.379, *z* = 0.937, *p* = 0.349
- **3 to 4 vs 1 to 4**: *β* = 0.57, *SE* = 0.401, *z* = 1.429, *p* = 0.153
- **4 to 4 vs 1 to 4**: *β* = 0.06, *SE* = 0.408, *z* = 0.158, *p* = 0.874
- **5 to 4 vs 1 to 4**: *β* = 0.40, *SE* = 0.398, *z* = 0.999, *p* = 0.318
- **6 to 4 vs 1 to 4**: *β* = 0.61, *SE* = 0.380, *z* = 1.613, *p* = 0.107
- **SNR**: *β* = 0.79, *SE* = 0.082, *z* = 9.609, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.35 | 0.38 | -0.94 | 0.349 | 0.986 | n.s. |
| 1 to 4 - 3 to 4 | -0.57 | 0.40 | -1.43 | 0.153 | 0.902 | n.s. |
| 1 to 4 - 4 to 4 | -0.06 | 0.41 | -0.16 | 0.874 | 0.998 | n.s. |
| 1 to 4 - 5 to 4 | -0.40 | 0.40 | -1.00 | 0.318 | 0.985 | n.s. |
| 1 to 4 - 6 to 4 | -0.61 | 0.38 | -1.61 | 0.107 | 0.816 | n.s. |
| 2 to 4 - 3 to 4 | -0.22 | 0.37 | -0.58 | 0.560 | 0.993 | n.s. |
| 2 to 4 - 4 to 4 | 0.29 | 0.39 | 0.74 | 0.461 | 0.993 | n.s. |
| 2 to 4 - 5 to 4 | -0.04 | 0.37 | -0.12 | 0.908 | 0.998 | n.s. |
| 2 to 4 - 6 to 4 | -0.26 | 0.36 | -0.71 | 0.479 | 0.993 | n.s. |
| 3 to 4 - 4 to 4 | 0.51 | 0.42 | 1.22 | 0.222 | 0.951 | n.s. |
| 3 to 4 - 5 to 4 | 0.18 | 0.40 | 0.44 | 0.656 | 0.993 | n.s. |
| 3 to 4 - 6 to 4 | -0.04 | 0.39 | -0.10 | 0.918 | 0.998 | n.s. |
| 4 to 4 - 5 to 4 | -0.33 | 0.41 | -0.81 | 0.417 | 0.992 | n.s. |
| 4 to 4 - 6 to 4 | -0.55 | 0.39 | -1.42 | 0.157 | 0.902 | n.s. |
| 5 to 4 - 6 to 4 | -0.22 | 0.38 | -0.56 | 0.573 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.41, *p* = 0.022, η²_G = 0.366
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.45 | 2 | = 0.427 | -0.76 [-1.02, 0.36] | medium | n.s. |
| 1 to 4 vs 3 to 4 | 4.14 | 2 | = 0.174 | 1.13 [-0.53, 1.03] | large | n.s. |
| 1 to 4 vs 4 to 4 | 6.57 | 2 | = 0.168 | 1.26 [-0.79, 0.75] | large | n.s. |
| 1 to 4 vs 5 to 4 | 1.15 | 2 | = 0.504 | 0.76 [-0.64, 0.91] | medium | n.s. |
| 1 to 4 vs 6 to 4 | -0.26 | 2 | = 0.927 | -0.14 [-1.19, 0.23] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 3.29 | 2 | = 0.174 | 1.63 [-0.67, 0.76] | large | n.s. |
| 2 to 4 vs 4 to 4 | 5.29 | 2 | = 0.170 | 1.85 [-0.86, 0.81] | large | n.s. |
| 2 to 4 vs 5 to 4 | 3.80 | 2 | = 0.174 | 1.20 [-0.43, 0.93] | large | n.s. |
| 2 to 4 vs 6 to 4 | 11.15 | 2 | = 0.119 | 0.58 [-1.10, 0.30] | medium | n.s. |
| 3 to 4 vs 4 to 4 | -0.59 | 2 | = 0.771 | -0.17 [-1.36, 0.78] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -0.19 | 2 | = 0.927 | -0.11 [-0.60, 1.10] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | -2.25 | 2 | = 0.256 | -1.18 [-2.03, -0.21] | large | n.s. |
| 4 to 4 vs 5 to 4 | 0.01 | 2 | = 0.994 | 0.00 [-1.22, 0.67] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | -3.57 | 2 | = 0.174 | -1.30 [-0.97, 0.40] | large | n.s. |
| 5 to 4 vs 6 to 4 | -2.37 | 2 | = 0.256 | -0.82 [-1.34, 0.20] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1051.98, BIC = 1075.95
- **2 to 4 vs 1 to 4**: *β* = 3.97, *SE* = 9.629, *z* = 0.413, *p* = 0.680
- **3 to 4 vs 1 to 4**: *β* = 7.11, *SE* = 10.099, *z* = 0.704, *p* = 0.482
- **4 to 4 vs 1 to 4**: *β* = -4.78, *SE* = 11.328, *z* = -0.422, *p* = 0.673
- **5 to 4 vs 1 to 4**: *β* = 1.67, *SE* = 9.303, *z* = 0.179, *p* = 0.858
- **6 to 4 vs 1 to 4**: *β* = 0.95, *SE* = 9.761, *z* = 0.098, *p* = 0.922
- **SNR**: *β* = 0.48, *SE* = 1.160, *z* = 0.416, *p* = 0.678

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -3.97 | 9.63 | -0.41 | 0.680 | 1.000 | n.s. |
| 1 to 4 - 3 to 4 | -7.11 | 10.10 | -0.70 | 0.482 | 1.000 | n.s. |
| 1 to 4 - 4 to 4 | 4.78 | 11.33 | 0.42 | 0.673 | 1.000 | n.s. |
| 1 to 4 - 5 to 4 | -1.67 | 9.30 | -0.18 | 0.858 | 1.000 | n.s. |
| 1 to 4 - 6 to 4 | -0.96 | 9.76 | -0.10 | 0.922 | 1.000 | n.s. |
| 2 to 4 - 3 to 4 | -3.14 | 10.22 | -0.31 | 0.759 | 1.000 | n.s. |
| 2 to 4 - 4 to 4 | 8.75 | 11.75 | 0.74 | 0.457 | 1.000 | n.s. |
| 2 to 4 - 5 to 4 | 2.31 | 9.50 | 0.24 | 0.808 | 1.000 | n.s. |
| 2 to 4 - 6 to 4 | 3.02 | 10.00 | 0.30 | 0.763 | 1.000 | n.s. |
| 3 to 4 - 4 to 4 | 11.88 | 12.03 | 0.99 | 0.323 | 0.997 | n.s. |
| 3 to 4 - 5 to 4 | 5.44 | 10.00 | 0.54 | 0.586 | 1.000 | n.s. |
| 3 to 4 - 6 to 4 | 6.15 | 10.42 | 0.59 | 0.555 | 1.000 | n.s. |
| 4 to 4 - 5 to 4 | -6.44 | 11.27 | -0.57 | 0.567 | 1.000 | n.s. |
| 4 to 4 - 6 to 4 | -5.73 | 11.49 | -0.50 | 0.618 | 1.000 | n.s. |
| 5 to 4 - 6 to 4 | 0.71 | 9.63 | 0.07 | 0.941 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.741, η²_G = 0.059
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.68 | 7 | = 0.857 | -0.34 [-0.56, 0.44] | small | n.s. |
| 1 to 4 vs 3 to 4 | -0.87 | 7 | = 0.857 | -0.37 [-0.66, 0.45] | small | n.s. |
| 1 to 4 vs 4 to 4 | -0.12 | 7 | = 0.974 | -0.07 [-0.70, 0.57] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -1.24 | 7 | = 0.857 | -0.77 [-0.47, 0.46] | medium | n.s. |
| 1 to 4 vs 6 to 4 | -0.92 | 7 | = 0.857 | -0.47 [-0.47, 0.56] | small | n.s. |
| 2 to 4 vs 3 to 4 | 0.00 | 7 | = 1.000 | 0.00 [-0.66, 0.49] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | 0.70 | 7 | = 0.857 | 0.28 [-0.47, 0.89] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.59 | 7 | = 0.857 | -0.33 [-0.41, 0.55] | small | n.s. |
| 2 to 4 vs 6 to 4 | -0.39 | 7 | = 0.883 | -0.09 [-0.23, 0.82] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | 0.59 | 7 | = 0.857 | 0.30 [-0.67, 0.76] | small | n.s. |
| 3 to 4 vs 5 to 4 | -0.72 | 7 | = 0.857 | -0.35 [-0.50, 0.61] | small | n.s. |
| 3 to 4 vs 6 to 4 | -0.17 | 7 | = 0.974 | -0.10 [-0.45, 0.70] | negligible | n.s. |
| 4 to 4 vs 5 to 4 | -1.77 | 7 | = 0.857 | -0.67 [-0.83, 0.45] | medium | n.s. |
| 4 to 4 vs 6 to 4 | -1.18 | 7 | = 0.857 | -0.39 [-1.18, 0.31] | small | n.s. |
| 5 to 4 vs 6 to 4 | 0.46 | 7 | = 0.883 | 0.25 [-0.43, 0.57] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 480.63, BIC = 504.60
- **2 to 4 vs 1 to 4**: *β* = 0.83, *SE* = 0.591, *z* = 1.405, *p* = 0.160
- **3 to 4 vs 1 to 4**: *β* = 0.86, *SE* = 0.624, *z* = 1.381, *p* = 0.167
- **4 to 4 vs 1 to 4**: *β* = -0.46, *SE* = 0.696, *z* = -0.656, *p* = 0.512
- **5 to 4 vs 1 to 4**: *β* = 0.61, *SE* = 0.569, *z* = 1.079, *p* = 0.281
- **6 to 4 vs 1 to 4**: *β* = 0.72, *SE* = 0.601, *z* = 1.194, *p* = 0.233
- **SNR**: *β* = 0.52, *SE* = 0.076, *z* = 6.790, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.83 | 0.59 | -1.40 | 0.160 | 0.853 | n.s. |
| 1 to 4 - 3 to 4 | -0.86 | 0.62 | -1.38 | 0.167 | 0.853 | n.s. |
| 1 to 4 - 4 to 4 | 0.46 | 0.70 | 0.66 | 0.512 | 0.993 | n.s. |
| 1 to 4 - 5 to 4 | -0.61 | 0.57 | -1.08 | 0.281 | 0.928 | n.s. |
| 1 to 4 - 6 to 4 | -0.72 | 0.60 | -1.19 | 0.233 | 0.908 | n.s. |
| 2 to 4 - 3 to 4 | -0.03 | 0.63 | -0.05 | 0.961 | 0.999 | n.s. |
| 2 to 4 - 4 to 4 | 1.29 | 0.72 | 1.78 | 0.075 | 0.686 | n.s. |
| 2 to 4 - 5 to 4 | 0.22 | 0.58 | 0.37 | 0.710 | 0.999 | n.s. |
| 2 to 4 - 6 to 4 | 0.11 | 0.62 | 0.18 | 0.854 | 0.999 | n.s. |
| 3 to 4 - 4 to 4 | 1.32 | 0.74 | 1.79 | 0.074 | 0.686 | n.s. |
| 3 to 4 - 5 to 4 | 0.25 | 0.62 | 0.40 | 0.689 | 0.999 | n.s. |
| 3 to 4 - 6 to 4 | 0.14 | 0.65 | 0.22 | 0.824 | 0.999 | n.s. |
| 4 to 4 - 5 to 4 | -1.07 | 0.69 | -1.54 | 0.123 | 0.792 | n.s. |
| 4 to 4 - 6 to 4 | -1.17 | 0.70 | -1.67 | 0.095 | 0.727 | n.s. |
| 5 to 4 - 6 to 4 | -0.10 | 0.59 | -0.17 | 0.861 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.51, *p* = 0.048, η²_G = 0.132
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.27 | 7 | = 0.477 | -0.36 [-0.88, 0.14] | small | n.s. |
| 1 to 4 vs 3 to 4 | -0.64 | 7 | = 0.739 | -0.20 [-0.93, 0.21] | small | n.s. |
| 1 to 4 vs 4 to 4 | 1.82 | 7 | = 0.333 | 0.78 [-0.20, 1.14] | medium | n.s. |
| 1 to 4 vs 5 to 4 | 0.08 | 7 | = 0.941 | 0.02 [-0.77, 0.18] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.28 | 7 | = 0.900 | 0.08 [-0.52, 0.51] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 0.56 | 7 | = 0.741 | 0.23 [-0.49, 0.67] | small | n.s. |
| 2 to 4 vs 4 to 4 | 3.03 | 7 | = 0.143 | 1.29 [0.10, 1.69] | large | n.s. |
| 2 to 4 vs 5 to 4 | 1.31 | 7 | = 0.477 | 0.40 [-0.31, 0.67] | small | n.s. |
| 2 to 4 vs 6 to 4 | 1.24 | 7 | = 0.477 | 0.47 [-0.21, 0.84] | small | n.s. |
| 3 to 4 vs 4 to 4 | 3.39 | 7 | = 0.143 | 1.42 [0.27, 2.15] | large | n.s. |
| 3 to 4 vs 5 to 4 | 0.70 | 7 | = 0.739 | 0.25 [-0.39, 0.73] | small | n.s. |
| 3 to 4 vs 6 to 4 | 0.70 | 7 | = 0.739 | 0.33 [-0.31, 0.86] | small | n.s. |
| 4 to 4 vs 5 to 4 | -2.23 | 7 | = 0.305 | -0.84 [-1.37, 0.03] | large | n.s. |
| 4 to 4 vs 6 to 4 | -1.92 | 7 | = 0.333 | -0.73 [-1.39, 0.17] | medium | n.s. |
| 5 to 4 vs 6 to 4 | 0.21 | 7 | = 0.900 | 0.07 [-0.39, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.022) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.048) (no significant pairwise comparisons)

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
