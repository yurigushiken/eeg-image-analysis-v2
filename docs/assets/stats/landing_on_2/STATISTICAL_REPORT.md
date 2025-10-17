# Statistical Analysis Report: tables

**Generated:** 2025-10-17 03:14:27

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
| 3 to 2 | 24 | -3.67 µV | 2.08 | 0.42 | [-8.19, -0.60] |
| 4 to 2 | 24 | -4.03 µV | 2.42 | 0.49 | [-9.04, -0.62] |
| 5 to 2 | 24 | -4.40 µV | 2.45 | 0.50 | [-9.27, -0.25] |
| Cardinality2 | 22 | -3.10 µV | 1.79 | 0.38 | [-7.17, -0.12] |
| increasing 1 to 2 | 21 | -3.38 µV | 1.76 | 0.38 | [-7.60, -0.36] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 24 | 177.49 ms | 11.02 | 2.25 | [160.15, 207.30] |
| 4 to 2 | 24 | 178.15 ms | 9.66 | 1.97 | [161.63, 204.46] |
| 5 to 2 | 24 | 175.41 ms | 9.41 | 1.92 | [155.87, 193.65] |
| Cardinality2 | 22 | 176.30 ms | 13.10 | 2.79 | [157.20, 197.73] |
| increasing 1 to 2 | 21 | 174.50 ms | 11.37 | 2.48 | [155.51, 206.27] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 11 | 1.80 µV | 1.47 | 0.44 | [-0.06, 4.06] |
| 4 to 2 | 14 | 2.01 µV | 1.01 | 0.27 | [0.89, 3.93] |
| 5 to 2 | 16 | 2.19 µV | 1.71 | 0.43 | [0.19, 5.35] |
| Cardinality2 | 13 | 2.11 µV | 1.84 | 0.51 | [0.55, 6.85] |
| increasing 1 to 2 | 13 | 1.09 µV | 1.19 | 0.33 | [0.13, 4.51] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 11 | 110.55 ms | 2.95 | 0.89 | [104.24, 113.59] |
| 4 to 2 | 14 | 113.05 ms | 1.20 | 0.32 | [111.02, 114.63] |
| 5 to 2 | 16 | 111.93 ms | 3.37 | 0.84 | [105.01, 118.47] |
| Cardinality2 | 13 | 112.52 ms | 2.84 | 0.79 | [107.32, 117.60] |
| increasing 1 to 2 | 13 | 112.21 ms | 3.65 | 1.01 | [106.47, 117.94] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 4.14 µV | 3.24 | 0.76 | [0.05, 12.11] |
| 4 to 2 | 19 | 3.37 µV | 2.46 | 0.57 | [0.11, 7.50] |
| 5 to 2 | 19 | 3.50 µV | 2.48 | 0.57 | [0.49, 10.08] |
| Cardinality2 | 11 | 2.64 µV | 1.81 | 0.55 | [0.77, 7.26] |
| increasing 1 to 2 | 17 | 3.42 µV | 2.85 | 0.69 | [0.03, 10.36] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 2 | 18 | 487.43 ms | 21.86 | 5.15 | [441.16, 530.94] |
| 4 to 2 | 19 | 477.00 ms | 18.30 | 4.20 | [431.61, 504.08] |
| 5 to 2 | 19 | 476.74 ms | 19.19 | 4.40 | [426.64, 514.84] |
| Cardinality2 | 11 | 473.22 ms | 14.15 | 4.27 | [443.18, 497.35] |
| increasing 1 to 2 | 17 | 485.62 ms | 21.75 | 5.28 | [450.23, 532.69] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 418.32, BIC = 440.28
- Effect 1 effect: *β* = -0.69, *SE* = 0.341, *z* = -2.033, *p* = 0.042
- Effect 2 effect: *β* = -0.65, *SE* = 0.338, *z* = -1.925, *p* = 0.054
- Effect 3 effect: *β* = 0.04, *SE* = 0.358, *z* = 0.100, *p* = 0.920
- Effect 4 effect: *β* = 0.26, *SE* = 0.353, *z* = 0.736, *p* = 0.461
- Effect 5 effect: *β* = -0.44, *SE* = 0.054, *z* = -8.032, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.50, *p* = 0.011, η²_G = 0.072
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 1.05 | 18 | = 0.343 | 0.23 [-0.24, 0.62] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.20 | 18 | = 0.343 | 0.27 [-0.08, 0.79] | small | n.s. |
| 3 to 2 vs Cardinality2 | -2.08 | 18 | = 0.131 | -0.45 [-0.83, 0.09] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | -1.68 | 18 | = 0.184 | -0.25 [-0.89, 0.06] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.21 | 18 | = 0.835 | 0.05 [-0.26, 0.59] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | -2.46 | 18 | = 0.096 | -0.66 [-0.92, 0.01] | medium | n.s. |
| 4 to 2 vs increasing 1 to 2 | -1.83 | 18 | = 0.169 | -0.48 [-0.90, 0.05] | small | n.s. |
| 5 to 2 vs Cardinality2 | -2.75 | 18 | = 0.096 | -0.69 [-1.10, -0.13] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | -2.38 | 18 | = 0.096 | -0.52 [-1.02, -0.05] | medium | n.s. |
| Cardinality2 vs increasing 1 to 2 | 1.06 | 18 | = 0.343 | 0.23 [-0.25, 0.73] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 852.63, BIC = 874.59
- Effect 1 effect: *β* = 0.38, *SE* = 2.241, *z* = 0.171, *p* = 0.864
- Effect 2 effect: *β* = -2.02, *SE* = 2.225, *z* = -0.906, *p* = 0.365
- Effect 3 effect: *β* = -1.95, *SE* = 2.353, *z* = -0.827, *p* = 0.408
- Effect 4 effect: *β* = -2.32, *SE* = 2.322, *z* = -1.001, *p* = 0.317
- Effect 5 effect: *β* = -0.36, *SE* = 0.356, *z* = -1.012, *p* = 0.312

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.30, *p* = 0.878, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.801 (ε = 0.657)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -1.18 | 18 | = 0.916 | -0.29 [-0.49, 0.36] | small | n.s. |
| 3 to 2 vs 5 to 2 | -0.64 | 18 | = 0.916 | -0.11 [-0.22, 0.63] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | -0.67 | 18 | = 0.916 | -0.14 [-0.37, 0.52] | negligible | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.11 | 18 | = 0.916 | -0.02 [-0.33, 0.58] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.67 | 18 | = 0.916 | 0.16 [-0.19, 0.67] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | 0.22 | 18 | = 0.916 | 0.06 [-0.35, 0.54] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 0.76 | 18 | = 0.916 | 0.20 [-0.19, 0.74] | small | n.s. |
| 5 to 2 vs Cardinality2 | -0.22 | 18 | = 0.916 | -0.05 [-0.40, 0.49] | negligible | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.25 | 18 | = 0.916 | 0.07 [-0.48, 0.43] | negligible | n.s. |
| Cardinality2 vs increasing 1 to 2 | 0.50 | 18 | = 0.916 | 0.10 [-0.37, 0.60] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 189.19, BIC = 206.83
- Effect 1 effect: *β* = 0.15, *SE* = 0.329, *z* = 0.452, *p* = 0.651
- Effect 2 effect: *β* = -0.17, *SE* = 0.329, *z* = -0.513, *p* = 0.608
- Effect 3 effect: *β* = 0.18, *SE* = 0.340, *z* = 0.525, *p* = 0.600
- Effect 4 effect: *β* = -0.41, *SE* = 0.340, *z* = -1.208, *p* = 0.227
- Effect 5 effect: *β* = 0.85, *SE* = 0.084, *z* = 10.230, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.249, η²_G = 0.235
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 0.27 | 4 | = 0.799 | 0.22 [-0.70, 0.83] | small | n.s. |
| 3 to 2 vs 5 to 2 | -1.78 | 4 | = 0.403 | -0.45 [-1.65, 0.23] | small | n.s. |
| 3 to 2 vs Cardinality2 | -0.98 | 4 | = 0.477 | -0.64 [-1.02, 0.84] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.72 | 4 | = 0.403 | 0.81 [-0.34, 1.73] | large | n.s. |
| 4 to 2 vs 5 to 2 | -1.00 | 4 | = 0.477 | -0.73 [-1.29, 0.15] | medium | n.s. |
| 4 to 2 vs Cardinality2 | -1.45 | 4 | = 0.439 | -0.85 [-0.77, 0.66] | large | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.03 | 4 | = 0.477 | 0.91 [-0.26, 1.15] | large | n.s. |
| 5 to 2 vs Cardinality2 | -0.35 | 4 | = 0.799 | -0.26 [-0.69, 0.65] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 2.07 | 4 | = 0.403 | 1.24 [-0.13, 1.45] | large | n.s. |
| Cardinality2 vs increasing 1 to 2 | 1.92 | 4 | = 0.403 | 1.24 [-0.13, 1.44] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 325.56, BIC = 343.20
- Effect 1 effect: *β* = 1.49, *SE* = 0.775, *z* = 1.923, *p* = 0.054
- Effect 2 effect: *β* = -0.23, *SE* = 0.804, *z* = -0.287, *p* = 0.774
- Effect 3 effect: *β* = 0.66, *SE* = 0.819, *z* = 0.804, *p* = 0.421
- Effect 4 effect: *β* = 1.24, *SE* = 0.802, *z* = 1.540, *p* = 0.123
- Effect 5 effect: *β* = 0.06, *SE* = 0.211, *z* = 0.278, *p* = 0.781

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.889, η²_G = 0.038
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | -1.59 | 4 | = 0.937 | -0.76 [-1.66, 0.10] | medium | n.s. |
| 3 to 2 vs 5 to 2 | -0.21 | 4 | = 0.937 | -0.13 [-0.72, 0.95] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | -1.23 | 4 | = 0.937 | -0.63 [-0.96, 0.89] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.41 | 4 | = 0.937 | -0.20 [-0.94, 0.91] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.80 | 4 | = 0.937 | 0.46 [-0.28, 1.12] | small | n.s. |
| 4 to 2 vs Cardinality2 | 0.74 | 4 | = 0.937 | 0.36 [-0.41, 1.06] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 0.33 | 4 | = 0.937 | 0.20 [-0.55, 0.80] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -0.63 | 4 | = 0.937 | -0.25 [-1.09, 0.30] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -0.22 | 4 | = 0.937 | -0.11 [-1.46, 0.12] | negligible | n.s. |
| Cardinality2 vs increasing 1 to 2 | 0.06 | 4 | = 0.955 | 0.03 [-0.84, 0.59] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 301.32, BIC = 320.76
- Effect 1 effect: *β* = -0.41, *SE* = 0.349, *z* = -1.186, *p* = 0.236
- Effect 2 effect: *β* = -1.43, *SE* = 0.360, *z* = -3.979, *p* < .001
- Effect 3 effect: *β* = -0.91, *SE* = 0.420, *z* = -2.160, *p* = 0.031
- Effect 4 effect: *β* = -0.93, *SE* = 0.366, *z* = -2.535, *p* = 0.011
- Effect 5 effect: *β* = 0.61, *SE* = 0.062, *z* = 9.850, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.59, *p* = 0.007, η²_G = 0.190
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 2.51 | 6 | = 0.115 | 0.45 [-0.21, 0.85] | small | n.s. |
| 3 to 2 vs 5 to 2 | 3.03 | 6 | = 0.095 | 0.77 [-0.22, 0.83] | medium | n.s. |
| 3 to 2 vs Cardinality2 | 4.23 | 6 | = 0.055 | 1.37 [-0.20, 1.35] | large | n.s. |
| 3 to 2 vs increasing 1 to 2 | 2.87 | 6 | = 0.095 | 0.90 [-0.14, 1.07] | large | n.s. |
| 4 to 2 vs 5 to 2 | 0.99 | 6 | = 0.374 | 0.23 [-0.43, 0.60] | small | n.s. |
| 4 to 2 vs Cardinality2 | 1.92 | 6 | = 0.207 | 0.84 [-0.30, 1.21] | large | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.37 | 6 | = 0.315 | 0.42 [-0.38, 0.74] | small | n.s. |
| 5 to 2 vs Cardinality2 | 1.56 | 6 | = 0.285 | 0.72 [-0.31, 1.19] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | 1.06 | 6 | = 0.374 | 0.25 [-0.42, 0.69] | small | n.s. |
| Cardinality2 vs increasing 1 to 2 | -0.96 | 6 | = 0.374 | -0.40 [-1.23, 0.37] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 740.95, BIC = 760.40
- Effect 1 effect: *β* = -9.99, *SE* = 5.238, *z* = -1.907, *p* = 0.057
- Effect 2 effect: *β* = -10.42, *SE* = 5.363, *z* = -1.943, *p* = 0.052
- Effect 3 effect: *β* = -10.38, *SE* = 6.345, *z* = -1.636, *p* = 0.102
- Effect 4 effect: *β* = -0.23, *SE* = 5.463, *z* = -0.042, *p* = 0.967
- Effect 5 effect: *β* = -0.02, *SE* = 0.822, *z* = -0.027, *p* = 0.978

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.59, *p* = 0.670, η²_G = 0.070
- Greenhouse-Geisser corrected: *p* = 0.573 (ε = 0.520)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 2 vs 4 to 2 | 1.27 | 6 | = 0.805 | 0.37 [0.03, 1.14] | small | n.s. |
| 3 to 2 vs 5 to 2 | 2.65 | 6 | = 0.381 | 0.57 [-0.04, 1.05] | medium | n.s. |
| 3 to 2 vs Cardinality2 | 1.18 | 6 | = 0.805 | 0.72 [-0.40, 1.07] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.26 | 6 | = 0.805 | 0.12 [-0.71, 0.45] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.66 | 6 | = 0.805 | 0.26 [-0.35, 0.69] | small | n.s. |
| 4 to 2 vs Cardinality2 | 0.83 | 6 | = 0.805 | 0.50 [-0.81, 0.62] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | -0.27 | 6 | = 0.805 | -0.11 [-0.83, 0.30] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | 0.48 | 6 | = 0.805 | 0.29 [-0.71, 0.72] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -0.47 | 6 | = 0.805 | -0.27 [-1.06, 0.11] | small | n.s. |
| Cardinality2 vs increasing 1 to 2 | -0.77 | 6 | = 0.805 | -0.45 [-1.06, 0.51] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.011) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.007) (no significant pairwise comparisons)

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
