# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:46:43

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
| 1 to 2 | 11 | 101.82 ms | 10.64 | 3.21 | [92.00, 116.00] |
| 2 to 2 | 14 | 108.29 ms | 7.76 | 2.07 | [92.00, 116.00] |
| 3 to 2 | 14 | 104.57 ms | 9.52 | 2.55 | [92.00, 116.00] |
| 4 to 2 | 13 | 109.23 ms | 5.97 | 1.66 | [96.00, 116.00] |
| 5 to 2 | 17 | 105.18 ms | 9.14 | 2.22 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 11 | -1.75 µV | 0.94 | 0.28 | [-3.35, -0.65] |
| 2 to 2 | 14 | -2.26 µV | 1.32 | 0.35 | [-5.94, -0.68] |
| 3 to 2 | 14 | -2.79 µV | 1.65 | 0.44 | [-5.62, -0.69] |
| 4 to 2 | 13 | -2.53 µV | 1.54 | 0.43 | [-4.94, -0.24] |
| 5 to 2 | 17 | -3.34 µV | 1.74 | 0.42 | [-6.65, -0.53] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | 171.64 ms | 17.84 | 3.80 | [144.00, 208.00] |
| 2 to 2 | 22 | 175.09 ms | 21.91 | 4.67 | [144.00, 212.00] |
| 3 to 2 | 22 | 173.27 ms | 23.04 | 4.91 | [144.00, 212.00] |
| 4 to 2 | 24 | 178.50 ms | 15.33 | 3.13 | [148.00, 212.00] |
| 5 to 2 | 24 | 174.17 ms | 18.35 | 3.75 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | -5.81 µV | 2.14 | 0.46 | [-10.03, -2.38] |
| 2 to 2 | 22 | -5.73 µV | 2.50 | 0.53 | [-10.50, -1.57] |
| 3 to 2 | 22 | -6.17 µV | 2.56 | 0.55 | [-10.33, -1.67] |
| 4 to 2 | 24 | -6.17 µV | 3.05 | 0.62 | [-12.20, -2.20] |
| 5 to 2 | 24 | -6.98 µV | 2.97 | 0.61 | [-11.17, -1.41] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 11 | 112.73 ms | 7.34 | 2.21 | [104.00, 120.00] |
| 2 to 2 | 13 | 112.62 ms | 7.09 | 1.97 | [104.00, 120.00] |
| 3 to 2 | 9 | 111.56 ms | 6.77 | 2.26 | [104.00, 120.00] |
| 4 to 2 | 14 | 116.00 ms | 5.66 | 1.51 | [104.00, 120.00] |
| 5 to 2 | 16 | 113.00 ms | 7.23 | 1.81 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 11 | 1.75 µV | 0.80 | 0.24 | [0.48, 3.14] |
| 2 to 2 | 13 | 2.97 µV | 1.81 | 0.50 | [1.11, 7.57] |
| 3 to 2 | 9 | 2.74 µV | 1.87 | 0.62 | [0.51, 6.10] |
| 4 to 2 | 14 | 2.76 µV | 1.19 | 0.32 | [0.45, 4.59] |
| 5 to 2 | 16 | 3.08 µV | 1.56 | 0.39 | [0.75, 6.20] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 481.41 ms | 43.45 | 10.54 | [420.00, 540.00] |
| 2 to 2 | 11 | 465.82 ms | 33.53 | 10.11 | [420.00, 536.00] |
| 3 to 2 | 18 | 490.00 ms | 32.12 | 7.57 | [432.00, 540.00] |
| 4 to 2 | 18 | 484.44 ms | 36.11 | 8.51 | [420.00, 536.00] |
| 5 to 2 | 18 | 477.78 ms | 37.85 | 8.92 | [420.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 5.80 µV | 2.98 | 0.72 | [1.85, 11.52] |
| 2 to 2 | 11 | 4.56 µV | 2.39 | 0.72 | [1.28, 10.57] |
| 3 to 2 | 18 | 6.73 µV | 4.05 | 0.96 | [2.10, 17.81] |
| 4 to 2 | 18 | 6.00 µV | 3.62 | 0.85 | [0.66, 14.41] |
| 5 to 2 | 18 | 5.90 µV | 2.71 | 0.64 | [3.15, 13.53] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 497.35, BIC = 515.23
- **2 to 2 vs 1 to 2**: *β* = 6.23, *SE* = 2.891, *z* = 2.154, *p* = 0.031
- **3 to 2 vs 1 to 2**: *β* = 1.69, *SE* = 2.937, *z* = 0.577, *p* = 0.564
- **4 to 2 vs 1 to 2**: *β* = 6.97, *SE* = 2.982, *z* = 2.338, *p* = 0.019
- **5 to 2 vs 1 to 2**: *β* = 2.01, *SE* = 2.855, *z* = 0.705, *p* = 0.481
- **SNR**: *β* = 0.61, *SE* = 0.759, *z* = 0.807, *p* = 0.420

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | -6.23 | 2.89 | -2.15 | 0.031 | 0.248 | n.s. |
| 1 to 2 - 3 to 2 | -1.69 | 2.94 | -0.58 | 0.564 | 0.927 | n.s. |
| 1 to 2 - 4 to 2 | -6.97 | 2.98 | -2.34 | 0.019 | 0.178 | n.s. |
| 1 to 2 - 5 to 2 | -2.01 | 2.85 | -0.70 | 0.481 | 0.927 | n.s. |
| 2 to 2 - 3 to 2 | 4.53 | 2.75 | 1.65 | 0.099 | 0.467 | n.s. |
| 2 to 2 - 4 to 2 | -0.74 | 2.77 | -0.27 | 0.788 | 0.955 | n.s. |
| 2 to 2 - 5 to 2 | 4.22 | 2.69 | 1.57 | 0.117 | 0.467 | n.s. |
| 3 to 2 - 4 to 2 | -5.28 | 2.78 | -1.90 | 0.058 | 0.378 | n.s. |
| 3 to 2 - 5 to 2 | -0.32 | 2.57 | -0.12 | 0.902 | 0.955 | n.s. |
| 4 to 2 - 5 to 2 | 4.96 | 2.70 | 1.84 | 0.066 | 0.381 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.56, *p* = 0.247, η²_G = 0.284
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -1.32 | 3 | = 0.465 | -1.26 [-1.19, 0.53] | large | n.s. |
| 1 to 2 vs 3 to 2 | -1.67 | 3 | = 0.465 | -1.21 [-1.05, 0.64] | large | n.s. |
| 1 to 2 vs 4 to 2 | -2.04 | 3 | = 0.465 | -1.58 [-2.24, 0.30] | large | n.s. |
| 1 to 2 vs 5 to 2 | -0.68 | 3 | = 0.684 | -0.44 [-0.71, 0.83] | small | n.s. |
| 2 to 2 vs 3 to 2 | 0.00 | 3 | = 1.000 | 0.00 [-0.43, 1.04] | negligible | n.s. |
| 2 to 2 vs 4 to 2 | -0.30 | 3 | = 0.870 | -0.22 [-1.04, 0.65] | small | n.s. |
| 2 to 2 vs 5 to 2 | 1.17 | 3 | = 0.465 | 0.81 [-0.18, 1.26] | large | n.s. |
| 3 to 2 vs 4 to 2 | -1.73 | 3 | = 0.465 | -0.21 [-1.57, 0.15] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.22 | 3 | = 0.465 | 0.79 [-0.83, 0.52] | medium | n.s. |
| 4 to 2 vs 5 to 2 | 1.80 | 3 | = 0.465 | 1.09 [-0.34, 1.14] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 218.71, BIC = 236.58
- **2 to 2 vs 1 to 2**: *β* = -0.64, *SE* = 0.413, *z* = -1.552, *p* = 0.121
- **3 to 2 vs 1 to 2**: *β* = -0.61, *SE* = 0.416, *z* = -1.463, *p* = 0.143
- **4 to 2 vs 1 to 2**: *β* = -0.85, *SE* = 0.423, *z* = -2.007, *p* = 0.045
- **5 to 2 vs 1 to 2**: *β* = -0.99, *SE* = 0.407, *z* = -2.445, *p* = 0.014
- **SNR**: *β* = -0.81, *SE* = 0.104, *z* = -7.817, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 0.64 | 0.41 | 1.55 | 0.121 | 0.642 | n.s. |
| 1 to 2 - 3 to 2 | 0.61 | 0.42 | 1.46 | 0.143 | 0.661 | n.s. |
| 1 to 2 - 4 to 2 | 0.85 | 0.42 | 2.01 | 0.045 | 0.338 | n.s. |
| 1 to 2 - 5 to 2 | 0.99 | 0.41 | 2.44 | 0.014 | 0.136 | n.s. |
| 2 to 2 - 3 to 2 | -0.03 | 0.39 | -0.08 | 0.935 | 0.959 | n.s. |
| 2 to 2 - 4 to 2 | 0.21 | 0.40 | 0.52 | 0.602 | 0.959 | n.s. |
| 2 to 2 - 5 to 2 | 0.35 | 0.39 | 0.91 | 0.361 | 0.893 | n.s. |
| 3 to 2 - 4 to 2 | 0.24 | 0.40 | 0.60 | 0.549 | 0.959 | n.s. |
| 3 to 2 - 5 to 2 | 0.39 | 0.37 | 1.04 | 0.300 | 0.882 | n.s. |
| 4 to 2 - 5 to 2 | 0.15 | 0.39 | 0.38 | 0.706 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.20, *p* = 0.360, η²_G = 0.275
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | 0.09 | 3 | = 0.965 | 0.08 [-0.58, 1.13] | negligible | n.s. |
| 1 to 2 vs 3 to 2 | 1.32 | 3 | = 0.780 | 0.87 [-0.31, 1.51] | large | n.s. |
| 1 to 2 vs 4 to 2 | -0.05 | 3 | = 0.965 | -0.03 [-0.84, 1.28] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | 3.64 | 3 | = 0.178 | 1.56 [0.14, 2.10] | large | n.s. |
| 2 to 2 vs 3 to 2 | 0.63 | 3 | = 0.822 | 0.50 [-0.34, 1.15] | medium | n.s. |
| 2 to 2 vs 4 to 2 | -0.11 | 3 | = 0.965 | -0.09 [-0.62, 1.07] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 1.15 | 3 | = 0.780 | 1.04 [-0.18, 1.26] | large | n.s. |
| 3 to 2 vs 4 to 2 | -0.83 | 3 | = 0.780 | -0.78 [-0.85, 0.69] | medium | n.s. |
| 3 to 2 vs 5 to 2 | 0.85 | 3 | = 0.780 | 0.73 [-0.26, 1.14] | medium | n.s. |
| 4 to 2 vs 5 to 2 | 7.67 | 3 | = 0.046 | 1.41 [-0.03, 1.61] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 992.79, BIC = 1014.68
- **2 to 2 vs 1 to 2**: *β* = 1.96, *SE* = 4.738, *z* = 0.413, *p* = 0.680
- **3 to 2 vs 1 to 2**: *β* = 2.00, *SE* = 4.702, *z* = 0.425, *p* = 0.671
- **4 to 2 vs 1 to 2**: *β* = 6.06, *SE* = 4.591, *z* = 1.320, *p* = 0.187
- **5 to 2 vs 1 to 2**: *β* = 2.31, *SE* = 4.633, *z* = 0.499, *p* = 0.618
- **SNR**: *β* = -0.38, *SE* = 0.736, *z* = -0.509, *p* = 0.611

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | -1.96 | 4.74 | -0.41 | 0.680 | 0.997 | n.s. |
| 1 to 2 - 3 to 2 | -2.00 | 4.70 | -0.42 | 0.671 | 0.997 | n.s. |
| 1 to 2 - 4 to 2 | -6.06 | 4.59 | -1.32 | 0.187 | 0.874 | n.s. |
| 1 to 2 - 5 to 2 | -2.31 | 4.63 | -0.50 | 0.618 | 0.997 | n.s. |
| 2 to 2 - 3 to 2 | -0.04 | 4.77 | -0.01 | 0.993 | 1.000 | n.s. |
| 2 to 2 - 4 to 2 | -4.10 | 4.58 | -0.90 | 0.370 | 0.984 | n.s. |
| 2 to 2 - 5 to 2 | -0.35 | 4.78 | -0.07 | 0.941 | 1.000 | n.s. |
| 3 to 2 - 4 to 2 | -4.06 | 4.63 | -0.88 | 0.380 | 0.984 | n.s. |
| 3 to 2 - 5 to 2 | -0.31 | 4.60 | -0.07 | 0.945 | 1.000 | n.s. |
| 4 to 2 - 5 to 2 | 3.75 | 4.60 | 0.81 | 0.415 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.440, η²_G = 0.027
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -1.34 | 18 | = 0.526 | -0.30 [-0.79, 0.17] | small | n.s. |
| 1 to 2 vs 3 to 2 | -0.18 | 18 | = 0.858 | -0.03 [-0.44, 0.49] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -1.55 | 18 | = 0.526 | -0.46 [-0.85, 0.07] | small | n.s. |
| 1 to 2 vs 5 to 2 | -0.33 | 18 | = 0.858 | -0.10 [-0.43, 0.45] | negligible | n.s. |
| 2 to 2 vs 3 to 2 | 0.96 | 18 | = 0.585 | 0.25 [-0.50, 0.41] | small | n.s. |
| 2 to 2 vs 4 to 2 | -0.29 | 18 | = 0.858 | -0.08 [-0.61, 0.29] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 1.16 | 18 | = 0.526 | 0.22 [-0.47, 0.42] | small | n.s. |
| 3 to 2 vs 4 to 2 | -1.55 | 18 | = 0.526 | -0.38 [-0.60, 0.29] | small | n.s. |
| 3 to 2 vs 5 to 2 | -0.19 | 18 | = 0.858 | -0.06 [-0.48, 0.40] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.17 | 18 | = 0.526 | 0.36 [-0.23, 0.62] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 481.84, BIC = 503.73
- **2 to 2 vs 1 to 2**: *β* = -0.20, *SE* = 0.474, *z* = -0.427, *p* = 0.670
- **3 to 2 vs 1 to 2**: *β* = -0.10, *SE* = 0.470, *z* = -0.203, *p* = 0.839
- **4 to 2 vs 1 to 2**: *β* = -0.66, *SE* = 0.458, *z* = -1.430, *p* = 0.153
- **5 to 2 vs 1 to 2**: *β* = -0.78, *SE* = 0.463, *z* = -1.681, *p* = 0.093
- **SNR**: *β* = -0.44, *SE* = 0.078, *z* = -5.658, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 0.20 | 0.47 | 0.43 | 0.670 | 0.988 | n.s. |
| 1 to 2 - 3 to 2 | 0.10 | 0.47 | 0.20 | 0.839 | 0.991 | n.s. |
| 1 to 2 - 4 to 2 | 0.66 | 0.46 | 1.43 | 0.153 | 0.735 | n.s. |
| 1 to 2 - 5 to 2 | 0.78 | 0.46 | 1.68 | 0.093 | 0.622 | n.s. |
| 2 to 2 - 3 to 2 | -0.11 | 0.48 | -0.22 | 0.823 | 0.991 | n.s. |
| 2 to 2 - 4 to 2 | 0.45 | 0.46 | 0.99 | 0.322 | 0.857 | n.s. |
| 2 to 2 - 5 to 2 | 0.58 | 0.48 | 1.20 | 0.231 | 0.834 | n.s. |
| 3 to 2 - 4 to 2 | 0.56 | 0.46 | 1.21 | 0.226 | 0.834 | n.s. |
| 3 to 2 - 5 to 2 | 0.68 | 0.46 | 1.49 | 0.137 | 0.734 | n.s. |
| 4 to 2 - 5 to 2 | 0.12 | 0.46 | 0.27 | 0.789 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.84, *p* = 0.030, η²_G = 0.048
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -1.08 | 18 | = 0.418 | -0.19 [-0.59, 0.35] | negligible | n.s. |
| 1 to 2 vs 3 to 2 | 0.79 | 18 | = 0.489 | 0.13 [-0.30, 0.65] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | 1.15 | 18 | = 0.418 | 0.26 [-0.24, 0.66] | small | n.s. |
| 1 to 2 vs 5 to 2 | 2.69 | 18 | = 0.075 | 0.50 [0.06, 1.00] | small | n.s. |
| 2 to 2 vs 3 to 2 | 1.42 | 18 | = 0.344 | 0.29 [-0.12, 0.81] | small | n.s. |
| 2 to 2 vs 4 to 2 | 1.74 | 18 | = 0.271 | 0.40 [-0.25, 0.65] | small | n.s. |
| 2 to 2 vs 5 to 2 | 3.04 | 18 | = 0.071 | 0.63 [0.03, 0.97] | medium | n.s. |
| 3 to 2 vs 4 to 2 | 0.61 | 18 | = 0.550 | 0.13 [-0.33, 0.56] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.69 | 18 | = 0.271 | 0.35 [0.00, 0.94] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.92 | 18 | = 0.465 | 0.20 [-0.13, 0.73] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 410.46, BIC = 427.61
- **2 to 2 vs 1 to 2**: *β* = -1.89, *SE* = 1.787, *z* = -1.056, *p* = 0.291
- **3 to 2 vs 1 to 2**: *β* = -0.52, *SE* = 1.959, *z* = -0.266, *p* = 0.790
- **4 to 2 vs 1 to 2**: *β* = 2.07, *SE* = 1.739, *z* = 1.190, *p* = 0.234
- **5 to 2 vs 1 to 2**: *β* = -2.78, *SE* = 1.780, *z* = -1.564, *p* = 0.118
- **SNR**: *β* = -0.04, *SE* = 0.496, *z* = -0.070, *p* = 0.944

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 1.89 | 1.79 | 1.06 | 0.291 | 0.798 | n.s. |
| 1 to 2 - 3 to 2 | 0.52 | 1.96 | 0.27 | 0.790 | 0.855 | n.s. |
| 1 to 2 - 4 to 2 | -2.07 | 1.74 | -1.19 | 0.234 | 0.798 | n.s. |
| 1 to 2 - 5 to 2 | 2.78 | 1.78 | 1.56 | 0.118 | 0.633 | n.s. |
| 2 to 2 - 3 to 2 | -1.37 | 1.91 | -0.71 | 0.475 | 0.855 | n.s. |
| 2 to 2 - 4 to 2 | -3.96 | 1.66 | -2.38 | 0.017 | 0.147 | n.s. |
| 2 to 2 - 5 to 2 | 0.90 | 1.62 | 0.55 | 0.580 | 0.855 | n.s. |
| 3 to 2 - 4 to 2 | -2.59 | 1.88 | -1.38 | 0.169 | 0.726 | n.s. |
| 3 to 2 - 5 to 2 | 2.26 | 1.90 | 1.19 | 0.234 | 0.798 | n.s. |
| 4 to 2 - 5 to 2 | 4.85 | 1.63 | 2.98 | 0.003 | 0.029 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.418, η²_G = 0.092
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -0.25 | 4 | = 0.905 | -0.12 [-0.76, 0.92] | negligible | n.s. |
| 1 to 2 vs 3 to 2 | -0.34 | 4 | = 0.905 | -0.11 [-1.20, 0.91] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -0.65 | 4 | = 0.905 | -0.35 [-1.16, 0.43] | small | n.s. |
| 1 to 2 vs 5 to 2 | 1.37 | 4 | = 0.745 | 0.40 [0.19, 2.20] | small | n.s. |
| 2 to 2 vs 3 to 2 | 0.00 | 4 | = 1.000 | 0.00 [-1.22, 0.67] | negligible | n.s. |
| 2 to 2 vs 4 to 2 | -0.78 | 4 | = 0.905 | -0.33 [-1.42, 0.15] | small | n.s. |
| 2 to 2 vs 5 to 2 | 2.24 | 4 | = 0.674 | 0.63 [-0.51, 0.84] | medium | n.s. |
| 3 to 2 vs 4 to 2 | -0.49 | 4 | = 0.905 | -0.28 [-1.36, 0.56] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.20 | 4 | = 0.745 | 0.57 [-0.45, 1.54] | medium | n.s. |
| 4 to 2 vs 5 to 2 | 1.87 | 4 | = 0.674 | 0.84 [0.10, 1.69] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 199.33, BIC = 216.48
- **2 to 2 vs 1 to 2**: *β* = 0.98, *SE* = 0.396, *z* = 2.485, *p* = 0.013
- **3 to 2 vs 1 to 2**: *β* = 0.65, *SE* = 0.435, *z* = 1.491, *p* = 0.136
- **4 to 2 vs 1 to 2**: *β* = 0.72, *SE* = 0.387, *z* = 1.860, *p* = 0.063
- **5 to 2 vs 1 to 2**: *β* = 0.79, *SE* = 0.385, *z* = 2.044, *p* = 0.041
- **SNR**: *β* = 0.78, *SE* = 0.104, *z* = 7.498, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | -0.98 | 0.40 | -2.48 | 0.013 | 0.122 | n.s. |
| 1 to 2 - 3 to 2 | -0.65 | 0.44 | -1.49 | 0.136 | 0.641 | n.s. |
| 1 to 2 - 4 to 2 | -0.72 | 0.39 | -1.86 | 0.063 | 0.405 | n.s. |
| 1 to 2 - 5 to 2 | -0.79 | 0.39 | -2.04 | 0.041 | 0.314 | n.s. |
| 2 to 2 - 3 to 2 | 0.33 | 0.42 | 0.80 | 0.423 | 0.963 | n.s. |
| 2 to 2 - 4 to 2 | 0.26 | 0.37 | 0.72 | 0.474 | 0.963 | n.s. |
| 2 to 2 - 5 to 2 | 0.20 | 0.36 | 0.55 | 0.585 | 0.970 | n.s. |
| 3 to 2 - 4 to 2 | -0.07 | 0.41 | -0.17 | 0.864 | 0.981 | n.s. |
| 3 to 2 - 5 to 2 | -0.14 | 0.41 | -0.34 | 0.733 | 0.981 | n.s. |
| 4 to 2 - 5 to 2 | -0.07 | 0.35 | -0.19 | 0.847 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.37, *p* = 0.289, η²_G = 0.212
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -1.70 | 4 | = 0.421 | -1.15 [-1.77, 0.16] | large | n.s. |
| 1 to 2 vs 3 to 2 | -1.68 | 4 | = 0.421 | -0.63 [-1.44, 0.72] | medium | n.s. |
| 1 to 2 vs 4 to 2 | -1.49 | 4 | = 0.423 | -1.24 [-1.35, 0.29] | large | n.s. |
| 1 to 2 vs 5 to 2 | -2.71 | 4 | = 0.421 | -1.31 [-2.17, -0.17] | large | n.s. |
| 2 to 2 vs 3 to 2 | 1.02 | 4 | = 0.609 | 0.67 [-0.93, 0.92] | medium | n.s. |
| 2 to 2 vs 4 to 2 | 0.87 | 4 | = 0.621 | 0.49 [-0.74, 0.69] | small | n.s. |
| 2 to 2 vs 5 to 2 | 0.23 | 4 | = 0.829 | 0.17 [-0.61, 0.74] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -0.44 | 4 | = 0.760 | -0.34 [-0.89, 0.96] | small | n.s. |
| 3 to 2 vs 5 to 2 | -2.17 | 4 | = 0.421 | -0.62 [-1.71, 0.35] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -0.61 | 4 | = 0.722 | -0.40 [-1.10, 0.30] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 825.61, BIC = 844.86
- **2 to 2 vs 1 to 2**: *β* = -9.33, *SE* = 12.055, *z* = -0.774, *p* = 0.439
- **3 to 2 vs 1 to 2**: *β* = 9.99, *SE* = 10.229, *z* = 0.977, *p* = 0.329
- **4 to 2 vs 1 to 2**: *β* = 5.60, *SE* = 10.254, *z* = 0.546, *p* = 0.585
- **5 to 2 vs 1 to 2**: *β* = -4.77, *SE* = 10.442, *z* = -0.457, *p* = 0.648
- **SNR**: *β* = 1.28, *SE* = 1.577, *z* = 0.814, *p* = 0.415

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 9.33 | 12.05 | 0.77 | 0.439 | 0.944 | n.s. |
| 1 to 2 - 3 to 2 | -9.99 | 10.23 | -0.98 | 0.329 | 0.931 | n.s. |
| 1 to 2 - 4 to 2 | -5.60 | 10.25 | -0.55 | 0.585 | 0.970 | n.s. |
| 1 to 2 - 5 to 2 | 4.77 | 10.44 | 0.46 | 0.648 | 0.970 | n.s. |
| 2 to 2 - 3 to 2 | -19.32 | 11.68 | -1.65 | 0.098 | 0.644 | n.s. |
| 2 to 2 - 4 to 2 | -14.93 | 11.60 | -1.29 | 0.198 | 0.829 | n.s. |
| 2 to 2 - 5 to 2 | -4.56 | 12.32 | -0.37 | 0.712 | 0.970 | n.s. |
| 3 to 2 - 4 to 2 | 4.39 | 9.90 | 0.44 | 0.657 | 0.970 | n.s. |
| 3 to 2 - 5 to 2 | 14.76 | 10.20 | 1.45 | 0.148 | 0.763 | n.s. |
| 4 to 2 - 5 to 2 | 10.37 | 10.36 | 1.00 | 0.317 | 0.931 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.45, *p* = 0.256, η²_G = 0.134
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -1.16 | 5 | = 0.518 | -0.44 [-0.87, 0.80] | small | n.s. |
| 1 to 2 vs 3 to 2 | -1.89 | 5 | = 0.404 | -0.91 [-0.90, 0.33] | large | n.s. |
| 1 to 2 vs 4 to 2 | -1.86 | 5 | = 0.404 | -1.00 [-0.89, 0.34] | large | n.s. |
| 1 to 2 vs 5 to 2 | -1.13 | 5 | = 0.518 | -0.83 [-0.61, 0.55] | large | n.s. |
| 2 to 2 vs 3 to 2 | -1.16 | 5 | = 0.518 | -0.42 [-1.38, 0.18] | small | n.s. |
| 2 to 2 vs 4 to 2 | -2.18 | 5 | = 0.404 | -0.50 [-1.08, 0.39] | medium | n.s. |
| 2 to 2 vs 5 to 2 | -0.52 | 5 | = 0.811 | -0.33 [-0.97, 0.48] | small | n.s. |
| 3 to 2 vs 4 to 2 | -0.25 | 5 | = 0.811 | -0.08 [-0.42, 0.65] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 0.27 | 5 | = 0.811 | 0.12 [-0.26, 0.82] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.44 | 5 | = 0.811 | 0.21 [-0.20, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 371.84, BIC = 391.10
- **2 to 2 vs 1 to 2**: *β* = -0.61, *SE* = 0.717, *z* = -0.847, *p* = 0.397
- **3 to 2 vs 1 to 2**: *β* = 1.05, *SE* = 0.608, *z* = 1.727, *p* = 0.084
- **4 to 2 vs 1 to 2**: *β* = 0.71, *SE* = 0.609, *z* = 1.170, *p* = 0.242
- **5 to 2 vs 1 to 2**: *β* = -0.80, *SE* = 0.624, *z* = -1.281, *p* = 0.200
- **SNR**: *β* = 0.64, *SE* = 0.102, *z* = 6.307, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 0.61 | 0.72 | 0.85 | 0.397 | 0.781 | n.s. |
| 1 to 2 - 3 to 2 | -1.05 | 0.61 | -1.73 | 0.084 | 0.410 | n.s. |
| 1 to 2 - 4 to 2 | -0.71 | 0.61 | -1.17 | 0.242 | 0.673 | n.s. |
| 1 to 2 - 5 to 2 | 0.80 | 0.62 | 1.28 | 0.200 | 0.673 | n.s. |
| 2 to 2 - 3 to 2 | -1.66 | 0.69 | -2.39 | 0.017 | 0.128 | n.s. |
| 2 to 2 - 4 to 2 | -1.32 | 0.69 | -1.91 | 0.056 | 0.333 | n.s. |
| 2 to 2 - 5 to 2 | 0.19 | 0.74 | 0.26 | 0.795 | 0.810 | n.s. |
| 3 to 2 - 4 to 2 | 0.34 | 0.59 | 0.58 | 0.565 | 0.810 | n.s. |
| 3 to 2 - 5 to 2 | 1.85 | 0.61 | 3.05 | 0.002 | 0.023 | * |
| 4 to 2 - 5 to 2 | 1.51 | 0.62 | 2.45 | 0.014 | 0.121 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.14, *p* = 0.013, η²_G = 0.202
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | 0.72 | 5 | = 0.560 | 0.31 [-0.49, 1.23] | small | n.s. |
| 1 to 2 vs 3 to 2 | -4.31 | 5 | = 0.076 | -1.08 [-0.96, 0.29] | large | n.s. |
| 1 to 2 vs 4 to 2 | -1.89 | 5 | = 0.235 | -0.70 [-0.87, 0.36] | medium | n.s. |
| 1 to 2 vs 5 to 2 | -0.77 | 5 | = 0.560 | -0.30 [-0.69, 0.47] | small | n.s. |
| 2 to 2 vs 3 to 2 | -3.51 | 5 | = 0.086 | -1.30 [-1.58, 0.05] | large | n.s. |
| 2 to 2 vs 4 to 2 | -2.38 | 5 | = 0.158 | -0.89 [-1.68, -0.01] | large | n.s. |
| 2 to 2 vs 5 to 2 | -1.09 | 5 | = 0.467 | -0.58 [-1.32, 0.22] | medium | n.s. |
| 3 to 2 vs 4 to 2 | 0.28 | 5 | = 0.790 | 0.07 [-0.28, 0.80] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 2.66 | 5 | = 0.149 | 0.81 [-0.13, 0.98] | large | n.s. |
| 4 to 2 vs 5 to 2 | 1.58 | 5 | = 0.291 | 0.51 [-0.38, 0.70] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.030) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.013) (no significant pairwise comparisons)

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
