# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:44:15

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
| Cardinality (no change) | 18 | 109.11 ms | 4.91 | 1.16 | [92.00, 112.00] |
| Decrease by 1 (Correct) | 15 | 101.87 ms | 7.69 | 1.99 | [92.00, 112.00] |
| Decrease by 1 (Incorrect) | 12 | 103.67 ms | 7.13 | 2.06 | [92.00, 112.00] |
| Decrease by 2 (Correct) | 21 | 106.10 ms | 7.44 | 1.62 | [92.00, 112.00] |
| Decrease by 2 (Incorrect) | 12 | 107.00 ms | 6.18 | 1.78 | [96.00, 112.00] |
| Decrease by 3 (Correct) | 19 | 103.79 ms | 7.60 | 1.74 | [92.00, 112.00] |
| Decrease by 3 (Incorrect) | 7 | 99.43 ms | 8.77 | 3.32 | [92.00, 112.00] |
| Increase by 1 (Correct) | 17 | 101.41 ms | 7.48 | 1.81 | [92.00, 112.00] |
| Increase by 1 (Incorrect) | 17 | 101.18 ms | 8.22 | 1.99 | [92.00, 112.00] |
| Increase by 2 (Correct) | 14 | 102.57 ms | 7.46 | 1.99 | [92.00, 112.00] |
| Increase by 2 (Incorrect) | 10 | 103.20 ms | 7.50 | 2.37 | [92.00, 112.00] |
| Increase by 3 (Correct) | 12 | 102.00 ms | 6.93 | 2.00 | [92.00, 112.00] |
| Increase by 3 (Incorrect) | 12 | 101.00 ms | 6.85 | 1.98 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 18 | -1.69 µV | 1.27 | 0.30 | [-4.83, -0.25] |
| Decrease by 1 (Correct) | 15 | -1.60 µV | 1.21 | 0.31 | [-4.56, -0.23] |
| Decrease by 1 (Incorrect) | 12 | -2.82 µV | 2.07 | 0.60 | [-8.16, -0.71] |
| Decrease by 2 (Correct) | 21 | -1.66 µV | 0.98 | 0.21 | [-4.30, -0.45] |
| Decrease by 2 (Incorrect) | 12 | -3.63 µV | 2.73 | 0.79 | [-8.85, -0.41] |
| Decrease by 3 (Correct) | 19 | -2.34 µV | 1.57 | 0.36 | [-6.39, -0.34] |
| Decrease by 3 (Incorrect) | 7 | -6.97 µV | 4.55 | 1.72 | [-15.27, -1.35] |
| Increase by 1 (Correct) | 17 | -1.66 µV | 1.07 | 0.26 | [-3.74, -0.14] |
| Increase by 1 (Incorrect) | 17 | -2.02 µV | 1.31 | 0.32 | [-4.54, -0.28] |
| Increase by 2 (Correct) | 14 | -1.62 µV | 1.18 | 0.32 | [-4.17, -0.21] |
| Increase by 2 (Incorrect) | 10 | -2.46 µV | 1.27 | 0.40 | [-4.91, -1.07] |
| Increase by 3 (Correct) | 12 | -1.98 µV | 0.97 | 0.28 | [-3.35, -0.70] |
| Increase by 3 (Incorrect) | 12 | -3.54 µV | 3.06 | 0.88 | [-8.80, -0.28] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | 176.00 ms | 17.10 | 3.57 | [144.00, 204.00] |
| Decrease by 1 (Correct) | 22 | 176.36 ms | 12.28 | 2.62 | [152.00, 204.00] |
| Decrease by 1 (Incorrect) | 22 | 170.55 ms | 17.52 | 3.74 | [144.00, 192.00] |
| Decrease by 2 (Correct) | 24 | 177.17 ms | 14.18 | 2.89 | [144.00, 204.00] |
| Decrease by 2 (Incorrect) | 15 | 177.07 ms | 20.25 | 5.23 | [148.00, 204.00] |
| Decrease by 3 (Correct) | 24 | 176.83 ms | 14.68 | 3.00 | [152.00, 204.00] |
| Decrease by 3 (Incorrect) | 9 | 174.22 ms | 16.26 | 5.42 | [148.00, 204.00] |
| Increase by 1 (Correct) | 23 | 169.39 ms | 18.75 | 3.91 | [144.00, 204.00] |
| Increase by 1 (Incorrect) | 22 | 176.55 ms | 16.30 | 3.47 | [144.00, 204.00] |
| Increase by 2 (Correct) | 24 | 168.83 ms | 18.42 | 3.76 | [144.00, 200.00] |
| Increase by 2 (Incorrect) | 18 | 171.33 ms | 18.21 | 4.29 | [144.00, 196.00] |
| Increase by 3 (Correct) | 23 | 170.09 ms | 18.33 | 3.82 | [144.00, 204.00] |
| Increase by 3 (Incorrect) | 20 | 167.00 ms | 19.46 | 4.35 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | -4.79 µV | 2.00 | 0.42 | [-9.57, -1.40] |
| Decrease by 1 (Correct) | 22 | -5.15 µV | 1.92 | 0.41 | [-9.90, -2.24] |
| Decrease by 1 (Incorrect) | 22 | -5.43 µV | 2.49 | 0.53 | [-13.51, -2.14] |
| Decrease by 2 (Correct) | 24 | -5.12 µV | 2.11 | 0.43 | [-9.59, -1.53] |
| Decrease by 2 (Incorrect) | 15 | -5.77 µV | 2.55 | 0.66 | [-10.77, -1.58] |
| Decrease by 3 (Correct) | 24 | -5.22 µV | 1.97 | 0.40 | [-8.60, -1.48] |
| Decrease by 3 (Incorrect) | 9 | -7.75 µV | 5.40 | 1.80 | [-16.59, -0.49] |
| Increase by 1 (Correct) | 23 | -5.10 µV | 2.17 | 0.45 | [-9.46, -0.56] |
| Increase by 1 (Incorrect) | 22 | -5.93 µV | 2.32 | 0.49 | [-9.82, -1.37] |
| Increase by 2 (Correct) | 24 | -5.47 µV | 2.43 | 0.50 | [-11.28, -1.22] |
| Increase by 2 (Incorrect) | 18 | -6.07 µV | 2.35 | 0.55 | [-11.01, -2.34] |
| Increase by 3 (Correct) | 23 | -6.29 µV | 2.53 | 0.53 | [-12.86, -2.06] |
| Increase by 3 (Incorrect) | 20 | -6.71 µV | 3.15 | 0.70 | [-13.50, -1.48] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 111.38 ms | 6.50 | 1.80 | [100.00, 116.00] |
| Decrease by 1 (Correct) | 14 | 110.86 ms | 8.07 | 2.16 | [92.00, 116.00] |
| Decrease by 1 (Incorrect) | 11 | 105.82 ms | 8.65 | 2.61 | [92.00, 116.00] |
| Decrease by 2 (Correct) | 17 | 109.88 ms | 8.50 | 2.06 | [92.00, 116.00] |
| Decrease by 2 (Incorrect) | 12 | 111.00 ms | 7.26 | 2.10 | [96.00, 116.00] |
| Decrease by 3 (Correct) | 17 | 109.41 ms | 6.32 | 1.53 | [96.00, 116.00] |
| Decrease by 3 (Incorrect) | 7 | 105.71 ms | 10.55 | 3.99 | [92.00, 116.00] |
| Increase by 1 (Correct) | 17 | 105.41 ms | 9.05 | 2.19 | [92.00, 116.00] |
| Increase by 1 (Incorrect) | 11 | 103.27 ms | 10.40 | 3.14 | [92.00, 116.00] |
| Increase by 2 (Correct) | 13 | 109.23 ms | 7.00 | 1.94 | [96.00, 116.00] |
| Increase by 2 (Incorrect) | 12 | 106.00 ms | 8.44 | 2.44 | [92.00, 116.00] |
| Increase by 3 (Correct) | 15 | 102.93 ms | 9.50 | 2.45 | [92.00, 116.00] |
| Increase by 3 (Incorrect) | 11 | 101.82 ms | 9.18 | 2.77 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 2.47 µV | 1.69 | 0.47 | [0.70, 5.73] |
| Decrease by 1 (Correct) | 14 | 2.19 µV | 1.67 | 0.45 | [0.47, 5.23] |
| Decrease by 1 (Incorrect) | 11 | 3.85 µV | 2.44 | 0.73 | [0.86, 8.84] |
| Decrease by 2 (Correct) | 17 | 2.32 µV | 1.29 | 0.31 | [0.54, 5.74] |
| Decrease by 2 (Incorrect) | 12 | 3.48 µV | 2.04 | 0.59 | [1.10, 7.73] |
| Decrease by 3 (Correct) | 17 | 2.61 µV | 1.93 | 0.47 | [0.48, 8.15] |
| Decrease by 3 (Incorrect) | 7 | 5.96 µV | 4.68 | 1.77 | [1.30, 12.94] |
| Increase by 1 (Correct) | 17 | 1.92 µV | 1.45 | 0.35 | [0.54, 4.44] |
| Increase by 1 (Incorrect) | 11 | 2.11 µV | 1.12 | 0.34 | [0.93, 4.59] |
| Increase by 2 (Correct) | 13 | 2.11 µV | 1.41 | 0.39 | [0.43, 4.70] |
| Increase by 2 (Incorrect) | 12 | 2.26 µV | 1.92 | 0.56 | [0.29, 7.59] |
| Increase by 3 (Correct) | 15 | 2.20 µV | 1.37 | 0.35 | [0.69, 5.27] |
| Increase by 3 (Incorrect) | 11 | 4.30 µV | 2.65 | 0.80 | [0.78, 8.76] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 470.57 ms | 23.14 | 6.19 | [436.00, 516.00] |
| Decrease by 1 (Correct) | 19 | 484.84 ms | 29.71 | 6.82 | [436.00, 528.00] |
| Decrease by 1 (Incorrect) | 10 | 498.80 ms | 19.51 | 6.17 | [472.00, 528.00] |
| Decrease by 2 (Correct) | 19 | 470.11 ms | 26.88 | 6.17 | [420.00, 528.00] |
| Decrease by 2 (Incorrect) | 11 | 460.00 ms | 34.78 | 10.49 | [420.00, 528.00] |
| Decrease by 3 (Correct) | 19 | 479.58 ms | 28.72 | 6.59 | [432.00, 524.00] |
| Decrease by 3 (Incorrect) | 5 | 479.20 ms | 43.58 | 19.49 | [420.00, 524.00] |
| Increase by 1 (Correct) | 17 | 489.41 ms | 39.19 | 9.51 | [420.00, 528.00] |
| Increase by 1 (Incorrect) | 9 | 471.11 ms | 31.23 | 10.41 | [420.00, 528.00] |
| Increase by 2 (Correct) | 18 | 483.11 ms | 29.67 | 6.99 | [428.00, 528.00] |
| Increase by 2 (Incorrect) | 12 | 472.00 ms | 31.17 | 9.00 | [420.00, 528.00] |
| Increase by 3 (Correct) | 21 | 477.33 ms | 35.13 | 7.67 | [420.00, 528.00] |
| Increase by 3 (Incorrect) | 13 | 470.77 ms | 30.17 | 8.37 | [420.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 2.75 µV | 1.66 | 0.44 | [0.90, 5.95] |
| Decrease by 1 (Correct) | 19 | 5.16 µV | 2.45 | 0.56 | [1.31, 9.87] |
| Decrease by 1 (Incorrect) | 10 | 4.57 µV | 3.06 | 0.97 | [1.14, 10.56] |
| Decrease by 2 (Correct) | 19 | 4.92 µV | 2.04 | 0.47 | [1.69, 8.68] |
| Decrease by 2 (Incorrect) | 11 | 8.15 µV | 5.71 | 1.72 | [2.46, 20.39] |
| Decrease by 3 (Correct) | 19 | 5.54 µV | 2.91 | 0.67 | [0.72, 12.38] |
| Decrease by 3 (Incorrect) | 5 | 5.47 µV | 3.93 | 1.76 | [2.16, 10.70] |
| Increase by 1 (Correct) | 17 | 4.65 µV | 2.62 | 0.63 | [1.41, 10.19] |
| Increase by 1 (Incorrect) | 9 | 3.85 µV | 3.16 | 1.05 | [1.16, 9.88] |
| Increase by 2 (Correct) | 18 | 5.42 µV | 2.70 | 0.64 | [1.31, 10.55] |
| Increase by 2 (Incorrect) | 12 | 6.10 µV | 3.12 | 0.90 | [2.59, 10.89] |
| Increase by 3 (Correct) | 21 | 4.41 µV | 2.60 | 0.57 | [1.25, 10.15] |
| Increase by 3 (Incorrect) | 13 | 5.87 µV | 2.74 | 0.76 | [2.47, 12.49] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1262.22, BIC = 1313.84
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = -5.63, *SE* = 2.227, *z* = -2.530, *p* = 0.011
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -4.56, *SE* = 2.333, *z* = -1.956, *p* = 0.050
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -2.14, *SE* = 2.007, *z* = -1.067, *p* = 0.286
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -1.82, *SE* = 2.344, *z* = -0.776, *p* = 0.438
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = -4.55, *SE* = 2.076, *z* = -2.193, *p* = 0.028
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = -9.28, *SE* = 2.824, *z* = -3.287, *p* = 0.001
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -7.07, *SE* = 2.103, *z* = -3.361, *p* = 0.001
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -6.37, *SE* = 2.143, *z* = -2.974, *p* = 0.003
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -6.36, *SE* = 2.219, *z* = -2.866, *p* = 0.004
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -5.32, *SE* = 2.484, *z* = -2.141, *p* = 0.032
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -6.25, *SE* = 2.334, *z* = -2.676, *p* = 0.007
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -6.64, *SE* = 2.370, *z* = -2.801, *p* = 0.005
- **SNR**: *β* = 0.74, *SE* = 0.295, *z* = 2.493, *p* = 0.013

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | 5.63 | 2.23 | 2.53 | 0.011 | 0.558 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 4.56 | 2.33 | 1.96 | 0.050 | 0.962 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 2.14 | 2.01 | 1.07 | 0.286 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 1.82 | 2.34 | 0.78 | 0.438 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | 4.55 | 2.08 | 2.19 | 0.028 | 0.854 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | 9.28 | 2.82 | 3.29 | 0.001 | 0.075 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | 7.07 | 2.10 | 3.36 | < .001 | 0.059 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 6.37 | 2.14 | 2.97 | 0.003 | 0.201 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 6.36 | 2.22 | 2.87 | 0.004 | 0.268 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 5.32 | 2.48 | 2.14 | 0.032 | 0.885 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 6.25 | 2.33 | 2.68 | 0.007 | 0.421 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 6.64 | 2.37 | 2.80 | 0.005 | 0.315 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | -1.07 | 2.43 | -0.44 | 0.660 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | -3.49 | 2.12 | -1.65 | 0.099 | 0.997 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -3.81 | 2.47 | -1.55 | 0.122 | 0.999 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | -1.08 | 2.18 | -0.50 | 0.619 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 3.65 | 2.92 | 1.25 | 0.212 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 1.44 | 2.23 | 0.64 | 0.520 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 0.74 | 2.24 | 0.33 | 0.742 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 0.73 | 2.36 | 0.31 | 0.758 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | -0.31 | 2.60 | -0.12 | 0.904 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 0.61 | 2.45 | 0.25 | 0.802 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 1.00 | 2.45 | 0.41 | 0.682 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -2.42 | 2.26 | -1.07 | 0.284 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -2.74 | 2.58 | -1.06 | 0.287 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -0.01 | 2.33 | -0.00 | 0.997 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | 4.72 | 3.02 | 1.57 | 0.117 | 0.999 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 2.51 | 2.35 | 1.07 | 0.286 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 1.81 | 2.38 | 0.76 | 0.448 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 1.80 | 2.49 | 0.72 | 0.471 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.76 | 2.70 | 0.28 | 0.779 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 1.68 | 2.55 | 0.66 | 0.509 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 2.08 | 2.58 | 0.81 | 0.421 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | -0.32 | 2.29 | -0.14 | 0.888 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 2.41 | 1.98 | 1.22 | 0.222 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 7.14 | 2.76 | 2.59 | 0.010 | 0.499 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 4.93 | 2.03 | 2.43 | 0.015 | 0.652 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 4.23 | 2.05 | 2.07 | 0.039 | 0.923 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 4.22 | 2.17 | 1.95 | 0.052 | 0.963 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 3.18 | 2.42 | 1.31 | 0.189 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 4.11 | 2.27 | 1.81 | 0.071 | 0.986 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 4.50 | 2.27 | 1.98 | 0.048 | 0.956 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 2.73 | 2.38 | 1.15 | 0.250 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 7.47 | 3.05 | 2.45 | 0.014 | 0.635 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 5.25 | 2.37 | 2.22 | 0.026 | 0.839 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 4.55 | 2.38 | 1.91 | 0.056 | 0.970 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 4.54 | 2.46 | 1.85 | 0.065 | 0.981 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 3.50 | 2.71 | 1.29 | 0.196 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 4.43 | 2.61 | 1.70 | 0.090 | 0.995 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 4.82 | 2.59 | 1.86 | 0.062 | 0.979 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 4.73 | 2.80 | 1.69 | 0.091 | 0.995 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 2.52 | 2.10 | 1.20 | 0.230 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 1.82 | 2.12 | 0.86 | 0.391 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 1.81 | 2.24 | 0.81 | 0.419 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 0.77 | 2.50 | 0.31 | 0.759 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 1.69 | 2.31 | 0.73 | 0.464 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 2.09 | 2.33 | 0.89 | 0.372 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -2.22 | 2.85 | -0.78 | 0.437 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -2.91 | 2.89 | -1.01 | 0.313 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -2.93 | 2.94 | -0.99 | 0.320 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -3.96 | 3.12 | -1.27 | 0.203 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | -3.04 | 3.02 | -1.00 | 0.315 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | -2.65 | 3.02 | -0.88 | 0.381 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | -0.70 | 2.16 | -0.32 | 0.747 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | -0.71 | 2.26 | -0.31 | 0.754 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -1.75 | 2.51 | -0.70 | 0.486 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | -0.82 | 2.37 | -0.35 | 0.728 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | -0.43 | 2.37 | -0.18 | 0.856 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -0.01 | 2.28 | -0.01 | 0.996 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -1.05 | 2.53 | -0.41 | 0.678 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -0.12 | 2.39 | -0.05 | 0.959 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 0.27 | 2.36 | 0.11 | 0.910 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -1.04 | 2.61 | -0.40 | 0.690 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | -0.11 | 2.48 | -0.05 | 0.964 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 0.28 | 2.50 | 0.11 | 0.911 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 0.93 | 2.72 | 0.34 | 0.733 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 1.32 | 2.70 | 0.49 | 0.626 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 0.39 | 2.60 | 0.15 | 0.880 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 659.32, BIC = 710.93
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = -0.26, *SE* = 0.431, *z* = -0.596, *p* = 0.551
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -1.28, *SE* = 0.454, *z* = -2.817, *p* = 0.005
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -0.24, *SE* = 0.390, *z* = -0.612, *p* = 0.541
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -2.28, *SE* = 0.457, *z* = -4.975, *p* < .001
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = -0.62, *SE* = 0.403, *z* = -1.543, *p* = 0.123
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = -5.35, *SE* = 0.552, *z* = -9.695, *p* < .001
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -0.13, *SE* = 0.410, *z* = -0.308, *p* = 0.758
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -0.86, *SE* = 0.417, *z* = -2.069, *p* = 0.039
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -0.14, *SE* = 0.432, *z* = -0.312, *p* = 0.755
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -1.51, *SE* = 0.486, *z* = -3.112, *p* = 0.002
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -0.17, *SE* = 0.453, *z* = -0.377, *p* = 0.706
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -2.45, *SE* = 0.462, *z* = -5.309, *p* < .001
- **SNR**: *β* = -0.49, *SE* = 0.059, *z* = -8.339, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | 0.26 | 0.43 | 0.60 | 0.551 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 1.28 | 0.45 | 2.82 | 0.005 | 0.211 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 0.24 | 0.39 | 0.61 | 0.541 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 2.28 | 0.46 | 4.97 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 3 (Correct) | 0.62 | 0.40 | 1.54 | 0.123 | 0.980 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | 5.35 | 0.55 | 9.69 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 1 (Correct) | 0.13 | 0.41 | 0.31 | 0.758 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 0.86 | 0.42 | 2.07 | 0.039 | 0.766 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 0.13 | 0.43 | 0.31 | 0.755 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 1.51 | 0.49 | 3.11 | 0.002 | 0.091 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 0.17 | 0.45 | 0.38 | 0.706 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 2.45 | 0.46 | 5.31 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 1.02 | 0.47 | 2.16 | 0.031 | 0.698 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | -0.02 | 0.41 | -0.04 | 0.965 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | 2.02 | 0.48 | 4.23 | < .001 | 0.001 | ** |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 0.36 | 0.42 | 0.86 | 0.390 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 5.09 | 0.57 | 8.92 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | -0.13 | 0.43 | -0.30 | 0.763 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 0.61 | 0.44 | 1.39 | 0.166 | 0.991 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | -0.12 | 0.46 | -0.27 | 0.789 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 1.25 | 0.51 | 2.48 | 0.013 | 0.431 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | -0.09 | 0.48 | -0.18 | 0.857 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 2.20 | 0.48 | 4.59 | < .001 | < .001 | *** |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -1.04 | 0.44 | -2.36 | 0.018 | 0.540 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | 1.00 | 0.50 | 1.99 | 0.047 | 0.822 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -0.66 | 0.45 | -1.44 | 0.148 | 0.989 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | 4.07 | 0.59 | 6.90 | < .001 | < .001 | *** |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | -1.15 | 0.46 | -2.52 | 0.012 | 0.408 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | -0.42 | 0.46 | -0.90 | 0.371 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | -1.14 | 0.49 | -2.36 | 0.018 | 0.540 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.23 | 0.53 | 0.44 | 0.659 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | -1.11 | 0.50 | -2.23 | 0.026 | 0.639 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 1.17 | 0.50 | 2.33 | 0.020 | 0.547 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 2.04 | 0.45 | 4.56 | < .001 | < .001 | *** |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 0.38 | 0.38 | 0.99 | 0.320 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 5.11 | 0.54 | 9.50 | < .001 | < .001 | *** |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | -0.11 | 0.40 | -0.28 | 0.776 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 0.62 | 0.40 | 1.56 | 0.118 | 0.980 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | -0.10 | 0.42 | -0.25 | 0.805 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 1.27 | 0.47 | 2.70 | 0.007 | 0.277 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | -0.07 | 0.44 | -0.15 | 0.878 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 2.21 | 0.44 | 5.00 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -1.65 | 0.46 | -3.58 | < .001 | 0.018 | * |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 3.08 | 0.60 | 5.15 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | -2.15 | 0.46 | -4.66 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | -1.41 | 0.46 | -3.06 | 0.002 | 0.106 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | -2.14 | 0.48 | -4.46 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | -0.76 | 0.53 | -1.44 | 0.151 | 0.989 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | -2.10 | 0.51 | -4.15 | < .001 | 0.002 | ** |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 0.18 | 0.50 | 0.35 | 0.725 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 4.73 | 0.55 | 8.66 | < .001 | < .001 | *** |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | -0.50 | 0.41 | -1.21 | 0.225 | 0.998 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 0.24 | 0.41 | 0.58 | 0.561 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | -0.49 | 0.43 | -1.12 | 0.262 | 0.999 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 0.89 | 0.49 | 1.83 | 0.067 | 0.913 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | -0.45 | 0.45 | -1.00 | 0.318 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 1.83 | 0.46 | 4.02 | < .001 | 0.003 | ** |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -5.23 | 0.56 | -9.37 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -4.49 | 0.57 | -7.94 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -5.22 | 0.57 | -9.08 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -3.84 | 0.61 | -6.32 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | -5.18 | 0.59 | -8.76 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | -2.90 | 0.59 | -4.91 | < .001 | < .001 | *** |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 0.74 | 0.42 | 1.75 | 0.080 | 0.937 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 0.01 | 0.44 | 0.02 | 0.985 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 1.39 | 0.49 | 2.82 | 0.005 | 0.211 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 0.04 | 0.46 | 0.10 | 0.923 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 2.33 | 0.46 | 5.03 | < .001 | < .001 | *** |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -0.73 | 0.44 | -1.64 | 0.101 | 0.967 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.65 | 0.50 | 1.31 | 0.191 | 0.995 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -0.69 | 0.47 | -1.48 | 0.138 | 0.987 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 1.59 | 0.46 | 3.45 | < .001 | 0.028 | * |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 1.38 | 0.51 | 2.70 | 0.007 | 0.277 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 0.04 | 0.48 | 0.07 | 0.940 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 2.32 | 0.49 | 4.76 | < .001 | < .001 | *** |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | -1.34 | 0.53 | -2.53 | 0.012 | 0.407 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 0.94 | 0.53 | 1.78 | 0.074 | 0.928 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 2.28 | 0.51 | 4.49 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 2183.78, BIC = 2241.30
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 2.36, *SE* = 3.524, *z* = 0.668, *p* = 0.504
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -4.66, *SE* = 3.563, *z* = -1.308, *p* = 0.191
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 1.44, *SE* = 3.444, *z* = 0.419, *p* = 0.675
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 2.61, *SE* = 4.028, *z* = 0.648, *p* = 0.517
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 1.14, *SE* = 3.448, *z* = 0.331, *p* = 0.741
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 0.29, *SE* = 4.770, *z* = 0.062, *p* = 0.951
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -5.13, *SE* = 3.505, *z* = -1.463, *p* = 0.143
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 1.62, *SE* = 3.522, *z* = 0.461, *p* = 0.644
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -6.82, *SE* = 3.456, *z* = -1.975, *p* = 0.048
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -4.28, *SE* = 3.756, *z* = -1.139, *p* = 0.255
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -4.50, *SE* = 3.489, *z* = -1.290, *p* = 0.197
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -10.48, *SE* = 3.700, *z* = -2.833, *p* = 0.005
- **SNR**: *β* = -0.07, *SE* = 0.189, *z* = -0.396, *p* = 0.692

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -2.36 | 3.52 | -0.67 | 0.504 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 4.66 | 3.56 | 1.31 | 0.191 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | -1.44 | 3.44 | -0.42 | 0.675 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -2.61 | 4.03 | -0.65 | 0.517 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | -1.14 | 3.45 | -0.33 | 0.741 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -0.30 | 4.77 | -0.06 | 0.951 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | 5.13 | 3.50 | 1.46 | 0.143 | 0.998 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -1.63 | 3.52 | -0.46 | 0.644 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 6.82 | 3.46 | 1.97 | 0.048 | 0.960 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 4.28 | 3.76 | 1.14 | 0.255 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 4.50 | 3.49 | 1.29 | 0.197 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 10.48 | 3.70 | 2.83 | 0.005 | 0.287 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 7.02 | 3.61 | 1.94 | 0.052 | 0.967 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 0.91 | 3.49 | 0.26 | 0.794 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -0.26 | 4.05 | -0.06 | 0.950 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 1.22 | 3.49 | 0.35 | 0.728 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 2.06 | 4.79 | 0.43 | 0.667 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 7.48 | 3.55 | 2.11 | 0.035 | 0.903 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 0.73 | 3.57 | 0.20 | 0.838 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 9.18 | 3.50 | 2.62 | 0.009 | 0.466 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 6.63 | 3.79 | 1.75 | 0.080 | 0.991 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 6.86 | 3.53 | 1.94 | 0.052 | 0.967 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 12.84 | 3.75 | 3.43 | < .001 | 0.047 | * |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -6.10 | 3.55 | -1.72 | 0.086 | 0.991 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -7.27 | 3.98 | -1.83 | 0.068 | 0.984 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -5.80 | 3.57 | -1.63 | 0.104 | 0.995 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -4.95 | 4.74 | -1.04 | 0.296 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 0.47 | 3.63 | 0.13 | 0.897 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | -6.29 | 3.58 | -1.76 | 0.079 | 0.991 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 2.16 | 3.59 | 0.60 | 0.546 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | -0.38 | 3.78 | -0.10 | 0.919 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | -0.16 | 3.59 | -0.04 | 0.965 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 5.82 | 3.67 | 1.58 | 0.113 | 0.996 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | -1.17 | 4.02 | -0.29 | 0.772 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 0.30 | 3.40 | 0.09 | 0.929 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 1.15 | 4.76 | 0.24 | 0.809 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 6.57 | 3.45 | 1.91 | 0.057 | 0.973 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | -0.18 | 3.50 | -0.05 | 0.959 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 8.27 | 3.40 | 2.43 | 0.015 | 0.662 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 5.72 | 3.74 | 1.53 | 0.126 | 0.997 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 5.94 | 3.44 | 1.73 | 0.084 | 0.991 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 11.93 | 3.70 | 3.22 | 0.001 | 0.092 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 1.47 | 4.04 | 0.36 | 0.716 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 2.32 | 5.05 | 0.46 | 0.647 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 7.74 | 4.11 | 1.88 | 0.060 | 0.975 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 0.99 | 4.03 | 0.24 | 0.807 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 9.44 | 4.07 | 2.32 | 0.020 | 0.752 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 6.89 | 4.19 | 1.65 | 0.100 | 0.995 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 7.11 | 4.07 | 1.75 | 0.080 | 0.991 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 13.09 | 4.08 | 3.21 | 0.001 | 0.096 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 0.85 | 4.77 | 0.18 | 0.859 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 6.27 | 3.45 | 1.82 | 0.069 | 0.984 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | -0.49 | 3.51 | -0.14 | 0.890 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 7.96 | 3.40 | 2.34 | 0.019 | 0.738 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 5.42 | 3.75 | 1.44 | 0.149 | 0.999 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 5.64 | 3.44 | 1.64 | 0.101 | 0.995 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 11.62 | 3.72 | 3.12 | 0.002 | 0.124 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 5.42 | 4.82 | 1.12 | 0.261 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -1.33 | 4.78 | -0.28 | 0.781 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | 7.12 | 4.79 | 1.49 | 0.137 | 0.998 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 4.57 | 4.90 | 0.93 | 0.351 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 4.80 | 4.79 | 1.00 | 0.317 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 10.78 | 4.85 | 2.22 | 0.026 | 0.832 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | -6.75 | 3.56 | -1.90 | 0.058 | 0.974 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 1.70 | 3.44 | 0.49 | 0.622 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -0.85 | 3.82 | -0.22 | 0.824 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | -0.63 | 3.48 | -0.18 | 0.857 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 5.35 | 3.81 | 1.41 | 0.160 | 0.999 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | 8.45 | 3.52 | 2.40 | 0.016 | 0.686 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | 5.90 | 3.79 | 1.56 | 0.119 | 0.997 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | 6.13 | 3.54 | 1.73 | 0.083 | 0.991 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 12.11 | 3.71 | 3.26 | 0.001 | 0.082 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -2.55 | 3.77 | -0.68 | 0.499 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | -2.32 | 3.44 | -0.67 | 0.500 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 3.66 | 3.74 | 0.98 | 0.329 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 0.22 | 3.79 | 0.06 | 0.953 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 6.20 | 3.88 | 1.60 | 0.110 | 0.996 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 5.98 | 3.76 | 1.59 | 0.111 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.76, *p* = 0.689, η²_G = 0.098
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | 0.00 | 3 | = 1.000 | 0.00 [-0.74, 0.18] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | 1.57 | 3 | = 0.787 | 0.34 [-0.24, 0.68] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | 0.00 | 3 | = 1.000 | 0.00 [-0.57, 0.30] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | 0.36 | 3 | = 0.961 | 0.13 [-0.86, 0.31] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -1.41 | 3 | = 0.787 | -0.27 [-0.52, 0.35] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | 0.12 | 3 | = 1.000 | 0.11 [-0.90, 0.77] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 1.57 | 3 | = 0.787 | 0.48 [-0.11, 0.81] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | -1.00 | 3 | = 0.824 | -0.06 [-0.65, 0.24] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | 1.57 | 3 | = 0.787 | 0.18 [0.02, 0.93] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | 2.85 | 3 | = 0.728 | 1.06 [-0.21, 0.85] | large | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | -0.54 | 3 | = 0.961 | -0.19 [-0.19, 0.71] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | 0.87 | 3 | = 0.915 | 0.19 [0.24, 1.34] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | 1.44 | 3 | = 0.787 | 0.36 [-0.10, 0.87] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | 0.00 | 3 | = 1.000 | 0.00 [-0.41, 0.48] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | 0.31 | 3 | = 0.961 | 0.13 [-0.57, 0.54] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | -1.10 | 3 | = 0.811 | -0.28 [-0.35, 0.54] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | 0.12 | 3 | = 1.000 | 0.11 [-0.81, 0.73] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 1.71 | 3 | = 0.787 | 0.49 [0.05, 1.03] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -0.52 | 3 | = 0.961 | -0.06 [-0.41, 0.52] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 1.57 | 3 | = 0.787 | 0.18 [0.18, 1.16] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 2.96 | 3 | = 0.728 | 1.11 [-0.23, 0.82] | large | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | -0.47 | 3 | = 0.961 | -0.20 [0.01, 0.98] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | 0.68 | 3 | = 0.961 | 0.19 [0.29, 1.46] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | -1.19 | 3 | = 0.811 | -0.38 [-0.87, 0.05] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | -0.48 | 3 | = 0.961 | -0.13 [-0.93, 0.21] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | -2.10 | 3 | = 0.787 | -0.63 [-0.81, 0.11] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | -0.21 | 3 | = 1.000 | -0.21 [-0.99, 0.56] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 0.33 | 3 | = 0.961 | 0.15 [-0.34, 0.55] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | -1.70 | 3 | = 0.787 | -0.38 [-0.73, 0.20] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | -0.54 | 3 | = 0.961 | -0.17 [-0.25, 0.65] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | 1.15 | 3 | = 0.811 | 0.65 [-0.56, 0.51] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | -1.12 | 3 | = 0.811 | -0.54 [-0.49, 0.39] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | -0.40 | 3 | = 0.961 | -0.09 [-0.04, 1.02] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 0.29 | 3 | = 0.961 | 0.14 [-0.64, 0.47] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | -1.41 | 3 | = 0.787 | -0.31 [-0.40, 0.45] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | 0.13 | 3 | = 1.000 | 0.12 [-0.84, 0.70] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 1.63 | 3 | = 0.787 | 0.52 [-0.08, 0.81] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | -0.33 | 3 | = 0.961 | -0.06 [-0.46, 0.43] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 1.19 | 3 | = 0.811 | 0.20 [0.10, 1.00] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | 3.60 | 3 | = 0.728 | 1.21 [-0.13, 0.90] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | -0.57 | 3 | = 0.961 | -0.22 [-0.10, 0.78] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | 0.58 | 3 | = 0.961 | 0.20 [0.22, 1.28] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | -0.82 | 3 | = 0.922 | -0.32 [-0.51, 0.60] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | -0.04 | 3 | = 1.000 | -0.04 [-0.97, 0.88] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 0.44 | 3 | = 0.961 | 0.24 [-0.18, 0.97] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | -0.47 | 3 | = 0.961 | -0.17 [-0.36, 0.81] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | 0.00 | 3 | = 1.000 | 0.00 [-0.21, 0.93] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | 1.01 | 3 | = 0.824 | 0.62 [-0.47, 0.81] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | -0.57 | 3 | = 0.961 | -0.27 [-0.32, 0.80] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | 0.17 | 3 | = 1.000 | 0.04 [-0.01, 1.41] | negligible | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.39 | 3 | = 0.961 | 0.35 [-0.67, 0.87] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 1.72 | 3 | = 0.787 | 0.74 [-0.13, 0.75] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | 0.79 | 3 | = 0.925 | 0.19 [-0.46, 0.42] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | 1.70 | 3 | = 0.787 | 0.46 [0.05, 0.95] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 3.52 | 3 | = 0.728 | 1.46 [-0.35, 0.65] | large | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | 0.29 | 3 | = 0.961 | 0.07 [-0.09, 0.80] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | 1.26 | 3 | = 0.811 | 0.40 [0.13, 1.16] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 0.41 | 3 | = 0.961 | 0.34 [-0.52, 1.05] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | -0.17 | 3 | = 1.000 | -0.16 [-1.03, 0.65] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | 0.06 | 3 | = 1.000 | 0.05 [-0.50, 1.07] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | 1.12 | 3 | = 0.811 | 0.84 [-0.59, 1.12] | large | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -0.35 | 3 | = 0.961 | -0.28 [-0.66, 0.88] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | 0.09 | 3 | = 1.000 | 0.09 [-0.82, 1.31] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -1.89 | 3 | = 0.787 | -0.51 [-0.91, 0.02] | medium | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | -1.57 | 3 | = 0.787 | -0.31 [-0.26, 0.62] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | 1.85 | 3 | = 0.787 | 0.43 [-0.58, 0.45] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -1.44 | 3 | = 0.787 | -0.65 [-0.49, 0.38] | medium | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | -0.60 | 3 | = 0.961 | -0.22 [-0.21, 0.77] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 2.45 | 3 | = 0.787 | 0.23 [0.01, 0.95] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | 2.89 | 3 | = 0.728 | 1.07 [-0.20, 0.90] | large | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | -0.32 | 3 | = 0.961 | -0.12 [-0.15, 0.76] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | 1.21 | 3 | = 0.811 | 0.23 [0.12, 1.21] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 2.94 | 3 | = 0.728 | 0.85 [-0.60, 0.40] | large | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | -1.00 | 3 | = 0.824 | -0.37 [-0.80, 0.09] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | 0.18 | 3 | = 1.000 | 0.05 [-0.26, 0.69] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | -3.69 | 3 | = 0.728 | -1.31 [-0.51, 0.51] | large | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | -1.34 | 3 | = 0.811 | -0.62 [-0.53, 0.58] | medium | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.85 | 3 | = 0.915 | 0.34 [-0.10, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1100.05, BIC = 1157.56
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = -0.14, *SE* = 0.474, *z* = -0.301, *p* = 0.763
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -1.04, *SE* = 0.479, *z* = -2.164, *p* = 0.030
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -0.20, *SE* = 0.463, *z* = -0.421, *p* = 0.674
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -1.41, *SE* = 0.542, *z* = -2.594, *p* = 0.009
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = -0.22, *SE* = 0.464, *z* = -0.482, *p* = 0.630
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = -3.50, *SE* = 0.641, *z* = -5.451, *p* < .001
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 0.04, *SE* = 0.472, *z* = 0.087, *p* = 0.931
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -1.30, *SE* = 0.474, *z* = -2.753, *p* = 0.006
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -0.39, *SE* = 0.465, *z* = -0.829, *p* = 0.407
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -1.49, *SE* = 0.505, *z* = -2.944, *p* = 0.003
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -1.30, *SE* = 0.470, *z* = -2.771, *p* = 0.006
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -2.54, *SE* = 0.498, *z* = -5.108, *p* < .001
- **SNR**: *β* = -0.18, *SE* = 0.025, *z* = -6.961, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | 0.14 | 0.47 | 0.30 | 0.763 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 1.04 | 0.48 | 2.16 | 0.030 | 0.681 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 0.20 | 0.46 | 0.42 | 0.674 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 1.41 | 0.54 | 2.59 | 0.009 | 0.391 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | 0.22 | 0.46 | 0.48 | 0.630 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | 3.50 | 0.64 | 5.45 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 1 (Correct) | -0.04 | 0.47 | -0.09 | 0.931 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 1.30 | 0.47 | 2.75 | 0.006 | 0.278 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 0.39 | 0.46 | 0.83 | 0.407 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 1.49 | 0.51 | 2.94 | 0.003 | 0.174 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 1.30 | 0.47 | 2.77 | 0.006 | 0.270 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 2.54 | 0.50 | 5.11 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 0.89 | 0.49 | 1.84 | 0.065 | 0.869 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 0.05 | 0.47 | 0.11 | 0.911 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | 1.26 | 0.55 | 2.32 | 0.021 | 0.582 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 0.08 | 0.47 | 0.17 | 0.863 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 3.35 | 0.64 | 5.21 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | -0.18 | 0.48 | -0.39 | 0.700 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 1.16 | 0.48 | 2.42 | 0.016 | 0.517 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 0.24 | 0.47 | 0.52 | 0.606 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 1.35 | 0.51 | 2.64 | 0.008 | 0.365 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 1.16 | 0.48 | 2.44 | 0.015 | 0.504 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 2.40 | 0.50 | 4.76 | < .001 | < .001 | *** |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -0.84 | 0.48 | -1.76 | 0.078 | 0.905 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | 0.37 | 0.54 | 0.69 | 0.492 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -0.81 | 0.48 | -1.70 | 0.090 | 0.929 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | 2.46 | 0.64 | 3.85 | < .001 | 0.008 | ** |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | -1.08 | 0.49 | -2.20 | 0.028 | 0.663 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 0.27 | 0.48 | 0.56 | 0.578 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | -0.65 | 0.48 | -1.35 | 0.177 | 0.994 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.45 | 0.51 | 0.89 | 0.375 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 0.26 | 0.48 | 0.55 | 0.585 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 1.51 | 0.49 | 3.05 | 0.002 | 0.133 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 1.21 | 0.54 | 2.24 | 0.025 | 0.642 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | 0.03 | 0.46 | 0.06 | 0.950 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 3.30 | 0.64 | 5.16 | < .001 | < .001 | *** |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | -0.24 | 0.46 | -0.51 | 0.611 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 1.11 | 0.47 | 2.36 | 0.019 | 0.560 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 0.19 | 0.46 | 0.42 | 0.678 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 1.29 | 0.50 | 2.57 | 0.010 | 0.406 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 1.11 | 0.46 | 2.39 | 0.017 | 0.537 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 2.35 | 0.50 | 4.72 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -1.18 | 0.54 | -2.17 | 0.030 | 0.681 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 2.09 | 0.68 | 3.07 | 0.002 | 0.124 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | -1.45 | 0.55 | -2.61 | 0.009 | 0.379 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | -0.10 | 0.54 | -0.19 | 0.852 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | -1.02 | 0.55 | -1.87 | 0.062 | 0.863 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 0.08 | 0.56 | 0.15 | 0.883 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | -0.10 | 0.55 | -0.19 | 0.848 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 1.14 | 0.55 | 2.07 | 0.038 | 0.744 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 3.27 | 0.64 | 5.10 | < .001 | < .001 | *** |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | -0.26 | 0.46 | -0.57 | 0.568 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 1.08 | 0.47 | 2.29 | 0.022 | 0.599 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 0.16 | 0.46 | 0.35 | 0.724 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 1.26 | 0.50 | 2.51 | 0.012 | 0.459 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 1.08 | 0.46 | 2.33 | 0.020 | 0.581 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 2.32 | 0.50 | 4.63 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -3.54 | 0.65 | -5.45 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | -2.19 | 0.64 | -3.41 | < .001 | 0.041 | * |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -3.11 | 0.64 | -4.83 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -2.01 | 0.66 | -3.05 | 0.002 | 0.133 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | -2.20 | 0.64 | -3.41 | < .001 | 0.041 | * |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | -0.95 | 0.65 | -1.46 | 0.144 | 0.985 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 1.35 | 0.48 | 2.81 | 0.005 | 0.249 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 0.43 | 0.46 | 0.92 | 0.357 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 1.53 | 0.51 | 2.97 | 0.003 | 0.162 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 1.34 | 0.47 | 2.87 | 0.004 | 0.214 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 2.58 | 0.51 | 5.04 | < .001 | < .001 | *** |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -0.92 | 0.47 | -1.94 | 0.052 | 0.821 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.18 | 0.51 | 0.36 | 0.719 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -0.00 | 0.48 | -0.01 | 0.994 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 1.24 | 0.50 | 2.48 | 0.013 | 0.477 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 1.10 | 0.51 | 2.18 | 0.030 | 0.681 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 0.92 | 0.46 | 1.98 | 0.048 | 0.804 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 2.16 | 0.50 | 4.28 | < .001 | 0.001 | ** |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | -0.19 | 0.51 | -0.37 | 0.714 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 1.06 | 0.52 | 2.02 | 0.043 | 0.777 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 1.24 | 0.51 | 2.46 | 0.014 | 0.492 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.873, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | 1.46 | 3 | = 0.988 | 0.38 [-0.29, 0.63] | small | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | 1.11 | 3 | = 0.988 | 0.31 [-0.20, 0.73] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | 1.96 | 3 | = 0.988 | 0.53 [-0.19, 0.69] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | 1.44 | 3 | = 0.988 | 0.47 [-0.33, 0.84] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | 1.47 | 3 | = 0.988 | 0.53 [-0.11, 0.78] | medium | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | 0.23 | 3 | = 0.988 | 0.07 [-0.35, 1.44] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 0.96 | 3 | = 0.988 | 0.51 [-0.16, 0.75] | medium | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | 1.43 | 3 | = 0.988 | 0.41 [0.17, 1.14] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | 3.17 | 3 | = 0.988 | 0.41 [0.12, 1.05] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | -0.12 | 3 | = 0.988 | -0.02 [0.07, 1.19] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | 2.37 | 3 | = 0.988 | 0.38 [0.59, 1.74] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | 1.14 | 3 | = 0.988 | 0.32 [0.12, 1.18] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | -0.61 | 3 | = 0.988 | -0.15 [-0.28, 0.66] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | 0.44 | 3 | = 0.988 | 0.10 [-0.34, 0.55] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | 0.25 | 3 | = 0.988 | 0.10 [-0.37, 0.75] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | 0.28 | 3 | = 0.988 | 0.06 [-0.32, 0.57] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | -0.54 | 3 | = 0.988 | -0.21 [-0.34, 1.28] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 0.06 | 3 | = 0.988 | 0.02 [-0.20, 0.73] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -0.02 | 3 | = 0.988 | -0.01 [0.02, 1.02] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | 0.27 | 3 | = 0.988 | 0.05 [0.08, 1.03] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | -1.23 | 3 | = 0.988 | -0.40 [-0.13, 0.94] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | -0.04 | 3 | = 0.988 | -0.02 [0.28, 1.33] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | -0.78 | 3 | = 0.988 | -0.09 [0.14, 1.25] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | 2.01 | 3 | = 0.988 | 0.29 [-0.49, 0.40] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | 0.67 | 3 | = 0.988 | 0.25 [-0.64, 0.47] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | 1.72 | 3 | = 0.988 | 0.27 [-0.47, 0.42] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | -0.28 | 3 | = 0.988 | -0.13 [-0.32, 1.32] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 0.76 | 3 | = 0.988 | 0.24 [-0.55, 0.34] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 0.44 | 3 | = 0.988 | 0.16 [-0.21, 0.71] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 0.67 | 3 | = 0.988 | 0.19 [-0.36, 0.53] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | -1.14 | 3 | = 0.988 | -0.34 [-0.49, 0.57] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 0.34 | 3 | = 0.988 | 0.13 [0.05, 0.99] | negligible | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 0.29 | 3 | = 0.988 | 0.05 [-0.12, 0.92] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | 0.06 | 3 | = 0.988 | 0.02 [-0.53, 0.58] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | -0.19 | 3 | = 0.988 | -0.05 [-0.36, 0.49] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | -0.79 | 3 | = 0.988 | -0.29 [-0.37, 1.24] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | -0.28 | 3 | = 0.988 | -0.10 [-0.49, 0.38] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | -0.41 | 3 | = 0.988 | -0.11 [-0.08, 0.84] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | -0.17 | 3 | = 0.988 | -0.04 [-0.26, 0.59] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | -2.57 | 3 | = 0.988 | -0.55 [-0.19, 0.82] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | -0.29 | 3 | = 0.988 | -0.12 [0.08, 1.00] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | -1.83 | 3 | = 0.988 | -0.21 [0.01, 1.00] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | -0.12 | 3 | = 0.988 | -0.06 [-0.62, 0.49] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | -1.26 | 3 | = 0.988 | -0.28 [-0.73, 1.14] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | -0.18 | 3 | = 0.988 | -0.10 [-0.61, 0.50] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | -0.71 | 3 | = 0.988 | -0.11 [-0.38, 0.78] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | -0.16 | 3 | = 0.988 | -0.05 [-0.47, 0.64] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | -3.20 | 3 | = 0.988 | -0.48 [-0.86, 0.43] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | -0.27 | 3 | = 0.988 | -0.12 [-0.27, 0.86] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.57 | 3 | = 0.988 | -0.19 [-0.43, 0.86] | negligible | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | -0.53 | 3 | = 0.988 | -0.27 [-0.41, 1.18] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | -0.26 | 3 | = 0.988 | -0.06 [-0.51, 0.35] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | -0.16 | 3 | = 0.988 | -0.08 [-0.15, 0.75] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | -0.02 | 3 | = 0.988 | -0.01 [-0.29, 0.55] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | -1.33 | 3 | = 0.988 | -0.55 [-0.23, 0.78] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | -0.19 | 3 | = 0.988 | -0.09 [0.03, 0.94] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | -0.94 | 3 | = 0.988 | -0.18 [-0.03, 0.96] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 0.42 | 3 | = 0.988 | 0.24 [-1.18, 0.41] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | 0.67 | 3 | = 0.988 | 0.21 [-1.05, 0.64] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | 0.84 | 3 | = 0.988 | 0.23 [-1.24, 0.37] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | -0.35 | 3 | = 0.988 | -0.09 [-1.15, 0.56] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | 0.50 | 3 | = 0.988 | 0.20 [-1.08, 0.49] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | 0.38 | 3 | = 0.988 | 0.15 [-1.55, 0.65] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -0.06 | 3 | = 0.988 | -0.03 [-0.07, 0.85] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | 0.07 | 3 | = 0.988 | 0.03 [-0.17, 0.71] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | -1.00 | 3 | = 0.988 | -0.53 [-0.33, 0.71] | medium | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -0.07 | 3 | = 0.988 | -0.04 [0.16, 1.10] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | -0.45 | 3 | = 0.988 | -0.14 [-0.05, 0.96] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | 0.16 | 3 | = 0.988 | 0.06 [-0.63, 0.27] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | -3.52 | 3 | = 0.988 | -0.43 [-0.51, 0.56] | small | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | -0.03 | 3 | = 0.988 | -0.01 [-0.20, 0.70] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | -0.25 | 3 | = 0.988 | -0.09 [-0.35, 0.65] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -1.94 | 3 | = 0.988 | -0.43 [-0.23, 0.78] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | -0.24 | 3 | = 0.988 | -0.06 [0.02, 0.94] | negligible | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | -0.64 | 3 | = 0.988 | -0.14 [-0.09, 0.88] | negligible | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | 1.32 | 3 | = 0.988 | 0.40 [-0.28, 0.77] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | 1.19 | 3 | = 0.988 | 0.34 [-0.11, 1.05] | small | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | -0.19 | 3 | = 0.988 | -0.08 [-0.34, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1197.76, BIC = 1247.94
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 0.70, *SE* = 2.709, *z* = 0.258, *p* = 0.796
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = -4.57, *SE* = 2.881, *z* = -1.587, *p* = 0.112
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -0.22, *SE* = 2.585, *z* = -0.085, *p* = 0.933
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 1.03, *SE* = 2.927, *z* = 0.354, *p* = 0.724
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = -0.01, *SE* = 2.643, *z* = -0.006, *p* = 0.995
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = -3.99, *SE* = 3.401, *z* = -1.173, *p* = 0.241
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = -4.16, *SE* = 2.630, *z* = -1.580, *p* = 0.114
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = -6.14, *SE* = 3.011, *z* = -2.038, *p* = 0.042
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = -1.64, *SE* = 2.780, *z* = -0.591, *p* = 0.555
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -4.53, *SE* = 2.891, *z* = -1.566, *p* = 0.117
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = -7.63, *SE* = 2.636, *z* = -2.895, *p* = 0.004
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -7.71, *SE* = 2.984, *z* = -2.585, *p* = 0.010
- **SNR**: *β* = 0.32, *SE* = 0.234, *z* = 1.353, *p* = 0.176

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -0.70 | 2.71 | -0.26 | 0.796 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | 4.57 | 2.88 | 1.59 | 0.112 | 0.997 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 0.22 | 2.58 | 0.08 | 0.933 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -1.04 | 2.93 | -0.35 | 0.724 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | 0.01 | 2.64 | 0.01 | 0.995 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | 3.99 | 3.40 | 1.17 | 0.241 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | 4.16 | 2.63 | 1.58 | 0.114 | 0.997 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | 6.14 | 3.01 | 2.04 | 0.042 | 0.928 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | 1.64 | 2.78 | 0.59 | 0.555 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 4.53 | 2.89 | 1.57 | 0.117 | 0.997 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | 7.63 | 2.64 | 2.89 | 0.004 | 0.239 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 7.71 | 2.98 | 2.58 | 0.010 | 0.491 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | 5.27 | 2.82 | 1.87 | 0.061 | 0.973 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 0.92 | 2.52 | 0.37 | 0.715 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -0.34 | 2.80 | -0.12 | 0.904 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 0.71 | 2.53 | 0.28 | 0.778 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 4.69 | 3.32 | 1.41 | 0.158 | 0.999 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 4.86 | 2.52 | 1.93 | 0.054 | 0.961 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 6.84 | 2.85 | 2.40 | 0.017 | 0.674 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 2.34 | 2.67 | 0.88 | 0.381 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 5.23 | 2.80 | 1.87 | 0.062 | 0.973 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 8.33 | 2.58 | 3.23 | 0.001 | 0.094 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 8.41 | 2.86 | 2.95 | 0.003 | 0.209 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | -4.35 | 2.71 | -1.60 | 0.109 | 0.997 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -5.61 | 2.97 | -1.89 | 0.059 | 0.971 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | -4.56 | 2.72 | -1.67 | 0.094 | 0.995 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -0.58 | 3.48 | -0.17 | 0.867 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | -0.42 | 2.72 | -0.15 | 0.878 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 1.56 | 3.03 | 0.52 | 0.606 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | -2.93 | 2.87 | -1.02 | 0.308 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | -0.05 | 2.98 | -0.02 | 0.987 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 3.06 | 2.76 | 1.11 | 0.268 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 3.14 | 3.02 | 1.04 | 0.298 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | -1.25 | 2.66 | -0.47 | 0.637 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | -0.20 | 2.41 | -0.08 | 0.933 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | 3.77 | 3.19 | 1.18 | 0.237 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 3.94 | 2.38 | 1.65 | 0.098 | 0.996 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 5.92 | 2.73 | 2.16 | 0.030 | 0.862 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 1.42 | 2.57 | 0.55 | 0.580 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | 4.31 | 2.66 | 1.62 | 0.105 | 0.996 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 7.41 | 2.45 | 3.03 | 0.002 | 0.170 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | 7.49 | 2.72 | 2.76 | 0.006 | 0.335 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 1.05 | 2.71 | 0.39 | 0.698 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 5.03 | 3.35 | 1.50 | 0.134 | 0.998 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 5.19 | 2.65 | 1.96 | 0.051 | 0.958 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 7.17 | 2.91 | 2.46 | 0.014 | 0.610 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 2.68 | 2.82 | 0.95 | 0.342 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 5.56 | 2.86 | 1.94 | 0.052 | 0.960 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 8.67 | 2.74 | 3.16 | 0.002 | 0.114 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 8.75 | 2.91 | 3.01 | 0.003 | 0.176 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 3.98 | 3.21 | 1.24 | 0.215 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 4.14 | 2.40 | 1.73 | 0.084 | 0.992 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 6.12 | 2.74 | 2.23 | 0.026 | 0.816 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 1.63 | 2.61 | 0.62 | 0.533 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 4.51 | 2.72 | 1.66 | 0.097 | 0.996 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 7.62 | 2.50 | 3.05 | 0.002 | 0.162 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 7.70 | 2.74 | 2.81 | 0.005 | 0.300 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 0.17 | 3.17 | 0.05 | 0.958 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 2.14 | 3.45 | 0.62 | 0.534 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | -2.35 | 3.33 | -0.70 | 0.481 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 0.53 | 3.37 | 0.16 | 0.874 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 3.64 | 3.26 | 1.12 | 0.264 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 3.72 | 3.42 | 1.09 | 0.277 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 1.98 | 2.71 | 0.73 | 0.465 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | -2.51 | 2.56 | -0.98 | 0.327 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 0.37 | 2.67 | 0.14 | 0.890 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 3.47 | 2.47 | 1.41 | 0.159 | 0.999 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 3.56 | 2.70 | 1.32 | 0.187 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -4.49 | 2.87 | -1.57 | 0.117 | 0.997 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -1.61 | 2.96 | -0.54 | 0.587 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | 1.50 | 2.82 | 0.53 | 0.596 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 1.58 | 2.96 | 0.53 | 0.594 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 2.88 | 2.81 | 1.03 | 0.305 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 5.99 | 2.63 | 2.28 | 0.023 | 0.782 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 6.07 | 2.88 | 2.11 | 0.035 | 0.895 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 3.11 | 2.72 | 1.14 | 0.254 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 3.19 | 2.94 | 1.08 | 0.278 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 0.08 | 2.80 | 0.03 | 0.977 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 629.55, BIC = 679.72
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 0.30, *SE* = 0.495, *z* = 0.603, *p* = 0.547
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = 1.82, *SE* = 0.527, *z* = 3.448, *p* = 0.001
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 0.48, *SE* = 0.472, *z* = 1.028, *p* = 0.304
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 2.04, *SE* = 0.537, *z* = 3.804, *p* < .001
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 0.83, *SE* = 0.484, *z* = 1.709, *p* = 0.087
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 4.67, *SE* = 0.624, *z* = 7.490, *p* < .001
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 0.33, *SE* = 0.481, *z* = 0.678, *p* = 0.498
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 0.48, *SE* = 0.554, *z* = 0.860, *p* = 0.390
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = 0.31, *SE* = 0.509, *z* = 0.600, *p* = 0.548
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = 1.03, *SE* = 0.532, *z* = 1.929, *p* = 0.054
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = 0.24, *SE* = 0.481, *z* = 0.498, *p* = 0.619
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = 2.85, *SE* = 0.547, *z* = 5.210, *p* < .001
- **SNR**: *β* = 0.28, *SE* = 0.045, *z* = 6.280, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -0.30 | 0.50 | -0.60 | 0.547 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | -1.82 | 0.53 | -3.45 | < .001 | 0.031 | * |
| Cardinality (no change) - Decrease by 2 (Correct) | -0.49 | 0.47 | -1.03 | 0.304 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -2.04 | 0.54 | -3.80 | < .001 | 0.008 | ** |
| Cardinality (no change) - Decrease by 3 (Correct) | -0.83 | 0.48 | -1.71 | 0.087 | 0.969 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -4.67 | 0.62 | -7.49 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 1 (Correct) | -0.33 | 0.48 | -0.68 | 0.498 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -0.48 | 0.55 | -0.86 | 0.390 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | -0.31 | 0.51 | -0.60 | 0.548 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | -1.03 | 0.53 | -1.93 | 0.054 | 0.890 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | -0.24 | 0.48 | -0.50 | 0.619 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | -2.85 | 0.55 | -5.21 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | -1.52 | 0.52 | -2.95 | 0.003 | 0.145 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | -0.19 | 0.46 | -0.41 | 0.685 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -1.75 | 0.51 | -3.40 | < .001 | 0.036 | * |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | -0.53 | 0.46 | -1.14 | 0.255 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | -4.37 | 0.61 | -7.16 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | -0.03 | 0.46 | -0.06 | 0.953 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | -0.18 | 0.52 | -0.34 | 0.734 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | -0.01 | 0.49 | -0.01 | 0.988 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | -0.73 | 0.51 | -1.42 | 0.156 | 0.996 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 0.06 | 0.47 | 0.12 | 0.901 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | -2.55 | 0.52 | -4.88 | < .001 | < .001 | *** |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | 1.33 | 0.50 | 2.68 | 0.007 | 0.283 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -0.23 | 0.55 | -0.41 | 0.679 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | 0.99 | 0.50 | 1.99 | 0.047 | 0.867 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -2.85 | 0.64 | -4.45 | < .001 | < .001 | *** |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 1.49 | 0.50 | 2.99 | 0.003 | 0.128 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 1.34 | 0.56 | 2.41 | 0.016 | 0.501 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 1.51 | 0.53 | 2.87 | 0.004 | 0.171 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 0.79 | 0.55 | 1.44 | 0.149 | 0.996 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 1.58 | 0.51 | 3.12 | 0.002 | 0.088 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | -1.03 | 0.55 | -1.87 | 0.062 | 0.917 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | -1.56 | 0.49 | -3.20 | 0.001 | 0.069 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | -0.34 | 0.44 | -0.77 | 0.439 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | -4.19 | 0.58 | -7.16 | < .001 | < .001 | *** |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 0.16 | 0.43 | 0.37 | 0.714 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | 0.01 | 0.50 | 0.02 | 0.986 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 0.18 | 0.47 | 0.38 | 0.702 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | -0.54 | 0.49 | -1.11 | 0.267 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | 0.25 | 0.45 | 0.55 | 0.583 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | -2.37 | 0.50 | -4.76 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 1.22 | 0.50 | 2.44 | 0.015 | 0.478 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | -2.63 | 0.62 | -4.26 | < .001 | 0.001 | ** |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 1.72 | 0.49 | 3.53 | < .001 | 0.023 | * |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 1.57 | 0.53 | 2.95 | 0.003 | 0.145 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 1.74 | 0.52 | 3.37 | < .001 | 0.039 | * |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 1.02 | 0.52 | 1.94 | 0.052 | 0.890 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 1.80 | 0.50 | 3.59 | < .001 | 0.019 | * |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | -0.81 | 0.53 | -1.52 | 0.128 | 0.993 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -3.84 | 0.59 | -6.53 | < .001 | < .001 | *** |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 0.50 | 0.44 | 1.14 | 0.254 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 0.35 | 0.51 | 0.69 | 0.489 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 0.52 | 0.48 | 1.09 | 0.276 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | -0.20 | 0.50 | -0.40 | 0.692 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 0.59 | 0.46 | 1.28 | 0.200 | 0.999 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | -2.02 | 0.50 | -4.01 | < .001 | 0.004 | ** |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 4.34 | 0.58 | 7.49 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 4.19 | 0.64 | 6.60 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | 4.36 | 0.61 | 7.12 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 3.64 | 0.62 | 5.87 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 4.43 | 0.60 | 7.41 | < .001 | < .001 | *** |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 1.82 | 0.63 | 2.89 | 0.004 | 0.164 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | -0.15 | 0.50 | -0.30 | 0.762 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 0.02 | 0.47 | 0.04 | 0.966 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -0.70 | 0.49 | -1.43 | 0.152 | 0.996 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 0.09 | 0.45 | 0.19 | 0.849 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | -2.53 | 0.49 | -5.12 | < .001 | < .001 | *** |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | 0.17 | 0.52 | 0.33 | 0.745 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -0.55 | 0.54 | -1.01 | 0.310 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | 0.24 | 0.52 | 0.46 | 0.647 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | -2.38 | 0.54 | -4.40 | < .001 | < .001 | *** |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -0.72 | 0.52 | -1.40 | 0.162 | 0.997 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 0.07 | 0.48 | 0.14 | 0.891 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | -2.55 | 0.53 | -4.83 | < .001 | < .001 | *** |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 0.79 | 0.50 | 1.57 | 0.116 | 0.989 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | -1.83 | 0.54 | -3.39 | < .001 | 0.037 | * |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -2.61 | 0.51 | -5.09 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1820.64, BIC = 1872.34
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 11.07, *SE* = 9.989, *z* = 1.109, *p* = 0.268
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = 28.74, *SE* = 11.440, *z* = 2.512, *p* = 0.012
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = -4.59, *SE* = 10.006, *z* = -0.459, *p* = 0.646
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = -8.13, *SE* = 11.108, *z* = -0.732, *p* = 0.464
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 4.50, *SE* = 10.219, *z* = 0.441, *p* = 0.660
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 9.49, *SE* = 14.662, *z* = 0.647, *p* = 0.518
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 17.12, *SE* = 10.181, *z* = 1.682, *p* = 0.093
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 1.73, *SE* = 11.776, *z* = 0.147, *p* = 0.883
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = 9.40, *SE* = 10.368, *z* = 0.907, *p* = 0.364
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = -0.77, *SE* = 10.882, *z* = -0.071, *p* = 0.943
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = 3.98, *SE* = 9.641, *z* = 0.413, *p* = 0.680
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = -1.56, *SE* = 10.657, *z* = -0.147, *p* = 0.883
- **SNR**: *β* = 0.52, *SE* = 0.554, *z* = 0.934, *p* = 0.350

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -11.07 | 9.99 | -1.11 | 0.268 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | -28.74 | 11.44 | -2.51 | 0.012 | 0.596 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | 4.60 | 10.01 | 0.46 | 0.646 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | 8.13 | 11.11 | 0.73 | 0.464 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Correct) | -4.50 | 10.22 | -0.44 | 0.660 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -9.49 | 14.66 | -0.65 | 0.518 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 (Correct) | -17.12 | 10.18 | -1.68 | 0.093 | 0.998 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -1.73 | 11.78 | -0.15 | 0.883 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | -9.40 | 10.37 | -0.91 | 0.364 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | 0.77 | 10.88 | 0.07 | 0.943 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Correct) | -3.98 | 9.64 | -0.41 | 0.680 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | 1.56 | 10.66 | 0.15 | 0.883 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | -17.66 | 11.02 | -1.60 | 0.109 | 0.999 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 15.67 | 8.87 | 1.77 | 0.077 | 0.995 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | 19.21 | 10.75 | 1.79 | 0.074 | 0.994 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | 6.57 | 8.92 | 0.74 | 0.461 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | 1.59 | 14.34 | 0.11 | 0.912 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | -6.05 | 9.15 | -0.66 | 0.509 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 9.35 | 11.45 | 0.82 | 0.414 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 1.67 | 9.03 | 0.19 | 0.853 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | 11.85 | 10.35 | 1.14 | 0.252 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 7.09 | 8.70 | 0.82 | 0.415 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | 12.64 | 10.18 | 1.24 | 0.215 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | 33.33 | 11.07 | 3.01 | 0.003 | 0.181 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | 36.87 | 12.06 | 3.06 | 0.002 | 0.160 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | 24.24 | 11.22 | 2.16 | 0.031 | 0.887 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | 19.25 | 15.36 | 1.25 | 0.210 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 11.61 | 11.20 | 1.04 | 0.300 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 27.01 | 12.69 | 2.13 | 0.033 | 0.904 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 19.34 | 11.34 | 1.71 | 0.088 | 0.998 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | 29.51 | 11.77 | 2.51 | 0.012 | 0.596 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 24.76 | 10.72 | 2.31 | 0.021 | 0.779 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | 30.30 | 11.61 | 2.61 | 0.009 | 0.498 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | 3.54 | 10.78 | 0.33 | 0.743 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | -9.10 | 8.89 | -1.02 | 0.306 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | -14.08 | 14.35 | -0.98 | 0.326 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | -21.72 | 9.16 | -2.37 | 0.018 | 0.729 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | -6.32 | 11.47 | -0.55 | 0.581 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | -14.00 | 9.06 | -1.55 | 0.122 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | -3.82 | 10.35 | -0.37 | 0.712 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | -8.58 | 8.70 | -0.99 | 0.324 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | -3.03 | 10.19 | -0.30 | 0.766 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | -12.63 | 10.95 | -1.15 | 0.248 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | -17.62 | 15.09 | -1.17 | 0.243 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | -25.26 | 10.92 | -2.31 | 0.021 | 0.779 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | -9.86 | 12.38 | -0.80 | 0.426 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | -17.54 | 11.09 | -1.58 | 0.114 | 0.999 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | -7.36 | 11.55 | -0.64 | 0.524 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | -12.11 | 10.44 | -1.16 | 0.246 | 1.000 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | -6.57 | 11.35 | -0.58 | 0.563 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -4.99 | 14.47 | -0.34 | 0.730 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | -12.62 | 9.20 | -1.37 | 0.170 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 2.77 | 11.62 | 0.24 | 0.811 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | -4.90 | 9.04 | -0.54 | 0.588 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | 5.28 | 10.50 | 0.50 | 0.615 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 0.52 | 8.78 | 0.06 | 0.953 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | 6.06 | 10.35 | 0.59 | 0.558 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | -7.64 | 14.47 | -0.53 | 0.598 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 7.76 | 15.54 | 0.50 | 0.618 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | 0.08 | 14.61 | 0.01 | 0.995 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | 10.26 | 14.96 | 0.69 | 0.493 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 5.51 | 14.10 | 0.39 | 0.696 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 11.05 | 14.74 | 0.75 | 0.454 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | 15.39 | 11.59 | 1.33 | 0.184 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | 7.72 | 9.32 | 0.83 | 0.408 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | 17.90 | 10.59 | 1.69 | 0.091 | 0.998 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Correct) | 13.14 | 8.97 | 1.46 | 0.143 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | 18.69 | 10.35 | 1.80 | 0.071 | 0.993 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | -7.67 | 11.77 | -0.65 | 0.514 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | 2.50 | 12.19 | 0.21 | 0.837 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | -2.25 | 11.15 | -0.20 | 0.840 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | 3.29 | 12.00 | 0.27 | 0.784 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 10.18 | 10.71 | 0.95 | 0.342 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | 5.42 | 8.98 | 0.60 | 0.546 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | 10.97 | 10.57 | 1.04 | 0.300 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | -4.76 | 10.05 | -0.47 | 0.636 | 1.000 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 0.79 | 11.04 | 0.07 | 0.943 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 5.54 | 9.82 | 0.56 | 0.572 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.857, η²_G = 0.163
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | 0.33 | 2 | = 0.993 | 0.22 [-1.08, 0.14] | small | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | -3.05 | 2 | = 0.993 | -3.08 [-2.16, -0.04] | large | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | 0.00 | 2 | = 1.000 | 0.00 [-0.49, 0.67] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | -0.65 | 2 | = 0.993 | -0.35 [-0.49, 1.08] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -0.41 | 2 | = 0.993 | -0.23 [-0.71, 0.50] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | -0.12 | 2 | = 0.993 | -0.07 [-2.55, 2.42] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | 0.11 | 2 | = 0.993 | 0.09 [-1.04, 0.22] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | -0.27 | 2 | = 0.993 | -0.30 [-0.73, 0.94] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | -0.46 | 2 | = 0.993 | -0.34 [-0.86, 0.31] | small | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | 0.81 | 2 | = 0.993 | 0.41 [-0.36, 1.25] | small | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | -1.61 | 2 | = 0.993 | -0.95 [-0.76, 0.40] | large | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | -1.06 | 2 | = 0.993 | -1.11 [-0.76, 0.78] | large | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | -3.28 | 2 | = 0.993 | -2.18 [-1.62, 0.02] | large | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -0.65 | 2 | = 0.993 | -0.16 [0.15, 1.26] | negligible | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | -0.50 | 2 | = 0.993 | -0.45 [-0.27, 1.14] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | -1.26 | 2 | = 0.993 | -0.35 [-0.22, 0.84] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | -0.27 | 2 | = 0.993 | -0.16 [-1.48, 1.72] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 0.00 | 2 | = 1.000 | 0.00 [-0.64, 0.43] | negligible | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -0.40 | 2 | = 0.993 | -0.42 [-0.53, 1.03] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | -1.64 | 2 | = 0.993 | -0.44 [-0.51, 0.48] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | 0.49 | 2 | = 0.993 | 0.23 [-0.34, 0.96] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | -3.78 | 2 | = 0.993 | -0.98 [-0.33, 0.64] | large | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | -1.58 | 2 | = 0.993 | -1.07 [-0.21, 1.13] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | 2.22 | 2 | = 0.993 | 1.74 [0.20, 2.23] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | 1.15 | 2 | = 0.993 | 1.15 [-0.51, 1.43] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | 1.61 | 2 | = 0.993 | 1.26 [-0.47, 1.11] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | 0.95 | 2 | = 0.993 | 0.82 [-2.12, 3.21] | large | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 1.29 | 2 | = 0.993 | 0.90 [-0.28, 1.36] | large | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 2.29 | 2 | = 0.993 | 1.68 [-0.46, 1.90] | large | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 1.31 | 2 | = 0.993 | 0.91 [-0.17, 1.39] | large | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | 2.08 | 2 | = 0.993 | 1.78 [0.12, 2.06] | large | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 0.60 | 2 | = 0.993 | 0.47 [-0.31, 1.19] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | 1.64 | 2 | = 0.993 | 0.80 [-0.09, 1.90] | large | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | -0.39 | 2 | = 0.993 | -0.29 [-0.62, 0.72] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | -2.00 | 2 | = 0.993 | -0.19 [-0.77, 0.25] | negligible | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | -0.14 | 2 | = 0.993 | -0.06 [-1.56, 1.63] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 0.12 | 2 | = 0.993 | 0.09 [-1.14, 0.01] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | -0.20 | 2 | = 0.993 | -0.22 [-0.76, 0.78] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | -0.82 | 2 | = 0.993 | -0.30 [-0.92, 0.15] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | 1.44 | 2 | = 0.993 | 0.35 [-0.65, 0.62] | small | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | -6.43 | 2 | = 0.912 | -0.79 [-0.67, 0.30] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | -0.97 | 2 | = 0.993 | -0.84 [-0.56, 0.71] | large | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | 0.12 | 2 | = 0.993 | 0.09 [-1.17, 0.24] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | 0.23 | 2 | = 0.993 | 0.12 [-1.81, 1.40] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 0.24 | 2 | = 0.993 | 0.26 [-1.14, 0.35] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | 0.10 | 2 | = 0.993 | 0.10 [-1.19, 0.69] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | -0.04 | 2 | = 1.000 | -0.04 [-1.03, 0.35] | negligible | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | 1.01 | 2 | = 0.993 | 0.58 [-0.54, 1.17] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | -0.62 | 2 | = 0.993 | -0.48 [-1.08, 0.31] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | -0.40 | 2 | = 0.993 | -0.46 [-1.53, 0.29] | small | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.15 | 2 | = 0.993 | 0.06 [-1.63, 1.55] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 0.28 | 2 | = 0.993 | 0.20 [-0.95, 0.15] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | 0.00 | 2 | = 1.000 | 0.00 [-0.69, 0.85] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | -0.38 | 2 | = 0.993 | -0.12 [-0.68, 0.39] | negligible | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | 2.31 | 2 | = 0.993 | 0.50 [-0.31, 1.00] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | -13.00 | 2 | = 0.457 | -0.56 [-0.30, 0.67] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | -0.65 | 2 | = 0.993 | -0.55 [-0.44, 0.85] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 0.13 | 2 | = 0.993 | 0.12 [-1.49, 1.71] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | -0.06 | 2 | = 1.000 | -0.07 [-1.61, 1.57] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | -0.25 | 2 | = 0.993 | -0.15 [-1.88, 1.36] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | 1.17 | 2 | = 0.993 | 0.30 [-2.08, 3.43] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | -1.09 | 2 | = 0.993 | -0.46 [-2.24, 1.16] | small | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | -0.45 | 2 | = 0.993 | -0.43 [-1.85, 1.38] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -0.28 | 2 | = 0.993 | -0.21 [-0.64, 0.90] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | -0.55 | 2 | = 0.993 | -0.27 [-0.40, 0.67] | small | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | 0.16 | 2 | = 0.993 | 0.14 [-0.35, 1.13] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -0.81 | 2 | = 0.993 | -0.57 [-0.13, 0.94] | medium | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | -1.09 | 2 | = 0.993 | -0.54 [-0.24, 1.08] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | -0.13 | 2 | = 0.993 | -0.13 [-0.94, 0.61] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | 0.49 | 2 | = 0.993 | 0.56 [-0.79, 1.07] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | -0.58 | 2 | = 0.993 | -0.64 [-1.00, 0.56] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | -1.15 | 2 | = 0.993 | -0.67 [-1.19, 0.69] | medium | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 1.15 | 2 | = 0.993 | 0.57 [-0.39, 0.99] | medium | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | -1.43 | 2 | = 0.993 | -0.39 [-0.26, 0.75] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | -0.55 | 2 | = 0.993 | -0.36 [-0.41, 0.96] | small | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | -4.11 | 2 | = 0.993 | -1.02 [-0.84, 0.45] | large | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | -1.11 | 2 | = 0.993 | -1.07 [-0.90, 0.65] | large | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.12 | 2 | = 0.993 | 0.10 [-0.46, 0.75] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 814.96, BIC = 866.65
- **Decrease by 1 (Correct) vs Cardinality (no change)**: *β* = 1.56, *SE* = 0.653, *z* = 2.385, *p* = 0.017
- **Decrease by 1 (Incorrect) vs Cardinality (no change)**: *β* = 2.13, *SE* = 0.743, *z* = 2.864, *p* = 0.004
- **Decrease by 2 (Correct) vs Cardinality (no change)**: *β* = 1.37, *SE* = 0.653, *z* = 2.098, *p* = 0.036
- **Decrease by 2 (Incorrect) vs Cardinality (no change)**: *β* = 5.26, *SE* = 0.720, *z* = 7.312, *p* < .001
- **Decrease by 3 (Correct) vs Cardinality (no change)**: *β* = 1.62, *SE* = 0.672, *z* = 2.413, *p* = 0.016
- **Decrease by 3 (Incorrect) vs Cardinality (no change)**: *β* = 3.44, *SE* = 0.973, *z* = 3.533, *p* < .001
- **Increase by 1 (Correct) vs Cardinality (no change)**: *β* = 1.00, *SE* = 0.665, *z* = 1.510, *p* = 0.131
- **Increase by 1 (Incorrect) vs Cardinality (no change)**: *β* = 1.50, *SE* = 0.764, *z* = 1.959, *p* = 0.050
- **Increase by 2 (Correct) vs Cardinality (no change)**: *β* = 1.19, *SE* = 0.680, *z* = 1.752, *p* = 0.080
- **Increase by 2 (Incorrect) vs Cardinality (no change)**: *β* = 3.49, *SE* = 0.706, *z* = 4.936, *p* < .001
- **Increase by 3 (Correct) vs Cardinality (no change)**: *β* = 1.44, *SE* = 0.630, *z* = 2.290, *p* = 0.022
- **Increase by 3 (Incorrect) vs Cardinality (no change)**: *β* = 3.33, *SE* = 0.692, *z* = 4.802, *p* < .001
- **SNR**: *β* = 0.29, *SE* = 0.039, *z* = 7.628, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 (Correct) | -1.56 | 0.65 | -2.38 | 0.017 | 0.570 | n.s. |
| Cardinality (no change) - Decrease by 1 (Incorrect) | -2.13 | 0.74 | -2.86 | 0.004 | 0.213 | n.s. |
| Cardinality (no change) - Decrease by 2 (Correct) | -1.37 | 0.65 | -2.10 | 0.036 | 0.784 | n.s. |
| Cardinality (no change) - Decrease by 2 (Incorrect) | -5.26 | 0.72 | -7.31 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 3 (Correct) | -1.62 | 0.67 | -2.41 | 0.016 | 0.549 | n.s. |
| Cardinality (no change) - Decrease by 3 (Incorrect) | -3.44 | 0.97 | -3.53 | < .001 | 0.027 | * |
| Cardinality (no change) - Increase by 1 (Correct) | -1.00 | 0.66 | -1.51 | 0.131 | 0.989 | n.s. |
| Cardinality (no change) - Increase by 1 (Incorrect) | -1.50 | 0.76 | -1.96 | 0.050 | 0.872 | n.s. |
| Cardinality (no change) - Increase by 2 (Correct) | -1.19 | 0.68 | -1.75 | 0.080 | 0.945 | n.s. |
| Cardinality (no change) - Increase by 2 (Incorrect) | -3.49 | 0.71 | -4.94 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 3 (Correct) | -1.44 | 0.63 | -2.29 | 0.022 | 0.633 | n.s. |
| Cardinality (no change) - Increase by 3 (Incorrect) | -3.33 | 0.69 | -4.80 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Decrease by 1 (Incorrect) | -0.57 | 0.72 | -0.80 | 0.424 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Correct) | 0.19 | 0.57 | 0.32 | 0.746 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 2 (Incorrect) | -3.70 | 0.70 | -5.29 | < .001 | < .001 | *** |
| Decrease by 1 (Correct) - Decrease by 3 (Correct) | -0.06 | 0.58 | -0.11 | 0.911 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Decrease by 3 (Incorrect) | -1.88 | 0.95 | -1.98 | 0.048 | 0.867 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Correct) | 0.55 | 0.59 | 0.93 | 0.350 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 1 (Incorrect) | 0.06 | 0.74 | 0.08 | 0.935 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Correct) | 0.36 | 0.58 | 0.62 | 0.532 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 2 (Incorrect) | -1.93 | 0.67 | -2.87 | 0.004 | 0.213 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Correct) | 0.11 | 0.56 | 0.20 | 0.840 | 1.000 | n.s. |
| Decrease by 1 (Correct) - Increase by 3 (Incorrect) | -1.77 | 0.66 | -2.67 | 0.008 | 0.346 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Correct) | 0.76 | 0.72 | 1.05 | 0.292 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 2 (Incorrect) | -3.13 | 0.78 | -4.00 | < .001 | 0.004 | ** |
| Decrease by 1 (Incorrect) - Decrease by 3 (Correct) | 0.51 | 0.73 | 0.69 | 0.487 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Decrease by 3 (Incorrect) | -1.31 | 1.02 | -1.29 | 0.197 | 0.999 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Correct) | 1.13 | 0.73 | 1.55 | 0.122 | 0.986 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 1 (Incorrect) | 0.63 | 0.82 | 0.77 | 0.442 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Correct) | 0.94 | 0.74 | 1.27 | 0.204 | 0.999 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 2 (Incorrect) | -1.36 | 0.76 | -1.78 | 0.075 | 0.939 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Correct) | 0.69 | 0.70 | 0.98 | 0.325 | 1.000 | n.s. |
| Decrease by 1 (Incorrect) - Increase by 3 (Incorrect) | -1.20 | 0.75 | -1.59 | 0.112 | 0.982 | n.s. |
| Decrease by 2 (Correct) - Decrease by 2 (Incorrect) | -3.89 | 0.70 | -5.55 | < .001 | < .001 | *** |
| Decrease by 2 (Correct) - Decrease by 3 (Correct) | -0.25 | 0.58 | -0.43 | 0.664 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Decrease by 3 (Incorrect) | -2.07 | 0.95 | -2.17 | 0.030 | 0.736 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Correct) | 0.37 | 0.59 | 0.62 | 0.535 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 1 (Incorrect) | -0.13 | 0.75 | -0.17 | 0.867 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Correct) | 0.18 | 0.59 | 0.31 | 0.760 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 2 (Incorrect) | -2.12 | 0.67 | -3.14 | 0.002 | 0.100 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Correct) | -0.07 | 0.56 | -0.13 | 0.898 | 1.000 | n.s. |
| Decrease by 2 (Correct) - Increase by 3 (Incorrect) | -1.95 | 0.66 | -2.95 | 0.003 | 0.176 | n.s. |
| Decrease by 2 (Incorrect) - Decrease by 3 (Correct) | 3.64 | 0.72 | 5.09 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Decrease by 3 (Incorrect) | 1.82 | 1.00 | 1.83 | 0.068 | 0.925 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 1 (Correct) | 4.26 | 0.71 | 5.98 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 1 (Incorrect) | 3.77 | 0.80 | 4.69 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 2 (Correct) | 4.07 | 0.73 | 5.60 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 2 (Incorrect) | 1.77 | 0.75 | 2.38 | 0.018 | 0.572 | n.s. |
| Decrease by 2 (Incorrect) - Increase by 3 (Correct) | 3.82 | 0.68 | 5.61 | < .001 | < .001 | *** |
| Decrease by 2 (Incorrect) - Increase by 3 (Incorrect) | 1.94 | 0.73 | 2.63 | 0.008 | 0.367 | n.s. |
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -1.82 | 0.96 | -1.89 | 0.059 | 0.902 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Correct) | 0.62 | 0.60 | 1.04 | 0.300 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 1 (Incorrect) | 0.13 | 0.76 | 0.17 | 0.869 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Correct) | 0.43 | 0.59 | 0.73 | 0.464 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 2 (Incorrect) | -1.87 | 0.69 | -2.72 | 0.007 | 0.307 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Correct) | 0.18 | 0.57 | 0.31 | 0.754 | 1.000 | n.s. |
| Decrease by 3 (Correct) - Increase by 3 (Incorrect) | -1.70 | 0.68 | -2.52 | 0.012 | 0.458 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Correct) | 2.44 | 0.96 | 2.54 | 0.011 | 0.447 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 1 (Incorrect) | 1.94 | 1.02 | 1.90 | 0.058 | 0.902 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Correct) | 2.25 | 0.97 | 2.32 | 0.021 | 0.615 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 2 (Incorrect) | -0.05 | 0.99 | -0.05 | 0.962 | 1.000 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Correct) | 2.00 | 0.94 | 2.13 | 0.033 | 0.766 | n.s. |
| Decrease by 3 (Incorrect) - Increase by 3 (Incorrect) | 0.11 | 0.98 | 0.12 | 0.907 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 1 (Incorrect) | -0.49 | 0.75 | -0.65 | 0.513 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Correct) | -0.19 | 0.60 | -0.31 | 0.755 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 2 (Incorrect) | -2.48 | 0.69 | -3.61 | < .001 | 0.020 | * |
| Increase by 1 (Correct) - Increase by 3 (Correct) | -0.44 | 0.58 | -0.76 | 0.449 | 1.000 | n.s. |
| Increase by 1 (Correct) - Increase by 3 (Incorrect) | -2.32 | 0.67 | -3.45 | < .001 | 0.036 | * |
| Increase by 1 (Incorrect) - Increase by 2 (Correct) | 0.30 | 0.77 | 0.40 | 0.692 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 2 (Incorrect) | -1.99 | 0.79 | -2.52 | 0.012 | 0.458 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Correct) | 0.05 | 0.73 | 0.07 | 0.942 | 1.000 | n.s. |
| Increase by 1 (Incorrect) - Increase by 3 (Incorrect) | -1.83 | 0.78 | -2.35 | 0.019 | 0.588 | n.s. |
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -2.29 | 0.70 | -3.28 | 0.001 | 0.064 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Correct) | -0.25 | 0.58 | -0.43 | 0.666 | 1.000 | n.s. |
| Increase by 2 (Correct) - Increase by 3 (Incorrect) | -2.13 | 0.69 | -3.08 | 0.002 | 0.117 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Correct) | 2.04 | 0.65 | 3.12 | 0.002 | 0.105 | n.s. |
| Increase by 2 (Incorrect) - Increase by 3 (Incorrect) | 0.16 | 0.72 | 0.23 | 0.822 | 1.000 | n.s. |
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -1.88 | 0.64 | -2.94 | 0.003 | 0.176 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 78 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.263, η²_G = 0.288
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 (Correct) | -1.17 | 2 | = 0.746 | -0.93 [-1.78, -0.34] | large | n.s. |
| Cardinality (no change) vs Decrease by 1 (Incorrect) | -1.77 | 2 | = 0.746 | -1.60 [-1.71, 0.19] | large | n.s. |
| Cardinality (no change) vs Decrease by 2 (Correct) | -1.81 | 2 | = 0.746 | -1.51 [-1.98, -0.45] | large | n.s. |
| Cardinality (no change) vs Decrease by 2 (Incorrect) | -2.17 | 2 | = 0.746 | -1.17 [-1.72, 0.06] | large | n.s. |
| Cardinality (no change) vs Decrease by 3 (Correct) | -3.01 | 2 | = 0.746 | -0.69 [-1.92, -0.36] | medium | n.s. |
| Cardinality (no change) vs Decrease by 3 (Incorrect) | -2.30 | 2 | = 0.746 | -1.23 [-4.74, 2.08] | large | n.s. |
| Cardinality (no change) vs Increase by 1 (Correct) | -0.32 | 2 | = 0.877 | -0.28 [-1.48, -0.10] | small | n.s. |
| Cardinality (no change) vs Increase by 1 (Incorrect) | -1.22 | 2 | = 0.746 | -0.81 [-1.48, 0.33] | large | n.s. |
| Cardinality (no change) vs Increase by 2 (Correct) | -1.54 | 2 | = 0.746 | -1.22 [-1.78, -0.34] | large | n.s. |
| Cardinality (no change) vs Increase by 2 (Incorrect) | -4.01 | 2 | = 0.746 | -1.42 [-2.53, -0.34] | large | n.s. |
| Cardinality (no change) vs Increase by 3 (Correct) | -2.42 | 2 | = 0.746 | -1.10 [-1.65, -0.26] | large | n.s. |
| Cardinality (no change) vs Increase by 3 (Incorrect) | -2.71 | 2 | = 0.746 | -1.12 [-2.19, -0.18] | large | n.s. |
| Decrease by 1 (Correct) vs Decrease by 1 (Incorrect) | -1.15 | 2 | = 0.746 | -1.26 [-0.48, 0.97] | large | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Correct) | -1.11 | 2 | = 0.746 | -1.28 [-0.32, 0.68] | large | n.s. |
| Decrease by 1 (Correct) vs Decrease by 2 (Incorrect) | -1.10 | 2 | = 0.746 | -0.91 [-1.12, 0.28] | large | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Correct) | 0.25 | 2 | = 0.892 | 0.20 [-0.87, 0.19] | small | n.s. |
| Decrease by 1 (Correct) vs Decrease by 3 (Incorrect) | -0.98 | 2 | = 0.746 | -0.88 [-1.99, 1.29] | large | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Correct) | 0.88 | 2 | = 0.746 | 0.99 [0.24, 1.49] | large | n.s. |
| Decrease by 1 (Correct) vs Increase by 1 (Incorrect) | -0.29 | 2 | = 0.877 | -0.28 [-0.38, 1.22] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Correct) | -0.61 | 2 | = 0.760 | -0.66 [-0.61, 0.39] | medium | n.s. |
| Decrease by 1 (Correct) vs Increase by 2 (Incorrect) | -1.43 | 2 | = 0.746 | -1.05 [-0.86, 0.43] | large | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Correct) | -0.47 | 2 | = 0.798 | -0.39 [-0.05, 0.96] | small | n.s. |
| Decrease by 1 (Correct) vs Increase by 3 (Incorrect) | -0.94 | 2 | = 0.746 | -0.77 [-0.78, 0.50] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Correct) | 1.18 | 2 | = 0.746 | 0.44 [-0.88, 0.66] | small | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 2 (Incorrect) | -0.73 | 2 | = 0.746 | -0.60 [-1.27, 0.63] | medium | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Correct) | 1.32 | 2 | = 0.746 | 1.16 [-0.84, 0.70] | large | n.s. |
| Decrease by 1 (Incorrect) vs Decrease by 3 (Incorrect) | -0.59 | 2 | = 0.760 | -0.40 [-2.90, 2.21] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Correct) | 17.80 | 2 | = 0.245 | 1.82 [-0.55, 1.01] | large | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 1 (Incorrect) | 0.71 | 2 | = 0.746 | 0.35 [-0.68, 1.51] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Correct) | 2.50 | 2 | = 0.746 | 0.43 [-1.30, 0.23] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.47 | 2 | = 0.798 | -0.46 [-1.29, 0.33] | small | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Correct) | 1.10 | 2 | = 0.746 | 0.94 [-0.67, 0.76] | large | n.s. |
| Decrease by 1 (Incorrect) vs Increase by 3 (Incorrect) | -0.41 | 2 | = 0.830 | -0.34 [-1.03, 0.66] | small | n.s. |
| Decrease by 2 (Correct) vs Decrease by 2 (Incorrect) | -0.88 | 2 | = 0.746 | -0.71 [-1.20, 0.22] | medium | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Correct) | 1.25 | 2 | = 0.746 | 1.02 [-0.84, 0.18] | large | n.s. |
| Decrease by 2 (Correct) vs Decrease by 3 (Incorrect) | -0.79 | 2 | = 0.746 | -0.58 [-2.00, 1.29] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Correct) | 6.74 | 2 | = 0.554 | 1.93 [-0.15, 0.95] | large | n.s. |
| Decrease by 2 (Correct) vs Increase by 1 (Incorrect) | 0.24 | 2 | = 0.892 | 0.15 [-0.26, 1.39] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Correct) | 0.29 | 2 | = 0.877 | 0.12 [-0.69, 0.34] | negligible | n.s. |
| Decrease by 2 (Correct) vs Increase by 2 (Incorrect) | -0.76 | 2 | = 0.746 | -0.68 [-1.01, 0.30] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Correct) | 0.97 | 2 | = 0.746 | 0.78 [-0.27, 0.71] | medium | n.s. |
| Decrease by 2 (Correct) vs Increase by 3 (Incorrect) | -0.61 | 2 | = 0.760 | -0.50 [-0.95, 0.35] | small | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Correct) | 1.49 | 2 | = 0.746 | 0.94 [-0.35, 1.04] | large | n.s. |
| Decrease by 2 (Incorrect) vs Decrease by 3 (Incorrect) | 0.71 | 2 | = 0.746 | 0.28 [-1.26, 2.05] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Correct) | 1.35 | 2 | = 0.746 | 1.10 [-0.29, 1.21] | large | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 1 (Incorrect) | 1.12 | 2 | = 0.746 | 0.72 [-0.46, 1.52] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Correct) | 0.94 | 2 | = 0.746 | 0.73 [-0.36, 1.02] | medium | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 2 (Incorrect) | 0.67 | 2 | = 0.746 | 0.31 [-0.63, 1.06] | small | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Correct) | 1.19 | 2 | = 0.746 | 0.84 [-0.16, 1.29] | large | n.s. |
| Decrease by 2 (Incorrect) vs Increase by 3 (Incorrect) | 1.46 | 2 | = 0.746 | 0.29 [-0.55, 1.16] | small | n.s. |
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | -1.53 | 2 | = 0.746 | -0.92 [-2.11, 1.23] | large | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Correct) | 0.67 | 2 | = 0.746 | 0.57 [0.10, 1.28] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 1 (Incorrect) | -0.54 | 2 | = 0.782 | -0.36 [-0.40, 1.20] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Correct) | -0.91 | 2 | = 0.746 | -0.69 [-0.30, 0.78] | medium | n.s. |
| Decrease by 3 (Correct) vs Increase by 2 (Incorrect) | -2.12 | 2 | = 0.746 | -1.07 [-0.83, 0.45] | large | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Correct) | -1.65 | 2 | = 0.746 | -0.46 [0.12, 1.19] | small | n.s. |
| Decrease by 3 (Correct) vs Increase by 3 (Incorrect) | -1.50 | 2 | = 0.746 | -0.82 [-0.69, 0.58] | large | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Correct) | 1.70 | 2 | = 0.746 | 1.17 [-1.10, 2.40] | large | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 1 (Incorrect) | 1.76 | 2 | = 0.746 | 0.57 [-1.00, 2.75] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Correct) | 0.99 | 2 | = 0.746 | 0.60 [-1.36, 1.87] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 2 (Incorrect) | 0.03 | 2 | = 0.985 | 0.02 [-2.47, 2.50] | negligible | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Correct) | 1.14 | 2 | = 0.746 | 0.77 [-1.20, 2.17] | medium | n.s. |
| Decrease by 3 (Incorrect) vs Increase by 3 (Incorrect) | 0.07 | 2 | = 0.977 | 0.03 [-1.93, 1.33] | negligible | n.s. |
| Increase by 1 (Correct) vs Increase by 1 (Incorrect) | -1.37 | 2 | = 0.746 | -0.71 [-0.61, 0.94] | medium | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Correct) | -7.01 | 2 | = 0.554 | -1.29 [-1.34, -0.14] | large | n.s. |
| Increase by 1 (Correct) vs Increase by 2 (Incorrect) | -1.46 | 2 | = 0.746 | -1.39 [-1.24, 0.27] | large | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Correct) | -1.48 | 2 | = 0.746 | -1.24 [-0.84, 0.21] | large | n.s. |
| Increase by 1 (Correct) vs Increase by 3 (Incorrect) | -1.27 | 2 | = 0.746 | -1.05 [-1.03, 0.28] | large | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Correct) | -0.20 | 2 | = 0.899 | -0.08 [-1.36, 0.28] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 2 (Incorrect) | -0.75 | 2 | = 0.746 | -0.63 [-1.81, 0.29] | medium | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Correct) | 0.19 | 2 | = 0.899 | 0.14 [-1.04, 0.53] | negligible | n.s. |
| Increase by 1 (Incorrect) vs Increase by 3 (Incorrect) | -0.82 | 2 | = 0.746 | -0.51 [-1.69, 0.36] | medium | n.s. |
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -0.75 | 2 | = 0.746 | -0.69 [-0.85, 0.51] | medium | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Correct) | 0.51 | 2 | = 0.791 | 0.39 [-0.10, 0.94] | small | n.s. |
| Increase by 2 (Correct) vs Increase by 3 (Incorrect) | -0.67 | 2 | = 0.746 | -0.52 [-0.68, 0.67] | medium | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Correct) | 1.45 | 2 | = 0.746 | 0.91 [-0.23, 1.09] | large | n.s. |
| Increase by 2 (Incorrect) vs Increase by 3 (Incorrect) | 0.02 | 2 | = 0.985 | 0.01 [-0.41, 1.18] | negligible | n.s. |
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | -1.03 | 2 | = 0.746 | -0.68 [-0.96, 0.28] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


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
