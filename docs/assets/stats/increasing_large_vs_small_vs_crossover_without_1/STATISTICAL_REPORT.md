# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:45:42

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
| Increasing Crossover (no 1) | 16 | 102.75 ms | 8.73 | 2.18 | [84.00, 112.00] |
| Increasing Large (no 1) | 17 | 99.06 ms | 9.22 | 2.24 | [84.00, 112.00] |
| Increasing Small (no 1) | 16 | 98.50 ms | 11.85 | 2.96 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 16 | -1.69 µV | 1.13 | 0.28 | [-5.10, -0.23] |
| Increasing Large (no 1) | 17 | -1.94 µV | 0.79 | 0.19 | [-3.44, -0.62] |
| Increasing Small (no 1) | 16 | -2.48 µV | 1.53 | 0.38 | [-5.76, -0.37] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 22 | 167.27 ms | 17.83 | 3.80 | [136.00, 204.00] |
| Increasing Large (no 1) | 22 | 167.64 ms | 18.80 | 4.01 | [136.00, 200.00] |
| Increasing Small (no 1) | 22 | 170.91 ms | 18.97 | 4.04 | [136.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 22 | -5.63 µV | 1.96 | 0.42 | [-10.09, -2.77] |
| Increasing Large (no 1) | 22 | -5.84 µV | 2.24 | 0.48 | [-10.36, -1.88] |
| Increasing Small (no 1) | 22 | -5.26 µV | 1.96 | 0.42 | [-10.61, -0.91] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 102.13 ms | 9.78 | 2.53 | [84.00, 112.00] |
| Increasing Large (no 1) | 14 | 102.29 ms | 8.70 | 2.32 | [84.00, 112.00] |
| Increasing Small (no 1) | 11 | 102.55 ms | 9.51 | 2.87 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 1.75 µV | 1.74 | 0.45 | [0.29, 6.53] |
| Increasing Large (no 1) | 14 | 2.18 µV | 1.27 | 0.34 | [0.61, 4.42] |
| Increasing Small (no 1) | 11 | 3.17 µV | 1.75 | 0.53 | [0.75, 6.87] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 18 | 478.00 ms | 34.03 | 8.02 | [420.00, 528.00] |
| Increasing Large (no 1) | 15 | 493.87 ms | 30.53 | 7.88 | [444.00, 528.00] |
| Increasing Small (no 1) | 18 | 478.44 ms | 44.55 | 10.50 | [420.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 18 | 4.51 µV | 2.31 | 0.55 | [0.74, 8.12] |
| Increasing Large (no 1) | 15 | 4.48 µV | 2.59 | 0.67 | [0.88, 10.38] |
| Increasing Small (no 1) | 18 | 5.85 µV | 3.54 | 0.83 | [1.42, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 362.12, BIC = 373.47
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -2.67, *SE* = 2.413, *z* = -1.106, *p* = 0.269
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -2.54, *SE* = 2.568, *z* = -0.990, *p* = 0.322
- **SNR**: *β* = 1.27, *SE* = 0.763, *z* = 1.664, *p* = 0.096

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 2.67 | 2.41 | 1.11 | 0.269 | 0.609 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 2.54 | 2.57 | 0.99 | 0.322 | 0.609 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.13 | 2.44 | -0.05 | 0.959 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.69, *p* = 0.516, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.15 | 9 | = 0.605 | 0.42 [-0.25, 1.00] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.54 | 9 | = 0.605 | 0.20 [-0.48, 0.87] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.74 | 9 | = 0.605 | -0.15 [-0.59, 0.68] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 148.70, BIC = 160.05
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.39, *SE* = 0.315, *z* = -1.232, *p* = 0.218
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -1.22, *SE* = 0.334, *z* = -3.660, *p* < .001
- **SNR**: *β* = -0.42, *SE* = 0.094, *z* = -4.413, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.39 | 0.32 | 1.23 | 0.218 | 0.218 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 1.22 | 0.33 | 3.66 | < .001 | < .001 | *** |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.83 | 0.32 | 2.58 | 0.010 | 0.020 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.36, *p* = 0.029, η²_G = 0.281
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.47 | 9 | = 0.646 | 0.24 [-0.63, 0.58] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 2.71 | 9 | = 0.072 | 1.19 [0.01, 1.55] | large | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 1.93 | 9 | = 0.129 | 1.03 [-0.27, 1.05] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 567.97, BIC = 581.11
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.02, *SE* = 4.123, *z* = 0.005, *p* = 0.996
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 5.19, *SE* = 5.280, *z* = 0.983, *p* = 0.326
- **SNR**: *β* = 0.27, *SE* = 0.608, *z* = 0.451, *p* = 0.652

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.02 | 4.12 | -0.00 | 0.996 | 0.996 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -5.19 | 5.28 | -0.98 | 0.326 | 0.568 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -5.17 | 4.44 | -1.16 | 0.244 | 0.568 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.635, η²_G = 0.009
- Greenhouse-Geisser corrected: *p* = 0.552 (ε = 0.644)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.28 | 19 | = 0.784 | 0.03 [-0.32, 0.59] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.64 | 19 | = 0.784 | -0.18 [-0.63, 0.28] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.76 | 19 | = 0.784 | -0.21 [-0.64, 0.28] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 231.74, BIC = 244.88
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.83, *SE* = 0.282, *z* = -2.945, *p* = 0.003
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.95, *SE* = 0.362, *z* = -2.630, *p* = 0.009
- **SNR**: *β* = -0.21, *SE* = 0.042, *z* = -4.983, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.83 | 0.28 | 2.94 | 0.003 | 0.010 | ** |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.95 | 0.36 | 2.63 | 0.009 | 0.017 | * |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.12 | 0.30 | 0.40 | 0.691 | 0.691 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.54, *p* = 0.228, η²_G = 0.016
- Greenhouse-Geisser corrected: *p* = 0.232 (ε = 0.709)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.69 | 19 | = 0.240 | 0.17 [-0.10, 0.84] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.65 | 19 | = 0.523 | -0.13 [-0.62, 0.30] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.46 | 19 | = 0.240 | -0.31 [-0.81, 0.12] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 286.16, BIC = 296.29
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.27, *SE* = 1.977, *z* = -0.137, *p* = 0.891
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.27, *SE* = 2.241, *z* = 0.566, *p* = 0.571
- **SNR**: *β* = 0.36, *SE* = 0.411, *z* = 0.869, *p* = 0.385

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.27 | 1.98 | 0.14 | 0.891 | 0.891 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.27 | 2.24 | -0.57 | 0.571 | 0.857 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.54 | 2.17 | -0.71 | 0.478 | 0.857 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.891, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.00 | 6 | = 1.000 | 0.00 [-0.57, 0.78] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.40 | 6 | = 1.000 | -0.15 [-0.98, 0.70] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.35 | 6 | = 1.000 | -0.16 [-1.03, 0.66] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 131.75, BIC = 141.88
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.81, *SE* = 0.362, *z* = 2.246, *p* = 0.025
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.81, *SE* = 0.395, *z* = 4.571, *p* < .001
- **SNR**: *β* = 0.44, *SE* = 0.071, *z* = 6.179, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.81 | 0.36 | -2.25 | 0.025 | 0.025 | * |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.81 | 0.40 | -4.57 | < .001 | < .001 | *** |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.99 | 0.39 | -2.56 | 0.010 | 0.021 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.36, *p* = 0.707, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.72 | 6 | = 0.745 | 0.24 [-0.87, 0.49] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.07 | 6 | = 0.947 | -0.03 [-1.00, 0.69] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.18 | 6 | = 0.745 | -0.40 [-1.46, 0.34] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 521.59, BIC = 533.18
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 11.71, *SE* = 13.063, *z* = 0.896, *p* = 0.370
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -3.65, *SE* = 12.495, *z* = -0.292, *p* = 0.770
- **SNR**: *β* = -1.32, *SE* = 1.364, *z* = -0.966, *p* = 0.334

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -11.71 | 13.06 | -0.90 | 0.370 | 0.603 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 3.65 | 12.49 | 0.29 | 0.770 | 0.770 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 15.36 | 12.35 | 1.24 | 0.214 | 0.514 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.30, *p* = 0.122, η²_G = 0.106
- Greenhouse-Geisser corrected: *p* = 0.142 (ε = 0.695)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -3.47 | 12 | = 0.014 | -0.91 [-1.07, 0.10] | large | * |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.48 | 12 | = 0.639 | -0.18 [-0.61, 0.46] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 1.28 | 12 | = 0.338 | 0.57 [-0.27, 0.98] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 230.21, BIC = 241.80
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.69, *SE* = 0.642, *z* = 1.077, *p* = 0.282
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 2.29, *SE* = 0.592, *z* = 3.873, *p* < .001
- **SNR**: *β* = 0.28, *SE* = 0.089, *z* = 3.169, *p* = 0.002

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.69 | 0.64 | -1.08 | 0.282 | 0.282 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -2.29 | 0.59 | -3.87 | < .001 | < .001 | *** |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.60 | 0.57 | -2.81 | 0.005 | 0.010 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.72, *p* = 0.019, η²_G = 0.081
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.14 | 12 | = 0.278 | 0.22 [-0.26, 0.87] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -2.22 | 12 | = 0.069 | -0.47 [-1.24, -0.06] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -2.38 | 12 | = 0.069 | -0.61 [-1.33, 0.01] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.029) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.019) (no significant pairwise comparisons)

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
