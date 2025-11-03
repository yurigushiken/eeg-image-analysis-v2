# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:50:19

---

## 1. Analysis Overview

**Total Measurements:** 460
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
| Ratio 0.5 (1:2, no 1) | 9 | 100.00 ms | 9.38 | 3.13 | [92.00, 112.00] |
| Ratio 0.67 (2:3, no 1) | 9 | 105.33 ms | 7.75 | 2.58 | [92.00, 112.00] |
| Ratio 0.75 (3:4, no 1) | 12 | 100.33 ms | 9.41 | 2.72 | [92.00, 112.00] |
| Ratio 0.8 (4:5, no 1) | 8 | 98.00 ms | 8.82 | 3.12 | [92.00, 112.00] |
| Ratio 0.83 (5:6, no 1) | 4 | 99.00 ms | 8.87 | 4.43 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 9 | 1.43 µV | 0.80 | 0.27 | [0.42, 2.63] |
| Ratio 0.67 (2:3, no 1) | 9 | 1.40 µV | 0.80 | 0.27 | [0.37, 2.79] |
| Ratio 0.75 (3:4, no 1) | 12 | 1.55 µV | 1.32 | 0.38 | [0.42, 5.25] |
| Ratio 0.8 (4:5, no 1) | 8 | 1.98 µV | 1.27 | 0.45 | [0.60, 4.16] |
| Ratio 0.83 (5:6, no 1) | 4 | 4.36 µV | 1.68 | 0.84 | [2.15, 6.18] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 23 | 171.30 ms | 14.90 | 3.11 | [140.00, 196.00] |
| Ratio 0.67 (2:3, no 1) | 23 | 171.83 ms | 18.59 | 3.88 | [144.00, 200.00] |
| Ratio 0.75 (3:4, no 1) | 22 | 172.73 ms | 19.43 | 4.14 | [140.00, 204.00] |
| Ratio 0.8 (4:5, no 1) | 22 | 170.91 ms | 18.85 | 4.02 | [140.00, 204.00] |
| Ratio 0.83 (5:6, no 1) | 17 | 176.24 ms | 21.79 | 5.29 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 23 | -6.00 µV | 2.16 | 0.45 | [-10.43, -2.77] |
| Ratio 0.67 (2:3, no 1) | 23 | -5.33 µV | 2.35 | 0.49 | [-10.09, -2.11] |
| Ratio 0.75 (3:4, no 1) | 22 | -5.98 µV | 1.84 | 0.39 | [-10.31, -3.43] |
| Ratio 0.8 (4:5, no 1) | 22 | -6.06 µV | 2.68 | 0.57 | [-11.24, -2.10] |
| Ratio 0.83 (5:6, no 1) | 17 | -6.46 µV | 2.41 | 0.58 | [-11.29, -2.31] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 14 | 108.29 ms | 7.76 | 2.07 | [96.00, 116.00] |
| Ratio 0.67 (2:3, no 1) | 11 | 109.45 ms | 7.43 | 2.24 | [96.00, 116.00] |
| Ratio 0.75 (3:4, no 1) | 11 | 108.00 ms | 8.00 | 2.41 | [96.00, 116.00] |
| Ratio 0.8 (4:5, no 1) | 16 | 106.75 ms | 6.96 | 1.74 | [96.00, 116.00] |
| Ratio 0.83 (5:6, no 1) | 11 | 109.09 ms | 7.40 | 2.23 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 14 | 2.18 µV | 1.36 | 0.36 | [0.31, 4.97] |
| Ratio 0.67 (2:3, no 1) | 11 | 2.45 µV | 1.61 | 0.48 | [0.64, 5.72] |
| Ratio 0.75 (3:4, no 1) | 11 | 2.66 µV | 1.43 | 0.43 | [1.16, 5.67] |
| Ratio 0.8 (4:5, no 1) | 16 | 2.97 µV | 1.79 | 0.45 | [0.46, 6.17] |
| Ratio 0.83 (5:6, no 1) | 11 | 4.04 µV | 4.38 | 1.32 | [0.74, 16.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 495.40 ms | 30.88 | 6.91 | [444.00, 540.00] |
| Ratio 0.67 (2:3, no 1) | 19 | 492.63 ms | 35.43 | 8.13 | [444.00, 540.00] |
| Ratio 0.75 (3:4, no 1) | 18 | 492.89 ms | 34.31 | 8.09 | [444.00, 540.00] |
| Ratio 0.8 (4:5, no 1) | 19 | 495.79 ms | 34.06 | 7.81 | [444.00, 540.00] |
| Ratio 0.83 (5:6, no 1) | 12 | 510.33 ms | 30.48 | 8.80 | [448.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 4.70 µV | 2.76 | 0.62 | [0.32, 10.84] |
| Ratio 0.67 (2:3, no 1) | 19 | 5.16 µV | 3.35 | 0.77 | [0.59, 14.05] |
| Ratio 0.75 (3:4, no 1) | 18 | 5.62 µV | 2.78 | 0.66 | [2.00, 11.73] |
| Ratio 0.8 (4:5, no 1) | 19 | 5.56 µV | 2.87 | 0.66 | [1.81, 10.40] |
| Ratio 0.83 (5:6, no 1) | 12 | 6.59 µV | 4.52 | 1.30 | [1.33, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.40, BIC = 311.30
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.96, *SE* = 2.609, *z* = 0.752, *p* = 0.452
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.42, *SE* = 2.422, *z* = 0.172, *p* = 0.863
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.56, *SE* = 2.503, *z* = -0.621, *p* = 0.534
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -5.89, *SE* = 4.016, *z* = -1.468, *p* = 0.142
- **SNR**: *β* = 2.04, *SE* = 0.990, *z* = 2.061, *p* = 0.039

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -1.96 | 2.61 | -0.75 | 0.452 | 0.943 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.42 | 2.42 | -0.17 | 0.863 | 0.943 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 1.56 | 2.50 | 0.62 | 0.534 | 0.943 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 5.89 | 4.02 | 1.47 | 0.142 | 0.707 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 1.54 | 2.57 | 0.60 | 0.548 | 0.943 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 3.52 | 2.91 | 1.21 | 0.227 | 0.835 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 7.86 | 3.79 | 2.07 | 0.038 | 0.323 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 1.97 | 2.53 | 0.78 | 0.436 | 0.943 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 6.31 | 3.72 | 1.70 | 0.090 | 0.572 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 4.34 | 4.28 | 1.01 | 0.310 | 0.892 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 119.78, BIC = 133.68
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.26, *SE* = 0.375, *z* = -0.697, *p* = 0.486
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.40, *SE* = 0.353, *z* = 1.125, *p* = 0.261
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.64, *SE* = 0.378, *z* = 1.689, *p* = 0.091
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 2.16, *SE* = 0.529, *z* = 4.087, *p* < .001
- **SNR**: *β* = 0.64, *SE* = 0.133, *z* = 4.831, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.26 | 0.37 | 0.70 | 0.486 | 0.736 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.40 | 0.35 | -1.12 | 0.261 | 0.596 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.64 | 0.38 | -1.69 | 0.091 | 0.318 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -2.16 | 0.53 | -4.09 | < .001 | < .001 | *** |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.66 | 0.36 | -1.82 | 0.069 | 0.301 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.90 | 0.40 | -2.27 | 0.023 | 0.132 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -2.42 | 0.51 | -4.73 | < .001 | < .001 | *** |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.24 | 0.36 | -0.67 | 0.506 | 0.736 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -1.76 | 0.51 | -3.44 | < .001 | 0.005 | ** |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -1.52 | 0.55 | -2.76 | 0.006 | 0.040 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 903.17, BIC = 924.55
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.59, *SE* = 3.700, *z* = 0.161, *p* = 0.872
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.57, *SE* = 3.988, *z* = 0.393, *p* = 0.694
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.79, *SE* = 3.953, *z* = 0.201, *p* = 0.841
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 4.80, *SE* = 4.600, *z* = 1.043, *p* = 0.297
- **SNR**: *β* = 0.05, *SE* = 0.358, *z* = 0.131, *p* = 0.896

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.59 | 3.70 | -0.16 | 0.872 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -1.57 | 3.99 | -0.39 | 0.694 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.79 | 3.95 | -0.20 | 0.841 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -4.80 | 4.60 | -1.04 | 0.297 | 0.971 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.97 | 3.83 | -0.25 | 0.800 | 1.000 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.20 | 3.80 | -0.05 | 0.958 | 1.000 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -4.20 | 4.37 | -0.96 | 0.336 | 0.975 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.77 | 3.79 | 0.20 | 0.839 | 1.000 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -3.23 | 4.15 | -0.78 | 0.437 | 0.982 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -4.00 | 4.17 | -0.96 | 0.337 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.20, *p* = 0.936, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.27 | 14 | = 0.954 | -0.07 [-0.47, 0.40] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.16 | 14 | = 0.954 | 0.05 [-0.50, 0.42] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.06 | 14 | = 0.954 | 0.01 [-0.49, 0.40] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.53 | 14 | = 0.954 | -0.17 [-0.70, 0.37] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.93 | 14 | = 0.954 | 0.11 [-0.50, 0.41] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.29 | 14 | = 0.954 | 0.08 [-0.46, 0.42] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.42 | 14 | = 0.954 | -0.09 [-0.68, 0.39] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.09 | 14 | = 0.954 | -0.03 [-0.46, 0.48] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.82 | 14 | = 0.954 | -0.20 [-0.74, 0.33] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.60 | 14 | = 0.954 | -0.16 [-0.73, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 412.56, BIC = 433.94
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.36, *SE* = 0.371, *z* = 0.960, *p* = 0.337
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.71, *SE* = 0.401, *z* = -1.780, *p* = 0.075
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.75, *SE* = 0.397, *z* = -1.887, *p* = 0.059
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.57, *SE* = 0.464, *z* = -3.392, *p* = 0.001
- **SNR**: *β* = -0.20, *SE* = 0.036, *z* = -5.618, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.36 | 0.37 | -0.96 | 0.337 | 0.561 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.71 | 0.40 | 1.78 | 0.075 | 0.222 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.75 | 0.40 | 1.89 | 0.059 | 0.222 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 1.57 | 0.46 | 3.39 | < .001 | 0.006 | ** |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 1.07 | 0.38 | 2.78 | 0.005 | 0.037 | * |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 1.10 | 0.38 | 2.90 | 0.004 | 0.029 | * |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 1.93 | 0.44 | 4.39 | < .001 | < .001 | *** |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.03 | 0.38 | 0.09 | 0.928 | 0.928 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.86 | 0.42 | 2.06 | 0.039 | 0.213 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.83 | 0.42 | 1.97 | 0.049 | 0.222 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.317, η²_G = 0.029
- Greenhouse-Geisser corrected: *p* = 0.318 (ε = 0.665)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -1.76 | 14 | = 0.498 | -0.23 [-1.02, -0.09] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.11 | 14 | = 0.917 | -0.02 [-0.53, 0.38] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.81 | 14 | = 0.538 | 0.17 [-0.48, 0.41] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 1.02 | 14 | = 0.538 | 0.27 [-0.29, 0.79] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.89 | 14 | = 0.538 | 0.22 [-0.15, 0.78] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 1.39 | 14 | = 0.538 | 0.37 [-0.18, 0.72] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.99 | 14 | = 0.498 | 0.48 [-0.09, 1.03] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 1.01 | 14 | = 0.538 | 0.20 [-0.31, 0.63] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 1.09 | 14 | = 0.538 | 0.30 [-0.34, 0.73] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.25 | 14 | = 0.900 | 0.07 [-0.43, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 417.56, BIC = 434.70
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.91, *SE* = 1.806, *z* = -0.504, *p* = 0.614
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.83, *SE* = 1.794, *z* = 0.461, *p* = 0.645
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.09, *SE* = 1.608, *z* = -0.676, *p* = 0.499
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.69, *SE* = 2.003, *z* = 0.844, *p* = 0.399
- **SNR**: *β* = 0.17, *SE* = 0.389, *z* = 0.440, *p* = 0.660

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.91 | 1.81 | 0.50 | 0.614 | 0.978 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.83 | 1.79 | -0.46 | 0.645 | 0.978 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 1.09 | 1.61 | 0.68 | 0.499 | 0.971 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -1.69 | 2.00 | -0.84 | 0.399 | 0.971 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -1.74 | 2.05 | -0.85 | 0.396 | 0.971 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.18 | 1.89 | 0.09 | 0.925 | 0.978 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -2.60 | 2.21 | -1.18 | 0.239 | 0.915 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 1.91 | 1.75 | 1.09 | 0.274 | 0.923 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -0.86 | 2.08 | -0.42 | 0.678 | 0.978 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -2.78 | 1.91 | -1.45 | 0.146 | 0.793 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.92, *p* = 0.483, η²_G = 0.085
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.68 | 3 | = 0.684 | 0.34 [-0.56, 1.00] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.00 | 3 | = 0.652 | -0.13 [-1.06, 0.50] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.00 | 3 | = 1.000 | 0.00 [-0.38, 0.85] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.57 | 3 | = 0.652 | -0.50 [-1.37, 0.55] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.74 | 3 | = 0.684 | -0.45 [-1.72, 0.87] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.00 | 3 | = 0.652 | -0.37 [-0.92, 0.75] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -1.26 | 3 | = 0.652 | -0.80 [-1.74, 0.54] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.40 | 3 | = 0.797 | 0.14 [-0.45, 1.01] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.00 | 3 | = 0.652 | -0.32 [-1.35, 0.79] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -1.57 | 3 | = 0.652 | -0.59 [-1.37, 0.55] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 282.40, BIC = 299.55
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.17, *SE* = 0.767, *z* = -0.217, *p* = 0.828
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.37, *SE* = 0.767, *z* = 0.480, *p* = 0.631
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.12, *SE* = 0.693, *z* = 1.610, *p* = 0.107
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 2.63, *SE* = 0.807, *z* = 3.254, *p* = 0.001
- **SNR**: *β* = 0.47, *SE* = 0.148, *z* = 3.171, *p* = 0.002

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.17 | 0.77 | 0.22 | 0.828 | 0.889 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.37 | 0.77 | -0.48 | 0.631 | 0.889 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -1.12 | 0.69 | -1.61 | 0.107 | 0.459 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -2.63 | 0.81 | -3.25 | 0.001 | 0.011 | * |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.54 | 0.83 | -0.64 | 0.519 | 0.889 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -1.28 | 0.77 | -1.66 | 0.097 | 0.459 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -2.79 | 0.88 | -3.17 | 0.002 | 0.014 | * |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.75 | 0.75 | -1.00 | 0.317 | 0.783 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -2.26 | 0.85 | -2.66 | 0.008 | 0.062 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -1.51 | 0.76 | -1.98 | 0.048 | 0.292 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.494, η²_G = 0.209
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.44 | 3 | = 0.859 | -0.23 [-0.74, 0.79] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.57 | 3 | = 0.859 | 0.36 [-0.99, 0.56] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.27 | 3 | = 0.890 | -0.16 [-1.11, 0.17] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.04 | 3 | = 0.859 | -0.77 [-1.38, 0.55] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.66 | 3 | = 0.859 | 0.42 [-1.16, 1.32] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.07 | 3 | = 0.947 | 0.03 [-1.02, 0.66] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.84 | 3 | = 0.859 | -0.69 [-1.48, 0.70] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.60 | 3 | = 0.859 | -0.36 [-1.20, 0.30] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.07 | 3 | = 0.859 | -0.83 [-1.50, 0.68] | large | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.97 | 3 | = 0.859 | -0.69 [-1.27, 0.63] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 854.04, BIC = 873.86
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -2.28, *SE* = 7.555, *z* = -0.302, *p* = 0.763
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.46, *SE* = 7.748, *z* = 0.059, *p* = 0.953
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.87, *SE* = 7.853, *z* = 0.238, *p* = 0.812
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 14.45, *SE* = 9.747, *z* = 1.483, *p* = 0.138
- **SNR**: *β* = -0.60, *SE* = 0.733, *z* = -0.816, *p* = 0.415

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 2.28 | 7.56 | 0.30 | 0.763 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.46 | 7.75 | -0.06 | 0.953 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -1.87 | 7.85 | -0.24 | 0.812 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -14.45 | 9.75 | -1.48 | 0.138 | 0.738 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -2.74 | 7.88 | -0.35 | 0.728 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -4.15 | 7.89 | -0.53 | 0.599 | 0.996 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -16.73 | 9.75 | -1.72 | 0.086 | 0.593 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -1.41 | 8.06 | -0.17 | 0.861 | 0.999 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -13.99 | 9.90 | -1.41 | 0.157 | 0.746 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -12.58 | 9.21 | -1.37 | 0.172 | 0.746 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.82, *p* = 0.039, η²_G = 0.102
- Greenhouse-Geisser corrected: *p* = 0.077 (ε = 0.569)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.75 | 9 | = 0.525 | 0.15 [-0.36, 0.61] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.00 | 9 | = 0.432 | -0.30 [-0.64, 0.39] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.36 | 9 | = 0.296 | -0.46 [-0.62, 0.38] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -2.24 | 9 | = 0.233 | -0.79 [-1.23, 0.14] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -1.84 | 9 | = 0.233 | -0.43 [-0.66, 0.41] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.71 | 9 | = 0.233 | -0.59 [-0.70, 0.30] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -2.65 | 9 | = 0.233 | -0.91 [-1.35, 0.05] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.43 | 9 | = 0.679 | -0.16 [-0.68, 0.40] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.62 | 9 | = 0.233 | -0.45 [-1.34, 0.13] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -1.65 | 9 | = 0.233 | -0.29 [-1.32, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 420.30, BIC = 440.11
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.38, *SE* = 0.644, *z* = 0.582, *p* = 0.560
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.81, *SE* = 0.660, *z* = 1.235, *p* = 0.217
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.41, *SE* = 0.671, *z* = 2.106, *p* = 0.035
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.96, *SE* = 0.856, *z* = 2.287, *p* = 0.022
- **SNR**: *β* = 0.23, *SE* = 0.064, *z* = 3.618, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.38 | 0.64 | -0.58 | 0.560 | 0.873 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.82 | 0.66 | -1.24 | 0.217 | 0.707 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -1.41 | 0.67 | -2.11 | 0.035 | 0.275 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -1.96 | 0.86 | -2.29 | 0.022 | 0.201 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.44 | 0.67 | -0.66 | 0.512 | 0.873 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -1.04 | 0.67 | -1.54 | 0.123 | 0.600 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -1.58 | 0.85 | -1.86 | 0.063 | 0.408 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.60 | 0.69 | -0.87 | 0.384 | 0.856 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -1.14 | 0.86 | -1.33 | 0.185 | 0.707 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -0.54 | 0.80 | -0.68 | 0.497 | 0.873 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.792, η²_G = 0.022
- Greenhouse-Geisser corrected: *p* = 0.602 (ε = 0.364)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -1.60 | 9 | = 0.911 | -0.28 [-0.68, 0.29] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.10 | 9 | = 0.911 | -0.29 [-0.94, 0.13] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.39 | 9 | = 0.911 | -0.28 [-1.01, 0.04] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.26 | 9 | = 0.980 | 0.10 [-0.69, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.07 | 9 | = 0.980 | 0.02 [-0.72, 0.35] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.05 | 9 | = 0.980 | 0.01 [-0.70, 0.30] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 0.63 | 9 | = 0.911 | 0.28 [-0.60, 0.68] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.03 | 9 | = 0.980 | -0.01 [-0.38, 0.69] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.63 | 9 | = 0.911 | 0.28 [-0.61, 0.73] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.75 | 9 | = 0.911 | 0.28 [-0.45, 0.91] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Significant main effect of condition (*p* = 0.039) (no significant pairwise comparisons)

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
