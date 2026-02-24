# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:24:15

---

## 1. Analysis Overview

**Total Measurements:** 384
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
| 1 to 3 | 24 | 89.83 ms | 16.30 | 3.33 | [68.00, 112.00] |
| 2 to 4 | 24 | 90.17 ms | 17.61 | 3.60 | [68.00, 112.00] |
| 3 to 5 | 24 | 94.33 ms | 15.82 | 3.23 | [68.00, 112.00] |
| 4 to 6 | 24 | 93.67 ms | 17.96 | 3.67 | [68.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -0.83 µV | 2.50 | 0.51 | [-5.86, 4.13] |
| 2 to 4 | 24 | -2.56 µV | 2.01 | 0.41 | [-6.04, 1.98] |
| 3 to 5 | 24 | -1.77 µV | 2.18 | 0.45 | [-4.98, 3.69] |
| 4 to 6 | 24 | -2.34 µV | 2.31 | 0.47 | [-7.19, 2.49] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 169.67 ms | 23.97 | 4.89 | [136.00, 208.00] |
| 2 to 4 | 24 | 173.00 ms | 18.32 | 3.74 | [136.00, 208.00] |
| 3 to 5 | 24 | 166.33 ms | 23.68 | 4.83 | [136.00, 208.00] |
| 4 to 6 | 24 | 166.83 ms | 20.58 | 4.20 | [136.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.35 µV | 2.66 | 0.54 | [-12.53, -1.95] |
| 2 to 4 | 24 | -6.11 µV | 3.19 | 0.65 | [-15.66, 1.17] |
| 3 to 5 | 24 | -5.65 µV | 2.74 | 0.56 | [-13.75, -0.84] |
| 4 to 6 | 24 | -6.43 µV | 3.84 | 0.78 | [-16.09, 0.71] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 87.00 ms | 15.97 | 3.26 | [68.00, 108.00] |
| 2 to 4 | 24 | 94.00 ms | 14.64 | 2.99 | [68.00, 108.00] |
| 3 to 5 | 24 | 87.17 ms | 14.68 | 3.00 | [68.00, 108.00] |
| 4 to 6 | 24 | 90.00 ms | 15.69 | 3.20 | [68.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 1.74 µV | 2.35 | 0.48 | [-2.33, 7.47] |
| 2 to 4 | 24 | 2.66 µV | 1.90 | 0.39 | [-0.56, 7.11] |
| 3 to 5 | 24 | 1.88 µV | 2.49 | 0.51 | [-3.55, 6.32] |
| 4 to 6 | 24 | 2.38 µV | 2.77 | 0.57 | [-3.02, 7.49] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 454.00 ms | 38.75 | 7.91 | [388.00, 516.00] |
| 2 to 4 | 24 | 470.67 ms | 48.33 | 9.86 | [388.00, 536.00] |
| 3 to 5 | 24 | 469.33 ms | 54.57 | 11.14 | [388.00, 536.00] |
| 4 to 6 | 24 | 480.50 ms | 49.64 | 10.13 | [388.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 5.39 µV | 4.12 | 0.84 | [-1.55, 14.25] |
| 2 to 4 | 24 | 5.87 µV | 4.97 | 1.01 | [-4.11, 17.43] |
| 3 to 5 | 24 | 4.55 µV | 4.01 | 0.82 | [-3.15, 16.52] |
| 4 to 6 | 24 | 5.49 µV | 3.80 | 0.77 | [0.89, 12.37] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 825.62, BIC = 843.57
- **2 to 4 vs 1 to 3**: *β* = 0.49, *SE* = 4.812, *z* = 0.103, *p* = 0.918
- **3 to 5 vs 1 to 3**: *β* = 4.55, *SE* = 4.789, *z* = 0.951, *p* = 0.342
- **4 to 6 vs 1 to 3**: *β* = 3.90, *SE* = 4.791, *z* = 0.814, *p* = 0.416
- **SNR**: *β* = 0.45, *SE* = 1.378, *z* = 0.328, *p* = 0.743

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -0.50 | 4.81 | -0.10 | 0.918 | 0.988 | n.s. |
| 1 to 3 - 3 to 5 | -4.55 | 4.79 | -0.95 | 0.342 | 0.919 | n.s. |
| 1 to 3 - 4 to 6 | -3.90 | 4.79 | -0.81 | 0.416 | 0.921 | n.s. |
| 2 to 4 - 3 to 5 | -4.06 | 4.80 | -0.85 | 0.398 | 0.921 | n.s. |
| 2 to 4 - 4 to 6 | -3.41 | 4.80 | -0.71 | 0.478 | 0.921 | n.s. |
| 3 to 5 - 4 to 6 | 0.65 | 4.79 | 0.14 | 0.892 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.743, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.06 | 23 | = 0.952 | -0.02 [-0.43, 0.41] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.90 | 23 | = 0.861 | -0.28 [-0.61, 0.24] | small | n.s. |
| 1 to 3 vs 4 to 6 | -0.75 | 23 | = 0.861 | -0.22 [-0.58, 0.27] | small | n.s. |
| 2 to 4 vs 3 to 5 | -0.92 | 23 | = 0.861 | -0.25 [-0.61, 0.24] | small | n.s. |
| 2 to 4 vs 4 to 6 | -0.57 | 23 | = 0.861 | -0.20 [-0.54, 0.31] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 0.16 | 23 | = 0.952 | 0.04 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 438.68, BIC = 456.63
- **2 to 4 vs 1 to 3**: *β* = -1.74, *SE* = 0.630, *z* = -2.763, *p* = 0.006
- **3 to 5 vs 1 to 3**: *β* = -0.94, *SE* = 0.627, *z* = -1.506, *p* = 0.132
- **4 to 6 vs 1 to 3**: *β* = -1.52, *SE* = 0.627, *z* = -2.420, *p* = 0.016
- **SNR**: *β* = -0.01, *SE* = 0.174, *z* = -0.042, *p* = 0.966

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 1.74 | 0.63 | 2.76 | 0.006 | 0.034 | * |
| 1 to 3 - 3 to 5 | 0.94 | 0.63 | 1.51 | 0.132 | 0.433 | n.s. |
| 1 to 3 - 4 to 6 | 1.52 | 0.63 | 2.42 | 0.016 | 0.075 | n.s. |
| 2 to 4 - 3 to 5 | -0.80 | 0.63 | -1.27 | 0.205 | 0.498 | n.s. |
| 2 to 4 - 4 to 6 | -0.22 | 0.63 | -0.35 | 0.723 | 0.723 | n.s. |
| 3 to 5 - 4 to 6 | 0.57 | 0.63 | 0.92 | 0.360 | 0.590 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.94, *p* = 0.039, η²_G = 0.084
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | 2.99 | 23 | = 0.039 | 0.77 [0.15, 1.07] | medium | * |
| 1 to 3 vs 3 to 5 | 1.77 | 23 | = 0.181 | 0.40 [-0.08, 0.80] | small | n.s. |
| 1 to 3 vs 4 to 6 | 1.98 | 23 | = 0.180 | 0.63 [-0.04, 0.84] | medium | n.s. |
| 2 to 4 vs 3 to 5 | -1.21 | 23 | = 0.355 | -0.38 [-0.68, 0.18] | small | n.s. |
| 2 to 4 vs 4 to 6 | -0.36 | 23 | = 0.724 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 0.87 | 23 | = 0.475 | 0.25 [-0.25, 0.60] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 843.50, BIC = 861.45
- **2 to 4 vs 1 to 3**: *β* = 3.60, *SE* = 4.263, *z* = 0.845, *p* = 0.398
- **3 to 5 vs 1 to 3**: *β* = -3.03, *SE* = 4.269, *z* = -0.710, *p* = 0.478
- **4 to 6 vs 1 to 3**: *β* = -2.80, *SE* = 4.241, *z* = -0.660, *p* = 0.509
- **SNR**: *β* = 0.43, *SE* = 0.702, *z* = 0.619, *p* = 0.536

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -3.60 | 4.26 | -0.84 | 0.398 | 0.869 | n.s. |
| 1 to 3 - 3 to 5 | 3.03 | 4.27 | 0.71 | 0.478 | 0.869 | n.s. |
| 1 to 3 - 4 to 6 | 2.80 | 4.24 | 0.66 | 0.509 | 0.869 | n.s. |
| 2 to 4 - 3 to 5 | 6.63 | 4.24 | 1.56 | 0.118 | 0.529 | n.s. |
| 2 to 4 - 4 to 6 | 6.40 | 4.26 | 1.50 | 0.133 | 0.529 | n.s. |
| 3 to 5 - 4 to 6 | -0.23 | 4.26 | -0.05 | 0.957 | 0.957 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.404, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.72 | 23 | = 0.650 | -0.16 [-0.57, 0.28] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | 0.69 | 23 | = 0.650 | 0.14 [-0.28, 0.56] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | 0.62 | 23 | = 0.650 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.78 | 23 | = 0.262 | 0.31 [-0.07, 0.80] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.87 | 23 | = 0.262 | 0.32 [-0.06, 0.82] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.10 | 23 | = 0.920 | -0.02 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 438.07, BIC = 456.02
- **2 to 4 vs 1 to 3**: *β* = -0.11, *SE* = 0.530, *z* = -0.207, *p* = 0.836
- **3 to 5 vs 1 to 3**: *β* = 0.31, *SE* = 0.531, *z* = 0.581, *p* = 0.561
- **4 to 6 vs 1 to 3**: *β* = -0.12, *SE* = 0.528, *z* = -0.233, *p* = 0.815
- **SNR**: *β* = -0.58, *SE* = 0.083, *z* = -6.896, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.11 | 0.53 | 0.21 | 0.836 | 0.994 | n.s. |
| 1 to 3 - 3 to 5 | -0.31 | 0.53 | -0.58 | 0.561 | 0.963 | n.s. |
| 1 to 3 - 4 to 6 | 0.12 | 0.53 | 0.23 | 0.815 | 0.994 | n.s. |
| 2 to 4 - 3 to 5 | -0.42 | 0.53 | -0.79 | 0.428 | 0.960 | n.s. |
| 2 to 4 - 4 to 6 | 0.01 | 0.53 | 0.03 | 0.979 | 0.994 | n.s. |
| 3 to 5 - 4 to 6 | 0.43 | 0.53 | 0.81 | 0.416 | 0.960 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.58, *p* = 0.627, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.36 | 23 | = 0.868 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -1.60 | 23 | = 0.542 | -0.26 [-0.76, 0.11] | small | n.s. |
| 1 to 3 vs 4 to 6 | 0.12 | 23 | = 0.908 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -0.68 | 23 | = 0.868 | -0.16 [-0.56, 0.29] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 0.40 | 23 | = 0.868 | 0.09 [-0.34, 0.50] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 1.38 | 23 | = 0.542 | 0.24 [-0.15, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 805.23, BIC = 823.18
- **2 to 4 vs 1 to 3**: *β* = 7.08, *SE* = 4.281, *z* = 1.654, *p* = 0.098
- **3 to 5 vs 1 to 3**: *β* = 0.10, *SE* = 4.280, *z* = 0.023, *p* = 0.982
- **4 to 6 vs 1 to 3**: *β* = 2.77, *SE* = 4.299, *z* = 0.645, *p* = 0.519
- **SNR**: *β* = 0.69, *SE* = 1.271, *z* = 0.541, *p* = 0.589

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -7.08 | 4.28 | -1.65 | 0.098 | 0.462 | n.s. |
| 1 to 3 - 3 to 5 | -0.10 | 4.28 | -0.02 | 0.982 | 0.982 | n.s. |
| 1 to 3 - 4 to 6 | -2.77 | 4.30 | -0.64 | 0.519 | 0.889 | n.s. |
| 2 to 4 - 3 to 5 | 6.98 | 4.29 | 1.63 | 0.103 | 0.462 | n.s. |
| 2 to 4 - 4 to 6 | 4.31 | 4.32 | 1.00 | 0.318 | 0.784 | n.s. |
| 3 to 5 - 4 to 6 | -2.67 | 4.29 | -0.62 | 0.533 | 0.889 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.12, *p* = 0.345, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.51 | 23 | = 0.432 | -0.46 [-0.74, 0.12] | small | n.s. |
| 1 to 3 vs 3 to 5 | -0.04 | 23 | = 0.967 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.69 | 23 | = 0.679 | -0.19 [-0.56, 0.28] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.86 | 23 | = 0.432 | 0.47 [-0.06, 0.82] | small | n.s. |
| 2 to 4 vs 4 to 6 | 0.87 | 23 | = 0.679 | 0.26 [-0.25, 0.60] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.58 | 23 | = 0.679 | -0.19 [-0.54, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 446.25, BIC = 464.20
- **2 to 4 vs 1 to 3**: *β* = 0.88, *SE* = 0.641, *z* = 1.372, *p* = 0.170
- **3 to 5 vs 1 to 3**: *β* = 0.18, *SE* = 0.641, *z* = 0.275, *p* = 0.784
- **4 to 6 vs 1 to 3**: *β* = 0.75, *SE* = 0.644, *z* = 1.171, *p* = 0.242
- **SNR**: *β* = -0.35, *SE* = 0.194, *z* = -1.809, *p* = 0.070

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -0.88 | 0.64 | -1.37 | 0.170 | 0.673 | n.s. |
| 1 to 3 - 3 to 5 | -0.18 | 0.64 | -0.27 | 0.784 | 0.953 | n.s. |
| 1 to 3 - 4 to 6 | -0.75 | 0.64 | -1.17 | 0.242 | 0.749 | n.s. |
| 2 to 4 - 3 to 5 | 0.70 | 0.64 | 1.10 | 0.273 | 0.749 | n.s. |
| 2 to 4 - 4 to 6 | 0.13 | 0.65 | 0.19 | 0.846 | 0.953 | n.s. |
| 3 to 5 - 4 to 6 | -0.58 | 0.64 | -0.90 | 0.368 | 0.749 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.84, *p* = 0.479, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.67 | 23 | = 0.649 | -0.43 [-0.78, 0.09] | small | n.s. |
| 1 to 3 vs 3 to 5 | -0.22 | 23 | = 0.827 | -0.06 [-0.47, 0.38] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.82 | 23 | = 0.679 | -0.25 [-0.59, 0.26] | small | n.s. |
| 2 to 4 vs 3 to 5 | 1.23 | 23 | = 0.679 | 0.35 [-0.18, 0.68] | small | n.s. |
| 2 to 4 vs 4 to 6 | 0.40 | 23 | = 0.827 | 0.12 [-0.34, 0.50] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -0.76 | 23 | = 0.679 | -0.19 [-0.58, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1025.88, BIC = 1043.83
- **2 to 4 vs 1 to 3**: *β* = 16.65, *SE* = 13.240, *z* = 1.257, *p* = 0.209
- **3 to 5 vs 1 to 3**: *β* = 15.42, *SE* = 13.408, *z* = 1.150, *p* = 0.250
- **4 to 6 vs 1 to 3**: *β* = 26.53, *SE* = 13.256, *z* = 2.002, *p* = 0.045
- **SNR**: *β* = 0.07, *SE* = 1.675, *z* = 0.041, *p* = 0.968

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -16.65 | 13.24 | -1.26 | 0.209 | 0.690 | n.s. |
| 1 to 3 - 3 to 5 | -15.42 | 13.41 | -1.15 | 0.250 | 0.690 | n.s. |
| 1 to 3 - 4 to 6 | -26.53 | 13.26 | -2.00 | 0.045 | 0.243 | n.s. |
| 2 to 4 - 3 to 5 | 1.23 | 13.49 | 0.09 | 0.928 | 0.928 | n.s. |
| 2 to 4 - 4 to 6 | -9.88 | 13.29 | -0.74 | 0.457 | 0.788 | n.s. |
| 3 to 5 - 4 to 6 | -11.11 | 13.30 | -0.84 | 0.404 | 0.788 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.31, *p* = 0.278, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.48 | 23 | = 0.454 | -0.38 [-0.73, 0.13] | small | n.s. |
| 1 to 3 vs 3 to 5 | -1.06 | 23 | = 0.548 | -0.32 [-0.64, 0.21] | small | n.s. |
| 1 to 3 vs 4 to 6 | -1.91 | 23 | = 0.415 | -0.60 [-0.83, 0.05] | medium | n.s. |
| 2 to 4 vs 3 to 5 | 0.09 | 23 | = 0.932 | 0.03 [-0.40, 0.44] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | -0.76 | 23 | = 0.548 | -0.20 [-0.58, 0.27] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.87 | 23 | = 0.548 | -0.21 [-0.60, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 474.32, BIC = 492.27
- **2 to 4 vs 1 to 3**: *β* = 0.34, *SE* = 0.584, *z* = 0.580, *p* = 0.562
- **3 to 5 vs 1 to 3**: *β* = -0.16, *SE* = 0.595, *z* = -0.272, *p* = 0.785
- **4 to 6 vs 1 to 3**: *β* = 0.36, *SE* = 0.585, *z* = 0.608, *p* = 0.544
- **SNR**: *β* = 0.52, *SE* = 0.088, *z* = 5.902, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -0.34 | 0.58 | -0.58 | 0.562 | 0.957 | n.s. |
| 1 to 3 - 3 to 5 | 0.16 | 0.59 | 0.27 | 0.785 | 0.957 | n.s. |
| 1 to 3 - 4 to 6 | -0.36 | 0.59 | -0.61 | 0.544 | 0.957 | n.s. |
| 2 to 4 - 3 to 5 | 0.50 | 0.60 | 0.83 | 0.404 | 0.943 | n.s. |
| 2 to 4 - 4 to 6 | -0.02 | 0.59 | -0.03 | 0.977 | 0.977 | n.s. |
| 3 to 5 - 4 to 6 | -0.52 | 0.59 | -0.88 | 0.379 | 0.943 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.290, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.56 | 23 | = 0.728 | -0.11 [-0.54, 0.31] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | 1.14 | 23 | = 0.529 | 0.21 [-0.19, 0.66] | small | n.s. |
| 1 to 3 vs 4 to 6 | -0.19 | 23 | = 0.848 | -0.03 [-0.46, 0.38] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.89 | 23 | = 0.339 | 0.29 [-0.05, 0.82] | small | n.s. |
| 2 to 4 vs 4 to 6 | 0.52 | 23 | = 0.728 | 0.08 [-0.32, 0.53] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -1.65 | 23 | = 0.339 | -0.24 [-0.77, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.039). Post-hoc tests revealed:
  - 1 to 3 showed greater amplitude than 2 to 4 (*d* = 0.77)

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
