# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:19:58

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
| 1 to 2 | 24 | 89.17 ms | 11.03 | 2.25 | [76.00, 104.00] |
| 1 to 3 | 24 | 89.33 ms | 12.12 | 2.47 | [76.00, 104.00] |
| 1 to 4 | 24 | 95.67 ms | 9.93 | 2.03 | [76.00, 104.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -0.65 µV | 1.90 | 0.39 | [-3.40, 3.95] |
| 1 to 3 | 24 | -0.54 µV | 2.41 | 0.49 | [-5.86, 4.44] |
| 1 to 4 | 24 | -1.29 µV | 1.94 | 0.40 | [-4.33, 3.17] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 175.00 ms | 20.54 | 4.19 | [144.00, 216.00] |
| 1 to 3 | 24 | 170.00 ms | 24.57 | 5.02 | [136.00, 216.00] |
| 1 to 4 | 24 | 173.00 ms | 20.13 | 4.11 | [136.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -5.53 µV | 2.34 | 0.48 | [-10.03, -0.30] |
| 1 to 3 | 24 | -6.37 µV | 2.63 | 0.54 | [-12.53, -2.34] |
| 1 to 4 | 24 | -6.41 µV | 3.21 | 0.65 | [-13.14, -1.20] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 83.67 ms | 12.64 | 2.58 | [68.00, 100.00] |
| 1 to 3 | 24 | 83.67 ms | 13.02 | 2.66 | [68.00, 100.00] |
| 1 to 4 | 24 | 90.83 ms | 10.25 | 2.09 | [68.00, 100.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 1.14 µV | 2.03 | 0.41 | [-2.48, 4.29] |
| 1 to 3 | 24 | 1.45 µV | 2.27 | 0.46 | [-2.33, 7.47] |
| 1 to 4 | 24 | 1.75 µV | 1.72 | 0.35 | [-1.51, 4.28] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 459.17 ms | 53.73 | 10.97 | [368.00, 536.00] |
| 1 to 3 | 24 | 451.00 ms | 42.89 | 8.76 | [368.00, 516.00] |
| 1 to 4 | 24 | 465.17 ms | 53.67 | 10.96 | [376.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 4.49 µV | 3.77 | 0.77 | [-3.51, 11.99] |
| 1 to 3 | 24 | 5.43 µV | 4.12 | 0.84 | [-1.55, 14.25] |
| 1 to 4 | 24 | 5.18 µV | 3.70 | 0.76 | [-0.58, 13.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 549.46, BIC = 563.12
- **1 to 3 vs 1 to 2**: *β* = 0.05, *SE* = 2.477, *z* = 0.019, *p* = 0.985
- **1 to 4 vs 1 to 2**: *β* = 6.43, *SE* = 2.470, *z* = 2.604, *p* = 0.009
- **SNR**: *β* = 0.48, *SE* = 0.919, *z* = 0.528, *p* = 0.598

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.05 | 2.48 | -0.02 | 0.985 | 0.985 | n.s. |
| 1 to 2 - 1 to 4 | -6.43 | 2.47 | -2.60 | 0.009 | 0.027 | * |
| 1 to 3 - 1 to 4 | -6.38 | 2.47 | -2.59 | 0.010 | 0.027 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.38, *p* = 0.018, η²_G = 0.072
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.08 | 23 | = 0.935 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -2.61 | 23 | = 0.047 | -0.62 [-0.98, -0.08] | medium | * |
| 1 to 3 vs 1 to 4 | -2.16 | 23 | = 0.062 | -0.57 [-0.88, 0.00] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 319.01, BIC = 332.67
- **1 to 3 vs 1 to 2**: *β* = 0.07, *SE* = 0.587, *z* = 0.110, *p* = 0.912
- **1 to 4 vs 1 to 2**: *β* = -0.67, *SE* = 0.586, *z* = -1.135, *p* = 0.256
- **SNR**: *β* = 0.16, *SE* = 0.182, *z* = 0.887, *p* = 0.375

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.06 | 0.59 | -0.11 | 0.912 | 0.912 | n.s. |
| 1 to 2 - 1 to 4 | 0.67 | 0.59 | 1.13 | 0.256 | 0.512 | n.s. |
| 1 to 3 - 1 to 4 | 0.73 | 0.59 | 1.25 | 0.213 | 0.512 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.409, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.21 | 23 | = 0.836 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 1.15 | 23 | = 0.464 | 0.33 [-0.19, 0.66] | small | n.s. |
| 1 to 3 vs 1 to 4 | 1.04 | 23 | = 0.464 | 0.34 [-0.21, 0.64] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 637.92, BIC = 651.58
- **1 to 3 vs 1 to 2**: *β* = -3.29, *SE* = 4.345, *z* = -0.758, *p* = 0.449
- **1 to 4 vs 1 to 2**: *β* = -1.08, *SE* = 4.268, *z* = -0.253, *p* = 0.800
- **SNR**: *β* = -1.60, *SE* = 0.905, *z* = -1.765, *p* = 0.078

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 3.29 | 4.34 | 0.76 | 0.449 | 0.832 | n.s. |
| 1 to 2 - 1 to 4 | 1.08 | 4.27 | 0.25 | 0.800 | 0.843 | n.s. |
| 1 to 3 - 1 to 4 | -2.21 | 4.26 | -0.52 | 0.604 | 0.843 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.536, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 1.04 | 23 | = 0.649 | 0.22 [-0.21, 0.64] | small | n.s. |
| 1 to 2 vs 1 to 4 | 0.42 | 23 | = 0.681 | 0.10 [-0.34, 0.51] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -0.80 | 23 | = 0.649 | -0.13 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 310.82, BIC = 324.48
- **1 to 3 vs 1 to 2**: *β* = -0.31, *SE* = 0.453, *z* = -0.674, *p* = 0.500
- **1 to 4 vs 1 to 2**: *β* = -0.60, *SE* = 0.445, *z* = -1.338, *p* = 0.181
- **SNR**: *β* = -0.50, *SE* = 0.096, *z* = -5.185, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.31 | 0.45 | 0.67 | 0.500 | 0.750 | n.s. |
| 1 to 2 - 1 to 4 | 0.60 | 0.45 | 1.34 | 0.181 | 0.450 | n.s. |
| 1 to 3 - 1 to 4 | 0.29 | 0.44 | 0.65 | 0.514 | 0.750 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.94, *p* = 0.155, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.15 | 23 | = 0.128 | 0.34 [-0.00, 0.88] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.52 | 23 | = 0.214 | 0.31 [-0.12, 0.74] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.08 | 23 | = 0.934 | 0.01 [-0.41, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 570.22, BIC = 583.88
- **1 to 3 vs 1 to 2**: *β* = 0.10, *SE* = 3.186, *z* = 0.032, *p* = 0.975
- **1 to 4 vs 1 to 2**: *β* = 7.22, *SE* = 3.172, *z* = 2.275, *p* = 0.023
- **SNR**: *β* = 0.29, *SE* = 0.999, *z* = 0.293, *p* = 0.770

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.10 | 3.19 | -0.03 | 0.975 | 0.975 | n.s. |
| 1 to 2 - 1 to 4 | -7.22 | 3.17 | -2.28 | 0.023 | 0.067 | n.s. |
| 1 to 3 - 1 to 4 | -7.12 | 3.17 | -2.24 | 0.025 | 0.067 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.28, *p* = 0.047, η²_G = 0.076
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -2.28 | 23 | = 0.061 | -0.62 [-0.91, -0.02] | medium | n.s. |
| 1 to 3 vs 1 to 4 | -2.17 | 23 | = 0.061 | -0.61 [-0.89, -0.00] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 311.65, BIC = 325.31
- **1 to 3 vs 1 to 2**: *β* = 0.40, *SE* = 0.542, *z* = 0.736, *p* = 0.462
- **1 to 4 vs 1 to 2**: *β* = 0.66, *SE* = 0.539, *z* = 1.215, *p* = 0.224
- **SNR**: *β* = 0.25, *SE* = 0.167, *z* = 1.494, *p* = 0.135

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.40 | 0.54 | -0.74 | 0.462 | 0.710 | n.s. |
| 1 to 2 - 1 to 4 | -0.66 | 0.54 | -1.21 | 0.224 | 0.534 | n.s. |
| 1 to 3 - 1 to 4 | -0.26 | 0.54 | -0.48 | 0.634 | 0.710 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.60, *p* = 0.552, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.53 | 23 | = 0.618 | -0.15 [-0.53, 0.32] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.26 | 23 | = 0.618 | -0.33 [-0.69, 0.17] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.51 | 23 | = 0.618 | -0.15 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 777.08, BIC = 790.74
- **1 to 3 vs 1 to 2**: *β* = -7.89, *SE* = 13.762, *z* = -0.574, *p* = 0.566
- **1 to 4 vs 1 to 2**: *β* = 6.21, *SE* = 13.710, *z* = 0.453, *p* = 0.651
- **SNR**: *β* = -0.34, *SE* = 2.215, *z* = -0.151, *p* = 0.880

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 7.89 | 13.76 | 0.57 | 0.566 | 0.812 | n.s. |
| 1 to 2 - 1 to 4 | -6.20 | 13.71 | -0.45 | 0.651 | 0.812 | n.s. |
| 1 to 3 - 1 to 4 | -14.10 | 13.65 | -1.03 | 0.302 | 0.659 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.52, *p* = 0.596, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.56 | 23 | = 0.651 | 0.17 [-0.31, 0.54] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.46 | 23 | = 0.651 | -0.11 [-0.52, 0.33] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.01 | 23 | = 0.651 | -0.29 [-0.63, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 366.34, BIC = 380.00
- **1 to 3 vs 1 to 2**: *β* = 0.70, *SE* = 0.616, *z* = 1.130, *p* = 0.258
- **1 to 4 vs 1 to 2**: *β* = 0.50, *SE* = 0.612, *z* = 0.822, *p* = 0.411
- **SNR**: *β* = 0.29, *SE* = 0.131, *z* = 2.229, *p* = 0.026

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.70 | 0.62 | -1.13 | 0.258 | 0.592 | n.s. |
| 1 to 2 - 1 to 4 | -0.50 | 0.61 | -0.82 | 0.411 | 0.653 | n.s. |
| 1 to 3 - 1 to 4 | 0.19 | 0.61 | 0.32 | 0.751 | 0.751 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.24, *p* = 0.300, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.42 | 23 | = 0.464 | -0.24 [-0.72, 0.14] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.04 | 23 | = 0.464 | -0.18 [-0.64, 0.21] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.49 | 23 | = 0.631 | 0.06 [-0.32, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.018). Post-hoc tests revealed:
  - 1 to 2 showed smaller latency than 1 to 4 (*d* = -0.62)
**P1 latency:** Significant main effect of condition (*p* = 0.047) (no significant pairwise comparisons)

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
