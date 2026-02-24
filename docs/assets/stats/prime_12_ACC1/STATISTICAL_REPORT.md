# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:30:14

---

## 1. Analysis Overview

**Total Measurements:** 380
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
| 1a | 24 | 75.67 ms | 28.65 | 5.85 | [32.00, 120.00] |
| 1b | 24 | 93.17 ms | 34.96 | 7.14 | [32.00, 124.00] |
| 1c | 24 | 88.17 ms | 28.66 | 5.85 | [32.00, 124.00] |
| 1d | 23 | 74.96 ms | 29.60 | 6.17 | [32.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | -3.67 µV | 2.72 | 0.56 | [-9.34, 1.01] |
| 1b | 24 | -4.83 µV | 2.96 | 0.60 | [-13.09, -0.79] |
| 1c | 24 | -3.06 µV | 3.07 | 0.63 | [-9.45, 3.76] |
| 1d | 23 | -4.33 µV | 3.41 | 0.71 | [-11.04, 0.81] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | 172.67 ms | 20.89 | 4.26 | [136.00, 208.00] |
| 1b | 24 | 170.67 ms | 19.01 | 3.88 | [144.00, 204.00] |
| 1c | 24 | 177.00 ms | 18.77 | 3.83 | [148.00, 208.00] |
| 1d | 23 | 167.48 ms | 21.69 | 4.52 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | -5.94 µV | 4.01 | 0.82 | [-14.17, 0.14] |
| 1b | 24 | -6.49 µV | 3.35 | 0.68 | [-12.80, 0.07] |
| 1c | 24 | -6.52 µV | 2.43 | 0.50 | [-12.73, -0.99] |
| 1d | 23 | -6.04 µV | 4.95 | 1.03 | [-15.24, 6.17] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | 73.83 ms | 34.95 | 7.13 | [8.00, 124.00] |
| 1b | 24 | 74.17 ms | 37.93 | 7.74 | [12.00, 124.00] |
| 1c | 24 | 78.17 ms | 37.06 | 7.56 | [16.00, 124.00] |
| 1d | 23 | 64.35 ms | 37.17 | 7.75 | [8.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | 4.74 µV | 3.14 | 0.64 | [-1.60, 14.54] |
| 1b | 24 | 4.71 µV | 2.90 | 0.59 | [0.67, 12.87] |
| 1c | 24 | 3.63 µV | 2.64 | 0.54 | [0.23, 9.85] |
| 1d | 23 | 4.89 µV | 3.64 | 0.76 | [0.02, 12.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | 456.17 ms | 9.40 | 1.92 | [448.00, 472.00] |
| 1b | 24 | 460.50 ms | 9.96 | 2.03 | [448.00, 472.00] |
| 1c | 24 | 459.17 ms | 10.61 | 2.17 | [448.00, 472.00] |
| 1d | 23 | 461.39 ms | 9.77 | 2.04 | [448.00, 472.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | 3.19 µV | 3.89 | 0.79 | [-3.84, 11.81] |
| 1b | 24 | 3.72 µV | 4.06 | 0.83 | [-6.89, 10.65] |
| 1c | 24 | 2.66 µV | 3.27 | 0.67 | [-3.15, 9.00] |
| 1d | 23 | 4.59 µV | 3.90 | 0.81 | [-4.00, 12.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 923.11, BIC = 940.99
- **1b vs 1a**: *β* = 17.48, *SE* = 8.360, *z* = 2.091, *p* = 0.037
- **1c vs 1a**: *β* = 10.96, *SE* = 8.381, *z* = 1.308, *p* = 0.191
- **1d vs 1a**: *β* = 0.81, *SE* = 8.474, *z* = 0.095, *p* = 0.924
- **SNR**: *β* = 10.37, *SE* = 4.064, *z* = 2.552, *p* = 0.011

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -17.48 | 8.36 | -2.09 | 0.037 | 0.200 | n.s. |
| 1a - 1c | -10.96 | 8.38 | -1.31 | 0.191 | 0.572 | n.s. |
| 1a - 1d | -0.81 | 8.47 | -0.10 | 0.924 | 0.924 | n.s. |
| 1b - 1c | 6.52 | 8.38 | 0.78 | 0.437 | 0.683 | n.s. |
| 1b - 1d | 16.67 | 8.47 | 1.97 | 0.049 | 0.223 | n.s. |
| 1c - 1d | 10.15 | 8.54 | 1.19 | 0.234 | 0.572 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.49, *p* = 0.226, η²_G = 0.052
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -1.32 | 22 | = 0.338 | -0.47 [-0.75, 0.11] | small | n.s. |
| 1a vs 1c | -1.25 | 22 | = 0.338 | -0.36 [-0.74, 0.12] | small | n.s. |
| 1a vs 1d | 0.21 | 22 | = 0.832 | 0.07 [-0.39, 0.48] | negligible | n.s. |
| 1b vs 1c | 0.47 | 22 | = 0.768 | 0.15 [-0.32, 0.53] | negligible | n.s. |
| 1b vs 1d | 1.86 | 22 | = 0.338 | 0.52 [-0.06, 0.84] | medium | n.s. |
| 1c vs 1d | 1.42 | 22 | = 0.338 | 0.42 [-0.15, 0.74] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 489.06, BIC = 506.94
- **1b vs 1a**: *β* = -1.16, *SE* = 0.814, *z* = -1.422, *p* = 0.155
- **1c vs 1a**: *β* = 0.70, *SE* = 0.816, *z* = 0.852, *p* = 0.394
- **1d vs 1a**: *β* = -0.73, *SE* = 0.826, *z* = -0.881, *p* = 0.378
- **SNR**: *β* = -0.54, *SE* = 0.426, *z* = -1.270, *p* = 0.204

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 1.16 | 0.81 | 1.42 | 0.155 | 0.490 | n.s. |
| 1a - 1c | -0.70 | 0.82 | -0.85 | 0.394 | 0.760 | n.s. |
| 1a - 1d | 0.73 | 0.83 | 0.88 | 0.378 | 0.760 | n.s. |
| 1b - 1c | -1.85 | 0.82 | -2.27 | 0.023 | 0.131 | n.s. |
| 1b - 1d | -0.43 | 0.83 | -0.52 | 0.603 | 0.760 | n.s. |
| 1c - 1d | 1.42 | 0.83 | 1.71 | 0.087 | 0.367 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.269, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 1.45 | 22 | = 0.480 | 0.40 [-0.12, 0.74] | small | n.s. |
| 1a vs 1c | -0.46 | 22 | = 0.651 | -0.16 [-0.55, 0.30] | negligible | n.s. |
| 1a vs 1d | 0.82 | 22 | = 0.597 | 0.22 [-0.27, 0.61] | small | n.s. |
| 1b vs 1c | -1.72 | 22 | = 0.480 | -0.53 [-0.83, 0.04] | medium | n.s. |
| 1b vs 1d | -0.69 | 22 | = 0.597 | -0.15 [-0.58, 0.29] | negligible | n.s. |
| 1c vs 1d | 1.21 | 22 | = 0.482 | 0.35 [-0.19, 0.69] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 837.90, BIC = 855.78
- **1b vs 1a**: *β* = -1.83, *SE* = 4.703, *z* = -0.389, *p* = 0.697
- **1c vs 1a**: *β* = 4.97, *SE* = 4.746, *z* = 1.048, *p* = 0.295
- **1d vs 1a**: *β* = -5.21, *SE* = 4.770, *z* = -1.092, *p* = 0.275
- **SNR**: *β* = -1.18, *SE* = 1.215, *z* = -0.971, *p* = 0.332

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 1.83 | 4.70 | 0.39 | 0.697 | 0.728 | n.s. |
| 1a - 1c | -4.97 | 4.75 | -1.05 | 0.295 | 0.724 | n.s. |
| 1a - 1d | 5.21 | 4.77 | 1.09 | 0.275 | 0.724 | n.s. |
| 1b - 1c | -6.80 | 4.72 | -1.44 | 0.150 | 0.556 | n.s. |
| 1b - 1d | 3.38 | 4.76 | 0.71 | 0.478 | 0.728 | n.s. |
| 1c - 1d | 10.18 | 4.77 | 2.13 | 0.033 | 0.182 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.49, *p* = 0.226, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.44 | 22 | = 0.665 | 0.11 [-0.34, 0.51] | negligible | n.s. |
| 1a vs 1c | -1.08 | 22 | = 0.440 | -0.23 [-0.65, 0.21] | small | n.s. |
| 1a vs 1d | 1.24 | 22 | = 0.440 | 0.27 [-0.18, 0.70] | small | n.s. |
| 1b vs 1c | -1.33 | 22 | = 0.440 | -0.35 [-0.69, 0.17] | small | n.s. |
| 1b vs 1d | 0.58 | 22 | = 0.665 | 0.17 [-0.31, 0.56] | negligible | n.s. |
| 1c vs 1d | 2.17 | 22 | = 0.247 | 0.51 [-0.00, 0.91] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 506.72, BIC = 524.60
- **1b vs 1a**: *β* = -0.42, *SE* = 0.816, *z* = -0.517, *p* = 0.605
- **1c vs 1a**: *β* = -0.08, *SE* = 0.824, *z* = -0.092, *p* = 0.927
- **1d vs 1a**: *β* = 0.20, *SE* = 0.828, *z* = 0.242, *p* = 0.809
- **SNR**: *β* = -0.93, *SE* = 0.212, *z* = -4.406, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 0.42 | 0.82 | 0.52 | 0.605 | 0.990 | n.s. |
| 1a - 1c | 0.08 | 0.82 | 0.09 | 0.927 | 0.990 | n.s. |
| 1a - 1d | -0.20 | 0.83 | -0.24 | 0.809 | 0.990 | n.s. |
| 1b - 1c | -0.35 | 0.82 | -0.42 | 0.673 | 0.990 | n.s. |
| 1b - 1d | -0.62 | 0.83 | -0.75 | 0.451 | 0.973 | n.s. |
| 1c - 1d | -0.28 | 0.83 | -0.33 | 0.739 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.17, *p* = 0.919, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.41 | 22 | = 0.997 | 0.11 [-0.30, 0.55] | negligible | n.s. |
| 1a vs 1c | 0.43 | 22 | = 0.997 | 0.12 [-0.29, 0.56] | negligible | n.s. |
| 1a vs 1d | -0.13 | 22 | = 0.997 | -0.04 [-0.46, 0.41] | negligible | n.s. |
| 1b vs 1c | -0.00 | 22 | = 0.997 | -0.00 [-0.42, 0.43] | negligible | n.s. |
| 1b vs 1d | -0.56 | 22 | = 0.997 | -0.13 [-0.55, 0.32] | negligible | n.s. |
| 1c vs 1d | -0.59 | 22 | = 0.997 | -0.14 [-0.56, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 962.54, BIC = 980.42
- **1b vs 1a**: *β* = 2.07, *SE* = 10.078, *z* = 0.206, *p* = 0.837
- **1c vs 1a**: *β* = 4.73, *SE* = 9.929, *z* = 0.477, *p* = 0.634
- **1d vs 1a**: *β* = -9.28, *SE* = 10.039, *z* = -0.924, *p* = 0.355
- **SNR**: *β* = 5.54, *SE* = 5.665, *z* = 0.978, *p* = 0.328

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -2.07 | 10.08 | -0.21 | 0.837 | 0.956 | n.s. |
| 1a - 1c | -4.73 | 9.93 | -0.48 | 0.634 | 0.951 | n.s. |
| 1a - 1d | 9.28 | 10.04 | 0.92 | 0.355 | 0.827 | n.s. |
| 1b - 1c | -2.66 | 10.01 | -0.27 | 0.790 | 0.956 | n.s. |
| 1b - 1d | 11.35 | 10.21 | 1.11 | 0.266 | 0.787 | n.s. |
| 1c - 1d | 14.01 | 10.05 | 1.39 | 0.163 | 0.657 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.50, *p* = 0.684, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.17 | 22 | = 0.866 | -0.06 [-0.43, 0.42] | negligible | n.s. |
| 1a vs 1c | -0.39 | 22 | = 0.866 | -0.12 [-0.51, 0.34] | negligible | n.s. |
| 1a vs 1d | 0.67 | 22 | = 0.866 | 0.21 [-0.29, 0.58] | small | n.s. |
| 1b vs 1c | -0.23 | 22 | = 0.866 | -0.06 [-0.51, 0.34] | negligible | n.s. |
| 1b vs 1d | 1.05 | 22 | = 0.866 | 0.26 [-0.22, 0.66] | small | n.s. |
| 1c vs 1d | 1.45 | 22 | = 0.866 | 0.32 [-0.14, 0.74] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 481.08, BIC = 498.96
- **1b vs 1a**: *β* = 0.43, *SE* = 0.775, *z* = 0.556, *p* = 0.578
- **1c vs 1a**: *β* = -1.00, *SE* = 0.763, *z* = -1.312, *p* = 0.190
- **1d vs 1a**: *β* = 0.14, *SE* = 0.772, *z* = 0.185, *p* = 0.853
- **SNR**: *β* = 1.47, *SE* = 0.440, *z* = 3.335, *p* = 0.001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -0.43 | 0.78 | -0.56 | 0.578 | 0.925 | n.s. |
| 1a - 1c | 1.00 | 0.76 | 1.31 | 0.190 | 0.568 | n.s. |
| 1a - 1d | -0.14 | 0.77 | -0.18 | 0.853 | 0.925 | n.s. |
| 1b - 1c | 1.43 | 0.77 | 1.86 | 0.063 | 0.322 | n.s. |
| 1b - 1d | 0.29 | 0.78 | 0.37 | 0.713 | 0.925 | n.s. |
| 1c - 1d | -1.14 | 0.77 | -1.48 | 0.139 | 0.526 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.85, *p* = 0.470, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.11 | 22 | = 0.914 | 0.03 [-0.41, 0.43] | negligible | n.s. |
| 1a vs 1c | 1.14 | 22 | = 0.536 | 0.37 [-0.18, 0.68] | small | n.s. |
| 1a vs 1d | -0.15 | 22 | = 0.914 | -0.04 [-0.46, 0.40] | negligible | n.s. |
| 1b vs 1c | 1.43 | 22 | = 0.536 | 0.36 [-0.11, 0.76] | small | n.s. |
| 1b vs 1d | -0.29 | 22 | = 0.914 | -0.07 [-0.49, 0.37] | negligible | n.s. |
| 1c vs 1d | -1.25 | 22 | = 0.536 | -0.38 [-0.70, 0.18] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 715.74, BIC = 733.62
- **1b vs 1a**: *β* = 4.26, *SE* = 2.810, *z* = 1.515, *p* = 0.130
- **1c vs 1a**: *β* = 2.80, *SE* = 2.834, *z* = 0.988, *p* = 0.323
- **1d vs 1a**: *β* = 5.13, *SE* = 2.843, *z* = 1.805, *p* = 0.071
- **SNR**: *β* = -0.28, *SE* = 0.559, *z* = -0.505, *p* = 0.613

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -4.26 | 2.81 | -1.52 | 0.130 | 0.501 | n.s. |
| 1a - 1c | -2.80 | 2.83 | -0.99 | 0.323 | 0.790 | n.s. |
| 1a - 1d | -5.13 | 2.84 | -1.80 | 0.071 | 0.358 | n.s. |
| 1b - 1c | 1.46 | 2.82 | 0.52 | 0.605 | 0.844 | n.s. |
| 1b - 1d | -0.87 | 2.84 | -0.31 | 0.758 | 0.844 | n.s. |
| 1c - 1d | -2.33 | 2.84 | -0.82 | 0.413 | 0.797 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.285, η²_G = 0.045
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -1.46 | 22 | = 0.479 | -0.50 [-0.70, 0.16] | medium | n.s. |
| 1a vs 1c | -0.81 | 22 | = 0.576 | -0.24 [-0.64, 0.22] | small | n.s. |
| 1a vs 1d | -1.92 | 22 | = 0.405 | -0.54 [-0.85, 0.05] | medium | n.s. |
| 1b vs 1c | 0.72 | 22 | = 0.576 | 0.24 [-0.34, 0.50] | small | n.s. |
| 1b vs 1d | -0.13 | 22 | = 0.894 | -0.04 [-0.46, 0.40] | negligible | n.s. |
| 1c vs 1d | -0.93 | 22 | = 0.576 | -0.27 [-0.63, 0.24] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 512.96, BIC = 530.84
- **1b vs 1a**: *β* = 0.75, *SE* = 0.931, *z* = 0.808, *p* = 0.419
- **1c vs 1a**: *β* = 0.07, *SE* = 0.939, *z* = 0.079, *p* = 0.937
- **1d vs 1a**: *β* = 1.71, *SE* = 0.942, *z* = 1.810, *p* = 0.070
- **SNR**: *β* = 0.86, *SE* = 0.193, *z* = 4.463, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -0.75 | 0.93 | -0.81 | 0.419 | 0.804 | n.s. |
| 1a - 1c | -0.07 | 0.94 | -0.08 | 0.937 | 0.937 | n.s. |
| 1a - 1d | -1.71 | 0.94 | -1.81 | 0.070 | 0.354 | n.s. |
| 1b - 1c | 0.68 | 0.93 | 0.73 | 0.468 | 0.804 | n.s. |
| 1b - 1d | -0.95 | 0.94 | -1.01 | 0.311 | 0.774 | n.s. |
| 1c - 1d | -1.63 | 0.94 | -1.73 | 0.084 | 0.354 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.16, *p* = 0.332, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.41 | 22 | = 0.822 | -0.12 [-0.52, 0.33] | negligible | n.s. |
| 1a vs 1c | 0.22 | 22 | = 0.826 | 0.06 [-0.32, 0.53] | negligible | n.s. |
| 1a vs 1d | -1.32 | 22 | = 0.599 | -0.40 [-0.72, 0.16] | small | n.s. |
| 1b vs 1c | 0.77 | 22 | = 0.671 | 0.19 [-0.20, 0.66] | negligible | n.s. |
| 1b vs 1d | -1.05 | 22 | = 0.612 | -0.27 [-0.66, 0.22] | small | n.s. |
| 1c vs 1d | -2.01 | 22 | = 0.342 | -0.50 [-0.87, 0.03] | small | n.s. |

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
