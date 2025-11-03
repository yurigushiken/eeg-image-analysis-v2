# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:44:42

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
| Cardinality (no change, no 1) | 15 | 108.27 ms | 5.34 | 1.38 | [92.00, 112.00] |
| Decrease by 1 (no 1) | 13 | 103.38 ms | 6.90 | 1.91 | [92.00, 112.00] |
| Decrease by 2 (no 1) | 20 | 105.80 ms | 7.05 | 1.58 | [92.00, 112.00] |
| Decrease by 3 (no 1) | 18 | 103.56 ms | 7.50 | 1.77 | [92.00, 112.00] |
| Increase by 1 (no 1) | 17 | 101.41 ms | 7.06 | 1.71 | [92.00, 112.00] |
| Increase by 2 (no 1) | 16 | 103.50 ms | 7.43 | 1.86 | [92.00, 112.00] |
| Increase by 3 (no 1) | 14 | 102.00 ms | 8.11 | 2.17 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 15 | -2.07 µV | 1.28 | 0.33 | [-4.72, -0.17] |
| Decrease by 1 (no 1) | 13 | -2.07 µV | 1.25 | 0.35 | [-4.76, -0.33] |
| Decrease by 2 (no 1) | 20 | -2.05 µV | 1.16 | 0.26 | [-6.06, -0.36] |
| Decrease by 3 (no 1) | 18 | -2.49 µV | 1.31 | 0.31 | [-5.62, -0.55] |
| Increase by 1 (no 1) | 17 | -2.10 µV | 1.20 | 0.29 | [-3.95, -0.62] |
| Increase by 2 (no 1) | 16 | -2.07 µV | 1.07 | 0.27 | [-3.67, -0.47] |
| Increase by 3 (no 1) | 14 | -2.08 µV | 1.67 | 0.45 | [-5.70, -0.42] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 23 | 173.39 ms | 19.58 | 4.08 | [140.00, 208.00] |
| Decrease by 1 (no 1) | 24 | 176.83 ms | 18.65 | 3.81 | [140.00, 208.00] |
| Decrease by 2 (no 1) | 24 | 173.50 ms | 15.28 | 3.12 | [140.00, 208.00] |
| Decrease by 3 (no 1) | 24 | 175.83 ms | 17.35 | 3.54 | [152.00, 208.00] |
| Increase by 1 (no 1) | 22 | 164.55 ms | 17.03 | 3.63 | [140.00, 200.00] |
| Increase by 2 (no 1) | 24 | 169.17 ms | 18.14 | 3.70 | [140.00, 200.00] |
| Increase by 3 (no 1) | 23 | 167.83 ms | 19.94 | 4.16 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 23 | -5.27 µV | 2.22 | 0.46 | [-10.60, -1.65] |
| Decrease by 1 (no 1) | 24 | -5.50 µV | 2.10 | 0.43 | [-9.73, -1.93] |
| Decrease by 2 (no 1) | 24 | -5.67 µV | 2.22 | 0.45 | [-10.30, -1.75] |
| Decrease by 3 (no 1) | 24 | -6.44 µV | 2.41 | 0.49 | [-10.52, -1.96] |
| Increase by 1 (no 1) | 22 | -5.45 µV | 2.05 | 0.44 | [-9.45, -1.12] |
| Increase by 2 (no 1) | 24 | -5.45 µV | 2.62 | 0.53 | [-10.99, -1.19] |
| Increase by 3 (no 1) | 23 | -6.41 µV | 2.52 | 0.53 | [-13.29, -2.62] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 12 | 107.00 ms | 9.05 | 2.61 | [92.00, 116.00] |
| Decrease by 1 (no 1) | 10 | 107.60 ms | 8.10 | 2.56 | [92.00, 116.00] |
| Decrease by 2 (no 1) | 17 | 110.82 ms | 7.45 | 1.81 | [92.00, 116.00] |
| Decrease by 3 (no 1) | 15 | 108.80 ms | 8.58 | 2.22 | [92.00, 116.00] |
| Increase by 1 (no 1) | 16 | 106.00 ms | 8.39 | 2.10 | [92.00, 116.00] |
| Increase by 2 (no 1) | 13 | 108.62 ms | 8.62 | 2.39 | [92.00, 116.00] |
| Increase by 3 (no 1) | 12 | 102.67 ms | 8.58 | 2.48 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 12 | 2.49 µV | 1.53 | 0.44 | [0.31, 5.25] |
| Decrease by 1 (no 1) | 10 | 2.44 µV | 1.53 | 0.48 | [0.44, 5.06] |
| Decrease by 2 (no 1) | 17 | 2.28 µV | 1.26 | 0.31 | [0.28, 4.48] |
| Decrease by 3 (no 1) | 15 | 2.42 µV | 1.44 | 0.37 | [0.74, 5.70] |
| Increase by 1 (no 1) | 16 | 2.47 µV | 1.64 | 0.41 | [0.43, 5.16] |
| Increase by 2 (no 1) | 13 | 2.38 µV | 1.43 | 0.40 | [0.73, 4.87] |
| Increase by 3 (no 1) | 12 | 2.88 µV | 2.43 | 0.70 | [0.38, 8.91] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 16 | 468.50 ms | 25.59 | 6.40 | [420.00, 516.00] |
| Decrease by 1 (no 1) | 19 | 482.11 ms | 27.76 | 6.37 | [440.00, 536.00] |
| Decrease by 2 (no 1) | 19 | 480.84 ms | 32.51 | 7.46 | [440.00, 536.00] |
| Decrease by 3 (no 1) | 19 | 476.42 ms | 33.14 | 7.60 | [420.00, 536.00] |
| Increase by 1 (no 1) | 18 | 492.44 ms | 36.09 | 8.51 | [420.00, 536.00] |
| Increase by 2 (no 1) | 19 | 496.00 ms | 31.16 | 7.15 | [428.00, 536.00] |
| Increase by 3 (no 1) | 22 | 472.00 ms | 37.64 | 8.03 | [420.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 16 | 2.75 µV | 1.77 | 0.44 | [0.97, 6.88] |
| Decrease by 1 (no 1) | 19 | 5.24 µV | 2.61 | 0.60 | [1.60, 11.40] |
| Decrease by 2 (no 1) | 19 | 4.92 µV | 2.30 | 0.53 | [1.12, 8.89] |
| Decrease by 3 (no 1) | 19 | 5.62 µV | 3.01 | 0.69 | [1.12, 13.58] |
| Increase by 1 (no 1) | 18 | 4.82 µV | 2.98 | 0.70 | [0.74, 9.74] |
| Increase by 2 (no 1) | 19 | 5.32 µV | 2.76 | 0.63 | [0.78, 9.72] |
| Increase by 3 (no 1) | 22 | 4.42 µV | 2.40 | 0.51 | [0.76, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 748.31, BIC = 775.59
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.85, *SE* = 2.089, *z* = -1.365, *p* = 0.172
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.73, *SE* = 1.861, *z* = -0.930, *p* = 0.352
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.49, *SE* = 1.907, *z* = -1.830, *p* = 0.067
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -5.98, *SE* = 1.902, *z* = -3.144, *p* = 0.002
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.42, *SE* = 1.925, *z* = -2.295, *p* = 0.022
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -5.42, *SE* = 2.023, *z* = -2.677, *p* = 0.007
- **SNR**: *β* = 0.76, *SE* = 0.294, *z* = 2.565, *p* = 0.010

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 2.85 | 2.09 | 1.36 | 0.172 | 0.914 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 1.73 | 1.86 | 0.93 | 0.352 | 0.977 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 3.49 | 1.91 | 1.83 | 0.067 | 0.672 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 5.98 | 1.90 | 3.14 | 0.002 | 0.034 | * |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 4.42 | 1.93 | 2.29 | 0.022 | 0.327 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 5.42 | 2.02 | 2.68 | 0.007 | 0.138 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -1.12 | 1.94 | -0.58 | 0.563 | 0.984 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.64 | 1.98 | 0.32 | 0.747 | 0.984 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 3.13 | 1.98 | 1.58 | 0.115 | 0.840 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 1.57 | 2.06 | 0.76 | 0.446 | 0.977 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 2.57 | 2.10 | 1.22 | 0.222 | 0.936 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.76 | 1.75 | 1.00 | 0.316 | 0.977 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 4.25 | 1.77 | 2.40 | 0.016 | 0.268 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 2.69 | 1.81 | 1.48 | 0.138 | 0.875 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 3.69 | 1.88 | 1.96 | 0.050 | 0.582 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 2.49 | 1.82 | 1.37 | 0.172 | 0.914 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.93 | 1.87 | 0.50 | 0.619 | 0.984 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 1.93 | 1.92 | 1.00 | 0.316 | 0.977 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -1.56 | 1.88 | -0.83 | 0.407 | 0.977 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.56 | 1.94 | -0.29 | 0.772 | 0.984 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 1.00 | 1.99 | 0.50 | 0.615 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.75, *p* = 0.036, η²_G = 0.192
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 0.30 | 4 | = 0.860 | 0.11 [-0.36, 1.26] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 0.00 | 4 | = 1.000 | 0.00 [-0.55, 0.72] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 0.41 | 4 | = 0.860 | 0.22 [-0.40, 0.89] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 2.06 | 4 | = 0.285 | 0.60 [0.22, 1.67] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.30 | 4 | = 0.860 | 0.11 [0.02, 1.37] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 2.27 | 4 | = 0.285 | 1.09 [-0.01, 1.64] | large | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.34 | 4 | = 0.860 | -0.13 [-0.85, 0.51] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.53 | 4 | = 0.860 | 0.14 [-0.63, 0.72] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 3.16 | 4 | = 0.285 | 0.60 [-0.19, 1.16] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 0.00 | 4 | = 1.000 | 0.00 [-0.37, 1.24] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 2.39 | 4 | = 0.285 | 1.20 [-0.19, 1.51] | large | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.49 | 4 | = 0.860 | 0.25 [-0.34, 0.78] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 2.06 | 4 | = 0.285 | 0.66 [-0.26, 0.87] | medium | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 0.41 | 4 | = 0.860 | 0.13 [-0.41, 0.81] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 2.27 | 4 | = 0.285 | 1.21 [-0.17, 1.17] | large | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 1.37 | 4 | = 0.508 | 0.46 [-0.26, 0.93] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -0.53 | 4 | = 0.860 | -0.13 [-0.40, 0.89] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.86 | 4 | = 0.320 | 1.04 [-0.32, 0.99] | large | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -2.24 | 4 | = 0.285 | -0.57 [-0.86, 0.43] | medium | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.95 | 4 | = 0.753 | 0.51 [-0.64, 0.64] | medium | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.39 | 4 | = 0.285 | 1.15 [-0.24, 1.28] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 304.98, BIC = 332.26
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.19, *SE* = 0.293, *z* = -0.662, *p* = 0.508
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.35, *SE* = 0.263, *z* = -1.351, *p* = 0.177
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.85, *SE* = 0.269, *z* = -3.146, *p* = 0.002
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.22, *SE* = 0.268, *z* = -0.812, *p* = 0.417
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.22, *SE* = 0.272, *z* = -0.822, *p* = 0.411
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.36, *SE* = 0.286, *z* = -1.266, *p* = 0.205
- **SNR**: *β* = -0.34, *SE* = 0.042, *z* = -8.036, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.19 | 0.29 | 0.66 | 0.508 | 1.000 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.36 | 0.26 | 1.35 | 0.177 | 0.946 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 0.85 | 0.27 | 3.15 | 0.002 | 0.034 | * |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.22 | 0.27 | 0.81 | 0.417 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.22 | 0.27 | 0.82 | 0.411 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 0.36 | 0.29 | 1.27 | 0.205 | 0.960 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.16 | 0.27 | 0.59 | 0.554 | 1.000 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.65 | 0.28 | 2.34 | 0.019 | 0.297 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.02 | 0.28 | 0.09 | 0.932 | 1.000 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.03 | 0.29 | 0.10 | 0.918 | 1.000 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 0.17 | 0.29 | 0.57 | 0.569 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.49 | 0.25 | 1.99 | 0.047 | 0.557 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.14 | 0.25 | -0.55 | 0.582 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.13 | 0.26 | -0.52 | 0.606 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 0.01 | 0.27 | 0.02 | 0.981 | 1.000 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -0.63 | 0.26 | -2.44 | 0.015 | 0.255 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -0.62 | 0.26 | -2.37 | 0.018 | 0.290 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.49 | 0.27 | -1.79 | 0.074 | 0.706 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.01 | 0.27 | 0.02 | 0.983 | 1.000 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.14 | 0.27 | 0.53 | 0.599 | 1.000 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.14 | 0.28 | 0.49 | 0.622 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.01, *p* = 0.441, η²_G = 0.098
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.89 | 4 | = 0.921 | -0.42 [-0.93, 0.61] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -1.00 | 4 | = 0.921 | -0.33 [-0.63, 0.64] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 0.46 | 4 | = 0.931 | 0.28 [-0.19, 1.15] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -1.82 | 4 | = 0.601 | -0.75 [-0.58, 0.63] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -1.56 | 4 | = 0.681 | -0.71 [-0.72, 0.49] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.84 | 4 | = 0.921 | -0.48 [-0.65, 0.78] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.11 | 4 | = 0.966 | -0.04 [-0.41, 0.95] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.26 | 4 | = 0.601 | 0.69 [0.12, 1.72] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.77 | 4 | = 0.921 | -0.39 [-0.61, 0.66] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.65 | 4 | = 0.931 | -0.28 [-0.92, 0.62] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -0.52 | 4 | = 0.931 | -0.18 [-0.43, 1.15] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.23 | 4 | = 0.862 | 0.53 [-0.17, 0.98] | medium | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -0.60 | 4 | = 0.931 | -0.25 [-0.45, 0.66] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.34 | 4 | = 0.931 | -0.15 [-0.43, 0.79] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -0.31 | 4 | = 0.931 | -0.11 [-1.13, 0.20] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -1.97 | 4 | = 0.601 | -0.98 [-1.28, -0.01] | large | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -1.86 | 4 | = 0.601 | -0.98 [-1.63, -0.13] | large | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -2.90 | 4 | = 0.601 | -0.68 [-1.28, 0.09] | medium | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.21 | 4 | = 0.931 | 0.15 [-0.53, 0.74] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.23 | 4 | = 0.931 | 0.13 [-0.44, 0.84] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.05 | 4 | = 0.966 | 0.02 [-0.61, 0.82] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1331.28, BIC = 1362.27
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 3.89, *SE* = 3.207, *z* = 1.212, *p* = 0.225
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.55, *SE* = 3.206, *z* = 0.172, *p* = 0.863
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.88, *SE* = 3.206, *z* = 0.899, *p* = 0.369
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -6.24, *SE* = 3.292, *z* = -1.897, *p* = 0.058
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.78, *SE* = 3.206, *z* = -1.180, *p* = 0.238
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.92, *SE* = 3.252, *z* = -1.206, *p* = 0.228
- **SNR**: *β* = -0.01, *SE* = 0.262, *z* = -0.035, *p* = 0.972

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -3.89 | 3.21 | -1.21 | 0.225 | 0.940 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -0.55 | 3.21 | -0.17 | 0.863 | 0.985 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -2.88 | 3.21 | -0.90 | 0.369 | 0.960 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 6.24 | 3.29 | 1.90 | 0.058 | 0.566 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 3.78 | 3.21 | 1.18 | 0.238 | 0.940 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 3.92 | 3.25 | 1.21 | 0.228 | 0.940 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 3.33 | 3.17 | 1.05 | 0.292 | 0.940 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.00 | 3.17 | 0.32 | 0.751 | 0.985 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 10.13 | 3.26 | 3.11 | 0.002 | 0.038 | * |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 7.67 | 3.17 | 2.42 | 0.015 | 0.253 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 7.81 | 3.22 | 2.43 | 0.015 | 0.253 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.33 | 3.17 | -0.74 | 0.462 | 0.972 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 6.80 | 3.25 | 2.09 | 0.037 | 0.445 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 4.34 | 3.17 | 1.37 | 0.171 | 0.903 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 4.47 | 3.22 | 1.39 | 0.164 | 0.903 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 9.13 | 3.25 | 2.81 | 0.005 | 0.095 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 6.67 | 3.17 | 2.11 | 0.035 | 0.445 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 6.80 | 3.21 | 2.12 | 0.034 | 0.445 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -2.46 | 3.25 | -0.76 | 0.449 | 0.972 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -2.32 | 3.28 | -0.71 | 0.478 | 0.972 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.14 | 3.21 | 0.04 | 0.966 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.57, *p* = 0.023, η²_G = 0.047
- Greenhouse-Geisser corrected: *p* = 0.050 (ε = 0.607)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -1.81 | 20 | = 0.274 | -0.25 [-0.82, 0.07] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.53 | 20 | = 0.666 | -0.07 [-0.47, 0.40] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.93 | 20 | = 0.530 | -0.21 [-0.62, 0.25] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 1.70 | 20 | = 0.274 | 0.34 [-0.10, 0.84] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.85 | 20 | = 0.535 | 0.18 [-0.22, 0.65] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 1.06 | 20 | = 0.488 | 0.23 [-0.26, 0.64] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.35 | 20 | = 0.370 | 0.21 [-0.14, 0.72] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.30 | 20 | = 0.767 | 0.06 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 2.71 | 20 | = 0.228 | 0.61 [0.08, 1.04] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 2.04 | 20 | = 0.228 | 0.44 [0.02, 0.91] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 2.12 | 20 | = 0.228 | 0.48 [-0.04, 0.86] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.76 | 20 | = 0.562 | -0.16 [-0.59, 0.26] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 2.14 | 20 | = 0.228 | 0.45 [0.00, 0.94] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 1.25 | 20 | = 0.394 | 0.28 [-0.15, 0.71] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.43 | 20 | = 0.355 | 0.32 [-0.20, 0.67] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 2.26 | 20 | = 0.228 | 0.57 [-0.00, 0.93] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 1.49 | 20 | = 0.355 | 0.40 [-0.10, 0.77] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.75 | 20 | = 0.274 | 0.44 [-0.10, 0.79] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.90 | 20 | = 0.530 | -0.16 [-0.61, 0.28] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.56 | 20 | = 0.666 | -0.11 [-0.54, 0.35] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.42 | 20 | = 0.716 | 0.05 [-0.42, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 598.30, BIC = 629.30
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.24, *SE* = 0.338, *z* = -0.718, *p* = 0.473
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.44, *SE* = 0.338, *z* = -1.293, *p* = 0.196
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.25, *SE* = 0.338, *z* = -3.704, *p* < .001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.12, *SE* = 0.347, *z* = -0.343, *p* = 0.732
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.25, *SE* = 0.338, *z* = -0.745, *p* = 0.456
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.28, *SE* = 0.343, *z* = -3.723, *p* < .001
- **SNR**: *β* = -0.16, *SE* = 0.028, *z* = -5.724, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.24 | 0.34 | 0.72 | 0.473 | 0.996 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.44 | 0.34 | 1.29 | 0.196 | 0.909 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 1.25 | 0.34 | 3.70 | < .001 | 0.004 | ** |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.12 | 0.35 | 0.34 | 0.732 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.25 | 0.34 | 0.74 | 0.456 | 0.996 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 1.28 | 0.34 | 3.72 | < .001 | 0.004 | ** |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.19 | 0.33 | 0.58 | 0.561 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.01 | 0.33 | 3.02 | 0.003 | 0.039 | * |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.12 | 0.34 | -0.36 | 0.719 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.01 | 0.33 | 0.03 | 0.978 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 1.03 | 0.34 | 3.05 | 0.002 | 0.039 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.82 | 0.33 | 2.44 | 0.015 | 0.162 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.32 | 0.34 | -0.93 | 0.354 | 0.987 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.19 | 0.33 | -0.55 | 0.579 | 0.997 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 0.84 | 0.34 | 2.48 | 0.013 | 0.159 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -1.13 | 0.34 | -3.31 | < .001 | 0.017 | * |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -1.00 | 0.33 | -3.00 | 0.003 | 0.039 | * |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 0.02 | 0.34 | 0.07 | 0.942 | 0.998 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.13 | 0.34 | 0.39 | 0.699 | 0.998 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.16 | 0.35 | 3.35 | < .001 | 0.015 | * |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 1.03 | 0.34 | 3.03 | 0.002 | 0.039 | * |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.12, *p* = 0.007, η²_G = 0.044
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 0.90 | 20 | = 0.570 | 0.14 [-0.25, 0.62] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 1.80 | 20 | = 0.202 | 0.27 [-0.15, 0.73] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 3.22 | 20 | = 0.045 | 0.54 [0.19, 1.15] | medium | * |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.53 | 20 | = 0.752 | 0.08 [-0.34, 0.57] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 1.47 | 20 | = 0.276 | 0.16 [-0.21, 0.66] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 3.50 | 20 | = 0.045 | 0.55 [0.27, 1.28] | medium | * |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.65 | 20 | = 0.732 | 0.14 [-0.33, 0.51] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.03 | 20 | = 0.170 | 0.43 [0.01, 0.89] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.32 | 20 | = 0.832 | -0.06 [-0.57, 0.32] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 0.25 | 20 | = 0.845 | 0.04 [-0.45, 0.39] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.95 | 20 | = 0.170 | 0.43 [-0.05, 0.85] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.71 | 20 | = 0.216 | 0.30 [-0.00, 0.88] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -1.00 | 20 | = 0.529 | -0.20 [-0.72, 0.18] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.47 | 20 | = 0.752 | -0.08 [-0.55, 0.30] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.61 | 20 | = 0.236 | 0.31 [-0.11, 0.78] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -2.41 | 20 | = 0.134 | -0.49 [-1.05, -0.09] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -2.15 | 20 | = 0.170 | -0.35 [-1.00, -0.09] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.02 | 20 | = 0.986 | 0.00 [-0.48, 0.39] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.51 | 20 | = 0.752 | 0.10 [-0.32, 0.57] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.55 | 20 | = 0.132 | 0.50 [0.10, 1.06] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.01 | 20 | = 0.170 | 0.36 [0.01, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 664.14, BIC = 689.68
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.72, *SE* = 2.730, *z* = 0.630, *p* = 0.528
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 5.08, *SE* = 2.378, *z* = 2.137, *p* = 0.033
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 3.58, *SE* = 2.456, *z* = 1.457, *p* = 0.145
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.24, *SE* = 2.433, *z* = 0.098, *p* = 0.922
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.36, *SE* = 2.575, *z* = 0.528, *p* = 0.597
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.75, *SE* = 2.583, *z* = -1.838, *p* = 0.066
- **SNR**: *β* = 0.28, *SE* = 0.303, *z* = 0.935, *p* = 0.350

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -1.72 | 2.73 | -0.63 | 0.528 | 0.994 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -5.08 | 2.38 | -2.14 | 0.033 | 0.412 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -3.58 | 2.46 | -1.46 | 0.145 | 0.837 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.24 | 2.43 | -0.10 | 0.922 | 0.994 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -1.36 | 2.57 | -0.53 | 0.597 | 0.994 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 4.75 | 2.58 | 1.84 | 0.066 | 0.616 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -3.36 | 2.54 | -1.32 | 0.186 | 0.872 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.86 | 2.58 | -0.72 | 0.472 | 0.994 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 1.48 | 2.58 | 0.57 | 0.566 | 0.994 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.36 | 2.74 | 0.13 | 0.895 | 0.994 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 6.47 | 2.76 | 2.35 | 0.019 | 0.292 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.50 | 2.21 | 0.68 | 0.497 | 0.994 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 4.84 | 2.15 | 2.25 | 0.025 | 0.345 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 3.72 | 2.36 | 1.58 | 0.114 | 0.794 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 9.83 | 2.38 | 4.13 | < .001 | < .001 | *** |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 3.34 | 2.26 | 1.48 | 0.140 | 0.837 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 2.22 | 2.43 | 0.91 | 0.361 | 0.982 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 8.33 | 2.47 | 3.36 | < .001 | 0.015 | * |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -1.12 | 2.37 | -0.47 | 0.636 | 0.994 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 4.99 | 2.44 | 2.04 | 0.041 | 0.468 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 6.11 | 2.52 | 2.42 | 0.015 | 0.256 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.98, *p* = 0.465, η²_G = 0.082
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -1.00 | 3 | = 0.651 | -0.17 [-1.14, 0.73] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -1.73 | 3 | = 0.651 | -0.31 [-1.17, 0.24] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.52 | 3 | = 0.750 | -0.15 [-1.44, 0.14] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -0.52 | 3 | = 0.750 | -0.15 [-0.77, 0.77] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.00 | 3 | = 1.000 | 0.00 [-0.54, 1.01] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 0.93 | 3 | = 0.651 | 0.53 [-0.16, 1.40] | medium | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.00 | 3 | = 0.651 | -0.18 [-1.66, 0.21] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.00 | 3 | = 1.000 | 0.00 [-0.74, 0.93] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 0.00 | 3 | = 1.000 | 0.00 [-0.73, 1.13] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 0.52 | 3 | = 0.750 | 0.15 [-1.05, 1.05] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.32 | 3 | = 0.651 | 0.73 [-0.21, 1.97] | medium | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.00 | 3 | = 0.651 | 0.15 [-0.44, 0.78] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 1.00 | 3 | = 0.651 | 0.15 [-0.15, 1.07] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 1.73 | 3 | = 0.651 | 0.28 [-0.29, 1.22] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.26 | 3 | = 0.651 | 0.83 [0.28, 2.02] | large | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | nan | 3 | n/a | 0.00 [-0.36, 1.02] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 1.00 | 3 | = 0.651 | 0.13 [-0.29, 1.36] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.00 | 3 | = 0.651 | 0.66 [0.12, 2.06] | medium | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 1.00 | 3 | = 0.651 | 0.13 [-0.71, 0.63] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.00 | 3 | = 0.651 | 0.66 [-0.27, 1.38] | medium | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.74 | 3 | = 0.734 | 0.49 [-0.16, 1.56] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.68, BIC = 323.22
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.06, *SE* = 0.392, *z* = 0.155, *p* = 0.877
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.37, *SE* = 0.342, *z* = 1.072, *p* = 0.284
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.51, *SE* = 0.353, *z* = 1.448, *p* = 0.148
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.42, *SE* = 0.350, *z* = 1.196, *p* = 0.232
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.36, *SE* = 0.371, *z* = 0.985, *p* = 0.325
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.98, *SE* = 0.371, *z* = 2.636, *p* = 0.008
- **SNR**: *β* = 0.32, *SE* = 0.044, *z* = 7.196, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -0.06 | 0.39 | -0.16 | 0.877 | 1.000 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -0.37 | 0.34 | -1.07 | 0.284 | 0.982 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -0.51 | 0.35 | -1.45 | 0.148 | 0.922 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.42 | 0.35 | -1.20 | 0.232 | 0.972 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -0.37 | 0.37 | -0.99 | 0.325 | 0.987 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -0.98 | 0.37 | -2.64 | 0.008 | 0.162 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.31 | 0.37 | -0.84 | 0.402 | 0.990 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.45 | 0.37 | -1.21 | 0.226 | 0.972 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.36 | 0.37 | -0.96 | 0.335 | 0.987 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -0.30 | 0.39 | -0.77 | 0.439 | 0.990 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.92 | 0.39 | -2.33 | 0.020 | 0.330 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.14 | 0.32 | -0.45 | 0.652 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.05 | 0.31 | -0.17 | 0.868 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 0.00 | 0.34 | 0.01 | 0.996 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.61 | 0.34 | -1.79 | 0.074 | 0.766 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.09 | 0.33 | 0.28 | 0.778 | 0.999 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.15 | 0.35 | 0.42 | 0.676 | 0.999 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.47 | 0.35 | -1.32 | 0.186 | 0.954 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.05 | 0.34 | 0.16 | 0.875 | 1.000 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.56 | 0.35 | -1.60 | 0.110 | 0.861 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.61 | 0.36 | -1.69 | 0.091 | 0.822 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.987, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.74 | 3 | = 0.920 | -0.30 [-1.43, 0.51] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.30 | 3 | = 0.920 | -0.10 [-0.63, 0.71] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.55 | 3 | = 0.920 | -0.46 [-0.79, 0.64] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -0.55 | 3 | = 0.920 | -0.30 [-0.92, 0.62] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -1.21 | 3 | = 0.920 | -1.12 [-0.70, 0.84] | large | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.41 | 3 | = 0.920 | -0.30 [-1.02, 0.44] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.35 | 3 | = 0.920 | 0.18 [-1.36, 0.41] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.29 | 3 | = 0.920 | -0.21 [-1.05, 0.64] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.17 | 3 | = 0.920 | -0.05 [-1.05, 0.80] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.64 | 3 | = 0.920 | -0.50 [-1.23, 0.89] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -0.27 | 3 | = 0.920 | -0.19 [-1.18, 0.70] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.47 | 3 | = 0.920 | -0.36 [-0.66, 0.55] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -0.43 | 3 | = 0.920 | -0.20 [-0.71, 0.45] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.78 | 3 | = 0.920 | -0.75 [-0.65, 0.78] | medium | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -0.40 | 3 | = 0.920 | -0.26 [-0.76, 0.59] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 0.25 | 3 | = 0.920 | 0.14 [-0.63, 0.72] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -0.18 | 3 | = 0.920 | -0.12 [-0.43, 1.16] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.17 | 3 | = 0.920 | -0.07 [-0.54, 1.02] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.40 | 3 | = 0.920 | -0.32 [-0.51, 0.84] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.29 | 3 | = 0.920 | -0.15 [-1.08, 0.49] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.03 | 3 | = 0.980 | -0.02 [-1.02, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1291.91, BIC = 1320.74
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 13.01, *SE* = 9.916, *z* = 1.312, *p* = 0.190
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 10.93, *SE* = 9.524, *z* = 1.148, *p* = 0.251
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 6.63, *SE* = 9.739, *z* = 0.681, *p* = 0.496
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 24.11, *SE* = 9.595, *z* = 2.513, *p* = 0.012
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 26.87, *SE* = 9.721, *z* = 2.765, *p* = 0.006
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.23, *SE* = 9.179, *z* = 0.243, *p* = 0.808
- **SNR**: *β* = 0.28, *SE* = 0.732, *z* = 0.379, *p* = 0.705

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -13.01 | 9.92 | -1.31 | 0.190 | 0.920 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -10.93 | 9.52 | -1.15 | 0.251 | 0.943 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -6.63 | 9.74 | -0.68 | 0.496 | 0.989 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -24.11 | 9.59 | -2.51 | 0.012 | 0.205 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -26.87 | 9.72 | -2.76 | 0.006 | 0.108 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -2.23 | 9.18 | -0.24 | 0.808 | 0.992 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 2.08 | 9.03 | 0.23 | 0.818 | 0.992 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 6.38 | 8.94 | 0.71 | 0.475 | 0.989 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -11.10 | 9.22 | -1.20 | 0.229 | 0.943 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -13.86 | 8.93 | -1.55 | 0.121 | 0.835 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 10.78 | 8.98 | 1.20 | 0.230 | 0.943 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 4.30 | 8.96 | 0.48 | 0.631 | 0.992 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -13.18 | 9.06 | -1.45 | 0.146 | 0.871 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -15.95 | 8.95 | -1.78 | 0.075 | 0.689 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 8.70 | 8.71 | 1.00 | 0.318 | 0.953 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -17.48 | 9.17 | -1.91 | 0.057 | 0.607 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -20.25 | 8.95 | -2.26 | 0.024 | 0.335 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 4.39 | 8.83 | 0.50 | 0.619 | 0.992 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -2.76 | 9.09 | -0.30 | 0.761 | 0.992 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 21.88 | 8.81 | 2.48 | 0.013 | 0.210 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 24.64 | 8.81 | 2.80 | 0.005 | 0.103 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.41, *p* = 0.221, η²_G = 0.060
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -1.44 | 14 | = 0.494 | -0.51 [-0.99, 0.13] | medium | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.94 | 14 | = 0.633 | -0.30 [-0.89, 0.21] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.27 | 14 | = 0.874 | -0.08 [-0.71, 0.37] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -1.98 | 14 | = 0.494 | -0.60 [-1.10, 0.08] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -1.80 | 14 | = 0.494 | -0.74 [-1.11, 0.03] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.31 | 14 | = 0.874 | -0.11 [-0.58, 0.48] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.75 | 14 | = 0.696 | 0.15 [-0.33, 0.67] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.96 | 14 | = 0.633 | 0.38 [-0.28, 0.73] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.69 | 14 | = 0.699 | -0.19 [-0.85, 0.21] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.84 | 14 | = 0.667 | -0.29 [-0.90, 0.13] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.01 | 14 | = 0.633 | 0.29 [-0.14, 0.89] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.58 | 14 | = 0.704 | 0.20 [-0.40, 0.60] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -1.50 | 14 | = 0.494 | -0.30 [-1.02, 0.06] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -1.10 | 14 | = 0.633 | -0.40 [-0.82, 0.20] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.64 | 14 | = 0.702 | 0.14 [-0.17, 0.86] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -1.38 | 14 | = 0.494 | -0.49 [-0.99, 0.13] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -2.05 | 14 | = 0.494 | -0.61 [-1.18, -0.06] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.13 | 14 | = 0.902 | -0.04 [-0.38, 0.62] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.21 | 14 | = 0.880 | -0.07 [-0.53, 0.47] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.42 | 14 | = 0.494 | 0.41 [-0.02, 1.04] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.66 | 14 | = 0.494 | 0.51 [0.09, 1.15] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 482.72, BIC = 511.55
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.31, *SE* = 0.421, *z* = 3.121, *p* = 0.002
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.70, *SE* = 0.400, *z* = 4.252, *p* < .001
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.99, *SE* = 0.413, *z* = 4.810, *p* < .001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.61, *SE* = 0.402, *z* = 4.008, *p* < .001
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.70, *SE* = 0.411, *z* = 4.139, *p* < .001
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.71, *SE* = 0.390, *z* = 4.376, *p* < .001
- **SNR**: *β* = 0.30, *SE* = 0.034, *z* = 8.899, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -1.31 | 0.42 | -3.12 | 0.002 | 0.028 | * |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -1.70 | 0.40 | -4.25 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -1.99 | 0.41 | -4.81 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -1.61 | 0.40 | -4.01 | < .001 | 0.001 | ** |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -1.70 | 0.41 | -4.14 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -1.71 | 0.39 | -4.38 | < .001 | < .001 | *** |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.39 | 0.38 | -1.03 | 0.303 | 0.993 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.67 | 0.37 | -1.80 | 0.072 | 0.673 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.30 | 0.39 | -0.77 | 0.439 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -0.39 | 0.37 | -1.04 | 0.299 | 0.993 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.39 | 0.38 | -1.04 | 0.298 | 0.993 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.28 | 0.37 | -0.76 | 0.450 | 0.997 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 0.09 | 0.38 | 0.24 | 0.813 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 0.00 | 0.37 | 0.00 | 0.997 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.00 | 0.37 | -0.01 | 0.990 | 1.000 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.37 | 0.38 | 0.97 | 0.333 | 0.993 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.28 | 0.37 | 0.76 | 0.448 | 0.997 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 0.28 | 0.37 | 0.75 | 0.454 | 0.997 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.09 | 0.38 | -0.23 | 0.816 | 1.000 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.09 | 0.37 | -0.25 | 0.799 | 1.000 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.01 | 0.37 | -0.02 | 0.987 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.08, *p* < .001, η²_G = 0.133
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.492)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -3.36 | 14 | = 0.025 | -1.17 [-1.51, -0.25] | large | * |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -3.95 | 14 | = 0.015 | -1.31 [-1.69, -0.37] | large | * |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -3.56 | 14 | = 0.022 | -1.26 [-1.58, -0.30] | large | * |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -2.87 | 14 | = 0.043 | -0.96 [-1.37, -0.12] | large | * |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -4.26 | 14 | = 0.015 | -1.27 [-1.81, -0.45] | large | * |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -3.19 | 14 | = 0.027 | -1.12 [-1.44, -0.21] | large | * |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.32 | 14 | = 0.809 | 0.06 [-0.36, 0.64] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.91 | 14 | = 0.527 | -0.15 [-0.84, 0.18] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.00 | 14 | = 0.503 | 0.12 [-0.19, 0.87] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.49 | 14 | = 0.736 | -0.09 [-0.61, 0.39] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.13 | 14 | = 0.476 | 0.16 [-0.20, 0.82] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.15 | 14 | = 0.476 | -0.22 [-0.94, 0.09] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 0.54 | 14 | = 0.736 | 0.08 [-0.30, 0.74] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.77 | 14 | = 0.592 | -0.15 [-0.65, 0.35] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.09 | 14 | = 0.476 | 0.12 [-0.12, 0.92] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 1.56 | 14 | = 0.372 | 0.25 [-0.09, 1.03] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.30 | 14 | = 0.809 | 0.07 [-0.38, 0.65] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.90 | 14 | = 0.236 | 0.31 [-0.12, 0.91] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.31 | 14 | = 0.476 | -0.20 [-0.87, 0.16] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.16 | 14 | = 0.873 | 0.02 [-0.51, 0.49] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.20 | 14 | = 0.476 | 0.25 [-0.18, 0.81] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.036) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* = 0.023) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* = 0.007). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed greater amplitude than Decrease by 3 (no 1) (*d* = 0.54)
  - Cardinality (no change, no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.55)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 1 (no 1) (*d* = -1.17)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 2 (no 1) (*d* = -1.31)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 3 (no 1) (*d* = -1.26)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 1 (no 1) (*d* = -0.96)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -1.27)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 3 (no 1) (*d* = -1.12)

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
