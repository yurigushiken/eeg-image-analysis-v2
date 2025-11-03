# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:47:01

---

## 1. Analysis Overview

**Total Measurements:** 364
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
| 3a | 5 | 100.00 ms | 8.00 | 3.58 | [88.00, 108.00] |
| 3b | 10 | 98.80 ms | 11.00 | 3.48 | [88.00, 116.00] |
| 3c | 10 | 95.60 ms | 11.23 | 3.55 | [88.00, 116.00] |
| 3d | 4 | 111.00 ms | 7.57 | 3.79 | [100.00, 116.00] |
| 3e | 12 | 99.67 ms | 10.85 | 3.13 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 5 | 4.65 µV | 0.85 | 0.38 | [3.79, 5.85] |
| 3b | 10 | 5.00 µV | 3.05 | 0.96 | [2.51, 12.87] |
| 3c | 10 | 3.51 µV | 2.34 | 0.74 | [0.75, 8.61] |
| 3d | 4 | 5.05 µV | 1.88 | 0.94 | [2.69, 7.28] |
| 3e | 12 | 6.87 µV | 3.77 | 1.09 | [1.46, 12.81] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 19 | 165.26 ms | 21.50 | 4.93 | [136.00, 204.00] |
| 3b | 10 | 167.20 ms | 22.05 | 6.97 | [132.00, 204.00] |
| 3c | 18 | 168.89 ms | 21.15 | 4.98 | [140.00, 204.00] |
| 3d | 7 | 150.86 ms | 15.61 | 5.90 | [132.00, 180.00] |
| 3e | 17 | 162.59 ms | 22.62 | 5.49 | [132.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 19 | -7.39 µV | 3.55 | 0.81 | [-13.94, -2.07] |
| 3b | 10 | -6.66 µV | 1.72 | 0.54 | [-8.97, -4.35] |
| 3c | 18 | -6.92 µV | 1.97 | 0.46 | [-10.17, -2.02] |
| 3d | 7 | -10.00 µV | 4.00 | 1.51 | [-16.22, -5.39] |
| 3e | 17 | -9.29 µV | 4.16 | 1.01 | [-19.76, -4.41] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 11 | 84.73 ms | 13.12 | 3.96 | [68.00, 108.00] |
| 3b | 8 | 84.50 ms | 20.11 | 7.11 | [64.00, 108.00] |
| 3c | 12 | 94.33 ms | 12.82 | 3.70 | [68.00, 108.00] |
| 3d | 9 | 88.44 ms | 14.48 | 4.83 | [68.00, 108.00] |
| 3e | 12 | 86.67 ms | 19.09 | 5.51 | [64.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 11 | 5.59 µV | 2.93 | 0.88 | [1.63, 10.25] |
| 3b | 8 | 5.30 µV | 1.63 | 0.58 | [2.86, 7.70] |
| 3c | 12 | 7.39 µV | 5.35 | 1.54 | [1.88, 20.29] |
| 3d | 9 | 6.06 µV | 3.18 | 1.06 | [2.70, 11.23] |
| 3e | 12 | 5.46 µV | 3.03 | 0.88 | [2.64, 12.33] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 9 | 461.78 ms | 60.57 | 20.19 | [392.00, 544.00] |
| 3b | 9 | 458.22 ms | 63.19 | 21.06 | [380.00, 544.00] |
| 3c | 15 | 479.73 ms | 54.42 | 14.05 | [380.00, 544.00] |
| 3d | 5 | 448.80 ms | 37.35 | 16.70 | [400.00, 496.00] |
| 3e | 15 | 482.93 ms | 45.97 | 11.87 | [412.00, 544.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 9 | 7.40 µV | 2.44 | 0.81 | [2.47, 9.90] |
| 3b | 9 | 8.51 µV | 2.63 | 0.88 | [4.16, 13.79] |
| 3c | 15 | 8.57 µV | 5.18 | 1.34 | [2.36, 20.18] |
| 3d | 5 | 7.09 µV | 2.07 | 0.93 | [4.36, 10.17] |
| 3e | 15 | 10.62 µV | 5.68 | 1.47 | [2.75, 22.08] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 319.22, BIC = 332.93
- **3b vs 3a**: *β* = -0.66, *SE* = 5.841, *z* = -0.112, *p* = 0.910
- **3c vs 3a**: *β* = -3.81, *SE* = 5.835, *z* = -0.653, *p* = 0.514
- **3d vs 3a**: *β* = 11.20, *SE* = 6.578, *z* = 1.703, *p* = 0.089
- **3e vs 3a**: *β* = -0.66, *SE* = 5.353, *z* = -0.123, *p* = 0.902
- **SNR**: *β* = 0.92, *SE* = 1.480, *z* = 0.621, *p* = 0.535

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.66 | 5.84 | 0.11 | 0.910 | 0.999 | n.s. |
| 3a - 3c | 3.81 | 5.83 | 0.65 | 0.514 | 0.978 | n.s. |
| 3a - 3d | -11.20 | 6.58 | -1.70 | 0.089 | 0.478 | n.s. |
| 3a - 3e | 0.66 | 5.35 | 0.12 | 0.902 | 0.999 | n.s. |
| 3b - 3c | 3.15 | 4.37 | 0.72 | 0.471 | 0.978 | n.s. |
| 3b - 3d | -11.86 | 6.04 | -1.96 | 0.050 | 0.335 | n.s. |
| 3b - 3e | 0.00 | 4.52 | 0.00 | 1.000 | 1.000 | n.s. |
| 3c - 3d | -15.01 | 6.03 | -2.49 | 0.013 | 0.122 | n.s. |
| 3c - 3e | -3.15 | 4.54 | -0.69 | 0.488 | 0.978 | n.s. |
| 3d - 3e | 11.86 | 5.74 | 2.07 | 0.039 | 0.300 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 203.78, BIC = 217.49
- **3b vs 3a**: *β* = 1.03, *SE* = 1.285, *z* = 0.805, *p* = 0.421
- **3c vs 3a**: *β* = -0.50, *SE* = 1.330, *z* = -0.374, *p* = 0.708
- **3d vs 3a**: *β* = 0.78, *SE* = 1.616, *z* = 0.483, *p* = 0.629
- **3e vs 3a**: *β* = 1.75, *SE* = 1.252, *z* = 1.402, *p* = 0.161
- **SNR**: *β* = 1.29, *SE* = 0.385, *z* = 3.352, *p* = 0.001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -1.03 | 1.28 | -0.81 | 0.421 | 0.971 | n.s. |
| 3a - 3c | 0.50 | 1.33 | 0.37 | 0.708 | 0.971 | n.s. |
| 3a - 3d | -0.78 | 1.62 | -0.48 | 0.629 | 0.971 | n.s. |
| 3a - 3e | -1.75 | 1.25 | -1.40 | 0.161 | 0.778 | n.s. |
| 3b - 3c | 1.53 | 1.08 | 1.43 | 0.154 | 0.778 | n.s. |
| 3b - 3d | 0.25 | 1.44 | 0.18 | 0.860 | 0.971 | n.s. |
| 3b - 3e | -0.72 | 1.05 | -0.69 | 0.493 | 0.971 | n.s. |
| 3c - 3d | -1.28 | 1.51 | -0.85 | 0.397 | 0.971 | n.s. |
| 3c - 3e | -2.25 | 1.10 | -2.06 | 0.040 | 0.334 | n.s. |
| 3d - 3e | -0.97 | 1.39 | -0.70 | 0.485 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 644.97, BIC = 663.07
- **3b vs 3a**: *β* = 2.92, *SE* = 7.716, *z* = 0.379, *p* = 0.705
- **3c vs 3a**: *β* = 4.31, *SE* = 6.392, *z* = 0.674, *p* = 0.500
- **3d vs 3a**: *β* = -13.39, *SE* = 8.762, *z* = -1.528, *p* = 0.126
- **3e vs 3a**: *β* = -0.42, *SE* = 6.881, *z* = -0.060, *p* = 0.952
- **SNR**: *β* = -0.97, *SE* = 1.138, *z* = -0.849, *p* = 0.396

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -2.92 | 7.72 | -0.38 | 0.705 | 0.991 | n.s. |
| 3a - 3c | -4.31 | 6.39 | -0.67 | 0.500 | 0.980 | n.s. |
| 3a - 3d | 13.39 | 8.76 | 1.53 | 0.126 | 0.661 | n.s. |
| 3a - 3e | 0.42 | 6.88 | 0.06 | 0.952 | 0.991 | n.s. |
| 3b - 3c | -1.39 | 7.94 | -0.17 | 0.861 | 0.991 | n.s. |
| 3b - 3d | 16.31 | 9.85 | 1.66 | 0.098 | 0.604 | n.s. |
| 3b - 3e | 3.34 | 8.45 | 0.39 | 0.693 | 0.991 | n.s. |
| 3c - 3d | 17.70 | 8.73 | 2.03 | 0.043 | 0.353 | n.s. |
| 3c - 3e | 4.73 | 6.70 | 0.71 | 0.480 | 0.980 | n.s. |
| 3d - 3e | -12.98 | 9.06 | -1.43 | 0.152 | 0.684 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 353.60, BIC = 371.70
- **3b vs 3a**: *β* = 0.34, *SE* = 0.976, *z* = 0.346, *p* = 0.729
- **3c vs 3a**: *β* = 1.30, *SE* = 0.825, *z* = 1.579, *p* = 0.114
- **3d vs 3a**: *β* = -1.79, *SE* = 1.128, *z* = -1.588, *p* = 0.112
- **3e vs 3a**: *β* = -0.19, *SE* = 0.880, *z* = -0.215, *p* = 0.830
- **SNR**: *β* = -0.78, *SE* = 0.146, *z* = -5.313, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.34 | 0.98 | -0.35 | 0.729 | 0.947 | n.s. |
| 3a - 3c | -1.30 | 0.83 | -1.58 | 0.114 | 0.566 | n.s. |
| 3a - 3d | 1.79 | 1.13 | 1.59 | 0.112 | 0.566 | n.s. |
| 3a - 3e | 0.19 | 0.88 | 0.22 | 0.830 | 0.947 | n.s. |
| 3b - 3c | -0.96 | 1.01 | -0.96 | 0.337 | 0.807 | n.s. |
| 3b - 3d | 2.13 | 1.26 | 1.69 | 0.090 | 0.545 | n.s. |
| 3b - 3e | 0.53 | 1.08 | 0.49 | 0.624 | 0.947 | n.s. |
| 3c - 3d | 3.09 | 1.12 | 2.77 | 0.006 | 0.055 | n.s. |
| 3c - 3e | 1.49 | 0.86 | 1.73 | 0.084 | 0.545 | n.s. |
| 3d - 3e | -1.60 | 1.17 | -1.37 | 0.170 | 0.605 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 439.31, BIC = 454.92
- **3b vs 3a**: *β* = 0.27, *SE* = 6.073, *z* = 0.045, *p* = 0.964
- **3c vs 3a**: *β* = 7.84, *SE* = 5.569, *z* = 1.409, *p* = 0.159
- **3d vs 3a**: *β* = 4.85, *SE* = 5.788, *z* = 0.838, *p* = 0.402
- **3e vs 3a**: *β* = 2.90, *SE* = 5.247, *z* = 0.553, *p* = 0.580
- **SNR**: *β* = 2.83, *SE* = 2.465, *z* = 1.147, *p* = 0.252

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.27 | 6.07 | -0.04 | 0.964 | 0.987 | n.s. |
| 3a - 3c | -7.84 | 5.57 | -1.41 | 0.159 | 0.823 | n.s. |
| 3a - 3d | -4.85 | 5.79 | -0.84 | 0.402 | 0.978 | n.s. |
| 3a - 3e | -2.90 | 5.25 | -0.55 | 0.580 | 0.987 | n.s. |
| 3b - 3c | -7.57 | 5.84 | -1.30 | 0.195 | 0.858 | n.s. |
| 3b - 3d | -4.58 | 6.54 | -0.70 | 0.484 | 0.981 | n.s. |
| 3b - 3e | -2.63 | 5.98 | -0.44 | 0.660 | 0.987 | n.s. |
| 3c - 3d | 2.99 | 6.05 | 0.49 | 0.621 | 0.987 | n.s. |
| 3c - 3e | 4.94 | 5.61 | 0.88 | 0.378 | 0.978 | n.s. |
| 3d - 3e | 1.95 | 5.74 | 0.34 | 0.734 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 273.16, BIC = 288.77
- **3b vs 3a**: *β* = -1.10, *SE* = 1.232, *z* = -0.897, *p* = 0.370
- **3c vs 3a**: *β* = 0.15, *SE* = 1.139, *z* = 0.136, *p* = 0.892
- **3d vs 3a**: *β* = 0.79, *SE* = 1.171, *z* = 0.675, *p* = 0.500
- **3e vs 3a**: *β* = -0.41, *SE* = 1.074, *z* = -0.381, *p* = 0.703
- **SNR**: *β* = 2.35, *SE* = 0.495, *z* = 4.740, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 1.11 | 1.23 | 0.90 | 0.370 | 0.960 | n.s. |
| 3a - 3c | -0.15 | 1.14 | -0.14 | 0.892 | 0.984 | n.s. |
| 3a - 3d | -0.79 | 1.17 | -0.67 | 0.500 | 0.984 | n.s. |
| 3a - 3e | 0.41 | 1.07 | 0.38 | 0.703 | 0.984 | n.s. |
| 3b - 3c | -1.26 | 1.18 | -1.07 | 0.285 | 0.951 | n.s. |
| 3b - 3d | -1.89 | 1.33 | -1.42 | 0.154 | 0.813 | n.s. |
| 3b - 3e | -0.70 | 1.21 | -0.58 | 0.565 | 0.984 | n.s. |
| 3c - 3d | -0.64 | 1.24 | -0.51 | 0.608 | 0.984 | n.s. |
| 3c - 3e | 0.56 | 1.13 | 0.50 | 0.619 | 0.984 | n.s. |
| 3d - 3e | 1.20 | 1.18 | 1.02 | 0.308 | 0.951 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 580.25, BIC = 596.01
- **3b vs 3a**: *β* = -3.51, *SE* = 22.106, *z* = -0.159, *p* = 0.874
- **3c vs 3a**: *β* = 16.95, *SE* = 19.988, *z* = 0.848, *p* = 0.396
- **3d vs 3a**: *β* = -12.07, *SE* = 26.726, *z* = -0.452, *p* = 0.652
- **3e vs 3a**: *β* = 24.99, *SE* = 20.227, *z* = 1.236, *p* = 0.217
- **SNR**: *β* = -2.08, *SE* = 2.176, *z* = -0.956, *p* = 0.339

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 3.51 | 22.11 | 0.16 | 0.874 | 0.983 | n.s. |
| 3a - 3c | -16.95 | 19.99 | -0.85 | 0.396 | 0.920 | n.s. |
| 3a - 3d | 12.07 | 26.73 | 0.45 | 0.652 | 0.983 | n.s. |
| 3a - 3e | -24.99 | 20.23 | -1.24 | 0.217 | 0.858 | n.s. |
| 3b - 3c | -20.47 | 19.71 | -1.04 | 0.299 | 0.881 | n.s. |
| 3b - 3d | 8.56 | 27.00 | 0.32 | 0.751 | 0.983 | n.s. |
| 3b - 3e | -28.51 | 20.61 | -1.38 | 0.167 | 0.806 | n.s. |
| 3c - 3d | 29.02 | 25.19 | 1.15 | 0.249 | 0.866 | n.s. |
| 3c - 3e | -8.04 | 17.15 | -0.47 | 0.639 | 0.983 | n.s. |
| 3d - 3e | -37.06 | 25.67 | -1.44 | 0.149 | 0.800 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.14, BIC = 295.91
- **3b vs 3a**: *β* = 1.64, *SE* = 1.164, *z* = 1.406, *p* = 0.160
- **3c vs 3a**: *β* = 0.22, *SE* = 1.079, *z* = 0.203, *p* = 0.839
- **3d vs 3a**: *β* = 1.28, *SE* = 1.460, *z* = 0.875, *p* = 0.382
- **3e vs 3a**: *β* = 0.97, *SE* = 1.071, *z* = 0.909, *p* = 0.363
- **SNR**: *β* = 0.90, *SE* = 0.115, *z* = 7.810, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -1.64 | 1.16 | -1.41 | 0.160 | 0.825 | n.s. |
| 3a - 3c | -0.22 | 1.08 | -0.20 | 0.839 | 0.993 | n.s. |
| 3a - 3d | -1.28 | 1.46 | -0.87 | 0.382 | 0.973 | n.s. |
| 3a - 3e | -0.97 | 1.07 | -0.91 | 0.363 | 0.973 | n.s. |
| 3b - 3c | 1.42 | 1.01 | 1.40 | 0.162 | 0.825 | n.s. |
| 3b - 3d | 0.36 | 1.51 | 0.24 | 0.812 | 0.993 | n.s. |
| 3b - 3e | 0.66 | 1.07 | 0.62 | 0.537 | 0.973 | n.s. |
| 3c - 3d | -1.06 | 1.44 | -0.73 | 0.463 | 0.973 | n.s. |
| 3c - 3e | -0.75 | 0.89 | -0.85 | 0.396 | 0.973 | n.s. |
| 3d - 3e | 0.30 | 1.44 | 0.21 | 0.833 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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
