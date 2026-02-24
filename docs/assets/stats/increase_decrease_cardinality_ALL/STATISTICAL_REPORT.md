# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:26:21

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| Cardinality (no change) | 24 | 107.17 ms | 8.98 | 1.83 | [92.00, 116.00] |
| Decreasing (any step) | 24 | 106.33 ms | 7.64 | 1.56 | [96.00, 116.00] |
| Increasing (any step) | 24 | 103.00 ms | 9.16 | 1.87 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -1.28 µV | 1.38 | 0.28 | [-4.83, 0.55] |
| Decreasing (any step) | 24 | -1.20 µV | 1.35 | 0.28 | [-5.27, 0.46] |
| Increasing (any step) | 24 | -0.92 µV | 0.94 | 0.19 | [-3.72, 0.35] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 175.67 ms | 16.80 | 3.43 | [144.00, 204.00] |
| Decreasing (any step) | 24 | 177.00 ms | 14.46 | 2.95 | [144.00, 204.00] |
| Increasing (any step) | 24 | 171.83 ms | 18.59 | 3.80 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | -4.62 µV | 2.14 | 0.44 | [-9.57, -0.60] |
| Decreasing (any step) | 24 | -4.81 µV | 1.89 | 0.39 | [-8.85, -1.59] |
| Increasing (any step) | 24 | -5.29 µV | 2.15 | 0.44 | [-10.07, -1.13] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 106.00 ms | 10.55 | 2.15 | [92.00, 116.00] |
| Decreasing (any step) | 24 | 109.00 ms | 7.93 | 1.62 | [92.00, 116.00] |
| Increasing (any step) | 24 | 101.67 ms | 8.98 | 1.83 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.27 µV | 1.86 | 0.38 | [-1.29, 5.73] |
| Decreasing (any step) | 24 | 1.26 µV | 1.88 | 0.38 | [-1.75, 5.65] |
| Increasing (any step) | 24 | 1.04 µV | 1.37 | 0.28 | [-1.16, 4.35] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 463.50 ms | 24.86 | 5.08 | [420.00, 516.00] |
| Decreasing (any step) | 24 | 475.83 ms | 27.24 | 5.56 | [420.00, 528.00] |
| Increasing (any step) | 24 | 480.17 ms | 31.99 | 6.53 | [420.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 24 | 1.14 µV | 2.72 | 0.56 | [-4.85, 5.95] |
| Decreasing (any step) | 24 | 3.38 µV | 2.99 | 0.61 | [-1.94, 8.19] |
| Increasing (any step) | 24 | 2.85 µV | 3.00 | 0.61 | [-1.87, 8.07] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 485.46, BIC = 499.12
- **Decreasing (any step) vs Cardinality (no change)**: *β* = -0.42, *SE* = 1.390, *z* = -0.304, *p* = 0.761
- **Increasing (any step) vs Cardinality (no change)**: *β* = -4.04, *SE* = 1.316, *z* = -3.069, *p* = 0.002
- **SNR**: *β* = -0.24, *SE* = 0.279, *z* = -0.876, *p* = 0.381

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | 0.42 | 1.39 | 0.30 | 0.761 | 0.761 | n.s. |
| Cardinality (no change) - Increasing (any step) | 4.04 | 1.32 | 3.07 | 0.002 | 0.006 | ** |
| Decreasing (any step) - Increasing (any step) | 3.62 | 1.35 | 2.68 | 0.007 | 0.015 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.29, *p* = 0.009, η²_G = 0.044
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | 0.71 | 23 | = 0.487 | 0.10 [-0.28, 0.57] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 2.83 | 23 | = 0.029 | 0.46 [0.12, 1.03] | small | * |
| Decreasing (any step) vs Increasing (any step) | 2.39 | 23 | = 0.038 | 0.40 [0.04, 0.93] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 177.30, BIC = 190.96
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.40, *SE* = 0.178, *z* = 2.276, *p* = 0.023
- **Increasing (any step) vs Cardinality (no change)**: *β* = 0.46, *SE* = 0.167, *z* = 2.719, *p* = 0.007
- **SNR**: *β* = -0.19, *SE* = 0.038, *z* = -5.148, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.40 | 0.18 | -2.28 | 0.023 | 0.045 | * |
| Cardinality (no change) - Increasing (any step) | -0.45 | 0.17 | -2.72 | 0.007 | 0.020 | * |
| Decreasing (any step) - Increasing (any step) | -0.05 | 0.17 | -0.29 | 0.770 | 0.770 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.99, *p* = 0.148, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.39 | 23 | = 0.700 | -0.06 [-0.50, 0.34] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | -1.90 | 23 | = 0.177 | -0.30 [-0.83, 0.05] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | -1.62 | 23 | = 0.177 | -0.24 [-0.77, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 585.51, BIC = 599.17
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 1.65, *SE* = 3.246, *z* = 0.510, *p* = 0.610
- **Increasing (any step) vs Cardinality (no change)**: *β* = -3.46, *SE* = 3.429, *z* = -1.008, *p* = 0.314
- **SNR**: *β* = -0.05, *SE* = 0.259, *z* = -0.179, *p* = 0.858

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -1.65 | 3.25 | -0.51 | 0.610 | 0.610 | n.s. |
| Cardinality (no change) - Increasing (any step) | 3.46 | 3.43 | 1.01 | 0.314 | 0.529 | n.s. |
| Decreasing (any step) - Increasing (any step) | 5.11 | 2.73 | 1.87 | 0.061 | 0.172 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.89, *p* = 0.162, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.63 | 23 | = 0.536 | -0.09 [-0.55, 0.30] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 1.48 | 23 | = 0.228 | 0.22 [-0.13, 0.73] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | 1.52 | 23 | = 0.228 | 0.31 [-0.12, 0.74] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 244.26, BIC = 257.92
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.28, *SE* = 0.289, *z* = 0.975, *p* = 0.329
- **Increasing (any step) vs Cardinality (no change)**: *β* = -0.11, *SE* = 0.308, *z* = -0.368, *p* = 0.713
- **SNR**: *β* = -0.07, *SE* = 0.025, *z* = -2.737, *p* = 0.006

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.28 | 0.29 | -0.98 | 0.329 | 0.550 | n.s. |
| Cardinality (no change) - Increasing (any step) | 0.11 | 0.31 | 0.37 | 0.713 | 0.713 | n.s. |
| Decreasing (any step) - Increasing (any step) | 0.39 | 0.23 | 1.70 | 0.089 | 0.243 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.37, *p* = 0.018, η²_G = 0.019
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | 0.75 | 23 | = 0.461 | 0.10 [-0.27, 0.58] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 3.35 | 23 | = 0.008 | 0.31 [0.21, 1.15] | small | ** |
| Decreasing (any step) vs Increasing (any step) | 2.01 | 23 | = 0.084 | 0.24 [-0.03, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 500.25, BIC = 513.91
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 3.02, *SE* = 1.526, *z* = 1.979, *p* = 0.048
- **Increasing (any step) vs Cardinality (no change)**: *β* = -4.33, *SE* = 1.496, *z* = -2.895, *p* = 0.004
- **SNR**: *β* = -0.01, *SE* = 0.204, *z* = -0.065, *p* = 0.948

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -3.02 | 1.53 | -1.98 | 0.048 | 0.048 | * |
| Cardinality (no change) - Increasing (any step) | 4.33 | 1.50 | 2.89 | 0.004 | 0.008 | ** |
| Decreasing (any step) - Increasing (any step) | 7.35 | 1.52 | 4.85 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 11.64, *p* < .001, η²_G = 0.100
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -2.34 | 23 | = 0.028 | -0.32 [-0.92, -0.03] | small | * |
| Cardinality (no change) vs Increasing (any step) | 2.75 | 23 | = 0.017 | 0.44 [0.11, 1.02] | small | * |
| Decreasing (any step) vs Increasing (any step) | 4.32 | 23 | < .001 | 0.87 [0.38, 1.38] | large | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 216.41, BIC = 230.07
- **Decreasing (any step) vs Cardinality (no change)**: *β* = -0.26, *SE* = 0.208, *z* = -1.234, *p* = 0.217
- **Increasing (any step) vs Cardinality (no change)**: *β* = -0.27, *SE* = 0.203, *z* = -1.343, *p* = 0.179
- **SNR**: *β* = 0.16, *SE* = 0.030, *z* = 5.426, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | 0.26 | 0.21 | 1.23 | 0.217 | 0.447 | n.s. |
| Cardinality (no change) - Increasing (any step) | 0.27 | 0.20 | 1.34 | 0.179 | 0.447 | n.s. |
| Decreasing (any step) - Increasing (any step) | 0.02 | 0.21 | 0.08 | 0.937 | 0.937 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.59, *p* = 0.560, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | 0.05 | 23 | = 0.964 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 0.91 | 23 | = 0.558 | 0.14 [-0.24, 0.61] | negligible | n.s. |
| Decreasing (any step) vs Increasing (any step) | 1.10 | 23 | = 0.558 | 0.13 [-0.20, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 686.81, BIC = 700.47
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 18.23, *SE* = 7.788, *z* = 2.340, *p* = 0.019
- **Increasing (any step) vs Cardinality (no change)**: *β* = 21.18, *SE* = 7.413, *z* = 2.857, *p* = 0.004
- **SNR**: *β* = -0.76, *SE* = 0.477, *z* = -1.584, *p* = 0.113

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -18.22 | 7.79 | -2.34 | 0.019 | 0.038 | * |
| Cardinality (no change) - Increasing (any step) | -21.18 | 7.41 | -2.86 | 0.004 | 0.013 | * |
| Decreasing (any step) - Increasing (any step) | -2.96 | 6.90 | -0.43 | 0.668 | 0.668 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.10, *p* = 0.055, η²_G = 0.061
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -1.71 | 23 | = 0.152 | -0.47 [-0.78, 0.09] | small | n.s. |
| Cardinality (no change) vs Increasing (any step) | -2.11 | 23 | = 0.139 | -0.58 [-0.87, 0.01] | medium | n.s. |
| Decreasing (any step) vs Increasing (any step) | -0.79 | 23 | = 0.437 | -0.15 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 296.81, BIC = 310.47
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 1.48, *SE* = 0.377, *z* = 3.924, *p* < .001
- **Increasing (any step) vs Cardinality (no change)**: *β* = 1.13, *SE* = 0.353, *z* = 3.195, *p* = 0.001
- **SNR**: *β* = 0.10, *SE* = 0.026, *z* = 3.740, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -1.48 | 0.38 | -3.92 | < .001 | < .001 | *** |
| Cardinality (no change) - Increasing (any step) | -1.13 | 0.35 | -3.19 | 0.001 | 0.003 | ** |
| Decreasing (any step) - Increasing (any step) | 0.35 | 0.32 | 1.09 | 0.276 | 0.276 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 20.84, *p* < .001, η²_G = 0.101
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.608)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -5.22 | 23 | < .001 | -0.78 [-1.60, -0.54] | medium | *** |
| Cardinality (no change) vs Increasing (any step) | -3.98 | 23 | < .001 | -0.60 [-1.30, -0.33] | medium | *** |
| Decreasing (any step) vs Increasing (any step) | 3.27 | 23 | = 0.003 | 0.18 [0.20, 1.14] | negligible | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.009). Post-hoc tests revealed:
  - Cardinality (no change) showed greater latency than Increasing (any step) (*d* = 0.46)
  - Decreasing (any step) showed greater latency than Increasing (any step) (*d* = 0.40)
**N1 amplitude:** Significant main effect of condition (*p* = 0.018). Post-hoc tests revealed:
  - Cardinality (no change) showed greater amplitude than Increasing (any step) (*d* = 0.31)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller latency than Decreasing (any step) (*d* = -0.32)
  - Cardinality (no change) showed greater latency than Increasing (any step) (*d* = 0.44)
  - Decreasing (any step) showed greater latency than Increasing (any step) (*d* = 0.87)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.055)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller amplitude than Decreasing (any step) (*d* = -0.78)
  - Cardinality (no change) showed smaller amplitude than Increasing (any step) (*d* = -0.60)
  - Decreasing (any step) showed greater amplitude than Increasing (any step) (*d* = 0.18)

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
