# Statistical Analysis Report: tables

**Generated:** 2025-10-15 22:45:18

---

## 1. Analysis Overview

**Total Measurements:** 432
**Number of Subjects:** 24
**Number of Conditions:** 6

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | -4.64 µV | 2.58 | 0.55 | [-10.69, -0.31] |
| 2 to 4 | 22 | -4.32 µV | 2.17 | 0.46 | [-10.88, -0.76] |
| 3 to 4 | 22 | -3.46 µV | 1.56 | 0.33 | [-7.41, -0.90] |
| 5 to 4 | 23 | -4.02 µV | 2.26 | 0.47 | [-8.57, -0.29] |
| 6 to 4 | 24 | -3.36 µV | 2.31 | 0.47 | [-9.80, -0.48] |
| Cardinality4 | 22 | -3.94 µV | 2.41 | 0.51 | [-9.95, -1.01] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | 172.61 ms | 8.07 | 1.72 | [158.31, 188.69] |
| 2 to 4 | 22 | 173.11 ms | 8.52 | 1.82 | [154.05, 195.41] |
| 3 to 4 | 22 | 169.40 ms | 7.83 | 1.67 | [146.84, 182.27] |
| 5 to 4 | 23 | 175.22 ms | 9.78 | 2.04 | [146.54, 197.33] |
| 6 to 4 | 24 | 174.19 ms | 11.38 | 2.32 | [156.51, 200.49] |
| Cardinality4 | 22 | 174.23 ms | 9.22 | 1.97 | [155.68, 192.80] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 12 | 2.21 µV | 1.62 | 0.47 | [0.11, 5.24] |
| 2 to 4 | 18 | 1.46 µV | 1.32 | 0.31 | [0.00, 5.30] |
| 3 to 4 | 14 | 2.00 µV | 1.90 | 0.51 | [0.07, 6.16] |
| 5 to 4 | 15 | 1.74 µV | 1.56 | 0.40 | [0.08, 5.02] |
| 6 to 4 | 15 | 2.13 µV | 1.60 | 0.41 | [0.33, 5.75] |
| Cardinality4 | 12 | 2.04 µV | 1.49 | 0.43 | [0.33, 4.41] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 12 | 104.90 ms | 5.55 | 1.60 | [96.00, 114.94] |
| 2 to 4 | 18 | 106.29 ms | 6.95 | 1.64 | [93.65, 117.16] |
| 3 to 4 | 14 | 104.00 ms | 6.95 | 1.86 | [93.48, 112.91] |
| 5 to 4 | 15 | 108.71 ms | 6.62 | 1.71 | [95.91, 118.82] |
| 6 to 4 | 15 | 108.70 ms | 5.44 | 1.40 | [97.62, 118.33] |
| Cardinality4 | 12 | 106.50 ms | 5.74 | 1.66 | [97.47, 116.00] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 19 | 4.02 µV | 2.83 | 0.65 | [0.83, 10.61] |
| 2 to 4 | 18 | 4.61 µV | 3.13 | 0.74 | [0.04, 11.06] |
| 3 to 4 | 17 | 3.67 µV | 2.44 | 0.59 | [0.19, 6.97] |
| 5 to 4 | 18 | 3.84 µV | 2.76 | 0.65 | [0.13, 8.93] |
| 6 to 4 | 19 | 3.41 µV | 2.46 | 0.57 | [0.05, 7.22] |
| Cardinality4 | 12 | 2.45 µV | 2.14 | 0.62 | [0.37, 7.23] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 19 | 483.35 ms | 12.96 | 2.97 | [455.96, 501.90] |
| 2 to 4 | 18 | 488.80 ms | 15.17 | 3.58 | [468.90, 523.76] |
| 3 to 4 | 17 | 483.42 ms | 16.05 | 3.89 | [454.80, 509.48] |
| 5 to 4 | 18 | 488.63 ms | 15.49 | 3.65 | [460.38, 519.49] |
| 6 to 4 | 19 | 483.97 ms | 21.85 | 5.01 | [436.74, 530.95] |
| Cardinality4 | 12 | 484.47 ms | 20.71 | 5.98 | [460.26, 525.69] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.24, *p* = 0.057, η²_G = 0.057
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.08 | 18 | = 0.556 | -0.23 [-0.68, 0.24] | small | n.s. |
| 1 to 4 vs 3 to 4 | -4.17 | 18 | = 0.009 | -0.84 [-1.04, -0.08] | large | ** |
| 1 to 4 vs 5 to 4 | -1.35 | 18 | = 0.418 | -0.30 [-0.65, 0.25] | small | n.s. |
| 1 to 4 vs 6 to 4 | -2.01 | 18 | = 0.205 | -0.52 [-0.85, 0.07] | medium | n.s. |
| 1 to 4 vs Cardinality4 | -1.92 | 18 | = 0.205 | -0.34 [-0.93, 0.05] | small | n.s. |
| 2 to 4 vs 3 to 4 | -2.43 | 18 | = 0.195 | -0.62 [-0.82, 0.12] | medium | n.s. |
| 2 to 4 vs 5 to 4 | -0.25 | 18 | = 0.815 | -0.07 [-0.46, 0.45] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.94 | 18 | = 0.570 | -0.31 [-0.71, 0.19] | small | n.s. |
| 2 to 4 vs Cardinality4 | -0.54 | 18 | = 0.691 | -0.13 [-0.63, 0.31] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | 1.84 | 18 | = 0.205 | 0.52 [-0.16, 0.75] | medium | n.s. |
| 3 to 4 vs 6 to 4 | 0.88 | 18 | = 0.570 | 0.24 [-0.39, 0.50] | small | n.s. |
| 3 to 4 vs Cardinality4 | 2.19 | 18 | = 0.205 | 0.42 [-0.12, 0.84] | small | n.s. |
| 5 to 4 vs 6 to 4 | -0.83 | 18 | = 0.570 | -0.23 [-0.65, 0.22] | small | n.s. |
| 5 to 4 vs Cardinality4 | -0.24 | 18 | = 0.815 | -0.06 [-0.49, 0.42] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 0.67 | 18 | = 0.638 | 0.16 [-0.26, 0.63] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 575.69, BIC = 598.93
- Condition effect: *β* = 0.34, *SE* = 0.504, *z* = 0.686, *p* = 0.493

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.02, *p* = 0.409, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.09 | 18 | = 0.930 | 0.02 [-0.56, 0.36] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 1.64 | 18 | = 0.575 | 0.33 [-0.00, 0.93] | small | n.s. |
| 1 to 4 vs 5 to 4 | -0.80 | 18 | = 0.817 | -0.21 [-0.63, 0.27] | small | n.s. |
| 1 to 4 vs 6 to 4 | 0.24 | 18 | = 0.930 | 0.05 [-0.50, 0.39] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | -0.18 | 18 | = 0.930 | -0.04 [-0.54, 0.40] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 1.71 | 18 | = 0.575 | 0.31 [0.03, 1.00] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.98 | 18 | = 0.731 | -0.23 [-0.63, 0.29] | small | n.s. |
| 2 to 4 vs 6 to 4 | 0.14 | 18 | = 0.930 | 0.03 [-0.48, 0.41] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | -0.21 | 18 | = 0.930 | -0.06 [-0.56, 0.38] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -1.79 | 18 | = 0.575 | -0.50 [-0.99, -0.04] | medium | n.s. |
| 3 to 4 vs 6 to 4 | -1.06 | 18 | = 0.731 | -0.24 [-0.87, 0.05] | small | n.s. |
| 3 to 4 vs Cardinality4 | -1.49 | 18 | = 0.575 | -0.36 [-0.90, 0.07] | small | n.s. |
| 5 to 4 vs 6 to 4 | 1.13 | 18 | = 0.731 | 0.24 [-0.22, 0.65] | small | n.s. |
| 5 to 4 vs Cardinality4 | 0.63 | 18 | = 0.895 | 0.17 [-0.34, 0.57] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | -0.43 | 18 | = 0.930 | -0.08 [-0.57, 0.32] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 928.23, BIC = 951.47
- Condition effect: *β* = 0.34, *SE* = 1.755, *z* = 0.192, *p* = 0.848


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.98, *p* = 0.460, η²_G = 0.092
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.35 | 3 | = 0.864 | -0.10 [-0.54, 0.90] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 1.53 | 3 | = 0.589 | 0.67 [-0.86, 0.99] | medium | n.s. |
| 1 to 4 vs 5 to 4 | 0.37 | 3 | = 0.864 | 0.29 [-0.51, 1.06] | small | n.s. |
| 1 to 4 vs 6 to 4 | 0.15 | 3 | = 0.894 | 0.03 [-0.76, 0.78] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | 1.25 | 3 | = 0.640 | 0.47 [-0.86, 0.68] | small | n.s. |
| 2 to 4 vs 3 to 4 | 4.12 | 3 | = 0.194 | 0.85 [-0.90, 0.54] | large | n.s. |
| 2 to 4 vs 5 to 4 | 0.72 | 3 | = 0.838 | 0.40 [-0.75, 0.47] | small | n.s. |
| 2 to 4 vs 6 to 4 | 1.48 | 3 | = 0.589 | 0.14 [-1.11, 0.29] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | 6.22 | 3 | = 0.126 | 0.63 [-1.06, 0.51] | medium | n.s. |
| 3 to 4 vs 5 to 4 | -0.66 | 3 | = 0.838 | -0.31 [-0.56, 1.00] | small | n.s. |
| 3 to 4 vs 6 to 4 | -2.82 | 3 | = 0.308 | -0.70 [-1.11, 0.29] | medium | n.s. |
| 3 to 4 vs Cardinality4 | -1.06 | 3 | = 0.686 | -0.21 [-1.20, 0.91] | small | n.s. |
| 5 to 4 vs 6 to 4 | -0.44 | 3 | = 0.864 | -0.28 [-0.89, 0.55] | small | n.s. |
| 5 to 4 vs Cardinality4 | 0.27 | 3 | = 0.864 | 0.13 [-0.69, 0.99] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 2.57 | 3 | = 0.308 | 0.48 [-0.82, 0.62] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 318.80, BIC = 338.43
- Condition effect: *β* = -0.70, *SE* = 0.474, *z* = -1.481, *p* = 0.139

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.96, *p* = 0.471, η²_G = 0.168
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.55 | 3 | = 0.739 | -0.34 [-1.50, 0.10] | small | n.s. |
| 1 to 4 vs 3 to 4 | 1.09 | 3 | = 0.647 | 0.31 [-1.15, 0.72] | small | n.s. |
| 1 to 4 vs 5 to 4 | -0.52 | 3 | = 0.739 | -0.41 [-1.44, 0.23] | small | n.s. |
| 1 to 4 vs 6 to 4 | -0.88 | 3 | = 0.647 | -0.59 [-1.76, 0.04] | medium | n.s. |
| 1 to 4 vs Cardinality4 | 1.28 | 3 | = 0.647 | 0.46 [-0.71, 0.83] | small | n.s. |
| 2 to 4 vs 3 to 4 | 0.82 | 3 | = 0.647 | 0.59 [-0.61, 0.82] | medium | n.s. |
| 2 to 4 vs 5 to 4 | -0.01 | 3 | = 0.989 | -0.01 [-0.83, 0.40] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -2.29 | 3 | = 0.647 | -0.28 [-0.99, 0.38] | small | n.s. |
| 2 to 4 vs Cardinality4 | 1.43 | 3 | = 0.647 | 1.05 [-0.67, 0.87] | large | n.s. |
| 3 to 4 vs 5 to 4 | -0.83 | 3 | = 0.647 | -0.64 [-1.28, 0.34] | medium | n.s. |
| 3 to 4 vs 6 to 4 | -1.01 | 3 | = 0.647 | -0.77 [-1.10, 0.30] | medium | n.s. |
| 3 to 4 vs Cardinality4 | -0.07 | 3 | = 0.989 | -0.03 [-0.92, 1.18] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.84 | 3 | = 0.647 | -0.38 [-0.58, 0.85] | small | n.s. |
| 5 to 4 vs Cardinality4 | 1.80 | 3 | = 0.647 | 1.55 [-0.43, 1.33] | large | n.s. |
| 6 to 4 vs Cardinality4 | 1.89 | 3 | = 0.647 | 1.49 [-0.03, 1.61] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 565.13, BIC = 584.77
- Condition effect: *β* = 2.21, *SE* = 2.040, *z* = 1.081, *p* = 0.280


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 1.78, *p* = 0.136, η²_G = 0.084
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.75 | 9 | = 0.642 | -0.18 [-0.76, 0.28] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 0.92 | 9 | = 0.573 | 0.29 [-0.27, 0.86] | small | n.s. |
| 1 to 4 vs 5 to 4 | 0.68 | 9 | = 0.643 | 0.19 [-0.35, 0.65] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.98 | 9 | = 0.573 | 0.31 [-0.30, 0.70] | small | n.s. |
| 1 to 4 vs Cardinality4 | 1.87 | 9 | = 0.402 | 0.73 [-0.18, 1.26] | medium | n.s. |
| 2 to 4 vs 3 to 4 | 1.43 | 9 | = 0.402 | 0.52 [-0.15, 1.01] | medium | n.s. |
| 2 to 4 vs 5 to 4 | 1.68 | 9 | = 0.402 | 0.38 [-0.14, 0.93] | small | n.s. |
| 2 to 4 vs 6 to 4 | 1.51 | 9 | = 0.402 | 0.54 [-0.13, 0.91] | medium | n.s. |
| 2 to 4 vs Cardinality4 | 3.58 | 9 | = 0.089 | 0.99 [0.16, 1.80] | large | n.s. |
| 3 to 4 vs 5 to 4 | -0.25 | 9 | = 0.868 | -0.08 [-0.67, 0.44] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 0.03 | 9 | = 0.977 | 0.01 [-0.51, 0.60] | negligible | n.s. |
| 3 to 4 vs Cardinality4 | 0.99 | 9 | = 0.573 | 0.48 [-0.37, 1.00] | small | n.s. |
| 5 to 4 vs 6 to 4 | 0.25 | 9 | = 0.868 | 0.09 [-0.41, 0.62] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | 1.67 | 9 | = 0.402 | 0.51 [-0.22, 1.20] | medium | n.s. |
| 6 to 4 vs Cardinality4 | 1.54 | 9 | = 0.402 | 0.48 [-0.30, 1.10] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 472.77, BIC = 493.85
- Condition effect: *β* = 0.66, *SE* = 0.623, *z* = 1.056, *p* = 0.291

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.91, *p* = 0.486, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.14 | 9 | = 0.663 | -0.40 [-0.92, 0.15] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.27 | 9 | = 0.915 | 0.13 [-0.56, 0.55] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -1.08 | 9 | = 0.663 | -0.59 [-0.76, 0.25] | medium | n.s. |
| 1 to 4 vs 6 to 4 | -1.74 | 9 | = 0.663 | -0.68 [-0.50, 0.50] | medium | n.s. |
| 1 to 4 vs Cardinality4 | -0.62 | 9 | = 0.805 | -0.29 [-0.78, 0.57] | small | n.s. |
| 2 to 4 vs 3 to 4 | 1.16 | 9 | = 0.663 | 0.49 [-0.33, 0.80] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.11 | 9 | = 0.915 | -0.06 [-0.42, 0.61] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.62 | 9 | = 0.805 | -0.26 [-0.31, 0.70] | small | n.s. |
| 2 to 4 vs Cardinality4 | 0.14 | 9 | = 0.915 | 0.05 [-0.55, 0.80] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -1.85 | 9 | = 0.663 | -0.67 [-0.79, 0.33] | medium | n.s. |
| 3 to 4 vs 6 to 4 | -1.50 | 9 | = 0.663 | -0.75 [-0.63, 0.48] | medium | n.s. |
| 3 to 4 vs Cardinality4 | -1.10 | 9 | = 0.663 | -0.37 [-0.82, 0.53] | small | n.s. |
| 5 to 4 vs 6 to 4 | -0.56 | 9 | = 0.805 | -0.26 [-0.35, 0.68] | small | n.s. |
| 5 to 4 vs Cardinality4 | 0.35 | 9 | = 0.914 | 0.11 [-0.63, 0.72] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 0.61 | 9 | = 0.805 | 0.29 [-0.60, 0.75] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 886.38, BIC = 907.46
- Condition effect: *β* = 5.59, *SE* = 5.296, *z* = 1.055, *p* = 0.291


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.057)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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

Within-subjects repeated-measures analyses were conducted using:
- Repeated-measures ANOVA with Greenhouse-Geisser correction for sphericity violations (ε < 0.75)
- Post-hoc pairwise t-tests with false discovery rate (FDR) correction for multiple comparisons
- Linear mixed-effects models (LMM) with random intercepts for subjects to handle missing data

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.11
- MNE-Python 1.10.1
- Statsmodels 0.14.5
- Pingouin 0.5.5

### References

- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
