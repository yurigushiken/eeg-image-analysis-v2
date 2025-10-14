# Statistical Analysis Report: tables

**Generated:** 2025-10-14 02:11:00

---

## 1. Analysis Overview

**Total Measurements:** 432
**Number of Subjects:** 24
**Number of Conditions:** 6

**Components Analyzed:** N1, P1, P3b
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

### 2.1 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | 177.87 ms | 19.18 | 4.95 | [144.00, 204.00] |
| Cardinality2 | 22 | 174.36 ms | 20.72 | 4.42 | [144.00, 204.00] |
| Cardinality3 | 22 | 168.18 ms | 15.93 | 3.40 | [144.00, 200.00] |
| Cardinality4 | 22 | 171.27 ms | 19.93 | 4.25 | [144.00, 204.00] |
| Cardinality5 | 24 | 171.67 ms | 16.04 | 3.27 | [144.00, 196.00] |
| Cardinality6 | 23 | 174.26 ms | 16.04 | 3.34 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | -4.90 µV | 1.85 | 0.48 | [-9.64, -2.66] |
| Cardinality2 | 22 | -5.64 µV | 2.44 | 0.52 | [-10.50, -1.57] |
| Cardinality3 | 22 | -5.19 µV | 2.04 | 0.43 | [-10.83, -1.55] |
| Cardinality4 | 22 | -5.95 µV | 3.12 | 0.67 | [-13.09, -1.82] |
| Cardinality5 | 24 | -5.96 µV | 2.55 | 0.52 | [-12.06, -1.67] |
| Cardinality6 | 23 | -5.73 µV | 2.88 | 0.60 | [-11.14, -0.87] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 113.68 ms | 8.88 | 2.04 | [96.00, 120.00] |
| Cardinality2 | 12 | 107.00 ms | 10.25 | 2.96 | [96.00, 120.00] |
| Cardinality3 | 14 | 110.00 ms | 9.25 | 2.47 | [96.00, 120.00] |
| Cardinality4 | 12 | 109.67 ms | 9.57 | 2.76 | [96.00, 120.00] |
| Cardinality5 | 14 | 106.00 ms | 7.32 | 1.96 | [96.00, 120.00] |
| Cardinality6 | 12 | 109.00 ms | 8.20 | 2.37 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 4.41 µV | 2.89 | 0.66 | [1.20, 13.26] |
| Cardinality2 | 12 | 3.07 µV | 1.84 | 0.53 | [1.36, 7.57] |
| Cardinality3 | 14 | 3.25 µV | 2.36 | 0.63 | [0.79, 8.96] |
| Cardinality4 | 12 | 3.28 µV | 1.83 | 0.53 | [0.96, 6.93] |
| Cardinality5 | 14 | 2.66 µV | 1.69 | 0.45 | [0.35, 5.37] |
| Cardinality6 | 12 | 2.97 µV | 2.08 | 0.60 | [0.77, 8.25] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 461.71 ms | 14.53 | 3.88 | [440.00, 480.00] |
| Cardinality2 | 13 | 456.31 ms | 15.36 | 4.26 | [440.00, 480.00] |
| Cardinality3 | 16 | 458.25 ms | 11.59 | 2.90 | [440.00, 476.00] |
| Cardinality4 | 11 | 455.27 ms | 8.73 | 2.63 | [440.00, 472.00] |
| Cardinality5 | 14 | 455.14 ms | 16.17 | 4.32 | [440.00, 480.00] |
| Cardinality6 | 14 | 466.57 ms | 14.09 | 3.76 | [440.00, 480.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 3.04 µV | 1.84 | 0.49 | [1.05, 7.06] |
| Cardinality2 | 13 | 3.78 µV | 2.08 | 0.58 | [0.41, 8.49] |
| Cardinality3 | 16 | 4.49 µV | 2.23 | 0.56 | [1.30, 9.60] |
| Cardinality4 | 11 | 4.18 µV | 2.57 | 0.78 | [0.65, 8.96] |
| Cardinality5 | 14 | 2.64 µV | 1.36 | 0.36 | [0.35, 5.39] |
| Cardinality6 | 14 | 4.55 µV | 2.34 | 0.63 | [1.85, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.06, *p* = 0.394, η²_G = 0.032
- Greenhouse-Geisser corrected: *p* = 0.372 (ε = 0.477)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.25 | 11 | = 0.869 | 0.09 [-0.43, 0.68] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 1.81 | 11 | = 0.488 | 0.43 [-0.09, 1.21] | small | n.s. |
| Cardinality1 vs Cardinality4 | 2.05 | 11 | = 0.488 | 0.52 [-0.06, 1.18] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 1.05 | 11 | = 0.666 | 0.30 [-0.10, 1.07] | small | n.s. |
| Cardinality1 vs Cardinality6 | 0.48 | 11 | = 0.743 | 0.15 [-0.32, 0.80] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.90 | 11 | = 0.666 | 0.26 [-0.17, 0.78] | small | n.s. |
| Cardinality2 vs Cardinality4 | 1.05 | 11 | = 0.666 | 0.35 [-0.31, 0.60] | small | n.s. |
| Cardinality2 vs Cardinality5 | 0.64 | 11 | = 0.668 | 0.15 [-0.33, 0.56] | negligible | n.s. |
| Cardinality2 vs Cardinality6 | 0.13 | 11 | = 0.900 | 0.04 [-0.37, 0.52] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | 0.79 | 11 | = 0.668 | 0.13 [-0.53, 0.40] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | -0.88 | 11 | = 0.666 | -0.14 [-0.64, 0.26] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -1.62 | 11 | = 0.497 | -0.28 [-0.73, 0.19] | small | n.s. |
| Cardinality4 vs Cardinality5 | -1.12 | 11 | = 0.666 | -0.26 [-0.47, 0.41] | small | n.s. |
| Cardinality4 vs Cardinality6 | -2.05 | 11 | = 0.488 | -0.37 [-0.68, 0.22] | small | n.s. |
| Cardinality5 vs Cardinality6 | -0.69 | 11 | = 0.668 | -0.14 [-0.53, 0.34] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 1053.48, BIC = 1076.30
- Condition effect: *β* = -3.22, *SE* = 3.887, *z* = -0.829, *p* = 0.407

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.29, *p* = 0.280, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.90 | 11 | = 0.632 | 0.39 [-0.25, 0.89] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.07 | 11 | = 0.632 | 0.36 [-0.26, 0.98] | small | n.s. |
| Cardinality1 vs Cardinality4 | 1.30 | 11 | = 0.632 | 0.50 [-0.24, 0.95] | small | n.s. |
| Cardinality1 vs Cardinality5 | 2.33 | 11 | = 0.593 | 0.87 [-0.06, 1.12] | large | n.s. |
| Cardinality1 vs Cardinality6 | 1.19 | 11 | = 0.632 | 0.40 [-0.17, 0.98] | small | n.s. |
| Cardinality2 vs Cardinality3 | -0.34 | 11 | = 0.792 | -0.07 [-0.61, 0.33] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | 0.82 | 11 | = 0.632 | 0.18 [-0.27, 0.65] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 1.11 | 11 | = 0.632 | 0.36 [-0.27, 0.62] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.25 | 11 | = 0.804 | 0.06 [-0.32, 0.57] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | 0.93 | 11 | = 0.632 | 0.24 [-0.14, 0.82] | small | n.s. |
| Cardinality3 vs Cardinality5 | 1.65 | 11 | = 0.632 | 0.47 [-0.04, 0.89] | small | n.s. |
| Cardinality3 vs Cardinality6 | 0.51 | 11 | = 0.779 | 0.12 [-0.24, 0.68] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.39 | 11 | = 0.792 | 0.10 [-0.46, 0.43] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -0.76 | 11 | = 0.632 | -0.10 [-0.56, 0.33] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -1.05 | 11 | = 0.632 | -0.24 [-0.53, 0.33] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 566.20, BIC = 589.01
- Condition effect: *β* = -0.97, *SE* = 0.594, *z* = -1.626, *p* = 0.104


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.68, *p* = 0.176, η²_G = 0.218
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.69 | 5 | = 0.441 | 1.01 [-0.25, 1.07] | large | n.s. |
| Cardinality1 vs Cardinality3 | 1.51 | 5 | = 0.441 | 0.89 [-0.10, 1.28] | large | n.s. |
| Cardinality1 vs Cardinality4 | 1.35 | 5 | = 0.441 | 0.69 [-0.17, 1.17] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 3.00 | 5 | = 0.316 | 1.82 [-0.10, 1.20] | large | n.s. |
| Cardinality1 vs Cardinality6 | 2.09 | 5 | = 0.441 | 1.18 [-0.30, 1.20] | large | n.s. |
| Cardinality2 vs Cardinality3 | -0.10 | 5 | = 0.988 | -0.07 [-0.85, 0.59] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -0.94 | 5 | = 0.533 | -0.54 [-0.81, 0.73] | medium | n.s. |
| Cardinality2 vs Cardinality5 | 0.75 | 5 | = 0.610 | 0.53 [-0.60, 0.84] | medium | n.s. |
| Cardinality2 vs Cardinality6 | -0.13 | 5 | = 0.988 | -0.08 [-0.98, 0.70] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.96 | 5 | = 0.533 | -0.45 [-1.02, 0.66] | small | n.s. |
| Cardinality3 vs Cardinality5 | 1.35 | 5 | = 0.441 | 0.60 [-0.38, 1.23] | medium | n.s. |
| Cardinality3 vs Cardinality6 | 0.00 | 5 | = 1.000 | 0.00 [-0.42, 1.18] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 1.86 | 5 | = 0.441 | 1.23 [-0.43, 1.03] | large | n.s. |
| Cardinality4 vs Cardinality6 | 2.71 | 5 | = 0.316 | 0.55 [-0.90, 0.77] | medium | n.s. |
| Cardinality5 vs Cardinality6 | -1.14 | 5 | = 0.512 | -0.69 [-1.14, 0.26] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 604.96, BIC = 624.31
- Condition effect: *β* = -6.70, *SE* = 2.912, *z* = -2.302, *p* = 0.021

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.38, *p* = 0.265, η²_G = 0.151
- Greenhouse-Geisser corrected: *p* = 0.293 (ε = 0.472)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 2.95 | 5 | = 0.480 | 0.75 [0.07, 1.53] | medium | n.s. |
| Cardinality1 vs Cardinality3 | 1.49 | 5 | = 0.647 | 0.84 [-0.17, 1.19] | large | n.s. |
| Cardinality1 vs Cardinality4 | 1.70 | 5 | = 0.647 | 0.70 [-0.12, 1.25] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 1.61 | 5 | = 0.647 | 0.96 [-0.03, 1.29] | large | n.s. |
| Cardinality1 vs Cardinality6 | 1.42 | 5 | = 0.647 | 0.72 [-0.15, 1.42] | medium | n.s. |
| Cardinality2 vs Cardinality3 | 0.24 | 5 | = 0.909 | 0.13 [-1.01, 0.45] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -0.40 | 5 | = 0.909 | -0.13 [-1.17, 0.42] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 0.46 | 5 | = 0.909 | 0.29 [-0.52, 0.92] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.00 | 5 | = 0.997 | 0.00 [-0.73, 0.95] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.70 | 5 | = 0.909 | -0.27 [-1.22, 0.50] | small | n.s. |
| Cardinality3 vs Cardinality5 | 0.20 | 5 | = 0.909 | 0.15 [-0.55, 1.00] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -0.36 | 5 | = 0.909 | -0.11 [-0.54, 1.02] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.65 | 5 | = 0.909 | 0.46 [-0.41, 1.06] | small | n.s. |
| Cardinality4 vs Cardinality6 | 0.44 | 5 | = 0.909 | 0.12 [-0.92, 0.75] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -0.37 | 5 | = 0.909 | -0.26 [-0.75, 0.59] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 367.23, BIC = 386.58
- Condition effect: *β* = -1.59, *SE* = 0.675, *z* = -2.361, *p* = 0.018


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 3.67, *p* = 0.090, η²_G = 0.675
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.40 | 1 | = 0.758 | 0.44 [-0.25, 1.28] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.80 | 1 | = 0.536 | 2.18 [-0.53, 0.83] | large | n.s. |
| Cardinality1 vs Cardinality4 | 2.50 | 1 | = 0.536 | 3.16 [-0.82, 1.31] | large | n.s. |
| Cardinality1 vs Cardinality5 | 13.00 | 1 | = 0.339 | 13.00 [-0.55, 1.01] | large | n.s. |
| Cardinality1 vs Cardinality6 | -1.67 | 1 | = 0.536 | -2.24 [-0.98, 0.48] | large | n.s. |
| Cardinality2 vs Cardinality3 | 1.00 | 1 | = 0.536 | 0.51 [-0.74, 0.53] | medium | n.s. |
| Cardinality2 vs Cardinality4 | 1.00 | 1 | = 0.536 | 0.63 [-0.33, 2.18] | medium | n.s. |
| Cardinality2 vs Cardinality5 | 1.00 | 1 | = 0.536 | 1.00 [-0.70, 0.64] | large | n.s. |
| Cardinality2 vs Cardinality6 | -1.29 | 1 | = 0.536 | -0.98 [-1.38, 0.27] | large | n.s. |
| Cardinality3 vs Cardinality4 | 1.00 | 1 | = 0.536 | 0.20 [-0.57, 1.14] | small | n.s. |
| Cardinality3 vs Cardinality5 | 1.00 | 1 | = 0.536 | 1.00 [-0.62, 0.65] | large | n.s. |
| Cardinality3 vs Cardinality6 | -7.00 | 1 | = 0.339 | -3.13 [-1.43, 0.14] | large | n.s. |
| Cardinality4 vs Cardinality5 | 1.00 | 1 | = 0.536 | 1.00 [-0.86, 0.81] | large | n.s. |
| Cardinality4 vs Cardinality6 | -15.00 | 1 | = 0.339 | -4.16 [-1.25, 0.36] | large | n.s. |
| Cardinality5 vs Cardinality6 | -9.00 | 1 | = 0.339 | -9.00 [-1.73, 0.06] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 672.09, BIC = 691.35
- Condition effect: *β* = -5.41, *SE* = 5.106, *z* = -1.059, *p* = 0.290

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 0.41, *p* = 0.827, η²_G = 0.220
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.76 | 1 | = 0.824 | 0.60 [-0.86, 0.58] | medium | n.s. |
| Cardinality1 vs Cardinality3 | -0.25 | 1 | = 0.985 | -0.34 [-1.28, 0.16] | small | n.s. |
| Cardinality1 vs Cardinality4 | 0.66 | 1 | = 0.985 | 0.06 [-1.45, 0.72] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | 0.04 | 1 | = 0.985 | 0.05 [-0.85, 0.69] | negligible | n.s. |
| Cardinality1 vs Cardinality6 | -2.75 | 1 | = 0.824 | -0.46 [-1.42, 0.15] | small | n.s. |
| Cardinality2 vs Cardinality3 | -0.93 | 1 | = 0.985 | -1.32 [-0.95, 0.35] | large | n.s. |
| Cardinality2 vs Cardinality4 | -2.23 | 1 | = 0.824 | -0.58 [-1.92, 0.45] | medium | n.s. |
| Cardinality2 vs Cardinality5 | -0.66 | 1 | = 0.985 | -0.91 [-0.43, 0.93] | large | n.s. |
| Cardinality2 vs Cardinality6 | -2.16 | 1 | = 0.824 | -1.03 [-1.04, 0.52] | large | n.s. |
| Cardinality3 vs Cardinality4 | 0.32 | 1 | = 0.985 | 0.45 [-0.69, 0.99] | small | n.s. |
| Cardinality3 vs Cardinality5 | 2.36 | 1 | = 0.824 | 0.64 [-0.02, 1.39] | medium | n.s. |
| Cardinality3 vs Cardinality6 | -0.19 | 1 | = 0.985 | -0.25 [-0.65, 0.78] | small | n.s. |
| Cardinality4 vs Cardinality5 | -0.02 | 1 | = 0.985 | -0.03 [-0.45, 1.30] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -2.10 | 1 | = 0.824 | -0.53 [-0.90, 0.64] | medium | n.s. |
| Cardinality5 vs Cardinality6 | -0.48 | 1 | = 0.985 | -0.60 [-1.39, 0.26] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 347.69, BIC = 366.94
- Condition effect: *β* = 0.65, *SE* = 0.622, *z* = 1.040, *p* = 0.298


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Marginal trend toward condition differences (*p* = 0.090)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

#### Latency

#### Amplitude

### 5.2 P1 Component

#### Latency

#### Amplitude

### 5.3 P3b Component

#### Latency

#### Amplitude

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
