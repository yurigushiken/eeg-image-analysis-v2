# Statistical Analysis Report: tables

**Generated:** 2025-10-17 17:22:06

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
| 2 to 1 | 16 | -2.53 µV | 2.27 | 0.57 | [-8.78, -0.03] |
| 3 to 2 | 23 | -4.00 µV | 2.15 | 0.45 | [-8.20, -0.85] |
| 4 to 3 | 22 | -3.60 µV | 1.53 | 0.33 | [-7.59, -1.27] |
| 5 to 4 | 23 | -4.08 µV | 2.32 | 0.48 | [-8.92, -0.28] |
| 6 to 5 | 24 | -3.97 µV | 1.93 | 0.39 | [-8.87, -0.40] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 177.84 ms | 8.63 | 2.16 | [162.16, 195.53] |
| 3 to 2 | 23 | 171.60 ms | 7.65 | 1.59 | [155.98, 192.06] |
| 4 to 3 | 22 | 168.52 ms | 7.03 | 1.50 | [147.89, 179.12] |
| 5 to 4 | 23 | 173.94 ms | 9.25 | 1.93 | [147.04, 195.48] |
| 6 to 5 | 24 | 172.81 ms | 9.04 | 1.84 | [160.07, 194.33] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 3.17 µV | 2.28 | 0.54 | [1.13, 8.73] |
| 3 to 2 | 12 | 1.61 µV | 1.43 | 0.41 | [-0.06, 4.03] |
| 4 to 3 | 13 | 2.27 µV | 1.99 | 0.55 | [-0.07, 6.21] |
| 5 to 4 | 15 | 1.89 µV | 1.63 | 0.42 | [0.24, 5.45] |
| 6 to 5 | 12 | 2.19 µV | 2.19 | 0.63 | [0.10, 7.74] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 109.81 ms | 2.80 | 0.66 | [104.85, 114.00] |
| 3 to 2 | 12 | 106.53 ms | 4.29 | 1.24 | [97.59, 112.58] |
| 4 to 3 | 13 | 107.68 ms | 5.82 | 1.61 | [96.11, 118.56] |
| 5 to 4 | 15 | 109.19 ms | 5.19 | 1.34 | [98.09, 116.75] |
| 6 to 5 | 12 | 106.79 ms | 4.30 | 1.24 | [97.20, 114.95] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 4.12 µV | 2.65 | 0.61 | [0.43, 9.96] |
| 3 to 2 | 18 | 4.33 µV | 3.32 | 0.78 | [0.11, 13.02] |
| 4 to 3 | 17 | 3.77 µV | 2.45 | 0.59 | [0.28, 7.83] |
| 5 to 4 | 18 | 3.96 µV | 2.85 | 0.67 | [0.12, 9.03] |
| 6 to 5 | 14 | 2.34 µV | 1.92 | 0.51 | [-0.00, 6.11] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 496.02 ms | 13.04 | 2.99 | [463.81, 523.42] |
| 3 to 2 | 18 | 493.53 ms | 16.61 | 3.92 | [447.07, 526.36] |
| 4 to 3 | 17 | 492.34 ms | 17.18 | 4.17 | [453.57, 515.46] |
| 5 to 4 | 18 | 494.36 ms | 14.48 | 3.41 | [462.72, 515.37] |
| 6 to 5 | 14 | 501.96 ms | 25.02 | 6.69 | [446.79, 535.78] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 369.08, BIC = 390.54
- Effect 1 effect: *β* = -0.73, *SE* = 0.362, *z* = -2.004, *p* = 0.045
- Effect 2 effect: *β* = -0.72, *SE* = 0.353, *z* = -2.054, *p* = 0.040
- Effect 3 effect: *β* = -0.72, *SE* = 0.365, *z* = -1.971, *p* = 0.049
- Effect 4 effect: *β* = -1.07, *SE* = 0.352, *z* = -3.043, *p* = 0.002
- Effect 5 effect: *β* = -0.45, *SE* = 0.042, *z* = -10.646, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.76, *p* = 0.002, η²_G = 0.139
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 4.23 | 15 | = 0.007 | 0.95 [0.39, 1.72] | large | ** |
| 2 to 1 vs 4 to 3 | 2.70 | 15 | = 0.041 | 0.73 [0.08, 1.27] | medium | * |
| 2 to 1 vs 5 to 4 | 3.01 | 15 | = 0.041 | 0.97 [0.15, 1.36] | large | * |
| 2 to 1 vs 6 to 5 | 2.75 | 15 | = 0.041 | 0.87 [0.09, 1.28] | large | * |
| 3 to 2 vs 4 to 3 | -1.49 | 15 | = 0.315 | -0.36 [-0.77, 0.14] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.08 | 15 | = 0.934 | 0.02 [-0.40, 0.47] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -0.42 | 15 | = 0.752 | -0.12 [-0.43, 0.43] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 1.11 | 15 | = 0.473 | 0.38 [-0.19, 0.72] | small | n.s. |
| 4 to 3 vs 6 to 5 | 0.94 | 15 | = 0.519 | 0.24 [-0.17, 0.74] | small | n.s. |
| 5 to 4 vs 6 to 5 | -0.55 | 15 | = 0.742 | -0.14 [-0.47, 0.39] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 757.14, BIC = 778.60
- Effect 1 effect: *β* = -4.94, *SE* = 2.249, *z* = -2.196, *p* = 0.028
- Effect 2 effect: *β* = -8.15, *SE* = 2.204, *z* = -3.697, *p* < .001
- Effect 3 effect: *β* = -2.50, *SE* = 2.264, *z* = -1.103, *p* = 0.270
- Effect 4 effect: *β* = -4.30, *SE* = 2.188, *z* = -1.967, *p* = 0.049
- Effect 5 effect: *β* = -0.53, *SE* = 0.256, *z* = -2.050, *p* = 0.040

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.37, *p* < .001, η²_G = 0.145
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.63 | 15 | = 0.048 | 0.84 [0.07, 1.24] | large | * |
| 2 to 1 vs 4 to 3 | 5.28 | 15 | < .001 | 1.13 [0.59, 2.05] | large | *** |
| 2 to 1 vs 5 to 4 | 1.63 | 15 | = 0.203 | 0.47 [-0.15, 0.96] | small | n.s. |
| 2 to 1 vs 6 to 5 | 2.95 | 15 | = 0.033 | 0.59 [0.14, 1.34] | medium | * |
| 3 to 2 vs 4 to 3 | 1.34 | 15 | = 0.251 | 0.43 [-0.21, 0.69] | small | n.s. |
| 3 to 2 vs 5 to 4 | -1.55 | 15 | = 0.203 | -0.42 [-0.70, 0.18] | small | n.s. |
| 3 to 2 vs 6 to 5 | -0.38 | 15 | = 0.712 | -0.13 [-0.50, 0.37] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -3.89 | 15 | = 0.007 | -0.79 [-0.99, -0.04] | medium | ** |
| 4 to 3 vs 6 to 5 | -1.93 | 15 | = 0.146 | -0.48 [-0.88, 0.05] | small | n.s. |
| 5 to 4 vs 6 to 5 | 0.75 | 15 | = 0.514 | 0.21 [-0.30, 0.57] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 220.45, BIC = 238.43
- Effect 1 effect: *β* = -0.17, *SE* = 0.385, *z* = -0.442, *p* = 0.659
- Effect 2 effect: *β* = 0.10, *SE* = 0.363, *z* = 0.266, *p* = 0.791
- Effect 3 effect: *β* = -0.14, *SE* = 0.354, *z* = -0.385, *p* = 0.700
- Effect 4 effect: *β* = -0.05, *SE* = 0.373, *z* = -0.125, *p* = 0.901
- Effect 5 effect: *β* = 0.77, *SE* = 0.073, *z* = 10.557, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.25, *p* = 0.329, η²_G = 0.147
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.70 | 4 | = 0.687 | 0.97 [0.01, 1.67] | large | n.s. |
| 2 to 1 vs 4 to 3 | 1.21 | 4 | = 0.687 | 0.55 [-0.18, 1.26] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 1.07 | 4 | = 0.687 | 0.74 [-0.26, 1.06] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 1.83 | 4 | = 0.687 | 0.56 [0.09, 1.81] | medium | n.s. |
| 3 to 2 vs 4 to 3 | -1.09 | 4 | = 0.687 | -0.73 [-1.54, 0.17] | medium | n.s. |
| 3 to 2 vs 5 to 4 | -0.52 | 4 | = 0.756 | -0.34 [-0.97, 0.58] | small | n.s. |
| 3 to 2 vs 6 to 5 | -0.66 | 4 | = 0.756 | -0.38 [-1.17, 0.70] | small | n.s. |
| 4 to 3 vs 5 to 4 | 0.60 | 4 | = 0.756 | 0.32 [-0.54, 1.17] | small | n.s. |
| 4 to 3 vs 6 to 5 | 0.44 | 4 | = 0.756 | 0.12 [-0.58, 1.12] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.20 | 4 | = 0.852 | -0.12 [-0.78, 0.65] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 416.25, BIC = 434.24
- Effect 1 effect: *β* = -2.75, *SE* = 1.568, *z* = -1.757, *p* = 0.079
- Effect 2 effect: *β* = -1.71, *SE* = 1.483, *z* = -1.154, *p* = 0.249
- Effect 3 effect: *β* = -0.14, *SE* = 1.446, *z* = -0.100, *p* = 0.920
- Effect 4 effect: *β* = -2.64, *SE* = 1.524, *z* = -1.730, *p* = 0.084
- Effect 5 effect: *β* = 0.27, *SE* = 0.285, *z* = 0.957, *p* = 0.338

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.18, *p* = 0.945, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.15 | 4 | = 0.985 | -0.08 [-0.26, 1.25] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | -0.42 | 4 | = 0.985 | -0.23 [-0.45, 0.91] | small | n.s. |
| 2 to 1 vs 5 to 4 | -0.02 | 4 | = 0.985 | -0.01 [-0.46, 0.82] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | -0.57 | 4 | = 0.985 | -0.26 [-0.20, 1.35] | small | n.s. |
| 3 to 2 vs 4 to 3 | -0.52 | 4 | = 0.985 | -0.16 [-1.66, 0.10] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.20 | 4 | = 0.985 | 0.07 [-1.00, 0.56] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -1.25 | 4 | = 0.985 | -0.21 [-0.77, 1.09] | small | n.s. |
| 4 to 3 vs 5 to 4 | 0.89 | 4 | = 0.985 | 0.21 [-1.19, 0.53] | small | n.s. |
| 4 to 3 vs 6 to 5 | -0.22 | 4 | = 0.985 | -0.07 [-0.96, 0.71] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.68 | 4 | = 0.985 | -0.25 [-0.34, 1.15] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 338.40, BIC = 358.04
- Effect 1 effect: *β* = 0.47, *SE* = 0.427, *z* = 1.109, *p* = 0.267
- Effect 2 effect: *β* = -0.79, *SE* = 0.430, *z* = -1.828, *p* = 0.068
- Effect 3 effect: *β* = -0.28, *SE* = 0.421, *z* = -0.675, *p* = 0.500
- Effect 4 effect: *β* = -1.33, *SE* = 0.471, *z* = -2.822, *p* = 0.005
- Effect 5 effect: *β* = 0.53, *SE* = 0.050, *z* = 10.625, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.38, *p* = 0.018, η²_G = 0.182
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.28 | 10 | = 0.783 | -0.11 [-0.61, 0.46] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 1.34 | 10 | = 0.352 | 0.41 [-0.28, 0.80] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.33 | 10 | = 0.783 | 0.14 [-0.42, 0.62] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 2.79 | 10 | = 0.079 | 1.35 [0.11, 1.50] | large | n.s. |
| 3 to 2 vs 4 to 3 | 1.44 | 10 | = 0.352 | 0.46 [-0.15, 1.01] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.64 | 10 | = 0.669 | 0.22 [-0.38, 0.69] | small | n.s. |
| 3 to 2 vs 6 to 5 | 2.67 | 10 | = 0.079 | 1.24 [0.04, 1.49] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.73 | 10 | = 0.669 | -0.24 [-0.69, 0.42] | small | n.s. |
| 4 to 3 vs 6 to 5 | 1.80 | 10 | = 0.256 | 0.86 [-0.10, 1.19] | large | n.s. |
| 5 to 4 vs 6 to 5 | 3.33 | 10 | = 0.076 | 1.09 [0.18, 1.61] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 733.80, BIC = 753.44
- Effect 1 effect: *β* = -1.95, *SE* = 4.592, *z* = -0.424, *p* = 0.671
- Effect 2 effect: *β* = -3.57, *SE* = 4.629, *z* = -0.771, *p* = 0.441
- Effect 3 effect: *β* = -0.78, *SE* = 4.545, *z* = -0.171, *p* = 0.864
- Effect 4 effect: *β* = 8.68, *SE* = 5.068, *z* = 1.712, *p* = 0.087
- Effect 5 effect: *β* = 0.10, *SE* = 0.520, *z* = 0.199, *p* = 0.842

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.98, *p* = 0.008, η²_G = 0.177
- Greenhouse-Geisser corrected: *p* = 0.025 (ε = 0.614)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.33 | 10 | = 0.748 | 0.06 [-0.57, 0.50] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 0.57 | 10 | = 0.728 | 0.20 [-0.46, 0.61] | negligible | n.s. |
| 2 to 1 vs 5 to 4 | -0.88 | 10 | = 0.644 | -0.29 [-0.49, 0.54] | small | n.s. |
| 2 to 1 vs 6 to 5 | -2.92 | 10 | = 0.093 | -1.01 [-1.00, 0.25] | large | n.s. |
| 3 to 2 vs 4 to 3 | 0.35 | 10 | = 0.748 | 0.12 [-0.48, 0.63] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.78 | 10 | = 0.644 | -0.28 [-0.64, 0.43] | small | n.s. |
| 3 to 2 vs 6 to 5 | -2.57 | 10 | = 0.093 | -0.93 [-1.03, 0.29] | large | n.s. |
| 4 to 3 vs 5 to 4 | -1.38 | 10 | = 0.397 | -0.40 [-0.81, 0.31] | small | n.s. |
| 4 to 3 vs 6 to 5 | -2.61 | 10 | = 0.093 | -0.99 [-1.40, -0.04] | large | n.s. |
| 5 to 4 vs 6 to 5 | -1.95 | 10 | = 0.199 | -0.85 [-1.15, 0.13] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 0.95)
  - 2 to 1 showed greater amplitude than 4 to 3 (*d* = 0.73)
  - 2 to 1 showed greater amplitude than 5 to 4 (*d* = 0.97)
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 0.87)
**N1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater latency than 3 to 2 (*d* = 0.84)
  - 2 to 1 showed greater latency than 4 to 3 (*d* = 1.13)
  - 2 to 1 showed greater latency than 6 to 5 (*d* = 0.59)
  - 4 to 3 showed smaller latency than 5 to 4 (*d* = -0.79)
**P3b amplitude:** Significant main effect of condition (*p* = 0.018) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.008) (no significant pairwise comparisons)

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
