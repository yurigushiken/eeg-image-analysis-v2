# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:18:37

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
| Decreasing Crossover | 24 | 106.83 ms | 9.40 | 1.92 | [92.00, 120.00] |
| Decreasing Large | 24 | 106.17 ms | 10.01 | 2.04 | [92.00, 120.00] |
| Decreasing Small | 24 | 108.83 ms | 10.81 | 2.21 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | -1.35 µV | 1.51 | 0.31 | [-5.88, 1.32] |
| Decreasing Large | 24 | -1.58 µV | 1.88 | 0.38 | [-7.43, 1.09] |
| Decreasing Small | 24 | -1.21 µV | 1.30 | 0.27 | [-4.34, 0.69] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 175.00 ms | 14.41 | 2.94 | [148.00, 208.00] |
| Decreasing Large | 24 | 176.00 ms | 17.97 | 3.67 | [148.00, 208.00] |
| Decreasing Small | 24 | 181.00 ms | 12.99 | 2.65 | [156.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | -5.28 µV | 1.87 | 0.38 | [-8.89, -1.81] |
| Decreasing Large | 24 | -5.42 µV | 2.11 | 0.43 | [-10.35, -1.44] |
| Decreasing Small | 24 | -3.97 µV | 2.39 | 0.49 | [-9.67, -0.79] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 112.33 ms | 9.36 | 1.91 | [100.00, 124.00] |
| Decreasing Large | 24 | 109.83 ms | 9.73 | 1.99 | [100.00, 124.00] |
| Decreasing Small | 24 | 117.00 ms | 7.85 | 1.60 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 1.49 µV | 1.84 | 0.38 | [-2.07, 5.79] |
| Decreasing Large | 24 | 1.13 µV | 2.68 | 0.55 | [-3.63, 7.08] |
| Decreasing Small | 24 | 2.16 µV | 1.86 | 0.38 | [-0.89, 7.19] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 476.33 ms | 27.28 | 5.57 | [432.00, 540.00] |
| Decreasing Large | 24 | 489.00 ms | 36.89 | 7.53 | [428.00, 540.00] |
| Decreasing Small | 24 | 482.83 ms | 27.12 | 5.54 | [432.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 3.85 µV | 3.21 | 0.65 | [-2.01, 10.69] |
| Decreasing Large | 24 | 2.83 µV | 3.35 | 0.68 | [-4.81, 8.30] |
| Decreasing Small | 24 | 4.31 µV | 3.08 | 0.63 | [-1.23, 10.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 527.73, BIC = 541.39
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.67, *SE* = 1.966, *z* = -0.339, *p* = 0.735
- **Decreasing Small vs Decreasing Crossover**: *β* = 1.93, *SE* = 2.070, *z* = 0.934, *p* = 0.350
- **SNR**: *β* = -0.06, *SE* = 0.535, *z* = -0.103, *p* = 0.918

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.67 | 1.97 | 0.34 | 0.735 | 0.735 | n.s. |
| Decreasing Crossover - Decreasing Small | -1.93 | 2.07 | -0.93 | 0.350 | 0.578 | n.s. |
| Decreasing Large - Decreasing Small | -2.60 | 2.07 | -1.26 | 0.209 | 0.505 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.393, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.33 | 23 | = 0.743 | 0.07 [-0.36, 0.49] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.99 | 23 | = 0.497 | -0.20 [-0.63, 0.22] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.33 | 23 | = 0.497 | -0.26 [-0.70, 0.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 237.89, BIC = 251.55
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.23, *SE* = 0.270, *z* = -0.850, *p* = 0.395
- **Decreasing Small vs Decreasing Crossover**: *β* = -0.26, *SE* = 0.286, *z* = -0.911, *p* = 0.362
- **SNR**: *β* = -0.33, *SE* = 0.077, *z* = -4.282, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.23 | 0.27 | 0.85 | 0.395 | 0.740 | n.s. |
| Decreasing Crossover - Decreasing Small | 0.26 | 0.29 | 0.91 | 0.362 | 0.740 | n.s. |
| Decreasing Large - Decreasing Small | 0.03 | 0.29 | 0.11 | 0.914 | 0.914 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.80, *p* = 0.456, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.70 | 23 | = 0.527 | 0.14 [-0.28, 0.57] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.64 | 23 | = 0.527 | -0.10 [-0.56, 0.29] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.14 | 23 | = 0.527 | -0.23 [-0.66, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 566.61, BIC = 580.27
- **Decreasing Large vs Decreasing Crossover**: *β* = 1.27, *SE* = 2.532, *z* = 0.502, *p* = 0.616
- **Decreasing Small vs Decreasing Crossover**: *β* = 6.40, *SE* = 2.776, *z* = 2.304, *p* = 0.021
- **SNR**: *β* = 0.06, *SE* = 0.225, *z* = 0.255, *p* = 0.799

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -1.27 | 2.53 | -0.50 | 0.616 | 0.616 | n.s. |
| Decreasing Crossover - Decreasing Small | -6.40 | 2.78 | -2.30 | 0.021 | 0.062 | n.s. |
| Decreasing Large - Decreasing Small | -5.13 | 2.35 | -2.18 | 0.029 | 0.062 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.75, *p* = 0.031, η²_G = 0.030
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -0.40 | 23 | = 0.691 | -0.06 [-0.51, 0.34] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -3.22 | 23 | = 0.011 | -0.44 [-1.12, -0.19] | small | * |
| Decreasing Large vs Decreasing Small | -1.90 | 23 | = 0.105 | -0.32 [-0.83, 0.05] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 285.45, BIC = 299.11
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.54, *SE* = 0.381, *z* = -1.409, *p* = 0.159
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.72, *SE* = 0.418, *z* = 1.729, *p* = 0.084
- **SNR**: *β* = -0.08, *SE* = 0.034, *z* = -2.491, *p* = 0.013

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.54 | 0.38 | 1.41 | 0.159 | 0.161 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.72 | 0.42 | -1.73 | 0.084 | 0.161 | n.s. |
| Decreasing Large - Decreasing Small | -1.26 | 0.35 | -3.56 | < .001 | 0.001 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.65, *p* < .001, η²_G = 0.088
- Greenhouse-Geisser corrected: *p* = 0.002 (ε = 0.696)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.47 | 23 | = 0.645 | 0.07 [-0.33, 0.52] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -4.44 | 23 | < .001 | -0.61 [-1.41, -0.41] | medium | *** |
| Decreasing Large vs Decreasing Small | -3.09 | 23 | = 0.008 | -0.64 [-1.09, -0.17] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 519.86, BIC = 533.52
- **Decreasing Large vs Decreasing Crossover**: *β* = -2.69, *SE* = 1.998, *z* = -1.344, *p* = 0.179
- **Decreasing Small vs Decreasing Crossover**: *β* = 4.41, *SE* = 2.014, *z* = 2.187, *p* = 0.029
- **SNR**: *β* = -0.25, *SE* = 0.343, *z* = -0.723, *p* = 0.469

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 2.69 | 2.00 | 1.34 | 0.179 | 0.179 | n.s. |
| Decreasing Crossover - Decreasing Small | -4.41 | 2.01 | -2.19 | 0.029 | 0.057 | n.s. |
| Decreasing Large - Decreasing Small | -7.09 | 1.98 | -3.57 | < .001 | 0.001 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.33, *p* = 0.004, η²_G = 0.102
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.23 | 23 | = 0.233 | 0.26 [-0.18, 0.68] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -2.93 | 23 | = 0.011 | -0.54 [-1.06, -0.14] | medium | * |
| Decreasing Large vs Decreasing Small | -2.96 | 23 | = 0.011 | -0.81 [-1.06, -0.15] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 273.91, BIC = 287.57
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.27, *SE* = 0.305, *z* = -0.890, *p* = 0.374
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.78, *SE* = 0.309, *z* = 2.536, *p* = 0.011
- **SNR**: *β* = 0.11, *SE* = 0.066, *z* = 1.665, *p* = 0.096

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.27 | 0.31 | 0.89 | 0.374 | 0.374 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.78 | 0.31 | -2.54 | 0.011 | 0.022 | * |
| Decreasing Large - Decreasing Small | -1.06 | 0.30 | -3.50 | < .001 | 0.001 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.93, *p* = 0.005, η²_G = 0.039
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.26 | 23 | = 0.220 | 0.15 [-0.17, 0.69] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -2.63 | 23 | = 0.023 | -0.36 [-0.99, -0.08] | small | * |
| Decreasing Large vs Decreasing Small | -2.84 | 23 | = 0.023 | -0.44 [-1.04, -0.12] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 694.66, BIC = 708.32
- **Decreasing Large vs Decreasing Crossover**: *β* = 8.31, *SE* = 7.128, *z* = 1.166, *p* = 0.244
- **Decreasing Small vs Decreasing Crossover**: *β* = 3.24, *SE* = 6.881, *z* = 0.471, *p* = 0.638
- **SNR**: *β* = -0.76, *SE* = 0.492, *z* = -1.552, *p* = 0.121

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -8.31 | 7.13 | -1.17 | 0.244 | 0.567 | n.s. |
| Decreasing Crossover - Decreasing Small | -3.24 | 6.88 | -0.47 | 0.638 | 0.688 | n.s. |
| Decreasing Large - Decreasing Small | 5.07 | 6.59 | 0.77 | 0.442 | 0.688 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.66, *p* = 0.202, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.69 | 23 | = 0.314 | -0.39 [-0.78, 0.09] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.07 | 23 | = 0.403 | -0.24 [-0.65, 0.21] | small | n.s. |
| Decreasing Large vs Decreasing Small | 0.85 | 23 | = 0.403 | 0.19 [-0.25, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 326.05, BIC = 339.71
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.57, *SE* = 0.454, *z* = -1.248, *p* = 0.212
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.80, *SE* = 0.436, *z* = 1.829, *p* = 0.067
- **SNR**: *β* = 0.08, *SE* = 0.033, *z* = 2.341, *p* = 0.019

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.57 | 0.45 | 1.25 | 0.212 | 0.212 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.80 | 0.44 | -1.83 | 0.067 | 0.130 | n.s. |
| Decreasing Large - Decreasing Small | -1.37 | 0.42 | -3.29 | 0.001 | 0.003 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.00, *p* = 0.005, η²_G = 0.037
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 2.01 | 23 | = 0.084 | 0.31 [-0.03, 0.85] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.60 | 23 | = 0.122 | -0.15 [-0.76, 0.11] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -3.05 | 23 | = 0.017 | -0.46 [-1.08, -0.16] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.031). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller latency than Decreasing Small (*d* = -0.44)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller amplitude than Decreasing Small (*d* = -0.61)
  - Decreasing Large showed smaller amplitude than Decreasing Small (*d* = -0.64)
**P1 latency:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller latency than Decreasing Small (*d* = -0.54)
  - Decreasing Large showed smaller latency than Decreasing Small (*d* = -0.81)
**P1 amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller amplitude than Decreasing Small (*d* = -0.36)
  - Decreasing Large showed smaller amplitude than Decreasing Small (*d* = -0.44)
**P3b amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - Decreasing Large showed smaller amplitude than Decreasing Small (*d* = -0.46)

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
