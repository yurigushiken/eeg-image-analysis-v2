# Statistical Analysis Report: tables

**Generated:** 2025-10-17 04:47:12

---

## 1. Analysis Overview

**Total Measurements:** 360
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 3 to 1 | 19 | -2.34 µV | 1.98 | 0.45 | [-6.82, 0.04] |
| 3 to 2 | 24 | -3.66 µV | 2.11 | 0.43 | [-7.98, -0.23] |
| 3 to 4 | 22 | -3.31 µV | 1.52 | 0.32 | [-7.06, -0.87] |
| 3 to 5 | 22 | -3.35 µV | 2.35 | 0.50 | [-9.75, -0.66] |
| 3 to 6 | 23 | -4.69 µV | 2.44 | 0.51 | [-10.68, -1.50] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 19 | 181.69 ms | 13.67 | 3.14 | [160.44, 207.99] |
| 3 to 2 | 24 | 174.19 ms | 11.00 | 2.25 | [158.22, 206.45] |
| 3 to 4 | 22 | 168.80 ms | 9.00 | 1.92 | [143.66, 184.69] |
| 3 to 5 | 22 | 170.03 ms | 12.73 | 2.71 | [146.19, 195.21] |
| 3 to 6 | 23 | 173.04 ms | 10.57 | 2.20 | [155.52, 196.51] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 1.79 µV | 1.21 | 0.28 | [0.18, 5.03] |
| 3 to 2 | 11 | 1.64 µV | 1.45 | 0.44 | [0.11, 4.15] |
| 3 to 4 | 16 | 1.72 µV | 1.73 | 0.43 | [0.23, 6.28] |
| 3 to 5 | 14 | 1.95 µV | 1.31 | 0.35 | [0.04, 4.73] |
| 3 to 6 | 10 | 2.37 µV | 2.07 | 0.65 | [0.55, 6.94] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 106.34 ms | 4.88 | 1.15 | [95.81, 114.89] |
| 3 to 2 | 11 | 103.82 ms | 5.58 | 1.68 | [95.44, 113.56] |
| 3 to 4 | 16 | 101.02 ms | 7.25 | 1.81 | [88.70, 112.99] |
| 3 to 5 | 14 | 102.28 ms | 5.81 | 1.55 | [89.03, 111.47] |
| 3 to 6 | 10 | 101.60 ms | 5.64 | 1.78 | [93.33, 111.36] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 3.91 µV | 2.34 | 0.52 | [0.27, 9.21] |
| 3 to 2 | 18 | 4.23 µV | 3.27 | 0.77 | [0.12, 12.41] |
| 3 to 4 | 17 | 3.65 µV | 2.46 | 0.60 | [0.16, 6.99] |
| 3 to 5 | 16 | 4.19 µV | 3.00 | 0.75 | [0.58, 12.84] |
| 3 to 6 | 20 | 2.82 µV | 2.01 | 0.45 | [0.16, 8.26] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 483.17 ms | 14.13 | 3.16 | [462.53, 520.82] |
| 3 to 2 | 18 | 488.63 ms | 19.67 | 4.64 | [442.81, 529.06] |
| 3 to 4 | 17 | 485.82 ms | 16.17 | 3.92 | [451.56, 514.37] |
| 3 to 5 | 16 | 484.20 ms | 14.39 | 3.60 | [459.91, 514.62] |
| 3 to 6 | 20 | 482.95 ms | 22.26 | 4.98 | [431.90, 536.11] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 381.50, BIC = 403.11
- Effect 1 effect: *β* = -0.28, *SE* = 0.352, *z* = -0.790, *p* = 0.429
- Effect 2 effect: *β* = -0.33, *SE* = 0.346, *z* = -0.964, *p* = 0.335
- Effect 3 effect: *β* = -0.40, *SE* = 0.346, *z* = -1.144, *p* = 0.253
- Effect 4 effect: *β* = -0.97, *SE* = 0.365, *z* = -2.654, *p* = 0.008
- Effect 5 effect: *β* = -0.56, *SE* = 0.051, *z* = -10.958, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.94, *p* = 0.001, η²_G = 0.121
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 3.32 | 17 | = 0.020 | 0.86 [0.21, 1.31] | large | * |
| 3 to 1 vs 3 to 4 | 2.80 | 17 | = 0.041 | 0.61 [0.11, 1.21] | medium | * |
| 3 to 1 vs 3 to 5 | 1.29 | 17 | = 0.266 | 0.42 [-0.20, 0.81] | small | n.s. |
| 3 to 1 vs 3 to 6 | 3.61 | 17 | = 0.020 | 1.02 [0.27, 1.43] | large | * |
| 3 to 2 vs 3 to 4 | -1.65 | 17 | = 0.195 | -0.36 [-0.86, 0.06] | small | n.s. |
| 3 to 2 vs 3 to 5 | -1.31 | 17 | = 0.266 | -0.35 [-0.69, 0.21] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.07 | 17 | = 0.332 | 0.24 [-0.04, 0.86] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.25 | 17 | = 0.807 | -0.07 [-0.43, 0.46] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 2.29 | 17 | = 0.071 | 0.59 [0.20, 1.19] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 2.47 | 17 | = 0.061 | 0.54 [0.16, 1.14] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 826.21, BIC = 847.81
- Effect 1 effect: *β* = -6.80, *SE* = 2.573, *z* = -2.642, *p* = 0.008
- Effect 2 effect: *β* = -10.90, *SE* = 2.528, *z* = -4.312, *p* < .001
- Effect 3 effect: *β* = -9.68, *SE* = 2.526, *z* = -3.834, *p* < .001
- Effect 4 effect: *β* = -6.87, *SE* = 2.667, *z* = -2.575, *p* = 0.010
- Effect 5 effect: *β* = -0.36, *SE* = 0.380, *z* = -0.940, *p* = 0.347

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.35, *p* < .001, η²_G = 0.124
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 2.97 | 17 | = 0.029 | 0.94 [0.15, 1.22] | large | * |
| 3 to 1 vs 3 to 4 | 3.87 | 17 | = 0.012 | 0.97 [0.32, 1.50] | large | * |
| 3 to 1 vs 3 to 5 | 3.15 | 17 | = 0.029 | 0.71 [0.18, 1.30] | medium | * |
| 3 to 1 vs 3 to 6 | 2.68 | 17 | = 0.039 | 0.69 [0.09, 1.18] | medium | * |
| 3 to 2 vs 3 to 4 | 0.68 | 17 | = 0.700 | 0.16 [-0.16, 0.74] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -0.23 | 17 | = 0.820 | -0.06 [-0.32, 0.57] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | -0.59 | 17 | = 0.700 | -0.20 [-0.45, 0.41] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.82 | 17 | = 0.700 | -0.17 [-0.59, 0.31] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -1.24 | 17 | = 0.467 | -0.31 [-0.81, 0.10] | small | n.s. |
| 3 to 5 vs 3 to 6 | -0.45 | 17 | = 0.728 | -0.10 [-0.64, 0.25] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 206.92, BIC = 224.79
- Effect 1 effect: *β* = 0.06, *SE* = 0.320, *z* = 0.181, *p* = 0.856
- Effect 2 effect: *β* = 0.29, *SE* = 0.296, *z* = 0.981, *p* = 0.327
- Effect 3 effect: *β* = -0.17, *SE* = 0.298, *z* = -0.573, *p* = 0.566
- Effect 4 effect: *β* = 0.17, *SE* = 0.336, *z* = 0.516, *p* = 0.606
- Effect 5 effect: *β* = 0.52, *SE* = 0.061, *z* = 8.532, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.73, *p* = 0.235, η²_G = 0.279
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -3.76 | 2 | = 0.550 | -2.70 [-0.59, 0.76] | large | n.s. |
| 3 to 1 vs 3 to 4 | -1.53 | 2 | = 0.550 | -1.33 [-0.75, 0.60] | large | n.s. |
| 3 to 1 vs 3 to 5 | -1.80 | 2 | = 0.550 | -1.53 [-0.88, 0.41] | large | n.s. |
| 3 to 1 vs 3 to 6 | -1.70 | 2 | = 0.550 | -1.44 [-1.08, 0.49] | large | n.s. |
| 3 to 2 vs 3 to 4 | -0.32 | 2 | = 0.866 | -0.27 [-1.25, 0.48] | small | n.s. |
| 3 to 2 vs 3 to 5 | -0.17 | 2 | = 0.879 | -0.11 [-1.03, 0.83] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | -0.70 | 2 | = 0.792 | -0.51 [-1.17, 0.54] | medium | n.s. |
| 3 to 4 vs 3 to 5 | 0.43 | 2 | = 0.866 | 0.16 [-0.19, 1.51] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -0.83 | 2 | = 0.792 | -0.22 [-1.47, 0.70] | small | n.s. |
| 3 to 5 vs 3 to 6 | -1.49 | 2 | = 0.550 | -0.38 [-1.56, 0.98] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 445.48, BIC = 463.36
- Effect 1 effect: *β* = -2.97, *SE* = 1.899, *z* = -1.566, *p* = 0.117
- Effect 2 effect: *β* = -4.60, *SE* = 1.746, *z* = -2.635, *p* = 0.008
- Effect 3 effect: *β* = -4.37, *SE* = 1.755, *z* = -2.488, *p* = 0.013
- Effect 4 effect: *β* = -4.76, *SE* = 1.977, *z* = -2.410, *p* = 0.016
- Effect 5 effect: *β* = 0.26, *SE* = 0.363, *z* = 0.711, *p* = 0.477

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.06, *p* = 0.992, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.04 | 2 | = 0.973 | -0.04 [-0.42, 0.94] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | -0.08 | 2 | = 0.973 | -0.08 [-0.40, 0.96] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | -0.25 | 2 | = 0.973 | -0.27 [-0.16, 1.20] | small | n.s. |
| 3 to 1 vs 3 to 6 | 0.04 | 2 | = 0.973 | 0.05 [-0.45, 1.13] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | -0.52 | 2 | = 0.973 | -0.07 [-1.34, 0.42] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -1.54 | 2 | = 0.877 | -0.38 [-0.86, 0.99] | small | n.s. |
| 3 to 2 vs 3 to 6 | 0.62 | 2 | = 0.973 | 0.12 [-0.33, 1.47] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -2.70 | 2 | = 0.877 | -0.30 [-0.94, 0.61] | small | n.s. |
| 3 to 4 vs 3 to 6 | 0.98 | 2 | = 0.973 | 0.18 [-0.71, 1.46] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 1.73 | 2 | = 0.877 | 0.43 [-1.30, 1.18] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 382.61, BIC = 402.69
- Effect 1 effect: *β* = 1.08, *SE* = 0.502, *z* = 2.154, *p* = 0.031
- Effect 2 effect: *β* = 0.02, *SE* = 0.507, *z* = 0.038, *p* = 0.970
- Effect 3 effect: *β* = 0.58, *SE* = 0.513, *z* = 1.139, *p* = 0.255
- Effect 4 effect: *β* = -0.10, *SE* = 0.500, *z* = -0.197, *p* = 0.844
- Effect 5 effect: *β* = 0.20, *SE* = 0.039, *z* = 5.115, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.390, η²_G = 0.042
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.40 | 10 | = 0.642 | -0.40 [-0.70, 0.34] | small | n.s. |
| 3 to 1 vs 3 to 4 | -0.02 | 10 | = 0.986 | -0.00 [-0.38, 0.74] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | -0.77 | 10 | = 0.776 | -0.20 [-0.64, 0.47] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 0.36 | 10 | = 0.806 | 0.14 [-0.17, 0.85] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 1.41 | 10 | = 0.642 | 0.43 [-0.11, 1.05] | small | n.s. |
| 3 to 2 vs 3 to 5 | 0.63 | 10 | = 0.776 | 0.19 [-0.41, 0.76] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 2.39 | 10 | = 0.382 | 0.61 [0.08, 1.21] | medium | n.s. |
| 3 to 4 vs 3 to 5 | -0.64 | 10 | = 0.776 | -0.21 [-0.80, 0.37] | small | n.s. |
| 3 to 4 vs 3 to 6 | 0.49 | 10 | = 0.789 | 0.17 [-0.26, 0.83] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.96 | 10 | = 0.776 | 0.37 [-0.22, 0.92] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 789.61, BIC = 809.69
- Effect 1 effect: *β* = 4.68, *SE* = 5.353, *z* = 0.874, *p* = 0.382
- Effect 2 effect: *β* = 2.52, *SE* = 5.356, *z* = 0.471, *p* = 0.638
- Effect 3 effect: *β* = 2.06, *SE* = 5.444, *z* = 0.379, *p* = 0.705
- Effect 4 effect: *β* = -0.95, *SE* = 5.328, *z* = -0.178, *p* = 0.859
- Effect 5 effect: *β* = 0.03, *SE* = 0.384, *z* = 0.068, *p* = 0.946

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.965, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 0.51 | 10 | = 0.957 | 0.11 [-0.63, 0.40] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | -0.06 | 10 | = 0.957 | -0.02 [-0.69, 0.43] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | -0.27 | 10 | = 0.957 | -0.13 [-0.54, 0.56] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 0.41 | 10 | = 0.957 | 0.15 [-0.47, 0.52] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | -0.30 | 10 | = 0.957 | -0.13 [-0.51, 0.60] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -0.54 | 10 | = 0.957 | -0.24 [-0.59, 0.56] | small | n.s. |
| 3 to 2 vs 3 to 6 | 0.06 | 10 | = 0.957 | 0.02 [-0.37, 0.67] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.40 | 10 | = 0.957 | -0.10 [-0.62, 0.53] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.34 | 10 | = 0.957 | 0.17 [-0.39, 0.68] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.65 | 10 | = 0.957 | 0.33 [-0.18, 0.97] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 3 to 2 (*d* = 0.86)
  - 3 to 1 showed greater amplitude than 3 to 4 (*d* = 0.61)
  - 3 to 1 showed greater amplitude than 3 to 6 (*d* = 1.02)
**N1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 3 to 1 showed greater latency than 3 to 2 (*d* = 0.94)
  - 3 to 1 showed greater latency than 3 to 4 (*d* = 0.97)
  - 3 to 1 showed greater latency than 3 to 5 (*d* = 0.71)
  - 3 to 1 showed greater latency than 3 to 6 (*d* = 0.69)

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
