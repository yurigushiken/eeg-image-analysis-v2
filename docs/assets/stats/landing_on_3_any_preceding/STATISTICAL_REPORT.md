# Statistical Analysis Report: tables

**Generated:** 2025-10-23 18:58:49

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

- Model converged successfully
- AIC = 463.44, BIC = 489.85
- **2 to 3 vs 1 to 3**: *β* = 0.39, *SE* = 0.322, *z* = 1.199, *p* = 0.231
- **4 to 3 vs 1 to 3**: *β* = -0.11, *SE* = 0.310, *z* = -0.342, *p* = 0.733
- **5 to 3 vs 1 to 3**: *β* = 0.09, *SE* = 0.309, *z* = 0.294, *p* = 0.769
- **6 to 3 vs 1 to 3**: *β* = -0.21, *SE* = 0.310, *z* = -0.675, *p* = 0.500
- **Cardinality3 vs 1 to 3**: *β* = 0.37, *SE* = 0.322, *z* = 1.142, *p* = 0.253
- **SNR**: *β* = -0.37, *SE* = 0.040, *z* = -9.297, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.39 | 0.32 | -1.20 | 0.231 | 0.944 | n.s. |
| 1 to 3 - 4 to 3 | 0.11 | 0.31 | 0.34 | 0.733 | 0.995 | n.s. |
| 1 to 3 - 5 to 3 | -0.09 | 0.31 | -0.29 | 0.769 | 0.995 | n.s. |
| 1 to 3 - 6 to 3 | 0.21 | 0.31 | 0.68 | 0.500 | 0.984 | n.s. |
| 1 to 3 - Cardinality3 | -0.37 | 0.32 | -1.14 | 0.253 | 0.946 | n.s. |
| 2 to 3 - 4 to 3 | 0.49 | 0.32 | 1.54 | 0.124 | 0.821 | n.s. |
| 2 to 3 - 5 to 3 | 0.30 | 0.31 | 0.94 | 0.346 | 0.973 | n.s. |
| 2 to 3 - 6 to 3 | 0.60 | 0.32 | 1.87 | 0.061 | 0.612 | n.s. |
| 2 to 3 - Cardinality3 | 0.02 | 0.32 | 0.06 | 0.952 | 0.995 | n.s. |
| 4 to 3 - 5 to 3 | -0.20 | 0.31 | -0.64 | 0.524 | 0.984 | n.s. |
| 4 to 3 - 6 to 3 | 0.10 | 0.31 | 0.33 | 0.740 | 0.995 | n.s. |
| 4 to 3 - Cardinality3 | -0.47 | 0.32 | -1.49 | 0.136 | 0.828 | n.s. |
| 5 to 3 - 6 to 3 | 0.30 | 0.31 | 0.97 | 0.331 | 0.973 | n.s. |
| 5 to 3 - Cardinality3 | -0.28 | 0.31 | -0.89 | 0.373 | 0.973 | n.s. |
| 6 to 3 - Cardinality3 | -0.58 | 0.32 | -1.82 | 0.069 | 0.633 | n.s. |

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

- Model converged successfully
- AIC = 232.82, BIC = 254.26
- **2 to 3 vs 1 to 3**: *β* = -0.02, *SE* = 0.359, *z* = -0.056, *p* = 0.955
- **4 to 3 vs 1 to 3**: *β* = -0.45, *SE* = 0.360, *z* = -1.254, *p* = 0.210
- **5 to 3 vs 1 to 3**: *β* = -0.54, *SE* = 0.320, *z* = -1.681, *p* = 0.093
- **6 to 3 vs 1 to 3**: *β* = -0.27, *SE* = 0.335, *z* = -0.792, *p* = 0.428
- **Cardinality3 vs 1 to 3**: *β* = 0.28, *SE* = 0.344, *z* = 0.808, *p* = 0.419
- **SNR**: *β* = 0.66, *SE* = 0.066, *z* = 10.002, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.02 | 0.36 | 0.06 | 0.955 | 0.970 | n.s. |
| 1 to 3 - 4 to 3 | 0.45 | 0.36 | 1.25 | 0.210 | 0.905 | n.s. |
| 1 to 3 - 5 to 3 | 0.54 | 0.32 | 1.68 | 0.093 | 0.689 | n.s. |
| 1 to 3 - 6 to 3 | 0.27 | 0.33 | 0.79 | 0.428 | 0.970 | n.s. |
| 1 to 3 - Cardinality3 | -0.28 | 0.34 | -0.81 | 0.419 | 0.970 | n.s. |
| 2 to 3 - 4 to 3 | 0.43 | 0.36 | 1.21 | 0.226 | 0.905 | n.s. |
| 2 to 3 - 5 to 3 | 0.52 | 0.31 | 1.64 | 0.100 | 0.689 | n.s. |
| 2 to 3 - 6 to 3 | 0.25 | 0.32 | 0.76 | 0.449 | 0.970 | n.s. |
| 2 to 3 - Cardinality3 | -0.30 | 0.34 | -0.88 | 0.378 | 0.970 | n.s. |
| 4 to 3 - 5 to 3 | 0.09 | 0.32 | 0.27 | 0.788 | 0.970 | n.s. |
| 4 to 3 - 6 to 3 | -0.19 | 0.33 | -0.56 | 0.576 | 0.970 | n.s. |
| 4 to 3 - Cardinality3 | -0.73 | 0.34 | -2.13 | 0.033 | 0.373 | n.s. |
| 5 to 3 - 6 to 3 | -0.27 | 0.29 | -0.93 | 0.354 | 0.970 | n.s. |
| 5 to 3 - Cardinality3 | -0.82 | 0.30 | -2.68 | 0.007 | 0.104 | n.s. |
| 6 to 3 - Cardinality3 | -0.54 | 0.31 | -1.73 | 0.083 | 0.678 | n.s. |

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

- Model converged successfully
- AIC = 471.46, BIC = 492.90
- **2 to 3 vs 1 to 3**: *β* = -0.69, *SE* = 1.599, *z* = -0.431, *p* = 0.667
- **4 to 3 vs 1 to 3**: *β* = -1.98, *SE* = 1.611, *z* = -1.232, *p* = 0.218
- **5 to 3 vs 1 to 3**: *β* = -0.56, *SE* = 1.428, *z* = -0.392, *p* = 0.695
- **6 to 3 vs 1 to 3**: *β* = -1.25, *SE* = 1.497, *z* = -0.838, *p* = 0.402
- **Cardinality3 vs 1 to 3**: *β* = -1.54, *SE* = 1.541, *z* = -1.003, *p* = 0.316
- **SNR**: *β* = -0.30, *SE* = 0.287, *z* = -1.033, *p* = 0.302

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.69 | 1.60 | 0.43 | 0.667 | 1.000 | n.s. |
| 1 to 3 - 4 to 3 | 1.98 | 1.61 | 1.23 | 0.218 | 0.975 | n.s. |
| 1 to 3 - 5 to 3 | 0.56 | 1.43 | 0.39 | 0.695 | 1.000 | n.s. |
| 1 to 3 - 6 to 3 | 1.25 | 1.50 | 0.84 | 0.402 | 0.998 | n.s. |
| 1 to 3 - Cardinality3 | 1.55 | 1.54 | 1.00 | 0.316 | 0.995 | n.s. |
| 2 to 3 - 4 to 3 | 1.29 | 1.59 | 0.81 | 0.416 | 0.998 | n.s. |
| 2 to 3 - 5 to 3 | -0.13 | 1.40 | -0.09 | 0.927 | 1.000 | n.s. |
| 2 to 3 - 6 to 3 | 0.57 | 1.45 | 0.39 | 0.696 | 1.000 | n.s. |
| 2 to 3 - Cardinality3 | 0.86 | 1.52 | 0.57 | 0.572 | 1.000 | n.s. |
| 4 to 3 - 5 to 3 | -1.42 | 1.42 | -1.00 | 0.315 | 0.995 | n.s. |
| 4 to 3 - 6 to 3 | -0.73 | 1.50 | -0.49 | 0.627 | 1.000 | n.s. |
| 4 to 3 - Cardinality3 | -0.44 | 1.53 | -0.29 | 0.775 | 1.000 | n.s. |
| 5 to 3 - 6 to 3 | 0.70 | 1.31 | 0.53 | 0.597 | 1.000 | n.s. |
| 5 to 3 - Cardinality3 | 0.99 | 1.36 | 0.72 | 0.469 | 0.998 | n.s. |
| 6 to 3 - Cardinality3 | 0.29 | 1.42 | 0.21 | 0.837 | 1.000 | n.s. |

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

- Model converged successfully
- AIC = 411.14, BIC = 435.28
- **2 to 3 vs 1 to 3**: *β* = -0.07, *SE* = 0.442, *z* = -0.157, *p* = 0.875
- **4 to 3 vs 1 to 3**: *β* = -0.31, *SE* = 0.406, *z* = -0.768, *p* = 0.443
- **5 to 3 vs 1 to 3**: *β* = -0.44, *SE* = 0.404, *z* = -1.080, *p* = 0.280
- **6 to 3 vs 1 to 3**: *β* = 0.04, *SE* = 0.407, *z* = 0.101, *p* = 0.919
- **Cardinality3 vs 1 to 3**: *β* = -0.52, *SE* = 0.450, *z* = -1.160, *p* = 0.246
- **SNR**: *β* = 0.47, *SE* = 0.051, *z* = 9.278, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.07 | 0.44 | 0.16 | 0.875 | 0.999 | n.s. |
| 1 to 3 - 4 to 3 | 0.31 | 0.41 | 0.77 | 0.443 | 0.993 | n.s. |
| 1 to 3 - 5 to 3 | 0.44 | 0.40 | 1.08 | 0.280 | 0.981 | n.s. |
| 1 to 3 - 6 to 3 | -0.04 | 0.41 | -0.10 | 0.919 | 0.999 | n.s. |
| 1 to 3 - Cardinality3 | 0.52 | 0.45 | 1.16 | 0.246 | 0.979 | n.s. |
| 2 to 3 - 4 to 3 | 0.24 | 0.45 | 0.54 | 0.588 | 0.998 | n.s. |
| 2 to 3 - 5 to 3 | 0.37 | 0.44 | 0.83 | 0.404 | 0.993 | n.s. |
| 2 to 3 - 6 to 3 | -0.11 | 0.45 | -0.25 | 0.804 | 0.999 | n.s. |
| 2 to 3 - Cardinality3 | 0.45 | 0.49 | 0.92 | 0.358 | 0.992 | n.s. |
| 4 to 3 - 5 to 3 | 0.12 | 0.41 | 0.30 | 0.762 | 0.999 | n.s. |
| 4 to 3 - 6 to 3 | -0.35 | 0.41 | -0.86 | 0.393 | 0.993 | n.s. |
| 4 to 3 - Cardinality3 | 0.21 | 0.45 | 0.46 | 0.642 | 0.998 | n.s. |
| 5 to 3 - 6 to 3 | -0.48 | 0.41 | -1.17 | 0.241 | 0.979 | n.s. |
| 5 to 3 - Cardinality3 | 0.09 | 0.44 | 0.19 | 0.847 | 0.999 | n.s. |
| 6 to 3 - Cardinality3 | 0.56 | 0.45 | 1.25 | 0.211 | 0.971 | n.s. |

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

- Model converged successfully
- AIC = 972.29, BIC = 996.43
- **2 to 3 vs 1 to 3**: *β* = -6.80, *SE* = 6.549, *z* = -1.038, *p* = 0.299
- **4 to 3 vs 1 to 3**: *β* = -3.28, *SE* = 6.083, *z* = -0.540, *p* = 0.589
- **5 to 3 vs 1 to 3**: *β* = -1.73, *SE* = 6.019, *z* = -0.287, *p* = 0.774
- **6 to 3 vs 1 to 3**: *β* = -3.16, *SE* = 6.081, *z* = -0.520, *p* = 0.603
- **Cardinality3 vs 1 to 3**: *β* = -15.40, *SE* = 6.646, *z* = -2.318, *p* = 0.020
- **SNR**: *β* = 0.56, *SE* = 0.679, *z* = 0.817, *p* = 0.414

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 6.80 | 6.55 | 1.04 | 0.299 | 0.971 | n.s. |
| 1 to 3 - 4 to 3 | 3.28 | 6.08 | 0.54 | 0.589 | 0.999 | n.s. |
| 1 to 3 - 5 to 3 | 1.73 | 6.02 | 0.29 | 0.774 | 0.999 | n.s. |
| 1 to 3 - 6 to 3 | 3.16 | 6.08 | 0.52 | 0.603 | 0.999 | n.s. |
| 1 to 3 - Cardinality3 | 15.40 | 6.65 | 2.32 | 0.020 | 0.267 | n.s. |
| 2 to 3 - 4 to 3 | -3.51 | 6.63 | -0.53 | 0.596 | 0.999 | n.s. |
| 2 to 3 - 5 to 3 | -5.07 | 6.55 | -0.77 | 0.439 | 0.995 | n.s. |
| 2 to 3 - 6 to 3 | -3.64 | 6.62 | -0.55 | 0.583 | 0.999 | n.s. |
| 2 to 3 - Cardinality3 | 8.61 | 7.23 | 1.19 | 0.234 | 0.947 | n.s. |
| 4 to 3 - 5 to 3 | -1.56 | 6.10 | -0.26 | 0.799 | 0.999 | n.s. |
| 4 to 3 - 6 to 3 | -0.12 | 6.17 | -0.02 | 0.984 | 0.999 | n.s. |
| 4 to 3 - Cardinality3 | 12.12 | 6.69 | 1.81 | 0.070 | 0.596 | n.s. |
| 5 to 3 - 6 to 3 | 1.43 | 6.08 | 0.24 | 0.814 | 0.999 | n.s. |
| 5 to 3 - Cardinality3 | 13.68 | 6.59 | 2.07 | 0.038 | 0.419 | n.s. |
| 6 to 3 - Cardinality3 | 12.24 | 6.69 | 1.83 | 0.067 | 0.596 | n.s. |

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
