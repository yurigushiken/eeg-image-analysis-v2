# Statistical Analysis Report: tables

**Generated:** 2025-10-17 17:34:02

---

## 1. Analysis Overview

**Total Measurements:** 336
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
| 1 to 2 | 22 | -3.34 µV | 1.75 | 0.37 | [-5.99, -0.12] |
| 2 to 3 | 21 | -3.42 µV | 1.39 | 0.30 | [-5.76, -0.76] |
| 3 to 4 | 23 | -3.40 µV | 1.68 | 0.35 | [-6.99, -0.75] |
| 4 to 5 | 22 | -4.73 µV | 3.14 | 0.67 | [-12.45, -1.47] |
| 5 to 6 | 12 | -3.41 µV | 3.07 | 0.89 | [-9.38, -0.17] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | 172.17 ms | 13.23 | 2.82 | [152.74, 203.80] |
| 2 to 3 | 21 | 170.15 ms | 8.78 | 1.92 | [151.61, 192.60] |
| 3 to 4 | 23 | 168.06 ms | 11.15 | 2.33 | [142.65, 198.83] |
| 4 to 5 | 22 | 168.93 ms | 11.17 | 2.38 | [146.14, 192.29] |
| 5 to 6 | 12 | 171.10 ms | 20.79 | 6.00 | [137.69, 202.14] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 1.24 µV | 0.87 | 0.24 | [0.16, 2.76] |
| 2 to 3 | 11 | 2.21 µV | 1.21 | 0.36 | [0.83, 4.83] |
| 3 to 4 | 15 | 1.68 µV | 1.76 | 0.46 | [0.14, 5.93] |
| 4 to 5 | 15 | 3.33 µV | 4.02 | 1.04 | [-0.16, 12.43] |
| 5 to 6 | 13 | 3.44 µV | 2.79 | 0.78 | [-0.25, 8.31] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 97.85 ms | 6.86 | 1.90 | [84.55, 111.51] |
| 2 to 3 | 11 | 101.33 ms | 5.09 | 1.53 | [92.03, 108.08] |
| 3 to 4 | 15 | 101.47 ms | 8.36 | 2.16 | [86.49, 114.91] |
| 4 to 5 | 15 | 100.04 ms | 7.75 | 2.00 | [87.37, 111.38] |
| 5 to 6 | 13 | 99.87 ms | 7.34 | 2.04 | [84.31, 111.14] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 3.66 µV | 2.76 | 0.67 | [0.26, 10.26] |
| 2 to 3 | 18 | 4.09 µV | 2.94 | 0.69 | [0.70, 10.29] |
| 3 to 4 | 16 | 4.37 µV | 2.29 | 0.57 | [0.37, 7.15] |
| 4 to 5 | 16 | 4.55 µV | 2.88 | 0.72 | [0.01, 10.27] |
| 5 to 6 | 9 | 4.38 µV | 2.51 | 0.84 | [2.10, 10.44] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 488.90 ms | 17.82 | 4.32 | [446.11, 528.93] |
| 2 to 3 | 18 | 481.95 ms | 13.86 | 3.27 | [457.65, 520.64] |
| 3 to 4 | 16 | 490.15 ms | 12.35 | 3.09 | [458.14, 510.91] |
| 4 to 5 | 16 | 500.09 ms | 15.60 | 3.90 | [474.84, 535.25] |
| 5 to 6 | 9 | 493.77 ms | 13.14 | 4.38 | [472.18, 514.66] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 403.51, BIC = 424.36
- Effect 1 effect: *β* = -0.04, *SE* = 0.475, *z* = -0.086, *p* = 0.932
- Effect 2 effect: *β* = -0.22, *SE* = 0.462, *z* = -0.484, *p* = 0.628
- Effect 3 effect: *β* = -1.18, *SE* = 0.468, *z* = -2.520, *p* = 0.012
- Effect 4 effect: *β* = -0.91, *SE* = 0.578, *z* = -1.567, *p* = 0.117
- Effect 5 effect: *β* = -0.45, *SE* = 0.063, *z* = -7.157, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.45, *p* = 0.237, η²_G = 0.091
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.49 | 9 | = 0.797 | -0.20 [-0.71, 0.26] | small | n.s. |
| 1 to 2 vs 3 to 4 | -1.35 | 9 | = 0.418 | -0.45 [-0.43, 0.48] | small | n.s. |
| 1 to 2 vs 4 to 5 | 1.63 | 9 | = 0.346 | 0.57 [-0.07, 0.91] | medium | n.s. |
| 1 to 2 vs 5 to 6 | -0.20 | 9 | = 0.937 | -0.09 [-0.74, 0.60] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | -0.52 | 9 | = 0.797 | -0.30 [-0.41, 0.50] | small | n.s. |
| 2 to 3 vs 4 to 5 | 1.67 | 9 | = 0.346 | 0.75 [0.00, 1.00] | medium | n.s. |
| 2 to 3 vs 5 to 6 | 0.06 | 9 | = 0.954 | 0.03 [-0.65, 0.62] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 2.52 | 9 | = 0.328 | 0.92 [0.00, 0.96] | large | n.s. |
| 3 to 4 vs 5 to 6 | 0.51 | 9 | = 0.797 | 0.19 [-0.51, 0.77] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -1.96 | 9 | = 0.346 | -0.49 [-1.46, 0.04] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 765.57, BIC = 786.41
- Effect 1 effect: *β* = -0.56, *SE* = 2.543, *z* = -0.218, *p* = 0.827
- Effect 2 effect: *β* = -4.32, *SE* = 2.463, *z* = -1.754, *p* = 0.079
- Effect 3 effect: *β* = -2.40, *SE* = 2.498, *z* = -0.963, *p* = 0.336
- Effect 4 effect: *β* = 0.17, *SE* = 3.166, *z* = 0.053, *p* = 0.958
- Effect 5 effect: *β* = 0.01, *SE* = 0.367, *z* = 0.039, *p* = 0.969

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.18, *p* = 0.336, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.47 | 9 | = 0.584 | -0.27 [-0.62, 0.35] | small | n.s. |
| 1 to 2 vs 3 to 4 | 1.28 | 9 | = 0.584 | 0.28 [-0.12, 0.82] | small | n.s. |
| 1 to 2 vs 4 to 5 | 1.09 | 9 | = 0.605 | 0.29 [-0.32, 0.62] | small | n.s. |
| 1 to 2 vs 5 to 6 | 0.09 | 9 | = 0.975 | 0.03 [-0.62, 0.72] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 3.16 | 9 | = 0.116 | 0.58 [-0.08, 0.87] | medium | n.s. |
| 2 to 3 vs 4 to 5 | 2.68 | 9 | = 0.126 | 0.61 [-0.24, 0.71] | medium | n.s. |
| 2 to 3 vs 5 to 6 | 0.75 | 9 | = 0.675 | 0.22 [-0.58, 0.70] | small | n.s. |
| 3 to 4 vs 4 to 5 | 0.03 | 9 | = 0.975 | 0.01 [-0.72, 0.20] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | -0.58 | 9 | = 0.716 | -0.17 [-0.91, 0.39] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -0.79 | 9 | = 0.675 | -0.18 [-1.08, 0.31] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 274.18, BIC = 291.82
- Effect 1 effect: *β* = 0.85, *SE* = 0.591, *z* = 1.434, *p* = 0.151
- Effect 2 effect: *β* = 0.55, *SE* = 0.568, *z* = 0.972, *p* = 0.331
- Effect 3 effect: *β* = 1.96, *SE* = 0.560, *z* = 3.501, *p* < .001
- Effect 4 effect: *β* = 1.68, *SE* = 0.595, *z* = 2.819, *p* = 0.005
- Effect 5 effect: *β* = 1.05, *SE* = 0.130, *z* = 8.113, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.827, η²_G = 0.101
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | 0.03 | 2 | = 0.980 | 0.03 [-1.19, 0.40] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | 0.61 | 2 | = 0.856 | 0.43 [-1.25, 0.36] | small | n.s. |
| 1 to 2 vs 4 to 5 | 0.47 | 2 | = 0.856 | 0.10 [-1.17, 0.42] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -0.54 | 2 | = 0.856 | -0.29 [-1.66, 0.58] | small | n.s. |
| 2 to 3 vs 3 to 4 | 0.69 | 2 | = 0.856 | 0.61 [-0.78, 0.90] | medium | n.s. |
| 2 to 3 vs 4 to 5 | 0.12 | 2 | = 0.980 | 0.12 [-1.15, 0.56] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | -0.67 | 2 | = 0.856 | -0.71 [-1.91, 0.77] | medium | n.s. |
| 3 to 4 vs 4 to 5 | -0.67 | 2 | = 0.856 | -0.36 [-1.12, 0.36] | small | n.s. |
| 3 to 4 vs 5 to 6 | -1.01 | 2 | = 0.856 | -0.93 [-2.16, 0.12] | large | n.s. |
| 4 to 5 vs 5 to 6 | -0.78 | 2 | = 0.856 | -0.47 [-0.81, 0.87] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 457.78, BIC = 475.42
- Effect 1 effect: *β* = 2.73, *SE* = 2.240, *z* = 1.219, *p* = 0.223
- Effect 2 effect: *β* = 3.53, *SE* = 2.126, *z* = 1.663, *p* = 0.096
- Effect 3 effect: *β* = 1.24, *SE* = 2.128, *z* = 0.584, *p* = 0.559
- Effect 4 effect: *β* = 0.28, *SE* = 2.285, *z* = 0.121, *p* = 0.904
- Effect 5 effect: *β* = -0.02, *SE* = 0.505, *z* = -0.047, *p* = 0.963

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.04, *p* = 0.085, η²_G = 0.546
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -3.48 | 2 | = 0.315 | -2.75 [-1.34, 0.30] | large | n.s. |
| 1 to 2 vs 3 to 4 | -6.88 | 2 | = 0.205 | -7.86 [-1.54, 0.17] | large | n.s. |
| 1 to 2 vs 4 to 5 | -1.16 | 2 | = 0.608 | -1.12 [-1.06, 0.51] | large | n.s. |
| 1 to 2 vs 5 to 6 | -0.96 | 2 | = 0.629 | -0.85 [-1.02, 1.07] | large | n.s. |
| 2 to 3 vs 3 to 4 | -2.55 | 2 | = 0.315 | -2.34 [-1.23, 0.50] | large | n.s. |
| 2 to 3 vs 4 to 5 | 0.17 | 2 | = 0.878 | 0.16 [-0.62, 1.07] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | 0.57 | 2 | = 0.695 | 0.62 [-0.84, 1.77] | medium | n.s. |
| 3 to 4 vs 4 to 5 | 2.00 | 2 | = 0.368 | 1.26 [0.15, 1.93] | large | n.s. |
| 3 to 4 vs 5 to 6 | 2.84 | 2 | = 0.315 | 1.95 [-0.39, 1.63] | large | n.s. |
| 4 to 5 vs 5 to 6 | 0.71 | 2 | = 0.687 | 0.31 [-0.55, 1.16] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 340.31, BIC = 358.96
- Effect 1 effect: *β* = 0.10, *SE* = 0.614, *z* = 0.165, *p* = 0.869
- Effect 2 effect: *β* = 0.20, *SE* = 0.635, *z* = 0.311, *p* = 0.756
- Effect 3 effect: *β* = 1.00, *SE* = 0.629, *z* = 1.583, *p* = 0.113
- Effect 4 effect: *β* = 1.18, *SE* = 0.775, *z* = 1.523, *p* = 0.128
- Effect 5 effect: *β* = 0.43, *SE* = 0.076, *z* = 5.609, *p* < .001

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.268, η²_G = 0.107
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -2.56 | 6 | = 0.253 | -0.75 [-1.06, 0.15] | medium | n.s. |
| 1 to 2 vs 3 to 4 | -2.44 | 6 | = 0.253 | -0.72 [-0.72, 0.49] | medium | n.s. |
| 1 to 2 vs 4 to 5 | -1.44 | 6 | = 0.565 | -0.70 [-0.75, 0.47] | medium | n.s. |
| 1 to 2 vs 5 to 6 | -0.27 | 6 | = 0.922 | -0.11 [-1.10, 0.60] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 0.71 | 6 | = 0.720 | 0.08 [-0.69, 0.47] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.22 | 6 | = 0.922 | 0.11 [-0.61, 0.60] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | 1.13 | 6 | = 0.565 | 0.58 [-0.52, 1.20] | medium | n.s. |
| 3 to 4 vs 4 to 5 | 0.07 | 6 | = 0.946 | 0.03 [-0.61, 0.60] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 1.04 | 6 | = 0.565 | 0.54 [-0.57, 1.35] | medium | n.s. |
| 4 to 5 vs 5 to 6 | 1.16 | 6 | = 0.565 | 0.52 [-0.38, 1.23] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 636.43, BIC = 655.08
- Effect 1 effect: *β* = -7.14, *SE* = 4.855, *z* = -1.472, *p* = 0.141
- Effect 2 effect: *β* = 1.04, *SE* = 5.002, *z* = 0.209, *p* = 0.834
- Effect 3 effect: *β* = 11.36, *SE* = 5.026, *z* = 2.260, *p* = 0.024
- Effect 4 effect: *β* = 5.41, *SE* = 6.091, *z* = 0.889, *p* = 0.374
- Effect 5 effect: *β* = 0.24, *SE* = 0.543, *z* = 0.449, *p* = 0.653

_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.34, *p* = 0.009, η²_G = 0.336
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.32 | 6 | = 0.757 | -0.12 [-0.45, 0.71] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -2.44 | 6 | = 0.167 | -1.02 [-0.74, 0.48] | large | n.s. |
| 1 to 2 vs 4 to 5 | -3.29 | 6 | = 0.098 | -1.61 [-1.56, -0.15] | large | n.s. |
| 1 to 2 vs 5 to 6 | -2.24 | 6 | = 0.167 | -1.08 [-1.78, 0.15] | large | n.s. |
| 2 to 3 vs 3 to 4 | -1.65 | 6 | = 0.213 | -1.06 [-0.91, 0.28] | large | n.s. |
| 2 to 3 vs 4 to 5 | -3.16 | 6 | = 0.098 | -1.73 [-1.78, -0.28] | large | n.s. |
| 2 to 3 vs 5 to 6 | -1.78 | 6 | = 0.211 | -1.10 [-1.62, 0.24] | large | n.s. |
| 3 to 4 vs 4 to 5 | -1.77 | 6 | = 0.211 | -0.79 [-1.06, 0.20] | medium | n.s. |
| 3 to 4 vs 5 to 6 | -0.49 | 6 | = 0.711 | -0.23 [-1.12, 0.75] | small | n.s. |
| 4 to 5 vs 5 to 6 | 0.85 | 6 | = 0.537 | 0.43 [-0.44, 1.14] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Marginal trend toward condition differences (*p* = 0.085)
**P3b latency:** Significant main effect of condition (*p* = 0.009) (no significant pairwise comparisons)

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
