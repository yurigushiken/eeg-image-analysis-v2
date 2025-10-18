# Statistical Analysis Report: tables

**Generated:** 2025-10-18 13:32:19

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
| 1 to 3 | 24 | -3.78 µV | 1.81 | 0.37 | [-7.99, -0.83] |
| 2 to 3 | 21 | -3.25 µV | 1.31 | 0.29 | [-5.71, -1.06] |
| 3 to 3 | 23 | -2.91 µV | 1.69 | 0.35 | [-7.14, -0.40] |
| 4 to 3 | 23 | -3.84 µV | 1.87 | 0.39 | [-8.15, -0.66] |
| 5 to 3 | 24 | -3.50 µV | 2.31 | 0.47 | [-8.41, -0.11] |
| 6 to 3 | 23 | -4.21 µV | 2.08 | 0.43 | [-9.48, -0.82] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 176.84 ms | 12.36 | 2.52 | [152.80, 206.00] |
| 2 to 3 | 21 | 173.55 ms | 9.84 | 2.15 | [154.17, 198.21] |
| 3 to 3 | 23 | 175.36 ms | 14.31 | 2.98 | [147.80, 212.45] |
| 4 to 3 | 23 | 175.59 ms | 12.11 | 2.52 | [154.62, 209.09] |
| 5 to 3 | 24 | 176.41 ms | 13.20 | 2.69 | [149.94, 214.66] |
| 6 to 3 | 23 | 176.77 ms | 10.67 | 2.22 | [162.49, 206.73] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 14 | 1.76 µV | 1.72 | 0.46 | [0.09, 6.39] |
| 2 to 3 | 12 | 2.17 µV | 1.34 | 0.39 | [0.18, 5.17] |
| 3 to 3 | 13 | 2.24 µV | 1.98 | 0.55 | [0.18, 7.43] |
| 4 to 3 | 12 | 1.64 µV | 1.24 | 0.36 | [0.19, 4.48] |
| 5 to 3 | 18 | 1.78 µV | 1.24 | 0.29 | [-0.03, 3.67] |
| 6 to 3 | 14 | 1.69 µV | 1.89 | 0.50 | [-0.15, 6.43] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 14 | 104.16 ms | 4.95 | 1.32 | [94.67, 113.65] |
| 2 to 3 | 12 | 104.77 ms | 4.60 | 1.33 | [97.50, 114.79] |
| 3 to 3 | 13 | 105.34 ms | 4.44 | 1.23 | [95.65, 112.11] |
| 4 to 3 | 12 | 104.26 ms | 5.05 | 1.46 | [96.63, 114.17] |
| 5 to 3 | 18 | 105.53 ms | 4.83 | 1.14 | [92.36, 113.61] |
| 6 to 3 | 14 | 104.42 ms | 5.14 | 1.37 | [96.74, 112.71] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 4.32 µV | 3.53 | 0.79 | [0.59, 12.44] |
| 2 to 3 | 18 | 4.02 µV | 2.73 | 0.64 | [0.21, 9.67] |
| 3 to 3 | 15 | 2.56 µV | 1.93 | 0.50 | [0.18, 6.63] |
| 4 to 3 | 19 | 3.74 µV | 2.67 | 0.61 | [-0.01, 8.82] |
| 5 to 3 | 19 | 3.56 µV | 1.62 | 0.37 | [0.97, 7.00] |
| 6 to 3 | 19 | 4.21 µV | 2.60 | 0.60 | [1.41, 11.32] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 460.39 ms | 19.03 | 4.26 | [410.25, 487.24] |
| 2 to 3 | 18 | 456.83 ms | 20.41 | 4.81 | [414.10, 507.69] |
| 3 to 3 | 15 | 448.99 ms | 24.30 | 6.28 | [400.18, 479.35] |
| 4 to 3 | 19 | 467.27 ms | 23.50 | 5.39 | [411.80, 525.73] |
| 5 to 3 | 19 | 459.65 ms | 22.84 | 5.24 | [407.93, 487.03] |
| 6 to 3 | 19 | 460.97 ms | 21.67 | 4.97 | [407.05, 506.18] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 475.30, BIC = 501.64
- **2 to 3 vs 1 to 3**: *β* = 0.27, *SE* = 0.342, *z* = 0.784, *p* = 0.433
- **3 to 3 vs 1 to 3**: *β* = 0.31, *SE* = 0.335, *z* = 0.915, *p* = 0.360
- **4 to 3 vs 1 to 3**: *β* = -0.22, *SE* = 0.329, *z* = -0.670, *p* = 0.503
- **5 to 3 vs 1 to 3**: *β* = 0.03, *SE* = 0.326, *z* = 0.100, *p* = 0.920
- **6 to 3 vs 1 to 3**: *β* = -0.38, *SE* = 0.329, *z* = -1.150, *p* = 0.250
- **SNR**: *β* = -0.39, *SE* = 0.042, *z* = -9.313, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.90, *p* = 0.018, η²_G = 0.076
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -3.10 | 19 | = 0.044 | -0.78 [-0.97, -0.01] | medium | * |
| 1 to 3 vs 3 to 3 | -3.12 | 19 | = 0.044 | -0.71 [-1.09, -0.15] | medium | * |
| 1 to 3 vs 4 to 3 | -0.31 | 19 | = 0.874 | -0.08 [-0.45, 0.41] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.93 | 19 | = 0.500 | -0.29 [-0.53, 0.32] | small | n.s. |
| 1 to 3 vs 6 to 3 | 0.24 | 19 | = 0.874 | 0.06 [-0.28, 0.59] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | -0.05 | 19 | = 0.964 | -0.01 [-0.54, 0.37] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 2.07 | 19 | = 0.131 | 0.63 [-0.03, 0.96] | medium | n.s. |
| 2 to 3 vs 5 to 3 | 1.18 | 19 | = 0.475 | 0.30 [-0.19, 0.74] | small | n.s. |
| 2 to 3 vs 6 to 3 | 2.71 | 19 | = 0.069 | 0.69 [0.04, 1.01] | medium | n.s. |
| 3 to 3 vs 4 to 3 | 2.36 | 19 | = 0.088 | 0.58 [0.03, 0.97] | medium | n.s. |
| 3 to 3 vs 5 to 3 | 1.08 | 19 | = 0.484 | 0.28 [-0.17, 0.71] | small | n.s. |
| 3 to 3 vs 6 to 3 | 2.42 | 19 | = 0.088 | 0.65 [0.11, 1.07] | medium | n.s. |
| 4 to 3 vs 5 to 3 | -1.01 | 19 | = 0.484 | -0.21 [-0.69, 0.19] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.59 | 19 | = 0.703 | 0.13 [-0.30, 0.59] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 1.43 | 19 | = 0.361 | 0.31 [-0.18, 0.70] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 986.55, BIC = 1012.89
- **2 to 3 vs 1 to 3**: *β* = -0.26, *SE* = 1.914, *z* = -0.135, *p* = 0.893
- **3 to 3 vs 1 to 3**: *β* = -0.48, *SE* = 1.873, *z* = -0.258, *p* = 0.796
- **4 to 3 vs 1 to 3**: *β* = -1.41, *SE* = 1.836, *z* = -0.770, *p* = 0.441
- **5 to 3 vs 1 to 3**: *β* = -0.26, *SE* = 1.816, *z* = -0.141, *p* = 0.888
- **6 to 3 vs 1 to 3**: *β* = 1.34, *SE* = 1.834, *z* = 0.729, *p* = 0.466
- **SNR**: *β* = 0.26, *SE* = 0.244, *z* = 1.071, *p* = 0.284

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.76, *p* = 0.581, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.43 | 19 | = 0.788 | 0.06 [-0.42, 0.49] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | 0.76 | 19 | = 0.788 | 0.19 [-0.35, 0.52] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.68 | 19 | = 0.788 | 0.15 [-0.25, 0.62] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.23 | 19 | = 0.823 | -0.05 [-0.38, 0.46] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.60 | 19 | = 0.788 | -0.13 [-0.56, 0.31] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 0.55 | 19 | = 0.788 | 0.12 [-0.35, 0.56] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 0.47 | 19 | = 0.788 | 0.09 [-0.36, 0.57] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | -0.55 | 19 | = 0.788 | -0.10 [-0.58, 0.34] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.97 | 19 | = 0.788 | -0.20 [-0.62, 0.29] | negligible | n.s. |
| 3 to 3 vs 4 to 3 | -0.29 | 19 | = 0.823 | -0.04 [-0.39, 0.50] | negligible | n.s. |
| 3 to 3 vs 5 to 3 | -1.09 | 19 | = 0.788 | -0.21 [-0.52, 0.35] | small | n.s. |
| 3 to 3 vs 6 to 3 | -1.91 | 19 | = 0.536 | -0.32 [-0.65, 0.24] | small | n.s. |
| 4 to 3 vs 5 to 3 | -1.23 | 19 | = 0.788 | -0.19 [-0.57, 0.30] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -2.25 | 19 | = 0.536 | -0.30 [-1.02, -0.07] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.41 | 19 | = 0.788 | -0.07 [-0.65, 0.23] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 259.77, BIC = 281.54
- **2 to 3 vs 1 to 3**: *β* = 0.41, *SE* = 0.377, *z* = 1.091, *p* = 0.275
- **3 to 3 vs 1 to 3**: *β* = 0.51, *SE* = 0.365, *z* = 1.404, *p* = 0.160
- **4 to 3 vs 1 to 3**: *β* = -0.32, *SE* = 0.375, *z* = -0.844, *p* = 0.399
- **5 to 3 vs 1 to 3**: *β* = -0.32, *SE* = 0.339, *z* = -0.930, *p* = 0.352
- **6 to 3 vs 1 to 3**: *β* = 0.26, *SE* = 0.359, *z* = 0.731, *p* = 0.465
- **SNR**: *β* = 0.64, *SE* = 0.068, *z* = 9.346, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.53, *p* = 0.747, η²_G = 0.167
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 1.69 | 2 | = 0.951 | 1.31 [-0.92, 0.93] | large | n.s. |
| 1 to 3 vs 3 to 3 | 0.43 | 2 | = 0.951 | 0.11 [-1.33, 0.30] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.45 | 2 | = 0.951 | 0.36 [-0.55, 1.17] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.78 | 2 | = 0.951 | 0.86 [-0.74, 0.53] | large | n.s. |
| 1 to 3 vs 6 to 3 | 0.05 | 2 | = 0.965 | 0.02 [-0.77, 0.66] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | -0.89 | 2 | = 0.951 | -0.71 [-1.22, 0.67] | medium | n.s. |
| 2 to 3 vs 4 to 3 | -1.99 | 2 | = 0.951 | -1.61 [-1.06, 0.80] | large | n.s. |
| 2 to 3 vs 5 to 3 | -0.43 | 2 | = 0.951 | -0.37 [-0.41, 0.96] | small | n.s. |
| 2 to 3 vs 6 to 3 | -1.32 | 2 | = 0.951 | -1.05 [-0.69, 0.74] | large | n.s. |
| 3 to 3 vs 4 to 3 | 0.16 | 2 | = 0.951 | 0.12 [-0.59, 1.11] | negligible | n.s. |
| 3 to 3 vs 5 to 3 | 0.47 | 2 | = 0.951 | 0.49 [-0.58, 0.77] | small | n.s. |
| 3 to 3 vs 6 to 3 | -0.19 | 2 | = 0.951 | -0.09 [-0.58, 0.97] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 1.17 | 2 | = 0.951 | 0.71 [-0.69, 0.74] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -0.29 | 2 | = 0.951 | -0.29 [-0.74, 0.80] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.65 | 2 | = 0.951 | -0.72 [-0.70, 0.57] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 502.15, BIC = 523.92
- **2 to 3 vs 1 to 3**: *β* = 0.14, *SE* = 1.633, *z* = 0.084, *p* = 0.933
- **3 to 3 vs 1 to 3**: *β* = 0.35, *SE* = 1.588, *z* = 0.222, *p* = 0.824
- **4 to 3 vs 1 to 3**: *β* = -0.38, *SE* = 1.626, *z* = -0.235, *p* = 0.814
- **5 to 3 vs 1 to 3**: *β* = 0.76, *SE* = 1.474, *z* = 0.516, *p* = 0.606
- **6 to 3 vs 1 to 3**: *β* = 0.28, *SE* = 1.545, *z* = 0.182, *p* = 0.856
- **SNR**: *β* = 0.04, *SE* = 0.295, *z* = 0.154, *p* = 0.877

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.418, η²_G = 0.208
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.24 | 2 | = 0.833 | -0.15 [-0.84, 1.01] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | 0.58 | 2 | = 0.779 | 0.19 [-0.96, 0.59] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 1.07 | 2 | = 0.746 | 0.81 [-0.73, 0.95] | large | n.s. |
| 1 to 3 vs 5 to 3 | 2.29 | 2 | = 0.746 | 0.68 [-0.58, 0.69] | medium | n.s. |
| 1 to 3 vs 6 to 3 | -0.50 | 2 | = 0.779 | -0.29 [-0.84, 0.60] | small | n.s. |
| 2 to 3 vs 3 to 3 | 0.84 | 2 | = 0.779 | 0.54 [-0.75, 1.11] | medium | n.s. |
| 2 to 3 vs 4 to 3 | 3.11 | 2 | = 0.746 | 2.17 [-1.22, 0.67] | large | n.s. |
| 2 to 3 vs 5 to 3 | 1.20 | 2 | = 0.746 | 0.86 [-0.91, 0.45] | large | n.s. |
| 2 to 3 vs 6 to 3 | -0.41 | 2 | = 0.779 | -0.23 [-0.59, 0.84] | small | n.s. |
| 3 to 3 vs 4 to 3 | 1.46 | 2 | = 0.746 | 1.06 [-0.93, 0.75] | large | n.s. |
| 3 to 3 vs 5 to 3 | 1.19 | 2 | = 0.746 | 0.63 [-0.64, 0.70] | medium | n.s. |
| 3 to 3 vs 6 to 3 | -0.65 | 2 | = 0.779 | -0.46 [-1.22, 0.39] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.40 | 2 | = 0.779 | 0.32 [-0.85, 0.59] | small | n.s. |
| 4 to 3 vs 6 to 3 | -1.12 | 2 | = 0.746 | -0.88 [-0.77, 0.77] | large | n.s. |
| 5 to 3 vs 6 to 3 | -1.35 | 2 | = 0.746 | -0.82 [-0.75, 0.52] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 434.21, BIC = 458.52
- **2 to 3 vs 1 to 3**: *β* = -0.40, *SE* = 0.452, *z* = -0.887, *p* = 0.375
- **3 to 3 vs 1 to 3**: *β* = -0.92, *SE* = 0.486, *z* = -1.896, *p* = 0.058
- **4 to 3 vs 1 to 3**: *β* = -0.55, *SE* = 0.443, *z* = -1.242, *p* = 0.214
- **5 to 3 vs 1 to 3**: *β* = -0.59, *SE* = 0.446, *z* = -1.316, *p* = 0.188
- **6 to 3 vs 1 to 3**: *β* = -0.14, *SE* = 0.441, *z* = -0.326, *p* = 0.745
- **SNR**: *β* = 0.45, *SE* = 0.050, *z* = 9.059, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.44, *p* = 0.047, η²_G = 0.093
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 1.69 | 10 | = 0.388 | 0.42 [-0.26, 0.78] | small | n.s. |
| 1 to 3 vs 3 to 3 | 2.33 | 10 | = 0.308 | 0.85 [-0.09, 1.09] | large | n.s. |
| 1 to 3 vs 4 to 3 | 0.86 | 10 | = 0.514 | 0.20 [-0.22, 0.79] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 1.14 | 10 | = 0.485 | 0.42 [-0.20, 0.82] | small | n.s. |
| 1 to 3 vs 6 to 3 | 1.12 | 10 | = 0.485 | 0.18 [-0.34, 0.63] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 1.54 | 10 | = 0.388 | 0.49 [-0.25, 1.01] | small | n.s. |
| 2 to 3 vs 4 to 3 | -0.98 | 10 | = 0.514 | -0.32 [-0.75, 0.37] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.24 | 10 | = 0.874 | -0.07 [-0.30, 0.71] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -1.12 | 10 | = 0.485 | -0.28 [-0.79, 0.26] | small | n.s. |
| 3 to 3 vs 4 to 3 | -2.94 | 10 | = 0.222 | -0.96 [-1.53, -0.13] | large | n.s. |
| 3 to 3 vs 5 to 3 | -1.56 | 10 | = 0.388 | -0.71 [-1.09, 0.13] | medium | n.s. |
| 3 to 3 vs 6 to 3 | -2.10 | 10 | = 0.308 | -0.80 [-1.15, 0.04] | large | n.s. |
| 4 to 3 vs 5 to 3 | 0.86 | 10 | = 0.514 | 0.32 [-0.34, 0.74] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.02 | 10 | = 0.985 | -0.00 [-0.56, 0.47] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.76 | 10 | = 0.539 | -0.27 [-0.77, 0.24] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 989.59, BIC = 1013.90
- **2 to 3 vs 1 to 3**: *β* = -3.79, *SE* = 5.862, *z* = -0.646, *p* = 0.518
- **3 to 3 vs 1 to 3**: *β* = -12.60, *SE* = 6.306, *z* = -1.998, *p* = 0.046
- **4 to 3 vs 1 to 3**: *β* = 6.81, *SE* = 5.766, *z* = 1.181, *p* = 0.238
- **5 to 3 vs 1 to 3**: *β* = -1.19, *SE* = 5.786, *z* = -0.206, *p* = 0.837
- **6 to 3 vs 1 to 3**: *β* = 0.63, *SE* = 5.735, *z* = 0.110, *p* = 0.912
- **SNR**: *β* = 0.06, *SE* = 0.619, *z* = 0.104, *p* = 0.917

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.570, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.14 | 10 | = 0.891 | 0.06 [-0.38, 0.65] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | 1.51 | 10 | = 0.815 | 0.51 [-0.06, 1.13] | medium | n.s. |
| 1 to 3 vs 4 to 3 | -0.23 | 10 | = 0.891 | -0.06 [-0.88, 0.15] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 0.46 | 10 | = 0.891 | 0.18 [-0.41, 0.59] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.29 | 10 | = 0.891 | -0.14 [-0.53, 0.44] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 0.95 | 10 | = 0.891 | 0.39 [-0.39, 0.84] | small | n.s. |
| 2 to 3 vs 4 to 3 | -0.29 | 10 | = 0.891 | -0.11 [-0.79, 0.33] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | 0.58 | 10 | = 0.891 | 0.11 [-0.63, 0.37] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.43 | 10 | = 0.891 | -0.18 [-0.60, 0.43] | negligible | n.s. |
| 3 to 3 vs 4 to 3 | -1.85 | 10 | = 0.702 | -0.57 [-1.16, 0.13] | medium | n.s. |
| 3 to 3 vs 5 to 3 | -0.82 | 10 | = 0.891 | -0.28 [-0.97, 0.23] | small | n.s. |
| 3 to 3 vs 6 to 3 | -1.88 | 10 | = 0.702 | -0.72 [-1.14, 0.04] | medium | n.s. |
| 4 to 3 vs 5 to 3 | 0.68 | 10 | = 0.891 | 0.24 [-0.19, 0.91] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.21 | 10 | = 0.891 | -0.07 [-0.26, 0.78] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.83 | 10 | = 0.891 | -0.33 [-0.64, 0.36] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.018). Post-hoc tests revealed:
  - 1 to 3 showed smaller amplitude than 2 to 3 (*d* = -0.78)
  - 1 to 3 showed smaller amplitude than 3 to 3 (*d* = -0.71)
**P3b amplitude:** Significant main effect of condition (*p* = 0.047) (no significant pairwise comparisons)

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
