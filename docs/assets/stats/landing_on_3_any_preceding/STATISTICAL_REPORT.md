# Statistical Analysis Report: tables

**Generated:** 2025-10-18 17:12:09

---

## 1. Analysis Overview

**Total Measurements:** 432
**Number of Subjects:** 24
**Number of Conditions:** 6

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -4.12 µV | 1.70 | 0.35 | [-8.47, -1.15] |
| 2 to 3 | 22 | -3.12 µV | 1.40 | 0.30 | [-5.71, -0.33] |
| 4 to 3 | 23 | -3.92 µV | 1.89 | 0.39 | [-8.15, -0.73] |
| 5 to 3 | 24 | -3.55 µV | 2.24 | 0.46 | [-8.41, -0.11] |
| 6 to 3 | 23 | -4.11 µV | 1.86 | 0.39 | [-8.15, -0.82] |
| Cardinality3 | 23 | -2.91 µV | 1.69 | 0.35 | [-7.14, -0.40] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 175.81 ms | 11.22 | 2.29 | [152.80, 202.59] |
| 2 to 3 | 22 | 174.69 ms | 10.26 | 2.19 | [154.17, 197.42] |
| 4 to 3 | 23 | 176.88 ms | 12.10 | 2.52 | [154.62, 210.97] |
| 5 to 3 | 24 | 176.23 ms | 12.08 | 2.46 | [149.94, 214.66] |
| 6 to 3 | 23 | 177.02 ms | 10.58 | 2.21 | [159.35, 206.73] |
| Cardinality3 | 23 | 175.36 ms | 14.31 | 2.98 | [147.80, 212.45] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 11 | 2.00 µV | 1.66 | 0.50 | [0.36, 6.39] |
| 2 to 3 | 12 | 1.98 µV | 1.40 | 0.40 | [-0.05, 5.17] |
| 4 to 3 | 11 | 1.83 µV | 1.23 | 0.37 | [0.19, 4.48] |
| 5 to 3 | 18 | 1.74 µV | 1.23 | 0.29 | [-0.03, 3.60] |
| 6 to 3 | 15 | 1.51 µV | 1.89 | 0.49 | [-0.15, 7.00] |
| Cardinality3 | 13 | 2.24 µV | 1.98 | 0.55 | [0.18, 7.43] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 11 | 106.35 ms | 3.83 | 1.16 | [102.45, 113.65] |
| 2 to 3 | 12 | 105.74 ms | 3.95 | 1.14 | [100.50, 114.79] |
| 4 to 3 | 11 | 104.42 ms | 4.10 | 1.24 | [96.63, 110.91] |
| 5 to 3 | 18 | 105.78 ms | 4.80 | 1.13 | [92.36, 113.61] |
| 6 to 3 | 15 | 104.94 ms | 5.52 | 1.42 | [96.74, 114.87] |
| Cardinality3 | 13 | 105.34 ms | 4.44 | 1.23 | [95.65, 112.11] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 3.98 µV | 3.31 | 0.74 | [0.00, 12.86] |
| 2 to 3 | 15 | 4.49 µV | 2.46 | 0.63 | [1.75, 9.70] |
| 4 to 3 | 19 | 3.55 µV | 2.52 | 0.58 | [0.53, 8.73] |
| 5 to 3 | 20 | 3.37 µV | 1.64 | 0.37 | [0.43, 6.88] |
| 6 to 3 | 19 | 4.02 µV | 2.64 | 0.61 | [1.26, 11.22] |
| Cardinality3 | 15 | 2.57 µV | 1.92 | 0.50 | [0.21, 6.65] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 463.26 ms | 19.16 | 4.28 | [408.75, 491.21] |
| 2 to 3 | 15 | 456.92 ms | 13.92 | 3.59 | [424.10, 478.08] |
| 4 to 3 | 19 | 459.60 ms | 22.52 | 5.17 | [408.21, 495.52] |
| 5 to 3 | 20 | 461.34 ms | 21.29 | 4.76 | [406.85, 496.11] |
| 6 to 3 | 19 | 459.96 ms | 23.00 | 5.28 | [404.92, 503.49] |
| Cardinality3 | 15 | 447.19 ms | 24.67 | 6.37 | [398.54, 477.57] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.47 | 0.29 | -1.61 | 0.108 | 0.715 | n.s. |
| 1 to 3 - 4 to 3 | 0.09 | 0.28 | 0.31 | 0.756 | 0.985 | n.s. |
| 1 to 3 - 5 to 3 | -0.13 | 0.28 | -0.47 | 0.637 | 0.985 | n.s. |
| 1 to 3 - 6 to 3 | 0.16 | 0.28 | 0.57 | 0.566 | 0.985 | n.s. |
| 1 to 3 - Cardinality3 | -0.44 | 0.29 | -1.51 | 0.131 | 0.755 | n.s. |
| 2 to 3 - 4 to 3 | 0.56 | 0.29 | 1.92 | 0.054 | 0.517 | n.s. |
| 2 to 3 - 5 to 3 | 0.34 | 0.29 | 1.19 | 0.234 | 0.909 | n.s. |
| 2 to 3 - 6 to 3 | 0.63 | 0.29 | 2.19 | 0.028 | 0.352 | n.s. |
| 2 to 3 - Cardinality3 | 0.03 | 0.29 | 0.10 | 0.918 | 0.985 | n.s. |
| 4 to 3 - 5 to 3 | -0.22 | 0.28 | -0.78 | 0.433 | 0.967 | n.s. |
| 4 to 3 - 6 to 3 | 0.07 | 0.28 | 0.26 | 0.794 | 0.985 | n.s. |
| 4 to 3 - Cardinality3 | -0.53 | 0.29 | -1.83 | 0.067 | 0.563 | n.s. |
| 5 to 3 - 6 to 3 | 0.29 | 0.28 | 1.05 | 0.294 | 0.922 | n.s. |
| 5 to 3 - Cardinality3 | -0.31 | 0.28 | -1.10 | 0.273 | 0.922 | n.s. |
| 6 to 3 - Cardinality3 | -0.60 | 0.29 | -2.09 | 0.037 | 0.406 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.37, *p* = 0.007, η²_G = 0.074
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -3.24 | 20 | = 0.043 | -0.69 [-1.16, -0.18] | medium | * |
| 1 to 3 vs 4 to 3 | -0.16 | 20 | = 0.934 | -0.04 [-0.55, 0.31] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.95 | 20 | = 0.481 | -0.26 [-0.66, 0.19] | small | n.s. |
| 1 to 3 vs 6 to 3 | 0.27 | 20 | = 0.911 | 0.07 [-0.48, 0.39] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | -3.10 | 20 | = 0.043 | -0.64 [-1.23, -0.25] | medium | * |
| 2 to 3 vs 4 to 3 | 2.40 | 20 | = 0.066 | 0.62 [0.04, 1.01] | medium | n.s. |
| 2 to 3 vs 5 to 3 | 1.29 | 20 | = 0.374 | 0.30 [-0.15, 0.76] | small | n.s. |
| 2 to 3 vs 6 to 3 | 2.77 | 20 | = 0.052 | 0.73 [0.08, 1.03] | medium | n.s. |
| 2 to 3 vs Cardinality3 | -0.00 | 20 | = 0.999 | -0.00 [-0.50, 0.39] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -1.19 | 20 | = 0.374 | -0.22 [-0.72, 0.16] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.46 | 20 | = 0.811 | 0.10 [-0.40, 0.49] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -2.70 | 20 | = 0.052 | -0.58 [-1.06, -0.10] | medium | n.s. |
| 5 to 3 vs 6 to 3 | 1.53 | 20 | = 0.302 | 0.31 [-0.23, 0.65] | small | n.s. |
| 5 to 3 vs Cardinality3 | -1.21 | 20 | = 0.374 | -0.29 [-0.75, 0.14] | small | n.s. |
| 6 to 3 vs Cardinality3 | -2.59 | 20 | = 0.053 | -0.69 [-1.06, -0.10] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1000.95, BIC = 1027.36
- **2 to 3 vs 1 to 3**: *β* = 1.12, *SE* = 2.014, *z* = 0.558, *p* = 0.577
- **4 to 3 vs 1 to 3**: *β* = 0.98, *SE* = 1.931, *z* = 0.507, *p* = 0.612
- **5 to 3 vs 1 to 3**: *β* = 0.66, *SE* = 1.925, *z* = 0.340, *p* = 0.734
- **6 to 3 vs 1 to 3**: *β* = 2.71, *SE* = 1.934, *z* = 1.402, *p* = 0.161
- **Cardinality3 vs 1 to 3**: *β* = 0.44, *SE* = 2.010, *z* = 0.217, *p* = 0.828
- **SNR**: *β* = 0.18, *SE* = 0.254, *z* = 0.706, *p* = 0.480

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -1.12 | 2.01 | -0.56 | 0.577 | 1.000 | n.s. |
| 1 to 3 - 4 to 3 | -0.98 | 1.93 | -0.51 | 0.612 | 1.000 | n.s. |
| 1 to 3 - 5 to 3 | -0.65 | 1.92 | -0.34 | 0.734 | 1.000 | n.s. |
| 1 to 3 - 6 to 3 | -2.71 | 1.93 | -1.40 | 0.161 | 0.928 | n.s. |
| 1 to 3 - Cardinality3 | -0.44 | 2.01 | -0.22 | 0.828 | 1.000 | n.s. |
| 2 to 3 - 4 to 3 | 0.15 | 2.00 | 0.07 | 0.942 | 1.000 | n.s. |
| 2 to 3 - 5 to 3 | 0.47 | 1.96 | 0.24 | 0.811 | 1.000 | n.s. |
| 2 to 3 - 6 to 3 | -1.59 | 1.98 | -0.80 | 0.423 | 0.998 | n.s. |
| 2 to 3 - Cardinality3 | 0.69 | 1.97 | 0.35 | 0.727 | 1.000 | n.s. |
| 4 to 3 - 5 to 3 | 0.32 | 1.92 | 0.17 | 0.866 | 1.000 | n.s. |
| 4 to 3 - 6 to 3 | -1.73 | 1.95 | -0.89 | 0.373 | 0.996 | n.s. |
| 4 to 3 - Cardinality3 | 0.54 | 1.98 | 0.27 | 0.785 | 1.000 | n.s. |
| 5 to 3 - 6 to 3 | -2.06 | 1.92 | -1.07 | 0.285 | 0.987 | n.s. |
| 5 to 3 - Cardinality3 | 0.22 | 1.94 | 0.11 | 0.910 | 1.000 | n.s. |
| 6 to 3 - Cardinality3 | 2.28 | 1.98 | 1.15 | 0.251 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.33, *p* = 0.894, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.829 (ε = 0.683)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.10 | 20 | = 0.991 | -0.01 [-0.48, 0.41] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.01 | 20 | = 0.991 | 0.00 [-0.51, 0.36] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 0.11 | 20 | = 0.991 | 0.02 [-0.47, 0.38] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.81 | 20 | = 0.991 | -0.16 [-0.68, 0.20] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 0.45 | 20 | = 0.991 | 0.09 [-0.40, 0.46] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 0.07 | 20 | = 0.991 | 0.02 [-0.44, 0.47] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | 0.16 | 20 | = 0.991 | 0.04 [-0.41, 0.48] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.78 | 20 | = 0.991 | -0.14 [-0.57, 0.32] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 0.54 | 20 | = 0.991 | 0.10 [-0.34, 0.55] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 0.11 | 20 | = 0.991 | 0.02 [-0.38, 0.49] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.94 | 20 | = 0.991 | -0.17 [-0.73, 0.17] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 0.38 | 20 | = 0.991 | 0.09 [-0.37, 0.52] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -1.19 | 20 | = 0.991 | -0.19 [-0.73, 0.15] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.36 | 20 | = 0.991 | 0.08 [-0.36, 0.51] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 1.45 | 20 | = 0.991 | 0.24 [-0.21, 0.69] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.07 | 0.33 | 0.20 | 0.843 | 0.940 | n.s. |
| 1 to 3 - 4 to 3 | 0.47 | 0.32 | 1.45 | 0.148 | 0.799 | n.s. |
| 1 to 3 - 5 to 3 | 0.55 | 0.29 | 1.94 | 0.052 | 0.472 | n.s. |
| 1 to 3 - 6 to 3 | 0.32 | 0.30 | 1.05 | 0.292 | 0.920 | n.s. |
| 1 to 3 - Cardinality3 | -0.27 | 0.31 | -0.87 | 0.382 | 0.928 | n.s. |
| 2 to 3 - 4 to 3 | 0.40 | 0.32 | 1.25 | 0.212 | 0.882 | n.s. |
| 2 to 3 - 5 to 3 | 0.49 | 0.28 | 1.74 | 0.082 | 0.609 | n.s. |
| 2 to 3 - 6 to 3 | 0.25 | 0.29 | 0.87 | 0.385 | 0.928 | n.s. |
| 2 to 3 - Cardinality3 | -0.33 | 0.30 | -1.10 | 0.271 | 0.920 | n.s. |
| 4 to 3 - 5 to 3 | 0.09 | 0.28 | 0.31 | 0.755 | 0.940 | n.s. |
| 4 to 3 - 6 to 3 | -0.15 | 0.30 | -0.51 | 0.607 | 0.939 | n.s. |
| 4 to 3 - Cardinality3 | -0.74 | 0.30 | -2.45 | 0.014 | 0.183 | n.s. |
| 5 to 3 - 6 to 3 | -0.24 | 0.26 | -0.93 | 0.355 | 0.928 | n.s. |
| 5 to 3 - Cardinality3 | -0.82 | 0.27 | -3.08 | 0.002 | 0.031 | * |
| 6 to 3 - Cardinality3 | -0.59 | 0.27 | -2.14 | 0.033 | 0.350 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.51, *p* = 0.760, η²_G = 0.140
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 1.83 | 2 | = 0.905 | 1.36 [-1.03, 1.48] | large | n.s. |
| 1 to 3 vs 4 to 3 | 0.45 | 2 | = 0.905 | 0.36 [-0.73, 1.44] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.74 | 2 | = 0.905 | 0.77 [-0.57, 0.87] | medium | n.s. |
| 1 to 3 vs 6 to 3 | 0.50 | 2 | = 0.905 | 0.14 [-0.24, 1.63] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 0.43 | 2 | = 0.905 | 0.11 [-1.15, 0.72] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -2.32 | 2 | = 0.905 | -1.68 [-1.42, 0.74] | large | n.s. |
| 2 to 3 vs 5 to 3 | -1.17 | 2 | = 0.905 | -1.01 [-0.53, 0.91] | large | n.s. |
| 2 to 3 vs 6 to 3 | -1.03 | 2 | = 0.905 | -0.81 [-0.75, 0.79] | large | n.s. |
| 2 to 3 vs Cardinality3 | -0.97 | 2 | = 0.905 | -0.74 [-1.24, 0.65] | medium | n.s. |
| 4 to 3 vs 5 to 3 | 1.17 | 2 | = 0.905 | 0.59 [-0.61, 0.82] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -0.13 | 2 | = 0.967 | -0.12 [-0.60, 0.94] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -0.16 | 2 | = 0.967 | -0.12 [-1.04, 0.65] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.41 | 2 | = 0.905 | -0.42 [-0.47, 0.74] | small | n.s. |
| 5 to 3 vs Cardinality3 | -0.41 | 2 | = 0.905 | -0.40 [-0.80, 0.55] | small | n.s. |
| 6 to 3 vs Cardinality3 | -0.05 | 2 | = 0.967 | -0.01 [-1.05, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.31 | 1.46 | 0.22 | 0.830 | 0.999 | n.s. |
| 1 to 3 - 4 to 3 | 1.96 | 1.44 | 1.36 | 0.173 | 0.943 | n.s. |
| 1 to 3 - 5 to 3 | 0.43 | 1.27 | 0.34 | 0.737 | 0.999 | n.s. |
| 1 to 3 - 6 to 3 | 0.81 | 1.33 | 0.61 | 0.543 | 0.996 | n.s. |
| 1 to 3 - Cardinality3 | 1.67 | 1.37 | 1.22 | 0.221 | 0.966 | n.s. |
| 2 to 3 - 4 to 3 | 1.64 | 1.43 | 1.15 | 0.252 | 0.969 | n.s. |
| 2 to 3 - 5 to 3 | 0.11 | 1.25 | 0.09 | 0.929 | 0.999 | n.s. |
| 2 to 3 - 6 to 3 | 0.50 | 1.28 | 0.39 | 0.699 | 0.999 | n.s. |
| 2 to 3 - Cardinality3 | 1.36 | 1.35 | 1.01 | 0.314 | 0.978 | n.s. |
| 4 to 3 - 5 to 3 | -1.53 | 1.23 | -1.24 | 0.215 | 0.966 | n.s. |
| 4 to 3 - 6 to 3 | -1.15 | 1.31 | -0.87 | 0.383 | 0.987 | n.s. |
| 4 to 3 - Cardinality3 | -0.28 | 1.34 | -0.21 | 0.832 | 0.999 | n.s. |
| 5 to 3 - 6 to 3 | 0.38 | 1.15 | 0.34 | 0.737 | 0.999 | n.s. |
| 5 to 3 - Cardinality3 | 1.25 | 1.19 | 1.05 | 0.294 | 0.978 | n.s. |
| 6 to 3 - Cardinality3 | 0.86 | 1.22 | 0.71 | 0.478 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.30, *p* = 0.339, η²_G = 0.214
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.86 | 2 | = 0.718 | -0.39 [-1.05, 1.46] | small | n.s. |
| 1 to 3 vs 4 to 3 | 1.07 | 2 | = 0.663 | 0.81 [-0.78, 1.36] | large | n.s. |
| 1 to 3 vs 5 to 3 | 4.89 | 2 | = 0.362 | 0.58 [-0.57, 0.87] | medium | n.s. |
| 1 to 3 vs 6 to 3 | -0.57 | 2 | = 0.720 | -0.31 [-0.73, 0.94] | small | n.s. |
| 1 to 3 vs Cardinality3 | 0.58 | 2 | = 0.720 | 0.19 [-0.88, 0.97] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 4.39 | 2 | = 0.362 | 2.92 [-0.13, 2.72] | large | n.s. |
| 2 to 3 vs 5 to 3 | 2.07 | 2 | = 0.651 | 1.07 [-0.82, 0.62] | large | n.s. |
| 2 to 3 vs 6 to 3 | -0.13 | 2 | = 0.938 | -0.09 [-0.46, 1.12] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 3.27 | 2 | = 0.411 | 0.93 [-0.71, 1.17] | large | n.s. |
| 4 to 3 vs 5 to 3 | 0.09 | 2 | = 0.938 | 0.07 [-1.00, 0.46] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -1.16 | 2 | = 0.663 | -0.91 [-0.87, 0.67] | large | n.s. |
| 4 to 3 vs Cardinality3 | -1.46 | 2 | = 0.663 | -1.06 [-0.91, 0.77] | large | n.s. |
| 5 to 3 vs 6 to 3 | -1.29 | 2 | = 0.663 | -0.76 [-0.79, 0.42] | medium | n.s. |
| 5 to 3 vs Cardinality3 | -1.37 | 2 | = 0.663 | -0.52 [-0.61, 0.73] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 0.70 | 2 | = 0.720 | 0.48 [-0.26, 1.26] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.13 | 0.40 | 0.32 | 0.750 | 0.997 | n.s. |
| 1 to 3 - 4 to 3 | 0.33 | 0.36 | 0.92 | 0.360 | 0.988 | n.s. |
| 1 to 3 - 5 to 3 | 0.48 | 0.36 | 1.31 | 0.189 | 0.935 | n.s. |
| 1 to 3 - 6 to 3 | -0.00 | 0.37 | -0.00 | 0.996 | 0.997 | n.s. |
| 1 to 3 - Cardinality3 | 0.60 | 0.41 | 1.48 | 0.138 | 0.888 | n.s. |
| 2 to 3 - 4 to 3 | 0.21 | 0.40 | 0.51 | 0.609 | 0.996 | n.s. |
| 2 to 3 - 5 to 3 | 0.35 | 0.40 | 0.89 | 0.375 | 0.988 | n.s. |
| 2 to 3 - 6 to 3 | -0.13 | 0.40 | -0.32 | 0.748 | 0.997 | n.s. |
| 2 to 3 - Cardinality3 | 0.48 | 0.45 | 1.06 | 0.288 | 0.976 | n.s. |
| 4 to 3 - 5 to 3 | 0.14 | 0.37 | 0.39 | 0.696 | 0.997 | n.s. |
| 4 to 3 - 6 to 3 | -0.34 | 0.37 | -0.90 | 0.366 | 0.988 | n.s. |
| 4 to 3 - Cardinality3 | 0.27 | 0.41 | 0.66 | 0.511 | 0.993 | n.s. |
| 5 to 3 - 6 to 3 | -0.48 | 0.37 | -1.31 | 0.189 | 0.935 | n.s. |
| 5 to 3 - Cardinality3 | 0.13 | 0.40 | 0.31 | 0.755 | 0.997 | n.s. |
| 6 to 3 - Cardinality3 | 0.61 | 0.41 | 1.49 | 0.136 | 0.888 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.459, η²_G = 0.042
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.39 | 9 | = 0.816 | 0.09 [-0.52, 0.64] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 1.31 | 9 | = 0.766 | 0.30 [-0.25, 0.73] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.63 | 9 | = 0.816 | 0.21 [-0.24, 0.74] | small | n.s. |
| 1 to 3 vs 6 to 3 | 0.24 | 9 | = 0.825 | 0.04 [-0.39, 0.57] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 1.21 | 9 | = 0.766 | 0.52 [-0.16, 1.00] | medium | n.s. |
| 2 to 3 vs 4 to 3 | 0.97 | 9 | = 0.766 | 0.27 [-0.22, 0.98] | small | n.s. |
| 2 to 3 vs 5 to 3 | 0.56 | 9 | = 0.816 | 0.15 [-0.13, 1.03] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.23 | 9 | = 0.825 | -0.06 [-0.59, 0.56] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 1.48 | 9 | = 0.766 | 0.56 [-0.28, 1.22] | medium | n.s. |
| 4 to 3 vs 5 to 3 | -0.41 | 9 | = 0.816 | -0.16 [-0.40, 0.60] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -1.15 | 9 | = 0.766 | -0.29 [-0.70, 0.30] | small | n.s. |
| 4 to 3 vs Cardinality3 | 0.73 | 9 | = 0.816 | 0.26 [-0.18, 1.03] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.53 | 9 | = 0.816 | -0.19 [-0.72, 0.26] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.97 | 9 | = 0.766 | 0.51 [-0.16, 0.99] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 1.31 | 9 | = 0.766 | 0.54 [-0.12, 1.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 6.95 | 6.02 | 1.15 | 0.249 | 0.943 | n.s. |
| 1 to 3 - 4 to 3 | 3.06 | 5.50 | 0.56 | 0.578 | 0.997 | n.s. |
| 1 to 3 - 5 to 3 | 2.04 | 5.49 | 0.37 | 0.711 | 0.997 | n.s. |
| 1 to 3 - 6 to 3 | 3.00 | 5.51 | 0.54 | 0.586 | 0.997 | n.s. |
| 1 to 3 - Cardinality3 | 16.16 | 6.14 | 2.63 | 0.008 | 0.120 | n.s. |
| 2 to 3 - 4 to 3 | -3.89 | 6.09 | -0.64 | 0.524 | 0.997 | n.s. |
| 2 to 3 - 5 to 3 | -4.91 | 5.97 | -0.82 | 0.411 | 0.991 | n.s. |
| 2 to 3 - 6 to 3 | -3.94 | 6.07 | -0.65 | 0.516 | 0.997 | n.s. |
| 2 to 3 - Cardinality3 | 9.21 | 6.75 | 1.36 | 0.172 | 0.875 | n.s. |
| 4 to 3 - 5 to 3 | -1.02 | 5.57 | -0.18 | 0.854 | 0.997 | n.s. |
| 4 to 3 - 6 to 3 | -0.06 | 5.60 | -0.01 | 0.992 | 0.997 | n.s. |
| 4 to 3 - Cardinality3 | 13.10 | 6.17 | 2.12 | 0.034 | 0.341 | n.s. |
| 5 to 3 - 6 to 3 | 0.97 | 5.51 | 0.18 | 0.861 | 0.997 | n.s. |
| 5 to 3 - Cardinality3 | 14.12 | 6.05 | 2.33 | 0.020 | 0.242 | n.s. |
| 6 to 3 - Cardinality3 | 13.15 | 6.12 | 2.15 | 0.032 | 0.341 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.40, *p* = 0.848, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.58 | 9 | = 0.971 | 0.29 [-0.44, 0.72] | small | n.s. |
| 1 to 3 vs 4 to 3 | 0.60 | 9 | = 0.971 | 0.21 [-0.39, 0.58] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.10 | 9 | = 0.971 | 0.04 [-0.39, 0.58] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.37 | 9 | = 0.971 | -0.16 [-0.39, 0.57] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 0.85 | 9 | = 0.971 | 0.24 [-0.02, 1.18] | small | n.s. |
| 2 to 3 vs 4 to 3 | -0.06 | 9 | = 0.971 | -0.02 [-0.66, 0.50] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | -1.01 | 9 | = 0.971 | -0.24 [-0.81, 0.32] | small | n.s. |
| 2 to 3 vs 6 to 3 | -1.82 | 9 | = 0.971 | -0.52 [-0.55, 0.60] | medium | n.s. |
| 2 to 3 vs Cardinality3 | -0.12 | 9 | = 0.971 | -0.05 [-0.75, 0.68] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -0.40 | 9 | = 0.971 | -0.17 [-0.53, 0.47] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.86 | 9 | = 0.971 | -0.37 [-0.46, 0.53] | small | n.s. |
| 4 to 3 vs Cardinality3 | -0.04 | 9 | = 0.971 | -0.01 [-0.30, 0.88] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.67 | 9 | = 0.971 | -0.21 [-0.48, 0.48] | small | n.s. |
| 5 to 3 vs Cardinality3 | 0.52 | 9 | = 0.971 | 0.19 [-0.08, 1.09] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 1.25 | 9 | = 0.971 | 0.46 [-0.02, 1.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.007). Post-hoc tests revealed:
  - 1 to 3 showed smaller amplitude than 2 to 3 (*d* = -0.69)
  - 1 to 3 showed smaller amplitude than Cardinality3 (*d* = -0.64)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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

- Python 3.12.4
- MNE-Python 1.9.0
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
