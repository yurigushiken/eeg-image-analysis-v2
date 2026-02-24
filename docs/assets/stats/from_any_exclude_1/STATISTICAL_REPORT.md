# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:22:13

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
| from 2 | 24 | 102.50 ms | 8.32 | 1.70 | [92.00, 112.00] |
| from 3 | 24 | 102.67 ms | 8.48 | 1.73 | [92.00, 112.00] |
| from 4 | 24 | 104.00 ms | 7.55 | 1.54 | [92.00, 112.00] |
| from 5 | 24 | 103.67 ms | 7.73 | 1.58 | [92.00, 112.00] |
| from 6 | 24 | 105.00 ms | 7.20 | 1.47 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | -0.87 µV | 1.29 | 0.26 | [-4.10, 1.73] |
| from 3 | 24 | -1.06 µV | 1.46 | 0.30 | [-4.25, 1.77] |
| from 4 | 24 | -0.81 µV | 1.50 | 0.31 | [-4.00, 1.39] |
| from 5 | 24 | -1.59 µV | 1.28 | 0.26 | [-4.87, 0.96] |
| from 6 | 24 | -1.52 µV | 1.66 | 0.34 | [-7.02, 0.48] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 169.17 ms | 17.31 | 3.53 | [140.00, 204.00] |
| from 3 | 24 | 171.00 ms | 19.64 | 4.01 | [140.00, 204.00] |
| from 4 | 24 | 171.83 ms | 18.89 | 3.86 | [140.00, 204.00] |
| from 5 | 24 | 174.50 ms | 15.05 | 3.07 | [144.00, 204.00] |
| from 6 | 24 | 173.50 ms | 16.16 | 3.30 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | -5.06 µV | 1.95 | 0.40 | [-9.93, -0.80] |
| from 3 | 24 | -5.20 µV | 2.07 | 0.42 | [-9.69, -1.72] |
| from 4 | 24 | -5.35 µV | 2.36 | 0.48 | [-10.69, -1.93] |
| from 5 | 24 | -5.55 µV | 2.21 | 0.45 | [-9.69, -1.15] |
| from 6 | 24 | -5.42 µV | 2.08 | 0.42 | [-9.40, -2.21] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 102.33 ms | 8.82 | 1.80 | [92.00, 112.00] |
| from 3 | 24 | 102.17 ms | 8.42 | 1.72 | [92.00, 112.00] |
| from 4 | 24 | 103.50 ms | 7.76 | 1.58 | [92.00, 112.00] |
| from 5 | 24 | 104.17 ms | 8.63 | 1.76 | [92.00, 112.00] |
| from 6 | 24 | 104.50 ms | 8.11 | 1.66 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 0.98 µV | 1.65 | 0.34 | [-2.63, 4.81] |
| from 3 | 24 | 0.92 µV | 1.85 | 0.38 | [-1.86, 6.45] |
| from 4 | 24 | 0.70 µV | 1.64 | 0.33 | [-1.45, 4.31] |
| from 5 | 24 | 1.31 µV | 1.39 | 0.28 | [-0.81, 4.27] |
| from 6 | 24 | 1.19 µV | 1.92 | 0.39 | [-2.48, 6.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 467.50 ms | 31.50 | 6.43 | [424.00, 532.00] |
| from 3 | 24 | 483.00 ms | 32.09 | 6.55 | [432.00, 532.00] |
| from 4 | 24 | 477.83 ms | 34.49 | 7.04 | [424.00, 532.00] |
| from 5 | 24 | 474.17 ms | 29.37 | 6.00 | [424.00, 524.00] |
| from 6 | 24 | 468.17 ms | 32.89 | 6.71 | [424.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 3.15 µV | 3.00 | 0.61 | [-3.97, 7.65] |
| from 3 | 24 | 2.90 µV | 3.20 | 0.65 | [-3.89, 8.91] |
| from 4 | 24 | 2.90 µV | 2.98 | 0.61 | [-2.80, 8.51] |
| from 5 | 24 | 2.49 µV | 2.83 | 0.58 | [-2.98, 6.53] |
| from 6 | 24 | 2.51 µV | 3.00 | 0.61 | [-4.12, 8.95] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 789.82, BIC = 812.12
- **from 3 vs from 2**: *β* = 0.12, *SE* = 1.431, *z* = 0.086, *p* = 0.931
- **from 4 vs from 2**: *β* = 1.46, *SE* = 1.429, *z* = 1.025, *p* = 0.305
- **from 5 vs from 2**: *β* = 1.06, *SE* = 1.475, *z* = 0.718, *p* = 0.473
- **from 6 vs from 2**: *β* = 2.46, *SE* = 1.430, *z* = 1.722, *p* = 0.085
- **SNR**: *β* = 0.08, *SE* = 0.276, *z* = 0.275, *p* = 0.784

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.12 | 1.43 | -0.09 | 0.931 | 0.959 | n.s. |
| from 2 - from 4 | -1.46 | 1.43 | -1.03 | 0.305 | 0.946 | n.s. |
| from 2 - from 5 | -1.06 | 1.48 | -0.72 | 0.473 | 0.959 | n.s. |
| from 2 - from 6 | -2.46 | 1.43 | -1.72 | 0.085 | 0.589 | n.s. |
| from 3 - from 4 | -1.34 | 1.42 | -0.94 | 0.346 | 0.946 | n.s. |
| from 3 - from 5 | -0.94 | 1.44 | -0.65 | 0.516 | 0.959 | n.s. |
| from 3 - from 6 | -2.34 | 1.42 | -1.64 | 0.100 | 0.614 | n.s. |
| from 4 - from 5 | 0.40 | 1.45 | 0.28 | 0.780 | 0.959 | n.s. |
| from 4 - from 6 | -1.00 | 1.42 | -0.70 | 0.483 | 0.959 | n.s. |
| from 5 - from 6 | -1.40 | 1.44 | -0.97 | 0.332 | 0.946 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.415, η²_G = 0.014
- Greenhouse-Geisser corrected: *p* = 0.399 (ε = 0.729)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.10 | 23 | = 0.922 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| from 2 vs from 4 | -0.94 | 23 | = 0.594 | -0.19 [-0.62, 0.23] | negligible | n.s. |
| from 2 vs from 5 | -0.67 | 23 | = 0.729 | -0.15 [-0.56, 0.29] | negligible | n.s. |
| from 2 vs from 6 | -1.81 | 23 | = 0.565 | -0.32 [-0.81, 0.07] | small | n.s. |
| from 3 vs from 4 | -1.19 | 23 | = 0.565 | -0.17 [-0.67, 0.19] | negligible | n.s. |
| from 3 vs from 5 | -0.54 | 23 | = 0.743 | -0.12 [-0.53, 0.31] | negligible | n.s. |
| from 3 vs from 6 | -1.59 | 23 | = 0.565 | -0.30 [-0.76, 0.11] | small | n.s. |
| from 4 vs from 5 | 0.25 | 23 | = 0.895 | 0.04 [-0.37, 0.47] | negligible | n.s. |
| from 4 vs from 6 | -1.10 | 23 | = 0.565 | -0.14 [-0.65, 0.20] | negligible | n.s. |
| from 5 vs from 6 | -1.14 | 23 | = 0.565 | -0.18 [-0.66, 0.20] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 373.72, BIC = 396.02
- **from 3 vs from 2**: *β* = -0.07, *SE* = 0.260, *z* = -0.253, *p* = 0.801
- **from 4 vs from 2**: *β* = 0.16, *SE* = 0.260, *z* = 0.632, *p* = 0.527
- **from 5 vs from 2**: *β* = -0.43, *SE* = 0.268, *z* = -1.594, *p* = 0.111
- **from 6 vs from 2**: *β* = -0.54, *SE* = 0.260, *z* = -2.086, *p* = 0.037
- **SNR**: *β* = -0.21, *SE* = 0.051, *z* = -4.074, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.07 | 0.26 | 0.25 | 0.801 | 0.894 | n.s. |
| from 2 - from 4 | -0.16 | 0.26 | -0.63 | 0.527 | 0.894 | n.s. |
| from 2 - from 5 | 0.43 | 0.27 | 1.59 | 0.111 | 0.506 | n.s. |
| from 2 - from 6 | 0.54 | 0.26 | 2.09 | 0.037 | 0.260 | n.s. |
| from 3 - from 4 | -0.23 | 0.26 | -0.89 | 0.374 | 0.847 | n.s. |
| from 3 - from 5 | 0.36 | 0.26 | 1.38 | 0.167 | 0.599 | n.s. |
| from 3 - from 6 | 0.48 | 0.26 | 1.84 | 0.066 | 0.378 | n.s. |
| from 4 - from 5 | 0.59 | 0.26 | 2.25 | 0.024 | 0.199 | n.s. |
| from 4 - from 6 | 0.71 | 0.26 | 2.73 | 0.006 | 0.061 | n.s. |
| from 5 - from 6 | 0.11 | 0.26 | 0.44 | 0.663 | 0.894 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.47, *p* = 0.011, η²_G = 0.051
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.71 | 23 | = 0.607 | 0.13 [-0.28, 0.57] | negligible | n.s. |
| from 2 vs from 4 | -0.23 | 23 | = 0.818 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| from 2 vs from 5 | 3.04 | 23 | = 0.058 | 0.56 [0.16, 1.08] | medium | n.s. |
| from 2 vs from 6 | 2.03 | 23 | = 0.109 | 0.43 [-0.03, 0.85] | small | n.s. |
| from 3 vs from 4 | -1.20 | 23 | = 0.349 | -0.17 [-0.67, 0.18] | negligible | n.s. |
| from 3 vs from 5 | 2.28 | 23 | = 0.107 | 0.39 [0.02, 0.91] | small | n.s. |
| from 3 vs from 6 | 1.68 | 23 | = 0.178 | 0.30 [-0.09, 0.78] | small | n.s. |
| from 4 vs from 5 | 2.39 | 23 | = 0.107 | 0.56 [0.04, 0.93] | medium | n.s. |
| from 4 vs from 6 | 2.08 | 23 | = 0.109 | 0.45 [-0.02, 0.87] | small | n.s. |
| from 5 vs from 6 | -0.29 | 23 | = 0.818 | -0.05 [-0.48, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 951.80, BIC = 974.10
- **from 3 vs from 2**: *β* = 1.75, *SE* = 2.660, *z* = 0.658, *p* = 0.510
- **from 4 vs from 2**: *β* = 2.61, *SE* = 2.658, *z* = 0.982, *p* = 0.326
- **from 5 vs from 2**: *β* = 5.17, *SE* = 2.672, *z* = 1.934, *p* = 0.053
- **from 6 vs from 2**: *β* = 4.38, *SE* = 2.658, *z* = 1.650, *p* = 0.099
- **SNR**: *β* = 0.11, *SE* = 0.189, *z* = 0.564, *p* = 0.573

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -1.75 | 2.66 | -0.66 | 0.510 | 0.940 | n.s. |
| from 2 - from 4 | -2.61 | 2.66 | -0.98 | 0.326 | 0.935 | n.s. |
| from 2 - from 5 | -5.17 | 2.67 | -1.93 | 0.053 | 0.421 | n.s. |
| from 2 - from 6 | -4.39 | 2.66 | -1.65 | 0.099 | 0.608 | n.s. |
| from 3 - from 4 | -0.86 | 2.66 | -0.32 | 0.746 | 0.940 | n.s. |
| from 3 - from 5 | -3.42 | 2.66 | -1.28 | 0.199 | 0.831 | n.s. |
| from 3 - from 6 | -2.63 | 2.67 | -0.99 | 0.323 | 0.935 | n.s. |
| from 4 - from 5 | -2.56 | 2.66 | -0.96 | 0.337 | 0.935 | n.s. |
| from 4 - from 6 | -1.77 | 2.66 | -0.67 | 0.505 | 0.940 | n.s. |
| from 5 - from 6 | 0.78 | 2.68 | 0.29 | 0.771 | 0.940 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.18, *p* = 0.324, η²_G = 0.012
- Greenhouse-Geisser corrected: *p* = 0.320 (ε = 0.612)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.66 | 23 | = 0.654 | -0.10 [-0.56, 0.29] | negligible | n.s. |
| from 2 vs from 4 | -1.33 | 23 | = 0.576 | -0.15 [-0.70, 0.16] | negligible | n.s. |
| from 2 vs from 5 | -1.52 | 23 | = 0.576 | -0.33 [-0.74, 0.12] | small | n.s. |
| from 2 vs from 6 | -1.46 | 23 | = 0.576 | -0.26 [-0.73, 0.13] | small | n.s. |
| from 3 vs from 4 | -0.44 | 23 | = 0.667 | -0.04 [-0.51, 0.33] | negligible | n.s. |
| from 3 vs from 5 | -1.23 | 23 | = 0.576 | -0.20 [-0.68, 0.18] | small | n.s. |
| from 3 vs from 6 | -0.90 | 23 | = 0.654 | -0.14 [-0.61, 0.24] | negligible | n.s. |
| from 4 vs from 5 | -0.81 | 23 | = 0.654 | -0.16 [-0.59, 0.26] | negligible | n.s. |
| from 4 vs from 6 | -0.59 | 23 | = 0.654 | -0.09 [-0.54, 0.30] | negligible | n.s. |
| from 5 vs from 6 | 0.55 | 23 | = 0.654 | 0.06 [-0.31, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 375.82, BIC = 398.12
- **from 3 vs from 2**: *β* = -0.08, *SE* = 0.228, *z* = -0.350, *p* = 0.726
- **from 4 vs from 2**: *β* = -0.25, *SE* = 0.227, *z* = -1.090, *p* = 0.276
- **from 5 vs from 2**: *β* = -0.36, *SE* = 0.229, *z* = -1.592, *p* = 0.111
- **from 6 vs from 2**: *β* = -0.40, *SE* = 0.227, *z* = -1.745, *p* = 0.081
- **SNR**: *β* = -0.08, *SE* = 0.016, *z* = -4.754, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.08 | 0.23 | 0.35 | 0.726 | 0.954 | n.s. |
| from 2 - from 4 | 0.25 | 0.23 | 1.09 | 0.276 | 0.856 | n.s. |
| from 2 - from 5 | 0.36 | 0.23 | 1.59 | 0.111 | 0.654 | n.s. |
| from 2 - from 6 | 0.40 | 0.23 | 1.75 | 0.081 | 0.570 | n.s. |
| from 3 - from 4 | 0.17 | 0.23 | 0.74 | 0.459 | 0.954 | n.s. |
| from 3 - from 5 | 0.28 | 0.23 | 1.25 | 0.211 | 0.810 | n.s. |
| from 3 - from 6 | 0.32 | 0.23 | 1.39 | 0.165 | 0.763 | n.s. |
| from 4 - from 5 | 0.12 | 0.23 | 0.51 | 0.610 | 0.954 | n.s. |
| from 4 - from 6 | 0.15 | 0.23 | 0.65 | 0.513 | 0.954 | n.s. |
| from 5 - from 6 | 0.03 | 0.23 | 0.14 | 0.887 | 0.954 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.13, *p* = 0.346, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.52 | 23 | = 0.673 | 0.07 [-0.32, 0.53] | negligible | n.s. |
| from 2 vs from 4 | 1.04 | 23 | = 0.666 | 0.13 [-0.21, 0.64] | negligible | n.s. |
| from 2 vs from 5 | 1.69 | 23 | = 0.509 | 0.23 [-0.09, 0.78] | small | n.s. |
| from 2 vs from 6 | 1.48 | 23 | = 0.509 | 0.18 [-0.13, 0.73] | negligible | n.s. |
| from 3 vs from 4 | 0.62 | 23 | = 0.673 | 0.07 [-0.30, 0.55] | negligible | n.s. |
| from 3 vs from 5 | 1.58 | 23 | = 0.509 | 0.16 [-0.11, 0.76] | negligible | n.s. |
| from 3 vs from 6 | 0.99 | 23 | = 0.666 | 0.11 [-0.22, 0.63] | negligible | n.s. |
| from 4 vs from 5 | 0.76 | 23 | = 0.673 | 0.09 [-0.27, 0.58] | negligible | n.s. |
| from 4 vs from 6 | 0.24 | 23 | = 0.812 | 0.03 [-0.37, 0.47] | negligible | n.s. |
| from 5 vs from 6 | -0.65 | 23 | = 0.673 | -0.06 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 809.09, BIC = 831.39
- **from 3 vs from 2**: *β* = -0.28, *SE* = 1.563, *z* = -0.176, *p* = 0.860
- **from 4 vs from 2**: *β* = 1.10, *SE* = 1.559, *z* = 0.708, *p* = 0.479
- **from 5 vs from 2**: *β* = 1.79, *SE* = 1.558, *z* = 1.148, *p* = 0.251
- **from 6 vs from 2**: *β* = 2.08, *SE* = 1.560, *z* = 1.333, *p* = 0.183
- **SNR**: *β* = 0.21, *SE* = 0.264, *z* = 0.810, *p* = 0.418

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.28 | 1.56 | 0.18 | 0.860 | 0.978 | n.s. |
| from 2 - from 4 | -1.10 | 1.56 | -0.71 | 0.479 | 0.962 | n.s. |
| from 2 - from 5 | -1.79 | 1.56 | -1.15 | 0.251 | 0.868 | n.s. |
| from 2 - from 6 | -2.08 | 1.56 | -1.33 | 0.183 | 0.837 | n.s. |
| from 3 - from 4 | -1.38 | 1.56 | -0.89 | 0.376 | 0.941 | n.s. |
| from 3 - from 5 | -2.06 | 1.56 | -1.32 | 0.186 | 0.837 | n.s. |
| from 3 - from 6 | -2.36 | 1.56 | -1.51 | 0.130 | 0.752 | n.s. |
| from 4 - from 5 | -0.68 | 1.56 | -0.44 | 0.660 | 0.962 | n.s. |
| from 4 - from 6 | -0.98 | 1.56 | -0.63 | 0.530 | 0.962 | n.s. |
| from 5 - from 6 | -0.29 | 1.56 | -0.19 | 0.851 | 0.978 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.87, *p* = 0.482, η²_G = 0.013
- Greenhouse-Geisser corrected: *p* = 0.445 (ε = 0.636)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.07 | 23 | = 0.942 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| from 2 vs from 4 | -0.73 | 23 | = 0.678 | -0.14 [-0.57, 0.28] | negligible | n.s. |
| from 2 vs from 5 | -0.99 | 23 | = 0.646 | -0.21 [-0.63, 0.22] | small | n.s. |
| from 2 vs from 6 | -1.80 | 23 | = 0.646 | -0.26 [-0.80, 0.07] | small | n.s. |
| from 3 vs from 4 | -0.90 | 23 | = 0.646 | -0.16 [-0.61, 0.24] | negligible | n.s. |
| from 3 vs from 5 | -1.45 | 23 | = 0.646 | -0.23 [-0.73, 0.14] | small | n.s. |
| from 3 vs from 6 | -1.33 | 23 | = 0.646 | -0.28 [-0.70, 0.16] | small | n.s. |
| from 4 vs from 5 | -0.42 | 23 | = 0.844 | -0.08 [-0.51, 0.34] | negligible | n.s. |
| from 4 vs from 6 | -0.88 | 23 | = 0.646 | -0.13 [-0.61, 0.25] | negligible | n.s. |
| from 5 vs from 6 | -0.24 | 23 | = 0.905 | -0.04 [-0.47, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 394.87, BIC = 417.17
- **from 3 vs from 2**: *β* = -0.09, *SE* = 0.266, *z* = -0.329, *p* = 0.742
- **from 4 vs from 2**: *β* = -0.30, *SE* = 0.265, *z* = -1.116, *p* = 0.265
- **from 5 vs from 2**: *β* = 0.32, *SE* = 0.265, *z* = 1.215, *p* = 0.224
- **from 6 vs from 2**: *β* = 0.19, *SE* = 0.266, *z* = 0.702, *p* = 0.483
- **SNR**: *β* = 0.05, *SE* = 0.047, *z* = 1.116, *p* = 0.264

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.09 | 0.27 | 0.33 | 0.742 | 0.896 | n.s. |
| from 2 - from 4 | 0.30 | 0.27 | 1.12 | 0.265 | 0.842 | n.s. |
| from 2 - from 5 | -0.32 | 0.27 | -1.22 | 0.224 | 0.831 | n.s. |
| from 2 - from 6 | -0.19 | 0.27 | -0.70 | 0.483 | 0.896 | n.s. |
| from 3 - from 4 | 0.21 | 0.27 | 0.79 | 0.432 | 0.896 | n.s. |
| from 3 - from 5 | -0.41 | 0.27 | -1.54 | 0.122 | 0.648 | n.s. |
| from 3 - from 6 | -0.27 | 0.27 | -1.03 | 0.301 | 0.842 | n.s. |
| from 4 - from 5 | -0.62 | 0.27 | -2.33 | 0.020 | 0.180 | n.s. |
| from 4 - from 6 | -0.48 | 0.27 | -1.82 | 0.069 | 0.473 | n.s. |
| from 5 - from 6 | 0.14 | 0.27 | 0.51 | 0.609 | 0.896 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.57, *p* = 0.190, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.22 | 23 | = 0.829 | 0.03 [-0.38, 0.47] | negligible | n.s. |
| from 2 vs from 4 | 1.03 | 23 | = 0.493 | 0.17 [-0.22, 0.64] | negligible | n.s. |
| from 2 vs from 5 | -1.39 | 23 | = 0.466 | -0.22 [-0.72, 0.15] | small | n.s. |
| from 2 vs from 6 | -0.87 | 23 | = 0.493 | -0.12 [-0.60, 0.25] | negligible | n.s. |
| from 3 vs from 4 | 0.96 | 23 | = 0.493 | 0.13 [-0.23, 0.62] | negligible | n.s. |
| from 3 vs from 5 | -1.36 | 23 | = 0.466 | -0.24 [-0.71, 0.15] | small | n.s. |
| from 3 vs from 6 | -1.22 | 23 | = 0.470 | -0.14 [-0.68, 0.18] | negligible | n.s. |
| from 4 vs from 5 | -1.90 | 23 | = 0.466 | -0.40 [-0.83, 0.05] | small | n.s. |
| from 4 vs from 6 | -1.48 | 23 | = 0.466 | -0.27 [-0.73, 0.13] | small | n.s. |
| from 5 vs from 6 | 0.49 | 23 | = 0.698 | 0.08 [-0.32, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1157.98, BIC = 1180.28
- **from 3 vs from 2**: *β* = 14.65, *SE* = 7.084, *z* = 2.068, *p* = 0.039
- **from 4 vs from 2**: *β* = 9.87, *SE* = 7.027, *z* = 1.405, *p* = 0.160
- **from 5 vs from 2**: *β* = 6.50, *SE* = 7.007, *z* = 0.928, *p* = 0.354
- **from 6 vs from 2**: *β* = 0.08, *SE* = 7.041, *z* = 0.012, *p* = 0.990
- **SNR**: *β* = 0.47, *SE* = 0.582, *z* = 0.800, *p* = 0.424

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -14.65 | 7.08 | -2.07 | 0.039 | 0.319 | n.s. |
| from 2 - from 4 | -9.87 | 7.03 | -1.40 | 0.160 | 0.752 | n.s. |
| from 2 - from 5 | -6.50 | 7.01 | -0.93 | 0.354 | 0.887 | n.s. |
| from 2 - from 6 | -0.08 | 7.04 | -0.01 | 0.990 | 0.990 | n.s. |
| from 3 - from 4 | 4.78 | 7.02 | 0.68 | 0.496 | 0.887 | n.s. |
| from 3 - from 5 | 8.15 | 7.06 | 1.16 | 0.248 | 0.819 | n.s. |
| from 3 - from 6 | 14.57 | 7.01 | 2.08 | 0.038 | 0.319 | n.s. |
| from 4 - from 5 | 3.37 | 7.01 | 0.48 | 0.630 | 0.887 | n.s. |
| from 4 - from 6 | 9.79 | 7.01 | 1.40 | 0.162 | 0.752 | n.s. |
| from 5 - from 6 | 6.41 | 7.02 | 0.91 | 0.361 | 0.887 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.65, *p* = 0.168, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -2.20 | 23 | = 0.379 | -0.49 [-0.89, -0.01] | small | n.s. |
| from 2 vs from 4 | -1.64 | 23 | = 0.385 | -0.31 [-0.77, 0.10] | small | n.s. |
| from 2 vs from 5 | -0.91 | 23 | = 0.555 | -0.22 [-0.61, 0.24] | small | n.s. |
| from 2 vs from 6 | -0.10 | 23 | = 0.924 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| from 3 vs from 4 | 0.88 | 23 | = 0.555 | 0.16 [-0.25, 0.60] | negligible | n.s. |
| from 3 vs from 5 | 1.37 | 23 | = 0.463 | 0.29 [-0.15, 0.71] | small | n.s. |
| from 3 vs from 6 | 1.64 | 23 | = 0.385 | 0.46 [-0.10, 0.77] | small | n.s. |
| from 4 vs from 5 | 0.54 | 23 | = 0.662 | 0.11 [-0.31, 0.53] | negligible | n.s. |
| from 4 vs from 6 | 1.22 | 23 | = 0.470 | 0.29 [-0.18, 0.68] | small | n.s. |
| from 5 vs from 6 | 0.76 | 23 | = 0.567 | 0.19 [-0.27, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 457.87, BIC = 480.17
- **from 3 vs from 2**: *β* = -0.37, *SE* = 0.316, *z* = -1.158, *p* = 0.247
- **from 4 vs from 2**: *β* = -0.31, *SE* = 0.313, *z* = -0.985, *p* = 0.325
- **from 5 vs from 2**: *β* = -0.68, *SE* = 0.312, *z* = -2.172, *p* = 0.030
- **from 6 vs from 2**: *β* = -0.72, *SE* = 0.314, *z* = -2.288, *p* = 0.022
- **SNR**: *β* = 0.06, *SE* = 0.027, *z* = 2.339, *p* = 0.019

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.37 | 0.32 | 1.16 | 0.247 | 0.850 | n.s. |
| from 2 - from 4 | 0.31 | 0.31 | 0.99 | 0.325 | 0.850 | n.s. |
| from 2 - from 5 | 0.68 | 0.31 | 2.17 | 0.030 | 0.239 | n.s. |
| from 2 - from 6 | 0.72 | 0.31 | 2.29 | 0.022 | 0.201 | n.s. |
| from 3 - from 4 | -0.06 | 0.31 | -0.18 | 0.855 | 0.979 | n.s. |
| from 3 - from 5 | 0.31 | 0.31 | 0.99 | 0.321 | 0.850 | n.s. |
| from 3 - from 6 | 0.35 | 0.31 | 1.13 | 0.259 | 0.850 | n.s. |
| from 4 - from 5 | 0.37 | 0.31 | 1.18 | 0.237 | 0.850 | n.s. |
| from 4 - from 6 | 0.41 | 0.31 | 1.31 | 0.189 | 0.813 | n.s. |
| from 5 - from 6 | 0.04 | 0.31 | 0.13 | 0.898 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.207, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.223 (ε = 0.707)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.78 | 23 | = 0.553 | 0.08 [-0.27, 0.58] | negligible | n.s. |
| from 2 vs from 4 | 1.06 | 23 | = 0.505 | 0.08 [-0.21, 0.64] | negligible | n.s. |
| from 2 vs from 5 | 2.36 | 23 | = 0.272 | 0.22 [0.04, 0.93] | small | n.s. |
| from 2 vs from 6 | 1.54 | 23 | = 0.410 | 0.21 [-0.12, 0.75] | small | n.s. |
| from 3 vs from 4 | -0.02 | 23 | = 0.987 | -0.00 [-0.43, 0.42] | negligible | n.s. |
| from 3 vs from 5 | 1.44 | 23 | = 0.410 | 0.13 [-0.14, 0.72] | negligible | n.s. |
| from 3 vs from 6 | 0.90 | 23 | = 0.538 | 0.13 [-0.24, 0.61] | negligible | n.s. |
| from 4 vs from 5 | 1.46 | 23 | = 0.410 | 0.14 [-0.13, 0.73] | negligible | n.s. |
| from 4 vs from 6 | 1.05 | 23 | = 0.505 | 0.13 [-0.21, 0.64] | negligible | n.s. |
| from 5 vs from 6 | -0.05 | 23 | = 0.987 | -0.01 [-0.43, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.011) (no significant pairwise comparisons)

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
