# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:25:54

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
| Cardinality (no change, no 1) | 24 | 105.83 ms | 7.27 | 1.48 | [92.00, 112.00] |
| Decrease by 1 (no 1) | 24 | 103.33 ms | 7.43 | 1.52 | [92.00, 112.00] |
| Decrease by 2 (no 1) | 24 | 105.17 ms | 7.60 | 1.55 | [92.00, 112.00] |
| Decrease by 3 (no 1) | 24 | 103.33 ms | 7.97 | 1.63 | [92.00, 112.00] |
| Increase by 1 (no 1) | 24 | 101.83 ms | 7.64 | 1.56 | [92.00, 112.00] |
| Increase by 2 (no 1) | 24 | 101.83 ms | 7.73 | 1.58 | [92.00, 112.00] |
| Increase by 3 (no 1) | 24 | 101.50 ms | 8.16 | 1.66 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | -1.22 µV | 1.53 | 0.31 | [-4.72, 0.98] |
| Decrease by 1 (no 1) | 24 | -0.88 µV | 1.71 | 0.35 | [-5.59, 2.14] |
| Decrease by 2 (no 1) | 24 | -1.49 µV | 1.50 | 0.31 | [-5.60, 2.21] |
| Decrease by 3 (no 1) | 24 | -1.62 µV | 1.87 | 0.38 | [-6.28, 2.33] |
| Increase by 1 (no 1) | 24 | -1.14 µV | 1.10 | 0.22 | [-3.26, 1.02] |
| Increase by 2 (no 1) | 24 | -1.33 µV | 1.30 | 0.26 | [-3.67, 0.34] |
| Increase by 3 (no 1) | 24 | -1.05 µV | 1.71 | 0.35 | [-6.02, 3.05] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 173.00 ms | 19.25 | 3.93 | [140.00, 208.00] |
| Decrease by 1 (no 1) | 24 | 174.00 ms | 17.77 | 3.63 | [140.00, 208.00] |
| Decrease by 2 (no 1) | 24 | 172.83 ms | 16.13 | 3.29 | [140.00, 208.00] |
| Decrease by 3 (no 1) | 24 | 175.00 ms | 16.98 | 3.47 | [148.00, 208.00] |
| Increase by 1 (no 1) | 24 | 170.83 ms | 19.96 | 4.08 | [140.00, 208.00] |
| Increase by 2 (no 1) | 24 | 168.50 ms | 17.51 | 3.57 | [140.00, 200.00] |
| Increase by 3 (no 1) | 24 | 170.17 ms | 20.50 | 4.18 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | -5.08 µV | 2.35 | 0.48 | [-10.60, -0.82] |
| Decrease by 1 (no 1) | 24 | -5.37 µV | 2.03 | 0.41 | [-9.50, -2.05] |
| Decrease by 2 (no 1) | 24 | -5.49 µV | 2.17 | 0.44 | [-9.98, -1.47] |
| Decrease by 3 (no 1) | 24 | -6.24 µV | 2.41 | 0.49 | [-10.22, -1.96] |
| Increase by 1 (no 1) | 24 | -5.08 µV | 2.20 | 0.45 | [-9.40, -0.93] |
| Increase by 2 (no 1) | 24 | -5.27 µV | 2.60 | 0.53 | [-10.89, -0.50] |
| Increase by 3 (no 1) | 24 | -6.12 µV | 2.41 | 0.49 | [-13.18, -2.28] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 102.67 ms | 9.11 | 1.86 | [92.00, 112.00] |
| Decrease by 1 (no 1) | 24 | 104.00 ms | 8.83 | 1.80 | [92.00, 112.00] |
| Decrease by 2 (no 1) | 24 | 107.33 ms | 7.33 | 1.50 | [92.00, 112.00] |
| Decrease by 3 (no 1) | 24 | 103.17 ms | 8.83 | 1.80 | [92.00, 112.00] |
| Increase by 1 (no 1) | 24 | 102.33 ms | 7.91 | 1.61 | [92.00, 112.00] |
| Increase by 2 (no 1) | 24 | 101.83 ms | 8.08 | 1.65 | [92.00, 112.00] |
| Increase by 3 (no 1) | 24 | 100.50 ms | 7.94 | 1.62 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 1.02 µV | 1.83 | 0.37 | [-1.52, 4.97] |
| Decrease by 1 (no 1) | 24 | 0.65 µV | 1.97 | 0.40 | [-2.35, 4.96] |
| Decrease by 2 (no 1) | 24 | 1.17 µV | 1.88 | 0.38 | [-3.30, 4.83] |
| Decrease by 3 (no 1) | 24 | 1.45 µV | 1.70 | 0.35 | [-1.66, 6.10] |
| Increase by 1 (no 1) | 24 | 1.15 µV | 1.43 | 0.29 | [-0.82, 4.52] |
| Increase by 2 (no 1) | 24 | 1.29 µV | 1.54 | 0.31 | [-1.64, 4.54] |
| Increase by 3 (no 1) | 24 | 1.16 µV | 2.19 | 0.45 | [-1.54, 9.07] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 464.67 ms | 26.97 | 5.50 | [416.00, 516.00] |
| Decrease by 1 (no 1) | 24 | 488.83 ms | 31.27 | 6.38 | [424.00, 532.00] |
| Decrease by 2 (no 1) | 24 | 474.83 ms | 30.66 | 6.26 | [436.00, 532.00] |
| Decrease by 3 (no 1) | 24 | 472.17 ms | 32.40 | 6.61 | [416.00, 532.00] |
| Increase by 1 (no 1) | 24 | 481.67 ms | 36.41 | 7.43 | [416.00, 532.00] |
| Increase by 2 (no 1) | 24 | 486.83 ms | 35.18 | 7.18 | [416.00, 532.00] |
| Increase by 3 (no 1) | 24 | 467.33 ms | 40.19 | 8.20 | [416.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 1.33 µV | 2.79 | 0.57 | [-4.73, 6.88] |
| Decrease by 1 (no 1) | 24 | 3.30 µV | 3.26 | 0.66 | [-2.96, 9.46] |
| Decrease by 2 (no 1) | 24 | 3.56 µV | 3.10 | 0.63 | [-1.49, 8.74] |
| Decrease by 3 (no 1) | 24 | 4.15 µV | 3.76 | 0.77 | [-1.41, 13.58] |
| Increase by 1 (no 1) | 24 | 2.41 µV | 3.45 | 0.70 | [-3.76, 8.98] |
| Increase by 2 (no 1) | 24 | 3.80 µV | 3.53 | 0.72 | [-3.29, 10.75] |
| Increase by 3 (no 1) | 24 | 3.99 µV | 2.39 | 0.49 | [0.81, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1120.01, BIC = 1151.25
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.76, *SE* = 1.626, *z* = -1.700, *p* = 0.089
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.67, *SE* = 1.623, *z* = -0.410, *p* = 0.682
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.44, *SE* = 1.623, *z* = -1.505, *p* = 0.132
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.73, *SE* = 1.626, *z* = -2.292, *p* = 0.022
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.94, *SE* = 1.623, *z* = -2.427, *p* = 0.015
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.01, *SE* = 1.628, *z* = -2.466, *p* = 0.014
- **SNR**: *β* = 0.71, *SE* = 0.284, *z* = 2.511, *p* = 0.012

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 2.76 | 1.63 | 1.70 | 0.089 | 0.753 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.67 | 1.62 | 0.41 | 0.682 | 0.997 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 2.44 | 1.62 | 1.50 | 0.132 | 0.863 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 3.73 | 1.63 | 2.29 | 0.022 | 0.343 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 3.94 | 1.62 | 2.43 | 0.015 | 0.264 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 4.01 | 1.63 | 2.47 | 0.014 | 0.251 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -2.10 | 1.63 | -1.29 | 0.197 | 0.942 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.32 | 1.63 | -0.20 | 0.843 | 0.999 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.96 | 1.64 | 0.59 | 0.556 | 0.994 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 1.17 | 1.63 | 0.72 | 0.471 | 0.994 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 1.25 | 1.64 | 0.76 | 0.446 | 0.994 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.78 | 1.62 | 1.09 | 0.274 | 0.978 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 3.06 | 1.63 | 1.88 | 0.060 | 0.627 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 3.27 | 1.62 | 2.02 | 0.044 | 0.533 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 3.35 | 1.63 | 2.06 | 0.040 | 0.517 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 1.29 | 1.62 | 0.79 | 0.429 | 0.994 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 1.50 | 1.62 | 0.92 | 0.357 | 0.988 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 1.57 | 1.63 | 0.97 | 0.334 | 0.988 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.21 | 1.62 | 0.13 | 0.897 | 0.999 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.29 | 1.62 | 0.18 | 0.860 | 0.999 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.08 | 1.63 | 0.05 | 0.963 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.04, *p* = 0.064, η²_G = 0.042
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 1.84 | 23 | = 0.274 | 0.34 [-0.06, 0.81] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 0.45 | 23 | = 0.810 | 0.09 [-0.33, 0.52] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 1.61 | 23 | = 0.320 | 0.33 [-0.11, 0.76] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 2.89 | 23 | = 0.112 | 0.54 [0.13, 1.05] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 2.50 | 23 | = 0.139 | 0.53 [0.06, 0.96] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 2.78 | 23 | = 0.112 | 0.56 [0.11, 1.02] | medium | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.19 | 23 | = 0.547 | -0.24 [-0.67, 0.19] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.04 | 23 | = 0.547 | 0.20 [-0.21, 0.64] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.00 | 23 | = 0.547 | 0.20 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.03 | 23 | = 0.547 | 0.24 [-0.22, 0.64] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.86 | 23 | = 0.547 | 0.24 [-0.25, 0.60] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 1.76 | 23 | = 0.274 | 0.44 [-0.08, 0.80] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 1.81 | 23 | = 0.274 | 0.43 [-0.07, 0.81] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.89 | 23 | = 0.274 | 0.47 [-0.05, 0.82] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 0.83 | 23 | = 0.547 | 0.19 [-0.26, 0.59] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.84 | 23 | = 0.547 | 0.19 [-0.25, 0.60] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.91 | 23 | = 0.547 | 0.23 [-0.24, 0.61] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.28 | 23 | = 0.910 | 0.04 [-0.36, 0.48] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.19 | 23 | = 0.943 | 0.04 [-0.38, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 558.98, BIC = 590.22
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.41, *SE* = 0.304, *z* = 1.344, *p* = 0.179
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.27, *SE* = 0.304, *z* = -0.886, *p* = 0.376
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.42, *SE* = 0.304, *z* = -1.386, *p* = 0.166
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.00, *SE* = 0.304, *z* = -0.002, *p* = 0.998
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.13, *SE* = 0.304, *z* = -0.415, *p* = 0.678
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.08, *SE* = 0.305, *z* = 0.275, *p* = 0.783
- **SNR**: *β* = -0.19, *SE* = 0.055, *z* = -3.511, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -0.41 | 0.30 | -1.34 | 0.179 | 0.954 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.27 | 0.30 | 0.89 | 0.376 | 0.991 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 0.42 | 0.30 | 1.39 | 0.166 | 0.954 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.00 | 0.30 | 0.00 | 0.998 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.13 | 0.30 | 0.41 | 0.678 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -0.08 | 0.30 | -0.28 | 0.783 | 0.999 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.68 | 0.30 | 2.23 | 0.026 | 0.408 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.83 | 0.30 | 2.72 | 0.006 | 0.127 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.41 | 0.31 | 1.34 | 0.181 | 0.954 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.54 | 0.30 | 1.76 | 0.079 | 0.791 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 0.33 | 0.31 | 1.06 | 0.289 | 0.983 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.15 | 0.30 | 0.50 | 0.617 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.27 | 0.30 | -0.88 | 0.378 | 0.991 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.14 | 0.30 | -0.47 | 0.638 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.35 | 0.30 | -1.16 | 0.247 | 0.975 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -0.42 | 0.30 | -1.38 | 0.167 | 0.954 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -0.30 | 0.30 | -0.97 | 0.331 | 0.988 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.51 | 0.30 | -1.66 | 0.097 | 0.841 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.13 | 0.30 | 0.41 | 0.680 | 0.999 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.08 | 0.30 | -0.28 | 0.781 | 0.999 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.21 | 0.30 | -0.69 | 0.490 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.264, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -1.26 | 23 | = 0.657 | -0.21 [-0.69, 0.17] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 0.95 | 23 | = 0.739 | 0.18 [-0.23, 0.62] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 1.28 | 23 | = 0.657 | 0.24 [-0.17, 0.69] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -0.29 | 23 | = 0.774 | -0.05 [-0.48, 0.36] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.42 | 23 | = 0.774 | 0.08 [-0.34, 0.51] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.50 | 23 | = 0.774 | -0.10 [-0.53, 0.32] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.89 | 23 | = 0.503 | 0.38 [-0.05, 0.82] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.39 | 23 | = 0.503 | 0.42 [0.04, 0.93] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 0.88 | 23 | = 0.739 | 0.18 [-0.25, 0.61] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.49 | 23 | = 0.652 | 0.30 [-0.13, 0.74] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 0.59 | 23 | = 0.774 | 0.10 [-0.30, 0.54] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.36 | 23 | = 0.774 | 0.08 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -1.17 | 23 | = 0.668 | -0.26 [-0.67, 0.19] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.45 | 23 | = 0.774 | -0.11 [-0.51, 0.33] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -1.09 | 23 | = 0.674 | -0.27 [-0.65, 0.21] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -1.47 | 23 | = 0.652 | -0.31 [-0.73, 0.13] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -0.82 | 23 | = 0.739 | -0.18 [-0.59, 0.26] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -1.96 | 23 | = 0.503 | -0.32 [-0.84, 0.04] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.68 | 23 | = 0.750 | 0.15 [-0.28, 0.56] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.30 | 23 | = 0.774 | -0.07 [-0.48, 0.36] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.75 | 23 | = 0.749 | -0.18 [-0.58, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1351.02, BIC = 1382.26
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.04, *SE* = 3.055, *z* = 0.339, *p* = 0.734
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.14, *SE* = 3.047, *z* = -0.045, *p* = 0.964
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.00, *SE* = 3.032, *z* = 0.660, *p* = 0.510
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.15, *SE* = 3.034, *z* = -0.710, *p* = 0.478
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.50, *SE* = 3.032, *z* = -1.484, *p* = 0.138
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.85, *SE* = 3.035, *z* = -0.938, *p* = 0.348
- **SNR**: *β* = -0.03, *SE* = 0.258, *z* = -0.099, *p* = 0.921

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -1.04 | 3.05 | -0.34 | 0.734 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.14 | 3.05 | 0.04 | 0.964 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -2.00 | 3.03 | -0.66 | 0.510 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 2.16 | 3.03 | 0.71 | 0.478 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 4.50 | 3.03 | 1.48 | 0.138 | 0.931 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 2.85 | 3.04 | 0.94 | 0.348 | 0.996 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 1.17 | 3.03 | 0.39 | 0.699 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.96 | 3.05 | -0.32 | 0.753 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 3.19 | 3.04 | 1.05 | 0.294 | 0.992 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 5.54 | 3.06 | 1.81 | 0.070 | 0.765 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 3.88 | 3.08 | 1.26 | 0.207 | 0.969 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.14 | 3.05 | -0.70 | 0.483 | 0.998 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 2.02 | 3.04 | 0.66 | 0.506 | 0.998 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 4.36 | 3.05 | 1.43 | 0.152 | 0.940 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 2.71 | 3.06 | 0.88 | 0.376 | 0.997 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 4.15 | 3.03 | 1.37 | 0.171 | 0.950 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 6.50 | 3.03 | 2.14 | 0.032 | 0.495 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 4.85 | 3.04 | 1.60 | 0.110 | 0.891 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 2.35 | 3.03 | 0.77 | 0.440 | 0.998 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.69 | 3.04 | 0.23 | 0.820 | 0.998 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -1.65 | 3.04 | -0.54 | 0.586 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.365, η²_G = 0.014
- Greenhouse-Geisser corrected: *p* = 0.360 (ε = 0.637)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.53 | 23 | = 0.704 | -0.05 [-0.53, 0.32] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 0.09 | 23 | = 0.933 | 0.01 [-0.40, 0.44] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.57 | 23 | = 0.704 | -0.11 [-0.54, 0.31] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.73 | 23 | = 0.704 | 0.11 [-0.28, 0.57] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 1.27 | 23 | = 0.704 | 0.24 [-0.17, 0.69] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 0.99 | 23 | = 0.704 | 0.14 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.75 | 23 | = 0.704 | 0.07 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.32 | 23 | = 0.825 | -0.06 [-0.49, 0.36] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 0.97 | 23 | = 0.704 | 0.17 [-0.23, 0.62] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.89 | 23 | = 0.704 | 0.31 [-0.05, 0.82] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.38 | 23 | = 0.704 | 0.20 [-0.15, 0.71] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.72 | 23 | = 0.704 | -0.13 [-0.57, 0.28] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 0.57 | 23 | = 0.704 | 0.11 [-0.31, 0.54] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 1.39 | 23 | = 0.704 | 0.26 [-0.15, 0.71] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.83 | 23 | = 0.704 | 0.14 [-0.26, 0.59] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 1.02 | 23 | = 0.704 | 0.22 [-0.22, 0.63] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 1.67 | 23 | = 0.704 | 0.38 [-0.09, 0.78] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.22 | 23 | = 0.704 | 0.26 [-0.18, 0.68] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.78 | 23 | = 0.704 | 0.12 [-0.27, 0.58] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.27 | 23 | = 0.825 | 0.03 [-0.37, 0.48] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.55 | 23 | = 0.704 | -0.09 [-0.54, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 593.09, BIC = 624.33
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.05, *SE* = 0.316, *z* = -0.172, *p* = 0.863
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.22, *SE* = 0.315, *z* = -0.708, *p* = 0.479
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.16, *SE* = 0.313, *z* = -3.694, *p* < .001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.07, *SE* = 0.313, *z* = 0.236, *p* = 0.813
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.19, *SE* = 0.313, *z* = -0.598, *p* = 0.550
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.13, *SE* = 0.314, *z* = -3.597, *p* < .001
- **SNR**: *β* = -0.16, *SE* = 0.027, *z* = -5.889, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.05 | 0.32 | 0.17 | 0.863 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.22 | 0.31 | 0.71 | 0.479 | 0.997 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 1.16 | 0.31 | 3.69 | < .001 | 0.004 | ** |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.07 | 0.31 | -0.24 | 0.813 | 0.999 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.19 | 0.31 | 0.60 | 0.550 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 1.13 | 0.31 | 3.60 | < .001 | 0.006 | ** |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.17 | 0.31 | 0.54 | 0.591 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.10 | 0.32 | 3.49 | < .001 | 0.008 | ** |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.13 | 0.31 | -0.41 | 0.683 | 0.999 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.13 | 0.32 | 0.42 | 0.674 | 0.999 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 1.07 | 0.32 | 3.38 | < .001 | 0.012 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.93 | 0.31 | 2.97 | 0.003 | 0.038 | * |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.30 | 0.31 | -0.95 | 0.344 | 0.990 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.04 | 0.31 | -0.11 | 0.910 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 0.90 | 0.32 | 2.86 | 0.004 | 0.050 | * |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -1.23 | 0.31 | -3.93 | < .001 | 0.002 | ** |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -0.97 | 0.31 | -3.10 | 0.002 | 0.029 | * |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.03 | 0.31 | -0.09 | 0.926 | 0.999 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.26 | 0.31 | 0.83 | 0.405 | 0.994 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.20 | 0.31 | 3.82 | < .001 | 0.003 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.94 | 0.31 | 3.00 | 0.003 | 0.037 | * |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.70, *p* = 0.002, η²_G = 0.036
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 0.93 | 23 | = 0.573 | 0.13 [-0.24, 0.62] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 1.15 | 23 | = 0.459 | 0.18 [-0.19, 0.66] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 3.01 | 23 | = 0.038 | 0.49 [0.15, 1.07] | small | * |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -0.01 | 23 | = 0.991 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.69 | 23 | = 0.697 | 0.07 [-0.28, 0.56] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 3.18 | 23 | = 0.038 | 0.44 [0.19, 1.11] | small | * |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.36 | 23 | = 0.833 | 0.06 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.29 | 23 | = 0.074 | 0.39 [0.02, 0.91] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.89 | 23 | = 0.573 | -0.14 [-0.61, 0.24] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.31 | 23 | = 0.833 | -0.04 [-0.49, 0.36] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 2.38 | 23 | = 0.074 | 0.34 [0.04, 0.93] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.34 | 23 | = 0.074 | 0.33 [0.03, 0.92] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -1.18 | 23 | = 0.459 | -0.19 [-0.67, 0.19] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.59 | 23 | = 0.734 | -0.09 [-0.54, 0.30] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.53 | 23 | = 0.294 | 0.28 [-0.12, 0.74] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -3.03 | 23 | = 0.038 | -0.50 [-1.08, -0.16] | medium | * |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -2.67 | 23 | = 0.058 | -0.39 [-1.00, -0.09] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.26 | 23 | = 0.833 | -0.05 [-0.48, 0.37] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.53 | 23 | = 0.747 | 0.08 [-0.32, 0.53] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.95 | 23 | = 0.038 | 0.45 [0.14, 1.06] | small | * |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.53 | 23 | = 0.065 | 0.34 [0.07, 0.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1147.61, BIC = 1178.85
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.31, *SE* = 1.752, *z* = 0.746, *p* = 0.455
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 4.71, *SE* = 1.753, *z* = 2.683, *p* = 0.007
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.59, *SE* = 1.763, *z* = 0.334, *p* = 0.739
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.22, *SE* = 1.772, *z* = -0.123, *p* = 0.902
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.73, *SE* = 1.767, *z* = -0.414, *p* = 0.679
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.06, *SE* = 1.770, *z* = -1.162, *p* = 0.245
- **SNR**: *β* = 0.10, *SE* = 0.241, *z* = 0.426, *p* = 0.670

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -1.31 | 1.75 | -0.75 | 0.455 | 0.995 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -4.70 | 1.75 | -2.68 | 0.007 | 0.123 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -0.59 | 1.76 | -0.33 | 0.739 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.22 | 1.77 | 0.12 | 0.902 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.73 | 1.77 | 0.41 | 0.679 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 2.06 | 1.77 | 1.16 | 0.245 | 0.974 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -3.40 | 1.76 | -1.93 | 0.053 | 0.583 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.72 | 1.77 | 0.41 | 0.685 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 1.53 | 1.78 | 0.86 | 0.392 | 0.993 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 2.04 | 1.78 | 1.15 | 0.251 | 0.974 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 3.37 | 1.78 | 1.89 | 0.059 | 0.596 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 4.12 | 1.76 | 2.35 | 0.019 | 0.279 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 4.92 | 1.76 | 2.80 | 0.005 | 0.094 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 5.44 | 1.76 | 3.09 | 0.002 | 0.039 | * |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 6.76 | 1.76 | 3.84 | < .001 | 0.003 | ** |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.81 | 1.75 | 0.46 | 0.645 | 0.998 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 1.32 | 1.75 | 0.75 | 0.451 | 0.995 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 2.65 | 1.75 | 1.51 | 0.131 | 0.860 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.51 | 1.75 | 0.29 | 0.769 | 0.998 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.84 | 1.75 | 1.05 | 0.294 | 0.978 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 1.33 | 1.75 | 0.76 | 0.449 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.90, *p* = 0.011, η²_G = 0.057
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -0.91 | 23 | = 0.555 | -0.15 [-0.61, 0.24] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -2.39 | 23 | = 0.133 | -0.56 [-0.93, -0.04] | medium | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.26 | 23 | = 0.839 | -0.06 [-0.48, 0.37] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.18 | 23 | = 0.858 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.52 | 23 | = 0.759 | 0.10 [-0.32, 0.53] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 1.34 | 23 | = 0.491 | 0.25 [-0.16, 0.70] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.82 | 23 | = 0.244 | -0.41 [-0.81, 0.06] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.38 | 23 | = 0.821 | 0.09 [-0.34, 0.50] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.00 | 23 | = 0.529 | 0.20 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.16 | 23 | = 0.491 | 0.26 [-0.19, 0.67] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 2.07 | 23 | = 0.194 | 0.42 [-0.02, 0.86] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.02 | 23 | = 0.194 | 0.51 [-0.03, 0.85] | medium | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 2.96 | 23 | = 0.049 | 0.66 [0.14, 1.06] | medium | * |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 3.58 | 23 | = 0.024 | 0.71 [0.25, 1.21] | medium | * |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 3.43 | 23 | = 0.024 | 0.89 [0.23, 1.17] | large | * |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 0.51 | 23 | = 0.759 | 0.10 [-0.32, 0.53] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.65 | 23 | = 0.731 | 0.16 [-0.29, 0.56] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.20 | 23 | = 0.491 | 0.32 [-0.18, 0.67] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.32 | 23 | = 0.832 | 0.06 [-0.36, 0.49] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.22 | 23 | = 0.491 | 0.23 [-0.18, 0.68] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.00 | 23 | = 0.529 | 0.17 [-0.22, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 587.41, BIC = 618.65
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.40, *SE* = 0.321, *z* = -1.252, *p* = 0.211
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.20, *SE* = 0.321, *z* = 0.606, *p* = 0.545
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.54, *SE* = 0.323, *z* = 1.683, *p* = 0.092
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.28, *SE* = 0.325, *z* = 0.859, *p* = 0.390
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.40, *SE* = 0.324, *z* = 1.239, *p* = 0.215
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.28, *SE* = 0.324, *z* = 0.849, *p* = 0.396
- **SNR**: *β* = 0.13, *SE* = 0.045, *z* = 2.899, *p* = 0.004

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.40 | 0.32 | 1.25 | 0.211 | 0.971 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -0.19 | 0.32 | -0.61 | 0.545 | 0.997 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -0.54 | 0.32 | -1.68 | 0.092 | 0.788 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.28 | 0.32 | -0.86 | 0.390 | 0.997 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -0.40 | 0.32 | -1.24 | 0.215 | 0.971 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -0.28 | 0.32 | -0.85 | 0.396 | 0.997 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.60 | 0.32 | -1.85 | 0.064 | 0.675 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.95 | 0.32 | -2.91 | 0.004 | 0.073 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.68 | 0.33 | -2.08 | 0.037 | 0.513 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -0.80 | 0.33 | -2.47 | 0.014 | 0.241 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.68 | 0.33 | -2.08 | 0.038 | 0.513 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.35 | 0.32 | -1.09 | 0.278 | 0.985 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.08 | 0.32 | -0.26 | 0.794 | 0.998 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.21 | 0.32 | -0.64 | 0.521 | 0.997 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.08 | 0.32 | -0.25 | 0.802 | 0.998 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.26 | 0.32 | 0.82 | 0.409 | 0.997 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.14 | 0.32 | 0.44 | 0.657 | 0.998 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 0.27 | 0.32 | 0.84 | 0.403 | 0.997 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.12 | 0.32 | -0.38 | 0.703 | 0.998 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.00 | 0.32 | 0.01 | 0.991 | 0.998 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.13 | 0.32 | 0.39 | 0.695 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.12, *p* = 0.355, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 1.03 | 23 | = 0.715 | 0.19 [-0.22, 0.64] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.54 | 23 | = 0.889 | -0.08 [-0.53, 0.31] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -1.29 | 23 | = 0.715 | -0.24 [-0.69, 0.17] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -0.41 | 23 | = 0.889 | -0.08 [-0.51, 0.34] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -0.89 | 23 | = 0.728 | -0.16 [-0.61, 0.24] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.31 | 23 | = 0.889 | -0.07 [-0.49, 0.36] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.71 | 23 | = 0.648 | -0.27 [-0.78, 0.09] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -2.66 | 23 | = 0.297 | -0.43 [-0.99, -0.09] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -1.60 | 23 | = 0.648 | -0.29 [-0.76, 0.11] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -2.33 | 23 | = 0.304 | -0.36 [-0.92, -0.03] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -1.46 | 23 | = 0.657 | -0.24 [-0.73, 0.13] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.97 | 23 | = 0.715 | -0.16 [-0.63, 0.23] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 0.04 | 23 | = 0.991 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.35 | 23 | = 0.889 | -0.07 [-0.49, 0.35] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.02 | 23 | = 0.991 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 1.05 | 23 | = 0.715 | 0.19 [-0.21, 0.64] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.54 | 23 | = 0.889 | 0.10 [-0.31, 0.53] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.99 | 23 | = 0.715 | 0.15 [-0.22, 0.63] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.43 | 23 | = 0.889 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.01 | 23 | = 0.991 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.39 | 23 | = 0.889 | 0.07 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1649.61, BIC = 1680.85
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 24.22, *SE* = 8.282, *z* = 2.924, *p* = 0.003
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 10.20, *SE* = 8.210, *z* = 1.242, *p* = 0.214
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 7.53, *SE* = 8.219, *z* = 0.916, *p* = 0.359
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 17.05, *SE* = 8.270, *z* = 2.061, *p* = 0.039
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 22.20, *SE* = 8.212, *z* = 2.703, *p* = 0.007
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.66, *SE* = 8.176, *z* = 0.326, *p* = 0.745
- **SNR**: *β* = -0.02, *SE* = 0.508, *z* = -0.038, *p* = 0.969

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -24.22 | 8.28 | -2.92 | 0.003 | 0.070 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -10.20 | 8.21 | -1.24 | 0.214 | 0.930 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -7.53 | 8.22 | -0.92 | 0.359 | 0.982 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -17.05 | 8.27 | -2.06 | 0.039 | 0.494 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -22.20 | 8.21 | -2.70 | 0.007 | 0.129 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -2.66 | 8.18 | -0.33 | 0.745 | 0.983 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 14.02 | 8.20 | 1.71 | 0.087 | 0.700 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 16.69 | 8.19 | 2.04 | 0.042 | 0.494 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 7.17 | 8.18 | 0.88 | 0.381 | 0.982 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 2.02 | 8.19 | 0.25 | 0.805 | 0.983 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 21.55 | 8.29 | 2.60 | 0.009 | 0.163 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 2.66 | 8.18 | 0.33 | 0.745 | 0.983 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -6.85 | 8.19 | -0.84 | 0.403 | 0.982 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -12.00 | 8.18 | -1.47 | 0.142 | 0.841 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 7.53 | 8.22 | 0.92 | 0.359 | 0.982 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -9.52 | 8.19 | -1.16 | 0.245 | 0.940 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -14.66 | 8.18 | -1.79 | 0.073 | 0.679 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 4.87 | 8.23 | 0.59 | 0.554 | 0.982 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -5.15 | 8.19 | -0.63 | 0.530 | 0.982 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 14.38 | 8.28 | 1.74 | 0.082 | 0.700 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 19.53 | 8.22 | 2.38 | 0.017 | 0.272 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.54, *p* = 0.023, η²_G = 0.066
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -3.89 | 23 | = 0.016 | -0.83 [-1.28, -0.31] | large | * |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -1.36 | 23 | = 0.412 | -0.35 [-0.71, 0.15] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -1.22 | 23 | = 0.412 | -0.25 [-0.68, 0.18] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -1.87 | 23 | = 0.194 | -0.53 [-0.82, 0.06] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -2.63 | 23 | = 0.094 | -0.71 [-0.99, -0.09] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.29 | 23 | = 0.812 | -0.08 [-0.48, 0.36] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 2.60 | 23 | = 0.094 | 0.45 [0.08, 0.98] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.43 | 23 | = 0.099 | 0.52 [0.05, 0.94] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 0.92 | 23 | = 0.541 | 0.21 [-0.24, 0.61] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 0.24 | 23 | = 0.812 | 0.06 [-0.37, 0.47] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 2.55 | 23 | = 0.094 | 0.60 [0.07, 0.97] | medium | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.33 | 23 | = 0.812 | 0.08 [-0.36, 0.49] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -0.88 | 23 | = 0.541 | -0.20 [-0.61, 0.25] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -1.24 | 23 | = 0.412 | -0.36 [-0.68, 0.18] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.80 | 23 | = 0.566 | 0.21 [-0.26, 0.59] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -0.95 | 23 | = 0.541 | -0.28 [-0.62, 0.23] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -1.95 | 23 | = 0.190 | -0.43 [-0.84, 0.04] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.59 | 23 | = 0.656 | 0.13 [-0.30, 0.54] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.62 | 23 | = 0.656 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.28 | 23 | = 0.412 | 0.37 [-0.17, 0.69] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.04 | 23 | = 0.187 | 0.52 [-0.02, 0.86] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 691.22, BIC = 722.46
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.74, *SE* = 0.413, *z* = 4.215, *p* < .001
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.09, *SE* = 0.409, *z* = 5.123, *p* < .001
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.67, *SE* = 0.409, *z* = 6.518, *p* < .001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.86, *SE* = 0.412, *z* = 2.093, *p* = 0.036
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.33, *SE* = 0.409, *z* = 5.707, *p* < .001
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.67, *SE* = 0.407, *z* = 6.561, *p* < .001
- **SNR**: *β* = 0.09, *SE* = 0.027, *z* = 3.372, *p* = 0.001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -1.74 | 0.41 | -4.21 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -2.09 | 0.41 | -5.12 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -2.67 | 0.41 | -6.52 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.86 | 0.41 | -2.09 | 0.036 | 0.284 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -2.33 | 0.41 | -5.71 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -2.67 | 0.41 | -6.56 | < .001 | < .001 | *** |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.35 | 0.41 | -0.87 | 0.385 | 0.912 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.93 | 0.41 | -2.28 | 0.023 | 0.243 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.88 | 0.41 | 2.16 | 0.031 | 0.270 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -0.59 | 0.41 | -1.46 | 0.146 | 0.716 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.93 | 0.41 | -2.25 | 0.025 | 0.243 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.57 | 0.41 | -1.41 | 0.159 | 0.716 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 1.23 | 0.41 | 3.02 | 0.003 | 0.032 | * |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.24 | 0.41 | -0.59 | 0.556 | 0.912 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.58 | 0.41 | -1.41 | 0.160 | 0.716 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 1.80 | 0.41 | 4.43 | < .001 | < .001 | *** |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.33 | 0.41 | 0.82 | 0.412 | 0.912 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.00 | 0.41 | -0.00 | 0.996 | 0.996 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -1.47 | 0.41 | -3.61 | < .001 | 0.004 | ** |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -1.81 | 0.41 | -4.38 | < .001 | < .001 | *** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.34 | 0.41 | -0.82 | 0.412 | 0.912 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 11.05, *p* < .001, η²_G = 0.081
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.624)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -4.51 | 23 | < .001 | -0.65 [-1.42, -0.42] | medium | *** |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -4.65 | 23 | < .001 | -0.75 [-1.46, -0.44] | medium | *** |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -4.28 | 23 | < .001 | -0.85 [-1.37, -0.38] | large | *** |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -2.20 | 23 | = 0.073 | -0.35 [-0.89, -0.01] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -5.42 | 23 | < .001 | -0.78 [-1.64, -0.57] | medium | *** |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -4.91 | 23 | < .001 | -1.02 [-1.52, -0.48] | large | *** |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.82 | 23 | = 0.519 | -0.08 [-0.59, 0.26] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -1.93 | 23 | = 0.116 | -0.24 [-0.83, 0.04] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 3.25 | 23 | = 0.007 | 0.27 [0.20, 1.13] | small | ** |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -1.72 | 23 | = 0.147 | -0.15 [-0.79, 0.08] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -1.83 | 23 | = 0.130 | -0.24 [-0.81, 0.06] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.46 | 23 | = 0.221 | -0.17 [-0.73, 0.13] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 4.11 | 23 | = 0.001 | 0.35 [0.35, 1.33] | small | ** |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.66 | 23 | = 0.579 | -0.07 [-0.56, 0.29] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -1.28 | 23 | = 0.282 | -0.16 [-0.69, 0.17] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 3.49 | 23 | = 0.005 | 0.48 [0.24, 1.18] | small | ** |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.65 | 23 | = 0.579 | 0.09 [-0.29, 0.56] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.34 | 23 | = 0.738 | 0.05 [-0.35, 0.49] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -4.96 | 23 | < .001 | -0.40 [-1.53, -0.49] | small | *** |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -3.95 | 23 | = 0.002 | -0.53 [-1.29, -0.32] | medium | ** |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.40 | 23 | = 0.731 | -0.06 [-0.50, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Marginal trend toward condition differences (*p* = 0.064)
**N1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed greater amplitude than Decrease by 3 (no 1) (*d* = 0.49)
  - Cardinality (no change, no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.44)
  - Decrease by 3 (no 1) showed smaller amplitude than Increase by 1 (no 1) (*d* = -0.50)
  - Increase by 1 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.45)
**P1 latency:** Significant main effect of condition (*p* = 0.011). Post-hoc tests revealed:
  - Decrease by 2 (no 1) showed greater latency than Increase by 1 (no 1) (*d* = 0.66)
  - Decrease by 2 (no 1) showed greater latency than Increase by 2 (no 1) (*d* = 0.71)
  - Decrease by 2 (no 1) showed greater latency than Increase by 3 (no 1) (*d* = 0.89)
**P3b latency:** Significant main effect of condition (*p* = 0.023). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed smaller latency than Decrease by 1 (no 1) (*d* = -0.83)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 1 (no 1) (*d* = -0.65)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 2 (no 1) (*d* = -0.75)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 3 (no 1) (*d* = -0.85)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -0.78)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 3 (no 1) (*d* = -1.02)
  - Decrease by 1 (no 1) showed greater amplitude than Increase by 1 (no 1) (*d* = 0.27)
  - Decrease by 2 (no 1) showed greater amplitude than Increase by 1 (no 1) (*d* = 0.35)
  - Decrease by 3 (no 1) showed greater amplitude than Increase by 1 (no 1) (*d* = 0.48)
  - Increase by 1 (no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -0.40)
  - Increase by 1 (no 1) showed smaller amplitude than Increase by 3 (no 1) (*d* = -0.53)

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
