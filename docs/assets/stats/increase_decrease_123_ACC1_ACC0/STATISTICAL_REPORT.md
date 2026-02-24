# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:25:16

---

## 1. Analysis Overview

**Total Measurements:** 1164
**Number of Subjects:** 24
**Number of Conditions:** 13

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
| Cardinality (no change) | 24 | 105.83 ms | 7.73 | 1.58 | [92.00, 112.00] |
| Decrease by 1 (Correct) | 24 | 104.17 ms | 7.95 | 1.62 | [92.00, 112.00] |
| Decrease by 1 (Incorrect) | 24 | 102.00 ms | 7.82 | 1.60 | [92.00, 112.00] |
| Decrease by 2 (Correct) | 24 | 105.50 ms | 7.72 | 1.58 | [92.00, 112.00] |
| Decrease by 2 (Incorrect) | 20 | 105.00 ms | 7.77 | 1.74 | [92.00, 112.00] |
| Decrease by 3 (Correct) | 24 | 103.83 ms | 8.13 | 1.66 | [92.00, 112.00] |
| Decrease by 3 (Incorrect) | 14 | 100.00 ms | 8.88 | 2.37 | [92.00, 112.00] |
| Increase by 1 (Correct) | 24 | 101.17 ms | 8.30 | 1.69 | [92.00, 112.00] |
| Increase by 1 (Incorrect) | 24 | 101.17 ms | 8.63 | 1.76 | [92.00, 112.00] |
| Increase by 2 (Correct) | 24 | 101.33 ms | 8.14 | 1.66 | [92.00, 112.00] |
| Increase by 2 (Incorrect) | 20 | 101.60 ms | 8.15 | 1.82 | [92.00, 112.00] |
| Increase by 3 (Correct) | 24 | 101.67 ms | 8.33 | 1.70 | [92.00, 112.00] |
| Increase by 3 (Incorrect) | 21 | 101.71 ms | 8.25 | 1.80 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -1.22 µV | 1.38 | 0.28 | [-4.83, 0.55] |
| Decrease by 1 (Correct) | 24 | -0.93 µV | 1.42 | 0.29 | [-4.56, 1.56] |
| Decrease by 1 (Incorrect) | 24 | -0.96 µV | 2.55 | 0.52 | [-8.16, 3.16] |
| Decrease by 2 (Correct) | 24 | -1.40 µV | 1.23 | 0.25 | [-4.30, 2.02] |
| Decrease by 2 (Incorrect) | 20 | -1.80 µV | 3.22 | 0.72 | [-8.85, 2.66] |
| Decrease by 3 (Correct) | 24 | -1.72 µV | 1.91 | 0.39 | [-6.39, 1.69] |
| Decrease by 3 (Incorrect) | 14 | -2.75 µV | 5.95 | 1.59 | [-15.27, 7.50] |
| Increase by 1 (Correct) | 24 | -1.11 µV | 1.29 | 0.26 | [-3.74, 1.09] |
| Increase by 1 (Incorrect) | 24 | -1.37 µV | 1.53 | 0.31 | [-4.54, 0.72] |
| Increase by 2 (Correct) | 24 | -0.99 µV | 1.23 | 0.25 | [-4.17, 0.52] |
| Increase by 2 (Incorrect) | 20 | -0.76 µV | 2.28 | 0.51 | [-4.91, 3.23] |
| Increase by 3 (Correct) | 24 | -1.11 µV | 1.23 | 0.25 | [-3.35, 1.12] |
| Increase by 3 (Incorrect) | 21 | -1.35 µV | 4.17 | 0.91 | [-8.80, 9.52] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 175.67 ms | 16.80 | 3.43 | [144.00, 204.00] |
| Decrease by 1 (Correct) | 24 | 178.67 ms | 14.09 | 2.88 | [152.00, 204.00] |
| Decrease by 1 (Incorrect) | 24 | 173.33 ms | 19.23 | 3.92 | [144.00, 204.00] |
| Decrease by 2 (Correct) | 24 | 177.17 ms | 14.18 | 2.89 | [144.00, 204.00] |
| Decrease by 2 (Incorrect) | 20 | 175.40 ms | 20.03 | 4.48 | [144.00, 204.00] |
| Decrease by 3 (Correct) | 24 | 176.83 ms | 14.68 | 3.00 | [152.00, 204.00] |
| Decrease by 3 (Incorrect) | 14 | 176.00 ms | 19.15 | 5.12 | [144.00, 204.00] |
| Increase by 1 (Correct) | 24 | 170.83 ms | 19.65 | 4.01 | [144.00, 204.00] |
| Increase by 1 (Incorrect) | 24 | 177.50 ms | 16.29 | 3.33 | [144.00, 204.00] |
| Increase by 2 (Correct) | 24 | 168.83 ms | 18.42 | 3.76 | [144.00, 200.00] |
| Increase by 2 (Incorrect) | 20 | 171.60 ms | 17.26 | 3.86 | [144.00, 196.00] |
| Increase by 3 (Correct) | 24 | 171.50 ms | 19.21 | 3.92 | [144.00, 204.00] |
| Increase by 3 (Incorrect) | 21 | 168.00 ms | 19.51 | 4.26 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -4.62 µV | 2.14 | 0.44 | [-9.57, -0.60] |
| Decrease by 1 (Correct) | 24 | -4.86 µV | 2.07 | 0.42 | [-9.90, -1.23] |
| Decrease by 1 (Incorrect) | 24 | -5.15 µV | 2.57 | 0.52 | [-13.51, -1.23] |
| Decrease by 2 (Correct) | 24 | -5.12 µV | 2.11 | 0.43 | [-9.59, -1.53] |
| Decrease by 2 (Incorrect) | 20 | -4.84 µV | 2.93 | 0.66 | [-10.77, 0.08] |
| Decrease by 3 (Correct) | 24 | -5.22 µV | 1.97 | 0.40 | [-8.60, -1.48] |
| Decrease by 3 (Incorrect) | 14 | -6.05 µV | 5.01 | 1.34 | [-16.59, -0.45] |
| Increase by 1 (Correct) | 24 | -5.07 µV | 2.13 | 0.44 | [-9.46, -0.56] |
| Increase by 1 (Incorrect) | 24 | -5.49 µV | 2.67 | 0.55 | [-9.82, -0.34] |
| Increase by 2 (Correct) | 24 | -5.47 µV | 2.43 | 0.50 | [-11.28, -1.22] |
| Increase by 2 (Incorrect) | 20 | -5.58 µV | 2.68 | 0.60 | [-11.01, -0.68] |
| Increase by 3 (Correct) | 24 | -6.16 µV | 2.55 | 0.52 | [-12.86, -2.06] |
| Increase by 3 (Incorrect) | 21 | -6.47 µV | 3.26 | 0.71 | [-13.50, -1.48] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 106.00 ms | 10.55 | 2.15 | [92.00, 116.00] |
| Decrease by 1 (Correct) | 24 | 108.50 ms | 9.68 | 1.98 | [92.00, 116.00] |
| Decrease by 1 (Incorrect) | 24 | 103.00 ms | 9.31 | 1.90 | [92.00, 116.00] |
| Decrease by 2 (Correct) | 24 | 109.50 ms | 8.32 | 1.70 | [92.00, 116.00] |
| Decrease by 2 (Incorrect) | 20 | 109.20 ms | 8.72 | 1.95 | [92.00, 116.00] |
| Decrease by 3 (Correct) | 24 | 107.33 ms | 9.03 | 1.84 | [92.00, 116.00] |
| Decrease by 3 (Incorrect) | 14 | 105.71 ms | 10.01 | 2.68 | [92.00, 116.00] |
| Increase by 1 (Correct) | 24 | 103.67 ms | 9.50 | 1.94 | [92.00, 116.00] |
| Increase by 1 (Incorrect) | 24 | 101.33 ms | 10.33 | 2.11 | [92.00, 116.00] |
| Increase by 2 (Correct) | 24 | 103.00 ms | 9.60 | 1.96 | [92.00, 116.00] |
| Increase by 2 (Incorrect) | 20 | 102.40 ms | 9.48 | 2.12 | [92.00, 116.00] |
| Increase by 3 (Correct) | 24 | 100.50 ms | 9.31 | 1.90 | [92.00, 116.00] |
| Increase by 3 (Incorrect) | 21 | 102.86 ms | 10.05 | 2.19 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.27 µV | 1.86 | 0.38 | [-1.29, 5.73] |
| Decrease by 1 (Correct) | 24 | 1.09 µV | 1.88 | 0.38 | [-1.32, 5.23] |
| Decrease by 1 (Incorrect) | 24 | 1.54 µV | 2.87 | 0.59 | [-3.73, 8.84] |
| Decrease by 2 (Correct) | 24 | 1.53 µV | 1.78 | 0.36 | [-2.32, 5.74] |
| Decrease by 2 (Incorrect) | 20 | 1.91 µV | 2.92 | 0.65 | [-3.15, 7.73] |
| Decrease by 3 (Correct) | 24 | 1.94 µV | 2.07 | 0.42 | [-1.76, 8.15] |
| Decrease by 3 (Incorrect) | 14 | 2.47 µV | 5.47 | 1.46 | [-8.18, 12.94] |
| Increase by 1 (Correct) | 24 | 1.32 µV | 1.67 | 0.34 | [-1.63, 4.44] |
| Increase by 1 (Incorrect) | 24 | 1.18 µV | 1.32 | 0.27 | [-0.65, 4.59] |
| Increase by 2 (Correct) | 24 | 1.10 µV | 1.60 | 0.33 | [-1.42, 4.70] |
| Increase by 2 (Incorrect) | 20 | 1.20 µV | 2.26 | 0.51 | [-3.39, 7.59] |
| Increase by 3 (Correct) | 24 | 1.39 µV | 1.66 | 0.34 | [-1.07, 5.27] |
| Increase by 3 (Incorrect) | 21 | 1.59 µV | 3.59 | 0.78 | [-3.94, 8.76] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 463.50 ms | 24.86 | 5.08 | [420.00, 516.00] |
| Decrease by 1 (Correct) | 24 | 485.67 ms | 31.56 | 6.44 | [420.00, 528.00] |
| Decrease by 1 (Incorrect) | 24 | 482.33 ms | 37.09 | 7.57 | [420.00, 528.00] |
| Decrease by 2 (Correct) | 24 | 469.00 ms | 28.78 | 5.87 | [420.00, 528.00] |
| Decrease by 2 (Incorrect) | 20 | 464.40 ms | 33.44 | 7.48 | [420.00, 528.00] |
| Decrease by 3 (Correct) | 24 | 478.83 ms | 31.35 | 6.40 | [420.00, 528.00] |
| Decrease by 3 (Incorrect) | 14 | 483.71 ms | 41.55 | 11.11 | [420.00, 528.00] |
| Increase by 1 (Correct) | 24 | 484.00 ms | 39.81 | 8.13 | [420.00, 528.00] |
| Increase by 1 (Incorrect) | 24 | 473.17 ms | 36.40 | 7.43 | [420.00, 528.00] |
| Increase by 2 (Correct) | 24 | 484.33 ms | 31.98 | 6.53 | [428.00, 528.00] |
| Increase by 2 (Incorrect) | 20 | 468.20 ms | 28.18 | 6.30 | [420.00, 528.00] |
| Increase by 3 (Correct) | 24 | 477.00 ms | 34.03 | 6.95 | [420.00, 528.00] |
| Increase by 3 (Incorrect) | 21 | 470.67 ms | 34.35 | 7.50 | [420.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.14 µV | 2.72 | 0.56 | [-4.85, 5.95] |
| Decrease by 1 (Correct) | 24 | 4.11 µV | 3.07 | 0.63 | [-2.27, 9.87] |
| Decrease by 1 (Incorrect) | 24 | 1.86 µV | 3.43 | 0.70 | [-5.71, 10.56] |
| Decrease by 2 (Correct) | 24 | 3.79 µV | 2.93 | 0.60 | [-1.71, 8.68] |
| Decrease by 2 (Incorrect) | 20 | 4.47 µV | 6.23 | 1.39 | [-7.70, 20.39] |
| Decrease by 3 (Correct) | 24 | 4.34 µV | 3.52 | 0.72 | [-1.21, 12.38] |
| Decrease by 3 (Incorrect) | 14 | 2.05 µV | 4.54 | 1.21 | [-9.67, 10.70] |
| Increase by 1 (Correct) | 24 | 2.99 µV | 3.55 | 0.73 | [-3.53, 10.19] |
| Increase by 1 (Incorrect) | 24 | 1.28 µV | 3.03 | 0.62 | [-2.88, 9.88] |
| Increase by 2 (Correct) | 24 | 3.99 µV | 3.48 | 0.71 | [-2.36, 10.55] |
| Increase by 2 (Incorrect) | 20 | 3.88 µV | 3.83 | 0.86 | [-2.53, 10.89] |
| Increase by 3 (Correct) | 24 | 3.93 µV | 2.75 | 0.56 | [0.21, 10.15] |
| Increase by 3 (Incorrect) | 21 | 3.95 µV | 3.59 | 0.78 | [-2.26, 12.49] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 2012.40, BIC = 2071.17
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = -1.50, *SE* = 1.962, *z* = -0.763, *p* = 0.445
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -3.78, *SE* = 1.958, *z* = -1.930, *p* = 0.054
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -0.32, *SE* = 1.957, *z* = -0.164, *p* = 0.869
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -0.90, *SE* = 2.075, *z* = -0.435, *p* = 0.664
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = -2.15, *SE* = 1.961, *z* = -1.098, *p* = 0.272
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = -5.65, *SE* = 2.301, *z* = -2.455, *p* = 0.014
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -4.58, *SE* = 1.959, *z* = -2.340, *p* = 0.019
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -4.40, *SE* = 1.969, *z* = -2.236, *p* = 0.025
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -4.32, *SE* = 1.963, *z* = -2.198, *p* = 0.028
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -4.39, *SE* = 2.061, *z* = -2.132, *p* = 0.033
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -4.03, *SE* = 1.960, *z* = -2.056, *p* = 0.040
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -3.97, *SE* = 2.038, *z* = -1.948, *p* = 0.051
- **SNR**: *β* = 0.34, *SE* = 0.275, *z* = 1.248, *p* = 0.212

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | 1.50 | 1.96 | 0.76 | 0.445 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 3.78 | 1.96 | 1.93 | 0.054 | 0.972 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 0.32 | 1.96 | 0.16 | 0.869 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 0.90 | 2.07 | 0.43 | 0.664 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | 2.15 | 1.96 | 1.10 | 0.272 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | 5.65 | 2.30 | 2.45 | 0.014 | 0.670 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | 4.58 | 1.96 | 2.34 | 0.019 | 0.777 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 4.40 | 1.97 | 2.24 | 0.025 | 0.854 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 4.32 | 1.96 | 2.20 | 0.028 | 0.877 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 4.39 | 2.06 | 2.13 | 0.033 | 0.911 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 4.03 | 1.96 | 2.06 | 0.040 | 0.942 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 3.97 | 2.04 | 1.95 | 0.051 | 0.969 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 2.28 | 1.96 | 1.16 | 0.244 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | -1.18 | 1.96 | -0.60 | 0.549 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -0.59 | 2.06 | -0.29 | 0.773 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 0.66 | 1.97 | 0.33 | 0.739 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 4.15 | 2.30 | 1.80 | 0.072 | 0.991 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 3.09 | 1.96 | 1.58 | 0.115 | 0.999 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 2.91 | 1.96 | 1.48 | 0.138 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 2.82 | 1.96 | 1.44 | 0.150 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 2.90 | 2.06 | 1.41 | 0.160 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 2.53 | 1.96 | 1.29 | 0.196 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 2.47 | 2.03 | 1.22 | 0.223 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -3.46 | 1.96 | -1.77 | 0.077 | 0.992 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -2.88 | 2.07 | -1.39 | 0.165 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -1.63 | 1.96 | -0.83 | 0.408 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | 1.87 | 2.30 | 0.81 | 0.416 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 0.80 | 1.96 | 0.41 | 0.681 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 0.62 | 1.96 | 0.32 | 0.751 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 0.54 | 1.96 | 0.27 | 0.784 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.61 | 2.06 | 0.30 | 0.766 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 0.25 | 1.96 | 0.13 | 0.898 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 0.19 | 2.03 | 0.09 | 0.925 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 0.58 | 2.07 | 0.28 | 0.779 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 1.83 | 1.96 | 0.93 | 0.350 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 5.33 | 2.30 | 2.31 | 0.021 | 0.795 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 4.26 | 1.96 | 2.18 | 0.030 | 0.888 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 4.08 | 1.97 | 2.07 | 0.038 | 0.937 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 3.99 | 1.96 | 2.04 | 0.042 | 0.948 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 4.07 | 2.06 | 1.98 | 0.048 | 0.964 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 3.71 | 1.96 | 1.89 | 0.058 | 0.979 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 3.65 | 2.04 | 1.79 | 0.073 | 0.991 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 1.25 | 2.09 | 0.60 | 0.550 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 4.75 | 2.40 | 1.98 | 0.048 | 0.964 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 3.68 | 2.07 | 1.78 | 0.075 | 0.991 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 3.50 | 2.06 | 1.70 | 0.089 | 0.996 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 3.41 | 2.06 | 1.65 | 0.098 | 0.997 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 3.49 | 2.16 | 1.62 | 0.106 | 0.998 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 3.13 | 2.06 | 1.52 | 0.130 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 3.07 | 2.13 | 1.44 | 0.150 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 3.50 | 2.31 | 1.52 | 0.130 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 2.43 | 1.97 | 1.24 | 0.217 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 2.25 | 1.99 | 1.13 | 0.258 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 2.16 | 1.98 | 1.09 | 0.274 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 2.24 | 2.07 | 1.08 | 0.279 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 1.88 | 1.97 | 0.95 | 0.341 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 1.82 | 2.05 | 0.89 | 0.376 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -1.07 | 2.30 | -0.46 | 0.643 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -1.25 | 2.31 | -0.54 | 0.589 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -1.33 | 2.30 | -0.58 | 0.563 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -1.26 | 2.39 | -0.53 | 0.599 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | -1.62 | 2.30 | -0.70 | 0.482 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | -1.68 | 2.37 | -0.71 | 0.479 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | -0.18 | 1.96 | -0.09 | 0.926 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | -0.27 | 1.96 | -0.14 | 0.891 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -0.19 | 2.06 | -0.09 | 0.926 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | -0.55 | 1.96 | -0.28 | 0.778 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | -0.61 | 2.03 | -0.30 | 0.763 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -0.09 | 1.96 | -0.04 | 0.965 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -0.01 | 2.07 | -0.00 | 0.996 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -0.37 | 1.96 | -0.19 | 0.850 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | -0.43 | 2.03 | -0.21 | 0.832 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 0.08 | 2.06 | 0.04 | 0.970 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | -0.29 | 1.96 | -0.15 | 0.884 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | -0.35 | 2.03 | -0.17 | 0.865 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | -0.36 | 2.06 | -0.18 | 0.860 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | -0.42 | 2.13 | -0.20 | 0.843 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -0.06 | 2.03 | -0.03 | 0.976 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.74, *p* = 0.070, η²_G = 0.126
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | 0.26 | 8 | = 0.929 | 0.06 [-0.17, 0.69] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | 1.04 | 8 | = 0.613 | 0.45 [-0.04, 0.84] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | -1.35 | 8 | = 0.528 | -0.33 [-0.38, 0.47] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | 0.68 | 8 | = 0.704 | 0.27 [-0.30, 0.64] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | 0.55 | 8 | = 0.773 | 0.17 [-0.22, 0.63] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | 1.23 | 8 | = 0.585 | 0.56 [-0.09, 1.15] | medium | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 1.44 | 8 | = 0.505 | 0.52 [0.16, 1.08] | medium | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | 1.46 | 8 | = 0.505 | 0.45 [0.17, 1.09] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | 2.31 | 8 | = 0.403 | 0.96 [0.13, 1.04] | large | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | 0.23 | 8 | = 0.929 | 0.11 [-0.03, 0.96] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | 1.90 | 8 | = 0.483 | 0.45 [0.23, 1.17] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | 1.70 | 8 | = 0.497 | 0.93 [-0.10, 0.84] | large | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | 1.14 | 8 | = 0.590 | 0.44 [-0.21, 0.64] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -1.51 | 8 | = 0.505 | -0.46 [-0.57, 0.27] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | 0.88 | 8 | = 0.665 | 0.24 [-0.52, 0.42] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | 0.35 | 8 | = 0.913 | 0.13 [-0.39, 0.45] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 1.44 | 8 | = 0.505 | 0.55 [-0.12, 1.10] | medium | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 2.00 | 8 | = 0.449 | 0.51 [-0.01, 0.87] | medium | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | 1.40 | 8 | = 0.515 | 0.43 [-0.13, 0.74] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 2.45 | 8 | = 0.403 | 0.99 [-0.11, 0.76] | large | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 0.13 | 8 | = 0.932 | 0.06 [-0.17, 0.79] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | 2.29 | 8 | = 0.403 | 0.43 [-0.01, 0.88] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | 1.86 | 8 | = 0.483 | 0.97 [-0.19, 0.73] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | -2.04 | 8 | = 0.449 | -0.98 [-0.83, 0.05] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | -0.67 | 8 | = 0.704 | -0.17 [-0.76, 0.19] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | -0.63 | 8 | = 0.723 | -0.31 [-0.61, 0.25] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | 0.76 | 8 | = 0.704 | 0.16 [-0.47, 0.69] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 0.32 | 8 | = 0.926 | 0.11 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 0.12 | 8 | = 0.932 | 0.05 [-0.34, 0.50] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 1.55 | 8 | = 0.497 | 0.58 [-0.36, 0.49] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.85 | 8 | = 0.665 | -0.37 [-0.50, 0.43] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 0.13 | 8 | = 0.932 | 0.05 [-0.39, 0.45] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 1.60 | 8 | = 0.497 | 0.54 [-0.40, 0.51] | medium | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 1.55 | 8 | = 0.497 | 0.68 [-0.42, 0.52] | medium | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | 2.53 | 8 | = 0.403 | 0.60 [-0.24, 0.62] | medium | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 2.14 | 8 | = 0.449 | 1.01 [0.22, 1.59] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 2.50 | 8 | = 0.403 | 0.99 [-0.01, 0.87] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | 2.08 | 8 | = 0.449 | 0.85 [0.07, 0.97] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 3.82 | 8 | = 0.397 | 1.55 [0.01, 0.90] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | 0.98 | 8 | = 0.647 | 0.52 [-0.13, 0.83] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | 2.68 | 8 | = 0.403 | 0.85 [0.00, 0.89] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | 2.87 | 8 | = 0.403 | 1.56 [-0.16, 0.77] | large | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | -0.25 | 8 | = 0.929 | -0.12 [-0.39, 0.54] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | 1.79 | 8 | = 0.483 | 0.31 [0.13, 1.62] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 1.25 | 8 | = 0.583 | 0.27 [-0.16, 0.81] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | 0.49 | 8 | = 0.811 | 0.20 [-0.22, 0.73] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | 1.80 | 8 | = 0.483 | 0.71 [-0.07, 0.91] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | -0.38 | 8 | = 0.894 | -0.17 [-0.32, 0.68] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | 0.69 | 8 | = 0.704 | 0.20 [-0.16, 0.81] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | 1.67 | 8 | = 0.497 | 0.67 [-0.10, 0.97] | medium | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.92 | 8 | = 0.665 | 0.44 [-0.32, 0.85] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 1.14 | 8 | = 0.590 | 0.39 [-0.17, 0.69] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | 0.71 | 8 | = 0.704 | 0.32 [-0.20, 0.66] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | 2.36 | 8 | = 0.403 | 0.86 [-0.18, 0.68] | large | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | -0.10 | 8 | = 0.932 | -0.06 [-0.33, 0.61] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | 1.15 | 8 | = 0.590 | 0.32 [-0.20, 0.66] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | 1.62 | 8 | = 0.497 | 0.83 [-0.26, 0.66] | large | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | -0.16 | 8 | = 0.932 | -0.05 [-0.77, 0.40] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | -0.21 | 8 | = 0.932 | -0.10 [-0.74, 0.43] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | 1.11 | 8 | = 0.595 | 0.36 [-0.54, 0.61] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | -1.10 | 8 | = 0.595 | -0.49 [-0.86, 0.43] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -0.26 | 8 | = 0.929 | -0.10 [-0.75, 0.41] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | 0.87 | 8 | = 0.665 | 0.32 [-0.48, 0.80] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -0.13 | 8 | = 0.932 | -0.05 [-0.42, 0.42] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | 1.04 | 8 | = 0.613 | 0.42 [-0.44, 0.40] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | -0.84 | 8 | = 0.665 | -0.45 [-0.49, 0.45] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -0.24 | 8 | = 0.929 | -0.05 [-0.50, 0.34] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | 0.89 | 8 | = 0.665 | 0.38 [-0.53, 0.39] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 1.18 | 8 | = 0.590 | 0.45 [-0.44, 0.41] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.76 | 8 | = 0.704 | -0.37 [-0.39, 0.55] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | 0.00 | 8 | = 1.000 | 0.00 [-0.47, 0.37] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | 0.72 | 8 | = 0.704 | 0.41 [-0.46, 0.46] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -1.71 | 8 | = 0.497 | -0.92 [-0.47, 0.47] | large | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | -1.34 | 8 | = 0.528 | -0.45 [-0.47, 0.38] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | -0.12 | 8 | = 0.932 | -0.06 [-0.55, 0.37] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | 0.71 | 8 | = 0.704 | 0.37 [-0.49, 0.45] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | 2.67 | 8 | = 0.403 | 0.89 [-0.50, 0.50] | large | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.86 | 8 | = 0.665 | 0.41 [-0.49, 0.42] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1307.86, BIC = 1366.64
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 0.17, *SE* = 0.591, *z* = 0.290, *p* = 0.772
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = 0.22, *SE* = 0.590, *z* = 0.373, *p* = 0.709
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -0.19, *SE* = 0.590, *z* = -0.320, *p* = 0.749
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -0.71, *SE* = 0.625, *z* = -1.132, *p* = 0.258
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = -0.40, *SE* = 0.591, *z* = -0.670, *p* = 0.503
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = -1.54, *SE* = 0.693, *z* = -2.229, *p* = 0.026
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 0.05, *SE* = 0.590, *z* = 0.083, *p* = 0.934
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -0.34, *SE* = 0.593, *z* = -0.567, *p* = 0.571
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = 0.10, *SE* = 0.591, *z* = 0.175, *p* = 0.861
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = 0.20, *SE* = 0.621, *z* = 0.322, *p* = 0.748
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = 0.01, *SE* = 0.591, *z* = 0.025, *p* = 0.980
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -0.28, *SE* = 0.614, *z* = -0.463, *p* = 0.643
- **SNR**: *β* = -0.24, *SE* = 0.084, *z* = -2.847, *p* = 0.004

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -0.17 | 0.59 | -0.29 | 0.772 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | -0.22 | 0.59 | -0.37 | 0.709 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 0.19 | 0.59 | 0.32 | 0.749 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 0.71 | 0.63 | 1.13 | 0.258 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | 0.40 | 0.59 | 0.67 | 0.503 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | 1.54 | 0.69 | 2.23 | 0.026 | 0.848 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | -0.05 | 0.59 | -0.08 | 0.934 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 0.34 | 0.59 | 0.57 | 0.571 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | -0.10 | 0.59 | -0.18 | 0.861 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | -0.20 | 0.62 | -0.32 | 0.748 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | -0.01 | 0.59 | -0.03 | 0.980 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 0.28 | 0.61 | 0.46 | 0.643 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | -0.05 | 0.59 | -0.08 | 0.934 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 0.36 | 0.59 | 0.61 | 0.543 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | 0.88 | 0.62 | 1.41 | 0.157 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 0.57 | 0.60 | 0.95 | 0.340 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 1.72 | 0.69 | 2.47 | 0.013 | 0.646 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 0.12 | 0.59 | 0.21 | 0.836 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 0.51 | 0.59 | 0.86 | 0.390 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 0.07 | 0.59 | 0.11 | 0.909 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | -0.03 | 0.62 | -0.05 | 0.963 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 0.16 | 0.59 | 0.26 | 0.791 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 0.46 | 0.61 | 0.74 | 0.456 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | 0.41 | 0.59 | 0.69 | 0.489 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | 0.93 | 0.62 | 1.49 | 0.137 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | 0.62 | 0.59 | 1.04 | 0.298 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | 1.76 | 0.69 | 2.55 | 0.011 | 0.575 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 0.17 | 0.59 | 0.29 | 0.772 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 0.56 | 0.59 | 0.94 | 0.348 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 0.12 | 0.59 | 0.20 | 0.844 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.02 | 0.62 | 0.03 | 0.974 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 0.20 | 0.59 | 0.35 | 0.728 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 0.50 | 0.61 | 0.82 | 0.411 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 0.52 | 0.62 | 0.83 | 0.406 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 0.21 | 0.59 | 0.35 | 0.726 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 1.36 | 0.69 | 1.96 | 0.050 | 0.975 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | -0.24 | 0.59 | -0.40 | 0.687 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 0.15 | 0.59 | 0.25 | 0.804 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | -0.29 | 0.59 | -0.49 | 0.621 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | -0.39 | 0.62 | -0.63 | 0.532 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | -0.20 | 0.59 | -0.34 | 0.730 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 0.10 | 0.61 | 0.16 | 0.876 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -0.31 | 0.63 | -0.49 | 0.621 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 0.84 | 0.72 | 1.16 | 0.247 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | -0.76 | 0.62 | -1.21 | 0.225 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | -0.37 | 0.62 | -0.60 | 0.549 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | -0.81 | 0.62 | -1.31 | 0.192 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | -0.91 | 0.65 | -1.39 | 0.164 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | -0.72 | 0.62 | -1.16 | 0.245 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | -0.42 | 0.64 | -0.66 | 0.510 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 1.15 | 0.69 | 1.65 | 0.098 | 0.999 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | -0.44 | 0.59 | -0.75 | 0.453 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | -0.06 | 0.60 | -0.10 | 0.920 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | -0.50 | 0.60 | -0.84 | 0.401 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | -0.60 | 0.62 | -0.96 | 0.339 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | -0.41 | 0.59 | -0.69 | 0.489 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | -0.11 | 0.62 | -0.18 | 0.857 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -1.59 | 0.69 | -2.30 | 0.022 | 0.800 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -1.21 | 0.70 | -1.74 | 0.082 | 0.997 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -1.65 | 0.69 | -2.37 | 0.018 | 0.735 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -1.74 | 0.72 | -2.43 | 0.015 | 0.689 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | -1.56 | 0.69 | -2.25 | 0.025 | 0.837 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | -1.26 | 0.71 | -1.77 | 0.077 | 0.996 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 0.38 | 0.59 | 0.65 | 0.515 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | -0.05 | 0.59 | -0.09 | 0.926 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -0.15 | 0.62 | -0.24 | 0.808 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 0.03 | 0.59 | 0.06 | 0.954 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 0.33 | 0.61 | 0.54 | 0.587 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -0.44 | 0.59 | -0.75 | 0.456 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -0.54 | 0.62 | -0.86 | 0.389 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -0.35 | 0.59 | -0.59 | 0.552 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | -0.05 | 0.61 | -0.08 | 0.933 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -0.10 | 0.62 | -0.15 | 0.877 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 0.09 | 0.59 | 0.15 | 0.881 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 0.39 | 0.61 | 0.63 | 0.526 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 0.18 | 0.62 | 0.30 | 0.766 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 0.48 | 0.64 | 0.75 | 0.451 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 0.30 | 0.61 | 0.49 | 0.625 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.58, *p* = 0.854, η²_G = 0.057
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | -0.41 | 8 | = 0.983 | -0.14 [-0.63, 0.22] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | -0.17 | 8 | = 0.983 | -0.07 [-0.54, 0.30] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | 0.44 | 8 | = 0.983 | 0.19 [-0.26, 0.59] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | 0.87 | 8 | = 0.983 | 0.36 [-0.33, 0.61] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | 0.73 | 8 | = 0.983 | 0.29 [-0.09, 0.78] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | 0.92 | 8 | = 0.983 | 0.48 [-0.32, 0.85] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | -1.00 | 8 | = 0.983 | -0.42 [-0.51, 0.34] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | -0.56 | 8 | = 0.983 | -0.19 [-0.32, 0.52] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | -0.60 | 8 | = 0.983 | -0.14 [-0.66, 0.19] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | -0.55 | 8 | = 0.983 | -0.27 [-0.58, 0.36] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | -0.24 | 8 | = 0.983 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | 0.19 | 8 | = 0.983 | 0.08 [-0.39, 0.52] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | 0.05 | 8 | = 0.983 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | 0.81 | 8 | = 0.983 | 0.32 [-0.08, 0.79] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | 0.96 | 8 | = 0.983 | 0.42 [-0.23, 0.72] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | 1.34 | 8 | = 0.983 | 0.38 [0.03, 0.92] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 1.11 | 8 | = 0.983 | 0.52 [-0.25, 0.94] | medium | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | -0.70 | 8 | = 0.983 | -0.20 [-0.29, 0.55] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -0.05 | 8 | = 0.983 | -0.03 [-0.21, 0.64] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 0.06 | 8 | = 0.983 | 0.01 [-0.36, 0.49] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | -0.32 | 8 | = 0.983 | -0.16 [-0.43, 0.51] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | 0.09 | 8 | = 0.983 | 0.04 [-0.31, 0.54] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | 0.33 | 8 | = 0.983 | 0.13 [-0.35, 0.56] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | 0.30 | 8 | = 0.983 | 0.15 [-0.25, 0.60] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | 1.60 | 8 | = 0.983 | 0.34 [-0.28, 0.67] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | 0.57 | 8 | = 0.983 | 0.23 [-0.11, 0.76] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | 1.08 | 8 | = 0.983 | 0.47 [-0.23, 0.97] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | -0.34 | 8 | = 0.983 | -0.14 [-0.36, 0.49] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | -0.08 | 8 | = 0.983 | -0.04 [-0.28, 0.57] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | -0.03 | 8 | = 0.983 | -0.01 [-0.41, 0.43] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.25 | 8 | = 0.983 | -0.14 [-0.49, 0.45] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 0.02 | 8 | = 0.983 | 0.01 [-0.35, 0.49] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 0.33 | 8 | = 0.983 | 0.11 [-0.40, 0.51] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 0.62 | 8 | = 0.983 | 0.31 [-0.33, 0.61] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | 0.38 | 8 | = 0.983 | 0.19 [-0.25, 0.61] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 0.92 | 8 | = 0.983 | 0.44 [-0.32, 0.85] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | -1.64 | 8 | = 0.983 | -0.78 [-0.63, 0.23] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | -0.75 | 8 | = 0.983 | -0.42 [-0.44, 0.40] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | -0.97 | 8 | = 0.983 | -0.34 [-0.75, 0.11] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | -0.89 | 8 | = 0.983 | -0.38 [-0.60, 0.34] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | -0.54 | 8 | = 0.983 | -0.28 [-0.62, 0.23] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | 0.07 | 8 | = 0.983 | 0.04 [-0.48, 0.43] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | -0.43 | 8 | = 0.983 | -0.20 [-0.46, 0.48] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | 0.54 | 8 | = 0.983 | 0.22 [-0.32, 0.99] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | -1.33 | 8 | = 0.983 | -0.54 [-0.64, 0.30] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | -0.99 | 8 | = 0.983 | -0.45 [-0.72, 0.23] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | -0.92 | 8 | = 0.983 | -0.42 [-0.68, 0.27] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | -0.89 | 8 | = 0.983 | -0.48 [-0.62, 0.38] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | -1.01 | 8 | = 0.983 | -0.40 [-0.68, 0.27] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.34 | 8 | = 0.983 | -0.14 [-0.60, 0.43] | negligible | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.77 | 8 | = 0.983 | 0.38 [-0.41, 0.75] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | -2.21 | 8 | = 0.983 | -0.66 [-0.84, 0.04] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | -0.91 | 8 | = 0.983 | -0.45 [-0.61, 0.24] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | -1.14 | 8 | = 0.983 | -0.40 [-0.91, -0.02] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | -0.95 | 8 | = 0.983 | -0.44 [-0.67, 0.28] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | -0.78 | 8 | = 0.983 | -0.35 [-0.76, 0.11] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | -0.06 | 8 | = 0.983 | -0.02 [-0.51, 0.40] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | -1.31 | 8 | = 0.983 | -0.59 [-0.91, 0.27] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | -1.04 | 8 | = 0.983 | -0.53 [-0.84, 0.34] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | -1.05 | 8 | = 0.983 | -0.52 [-0.91, 0.27] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | -1.19 | 8 | = 0.983 | -0.57 [-0.95, 0.35] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -1.05 | 8 | = 0.983 | -0.51 [-0.89, 0.29] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | -0.59 | 8 | = 0.983 | -0.30 [-0.78, 0.49] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | 0.35 | 8 | = 0.983 | 0.20 [-0.28, 0.56] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | 0.66 | 8 | = 0.983 | 0.24 [-0.52, 0.33] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | -0.08 | 8 | = 0.983 | -0.04 [-0.53, 0.41] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | 0.57 | 8 | = 0.983 | 0.26 [-0.42, 0.42] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | 0.47 | 8 | = 0.983 | 0.19 [-0.37, 0.54] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 0.09 | 8 | = 0.983 | 0.04 [-0.64, 0.22] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.29 | 8 | = 0.983 | -0.15 [-0.55, 0.38] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | 0.20 | 8 | = 0.983 | 0.07 [-0.60, 0.25] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | 0.29 | 8 | = 0.983 | 0.14 [-0.45, 0.46] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -0.39 | 8 | = 0.983 | -0.17 [-0.50, 0.43] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | 0.07 | 8 | = 0.983 | 0.03 [-0.34, 0.50] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | 0.30 | 8 | = 0.983 | 0.12 [-0.35, 0.57] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | 0.34 | 8 | = 0.983 | 0.19 [-0.40, 0.53] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | 0.43 | 8 | = 0.983 | 0.20 [-0.43, 0.56] | negligible | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.27 | 8 | = 0.983 | 0.11 [-0.39, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 2371.03, BIC = 2429.80
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 3.01, *SE* = 3.501, *z* = 0.859, *p* = 0.391
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -2.66, *SE* = 3.535, *z* = -0.754, *p* = 0.451
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 1.63, *SE* = 3.506, *z* = 0.465, *p* = 0.642
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -1.48, *SE* = 3.757, *z* = -0.393, *p* = 0.694
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 1.35, *SE* = 3.511, *z* = 0.384, *p* = 0.701
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 0.77, *SE* = 4.169, *z* = 0.184, *p* = 0.854
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -4.56, *SE* = 3.524, *z* = -1.293, *p* = 0.196
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 1.72, *SE* = 3.505, *z* = 0.491, *p* = 0.623
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -6.59, *SE* = 3.519, *z* = -1.873, *p* = 0.061
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -4.82, *SE* = 3.706, *z* = -1.300, *p* = 0.194
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -4.00, *SE* = 3.509, *z* = -1.141, *p* = 0.254
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -9.53, *SE* = 3.717, *z* = -2.565, *p* = 0.010
- **SNR**: *β* = -0.13, *SE* = 0.191, *z* = -0.680, *p* = 0.496

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -3.01 | 3.50 | -0.86 | 0.391 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 2.66 | 3.53 | 0.75 | 0.451 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | -1.63 | 3.51 | -0.46 | 0.642 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 1.48 | 3.76 | 0.39 | 0.694 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | -1.35 | 3.51 | -0.38 | 0.701 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -0.76 | 4.17 | -0.18 | 0.854 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | 4.56 | 3.52 | 1.29 | 0.196 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -1.72 | 3.50 | -0.49 | 0.623 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 6.59 | 3.52 | 1.87 | 0.061 | 0.981 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 4.82 | 3.71 | 1.30 | 0.194 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 4.00 | 3.51 | 1.14 | 0.254 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 9.53 | 3.72 | 2.56 | 0.010 | 0.531 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 5.67 | 3.54 | 1.60 | 0.109 | 0.998 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 1.38 | 3.51 | 0.39 | 0.695 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | 4.48 | 3.76 | 1.19 | 0.233 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 1.66 | 3.51 | 0.47 | 0.637 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 2.24 | 4.17 | 0.54 | 0.591 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 7.56 | 3.52 | 2.15 | 0.032 | 0.889 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 1.28 | 3.51 | 0.37 | 0.714 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 9.60 | 3.52 | 2.73 | 0.006 | 0.377 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 7.82 | 3.71 | 2.11 | 0.035 | 0.907 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 7.01 | 3.51 | 2.00 | 0.046 | 0.952 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 12.54 | 3.72 | 3.37 | < .001 | 0.057 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -4.29 | 3.57 | -1.20 | 0.229 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -1.19 | 3.69 | -0.32 | 0.748 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -4.01 | 3.58 | -1.12 | 0.263 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -3.43 | 4.12 | -0.83 | 0.406 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 1.89 | 3.61 | 0.52 | 0.600 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | -4.39 | 3.52 | -1.25 | 0.212 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 3.93 | 3.60 | 1.09 | 0.276 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 2.15 | 3.69 | 0.58 | 0.559 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 1.34 | 3.58 | 0.37 | 0.708 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 6.87 | 3.65 | 1.88 | 0.060 | 0.980 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 3.11 | 3.80 | 0.82 | 0.413 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 0.28 | 3.50 | 0.08 | 0.936 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 0.86 | 4.20 | 0.21 | 0.837 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 6.19 | 3.51 | 1.76 | 0.078 | 0.993 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | -0.09 | 3.52 | -0.03 | 0.979 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 8.22 | 3.50 | 2.35 | 0.019 | 0.741 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 6.45 | 3.73 | 1.73 | 0.084 | 0.994 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 5.63 | 3.50 | 1.61 | 0.108 | 0.998 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 11.16 | 3.76 | 2.97 | 0.003 | 0.204 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -2.83 | 3.82 | -0.74 | 0.459 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | -2.24 | 4.28 | -0.52 | 0.600 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 3.08 | 3.86 | 0.80 | 0.425 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | -3.20 | 3.73 | -0.86 | 0.391 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 5.11 | 3.84 | 1.33 | 0.183 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 3.34 | 3.87 | 0.86 | 0.388 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 2.53 | 3.81 | 0.66 | 0.508 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 8.06 | 3.82 | 2.11 | 0.035 | 0.907 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 0.58 | 4.22 | 0.14 | 0.890 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 5.91 | 3.50 | 1.69 | 0.092 | 0.996 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | -0.37 | 3.53 | -0.11 | 0.916 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 7.94 | 3.50 | 2.27 | 0.023 | 0.805 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 6.17 | 3.74 | 1.65 | 0.099 | 0.997 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 5.35 | 3.50 | 1.53 | 0.126 | 0.999 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 10.88 | 3.78 | 2.88 | 0.004 | 0.260 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 5.32 | 4.25 | 1.25 | 0.210 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -0.96 | 4.15 | -0.23 | 0.818 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | 7.36 | 4.24 | 1.74 | 0.083 | 0.994 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 5.58 | 4.28 | 1.30 | 0.192 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 4.77 | 4.21 | 1.13 | 0.258 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 10.30 | 4.24 | 2.43 | 0.015 | 0.666 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | -6.28 | 3.55 | -1.77 | 0.077 | 0.993 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 2.03 | 3.50 | 0.58 | 0.562 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 0.26 | 3.77 | 0.07 | 0.945 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | -0.55 | 3.50 | -0.16 | 0.874 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 4.98 | 3.82 | 1.30 | 0.193 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | 8.31 | 3.54 | 2.35 | 0.019 | 0.741 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | 6.54 | 3.69 | 1.77 | 0.077 | 0.993 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | 5.73 | 3.52 | 1.62 | 0.104 | 0.998 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 11.26 | 3.69 | 3.05 | 0.002 | 0.160 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -1.77 | 3.76 | -0.47 | 0.637 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | -2.59 | 3.50 | -0.74 | 0.460 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 2.94 | 3.81 | 0.77 | 0.440 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | -0.81 | 3.74 | -0.22 | 0.827 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 4.72 | 3.83 | 1.23 | 0.218 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 5.53 | 3.78 | 1.46 | 0.143 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.81, *p* = 0.642, η²_G = 0.027
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | -0.89 | 8 | = 0.827 | -0.07 [-0.70, 0.16] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | 0.00 | 8 | = 1.000 | 0.00 [-0.29, 0.56] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | -0.66 | 8 | = 0.904 | -0.10 [-0.56, 0.29] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | 1.64 | 8 | = 0.827 | 0.31 [-0.50, 0.44] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -1.67 | 8 | = 0.827 | -0.17 [-0.49, 0.35] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | 0.06 | 8 | = 0.983 | 0.02 [-0.70, 0.45] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 0.47 | 8 | = 0.922 | 0.08 [-0.09, 0.78] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | -1.51 | 8 | = 0.827 | -0.18 [-0.64, 0.21] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | 1.18 | 8 | = 0.827 | 0.09 [0.04, 0.94] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | 1.23 | 8 | = 0.827 | 0.37 [-0.22, 0.73] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | -0.33 | 8 | = 0.968 | -0.04 [-0.16, 0.70] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | 0.43 | 8 | = 0.925 | 0.11 [0.09, 1.07] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | 0.32 | 8 | = 0.968 | 0.07 [-0.11, 0.76] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -0.14 | 8 | = 0.983 | -0.02 [-0.29, 0.56] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | 1.71 | 8 | = 0.827 | 0.38 [-0.23, 0.73] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | -0.88 | 8 | = 0.827 | -0.10 [-0.24, 0.61] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 0.22 | 8 | = 0.983 | 0.09 [-0.49, 0.67] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 0.89 | 8 | = 0.827 | 0.15 [0.05, 0.94] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -0.74 | 8 | = 0.889 | -0.11 [-0.34, 0.51] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 2.40 | 8 | = 0.783 | 0.15 [0.22, 1.16] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 1.34 | 8 | = 0.827 | 0.44 [-0.09, 0.89] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | 0.15 | 8 | = 0.983 | 0.02 [0.03, 0.92] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | 0.59 | 8 | = 0.905 | 0.17 [0.18, 1.19] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | -0.71 | 8 | = 0.903 | -0.10 [-0.64, 0.21] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | 1.30 | 8 | = 0.827 | 0.32 [-0.57, 0.36] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | -0.77 | 8 | = 0.882 | -0.17 [-0.59, 0.26] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | 0.05 | 8 | = 0.983 | 0.02 [-0.64, 0.52] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 0.40 | 8 | = 0.939 | 0.08 [-0.26, 0.59] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | -1.36 | 8 | = 0.827 | -0.18 [-0.65, 0.21] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 0.46 | 8 | = 0.922 | 0.09 [-0.14, 0.73] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | 1.50 | 8 | = 0.827 | 0.38 [-0.33, 0.61] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | -0.16 | 8 | = 0.983 | -0.04 [-0.33, 0.52] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 0.64 | 8 | = 0.904 | 0.11 [0.03, 1.00] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 1.55 | 8 | = 0.827 | 0.43 [-0.34, 0.60] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | -0.49 | 8 | = 0.922 | -0.08 [-0.40, 0.45] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 0.34 | 8 | = 0.968 | 0.12 [-0.68, 0.48] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 1.02 | 8 | = 0.827 | 0.18 [-0.08, 0.80] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | -0.84 | 8 | = 0.852 | -0.10 [-0.45, 0.40] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 1.36 | 8 | = 0.827 | 0.19 [0.10, 1.00] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | 2.09 | 8 | = 0.783 | 0.50 [-0.05, 0.93] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | 0.21 | 8 | = 0.983 | 0.05 [-0.10, 0.77] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | 1.03 | 8 | = 0.827 | 0.21 [0.20, 1.22] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | -2.44 | 8 | = 0.783 | -0.49 [-0.61, 0.33] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | -0.60 | 8 | = 0.905 | -0.30 [-0.79, 0.48] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | -0.68 | 8 | = 0.904 | -0.22 [-0.34, 0.60] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | -2.12 | 8 | = 0.783 | -0.49 [-0.50, 0.44] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | -0.98 | 8 | = 0.827 | -0.23 [-0.29, 0.65] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | 0.05 | 8 | = 0.983 | 0.02 [-0.41, 0.59] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | -1.50 | 8 | = 0.827 | -0.34 [-0.41, 0.53] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.78 | 8 | = 0.882 | -0.20 [-0.23, 0.82] | small | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.48 | 8 | = 0.922 | 0.19 [-0.50, 0.65] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 1.07 | 8 | = 0.827 | 0.24 [-0.13, 0.73] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | -0.13 | 8 | = 0.983 | -0.02 [-0.46, 0.38] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | 2.14 | 8 | = 0.783 | 0.26 [0.05, 0.95] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 1.67 | 8 | = 0.827 | 0.57 [-0.26, 0.69] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | 0.96 | 8 | = 0.827 | 0.11 [-0.09, 0.78] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | 1.02 | 8 | = 0.827 | 0.27 [0.04, 1.01] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 0.16 | 8 | = 0.983 | 0.06 [-0.39, 0.78] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | -0.50 | 8 | = 0.922 | -0.20 [-0.63, 0.52] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | 0.16 | 8 | = 0.983 | 0.07 [-0.28, 0.90] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | 1.08 | 8 | = 0.827 | 0.35 [-0.29, 1.03] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -0.17 | 8 | = 0.983 | -0.06 [-0.39, 0.77] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | 0.20 | 8 | = 0.983 | 0.09 [-0.31, 0.99] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -1.75 | 8 | = 0.827 | -0.25 [-0.88, 0.00] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | 0.00 | 8 | = 1.000 | 0.00 [-0.23, 0.62] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | 1.09 | 8 | = 0.827 | 0.26 [-0.43, 0.51] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -0.54 | 8 | = 0.922 | -0.12 [-0.47, 0.37] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | 0.07 | 8 | = 0.983 | 0.02 [-0.23, 0.70] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 2.41 | 8 | = 0.783 | 0.26 [0.05, 0.94] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | 2.26 | 8 | = 0.783 | 0.56 [-0.11, 0.86] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | 0.63 | 8 | = 0.904 | 0.13 [-0.12, 0.75] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | 1.30 | 8 | = 0.827 | 0.28 [0.10, 1.09] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 0.92 | 8 | = 0.827 | 0.27 [-0.53, 0.40] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | -0.92 | 8 | = 0.827 | -0.12 [-0.80, 0.07] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | 0.08 | 8 | = 0.983 | 0.02 [-0.33, 0.59] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | -1.13 | 8 | = 0.827 | -0.39 [-0.54, 0.40] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.93 | 8 | = 0.827 | -0.24 [-0.43, 0.56] | small | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.45 | 8 | = 0.922 | 0.14 [-0.21, 0.71] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1226.17, BIC = 1284.94
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = -0.24, *SE* = 0.494, *z* = -0.482, *p* = 0.629
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -1.02, *SE* = 0.499, *z* = -2.040, *p* = 0.041
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -0.31, *SE* = 0.495, *z* = -0.634, *p* = 0.526
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -0.86, *SE* = 0.531, *z* = -1.629, *p* = 0.103
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = -0.34, *SE* = 0.496, *z* = -0.680, *p* = 0.497
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = -2.18, *SE* = 0.588, *z* = -3.707, *p* < .001
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -0.05, *SE* = 0.498, *z* = -0.097, *p* = 0.923
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -1.03, *SE* = 0.495, *z* = -2.091, *p* = 0.037
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -0.49, *SE* = 0.497, *z* = -0.991, *p* = 0.322
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -1.44, *SE* = 0.523, *z* = -2.755, *p* = 0.006
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -1.30, *SE* = 0.495, *z* = -2.632, *p* = 0.008
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -2.62, *SE* = 0.525, *z* = -4.996, *p* < .001
- **SNR**: *β* = -0.19, *SE* = 0.027, *z* = -7.031, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | 0.24 | 0.49 | 0.48 | 0.629 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 1.02 | 0.50 | 2.04 | 0.041 | 0.884 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 0.31 | 0.49 | 0.63 | 0.526 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 0.86 | 0.53 | 1.63 | 0.103 | 0.990 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | 0.34 | 0.50 | 0.68 | 0.497 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | 2.18 | 0.59 | 3.71 | < .001 | 0.015 | * |
| Cardinality (no change) - Increase by 1 (Correct) | 0.05 | 0.50 | 0.10 | 0.923 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 1.03 | 0.49 | 2.09 | 0.037 | 0.861 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 0.49 | 0.50 | 0.99 | 0.322 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 1.44 | 0.52 | 2.75 | 0.006 | 0.310 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 1.30 | 0.50 | 2.63 | 0.008 | 0.411 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 2.62 | 0.52 | 5.00 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 0.78 | 0.50 | 1.56 | 0.118 | 0.993 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 0.08 | 0.49 | 0.15 | 0.879 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | 0.63 | 0.53 | 1.18 | 0.238 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 0.10 | 0.50 | 0.20 | 0.842 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 1.94 | 0.59 | 3.30 | < .001 | 0.065 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | -0.19 | 0.50 | -0.38 | 0.702 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 0.80 | 0.49 | 1.61 | 0.108 | 0.991 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 0.25 | 0.50 | 0.51 | 0.609 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 1.20 | 0.52 | 2.30 | 0.022 | 0.717 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 1.07 | 0.50 | 2.15 | 0.031 | 0.828 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 2.38 | 0.53 | 4.54 | < .001 | < .001 | *** |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -0.70 | 0.50 | -1.40 | 0.162 | 0.998 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -0.15 | 0.52 | -0.29 | 0.768 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -0.68 | 0.51 | -1.35 | 0.178 | 0.999 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | 1.16 | 0.58 | 2.00 | 0.046 | 0.901 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | -0.97 | 0.51 | -1.90 | 0.057 | 0.929 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 0.02 | 0.50 | 0.03 | 0.974 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | -0.53 | 0.51 | -1.03 | 0.301 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.42 | 0.52 | 0.81 | 0.417 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 0.29 | 0.50 | 0.57 | 0.571 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 1.60 | 0.51 | 3.12 | 0.002 | 0.116 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 0.55 | 0.54 | 1.03 | 0.305 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 0.02 | 0.49 | 0.05 | 0.962 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 1.87 | 0.59 | 3.15 | 0.002 | 0.105 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | -0.27 | 0.50 | -0.54 | 0.592 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 0.72 | 0.50 | 1.45 | 0.147 | 0.997 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 0.18 | 0.49 | 0.36 | 0.718 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 1.13 | 0.53 | 2.14 | 0.032 | 0.830 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 0.99 | 0.49 | 2.00 | 0.045 | 0.901 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 2.31 | 0.53 | 4.35 | < .001 | 0.001 | ** |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -0.53 | 0.54 | -0.98 | 0.328 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 1.32 | 0.60 | 2.18 | 0.029 | 0.812 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | -0.82 | 0.54 | -1.50 | 0.134 | 0.996 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 0.17 | 0.53 | 0.32 | 0.747 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | -0.37 | 0.54 | -0.69 | 0.493 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 0.58 | 0.55 | 1.06 | 0.291 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 0.44 | 0.54 | 0.82 | 0.414 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 1.76 | 0.54 | 3.26 | 0.001 | 0.073 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 1.84 | 0.60 | 3.10 | 0.002 | 0.121 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | -0.29 | 0.49 | -0.58 | 0.559 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 0.70 | 0.50 | 1.40 | 0.161 | 0.998 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 0.16 | 0.49 | 0.31 | 0.753 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 1.10 | 0.53 | 2.09 | 0.037 | 0.861 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 0.97 | 0.49 | 1.96 | 0.050 | 0.911 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 2.29 | 0.53 | 4.28 | < .001 | 0.001 | ** |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -2.13 | 0.60 | -3.56 | < .001 | 0.026 | * |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -1.15 | 0.59 | -1.96 | 0.050 | 0.911 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -1.69 | 0.60 | -2.82 | 0.005 | 0.263 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -0.74 | 0.60 | -1.22 | 0.221 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | -0.88 | 0.59 | -1.48 | 0.140 | 0.997 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 0.44 | 0.60 | 0.74 | 0.461 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 0.99 | 0.50 | 1.97 | 0.049 | 0.910 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 0.44 | 0.49 | 0.90 | 0.369 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 1.39 | 0.53 | 2.62 | 0.009 | 0.419 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 1.26 | 0.49 | 2.54 | 0.011 | 0.490 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 2.57 | 0.54 | 4.77 | < .001 | < .001 | *** |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -0.54 | 0.50 | -1.08 | 0.278 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.41 | 0.52 | 0.78 | 0.435 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | 0.27 | 0.50 | 0.54 | 0.588 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 1.59 | 0.52 | 3.05 | 0.002 | 0.138 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 0.95 | 0.53 | 1.79 | 0.074 | 0.966 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 0.81 | 0.49 | 1.64 | 0.101 | 0.990 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 2.13 | 0.54 | 3.96 | < .001 | 0.005 | ** |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | -0.14 | 0.53 | -0.26 | 0.795 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 1.18 | 0.54 | 2.18 | 0.029 | 0.812 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 1.32 | 0.53 | 2.47 | 0.013 | 0.549 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.71, *p* = 0.735, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | 1.97 | 8 | = 0.867 | 0.30 [-0.23, 0.62] | small | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | 0.86 | 8 | = 0.870 | 0.23 [-0.18, 0.67] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | 0.92 | 8 | = 0.867 | 0.22 [-0.12, 0.75] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | -0.09 | 8 | = 0.999 | -0.03 [-0.42, 0.52] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | 1.71 | 8 | = 0.867 | 0.34 [-0.05, 0.82] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | 0.67 | 8 | = 0.870 | 0.31 [-0.31, 0.87] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 1.45 | 8 | = 0.867 | 0.31 [-0.12, 0.74] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | 0.17 | 8 | = 0.984 | 0.03 [-0.00, 0.88] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | 2.83 | 8 | = 0.867 | 0.36 [0.17, 1.09] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | 1.99 | 8 | = 0.867 | 0.40 [0.04, 1.04] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | 2.50 | 8 | = 0.867 | 0.44 [0.49, 1.53] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | 2.14 | 8 | = 0.867 | 0.58 [0.14, 1.13] | medium | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | -0.58 | 8 | = 0.870 | -0.11 [-0.28, 0.57] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -0.65 | 8 | = 0.870 | -0.10 [-0.26, 0.59] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | -1.09 | 8 | = 0.867 | -0.30 [-0.54, 0.40] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | 0.03 | 8 | = 0.999 | 0.00 [-0.20, 0.66] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 0.26 | 8 | = 0.960 | 0.11 [-0.36, 0.81] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 0.01 | 8 | = 0.999 | 0.00 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -1.02 | 8 | = 0.867 | -0.24 [-0.16, 0.70] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 0.76 | 8 | = 0.870 | 0.09 [0.08, 0.98] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 0.50 | 8 | = 0.870 | 0.13 [-0.12, 0.84] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | 0.66 | 8 | = 0.870 | 0.15 [0.25, 1.19] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | 1.34 | 8 | = 0.867 | 0.33 [0.13, 1.13] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | -0.00 | 8 | = 0.999 | -0.00 [-0.44, 0.40] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | -1.08 | 8 | = 0.867 | -0.23 [-0.67, 0.27] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | 0.68 | 8 | = 0.870 | 0.13 [-0.39, 0.46] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | 0.47 | 8 | = 0.870 | 0.18 [-0.27, 0.91] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 0.49 | 8 | = 0.870 | 0.11 [-0.46, 0.38] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | -0.65 | 8 | = 0.870 | -0.17 [-0.29, 0.56] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 0.96 | 8 | = 0.867 | 0.19 [-0.29, 0.55] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | 0.69 | 8 | = 0.870 | 0.23 [-0.41, 0.53] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 1.01 | 8 | = 0.867 | 0.27 [0.09, 1.00] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 1.51 | 8 | = 0.867 | 0.44 [-0.02, 0.94] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | -1.23 | 8 | = 0.867 | -0.22 [-0.61, 0.33] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | 0.67 | 8 | = 0.870 | 0.12 [-0.36, 0.49] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 0.45 | 8 | = 0.870 | 0.18 [-0.31, 0.87] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 0.50 | 8 | = 0.870 | 0.10 [-0.45, 0.39] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | -0.75 | 8 | = 0.870 | -0.16 [-0.24, 0.61] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 0.91 | 8 | = 0.867 | 0.18 [-0.26, 0.59] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | 0.68 | 8 | = 0.870 | 0.22 [-0.27, 0.68] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | 0.96 | 8 | = 0.867 | 0.26 [0.08, 0.98] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | 1.27 | 8 | = 0.867 | 0.43 [-0.03, 0.92] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | 1.13 | 8 | = 0.867 | 0.32 [-0.27, 0.68] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | 0.93 | 8 | = 0.867 | 0.31 [-0.40, 0.89] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 0.98 | 8 | = 0.867 | 0.30 [-0.34, 0.60] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | 0.26 | 8 | = 0.960 | 0.06 [-0.28, 0.66] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | 1.39 | 8 | = 0.867 | 0.35 [-0.18, 0.77] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | 1.01 | 8 | = 0.867 | 0.39 [-0.19, 0.83] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | 1.35 | 8 | = 0.867 | 0.42 [-0.01, 0.98] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | 1.55 | 8 | = 0.867 | 0.56 [-0.09, 0.99] | medium | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.23 | 8 | = 0.960 | 0.11 [-0.43, 0.73] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | -0.02 | 8 | = 0.999 | -0.00 [-0.51, 0.33] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | -1.08 | 8 | = 0.867 | -0.26 [-0.30, 0.55] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | 0.44 | 8 | = 0.870 | 0.09 [-0.29, 0.55] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 0.39 | 8 | = 0.901 | 0.13 [-0.28, 0.67] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | 0.56 | 8 | = 0.870 | 0.16 [-0.01, 0.87] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | 1.17 | 8 | = 0.867 | 0.35 [-0.04, 0.91] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | -0.23 | 8 | = 0.960 | -0.11 [-0.75, 0.42] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | -0.59 | 8 | = 0.870 | -0.27 [-0.75, 0.41] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | -0.10 | 8 | = 0.999 | -0.04 [-0.68, 0.48] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | -0.03 | 8 | = 0.999 | -0.01 [-0.62, 0.65] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -0.01 | 8 | = 0.999 | -0.00 [-0.61, 0.55] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | 0.38 | 8 | = 0.901 | 0.15 [-0.63, 0.64] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -1.13 | 8 | = 0.867 | -0.24 [-0.22, 0.63] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | 0.49 | 8 | = 0.870 | 0.09 [-0.17, 0.69] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | 0.48 | 8 | = 0.870 | 0.13 [-0.30, 0.64] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | 0.63 | 8 | = 0.870 | 0.15 [0.12, 1.03] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | 1.22 | 8 | = 0.867 | 0.33 [-0.04, 0.91] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 1.67 | 8 | = 0.867 | 0.30 [-0.43, 0.41] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | 1.17 | 8 | = 0.867 | 0.34 [-0.37, 0.57] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | 1.91 | 8 | = 0.867 | 0.37 [-0.09, 0.78] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | 1.49 | 8 | = 0.867 | 0.52 [-0.16, 0.77] | medium | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 0.17 | 8 | = 0.984 | 0.04 [-0.32, 0.63] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | 0.33 | 8 | = 0.926 | 0.05 [-0.01, 0.87] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | 1.05 | 8 | = 0.867 | 0.24 [-0.13, 0.81] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | 0.06 | 8 | = 0.999 | 0.01 [-0.28, 0.67] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | 0.84 | 8 | = 0.870 | 0.21 [-0.18, 0.84] | small | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.61 | 8 | = 0.870 | 0.20 [-0.33, 0.59] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 2081.99, BIC = 2140.76
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 2.77, *SE* = 2.192, *z* = 1.266, *p* = 0.206
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -2.68, *SE* = 2.196, *z* = -1.222, *p* = 0.222
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 3.67, *SE* = 2.185, *z* = 1.681, *p* = 0.093
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 3.47, *SE* = 2.354, *z* = 1.474, *p* = 0.141
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 1.61, *SE* = 2.192, *z* = 0.734, *p* = 0.463
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 0.55, *SE* = 2.601, *z* = 0.210, *p* = 0.834
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -1.97, *SE* = 2.200, *z* = -0.897, *p* = 0.370
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -4.03, *SE* = 2.240, *z* = -1.801, *p* = 0.072
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -2.70, *SE* = 2.194, *z* = -1.229, *p* = 0.219
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -3.59, *SE* = 2.337, *z* = -1.535, *p* = 0.125
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -5.28, *SE* = 2.188, *z* = -2.411, *p* = 0.016
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -2.79, *SE* = 2.297, *z* = -1.214, *p* = 0.225
- **SNR**: *β* = 0.27, *SE* = 0.217, *z* = 1.239, *p* = 0.215

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -2.77 | 2.19 | -1.27 | 0.206 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 2.68 | 2.20 | 1.22 | 0.222 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | -3.67 | 2.19 | -1.68 | 0.093 | 0.990 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -3.47 | 2.35 | -1.47 | 0.141 | 0.998 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | -1.61 | 2.19 | -0.73 | 0.463 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -0.55 | 2.60 | -0.21 | 0.834 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | 1.97 | 2.20 | 0.90 | 0.370 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 4.03 | 2.24 | 1.80 | 0.072 | 0.974 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 2.70 | 2.19 | 1.23 | 0.219 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 3.59 | 2.34 | 1.54 | 0.125 | 0.997 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 5.28 | 2.19 | 2.41 | 0.016 | 0.599 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 2.79 | 2.30 | 1.21 | 0.225 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 5.46 | 2.18 | 2.50 | 0.012 | 0.519 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | -0.90 | 2.18 | -0.41 | 0.681 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -0.69 | 2.31 | -0.30 | 0.764 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 1.17 | 2.18 | 0.53 | 0.593 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 2.23 | 2.57 | 0.87 | 0.386 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 4.75 | 2.18 | 2.18 | 0.030 | 0.796 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 6.81 | 2.20 | 3.10 | 0.002 | 0.130 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 5.47 | 2.18 | 2.51 | 0.012 | 0.519 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 6.36 | 2.31 | 2.76 | 0.006 | 0.318 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 8.05 | 2.18 | 3.69 | < .001 | 0.017 | * |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 5.56 | 2.27 | 2.45 | 0.014 | 0.564 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -6.36 | 2.18 | -2.91 | 0.004 | 0.218 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -6.15 | 2.31 | -2.66 | 0.008 | 0.393 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -4.29 | 2.18 | -1.97 | 0.049 | 0.924 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -3.23 | 2.57 | -1.26 | 0.209 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | -0.71 | 2.18 | -0.33 | 0.745 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 1.35 | 2.20 | 0.62 | 0.538 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 0.01 | 2.18 | 0.01 | 0.995 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.90 | 2.30 | 0.39 | 0.695 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 2.59 | 2.18 | 1.19 | 0.235 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 0.11 | 2.27 | 0.05 | 0.963 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 0.20 | 2.33 | 0.09 | 0.930 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 2.06 | 2.18 | 0.95 | 0.344 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 3.13 | 2.58 | 1.21 | 0.226 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 5.65 | 2.19 | 2.58 | 0.010 | 0.457 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 7.71 | 2.21 | 3.48 | < .001 | 0.036 | * |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 6.37 | 2.18 | 2.92 | 0.004 | 0.216 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 7.26 | 2.31 | 3.14 | 0.002 | 0.116 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 8.95 | 2.18 | 4.10 | < .001 | 0.003 | ** |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 6.46 | 2.28 | 2.84 | 0.005 | 0.263 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 1.86 | 2.31 | 0.80 | 0.422 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 2.92 | 2.66 | 1.10 | 0.272 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 5.44 | 2.31 | 2.36 | 0.018 | 0.645 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 7.50 | 2.30 | 3.27 | 0.001 | 0.077 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 6.17 | 2.31 | 2.67 | 0.008 | 0.393 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 7.06 | 2.40 | 2.94 | 0.003 | 0.205 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 8.75 | 2.32 | 3.77 | < .001 | 0.013 | * |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 6.26 | 2.38 | 2.63 | 0.009 | 0.417 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 1.06 | 2.57 | 0.41 | 0.679 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 3.58 | 2.18 | 1.64 | 0.101 | 0.992 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 5.64 | 2.20 | 2.57 | 0.010 | 0.468 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 4.31 | 2.18 | 1.97 | 0.048 | 0.924 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 5.20 | 2.31 | 2.25 | 0.024 | 0.735 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 6.89 | 2.18 | 3.16 | 0.002 | 0.110 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 4.40 | 2.27 | 1.94 | 0.053 | 0.933 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 2.52 | 2.57 | 0.98 | 0.327 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 4.58 | 2.57 | 1.78 | 0.074 | 0.975 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | 3.24 | 2.57 | 1.26 | 0.207 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 4.13 | 2.66 | 1.55 | 0.120 | 0.997 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 5.82 | 2.58 | 2.26 | 0.024 | 0.735 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 3.34 | 2.64 | 1.26 | 0.206 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 2.06 | 2.19 | 0.94 | 0.347 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 0.72 | 2.18 | 0.33 | 0.740 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 1.61 | 2.30 | 0.70 | 0.483 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 3.30 | 2.18 | 1.51 | 0.130 | 0.998 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 0.82 | 2.27 | 0.36 | 0.719 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -1.34 | 2.20 | -0.61 | 0.543 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -0.45 | 2.30 | -0.19 | 0.846 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | 1.24 | 2.21 | 0.56 | 0.573 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | -1.24 | 2.27 | -0.55 | 0.583 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 0.89 | 2.30 | 0.39 | 0.699 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 2.58 | 2.18 | 1.18 | 0.237 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 0.09 | 2.27 | 0.04 | 0.967 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 1.69 | 2.31 | 0.73 | 0.465 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | -0.80 | 2.37 | -0.34 | 0.736 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -2.49 | 2.27 | -1.09 | 0.274 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.240, η²_G = 0.080
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | -1.21 | 8 | = 0.703 | -0.25 [-0.79, 0.08] | small | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | 0.13 | 8 | = 0.973 | 0.04 [-0.08, 0.79] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | -1.98 | 8 | = 0.608 | -0.49 [-0.85, 0.03] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | -1.05 | 8 | = 0.703 | -0.29 [-0.73, 0.22] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -0.70 | 8 | = 0.792 | -0.25 [-0.55, 0.30] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | -1.11 | 8 | = 0.703 | -0.30 [-0.77, 0.39] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 0.00 | 8 | = 1.000 | 0.00 [-0.22, 0.64] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | 0.13 | 8 | = 0.973 | 0.04 [0.00, 0.89] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | 1.17 | 8 | = 0.703 | 0.21 [0.01, 0.90] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | -0.31 | 8 | = 0.931 | -0.13 [-0.11, 0.85] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | 1.41 | 8 | = 0.703 | 0.25 [0.13, 1.04] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | 1.14 | 8 | = 0.703 | 0.52 [-0.18, 0.75] | medium | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | 0.80 | 8 | = 0.755 | 0.31 [0.06, 0.95] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -0.83 | 8 | = 0.755 | -0.24 [-0.53, 0.31] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | -0.22 | 8 | = 0.973 | -0.04 [-0.47, 0.47] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | 0.00 | 8 | = 1.000 | 0.00 [-0.32, 0.53] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | -0.14 | 8 | = 0.973 | -0.05 [-0.50, 0.66] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 1.07 | 8 | = 0.703 | 0.27 [0.00, 0.89] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | 1.02 | 8 | = 0.708 | 0.29 [0.23, 1.18] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 1.54 | 8 | = 0.703 | 0.49 [0.10, 1.00] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 0.29 | 8 | = 0.931 | 0.15 [0.06, 1.07] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | 2.07 | 8 | = 0.608 | 0.54 [0.25, 1.19] | medium | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | 2.09 | 8 | = 0.608 | 0.83 [0.03, 1.00] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | -1.39 | 8 | = 0.703 | -0.59 [-1.10, -0.17] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | -1.06 | 8 | = 0.703 | -0.36 [-0.90, 0.07] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | -0.77 | 8 | = 0.763 | -0.32 [-0.79, 0.08] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | -1.08 | 8 | = 0.703 | -0.38 [-0.91, 0.28] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | -0.16 | 8 | = 0.973 | -0.04 [-0.48, 0.36] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 0.00 | 8 | = 1.000 | 0.00 [-0.29, 0.55] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 0.51 | 8 | = 0.852 | 0.18 [-0.42, 0.42] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.46 | 8 | = 0.852 | -0.20 [-0.31, 0.63] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 0.81 | 8 | = 0.755 | 0.23 [-0.17, 0.69] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 1.26 | 8 | = 0.703 | 0.52 [-0.46, 0.46] | medium | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 0.49 | 8 | = 0.852 | 0.20 [-0.37, 0.57] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | 0.96 | 8 | = 0.752 | 0.25 [-0.20, 0.65] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 0.47 | 8 | = 0.852 | 0.21 [-0.23, 0.96] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 1.37 | 8 | = 0.703 | 0.53 [0.03, 0.92] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | 1.84 | 8 | = 0.608 | 0.53 [0.29, 1.25] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 2.69 | 8 | = 0.608 | 0.78 [0.24, 1.19] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | 0.87 | 8 | = 0.755 | 0.43 [0.16, 1.20] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | 2.98 | 8 | = 0.608 | 0.83 [0.37, 1.36] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | 2.21 | 8 | = 0.608 | 1.17 [-0.03, 0.93] | large | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | 0.10 | 8 | = 0.973 | 0.05 [-0.31, 0.63] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | 0.00 | 8 | = 1.000 | 0.00 [-0.26, 1.07] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 1.31 | 8 | = 0.703 | 0.31 [-0.00, 0.99] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | 0.88 | 8 | = 0.755 | 0.33 [0.07, 1.09] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | 1.63 | 8 | = 0.688 | 0.54 [0.10, 1.12] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | 0.43 | 8 | = 0.871 | 0.20 [-0.04, 1.01] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | 1.80 | 8 | = 0.608 | 0.59 [0.28, 1.36] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | 2.42 | 8 | = 0.608 | 0.89 [0.01, 1.12] | large | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | -0.11 | 8 | = 0.973 | -0.05 [-0.48, 0.68] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 0.83 | 8 | = 0.755 | 0.27 [-0.09, 0.78] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | 0.76 | 8 | = 0.763 | 0.29 [0.08, 0.98] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | 1.23 | 8 | = 0.703 | 0.50 [-0.02, 0.87] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 0.30 | 8 | = 0.931 | 0.15 [-0.15, 0.81] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | 1.94 | 8 | = 0.608 | 0.55 [0.22, 1.17] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | 1.81 | 8 | = 0.608 | 0.85 [-0.11, 0.83] | large | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 1.05 | 8 | = 0.703 | 0.33 [-0.45, 0.71] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | 0.86 | 8 | = 0.755 | 0.34 [-0.29, 0.89] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | 2.22 | 8 | = 0.608 | 0.56 [-0.22, 0.97] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | 0.63 | 8 | = 0.824 | 0.21 [-0.30, 1.01] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | 2.23 | 8 | = 0.608 | 0.61 [-0.18, 1.03] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | 2.38 | 8 | = 0.608 | 0.93 [-0.05, 1.35] | large | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | 0.10 | 8 | = 0.973 | 0.04 [-0.22, 0.63] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | 0.57 | 8 | = 0.843 | 0.22 [-0.36, 0.49] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | -0.31 | 8 | = 0.931 | -0.15 [-0.37, 0.57] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | 1.21 | 8 | = 0.703 | 0.27 [0.04, 0.93] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | 1.75 | 8 | = 0.619 | 0.56 [-0.41, 0.50] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 0.55 | 8 | = 0.843 | 0.16 [-0.59, 0.26] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.48 | 8 | = 0.852 | -0.18 [-0.45, 0.49] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | 0.69 | 8 | = 0.792 | 0.21 [-0.34, 0.50] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | 0.84 | 8 | = 0.755 | 0.47 [-0.47, 0.44] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -1.18 | 8 | = 0.703 | -0.39 [-0.38, 0.55] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | 0.18 | 8 | = 0.973 | 0.04 [-0.12, 0.75] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | 0.61 | 8 | = 0.824 | 0.33 [-0.47, 0.44] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | 1.15 | 8 | = 0.703 | 0.44 [-0.29, 0.66] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | 1.35 | 8 | = 0.703 | 0.76 [-0.47, 0.53] | medium | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.62 | 8 | = 0.824 | 0.28 [-0.67, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1289.04, BIC = 1347.81
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = -0.12, *SE* = 0.562, *z* = -0.217, *p* = 0.828
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = 0.34, *SE* = 0.563, *z* = 0.605, *p* = 0.545
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 0.30, *SE* = 0.560, *z* = 0.536, *p* = 0.592
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 0.67, *SE* = 0.605, *z* = 1.109, *p* = 0.267
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 0.73, *SE* = 0.562, *z* = 1.291, *p* = 0.197
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 1.13, *SE* = 0.668, *z* = 1.697, *p* = 0.090
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 0.13, *SE* = 0.564, *z* = 0.230, *p* = 0.818
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 0.05, *SE* = 0.575, *z* = 0.090, *p* = 0.928
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -0.11, *SE* = 0.563, *z* = -0.189, *p* = 0.850
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = 0.31, *SE* = 0.599, *z* = 0.510, *p* = 0.610
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = 0.17, *SE* = 0.561, *z* = 0.305, *p* = 0.760
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = 0.41, *SE* = 0.589, *z* = 0.701, *p* = 0.483
- **SNR**: *β* = 0.06, *SE* = 0.057, *z* = 1.088, *p* = 0.277

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | 0.12 | 0.56 | 0.22 | 0.828 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | -0.34 | 0.56 | -0.60 | 0.545 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | -0.30 | 0.56 | -0.54 | 0.592 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -0.67 | 0.60 | -1.11 | 0.267 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | -0.73 | 0.56 | -1.29 | 0.197 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -1.13 | 0.67 | -1.70 | 0.090 | 0.999 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | -0.13 | 0.56 | -0.23 | 0.818 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -0.05 | 0.57 | -0.09 | 0.928 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 0.11 | 0.56 | 0.19 | 0.850 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | -0.31 | 0.60 | -0.51 | 0.610 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | -0.17 | 0.56 | -0.31 | 0.760 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | -0.41 | 0.59 | -0.70 | 0.483 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | -0.46 | 0.56 | -0.83 | 0.408 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | -0.42 | 0.56 | -0.75 | 0.451 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -0.79 | 0.59 | -1.33 | 0.182 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | -0.85 | 0.56 | -1.52 | 0.129 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | -1.25 | 0.66 | -1.90 | 0.057 | 0.990 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | -0.25 | 0.56 | -0.45 | 0.653 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | -0.17 | 0.56 | -0.31 | 0.758 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | -0.02 | 0.56 | -0.03 | 0.978 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | -0.43 | 0.59 | -0.72 | 0.469 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | -0.29 | 0.56 | -0.52 | 0.600 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | -0.54 | 0.58 | -0.92 | 0.358 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | 0.04 | 0.56 | 0.07 | 0.942 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -0.33 | 0.59 | -0.56 | 0.578 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -0.39 | 0.56 | -0.69 | 0.491 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -0.79 | 0.66 | -1.20 | 0.230 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 0.21 | 0.56 | 0.38 | 0.706 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 0.29 | 0.56 | 0.51 | 0.608 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 0.45 | 0.56 | 0.80 | 0.424 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.03 | 0.59 | 0.06 | 0.953 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 0.17 | 0.56 | 0.30 | 0.762 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | -0.07 | 0.58 | -0.13 | 0.900 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | -0.37 | 0.60 | -0.62 | 0.535 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | -0.43 | 0.56 | -0.76 | 0.447 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | -0.83 | 0.66 | -1.26 | 0.209 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 0.17 | 0.56 | 0.30 | 0.761 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 0.25 | 0.57 | 0.44 | 0.662 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 0.41 | 0.56 | 0.73 | 0.468 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | -0.01 | 0.59 | -0.01 | 0.992 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 0.13 | 0.56 | 0.23 | 0.818 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | -0.11 | 0.58 | -0.19 | 0.846 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -0.06 | 0.59 | -0.09 | 0.926 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | -0.46 | 0.68 | -0.68 | 0.499 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 0.54 | 0.59 | 0.91 | 0.361 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 0.62 | 0.59 | 1.05 | 0.293 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 0.78 | 0.59 | 1.31 | 0.190 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 0.36 | 0.62 | 0.59 | 0.554 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 0.50 | 0.60 | 0.84 | 0.402 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 0.26 | 0.61 | 0.42 | 0.673 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -0.41 | 0.66 | -0.62 | 0.538 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 0.60 | 0.56 | 1.07 | 0.287 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 0.67 | 0.56 | 1.19 | 0.232 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 0.83 | 0.56 | 1.49 | 0.137 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 0.42 | 0.59 | 0.71 | 0.477 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 0.55 | 0.56 | 0.99 | 0.321 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 0.31 | 0.58 | 0.54 | 0.591 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 1.00 | 0.66 | 1.52 | 0.128 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 1.08 | 0.66 | 1.64 | 0.101 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | 1.24 | 0.66 | 1.88 | 0.060 | 0.992 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 0.83 | 0.68 | 1.21 | 0.226 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 0.96 | 0.66 | 1.45 | 0.146 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 0.72 | 0.68 | 1.06 | 0.287 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 0.08 | 0.56 | 0.14 | 0.890 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 0.24 | 0.56 | 0.42 | 0.673 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -0.18 | 0.59 | -0.30 | 0.766 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | -0.04 | 0.56 | -0.07 | 0.941 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | -0.28 | 0.58 | -0.49 | 0.625 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | 0.16 | 0.56 | 0.28 | 0.779 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -0.25 | 0.59 | -0.43 | 0.666 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -0.12 | 0.57 | -0.21 | 0.833 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | -0.36 | 0.58 | -0.62 | 0.534 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -0.41 | 0.59 | -0.70 | 0.485 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | -0.28 | 0.56 | -0.50 | 0.620 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | -0.52 | 0.58 | -0.89 | 0.371 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 0.13 | 0.59 | 0.23 | 0.820 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | -0.11 | 0.61 | -0.18 | 0.859 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -0.24 | 0.58 | -0.42 | 0.678 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.47, *p* = 0.925, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | 0.36 | 8 | = 0.992 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | -0.44 | 8 | = 0.992 | -0.18 [-0.54, 0.31] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | -0.94 | 8 | = 0.969 | -0.21 [-0.63, 0.22] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | -0.93 | 8 | = 0.969 | -0.28 [-0.60, 0.34] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -0.63 | 8 | = 0.992 | -0.16 [-0.85, 0.03] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | 0.19 | 8 | = 0.992 | 0.10 [-0.77, 0.39] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 1.38 | 8 | = 0.969 | 0.40 [-0.45, 0.39] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | 0.30 | 8 | = 0.992 | 0.12 [-0.37, 0.47] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | 0.61 | 8 | = 0.992 | 0.22 [-0.29, 0.55] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | 0.53 | 8 | = 0.992 | 0.25 [-0.51, 0.43] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | 0.59 | 8 | = 0.992 | 0.18 [-0.50, 0.34] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | -0.76 | 8 | = 0.992 | -0.23 [-0.60, 0.32] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | -0.92 | 8 | = 0.969 | -0.31 [-0.67, 0.19] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -1.24 | 8 | = 0.969 | -0.38 [-0.75, 0.11] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | -0.93 | 8 | = 0.969 | -0.39 [-0.69, 0.26] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | -1.19 | 8 | = 0.969 | -0.32 [-1.07, -0.15] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 0.06 | 8 | = 0.992 | 0.03 [-0.82, 0.35] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 1.09 | 8 | = 0.969 | 0.28 [-0.57, 0.28] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -0.09 | 8 | = 0.992 | -0.02 [-0.47, 0.37] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 0.45 | 8 | = 0.992 | 0.08 [-0.43, 0.41] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 0.19 | 8 | = 0.992 | 0.10 [-0.65, 0.29] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | 0.15 | 8 | = 0.992 | 0.05 [-0.65, 0.21] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | -0.86 | 8 | = 0.974 | -0.32 [-0.63, 0.29] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | 0.04 | 8 | = 0.992 | 0.02 [-0.42, 0.43] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | -0.27 | 8 | = 0.992 | -0.11 [-0.49, 0.44] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | 0.18 | 8 | = 0.992 | 0.05 [-0.68, 0.18] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | 0.51 | 8 | = 0.992 | 0.22 [-0.67, 0.49] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 1.75 | 8 | = 0.969 | 0.58 [-0.33, 0.51] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 1.32 | 8 | = 0.969 | 0.32 [-0.29, 0.56] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 1.30 | 8 | = 0.969 | 0.41 [-0.19, 0.67] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | 0.80 | 8 | = 0.974 | 0.47 [-0.52, 0.42] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 1.43 | 8 | = 0.969 | 0.38 [-0.35, 0.50] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | -0.27 | 8 | = 0.992 | -0.10 [-0.50, 0.41] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | -0.45 | 8 | = 0.992 | -0.15 [-0.57, 0.37] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | 0.15 | 8 | = 0.992 | 0.04 [-0.68, 0.17] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 0.43 | 8 | = 0.992 | 0.23 [-0.73, 0.43] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 2.77 | 8 | = 0.633 | 0.77 [-0.31, 0.54] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | 0.99 | 8 | = 0.969 | 0.42 [-0.24, 0.61] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 1.71 | 8 | = 0.969 | 0.55 [-0.11, 0.75] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | 1.55 | 8 | = 0.969 | 0.69 [-0.45, 0.49] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | 1.51 | 8 | = 0.969 | 0.49 [-0.34, 0.50] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | -0.33 | 8 | = 0.992 | -0.13 [-0.44, 0.47] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | 0.50 | 8 | = 0.992 | 0.17 [-0.50, 0.44] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | 0.52 | 8 | = 0.992 | 0.28 [-0.49, 0.79] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 2.00 | 8 | = 0.969 | 0.62 [-0.34, 0.60] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | 0.87 | 8 | = 0.974 | 0.40 [-0.20, 0.75] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | 1.07 | 8 | = 0.969 | 0.48 [-0.24, 0.71] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | 1.05 | 8 | = 0.969 | 0.52 [-0.43, 0.57] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | 1.38 | 8 | = 0.969 | 0.45 [-0.31, 0.63] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.04 | 8 | = 0.992 | -0.01 [-0.57, 0.46] | negligible | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.41 | 8 | = 0.992 | 0.20 [-0.65, 0.51] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 3.09 | 8 | = 0.633 | 0.66 [-0.10, 0.77] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | 1.23 | 8 | = 0.969 | 0.34 [-0.05, 0.82] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | 2.20 | 8 | = 0.969 | 0.46 [0.17, 1.09] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 1.03 | 8 | = 0.969 | 0.55 [-0.39, 0.55] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | 3.00 | 8 | = 0.633 | 0.41 [-0.08, 0.79] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | -0.44 | 8 | = 0.992 | -0.14 [-0.33, 0.58] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 0.25 | 8 | = 0.992 | 0.12 [-0.35, 0.82] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | -0.10 | 8 | = 0.992 | -0.04 [-0.40, 0.77] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | 0.03 | 8 | = 0.992 | 0.01 [-0.34, 0.83] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | 0.04 | 8 | = 0.992 | 0.02 [-0.40, 0.89] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -0.01 | 8 | = 0.995 | -0.00 [-0.38, 0.79] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | -0.44 | 8 | = 0.992 | -0.26 [-0.61, 0.66] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -1.11 | 8 | = 0.969 | -0.33 [-0.34, 0.51] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | -0.72 | 8 | = 0.992 | -0.23 [-0.28, 0.56] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | -0.44 | 8 | = 0.992 | -0.25 [-0.49, 0.45] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -1.21 | 8 | = 0.969 | -0.25 [-0.47, 0.37] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | -1.52 | 8 | = 0.969 | -0.49 [-0.57, 0.35] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 0.45 | 8 | = 0.992 | 0.12 [-0.37, 0.47] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | 0.24 | 8 | = 0.992 | 0.15 [-0.49, 0.45] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | 0.23 | 8 | = 0.992 | 0.08 [-0.54, 0.31] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | -0.81 | 8 | = 0.974 | -0.32 [-0.59, 0.33] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 0.03 | 8 | = 0.992 | 0.01 [-0.64, 0.31] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | -0.13 | 8 | = 0.992 | -0.04 [-0.67, 0.19] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | -1.01 | 8 | = 0.969 | -0.38 [-0.61, 0.30] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | -0.10 | 8 | = 0.992 | -0.05 [-0.43, 0.51] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.80 | 8 | = 0.974 | -0.40 [-0.47, 0.52] | small | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | -0.99 | 8 | = 0.969 | -0.35 [-0.51, 0.41] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 2870.77, BIC = 2929.54
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 22.70, *SE* = 8.872, *z* = 2.559, *p* = 0.010
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = 18.59, *SE* = 8.808, *z* = 2.111, *p* = 0.035
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 6.10, *SE* = 8.890, *z* = 0.686, *p* = 0.493
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 0.70, *SE* = 9.259, *z* = 0.076, *p* = 0.940
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 16.13, *SE* = 8.968, *z* = 1.799, *p* = 0.072
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 20.11, *SE* = 10.334, *z* = 1.947, *p* = 0.052
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 21.15, *SE* = 8.909, *z* = 2.374, *p* = 0.018
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 9.40, *SE* = 8.812, *z* = 1.066, *p* = 0.286
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = 21.61, *SE* = 8.956, *z* = 2.412, *p* = 0.016
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = 3.51, *SE* = 9.259, *z* = 0.380, *p* = 0.704
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = 13.76, *SE* = 8.810, *z* = 1.562, *p* = 0.118
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = 6.44, *SE* = 9.144, *z* = 0.704, *p* = 0.481
- **SNR**: *β* = -0.22, *SE* = 0.479, *z* = -0.452, *p* = 0.651

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -22.70 | 8.87 | -2.56 | 0.010 | 0.561 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | -18.59 | 8.81 | -2.11 | 0.035 | 0.922 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | -6.10 | 8.89 | -0.69 | 0.493 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -0.70 | 9.26 | -0.08 | 0.940 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | -16.13 | 8.97 | -1.80 | 0.072 | 0.992 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -20.11 | 10.33 | -1.95 | 0.052 | 0.975 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | -21.15 | 8.91 | -2.37 | 0.018 | 0.740 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -9.40 | 8.81 | -1.07 | 0.286 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | -21.60 | 8.96 | -2.41 | 0.016 | 0.708 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | -3.51 | 9.26 | -0.38 | 0.704 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | -13.76 | 8.81 | -1.56 | 0.118 | 0.999 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | -6.44 | 9.14 | -0.70 | 0.481 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 4.11 | 8.96 | 0.46 | 0.646 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 16.61 | 8.79 | 1.89 | 0.059 | 0.983 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | 22.00 | 9.40 | 2.34 | 0.019 | 0.767 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 6.57 | 8.81 | 0.75 | 0.456 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 2.59 | 10.47 | 0.25 | 0.805 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 1.55 | 8.80 | 0.18 | 0.860 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 13.31 | 8.97 | 1.48 | 0.138 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 1.10 | 8.81 | 0.12 | 0.901 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 19.19 | 9.40 | 2.04 | 0.041 | 0.949 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 8.95 | 8.81 | 1.01 | 0.310 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 16.27 | 9.31 | 1.75 | 0.081 | 0.995 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | 12.49 | 8.99 | 1.39 | 0.164 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | 17.89 | 9.24 | 1.94 | 0.053 | 0.977 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | 2.46 | 9.09 | 0.27 | 0.787 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -1.52 | 10.32 | -0.15 | 0.882 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | -2.56 | 9.01 | -0.28 | 0.776 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 9.19 | 8.79 | 1.05 | 0.296 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | -3.01 | 9.07 | -0.33 | 0.740 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 15.08 | 9.25 | 1.63 | 0.103 | 0.999 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 4.83 | 8.86 | 0.55 | 0.586 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 12.15 | 9.12 | 1.33 | 0.183 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 5.40 | 9.42 | 0.57 | 0.567 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | -10.04 | 8.80 | -1.14 | 0.254 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | -14.02 | 10.49 | -1.34 | 0.182 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | -15.05 | 8.79 | -1.71 | 0.087 | 0.996 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | -3.30 | 9.00 | -0.37 | 0.714 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | -15.51 | 8.80 | -1.76 | 0.078 | 0.994 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 2.58 | 9.42 | 0.27 | 0.784 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | -7.66 | 8.82 | -0.87 | 0.385 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | -0.34 | 9.34 | -0.04 | 0.971 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -15.43 | 9.52 | -1.62 | 0.105 | 0.999 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | -19.42 | 10.70 | -1.81 | 0.070 | 0.991 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | -20.45 | 9.45 | -2.16 | 0.030 | 0.895 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | -8.70 | 9.25 | -0.94 | 0.347 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | -20.91 | 9.51 | -2.20 | 0.028 | 0.877 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | -2.81 | 9.66 | -0.29 | 0.771 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | -13.06 | 9.31 | -1.40 | 0.161 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | -5.74 | 9.56 | -0.60 | 0.549 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -3.98 | 10.59 | -0.38 | 0.707 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | -5.02 | 8.80 | -0.57 | 0.568 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 6.73 | 9.10 | 0.74 | 0.459 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | -5.47 | 8.79 | -0.62 | 0.534 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 12.62 | 9.52 | 1.33 | 0.185 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 2.37 | 8.87 | 0.27 | 0.789 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 9.70 | 9.44 | 1.03 | 0.304 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -1.04 | 10.52 | -0.10 | 0.922 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 10.72 | 10.32 | 1.04 | 0.299 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -1.49 | 10.57 | -0.14 | 0.888 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 16.60 | 10.70 | 1.55 | 0.121 | 0.999 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 6.36 | 10.38 | 0.61 | 0.540 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 13.68 | 10.60 | 1.29 | 0.197 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 11.75 | 9.02 | 1.30 | 0.193 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | -0.45 | 8.80 | -0.05 | 0.959 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 17.64 | 9.44 | 1.87 | 0.062 | 0.985 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 7.39 | 8.83 | 0.84 | 0.403 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 14.71 | 9.36 | 1.57 | 0.116 | 0.999 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -12.21 | 9.09 | -1.34 | 0.179 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | 5.88 | 9.25 | 0.64 | 0.525 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -4.36 | 8.87 | -0.49 | 0.623 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 2.96 | 9.12 | 0.32 | 0.745 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 18.09 | 9.50 | 1.90 | 0.057 | 0.981 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 7.85 | 8.87 | 0.89 | 0.376 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 15.17 | 9.43 | 1.61 | 0.108 | 0.999 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | -10.24 | 9.31 | -1.10 | 0.271 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | -2.92 | 9.55 | -0.31 | 0.760 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 7.32 | 9.20 | 0.80 | 0.426 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.80, *p* = 0.649, η²_G = 0.078
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | -2.11 | 8 | = 0.812 | -0.85 [-1.16, -0.22] | large | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | -1.88 | 8 | = 0.812 | -0.73 [-0.94, -0.04] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | -0.64 | 8 | = 0.987 | -0.32 [-0.59, 0.26] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | -0.43 | 8 | = 0.987 | -0.15 [-0.50, 0.44] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -2.68 | 8 | = 0.803 | -0.92 [-0.88, 0.00] | large | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | -1.93 | 8 | = 0.812 | -0.60 [-1.47, -0.14] | medium | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | -1.12 | 8 | = 0.957 | -0.55 [-0.91, -0.02] | medium | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | -1.17 | 8 | = 0.936 | -0.58 [-0.65, 0.20] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | -2.62 | 8 | = 0.803 | -1.16 [-0.97, -0.07] | large | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | -1.24 | 8 | = 0.936 | -0.59 [-0.51, 0.42] | medium | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | -2.98 | 8 | = 0.803 | -0.86 [-0.80, 0.07] | large | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | -1.24 | 8 | = 0.936 | -0.72 [-0.59, 0.33] | medium | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | 0.05 | 8 | = 0.987 | 0.03 [-0.35, 0.49] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | 1.69 | 8 | = 0.913 | 0.68 [0.10, 1.01] | medium | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | 1.09 | 8 | = 0.962 | 0.63 [-0.09, 0.88] | medium | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | -0.12 | 8 | = 0.987 | -0.04 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 0.23 | 8 | = 0.987 | 0.08 [-0.60, 0.56] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 0.40 | 8 | = 0.987 | 0.15 [-0.38, 0.47] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | 0.37 | 8 | = 0.987 | 0.19 [-0.17, 0.68] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | -0.81 | 8 | = 0.987 | -0.29 [-0.38, 0.46] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 0.48 | 8 | = 0.987 | 0.19 [-0.05, 0.93] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | -0.26 | 8 | = 0.987 | -0.09 [-0.20, 0.65] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | 0.16 | 8 | = 0.987 | 0.08 [-0.06, 0.89] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | 1.25 | 8 | = 0.936 | 0.56 [-0.16, 0.70] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | 1.21 | 8 | = 0.936 | 0.55 [-0.19, 0.76] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | -0.12 | 8 | = 0.987 | -0.07 [-0.36, 0.49] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | 0.11 | 8 | = 0.987 | 0.06 [-0.72, 0.44] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 0.27 | 8 | = 0.987 | 0.12 [-0.46, 0.39] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 0.56 | 8 | = 0.987 | 0.15 [-0.24, 0.62] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | -0.52 | 8 | = 0.987 | -0.29 [-0.46, 0.38] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | 0.33 | 8 | = 0.987 | 0.15 [-0.16, 0.80] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | -0.20 | 8 | = 0.987 | -0.11 [-0.33, 0.52] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 0.12 | 8 | = 0.987 | 0.05 [-0.21, 0.71] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 0.20 | 8 | = 0.987 | 0.10 [-0.42, 0.52] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | -1.53 | 8 | = 0.936 | -0.76 [-0.72, 0.14] | medium | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | -0.97 | 8 | = 0.987 | -0.42 [-0.91, 0.27] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | -0.83 | 8 | = 0.987 | -0.37 [-0.84, 0.04] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | -0.88 | 8 | = 0.987 | -0.38 [-0.51, 0.34] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | -2.36 | 8 | = 0.812 | -1.03 [-0.83, 0.04] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | -0.98 | 8 | = 0.987 | -0.40 [-0.36, 0.58] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | -1.48 | 8 | = 0.936 | -0.70 [-0.64, 0.22] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | -1.22 | 8 | = 0.936 | -0.54 [-0.52, 0.39] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | -1.89 | 8 | = 0.812 | -0.69 [-0.99, 0.00] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | -1.24 | 8 | = 0.936 | -0.44 [-0.88, 0.41] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | -0.67 | 8 | = 0.987 | -0.39 [-0.78, 0.17] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | -0.78 | 8 | = 0.987 | -0.40 [-0.74, 0.21] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | -2.07 | 8 | = 0.812 | -0.91 [-0.98, 0.01] | large | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | -0.83 | 8 | = 0.987 | -0.41 [-0.52, 0.47] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | -1.83 | 8 | = 0.812 | -0.67 [-0.89, 0.08] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.89 | 8 | = 0.987 | -0.52 [-0.73, 0.31] | medium | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.41 | 8 | = 0.987 | 0.12 [-0.58, 0.58] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 0.44 | 8 | = 0.987 | 0.19 [-0.55, 0.30] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | 0.39 | 8 | = 0.987 | 0.23 [-0.31, 0.53] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | -1.17 | 8 | = 0.936 | -0.25 [-0.64, 0.21] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 0.63 | 8 | = 0.987 | 0.24 [-0.08, 0.89] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | -0.28 | 8 | = 0.987 | -0.05 [-0.34, 0.51] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | 0.23 | 8 | = 0.987 | 0.13 [-0.28, 0.63] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 0.10 | 8 | = 0.987 | 0.05 [-0.45, 0.71] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | 0.15 | 8 | = 0.987 | 0.08 [-0.37, 0.80] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | -0.82 | 8 | = 0.987 | -0.32 [-0.61, 0.54] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | 0.17 | 8 | = 0.987 | 0.08 [-0.48, 0.80] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -0.56 | 8 | = 0.987 | -0.16 [-0.64, 0.51] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | -0.02 | 8 | = 0.998 | -0.01 [-0.50, 0.78] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | 0.06 | 8 | = 0.987 | 0.02 [-0.24, 0.61] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | -1.17 | 8 | = 0.936 | -0.40 [-0.43, 0.41] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | 0.07 | 8 | = 0.987 | 0.02 [-0.10, 0.88] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -0.48 | 8 | = 0.987 | -0.22 [-0.28, 0.57] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | -0.23 | 8 | = 0.987 | -0.07 [-0.18, 0.75] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | -0.85 | 8 | = 0.987 | -0.46 [-0.67, 0.18] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | 0.00 | 8 | = 1.000 | 0.00 [-0.35, 0.59] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | -0.44 | 8 | = 0.987 | -0.26 [-0.50, 0.35] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | -0.24 | 8 | = 0.987 | -0.10 [-0.36, 0.56] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 1.37 | 8 | = 0.936 | 0.47 [0.01, 1.01] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | 0.64 | 8 | = 0.987 | 0.17 [-0.19, 0.66] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | 0.71 | 8 | = 0.987 | 0.36 [-0.05, 0.90] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | -0.58 | 8 | = 0.987 | -0.27 [-0.80, 0.16] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.28 | 8 | = 0.987 | -0.11 [-0.45, 0.54] | negligible | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.29 | 8 | = 0.987 | 0.17 [-0.33, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1373.16, BIC = 1431.94
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 2.51, *SE* = 0.626, *z* = 4.003, *p* < .001
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = 0.92, *SE* = 0.621, *z* = 1.484, *p* = 0.138
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 2.14, *SE* = 0.628, *z* = 3.413, *p* = 0.001
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 3.41, *SE* = 0.653, *z* = 5.226, *p* < .001
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 2.52, *SE* = 0.634, *z* = 3.984, *p* < .001
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 1.89, *SE* = 0.731, *z* = 2.590, *p* = 0.010
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 1.30, *SE* = 0.629, *z* = 2.061, *p* = 0.039
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 0.36, *SE* = 0.621, *z* = 0.586, *p* = 0.558
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = 2.19, *SE* = 0.633, *z* = 3.460, *p* = 0.001
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = 2.66, *SE* = 0.653, *z* = 4.074, *p* < .001
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = 2.57, *SE* = 0.621, *z* = 4.140, *p* < .001
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = 3.06, *SE* = 0.646, *z* = 4.739, *p* < .001
- **SNR**: *β* = 0.18, *SE* = 0.036, *z* = 5.128, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -2.51 | 0.63 | -4.00 | < .001 | 0.004 | ** |
| Cardinality (no change) - Decrease by 1 (Incorrect) | -0.92 | 0.62 | -1.48 | 0.138 | 0.998 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | -2.14 | 0.63 | -3.41 | < .001 | 0.041 | * |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -3.41 | 0.65 | -5.23 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 3 (Correct) | -2.52 | 0.63 | -3.98 | < .001 | 0.005 | ** |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -1.89 | 0.73 | -2.59 | 0.010 | 0.417 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | -1.30 | 0.63 | -2.06 | 0.039 | 0.876 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -0.36 | 0.62 | -0.59 | 0.558 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | -2.19 | 0.63 | -3.46 | < .001 | 0.036 | * |
| Cardinality (no change) - Increase by 2 (Incorrect) | -2.66 | 0.65 | -4.07 | < .001 | 0.003 | ** |
| Cardinality (no change) - Increase by 3 (Correct) | -2.57 | 0.62 | -4.14 | < .001 | 0.003 | ** |
| Cardinality (no change) - Increase by 3 (Incorrect) | -3.06 | 0.65 | -4.74 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 1.58 | 0.63 | 2.50 | 0.012 | 0.494 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 0.36 | 0.62 | 0.59 | 0.557 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -0.91 | 0.66 | -1.37 | 0.171 | 0.999 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | -0.02 | 0.62 | -0.03 | 0.977 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 0.61 | 0.74 | 0.83 | 0.408 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 1.21 | 0.62 | 1.95 | 0.051 | 0.910 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 2.14 | 0.63 | 3.38 | < .001 | 0.046 | * |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 0.32 | 0.62 | 0.51 | 0.610 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | -0.16 | 0.66 | -0.23 | 0.814 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | -0.07 | 0.62 | -0.11 | 0.916 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | -0.55 | 0.66 | -0.84 | 0.401 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -1.22 | 0.64 | -1.92 | 0.055 | 0.920 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -2.49 | 0.65 | -3.82 | < .001 | 0.009 | ** |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -1.60 | 0.64 | -2.49 | 0.013 | 0.499 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -0.97 | 0.73 | -1.33 | 0.183 | 0.999 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | -0.37 | 0.64 | -0.59 | 0.557 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 0.56 | 0.62 | 0.90 | 0.368 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | -1.27 | 0.64 | -1.97 | 0.048 | 0.904 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | -1.74 | 0.65 | -2.67 | 0.008 | 0.365 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | -1.65 | 0.63 | -2.64 | 0.008 | 0.379 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | -2.14 | 0.64 | -3.32 | < .001 | 0.055 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | -1.27 | 0.67 | -1.91 | 0.056 | 0.920 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | -0.38 | 0.62 | -0.62 | 0.538 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 0.25 | 0.74 | 0.33 | 0.738 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 0.85 | 0.62 | 1.36 | 0.172 | 0.999 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 1.78 | 0.64 | 2.80 | 0.005 | 0.268 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | -0.05 | 0.62 | -0.08 | 0.939 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | -0.52 | 0.67 | -0.78 | 0.435 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | -0.43 | 0.62 | -0.69 | 0.490 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | -0.92 | 0.66 | -1.39 | 0.165 | 0.999 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 0.89 | 0.67 | 1.32 | 0.186 | 0.999 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 1.52 | 0.76 | 2.01 | 0.045 | 0.893 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 2.12 | 0.67 | 3.17 | 0.001 | 0.089 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 3.05 | 0.65 | 4.67 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 1.22 | 0.67 | 1.82 | 0.068 | 0.952 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 0.75 | 0.68 | 1.10 | 0.270 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 0.84 | 0.66 | 1.28 | 0.199 | 0.999 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 0.35 | 0.68 | 0.52 | 0.600 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 0.63 | 0.75 | 0.84 | 0.400 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 1.23 | 0.62 | 1.98 | 0.048 | 0.904 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 2.16 | 0.64 | 3.35 | < .001 | 0.050 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 0.33 | 0.62 | 0.54 | 0.589 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | -0.14 | 0.67 | -0.20 | 0.838 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | -0.05 | 0.63 | -0.08 | 0.940 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | -0.54 | 0.67 | -0.80 | 0.424 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 0.60 | 0.74 | 0.80 | 0.423 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 1.53 | 0.73 | 2.09 | 0.036 | 0.858 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -0.30 | 0.75 | -0.40 | 0.692 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -0.77 | 0.76 | -1.02 | 0.310 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | -0.68 | 0.73 | -0.92 | 0.356 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | -1.17 | 0.75 | -1.55 | 0.120 | 0.995 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 0.93 | 0.64 | 1.46 | 0.144 | 0.998 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | -0.89 | 0.62 | -1.44 | 0.150 | 0.998 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -1.37 | 0.67 | -2.05 | 0.041 | 0.880 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | -1.28 | 0.62 | -2.05 | 0.041 | 0.880 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | -1.76 | 0.66 | -2.66 | 0.008 | 0.367 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -1.83 | 0.64 | -2.84 | 0.005 | 0.242 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -2.30 | 0.65 | -3.52 | < .001 | 0.029 | * |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -2.21 | 0.63 | -3.53 | < .001 | 0.029 | * |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | -2.70 | 0.64 | -4.19 | < .001 | 0.002 | ** |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -0.47 | 0.67 | -0.70 | 0.482 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | -0.38 | 0.63 | -0.61 | 0.541 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | -0.87 | 0.67 | -1.30 | 0.193 | 0.999 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 0.09 | 0.66 | 0.14 | 0.890 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | -0.40 | 0.67 | -0.59 | 0.556 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -0.49 | 0.65 | -0.75 | 0.453 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.41, *p* = 0.177, η²_G = 0.062
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | -3.26 | 8 | = 0.128 | -0.85 [-1.83, -0.69] | large | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | -1.48 | 8 | = 0.573 | -0.44 [-0.76, 0.11] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | -3.06 | 8 | = 0.153 | -0.87 [-1.84, -0.70] | large | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | -1.02 | 8 | = 0.803 | -0.29 [-1.10, -0.09] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -3.35 | 8 | = 0.128 | -1.03 [-1.57, -0.52] | large | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | -1.54 | 8 | = 0.552 | -0.56 [-0.98, 0.22] | medium | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | -0.64 | 8 | = 0.934 | -0.15 [-1.15, -0.21] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | -0.50 | 8 | = 0.934 | -0.14 [-0.49, 0.36] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | -3.38 | 8 | = 0.128 | -0.68 [-1.71, -0.62] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | -3.52 | 8 | = 0.128 | -0.69 [-1.39, -0.30] | medium | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | -3.69 | 8 | = 0.128 | -0.98 [-1.65, -0.58] | large | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | -2.33 | 8 | = 0.237 | -0.71 [-1.42, -0.34] | medium | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | 0.86 | 8 | = 0.878 | 0.25 [0.34, 1.31] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -0.19 | 8 | = 0.934 | -0.05 [-0.22, 0.64] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | 0.30 | 8 | = 0.934 | 0.12 [-0.57, 0.37] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | -1.04 | 8 | = 0.797 | -0.23 [-0.57, 0.28] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 0.15 | 8 | = 0.934 | 0.06 [-0.34, 0.84] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 2.84 | 8 | = 0.154 | 0.68 [0.34, 1.32] | medium | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | 1.90 | 8 | = 0.355 | 0.62 [0.46, 1.48] | medium | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 0.01 | 8 | = 0.995 | 0.00 [-0.34, 0.51] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | -0.40 | 8 | = 0.934 | -0.12 [-0.34, 0.60] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | -0.40 | 8 | = 0.934 | -0.10 [-0.28, 0.56] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | -0.55 | 8 | = 0.934 | -0.18 [-0.40, 0.52] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | -0.99 | 8 | = 0.806 | -0.28 [-1.24, -0.28] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | -0.07 | 8 | = 0.980 | -0.02 [-0.89, 0.08] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | -1.31 | 8 | = 0.707 | -0.41 [-1.18, -0.23] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | -0.47 | 8 | = 0.934 | -0.14 [-0.71, 0.45] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 1.08 | 8 | = 0.796 | 0.30 [-0.79, 0.08] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 1.27 | 8 | = 0.721 | 0.29 [-0.13, 0.74] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | -0.88 | 8 | = 0.878 | -0.21 [-1.24, -0.28] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | -1.13 | 8 | = 0.796 | -0.28 [-1.01, -0.01] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | -1.10 | 8 | = 0.796 | -0.33 [-1.18, -0.23] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | -1.07 | 8 | = 0.796 | -0.33 [-1.03, -0.06] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 0.37 | 8 | = 0.934 | 0.14 [-0.61, 0.33] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | -0.51 | 8 | = 0.934 | -0.17 [-0.72, 0.14] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 0.29 | 8 | = 0.934 | 0.09 [-0.40, 0.76] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 3.51 | 8 | = 0.128 | 0.70 [0.05, 0.94] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | 2.91 | 8 | = 0.154 | 0.65 [0.47, 1.50] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 0.16 | 8 | = 0.934 | 0.04 [-0.53, 0.31] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | -0.27 | 8 | = 0.934 | -0.09 [-0.44, 0.49] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | -0.19 | 8 | = 0.934 | -0.04 [-0.51, 0.33] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | -0.44 | 8 | = 0.934 | -0.15 [-0.50, 0.41] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | -0.51 | 8 | = 0.934 | -0.21 [-0.42, 0.52] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | -0.25 | 8 | = 0.934 | -0.07 [-0.62, 0.65] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 0.62 | 8 | = 0.934 | 0.21 [-0.17, 0.79] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | 0.77 | 8 | = 0.920 | 0.21 [0.02, 1.01] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | -0.34 | 8 | = 0.934 | -0.11 [-0.35, 0.59] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | -0.76 | 8 | = 0.920 | -0.17 [-0.31, 0.69] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | -0.39 | 8 | = 0.934 | -0.15 [-0.34, 0.60] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.92 | 8 | = 0.855 | -0.21 [-0.54, 0.48] | small | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.51 | 8 | = 0.934 | 0.21 [-0.32, 0.85] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 2.72 | 8 | = 0.172 | 0.85 [0.18, 1.11] | large | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | 2.16 | 8 | = 0.271 | 0.78 [0.34, 1.32] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | 0.56 | 8 | = 0.934 | 0.17 [-0.25, 0.60] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 0.06 | 8 | = 0.982 | 0.02 [-0.34, 0.60] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | 0.61 | 8 | = 0.934 | 0.15 [-0.19, 0.67] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | -0.17 | 8 | = 0.934 | -0.05 [-0.33, 0.58] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 1.21 | 8 | = 0.750 | 0.43 [-0.47, 0.69] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | 2.29 | 8 | = 0.237 | 0.41 [-0.26, 0.93] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | -0.15 | 8 | = 0.934 | -0.05 [-0.79, 0.37] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | -0.44 | 8 | = 0.934 | -0.14 [-0.76, 0.52] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -0.34 | 8 | = 0.934 | -0.12 [-0.86, 0.31] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | -0.76 | 8 | = 0.920 | -0.19 [-1.07, 0.25] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | 0.01 | 8 | = 0.995 | 0.00 [0.11, 1.02] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | -6.87 | 8 | = 0.010 | -0.54 [-1.21, -0.26] | medium | * |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | -1.85 | 8 | = 0.360 | -0.57 [-0.74, 0.21] | medium | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -2.86 | 8 | = 0.154 | -0.79 [-1.05, -0.14] | medium | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | -1.89 | 8 | = 0.355 | -0.60 [-0.72, 0.21] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | -2.41 | 8 | = 0.237 | -0.51 [-1.48, -0.46] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | -1.95 | 8 | = 0.355 | -0.54 [-1.27, -0.21] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | -2.29 | 8 | = 0.237 | -0.72 [-1.42, -0.41] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | -2.30 | 8 | = 0.237 | -0.58 [-1.37, -0.31] | medium | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -0.38 | 8 | = 0.934 | -0.10 [-0.40, 0.54] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | -0.25 | 8 | = 0.934 | -0.07 [-0.39, 0.45] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | -0.54 | 8 | = 0.934 | -0.16 [-0.43, 0.48] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | 0.20 | 8 | = 0.934 | 0.07 [-0.49, 0.44] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.25 | 8 | = 0.934 | -0.06 [-0.56, 0.43] | negligible | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | -0.36 | 8 | = 0.934 | -0.13 [-0.41, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Marginal trend toward condition differences (*p* = 0.070)

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

#### Amplitude

### 5.3 P1 Component

#### Latency

#### Amplitude

### 5.4 P3b Component

#### Latency

#### Amplitude

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
