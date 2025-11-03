# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:36:49

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
| from 1 | 12 | 104.67 ms | 10.35 | 2.99 | [92.00, 116.00] |
| from 2 | 8 | 108.50 ms | 10.99 | 3.89 | [92.00, 116.00] |
| from 3 | 11 | 106.55 ms | 11.21 | 3.38 | [92.00, 116.00] |
| from 4 | 9 | 104.44 ms | 9.89 | 3.30 | [92.00, 116.00] |
| from 5 | 4 | 104.00 ms | 13.86 | 6.93 | [92.00, 116.00] |
| from 6 | 9 | 105.33 ms | 12.65 | 4.22 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 12 | 1.62 µV | 0.98 | 0.28 | [0.51, 3.93] |
| from 2 | 8 | 1.35 µV | 0.53 | 0.19 | [0.87, 2.45] |
| from 3 | 11 | 1.43 µV | 0.95 | 0.29 | [0.46, 3.36] |
| from 4 | 9 | 1.43 µV | 0.84 | 0.28 | [0.52, 2.53] |
| from 5 | 4 | 2.16 µV | 1.12 | 0.56 | [1.22, 3.76] |
| from 6 | 9 | 1.43 µV | 0.88 | 0.29 | [0.51, 3.07] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 173.00 ms | 18.28 | 3.73 | [144.00, 204.00] |
| from 2 | 23 | 175.30 ms | 17.17 | 3.58 | [144.00, 204.00] |
| from 3 | 22 | 171.45 ms | 16.67 | 3.55 | [144.00, 204.00] |
| from 4 | 24 | 175.00 ms | 16.98 | 3.47 | [144.00, 204.00] |
| from 5 | 23 | 173.22 ms | 13.98 | 2.92 | [144.00, 196.00] |
| from 6 | 24 | 173.50 ms | 16.16 | 3.30 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | -4.89 µV | 2.05 | 0.42 | [-9.98, -1.35] |
| from 2 | 23 | -4.64 µV | 1.73 | 0.36 | [-8.54, -1.45] |
| from 3 | 22 | -5.00 µV | 1.94 | 0.41 | [-9.13, -1.83] |
| from 4 | 24 | -4.84 µV | 2.05 | 0.42 | [-9.57, -1.72] |
| from 5 | 23 | -5.66 µV | 2.19 | 0.46 | [-9.69, -1.15] |
| from 6 | 24 | -5.42 µV | 2.08 | 0.42 | [-9.40, -2.21] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 15 | 107.20 ms | 8.58 | 2.22 | [96.00, 116.00] |
| from 2 | 15 | 108.00 ms | 9.20 | 2.37 | [92.00, 116.00] |
| from 3 | 16 | 107.00 ms | 9.41 | 2.35 | [92.00, 116.00] |
| from 4 | 13 | 109.85 ms | 5.57 | 1.54 | [100.00, 116.00] |
| from 5 | 15 | 106.93 ms | 9.85 | 2.54 | [92.00, 116.00] |
| from 6 | 12 | 111.67 ms | 5.52 | 1.59 | [104.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 15 | 2.11 µV | 1.69 | 0.44 | [0.43, 6.82] |
| from 2 | 15 | 2.17 µV | 1.73 | 0.45 | [0.61, 5.63] |
| from 3 | 16 | 1.94 µV | 1.54 | 0.39 | [0.41, 5.48] |
| from 4 | 13 | 2.11 µV | 1.55 | 0.43 | [0.34, 4.49] |
| from 5 | 15 | 2.25 µV | 1.05 | 0.27 | [0.84, 4.51] |
| from 6 | 12 | 2.81 µV | 1.61 | 0.46 | [1.25, 6.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 17 | 474.12 ms | 36.69 | 8.90 | [420.00, 532.00] |
| from 2 | 19 | 481.05 ms | 35.77 | 8.21 | [424.00, 532.00] |
| from 3 | 19 | 478.74 ms | 27.71 | 6.36 | [432.00, 532.00] |
| from 4 | 17 | 484.94 ms | 30.05 | 7.29 | [436.00, 532.00] |
| from 5 | 18 | 468.00 ms | 24.85 | 5.86 | [420.00, 524.00] |
| from 6 | 18 | 470.67 ms | 35.54 | 8.38 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 17 | 4.15 µV | 2.38 | 0.58 | [1.04, 9.68] |
| from 2 | 19 | 4.13 µV | 2.11 | 0.48 | [0.80, 7.14] |
| from 3 | 19 | 4.14 µV | 2.34 | 0.54 | [1.05, 9.05] |
| from 4 | 17 | 4.34 µV | 2.40 | 0.58 | [0.64, 8.07] |
| from 5 | 18 | 3.76 µV | 1.86 | 0.44 | [1.22, 6.53] |
| from 6 | 18 | 3.76 µV | 2.16 | 0.51 | [1.25, 8.95] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 403.29, BIC = 421.02
- **from 2 vs from 1**: *β* = 1.79, *SE* = 3.646, *z* = 0.491, *p* = 0.623
- **from 3 vs from 1**: *β* = 2.50, *SE* = 3.401, *z* = 0.735, *p* = 0.463
- **from 4 vs from 1**: *β* = 1.38, *SE* = 3.426, *z* = 0.402, *p* = 0.688
- **from 5 vs from 1**: *β* = -1.00, *SE* = 4.738, *z* = -0.212, *p* = 0.832
- **from 6 vs from 1**: *β* = -0.34, *SE* = 3.698, *z* = -0.093, *p* = 0.926
- **SNR**: *β* = -0.48, *SE* = 1.033, *z* = -0.461, *p* = 0.645

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -1.79 | 3.65 | -0.49 | 0.623 | 1.000 | n.s. |
| from 1 - from 3 | -2.50 | 3.40 | -0.73 | 0.463 | 1.000 | n.s. |
| from 1 - from 4 | -1.38 | 3.43 | -0.40 | 0.688 | 1.000 | n.s. |
| from 1 - from 5 | 1.00 | 4.74 | 0.21 | 0.832 | 1.000 | n.s. |
| from 1 - from 6 | 0.35 | 3.70 | 0.09 | 0.926 | 1.000 | n.s. |
| from 2 - from 3 | -0.71 | 3.64 | -0.19 | 0.846 | 1.000 | n.s. |
| from 2 - from 4 | 0.41 | 3.87 | 0.11 | 0.915 | 1.000 | n.s. |
| from 2 - from 5 | 2.79 | 5.21 | 0.54 | 0.592 | 1.000 | n.s. |
| from 2 - from 6 | 2.14 | 3.88 | 0.55 | 0.582 | 1.000 | n.s. |
| from 3 - from 4 | 1.12 | 3.47 | 0.32 | 0.747 | 1.000 | n.s. |
| from 3 - from 5 | 3.50 | 4.75 | 0.74 | 0.461 | 1.000 | n.s. |
| from 3 - from 6 | 2.84 | 3.48 | 0.82 | 0.413 | 1.000 | n.s. |
| from 4 - from 5 | 2.38 | 4.85 | 0.49 | 0.624 | 1.000 | n.s. |
| from 4 - from 6 | 1.72 | 3.84 | 0.45 | 0.653 | 1.000 | n.s. |
| from 5 - from 6 | -0.66 | 4.90 | -0.13 | 0.893 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 95.94, BIC = 113.67
- **from 2 vs from 1**: *β* = -0.06, *SE* = 0.179, *z* = -0.337, *p* = 0.736
- **from 3 vs from 1**: *β* = 0.05, *SE* = 0.169, *z* = 0.286, *p* = 0.775
- **from 4 vs from 1**: *β* = -0.08, *SE* = 0.169, *z* = -0.449, *p* = 0.653
- **from 5 vs from 1**: *β* = 0.30, *SE* = 0.237, *z* = 1.259, *p* = 0.208
- **from 6 vs from 1**: *β* = 0.20, *SE* = 0.183, *z* = 1.087, *p* = 0.277
- **SNR**: *β* = 0.23, *SE* = 0.052, *z* = 4.504, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.06 | 0.18 | 0.34 | 0.736 | 0.995 | n.s. |
| from 1 - from 3 | -0.05 | 0.17 | -0.29 | 0.775 | 0.995 | n.s. |
| from 1 - from 4 | 0.08 | 0.17 | 0.45 | 0.653 | 0.995 | n.s. |
| from 1 - from 5 | -0.30 | 0.24 | -1.26 | 0.208 | 0.923 | n.s. |
| from 1 - from 6 | -0.20 | 0.18 | -1.09 | 0.277 | 0.961 | n.s. |
| from 2 - from 3 | -0.11 | 0.18 | -0.61 | 0.543 | 0.991 | n.s. |
| from 2 - from 4 | 0.02 | 0.19 | 0.08 | 0.933 | 0.995 | n.s. |
| from 2 - from 5 | -0.36 | 0.26 | -1.38 | 0.166 | 0.906 | n.s. |
| from 2 - from 6 | -0.26 | 0.19 | -1.35 | 0.177 | 0.906 | n.s. |
| from 3 - from 4 | 0.12 | 0.17 | 0.73 | 0.463 | 0.987 | n.s. |
| from 3 - from 5 | -0.25 | 0.24 | -1.06 | 0.288 | 0.961 | n.s. |
| from 3 - from 6 | -0.15 | 0.17 | -0.89 | 0.375 | 0.977 | n.s. |
| from 4 - from 5 | -0.37 | 0.24 | -1.55 | 0.120 | 0.853 | n.s. |
| from 4 - from 6 | -0.28 | 0.19 | -1.46 | 0.143 | 0.885 | n.s. |
| from 5 - from 6 | 0.10 | 0.24 | 0.41 | 0.681 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1016.85, BIC = 1043.33
- **from 2 vs from 1**: *β* = 3.09, *SE* = 1.844, *z* = 1.678, *p* = 0.093
- **from 3 vs from 1**: *β* = 0.22, *SE* = 1.886, *z* = 0.117, *p* = 0.907
- **from 4 vs from 1**: *β* = 1.69, *SE* = 1.830, *z* = 0.921, *p* = 0.357
- **from 5 vs from 1**: *β* = 0.86, *SE* = 1.879, *z* = 0.457, *p* = 0.648
- **from 6 vs from 1**: *β* = 0.38, *SE* = 1.821, *z* = 0.207, *p* = 0.836
- **SNR**: *β* = 0.21, *SE* = 0.130, *z* = 1.631, *p* = 0.103

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -3.09 | 1.84 | -1.68 | 0.093 | 0.770 | n.s. |
| from 1 - from 3 | -0.22 | 1.89 | -0.12 | 0.907 | 0.999 | n.s. |
| from 1 - from 4 | -1.69 | 1.83 | -0.92 | 0.357 | 0.992 | n.s. |
| from 1 - from 5 | -0.86 | 1.88 | -0.46 | 0.648 | 0.999 | n.s. |
| from 1 - from 6 | -0.38 | 1.82 | -0.21 | 0.836 | 0.999 | n.s. |
| from 2 - from 3 | 2.87 | 1.90 | 1.52 | 0.130 | 0.857 | n.s. |
| from 2 - from 4 | 1.41 | 1.85 | 0.76 | 0.447 | 0.997 | n.s. |
| from 2 - from 5 | 2.24 | 1.90 | 1.18 | 0.239 | 0.962 | n.s. |
| from 2 - from 6 | 2.72 | 1.84 | 1.47 | 0.141 | 0.861 | n.s. |
| from 3 - from 4 | -1.47 | 1.87 | -0.78 | 0.433 | 0.997 | n.s. |
| from 3 - from 5 | -0.64 | 1.89 | -0.34 | 0.735 | 0.999 | n.s. |
| from 3 - from 6 | -0.16 | 1.88 | -0.08 | 0.933 | 0.999 | n.s. |
| from 4 - from 5 | 0.83 | 1.85 | 0.45 | 0.655 | 0.999 | n.s. |
| from 4 - from 6 | 1.31 | 1.82 | 0.72 | 0.473 | 0.997 | n.s. |
| from 5 - from 6 | 0.48 | 1.87 | 0.26 | 0.797 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.511, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.474 (ε = 0.655)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.88 | 21 | = 0.574 | -0.23 [-0.84, 0.06] | small | n.s. |
| from 1 vs from 3 | -0.56 | 21 | = 0.735 | -0.08 [-0.56, 0.33] | negligible | n.s. |
| from 1 vs from 4 | -1.48 | 21 | = 0.574 | -0.16 [-0.68, 0.18] | negligible | n.s. |
| from 1 vs from 5 | -0.80 | 21 | = 0.735 | -0.14 [-0.56, 0.31] | negligible | n.s. |
| from 1 vs from 6 | -0.77 | 21 | = 0.735 | -0.09 [-0.48, 0.37] | negligible | n.s. |
| from 2 vs from 3 | 1.60 | 21 | = 0.574 | 0.15 [-0.11, 0.80] | negligible | n.s. |
| from 2 vs from 4 | 0.55 | 21 | = 0.735 | 0.08 [-0.32, 0.55] | negligible | n.s. |
| from 2 vs from 5 | 0.83 | 21 | = 0.735 | 0.11 [-0.27, 0.62] | negligible | n.s. |
| from 2 vs from 6 | 1.62 | 21 | = 0.574 | 0.15 [-0.11, 0.78] | negligible | n.s. |
| from 3 vs from 4 | -0.65 | 21 | = 0.735 | -0.08 [-0.58, 0.31] | negligible | n.s. |
| from 3 vs from 5 | -0.57 | 21 | = 0.735 | -0.06 [-0.57, 0.32] | negligible | n.s. |
| from 3 vs from 6 | -0.12 | 21 | = 0.905 | -0.01 [-0.47, 0.42] | negligible | n.s. |
| from 4 vs from 5 | 0.15 | 21 | = 0.905 | 0.02 [-0.39, 0.48] | negligible | n.s. |
| from 4 vs from 6 | 0.63 | 21 | = 0.735 | 0.07 [-0.24, 0.61] | negligible | n.s. |
| from 5 vs from 6 | 0.37 | 21 | = 0.825 | 0.05 [-0.32, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 414.62, BIC = 441.09
- **from 2 vs from 1**: *β* = 0.41, *SE* = 0.218, *z* = 1.901, *p* = 0.057
- **from 3 vs from 1**: *β* = 0.20, *SE* = 0.223, *z* = 0.918, *p* = 0.359
- **from 4 vs from 1**: *β* = 0.16, *SE* = 0.216, *z* = 0.727, *p* = 0.467
- **from 5 vs from 1**: *β* = -0.54, *SE* = 0.222, *z* = -2.435, *p* = 0.015
- **from 6 vs from 1**: *β* = -0.49, *SE* = 0.215, *z* = -2.263, *p* = 0.024
- **SNR**: *β* = -0.07, *SE* = 0.015, *z* = -4.687, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.41 | 0.22 | -1.90 | 0.057 | 0.338 | n.s. |
| from 1 - from 3 | -0.20 | 0.22 | -0.92 | 0.359 | 0.883 | n.s. |
| from 1 - from 4 | -0.16 | 0.22 | -0.73 | 0.467 | 0.883 | n.s. |
| from 1 - from 5 | 0.54 | 0.22 | 2.44 | 0.015 | 0.126 | n.s. |
| from 1 - from 6 | 0.49 | 0.22 | 2.26 | 0.024 | 0.174 | n.s. |
| from 2 - from 3 | 0.21 | 0.22 | 0.94 | 0.349 | 0.883 | n.s. |
| from 2 - from 4 | 0.26 | 0.22 | 1.17 | 0.240 | 0.807 | n.s. |
| from 2 - from 5 | 0.96 | 0.22 | 4.26 | < .001 | < .001 | *** |
| from 2 - from 6 | 0.90 | 0.22 | 4.13 | < .001 | < .001 | *** |
| from 3 - from 4 | 0.05 | 0.22 | 0.21 | 0.831 | 0.963 | n.s. |
| from 3 - from 5 | 0.75 | 0.22 | 3.34 | < .001 | 0.011 | * |
| from 3 - from 6 | 0.69 | 0.22 | 3.12 | 0.002 | 0.020 | * |
| from 4 - from 5 | 0.70 | 0.22 | 3.19 | 0.001 | 0.017 | * |
| from 4 - from 6 | 0.64 | 0.22 | 2.99 | 0.003 | 0.028 | * |
| from 5 - from 6 | -0.05 | 0.22 | -0.25 | 0.806 | 0.963 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.65, *p* < .001, η²_G = 0.044
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -2.15 | 21 | = 0.105 | -0.24 [-0.86, 0.04] | small | n.s. |
| from 1 vs from 3 | -0.41 | 21 | = 0.795 | -0.04 [-0.53, 0.36] | negligible | n.s. |
| from 1 vs from 4 | -0.22 | 21 | = 0.889 | -0.03 [-0.47, 0.38] | negligible | n.s. |
| from 1 vs from 5 | 3.15 | 21 | = 0.015 | 0.39 [0.16, 1.11] | small | * |
| from 1 vs from 6 | 1.71 | 21 | = 0.147 | 0.26 [-0.06, 0.82] | small | n.s. |
| from 2 vs from 3 | 1.77 | 21 | = 0.147 | 0.20 [-0.08, 0.84] | small | n.s. |
| from 2 vs from 4 | 1.68 | 21 | = 0.147 | 0.21 [-0.15, 0.73] | small | n.s. |
| from 2 vs from 5 | 4.93 | 21 | = 0.001 | 0.65 [0.50, 1.60] | medium | ** |
| from 2 vs from 6 | 3.93 | 21 | = 0.006 | 0.52 [0.28, 1.27] | medium | ** |
| from 3 vs from 4 | 0.12 | 21 | = 0.906 | 0.01 [-0.42, 0.47] | negligible | n.s. |
| from 3 vs from 5 | 3.28 | 21 | = 0.015 | 0.44 [0.20, 1.19] | small | * |
| from 3 vs from 6 | 2.09 | 21 | = 0.105 | 0.31 [-0.02, 0.91] | small | n.s. |
| from 4 vs from 5 | 3.22 | 21 | = 0.015 | 0.42 [0.15, 1.09] | small | * |
| from 4 vs from 6 | 1.94 | 21 | = 0.124 | 0.29 [-0.01, 0.87] | small | n.s. |
| from 5 vs from 6 | -1.32 | 21 | = 0.253 | -0.13 [-0.65, 0.22] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 603.09, BIC = 625.18
- **from 2 vs from 1**: *β* = -0.29, *SE* = 2.311, *z* = -0.128, *p* = 0.898
- **from 3 vs from 1**: *β* = -0.84, *SE* = 2.281, *z* = -0.369, *p* = 0.712
- **from 4 vs from 1**: *β* = 1.56, *SE* = 2.394, *z* = 0.650, *p* = 0.516
- **from 5 vs from 1**: *β* = -0.89, *SE* = 2.300, *z* = -0.389, *p* = 0.697
- **from 6 vs from 1**: *β* = 2.77, *SE* = 2.455, *z* = 1.127, *p* = 0.260
- **SNR**: *β* = 0.12, *SE* = 0.182, *z* = 0.637, *p* = 0.524

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.29 | 2.31 | 0.13 | 0.898 | 0.999 | n.s. |
| from 1 - from 3 | 0.84 | 2.28 | 0.37 | 0.712 | 0.999 | n.s. |
| from 1 - from 4 | -1.56 | 2.39 | -0.65 | 0.516 | 0.997 | n.s. |
| from 1 - from 5 | 0.89 | 2.30 | 0.39 | 0.697 | 0.999 | n.s. |
| from 1 - from 6 | -2.77 | 2.46 | -1.13 | 0.260 | 0.973 | n.s. |
| from 2 - from 3 | 0.55 | 2.30 | 0.24 | 0.812 | 0.999 | n.s. |
| from 2 - from 4 | -1.85 | 2.41 | -0.77 | 0.443 | 0.995 | n.s. |
| from 2 - from 5 | 0.60 | 2.35 | 0.26 | 0.799 | 0.999 | n.s. |
| from 2 - from 6 | -3.06 | 2.44 | -1.25 | 0.210 | 0.954 | n.s. |
| from 3 - from 4 | -2.40 | 2.34 | -1.03 | 0.305 | 0.982 | n.s. |
| from 3 - from 5 | 0.05 | 2.28 | 0.02 | 0.981 | 0.999 | n.s. |
| from 3 - from 6 | -3.61 | 2.41 | -1.50 | 0.134 | 0.884 | n.s. |
| from 4 - from 5 | 2.45 | 2.41 | 1.02 | 0.310 | 0.982 | n.s. |
| from 4 - from 6 | -1.21 | 2.53 | -0.48 | 0.632 | 0.999 | n.s. |
| from 5 - from 6 | -3.66 | 2.44 | -1.50 | 0.134 | 0.884 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.446, η²_G = 0.057
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 1.00 | 5 | = 0.565 | 0.52 [-0.59, 0.68] | medium | n.s. |
| from 1 vs from 3 | nan | 5 | n/a | 0.00 [-0.64, 0.64] | negligible | n.s. |
| from 1 vs from 4 | 1.58 | 5 | = 0.406 | 0.27 [-1.15, 0.26] | small | n.s. |
| from 1 vs from 5 | 2.00 | 5 | = 0.406 | 0.47 [-0.42, 0.86] | small | n.s. |
| from 1 vs from 6 | 1.46 | 5 | = 0.406 | 0.35 [-1.04, 0.43] | small | n.s. |
| from 2 vs from 3 | -1.00 | 5 | = 0.565 | -0.52 [-0.59, 0.69] | medium | n.s. |
| from 2 vs from 4 | -0.76 | 5 | = 0.658 | -0.35 [-0.63, 0.72] | small | n.s. |
| from 2 vs from 5 | -0.44 | 5 | = 0.679 | -0.17 [-0.79, 0.56] | negligible | n.s. |
| from 2 vs from 6 | -0.70 | 5 | = 0.658 | -0.25 [-0.88, 0.47] | small | n.s. |
| from 3 vs from 4 | 1.58 | 5 | = 0.406 | 0.27 [-0.89, 0.40] | small | n.s. |
| from 3 vs from 5 | 2.00 | 5 | = 0.406 | 0.47 [-0.60, 0.67] | small | n.s. |
| from 3 vs from 6 | 1.46 | 5 | = 0.406 | 0.35 [-1.05, 0.34] | small | n.s. |
| from 4 vs from 5 | 1.58 | 5 | = 0.406 | 0.25 [-0.43, 1.03] | small | n.s. |
| from 4 vs from 6 | 0.54 | 5 | = 0.658 | 0.12 [-0.86, 0.68] | negligible | n.s. |
| from 5 vs from 6 | -0.54 | 5 | = 0.658 | -0.11 [-1.05, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 243.55, BIC = 265.64
- **from 2 vs from 1**: *β* = -0.23, *SE* = 0.263, *z* = -0.867, *p* = 0.386
- **from 3 vs from 1**: *β* = -0.19, *SE* = 0.260, *z* = -0.717, *p* = 0.474
- **from 4 vs from 1**: *β* = -0.16, *SE* = 0.272, *z* = -0.591, *p* = 0.554
- **from 5 vs from 1**: *β* = 0.07, *SE* = 0.262, *z* = 0.279, *p* = 0.781
- **from 6 vs from 1**: *β* = 0.35, *SE* = 0.278, *z* = 1.260, *p* = 0.208
- **SNR**: *β* = 0.11, *SE* = 0.022, *z* = 5.130, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.23 | 0.26 | 0.87 | 0.386 | 0.980 | n.s. |
| from 1 - from 3 | 0.19 | 0.26 | 0.72 | 0.474 | 0.980 | n.s. |
| from 1 - from 4 | 0.16 | 0.27 | 0.59 | 0.554 | 0.982 | n.s. |
| from 1 - from 5 | -0.07 | 0.26 | -0.28 | 0.781 | 0.998 | n.s. |
| from 1 - from 6 | -0.35 | 0.28 | -1.26 | 0.208 | 0.939 | n.s. |
| from 2 - from 3 | -0.04 | 0.26 | -0.16 | 0.874 | 0.998 | n.s. |
| from 2 - from 4 | -0.07 | 0.28 | -0.24 | 0.807 | 0.998 | n.s. |
| from 2 - from 5 | -0.30 | 0.27 | -1.12 | 0.263 | 0.965 | n.s. |
| from 2 - from 6 | -0.58 | 0.28 | -2.08 | 0.038 | 0.439 | n.s. |
| from 3 - from 4 | -0.03 | 0.27 | -0.10 | 0.923 | 0.998 | n.s. |
| from 3 - from 5 | -0.26 | 0.26 | -0.99 | 0.321 | 0.978 | n.s. |
| from 3 - from 6 | -0.54 | 0.27 | -1.96 | 0.050 | 0.512 | n.s. |
| from 4 - from 5 | -0.23 | 0.28 | -0.85 | 0.396 | 0.980 | n.s. |
| from 4 - from 6 | -0.51 | 0.29 | -1.78 | 0.075 | 0.639 | n.s. |
| from 5 - from 6 | -0.28 | 0.28 | -1.00 | 0.317 | 0.978 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.83, *p* = 0.538, η²_G = 0.045
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 0.19 | 5 | = 0.985 | 0.06 [-0.46, 0.82] | negligible | n.s. |
| from 1 vs from 3 | 0.67 | 5 | = 0.889 | 0.32 [-0.55, 0.72] | small | n.s. |
| from 1 vs from 4 | 0.94 | 5 | = 0.732 | 0.42 [-0.53, 0.82] | small | n.s. |
| from 1 vs from 5 | 1.06 | 5 | = 0.727 | 0.50 [-0.56, 0.72] | medium | n.s. |
| from 1 vs from 6 | 0.01 | 5 | = 0.995 | 0.00 [-0.80, 0.63] | negligible | n.s. |
| from 2 vs from 3 | 1.32 | 5 | = 0.727 | 0.25 [-0.52, 0.75] | small | n.s. |
| from 2 vs from 4 | 1.44 | 5 | = 0.727 | 0.35 [-0.57, 0.78] | small | n.s. |
| from 2 vs from 5 | 1.13 | 5 | = 0.727 | 0.42 [-0.61, 0.74] | small | n.s. |
| from 2 vs from 6 | -0.37 | 5 | = 0.909 | -0.06 [-1.05, 0.34] | negligible | n.s. |
| from 3 vs from 4 | 0.46 | 5 | = 0.909 | 0.09 [-0.68, 0.59] | negligible | n.s. |
| from 3 vs from 5 | 0.43 | 5 | = 0.909 | 0.13 [-0.93, 0.36] | negligible | n.s. |
| from 3 vs from 6 | -2.49 | 5 | = 0.727 | -0.33 [-1.95, -0.25] | small | n.s. |
| from 4 vs from 5 | 0.08 | 5 | = 0.995 | 0.03 [-1.11, 0.37] | negligible | n.s. |
| from 4 vs from 6 | -1.78 | 5 | = 0.727 | -0.44 [-1.59, 0.14] | small | n.s. |
| from 5 vs from 6 | -1.41 | 5 | = 0.727 | -0.54 [-1.01, 0.37] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1045.75, BIC = 1069.89
- **from 2 vs from 1**: *β* = 7.89, *SE* = 8.338, *z* = 0.947, *p* = 0.344
- **from 3 vs from 1**: *β* = 3.45, *SE* = 8.404, *z* = 0.410, *p* = 0.682
- **from 4 vs from 1**: *β* = 8.28, *SE* = 8.795, *z* = 0.941, *p* = 0.347
- **from 5 vs from 1**: *β* = -7.06, *SE* = 8.398, *z* = -0.840, *p* = 0.401
- **from 6 vs from 1**: *β* = -2.37, *SE* = 8.402, *z* = -0.282, *p* = 0.778
- **SNR**: *β* = 0.77, *SE* = 0.622, *z* = 1.239, *p* = 0.215

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -7.89 | 8.34 | -0.95 | 0.344 | 0.985 | n.s. |
| from 1 - from 3 | -3.45 | 8.40 | -0.41 | 0.682 | 0.993 | n.s. |
| from 1 - from 4 | -8.28 | 8.79 | -0.94 | 0.347 | 0.985 | n.s. |
| from 1 - from 5 | 7.06 | 8.40 | 0.84 | 0.401 | 0.985 | n.s. |
| from 1 - from 6 | 2.37 | 8.40 | 0.28 | 0.778 | 0.993 | n.s. |
| from 2 - from 3 | 4.44 | 8.15 | 0.55 | 0.585 | 0.993 | n.s. |
| from 2 - from 4 | -0.38 | 8.56 | -0.04 | 0.964 | 0.993 | n.s. |
| from 2 - from 5 | 14.95 | 8.25 | 1.81 | 0.070 | 0.663 | n.s. |
| from 2 - from 6 | 10.27 | 8.18 | 1.25 | 0.210 | 0.948 | n.s. |
| from 3 - from 4 | -4.83 | 8.35 | -0.58 | 0.563 | 0.993 | n.s. |
| from 3 - from 5 | 10.51 | 8.27 | 1.27 | 0.204 | 0.948 | n.s. |
| from 3 - from 6 | 5.82 | 8.23 | 0.71 | 0.479 | 0.990 | n.s. |
| from 4 - from 5 | 15.33 | 8.66 | 1.77 | 0.077 | 0.673 | n.s. |
| from 4 - from 6 | 10.65 | 8.65 | 1.23 | 0.218 | 0.948 | n.s. |
| from 5 - from 6 | -4.68 | 8.31 | -0.56 | 0.573 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.17, *p* = 0.330, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.04 | 15 | = 0.655 | -0.33 [-0.77, 0.28] | small | n.s. |
| from 1 vs from 3 | -0.85 | 15 | = 0.678 | -0.25 [-0.59, 0.44] | small | n.s. |
| from 1 vs from 4 | -1.64 | 15 | = 0.473 | -0.40 [-0.97, 0.14] | small | n.s. |
| from 1 vs from 5 | 0.20 | 15 | = 0.925 | 0.07 [-0.36, 0.67] | negligible | n.s. |
| from 1 vs from 6 | 0.17 | 15 | = 0.925 | 0.05 [-0.47, 0.56] | negligible | n.s. |
| from 2 vs from 3 | 0.42 | 15 | = 0.925 | 0.12 [-0.35, 0.65] | negligible | n.s. |
| from 2 vs from 4 | -0.21 | 15 | = 0.925 | -0.05 [-0.59, 0.48] | negligible | n.s. |
| from 2 vs from 5 | 1.47 | 15 | = 0.486 | 0.44 [-0.09, 0.98] | small | n.s. |
| from 2 vs from 6 | 1.62 | 15 | = 0.473 | 0.38 [-0.18, 0.85] | small | n.s. |
| from 3 vs from 4 | -0.77 | 15 | = 0.683 | -0.19 [-0.64, 0.39] | negligible | n.s. |
| from 3 vs from 5 | 1.10 | 15 | = 0.655 | 0.38 [-0.16, 0.86] | small | n.s. |
| from 3 vs from 6 | 0.97 | 15 | = 0.655 | 0.32 [-0.38, 0.62] | small | n.s. |
| from 4 vs from 5 | 2.00 | 15 | = 0.473 | 0.53 [-0.00, 1.10] | medium | n.s. |
| from 4 vs from 6 | 1.76 | 15 | = 0.473 | 0.46 [-0.12, 1.00] | small | n.s. |
| from 5 vs from 6 | -0.03 | 15 | = 0.978 | -0.01 [-0.64, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 350.72, BIC = 374.86
- **from 2 vs from 1**: *β* = 0.08, *SE* = 0.293, *z* = 0.282, *p* = 0.778
- **from 3 vs from 1**: *β* = -0.09, *SE* = 0.295, *z* = -0.308, *p* = 0.758
- **from 4 vs from 1**: *β* = -0.35, *SE* = 0.309, *z* = -1.142, *p* = 0.254
- **from 5 vs from 1**: *β* = -0.23, *SE* = 0.293, *z* = -0.787, *p* = 0.431
- **from 6 vs from 1**: *β* = -0.35, *SE* = 0.293, *z* = -1.206, *p* = 0.228
- **SNR**: *β* = 0.16, *SE* = 0.024, *z* = 6.840, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.08 | 0.29 | -0.28 | 0.778 | 0.997 | n.s. |
| from 1 - from 3 | 0.09 | 0.29 | 0.31 | 0.758 | 0.997 | n.s. |
| from 1 - from 4 | 0.35 | 0.31 | 1.14 | 0.254 | 0.970 | n.s. |
| from 1 - from 5 | 0.23 | 0.29 | 0.79 | 0.431 | 0.989 | n.s. |
| from 1 - from 6 | 0.35 | 0.29 | 1.21 | 0.228 | 0.965 | n.s. |
| from 2 - from 3 | 0.17 | 0.29 | 0.61 | 0.544 | 0.996 | n.s. |
| from 2 - from 4 | 0.43 | 0.30 | 1.45 | 0.148 | 0.894 | n.s. |
| from 2 - from 5 | 0.31 | 0.29 | 1.08 | 0.280 | 0.973 | n.s. |
| from 2 - from 6 | 0.44 | 0.29 | 1.52 | 0.128 | 0.872 | n.s. |
| from 3 - from 4 | 0.26 | 0.29 | 0.90 | 0.369 | 0.989 | n.s. |
| from 3 - from 5 | 0.14 | 0.29 | 0.48 | 0.629 | 0.997 | n.s. |
| from 3 - from 6 | 0.26 | 0.29 | 0.91 | 0.361 | 0.989 | n.s. |
| from 4 - from 5 | -0.12 | 0.30 | -0.40 | 0.687 | 0.997 | n.s. |
| from 4 - from 6 | 0.00 | 0.30 | 0.00 | 0.997 | 0.997 | n.s. |
| from 5 - from 6 | 0.12 | 0.29 | 0.42 | 0.671 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.09, *p* = 0.374, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.56 | 15 | = 0.769 | -0.11 [-0.64, 0.39] | negligible | n.s. |
| from 1 vs from 3 | -0.78 | 15 | = 0.769 | -0.15 [-0.72, 0.32] | negligible | n.s. |
| from 1 vs from 4 | -0.54 | 15 | = 0.769 | -0.10 [-0.67, 0.40] | negligible | n.s. |
| from 1 vs from 5 | 0.62 | 15 | = 0.769 | 0.14 [-0.37, 0.66] | negligible | n.s. |
| from 1 vs from 6 | 0.68 | 15 | = 0.769 | 0.16 [-0.38, 0.65] | negligible | n.s. |
| from 2 vs from 3 | -0.41 | 15 | = 0.792 | -0.05 [-0.55, 0.44] | negligible | n.s. |
| from 2 vs from 4 | 0.04 | 15 | = 0.966 | 0.01 [-0.52, 0.54] | negligible | n.s. |
| from 2 vs from 5 | 2.16 | 15 | = 0.357 | 0.27 [-0.07, 1.02] | small | n.s. |
| from 2 vs from 6 | 1.30 | 15 | = 0.607 | 0.28 [-0.22, 0.79] | small | n.s. |
| from 3 vs from 4 | 0.51 | 15 | = 0.769 | 0.05 [-0.37, 0.67] | negligible | n.s. |
| from 3 vs from 5 | 2.33 | 15 | = 0.357 | 0.32 [-0.00, 1.06] | small | n.s. |
| from 3 vs from 6 | 1.43 | 15 | = 0.607 | 0.32 [-0.21, 0.81] | small | n.s. |
| from 4 vs from 5 | 1.54 | 15 | = 0.607 | 0.25 [-0.19, 0.87] | small | n.s. |
| from 4 vs from 6 | 1.22 | 15 | = 0.607 | 0.26 [-0.24, 0.85] | small | n.s. |
| from 5 vs from 6 | 0.16 | 15 | = 0.937 | 0.04 [-0.50, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed greater amplitude than from 5 (*d* = 0.39)
  - from 2 showed greater amplitude than from 5 (*d* = 0.65)
  - from 2 showed greater amplitude than from 6 (*d* = 0.52)
  - from 3 showed greater amplitude than from 5 (*d* = 0.44)
  - from 4 showed greater amplitude than from 5 (*d* = 0.42)

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
