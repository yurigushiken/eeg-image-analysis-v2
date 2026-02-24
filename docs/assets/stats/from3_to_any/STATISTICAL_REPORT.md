# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:20:34

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
| 3 to 1 | 24 | 105.17 ms | 11.03 | 2.25 | [88.00, 116.00] |
| 3 to 2 | 24 | 103.83 ms | 10.84 | 2.21 | [88.00, 116.00] |
| 3 to 4 | 24 | 103.67 ms | 10.74 | 2.19 | [88.00, 116.00] |
| 3 to 5 | 24 | 102.67 ms | 10.05 | 2.05 | [88.00, 116.00] |
| 3 to 6 | 24 | 101.17 ms | 11.16 | 2.28 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -1.72 µV | 1.96 | 0.40 | [-6.18, 1.52] |
| 3 to 2 | 24 | -1.25 µV | 2.20 | 0.45 | [-5.65, 2.93] |
| 3 to 4 | 24 | -1.66 µV | 1.73 | 0.35 | [-5.42, 1.50] |
| 3 to 5 | 24 | -1.79 µV | 2.02 | 0.41 | [-4.95, 2.58] |
| 3 to 6 | 24 | -1.76 µV | 2.37 | 0.48 | [-4.88, 4.55] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 181.50 ms | 14.72 | 3.01 | [156.00, 208.00] |
| 3 to 2 | 24 | 175.33 ms | 22.28 | 4.55 | [140.00, 208.00] |
| 3 to 4 | 24 | 167.67 ms | 19.73 | 4.03 | [140.00, 208.00] |
| 3 to 5 | 24 | 170.67 ms | 22.46 | 4.59 | [140.00, 208.00] |
| 3 to 6 | 24 | 172.00 ms | 20.36 | 4.16 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -3.92 µV | 2.56 | 0.52 | [-10.41, -0.72] |
| 3 to 2 | 24 | -5.77 µV | 2.55 | 0.52 | [-10.33, -1.35] |
| 3 to 4 | 24 | -5.39 µV | 2.45 | 0.50 | [-10.31, 0.18] |
| 3 to 5 | 24 | -5.20 µV | 2.65 | 0.54 | [-11.97, 0.09] |
| 3 to 6 | 24 | -6.66 µV | 2.86 | 0.58 | [-12.81, -2.56] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 108.00 ms | 10.01 | 2.04 | [88.00, 116.00] |
| 3 to 2 | 24 | 102.67 ms | 11.35 | 2.32 | [88.00, 116.00] |
| 3 to 4 | 24 | 101.67 ms | 11.31 | 2.31 | [88.00, 116.00] |
| 3 to 5 | 24 | 102.00 ms | 11.25 | 2.30 | [88.00, 116.00] |
| 3 to 6 | 24 | 100.67 ms | 10.40 | 2.12 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 2.80 µV | 2.09 | 0.43 | [-0.93, 9.14] |
| 3 to 2 | 24 | 0.80 µV | 2.26 | 0.46 | [-3.61, 5.36] |
| 3 to 4 | 24 | 2.26 µV | 2.18 | 0.44 | [-0.59, 7.39] |
| 3 to 5 | 24 | 1.64 µV | 2.29 | 0.47 | [-2.94, 5.64] |
| 3 to 6 | 24 | 1.54 µV | 2.51 | 0.51 | [-2.13, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 479.17 ms | 30.71 | 6.27 | [428.00, 540.00] |
| 3 to 2 | 24 | 485.83 ms | 36.01 | 7.35 | [432.00, 540.00] |
| 3 to 4 | 24 | 487.83 ms | 41.06 | 8.38 | [428.00, 540.00] |
| 3 to 5 | 24 | 483.50 ms | 39.76 | 8.12 | [428.00, 540.00] |
| 3 to 6 | 24 | 488.00 ms | 41.82 | 8.54 | [428.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 4.85 µV | 3.47 | 0.71 | [-0.59, 14.34] |
| 3 to 2 | 24 | 5.05 µV | 4.52 | 0.92 | [-2.08, 17.81] |
| 3 to 4 | 24 | 4.02 µV | 4.39 | 0.90 | [-3.98, 13.58] |
| 3 to 5 | 24 | 4.20 µV | 4.28 | 0.87 | [-2.99, 15.40] |
| 3 to 6 | 24 | 3.97 µV | 2.93 | 0.60 | [-3.66, 10.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 914.23, BIC = 936.53
- **3 to 2 vs 3 to 1**: *β* = -1.69, *SE* = 2.759, *z* = -0.612, *p* = 0.540
- **3 to 4 vs 3 to 1**: *β* = -1.39, *SE* = 2.741, *z* = -0.507, *p* = 0.612
- **3 to 5 vs 3 to 1**: *β* = -2.97, *SE* = 2.773, *z* = -1.070, *p* = 0.285
- **3 to 6 vs 3 to 1**: *β* = -4.35, *SE* = 2.758, *z* = -1.578, *p* = 0.115
- **SNR**: *β* = 0.74, *SE* = 0.683, *z* = 1.078, *p* = 0.281

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 1.69 | 2.76 | 0.61 | 0.540 | 0.991 | n.s. |
| 3 to 1 - 3 to 4 | 1.39 | 2.74 | 0.51 | 0.612 | 0.991 | n.s. |
| 3 to 1 - 3 to 5 | 2.97 | 2.77 | 1.07 | 0.285 | 0.951 | n.s. |
| 3 to 1 - 3 to 6 | 4.35 | 2.76 | 1.58 | 0.115 | 0.704 | n.s. |
| 3 to 2 - 3 to 4 | -0.30 | 2.77 | -0.11 | 0.914 | 0.991 | n.s. |
| 3 to 2 - 3 to 5 | 1.28 | 2.74 | 0.47 | 0.641 | 0.991 | n.s. |
| 3 to 2 - 3 to 6 | 2.66 | 2.74 | 0.97 | 0.331 | 0.951 | n.s. |
| 3 to 4 - 3 to 5 | 1.58 | 2.79 | 0.56 | 0.572 | 0.991 | n.s. |
| 3 to 4 - 3 to 6 | 2.96 | 2.77 | 1.07 | 0.285 | 0.951 | n.s. |
| 3 to 5 - 3 to 6 | 1.39 | 2.74 | 0.51 | 0.613 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.56, *p* = 0.690, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 0.40 | 23 | = 0.773 | 0.12 [-0.34, 0.50] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | 0.58 | 23 | = 0.773 | 0.14 [-0.31, 0.54] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | 0.85 | 23 | = 0.773 | 0.24 [-0.25, 0.60] | small | n.s. |
| 3 to 1 vs 3 to 6 | 1.15 | 23 | = 0.773 | 0.36 [-0.19, 0.66] | small | n.s. |
| 3 to 2 vs 3 to 4 | 0.06 | 23 | = 0.956 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.43 | 23 | = 0.773 | 0.11 [-0.34, 0.51] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 0.98 | 23 | = 0.773 | 0.24 [-0.23, 0.63] | small | n.s. |
| 3 to 4 vs 3 to 5 | 0.44 | 23 | = 0.773 | 0.10 [-0.33, 0.51] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.07 | 23 | = 0.773 | 0.23 [-0.21, 0.64] | small | n.s. |
| 3 to 5 vs 3 to 6 | 0.65 | 23 | = 0.773 | 0.14 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 512.33, BIC = 534.63
- **3 to 2 vs 3 to 1**: *β* = 0.54, *SE* = 0.502, *z* = 1.065, *p* = 0.287
- **3 to 4 vs 3 to 1**: *β* = 0.03, *SE* = 0.499, *z* = 0.069, *p* = 0.945
- **3 to 5 vs 3 to 1**: *β* = 0.02, *SE* = 0.505, *z* = 0.039, *p* = 0.969
- **3 to 6 vs 3 to 1**: *β* = 0.03, *SE* = 0.502, *z* = 0.052, *p* = 0.959
- **SNR**: *β* = -0.14, *SE* = 0.126, *z* = -1.138, *p* = 0.255

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -0.53 | 0.50 | -1.07 | 0.287 | 0.966 | n.s. |
| 3 to 1 - 3 to 4 | -0.03 | 0.50 | -0.07 | 0.945 | 1.000 | n.s. |
| 3 to 1 - 3 to 5 | -0.02 | 0.50 | -0.04 | 0.969 | 1.000 | n.s. |
| 3 to 1 - 3 to 6 | -0.03 | 0.50 | -0.05 | 0.959 | 1.000 | n.s. |
| 3 to 2 - 3 to 4 | 0.50 | 0.50 | 0.99 | 0.321 | 0.966 | n.s. |
| 3 to 2 - 3 to 5 | 0.51 | 0.50 | 1.03 | 0.302 | 0.966 | n.s. |
| 3 to 2 - 3 to 6 | 0.51 | 0.50 | 1.02 | 0.307 | 0.966 | n.s. |
| 3 to 4 - 3 to 5 | 0.01 | 0.51 | 0.03 | 0.977 | 1.000 | n.s. |
| 3 to 4 - 3 to 6 | 0.01 | 0.50 | 0.02 | 0.987 | 1.000 | n.s. |
| 3 to 5 - 3 to 6 | -0.01 | 0.50 | -0.01 | 0.990 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.831, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.11 | 23 | = 0.897 | -0.22 [-0.65, 0.20] | small | n.s. |
| 3 to 1 vs 3 to 4 | -0.12 | 23 | = 0.966 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | 0.15 | 23 | = 0.966 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 0.08 | 23 | = 0.966 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 0.94 | 23 | = 0.897 | 0.21 [-0.24, 0.62] | small | n.s. |
| 3 to 2 vs 3 to 5 | 0.94 | 23 | = 0.897 | 0.25 [-0.23, 0.62] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.06 | 23 | = 0.897 | 0.22 [-0.21, 0.64] | small | n.s. |
| 3 to 4 vs 3 to 5 | 0.27 | 23 | = 0.966 | 0.07 [-0.37, 0.48] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.18 | 23 | = 0.966 | 0.05 [-0.39, 0.46] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | -0.04 | 23 | = 0.966 | -0.01 [-0.43, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1036.77, BIC = 1059.07
- **3 to 2 vs 3 to 1**: *β* = -5.16, *SE* = 4.415, *z* = -1.168, *p* = 0.243
- **3 to 4 vs 3 to 1**: *β* = -13.33, *SE* = 4.230, *z* = -3.150, *p* = 0.002
- **3 to 5 vs 3 to 1**: *β* = -10.31, *SE* = 4.234, *z* = -2.436, *p* = 0.015
- **3 to 6 vs 3 to 1**: *β* = -8.28, *SE* = 4.523, *z* = -1.831, *p* = 0.067
- **SNR**: *β* = -0.47, *SE* = 0.679, *z* = -0.691, *p* = 0.490

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 5.16 | 4.41 | 1.17 | 0.243 | 0.779 | n.s. |
| 3 to 1 - 3 to 4 | 13.33 | 4.23 | 3.15 | 0.002 | 0.016 | * |
| 3 to 1 - 3 to 5 | 10.31 | 4.23 | 2.44 | 0.015 | 0.126 | n.s. |
| 3 to 1 - 3 to 6 | 8.28 | 4.52 | 1.83 | 0.067 | 0.385 | n.s. |
| 3 to 2 - 3 to 4 | 8.17 | 4.23 | 1.93 | 0.053 | 0.355 | n.s. |
| 3 to 2 - 3 to 5 | 5.16 | 4.23 | 1.22 | 0.222 | 0.779 | n.s. |
| 3 to 2 - 3 to 6 | 3.13 | 4.18 | 0.75 | 0.454 | 0.837 | n.s. |
| 3 to 4 - 3 to 5 | -3.01 | 4.17 | -0.72 | 0.469 | 0.837 | n.s. |
| 3 to 4 - 3 to 6 | -5.04 | 4.29 | -1.18 | 0.240 | 0.779 | n.s. |
| 3 to 5 - 3 to 6 | -2.03 | 4.29 | -0.47 | 0.636 | 0.837 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.08, *p* = 0.020, η²_G = 0.054
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 1.34 | 23 | = 0.339 | 0.33 [-0.16, 0.70] | small | n.s. |
| 3 to 1 vs 3 to 4 | 3.74 | 23 | = 0.011 | 0.79 [0.28, 1.24] | medium | * |
| 3 to 1 vs 3 to 5 | 3.32 | 23 | = 0.015 | 0.57 [0.21, 1.15] | medium | * |
| 3 to 1 vs 3 to 6 | 2.20 | 23 | = 0.126 | 0.53 [0.01, 0.89] | medium | n.s. |
| 3 to 2 vs 3 to 4 | 1.68 | 23 | = 0.266 | 0.36 [-0.09, 0.78] | small | n.s. |
| 3 to 2 vs 3 to 5 | 0.88 | 23 | = 0.488 | 0.21 [-0.25, 0.60] | small | n.s. |
| 3 to 2 vs 3 to 6 | 0.90 | 23 | = 0.488 | 0.16 [-0.24, 0.61] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.62 | 23 | = 0.600 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -1.31 | 23 | = 0.339 | -0.22 [-0.70, 0.16] | small | n.s. |
| 3 to 5 vs 3 to 6 | -0.30 | 23 | = 0.767 | -0.06 [-0.48, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 498.03, BIC = 520.33
- **3 to 2 vs 3 to 1**: *β* = -0.73, *SE* = 0.465, *z* = -1.579, *p* = 0.114
- **3 to 4 vs 3 to 1**: *β* = -0.91, *SE* = 0.445, *z* = -2.041, *p* = 0.041
- **3 to 5 vs 3 to 1**: *β* = -0.70, *SE* = 0.445, *z* = -1.577, *p* = 0.115
- **3 to 6 vs 3 to 1**: *β* = -1.39, *SE* = 0.476, *z* = -2.921, *p* = 0.003
- **SNR**: *β* = -0.52, *SE* = 0.072, *z* = -7.213, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.73 | 0.46 | 1.58 | 0.114 | 0.621 | n.s. |
| 3 to 1 - 3 to 4 | 0.91 | 0.45 | 2.04 | 0.041 | 0.315 | n.s. |
| 3 to 1 - 3 to 5 | 0.70 | 0.45 | 1.58 | 0.115 | 0.621 | n.s. |
| 3 to 1 - 3 to 6 | 1.39 | 0.48 | 2.92 | 0.003 | 0.034 | * |
| 3 to 2 - 3 to 4 | 0.17 | 0.44 | 0.39 | 0.695 | 0.953 | n.s. |
| 3 to 2 - 3 to 5 | -0.03 | 0.44 | -0.07 | 0.944 | 0.953 | n.s. |
| 3 to 2 - 3 to 6 | 0.66 | 0.44 | 1.50 | 0.135 | 0.621 | n.s. |
| 3 to 4 - 3 to 5 | -0.21 | 0.44 | -0.47 | 0.638 | 0.953 | n.s. |
| 3 to 4 - 3 to 6 | 0.48 | 0.45 | 1.07 | 0.285 | 0.738 | n.s. |
| 3 to 5 - 3 to 6 | 0.69 | 0.45 | 1.53 | 0.127 | 0.621 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.98, *p* < .001, η²_G = 0.107
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 3.22 | 23 | = 0.013 | 0.72 [0.19, 1.12] | medium | * |
| 3 to 1 vs 3 to 4 | 2.90 | 23 | = 0.020 | 0.59 [0.13, 1.05] | medium | * |
| 3 to 1 vs 3 to 5 | 2.04 | 23 | = 0.089 | 0.49 [-0.02, 0.86] | small | n.s. |
| 3 to 1 vs 3 to 6 | 3.86 | 23 | = 0.008 | 1.01 [0.31, 1.27] | large | ** |
| 3 to 2 vs 3 to 4 | -0.95 | 23 | = 0.389 | -0.15 [-0.62, 0.23] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -1.06 | 23 | = 0.375 | -0.22 [-0.64, 0.21] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.85 | 23 | = 0.110 | 0.33 [-0.06, 0.82] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.39 | 23 | = 0.699 | -0.07 [-0.50, 0.34] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 2.70 | 23 | = 0.025 | 0.48 [0.10, 1.00] | small | * |
| 3 to 5 vs 3 to 6 | 3.20 | 23 | = 0.013 | 0.53 [0.19, 1.12] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 919.23, BIC = 941.53
- **3 to 2 vs 3 to 1**: *β* = -5.12, *SE* = 2.962, *z* = -1.727, *p* = 0.084
- **3 to 4 vs 3 to 1**: *β* = -5.84, *SE* = 2.969, *z* = -1.966, *p* = 0.049
- **3 to 5 vs 3 to 1**: *β* = -6.62, *SE* = 2.974, *z* = -2.226, *p* = 0.026
- **3 to 6 vs 3 to 1**: *β* = -7.59, *SE* = 2.963, *z* = -2.563, *p* = 0.010
- **SNR**: *β* = 1.30, *SE* = 0.600, *z* = 2.161, *p* = 0.031

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 5.11 | 2.96 | 1.73 | 0.084 | 0.460 | n.s. |
| 3 to 1 - 3 to 4 | 5.84 | 2.97 | 1.97 | 0.049 | 0.332 | n.s. |
| 3 to 1 - 3 to 5 | 6.62 | 2.97 | 2.23 | 0.026 | 0.211 | n.s. |
| 3 to 1 - 3 to 6 | 7.59 | 2.96 | 2.56 | 0.010 | 0.099 | n.s. |
| 3 to 2 - 3 to 4 | 0.72 | 2.96 | 0.24 | 0.807 | 0.983 | n.s. |
| 3 to 2 - 3 to 5 | 1.50 | 2.99 | 0.50 | 0.614 | 0.983 | n.s. |
| 3 to 2 - 3 to 6 | 2.48 | 2.97 | 0.83 | 0.404 | 0.955 | n.s. |
| 3 to 4 - 3 to 5 | 0.78 | 3.00 | 0.26 | 0.795 | 0.983 | n.s. |
| 3 to 4 - 3 to 6 | 1.75 | 2.98 | 0.59 | 0.556 | 0.983 | n.s. |
| 3 to 5 - 3 to 6 | 0.97 | 2.96 | 0.33 | 0.743 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.77, *p* = 0.142, η²_G = 0.056
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 1.87 | 23 | = 0.209 | 0.50 [-0.06, 0.82] | small | n.s. |
| 3 to 1 vs 3 to 4 | 2.01 | 23 | = 0.209 | 0.59 [-0.03, 0.85] | medium | n.s. |
| 3 to 1 vs 3 to 5 | 1.81 | 23 | = 0.209 | 0.56 [-0.07, 0.81] | medium | n.s. |
| 3 to 1 vs 3 to 6 | 2.25 | 23 | = 0.209 | 0.72 [0.01, 0.90] | medium | n.s. |
| 3 to 2 vs 3 to 4 | 0.28 | 23 | = 0.914 | 0.09 [-0.37, 0.48] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.21 | 23 | = 0.914 | 0.06 [-0.38, 0.47] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 0.71 | 23 | = 0.914 | 0.18 [-0.28, 0.57] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -0.11 | 23 | = 0.914 | -0.03 [-0.44, 0.40] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.35 | 23 | = 0.914 | 0.09 [-0.35, 0.49] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.54 | 23 | = 0.914 | 0.12 [-0.31, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 522.50, BIC = 544.80
- **3 to 2 vs 3 to 1**: *β* = -1.93, *SE* = 0.530, *z* = -3.637, *p* < .001
- **3 to 4 vs 3 to 1**: *β* = -0.37, *SE* = 0.531, *z* = -0.704, *p* = 0.481
- **3 to 5 vs 3 to 1**: *β* = -1.38, *SE* = 0.532, *z* = -2.590, *p* = 0.010
- **3 to 6 vs 3 to 1**: *β* = -1.36, *SE* = 0.530, *z* = -2.566, *p* = 0.010
- **SNR**: *β* = 0.46, *SE* = 0.114, *z* = 4.020, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 1.93 | 0.53 | 3.64 | < .001 | 0.003 | ** |
| 3 to 1 - 3 to 4 | 0.37 | 0.53 | 0.70 | 0.481 | 0.739 | n.s. |
| 3 to 1 - 3 to 5 | 1.38 | 0.53 | 2.59 | 0.010 | 0.074 | n.s. |
| 3 to 1 - 3 to 6 | 1.36 | 0.53 | 2.57 | 0.010 | 0.074 | n.s. |
| 3 to 2 - 3 to 4 | -1.55 | 0.53 | -2.93 | 0.003 | 0.030 | * |
| 3 to 2 - 3 to 5 | -0.55 | 0.53 | -1.03 | 0.305 | 0.739 | n.s. |
| 3 to 2 - 3 to 6 | -0.57 | 0.53 | -1.07 | 0.286 | 0.739 | n.s. |
| 3 to 4 - 3 to 5 | 1.00 | 0.54 | 1.87 | 0.062 | 0.319 | n.s. |
| 3 to 4 - 3 to 6 | 0.99 | 0.53 | 1.85 | 0.065 | 0.319 | n.s. |
| 3 to 5 - 3 to 6 | -0.02 | 0.53 | -0.04 | 0.971 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.55, *p* = 0.010, η²_G = 0.085
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 3.82 | 23 | = 0.009 | 0.92 [0.30, 1.26] | large | ** |
| 3 to 1 vs 3 to 4 | 0.96 | 23 | = 0.387 | 0.26 [-0.23, 0.62] | small | n.s. |
| 3 to 1 vs 3 to 5 | 1.92 | 23 | = 0.182 | 0.53 [-0.05, 0.83] | medium | n.s. |
| 3 to 1 vs 3 to 6 | 1.88 | 23 | = 0.182 | 0.55 [-0.05, 0.82] | medium | n.s. |
| 3 to 2 vs 3 to 4 | -2.51 | 23 | = 0.098 | -0.66 [-0.96, -0.06] | medium | n.s. |
| 3 to 2 vs 3 to 5 | -1.47 | 23 | = 0.258 | -0.37 [-0.73, 0.13] | small | n.s. |
| 3 to 2 vs 3 to 6 | -1.64 | 23 | = 0.228 | -0.31 [-0.77, 0.10] | small | n.s. |
| 3 to 4 vs 3 to 5 | 1.28 | 23 | = 0.287 | 0.27 [-0.17, 0.69] | small | n.s. |
| 3 to 4 vs 3 to 6 | 1.23 | 23 | = 0.287 | 0.31 [-0.18, 0.68] | small | n.s. |
| 3 to 5 vs 3 to 6 | 0.17 | 23 | = 0.865 | 0.05 [-0.39, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1218.47, BIC = 1240.77
- **3 to 2 vs 3 to 1**: *β* = 6.43, *SE* = 9.949, *z* = 0.647, *p* = 0.518
- **3 to 4 vs 3 to 1**: *β* = 8.53, *SE* = 9.781, *z* = 0.872, *p* = 0.383
- **3 to 5 vs 3 to 1**: *β* = 4.16, *SE* = 9.843, *z* = 0.422, *p* = 0.673
- **3 to 6 vs 3 to 1**: *β* = 8.58, *SE* = 9.993, *z* = 0.859, *p* = 0.390
- **SNR**: *β* = -0.08, *SE* = 0.749, *z* = -0.105, *p* = 0.917

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -6.43 | 9.95 | -0.65 | 0.518 | 0.997 | n.s. |
| 3 to 1 - 3 to 4 | -8.53 | 9.78 | -0.87 | 0.383 | 0.992 | n.s. |
| 3 to 1 - 3 to 5 | -4.16 | 9.84 | -0.42 | 0.673 | 0.999 | n.s. |
| 3 to 1 - 3 to 6 | -8.58 | 9.99 | -0.86 | 0.390 | 0.992 | n.s. |
| 3 to 2 - 3 to 4 | -2.10 | 9.74 | -0.22 | 0.829 | 0.999 | n.s. |
| 3 to 2 - 3 to 5 | 2.28 | 9.71 | 0.23 | 0.815 | 0.999 | n.s. |
| 3 to 2 - 3 to 6 | -2.15 | 9.70 | -0.22 | 0.825 | 0.999 | n.s. |
| 3 to 4 - 3 to 5 | 4.38 | 9.71 | 0.45 | 0.652 | 0.999 | n.s. |
| 3 to 4 - 3 to 6 | -0.05 | 9.77 | -0.00 | 0.996 | 0.999 | n.s. |
| 3 to 5 - 3 to 6 | -4.42 | 9.73 | -0.45 | 0.649 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.27, *p* = 0.894, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.80 | 23 | = 0.931 | -0.20 [-0.59, 0.26] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | -0.88 | 23 | = 0.931 | -0.24 [-0.60, 0.25] | small | n.s. |
| 3 to 1 vs 3 to 5 | -0.54 | 23 | = 0.931 | -0.12 [-0.53, 0.31] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | -0.89 | 23 | = 0.931 | -0.24 [-0.61, 0.24] | small | n.s. |
| 3 to 2 vs 3 to 4 | -0.21 | 23 | = 0.931 | -0.05 [-0.46, 0.38] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.22 | 23 | = 0.931 | 0.06 [-0.38, 0.47] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | -0.21 | 23 | = 0.931 | -0.06 [-0.47, 0.38] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | 0.44 | 23 | = 0.931 | 0.11 [-0.33, 0.51] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -0.01 | 23 | = 0.988 | -0.00 [-0.43, 0.42] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | -0.41 | 23 | = 0.931 | -0.11 [-0.51, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 593.87, BIC = 616.17
- **3 to 2 vs 3 to 1**: *β* = 0.66, *SE* = 0.627, *z* = 1.049, *p* = 0.294
- **3 to 4 vs 3 to 1**: *β* = -0.57, *SE* = 0.614, *z* = -0.932, *p* = 0.351
- **3 to 5 vs 3 to 1**: *β* = -0.31, *SE* = 0.619, *z* = -0.499, *p* = 0.618
- **3 to 6 vs 3 to 1**: *β* = -0.39, *SE* = 0.630, *z* = -0.617, *p* = 0.537
- **SNR**: *β* = 0.15, *SE* = 0.051, *z* = 3.002, *p* = 0.003

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -0.66 | 0.63 | -1.05 | 0.294 | 0.913 | n.s. |
| 3 to 1 - 3 to 4 | 0.57 | 0.61 | 0.93 | 0.351 | 0.926 | n.s. |
| 3 to 1 - 3 to 5 | 0.31 | 0.62 | 0.50 | 0.618 | 0.979 | n.s. |
| 3 to 1 - 3 to 6 | 0.39 | 0.63 | 0.62 | 0.537 | 0.979 | n.s. |
| 3 to 2 - 3 to 4 | 1.23 | 0.61 | 2.01 | 0.044 | 0.365 | n.s. |
| 3 to 2 - 3 to 5 | 0.97 | 0.61 | 1.59 | 0.113 | 0.616 | n.s. |
| 3 to 2 - 3 to 6 | 1.05 | 0.61 | 1.72 | 0.085 | 0.553 | n.s. |
| 3 to 4 - 3 to 5 | -0.26 | 0.61 | -0.43 | 0.665 | 0.979 | n.s. |
| 3 to 4 - 3 to 6 | -0.18 | 0.61 | -0.30 | 0.764 | 0.979 | n.s. |
| 3 to 5 - 3 to 6 | 0.08 | 0.61 | 0.13 | 0.896 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.22, *p* = 0.310, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.27 | 23 | = 0.889 | -0.05 [-0.48, 0.37] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | 1.20 | 23 | = 0.484 | 0.21 [-0.18, 0.67] | small | n.s. |
| 3 to 1 vs 3 to 5 | 1.05 | 23 | = 0.509 | 0.17 [-0.21, 0.64] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 1.54 | 23 | = 0.459 | 0.27 [-0.12, 0.75] | small | n.s. |
| 3 to 2 vs 3 to 4 | 1.56 | 23 | = 0.459 | 0.23 [-0.11, 0.75] | small | n.s. |
| 3 to 2 vs 3 to 5 | 1.33 | 23 | = 0.484 | 0.19 [-0.16, 0.70] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 1.90 | 23 | = 0.459 | 0.28 [-0.05, 0.83] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.26 | 23 | = 0.889 | -0.04 [-0.47, 0.37] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.09 | 23 | = 0.933 | 0.01 [-0.40, 0.44] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.38 | 23 | = 0.889 | 0.06 [-0.35, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.020). Post-hoc tests revealed:
  - 3 to 1 showed greater latency than 3 to 4 (*d* = 0.79)
  - 3 to 1 showed greater latency than 3 to 5 (*d* = 0.57)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 3 to 2 (*d* = 0.72)
  - 3 to 1 showed greater amplitude than 3 to 4 (*d* = 0.59)
  - 3 to 1 showed greater amplitude than 3 to 6 (*d* = 1.01)
  - 3 to 4 showed greater amplitude than 3 to 6 (*d* = 0.48)
  - 3 to 5 showed greater amplitude than 3 to 6 (*d* = 0.53)
**P1 amplitude:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 3 to 2 (*d* = 0.92)

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
