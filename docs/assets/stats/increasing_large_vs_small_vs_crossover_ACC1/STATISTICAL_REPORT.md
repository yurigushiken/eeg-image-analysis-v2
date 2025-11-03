# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:45:33

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
| Increasing Crossover | 17 | 97.41 ms | 9.27 | 2.25 | [84.00, 108.00] |
| Increasing Large | 17 | 98.12 ms | 8.85 | 2.15 | [84.00, 108.00] |
| Increasing Small | 11 | 94.18 ms | 9.69 | 2.92 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 17 | -1.49 µV | 0.88 | 0.21 | [-4.07, -0.46] |
| Increasing Large | 17 | -2.59 µV | 1.49 | 0.36 | [-5.60, -0.75] |
| Increasing Small | 11 | -1.73 µV | 1.03 | 0.31 | [-3.77, -0.62] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 23 | 169.22 ms | 19.61 | 4.09 | [136.00, 208.00] |
| Increasing Large | 22 | 167.64 ms | 20.80 | 4.43 | [136.00, 200.00] |
| Increasing Small | 23 | 170.26 ms | 20.50 | 4.27 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 23 | -5.81 µV | 2.05 | 0.43 | [-10.54, -2.66] |
| Increasing Large | 22 | -6.55 µV | 3.11 | 0.66 | [-14.92, -2.97] |
| Increasing Small | 23 | -5.50 µV | 2.05 | 0.43 | [-10.86, -1.45] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 98.93 ms | 9.25 | 2.39 | [80.00, 108.00] |
| Increasing Large | 14 | 96.29 ms | 11.58 | 3.09 | [80.00, 108.00] |
| Increasing Small | 12 | 98.00 ms | 9.87 | 2.85 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 1.84 µV | 1.35 | 0.35 | [0.50, 5.19] |
| Increasing Large | 14 | 3.34 µV | 1.90 | 0.51 | [1.15, 6.45] |
| Increasing Small | 12 | 1.98 µV | 1.10 | 0.32 | [0.58, 3.56] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 487.37 ms | 36.67 | 8.41 | [428.00, 536.00] |
| Increasing Large | 15 | 489.60 ms | 37.76 | 9.75 | [436.00, 536.00] |
| Increasing Small | 20 | 476.60 ms | 34.88 | 7.80 | [436.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 4.52 µV | 2.45 | 0.56 | [0.94, 8.97] |
| Increasing Large | 15 | 5.93 µV | 2.64 | 0.68 | [1.73, 10.58] |
| Increasing Small | 20 | 4.71 µV | 2.99 | 0.67 | [0.63, 11.98] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 329.99, BIC = 340.83
- **Increasing Large vs Increasing Crossover**: *β* = 0.61, *SE* = 2.470, *z* = 0.247, *p* = 0.805
- **Increasing Small vs Increasing Crossover**: *β* = -3.83, *SE* = 2.761, *z* = -1.387, *p* = 0.165
- **SNR**: *β* = 1.18, *SE* = 0.956, *z* = 1.234, *p* = 0.217

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.61 | 2.47 | -0.25 | 0.805 | 0.805 | n.s. |
| Increasing Crossover - Increasing Small | 3.83 | 2.76 | 1.39 | 0.165 | 0.329 | n.s. |
| Increasing Large - Increasing Small | 4.44 | 2.89 | 1.54 | 0.124 | 0.329 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.414, η²_G = 0.074
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.11 | 6 | = 0.919 | 0.06 [-0.52, 0.69] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 1.47 | 6 | = 0.408 | 0.55 [-0.31, 1.19] | medium | n.s. |
| Increasing Large vs Increasing Small | 1.21 | 6 | = 0.408 | 0.51 [-0.51, 1.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 137.34, BIC = 148.18
- **Increasing Large vs Increasing Crossover**: *β* = -1.25, *SE* = 0.305, *z* = -4.087, *p* < .001
- **Increasing Small vs Increasing Crossover**: *β* = -0.22, *SE* = 0.343, *z* = -0.628, *p* = 0.530
- **SNR**: *β* = -0.40, *SE* = 0.112, *z* = -3.533, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.25 | 0.31 | 4.09 | < .001 | < .001 | *** |
| Increasing Crossover - Increasing Small | 0.22 | 0.34 | 0.63 | 0.530 | 0.530 | n.s. |
| Increasing Large - Increasing Small | -1.03 | 0.36 | -2.91 | 0.004 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.07, *p* = 0.169, η²_G = 0.125
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.36 | 6 | = 0.332 | 0.58 [0.03, 1.37] | medium | n.s. |
| Increasing Crossover vs Increasing Small | -0.61 | 6 | = 0.563 | -0.19 [-0.48, 0.97] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.63 | 6 | = 0.332 | -0.75 [-1.62, 0.39] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 583.21, BIC = 596.52
- **Increasing Large vs Increasing Crossover**: *β* = -0.33, *SE* = 3.700, *z* = -0.090, *p* = 0.929
- **Increasing Small vs Increasing Crossover**: *β* = 2.30, *SE* = 3.668, *z* = 0.627, *p* = 0.531
- **SNR**: *β* = 0.40, *SE* = 0.410, *z* = 0.978, *p* = 0.328

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.33 | 3.70 | 0.09 | 0.929 | 0.929 | n.s. |
| Increasing Crossover - Increasing Small | -2.30 | 3.67 | -0.63 | 0.531 | 0.825 | n.s. |
| Increasing Large - Increasing Small | -2.63 | 3.41 | -0.77 | 0.440 | 0.825 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.09, *p* = 0.916, η²_G = 0.001
- Greenhouse-Geisser corrected: *p* = 0.826 (ε = 0.632)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.53 | 19 | = 0.894 | 0.05 [-0.25, 0.67] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.13 | 19 | = 0.894 | -0.03 [-0.50, 0.39] | negligible | n.s. |
| Increasing Large vs Increasing Small | -0.35 | 19 | = 0.894 | -0.08 [-0.55, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.70, BIC = 289.02
- **Increasing Large vs Increasing Crossover**: *β* = -1.43, *SE* = 0.396, *z* = -3.609, *p* < .001
- **Increasing Small vs Increasing Crossover**: *β* = -0.46, *SE* = 0.393, *z* = -1.168, *p* = 0.243
- **SNR**: *β* = -0.19, *SE* = 0.043, *z* = -4.411, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.43 | 0.40 | 3.61 | < .001 | < .001 | *** |
| Increasing Crossover - Increasing Small | 0.46 | 0.39 | 1.17 | 0.243 | 0.243 | n.s. |
| Increasing Large - Increasing Small | -0.97 | 0.37 | -2.64 | 0.008 | 0.016 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.08, *p* = 0.139, η²_G = 0.025
- Greenhouse-Geisser corrected: *p* = 0.158 (ε = 0.660)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.76 | 19 | = 0.215 | 0.23 [-0.02, 0.93] | small | n.s. |
| Increasing Crossover vs Increasing Small | -0.77 | 19 | = 0.449 | -0.15 [-0.60, 0.29] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.53 | 19 | = 0.215 | -0.34 [-0.83, 0.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 310.06, BIC = 320.34
- **Increasing Large vs Increasing Crossover**: *β* = -1.45, *SE* = 3.447, *z* = -0.419, *p* = 0.675
- **Increasing Small vs Increasing Crossover**: *β* = 0.17, *SE* = 3.349, *z* = 0.051, *p* = 0.959
- **SNR**: *β* = 1.96, *SE* = 0.760, *z* = 2.574, *p* = 0.010

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.45 | 3.45 | 0.42 | 0.675 | 0.960 | n.s. |
| Increasing Crossover - Increasing Small | -0.17 | 3.35 | -0.05 | 0.959 | 0.960 | n.s. |
| Increasing Large - Increasing Small | -1.62 | 3.65 | -0.44 | 0.658 | 0.960 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.65, *p* = 0.119, η²_G = 0.246
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 2.08 | 5 | = 0.227 | 1.18 [-0.35, 1.27] | large | n.s. |
| Increasing Crossover vs Increasing Small | 0.15 | 5 | = 0.886 | 0.07 [-0.48, 0.88] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.69 | 5 | = 0.227 | -1.05 [-1.63, 0.39] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 142.38, BIC = 152.67
- **Increasing Large vs Increasing Crossover**: *β* = 1.65, *SE* = 0.421, *z* = 3.904, *p* < .001
- **Increasing Small vs Increasing Crossover**: *β* = 0.33, *SE* = 0.388, *z* = 0.852, *p* = 0.394
- **SNR**: *β* = 0.33, *SE* = 0.100, *z* = 3.319, *p* = 0.001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -1.64 | 0.42 | -3.90 | < .001 | < .001 | *** |
| Increasing Crossover - Increasing Small | -0.33 | 0.39 | -0.85 | 0.394 | 0.394 | n.s. |
| Increasing Large - Increasing Small | 1.31 | 0.44 | 3.01 | 0.003 | 0.005 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.03, *p* = 0.031, η²_G = 0.131
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -0.29 | 5 | = 0.784 | -0.07 [-1.28, 0.34] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 3.60 | 5 | = 0.047 | 0.74 [-0.59, 0.75] | medium | * |
| Increasing Large vs Increasing Small | 2.26 | 5 | = 0.110 | 0.84 [-0.30, 1.80] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 545.59, BIC = 557.52
- **Increasing Large vs Increasing Crossover**: *β* = 5.13, *SE* = 10.610, *z* = 0.484, *p* = 0.628
- **Increasing Small vs Increasing Crossover**: *β* = -9.02, *SE* = 9.471, *z* = -0.952, *p* = 0.341
- **SNR**: *β* = 0.30, *SE* = 1.003, *z* = 0.295, *p* = 0.768

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -5.13 | 10.61 | -0.48 | 0.628 | 0.628 | n.s. |
| Increasing Crossover - Increasing Small | 9.02 | 9.47 | 0.95 | 0.341 | 0.566 | n.s. |
| Increasing Large - Increasing Small | 14.15 | 10.47 | 1.35 | 0.176 | 0.442 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.518, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -0.66 | 13 | = 0.644 | -0.24 [-0.69, 0.43] | small | n.s. |
| Increasing Crossover vs Increasing Small | 0.47 | 13 | = 0.644 | 0.14 [-0.35, 0.65] | negligible | n.s. |
| Increasing Large vs Increasing Small | 1.14 | 13 | = 0.644 | 0.37 [-0.29, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 224.30, BIC = 236.23
- **Increasing Large vs Increasing Crossover**: *β* = 1.37, *SE* = 0.444, *z* = 3.080, *p* = 0.002
- **Increasing Small vs Increasing Crossover**: *β* = 0.43, *SE* = 0.375, *z* = 1.161, *p* = 0.246
- **SNR**: *β* = 0.15, *SE* = 0.053, *z* = 2.824, *p* = 0.005

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -1.37 | 0.44 | -3.08 | 0.002 | 0.006 | ** |
| Increasing Crossover - Increasing Small | -0.43 | 0.37 | -1.16 | 0.246 | 0.246 | n.s. |
| Increasing Large - Increasing Small | 0.93 | 0.45 | 2.08 | 0.038 | 0.074 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.09, *p* = 0.353, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -1.43 | 13 | = 0.478 | -0.28 [-0.97, 0.18] | small | n.s. |
| Increasing Crossover vs Increasing Small | -0.35 | 13 | = 0.731 | -0.06 [-0.80, 0.22] | negligible | n.s. |
| Increasing Large vs Increasing Small | 1.04 | 13 | = 0.478 | 0.18 [-0.31, 0.87] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.031). Post-hoc tests revealed:
  - Increasing Crossover showed smaller amplitude than Increasing Small (*d* = 0.74)

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
