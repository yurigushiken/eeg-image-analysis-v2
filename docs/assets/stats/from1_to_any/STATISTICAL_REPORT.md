# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:39:00

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
| 1 to 2 | 12 | 92.67 ms | 9.32 | 2.69 | [80.00, 104.00] |
| 1 to 3 | 15 | 94.13 ms | 10.89 | 2.81 | [80.00, 104.00] |
| 1 to 4 | 11 | 89.45 ms | 11.07 | 3.34 | [80.00, 104.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 2.58 µV | 1.90 | 0.55 | [0.81, 5.82] |
| 1 to 3 | 15 | 2.91 µV | 1.79 | 0.46 | [0.49, 7.57] |
| 1 to 4 | 11 | 2.21 µV | 1.14 | 0.34 | [0.70, 3.99] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | 168.00 ms | 15.18 | 3.31 | [144.00, 196.00] |
| 1 to 3 | 24 | 168.50 ms | 22.91 | 4.68 | [136.00, 216.00] |
| 1 to 4 | 21 | 170.29 ms | 20.57 | 4.49 | [136.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | -5.63 µV | 2.29 | 0.50 | [-9.95, -2.19] |
| 1 to 3 | 24 | -6.66 µV | 2.55 | 0.52 | [-12.65, -2.71] |
| 1 to 4 | 21 | -6.94 µV | 2.64 | 0.58 | [-12.55, -2.71] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 10 | 89.60 ms | 9.65 | 3.05 | [76.00, 100.00] |
| 1 to 3 | 10 | 85.60 ms | 12.95 | 4.10 | [72.00, 100.00] |
| 1 to 4 | 15 | 90.13 ms | 10.46 | 2.70 | [68.00, 100.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 10 | 2.81 µV | 1.39 | 0.44 | [0.60, 4.45] |
| 1 to 3 | 10 | 2.60 µV | 1.93 | 0.61 | [0.93, 7.47] |
| 1 to 4 | 15 | 2.54 µV | 1.17 | 0.30 | [0.74, 4.28] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 15 | 438.93 ms | 55.93 | 14.44 | [368.00, 536.00] |
| 1 to 3 | 19 | 471.37 ms | 46.48 | 10.66 | [368.00, 536.00] |
| 1 to 4 | 20 | 462.20 ms | 57.43 | 12.84 | [376.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 15 | 6.04 µV | 3.09 | 0.80 | [1.69, 11.99] |
| 1 to 3 | 19 | 6.21 µV | 3.60 | 0.83 | [1.71, 15.57] |
| 1 to 4 | 20 | 6.05 µV | 3.13 | 0.70 | [2.27, 13.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 285.55, BIC = 295.38
- **1 to 3 vs 1 to 2**: *β* = -0.21, *SE* = 2.562, *z* = -0.084, *p* = 0.933
- **1 to 4 vs 1 to 2**: *β* = -2.62, *SE* = 2.984, *z* = -0.878, *p* = 0.380
- **SNR**: *β* = 2.09, *SE* = 0.832, *z* = 2.507, *p* = 0.012

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.21 | 2.56 | 0.08 | 0.933 | 0.933 | n.s. |
| 1 to 2 - 1 to 4 | 2.62 | 2.98 | 0.88 | 0.380 | 0.762 | n.s. |
| 1 to 3 - 1 to 4 | 2.40 | 2.74 | 0.88 | 0.381 | 0.762 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.582, η²_G = 0.120
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.96 | 2 | = 0.657 | 0.89 [-0.71, 0.97] | large | n.s. |
| 1 to 2 vs 1 to 4 | 0.48 | 2 | = 0.678 | 0.39 [-1.36, 1.87] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.00 | 2 | = 0.657 | -0.31 [-0.69, 1.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 117.70, BIC = 127.53
- **1 to 3 vs 1 to 2**: *β* = -0.11, *SE* = 0.382, *z* = -0.277, *p* = 0.782
- **1 to 4 vs 1 to 2**: *β* = -0.12, *SE* = 0.416, *z* = -0.278, *p* = 0.781
- **SNR**: *β* = 0.86, *SE* = 0.107, *z* = 8.011, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.11 | 0.38 | 0.28 | 0.782 | 0.989 | n.s. |
| 1 to 2 - 1 to 4 | 0.12 | 0.42 | 0.28 | 0.781 | 0.989 | n.s. |
| 1 to 3 - 1 to 4 | 0.01 | 0.40 | 0.03 | 0.979 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.05, *p* = 0.431, η²_G = 0.287
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.12 | 2 | = 0.504 | 1.02 [-0.69, 0.99] | large | n.s. |
| 1 to 2 vs 1 to 4 | 0.86 | 2 | = 0.723 | 0.90 [-1.24, 2.08] | large | n.s. |
| 1 to 3 vs 1 to 4 | -0.13 | 2 | = 0.905 | -0.15 [-0.64, 1.25] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 582.25, BIC = 595.39
- **1 to 3 vs 1 to 2**: *β* = -0.15, *SE* = 4.639, *z* = -0.032, *p* = 0.974
- **1 to 4 vs 1 to 2**: *β* = 3.32, *SE* = 4.692, *z* = 0.707, *p* = 0.479
- **SNR**: *β* = 0.27, *SE* = 0.868, *z* = 0.316, *p* = 0.752

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.15 | 4.64 | 0.03 | 0.974 | 0.974 | n.s. |
| 1 to 2 - 1 to 4 | -3.32 | 4.69 | -0.71 | 0.479 | 0.835 | n.s. |
| 1 to 3 - 1 to 4 | -3.47 | 4.60 | -0.75 | 0.451 | 0.835 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.81, *p* = 0.454, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.61 | 18 | = 0.577 | 0.16 [-0.43, 0.48] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.57 | 18 | = 0.577 | -0.17 [-0.61, 0.35] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.57 | 18 | = 0.401 | -0.29 [-0.81, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 270.98, BIC = 284.12
- **1 to 3 vs 1 to 2**: *β* = -0.49, *SE* = 0.407, *z* = -1.213, *p* = 0.225
- **1 to 4 vs 1 to 2**: *β* = -0.94, *SE* = 0.409, *z* = -2.291, *p* = 0.022
- **SNR**: *β* = -0.38, *SE* = 0.085, *z* = -4.491, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.49 | 0.41 | 1.21 | 0.225 | 0.400 | n.s. |
| 1 to 2 - 1 to 4 | 0.94 | 0.41 | 2.29 | 0.022 | 0.064 | n.s. |
| 1 to 3 - 1 to 4 | 0.44 | 0.40 | 1.09 | 0.274 | 0.400 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.21, *p* = 0.124, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.40 | 18 | = 0.082 | 0.39 [0.10, 1.09] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.81 | 18 | = 0.130 | 0.35 [-0.09, 0.92] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.10 | 18 | = 0.920 | -0.02 [-0.47, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.64, BIC = 284.97
- **1 to 3 vs 1 to 2**: *β* = -3.04, *SE* = 4.933, *z* = -0.617, *p* = 0.537
- **1 to 4 vs 1 to 2**: *β* = 1.21, *SE* = 4.378, *z* = 0.276, *p* = 0.782
- **SNR**: *β* = 0.84, *SE* = 1.291, *z* = 0.651, *p* = 0.515

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 3.04 | 4.93 | 0.62 | 0.537 | 0.786 | n.s. |
| 1 to 2 - 1 to 4 | -1.21 | 4.38 | -0.28 | 0.782 | 0.786 | n.s. |
| 1 to 3 - 1 to 4 | -4.25 | 4.34 | -0.98 | 0.328 | 0.696 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.06, *p* = 0.208, η²_G = 0.330
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.90 | 3 | = 0.432 | 0.51 [-0.48, 1.84] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -1.57 | 3 | = 0.323 | -1.11 [-2.05, 0.70] | large | n.s. |
| 1 to 3 vs 1 to 4 | -1.59 | 3 | = 0.323 | -1.46 [-0.98, 0.70] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 126.81, BIC = 136.14
- **1 to 3 vs 1 to 2**: *β* = 0.30, *SE* = 0.592, *z* = 0.514, *p* = 0.607
- **1 to 4 vs 1 to 2**: *β* = 0.09, *SE* = 0.526, *z* = 0.172, *p* = 0.864
- **SNR**: *β* = 0.45, *SE* = 0.146, *z* = 3.102, *p* = 0.002

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.30 | 0.59 | -0.51 | 0.607 | 0.939 | n.s. |
| 1 to 2 - 1 to 4 | -0.09 | 0.53 | -0.17 | 0.864 | 0.939 | n.s. |
| 1 to 3 - 1 to 4 | 0.21 | 0.51 | 0.42 | 0.677 | 0.939 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.696, η²_G = 0.103
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.31 | 3 | = 0.776 | -0.26 [-1.02, 1.08] | small | n.s. |
| 1 to 2 vs 1 to 4 | 0.85 | 3 | = 0.776 | 0.63 [-1.10, 1.40] | medium | n.s. |
| 1 to 3 vs 1 to 4 | 0.72 | 3 | = 0.776 | 0.60 [-0.73, 0.94] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 591.27, BIC = 603.21
- **1 to 3 vs 1 to 2**: *β* = 31.93, *SE* = 17.662, *z* = 1.808, *p* = 0.071
- **1 to 4 vs 1 to 2**: *β* = 22.30, *SE* = 17.378, *z* = 1.283, *p* = 0.199
- **SNR**: *β* = -1.07, *SE* = 2.724, *z* = -0.392, *p* = 0.695

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -31.93 | 17.66 | -1.81 | 0.071 | 0.197 | n.s. |
| 1 to 2 - 1 to 4 | -22.30 | 17.38 | -1.28 | 0.199 | 0.359 | n.s. |
| 1 to 3 - 1 to 4 | 9.62 | 16.11 | 0.60 | 0.550 | 0.550 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.292, η²_G = 0.058
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.34 | 13 | = 0.307 | -0.52 [-0.95, 0.24] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -1.34 | 13 | = 0.307 | -0.49 [-0.76, 0.36] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.02 | 13 | = 0.987 | -0.01 [-0.39, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 242.88, BIC = 254.81
- **1 to 3 vs 1 to 2**: *β* = 0.17, *SE* = 0.562, *z* = 0.294, *p* = 0.769
- **1 to 4 vs 1 to 2**: *β* = 0.30, *SE* = 0.545, *z* = 0.553, *p* = 0.580
- **SNR**: *β* = 0.54, *SE* = 0.120, *z* = 4.447, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.16 | 0.56 | -0.29 | 0.769 | 0.947 | n.s. |
| 1 to 2 - 1 to 4 | -0.30 | 0.55 | -0.55 | 0.580 | 0.926 | n.s. |
| 1 to 3 - 1 to 4 | -0.14 | 0.50 | -0.28 | 0.783 | 0.947 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.428, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.97 | 13 | = 0.522 | -0.22 [-0.85, 0.33] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.17 | 13 | = 0.522 | -0.26 [-0.89, 0.24] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.09 | 13 | = 0.926 | -0.02 [-0.46, 0.50] | negligible | n.s. |

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
