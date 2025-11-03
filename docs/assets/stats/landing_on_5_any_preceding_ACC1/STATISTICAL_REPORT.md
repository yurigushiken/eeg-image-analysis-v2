# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:45:27

---

## 1. Analysis Overview

**Total Measurements:** 448
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
| 2 to 5 | 15 | 101.07 ms | 13.48 | 3.48 | [84.00, 112.00] |
| 3 to 5 | 9 | 103.11 ms | 9.96 | 3.32 | [88.00, 112.00] |
| 4 to 5 | 7 | 102.29 ms | 10.55 | 3.99 | [84.00, 112.00] |
| 5 to 5 | 9 | 96.00 ms | 12.49 | 4.16 | [84.00, 112.00] |
| 6 to 5 | 9 | 98.22 ms | 10.60 | 3.53 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 15 | 1.88 µV | 0.79 | 0.20 | [0.95, 3.30] |
| 3 to 5 | 9 | 3.60 µV | 2.17 | 0.72 | [1.02, 7.66] |
| 4 to 5 | 7 | 3.26 µV | 1.55 | 0.59 | [1.77, 5.87] |
| 5 to 5 | 9 | 2.27 µV | 1.58 | 0.53 | [0.42, 5.46] |
| 6 to 5 | 9 | 4.42 µV | 1.90 | 0.63 | [2.39, 7.38] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 172.83 ms | 20.43 | 4.17 | [132.00, 208.00] |
| 3 to 5 | 22 | 162.55 ms | 22.61 | 4.82 | [132.00, 208.00] |
| 4 to 5 | 22 | 169.45 ms | 21.58 | 4.60 | [132.00, 208.00] |
| 5 to 5 | 23 | 170.26 ms | 17.88 | 3.73 | [132.00, 196.00] |
| 6 to 5 | 15 | 176.80 ms | 25.62 | 6.62 | [132.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | -6.40 µV | 2.60 | 0.53 | [-13.83, -1.17] |
| 3 to 5 | 22 | -6.04 µV | 2.56 | 0.55 | [-13.75, -1.70] |
| 4 to 5 | 22 | -7.40 µV | 3.54 | 0.75 | [-16.53, -2.79] |
| 5 to 5 | 23 | -6.21 µV | 2.46 | 0.51 | [-12.06, -1.67] |
| 6 to 5 | 15 | -7.74 µV | 1.81 | 0.47 | [-10.73, -4.91] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 11 | 99.27 ms | 8.73 | 2.63 | [88.00, 108.00] |
| 3 to 5 | 13 | 98.77 ms | 8.39 | 2.33 | [88.00, 108.00] |
| 4 to 5 | 16 | 100.50 ms | 7.14 | 1.78 | [88.00, 108.00] |
| 5 to 5 | 15 | 101.33 ms | 8.09 | 2.09 | [88.00, 108.00] |
| 6 to 5 | 4 | 101.00 ms | 8.25 | 4.12 | [92.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 11 | 3.16 µV | 3.08 | 0.93 | [0.74, 11.63] |
| 3 to 5 | 13 | 3.02 µV | 1.45 | 0.40 | [1.16, 5.64] |
| 4 to 5 | 16 | 5.15 µV | 5.22 | 1.30 | [0.83, 19.20] |
| 5 to 5 | 15 | 2.59 µV | 1.56 | 0.40 | [0.35, 5.37] |
| 6 to 5 | 4 | 3.42 µV | 1.17 | 0.58 | [2.42, 5.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 19 | 461.47 ms | 68.35 | 15.68 | [364.00, 572.00] |
| 3 to 5 | 16 | 484.00 ms | 60.20 | 15.05 | [376.00, 564.00] |
| 4 to 5 | 15 | 479.20 ms | 69.42 | 17.92 | [360.00, 572.00] |
| 5 to 5 | 13 | 471.08 ms | 80.09 | 22.21 | [356.00, 564.00] |
| 6 to 5 | 12 | 514.00 ms | 61.20 | 17.67 | [376.00, 572.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 19 | 6.64 µV | 2.81 | 0.64 | [2.58, 11.71] |
| 3 to 5 | 16 | 6.62 µV | 3.31 | 0.83 | [2.85, 16.52] |
| 4 to 5 | 15 | 8.30 µV | 3.55 | 0.92 | [1.79, 13.88] |
| 5 to 5 | 13 | 4.04 µV | 1.15 | 0.32 | [1.49, 5.39] |
| 6 to 5 | 12 | 6.82 µV | 2.37 | 0.69 | [2.47, 10.24] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 391.76, BIC = 406.89
- **3 to 5 vs 2 to 5**: *β* = 2.55, *SE* = 5.408, *z* = 0.472, *p* = 0.637
- **4 to 5 vs 2 to 5**: *β* = 1.55, *SE* = 5.265, *z* = 0.295, *p* = 0.768
- **5 to 5 vs 2 to 5**: *β* = -4.95, *SE* = 4.776, *z* = -1.035, *p* = 0.301
- **6 to 5 vs 2 to 5**: *β* = -2.55, *SE* = 4.823, *z* = -0.528, *p* = 0.597
- **SNR**: *β* = -0.43, *SE* = 1.541, *z* = -0.281, *p* = 0.778

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -2.55 | 5.41 | -0.47 | 0.637 | 0.989 | n.s. |
| 2 to 5 - 4 to 5 | -1.56 | 5.26 | -0.30 | 0.768 | 0.989 | n.s. |
| 2 to 5 - 5 to 5 | 4.94 | 4.78 | 1.04 | 0.301 | 0.943 | n.s. |
| 2 to 5 - 6 to 5 | 2.55 | 4.82 | 0.53 | 0.597 | 0.989 | n.s. |
| 3 to 5 - 4 to 5 | 0.99 | 5.88 | 0.17 | 0.866 | 0.989 | n.s. |
| 3 to 5 - 5 to 5 | 7.49 | 5.61 | 1.34 | 0.182 | 0.866 | n.s. |
| 3 to 5 - 6 to 5 | 5.10 | 5.75 | 0.89 | 0.375 | 0.963 | n.s. |
| 4 to 5 - 5 to 5 | 6.50 | 5.69 | 1.14 | 0.253 | 0.928 | n.s. |
| 4 to 5 - 6 to 5 | 4.10 | 5.67 | 0.72 | 0.470 | 0.978 | n.s. |
| 5 to 5 - 6 to 5 | -2.40 | 5.36 | -0.45 | 0.655 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 171.86, BIC = 186.99
- **3 to 5 vs 2 to 5**: *β* = 0.76, *SE* = 0.517, *z* = 1.474, *p* = 0.141
- **4 to 5 vs 2 to 5**: *β* = 0.80, *SE* = 0.551, *z* = 1.452, *p* = 0.146
- **5 to 5 vs 2 to 5**: *β* = 0.11, *SE* = 0.492, *z* = 0.222, *p* = 0.825
- **6 to 5 vs 2 to 5**: *β* = 2.03, *SE* = 0.502, *z* = 4.044, *p* < .001
- **SNR**: *β* = 0.83, *SE* = 0.154, *z* = 5.390, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.76 | 0.52 | -1.47 | 0.141 | 0.597 | n.s. |
| 2 to 5 - 4 to 5 | -0.80 | 0.55 | -1.45 | 0.146 | 0.597 | n.s. |
| 2 to 5 - 5 to 5 | -0.11 | 0.49 | -0.22 | 0.825 | 0.969 | n.s. |
| 2 to 5 - 6 to 5 | -2.03 | 0.50 | -4.04 | < .001 | < .001 | *** |
| 3 to 5 - 4 to 5 | -0.04 | 0.60 | -0.06 | 0.950 | 0.969 | n.s. |
| 3 to 5 - 5 to 5 | 0.65 | 0.56 | 1.16 | 0.245 | 0.676 | n.s. |
| 3 to 5 - 6 to 5 | -1.27 | 0.56 | -2.27 | 0.023 | 0.170 | n.s. |
| 4 to 5 - 5 to 5 | 0.69 | 0.62 | 1.11 | 0.266 | 0.676 | n.s. |
| 4 to 5 - 6 to 5 | -1.23 | 0.59 | -2.10 | 0.036 | 0.225 | n.s. |
| 5 to 5 - 6 to 5 | -1.92 | 0.57 | -3.36 | < .001 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 917.23, BIC = 938.53
- **3 to 5 vs 2 to 5**: *β* = -8.93, *SE* = 4.040, *z* = -2.210, *p* = 0.027
- **4 to 5 vs 2 to 5**: *β* = -3.00, *SE* = 4.057, *z* = -0.740, *p* = 0.459
- **5 to 5 vs 2 to 5**: *β* = -2.13, *SE* = 3.990, *z* = -0.535, *p* = 0.593
- **6 to 5 vs 2 to 5**: *β* = 5.27, *SE* = 4.614, *z* = 1.141, *p* = 0.254
- **SNR**: *β* = 1.00, *SE* = 0.631, *z* = 1.590, *p* = 0.112

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 8.93 | 4.04 | 2.21 | 0.027 | 0.219 | n.s. |
| 2 to 5 - 4 to 5 | 3.00 | 4.06 | 0.74 | 0.459 | 0.842 | n.s. |
| 2 to 5 - 5 to 5 | 2.13 | 3.99 | 0.53 | 0.593 | 0.842 | n.s. |
| 2 to 5 - 6 to 5 | -5.27 | 4.61 | -1.14 | 0.254 | 0.690 | n.s. |
| 3 to 5 - 4 to 5 | -5.93 | 4.12 | -1.44 | 0.150 | 0.556 | n.s. |
| 3 to 5 - 5 to 5 | -6.80 | 4.06 | -1.68 | 0.094 | 0.507 | n.s. |
| 3 to 5 - 6 to 5 | -14.20 | 4.75 | -2.99 | 0.003 | 0.028 | * |
| 4 to 5 - 5 to 5 | -0.87 | 4.06 | -0.21 | 0.831 | 0.842 | n.s. |
| 4 to 5 - 6 to 5 | -8.27 | 4.79 | -1.72 | 0.085 | 0.507 | n.s. |
| 5 to 5 - 6 to 5 | -7.40 | 4.74 | -1.56 | 0.119 | 0.532 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.421, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.91 | 13 | = 0.628 | 0.24 [-0.04, 0.88] | small | n.s. |
| 2 to 5 vs 4 to 5 | 0.42 | 13 | = 0.756 | 0.10 [-0.37, 0.52] | negligible | n.s. |
| 2 to 5 vs 5 to 5 | 0.07 | 13 | = 0.947 | 0.01 [-0.36, 0.51] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.77 | 13 | = 0.628 | -0.22 [-0.76, 0.36] | small | n.s. |
| 3 to 5 vs 4 to 5 | -0.75 | 13 | = 0.628 | -0.15 [-0.70, 0.22] | negligible | n.s. |
| 3 to 5 vs 5 to 5 | -1.33 | 13 | = 0.628 | -0.24 [-0.86, 0.06] | small | n.s. |
| 3 to 5 vs 6 to 5 | -1.61 | 13 | = 0.628 | -0.44 [-1.03, 0.17] | small | n.s. |
| 4 to 5 vs 5 to 5 | -0.69 | 13 | = 0.628 | -0.09 [-0.43, 0.46] | negligible | n.s. |
| 4 to 5 vs 6 to 5 | -1.06 | 13 | = 0.628 | -0.31 [-0.87, 0.31] | small | n.s. |
| 5 to 5 vs 6 to 5 | -0.83 | 13 | = 0.628 | -0.24 [-0.81, 0.36] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 471.67, BIC = 492.98
- **3 to 5 vs 2 to 5**: *β* = 0.64, *SE* = 0.511, *z* = 1.257, *p* = 0.209
- **4 to 5 vs 2 to 5**: *β* = -0.78, *SE* = 0.513, *z* = -1.524, *p* = 0.127
- **5 to 5 vs 2 to 5**: *β* = 0.36, *SE* = 0.505, *z* = 0.707, *p* = 0.479
- **6 to 5 vs 2 to 5**: *β* = -1.38, *SE* = 0.583, *z* = -2.365, *p* = 0.018
- **SNR**: *β* = -0.28, *SE* = 0.077, *z* = -3.616, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.64 | 0.51 | -1.26 | 0.209 | 0.608 | n.s. |
| 2 to 5 - 4 to 5 | 0.78 | 0.51 | 1.52 | 0.127 | 0.494 | n.s. |
| 2 to 5 - 5 to 5 | -0.36 | 0.51 | -0.71 | 0.479 | 0.729 | n.s. |
| 2 to 5 - 6 to 5 | 1.38 | 0.58 | 2.37 | 0.018 | 0.119 | n.s. |
| 3 to 5 - 4 to 5 | 1.43 | 0.52 | 2.73 | 0.006 | 0.049 | * |
| 3 to 5 - 5 to 5 | 0.29 | 0.51 | 0.56 | 0.579 | 0.729 | n.s. |
| 3 to 5 - 6 to 5 | 2.02 | 0.60 | 3.37 | < .001 | 0.008 | ** |
| 4 to 5 - 5 to 5 | -1.14 | 0.51 | -2.22 | 0.026 | 0.148 | n.s. |
| 4 to 5 - 6 to 5 | 0.60 | 0.61 | 0.99 | 0.324 | 0.691 | n.s. |
| 5 to 5 - 6 to 5 | 1.74 | 0.60 | 2.90 | 0.004 | 0.033 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.18, *p* = 0.005, η²_G = 0.113
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.85 | 13 | = 0.587 | -0.19 [-0.67, 0.23] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 2.21 | 13 | = 0.091 | 0.52 [-0.12, 0.79] | medium | n.s. |
| 2 to 5 vs 5 to 5 | -0.60 | 13 | = 0.698 | -0.14 [-0.51, 0.35] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 1.66 | 13 | = 0.202 | 0.53 [-0.14, 1.02] | medium | n.s. |
| 3 to 5 vs 4 to 5 | 2.92 | 13 | = 0.060 | 0.73 [0.09, 1.08] | medium | n.s. |
| 3 to 5 vs 5 to 5 | 0.29 | 13 | = 0.779 | 0.06 [-0.25, 0.65] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 3.68 | 13 | = 0.028 | 0.92 [0.28, 1.69] | large | * |
| 4 to 5 vs 5 to 5 | -2.59 | 13 | = 0.060 | -0.68 [-0.85, 0.07] | medium | n.s. |
| 4 to 5 vs 6 to 5 | -0.47 | 13 | = 0.715 | -0.15 [-0.71, 0.45] | negligible | n.s. |
| 5 to 5 vs 6 to 5 | 2.55 | 13 | = 0.060 | 0.83 [0.04, 1.32] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 414.91, BIC = 431.53
- **3 to 5 vs 2 to 5**: *β* = -0.30, *SE* = 2.559, *z* = -0.117, *p* = 0.907
- **4 to 5 vs 2 to 5**: *β* = -0.02, *SE* = 2.558, *z* = -0.007, *p* = 0.994
- **5 to 5 vs 2 to 5**: *β* = 0.86, *SE* = 2.540, *z* = 0.340, *p* = 0.734
- **6 to 5 vs 2 to 5**: *β* = 2.79, *SE* = 3.957, *z* = 0.704, *p* = 0.481
- **SNR**: *β* = 1.16, *SE* = 0.774, *z* = 1.501, *p* = 0.133

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.30 | 2.56 | 0.12 | 0.907 | 0.999 | n.s. |
| 2 to 5 - 4 to 5 | 0.02 | 2.56 | 0.01 | 0.994 | 0.999 | n.s. |
| 2 to 5 - 5 to 5 | -0.86 | 2.54 | -0.34 | 0.734 | 0.999 | n.s. |
| 2 to 5 - 6 to 5 | -2.79 | 3.96 | -0.70 | 0.481 | 0.997 | n.s. |
| 3 to 5 - 4 to 5 | -0.28 | 2.41 | -0.12 | 0.907 | 0.999 | n.s. |
| 3 to 5 - 5 to 5 | -1.16 | 2.38 | -0.49 | 0.625 | 0.999 | n.s. |
| 3 to 5 - 6 to 5 | -3.09 | 3.77 | -0.82 | 0.413 | 0.995 | n.s. |
| 4 to 5 - 5 to 5 | -0.88 | 2.26 | -0.39 | 0.696 | 0.999 | n.s. |
| 4 to 5 - 6 to 5 | -2.80 | 3.88 | -0.72 | 0.470 | 0.997 | n.s. |
| 5 to 5 - 6 to 5 | -1.92 | 3.90 | -0.49 | 0.622 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 279.08, BIC = 295.70
- **3 to 5 vs 2 to 5**: *β* = -0.91, *SE* = 0.805, *z* = -1.131, *p* = 0.258
- **4 to 5 vs 2 to 5**: *β* = 0.92, *SE* = 0.810, *z* = 1.136, *p* = 0.256
- **5 to 5 vs 2 to 5**: *β* = -1.63, *SE* = 0.800, *z* = -2.043, *p* = 0.041
- **6 to 5 vs 2 to 5**: *β* = 0.88, *SE* = 1.239, *z* = 0.712, *p* = 0.477
- **SNR**: *β* = 1.63, *SE* = 0.243, *z* = 6.712, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.91 | 0.81 | 1.13 | 0.258 | 0.772 | n.s. |
| 2 to 5 - 4 to 5 | -0.92 | 0.81 | -1.14 | 0.256 | 0.772 | n.s. |
| 2 to 5 - 5 to 5 | 1.63 | 0.80 | 2.04 | 0.041 | 0.272 | n.s. |
| 2 to 5 - 6 to 5 | -0.88 | 1.24 | -0.71 | 0.477 | 0.772 | n.s. |
| 3 to 5 - 4 to 5 | -1.83 | 0.75 | -2.44 | 0.015 | 0.126 | n.s. |
| 3 to 5 - 5 to 5 | 0.72 | 0.75 | 0.97 | 0.332 | 0.772 | n.s. |
| 3 to 5 - 6 to 5 | -1.79 | 1.19 | -1.51 | 0.132 | 0.571 | n.s. |
| 4 to 5 - 5 to 5 | 2.55 | 0.71 | 3.57 | < .001 | 0.004 | ** |
| 4 to 5 - 6 to 5 | 0.04 | 1.21 | 0.03 | 0.975 | 0.975 | n.s. |
| 5 to 5 - 6 to 5 | -2.52 | 1.22 | -2.07 | 0.039 | 0.272 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 852.31, BIC = 870.85
- **3 to 5 vs 2 to 5**: *β* = 21.34, *SE* = 20.287, *z* = 1.052, *p* = 0.293
- **4 to 5 vs 2 to 5**: *β* = 20.99, *SE* = 20.546, *z* = 1.022, *p* = 0.307
- **5 to 5 vs 2 to 5**: *β* = 15.95, *SE* = 22.001, *z* = 0.725, *p* = 0.468
- **6 to 5 vs 2 to 5**: *β* = 60.22, *SE* = 22.664, *z* = 2.657, *p* = 0.008
- **SNR**: *β* = 3.46, *SE* = 3.012, *z* = 1.148, *p* = 0.251

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -21.34 | 20.29 | -1.05 | 0.293 | 0.875 | n.s. |
| 2 to 5 - 4 to 5 | -20.99 | 20.55 | -1.02 | 0.307 | 0.875 | n.s. |
| 2 to 5 - 5 to 5 | -15.95 | 22.00 | -0.73 | 0.468 | 0.920 | n.s. |
| 2 to 5 - 6 to 5 | -60.22 | 22.66 | -2.66 | 0.008 | 0.076 | n.s. |
| 3 to 5 - 4 to 5 | 0.35 | 21.48 | 0.02 | 0.987 | 0.993 | n.s. |
| 3 to 5 - 5 to 5 | 5.39 | 22.67 | 0.24 | 0.812 | 0.993 | n.s. |
| 3 to 5 - 6 to 5 | -38.88 | 23.10 | -1.68 | 0.092 | 0.538 | n.s. |
| 4 to 5 - 5 to 5 | 5.04 | 22.82 | 0.22 | 0.825 | 0.993 | n.s. |
| 4 to 5 - 6 to 5 | -39.23 | 23.28 | -1.69 | 0.092 | 0.538 | n.s. |
| 5 to 5 - 6 to 5 | -44.27 | 23.74 | -1.86 | 0.062 | 0.439 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.95, *p* = 0.134, η²_G = 0.169
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.37 | 6 | = 0.829 | -0.05 [-1.18, 0.06] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -2.23 | 6 | = 0.251 | -1.09 [-0.82, 0.35] | large | n.s. |
| 2 to 5 vs 5 to 5 | -0.28 | 6 | = 0.829 | -0.17 [-0.59, 0.68] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -1.94 | 6 | = 0.251 | -0.76 [-1.54, -0.01] | medium | n.s. |
| 3 to 5 vs 4 to 5 | -2.42 | 6 | = 0.251 | -1.29 [-0.75, 0.52] | large | n.s. |
| 3 to 5 vs 5 to 5 | -0.23 | 6 | = 0.829 | -0.14 [-0.72, 0.72] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.97 | 6 | = 0.251 | -0.83 [-1.98, -0.26] | large | n.s. |
| 4 to 5 vs 5 to 5 | 1.61 | 6 | = 0.316 | 0.84 [-0.60, 0.84] | large | n.s. |
| 4 to 5 vs 6 to 5 | 0.84 | 6 | = 0.619 | 0.31 [-0.93, 0.52] | small | n.s. |
| 5 to 5 vs 6 to 5 | -1.31 | 6 | = 0.395 | -0.54 [-1.09, 0.39] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 355.82, BIC = 374.36
- **3 to 5 vs 2 to 5**: *β* = 0.22, *SE* = 0.698, *z* = 0.320, *p* = 0.749
- **4 to 5 vs 2 to 5**: *β* = 1.95, *SE* = 0.707, *z* = 2.764, *p* = 0.006
- **5 to 5 vs 2 to 5**: *β* = -1.40, *SE* = 0.767, *z* = -1.820, *p* = 0.069
- **6 to 5 vs 2 to 5**: *β* = 1.04, *SE* = 0.786, *z* = 1.321, *p* = 0.187
- **SNR**: *β* = 0.48, *SE* = 0.107, *z* = 4.475, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.22 | 0.70 | -0.32 | 0.749 | 0.749 | n.s. |
| 2 to 5 - 4 to 5 | -1.95 | 0.71 | -2.76 | 0.006 | 0.045 | * |
| 2 to 5 - 5 to 5 | 1.40 | 0.77 | 1.82 | 0.069 | 0.300 | n.s. |
| 2 to 5 - 6 to 5 | -1.04 | 0.79 | -1.32 | 0.187 | 0.562 | n.s. |
| 3 to 5 - 4 to 5 | -1.73 | 0.74 | -2.35 | 0.019 | 0.126 | n.s. |
| 3 to 5 - 5 to 5 | 1.62 | 0.79 | 2.06 | 0.040 | 0.216 | n.s. |
| 3 to 5 - 6 to 5 | -0.81 | 0.79 | -1.03 | 0.304 | 0.587 | n.s. |
| 4 to 5 - 5 to 5 | 3.35 | 0.80 | 4.21 | < .001 | < .001 | *** |
| 4 to 5 - 6 to 5 | 0.91 | 0.80 | 1.14 | 0.255 | 0.587 | n.s. |
| 5 to 5 - 6 to 5 | -2.43 | 0.82 | -2.97 | 0.003 | 0.026 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.88, *p* < .001, η²_G = 0.435
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 2.54 | 6 | = 0.089 | 1.20 [-0.44, 0.72] | large | n.s. |
| 2 to 5 vs 4 to 5 | -0.23 | 6 | = 0.825 | -0.12 [-1.02, 0.18] | negligible | n.s. |
| 2 to 5 vs 5 to 5 | 7.64 | 6 | = 0.003 | 3.20 [0.12, 1.61] | large | ** |
| 2 to 5 vs 6 to 5 | 1.79 | 6 | = 0.176 | 0.67 [-0.26, 1.15] | medium | n.s. |
| 3 to 5 vs 4 to 5 | -1.87 | 6 | = 0.176 | -1.00 [-1.03, 0.28] | large | n.s. |
| 3 to 5 vs 5 to 5 | 3.20 | 6 | = 0.046 | 1.64 [0.15, 1.92] | large | * |
| 3 to 5 vs 6 to 5 | -0.64 | 6 | = 0.608 | -0.36 [-0.95, 0.42] | small | n.s. |
| 4 to 5 vs 5 to 5 | 4.65 | 6 | = 0.018 | 2.15 [0.12, 1.87] | large | * |
| 4 to 5 vs 6 to 5 | 1.25 | 6 | = 0.321 | 0.63 [-0.39, 1.09] | medium | n.s. |
| 5 to 5 vs 6 to 5 | -4.02 | 6 | = 0.023 | -1.71 [-1.88, -0.13] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - 3 to 5 showed greater amplitude than 6 to 5 (*d* = 0.92)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 5 showed greater amplitude than 5 to 5 (*d* = 3.20)
  - 3 to 5 showed greater amplitude than 5 to 5 (*d* = 1.64)
  - 4 to 5 showed greater amplitude than 5 to 5 (*d* = 2.15)
  - 5 to 5 showed smaller amplitude than 6 to 5 (*d* = -1.71)

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
