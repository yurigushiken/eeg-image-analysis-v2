# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:44:55

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
| Decrease by 1 (no 1) | 13 | 104.62 ms | 6.50 | 1.80 | [96.00, 112.00] |
| Decrease by 2 (no 1) | 20 | 105.60 ms | 7.50 | 1.68 | [92.00, 112.00] |
| Decrease by 3 (no 1) | 17 | 104.00 ms | 7.35 | 1.78 | [92.00, 112.00] |
| Increase by 1 (no 1) | 16 | 102.75 ms | 6.81 | 1.70 | [92.00, 112.00] |
| Increase by 2 (no 1) | 16 | 103.75 ms | 7.08 | 1.77 | [92.00, 112.00] |
| Increase by 3 (no 1) | 14 | 101.14 ms | 7.09 | 1.90 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 15 | -2.07 µV | 1.28 | 0.33 | [-4.72, -0.17] |
| Decrease by 1 (no 1) | 13 | -2.03 µV | 1.38 | 0.38 | [-5.59, -0.54] |
| Decrease by 2 (no 1) | 20 | -1.88 µV | 1.21 | 0.27 | [-5.60, -0.24] |
| Decrease by 3 (no 1) | 17 | -2.45 µV | 1.40 | 0.34 | [-6.28, -0.55] |
| Increase by 1 (no 1) | 16 | -1.70 µV | 0.79 | 0.20 | [-3.26, -0.62] |
| Increase by 2 (no 1) | 16 | -2.00 µV | 1.04 | 0.26 | [-3.67, -0.24] |
| Increase by 3 (no 1) | 14 | -1.85 µV | 1.51 | 0.40 | [-6.02, -0.20] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 23 | 173.39 ms | 19.58 | 4.08 | [140.00, 208.00] |
| Decrease by 1 (no 1) | 24 | 174.00 ms | 17.77 | 3.63 | [140.00, 208.00] |
| Decrease by 2 (no 1) | 24 | 172.83 ms | 16.13 | 3.29 | [140.00, 208.00] |
| Decrease by 3 (no 1) | 24 | 175.00 ms | 16.98 | 3.47 | [148.00, 208.00] |
| Increase by 1 (no 1) | 23 | 169.22 ms | 18.74 | 3.91 | [140.00, 208.00] |
| Increase by 2 (no 1) | 24 | 168.50 ms | 17.51 | 3.57 | [140.00, 200.00] |
| Increase by 3 (no 1) | 23 | 168.52 ms | 19.27 | 4.02 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 23 | -5.27 µV | 2.22 | 0.46 | [-10.60, -1.65] |
| Decrease by 1 (no 1) | 24 | -5.37 µV | 2.03 | 0.41 | [-9.50, -2.05] |
| Decrease by 2 (no 1) | 24 | -5.49 µV | 2.17 | 0.44 | [-9.98, -1.47] |
| Decrease by 3 (no 1) | 24 | -6.24 µV | 2.41 | 0.49 | [-10.22, -1.96] |
| Increase by 1 (no 1) | 23 | -5.19 µV | 2.18 | 0.45 | [-9.40, -0.93] |
| Increase by 2 (no 1) | 24 | -5.27 µV | 2.60 | 0.53 | [-10.89, -0.50] |
| Increase by 3 (no 1) | 23 | -6.18 µV | 2.45 | 0.51 | [-13.18, -2.28] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 12 | 105.67 ms | 7.71 | 2.23 | [92.00, 112.00] |
| Decrease by 1 (no 1) | 14 | 105.14 ms | 8.51 | 2.27 | [92.00, 112.00] |
| Decrease by 2 (no 1) | 14 | 108.57 ms | 6.63 | 1.77 | [92.00, 112.00] |
| Decrease by 3 (no 1) | 14 | 106.29 ms | 7.31 | 1.95 | [92.00, 112.00] |
| Increase by 1 (no 1) | 15 | 103.73 ms | 6.50 | 1.68 | [92.00, 112.00] |
| Increase by 2 (no 1) | 16 | 104.25 ms | 7.93 | 1.98 | [92.00, 112.00] |
| Increase by 3 (no 1) | 10 | 102.00 ms | 7.60 | 2.40 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 12 | 2.37 µV | 1.48 | 0.43 | [0.31, 4.97] |
| Decrease by 1 (no 1) | 14 | 1.82 µV | 1.62 | 0.43 | [0.40, 4.96] |
| Decrease by 2 (no 1) | 14 | 2.31 µV | 1.23 | 0.33 | [0.43, 4.83] |
| Decrease by 3 (no 1) | 14 | 2.42 µV | 1.49 | 0.40 | [0.91, 6.10] |
| Increase by 1 (no 1) | 15 | 1.76 µV | 1.40 | 0.36 | [0.29, 4.52] |
| Increase by 2 (no 1) | 16 | 1.97 µV | 1.32 | 0.33 | [0.36, 4.54] |
| Increase by 3 (no 1) | 10 | 2.57 µV | 2.43 | 0.77 | [0.54, 9.07] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 16 | 468.25 ms | 26.11 | 6.53 | [416.00, 516.00] |
| Decrease by 1 (no 1) | 19 | 485.89 ms | 28.14 | 6.46 | [440.00, 532.00] |
| Decrease by 2 (no 1) | 18 | 478.22 ms | 29.14 | 6.87 | [440.00, 532.00] |
| Decrease by 3 (no 1) | 18 | 470.00 ms | 30.25 | 7.13 | [416.00, 524.00] |
| Increase by 1 (no 1) | 16 | 491.25 ms | 36.61 | 9.15 | [416.00, 532.00] |
| Increase by 2 (no 1) | 17 | 485.65 ms | 35.04 | 8.50 | [416.00, 532.00] |
| Increase by 3 (no 1) | 22 | 466.73 ms | 38.00 | 8.10 | [416.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 16 | 2.76 µV | 1.77 | 0.44 | [0.97, 6.88] |
| Decrease by 1 (no 1) | 19 | 4.48 µV | 2.50 | 0.57 | [1.07, 9.46] |
| Decrease by 2 (no 1) | 18 | 4.91 µV | 2.20 | 0.52 | [2.16, 8.74] |
| Decrease by 3 (no 1) | 18 | 5.64 µV | 3.06 | 0.72 | [1.12, 13.58] |
| Increase by 1 (no 1) | 16 | 4.20 µV | 2.61 | 0.65 | [0.98, 8.98] |
| Increase by 2 (no 1) | 17 | 5.50 µV | 2.56 | 0.62 | [1.49, 10.75] |
| Increase by 3 (no 1) | 22 | 4.25 µV | 2.32 | 0.49 | [0.84, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 736.28, BIC = 763.37
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.38, *SE* = 2.091, *z* = -1.615, *p* = 0.106
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.10, *SE* = 1.917, *z* = -1.096, *p* = 0.273
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.50, *SE* = 1.960, *z* = -1.784, *p* = 0.074
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.70, *SE* = 1.982, *z* = -2.370, *p* = 0.018
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.89, *SE* = 1.967, *z* = -2.485, *p* = 0.013
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -5.90, *SE* = 2.071, *z* = -2.847, *p* = 0.004
- **SNR**: *β* = 0.39, *SE* = 0.333, *z* = 1.184, *p* = 0.236

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 3.38 | 2.09 | 1.61 | 0.106 | 0.834 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 2.10 | 1.92 | 1.10 | 0.273 | 0.970 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 3.50 | 1.96 | 1.78 | 0.074 | 0.732 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 4.70 | 1.98 | 2.37 | 0.018 | 0.289 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 4.89 | 1.97 | 2.49 | 0.013 | 0.229 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 5.90 | 2.07 | 2.85 | 0.004 | 0.089 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -1.28 | 2.00 | -0.64 | 0.522 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.12 | 2.05 | 0.06 | 0.953 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 1.32 | 2.07 | 0.64 | 0.524 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 1.51 | 2.08 | 0.73 | 0.468 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 2.52 | 2.16 | 1.17 | 0.243 | 0.964 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.40 | 1.82 | 0.77 | 0.441 | 0.997 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 2.60 | 1.85 | 1.41 | 0.160 | 0.912 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 2.79 | 1.87 | 1.49 | 0.135 | 0.887 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 3.80 | 1.93 | 1.97 | 0.049 | 0.594 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 1.20 | 1.92 | 0.63 | 0.531 | 0.997 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 1.39 | 1.93 | 0.72 | 0.471 | 0.997 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 2.40 | 1.98 | 1.21 | 0.224 | 0.963 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.19 | 1.96 | 0.10 | 0.923 | 0.997 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.20 | 2.00 | 0.60 | 0.547 | 0.997 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 1.01 | 2.05 | 0.49 | 0.622 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.91, *p* = 0.121, η²_G = 0.197
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 3.21 | 4 | = 0.343 | 0.95 [-0.04, 1.59] | large | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 1.37 | 4 | = 0.508 | 0.51 [-0.50, 0.78] | medium | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 0.74 | 4 | = 0.694 | 0.45 [-0.40, 0.89] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 2.45 | 4 | = 0.467 | 0.69 [0.09, 1.46] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 2.24 | 4 | = 0.467 | 0.72 [0.22, 1.67] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 3.21 | 4 | = 0.343 | 1.84 [0.09, 1.67] | large | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.78 | 4 | = 0.694 | -0.22 [-0.89, 0.47] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.69 | 4 | = 0.694 | -0.37 [-0.99, 0.46] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -1.50 | 4 | = 0.494 | -0.47 [-0.43, 0.93] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -1.00 | 4 | = 0.654 | -0.12 [-1.12, 0.46] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.24 | 4 | = 0.541 | 0.74 [-0.31, 1.32] | medium | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.15 | 4 | = 0.931 | -0.11 [-0.36, 0.76] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -0.27 | 4 | = 0.883 | -0.13 [-0.43, 0.73] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 0.41 | 4 | = 0.821 | 0.10 [-0.37, 0.86] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.49 | 4 | = 0.494 | 0.86 [-0.18, 1.16] | large | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 0.00 | 4 | = 1.000 | 0.00 [-0.42, 0.80] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.43 | 4 | = 0.821 | 0.23 [-0.41, 0.88] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.62 | 4 | = 0.494 | 1.09 [-0.25, 1.01] | large | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.78 | 4 | = 0.694 | 0.28 [-0.46, 0.82] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.96 | 4 | = 0.494 | 1.36 [-0.40, 0.82] | large | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.51 | 4 | = 0.494 | 0.82 [-0.60, 0.84] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.53, BIC = 302.63
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.19, *SE* = 0.251, *z* = 0.763, *p* = 0.446
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.21, *SE* = 0.231, *z* = -0.890, *p* = 0.373
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.61, *SE* = 0.235, *z* = -2.609, *p* = 0.009
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.14, *SE* = 0.238, *z* = 0.566, *p* = 0.572
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.07, *SE* = 0.236, *z* = -0.276, *p* = 0.783
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.10, *SE* = 0.249, *z* = -0.385, *p* = 0.700
- **SNR**: *β* = -0.33, *SE* = 0.042, *z* = -7.886, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -0.19 | 0.25 | -0.76 | 0.446 | 0.991 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.21 | 0.23 | 0.89 | 0.373 | 0.991 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 0.61 | 0.24 | 2.61 | 0.009 | 0.159 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.13 | 0.24 | -0.57 | 0.572 | 0.995 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.07 | 0.24 | 0.28 | 0.783 | 0.995 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 0.10 | 0.25 | 0.38 | 0.700 | 0.995 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.40 | 0.24 | 1.65 | 0.098 | 0.789 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.81 | 0.25 | 3.27 | 0.001 | 0.022 | * |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.06 | 0.25 | 0.23 | 0.818 | 0.995 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.26 | 0.25 | 1.03 | 0.305 | 0.987 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 0.29 | 0.26 | 1.11 | 0.268 | 0.983 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.41 | 0.22 | 1.87 | 0.061 | 0.637 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.34 | 0.22 | -1.53 | 0.126 | 0.848 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.14 | 0.22 | -0.63 | 0.530 | 0.995 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.11 | 0.23 | -0.47 | 0.635 | 0.995 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -0.75 | 0.23 | -3.25 | 0.001 | 0.023 | * |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -0.55 | 0.23 | -2.37 | 0.018 | 0.274 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.52 | 0.24 | -2.19 | 0.029 | 0.392 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.20 | 0.24 | 0.85 | 0.396 | 0.991 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.23 | 0.24 | 0.96 | 0.336 | 0.989 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.03 | 0.25 | 0.12 | 0.901 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.70, *p* = 0.164, η²_G = 0.125
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.70 | 4 | = 0.731 | -0.30 [-0.87, 0.57] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.98 | 4 | = 0.670 | -0.26 [-0.87, 0.41] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 0.27 | 4 | = 0.841 | 0.14 [-0.28, 1.04] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -3.99 | 4 | = 0.342 | -1.30 [-1.04, 0.22] | large | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -1.88 | 4 | = 0.466 | -0.59 [-0.71, 0.50] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.94 | 4 | = 0.670 | -0.47 [-0.86, 0.49] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.04 | 4 | = 0.967 | 0.02 [-0.49, 0.87] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 1.40 | 4 | = 0.616 | 0.39 [-0.08, 1.53] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -1.60 | 4 | = 0.555 | -0.77 [-1.01, 0.37] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.34 | 4 | = 0.841 | -0.13 [-0.88, 0.66] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -1.17 | 4 | = 0.647 | -0.21 [-0.74, 0.80] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.91 | 4 | = 0.670 | 0.35 [-0.10, 1.07] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -2.82 | 4 | = 0.379 | -0.74 [-0.73, 0.43] | medium | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.31 | 4 | = 0.841 | -0.14 [-0.43, 0.79] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -0.52 | 4 | = 0.824 | -0.21 [-0.91, 0.38] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -2.70 | 4 | = 0.379 | -1.23 [-1.55, -0.14] | large | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -1.30 | 4 | = 0.616 | -0.63 [-1.54, -0.08] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -2.31 | 4 | = 0.432 | -0.54 [-1.26, 0.06] | medium | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 1.95 | 4 | = 0.466 | 0.96 [-0.18, 1.17] | large | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.73 | 4 | = 0.731 | 0.39 [-0.46, 0.75] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.32 | 4 | = 0.841 | -0.15 [-0.72, 0.71] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1329.93, BIC = 1360.99
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.04, *SE* = 3.119, *z* = 0.333, *p* = 0.739
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.14, *SE* = 3.112, *z* = -0.044, *p* = 0.965
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.00, *SE* = 3.099, *z* = 0.644, *p* = 0.520
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.52, *SE* = 3.140, *z* = -0.801, *p* = 0.423
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.50, *SE* = 3.099, *z* = -1.454, *p* = 0.146
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.24, *SE* = 3.143, *z* = -1.031, *p* = 0.303
- **SNR**: *β* = -0.03, *SE* = 0.260, *z* = -0.113, *p* = 0.910

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -1.04 | 3.12 | -0.33 | 0.739 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.14 | 3.11 | 0.04 | 0.965 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -2.00 | 3.10 | -0.64 | 0.520 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 2.52 | 3.14 | 0.80 | 0.423 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 4.51 | 3.10 | 1.45 | 0.146 | 0.942 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 3.24 | 3.14 | 1.03 | 0.303 | 0.991 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 1.17 | 3.06 | 0.38 | 0.701 | 0.999 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.96 | 3.08 | -0.31 | 0.756 | 0.999 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 3.55 | 3.11 | 1.14 | 0.254 | 0.983 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 5.54 | 3.08 | 1.80 | 0.072 | 0.777 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 4.28 | 3.14 | 1.36 | 0.174 | 0.943 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.13 | 3.08 | -0.69 | 0.488 | 0.998 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 2.38 | 3.11 | 0.77 | 0.444 | 0.998 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 4.37 | 3.08 | 1.42 | 0.156 | 0.942 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 3.10 | 3.13 | 0.99 | 0.322 | 0.991 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 4.51 | 3.10 | 1.45 | 0.146 | 0.942 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 6.50 | 3.06 | 2.12 | 0.034 | 0.513 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 5.23 | 3.10 | 1.69 | 0.092 | 0.839 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.99 | 3.10 | 0.64 | 0.521 | 0.998 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.72 | 3.14 | 0.23 | 0.817 | 0.999 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -1.27 | 3.10 | -0.41 | 0.683 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.463, η²_G = 0.015
- Greenhouse-Geisser corrected: *p* = 0.437 (ε = 0.634)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.44 | 21 | = 0.776 | -0.05 [-0.52, 0.34] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 0.09 | 21 | = 0.933 | 0.01 [-0.41, 0.45] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.67 | 21 | = 0.776 | -0.15 [-0.56, 0.30] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.72 | 21 | = 0.776 | 0.13 [-0.29, 0.60] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 1.04 | 21 | = 0.776 | 0.22 [-0.19, 0.68] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 0.93 | 21 | = 0.776 | 0.15 [-0.25, 0.65] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.65 | 21 | = 0.776 | 0.07 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.48 | 21 | = 0.776 | -0.10 [-0.49, 0.36] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 0.92 | 21 | = 0.776 | 0.18 [-0.24, 0.64] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.55 | 21 | = 0.776 | 0.29 [-0.05, 0.82] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.27 | 21 | = 0.776 | 0.21 [-0.15, 0.73] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.84 | 21 | = 0.776 | -0.18 [-0.57, 0.28] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 0.57 | 21 | = 0.776 | 0.13 [-0.32, 0.55] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 1.13 | 21 | = 0.776 | 0.24 [-0.15, 0.71] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.78 | 21 | = 0.776 | 0.16 [-0.26, 0.61] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 1.10 | 21 | = 0.776 | 0.28 [-0.22, 0.66] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 1.54 | 21 | = 0.776 | 0.39 [-0.09, 0.78] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.27 | 21 | = 0.776 | 0.30 [-0.18, 0.70] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.51 | 21 | = 0.776 | 0.09 [-0.31, 0.56] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.21 | 21 | = 0.881 | 0.03 [-0.38, 0.49] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.33 | 21 | = 0.819 | -0.06 [-0.51, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 579.54, BIC = 610.60
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.05, *SE* = 0.315, *z* = 0.171, *p* = 0.864
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.11, *SE* = 0.314, *z* = -0.362, *p* = 0.717
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.04, *SE* = 0.313, *z* = -3.340, *p* = 0.001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.12, *SE* = 0.317, *z* = 0.366, *p* = 0.714
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.07, *SE* = 0.313, *z* = -0.240, *p* = 0.811
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.02, *SE* = 0.317, *z* = -3.227, *p* = 0.001
- **SNR**: *β* = -0.15, *SE* = 0.027, *z* = -5.864, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -0.05 | 0.31 | -0.17 | 0.864 | 1.000 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.11 | 0.31 | 0.36 | 0.717 | 1.000 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 1.04 | 0.31 | 3.34 | < .001 | 0.014 | * |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.12 | 0.32 | -0.37 | 0.714 | 1.000 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.07 | 0.31 | 0.24 | 0.811 | 1.000 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 1.02 | 0.32 | 3.23 | 0.001 | 0.020 | * |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.17 | 0.31 | 0.54 | 0.587 | 1.000 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.10 | 0.31 | 3.53 | < .001 | 0.008 | ** |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.06 | 0.31 | -0.20 | 0.843 | 1.000 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.13 | 0.31 | 0.41 | 0.679 | 1.000 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 1.08 | 0.32 | 3.40 | < .001 | 0.012 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.93 | 0.31 | 3.00 | 0.003 | 0.035 | * |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.23 | 0.31 | -0.73 | 0.463 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.04 | 0.31 | -0.13 | 0.900 | 1.000 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 0.91 | 0.32 | 2.88 | 0.004 | 0.047 | * |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -1.16 | 0.31 | -3.71 | < .001 | 0.004 | ** |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -0.97 | 0.31 | -3.14 | 0.002 | 0.025 | * |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.02 | 0.31 | -0.07 | 0.946 | 1.000 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.19 | 0.31 | 0.61 | 0.542 | 1.000 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.14 | 0.32 | 3.60 | < .001 | 0.006 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.95 | 0.31 | 3.03 | 0.002 | 0.034 | * |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.12, *p* = 0.007, η²_G = 0.032
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 0.54 | 21 | = 0.830 | 0.07 [-0.35, 0.52] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 1.08 | 21 | = 0.554 | 0.16 [-0.28, 0.59] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 2.97 | 21 | = 0.076 | 0.45 [0.10, 1.04] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.32 | 21 | = 0.925 | 0.04 [-0.37, 0.51] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.62 | 21 | = 0.830 | 0.07 [-0.35, 0.51] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 3.05 | 21 | = 0.076 | 0.43 [0.16, 1.14] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.55 | 21 | = 0.830 | 0.09 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.27 | 21 | = 0.089 | 0.41 [0.02, 0.91] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.20 | 21 | = 0.929 | -0.03 [-0.56, 0.31] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 0.07 | 21 | = 0.948 | 0.01 [-0.49, 0.36] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 2.58 | 21 | = 0.089 | 0.38 [0.04, 0.95] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.09 | 21 | = 0.114 | 0.31 [0.03, 0.92] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -0.75 | 21 | = 0.807 | -0.12 [-0.66, 0.21] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.46 | 21 | = 0.851 | -0.08 [-0.54, 0.30] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.48 | 21 | = 0.321 | 0.28 [-0.15, 0.73] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -2.54 | 21 | = 0.089 | -0.43 [-1.06, -0.12] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -2.37 | 21 | = 0.089 | -0.36 [-1.00, -0.09] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.15 | 21 | = 0.929 | -0.03 [-0.50, 0.37] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.22 | 21 | = 0.929 | 0.03 [-0.36, 0.50] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.46 | 21 | = 0.089 | 0.41 [0.10, 1.03] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.29 | 21 | = 0.089 | 0.33 [0.05, 0.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 643.80, BIC = 669.34
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.22, *SE* = 2.214, *z* = -0.100, *p* = 0.920
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.73, *SE* = 2.232, *z* = 1.222, *p* = 0.222
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.78, *SE* = 2.243, *z* = 0.346, *p* = 0.729
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.06, *SE* = 2.214, *z* = -0.480, *p* = 0.631
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.91, *SE* = 2.201, *z* = -0.866, *p* = 0.386
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.78, *SE* = 2.435, *z* = -1.963, *p* = 0.050
- **SNR**: *β* = 0.11, *SE* = 0.273, *z* = 0.398, *p* = 0.690

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.22 | 2.21 | 0.10 | 0.920 | 0.997 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -2.73 | 2.23 | -1.22 | 0.222 | 0.940 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -0.78 | 2.24 | -0.35 | 0.729 | 0.997 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 1.06 | 2.21 | 0.48 | 0.631 | 0.997 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 1.91 | 2.20 | 0.87 | 0.386 | 0.987 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 4.78 | 2.43 | 1.96 | 0.050 | 0.600 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -2.95 | 2.11 | -1.40 | 0.161 | 0.914 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.00 | 2.12 | -0.47 | 0.638 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.84 | 2.11 | 0.40 | 0.691 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 1.68 | 2.08 | 0.81 | 0.419 | 0.987 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 4.56 | 2.33 | 1.96 | 0.050 | 0.600 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.95 | 2.10 | 0.93 | 0.352 | 0.987 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 3.79 | 2.09 | 1.82 | 0.069 | 0.683 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 4.64 | 2.07 | 2.23 | 0.025 | 0.387 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 7.51 | 2.33 | 3.22 | 0.001 | 0.027 | * |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 1.84 | 2.09 | 0.88 | 0.378 | 0.987 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 2.68 | 2.07 | 1.30 | 0.195 | 0.940 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 5.56 | 2.36 | 2.36 | 0.018 | 0.309 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.84 | 2.04 | 0.41 | 0.680 | 0.997 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 3.72 | 2.32 | 1.60 | 0.109 | 0.824 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 2.87 | 2.28 | 1.26 | 0.207 | 0.940 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.14, *p* = 0.098, η²_G = 0.321
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.52 | 3 | = 0.669 | -0.21 [-0.72, 0.72] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -3.00 | 3 | = 0.487 | -0.66 [-1.14, 0.44] | medium | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 0.00 | 3 | = 1.000 | 0.00 [-1.28, 0.34] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.58 | 3 | = 0.669 | 0.33 [-0.52, 0.92] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 1.57 | 3 | = 0.487 | 0.56 [-0.11, 1.49] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 1.58 | 3 | = 0.487 | 1.45 [-0.19, 1.71] | large | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.00 | 3 | = 0.587 | -0.46 [-1.10, 0.30] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 1.00 | 3 | = 0.587 | 0.24 [-0.93, 0.51] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 0.68 | 3 | = 0.669 | 0.51 [-0.67, 0.77] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.41 | 3 | = 0.487 | 0.77 [-0.22, 1.20] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.73 | 3 | = 0.487 | 1.73 [-0.13, 1.60] | large | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.57 | 3 | = 0.487 | 0.77 [-0.42, 0.86] | medium | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 1.32 | 3 | = 0.487 | 0.89 [-0.26, 1.14] | large | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 2.32 | 3 | = 0.487 | 1.22 [-0.19, 1.24] | large | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 2.61 | 3 | = 0.487 | 2.31 [-0.03, 2.02] | large | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 0.58 | 3 | = 0.669 | 0.36 [-0.28, 1.12] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 1.57 | 3 | = 0.487 | 0.62 [-0.59, 0.75] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.70 | 3 | = 0.487 | 1.65 [-0.21, 1.97] | large | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.52 | 3 | = 0.669 | 0.16 [-0.36, 1.02] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.32 | 3 | = 0.487 | 0.86 [-0.29, 1.54] | large | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.93 | 3 | = 0.592 | 0.77 [-0.34, 1.28] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 262.72, BIC = 288.26
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.22, *SE* = 0.295, *z* = -0.733, *p* = 0.464
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.25, *SE* = 0.297, *z* = 0.848, *p* = 0.397
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.46, *SE* = 0.298, *z* = 1.544, *p* = 0.123
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.02, *SE* = 0.295, *z* = -0.077, *p* = 0.938
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.21, *SE* = 0.293, *z* = 0.713, *p* = 0.476
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.67, *SE* = 0.322, *z* = 2.089, *p* = 0.037
- **SNR**: *β* = 0.31, *SE* = 0.037, *z* = 8.356, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.22 | 0.29 | 0.73 | 0.464 | 0.989 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -0.25 | 0.30 | -0.85 | 0.397 | 0.989 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -0.46 | 0.30 | -1.54 | 0.123 | 0.860 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.02 | 0.29 | 0.08 | 0.938 | 0.989 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -0.21 | 0.29 | -0.71 | 0.476 | 0.989 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -0.67 | 0.32 | -2.09 | 0.037 | 0.490 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.47 | 0.28 | -1.67 | 0.095 | 0.796 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.68 | 0.28 | -2.40 | 0.017 | 0.283 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.19 | 0.28 | -0.69 | 0.492 | 0.989 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -0.42 | 0.28 | -1.53 | 0.126 | 0.860 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.89 | 0.31 | -2.88 | 0.004 | 0.079 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.21 | 0.28 | -0.75 | 0.453 | 0.989 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 0.27 | 0.28 | 0.99 | 0.323 | 0.986 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 0.04 | 0.28 | 0.16 | 0.877 | 0.989 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.42 | 0.31 | -1.36 | 0.174 | 0.899 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.48 | 0.28 | 1.74 | 0.082 | 0.764 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.25 | 0.28 | 0.91 | 0.361 | 0.989 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.21 | 0.31 | -0.68 | 0.498 | 0.989 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.23 | 0.27 | -0.85 | 0.395 | 0.989 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.69 | 0.31 | -2.26 | 0.024 | 0.364 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.46 | 0.30 | -1.54 | 0.125 | 0.860 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.881, η²_G = 0.038
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.73 | 3 | = 0.887 | -0.14 [-0.76, 0.68] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.69 | 3 | = 0.887 | -0.16 [-0.64, 0.91] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.68 | 3 | = 0.887 | -0.34 [-0.86, 0.68] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.86 | 3 | = 0.887 | 0.24 [-0.44, 1.01] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -0.48 | 3 | = 0.887 | -0.14 [-0.63, 0.80] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.53 | 3 | = 0.887 | -0.30 [-1.20, 0.52] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.08 | 3 | = 0.999 | -0.01 [-1.03, 0.35] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.54 | 3 | = 0.887 | -0.20 [-1.11, 0.37] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.54 | 3 | = 0.887 | 0.37 [-0.67, 0.77] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.00 | 3 | = 0.999 | -0.00 [-0.94, 0.43] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -0.47 | 3 | = 0.887 | -0.21 [-1.16, 0.43] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.41 | 3 | = 0.887 | -0.20 [-0.81, 0.47] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 1.61 | 3 | = 0.887 | 0.42 [-0.55, 0.80] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 0.03 | 3 | = 0.999 | 0.01 [-0.36, 1.02] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -0.41 | 3 | = 0.887 | -0.21 [-1.01, 0.67] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 1.46 | 3 | = 0.887 | 0.57 [-0.33, 1.06] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.56 | 3 | = 0.887 | 0.21 [-0.21, 1.21] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.23 | 3 | = 0.974 | -0.07 [-0.80, 1.06] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.03 | 3 | = 0.887 | -0.38 [-1.16, 0.25] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.86 | 3 | = 0.887 | -0.44 [-1.37, 0.40] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.40 | 3 | = 0.887 | -0.21 [-0.90, 0.64] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1236.07, BIC = 1264.43
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 14.22, *SE* = 10.127, *z* = 1.405, *p* = 0.160
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 8.45, *SE* = 9.854, *z* = 0.857, *p* = 0.391
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.12, *SE* = 10.110, *z* = -0.210, *p* = 0.834
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 21.38, *SE* = 10.124, *z* = 2.111, *p* = 0.035
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 15.51, *SE* = 10.222, *z* = 1.517, *p* = 0.129
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.36, *SE* = 9.345, *z* = -0.360, *p* = 0.719
- **SNR**: *β* = 0.62, *SE* = 0.755, *z* = 0.820, *p* = 0.412

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -14.22 | 10.13 | -1.40 | 0.160 | 0.897 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -8.45 | 9.85 | -0.86 | 0.391 | 0.989 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 2.12 | 10.11 | 0.21 | 0.834 | 0.995 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -21.38 | 10.12 | -2.11 | 0.035 | 0.489 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -15.51 | 10.22 | -1.52 | 0.129 | 0.856 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 3.36 | 9.35 | 0.36 | 0.719 | 0.994 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 5.78 | 9.31 | 0.62 | 0.535 | 0.992 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 16.34 | 9.23 | 1.77 | 0.077 | 0.697 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -7.15 | 9.61 | -0.74 | 0.457 | 0.992 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -1.29 | 9.35 | -0.14 | 0.891 | 0.995 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 17.59 | 9.13 | 1.93 | 0.054 | 0.612 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 10.57 | 9.42 | 1.12 | 0.262 | 0.952 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -12.93 | 9.64 | -1.34 | 0.180 | 0.907 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -7.06 | 9.51 | -0.74 | 0.458 | 0.992 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 11.81 | 9.01 | 1.31 | 0.190 | 0.907 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -23.50 | 9.71 | -2.42 | 0.016 | 0.269 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -17.63 | 9.54 | -1.85 | 0.065 | 0.656 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 1.24 | 9.15 | 0.14 | 0.892 | 0.995 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 5.87 | 9.80 | 0.60 | 0.549 | 0.992 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 24.74 | 9.32 | 2.65 | 0.008 | 0.155 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 18.87 | 9.32 | 2.03 | 0.043 | 0.545 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.228, η²_G = 0.067
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -2.21 | 12 | = 0.432 | -0.65 [-1.15, 0.00] | medium | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.67 | 12 | = 0.776 | -0.24 [-0.77, 0.31] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 0.40 | 12 | = 0.814 | 0.12 [-0.51, 0.60] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -1.65 | 12 | = 0.439 | -0.55 [-1.04, 0.17] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -1.06 | 12 | = 0.649 | -0.39 [-0.97, 0.18] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 0.00 | 12 | = 1.000 | 0.00 [-0.54, 0.53] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 2.06 | 12 | = 0.432 | 0.40 [-0.10, 0.97] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.11 | 12 | = 0.432 | 0.76 [0.03, 1.15] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.08 | 12 | = 0.987 | -0.02 [-0.75, 0.33] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 0.49 | 12 | = 0.781 | 0.16 [-0.54, 0.49] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.55 | 12 | = 0.439 | 0.55 [-0.07, 0.97] | medium | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.98 | 12 | = 0.650 | 0.35 [-0.19, 0.90] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -1.47 | 12 | = 0.439 | -0.35 [-1.11, 0.07] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.53 | 12 | = 0.781 | -0.18 [-0.69, 0.38] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.69 | 12 | = 0.776 | 0.20 [-0.17, 0.85] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -1.77 | 12 | = 0.439 | -0.65 [-1.14, 0.05] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -1.66 | 12 | = 0.439 | -0.50 [-1.10, 0.08] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.28 | 12 | = 0.867 | -0.10 [-0.53, 0.50] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.52 | 12 | = 0.781 | 0.15 [-0.36, 0.76] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.39 | 12 | = 0.443 | 0.49 [-0.10, 1.02] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.93 | 12 | = 0.650 | 0.35 [-0.05, 1.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 464.32, BIC = 492.68
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.59, *SE* = 0.433, *z* = 1.358, *p* = 0.175
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.49, *SE* = 0.416, *z* = 3.580, *p* < .001
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.88, *SE* = 0.430, *z* = 4.363, *p* < .001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.57, *SE* = 0.425, *z* = 1.331, *p* = 0.183
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.59, *SE* = 0.433, *z* = 3.683, *p* < .001
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.53, *SE* = 0.400, *z* = 3.824, *p* < .001
- **SNR**: *β* = 0.29, *SE* = 0.035, *z* = 8.152, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -0.59 | 0.43 | -1.36 | 0.175 | 0.822 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -1.49 | 0.42 | -3.58 | < .001 | 0.006 | ** |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -1.88 | 0.43 | -4.36 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.57 | 0.43 | -1.33 | 0.183 | 0.822 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -1.59 | 0.43 | -3.68 | < .001 | 0.004 | ** |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -1.53 | 0.40 | -3.82 | < .001 | 0.003 | ** |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.90 | 0.39 | -2.30 | 0.021 | 0.210 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.29 | 0.39 | -3.34 | < .001 | 0.014 | * |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.02 | 0.40 | 0.05 | 0.957 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -1.01 | 0.39 | -2.58 | 0.010 | 0.139 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.94 | 0.39 | -2.43 | 0.015 | 0.171 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.39 | 0.40 | -0.98 | 0.325 | 0.936 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 0.92 | 0.40 | 2.29 | 0.022 | 0.210 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.11 | 0.40 | -0.26 | 0.792 | 0.998 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.04 | 0.38 | -0.10 | 0.917 | 0.998 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 1.31 | 0.41 | 3.22 | 0.001 | 0.021 | * |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.28 | 0.40 | 0.71 | 0.477 | 0.961 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 0.35 | 0.39 | 0.90 | 0.366 | 0.936 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -1.03 | 0.41 | -2.51 | 0.012 | 0.157 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.96 | 0.39 | -2.45 | 0.014 | 0.171 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.07 | 0.39 | 0.17 | 0.867 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.20, *p* < .001, η²_G = 0.183
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -3.84 | 12 | = 0.022 | -1.20 [-1.44, -0.21] | large | * |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -3.54 | 12 | = 0.022 | -1.35 [-1.54, -0.27] | large | * |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -3.52 | 12 | = 0.022 | -1.35 [-1.64, -0.30] | large | * |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -2.43 | 12 | = 0.095 | -0.81 [-1.25, 0.01] | large | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -5.82 | 12 | = 0.002 | -1.55 [-2.10, -0.57] | large | ** |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -3.23 | 12 | = 0.025 | -1.27 [-1.38, -0.17] | large | * |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.33 | 12 | = 0.823 | -0.07 [-0.77, 0.28] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -1.49 | 12 | = 0.245 | -0.33 [-1.10, 0.01] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.79 | 12 | = 0.193 | 0.30 [-0.06, 1.07] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -1.78 | 12 | = 0.193 | -0.33 [-1.08, 0.02] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -0.00 | 12 | = 0.997 | -0.00 [-0.64, 0.36] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.27 | 12 | = 0.319 | -0.29 [-0.96, 0.15] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 2.00 | 12 | = 0.160 | 0.38 [0.03, 1.25] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -1.04 | 12 | = 0.392 | -0.27 [-0.76, 0.31] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.48 | 12 | = 0.748 | 0.07 [-0.23, 0.79] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 2.17 | 12 | = 0.134 | 0.58 [0.08, 1.32] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.20 | 12 | = 0.890 | 0.05 [-0.45, 0.66] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.64 | 12 | = 0.221 | 0.34 [-0.08, 1.00] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -3.39 | 12 | = 0.022 | -0.61 [-1.70, -0.34] | medium | * |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.48 | 12 | = 0.245 | -0.31 [-1.08, 0.05] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.21 | 12 | = 0.329 | 0.34 [-0.26, 0.79] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.007) (no significant pairwise comparisons)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.098)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 1 (no 1) (*d* = -1.20)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 2 (no 1) (*d* = -1.35)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 3 (no 1) (*d* = -1.35)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -1.55)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 3 (no 1) (*d* = -1.27)
  - Increase by 1 (no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -0.61)

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
