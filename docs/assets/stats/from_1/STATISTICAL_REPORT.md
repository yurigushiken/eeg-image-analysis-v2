# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:40:30

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
| 1 to 2 | 12 | 101.33 ms | 9.85 | 2.84 | [88.00, 112.00] |
| 1 to 3 | 16 | 102.75 ms | 9.77 | 2.44 | [88.00, 112.00] |
| 1 to 4 | 12 | 99.33 ms | 11.67 | 3.37 | [88.00, 112.00] |
| Cardinality1 | 10 | 101.20 ms | 10.67 | 3.38 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 2.60 µV | 1.94 | 0.56 | [0.68, 5.82] |
| 1 to 3 | 16 | 3.03 µV | 2.24 | 0.56 | [0.49, 8.95] |
| 1 to 4 | 12 | 2.41 µV | 1.39 | 0.40 | [0.70, 5.41] |
| Cardinality1 | 10 | 2.87 µV | 2.31 | 0.73 | [0.62, 8.77] |


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
- AIC = 381.66, BIC = 395.05
- **1 to 3 vs 1 to 2**: *β* = 1.11, *SE* = 3.244, *z* = 0.342, *p* = 0.732
- **1 to 4 vs 1 to 2**: *β* = -1.36, *SE* = 3.564, *z* = -0.382, *p* = 0.703
- **Cardinality1 vs 1 to 2**: *β* = 1.26, *SE* = 3.783, *z* = 0.333, *p* = 0.739
- **SNR**: *β* = 1.41, *SE* = 0.801, *z* = 1.761, *p* = 0.078

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -1.11 | 3.24 | -0.34 | 0.732 | 0.992 | n.s. |
| 1 to 2 - 1 to 4 | 1.36 | 3.56 | 0.38 | 0.703 | 0.992 | n.s. |
| 1 to 2 - Cardinality1 | -1.26 | 3.78 | -0.33 | 0.739 | 0.992 | n.s. |
| 1 to 3 - 1 to 4 | 2.47 | 3.38 | 0.73 | 0.465 | 0.976 | n.s. |
| 1 to 3 - Cardinality1 | -0.15 | 3.58 | -0.04 | 0.966 | 0.992 | n.s. |
| 1 to 4 - Cardinality1 | -2.62 | 3.65 | -0.72 | 0.473 | 0.976 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.927, η²_G = 0.046
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.61 | 2 | = 0.926 | -0.70 [-0.77, 0.66] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -0.10 | 2 | = 0.926 | -0.12 [-0.96, 1.14] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -0.10 | 2 | = 0.926 | -0.12 [-1.36, 1.13] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 1.00 | 2 | = 0.926 | 0.37 [-0.52, 1.20] | small | n.s. |
| 1 to 3 vs Cardinality1 | 1.00 | 2 | = 0.926 | 0.37 [-0.66, 1.23] | small | n.s. |
| 1 to 4 vs Cardinality1 | nan | 2 | n/a | 0.00 [-1.43, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 174.64, BIC = 188.02
- **1 to 3 vs 1 to 2**: *β* = -0.19, *SE* = 0.399, *z* = -0.471, *p* = 0.638
- **1 to 4 vs 1 to 2**: *β* = -0.09, *SE* = 0.450, *z* = -0.209, *p* = 0.834
- **Cardinality1 vs 1 to 2**: *β* = 0.43, *SE* = 0.462, *z* = 0.937, *p* = 0.349
- **SNR**: *β* = 0.93, *SE* = 0.096, *z* = 9.686, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.19 | 0.40 | 0.47 | 0.638 | 0.953 | n.s. |
| 1 to 2 - 1 to 4 | 0.09 | 0.45 | 0.21 | 0.834 | 0.969 | n.s. |
| 1 to 2 - Cardinality1 | -0.43 | 0.46 | -0.94 | 0.349 | 0.820 | n.s. |
| 1 to 3 - 1 to 4 | -0.09 | 0.42 | -0.22 | 0.824 | 0.969 | n.s. |
| 1 to 3 - Cardinality1 | -0.62 | 0.44 | -1.42 | 0.155 | 0.635 | n.s. |
| 1 to 4 - Cardinality1 | -0.53 | 0.45 | -1.18 | 0.239 | 0.745 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.764, η²_G = 0.074
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 1.15 | 2 | = 0.810 | 0.14 [-0.60, 0.84] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 0.49 | 2 | = 0.810 | 0.37 [-0.79, 1.34] | small | n.s. |
| 1 to 2 vs Cardinality1 | -0.27 | 2 | = 0.810 | -0.19 [-1.38, 1.11] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.32 | 2 | = 0.810 | 0.24 [-0.60, 1.09] | small | n.s. |
| 1 to 3 vs Cardinality1 | -0.71 | 2 | = 0.810 | -0.46 [-0.47, 1.49] | small | n.s. |
| 1 to 4 vs Cardinality1 | -2.34 | 2 | = 0.810 | -1.62 [-1.42, 0.52] | large | n.s. |

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
