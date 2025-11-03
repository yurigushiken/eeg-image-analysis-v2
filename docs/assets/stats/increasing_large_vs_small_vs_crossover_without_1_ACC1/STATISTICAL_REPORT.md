# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:43:54

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
| Increasing Crossover (no 1) | 8 | 99.00 ms | 13.98 | 4.94 | [84.00, 112.00] |
| Increasing Large (no 1) | 7 | 104.57 ms | 10.94 | 4.13 | [84.00, 112.00] |
| Increasing Small (no 1) | 11 | 96.73 ms | 11.43 | 3.45 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 8 | 1.22 µV | 0.69 | 0.24 | [0.24, 2.21] |
| Increasing Large (no 1) | 7 | 2.67 µV | 1.05 | 0.40 | [0.83, 4.01] |
| Increasing Small (no 1) | 11 | 2.17 µV | 1.44 | 0.44 | [0.25, 5.40] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 23 | 167.48 ms | 19.19 | 4.00 | [136.00, 204.00] |
| Increasing Large (no 1) | 22 | 167.64 ms | 20.80 | 4.43 | [136.00, 200.00] |
| Increasing Small (no 1) | 21 | 168.95 ms | 18.84 | 4.11 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 23 | -5.72 µV | 1.88 | 0.39 | [-9.99, -2.74] |
| Increasing Large (no 1) | 22 | -6.55 µV | 3.11 | 0.66 | [-14.92, -2.97] |
| Increasing Small (no 1) | 21 | -5.65 µV | 1.80 | 0.39 | [-10.61, -2.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 101.60 ms | 9.05 | 2.34 | [80.00, 112.00] |
| Increasing Large (no 1) | 13 | 102.46 ms | 10.78 | 2.99 | [80.00, 112.00] |
| Increasing Small (no 1) | 12 | 100.00 ms | 12.06 | 3.48 | [80.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 1.73 µV | 1.65 | 0.43 | [0.26, 6.32] |
| Increasing Large (no 1) | 13 | 3.34 µV | 1.68 | 0.47 | [1.15, 6.45] |
| Increasing Small (no 1) | 12 | 3.30 µV | 1.84 | 0.53 | [0.75, 6.87] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 20 | 489.20 ms | 33.57 | 7.51 | [424.00, 528.00] |
| Increasing Large (no 1) | 15 | 488.53 ms | 36.44 | 9.41 | [436.00, 528.00] |
| Increasing Small (no 1) | 19 | 464.00 ms | 32.39 | 7.43 | [424.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 20 | 4.24 µV | 2.41 | 0.54 | [0.92, 8.13] |
| Increasing Large (no 1) | 15 | 5.85 µV | 2.59 | 0.67 | [1.73, 10.58] |
| Increasing Small (no 1) | 19 | 6.16 µV | 3.34 | 0.77 | [1.82, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 204.67, BIC = 212.22
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 3.12, *SE* = 3.926, *z* = 0.796, *p* = 0.426
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -3.81, *SE* = 4.207, *z* = -0.905, *p* = 0.365
- **SNR**: *β* = -0.57, *SE* = 2.245, *z* = -0.253, *p* = 0.800

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -3.12 | 3.93 | -0.80 | 0.426 | 0.597 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 3.81 | 4.21 | 0.91 | 0.365 | 0.597 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 6.93 | 3.81 | 1.82 | 0.069 | 0.192 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.00 | 1 | = 0.500 | 0.11 [-1.91, 1.34] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 1.00 | 1 | = 0.500 | 0.11 [-1.20, 2.16] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | nan | 1 | n/a | 0.00 [-2.11, 3.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 84.27, BIC = 91.82
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 1.18, *SE* = 0.512, *z* = 2.299, *p* = 0.021
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 0.51, *SE* = 0.482, *z* = 1.051, *p* = 0.293
- **SNR**: *β* = 0.44, *SE* = 0.173, *z* = 2.560, *p* = 0.010

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -1.18 | 0.51 | -2.30 | 0.021 | 0.063 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -0.51 | 0.48 | -1.05 | 0.293 | 0.293 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.67 | 0.47 | 1.42 | 0.157 | 0.289 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -35.41 | 1 | = 0.054 | -3.46 [-11.44, 0.87] | large | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -2.76 | 1 | = 0.332 | -2.13 [-2.87, 0.97] | large | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.48 | 1 | = 0.378 | -1.19 [-2.44, 2.53] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 575.67, BIC = 588.81
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 2.67, *SE* = 4.110, *z* = 0.651, *p* = 0.515
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 9.15, *SE* = 4.960, *z* = 1.845, *p* = 0.065
- **SNR**: *β* = 1.06, *SE* = 0.536, *z* = 1.979, *p* = 0.048

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -2.67 | 4.11 | -0.65 | 0.515 | 0.515 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -9.15 | 4.96 | -1.85 | 0.065 | 0.183 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -6.48 | 4.36 | -1.49 | 0.137 | 0.255 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.49, *p* = 0.615, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.549 (ε = 0.694)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -0.23 | 19 | = 0.824 | -0.03 [-0.44, 0.47] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.81 | 19 | = 0.766 | -0.23 [-0.68, 0.24] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.67 | 19 | = 0.766 | -0.18 [-0.62, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 266.41, BIC = 279.55
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -1.43, *SE* = 0.400, *z* = -3.563, *p* < .001
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -1.15, *SE* = 0.458, *z* = -2.510, *p* = 0.012
- **SNR**: *β* = -0.25, *SE* = 0.047, *z* = -5.311, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 1.42 | 0.40 | 3.56 | < .001 | 0.001 | ** |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 1.15 | 0.46 | 2.51 | 0.012 | 0.024 | * |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.27 | 0.42 | -0.66 | 0.509 | 0.509 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.18, *p* = 0.127, η²_G = 0.033
- Greenhouse-Geisser corrected: *p* = 0.151 (ε = 0.605)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 2.05 | 19 | = 0.165 | 0.29 [0.03, 1.00] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.56 | 19 | = 0.580 | -0.12 [-0.61, 0.31] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.48 | 19 | = 0.233 | -0.38 [-0.81, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.49, BIC = 312.62
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -3.35, *SE* = 2.916, *z* = -1.149, *p* = 0.250
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -3.21, *SE* = 2.938, *z* = -1.094, *p* = 0.274
- **SNR**: *β* = 0.61, *SE* = 0.665, *z* = 0.925, *p* = 0.355

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 3.35 | 2.92 | 1.15 | 0.250 | 0.579 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 3.21 | 2.94 | 1.09 | 0.274 | 0.579 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.14 | 3.02 | -0.05 | 0.963 | 0.963 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.76, *p* = 0.506, η²_G = 0.078
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.41 | 3 | = 0.718 | 0.55 [-0.25, 1.42] | medium | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.40 | 3 | = 0.718 | 0.21 [-0.36, 1.42] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.68 | 3 | = 0.718 | -0.39 [-1.56, 0.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 138.81, BIC = 148.94
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 1.76, *SE* = 0.422, *z* = 4.181, *p* < .001
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.90, *SE* = 0.437, *z* = 4.346, *p* < .001
- **SNR**: *β* = 0.57, *SE* = 0.096, *z* = 5.923, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -1.76 | 0.42 | -4.18 | < .001 | < .001 | *** |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.90 | 0.44 | -4.35 | < .001 | < .001 | *** |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.14 | 0.45 | -0.30 | 0.762 | 0.762 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.11, *p* = 0.388, η²_G = 0.130
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.08 | 3 | = 0.940 | 0.03 [-1.36, 0.28] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 1.17 | 3 | = 0.491 | 0.73 [-1.24, 0.49] | medium | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 1.28 | 3 | = 0.491 | 0.93 [-0.57, 1.69] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 539.74, BIC = 551.68
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -1.12, *SE* = 9.998, *z* = -0.112, *p* = 0.911
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -25.08, *SE* = 9.524, *z* = -2.633, *p* = 0.008
- **SNR**: *β* = -0.28, *SE* = 1.199, *z* = -0.237, *p* = 0.813

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 1.12 | 10.00 | 0.11 | 0.911 | 0.911 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 25.08 | 9.52 | 2.63 | 0.008 | 0.025 | * |
| Increasing Large (no 1) - Increasing Small (no 1) | 23.96 | 9.98 | 2.40 | 0.016 | 0.032 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.93, *p* = 0.032, η²_G = 0.132
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.18 | 13 | = 0.859 | 0.07 [-0.48, 0.63] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 2.48 | 13 | = 0.041 | 0.88 [-0.00, 1.06] | large | * |
| Increasing Large (no 1) vs Increasing Small (no 1) | 2.76 | 13 | = 0.041 | 0.75 [0.09, 1.39] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 236.51, BIC = 248.44
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 1.54, *SE* = 0.517, *z* = 2.989, *p* = 0.003
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 2.36, *SE* = 0.488, *z* = 4.834, *p* < .001
- **SNR**: *β* = 0.25, *SE* = 0.076, *z* = 3.296, *p* = 0.001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -1.54 | 0.52 | -2.99 | 0.003 | 0.006 | ** |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -2.36 | 0.49 | -4.83 | < .001 | < .001 | *** |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.82 | 0.50 | -1.64 | 0.101 | 0.101 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.73, *p* = 0.084, η²_G = 0.038
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -1.38 | 13 | = 0.285 | -0.28 [-0.99, 0.17] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -2.17 | 13 | = 0.147 | -0.45 [-1.30, -0.18] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.11 | 13 | = 0.285 | -0.21 [-0.89, 0.29] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Significant main effect of condition (*p* = 0.032). Post-hoc tests revealed:
  - Increasing Crossover (no 1) showed greater latency than Increasing Small (no 1) (*d* = 0.88)
  - Increasing Large (no 1) showed greater latency than Increasing Small (no 1) (*d* = 0.75)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.084)

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
