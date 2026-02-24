# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:25:29

---

## 1. Analysis Overview

**Total Measurements:** 672
**Number of Subjects:** 24
**Number of Conditions:** 7

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
| Cardinality (no change) | 24 | 107.17 ms | 8.98 | 1.83 | [92.00, 116.00] |
| Decrease by 1 | 24 | 105.33 ms | 8.64 | 1.76 | [92.00, 116.00] |
| Decrease by 2 | 24 | 107.50 ms | 8.37 | 1.71 | [92.00, 116.00] |
| Decrease by 3 | 24 | 103.67 ms | 9.28 | 1.89 | [92.00, 116.00] |
| Increase by 1 | 24 | 101.67 ms | 9.50 | 1.94 | [92.00, 116.00] |
| Increase by 2 | 24 | 102.33 ms | 8.82 | 1.80 | [92.00, 116.00] |
| Increase by 3 | 24 | 102.17 ms | 8.50 | 1.74 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -1.28 µV | 1.38 | 0.28 | [-4.83, 0.55] |
| Decrease by 1 | 24 | -0.98 µV | 1.52 | 0.31 | [-5.36, 1.17] |
| Decrease by 2 | 24 | -1.38 µV | 1.29 | 0.26 | [-4.58, 2.04] |
| Decrease by 3 | 24 | -1.72 µV | 1.87 | 0.38 | [-6.67, 1.69] |
| Increase by 1 | 24 | -1.00 µV | 1.01 | 0.21 | [-3.28, 0.46] |
| Increase by 2 | 24 | -0.94 µV | 1.27 | 0.26 | [-4.17, 0.92] |
| Increase by 3 | 24 | -0.97 µV | 1.35 | 0.27 | [-3.87, 1.99] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 175.83 ms | 17.11 | 3.49 | [144.00, 208.00] |
| Decrease by 1 | 24 | 178.00 ms | 15.83 | 3.23 | [144.00, 208.00] |
| Decrease by 2 | 24 | 177.50 ms | 14.82 | 3.02 | [144.00, 208.00] |
| Decrease by 3 | 24 | 177.67 ms | 14.59 | 2.98 | [156.00, 208.00] |
| Increase by 1 | 24 | 171.33 ms | 19.73 | 4.03 | [144.00, 208.00] |
| Increase by 2 | 24 | 168.50 ms | 19.46 | 3.97 | [144.00, 208.00] |
| Increase by 3 | 24 | 171.00 ms | 19.53 | 3.99 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -4.62 µV | 2.14 | 0.44 | [-9.57, -0.60] |
| Decrease by 1 | 24 | -4.85 µV | 2.02 | 0.41 | [-9.17, -1.44] |
| Decrease by 2 | 24 | -4.95 µV | 2.01 | 0.41 | [-9.37, -1.43] |
| Decrease by 3 | 24 | -5.07 µV | 1.98 | 0.40 | [-8.57, -1.48] |
| Increase by 1 | 24 | -5.00 µV | 2.17 | 0.44 | [-9.36, -1.04] |
| Increase by 2 | 24 | -5.39 µV | 2.36 | 0.48 | [-10.65, -0.86] |
| Increase by 3 | 24 | -6.05 µV | 2.46 | 0.50 | [-12.86, -1.94] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 106.00 ms | 10.55 | 2.15 | [92.00, 116.00] |
| Decrease by 1 | 24 | 105.83 ms | 10.35 | 2.11 | [92.00, 116.00] |
| Decrease by 2 | 24 | 110.33 ms | 6.87 | 1.40 | [92.00, 116.00] |
| Decrease by 3 | 24 | 108.17 ms | 9.10 | 1.86 | [92.00, 116.00] |
| Increase by 1 | 24 | 103.83 ms | 9.76 | 1.99 | [92.00, 116.00] |
| Increase by 2 | 24 | 103.17 ms | 9.14 | 1.86 | [92.00, 116.00] |
| Increase by 3 | 24 | 100.83 ms | 9.36 | 1.91 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.27 µV | 1.86 | 0.38 | [-1.29, 5.73] |
| Decrease by 1 | 24 | 1.02 µV | 2.02 | 0.41 | [-1.44, 5.89] |
| Decrease by 2 | 24 | 1.47 µV | 1.79 | 0.37 | [-2.14, 5.51] |
| Decrease by 3 | 24 | 1.93 µV | 2.07 | 0.42 | [-1.76, 8.21] |
| Increase by 1 | 24 | 1.10 µV | 1.42 | 0.29 | [-1.10, 4.07] |
| Increase by 2 | 24 | 1.05 µV | 1.60 | 0.33 | [-1.49, 4.70] |
| Increase by 3 | 24 | 1.21 µV | 1.68 | 0.34 | [-0.96, 5.72] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 463.17 ms | 25.49 | 5.20 | [416.00, 516.00] |
| Decrease by 1 | 24 | 486.67 ms | 36.46 | 7.44 | [416.00, 528.00] |
| Decrease by 2 | 24 | 468.67 ms | 29.10 | 5.94 | [416.00, 532.00] |
| Decrease by 3 | 24 | 477.17 ms | 33.25 | 6.79 | [416.00, 532.00] |
| Increase by 1 | 24 | 479.67 ms | 37.15 | 7.58 | [416.00, 532.00] |
| Increase by 2 | 24 | 483.67 ms | 32.06 | 6.54 | [428.00, 532.00] |
| Increase by 3 | 24 | 474.00 ms | 38.69 | 7.90 | [416.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.16 µV | 2.72 | 0.56 | [-4.85, 5.95] |
| Decrease by 1 | 24 | 3.43 µV | 3.05 | 0.62 | [-2.65, 8.87] |
| Decrease by 2 | 24 | 3.56 µV | 2.95 | 0.60 | [-1.65, 8.53] |
| Decrease by 3 | 24 | 4.20 µV | 3.52 | 0.72 | [-1.22, 12.38] |
| Increase by 1 | 24 | 2.40 µV | 3.33 | 0.68 | [-3.42, 8.79] |
| Increase by 2 | 24 | 3.77 µV | 3.39 | 0.69 | [-2.45, 9.72] |
| Increase by 3 | 24 | 3.77 µV | 2.65 | 0.54 | [0.31, 9.96] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1173.97, BIC = 1205.21
- **Decrease by 1 vs Cardinality (no change)**: *β* = -1.73, *SE* = 1.914, *z* = -0.903, *p* = 0.367
- **Decrease by 2 vs Cardinality (no change)**: *β* = 0.44, *SE* = 1.914, *z* = 0.228, *p* = 0.820
- **Decrease by 3 vs Cardinality (no change)**: *β* = -3.85, *SE* = 1.922, *z* = -2.000, *p* = 0.045
- **Increase by 1 vs Cardinality (no change)**: *β* = -5.33, *SE* = 1.916, *z* = -2.781, *p* = 0.005
- **Increase by 2 vs Cardinality (no change)**: *β* = -4.45, *SE* = 1.925, *z* = -2.311, *p* = 0.021
- **Increase by 3 vs Cardinality (no change)**: *β* = -4.73, *SE* = 1.919, *z* = -2.464, *p* = 0.014
- **SNR**: *β* = 0.58, *SE* = 0.318, *z* = 1.830, *p* = 0.067

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 1.73 | 1.91 | 0.90 | 0.367 | 0.974 | n.s. |
| Cardinality (no change) - Decrease by 2 | -0.44 | 1.91 | -0.23 | 0.820 | 0.998 | n.s. |
| Cardinality (no change) - Decrease by 3 | 3.85 | 1.92 | 2.00 | 0.045 | 0.479 | n.s. |
| Cardinality (no change) - Increase by 1 | 5.33 | 1.92 | 2.78 | 0.005 | 0.103 | n.s. |
| Cardinality (no change) - Increase by 2 | 4.45 | 1.92 | 2.31 | 0.021 | 0.286 | n.s. |
| Cardinality (no change) - Increase by 3 | 4.73 | 1.92 | 2.46 | 0.014 | 0.210 | n.s. |
| Decrease by 1 - Decrease by 2 | -2.16 | 1.91 | -1.13 | 0.258 | 0.949 | n.s. |
| Decrease by 1 - Decrease by 3 | 2.12 | 1.93 | 1.10 | 0.272 | 0.949 | n.s. |
| Decrease by 1 - Increase by 1 | 3.60 | 1.91 | 1.88 | 0.060 | 0.553 | n.s. |
| Decrease by 1 - Increase by 2 | 2.72 | 1.92 | 1.42 | 0.156 | 0.846 | n.s. |
| Decrease by 1 - Increase by 3 | 3.00 | 1.92 | 1.57 | 0.117 | 0.776 | n.s. |
| Decrease by 2 - Decrease by 3 | 4.28 | 1.93 | 2.22 | 0.026 | 0.331 | n.s. |
| Decrease by 2 - Increase by 1 | 5.76 | 1.91 | 3.01 | 0.003 | 0.053 | n.s. |
| Decrease by 2 - Increase by 2 | 4.88 | 1.92 | 2.54 | 0.011 | 0.180 | n.s. |
| Decrease by 2 - Increase by 3 | 5.16 | 1.92 | 2.70 | 0.007 | 0.125 | n.s. |
| Decrease by 3 - Increase by 1 | 1.48 | 1.93 | 0.77 | 0.444 | 0.984 | n.s. |
| Decrease by 3 - Increase by 2 | 0.60 | 1.95 | 0.31 | 0.758 | 0.998 | n.s. |
| Decrease by 3 - Increase by 3 | 0.88 | 1.94 | 0.45 | 0.650 | 0.998 | n.s. |
| Increase by 1 - Increase by 2 | -0.88 | 1.92 | -0.46 | 0.647 | 0.998 | n.s. |
| Increase by 1 - Increase by 3 | -0.60 | 1.91 | -0.31 | 0.755 | 0.998 | n.s. |
| Increase by 2 - Increase by 3 | 0.28 | 1.91 | 0.15 | 0.883 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.03, *p* = 0.008, η²_G = 0.063
- Greenhouse-Geisser corrected: *p* = 0.020 (ε = 0.683)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 1.49 | 23 | = 0.263 | 0.21 [-0.13, 0.74] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.17 | 23 | = 0.907 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.49 | 23 | = 0.263 | 0.38 [-0.13, 0.74] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 3.06 | 23 | = 0.039 | 0.59 [0.16, 1.09] | medium | * |
| Cardinality (no change) vs Increase by 2 | 2.47 | 23 | = 0.089 | 0.54 [0.06, 0.95] | medium | n.s. |
| Cardinality (no change) vs Increase by 3 | 3.40 | 23 | = 0.039 | 0.57 [0.22, 1.16] | medium | * |
| Decrease by 1 vs Decrease by 2 | -1.18 | 23 | = 0.403 | -0.25 [-0.67, 0.19] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.65 | 23 | = 0.677 | 0.19 [-0.29, 0.56] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 2.06 | 23 | = 0.135 | 0.40 [-0.02, 0.86] | small | n.s. |
| Decrease by 1 vs Increase by 2 | 1.52 | 23 | = 0.263 | 0.34 [-0.12, 0.74] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 2.26 | 23 | = 0.102 | 0.37 [0.02, 0.90] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | 1.80 | 23 | = 0.199 | 0.43 [-0.07, 0.80] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 3.10 | 23 | = 0.039 | 0.65 [0.17, 1.10] | medium | * |
| Decrease by 2 vs Increase by 2 | 2.26 | 23 | = 0.102 | 0.60 [0.02, 0.90] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 2.87 | 23 | = 0.046 | 0.63 [0.13, 1.04] | medium | * |
| Decrease by 3 vs Increase by 1 | 0.80 | 23 | = 0.645 | 0.21 [-0.26, 0.59] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 0.61 | 23 | = 0.677 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 0.61 | 23 | = 0.677 | 0.17 [-0.30, 0.55] | negligible | n.s. |
| Increase by 1 vs Increase by 2 | -0.31 | 23 | = 0.836 | -0.07 [-0.49, 0.36] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.40 | 23 | = 0.811 | -0.06 [-0.50, 0.34] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.10 | 23 | = 0.920 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 514.79, BIC = 546.03
- **Decrease by 1 vs Cardinality (no change)**: *β* = 0.26, *SE* = 0.264, *z* = 1.001, *p* = 0.317
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.13, *SE* = 0.264, *z* = -0.504, *p* = 0.614
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.34, *SE* = 0.265, *z* = -1.293, *p* = 0.196
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.23, *SE* = 0.264, *z* = 0.872, *p* = 0.383
- **Increase by 2 vs Cardinality (no change)**: *β* = 0.23, *SE* = 0.266, *z* = 0.849, *p* = 0.396
- **Increase by 3 vs Cardinality (no change)**: *β* = 0.23, *SE* = 0.265, *z* = 0.866, *p* = 0.387
- **SNR**: *β* = -0.17, *SE* = 0.045, *z* = -3.717, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -0.26 | 0.26 | -1.00 | 0.317 | 0.990 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.13 | 0.26 | 0.50 | 0.614 | 0.999 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.34 | 0.27 | 1.29 | 0.196 | 0.948 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.23 | 0.26 | -0.87 | 0.383 | 0.995 | n.s. |
| Cardinality (no change) - Increase by 2 | -0.23 | 0.27 | -0.85 | 0.396 | 0.995 | n.s. |
| Cardinality (no change) - Increase by 3 | -0.23 | 0.26 | -0.87 | 0.387 | 0.995 | n.s. |
| Decrease by 1 - Decrease by 2 | 0.40 | 0.26 | 1.51 | 0.132 | 0.910 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.61 | 0.27 | 2.28 | 0.023 | 0.380 | n.s. |
| Decrease by 1 - Increase by 1 | 0.03 | 0.26 | 0.13 | 0.898 | 1.000 | n.s. |
| Decrease by 1 - Increase by 2 | 0.04 | 0.26 | 0.15 | 0.883 | 1.000 | n.s. |
| Decrease by 1 - Increase by 3 | 0.04 | 0.26 | 0.13 | 0.894 | 1.000 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.21 | 0.27 | 0.79 | 0.430 | 0.995 | n.s. |
| Decrease by 2 - Increase by 1 | -0.36 | 0.26 | -1.38 | 0.169 | 0.948 | n.s. |
| Decrease by 2 - Increase by 2 | -0.36 | 0.26 | -1.35 | 0.176 | 0.948 | n.s. |
| Decrease by 2 - Increase by 3 | -0.36 | 0.26 | -1.37 | 0.170 | 0.948 | n.s. |
| Decrease by 3 - Increase by 1 | -0.57 | 0.27 | -2.15 | 0.032 | 0.475 | n.s. |
| Decrease by 3 - Increase by 2 | -0.57 | 0.27 | -2.11 | 0.035 | 0.476 | n.s. |
| Decrease by 3 - Increase by 3 | -0.57 | 0.27 | -2.13 | 0.033 | 0.475 | n.s. |
| Increase by 1 - Increase by 2 | 0.01 | 0.26 | 0.02 | 0.985 | 1.000 | n.s. |
| Increase by 1 - Increase by 3 | 0.00 | 0.26 | 0.00 | 0.996 | 1.000 | n.s. |
| Increase by 2 - Increase by 3 | -0.00 | 0.26 | -0.01 | 0.989 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.24, *p* = 0.043, η²_G = 0.038
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.10 | 23 | = 0.487 | -0.20 [-0.65, 0.20] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | 0.47 | 23 | = 0.901 | 0.08 [-0.33, 0.52] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.50 | 23 | = 0.367 | 0.27 [-0.13, 0.74] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | -1.30 | 23 | = 0.416 | -0.23 [-0.69, 0.17] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | -1.59 | 23 | = 0.367 | -0.25 [-0.76, 0.11] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | -1.04 | 23 | = 0.487 | -0.23 [-0.64, 0.22] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 1.46 | 23 | = 0.367 | 0.28 [-0.13, 0.73] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | 2.55 | 23 | = 0.144 | 0.43 [0.07, 0.97] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 0.05 | 23 | = 0.963 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | -0.19 | 23 | = 0.963 | -0.03 [-0.46, 0.38] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | -0.05 | 23 | = 0.963 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 1.01 | 23 | = 0.487 | 0.21 [-0.22, 0.63] | small | n.s. |
| Decrease by 2 vs Increase by 1 | -1.52 | 23 | = 0.367 | -0.33 [-0.74, 0.12] | small | n.s. |
| Decrease by 2 vs Increase by 2 | -1.61 | 23 | = 0.367 | -0.34 [-0.76, 0.10] | small | n.s. |
| Decrease by 2 vs Increase by 3 | -1.27 | 23 | = 0.416 | -0.31 [-0.69, 0.17] | small | n.s. |
| Decrease by 3 vs Increase by 1 | -2.58 | 23 | = 0.144 | -0.48 [-0.98, -0.08] | small | n.s. |
| Decrease by 3 vs Increase by 2 | -2.35 | 23 | = 0.144 | -0.49 [-0.93, -0.03] | small | n.s. |
| Decrease by 3 vs Increase by 3 | -2.41 | 23 | = 0.144 | -0.46 [-0.94, -0.05] | small | n.s. |
| Increase by 1 vs Increase by 2 | -0.24 | 23 | = 0.963 | -0.05 [-0.47, 0.37] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.10 | 23 | = 0.963 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.09 | 23 | = 0.963 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1339.99, BIC = 1371.23
- **Decrease by 1 vs Cardinality (no change)**: *β* = 2.31, *SE* = 2.966, *z* = 0.777, *p* = 0.437
- **Decrease by 2 vs Cardinality (no change)**: *β* = 1.80, *SE* = 2.965, *z* = 0.607, *p* = 0.544
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.00, *SE* = 2.972, *z* = 0.673, *p* = 0.501
- **Increase by 1 vs Cardinality (no change)**: *β* = -4.11, *SE* = 3.060, *z* = -1.342, *p* = 0.180
- **Increase by 2 vs Cardinality (no change)**: *β* = -7.16, *SE* = 2.975, *z* = -2.405, *p* = 0.016
- **Increase by 3 vs Cardinality (no change)**: *β* = -4.69, *SE* = 2.967, *z* = -1.580, *p* = 0.114
- **SNR**: *β* = -0.11, *SE* = 0.221, *z* = -0.487, *p* = 0.626

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -2.30 | 2.97 | -0.78 | 0.437 | 0.984 | n.s. |
| Cardinality (no change) - Decrease by 2 | -1.80 | 2.96 | -0.61 | 0.544 | 0.985 | n.s. |
| Cardinality (no change) - Decrease by 3 | -2.00 | 2.97 | -0.67 | 0.501 | 0.985 | n.s. |
| Cardinality (no change) - Increase by 1 | 4.11 | 3.06 | 1.34 | 0.180 | 0.862 | n.s. |
| Cardinality (no change) - Increase by 2 | 7.16 | 2.97 | 2.41 | 0.016 | 0.254 | n.s. |
| Cardinality (no change) - Increase by 3 | 4.69 | 2.97 | 1.58 | 0.114 | 0.736 | n.s. |
| Decrease by 1 - Decrease by 2 | 0.50 | 2.95 | 0.17 | 0.864 | 0.999 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.31 | 2.95 | 0.10 | 0.918 | 0.999 | n.s. |
| Decrease by 1 - Increase by 1 | 6.41 | 3.00 | 2.14 | 0.032 | 0.370 | n.s. |
| Decrease by 1 - Increase by 2 | 9.46 | 2.95 | 3.20 | 0.001 | 0.028 | * |
| Decrease by 1 - Increase by 3 | 6.99 | 2.95 | 2.37 | 0.018 | 0.264 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.20 | 2.95 | -0.07 | 0.946 | 0.999 | n.s. |
| Decrease by 2 - Increase by 1 | 5.91 | 3.00 | 1.97 | 0.049 | 0.452 | n.s. |
| Decrease by 2 - Increase by 2 | 8.96 | 2.95 | 3.03 | 0.002 | 0.045 | * |
| Decrease by 2 - Increase by 3 | 6.49 | 2.95 | 2.20 | 0.028 | 0.347 | n.s. |
| Decrease by 3 - Increase by 1 | 6.11 | 2.99 | 2.04 | 0.041 | 0.420 | n.s. |
| Decrease by 3 - Increase by 2 | 9.15 | 2.95 | 3.10 | 0.002 | 0.038 | * |
| Decrease by 3 - Increase by 3 | 6.69 | 2.95 | 2.26 | 0.024 | 0.317 | n.s. |
| Increase by 1 - Increase by 2 | 3.05 | 2.98 | 1.02 | 0.307 | 0.963 | n.s. |
| Increase by 1 - Increase by 3 | 0.58 | 3.00 | 0.19 | 0.846 | 0.999 | n.s. |
| Increase by 2 - Increase by 3 | -2.47 | 2.95 | -0.84 | 0.403 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.34, *p* = 0.004, η²_G = 0.043
- Greenhouse-Geisser corrected: *p* = 0.022 (ε = 0.526)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.20 | 23 | = 0.338 | -0.13 [-0.67, 0.18] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.70 | 23 | = 0.642 | -0.10 [-0.57, 0.28] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.56 | 23 | = 0.721 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.53 | 23 | = 0.242 | 0.24 [-0.12, 0.75] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.37 | 23 | = 0.141 | 0.40 [0.04, 0.93] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 1.67 | 23 | = 0.236 | 0.26 [-0.09, 0.77] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 0.30 | 23 | = 0.893 | 0.03 [-0.36, 0.48] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.11 | 23 | = 0.953 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 2.03 | 23 | = 0.163 | 0.37 [-0.03, 0.85] | small | n.s. |
| Decrease by 1 vs Increase by 2 | 2.86 | 23 | = 0.136 | 0.54 [0.13, 1.04] | medium | n.s. |
| Decrease by 1 vs Increase by 3 | 2.16 | 23 | = 0.163 | 0.39 [-0.00, 0.88] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.06 | 23 | = 0.953 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 1.61 | 23 | = 0.236 | 0.35 [-0.10, 0.76] | small | n.s. |
| Decrease by 2 vs Increase by 2 | 2.66 | 23 | = 0.136 | 0.52 [0.09, 1.00] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 1.82 | 23 | = 0.214 | 0.37 [-0.06, 0.81] | small | n.s. |
| Decrease by 3 vs Increase by 1 | 1.60 | 23 | = 0.236 | 0.37 [-0.11, 0.76] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 2.51 | 23 | = 0.136 | 0.53 [0.06, 0.96] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | 2.09 | 23 | = 0.163 | 0.39 [-0.01, 0.87] | small | n.s. |
| Increase by 1 vs Increase by 2 | 1.24 | 23 | = 0.338 | 0.14 [-0.18, 0.68] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.14 | 23 | = 0.953 | 0.02 [-0.39, 0.45] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.34 | 23 | = 0.311 | -0.13 [-0.70, 0.16] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 569.83, BIC = 601.07
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.08, *SE* = 0.292, *z* = -0.282, *p* = 0.778
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.19, *SE* = 0.292, *z* = -0.636, *p* = 0.525
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.27, *SE* = 0.292, *z* = -0.929, *p* = 0.353
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.02, *SE* = 0.301, *z* = 0.076, *p* = 0.939
- **Increase by 2 vs Cardinality (no change)**: *β* = -0.59, *SE* = 0.293, *z* = -2.008, *p* = 0.045
- **Increase by 3 vs Cardinality (no change)**: *β* = -1.27, *SE* = 0.292, *z* = -4.358, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.022, *z* = -4.993, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.08 | 0.29 | 0.28 | 0.778 | 0.998 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.19 | 0.29 | 0.64 | 0.525 | 0.995 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.27 | 0.29 | 0.93 | 0.353 | 0.980 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.02 | 0.30 | -0.08 | 0.939 | 0.998 | n.s. |
| Cardinality (no change) - Increase by 2 | 0.59 | 0.29 | 2.01 | 0.045 | 0.472 | n.s. |
| Cardinality (no change) - Increase by 3 | 1.27 | 0.29 | 4.36 | < .001 | < .001 | *** |
| Decrease by 1 - Decrease by 2 | 0.10 | 0.29 | 0.36 | 0.722 | 0.998 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.19 | 0.29 | 0.65 | 0.515 | 0.995 | n.s. |
| Decrease by 1 - Increase by 1 | -0.11 | 0.30 | -0.36 | 0.722 | 0.998 | n.s. |
| Decrease by 1 - Increase by 2 | 0.51 | 0.29 | 1.74 | 0.082 | 0.670 | n.s. |
| Decrease by 1 - Increase by 3 | 1.19 | 0.29 | 4.10 | < .001 | < .001 | *** |
| Decrease by 2 - Decrease by 3 | 0.09 | 0.29 | 0.30 | 0.767 | 0.998 | n.s. |
| Decrease by 2 - Increase by 1 | -0.21 | 0.30 | -0.71 | 0.480 | 0.995 | n.s. |
| Decrease by 2 - Increase by 2 | 0.40 | 0.29 | 1.38 | 0.166 | 0.887 | n.s. |
| Decrease by 2 - Increase by 3 | 1.09 | 0.29 | 3.74 | < .001 | 0.003 | ** |
| Decrease by 3 - Increase by 1 | -0.29 | 0.29 | -1.00 | 0.317 | 0.978 | n.s. |
| Decrease by 3 - Increase by 2 | 0.32 | 0.29 | 1.09 | 0.276 | 0.971 | n.s. |
| Decrease by 3 - Increase by 3 | 1.00 | 0.29 | 3.45 | < .001 | 0.010 | ** |
| Increase by 1 - Increase by 2 | 0.61 | 0.29 | 2.08 | 0.038 | 0.437 | n.s. |
| Increase by 1 - Increase by 3 | 1.30 | 0.29 | 4.39 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.68 | 0.29 | 2.36 | 0.018 | 0.257 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.34, *p* < .001, η²_G = 0.040
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.83 | 23 | = 0.584 | 0.11 [-0.26, 0.59] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | 0.99 | 23 | = 0.536 | 0.16 [-0.22, 0.63] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.40 | 23 | = 0.368 | 0.21 [-0.15, 0.72] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.50 | 23 | = 0.341 | 0.18 [-0.13, 0.74] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 | 3.06 | 23 | = 0.029 | 0.34 [0.16, 1.09] | small | * |
| Cardinality (no change) vs Increase by 3 | 4.60 | 23 | = 0.003 | 0.62 [0.43, 1.45] | medium | ** |
| Decrease by 1 vs Decrease by 2 | 0.36 | 23 | = 0.798 | 0.05 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.74 | 23 | = 0.615 | 0.11 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 0.57 | 23 | = 0.713 | 0.07 [-0.31, 0.54] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 2.02 | 23 | = 0.145 | 0.25 [-0.03, 0.85] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 3.89 | 23 | = 0.008 | 0.53 [0.31, 1.28] | medium | ** |
| Decrease by 2 vs Decrease by 3 | 0.46 | 23 | = 0.755 | 0.06 [-0.33, 0.52] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 0.18 | 23 | = 0.861 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | 1.15 | 23 | = 0.457 | 0.20 [-0.19, 0.66] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 2.73 | 23 | = 0.050 | 0.49 [0.10, 1.01] | small | n.s. |
| Decrease by 3 vs Increase by 1 | -0.18 | 23 | = 0.861 | -0.03 [-0.46, 0.38] | negligible | n.s. |
| Decrease by 3 vs Increase by 2 | 0.87 | 23 | = 0.584 | 0.15 [-0.25, 0.60] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 2.32 | 23 | = 0.103 | 0.44 [0.03, 0.92] | small | n.s. |
| Increase by 1 vs Increase by 2 | 1.33 | 23 | = 0.373 | 0.17 [-0.16, 0.70] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 3.29 | 23 | = 0.022 | 0.45 [0.20, 1.14] | small | * |
| Increase by 2 vs Increase by 3 | 2.24 | 23 | = 0.105 | 0.27 [0.01, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1168.27, BIC = 1199.51
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.04, *SE* = 1.832, *z* = -0.024, *p* = 0.981
- **Decrease by 2 vs Cardinality (no change)**: *β* = 4.51, *SE* = 1.835, *z* = 2.459, *p* = 0.014
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.39, *SE* = 1.838, *z* = 1.299, *p* = 0.194
- **Increase by 1 vs Cardinality (no change)**: *β* = -1.76, *SE* = 1.856, *z* = -0.949, *p* = 0.343
- **Increase by 2 vs Cardinality (no change)**: *β* = -2.44, *SE* = 1.855, *z* = -1.313, *p* = 0.189
- **Increase by 3 vs Cardinality (no change)**: *β* = -4.84, *SE* = 1.848, *z* = -2.617, *p* = 0.009
- **SNR**: *β* = 0.30, *SE* = 0.229, *z* = 1.306, *p* = 0.191

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.04 | 1.83 | 0.02 | 0.981 | 0.981 | n.s. |
| Cardinality (no change) - Decrease by 2 | -4.51 | 1.84 | -2.46 | 0.014 | 0.167 | n.s. |
| Cardinality (no change) - Decrease by 3 | -2.39 | 1.84 | -1.30 | 0.194 | 0.870 | n.s. |
| Cardinality (no change) - Increase by 1 | 1.76 | 1.86 | 0.95 | 0.343 | 0.870 | n.s. |
| Cardinality (no change) - Increase by 2 | 2.44 | 1.86 | 1.31 | 0.189 | 0.870 | n.s. |
| Cardinality (no change) - Increase by 3 | 4.84 | 1.85 | 2.62 | 0.009 | 0.136 | n.s. |
| Decrease by 1 - Decrease by 2 | -4.56 | 1.83 | -2.49 | 0.013 | 0.165 | n.s. |
| Decrease by 1 - Decrease by 3 | -2.43 | 1.83 | -1.33 | 0.184 | 0.870 | n.s. |
| Decrease by 1 - Increase by 1 | 1.72 | 1.84 | 0.93 | 0.352 | 0.870 | n.s. |
| Decrease by 1 - Increase by 2 | 2.39 | 1.84 | 1.30 | 0.194 | 0.870 | n.s. |
| Decrease by 1 - Increase by 3 | 4.79 | 1.84 | 2.61 | 0.009 | 0.136 | n.s. |
| Decrease by 2 - Decrease by 3 | 2.13 | 1.83 | 1.16 | 0.246 | 0.870 | n.s. |
| Decrease by 2 - Increase by 1 | 6.27 | 1.84 | 3.41 | < .001 | 0.012 | * |
| Decrease by 2 - Increase by 2 | 6.95 | 1.84 | 3.78 | < .001 | 0.003 | ** |
| Decrease by 2 - Increase by 3 | 9.35 | 1.83 | 5.10 | < .001 | < .001 | *** |
| Decrease by 3 - Increase by 1 | 4.15 | 1.84 | 2.26 | 0.024 | 0.251 | n.s. |
| Decrease by 3 - Increase by 2 | 4.82 | 1.84 | 2.63 | 0.009 | 0.136 | n.s. |
| Decrease by 3 - Increase by 3 | 7.22 | 1.83 | 3.94 | < .001 | 0.002 | ** |
| Increase by 1 - Increase by 2 | 0.67 | 1.83 | 0.37 | 0.713 | 0.917 | n.s. |
| Increase by 1 - Increase by 3 | 3.07 | 1.83 | 1.68 | 0.093 | 0.659 | n.s. |
| Increase by 2 - Increase by 3 | 2.40 | 1.83 | 1.31 | 0.190 | 0.870 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.76, *p* < .001, η²_G = 0.094
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.15 | 23 | = 0.880 | 0.02 [-0.39, 0.45] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | -2.52 | 23 | = 0.057 | -0.49 [-0.96, -0.07] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | -1.08 | 23 | = 0.347 | -0.22 [-0.65, 0.21] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.08 | 23 | = 0.347 | 0.21 [-0.21, 0.65] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 1.90 | 23 | = 0.123 | 0.29 [-0.05, 0.83] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 2.78 | 23 | = 0.044 | 0.52 [0.11, 1.02] | medium | * |
| Decrease by 1 vs Decrease by 2 | -2.69 | 23 | = 0.046 | -0.51 [-1.00, -0.10] | medium | * |
| Decrease by 1 vs Decrease by 3 | -1.13 | 23 | = 0.347 | -0.24 [-0.66, 0.20] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 1.03 | 23 | = 0.347 | 0.20 [-0.22, 0.64] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 1.42 | 23 | = 0.253 | 0.27 [-0.14, 0.72] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 2.43 | 23 | = 0.062 | 0.51 [0.05, 0.94] | medium | n.s. |
| Decrease by 2 vs Decrease by 3 | 1.03 | 23 | = 0.347 | 0.27 [-0.22, 0.64] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 3.19 | 23 | = 0.022 | 0.77 [0.19, 1.12] | medium | * |
| Decrease by 2 vs Increase by 2 | 4.44 | 23 | = 0.002 | 0.89 [0.40, 1.41] | large | ** |
| Decrease by 2 vs Increase by 3 | 5.02 | 23 | < .001 | 1.16 [0.50, 1.55] | large | *** |
| Decrease by 3 vs Increase by 1 | 2.05 | 23 | = 0.109 | 0.46 [-0.02, 0.86] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 2.15 | 23 | = 0.099 | 0.55 [-0.00, 0.88] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | 3.60 | 23 | = 0.011 | 0.79 [0.26, 1.21] | medium | * |
| Increase by 1 vs Increase by 2 | 0.34 | 23 | = 0.774 | 0.07 [-0.35, 0.49] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.94 | 23 | = 0.123 | 0.31 [-0.04, 0.83] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.53 | 23 | = 0.224 | 0.25 [-0.12, 0.75] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 538.84, BIC = 570.08
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.19, *SE* = 0.271, *z* = -0.697, *p* = 0.486
- **Decrease by 2 vs Cardinality (no change)**: *β* = 0.29, *SE* = 0.271, *z* = 1.074, *p* = 0.283
- **Decrease by 3 vs Cardinality (no change)**: *β* = 0.76, *SE* = 0.272, *z* = 2.811, *p* = 0.005
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.03, *SE* = 0.275, *z* = 0.104, *p* = 0.917
- **Increase by 2 vs Cardinality (no change)**: *β* = -0.03, *SE* = 0.274, *z* = -0.098, *p* = 0.922
- **Increase by 3 vs Cardinality (no change)**: *β* = 0.10, *SE* = 0.273, *z* = 0.370, *p* = 0.711
- **SNR**: *β* = 0.15, *SE* = 0.035, *z* = 4.339, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.19 | 0.27 | 0.70 | 0.486 | 0.997 | n.s. |
| Cardinality (no change) - Decrease by 2 | -0.29 | 0.27 | -1.07 | 0.283 | 0.987 | n.s. |
| Cardinality (no change) - Decrease by 3 | -0.76 | 0.27 | -2.81 | 0.005 | 0.090 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.03 | 0.27 | -0.10 | 0.917 | 0.998 | n.s. |
| Cardinality (no change) - Increase by 2 | 0.03 | 0.27 | 0.10 | 0.922 | 0.998 | n.s. |
| Cardinality (no change) - Increase by 3 | -0.10 | 0.27 | -0.37 | 0.711 | 0.998 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.48 | 0.27 | -1.78 | 0.076 | 0.717 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.95 | 0.27 | -3.52 | < .001 | 0.009 | ** |
| Decrease by 1 - Increase by 1 | -0.22 | 0.27 | -0.80 | 0.425 | 0.996 | n.s. |
| Decrease by 1 - Increase by 2 | -0.16 | 0.27 | -0.59 | 0.552 | 0.997 | n.s. |
| Decrease by 1 - Increase by 3 | -0.29 | 0.27 | -1.07 | 0.286 | 0.987 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.47 | 0.27 | -1.75 | 0.081 | 0.718 | n.s. |
| Decrease by 2 - Increase by 1 | 0.26 | 0.27 | 0.97 | 0.333 | 0.988 | n.s. |
| Decrease by 2 - Increase by 2 | 0.32 | 0.27 | 1.17 | 0.241 | 0.979 | n.s. |
| Decrease by 2 - Increase by 3 | 0.19 | 0.27 | 0.70 | 0.483 | 0.997 | n.s. |
| Decrease by 3 - Increase by 1 | 0.74 | 0.27 | 2.71 | 0.007 | 0.115 | n.s. |
| Decrease by 3 - Increase by 2 | 0.79 | 0.27 | 2.91 | 0.004 | 0.069 | n.s. |
| Decrease by 3 - Increase by 3 | 0.66 | 0.27 | 2.45 | 0.014 | 0.219 | n.s. |
| Increase by 1 - Increase by 2 | 0.06 | 0.27 | 0.20 | 0.838 | 0.998 | n.s. |
| Increase by 1 - Increase by 3 | -0.07 | 0.27 | -0.27 | 0.788 | 0.998 | n.s. |
| Increase by 2 - Increase by 3 | -0.13 | 0.27 | -0.47 | 0.636 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.45, *p* = 0.028, η²_G = 0.028
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.78 | 23 | = 0.672 | 0.13 [-0.27, 0.58] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.78 | 23 | = 0.672 | -0.11 [-0.58, 0.27] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -1.94 | 23 | = 0.274 | -0.33 [-0.83, 0.04] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 0.57 | 23 | = 0.752 | 0.11 [-0.31, 0.54] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 | 0.84 | 23 | = 0.672 | 0.13 [-0.25, 0.60] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 | 0.23 | 23 | = 0.910 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| Decrease by 1 vs Decrease by 2 | -1.54 | 23 | = 0.397 | -0.24 [-0.75, 0.12] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -3.63 | 23 | = 0.029 | -0.44 [-1.22, -0.27] | small | * |
| Decrease by 1 vs Increase by 1 | -0.25 | 23 | = 0.910 | -0.04 [-0.47, 0.37] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | -0.10 | 23 | = 0.919 | -0.01 [-0.44, 0.40] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | -0.77 | 23 | = 0.672 | -0.10 [-0.58, 0.27] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.49 | 23 | = 0.397 | -0.23 [-0.74, 0.13] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 1.15 | 23 | = 0.611 | 0.23 [-0.19, 0.66] | small | n.s. |
| Decrease by 2 vs Increase by 2 | 1.53 | 23 | = 0.397 | 0.25 [-0.12, 0.74] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 0.78 | 23 | = 0.672 | 0.15 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | 2.51 | 23 | = 0.103 | 0.47 [0.06, 0.96] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 3.11 | 23 | = 0.052 | 0.48 [0.17, 1.10] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 2.84 | 23 | = 0.065 | 0.38 [0.12, 1.04] | small | n.s. |
| Increase by 1 vs Increase by 2 | 0.16 | 23 | = 0.915 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.42 | 23 | = 0.835 | -0.07 [-0.51, 0.34] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -0.70 | 23 | = 0.687 | -0.10 [-0.57, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1643.99, BIC = 1675.23
- **Decrease by 1 vs Cardinality (no change)**: *β* = 24.76, *SE* = 8.143, *z* = 3.041, *p* = 0.002
- **Decrease by 2 vs Cardinality (no change)**: *β* = 6.61, *SE* = 8.111, *z* = 0.814, *p* = 0.415
- **Decrease by 3 vs Cardinality (no change)**: *β* = 15.47, *SE* = 8.194, *z* = 1.889, *p* = 0.059
- **Increase by 1 vs Cardinality (no change)**: *β* = 17.91, *SE* = 8.177, *z* = 2.190, *p* = 0.029
- **Increase by 2 vs Cardinality (no change)**: *β* = 21.87, *SE* = 8.168, *z* = 2.677, *p* = 0.007
- **Increase by 3 vs Cardinality (no change)**: *β* = 11.41, *SE* = 8.034, *z* = 1.420, *p* = 0.155
- **SNR**: *β* = -0.43, *SE* = 0.511, *z* = -0.842, *p* = 0.400

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -24.76 | 8.14 | -3.04 | 0.002 | 0.048 | * |
| Cardinality (no change) - Decrease by 2 | -6.60 | 8.11 | -0.81 | 0.415 | 0.989 | n.s. |
| Cardinality (no change) - Decrease by 3 | -15.47 | 8.19 | -1.89 | 0.059 | 0.629 | n.s. |
| Cardinality (no change) - Increase by 1 | -17.91 | 8.18 | -2.19 | 0.029 | 0.406 | n.s. |
| Cardinality (no change) - Increase by 2 | -21.87 | 8.17 | -2.68 | 0.007 | 0.138 | n.s. |
| Cardinality (no change) - Increase by 3 | -11.41 | 8.03 | -1.42 | 0.155 | 0.906 | n.s. |
| Decrease by 1 - Decrease by 2 | 18.16 | 8.01 | 2.27 | 0.023 | 0.362 | n.s. |
| Decrease by 1 - Decrease by 3 | 9.29 | 8.01 | 1.16 | 0.246 | 0.955 | n.s. |
| Decrease by 1 - Increase by 1 | 6.85 | 8.01 | 0.86 | 0.392 | 0.989 | n.s. |
| Decrease by 1 - Increase by 2 | 2.89 | 8.01 | 0.36 | 0.718 | 0.989 | n.s. |
| Decrease by 1 - Increase by 3 | 13.35 | 8.05 | 1.66 | 0.097 | 0.784 | n.s. |
| Decrease by 2 - Decrease by 3 | -8.87 | 8.02 | -1.11 | 0.269 | 0.956 | n.s. |
| Decrease by 2 - Increase by 1 | -11.30 | 8.01 | -1.41 | 0.158 | 0.906 | n.s. |
| Decrease by 2 - Increase by 2 | -15.26 | 8.01 | -1.91 | 0.057 | 0.629 | n.s. |
| Decrease by 2 - Increase by 3 | -4.81 | 8.03 | -0.60 | 0.549 | 0.989 | n.s. |
| Decrease by 3 - Increase by 1 | -2.43 | 8.00 | -0.30 | 0.761 | 0.989 | n.s. |
| Decrease by 3 - Increase by 2 | -6.39 | 8.01 | -0.80 | 0.424 | 0.989 | n.s. |
| Decrease by 3 - Increase by 3 | 4.06 | 8.07 | 0.50 | 0.615 | 0.989 | n.s. |
| Increase by 1 - Increase by 2 | -3.96 | 8.00 | -0.49 | 0.621 | 0.989 | n.s. |
| Increase by 1 - Increase by 3 | 6.50 | 8.06 | 0.81 | 0.420 | 0.989 | n.s. |
| Increase by 2 - Increase by 3 | 10.46 | 8.06 | 1.30 | 0.194 | 0.925 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.05, *p* = 0.063, η²_G = 0.052
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -3.13 | 23 | = 0.098 | -0.75 [-1.10, -0.18] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.91 | 23 | = 0.523 | -0.20 [-0.61, 0.24] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | -1.97 | 23 | = 0.265 | -0.47 [-0.84, 0.04] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | -1.82 | 23 | = 0.287 | -0.52 [-0.81, 0.07] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | -2.64 | 23 | = 0.106 | -0.71 [-0.99, -0.09] | medium | n.s. |
| Cardinality (no change) vs Increase by 3 | -1.20 | 23 | = 0.453 | -0.33 [-0.67, 0.18] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 2.63 | 23 | = 0.106 | 0.55 [0.08, 0.99] | medium | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.16 | 23 | = 0.453 | 0.27 [-0.19, 0.66] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 0.95 | 23 | = 0.523 | 0.19 [-0.23, 0.62] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 0.35 | 23 | = 0.763 | 0.09 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 1.28 | 23 | = 0.453 | 0.34 [-0.17, 0.69] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.25 | 23 | = 0.453 | -0.27 [-0.69, 0.17] | small | n.s. |
| Decrease by 2 vs Increase by 1 | -1.59 | 23 | = 0.378 | -0.33 [-0.76, 0.11] | small | n.s. |
| Decrease by 2 vs Increase by 2 | -1.95 | 23 | = 0.265 | -0.49 [-0.84, 0.04] | small | n.s. |
| Decrease by 2 vs Increase by 3 | -0.58 | 23 | = 0.738 | -0.16 [-0.54, 0.31] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | -0.26 | 23 | = 0.798 | -0.07 [-0.48, 0.37] | negligible | n.s. |
| Decrease by 3 vs Increase by 2 | -1.04 | 23 | = 0.498 | -0.20 [-0.64, 0.21] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 0.48 | 23 | = 0.738 | 0.09 [-0.32, 0.52] | negligible | n.s. |
| Increase by 1 vs Increase by 2 | -0.43 | 23 | = 0.738 | -0.12 [-0.51, 0.33] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.48 | 23 | = 0.738 | 0.15 [-0.33, 0.52] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 1.26 | 23 | = 0.453 | 0.27 [-0.17, 0.69] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 651.72, BIC = 682.96
- **Decrease by 1 vs Cardinality (no change)**: *β* = 2.02, *SE* = 0.364, *z* = 5.556, *p* < .001
- **Decrease by 2 vs Cardinality (no change)**: *β* = 2.18, *SE* = 0.362, *z* = 6.024, *p* < .001
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.75, *SE* = 0.367, *z* = 7.494, *p* < .001
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.96, *SE* = 0.366, *z* = 2.618, *p* = 0.009
- **Increase by 2 vs Cardinality (no change)**: *β* = 2.34, *SE* = 0.365, *z* = 6.413, *p* < .001
- **Increase by 3 vs Cardinality (no change)**: *β* = 2.49, *SE* = 0.358, *z* = 6.955, *p* < .001
- **SNR**: *β* = 0.09, *SE* = 0.025, *z* = 3.423, *p* = 0.001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -2.02 | 0.36 | -5.56 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 2 | -2.18 | 0.36 | -6.02 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 3 | -2.75 | 0.37 | -7.49 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 1 | -0.96 | 0.37 | -2.62 | 0.009 | 0.093 | n.s. |
| Cardinality (no change) - Increase by 2 | -2.34 | 0.37 | -6.41 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 3 | -2.49 | 0.36 | -6.95 | < .001 | < .001 | *** |
| Decrease by 1 - Decrease by 2 | -0.16 | 0.36 | -0.45 | 0.654 | 0.959 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.73 | 0.36 | -2.03 | 0.042 | 0.349 | n.s. |
| Decrease by 1 - Increase by 1 | 1.07 | 0.36 | 2.99 | 0.003 | 0.033 | * |
| Decrease by 1 - Increase by 2 | -0.32 | 0.36 | -0.90 | 0.370 | 0.937 | n.s. |
| Decrease by 1 - Increase by 3 | -0.47 | 0.36 | -1.31 | 0.191 | 0.817 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.57 | 0.36 | -1.58 | 0.113 | 0.662 | n.s. |
| Decrease by 2 - Increase by 1 | 1.23 | 0.36 | 3.43 | < .001 | 0.008 | ** |
| Decrease by 2 - Increase by 2 | -0.16 | 0.36 | -0.45 | 0.654 | 0.959 | n.s. |
| Decrease by 2 - Increase by 3 | -0.31 | 0.36 | -0.86 | 0.388 | 0.937 | n.s. |
| Decrease by 3 - Increase by 1 | 1.79 | 0.36 | 5.02 | < .001 | < .001 | *** |
| Decrease by 3 - Increase by 2 | 0.41 | 0.36 | 1.14 | 0.256 | 0.873 | n.s. |
| Decrease by 3 - Increase by 3 | 0.26 | 0.36 | 0.71 | 0.476 | 0.937 | n.s. |
| Increase by 1 - Increase by 2 | -1.39 | 0.36 | -3.88 | < .001 | 0.001 | ** |
| Increase by 1 - Increase by 3 | -1.53 | 0.36 | -4.26 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | -0.15 | 0.36 | -0.41 | 0.679 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 15.63, *p* < .001, η²_G = 0.093
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.570)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -5.27 | 23 | < .001 | -0.79 [-1.61, -0.54] | medium | *** |
| Cardinality (no change) vs Decrease by 2 | -5.56 | 23 | < .001 | -0.85 [-1.68, -0.59] | large | *** |
| Cardinality (no change) vs Decrease by 3 | -4.96 | 23 | < .001 | -0.97 [-1.53, -0.49] | large | *** |
| Cardinality (no change) vs Increase by 1 | -2.61 | 23 | = 0.030 | -0.41 [-0.98, -0.08] | small | * |
| Cardinality (no change) vs Increase by 2 | -5.67 | 23 | < .001 | -0.85 [-1.70, -0.61] | large | *** |
| Cardinality (no change) vs Increase by 3 | -5.16 | 23 | < .001 | -0.97 [-1.58, -0.53] | large | *** |
| Decrease by 1 vs Decrease by 2 | -0.50 | 23 | = 0.650 | -0.04 [-0.53, 0.32] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.25 | 23 | = 0.060 | -0.23 [-0.90, -0.02] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 4.08 | 23 | < .001 | 0.32 [0.34, 1.32] | small | *** |
| Decrease by 1 vs Increase by 2 | -1.33 | 23 | = 0.281 | -0.11 [-0.70, 0.16] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | -1.28 | 23 | = 0.281 | -0.12 [-0.69, 0.17] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.77 | 23 | = 0.145 | -0.20 [-0.80, 0.07] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 4.36 | 23 | < .001 | 0.37 [0.39, 1.39] | small | *** |
| Decrease by 2 vs Increase by 2 | -0.65 | 23 | = 0.579 | -0.07 [-0.56, 0.29] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | -0.72 | 23 | = 0.560 | -0.07 [-0.57, 0.28] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | 4.21 | 23 | < .001 | 0.53 [0.37, 1.35] | medium | *** |
| Decrease by 3 vs Increase by 2 | 1.03 | 23 | = 0.390 | 0.12 [-0.22, 0.64] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 1.31 | 23 | = 0.281 | 0.14 [-0.16, 0.70] | negligible | n.s. |
| Increase by 1 vs Increase by 2 | -4.65 | 23 | < .001 | -0.41 [-1.46, -0.44] | small | *** |
| Increase by 1 vs Increase by 3 | -4.44 | 23 | < .001 | -0.46 [-1.41, -0.40] | small | *** |
| Increase by 2 vs Increase by 3 | 0.02 | 23 | = 0.982 | 0.00 [-0.42, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.008). Post-hoc tests revealed:
  - Cardinality (no change) showed greater latency than Increase by 1 (*d* = 0.59)
  - Cardinality (no change) showed greater latency than Increase by 3 (*d* = 0.57)
  - Decrease by 2 showed greater latency than Increase by 1 (*d* = 0.65)
  - Decrease by 2 showed greater latency than Increase by 3 (*d* = 0.63)
**Fz amplitude:** Significant main effect of condition (*p* = 0.043) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* = 0.004) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed greater amplitude than Increase by 2 (*d* = 0.34)
  - Cardinality (no change) showed greater amplitude than Increase by 3 (*d* = 0.62)
  - Decrease by 1 showed greater amplitude than Increase by 3 (*d* = 0.53)
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.45)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed greater latency than Increase by 3 (*d* = 0.52)
  - Decrease by 1 showed smaller latency than Decrease by 2 (*d* = -0.51)
  - Decrease by 2 showed greater latency than Increase by 1 (*d* = 0.77)
  - Decrease by 2 showed greater latency than Increase by 2 (*d* = 0.89)
  - Decrease by 2 showed greater latency than Increase by 3 (*d* = 1.16)
  - Decrease by 3 showed greater latency than Increase by 3 (*d* = 0.79)
**P1 amplitude:** Significant main effect of condition (*p* = 0.028). Post-hoc tests revealed:
  - Decrease by 1 showed smaller amplitude than Decrease by 3 (*d* = -0.44)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.063)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller amplitude than Decrease by 1 (*d* = -0.79)
  - Cardinality (no change) showed smaller amplitude than Decrease by 2 (*d* = -0.85)
  - Cardinality (no change) showed smaller amplitude than Decrease by 3 (*d* = -0.97)
  - Cardinality (no change) showed smaller amplitude than Increase by 1 (*d* = -0.41)
  - Cardinality (no change) showed smaller amplitude than Increase by 2 (*d* = -0.85)
  - Cardinality (no change) showed smaller amplitude than Increase by 3 (*d* = -0.97)
  - Decrease by 1 showed greater amplitude than Increase by 1 (*d* = 0.32)
  - Decrease by 2 showed greater amplitude than Increase by 1 (*d* = 0.37)
  - Decrease by 3 showed greater amplitude than Increase by 1 (*d* = 0.53)
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.41)
  - Increase by 1 showed smaller amplitude than Increase by 3 (*d* = -0.46)

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

#### Amplitude

### 5.3 P1 Component

#### Latency

#### Amplitude

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
