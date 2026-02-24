# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:11:22

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
| Decreasing 2 to 1 | 24 | 108.00 ms | 12.14 | 2.48 | [88.00, 120.00] |
| Decreasing 3 to 1 | 24 | 108.50 ms | 11.46 | 2.34 | [88.00, 120.00] |
| Increasing 1 to 2 | 24 | 101.17 ms | 13.83 | 2.82 | [88.00, 120.00] |
| Increasing 1 to 3 | 24 | 101.17 ms | 12.45 | 2.54 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | -2.17 µV | 1.86 | 0.38 | [-6.41, 2.51] |
| Decreasing 3 to 1 | 24 | -1.88 µV | 2.02 | 0.41 | [-6.18, 1.52] |
| Increasing 1 to 2 | 24 | -0.52 µV | 2.34 | 0.48 | [-6.41, 5.05] |
| Increasing 1 to 3 | 24 | -0.16 µV | 2.41 | 0.49 | [-5.86, 3.53] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 182.50 ms | 14.05 | 2.87 | [160.00, 212.00] |
| Decreasing 3 to 1 | 24 | 183.00 ms | 16.27 | 3.32 | [156.00, 212.00] |
| Increasing 1 to 2 | 24 | 170.83 ms | 17.71 | 3.62 | [148.00, 208.00] |
| Increasing 1 to 3 | 24 | 170.83 ms | 19.93 | 4.07 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | -3.43 µV | 3.22 | 0.66 | [-10.79, 2.16] |
| Decreasing 3 to 1 | 24 | -3.96 µV | 2.53 | 0.52 | [-10.41, -0.72] |
| Increasing 1 to 2 | 24 | -5.31 µV | 2.41 | 0.49 | [-9.95, -0.26] |
| Increasing 1 to 3 | 24 | -6.52 µV | 2.47 | 0.50 | [-12.65, -2.57] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 118.00 ms | 10.75 | 2.19 | [96.00, 128.00] |
| Decreasing 3 to 1 | 24 | 116.17 ms | 11.22 | 2.29 | [96.00, 128.00] |
| Increasing 1 to 2 | 24 | 110.00 ms | 13.34 | 2.72 | [96.00, 128.00] |
| Increasing 1 to 3 | 24 | 108.17 ms | 10.97 | 2.24 | [96.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 3.80 µV | 2.58 | 0.53 | [-0.45, 9.13] |
| Decreasing 3 to 1 | 24 | 3.43 µV | 2.15 | 0.44 | [-2.06, 9.14] |
| Increasing 1 to 2 | 24 | 0.83 µV | 2.22 | 0.45 | [-3.63, 5.29] |
| Increasing 1 to 3 | 24 | 0.83 µV | 2.75 | 0.56 | [-5.83, 7.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 493.17 ms | 35.08 | 7.16 | [420.00, 536.00] |
| Decreasing 3 to 1 | 24 | 473.83 ms | 30.69 | 6.26 | [420.00, 536.00] |
| Increasing 1 to 2 | 24 | 479.00 ms | 42.01 | 8.57 | [420.00, 536.00] |
| Increasing 1 to 3 | 24 | 476.00 ms | 34.35 | 7.01 | [420.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 24 | 4.89 µV | 3.19 | 0.65 | [-1.47, 11.08] |
| Decreasing 3 to 1 | 24 | 4.89 µV | 3.42 | 0.70 | [-0.59, 14.34] |
| Increasing 1 to 2 | 24 | 3.95 µV | 3.77 | 0.77 | [-3.51, 11.52] |
| Increasing 1 to 3 | 24 | 4.93 µV | 4.07 | 0.83 | [-2.06, 15.57] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 763.49, BIC = 781.44
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 0.13, *SE* = 3.261, *z* = 0.039, *p* = 0.969
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -6.92, *SE* = 3.252, *z* = -2.128, *p* = 0.033
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -6.06, *SE* = 3.292, *z* = -1.839, *p* = 0.066
- **SNR**: *β* = -1.20, *SE* = 0.797, *z* = -1.499, *p* = 0.134

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -0.13 | 3.26 | -0.04 | 0.969 | 0.969 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 6.92 | 3.25 | 2.13 | 0.033 | 0.169 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 6.06 | 3.29 | 1.84 | 0.066 | 0.233 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 7.05 | 3.26 | 2.16 | 0.030 | 0.169 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 6.18 | 3.34 | 1.85 | 0.064 | 0.233 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.86 | 3.30 | -0.26 | 0.794 | 0.957 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.90, *p* = 0.041, η²_G = 0.077
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.15 | 23 | = 1.000 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.99 | 23 | = 0.096 | 0.53 [-0.03, 0.85] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 1.95 | 23 | = 0.096 | 0.56 [-0.04, 0.84] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.19 | 23 | = 0.096 | 0.58 [0.00, 0.89] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.76 | 23 | = 0.067 | 0.61 [0.11, 1.02] | medium | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 425.14, BIC = 443.09
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 0.33, *SE* = 0.543, *z* = 0.611, *p* = 0.541
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = 1.66, *SE* = 0.541, *z* = 3.063, *p* = 0.002
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = 1.93, *SE* = 0.548, *z* = 3.520, *p* < .001
- **SNR**: *β* = 0.12, *SE* = 0.134, *z* = 0.889, *p* = 0.374

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -0.33 | 0.54 | -0.61 | 0.541 | 0.789 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | -1.66 | 0.54 | -3.06 | 0.002 | 0.011 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | -1.93 | 0.55 | -3.52 | < .001 | 0.003 | ** |
| Decreasing 3 to 1 - Increasing 1 to 2 | -1.33 | 0.54 | -2.45 | 0.014 | 0.043 | * |
| Decreasing 3 to 1 - Increasing 1 to 3 | -1.60 | 0.56 | -2.87 | 0.004 | 0.016 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.27 | 0.55 | -0.49 | 0.621 | 0.789 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.31, *p* < .001, η²_G = 0.139
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.53 | 23 | = 0.601 | -0.15 [-0.53, 0.32] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | -2.66 | 23 | = 0.027 | -0.78 [-1.00, -0.09] | medium | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | -3.80 | 23 | = 0.006 | -0.93 [-1.26, -0.29] | large | ** |
| Decreasing 3 to 1 vs Increasing 1 to 2 | -2.54 | 23 | = 0.027 | -0.62 [-0.97, -0.07] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -3.37 | 23 | = 0.008 | -0.77 [-1.16, -0.22] | medium | ** |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.61 | 23 | = 0.601 | -0.15 [-0.55, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 809.85, BIC = 827.80
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 0.49, *SE* = 3.749, *z* = 0.132, *p* = 0.895
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -11.51, *SE* = 3.835, *z* = -3.002, *p* = 0.003
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -11.32, *SE* = 4.164, *z* = -2.718, *p* = 0.007
- **SNR**: *β* = -0.11, *SE* = 0.587, *z* = -0.192, *p* = 0.848

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -0.49 | 3.75 | -0.13 | 0.895 | 0.989 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 11.51 | 3.83 | 3.00 | 0.003 | 0.013 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 11.32 | 4.16 | 2.72 | 0.007 | 0.020 | * |
| Decreasing 3 to 1 - Increasing 1 to 2 | 12.01 | 3.84 | 3.12 | 0.002 | 0.011 | * |
| Decreasing 3 to 1 - Increasing 1 to 3 | 11.81 | 4.18 | 2.83 | 0.005 | 0.019 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.19 | 3.88 | -0.05 | 0.960 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.46, *p* < .001, η²_G = 0.112
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.23 | 23 | = 0.980 | -0.03 [-0.47, 0.37] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.97 | 23 | = 0.010 | 0.73 [0.15, 1.07] | medium | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 3.19 | 23 | = 0.010 | 0.68 [0.19, 1.12] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 3.02 | 23 | = 0.010 | 0.72 [0.16, 1.08] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 3.01 | 23 | = 0.010 | 0.67 [0.15, 1.08] | medium | * |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 408.92, BIC = 426.87
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.55, *SE* = 0.450, *z* = -1.217, *p* = 0.224
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -1.31, *SE* = 0.461, *z* = -2.842, *p* = 0.004
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -1.82, *SE* = 0.506, *z* = -3.596, *p* < .001
- **SNR**: *β* = -0.41, *SE* = 0.075, *z* = -5.490, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.55 | 0.45 | 1.22 | 0.224 | 0.397 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 1.31 | 0.46 | 2.84 | 0.004 | 0.022 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 1.82 | 0.51 | 3.60 | < .001 | 0.002 | ** |
| Decreasing 3 to 1 - Increasing 1 to 2 | 0.76 | 0.46 | 1.65 | 0.099 | 0.268 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 1.27 | 0.51 | 2.50 | 0.012 | 0.048 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.51 | 0.47 | 1.08 | 0.278 | 0.397 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 14.61, *p* < .001, η²_G = 0.174
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.95 | 23 | = 0.352 | 0.18 [-0.23, 0.62] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 3.52 | 23 | = 0.004 | 0.66 [0.24, 1.19] | medium | ** |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 5.44 | 23 | < .001 | 1.07 [0.57, 1.65] | large | *** |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.80 | 23 | = 0.012 | 0.55 [0.12, 1.03] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 4.91 | 23 | < .001 | 1.02 [0.49, 1.52] | large | *** |
| Increasing 1 to 2 vs Increasing 1 to 3 | 2.93 | 23 | = 0.011 | 0.50 [0.14, 1.06] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 750.31, BIC = 768.27
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -2.15, *SE* = 3.101, *z* = -0.695, *p* = 0.487
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -8.74, *SE* = 3.148, *z* = -2.775, *p* = 0.006
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -10.05, *SE* = 3.095, *z* = -3.246, *p* = 0.001
- **SNR**: *β* = -0.62, *SE* = 0.502, *z* = -1.225, *p* = 0.220

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 2.15 | 3.10 | 0.69 | 0.487 | 0.737 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 8.74 | 3.15 | 2.78 | 0.006 | 0.027 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 10.05 | 3.09 | 3.25 | 0.001 | 0.007 | ** |
| Decreasing 3 to 1 - Increasing 1 to 2 | 6.58 | 3.11 | 2.12 | 0.034 | 0.099 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 7.89 | 3.09 | 2.55 | 0.011 | 0.042 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | 1.31 | 3.12 | 0.42 | 0.674 | 0.737 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.46, *p* = 0.006, η²_G = 0.115
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.67 | 23 | = 0.528 | 0.17 [-0.29, 0.56] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.17 | 23 | = 0.075 | 0.66 [-0.00, 0.88] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 3.01 | 23 | = 0.037 | 0.91 [0.15, 1.08] | large | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.07 | 23 | = 0.075 | 0.50 [-0.02, 0.86] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.36 | 23 | = 0.075 | 0.72 [0.03, 0.93] | medium | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.64 | 23 | = 0.528 | 0.15 [-0.29, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 429.42, BIC = 447.37
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.32, *SE* = 0.514, *z* = -0.618, *p* = 0.537
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -2.85, *SE* = 0.523, *z* = -5.450, *p* < .001
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -2.94, *SE* = 0.512, *z* = -5.726, *p* < .001
- **SNR**: *β* = 0.10, *SE* = 0.092, *z* = 1.093, *p* = 0.274

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.32 | 0.51 | 0.62 | 0.537 | 0.786 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 2.85 | 0.52 | 5.45 | < .001 | < .001 | *** |
| Decreasing 2 to 1 - Increasing 1 to 3 | 2.93 | 0.51 | 5.73 | < .001 | < .001 | *** |
| Decreasing 3 to 1 - Increasing 1 to 2 | 2.53 | 0.52 | 4.92 | < .001 | < .001 | *** |
| Decreasing 3 to 1 - Increasing 1 to 3 | 2.62 | 0.51 | 5.11 | < .001 | < .001 | *** |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.08 | 0.52 | 0.16 | 0.872 | 0.872 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 19.24, *p* < .001, η²_G = 0.256
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.76 | 23 | = 0.547 | 0.16 [-0.27, 0.58] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 5.85 | 23 | < .001 | 1.23 [0.64, 1.75] | large | *** |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 5.08 | 23 | < .001 | 1.12 [0.51, 1.56] | large | *** |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 5.32 | 23 | < .001 | 1.19 [0.55, 1.62] | large | *** |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 5.39 | 23 | < .001 | 1.05 [0.56, 1.63] | large | *** |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.00 | 23 | = 0.997 | -0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 964.80, BIC = 982.75
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -19.43, *SE* = 9.259, *z* = -2.098, *p* = 0.036
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -14.16, *SE* = 9.099, *z* = -1.557, *p* = 0.120
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -17.20, *SE* = 9.118, *z* = -1.886, *p* = 0.059
- **SNR**: *β* = 0.04, *SE* = 0.772, *z* = 0.054, *p* = 0.957

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 19.43 | 9.26 | 2.10 | 0.036 | 0.197 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 14.16 | 9.10 | 1.56 | 0.120 | 0.399 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 17.20 | 9.12 | 1.89 | 0.059 | 0.263 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -5.26 | 9.27 | -0.57 | 0.570 | 0.921 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -2.23 | 9.17 | -0.24 | 0.808 | 0.932 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 3.04 | 9.12 | 0.33 | 0.739 | 0.932 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.75, *p* = 0.164, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 2.72 | 23 | = 0.074 | 0.59 [0.10, 1.01] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.28 | 23 | = 0.424 | 0.37 [-0.17, 0.69] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.25 | 23 | = 0.104 | 0.49 [0.01, 0.90] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | -0.50 | 23 | = 0.801 | -0.14 [-0.53, 0.32] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.25 | 23 | = 0.801 | -0.07 [-0.47, 0.37] | negligible | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.29 | 23 | = 0.801 | 0.08 [-0.36, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 476.50, BIC = 494.45
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.44, *SE* = 0.626, *z* = -0.709, *p* = 0.478
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.92, *SE* = 0.613, *z* = -1.499, *p* = 0.134
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.12, *SE* = 0.614, *z* = -0.191, *p* = 0.848
- **SNR**: *β* = 0.20, *SE* = 0.057, *z* = 3.572, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.44 | 0.63 | 0.71 | 0.478 | 0.908 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.92 | 0.61 | 1.50 | 0.134 | 0.578 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.12 | 0.61 | 0.19 | 0.848 | 0.908 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 0.47 | 0.63 | 0.76 | 0.449 | 0.908 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.33 | 0.62 | -0.53 | 0.597 | 0.908 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.80 | 0.61 | -1.30 | 0.192 | 0.657 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.380, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.01 | 23 | = 0.989 | -0.00 [-0.43, 0.42] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.49 | 23 | = 0.390 | 0.27 [-0.13, 0.74] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | -0.06 | 23 | = 0.989 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.33 | 23 | = 0.390 | 0.26 [-0.16, 0.70] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.04 | 23 | = 0.989 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.65 | 23 | = 0.390 | -0.25 [-0.77, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.041) (no significant pairwise comparisons)
**Fz amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed smaller amplitude than Increasing 1 to 2 (*d* = -0.78)
  - Decreasing 2 to 1 showed smaller amplitude than Increasing 1 to 3 (*d* = -0.93)
  - Decreasing 3 to 1 showed smaller amplitude than Increasing 1 to 2 (*d* = -0.62)
  - Decreasing 3 to 1 showed smaller amplitude than Increasing 1 to 3 (*d* = -0.77)
**N1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.73)
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.68)
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.72)
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.67)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 0.66)
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 1.07)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 0.55)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 1.02)
  - Increasing 1 to 2 showed greater amplitude than Increasing 1 to 3 (*d* = 0.50)
**P1 latency:** Significant main effect of condition (*p* = 0.006). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.91)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 1.23)
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 1.12)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 1.19)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 1.05)

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
