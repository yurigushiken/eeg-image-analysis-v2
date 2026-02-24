# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:17:04

---

## 1. Analysis Overview

**Total Measurements:** 448
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 2 to 1 | 24 | 109.00 ms | 8.69 | 1.77 | [96.00, 116.00] |
| 3 to 2 | 24 | 105.83 ms | 8.98 | 1.83 | [96.00, 116.00] |
| 4 to 3 | 24 | 106.17 ms | 7.82 | 1.60 | [96.00, 116.00] |
| 5 to 4 | 24 | 106.67 ms | 7.70 | 1.57 | [96.00, 116.00] |
| 6 to 5 | 16 | 106.50 ms | 8.63 | 2.16 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -1.70 µV | 2.23 | 0.45 | [-5.91, 3.96] |
| 3 to 2 | 24 | -1.31 µV | 2.28 | 0.46 | [-5.62, 2.93] |
| 4 to 3 | 24 | -0.71 µV | 2.15 | 0.44 | [-6.08, 2.67] |
| 5 to 4 | 24 | -1.73 µV | 2.89 | 0.59 | [-8.72, 3.27] |
| 6 to 5 | 16 | -0.56 µV | 2.78 | 0.69 | [-4.24, 5.53] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 182.83 ms | 14.47 | 2.95 | [160.00, 212.00] |
| 3 to 2 | 24 | 176.17 ms | 24.13 | 4.93 | [144.00, 212.00] |
| 4 to 3 | 24 | 174.83 ms | 17.83 | 3.64 | [152.00, 212.00] |
| 5 to 4 | 24 | 179.00 ms | 22.04 | 4.50 | [144.00, 212.00] |
| 6 to 5 | 16 | 180.75 ms | 23.74 | 5.94 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -3.58 µV | 3.34 | 0.68 | [-10.79, 2.16] |
| 3 to 2 | 24 | -5.94 µV | 2.56 | 0.52 | [-10.33, -1.67] |
| 4 to 3 | 24 | -6.03 µV | 2.75 | 0.56 | [-10.92, 1.75] |
| 5 to 4 | 24 | -5.87 µV | 3.15 | 0.64 | [-14.15, 0.28] |
| 6 to 5 | 16 | -7.34 µV | 2.23 | 0.56 | [-10.73, -3.38] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 114.83 ms | 7.41 | 1.51 | [100.00, 120.00] |
| 3 to 2 | 24 | 111.17 ms | 8.59 | 1.75 | [100.00, 120.00] |
| 4 to 3 | 24 | 109.83 ms | 8.67 | 1.77 | [100.00, 120.00] |
| 5 to 4 | 24 | 110.00 ms | 8.17 | 1.67 | [100.00, 120.00] |
| 6 to 5 | 16 | 109.50 ms | 8.12 | 2.03 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 3.32 µV | 2.79 | 0.57 | [-1.05, 9.13] |
| 3 to 2 | 24 | 0.61 µV | 2.30 | 0.47 | [-2.89, 6.10] |
| 4 to 3 | 24 | 0.77 µV | 2.20 | 0.45 | [-3.32, 5.30] |
| 5 to 4 | 24 | 1.49 µV | 2.73 | 0.56 | [-3.65, 6.01] |
| 6 to 5 | 16 | 0.61 µV | 2.66 | 0.67 | [-3.81, 6.31] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 506.17 ms | 38.89 | 7.94 | [440.00, 556.00] |
| 3 to 2 | 24 | 492.00 ms | 36.94 | 7.54 | [440.00, 556.00] |
| 4 to 3 | 24 | 482.17 ms | 28.84 | 5.89 | [444.00, 544.00] |
| 5 to 4 | 24 | 500.00 ms | 35.87 | 7.32 | [440.00, 556.00] |
| 6 to 5 | 16 | 513.50 ms | 47.24 | 11.81 | [440.00, 556.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 5.48 µV | 3.59 | 0.73 | [-2.33, 11.21] |
| 3 to 2 | 24 | 5.40 µV | 4.39 | 0.90 | [-1.20, 17.81] |
| 4 to 3 | 24 | 4.94 µV | 3.61 | 0.74 | [-1.86, 11.65] |
| 5 to 4 | 24 | 5.17 µV | 3.95 | 0.81 | [-3.32, 11.69] |
| 6 to 5 | 16 | 4.66 µV | 4.04 | 1.01 | [-4.08, 10.24] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 800.36, BIC = 822.11
- **3 to 2 vs 2 to 1**: *β* = -3.15, *SE* = 2.180, *z* = -1.445, *p* = 0.149
- **4 to 3 vs 2 to 1**: *β* = -2.72, *SE* = 2.198, *z* = -1.238, *p* = 0.216
- **5 to 4 vs 2 to 1**: *β* = -2.28, *SE* = 2.183, *z* = -1.045, *p* = 0.296
- **6 to 5 vs 2 to 1**: *β* = -2.60, *SE* = 2.477, *z* = -1.051, *p* = 0.293
- **SNR**: *β* = 0.21, *SE* = 0.545, *z* = 0.394, *p* = 0.694

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.15 | 2.18 | 1.44 | 0.149 | 0.800 | n.s. |
| 2 to 1 - 4 to 3 | 2.72 | 2.20 | 1.24 | 0.216 | 0.888 | n.s. |
| 2 to 1 - 5 to 4 | 2.28 | 2.18 | 1.04 | 0.296 | 0.938 | n.s. |
| 2 to 1 - 6 to 5 | 2.60 | 2.48 | 1.05 | 0.293 | 0.938 | n.s. |
| 3 to 2 - 4 to 3 | -0.43 | 2.19 | -0.20 | 0.845 | 1.000 | n.s. |
| 3 to 2 - 5 to 4 | -0.87 | 2.18 | -0.40 | 0.691 | 0.999 | n.s. |
| 3 to 2 - 6 to 5 | -0.55 | 2.47 | -0.22 | 0.825 | 1.000 | n.s. |
| 4 to 3 - 5 to 4 | -0.44 | 2.18 | -0.20 | 0.840 | 1.000 | n.s. |
| 4 to 3 - 6 to 5 | -0.12 | 2.46 | -0.05 | 0.962 | 1.000 | n.s. |
| 5 to 4 - 6 to 5 | 0.32 | 2.47 | 0.13 | 0.896 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.25, *p* = 0.298, η²_G = 0.048
- Greenhouse-Geisser corrected: *p* = 0.302 (ε = 0.673)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.03 | 15 | = 0.764 | 0.41 [-0.19, 0.66] | small | n.s. |
| 2 to 1 vs 4 to 3 | 1.35 | 15 | = 0.695 | 0.50 [-0.19, 0.67] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 2.20 | 15 | = 0.439 | 0.72 [-0.22, 0.63] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 1.31 | 15 | = 0.695 | 0.52 [-0.22, 0.88] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.43 | 15 | = 0.845 | 0.08 [-0.46, 0.38] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.90 | 15 | = 0.764 | 0.23 [-0.50, 0.35] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.27 | 15 | = 0.877 | 0.08 [-0.47, 0.60] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 0.63 | 15 | = 0.771 | 0.15 [-0.49, 0.36] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.00 | 15 | = 1.000 | 0.00 [-0.53, 0.53] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.72 | 15 | = 0.771 | -0.15 [-0.72, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 523.97, BIC = 545.72
- **3 to 2 vs 2 to 1**: *β* = 0.36, *SE* = 0.647, *z* = 0.562, *p* = 0.574
- **4 to 3 vs 2 to 1**: *β* = 0.81, *SE* = 0.652, *z* = 1.242, *p* = 0.214
- **5 to 4 vs 2 to 1**: *β* = -0.11, *SE* = 0.648, *z* = -0.171, *p* = 0.864
- **6 to 5 vs 2 to 1**: *β* = 0.93, *SE* = 0.733, *z* = 1.271, *p* = 0.204
- **SNR**: *β* = -0.33, *SE* = 0.160, *z* = -2.071, *p* = 0.038

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.36 | 0.65 | -0.56 | 0.574 | 0.968 | n.s. |
| 2 to 1 - 4 to 3 | -0.81 | 0.65 | -1.24 | 0.214 | 0.838 | n.s. |
| 2 to 1 - 5 to 4 | 0.11 | 0.65 | 0.17 | 0.864 | 0.981 | n.s. |
| 2 to 1 - 6 to 5 | -0.93 | 0.73 | -1.27 | 0.204 | 0.838 | n.s. |
| 3 to 2 - 4 to 3 | -0.45 | 0.65 | -0.69 | 0.493 | 0.968 | n.s. |
| 3 to 2 - 5 to 4 | 0.47 | 0.65 | 0.73 | 0.463 | 0.968 | n.s. |
| 3 to 2 - 6 to 5 | -0.57 | 0.73 | -0.78 | 0.438 | 0.968 | n.s. |
| 4 to 3 - 5 to 4 | 0.92 | 0.65 | 1.42 | 0.155 | 0.810 | n.s. |
| 4 to 3 - 6 to 5 | -0.12 | 0.73 | -0.17 | 0.868 | 0.981 | n.s. |
| 5 to 4 - 6 to 5 | -1.04 | 0.73 | -1.43 | 0.153 | 0.810 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.24, *p* = 0.305, η²_G = 0.061
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.62 | 15 | = 0.682 | -0.26 [-0.53, 0.31] | small | n.s. |
| 2 to 1 vs 4 to 3 | -2.04 | 15 | = 0.523 | -0.78 [-0.77, 0.10] | medium | n.s. |
| 2 to 1 vs 5 to 4 | -0.88 | 15 | = 0.657 | -0.35 [-0.41, 0.43] | small | n.s. |
| 2 to 1 vs 6 to 5 | -1.54 | 15 | = 0.523 | -0.55 [-0.94, 0.17] | medium | n.s. |
| 3 to 2 vs 4 to 3 | -1.49 | 15 | = 0.523 | -0.45 [-0.68, 0.18] | small | n.s. |
| 3 to 2 vs 5 to 4 | -0.20 | 15 | = 0.847 | -0.06 [-0.30, 0.55] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -1.02 | 15 | = 0.652 | -0.30 [-0.80, 0.29] | small | n.s. |
| 4 to 3 vs 5 to 4 | 1.26 | 15 | = 0.568 | 0.44 [-0.09, 0.78] | small | n.s. |
| 4 to 3 vs 6 to 5 | 0.21 | 15 | = 0.847 | 0.08 [-0.48, 0.59] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.73 | 15 | = 0.679 | -0.27 [-0.72, 0.35] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 967.28, BIC = 989.02
- **3 to 2 vs 2 to 1**: *β* = -5.71, *SE* = 4.168, *z* = -1.370, *p* = 0.171
- **4 to 3 vs 2 to 1**: *β* = -6.89, *SE* = 4.204, *z* = -1.638, *p* = 0.101
- **5 to 4 vs 2 to 1**: *β* = -2.89, *SE* = 4.166, *z* = -0.693, *p* = 0.488
- **6 to 5 vs 2 to 1**: *β* = -2.86, *SE* = 4.651, *z* = -0.615, *p* = 0.538
- **SNR**: *β* = -0.67, *SE* = 0.636, *z* = -1.049, *p* = 0.294

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 5.71 | 4.17 | 1.37 | 0.171 | 0.814 | n.s. |
| 2 to 1 - 4 to 3 | 6.89 | 4.20 | 1.64 | 0.101 | 0.656 | n.s. |
| 2 to 1 - 5 to 4 | 2.89 | 4.17 | 0.69 | 0.488 | 0.982 | n.s. |
| 2 to 1 - 6 to 5 | 2.86 | 4.65 | 0.62 | 0.538 | 0.982 | n.s. |
| 3 to 2 - 4 to 3 | 1.18 | 4.07 | 0.29 | 0.773 | 0.982 | n.s. |
| 3 to 2 - 5 to 4 | -2.82 | 4.07 | -0.69 | 0.488 | 0.982 | n.s. |
| 3 to 2 - 6 to 5 | -2.85 | 4.67 | -0.61 | 0.542 | 0.982 | n.s. |
| 4 to 3 - 5 to 4 | -4.00 | 4.07 | -0.98 | 0.326 | 0.957 | n.s. |
| 4 to 3 - 6 to 5 | -4.02 | 4.69 | -0.86 | 0.391 | 0.969 | n.s. |
| 5 to 4 - 6 to 5 | -0.03 | 4.67 | -0.01 | 0.996 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.385, η²_G = 0.028
- Greenhouse-Geisser corrected: *p* = 0.358 (ε = 0.486)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.52 | 15 | = 0.869 | 0.14 [-0.11, 0.76] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 3.57 | 15 | = 0.028 | 0.65 [0.17, 1.10] | medium | * |
| 2 to 1 vs 5 to 4 | 0.85 | 15 | = 0.815 | 0.21 [-0.22, 0.64] | small | n.s. |
| 2 to 1 vs 6 to 5 | 0.70 | 15 | = 0.826 | 0.16 [-0.36, 0.71] | negligible | n.s. |
| 3 to 2 vs 4 to 3 | 1.30 | 15 | = 0.531 | 0.37 [-0.37, 0.48] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.19 | 15 | = 0.948 | 0.06 [-0.53, 0.32] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.06 | 15 | = 0.949 | 0.02 [-0.52, 0.55] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -1.73 | 15 | = 0.348 | -0.29 [-0.70, 0.16] | small | n.s. |
| 4 to 3 vs 6 to 5 | -1.87 | 15 | = 0.348 | -0.35 [-1.03, 0.09] | small | n.s. |
| 5 to 4 vs 6 to 5 | -0.26 | 15 | = 0.948 | -0.04 [-0.60, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 517.92, BIC = 539.67
- **3 to 2 vs 2 to 1**: *β* = -1.64, *SE* = 0.600, *z* = -2.738, *p* = 0.006
- **4 to 3 vs 2 to 1**: *β* = -1.61, *SE* = 0.605, *z* = -2.654, *p* = 0.008
- **5 to 4 vs 2 to 1**: *β* = -1.58, *SE* = 0.600, *z* = -2.629, *p* = 0.009
- **6 to 5 vs 2 to 1**: *β* = -3.54, *SE* = 0.668, *z* = -5.308, *p* < .001
- **SNR**: *β* = -0.50, *SE* = 0.088, *z* = -5.732, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 1.64 | 0.60 | 2.74 | 0.006 | 0.037 | * |
| 2 to 1 - 4 to 3 | 1.61 | 0.61 | 2.65 | 0.008 | 0.039 | * |
| 2 to 1 - 5 to 4 | 1.58 | 0.60 | 2.63 | 0.009 | 0.039 | * |
| 2 to 1 - 6 to 5 | 3.54 | 0.67 | 5.31 | < .001 | < .001 | *** |
| 3 to 2 - 4 to 3 | -0.04 | 0.59 | -0.06 | 0.949 | 0.999 | n.s. |
| 3 to 2 - 5 to 4 | -0.07 | 0.59 | -0.11 | 0.911 | 0.999 | n.s. |
| 3 to 2 - 6 to 5 | 1.90 | 0.67 | 2.83 | 0.005 | 0.032 | * |
| 4 to 3 - 5 to 4 | -0.03 | 0.59 | -0.05 | 0.962 | 0.999 | n.s. |
| 4 to 3 - 6 to 5 | 1.94 | 0.67 | 2.88 | 0.004 | 0.032 | * |
| 5 to 4 - 6 to 5 | 1.97 | 0.67 | 2.93 | 0.003 | 0.030 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.00, *p* < .001, η²_G = 0.185
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.85 | 15 | = 0.030 | 0.72 [0.33, 1.30] | medium | * |
| 2 to 1 vs 4 to 3 | 3.52 | 15 | = 0.015 | 1.05 [0.14, 1.05] | large | * |
| 2 to 1 vs 5 to 4 | 2.58 | 15 | = 0.042 | 0.79 [0.17, 1.09] | medium | * |
| 2 to 1 vs 6 to 5 | 5.25 | 15 | < .001 | 1.52 [0.59, 2.04] | large | *** |
| 3 to 2 vs 4 to 3 | 0.86 | 15 | = 0.504 | 0.27 [-0.40, 0.45] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.58 | 15 | = 0.631 | 0.13 [-0.45, 0.40] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 3.14 | 15 | = 0.022 | 0.73 [0.18, 1.40] | medium | * |
| 4 to 3 vs 5 to 4 | -0.35 | 15 | = 0.728 | -0.10 [-0.47, 0.38] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.94 | 15 | = 0.120 | 0.50 [-0.08, 1.05] | medium | n.s. |
| 5 to 4 vs 6 to 5 | 1.81 | 15 | = 0.129 | 0.51 [-0.11, 1.01] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 782.28, BIC = 804.03
- **3 to 2 vs 2 to 1**: *β* = -3.32, *SE* = 1.946, *z* = -1.706, *p* = 0.088
- **4 to 3 vs 2 to 1**: *β* = -4.70, *SE* = 1.929, *z* = -2.436, *p* = 0.015
- **5 to 4 vs 2 to 1**: *β* = -4.53, *SE* = 1.928, *z* = -2.351, *p* = 0.019
- **6 to 5 vs 2 to 1**: *β* = -5.01, *SE* = 2.213, *z* = -2.263, *p* = 0.024
- **SNR**: *β* = 0.26, *SE* = 0.387, *z* = 0.665, *p* = 0.506

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.32 | 1.95 | 1.71 | 0.088 | 0.476 | n.s. |
| 2 to 1 - 4 to 3 | 4.70 | 1.93 | 2.44 | 0.015 | 0.139 | n.s. |
| 2 to 1 - 5 to 4 | 4.53 | 1.93 | 2.35 | 0.019 | 0.156 | n.s. |
| 2 to 1 - 6 to 5 | 5.01 | 2.21 | 2.26 | 0.024 | 0.174 | n.s. |
| 3 to 2 - 4 to 3 | 1.38 | 1.88 | 0.73 | 0.462 | 0.965 | n.s. |
| 3 to 2 - 5 to 4 | 1.21 | 1.88 | 0.65 | 0.518 | 0.965 | n.s. |
| 3 to 2 - 6 to 5 | 1.69 | 2.13 | 0.79 | 0.429 | 0.965 | n.s. |
| 4 to 3 - 5 to 4 | -0.16 | 1.88 | -0.09 | 0.930 | 0.995 | n.s. |
| 4 to 3 - 6 to 5 | 0.31 | 2.14 | 0.14 | 0.885 | 0.995 | n.s. |
| 5 to 4 - 6 to 5 | 0.47 | 2.14 | 0.22 | 0.825 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.60, *p* = 0.045, η²_G = 0.074
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.62 | 15 | = 0.318 | 0.51 [-0.01, 0.87] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 2.03 | 15 | = 0.200 | 0.69 [-0.01, 0.87] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 2.57 | 15 | = 0.107 | 0.79 [0.03, 0.92] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 2.90 | 15 | = 0.107 | 0.80 [0.13, 1.33] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.77 | 15 | = 0.649 | 0.19 [-0.29, 0.56] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 1.04 | 15 | = 0.634 | 0.24 [-0.30, 0.55] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.78 | 15 | = 0.649 | 0.24 [-0.34, 0.73] | small | n.s. |
| 4 to 3 vs 5 to 4 | 0.11 | 15 | = 1.000 | 0.03 [-0.44, 0.40] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.13 | 15 | = 1.000 | 0.03 [-0.50, 0.56] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 0.00 | 15 | = 1.000 | 0.00 [-0.53, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 507.20, BIC = 528.95
- **3 to 2 vs 2 to 1**: *β* = -2.33, *SE* = 0.573, *z* = -4.063, *p* < .001
- **4 to 3 vs 2 to 1**: *β* = -2.21, *SE* = 0.567, *z* = -3.903, *p* < .001
- **5 to 4 vs 2 to 1**: *β* = -1.50, *SE* = 0.567, *z* = -2.648, *p* = 0.008
- **6 to 5 vs 2 to 1**: *β* = -2.20, *SE* = 0.651, *z* = -3.385, *p* = 0.001
- **SNR**: *β* = 0.29, *SE* = 0.120, *z* = 2.386, *p* = 0.017

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 2.33 | 0.57 | 4.06 | < .001 | < .001 | *** |
| 2 to 1 - 4 to 3 | 2.21 | 0.57 | 3.90 | < .001 | < .001 | *** |
| 2 to 1 - 5 to 4 | 1.50 | 0.57 | 2.65 | 0.008 | 0.055 | n.s. |
| 2 to 1 - 6 to 5 | 2.20 | 0.65 | 3.38 | < .001 | 0.006 | ** |
| 3 to 2 - 4 to 3 | -0.11 | 0.55 | -0.21 | 0.836 | 0.996 | n.s. |
| 3 to 2 - 5 to 4 | -0.83 | 0.55 | -1.50 | 0.133 | 0.576 | n.s. |
| 3 to 2 - 6 to 5 | -0.13 | 0.63 | -0.20 | 0.841 | 0.996 | n.s. |
| 4 to 3 - 5 to 4 | -0.71 | 0.55 | -1.30 | 0.195 | 0.662 | n.s. |
| 4 to 3 - 6 to 5 | -0.01 | 0.63 | -0.02 | 0.985 | 0.996 | n.s. |
| 5 to 4 - 6 to 5 | 0.70 | 0.63 | 1.12 | 0.263 | 0.705 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.71, *p* < .001, η²_G = 0.166
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 4.18 | 15 | = 0.003 | 1.22 [0.35, 1.33] | large | ** |
| 2 to 1 vs 4 to 3 | 4.36 | 15 | = 0.003 | 1.12 [0.38, 1.38] | large | ** |
| 2 to 1 vs 5 to 4 | 3.10 | 15 | = 0.018 | 0.91 [0.15, 1.07] | large | * |
| 2 to 1 vs 6 to 5 | 4.10 | 15 | = 0.003 | 1.11 [0.37, 1.68] | large | ** |
| 3 to 2 vs 4 to 3 | -0.43 | 15 | = 0.838 | -0.10 [-0.51, 0.34] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.81 | 15 | = 0.838 | -0.22 [-0.74, 0.12] | small | n.s. |
| 3 to 2 vs 6 to 5 | -0.17 | 15 | = 0.871 | -0.03 [-0.57, 0.49] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -0.46 | 15 | = 0.838 | -0.12 [-0.70, 0.16] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.26 | 15 | = 0.871 | 0.06 [-0.47, 0.60] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 0.57 | 15 | = 0.838 | 0.17 [-0.39, 0.68] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1124.52, BIC = 1146.27
- **3 to 2 vs 2 to 1**: *β* = -15.42, *SE* = 8.774, *z* = -1.758, *p* = 0.079
- **4 to 3 vs 2 to 1**: *β* = -23.59, *SE* = 8.744, *z* = -2.698, *p* = 0.007
- **5 to 4 vs 2 to 1**: *β* = -6.11, *SE* = 8.740, *z* = -0.699, *p* = 0.485
- **6 to 5 vs 2 to 1**: *β* = 6.82, *SE* = 10.013, *z* = 0.681, *p* = 0.496
- **SNR**: *β* = -1.59, *SE* = 0.972, *z* = -1.632, *p* = 0.103

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 15.42 | 8.77 | 1.76 | 0.079 | 0.389 | n.s. |
| 2 to 1 - 4 to 3 | 23.59 | 8.74 | 2.70 | 0.007 | 0.061 | n.s. |
| 2 to 1 - 5 to 4 | 6.11 | 8.74 | 0.70 | 0.485 | 0.744 | n.s. |
| 2 to 1 - 6 to 5 | -6.82 | 10.01 | -0.68 | 0.496 | 0.744 | n.s. |
| 3 to 2 - 4 to 3 | 8.17 | 8.80 | 0.93 | 0.353 | 0.744 | n.s. |
| 3 to 2 - 5 to 4 | -9.32 | 8.78 | -1.06 | 0.288 | 0.744 | n.s. |
| 3 to 2 - 6 to 5 | -22.25 | 9.94 | -2.24 | 0.025 | 0.185 | n.s. |
| 4 to 3 - 5 to 4 | -17.49 | 8.74 | -2.00 | 0.046 | 0.278 | n.s. |
| 4 to 3 - 6 to 5 | -30.41 | 10.05 | -3.03 | 0.002 | 0.024 | * |
| 5 to 4 - 6 to 5 | -12.93 | 10.02 | -1.29 | 0.197 | 0.666 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.20, *p* = 0.080, η²_G = 0.081
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.81 | 15 | = 0.478 | 0.26 [-0.11, 0.76] | small | n.s. |
| 2 to 1 vs 4 to 3 | 1.73 | 15 | = 0.310 | 0.53 [0.16, 1.09] | medium | n.s. |
| 2 to 1 vs 5 to 4 | -0.04 | 15 | = 0.970 | -0.01 [-0.31, 0.54] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | -1.32 | 15 | = 0.410 | -0.35 [-0.88, 0.22] | small | n.s. |
| 3 to 2 vs 4 to 3 | 0.92 | 15 | = 0.476 | 0.26 [-0.16, 0.70] | small | n.s. |
| 3 to 2 vs 5 to 4 | -0.90 | 15 | = 0.476 | -0.27 [-0.61, 0.25] | small | n.s. |
| 3 to 2 vs 6 to 5 | -1.63 | 15 | = 0.310 | -0.56 [-0.96, 0.15] | medium | n.s. |
| 4 to 3 vs 5 to 4 | -1.66 | 15 | = 0.310 | -0.54 [-0.87, 0.01] | medium | n.s. |
| 4 to 3 vs 6 to 5 | -3.17 | 15 | = 0.064 | -0.80 [-1.40, -0.18] | large | n.s. |
| 5 to 4 vs 6 to 5 | -1.13 | 15 | = 0.458 | -0.33 [-0.83, 0.26] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 570.55, BIC = 592.30
- **3 to 2 vs 2 to 1**: *β* = 0.18, *SE* = 0.675, *z* = 0.264, *p* = 0.792
- **4 to 3 vs 2 to 1**: *β* = -0.62, *SE* = 0.672, *z* = -0.928, *p* = 0.354
- **5 to 4 vs 2 to 1**: *β* = -0.32, *SE* = 0.672, *z* = -0.476, *p* = 0.634
- **6 to 5 vs 2 to 1**: *β* = -0.90, *SE* = 0.777, *z* = -1.156, *p* = 0.248
- **SNR**: *β* = 0.32, *SE* = 0.078, *z* = 4.147, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.18 | 0.67 | -0.26 | 0.792 | 0.982 | n.s. |
| 2 to 1 - 4 to 3 | 0.62 | 0.67 | 0.93 | 0.354 | 0.953 | n.s. |
| 2 to 1 - 5 to 4 | 0.32 | 0.67 | 0.48 | 0.634 | 0.982 | n.s. |
| 2 to 1 - 6 to 5 | 0.90 | 0.78 | 1.16 | 0.248 | 0.912 | n.s. |
| 3 to 2 - 4 to 3 | 0.80 | 0.68 | 1.18 | 0.236 | 0.912 | n.s. |
| 3 to 2 - 5 to 4 | 0.50 | 0.68 | 0.74 | 0.460 | 0.974 | n.s. |
| 3 to 2 - 6 to 5 | 1.08 | 0.77 | 1.40 | 0.162 | 0.829 | n.s. |
| 4 to 3 - 5 to 4 | -0.30 | 0.67 | -0.45 | 0.652 | 0.982 | n.s. |
| 4 to 3 - 6 to 5 | 0.27 | 0.78 | 0.35 | 0.725 | 0.982 | n.s. |
| 5 to 4 - 6 to 5 | 0.58 | 0.78 | 0.74 | 0.457 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.463, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.17 | 15 | = 0.866 | -0.04 [-0.40, 0.44] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 0.57 | 15 | = 0.866 | 0.13 [-0.26, 0.59] | negligible | n.s. |
| 2 to 1 vs 5 to 4 | 0.32 | 15 | = 0.866 | 0.08 [-0.35, 0.50] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 1.96 | 15 | = 0.694 | 0.36 [-0.07, 1.05] | small | n.s. |
| 3 to 2 vs 4 to 3 | 0.87 | 15 | = 0.800 | 0.16 [-0.27, 0.58] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.48 | 15 | = 0.866 | 0.11 [-0.36, 0.48] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 1.39 | 15 | = 0.762 | 0.38 [-0.20, 0.90] | small | n.s. |
| 4 to 3 vs 5 to 4 | -0.28 | 15 | = 0.866 | -0.06 [-0.49, 0.35] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.87 | 15 | = 0.800 | 0.22 [-0.32, 0.76] | small | n.s. |
| 5 to 4 vs 6 to 5 | 1.26 | 15 | = 0.762 | 0.29 [-0.23, 0.86] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 0.72)
  - 2 to 1 showed greater amplitude than 4 to 3 (*d* = 1.05)
  - 2 to 1 showed greater amplitude than 5 to 4 (*d* = 0.79)
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 1.52)
  - 3 to 2 showed greater amplitude than 6 to 5 (*d* = 0.73)
**P1 latency:** Significant main effect of condition (*p* = 0.045) (no significant pairwise comparisons)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 1.22)
  - 2 to 1 showed greater amplitude than 4 to 3 (*d* = 1.12)
  - 2 to 1 showed greater amplitude than 5 to 4 (*d* = 0.91)
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 1.11)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.080)

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
