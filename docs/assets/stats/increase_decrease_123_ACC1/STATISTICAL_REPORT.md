# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:24:56

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
| Decrease by 1 | 24 | 106.17 ms | 8.90 | 1.82 | [92.00, 116.00] |
| Decrease by 2 | 24 | 107.00 ms | 9.08 | 1.85 | [92.00, 116.00] |
| Decrease by 3 | 24 | 104.83 ms | 9.29 | 1.90 | [92.00, 116.00] |
| Increase by 1 | 24 | 102.17 ms | 9.73 | 1.99 | [92.00, 116.00] |
| Increase by 2 | 24 | 102.00 ms | 9.14 | 1.87 | [92.00, 116.00] |
| Increase by 3 | 24 | 102.00 ms | 8.83 | 1.80 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -1.28 µV | 1.38 | 0.28 | [-4.83, 0.55] |
| Decrease by 1 | 24 | -1.00 µV | 1.40 | 0.29 | [-4.56, 1.16] |
| Decrease by 2 | 24 | -1.46 µV | 1.25 | 0.26 | [-4.30, 2.02] |
| Decrease by 3 | 24 | -1.78 µV | 1.87 | 0.38 | [-6.39, 1.69] |
| Increase by 1 | 24 | -1.14 µV | 1.28 | 0.26 | [-3.74, 0.92] |
| Increase by 2 | 24 | -1.03 µV | 1.25 | 0.26 | [-4.17, 0.52] |
| Increase by 3 | 24 | -1.13 µV | 1.22 | 0.25 | [-3.35, 1.12] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 175.83 ms | 17.11 | 3.49 | [144.00, 208.00] |
| Decrease by 1 | 24 | 179.00 ms | 14.74 | 3.01 | [152.00, 208.00] |
| Decrease by 2 | 24 | 177.33 ms | 14.53 | 2.97 | [144.00, 208.00] |
| Decrease by 3 | 24 | 177.00 ms | 15.02 | 3.07 | [152.00, 208.00] |
| Increase by 1 | 24 | 171.17 ms | 20.26 | 4.14 | [144.00, 208.00] |
| Increase by 2 | 24 | 168.83 ms | 18.42 | 3.76 | [144.00, 200.00] |
| Increase by 3 | 24 | 171.83 ms | 19.82 | 4.05 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -4.62 µV | 2.14 | 0.44 | [-9.57, -0.60] |
| Decrease by 1 | 24 | -4.90 µV | 2.05 | 0.42 | [-9.90, -1.23] |
| Decrease by 2 | 24 | -5.13 µV | 2.10 | 0.43 | [-9.59, -1.53] |
| Decrease by 3 | 24 | -5.22 µV | 1.97 | 0.40 | [-8.60, -1.48] |
| Increase by 1 | 24 | -5.08 µV | 2.11 | 0.43 | [-9.46, -0.80] |
| Increase by 2 | 24 | -5.47 µV | 2.43 | 0.50 | [-11.28, -1.22] |
| Increase by 3 | 24 | -6.17 µV | 2.54 | 0.52 | [-12.86, -2.17] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 106.00 ms | 10.55 | 2.15 | [92.00, 116.00] |
| Decrease by 1 | 24 | 108.50 ms | 9.68 | 1.98 | [92.00, 116.00] |
| Decrease by 2 | 24 | 109.50 ms | 8.32 | 1.70 | [92.00, 116.00] |
| Decrease by 3 | 24 | 107.33 ms | 9.03 | 1.84 | [92.00, 116.00] |
| Increase by 1 | 24 | 103.67 ms | 9.50 | 1.94 | [92.00, 116.00] |
| Increase by 2 | 24 | 103.00 ms | 9.60 | 1.96 | [92.00, 116.00] |
| Increase by 3 | 24 | 100.50 ms | 9.31 | 1.90 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.27 µV | 1.86 | 0.38 | [-1.29, 5.73] |
| Decrease by 1 | 24 | 1.09 µV | 1.88 | 0.38 | [-1.32, 5.23] |
| Decrease by 2 | 24 | 1.53 µV | 1.78 | 0.36 | [-2.32, 5.74] |
| Decrease by 3 | 24 | 1.94 µV | 2.07 | 0.42 | [-1.76, 8.15] |
| Increase by 1 | 24 | 1.32 µV | 1.67 | 0.34 | [-1.63, 4.44] |
| Increase by 2 | 24 | 1.10 µV | 1.60 | 0.33 | [-1.42, 4.70] |
| Increase by 3 | 24 | 1.39 µV | 1.66 | 0.34 | [-1.07, 5.27] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 463.50 ms | 24.86 | 5.08 | [420.00, 516.00] |
| Decrease by 1 | 24 | 486.17 ms | 32.26 | 6.58 | [420.00, 532.00] |
| Decrease by 2 | 24 | 472.33 ms | 32.06 | 6.54 | [420.00, 532.00] |
| Decrease by 3 | 24 | 480.17 ms | 33.08 | 6.75 | [420.00, 532.00] |
| Increase by 1 | 24 | 484.50 ms | 40.40 | 8.25 | [420.00, 532.00] |
| Increase by 2 | 24 | 487.67 ms | 33.40 | 6.82 | [428.00, 532.00] |
| Increase by 3 | 24 | 478.50 ms | 36.06 | 7.36 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.14 µV | 2.72 | 0.56 | [-4.85, 5.95] |
| Decrease by 1 | 24 | 4.11 µV | 3.08 | 0.63 | [-2.27, 9.87] |
| Decrease by 2 | 24 | 3.81 µV | 2.92 | 0.60 | [-1.68, 8.68] |
| Decrease by 3 | 24 | 4.36 µV | 3.49 | 0.71 | [-1.21, 12.38] |
| Increase by 1 | 24 | 3.02 µV | 3.58 | 0.73 | [-3.53, 10.19] |
| Increase by 2 | 24 | 4.01 µV | 3.47 | 0.71 | [-2.36, 10.55] |
| Increase by 3 | 24 | 3.96 µV | 2.76 | 0.56 | [0.21, 10.15] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1166.66, BIC = 1197.90
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.50, *SE* = 1.853, *z* = -0.272, *p* = 0.785
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.05, *SE* = 1.837, *z* = -0.027, *p* = 0.979
- **Decrease by 3 vs Cardinality (no change)**: *β* = -2.49, *SE* = 1.838, *z* = -1.356, *p* = 0.175
- **Increase by 1 vs Cardinality (no change)**: *β* = -4.68, *SE* = 1.843, *z* = -2.538, *p* = 0.011
- **Increase by 2 vs Cardinality (no change)**: *β* = -4.74, *SE* = 1.848, *z* = -2.566, *p* = 0.010
- **Increase by 3 vs Cardinality (no change)**: *β* = -4.73, *SE* = 1.849, *z* = -2.559, *p* = 0.010
- **SNR**: *β* = 0.68, *SE* = 0.343, *z* = 1.989, *p* = 0.047

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.50 | 1.85 | 0.27 | 0.785 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.05 | 1.84 | 0.03 | 0.979 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 | 2.49 | 1.84 | 1.36 | 0.175 | 0.901 | n.s. |
| Cardinality (no change) - Increase by 1 | 4.68 | 1.84 | 2.54 | 0.011 | 0.195 | n.s. |
| Cardinality (no change) - Increase by 2 | 4.74 | 1.85 | 2.57 | 0.010 | 0.195 | n.s. |
| Cardinality (no change) - Increase by 3 | 4.73 | 1.85 | 2.56 | 0.010 | 0.195 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.46 | 1.85 | -0.25 | 0.805 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 3 | 1.99 | 1.87 | 1.07 | 0.286 | 0.923 | n.s. |
| Decrease by 1 - Increase by 1 | 4.17 | 1.84 | 2.27 | 0.023 | 0.272 | n.s. |
| Decrease by 1 - Increase by 2 | 4.24 | 1.84 | 2.31 | 0.021 | 0.272 | n.s. |
| Decrease by 1 - Increase by 3 | 4.23 | 1.84 | 2.30 | 0.021 | 0.272 | n.s. |
| Decrease by 2 - Decrease by 3 | 2.44 | 1.84 | 1.33 | 0.184 | 0.901 | n.s. |
| Decrease by 2 - Increase by 1 | 4.63 | 1.84 | 2.52 | 0.012 | 0.195 | n.s. |
| Decrease by 2 - Increase by 2 | 4.69 | 1.84 | 2.55 | 0.011 | 0.195 | n.s. |
| Decrease by 2 - Increase by 3 | 4.68 | 1.84 | 2.54 | 0.011 | 0.195 | n.s. |
| Decrease by 3 - Increase by 1 | 2.18 | 1.85 | 1.18 | 0.238 | 0.923 | n.s. |
| Decrease by 3 - Increase by 2 | 2.25 | 1.86 | 1.21 | 0.226 | 0.923 | n.s. |
| Decrease by 3 - Increase by 3 | 2.24 | 1.86 | 1.20 | 0.229 | 0.923 | n.s. |
| Increase by 1 - Increase by 2 | 0.07 | 1.84 | 0.04 | 0.971 | 1.000 | n.s. |
| Increase by 1 - Increase by 3 | 0.05 | 1.84 | 0.03 | 0.976 | 1.000 | n.s. |
| Increase by 2 - Increase by 3 | -0.01 | 1.84 | -0.01 | 0.995 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.17, *p* = 0.006, η²_G = 0.058
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.92 | 23 | = 0.512 | 0.11 [-0.24, 0.61] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | 0.11 | 23 | = 0.981 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.07 | 23 | = 0.459 | 0.26 [-0.21, 0.65] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 2.85 | 23 | = 0.064 | 0.53 [0.12, 1.04] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.88 | 23 | = 0.064 | 0.57 [0.13, 1.05] | medium | n.s. |
| Cardinality (no change) vs Increase by 3 | 3.71 | 23 | = 0.024 | 0.58 [0.28, 1.24] | medium | * |
| Decrease by 1 vs Decrease by 2 | -0.48 | 23 | = 0.785 | -0.09 [-0.52, 0.33] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.57 | 23 | = 0.752 | 0.15 [-0.31, 0.54] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 2.24 | 23 | = 0.092 | 0.43 [0.01, 0.90] | small | n.s. |
| Decrease by 1 vs Increase by 2 | 2.34 | 23 | = 0.084 | 0.46 [0.03, 0.92] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 2.66 | 23 | = 0.066 | 0.47 [0.09, 0.99] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | 1.05 | 23 | = 0.459 | 0.24 [-0.21, 0.64] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 2.07 | 23 | = 0.116 | 0.51 [-0.02, 0.86] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 2.38 | 23 | = 0.084 | 0.55 [0.04, 0.93] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 2.61 | 23 | = 0.066 | 0.56 [0.08, 0.98] | medium | n.s. |
| Decrease by 3 vs Increase by 1 | 1.13 | 23 | = 0.459 | 0.28 [-0.20, 0.66] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 1.23 | 23 | = 0.441 | 0.31 [-0.18, 0.68] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 1.38 | 23 | = 0.378 | 0.31 [-0.15, 0.71] | small | n.s. |
| Increase by 1 vs Increase by 2 | 0.08 | 23 | = 0.981 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.12 | 23 | = 0.981 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 521.67, BIC = 552.91
- **Decrease by 1 vs Cardinality (no change)**: *β* = 0.10, *SE* = 0.277, *z* = 0.374, *p* = 0.708
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.23, *SE* = 0.275, *z* = -0.820, *p* = 0.412
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.45, *SE* = 0.275, *z* = -1.636, *p* = 0.102
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.02, *SE* = 0.276, *z* = 0.072, *p* = 0.942
- **Increase by 2 vs Cardinality (no change)**: *β* = 0.10, *SE* = 0.277, *z* = 0.363, *p* = 0.717
- **Increase by 3 vs Cardinality (no change)**: *β* = -0.01, *SE* = 0.277, *z* = -0.036, *p* = 0.971
- **SNR**: *β* = -0.24, *SE* = 0.052, *z* = -4.626, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -0.10 | 0.28 | -0.37 | 0.708 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.23 | 0.27 | 0.82 | 0.412 | 0.999 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.45 | 0.28 | 1.64 | 0.102 | 0.855 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.02 | 0.28 | -0.07 | 0.942 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 | -0.10 | 0.28 | -0.36 | 0.717 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 | 0.01 | 0.28 | 0.04 | 0.971 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 2 | 0.33 | 0.28 | 1.19 | 0.233 | 0.986 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.55 | 0.28 | 1.98 | 0.047 | 0.639 | n.s. |
| Decrease by 1 - Increase by 1 | 0.08 | 0.28 | 0.30 | 0.761 | 1.000 | n.s. |
| Decrease by 1 - Increase by 2 | 0.00 | 0.27 | 0.01 | 0.990 | 1.000 | n.s. |
| Decrease by 1 - Increase by 3 | 0.11 | 0.27 | 0.41 | 0.679 | 1.000 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.22 | 0.28 | 0.81 | 0.415 | 0.999 | n.s. |
| Decrease by 2 - Increase by 1 | -0.25 | 0.28 | -0.89 | 0.372 | 0.999 | n.s. |
| Decrease by 2 - Increase by 2 | -0.33 | 0.28 | -1.18 | 0.237 | 0.986 | n.s. |
| Decrease by 2 - Increase by 3 | -0.22 | 0.28 | -0.78 | 0.434 | 0.999 | n.s. |
| Decrease by 3 - Increase by 1 | -0.47 | 0.28 | -1.70 | 0.090 | 0.833 | n.s. |
| Decrease by 3 - Increase by 2 | -0.55 | 0.28 | -1.98 | 0.048 | 0.639 | n.s. |
| Decrease by 3 - Increase by 3 | -0.44 | 0.28 | -1.58 | 0.114 | 0.872 | n.s. |
| Increase by 1 - Increase by 2 | -0.08 | 0.27 | -0.29 | 0.770 | 1.000 | n.s. |
| Increase by 1 - Increase by 3 | 0.03 | 0.27 | 0.11 | 0.913 | 1.000 | n.s. |
| Increase by 2 - Increase by 3 | 0.11 | 0.27 | 0.40 | 0.688 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.81, *p* = 0.101, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -0.99 | 23 | = 0.638 | -0.20 [-0.63, 0.23] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | 0.79 | 23 | = 0.709 | 0.14 [-0.26, 0.59] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.68 | 23 | = 0.366 | 0.31 [-0.09, 0.78] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | -0.52 | 23 | = 0.779 | -0.10 [-0.53, 0.32] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 | -1.25 | 23 | = 0.589 | -0.19 [-0.68, 0.17] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 | -0.48 | 23 | = 0.779 | -0.11 [-0.52, 0.33] | negligible | n.s. |
| Decrease by 1 vs Decrease by 2 | 1.66 | 23 | = 0.366 | 0.35 [-0.10, 0.77] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | 2.35 | 23 | = 0.279 | 0.48 [0.03, 0.93] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 0.52 | 23 | = 0.779 | 0.11 [-0.32, 0.53] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 0.16 | 23 | = 0.916 | 0.02 [-0.39, 0.46] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 0.43 | 23 | = 0.779 | 0.10 [-0.33, 0.51] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.88 | 23 | = 0.677 | 0.20 [-0.25, 0.61] | small | n.s. |
| Decrease by 2 vs Increase by 1 | -1.08 | 23 | = 0.624 | -0.25 [-0.65, 0.21] | small | n.s. |
| Decrease by 2 vs Increase by 2 | -1.61 | 23 | = 0.366 | -0.35 [-0.76, 0.11] | small | n.s. |
| Decrease by 2 vs Increase by 3 | -1.07 | 23 | = 0.624 | -0.27 [-0.64, 0.21] | small | n.s. |
| Decrease by 3 vs Increase by 1 | -2.18 | 23 | = 0.279 | -0.40 [-0.89, -0.00] | small | n.s. |
| Decrease by 3 vs Increase by 2 | -2.39 | 23 | = 0.279 | -0.48 [-0.93, -0.04] | small | n.s. |
| Decrease by 3 vs Increase by 3 | -1.73 | 23 | = 0.366 | -0.41 [-0.79, 0.08] | small | n.s. |
| Increase by 1 vs Increase by 2 | -0.45 | 23 | = 0.779 | -0.09 [-0.52, 0.33] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.03 | 23 | = 0.976 | -0.01 [-0.43, 0.42] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.34 | 23 | = 0.817 | 0.09 [-0.35, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1331.65, BIC = 1362.89
- **Decrease by 1 vs Cardinality (no change)**: *β* = 3.17, *SE* = 2.865, *z* = 1.106, *p* = 0.269
- **Decrease by 2 vs Cardinality (no change)**: *β* = 1.54, *SE* = 2.873, *z* = 0.536, *p* = 0.592
- **Decrease by 3 vs Cardinality (no change)**: *β* = 1.22, *SE* = 2.880, *z* = 0.424, *p* = 0.671
- **Increase by 1 vs Cardinality (no change)**: *β* = -4.59, *SE* = 2.895, *z* = -1.584, *p* = 0.113
- **Increase by 2 vs Cardinality (no change)**: *β* = -6.93, *SE* = 2.890, *z* = -2.397, *p* = 0.017
- **Increase by 3 vs Cardinality (no change)**: *β* = -3.95, *SE* = 2.876, *z* = -1.374, *p* = 0.169
- **SNR**: *β* = -0.04, *SE* = 0.206, *z* = -0.192, *p* = 0.848

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -3.17 | 2.87 | -1.11 | 0.269 | 0.940 | n.s. |
| Cardinality (no change) - Decrease by 2 | -1.54 | 2.87 | -0.54 | 0.592 | 0.985 | n.s. |
| Cardinality (no change) - Decrease by 3 | -1.22 | 2.88 | -0.42 | 0.671 | 0.985 | n.s. |
| Cardinality (no change) - Increase by 1 | 4.59 | 2.90 | 1.58 | 0.113 | 0.733 | n.s. |
| Cardinality (no change) - Increase by 2 | 6.93 | 2.89 | 2.40 | 0.017 | 0.234 | n.s. |
| Cardinality (no change) - Increase by 3 | 3.95 | 2.88 | 1.37 | 0.169 | 0.844 | n.s. |
| Decrease by 1 - Decrease by 2 | 1.63 | 2.87 | 0.57 | 0.571 | 0.985 | n.s. |
| Decrease by 1 - Decrease by 3 | 1.95 | 2.88 | 0.68 | 0.499 | 0.984 | n.s. |
| Decrease by 1 - Increase by 1 | 7.75 | 2.89 | 2.68 | 0.007 | 0.125 | n.s. |
| Decrease by 1 - Increase by 2 | 10.10 | 2.89 | 3.49 | < .001 | 0.010 | ** |
| Decrease by 1 - Increase by 3 | 7.12 | 2.88 | 2.48 | 0.013 | 0.203 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.32 | 2.87 | 0.11 | 0.912 | 0.985 | n.s. |
| Decrease by 2 - Increase by 1 | 6.13 | 2.87 | 2.13 | 0.033 | 0.395 | n.s. |
| Decrease by 2 - Increase by 2 | 8.47 | 2.87 | 2.95 | 0.003 | 0.062 | n.s. |
| Decrease by 2 - Increase by 3 | 5.49 | 2.87 | 1.92 | 0.055 | 0.523 | n.s. |
| Decrease by 3 - Increase by 1 | 5.81 | 2.87 | 2.03 | 0.043 | 0.458 | n.s. |
| Decrease by 3 - Increase by 2 | 8.15 | 2.87 | 2.84 | 0.004 | 0.082 | n.s. |
| Decrease by 3 - Increase by 3 | 5.17 | 2.87 | 1.81 | 0.071 | 0.587 | n.s. |
| Increase by 1 - Increase by 2 | 2.34 | 2.87 | 0.82 | 0.414 | 0.976 | n.s. |
| Increase by 1 - Increase by 3 | -0.63 | 2.87 | -0.22 | 0.825 | 0.985 | n.s. |
| Increase by 2 - Increase by 3 | -2.98 | 2.87 | -1.04 | 0.300 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.37, *p* = 0.004, η²_G = 0.041
- Greenhouse-Geisser corrected: *p* = 0.020 (ε = 0.535)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.42 | 23 | = 0.274 | -0.20 [-0.72, 0.14] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.66 | 23 | = 0.601 | -0.09 [-0.56, 0.29] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.35 | 23 | = 0.805 | -0.07 [-0.49, 0.35] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.62 | 23 | = 0.248 | 0.25 [-0.10, 0.76] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.46 | 23 | = 0.098 | 0.39 [0.05, 0.95] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 1.27 | 23 | = 0.323 | 0.22 [-0.17, 0.69] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 0.73 | 23 | = 0.584 | 0.11 [-0.28, 0.57] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.95 | 23 | = 0.460 | 0.13 [-0.23, 0.62] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 2.43 | 23 | = 0.098 | 0.44 [0.05, 0.94] | small | n.s. |
| Decrease by 1 vs Increase by 2 | 3.49 | 23 | = 0.041 | 0.61 [0.24, 1.19] | medium | * |
| Decrease by 1 vs Increase by 3 | 2.29 | 23 | = 0.110 | 0.41 [0.02, 0.91] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.12 | 23 | = 0.906 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 1.69 | 23 | = 0.248 | 0.35 [-0.09, 0.78] | small | n.s. |
| Decrease by 2 vs Increase by 2 | 2.75 | 23 | = 0.098 | 0.51 [0.11, 1.01] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 1.56 | 23 | = 0.253 | 0.32 [-0.11, 0.75] | small | n.s. |
| Decrease by 3 vs Increase by 1 | 1.43 | 23 | = 0.274 | 0.33 [-0.14, 0.72] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 2.50 | 23 | = 0.098 | 0.49 [0.06, 0.96] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 1.63 | 23 | = 0.248 | 0.29 [-0.10, 0.77] | small | n.s. |
| Increase by 1 vs Increase by 2 | 1.09 | 23 | = 0.401 | 0.12 [-0.20, 0.65] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.26 | 23 | = 0.840 | -0.03 [-0.47, 0.37] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.99 | 23 | = 0.176 | -0.16 [-0.85, 0.03] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 587.36, BIC = 618.60
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.27, *SE* = 0.309, *z* = -0.873, *p* = 0.383
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.40, *SE* = 0.310, *z* = -1.279, *p* = 0.201
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.44, *SE* = 0.311, *z* = -1.407, *p* = 0.159
- **Increase by 1 vs Cardinality (no change)**: *β* = -0.23, *SE* = 0.312, *z* = -0.737, *p* = 0.461
- **Increase by 2 vs Cardinality (no change)**: *β* = -0.64, *SE* = 0.312, *z* = -2.036, *p* = 0.042
- **Increase by 3 vs Cardinality (no change)**: *β* = -1.41, *SE* = 0.310, *z* = -4.552, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.022, *z* = -5.045, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.27 | 0.31 | 0.87 | 0.383 | 0.992 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.40 | 0.31 | 1.28 | 0.201 | 0.936 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.44 | 0.31 | 1.41 | 0.159 | 0.912 | n.s. |
| Cardinality (no change) - Increase by 1 | 0.23 | 0.31 | 0.74 | 0.461 | 0.995 | n.s. |
| Cardinality (no change) - Increase by 2 | 0.64 | 0.31 | 2.04 | 0.042 | 0.472 | n.s. |
| Cardinality (no change) - Increase by 3 | 1.41 | 0.31 | 4.55 | < .001 | < .001 | *** |
| Decrease by 1 - Decrease by 2 | 0.13 | 0.31 | 0.41 | 0.683 | 0.995 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.17 | 0.31 | 0.54 | 0.590 | 0.995 | n.s. |
| Decrease by 1 - Increase by 1 | -0.04 | 0.31 | -0.13 | 0.899 | 0.995 | n.s. |
| Decrease by 1 - Increase by 2 | 0.37 | 0.31 | 1.17 | 0.241 | 0.952 | n.s. |
| Decrease by 1 - Increase by 3 | 1.14 | 0.31 | 3.68 | < .001 | 0.004 | ** |
| Decrease by 2 - Decrease by 3 | 0.04 | 0.31 | 0.13 | 0.895 | 0.995 | n.s. |
| Decrease by 2 - Increase by 1 | -0.17 | 0.31 | -0.54 | 0.592 | 0.995 | n.s. |
| Decrease by 2 - Increase by 2 | 0.24 | 0.31 | 0.77 | 0.441 | 0.995 | n.s. |
| Decrease by 2 - Increase by 3 | 1.02 | 0.31 | 3.29 | 0.001 | 0.018 | * |
| Decrease by 3 - Increase by 1 | -0.21 | 0.31 | -0.67 | 0.504 | 0.995 | n.s. |
| Decrease by 3 - Increase by 2 | 0.20 | 0.31 | 0.64 | 0.523 | 0.995 | n.s. |
| Decrease by 3 - Increase by 3 | 0.98 | 0.31 | 3.15 | 0.002 | 0.027 | * |
| Increase by 1 - Increase by 2 | 0.40 | 0.31 | 1.31 | 0.191 | 0.936 | n.s. |
| Increase by 1 - Increase by 3 | 1.18 | 0.31 | 3.82 | < .001 | 0.003 | ** |
| Increase by 2 - Increase by 3 | 0.78 | 0.31 | 2.51 | 0.012 | 0.175 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.29, *p* < .001, η²_G = 0.043
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 1.06 | 23 | = 0.473 | 0.13 [-0.21, 0.64] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | 1.58 | 23 | = 0.250 | 0.24 [-0.11, 0.76] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.87 | 23 | = 0.174 | 0.29 [-0.06, 0.82] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.57 | 23 | = 0.250 | 0.22 [-0.11, 0.75] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 3.06 | 23 | = 0.039 | 0.37 [0.16, 1.09] | small | * |
| Cardinality (no change) vs Increase by 3 | 5.01 | 23 | < .001 | 0.66 [0.50, 1.54] | medium | *** |
| Decrease by 1 vs Decrease by 2 | 0.76 | 23 | = 0.596 | 0.11 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.03 | 23 | = 0.473 | 0.16 [-0.22, 0.64] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 0.66 | 23 | = 0.621 | 0.09 [-0.29, 0.56] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 2.41 | 23 | = 0.086 | 0.25 [0.04, 0.94] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 3.46 | 23 | = 0.022 | 0.55 [0.23, 1.18] | medium | * |
| Decrease by 2 vs Decrease by 3 | 0.29 | 23 | = 0.815 | 0.04 [-0.36, 0.48] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | -0.14 | 23 | = 0.890 | -0.02 [-0.45, 0.39] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | 0.79 | 23 | = 0.596 | 0.15 [-0.26, 0.59] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | 2.59 | 23 | = 0.069 | 0.45 [0.08, 0.98] | small | n.s. |
| Decrease by 3 vs Increase by 1 | -0.40 | 23 | = 0.768 | -0.07 [-0.50, 0.34] | negligible | n.s. |
| Decrease by 3 vs Increase by 2 | 0.63 | 23 | = 0.621 | 0.11 [-0.29, 0.55] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 2.15 | 23 | = 0.110 | 0.42 [-0.00, 0.88] | small | n.s. |
| Increase by 1 vs Increase by 2 | 1.24 | 23 | = 0.400 | 0.17 [-0.18, 0.68] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 2.83 | 23 | = 0.050 | 0.47 [0.12, 1.03] | small | * |
| Increase by 2 vs Increase by 3 | 2.15 | 23 | = 0.110 | 0.28 [-0.00, 0.88] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1184.53, BIC = 1215.77
- **Decrease by 1 vs Cardinality (no change)**: *β* = 2.77, *SE* = 1.961, *z* = 1.413, *p* = 0.158
- **Decrease by 2 vs Cardinality (no change)**: *β* = 3.67, *SE* = 1.952, *z* = 1.880, *p* = 0.060
- **Decrease by 3 vs Cardinality (no change)**: *β* = 1.60, *SE* = 1.961, *z* = 0.818, *p* = 0.413
- **Increase by 1 vs Cardinality (no change)**: *β* = -1.98, *SE* = 1.971, *z* = -1.004, *p* = 0.315
- **Increase by 2 vs Cardinality (no change)**: *β* = -2.70, *SE* = 1.964, *z* = -1.376, *p* = 0.169
- **Increase by 3 vs Cardinality (no change)**: *β* = -5.28, *SE* = 1.956, *z* = -2.700, *p* = 0.007
- **SNR**: *β* = 0.27, *SE* = 0.233, *z* = 1.137, *p* = 0.255

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -2.77 | 1.96 | -1.41 | 0.158 | 0.787 | n.s. |
| Cardinality (no change) - Decrease by 2 | -3.67 | 1.95 | -1.88 | 0.060 | 0.525 | n.s. |
| Cardinality (no change) - Decrease by 3 | -1.60 | 1.96 | -0.82 | 0.413 | 0.881 | n.s. |
| Cardinality (no change) - Increase by 1 | 1.98 | 1.97 | 1.00 | 0.315 | 0.871 | n.s. |
| Cardinality (no change) - Increase by 2 | 2.70 | 1.96 | 1.38 | 0.169 | 0.787 | n.s. |
| Cardinality (no change) - Increase by 3 | 5.28 | 1.96 | 2.70 | 0.007 | 0.099 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.90 | 1.95 | -0.46 | 0.644 | 0.908 | n.s. |
| Decrease by 1 - Decrease by 3 | 1.17 | 1.95 | 0.60 | 0.549 | 0.908 | n.s. |
| Decrease by 1 - Increase by 1 | 4.75 | 1.95 | 2.44 | 0.015 | 0.188 | n.s. |
| Decrease by 1 - Increase by 2 | 5.47 | 1.95 | 2.81 | 0.005 | 0.076 | n.s. |
| Decrease by 1 - Increase by 3 | 8.05 | 1.95 | 4.14 | < .001 | < .001 | *** |
| Decrease by 2 - Decrease by 3 | 2.07 | 1.95 | 1.06 | 0.289 | 0.871 | n.s. |
| Decrease by 2 - Increase by 1 | 5.65 | 1.95 | 2.89 | 0.004 | 0.063 | n.s. |
| Decrease by 2 - Increase by 2 | 6.37 | 1.95 | 3.27 | 0.001 | 0.019 | * |
| Decrease by 2 - Increase by 3 | 8.95 | 1.95 | 4.60 | < .001 | < .001 | *** |
| Decrease by 3 - Increase by 1 | 3.58 | 1.95 | 1.84 | 0.066 | 0.527 | n.s. |
| Decrease by 3 - Increase by 2 | 4.31 | 1.95 | 2.21 | 0.027 | 0.299 | n.s. |
| Decrease by 3 - Increase by 3 | 6.88 | 1.95 | 3.54 | < .001 | 0.008 | ** |
| Increase by 1 - Increase by 2 | 0.72 | 1.95 | 0.37 | 0.711 | 0.908 | n.s. |
| Increase by 1 - Increase by 3 | 3.30 | 1.95 | 1.69 | 0.090 | 0.613 | n.s. |
| Increase by 2 - Increase by 3 | 2.58 | 1.95 | 1.32 | 0.185 | 0.787 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.31, *p* < .001, η²_G = 0.095
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.678)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.76 | 23 | = 0.148 | -0.25 [-0.79, 0.08] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | -2.01 | 23 | = 0.099 | -0.37 [-0.85, 0.03] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.60 | 23 | = 0.645 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.03 | 23 | = 0.389 | 0.23 [-0.22, 0.64] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.23 | 23 | = 0.082 | 0.30 [0.01, 0.90] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 2.86 | 23 | = 0.037 | 0.55 [0.13, 1.04] | medium | * |
| Decrease by 1 vs Decrease by 2 | -0.54 | 23 | = 0.646 | -0.11 [-0.53, 0.31] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.51 | 23 | = 0.646 | 0.12 [-0.32, 0.53] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 2.19 | 23 | = 0.082 | 0.50 [0.00, 0.89] | medium | n.s. |
| Decrease by 1 vs Increase by 2 | 2.70 | 23 | = 0.045 | 0.57 [0.10, 1.00] | medium | * |
| Decrease by 1 vs Increase by 3 | 3.52 | 23 | = 0.013 | 0.84 [0.25, 1.19] | large | * |
| Decrease by 2 vs Decrease by 3 | 1.10 | 23 | = 0.371 | 0.25 [-0.20, 0.65] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 2.31 | 23 | = 0.079 | 0.65 [0.03, 0.92] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 3.49 | 23 | = 0.013 | 0.72 [0.24, 1.19] | medium | * |
| Decrease by 2 vs Increase by 3 | 4.25 | 23 | = 0.006 | 1.02 [0.37, 1.36] | large | ** |
| Decrease by 3 vs Increase by 1 | 1.70 | 23 | = 0.153 | 0.40 [-0.09, 0.78] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 2.08 | 23 | = 0.093 | 0.46 [-0.02, 0.87] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 3.40 | 23 | = 0.013 | 0.74 [0.22, 1.17] | medium | * |
| Increase by 1 vs Increase by 2 | 0.33 | 23 | = 0.747 | 0.07 [-0.36, 0.49] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 2.36 | 23 | = 0.079 | 0.34 [0.04, 0.93] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.53 | 23 | = 0.194 | 0.26 [-0.12, 0.75] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 553.78, BIC = 585.02
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.03, *SE* = 0.288, *z* = -0.096, *p* = 0.923
- **Decrease by 2 vs Cardinality (no change)**: *β* = 0.36, *SE* = 0.287, *z* = 1.254, *p* = 0.210
- **Decrease by 3 vs Cardinality (no change)**: *β* = 0.82, *SE* = 0.288, *z* = 2.850, *p* = 0.004
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.25, *SE* = 0.290, *z* = 0.875, *p* = 0.382
- **Increase by 2 vs Cardinality (no change)**: *β* = -0.00, *SE* = 0.288, *z* = -0.009, *p* = 0.993
- **Increase by 3 vs Cardinality (no change)**: *β* = 0.25, *SE* = 0.287, *z* = 0.863, *p* = 0.388
- **SNR**: *β* = 0.15, *SE* = 0.035, *z* = 4.375, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.03 | 0.29 | 0.10 | 0.923 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 | -0.36 | 0.29 | -1.25 | 0.210 | 0.960 | n.s. |
| Cardinality (no change) - Decrease by 3 | -0.82 | 0.29 | -2.85 | 0.004 | 0.080 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.25 | 0.29 | -0.87 | 0.382 | 0.991 | n.s. |
| Cardinality (no change) - Increase by 2 | 0.00 | 0.29 | 0.01 | 0.993 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 | -0.25 | 0.29 | -0.86 | 0.388 | 0.991 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.39 | 0.29 | -1.35 | 0.176 | 0.945 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.85 | 0.29 | -2.97 | 0.003 | 0.061 | n.s. |
| Decrease by 1 - Increase by 1 | -0.28 | 0.29 | -0.98 | 0.326 | 0.991 | n.s. |
| Decrease by 1 - Increase by 2 | -0.03 | 0.29 | -0.09 | 0.930 | 1.000 | n.s. |
| Decrease by 1 - Increase by 3 | -0.28 | 0.29 | -0.96 | 0.335 | 0.991 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.46 | 0.29 | -1.61 | 0.107 | 0.836 | n.s. |
| Decrease by 2 - Increase by 1 | 0.11 | 0.29 | 0.37 | 0.711 | 0.999 | n.s. |
| Decrease by 2 - Increase by 2 | 0.36 | 0.29 | 1.26 | 0.206 | 0.960 | n.s. |
| Decrease by 2 - Increase by 3 | 0.11 | 0.29 | 0.39 | 0.696 | 0.999 | n.s. |
| Decrease by 3 - Increase by 1 | 0.57 | 0.29 | 1.98 | 0.047 | 0.564 | n.s. |
| Decrease by 3 - Increase by 2 | 0.82 | 0.29 | 2.88 | 0.004 | 0.076 | n.s. |
| Decrease by 3 - Increase by 3 | 0.57 | 0.29 | 2.00 | 0.045 | 0.564 | n.s. |
| Increase by 1 - Increase by 2 | 0.26 | 0.29 | 0.89 | 0.371 | 0.991 | n.s. |
| Increase by 1 - Increase by 3 | 0.01 | 0.29 | 0.02 | 0.985 | 1.000 | n.s. |
| Increase by 2 - Increase by 3 | -0.25 | 0.29 | -0.88 | 0.381 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.83, *p* = 0.097, η²_G = 0.023
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.61 | 23 | = 0.744 | 0.10 [-0.30, 0.55] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | -1.02 | 23 | = 0.611 | -0.14 [-0.63, 0.22] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -2.03 | 23 | = 0.381 | -0.34 [-0.85, 0.03] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | -0.14 | 23 | = 0.935 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 | 0.64 | 23 | = 0.744 | 0.10 [-0.29, 0.55] | negligible | n.s. |
| Cardinality (no change) vs Increase by 3 | -0.38 | 23 | = 0.822 | -0.07 [-0.50, 0.34] | negligible | n.s. |
| Decrease by 1 vs Decrease by 2 | -1.56 | 23 | = 0.399 | -0.24 [-0.75, 0.11] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -3.00 | 23 | = 0.066 | -0.43 [-1.07, -0.15] | small | n.s. |
| Decrease by 1 vs Increase by 1 | -0.72 | 23 | = 0.744 | -0.13 [-0.57, 0.28] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | -0.05 | 23 | = 0.964 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | -1.09 | 23 | = 0.604 | -0.17 [-0.65, 0.21] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.25 | 23 | = 0.572 | -0.21 [-0.68, 0.17] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 0.58 | 23 | = 0.744 | 0.12 [-0.31, 0.54] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | 1.57 | 23 | = 0.399 | 0.26 [-0.11, 0.75] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 0.38 | 23 | = 0.822 | 0.08 [-0.34, 0.50] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | 1.64 | 23 | = 0.399 | 0.33 [-0.10, 0.77] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 3.07 | 23 | = 0.066 | 0.45 [0.17, 1.09] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 1.75 | 23 | = 0.399 | 0.29 [-0.08, 0.79] | small | n.s. |
| Increase by 1 vs Increase by 2 | 0.68 | 23 | = 0.744 | 0.14 [-0.28, 0.56] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.24 | 23 | = 0.902 | -0.04 [-0.47, 0.37] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.19 | 23 | = 0.572 | -0.18 [-0.67, 0.19] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1630.22, BIC = 1661.46
- **Decrease by 1 vs Cardinality (no change)**: *β* = 22.39, *SE* = 7.589, *z* = 2.950, *p* = 0.003
- **Decrease by 2 vs Cardinality (no change)**: *β* = 8.52, *SE* = 7.611, *z* = 1.120, *p* = 0.263
- **Decrease by 3 vs Cardinality (no change)**: *β* = 16.25, *SE* = 7.706, *z* = 2.109, *p* = 0.035
- **Increase by 1 vs Cardinality (no change)**: *β* = 20.66, *SE* = 7.636, *z* = 2.705, *p* = 0.007
- **Increase by 2 vs Cardinality (no change)**: *β* = 23.77, *SE* = 7.693, *z* = 3.089, *p* = 0.002
- **Increase by 3 vs Cardinality (no change)**: *β* = 14.87, *SE* = 7.510, *z* = 1.980, *p* = 0.048
- **SNR**: *β* = 0.11, *SE* = 0.502, *z* = 0.227, *p* = 0.820

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -22.39 | 7.59 | -2.95 | 0.003 | 0.062 | n.s. |
| Cardinality (no change) - Decrease by 2 | -8.52 | 7.61 | -1.12 | 0.263 | 0.974 | n.s. |
| Cardinality (no change) - Decrease by 3 | -16.25 | 7.71 | -2.11 | 0.035 | 0.473 | n.s. |
| Cardinality (no change) - Increase by 1 | -20.66 | 7.64 | -2.71 | 0.007 | 0.122 | n.s. |
| Cardinality (no change) - Increase by 2 | -23.76 | 7.69 | -3.09 | 0.002 | 0.041 | * |
| Cardinality (no change) - Increase by 3 | -14.87 | 7.51 | -1.98 | 0.048 | 0.543 | n.s. |
| Decrease by 1 - Decrease by 2 | 13.86 | 7.49 | 1.85 | 0.064 | 0.630 | n.s. |
| Decrease by 1 - Decrease by 3 | 6.13 | 7.51 | 0.82 | 0.414 | 0.983 | n.s. |
| Decrease by 1 - Increase by 1 | 1.73 | 7.49 | 0.23 | 0.818 | 0.994 | n.s. |
| Decrease by 1 - Increase by 2 | -1.38 | 7.51 | -0.18 | 0.854 | 0.994 | n.s. |
| Decrease by 1 - Increase by 3 | 7.52 | 7.52 | 1.00 | 0.317 | 0.981 | n.s. |
| Decrease by 2 - Decrease by 3 | -7.73 | 7.50 | -1.03 | 0.303 | 0.981 | n.s. |
| Decrease by 2 - Increase by 1 | -12.14 | 7.49 | -1.62 | 0.105 | 0.789 | n.s. |
| Decrease by 2 - Increase by 2 | -15.24 | 7.50 | -2.03 | 0.042 | 0.518 | n.s. |
| Decrease by 2 - Increase by 3 | -6.34 | 7.53 | -0.84 | 0.399 | 0.983 | n.s. |
| Decrease by 3 - Increase by 1 | -4.41 | 7.49 | -0.59 | 0.557 | 0.983 | n.s. |
| Decrease by 3 - Increase by 2 | -7.51 | 7.49 | -1.00 | 0.316 | 0.981 | n.s. |
| Decrease by 3 - Increase by 3 | 1.39 | 7.59 | 0.18 | 0.855 | 0.994 | n.s. |
| Increase by 1 - Increase by 2 | -3.11 | 7.49 | -0.41 | 0.678 | 0.989 | n.s. |
| Increase by 1 - Increase by 3 | 5.79 | 7.54 | 0.77 | 0.443 | 0.983 | n.s. |
| Increase by 2 - Increase by 3 | 8.90 | 7.58 | 1.17 | 0.241 | 0.972 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.52, *p* = 0.024, η²_G = 0.056
- Greenhouse-Geisser corrected: *p* = 0.046 (ε = 0.675)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -3.38 | 23 | = 0.054 | -0.79 [-1.16, -0.22] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 | -1.18 | 23 | = 0.478 | -0.31 [-0.67, 0.19] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | -2.26 | 23 | = 0.142 | -0.57 [-0.91, -0.02] | medium | n.s. |
| Cardinality (no change) vs Increase by 1 | -2.29 | 23 | = 0.142 | -0.63 [-0.91, -0.02] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | -2.79 | 23 | = 0.110 | -0.82 [-1.02, -0.11] | large | n.s. |
| Cardinality (no change) vs Increase by 3 | -1.85 | 23 | = 0.229 | -0.48 [-0.82, 0.06] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 2.35 | 23 | = 0.142 | 0.43 [0.03, 0.92] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.88 | 23 | = 0.582 | 0.18 [-0.25, 0.61] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 0.22 | 23 | = 0.827 | 0.05 [-0.38, 0.47] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | -0.22 | 23 | = 0.827 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 0.93 | 23 | = 0.582 | 0.22 [-0.24, 0.62] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.12 | 23 | = 0.481 | -0.24 [-0.66, 0.20] | small | n.s. |
| Decrease by 2 vs Increase by 1 | -1.40 | 23 | = 0.366 | -0.33 [-0.72, 0.14] | small | n.s. |
| Decrease by 2 vs Increase by 2 | -1.88 | 23 | = 0.229 | -0.47 [-0.82, 0.05] | small | n.s. |
| Decrease by 2 vs Increase by 3 | -0.73 | 23 | = 0.665 | -0.18 [-0.57, 0.28] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | -0.48 | 23 | = 0.786 | -0.12 [-0.52, 0.33] | negligible | n.s. |
| Decrease by 3 vs Increase by 2 | -1.64 | 23 | = 0.302 | -0.23 [-0.77, 0.10] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 0.34 | 23 | = 0.815 | 0.05 [-0.35, 0.49] | negligible | n.s. |
| Increase by 1 vs Increase by 2 | -0.37 | 23 | = 0.815 | -0.09 [-0.50, 0.35] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.59 | 23 | = 0.736 | 0.16 [-0.30, 0.54] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 1.55 | 23 | = 0.312 | 0.26 [-0.12, 0.75] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 666.14, BIC = 697.37
- **Decrease by 1 vs Cardinality (no change)**: *β* = 2.73, *SE* = 0.381, *z* = 7.162, *p* < .001
- **Decrease by 2 vs Cardinality (no change)**: *β* = 2.40, *SE* = 0.382, *z* = 6.285, *p* < .001
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.87, *SE* = 0.387, *z* = 7.413, *p* < .001
- **Increase by 1 vs Cardinality (no change)**: *β* = 1.59, *SE* = 0.383, *z* = 4.151, *p* < .001
- **Increase by 2 vs Cardinality (no change)**: *β* = 2.52, *SE* = 0.386, *z* = 6.535, *p* < .001
- **Increase by 3 vs Cardinality (no change)**: *β* = 2.70, *SE* = 0.376, *z* = 7.181, *p* < .001
- **SNR**: *β* = 0.10, *SE* = 0.026, *z* = 3.644, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -2.73 | 0.38 | -7.16 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 2 | -2.40 | 0.38 | -6.29 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 3 | -2.87 | 0.39 | -7.41 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 1 | -1.59 | 0.38 | -4.15 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 2 | -2.53 | 0.39 | -6.54 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 3 | -2.70 | 0.38 | -7.18 | < .001 | < .001 | *** |
| Decrease by 1 - Decrease by 2 | 0.33 | 0.38 | 0.87 | 0.384 | 0.982 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.14 | 0.38 | -0.38 | 0.703 | 0.995 | n.s. |
| Decrease by 1 - Increase by 1 | 1.14 | 0.38 | 3.03 | 0.002 | 0.034 | * |
| Decrease by 1 - Increase by 2 | 0.20 | 0.38 | 0.53 | 0.593 | 0.995 | n.s. |
| Decrease by 1 - Increase by 3 | 0.02 | 0.38 | 0.06 | 0.949 | 0.995 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.47 | 0.38 | -1.25 | 0.211 | 0.907 | n.s. |
| Decrease by 2 - Increase by 1 | 0.81 | 0.38 | 2.16 | 0.031 | 0.293 | n.s. |
| Decrease by 2 - Increase by 2 | -0.13 | 0.38 | -0.33 | 0.738 | 0.995 | n.s. |
| Decrease by 2 - Increase by 3 | -0.30 | 0.38 | -0.80 | 0.424 | 0.982 | n.s. |
| Decrease by 3 - Increase by 1 | 1.28 | 0.38 | 3.41 | < .001 | 0.010 | ** |
| Decrease by 3 - Increase by 2 | 0.34 | 0.37 | 0.92 | 0.358 | 0.982 | n.s. |
| Decrease by 3 - Increase by 3 | 0.17 | 0.38 | 0.44 | 0.659 | 0.995 | n.s. |
| Increase by 1 - Increase by 2 | -0.93 | 0.38 | -2.49 | 0.013 | 0.143 | n.s. |
| Increase by 1 - Increase by 3 | -1.11 | 0.38 | -2.94 | 0.003 | 0.042 | * |
| Increase by 2 - Increase by 3 | -0.18 | 0.38 | -0.46 | 0.642 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 15.78, *p* < .001, η²_G = 0.100
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.579)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -6.17 | 23 | < .001 | -1.02 [-1.82, -0.69] | large | *** |
| Cardinality (no change) vs Decrease by 2 | -6.29 | 23 | < .001 | -0.94 [-1.85, -0.71] | large | *** |
| Cardinality (no change) vs Decrease by 3 | -5.17 | 23 | < .001 | -1.03 [-1.58, -0.53] | large | *** |
| Cardinality (no change) vs Increase by 1 | -3.38 | 23 | = 0.007 | -0.59 [-1.16, -0.22] | medium | ** |
| Cardinality (no change) vs Increase by 2 | -5.81 | 23 | < .001 | -0.92 [-1.74, -0.64] | large | *** |
| Cardinality (no change) vs Increase by 3 | -5.49 | 23 | < .001 | -1.03 [-1.66, -0.58] | large | *** |
| Decrease by 1 vs Decrease by 2 | 1.00 | 23 | = 0.493 | 0.10 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.77 | 23 | = 0.588 | -0.08 [-0.58, 0.27] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 3.98 | 23 | = 0.002 | 0.32 [0.33, 1.30] | small | ** |
| Decrease by 1 vs Increase by 2 | 0.34 | 23 | = 0.776 | 0.03 [-0.35, 0.49] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 0.60 | 23 | = 0.673 | 0.05 [-0.30, 0.55] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.45 | 23 | = 0.279 | -0.17 [-0.73, 0.13] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 2.36 | 23 | = 0.052 | 0.24 [0.04, 0.93] | small | n.s. |
| Decrease by 2 vs Increase by 2 | -0.57 | 23 | = 0.673 | -0.06 [-0.54, 0.31] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | -0.47 | 23 | = 0.707 | -0.05 [-0.52, 0.33] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | 3.12 | 23 | = 0.011 | 0.38 [0.17, 1.10] | small | * |
| Decrease by 3 vs Increase by 2 | 0.85 | 23 | = 0.567 | 0.10 [-0.25, 0.60] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 1.16 | 23 | = 0.419 | 0.13 [-0.19, 0.66] | negligible | n.s. |
| Increase by 1 vs Increase by 2 | -3.42 | 23 | = 0.007 | -0.28 [-1.17, -0.23] | small | ** |
| Increase by 1 vs Increase by 3 | -2.88 | 23 | = 0.018 | -0.29 [-1.04, -0.13] | small | * |
| Increase by 2 vs Increase by 3 | 0.15 | 23 | = 0.879 | 0.02 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.006). Post-hoc tests revealed:
  - Cardinality (no change) showed greater latency than Increase by 3 (*d* = 0.58)
**N1 latency:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Decrease by 1 showed greater latency than Increase by 2 (*d* = 0.61)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed greater amplitude than Increase by 2 (*d* = 0.37)
  - Cardinality (no change) showed greater amplitude than Increase by 3 (*d* = 0.66)
  - Decrease by 1 showed greater amplitude than Increase by 3 (*d* = 0.55)
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.47)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed greater latency than Increase by 3 (*d* = 0.55)
  - Decrease by 1 showed greater latency than Increase by 2 (*d* = 0.57)
  - Decrease by 1 showed greater latency than Increase by 3 (*d* = 0.84)
  - Decrease by 2 showed greater latency than Increase by 2 (*d* = 0.72)
  - Decrease by 2 showed greater latency than Increase by 3 (*d* = 1.02)
  - Decrease by 3 showed greater latency than Increase by 3 (*d* = 0.74)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.097)
**P3b latency:** Significant main effect of condition (*p* = 0.024) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller amplitude than Decrease by 1 (*d* = -1.02)
  - Cardinality (no change) showed smaller amplitude than Decrease by 2 (*d* = -0.94)
  - Cardinality (no change) showed smaller amplitude than Decrease by 3 (*d* = -1.03)
  - Cardinality (no change) showed smaller amplitude than Increase by 1 (*d* = -0.59)
  - Cardinality (no change) showed smaller amplitude than Increase by 2 (*d* = -0.92)
  - Cardinality (no change) showed smaller amplitude than Increase by 3 (*d* = -1.03)
  - Decrease by 1 showed greater amplitude than Increase by 1 (*d* = 0.32)
  - Decrease by 3 showed greater amplitude than Increase by 1 (*d* = 0.38)
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.28)
  - Increase by 1 showed smaller amplitude than Increase by 3 (*d* = -0.29)

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
