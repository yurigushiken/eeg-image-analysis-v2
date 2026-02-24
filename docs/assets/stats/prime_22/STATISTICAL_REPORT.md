# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:30:41

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
| 2a | 24 | 106.00 ms | 13.13 | 2.68 | [84.00, 128.00] |
| 2b | 24 | 104.67 ms | 15.45 | 3.15 | [84.00, 128.00] |
| 2c | 24 | 108.50 ms | 17.74 | 3.62 | [84.00, 128.00] |
| 2d | 24 | 114.00 ms | 12.54 | 2.56 | [92.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 24 | -5.05 µV | 4.65 | 0.95 | [-14.46, 1.38] |
| 2b | 24 | -3.11 µV | 3.58 | 0.73 | [-10.37, 3.74] |
| 2c | 24 | -3.51 µV | 3.60 | 0.73 | [-11.54, 4.15] |
| 2d | 24 | -3.30 µV | 3.40 | 0.69 | [-12.12, 2.39] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 24 | 175.50 ms | 23.83 | 4.87 | [140.00, 212.00] |
| 2b | 24 | 167.17 ms | 21.23 | 4.33 | [140.00, 204.00] |
| 2c | 24 | 180.83 ms | 21.56 | 4.40 | [148.00, 212.00] |
| 2d | 24 | 168.83 ms | 19.06 | 3.89 | [140.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 24 | -7.10 µV | 4.58 | 0.94 | [-17.87, 1.95] |
| 2b | 24 | -6.24 µV | 3.92 | 0.80 | [-14.05, 0.95] |
| 2c | 24 | -5.17 µV | 2.63 | 0.54 | [-9.94, -0.77] |
| 2d | 24 | -5.53 µV | 3.21 | 0.66 | [-12.00, -0.51] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 24 | 103.83 ms | 18.44 | 3.76 | [64.00, 128.00] |
| 2b | 24 | 90.67 ms | 20.52 | 4.19 | [64.00, 128.00] |
| 2c | 24 | 106.50 ms | 20.66 | 4.22 | [64.00, 128.00] |
| 2d | 24 | 103.83 ms | 19.96 | 4.08 | [64.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 24 | 5.54 µV | 3.72 | 0.76 | [-1.56, 12.57] |
| 2b | 24 | 3.62 µV | 2.34 | 0.48 | [-0.66, 8.58] |
| 2c | 24 | 3.97 µV | 3.19 | 0.65 | [-0.81, 10.50] |
| 2d | 24 | 3.63 µV | 2.29 | 0.47 | [-0.97, 7.42] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 24 | 463.50 ms | 14.93 | 3.05 | [444.00, 484.00] |
| 2b | 24 | 460.00 ms | 16.26 | 3.32 | [444.00, 484.00] |
| 2c | 24 | 467.00 ms | 14.02 | 2.86 | [444.00, 484.00] |
| 2d | 24 | 461.50 ms | 13.95 | 2.85 | [444.00, 484.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 24 | 6.04 µV | 4.66 | 0.95 | [-0.91, 17.25] |
| 2b | 24 | 2.12 µV | 4.10 | 0.84 | [-3.73, 10.27] |
| 2c | 24 | 1.51 µV | 3.54 | 0.72 | [-6.58, 8.14] |
| 2d | 24 | 1.26 µV | 3.85 | 0.79 | [-10.80, 8.33] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 800.03, BIC = 817.98
- **2b vs 2a**: *β* = -1.33, *SE* = 4.082, *z* = -0.325, *p* = 0.745
- **2c vs 2a**: *β* = 2.50, *SE* = 4.073, *z* = 0.614, *p* = 0.539
- **2d vs 2a**: *β* = 8.00, *SE* = 4.073, *z* = 1.965, *p* = 0.049
- **SNR**: *β* = -0.02, *SE* = 1.207, *z* = -0.017, *p* = 0.986

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 1.33 | 4.08 | 0.33 | 0.745 | 0.788 | n.s. |
| 2a - 2c | -2.50 | 4.07 | -0.61 | 0.539 | 0.788 | n.s. |
| 2a - 2d | -8.00 | 4.07 | -1.96 | 0.049 | 0.224 | n.s. |
| 2b - 2c | -3.83 | 4.08 | -0.94 | 0.347 | 0.722 | n.s. |
| 2b - 2d | -9.33 | 4.08 | -2.29 | 0.022 | 0.125 | n.s. |
| 2c - 2d | -5.50 | 4.07 | -1.35 | 0.177 | 0.541 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.97, *p* = 0.127, η²_G = 0.057
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.28 | 23 | = 0.779 | 0.09 [-0.36, 0.48] | negligible | n.s. |
| 2a vs 2c | -0.55 | 23 | = 0.707 | -0.16 [-0.54, 0.31] | negligible | n.s. |
| 2a vs 2d | -2.10 | 23 | = 0.140 | -0.62 [-0.87, 0.01] | medium | n.s. |
| 2b vs 2c | -0.80 | 23 | = 0.652 | -0.23 [-0.59, 0.26] | small | n.s. |
| 2b vs 2d | -2.57 | 23 | = 0.103 | -0.66 [-0.97, -0.07] | medium | n.s. |
| 2c vs 2d | -1.73 | 23 | = 0.193 | -0.36 [-0.79, 0.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 527.64, BIC = 545.59
- **2b vs 2a**: *β* = 2.21, *SE* = 1.016, *z* = 2.175, *p* = 0.030
- **2c vs 2a**: *β* = 1.62, *SE* = 1.014, *z* = 1.599, *p* = 0.110
- **2d vs 2a**: *β* = 1.84, *SE* = 1.014, *z* = 1.812, *p* = 0.070
- **SNR**: *β* = -1.09, *SE* = 0.293, *z* = -3.703, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -2.21 | 1.02 | -2.17 | 0.030 | 0.165 | n.s. |
| 2a - 2c | -1.62 | 1.01 | -1.60 | 0.110 | 0.372 | n.s. |
| 2a - 2d | -1.84 | 1.01 | -1.81 | 0.070 | 0.304 | n.s. |
| 2b - 2c | 0.59 | 1.02 | 0.58 | 0.561 | 0.916 | n.s. |
| 2b - 2d | 0.37 | 1.02 | 0.37 | 0.713 | 0.918 | n.s. |
| 2c - 2d | -0.22 | 1.01 | -0.21 | 0.831 | 0.918 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.288, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | -1.53 | 23 | = 0.316 | -0.47 [-0.74, 0.12] | small | n.s. |
| 2a vs 2c | -1.52 | 23 | = 0.316 | -0.37 [-0.74, 0.12] | small | n.s. |
| 2a vs 2d | -1.46 | 23 | = 0.316 | -0.43 [-0.73, 0.13] | small | n.s. |
| 2b vs 2c | 0.34 | 23 | = 0.849 | 0.11 [-0.35, 0.49] | negligible | n.s. |
| 2b vs 2d | 0.24 | 23 | = 0.849 | 0.06 [-0.37, 0.47] | negligible | n.s. |
| 2c vs 2d | -0.19 | 23 | = 0.849 | -0.06 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 859.85, BIC = 877.80
- **2b vs 2a**: *β* = -7.86, *SE* = 5.074, *z* = -1.550, *p* = 0.121
- **2c vs 2a**: *β* = 5.37, *SE* = 5.037, *z* = 1.066, *p* = 0.286
- **2d vs 2a**: *β* = -6.15, *SE* = 5.083, *z* = -1.209, *p* = 0.227
- **SNR**: *β* = -0.77, *SE* = 0.999, *z* = -0.765, *p* = 0.444

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 7.86 | 5.07 | 1.55 | 0.121 | 0.404 | n.s. |
| 2a - 2c | -5.37 | 5.04 | -1.07 | 0.286 | 0.537 | n.s. |
| 2a - 2d | 6.15 | 5.08 | 1.21 | 0.227 | 0.537 | n.s. |
| 2b - 2c | -13.23 | 5.07 | -2.61 | 0.009 | 0.053 | n.s. |
| 2b - 2d | -1.72 | 5.04 | -0.34 | 0.733 | 0.733 | n.s. |
| 2c - 2d | 11.52 | 5.08 | 2.27 | 0.023 | 0.111 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.98, *p* = 0.037, η²_G = 0.063
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 1.53 | 23 | = 0.278 | 0.37 [-0.12, 0.75] | small | n.s. |
| 2a vs 2c | -0.83 | 23 | = 0.497 | -0.23 [-0.60, 0.26] | small | n.s. |
| 2a vs 2d | 1.36 | 23 | = 0.281 | 0.31 [-0.15, 0.71] | small | n.s. |
| 2b vs 2c | -3.25 | 23 | = 0.021 | -0.64 [-1.13, -0.20] | medium | * |
| 2b vs 2d | -0.36 | 23 | = 0.722 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 2c vs 2d | 2.37 | 23 | = 0.080 | 0.59 [0.04, 0.93] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 486.94, BIC = 504.89
- **2b vs 2a**: *β* = 1.42, *SE* = 0.708, *z* = 2.003, *p* = 0.045
- **2c vs 2a**: *β* = 1.98, *SE* = 0.703, *z* = 2.817, *p* = 0.005
- **2d vs 2a**: *β* = 2.19, *SE* = 0.710, *z* = 3.080, *p* = 0.002
- **SNR**: *β* = -0.90, *SE* = 0.142, *z* = -6.342, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -1.42 | 0.71 | -2.00 | 0.045 | 0.169 | n.s. |
| 2a - 2c | -1.98 | 0.70 | -2.82 | 0.005 | 0.024 | * |
| 2a - 2d | -2.19 | 0.71 | -3.08 | 0.002 | 0.012 | * |
| 2b - 2c | -0.56 | 0.71 | -0.79 | 0.428 | 0.672 | n.s. |
| 2b - 2d | -0.77 | 0.70 | -1.09 | 0.276 | 0.620 | n.s. |
| 2c - 2d | -0.20 | 0.71 | -0.29 | 0.772 | 0.772 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.91, *p* = 0.137, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | -0.80 | 23 | = 0.518 | -0.20 [-0.59, 0.26] | small | n.s. |
| 2a vs 2c | -2.16 | 23 | = 0.241 | -0.52 [-0.88, 0.00] | medium | n.s. |
| 2a vs 2d | -1.83 | 23 | = 0.241 | -0.40 [-0.81, 0.06] | small | n.s. |
| 2b vs 2c | -1.41 | 23 | = 0.343 | -0.32 [-0.72, 0.14] | small | n.s. |
| 2b vs 2d | -0.80 | 23 | = 0.518 | -0.20 [-0.59, 0.26] | negligible | n.s. |
| 2c vs 2d | 0.50 | 23 | = 0.620 | 0.12 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 849.51, BIC = 867.46
- **2b vs 2a**: *β* = -13.08, *SE* = 4.885, *z* = -2.677, *p* = 0.007
- **2c vs 2a**: *β* = 2.79, *SE* = 4.891, *z* = 0.572, *p* = 0.568
- **2d vs 2a**: *β* = 0.05, *SE* = 4.882, *z* = 0.011, *p* = 0.991
- **SNR**: *β* = -0.81, *SE* = 2.025, *z* = -0.397, *p* = 0.691

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 13.08 | 4.89 | 2.68 | 0.007 | 0.035 | * |
| 2a - 2c | -2.80 | 4.89 | -0.57 | 0.568 | 0.919 | n.s. |
| 2a - 2d | -0.05 | 4.88 | -0.01 | 0.991 | 0.991 | n.s. |
| 2b - 2c | -15.87 | 4.88 | -3.25 | 0.001 | 0.007 | ** |
| 2b - 2d | -13.13 | 4.88 | -2.69 | 0.007 | 0.035 | * |
| 2c - 2d | 2.74 | 4.88 | 0.56 | 0.575 | 0.919 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.09, *p* = 0.010, η²_G = 0.091
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 2.46 | 23 | = 0.044 | 0.67 [0.05, 0.95] | medium | * |
| 2a vs 2c | -0.66 | 23 | = 0.748 | -0.14 [-0.56, 0.29] | negligible | n.s. |
| 2a vs 2d | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 2b vs 2c | -3.00 | 23 | = 0.019 | -0.77 [-1.07, -0.15] | medium | * |
| 2b vs 2d | -3.53 | 23 | = 0.011 | -0.65 [-1.19, -0.25] | medium | * |
| 2c vs 2d | 0.50 | 23 | = 0.748 | 0.13 [-0.32, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 484.11, BIC = 502.06
- **2b vs 2a**: *β* = -1.98, *SE* = 0.767, *z* = -2.578, *p* = 0.010
- **2c vs 2a**: *β* = -1.67, *SE* = 0.768, *z* = -2.168, *p* = 0.030
- **2d vs 2a**: *β* = -1.95, *SE* = 0.767, *z* = -2.537, *p* = 0.011
- **SNR**: *β* = 0.59, *SE* = 0.309, *z* = 1.912, *p* = 0.056

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 1.98 | 0.77 | 2.58 | 0.010 | 0.058 | n.s. |
| 2a - 2c | 1.66 | 0.77 | 2.17 | 0.030 | 0.115 | n.s. |
| 2a - 2d | 1.94 | 0.77 | 2.54 | 0.011 | 0.058 | n.s. |
| 2b - 2c | -0.31 | 0.77 | -0.41 | 0.683 | 0.968 | n.s. |
| 2b - 2d | -0.03 | 0.77 | -0.04 | 0.966 | 0.968 | n.s. |
| 2c - 2d | 0.28 | 0.77 | 0.37 | 0.715 | 0.968 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.65, *p* = 0.056, η²_G = 0.070
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 2.24 | 23 | = 0.105 | 0.62 [0.01, 0.90] | medium | n.s. |
| 2a vs 2c | 1.84 | 23 | = 0.158 | 0.45 [-0.06, 0.81] | small | n.s. |
| 2a vs 2d | 2.61 | 23 | = 0.093 | 0.62 [0.08, 0.98] | medium | n.s. |
| 2b vs 2c | -0.38 | 23 | = 0.846 | -0.12 [-0.50, 0.34] | negligible | n.s. |
| 2b vs 2d | -0.01 | 23 | = 0.989 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| 2c vs 2d | 0.41 | 23 | = 0.846 | 0.12 [-0.34, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 798.73, BIC = 816.68
- **2b vs 2a**: *β* = -3.91, *SE* = 4.186, *z* = -0.934, *p* = 0.350
- **2c vs 2a**: *β* = 3.18, *SE* = 4.176, *z* = 0.762, *p* = 0.446
- **2d vs 2a**: *β* = -2.20, *SE* = 4.167, *z* = -0.527, *p* = 0.598
- **SNR**: *β* = 0.70, *SE* = 0.775, *z* = 0.900, *p* = 0.368

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 3.91 | 4.19 | 0.93 | 0.350 | 0.822 | n.s. |
| 2a - 2c | -3.18 | 4.18 | -0.76 | 0.446 | 0.830 | n.s. |
| 2a - 2d | 2.20 | 4.17 | 0.53 | 0.598 | 0.838 | n.s. |
| 2b - 2c | -7.09 | 4.16 | -1.70 | 0.088 | 0.426 | n.s. |
| 2b - 2d | -1.71 | 4.17 | -0.41 | 0.681 | 0.838 | n.s. |
| 2c - 2d | 5.38 | 4.16 | 1.29 | 0.196 | 0.664 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.456, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.80 | 23 | = 0.744 | 0.22 [-0.26, 0.59] | small | n.s. |
| 2a vs 2c | -0.69 | 23 | = 0.744 | -0.24 [-0.57, 0.28] | small | n.s. |
| 2a vs 2d | 0.50 | 23 | = 0.750 | 0.14 [-0.32, 0.52] | negligible | n.s. |
| 2b vs 2c | -1.55 | 23 | = 0.567 | -0.46 [-0.75, 0.12] | small | n.s. |
| 2b vs 2d | -0.29 | 23 | = 0.776 | -0.10 [-0.48, 0.36] | negligible | n.s. |
| 2c vs 2d | 1.35 | 23 | = 0.567 | 0.39 [-0.15, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 536.07, BIC = 554.02
- **2b vs 2a**: *β* = -3.84, *SE* = 0.921, *z* = -4.174, *p* < .001
- **2c vs 2a**: *β* = -4.47, *SE* = 0.919, *z* = -4.863, *p* < .001
- **2d vs 2a**: *β* = -4.74, *SE* = 0.917, *z* = -5.173, *p* < .001
- **SNR**: *β* = -0.14, *SE* = 0.155, *z* = -0.900, *p* = 0.368

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 3.84 | 0.92 | 4.17 | < .001 | < .001 | *** |
| 2a - 2c | 4.47 | 0.92 | 4.86 | < .001 | < .001 | *** |
| 2a - 2d | 4.74 | 0.92 | 5.17 | < .001 | < .001 | *** |
| 2b - 2c | 0.62 | 0.92 | 0.68 | 0.495 | 0.745 | n.s. |
| 2b - 2d | 0.90 | 0.92 | 0.98 | 0.326 | 0.694 | n.s. |
| 2c - 2d | 0.28 | 0.92 | 0.30 | 0.763 | 0.763 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 11.36, *p* < .001, η²_G = 0.192
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 4.34 | 23 | < .001 | 0.89 [0.39, 1.38] | large | *** |
| 2a vs 2c | 4.41 | 23 | < .001 | 1.10 [0.40, 1.40] | large | *** |
| 2a vs 2d | 4.35 | 23 | < .001 | 1.12 [0.39, 1.39] | large | *** |
| 2b vs 2c | 0.71 | 23 | = 0.584 | 0.16 [-0.28, 0.57] | negligible | n.s. |
| 2b vs 2d | 1.02 | 23 | = 0.480 | 0.22 [-0.22, 0.63] | small | n.s. |
| 2c vs 2d | 0.29 | 23 | = 0.774 | 0.07 [-0.36, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.037). Post-hoc tests revealed:
  - 2b showed smaller latency than 2c (*d* = -0.64)
**P1 latency:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - 2a showed greater latency than 2b (*d* = 0.67)
  - 2b showed smaller latency than 2c (*d* = -0.77)
  - 2b showed smaller latency than 2d (*d* = -0.65)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.056)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2a showed greater amplitude than 2b (*d* = 0.89)
  - 2a showed greater amplitude than 2c (*d* = 1.10)
  - 2a showed greater amplitude than 2d (*d* = 1.12)

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

#### Amplitude

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
