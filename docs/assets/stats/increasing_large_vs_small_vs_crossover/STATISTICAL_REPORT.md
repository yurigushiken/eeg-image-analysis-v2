# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:41:11

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
| Increasing Crossover | 7 | 94.86 ms | 12.38 | 4.68 | [84.00, 108.00] |
| Increasing Large | 7 | 93.14 ms | 10.51 | 3.97 | [84.00, 108.00] |
| Increasing Small | 15 | 98.67 ms | 10.22 | 2.64 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 7 | 1.08 µV | 0.48 | 0.18 | [0.43, 1.68] |
| Increasing Large | 7 | 1.23 µV | 1.01 | 0.38 | [0.18, 2.90] |
| Increasing Small | 15 | 1.42 µV | 0.94 | 0.24 | [0.52, 3.95] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 22 | 167.64 ms | 18.14 | 3.87 | [136.00, 208.00] |
| Increasing Large | 22 | 167.64 ms | 18.80 | 4.01 | [136.00, 200.00] |
| Increasing Small | 24 | 169.67 ms | 20.73 | 4.23 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 22 | -5.76 µV | 2.06 | 0.44 | [-10.48, -2.66] |
| Increasing Large | 22 | -5.84 µV | 2.24 | 0.48 | [-10.36, -1.88] |
| Increasing Small | 24 | -5.28 µV | 2.12 | 0.43 | [-10.78, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 99.20 ms | 10.39 | 2.68 | [80.00, 108.00] |
| Increasing Large | 13 | 96.92 ms | 9.82 | 2.72 | [80.00, 108.00] |
| Increasing Small | 11 | 101.09 ms | 8.78 | 2.65 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 1.74 µV | 1.39 | 0.36 | [0.54, 5.41] |
| Increasing Large | 13 | 2.34 µV | 1.19 | 0.33 | [0.61, 4.42] |
| Increasing Small | 11 | 2.02 µV | 1.14 | 0.34 | [0.58, 3.66] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 479.16 ms | 33.08 | 7.59 | [420.00, 532.00] |
| Increasing Large | 15 | 494.40 ms | 31.20 | 8.06 | [444.00, 532.00] |
| Increasing Small | 19 | 474.74 ms | 27.94 | 6.41 | [436.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 4.33 µV | 2.46 | 0.56 | [0.71, 8.36] |
| Increasing Large | 15 | 4.52 µV | 2.61 | 0.67 | [0.88, 10.38] |
| Increasing Small | 19 | 4.79 µV | 3.03 | 0.70 | [1.00, 12.65] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 220.51, BIC = 228.71
- **Increasing Large vs Increasing Crossover**: *β* = 0.91, *SE* = 3.474, *z* = 0.263, *p* = 0.792
- **Increasing Small vs Increasing Crossover**: *β* = 6.42, *SE* = 3.130, *z* = 2.053, *p* = 0.040
- **SNR**: *β* = -0.10, *SE* = 1.060, *z* = -0.096, *p* = 0.923

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.91 | 3.47 | -0.26 | 0.792 | 0.792 | n.s. |
| Increasing Crossover - Increasing Small | -6.42 | 3.13 | -2.05 | 0.040 | 0.116 | n.s. |
| Increasing Large - Increasing Small | -5.51 | 2.90 | -1.90 | 0.058 | 0.116 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.30, *p* = 0.101, η²_G = 0.164
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.00 | 2 | = 0.423 | 0.10 [-1.97, 1.30] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -1.73 | 2 | = 0.338 | -0.71 [-2.08, 0.37] | medium | n.s. |
| Increasing Large vs Increasing Small | -2.65 | 2 | = 0.338 | -0.94 [-2.22, 0.31] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 72.43, BIC = 80.64
- **Increasing Large vs Increasing Crossover**: *β* = -0.15, *SE* = 0.346, *z* = -0.446, *p* = 0.656
- **Increasing Small vs Increasing Crossover**: *β* = -0.01, *SE* = 0.304, *z* = -0.037, *p* = 0.970
- **SNR**: *β* = 0.34, *SE* = 0.101, *z* = 3.322, *p* = 0.001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.15 | 0.35 | 0.45 | 0.656 | 0.945 | n.s. |
| Increasing Crossover - Increasing Small | 0.01 | 0.30 | 0.04 | 0.970 | 0.970 | n.s. |
| Increasing Large - Increasing Small | -0.14 | 0.29 | -0.49 | 0.621 | 0.945 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.426, η²_G = 0.318
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.27 | 2 | = 0.496 | 0.89 [-1.41, 1.80] | large | n.s. |
| Increasing Crossover vs Increasing Small | -0.61 | 2 | = 0.606 | -0.56 [-1.62, 0.61] | medium | n.s. |
| Increasing Large vs Increasing Small | -1.27 | 2 | = 0.496 | -1.36 [-1.15, 0.95] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 591.24, BIC = 604.55
- **Increasing Large vs Increasing Crossover**: *β* = -1.93, *SE* = 4.431, *z* = -0.436, *p* = 0.663
- **Increasing Small vs Increasing Crossover**: *β* = -0.58, *SE* = 4.309, *z* = -0.135, *p* = 0.892
- **SNR**: *β* = -0.25, *SE* = 0.485, *z* = -0.510, *p* = 0.610

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.93 | 4.43 | 0.44 | 0.663 | 0.962 | n.s. |
| Increasing Crossover - Increasing Small | 0.58 | 4.31 | 0.14 | 0.892 | 0.962 | n.s. |
| Increasing Large - Increasing Small | -1.35 | 4.05 | -0.33 | 0.740 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.872, η²_G = 0.003
- Greenhouse-Geisser corrected: *p* = 0.788 (ε = 0.674)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.71 | 20 | = 0.937 | 0.09 [-0.30, 0.61] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 0.41 | 20 | = 0.937 | 0.11 [-0.38, 0.51] | negligible | n.s. |
| Increasing Large vs Increasing Small | 0.08 | 20 | = 0.937 | 0.02 [-0.45, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 230.90, BIC = 244.21
- **Increasing Large vs Increasing Crossover**: *β* = -0.70, *SE* = 0.255, *z* = -2.723, *p* = 0.006
- **Increasing Small vs Increasing Crossover**: *β* = -0.17, *SE* = 0.246, *z* = -0.682, *p* = 0.496
- **SNR**: *β* = -0.15, *SE* = 0.032, *z* = -4.879, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.70 | 0.26 | 2.72 | 0.006 | 0.019 | * |
| Increasing Crossover - Increasing Small | 0.17 | 0.25 | 0.68 | 0.496 | 0.496 | n.s. |
| Increasing Large - Increasing Small | -0.53 | 0.23 | -2.31 | 0.021 | 0.041 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.25, *p* = 0.297, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.93 | 20 | = 0.436 | 0.09 [-0.26, 0.66] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.80 | 20 | = 0.436 | -0.13 [-0.63, 0.27] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.47 | 20 | = 0.436 | -0.22 [-0.78, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 293.14, BIC = 303.12
- **Increasing Large vs Increasing Crossover**: *β* = -2.76, *SE* = 2.848, *z* = -0.968, *p* = 0.333
- **Increasing Small vs Increasing Crossover**: *β* = 2.75, *SE* = 2.790, *z* = 0.985, *p* = 0.325
- **SNR**: *β* = 0.39, *SE* = 0.750, *z* = 0.519, *p* = 0.604

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 2.76 | 2.85 | 0.97 | 0.333 | 0.544 | n.s. |
| Increasing Crossover - Increasing Small | -2.75 | 2.79 | -0.98 | 0.325 | 0.544 | n.s. |
| Increasing Large - Increasing Small | -5.51 | 3.03 | -1.82 | 0.069 | 0.193 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.17, *p* = 0.086, η²_G = 0.288
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.17 | 5 | = 0.296 | 0.70 [-0.49, 1.08] | medium | n.s. |
| Increasing Crossover vs Increasing Small | -1.47 | 5 | = 0.296 | -0.69 [-1.01, 0.45] | medium | n.s. |
| Increasing Large vs Increasing Small | -2.63 | 5 | = 0.140 | -1.53 [-2.02, 0.18] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 119.13, BIC = 129.11
- **Increasing Large vs Increasing Crossover**: *β* = 0.88, *SE* = 0.350, *z* = 2.502, *p* = 0.012
- **Increasing Small vs Increasing Crossover**: *β* = 0.36, *SE* = 0.346, *z* = 1.047, *p* = 0.295
- **SNR**: *β* = 0.34, *SE* = 0.083, *z* = 4.109, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.88 | 0.35 | -2.50 | 0.012 | 0.037 | * |
| Increasing Crossover - Increasing Small | -0.36 | 0.35 | -1.05 | 0.295 | 0.299 | n.s. |
| Increasing Large - Increasing Small | 0.51 | 0.37 | 1.40 | 0.163 | 0.299 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.07, *p* = 0.177, η²_G = 0.085
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.99 | 5 | = 0.415 | 0.33 [-0.83, 0.71] | small | n.s. |
| Increasing Crossover vs Increasing Small | 2.51 | 5 | = 0.161 | 0.63 [-0.63, 0.80] | medium | n.s. |
| Increasing Large vs Increasing Small | 0.89 | 5 | = 0.415 | 0.40 [-0.74, 1.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 519.78, BIC = 531.60
- **Increasing Large vs Increasing Crossover**: *β* = 12.62, *SE* = 10.071, *z* = 1.253, *p* = 0.210
- **Increasing Small vs Increasing Crossover**: *β* = -5.34, *SE* = 8.730, *z* = -0.612, *p* = 0.541
- **SNR**: *β* = -0.90, *SE* = 0.997, *z* = -0.898, *p* = 0.369

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -12.61 | 10.07 | -1.25 | 0.210 | 0.376 | n.s. |
| Increasing Crossover - Increasing Small | 5.34 | 8.73 | 0.61 | 0.541 | 0.541 | n.s. |
| Increasing Large - Increasing Small | 17.96 | 9.62 | 1.87 | 0.062 | 0.175 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.15, *p* = 0.027, η²_G = 0.128
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -2.60 | 13 | = 0.066 | -0.74 [-1.01, 0.15] | medium | n.s. |
| Increasing Crossover vs Increasing Small | 0.23 | 13 | = 0.823 | 0.06 [-0.48, 0.51] | negligible | n.s. |
| Increasing Large vs Increasing Small | 2.07 | 13 | = 0.088 | 0.83 [-0.07, 1.17] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 215.98, BIC = 227.80
- **Increasing Large vs Increasing Crossover**: *β* = 1.22, *SE* = 0.527, *z* = 2.317, *p* = 0.021
- **Increasing Small vs Increasing Crossover**: *β* = 0.92, *SE* = 0.413, *z* = 2.230, *p* = 0.026
- **SNR**: *β* = 0.33, *SE* = 0.063, *z* = 5.151, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -1.22 | 0.53 | -2.32 | 0.021 | 0.060 | n.s. |
| Increasing Crossover - Increasing Small | -0.92 | 0.41 | -2.23 | 0.026 | 0.060 | n.s. |
| Increasing Large - Increasing Small | 0.30 | 0.49 | 0.61 | 0.541 | 0.541 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.355, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.11 | 13 | = 0.431 | 0.24 [-0.28, 0.85] | small | n.s. |
| Increasing Crossover vs Increasing Small | -0.59 | 13 | = 0.566 | -0.10 [-0.81, 0.21] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.13 | 13 | = 0.431 | -0.30 [-0.89, 0.29] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Marginal trend toward condition differences (*p* = 0.086)
**P3b latency:** Significant main effect of condition (*p* = 0.027) (no significant pairwise comparisons)

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
