# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:26:39

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
| Increasing Crossover | 24 | 98.17 ms | 9.36 | 1.91 | [84.00, 108.00] |
| Increasing Large | 24 | 95.67 ms | 9.21 | 1.88 | [84.00, 108.00] |
| Increasing Small | 24 | 92.33 ms | 9.36 | 1.91 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | -1.19 µV | 0.90 | 0.18 | [-4.07, 0.08] |
| Increasing Large | 24 | -1.90 µV | 1.82 | 0.37 | [-5.60, 2.40] |
| Increasing Small | 24 | -0.47 µV | 1.50 | 0.31 | [-3.77, 2.61] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 170.83 ms | 20.75 | 4.24 | [136.00, 208.00] |
| Increasing Large | 24 | 168.17 ms | 20.98 | 4.28 | [136.00, 200.00] |
| Increasing Small | 24 | 171.50 ms | 20.95 | 4.28 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | -5.60 µV | 2.25 | 0.46 | [-10.54, -0.89] |
| Increasing Large | 24 | -6.06 µV | 3.41 | 0.70 | [-14.92, 0.07] |
| Increasing Small | 24 | -5.31 µV | 2.22 | 0.45 | [-10.86, -0.77] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 97.83 ms | 10.48 | 2.14 | [80.00, 108.00] |
| Increasing Large | 24 | 94.50 ms | 11.36 | 2.32 | [80.00, 108.00] |
| Increasing Small | 24 | 94.00 ms | 12.26 | 2.50 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 1.46 µV | 1.34 | 0.27 | [-0.68, 5.19] |
| Increasing Large | 24 | 1.91 µV | 2.42 | 0.49 | [-1.97, 6.45] |
| Increasing Small | 24 | 0.84 µV | 1.48 | 0.30 | [-1.50, 3.56] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 487.00 ms | 35.49 | 7.24 | [428.00, 536.00] |
| Increasing Large | 24 | 488.83 ms | 38.40 | 7.84 | [428.00, 536.00] |
| Increasing Small | 24 | 472.83 ms | 33.78 | 6.89 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 3.48 µV | 3.03 | 0.62 | [-1.79, 8.97] |
| Increasing Large | 24 | 3.84 µV | 3.56 | 0.73 | [-3.13, 10.58] |
| Increasing Small | 24 | 3.74 µV | 3.52 | 0.72 | [-2.32, 11.98] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 526.68, BIC = 540.34
- **Increasing Large vs Increasing Crossover**: *β* = -2.45, *SE* = 2.207, *z* = -1.110, *p* = 0.267
- **Increasing Small vs Increasing Crossover**: *β* = -6.15, *SE* = 2.217, *z* = -2.773, *p* = 0.006
- **SNR**: *β* = 1.20, *SE* = 0.811, *z* = 1.480, *p* = 0.139

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 2.45 | 2.21 | 1.11 | 0.267 | 0.267 | n.s. |
| Increasing Crossover - Increasing Small | 6.15 | 2.22 | 2.77 | 0.006 | 0.017 | * |
| Increasing Large - Increasing Small | 3.70 | 2.22 | 1.67 | 0.096 | 0.182 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.36, *p* = 0.043, η²_G = 0.064
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.10 | 23 | = 0.282 | 0.27 [-0.20, 0.65] | small | n.s. |
| Increasing Crossover vs Increasing Small | 2.78 | 23 | = 0.032 | 0.62 [0.11, 1.02] | medium | * |
| Increasing Large vs Increasing Small | 1.39 | 23 | = 0.265 | 0.36 [-0.15, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 258.72, BIC = 272.38
- **Increasing Large vs Increasing Crossover**: *β* = -0.72, *SE* = 0.355, *z* = -2.041, *p* = 0.041
- **Increasing Small vs Increasing Crossover**: *β* = 0.80, *SE* = 0.357, *z* = 2.253, *p* = 0.024
- **SNR**: *β* = -0.31, *SE* = 0.125, *z* = -2.492, *p* = 0.013

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.73 | 0.36 | 2.04 | 0.041 | 0.048 | * |
| Increasing Crossover - Increasing Small | -0.80 | 0.36 | -2.25 | 0.024 | 0.048 | * |
| Increasing Large - Increasing Small | -1.53 | 0.36 | -4.28 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.31, *p* = 0.002, η²_G = 0.144
- Greenhouse-Geisser corrected: *p* = 0.006 (ε = 0.692)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 2.14 | 23 | = 0.043 | 0.50 [-0.00, 0.88] | small | * |
| Increasing Crossover vs Increasing Small | -2.57 | 23 | = 0.026 | -0.58 [-0.97, -0.07] | medium | * |
| Increasing Large vs Increasing Small | -2.97 | 23 | = 0.020 | -0.86 [-1.07, -0.15] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 612.76, BIC = 626.42
- **Increasing Large vs Increasing Crossover**: *β* = -1.53, *SE* = 3.382, *z* = -0.452, *p* = 0.651
- **Increasing Small vs Increasing Crossover**: *β* = 1.88, *SE* = 3.415, *z* = 0.552, *p* = 0.581
- **SNR**: *β* = 0.36, *SE* = 0.391, *z* = 0.914, *p* = 0.361

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.53 | 3.38 | 0.45 | 0.651 | 0.825 | n.s. |
| Increasing Crossover - Increasing Small | -1.88 | 3.41 | -0.55 | 0.581 | 0.825 | n.s. |
| Increasing Large - Increasing Small | -3.41 | 3.15 | -1.08 | 0.278 | 0.624 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.58, *p* = 0.565, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.501 (ε = 0.669)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.48 | 23 | = 0.454 | 0.13 [-0.13, 0.73] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.18 | 23 | = 0.860 | -0.03 [-0.46, 0.39] | negligible | n.s. |
| Increasing Large vs Increasing Small | -0.86 | 23 | = 0.601 | -0.16 [-0.60, 0.25] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 308.72, BIC = 322.38
- **Increasing Large vs Increasing Crossover**: *β* = -1.12, *SE* = 0.449, *z* = -2.487, *p* = 0.013
- **Increasing Small vs Increasing Crossover**: *β* = -0.41, *SE* = 0.453, *z* = -0.893, *p* = 0.372
- **SNR**: *β* = -0.21, *SE* = 0.050, *z* = -4.125, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.12 | 0.45 | 2.49 | 0.013 | 0.038 | * |
| Increasing Crossover - Increasing Small | 0.40 | 0.45 | 0.89 | 0.372 | 0.372 | n.s. |
| Increasing Large - Increasing Small | -0.71 | 0.42 | -1.70 | 0.090 | 0.172 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.40, *p* = 0.258, η²_G = 0.014
- Greenhouse-Geisser corrected: *p* = 0.256 (ε = 0.655)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.14 | 23 | = 0.369 | 0.16 [-0.20, 0.66] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.92 | 23 | = 0.369 | -0.13 [-0.61, 0.24] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.27 | 23 | = 0.369 | -0.26 [-0.69, 0.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.14, BIC = 563.80
- **Increasing Large vs Increasing Crossover**: *β* = -2.96, *SE* = 2.496, *z* = -1.184, *p* = 0.236
- **Increasing Small vs Increasing Crossover**: *β* = -3.73, *SE* = 2.492, *z* = -1.498, *p* = 0.134
- **SNR**: *β* = 1.65, *SE* = 0.644, *z* = 2.568, *p* = 0.010

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 2.96 | 2.50 | 1.18 | 0.236 | 0.417 | n.s. |
| Increasing Crossover - Increasing Small | 3.73 | 2.49 | 1.50 | 0.134 | 0.351 | n.s. |
| Increasing Large - Increasing Small | 0.78 | 2.49 | 0.31 | 0.755 | 0.755 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.20, *p* = 0.309, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.43 | 23 | = 0.249 | 0.30 [-0.14, 0.72] | small | n.s. |
| Increasing Crossover vs Increasing Small | 1.48 | 23 | = 0.249 | 0.34 [-0.13, 0.73] | small | n.s. |
| Increasing Large vs Increasing Small | 0.16 | 23 | = 0.872 | 0.04 [-0.39, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 292.24, BIC = 305.90
- **Increasing Large vs Increasing Crossover**: *β* = 0.48, *SE* = 0.432, *z* = 1.108, *p* = 0.268
- **Increasing Small vs Increasing Crossover**: *β* = -0.61, *SE* = 0.431, *z* = -1.424, *p* = 0.154
- **SNR**: *β* = 0.12, *SE* = 0.110, *z* = 1.114, *p* = 0.265

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.48 | 0.43 | -1.11 | 0.268 | 0.285 | n.s. |
| Increasing Crossover - Increasing Small | 0.61 | 0.43 | 1.42 | 0.154 | 0.285 | n.s. |
| Increasing Large - Increasing Small | 1.09 | 0.43 | 2.53 | 0.011 | 0.034 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.97, *p* = 0.061, η²_G = 0.058
- Greenhouse-Geisser corrected: *p* = 0.084 (ε = 0.665)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -1.05 | 23 | = 0.306 | -0.23 [-0.64, 0.21] | small | n.s. |
| Increasing Crossover vs Increasing Small | 2.19 | 23 | = 0.106 | 0.44 [0.00, 0.89] | small | n.s. |
| Increasing Large vs Increasing Small | 1.90 | 23 | = 0.106 | 0.53 [-0.05, 0.83] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 724.28, BIC = 737.94
- **Increasing Large vs Increasing Crossover**: *β* = 1.18, *SE* = 8.912, *z* = 0.133, *p* = 0.895
- **Increasing Small vs Increasing Crossover**: *β* = -14.30, *SE* = 8.692, *z* = -1.646, *p* = 0.100
- **SNR**: *β* = -0.28, *SE* = 0.876, *z* = -0.324, *p* = 0.746

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -1.18 | 8.91 | -0.13 | 0.895 | 0.895 | n.s. |
| Increasing Crossover - Increasing Small | 14.30 | 8.69 | 1.65 | 0.100 | 0.220 | n.s. |
| Increasing Large - Increasing Small | 15.49 | 8.83 | 1.75 | 0.079 | 0.220 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.95, *p* = 0.154, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -0.18 | 23 | = 0.858 | -0.05 [-0.46, 0.39] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 1.79 | 23 | = 0.130 | 0.41 [-0.07, 0.80] | small | n.s. |
| Increasing Large vs Increasing Small | 1.90 | 23 | = 0.130 | 0.44 [-0.05, 0.83] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.05, BIC = 328.71
- **Increasing Large vs Increasing Crossover**: *β* = 0.64, *SE* = 0.377, *z* = 1.704, *p* = 0.088
- **Increasing Small vs Increasing Crossover**: *β* = 0.33, *SE* = 0.361, *z* = 0.901, *p* = 0.368
- **SNR**: *β* = 0.12, *SE* = 0.048, *z* = 2.533, *p* = 0.011

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.64 | 0.38 | -1.70 | 0.088 | 0.242 | n.s. |
| Increasing Crossover - Increasing Small | -0.33 | 0.36 | -0.90 | 0.368 | 0.600 | n.s. |
| Increasing Large - Increasing Small | 0.32 | 0.37 | 0.85 | 0.393 | 0.600 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.50, *p* = 0.612, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -1.08 | 23 | = 0.648 | -0.11 [-0.65, 0.21] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.80 | 23 | = 0.648 | -0.08 [-0.59, 0.26] | negligible | n.s. |
| Increasing Large vs Increasing Small | 0.21 | 23 | = 0.832 | 0.03 [-0.38, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.043). Post-hoc tests revealed:
  - Increasing Crossover showed greater latency than Increasing Small (*d* = 0.62)
**Fz amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Increasing Crossover showed greater amplitude than Increasing Large (*d* = 0.50)
  - Increasing Crossover showed smaller amplitude than Increasing Small (*d* = -0.58)
  - Increasing Large showed smaller amplitude than Increasing Small (*d* = -0.86)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.061)

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
