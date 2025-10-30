# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:50:26

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
| 2 to 1 | 16 | -2.63 µV | 2.26 | 0.56 | [-8.75, -0.13] |
| 3 to 2 | 24 | -3.83 µV | 2.22 | 0.45 | [-8.28, -0.34] |
| 4 to 3 | 23 | -4.26 µV | 2.02 | 0.42 | [-8.84, -0.53] |
| 5 to 4 | 23 | -4.11 µV | 2.26 | 0.47 | [-8.23, -0.10] |
| 6 to 5 | 24 | -3.88 µV | 1.87 | 0.38 | [-8.82, -0.57] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 180.41 ms | 9.80 | 2.45 | [162.74, 202.98] |
| 3 to 2 | 24 | 175.23 ms | 9.20 | 1.88 | [161.61, 201.28] |
| 4 to 3 | 23 | 175.61 ms | 8.74 | 1.82 | [160.00, 201.39] |
| 5 to 4 | 23 | 176.25 ms | 9.09 | 1.89 | [148.72, 196.50] |
| 6 to 5 | 24 | 175.21 ms | 8.94 | 1.82 | [163.45, 193.99] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 3.17 µV | 2.28 | 0.54 | [1.13, 8.73] |
| 3 to 2 | 12 | 1.61 µV | 1.43 | 0.41 | [-0.06, 4.03] |
| 4 to 3 | 11 | 1.78 µV | 1.34 | 0.40 | [0.16, 4.63] |
| 5 to 4 | 15 | 1.89 µV | 1.63 | 0.42 | [0.24, 5.45] |
| 6 to 5 | 12 | 2.19 µV | 2.19 | 0.63 | [0.10, 7.74] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 109.81 ms | 2.80 | 0.66 | [104.85, 114.00] |
| 3 to 2 | 12 | 106.53 ms | 4.29 | 1.24 | [97.59, 112.58] |
| 4 to 3 | 11 | 106.32 ms | 4.45 | 1.34 | [97.03, 112.76] |
| 5 to 4 | 15 | 109.19 ms | 5.19 | 1.34 | [98.09, 116.75] |
| 6 to 5 | 12 | 106.79 ms | 4.30 | 1.24 | [97.20, 114.95] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 4.04 µV | 2.59 | 0.59 | [0.38, 9.87] |
| 3 to 2 | 18 | 4.23 µV | 3.25 | 0.77 | [0.09, 12.56] |
| 4 to 3 | 21 | 3.54 µV | 2.80 | 0.61 | [0.07, 9.36] |
| 5 to 4 | 18 | 3.84 µV | 2.78 | 0.66 | [0.03, 8.79] |
| 6 to 5 | 13 | 2.47 µV | 1.89 | 0.52 | [0.46, 6.12] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 495.48 ms | 14.96 | 3.43 | [460.38, 529.17] |
| 3 to 2 | 18 | 492.68 ms | 19.69 | 4.64 | [439.22, 533.11] |
| 4 to 3 | 21 | 485.92 ms | 18.67 | 4.07 | [436.49, 524.82] |
| 5 to 4 | 18 | 493.70 ms | 16.44 | 3.88 | [457.51, 516.39] |
| 6 to 5 | 13 | 506.63 ms | 22.83 | 6.33 | [476.62, 540.12] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 393.69, BIC = 415.29
- **3 to 2 vs 2 to 1**: *β* = -0.83, *SE* = 0.383, *z* = -2.181, *p* = 0.029
- **4 to 3 vs 2 to 1**: *β* = -1.18, *SE* = 0.392, *z* = -2.999, *p* = 0.003
- **5 to 4 vs 2 to 1**: *β* = -0.89, *SE* = 0.391, *z* = -2.286, *p* = 0.022
- **6 to 5 vs 2 to 1**: *β* = -1.16, *SE* = 0.377, *z* = -3.062, *p* = 0.002
- **SNR**: *β* = -0.38, *SE* = 0.042, *z* = -9.089, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.84 | 0.38 | 2.18 | 0.029 | 0.187 | n.s. |
| 2 to 1 - 4 to 3 | 1.17 | 0.39 | 3.00 | 0.003 | 0.024 | * |
| 2 to 1 - 5 to 4 | 0.89 | 0.39 | 2.29 | 0.022 | 0.165 | n.s. |
| 2 to 1 - 6 to 5 | 1.16 | 0.38 | 3.06 | 0.002 | 0.022 | * |
| 3 to 2 - 4 to 3 | 0.34 | 0.33 | 1.03 | 0.305 | 0.887 | n.s. |
| 3 to 2 - 5 to 4 | 0.06 | 0.33 | 0.18 | 0.860 | 0.980 | n.s. |
| 3 to 2 - 6 to 5 | 0.32 | 0.33 | 0.98 | 0.328 | 0.887 | n.s. |
| 4 to 3 - 5 to 4 | -0.28 | 0.33 | -0.84 | 0.401 | 0.887 | n.s. |
| 4 to 3 - 6 to 5 | -0.02 | 0.33 | -0.06 | 0.953 | 0.980 | n.s. |
| 5 to 4 - 6 to 5 | 0.26 | 0.33 | 0.79 | 0.432 | 0.887 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.92, *p* = 0.002, η²_G = 0.157
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 4.14 | 13 | = 0.012 | 1.01 [0.35, 1.65] | large | * |
| 2 to 1 vs 4 to 3 | 3.43 | 13 | = 0.022 | 1.03 [0.23, 1.54] | large | * |
| 2 to 1 vs 5 to 4 | 3.10 | 13 | = 0.028 | 1.09 [0.11, 1.36] | large | * |
| 2 to 1 vs 6 to 5 | 2.17 | 13 | = 0.122 | 0.74 [0.05, 1.22] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.14 | 13 | = 0.894 | 0.03 [-0.15, 0.73] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.26 | 13 | = 0.894 | 0.09 [-0.38, 0.49] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -0.98 | 13 | = 0.493 | -0.28 [-0.40, 0.45] | small | n.s. |
| 4 to 3 vs 5 to 4 | 0.18 | 13 | = 0.894 | 0.05 [-0.58, 0.31] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | -1.17 | 13 | = 0.438 | -0.31 [-0.66, 0.21] | small | n.s. |
| 5 to 4 vs 6 to 5 | -1.42 | 13 | = 0.361 | -0.37 [-0.54, 0.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 779.62, BIC = 801.22
- **3 to 2 vs 2 to 1**: *β* = -3.48, *SE* = 2.231, *z* = -1.562, *p* = 0.118
- **4 to 3 vs 2 to 1**: *β* = -3.09, *SE* = 2.276, *z* = -1.356, *p* = 0.175
- **5 to 4 vs 2 to 1**: *β* = -1.60, *SE* = 2.280, *z* = -0.702, *p* = 0.483
- **6 to 5 vs 2 to 1**: *β* = -3.82, *SE* = 2.201, *z* = -1.735, *p* = 0.083
- **SNR**: *β* = -0.46, *SE* = 0.243, *z* = -1.895, *p* = 0.058

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.49 | 2.23 | 1.56 | 0.118 | 0.678 | n.s. |
| 2 to 1 - 4 to 3 | 3.09 | 2.28 | 1.36 | 0.175 | 0.785 | n.s. |
| 2 to 1 - 5 to 4 | 1.60 | 2.28 | 0.70 | 0.483 | 0.949 | n.s. |
| 2 to 1 - 6 to 5 | 3.82 | 2.20 | 1.73 | 0.083 | 0.579 | n.s. |
| 3 to 2 - 4 to 3 | -0.40 | 1.94 | -0.21 | 0.837 | 0.975 | n.s. |
| 3 to 2 - 5 to 4 | -1.89 | 1.94 | -0.97 | 0.331 | 0.910 | n.s. |
| 3 to 2 - 6 to 5 | 0.33 | 1.92 | 0.17 | 0.862 | 0.975 | n.s. |
| 4 to 3 - 5 to 4 | -1.49 | 1.96 | -0.76 | 0.448 | 0.949 | n.s. |
| 4 to 3 - 6 to 5 | 0.73 | 1.95 | 0.37 | 0.708 | 0.975 | n.s. |
| 5 to 4 - 6 to 5 | 2.22 | 1.95 | 1.14 | 0.256 | 0.874 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.213, η²_G = 0.053
- Greenhouse-Geisser corrected: *p* = 0.237 (ε = 0.562)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.87 | 13 | = 0.294 | 0.66 [-0.08, 1.05] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 1.84 | 13 | = 0.294 | 0.58 [-0.10, 1.07] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 1.40 | 13 | = 0.459 | 0.39 [-0.28, 0.85] | small | n.s. |
| 2 to 1 vs 6 to 5 | 2.08 | 13 | = 0.294 | 0.47 [-0.08, 1.05] | small | n.s. |
| 3 to 2 vs 4 to 3 | -0.42 | 13 | = 0.845 | -0.06 [-0.44, 0.43] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -1.08 | 13 | = 0.602 | -0.30 [-0.70, 0.18] | small | n.s. |
| 3 to 2 vs 6 to 5 | -0.31 | 13 | = 0.845 | -0.12 [-0.42, 0.42] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -0.87 | 13 | = 0.666 | -0.22 [-0.64, 0.26] | small | n.s. |
| 4 to 3 vs 6 to 5 | -0.17 | 13 | = 0.866 | -0.06 [-0.38, 0.49] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 0.48 | 13 | = 0.845 | 0.14 [-0.31, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 207.55, BIC = 225.30
- **3 to 2 vs 2 to 1**: *β* = -0.20, *SE* = 0.358, *z* = -0.562, *p* = 0.574
- **4 to 3 vs 2 to 1**: *β* = -0.56, *SE* = 0.354, *z* = -1.567, *p* = 0.117
- **5 to 4 vs 2 to 1**: *β* = -0.17, *SE* = 0.329, *z* = -0.514, *p* = 0.607
- **6 to 5 vs 2 to 1**: *β* = -0.07, *SE* = 0.347, *z* = -0.199, *p* = 0.842
- **SNR**: *β* = 0.74, *SE* = 0.068, *z* = 10.815, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.20 | 0.36 | 0.56 | 0.574 | 0.994 | n.s. |
| 2 to 1 - 4 to 3 | 0.55 | 0.35 | 1.57 | 0.117 | 0.712 | n.s. |
| 2 to 1 - 5 to 4 | 0.17 | 0.33 | 0.51 | 0.607 | 0.994 | n.s. |
| 2 to 1 - 6 to 5 | 0.07 | 0.35 | 0.20 | 0.842 | 0.994 | n.s. |
| 3 to 2 - 4 to 3 | 0.35 | 0.37 | 0.96 | 0.339 | 0.945 | n.s. |
| 3 to 2 - 5 to 4 | -0.03 | 0.34 | -0.09 | 0.926 | 0.994 | n.s. |
| 3 to 2 - 6 to 5 | -0.13 | 0.37 | -0.36 | 0.719 | 0.994 | n.s. |
| 4 to 3 - 5 to 4 | -0.39 | 0.35 | -1.10 | 0.273 | 0.922 | n.s. |
| 4 to 3 - 6 to 5 | -0.49 | 0.37 | -1.30 | 0.192 | 0.854 | n.s. |
| 5 to 4 - 6 to 5 | -0.10 | 0.34 | -0.29 | 0.769 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.298, η²_G = 0.190
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.83 | 4 | = 0.472 | 1.10 [0.01, 1.67] | large | n.s. |
| 2 to 1 vs 4 to 3 | 2.10 | 4 | = 0.472 | 1.04 [0.01, 1.85] | large | n.s. |
| 2 to 1 vs 5 to 4 | 0.87 | 4 | = 0.790 | 0.66 [-0.26, 1.06] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 2.23 | 4 | = 0.472 | 0.68 [0.09, 1.81] | medium | n.s. |
| 3 to 2 vs 4 to 3 | -0.21 | 4 | = 0.848 | -0.14 [-0.86, 0.82] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.79 | 4 | = 0.790 | -0.62 [-0.97, 0.58] | medium | n.s. |
| 3 to 2 vs 6 to 5 | -0.48 | 4 | = 0.848 | -0.27 [-1.17, 0.70] | small | n.s. |
| 4 to 3 vs 5 to 4 | -0.83 | 4 | = 0.790 | -0.52 [-0.85, 0.69] | medium | n.s. |
| 4 to 3 vs 6 to 5 | -0.36 | 4 | = 0.848 | -0.20 [-1.02, 0.83] | small | n.s. |
| 5 to 4 vs 6 to 5 | 0.20 | 4 | = 0.848 | 0.14 [-0.78, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 396.98, BIC = 414.73
- **3 to 2 vs 2 to 1**: *β* = -3.08, *SE* = 1.503, *z* = -2.047, *p* = 0.041
- **4 to 3 vs 2 to 1**: *β* = -3.31, *SE* = 1.494, *z* = -2.218, *p* = 0.027
- **5 to 4 vs 2 to 1**: *β* = -0.47, *SE* = 1.388, *z* = -0.339, *p* = 0.735
- **6 to 5 vs 2 to 1**: *β* = -2.97, *SE* = 1.464, *z* = -2.031, *p* = 0.042
- **SNR**: *β* = 0.18, *SE* = 0.270, *z* = 0.680, *p* = 0.496

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.08 | 1.50 | 2.05 | 0.041 | 0.312 | n.s. |
| 2 to 1 - 4 to 3 | 3.31 | 1.49 | 2.22 | 0.027 | 0.236 | n.s. |
| 2 to 1 - 5 to 4 | 0.47 | 1.39 | 0.34 | 0.735 | 0.995 | n.s. |
| 2 to 1 - 6 to 5 | 2.97 | 1.46 | 2.03 | 0.042 | 0.312 | n.s. |
| 3 to 2 - 4 to 3 | 0.24 | 1.59 | 0.15 | 0.880 | 0.995 | n.s. |
| 3 to 2 - 5 to 4 | -2.61 | 1.47 | -1.77 | 0.076 | 0.379 | n.s. |
| 3 to 2 - 6 to 5 | -0.10 | 1.56 | -0.07 | 0.948 | 0.995 | n.s. |
| 4 to 3 - 5 to 4 | -2.84 | 1.51 | -1.89 | 0.059 | 0.346 | n.s. |
| 4 to 3 - 6 to 5 | -0.34 | 1.59 | -0.21 | 0.830 | 0.995 | n.s. |
| 5 to 4 - 6 to 5 | 2.50 | 1.46 | 1.71 | 0.087 | 0.379 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.03, *p* = 0.424, η²_G = 0.085
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.22 | 4 | = 0.581 | 0.31 [-0.26, 1.25] | small | n.s. |
| 2 to 1 vs 4 to 3 | 2.59 | 4 | = 0.568 | 0.87 [-0.05, 1.75] | large | n.s. |
| 2 to 1 vs 5 to 4 | 1.88 | 4 | = 0.568 | 0.77 [-0.46, 0.82] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 1.22 | 4 | = 0.581 | 0.53 [-0.20, 1.35] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 1.67 | 4 | = 0.568 | 0.54 [-1.08, 0.62] | medium | n.s. |
| 3 to 2 vs 5 to 4 | 0.97 | 4 | = 0.646 | 0.39 [-1.00, 0.56] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.56 | 4 | = 0.829 | 0.30 [-0.77, 1.09] | small | n.s. |
| 4 to 3 vs 5 to 4 | -0.47 | 4 | = 0.829 | -0.21 [-1.35, 0.29] | small | n.s. |
| 4 to 3 vs 6 to 5 | -0.33 | 4 | = 0.844 | -0.13 [-0.80, 1.05] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 0.05 | 4 | = 0.959 | 0.03 [-0.34, 1.15] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 356.19, BIC = 376.10
- **3 to 2 vs 2 to 1**: *β* = 0.50, *SE* = 0.457, *z* = 1.099, *p* = 0.272
- **4 to 3 vs 2 to 1**: *β* = -0.48, *SE* = 0.442, *z* = -1.086, *p* = 0.277
- **5 to 4 vs 2 to 1**: *β* = -0.30, *SE* = 0.452, *z* = -0.661, *p* = 0.508
- **6 to 5 vs 2 to 1**: *β* = -1.25, *SE* = 0.516, *z* = -2.423, *p* = 0.015
- **SNR**: *β* = 0.55, *SE* = 0.053, *z* = 10.478, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.50 | 0.46 | -1.10 | 0.272 | 0.719 | n.s. |
| 2 to 1 - 4 to 3 | 0.48 | 0.44 | 1.09 | 0.277 | 0.719 | n.s. |
| 2 to 1 - 5 to 4 | 0.30 | 0.45 | 0.66 | 0.508 | 0.758 | n.s. |
| 2 to 1 - 6 to 5 | 1.25 | 0.52 | 2.42 | 0.015 | 0.130 | n.s. |
| 3 to 2 - 4 to 3 | 0.98 | 0.44 | 2.21 | 0.027 | 0.195 | n.s. |
| 3 to 2 - 5 to 4 | 0.80 | 0.46 | 1.74 | 0.082 | 0.402 | n.s. |
| 3 to 2 - 6 to 5 | 1.75 | 0.52 | 3.39 | < .001 | 0.007 | ** |
| 4 to 3 - 5 to 4 | -0.18 | 0.45 | -0.41 | 0.684 | 0.758 | n.s. |
| 4 to 3 - 6 to 5 | 0.77 | 0.51 | 1.52 | 0.130 | 0.501 | n.s. |
| 5 to 4 - 6 to 5 | 0.95 | 0.52 | 1.83 | 0.067 | 0.387 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.15, *p* = 0.024, η²_G = 0.170
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.33 | 10 | = 0.749 | -0.12 [-0.61, 0.45] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 0.64 | 10 | = 0.749 | 0.25 [-0.46, 0.57] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.35 | 10 | = 0.749 | 0.15 [-0.40, 0.63] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 2.72 | 10 | = 0.079 | 1.31 [0.04, 1.48] | large | n.s. |
| 3 to 2 vs 4 to 3 | 1.32 | 10 | = 0.433 | 0.33 [-0.42, 0.58] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.71 | 10 | = 0.749 | 0.25 [-0.36, 0.71] | small | n.s. |
| 3 to 2 vs 6 to 5 | 2.67 | 10 | = 0.079 | 1.25 [0.03, 1.58] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.34 | 10 | = 0.749 | -0.10 [-0.51, 0.52] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.82 | 10 | = 0.246 | 0.89 [-0.21, 1.06] | large | n.s. |
| 5 to 4 vs 6 to 5 | 3.23 | 10 | = 0.079 | 1.06 [0.16, 1.67] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 760.92, BIC = 780.83
- **3 to 2 vs 2 to 1**: *β* = -3.67, *SE* = 4.419, *z* = -0.832, *p* = 0.406
- **4 to 3 vs 2 to 1**: *β* = -8.04, *SE* = 4.284, *z* = -1.877, *p* = 0.061
- **5 to 4 vs 2 to 1**: *β* = -1.15, *SE* = 4.371, *z* = -0.264, *p* = 0.792
- **6 to 5 vs 2 to 1**: *β* = 15.10, *SE* = 5.003, *z* = 3.019, *p* = 0.003
- **SNR**: *β* = -0.15, *SE* = 0.507, *z* = -0.293, *p* = 0.770

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.67 | 4.42 | 0.83 | 0.406 | 0.790 | n.s. |
| 2 to 1 - 4 to 3 | 8.04 | 4.28 | 1.88 | 0.061 | 0.312 | n.s. |
| 2 to 1 - 5 to 4 | 1.15 | 4.37 | 0.26 | 0.792 | 0.816 | n.s. |
| 2 to 1 - 6 to 5 | -15.10 | 5.00 | -3.02 | 0.003 | 0.018 | * |
| 3 to 2 - 4 to 3 | 4.37 | 4.30 | 1.02 | 0.310 | 0.773 | n.s. |
| 3 to 2 - 5 to 4 | -2.52 | 4.46 | -0.57 | 0.571 | 0.816 | n.s. |
| 3 to 2 - 6 to 5 | -18.78 | 5.01 | -3.75 | < .001 | 0.002 | ** |
| 4 to 3 - 5 to 4 | -6.89 | 4.31 | -1.60 | 0.110 | 0.441 | n.s. |
| 4 to 3 - 6 to 5 | -23.15 | 4.88 | -4.75 | < .001 | < .001 | *** |
| 5 to 4 - 6 to 5 | -16.26 | 5.03 | -3.23 | 0.001 | 0.010 | ** |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.40, *p* = 0.001, η²_G = 0.212
- Greenhouse-Geisser corrected: *p* = 0.012 (ε = 0.532)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.98 | 10 | = 0.499 | 0.17 [-0.53, 0.54] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 0.74 | 10 | = 0.547 | 0.24 [-0.04, 1.06] | small | n.s. |
| 2 to 1 vs 5 to 4 | -0.71 | 10 | = 0.547 | -0.24 [-0.49, 0.54] | small | n.s. |
| 2 to 1 vs 6 to 5 | -2.98 | 10 | = 0.066 | -1.00 [-1.58, -0.10] | large | n.s. |
| 3 to 2 vs 4 to 3 | 0.02 | 10 | = 0.984 | 0.01 [-0.40, 0.59] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.99 | 10 | = 0.499 | -0.36 [-0.67, 0.40] | small | n.s. |
| 3 to 2 vs 6 to 5 | -2.77 | 10 | = 0.066 | -1.00 [-1.62, -0.05] | large | n.s. |
| 4 to 3 vs 5 to 4 | -1.51 | 10 | = 0.324 | -0.49 [-0.92, 0.15] | small | n.s. |
| 4 to 3 vs 6 to 5 | -3.90 | 10 | = 0.030 | -1.14 [-2.16, -0.50] | large | * |
| 5 to 4 vs 6 to 5 | -2.03 | 10 | = 0.173 | -0.87 [-1.36, 0.05] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 1.01)
  - 2 to 1 showed greater amplitude than 4 to 3 (*d* = 1.03)
  - 2 to 1 showed greater amplitude than 5 to 4 (*d* = 1.09)
**P3b amplitude:** Significant main effect of condition (*p* = 0.024) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - 4 to 3 showed smaller latency than 6 to 5 (*d* = -1.14)

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
