# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:45:05

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
| Decreasing (any step) | 17 | 106.59 ms | 7.74 | 1.88 | [96.00, 116.00] |
| Increasing (any step) | 17 | 103.06 ms | 8.55 | 2.07 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 18 | -1.77 µV | 1.24 | 0.29 | [-4.83, -0.25] |
| Decreasing (any step) | 17 | -1.75 µV | 1.10 | 0.27 | [-4.87, -0.79] |
| Increasing (any step) | 17 | -1.34 µV | 0.94 | 0.23 | [-3.80, -0.19] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | 176.00 ms | 17.10 | 3.57 | [144.00, 204.00] |
| Decreasing (any step) | 24 | 177.17 ms | 14.85 | 3.03 | [144.00, 204.00] |
| Increasing (any step) | 24 | 171.17 ms | 19.02 | 3.88 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | -4.79 µV | 2.00 | 0.42 | [-9.57, -1.40] |
| Decreasing (any step) | 24 | -4.92 µV | 1.92 | 0.39 | [-9.28, -1.69] |
| Increasing (any step) | 24 | -5.42 µV | 2.16 | 0.44 | [-9.98, -1.28] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 113.43 ms | 7.78 | 2.08 | [100.00, 120.00] |
| Decreasing (any step) | 17 | 112.47 ms | 7.73 | 1.87 | [100.00, 120.00] |
| Increasing (any step) | 14 | 106.00 ms | 9.51 | 2.54 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 2.51 µV | 1.63 | 0.44 | [0.82, 5.73] |
| Decreasing (any step) | 17 | 2.21 µV | 1.62 | 0.39 | [0.22, 5.27] |
| Increasing (any step) | 14 | 1.99 µV | 1.35 | 0.36 | [0.60, 4.54] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 470.57 ms | 23.14 | 6.19 | [436.00, 516.00] |
| Decreasing (any step) | 19 | 484.00 ms | 26.80 | 6.15 | [436.00, 532.00] |
| Increasing (any step) | 19 | 483.16 ms | 34.66 | 7.95 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 2.75 µV | 1.66 | 0.44 | [0.90, 5.95] |
| Decreasing (any step) | 19 | 4.83 µV | 2.34 | 0.54 | [1.42, 9.02] |
| Increasing (any step) | 19 | 4.34 µV | 2.48 | 0.57 | [1.09, 8.85] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 357.95, BIC = 369.66
- **Decreasing (any step) vs Cardinality (no change)**: *β* = -2.61, *SE* = 2.113, *z* = -1.234, *p* = 0.217
- **Increasing (any step) vs Cardinality (no change)**: *β* = -7.07, *SE* = 1.802, *z* = -3.924, *p* < .001
- **SNR**: *β* = 0.06, *SE* = 0.333, *z* = 0.189, *p* = 0.850

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | 2.61 | 2.11 | 1.23 | 0.217 | 0.217 | n.s. |
| Cardinality (no change) - Increasing (any step) | 7.07 | 1.80 | 3.92 | < .001 | < .001 | *** |
| Decreasing (any step) - Increasing (any step) | 4.46 | 2.04 | 2.18 | 0.029 | 0.057 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.62, *p* = 0.012, η²_G = 0.171
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | 0.45 | 10 | = 0.659 | 0.11 [-0.51, 0.77] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 2.82 | 10 | = 0.054 | 0.90 [0.24, 1.49] | large | n.s. |
| Decreasing (any step) vs Increasing (any step) | 2.32 | 10 | = 0.064 | 0.85 [-0.04, 1.36] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 107.67, BIC = 119.38
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.44, *SE* = 0.176, *z* = 2.517, *p* = 0.012
- **Increasing (any step) vs Cardinality (no change)**: *β* = 0.51, *SE* = 0.155, *z* = 3.302, *p* = 0.001
- **SNR**: *β* = -0.20, *SE* = 0.032, *z* = -5.998, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.44 | 0.18 | -2.52 | 0.012 | 0.024 | * |
| Cardinality (no change) - Increasing (any step) | -0.51 | 0.15 | -3.30 | < .001 | 0.003 | ** |
| Decreasing (any step) - Increasing (any step) | -0.07 | 0.18 | -0.39 | 0.696 | 0.696 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.09, *p* = 0.068, η²_G = 0.032
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.57 | 10 | = 0.583 | -0.08 [-0.70, 0.58] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | -2.07 | 10 | = 0.098 | -0.42 [-1.12, 0.02] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | -2.09 | 10 | = 0.098 | -0.33 [-1.39, 0.02] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 577.78, BIC = 591.36
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 1.68, *SE* = 3.198, *z* = 0.526, *p* = 0.599
- **Increasing (any step) vs Cardinality (no change)**: *β* = -4.31, *SE* = 3.275, *z* = -1.315, *p* = 0.189
- **SNR**: *β* = -0.02, *SE* = 0.225, *z* = -0.089, *p* = 0.929

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -1.68 | 3.20 | -0.53 | 0.599 | 0.599 | n.s. |
| Cardinality (no change) - Increasing (any step) | 4.31 | 3.27 | 1.31 | 0.189 | 0.342 | n.s. |
| Decreasing (any step) - Increasing (any step) | 5.99 | 2.66 | 2.25 | 0.025 | 0.072 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.38, *p* = 0.104, η²_G = 0.022
- Greenhouse-Geisser corrected: *p* = 0.120 (ε = 0.749)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.74 | 22 | = 0.467 | -0.10 [-0.59, 0.28] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 1.65 | 22 | = 0.170 | 0.24 [-0.10, 0.79] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | 1.69 | 22 | = 0.170 | 0.34 [-0.07, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 233.66, BIC = 247.23
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.23, *SE* = 0.263, *z* = 0.860, *p* = 0.390
- **Increasing (any step) vs Cardinality (no change)**: *β* = -0.24, *SE* = 0.271, *z* = -0.901, *p* = 0.368
- **SNR**: *β* = -0.06, *SE* = 0.020, *z* = -2.744, *p* = 0.006

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.23 | 0.26 | -0.86 | 0.390 | 0.600 | n.s. |
| Cardinality (no change) - Increasing (any step) | 0.24 | 0.27 | 0.90 | 0.368 | 0.600 | n.s. |
| Decreasing (any step) - Increasing (any step) | 0.47 | 0.21 | 2.24 | 0.025 | 0.074 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.63, *p* = 0.007, η²_G = 0.023
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | 0.83 | 22 | = 0.417 | 0.10 [-0.26, 0.61] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 3.61 | 22 | = 0.005 | 0.35 [0.26, 1.24] | small | ** |
| Decreasing (any step) vs Increasing (any step) | 2.22 | 22 | = 0.055 | 0.26 [0.00, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 323.57, BIC = 334.41
- **Decreasing (any step) vs Cardinality (no change)**: *β* = -0.38, *SE* = 2.540, *z* = -0.150, *p* = 0.880
- **Increasing (any step) vs Cardinality (no change)**: *β* = -7.53, *SE* = 2.518, *z* = -2.989, *p* = 0.003
- **SNR**: *β* = 0.17, *SE* = 0.248, *z* = 0.701, *p* = 0.483

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | 0.38 | 2.54 | 0.15 | 0.880 | 0.880 | n.s. |
| Cardinality (no change) - Increasing (any step) | 7.53 | 2.52 | 2.99 | 0.003 | 0.008 | ** |
| Decreasing (any step) - Increasing (any step) | 7.14 | 2.56 | 2.80 | 0.005 | 0.010 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.64, *p* = 0.011, η²_G = 0.194
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.69 | 11 | = 0.504 | -0.20 [-0.84, 0.44] | small | n.s. |
| Cardinality (no change) vs Increasing (any step) | 2.43 | 11 | = 0.050 | 0.82 [0.09, 1.47] | large | * |
| Decreasing (any step) vs Increasing (any step) | 2.73 | 11 | = 0.050 | 1.03 [0.15, 1.57] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 114.44, BIC = 125.28
- **Decreasing (any step) vs Cardinality (no change)**: *β* = -0.35, *SE* = 0.209, *z* = -1.687, *p* = 0.092
- **Increasing (any step) vs Cardinality (no change)**: *β* = -0.45, *SE* = 0.201, *z* = -2.236, *p* = 0.025
- **SNR**: *β* = 0.18, *SE* = 0.023, *z* = 7.758, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | 0.35 | 0.21 | 1.69 | 0.092 | 0.175 | n.s. |
| Cardinality (no change) - Increasing (any step) | 0.45 | 0.20 | 2.24 | 0.025 | 0.074 | n.s. |
| Decreasing (any step) - Increasing (any step) | 0.10 | 0.21 | 0.48 | 0.632 | 0.632 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.245, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.31 | 11 | = 0.762 | -0.07 [-0.73, 0.55] | negligible | n.s. |
| Cardinality (no change) vs Increasing (any step) | 1.13 | 11 | = 0.427 | 0.31 [-0.27, 0.97] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | 2.19 | 11 | = 0.154 | 0.41 [-0.07, 1.23] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 501.46, BIC = 513.17
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 20.49, *SE* = 10.642, *z* = 1.925, *p* = 0.054
- **Increasing (any step) vs Cardinality (no change)**: *β* = 18.30, *SE* = 9.691, *z* = 1.888, *p* = 0.059
- **SNR**: *β* = -0.81, *SE* = 0.536, *z* = -1.505, *p* = 0.132

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -20.49 | 10.64 | -1.93 | 0.054 | 0.154 | n.s. |
| Cardinality (no change) - Increasing (any step) | -18.30 | 9.69 | -1.89 | 0.059 | 0.154 | n.s. |
| Decreasing (any step) - Increasing (any step) | 2.19 | 8.04 | 0.27 | 0.785 | 0.785 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.543, η²_G = 0.023
- Greenhouse-Geisser corrected: *p* = 0.476 (ε = 0.632)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -0.89 | 13 | = 0.670 | -0.35 [-0.82, 0.35] | small | n.s. |
| Cardinality (no change) vs Increasing (any step) | -0.79 | 13 | = 0.670 | -0.31 [-0.79, 0.37] | small | n.s. |
| Decreasing (any step) vs Increasing (any step) | -0.06 | 13 | = 0.954 | -0.01 [-0.65, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 205.92, BIC = 217.63
- **Decreasing (any step) vs Cardinality (no change)**: *β* = 0.89, *SE* = 0.578, *z* = 1.540, *p* = 0.124
- **Increasing (any step) vs Cardinality (no change)**: *β* = 0.76, *SE* = 0.525, *z* = 1.456, *p* = 0.145
- **SNR**: *β* = 0.14, *SE* = 0.030, *z* = 4.695, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decreasing (any step) | -0.89 | 0.58 | -1.54 | 0.124 | 0.327 | n.s. |
| Cardinality (no change) - Increasing (any step) | -0.76 | 0.52 | -1.46 | 0.145 | 0.327 | n.s. |
| Decreasing (any step) - Increasing (any step) | 0.13 | 0.41 | 0.31 | 0.756 | 0.756 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 12.78, *p* < .001, η²_G = 0.248
- Greenhouse-Geisser corrected: *p* = 0.002 (ε = 0.573)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decreasing (any step) | -4.12 | 13 | = 0.004 | -1.40 [-1.83, -0.37] | large | ** |
| Cardinality (no change) vs Increasing (any step) | -3.14 | 13 | = 0.012 | -1.06 [-1.51, -0.17] | large | * |
| Decreasing (any step) vs Increasing (any step) | 2.33 | 13 | = 0.037 | 0.22 [0.14, 1.24] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.012) (no significant pairwise comparisons)
**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.068)
**N1 amplitude:** Significant main effect of condition (*p* = 0.007). Post-hoc tests revealed:
  - Cardinality (no change) showed greater amplitude than Increasing (any step) (*d* = 0.35)
**P1 latency:** Significant main effect of condition (*p* = 0.011). Post-hoc tests revealed:
  - Cardinality (no change) showed greater latency than Increasing (any step) (*d* = 0.82)
  - Decreasing (any step) showed greater latency than Increasing (any step) (*d* = 1.03)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller amplitude than Decreasing (any step) (*d* = -1.40)
  - Cardinality (no change) showed smaller amplitude than Increasing (any step) (*d* = -1.06)
  - Decreasing (any step) showed greater amplitude than Increasing (any step) (*d* = 0.22)

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
