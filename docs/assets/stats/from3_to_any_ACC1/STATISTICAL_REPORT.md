# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:20:50

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
| 3 to 1 | 18 | -2.65 µV | 2.17 | 0.51 | [-6.82, -0.01] |
| 3 to 2 | 22 | -3.92 µV | 2.01 | 0.43 | [-7.98, -0.58] |
| 3 to 3 | 22 | -3.22 µV | 1.65 | 0.35 | [-7.54, -0.94] |
| 3 to 4 | 23 | -3.39 µV | 1.76 | 0.37 | [-7.06, -0.73] |
| 3 to 5 | 22 | -3.64 µV | 2.30 | 0.49 | [-10.12, -0.74] |
| 3 to 6 | 23 | -4.87 µV | 2.57 | 0.54 | [-10.95, -1.29] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 181.97 ms | 13.13 | 3.09 | [160.44, 207.70] |
| 3 to 2 | 22 | 171.18 ms | 8.92 | 1.90 | [158.22, 195.85] |
| 3 to 3 | 22 | 172.31 ms | 10.44 | 2.23 | [151.69, 197.41] |
| 3 to 4 | 23 | 169.92 ms | 11.56 | 2.41 | [143.66, 200.12] |
| 3 to 5 | 22 | 169.65 ms | 10.64 | 2.27 | [154.48, 196.10] |
| 3 to 6 | 23 | 173.08 ms | 10.66 | 2.22 | [155.52, 195.70] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 2.06 µV | 1.39 | 0.33 | [0.10, 5.76] |
| 3 to 2 | 10 | 1.82 µV | 1.51 | 0.48 | [-0.00, 3.98] |
| 3 to 3 | 13 | 2.24 µV | 1.98 | 0.55 | [0.18, 7.43] |
| 3 to 4 | 14 | 2.08 µV | 1.99 | 0.53 | [0.18, 6.53] |
| 3 to 5 | 11 | 2.15 µV | 1.56 | 0.47 | [0.12, 4.94] |
| 3 to 6 | 10 | 2.39 µV | 2.38 | 0.75 | [-0.02, 6.95] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 106.54 ms | 5.21 | 1.23 | [93.98, 115.32] |
| 3 to 2 | 10 | 104.36 ms | 4.04 | 1.28 | [96.85, 110.28] |
| 3 to 3 | 13 | 105.34 ms | 4.44 | 1.23 | [95.65, 112.11] |
| 3 to 4 | 14 | 103.31 ms | 5.38 | 1.44 | [94.03, 110.86] |
| 3 to 5 | 11 | 104.77 ms | 5.10 | 1.54 | [96.83, 114.70] |
| 3 to 6 | 10 | 104.27 ms | 6.98 | 2.21 | [95.39, 115.78] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 4.15 µV | 2.51 | 0.56 | [0.73, 10.83] |
| 3 to 2 | 18 | 4.32 µV | 3.21 | 0.76 | [0.38, 12.41] |
| 3 to 3 | 15 | 2.43 µV | 2.03 | 0.52 | [0.14, 6.55] |
| 3 to 4 | 16 | 4.24 µV | 2.29 | 0.57 | [0.16, 6.99] |
| 3 to 5 | 16 | 3.81 µV | 2.57 | 0.64 | [-0.00, 9.70] |
| 3 to 6 | 19 | 2.96 µV | 1.98 | 0.46 | [0.36, 8.92] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 480.90 ms | 11.87 | 2.65 | [462.53, 504.81] |
| 3 to 2 | 18 | 488.17 ms | 18.95 | 4.47 | [442.81, 529.06] |
| 3 to 3 | 15 | 473.58 ms | 24.85 | 6.42 | [432.05, 531.18] |
| 3 to 4 | 16 | 488.78 ms | 13.87 | 3.47 | [462.52, 518.00] |
| 3 to 5 | 16 | 485.51 ms | 21.30 | 5.32 | [445.08, 537.40] |
| 3 to 6 | 19 | 481.95 ms | 18.23 | 4.18 | [437.44, 511.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 463.70, BIC = 489.51
- **3 to 2 vs 3 to 1**: *β* = -0.17, *SE* = 0.400, *z* = -0.428, *p* = 0.668
- **3 to 3 vs 3 to 1**: *β* = -0.02, *SE* = 0.391, *z* = -0.046, *p* = 0.963
- **3 to 4 vs 3 to 1**: *β* = -0.13, *SE* = 0.386, *z* = -0.343, *p* = 0.732
- **3 to 5 vs 3 to 1**: *β* = 0.06, *SE* = 0.398, *z* = 0.137, *p* = 0.891
- **3 to 6 vs 3 to 1**: *β* = -1.20, *SE* = 0.397, *z* = -3.011, *p* = 0.003
- **SNR**: *β* = -0.53, *SE* = 0.050, *z* = -10.536, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.17 | 0.40 | 0.43 | 0.668 | 1.000 | n.s. |
| 3 to 1 - 3 to 3 | 0.02 | 0.39 | 0.05 | 0.963 | 1.000 | n.s. |
| 3 to 1 - 3 to 4 | 0.13 | 0.39 | 0.34 | 0.732 | 1.000 | n.s. |
| 3 to 1 - 3 to 5 | -0.05 | 0.40 | -0.14 | 0.891 | 1.000 | n.s. |
| 3 to 1 - 3 to 6 | 1.20 | 0.40 | 3.01 | 0.003 | 0.033 | * |
| 3 to 2 - 3 to 3 | -0.15 | 0.37 | -0.42 | 0.675 | 1.000 | n.s. |
| 3 to 2 - 3 to 4 | -0.04 | 0.36 | -0.11 | 0.914 | 1.000 | n.s. |
| 3 to 2 - 3 to 5 | -0.23 | 0.36 | -0.63 | 0.532 | 0.999 | n.s. |
| 3 to 2 - 3 to 6 | 1.02 | 0.36 | 2.86 | 0.004 | 0.045 | * |
| 3 to 3 - 3 to 4 | 0.11 | 0.36 | 0.32 | 0.751 | 1.000 | n.s. |
| 3 to 3 - 3 to 5 | -0.07 | 0.37 | -0.20 | 0.843 | 1.000 | n.s. |
| 3 to 3 - 3 to 6 | 1.18 | 0.36 | 3.26 | 0.001 | 0.015 | * |
| 3 to 4 - 3 to 5 | -0.19 | 0.36 | -0.52 | 0.604 | 1.000 | n.s. |
| 3 to 4 - 3 to 6 | 1.06 | 0.36 | 2.98 | 0.003 | 0.035 | * |
| 3 to 5 - 3 to 6 | 1.25 | 0.36 | 3.49 | < .001 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.16, *p* = 0.012, η²_G = 0.102
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 2.33 | 15 | = 0.129 | 0.63 [0.07, 1.20] | medium | n.s. |
| 3 to 1 vs 3 to 3 | 0.85 | 15 | = 0.518 | 0.26 [-0.33, 0.75] | small | n.s. |
| 3 to 1 vs 3 to 4 | 1.61 | 15 | = 0.274 | 0.40 [-0.04, 1.02] | small | n.s. |
| 3 to 1 vs 3 to 5 | 0.93 | 15 | = 0.518 | 0.34 [-0.26, 0.79] | small | n.s. |
| 3 to 1 vs 3 to 6 | 2.86 | 15 | = 0.091 | 0.96 [0.14, 1.29] | large | n.s. |
| 3 to 2 vs 3 to 3 | -1.92 | 15 | = 0.184 | -0.44 [-0.86, 0.09] | small | n.s. |
| 3 to 2 vs 3 to 4 | -1.07 | 15 | = 0.500 | -0.27 [-0.71, 0.19] | small | n.s. |
| 3 to 2 vs 3 to 5 | -0.84 | 15 | = 0.518 | -0.23 [-0.57, 0.32] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.38 | 15 | = 0.351 | 0.38 [-0.03, 0.89] | small | n.s. |
| 3 to 3 vs 3 to 4 | 0.64 | 15 | = 0.615 | 0.17 [-0.37, 0.54] | negligible | n.s. |
| 3 to 3 vs 3 to 5 | 0.53 | 15 | = 0.645 | 0.14 [-0.27, 0.65] | negligible | n.s. |
| 3 to 3 vs 3 to 6 | 2.85 | 15 | = 0.091 | 0.81 [0.29, 1.31] | large | n.s. |
| 3 to 4 vs 3 to 5 | -0.01 | 15 | = 0.989 | -0.00 [-0.37, 0.52] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 2.16 | 15 | = 0.142 | 0.64 [0.12, 1.09] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 2.35 | 15 | = 0.129 | 0.57 [0.10, 1.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 962.00, BIC = 987.81
- **3 to 2 vs 3 to 1**: *β* = -9.19, *SE* = 2.556, *z* = -3.594, *p* < .001
- **3 to 3 vs 3 to 1**: *β* = -8.63, *SE* = 2.496, *z* = -3.456, *p* = 0.001
- **3 to 4 vs 3 to 1**: *β* = -11.38, *SE* = 2.454, *z* = -4.636, *p* < .001
- **3 to 5 vs 3 to 1**: *β* = -10.73, *SE* = 2.546, *z* = -4.213, *p* < .001
- **3 to 6 vs 3 to 1**: *β* = -8.07, *SE* = 2.538, *z* = -3.178, *p* = 0.001
- **SNR**: *β* = -0.10, *SE* = 0.327, *z* = -0.302, *p* = 0.763

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 9.19 | 2.56 | 3.59 | < .001 | 0.004 | ** |
| 3 to 1 - 3 to 3 | 8.63 | 2.50 | 3.46 | < .001 | 0.007 | ** |
| 3 to 1 - 3 to 4 | 11.38 | 2.45 | 4.64 | < .001 | < .001 | *** |
| 3 to 1 - 3 to 5 | 10.73 | 2.55 | 4.21 | < .001 | < .001 | *** |
| 3 to 1 - 3 to 6 | 8.07 | 2.54 | 3.18 | 0.001 | 0.016 | * |
| 3 to 2 - 3 to 3 | -0.56 | 2.33 | -0.24 | 0.809 | 0.989 | n.s. |
| 3 to 2 - 3 to 4 | 2.19 | 2.29 | 0.95 | 0.340 | 0.945 | n.s. |
| 3 to 2 - 3 to 5 | 1.54 | 2.29 | 0.67 | 0.501 | 0.969 | n.s. |
| 3 to 2 - 3 to 6 | -1.12 | 2.27 | -0.49 | 0.622 | 0.979 | n.s. |
| 3 to 3 - 3 to 4 | 2.75 | 2.29 | 1.20 | 0.229 | 0.904 | n.s. |
| 3 to 3 - 3 to 5 | 2.10 | 2.32 | 0.90 | 0.366 | 0.945 | n.s. |
| 3 to 3 - 3 to 6 | -0.56 | 2.29 | -0.24 | 0.807 | 0.989 | n.s. |
| 3 to 4 - 3 to 5 | -0.65 | 2.29 | -0.28 | 0.777 | 0.989 | n.s. |
| 3 to 4 - 3 to 6 | -3.31 | 2.27 | -1.46 | 0.145 | 0.792 | n.s. |
| 3 to 5 - 3 to 6 | -2.66 | 2.27 | -1.17 | 0.242 | 0.904 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.71, *p* < .001, η²_G = 0.112
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 3.08 | 15 | = 0.038 | 0.95 [0.17, 1.34] | large | * |
| 3 to 1 vs 3 to 3 | 2.69 | 15 | = 0.064 | 0.66 [0.08, 1.26] | medium | n.s. |
| 3 to 1 vs 3 to 4 | 4.22 | 15 | = 0.011 | 0.93 [0.36, 1.56] | large | * |
| 3 to 1 vs 3 to 5 | 3.29 | 15 | = 0.037 | 0.81 [0.27, 1.48] | large | * |
| 3 to 1 vs 3 to 6 | 2.47 | 15 | = 0.078 | 0.84 [0.10, 1.24] | large | n.s. |
| 3 to 2 vs 3 to 3 | -1.24 | 15 | = 0.499 | -0.29 [-0.40, 0.51] | small | n.s. |
| 3 to 2 vs 3 to 4 | 0.39 | 15 | = 0.875 | 0.10 [-0.23, 0.67] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.01 | 15 | = 0.991 | 0.00 [-0.33, 0.56] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | -0.24 | 15 | = 0.875 | -0.06 [-0.51, 0.37] | negligible | n.s. |
| 3 to 3 vs 3 to 4 | 1.70 | 15 | = 0.276 | 0.35 [-0.12, 0.82] | small | n.s. |
| 3 to 3 vs 3 to 5 | 1.09 | 15 | = 0.524 | 0.24 [-0.23, 0.70] | small | n.s. |
| 3 to 3 vs 3 to 6 | 1.04 | 15 | = 0.524 | 0.21 [-0.43, 0.45] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.47 | 15 | = 0.875 | -0.09 [-0.59, 0.30] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -0.61 | 15 | = 0.825 | -0.15 [-0.82, 0.09] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | -0.25 | 15 | = 0.875 | -0.05 [-0.72, 0.18] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 234.57, BIC = 255.55
- **3 to 2 vs 3 to 1**: *β* = -0.20, *SE* = 0.344, *z* = -0.567, *p* = 0.571
- **3 to 3 vs 3 to 1**: *β* = 0.21, *SE* = 0.316, *z* = 0.675, *p* = 0.500
- **3 to 4 vs 3 to 1**: *β* = 0.27, *SE* = 0.311, *z* = 0.883, *p* = 0.377
- **3 to 5 vs 3 to 1**: *β* = -0.03, *SE* = 0.336, *z* = -0.083, *p* = 0.934
- **3 to 6 vs 3 to 1**: *β* = -0.08, *SE* = 0.349, *z* = -0.241, *p* = 0.809
- **SNR**: *β* = 0.60, *SE* = 0.057, *z* = 10.565, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.19 | 0.34 | 0.57 | 0.571 | 0.998 | n.s. |
| 3 to 1 - 3 to 3 | -0.21 | 0.32 | -0.67 | 0.500 | 0.998 | n.s. |
| 3 to 1 - 3 to 4 | -0.27 | 0.31 | -0.88 | 0.377 | 0.997 | n.s. |
| 3 to 1 - 3 to 5 | 0.03 | 0.34 | 0.08 | 0.934 | 0.999 | n.s. |
| 3 to 1 - 3 to 6 | 0.08 | 0.35 | 0.24 | 0.809 | 0.999 | n.s. |
| 3 to 2 - 3 to 3 | -0.41 | 0.36 | -1.14 | 0.252 | 0.983 | n.s. |
| 3 to 2 - 3 to 4 | -0.47 | 0.36 | -1.30 | 0.193 | 0.960 | n.s. |
| 3 to 2 - 3 to 5 | -0.17 | 0.38 | -0.44 | 0.658 | 0.998 | n.s. |
| 3 to 2 - 3 to 6 | -0.11 | 0.38 | -0.29 | 0.773 | 0.999 | n.s. |
| 3 to 3 - 3 to 4 | -0.06 | 0.34 | -0.18 | 0.855 | 0.999 | n.s. |
| 3 to 3 - 3 to 5 | 0.24 | 0.35 | 0.68 | 0.496 | 0.998 | n.s. |
| 3 to 3 - 3 to 6 | 0.30 | 0.36 | 0.83 | 0.405 | 0.997 | n.s. |
| 3 to 4 - 3 to 5 | 0.30 | 0.35 | 0.86 | 0.389 | 0.997 | n.s. |
| 3 to 4 - 3 to 6 | 0.36 | 0.37 | 0.97 | 0.332 | 0.995 | n.s. |
| 3 to 5 - 3 to 6 | 0.06 | 0.38 | 0.15 | 0.882 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.81, *p* = 0.589, η²_G = 0.407
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -13.52 | 1 | = 0.705 | -2.80 [-0.52, 1.04] | large | n.s. |
| 3 to 1 vs 3 to 3 | -1.03 | 1 | = 0.795 | -1.30 [-0.47, 0.89] | large | n.s. |
| 3 to 1 vs 3 to 4 | -0.77 | 1 | = 0.795 | -0.62 [-0.42, 1.05] | medium | n.s. |
| 3 to 1 vs 3 to 5 | -2.20 | 1 | = 0.795 | -1.19 [-0.71, 0.96] | large | n.s. |
| 3 to 1 vs 3 to 6 | -1.64 | 1 | = 0.795 | -1.01 [-0.85, 1.01] | large | n.s. |
| 3 to 2 vs 3 to 3 | 0.14 | 1 | = 0.945 | 0.19 [-1.11, 0.59] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 3.48 | 1 | = 0.795 | 2.99 [-1.19, 0.69] | large | n.s. |
| 3 to 2 vs 3 to 5 | 1.51 | 1 | = 0.795 | 0.58 [-1.29, 0.83] | medium | n.s. |
| 3 to 2 vs 3 to 6 | 1.08 | 1 | = 0.795 | 0.52 [-1.28, 0.84] | medium | n.s. |
| 3 to 3 vs 3 to 4 | 1.09 | 1 | = 0.795 | 1.16 [-0.63, 1.06] | large | n.s. |
| 3 to 3 vs 3 to 5 | 0.18 | 1 | = 0.945 | 0.26 [-0.80, 1.06] | small | n.s. |
| 3 to 3 vs 3 to 6 | 0.17 | 1 | = 0.945 | 0.25 [-0.84, 0.83] | small | n.s. |
| 3 to 4 vs 3 to 5 | -1.11 | 1 | = 0.795 | -1.02 [-0.52, 1.43] | large | n.s. |
| 3 to 4 vs 3 to 6 | -0.90 | 1 | = 0.795 | -0.84 [-1.12, 1.37] | large | n.s. |
| 3 to 5 vs 3 to 6 | 0.09 | 1 | = 0.945 | 0.01 [-0.68, 1.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 479.06, BIC = 500.03
- **3 to 2 vs 3 to 1**: *β* = -2.15, *SE* = 1.985, *z* = -1.082, *p* = 0.279
- **3 to 3 vs 3 to 1**: *β* = -1.18, *SE* = 1.830, *z* = -0.645, *p* = 0.519
- **3 to 4 vs 3 to 1**: *β* = -3.18, *SE* = 1.800, *z* = -1.769, *p* = 0.077
- **3 to 5 vs 3 to 1**: *β* = -1.77, *SE* = 1.939, *z* = -0.914, *p* = 0.360
- **3 to 6 vs 3 to 1**: *β* = -2.27, *SE* = 1.979, *z* = -1.146, *p* = 0.252
- **SNR**: *β* = 0.06, *SE* = 0.304, *z* = 0.208, *p* = 0.835

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 2.15 | 1.99 | 1.08 | 0.279 | 0.986 | n.s. |
| 3 to 1 - 3 to 3 | 1.18 | 1.83 | 0.65 | 0.519 | 0.999 | n.s. |
| 3 to 1 - 3 to 4 | 3.18 | 1.80 | 1.77 | 0.077 | 0.699 | n.s. |
| 3 to 1 - 3 to 5 | 1.77 | 1.94 | 0.91 | 0.360 | 0.993 | n.s. |
| 3 to 1 - 3 to 6 | 2.27 | 1.98 | 1.15 | 0.252 | 0.983 | n.s. |
| 3 to 2 - 3 to 3 | -0.97 | 2.11 | -0.46 | 0.647 | 0.999 | n.s. |
| 3 to 2 - 3 to 4 | 1.04 | 2.08 | 0.50 | 0.619 | 0.999 | n.s. |
| 3 to 2 - 3 to 5 | -0.38 | 2.21 | -0.17 | 0.865 | 0.999 | n.s. |
| 3 to 2 - 3 to 6 | 0.12 | 2.25 | 0.05 | 0.957 | 0.999 | n.s. |
| 3 to 3 - 3 to 4 | 2.00 | 1.94 | 1.03 | 0.302 | 0.987 | n.s. |
| 3 to 3 - 3 to 5 | 0.59 | 2.07 | 0.29 | 0.774 | 0.999 | n.s. |
| 3 to 3 - 3 to 6 | 1.09 | 2.11 | 0.51 | 0.607 | 0.999 | n.s. |
| 3 to 4 - 3 to 5 | -1.41 | 2.06 | -0.68 | 0.494 | 0.999 | n.s. |
| 3 to 4 - 3 to 6 | -0.92 | 2.09 | -0.44 | 0.661 | 0.999 | n.s. |
| 3 to 5 - 3 to 6 | 0.50 | 2.21 | 0.22 | 0.823 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.826, η²_G = 0.280
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.53 | 1 | = 0.822 | -0.68 [-0.65, 0.89] | medium | n.s. |
| 3 to 1 vs 3 to 3 | -0.53 | 1 | = 0.822 | -0.59 [-0.72, 0.63] | medium | n.s. |
| 3 to 1 vs 3 to 4 | -0.74 | 1 | = 0.822 | -0.91 [-0.60, 0.83] | large | n.s. |
| 3 to 1 vs 3 to 5 | -0.73 | 1 | = 0.822 | -0.92 [-0.57, 1.14] | large | n.s. |
| 3 to 1 vs 3 to 6 | -0.55 | 1 | = 0.822 | -0.77 [-1.09, 0.77] | medium | n.s. |
| 3 to 2 vs 3 to 3 | 0.56 | 1 | = 0.822 | 0.33 [-0.75, 0.93] | small | n.s. |
| 3 to 2 vs 3 to 4 | -3.08 | 1 | = 0.822 | -0.50 [-1.38, 0.55] | medium | n.s. |
| 3 to 2 vs 3 to 5 | -5.75 | 1 | = 0.822 | -0.51 [-0.82, 1.31] | medium | n.s. |
| 3 to 2 vs 3 to 6 | -0.65 | 1 | = 0.822 | -0.26 [-1.09, 1.01] | small | n.s. |
| 3 to 3 vs 3 to 4 | -2.34 | 1 | = 0.822 | -1.14 [-1.10, 0.60] | large | n.s. |
| 3 to 3 vs 3 to 5 | -2.02 | 1 | = 0.822 | -1.09 [-0.71, 1.16] | large | n.s. |
| 3 to 3 vs 3 to 6 | -0.61 | 1 | = 0.822 | -0.48 [-0.87, 0.81] | small | n.s. |
| 3 to 4 vs 3 to 5 | -0.49 | 1 | = 0.822 | -0.04 [-1.16, 0.72] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 0.08 | 1 | = 0.950 | 0.04 [-0.81, 1.82] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | 0.13 | 1 | = 0.950 | 0.06 [-1.36, 0.78] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 438.25, BIC = 462.05
- **3 to 2 vs 3 to 1**: *β* = 0.99, *SE* = 0.536, *z* = 1.850, *p* = 0.064
- **3 to 3 vs 3 to 1**: *β* = -0.79, *SE* = 0.573, *z* = -1.386, *p* = 0.166
- **3 to 4 vs 3 to 1**: *β* = 0.52, *SE* = 0.550, *z* = 0.951, *p* = 0.342
- **3 to 5 vs 3 to 1**: *β* = 0.37, *SE* = 0.561, *z* = 0.654, *p* = 0.513
- **3 to 6 vs 3 to 1**: *β* = -0.19, *SE* = 0.542, *z* = -0.357, *p* = 0.721
- **SNR**: *β* = 0.23, *SE* = 0.044, *z* = 5.292, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -0.99 | 0.54 | -1.85 | 0.064 | 0.519 | n.s. |
| 3 to 1 - 3 to 3 | 0.79 | 0.57 | 1.39 | 0.166 | 0.837 | n.s. |
| 3 to 1 - 3 to 4 | -0.52 | 0.55 | -0.95 | 0.342 | 0.906 | n.s. |
| 3 to 1 - 3 to 5 | -0.37 | 0.56 | -0.65 | 0.513 | 0.906 | n.s. |
| 3 to 1 - 3 to 6 | 0.19 | 0.54 | 0.36 | 0.721 | 0.922 | n.s. |
| 3 to 2 - 3 to 3 | 1.78 | 0.56 | 3.18 | 0.001 | 0.022 | * |
| 3 to 2 - 3 to 4 | 0.47 | 0.55 | 0.85 | 0.394 | 0.906 | n.s. |
| 3 to 2 - 3 to 5 | 0.62 | 0.55 | 1.14 | 0.256 | 0.906 | n.s. |
| 3 to 2 - 3 to 6 | 1.18 | 0.52 | 2.26 | 0.024 | 0.288 | n.s. |
| 3 to 3 - 3 to 4 | -1.32 | 0.59 | -2.24 | 0.025 | 0.288 | n.s. |
| 3 to 3 - 3 to 5 | -1.16 | 0.58 | -2.01 | 0.044 | 0.419 | n.s. |
| 3 to 3 - 3 to 6 | -0.60 | 0.55 | -1.09 | 0.277 | 0.906 | n.s. |
| 3 to 4 - 3 to 5 | 0.16 | 0.57 | 0.27 | 0.783 | 0.922 | n.s. |
| 3 to 4 - 3 to 6 | 0.72 | 0.54 | 1.32 | 0.188 | 0.846 | n.s. |
| 3 to 5 - 3 to 6 | 0.56 | 0.54 | 1.04 | 0.299 | 0.906 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.51, *p* = 0.003, η²_G = 0.210
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.27 | 7 | = 0.407 | -0.46 [-0.64, 0.39] | small | n.s. |
| 3 to 1 vs 3 to 3 | 3.33 | 7 | = 0.048 | 1.09 [-0.11, 1.06] | large | * |
| 3 to 1 vs 3 to 4 | 0.07 | 7 | = 0.945 | 0.03 [-0.39, 0.77] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | 0.20 | 7 | = 0.945 | 0.06 [-0.40, 0.71] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 0.79 | 7 | = 0.606 | 0.36 [-0.18, 0.88] | small | n.s. |
| 3 to 2 vs 3 to 3 | 4.86 | 7 | = 0.028 | 1.55 [-0.05, 1.27] | large | * |
| 3 to 2 vs 3 to 4 | 1.60 | 7 | = 0.331 | 0.55 [-0.28, 0.91] | medium | n.s. |
| 3 to 2 vs 3 to 5 | 1.48 | 7 | = 0.340 | 0.51 [-0.18, 1.03] | medium | n.s. |
| 3 to 2 vs 3 to 6 | 3.95 | 7 | = 0.042 | 0.85 [0.19, 1.41] | large | * |
| 3 to 3 vs 3 to 4 | -3.39 | 7 | = 0.048 | -1.32 [-1.98, -0.18] | large | * |
| 3 to 3 vs 3 to 5 | -2.99 | 7 | = 0.061 | -1.02 [-1.09, 0.24] | large | n.s. |
| 3 to 3 vs 3 to 6 | -2.02 | 7 | = 0.209 | -0.85 [-0.89, 0.29] | large | n.s. |
| 3 to 4 vs 3 to 5 | 0.12 | 7 | = 0.945 | 0.04 [-0.40, 0.82] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.10 | 7 | = 0.464 | 0.41 [0.01, 1.21] | small | n.s. |
| 3 to 5 vs 3 to 6 | 0.74 | 7 | = 0.606 | 0.29 [-0.23, 0.91] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 907.41, BIC = 931.21
- **3 to 2 vs 3 to 1**: *β* = 8.02, *SE* = 5.467, *z* = 1.467, *p* = 0.142
- **3 to 3 vs 3 to 1**: *β* = -6.60, *SE* = 5.840, *z* = -1.130, *p* = 0.259
- **3 to 4 vs 3 to 1**: *β* = 8.76, *SE* = 5.592, *z* = 1.566, *p* = 0.117
- **3 to 5 vs 3 to 1**: *β* = 7.13, *SE* = 5.722, *z* = 1.247, *p* = 0.212
- **3 to 6 vs 3 to 1**: *β* = 1.93, *SE* = 5.517, *z* = 0.350, *p* = 0.726
- **SNR**: *β* = 0.39, *SE* = 0.425, *z* = 0.926, *p* = 0.354

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -8.02 | 5.47 | -1.47 | 0.142 | 0.786 | n.s. |
| 3 to 1 - 3 to 3 | 6.60 | 5.84 | 1.13 | 0.259 | 0.883 | n.s. |
| 3 to 1 - 3 to 4 | -8.76 | 5.59 | -1.57 | 0.117 | 0.777 | n.s. |
| 3 to 1 - 3 to 5 | -7.14 | 5.72 | -1.25 | 0.212 | 0.883 | n.s. |
| 3 to 1 - 3 to 6 | -1.93 | 5.52 | -0.35 | 0.726 | 0.994 | n.s. |
| 3 to 2 - 3 to 3 | 14.61 | 5.74 | 2.55 | 0.011 | 0.145 | n.s. |
| 3 to 2 - 3 to 4 | -0.74 | 5.63 | -0.13 | 0.896 | 0.994 | n.s. |
| 3 to 2 - 3 to 5 | 0.88 | 5.65 | 0.16 | 0.876 | 0.994 | n.s. |
| 3 to 2 - 3 to 6 | 6.08 | 5.38 | 1.13 | 0.258 | 0.883 | n.s. |
| 3 to 3 - 3 to 4 | -15.35 | 5.99 | -2.56 | 0.010 | 0.145 | n.s. |
| 3 to 3 - 3 to 5 | -13.73 | 5.94 | -2.31 | 0.021 | 0.240 | n.s. |
| 3 to 3 - 3 to 6 | -8.53 | 5.64 | -1.51 | 0.131 | 0.786 | n.s. |
| 3 to 4 - 3 to 5 | 1.62 | 5.82 | 0.28 | 0.781 | 0.994 | n.s. |
| 3 to 4 - 3 to 6 | 6.82 | 5.59 | 1.22 | 0.222 | 0.883 | n.s. |
| 3 to 5 - 3 to 6 | 5.20 | 5.59 | 0.93 | 0.352 | 0.886 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.40, *p* = 0.013, η²_G = 0.274
- Greenhouse-Geisser corrected: *p* = 0.054 (ε = 0.457)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -0.16 | 7 | = 0.875 | -0.05 [-0.77, 0.27] | negligible | n.s. |
| 3 to 1 vs 3 to 3 | 1.54 | 7 | = 0.342 | 0.88 [-0.26, 0.88] | large | n.s. |
| 3 to 1 vs 3 to 4 | -1.47 | 7 | = 0.342 | -0.88 [-1.21, 0.04] | large | n.s. |
| 3 to 1 vs 3 to 5 | -1.32 | 7 | = 0.342 | -0.79 [-0.75, 0.37] | medium | n.s. |
| 3 to 1 vs 3 to 6 | 0.67 | 7 | = 0.606 | 0.18 [-0.59, 0.44] | negligible | n.s. |
| 3 to 2 vs 3 to 3 | 1.89 | 7 | = 0.342 | 0.87 [0.10, 1.48] | large | n.s. |
| 3 to 2 vs 3 to 4 | -1.34 | 7 | = 0.342 | -0.76 [-0.73, 0.43] | medium | n.s. |
| 3 to 2 vs 3 to 5 | -1.20 | 7 | = 0.367 | -0.71 [-0.66, 0.50] | medium | n.s. |
| 3 to 2 vs 3 to 6 | 0.87 | 7 | = 0.518 | 0.21 [-0.40, 0.67] | small | n.s. |
| 3 to 3 vs 3 to 4 | -3.37 | 7 | = 0.179 | -1.41 [-2.12, -0.25] | large | n.s. |
| 3 to 3 vs 3 to 5 | -2.80 | 7 | = 0.199 | -1.34 [-1.33, 0.06] | large | n.s. |
| 3 to 3 vs 3 to 6 | -1.56 | 7 | = 0.342 | -0.70 [-0.77, 0.40] | medium | n.s. |
| 3 to 4 vs 3 to 5 | -0.37 | 7 | = 0.777 | -0.09 [-0.65, 0.56] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.61 | 7 | = 0.342 | 0.93 [-0.30, 0.83] | large | n.s. |
| 3 to 5 vs 3 to 6 | 1.47 | 7 | = 0.342 | 0.86 [-0.24, 0.90] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.012) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 3 to 1 showed greater latency than 3 to 2 (*d* = 0.95)
  - 3 to 1 showed greater latency than 3 to 4 (*d* = 0.93)
  - 3 to 1 showed greater latency than 3 to 5 (*d* = 0.81)
**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 3 to 3 (*d* = 1.09)
  - 3 to 2 showed greater amplitude than 3 to 3 (*d* = 1.55)
  - 3 to 2 showed greater amplitude than 3 to 6 (*d* = 0.85)
  - 3 to 3 showed smaller amplitude than 3 to 4 (*d* = -1.32)
**P3b latency:** Significant main effect of condition (*p* = 0.013) (no significant pairwise comparisons)

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
