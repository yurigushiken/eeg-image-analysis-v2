# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:40:05

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
| 3 to 1 | 14 | 106.86 ms | 10.34 | 2.76 | [88.00, 116.00] |
| 3 to 2 | 13 | 104.31 ms | 8.71 | 2.42 | [92.00, 116.00] |
| 3 to 4 | 15 | 103.73 ms | 11.66 | 3.01 | [88.00, 116.00] |
| 3 to 5 | 17 | 104.47 ms | 8.93 | 2.17 | [88.00, 116.00] |
| 3 to 6 | 14 | 100.29 ms | 10.10 | 2.70 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 14 | -2.61 µV | 1.68 | 0.45 | [-6.18, -1.03] |
| 3 to 2 | 13 | -2.78 µV | 1.64 | 0.45 | [-5.65, -0.61] |
| 3 to 4 | 15 | -2.50 µV | 1.49 | 0.39 | [-5.42, -0.95] |
| 3 to 5 | 17 | -2.77 µV | 1.24 | 0.30 | [-4.95, -0.87] |
| 3 to 6 | 14 | -3.13 µV | 1.25 | 0.33 | [-4.88, -1.00] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 19 | 182.32 ms | 15.74 | 3.61 | [156.00, 208.00] |
| 3 to 2 | 24 | 175.33 ms | 22.28 | 4.55 | [140.00, 208.00] |
| 3 to 4 | 22 | 164.18 ms | 16.54 | 3.53 | [140.00, 204.00] |
| 3 to 5 | 22 | 167.82 ms | 21.15 | 4.51 | [140.00, 208.00] |
| 3 to 6 | 23 | 170.43 ms | 19.29 | 4.02 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 19 | -4.55 µV | 2.51 | 0.58 | [-10.41, -1.36] |
| 3 to 2 | 24 | -5.77 µV | 2.55 | 0.52 | [-10.33, -1.35] |
| 3 to 4 | 22 | -5.67 µV | 2.24 | 0.48 | [-10.31, -2.95] |
| 3 to 5 | 22 | -5.54 µV | 2.45 | 0.52 | [-11.97, -1.70] |
| 3 to 6 | 23 | -6.82 µV | 2.82 | 0.59 | [-12.81, -2.56] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 108.44 ms | 8.56 | 2.02 | [88.00, 116.00] |
| 3 to 2 | 11 | 101.82 ms | 9.53 | 2.87 | [88.00, 116.00] |
| 3 to 4 | 16 | 101.25 ms | 11.19 | 2.80 | [88.00, 116.00] |
| 3 to 5 | 14 | 103.71 ms | 10.22 | 2.73 | [88.00, 116.00] |
| 3 to 6 | 10 | 102.40 ms | 8.68 | 2.75 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 3.44 µV | 1.98 | 0.47 | [0.91, 9.14] |
| 3 to 2 | 11 | 2.59 µV | 1.70 | 0.51 | [0.60, 5.36] |
| 3 to 4 | 16 | 3.22 µV | 1.98 | 0.49 | [0.44, 7.39] |
| 3 to 5 | 14 | 3.17 µV | 1.25 | 0.33 | [1.48, 5.64] |
| 3 to 6 | 10 | 3.66 µV | 2.12 | 0.67 | [1.16, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 481.40 ms | 26.92 | 6.02 | [448.00, 540.00] |
| 3 to 2 | 18 | 486.00 ms | 33.92 | 8.00 | [432.00, 540.00] |
| 3 to 4 | 17 | 488.71 ms | 42.41 | 10.29 | [428.00, 540.00] |
| 3 to 5 | 16 | 485.50 ms | 37.94 | 9.49 | [428.00, 540.00] |
| 3 to 6 | 20 | 483.20 ms | 38.42 | 8.59 | [428.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 5.75 µV | 3.05 | 0.68 | [0.90, 14.34] |
| 3 to 2 | 18 | 6.50 µV | 4.11 | 0.97 | [2.10, 17.81] |
| 3 to 4 | 17 | 6.11 µV | 3.26 | 0.79 | [1.82, 13.58] |
| 3 to 5 | 16 | 6.36 µV | 3.29 | 0.82 | [2.79, 15.40] |
| 3 to 6 | 20 | 4.76 µV | 2.30 | 0.51 | [1.70, 10.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.65, BIC = 568.97
- **3 to 2 vs 3 to 1**: *β* = -3.93, *SE* = 3.525, *z* = -1.116, *p* = 0.264
- **3 to 4 vs 3 to 1**: *β* = -3.30, *SE* = 3.326, *z* = -0.991, *p* = 0.322
- **3 to 5 vs 3 to 1**: *β* = -3.51, *SE* = 3.294, *z* = -1.066, *p* = 0.286
- **3 to 6 vs 3 to 1**: *β* = -7.54, *SE* = 3.431, *z* = -2.199, *p* = 0.028
- **SNR**: *β* = 0.70, *SE* = 0.794, *z* = 0.882, *p* = 0.378

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 3.93 | 3.52 | 1.12 | 0.264 | 0.883 | n.s. |
| 3 to 1 - 3 to 4 | 3.30 | 3.33 | 0.99 | 0.322 | 0.883 | n.s. |
| 3 to 1 - 3 to 5 | 3.51 | 3.29 | 1.07 | 0.286 | 0.883 | n.s. |
| 3 to 1 - 3 to 6 | 7.55 | 3.43 | 2.20 | 0.028 | 0.246 | n.s. |
| 3 to 2 - 3 to 4 | -0.64 | 3.43 | -0.19 | 0.852 | 0.997 | n.s. |
| 3 to 2 - 3 to 5 | -0.42 | 3.31 | -0.13 | 0.898 | 0.997 | n.s. |
| 3 to 2 - 3 to 6 | 3.61 | 3.43 | 1.05 | 0.292 | 0.883 | n.s. |
| 3 to 4 - 3 to 5 | 0.22 | 3.23 | 0.07 | 0.947 | 0.997 | n.s. |
| 3 to 4 - 3 to 6 | 4.25 | 3.36 | 1.27 | 0.206 | 0.874 | n.s. |
| 3 to 5 - 3 to 6 | 4.03 | 3.25 | 1.24 | 0.215 | 0.874 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.57, *p* = 0.689, η²_G = 0.077
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 1.41 | 3 | = 0.841 | 0.41 [-0.68, 1.00] | small | n.s. |
| 3 to 1 vs 3 to 4 | -0.40 | 3 | = 0.889 | -0.22 [-0.88, 0.66] | small | n.s. |
| 3 to 1 vs 3 to 5 | 0.68 | 3 | = 0.889 | 0.32 [-0.54, 0.81] | small | n.s. |
| 3 to 1 vs 3 to 6 | 0.91 | 3 | = 0.889 | 0.49 [-0.02, 2.04] | small | n.s. |
| 3 to 2 vs 3 to 4 | -1.73 | 3 | = 0.841 | -0.57 [-0.82, 0.61] | medium | n.s. |
| 3 to 2 vs 3 to 5 | -0.15 | 3 | = 0.889 | -0.09 [-0.87, 0.57] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 0.29 | 3 | = 0.889 | 0.09 [-0.46, 1.00] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | 0.59 | 3 | = 0.889 | 0.49 [-0.47, 0.89] | small | n.s. |
| 3 to 4 vs 3 to 6 | 2.78 | 3 | = 0.689 | 0.64 [-0.47, 1.10] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 0.24 | 3 | = 0.889 | 0.18 [-0.33, 1.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 243.19, BIC = 261.51
- **3 to 2 vs 3 to 1**: *β* = 0.42, *SE* = 0.418, *z* = 1.005, *p* = 0.315
- **3 to 4 vs 3 to 1**: *β* = 0.32, *SE* = 0.394, *z* = 0.807, *p* = 0.420
- **3 to 5 vs 3 to 1**: *β* = 0.46, *SE* = 0.390, *z* = 1.174, *p* = 0.240
- **3 to 6 vs 3 to 1**: *β* = -0.02, *SE* = 0.403, *z* = -0.039, *p* = 0.969
- **SNR**: *β* = -0.57, *SE* = 0.099, *z* = -5.792, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -0.42 | 0.42 | -1.01 | 0.315 | 0.929 | n.s. |
| 3 to 1 - 3 to 4 | -0.32 | 0.39 | -0.81 | 0.420 | 0.952 | n.s. |
| 3 to 1 - 3 to 5 | -0.46 | 0.39 | -1.17 | 0.240 | 0.916 | n.s. |
| 3 to 1 - 3 to 6 | 0.02 | 0.40 | 0.04 | 0.969 | 0.994 | n.s. |
| 3 to 2 - 3 to 4 | 0.10 | 0.40 | 0.26 | 0.798 | 0.993 | n.s. |
| 3 to 2 - 3 to 5 | -0.04 | 0.39 | -0.10 | 0.923 | 0.994 | n.s. |
| 3 to 2 - 3 to 6 | 0.44 | 0.40 | 1.08 | 0.278 | 0.926 | n.s. |
| 3 to 4 - 3 to 5 | -0.14 | 0.38 | -0.37 | 0.712 | 0.993 | n.s. |
| 3 to 4 - 3 to 6 | 0.33 | 0.39 | 0.85 | 0.397 | 0.952 | n.s. |
| 3 to 5 - 3 to 6 | 0.47 | 0.38 | 1.23 | 0.218 | 0.915 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.53, *p* = 0.716, η²_G = 0.132
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.61 | 3 | = 0.831 | -0.39 [-0.85, 0.82] | small | n.s. |
| 3 to 1 vs 3 to 4 | -1.84 | 3 | = 0.831 | -0.65 [-1.44, 0.23] | medium | n.s. |
| 3 to 1 vs 3 to 5 | -0.90 | 3 | = 0.831 | -0.65 [-0.79, 0.56] | medium | n.s. |
| 3 to 1 vs 3 to 6 | -0.09 | 3 | = 0.935 | -0.08 [-0.72, 0.96] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | -0.59 | 3 | = 0.831 | -0.45 [-0.76, 0.67] | small | n.s. |
| 3 to 2 vs 3 to 5 | -0.48 | 3 | = 0.831 | -0.44 [-0.83, 0.61] | small | n.s. |
| 3 to 2 vs 3 to 6 | 0.64 | 3 | = 0.831 | 0.50 [-0.40, 1.08] | small | n.s. |
| 3 to 4 vs 3 to 5 | 0.09 | 3 | = 0.935 | 0.07 [-0.68, 0.66] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.82 | 3 | = 0.831 | 0.77 [-0.69, 0.85] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 1.26 | 3 | = 0.831 | 0.81 [-0.83, 0.71] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 953.38, BIC = 974.99
- **3 to 2 vs 3 to 1**: *β* = -6.08, *SE* = 4.798, *z* = -1.267, *p* = 0.205
- **3 to 4 vs 3 to 1**: *β* = -16.16, *SE* = 4.734, *z* = -3.414, *p* = 0.001
- **3 to 5 vs 3 to 1**: *β* = -12.54, *SE* = 4.729, *z* = -2.653, *p* = 0.008
- **3 to 6 vs 3 to 1**: *β* = -10.05, *SE* = 4.966, *z* = -2.024, *p* = 0.043
- **SNR**: *β* = -0.40, *SE* = 0.685, *z* = -0.583, *p* = 0.560

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 6.08 | 4.80 | 1.27 | 0.205 | 0.621 | n.s. |
| 3 to 1 - 3 to 4 | 16.16 | 4.73 | 3.41 | < .001 | 0.006 | ** |
| 3 to 1 - 3 to 5 | 12.54 | 4.73 | 2.65 | 0.008 | 0.070 | n.s. |
| 3 to 1 - 3 to 6 | 10.05 | 4.97 | 2.02 | 0.043 | 0.265 | n.s. |
| 3 to 2 - 3 to 4 | 10.08 | 4.43 | 2.28 | 0.023 | 0.169 | n.s. |
| 3 to 2 - 3 to 5 | 6.47 | 4.44 | 1.46 | 0.145 | 0.610 | n.s. |
| 3 to 2 - 3 to 6 | 3.97 | 4.32 | 0.92 | 0.358 | 0.735 | n.s. |
| 3 to 4 - 3 to 5 | -3.62 | 4.43 | -0.82 | 0.415 | 0.735 | n.s. |
| 3 to 4 - 3 to 6 | -6.11 | 4.52 | -1.35 | 0.176 | 0.621 | n.s. |
| 3 to 5 - 3 to 6 | -2.49 | 4.53 | -0.55 | 0.582 | 0.735 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.47, *p* = 0.012, η²_G = 0.083
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 1.95 | 17 | = 0.169 | 0.50 [-0.06, 0.95] | small | n.s. |
| 3 to 1 vs 3 to 4 | 3.76 | 17 | = 0.013 | 0.96 [0.30, 1.47] | large | * |
| 3 to 1 vs 3 to 5 | 3.53 | 17 | = 0.013 | 0.71 [0.25, 1.41] | medium | * |
| 3 to 1 vs 3 to 6 | 2.18 | 17 | = 0.144 | 0.65 [-0.01, 1.04] | medium | n.s. |
| 3 to 2 vs 3 to 4 | 1.43 | 17 | = 0.344 | 0.39 [-0.07, 0.85] | small | n.s. |
| 3 to 2 vs 3 to 5 | 1.09 | 17 | = 0.482 | 0.23 [-0.25, 0.64] | small | n.s. |
| 3 to 2 vs 3 to 6 | 0.60 | 17 | = 0.680 | 0.14 [-0.25, 0.62] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.42 | 17 | = 0.680 | -0.12 [-0.59, 0.30] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -0.98 | 17 | = 0.487 | -0.25 [-0.72, 0.18] | small | n.s. |
| 3 to 5 vs 3 to 6 | -0.46 | 17 | = 0.680 | -0.10 [-0.48, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 443.62, BIC = 465.22
- **3 to 2 vs 3 to 1**: *β* = -0.21, *SE* = 0.459, *z* = -0.458, *p* = 0.647
- **3 to 4 vs 3 to 1**: *β* = -0.54, *SE* = 0.451, *z* = -1.186, *p* = 0.236
- **3 to 5 vs 3 to 1**: *β* = -0.43, *SE* = 0.450, *z* = -0.957, *p* = 0.339
- **3 to 6 vs 3 to 1**: *β* = -0.96, *SE* = 0.475, *z* = -2.011, *p* = 0.044
- **SNR**: *β* = -0.53, *SE* = 0.067, *z* = -7.943, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.21 | 0.46 | 0.46 | 0.647 | 0.936 | n.s. |
| 3 to 1 - 3 to 4 | 0.53 | 0.45 | 1.19 | 0.236 | 0.868 | n.s. |
| 3 to 1 - 3 to 5 | 0.43 | 0.45 | 0.96 | 0.339 | 0.908 | n.s. |
| 3 to 1 - 3 to 6 | 0.96 | 0.48 | 2.01 | 0.044 | 0.364 | n.s. |
| 3 to 2 - 3 to 4 | 0.32 | 0.42 | 0.77 | 0.441 | 0.908 | n.s. |
| 3 to 2 - 3 to 5 | 0.22 | 0.42 | 0.52 | 0.601 | 0.936 | n.s. |
| 3 to 2 - 3 to 6 | 0.75 | 0.41 | 1.82 | 0.069 | 0.476 | n.s. |
| 3 to 4 - 3 to 5 | -0.10 | 0.42 | -0.25 | 0.806 | 0.936 | n.s. |
| 3 to 4 - 3 to 6 | 0.42 | 0.43 | 0.98 | 0.328 | 0.908 | n.s. |
| 3 to 5 - 3 to 6 | 0.53 | 0.43 | 1.22 | 0.223 | 0.868 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.39, *p* = 0.014, η²_G = 0.073
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 2.16 | 17 | = 0.117 | 0.61 [0.01, 1.04] | medium | n.s. |
| 3 to 1 vs 3 to 4 | 2.14 | 17 | = 0.117 | 0.50 [-0.02, 1.03] | small | n.s. |
| 3 to 1 vs 3 to 5 | 1.18 | 17 | = 0.398 | 0.34 [-0.23, 0.79] | small | n.s. |
| 3 to 1 vs 3 to 6 | 2.66 | 17 | = 0.117 | 0.78 [0.08, 1.17] | medium | n.s. |
| 3 to 2 vs 3 to 4 | -0.83 | 17 | = 0.465 | -0.16 [-0.59, 0.30] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -1.12 | 17 | = 0.398 | -0.27 [-0.60, 0.30] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.00 | 17 | = 0.412 | 0.19 [-0.03, 0.87] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.58 | 17 | = 0.573 | -0.13 [-0.50, 0.39] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.96 | 17 | = 0.134 | 0.35 [0.09, 1.05] | small | n.s. |
| 3 to 5 vs 3 to 6 | 2.48 | 17 | = 0.117 | 0.45 [0.14, 1.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 515.64, BIC = 533.52
- **3 to 2 vs 3 to 1**: *β* = -6.71, *SE* = 3.311, *z* = -2.027, *p* = 0.043
- **3 to 4 vs 3 to 1**: *β* = -6.56, *SE* = 2.986, *z* = -2.197, *p* = 0.028
- **3 to 5 vs 3 to 1**: *β* = -5.54, *SE* = 3.067, *z* = -1.805, *p* = 0.071
- **3 to 6 vs 3 to 1**: *β* = -6.27, *SE* = 3.448, *z* = -1.817, *p* = 0.069
- **SNR**: *β* = 0.93, *SE* = 0.608, *z* = 1.526, *p* = 0.127

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 6.71 | 3.31 | 2.03 | 0.043 | 0.324 | n.s. |
| 3 to 1 - 3 to 4 | 6.56 | 2.99 | 2.20 | 0.028 | 0.247 | n.s. |
| 3 to 1 - 3 to 5 | 5.54 | 3.07 | 1.81 | 0.071 | 0.436 | n.s. |
| 3 to 1 - 3 to 6 | 6.27 | 3.45 | 1.82 | 0.069 | 0.436 | n.s. |
| 3 to 2 - 3 to 4 | -0.15 | 3.43 | -0.04 | 0.965 | 1.000 | n.s. |
| 3 to 2 - 3 to 5 | -1.17 | 3.54 | -0.33 | 0.740 | 1.000 | n.s. |
| 3 to 2 - 3 to 6 | -0.45 | 3.88 | -0.11 | 0.909 | 1.000 | n.s. |
| 3 to 4 - 3 to 5 | -1.02 | 3.22 | -0.32 | 0.751 | 1.000 | n.s. |
| 3 to 4 - 3 to 6 | -0.29 | 3.59 | -0.08 | 0.935 | 1.000 | n.s. |
| 3 to 5 - 3 to 6 | 0.73 | 3.67 | 0.20 | 0.842 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.799, η²_G = 0.160
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.76 | 2 | = 0.780 | -0.77 [-0.34, 1.05] | medium | n.s. |
| 3 to 1 vs 3 to 4 | -0.57 | 2 | = 0.780 | -0.62 [-0.47, 0.89] | medium | n.s. |
| 3 to 1 vs 3 to 5 | -0.69 | 2 | = 0.780 | -0.74 [-0.31, 1.00] | medium | n.s. |
| 3 to 1 vs 3 to 6 | -0.31 | 2 | = 0.872 | -0.35 [-0.67, 0.87] | small | n.s. |
| 3 to 2 vs 3 to 4 | 1.00 | 2 | = 0.780 | 0.25 [-1.19, 0.53] | small | n.s. |
| 3 to 2 vs 3 to 5 | 0.00 | 2 | = 1.000 | 0.00 [-1.46, 0.50] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 1.73 | 2 | = 0.751 | 0.59 [-0.98, 0.70] | medium | n.s. |
| 3 to 4 vs 3 to 5 | -1.00 | 2 | = 0.780 | -0.22 [-1.01, 0.54] | small | n.s. |
| 3 to 4 vs 3 to 6 | 2.00 | 2 | = 0.751 | 0.37 [-0.79, 1.36] | small | n.s. |
| 3 to 5 vs 3 to 6 | 1.73 | 2 | = 0.751 | 0.55 [-1.35, 1.14] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 241.03, BIC = 258.90
- **3 to 2 vs 3 to 1**: *β* = -0.63, *SE* = 0.407, *z* = -1.555, *p* = 0.120
- **3 to 4 vs 3 to 1**: *β* = 0.13, *SE* = 0.376, *z* = 0.352, *p* = 0.724
- **3 to 5 vs 3 to 1**: *β* = -0.79, *SE* = 0.380, *z* = -2.075, *p* = 0.038
- **3 to 6 vs 3 to 1**: *β* = -0.14, *SE* = 0.428, *z* = -0.327, *p* = 0.744
- **SNR**: *β* = 0.58, *SE* = 0.077, *z* = 7.540, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.63 | 0.41 | 1.55 | 0.120 | 0.591 | n.s. |
| 3 to 1 - 3 to 4 | -0.13 | 0.38 | -0.35 | 0.724 | 0.979 | n.s. |
| 3 to 1 - 3 to 5 | 0.79 | 0.38 | 2.07 | 0.038 | 0.294 | n.s. |
| 3 to 1 - 3 to 6 | 0.14 | 0.43 | 0.33 | 0.744 | 0.979 | n.s. |
| 3 to 2 - 3 to 4 | -0.76 | 0.43 | -1.80 | 0.072 | 0.452 | n.s. |
| 3 to 2 - 3 to 5 | 0.16 | 0.44 | 0.35 | 0.725 | 0.979 | n.s. |
| 3 to 2 - 3 to 6 | -0.49 | 0.47 | -1.05 | 0.296 | 0.827 | n.s. |
| 3 to 4 - 3 to 5 | 0.92 | 0.41 | 2.27 | 0.024 | 0.212 | n.s. |
| 3 to 4 - 3 to 6 | 0.27 | 0.45 | 0.60 | 0.547 | 0.958 | n.s. |
| 3 to 5 - 3 to 6 | -0.65 | 0.46 | -1.40 | 0.163 | 0.655 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.288, η²_G = 0.317
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.79 | 2 | = 0.538 | -2.06 [-0.39, 0.98] | large | n.s. |
| 3 to 1 vs 3 to 4 | -2.09 | 2 | = 0.538 | -1.42 [-0.71, 0.64] | large | n.s. |
| 3 to 1 vs 3 to 5 | -6.47 | 2 | = 0.231 | -1.98 [-0.47, 0.80] | large | n.s. |
| 3 to 1 vs 3 to 6 | -2.55 | 2 | = 0.538 | -1.45 [-1.22, 0.39] | large | n.s. |
| 3 to 2 vs 3 to 4 | -0.44 | 2 | = 0.813 | -0.42 [-1.52, 0.30] | small | n.s. |
| 3 to 2 vs 3 to 5 | -0.31 | 2 | = 0.813 | -0.34 [-1.07, 0.79] | small | n.s. |
| 3 to 2 vs 3 to 6 | -0.51 | 2 | = 0.813 | -0.52 [-1.20, 0.52] | medium | n.s. |
| 3 to 4 vs 3 to 5 | 0.27 | 2 | = 0.813 | 0.19 [-0.17, 1.53] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -0.28 | 2 | = 0.813 | -0.11 [-1.29, 0.84] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | -0.64 | 2 | = 0.813 | -0.31 [-1.47, 1.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 916.21, BIC = 936.30
- **3 to 2 vs 3 to 1**: *β* = 2.78, *SE* = 10.554, *z* = 0.263, *p* = 0.792
- **3 to 4 vs 3 to 1**: *β* = 7.45, *SE* = 10.597, *z* = 0.703, *p* = 0.482
- **3 to 5 vs 3 to 1**: *β* = 5.81, *SE* = 10.761, *z* = 0.540, *p* = 0.589
- **3 to 6 vs 3 to 1**: *β* = -0.31, *SE* = 10.514, *z* = -0.030, *p* = 0.976
- **SNR**: *β* = -0.06, *SE* = 0.766, *z* = -0.078, *p* = 0.938

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -2.78 | 10.55 | -0.26 | 0.792 | 0.999 | n.s. |
| 3 to 1 - 3 to 4 | -7.45 | 10.60 | -0.70 | 0.482 | 0.998 | n.s. |
| 3 to 1 - 3 to 5 | -5.81 | 10.76 | -0.54 | 0.589 | 0.999 | n.s. |
| 3 to 1 - 3 to 6 | 0.31 | 10.51 | 0.03 | 0.976 | 0.999 | n.s. |
| 3 to 2 - 3 to 4 | -4.67 | 10.68 | -0.44 | 0.662 | 0.999 | n.s. |
| 3 to 2 - 3 to 5 | -3.03 | 10.93 | -0.28 | 0.781 | 0.999 | n.s. |
| 3 to 2 - 3 to 6 | 3.09 | 10.22 | 0.30 | 0.762 | 0.999 | n.s. |
| 3 to 4 - 3 to 5 | 1.64 | 10.97 | 0.15 | 0.882 | 0.999 | n.s. |
| 3 to 4 - 3 to 6 | 7.76 | 10.50 | 0.74 | 0.460 | 0.998 | n.s. |
| 3 to 5 - 3 to 6 | 6.12 | 10.76 | 0.57 | 0.569 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.967, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.31 | 10 | = 0.958 | -0.11 [-0.55, 0.48] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | -0.57 | 10 | = 0.958 | -0.24 [-0.78, 0.34] | small | n.s. |
| 3 to 1 vs 3 to 5 | -0.58 | 10 | = 0.958 | -0.30 [-0.69, 0.42] | small | n.s. |
| 3 to 1 vs 3 to 6 | -0.37 | 10 | = 0.958 | -0.16 [-0.51, 0.49] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | -0.37 | 10 | = 0.958 | -0.14 [-0.68, 0.43] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -0.47 | 10 | = 0.958 | -0.17 [-0.81, 0.36] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | -0.21 | 10 | = 0.958 | -0.06 [-0.39, 0.64] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.05 | 10 | = 0.958 | -0.02 [-0.58, 0.58] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.16 | 10 | = 0.958 | 0.07 [-0.42, 0.65] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.21 | 10 | = 0.958 | 0.09 [-0.40, 0.71] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 427.08, BIC = 447.17
- **3 to 2 vs 3 to 1**: *β* = 1.56, *SE* = 0.643, *z* = 2.427, *p* = 0.015
- **3 to 4 vs 3 to 1**: *β* = 0.59, *SE* = 0.650, *z* = 0.915, *p* = 0.360
- **3 to 5 vs 3 to 1**: *β* = 0.77, *SE* = 0.657, *z* = 1.174, *p* = 0.240
- **3 to 6 vs 3 to 1**: *β* = 0.03, *SE* = 0.641, *z* = 0.045, *p* = 0.964
- **SNR**: *β* = 0.21, *SE* = 0.050, *z* = 4.329, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -1.56 | 0.64 | -2.43 | 0.015 | 0.129 | n.s. |
| 3 to 1 - 3 to 4 | -0.59 | 0.65 | -0.91 | 0.360 | 0.843 | n.s. |
| 3 to 1 - 3 to 5 | -0.77 | 0.66 | -1.17 | 0.240 | 0.843 | n.s. |
| 3 to 1 - 3 to 6 | -0.03 | 0.64 | -0.04 | 0.964 | 0.964 | n.s. |
| 3 to 2 - 3 to 4 | 0.97 | 0.65 | 1.50 | 0.135 | 0.686 | n.s. |
| 3 to 2 - 3 to 5 | 0.79 | 0.66 | 1.19 | 0.232 | 0.843 | n.s. |
| 3 to 2 - 3 to 6 | 1.53 | 0.62 | 2.48 | 0.013 | 0.125 | n.s. |
| 3 to 4 - 3 to 5 | -0.18 | 0.66 | -0.27 | 0.789 | 0.955 | n.s. |
| 3 to 4 - 3 to 6 | 0.57 | 0.63 | 0.89 | 0.373 | 0.843 | n.s. |
| 3 to 5 - 3 to 6 | 0.74 | 0.65 | 1.15 | 0.252 | 0.843 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.401, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.29 | 10 | = 0.734 | -0.43 [-0.75, 0.29] | small | n.s. |
| 3 to 1 vs 3 to 4 | -0.43 | 10 | = 0.849 | -0.13 [-0.56, 0.55] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | -0.50 | 10 | = 0.849 | -0.11 [-0.59, 0.52] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 0.30 | 10 | = 0.856 | 0.10 [-0.22, 0.79] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 1.01 | 10 | = 0.734 | 0.32 [-0.26, 0.87] | small | n.s. |
| 3 to 2 vs 3 to 5 | 1.12 | 10 | = 0.734 | 0.32 [-0.29, 0.89] | small | n.s. |
| 3 to 2 vs 3 to 6 | 2.46 | 10 | = 0.337 | 0.61 [0.11, 1.26] | medium | n.s. |
| 3 to 4 vs 3 to 5 | 0.03 | 10 | = 0.974 | 0.01 [-0.63, 0.53] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.91 | 10 | = 0.734 | 0.27 [-0.12, 0.99] | small | n.s. |
| 3 to 5 vs 3 to 6 | 0.80 | 10 | = 0.734 | 0.24 [-0.15, 1.01] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.012). Post-hoc tests revealed:
  - 3 to 1 showed greater latency than 3 to 4 (*d* = 0.96)
  - 3 to 1 showed greater latency than 3 to 5 (*d* = 0.71)
**N1 amplitude:** Significant main effect of condition (*p* = 0.014) (no significant pairwise comparisons)

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
