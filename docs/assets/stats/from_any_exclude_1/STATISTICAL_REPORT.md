# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:37:20

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
| from 2 | 9 | 107.56 ms | 7.33 | 2.44 | [92.00, 112.00] |
| from 3 | 11 | 100.36 ms | 9.54 | 2.88 | [92.00, 112.00] |
| from 4 | 9 | 100.89 ms | 8.89 | 2.96 | [92.00, 112.00] |
| from 5 | 4 | 102.00 ms | 11.55 | 5.77 | [92.00, 112.00] |
| from 6 | 9 | 100.89 ms | 10.54 | 3.51 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 9 | 1.19 µV | 0.76 | 0.25 | [0.38, 2.94] |
| from 3 | 11 | 1.31 µV | 0.89 | 0.27 | [0.10, 3.01] |
| from 4 | 9 | 1.57 µV | 0.82 | 0.27 | [0.73, 3.35] |
| from 5 | 4 | 1.86 µV | 0.77 | 0.38 | [1.22, 2.98] |
| from 6 | 9 | 1.12 µV | 0.64 | 0.21 | [0.23, 2.32] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 169.17 ms | 17.31 | 3.53 | [140.00, 204.00] |
| from 3 | 23 | 169.57 ms | 18.75 | 3.91 | [140.00, 204.00] |
| from 4 | 23 | 170.43 ms | 18.00 | 3.75 | [140.00, 204.00] |
| from 5 | 23 | 173.22 ms | 13.98 | 2.92 | [144.00, 196.00] |
| from 6 | 24 | 173.50 ms | 16.16 | 3.30 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | -5.06 µV | 1.95 | 0.40 | [-9.93, -0.80] |
| from 3 | 23 | -5.27 µV | 2.09 | 0.44 | [-9.69, -1.72] |
| from 4 | 23 | -5.43 µV | 2.38 | 0.50 | [-10.69, -1.93] |
| from 5 | 23 | -5.66 µV | 2.19 | 0.46 | [-9.69, -1.15] |
| from 6 | 24 | -5.42 µV | 2.08 | 0.42 | [-9.40, -2.21] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 14 | 103.71 ms | 8.37 | 2.24 | [92.00, 112.00] |
| from 3 | 14 | 105.43 ms | 7.46 | 1.99 | [92.00, 112.00] |
| from 4 | 9 | 107.11 ms | 5.21 | 1.74 | [100.00, 112.00] |
| from 5 | 15 | 105.33 ms | 8.37 | 2.16 | [92.00, 112.00] |
| from 6 | 13 | 108.00 ms | 5.89 | 1.63 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 14 | 1.85 µV | 1.49 | 0.40 | [0.44, 4.81] |
| from 3 | 14 | 1.95 µV | 1.67 | 0.45 | [0.50, 6.45] |
| from 4 | 9 | 2.46 µV | 1.22 | 0.41 | [0.70, 4.31] |
| from 5 | 15 | 2.15 µV | 1.02 | 0.26 | [0.84, 4.27] |
| from 6 | 13 | 2.52 µV | 1.50 | 0.42 | [1.07, 6.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 19 | 463.37 ms | 30.73 | 7.05 | [424.00, 532.00] |
| from 3 | 18 | 476.00 ms | 26.10 | 6.15 | [432.00, 532.00] |
| from 4 | 19 | 477.26 ms | 34.20 | 7.85 | [424.00, 532.00] |
| from 5 | 18 | 468.22 ms | 24.41 | 5.75 | [424.00, 524.00] |
| from 6 | 18 | 470.89 ms | 35.22 | 8.30 | [424.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 19 | 4.16 µV | 2.29 | 0.53 | [0.90, 7.65] |
| from 3 | 18 | 4.21 µV | 2.38 | 0.56 | [1.48, 8.91] |
| from 4 | 19 | 3.91 µV | 2.44 | 0.56 | [0.47, 8.51] |
| from 5 | 18 | 3.75 µV | 1.86 | 0.44 | [1.22, 6.53] |
| from 6 | 18 | 3.74 µV | 2.18 | 0.51 | [0.95, 8.95] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 300.68, BIC = 314.58
- **from 3 vs from 2**: *β* = -2.67, *SE* = 2.692, *z* = -0.993, *p* = 0.321
- **from 4 vs from 2**: *β* = -2.07, *SE* = 2.784, *z* = -0.744, *p* = 0.457
- **from 5 vs from 2**: *β* = 0.10, *SE* = 3.783, *z* = 0.027, *p* = 0.978
- **from 6 vs from 2**: *β* = -4.07, *SE* = 2.915, *z* = -1.396, *p* = 0.163
- **SNR**: *β* = -0.22, *SE* = 0.805, *z* = -0.277, *p* = 0.782

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 2.67 | 2.69 | 0.99 | 0.321 | 0.955 | n.s. |
| from 2 - from 4 | 2.07 | 2.78 | 0.74 | 0.457 | 0.979 | n.s. |
| from 2 - from 5 | -0.10 | 3.78 | -0.03 | 0.978 | 0.979 | n.s. |
| from 2 - from 6 | 4.07 | 2.91 | 1.40 | 0.163 | 0.831 | n.s. |
| from 3 - from 4 | -0.60 | 2.69 | -0.22 | 0.823 | 0.979 | n.s. |
| from 3 - from 5 | -2.78 | 3.48 | -0.80 | 0.425 | 0.979 | n.s. |
| from 3 - from 6 | 1.40 | 2.59 | 0.54 | 0.590 | 0.979 | n.s. |
| from 4 - from 5 | -2.18 | 3.54 | -0.62 | 0.538 | 0.979 | n.s. |
| from 4 - from 6 | 2.00 | 3.01 | 0.66 | 0.507 | 0.979 | n.s. |
| from 5 - from 6 | 4.17 | 3.65 | 1.14 | 0.253 | 0.927 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 89.97, BIC = 103.87
- **from 3 vs from 2**: *β* = 0.32, *SE* = 0.230, *z* = 1.400, *p* = 0.162
- **from 4 vs from 2**: *β* = 0.24, *SE* = 0.240, *z* = 1.024, *p* = 0.306
- **from 5 vs from 2**: *β* = 0.43, *SE* = 0.320, *z* = 1.340, *p* = 0.180
- **from 6 vs from 2**: *β* = 0.23, *SE* = 0.249, *z* = 0.919, *p* = 0.358
- **SNR**: *β* = 0.24, *SE* = 0.069, *z* = 3.562, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.32 | 0.23 | -1.40 | 0.162 | 0.828 | n.s. |
| from 2 - from 4 | -0.25 | 0.24 | -1.02 | 0.306 | 0.946 | n.s. |
| from 2 - from 5 | -0.43 | 0.32 | -1.34 | 0.180 | 0.833 | n.s. |
| from 2 - from 6 | -0.23 | 0.25 | -0.92 | 0.358 | 0.955 | n.s. |
| from 3 - from 4 | 0.08 | 0.23 | 0.33 | 0.744 | 0.990 | n.s. |
| from 3 - from 5 | -0.11 | 0.30 | -0.35 | 0.726 | 0.990 | n.s. |
| from 3 - from 6 | 0.09 | 0.23 | 0.41 | 0.681 | 0.990 | n.s. |
| from 4 - from 5 | -0.18 | 0.31 | -0.60 | 0.552 | 0.989 | n.s. |
| from 4 - from 6 | 0.02 | 0.26 | 0.06 | 0.949 | 0.990 | n.s. |
| from 5 - from 6 | 0.20 | 0.32 | 0.63 | 0.528 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 931.66, BIC = 953.75
- **from 3 vs from 2**: *β* = 1.47, *SE* = 2.750, *z* = 0.535, *p* = 0.592
- **from 4 vs from 2**: *β* = 2.37, *SE* = 2.747, *z* = 0.862, *p* = 0.388
- **from 5 vs from 2**: *β* = 5.03, *SE* = 2.763, *z* = 1.822, *p* = 0.068
- **from 6 vs from 2**: *β* = 4.39, *SE* = 2.704, *z* = 1.622, *p* = 0.105
- **SNR**: *β* = 0.11, *SE* = 0.192, *z* = 0.565, *p* = 0.572

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -1.47 | 2.75 | -0.54 | 0.592 | 0.932 | n.s. |
| from 2 - from 4 | -2.37 | 2.75 | -0.86 | 0.388 | 0.914 | n.s. |
| from 2 - from 5 | -5.03 | 2.76 | -1.82 | 0.068 | 0.508 | n.s. |
| from 2 - from 6 | -4.39 | 2.70 | -1.62 | 0.105 | 0.631 | n.s. |
| from 3 - from 4 | -0.90 | 2.76 | -0.32 | 0.745 | 0.935 | n.s. |
| from 3 - from 5 | -3.56 | 2.77 | -1.29 | 0.198 | 0.828 | n.s. |
| from 3 - from 6 | -2.91 | 2.76 | -1.06 | 0.290 | 0.909 | n.s. |
| from 4 - from 5 | -2.67 | 2.77 | -0.96 | 0.336 | 0.914 | n.s. |
| from 4 - from 6 | -2.02 | 2.75 | -0.73 | 0.464 | 0.917 | n.s. |
| from 5 - from 6 | 0.65 | 2.78 | 0.23 | 0.815 | 0.935 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.18, *p* = 0.324, η²_G = 0.015
- Greenhouse-Geisser corrected: *p* = 0.321 (ε = 0.613)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.66 | 22 | = 0.654 | -0.11 [-0.57, 0.30] | negligible | n.s. |
| from 2 vs from 4 | -1.33 | 22 | = 0.577 | -0.16 [-0.72, 0.16] | negligible | n.s. |
| from 2 vs from 5 | -1.52 | 22 | = 0.577 | -0.37 [-0.76, 0.13] | small | n.s. |
| from 2 vs from 6 | -1.46 | 22 | = 0.577 | -0.29 [-0.73, 0.13] | small | n.s. |
| from 3 vs from 4 | -0.44 | 22 | = 0.667 | -0.05 [-0.52, 0.34] | negligible | n.s. |
| from 3 vs from 5 | -1.23 | 22 | = 0.577 | -0.22 [-0.70, 0.18] | small | n.s. |
| from 3 vs from 6 | -0.90 | 22 | = 0.654 | -0.15 [-0.62, 0.25] | negligible | n.s. |
| from 4 vs from 5 | -0.81 | 22 | = 0.654 | -0.17 [-0.60, 0.27] | negligible | n.s. |
| from 4 vs from 6 | -0.59 | 22 | = 0.654 | -0.10 [-0.56, 0.31] | negligible | n.s. |
| from 5 vs from 6 | 0.55 | 22 | = 0.654 | 0.07 [-0.32, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 365.52, BIC = 387.62
- **from 3 vs from 2**: *β* = -0.13, *SE* = 0.228, *z* = -0.552, *p* = 0.581
- **from 4 vs from 2**: *β* = -0.31, *SE* = 0.228, *z* = -1.366, *p* = 0.172
- **from 5 vs from 2**: *β* = -0.45, *SE* = 0.230, *z* = -1.975, *p* = 0.048
- **from 6 vs from 2**: *β* = -0.40, *SE* = 0.225, *z* = -1.762, *p* = 0.078
- **SNR**: *β* = -0.08, *SE* = 0.016, *z* = -4.649, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.13 | 0.23 | 0.55 | 0.581 | 0.954 | n.s. |
| from 2 - from 4 | 0.31 | 0.23 | 1.37 | 0.172 | 0.737 | n.s. |
| from 2 - from 5 | 0.45 | 0.23 | 1.98 | 0.048 | 0.390 | n.s. |
| from 2 - from 6 | 0.40 | 0.22 | 1.76 | 0.078 | 0.518 | n.s. |
| from 3 - from 4 | 0.19 | 0.23 | 0.81 | 0.418 | 0.933 | n.s. |
| from 3 - from 5 | 0.33 | 0.23 | 1.43 | 0.154 | 0.737 | n.s. |
| from 3 - from 6 | 0.27 | 0.23 | 1.18 | 0.239 | 0.805 | n.s. |
| from 4 - from 5 | 0.14 | 0.23 | 0.62 | 0.537 | 0.954 | n.s. |
| from 4 - from 6 | 0.08 | 0.23 | 0.37 | 0.713 | 0.954 | n.s. |
| from 5 - from 6 | -0.06 | 0.23 | -0.25 | 0.802 | 0.954 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.61, *p* = 0.180, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.81 | 22 | = 0.535 | 0.11 [-0.27, 0.60] | negligible | n.s. |
| from 2 vs from 4 | 1.41 | 22 | = 0.432 | 0.17 [-0.15, 0.74] | negligible | n.s. |
| from 2 vs from 5 | 2.23 | 22 | = 0.363 | 0.29 [0.01, 0.92] | small | n.s. |
| from 2 vs from 6 | 1.66 | 22 | = 0.371 | 0.20 [-0.13, 0.73] | small | n.s. |
| from 3 vs from 4 | 0.67 | 22 | = 0.569 | 0.07 [-0.30, 0.57] | negligible | n.s. |
| from 3 vs from 5 | 1.74 | 22 | = 0.371 | 0.18 [-0.08, 0.81] | negligible | n.s. |
| from 3 vs from 6 | 0.84 | 22 | = 0.535 | 0.09 [-0.26, 0.61] | negligible | n.s. |
| from 4 vs from 5 | 0.83 | 22 | = 0.535 | 0.10 [-0.26, 0.61] | negligible | n.s. |
| from 4 vs from 6 | 0.09 | 22 | = 0.928 | 0.01 [-0.41, 0.45] | negligible | n.s. |
| from 5 vs from 6 | -1.02 | 22 | = 0.535 | -0.09 [-0.65, 0.22] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 430.00, BIC = 447.39
- **from 3 vs from 2**: *β* = 1.33, *SE* = 1.754, *z* = 0.761, *p* = 0.447
- **from 4 vs from 2**: *β* = 2.02, *SE* = 1.974, *z* = 1.025, *p* = 0.305
- **from 5 vs from 2**: *β* = 1.38, *SE* = 1.772, *z* = 0.778, *p* = 0.437
- **from 6 vs from 2**: *β* = 3.49, *SE* = 1.814, *z* = 1.925, *p* = 0.054
- **SNR**: *β* = 0.32, *SE* = 0.275, *z* = 1.166, *p* = 0.244

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -1.34 | 1.75 | -0.76 | 0.447 | 0.968 | n.s. |
| from 2 - from 4 | -2.02 | 1.97 | -1.03 | 0.305 | 0.922 | n.s. |
| from 2 - from 5 | -1.38 | 1.77 | -0.78 | 0.437 | 0.968 | n.s. |
| from 2 - from 6 | -3.49 | 1.81 | -1.92 | 0.054 | 0.428 | n.s. |
| from 3 - from 4 | -0.69 | 1.97 | -0.35 | 0.726 | 0.979 | n.s. |
| from 3 - from 5 | -0.04 | 1.75 | -0.02 | 0.980 | 0.980 | n.s. |
| from 3 - from 6 | -2.16 | 1.78 | -1.21 | 0.225 | 0.899 | n.s. |
| from 4 - from 5 | 0.65 | 2.00 | 0.32 | 0.747 | 0.979 | n.s. |
| from 4 - from 6 | -1.47 | 2.03 | -0.72 | 0.469 | 0.968 | n.s. |
| from 5 - from 6 | -2.11 | 1.74 | -1.21 | 0.225 | 0.899 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.22, *p* = 0.342, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | nan | 4 | n/a | 0.00 [-0.67, 0.67] | negligible | n.s. |
| from 2 vs from 4 | 1.63 | 4 | = 0.421 | 0.34 [-1.06, 0.63] | small | n.s. |
| from 2 vs from 5 | 1.00 | 4 | = 0.421 | 0.18 [-1.06, 0.41] | negligible | n.s. |
| from 2 vs from 6 | 1.00 | 4 | = 0.421 | 0.20 [-1.29, 0.23] | negligible | n.s. |
| from 3 vs from 4 | 1.63 | 4 | = 0.421 | 0.34 [-0.51, 1.22] | small | n.s. |
| from 3 vs from 5 | 1.00 | 4 | = 0.421 | 0.18 [-0.83, 0.60] | negligible | n.s. |
| from 3 vs from 6 | 1.00 | 4 | = 0.421 | 0.20 [-1.01, 0.45] | negligible | n.s. |
| from 4 vs from 5 | -1.00 | 4 | = 0.421 | -0.15 [-0.92, 0.92] | negligible | n.s. |
| from 4 vs from 6 | -1.00 | 4 | = 0.421 | -0.16 [-1.59, 0.42] | negligible | n.s. |
| from 5 vs from 6 | 0.00 | 4 | = 1.000 | 0.00 [-0.95, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 187.20, BIC = 204.59
- **from 3 vs from 2**: *β* = 0.01, *SE* = 0.278, *z* = 0.047, *p* = 0.963
- **from 4 vs from 2**: *β* = 0.27, *SE* = 0.313, *z* = 0.859, *p* = 0.391
- **from 5 vs from 2**: *β* = 0.30, *SE* = 0.281, *z* = 1.059, *p* = 0.290
- **from 6 vs from 2**: *β* = 0.50, *SE* = 0.288, *z* = 1.747, *p* = 0.081
- **SNR**: *β* = 0.17, *SE* = 0.045, *z* = 3.793, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.01 | 0.28 | -0.05 | 0.963 | 0.995 | n.s. |
| from 2 - from 4 | -0.27 | 0.31 | -0.86 | 0.391 | 0.949 | n.s. |
| from 2 - from 5 | -0.30 | 0.28 | -1.06 | 0.290 | 0.935 | n.s. |
| from 2 - from 6 | -0.50 | 0.29 | -1.75 | 0.081 | 0.568 | n.s. |
| from 3 - from 4 | -0.26 | 0.31 | -0.82 | 0.413 | 0.949 | n.s. |
| from 3 - from 5 | -0.28 | 0.28 | -1.03 | 0.305 | 0.935 | n.s. |
| from 3 - from 6 | -0.49 | 0.28 | -1.74 | 0.082 | 0.568 | n.s. |
| from 4 - from 5 | -0.03 | 0.32 | -0.09 | 0.928 | 0.995 | n.s. |
| from 4 - from 6 | -0.23 | 0.32 | -0.73 | 0.468 | 0.949 | n.s. |
| from 5 - from 6 | -0.21 | 0.28 | -0.75 | 0.456 | 0.949 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.49, *p* = 0.741, η²_G = 0.047
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.22 | 4 | = 0.936 | -0.10 [-0.78, 0.57] | negligible | n.s. |
| from 2 vs from 4 | 0.89 | 4 | = 0.874 | 0.39 [-0.96, 0.72] | small | n.s. |
| from 2 vs from 5 | -0.02 | 4 | = 0.989 | -0.01 [-0.97, 0.48] | negligible | n.s. |
| from 2 vs from 6 | -0.85 | 4 | = 0.874 | -0.27 [-1.50, 0.10] | small | n.s. |
| from 3 vs from 4 | 0.76 | 4 | = 0.874 | 0.42 [-0.87, 0.81] | small | n.s. |
| from 3 vs from 5 | 0.21 | 4 | = 0.936 | 0.11 [-0.94, 0.51] | negligible | n.s. |
| from 3 vs from 6 | -0.63 | 4 | = 0.874 | -0.14 [-1.46, 0.12] | negligible | n.s. |
| from 4 vs from 5 | -1.80 | 4 | = 0.874 | -0.74 [-2.11, 0.14] | medium | n.s. |
| from 4 vs from 6 | -1.28 | 4 | = 0.874 | -0.65 [-1.58, 0.42] | medium | n.s. |
| from 5 vs from 6 | -0.55 | 4 | = 0.874 | -0.31 [-0.94, 0.43] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 879.35, BIC = 899.53
- **from 3 vs from 2**: *β* = 10.84, *SE* = 7.579, *z* = 1.430, *p* = 0.153
- **from 4 vs from 2**: *β* = 12.26, *SE* = 7.476, *z* = 1.640, *p* = 0.101
- **from 5 vs from 2**: *β* = 3.44, *SE* = 7.584, *z* = 0.454, *p* = 0.650
- **from 6 vs from 2**: *β* = 7.32, *SE* = 7.533, *z* = 0.972, *p* = 0.331
- **SNR**: *β* = 1.41, *SE* = 0.605, *z* = 2.327, *p* = 0.020

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -10.84 | 7.58 | -1.43 | 0.153 | 0.775 | n.s. |
| from 2 - from 4 | -12.26 | 7.48 | -1.64 | 0.101 | 0.655 | n.s. |
| from 2 - from 5 | -3.44 | 7.58 | -0.45 | 0.650 | 0.977 | n.s. |
| from 2 - from 6 | -7.32 | 7.53 | -0.97 | 0.331 | 0.940 | n.s. |
| from 3 - from 4 | -1.42 | 7.53 | -0.19 | 0.850 | 0.977 | n.s. |
| from 3 - from 5 | 7.39 | 7.71 | 0.96 | 0.338 | 0.940 | n.s. |
| from 3 - from 6 | 3.52 | 7.62 | 0.46 | 0.645 | 0.977 | n.s. |
| from 4 - from 5 | 8.82 | 7.54 | 1.17 | 0.242 | 0.891 | n.s. |
| from 4 - from 6 | 4.94 | 7.53 | 0.66 | 0.512 | 0.972 | n.s. |
| from 5 - from 6 | -3.88 | 7.65 | -0.51 | 0.613 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.463, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -1.37 | 16 | = 0.602 | -0.43 [-0.87, 0.15] | small | n.s. |
| from 2 vs from 4 | -1.69 | 16 | = 0.602 | -0.41 [-0.92, 0.11] | small | n.s. |
| from 2 vs from 5 | -0.32 | 16 | = 0.840 | -0.10 [-0.59, 0.44] | negligible | n.s. |
| from 2 vs from 6 | -0.99 | 16 | = 0.670 | -0.23 [-0.76, 0.25] | small | n.s. |
| from 3 vs from 4 | -0.11 | 16 | = 0.917 | -0.02 [-0.48, 0.51] | negligible | n.s. |
| from 3 vs from 5 | 1.22 | 16 | = 0.602 | 0.38 [-0.23, 0.82] | small | n.s. |
| from 3 vs from 6 | 0.45 | 16 | = 0.819 | 0.15 [-0.38, 0.62] | negligible | n.s. |
| from 4 vs from 5 | 1.35 | 16 | = 0.602 | 0.35 [-0.14, 0.89] | small | n.s. |
| from 4 vs from 6 | 0.57 | 16 | = 0.819 | 0.16 [-0.38, 0.62] | negligible | n.s. |
| from 5 vs from 6 | -0.52 | 16 | = 0.819 | -0.16 [-0.64, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 300.13, BIC = 320.30
- **from 3 vs from 2**: *β* = -0.24, *SE* = 0.274, *z* = -0.885, *p* = 0.376
- **from 4 vs from 2**: *β* = -0.33, *SE* = 0.271, *z* = -1.221, *p* = 0.222
- **from 5 vs from 2**: *β* = -0.42, *SE* = 0.275, *z* = -1.512, *p* = 0.130
- **from 6 vs from 2**: *β* = -0.54, *SE* = 0.273, *z* = -1.985, *p* = 0.047
- **SNR**: *β* = 0.15, *SE* = 0.023, *z* = 6.383, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.24 | 0.27 | 0.89 | 0.376 | 0.941 | n.s. |
| from 2 - from 4 | 0.33 | 0.27 | 1.22 | 0.222 | 0.866 | n.s. |
| from 2 - from 5 | 0.42 | 0.28 | 1.51 | 0.130 | 0.716 | n.s. |
| from 2 - from 6 | 0.54 | 0.27 | 1.99 | 0.047 | 0.383 | n.s. |
| from 3 - from 4 | 0.09 | 0.27 | 0.33 | 0.745 | 0.958 | n.s. |
| from 3 - from 5 | 0.17 | 0.28 | 0.62 | 0.534 | 0.953 | n.s. |
| from 3 - from 6 | 0.30 | 0.27 | 1.09 | 0.277 | 0.897 | n.s. |
| from 4 - from 5 | 0.09 | 0.27 | 0.31 | 0.754 | 0.958 | n.s. |
| from 4 - from 6 | 0.21 | 0.27 | 0.77 | 0.439 | 0.945 | n.s. |
| from 5 - from 6 | 0.12 | 0.28 | 0.45 | 0.651 | 0.958 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.432, η²_G = 0.011
- Greenhouse-Geisser corrected: *p* = 0.402 (ε = 0.592)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.02 | 16 | = 0.982 | 0.00 [-0.45, 0.55] | negligible | n.s. |
| from 2 vs from 4 | 0.62 | 16 | = 0.683 | 0.07 [-0.33, 0.67] | negligible | n.s. |
| from 2 vs from 5 | 2.05 | 16 | = 0.568 | 0.23 [-0.05, 1.04] | small | n.s. |
| from 2 vs from 6 | 1.05 | 16 | = 0.633 | 0.23 [-0.24, 0.78] | small | n.s. |
| from 3 vs from 4 | 0.63 | 16 | = 0.683 | 0.06 [-0.38, 0.62] | negligible | n.s. |
| from 3 vs from 5 | 1.67 | 16 | = 0.569 | 0.23 [-0.13, 0.94] | small | n.s. |
| from 3 vs from 6 | 1.03 | 16 | = 0.633 | 0.22 [-0.27, 0.74] | small | n.s. |
| from 4 vs from 5 | 1.08 | 16 | = 0.633 | 0.16 [-0.29, 0.72] | negligible | n.s. |
| from 4 vs from 6 | 0.80 | 16 | = 0.683 | 0.16 [-0.31, 0.70] | negligible | n.s. |
| from 5 vs from 6 | 0.07 | 16 | = 0.982 | 0.01 [-0.50, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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
