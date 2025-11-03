# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:48:03

---

## 1. Analysis Overview

**Total Measurements:** 480
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
| 2 to 5 | 11 | 99.64 ms | 8.48 | 2.56 | [88.00, 108.00] |
| 3 to 5 | 17 | 103.53 ms | 7.73 | 1.87 | [88.00, 112.00] |
| 4 to 5 | 14 | 101.43 ms | 8.39 | 2.24 | [88.00, 112.00] |
| 6 to 5 | 11 | 101.09 ms | 6.47 | 1.95 | [88.00, 112.00] |
| Cardinality5 | 15 | 99.20 ms | 9.94 | 2.57 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 11 | -2.13 µV | 2.97 | 0.90 | [-10.84, -0.71] |
| 3 to 5 | 17 | -2.69 µV | 1.28 | 0.31 | [-4.95, -0.87] |
| 4 to 5 | 14 | -3.65 µV | 2.78 | 0.74 | [-10.33, -1.15] |
| 6 to 5 | 11 | -3.17 µV | 2.16 | 0.65 | [-8.14, -0.31] |
| Cardinality5 | 15 | -3.07 µV | 2.07 | 0.54 | [-7.37, -0.36] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 169.67 ms | 21.39 | 4.37 | [132.00, 204.00] |
| 3 to 5 | 22 | 163.64 ms | 21.48 | 4.58 | [132.00, 204.00] |
| 4 to 5 | 23 | 166.43 ms | 19.81 | 4.13 | [132.00, 204.00] |
| 6 to 5 | 24 | 171.83 ms | 20.92 | 4.27 | [132.00, 204.00] |
| Cardinality5 | 23 | 170.26 ms | 17.88 | 3.73 | [132.00, 196.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | -6.05 µV | 2.54 | 0.52 | [-13.83, -1.66] |
| 3 to 5 | 22 | -5.65 µV | 2.41 | 0.51 | [-11.97, -1.70] |
| 4 to 5 | 23 | -5.80 µV | 2.72 | 0.57 | [-11.05, -1.20] |
| 6 to 5 | 24 | -5.93 µV | 2.12 | 0.43 | [-10.60, -2.05] |
| Cardinality5 | 23 | -6.21 µV | 2.46 | 0.51 | [-12.06, -1.67] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 13 | 94.77 ms | 10.38 | 2.88 | [84.00, 108.00] |
| 3 to 5 | 15 | 99.73 ms | 8.75 | 2.26 | [84.00, 108.00] |
| 4 to 5 | 14 | 101.14 ms | 7.91 | 2.11 | [84.00, 108.00] |
| 6 to 5 | 14 | 97.43 ms | 8.96 | 2.39 | [84.00, 108.00] |
| Cardinality5 | 13 | 100.00 ms | 9.52 | 2.64 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 13 | 2.83 µV | 2.81 | 0.78 | [0.58, 10.47] |
| 3 to 5 | 15 | 2.94 µV | 1.39 | 0.36 | [1.48, 5.64] |
| 4 to 5 | 14 | 3.75 µV | 3.18 | 0.85 | [1.14, 13.41] |
| 6 to 5 | 14 | 3.07 µV | 2.38 | 0.64 | [0.33, 9.47] |
| Cardinality5 | 13 | 2.76 µV | 1.60 | 0.44 | [0.35, 5.37] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 22 | 440.73 ms | 48.52 | 10.34 | [368.00, 536.00] |
| 3 to 5 | 16 | 466.75 ms | 56.70 | 14.17 | [376.00, 540.00] |
| 4 to 5 | 16 | 496.00 ms | 36.98 | 9.24 | [436.00, 540.00] |
| 6 to 5 | 12 | 479.67 ms | 62.05 | 17.91 | [360.00, 540.00] |
| Cardinality5 | 12 | 448.00 ms | 65.84 | 19.01 | [356.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 22 | 5.66 µV | 2.60 | 0.56 | [2.17, 11.71] |
| 3 to 5 | 16 | 6.54 µV | 3.12 | 0.78 | [3.40, 15.40] |
| 4 to 5 | 16 | 6.02 µV | 3.97 | 0.99 | [1.66, 16.10] |
| 6 to 5 | 12 | 4.88 µV | 2.51 | 0.73 | [2.36, 10.64] |
| Cardinality5 | 12 | 3.73 µV | 1.24 | 0.36 | [1.49, 5.39] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 487.79, BIC = 505.54
- **3 to 5 vs 2 to 5**: *β* = 3.56, *SE* = 2.832, *z* = 1.256, *p* = 0.209
- **4 to 5 vs 2 to 5**: *β* = 0.81, *SE* = 3.001, *z* = 0.271, *p* = 0.787
- **6 to 5 vs 2 to 5**: *β* = 1.72, *SE* = 3.152, *z* = 0.545, *p* = 0.586
- **Cardinality5 vs 2 to 5**: *β* = -0.59, *SE* = 2.899, *z* = -0.205, *p* = 0.837
- **SNR**: *β* = 0.33, *SE* = 0.324, *z* = 1.021, *p* = 0.307

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -3.56 | 2.83 | -1.26 | 0.209 | 0.879 | n.s. |
| 2 to 5 - 4 to 5 | -0.81 | 3.00 | -0.27 | 0.787 | 0.988 | n.s. |
| 2 to 5 - 6 to 5 | -1.72 | 3.15 | -0.54 | 0.586 | 0.988 | n.s. |
| 2 to 5 - Cardinality5 | 0.60 | 2.90 | 0.21 | 0.837 | 0.988 | n.s. |
| 3 to 5 - 4 to 5 | 2.74 | 2.64 | 1.04 | 0.299 | 0.942 | n.s. |
| 3 to 5 - 6 to 5 | 1.84 | 2.89 | 0.64 | 0.524 | 0.988 | n.s. |
| 3 to 5 - Cardinality5 | 4.15 | 2.59 | 1.61 | 0.108 | 0.682 | n.s. |
| 4 to 5 - 6 to 5 | -0.90 | 3.06 | -0.30 | 0.768 | 0.988 | n.s. |
| 4 to 5 - Cardinality5 | 1.41 | 2.81 | 0.50 | 0.617 | 0.988 | n.s. |
| 6 to 5 - Cardinality5 | 2.31 | 2.92 | 0.79 | 0.428 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.400, η²_G = 0.136
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.22 | 3 | = 0.624 | -0.50 [-0.95, 0.60] | medium | n.s. |
| 2 to 5 vs 4 to 5 | -1.21 | 3 | = 0.624 | -0.67 [-1.15, 0.72] | medium | n.s. |
| 2 to 5 vs 6 to 5 | -0.42 | 3 | = 0.781 | -0.26 [-1.48, 0.70] | small | n.s. |
| 2 to 5 vs Cardinality5 | -2.32 | 3 | = 0.624 | -0.77 [-0.70, 0.84] | medium | n.s. |
| 3 to 5 vs 4 to 5 | -0.29 | 3 | = 0.789 | -0.21 [-0.39, 0.99] | small | n.s. |
| 3 to 5 vs 6 to 5 | 0.58 | 3 | = 0.781 | 0.37 [-0.96, 0.72] | small | n.s. |
| 3 to 5 vs Cardinality5 | -0.77 | 3 | = 0.781 | -0.37 [-0.24, 1.01] | small | n.s. |
| 4 to 5 vs 6 to 5 | 1.57 | 3 | = 0.624 | 0.66 [-1.15, 0.72] | medium | n.s. |
| 4 to 5 vs Cardinality5 | -0.52 | 3 | = 0.781 | -0.22 [-1.40, 0.53] | small | n.s. |
| 6 to 5 vs Cardinality5 | -1.22 | 3 | = 0.624 | -0.77 [-0.84, 0.84] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 244.12, BIC = 261.88
- **3 to 5 vs 2 to 5**: *β* = -0.54, *SE* = 0.451, *z* = -1.190, *p* = 0.234
- **4 to 5 vs 2 to 5**: *β* = -1.07, *SE* = 0.477, *z* = -2.238, *p* = 0.025
- **6 to 5 vs 2 to 5**: *β* = -0.92, *SE* = 0.503, *z* = -1.828, *p* = 0.068
- **Cardinality5 vs 2 to 5**: *β* = -0.72, *SE* = 0.462, *z* = -1.549, *p* = 0.121
- **SNR**: *β* = -0.47, *SE* = 0.053, *z* = -8.849, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.54 | 0.45 | 1.19 | 0.234 | 0.802 | n.s. |
| 2 to 5 - 4 to 5 | 1.07 | 0.48 | 2.24 | 0.025 | 0.225 | n.s. |
| 2 to 5 - 6 to 5 | 0.92 | 0.50 | 1.83 | 0.068 | 0.467 | n.s. |
| 2 to 5 - Cardinality5 | 0.72 | 0.46 | 1.55 | 0.121 | 0.645 | n.s. |
| 3 to 5 - 4 to 5 | 0.53 | 0.42 | 1.26 | 0.207 | 0.802 | n.s. |
| 3 to 5 - 6 to 5 | 0.38 | 0.46 | 0.84 | 0.401 | 0.923 | n.s. |
| 3 to 5 - Cardinality5 | 0.18 | 0.41 | 0.44 | 0.660 | 0.961 | n.s. |
| 4 to 5 - 6 to 5 | -0.15 | 0.48 | -0.31 | 0.755 | 0.961 | n.s. |
| 4 to 5 - Cardinality5 | -0.35 | 0.45 | -0.79 | 0.431 | 0.923 | n.s. |
| 6 to 5 - Cardinality5 | -0.20 | 0.47 | -0.43 | 0.664 | 0.961 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.40, *p* = 0.803, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.13 | 3 | = 0.953 | -0.07 [-0.72, 0.82] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 1.16 | 3 | = 0.953 | 0.28 [-0.34, 1.71] | small | n.s. |
| 2 to 5 vs 6 to 5 | 0.25 | 3 | = 0.953 | 0.06 [-0.69, 1.49] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | 0.53 | 3 | = 0.953 | 0.29 [-0.49, 1.08] | small | n.s. |
| 3 to 5 vs 4 to 5 | 0.88 | 3 | = 0.953 | 0.49 [-0.38, 1.00] | small | n.s. |
| 3 to 5 vs 6 to 5 | 0.47 | 3 | = 0.953 | 0.21 [-0.50, 1.23] | small | n.s. |
| 3 to 5 vs Cardinality5 | 1.92 | 3 | = 0.953 | 0.60 [-0.22, 1.04] | medium | n.s. |
| 4 to 5 vs 6 to 5 | -0.84 | 3 | = 0.953 | -0.28 [-1.15, 0.72] | small | n.s. |
| 4 to 5 vs Cardinality5 | -0.06 | 3 | = 0.953 | -0.04 [-0.74, 1.12] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 0.75 | 3 | = 0.953 | 0.31 [-0.88, 0.79] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 996.15, BIC = 1018.18
- **3 to 5 vs 2 to 5**: *β* = -5.31, *SE* = 4.100, *z* = -1.295, *p* = 0.195
- **4 to 5 vs 2 to 5**: *β* = -2.57, *SE* = 4.026, *z* = -0.639, *p* = 0.523
- **6 to 5 vs 2 to 5**: *β* = 2.10, *SE* = 3.968, *z* = 0.530, *p* = 0.596
- **Cardinality5 vs 2 to 5**: *β* = 1.40, *SE* = 4.032, *z* = 0.346, *p* = 0.729
- **SNR**: *β* = -0.48, *SE* = 0.654, *z* = -0.736, *p* = 0.462

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 5.31 | 4.10 | 1.29 | 0.195 | 0.824 | n.s. |
| 2 to 5 - 4 to 5 | 2.57 | 4.03 | 0.64 | 0.523 | 0.971 | n.s. |
| 2 to 5 - 6 to 5 | -2.10 | 3.97 | -0.53 | 0.596 | 0.971 | n.s. |
| 2 to 5 - Cardinality5 | -1.40 | 4.03 | -0.35 | 0.729 | 0.971 | n.s. |
| 3 to 5 - 4 to 5 | -2.74 | 4.13 | -0.66 | 0.508 | 0.971 | n.s. |
| 3 to 5 - 6 to 5 | -7.41 | 4.09 | -1.81 | 0.070 | 0.517 | n.s. |
| 3 to 5 - Cardinality5 | -6.70 | 4.15 | -1.61 | 0.106 | 0.637 | n.s. |
| 4 to 5 - 6 to 5 | -4.68 | 4.03 | -1.16 | 0.246 | 0.861 | n.s. |
| 4 to 5 - Cardinality5 | -3.97 | 4.06 | -0.98 | 0.328 | 0.908 | n.s. |
| 6 to 5 - Cardinality5 | 0.71 | 4.04 | 0.18 | 0.861 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.89, *p* = 0.474, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.96 | 21 | = 0.747 | 0.21 [-0.24, 0.65] | small | n.s. |
| 2 to 5 vs 4 to 5 | 0.61 | 21 | = 0.747 | 0.09 [-0.31, 0.56] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.68 | 21 | = 0.747 | -0.14 [-0.53, 0.32] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.38 | 21 | = 0.765 | -0.07 [-0.55, 0.32] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.54 | 21 | = 0.747 | -0.12 [-0.56, 0.33] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.48 | 21 | = 0.747 | -0.34 [-0.77, 0.14] | small | n.s. |
| 3 to 5 vs Cardinality5 | -1.97 | 21 | = 0.620 | -0.29 [-0.88, 0.04] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.99 | 21 | = 0.747 | -0.23 [-0.67, 0.21] | small | n.s. |
| 4 to 5 vs Cardinality5 | -0.78 | 21 | = 0.747 | -0.17 [-0.63, 0.24] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 0.30 | 21 | = 0.765 | 0.07 [-0.38, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 458.25, BIC = 480.28
- **3 to 5 vs 2 to 5**: *β* = 0.34, *SE* = 0.399, *z* = 0.846, *p* = 0.398
- **4 to 5 vs 2 to 5**: *β* = 0.27, *SE* = 0.392, *z* = 0.681, *p* = 0.496
- **6 to 5 vs 2 to 5**: *β* = 0.07, *SE* = 0.386, *z* = 0.175, *p* = 0.861
- **Cardinality5 vs 2 to 5**: *β* = -0.04, *SE* = 0.392, *z* = -0.099, *p* = 0.922
- **SNR**: *β* = -0.38, *SE* = 0.064, *z* = -5.928, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.34 | 0.40 | -0.85 | 0.398 | 0.990 | n.s. |
| 2 to 5 - 4 to 5 | -0.27 | 0.39 | -0.68 | 0.496 | 0.992 | n.s. |
| 2 to 5 - 6 to 5 | -0.07 | 0.39 | -0.18 | 0.861 | 0.998 | n.s. |
| 2 to 5 - Cardinality5 | 0.04 | 0.39 | 0.10 | 0.922 | 0.998 | n.s. |
| 3 to 5 - 4 to 5 | 0.07 | 0.40 | 0.18 | 0.861 | 0.998 | n.s. |
| 3 to 5 - 6 to 5 | 0.27 | 0.40 | 0.68 | 0.498 | 0.992 | n.s. |
| 3 to 5 - Cardinality5 | 0.38 | 0.40 | 0.93 | 0.352 | 0.987 | n.s. |
| 4 to 5 - 6 to 5 | 0.20 | 0.39 | 0.51 | 0.611 | 0.992 | n.s. |
| 4 to 5 - Cardinality5 | 0.31 | 0.39 | 0.77 | 0.439 | 0.990 | n.s. |
| 6 to 5 - Cardinality5 | 0.11 | 0.39 | 0.27 | 0.787 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.567, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.27 | 21 | = 0.740 | -0.24 [-0.72, 0.18] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.37 | 21 | = 0.865 | -0.09 [-0.52, 0.35] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.25 | 21 | = 0.865 | -0.05 [-0.48, 0.37] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | 0.39 | 21 | = 0.865 | 0.08 [-0.35, 0.52] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 0.94 | 21 | = 0.740 | 0.14 [-0.25, 0.65] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 1.14 | 21 | = 0.740 | 0.20 [-0.21, 0.69] | small | n.s. |
| 3 to 5 vs Cardinality5 | 1.95 | 21 | = 0.650 | 0.33 [-0.05, 0.88] | small | n.s. |
| 4 to 5 vs 6 to 5 | 0.17 | 21 | = 0.865 | 0.04 [-0.38, 0.48] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 0.78 | 21 | = 0.740 | 0.17 [-0.26, 0.61] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 0.85 | 21 | = 0.740 | 0.15 [-0.27, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 495.33, BIC = 513.21
- **3 to 5 vs 2 to 5**: *β* = 4.40, *SE* = 2.549, *z* = 1.725, *p* = 0.085
- **4 to 5 vs 2 to 5**: *β* = 5.68, *SE* = 2.619, *z* = 2.167, *p* = 0.030
- **6 to 5 vs 2 to 5**: *β* = 2.34, *SE* = 2.586, *z* = 0.906, *p* = 0.365
- **Cardinality5 vs 2 to 5**: *β* = 4.36, *SE* = 2.645, *z* = 1.647, *p* = 0.100
- **SNR**: *β* = 0.62, *SE* = 0.505, *z* = 1.233, *p* = 0.217

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -4.40 | 2.55 | -1.73 | 0.085 | 0.548 | n.s. |
| 2 to 5 - 4 to 5 | -5.68 | 2.62 | -2.17 | 0.030 | 0.264 | n.s. |
| 2 to 5 - 6 to 5 | -2.34 | 2.59 | -0.91 | 0.365 | 0.934 | n.s. |
| 2 to 5 - Cardinality5 | -4.36 | 2.65 | -1.65 | 0.100 | 0.568 | n.s. |
| 3 to 5 - 4 to 5 | -1.28 | 2.52 | -0.51 | 0.612 | 0.941 | n.s. |
| 3 to 5 - 6 to 5 | 2.05 | 2.47 | 0.83 | 0.407 | 0.934 | n.s. |
| 3 to 5 - Cardinality5 | 0.04 | 2.48 | 0.02 | 0.987 | 0.987 | n.s. |
| 4 to 5 - 6 to 5 | 3.33 | 2.55 | 1.31 | 0.191 | 0.773 | n.s. |
| 4 to 5 - Cardinality5 | 1.32 | 2.62 | 0.50 | 0.614 | 0.941 | n.s. |
| 6 to 5 - Cardinality5 | -2.01 | 2.56 | -0.79 | 0.431 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.32, *p* = 0.859, η²_G = 0.064
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.00 | 4 | = 1.000 | 0.00 [-1.11, 0.37] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 0.36 | 4 | = 1.000 | 0.19 [-1.12, 0.46] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 0.00 | 4 | = 1.000 | 0.00 [-1.19, 0.40] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -1.09 | 4 | = 0.935 | -0.76 [-1.87, -0.02] | medium | n.s. |
| 3 to 5 vs 4 to 5 | 0.25 | 4 | = 1.000 | 0.18 [-0.88, 0.66] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 0.00 | 4 | = 1.000 | 0.00 [-0.50, 0.94] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | -1.00 | 4 | = 0.935 | -0.63 [-0.67, 0.67] | medium | n.s. |
| 4 to 5 vs 6 to 5 | -0.27 | 4 | = 1.000 | -0.19 [-0.60, 0.95] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | -1.00 | 4 | = 0.935 | -0.64 [-0.94, 0.74] | medium | n.s. |
| 6 to 5 vs Cardinality5 | -1.37 | 4 | = 0.935 | -0.76 [-1.03, 0.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 262.02, BIC = 279.90
- **3 to 5 vs 2 to 5**: *β* = -0.21, *SE* = 0.483, *z* = -0.441, *p* = 0.659
- **4 to 5 vs 2 to 5**: *β* = 0.79, *SE* = 0.496, *z* = 1.597, *p* = 0.110
- **6 to 5 vs 2 to 5**: *β* = 0.20, *SE* = 0.490, *z* = 0.398, *p* = 0.690
- **Cardinality5 vs 2 to 5**: *β* = -0.26, *SE* = 0.504, *z* = -0.517, *p* = 0.605
- **SNR**: *β* = 0.81, *SE* = 0.095, *z* = 8.546, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.21 | 0.48 | 0.44 | 0.659 | 0.976 | n.s. |
| 2 to 5 - 4 to 5 | -0.79 | 0.50 | -1.60 | 0.110 | 0.607 | n.s. |
| 2 to 5 - 6 to 5 | -0.20 | 0.49 | -0.40 | 0.690 | 0.976 | n.s. |
| 2 to 5 - Cardinality5 | 0.26 | 0.50 | 0.52 | 0.605 | 0.976 | n.s. |
| 3 to 5 - 4 to 5 | -1.00 | 0.48 | -2.11 | 0.035 | 0.286 | n.s. |
| 3 to 5 - 6 to 5 | -0.41 | 0.47 | -0.87 | 0.383 | 0.922 | n.s. |
| 3 to 5 - Cardinality5 | 0.05 | 0.47 | 0.10 | 0.919 | 0.976 | n.s. |
| 4 to 5 - 6 to 5 | 0.60 | 0.48 | 1.24 | 0.215 | 0.816 | n.s. |
| 4 to 5 - Cardinality5 | 1.05 | 0.49 | 2.13 | 0.033 | 0.286 | n.s. |
| 6 to 5 - Cardinality5 | 0.46 | 0.48 | 0.94 | 0.347 | 0.922 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.05, *p* = 0.995, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.24 | 4 | = 0.957 | 0.11 [-0.88, 0.56] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 0.23 | 4 | = 0.957 | 0.06 [-1.18, 0.41] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 0.56 | 4 | = 0.957 | 0.06 [-0.86, 0.68] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.06 | 4 | = 0.957 | -0.03 [-0.83, 0.71] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.15 | 4 | = 0.957 | -0.06 [-1.19, 0.40] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -0.07 | 4 | = 0.957 | -0.03 [-0.88, 0.56] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | -1.51 | 4 | = 0.957 | -0.23 [-0.34, 1.05] | small | n.s. |
| 4 to 5 vs 6 to 5 | 0.06 | 4 | = 0.957 | 0.01 [-0.70, 0.84] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | -0.27 | 4 | = 0.957 | -0.14 [-0.99, 0.69] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | -0.21 | 4 | = 0.957 | -0.11 [-0.66, 0.78] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 852.02, BIC = 870.87
- **3 to 5 vs 2 to 5**: *β* = 24.93, *SE* = 16.642, *z* = 1.498, *p* = 0.134
- **4 to 5 vs 2 to 5**: *β* = 56.74, *SE* = 16.763, *z* = 3.385, *p* = 0.001
- **6 to 5 vs 2 to 5**: *β* = 40.92, *SE* = 18.355, *z* = 2.229, *p* = 0.026
- **Cardinality5 vs 2 to 5**: *β* = 9.43, *SE* = 18.457, *z* = 0.511, *p* = 0.609
- **SNR**: *β* = 1.61, *SE* = 2.074, *z* = 0.775, *p* = 0.438

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -24.93 | 16.64 | -1.50 | 0.134 | 0.569 | n.s. |
| 2 to 5 - 4 to 5 | -56.74 | 16.76 | -3.38 | < .001 | 0.007 | ** |
| 2 to 5 - 6 to 5 | -40.92 | 18.35 | -2.23 | 0.026 | 0.189 | n.s. |
| 2 to 5 - Cardinality5 | -9.43 | 18.46 | -0.51 | 0.609 | 0.884 | n.s. |
| 3 to 5 - 4 to 5 | -31.80 | 18.15 | -1.75 | 0.080 | 0.441 | n.s. |
| 3 to 5 - 6 to 5 | -15.99 | 19.68 | -0.81 | 0.417 | 0.884 | n.s. |
| 3 to 5 - Cardinality5 | 15.50 | 19.76 | 0.78 | 0.433 | 0.884 | n.s. |
| 4 to 5 - 6 to 5 | 15.82 | 19.44 | 0.81 | 0.416 | 0.884 | n.s. |
| 4 to 5 - Cardinality5 | 47.31 | 19.39 | 2.44 | 0.015 | 0.125 | n.s. |
| 6 to 5 - Cardinality5 | 31.49 | 20.84 | 1.51 | 0.131 | 0.569 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.52, *p* = 0.235, η²_G = 0.186
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.15 | 5 | = 0.570 | -0.15 [-0.95, 0.16] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -2.01 | 5 | = 0.512 | -1.08 [-1.63, -0.29] | large | n.s. |
| 2 to 5 vs 6 to 5 | -1.02 | 5 | = 0.570 | -0.59 [-1.49, 0.03] | medium | n.s. |
| 2 to 5 vs Cardinality5 | 0.17 | 5 | = 0.872 | 0.11 [-0.64, 0.64] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -1.67 | 5 | = 0.512 | -1.02 [-0.82, 0.46] | large | n.s. |
| 3 to 5 vs 6 to 5 | -0.81 | 5 | = 0.570 | -0.48 [-1.21, 0.29] | small | n.s. |
| 3 to 5 vs Cardinality5 | 0.44 | 5 | = 0.750 | 0.28 [-0.74, 0.70] | small | n.s. |
| 4 to 5 vs 6 to 5 | 0.87 | 5 | = 0.570 | 0.47 [-0.32, 1.31] | small | n.s. |
| 4 to 5 vs Cardinality5 | 1.86 | 5 | = 0.512 | 1.25 [-0.08, 1.68] | large | n.s. |
| 6 to 5 vs Cardinality5 | 1.46 | 5 | = 0.512 | 0.72 [-0.44, 1.55] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 353.62, BIC = 372.47
- **3 to 5 vs 2 to 5**: *β* = 0.51, *SE* = 0.573, *z* = 0.881, *p* = 0.378
- **4 to 5 vs 2 to 5**: *β* = 0.74, *SE* = 0.587, *z* = 1.266, *p* = 0.205
- **6 to 5 vs 2 to 5**: *β* = -0.55, *SE* = 0.647, *z* = -0.847, *p* = 0.397
- **Cardinality5 vs 2 to 5**: *β* = -0.67, *SE* = 0.654, *z* = -1.019, *p* = 0.308
- **SNR**: *β* = 0.46, *SE* = 0.079, *z* = 5.758, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.50 | 0.57 | -0.88 | 0.378 | 0.851 | n.s. |
| 2 to 5 - 4 to 5 | -0.74 | 0.59 | -1.27 | 0.205 | 0.748 | n.s. |
| 2 to 5 - 6 to 5 | 0.55 | 0.65 | 0.85 | 0.397 | 0.851 | n.s. |
| 2 to 5 - Cardinality5 | 0.67 | 0.65 | 1.02 | 0.308 | 0.841 | n.s. |
| 3 to 5 - 4 to 5 | -0.24 | 0.63 | -0.38 | 0.705 | 0.913 | n.s. |
| 3 to 5 - 6 to 5 | 1.05 | 0.68 | 1.55 | 0.121 | 0.593 | n.s. |
| 3 to 5 - Cardinality5 | 1.17 | 0.69 | 1.69 | 0.091 | 0.535 | n.s. |
| 4 to 5 - 6 to 5 | 1.29 | 0.68 | 1.90 | 0.057 | 0.411 | n.s. |
| 4 to 5 - Cardinality5 | 1.41 | 0.69 | 2.06 | 0.040 | 0.332 | n.s. |
| 6 to 5 - Cardinality5 | 0.12 | 0.74 | 0.16 | 0.872 | 0.913 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.06, *p* = 0.124, η²_G = 0.250
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.80 | 5 | = 0.576 | 0.59 [-0.58, 0.48] | medium | n.s. |
| 2 to 5 vs 4 to 5 | 1.19 | 5 | = 0.479 | 0.51 [-0.60, 0.51] | medium | n.s. |
| 2 to 5 vs 6 to 5 | 1.80 | 5 | = 0.352 | 1.08 [-0.34, 1.05] | large | n.s. |
| 2 to 5 vs Cardinality5 | 3.62 | 5 | = 0.080 | 2.37 [0.04, 1.48] | large | n.s. |
| 3 to 5 vs 4 to 5 | 0.21 | 5 | = 0.843 | 0.14 [-0.48, 0.80] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 1.75 | 5 | = 0.352 | 0.65 [-0.09, 1.52] | medium | n.s. |
| 3 to 5 vs Cardinality5 | 3.57 | 5 | = 0.080 | 1.73 [0.04, 1.73] | large | n.s. |
| 4 to 5 vs 6 to 5 | 0.55 | 5 | = 0.672 | 0.34 [-0.41, 1.18] | small | n.s. |
| 4 to 5 vs Cardinality5 | 1.34 | 5 | = 0.474 | 0.82 [-0.42, 1.17] | large | n.s. |
| 6 to 5 vs Cardinality5 | 1.00 | 5 | = 0.518 | 0.51 [-0.56, 1.36] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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
