# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:39:32

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
| 2 to 1 | 8 | 100.50 ms | 10.35 | 3.66 | [92.00, 116.00] |
| 2 to 2 | 10 | 100.00 ms | 9.43 | 2.98 | [92.00, 116.00] |
| 2 to 3 | 10 | 110.00 ms | 8.69 | 2.75 | [92.00, 116.00] |
| 2 to 4 | 8 | 110.00 ms | 10.03 | 3.55 | [92.00, 116.00] |
| 2 to 5 | 14 | 109.43 ms | 9.75 | 2.61 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 8 | 3.56 µV | 2.02 | 0.71 | [0.76, 6.52] |
| 2 to 2 | 10 | 2.45 µV | 1.50 | 0.47 | [0.81, 6.00] |
| 2 to 3 | 10 | 2.38 µV | 1.71 | 0.54 | [0.45, 6.35] |
| 2 to 4 | 8 | 1.77 µV | 1.22 | 0.43 | [0.48, 4.01] |
| 2 to 5 | 14 | 2.16 µV | 1.06 | 0.28 | [0.95, 4.40] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 180.25 ms | 12.00 | 3.00 | [160.00, 204.00] |
| 2 to 2 | 22 | 174.36 ms | 20.72 | 4.42 | [144.00, 204.00] |
| 2 to 3 | 21 | 168.95 ms | 17.39 | 3.79 | [144.00, 204.00] |
| 2 to 4 | 21 | 169.52 ms | 14.78 | 3.22 | [144.00, 196.00] |
| 2 to 5 | 24 | 173.50 ms | 18.64 | 3.81 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | -5.20 µV | 2.57 | 0.64 | [-10.79, -1.72] |
| 2 to 2 | 22 | -5.64 µV | 2.44 | 0.52 | [-10.50, -1.57] |
| 2 to 3 | 21 | -5.62 µV | 1.74 | 0.38 | [-10.20, -2.59] |
| 2 to 4 | 21 | -6.78 µV | 2.60 | 0.57 | [-15.66, -3.83] |
| 2 to 5 | 24 | -6.33 µV | 2.61 | 0.53 | [-13.83, -1.17] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 116.71 ms | 9.19 | 2.23 | [92.00, 124.00] |
| 2 to 2 | 12 | 106.00 ms | 14.22 | 4.10 | [88.00, 124.00] |
| 2 to 3 | 13 | 111.08 ms | 12.87 | 3.57 | [88.00, 124.00] |
| 2 to 4 | 15 | 108.27 ms | 12.51 | 3.23 | [88.00, 124.00] |
| 2 to 5 | 12 | 104.00 ms | 10.92 | 3.15 | [88.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 4.70 µV | 2.37 | 0.58 | [1.72, 9.13] |
| 2 to 2 | 12 | 3.32 µV | 1.81 | 0.52 | [1.61, 7.57] |
| 2 to 3 | 13 | 3.45 µV | 1.72 | 0.48 | [1.17, 6.87] |
| 2 to 4 | 15 | 3.56 µV | 2.10 | 0.54 | [1.12, 7.56] |
| 2 to 5 | 12 | 3.21 µV | 3.00 | 0.87 | [0.74, 11.82] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 479.20 ms | 43.37 | 9.70 | [392.00, 528.00] |
| 2 to 2 | 13 | 451.69 ms | 35.83 | 9.94 | [392.00, 496.00] |
| 2 to 3 | 18 | 450.00 ms | 40.59 | 9.57 | [392.00, 528.00] |
| 2 to 4 | 19 | 468.00 ms | 52.27 | 11.99 | [392.00, 528.00] |
| 2 to 5 | 23 | 450.09 ms | 41.00 | 8.55 | [392.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 6.12 µV | 3.06 | 0.69 | [1.72, 11.08] |
| 2 to 2 | 13 | 4.65 µV | 2.31 | 0.64 | [1.28, 10.57] |
| 2 to 3 | 18 | 6.51 µV | 3.27 | 0.77 | [1.82, 13.70] |
| 2 to 4 | 19 | 7.30 µV | 4.34 | 1.00 | [1.60, 17.43] |
| 2 to 5 | 23 | 5.71 µV | 2.49 | 0.52 | [2.48, 11.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 376.23, BIC = 391.53
- **2 to 2 vs 2 to 1**: *β* = -0.52, *SE* = 4.400, *z* = -0.118, *p* = 0.906
- **2 to 3 vs 2 to 1**: *β* = 8.58, *SE* = 4.276, *z* = 2.006, *p* = 0.045
- **2 to 4 vs 2 to 1**: *β* = 10.61, *SE* = 4.425, *z* = 2.398, *p* = 0.016
- **2 to 5 vs 2 to 1**: *β* = 9.79, *SE* = 4.120, *z* = 2.376, *p* = 0.017
- **SNR**: *β* = 1.81, *SE* = 1.178, *z* = 1.537, *p* = 0.124

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.52 | 4.40 | 0.12 | 0.906 | 0.983 | n.s. |
| 2 to 1 - 2 to 3 | -8.58 | 4.28 | -2.01 | 0.045 | 0.205 | n.s. |
| 2 to 1 - 2 to 4 | -10.61 | 4.42 | -2.40 | 0.016 | 0.124 | n.s. |
| 2 to 1 - 2 to 5 | -9.79 | 4.12 | -2.38 | 0.017 | 0.124 | n.s. |
| 2 to 2 - 2 to 3 | -9.10 | 3.90 | -2.33 | 0.020 | 0.124 | n.s. |
| 2 to 2 - 2 to 4 | -11.13 | 4.24 | -2.63 | 0.009 | 0.075 | n.s. |
| 2 to 2 - 2 to 5 | -10.31 | 3.59 | -2.87 | 0.004 | 0.040 | * |
| 2 to 3 - 2 to 4 | -2.03 | 4.34 | -0.47 | 0.639 | 0.983 | n.s. |
| 2 to 3 - 2 to 5 | -1.21 | 3.71 | -0.33 | 0.744 | 0.983 | n.s. |
| 2 to 4 - 2 to 5 | 0.82 | 3.87 | 0.21 | 0.832 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.71 | 0.55 | 1.30 | 0.195 | 0.781 | n.s. |
| 2 to 1 - 2 to 3 | 1.28 | 0.53 | 2.40 | 0.016 | 0.153 | n.s. |
| 2 to 1 - 2 to 4 | 1.20 | 0.55 | 2.18 | 0.029 | 0.232 | n.s. |
| 2 to 1 - 2 to 5 | 0.72 | 0.49 | 1.45 | 0.147 | 0.718 | n.s. |
| 2 to 2 - 2 to 3 | 0.56 | 0.49 | 1.16 | 0.244 | 0.802 | n.s. |
| 2 to 2 - 2 to 4 | 0.49 | 0.57 | 0.87 | 0.386 | 0.802 | n.s. |
| 2 to 2 - 2 to 5 | 0.01 | 0.47 | 0.01 | 0.989 | 0.989 | n.s. |
| 2 to 3 - 2 to 4 | -0.07 | 0.57 | -0.13 | 0.896 | 0.989 | n.s. |
| 2 to 3 - 2 to 5 | -0.56 | 0.47 | -1.18 | 0.236 | 0.802 | n.s. |
| 2 to 4 - 2 to 5 | -0.48 | 0.49 | -1.00 | 0.319 | 0.802 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 878.84, BIC = 900.00
- **2 to 2 vs 2 to 1**: *β* = -5.14, *SE* = 4.399, *z* = -1.169, *p* = 0.242
- **2 to 3 vs 2 to 1**: *β* = -8.73, *SE* = 4.501, *z* = -1.940, *p* = 0.052
- **2 to 4 vs 2 to 1**: *β* = -7.94, *SE* = 4.577, *z* = -1.736, *p* = 0.083
- **2 to 5 vs 2 to 1**: *β* = -5.65, *SE* = 4.386, *z* = -1.288, *p* = 0.198
- **SNR**: *β* = -0.31, *SE* = 0.637, *z* = -0.489, *p* = 0.625

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 5.14 | 4.40 | 1.17 | 0.242 | 0.857 | n.s. |
| 2 to 1 - 2 to 3 | 8.73 | 4.50 | 1.94 | 0.052 | 0.416 | n.s. |
| 2 to 1 - 2 to 4 | 7.94 | 4.58 | 1.74 | 0.083 | 0.540 | n.s. |
| 2 to 1 - 2 to 5 | 5.65 | 4.39 | 1.29 | 0.198 | 0.828 | n.s. |
| 2 to 2 - 2 to 3 | 3.59 | 4.09 | 0.88 | 0.381 | 0.944 | n.s. |
| 2 to 2 - 2 to 4 | 2.80 | 4.17 | 0.67 | 0.502 | 0.944 | n.s. |
| 2 to 2 - 2 to 5 | 0.51 | 3.95 | 0.13 | 0.898 | 0.977 | n.s. |
| 2 to 3 - 2 to 4 | -0.79 | 4.11 | -0.19 | 0.848 | 0.977 | n.s. |
| 2 to 3 - 2 to 5 | -3.08 | 3.98 | -0.77 | 0.439 | 0.944 | n.s. |
| 2 to 4 - 2 to 5 | -2.30 | 4.00 | -0.57 | 0.566 | 0.944 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.84, *p* = 0.504, η²_G = 0.036
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 1.15 | 13 | = 0.677 | 0.29 [-0.28, 0.81] | small | n.s. |
| 2 to 1 vs 2 to 3 | 1.91 | 13 | = 0.605 | 0.60 [-0.12, 1.05] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 1.66 | 13 | = 0.605 | 0.63 [-0.10, 1.07] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 1.36 | 13 | = 0.661 | 0.46 [-0.18, 0.92] | small | n.s. |
| 2 to 2 vs 2 to 3 | 0.69 | 13 | = 0.861 | 0.20 [-0.28, 0.66] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | 0.61 | 13 | = 0.861 | 0.22 [-0.35, 0.59] | small | n.s. |
| 2 to 2 vs 2 to 5 | 0.41 | 13 | = 0.861 | 0.12 [-0.43, 0.45] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | 0.04 | 13 | = 0.966 | 0.02 [-0.53, 0.40] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | -0.21 | 13 | = 0.932 | -0.08 [-0.52, 0.39] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | -0.44 | 13 | = 0.861 | -0.09 [-0.57, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 446.30, BIC = 467.46
- **2 to 2 vs 2 to 1**: *β* = -0.53, *SE* = 0.565, *z* = -0.939, *p* = 0.348
- **2 to 3 vs 2 to 1**: *β* = -0.14, *SE* = 0.577, *z* = -0.241, *p* = 0.810
- **2 to 4 vs 2 to 1**: *β* = -0.90, *SE* = 0.586, *z* = -1.537, *p* = 0.124
- **2 to 5 vs 2 to 1**: *β* = -0.92, *SE* = 0.563, *z* = -1.635, *p* = 0.102
- **SNR**: *β* = -0.52, *SE* = 0.080, *z* = -6.549, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.53 | 0.56 | 0.94 | 0.348 | 0.923 | n.s. |
| 2 to 1 - 2 to 3 | 0.14 | 0.58 | 0.24 | 0.810 | 0.964 | n.s. |
| 2 to 1 - 2 to 4 | 0.90 | 0.59 | 1.54 | 0.124 | 0.697 | n.s. |
| 2 to 1 - 2 to 5 | 0.92 | 0.56 | 1.63 | 0.102 | 0.659 | n.s. |
| 2 to 2 - 2 to 3 | -0.39 | 0.53 | -0.75 | 0.456 | 0.946 | n.s. |
| 2 to 2 - 2 to 4 | 0.37 | 0.53 | 0.69 | 0.488 | 0.946 | n.s. |
| 2 to 2 - 2 to 5 | 0.39 | 0.51 | 0.77 | 0.442 | 0.946 | n.s. |
| 2 to 3 - 2 to 4 | 0.76 | 0.53 | 1.44 | 0.149 | 0.697 | n.s. |
| 2 to 3 - 2 to 5 | 0.78 | 0.51 | 1.53 | 0.126 | 0.697 | n.s. |
| 2 to 4 - 2 to 5 | 0.02 | 0.51 | 0.04 | 0.971 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.80, *p* = 0.142, η²_G = 0.078
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 1.41 | 13 | = 0.455 | 0.46 [-0.24, 0.85] | small | n.s. |
| 2 to 1 vs 2 to 3 | 1.70 | 13 | = 0.377 | 0.54 [-0.21, 0.93] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 2.01 | 13 | = 0.328 | 0.76 [-0.06, 1.12] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 2.27 | 13 | = 0.328 | 0.69 [-0.16, 0.94] | medium | n.s. |
| 2 to 2 vs 2 to 3 | 0.02 | 13 | = 0.984 | 0.01 [-0.40, 0.54] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | 1.05 | 13 | = 0.551 | 0.33 [-0.14, 0.83] | small | n.s. |
| 2 to 2 vs 2 to 5 | 0.76 | 13 | = 0.578 | 0.24 [-0.11, 0.80] | small | n.s. |
| 2 to 3 vs 2 to 4 | 1.01 | 13 | = 0.551 | 0.37 [-0.10, 0.87] | small | n.s. |
| 2 to 3 vs 2 to 5 | 0.80 | 13 | = 0.578 | 0.27 [-0.14, 0.80] | small | n.s. |
| 2 to 4 vs 2 to 5 | -0.29 | 13 | = 0.860 | -0.10 [-0.49, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 546.82, BIC = 564.69
- **2 to 2 vs 2 to 1**: *β* = -9.45, *SE* = 4.449, *z* = -2.124, *p* = 0.034
- **2 to 3 vs 2 to 1**: *β* = -4.47, *SE* = 4.351, *z* = -1.027, *p* = 0.304
- **2 to 4 vs 2 to 1**: *β* = -7.30, *SE* = 4.081, *z* = -1.790, *p* = 0.073
- **2 to 5 vs 2 to 1**: *β* = -11.07, *SE* = 4.507, *z* = -2.457, *p* = 0.014
- **SNR**: *β* = 0.85, *SE* = 0.691, *z* = 1.236, *p* = 0.217

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 9.45 | 4.45 | 2.12 | 0.034 | 0.266 | n.s. |
| 2 to 1 - 2 to 3 | 4.47 | 4.35 | 1.03 | 0.304 | 0.844 | n.s. |
| 2 to 1 - 2 to 4 | 7.30 | 4.08 | 1.79 | 0.073 | 0.457 | n.s. |
| 2 to 1 - 2 to 5 | 11.07 | 4.51 | 2.46 | 0.014 | 0.132 | n.s. |
| 2 to 2 - 2 to 3 | -4.98 | 4.48 | -1.11 | 0.266 | 0.844 | n.s. |
| 2 to 2 - 2 to 4 | -2.14 | 4.39 | -0.49 | 0.626 | 0.883 | n.s. |
| 2 to 2 - 2 to 5 | 1.62 | 4.57 | 0.36 | 0.722 | 0.883 | n.s. |
| 2 to 3 - 2 to 4 | 2.84 | 4.31 | 0.66 | 0.511 | 0.883 | n.s. |
| 2 to 3 - 2 to 5 | 6.60 | 4.50 | 1.47 | 0.142 | 0.657 | n.s. |
| 2 to 4 - 2 to 5 | 3.77 | 4.40 | 0.86 | 0.392 | 0.863 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.78, *p* = 0.199, η²_G = 0.329
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 0.00 | 3 | = 1.000 | 0.00 [-0.17, 1.54] | negligible | n.s. |
| 2 to 1 vs 2 to 3 | 2.75 | 3 | = 0.236 | 2.07 [-0.05, 1.58] | large | n.s. |
| 2 to 1 vs 2 to 4 | 0.46 | 3 | = 0.750 | 0.38 [-0.36, 1.26] | small | n.s. |
| 2 to 1 vs 2 to 5 | 2.89 | 3 | = 0.236 | 2.24 [0.27, 2.15] | large | n.s. |
| 2 to 2 vs 2 to 3 | 1.72 | 3 | = 0.459 | 1.60 [-0.89, 0.66] | large | n.s. |
| 2 to 2 vs 2 to 4 | 0.59 | 3 | = 0.750 | 0.34 [-1.05, 0.64] | small | n.s. |
| 2 to 2 vs 2 to 5 | 3.87 | 3 | = 0.236 | 1.46 [-0.83, 0.71] | large | n.s. |
| 2 to 3 vs 2 to 4 | -1.29 | 3 | = 0.578 | -0.77 [-1.16, 0.71] | medium | n.s. |
| 2 to 3 vs 2 to 5 | -0.47 | 3 | = 0.750 | -0.45 [-0.59, 0.96] | small | n.s. |
| 2 to 4 vs 2 to 5 | 0.77 | 3 | = 0.750 | 0.56 [-0.20, 1.49] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 287.58, BIC = 305.45
- **2 to 2 vs 2 to 1**: *β* = -0.33, *SE* = 0.679, *z* = -0.489, *p* = 0.624
- **2 to 3 vs 2 to 1**: *β* = -0.28, *SE* = 0.670, *z* = -0.424, *p* = 0.672
- **2 to 4 vs 2 to 1**: *β* = -0.32, *SE* = 0.625, *z* = -0.507, *p* = 0.612
- **2 to 5 vs 2 to 1**: *β* = -0.23, *SE* = 0.700, *z* = -0.326, *p* = 0.745
- **SNR**: *β* = 0.62, *SE* = 0.114, *z* = 5.462, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.33 | 0.68 | 0.49 | 0.624 | 1.000 | n.s. |
| 2 to 1 - 2 to 3 | 0.28 | 0.67 | 0.42 | 0.672 | 1.000 | n.s. |
| 2 to 1 - 2 to 4 | 0.32 | 0.62 | 0.51 | 0.612 | 1.000 | n.s. |
| 2 to 1 - 2 to 5 | 0.23 | 0.70 | 0.33 | 0.745 | 1.000 | n.s. |
| 2 to 2 - 2 to 3 | -0.05 | 0.68 | -0.07 | 0.943 | 1.000 | n.s. |
| 2 to 2 - 2 to 4 | -0.02 | 0.66 | -0.02 | 0.981 | 1.000 | n.s. |
| 2 to 2 - 2 to 5 | -0.10 | 0.69 | -0.15 | 0.881 | 1.000 | n.s. |
| 2 to 3 - 2 to 4 | 0.03 | 0.65 | 0.05 | 0.960 | 1.000 | n.s. |
| 2 to 3 - 2 to 5 | -0.06 | 0.68 | -0.08 | 0.935 | 1.000 | n.s. |
| 2 to 4 - 2 to 5 | -0.09 | 0.67 | -0.13 | 0.894 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.61, *p* < .001, η²_G = 0.621
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 3.28 | 3 | = 0.093 | 1.58 [0.34, 2.53] | large | n.s. |
| 2 to 1 vs 2 to 3 | 5.67 | 3 | = 0.049 | 4.52 [-0.08, 1.52] | large | * |
| 2 to 1 vs 2 to 4 | 5.09 | 3 | = 0.049 | 1.67 [0.03, 1.89] | large | * |
| 2 to 1 vs 2 to 5 | 31.80 | 3 | < .001 | 4.98 [0.09, 1.82] | large | *** |
| 2 to 2 vs 2 to 3 | 1.39 | 3 | = 0.359 | 0.82 [-0.54, 1.02] | large | n.s. |
| 2 to 2 vs 2 to 4 | -0.09 | 3 | = 0.935 | -0.04 [-1.31, 0.44] | negligible | n.s. |
| 2 to 2 vs 2 to 5 | 2.73 | 3 | = 0.120 | 1.28 [-0.80, 0.74] | large | n.s. |
| 2 to 3 vs 2 to 4 | -1.18 | 3 | = 0.359 | -0.97 [-1.61, 0.40] | large | n.s. |
| 2 to 3 vs 2 to 5 | 1.27 | 3 | = 0.359 | 0.96 [-0.71, 0.83] | large | n.s. |
| 2 to 4 vs 2 to 5 | 3.60 | 3 | = 0.092 | 1.46 [-0.13, 1.60] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 975.48, BIC = 995.74
- **2 to 2 vs 2 to 1**: *β* = -25.64, *SE* = 15.081, *z* = -1.700, *p* = 0.089
- **2 to 3 vs 2 to 1**: *β* = -29.31, *SE* = 13.502, *z* = -2.171, *p* = 0.030
- **2 to 4 vs 2 to 1**: *β* = -11.22, *SE* = 13.394, *z* = -0.837, *p* = 0.402
- **2 to 5 vs 2 to 1**: *β* = -28.73, *SE* = 12.621, *z* = -2.276, *p* = 0.023
- **SNR**: *β* = 0.46, *SE* = 1.445, *z* = 0.319, *p* = 0.750

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 25.63 | 15.08 | 1.70 | 0.089 | 0.526 | n.s. |
| 2 to 1 - 2 to 3 | 29.31 | 13.50 | 2.17 | 0.030 | 0.239 | n.s. |
| 2 to 1 - 2 to 4 | 11.22 | 13.39 | 0.84 | 0.402 | 0.887 | n.s. |
| 2 to 1 - 2 to 5 | 28.73 | 12.62 | 2.28 | 0.023 | 0.206 | n.s. |
| 2 to 2 - 2 to 3 | 3.67 | 15.59 | 0.24 | 0.814 | 0.994 | n.s. |
| 2 to 2 - 2 to 4 | -14.42 | 15.52 | -0.93 | 0.353 | 0.887 | n.s. |
| 2 to 2 - 2 to 5 | 3.09 | 14.59 | 0.21 | 0.832 | 0.994 | n.s. |
| 2 to 3 - 2 to 4 | -18.09 | 13.58 | -1.33 | 0.183 | 0.750 | n.s. |
| 2 to 3 - 2 to 5 | -0.58 | 13.14 | -0.04 | 0.965 | 0.994 | n.s. |
| 2 to 4 - 2 to 5 | 17.51 | 13.05 | 1.34 | 0.180 | 0.750 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.45, *p* = 0.233, η²_G = 0.096
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 1.29 | 11 | = 0.550 | 0.66 [-0.35, 0.88] | medium | n.s. |
| 2 to 1 vs 2 to 3 | 1.57 | 11 | = 0.480 | 0.76 [-0.11, 1.01] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 0.32 | 11 | = 0.841 | 0.09 [-0.43, 0.57] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | 2.12 | 11 | = 0.480 | 0.78 [-0.03, 0.96] | medium | n.s. |
| 2 to 2 vs 2 to 3 | 0.44 | 11 | = 0.841 | 0.13 [-0.51, 0.76] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | -0.92 | 11 | = 0.631 | -0.47 [-0.78, 0.44] | small | n.s. |
| 2 to 2 vs 2 to 5 | 0.32 | 11 | = 0.841 | 0.12 [-0.50, 0.71] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -1.15 | 11 | = 0.550 | -0.56 [-0.78, 0.26] | medium | n.s. |
| 2 to 3 vs 2 to 5 | -0.02 | 11 | = 0.982 | -0.01 [-0.49, 0.54] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.76 | 11 | = 0.480 | 0.57 [-0.14, 0.85] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 415.63, BIC = 435.90
- **2 to 2 vs 2 to 1**: *β* = -0.75, *SE* = 0.641, *z* = -1.174, *p* = 0.240
- **2 to 3 vs 2 to 1**: *β* = -0.12, *SE* = 0.574, *z* = -0.217, *p* = 0.828
- **2 to 4 vs 2 to 1**: *β* = 0.40, *SE* = 0.563, *z* = 0.713, *p* = 0.476
- **2 to 5 vs 2 to 1**: *β* = -0.11, *SE* = 0.532, *z* = -0.201, *p* = 0.841
- **SNR**: *β* = 0.61, *SE* = 0.068, *z* = 8.980, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.75 | 0.64 | 1.17 | 0.240 | 0.916 | n.s. |
| 2 to 1 - 2 to 3 | 0.12 | 0.57 | 0.22 | 0.828 | 0.995 | n.s. |
| 2 to 1 - 2 to 4 | -0.40 | 0.56 | -0.71 | 0.476 | 0.950 | n.s. |
| 2 to 1 - 2 to 5 | 0.11 | 0.53 | 0.20 | 0.841 | 0.995 | n.s. |
| 2 to 2 - 2 to 3 | -0.63 | 0.67 | -0.94 | 0.348 | 0.950 | n.s. |
| 2 to 2 - 2 to 4 | -1.15 | 0.67 | -1.73 | 0.084 | 0.583 | n.s. |
| 2 to 2 - 2 to 5 | -0.65 | 0.63 | -1.03 | 0.305 | 0.945 | n.s. |
| 2 to 3 - 2 to 4 | -0.53 | 0.57 | -0.92 | 0.358 | 0.950 | n.s. |
| 2 to 3 - 2 to 5 | -0.02 | 0.56 | -0.03 | 0.975 | 0.995 | n.s. |
| 2 to 4 - 2 to 5 | 0.51 | 0.55 | 0.92 | 0.356 | 0.950 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.19, *p* = 0.022, η²_G = 0.128
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 3.28 | 11 | = 0.037 | 0.91 [0.01, 1.36] | large | * |
| 2 to 1 vs 2 to 3 | -0.61 | 11 | = 0.616 | -0.20 [-0.63, 0.44] | small | n.s. |
| 2 to 1 vs 2 to 4 | -0.63 | 11 | = 0.616 | -0.23 [-0.74, 0.27] | small | n.s. |
| 2 to 1 vs 2 to 5 | 1.05 | 11 | = 0.453 | 0.24 [-0.39, 0.55] | small | n.s. |
| 2 to 2 vs 2 to 3 | -3.55 | 11 | = 0.037 | -1.22 [-1.81, -0.24] | large | * |
| 2 to 2 vs 2 to 4 | -2.59 | 11 | = 0.084 | -0.89 [-1.33, 0.00] | large | n.s. |
| 2 to 2 vs 2 to 5 | -2.01 | 11 | = 0.165 | -0.70 [-1.11, 0.16] | medium | n.s. |
| 2 to 3 vs 2 to 4 | -0.29 | 11 | = 0.776 | -0.09 [-0.72, 0.32] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 1.91 | 11 | = 0.165 | 0.47 [-0.32, 0.72] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.22 | 11 | = 0.412 | 0.41 [-0.18, 0.81] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 3 (*d* = 4.52)
  - 2 to 1 showed greater amplitude than 2 to 4 (*d* = 1.67)
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 4.98)
**P3b amplitude:** Significant main effect of condition (*p* = 0.022). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 2 (*d* = 0.91)
  - 2 to 2 showed smaller amplitude than 2 to 3 (*d* = -1.22)

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
