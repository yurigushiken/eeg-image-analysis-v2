# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:15:00

---

## 1. Analysis Overview

**Total Measurements:** 576
**Number of Subjects:** 24
**Number of Conditions:** 6

**Components Analyzed:** Fz, N1, P1, P3b
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

### 2.1 Fz Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | 108.33 ms | 10.81 | 2.21 | [88.00, 116.00] |
| Landing on 2 | 24 | 106.67 ms | 9.03 | 1.84 | [88.00, 116.00] |
| Landing on 3 | 24 | 102.50 ms | 9.78 | 2.00 | [88.00, 116.00] |
| Landing on 4 | 24 | 102.83 ms | 10.45 | 2.13 | [88.00, 116.00] |
| Landing on 5 | 24 | 101.33 ms | 9.03 | 1.84 | [88.00, 116.00] |
| Landing on 6 | 24 | 101.50 ms | 10.67 | 2.18 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | -1.79 µV | 1.54 | 0.31 | [-6.25, 0.46] |
| Landing on 2 | 24 | -0.76 µV | 1.64 | 0.34 | [-3.80, 2.44] |
| Landing on 3 | 24 | -1.10 µV | 1.41 | 0.29 | [-4.27, 0.74] |
| Landing on 4 | 24 | -1.52 µV | 1.18 | 0.24 | [-4.68, -0.02] |
| Landing on 5 | 24 | -1.37 µV | 1.94 | 0.40 | [-8.37, 0.99] |
| Landing on 6 | 24 | -1.80 µV | 1.64 | 0.34 | [-4.55, 1.58] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | 182.33 ms | 13.55 | 2.77 | [156.00, 208.00] |
| Landing on 2 | 24 | 176.33 ms | 19.52 | 3.98 | [144.00, 208.00] |
| Landing on 3 | 24 | 171.50 ms | 16.36 | 3.34 | [144.00, 208.00] |
| Landing on 4 | 24 | 175.50 ms | 18.40 | 3.76 | [144.00, 208.00] |
| Landing on 5 | 24 | 170.50 ms | 21.06 | 4.30 | [144.00, 208.00] |
| Landing on 6 | 24 | 171.00 ms | 19.03 | 3.88 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | -3.53 µV | 2.44 | 0.50 | [-9.34, -0.77] |
| Landing on 2 | 24 | -5.59 µV | 2.35 | 0.48 | [-10.11, -1.67] |
| Landing on 3 | 24 | -5.49 µV | 1.79 | 0.37 | [-8.74, -1.75] |
| Landing on 4 | 24 | -5.51 µV | 2.36 | 0.48 | [-10.23, -0.85] |
| Landing on 5 | 24 | -5.84 µV | 2.30 | 0.47 | [-11.30, -1.56] |
| Landing on 6 | 24 | -6.15 µV | 2.94 | 0.60 | [-13.47, -1.82] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | 112.33 ms | 7.26 | 1.48 | [92.00, 116.00] |
| Landing on 2 | 24 | 107.50 ms | 9.01 | 1.84 | [92.00, 116.00] |
| Landing on 3 | 24 | 106.17 ms | 9.14 | 1.86 | [92.00, 116.00] |
| Landing on 4 | 24 | 103.83 ms | 9.97 | 2.04 | [92.00, 116.00] |
| Landing on 5 | 24 | 102.17 ms | 9.73 | 1.99 | [92.00, 116.00] |
| Landing on 6 | 24 | 102.33 ms | 10.00 | 2.04 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | 2.79 µV | 2.61 | 0.53 | [-1.37, 9.39] |
| Landing on 2 | 24 | 0.55 µV | 1.77 | 0.36 | [-2.91, 3.81] |
| Landing on 3 | 24 | 1.02 µV | 1.76 | 0.36 | [-2.58, 4.77] |
| Landing on 4 | 24 | 1.65 µV | 1.82 | 0.37 | [-0.65, 6.17] |
| Landing on 5 | 24 | 1.27 µV | 2.25 | 0.46 | [-2.42, 7.60] |
| Landing on 6 | 24 | 1.56 µV | 2.41 | 0.49 | [-2.29, 6.28] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | 481.00 ms | 31.79 | 6.49 | [424.00, 536.00] |
| Landing on 2 | 24 | 482.00 ms | 34.45 | 7.03 | [424.00, 536.00] |
| Landing on 3 | 24 | 475.50 ms | 30.20 | 6.16 | [436.00, 536.00] |
| Landing on 4 | 24 | 491.00 ms | 30.81 | 6.29 | [440.00, 536.00] |
| Landing on 5 | 24 | 496.83 ms | 38.76 | 7.91 | [424.00, 536.00] |
| Landing on 6 | 24 | 491.33 ms | 40.58 | 8.28 | [424.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Landing on 1 | 24 | 4.62 µV | 2.83 | 0.58 | [-0.40, 9.85] |
| Landing on 2 | 24 | 3.70 µV | 3.42 | 0.70 | [-1.79, 11.63] |
| Landing on 3 | 24 | 4.05 µV | 3.35 | 0.68 | [-2.36, 11.30] |
| Landing on 4 | 24 | 3.76 µV | 3.54 | 0.72 | [-2.79, 10.44] |
| Landing on 5 | 24 | 3.32 µV | 2.89 | 0.59 | [-2.80, 7.80] |
| Landing on 6 | 24 | 3.92 µV | 2.84 | 0.58 | [-1.82, 9.90] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.84, *p* = 0.019, η²_G = 0.069
- Greenhouse-Geisser corrected: *p* = 0.042 (ε = 0.628)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | 0.67 | 23 | = 0.683 | 0.17 [-0.29, 0.56] | negligible | n.s. |
| Landing on 1 vs Landing on 3 | 1.76 | 23 | = 0.180 | 0.57 [-0.08, 0.79] | medium | n.s. |
| Landing on 1 vs Landing on 4 | 2.21 | 23 | = 0.167 | 0.52 [0.01, 0.89] | medium | n.s. |
| Landing on 1 vs Landing on 5 | 2.25 | 23 | = 0.167 | 0.70 [0.02, 0.90] | medium | n.s. |
| Landing on 1 vs Landing on 6 | 2.18 | 23 | = 0.167 | 0.64 [0.00, 0.89] | medium | n.s. |
| Landing on 2 vs Landing on 3 | 1.74 | 23 | = 0.180 | 0.44 [-0.08, 0.79] | small | n.s. |
| Landing on 2 vs Landing on 4 | 1.92 | 23 | = 0.167 | 0.39 [-0.05, 0.83] | small | n.s. |
| Landing on 2 vs Landing on 5 | 2.09 | 23 | = 0.167 | 0.59 [-0.02, 0.87] | medium | n.s. |
| Landing on 2 vs Landing on 6 | 2.01 | 23 | = 0.167 | 0.52 [-0.03, 0.85] | medium | n.s. |
| Landing on 3 vs Landing on 4 | -0.16 | 23 | = 0.923 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| Landing on 3 vs Landing on 5 | 0.62 | 23 | = 0.683 | 0.12 [-0.30, 0.55] | negligible | n.s. |
| Landing on 3 vs Landing on 6 | 0.60 | 23 | = 0.683 | 0.10 [-0.30, 0.55] | negligible | n.s. |
| Landing on 4 vs Landing on 5 | 0.68 | 23 | = 0.683 | 0.15 [-0.29, 0.56] | negligible | n.s. |
| Landing on 4 vs Landing on 6 | 0.54 | 23 | = 0.683 | 0.13 [-0.31, 0.53] | negligible | n.s. |
| Landing on 5 vs Landing on 6 | -0.10 | 23 | = 0.923 | -0.02 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.44, *p* = 0.038, η²_G = 0.055
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | -2.93 | 23 | = 0.114 | -0.65 [-1.06, -0.14] | medium | n.s. |
| Landing on 1 vs Landing on 3 | -2.22 | 23 | = 0.138 | -0.47 [-0.90, -0.01] | small | n.s. |
| Landing on 1 vs Landing on 4 | -1.06 | 23 | = 0.457 | -0.20 [-0.64, 0.21] | small | n.s. |
| Landing on 1 vs Landing on 5 | -1.15 | 23 | = 0.457 | -0.24 [-0.66, 0.19] | small | n.s. |
| Landing on 1 vs Landing on 6 | 0.01 | 23 | = 0.989 | 0.00 [-0.42, 0.43] | negligible | n.s. |
| Landing on 2 vs Landing on 3 | 1.05 | 23 | = 0.457 | 0.23 [-0.21, 0.64] | small | n.s. |
| Landing on 2 vs Landing on 4 | 2.27 | 23 | = 0.138 | 0.53 [0.02, 0.91] | medium | n.s. |
| Landing on 2 vs Landing on 5 | 1.82 | 23 | = 0.242 | 0.34 [-0.07, 0.81] | small | n.s. |
| Landing on 2 vs Landing on 6 | 2.34 | 23 | = 0.138 | 0.63 [0.03, 0.92] | medium | n.s. |
| Landing on 3 vs Landing on 4 | 1.70 | 23 | = 0.242 | 0.32 [-0.09, 0.78] | small | n.s. |
| Landing on 3 vs Landing on 5 | 0.83 | 23 | = 0.520 | 0.16 [-0.26, 0.59] | negligible | n.s. |
| Landing on 3 vs Landing on 6 | 1.65 | 23 | = 0.242 | 0.46 [-0.10, 0.77] | small | n.s. |
| Landing on 4 vs Landing on 5 | -0.43 | 23 | = 0.719 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| Landing on 4 vs Landing on 6 | 0.69 | 23 | = 0.571 | 0.20 [-0.28, 0.57] | negligible | n.s. |
| Landing on 5 vs Landing on 6 | 0.91 | 23 | = 0.506 | 0.24 [-0.24, 0.61] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.71, *p* = 0.004, η²_G = 0.052
- Greenhouse-Geisser corrected: *p* = 0.011 (ε = 0.683)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | 1.71 | 23 | = 0.217 | 0.36 [-0.09, 0.78] | small | n.s. |
| Landing on 1 vs Landing on 3 | 3.95 | 23 | = 0.009 | 0.72 [0.32, 1.29] | medium | ** |
| Landing on 1 vs Landing on 4 | 2.48 | 23 | = 0.062 | 0.42 [0.06, 0.96] | small | n.s. |
| Landing on 1 vs Landing on 5 | 3.09 | 23 | = 0.026 | 0.67 [0.17, 1.09] | medium | * |
| Landing on 1 vs Landing on 6 | 3.20 | 23 | = 0.026 | 0.69 [0.19, 1.12] | medium | * |
| Landing on 2 vs Landing on 3 | 1.38 | 23 | = 0.293 | 0.27 [-0.15, 0.71] | small | n.s. |
| Landing on 2 vs Landing on 4 | 0.22 | 23 | = 0.881 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| Landing on 2 vs Landing on 5 | 1.55 | 23 | = 0.254 | 0.29 [-0.12, 0.75] | small | n.s. |
| Landing on 2 vs Landing on 6 | 1.89 | 23 | = 0.179 | 0.28 [-0.05, 0.82] | small | n.s. |
| Landing on 3 vs Landing on 4 | -2.89 | 23 | = 0.031 | -0.23 [-1.05, -0.13] | small | * |
| Landing on 3 vs Landing on 5 | 0.28 | 23 | = 0.881 | 0.05 [-0.36, 0.48] | negligible | n.s. |
| Landing on 3 vs Landing on 6 | 0.15 | 23 | = 0.881 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| Landing on 4 vs Landing on 5 | 1.23 | 23 | = 0.313 | 0.25 [-0.18, 0.68] | small | n.s. |
| Landing on 4 vs Landing on 6 | 1.33 | 23 | = 0.293 | 0.24 [-0.16, 0.70] | small | n.s. |
| Landing on 5 vs Landing on 6 | -0.16 | 23 | = 0.881 | -0.02 [-0.46, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.27, *p* < .001, η²_G = 0.116
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.577)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | 5.85 | 23 | < .001 | 0.86 [0.64, 1.75] | large | *** |
| Landing on 1 vs Landing on 3 | 4.51 | 23 | < .001 | 0.92 [0.42, 1.42] | large | *** |
| Landing on 1 vs Landing on 4 | 3.84 | 23 | = 0.003 | 0.82 [0.30, 1.27] | large | ** |
| Landing on 1 vs Landing on 5 | 4.41 | 23 | < .001 | 0.97 [0.40, 1.40] | large | *** |
| Landing on 1 vs Landing on 6 | 4.31 | 23 | < .001 | 0.97 [0.38, 1.38] | large | *** |
| Landing on 2 vs Landing on 3 | -0.34 | 23 | = 0.844 | -0.05 [-0.49, 0.35] | negligible | n.s. |
| Landing on 2 vs Landing on 4 | -0.27 | 23 | = 0.844 | -0.04 [-0.48, 0.37] | negligible | n.s. |
| Landing on 2 vs Landing on 5 | 0.61 | 23 | = 0.683 | 0.11 [-0.30, 0.55] | negligible | n.s. |
| Landing on 2 vs Landing on 6 | 1.22 | 23 | = 0.438 | 0.21 [-0.18, 0.68] | small | n.s. |
| Landing on 3 vs Landing on 4 | 0.07 | 23 | = 0.946 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| Landing on 3 vs Landing on 5 | 1.05 | 23 | = 0.464 | 0.17 [-0.21, 0.64] | negligible | n.s. |
| Landing on 3 vs Landing on 6 | 1.49 | 23 | = 0.321 | 0.27 [-0.13, 0.74] | small | n.s. |
| Landing on 4 vs Landing on 5 | 1.04 | 23 | = 0.464 | 0.14 [-0.21, 0.64] | negligible | n.s. |
| Landing on 4 vs Landing on 6 | 1.83 | 23 | = 0.201 | 0.24 [-0.06, 0.81] | small | n.s. |
| Landing on 5 vs Landing on 6 | 0.80 | 23 | = 0.585 | 0.12 [-0.26, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.65, *p* < .001, η²_G = 0.132
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | 2.61 | 23 | = 0.047 | 0.59 [0.08, 0.98] | medium | * |
| Landing on 1 vs Landing on 3 | 2.70 | 23 | = 0.047 | 0.75 [0.10, 1.00] | medium | * |
| Landing on 1 vs Landing on 4 | 4.02 | 23 | = 0.003 | 0.97 [0.33, 1.31] | large | ** |
| Landing on 1 vs Landing on 5 | 4.53 | 23 | = 0.002 | 1.18 [0.42, 1.43] | large | ** |
| Landing on 1 vs Landing on 6 | 4.40 | 23 | = 0.002 | 1.14 [0.40, 1.40] | large | ** |
| Landing on 2 vs Landing on 3 | 0.67 | 23 | = 0.544 | 0.15 [-0.29, 0.56] | negligible | n.s. |
| Landing on 2 vs Landing on 4 | 1.75 | 23 | = 0.141 | 0.39 [-0.08, 0.79] | small | n.s. |
| Landing on 2 vs Landing on 5 | 2.04 | 23 | = 0.099 | 0.57 [-0.02, 0.86] | medium | n.s. |
| Landing on 2 vs Landing on 6 | 2.04 | 23 | = 0.099 | 0.54 [-0.02, 0.86] | medium | n.s. |
| Landing on 3 vs Landing on 4 | 1.11 | 23 | = 0.378 | 0.24 [-0.20, 0.65] | small | n.s. |
| Landing on 3 vs Landing on 5 | 2.04 | 23 | = 0.099 | 0.42 [-0.02, 0.86] | small | n.s. |
| Landing on 3 vs Landing on 6 | 1.94 | 23 | = 0.108 | 0.40 [-0.04, 0.83] | small | n.s. |
| Landing on 4 vs Landing on 5 | 0.83 | 23 | = 0.516 | 0.17 [-0.26, 0.60] | negligible | n.s. |
| Landing on 4 vs Landing on 6 | 0.75 | 23 | = 0.535 | 0.15 [-0.27, 0.58] | negligible | n.s. |
| Landing on 5 vs Landing on 6 | -0.11 | 23 | = 0.915 | -0.02 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.50, *p* < .001, η²_G = 0.099
- Greenhouse-Geisser corrected: *p* = 0.002 (ε = 0.561)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | 5.00 | 23 | < .001 | 1.01 [0.50, 1.54] | large | *** |
| Landing on 1 vs Landing on 3 | 4.25 | 23 | = 0.002 | 0.79 [0.37, 1.36] | medium | ** |
| Landing on 1 vs Landing on 4 | 2.89 | 23 | = 0.030 | 0.51 [0.13, 1.05] | medium | * |
| Landing on 1 vs Landing on 5 | 2.80 | 23 | = 0.030 | 0.62 [0.12, 1.03] | medium | * |
| Landing on 1 vs Landing on 6 | 1.72 | 23 | = 0.166 | 0.49 [-0.08, 0.79] | small | n.s. |
| Landing on 2 vs Landing on 3 | -1.57 | 23 | = 0.196 | -0.27 [-0.75, 0.11] | small | n.s. |
| Landing on 2 vs Landing on 4 | -3.36 | 23 | = 0.013 | -0.61 [-1.16, -0.22] | medium | * |
| Landing on 2 vs Landing on 5 | -1.74 | 23 | = 0.166 | -0.36 [-0.79, 0.08] | small | n.s. |
| Landing on 2 vs Landing on 6 | -2.10 | 23 | = 0.100 | -0.48 [-0.87, 0.01] | small | n.s. |
| Landing on 3 vs Landing on 4 | -2.25 | 23 | = 0.085 | -0.35 [-0.90, -0.02] | small | n.s. |
| Landing on 3 vs Landing on 5 | -0.65 | 23 | = 0.563 | -0.12 [-0.56, 0.29] | negligible | n.s. |
| Landing on 3 vs Landing on 6 | -1.00 | 23 | = 0.445 | -0.25 [-0.63, 0.22] | small | n.s. |
| Landing on 4 vs Landing on 5 | 0.93 | 23 | = 0.455 | 0.18 [-0.24, 0.61] | negligible | n.s. |
| Landing on 4 vs Landing on 6 | 0.16 | 23 | = 0.873 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| Landing on 5 vs Landing on 6 | -0.65 | 23 | = 0.563 | -0.12 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.56, *p* = 0.031, η²_G = 0.044
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | -0.16 | 23 | = 0.939 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| Landing on 1 vs Landing on 3 | 0.98 | 23 | = 0.485 | 0.18 [-0.23, 0.63] | negligible | n.s. |
| Landing on 1 vs Landing on 4 | -1.54 | 23 | = 0.325 | -0.32 [-0.75, 0.12] | small | n.s. |
| Landing on 1 vs Landing on 5 | -2.37 | 23 | = 0.099 | -0.45 [-0.93, -0.04] | small | n.s. |
| Landing on 1 vs Landing on 6 | -1.48 | 23 | = 0.325 | -0.28 [-0.73, 0.13] | small | n.s. |
| Landing on 2 vs Landing on 3 | 0.89 | 23 | = 0.485 | 0.20 [-0.24, 0.61] | small | n.s. |
| Landing on 2 vs Landing on 4 | -1.06 | 23 | = 0.485 | -0.28 [-0.64, 0.21] | small | n.s. |
| Landing on 2 vs Landing on 5 | -1.73 | 23 | = 0.293 | -0.40 [-0.79, 0.08] | small | n.s. |
| Landing on 2 vs Landing on 6 | -1.21 | 23 | = 0.448 | -0.25 [-0.68, 0.18] | small | n.s. |
| Landing on 3 vs Landing on 4 | -3.24 | 23 | = 0.054 | -0.51 [-1.13, -0.20] | medium | n.s. |
| Landing on 3 vs Landing on 5 | -2.85 | 23 | = 0.068 | -0.61 [-1.04, -0.13] | medium | n.s. |
| Landing on 3 vs Landing on 6 | -2.55 | 23 | = 0.090 | -0.44 [-0.97, -0.07] | small | n.s. |
| Landing on 4 vs Landing on 5 | -0.74 | 23 | = 0.536 | -0.17 [-0.58, 0.27] | negligible | n.s. |
| Landing on 4 vs Landing on 6 | -0.04 | 23 | = 0.968 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Landing on 5 vs Landing on 6 | 0.88 | 23 | = 0.485 | 0.14 [-0.25, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

_LMM results not available._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.37, *p* = 0.043, η²_G = 0.016
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Landing on 1 vs Landing on 2 | 2.35 | 23 | = 0.198 | 0.29 [0.03, 0.93] | small | n.s. |
| Landing on 1 vs Landing on 3 | 1.40 | 23 | = 0.373 | 0.18 [-0.14, 0.72] | negligible | n.s. |
| Landing on 1 vs Landing on 4 | 1.79 | 23 | = 0.326 | 0.27 [-0.07, 0.80] | small | n.s. |
| Landing on 1 vs Landing on 5 | 2.74 | 23 | = 0.174 | 0.45 [0.11, 1.01] | small | n.s. |
| Landing on 1 vs Landing on 6 | 2.18 | 23 | = 0.198 | 0.25 [0.00, 0.89] | small | n.s. |
| Landing on 2 vs Landing on 3 | -1.15 | 23 | = 0.449 | -0.10 [-0.66, 0.19] | negligible | n.s. |
| Landing on 2 vs Landing on 4 | -0.13 | 23 | = 0.898 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| Landing on 2 vs Landing on 5 | 0.80 | 23 | = 0.590 | 0.12 [-0.26, 0.59] | negligible | n.s. |
| Landing on 2 vs Landing on 6 | -0.70 | 23 | = 0.615 | -0.07 [-0.57, 0.28] | negligible | n.s. |
| Landing on 3 vs Landing on 4 | 0.81 | 23 | = 0.590 | 0.08 [-0.26, 0.59] | negligible | n.s. |
| Landing on 3 vs Landing on 5 | 1.67 | 23 | = 0.326 | 0.23 [-0.09, 0.78] | small | n.s. |
| Landing on 3 vs Landing on 6 | 0.46 | 23 | = 0.751 | 0.04 [-0.33, 0.52] | negligible | n.s. |
| Landing on 4 vs Landing on 5 | 1.13 | 23 | = 0.449 | 0.13 [-0.20, 0.66] | negligible | n.s. |
| Landing on 4 vs Landing on 6 | -0.39 | 23 | = 0.753 | -0.05 [-0.50, 0.34] | negligible | n.s. |
| Landing on 5 vs Landing on 6 | -1.54 | 23 | = 0.344 | -0.21 [-0.75, 0.12] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.019) (no significant pairwise comparisons)
**Fz amplitude:** Significant main effect of condition (*p* = 0.038) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Landing on 1 showed greater latency than Landing on 3 (*d* = 0.72)
  - Landing on 1 showed greater latency than Landing on 5 (*d* = 0.67)
  - Landing on 1 showed greater latency than Landing on 6 (*d* = 0.69)
  - Landing on 3 showed smaller latency than Landing on 4 (*d* = -0.23)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Landing on 1 showed greater amplitude than Landing on 2 (*d* = 0.86)
  - Landing on 1 showed greater amplitude than Landing on 3 (*d* = 0.92)
  - Landing on 1 showed greater amplitude than Landing on 4 (*d* = 0.82)
  - Landing on 1 showed greater amplitude than Landing on 5 (*d* = 0.97)
  - Landing on 1 showed greater amplitude than Landing on 6 (*d* = 0.97)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Landing on 1 showed greater latency than Landing on 2 (*d* = 0.59)
  - Landing on 1 showed greater latency than Landing on 3 (*d* = 0.75)
  - Landing on 1 showed greater latency than Landing on 4 (*d* = 0.97)
  - Landing on 1 showed greater latency than Landing on 5 (*d* = 1.18)
  - Landing on 1 showed greater latency than Landing on 6 (*d* = 1.14)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Landing on 1 showed greater amplitude than Landing on 2 (*d* = 1.01)
  - Landing on 1 showed greater amplitude than Landing on 3 (*d* = 0.79)
  - Landing on 1 showed greater amplitude than Landing on 4 (*d* = 0.51)
  - Landing on 1 showed greater amplitude than Landing on 5 (*d* = 0.62)
  - Landing on 2 showed smaller amplitude than Landing on 4 (*d* = -0.61)
**P3b latency:** Significant main effect of condition (*p* = 0.031) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.043) (no significant pairwise comparisons)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

_No visualization plots found._

---

## 6. Methods Summary (for Publication)

### ERP Measurement

ERP components were measured using a collapsed localizer approach, where component peaks were identified from the grand average of all conditions combined to avoid circular analysis (Luck & Gaspelin, 2017). Measurement windows were defined as the full-width at half-maximum (FWHM) around each peak. Component latency was quantified using the 50% fractional area latency (FAL), which represents the time point at which the cumulative area under the curve reaches 50% of its total value within the measurement window. This metric provides a robust estimate of component timing with lower measurement error than peak latency (Kiesel et al., 2008). Mean amplitude was computed as the average voltage within the FWHM window across predefined regions of interest (ROI).

### Statistical Analysis

For comparison with traditional approaches, repeated-measures ANOVA and pairwise t-tests were also performed on complete cases; however, power was substantially reduced by listwise deletion. Therefore, LMM results are emphasized in interpretation.

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.4
- MNE-Python 1.9.0
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
