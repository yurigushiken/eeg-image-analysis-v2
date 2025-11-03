# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:40:50

---

## 1. Analysis Overview

**Total Measurements:** 384
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 1 to 2 | 12 | 98.00 ms | 10.02 | 2.89 | [88.00, 112.00] |
| 1 to 3 | 8 | 102.00 ms | 8.82 | 3.12 | [88.00, 112.00] |
| 1 to 4 | 12 | 99.67 ms | 8.77 | 2.53 | [88.00, 112.00] |
| Cardinality1 | 14 | 105.14 ms | 7.75 | 2.07 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | -2.07 µV | 1.54 | 0.44 | [-6.14, -0.66] |
| 1 to 3 | 8 | -2.71 µV | 1.94 | 0.69 | [-5.86, -0.51] |
| 1 to 4 | 12 | -2.88 µV | 1.30 | 0.37 | [-4.46, -0.45] |
| Cardinality1 | 14 | -2.83 µV | 1.41 | 0.38 | [-5.36, -1.08] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | 168.00 ms | 15.18 | 3.31 | [144.00, 196.00] |
| 1 to 3 | 24 | 168.50 ms | 21.76 | 4.44 | [140.00, 208.00] |
| 1 to 4 | 22 | 169.82 ms | 18.55 | 3.95 | [140.00, 208.00] |
| Cardinality1 | 14 | 179.43 ms | 19.90 | 5.32 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | -5.63 µV | 2.29 | 0.50 | [-9.95, -2.19] |
| 1 to 3 | 24 | -6.62 µV | 2.58 | 0.53 | [-12.65, -2.26] |
| 1 to 4 | 22 | -6.74 µV | 2.73 | 0.58 | [-12.55, -2.67] |
| Cardinality1 | 14 | -5.06 µV | 1.81 | 0.48 | [-9.64, -2.66] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 101.85 ms | 12.92 | 3.58 | [88.00, 120.00] |
| 1 to 3 | 11 | 107.27 ms | 9.77 | 2.95 | [88.00, 120.00] |
| 1 to 4 | 12 | 105.00 ms | 10.80 | 3.12 | [88.00, 120.00] |
| Cardinality1 | 18 | 112.89 ms | 10.04 | 2.37 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 2.18 µV | 1.59 | 0.44 | [0.56, 5.23] |
| 1 to 3 | 11 | 3.04 µV | 1.86 | 0.56 | [1.13, 7.47] |
| 1 to 4 | 12 | 3.45 µV | 1.84 | 0.53 | [1.06, 6.92] |
| Cardinality1 | 18 | 4.56 µV | 2.89 | 0.68 | [1.20, 13.26] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 445.00 ms | 59.23 | 14.81 | [368.00, 536.00] |
| 1 to 3 | 19 | 471.37 ms | 46.48 | 10.66 | [368.00, 536.00] |
| 1 to 4 | 20 | 462.20 ms | 57.43 | 12.84 | [376.00, 536.00] |
| Cardinality1 | 11 | 444.73 ms | 57.68 | 17.39 | [356.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 5.79 µV | 3.15 | 0.79 | [1.69, 11.99] |
| 1 to 3 | 19 | 6.21 µV | 3.60 | 0.83 | [1.71, 15.57] |
| 1 to 4 | 20 | 6.05 µV | 3.13 | 0.70 | [2.27, 13.02] |
| Cardinality1 | 11 | 4.43 µV | 1.78 | 0.54 | [2.13, 7.37] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 331.63, BIC = 344.43
- **1 to 3 vs 1 to 2**: *β* = 2.02, *SE* = 3.658, *z* = 0.551, *p* = 0.581
- **1 to 4 vs 1 to 2**: *β* = -0.03, *SE* = 3.195, *z* = -0.009, *p* = 0.993
- **Cardinality1 vs 1 to 2**: *β* = 6.18, *SE* = 3.084, *z* = 2.003, *p* = 0.045
- **SNR**: *β* = 2.65, *SE* = 0.904, *z* = 2.931, *p* = 0.003

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -2.02 | 3.66 | -0.55 | 0.581 | 0.927 | n.s. |
| 1 to 2 - 1 to 4 | 0.03 | 3.19 | 0.01 | 0.993 | 0.993 | n.s. |
| 1 to 2 - Cardinality1 | -6.18 | 3.08 | -2.00 | 0.045 | 0.242 | n.s. |
| 1 to 3 - 1 to 4 | 2.05 | 3.74 | 0.55 | 0.584 | 0.927 | n.s. |
| 1 to 3 - Cardinality1 | -4.16 | 3.41 | -1.22 | 0.223 | 0.636 | n.s. |
| 1 to 4 - Cardinality1 | -6.21 | 3.19 | -1.94 | 0.052 | 0.242 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.990, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.11 | 2 | = 1.000 | 0.13 [-1.14, 0.96] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 2.00 | 2 | = 1.000 | 0.24 [-1.26, 0.86] | small | n.s. |
| 1 to 2 vs Cardinality1 | 0.38 | 2 | = 1.000 | 0.17 [-1.86, 0.27] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.10 | 2 | = 1.000 | 0.12 [-1.44, 1.77] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | 0.00 | 2 | = 1.000 | 0.00 [-1.17, 1.32] | negligible | n.s. |
| 1 to 4 vs Cardinality1 | -0.28 | 2 | = 1.000 | -0.15 [-1.66, 0.10] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 131.56, BIC = 144.36
- **1 to 3 vs 1 to 2**: *β* = -0.08, *SE* = 0.357, *z* = -0.235, *p* = 0.814
- **1 to 4 vs 1 to 2**: *β* = -0.31, *SE* = 0.328, *z* = -0.942, *p* = 0.346
- **Cardinality1 vs 1 to 2**: *β* = -0.47, *SE* = 0.314, *z* = -1.503, *p* = 0.133
- **SNR**: *β* = -0.84, *SE* = 0.095, *z* = -8.865, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.08 | 0.36 | 0.23 | 0.814 | 0.899 | n.s. |
| 1 to 2 - 1 to 4 | 0.31 | 0.33 | 0.94 | 0.346 | 0.818 | n.s. |
| 1 to 2 - Cardinality1 | 0.47 | 0.31 | 1.50 | 0.133 | 0.575 | n.s. |
| 1 to 3 - 1 to 4 | 0.22 | 0.36 | 0.62 | 0.534 | 0.899 | n.s. |
| 1 to 3 - Cardinality1 | 0.39 | 0.35 | 1.11 | 0.266 | 0.786 | n.s. |
| 1 to 4 - Cardinality1 | 0.16 | 0.30 | 0.54 | 0.588 | 0.899 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.34, *p* = 0.801, η²_G = 0.080
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.40 | 2 | = 0.772 | -0.39 [-0.80, 1.33] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.33 | 2 | = 0.772 | -0.11 [-0.54, 1.73] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | 0.51 | 2 | = 0.772 | 0.20 [-0.53, 1.40] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.34 | 2 | = 0.772 | 0.36 [-1.32, 1.93] | small | n.s. |
| 1 to 3 vs Cardinality1 | 1.08 | 2 | = 0.772 | 1.10 [-0.67, 2.13] | large | n.s. |
| 1 to 4 vs Cardinality1 | 1.16 | 2 | = 0.772 | 0.43 [-0.35, 1.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 698.97, BIC = 715.74
- **1 to 3 vs 1 to 2**: *β* = -0.34, *SE* = 4.134, *z* = -0.081, *p* = 0.935
- **1 to 4 vs 1 to 2**: *β* = 3.11, *SE* = 4.162, *z* = 0.748, *p* = 0.455
- **Cardinality1 vs 1 to 2**: *β* = 11.25, *SE* = 4.891, *z* = 2.300, *p* = 0.021
- **SNR**: *β* = 0.48, *SE* = 0.597, *z* = 0.809, *p* = 0.419

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.34 | 4.13 | 0.08 | 0.935 | 0.935 | n.s. |
| 1 to 2 - 1 to 4 | -3.11 | 4.16 | -0.75 | 0.455 | 0.781 | n.s. |
| 1 to 2 - Cardinality1 | -11.25 | 4.89 | -2.30 | 0.021 | 0.103 | n.s. |
| 1 to 3 - 1 to 4 | -3.45 | 4.07 | -0.85 | 0.397 | 0.781 | n.s. |
| 1 to 3 - Cardinality1 | -11.58 | 4.88 | -2.37 | 0.018 | 0.101 | n.s. |
| 1 to 4 - Cardinality1 | -8.14 | 4.84 | -1.68 | 0.093 | 0.323 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.70, *p* = 0.185, η²_G = 0.066
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.45 | 11 | = 0.790 | 0.15 [-0.43, 0.48] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.17 | 11 | = 0.865 | -0.07 [-0.59, 0.35] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -1.71 | 11 | = 0.232 | -0.61 [-1.17, 0.18] | medium | n.s. |
| 1 to 3 vs 1 to 4 | -0.83 | 11 | = 0.633 | -0.20 [-0.76, 0.15] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | -2.01 | 11 | = 0.232 | -0.71 [-1.14, 0.09] | medium | n.s. |
| 1 to 4 vs Cardinality1 | -1.93 | 11 | = 0.232 | -0.47 [-1.01, 0.24] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 329.86, BIC = 346.62
- **1 to 3 vs 1 to 2**: *β* = -0.48, *SE* = 0.431, *z* = -1.123, *p* = 0.262
- **1 to 4 vs 1 to 2**: *β* = -0.91, *SE* = 0.434, *z* = -2.099, *p* = 0.036
- **Cardinality1 vs 1 to 2**: *β* = 0.51, *SE* = 0.513, *z* = 0.999, *p* = 0.318
- **SNR**: *β* = -0.40, *SE* = 0.062, *z* = -6.319, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.48 | 0.43 | 1.12 | 0.262 | 0.597 | n.s. |
| 1 to 2 - 1 to 4 | 0.91 | 0.43 | 2.10 | 0.036 | 0.167 | n.s. |
| 1 to 2 - Cardinality1 | -0.51 | 0.51 | -1.00 | 0.318 | 0.597 | n.s. |
| 1 to 3 - 1 to 4 | 0.43 | 0.42 | 1.01 | 0.314 | 0.597 | n.s. |
| 1 to 3 - Cardinality1 | -1.00 | 0.51 | -1.94 | 0.052 | 0.192 | n.s. |
| 1 to 4 - Cardinality1 | -1.42 | 0.51 | -2.82 | 0.005 | 0.029 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.63, *p* = 0.023, η²_G = 0.102
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.57 | 11 | = 0.091 | 0.46 [0.07, 1.05] | small | n.s. |
| 1 to 2 vs 1 to 4 | 0.14 | 11 | = 0.890 | 0.02 [-0.09, 0.88] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -1.24 | 11 | = 0.287 | -0.47 [-1.01, 0.30] | small | n.s. |
| 1 to 3 vs 1 to 4 | -2.25 | 11 | = 0.091 | -0.43 [-0.49, 0.40] | small | n.s. |
| 1 to 3 vs Cardinality1 | -2.40 | 11 | = 0.091 | -0.94 [-1.44, -0.12] | large | n.s. |
| 1 to 4 vs Cardinality1 | -1.42 | 11 | = 0.274 | -0.48 [-1.14, 0.14] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 419.02, BIC = 432.94
- **1 to 3 vs 1 to 2**: *β* = 5.06, *SE* = 4.234, *z* = 1.196, *p* = 0.232
- **1 to 4 vs 1 to 2**: *β* = 2.13, *SE* = 4.183, *z* = 0.509, *p* = 0.610
- **Cardinality1 vs 1 to 2**: *β* = 10.46, *SE* = 3.769, *z* = 2.774, *p* = 0.006
- **SNR**: *β* = 1.33, *SE* = 0.889, *z* = 1.497, *p* = 0.134

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -5.06 | 4.23 | -1.20 | 0.232 | 0.547 | n.s. |
| 1 to 2 - 1 to 4 | -2.13 | 4.18 | -0.51 | 0.610 | 0.747 | n.s. |
| 1 to 2 - Cardinality1 | -10.46 | 3.77 | -2.77 | 0.006 | 0.033 | * |
| 1 to 3 - 1 to 4 | 2.93 | 4.32 | 0.68 | 0.497 | 0.747 | n.s. |
| 1 to 3 - Cardinality1 | -5.39 | 3.94 | -1.37 | 0.171 | 0.529 | n.s. |
| 1 to 4 - Cardinality1 | -8.32 | 3.85 | -2.16 | 0.030 | 0.143 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.777, η²_G = 0.156
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.08 | 2 | = 0.946 | 0.07 [-0.99, 0.87] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 0.15 | 2 | = 0.946 | 0.15 [-1.12, 0.75] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -1.00 | 2 | = 0.845 | -0.82 [-1.36, 0.11] | large | n.s. |
| 1 to 3 vs 1 to 4 | 0.08 | 2 | = 0.946 | 0.08 [-0.75, 1.40] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | -1.19 | 2 | = 0.845 | -0.97 [-1.21, 0.29] | large | n.s. |
| 1 to 4 vs Cardinality1 | -1.43 | 2 | = 0.845 | -1.17 [-1.49, 0.10] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 208.92, BIC = 222.84
- **1 to 3 vs 1 to 2**: *β* = 0.57, *SE* = 0.554, *z* = 1.028, *p* = 0.304
- **1 to 4 vs 1 to 2**: *β* = 0.55, *SE* = 0.553, *z* = 0.997, *p* = 0.319
- **Cardinality1 vs 1 to 2**: *β* = 2.03, *SE* = 0.493, *z* = 4.116, *p* < .001
- **SNR**: *β* = 0.91, *SE* = 0.130, *z* = 7.005, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.57 | 0.55 | -1.03 | 0.304 | 0.663 | n.s. |
| 1 to 2 - 1 to 4 | -0.55 | 0.55 | -1.00 | 0.319 | 0.663 | n.s. |
| 1 to 2 - Cardinality1 | -2.03 | 0.49 | -4.12 | < .001 | < .001 | *** |
| 1 to 3 - 1 to 4 | 0.02 | 0.57 | 0.03 | 0.974 | 0.974 | n.s. |
| 1 to 3 - Cardinality1 | -1.46 | 0.51 | -2.84 | 0.005 | 0.018 | * |
| 1 to 4 - Cardinality1 | -1.48 | 0.50 | -2.94 | 0.003 | 0.016 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.44, *p* = 0.057, η²_G = 0.460
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.27 | 2 | = 0.810 | 0.23 [-1.38, 0.55] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.62 | 2 | = 0.297 | -0.96 [-1.94, 0.22] | large | n.s. |
| 1 to 2 vs Cardinality1 | -1.89 | 2 | = 0.297 | -1.42 [-1.73, -0.12] | large | n.s. |
| 1 to 3 vs 1 to 4 | -3.39 | 2 | = 0.265 | -1.21 [-1.30, 0.83] | large | n.s. |
| 1 to 3 vs Cardinality1 | -3.14 | 2 | = 0.265 | -1.57 [-1.48, 0.11] | large | n.s. |
| 1 to 4 vs Cardinality1 | -2.04 | 2 | = 0.297 | -0.85 [-1.64, 0.01] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 724.65, BIC = 739.98
- **1 to 3 vs 1 to 2**: *β* = 27.35, *SE* = 17.428, *z* = 1.569, *p* = 0.117
- **1 to 4 vs 1 to 2**: *β* = 17.57, *SE* = 17.152, *z* = 1.024, *p* = 0.306
- **Cardinality1 vs 1 to 2**: *β* = -5.56, *SE* = 21.107, *z* = -0.263, *p* = 0.792
- **SNR**: *β* = -2.11, *SE* = 2.641, *z* = -0.800, *p* = 0.424

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -27.35 | 17.43 | -1.57 | 0.117 | 0.525 | n.s. |
| 1 to 2 - 1 to 4 | -17.57 | 17.15 | -1.02 | 0.306 | 0.707 | n.s. |
| 1 to 2 - Cardinality1 | 5.56 | 21.11 | 0.26 | 0.792 | 0.796 | n.s. |
| 1 to 3 - 1 to 4 | 9.78 | 16.28 | 0.60 | 0.548 | 0.796 | n.s. |
| 1 to 3 - Cardinality1 | 32.90 | 21.12 | 1.56 | 0.119 | 0.525 | n.s. |
| 1 to 4 - Cardinality1 | 23.12 | 20.70 | 1.12 | 0.264 | 0.707 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.729, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.54 | 9 | = 0.809 | -0.27 [-0.95, 0.24] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.09 | 9 | = 0.809 | -0.40 [-0.76, 0.36] | small | n.s. |
| 1 to 2 vs Cardinality1 | -0.69 | 9 | = 0.809 | -0.27 [-0.94, 0.51] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.51 | 9 | = 0.809 | -0.16 [-0.39, 0.58] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | -0.02 | 9 | = 0.981 | -0.01 [-0.46, 0.90] | negligible | n.s. |
| 1 to 4 vs Cardinality1 | 0.44 | 9 | = 0.809 | 0.15 [-0.38, 1.00] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 286.17, BIC = 301.50
- **1 to 3 vs 1 to 2**: *β* = 0.15, *SE* = 0.528, *z* = 0.281, *p* = 0.778
- **1 to 4 vs 1 to 2**: *β* = 0.24, *SE* = 0.515, *z* = 0.470, *p* = 0.638
- **Cardinality1 vs 1 to 2**: *β* = -0.26, *SE* = 0.656, *z* = -0.393, *p* = 0.694
- **SNR**: *β* = 0.61, *SE* = 0.097, *z* = 6.367, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.15 | 0.53 | -0.28 | 0.778 | 0.983 | n.s. |
| 1 to 2 - 1 to 4 | -0.24 | 0.52 | -0.47 | 0.638 | 0.983 | n.s. |
| 1 to 2 - Cardinality1 | 0.26 | 0.66 | 0.39 | 0.694 | 0.983 | n.s. |
| 1 to 3 - 1 to 4 | -0.09 | 0.47 | -0.20 | 0.843 | 0.983 | n.s. |
| 1 to 3 - Cardinality1 | 0.41 | 0.68 | 0.60 | 0.550 | 0.981 | n.s. |
| 1 to 4 - Cardinality1 | 0.50 | 0.67 | 0.75 | 0.453 | 0.973 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.78, *p* = 0.008, η²_G = 0.153
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.40 | 9 | = 0.234 | -0.38 [-0.85, 0.33] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.55 | 9 | = 0.234 | -0.42 [-0.89, 0.24] | small | n.s. |
| 1 to 2 vs Cardinality1 | 2.07 | 9 | = 0.136 | 0.63 [-0.13, 1.44] | medium | n.s. |
| 1 to 3 vs 1 to 4 | 0.03 | 9 | = 0.980 | 0.01 [-0.46, 0.50] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | 2.53 | 9 | = 0.097 | 1.03 [0.00, 1.53] | large | n.s. |
| 1 to 4 vs Cardinality1 | 3.25 | 9 | = 0.060 | 1.20 [0.14, 1.76] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.023) (no significant pairwise comparisons)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.057)
**P3b amplitude:** Significant main effect of condition (*p* = 0.008) (no significant pairwise comparisons)

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
