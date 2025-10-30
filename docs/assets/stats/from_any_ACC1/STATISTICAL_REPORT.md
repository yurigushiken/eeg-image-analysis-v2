# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:53:57

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
| from 1 | 24 | -3.82 µV | 1.98 | 0.40 | [-9.07, -0.53] |
| from 2 | 22 | -3.26 µV | 1.32 | 0.28 | [-6.61, -0.70] |
| from 3 | 22 | -3.53 µV | 1.57 | 0.34 | [-7.34, -1.56] |
| from 4 | 24 | -3.37 µV | 1.74 | 0.35 | [-7.82, -0.78] |
| from 5 | 23 | -4.14 µV | 1.83 | 0.38 | [-7.67, -0.88] |
| from 6 | 24 | -3.92 µV | 1.82 | 0.37 | [-7.77, -0.92] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 175.64 ms | 10.60 | 2.16 | [156.63, 204.20] |
| from 2 | 22 | 174.62 ms | 8.52 | 1.82 | [157.36, 196.98] |
| from 3 | 22 | 173.51 ms | 7.36 | 1.57 | [158.16, 188.38] |
| from 4 | 24 | 176.11 ms | 8.83 | 1.80 | [160.18, 201.69] |
| from 5 | 23 | 174.62 ms | 6.67 | 1.39 | [161.33, 191.02] |
| from 6 | 24 | 175.31 ms | 9.88 | 2.02 | [159.91, 201.34] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 13 | 1.39 µV | 1.03 | 0.29 | [-0.08, 3.74] |
| from 2 | 16 | 1.68 µV | 1.51 | 0.38 | [-0.03, 4.64] |
| from 3 | 14 | 1.36 µV | 1.31 | 0.35 | [0.04, 4.23] |
| from 4 | 12 | 2.02 µV | 1.30 | 0.38 | [0.58, 4.68] |
| from 5 | 15 | 1.79 µV | 1.00 | 0.26 | [0.10, 3.59] |
| from 6 | 15 | 1.74 µV | 1.46 | 0.38 | [0.34, 6.09] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 13 | 107.04 ms | 4.84 | 1.34 | [97.37, 115.73] |
| from 2 | 16 | 109.06 ms | 4.68 | 1.17 | [100.75, 119.94] |
| from 3 | 14 | 107.72 ms | 5.15 | 1.38 | [97.60, 115.37] |
| from 4 | 12 | 109.63 ms | 1.97 | 0.57 | [107.29, 114.37] |
| from 5 | 15 | 108.43 ms | 4.53 | 1.17 | [96.93, 115.75] |
| from 6 | 15 | 109.48 ms | 4.83 | 1.25 | [98.08, 116.65] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 19 | 3.74 µV | 2.92 | 0.67 | [0.30, 11.17] |
| from 2 | 19 | 3.76 µV | 2.29 | 0.52 | [0.23, 7.11] |
| from 3 | 19 | 3.45 µV | 2.24 | 0.51 | [0.54, 7.57] |
| from 4 | 20 | 3.51 µV | 2.45 | 0.55 | [0.19, 7.22] |
| from 5 | 18 | 3.56 µV | 2.07 | 0.49 | [0.44, 8.81] |
| from 6 | 19 | 3.28 µV | 2.14 | 0.49 | [0.11, 7.36] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 19 | 480.65 ms | 15.46 | 3.55 | [442.13, 511.08] |
| from 2 | 19 | 478.93 ms | 16.45 | 3.77 | [440.73, 521.67] |
| from 3 | 19 | 480.41 ms | 11.51 | 2.64 | [462.43, 509.72] |
| from 4 | 20 | 486.92 ms | 13.91 | 3.11 | [464.84, 513.92] |
| from 5 | 18 | 479.56 ms | 12.10 | 2.85 | [450.17, 510.14] |
| from 6 | 19 | 481.88 ms | 17.75 | 4.07 | [449.65, 520.85] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 401.00, BIC = 427.41
- **from 2 vs from 1**: *β* = 0.63, *SE* = 0.226, *z* = 2.795, *p* = 0.005
- **from 3 vs from 1**: *β* = 0.71, *SE* = 0.228, *z* = 3.126, *p* = 0.002
- **from 4 vs from 1**: *β* = 0.49, *SE* = 0.220, *z* = 2.210, *p* = 0.027
- **from 5 vs from 1**: *β* = -0.16, *SE* = 0.223, *z* = -0.736, *p* = 0.462
- **from 6 vs from 1**: *β* = -0.16, *SE* = 0.220, *z* = -0.738, *p* = 0.461
- **SNR**: *β* = -0.12, *SE* = 0.018, *z* = -7.014, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.63 | 0.23 | -2.79 | 0.005 | 0.041 | * |
| from 1 - from 3 | -0.71 | 0.23 | -3.13 | 0.002 | 0.019 | * |
| from 1 - from 4 | -0.49 | 0.22 | -2.21 | 0.027 | 0.175 | n.s. |
| from 1 - from 5 | 0.16 | 0.22 | 0.74 | 0.462 | 0.954 | n.s. |
| from 1 - from 6 | 0.16 | 0.22 | 0.74 | 0.461 | 0.954 | n.s. |
| from 2 - from 3 | -0.08 | 0.23 | -0.34 | 0.731 | 0.954 | n.s. |
| from 2 - from 4 | 0.15 | 0.23 | 0.64 | 0.519 | 0.954 | n.s. |
| from 2 - from 5 | 0.80 | 0.23 | 3.47 | < .001 | 0.006 | ** |
| from 2 - from 6 | 0.79 | 0.23 | 3.52 | < .001 | 0.006 | ** |
| from 3 - from 4 | 0.23 | 0.23 | 1.00 | 0.319 | 0.900 | n.s. |
| from 3 - from 5 | 0.88 | 0.23 | 3.83 | < .001 | 0.002 | ** |
| from 3 - from 6 | 0.87 | 0.23 | 3.82 | < .001 | 0.002 | ** |
| from 4 - from 5 | 0.65 | 0.22 | 2.92 | 0.004 | 0.032 | * |
| from 4 - from 6 | 0.65 | 0.22 | 2.94 | 0.003 | 0.032 | * |
| from 5 - from 6 | -0.00 | 0.22 | -0.01 | 0.994 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.00, *p* < .001, η²_G = 0.057
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -4.07 | 20 | = 0.005 | -0.61 [-1.26, -0.25] | medium | ** |
| from 1 vs from 3 | -2.71 | 20 | = 0.040 | -0.39 [-0.97, -0.03] | small | * |
| from 1 vs from 4 | -3.21 | 20 | = 0.022 | -0.40 [-0.81, 0.07] | small | * |
| from 1 vs from 5 | 0.41 | 20 | = 0.793 | 0.06 [-0.29, 0.58] | negligible | n.s. |
| from 1 vs from 6 | -0.19 | 20 | = 0.848 | -0.04 [-0.35, 0.50] | negligible | n.s. |
| from 2 vs from 3 | 1.23 | 20 | = 0.349 | 0.19 [-0.19, 0.73] | negligible | n.s. |
| from 2 vs from 4 | 1.02 | 20 | = 0.439 | 0.15 [-0.27, 0.62] | negligible | n.s. |
| from 2 vs from 5 | 4.42 | 20 | = 0.004 | 0.67 [0.41, 1.51] | medium | ** |
| from 2 vs from 6 | 2.94 | 20 | = 0.030 | 0.55 [0.11, 1.07] | medium | * |
| from 3 vs from 4 | -0.22 | 20 | = 0.848 | -0.03 [-0.39, 0.50] | negligible | n.s. |
| from 3 vs from 5 | 2.17 | 20 | = 0.090 | 0.45 [0.01, 0.95] | small | n.s. |
| from 3 vs from 6 | 1.62 | 20 | = 0.201 | 0.35 [-0.08, 0.83] | small | n.s. |
| from 4 vs from 5 | 2.63 | 20 | = 0.040 | 0.46 [0.02, 0.93] | small | * |
| from 4 vs from 6 | 1.87 | 20 | = 0.142 | 0.36 [-0.06, 0.82] | small | n.s. |
| from 5 vs from 6 | -0.66 | 20 | = 0.644 | -0.10 [-0.50, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 837.89, BIC = 864.30
- **from 2 vs from 1**: *β* = -0.06, *SE* = 1.004, *z* = -0.063, *p* = 0.950
- **from 3 vs from 1**: *β* = -0.73, *SE* = 1.013, *z* = -0.724, *p* = 0.469
- **from 4 vs from 1**: *β* = 0.45, *SE* = 0.976, *z* = 0.456, *p* = 0.648
- **from 5 vs from 1**: *β* = 0.01, *SE* = 0.990, *z* = 0.009, *p* = 0.993
- **from 6 vs from 1**: *β* = -0.30, *SE* = 0.977, *z* = -0.311, *p* = 0.756
- **SNR**: *β* = 0.07, *SE* = 0.078, *z* = 0.948, *p* = 0.343

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.06 | 1.00 | 0.06 | 0.950 | 1.000 | n.s. |
| from 1 - from 3 | 0.73 | 1.01 | 0.72 | 0.469 | 1.000 | n.s. |
| from 1 - from 4 | -0.45 | 0.98 | -0.46 | 0.648 | 1.000 | n.s. |
| from 1 - from 5 | -0.01 | 0.99 | -0.01 | 0.993 | 1.000 | n.s. |
| from 1 - from 6 | 0.30 | 0.98 | 0.31 | 0.756 | 1.000 | n.s. |
| from 2 - from 3 | 0.67 | 1.04 | 0.64 | 0.520 | 1.000 | n.s. |
| from 2 - from 4 | -0.51 | 1.01 | -0.51 | 0.613 | 1.000 | n.s. |
| from 2 - from 5 | -0.07 | 1.02 | -0.07 | 0.944 | 1.000 | n.s. |
| from 2 - from 6 | 0.24 | 1.00 | 0.24 | 0.810 | 1.000 | n.s. |
| from 3 - from 4 | -1.18 | 1.01 | -1.17 | 0.243 | 0.985 | n.s. |
| from 3 - from 5 | -0.74 | 1.02 | -0.73 | 0.466 | 1.000 | n.s. |
| from 3 - from 6 | -0.43 | 1.02 | -0.42 | 0.673 | 1.000 | n.s. |
| from 4 - from 5 | 0.44 | 0.99 | 0.44 | 0.659 | 1.000 | n.s. |
| from 4 - from 6 | 0.75 | 0.98 | 0.77 | 0.444 | 1.000 | n.s. |
| from 5 - from 6 | 0.31 | 0.99 | 0.31 | 0.753 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.20, *p* = 0.316, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.14 | 20 | = 0.626 | -0.14 [-0.59, 0.30] | negligible | n.s. |
| from 1 vs from 3 | -0.31 | 20 | = 0.793 | -0.04 [-0.40, 0.49] | negligible | n.s. |
| from 1 vs from 4 | -1.47 | 20 | = 0.520 | -0.22 [-0.51, 0.34] | small | n.s. |
| from 1 vs from 5 | -1.49 | 20 | = 0.520 | -0.27 [-0.46, 0.40] | small | n.s. |
| from 1 vs from 6 | -0.45 | 20 | = 0.793 | -0.06 [-0.35, 0.50] | negligible | n.s. |
| from 2 vs from 3 | 0.92 | 20 | = 0.678 | 0.11 [-0.26, 0.66] | negligible | n.s. |
| from 2 vs from 4 | -0.42 | 20 | = 0.793 | -0.06 [-0.58, 0.31] | negligible | n.s. |
| from 2 vs from 5 | -0.85 | 20 | = 0.678 | -0.12 [-0.64, 0.27] | negligible | n.s. |
| from 2 vs from 6 | 0.62 | 20 | = 0.793 | 0.08 [-0.36, 0.53] | negligible | n.s. |
| from 3 vs from 4 | -1.60 | 20 | = 0.520 | -0.18 [-0.66, 0.23] | negligible | n.s. |
| from 3 vs from 5 | -1.95 | 20 | = 0.520 | -0.23 [-0.66, 0.23] | small | n.s. |
| from 3 vs from 6 | -0.27 | 20 | = 0.793 | -0.03 [-0.51, 0.37] | negligible | n.s. |
| from 4 vs from 5 | -0.38 | 20 | = 0.793 | -0.06 [-0.36, 0.50] | negligible | n.s. |
| from 4 vs from 6 | 1.08 | 20 | = 0.626 | 0.14 [-0.25, 0.60] | negligible | n.s. |
| from 5 vs from 6 | 1.41 | 20 | = 0.520 | 0.19 [-0.35, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 177.69, BIC = 199.68
- **from 2 vs from 1**: *β* = 0.31, *SE* = 0.194, *z* = 1.606, *p* = 0.108
- **from 3 vs from 1**: *β* = -0.17, *SE* = 0.203, *z* = -0.821, *p* = 0.412
- **from 4 vs from 1**: *β* = 0.23, *SE* = 0.213, *z* = 1.066, *p* = 0.286
- **from 5 vs from 1**: *β* = 0.26, *SE* = 0.194, *z* = 1.355, *p* = 0.176
- **from 6 vs from 1**: *β* = 0.49, *SE* = 0.200, *z* = 2.467, *p* = 0.014
- **SNR**: *β* = 0.37, *SE* = 0.039, *z* = 9.449, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.31 | 0.19 | -1.61 | 0.108 | 0.682 | n.s. |
| from 1 - from 3 | 0.17 | 0.20 | 0.82 | 0.412 | 0.880 | n.s. |
| from 1 - from 4 | -0.23 | 0.21 | -1.07 | 0.286 | 0.868 | n.s. |
| from 1 - from 5 | -0.26 | 0.19 | -1.35 | 0.176 | 0.824 | n.s. |
| from 1 - from 6 | -0.49 | 0.20 | -2.47 | 0.014 | 0.163 | n.s. |
| from 2 - from 3 | 0.48 | 0.19 | 2.51 | 0.012 | 0.157 | n.s. |
| from 2 - from 4 | 0.08 | 0.20 | 0.42 | 0.673 | 0.965 | n.s. |
| from 2 - from 5 | 0.05 | 0.19 | 0.26 | 0.791 | 0.965 | n.s. |
| from 2 - from 6 | -0.18 | 0.19 | -0.97 | 0.332 | 0.868 | n.s. |
| from 3 - from 4 | -0.39 | 0.20 | -1.94 | 0.053 | 0.449 | n.s. |
| from 3 - from 5 | -0.43 | 0.19 | -2.21 | 0.027 | 0.281 | n.s. |
| from 3 - from 6 | -0.66 | 0.19 | -3.39 | < .001 | 0.010 | * |
| from 4 - from 5 | -0.04 | 0.20 | -0.18 | 0.861 | 0.965 | n.s. |
| from 4 - from 6 | -0.27 | 0.21 | -1.30 | 0.195 | 0.824 | n.s. |
| from 5 - from 6 | -0.23 | 0.19 | -1.19 | 0.233 | 0.843 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.416, η²_G = 0.046
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.18 | 5 | = 0.630 | -0.43 [-1.08, 0.25] | small | n.s. |
| from 1 vs from 3 | -0.45 | 5 | = 0.777 | -0.19 [-0.69, 0.85] | negligible | n.s. |
| from 1 vs from 4 | -1.17 | 5 | = 0.630 | -0.46 [-1.17, 0.54] | small | n.s. |
| from 1 vs from 5 | -0.63 | 5 | = 0.755 | -0.21 [-0.95, 0.29] | small | n.s. |
| from 1 vs from 6 | -1.23 | 5 | = 0.630 | -0.60 [-1.03, 0.44] | medium | n.s. |
| from 2 vs from 3 | 1.31 | 5 | = 0.630 | 0.22 [0.03, 1.46] | small | n.s. |
| from 2 vs from 4 | 0.08 | 5 | = 0.942 | 0.01 [-0.74, 0.69] | negligible | n.s. |
| from 2 vs from 5 | 0.86 | 5 | = 0.713 | 0.29 [-0.51, 0.70] | small | n.s. |
| from 2 vs from 6 | -0.54 | 5 | = 0.766 | -0.15 [-0.68, 0.53] | negligible | n.s. |
| from 3 vs from 4 | -2.40 | 5 | = 0.630 | -0.23 [-2.25, -0.41] | small | n.s. |
| from 3 vs from 5 | 0.10 | 5 | = 0.942 | 0.03 [-1.27, 0.17] | negligible | n.s. |
| from 3 vs from 6 | -1.42 | 5 | = 0.630 | -0.38 [-1.01, 0.37] | small | n.s. |
| from 4 vs from 5 | 0.94 | 5 | = 0.713 | 0.31 [-0.81, 0.62] | small | n.s. |
| from 4 vs from 6 | -0.65 | 5 | = 0.755 | -0.16 [-0.63, 0.80] | negligible | n.s. |
| from 5 vs from 6 | -1.20 | 5 | = 0.630 | -0.47 [-0.79, 0.56] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 481.15, BIC = 503.13
- **from 2 vs from 1**: *β* = 1.30, *SE* = 1.122, *z* = 1.157, *p* = 0.247
- **from 3 vs from 1**: *β* = 1.02, *SE* = 1.168, *z* = 0.871, *p* = 0.384
- **from 4 vs from 1**: *β* = 2.47, *SE* = 1.223, *z* = 2.020, *p* = 0.043
- **from 5 vs from 1**: *β* = 1.30, *SE* = 1.110, *z* = 1.172, *p* = 0.241
- **from 6 vs from 1**: *β* = 2.17, *SE* = 1.154, *z* = 1.876, *p* = 0.061
- **SNR**: *β* = 0.12, *SE* = 0.213, *z* = 0.561, *p* = 0.575

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -1.30 | 1.12 | -1.16 | 0.247 | 0.964 | n.s. |
| from 1 - from 3 | -1.02 | 1.17 | -0.87 | 0.384 | 0.974 | n.s. |
| from 1 - from 4 | -2.47 | 1.22 | -2.02 | 0.043 | 0.486 | n.s. |
| from 1 - from 5 | -1.30 | 1.11 | -1.17 | 0.241 | 0.964 | n.s. |
| from 1 - from 6 | -2.17 | 1.15 | -1.88 | 0.061 | 0.583 | n.s. |
| from 2 - from 3 | 0.28 | 1.10 | 0.26 | 0.798 | 0.998 | n.s. |
| from 2 - from 4 | -1.17 | 1.17 | -1.00 | 0.315 | 0.974 | n.s. |
| from 2 - from 5 | -0.00 | 1.08 | -0.00 | 0.999 | 0.999 | n.s. |
| from 2 - from 6 | -0.87 | 1.09 | -0.80 | 0.424 | 0.974 | n.s. |
| from 3 - from 4 | -1.45 | 1.16 | -1.25 | 0.212 | 0.955 | n.s. |
| from 3 - from 5 | -0.28 | 1.11 | -0.25 | 0.799 | 0.998 | n.s. |
| from 3 - from 6 | -1.15 | 1.12 | -1.02 | 0.306 | 0.974 | n.s. |
| from 4 - from 5 | 1.17 | 1.16 | 1.01 | 0.315 | 0.974 | n.s. |
| from 4 - from 6 | 0.30 | 1.19 | 0.26 | 0.798 | 0.998 | n.s. |
| from 5 - from 6 | -0.86 | 1.12 | -0.77 | 0.440 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.70, *p* = 0.171, η²_G = 0.087
- Greenhouse-Geisser corrected: *p* = 0.241 (ε = 0.312)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 0.44 | 5 | = 0.729 | 0.24 [-0.75, 0.52] | small | n.s. |
| from 1 vs from 3 | -2.76 | 5 | = 0.300 | -0.57 [-1.45, 0.23] | medium | n.s. |
| from 1 vs from 4 | -1.72 | 5 | = 0.380 | -0.48 [-2.00, 0.03] | small | n.s. |
| from 1 vs from 5 | -0.85 | 5 | = 0.590 | -0.17 [-1.13, 0.15] | negligible | n.s. |
| from 1 vs from 6 | -1.86 | 5 | = 0.380 | -0.40 [-1.31, 0.22] | small | n.s. |
| from 2 vs from 3 | -1.66 | 5 | = 0.380 | -1.03 [-0.73, 0.54] | large | n.s. |
| from 2 vs from 4 | -1.57 | 5 | = 0.380 | -1.02 [-1.05, 0.42] | large | n.s. |
| from 2 vs from 5 | -0.69 | 5 | = 0.631 | -0.43 [-0.66, 0.55] | small | n.s. |
| from 2 vs from 6 | -1.17 | 5 | = 0.474 | -0.72 [-1.09, 0.18] | medium | n.s. |
| from 3 vs from 4 | 1.11 | 5 | = 0.474 | 0.14 [-1.05, 0.33] | negligible | n.s. |
| from 3 vs from 5 | 3.03 | 5 | = 0.300 | 0.36 [-0.91, 0.45] | small | n.s. |
| from 3 vs from 6 | 0.65 | 5 | = 0.631 | 0.10 [-0.48, 0.87] | negligible | n.s. |
| from 4 vs from 5 | 1.45 | 5 | = 0.389 | 0.26 [0.01, 1.67] | small | n.s. |
| from 4 vs from 6 | -0.04 | 5 | = 0.968 | -0.01 [-0.71, 0.73] | negligible | n.s. |
| from 5 vs from 6 | -1.79 | 5 | = 0.380 | -0.23 [-1.30, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 375.88, BIC = 400.50
- **from 2 vs from 1**: *β* = 0.05, *SE* = 0.292, *z* = 0.166, *p* = 0.869
- **from 3 vs from 1**: *β* = -0.49, *SE* = 0.291, *z* = -1.696, *p* = 0.090
- **from 4 vs from 1**: *β* = -0.43, *SE* = 0.293, *z* = -1.480, *p* = 0.139
- **from 5 vs from 1**: *β* = -0.40, *SE* = 0.297, *z* = -1.349, *p* = 0.177
- **from 6 vs from 1**: *β* = -0.41, *SE* = 0.292, *z* = -1.410, *p* = 0.159
- **SNR**: *β* = 0.17, *SE* = 0.024, *z* = 7.150, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.05 | 0.29 | -0.17 | 0.869 | 1.000 | n.s. |
| from 1 - from 3 | 0.49 | 0.29 | 1.70 | 0.090 | 0.733 | n.s. |
| from 1 - from 4 | 0.43 | 0.29 | 1.48 | 0.139 | 0.788 | n.s. |
| from 1 - from 5 | 0.40 | 0.30 | 1.35 | 0.177 | 0.790 | n.s. |
| from 1 - from 6 | 0.41 | 0.29 | 1.41 | 0.159 | 0.789 | n.s. |
| from 2 - from 3 | 0.54 | 0.29 | 1.85 | 0.065 | 0.635 | n.s. |
| from 2 - from 4 | 0.48 | 0.29 | 1.65 | 0.099 | 0.743 | n.s. |
| from 2 - from 5 | 0.45 | 0.30 | 1.51 | 0.132 | 0.788 | n.s. |
| from 2 - from 6 | 0.46 | 0.29 | 1.56 | 0.118 | 0.779 | n.s. |
| from 3 - from 4 | -0.06 | 0.29 | -0.20 | 0.838 | 1.000 | n.s. |
| from 3 - from 5 | -0.09 | 0.30 | -0.31 | 0.756 | 1.000 | n.s. |
| from 3 - from 6 | -0.08 | 0.29 | -0.28 | 0.783 | 1.000 | n.s. |
| from 4 - from 5 | -0.03 | 0.29 | -0.11 | 0.911 | 1.000 | n.s. |
| from 4 - from 6 | -0.02 | 0.29 | -0.07 | 0.941 | 1.000 | n.s. |
| from 5 - from 6 | 0.01 | 0.29 | 0.04 | 0.970 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.94, *p* = 0.460, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.07 | 16 | = 0.943 | -0.01 [-0.54, 0.46] | negligible | n.s. |
| from 1 vs from 3 | 0.82 | 16 | = 0.704 | 0.15 [-0.33, 0.64] | negligible | n.s. |
| from 1 vs from 4 | 0.27 | 16 | = 0.908 | 0.04 [-0.44, 0.56] | negligible | n.s. |
| from 1 vs from 5 | 1.42 | 16 | = 0.650 | 0.20 [-0.18, 0.87] | small | n.s. |
| from 1 vs from 6 | 1.27 | 16 | = 0.654 | 0.22 [-0.22, 0.80] | small | n.s. |
| from 2 vs from 3 | 1.61 | 16 | = 0.650 | 0.19 [-0.16, 0.87] | negligible | n.s. |
| from 2 vs from 4 | 0.49 | 16 | = 0.888 | 0.07 [-0.42, 0.57] | negligible | n.s. |
| from 2 vs from 5 | 1.99 | 16 | = 0.650 | 0.26 [-0.06, 1.03] | small | n.s. |
| from 2 vs from 6 | 1.49 | 16 | = 0.650 | 0.28 [-0.17, 0.89] | small | n.s. |
| from 3 vs from 4 | -1.02 | 16 | = 0.654 | -0.12 [-0.76, 0.25] | negligible | n.s. |
| from 3 vs from 5 | 0.38 | 16 | = 0.888 | 0.06 [-0.42, 0.61] | negligible | n.s. |
| from 3 vs from 6 | 0.38 | 16 | = 0.888 | 0.08 [-0.42, 0.58] | negligible | n.s. |
| from 4 vs from 5 | 0.97 | 16 | = 0.654 | 0.18 [-0.38, 0.61] | negligible | n.s. |
| from 4 vs from 6 | 1.08 | 16 | = 0.654 | 0.20 [-0.26, 0.72] | negligible | n.s. |
| from 5 vs from 6 | 0.11 | 16 | = 0.943 | 0.02 [-0.40, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 893.93, BIC = 918.56
- **from 2 vs from 1**: *β* = -3.00, *SE* = 2.967, *z* = -1.010, *p* = 0.313
- **from 3 vs from 1**: *β* = -0.12, *SE* = 2.952, *z* = -0.042, *p* = 0.966
- **from 4 vs from 1**: *β* = 3.16, *SE* = 2.979, *z* = 1.061, *p* = 0.289
- **from 5 vs from 1**: *β* = -3.13, *SE* = 3.018, *z* = -1.038, *p* = 0.299
- **from 6 vs from 1**: *β* = -0.91, *SE* = 2.968, *z* = -0.305, *p* = 0.760
- **SNR**: *β* = -0.10, *SE* = 0.231, *z* = -0.439, *p* = 0.661

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 3.00 | 2.97 | 1.01 | 0.313 | 0.976 | n.s. |
| from 1 - from 3 | 0.13 | 2.95 | 0.04 | 0.966 | 0.999 | n.s. |
| from 1 - from 4 | -3.16 | 2.98 | -1.06 | 0.289 | 0.976 | n.s. |
| from 1 - from 5 | 3.13 | 3.02 | 1.04 | 0.299 | 0.976 | n.s. |
| from 1 - from 6 | 0.91 | 2.97 | 0.31 | 0.760 | 0.997 | n.s. |
| from 2 - from 3 | -2.87 | 2.98 | -0.96 | 0.335 | 0.976 | n.s. |
| from 2 - from 4 | -6.16 | 2.97 | -2.07 | 0.038 | 0.419 | n.s. |
| from 2 - from 5 | 0.14 | 3.02 | 0.05 | 0.964 | 0.999 | n.s. |
| from 2 - from 6 | -2.09 | 2.99 | -0.70 | 0.485 | 0.976 | n.s. |
| from 3 - from 4 | -3.29 | 2.95 | -1.11 | 0.266 | 0.975 | n.s. |
| from 3 - from 5 | 3.01 | 3.02 | 1.00 | 0.319 | 0.976 | n.s. |
| from 3 - from 6 | 0.78 | 2.99 | 0.26 | 0.794 | 0.997 | n.s. |
| from 4 - from 5 | 6.29 | 2.99 | 2.11 | 0.035 | 0.415 | n.s. |
| from 4 - from 6 | 4.07 | 2.97 | 1.37 | 0.171 | 0.912 | n.s. |
| from 5 - from 6 | -2.23 | 3.00 | -0.74 | 0.457 | 0.976 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.496, η²_G = 0.020
- Greenhouse-Geisser corrected: *p* = 0.452 (ε = 0.571)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 1.53 | 16 | = 0.637 | 0.30 [-0.15, 0.88] | small | n.s. |
| from 1 vs from 3 | 0.28 | 16 | = 0.838 | 0.07 [-0.47, 0.50] | negligible | n.s. |
| from 1 vs from 4 | -1.15 | 16 | = 0.637 | -0.16 [-0.77, 0.24] | negligible | n.s. |
| from 1 vs from 5 | 1.01 | 16 | = 0.637 | 0.21 [-0.28, 0.77] | small | n.s. |
| from 1 vs from 6 | 0.30 | 16 | = 0.838 | 0.08 [-0.36, 0.64] | negligible | n.s. |
| from 2 vs from 3 | -1.06 | 16 | = 0.637 | -0.24 [-0.87, 0.16] | small | n.s. |
| from 2 vs from 4 | -2.78 | 16 | = 0.202 | -0.48 [-0.97, 0.07] | small | n.s. |
| from 2 vs from 5 | -0.30 | 16 | = 0.838 | -0.07 [-0.59, 0.44] | negligible | n.s. |
| from 2 vs from 6 | -0.72 | 16 | = 0.719 | -0.16 [-0.69, 0.34] | negligible | n.s. |
| from 3 vs from 4 | -0.90 | 16 | = 0.637 | -0.23 [-0.79, 0.22] | small | n.s. |
| from 3 vs from 5 | 0.92 | 16 | = 0.637 | 0.15 [-0.30, 0.74] | negligible | n.s. |
| from 3 vs from 6 | 0.09 | 16 | = 0.926 | 0.03 [-0.47, 0.52] | negligible | n.s. |
| from 4 vs from 5 | 1.63 | 16 | = 0.637 | 0.37 [-0.06, 0.99] | small | n.s. |
| from 4 vs from 6 | 1.09 | 16 | = 0.637 | 0.21 [-0.16, 0.83] | small | n.s. |
| from 5 vs from 6 | -0.38 | 16 | = 0.838 | -0.10 [-0.67, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed smaller amplitude than from 2 (*d* = -0.61)
  - from 1 showed smaller amplitude than from 3 (*d* = -0.39)
  - from 1 showed smaller amplitude than from 4 (*d* = -0.40)
  - from 2 showed greater amplitude than from 5 (*d* = 0.67)
  - from 2 showed greater amplitude than from 6 (*d* = 0.55)
  - from 4 showed greater amplitude than from 5 (*d* = 0.46)

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
