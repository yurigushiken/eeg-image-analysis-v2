# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:27:56

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
| 1 to 3 | 24 | 100.67 ms | 11.72 | 2.39 | [88.00, 116.00] |
| 2 to 3 | 24 | 100.50 ms | 10.96 | 2.24 | [88.00, 116.00] |
| 4 to 3 | 24 | 103.83 ms | 9.54 | 1.95 | [88.00, 116.00] |
| 5 to 3 | 24 | 103.00 ms | 9.96 | 2.03 | [88.00, 116.00] |
| 6 to 3 | 24 | 102.83 ms | 10.32 | 2.11 | [88.00, 116.00] |
| Cardinality3 | 24 | 104.50 ms | 11.99 | 2.45 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -0.14 µV | 2.40 | 0.49 | [-5.86, 3.53] |
| 2 to 3 | 24 | -1.44 µV | 2.03 | 0.42 | [-5.76, 2.45] |
| 4 to 3 | 24 | -0.84 µV | 2.13 | 0.43 | [-6.08, 3.45] |
| 5 to 3 | 24 | -2.47 µV | 2.03 | 0.41 | [-5.05, 1.51] |
| 6 to 3 | 24 | -1.76 µV | 1.75 | 0.36 | [-6.41, 1.40] |
| Cardinality3 | 24 | -1.43 µV | 2.62 | 0.54 | [-8.81, 1.87] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 168.83 ms | 22.44 | 4.58 | [140.00, 216.00] |
| 2 to 3 | 24 | 171.67 ms | 21.03 | 4.29 | [140.00, 208.00] |
| 4 to 3 | 24 | 178.00 ms | 19.95 | 4.07 | [148.00, 216.00] |
| 5 to 3 | 24 | 174.33 ms | 16.88 | 3.45 | [140.00, 208.00] |
| 6 to 3 | 24 | 176.17 ms | 17.15 | 3.50 | [152.00, 216.00] |
| Cardinality3 | 24 | 172.17 ms | 21.25 | 4.34 | [140.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.64 µV | 2.55 | 0.52 | [-12.65, -2.71] |
| 2 to 3 | 24 | -4.95 µV | 2.20 | 0.45 | [-10.61, -0.11] |
| 4 to 3 | 24 | -6.09 µV | 2.68 | 0.55 | [-11.27, 1.75] |
| 5 to 3 | 24 | -5.96 µV | 2.70 | 0.55 | [-12.11, -1.76] |
| 6 to 3 | 24 | -6.45 µV | 2.18 | 0.44 | [-10.34, -1.59] |
| Cardinality3 | 24 | -5.18 µV | 1.95 | 0.40 | [-10.83, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 104.00 ms | 9.21 | 1.88 | [92.00, 116.00] |
| 2 to 3 | 24 | 105.33 ms | 9.85 | 2.01 | [92.00, 116.00] |
| 4 to 3 | 24 | 102.50 ms | 9.42 | 1.92 | [92.00, 116.00] |
| 5 to 3 | 24 | 107.83 ms | 9.10 | 1.86 | [92.00, 116.00] |
| 6 to 3 | 24 | 106.00 ms | 9.58 | 1.96 | [92.00, 116.00] |
| Cardinality3 | 24 | 106.33 ms | 10.54 | 2.15 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 0.74 µV | 2.77 | 0.57 | [-6.53, 7.47] |
| 2 to 3 | 24 | 1.40 µV | 2.31 | 0.47 | [-4.20, 6.87] |
| 4 to 3 | 24 | 0.81 µV | 2.16 | 0.44 | [-2.73, 5.30] |
| 5 to 3 | 24 | 1.81 µV | 2.18 | 0.44 | [-3.22, 4.61] |
| 6 to 3 | 24 | 1.68 µV | 2.26 | 0.46 | [-3.06, 8.17] |
| Cardinality3 | 24 | 1.55 µV | 2.89 | 0.59 | [-3.19, 8.96] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 464.50 ms | 41.54 | 8.48 | [388.00, 528.00] |
| 2 to 3 | 24 | 465.83 ms | 53.01 | 10.82 | [388.00, 528.00] |
| 4 to 3 | 24 | 461.50 ms | 42.88 | 8.75 | [388.00, 528.00] |
| 5 to 3 | 24 | 463.00 ms | 33.33 | 6.80 | [400.00, 528.00] |
| 6 to 3 | 24 | 462.50 ms | 35.05 | 7.15 | [396.00, 524.00] |
| Cardinality3 | 24 | 440.67 ms | 43.70 | 8.92 | [388.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 4.99 µV | 3.98 | 0.81 | [-1.07, 15.57] |
| 2 to 3 | 24 | 4.55 µV | 4.12 | 0.84 | [-3.39, 13.70] |
| 4 to 3 | 24 | 4.80 µV | 3.49 | 0.71 | [-1.86, 11.65] |
| 5 to 3 | 24 | 4.66 µV | 3.26 | 0.66 | [-3.30, 10.28] |
| 6 to 3 | 24 | 5.17 µV | 4.22 | 0.86 | [-2.21, 14.26] |
| Cardinality3 | 24 | 3.34 µV | 3.27 | 0.67 | [-5.21, 9.60] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1102.20, BIC = 1128.93
- **2 to 3 vs 1 to 3**: *β* = -0.17, *SE* = 2.937, *z* = -0.058, *p* = 0.954
- **4 to 3 vs 1 to 3**: *β* = 3.16, *SE* = 2.944, *z* = 1.074, *p* = 0.283
- **5 to 3 vs 1 to 3**: *β* = 2.33, *SE* = 2.883, *z* = 0.809, *p* = 0.418
- **6 to 3 vs 1 to 3**: *β* = 2.16, *SE* = 2.925, *z* = 0.740, *p* = 0.460
- **Cardinality3 vs 1 to 3**: *β* = 3.83, *SE* = 2.939, *z* = 1.303, *p* = 0.193
- **SNR**: *β* = -0.00, *SE* = 0.661, *z* = -0.007, *p* = 0.995

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.17 | 2.94 | 0.06 | 0.954 | 0.999 | n.s. |
| 1 to 3 - 4 to 3 | -3.16 | 2.94 | -1.07 | 0.283 | 0.981 | n.s. |
| 1 to 3 - 5 to 3 | -2.33 | 2.88 | -0.81 | 0.418 | 0.996 | n.s. |
| 1 to 3 - 6 to 3 | -2.16 | 2.93 | -0.74 | 0.460 | 0.996 | n.s. |
| 1 to 3 - Cardinality3 | -3.83 | 2.94 | -1.30 | 0.193 | 0.950 | n.s. |
| 2 to 3 - 4 to 3 | -3.33 | 2.88 | -1.16 | 0.248 | 0.975 | n.s. |
| 2 to 3 - 5 to 3 | -2.50 | 2.93 | -0.86 | 0.392 | 0.996 | n.s. |
| 2 to 3 - 6 to 3 | -2.33 | 2.88 | -0.81 | 0.418 | 0.996 | n.s. |
| 2 to 3 - Cardinality3 | -4.00 | 2.88 | -1.39 | 0.165 | 0.933 | n.s. |
| 4 to 3 - 5 to 3 | 0.83 | 2.93 | 0.28 | 0.777 | 0.999 | n.s. |
| 4 to 3 - 6 to 3 | 1.00 | 2.88 | 0.35 | 0.729 | 0.999 | n.s. |
| 4 to 3 - Cardinality3 | -0.67 | 2.88 | -0.23 | 0.817 | 0.999 | n.s. |
| 5 to 3 - 6 to 3 | 0.17 | 2.91 | 0.06 | 0.954 | 0.999 | n.s. |
| 5 to 3 - Cardinality3 | -1.50 | 2.93 | -0.51 | 0.609 | 0.997 | n.s. |
| 6 to 3 - Cardinality3 | -1.67 | 2.88 | -0.58 | 0.563 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.683, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.06 | 23 | = 0.953 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | -1.03 | 23 | = 0.895 | -0.30 [-0.64, 0.22] | small | n.s. |
| 1 to 3 vs 5 to 3 | -0.72 | 23 | = 0.895 | -0.21 [-0.57, 0.28] | small | n.s. |
| 1 to 3 vs 6 to 3 | -0.77 | 23 | = 0.895 | -0.20 [-0.58, 0.27] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | -1.05 | 23 | = 0.895 | -0.32 [-0.64, 0.21] | small | n.s. |
| 2 to 3 vs 4 to 3 | -1.32 | 23 | = 0.895 | -0.32 [-0.70, 0.16] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.91 | 23 | = 0.895 | -0.24 [-0.61, 0.24] | small | n.s. |
| 2 to 3 vs 6 to 3 | -0.81 | 23 | = 0.895 | -0.22 [-0.59, 0.26] | small | n.s. |
| 2 to 3 vs Cardinality3 | -1.16 | 23 | = 0.895 | -0.35 [-0.66, 0.19] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.33 | 23 | = 0.930 | 0.09 [-0.36, 0.49] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.35 | 23 | = 0.930 | 0.10 [-0.35, 0.49] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -0.24 | 23 | = 0.941 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.06 | 23 | = 0.953 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -0.57 | 23 | = 0.907 | -0.14 [-0.54, 0.31] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | -0.52 | 23 | = 0.907 | -0.15 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 622.42, BIC = 649.15
- **2 to 3 vs 1 to 3**: *β* = -1.29, *SE* = 0.521, *z* = -2.472, *p* = 0.013
- **4 to 3 vs 1 to 3**: *β* = -0.68, *SE* = 0.522, *z* = -1.309, *p* = 0.191
- **5 to 3 vs 1 to 3**: *β* = -2.33, *SE* = 0.510, *z* = -4.562, *p* < .001
- **6 to 3 vs 1 to 3**: *β* = -1.61, *SE* = 0.518, *z* = -3.104, *p* = 0.002
- **Cardinality3 vs 1 to 3**: *β* = -1.27, *SE* = 0.521, *z* = -2.441, *p* = 0.015
- **SNR**: *β* = 0.02, *SE* = 0.123, *z* = 0.160, *p* = 0.873

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 1.29 | 0.52 | 2.47 | 0.013 | 0.150 | n.s. |
| 1 to 3 - 4 to 3 | 0.68 | 0.52 | 1.31 | 0.191 | 0.719 | n.s. |
| 1 to 3 - 5 to 3 | 2.33 | 0.51 | 4.56 | < .001 | < .001 | *** |
| 1 to 3 - 6 to 3 | 1.61 | 0.52 | 3.10 | 0.002 | 0.025 | * |
| 1 to 3 - Cardinality3 | 1.27 | 0.52 | 2.44 | 0.015 | 0.150 | n.s. |
| 2 to 3 - 4 to 3 | -0.60 | 0.51 | -1.18 | 0.236 | 0.740 | n.s. |
| 2 to 3 - 5 to 3 | 1.04 | 0.52 | 2.01 | 0.045 | 0.349 | n.s. |
| 2 to 3 - 6 to 3 | 0.32 | 0.51 | 0.63 | 0.528 | 0.881 | n.s. |
| 2 to 3 - Cardinality3 | -0.02 | 0.51 | -0.03 | 0.976 | 0.976 | n.s. |
| 4 to 3 - 5 to 3 | 1.64 | 0.52 | 3.16 | 0.002 | 0.022 | * |
| 4 to 3 - 6 to 3 | 0.93 | 0.51 | 1.81 | 0.070 | 0.439 | n.s. |
| 4 to 3 - Cardinality3 | 0.59 | 0.51 | 1.15 | 0.248 | 0.740 | n.s. |
| 5 to 3 - 6 to 3 | -0.72 | 0.52 | -1.39 | 0.164 | 0.716 | n.s. |
| 5 to 3 - Cardinality3 | -1.05 | 0.52 | -2.03 | 0.042 | 0.349 | n.s. |
| 6 to 3 - Cardinality3 | -0.34 | 0.51 | -0.66 | 0.509 | 0.881 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.65, *p* < .001, η²_G = 0.104
- Greenhouse-Geisser corrected: *p* = 0.003 (ε = 0.736)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 2.01 | 23 | = 0.129 | 0.59 [-0.03, 0.85] | medium | n.s. |
| 1 to 3 vs 4 to 3 | 1.53 | 23 | = 0.210 | 0.31 [-0.12, 0.74] | small | n.s. |
| 1 to 3 vs 5 to 3 | 3.94 | 23 | = 0.010 | 1.05 [0.32, 1.29] | large | ** |
| 1 to 3 vs 6 to 3 | 3.33 | 23 | = 0.018 | 0.77 [0.21, 1.15] | medium | * |
| 1 to 3 vs Cardinality3 | 2.27 | 23 | = 0.099 | 0.51 [0.02, 0.91] | medium | n.s. |
| 2 to 3 vs 4 to 3 | -0.92 | 23 | = 0.457 | -0.29 [-0.61, 0.24] | small | n.s. |
| 2 to 3 vs 5 to 3 | 1.95 | 23 | = 0.129 | 0.50 [-0.04, 0.84] | medium | n.s. |
| 2 to 3 vs 6 to 3 | 0.63 | 23 | = 0.575 | 0.17 [-0.30, 0.55] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | -0.02 | 23 | = 0.981 | -0.01 [-0.43, 0.42] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 3.07 | 23 | = 0.021 | 0.78 [0.16, 1.09] | medium | * |
| 4 to 3 vs 6 to 3 | 3.25 | 23 | = 0.018 | 0.47 [0.20, 1.13] | small | * |
| 4 to 3 vs Cardinality3 | 1.36 | 23 | = 0.253 | 0.25 [-0.15, 0.71] | small | n.s. |
| 5 to 3 vs 6 to 3 | -1.66 | 23 | = 0.183 | -0.37 [-0.77, 0.09] | small | n.s. |
| 5 to 3 vs Cardinality3 | -1.91 | 23 | = 0.129 | -0.44 [-0.83, 0.05] | small | n.s. |
| 6 to 3 vs Cardinality3 | -0.81 | 23 | = 0.492 | -0.15 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1232.33, BIC = 1259.06
- **2 to 3 vs 1 to 3**: *β* = 4.36, *SE* = 4.175, *z* = 1.045, *p* = 0.296
- **4 to 3 vs 1 to 3**: *β* = 9.83, *SE* = 4.057, *z* = 2.422, *p* = 0.015
- **5 to 3 vs 1 to 3**: *β* = 6.46, *SE* = 4.088, *z* = 1.581, *p* = 0.114
- **6 to 3 vs 1 to 3**: *β* = 8.00, *SE* = 4.058, *z* = 1.972, *p* = 0.049
- **Cardinality3 vs 1 to 3**: *β* = 5.10, *SE* = 4.223, *z* = 1.209, *p* = 0.227
- **SNR**: *β* = 0.74, *SE* = 0.527, *z* = 1.401, *p* = 0.161

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -4.36 | 4.17 | -1.04 | 0.296 | 0.958 | n.s. |
| 1 to 3 - 4 to 3 | -9.83 | 4.06 | -2.42 | 0.015 | 0.208 | n.s. |
| 1 to 3 - 5 to 3 | -6.46 | 4.09 | -1.58 | 0.114 | 0.792 | n.s. |
| 1 to 3 - 6 to 3 | -8.00 | 4.06 | -1.97 | 0.049 | 0.502 | n.s. |
| 1 to 3 - Cardinality3 | -5.10 | 4.22 | -1.21 | 0.227 | 0.941 | n.s. |
| 2 to 3 - 4 to 3 | -5.47 | 4.08 | -1.34 | 0.180 | 0.908 | n.s. |
| 2 to 3 - 5 to 3 | -2.10 | 4.05 | -0.52 | 0.604 | 0.990 | n.s. |
| 2 to 3 - 6 to 3 | -3.64 | 4.08 | -0.89 | 0.372 | 0.976 | n.s. |
| 2 to 3 - Cardinality3 | -0.74 | 4.03 | -0.18 | 0.854 | 0.990 | n.s. |
| 4 to 3 - 5 to 3 | 3.36 | 4.04 | 0.83 | 0.404 | 0.976 | n.s. |
| 4 to 3 - 6 to 3 | 1.83 | 4.03 | 0.45 | 0.651 | 0.990 | n.s. |
| 4 to 3 - Cardinality3 | 4.72 | 4.11 | 1.15 | 0.250 | 0.944 | n.s. |
| 5 to 3 - 6 to 3 | -1.54 | 4.04 | -0.38 | 0.703 | 0.990 | n.s. |
| 5 to 3 - Cardinality3 | 1.36 | 4.07 | 0.33 | 0.739 | 0.990 | n.s. |
| 6 to 3 - Cardinality3 | 2.90 | 4.11 | 0.71 | 0.480 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.26, *p* = 0.285, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.73 | 23 | = 0.655 | -0.13 [-0.57, 0.28] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | -1.87 | 23 | = 0.559 | -0.43 [-0.82, 0.06] | small | n.s. |
| 1 to 3 vs 5 to 3 | -1.40 | 23 | = 0.576 | -0.28 [-0.72, 0.15] | small | n.s. |
| 1 to 3 vs 6 to 3 | -1.91 | 23 | = 0.559 | -0.37 [-0.83, 0.05] | small | n.s. |
| 1 to 3 vs Cardinality3 | -0.88 | 23 | = 0.655 | -0.15 [-0.61, 0.25] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -1.27 | 23 | = 0.576 | -0.31 [-0.69, 0.17] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.65 | 23 | = 0.655 | -0.14 [-0.56, 0.29] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.99 | 23 | = 0.655 | -0.23 [-0.63, 0.22] | small | n.s. |
| 2 to 3 vs Cardinality3 | -0.10 | 23 | = 0.924 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 0.77 | 23 | = 0.655 | 0.20 [-0.27, 0.58] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.51 | 23 | = 0.655 | 0.10 [-0.32, 0.53] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.36 | 23 | = 0.576 | 0.28 [-0.15, 0.71] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.58 | 23 | = 0.655 | -0.11 [-0.54, 0.31] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.57 | 23 | = 0.655 | 0.11 [-0.31, 0.54] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 1.23 | 23 | = 0.576 | 0.21 [-0.18, 0.68] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 598.81, BIC = 625.54
- **2 to 3 vs 1 to 3**: *β* = 0.81, *SE* = 0.489, *z* = 1.646, *p* = 0.100
- **4 to 3 vs 1 to 3**: *β* = 0.17, *SE* = 0.476, *z* = 0.361, *p* = 0.718
- **5 to 3 vs 1 to 3**: *β* = 0.12, *SE* = 0.480, *z* = 0.261, *p* = 0.794
- **6 to 3 vs 1 to 3**: *β* = -0.19, *SE* = 0.476, *z* = -0.399, *p* = 0.690
- **Cardinality3 vs 1 to 3**: *β* = 0.44, *SE* = 0.494, *z* = 0.882, *p* = 0.378
- **SNR**: *β* = -0.43, *SE* = 0.059, *z* = -7.220, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.81 | 0.49 | -1.65 | 0.100 | 0.770 | n.s. |
| 1 to 3 - 4 to 3 | -0.17 | 0.48 | -0.36 | 0.718 | 0.994 | n.s. |
| 1 to 3 - 5 to 3 | -0.13 | 0.48 | -0.26 | 0.794 | 0.994 | n.s. |
| 1 to 3 - 6 to 3 | 0.19 | 0.48 | 0.40 | 0.690 | 0.994 | n.s. |
| 1 to 3 - Cardinality3 | -0.44 | 0.49 | -0.88 | 0.378 | 0.991 | n.s. |
| 2 to 3 - 4 to 3 | 0.63 | 0.48 | 1.32 | 0.186 | 0.915 | n.s. |
| 2 to 3 - 5 to 3 | 0.68 | 0.48 | 1.43 | 0.153 | 0.884 | n.s. |
| 2 to 3 - 6 to 3 | 1.00 | 0.48 | 2.08 | 0.038 | 0.437 | n.s. |
| 2 to 3 - Cardinality3 | 0.37 | 0.47 | 0.78 | 0.436 | 0.994 | n.s. |
| 4 to 3 - 5 to 3 | 0.05 | 0.47 | 0.10 | 0.922 | 0.994 | n.s. |
| 4 to 3 - 6 to 3 | 0.36 | 0.47 | 0.76 | 0.445 | 0.994 | n.s. |
| 4 to 3 - Cardinality3 | -0.26 | 0.48 | -0.55 | 0.583 | 0.994 | n.s. |
| 5 to 3 - 6 to 3 | 0.31 | 0.47 | 0.66 | 0.506 | 0.994 | n.s. |
| 5 to 3 - Cardinality3 | -0.31 | 0.48 | -0.65 | 0.515 | 0.994 | n.s. |
| 6 to 3 - Cardinality3 | -0.63 | 0.48 | -1.30 | 0.194 | 0.915 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.99, *p* = 0.014, η²_G = 0.065
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -3.57 | 23 | = 0.012 | -0.71 [-1.20, -0.25] | medium | * |
| 1 to 3 vs 4 to 3 | -0.99 | 23 | = 0.505 | -0.21 [-0.63, 0.22] | small | n.s. |
| 1 to 3 vs 5 to 3 | -0.98 | 23 | = 0.505 | -0.26 [-0.63, 0.23] | small | n.s. |
| 1 to 3 vs 6 to 3 | -0.37 | 23 | = 0.764 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | -3.98 | 23 | = 0.009 | -0.64 [-1.30, -0.33] | medium | ** |
| 2 to 3 vs 4 to 3 | 1.71 | 23 | = 0.250 | 0.46 [-0.09, 0.78] | small | n.s. |
| 2 to 3 vs 5 to 3 | 1.82 | 23 | = 0.247 | 0.41 [-0.07, 0.81] | small | n.s. |
| 2 to 3 vs 6 to 3 | 2.85 | 23 | = 0.045 | 0.68 [0.13, 1.04] | medium | * |
| 2 to 3 vs Cardinality3 | 0.52 | 23 | = 0.704 | 0.11 [-0.32, 0.53] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -0.20 | 23 | = 0.843 | -0.05 [-0.46, 0.38] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.59 | 23 | = 0.698 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -1.63 | 23 | = 0.251 | -0.39 [-0.77, 0.10] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.90 | 23 | = 0.512 | 0.20 [-0.24, 0.61] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -1.34 | 23 | = 0.365 | -0.33 [-0.70, 0.16] | small | n.s. |
| 6 to 3 vs Cardinality3 | -2.51 | 23 | = 0.074 | -0.61 [-0.96, -0.06] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1046.38, BIC = 1073.11
- **2 to 3 vs 1 to 3**: *β* = 0.70, *SE* = 2.240, *z* = 0.314, *p* = 0.754
- **4 to 3 vs 1 to 3**: *β* = -1.71, *SE* = 2.221, *z* = -0.770, *p* = 0.441
- **5 to 3 vs 1 to 3**: *β* = 3.73, *SE* = 2.219, *z* = 1.683, *p* = 0.092
- **6 to 3 vs 1 to 3**: *β* = 1.61, *SE* = 2.227, *z* = 0.722, *p* = 0.470
- **Cardinality3 vs 1 to 3**: *β* = 1.85, *SE* = 2.231, *z* = 0.830, *p* = 0.407
- **SNR**: *β* = -0.91, *SE* = 0.443, *z* = -2.052, *p* = 0.040

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.70 | 2.24 | -0.31 | 0.754 | 0.983 | n.s. |
| 1 to 3 - 4 to 3 | 1.71 | 2.22 | 0.77 | 0.441 | 0.983 | n.s. |
| 1 to 3 - 5 to 3 | -3.73 | 2.22 | -1.68 | 0.092 | 0.743 | n.s. |
| 1 to 3 - 6 to 3 | -1.61 | 2.23 | -0.72 | 0.470 | 0.983 | n.s. |
| 1 to 3 - Cardinality3 | -1.85 | 2.23 | -0.83 | 0.407 | 0.983 | n.s. |
| 2 to 3 - 4 to 3 | 2.41 | 2.23 | 1.08 | 0.279 | 0.962 | n.s. |
| 2 to 3 - 5 to 3 | -3.03 | 2.23 | -1.36 | 0.175 | 0.879 | n.s. |
| 2 to 3 - 6 to 3 | -0.90 | 2.22 | -0.41 | 0.684 | 0.983 | n.s. |
| 2 to 3 - Cardinality3 | -1.15 | 2.22 | -0.52 | 0.605 | 0.983 | n.s. |
| 4 to 3 - 5 to 3 | -5.44 | 2.22 | -2.45 | 0.014 | 0.193 | n.s. |
| 4 to 3 - 6 to 3 | -3.32 | 2.22 | -1.49 | 0.135 | 0.825 | n.s. |
| 4 to 3 - Cardinality3 | -3.56 | 2.22 | -1.60 | 0.109 | 0.777 | n.s. |
| 5 to 3 - 6 to 3 | 2.13 | 2.22 | 0.96 | 0.339 | 0.976 | n.s. |
| 5 to 3 - Cardinality3 | 1.88 | 2.23 | 0.85 | 0.398 | 0.983 | n.s. |
| 6 to 3 - Cardinality3 | -0.24 | 2.22 | -0.11 | 0.912 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.32, *p* = 0.262, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.58 | 23 | = 0.713 | -0.14 [-0.54, 0.31] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.58 | 23 | = 0.713 | 0.16 [-0.30, 0.54] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -1.84 | 23 | = 0.409 | -0.42 [-0.81, 0.06] | small | n.s. |
| 1 to 3 vs 6 to 3 | -1.15 | 23 | = 0.615 | -0.21 [-0.66, 0.19] | small | n.s. |
| 1 to 3 vs Cardinality3 | -0.93 | 23 | = 0.615 | -0.24 [-0.62, 0.24] | small | n.s. |
| 2 to 3 vs 4 to 3 | 1.07 | 23 | = 0.615 | 0.29 [-0.21, 0.65] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.95 | 23 | = 0.615 | -0.26 [-0.62, 0.23] | small | n.s. |
| 2 to 3 vs 6 to 3 | -0.29 | 23 | = 0.833 | -0.07 [-0.48, 0.36] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | -0.33 | 23 | = 0.833 | -0.10 [-0.49, 0.35] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -2.55 | 23 | = 0.271 | -0.58 [-0.97, -0.07] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -1.50 | 23 | = 0.555 | -0.37 [-0.74, 0.13] | small | n.s. |
| 4 to 3 vs Cardinality3 | -1.82 | 23 | = 0.409 | -0.38 [-0.81, 0.06] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.92 | 23 | = 0.615 | 0.20 [-0.24, 0.61] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.83 | 23 | = 0.625 | 0.15 [-0.26, 0.59] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | -0.16 | 23 | = 0.873 | -0.03 [-0.46, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 647.94, BIC = 674.67
- **2 to 3 vs 1 to 3**: *β* = 0.75, *SE* = 0.557, *z* = 1.352, *p* = 0.177
- **4 to 3 vs 1 to 3**: *β* = 0.10, *SE* = 0.553, *z* = 0.185, *p* = 0.853
- **5 to 3 vs 1 to 3**: *β* = 1.08, *SE* = 0.552, *z* = 1.956, *p* = 0.050
- **6 to 3 vs 1 to 3**: *β* = 1.00, *SE* = 0.554, *z* = 1.800, *p* = 0.072
- **Cardinality3 vs 1 to 3**: *β* = 0.88, *SE* = 0.555, *z* = 1.589, *p* = 0.112
- **SNR**: *β* = 0.14, *SE* = 0.111, *z* = 1.251, *p* = 0.211

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.75 | 0.56 | -1.35 | 0.177 | 0.826 | n.s. |
| 1 to 3 - 4 to 3 | -0.10 | 0.55 | -0.18 | 0.853 | 0.999 | n.s. |
| 1 to 3 - 5 to 3 | -1.08 | 0.55 | -1.96 | 0.050 | 0.540 | n.s. |
| 1 to 3 - 6 to 3 | -1.00 | 0.55 | -1.80 | 0.072 | 0.648 | n.s. |
| 1 to 3 - Cardinality3 | -0.88 | 0.56 | -1.59 | 0.112 | 0.736 | n.s. |
| 2 to 3 - 4 to 3 | 0.65 | 0.55 | 1.17 | 0.240 | 0.889 | n.s. |
| 2 to 3 - 5 to 3 | -0.33 | 0.56 | -0.59 | 0.557 | 0.997 | n.s. |
| 2 to 3 - 6 to 3 | -0.24 | 0.55 | -0.44 | 0.659 | 0.998 | n.s. |
| 2 to 3 - Cardinality3 | -0.13 | 0.55 | -0.23 | 0.815 | 0.999 | n.s. |
| 4 to 3 - 5 to 3 | -0.98 | 0.55 | -1.77 | 0.077 | 0.648 | n.s. |
| 4 to 3 - 6 to 3 | -0.90 | 0.55 | -1.62 | 0.105 | 0.736 | n.s. |
| 4 to 3 - Cardinality3 | -0.78 | 0.55 | -1.41 | 0.158 | 0.822 | n.s. |
| 5 to 3 - 6 to 3 | 0.08 | 0.55 | 0.15 | 0.881 | 0.999 | n.s. |
| 5 to 3 - Cardinality3 | 0.20 | 0.55 | 0.36 | 0.721 | 0.998 | n.s. |
| 6 to 3 - Cardinality3 | 0.12 | 0.55 | 0.21 | 0.835 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.27, *p* = 0.281, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.92 | 23 | = 0.701 | -0.26 [-0.61, 0.24] | small | n.s. |
| 1 to 3 vs 4 to 3 | -0.12 | 23 | = 0.905 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -2.38 | 23 | = 0.360 | -0.43 [-0.93, -0.04] | small | n.s. |
| 1 to 3 vs 6 to 3 | -1.74 | 23 | = 0.360 | -0.37 [-0.79, 0.08] | small | n.s. |
| 1 to 3 vs Cardinality3 | -1.27 | 23 | = 0.542 | -0.29 [-0.69, 0.17] | small | n.s. |
| 2 to 3 vs 4 to 3 | 0.91 | 23 | = 0.701 | 0.26 [-0.24, 0.61] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.73 | 23 | = 0.791 | -0.18 [-0.57, 0.28] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.54 | 23 | = 0.866 | -0.12 [-0.53, 0.31] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | -0.25 | 23 | = 0.866 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -1.80 | 23 | = 0.360 | -0.46 [-0.80, 0.07] | small | n.s. |
| 4 to 3 vs 6 to 3 | -1.90 | 23 | = 0.360 | -0.39 [-0.83, 0.05] | small | n.s. |
| 4 to 3 vs Cardinality3 | -1.38 | 23 | = 0.539 | -0.29 [-0.71, 0.15] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.26 | 23 | = 0.866 | 0.06 [-0.37, 0.48] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.39 | 23 | = 0.866 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 0.28 | 23 | = 0.866 | 0.05 [-0.37, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1488.66, BIC = 1515.39
- **2 to 3 vs 1 to 3**: *β* = 1.11, *SE* = 10.859, *z* = 0.102, *p* = 0.919
- **4 to 3 vs 1 to 3**: *β* = -3.97, *SE* = 10.877, *z* = -0.365, *p* = 0.715
- **5 to 3 vs 1 to 3**: *β* = -1.40, *SE* = 10.858, *z* = -0.129, *p* = 0.898
- **6 to 3 vs 1 to 3**: *β* = -2.35, *SE* = 10.860, *z* = -0.217, *p* = 0.828
- **Cardinality3 vs 1 to 3**: *β* = -26.46, *SE* = 10.994, *z* = -2.407, *p* = 0.016
- **SNR**: *β* = -1.74, *SE* = 1.140, *z* = -1.522, *p* = 0.128

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -1.11 | 10.86 | -0.10 | 0.919 | 1.000 | n.s. |
| 1 to 3 - 4 to 3 | 3.97 | 10.88 | 0.37 | 0.715 | 1.000 | n.s. |
| 1 to 3 - 5 to 3 | 1.40 | 10.86 | 0.13 | 0.898 | 1.000 | n.s. |
| 1 to 3 - 6 to 3 | 2.36 | 10.86 | 0.22 | 0.828 | 1.000 | n.s. |
| 1 to 3 - Cardinality3 | 26.46 | 10.99 | 2.41 | 0.016 | 0.203 | n.s. |
| 2 to 3 - 4 to 3 | 5.08 | 10.87 | 0.47 | 0.640 | 1.000 | n.s. |
| 2 to 3 - 5 to 3 | 2.51 | 10.86 | 0.23 | 0.817 | 1.000 | n.s. |
| 2 to 3 - 6 to 3 | 3.46 | 10.86 | 0.32 | 0.750 | 1.000 | n.s. |
| 2 to 3 - Cardinality3 | 27.57 | 10.97 | 2.51 | 0.012 | 0.165 | n.s. |
| 4 to 3 - 5 to 3 | -2.58 | 10.88 | -0.24 | 0.813 | 1.000 | n.s. |
| 4 to 3 - 6 to 3 | -1.62 | 10.87 | -0.15 | 0.882 | 1.000 | n.s. |
| 4 to 3 - Cardinality3 | 22.49 | 10.91 | 2.06 | 0.039 | 0.357 | n.s. |
| 5 to 3 - 6 to 3 | 0.96 | 10.86 | 0.09 | 0.930 | 1.000 | n.s. |
| 5 to 3 - Cardinality3 | 25.06 | 11.00 | 2.28 | 0.023 | 0.259 | n.s. |
| 6 to 3 - Cardinality3 | 24.10 | 10.96 | 2.20 | 0.028 | 0.288 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.43, *p* = 0.219, η²_G = 0.042
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.12 | 23 | = 0.953 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.22 | 23 | = 0.953 | 0.07 [-0.38, 0.47] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 0.14 | 23 | = 0.953 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | 0.17 | 23 | = 0.953 | 0.05 [-0.39, 0.46] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 1.89 | 23 | = 0.270 | 0.56 [-0.05, 0.82] | medium | n.s. |
| 2 to 3 vs 4 to 3 | 0.39 | 23 | = 0.953 | 0.09 [-0.34, 0.50] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | 0.23 | 23 | = 0.953 | 0.06 [-0.38, 0.47] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | 0.28 | 23 | = 0.953 | 0.07 [-0.36, 0.48] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 1.87 | 23 | = 0.270 | 0.52 [-0.05, 0.82] | medium | n.s. |
| 4 to 3 vs 5 to 3 | -0.14 | 23 | = 0.953 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.11 | 23 | = 0.953 | -0.03 [-0.44, 0.40] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.77 | 23 | = 0.270 | 0.48 [-0.07, 0.80] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.06 | 23 | = 0.953 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 2.54 | 23 | = 0.145 | 0.57 [0.07, 0.97] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 2.52 | 23 | = 0.145 | 0.55 [0.06, 0.96] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 687.88, BIC = 714.61
- **2 to 3 vs 1 to 3**: *β* = -0.40, *SE* = 0.580, *z* = -0.687, *p* = 0.492
- **4 to 3 vs 1 to 3**: *β* = -0.02, *SE* = 0.581, *z* = -0.038, *p* = 0.970
- **5 to 3 vs 1 to 3**: *β* = -0.35, *SE* = 0.580, *z* = -0.597, *p* = 0.551
- **6 to 3 vs 1 to 3**: *β* = 0.24, *SE* = 0.580, *z* = 0.416, *p* = 0.677
- **Cardinality3 vs 1 to 3**: *β* = -1.20, *SE* = 0.589, *z* = -2.044, *p* = 0.041
- **SNR**: *β* = 0.29, *SE* = 0.068, *z* = 4.316, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.40 | 0.58 | 0.69 | 0.492 | 0.996 | n.s. |
| 1 to 3 - 4 to 3 | 0.02 | 0.58 | 0.04 | 0.970 | 0.996 | n.s. |
| 1 to 3 - 5 to 3 | 0.35 | 0.58 | 0.60 | 0.551 | 0.996 | n.s. |
| 1 to 3 - 6 to 3 | -0.24 | 0.58 | -0.42 | 0.677 | 0.996 | n.s. |
| 1 to 3 - Cardinality3 | 1.20 | 0.59 | 2.04 | 0.041 | 0.443 | n.s. |
| 2 to 3 - 4 to 3 | -0.38 | 0.58 | -0.65 | 0.516 | 0.996 | n.s. |
| 2 to 3 - 5 to 3 | -0.05 | 0.58 | -0.09 | 0.928 | 0.996 | n.s. |
| 2 to 3 - 6 to 3 | -0.64 | 0.58 | -1.10 | 0.270 | 0.957 | n.s. |
| 2 to 3 - Cardinality3 | 0.80 | 0.59 | 1.37 | 0.171 | 0.872 | n.s. |
| 4 to 3 - 5 to 3 | 0.32 | 0.58 | 0.56 | 0.577 | 0.996 | n.s. |
| 4 to 3 - 6 to 3 | -0.26 | 0.58 | -0.45 | 0.650 | 0.996 | n.s. |
| 4 to 3 - Cardinality3 | 1.18 | 0.58 | 2.03 | 0.043 | 0.443 | n.s. |
| 5 to 3 - 6 to 3 | -0.59 | 0.58 | -1.01 | 0.311 | 0.965 | n.s. |
| 5 to 3 - Cardinality3 | 0.86 | 0.59 | 1.45 | 0.146 | 0.849 | n.s. |
| 6 to 3 - Cardinality3 | 1.44 | 0.59 | 2.46 | 0.014 | 0.188 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.067, η²_G = 0.025
- Greenhouse-Geisser corrected: *p* = 0.098 (ε = 0.662)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.75 | 23 | = 0.827 | 0.11 [-0.27, 0.58] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.37 | 23 | = 0.827 | 0.05 [-0.35, 0.50] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 0.48 | 23 | = 0.827 | 0.09 [-0.32, 0.52] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.40 | 23 | = 0.827 | -0.04 [-0.50, 0.34] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 1.95 | 23 | = 0.239 | 0.45 [-0.04, 0.84] | small | n.s. |
| 2 to 3 vs 4 to 3 | -0.44 | 23 | = 0.827 | -0.07 [-0.51, 0.33] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | -0.21 | 23 | = 0.837 | -0.03 [-0.46, 0.38] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -1.04 | 23 | = 0.777 | -0.15 [-0.64, 0.22] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 1.49 | 23 | = 0.453 | 0.32 [-0.13, 0.74] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.29 | 23 | = 0.827 | 0.04 [-0.36, 0.48] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.64 | 23 | = 0.827 | -0.09 [-0.56, 0.29] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 2.02 | 23 | = 0.239 | 0.43 [-0.03, 0.85] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.79 | 23 | = 0.827 | -0.14 [-0.59, 0.26] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 2.35 | 23 | = 0.207 | 0.40 [0.03, 0.93] | small | n.s. |
| 6 to 3 vs Cardinality3 | 2.53 | 23 | = 0.207 | 0.48 [0.07, 0.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 3 showed greater amplitude than 5 to 3 (*d* = 1.05)
  - 1 to 3 showed greater amplitude than 6 to 3 (*d* = 0.77)
  - 4 to 3 showed greater amplitude than 5 to 3 (*d* = 0.78)
  - 4 to 3 showed greater amplitude than 6 to 3 (*d* = 0.47)
**N1 amplitude:** Significant main effect of condition (*p* = 0.014). Post-hoc tests revealed:
  - 1 to 3 showed smaller amplitude than 2 to 3 (*d* = -0.71)
  - 1 to 3 showed smaller amplitude than Cardinality3 (*d* = -0.64)
  - 2 to 3 showed greater amplitude than 6 to 3 (*d* = 0.68)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.067)

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
