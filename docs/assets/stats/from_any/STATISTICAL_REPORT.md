# Statistical Analysis Report: tables

**Generated:** 2025-10-17 00:51:46

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
| from 1 | 24 | -3.24 µV | 1.78 | 0.36 | [-8.35, -0.15] |
| from 2 | 23 | -3.06 µV | 1.51 | 0.32 | [-6.77, 0.01] |
| from 3 | 22 | -3.48 µV | 1.52 | 0.33 | [-7.59, -1.60] |
| from 4 | 24 | -3.36 µV | 1.81 | 0.37 | [-8.29, 0.02] |
| from 5 | 23 | -4.17 µV | 1.85 | 0.39 | [-8.17, -0.65] |
| from 6 | 24 | -3.69 µV | 1.79 | 0.37 | [-7.18, -1.27] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 175.22 ms | 10.09 | 2.06 | [157.81, 201.97] |
| from 2 | 23 | 175.00 ms | 9.93 | 2.07 | [158.97, 203.64] |
| from 3 | 22 | 172.75 ms | 6.89 | 1.47 | [158.77, 187.36] |
| from 4 | 24 | 175.20 ms | 8.72 | 1.78 | [159.50, 203.96] |
| from 5 | 23 | 173.93 ms | 6.37 | 1.33 | [157.22, 186.57] |
| from 6 | 24 | 174.00 ms | 9.13 | 1.86 | [159.91, 194.67] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 15 | 1.39 µV | 1.36 | 0.35 | [0.17, 4.89] |
| from 2 | 15 | 1.45 µV | 1.51 | 0.39 | [0.08, 4.92] |
| from 3 | 16 | 1.21 µV | 1.30 | 0.33 | [0.11, 4.87] |
| from 4 | 13 | 1.50 µV | 1.35 | 0.38 | [0.02, 3.71] |
| from 5 | 15 | 1.38 µV | 1.01 | 0.26 | [0.14, 3.20] |
| from 6 | 12 | 1.83 µV | 1.34 | 0.39 | [0.58, 5.50] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 15 | 105.50 ms | 4.46 | 1.15 | [98.94, 113.70] |
| from 2 | 15 | 104.99 ms | 4.73 | 1.22 | [96.28, 112.44] |
| from 3 | 16 | 105.37 ms | 5.22 | 1.30 | [94.79, 112.73] |
| from 4 | 13 | 106.26 ms | 4.60 | 1.27 | [94.17, 114.71] |
| from 5 | 15 | 104.50 ms | 5.69 | 1.47 | [93.76, 112.51] |
| from 6 | 12 | 107.09 ms | 2.65 | 0.77 | [103.57, 111.38] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 17 | 3.21 µV | 2.27 | 0.55 | [0.37, 8.57] |
| from 2 | 19 | 3.07 µV | 2.00 | 0.46 | [0.04, 6.09] |
| from 3 | 19 | 3.06 µV | 2.05 | 0.47 | [0.08, 7.58] |
| from 4 | 17 | 3.22 µV | 1.97 | 0.48 | [0.12, 6.49] |
| from 5 | 18 | 2.53 µV | 1.61 | 0.38 | [0.01, 5.26] |
| from 6 | 18 | 2.53 µV | 1.86 | 0.44 | [0.11, 6.18] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 17 | 473.52 ms | 10.32 | 2.50 | [447.42, 494.73] |
| from 2 | 19 | 472.72 ms | 14.18 | 3.25 | [422.58, 485.84] |
| from 3 | 19 | 476.61 ms | 15.42 | 3.54 | [456.92, 527.62] |
| from 4 | 17 | 479.96 ms | 13.37 | 3.24 | [454.86, 509.96] |
| from 5 | 18 | 472.22 ms | 10.95 | 2.58 | [448.53, 486.88] |
| from 6 | 18 | 473.52 ms | 21.27 | 5.01 | [425.11, 524.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 6.73, *p* < .001, η²_G = 0.052
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.689)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -2.21 | 21 | = 0.071 | -0.24 [-0.84, 0.05] | small | n.s. |
| from 1 vs from 3 | -0.17 | 21 | = 0.867 | -0.02 [-0.48, 0.41] | negligible | n.s. |
| from 1 vs from 4 | 0.45 | 21 | = 0.703 | 0.06 [-0.31, 0.54] | negligible | n.s. |
| from 1 vs from 5 | 3.47 | 21 | = 0.011 | 0.49 [0.26, 1.23] | small | * |
| from 1 vs from 6 | 1.42 | 21 | = 0.234 | 0.23 [-0.08, 0.80] | small | n.s. |
| from 2 vs from 3 | 1.85 | 21 | = 0.130 | 0.23 [-0.07, 0.86] | small | n.s. |
| from 2 vs from 4 | 2.41 | 21 | = 0.058 | 0.30 [-0.03, 0.87] | small | n.s. |
| from 2 vs from 5 | 5.22 | 21 | < .001 | 0.73 [0.55, 1.68] | medium | *** |
| from 2 vs from 6 | 3.67 | 21 | = 0.011 | 0.47 [0.27, 1.26] | small | * |
| from 3 vs from 4 | 0.83 | 21 | = 0.481 | 0.09 [-0.27, 0.62] | negligible | n.s. |
| from 3 vs from 5 | 3.12 | 21 | = 0.020 | 0.52 [0.17, 1.15] | medium | * |
| from 3 vs from 6 | 1.66 | 21 | = 0.169 | 0.26 [-0.10, 0.81] | small | n.s. |
| from 4 vs from 5 | 2.97 | 21 | = 0.022 | 0.42 [0.12, 1.06] | small | * |
| from 4 vs from 6 | 1.11 | 21 | = 0.351 | 0.17 [-0.15, 0.71] | negligible | n.s. |
| from 5 vs from 6 | -2.37 | 21 | = 0.058 | -0.25 [-0.89, 0.01] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 398.83, BIC = 422.36
- Condition effect: *β* = 0.30, *SE* = 0.208, *z* = 1.454, *p* = 0.146

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.68, *p* = 0.637, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.542 (ε = 0.503)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.32 | 21 | = 0.782 | -0.15 [-0.64, 0.23] | negligible | n.s. |
| from 1 vs from 3 | 0.15 | 21 | = 0.983 | 0.01 [-0.41, 0.47] | negligible | n.s. |
| from 1 vs from 4 | -0.93 | 21 | = 0.782 | -0.09 [-0.42, 0.43] | negligible | n.s. |
| from 1 vs from 5 | -0.74 | 21 | = 0.782 | -0.09 [-0.41, 0.46] | negligible | n.s. |
| from 1 vs from 6 | 0.27 | 21 | = 0.983 | 0.02 [-0.18, 0.68] | negligible | n.s. |
| from 2 vs from 3 | 1.32 | 21 | = 0.782 | 0.16 [-0.17, 0.73] | negligible | n.s. |
| from 2 vs from 4 | 0.47 | 21 | = 0.920 | 0.08 [-0.39, 0.47] | negligible | n.s. |
| from 2 vs from 5 | 0.43 | 21 | = 0.920 | 0.08 [-0.35, 0.54] | negligible | n.s. |
| from 2 vs from 6 | 1.65 | 21 | = 0.782 | 0.16 [-0.08, 0.81] | negligible | n.s. |
| from 3 vs from 4 | -0.86 | 21 | = 0.782 | -0.10 [-0.63, 0.26] | negligible | n.s. |
| from 3 vs from 5 | -0.84 | 21 | = 0.782 | -0.10 [-0.63, 0.27] | negligible | n.s. |
| from 3 vs from 6 | 0.10 | 21 | = 0.983 | 0.01 [-0.42, 0.47] | negligible | n.s. |
| from 4 vs from 5 | -0.02 | 21 | = 0.983 | -0.00 [-0.43, 0.44] | negligible | n.s. |
| from 4 vs from 6 | 0.81 | 21 | = 0.782 | 0.10 [-0.16, 0.70] | negligible | n.s. |
| from 5 vs from 6 | 0.74 | 21 | = 0.782 | 0.11 [-0.26, 0.61] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 826.89, BIC = 850.42
- Condition effect: *β* = 0.35, *SE* = 0.931, *z* = 0.378, *p* = 0.705


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 0.75, *p* = 0.593, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.14 | 5 | = 0.919 | -0.05 [-0.64, 0.63] | negligible | n.s. |
| from 1 vs from 3 | 0.58 | 5 | = 0.907 | 0.29 [-0.54, 0.74] | small | n.s. |
| from 1 vs from 4 | 0.81 | 5 | = 0.851 | 0.38 [-0.61, 0.74] | small | n.s. |
| from 1 vs from 5 | 1.08 | 5 | = 0.710 | 0.53 [-0.43, 0.85] | medium | n.s. |
| from 1 vs from 6 | 0.11 | 5 | = 0.919 | 0.05 [-0.76, 0.68] | negligible | n.s. |
| from 2 vs from 3 | 1.36 | 5 | = 0.710 | 0.30 [-0.42, 0.87] | small | n.s. |
| from 2 vs from 4 | 1.50 | 5 | = 0.710 | 0.38 [-0.65, 0.69] | small | n.s. |
| from 2 vs from 5 | 1.35 | 5 | = 0.710 | 0.50 [-0.51, 0.84] | medium | n.s. |
| from 2 vs from 6 | 0.43 | 5 | = 0.907 | 0.09 [-0.66, 0.68] | negligible | n.s. |
| from 3 vs from 4 | 0.27 | 5 | = 0.919 | 0.06 [-0.82, 0.46] | negligible | n.s. |
| from 3 vs from 5 | 0.49 | 5 | = 0.907 | 0.15 [-0.93, 0.36] | negligible | n.s. |
| from 3 vs from 6 | -1.97 | 5 | = 0.710 | -0.22 [-1.61, -0.05] | small | n.s. |
| from 4 vs from 5 | 0.37 | 5 | = 0.907 | 0.09 [-1.04, 0.43] | negligible | n.s. |
| from 4 vs from 6 | -1.31 | 5 | = 0.710 | -0.30 [-1.06, 0.51] | small | n.s. |
| from 5 vs from 6 | -1.17 | 5 | = 0.710 | -0.42 [-0.87, 0.48] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 250.15, BIC = 269.79
- Condition effect: *β* = -0.02, *SE* = 0.280, *z* = -0.058, *p* = 0.954

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 1.36, *p* = 0.274, η²_G = 0.104
- Greenhouse-Geisser corrected: *p* = 0.302 (ε = 0.379)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 1.01 | 5 | = 0.505 | 0.42 [-0.56, 0.71] | small | n.s. |
| from 1 vs from 3 | -1.47 | 5 | = 0.505 | -0.66 [-0.68, 0.59] | medium | n.s. |
| from 1 vs from 4 | -0.98 | 5 | = 0.505 | -0.47 [-1.24, 0.19] | small | n.s. |
| from 1 vs from 5 | -0.57 | 5 | = 0.687 | -0.25 [-0.47, 0.81] | small | n.s. |
| from 1 vs from 6 | -0.67 | 5 | = 0.669 | -0.21 [-1.21, 0.30] | small | n.s. |
| from 2 vs from 3 | -1.33 | 5 | = 0.505 | -0.89 [-0.69, 0.58] | large | n.s. |
| from 2 vs from 4 | -1.62 | 5 | = 0.505 | -0.72 [-0.82, 0.53] | medium | n.s. |
| from 2 vs from 5 | -1.07 | 5 | = 0.505 | -0.55 [-0.85, 0.50] | medium | n.s. |
| from 2 vs from 6 | -1.31 | 5 | = 0.505 | -0.56 [-1.19, 0.23] | medium | n.s. |
| from 3 vs from 4 | 0.20 | 5 | = 0.852 | 0.08 [-0.62, 0.65] | negligible | n.s. |
| from 3 vs from 5 | 1.09 | 5 | = 0.505 | 0.33 [-0.51, 0.77] | small | n.s. |
| from 3 vs from 6 | 1.24 | 5 | = 0.505 | 0.45 [-0.96, 0.41] | small | n.s. |
| from 4 vs from 5 | 1.43 | 5 | = 0.505 | 0.22 [-0.17, 1.39] | small | n.s. |
| from 4 vs from 6 | 1.14 | 5 | = 0.505 | 0.30 [-0.72, 0.81] | small | n.s. |
| from 5 vs from 6 | 0.33 | 5 | = 0.808 | 0.07 [-0.86, 0.49] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 500.85, BIC = 520.48
- Condition effect: *β* = -0.80, *SE* = 1.240, *z* = -0.648, *p* = 0.517


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Repeated-Measures ANOVA:**

- *F* = 2.36, *p* = 0.048, η²_G = 0.035
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.42 | 15 | = 0.877 | -0.08 [-0.60, 0.43] | negligible | n.s. |
| from 1 vs from 3 | -0.39 | 15 | = 0.877 | -0.08 [-0.63, 0.40] | negligible | n.s. |
| from 1 vs from 4 | -0.09 | 15 | = 0.976 | -0.02 [-0.55, 0.51] | negligible | n.s. |
| from 1 vs from 5 | 1.57 | 15 | = 0.296 | 0.31 [-0.14, 0.93] | small | n.s. |
| from 1 vs from 6 | 1.40 | 15 | = 0.343 | 0.32 [-0.24, 0.81] | small | n.s. |
| from 2 vs from 3 | 0.03 | 15 | = 0.976 | 0.00 [-0.56, 0.43] | negligible | n.s. |
| from 2 vs from 4 | 0.60 | 15 | = 0.836 | 0.07 [-0.39, 0.69] | negligible | n.s. |
| from 2 vs from 5 | 3.14 | 15 | = 0.100 | 0.46 [0.17, 1.33] | small | n.s. |
| from 2 vs from 6 | 2.08 | 15 | = 0.189 | 0.45 [-0.12, 0.91] | small | n.s. |
| from 3 vs from 4 | 0.68 | 15 | = 0.836 | 0.07 [-0.36, 0.68] | negligible | n.s. |
| from 3 vs from 5 | 2.69 | 15 | = 0.126 | 0.44 [0.09, 1.18] | small | n.s. |
| from 3 vs from 6 | 2.01 | 15 | = 0.189 | 0.44 [-0.08, 0.96] | small | n.s. |
| from 4 vs from 5 | 2.33 | 15 | = 0.170 | 0.36 [-0.02, 1.08] | small | n.s. |
| from 4 vs from 6 | 1.81 | 15 | = 0.226 | 0.37 [-0.11, 1.01] | small | n.s. |
| from 5 vs from 6 | 0.23 | 15 | = 0.952 | 0.05 [-0.53, 0.50] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 363.86, BIC = 385.32
- Condition effect: *β* = 0.08, *SE* = 0.313, *z* = 0.264, *p* = 0.792

#### Latency (50% Fractional Area)

**Repeated-Measures ANOVA:**

- *F* = 0.33, *p* = 0.896, η²_G = 0.012
- Greenhouse-Geisser corrected: *p* = 0.738 (ε = 0.428)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.21 | 15 | = 0.997 | -0.05 [-0.71, 0.33] | negligible | n.s. |
| from 1 vs from 3 | -0.06 | 15 | = 0.997 | -0.02 [-0.64, 0.39] | negligible | n.s. |
| from 1 vs from 4 | -1.11 | 15 | = 0.997 | -0.30 [-0.82, 0.27] | small | n.s. |
| from 1 vs from 5 | 0.57 | 15 | = 0.997 | 0.15 [-0.39, 0.65] | negligible | n.s. |
| from 1 vs from 6 | -0.03 | 15 | = 0.997 | -0.01 [-0.61, 0.42] | negligible | n.s. |
| from 2 vs from 3 | 0.14 | 15 | = 0.997 | 0.03 [-0.62, 0.38] | negligible | n.s. |
| from 2 vs from 4 | -1.33 | 15 | = 0.997 | -0.26 [-0.88, 0.22] | small | n.s. |
| from 2 vs from 5 | 0.70 | 15 | = 0.997 | 0.20 [-0.25, 0.80] | negligible | n.s. |
| from 2 vs from 6 | 0.06 | 15 | = 0.997 | 0.02 [-0.56, 0.44] | negligible | n.s. |
| from 3 vs from 4 | -0.91 | 15 | = 0.997 | -0.28 [-0.64, 0.39] | small | n.s. |
| from 3 vs from 5 | 0.70 | 15 | = 0.997 | 0.16 [-0.16, 0.86] | negligible | n.s. |
| from 3 vs from 6 | -0.00 | 15 | = 0.997 | -0.00 [-0.49, 0.51] | negligible | n.s. |
| from 4 vs from 5 | 1.65 | 15 | = 0.997 | 0.40 [-0.06, 1.02] | small | n.s. |
| from 4 vs from 6 | 0.62 | 15 | = 0.997 | 0.17 [-0.38, 0.69] | negligible | n.s. |
| from 5 vs from 6 | -0.31 | 15 | = 0.997 | -0.09 [-0.68, 0.35] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 871.22, BIC = 892.68
- Condition effect: *β* = 0.57, *SE* = 3.609, *z* = 0.157, *p* = 0.875


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed greater amplitude than from 5 (*d* = 0.49)
  - from 2 showed greater amplitude than from 5 (*d* = 0.73)
  - from 2 showed greater amplitude than from 6 (*d* = 0.47)
  - from 3 showed greater amplitude than from 5 (*d* = 0.52)
  - from 4 showed greater amplitude than from 5 (*d* = 0.42)
**P3b amplitude:** Significant main effect of condition (*p* = 0.048) (no significant pairwise comparisons)

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
