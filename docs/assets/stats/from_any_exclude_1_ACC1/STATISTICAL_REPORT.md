# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:22:28

---

## 1. Analysis Overview

**Total Measurements:** 480
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| from 2 | 24 | 102.50 ms | 7.98 | 1.63 | [92.00, 112.00] |
| from 3 | 24 | 102.17 ms | 8.17 | 1.67 | [92.00, 112.00] |
| from 4 | 24 | 104.17 ms | 7.60 | 1.55 | [92.00, 112.00] |
| from 5 | 24 | 102.83 ms | 7.78 | 1.59 | [92.00, 112.00] |
| from 6 | 24 | 104.67 ms | 7.24 | 1.48 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | -1.13 µV | 1.36 | 0.28 | [-4.46, 1.18] |
| from 3 | 24 | -1.18 µV | 1.23 | 0.25 | [-3.47, 0.72] |
| from 4 | 24 | -0.79 µV | 1.69 | 0.35 | [-4.85, 2.56] |
| from 5 | 24 | -1.92 µV | 1.41 | 0.29 | [-6.01, 0.69] |
| from 6 | 24 | -1.66 µV | 1.52 | 0.31 | [-6.83, 0.43] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 170.33 ms | 18.87 | 3.85 | [140.00, 208.00] |
| from 3 | 24 | 170.67 ms | 20.35 | 4.15 | [140.00, 208.00] |
| from 4 | 24 | 172.17 ms | 18.02 | 3.68 | [140.00, 208.00] |
| from 5 | 24 | 169.83 ms | 15.96 | 3.26 | [140.00, 208.00] |
| from 6 | 24 | 173.50 ms | 17.37 | 3.55 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | -5.39 µV | 2.12 | 0.43 | [-10.28, -0.17] |
| from 3 | 24 | -5.45 µV | 2.09 | 0.43 | [-9.91, -1.86] |
| from 4 | 24 | -5.72 µV | 2.56 | 0.52 | [-12.11, -2.09] |
| from 5 | 24 | -5.74 µV | 2.28 | 0.46 | [-9.50, -1.21] |
| from 6 | 24 | -5.96 µV | 2.12 | 0.43 | [-10.13, -3.03] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 103.33 ms | 7.43 | 1.52 | [96.00, 116.00] |
| from 3 | 24 | 105.33 ms | 7.88 | 1.61 | [96.00, 116.00] |
| from 4 | 24 | 106.50 ms | 7.63 | 1.56 | [96.00, 116.00] |
| from 5 | 24 | 107.83 ms | 8.04 | 1.64 | [96.00, 116.00] |
| from 6 | 24 | 108.33 ms | 8.58 | 1.75 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 1.13 µV | 1.69 | 0.35 | [-2.39, 5.24] |
| from 3 | 24 | 0.82 µV | 1.84 | 0.38 | [-1.59, 6.01] |
| from 4 | 24 | 0.66 µV | 1.98 | 0.40 | [-2.85, 3.65] |
| from 5 | 24 | 1.46 µV | 1.88 | 0.38 | [-3.12, 4.48] |
| from 6 | 24 | 1.60 µV | 2.20 | 0.45 | [-2.13, 7.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 475.33 ms | 38.14 | 7.79 | [428.00, 536.00] |
| from 3 | 24 | 485.67 ms | 33.98 | 6.94 | [432.00, 536.00] |
| from 4 | 24 | 483.33 ms | 33.21 | 6.78 | [428.00, 536.00] |
| from 5 | 24 | 483.83 ms | 30.27 | 6.18 | [432.00, 536.00] |
| from 6 | 24 | 480.50 ms | 35.25 | 7.20 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 4.09 µV | 3.33 | 0.68 | [-2.96, 10.63] |
| from 3 | 24 | 3.50 µV | 3.55 | 0.72 | [-3.39, 10.28] |
| from 4 | 24 | 3.93 µV | 3.30 | 0.67 | [-1.81, 9.14] |
| from 5 | 24 | 3.72 µV | 3.20 | 0.65 | [-2.34, 10.98] |
| from 6 | 24 | 3.81 µV | 3.24 | 0.66 | [-3.08, 9.98] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 789.38, BIC = 811.68
- **from 3 vs from 2**: *β* = -0.41, *SE* = 1.440, *z* = -0.284, *p* = 0.777
- **from 4 vs from 2**: *β* = 1.57, *SE* = 1.447, *z* = 1.087, *p* = 0.277
- **from 5 vs from 2**: *β* = 0.14, *SE* = 1.502, *z* = 0.096, *p* = 0.923
- **from 6 vs from 2**: *β* = 2.14, *SE* = 1.430, *z* = 1.493, *p* = 0.135
- **SNR**: *β* = 0.13, *SE* = 0.331, *z* = 0.406, *p* = 0.685

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.41 | 1.44 | 0.28 | 0.777 | 0.991 | n.s. |
| from 2 - from 4 | -1.57 | 1.45 | -1.09 | 0.277 | 0.857 | n.s. |
| from 2 - from 5 | -0.14 | 1.50 | -0.10 | 0.923 | 0.991 | n.s. |
| from 2 - from 6 | -2.14 | 1.43 | -1.49 | 0.135 | 0.730 | n.s. |
| from 3 - from 4 | -1.98 | 1.43 | -1.39 | 0.166 | 0.765 | n.s. |
| from 3 - from 5 | -0.55 | 1.46 | -0.38 | 0.704 | 0.991 | n.s. |
| from 3 - from 6 | -2.54 | 1.43 | -1.78 | 0.076 | 0.545 | n.s. |
| from 4 - from 5 | 1.43 | 1.45 | 0.99 | 0.324 | 0.859 | n.s. |
| from 4 - from 6 | -0.56 | 1.44 | -0.39 | 0.695 | 0.991 | n.s. |
| from 5 - from 6 | -1.99 | 1.48 | -1.35 | 0.179 | 0.765 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.12, *p* = 0.353, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.19 | 23 | = 0.848 | 0.04 [-0.38, 0.46] | negligible | n.s. |
| from 2 vs from 4 | -1.07 | 23 | = 0.493 | -0.21 [-0.65, 0.21] | small | n.s. |
| from 2 vs from 5 | -0.20 | 23 | = 0.848 | -0.04 [-0.46, 0.38] | negligible | n.s. |
| from 2 vs from 6 | -1.48 | 23 | = 0.381 | -0.28 [-0.73, 0.13] | small | n.s. |
| from 3 vs from 4 | -1.49 | 23 | = 0.381 | -0.25 [-0.74, 0.13] | small | n.s. |
| from 3 vs from 5 | -0.42 | 23 | = 0.848 | -0.08 [-0.51, 0.34] | negligible | n.s. |
| from 3 vs from 6 | -1.65 | 23 | = 0.381 | -0.32 [-0.77, 0.10] | small | n.s. |
| from 4 vs from 5 | 1.14 | 23 | = 0.493 | 0.17 [-0.20, 0.66] | negligible | n.s. |
| from 4 vs from 6 | -0.37 | 23 | = 0.848 | -0.07 [-0.50, 0.35] | negligible | n.s. |
| from 5 vs from 6 | -1.66 | 23 | = 0.381 | -0.24 [-0.77, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 376.70, BIC = 399.00
- **from 3 vs from 2**: *β* = 0.11, *SE* = 0.270, *z* = 0.414, *p* = 0.679
- **from 4 vs from 2**: *β* = 0.54, *SE* = 0.271, *z* = 1.984, *p* = 0.047
- **from 5 vs from 2**: *β* = -0.39, *SE* = 0.282, *z* = -1.371, *p* = 0.171
- **from 6 vs from 2**: *β* = -0.46, *SE* = 0.268, *z* = -1.726, *p* = 0.084
- **SNR**: *β* = -0.28, *SE* = 0.063, *z* = -4.509, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.11 | 0.27 | -0.41 | 0.679 | 0.897 | n.s. |
| from 2 - from 4 | -0.54 | 0.27 | -1.98 | 0.047 | 0.287 | n.s. |
| from 2 - from 5 | 0.39 | 0.28 | 1.37 | 0.171 | 0.429 | n.s. |
| from 2 - from 6 | 0.46 | 0.27 | 1.73 | 0.084 | 0.356 | n.s. |
| from 3 - from 4 | -0.43 | 0.27 | -1.59 | 0.111 | 0.376 | n.s. |
| from 3 - from 5 | 0.50 | 0.27 | 1.83 | 0.068 | 0.345 | n.s. |
| from 3 - from 6 | 0.57 | 0.27 | 2.14 | 0.032 | 0.232 | n.s. |
| from 4 - from 5 | 0.92 | 0.27 | 3.41 | < .001 | 0.006 | ** |
| from 4 - from 6 | 1.00 | 0.27 | 3.72 | < .001 | 0.002 | ** |
| from 5 - from 6 | 0.08 | 0.28 | 0.27 | 0.784 | 0.897 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.83, *p* = 0.001, η²_G = 0.074
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.17 | 23 | = 0.868 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| from 2 vs from 4 | -0.93 | 23 | = 0.404 | -0.22 [-0.62, 0.24] | small | n.s. |
| from 2 vs from 5 | 2.86 | 23 | = 0.030 | 0.57 [0.13, 1.04] | medium | * |
| from 2 vs from 6 | 1.75 | 23 | = 0.155 | 0.37 [-0.08, 0.79] | small | n.s. |
| from 3 vs from 4 | -1.36 | 23 | = 0.266 | -0.26 [-0.71, 0.15] | small | n.s. |
| from 3 vs from 5 | 2.91 | 23 | = 0.030 | 0.56 [0.14, 1.05] | medium | * |
| from 3 vs from 6 | 2.19 | 23 | = 0.078 | 0.35 [0.00, 0.89] | small | n.s. |
| from 4 vs from 5 | 3.61 | 23 | = 0.015 | 0.72 [0.26, 1.21] | medium | * |
| from 4 vs from 6 | 2.67 | 23 | = 0.034 | 0.54 [0.09, 1.00] | medium | * |
| from 5 vs from 6 | -1.08 | 23 | = 0.366 | -0.18 [-0.65, 0.21] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 958.70, BIC = 981.00
- **from 3 vs from 2**: *β* = -0.80, *SE* = 2.727, *z* = -0.293, *p* = 0.770
- **from 4 vs from 2**: *β* = 1.35, *SE* = 2.704, *z* = 0.498, *p* = 0.618
- **from 5 vs from 2**: *β* = -1.45, *SE* = 2.718, *z* = -0.532, *p* = 0.595
- **from 6 vs from 2**: *β* = 2.92, *SE* = 2.700, *z* = 1.080, *p* = 0.280
- **SNR**: *β* = 0.88, *SE* = 0.302, *z* = 2.913, *p* = 0.004

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.80 | 2.73 | 0.29 | 0.770 | 0.984 | n.s. |
| from 2 - from 4 | -1.35 | 2.70 | -0.50 | 0.618 | 0.984 | n.s. |
| from 2 - from 5 | 1.45 | 2.72 | 0.53 | 0.595 | 0.984 | n.s. |
| from 2 - from 6 | -2.92 | 2.70 | -1.08 | 0.280 | 0.928 | n.s. |
| from 3 - from 4 | -2.15 | 2.71 | -0.79 | 0.428 | 0.965 | n.s. |
| from 3 - from 5 | 0.65 | 2.70 | 0.24 | 0.810 | 0.984 | n.s. |
| from 3 - from 6 | -3.71 | 2.72 | -1.37 | 0.172 | 0.816 | n.s. |
| from 4 - from 5 | 2.79 | 2.70 | 1.03 | 0.301 | 0.928 | n.s. |
| from 4 - from 6 | -1.57 | 2.70 | -0.58 | 0.561 | 0.984 | n.s. |
| from 5 - from 6 | -4.36 | 2.71 | -1.61 | 0.107 | 0.679 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.53, *p* = 0.712, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.629 (ε = 0.625)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.12 | 23 | = 0.903 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| from 2 vs from 4 | -0.84 | 23 | = 0.787 | -0.10 [-0.60, 0.25] | negligible | n.s. |
| from 2 vs from 5 | 0.14 | 23 | = 0.903 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| from 2 vs from 6 | -0.99 | 23 | = 0.787 | -0.17 [-0.63, 0.22] | negligible | n.s. |
| from 3 vs from 4 | -0.74 | 23 | = 0.787 | -0.08 [-0.58, 0.27] | negligible | n.s. |
| from 3 vs from 5 | 0.22 | 23 | = 0.903 | 0.05 [-0.38, 0.47] | negligible | n.s. |
| from 3 vs from 6 | -0.96 | 23 | = 0.787 | -0.15 [-0.62, 0.23] | negligible | n.s. |
| from 4 vs from 5 | 0.73 | 23 | = 0.787 | 0.14 [-0.28, 0.57] | negligible | n.s. |
| from 4 vs from 6 | -0.45 | 23 | = 0.903 | -0.08 [-0.52, 0.33] | negligible | n.s. |
| from 5 vs from 6 | -1.77 | 23 | = 0.787 | -0.22 [-0.80, 0.07] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 416.46, BIC = 438.76
- **from 3 vs from 2**: *β* = 0.19, *SE* = 0.288, *z* = 0.646, *p* = 0.519
- **from 4 vs from 2**: *β* = -0.23, *SE* = 0.285, *z* = -0.790, *p* = 0.430
- **from 5 vs from 2**: *β* = -0.15, *SE* = 0.287, *z* = -0.521, *p* = 0.602
- **from 6 vs from 2**: *β* = -0.52, *SE* = 0.285, *z* = -1.827, *p* = 0.068
- **SNR**: *β* = -0.19, *SE* = 0.032, *z* = -6.113, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.19 | 0.29 | -0.65 | 0.519 | 0.894 | n.s. |
| from 2 - from 4 | 0.23 | 0.29 | 0.79 | 0.430 | 0.894 | n.s. |
| from 2 - from 5 | 0.15 | 0.29 | 0.52 | 0.602 | 0.894 | n.s. |
| from 2 - from 6 | 0.52 | 0.28 | 1.83 | 0.068 | 0.468 | n.s. |
| from 3 - from 4 | 0.41 | 0.29 | 1.44 | 0.150 | 0.728 | n.s. |
| from 3 - from 5 | 0.34 | 0.28 | 1.18 | 0.239 | 0.806 | n.s. |
| from 3 - from 6 | 0.71 | 0.29 | 2.46 | 0.014 | 0.129 | n.s. |
| from 4 - from 5 | -0.08 | 0.29 | -0.27 | 0.790 | 0.894 | n.s. |
| from 4 - from 6 | 0.30 | 0.28 | 1.04 | 0.300 | 0.832 | n.s. |
| from 5 - from 6 | 0.37 | 0.29 | 1.30 | 0.194 | 0.779 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.410, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.20 | 23 | = 0.938 | 0.03 [-0.38, 0.46] | negligible | n.s. |
| from 2 vs from 4 | 0.80 | 23 | = 0.668 | 0.14 [-0.26, 0.59] | negligible | n.s. |
| from 2 vs from 5 | 1.18 | 23 | = 0.622 | 0.16 [-0.19, 0.67] | negligible | n.s. |
| from 2 vs from 6 | 1.61 | 23 | = 0.601 | 0.27 [-0.10, 0.76] | small | n.s. |
| from 3 vs from 4 | 0.90 | 23 | = 0.668 | 0.12 [-0.24, 0.61] | negligible | n.s. |
| from 3 vs from 5 | 1.21 | 23 | = 0.622 | 0.13 [-0.18, 0.67] | negligible | n.s. |
| from 3 vs from 6 | 1.73 | 23 | = 0.601 | 0.24 [-0.08, 0.79] | small | n.s. |
| from 4 vs from 5 | 0.07 | 23 | = 0.945 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| from 4 vs from 6 | 0.62 | 23 | = 0.677 | 0.10 [-0.30, 0.55] | negligible | n.s. |
| from 5 vs from 6 | 0.74 | 23 | = 0.668 | 0.10 [-0.27, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 809.07, BIC = 831.37
- **from 3 vs from 2**: *β* = 1.72, *SE* = 1.613, *z* = 1.064, *p* = 0.287
- **from 4 vs from 2**: *β* = 2.88, *SE* = 1.613, *z* = 1.788, *p* = 0.074
- **from 5 vs from 2**: *β* = 4.28, *SE* = 1.606, *z* = 2.667, *p* = 0.008
- **from 6 vs from 2**: *β* = 4.90, *SE* = 1.599, *z* = 3.063, *p* = 0.002
- **SNR**: *β* = 0.46, *SE* = 0.371, *z* = 1.229, *p* = 0.219

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -1.72 | 1.61 | -1.06 | 0.287 | 0.742 | n.s. |
| from 2 - from 4 | -2.88 | 1.61 | -1.79 | 0.074 | 0.415 | n.s. |
| from 2 - from 5 | -4.28 | 1.61 | -2.67 | 0.008 | 0.067 | n.s. |
| from 2 - from 6 | -4.90 | 1.60 | -3.06 | 0.002 | 0.022 | * |
| from 3 - from 4 | -1.17 | 1.60 | -0.73 | 0.465 | 0.763 | n.s. |
| from 3 - from 5 | -2.57 | 1.60 | -1.61 | 0.108 | 0.497 | n.s. |
| from 3 - from 6 | -3.18 | 1.60 | -1.98 | 0.047 | 0.321 | n.s. |
| from 4 - from 5 | -1.40 | 1.60 | -0.88 | 0.381 | 0.763 | n.s. |
| from 4 - from 6 | -2.01 | 1.60 | -1.26 | 0.209 | 0.691 | n.s. |
| from 5 - from 6 | -0.61 | 1.60 | -0.38 | 0.701 | 0.763 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.01, *p* = 0.022, η²_G = 0.051
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -1.05 | 23 | = 0.410 | -0.26 [-0.64, 0.21] | small | n.s. |
| from 2 vs from 4 | -1.64 | 23 | = 0.267 | -0.42 [-0.77, 0.10] | small | n.s. |
| from 2 vs from 5 | -2.63 | 23 | = 0.074 | -0.58 [-0.99, -0.09] | medium | n.s. |
| from 2 vs from 6 | -3.02 | 23 | = 0.061 | -0.62 [-1.08, -0.16] | medium | n.s. |
| from 3 vs from 4 | -0.81 | 23 | = 0.471 | -0.15 [-0.59, 0.26] | negligible | n.s. |
| from 3 vs from 5 | -1.44 | 23 | = 0.271 | -0.31 [-0.73, 0.14] | small | n.s. |
| from 3 vs from 6 | -1.59 | 23 | = 0.267 | -0.36 [-0.76, 0.11] | small | n.s. |
| from 4 vs from 5 | -1.00 | 23 | = 0.410 | -0.17 [-0.63, 0.22] | negligible | n.s. |
| from 4 vs from 6 | -1.55 | 23 | = 0.267 | -0.23 [-0.75, 0.12] | small | n.s. |
| from 5 vs from 6 | -0.33 | 23 | = 0.743 | -0.06 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 429.66, BIC = 451.96
- **from 3 vs from 2**: *β* = -0.42, *SE* = 0.316, *z* = -1.330, *p* = 0.184
- **from 4 vs from 2**: *β* = -0.58, *SE* = 0.316, *z* = -1.842, *p* = 0.066
- **from 5 vs from 2**: *β* = 0.25, *SE* = 0.314, *z* = 0.792, *p* = 0.428
- **from 6 vs from 2**: *β* = 0.44, *SE* = 0.312, *z* = 1.397, *p* = 0.162
- **SNR**: *β* = 0.18, *SE* = 0.076, *z* = 2.366, *p* = 0.018

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.42 | 0.32 | 1.33 | 0.184 | 0.588 | n.s. |
| from 2 - from 4 | 0.58 | 0.32 | 1.84 | 0.066 | 0.334 | n.s. |
| from 2 - from 5 | -0.25 | 0.31 | -0.79 | 0.428 | 0.813 | n.s. |
| from 2 - from 6 | -0.44 | 0.31 | -1.40 | 0.162 | 0.588 | n.s. |
| from 3 - from 4 | 0.16 | 0.31 | 0.52 | 0.605 | 0.813 | n.s. |
| from 3 - from 5 | -0.67 | 0.31 | -2.14 | 0.032 | 0.205 | n.s. |
| from 3 - from 6 | -0.86 | 0.31 | -2.73 | 0.006 | 0.055 | n.s. |
| from 4 - from 5 | -0.83 | 0.31 | -2.66 | 0.008 | 0.061 | n.s. |
| from 4 - from 6 | -1.02 | 0.31 | -3.25 | 0.001 | 0.012 | * |
| from 5 - from 6 | -0.19 | 0.31 | -0.60 | 0.548 | 0.813 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.15, *p* = 0.018, η²_G = 0.035
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 1.17 | 23 | = 0.319 | 0.17 [-0.19, 0.67] | negligible | n.s. |
| from 2 vs from 4 | 1.33 | 23 | = 0.319 | 0.25 [-0.16, 0.70] | small | n.s. |
| from 2 vs from 5 | -1.19 | 23 | = 0.319 | -0.19 [-0.67, 0.18] | negligible | n.s. |
| from 2 vs from 6 | -1.67 | 23 | = 0.219 | -0.24 [-0.77, 0.09] | small | n.s. |
| from 3 vs from 4 | 0.65 | 23 | = 0.582 | 0.08 [-0.29, 0.56] | negligible | n.s. |
| from 3 vs from 5 | -1.82 | 23 | = 0.203 | -0.34 [-0.81, 0.06] | small | n.s. |
| from 3 vs from 6 | -2.91 | 23 | = 0.079 | -0.39 [-1.05, -0.14] | small | n.s. |
| from 4 vs from 5 | -2.01 | 23 | = 0.187 | -0.42 [-0.85, 0.03] | small | n.s. |
| from 4 vs from 6 | -2.43 | 23 | = 0.117 | -0.45 [-0.94, -0.05] | small | n.s. |
| from 5 vs from 6 | -0.42 | 23 | = 0.676 | -0.07 [-0.51, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1175.02, BIC = 1197.32
- **from 3 vs from 2**: *β* = 10.37, *SE* = 7.630, *z* = 1.359, *p* = 0.174
- **from 4 vs from 2**: *β* = 8.05, *SE* = 7.675, *z* = 1.049, *p* = 0.294
- **from 5 vs from 2**: *β* = 8.54, *SE* = 7.627, *z* = 1.119, *p* = 0.263
- **from 6 vs from 2**: *β* = 5.20, *SE* = 7.622, *z* = 0.682, *p* = 0.495
- **SNR**: *β* = -0.03, *SE* = 0.646, *z* = -0.042, *p* = 0.966

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -10.37 | 7.63 | -1.36 | 0.174 | 0.852 | n.s. |
| from 2 - from 4 | -8.05 | 7.68 | -1.05 | 0.294 | 0.938 | n.s. |
| from 2 - from 5 | -8.54 | 7.63 | -1.12 | 0.263 | 0.936 | n.s. |
| from 2 - from 6 | -5.20 | 7.62 | -0.68 | 0.495 | 0.992 | n.s. |
| from 3 - from 4 | 2.32 | 7.58 | 0.31 | 0.760 | 0.995 | n.s. |
| from 3 - from 5 | 1.83 | 7.58 | 0.24 | 0.809 | 0.995 | n.s. |
| from 3 - from 6 | 5.17 | 7.58 | 0.68 | 0.495 | 0.992 | n.s. |
| from 4 - from 5 | -0.48 | 7.59 | -0.06 | 0.949 | 0.995 | n.s. |
| from 4 - from 6 | 2.85 | 7.59 | 0.38 | 0.707 | 0.995 | n.s. |
| from 5 - from 6 | 3.34 | 7.58 | 0.44 | 0.660 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.705, η²_G = 0.011
- Greenhouse-Geisser corrected: *p* = 0.632 (ε = 0.658)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -1.04 | 23 | = 0.877 | -0.29 [-0.64, 0.22] | small | n.s. |
| from 2 vs from 4 | -0.95 | 23 | = 0.877 | -0.22 [-0.62, 0.23] | small | n.s. |
| from 2 vs from 5 | -1.32 | 23 | = 0.877 | -0.25 [-0.70, 0.16] | small | n.s. |
| from 2 vs from 6 | -1.17 | 23 | = 0.877 | -0.14 [-0.67, 0.19] | negligible | n.s. |
| from 3 vs from 4 | 0.30 | 23 | = 0.906 | 0.07 [-0.36, 0.48] | negligible | n.s. |
| from 3 vs from 5 | 0.24 | 23 | = 0.906 | 0.06 [-0.37, 0.47] | negligible | n.s. |
| from 3 vs from 6 | 0.55 | 23 | = 0.906 | 0.15 [-0.31, 0.53] | negligible | n.s. |
| from 4 vs from 5 | -0.08 | 23 | = 0.936 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| from 4 vs from 6 | 0.34 | 23 | = 0.906 | 0.08 [-0.35, 0.49] | negligible | n.s. |
| from 5 vs from 6 | 0.48 | 23 | = 0.906 | 0.10 [-0.33, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 483.19, BIC = 505.49
- **from 3 vs from 2**: *β* = -0.77, *SE* = 0.356, *z* = -2.167, *p* = 0.030
- **from 4 vs from 2**: *β* = -0.41, *SE* = 0.358, *z* = -1.153, *p* = 0.249
- **from 5 vs from 2**: *β* = -0.54, *SE* = 0.356, *z* = -1.520, *p* = 0.128
- **from 6 vs from 2**: *β* = -0.44, *SE* = 0.355, *z* = -1.245, *p* = 0.213
- **SNR**: *β* = 0.13, *SE* = 0.033, *z* = 4.016, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.77 | 0.36 | 2.17 | 0.030 | 0.264 | n.s. |
| from 2 - from 4 | 0.41 | 0.36 | 1.15 | 0.249 | 0.865 | n.s. |
| from 2 - from 5 | 0.54 | 0.36 | 1.52 | 0.128 | 0.710 | n.s. |
| from 2 - from 6 | 0.44 | 0.36 | 1.24 | 0.213 | 0.853 | n.s. |
| from 3 - from 4 | -0.36 | 0.35 | -1.01 | 0.311 | 0.893 | n.s. |
| from 3 - from 5 | -0.23 | 0.35 | -0.65 | 0.514 | 0.944 | n.s. |
| from 3 - from 6 | -0.33 | 0.35 | -0.93 | 0.351 | 0.893 | n.s. |
| from 4 - from 5 | 0.13 | 0.35 | 0.36 | 0.719 | 0.978 | n.s. |
| from 4 - from 6 | 0.03 | 0.35 | 0.08 | 0.935 | 0.978 | n.s. |
| from 5 - from 6 | -0.10 | 0.35 | -0.28 | 0.780 | 0.978 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.66, *p* = 0.623, η²_G = 0.004
- Greenhouse-Geisser corrected: *p* = 0.575 (ε = 0.720)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 1.69 | 23 | = 0.569 | 0.17 [-0.09, 0.78] | negligible | n.s. |
| from 2 vs from 4 | 0.48 | 23 | = 0.797 | 0.05 [-0.33, 0.52] | negligible | n.s. |
| from 2 vs from 5 | 1.27 | 23 | = 0.726 | 0.11 [-0.17, 0.69] | negligible | n.s. |
| from 2 vs from 6 | 0.60 | 23 | = 0.797 | 0.08 [-0.30, 0.55] | negligible | n.s. |
| from 3 vs from 4 | -1.64 | 23 | = 0.569 | -0.12 [-0.77, 0.10] | negligible | n.s. |
| from 3 vs from 5 | -0.67 | 23 | = 0.797 | -0.07 [-0.56, 0.29] | negligible | n.s. |
| from 3 vs from 6 | -0.64 | 23 | = 0.797 | -0.09 [-0.55, 0.29] | negligible | n.s. |
| from 4 vs from 5 | 0.51 | 23 | = 0.797 | 0.06 [-0.32, 0.53] | negligible | n.s. |
| from 4 vs from 6 | 0.24 | 23 | = 0.825 | 0.03 [-0.37, 0.47] | negligible | n.s. |
| from 5 vs from 6 | -0.22 | 23 | = 0.825 | -0.03 [-0.47, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - from 2 showed greater amplitude than from 5 (*d* = 0.57)
  - from 3 showed greater amplitude than from 5 (*d* = 0.56)
  - from 4 showed greater amplitude than from 5 (*d* = 0.72)
  - from 4 showed greater amplitude than from 6 (*d* = 0.54)
**P1 latency:** Significant main effect of condition (*p* = 0.022) (no significant pairwise comparisons)
**P1 amplitude:** Significant main effect of condition (*p* = 0.018) (no significant pairwise comparisons)

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
