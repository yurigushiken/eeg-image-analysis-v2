# Statistical Analysis Report: tables

**Generated:** 2025-10-17 03:15:05

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
| 1 to 3 | 24 | -3.71 µV | 1.76 | 0.36 | [-7.67, -0.90] |
| 2 to 3 | 21 | -3.18 µV | 1.31 | 0.29 | [-5.72, -1.11] |
| 4 to 3 | 23 | -3.78 µV | 1.84 | 0.38 | [-8.01, -0.64] |
| 5 to 3 | 24 | -3.42 µV | 2.26 | 0.46 | [-8.30, -0.20] |
| 6 to 3 | 23 | -4.15 µV | 2.05 | 0.43 | [-9.49, -0.82] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 177.95 ms | 12.98 | 2.65 | [152.77, 207.58] |
| 2 to 3 | 21 | 174.28 ms | 10.55 | 2.30 | [154.00, 200.10] |
| 4 to 3 | 23 | 176.52 ms | 12.73 | 2.66 | [153.98, 210.92] |
| 5 to 3 | 24 | 177.19 ms | 13.54 | 2.76 | [149.19, 216.16] |
| 6 to 3 | 23 | 177.82 ms | 11.17 | 2.33 | [162.68, 208.58] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 14 | 1.76 µV | 1.72 | 0.46 | [0.09, 6.39] |
| 2 to 3 | 12 | 2.17 µV | 1.34 | 0.39 | [0.18, 5.17] |
| 4 to 3 | 12 | 1.64 µV | 1.24 | 0.36 | [0.19, 4.48] |
| 5 to 3 | 18 | 1.78 µV | 1.24 | 0.29 | [-0.03, 3.67] |
| 6 to 3 | 14 | 1.69 µV | 1.89 | 0.50 | [-0.15, 6.43] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 14 | 104.16 ms | 4.95 | 1.32 | [94.67, 113.65] |
| 2 to 3 | 12 | 104.77 ms | 4.60 | 1.33 | [97.50, 114.79] |
| 4 to 3 | 12 | 104.26 ms | 5.05 | 1.46 | [96.63, 114.17] |
| 5 to 3 | 18 | 105.53 ms | 4.83 | 1.14 | [92.36, 113.61] |
| 6 to 3 | 14 | 104.42 ms | 5.14 | 1.37 | [96.74, 112.71] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 4.34 µV | 3.56 | 0.80 | [0.60, 12.45] |
| 2 to 3 | 18 | 4.05 µV | 2.74 | 0.65 | [0.27, 9.62] |
| 4 to 3 | 19 | 3.78 µV | 2.67 | 0.61 | [0.10, 8.91] |
| 5 to 3 | 19 | 3.58 µV | 1.65 | 0.38 | [0.91, 7.13] |
| 6 to 3 | 19 | 4.23 µV | 2.63 | 0.60 | [1.42, 11.43] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 461.80 ms | 18.62 | 4.16 | [412.02, 487.19] |
| 2 to 3 | 18 | 457.51 ms | 18.27 | 4.31 | [414.07, 494.32] |
| 4 to 3 | 19 | 467.69 ms | 21.80 | 5.00 | [414.98, 518.60] |
| 5 to 3 | 19 | 460.72 ms | 22.45 | 5.15 | [409.48, 487.23] |
| 6 to 3 | 19 | 462.10 ms | 21.01 | 4.82 | [409.92, 506.46] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 407.82, BIC = 429.78
- Effect 1 effect: *β* = 0.27, *SE* = 0.357, *z* = 0.746, *p* = 0.456
- Effect 2 effect: *β* = -0.23, *SE* = 0.343, *z* = -0.669, *p* = 0.503
- Effect 3 effect: *β* = 0.05, *SE* = 0.339, *z* = 0.149, *p* = 0.882
- Effect 4 effect: *β* = -0.40, *SE* = 0.343, *z* = -1.158, *p* = 0.247
- Effect 5 effect: *β* = -0.38, *SE* = 0.048, *z* = -7.983, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.29, *p* = 0.067, η²_G = 0.059
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -3.05 | 19 | = 0.065 | -0.76 [-0.98, -0.01] | medium | n.s. |
| 1 to 3 vs 4 to 3 | -0.27 | 19 | = 0.790 | -0.07 [-0.44, 0.42] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.91 | 19 | = 0.536 | -0.28 [-0.53, 0.31] | small | n.s. |
| 1 to 3 vs 6 to 3 | 0.30 | 19 | = 0.790 | 0.08 [-0.27, 0.60] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 2.01 | 19 | = 0.195 | 0.62 [-0.04, 0.94] | medium | n.s. |
| 2 to 3 vs 5 to 3 | 1.15 | 19 | = 0.525 | 0.29 [-0.20, 0.73] | small | n.s. |
| 2 to 3 vs 6 to 3 | 2.74 | 19 | = 0.065 | 0.70 [0.05, 1.02] | medium | n.s. |
| 4 to 3 vs 5 to 3 | -1.00 | 19 | = 0.536 | -0.21 [-0.69, 0.19] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.62 | 19 | = 0.681 | 0.14 [-0.29, 0.60] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 1.46 | 19 | = 0.398 | 0.32 [-0.17, 0.72] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 831.50, BIC = 853.46
- Effect 1 effect: *β* = -0.88, *SE* = 1.928, *z* = -0.457, *p* = 0.648
- Effect 2 effect: *β* = -1.73, *SE* = 1.841, *z* = -0.939, *p* = 0.348
- Effect 3 effect: *β* = -0.67, *SE* = 1.822, *z* = -0.366, *p* = 0.714
- Effect 4 effect: *β* = 1.23, *SE* = 1.840, *z* = 0.670, *p* = 0.503
- Effect 5 effect: *β* = 0.16, *SE* = 0.270, *z* = 0.585, *p* = 0.559

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.614, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.54 | 19 | = 0.750 | 0.07 [-0.37, 0.54] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.69 | 19 | = 0.750 | 0.16 [-0.25, 0.62] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.12 | 19 | = 0.909 | -0.02 [-0.35, 0.49] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.62 | 19 | = 0.750 | -0.14 [-0.54, 0.32] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 0.43 | 19 | = 0.750 | 0.08 [-0.37, 0.56] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | -0.50 | 19 | = 0.750 | -0.09 [-0.56, 0.35] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -1.09 | 19 | = 0.750 | -0.21 [-0.65, 0.27] | small | n.s. |
| 4 to 3 vs 5 to 3 | -1.15 | 19 | = 0.750 | -0.17 [-0.55, 0.32] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -2.30 | 19 | = 0.328 | -0.31 [-1.04, -0.09] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.61 | 19 | = 0.750 | -0.10 [-0.68, 0.20] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 212.28, BIC = 230.27
- Effect 1 effect: *β* = 0.42, *SE* = 0.366, *z* = 1.157, *p* = 0.247
- Effect 2 effect: *β* = -0.30, *SE* = 0.364, *z* = -0.831, *p* = 0.406
- Effect 3 effect: *β* = -0.33, *SE* = 0.329, *z* = -0.995, *p* = 0.320
- Effect 4 effect: *β* = 0.24, *SE* = 0.350, *z* = 0.677, *p* = 0.498
- Effect 5 effect: *β* = 0.62, *SE* = 0.070, *z* = 8.848, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.620, η²_G = 0.096
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 1.96 | 4 | = 0.758 | 1.05 [-0.92, 0.93] | large | n.s. |
| 1 to 3 vs 4 to 3 | 1.02 | 4 | = 0.758 | 0.47 [-0.55, 1.17] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.93 | 4 | = 0.758 | 0.69 [-0.74, 0.53] | medium | n.s. |
| 1 to 3 vs 6 to 3 | 0.78 | 4 | = 0.758 | 0.25 [-0.77, 0.66] | small | n.s. |
| 2 to 3 vs 4 to 3 | -1.06 | 4 | = 0.758 | -0.56 [-1.06, 0.80] | medium | n.s. |
| 2 to 3 vs 5 to 3 | -0.69 | 4 | = 0.758 | -0.38 [-0.41, 0.96] | small | n.s. |
| 2 to 3 vs 6 to 3 | -0.81 | 4 | = 0.758 | -0.48 [-0.69, 0.74] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.45 | 4 | = 0.820 | 0.21 [-0.69, 0.74] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.22 | 4 | = 0.837 | -0.12 [-0.74, 0.80] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.36 | 4 | = 0.820 | -0.27 [-0.70, 0.57] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 427.75, BIC = 445.74
- Effect 1 effect: *β* = 0.00, *SE* = 1.683, *z* = 0.001, *p* = 0.999
- Effect 2 effect: *β* = -0.45, *SE* = 1.676, *z* = -0.270, *p* = 0.787
- Effect 3 effect: *β* = 0.72, *SE* = 1.522, *z* = 0.470, *p* = 0.638
- Effect 4 effect: *β* = 0.13, *SE* = 1.587, *z* = 0.082, *p* = 0.935
- Effect 5 effect: *β* = 0.12, *SE* = 0.328, *z* = 0.383, *p* = 0.702

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.925, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.93 | 4 | = 0.917 | 0.53 [-0.84, 1.01] | medium | n.s. |
| 1 to 3 vs 4 to 3 | 0.48 | 4 | = 0.917 | 0.37 [-0.73, 0.95] | small | n.s. |
| 1 to 3 vs 5 to 3 | 1.07 | 4 | = 0.917 | 0.42 [-0.58, 0.69] | small | n.s. |
| 1 to 3 vs 6 to 3 | 0.38 | 4 | = 0.917 | 0.15 [-0.84, 0.60] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -0.50 | 4 | = 0.917 | -0.27 [-1.22, 0.67] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.20 | 4 | = 0.917 | -0.14 [-0.91, 0.45] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.62 | 4 | = 0.917 | -0.27 [-0.59, 0.84] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.21 | 4 | = 0.917 | 0.13 [-0.85, 0.59] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.11 | 4 | = 0.917 | -0.08 [-0.77, 0.77] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.27 | 4 | = 0.917 | -0.16 [-0.75, 0.52] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 384.62, BIC = 405.05
- Effect 1 effect: *β* = -0.42, *SE* = 0.461, *z* = -0.906, *p* = 0.365
- Effect 2 effect: *β* = -0.54, *SE* = 0.453, *z* = -1.198, *p* = 0.231
- Effect 3 effect: *β* = -0.63, *SE* = 0.455, *z* = -1.391, *p* = 0.164
- Effect 4 effect: *β* = -0.15, *SE* = 0.449, *z* = -0.335, *p* = 0.738
- Effect 5 effect: *β* = 0.41, *SE* = 0.055, *z* = 7.491, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.214, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 1.48 | 14 | = 0.478 | 0.32 [-0.27, 0.78] | small | n.s. |
| 1 to 3 vs 4 to 3 | 1.01 | 14 | = 0.528 | 0.19 [-0.23, 0.78] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 1.63 | 14 | = 0.478 | 0.51 [-0.20, 0.81] | medium | n.s. |
| 1 to 3 vs 6 to 3 | 1.11 | 14 | = 0.528 | 0.16 [-0.34, 0.63] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -0.74 | 14 | = 0.588 | -0.18 [-0.75, 0.37] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | 0.63 | 14 | = 0.600 | 0.16 [-0.29, 0.72] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.93 | 14 | = 0.528 | -0.19 [-0.78, 0.26] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 1.38 | 14 | = 0.478 | 0.40 [-0.33, 0.75] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.15 | 14 | = 0.885 | -0.03 [-0.55, 0.48] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -1.37 | 14 | = 0.478 | -0.40 [-0.77, 0.24] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 834.99, BIC = 855.42
- Effect 1 effect: *β* = -4.34, *SE* = 5.047, *z* = -0.861, *p* = 0.389
- Effect 2 effect: *β* = 5.68, *SE* = 4.963, *z* = 1.145, *p* = 0.252
- Effect 3 effect: *β* = -1.90, *SE* = 4.982, *z* = -0.380, *p* = 0.704
- Effect 4 effect: *β* = 0.33, *SE* = 4.925, *z* = 0.067, *p* = 0.947
- Effect 5 effect: *β* = 0.10, *SE* = 0.569, *z* = 0.179, *p* = 0.858

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.50, *p* = 0.736, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.20 | 14 | = 0.992 | 0.07 [-0.34, 0.69] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | -1.36 | 14 | = 0.726 | -0.29 [-0.86, 0.16] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.16 | 14 | = 0.992 | 0.05 [-0.39, 0.60] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | 0.19 | 14 | = 0.992 | 0.06 [-0.51, 0.45] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -1.10 | 14 | = 0.726 | -0.35 [-0.85, 0.28] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.05 | 14 | = 0.992 | -0.01 [-0.67, 0.33] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.02 | 14 | = 0.992 | -0.01 [-0.64, 0.39] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 1.18 | 14 | = 0.726 | 0.31 [-0.18, 0.92] | small | n.s. |
| 4 to 3 vs 6 to 3 | 1.18 | 14 | = 0.726 | 0.35 [-0.27, 0.78] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.01 | 14 | = 0.992 | 0.00 [-0.64, 0.36] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.067)

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
