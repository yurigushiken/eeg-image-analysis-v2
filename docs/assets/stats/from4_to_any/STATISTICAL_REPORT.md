# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:40:08

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
| 4 to 1 | 6 | 110.67 ms | 9.35 | 3.82 | [92.00, 116.00] |
| 4 to 2 | 12 | 102.00 ms | 10.72 | 3.09 | [92.00, 116.00] |
| 4 to 3 | 12 | 103.00 ms | 10.39 | 3.00 | [92.00, 116.00] |
| 4 to 5 | 10 | 109.20 ms | 8.85 | 2.80 | [92.00, 116.00] |
| 4 to 6 | 11 | 107.27 ms | 9.09 | 2.74 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 6 | 2.16 µV | 1.09 | 0.44 | [1.11, 4.00] |
| 4 to 2 | 12 | 3.05 µV | 1.84 | 0.53 | [0.57, 5.76] |
| 4 to 3 | 12 | 2.32 µV | 1.02 | 0.29 | [1.06, 3.91] |
| 4 to 5 | 10 | 2.89 µV | 1.40 | 0.44 | [0.78, 5.59] |
| 4 to 6 | 11 | 3.25 µV | 1.77 | 0.53 | [0.85, 5.74] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 182.80 ms | 14.63 | 3.27 | [144.00, 208.00] |
| 4 to 2 | 24 | 174.67 ms | 14.81 | 3.02 | [148.00, 208.00] |
| 4 to 3 | 23 | 175.83 ms | 18.23 | 3.80 | [148.00, 208.00] |
| 4 to 5 | 23 | 168.87 ms | 20.92 | 4.36 | [144.00, 208.00] |
| 4 to 6 | 23 | 172.52 ms | 21.25 | 4.43 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | -3.98 µV | 1.84 | 0.41 | [-8.09, -0.51] |
| 4 to 2 | 24 | -6.13 µV | 3.05 | 0.62 | [-11.92, -1.89] |
| 4 to 3 | 23 | -6.41 µV | 2.15 | 0.45 | [-11.27, -1.89] |
| 4 to 5 | 23 | -5.78 µV | 2.70 | 0.56 | [-11.05, -1.46] |
| 4 to 6 | 23 | -6.14 µV | 2.95 | 0.62 | [-13.20, -2.83] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 18 | 113.33 ms | 5.13 | 1.21 | [96.00, 116.00] |
| 4 to 2 | 14 | 114.00 ms | 3.42 | 0.91 | [108.00, 116.00] |
| 4 to 3 | 11 | 105.45 ms | 7.22 | 2.18 | [96.00, 116.00] |
| 4 to 5 | 13 | 106.77 ms | 8.06 | 2.24 | [96.00, 116.00] |
| 4 to 6 | 12 | 106.67 ms | 7.50 | 2.16 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 18 | 4.49 µV | 3.02 | 0.71 | [1.26, 13.38] |
| 4 to 2 | 14 | 2.41 µV | 1.03 | 0.28 | [1.14, 4.31] |
| 4 to 3 | 11 | 2.68 µV | 1.41 | 0.42 | [0.60, 5.30] |
| 4 to 5 | 13 | 3.76 µV | 3.35 | 0.93 | [1.14, 13.41] |
| 4 to 6 | 12 | 3.07 µV | 1.23 | 0.35 | [1.15, 5.39] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 487.20 ms | 33.00 | 7.38 | [432.00, 540.00] |
| 4 to 2 | 19 | 481.89 ms | 37.08 | 8.51 | [428.00, 540.00] |
| 4 to 3 | 21 | 474.29 ms | 35.45 | 7.74 | [428.00, 536.00] |
| 4 to 5 | 16 | 496.00 ms | 36.98 | 9.24 | [436.00, 540.00] |
| 4 to 6 | 18 | 495.56 ms | 38.17 | 9.00 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 6.11 µV | 3.12 | 0.70 | [1.64, 12.03] |
| 4 to 2 | 19 | 5.40 µV | 3.11 | 0.71 | [1.15, 11.62] |
| 4 to 3 | 21 | 5.44 µV | 3.05 | 0.67 | [1.17, 11.65] |
| 4 to 5 | 16 | 6.02 µV | 3.97 | 0.99 | [1.66, 16.10] |
| 4 to 6 | 18 | 5.79 µV | 3.01 | 0.71 | [1.67, 9.75] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 382.44, BIC = 397.89
- **4 to 2 vs 4 to 1**: *β* = -7.67, *SE* = 4.183, *z* = -1.834, *p* = 0.067
- **4 to 3 vs 4 to 1**: *β* = -7.54, *SE* = 4.035, *z* = -1.869, *p* = 0.062
- **4 to 5 vs 4 to 1**: *β* = -1.15, *SE* = 4.309, *z* = -0.266, *p* = 0.790
- **4 to 6 vs 4 to 1**: *β* = -3.06, *SE* = 4.353, *z* = -0.703, *p* = 0.482
- **SNR**: *β* = -0.89, *SE* = 0.721, *z* = -1.236, *p* = 0.216

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 7.67 | 4.18 | 1.83 | 0.067 | 0.460 | n.s. |
| 4 to 1 - 4 to 3 | 7.54 | 4.04 | 1.87 | 0.062 | 0.460 | n.s. |
| 4 to 1 - 4 to 5 | 1.15 | 4.31 | 0.27 | 0.790 | 0.956 | n.s. |
| 4 to 1 - 4 to 6 | 3.06 | 4.35 | 0.70 | 0.482 | 0.928 | n.s. |
| 4 to 2 - 4 to 3 | -0.13 | 3.31 | -0.04 | 0.968 | 0.968 | n.s. |
| 4 to 2 - 4 to 5 | -6.53 | 3.47 | -1.88 | 0.060 | 0.460 | n.s. |
| 4 to 2 - 4 to 6 | -4.61 | 3.39 | -1.36 | 0.174 | 0.682 | n.s. |
| 4 to 3 - 4 to 5 | -6.39 | 3.40 | -1.88 | 0.060 | 0.460 | n.s. |
| 4 to 3 - 4 to 6 | -4.48 | 3.44 | -1.30 | 0.193 | 0.682 | n.s. |
| 4 to 5 - 4 to 6 | 1.91 | 3.52 | 0.54 | 0.586 | 0.929 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 164.30, BIC = 179.75
- **4 to 2 vs 4 to 1**: *β* = 0.46, *SE* = 0.460, *z* = 0.997, *p* = 0.319
- **4 to 3 vs 4 to 1**: *β* = -0.08, *SE* = 0.436, *z* = -0.183, *p* = 0.855
- **4 to 5 vs 4 to 1**: *β* = 0.12, *SE* = 0.469, *z* = 0.248, *p* = 0.804
- **4 to 6 vs 4 to 1**: *β* = 0.80, *SE* = 0.485, *z* = 1.645, *p* = 0.100
- **SNR**: *β* = 0.48, *SE* = 0.080, *z* = 6.052, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.46 | 0.46 | -1.00 | 0.319 | 0.900 | n.s. |
| 4 to 1 - 4 to 3 | 0.08 | 0.44 | 0.18 | 0.855 | 0.962 | n.s. |
| 4 to 1 - 4 to 5 | -0.12 | 0.47 | -0.25 | 0.804 | 0.962 | n.s. |
| 4 to 1 - 4 to 6 | -0.80 | 0.48 | -1.64 | 0.100 | 0.570 | n.s. |
| 4 to 2 - 4 to 3 | 0.54 | 0.36 | 1.51 | 0.130 | 0.623 | n.s. |
| 4 to 2 - 4 to 5 | 0.34 | 0.37 | 0.93 | 0.354 | 0.900 | n.s. |
| 4 to 2 - 4 to 6 | -0.34 | 0.37 | -0.92 | 0.355 | 0.900 | n.s. |
| 4 to 3 - 4 to 5 | -0.20 | 0.36 | -0.54 | 0.589 | 0.930 | n.s. |
| 4 to 3 - 4 to 6 | -0.88 | 0.38 | -2.31 | 0.021 | 0.189 | n.s. |
| 4 to 5 - 4 to 6 | -0.68 | 0.38 | -1.79 | 0.074 | 0.498 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 963.97, BIC = 985.79
- **4 to 2 vs 4 to 1**: *β* = -9.60, *SE* = 4.275, *z* = -2.246, *p* = 0.025
- **4 to 3 vs 4 to 1**: *β* = -9.18, *SE* = 4.483, *z* = -2.047, *p* = 0.041
- **4 to 5 vs 4 to 1**: *β* = -14.60, *SE* = 4.350, *z* = -3.356, *p* = 0.001
- **4 to 6 vs 4 to 1**: *β* = -12.09, *SE* = 4.430, *z* = -2.728, *p* = 0.006
- **SNR**: *β* = 0.44, *SE* = 0.569, *z* = 0.768, *p* = 0.443

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 9.60 | 4.27 | 2.25 | 0.025 | 0.182 | n.s. |
| 4 to 1 - 4 to 3 | 9.18 | 4.48 | 2.05 | 0.041 | 0.252 | n.s. |
| 4 to 1 - 4 to 5 | 14.60 | 4.35 | 3.36 | < .001 | 0.008 | ** |
| 4 to 1 - 4 to 6 | 12.09 | 4.43 | 2.73 | 0.006 | 0.056 | n.s. |
| 4 to 2 - 4 to 3 | -0.42 | 4.07 | -0.10 | 0.917 | 0.924 | n.s. |
| 4 to 2 - 4 to 5 | 5.00 | 4.02 | 1.24 | 0.214 | 0.710 | n.s. |
| 4 to 2 - 4 to 6 | 2.49 | 4.05 | 0.61 | 0.539 | 0.924 | n.s. |
| 4 to 3 - 4 to 5 | 5.42 | 4.10 | 1.32 | 0.186 | 0.710 | n.s. |
| 4 to 3 - 4 to 6 | 2.91 | 4.08 | 0.71 | 0.475 | 0.924 | n.s. |
| 4 to 5 - 4 to 6 | -2.51 | 4.09 | -0.61 | 0.539 | 0.924 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.69, *p* = 0.009, η²_G = 0.101
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 2.27 | 16 | = 0.093 | 0.76 [0.02, 1.02] | medium | n.s. |
| 4 to 1 vs 4 to 3 | 1.27 | 16 | = 0.311 | 0.33 [-0.13, 0.87] | small | n.s. |
| 4 to 1 vs 4 to 5 | 3.14 | 16 | = 0.063 | 0.98 [0.19, 1.27] | large | n.s. |
| 4 to 1 vs 4 to 6 | 2.46 | 16 | = 0.093 | 0.65 [0.07, 1.12] | medium | n.s. |
| 4 to 2 vs 4 to 3 | -1.21 | 16 | = 0.311 | -0.33 [-0.49, 0.38] | small | n.s. |
| 4 to 2 vs 4 to 5 | 1.81 | 16 | = 0.179 | 0.36 [-0.17, 0.71] | small | n.s. |
| 4 to 2 vs 4 to 6 | 0.22 | 16 | = 0.826 | 0.06 [-0.33, 0.54] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 2.30 | 16 | = 0.093 | 0.61 [-0.24, 0.66] | medium | n.s. |
| 4 to 3 vs 4 to 6 | 1.20 | 16 | = 0.311 | 0.33 [-0.25, 0.64] | small | n.s. |
| 4 to 5 vs 4 to 6 | -1.06 | 16 | = 0.339 | -0.25 [-0.61, 0.29] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 466.15, BIC = 487.97
- **4 to 2 vs 4 to 1**: *β* = -1.70, *SE* = 0.449, *z* = -3.780, *p* < .001
- **4 to 3 vs 4 to 1**: *β* = -1.51, *SE* = 0.471, *z* = -3.215, *p* = 0.001
- **4 to 5 vs 4 to 1**: *β* = -1.21, *SE* = 0.458, *z* = -2.643, *p* = 0.008
- **4 to 6 vs 4 to 1**: *β* = -1.35, *SE* = 0.466, *z* = -2.906, *p* = 0.004
- **SNR**: *β* = -0.41, *SE* = 0.061, *z* = -6.758, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 1.70 | 0.45 | 3.78 | < .001 | 0.002 | ** |
| 4 to 1 - 4 to 3 | 1.52 | 0.47 | 3.22 | 0.001 | 0.012 | * |
| 4 to 1 - 4 to 5 | 1.21 | 0.46 | 2.64 | 0.008 | 0.056 | n.s. |
| 4 to 1 - 4 to 6 | 1.35 | 0.47 | 2.91 | 0.004 | 0.029 | * |
| 4 to 2 - 4 to 3 | -0.18 | 0.43 | -0.43 | 0.669 | 0.964 | n.s. |
| 4 to 2 - 4 to 5 | -0.49 | 0.42 | -1.16 | 0.247 | 0.818 | n.s. |
| 4 to 2 - 4 to 6 | -0.34 | 0.42 | -0.81 | 0.418 | 0.933 | n.s. |
| 4 to 3 - 4 to 5 | -0.31 | 0.43 | -0.71 | 0.477 | 0.933 | n.s. |
| 4 to 3 - 4 to 6 | -0.16 | 0.43 | -0.38 | 0.705 | 0.964 | n.s. |
| 4 to 5 - 4 to 6 | 0.14 | 0.43 | 0.34 | 0.736 | 0.964 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.63, *p* < .001, η²_G = 0.147
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 3.43 | 16 | = 0.011 | 0.96 [0.25, 1.32] | large | * |
| 4 to 1 vs 4 to 3 | 5.11 | 16 | = 0.001 | 1.32 [0.59, 1.86] | large | ** |
| 4 to 1 vs 4 to 5 | 4.23 | 16 | = 0.003 | 1.18 [0.31, 1.45] | large | ** |
| 4 to 1 vs 4 to 6 | 3.17 | 16 | = 0.015 | 0.92 [0.19, 1.27] | large | * |
| 4 to 2 vs 4 to 3 | 0.38 | 16 | = 0.926 | 0.08 [-0.24, 0.64] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 0.30 | 16 | = 0.926 | 0.08 [-0.60, 0.27] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | -0.21 | 16 | = 0.926 | -0.04 [-0.44, 0.43] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 0.03 | 16 | = 0.977 | 0.01 [-0.70, 0.20] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | -0.57 | 16 | = 0.926 | -0.13 [-0.56, 0.33] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -0.48 | 16 | = 0.926 | -0.13 [-0.33, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 449.50, BIC = 467.26
- **4 to 2 vs 4 to 1**: *β* = 1.33, *SE* = 2.103, *z* = 0.631, *p* = 0.528
- **4 to 3 vs 4 to 1**: *β* = -7.55, *SE* = 2.128, *z* = -3.549, *p* < .001
- **4 to 5 vs 4 to 1**: *β* = -6.14, *SE* = 1.992, *z* = -3.082, *p* = 0.002
- **4 to 6 vs 4 to 1**: *β* = -5.71, *SE* = 2.131, *z* = -2.679, *p* = 0.007
- **SNR**: *β* = 0.53, *SE* = 0.415, *z* = 1.285, *p* = 0.199

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -1.33 | 2.10 | -0.63 | 0.528 | 0.892 | n.s. |
| 4 to 1 - 4 to 3 | 7.55 | 2.13 | 3.55 | < .001 | 0.003 | ** |
| 4 to 1 - 4 to 5 | 6.14 | 1.99 | 3.08 | 0.002 | 0.012 | * |
| 4 to 1 - 4 to 6 | 5.71 | 2.13 | 2.68 | 0.007 | 0.036 | * |
| 4 to 2 - 4 to 3 | 8.88 | 2.19 | 4.05 | < .001 | < .001 | *** |
| 4 to 2 - 4 to 5 | 7.46 | 2.14 | 3.48 | < .001 | 0.004 | ** |
| 4 to 2 - 4 to 6 | 7.03 | 2.17 | 3.24 | 0.001 | 0.008 | ** |
| 4 to 3 - 4 to 5 | -1.41 | 2.22 | -0.64 | 0.524 | 0.892 | n.s. |
| 4 to 3 - 4 to 6 | -1.84 | 2.28 | -0.81 | 0.419 | 0.886 | n.s. |
| 4 to 5 - 4 to 6 | -0.43 | 2.18 | -0.20 | 0.844 | 0.892 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.55, *p* = 0.079, η²_G = 0.247
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.50 | 4 | = 0.353 | 0.72 [-0.64, 0.64] | medium | n.s. |
| 4 to 1 vs 4 to 3 | 2.56 | 4 | = 0.331 | 1.66 [0.29, 2.41] | large | n.s. |
| 4 to 1 vs 4 to 5 | 1.09 | 4 | = 0.439 | 0.76 [-0.17, 1.27] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 1.49 | 4 | = 0.353 | 1.02 [-0.30, 1.34] | large | n.s. |
| 4 to 2 vs 4 to 3 | 1.73 | 4 | = 0.353 | 1.07 [0.07, 1.79] | large | n.s. |
| 4 to 2 vs 4 to 5 | 0.30 | 4 | = 0.778 | 0.16 [-0.09, 1.52] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | 1.05 | 4 | = 0.439 | 0.58 [-0.15, 1.78] | medium | n.s. |
| 4 to 3 vs 4 to 5 | -2.33 | 4 | = 0.331 | -0.86 [-1.22, 0.51] | large | n.s. |
| 4 to 3 vs 4 to 6 | -0.80 | 4 | = 0.520 | -0.30 [-1.25, 0.64] | small | n.s. |
| 4 to 5 vs 4 to 6 | 2.14 | 4 | = 0.331 | 0.44 [-0.68, 0.87] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.27, BIC = 293.03
- **4 to 2 vs 4 to 1**: *β* = -0.54, *SE* = 0.602, *z* = -0.890, *p* = 0.373
- **4 to 3 vs 4 to 1**: *β* = -1.24, *SE* = 0.611, *z* = -2.030, *p* = 0.042
- **4 to 5 vs 4 to 1**: *β* = -0.18, *SE* = 0.575, *z* = -0.316, *p* = 0.752
- **4 to 6 vs 4 to 1**: *β* = -0.45, *SE* = 0.612, *z* = -0.730, *p* = 0.465
- **SNR**: *β* = 0.81, *SE* = 0.114, *z* = 7.067, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 0.54 | 0.60 | 0.89 | 0.373 | 0.940 | n.s. |
| 4 to 1 - 4 to 3 | 1.24 | 0.61 | 2.03 | 0.042 | 0.351 | n.s. |
| 4 to 1 - 4 to 5 | 0.18 | 0.57 | 0.32 | 0.752 | 0.965 | n.s. |
| 4 to 1 - 4 to 6 | 0.45 | 0.61 | 0.73 | 0.465 | 0.956 | n.s. |
| 4 to 2 - 4 to 3 | 0.70 | 0.63 | 1.11 | 0.265 | 0.884 | n.s. |
| 4 to 2 - 4 to 5 | -0.35 | 0.61 | -0.58 | 0.563 | 0.964 | n.s. |
| 4 to 2 - 4 to 6 | -0.09 | 0.62 | -0.14 | 0.885 | 0.965 | n.s. |
| 4 to 3 - 4 to 5 | -1.06 | 0.64 | -1.66 | 0.096 | 0.598 | n.s. |
| 4 to 3 - 4 to 6 | -0.79 | 0.65 | -1.22 | 0.224 | 0.869 | n.s. |
| 4 to 5 - 4 to 6 | 0.27 | 0.63 | 0.42 | 0.672 | 0.965 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.66, *p* = 0.027, η²_G = 0.370
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 2.58 | 4 | = 0.205 | 1.57 [-0.00, 1.42] | large | n.s. |
| 4 to 1 vs 4 to 3 | 1.96 | 4 | = 0.209 | 1.03 [-0.05, 1.74] | large | n.s. |
| 4 to 1 vs 4 to 5 | 1.93 | 4 | = 0.209 | 0.90 [-0.07, 1.42] | large | n.s. |
| 4 to 1 vs 4 to 6 | 1.56 | 4 | = 0.278 | 1.00 [-0.30, 1.33] | large | n.s. |
| 4 to 2 vs 4 to 3 | -3.16 | 4 | = 0.189 | -1.91 [-0.80, 0.63] | large | n.s. |
| 4 to 2 vs 4 to 5 | -2.19 | 4 | = 0.209 | -1.11 [-1.41, 0.15] | large | n.s. |
| 4 to 2 vs 4 to 6 | -3.06 | 4 | = 0.189 | -1.78 [-1.81, 0.13] | large | n.s. |
| 4 to 3 vs 4 to 5 | -0.16 | 4 | = 0.934 | -0.10 [-1.35, 0.41] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | -0.09 | 4 | = 0.934 | -0.06 [-0.99, 0.86] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 0.11 | 4 | = 0.934 | 0.06 [-0.53, 1.03] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 950.25, BIC = 970.60
- **4 to 2 vs 4 to 1**: *β* = -7.17, *SE* = 11.118, *z* = -0.645, *p* = 0.519
- **4 to 3 vs 4 to 1**: *β* = -13.86, *SE* = 10.647, *z* = -1.302, *p* = 0.193
- **4 to 5 vs 4 to 1**: *β* = 6.95, *SE* = 11.605, *z* = 0.599, *p* = 0.549
- **4 to 6 vs 4 to 1**: *β* = 7.91, *SE* = 11.087, *z* = 0.713, *p* = 0.476
- **SNR**: *β* = -0.44, *SE* = 0.801, *z* = -0.545, *p* = 0.586

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 7.17 | 11.12 | 0.64 | 0.519 | 0.960 | n.s. |
| 4 to 1 - 4 to 3 | 13.86 | 10.65 | 1.30 | 0.193 | 0.784 | n.s. |
| 4 to 1 - 4 to 5 | -6.95 | 11.61 | -0.60 | 0.549 | 0.960 | n.s. |
| 4 to 1 - 4 to 6 | -7.91 | 11.09 | -0.71 | 0.476 | 0.960 | n.s. |
| 4 to 2 - 4 to 3 | 6.69 | 10.66 | 0.63 | 0.530 | 0.960 | n.s. |
| 4 to 2 - 4 to 5 | -14.13 | 11.39 | -1.24 | 0.215 | 0.784 | n.s. |
| 4 to 2 - 4 to 6 | -15.08 | 11.11 | -1.36 | 0.175 | 0.784 | n.s. |
| 4 to 3 - 4 to 5 | -20.82 | 11.18 | -1.86 | 0.063 | 0.441 | n.s. |
| 4 to 3 - 4 to 6 | -21.77 | 10.76 | -2.02 | 0.043 | 0.356 | n.s. |
| 4 to 5 - 4 to 6 | -0.95 | 11.58 | -0.08 | 0.934 | 0.960 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.134, η²_G = 0.094
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.27 | 12 | = 0.435 | 0.40 [-0.46, 0.57] | small | n.s. |
| 4 to 1 vs 4 to 3 | 0.55 | 12 | = 0.668 | 0.21 [-0.30, 0.70] | small | n.s. |
| 4 to 1 vs 4 to 5 | -1.18 | 12 | = 0.435 | -0.42 [-0.76, 0.36] | small | n.s. |
| 4 to 1 vs 4 to 6 | -0.95 | 12 | = 0.517 | -0.36 [-0.68, 0.39] | small | n.s. |
| 4 to 2 vs 4 to 3 | -0.54 | 12 | = 0.668 | -0.17 [-0.42, 0.58] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | -2.20 | 12 | = 0.297 | -0.80 [-1.12, 0.06] | large | n.s. |
| 4 to 2 vs 4 to 6 | -2.08 | 12 | = 0.297 | -0.73 [-0.92, 0.18] | medium | n.s. |
| 4 to 3 vs 4 to 5 | -1.55 | 12 | = 0.369 | -0.62 [-0.90, 0.20] | medium | n.s. |
| 4 to 3 vs 4 to 6 | -1.64 | 12 | = 0.369 | -0.55 [-0.94, 0.10] | medium | n.s. |
| 4 to 5 vs 4 to 6 | 0.09 | 12 | = 0.931 | 0.03 [-0.68, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 416.13, BIC = 436.48
- **4 to 2 vs 4 to 1**: *β* = 0.19, *SE* = 0.541, *z* = 0.358, *p* = 0.720
- **4 to 3 vs 4 to 1**: *β* = -0.02, *SE* = 0.516, *z* = -0.046, *p* = 0.963
- **4 to 5 vs 4 to 1**: *β* = 0.51, *SE* = 0.567, *z* = 0.892, *p* = 0.373
- **4 to 6 vs 4 to 1**: *β* = 0.22, *SE* = 0.542, *z* = 0.414, *p* = 0.679
- **SNR**: *β* = 0.26, *SE* = 0.045, *z* = 5.883, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.19 | 0.54 | -0.36 | 0.720 | 0.999 | n.s. |
| 4 to 1 - 4 to 3 | 0.02 | 0.52 | 0.05 | 0.963 | 0.999 | n.s. |
| 4 to 1 - 4 to 5 | -0.51 | 0.57 | -0.89 | 0.373 | 0.985 | n.s. |
| 4 to 1 - 4 to 6 | -0.22 | 0.54 | -0.41 | 0.679 | 0.999 | n.s. |
| 4 to 2 - 4 to 3 | 0.22 | 0.51 | 0.43 | 0.671 | 0.999 | n.s. |
| 4 to 2 - 4 to 5 | -0.31 | 0.55 | -0.57 | 0.568 | 0.999 | n.s. |
| 4 to 2 - 4 to 6 | -0.03 | 0.53 | -0.06 | 0.954 | 0.999 | n.s. |
| 4 to 3 - 4 to 5 | -0.53 | 0.54 | -0.98 | 0.325 | 0.980 | n.s. |
| 4 to 3 - 4 to 6 | -0.25 | 0.51 | -0.48 | 0.629 | 0.999 | n.s. |
| 4 to 5 - 4 to 6 | 0.28 | 0.55 | 0.51 | 0.610 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.967, η²_G = 0.003
- Greenhouse-Geisser corrected: *p* = 0.887 (ε = 0.545)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.38 | 12 | = 0.940 | 0.06 [-0.24, 0.81] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | 0.35 | 12 | = 0.940 | 0.09 [-0.27, 0.74] | negligible | n.s. |
| 4 to 1 vs 4 to 5 | -0.12 | 12 | = 0.940 | -0.03 [-0.54, 0.57] | negligible | n.s. |
| 4 to 1 vs 4 to 6 | 0.76 | 12 | = 0.940 | 0.11 [-0.33, 0.75] | negligible | n.s. |
| 4 to 2 vs 4 to 3 | 0.12 | 12 | = 0.940 | 0.02 [-0.53, 0.46] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | -0.55 | 12 | = 0.940 | -0.09 [-0.66, 0.45] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | 0.28 | 12 | = 0.940 | 0.05 [-0.54, 0.53] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | -0.34 | 12 | = 0.940 | -0.11 [-0.56, 0.50] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | 0.08 | 12 | = 0.940 | 0.02 [-0.48, 0.51] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 0.62 | 12 | = 0.940 | 0.13 [-0.59, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.009) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 2 (*d* = 0.96)
  - 4 to 1 showed greater amplitude than 4 to 3 (*d* = 1.32)
  - 4 to 1 showed greater amplitude than 4 to 5 (*d* = 1.18)
  - 4 to 1 showed greater amplitude than 4 to 6 (*d* = 0.92)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.079)
**P1 amplitude:** Significant main effect of condition (*p* = 0.027) (no significant pairwise comparisons)

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
