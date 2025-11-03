# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:51:59

---

## 1. Analysis Overview

**Total Measurements:** 336
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
| 5a | 8 | 106.50 ms | 9.30 | 3.29 | [92.00, 116.00] |
| 5b | 12 | 108.33 ms | 7.90 | 2.28 | [92.00, 116.00] |
| 5c | 16 | 102.25 ms | 8.64 | 2.16 | [92.00, 116.00] |
| 5d | 14 | 102.86 ms | 8.80 | 2.35 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 8 | -5.42 µV | 3.54 | 1.25 | [-12.87, -1.40] |
| 5b | 12 | -4.92 µV | 3.68 | 1.06 | [-14.38, -1.06] |
| 5c | 16 | -4.96 µV | 2.94 | 0.73 | [-11.51, -1.59] |
| 5d | 14 | -5.41 µV | 3.38 | 0.90 | [-16.02, -1.79] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 11 | 172.36 ms | 14.36 | 4.33 | [152.00, 200.00] |
| 5b | 20 | 170.20 ms | 19.57 | 4.38 | [140.00, 196.00] |
| 5c | 19 | 167.79 ms | 16.89 | 3.87 | [140.00, 200.00] |
| 5d | 22 | 174.55 ms | 17.26 | 3.68 | [140.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 11 | -10.14 µV | 4.50 | 1.36 | [-21.47, -5.27] |
| 5b | 20 | -6.87 µV | 2.89 | 0.65 | [-13.58, -2.20] |
| 5c | 19 | -8.68 µV | 3.83 | 0.88 | [-17.27, -4.00] |
| 5d | 22 | -7.53 µV | 2.86 | 0.61 | [-13.12, -1.35] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 8 | 95.50 ms | 10.78 | 3.81 | [84.00, 108.00] |
| 5b | 13 | 97.23 ms | 10.38 | 2.88 | [84.00, 108.00] |
| 5c | 12 | 95.67 ms | 9.72 | 2.81 | [84.00, 108.00] |
| 5d | 13 | 100.00 ms | 7.48 | 2.08 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 8 | 3.08 µV | 1.65 | 0.58 | [1.44, 6.35] |
| 5b | 13 | 5.86 µV | 3.63 | 1.01 | [1.42, 13.70] |
| 5c | 12 | 5.68 µV | 3.69 | 1.06 | [2.27, 15.51] |
| 5d | 13 | 4.39 µV | 2.73 | 0.76 | [1.16, 8.81] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 5 | 348.80 ms | 11.80 | 5.28 | [332.00, 360.00] |
| 5b | 12 | 356.00 ms | 15.72 | 4.54 | [332.00, 372.00] |
| 5c | 13 | 352.62 ms | 10.56 | 2.93 | [332.00, 372.00] |
| 5d | 14 | 351.71 ms | 16.19 | 4.33 | [332.00, 372.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 5 | 7.57 µV | 6.79 | 3.04 | [3.44, 19.50] |
| 5b | 12 | 4.07 µV | 1.38 | 0.40 | [1.96, 6.51] |
| 5c | 13 | 4.66 µV | 2.90 | 0.80 | [1.56, 11.31] |
| 5d | 14 | 4.38 µV | 2.19 | 0.58 | [2.11, 9.51] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 365.81, BIC = 379.19
- **5b vs 5a**: *β* = 1.75, *SE* = 3.494, *z* = 0.500, *p* = 0.617
- **5c vs 5a**: *β* = -5.11, *SE* = 3.405, *z* = -1.501, *p* = 0.133
- **5d vs 5a**: *β* = -4.68, *SE* = 3.487, *z* = -1.343, *p* = 0.179
- **SNR**: *β* = -0.09, *SE* = 0.720, *z* = -0.124, *p* = 0.902

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -1.75 | 3.49 | -0.50 | 0.617 | 0.854 | n.s. |
| 5a - 5c | 5.11 | 3.40 | 1.50 | 0.133 | 0.436 | n.s. |
| 5a - 5d | 4.68 | 3.49 | 1.34 | 0.179 | 0.447 | n.s. |
| 5b - 5c | 6.86 | 3.08 | 2.23 | 0.026 | 0.146 | n.s. |
| 5b - 5d | 6.43 | 3.12 | 2.06 | 0.039 | 0.181 | n.s. |
| 5c - 5d | -0.43 | 2.77 | -0.15 | 0.878 | 0.878 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 226.08, BIC = 239.47
- **5b vs 5a**: *β* = 0.61, *SE* = 0.948, *z* = 0.641, *p* = 0.521
- **5c vs 5a**: *β* = 0.42, *SE* = 0.879, *z* = 0.480, *p* = 0.631
- **5d vs 5a**: *β* = 0.38, *SE* = 0.932, *z* = 0.407, *p* = 0.684
- **SNR**: *β* = -1.26, *SE* = 0.145, *z* = -8.654, *p* < .001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -0.61 | 0.95 | -0.64 | 0.521 | 0.988 | n.s. |
| 5a - 5c | -0.42 | 0.88 | -0.48 | 0.631 | 0.993 | n.s. |
| 5a - 5d | -0.38 | 0.93 | -0.41 | 0.684 | 0.993 | n.s. |
| 5b - 5c | 0.19 | 0.78 | 0.24 | 0.811 | 0.993 | n.s. |
| 5b - 5d | 0.23 | 0.79 | 0.29 | 0.773 | 0.993 | n.s. |
| 5c - 5d | 0.04 | 0.75 | 0.06 | 0.955 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 624.06, BIC = 639.99
- **5b vs 5a**: *β* = 0.63, *SE* = 6.059, *z* = 0.104, *p* = 0.918
- **5c vs 5a**: *β* = -2.41, *SE* = 6.014, *z* = -0.400, *p* = 0.689
- **5d vs 5a**: *β* = 5.17, *SE* = 6.012, *z* = 0.860, *p* = 0.390
- **SNR**: *β* = 1.08, *SE* = 1.109, *z* = 0.974, *p* = 0.330

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -0.63 | 6.06 | -0.10 | 0.918 | 0.918 | n.s. |
| 5a - 5c | 2.41 | 6.01 | 0.40 | 0.689 | 0.903 | n.s. |
| 5a - 5d | -5.17 | 6.01 | -0.86 | 0.390 | 0.873 | n.s. |
| 5b - 5c | 3.03 | 4.96 | 0.61 | 0.541 | 0.903 | n.s. |
| 5b - 5d | -4.54 | 4.75 | -0.96 | 0.339 | 0.873 | n.s. |
| 5c - 5d | -7.57 | 4.85 | -1.56 | 0.118 | 0.531 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.652, η²_G = 0.068
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | -1.06 | 6 | = 0.886 | -0.60 [-1.28, 0.34] | medium | n.s. |
| 5a vs 5c | -0.33 | 6 | = 0.907 | -0.19 [-0.79, 0.65] | negligible | n.s. |
| 5a vs 5d | -0.95 | 6 | = 0.886 | -0.58 [-0.89, 0.65] | medium | n.s. |
| 5b vs 5c | 0.77 | 6 | = 0.886 | 0.41 [-0.33, 0.71] | small | n.s. |
| 5b vs 5d | 0.10 | 6 | = 0.926 | 0.03 [-0.72, 0.29] | negligible | n.s. |
| 5c vs 5d | -0.57 | 6 | = 0.886 | -0.38 [-1.05, 0.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 370.80, BIC = 386.74
- **5b vs 5a**: *β* = 3.26, *SE* = 0.981, *z* = 3.323, *p* = 0.001
- **5c vs 5a**: *β* = 1.15, *SE* = 0.988, *z* = 1.163, *p* = 0.245
- **5d vs 5a**: *β* = 2.30, *SE* = 0.969, *z* = 2.371, *p* = 0.018
- **SNR**: *β* = -0.63, *SE* = 0.174, *z* = -3.642, *p* < .001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -3.26 | 0.98 | -3.32 | < .001 | 0.005 | ** |
| 5a - 5c | -1.15 | 0.99 | -1.16 | 0.245 | 0.390 | n.s. |
| 5a - 5d | -2.30 | 0.97 | -2.37 | 0.018 | 0.069 | n.s. |
| 5b - 5c | 2.11 | 0.81 | 2.60 | 0.009 | 0.046 | * |
| 5b - 5d | 0.96 | 0.78 | 1.23 | 0.219 | 0.390 | n.s. |
| 5c - 5d | -1.15 | 0.80 | -1.44 | 0.150 | 0.385 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.72, *p* = 0.075, η²_G = 0.156
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | -2.26 | 6 | = 0.243 | -0.72 [-1.87, -0.02] | medium | n.s. |
| 5a vs 5c | -1.15 | 6 | = 0.353 | -0.34 [-1.12, 0.36] | small | n.s. |
| 5a vs 5d | -2.09 | 6 | = 0.243 | -1.13 [-1.64, 0.11] | large | n.s. |
| 5b vs 5c | 1.18 | 6 | = 0.353 | 0.31 [0.11, 1.25] | small | n.s. |
| 5b vs 5d | -0.89 | 6 | = 0.405 | -0.51 [-0.35, 0.65] | medium | n.s. |
| 5c vs 5d | -1.37 | 6 | = 0.353 | -0.68 [-0.63, 0.40] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 341.08, BIC = 353.88
- **5b vs 5a**: *β* = -0.89, *SE* = 3.457, *z* = -0.256, *p* = 0.798
- **5c vs 5a**: *β* = -3.83, *SE* = 3.837, *z* = -0.998, *p* = 0.318
- **5d vs 5a**: *β* = 1.46, *SE* = 3.470, *z* = 0.419, *p* = 0.675
- **SNR**: *β* = 0.89, *SE* = 0.779, *z* = 1.137, *p* = 0.256

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 0.89 | 3.46 | 0.26 | 0.798 | 0.894 | n.s. |
| 5a - 5c | 3.83 | 3.84 | 1.00 | 0.318 | 0.853 | n.s. |
| 5a - 5d | -1.46 | 3.47 | -0.42 | 0.675 | 0.894 | n.s. |
| 5b - 5c | 2.95 | 3.03 | 0.97 | 0.330 | 0.853 | n.s. |
| 5b - 5d | -2.34 | 2.91 | -0.81 | 0.420 | 0.853 | n.s. |
| 5c - 5d | -5.29 | 3.11 | -1.70 | 0.089 | 0.430 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 235.88, BIC = 248.68
- **5b vs 5a**: *β* = 1.96, *SE* = 1.276, *z* = 1.534, *p* = 0.125
- **5c vs 5a**: *β* = 1.34, *SE* = 1.383, *z* = 0.968, *p* = 0.333
- **5d vs 5a**: *β* = 0.20, *SE* = 1.365, *z* = 0.150, *p* = 0.881
- **SNR**: *β* = 0.87, *SE* = 0.261, *z* = 3.326, *p* = 0.001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -1.96 | 1.28 | -1.53 | 0.125 | 0.487 | n.s. |
| 5a - 5c | -1.34 | 1.38 | -0.97 | 0.333 | 0.743 | n.s. |
| 5a - 5d | -0.20 | 1.36 | -0.15 | 0.881 | 0.881 | n.s. |
| 5b - 5c | 0.62 | 1.08 | 0.57 | 0.567 | 0.812 | n.s. |
| 5b - 5d | 1.75 | 1.06 | 1.65 | 0.098 | 0.463 | n.s. |
| 5c - 5d | 1.14 | 1.07 | 1.06 | 0.288 | 0.743 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 367.89, BIC = 380.38
- **5b vs 5a**: *β* = 7.42, *SE* = 6.249, *z* = 1.188, *p* = 0.235
- **5c vs 5a**: *β* = 3.78, *SE* = 7.105, *z* = 0.532, *p* = 0.595
- **5d vs 5a**: *β* = 3.00, *SE* = 7.031, *z* = 0.426, *p* = 0.670
- **SNR**: *β* = -0.23, *SE* = 0.808, *z* = -0.279, *p* = 0.780

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -7.42 | 6.25 | -1.19 | 0.235 | 0.738 | n.s. |
| 5a - 5c | -3.78 | 7.11 | -0.53 | 0.595 | 0.933 | n.s. |
| 5a - 5d | -3.00 | 7.03 | -0.43 | 0.670 | 0.933 | n.s. |
| 5b - 5c | 3.64 | 4.11 | 0.89 | 0.376 | 0.848 | n.s. |
| 5b - 5d | 4.42 | 3.36 | 1.32 | 0.188 | 0.713 | n.s. |
| 5c - 5d | 0.78 | 5.22 | 0.15 | 0.881 | 0.933 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 221.96, BIC = 234.45
- **5b vs 5a**: *β* = -3.95, *SE* = 1.322, *z* = -2.991, *p* = 0.003
- **5c vs 5a**: *β* = -2.60, *SE* = 1.277, *z* = -2.035, *p* = 0.042
- **5d vs 5a**: *β* = -3.44, *SE* = 1.272, *z* = -2.707, *p* = 0.007
- **SNR**: *β* = 0.73, *SE* = 0.215, *z* = 3.375, *p* = 0.001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 3.95 | 1.32 | 2.99 | 0.003 | 0.017 | * |
| 5a - 5c | 2.60 | 1.28 | 2.03 | 0.042 | 0.157 | n.s. |
| 5a - 5d | 3.44 | 1.27 | 2.71 | 0.007 | 0.034 | * |
| 5b - 5c | -1.35 | 1.01 | -1.35 | 0.178 | 0.445 | n.s. |
| 5b - 5d | -0.51 | 0.95 | -0.54 | 0.592 | 0.604 | n.s. |
| 5c - 5d | 0.85 | 0.94 | 0.90 | 0.370 | 0.604 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.075)

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
