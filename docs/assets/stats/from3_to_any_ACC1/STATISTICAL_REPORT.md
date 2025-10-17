# Statistical Analysis Report: tables

**Generated:** 2025-10-17 04:47:21

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
| 3 to 1 | 18 | -2.65 µV | 2.17 | 0.51 | [-6.82, -0.01] |
| 3 to 2 | 22 | -3.92 µV | 2.01 | 0.43 | [-7.98, -0.58] |
| 3 to 4 | 23 | -3.39 µV | 1.76 | 0.37 | [-7.06, -0.73] |
| 3 to 5 | 22 | -3.64 µV | 2.30 | 0.49 | [-10.12, -0.74] |
| 3 to 6 | 23 | -4.87 µV | 2.57 | 0.54 | [-10.95, -1.29] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 181.97 ms | 13.13 | 3.09 | [160.44, 207.70] |
| 3 to 2 | 22 | 171.18 ms | 8.92 | 1.90 | [158.22, 195.85] |
| 3 to 4 | 23 | 169.92 ms | 11.56 | 2.41 | [143.66, 200.12] |
| 3 to 5 | 22 | 169.65 ms | 10.64 | 2.27 | [154.48, 196.10] |
| 3 to 6 | 23 | 173.08 ms | 10.66 | 2.22 | [155.52, 195.70] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 17 | 1.93 µV | 1.19 | 0.29 | [0.24, 5.03] |
| 3 to 2 | 9 | 1.96 µV | 1.46 | 0.49 | [0.29, 4.15] |
| 3 to 4 | 15 | 1.82 µV | 1.88 | 0.48 | [0.26, 6.28] |
| 3 to 5 | 12 | 1.88 µV | 1.50 | 0.43 | [0.04, 4.73] |
| 3 to 6 | 9 | 2.65 µV | 2.25 | 0.75 | [0.12, 6.94] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 17 | 105.50 ms | 5.77 | 1.40 | [91.43, 114.42] |
| 3 to 2 | 9 | 102.66 ms | 4.98 | 1.66 | [95.44, 111.32] |
| 3 to 4 | 15 | 101.79 ms | 7.17 | 1.85 | [88.70, 112.71] |
| 3 to 5 | 12 | 102.71 ms | 6.89 | 1.99 | [89.03, 114.68] |
| 3 to 6 | 9 | 101.89 ms | 7.32 | 2.44 | [93.33, 113.36] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 4.14 µV | 2.52 | 0.56 | [0.83, 10.94] |
| 3 to 2 | 18 | 4.33 µV | 3.20 | 0.75 | [0.35, 12.51] |
| 3 to 4 | 16 | 4.29 µV | 2.27 | 0.57 | [0.31, 7.23] |
| 3 to 5 | 16 | 3.83 µV | 2.64 | 0.66 | [0.01, 10.10] |
| 3 to 6 | 20 | 2.82 µV | 2.04 | 0.46 | [0.10, 8.90] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 483.30 ms | 12.22 | 2.73 | [463.91, 507.04] |
| 3 to 2 | 18 | 490.21 ms | 19.08 | 4.50 | [441.23, 530.96] |
| 3 to 4 | 16 | 491.84 ms | 14.37 | 3.59 | [462.33, 519.76] |
| 3 to 5 | 16 | 487.63 ms | 21.43 | 5.36 | [440.02, 531.77] |
| 3 to 6 | 20 | 487.68 ms | 22.42 | 5.01 | [438.21, 543.49] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 401.78, BIC = 423.23
- Effect 1 effect: *β* = -0.15, *SE* = 0.429, *z* = -0.351, *p* = 0.725
- Effect 2 effect: *β* = -0.12, *SE* = 0.412, *z* = -0.301, *p* = 0.763
- Effect 3 effect: *β* = 0.07, *SE* = 0.427, *z* = 0.172, *p* = 0.863
- Effect 4 effect: *β* = -1.17, *SE* = 0.426, *z* = -2.750, *p* = 0.006
- Effect 5 effect: *β* = -0.54, *SE* = 0.057, *z* = -9.451, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.33, *p* = 0.015, η²_G = 0.097
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 2.61 | 16 | = 0.096 | 0.67 [0.07, 1.20] | medium | n.s. |
| 3 to 1 vs 3 to 4 | 1.93 | 16 | = 0.152 | 0.47 [-0.04, 1.02] | small | n.s. |
| 3 to 1 vs 3 to 5 | 1.08 | 16 | = 0.396 | 0.37 [-0.26, 0.79] | small | n.s. |
| 3 to 1 vs 3 to 6 | 2.96 | 16 | = 0.092 | 0.90 [0.14, 1.29] | large | n.s. |
| 3 to 2 vs 3 to 4 | -1.03 | 16 | = 0.396 | -0.25 [-0.71, 0.19] | small | n.s. |
| 3 to 2 vs 3 to 5 | -0.91 | 16 | = 0.418 | -0.24 [-0.57, 0.32] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.20 | 16 | = 0.396 | 0.32 [-0.03, 0.89] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.11 | 16 | = 0.911 | -0.03 [-0.37, 0.52] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.90 | 16 | = 0.152 | 0.55 [0.12, 1.09] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 2.20 | 16 | = 0.142 | 0.51 [0.10, 1.05] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 811.72, BIC = 833.18
- Effect 1 effect: *β* = -9.26, *SE* = 2.733, *z* = -3.387, *p* = 0.001
- Effect 2 effect: *β* = -11.48, *SE* = 2.614, *z* = -4.390, *p* < .001
- Effect 3 effect: *β* = -10.81, *SE* = 2.721, *z* = -3.973, *p* < .001
- Effect 4 effect: *β* = -7.87, *SE* = 2.713, *z* = -2.900, *p* = 0.004
- Effect 5 effect: *β* = -0.23, *SE* = 0.372, *z* = -0.626, *p* = 0.531

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.21, *p* < .001, η²_G = 0.153
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 3.12 | 16 | = 0.022 | 1.07 [0.17, 1.34] | large | * |
| 3 to 1 vs 3 to 4 | 4.06 | 16 | = 0.009 | 1.03 [0.36, 1.56] | large | ** |
| 3 to 1 vs 3 to 5 | 3.60 | 16 | = 0.012 | 0.85 [0.27, 1.48] | large | * |
| 3 to 1 vs 3 to 6 | 2.75 | 16 | = 0.035 | 0.77 [0.10, 1.24] | medium | * |
| 3 to 2 vs 3 to 4 | 0.19 | 16 | = 0.855 | 0.05 [-0.23, 0.67] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -0.48 | 16 | = 0.708 | -0.13 [-0.33, 0.56] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | -0.87 | 16 | = 0.593 | -0.27 [-0.51, 0.37] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.84 | 16 | = 0.593 | -0.16 [-0.59, 0.30] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -1.08 | 16 | = 0.591 | -0.28 [-0.82, 0.09] | small | n.s. |
| 3 to 5 vs 3 to 6 | -0.56 | 16 | = 0.708 | -0.11 [-0.72, 0.18] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 181.82, BIC = 198.84
- Effect 1 effect: *β* = 0.03, *SE* = 0.330, *z* = 0.080, *p* = 0.936
- Effect 2 effect: *β* = 0.28, *SE* = 0.285, *z* = 0.978, *p* = 0.328
- Effect 3 effect: *β* = 0.07, *SE* = 0.304, *z* = 0.226, *p* = 0.821
- Effect 4 effect: *β* = 0.13, *SE* = 0.339, *z* = 0.393, *p* = 0.694
- Effect 5 effect: *β* = 0.61, *SE* = 0.062, *z* = 9.841, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.48, *p* = 0.127, η²_G = 0.504
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -4.75 | 1 | = 0.557 | -2.85 [-0.74, 0.93] | large | n.s. |
| 3 to 1 vs 3 to 4 | -1.25 | 1 | = 0.557 | -0.38 [-0.38, 1.10] | small | n.s. |
| 3 to 1 vs 3 to 5 | -1.77 | 1 | = 0.557 | -1.27 [-0.83, 0.85] | large | n.s. |
| 3 to 1 vs 3 to 6 | -1.39 | 1 | = 0.557 | -1.11 [-1.19, 0.92] | large | n.s. |
| 3 to 2 vs 3 to 4 | 3.72 | 1 | = 0.557 | 2.79 [-1.05, 1.05] | large | n.s. |
| 3 to 2 vs 3 to 5 | 2.95 | 1 | = 0.557 | 0.69 [-1.42, 1.08] | medium | n.s. |
| 3 to 2 vs 3 to 6 | 0.97 | 1 | = 0.568 | 0.41 [-1.62, 0.93] | small | n.s. |
| 3 to 4 vs 3 to 5 | -1.43 | 1 | = 0.557 | -1.18 [-0.45, 1.29] | large | n.s. |
| 3 to 4 vs 3 to 6 | -1.19 | 1 | = 0.557 | -1.04 [-1.23, 1.25] | large | n.s. |
| 3 to 5 vs 3 to 6 | -0.61 | 1 | = 0.650 | -0.13 [-1.17, 1.31] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 418.21, BIC = 435.23
- Effect 1 effect: *β* = -2.86, *SE* = 2.538, *z* = -1.127, *p* = 0.260
- Effect 2 effect: *β* = -3.44, *SE* = 2.205, *z* = -1.562, *p* = 0.118
- Effect 3 effect: *β* = -2.72, *SE* = 2.316, *z* = -1.176, *p* = 0.240
- Effect 4 effect: *β* = -3.63, *SE* = 2.547, *z* = -1.427, *p* = 0.154
- Effect 5 effect: *β* = 0.25, *SE* = 0.433, *z* = 0.586, *p* = 0.558

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.830, η²_G = 0.256
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.42 | 1 | = 0.752 | -0.54 [-0.66, 1.03] | medium | n.s. |
| 3 to 1 vs 3 to 4 | -0.75 | 1 | = 0.752 | -0.93 [-0.67, 0.76] | large | n.s. |
| 3 to 1 vs 3 to 5 | -0.67 | 1 | = 0.752 | -0.82 [-0.54, 1.17] | large | n.s. |
| 3 to 1 vs 3 to 6 | -0.44 | 1 | = 0.752 | -0.61 [-1.11, 0.99] | medium | n.s. |
| 3 to 2 vs 3 to 4 | -5.60 | 1 | = 0.563 | -0.87 [-2.87, 0.08] | large | n.s. |
| 3 to 2 vs 3 to 5 | -3.25 | 1 | = 0.634 | -0.62 [-1.42, 1.08] | medium | n.s. |
| 3 to 2 vs 3 to 6 | -0.56 | 1 | = 0.752 | -0.20 [-1.12, 1.37] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | 7.48 | 1 | = 0.563 | 0.29 [-1.06, 0.63] | small | n.s. |
| 3 to 4 vs 3 to 6 | 0.79 | 1 | = 0.752 | 0.38 [-0.62, 2.24] | small | n.s. |
| 3 to 5 vs 3 to 6 | 0.41 | 1 | = 0.752 | 0.21 [-1.32, 1.17] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 381.19, BIC = 401.19
- Effect 1 effect: *β* = 0.88, *SE* = 0.515, *z* = 1.705, *p* = 0.088
- Effect 2 effect: *β* = 0.35, *SE* = 0.532, *z* = 0.653, *p* = 0.514
- Effect 3 effect: *β* = 0.18, *SE* = 0.541, *z* = 0.331, *p* = 0.741
- Effect 4 effect: *β* = -0.44, *SE* = 0.518, *z* = -0.849, *p* = 0.396
- Effect 5 effect: *β* = 0.18, *SE* = 0.044, *z* = 4.088, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.293, η²_G = 0.054
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.71 | 9 | = 0.711 | -0.22 [-0.64, 0.39] | small | n.s. |
| 3 to 1 vs 3 to 4 | -0.11 | 9 | = 0.918 | -0.03 [-0.42, 0.74] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | 0.30 | 9 | = 0.854 | 0.08 [-0.42, 0.69] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 1.13 | 9 | = 0.706 | 0.44 [-0.13, 0.90] | small | n.s. |
| 3 to 2 vs 3 to 4 | 0.71 | 9 | = 0.711 | 0.23 [-0.30, 0.88] | small | n.s. |
| 3 to 2 vs 3 to 5 | 0.98 | 9 | = 0.706 | 0.31 [-0.20, 1.00] | small | n.s. |
| 3 to 2 vs 3 to 6 | 3.04 | 9 | = 0.139 | 0.67 [0.19, 1.37] | medium | n.s. |
| 3 to 4 vs 3 to 5 | 0.44 | 9 | = 0.840 | 0.14 [-0.41, 0.81] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.90 | 9 | = 0.451 | 0.62 [0.03, 1.24] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 1.06 | 9 | = 0.706 | 0.38 [-0.23, 0.90] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 781.30, BIC = 801.30
- Effect 1 effect: *β* = 6.38, *SE* = 5.170, *z* = 1.234, *p* = 0.217
- Effect 2 effect: *β* = 8.75, *SE* = 5.287, *z* = 1.655, *p* = 0.098
- Effect 3 effect: *β* = 6.69, *SE* = 5.384, *z* = 1.242, *p* = 0.214
- Effect 4 effect: *β* = 4.34, *SE* = 5.176, *z* = 0.839, *p* = 0.402
- Effect 5 effect: *β* = 0.21, *SE* = 0.416, *z* = 0.501, *p* = 0.616

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.65, *p* = 0.182, η²_G = 0.099
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 0.35 | 9 | = 0.812 | 0.08 [-0.75, 0.29] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | -1.72 | 9 | = 0.398 | -0.74 [-1.21, 0.04] | medium | n.s. |
| 3 to 1 vs 3 to 5 | -1.54 | 9 | = 0.398 | -0.68 [-0.77, 0.35] | medium | n.s. |
| 3 to 1 vs 3 to 6 | -0.70 | 9 | = 0.624 | -0.23 [-0.74, 0.27] | small | n.s. |
| 3 to 2 vs 3 to 4 | -1.73 | 9 | = 0.398 | -0.66 [-0.77, 0.40] | medium | n.s. |
| 3 to 2 vs 3 to 5 | -1.58 | 9 | = 0.398 | -0.63 [-0.65, 0.50] | medium | n.s. |
| 3 to 2 vs 3 to 6 | -0.73 | 9 | = 0.624 | -0.26 [-0.53, 0.50] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.06 | 9 | = 0.953 | -0.01 [-0.59, 0.62] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.00 | 9 | = 0.624 | 0.51 [-0.27, 0.86] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 0.91 | 9 | = 0.624 | 0.47 [-0.25, 0.89] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.015) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 3 to 1 showed greater latency than 3 to 2 (*d* = 1.07)
  - 3 to 1 showed greater latency than 3 to 4 (*d* = 1.03)
  - 3 to 1 showed greater latency than 3 to 5 (*d* = 0.85)
  - 3 to 1 showed greater latency than 3 to 6 (*d* = 0.77)

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
