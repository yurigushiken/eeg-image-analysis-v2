# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:27:53

---

## 1. Analysis Overview

**Total Measurements:** 252
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 1a | 13 | -4.82 µV | 2.15 | 0.60 | [-8.42, -0.62] |
| 1b | 15 | -3.69 µV | 2.64 | 0.68 | [-8.79, -0.16] |
| 1c | 20 | -4.15 µV | 2.28 | 0.51 | [-9.60, -0.18] |
| 1d | 16 | -3.90 µV | 2.59 | 0.65 | [-10.70, -0.64] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 175.61 ms | 10.86 | 3.01 | [161.15, 196.99] |
| 1b | 15 | 171.97 ms | 12.64 | 3.26 | [148.28, 195.75] |
| 1c | 20 | 174.99 ms | 11.73 | 2.62 | [154.15, 198.56] |
| 1d | 16 | 163.31 ms | 11.00 | 2.75 | [146.82, 182.30] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 10 | 2.08 µV | 1.69 | 0.53 | [0.24, 4.69] |
| 1b | 10 | 2.72 µV | 1.72 | 0.54 | [0.28, 4.77] |
| 1c | 11 | 1.82 µV | 1.21 | 0.37 | [0.19, 4.18] |
| 1d | 12 | 4.36 µV | 4.15 | 1.20 | [0.44, 15.69] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 10 | 79.28 ms | 6.80 | 2.15 | [69.11, 92.53] |
| 1b | 10 | 82.72 ms | 3.65 | 1.16 | [75.18, 86.62] |
| 1c | 11 | 82.58 ms | 7.01 | 2.11 | [69.21, 90.96] |
| 1d | 12 | 79.30 ms | 4.49 | 1.30 | [70.14, 84.11] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 4.32 µV | 3.98 | 1.10 | [0.02, 13.22] |
| 1b | 13 | 5.20 µV | 3.27 | 0.91 | [0.62, 10.46] |
| 1c | 16 | 3.86 µV | 3.59 | 0.90 | [-0.14, 10.33] |
| 1d | 15 | 4.97 µV | 2.98 | 0.77 | [1.14, 11.03] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 492.69 ms | 27.59 | 7.65 | [458.35, 543.22] |
| 1b | 13 | 490.49 ms | 22.27 | 6.18 | [455.55, 537.79] |
| 1c | 16 | 489.54 ms | 24.32 | 6.08 | [452.27, 538.06] |
| 1d | 15 | 483.52 ms | 17.02 | 4.39 | [452.23, 511.17] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 240.37, BIC = 255.49
- **1b vs 1a**: *β* = -0.55, *SE* = 0.551, *z* = -0.999, *p* = 0.318
- **1c vs 1a**: *β* = 0.11, *SE* = 0.492, *z* = 0.221, *p* = 0.825
- **1d vs 1a**: *β* = -0.33, *SE* = 0.516, *z* = -0.633, *p* = 0.527
- **SNR**: *β* = -0.97, *SE* = 0.093, *z* = -10.469, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 0.55 | 0.55 | 1.00 | 0.318 | 0.852 | n.s. |
| 1a - 1c | -0.11 | 0.49 | -0.22 | 0.825 | 0.894 | n.s. |
| 1a - 1d | 0.33 | 0.52 | 0.63 | 0.527 | 0.894 | n.s. |
| 1b - 1c | -0.66 | 0.47 | -1.41 | 0.159 | 0.647 | n.s. |
| 1b - 1d | -0.22 | 0.51 | -0.44 | 0.662 | 0.894 | n.s. |
| 1c - 1d | 0.44 | 0.47 | 0.93 | 0.353 | 0.852 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.41, *p* = 0.288, η²_G = 0.241
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.88 | 4 | = 0.573 | -0.65 [-1.19, 0.52] | medium | n.s. |
| 1a vs 1c | -0.98 | 4 | = 0.573 | -0.71 [-0.76, 0.59] | medium | n.s. |
| 1a vs 1d | -3.61 | 4 | = 0.136 | -1.86 [-1.19, 0.31] | large | n.s. |
| 1b vs 1c | -0.17 | 4 | = 0.870 | -0.07 [-0.75, 0.52] | negligible | n.s. |
| 1b vs 1d | -0.99 | 4 | = 0.573 | -0.79 [-1.16, 0.25] | medium | n.s. |
| 1c vs 1d | -0.78 | 4 | = 0.573 | -0.69 [-0.73, 0.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 500.94, BIC = 516.05
- **1b vs 1a**: *β* = -2.93, *SE* = 3.962, *z* = -0.739, *p* = 0.460
- **1c vs 1a**: *β* = 0.36, *SE* = 3.586, *z* = 0.099, *p* = 0.921
- **1d vs 1a**: *β* = -11.54, *SE* = 3.872, *z* = -2.980, *p* = 0.003
- **SNR**: *β* = -0.70, *SE* = 0.704, *z* = -0.995, *p* = 0.320

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 2.93 | 3.96 | 0.74 | 0.460 | 0.708 | n.s. |
| 1a - 1c | -0.36 | 3.59 | -0.10 | 0.921 | 0.921 | n.s. |
| 1a - 1d | 11.54 | 3.87 | 2.98 | 0.003 | 0.014 | * |
| 1b - 1c | -3.29 | 3.41 | -0.96 | 0.336 | 0.707 | n.s. |
| 1b - 1d | 8.61 | 3.53 | 2.44 | 0.015 | 0.057 | n.s. |
| 1c - 1d | 11.89 | 3.33 | 3.57 | < .001 | 0.002 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.94, *p* = 0.036, η²_G = 0.345
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.12 | 4 | = 0.907 | -0.07 [-1.29, 0.45] | negligible | n.s. |
| 1a vs 1c | 0.21 | 4 | = 0.907 | 0.13 [-0.72, 0.63] | negligible | n.s. |
| 1a vs 1d | 2.73 | 4 | = 0.157 | 1.99 [-0.14, 1.44] | large | n.s. |
| 1b vs 1c | 0.43 | 4 | = 0.907 | 0.16 [-0.99, 0.32] | negligible | n.s. |
| 1b vs 1d | 3.12 | 4 | = 0.157 | 1.67 [0.13, 1.74] | large | n.s. |
| 1c vs 1d | 2.18 | 4 | = 0.189 | 1.08 [0.08, 1.38] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 182.35, BIC = 194.68
- **1b vs 1a**: *β* = 0.82, *SE* = 0.756, *z* = 1.082, *p* = 0.279
- **1c vs 1a**: *β* = -0.51, *SE* = 0.774, *z* = -0.660, *p* = 0.509
- **1d vs 1a**: *β* = 1.23, *SE* = 0.775, *z* = 1.580, *p* = 0.114
- **SNR**: *β* = 1.33, *SE* = 0.201, *z* = 6.621, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -0.82 | 0.76 | -1.08 | 0.279 | 0.625 | n.s. |
| 1a - 1c | 0.51 | 0.77 | 0.66 | 0.509 | 0.759 | n.s. |
| 1a - 1d | -1.22 | 0.78 | -1.58 | 0.114 | 0.384 | n.s. |
| 1b - 1c | 1.33 | 0.75 | 1.76 | 0.078 | 0.332 | n.s. |
| 1b - 1d | -0.41 | 0.76 | -0.53 | 0.594 | 0.759 | n.s. |
| 1c - 1d | -1.74 | 0.72 | -2.42 | 0.016 | 0.090 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.24, *p* = 0.103, η²_G = 0.685
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -2.44 | 1 | = 0.372 | -2.52 [-2.28, 0.29] | large | n.s. |
| 1a vs 1c | -0.10 | 1 | = 0.935 | -0.06 [-2.05, 1.26] | negligible | n.s. |
| 1a vs 1d | -5.55 | 1 | = 0.340 | -1.64 [-1.62, 0.61] | large | n.s. |
| 1b vs 1c | 6.26 | 1 | = 0.340 | 6.79 [-0.69, 1.49] | large | n.s. |
| 1b vs 1d | -0.32 | 1 | = 0.935 | -0.33 [-1.18, 2.21] | small | n.s. |
| 1c vs 1d | -2.50 | 1 | = 0.372 | -1.87 [-2.53, 1.06] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 277.96, BIC = 290.28
- **1b vs 1a**: *β* = 3.60, *SE* = 2.718, *z* = 1.324, *p* = 0.185
- **1c vs 1a**: *β* = 3.16, *SE* = 2.350, *z* = 1.344, *p* = 0.179
- **1d vs 1a**: *β* = -0.76, *SE* = 2.499, *z* = -0.304, *p* = 0.761
- **SNR**: *β* = 1.05, *SE* = 0.778, *z* = 1.348, *p* = 0.178

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -3.60 | 2.72 | -1.32 | 0.185 | 0.561 | n.s. |
| 1a - 1c | -3.16 | 2.35 | -1.34 | 0.179 | 0.561 | n.s. |
| 1a - 1d | 0.76 | 2.50 | 0.30 | 0.761 | 0.943 | n.s. |
| 1b - 1c | 0.44 | 3.02 | 0.15 | 0.884 | 0.943 | n.s. |
| 1b - 1d | 4.36 | 2.32 | 1.88 | 0.061 | 0.313 | n.s. |
| 1c - 1d | 3.92 | 2.73 | 1.43 | 0.152 | 0.561 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.27, *p* = 0.425, η²_G = 0.493
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -1.23 | 1 | = 0.768 | -1.71 [-1.43, 0.73] | large | n.s. |
| 1a vs 1c | -2.47 | 1 | = 0.768 | -2.55 [-2.57, 1.05] | large | n.s. |
| 1a vs 1d | 0.07 | 1 | = 0.957 | 0.03 [-1.05, 1.04] | negligible | n.s. |
| 1b vs 1c | -0.63 | 1 | = 0.768 | -0.61 [-1.62, 0.61] | medium | n.s. |
| 1b vs 1d | 0.78 | 1 | = 0.768 | 0.99 [-0.87, 3.37] | large | n.s. |
| 1c vs 1d | 1.24 | 1 | = 0.768 | 1.26 [-1.00, 2.73] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 271.15, BIC = 285.45
- **1b vs 1a**: *β* = 0.75, *SE* = 0.809, *z* = 0.923, *p* = 0.356
- **1c vs 1a**: *β* = 0.59, *SE* = 0.792, *z* = 0.747, *p* = 0.455
- **1d vs 1a**: *β* = 1.06, *SE* = 0.769, *z* = 1.382, *p* = 0.167
- **SNR**: *β* = 1.26, *SE* = 0.163, *z* = 7.727, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -0.75 | 0.81 | -0.92 | 0.356 | 0.889 | n.s. |
| 1a - 1c | -0.59 | 0.79 | -0.75 | 0.455 | 0.912 | n.s. |
| 1a - 1d | -1.06 | 0.77 | -1.38 | 0.167 | 0.666 | n.s. |
| 1b - 1c | 0.15 | 0.78 | 0.20 | 0.842 | 0.912 | n.s. |
| 1b - 1d | -0.32 | 0.77 | -0.41 | 0.683 | 0.912 | n.s. |
| 1c - 1d | -0.47 | 0.73 | -0.64 | 0.519 | 0.912 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.788, η²_G = 0.043
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.44 | 4 | = 0.851 | -0.24 [-1.30, 0.45] | small | n.s. |
| 1a vs 1c | 0.05 | 4 | = 0.964 | 0.02 [-0.63, 1.27] | negligible | n.s. |
| 1a vs 1d | 0.40 | 4 | = 0.851 | 0.27 [-0.72, 0.71] | small | n.s. |
| 1b vs 1c | 1.24 | 4 | = 0.851 | 0.29 [-0.61, 0.83] | small | n.s. |
| 1b vs 1d | 1.05 | 4 | = 0.851 | 0.62 [-0.60, 0.84] | medium | n.s. |
| 1c vs 1d | 0.51 | 4 | = 0.851 | 0.28 [-0.70, 0.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 528.62, BIC = 542.92
- **1b vs 1a**: *β* = -2.23, *SE* = 8.678, *z* = -0.257, *p* = 0.797
- **1c vs 1a**: *β* = -3.98, *SE* = 8.355, *z* = -0.477, *p* = 0.633
- **1d vs 1a**: *β* = -9.48, *SE* = 8.420, *z* = -1.126, *p* = 0.260
- **SNR**: *β* = -1.03, *SE* = 1.627, *z* = -0.634, *p* = 0.526

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 2.23 | 8.68 | 0.26 | 0.797 | 0.959 | n.s. |
| 1a - 1c | 3.98 | 8.36 | 0.48 | 0.633 | 0.951 | n.s. |
| 1a - 1d | 9.48 | 8.42 | 1.13 | 0.260 | 0.836 | n.s. |
| 1b - 1c | 1.76 | 8.36 | 0.21 | 0.834 | 0.959 | n.s. |
| 1b - 1d | 7.26 | 8.47 | 0.86 | 0.392 | 0.917 | n.s. |
| 1c - 1d | 5.50 | 8.02 | 0.69 | 0.493 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.11, *p* = 0.385, η²_G = 0.141
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 1.07 | 4 | = 0.608 | 0.62 [-0.53, 1.19] | medium | n.s. |
| 1a vs 1c | 0.67 | 4 | = 0.608 | 0.36 [-0.94, 0.91] | small | n.s. |
| 1a vs 1d | 1.53 | 4 | = 0.608 | 0.94 [-0.31, 1.19] | large | n.s. |
| 1b vs 1c | -0.83 | 4 | = 0.608 | -0.31 [-0.86, 0.58] | small | n.s. |
| 1b vs 1d | 0.56 | 4 | = 0.608 | 0.32 [-0.25, 1.27] | small | n.s. |
| 1c vs 1d | 0.98 | 4 | = 0.608 | 0.69 [-0.57, 0.77] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.036) (no significant pairwise comparisons)

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
