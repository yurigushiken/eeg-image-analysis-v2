# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:23:44

---

## 1. Analysis Overview

**Total Measurements:** 448
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
| 1 to 2 | 24 | 96.17 ms | 11.65 | 2.38 | [84.00, 112.00] |
| 2 to 3 | 24 | 96.17 ms | 11.16 | 2.28 | [84.00, 112.00] |
| 3 to 4 | 24 | 100.17 ms | 10.04 | 2.05 | [84.00, 112.00] |
| 4 to 5 | 24 | 95.83 ms | 9.32 | 1.90 | [84.00, 112.00] |
| 5 to 6 | 16 | 101.00 ms | 9.06 | 2.27 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -0.37 µV | 2.00 | 0.41 | [-3.35, 4.51] |
| 2 to 3 | 24 | -1.47 µV | 2.19 | 0.45 | [-5.76, 2.45] |
| 3 to 4 | 24 | -1.71 µV | 1.82 | 0.37 | [-5.20, 2.48] |
| 4 to 5 | 24 | -4.18 µV | 5.10 | 1.04 | [-18.83, 3.46] |
| 5 to 6 | 16 | -4.44 µV | 4.55 | 1.14 | [-17.83, 1.30] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 172.00 ms | 18.46 | 3.77 | [144.00, 204.00] |
| 2 to 3 | 24 | 170.00 ms | 20.60 | 4.20 | [136.00, 204.00] |
| 3 to 4 | 24 | 165.50 ms | 18.83 | 3.84 | [136.00, 204.00] |
| 4 to 5 | 24 | 167.17 ms | 19.77 | 4.04 | [136.00, 196.00] |
| 5 to 6 | 16 | 170.75 ms | 24.60 | 6.15 | [136.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -5.50 µV | 2.36 | 0.48 | [-10.03, -0.26] |
| 2 to 3 | 24 | -5.03 µV | 2.41 | 0.49 | [-10.61, 0.67] |
| 3 to 4 | 24 | -5.74 µV | 2.21 | 0.45 | [-10.53, -1.52] |
| 4 to 5 | 24 | -6.76 µV | 4.00 | 0.82 | [-16.53, 0.62] |
| 5 to 6 | 16 | -5.20 µV | 4.53 | 1.13 | [-12.77, 2.93] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 97.50 ms | 14.44 | 2.95 | [84.00, 116.00] |
| 2 to 3 | 24 | 100.67 ms | 13.64 | 2.78 | [84.00, 116.00] |
| 3 to 4 | 24 | 101.00 ms | 11.99 | 2.45 | [84.00, 116.00] |
| 4 to 5 | 24 | 98.50 ms | 11.18 | 2.28 | [84.00, 116.00] |
| 5 to 6 | 16 | 103.00 ms | 10.78 | 2.70 | [84.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 1.16 µV | 1.95 | 0.40 | [-3.63, 4.29] |
| 2 to 3 | 24 | 1.68 µV | 2.33 | 0.48 | [-3.02, 6.87] |
| 3 to 4 | 24 | 2.34 µV | 2.17 | 0.44 | [-1.38, 7.39] |
| 4 to 5 | 24 | 3.72 µV | 4.95 | 1.01 | [-3.43, 19.20] |
| 5 to 6 | 16 | 4.26 µV | 4.85 | 1.21 | [-4.67, 16.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 483.17 ms | 35.62 | 7.27 | [440.00, 536.00] |
| 2 to 3 | 24 | 472.00 ms | 33.17 | 6.77 | [440.00, 536.00] |
| 3 to 4 | 24 | 496.17 ms | 32.99 | 6.74 | [440.00, 536.00] |
| 4 to 5 | 24 | 494.83 ms | 32.72 | 6.68 | [440.00, 536.00] |
| 5 to 6 | 16 | 485.25 ms | 40.47 | 10.12 | [440.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 3.99 µV | 3.80 | 0.78 | [-3.51, 11.52] |
| 2 to 3 | 24 | 4.53 µV | 4.42 | 0.90 | [-3.66, 13.70] |
| 3 to 4 | 24 | 4.26 µV | 4.69 | 0.96 | [-5.10, 12.86] |
| 4 to 5 | 24 | 4.52 µV | 5.43 | 1.11 | [-5.31, 13.88] |
| 5 to 6 | 16 | 3.75 µV | 6.12 | 1.53 | [-7.31, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 850.68, BIC = 872.43
- **2 to 3 vs 1 to 2**: *β* = -0.02, *SE* = 2.758, *z* = -0.007, *p* = 0.995
- **3 to 4 vs 1 to 2**: *β* = 4.04, *SE* = 2.763, *z* = 1.463, *p* = 0.144
- **4 to 5 vs 1 to 2**: *β* = -0.38, *SE* = 2.766, *z* = -0.139, *p* = 0.890
- **5 to 6 vs 1 to 2**: *β* = 4.77, *SE* = 3.117, *z* = 1.530, *p* = 0.126
- **SNR**: *β* = 0.13, *SE* = 0.597, *z* = 0.223, *p* = 0.823

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 0.02 | 2.76 | 0.01 | 0.995 | 0.999 | n.s. |
| 1 to 2 - 3 to 4 | -4.04 | 2.76 | -1.46 | 0.144 | 0.658 | n.s. |
| 1 to 2 - 4 to 5 | 0.38 | 2.77 | 0.14 | 0.890 | 0.999 | n.s. |
| 1 to 2 - 5 to 6 | -4.77 | 3.12 | -1.53 | 0.126 | 0.658 | n.s. |
| 2 to 3 - 3 to 4 | -4.06 | 2.77 | -1.47 | 0.143 | 0.658 | n.s. |
| 2 to 3 - 4 to 5 | 0.37 | 2.76 | 0.13 | 0.895 | 0.999 | n.s. |
| 2 to 3 - 5 to 6 | -4.79 | 3.11 | -1.54 | 0.124 | 0.658 | n.s. |
| 3 to 4 - 4 to 5 | 4.43 | 2.79 | 1.59 | 0.112 | 0.658 | n.s. |
| 3 to 4 - 5 to 6 | -0.73 | 3.14 | -0.23 | 0.817 | 0.999 | n.s. |
| 4 to 5 - 5 to 6 | -5.15 | 3.11 | -1.66 | 0.097 | 0.641 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.41, *p* = 0.241, η²_G = 0.067
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.76 | 15 | = 0.580 | -0.28 [-0.42, 0.42] | small | n.s. |
| 1 to 2 vs 3 to 4 | -1.87 | 15 | = 0.338 | -0.64 [-0.68, 0.17] | medium | n.s. |
| 1 to 2 vs 4 to 5 | -0.75 | 15 | = 0.580 | -0.27 [-0.40, 0.45] | small | n.s. |
| 1 to 2 vs 5 to 6 | -1.97 | 15 | = 0.338 | -0.69 [-1.06, 0.07] | medium | n.s. |
| 2 to 3 vs 3 to 4 | -0.84 | 15 | = 0.580 | -0.36 [-0.67, 0.19] | small | n.s. |
| 2 to 3 vs 4 to 5 | 0.07 | 15 | = 1.000 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | -1.17 | 15 | = 0.522 | -0.39 [-0.84, 0.25] | small | n.s. |
| 3 to 4 vs 4 to 5 | 1.26 | 15 | = 0.522 | 0.41 [-0.08, 0.79] | small | n.s. |
| 3 to 4 vs 5 to 6 | 0.00 | 15 | = 1.000 | 0.00 [-0.53, 0.53] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -1.75 | 15 | = 0.338 | -0.44 [-0.99, 0.12] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 578.92, BIC = 600.67
- **2 to 3 vs 1 to 2**: *β* = -0.99, *SE* = 0.819, *z* = -1.212, *p* = 0.226
- **3 to 4 vs 1 to 2**: *β* = -1.59, *SE* = 0.821, *z* = -1.943, *p* = 0.052
- **4 to 5 vs 1 to 2**: *β* = -3.51, *SE* = 0.822, *z* = -4.270, *p* < .001
- **5 to 6 vs 1 to 2**: *β* = -3.95, *SE* = 0.934, *z* = -4.235, *p* < .001
- **SNR**: *β* = -0.78, *SE* = 0.177, *z* = -4.431, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 0.99 | 0.82 | 1.21 | 0.226 | 0.536 | n.s. |
| 1 to 2 - 3 to 4 | 1.59 | 0.82 | 1.94 | 0.052 | 0.193 | n.s. |
| 1 to 2 - 4 to 5 | 3.51 | 0.82 | 4.27 | < .001 | < .001 | *** |
| 1 to 2 - 5 to 6 | 3.95 | 0.93 | 4.24 | < .001 | < .001 | *** |
| 2 to 3 - 3 to 4 | 0.60 | 0.82 | 0.73 | 0.464 | 0.713 | n.s. |
| 2 to 3 - 4 to 5 | 2.52 | 0.82 | 3.07 | 0.002 | 0.015 | * |
| 2 to 3 - 5 to 6 | 2.96 | 0.93 | 3.18 | 0.001 | 0.012 | * |
| 3 to 4 - 4 to 5 | 1.91 | 0.83 | 2.31 | 0.021 | 0.100 | n.s. |
| 3 to 4 - 5 to 6 | 2.36 | 0.94 | 2.51 | 0.012 | 0.070 | n.s. |
| 4 to 5 - 5 to 6 | 0.45 | 0.93 | 0.48 | 0.632 | 0.713 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.49, *p* < .001, η²_G = 0.230
- Greenhouse-Geisser corrected: *p* = 0.006 (ε = 0.599)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | 1.02 | 15 | = 0.405 | 0.33 [-0.01, 0.87] | small | n.s. |
| 1 to 2 vs 3 to 4 | 1.69 | 15 | = 0.160 | 0.63 [0.11, 1.02] | medium | n.s. |
| 1 to 2 vs 4 to 5 | 2.87 | 15 | = 0.035 | 1.03 [0.29, 1.25] | large | * |
| 1 to 2 vs 5 to 6 | 3.21 | 15 | = 0.035 | 1.24 [0.19, 1.42] | large | * |
| 2 to 3 vs 3 to 4 | 0.79 | 15 | = 0.491 | 0.27 [-0.33, 0.52] | small | n.s. |
| 2 to 3 vs 4 to 5 | 2.34 | 15 | = 0.068 | 0.83 [0.05, 0.95] | large | n.s. |
| 2 to 3 vs 5 to 6 | 2.78 | 15 | = 0.035 | 1.05 [0.10, 1.29] | large | * |
| 3 to 4 vs 4 to 5 | 2.16 | 15 | = 0.079 | 0.69 [0.09, 1.00] | medium | n.s. |
| 3 to 4 vs 5 to 6 | 3.00 | 15 | = 0.035 | 0.92 [0.15, 1.35] | large | * |
| 4 to 5 vs 5 to 6 | 0.56 | 15 | = 0.580 | 0.22 [-0.39, 0.68] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 979.28, BIC = 1001.02
- **2 to 3 vs 1 to 2**: *β* = -1.81, *SE* = 4.447, *z* = -0.408, *p* = 0.683
- **3 to 4 vs 1 to 2**: *β* = -6.22, *SE* = 4.449, *z* = -1.399, *p* = 0.162
- **4 to 5 vs 1 to 2**: *β* = -5.22, *SE* = 4.453, *z* = -1.172, *p* = 0.241
- **5 to 6 vs 1 to 2**: *β* = -0.99, *SE* = 5.179, *z* = -0.192, *p* = 0.848
- **SNR**: *β* = 0.94, *SE* = 0.639, *z* = 1.480, *p* = 0.139

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 1.81 | 4.45 | 0.41 | 0.683 | 0.990 | n.s. |
| 1 to 2 - 3 to 4 | 6.22 | 4.45 | 1.40 | 0.162 | 0.829 | n.s. |
| 1 to 2 - 4 to 5 | 5.22 | 4.45 | 1.17 | 0.241 | 0.917 | n.s. |
| 1 to 2 - 5 to 6 | 0.99 | 5.18 | 0.19 | 0.848 | 0.994 | n.s. |
| 2 to 3 - 3 to 4 | 4.41 | 4.45 | 0.99 | 0.321 | 0.948 | n.s. |
| 2 to 3 - 4 to 5 | 3.40 | 4.46 | 0.76 | 0.446 | 0.962 | n.s. |
| 2 to 3 - 5 to 6 | -0.82 | 5.15 | -0.16 | 0.873 | 0.994 | n.s. |
| 3 to 4 - 4 to 5 | -1.01 | 4.47 | -0.23 | 0.822 | 0.994 | n.s. |
| 3 to 4 - 5 to 6 | -5.23 | 5.14 | -1.02 | 0.309 | 0.948 | n.s. |
| 4 to 5 - 5 to 6 | -4.23 | 5.24 | -0.81 | 0.420 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.66, *p* = 0.622, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.32 | 15 | = 0.755 | -0.31 [-0.34, 0.50] | small | n.s. |
| 1 to 2 vs 3 to 4 | 0.27 | 15 | = 0.959 | 0.05 [-0.12, 0.75] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.24 | 15 | = 0.959 | 0.07 [-0.22, 0.63] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -0.16 | 15 | = 0.959 | -0.05 [-0.57, 0.49] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 1.26 | 15 | = 0.755 | 0.34 [-0.24, 0.61] | small | n.s. |
| 2 to 3 vs 4 to 5 | 1.43 | 15 | = 0.755 | 0.35 [-0.31, 0.54] | small | n.s. |
| 2 to 3 vs 5 to 6 | 0.86 | 15 | = 0.959 | 0.21 [-0.32, 0.75] | small | n.s. |
| 3 to 4 vs 4 to 5 | 0.05 | 15 | = 0.959 | 0.01 [-0.52, 0.33] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | -0.42 | 15 | = 0.959 | -0.09 [-0.64, 0.43] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -0.51 | 15 | = 0.959 | -0.10 [-0.66, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.64, BIC = 572.39
- **2 to 3 vs 1 to 2**: *β* = 0.40, *SE* = 0.671, *z* = 0.594, *p* = 0.552
- **3 to 4 vs 1 to 2**: *β* = -0.35, *SE* = 0.671, *z* = -0.521, *p* = 0.602
- **4 to 5 vs 1 to 2**: *β* = -1.09, *SE* = 0.671, *z* = -1.629, *p* = 0.103
- **5 to 6 vs 1 to 2**: *β* = -0.37, *SE* = 0.779, *z* = -0.478, *p* = 0.633
- **SNR**: *β* = -0.39, *SE* = 0.094, *z* = -4.158, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.40 | 0.67 | -0.59 | 0.552 | 0.960 | n.s. |
| 1 to 2 - 3 to 4 | 0.35 | 0.67 | 0.52 | 0.602 | 0.960 | n.s. |
| 1 to 2 - 4 to 5 | 1.09 | 0.67 | 1.63 | 0.103 | 0.625 | n.s. |
| 1 to 2 - 5 to 6 | 0.37 | 0.78 | 0.48 | 0.633 | 0.960 | n.s. |
| 2 to 3 - 3 to 4 | 0.75 | 0.67 | 1.12 | 0.264 | 0.914 | n.s. |
| 2 to 3 - 4 to 5 | 1.49 | 0.67 | 2.22 | 0.027 | 0.236 | n.s. |
| 2 to 3 - 5 to 6 | 0.77 | 0.78 | 0.99 | 0.320 | 0.914 | n.s. |
| 3 to 4 - 4 to 5 | 0.74 | 0.67 | 1.11 | 0.269 | 0.914 | n.s. |
| 3 to 4 - 5 to 6 | 0.02 | 0.77 | 0.03 | 0.977 | 0.977 | n.s. |
| 4 to 5 - 5 to 6 | -0.72 | 0.79 | -0.92 | 0.360 | 0.914 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.43, *p* = 0.787, η²_G = 0.016
- Greenhouse-Geisser corrected: *p* = 0.695 (ε = 0.615)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | 0.11 | 15 | = 0.912 | 0.03 [-0.64, 0.21] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -0.22 | 15 | = 0.912 | -0.04 [-0.30, 0.54] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.82 | 15 | = 0.912 | 0.25 [-0.12, 0.74] | small | n.s. |
| 1 to 2 vs 5 to 6 | -0.34 | 15 | = 0.912 | -0.11 [-0.62, 0.45] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | -0.30 | 15 | = 0.912 | -0.07 [-0.12, 0.74] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.80 | 15 | = 0.912 | 0.24 [-0.00, 0.88] | small | n.s. |
| 2 to 3 vs 5 to 6 | -0.42 | 15 | = 0.912 | -0.13 [-0.64, 0.43] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 0.88 | 15 | = 0.912 | 0.29 [-0.14, 0.72] | small | n.s. |
| 3 to 4 vs 5 to 6 | -0.25 | 15 | = 0.912 | -0.08 [-0.60, 0.47] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -0.99 | 15 | = 0.912 | -0.28 [-0.79, 0.29] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 894.69, BIC = 916.44
- **2 to 3 vs 1 to 2**: *β* = 3.18, *SE* = 3.386, *z* = 0.940, *p* = 0.347
- **3 to 4 vs 1 to 2**: *β* = 3.53, *SE* = 3.398, *z* = 1.039, *p* = 0.299
- **4 to 5 vs 1 to 2**: *β* = 1.00, *SE* = 3.380, *z* = 0.296, *p* = 0.767
- **5 to 6 vs 1 to 2**: *β* = 5.42, *SE* = 3.824, *z* = 1.419, *p* = 0.156
- **SNR**: *β* = 0.07, *SE* = 0.830, *z* = 0.088, *p* = 0.930

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -3.18 | 3.39 | -0.94 | 0.347 | 0.949 | n.s. |
| 1 to 2 - 3 to 4 | -3.53 | 3.40 | -1.04 | 0.299 | 0.942 | n.s. |
| 1 to 2 - 4 to 5 | -1.00 | 3.38 | -0.30 | 0.767 | 0.974 | n.s. |
| 1 to 2 - 5 to 6 | -5.42 | 3.82 | -1.42 | 0.156 | 0.817 | n.s. |
| 2 to 3 - 3 to 4 | -0.35 | 3.38 | -0.10 | 0.918 | 0.974 | n.s. |
| 2 to 3 - 4 to 5 | 2.18 | 3.39 | 0.65 | 0.519 | 0.974 | n.s. |
| 2 to 3 - 5 to 6 | -2.24 | 3.85 | -0.58 | 0.560 | 0.974 | n.s. |
| 3 to 4 - 4 to 5 | 2.53 | 3.40 | 0.74 | 0.456 | 0.974 | n.s. |
| 3 to 4 - 5 to 6 | -1.89 | 3.87 | -0.49 | 0.625 | 0.974 | n.s. |
| 4 to 5 - 5 to 6 | -4.43 | 3.82 | -1.16 | 0.247 | 0.922 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.48, *p* = 0.752, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.31 | 15 | = 0.865 | -0.12 [-0.57, 0.28] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -0.87 | 15 | = 0.865 | -0.29 [-0.62, 0.23] | small | n.s. |
| 1 to 2 vs 4 to 5 | -0.11 | 15 | = 0.916 | -0.04 [-0.48, 0.36] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -1.20 | 15 | = 0.865 | -0.39 [-0.85, 0.24] | small | n.s. |
| 2 to 3 vs 3 to 4 | -0.52 | 15 | = 0.865 | -0.17 [-0.44, 0.40] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.30 | 15 | = 0.865 | 0.10 [-0.29, 0.56] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | -0.66 | 15 | = 0.865 | -0.26 [-0.70, 0.37] | small | n.s. |
| 3 to 4 vs 4 to 5 | 0.79 | 15 | = 0.865 | 0.28 [-0.26, 0.59] | small | n.s. |
| 3 to 4 vs 5 to 6 | -0.29 | 15 | = 0.865 | -0.08 [-0.61, 0.46] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -1.19 | 15 | = 0.865 | -0.40 [-0.84, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 592.16, BIC = 613.91
- **2 to 3 vs 1 to 2**: *β* = 0.64, *SE* = 0.851, *z* = 0.752, *p* = 0.452
- **3 to 4 vs 1 to 2**: *β* = 1.39, *SE* = 0.854, *z* = 1.629, *p* = 0.103
- **4 to 5 vs 1 to 2**: *β* = 2.56, *SE* = 0.849, *z* = 3.012, *p* = 0.003
- **5 to 6 vs 1 to 2**: *β* = 3.07, *SE* = 0.968, *z* = 3.177, *p* = 0.001
- **SNR**: *β* = 0.50, *SE* = 0.213, *z* = 2.334, *p* = 0.020

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.64 | 0.85 | -0.75 | 0.452 | 0.758 | n.s. |
| 1 to 2 - 3 to 4 | -1.39 | 0.85 | -1.63 | 0.103 | 0.420 | n.s. |
| 1 to 2 - 4 to 5 | -2.56 | 0.85 | -3.01 | 0.003 | 0.023 | * |
| 1 to 2 - 5 to 6 | -3.07 | 0.97 | -3.18 | 0.001 | 0.015 | * |
| 2 to 3 - 3 to 4 | -0.75 | 0.85 | -0.88 | 0.377 | 0.758 | n.s. |
| 2 to 3 - 4 to 5 | -1.92 | 0.85 | -2.26 | 0.024 | 0.157 | n.s. |
| 2 to 3 - 5 to 6 | -2.43 | 0.97 | -2.50 | 0.012 | 0.095 | n.s. |
| 3 to 4 - 4 to 5 | -1.17 | 0.85 | -1.37 | 0.172 | 0.529 | n.s. |
| 3 to 4 - 5 to 6 | -1.68 | 0.98 | -1.72 | 0.086 | 0.418 | n.s. |
| 4 to 5 - 5 to 6 | -0.51 | 0.97 | -0.53 | 0.595 | 0.758 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.88, *p* = 0.007, η²_G = 0.153
- Greenhouse-Geisser corrected: *p* = 0.024 (ε = 0.598)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.98 | 15 | = 0.381 | -0.28 [-0.67, 0.19] | small | n.s. |
| 1 to 2 vs 3 to 4 | -2.73 | 15 | = 0.077 | -0.82 [-0.99, -0.09] | large | n.s. |
| 1 to 2 vs 4 to 5 | -2.28 | 15 | = 0.094 | -0.80 [-0.94, -0.05] | large | n.s. |
| 1 to 2 vs 5 to 6 | -2.91 | 15 | = 0.077 | -1.03 [-1.33, -0.13] | large | n.s. |
| 2 to 3 vs 3 to 4 | -1.30 | 15 | = 0.265 | -0.43 [-0.69, 0.17] | small | n.s. |
| 2 to 3 vs 4 to 5 | -1.89 | 15 | = 0.129 | -0.65 [-0.82, 0.05] | medium | n.s. |
| 2 to 3 vs 5 to 6 | -2.46 | 15 | = 0.089 | -0.85 [-1.19, -0.03] | large | n.s. |
| 3 to 4 vs 4 to 5 | -1.41 | 15 | = 0.256 | -0.48 [-0.72, 0.14] | small | n.s. |
| 3 to 4 vs 5 to 6 | -2.05 | 15 | = 0.116 | -0.66 [-1.08, 0.05] | medium | n.s. |
| 4 to 5 vs 5 to 6 | -0.23 | 15 | = 0.818 | -0.07 [-0.59, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1120.83, BIC = 1142.58
- **2 to 3 vs 1 to 2**: *β* = -10.92, *SE* = 9.274, *z* = -1.178, *p* = 0.239
- **3 to 4 vs 1 to 2**: *β* = 13.36, *SE* = 9.309, *z* = 1.435, *p* = 0.151
- **4 to 5 vs 1 to 2**: *β* = 11.78, *SE* = 9.250, *z* = 1.273, *p* = 0.203
- **5 to 6 vs 1 to 2**: *β* = 2.30, *SE* = 10.473, *z* = 0.219, *p* = 0.826
- **SNR**: *β* = -0.30, *SE* = 0.902, *z* = -0.332, *p* = 0.740

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 10.92 | 9.27 | 1.18 | 0.239 | 0.796 | n.s. |
| 1 to 2 - 3 to 4 | -13.36 | 9.31 | -1.44 | 0.151 | 0.730 | n.s. |
| 1 to 2 - 4 to 5 | -11.78 | 9.25 | -1.27 | 0.203 | 0.796 | n.s. |
| 1 to 2 - 5 to 6 | -2.30 | 10.47 | -0.22 | 0.826 | 0.970 | n.s. |
| 2 to 3 - 3 to 4 | -24.28 | 9.25 | -2.62 | 0.009 | 0.083 | n.s. |
| 2 to 3 - 4 to 5 | -22.70 | 9.25 | -2.45 | 0.014 | 0.121 | n.s. |
| 2 to 3 - 5 to 6 | -13.22 | 10.57 | -1.25 | 0.211 | 0.796 | n.s. |
| 3 to 4 - 4 to 5 | 1.59 | 9.28 | 0.17 | 0.864 | 0.970 | n.s. |
| 3 to 4 - 5 to 6 | 11.06 | 10.63 | 1.04 | 0.298 | 0.796 | n.s. |
| 4 to 5 - 5 to 6 | 9.48 | 10.51 | 0.90 | 0.367 | 0.796 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.94, *p* = 0.116, η²_G = 0.085
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | 0.83 | 15 | = 0.560 | 0.20 [-0.12, 0.75] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -1.12 | 15 | = 0.466 | -0.39 [-0.69, 0.17] | small | n.s. |
| 1 to 2 vs 4 to 5 | -2.01 | 15 | = 0.316 | -0.73 [-0.69, 0.17] | medium | n.s. |
| 1 to 2 vs 5 to 6 | -0.57 | 15 | = 0.643 | -0.21 [-0.68, 0.39] | small | n.s. |
| 2 to 3 vs 3 to 4 | -1.51 | 15 | = 0.379 | -0.57 [-0.93, -0.04] | medium | n.s. |
| 2 to 3 vs 4 to 5 | -2.81 | 15 | = 0.132 | -0.90 [-1.02, -0.11] | large | n.s. |
| 2 to 3 vs 5 to 6 | -1.17 | 15 | = 0.466 | -0.38 [-0.84, 0.25] | small | n.s. |
| 3 to 4 vs 4 to 5 | -0.78 | 15 | = 0.560 | -0.30 [-0.40, 0.45] | small | n.s. |
| 3 to 4 vs 5 to 6 | 0.42 | 15 | = 0.679 | 0.15 [-0.43, 0.64] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | 1.66 | 15 | = 0.379 | 0.43 [-0.14, 0.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 639.87, BIC = 661.62
- **2 to 3 vs 1 to 2**: *β* = 0.39, *SE* = 0.925, *z* = 0.425, *p* = 0.671
- **3 to 4 vs 1 to 2**: *β* = 0.06, *SE* = 0.930, *z* = 0.062, *p* = 0.951
- **4 to 5 vs 1 to 2**: *β* = 0.47, *SE* = 0.921, *z* = 0.510, *p* = 0.610
- **5 to 6 vs 1 to 2**: *β* = -0.67, *SE* = 1.060, *z* = -0.627, *p* = 0.531
- **SNR**: *β* = 0.18, *SE* = 0.111, *z* = 1.621, *p* = 0.105

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.39 | 0.92 | -0.42 | 0.671 | 0.997 | n.s. |
| 1 to 2 - 3 to 4 | -0.06 | 0.93 | -0.06 | 0.951 | 0.997 | n.s. |
| 1 to 2 - 4 to 5 | -0.47 | 0.92 | -0.51 | 0.610 | 0.997 | n.s. |
| 1 to 2 - 5 to 6 | 0.66 | 1.06 | 0.63 | 0.531 | 0.996 | n.s. |
| 2 to 3 - 3 to 4 | 0.34 | 0.92 | 0.36 | 0.716 | 0.997 | n.s. |
| 2 to 3 - 4 to 5 | -0.08 | 0.92 | -0.08 | 0.934 | 0.997 | n.s. |
| 2 to 3 - 5 to 6 | 1.06 | 1.08 | 0.98 | 0.326 | 0.971 | n.s. |
| 3 to 4 - 4 to 5 | -0.41 | 0.92 | -0.45 | 0.656 | 0.997 | n.s. |
| 3 to 4 - 5 to 6 | 0.72 | 1.09 | 0.67 | 0.506 | 0.996 | n.s. |
| 4 to 5 - 5 to 6 | 1.13 | 1.07 | 1.06 | 0.287 | 0.966 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.23, *p* = 0.308, η²_G = 0.028
- Greenhouse-Geisser corrected: *p* = 0.309 (ε = 0.566)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.30 | 15 | = 0.564 | -0.25 [-0.58, 0.27] | small | n.s. |
| 1 to 2 vs 3 to 4 | -1.12 | 15 | = 0.564 | -0.17 [-0.50, 0.35] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | -1.41 | 15 | = 0.564 | -0.41 [-0.52, 0.33] | small | n.s. |
| 1 to 2 vs 5 to 6 | 0.36 | 15 | = 0.740 | 0.11 [-0.44, 0.62] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 0.34 | 15 | = 0.740 | 0.05 [-0.34, 0.50] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | -0.67 | 15 | = 0.644 | -0.17 [-0.42, 0.42] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | 1.15 | 15 | = 0.564 | 0.29 [-0.26, 0.83] | small | n.s. |
| 3 to 4 vs 4 to 5 | -0.82 | 15 | = 0.607 | -0.21 [-0.47, 0.37] | small | n.s. |
| 3 to 4 vs 5 to 6 | 0.93 | 15 | = 0.607 | 0.23 [-0.31, 0.77] | small | n.s. |
| 4 to 5 vs 5 to 6 | 2.25 | 15 | = 0.398 | 0.41 [-0.01, 1.14] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than 4 to 5 (*d* = 1.03)
  - 1 to 2 showed greater amplitude than 5 to 6 (*d* = 1.24)
  - 2 to 3 showed greater amplitude than 5 to 6 (*d* = 1.05)
  - 3 to 4 showed greater amplitude than 5 to 6 (*d* = 0.92)
**P1 amplitude:** Significant main effect of condition (*p* = 0.007) (no significant pairwise comparisons)

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
