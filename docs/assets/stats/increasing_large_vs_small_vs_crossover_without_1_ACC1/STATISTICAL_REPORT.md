# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:26:57

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
| Increasing Crossover (no 1) | 24 | 101.00 ms | 9.96 | 2.03 | [84.00, 112.00] |
| Increasing Large (no 1) | 24 | 97.33 ms | 10.12 | 2.07 | [84.00, 112.00] |
| Increasing Small (no 1) | 24 | 96.17 ms | 11.16 | 2.28 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | -1.32 µV | 1.13 | 0.23 | [-4.95, 0.11] |
| Increasing Large (no 1) | 24 | -1.93 µV | 1.85 | 0.38 | [-5.60, 2.40] |
| Increasing Small (no 1) | 24 | -1.47 µV | 2.19 | 0.45 | [-5.76, 2.45] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 169.17 ms | 20.51 | 4.19 | [136.00, 208.00] |
| Increasing Large (no 1) | 24 | 168.17 ms | 20.98 | 4.28 | [136.00, 200.00] |
| Increasing Small (no 1) | 24 | 170.50 ms | 21.49 | 4.39 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | -5.52 µV | 2.09 | 0.43 | [-9.99, -0.85] |
| Increasing Large (no 1) | 24 | -6.06 µV | 3.41 | 0.70 | [-14.92, 0.07] |
| Increasing Small (no 1) | 24 | -5.04 µV | 2.41 | 0.49 | [-10.61, 0.67] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 99.17 ms | 11.43 | 2.33 | [80.00, 112.00] |
| Increasing Large (no 1) | 24 | 97.50 ms | 12.19 | 2.49 | [80.00, 112.00] |
| Increasing Small (no 1) | 24 | 96.83 ms | 13.86 | 2.83 | [80.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 1.49 µV | 1.59 | 0.32 | [-0.99, 6.32] |
| Increasing Large (no 1) | 24 | 1.98 µV | 2.43 | 0.50 | [-1.97, 6.45] |
| Increasing Small (no 1) | 24 | 1.72 µV | 2.21 | 0.45 | [-2.42, 6.87] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 488.00 ms | 33.55 | 6.85 | [424.00, 528.00] |
| Increasing Large (no 1) | 24 | 487.83 ms | 37.70 | 7.70 | [424.00, 528.00] |
| Increasing Small (no 1) | 24 | 463.83 ms | 33.06 | 6.75 | [424.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 24 | 3.37 µV | 2.97 | 0.61 | [-2.20, 8.13] |
| Increasing Large (no 1) | 24 | 3.80 µV | 3.49 | 0.71 | [-3.13, 10.58] |
| Increasing Small (no 1) | 24 | 4.61 µV | 4.36 | 0.89 | [-3.66, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 534.51, BIC = 548.17
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -3.64, *SE* = 2.120, *z* = -1.717, *p* = 0.086
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -4.81, *SE* = 2.120, *z* = -2.269, *p* = 0.023
- **SNR**: *β* = 0.73, *SE* = 0.771, *z* = 0.942, *p* = 0.346

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 3.64 | 2.12 | 1.72 | 0.086 | 0.165 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 4.81 | 2.12 | 2.27 | 0.023 | 0.068 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 1.17 | 2.12 | 0.55 | 0.581 | 0.581 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.72, *p* = 0.077, η²_G = 0.039
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 2.11 | 23 | = 0.088 | 0.37 [-0.01, 0.87] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 1.99 | 23 | = 0.088 | 0.46 [-0.03, 0.85] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 0.52 | 23 | = 0.611 | 0.11 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 292.70, BIC = 306.36
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.62, *SE* = 0.468, *z* = -1.332, *p* = 0.183
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.15, *SE* = 0.468, *z* = -0.331, *p* = 0.741
- **SNR**: *β* = -0.27, *SE* = 0.151, *z* = -1.779, *p* = 0.075

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.62 | 0.47 | 1.33 | 0.183 | 0.455 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.15 | 0.47 | 0.33 | 0.741 | 0.741 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.47 | 0.47 | -1.00 | 0.317 | 0.533 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.85, *p* = 0.436, η²_G = 0.022
- Greenhouse-Geisser corrected: *p* = 0.396 (ε = 0.666)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.95 | 23 | = 0.192 | 0.40 [-0.04, 0.84] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.30 | 23 | = 0.763 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.74 | 23 | = 0.699 | -0.23 [-0.58, 0.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 636.24, BIC = 649.90
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.70, *SE* = 4.340, *z* = 0.161, *p* = 0.872
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 5.15, *SE* = 4.971, *z* = 1.036, *p* = 0.300
- **SNR**: *β* = 0.78, *SE* = 0.556, *z* = 1.409, *p* = 0.159

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.70 | 4.34 | -0.16 | 0.872 | 0.872 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -5.15 | 4.97 | -1.04 | 0.300 | 0.658 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -4.45 | 4.43 | -1.00 | 0.315 | 0.658 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.873, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.782 (ε = 0.656)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.42 | 23 | = 0.805 | 0.05 [-0.34, 0.51] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.25 | 23 | = 0.805 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.46 | 23 | = 0.805 | -0.11 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 311.37, BIC = 325.03
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -1.12, *SE* = 0.460, *z* = -2.435, *p* = 0.015
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.82, *SE* = 0.522, *z* = -1.564, *p* = 0.118
- **SNR**: *β* = -0.27, *SE* = 0.057, *z* = -4.700, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 1.12 | 0.46 | 2.43 | 0.015 | 0.044 | * |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.82 | 0.52 | 1.56 | 0.118 | 0.222 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.30 | 0.47 | -0.65 | 0.518 | 0.518 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.131, η²_G = 0.024
- Greenhouse-Geisser corrected: *p* = 0.151 (ε = 0.651)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.24 | 23 | = 0.228 | 0.19 [-0.18, 0.68] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -1.36 | 23 | = 0.228 | -0.21 [-0.71, 0.15] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.57 | 23 | = 0.228 | -0.35 [-0.75, 0.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 568.58, BIC = 582.24
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -1.84, *SE* = 2.921, *z* = -0.632, *p* = 0.528
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -1.80, *SE* = 2.936, *z* = -0.615, *p* = 0.539
- **SNR**: *β* = 1.27, *SE* = 0.760, *z* = 1.678, *p* = 0.093

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 1.85 | 2.92 | 0.63 | 0.528 | 0.895 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 1.80 | 2.94 | 0.61 | 0.539 | 0.895 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.04 | 2.95 | -0.01 | 0.989 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.32, *p* = 0.730, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.70 | 23 | = 0.734 | 0.14 [-0.28, 0.57] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.78 | 23 | = 0.734 | 0.18 [-0.27, 0.58] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 0.19 | 23 | = 0.853 | 0.05 [-0.38, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 314.40, BIC = 328.06
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.45, *SE* = 0.518, *z* = 0.871, *p* = 0.384
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 0.32, *SE* = 0.520, *z* = 0.610, *p* = 0.542
- **SNR**: *β* = 0.22, *SE* = 0.132, *z* = 1.669, *p* = 0.095

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.45 | 0.52 | -0.87 | 0.384 | 0.766 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -0.32 | 0.52 | -0.61 | 0.542 | 0.790 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.13 | 0.52 | 0.26 | 0.798 | 0.798 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.668, η²_G = 0.009
- Greenhouse-Geisser corrected: *p* = 0.599 (ε = 0.709)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -1.24 | 23 | = 0.681 | -0.23 [-0.68, 0.18] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.46 | 23 | = 0.709 | -0.12 [-0.52, 0.33] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 0.38 | 23 | = 0.709 | 0.11 [-0.35, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 718.30, BIC = 731.96
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -1.77, *SE* = 8.534, *z* = -0.207, *p* = 0.836
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -26.13, *SE* = 8.629, *z* = -3.029, *p* = 0.002
- **SNR**: *β* = -0.97, *SE* = 1.084, *z* = -0.893, *p* = 0.372

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 1.77 | 8.53 | 0.21 | 0.836 | 0.836 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 26.13 | 8.63 | 3.03 | 0.002 | 0.007 | ** |
| Increasing Large (no 1) - Increasing Small (no 1) | 24.36 | 8.35 | 2.92 | 0.004 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.38, *p* = 0.008, η²_G = 0.100
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.02 | 23 | = 0.987 | 0.00 [-0.42, 0.43] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 3.05 | 23 | = 0.008 | 0.73 [0.16, 1.08] | medium | ** |
| Increasing Large (no 1) vs Increasing Small (no 1) | 3.18 | 23 | = 0.008 | 0.68 [0.18, 1.11] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 343.60, BIC = 357.26
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.73, *SE* = 0.482, *z* = 1.504, *p* = 0.133
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.59, *SE* = 0.491, *z* = 3.248, *p* = 0.001
- **SNR**: *β* = 0.18, *SE* = 0.077, *z* = 2.290, *p* = 0.022

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.73 | 0.48 | -1.50 | 0.133 | 0.133 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.59 | 0.49 | -3.25 | 0.001 | 0.003 | ** |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.87 | 0.47 | -1.86 | 0.063 | 0.121 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.30, *p* = 0.046, η²_G = 0.020
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -1.26 | 23 | = 0.219 | -0.13 [-0.69, 0.17] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -2.44 | 23 | = 0.069 | -0.33 [-0.95, -0.05] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.37 | 23 | = 0.219 | -0.20 [-0.71, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Marginal trend toward condition differences (*p* = 0.077)
**P3b latency:** Significant main effect of condition (*p* = 0.008). Post-hoc tests revealed:
  - Increasing Crossover (no 1) showed greater latency than Increasing Small (no 1) (*d* = 0.73)
  - Increasing Large (no 1) showed greater latency than Increasing Small (no 1) (*d* = 0.68)
**P3b amplitude:** Significant main effect of condition (*p* = 0.046) (no significant pairwise comparisons)

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
