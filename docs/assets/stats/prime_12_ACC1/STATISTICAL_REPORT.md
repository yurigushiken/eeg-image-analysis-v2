# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:49:57

---

## 1. Analysis Overview

**Total Measurements:** 336
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 1a | 9 | 80.00 ms | 20.10 | 6.70 | [44.00, 108.00] |
| 1b | 14 | 72.00 ms | 25.30 | 6.76 | [44.00, 104.00] |
| 1c | 8 | 91.00 ms | 13.48 | 4.77 | [64.00, 108.00] |
| 1d | 12 | 75.67 ms | 20.64 | 5.96 | [44.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 9 | -6.21 µV | 3.76 | 1.25 | [-14.76, -3.21] |
| 1b | 14 | -5.29 µV | 2.42 | 0.65 | [-10.41, -2.61] |
| 1c | 8 | -4.78 µV | 2.46 | 0.87 | [-9.79, -1.78] |
| 1d | 12 | -6.87 µV | 3.21 | 0.93 | [-11.33, -2.95] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 178.77 ms | 19.76 | 5.48 | [140.00, 204.00] |
| 1b | 15 | 180.53 ms | 19.70 | 5.09 | [152.00, 204.00] |
| 1c | 20 | 177.60 ms | 15.76 | 3.52 | [144.00, 200.00] |
| 1d | 16 | 162.50 ms | 16.96 | 4.24 | [140.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | -8.00 µV | 2.20 | 0.61 | [-11.43, -3.33] |
| 1b | 15 | -7.13 µV | 3.06 | 0.79 | [-13.50, -2.13] |
| 1c | 20 | -7.18 µV | 2.57 | 0.57 | [-13.26, -3.09] |
| 1d | 16 | -7.40 µV | 3.03 | 0.76 | [-14.39, -3.68] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 10 | 78.40 ms | 9.65 | 3.05 | [68.00, 96.00] |
| 1b | 10 | 84.40 ms | 8.93 | 2.83 | [68.00, 96.00] |
| 1c | 11 | 86.91 ms | 10.44 | 3.15 | [68.00, 96.00] |
| 1d | 12 | 78.00 ms | 10.58 | 3.06 | [68.00, 96.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 10 | 3.83 µV | 1.83 | 0.58 | [0.75, 6.37] |
| 1b | 10 | 4.05 µV | 2.50 | 0.79 | [0.68, 7.63] |
| 1c | 11 | 3.94 µV | 1.89 | 0.57 | [1.43, 7.27] |
| 1d | 12 | 6.22 µV | 5.07 | 1.46 | [2.34, 20.35] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 498.77 ms | 39.95 | 11.08 | [448.00, 544.00] |
| 1b | 13 | 498.15 ms | 38.84 | 10.77 | [436.00, 544.00] |
| 1c | 16 | 487.75 ms | 38.49 | 9.62 | [432.00, 544.00] |
| 1d | 15 | 481.07 ms | 34.06 | 8.79 | [432.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 7.21 µV | 3.68 | 1.02 | [2.99, 16.08] |
| 1b | 13 | 8.83 µV | 3.50 | 0.97 | [3.75, 14.88] |
| 1c | 16 | 7.93 µV | 5.99 | 1.50 | [1.96, 22.66] |
| 1d | 15 | 8.76 µV | 3.71 | 0.96 | [3.64, 17.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 389.56, BIC = 401.89
- **1b vs 1a**: *β* = -8.89, *SE* = 8.258, *z* = -1.077, *p* = 0.281
- **1c vs 1a**: *β* = 9.72, *SE* = 10.619, *z* = 0.915, *p* = 0.360
- **1d vs 1a**: *β* = -7.79, *SE* = 9.095, *z* = -0.857, *p* = 0.392
- **SNR**: *β* = 9.34, *SE* = 4.139, *z* = 2.256, *p* = 0.024

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 8.89 | 8.26 | 1.08 | 0.281 | 0.733 | n.s. |
| 1a - 1c | -9.72 | 10.62 | -0.92 | 0.360 | 0.738 | n.s. |
| 1a - 1d | 7.79 | 9.09 | 0.86 | 0.392 | 0.738 | n.s. |
| 1b - 1c | -18.61 | 9.14 | -2.04 | 0.042 | 0.225 | n.s. |
| 1b - 1d | -1.10 | 7.69 | -0.14 | 0.886 | 0.886 | n.s. |
| 1c - 1d | 17.51 | 8.94 | 1.96 | 0.050 | 0.227 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 213.50, BIC = 225.83
- **1b vs 1a**: *β* = 1.13, *SE* = 1.031, *z* = 1.095, *p* = 0.273
- **1c vs 1a**: *β* = 1.74, *SE* = 1.223, *z* = 1.424, *p* = 0.155
- **1d vs 1a**: *β* = 0.22, *SE* = 1.099, *z* = 0.199, *p* = 0.843
- **SNR**: *β* = -1.96, *SE* = 0.532, *z* = -3.684, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -1.13 | 1.03 | -1.10 | 0.273 | 0.721 | n.s. |
| 1a - 1c | -1.74 | 1.22 | -1.42 | 0.155 | 0.635 | n.s. |
| 1a - 1d | -0.22 | 1.10 | -0.20 | 0.843 | 0.843 | n.s. |
| 1b - 1c | -0.61 | 1.09 | -0.56 | 0.575 | 0.820 | n.s. |
| 1b - 1d | 0.91 | 0.97 | 0.94 | 0.347 | 0.722 | n.s. |
| 1c - 1d | 1.52 | 1.17 | 1.30 | 0.194 | 0.660 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 553.86, BIC = 568.97
- **1b vs 1a**: *β* = 3.01, *SE* = 5.685, *z* = 0.529, *p* = 0.597
- **1c vs 1a**: *β* = -0.61, *SE* = 5.154, *z* = -0.119, *p* = 0.906
- **1d vs 1a**: *β* = -13.88, *SE* = 5.625, *z* = -2.468, *p* = 0.014
- **SNR**: *β* = -0.38, *SE* = 1.061, *z* = -0.361, *p* = 0.718

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -3.01 | 5.69 | -0.53 | 0.597 | 0.848 | n.s. |
| 1a - 1c | 0.61 | 5.15 | 0.12 | 0.906 | 0.906 | n.s. |
| 1a - 1d | 13.88 | 5.63 | 2.47 | 0.014 | 0.053 | n.s. |
| 1b - 1c | 3.62 | 4.96 | 0.73 | 0.466 | 0.848 | n.s. |
| 1b - 1d | 16.89 | 5.12 | 3.30 | < .001 | 0.006 | ** |
| 1c - 1d | 13.27 | 4.88 | 2.72 | 0.007 | 0.032 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.77, *p* = 0.207, η²_G = 0.208
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.10 | 4 | = 0.922 | 0.04 [-0.98, 0.70] | negligible | n.s. |
| 1a vs 1c | 1.21 | 4 | = 0.353 | 0.71 [-0.73, 0.61] | medium | n.s. |
| 1a vs 1d | 1.57 | 4 | = 0.353 | 1.30 [-0.27, 1.24] | large | n.s. |
| 1b vs 1c | 1.33 | 4 | = 0.353 | 0.48 [-0.15, 1.21] | small | n.s. |
| 1b vs 1d | 1.41 | 4 | = 0.353 | 0.94 [-0.06, 1.44] | large | n.s. |
| 1c vs 1d | 1.26 | 4 | = 0.353 | 0.67 [0.03, 1.31] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 284.23, BIC = 299.34
- **1b vs 1a**: *β* = -0.95, *SE* = 0.692, *z* = -1.377, *p* = 0.168
- **1c vs 1a**: *β* = 0.11, *SE* = 0.626, *z* = 0.171, *p* = 0.864
- **1d vs 1a**: *β* = -0.52, *SE* = 0.668, *z* = -0.770, *p* = 0.441
- **SNR**: *β* = -0.80, *SE* = 0.128, *z* = -6.259, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 0.95 | 0.69 | 1.38 | 0.168 | 0.602 | n.s. |
| 1a - 1c | -0.11 | 0.63 | -0.17 | 0.864 | 0.864 | n.s. |
| 1a - 1d | 0.51 | 0.67 | 0.77 | 0.441 | 0.825 | n.s. |
| 1b - 1c | -1.06 | 0.60 | -1.77 | 0.076 | 0.377 | n.s. |
| 1b - 1d | -0.44 | 0.63 | -0.70 | 0.485 | 0.825 | n.s. |
| 1c - 1d | 0.62 | 0.59 | 1.06 | 0.289 | 0.745 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.05, *p* = 0.406, η²_G = 0.160
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -1.18 | 4 | = 0.629 | -0.70 [-0.87, 0.80] | medium | n.s. |
| 1a vs 1c | -0.55 | 4 | = 0.737 | -0.31 [-0.77, 0.57] | small | n.s. |
| 1a vs 1d | -2.30 | 4 | = 0.498 | -1.29 [-1.05, 0.42] | large | n.s. |
| 1b vs 1c | 0.90 | 4 | = 0.629 | 0.37 [-0.85, 0.44] | small | n.s. |
| 1b vs 1d | -0.34 | 4 | = 0.754 | -0.27 [-1.12, 0.28] | small | n.s. |
| 1c vs 1d | -1.01 | 4 | = 0.629 | -0.75 [-0.57, 0.58] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 329.15, BIC = 341.48
- **1b vs 1a**: *β* = 6.12, *SE* = 4.315, *z* = 1.417, *p* = 0.156
- **1c vs 1a**: *β* = 8.40, *SE* = 4.133, *z* = 2.033, *p* = 0.042
- **1d vs 1a**: *β* = -0.96, *SE* = 4.157, *z* = -0.232, *p* = 0.817
- **SNR**: *β* = 0.76, *SE* = 1.112, *z* = 0.681, *p* = 0.496

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -6.12 | 4.31 | -1.42 | 0.156 | 0.400 | n.s. |
| 1a - 1c | -8.40 | 4.13 | -2.03 | 0.042 | 0.194 | n.s. |
| 1a - 1d | 0.96 | 4.16 | 0.23 | 0.817 | 0.834 | n.s. |
| 1b - 1c | -2.28 | 4.26 | -0.54 | 0.592 | 0.834 | n.s. |
| 1b - 1d | 7.08 | 4.18 | 1.69 | 0.090 | 0.315 | n.s. |
| 1c - 1d | 9.36 | 4.05 | 2.31 | 0.021 | 0.119 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.476, η²_G = 0.432
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.33 | 1 | = 1.000 | -0.45 [-1.32, 0.81] | small | n.s. |
| 1a vs 1c | -4.00 | 1 | = 0.468 | -4.00 [-2.69, 1.01] | large | n.s. |
| 1a vs 1d | -0.20 | 1 | = 1.000 | -0.14 [-0.86, 1.26] | negligible | n.s. |
| 1b vs 1c | -7.00 | 1 | = 0.468 | -7.00 [-3.23, -0.03] | large | n.s. |
| 1b vs 1d | 0.00 | 1 | = 1.000 | 0.00 [-1.10, 2.40] | negligible | n.s. |
| 1c vs 1d | 1.00 | 1 | = 1.000 | 1.00 [-0.99, 2.77] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 213.48, BIC = 225.81
- **1b vs 1a**: *β* = 0.43, *SE* = 1.102, *z* = 0.391, *p* = 0.696
- **1c vs 1a**: *β* = -0.09, *SE* = 1.113, *z* = -0.080, *p* = 0.936
- **1d vs 1a**: *β* = 1.35, *SE* = 1.125, *z* = 1.204, *p* = 0.229
- **SNR**: *β* = 1.39, *SE* = 0.289, *z* = 4.802, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -0.43 | 1.10 | -0.39 | 0.696 | 0.953 | n.s. |
| 1a - 1c | 0.09 | 1.11 | 0.08 | 0.936 | 0.953 | n.s. |
| 1a - 1d | -1.35 | 1.12 | -1.20 | 0.229 | 0.727 | n.s. |
| 1b - 1c | 0.52 | 1.10 | 0.47 | 0.638 | 0.953 | n.s. |
| 1b - 1d | -0.92 | 1.12 | -0.82 | 0.410 | 0.879 | n.s. |
| 1c - 1d | -1.44 | 1.04 | -1.38 | 0.166 | 0.664 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 18.08, *p* = 0.020, η²_G = 0.932
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -3.16 | 1 | = 0.292 | -4.38 [-1.91, 0.45] | large | n.s. |
| 1a vs 1c | -0.10 | 1 | = 0.939 | -0.07 [-1.95, 1.31] | negligible | n.s. |
| 1a vs 1d | -181.52 | 1 | = 0.021 | -4.50 [-1.67, 0.58] | large | * |
| 1b vs 1c | 5.72 | 1 | = 0.220 | 7.34 [-0.86, 1.26] | large | n.s. |
| 1b vs 1d | -0.61 | 1 | = 0.784 | -0.84 [-1.24, 2.09] | large | n.s. |
| 1c vs 1d | -8.54 | 1 | = 0.220 | -6.21 [-2.64, 1.03] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 582.58, BIC = 596.88
- **1b vs 1a**: *β* = 2.25, *SE* = 13.089, *z* = 0.172, *p* = 0.864
- **1c vs 1a**: *β* = -13.71, *SE* = 12.708, *z* = -1.079, *p* = 0.280
- **1d vs 1a**: *β* = -19.43, *SE* = 12.493, *z* = -1.556, *p* = 0.120
- **SNR**: *β* = -3.06, *SE* = 2.691, *z* = -1.138, *p* = 0.255

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -2.25 | 13.09 | -0.17 | 0.864 | 0.864 | n.s. |
| 1a - 1c | 13.71 | 12.71 | 1.08 | 0.280 | 0.628 | n.s. |
| 1a - 1d | 19.43 | 12.49 | 1.56 | 0.120 | 0.472 | n.s. |
| 1b - 1c | 15.96 | 12.69 | 1.26 | 0.209 | 0.608 | n.s. |
| 1b - 1d | 21.68 | 12.71 | 1.71 | 0.088 | 0.425 | n.s. |
| 1c - 1d | 5.72 | 11.83 | 0.48 | 0.629 | 0.862 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.469, η²_G = 0.078
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -1.38 | 4 | = 0.478 | -0.48 [-0.90, 0.77] | small | n.s. |
| 1a vs 1c | -0.38 | 4 | = 0.814 | -0.22 [-0.94, 0.91] | small | n.s. |
| 1a vs 1d | 0.25 | 4 | = 0.814 | 0.16 [-0.33, 1.16] | negligible | n.s. |
| 1b vs 1c | 0.93 | 4 | = 0.605 | 0.35 [-0.48, 0.97] | small | n.s. |
| 1b vs 1d | 1.61 | 4 | = 0.478 | 0.65 [-0.04, 1.59] | medium | n.s. |
| 1c vs 1d | 2.13 | 4 | = 0.478 | 0.43 [-0.64, 0.70] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 320.75, BIC = 335.05
- **1b vs 1a**: *β* = 1.44, *SE* = 1.283, *z* = 1.124, *p* = 0.261
- **1c vs 1a**: *β* = 1.44, *SE* = 1.256, *z* = 1.146, *p* = 0.252
- **1d vs 1a**: *β* = 1.77, *SE* = 1.226, *z* = 1.442, *p* = 0.149
- **SNR**: *β* = 1.12, *SE* = 0.256, *z* = 4.373, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -1.44 | 1.28 | -1.12 | 0.261 | 0.766 | n.s. |
| 1a - 1c | -1.44 | 1.26 | -1.15 | 0.252 | 0.766 | n.s. |
| 1a - 1d | -1.77 | 1.23 | -1.44 | 0.149 | 0.621 | n.s. |
| 1b - 1c | 0.00 | 1.23 | 0.00 | 0.998 | 0.998 | n.s. |
| 1b - 1d | -0.33 | 1.23 | -0.27 | 0.791 | 0.989 | n.s. |
| 1c - 1d | -0.33 | 1.16 | -0.28 | 0.777 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.933, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.48 | 4 | = 0.967 | -0.28 [-1.26, 0.48] | small | n.s. |
| 1a vs 1c | -0.43 | 4 | = 0.967 | -0.16 [-0.78, 1.08] | negligible | n.s. |
| 1a vs 1d | 0.04 | 4 | = 0.967 | 0.03 [-0.85, 0.59] | negligible | n.s. |
| 1b vs 1c | 0.14 | 4 | = 0.967 | 0.05 [-0.51, 0.93] | negligible | n.s. |
| 1b vs 1d | 0.55 | 4 | = 0.967 | 0.28 [-0.75, 0.69] | small | n.s. |
| 1c vs 1d | 0.39 | 4 | = 0.967 | 0.18 [-0.67, 0.68] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.020). Post-hoc tests revealed:
  - 1a showed smaller amplitude than 1d (*d* = -4.50)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 Fz Component

#### Latency

#### Amplitude

### 5.2 N1 Component

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

### 5.3 P1 Component

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

### 5.4 P3b Component

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
