# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:11:35

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
| Decreasing 2 to 1 | 24 | 109.67 ms | 12.25 | 2.50 | [88.00, 120.00] |
| Decreasing 3 to 1 | 24 | 109.17 ms | 11.76 | 2.40 | [88.00, 120.00] |
| Increasing 1 to 2 | 24 | 101.17 ms | 13.05 | 2.66 | [88.00, 120.00] |
| Increasing 1 to 3 | 24 | 101.83 ms | 12.87 | 2.63 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | -1.95 µV | 2.17 | 0.44 | [-6.40, 3.32] |
| Decreasing 3 to 1 | 24 | -1.96 µV | 2.03 | 0.42 | [-6.48, 1.38] |
| Increasing 1 to 2 | 24 | -0.40 µV | 2.06 | 0.42 | [-3.35, 5.05] |
| Increasing 1 to 3 | 24 | -0.45 µV | 2.48 | 0.51 | [-5.86, 4.93] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 182.83 ms | 14.47 | 2.95 | [160.00, 212.00] |
| Decreasing 3 to 1 | 24 | 184.33 ms | 15.51 | 3.17 | [156.00, 212.00] |
| Increasing 1 to 2 | 24 | 172.50 ms | 18.85 | 3.85 | [148.00, 208.00] |
| Increasing 1 to 3 | 24 | 173.67 ms | 21.87 | 4.47 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | -3.58 µV | 3.34 | 0.68 | [-10.79, 2.16] |
| Decreasing 3 to 1 | 24 | -4.22 µV | 2.81 | 0.57 | [-10.41, -0.12] |
| Increasing 1 to 2 | 24 | -5.52 µV | 2.34 | 0.48 | [-9.87, -0.26] |
| Increasing 1 to 3 | 24 | -6.15 µV | 2.65 | 0.54 | [-12.30, -2.18] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 119.33 ms | 9.77 | 2.00 | [100.00, 128.00] |
| Decreasing 3 to 1 | 24 | 116.33 ms | 10.34 | 2.11 | [100.00, 128.00] |
| Increasing 1 to 2 | 24 | 112.67 ms | 11.78 | 2.40 | [100.00, 128.00] |
| Increasing 1 to 3 | 24 | 110.33 ms | 11.06 | 2.26 | [100.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 3.77 µV | 2.78 | 0.57 | [-1.05, 9.13] |
| Decreasing 3 to 1 | 24 | 3.42 µV | 2.27 | 0.46 | [-3.47, 9.14] |
| Increasing 1 to 2 | 24 | 0.52 µV | 2.03 | 0.41 | [-3.63, 3.14] |
| Increasing 1 to 3 | 24 | 0.95 µV | 2.85 | 0.58 | [-5.83, 7.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 490.17 ms | 36.32 | 7.41 | [416.00, 536.00] |
| Decreasing 3 to 1 | 24 | 483.67 ms | 31.91 | 6.51 | [416.00, 536.00] |
| Increasing 1 to 2 | 24 | 472.83 ms | 43.66 | 8.91 | [416.00, 536.00] |
| Increasing 1 to 3 | 24 | 467.17 ms | 38.09 | 7.78 | [416.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 5.36 µV | 3.39 | 0.69 | [-1.06, 11.08] |
| Decreasing 3 to 1 | 24 | 5.21 µV | 3.60 | 0.74 | [-1.29, 16.27] |
| Increasing 1 to 2 | 24 | 4.11 µV | 3.78 | 0.77 | [-3.51, 11.52] |
| Increasing 1 to 3 | 24 | 5.27 µV | 4.16 | 0.85 | [-1.55, 14.25] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 764.60, BIC = 782.55
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.82, *SE* = 3.312, *z* = -0.249, *p* = 0.804
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -8.78, *SE* = 3.305, *z* = -2.656, *p* = 0.008
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -7.77, *SE* = 3.287, *z* = -2.363, *p* = 0.018
- **SNR**: *β* = -0.62, *SE* = 0.797, *z* = -0.775, *p* = 0.439

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.82 | 3.31 | 0.25 | 0.804 | 0.942 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 8.78 | 3.30 | 2.66 | 0.008 | 0.046 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 7.77 | 3.29 | 2.36 | 0.018 | 0.075 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 7.96 | 3.29 | 2.42 | 0.015 | 0.075 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 6.94 | 3.32 | 2.09 | 0.037 | 0.106 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -1.01 | 3.32 | -0.31 | 0.760 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.70, *p* = 0.016, η²_G = 0.095
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.16 | 23 | = 0.877 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.39 | 23 | = 0.038 | 0.67 [0.04, 0.94] | medium | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.78 | 23 | = 0.038 | 0.62 [0.11, 1.02] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.44 | 23 | = 0.038 | 0.64 [0.05, 0.94] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.44 | 23 | = 0.038 | 0.59 [0.05, 0.95] | medium | * |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.16 | 23 | = 0.877 | -0.05 [-0.45, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 428.57, BIC = 446.52
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.00, *SE* = 0.561, *z* = -0.004, *p* = 0.997
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = 1.56, *SE* = 0.560, *z* = 2.783, *p* = 0.005
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = 1.50, *SE* = 0.557, *z* = 2.693, *p* = 0.007
- **SNR**: *β* = 0.01, *SE* = 0.138, *z* = 0.097, *p* = 0.922

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.00 | 0.56 | 0.00 | 0.997 | 0.997 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | -1.56 | 0.56 | -2.78 | 0.005 | 0.030 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | -1.50 | 0.56 | -2.69 | 0.007 | 0.030 | * |
| Decreasing 3 to 1 - Increasing 1 to 2 | -1.56 | 0.56 | -2.80 | 0.005 | 0.030 | * |
| Decreasing 3 to 1 - Increasing 1 to 3 | -1.50 | 0.56 | -2.67 | 0.008 | 0.030 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.06 | 0.56 | 0.11 | 0.916 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.84, *p* = 0.004, η²_G = 0.113
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.01 | 23 | = 0.988 | 0.00 [-0.42, 0.43] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | -2.42 | 23 | = 0.036 | -0.73 [-0.94, -0.05] | medium | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | -2.79 | 23 | = 0.021 | -0.64 [-1.03, -0.11] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | -3.27 | 23 | = 0.020 | -0.76 [-1.14, -0.20] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -2.84 | 23 | = 0.021 | -0.67 [-1.04, -0.12] | medium | * |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.09 | 23 | = 0.988 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 812.04, BIC = 829.99
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 1.64, *SE* = 3.704, *z* = 0.442, *p* = 0.659
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -10.65, *SE* = 3.760, *z* = -2.831, *p* = 0.005
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -9.77, *SE* = 3.943, *z* = -2.478, *p* = 0.013
- **SNR**: *β* = 0.29, *SE* = 0.659, *z* = 0.437, *p* = 0.662

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -1.64 | 3.70 | -0.44 | 0.659 | 0.883 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 10.65 | 3.76 | 2.83 | 0.005 | 0.023 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 9.77 | 3.94 | 2.48 | 0.013 | 0.039 | * |
| Decreasing 3 to 1 - Increasing 1 to 2 | 12.28 | 3.83 | 3.21 | 0.001 | 0.008 | ** |
| Decreasing 3 to 1 - Increasing 1 to 3 | 11.41 | 4.06 | 2.81 | 0.005 | 0.023 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.87 | 3.75 | -0.23 | 0.816 | 0.883 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.23, *p* = 0.003, η²_G = 0.083
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.57 | 23 | = 0.692 | -0.10 [-0.54, 0.31] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 3.04 | 23 | = 0.017 | 0.62 [0.16, 1.08] | medium | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.28 | 23 | = 0.048 | 0.49 [0.02, 0.91] | small | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 3.37 | 23 | = 0.016 | 0.69 [0.22, 1.16] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.66 | 23 | = 0.028 | 0.56 [0.09, 0.99] | medium | * |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.25 | 23 | = 0.808 | -0.06 [-0.47, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 426.69, BIC = 444.64
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.86, *SE* = 0.504, *z* = -1.708, *p* = 0.088
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -1.43, *SE* = 0.512, *z* = -2.795, *p* = 0.005
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -1.58, *SE* = 0.538, *z* = -2.933, *p* = 0.003
- **SNR**: *β* = -0.47, *SE* = 0.091, *z* = -5.154, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.86 | 0.50 | 1.71 | 0.088 | 0.307 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 1.43 | 0.51 | 2.79 | 0.005 | 0.026 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 1.58 | 0.54 | 2.93 | 0.003 | 0.020 | * |
| Decreasing 3 to 1 - Increasing 1 to 2 | 0.57 | 0.52 | 1.09 | 0.275 | 0.482 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.72 | 0.56 | 1.29 | 0.197 | 0.482 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.15 | 0.51 | 0.29 | 0.774 | 0.774 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.71, *p* < .001, η²_G = 0.121
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 1.13 | 23 | = 0.271 | 0.21 [-0.20, 0.66] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 3.54 | 23 | = 0.005 | 0.67 [0.25, 1.20] | medium | ** |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 4.16 | 23 | = 0.002 | 0.85 [0.36, 1.34] | large | ** |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.34 | 23 | = 0.042 | 0.50 [0.03, 0.92] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.98 | 23 | = 0.013 | 0.71 [0.15, 1.07] | medium | * |
| Increasing 1 to 2 vs Increasing 1 to 3 | 1.49 | 23 | = 0.179 | 0.25 [-0.13, 0.74] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 731.65, BIC = 749.60
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -2.97, *SE* = 2.662, *z* = -1.116, *p* = 0.264
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -6.61, *SE* = 2.712, *z* = -2.436, *p* = 0.015
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -8.97, *SE* = 2.657, *z* = -3.377, *p* = 0.001
- **SNR**: *β* = 0.04, *SE* = 0.405, *z* = 0.100, *p* = 0.920

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 2.97 | 2.66 | 1.12 | 0.264 | 0.459 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 6.61 | 2.71 | 2.44 | 0.015 | 0.072 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 8.97 | 2.66 | 3.38 | < .001 | 0.004 | ** |
| Decreasing 3 to 1 - Increasing 1 to 2 | 3.64 | 2.66 | 1.37 | 0.172 | 0.432 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 6.00 | 2.65 | 2.27 | 0.023 | 0.090 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 2.37 | 2.67 | 0.89 | 0.375 | 0.459 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.32, *p* = 0.008, η²_G = 0.096
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 1.20 | 23 | = 0.289 | 0.30 [-0.18, 0.67] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.27 | 23 | = 0.074 | 0.62 [0.02, 0.91] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 3.17 | 23 | = 0.026 | 0.86 [0.18, 1.11] | large | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.35 | 23 | = 0.284 | 0.33 [-0.15, 0.71] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.21 | 23 | = 0.074 | 0.56 [0.01, 0.89] | medium | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.94 | 23 | = 0.358 | 0.20 [-0.23, 0.62] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 434.10, BIC = 452.05
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.19, *SE* = 0.542, *z* = -0.357, *p* = 0.721
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -2.93, *SE* = 0.553, *z* = -5.295, *p* < .001
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -2.68, *SE* = 0.541, *z* = -4.955, *p* < .001
- **SNR**: *β* = 0.21, *SE* = 0.087, *z* = 2.462, *p* = 0.014

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.19 | 0.54 | 0.36 | 0.721 | 0.875 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 2.93 | 0.55 | 5.29 | < .001 | < .001 | *** |
| Decreasing 2 to 1 - Increasing 1 to 3 | 2.68 | 0.54 | 4.95 | < .001 | < .001 | *** |
| Decreasing 3 to 1 - Increasing 1 to 2 | 2.73 | 0.54 | 5.05 | < .001 | < .001 | *** |
| Decreasing 3 to 1 - Increasing 1 to 3 | 2.49 | 0.54 | 4.62 | < .001 | < .001 | *** |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.25 | 0.54 | -0.46 | 0.646 | 0.875 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 17.86, *p* < .001, η²_G = 0.256
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.62 | 23 | = 0.544 | 0.14 [-0.30, 0.55] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 5.65 | 23 | < .001 | 1.34 [0.61, 1.70] | large | *** |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 4.51 | 23 | < .001 | 1.00 [0.42, 1.43] | large | *** |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 5.65 | 23 | < .001 | 1.34 [0.61, 1.70] | large | *** |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 4.72 | 23 | < .001 | 0.96 [0.45, 1.47] | large | *** |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.81 | 23 | = 0.513 | -0.17 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 975.03, BIC = 992.98
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -5.73, *SE* = 9.770, *z* = -0.586, *p* = 0.558
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -17.41, *SE* = 9.612, *z* = -1.812, *p* = 0.070
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -22.76, *SE* = 9.626, *z* = -2.365, *p* = 0.018
- **SNR**: *β* = -0.36, *SE* = 0.831, *z* = -0.438, *p* = 0.661

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 5.73 | 9.77 | 0.59 | 0.558 | 0.804 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 17.41 | 9.61 | 1.81 | 0.070 | 0.304 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 22.76 | 9.63 | 2.36 | 0.018 | 0.103 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 11.68 | 9.81 | 1.19 | 0.233 | 0.549 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 17.03 | 9.69 | 1.76 | 0.079 | 0.304 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 5.35 | 9.64 | 0.55 | 0.579 | 0.804 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.23, *p* = 0.092, η²_G = 0.056
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.92 | 23 | = 0.442 | 0.19 [-0.24, 0.61] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.49 | 23 | = 0.298 | 0.43 [-0.13, 0.74] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.69 | 23 | = 0.078 | 0.62 [0.10, 1.00] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.02 | 23 | = 0.442 | 0.28 [-0.22, 0.64] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.87 | 23 | = 0.221 | 0.47 [-0.05, 0.82] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.49 | 23 | = 0.626 | 0.14 [-0.32, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 487.62, BIC = 505.57
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.65, *SE* = 0.678, *z* = -0.956, *p* = 0.339
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -1.20, *SE* = 0.665, *z* = -1.806, *p* = 0.071
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.24, *SE* = 0.666, *z* = -0.368, *p* = 0.713
- **SNR**: *β* = 0.24, *SE* = 0.063, *z* = 3.755, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.65 | 0.68 | 0.96 | 0.339 | 0.809 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 1.20 | 0.66 | 1.81 | 0.071 | 0.357 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.24 | 0.67 | 0.37 | 0.713 | 0.809 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 0.55 | 0.68 | 0.81 | 0.418 | 0.809 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.40 | 0.67 | -0.60 | 0.548 | 0.809 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.96 | 0.67 | -1.43 | 0.152 | 0.561 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.269, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.22 | 23 | = 0.942 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.74 | 23 | = 0.288 | 0.35 [-0.08, 0.79] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 0.12 | 23 | = 0.942 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.49 | 23 | = 0.300 | 0.30 [-0.13, 0.74] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.07 | 23 | = 0.942 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.79 | 23 | = 0.288 | -0.29 [-0.80, 0.07] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.016). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.67)
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.62)
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.64)
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.59)
**Fz amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed smaller amplitude than Increasing 1 to 2 (*d* = -0.73)
  - Decreasing 2 to 1 showed smaller amplitude than Increasing 1 to 3 (*d* = -0.64)
  - Decreasing 3 to 1 showed smaller amplitude than Increasing 1 to 2 (*d* = -0.76)
  - Decreasing 3 to 1 showed smaller amplitude than Increasing 1 to 3 (*d* = -0.67)
**N1 latency:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.62)
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.49)
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.69)
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.56)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 0.67)
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 0.85)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 0.50)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 0.71)
**P1 latency:** Significant main effect of condition (*p* = 0.008). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.86)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 1.34)
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 1.00)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 1.34)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 0.96)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.092)

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
