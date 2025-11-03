# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:43:59

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
| Cardinality (no change) | 18 | 110.89 ms | 6.26 | 1.48 | [92.00, 116.00] |
| Decrease by 1 | 16 | 106.25 ms | 8.64 | 2.16 | [92.00, 116.00] |
| Decrease by 2 | 21 | 107.62 ms | 8.75 | 1.91 | [92.00, 116.00] |
| Decrease by 3 | 18 | 105.11 ms | 8.09 | 1.91 | [92.00, 116.00] |
| Increase by 1 | 16 | 102.50 ms | 8.75 | 2.19 | [92.00, 116.00] |
| Increase by 2 | 15 | 104.00 ms | 8.68 | 2.24 | [92.00, 116.00] |
| Increase by 3 | 14 | 103.14 ms | 7.05 | 1.88 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 18 | -1.77 µV | 1.24 | 0.29 | [-4.83, -0.25] |
| Decrease by 1 | 16 | -1.64 µV | 1.20 | 0.30 | [-4.56, -0.23] |
| Decrease by 2 | 21 | -1.73 µV | 0.99 | 0.22 | [-4.30, -0.45] |
| Decrease by 3 | 18 | -2.41 µV | 1.59 | 0.38 | [-6.39, -0.34] |
| Increase by 1 | 16 | -1.75 µV | 1.08 | 0.27 | [-3.74, -0.14] |
| Increase by 2 | 15 | -1.67 µV | 1.17 | 0.30 | [-4.17, -0.21] |
| Increase by 3 | 14 | -1.78 µV | 1.04 | 0.28 | [-3.35, -0.46] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | 176.17 ms | 17.41 | 3.63 | [144.00, 208.00] |
| Decrease by 1 | 22 | 176.55 ms | 12.73 | 2.71 | [152.00, 208.00] |
| Decrease by 2 | 24 | 177.33 ms | 14.53 | 2.97 | [144.00, 208.00] |
| Decrease by 3 | 24 | 177.00 ms | 15.02 | 3.07 | [152.00, 208.00] |
| Increase by 1 | 23 | 169.57 ms | 19.10 | 3.98 | [144.00, 208.00] |
| Increase by 2 | 24 | 168.83 ms | 18.42 | 3.76 | [144.00, 200.00] |
| Increase by 3 | 23 | 170.26 ms | 18.68 | 3.89 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | -4.80 µV | 2.00 | 0.42 | [-9.57, -1.40] |
| Decrease by 1 | 22 | -5.16 µV | 1.92 | 0.41 | [-9.90, -2.24] |
| Decrease by 2 | 24 | -5.13 µV | 2.10 | 0.43 | [-9.59, -1.53] |
| Decrease by 3 | 24 | -5.22 µV | 1.97 | 0.40 | [-8.60, -1.48] |
| Increase by 1 | 23 | -5.11 µV | 2.15 | 0.45 | [-9.46, -0.80] |
| Increase by 2 | 24 | -5.47 µV | 2.43 | 0.50 | [-11.28, -1.22] |
| Increase by 3 | 23 | -6.29 µV | 2.53 | 0.53 | [-12.86, -2.17] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 111.38 ms | 6.50 | 1.80 | [100.00, 116.00] |
| Decrease by 1 | 14 | 110.86 ms | 8.07 | 2.16 | [92.00, 116.00] |
| Decrease by 2 | 17 | 109.88 ms | 8.50 | 2.06 | [92.00, 116.00] |
| Decrease by 3 | 17 | 109.41 ms | 6.32 | 1.53 | [96.00, 116.00] |
| Increase by 1 | 17 | 105.41 ms | 9.05 | 2.19 | [92.00, 116.00] |
| Increase by 2 | 13 | 109.23 ms | 7.00 | 1.94 | [96.00, 116.00] |
| Increase by 3 | 15 | 102.93 ms | 9.50 | 2.45 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 2.47 µV | 1.69 | 0.47 | [0.70, 5.73] |
| Decrease by 1 | 14 | 2.19 µV | 1.67 | 0.45 | [0.47, 5.23] |
| Decrease by 2 | 17 | 2.32 µV | 1.29 | 0.31 | [0.54, 5.74] |
| Decrease by 3 | 17 | 2.61 µV | 1.93 | 0.47 | [0.48, 8.15] |
| Increase by 1 | 17 | 1.92 µV | 1.45 | 0.35 | [0.54, 4.44] |
| Increase by 2 | 13 | 2.11 µV | 1.41 | 0.39 | [0.43, 4.70] |
| Increase by 3 | 15 | 2.20 µV | 1.37 | 0.35 | [0.69, 5.27] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 470.57 ms | 23.14 | 6.19 | [436.00, 516.00] |
| Decrease by 1 | 19 | 485.05 ms | 30.05 | 6.89 | [436.00, 532.00] |
| Decrease by 2 | 19 | 470.32 ms | 27.37 | 6.28 | [420.00, 532.00] |
| Decrease by 3 | 19 | 479.58 ms | 28.72 | 6.59 | [432.00, 524.00] |
| Increase by 1 | 17 | 489.88 ms | 39.70 | 9.63 | [420.00, 532.00] |
| Increase by 2 | 18 | 487.33 ms | 31.50 | 7.43 | [428.00, 532.00] |
| Increase by 3 | 21 | 479.05 ms | 37.37 | 8.16 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 2.75 µV | 1.66 | 0.44 | [0.90, 5.95] |
| Decrease by 1 | 19 | 5.16 µV | 2.46 | 0.56 | [1.31, 9.87] |
| Decrease by 2 | 19 | 4.93 µV | 2.05 | 0.47 | [1.69, 8.68] |
| Decrease by 3 | 19 | 5.54 µV | 2.91 | 0.67 | [0.72, 12.38] |
| Increase by 1 | 17 | 4.69 µV | 2.66 | 0.64 | [1.41, 10.19] |
| Increase by 2 | 18 | 5.45 µV | 2.67 | 0.63 | [1.31, 10.55] |
| Increase by 3 | 21 | 4.44 µV | 2.61 | 0.57 | [1.25, 10.15] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 807.23, BIC = 834.94
- **Decrease by 1 vs Cardinality (no change)**: *β* = -2.65, *SE* = 2.105, *z* = -1.257, *p* = 0.209
- **Decrease by 2 vs Cardinality (no change)**: *β* = -1.69, *SE* = 1.923, *z* = -0.876, *p* = 0.381
- **Decrease by 3 vs Cardinality (no change)**: *β* = -4.42, *SE* = 2.015, *z* = -2.196, *p* = 0.028
- **Increase by 1 vs Cardinality (no change)**: *β* = -6.70, *SE* = 2.052, *z* = -3.263, *p* = 0.001
- **Increase by 2 vs Cardinality (no change)**: *β* = -6.40, *SE* = 2.083, *z* = -3.072, *p* = 0.002
- **Increase by 3 vs Cardinality (no change)**: *β* = -6.21, *SE* = 2.128, *z* = -2.921, *p* = 0.003
- **SNR**: *β* = 0.87, *SE* = 0.345, *z* = 2.533, *p* = 0.011

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 2.65 | 2.11 | 1.26 | 0.209 | 0.904 | n.s. |
| Cardinality (no change) - Decrease by 2 | 1.68 | 1.92 | 0.88 | 0.381 | 0.970 | n.s. |
| Cardinality (no change) - Decrease by 3 | 4.42 | 2.01 | 2.20 | 0.028 | 0.366 | n.s. |
| Cardinality (no change) - Increase by 1 | 6.70 | 2.05 | 3.26 | 0.001 | 0.023 | * |
| Cardinality (no change) - Increase by 2 | 6.40 | 2.08 | 3.07 | 0.002 | 0.042 | * |
| Cardinality (no change) - Increase by 3 | 6.22 | 2.13 | 2.92 | 0.003 | 0.064 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.96 | 2.01 | -0.48 | 0.633 | 0.982 | n.s. |
| Decrease by 1 - Decrease by 3 | 1.78 | 2.12 | 0.84 | 0.402 | 0.970 | n.s. |
| Decrease by 1 - Increase by 1 | 4.05 | 2.12 | 1.91 | 0.057 | 0.557 | n.s. |
| Decrease by 1 - Increase by 2 | 3.76 | 2.17 | 1.73 | 0.084 | 0.680 | n.s. |
| Decrease by 1 - Increase by 3 | 3.57 | 2.23 | 1.60 | 0.109 | 0.750 | n.s. |
| Decrease by 2 - Decrease by 3 | 2.74 | 1.91 | 1.44 | 0.151 | 0.835 | n.s. |
| Decrease by 2 - Increase by 1 | 5.01 | 1.98 | 2.53 | 0.011 | 0.186 | n.s. |
| Decrease by 2 - Increase by 2 | 4.72 | 2.04 | 2.31 | 0.021 | 0.300 | n.s. |
| Decrease by 2 - Increase by 3 | 4.53 | 2.07 | 2.19 | 0.029 | 0.366 | n.s. |
| Decrease by 3 - Increase by 1 | 2.27 | 2.07 | 1.10 | 0.273 | 0.943 | n.s. |
| Decrease by 3 - Increase by 2 | 1.98 | 2.14 | 0.92 | 0.355 | 0.970 | n.s. |
| Decrease by 3 - Increase by 3 | 1.79 | 2.15 | 0.83 | 0.404 | 0.970 | n.s. |
| Increase by 1 - Increase by 2 | -0.30 | 2.17 | -0.14 | 0.892 | 0.995 | n.s. |
| Increase by 1 - Increase by 3 | -0.48 | 2.19 | -0.22 | 0.826 | 0.995 | n.s. |
| Increase by 2 - Increase by 3 | -0.19 | 2.23 | -0.08 | 0.934 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.19, *p* = 0.357, η²_G = 0.096
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 1.19 | 3 | = 0.693 | 0.51 [-0.49, 0.79] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 | 1.00 | 3 | = 0.693 | 0.22 [-0.28, 0.80] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.57 | 3 | = 0.693 | 0.84 [-0.27, 0.98] | large | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.57 | 3 | = 0.693 | 0.93 [0.09, 1.40] | large | n.s. |
| Cardinality (no change) vs Increase by 2 | 0.77 | 3 | = 0.693 | 0.31 [0.01, 1.28] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 1.57 | 3 | = 0.693 | 0.62 [0.40, 1.99] | medium | n.s. |
| Decrease by 1 vs Decrease by 2 | -0.77 | 3 | = 0.693 | -0.32 [-0.49, 0.67] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.00 | 3 | = 1.000 | 0.00 [-0.82, 0.53] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 1.57 | 3 | = 0.693 | 0.39 [-0.25, 1.07] | small | n.s. |
| Decrease by 1 vs Increase by 2 | -1.00 | 3 | = 0.693 | -0.13 [-0.34, 1.05] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 0.00 | 3 | = 1.000 | 0.00 [-0.27, 1.38] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.77 | 3 | = 0.693 | 0.46 [-0.32, 0.72] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 1.21 | 3 | = 0.693 | 0.73 [-0.15, 1.01] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 0.40 | 3 | = 0.887 | 0.15 [-0.18, 1.09] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | 0.77 | 3 | = 0.693 | 0.37 [-0.08, 1.22] | small | n.s. |
| Decrease by 3 vs Increase by 1 | 1.19 | 3 | = 0.693 | 0.48 [-0.36, 0.86] | small | n.s. |
| Decrease by 3 vs Increase by 2 | -0.33 | 3 | = 0.888 | -0.16 [-0.48, 0.88] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 0.00 | 3 | = 1.000 | 0.00 [-0.43, 0.86] | negligible | n.s. |
| Increase by 1 vs Increase by 2 | -1.41 | 3 | = 0.693 | -0.49 [-1.23, 0.28] | small | n.s. |
| Increase by 1 vs Increase by 3 | -1.19 | 3 | = 0.693 | -0.42 [-0.73, 0.61] | small | n.s. |
| Increase by 2 vs Increase by 3 | 0.52 | 3 | = 0.837 | 0.14 [-1.10, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 284.74, BIC = 312.45
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.13, *SE* = 0.227, *z* = -0.572, *p* = 0.567
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.13, *SE* = 0.207, *z* = -0.617, *p* = 0.537
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.62, *SE* = 0.217, *z* = -2.870, *p* = 0.004
- **Increase by 1 vs Cardinality (no change)**: *β* = -0.06, *SE* = 0.221, *z* = -0.282, *p* = 0.778
- **Increase by 2 vs Cardinality (no change)**: *β* = -0.07, *SE* = 0.225, *z* = -0.312, *p* = 0.755
- **Increase by 3 vs Cardinality (no change)**: *β* = -0.16, *SE* = 0.229, *z* = -0.702, *p* = 0.483
- **SNR**: *β* = -0.35, *SE* = 0.038, *z* = -9.261, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.13 | 0.23 | 0.57 | 0.567 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.13 | 0.21 | 0.62 | 0.537 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.62 | 0.22 | 2.87 | 0.004 | 0.083 | n.s. |
| Cardinality (no change) - Increase by 1 | 0.06 | 0.22 | 0.28 | 0.778 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 | 0.07 | 0.22 | 0.31 | 0.755 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 | 0.16 | 0.23 | 0.70 | 0.483 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.00 | 0.22 | -0.01 | 0.993 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.49 | 0.23 | 2.14 | 0.032 | 0.427 | n.s. |
| Decrease by 1 - Increase by 1 | -0.07 | 0.23 | -0.29 | 0.769 | 1.000 | n.s. |
| Decrease by 1 - Increase by 2 | -0.06 | 0.23 | -0.25 | 0.799 | 1.000 | n.s. |
| Decrease by 1 - Increase by 3 | 0.03 | 0.24 | 0.13 | 0.897 | 1.000 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.50 | 0.21 | 2.41 | 0.016 | 0.266 | n.s. |
| Decrease by 2 - Increase by 1 | -0.07 | 0.21 | -0.31 | 0.760 | 1.000 | n.s. |
| Decrease by 2 - Increase by 2 | -0.06 | 0.22 | -0.26 | 0.793 | 1.000 | n.s. |
| Decrease by 2 - Increase by 3 | 0.03 | 0.22 | 0.15 | 0.882 | 1.000 | n.s. |
| Decrease by 3 - Increase by 1 | -0.56 | 0.22 | -2.50 | 0.012 | 0.222 | n.s. |
| Decrease by 3 - Increase by 2 | -0.55 | 0.23 | -2.40 | 0.017 | 0.266 | n.s. |
| Decrease by 3 - Increase by 3 | -0.46 | 0.23 | -1.99 | 0.046 | 0.533 | n.s. |
| Increase by 1 - Increase by 2 | 0.01 | 0.23 | 0.03 | 0.974 | 1.000 | n.s. |
| Increase by 1 - Increase by 3 | 0.10 | 0.24 | 0.42 | 0.676 | 1.000 | n.s. |
| Increase by 2 - Increase by 3 | 0.09 | 0.24 | 0.38 | 0.706 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.03, *p* = 0.032, η²_G = 0.250
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -0.43 | 3 | = 0.862 | -0.25 [-0.71, 0.56] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | -3.12 | 3 | = 0.243 | -0.28 [-0.53, 0.54] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.46 | 3 | = 0.390 | 0.49 [-0.16, 1.12] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | -3.06 | 3 | = 0.243 | -0.96 [-0.70, 0.46] | large | n.s. |
| Cardinality (no change) vs Increase by 2 | -0.38 | 3 | = 0.862 | -0.20 [-0.71, 0.45] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 | -1.50 | 3 | = 0.390 | -0.95 [-0.78, 0.44] | large | n.s. |
| Decrease by 1 vs Decrease by 2 | -0.12 | 3 | = 0.960 | -0.06 [-0.47, 0.69] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.72 | 3 | = 0.390 | 0.73 [0.08, 1.66] | medium | n.s. |
| Decrease by 1 vs Increase by 1 | -2.47 | 3 | = 0.243 | -0.82 [-0.55, 0.73] | large | n.s. |
| Decrease by 1 vs Increase by 2 | 0.34 | 3 | = 0.862 | 0.09 [-0.80, 0.55] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | -1.52 | 3 | = 0.390 | -0.81 [-0.96, 0.59] | large | n.s. |
| Decrease by 2 vs Decrease by 3 | 2.44 | 3 | = 0.243 | 0.71 [0.01, 1.12] | medium | n.s. |
| Decrease by 2 vs Increase by 1 | -2.48 | 3 | = 0.243 | -0.66 [-0.48, 0.62] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 0.31 | 3 | = 0.862 | 0.14 [-0.72, 0.49] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | -1.00 | 3 | = 0.545 | -0.65 [-0.67, 0.54] | medium | n.s. |
| Decrease by 3 vs Increase by 1 | -6.84 | 3 | = 0.134 | -1.28 [-2.18, -0.51] | large | n.s. |
| Decrease by 3 vs Increase by 2 | -1.52 | 3 | = 0.390 | -0.70 [-1.95, -0.25] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | -2.56 | 3 | = 0.243 | -1.27 [-1.16, 0.18] | large | n.s. |
| Increase by 1 vs Increase by 2 | 2.69 | 3 | = 0.243 | 0.95 [-0.55, 0.89] | large | n.s. |
| Increase by 1 vs Increase by 3 | 0.00 | 3 | = 0.999 | 0.00 [-0.41, 0.96] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.37 | 3 | = 0.397 | -0.94 [-0.74, 0.69] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1296.95, BIC = 1327.88
- **Decrease by 1 vs Cardinality (no change)**: *β* = 2.83, *SE* = 3.021, *z* = 0.937, *p* = 0.349
- **Decrease by 2 vs Cardinality (no change)**: *β* = 1.61, *SE* = 2.952, *z* = 0.544, *p* = 0.586
- **Decrease by 3 vs Cardinality (no change)**: *β* = 1.28, *SE* = 2.959, *z* = 0.433, *p* = 0.665
- **Increase by 1 vs Cardinality (no change)**: *β* = -4.93, *SE* = 3.015, *z* = -1.635, *p* = 0.102
- **Increase by 2 vs Cardinality (no change)**: *β* = -6.88, *SE* = 2.969, *z* = -2.316, *p* = 0.021
- **Increase by 3 vs Cardinality (no change)**: *β* = -4.25, *SE* = 2.994, *z* = -1.421, *p* = 0.155
- **SNR**: *β* = -0.02, *SE* = 0.209, *z* = -0.111, *p* = 0.912

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -2.83 | 3.02 | -0.94 | 0.349 | 0.979 | n.s. |
| Cardinality (no change) - Decrease by 2 | -1.61 | 2.95 | -0.54 | 0.586 | 0.995 | n.s. |
| Cardinality (no change) - Decrease by 3 | -1.28 | 2.96 | -0.43 | 0.665 | 0.995 | n.s. |
| Cardinality (no change) - Increase by 1 | 4.93 | 3.02 | 1.63 | 0.102 | 0.694 | n.s. |
| Cardinality (no change) - Increase by 2 | 6.88 | 2.97 | 2.32 | 0.021 | 0.284 | n.s. |
| Cardinality (no change) - Increase by 3 | 4.25 | 2.99 | 1.42 | 0.155 | 0.815 | n.s. |
| Decrease by 1 - Decrease by 2 | 1.22 | 2.99 | 0.41 | 0.682 | 0.995 | n.s. |
| Decrease by 1 - Decrease by 3 | 1.55 | 3.00 | 0.52 | 0.606 | 0.995 | n.s. |
| Decrease by 1 - Increase by 1 | 7.76 | 3.05 | 2.54 | 0.011 | 0.180 | n.s. |
| Decrease by 1 - Increase by 2 | 9.70 | 3.01 | 3.23 | 0.001 | 0.026 | * |
| Decrease by 1 - Increase by 3 | 7.08 | 3.03 | 2.34 | 0.019 | 0.284 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.32 | 2.91 | 0.11 | 0.911 | 0.995 | n.s. |
| Decrease by 2 - Increase by 1 | 6.54 | 2.96 | 2.21 | 0.027 | 0.337 | n.s. |
| Decrease by 2 - Increase by 2 | 8.48 | 2.91 | 2.91 | 0.004 | 0.070 | n.s. |
| Decrease by 2 - Increase by 3 | 5.86 | 2.95 | 1.99 | 0.047 | 0.463 | n.s. |
| Decrease by 3 - Increase by 1 | 6.21 | 2.95 | 2.11 | 0.035 | 0.395 | n.s. |
| Decrease by 3 - Increase by 2 | 8.16 | 2.91 | 2.80 | 0.005 | 0.092 | n.s. |
| Decrease by 3 - Increase by 3 | 5.54 | 2.95 | 1.88 | 0.060 | 0.525 | n.s. |
| Increase by 1 - Increase by 2 | 1.95 | 2.95 | 0.66 | 0.509 | 0.993 | n.s. |
| Increase by 1 - Increase by 3 | -0.68 | 2.98 | -0.23 | 0.820 | 0.995 | n.s. |
| Increase by 2 - Increase by 3 | -2.62 | 2.95 | -0.89 | 0.374 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.61, *p* = 0.003, η²_G = 0.080
- Greenhouse-Geisser corrected: *p* = 0.016 (ε = 0.543)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.28 | 19 | = 0.322 | -0.26 [-0.74, 0.18] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | -1.08 | 19 | = 0.408 | -0.20 [-0.57, 0.30] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.62 | 19 | = 0.714 | -0.17 [-0.52, 0.35] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.80 | 19 | = 0.167 | 0.38 [-0.12, 0.79] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.14 | 19 | = 0.137 | 0.46 [0.03, 0.95] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 1.31 | 19 | = 0.322 | 0.31 [-0.20, 0.70] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 0.24 | 19 | = 0.855 | 0.05 [-0.41, 0.48] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.43 | 19 | = 0.778 | 0.08 [-0.35, 0.54] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 2.49 | 19 | = 0.117 | 0.68 [0.05, 1.03] | medium | n.s. |
| Decrease by 1 vs Increase by 2 | 3.06 | 19 | = 0.113 | 0.77 [0.19, 1.18] | medium | n.s. |
| Decrease by 1 vs Increase by 3 | 2.22 | 19 | = 0.137 | 0.59 [0.01, 0.98] | medium | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.12 | 19 | = 0.906 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 2.19 | 19 | = 0.137 | 0.59 [-0.09, 0.80] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 2.83 | 19 | = 0.113 | 0.67 [0.11, 1.01] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 1.93 | 19 | = 0.161 | 0.51 [-0.12, 0.77] | medium | n.s. |
| Decrease by 3 vs Increase by 1 | 1.81 | 19 | = 0.167 | 0.56 [-0.14, 0.74] | medium | n.s. |
| Decrease by 3 vs Increase by 2 | 2.51 | 19 | = 0.117 | 0.64 [0.06, 0.96] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | 2.02 | 19 | = 0.153 | 0.48 [-0.10, 0.79] | small | n.s. |
| Increase by 1 vs Increase by 2 | 0.48 | 19 | = 0.778 | 0.07 [-0.24, 0.63] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.39 | 19 | = 0.778 | -0.07 [-0.49, 0.38] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.37 | 19 | = 0.322 | -0.15 [-0.82, 0.07] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 569.58, BIC = 600.52
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.20, *SE* = 0.319, *z* = -0.612, *p* = 0.540
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.30, *SE* = 0.312, *z* = -0.974, *p* = 0.330
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.34, *SE* = 0.313, *z* = -1.104, *p* = 0.270
- **Increase by 1 vs Cardinality (no change)**: *β* = -0.14, *SE* = 0.319, *z* = -0.425, *p* = 0.671
- **Increase by 2 vs Cardinality (no change)**: *β* = -0.54, *SE* = 0.314, *z* = -1.732, *p* = 0.083
- **Increase by 3 vs Cardinality (no change)**: *β* = -1.41, *SE* = 0.316, *z* = -4.453, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.022, *z* = -5.005, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.20 | 0.32 | 0.61 | 0.540 | 0.998 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.30 | 0.31 | 0.97 | 0.330 | 0.988 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.35 | 0.31 | 1.10 | 0.270 | 0.983 | n.s. |
| Cardinality (no change) - Increase by 1 | 0.14 | 0.32 | 0.43 | 0.671 | 0.998 | n.s. |
| Cardinality (no change) - Increase by 2 | 0.54 | 0.31 | 1.73 | 0.083 | 0.729 | n.s. |
| Cardinality (no change) - Increase by 3 | 1.41 | 0.32 | 4.45 | < .001 | < .001 | *** |
| Decrease by 1 - Decrease by 2 | 0.11 | 0.32 | 0.34 | 0.732 | 0.998 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.15 | 0.32 | 0.47 | 0.636 | 0.998 | n.s. |
| Decrease by 1 - Increase by 1 | -0.06 | 0.32 | -0.19 | 0.853 | 0.998 | n.s. |
| Decrease by 1 - Increase by 2 | 0.35 | 0.32 | 1.10 | 0.273 | 0.983 | n.s. |
| Decrease by 1 - Increase by 3 | 1.21 | 0.32 | 3.79 | < .001 | 0.003 | ** |
| Decrease by 2 - Decrease by 3 | 0.04 | 0.31 | 0.13 | 0.893 | 0.998 | n.s. |
| Decrease by 2 - Increase by 1 | -0.17 | 0.31 | -0.54 | 0.590 | 0.998 | n.s. |
| Decrease by 2 - Increase by 2 | 0.24 | 0.31 | 0.78 | 0.436 | 0.997 | n.s. |
| Decrease by 2 - Increase by 3 | 1.10 | 0.31 | 3.55 | < .001 | 0.007 | ** |
| Decrease by 3 - Increase by 1 | -0.21 | 0.31 | -0.67 | 0.501 | 0.998 | n.s. |
| Decrease by 3 - Increase by 2 | 0.20 | 0.31 | 0.65 | 0.519 | 0.998 | n.s. |
| Decrease by 3 - Increase by 3 | 1.06 | 0.31 | 3.42 | < .001 | 0.011 | * |
| Increase by 1 - Increase by 2 | 0.41 | 0.31 | 1.31 | 0.190 | 0.948 | n.s. |
| Increase by 1 - Increase by 3 | 1.27 | 0.31 | 4.05 | < .001 | 0.001 | ** |
| Increase by 2 - Increase by 3 | 0.87 | 0.31 | 2.78 | 0.005 | 0.084 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.56, *p* < .001, η²_G = 0.063
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.75 | 19 | = 0.566 | 0.10 [-0.28, 0.64] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | 1.34 | 19 | = 0.376 | 0.23 [-0.18, 0.70] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.26 | 19 | = 0.387 | 0.23 [-0.11, 0.78] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 2.08 | 19 | = 0.134 | 0.34 [-0.15, 0.76] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 3.36 | 19 | = 0.023 | 0.45 [0.11, 1.04] | small | * |
| Cardinality (no change) vs Increase by 3 | 5.30 | 19 | < .001 | 0.78 [0.59, 1.74] | medium | *** |
| Decrease by 1 vs Decrease by 2 | 0.73 | 19 | = 0.566 | 0.13 [-0.34, 0.55] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.71 | 19 | = 0.566 | 0.13 [-0.33, 0.56] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 1.34 | 19 | = 0.376 | 0.23 [-0.20, 0.73] | small | n.s. |
| Decrease by 1 vs Increase by 2 | 2.84 | 19 | = 0.055 | 0.35 [0.06, 1.01] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 3.72 | 19 | = 0.015 | 0.69 [0.28, 1.33] | medium | * |
| Decrease by 2 vs Decrease by 3 | -0.00 | 19 | = 0.996 | -0.00 [-0.36, 0.48] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 0.42 | 19 | = 0.712 | 0.09 [-0.48, 0.38] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | 1.01 | 19 | = 0.487 | 0.23 [-0.26, 0.59] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 2.67 | 19 | = 0.063 | 0.56 [0.08, 1.01] | medium | n.s. |
| Decrease by 3 vs Increase by 1 | 0.47 | 19 | = 0.711 | 0.09 [-0.51, 0.36] | negligible | n.s. |
| Decrease by 3 vs Increase by 2 | 1.15 | 19 | = 0.428 | 0.23 [-0.29, 0.55] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 2.50 | 19 | = 0.068 | 0.57 [0.03, 0.94] | medium | n.s. |
| Increase by 1 vs Increase by 2 | 0.89 | 19 | = 0.536 | 0.16 [-0.18, 0.70] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 2.48 | 19 | = 0.068 | 0.53 [0.15, 1.10] | medium | n.s. |
| Increase by 2 vs Increase by 3 | 1.99 | 19 | = 0.142 | 0.33 [0.03, 0.94] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 740.41, BIC = 767.05
- **Decrease by 1 vs Cardinality (no change)**: *β* = 0.74, *SE* = 2.582, *z* = 0.286, *p* = 0.775
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.06, *SE* = 2.473, *z* = -0.025, *p* = 0.980
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.01, *SE* = 2.549, *z* = -0.002, *p* = 0.998
- **Increase by 1 vs Cardinality (no change)**: *β* = -4.00, *SE* = 2.535, *z* = -1.579, *p* = 0.114
- **Increase by 2 vs Cardinality (no change)**: *β* = -1.43, *SE* = 2.658, *z* = -0.539, *p* = 0.590
- **Increase by 3 vs Cardinality (no change)**: *β* = -7.69, *SE* = 2.509, *z* = -3.066, *p* = 0.002
- **SNR**: *β* = 0.24, *SE* = 0.248, *z* = 0.977, *p* = 0.329

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -0.74 | 2.58 | -0.29 | 0.775 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.06 | 2.47 | 0.02 | 0.980 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.01 | 2.55 | 0.00 | 0.998 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 1 | 4.00 | 2.53 | 1.58 | 0.114 | 0.794 | n.s. |
| Cardinality (no change) - Increase by 2 | 1.43 | 2.66 | 0.54 | 0.590 | 0.999 | n.s. |
| Cardinality (no change) - Increase by 3 | 7.69 | 2.51 | 3.07 | 0.002 | 0.038 | * |
| Decrease by 1 - Decrease by 2 | 0.80 | 2.40 | 0.33 | 0.739 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.74 | 2.42 | 0.31 | 0.759 | 1.000 | n.s. |
| Decrease by 1 - Increase by 1 | 4.74 | 2.40 | 1.97 | 0.048 | 0.548 | n.s. |
| Decrease by 1 - Increase by 2 | 2.17 | 2.54 | 0.86 | 0.392 | 0.993 | n.s. |
| Decrease by 1 - Increase by 3 | 8.43 | 2.46 | 3.43 | < .001 | 0.013 | * |
| Decrease by 2 - Decrease by 3 | -0.06 | 2.30 | -0.02 | 0.981 | 1.000 | n.s. |
| Decrease by 2 - Increase by 1 | 3.94 | 2.26 | 1.74 | 0.082 | 0.713 | n.s. |
| Decrease by 2 - Increase by 2 | 1.37 | 2.46 | 0.56 | 0.577 | 0.999 | n.s. |
| Decrease by 2 - Increase by 3 | 7.63 | 2.33 | 3.27 | 0.001 | 0.021 | * |
| Decrease by 3 - Increase by 1 | 4.00 | 2.28 | 1.75 | 0.080 | 0.713 | n.s. |
| Decrease by 3 - Increase by 2 | 1.43 | 2.51 | 0.57 | 0.569 | 0.999 | n.s. |
| Decrease by 3 - Increase by 3 | 7.69 | 2.40 | 3.21 | 0.001 | 0.025 | * |
| Increase by 1 - Increase by 2 | -2.57 | 2.45 | -1.05 | 0.295 | 0.979 | n.s. |
| Increase by 1 - Increase by 3 | 3.69 | 2.36 | 1.56 | 0.118 | 0.794 | n.s. |
| Increase by 2 - Increase by 3 | 6.26 | 2.50 | 2.50 | 0.012 | 0.192 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.15, *p* = 0.068, η²_G = 0.145
- Greenhouse-Geisser corrected: *p* = 0.156 (ε = 0.324)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 1.00 | 7 | = 0.539 | 0.11 [-0.92, 0.38] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | nan | 7 | n/a | 0.00 [-0.64, 0.64] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 0.89 | 7 | = 0.540 | 0.43 [-0.72, 0.81] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.69 | 7 | = 0.336 | 0.77 [-0.27, 1.13] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.55 | 7 | = 0.328 | 0.78 [-0.05, 1.45] | medium | n.s. |
| Cardinality (no change) vs Increase by 3 | 2.03 | 7 | = 0.328 | 0.97 [0.07, 1.44] | large | n.s. |
| Decrease by 1 vs Decrease by 2 | -1.00 | 7 | = 0.539 | -0.11 [-0.39, 0.90] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.68 | 7 | = 0.608 | 0.35 [-0.72, 0.63] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 1.49 | 7 | = 0.371 | 0.71 [-0.20, 1.15] | medium | n.s. |
| Decrease by 1 vs Increase by 2 | 2.16 | 7 | = 0.328 | 0.69 [-0.04, 1.36] | medium | n.s. |
| Decrease by 1 vs Increase by 3 | 1.77 | 7 | = 0.336 | 0.90 [0.08, 1.55] | large | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.89 | 7 | = 0.540 | 0.43 [-0.51, 0.70] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 1.69 | 7 | = 0.336 | 0.77 [-0.34, 0.79] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 2.55 | 7 | = 0.328 | 0.78 [-0.20, 1.14] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 2.03 | 7 | = 0.328 | 0.97 [0.09, 1.39] | large | n.s. |
| Decrease by 3 vs Increase by 1 | 1.31 | 7 | = 0.419 | 0.41 [-0.03, 1.22] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 0.54 | 7 | = 0.673 | 0.30 [-0.47, 0.98] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 1.47 | 7 | = 0.371 | 0.53 [0.06, 1.62] | medium | n.s. |
| Increase by 1 vs Increase by 2 | -0.42 | 7 | = 0.721 | -0.18 [-0.82, 0.46] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.36 | 7 | = 0.732 | 0.05 [-0.12, 1.17] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.71 | 7 | = 0.608 | 0.27 [-0.15, 1.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 296.57, BIC = 323.21
- **Decrease by 1 vs Cardinality (no change)**: *β* = 0.31, *SE* = 0.299, *z* = 1.033, *p* = 0.302
- **Decrease by 2 vs Cardinality (no change)**: *β* = 0.48, *SE* = 0.285, *z* = 1.701, *p* = 0.089
- **Decrease by 3 vs Cardinality (no change)**: *β* = 0.90, *SE* = 0.297, *z* = 3.023, *p* = 0.003
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.30, *SE* = 0.293, *z* = 1.038, *p* = 0.299
- **Increase by 2 vs Cardinality (no change)**: *β* = 0.36, *SE* = 0.308, *z* = 1.186, *p* = 0.236
- **Increase by 3 vs Cardinality (no change)**: *β* = 0.28, *SE* = 0.289, *z* = 0.980, *p* = 0.327
- **SNR**: *β* = 0.27, *SE* = 0.031, *z* = 8.622, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -0.31 | 0.30 | -1.03 | 0.302 | 0.990 | n.s. |
| Cardinality (no change) - Decrease by 2 | -0.49 | 0.29 | -1.70 | 0.089 | 0.775 | n.s. |
| Cardinality (no change) - Decrease by 3 | -0.90 | 0.30 | -3.02 | 0.003 | 0.051 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.30 | 0.29 | -1.04 | 0.299 | 0.990 | n.s. |
| Cardinality (no change) - Increase by 2 | -0.37 | 0.31 | -1.19 | 0.236 | 0.977 | n.s. |
| Cardinality (no change) - Increase by 3 | -0.28 | 0.29 | -0.98 | 0.327 | 0.990 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.18 | 0.28 | -0.63 | 0.526 | 0.998 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.59 | 0.28 | -2.08 | 0.038 | 0.500 | n.s. |
| Decrease by 1 - Increase by 1 | 0.00 | 0.28 | 0.01 | 0.988 | 1.000 | n.s. |
| Decrease by 1 - Increase by 2 | -0.06 | 0.29 | -0.19 | 0.846 | 1.000 | n.s. |
| Decrease by 1 - Increase by 3 | 0.03 | 0.28 | 0.09 | 0.929 | 1.000 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.41 | 0.27 | -1.53 | 0.125 | 0.865 | n.s. |
| Decrease by 2 - Increase by 1 | 0.18 | 0.26 | 0.69 | 0.489 | 0.998 | n.s. |
| Decrease by 2 - Increase by 2 | 0.12 | 0.28 | 0.42 | 0.674 | 1.000 | n.s. |
| Decrease by 2 - Increase by 3 | 0.20 | 0.27 | 0.75 | 0.453 | 0.998 | n.s. |
| Decrease by 3 - Increase by 1 | 0.59 | 0.27 | 2.22 | 0.026 | 0.412 | n.s. |
| Decrease by 3 - Increase by 2 | 0.53 | 0.29 | 1.82 | 0.069 | 0.704 | n.s. |
| Decrease by 3 - Increase by 3 | 0.61 | 0.28 | 2.20 | 0.028 | 0.418 | n.s. |
| Increase by 1 - Increase by 2 | -0.06 | 0.28 | -0.22 | 0.829 | 1.000 | n.s. |
| Increase by 1 - Increase by 3 | 0.02 | 0.27 | 0.08 | 0.939 | 1.000 | n.s. |
| Increase by 2 - Increase by 3 | 0.08 | 0.29 | 0.28 | 0.777 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.78, *p* = 0.126, η²_G = 0.078
- Greenhouse-Geisser corrected: *p* = 0.196 (ε = 0.397)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -0.04 | 7 | = 0.967 | -0.02 [-0.57, 0.71] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.25 | 7 | = 0.945 | -0.06 [-0.67, 0.60] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.84 | 7 | = 0.639 | -0.29 [-1.09, 0.48] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.67 | 7 | = 0.419 | 0.52 [-0.44, 0.92] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | 0.78 | 7 | = 0.639 | 0.30 [-0.52, 0.84] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 0.73 | 7 | = 0.639 | 0.29 [-0.51, 0.70] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | -0.13 | 7 | = 0.967 | -0.05 [-0.92, 0.38] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.20 | 7 | = 0.565 | -0.29 [-1.36, 0.11] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 2.62 | 7 | = 0.181 | 0.58 [-0.42, 0.87] | medium | n.s. |
| Decrease by 1 vs Increase by 2 | 2.14 | 7 | = 0.293 | 0.34 [-0.32, 0.98] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 1.42 | 7 | = 0.520 | 0.33 [-0.65, 0.62] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.65 | 7 | = 0.663 | -0.28 [-0.82, 0.40] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 1.93 | 7 | = 0.334 | 0.75 [-0.24, 0.90] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 1.09 | 7 | = 0.599 | 0.44 [-0.26, 1.06] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 0.91 | 7 | = 0.639 | 0.44 [-0.45, 0.71] | small | n.s. |
| Decrease by 3 vs Increase by 1 | 3.04 | 7 | = 0.181 | 0.78 [0.03, 1.30] | medium | n.s. |
| Decrease by 3 vs Increase by 2 | 2.74 | 7 | = 0.181 | 0.57 [0.03, 1.71] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | 3.03 | 7 | = 0.181 | 0.57 [0.19, 1.84] | medium | n.s. |
| Increase by 1 vs Increase by 2 | -0.85 | 7 | = 0.639 | -0.23 [-0.67, 0.61] | small | n.s. |
| Increase by 1 vs Increase by 3 | -1.29 | 7 | = 0.557 | -0.24 [-0.97, 0.27] | small | n.s. |
| Increase by 2 vs Increase by 3 | -0.05 | 7 | = 0.967 | -0.01 [-0.79, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1229.21, BIC = 1257.65
- **Decrease by 1 vs Cardinality (no change)**: *β* = 10.84, *SE* = 9.438, *z* = 1.148, *p* = 0.251
- **Decrease by 2 vs Cardinality (no change)**: *β* = -5.20, *SE* = 9.438, *z* = -0.551, *p* = 0.581
- **Decrease by 3 vs Cardinality (no change)**: *β* = 3.78, *SE* = 9.705, *z* = 0.390, *p* = 0.697
- **Increase by 1 vs Cardinality (no change)**: *β* = 17.77, *SE* = 9.589, *z* = 1.853, *p* = 0.064
- **Increase by 2 vs Cardinality (no change)**: *β* = 13.28, *SE* = 9.864, *z* = 1.347, *p* = 0.178
- **Increase by 3 vs Cardinality (no change)**: *β* = 5.07, *SE* = 9.067, *z* = 0.559, *p* = 0.576
- **SNR**: *β* = 0.54, *SE* = 0.592, *z* = 0.908, *p* = 0.364

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -10.84 | 9.44 | -1.15 | 0.251 | 0.977 | n.s. |
| Cardinality (no change) - Decrease by 2 | 5.20 | 9.44 | 0.55 | 0.581 | 0.994 | n.s. |
| Cardinality (no change) - Decrease by 3 | -3.78 | 9.70 | -0.39 | 0.697 | 0.994 | n.s. |
| Cardinality (no change) - Increase by 1 | -17.77 | 9.59 | -1.85 | 0.064 | 0.695 | n.s. |
| Cardinality (no change) - Increase by 2 | -13.28 | 9.86 | -1.35 | 0.178 | 0.947 | n.s. |
| Cardinality (no change) - Increase by 3 | -5.07 | 9.07 | -0.56 | 0.576 | 0.994 | n.s. |
| Decrease by 1 - Decrease by 2 | 16.04 | 8.24 | 1.95 | 0.052 | 0.634 | n.s. |
| Decrease by 1 - Decrease by 3 | 7.06 | 8.31 | 0.85 | 0.396 | 0.989 | n.s. |
| Decrease by 1 - Increase by 1 | -6.93 | 8.52 | -0.81 | 0.416 | 0.989 | n.s. |
| Decrease by 1 - Increase by 2 | -2.45 | 8.39 | -0.29 | 0.771 | 0.994 | n.s. |
| Decrease by 1 - Increase by 3 | 5.77 | 8.10 | 0.71 | 0.476 | 0.989 | n.s. |
| Decrease by 2 - Decrease by 3 | -8.99 | 8.27 | -1.09 | 0.277 | 0.977 | n.s. |
| Decrease by 2 - Increase by 1 | -22.97 | 8.53 | -2.69 | 0.007 | 0.138 | n.s. |
| Decrease by 2 - Increase by 2 | -18.49 | 8.44 | -2.19 | 0.029 | 0.440 | n.s. |
| Decrease by 2 - Increase by 3 | -10.27 | 8.09 | -1.27 | 0.204 | 0.959 | n.s. |
| Decrease by 3 - Increase by 1 | -13.99 | 8.58 | -1.63 | 0.103 | 0.843 | n.s. |
| Decrease by 3 - Increase by 2 | -9.50 | 8.43 | -1.13 | 0.260 | 0.977 | n.s. |
| Decrease by 3 - Increase by 3 | -1.29 | 8.18 | -0.16 | 0.875 | 0.994 | n.s. |
| Increase by 1 - Increase by 2 | 4.49 | 8.69 | 0.52 | 0.606 | 0.994 | n.s. |
| Increase by 1 - Increase by 3 | 12.70 | 8.36 | 1.52 | 0.129 | 0.889 | n.s. |
| Increase by 2 - Increase by 3 | 8.21 | 8.40 | 0.98 | 0.329 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.250, η²_G = 0.055
- Greenhouse-Geisser corrected: *p* = 0.274 (ε = 0.554)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.77 | 12 | = 0.634 | -0.61 [-1.08, 0.14] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 | 0.13 | 12 | = 0.945 | 0.05 [-0.50, 0.66] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.38 | 12 | = 0.839 | -0.14 [-0.71, 0.50] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | -1.51 | 12 | = 0.634 | -0.58 [-1.05, 0.21] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | -0.65 | 12 | = 0.787 | -0.26 [-0.87, 0.31] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | -0.31 | 12 | = 0.839 | -0.12 [-0.77, 0.40] | negligible | n.s. |
| Decrease by 1 vs Decrease by 2 | 2.51 | 12 | = 0.513 | 0.59 [0.15, 1.26] | medium | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.28 | 12 | = 0.634 | 0.43 [-0.21, 0.84] | small | n.s. |
| Decrease by 1 vs Increase by 1 | -0.35 | 12 | = 0.839 | -0.09 [-0.64, 0.43] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 1.23 | 12 | = 0.634 | 0.31 [-0.62, 0.38] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 1.11 | 12 | = 0.634 | 0.38 [-0.38, 0.59] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.60 | 12 | = 0.787 | -0.17 [-0.76, 0.25] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | -2.19 | 12 | = 0.513 | -0.57 [-1.15, 0.00] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | -0.94 | 12 | = 0.696 | -0.27 [-1.02, 0.06] | small | n.s. |
| Decrease by 2 vs Increase by 3 | -0.56 | 12 | = 0.787 | -0.15 [-0.70, 0.27] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | -1.28 | 12 | = 0.634 | -0.44 [-0.96, 0.14] | small | n.s. |
| Decrease by 3 vs Increase by 2 | -0.58 | 12 | = 0.787 | -0.11 [-0.93, 0.17] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 0.00 | 12 | = 1.000 | 0.00 [-0.38, 0.59] | negligible | n.s. |
| Increase by 1 vs Increase by 2 | 1.08 | 12 | = 0.634 | 0.34 [-0.39, 0.68] | small | n.s. |
| Increase by 1 vs Increase by 3 | 1.16 | 12 | = 0.634 | 0.41 [-0.13, 0.94] | small | n.s. |
| Increase by 2 vs Increase by 3 | 0.54 | 12 | = 0.787 | 0.10 [-0.14, 0.89] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 462.81, BIC = 491.25
- **Decrease by 1 vs Cardinality (no change)**: *β* = 2.08, *SE* = 0.423, *z* = 4.916, *p* < .001
- **Decrease by 2 vs Cardinality (no change)**: *β* = 1.91, *SE* = 0.422, *z* = 4.536, *p* < .001
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.31, *SE* = 0.438, *z* = 5.266, *p* < .001
- **Increase by 1 vs Cardinality (no change)**: *β* = 1.49, *SE* = 0.428, *z* = 3.493, *p* < .001
- **Increase by 2 vs Cardinality (no change)**: *β* = 1.92, *SE* = 0.444, *z* = 4.318, *p* < .001
- **Increase by 3 vs Cardinality (no change)**: *β* = 1.86, *SE* = 0.406, *z* = 4.594, *p* < .001
- **SNR**: *β* = 0.18, *SE* = 0.029, *z* = 6.470, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -2.08 | 0.42 | -4.92 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 2 | -1.91 | 0.42 | -4.54 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 3 | -2.31 | 0.44 | -5.27 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 1 | -1.49 | 0.43 | -3.49 | < .001 | 0.008 | ** |
| Cardinality (no change) - Increase by 2 | -1.92 | 0.44 | -4.32 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 3 | -1.86 | 0.41 | -4.59 | < .001 | < .001 | *** |
| Decrease by 1 - Decrease by 2 | 0.16 | 0.36 | 0.45 | 0.653 | 0.995 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.23 | 0.37 | -0.63 | 0.529 | 0.995 | n.s. |
| Decrease by 1 - Increase by 1 | 0.58 | 0.38 | 1.55 | 0.120 | 0.834 | n.s. |
| Decrease by 1 - Increase by 2 | 0.16 | 0.37 | 0.43 | 0.664 | 0.995 | n.s. |
| Decrease by 1 - Increase by 3 | 0.21 | 0.36 | 0.60 | 0.551 | 0.995 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.39 | 0.37 | -1.08 | 0.281 | 0.974 | n.s. |
| Decrease by 2 - Increase by 1 | 0.42 | 0.38 | 1.12 | 0.263 | 0.974 | n.s. |
| Decrease by 2 - Increase by 2 | -0.00 | 0.37 | -0.01 | 0.995 | 0.999 | n.s. |
| Decrease by 2 - Increase by 3 | 0.05 | 0.36 | 0.14 | 0.889 | 0.999 | n.s. |
| Decrease by 3 - Increase by 1 | 0.81 | 0.38 | 2.15 | 0.032 | 0.384 | n.s. |
| Decrease by 3 - Increase by 2 | 0.39 | 0.37 | 1.05 | 0.293 | 0.974 | n.s. |
| Decrease by 3 - Increase by 3 | 0.44 | 0.36 | 1.23 | 0.219 | 0.960 | n.s. |
| Increase by 1 - Increase by 2 | -0.42 | 0.38 | -1.10 | 0.270 | 0.974 | n.s. |
| Increase by 1 - Increase by 3 | -0.37 | 0.37 | -1.01 | 0.313 | 0.974 | n.s. |
| Increase by 2 - Increase by 3 | 0.05 | 0.37 | 0.14 | 0.888 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.71, *p* < .001, η²_G = 0.195
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -4.29 | 12 | = 0.008 | -1.59 [-1.78, -0.34] | large | ** |
| Cardinality (no change) vs Decrease by 2 | -4.66 | 12 | = 0.008 | -1.68 [-1.97, -0.45] | large | ** |
| Cardinality (no change) vs Decrease by 3 | -4.11 | 12 | = 0.008 | -1.62 [-1.92, -0.36] | large | ** |
| Cardinality (no change) vs Increase by 1 | -2.88 | 12 | = 0.048 | -1.09 [-1.49, -0.11] | large | * |
| Cardinality (no change) vs Increase by 2 | -4.17 | 12 | = 0.008 | -1.44 [-1.80, -0.35] | large | ** |
| Cardinality (no change) vs Increase by 3 | -3.56 | 12 | = 0.017 | -1.32 [-1.65, -0.26] | large | * |
| Decrease by 1 vs Decrease by 2 | 0.81 | 12 | = 0.509 | 0.15 [-0.32, 0.68] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.06 | 12 | = 0.409 | -0.19 [-0.86, 0.19] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 2.66 | 12 | = 0.056 | 0.30 [0.22, 1.46] | small | n.s. |
| Decrease by 1 vs Increase by 2 | -0.15 | 12 | = 0.886 | -0.02 [-0.63, 0.37] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 1.46 | 12 | = 0.323 | 0.17 [-0.08, 0.92] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.39 | 12 | = 0.333 | -0.34 [-0.84, 0.19] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 1.14 | 12 | = 0.388 | 0.20 [-0.18, 0.92] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | -0.73 | 12 | = 0.528 | -0.16 [-0.70, 0.33] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | 0.20 | 12 | = 0.886 | 0.04 [-0.28, 0.69] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | 2.64 | 12 | = 0.056 | 0.46 [0.06, 1.23] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 0.81 | 12 | = 0.509 | 0.15 [-0.31, 0.77] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 1.97 | 12 | = 0.152 | 0.34 [0.10, 1.16] | small | n.s. |
| Increase by 1 vs Increase by 2 | -2.03 | 12 | = 0.152 | -0.30 [-1.26, -0.08] | small | n.s. |
| Increase by 1 vs Increase by 3 | -1.23 | 12 | = 0.383 | -0.14 [-0.82, 0.23] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 1.19 | 12 | = 0.383 | 0.18 [-0.11, 0.93] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.032) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* = 0.003) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed greater amplitude than Increase by 2 (*d* = 0.45)
  - Cardinality (no change) showed greater amplitude than Increase by 3 (*d* = 0.78)
  - Decrease by 1 showed greater amplitude than Increase by 3 (*d* = 0.69)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.068)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller amplitude than Decrease by 1 (*d* = -1.59)
  - Cardinality (no change) showed smaller amplitude than Decrease by 2 (*d* = -1.68)
  - Cardinality (no change) showed smaller amplitude than Decrease by 3 (*d* = -1.62)
  - Cardinality (no change) showed smaller amplitude than Increase by 1 (*d* = -1.09)
  - Cardinality (no change) showed smaller amplitude than Increase by 2 (*d* = -1.44)
  - Cardinality (no change) showed smaller amplitude than Increase by 3 (*d* = -1.32)

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
