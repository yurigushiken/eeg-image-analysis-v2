# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:26:48

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
| Increasing Crossover (no 1) | 24 | 101.50 ms | 9.86 | 2.01 | [84.00, 112.00] |
| Increasing Large (no 1) | 24 | 97.83 ms | 9.80 | 2.00 | [84.00, 112.00] |
| Increasing Small (no 1) | 24 | 97.50 ms | 11.12 | 2.27 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | -1.22 µV | 1.16 | 0.24 | [-5.10, 0.48] |
| Increasing Large (no 1) | 24 | -1.24 µV | 1.34 | 0.27 | [-3.44, 1.53] |
| Increasing Small (no 1) | 24 | -1.49 µV | 2.02 | 0.41 | [-5.76, 2.45] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 170.33 ms | 19.94 | 4.07 | [136.00, 204.00] |
| Increasing Large (no 1) | 24 | 168.67 ms | 19.23 | 3.92 | [136.00, 200.00] |
| Increasing Small (no 1) | 24 | 170.83 ms | 20.72 | 4.23 | [136.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | -5.36 µV | 2.15 | 0.44 | [-10.09, -0.58] |
| Increasing Large (no 1) | 24 | -5.43 µV | 2.57 | 0.53 | [-10.36, 0.02] |
| Increasing Small (no 1) | 24 | -4.95 µV | 2.18 | 0.44 | [-10.61, -0.35] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 99.33 ms | 10.85 | 2.22 | [84.00, 112.00] |
| Increasing Large (no 1) | 24 | 100.00 ms | 10.87 | 2.22 | [84.00, 112.00] |
| Increasing Small (no 1) | 24 | 100.67 ms | 11.04 | 2.25 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 1.39 µV | 1.63 | 0.33 | [-0.83, 6.53] |
| Increasing Large (no 1) | 24 | 1.30 µV | 1.73 | 0.35 | [-2.05, 4.42] |
| Increasing Small (no 1) | 24 | 1.51 µV | 2.12 | 0.43 | [-3.02, 6.87] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 480.67 ms | 33.25 | 6.79 | [420.00, 528.00] |
| Increasing Large (no 1) | 24 | 488.17 ms | 35.43 | 7.23 | [420.00, 528.00] |
| Increasing Small (no 1) | 24 | 473.00 ms | 43.71 | 8.92 | [420.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 3.29 µV | 3.00 | 0.61 | [-2.25, 8.12] |
| Increasing Large (no 1) | 24 | 2.64 µV | 3.23 | 0.66 | [-2.73, 10.38] |
| Increasing Small (no 1) | 24 | 4.29 µV | 4.27 | 0.87 | [-3.54, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 528.52, BIC = 542.18
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -3.66, *SE* = 1.997, *z* = -1.831, *p* = 0.067
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -3.66, *SE* = 2.008, *z* = -1.822, *p* = 0.068
- **SNR**: *β* = 1.02, *SE* = 0.648, *z* = 1.580, *p* = 0.114

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 3.66 | 2.00 | 1.83 | 0.067 | 0.188 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 3.66 | 2.01 | 1.82 | 0.068 | 0.188 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.00 | 2.01 | 0.00 | 0.999 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.31, *p* = 0.111, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 2.07 | 23 | = 0.142 | 0.37 [-0.02, 0.86] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 1.74 | 23 | = 0.142 | 0.38 [-0.08, 0.79] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 0.16 | 23 | = 0.875 | 0.03 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 273.03, BIC = 286.69
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.03, *SE* = 0.398, *z* = -0.069, *p* = 0.945
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.33, *SE* = 0.400, *z* = -0.814, *p* = 0.415
- **SNR**: *β* = -0.15, *SE* = 0.117, *z* = -1.325, *p* = 0.185

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.03 | 0.40 | 0.07 | 0.945 | 0.945 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.33 | 0.40 | 0.81 | 0.415 | 0.800 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.30 | 0.40 | 0.75 | 0.456 | 0.800 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.27, *p* = 0.763, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.10 | 23 | = 0.925 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.62 | 23 | = 0.919 | 0.17 [-0.30, 0.55] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 0.51 | 23 | = 0.919 | 0.14 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 629.85, BIC = 643.51
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -2.13, *SE* = 4.366, *z* = -0.488, *p* = 0.626
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.66, *SE* = 5.362, *z* = -0.123, *p* = 0.902
- **SNR**: *β* = -0.22, *SE* = 0.631, *z* = -0.342, *p* = 0.732

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 2.13 | 4.37 | 0.49 | 0.626 | 0.948 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.66 | 5.36 | 0.12 | 0.902 | 0.948 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.47 | 4.62 | -0.32 | 0.751 | 0.948 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.865, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.756 (ε = 0.612)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.87 | 23 | = 0.923 | 0.09 [-0.25, 0.60] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.10 | 23 | = 0.923 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.45 | 23 | = 0.923 | -0.11 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 273.58, BIC = 287.24
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.55, *SE* = 0.332, *z* = -1.650, *p* = 0.099
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.80, *SE* = 0.414, *z* = -1.928, *p* = 0.054
- **SNR**: *β* = -0.23, *SE* = 0.050, *z* = -4.498, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.55 | 0.33 | 1.65 | 0.099 | 0.188 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.80 | 0.41 | 1.93 | 0.054 | 0.153 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.25 | 0.35 | 0.71 | 0.478 | 0.478 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.12, *p* = 0.335, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.22 | 23 | = 0.829 | 0.03 [-0.38, 0.47] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -1.22 | 23 | = 0.376 | -0.19 [-0.68, 0.18] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.18 | 23 | = 0.376 | -0.20 [-0.67, 0.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 544.52, BIC = 558.18
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.97, *SE* = 2.329, *z* = 0.416, *p* = 0.678
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.78, *SE* = 2.363, *z* = 0.754, *p* = 0.451
- **SNR**: *β* = 0.47, *SE* = 0.556, *z* = 0.835, *p* = 0.404

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.97 | 2.33 | -0.42 | 0.678 | 0.896 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.78 | 2.36 | -0.75 | 0.451 | 0.834 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.81 | 2.31 | -0.35 | 0.724 | 0.896 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.854, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -0.32 | 23 | = 0.786 | -0.06 [-0.49, 0.36] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.52 | 23 | = 0.786 | -0.12 [-0.53, 0.32] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.27 | 23 | = 0.786 | -0.06 [-0.48, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 287.19, BIC = 300.85
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.10, *SE* = 0.424, *z* = 0.248, *p* = 0.804
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 0.42, *SE* = 0.430, *z* = 0.973, *p* = 0.331
- **SNR**: *β* = 0.30, *SE* = 0.098, *z* = 3.098, *p* = 0.002

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.11 | 0.42 | -0.25 | 0.804 | 0.804 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -0.42 | 0.43 | -0.97 | 0.331 | 0.700 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.31 | 0.42 | -0.74 | 0.457 | 0.705 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.891, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.28 | 23 | = 0.798 | 0.05 [-0.36, 0.48] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.26 | 23 | = 0.798 | -0.07 [-0.48, 0.37] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.41 | 23 | = 0.798 | -0.11 [-0.51, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 732.94, BIC = 746.60
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 3.82, *SE* = 10.311, *z* = 0.370, *p* = 0.711
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -11.92, *SE* = 10.389, *z* = -1.148, *p* = 0.251
- **SNR**: *β* = -1.84, *SE* = 1.099, *z* = -1.676, *p* = 0.094

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -3.82 | 10.31 | -0.37 | 0.711 | 0.711 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 11.92 | 10.39 | 1.15 | 0.251 | 0.439 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 15.74 | 10.08 | 1.56 | 0.118 | 0.315 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.360, η²_G = 0.027
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -0.87 | 23 | = 0.464 | -0.22 [-0.60, 0.25] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.75 | 23 | = 0.464 | 0.20 [-0.27, 0.58] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 1.24 | 23 | = 0.464 | 0.38 [-0.18, 0.68] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 336.16, BIC = 349.82
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.35, *SE* = 0.457, *z* = -0.770, *p* = 0.442
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.35, *SE* = 0.465, *z* = 2.905, *p* = 0.004
- **SNR**: *β* = 0.15, *SE* = 0.070, *z* = 2.097, *p* = 0.036

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.35 | 0.46 | 0.77 | 0.442 | 0.442 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.35 | 0.46 | -2.91 | 0.004 | 0.007 | ** |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.70 | 0.44 | -3.91 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.75, *p* = 0.003, η²_G = 0.037
- Greenhouse-Geisser corrected: *p* = 0.007 (ε = 0.740)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 2.10 | 23 | = 0.047 | 0.21 [-0.01, 0.87] | small | * |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -2.16 | 23 | = 0.047 | -0.27 [-0.88, 0.00] | small | * |
| Increasing Large (no 1) vs Increasing Small (no 1) | -3.00 | 23 | = 0.019 | -0.44 [-1.07, -0.15] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - Increasing Crossover (no 1) showed greater amplitude than Increasing Large (no 1) (*d* = 0.21)
  - Increasing Crossover (no 1) showed smaller amplitude than Increasing Small (no 1) (*d* = -0.27)
  - Increasing Large (no 1) showed smaller amplitude than Increasing Small (no 1) (*d* = -0.44)

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
