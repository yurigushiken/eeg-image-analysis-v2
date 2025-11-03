# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:27:31

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
| Decreasing 2 to 1 | 6 | 104.00 ms | 14.53 | 5.93 | [88.00, 120.00] |
| Decreasing 3 to 1 | 7 | 106.86 ms | 14.37 | 5.43 | [88.00, 120.00] |
| Increasing 1 to 2 | 15 | 106.67 ms | 13.06 | 3.37 | [88.00, 120.00] |
| Increasing 1 to 3 | 17 | 106.35 ms | 12.89 | 3.13 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 6 | 3.64 µV | 2.47 | 1.01 | [0.99, 7.15] |
| Decreasing 3 to 1 | 7 | 2.37 µV | 0.60 | 0.23 | [1.84, 3.43] |
| Increasing 1 to 2 | 15 | 2.79 µV | 1.74 | 0.45 | [0.68, 5.82] |
| Increasing 1 to 3 | 17 | 3.36 µV | 2.53 | 0.61 | [0.49, 9.00] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 16 | 180.75 ms | 12.41 | 3.10 | [160.00, 208.00] |
| Decreasing 3 to 1 | 20 | 184.40 ms | 17.02 | 3.80 | [156.00, 212.00] |
| Increasing 1 to 2 | 22 | 170.00 ms | 16.13 | 3.44 | [148.00, 204.00] |
| Increasing 1 to 3 | 24 | 170.83 ms | 19.93 | 4.07 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 16 | -4.99 µV | 2.67 | 0.67 | [-10.79, -1.30] |
| Decreasing 3 to 1 | 20 | -4.47 µV | 2.46 | 0.55 | [-10.41, -1.40] |
| Increasing 1 to 2 | 22 | -5.57 µV | 2.24 | 0.48 | [-9.95, -2.06] |
| Increasing 1 to 3 | 24 | -6.52 µV | 2.47 | 0.50 | [-12.65, -2.57] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 19 | 118.32 ms | 10.36 | 2.38 | [96.00, 128.00] |
| Decreasing 3 to 1 | 21 | 116.57 ms | 10.83 | 2.36 | [96.00, 128.00] |
| Increasing 1 to 2 | 12 | 114.67 ms | 11.98 | 3.46 | [96.00, 128.00] |
| Increasing 1 to 3 | 11 | 108.36 ms | 9.03 | 2.72 | [96.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 19 | 4.53 µV | 2.27 | 0.52 | [1.48, 9.13] |
| Decreasing 3 to 1 | 21 | 3.75 µV | 1.87 | 0.41 | [1.37, 9.14] |
| Increasing 1 to 2 | 12 | 2.05 µV | 1.30 | 0.37 | [0.65, 5.29] |
| Increasing 1 to 3 | 11 | 2.99 µV | 1.90 | 0.57 | [1.20, 7.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 496.80 ms | 27.67 | 6.19 | [432.00, 536.00] |
| Decreasing 3 to 1 | 20 | 475.60 ms | 27.00 | 6.04 | [420.00, 536.00] |
| Increasing 1 to 2 | 17 | 482.35 ms | 43.22 | 10.48 | [420.00, 536.00] |
| Increasing 1 to 3 | 20 | 480.40 ms | 35.09 | 7.85 | [420.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 5.68 µV | 2.78 | 0.62 | [1.47, 11.08] |
| Decreasing 3 to 1 | 20 | 5.77 µV | 3.01 | 0.67 | [1.30, 14.34] |
| Increasing 1 to 2 | 17 | 5.52 µV | 3.09 | 0.75 | [1.68, 11.52] |
| Increasing 1 to 3 | 20 | 5.93 µV | 3.64 | 0.81 | [1.71, 15.57] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 370.22, BIC = 382.86
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 2.79, *SE* = 7.115, *z* = 0.392, *p* = 0.695
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = 3.04, *SE* = 6.440, *z* = 0.471, *p* = 0.637
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = 1.99, *SE* = 6.364, *z* = 0.312, *p* = 0.755
- **SNR**: *β* = 0.96, *SE* = 1.155, *z* = 0.834, *p* = 0.404

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -2.79 | 7.12 | -0.39 | 0.695 | 0.998 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | -3.04 | 6.44 | -0.47 | 0.637 | 0.998 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | -1.98 | 6.36 | -0.31 | 0.755 | 0.998 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -0.25 | 6.52 | -0.04 | 0.970 | 0.998 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.81 | 6.45 | 0.13 | 0.900 | 0.998 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 1.05 | 4.57 | 0.23 | 0.818 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 164.04, BIC = 176.69
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -1.70, *SE* = 0.609, *z* = -2.798, *p* = 0.005
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.58, *SE* = 0.541, *z* = -1.071, *p* = 0.284
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.68, *SE* = 0.534, *z* = -1.281, *p* = 0.200
- **SNR**: *β* = 0.84, *SE* = 0.106, *z* = 7.939, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 1.70 | 0.61 | 2.80 | 0.005 | 0.030 | * |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.58 | 0.54 | 1.07 | 0.284 | 0.488 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.68 | 0.53 | 1.28 | 0.200 | 0.488 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -1.12 | 0.50 | -2.25 | 0.025 | 0.117 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -1.02 | 0.49 | -2.07 | 0.038 | 0.144 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.10 | 0.38 | 0.27 | 0.786 | 0.786 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 687.28, BIC = 704.13
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 3.58, *SE* = 4.120, *z* = 0.868, *p* = 0.385
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -11.07, *SE* = 4.175, *z* = -2.651, *p* = 0.008
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -9.64, *SE* = 4.381, *z* = -2.201, *p* = 0.028
- **SNR**: *β* = -0.21, *SE* = 0.570, *z* = -0.373, *p* = 0.709

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -3.58 | 4.12 | -0.87 | 0.385 | 0.622 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 11.07 | 4.17 | 2.65 | 0.008 | 0.032 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 9.64 | 4.38 | 2.20 | 0.028 | 0.081 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 14.64 | 3.86 | 3.80 | < .001 | < .001 | *** |
| Decreasing 3 to 1 - Increasing 1 to 3 | 13.22 | 4.11 | 3.22 | 0.001 | 0.006 | ** |
| Increasing 1 to 2 - Increasing 1 to 3 | -1.42 | 3.68 | -0.39 | 0.699 | 0.699 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.97, *p* = 0.005, η²_G = 0.107
- Greenhouse-Geisser corrected: *p* = 0.015 (ε = 0.650)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.90 | 14 | = 0.460 | -0.15 [-0.79, 0.33] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 3.26 | 14 | = 0.030 | 0.70 [0.20, 1.49] | medium | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 1.91 | 14 | = 0.115 | 0.56 [-0.02, 1.12] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.98 | 14 | = 0.030 | 0.76 [0.27, 1.36] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.23 | 14 | = 0.085 | 0.63 [0.22, 1.29] | medium | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.28 | 14 | = 0.786 | -0.06 [-0.52, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 326.13, BIC = 342.98
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 0.20, *SE* = 0.448, *z* = 0.438, *p* = 0.661
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.41, *SE* = 0.459, *z* = -0.892, *p* = 0.372
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.70, *SE* = 0.484, *z* = -1.439, *p* = 0.150
- **SNR**: *β* = -0.42, *SE* = 0.064, *z* = -6.549, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -0.20 | 0.45 | -0.44 | 0.661 | 0.753 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.41 | 0.46 | 0.89 | 0.372 | 0.753 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.70 | 0.48 | 1.44 | 0.150 | 0.556 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 0.61 | 0.42 | 1.44 | 0.150 | 0.556 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.89 | 0.45 | 1.98 | 0.047 | 0.253 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.29 | 0.40 | 0.72 | 0.471 | 0.753 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.38, *p* = 0.001, η²_G = 0.140
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.38 | 14 | = 0.710 | -0.09 [-0.65, 0.46] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.03 | 14 | = 0.074 | 0.56 [-0.07, 1.11] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 3.11 | 14 | = 0.023 | 0.80 [0.24, 1.49] | medium | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.32 | 14 | = 0.065 | 0.69 [0.07, 1.08] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 3.50 | 14 | = 0.021 | 0.92 [0.36, 1.48] | large | * |
| Increasing 1 to 2 vs Increasing 1 to 3 | 2.22 | 14 | = 0.065 | 0.34 [0.06, 1.01] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 485.69, BIC = 500.70
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -1.35, *SE* = 3.133, *z* = -0.432, *p* = 0.666
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -3.38, *SE* = 3.807, *z* = -0.888, *p* = 0.374
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -10.04, *SE* = 3.761, *z* = -2.670, *p* = 0.008
- **SNR**: *β* = 0.06, *SE* = 0.544, *z* = 0.111, *p* = 0.912

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 1.35 | 3.13 | 0.43 | 0.666 | 0.816 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 3.38 | 3.81 | 0.89 | 0.374 | 0.755 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 10.04 | 3.76 | 2.67 | 0.008 | 0.045 | * |
| Decreasing 3 to 1 - Increasing 1 to 2 | 2.03 | 3.58 | 0.57 | 0.571 | 0.816 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 8.69 | 3.66 | 2.38 | 0.017 | 0.084 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 6.66 | 4.08 | 1.63 | 0.103 | 0.352 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.55, *p* = 0.088, η²_G = 0.244
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.42 | 6 | = 0.747 | -0.22 [-0.57, 0.46] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.34 | 6 | = 0.747 | 0.22 [-0.53, 0.91] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.50 | 6 | = 0.140 | 1.19 [-0.06, 1.55] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 0.74 | 6 | = 0.728 | 0.41 [-0.29, 1.11] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.86 | 6 | = 0.140 | 1.48 [0.07, 1.63] | large | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 1.73 | 6 | = 0.269 | 0.82 [-0.18, 1.73] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 233.35, BIC = 248.35
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.35, *SE* = 0.403, *z* = -0.860, *p* = 0.390
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -1.56, *SE* = 0.501, *z* = -3.116, *p* = 0.002
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.96, *SE* = 0.497, *z* = -1.941, *p* = 0.052
- **SNR**: *β* = 0.45, *SE* = 0.074, *z* = 6.025, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.35 | 0.40 | 0.86 | 0.390 | 0.478 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 1.56 | 0.50 | 3.12 | 0.002 | 0.011 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.96 | 0.50 | 1.94 | 0.052 | 0.193 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 1.21 | 0.47 | 2.57 | 0.010 | 0.050 | * |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.62 | 0.48 | 1.30 | 0.195 | 0.478 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.60 | 0.53 | -1.12 | 0.261 | 0.478 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.24, *p* = 0.004, η²_G = 0.308
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 1.06 | 6 | = 0.345 | 0.27 [-0.16, 0.90] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 3.73 | 6 | = 0.051 | 1.63 [0.32, 2.25] | large | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.95 | 6 | = 0.051 | 0.97 [-0.04, 1.60] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 3.26 | 6 | = 0.051 | 1.43 [0.13, 1.75] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.69 | 6 | = 0.212 | 0.74 [-0.13, 1.33] | medium | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.02 | 6 | = 0.345 | -0.58 [-1.18, 0.54] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 766.64, BIC = 783.04
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -22.53, *SE* = 9.777, *z* = -2.305, *p* = 0.021
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -13.33, *SE* = 9.882, *z* = -1.349, *p* = 0.177
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -16.82, *SE* = 9.534, *z* = -1.764, *p* = 0.078
- **SNR**: *β* = 0.15, *SE* = 0.776, *z* = 0.193, *p* = 0.847

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 22.53 | 9.78 | 2.30 | 0.021 | 0.121 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 13.33 | 9.88 | 1.35 | 0.177 | 0.542 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 16.82 | 9.53 | 1.76 | 0.078 | 0.333 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -9.20 | 10.25 | -0.90 | 0.369 | 0.749 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -5.72 | 9.61 | -0.59 | 0.552 | 0.799 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 3.49 | 9.96 | 0.35 | 0.726 | 0.799 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.04, *p* = 0.123, η²_G = 0.087
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 2.65 | 14 | = 0.115 | 1.10 [0.19, 1.31] | large | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.42 | 14 | = 0.358 | 0.49 [-0.32, 0.72] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.08 | 14 | = 0.169 | 0.56 [-0.05, 1.04] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | -0.87 | 14 | = 0.514 | -0.29 [-0.81, 0.28] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.82 | 14 | = 0.514 | -0.30 [-0.66, 0.34] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.04 | 14 | = 0.969 | 0.01 [-0.44, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 365.86, BIC = 382.27
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.64, *SE* = 0.644, *z* = -0.991, *p* = 0.322
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.30, *SE* = 0.647, *z* = -0.464, *p* = 0.643
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = 0.12, *SE* = 0.632, *z* = 0.189, *p* = 0.850
- **SNR**: *β* = 0.26, *SE* = 0.054, *z* = 4.770, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.64 | 0.64 | 0.99 | 0.322 | 0.856 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.30 | 0.65 | 0.46 | 0.643 | 0.948 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | -0.12 | 0.63 | -0.19 | 0.850 | 0.948 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -0.34 | 0.67 | -0.50 | 0.616 | 0.948 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.76 | 0.63 | -1.20 | 0.230 | 0.792 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.42 | 0.66 | -0.64 | 0.522 | 0.948 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.774, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.08 | 14 | = 0.940 | -0.02 [-0.53, 0.47] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.56 | 14 | = 0.862 | 0.18 [-0.41, 0.62] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | -0.47 | 14 | = 0.862 | -0.14 [-0.66, 0.37] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 0.57 | 14 | = 0.862 | 0.18 [-0.38, 0.69] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.37 | 14 | = 0.862 | -0.11 [-0.58, 0.42] | negligible | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.30 | 14 | = 0.862 | -0.28 [-0.88, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.70)
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 2 (*d* = 0.76)
**N1 amplitude:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 0.80)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 0.92)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.088)
**P1 amplitude:** Significant main effect of condition (*p* = 0.004) (no significant pairwise comparisons)

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
