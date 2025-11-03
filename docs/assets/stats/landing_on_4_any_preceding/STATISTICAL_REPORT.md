# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:45:50

---

## 1. Analysis Overview

**Total Measurements:** 576
**Number of Subjects:** 24
**Number of Conditions:** 6

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
| 1 to 4 | 11 | 108.36 ms | 9.20 | 2.77 | [96.00, 116.00] |
| 2 to 4 | 8 | 113.50 ms | 7.07 | 2.50 | [96.00, 116.00] |
| 3 to 4 | 7 | 112.00 ms | 7.66 | 2.89 | [96.00, 116.00] |
| 5 to 4 | 9 | 105.78 ms | 9.82 | 3.27 | [96.00, 116.00] |
| 6 to 4 | 6 | 106.00 ms | 10.95 | 4.47 | [96.00, 116.00] |
| Cardinality4 | 10 | 105.60 ms | 9.65 | 3.05 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 11 | 2.43 µV | 1.68 | 0.51 | [0.42, 6.01] |
| 2 to 4 | 8 | 1.71 µV | 0.88 | 0.31 | [0.58, 3.15] |
| 3 to 4 | 7 | 2.28 µV | 1.49 | 0.56 | [1.05, 4.59] |
| 5 to 4 | 9 | 3.35 µV | 1.89 | 0.63 | [0.61, 6.13] |
| 6 to 4 | 6 | 2.44 µV | 1.15 | 0.47 | [1.05, 3.78] |
| Cardinality4 | 10 | 1.88 µV | 1.29 | 0.41 | [0.58, 4.79] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | 169.09 ms | 16.52 | 3.52 | [144.00, 204.00] |
| 2 to 4 | 22 | 171.27 ms | 15.50 | 3.30 | [144.00, 196.00] |
| 3 to 4 | 22 | 164.55 ms | 16.01 | 3.41 | [144.00, 204.00] |
| 5 to 4 | 23 | 173.39 ms | 19.05 | 3.97 | [144.00, 204.00] |
| 6 to 4 | 24 | 173.00 ms | 20.10 | 4.10 | [144.00, 204.00] |
| Cardinality4 | 22 | 171.27 ms | 19.93 | 4.25 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | -6.72 µV | 2.75 | 0.59 | [-12.55, -2.56] |
| 2 to 4 | 22 | -6.66 µV | 2.63 | 0.56 | [-15.66, -2.59] |
| 3 to 4 | 22 | -5.65 µV | 2.22 | 0.47 | [-10.31, -2.95] |
| 5 to 4 | 23 | -6.01 µV | 2.78 | 0.58 | [-14.15, -1.72] |
| 6 to 4 | 24 | -5.41 µV | 2.71 | 0.55 | [-12.20, -1.17] |
| Cardinality4 | 22 | -5.95 µV | 3.12 | 0.67 | [-13.09, -1.82] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 12 | 105.33 ms | 10.28 | 2.97 | [92.00, 120.00] |
| 2 to 4 | 18 | 107.56 ms | 10.97 | 2.58 | [92.00, 120.00] |
| 3 to 4 | 14 | 106.29 ms | 10.72 | 2.87 | [92.00, 120.00] |
| 5 to 4 | 15 | 110.40 ms | 10.99 | 2.84 | [92.00, 120.00] |
| 6 to 4 | 15 | 110.40 ms | 8.53 | 2.20 | [92.00, 120.00] |
| Cardinality4 | 12 | 109.33 ms | 10.14 | 2.93 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 12 | 3.45 µV | 1.84 | 0.53 | [1.06, 6.92] |
| 2 to 4 | 18 | 2.70 µV | 1.86 | 0.44 | [1.12, 7.56] |
| 3 to 4 | 14 | 3.41 µV | 2.16 | 0.58 | [0.38, 7.39] |
| 5 to 4 | 15 | 2.98 µV | 1.81 | 0.47 | [0.98, 7.17] |
| 6 to 4 | 15 | 3.71 µV | 2.08 | 0.54 | [0.71, 7.60] |
| Cardinality4 | 12 | 3.32 µV | 1.89 | 0.55 | [0.96, 6.93] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 19 | 489.68 ms | 31.34 | 7.19 | [432.00, 536.00] |
| 2 to 4 | 18 | 486.67 ms | 34.16 | 8.05 | [432.00, 536.00] |
| 3 to 4 | 17 | 490.82 ms | 37.97 | 9.21 | [432.00, 536.00] |
| 5 to 4 | 18 | 497.33 ms | 30.43 | 7.17 | [440.00, 536.00] |
| 6 to 4 | 19 | 487.37 ms | 32.31 | 7.41 | [432.00, 536.00] |
| Cardinality4 | 12 | 484.00 ms | 32.54 | 9.39 | [432.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 19 | 5.69 µV | 3.03 | 0.69 | [1.91, 11.88] |
| 2 to 4 | 18 | 6.90 µV | 4.16 | 0.98 | [1.37, 17.43] |
| 3 to 4 | 17 | 6.01 µV | 3.17 | 0.77 | [1.82, 12.86] |
| 5 to 4 | 18 | 6.10 µV | 3.13 | 0.74 | [1.76, 11.49] |
| 6 to 4 | 19 | 5.40 µV | 2.49 | 0.57 | [1.73, 9.62] |
| Cardinality4 | 12 | 4.24 µV | 2.47 | 0.71 | [2.14, 8.96] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 376.48, BIC = 393.87
- **2 to 4 vs 1 to 4**: *β* = 5.91, *SE* = 3.534, *z* = 1.672, *p* = 0.095
- **3 to 4 vs 1 to 4**: *β* = 2.42, *SE* = 3.561, *z* = 0.679, *p* = 0.497
- **5 to 4 vs 1 to 4**: *β* = -2.02, *SE* = 3.337, *z* = -0.605, *p* = 0.545
- **6 to 4 vs 1 to 4**: *β* = -1.95, *SE* = 3.783, *z* = -0.516, *p* = 0.606
- **Cardinality4 vs 1 to 4**: *β* = -3.83, *SE* = 3.238, *z* = -1.181, *p* = 0.237
- **SNR**: *β* = -0.29, *SE* = 0.897, *z* = -0.320, *p* = 0.749

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -5.91 | 3.53 | -1.67 | 0.095 | 0.665 | n.s. |
| 1 to 4 - 3 to 4 | -2.42 | 3.56 | -0.68 | 0.497 | 0.984 | n.s. |
| 1 to 4 - 5 to 4 | 2.02 | 3.34 | 0.61 | 0.545 | 0.984 | n.s. |
| 1 to 4 - 6 to 4 | 1.95 | 3.78 | 0.52 | 0.606 | 0.984 | n.s. |
| 1 to 4 - Cardinality4 | 3.82 | 3.24 | 1.18 | 0.237 | 0.928 | n.s. |
| 2 to 4 - 3 to 4 | 3.49 | 3.88 | 0.90 | 0.369 | 0.960 | n.s. |
| 2 to 4 - 5 to 4 | 7.93 | 3.75 | 2.12 | 0.034 | 0.387 | n.s. |
| 2 to 4 - 6 to 4 | 7.86 | 4.00 | 1.96 | 0.050 | 0.484 | n.s. |
| 2 to 4 - Cardinality4 | 9.73 | 3.58 | 2.72 | 0.006 | 0.093 | n.s. |
| 3 to 4 - 5 to 4 | 4.44 | 3.71 | 1.20 | 0.231 | 0.928 | n.s. |
| 3 to 4 - 6 to 4 | 4.37 | 4.11 | 1.06 | 0.287 | 0.933 | n.s. |
| 3 to 4 - Cardinality4 | 6.24 | 3.62 | 1.73 | 0.084 | 0.653 | n.s. |
| 5 to 4 - 6 to 4 | -0.07 | 4.05 | -0.02 | 0.987 | 0.987 | n.s. |
| 5 to 4 - Cardinality4 | 1.80 | 3.62 | 0.50 | 0.618 | 0.984 | n.s. |
| 6 to 4 - Cardinality4 | 1.87 | 3.94 | 0.47 | 0.635 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 150.82, BIC = 168.21
- **2 to 4 vs 1 to 4**: *β* = -0.29, *SE* = 0.378, *z* = -0.756, *p* = 0.450
- **3 to 4 vs 1 to 4**: *β* = -0.14, *SE* = 0.386, *z* = -0.360, *p* = 0.719
- **5 to 4 vs 1 to 4**: *β* = 0.52, *SE* = 0.359, *z* = 1.461, *p* = 0.144
- **6 to 4 vs 1 to 4**: *β* = 0.29, *SE* = 0.411, *z* = 0.703, *p* = 0.482
- **Cardinality4 vs 1 to 4**: *β* = -0.28, *SE* = 0.350, *z* = -0.800, *p* = 0.424
- **SNR**: *β* = 0.76, *SE* = 0.097, *z* = 7.844, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 0.29 | 0.38 | 0.76 | 0.450 | 0.988 | n.s. |
| 1 to 4 - 3 to 4 | 0.14 | 0.39 | 0.36 | 0.719 | 0.993 | n.s. |
| 1 to 4 - 5 to 4 | -0.52 | 0.36 | -1.46 | 0.144 | 0.846 | n.s. |
| 1 to 4 - 6 to 4 | -0.29 | 0.41 | -0.70 | 0.482 | 0.988 | n.s. |
| 1 to 4 - Cardinality4 | 0.28 | 0.35 | 0.80 | 0.424 | 0.988 | n.s. |
| 2 to 4 - 3 to 4 | -0.15 | 0.41 | -0.36 | 0.721 | 0.993 | n.s. |
| 2 to 4 - 5 to 4 | -0.81 | 0.40 | -2.02 | 0.044 | 0.466 | n.s. |
| 2 to 4 - 6 to 4 | -0.57 | 0.43 | -1.34 | 0.182 | 0.876 | n.s. |
| 2 to 4 - Cardinality4 | -0.01 | 0.37 | -0.02 | 0.987 | 0.993 | n.s. |
| 3 to 4 - 5 to 4 | -0.66 | 0.39 | -1.68 | 0.093 | 0.718 | n.s. |
| 3 to 4 - 6 to 4 | -0.43 | 0.44 | -0.98 | 0.326 | 0.971 | n.s. |
| 3 to 4 - Cardinality4 | 0.14 | 0.39 | 0.36 | 0.716 | 0.993 | n.s. |
| 5 to 4 - 6 to 4 | 0.23 | 0.44 | 0.54 | 0.591 | 0.989 | n.s. |
| 5 to 4 - Cardinality4 | 0.80 | 0.39 | 2.09 | 0.037 | 0.432 | n.s. |
| 6 to 4 - Cardinality4 | 0.57 | 0.42 | 1.36 | 0.173 | 0.876 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1112.28, BIC = 1138.42
- **2 to 4 vs 1 to 4**: *β* = 1.90, *SE* = 3.469, *z* = 0.548, *p* = 0.584
- **3 to 4 vs 1 to 4**: *β* = -4.18, *SE* = 3.472, *z* = -1.203, *p* = 0.229
- **5 to 4 vs 1 to 4**: *β* = 3.42, *SE* = 3.425, *z* = 0.998, *p* = 0.318
- **6 to 4 vs 1 to 4**: *β* = 2.33, *SE* = 3.401, *z* = 0.685, *p* = 0.493
- **Cardinality4 vs 1 to 4**: *β* = 1.49, *SE* = 3.488, *z* = 0.428, *p* = 0.669
- **SNR**: *β* = 0.34, *SE* = 0.355, *z* = 0.957, *p* = 0.338

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -1.90 | 3.47 | -0.55 | 0.584 | 0.999 | n.s. |
| 1 to 4 - 3 to 4 | 4.18 | 3.47 | 1.20 | 0.229 | 0.943 | n.s. |
| 1 to 4 - 5 to 4 | -3.42 | 3.43 | -1.00 | 0.318 | 0.978 | n.s. |
| 1 to 4 - 6 to 4 | -2.33 | 3.40 | -0.69 | 0.493 | 0.998 | n.s. |
| 1 to 4 - Cardinality4 | -1.49 | 3.49 | -0.43 | 0.669 | 0.999 | n.s. |
| 2 to 4 - 3 to 4 | 6.08 | 3.48 | 1.74 | 0.081 | 0.667 | n.s. |
| 2 to 4 - 5 to 4 | -1.52 | 3.44 | -0.44 | 0.659 | 0.999 | n.s. |
| 2 to 4 - 6 to 4 | -0.43 | 3.40 | -0.13 | 0.899 | 0.999 | n.s. |
| 2 to 4 - Cardinality4 | 0.41 | 3.48 | 0.12 | 0.907 | 0.999 | n.s. |
| 3 to 4 - 5 to 4 | -7.60 | 3.46 | -2.20 | 0.028 | 0.348 | n.s. |
| 3 to 4 - 6 to 4 | -6.51 | 3.41 | -1.91 | 0.057 | 0.557 | n.s. |
| 3 to 4 - Cardinality4 | -5.67 | 3.50 | -1.62 | 0.105 | 0.738 | n.s. |
| 5 to 4 - 6 to 4 | 1.09 | 3.35 | 0.32 | 0.746 | 0.999 | n.s. |
| 5 to 4 - Cardinality4 | 1.92 | 3.44 | 0.56 | 0.576 | 0.999 | n.s. |
| 6 to 4 - Cardinality4 | 0.84 | 3.39 | 0.25 | 0.805 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.383, η²_G = 0.024
- Greenhouse-Geisser corrected: *p* = 0.364 (ε = 0.505)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.64 | 18 | = 0.775 | -0.20 [-0.62, 0.30] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 0.75 | 18 | = 0.770 | 0.22 [-0.22, 0.68] | small | n.s. |
| 1 to 4 vs 5 to 4 | -1.65 | 18 | = 0.582 | -0.27 [-0.69, 0.21] | small | n.s. |
| 1 to 4 vs 6 to 4 | -1.08 | 18 | = 0.737 | -0.18 [-0.60, 0.29] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | -0.15 | 18 | = 0.948 | -0.03 [-0.50, 0.44] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 2.78 | 18 | = 0.183 | 0.41 [0.10, 1.08] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.36 | 18 | = 0.833 | -0.10 [-0.55, 0.36] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.05 | 18 | = 0.964 | -0.01 [-0.47, 0.42] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | 0.50 | 18 | = 0.775 | 0.16 [-0.39, 0.55] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -2.00 | 18 | = 0.453 | -0.46 [-0.96, -0.02] | small | n.s. |
| 3 to 4 vs 6 to 4 | -1.44 | 18 | = 0.625 | -0.37 [-0.81, 0.10] | small | n.s. |
| 3 to 4 vs Cardinality4 | -0.76 | 18 | = 0.770 | -0.23 [-0.73, 0.22] | small | n.s. |
| 5 to 4 vs 6 to 4 | 0.57 | 18 | = 0.775 | 0.08 [-0.28, 0.59] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | 1.13 | 18 | = 0.737 | 0.23 [-0.34, 0.58] | small | n.s. |
| 6 to 4 vs Cardinality4 | 0.94 | 18 | = 0.768 | 0.15 [-0.36, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 564.91, BIC = 591.06
- **2 to 4 vs 1 to 4**: *β* = 0.04, *SE* = 0.464, *z* = 0.089, *p* = 0.929
- **3 to 4 vs 1 to 4**: *β* = 0.65, *SE* = 0.464, *z* = 1.389, *p* = 0.165
- **5 to 4 vs 1 to 4**: *β* = 0.69, *SE* = 0.458, *z* = 1.502, *p* = 0.133
- **6 to 4 vs 1 to 4**: *β* = 1.06, *SE* = 0.454, *z* = 2.332, *p* = 0.020
- **Cardinality4 vs 1 to 4**: *β* = 0.61, *SE* = 0.466, *z* = 1.309, *p* = 0.190
- **SNR**: *β* = -0.39, *SE* = 0.047, *z* = -8.303, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.04 | 0.46 | -0.09 | 0.929 | 1.000 | n.s. |
| 1 to 4 - 3 to 4 | -0.64 | 0.46 | -1.39 | 0.165 | 0.877 | n.s. |
| 1 to 4 - 5 to 4 | -0.69 | 0.46 | -1.50 | 0.133 | 0.844 | n.s. |
| 1 to 4 - 6 to 4 | -1.06 | 0.45 | -2.33 | 0.020 | 0.258 | n.s. |
| 1 to 4 - Cardinality4 | -0.61 | 0.47 | -1.31 | 0.190 | 0.879 | n.s. |
| 2 to 4 - 3 to 4 | -0.60 | 0.47 | -1.30 | 0.195 | 0.879 | n.s. |
| 2 to 4 - 5 to 4 | -0.65 | 0.46 | -1.40 | 0.160 | 0.877 | n.s. |
| 2 to 4 - 6 to 4 | -1.02 | 0.45 | -2.24 | 0.025 | 0.297 | n.s. |
| 2 to 4 - Cardinality4 | -0.57 | 0.47 | -1.22 | 0.222 | 0.879 | n.s. |
| 3 to 4 - 5 to 4 | -0.04 | 0.46 | -0.09 | 0.926 | 1.000 | n.s. |
| 3 to 4 - 6 to 4 | -0.41 | 0.46 | -0.91 | 0.363 | 0.934 | n.s. |
| 3 to 4 - Cardinality4 | 0.03 | 0.47 | 0.07 | 0.941 | 1.000 | n.s. |
| 5 to 4 - 6 to 4 | -0.37 | 0.45 | -0.83 | 0.407 | 0.934 | n.s. |
| 5 to 4 - Cardinality4 | 0.08 | 0.46 | 0.17 | 0.866 | 1.000 | n.s. |
| 6 to 4 - Cardinality4 | 0.45 | 0.45 | 0.99 | 0.322 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.93, *p* = 0.097, η²_G = 0.042
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.52 | 18 | = 0.701 | -0.11 [-0.56, 0.35] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | -4.02 | 18 | = 0.012 | -0.69 [-0.93, 0.00] | medium | * |
| 1 to 4 vs 5 to 4 | -1.69 | 18 | = 0.272 | -0.29 [-0.69, 0.21] | small | n.s. |
| 1 to 4 vs 6 to 4 | -1.97 | 18 | = 0.240 | -0.47 [-0.80, 0.11] | small | n.s. |
| 1 to 4 vs Cardinality4 | -2.11 | 18 | = 0.240 | -0.33 [-0.97, 0.02] | small | n.s. |
| 2 to 4 vs 3 to 4 | -2.04 | 18 | = 0.240 | -0.57 [-0.74, 0.18] | medium | n.s. |
| 2 to 4 vs 5 to 4 | -0.69 | 18 | = 0.660 | -0.18 [-0.54, 0.37] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -1.15 | 18 | = 0.511 | -0.36 [-0.74, 0.16] | small | n.s. |
| 2 to 4 vs Cardinality4 | -1.05 | 18 | = 0.511 | -0.23 [-0.73, 0.22] | small | n.s. |
| 3 to 4 vs 5 to 4 | 1.72 | 18 | = 0.272 | 0.34 [-0.21, 0.69] | small | n.s. |
| 3 to 4 vs 6 to 4 | 0.64 | 18 | = 0.660 | 0.16 [-0.41, 0.48] | negligible | n.s. |
| 3 to 4 vs Cardinality4 | 1.09 | 18 | = 0.511 | 0.25 [-0.28, 0.67] | small | n.s. |
| 5 to 4 vs 6 to 4 | -0.67 | 18 | = 0.660 | -0.17 [-0.60, 0.27] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | -0.26 | 18 | = 0.799 | -0.06 [-0.48, 0.43] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 0.46 | 18 | = 0.701 | 0.10 [-0.28, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 641.19, BIC = 663.28
- **2 to 4 vs 1 to 4**: *β* = 3.93, *SE* = 3.068, *z* = 1.280, *p* = 0.200
- **3 to 4 vs 1 to 4**: *β* = 3.11, *SE* = 3.281, *z* = 0.947, *p* = 0.344
- **5 to 4 vs 1 to 4**: *β* = 7.31, *SE* = 3.180, *z* = 2.299, *p* = 0.022
- **6 to 4 vs 1 to 4**: *β* = 6.63, *SE* = 3.150, *z* = 2.105, *p* = 0.035
- **Cardinality4 vs 1 to 4**: *β* = 4.18, *SE* = 3.279, *z* = 1.274, *p* = 0.203
- **SNR**: *β* = 0.86, *SE* = 0.691, *z* = 1.240, *p* = 0.215

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -3.93 | 3.07 | -1.28 | 0.200 | 0.932 | n.s. |
| 1 to 4 - 3 to 4 | -3.11 | 3.28 | -0.95 | 0.344 | 0.959 | n.s. |
| 1 to 4 - 5 to 4 | -7.31 | 3.18 | -2.30 | 0.022 | 0.278 | n.s. |
| 1 to 4 - 6 to 4 | -6.63 | 3.15 | -2.10 | 0.035 | 0.396 | n.s. |
| 1 to 4 - Cardinality4 | -4.18 | 3.28 | -1.27 | 0.203 | 0.932 | n.s. |
| 2 to 4 - 3 to 4 | 0.82 | 2.94 | 0.28 | 0.779 | 0.996 | n.s. |
| 2 to 4 - 5 to 4 | -3.38 | 2.83 | -1.20 | 0.232 | 0.932 | n.s. |
| 2 to 4 - 6 to 4 | -2.70 | 2.90 | -0.93 | 0.351 | 0.959 | n.s. |
| 2 to 4 - Cardinality4 | -0.25 | 3.09 | -0.08 | 0.935 | 0.996 | n.s. |
| 3 to 4 - 5 to 4 | -4.21 | 3.05 | -1.38 | 0.168 | 0.909 | n.s. |
| 3 to 4 - 6 to 4 | -3.52 | 3.02 | -1.17 | 0.243 | 0.932 | n.s. |
| 3 to 4 - Cardinality4 | -1.07 | 3.30 | -0.32 | 0.745 | 0.996 | n.s. |
| 5 to 4 - 6 to 4 | 0.68 | 3.00 | 0.23 | 0.820 | 0.996 | n.s. |
| 5 to 4 - Cardinality4 | 3.13 | 3.20 | 0.98 | 0.328 | 0.959 | n.s. |
| 6 to 4 - Cardinality4 | 2.45 | 3.13 | 0.78 | 0.433 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.813, η²_G = 0.072
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.24 | 3 | = 0.959 | -0.17 [-1.03, 0.43] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 0.00 | 3 | = 1.000 | 0.00 [-1.35, 0.57] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -1.00 | 3 | = 0.922 | -0.71 [-1.50, 0.19] | medium | n.s. |
| 1 to 4 vs 6 to 4 | -1.00 | 3 | = 0.922 | -0.60 [-1.87, -0.02] | medium | n.s. |
| 1 to 4 vs Cardinality4 | -0.40 | 3 | = 0.959 | -0.11 [-1.04, 0.53] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 0.21 | 3 | = 0.959 | 0.15 [-0.69, 0.74] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.93 | 3 | = 0.922 | -0.39 [-0.82, 0.40] | small | n.s. |
| 2 to 4 vs 6 to 4 | -0.63 | 3 | = 0.951 | -0.30 [-0.96, 0.41] | small | n.s. |
| 2 to 4 vs Cardinality4 | 0.14 | 3 | = 0.959 | 0.09 [-0.91, 0.64] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -0.81 | 3 | = 0.922 | -0.59 [-1.16, 0.43] | medium | n.s. |
| 3 to 4 vs 6 to 4 | -0.78 | 3 | = 0.922 | -0.50 [-0.96, 0.41] | small | n.s. |
| 3 to 4 vs Cardinality4 | -0.24 | 3 | = 0.959 | -0.09 [-1.35, 0.79] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 1.00 | 3 | = 0.922 | 0.19 [-0.29, 1.22] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | 1.32 | 3 | = 0.922 | 0.80 [-0.40, 1.36] | medium | n.s. |
| 6 to 4 vs Cardinality4 | 1.41 | 3 | = 0.922 | 0.67 [-0.28, 1.23] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 272.82, BIC = 294.91
- **2 to 4 vs 1 to 4**: *β* = -0.05, *SE* = 0.352, *z* = -0.148, *p* = 0.882
- **3 to 4 vs 1 to 4**: *β* = 0.53, *SE* = 0.376, *z* = 1.422, *p* = 0.155
- **5 to 4 vs 1 to 4**: *β* = 0.24, *SE* = 0.363, *z* = 0.649, *p* = 0.516
- **6 to 4 vs 1 to 4**: *β* = 0.38, *SE* = 0.359, *z* = 1.057, *p* = 0.291
- **Cardinality4 vs 1 to 4**: *β* = -0.03, *SE* = 0.375, *z* = -0.076, *p* = 0.940
- **SNR**: *β* = 0.81, *SE* = 0.080, *z* = 10.138, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 0.05 | 0.35 | 0.15 | 0.882 | 0.998 | n.s. |
| 1 to 4 - 3 to 4 | -0.53 | 0.38 | -1.42 | 0.155 | 0.888 | n.s. |
| 1 to 4 - 5 to 4 | -0.24 | 0.36 | -0.65 | 0.516 | 0.988 | n.s. |
| 1 to 4 - 6 to 4 | -0.38 | 0.36 | -1.06 | 0.291 | 0.968 | n.s. |
| 1 to 4 - Cardinality4 | 0.03 | 0.38 | 0.08 | 0.940 | 0.998 | n.s. |
| 2 to 4 - 3 to 4 | -0.59 | 0.34 | -1.74 | 0.082 | 0.721 | n.s. |
| 2 to 4 - 5 to 4 | -0.29 | 0.32 | -0.89 | 0.373 | 0.985 | n.s. |
| 2 to 4 - 6 to 4 | -0.43 | 0.33 | -1.30 | 0.193 | 0.924 | n.s. |
| 2 to 4 - Cardinality4 | -0.02 | 0.35 | -0.07 | 0.947 | 0.998 | n.s. |
| 3 to 4 - 5 to 4 | 0.30 | 0.35 | 0.85 | 0.395 | 0.985 | n.s. |
| 3 to 4 - 6 to 4 | 0.15 | 0.35 | 0.45 | 0.655 | 0.995 | n.s. |
| 3 to 4 - Cardinality4 | 0.56 | 0.38 | 1.49 | 0.137 | 0.872 | n.s. |
| 5 to 4 - 6 to 4 | -0.14 | 0.34 | -0.42 | 0.676 | 0.995 | n.s. |
| 5 to 4 - Cardinality4 | 0.26 | 0.37 | 0.72 | 0.471 | 0.988 | n.s. |
| 6 to 4 - Cardinality4 | 0.41 | 0.36 | 1.14 | 0.252 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.22, *p* = 0.036, η²_G = 0.136
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.84 | 3 | = 0.626 | -0.28 [-0.65, 0.78] | small | n.s. |
| 1 to 4 vs 3 to 4 | 1.71 | 3 | = 0.370 | 0.45 [-0.92, 0.93] | small | n.s. |
| 1 to 4 vs 5 to 4 | 0.69 | 3 | = 0.626 | 0.37 [-0.56, 0.99] | small | n.s. |
| 1 to 4 vs 6 to 4 | -0.68 | 3 | = 0.626 | -0.18 [-0.93, 0.62] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | 3.71 | 3 | = 0.128 | 0.85 [-0.81, 0.73] | large | n.s. |
| 2 to 4 vs 3 to 4 | 6.57 | 3 | = 0.054 | 0.66 [-0.82, 0.61] | medium | n.s. |
| 2 to 4 vs 5 to 4 | 2.43 | 3 | = 0.234 | 0.57 [-0.72, 0.49] | medium | n.s. |
| 2 to 4 vs 6 to 4 | 1.08 | 3 | = 0.537 | 0.12 [-1.26, 0.18] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | 3.06 | 3 | = 0.165 | 1.00 [-0.93, 0.61] | large | n.s. |
| 3 to 4 vs 5 to 4 | -0.09 | 3 | = 0.935 | -0.03 [-0.54, 1.02] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | -44.99 | 3 | < .001 | -0.60 [-1.53, -0.00] | medium | *** |
| 3 to 4 vs Cardinality4 | 1.15 | 3 | = 0.537 | 0.28 [-0.73, 1.43] | small | n.s. |
| 5 to 4 vs 6 to 4 | -1.65 | 3 | = 0.370 | -0.51 [-1.13, 0.35] | medium | n.s. |
| 5 to 4 vs Cardinality4 | 0.58 | 3 | = 0.643 | 0.27 [-0.69, 0.99] | small | n.s. |
| 6 to 4 vs Cardinality4 | 4.15 | 3 | = 0.127 | 0.99 [-0.53, 0.92] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1022.31, BIC = 1046.02
- **2 to 4 vs 1 to 4**: *β* = -2.05, *SE* = 9.945, *z* = -0.206, *p* = 0.837
- **3 to 4 vs 1 to 4**: *β* = 0.40, *SE* = 10.102, *z* = 0.039, *p* = 0.969
- **5 to 4 vs 1 to 4**: *β* = 8.15, *SE* = 9.867, *z* = 0.826, *p* = 0.409
- **6 to 4 vs 1 to 4**: *β* = -2.55, *SE* = 9.795, *z* = -0.260, *p* = 0.795
- **Cardinality4 vs 1 to 4**: *β* = -4.85, *SE* = 11.492, *z* = -0.422, *p* = 0.673
- **SNR**: *β* = -0.34, *SE* = 1.062, *z* = -0.324, *p* = 0.746

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 2.05 | 9.95 | 0.21 | 0.837 | 1.000 | n.s. |
| 1 to 4 - 3 to 4 | -0.40 | 10.10 | -0.04 | 0.969 | 1.000 | n.s. |
| 1 to 4 - 5 to 4 | -8.15 | 9.87 | -0.83 | 0.409 | 0.998 | n.s. |
| 1 to 4 - 6 to 4 | 2.55 | 9.80 | 0.26 | 0.795 | 1.000 | n.s. |
| 1 to 4 - Cardinality4 | 4.85 | 11.49 | 0.42 | 0.673 | 1.000 | n.s. |
| 2 to 4 - 3 to 4 | -2.45 | 10.27 | -0.24 | 0.812 | 1.000 | n.s. |
| 2 to 4 - 5 to 4 | -10.20 | 10.07 | -1.01 | 0.311 | 0.992 | n.s. |
| 2 to 4 - 6 to 4 | 0.50 | 10.06 | 0.05 | 0.960 | 1.000 | n.s. |
| 2 to 4 - Cardinality4 | 2.80 | 11.81 | 0.24 | 0.813 | 1.000 | n.s. |
| 3 to 4 - 5 to 4 | -7.75 | 10.24 | -0.76 | 0.449 | 0.999 | n.s. |
| 3 to 4 - 6 to 4 | 2.95 | 10.18 | 0.29 | 0.772 | 1.000 | n.s. |
| 3 to 4 - Cardinality4 | 5.25 | 11.80 | 0.44 | 0.656 | 1.000 | n.s. |
| 5 to 4 - 6 to 4 | 10.70 | 9.93 | 1.08 | 0.281 | 0.990 | n.s. |
| 5 to 4 - Cardinality4 | 13.00 | 11.54 | 1.13 | 0.260 | 0.989 | n.s. |
| 6 to 4 - Cardinality4 | 2.30 | 11.31 | 0.20 | 0.839 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.66, *p* = 0.652, η²_G = 0.059
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.13 | 9 | = 0.965 | 0.05 [-0.47, 0.56] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 0.13 | 9 | = 0.965 | 0.06 [-0.47, 0.64] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -1.01 | 9 | = 0.685 | -0.57 [-0.71, 0.29] | medium | n.s. |
| 1 to 4 vs 6 to 4 | -1.07 | 9 | = 0.685 | -0.48 [-0.44, 0.55] | small | n.s. |
| 1 to 4 vs Cardinality4 | -0.22 | 9 | = 0.965 | -0.12 [-0.66, 0.68] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 0.02 | 9 | = 0.983 | 0.01 [-0.58, 0.53] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.95 | 9 | = 0.685 | -0.54 [-0.70, 0.33] | medium | n.s. |
| 2 to 4 vs 6 to 4 | -1.14 | 9 | = 0.685 | -0.46 [-0.47, 0.52] | small | n.s. |
| 2 to 4 vs Cardinality4 | -0.30 | 9 | = 0.965 | -0.14 [-0.71, 0.63] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -1.31 | 9 | = 0.685 | -0.60 [-0.79, 0.34] | medium | n.s. |
| 3 to 4 vs 6 to 4 | -1.27 | 9 | = 0.685 | -0.51 [-0.62, 0.49] | medium | n.s. |
| 3 to 4 vs Cardinality4 | -0.47 | 9 | = 0.965 | -0.17 [-0.86, 0.49] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 0.15 | 9 | = 0.965 | 0.07 [-0.30, 0.75] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | 1.19 | 9 | = 0.685 | 0.43 [-0.28, 1.12] | small | n.s. |
| 6 to 4 vs Cardinality4 | 1.14 | 9 | = 0.685 | 0.35 [-0.36, 1.02] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 441.78, BIC = 465.49
- **2 to 4 vs 1 to 4**: *β* = 0.68, *SE* = 0.530, *z* = 1.286, *p* = 0.198
- **3 to 4 vs 1 to 4**: *β* = -0.01, *SE* = 0.542, *z* = -0.014, *p* = 0.989
- **5 to 4 vs 1 to 4**: *β* = 0.41, *SE* = 0.522, *z* = 0.791, *p* = 0.429
- **6 to 4 vs 1 to 4**: *β* = 0.28, *SE* = 0.520, *z* = 0.529, *p* = 0.597
- **Cardinality4 vs 1 to 4**: *β* = -0.20, *SE* = 0.617, *z* = -0.328, *p* = 0.743
- **SNR**: *β* = 0.55, *SE* = 0.063, *z* = 8.765, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.68 | 0.53 | -1.29 | 0.198 | 0.955 | n.s. |
| 1 to 4 - 3 to 4 | 0.01 | 0.54 | 0.01 | 0.989 | 0.998 | n.s. |
| 1 to 4 - 5 to 4 | -0.41 | 0.52 | -0.79 | 0.429 | 0.998 | n.s. |
| 1 to 4 - 6 to 4 | -0.27 | 0.52 | -0.53 | 0.597 | 0.998 | n.s. |
| 1 to 4 - Cardinality4 | 0.20 | 0.62 | 0.33 | 0.743 | 0.998 | n.s. |
| 2 to 4 - 3 to 4 | 0.69 | 0.55 | 1.25 | 0.210 | 0.955 | n.s. |
| 2 to 4 - 5 to 4 | 0.27 | 0.54 | 0.50 | 0.615 | 0.998 | n.s. |
| 2 to 4 - 6 to 4 | 0.41 | 0.53 | 0.76 | 0.446 | 0.998 | n.s. |
| 2 to 4 - Cardinality4 | 0.88 | 0.64 | 1.39 | 0.166 | 0.934 | n.s. |
| 3 to 4 - 5 to 4 | -0.42 | 0.55 | -0.77 | 0.442 | 0.998 | n.s. |
| 3 to 4 - 6 to 4 | -0.28 | 0.55 | -0.52 | 0.604 | 0.998 | n.s. |
| 3 to 4 - Cardinality4 | 0.19 | 0.63 | 0.31 | 0.756 | 0.998 | n.s. |
| 5 to 4 - 6 to 4 | 0.14 | 0.53 | 0.26 | 0.794 | 0.998 | n.s. |
| 5 to 4 - Cardinality4 | 0.61 | 0.62 | 0.99 | 0.321 | 0.990 | n.s. |
| 6 to 4 - Cardinality4 | 0.48 | 0.61 | 0.79 | 0.432 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.90, *p* = 0.113, η²_G = 0.076
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.11 | 9 | = 0.492 | -0.26 [-0.85, 0.20] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.40 | 9 | = 0.870 | 0.13 [-0.52, 0.59] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | 0.46 | 9 | = 0.870 | 0.12 [-0.61, 0.39] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.82 | 9 | = 0.651 | 0.20 [-0.39, 0.61] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | 1.78 | 9 | = 0.297 | 0.63 [-0.18, 1.25] | medium | n.s. |
| 2 to 4 vs 3 to 4 | 1.17 | 9 | = 0.492 | 0.41 [-0.24, 0.89] | small | n.s. |
| 2 to 4 vs 5 to 4 | 1.72 | 9 | = 0.297 | 0.38 [-0.22, 0.83] | small | n.s. |
| 2 to 4 vs 6 to 4 | 1.75 | 9 | = 0.297 | 0.51 [-0.12, 0.92] | medium | n.s. |
| 2 to 4 vs Cardinality4 | 3.46 | 9 | = 0.107 | 0.92 [0.14, 1.76] | large | n.s. |
| 3 to 4 vs 5 to 4 | -0.01 | 9 | = 0.994 | -0.00 [-0.61, 0.50] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 0.16 | 9 | = 0.938 | 0.07 [-0.42, 0.70] | negligible | n.s. |
| 3 to 4 vs Cardinality4 | 1.17 | 9 | = 0.492 | 0.55 [-0.31, 1.08] | medium | n.s. |
| 5 to 4 vs 6 to 4 | 0.20 | 9 | = 0.938 | 0.06 [-0.33, 0.70] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | 1.76 | 9 | = 0.297 | 0.49 [-0.15, 1.30] | small | n.s. |
| 6 to 4 vs Cardinality4 | 2.45 | 9 | = 0.275 | 0.54 [0.03, 1.57] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.097)
**P1 amplitude:** Significant main effect of condition (*p* = 0.036). Post-hoc tests revealed:
  - 3 to 4 showed smaller amplitude than 6 to 4 (*d* = -0.60)

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
