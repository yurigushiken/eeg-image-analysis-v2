# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:21:35

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
| 1 to 1 | 24 | 102.17 ms | 9.65 | 1.97 | [88.00, 112.00] |
| 1 to 2 | 24 | 99.17 ms | 10.28 | 2.10 | [88.00, 112.00] |
| 1 to 3 | 24 | 99.17 ms | 10.68 | 2.18 | [88.00, 112.00] |
| 1 to 4 | 24 | 102.00 ms | 9.51 | 1.94 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | -1.52 µV | 2.13 | 0.44 | [-5.36, 3.66] |
| 1 to 2 | 24 | -0.21 µV | 2.14 | 0.44 | [-3.35, 5.05] |
| 1 to 3 | 24 | -0.30 µV | 2.51 | 0.51 | [-5.86, 4.93] |
| 1 to 4 | 24 | -1.36 µV | 1.95 | 0.40 | [-4.46, 2.21] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 178.67 ms | 19.12 | 3.90 | [144.00, 208.00] |
| 1 to 2 | 24 | 172.33 ms | 19.09 | 3.90 | [144.00, 208.00] |
| 1 to 3 | 24 | 170.67 ms | 22.62 | 4.62 | [144.00, 208.00] |
| 1 to 4 | 24 | 175.00 ms | 17.86 | 3.65 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | -3.27 µV | 2.62 | 0.53 | [-9.64, 0.56] |
| 1 to 2 | 24 | -5.53 µV | 2.35 | 0.48 | [-10.03, -0.26] |
| 1 to 3 | 24 | -6.24 µV | 2.69 | 0.55 | [-12.30, -1.95] |
| 1 to 4 | 24 | -6.39 µV | 3.22 | 0.66 | [-13.14, -1.20] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 112.33 ms | 14.25 | 2.91 | [80.00, 124.00] |
| 1 to 2 | 24 | 99.00 ms | 18.66 | 3.81 | [80.00, 124.00] |
| 1 to 3 | 24 | 98.33 ms | 17.05 | 3.48 | [80.00, 124.00] |
| 1 to 4 | 24 | 97.00 ms | 13.51 | 2.76 | [80.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 3.84 µV | 3.02 | 0.62 | [-0.77, 13.50] |
| 1 to 2 | 24 | 1.47 µV | 1.88 | 0.38 | [-3.63, 4.29] |
| 1 to 3 | 24 | 1.54 µV | 2.43 | 0.50 | [-2.50, 7.47] |
| 1 to 4 | 24 | 2.22 µV | 2.22 | 0.45 | [-1.00, 6.92] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 437.50 ms | 61.72 | 12.60 | [356.00, 536.00] |
| 1 to 2 | 24 | 454.83 ms | 57.39 | 11.72 | [360.00, 536.00] |
| 1 to 3 | 24 | 445.00 ms | 48.71 | 9.94 | [356.00, 516.00] |
| 1 to 4 | 24 | 460.00 ms | 57.98 | 11.83 | [356.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 2.52 µV | 2.40 | 0.49 | [-2.10, 7.37] |
| 1 to 2 | 24 | 4.50 µV | 3.76 | 0.77 | [-3.36, 11.99] |
| 1 to 3 | 24 | 5.44 µV | 4.11 | 0.84 | [-1.55, 14.25] |
| 1 to 4 | 24 | 5.18 µV | 3.70 | 0.76 | [-0.58, 13.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 724.57, BIC = 742.52
- **1 to 2 vs 1 to 1**: *β* = -2.89, *SE* = 2.831, *z* = -1.021, *p* = 0.307
- **1 to 3 vs 1 to 1**: *β* = -3.14, *SE* = 2.834, *z* = -1.109, *p* = 0.267
- **1 to 4 vs 1 to 1**: *β* = -0.20, *SE* = 2.828, *z* = -0.069, *p* = 0.945
- **SNR**: *β* = 0.58, *SE* = 0.738, *z* = 0.792, *p* = 0.429

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 2.89 | 2.83 | 1.02 | 0.307 | 0.845 | n.s. |
| 1 to 1 - 1 to 3 | 3.14 | 2.83 | 1.11 | 0.267 | 0.845 | n.s. |
| 1 to 1 - 1 to 4 | 0.20 | 2.83 | 0.07 | 0.945 | 0.995 | n.s. |
| 1 to 2 - 1 to 3 | 0.25 | 2.85 | 0.09 | 0.929 | 0.995 | n.s. |
| 1 to 2 - 1 to 4 | -2.69 | 2.83 | -0.95 | 0.342 | 0.845 | n.s. |
| 1 to 3 - 1 to 4 | -2.95 | 2.83 | -1.04 | 0.298 | 0.845 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.565, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 0.97 | 23 | = 0.516 | 0.30 [-0.23, 0.62] | small | n.s. |
| 1 to 1 vs 1 to 3 | 1.02 | 23 | = 0.516 | 0.29 [-0.22, 0.63] | small | n.s. |
| 1 to 1 vs 1 to 4 | 0.06 | 23 | = 1.000 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.98 | 23 | = 0.516 | -0.29 [-0.63, 0.23] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.19 | 23 | = 0.516 | -0.28 [-0.67, 0.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 432.67, BIC = 450.62
- **1 to 2 vs 1 to 1**: *β* = 1.30, *SE* = 0.602, *z* = 2.162, *p* = 0.031
- **1 to 3 vs 1 to 1**: *β* = 1.23, *SE* = 0.603, *z* = 2.041, *p* = 0.041
- **1 to 4 vs 1 to 1**: *β* = 0.16, *SE* = 0.602, *z* = 0.271, *p* = 0.787
- **SNR**: *β* = -0.05, *SE* = 0.154, *z* = -0.311, *p* = 0.756

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | -1.30 | 0.60 | -2.16 | 0.031 | 0.170 | n.s. |
| 1 to 1 - 1 to 3 | -1.23 | 0.60 | -2.04 | 0.041 | 0.190 | n.s. |
| 1 to 1 - 1 to 4 | -0.16 | 0.60 | -0.27 | 0.787 | 0.954 | n.s. |
| 1 to 2 - 1 to 3 | 0.07 | 0.61 | 0.12 | 0.905 | 0.954 | n.s. |
| 1 to 2 - 1 to 4 | 1.14 | 0.60 | 1.89 | 0.059 | 0.215 | n.s. |
| 1 to 3 - 1 to 4 | 1.07 | 0.60 | 1.77 | 0.076 | 0.215 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.50, *p* = 0.066, η²_G = 0.072
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -2.02 | 23 | = 0.136 | -0.61 [-0.85, 0.03] | medium | n.s. |
| 1 to 1 vs 1 to 3 | -1.91 | 23 | = 0.136 | -0.52 [-0.83, 0.05] | medium | n.s. |
| 1 to 1 vs 1 to 4 | -0.31 | 23 | = 0.872 | -0.08 [-0.49, 0.36] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | 0.16 | 23 | = 0.872 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 2.12 | 23 | = 0.136 | 0.56 [-0.01, 0.87] | medium | n.s. |
| 1 to 3 vs 1 to 4 | 1.41 | 23 | = 0.256 | 0.47 [-0.14, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 829.47, BIC = 847.42
- **1 to 2 vs 1 to 1**: *β* = -6.38, *SE* = 4.094, *z* = -1.559, *p* = 0.119
- **1 to 3 vs 1 to 1**: *β* = -8.09, *SE* = 4.236, *z* = -1.909, *p* = 0.056
- **1 to 4 vs 1 to 1**: *β* = -3.73, *SE* = 4.160, *z* = -0.898, *p* = 0.369
- **SNR**: *β* = 0.04, *SE* = 0.584, *z* = 0.065, *p* = 0.948

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 6.38 | 4.09 | 1.56 | 0.119 | 0.469 | n.s. |
| 1 to 1 - 1 to 3 | 8.09 | 4.24 | 1.91 | 0.056 | 0.294 | n.s. |
| 1 to 1 - 1 to 4 | 3.73 | 4.16 | 0.90 | 0.369 | 0.749 | n.s. |
| 1 to 2 - 1 to 3 | 1.70 | 4.07 | 0.42 | 0.675 | 0.762 | n.s. |
| 1 to 2 - 1 to 4 | -2.65 | 4.04 | -0.66 | 0.512 | 0.762 | n.s. |
| 1 to 3 - 1 to 4 | -4.35 | 4.03 | -1.08 | 0.281 | 0.732 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.44, *p* = 0.238, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.39 | 23 | = 0.395 | 0.33 [-0.15, 0.71] | small | n.s. |
| 1 to 1 vs 1 to 3 | 1.64 | 23 | = 0.395 | 0.38 [-0.10, 0.77] | small | n.s. |
| 1 to 1 vs 1 to 4 | 0.99 | 23 | = 0.498 | 0.20 [-0.22, 0.63] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | 0.37 | 23 | = 0.717 | 0.08 [-0.35, 0.50] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.77 | 23 | = 0.539 | -0.14 [-0.58, 0.27] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.33 | 23 | = 0.395 | -0.21 [-0.70, 0.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 410.94, BIC = 428.89
- **1 to 2 vs 1 to 1**: *β* = -1.61, *SE* = 0.478, *z* = -3.357, *p* = 0.001
- **1 to 3 vs 1 to 1**: *β* = -1.81, *SE* = 0.494, *z* = -3.672, *p* < .001
- **1 to 4 vs 1 to 1**: *β* = -2.21, *SE* = 0.486, *z* = -4.542, *p* < .001
- **SNR**: *β* = -0.51, *SE* = 0.067, *z* = -7.629, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 1.61 | 0.48 | 3.36 | < .001 | 0.003 | ** |
| 1 to 1 - 1 to 3 | 1.82 | 0.49 | 3.67 | < .001 | 0.001 | ** |
| 1 to 1 - 1 to 4 | 2.21 | 0.49 | 4.54 | < .001 | < .001 | *** |
| 1 to 2 - 1 to 3 | 0.21 | 0.48 | 0.44 | 0.660 | 0.660 | n.s. |
| 1 to 2 - 1 to 4 | 0.60 | 0.47 | 1.27 | 0.204 | 0.495 | n.s. |
| 1 to 3 - 1 to 4 | 0.39 | 0.47 | 0.83 | 0.407 | 0.648 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 11.32, *p* < .001, η²_G = 0.178
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.712)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 4.28 | 23 | < .001 | 0.91 [0.38, 1.37] | large | *** |
| 1 to 1 vs 1 to 3 | 4.32 | 23 | < .001 | 1.12 [0.38, 1.38] | large | *** |
| 1 to 1 vs 1 to 4 | 3.88 | 23 | = 0.002 | 1.06 [0.31, 1.28] | large | ** |
| 1 to 2 vs 1 to 3 | 1.71 | 23 | = 0.152 | 0.28 [-0.09, 0.78] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.47 | 23 | = 0.185 | 0.31 [-0.13, 0.73] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.29 | 23 | = 0.774 | 0.05 [-0.36, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 806.71, BIC = 824.66
- **1 to 2 vs 1 to 1**: *β* = -13.31, *SE* = 3.891, *z* = -3.421, *p* = 0.001
- **1 to 3 vs 1 to 1**: *β* = -14.07, *SE* = 3.895, *z* = -3.612, *p* < .001
- **1 to 4 vs 1 to 1**: *β* = -15.35, *SE* = 3.891, *z* = -3.944, *p* < .001
- **SNR**: *β* = 0.45, *SE* = 1.148, *z* = 0.392, *p* = 0.695

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 13.31 | 3.89 | 3.42 | < .001 | 0.002 | ** |
| 1 to 1 - 1 to 3 | 14.07 | 3.89 | 3.61 | < .001 | 0.002 | ** |
| 1 to 1 - 1 to 4 | 15.35 | 3.89 | 3.94 | < .001 | < .001 | *** |
| 1 to 2 - 1 to 3 | 0.75 | 3.90 | 0.19 | 0.847 | 0.937 | n.s. |
| 1 to 2 - 1 to 4 | 2.03 | 3.89 | 0.52 | 0.601 | 0.937 | n.s. |
| 1 to 3 - 1 to 4 | 1.28 | 3.89 | 0.33 | 0.742 | 0.937 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.50, *p* < .001, η²_G = 0.135
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 3.23 | 23 | = 0.007 | 0.80 [0.19, 1.12] | large | ** |
| 1 to 1 vs 1 to 3 | 3.70 | 23 | = 0.004 | 0.89 [0.28, 1.23] | large | ** |
| 1 to 1 vs 1 to 4 | 4.76 | 23 | < .001 | 1.10 [0.46, 1.49] | large | *** |
| 1 to 2 vs 1 to 3 | 0.15 | 23 | = 0.885 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 0.48 | 23 | = 0.880 | 0.12 [-0.32, 0.52] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.34 | 23 | = 0.880 | 0.09 [-0.35, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 435.66, BIC = 453.61
- **1 to 2 vs 1 to 1**: *β* = -2.35, *SE* = 0.569, *z* = -4.129, *p* < .001
- **1 to 3 vs 1 to 1**: *β* = -2.38, *SE* = 0.569, *z* = -4.174, *p* < .001
- **1 to 4 vs 1 to 1**: *β* = -1.64, *SE* = 0.569, *z* = -2.884, *p* = 0.004
- **SNR**: *β* = 0.47, *SE* = 0.169, *z* = 2.761, *p* = 0.006

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 2.35 | 0.57 | 4.13 | < .001 | < .001 | *** |
| 1 to 1 - 1 to 3 | 2.38 | 0.57 | 4.17 | < .001 | < .001 | *** |
| 1 to 1 - 1 to 4 | 1.64 | 0.57 | 2.88 | 0.004 | 0.016 | * |
| 1 to 2 - 1 to 3 | 0.03 | 0.57 | 0.05 | 0.961 | 0.961 | n.s. |
| 1 to 2 - 1 to 4 | -0.71 | 0.57 | -1.24 | 0.213 | 0.480 | n.s. |
| 1 to 3 - 1 to 4 | -0.74 | 0.57 | -1.29 | 0.196 | 0.480 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.95, *p* < .001, η²_G = 0.140
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 3.54 | 23 | = 0.005 | 0.94 [0.25, 1.20] | large | ** |
| 1 to 1 vs 1 to 3 | 4.00 | 23 | = 0.003 | 0.84 [0.33, 1.30] | large | ** |
| 1 to 1 vs 1 to 4 | 3.08 | 23 | = 0.011 | 0.61 [0.17, 1.09] | medium | * |
| 1 to 2 vs 1 to 3 | -0.10 | 23 | = 0.919 | -0.03 [-0.44, 0.40] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.40 | 23 | = 0.260 | -0.36 [-0.72, 0.14] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.09 | 23 | = 0.343 | -0.29 [-0.65, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1055.70, BIC = 1073.65
- **1 to 2 vs 1 to 1**: *β* = 19.68, *SE* = 15.645, *z* = 1.258, *p* = 0.208
- **1 to 3 vs 1 to 1**: *β* = 11.01, *SE* = 16.167, *z* = 0.681, *p* = 0.496
- **1 to 4 vs 1 to 1**: *β* = 25.82, *SE* = 16.070, *z* = 1.607, *p* = 0.108
- **SNR**: *β* = -1.48, *SE* = 2.318, *z* = -0.640, *p* = 0.522

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | -19.68 | 15.65 | -1.26 | 0.208 | 0.689 | n.s. |
| 1 to 1 - 1 to 3 | -11.01 | 16.17 | -0.68 | 0.496 | 0.872 | n.s. |
| 1 to 1 - 1 to 4 | -25.82 | 16.07 | -1.61 | 0.108 | 0.497 | n.s. |
| 1 to 2 - 1 to 3 | 8.67 | 15.32 | 0.57 | 0.571 | 0.872 | n.s. |
| 1 to 2 - 1 to 4 | -6.14 | 15.28 | -0.40 | 0.688 | 0.872 | n.s. |
| 1 to 3 - 1 to 4 | -14.81 | 15.21 | -0.97 | 0.330 | 0.799 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.84, *p* = 0.477, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -1.03 | 23 | = 0.657 | -0.29 [-0.64, 0.22] | small | n.s. |
| 1 to 1 vs 1 to 3 | -0.50 | 23 | = 0.719 | -0.13 [-0.52, 0.32] | negligible | n.s. |
| 1 to 1 vs 1 to 4 | -1.41 | 23 | = 0.657 | -0.38 [-0.72, 0.14] | small | n.s. |
| 1 to 2 vs 1 to 3 | 0.63 | 23 | = 0.719 | 0.18 [-0.30, 0.55] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.36 | 23 | = 0.719 | -0.09 [-0.50, 0.35] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.00 | 23 | = 0.657 | -0.28 [-0.63, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 471.96, BIC = 489.91
- **1 to 2 vs 1 to 1**: *β* = 1.46, *SE* = 0.624, *z* = 2.338, *p* = 0.019
- **1 to 3 vs 1 to 1**: *β* = 2.15, *SE* = 0.652, *z* = 3.295, *p* = 0.001
- **1 to 4 vs 1 to 1**: *β* = 1.92, *SE* = 0.646, *z* = 2.968, *p* = 0.003
- **SNR**: *β* = 0.33, *SE* = 0.107, *z* = 3.060, *p* = 0.002

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | -1.46 | 0.62 | -2.34 | 0.019 | 0.075 | n.s. |
| 1 to 1 - 1 to 3 | -2.15 | 0.65 | -3.29 | < .001 | 0.006 | ** |
| 1 to 1 - 1 to 4 | -1.92 | 0.65 | -2.97 | 0.003 | 0.015 | * |
| 1 to 2 - 1 to 3 | -0.69 | 0.61 | -1.13 | 0.256 | 0.589 | n.s. |
| 1 to 2 - 1 to 4 | -0.46 | 0.60 | -0.76 | 0.447 | 0.694 | n.s. |
| 1 to 3 - 1 to 4 | 0.23 | 0.60 | 0.38 | 0.704 | 0.704 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.71, *p* < .001, η²_G = 0.097
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -2.98 | 23 | = 0.013 | -0.63 [-1.07, -0.15] | medium | * |
| 1 to 1 vs 1 to 3 | -4.04 | 23 | = 0.002 | -0.87 [-1.31, -0.34] | large | ** |
| 1 to 1 vs 1 to 4 | -4.76 | 23 | < .001 | -0.85 [-1.48, -0.46] | large | *** |
| 1 to 2 vs 1 to 3 | -1.44 | 23 | = 0.244 | -0.24 [-0.73, 0.14] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.03 | 23 | = 0.375 | -0.18 [-0.64, 0.22] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.52 | 23 | = 0.608 | 0.07 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.066)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 1 showed greater amplitude than 1 to 2 (*d* = 0.91)
  - 1 to 1 showed greater amplitude than 1 to 3 (*d* = 1.12)
  - 1 to 1 showed greater amplitude than 1 to 4 (*d* = 1.06)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 1 showed greater latency than 1 to 2 (*d* = 0.80)
  - 1 to 1 showed greater latency than 1 to 3 (*d* = 0.89)
  - 1 to 1 showed greater latency than 1 to 4 (*d* = 1.10)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 1 showed greater amplitude than 1 to 2 (*d* = 0.94)
  - 1 to 1 showed greater amplitude than 1 to 3 (*d* = 0.84)
  - 1 to 1 showed greater amplitude than 1 to 4 (*d* = 0.61)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 1 showed smaller amplitude than 1 to 2 (*d* = -0.63)
  - 1 to 1 showed smaller amplitude than 1 to 3 (*d* = -0.87)
  - 1 to 1 showed smaller amplitude than 1 to 4 (*d* = -0.85)

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
