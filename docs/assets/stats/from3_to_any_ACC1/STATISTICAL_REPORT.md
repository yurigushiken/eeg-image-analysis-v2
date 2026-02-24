# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:20:47

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
| 3 to 1 | 24 | 105.67 ms | 11.37 | 2.32 | [88.00, 116.00] |
| 3 to 2 | 24 | 104.17 ms | 11.10 | 2.26 | [88.00, 116.00] |
| 3 to 3 | 24 | 104.50 ms | 11.99 | 2.45 | [88.00, 116.00] |
| 3 to 4 | 24 | 102.67 ms | 9.92 | 2.02 | [88.00, 116.00] |
| 3 to 5 | 24 | 101.33 ms | 10.46 | 2.14 | [88.00, 116.00] |
| 3 to 6 | 24 | 100.83 ms | 11.56 | 2.36 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -1.80 µV | 1.99 | 0.41 | [-6.48, 1.50] |
| 3 to 2 | 24 | -1.45 µV | 2.17 | 0.44 | [-5.62, 2.93] |
| 3 to 3 | 24 | -1.43 µV | 2.62 | 0.54 | [-8.81, 1.87] |
| 3 to 4 | 24 | -1.73 µV | 1.91 | 0.39 | [-5.42, 2.48] |
| 3 to 5 | 24 | -1.45 µV | 2.44 | 0.50 | [-4.98, 5.40] |
| 3 to 6 | 24 | -2.16 µV | 1.99 | 0.41 | [-4.89, 1.55] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 181.33 ms | 16.46 | 3.36 | [140.00, 208.00] |
| 3 to 2 | 24 | 175.17 ms | 23.11 | 4.72 | [140.00, 208.00] |
| 3 to 3 | 24 | 171.17 ms | 19.45 | 3.97 | [140.00, 208.00] |
| 3 to 4 | 24 | 165.67 ms | 18.57 | 3.79 | [140.00, 204.00] |
| 3 to 5 | 24 | 169.50 ms | 23.50 | 4.80 | [140.00, 208.00] |
| 3 to 6 | 24 | 169.67 ms | 20.46 | 4.18 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -4.21 µV | 2.80 | 0.57 | [-10.41, -0.30] |
| 3 to 2 | 24 | -5.92 µV | 2.55 | 0.52 | [-10.33, -1.67] |
| 3 to 3 | 24 | -5.16 µV | 1.95 | 0.40 | [-10.83, -1.55] |
| 3 to 4 | 24 | -5.71 µV | 2.27 | 0.46 | [-10.53, -0.87] |
| 3 to 5 | 24 | -5.59 µV | 2.77 | 0.57 | [-13.75, -0.84] |
| 3 to 6 | 24 | -6.86 µV | 2.91 | 0.59 | [-12.76, -1.85] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 108.17 ms | 9.32 | 1.90 | [92.00, 116.00] |
| 3 to 2 | 24 | 104.83 ms | 9.87 | 2.01 | [92.00, 116.00] |
| 3 to 3 | 24 | 106.33 ms | 10.54 | 2.15 | [92.00, 116.00] |
| 3 to 4 | 24 | 102.83 ms | 9.54 | 1.95 | [92.00, 116.00] |
| 3 to 5 | 24 | 102.50 ms | 10.13 | 2.07 | [92.00, 116.00] |
| 3 to 6 | 24 | 102.50 ms | 9.78 | 2.00 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 2.82 µV | 2.18 | 0.45 | [-0.93, 9.14] |
| 3 to 2 | 24 | 0.64 µV | 2.32 | 0.47 | [-3.61, 5.61] |
| 3 to 3 | 24 | 1.55 µV | 2.89 | 0.59 | [-3.19, 8.96] |
| 3 to 4 | 24 | 2.17 µV | 2.22 | 0.45 | [-1.38, 7.39] |
| 3 to 5 | 24 | 1.12 µV | 2.52 | 0.52 | [-2.94, 5.64] |
| 3 to 6 | 24 | 1.64 µV | 2.61 | 0.53 | [-2.10, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 484.50 ms | 31.48 | 6.43 | [428.00, 540.00] |
| 3 to 2 | 24 | 488.50 ms | 34.35 | 7.01 | [432.00, 540.00] |
| 3 to 3 | 24 | 473.00 ms | 33.12 | 6.76 | [428.00, 540.00] |
| 3 to 4 | 24 | 494.33 ms | 37.82 | 7.72 | [428.00, 540.00] |
| 3 to 5 | 24 | 486.00 ms | 40.84 | 8.34 | [428.00, 540.00] |
| 3 to 6 | 24 | 493.33 ms | 40.55 | 8.28 | [428.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 5.19 µV | 3.62 | 0.74 | [-0.82, 16.27] |
| 3 to 2 | 24 | 5.31 µV | 4.41 | 0.90 | [-1.20, 17.81] |
| 3 to 3 | 24 | 2.90 µV | 3.32 | 0.68 | [-6.17, 9.60] |
| 3 to 4 | 24 | 4.34 µV | 4.76 | 0.97 | [-5.10, 13.58] |
| 3 to 5 | 24 | 4.21 µV | 4.37 | 0.89 | [-3.15, 16.52] |
| 3 to 6 | 24 | 4.15 µV | 2.93 | 0.60 | [-3.66, 11.34] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1111.93, BIC = 1138.66
- **3 to 2 vs 3 to 1**: *β* = -1.50, *SE* = 3.087, *z* = -0.486, *p* = 0.627
- **3 to 3 vs 3 to 1**: *β* = -1.17, *SE* = 3.079, *z* = -0.379, *p* = 0.705
- **3 to 4 vs 3 to 1**: *β* = -3.00, *SE* = 3.078, *z* = -0.975, *p* = 0.330
- **3 to 5 vs 3 to 1**: *β* = -4.33, *SE* = 3.120, *z* = -1.390, *p* = 0.165
- **3 to 6 vs 3 to 1**: *β* = -4.83, *SE* = 3.079, *z* = -1.570, *p* = 0.116
- **SNR**: *β* = 0.00, *SE* = 0.710, *z* = 0.003, *p* = 0.997

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 1.50 | 3.09 | 0.49 | 0.627 | 0.998 | n.s. |
| 3 to 1 - 3 to 3 | 1.17 | 3.08 | 0.38 | 0.705 | 0.998 | n.s. |
| 3 to 1 - 3 to 4 | 3.00 | 3.08 | 0.97 | 0.330 | 0.982 | n.s. |
| 3 to 1 - 3 to 5 | 4.34 | 3.12 | 1.39 | 0.165 | 0.919 | n.s. |
| 3 to 1 - 3 to 6 | 4.83 | 3.08 | 1.57 | 0.116 | 0.844 | n.s. |
| 3 to 2 - 3 to 3 | -0.33 | 3.08 | -0.11 | 0.914 | 0.998 | n.s. |
| 3 to 2 - 3 to 4 | 1.50 | 3.09 | 0.48 | 0.628 | 0.998 | n.s. |
| 3 to 2 - 3 to 5 | 2.83 | 3.09 | 0.92 | 0.359 | 0.982 | n.s. |
| 3 to 2 - 3 to 6 | 3.33 | 3.08 | 1.08 | 0.279 | 0.980 | n.s. |
| 3 to 3 - 3 to 4 | 1.83 | 3.08 | 0.59 | 0.552 | 0.998 | n.s. |
| 3 to 3 - 3 to 5 | 3.17 | 3.10 | 1.02 | 0.308 | 0.982 | n.s. |
| 3 to 3 - 3 to 6 | 3.67 | 3.08 | 1.19 | 0.233 | 0.968 | n.s. |
| 3 to 4 - 3 to 5 | 1.34 | 3.13 | 0.43 | 0.670 | 0.998 | n.s. |
| 3 to 4 - 3 to 6 | 1.83 | 3.08 | 0.60 | 0.552 | 0.998 | n.s. |
| 3 to 5 - 3 to 6 | 0.50 | 3.11 | 0.16 | 0.872 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.566, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 0.43 | 23 | = 0.842 | 0.13 [-0.34, 0.51] | negligible | n.s. |
| 3 to 1 vs 3 to 3 | 0.33 | 23 | = 0.855 | 0.10 [-0.35, 0.49] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | 1.04 | 23 | = 0.805 | 0.28 [-0.21, 0.64] | small | n.s. |
| 3 to 1 vs 3 to 5 | 1.52 | 23 | = 0.805 | 0.40 [-0.12, 0.74] | small | n.s. |
| 3 to 1 vs 3 to 6 | 1.43 | 23 | = 0.805 | 0.42 [-0.14, 0.72] | small | n.s. |
| 3 to 2 vs 3 to 3 | -0.10 | 23 | = 0.920 | -0.03 [-0.44, 0.40] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 0.48 | 23 | = 0.842 | 0.14 [-0.33, 0.52] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.89 | 23 | = 0.822 | 0.26 [-0.24, 0.61] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.17 | 23 | = 0.805 | 0.29 [-0.19, 0.67] | small | n.s. |
| 3 to 3 vs 3 to 4 | 0.60 | 23 | = 0.842 | 0.17 [-0.30, 0.55] | negligible | n.s. |
| 3 to 3 vs 3 to 5 | 1.01 | 23 | = 0.805 | 0.28 [-0.22, 0.63] | small | n.s. |
| 3 to 3 vs 3 to 6 | 1.19 | 23 | = 0.805 | 0.31 [-0.19, 0.67] | small | n.s. |
| 3 to 4 vs 3 to 5 | 0.52 | 23 | = 0.842 | 0.13 [-0.32, 0.53] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.75 | 23 | = 0.842 | 0.17 [-0.27, 0.58] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.19 | 23 | = 0.908 | 0.05 [-0.38, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 629.46, BIC = 656.18
- **3 to 2 vs 3 to 1**: *β* = 0.39, *SE* = 0.531, *z* = 0.742, *p* = 0.458
- **3 to 3 vs 3 to 1**: *β* = 0.39, *SE* = 0.530, *z* = 0.733, *p* = 0.463
- **3 to 4 vs 3 to 1**: *β* = 0.05, *SE* = 0.529, *z* = 0.100, *p* = 0.921
- **3 to 5 vs 3 to 1**: *β* = 0.45, *SE* = 0.537, *z* = 0.834, *p* = 0.404
- **3 to 6 vs 3 to 1**: *β* = -0.35, *SE* = 0.530, *z* = -0.653, *p* = 0.514
- **SNR**: *β* = -0.15, *SE* = 0.127, *z* = -1.149, *p* = 0.251

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -0.39 | 0.53 | -0.74 | 0.458 | 0.999 | n.s. |
| 3 to 1 - 3 to 3 | -0.39 | 0.53 | -0.73 | 0.463 | 0.999 | n.s. |
| 3 to 1 - 3 to 4 | -0.05 | 0.53 | -0.10 | 0.921 | 1.000 | n.s. |
| 3 to 1 - 3 to 5 | -0.45 | 0.54 | -0.83 | 0.404 | 0.998 | n.s. |
| 3 to 1 - 3 to 6 | 0.35 | 0.53 | 0.65 | 0.514 | 0.999 | n.s. |
| 3 to 2 - 3 to 3 | 0.01 | 0.53 | 0.01 | 0.991 | 1.000 | n.s. |
| 3 to 2 - 3 to 4 | 0.34 | 0.53 | 0.64 | 0.521 | 0.999 | n.s. |
| 3 to 2 - 3 to 5 | -0.05 | 0.53 | -0.10 | 0.920 | 1.000 | n.s. |
| 3 to 2 - 3 to 6 | 0.74 | 0.53 | 1.40 | 0.163 | 0.917 | n.s. |
| 3 to 3 - 3 to 4 | 0.34 | 0.53 | 0.63 | 0.527 | 0.999 | n.s. |
| 3 to 3 - 3 to 5 | -0.06 | 0.53 | -0.11 | 0.911 | 1.000 | n.s. |
| 3 to 3 - 3 to 6 | 0.73 | 0.53 | 1.39 | 0.165 | 0.917 | n.s. |
| 3 to 4 - 3 to 5 | -0.40 | 0.54 | -0.73 | 0.464 | 0.999 | n.s. |
| 3 to 4 - 3 to 6 | 0.40 | 0.53 | 0.75 | 0.452 | 0.999 | n.s. |
| 3 to 5 - 3 to 6 | 0.79 | 0.53 | 1.48 | 0.138 | 0.892 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.56, *p* = 0.731, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.69 | 23 | = 0.852 | -0.17 [-0.57, 0.28] | negligible | n.s. |
| 3 to 1 vs 3 to 3 | -0.74 | 23 | = 0.852 | -0.16 [-0.58, 0.27] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | -0.14 | 23 | = 0.997 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | -0.60 | 23 | = 0.852 | -0.15 [-0.55, 0.30] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 0.70 | 23 | = 0.852 | 0.18 [-0.28, 0.57] | negligible | n.s. |
| 3 to 2 vs 3 to 3 | -0.04 | 23 | = 0.997 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 0.58 | 23 | = 0.852 | 0.14 [-0.31, 0.54] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.00 | 23 | = 0.997 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 1.70 | 23 | = 0.852 | 0.34 [-0.09, 0.78] | small | n.s. |
| 3 to 3 vs 3 to 4 | 0.74 | 23 | = 0.852 | 0.13 [-0.27, 0.58] | negligible | n.s. |
| 3 to 3 vs 3 to 5 | 0.04 | 23 | = 0.997 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 3 to 3 vs 3 to 6 | 1.19 | 23 | = 0.852 | 0.31 [-0.19, 0.67] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.45 | 23 | = 0.894 | -0.13 [-0.52, 0.33] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.85 | 23 | = 0.852 | 0.22 [-0.25, 0.60] | small | n.s. |
| 3 to 5 vs 3 to 6 | 0.98 | 23 | = 0.852 | 0.32 [-0.23, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1244.28, BIC = 1271.01
- **3 to 2 vs 3 to 1**: *β* = -6.21, *SE* = 4.425, *z* = -1.404, *p* = 0.160
- **3 to 3 vs 3 to 1**: *β* = -10.19, *SE* = 4.300, *z* = -2.370, *p* = 0.018
- **3 to 4 vs 3 to 1**: *β* = -15.70, *SE* = 4.329, *z* = -3.627, *p* < .001
- **3 to 5 vs 3 to 1**: *β* = -11.88, *SE* = 4.411, *z* = -2.693, *p* = 0.007
- **3 to 6 vs 3 to 1**: *β* = -11.72, *SE* = 4.460, *z* = -2.627, *p* = 0.009
- **SNR**: *β* = 0.02, *SE* = 0.615, *z* = 0.037, *p* = 0.971

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 6.21 | 4.43 | 1.40 | 0.160 | 0.826 | n.s. |
| 3 to 1 - 3 to 3 | 10.19 | 4.30 | 2.37 | 0.018 | 0.194 | n.s. |
| 3 to 1 - 3 to 4 | 15.70 | 4.33 | 3.63 | < .001 | 0.004 | ** |
| 3 to 1 - 3 to 5 | 11.88 | 4.41 | 2.69 | 0.007 | 0.095 | n.s. |
| 3 to 1 - 3 to 6 | 11.72 | 4.46 | 2.63 | 0.009 | 0.106 | n.s. |
| 3 to 2 - 3 to 3 | 3.98 | 4.29 | 0.93 | 0.353 | 0.926 | n.s. |
| 3 to 2 - 3 to 4 | 9.48 | 4.27 | 2.22 | 0.026 | 0.253 | n.s. |
| 3 to 2 - 3 to 5 | 5.66 | 4.25 | 1.33 | 0.182 | 0.837 | n.s. |
| 3 to 2 - 3 to 6 | 5.50 | 4.25 | 1.30 | 0.195 | 0.837 | n.s. |
| 3 to 3 - 3 to 4 | 5.51 | 4.25 | 1.30 | 0.195 | 0.837 | n.s. |
| 3 to 3 - 3 to 5 | 1.69 | 4.28 | 0.39 | 0.694 | 0.971 | n.s. |
| 3 to 3 - 3 to 6 | 1.53 | 4.30 | 0.35 | 0.723 | 0.971 | n.s. |
| 3 to 4 - 3 to 5 | -3.82 | 4.26 | -0.90 | 0.370 | 0.926 | n.s. |
| 3 to 4 - 3 to 6 | -3.98 | 4.28 | -0.93 | 0.352 | 0.926 | n.s. |
| 3 to 5 - 3 to 6 | -0.16 | 4.25 | -0.04 | 0.970 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.18, *p* = 0.010, η²_G = 0.059
- Greenhouse-Geisser corrected: *p* = 0.027 (ε = 0.636)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 1.15 | 23 | = 0.464 | 0.31 [-0.19, 0.66] | small | n.s. |
| 3 to 1 vs 3 to 3 | 3.23 | 23 | = 0.019 | 0.56 [0.19, 1.13] | medium | * |
| 3 to 1 vs 3 to 4 | 4.01 | 23 | = 0.008 | 0.89 [0.33, 1.31] | large | ** |
| 3 to 1 vs 3 to 5 | 3.39 | 23 | = 0.019 | 0.58 [0.22, 1.16] | medium | * |
| 3 to 1 vs 3 to 6 | 2.53 | 23 | = 0.071 | 0.63 [0.07, 0.97] | medium | n.s. |
| 3 to 2 vs 3 to 3 | 1.07 | 23 | = 0.464 | 0.19 [-0.21, 0.64] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 1.90 | 23 | = 0.210 | 0.45 [-0.05, 0.83] | small | n.s. |
| 3 to 2 vs 3 to 5 | 1.04 | 23 | = 0.464 | 0.24 [-0.21, 0.64] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.53 | 23 | = 0.299 | 0.25 [-0.12, 0.74] | small | n.s. |
| 3 to 3 vs 3 to 4 | 1.66 | 23 | = 0.277 | 0.29 [-0.10, 0.77] | small | n.s. |
| 3 to 3 vs 3 to 5 | 0.38 | 23 | = 0.755 | 0.08 [-0.34, 0.50] | negligible | n.s. |
| 3 to 3 vs 3 to 6 | 0.48 | 23 | = 0.730 | 0.08 [-0.32, 0.52] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.66 | 23 | = 0.642 | -0.18 [-0.56, 0.29] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -0.88 | 23 | = 0.527 | -0.20 [-0.61, 0.25] | small | n.s. |
| 3 to 5 vs 3 to 6 | -0.04 | 23 | = 0.970 | -0.01 [-0.43, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 605.51, BIC = 632.24
- **3 to 2 vs 3 to 1**: *β* = -0.75, *SE* = 0.492, *z* = -1.516, *p* = 0.129
- **3 to 3 vs 3 to 1**: *β* = -0.43, *SE* = 0.478, *z* = -0.905, *p* = 0.365
- **3 to 4 vs 3 to 1**: *β* = -0.85, *SE* = 0.481, *z* = -1.773, *p* = 0.076
- **3 to 5 vs 3 to 1**: *β* = -0.46, *SE* = 0.490, *z* = -0.933, *p* = 0.351
- **3 to 6 vs 3 to 1**: *β* = -1.60, *SE* = 0.496, *z* = -3.219, *p* = 0.001
- **SNR**: *β* = -0.47, *SE* = 0.068, *z* = -6.983, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.75 | 0.49 | 1.52 | 0.129 | 0.718 | n.s. |
| 3 to 1 - 3 to 3 | 0.43 | 0.48 | 0.91 | 0.365 | 0.968 | n.s. |
| 3 to 1 - 3 to 4 | 0.85 | 0.48 | 1.77 | 0.076 | 0.593 | n.s. |
| 3 to 1 - 3 to 5 | 0.46 | 0.49 | 0.93 | 0.351 | 0.968 | n.s. |
| 3 to 1 - 3 to 6 | 1.60 | 0.50 | 3.22 | 0.001 | 0.019 | * |
| 3 to 2 - 3 to 3 | -0.31 | 0.48 | -0.66 | 0.511 | 0.968 | n.s. |
| 3 to 2 - 3 to 4 | 0.11 | 0.47 | 0.23 | 0.821 | 0.968 | n.s. |
| 3 to 2 - 3 to 5 | -0.29 | 0.47 | -0.61 | 0.542 | 0.968 | n.s. |
| 3 to 2 - 3 to 6 | 0.85 | 0.47 | 1.80 | 0.072 | 0.593 | n.s. |
| 3 to 3 - 3 to 4 | 0.42 | 0.47 | 0.89 | 0.374 | 0.968 | n.s. |
| 3 to 3 - 3 to 5 | 0.02 | 0.48 | 0.05 | 0.959 | 0.968 | n.s. |
| 3 to 3 - 3 to 6 | 1.16 | 0.48 | 2.43 | 0.015 | 0.192 | n.s. |
| 3 to 4 - 3 to 5 | -0.40 | 0.47 | -0.84 | 0.404 | 0.968 | n.s. |
| 3 to 4 - 3 to 6 | 0.74 | 0.48 | 1.56 | 0.119 | 0.718 | n.s. |
| 3 to 5 - 3 to 6 | 1.14 | 0.47 | 2.41 | 0.016 | 0.192 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.07, *p* < .001, η²_G = 0.091
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 2.88 | 23 | = 0.032 | 0.64 [0.13, 1.05] | medium | * |
| 3 to 1 vs 3 to 3 | 1.57 | 23 | = 0.195 | 0.39 [-0.11, 0.75] | small | n.s. |
| 3 to 1 vs 3 to 4 | 3.02 | 23 | = 0.030 | 0.59 [0.16, 1.08] | medium | * |
| 3 to 1 vs 3 to 5 | 1.96 | 23 | = 0.120 | 0.49 [-0.04, 0.84] | small | n.s. |
| 3 to 1 vs 3 to 6 | 3.44 | 23 | = 0.030 | 0.93 [0.23, 1.17] | large | * |
| 3 to 2 vs 3 to 3 | -1.95 | 23 | = 0.120 | -0.33 [-0.84, 0.04] | small | n.s. |
| 3 to 2 vs 3 to 4 | -0.49 | 23 | = 0.674 | -0.09 [-0.52, 0.32] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -0.64 | 23 | = 0.609 | -0.12 [-0.55, 0.29] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 1.81 | 23 | = 0.138 | 0.34 [-0.07, 0.81] | small | n.s. |
| 3 to 3 vs 3 to 4 | 1.11 | 23 | = 0.380 | 0.26 [-0.20, 0.65] | small | n.s. |
| 3 to 3 vs 3 to 5 | 0.97 | 23 | = 0.430 | 0.18 [-0.23, 0.62] | negligible | n.s. |
| 3 to 3 vs 3 to 6 | 3.14 | 23 | = 0.030 | 0.68 [0.18, 1.11] | medium | * |
| 3 to 4 vs 3 to 5 | -0.23 | 23 | = 0.819 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 2.06 | 23 | = 0.120 | 0.44 [-0.02, 0.86] | small | n.s. |
| 3 to 5 vs 3 to 6 | 2.39 | 23 | = 0.076 | 0.45 [0.04, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1075.58, BIC = 1102.31
- **3 to 2 vs 3 to 1**: *β* = -3.26, *SE* = 2.619, *z* = -1.245, *p* = 0.213
- **3 to 3 vs 3 to 1**: *β* = -1.77, *SE* = 2.618, *z* = -0.676, *p* = 0.499
- **3 to 4 vs 3 to 1**: *β* = -5.22, *SE* = 2.626, *z* = -1.987, *p* = 0.047
- **3 to 5 vs 3 to 1**: *β* = -5.73, *SE* = 2.618, *z* = -2.189, *p* = 0.029
- **3 to 6 vs 3 to 1**: *β* = -5.59, *SE* = 2.619, *z* = -2.136, *p* = 0.033
- **SNR**: *β* = 0.23, *SE* = 0.480, *z* = 0.482, *p* = 0.630

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 3.26 | 2.62 | 1.24 | 0.213 | 0.885 | n.s. |
| 3 to 1 - 3 to 3 | 1.77 | 2.62 | 0.68 | 0.499 | 0.974 | n.s. |
| 3 to 1 - 3 to 4 | 5.22 | 2.63 | 1.99 | 0.047 | 0.465 | n.s. |
| 3 to 1 - 3 to 5 | 5.73 | 2.62 | 2.19 | 0.029 | 0.353 | n.s. |
| 3 to 1 - 3 to 6 | 5.59 | 2.62 | 2.14 | 0.033 | 0.372 | n.s. |
| 3 to 2 - 3 to 3 | -1.49 | 2.61 | -0.57 | 0.569 | 0.974 | n.s. |
| 3 to 2 - 3 to 4 | 1.96 | 2.62 | 0.75 | 0.454 | 0.974 | n.s. |
| 3 to 2 - 3 to 5 | 2.47 | 2.63 | 0.94 | 0.348 | 0.967 | n.s. |
| 3 to 2 - 3 to 6 | 2.33 | 2.61 | 0.89 | 0.372 | 0.967 | n.s. |
| 3 to 3 - 3 to 4 | 3.45 | 2.62 | 1.32 | 0.188 | 0.875 | n.s. |
| 3 to 3 - 3 to 5 | 3.96 | 2.63 | 1.51 | 0.132 | 0.816 | n.s. |
| 3 to 3 - 3 to 6 | 3.83 | 2.61 | 1.46 | 0.143 | 0.818 | n.s. |
| 3 to 4 - 3 to 5 | 0.51 | 2.64 | 0.19 | 0.846 | 0.996 | n.s. |
| 3 to 4 - 3 to 6 | 0.38 | 2.62 | 0.14 | 0.885 | 0.996 | n.s. |
| 3 to 5 - 3 to 6 | -0.14 | 2.63 | -0.05 | 0.959 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.55, *p* = 0.179, η²_G = 0.047
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 1.33 | 23 | = 0.418 | 0.35 [-0.16, 0.70] | small | n.s. |
| 3 to 1 vs 3 to 3 | 0.60 | 23 | = 0.696 | 0.18 [-0.30, 0.55] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | 1.83 | 23 | = 0.402 | 0.57 [-0.06, 0.81] | medium | n.s. |
| 3 to 1 vs 3 to 5 | 2.03 | 23 | = 0.402 | 0.58 [-0.02, 0.86] | medium | n.s. |
| 3 to 1 vs 3 to 6 | 1.97 | 23 | = 0.402 | 0.59 [-0.04, 0.84] | medium | n.s. |
| 3 to 2 vs 3 to 3 | -0.61 | 23 | = 0.696 | -0.15 [-0.55, 0.30] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 0.70 | 23 | = 0.696 | 0.21 [-0.28, 0.57] | small | n.s. |
| 3 to 2 vs 3 to 5 | 0.80 | 23 | = 0.696 | 0.23 [-0.26, 0.59] | small | n.s. |
| 3 to 2 vs 3 to 6 | 0.96 | 23 | = 0.655 | 0.24 [-0.23, 0.62] | small | n.s. |
| 3 to 3 vs 3 to 4 | 1.50 | 23 | = 0.418 | 0.35 [-0.12, 0.74] | small | n.s. |
| 3 to 3 vs 3 to 5 | 1.62 | 23 | = 0.418 | 0.37 [-0.10, 0.76] | small | n.s. |
| 3 to 3 vs 3 to 6 | 1.34 | 23 | = 0.418 | 0.38 [-0.16, 0.70] | small | n.s. |
| 3 to 4 vs 3 to 5 | 0.13 | 23 | = 0.962 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.14 | 23 | = 0.962 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 649.56, BIC = 676.29
- **3 to 2 vs 3 to 1**: *β* = -2.06, *SE* = 0.571, *z* = -3.616, *p* < .001
- **3 to 3 vs 3 to 1**: *β* = -1.16, *SE* = 0.571, *z* = -2.038, *p* = 0.042
- **3 to 4 vs 3 to 1**: *β* = -0.45, *SE* = 0.572, *z* = -0.792, *p* = 0.428
- **3 to 5 vs 3 to 1**: *β* = -1.81, *SE* = 0.571, *z* = -3.167, *p* = 0.002
- **3 to 6 vs 3 to 1**: *β* = -1.06, *SE* = 0.571, *z* = -1.851, *p* = 0.064
- **SNR**: *β* = 0.39, *SE* = 0.107, *z* = 3.637, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 2.06 | 0.57 | 3.62 | < .001 | 0.004 | ** |
| 3 to 1 - 3 to 3 | 1.16 | 0.57 | 2.04 | 0.042 | 0.373 | n.s. |
| 3 to 1 - 3 to 4 | 0.45 | 0.57 | 0.79 | 0.428 | 0.813 | n.s. |
| 3 to 1 - 3 to 5 | 1.81 | 0.57 | 3.17 | 0.002 | 0.021 | * |
| 3 to 1 - 3 to 6 | 1.06 | 0.57 | 1.85 | 0.064 | 0.484 | n.s. |
| 3 to 2 - 3 to 3 | -0.90 | 0.57 | -1.58 | 0.114 | 0.619 | n.s. |
| 3 to 2 - 3 to 4 | -1.61 | 0.57 | -2.82 | 0.005 | 0.060 | n.s. |
| 3 to 2 - 3 to 5 | -0.26 | 0.57 | -0.45 | 0.654 | 0.880 | n.s. |
| 3 to 2 - 3 to 6 | -1.01 | 0.57 | -1.77 | 0.077 | 0.515 | n.s. |
| 3 to 3 - 3 to 4 | -0.71 | 0.57 | -1.24 | 0.214 | 0.772 | n.s. |
| 3 to 3 - 3 to 5 | 0.64 | 0.57 | 1.12 | 0.261 | 0.779 | n.s. |
| 3 to 3 - 3 to 6 | -0.11 | 0.57 | -0.19 | 0.853 | 0.880 | n.s. |
| 3 to 4 - 3 to 5 | 1.35 | 0.58 | 2.35 | 0.019 | 0.203 | n.s. |
| 3 to 4 - 3 to 6 | 0.60 | 0.57 | 1.06 | 0.290 | 0.779 | n.s. |
| 3 to 5 - 3 to 6 | -0.75 | 0.57 | -1.31 | 0.191 | 0.772 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.25, *p* = 0.009, η²_G = 0.078
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 3.73 | 23 | = 0.017 | 0.97 [0.28, 1.24] | large | * |
| 3 to 1 vs 3 to 3 | 1.96 | 23 | = 0.173 | 0.50 [-0.04, 0.84] | small | n.s. |
| 3 to 1 vs 3 to 4 | 1.10 | 23 | = 0.472 | 0.30 [-0.20, 0.65] | small | n.s. |
| 3 to 1 vs 3 to 5 | 2.58 | 23 | = 0.086 | 0.72 [0.08, 0.98] | medium | n.s. |
| 3 to 1 vs 3 to 6 | 1.59 | 23 | = 0.234 | 0.49 [-0.11, 0.76] | small | n.s. |
| 3 to 2 vs 3 to 3 | -1.80 | 23 | = 0.181 | -0.35 [-0.80, 0.07] | small | n.s. |
| 3 to 2 vs 3 to 4 | -2.57 | 23 | = 0.086 | -0.68 [-0.97, -0.07] | medium | n.s. |
| 3 to 2 vs 3 to 5 | -0.87 | 23 | = 0.490 | -0.20 [-0.60, 0.25] | small | n.s. |
| 3 to 2 vs 3 to 6 | -2.03 | 23 | = 0.173 | -0.41 [-0.85, 0.03] | small | n.s. |
| 3 to 3 vs 3 to 4 | -1.01 | 23 | = 0.484 | -0.24 [-0.63, 0.22] | small | n.s. |
| 3 to 3 vs 3 to 5 | 0.74 | 23 | = 0.501 | 0.16 [-0.27, 0.58] | negligible | n.s. |
| 3 to 3 vs 3 to 6 | -0.15 | 23 | = 0.878 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | 1.91 | 23 | = 0.173 | 0.44 [-0.05, 0.83] | small | n.s. |
| 3 to 4 vs 3 to 6 | 0.87 | 23 | = 0.490 | 0.22 [-0.25, 0.60] | small | n.s. |
| 3 to 5 vs 3 to 6 | -0.76 | 23 | = 0.501 | -0.20 [-0.58, 0.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1443.46, BIC = 1470.19
- **3 to 2 vs 3 to 1**: *β* = 2.25, *SE* = 9.289, *z* = 0.242, *p* = 0.809
- **3 to 3 vs 3 to 1**: *β* = -13.50, *SE* = 9.354, *z* = -1.443, *p* = 0.149
- **3 to 4 vs 3 to 1**: *β* = 9.05, *SE* = 9.114, *z* = 0.993, *p* = 0.321
- **3 to 5 vs 3 to 1**: *β* = -0.28, *SE* = 9.296, *z* = -0.030, *p* = 0.976
- **3 to 6 vs 3 to 1**: *β* = 6.92, *SE* = 9.330, *z* = 0.742, *p* = 0.458
- **SNR**: *β* = -0.61, *SE* = 0.699, *z* = -0.875, *p* = 0.381

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -2.25 | 9.29 | -0.24 | 0.809 | 0.998 | n.s. |
| 3 to 1 - 3 to 3 | 13.50 | 9.35 | 1.44 | 0.149 | 0.848 | n.s. |
| 3 to 1 - 3 to 4 | -9.05 | 9.11 | -0.99 | 0.321 | 0.975 | n.s. |
| 3 to 1 - 3 to 5 | 0.28 | 9.30 | 0.03 | 0.976 | 0.998 | n.s. |
| 3 to 1 - 3 to 6 | -6.92 | 9.33 | -0.74 | 0.458 | 0.988 | n.s. |
| 3 to 2 - 3 to 3 | 15.75 | 9.07 | 1.74 | 0.083 | 0.674 | n.s. |
| 3 to 2 - 3 to 4 | -6.81 | 9.14 | -0.74 | 0.456 | 0.988 | n.s. |
| 3 to 2 - 3 to 5 | 2.53 | 9.07 | 0.28 | 0.781 | 0.998 | n.s. |
| 3 to 2 - 3 to 6 | -4.67 | 9.07 | -0.52 | 0.606 | 0.991 | n.s. |
| 3 to 3 - 3 to 4 | -22.55 | 9.18 | -2.46 | 0.014 | 0.190 | n.s. |
| 3 to 3 - 3 to 5 | -13.22 | 9.07 | -1.46 | 0.145 | 0.848 | n.s. |
| 3 to 3 - 3 to 6 | -20.42 | 9.07 | -2.25 | 0.024 | 0.292 | n.s. |
| 3 to 4 - 3 to 5 | 9.33 | 9.14 | 1.02 | 0.307 | 0.975 | n.s. |
| 3 to 4 - 3 to 6 | 2.13 | 9.16 | 0.23 | 0.816 | 0.998 | n.s. |
| 3 to 5 - 3 to 6 | -7.20 | 9.07 | -0.79 | 0.427 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.234, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.47 | 23 | = 0.803 | -0.12 [-0.52, 0.33] | negligible | n.s. |
| 3 to 1 vs 3 to 3 | 1.32 | 23 | = 0.687 | 0.36 [-0.16, 0.70] | small | n.s. |
| 3 to 1 vs 3 to 4 | -1.10 | 23 | = 0.687 | -0.28 [-0.65, 0.20] | small | n.s. |
| 3 to 1 vs 3 to 5 | -0.19 | 23 | = 0.910 | -0.04 [-0.46, 0.38] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | -0.92 | 23 | = 0.687 | -0.24 [-0.61, 0.24] | small | n.s. |
| 3 to 2 vs 3 to 3 | 1.86 | 23 | = 0.379 | 0.46 [-0.06, 0.82] | small | n.s. |
| 3 to 2 vs 3 to 4 | -0.64 | 23 | = 0.791 | -0.16 [-0.56, 0.29] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.23 | 23 | = 0.910 | 0.07 [-0.38, 0.47] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | -0.56 | 23 | = 0.793 | -0.13 [-0.54, 0.31] | negligible | n.s. |
| 3 to 3 vs 3 to 4 | -2.30 | 23 | = 0.240 | -0.60 [-0.92, -0.03] | medium | n.s. |
| 3 to 3 vs 3 to 5 | -1.23 | 23 | = 0.687 | -0.35 [-0.68, 0.18] | small | n.s. |
| 3 to 3 vs 3 to 6 | -2.28 | 23 | = 0.240 | -0.55 [-0.91, -0.02] | medium | n.s. |
| 3 to 4 vs 3 to 5 | 1.01 | 23 | = 0.687 | 0.21 [-0.22, 0.63] | small | n.s. |
| 3 to 4 vs 3 to 6 | 0.10 | 23 | = 0.923 | 0.03 [-0.40, 0.44] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | -0.68 | 23 | = 0.791 | -0.18 [-0.56, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 740.68, BIC = 767.41
- **3 to 2 vs 3 to 1**: *β* = 0.48, *SE* = 0.733, *z* = 0.651, *p* = 0.515
- **3 to 3 vs 3 to 1**: *β* = -1.88, *SE* = 0.739, *z* = -2.549, *p* = 0.011
- **3 to 4 vs 3 to 1**: *β* = -0.69, *SE* = 0.718, *z* = -0.966, *p* = 0.334
- **3 to 5 vs 3 to 1**: *β* = -0.62, *SE* = 0.734, *z* = -0.839, *p* = 0.401
- **3 to 6 vs 3 to 1**: *β* = -0.65, *SE* = 0.737, *z* = -0.877, *p* = 0.381
- **SNR**: *β* = 0.12, *SE* = 0.058, *z* = 2.141, *p* = 0.032

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -0.48 | 0.73 | -0.65 | 0.515 | 0.945 | n.s. |
| 3 to 1 - 3 to 3 | 1.88 | 0.74 | 2.55 | 0.011 | 0.141 | n.s. |
| 3 to 1 - 3 to 4 | 0.69 | 0.72 | 0.97 | 0.334 | 0.942 | n.s. |
| 3 to 1 - 3 to 5 | 0.62 | 0.73 | 0.84 | 0.401 | 0.944 | n.s. |
| 3 to 1 - 3 to 6 | 0.65 | 0.74 | 0.88 | 0.381 | 0.944 | n.s. |
| 3 to 2 - 3 to 3 | 2.36 | 0.71 | 3.31 | < .001 | 0.014 | * |
| 3 to 2 - 3 to 4 | 1.17 | 0.72 | 1.63 | 0.104 | 0.686 | n.s. |
| 3 to 2 - 3 to 5 | 1.09 | 0.71 | 1.53 | 0.126 | 0.686 | n.s. |
| 3 to 2 - 3 to 6 | 1.12 | 0.71 | 1.57 | 0.116 | 0.686 | n.s. |
| 3 to 3 - 3 to 4 | -1.19 | 0.72 | -1.65 | 0.100 | 0.686 | n.s. |
| 3 to 3 - 3 to 5 | -1.27 | 0.71 | -1.77 | 0.076 | 0.642 | n.s. |
| 3 to 3 - 3 to 6 | -1.24 | 0.71 | -1.73 | 0.083 | 0.647 | n.s. |
| 3 to 4 - 3 to 5 | -0.08 | 0.72 | -0.11 | 0.914 | 0.999 | n.s. |
| 3 to 4 - 3 to 6 | -0.05 | 0.72 | -0.07 | 0.948 | 0.999 | n.s. |
| 3 to 5 - 3 to 6 | 0.03 | 0.71 | 0.04 | 0.966 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.76, *p* = 0.021, η²_G = 0.040
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.15 | 23 | = 0.932 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| 3 to 1 vs 3 to 3 | 2.99 | 23 | = 0.068 | 0.66 [0.15, 1.07] | medium | n.s. |
| 3 to 1 vs 3 to 4 | 1.04 | 23 | = 0.422 | 0.20 [-0.21, 0.64] | small | n.s. |
| 3 to 1 vs 3 to 5 | 1.51 | 23 | = 0.273 | 0.24 [-0.12, 0.74] | small | n.s. |
| 3 to 1 vs 3 to 6 | 1.58 | 23 | = 0.273 | 0.31 [-0.11, 0.76] | small | n.s. |
| 3 to 2 vs 3 to 3 | 2.85 | 23 | = 0.068 | 0.62 [0.13, 1.04] | medium | n.s. |
| 3 to 2 vs 3 to 4 | 1.28 | 23 | = 0.318 | 0.21 [-0.17, 0.69] | small | n.s. |
| 3 to 2 vs 3 to 5 | 1.70 | 23 | = 0.273 | 0.25 [-0.09, 0.78] | small | n.s. |
| 3 to 2 vs 3 to 6 | 2.07 | 23 | = 0.187 | 0.31 [-0.02, 0.86] | small | n.s. |
| 3 to 3 vs 3 to 4 | -1.40 | 23 | = 0.291 | -0.35 [-0.72, 0.14] | small | n.s. |
| 3 to 3 vs 3 to 5 | -1.65 | 23 | = 0.273 | -0.34 [-0.77, 0.10] | small | n.s. |
| 3 to 3 vs 3 to 6 | -2.10 | 23 | = 0.187 | -0.40 [-0.87, 0.01] | small | n.s. |
| 3 to 4 vs 3 to 5 | 0.18 | 23 | = 0.932 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.26 | 23 | = 0.932 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.09 | 23 | = 0.932 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - 3 to 1 showed greater latency than 3 to 3 (*d* = 0.56)
  - 3 to 1 showed greater latency than 3 to 4 (*d* = 0.89)
  - 3 to 1 showed greater latency than 3 to 5 (*d* = 0.58)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 3 to 2 (*d* = 0.64)
  - 3 to 1 showed greater amplitude than 3 to 4 (*d* = 0.59)
  - 3 to 1 showed greater amplitude than 3 to 6 (*d* = 0.93)
  - 3 to 3 showed greater amplitude than 3 to 6 (*d* = 0.68)
**P1 amplitude:** Significant main effect of condition (*p* = 0.009). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 3 to 2 (*d* = 0.97)
**P3b amplitude:** Significant main effect of condition (*p* = 0.021) (no significant pairwise comparisons)

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
