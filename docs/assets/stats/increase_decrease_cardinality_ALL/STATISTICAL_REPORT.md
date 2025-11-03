# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:45:14

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
| Cardinality (no change) | 18 | 110.89 ms | 6.26 | 1.48 | [92.00, 116.00] |
| Decreasing (any step) | 17 | 105.65 ms | 7.22 | 1.75 | [96.00, 116.00] |
| Increasing (any step) | 15 | 104.53 ms | 8.40 | 2.17 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 18 | -1.77 µV | 1.24 | 0.29 | [-4.83, -0.25] |
| Decreasing (any step) | 17 | -1.74 µV | 1.23 | 0.30 | [-5.27, -0.58] |
| Increasing (any step) | 15 | -1.43 µV | 0.83 | 0.21 | [-3.72, -0.41] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | 176.00 ms | 17.10 | 3.57 | [144.00, 204.00] |
| Decreasing (any step) | 24 | 177.00 ms | 14.46 | 2.95 | [144.00, 204.00] |
| Increasing (any step) | 23 | 170.43 ms | 17.67 | 3.69 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | -4.79 µV | 2.00 | 0.42 | [-9.57, -1.40] |
| Decreasing (any step) | 24 | -4.81 µV | 1.89 | 0.39 | [-8.85, -1.59] |
| Increasing (any step) | 23 | -5.37 µV | 2.17 | 0.45 | [-10.07, -1.13] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 111.38 ms | 6.50 | 1.80 | [100.00, 116.00] |
| Decreasing (any step) | 15 | 110.13 ms | 7.07 | 1.83 | [96.00, 116.00] |
| Increasing (any step) | 15 | 104.80 ms | 8.71 | 2.25 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 2.47 µV | 1.69 | 0.47 | [0.70, 5.73] |
| Decreasing (any step) | 15 | 2.24 µV | 1.64 | 0.42 | [0.48, 5.65] |
| Increasing (any step) | 15 | 1.68 µV | 1.27 | 0.33 | [0.20, 4.35] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 470.57 ms | 23.14 | 6.19 | [436.00, 516.00] |
| Decreasing (any step) | 19 | 481.26 ms | 25.65 | 5.88 | [436.00, 528.00] |
| Increasing (any step) | 18 | 477.11 ms | 32.35 | 7.62 | [420.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 2.75 µV | 1.66 | 0.44 | [0.90, 5.95] |
| Decreasing (any step) | 19 | 4.41 µV | 2.38 | 0.55 | [0.77, 8.19] |
| Increasing (any step) | 18 | 4.08 µV | 2.37 | 0.56 | [0.93, 8.07] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 329.87, BIC = 341.35
- **Decreasing (any step) vs Cardinality (no change)**: *β* = -2.74, *SE* = 1.585, *z* = -1.727, *p* = 0.084
- **Increasing (any step) vs Cardinality (no change)**: *β* = -4.61, *SE* = 1.438, *z* = -3.207, *p* = 0.001
- **SNR**: *β* = -0.12, *SE* = 0.254, *z* = -0.470, *p* = 0.638

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | 2.74 | 1.59 | 1.73 | 0.084 | 0.161 | n.s. |
| Cardinality (no change) - Increasing (any step) | 4.61 | 1.44 | 3.21 | 0.001 | 0.004 | ** |
| Decreasing (any step) - Increasing (any step) | 1.87 | 1.57 | 1.19 | 0.233 | 0.233 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.49, *p* = 0.111, η²_G = 0.061
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | 1.00 | 9 | = 0.343 | 0.30 [-0.23, 1.02] | small | n.s. |
| Cardinality (no change) vs Increasing (any step) | 2.54 | 9 | = 0.095 | 0.56 [0.14, 1.47] | medium | n.s. |
| Decreasing (any step) vs Increasing (any step) | 1.11 | 9 | = 0.343 | 0.31 [-0.31, 1.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 99.64, BIC = 111.11
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.46, *SE* = 0.160, *z* = 2.864, *p* = 0.004
- **Increasing (any step) vs Cardinality (no change)**: *β* = 0.61, *SE* = 0.147, *z* = 4.125, *p* < .001
- **SNR**: *β* = -0.19, *SE* = 0.029, *z* = -6.455, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.46 | 0.16 | -2.86 | 0.004 | 0.008 | ** |
| Cardinality (no change) - Increasing (any step) | -0.61 | 0.15 | -4.12 | < .001 | < .001 | *** |
| Decreasing (any step) - Increasing (any step) | -0.15 | 0.16 | -0.89 | 0.372 | 0.372 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.64, *p* = 0.099, η²_G = 0.037
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.51 | 9 | = 0.621 | -0.08 [-0.53, 0.68] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | -1.93 | 9 | = 0.162 | -0.48 [-1.32, -0.04] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | -1.79 | 9 | = 0.162 | -0.36 [-1.23, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 571.34, BIC = 584.83
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 1.44, *SE* = 3.346, *z* = 0.432, *p* = 0.666
- **Increasing (any step) vs Cardinality (no change)**: *β* = -4.14, *SE* = 3.599, *z* = -1.150, *p* = 0.250
- **SNR**: *β* = -0.02, *SE* = 0.264, *z* = -0.089, *p* = 0.929

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -1.44 | 3.35 | -0.43 | 0.666 | 0.666 | n.s. |
| Cardinality (no change) - Increasing (any step) | 4.14 | 3.60 | 1.15 | 0.250 | 0.438 | n.s. |
| Decreasing (any step) - Increasing (any step) | 5.58 | 2.83 | 1.97 | 0.048 | 0.138 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.76, *p* = 0.184, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.63 | 21 | = 0.537 | -0.10 [-0.57, 0.30] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 1.42 | 21 | = 0.257 | 0.23 [-0.15, 0.76] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | 1.47 | 21 | = 0.257 | 0.34 [-0.13, 0.76] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 231.25, BIC = 244.74
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.36, *SE* = 0.274, *z* = 1.333, *p* = 0.182
- **Increasing (any step) vs Cardinality (no change)**: *β* = -0.08, *SE* = 0.299, *z* = -0.270, *p* = 0.787
- **SNR**: *β* = -0.07, *SE* = 0.024, *z* = -2.730, *p* = 0.006

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.37 | 0.27 | -1.33 | 0.182 | 0.332 | n.s. |
| Cardinality (no change) - Increasing (any step) | 0.08 | 0.30 | 0.27 | 0.787 | 0.787 | n.s. |
| Decreasing (any step) - Increasing (any step) | 0.45 | 0.22 | 2.03 | 0.042 | 0.122 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.53, *p* = 0.007, η²_G = 0.023
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | 0.46 | 21 | = 0.648 | 0.06 [-0.38, 0.49] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 3.77 | 21 | = 0.003 | 0.33 [0.29, 1.31] | small | ** |
| Decreasing (any step) vs Increasing (any step) | 2.38 | 21 | = 0.040 | 0.29 [-0.01, 0.89] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.82, BIC = 308.38
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.27, *SE* = 2.216, *z* = 0.123, *p* = 0.902
- **Increasing (any step) vs Cardinality (no change)**: *β* = -6.15, *SE* = 2.015, *z* = -3.051, *p* = 0.002
- **SNR**: *β* = -0.01, *SE* = 0.225, *z* = -0.027, *p* = 0.979

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.27 | 2.22 | -0.12 | 0.902 | 0.902 | n.s. |
| Cardinality (no change) - Increasing (any step) | 6.15 | 2.01 | 3.05 | 0.002 | 0.007 | ** |
| Decreasing (any step) - Increasing (any step) | 6.42 | 2.13 | 3.01 | 0.003 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.25, *p* = 0.008, η²_G = 0.214
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.45 | 10 | = 0.659 | -0.14 [-0.81, 0.54] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 2.76 | 10 | = 0.033 | 0.87 [0.05, 1.50] | large | * |
| Decreasing (any step) vs Increasing (any step) | 2.71 | 10 | = 0.033 | 1.06 [0.18, 1.61] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 97.72, BIC = 108.29
- **Decreasing (any step) vs Cardinality (no change)**: *β* = -0.53, *SE* = 0.206, *z* = -2.579, *p* = 0.010
- **Increasing (any step) vs Cardinality (no change)**: *β* = -0.59, *SE* = 0.188, *z* = -3.154, *p* = 0.002
- **SNR**: *β* = 0.20, *SE* = 0.024, *z* = 8.057, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | 0.53 | 0.21 | 2.58 | 0.010 | 0.020 | * |
| Cardinality (no change) - Increasing (any step) | 0.59 | 0.19 | 3.15 | 0.002 | 0.005 | ** |
| Decreasing (any step) - Increasing (any step) | 0.06 | 0.20 | 0.31 | 0.758 | 0.758 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.60, *p* = 0.099, η²_G = 0.047
- Greenhouse-Geisser corrected: *p* = 0.127 (ε = 0.629)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.40 | 10 | = 0.698 | -0.10 [-0.79, 0.55] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 1.41 | 10 | = 0.284 | 0.39 [-0.23, 1.10] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | 4.41 | 10 | = 0.004 | 0.53 [0.44, 2.05] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 487.61, BIC = 499.20
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 17.39, *SE* = 9.931, *z* = 1.751, *p* = 0.080
- **Increasing (any step) vs Cardinality (no change)**: *β* = 12.04, *SE* = 9.596, *z* = 1.255, *p* = 0.209
- **SNR**: *β* = -0.68, *SE* = 0.568, *z* = -1.198, *p* = 0.231

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -17.39 | 9.93 | -1.75 | 0.080 | 0.221 | n.s. |
| Cardinality (no change) - Increasing (any step) | -12.04 | 9.60 | -1.26 | 0.209 | 0.375 | n.s. |
| Decreasing (any step) - Increasing (any step) | 5.34 | 7.68 | 0.70 | 0.487 | 0.487 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.553, η²_G = 0.022
- Greenhouse-Geisser corrected: *p* = 0.495 (ε = 0.676)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -1.00 | 13 | = 0.567 | -0.40 [-0.86, 0.32] | small | n.s. |
| Cardinality (no change) vs Increasing (any step) | -0.48 | 13 | = 0.640 | -0.18 [-0.71, 0.45] | negligible | n.s. |
| Decreasing (any step) vs Increasing (any step) | 0.91 | 13 | = 0.567 | 0.15 [-0.26, 0.78] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 194.64, BIC = 206.24
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.48, *SE* = 0.519, *z* = 0.920, *p* = 0.357
- **Increasing (any step) vs Cardinality (no change)**: *β* = 0.26, *SE* = 0.487, *z* = 0.530, *p* = 0.596
- **SNR**: *β* = 0.16, *SE* = 0.031, *z* = 5.355, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.48 | 0.52 | -0.92 | 0.357 | 0.735 | n.s. |
| Cardinality (no change) - Increasing (any step) | -0.26 | 0.49 | -0.53 | 0.596 | 0.795 | n.s. |
| Decreasing (any step) - Increasing (any step) | 0.22 | 0.36 | 0.60 | 0.547 | 0.795 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 11.02, *p* < .001, η²_G = 0.206
- Greenhouse-Geisser corrected: *p* = 0.004 (ε = 0.571)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -3.78 | 13 | = 0.007 | -1.23 [-1.72, -0.30] | large | ** |
| Cardinality (no change) vs Increasing (any step) | -2.85 | 13 | = 0.014 | -0.91 [-1.42, -0.11] | large | * |
| Decreasing (any step) vs Increasing (any step) | 2.85 | 13 | = 0.014 | 0.24 [0.13, 1.28] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.099)
**N1 amplitude:** Significant main effect of condition (*p* = 0.007). Post-hoc tests revealed:
  - Cardinality (no change) showed greater amplitude than Increasing (any step) (*d* = 0.33)
  - Decreasing (any step) showed greater amplitude than Increasing (any step) (*d* = 0.29)
**P1 latency:** Significant main effect of condition (*p* = 0.008). Post-hoc tests revealed:
  - Cardinality (no change) showed greater latency than Increasing (any step) (*d* = 0.87)
  - Decreasing (any step) showed greater latency than Increasing (any step) (*d* = 1.06)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.099)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller amplitude than Decreasing (any step) (*d* = -1.23)
  - Cardinality (no change) showed smaller amplitude than Increasing (any step) (*d* = -0.91)
  - Decreasing (any step) showed greater amplitude than Increasing (any step) (*d* = 0.24)

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
