# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:48:59

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
| Ratio 0.5 (1:2) | 7 | 102.86 ms | 9.44 | 3.57 | [92.00, 112.00] |
| Ratio 0.67 (2:3) | 9 | 105.33 ms | 7.75 | 2.58 | [92.00, 112.00] |
| Ratio 0.75 (3:4) | 12 | 100.33 ms | 9.41 | 2.72 | [92.00, 112.00] |
| Ratio 0.8 (4:5) | 8 | 98.00 ms | 8.82 | 3.12 | [92.00, 112.00] |
| Ratio 0.83 (5:6) | 4 | 99.00 ms | 8.87 | 4.43 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 7 | 0.99 µV | 0.73 | 0.27 | [0.18, 2.14] |
| Ratio 0.67 (2:3) | 9 | 1.40 µV | 0.80 | 0.27 | [0.37, 2.79] |
| Ratio 0.75 (3:4) | 12 | 1.55 µV | 1.32 | 0.38 | [0.42, 5.25] |
| Ratio 0.8 (4:5) | 8 | 1.98 µV | 1.27 | 0.45 | [0.60, 4.16] |
| Ratio 0.83 (5:6) | 4 | 4.36 µV | 1.68 | 0.84 | [2.15, 6.18] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 23 | 171.65 ms | 14.86 | 3.10 | [140.00, 204.00] |
| Ratio 0.67 (2:3) | 23 | 171.83 ms | 18.59 | 3.88 | [144.00, 200.00] |
| Ratio 0.75 (3:4) | 22 | 172.73 ms | 19.43 | 4.14 | [140.00, 204.00] |
| Ratio 0.8 (4:5) | 22 | 170.91 ms | 18.85 | 4.02 | [140.00, 204.00] |
| Ratio 0.83 (5:6) | 17 | 176.24 ms | 21.79 | 5.29 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 23 | -5.25 µV | 2.02 | 0.42 | [-9.37, -2.16] |
| Ratio 0.67 (2:3) | 23 | -5.33 µV | 2.35 | 0.49 | [-10.09, -2.11] |
| Ratio 0.75 (3:4) | 22 | -5.98 µV | 1.84 | 0.39 | [-10.31, -3.43] |
| Ratio 0.8 (4:5) | 22 | -6.06 µV | 2.68 | 0.57 | [-11.24, -2.10] |
| Ratio 0.83 (5:6) | 17 | -6.46 µV | 2.41 | 0.58 | [-11.29, -2.31] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 112.53 ms | 5.42 | 1.40 | [100.00, 116.00] |
| Ratio 0.67 (2:3) | 11 | 109.45 ms | 7.43 | 2.24 | [96.00, 116.00] |
| Ratio 0.75 (3:4) | 11 | 108.00 ms | 8.00 | 2.41 | [96.00, 116.00] |
| Ratio 0.8 (4:5) | 16 | 106.75 ms | 6.96 | 1.74 | [96.00, 116.00] |
| Ratio 0.83 (5:6) | 11 | 109.09 ms | 7.40 | 2.23 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 2.01 µV | 1.30 | 0.34 | [0.47, 5.03] |
| Ratio 0.67 (2:3) | 11 | 2.45 µV | 1.61 | 0.48 | [0.64, 5.72] |
| Ratio 0.75 (3:4) | 11 | 2.66 µV | 1.43 | 0.43 | [1.16, 5.67] |
| Ratio 0.8 (4:5) | 16 | 2.97 µV | 1.79 | 0.45 | [0.46, 6.17] |
| Ratio 0.83 (5:6) | 11 | 4.04 µV | 4.38 | 1.32 | [0.74, 16.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 488.20 ms | 34.79 | 7.78 | [444.00, 540.00] |
| Ratio 0.67 (2:3) | 19 | 492.63 ms | 35.43 | 8.13 | [444.00, 540.00] |
| Ratio 0.75 (3:4) | 18 | 492.89 ms | 34.31 | 8.09 | [444.00, 540.00] |
| Ratio 0.8 (4:5) | 19 | 495.79 ms | 34.06 | 7.81 | [444.00, 540.00] |
| Ratio 0.83 (5:6) | 12 | 510.33 ms | 30.48 | 8.80 | [448.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 4.36 µV | 2.63 | 0.59 | [0.83, 9.90] |
| Ratio 0.67 (2:3) | 19 | 5.16 µV | 3.35 | 0.77 | [0.59, 14.05] |
| Ratio 0.75 (3:4) | 18 | 5.62 µV | 2.78 | 0.66 | [2.00, 11.73] |
| Ratio 0.8 (4:5) | 19 | 5.56 µV | 2.87 | 0.66 | [1.81, 10.40] |
| Ratio 0.83 (5:6) | 12 | 6.59 µV | 4.52 | 1.30 | [1.33, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 286.29, BIC = 299.81
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -1.69, *SE* = 2.823, *z* = -0.597, *p* = 0.551
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -2.69, *SE* = 2.657, *z* = -1.011, *p* = 0.312
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -4.57, *SE* = 2.823, *z* = -1.618, *p* = 0.106
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -10.15, *SE* = 4.116, *z* = -2.466, *p* = 0.014
- **SNR**: *β* = 2.78, *SE* = 1.097, *z* = 2.536, *p* = 0.011

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 1.68 | 2.82 | 0.60 | 0.551 | 0.849 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 2.69 | 2.66 | 1.01 | 0.312 | 0.846 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 4.57 | 2.82 | 1.62 | 0.106 | 0.543 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 10.15 | 4.12 | 2.47 | 0.014 | 0.129 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 1.00 | 2.67 | 0.37 | 0.708 | 0.849 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 2.88 | 3.01 | 0.96 | 0.339 | 0.846 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 8.47 | 3.78 | 2.24 | 0.025 | 0.204 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 1.88 | 2.59 | 0.73 | 0.468 | 0.849 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 7.46 | 3.81 | 1.96 | 0.050 | 0.338 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 5.58 | 4.34 | 1.29 | 0.198 | 0.734 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 112.14, BIC = 125.65
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.02, *SE* = 0.402, *z* = -0.051, *p* = 0.960
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.70, *SE* = 0.374, *z* = 1.864, *p* = 0.062
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.94, *SE* = 0.404, *z* = 2.328, *p* = 0.020
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 2.34, *SE* = 0.534, *z* = 4.388, *p* < .001
- **SNR**: *β* = 0.72, *SE* = 0.132, *z* = 5.475, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.02 | 0.40 | 0.05 | 0.960 | 0.960 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.70 | 0.37 | -1.86 | 0.062 | 0.176 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.94 | 0.40 | -2.33 | 0.020 | 0.096 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -2.34 | 0.53 | -4.39 | < .001 | < .001 | *** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.72 | 0.36 | -1.99 | 0.047 | 0.174 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.96 | 0.39 | -2.47 | 0.014 | 0.079 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -2.36 | 0.50 | -4.72 | < .001 | < .001 | *** |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.24 | 0.36 | -0.68 | 0.496 | 0.746 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -1.65 | 0.50 | -3.28 | 0.001 | 0.008 | ** |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -1.40 | 0.53 | -2.64 | 0.008 | 0.056 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 900.65, BIC = 922.04
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.10, *SE* = 3.723, *z* = 0.027, *p* = 0.979
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.67, *SE* = 3.978, *z* = 0.168, *p* = 0.867
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.03, *SE* = 3.956, *z* = 0.006, *p* = 0.995
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 3.62, *SE* = 4.504, *z* = 0.805, *p* = 0.421
- **SNR**: *β* = -0.07, *SE* = 0.299, *z* = -0.231, *p* = 0.817

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.10 | 3.72 | -0.03 | 0.979 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.67 | 3.98 | -0.17 | 0.867 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.03 | 3.96 | -0.01 | 0.995 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -3.62 | 4.50 | -0.80 | 0.421 | 0.991 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.57 | 3.73 | -0.15 | 0.879 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.07 | 3.72 | 0.02 | 0.984 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -3.52 | 4.20 | -0.84 | 0.401 | 0.991 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.64 | 3.73 | 0.17 | 0.863 | 1.000 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -2.96 | 4.07 | -0.73 | 0.467 | 0.991 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -3.60 | 4.07 | -0.88 | 0.376 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.926, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.850 (ε = 0.630)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.34 | 14 | = 1.000 | -0.09 [-0.47, 0.42] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.11 | 14 | = 1.000 | 0.03 [-0.48, 0.43] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.00 | 14 | = 1.000 | 0.00 [-0.50, 0.39] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.57 | 14 | = 1.000 | -0.18 [-0.69, 0.35] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.93 | 14 | = 1.000 | 0.11 [-0.50, 0.41] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.29 | 14 | = 1.000 | 0.08 [-0.46, 0.42] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.42 | 14 | = 1.000 | -0.09 [-0.68, 0.39] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.09 | 14 | = 1.000 | -0.03 [-0.46, 0.48] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.82 | 14 | = 1.000 | -0.20 [-0.74, 0.33] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.60 | 14 | = 1.000 | -0.16 [-0.73, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 416.57, BIC = 437.95
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.55, *SE* = 0.387, *z* = -1.425, *p* = 0.154
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.49, *SE* = 0.415, *z* = -3.593, *p* < .001
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.55, *SE* = 0.411, *z* = -3.768, *p* < .001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -2.24, *SE* = 0.471, *z* = -4.765, *p* < .001
- **SNR**: *β* = -0.15, *SE* = 0.032, *z* = -4.792, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.55 | 0.39 | 1.42 | 0.154 | 0.285 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.49 | 0.41 | 3.59 | < .001 | 0.002 | ** |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.55 | 0.41 | 3.77 | < .001 | 0.001 | ** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 2.24 | 0.47 | 4.77 | < .001 | < .001 | *** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.94 | 0.39 | 2.42 | 0.016 | 0.076 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 1.00 | 0.39 | 2.59 | 0.010 | 0.057 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 1.69 | 0.44 | 3.86 | < .001 | 0.001 | ** |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.06 | 0.39 | 0.16 | 0.876 | 0.876 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.75 | 0.42 | 1.78 | 0.075 | 0.269 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.69 | 0.42 | 1.64 | 0.102 | 0.276 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.61, *p* = 0.045, η²_G = 0.061
- Greenhouse-Geisser corrected: *p* = 0.078 (ε = 0.611)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 2.98 | 14 | = 0.067 | 0.21 [-0.31, 0.58] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 2.01 | 14 | = 0.133 | 0.44 [-0.01, 0.95] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 2.23 | 14 | = 0.133 | 0.55 [-0.10, 0.82] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 2.83 | 14 | = 0.067 | 0.68 [0.11, 1.25] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.89 | 14 | = 0.433 | 0.22 [-0.15, 0.78] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 1.39 | 14 | = 0.310 | 0.37 [-0.18, 0.72] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.99 | 14 | = 0.133 | 0.48 [-0.09, 1.03] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 1.01 | 14 | = 0.410 | 0.20 [-0.31, 0.63] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 1.09 | 14 | = 0.410 | 0.30 [-0.34, 0.73] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.25 | 14 | = 0.810 | 0.07 [-0.43, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 416.05, BIC = 433.32
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -4.19, *SE* = 1.638, *z* = -2.559, *p* = 0.010
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -3.06, *SE* = 1.720, *z* = -1.776, *p* = 0.076
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -5.17, *SE* = 1.569, *z* = -3.298, *p* = 0.001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -2.51, *SE* = 1.919, *z* = -1.307, *p* = 0.191
- **SNR**: *β* = -0.17, *SE* = 0.315, *z* = -0.522, *p* = 0.602

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 4.19 | 1.64 | 2.56 | 0.010 | 0.091 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 3.06 | 1.72 | 1.78 | 0.076 | 0.467 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 5.17 | 1.57 | 3.30 | < .001 | 0.010 | ** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 2.51 | 1.92 | 1.31 | 0.191 | 0.720 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -1.14 | 1.91 | -0.60 | 0.552 | 0.910 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.98 | 1.74 | 0.56 | 0.573 | 0.910 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -1.68 | 2.02 | -0.83 | 0.405 | 0.875 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 2.12 | 1.64 | 1.29 | 0.197 | 0.720 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -0.55 | 1.92 | -0.29 | 0.776 | 0.910 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -2.67 | 1.78 | -1.50 | 0.134 | 0.634 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.445, η²_G = 0.095
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 1.00 | 3 | = 0.559 | 0.50 [-0.16, 1.40] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.00 | 3 | = 1.000 | 0.00 [-0.40, 1.19] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 1.00 | 3 | = 0.559 | 0.17 [0.18, 1.62] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -1.73 | 3 | = 0.559 | -0.41 [-0.63, 1.06] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.74 | 3 | = 0.642 | -0.45 [-1.72, 0.87] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.00 | 3 | = 0.559 | -0.37 [-0.92, 0.75] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -1.26 | 3 | = 0.559 | -0.80 [-1.74, 0.54] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.40 | 3 | = 0.797 | 0.14 [-0.45, 1.01] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.00 | 3 | = 0.559 | -0.32 [-1.35, 0.79] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -1.57 | 3 | = 0.559 | -0.59 [-1.37, 0.55] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 286.77, BIC = 304.05
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.41, *SE* = 0.757, *z* = 0.547, *p* = 0.585
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.90, *SE* = 0.776, *z* = 1.154, *p* = 0.249
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 1.57, *SE* = 0.711, *z* = 2.216, *p* = 0.027
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 3.00, *SE* = 0.821, *z* = 3.646, *p* < .001
- **SNR**: *β* = 0.39, *SE* = 0.123, *z* = 3.171, *p* = 0.002

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.41 | 0.76 | -0.55 | 0.585 | 0.810 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.89 | 0.78 | -1.15 | 0.249 | 0.681 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -1.58 | 0.71 | -2.22 | 0.027 | 0.173 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -2.99 | 0.82 | -3.65 | < .001 | 0.003 | ** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.48 | 0.83 | -0.58 | 0.564 | 0.810 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -1.16 | 0.77 | -1.50 | 0.133 | 0.510 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -2.58 | 0.87 | -2.97 | 0.003 | 0.026 | * |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.68 | 0.75 | -0.90 | 0.367 | 0.747 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -2.10 | 0.85 | -2.48 | 0.013 | 0.101 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -1.42 | 0.77 | -1.85 | 0.064 | 0.326 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.489, η²_G = 0.217
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.91 | 3 | = 0.778 | -0.47 [-0.79, 0.64] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -0.05 | 3 | = 0.961 | -0.02 [-1.37, 0.28] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.55 | 3 | = 0.778 | -0.40 [-1.17, 0.12] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -1.04 | 3 | = 0.778 | -0.84 [-1.32, 0.43] | large | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.66 | 3 | = 0.778 | 0.42 [-1.16, 1.32] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.07 | 3 | = 0.961 | 0.03 [-1.02, 0.66] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.84 | 3 | = 0.778 | -0.69 [-1.48, 0.70] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.60 | 3 | = 0.778 | -0.36 [-1.20, 0.30] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.07 | 3 | = 0.778 | -0.83 [-1.50, 0.68] | large | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.97 | 3 | = 0.778 | -0.69 [-1.27, 0.63] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 856.30, BIC = 876.12
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 4.87, *SE* = 7.568, *z* = 0.644, *p* = 0.520
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 6.89, *SE* = 7.759, *z* = 0.888, *p* = 0.374
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 8.11, *SE* = 7.990, *z* = 1.015, *p* = 0.310
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 18.65, *SE* = 9.986, *z* = 1.867, *p* = 0.062
- **SNR**: *β* = -1.14, *SE* = 0.722, *z* = -1.580, *p* = 0.114

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -4.87 | 7.57 | -0.64 | 0.520 | 0.947 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -6.89 | 7.76 | -0.89 | 0.374 | 0.904 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -8.11 | 7.99 | -1.01 | 0.310 | 0.892 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -18.65 | 9.99 | -1.87 | 0.062 | 0.472 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -2.02 | 7.86 | -0.26 | 0.797 | 0.967 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -3.24 | 7.86 | -0.41 | 0.681 | 0.967 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -13.78 | 9.73 | -1.42 | 0.157 | 0.785 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -1.21 | 8.04 | -0.15 | 0.880 | 0.967 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -11.75 | 9.87 | -1.19 | 0.234 | 0.881 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -10.54 | 9.21 | -1.14 | 0.252 | 0.881 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.20, *p* = 0.002, η²_G = 0.172
- Greenhouse-Geisser corrected: *p* = 0.012 (ε = 0.577)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -1.12 | 9 | = 0.324 | -0.29 [-0.71, 0.27] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -2.30 | 9 | = 0.118 | -0.78 [-0.82, 0.23] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -3.56 | 9 | = 0.031 | -0.96 [-1.06, 0.00] | large | * |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -4.14 | 9 | = 0.025 | -1.37 [-1.58, -0.10] | large | * |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -1.84 | 9 | = 0.175 | -0.43 [-0.66, 0.41] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.71 | 9 | = 0.175 | -0.59 [-0.70, 0.30] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -2.65 | 9 | = 0.088 | -0.91 [-1.35, 0.05] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.43 | 9 | = 0.679 | -0.16 [-0.68, 0.40] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.62 | 9 | = 0.175 | -0.45 [-1.34, 0.13] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -1.65 | 9 | = 0.175 | -0.29 [-1.32, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 420.10, BIC = 439.92
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.89, *SE* = 0.649, *z* = 1.365, *p* = 0.172
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 1.34, *SE* = 0.665, *z* = 2.011, *p* = 0.044
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 1.89, *SE* = 0.686, *z* = 2.752, *p* = 0.006
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 2.42, *SE* = 0.880, *z* = 2.752, *p* = 0.006
- **SNR**: *β* = 0.22, *SE* = 0.063, *z* = 3.481, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.89 | 0.65 | -1.36 | 0.172 | 0.612 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -1.34 | 0.66 | -2.01 | 0.044 | 0.304 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -1.89 | 0.69 | -2.75 | 0.006 | 0.058 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -2.42 | 0.88 | -2.75 | 0.006 | 0.058 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.45 | 0.67 | -0.67 | 0.503 | 0.807 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -1.00 | 0.67 | -1.49 | 0.137 | 0.586 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -1.54 | 0.85 | -1.80 | 0.072 | 0.406 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.55 | 0.69 | -0.80 | 0.422 | 0.807 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -1.09 | 0.86 | -1.26 | 0.208 | 0.612 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -0.53 | 0.80 | -0.66 | 0.506 | 0.807 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.701, η²_G = 0.029
- Greenhouse-Geisser corrected: *p* = 0.533 (ε = 0.357)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -2.34 | 9 | = 0.313 | -0.41 [-1.00, 0.02] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -2.04 | 9 | = 0.313 | -0.43 [-1.34, -0.17] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -1.87 | 9 | = 0.313 | -0.43 [-1.24, -0.13] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.04 | 9 | = 0.980 | 0.01 [-0.77, 0.51] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.07 | 9 | = 0.980 | 0.02 [-0.72, 0.35] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.05 | 9 | = 0.980 | 0.01 [-0.70, 0.30] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.63 | 9 | = 0.911 | 0.28 [-0.60, 0.68] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.03 | 9 | = 0.980 | -0.01 [-0.38, 0.69] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.63 | 9 | = 0.911 | 0.28 [-0.61, 0.73] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.75 | 9 | = 0.911 | 0.28 [-0.45, 0.91] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.045) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Ratio 0.5 (1:2) showed smaller latency than Ratio 0.8 (4:5) (*d* = -0.96)
  - Ratio 0.5 (1:2) showed smaller latency than Ratio 0.83 (5:6) (*d* = -1.37)

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
