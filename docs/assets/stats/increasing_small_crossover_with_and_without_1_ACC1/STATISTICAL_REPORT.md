# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:42:22

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
| Crossover (with 1) | 7 | 100.57 ms | 14.32 | 5.41 | [84.00, 112.00] |
| Crossover (without 1) | 8 | 99.00 ms | 13.98 | 4.94 | [84.00, 112.00] |
| Small (with 1) | 13 | 101.23 ms | 11.24 | 3.12 | [84.00, 112.00] |
| Small (without 1) | 11 | 96.73 ms | 11.43 | 3.45 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 7 | 1.39 µV | 0.96 | 0.36 | [0.32, 2.79] |
| Crossover (without 1) | 8 | 1.22 µV | 0.69 | 0.24 | [0.24, 2.21] |
| Small (with 1) | 13 | 1.75 µV | 0.94 | 0.26 | [0.78, 3.99] |
| Small (without 1) | 11 | 2.17 µV | 1.44 | 0.44 | [0.25, 5.40] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 23 | 169.22 ms | 19.61 | 4.09 | [136.00, 208.00] |
| Crossover (without 1) | 23 | 167.48 ms | 19.19 | 4.00 | [136.00, 204.00] |
| Small (with 1) | 23 | 170.26 ms | 20.50 | 4.27 | [140.00, 208.00] |
| Small (without 1) | 21 | 168.95 ms | 18.84 | 4.11 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 23 | -5.81 µV | 2.05 | 0.43 | [-10.54, -2.66] |
| Crossover (without 1) | 23 | -5.72 µV | 1.88 | 0.39 | [-9.99, -2.74] |
| Small (with 1) | 23 | -5.50 µV | 2.05 | 0.43 | [-10.86, -1.45] |
| Small (without 1) | 21 | -5.65 µV | 1.80 | 0.39 | [-10.61, -2.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 14 | 101.71 ms | 7.80 | 2.08 | [84.00, 112.00] |
| Crossover (without 1) | 15 | 101.60 ms | 9.05 | 2.34 | [80.00, 112.00] |
| Small (with 1) | 12 | 99.00 ms | 11.07 | 3.20 | [80.00, 112.00] |
| Small (without 1) | 12 | 100.00 ms | 12.06 | 3.48 | [80.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 14 | 1.95 µV | 1.41 | 0.38 | [0.66, 5.19] |
| Crossover (without 1) | 15 | 1.73 µV | 1.65 | 0.43 | [0.26, 6.32] |
| Small (with 1) | 12 | 2.04 µV | 1.13 | 0.33 | [0.58, 3.56] |
| Small (without 1) | 12 | 3.30 µV | 1.84 | 0.53 | [0.75, 6.87] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 19 | 467.37 ms | 41.06 | 9.42 | [396.00, 532.00] |
| Crossover (without 1) | 19 | 482.32 ms | 40.45 | 9.28 | [396.00, 532.00] |
| Small (with 1) | 19 | 462.95 ms | 40.44 | 9.28 | [396.00, 532.00] |
| Small (without 1) | 18 | 460.67 ms | 41.91 | 9.88 | [396.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 19 | 4.55 µV | 2.43 | 0.56 | [0.98, 8.79] |
| Crossover (without 1) | 19 | 4.47 µV | 2.35 | 0.54 | [0.92, 8.56] |
| Small (with 1) | 19 | 4.93 µV | 2.92 | 0.67 | [0.63, 11.98] |
| Small (without 1) | 18 | 6.49 µV | 3.30 | 0.78 | [1.82, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 313.11, BIC = 324.75
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -1.80, *SE* = 5.160, *z* = -0.350, *p* = 0.727
- **Small (with 1) vs Crossover (with 1)**: *β* = -0.71, *SE* = 5.161, *z* = -0.138, *p* = 0.891
- **Small (without 1) vs Crossover (with 1)**: *β* = -6.31, *SE* = 5.164, *z* = -1.222, *p* = 0.222
- **SNR**: *β* = 1.62, *SE* = 1.842, *z* = 0.881, *p* = 0.378

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 1.80 | 5.16 | 0.35 | 0.727 | 0.980 | n.s. |
| Crossover (with 1) - Small (with 1) | 0.71 | 5.16 | 0.14 | 0.891 | 0.980 | n.s. |
| Crossover (with 1) - Small (without 1) | 6.31 | 5.16 | 1.22 | 0.222 | 0.714 | n.s. |
| Crossover (without 1) - Small (with 1) | -1.09 | 5.15 | -0.21 | 0.832 | 0.980 | n.s. |
| Crossover (without 1) - Small (without 1) | 4.51 | 5.16 | 0.87 | 0.382 | 0.854 | n.s. |
| Small (with 1) - Small (without 1) | 5.60 | 4.12 | 1.36 | 0.174 | 0.682 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.05, *p* = 0.178, η²_G = 0.204
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.81 | 3 | = 0.572 | 0.41 [-0.92, 1.65] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.30 | 3 | = 0.783 | -0.19 [-1.38, 0.55] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 1.73 | 3 | = 0.363 | 0.89 [-0.64, 1.57] | large | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.73 | 3 | = 0.363 | -0.70 [-2.52, 0.52] | medium | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.96 | 3 | = 0.572 | 0.43 [-1.20, 2.16] | small | n.s. |
| Small (with 1) vs Small (without 1) | 2.65 | 3 | = 0.363 | 1.40 [-0.32, 1.32] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 107.71, BIC = 119.36
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.24, *SE* = 0.403, *z* = -0.591, *p* = 0.554
- **Small (with 1) vs Crossover (with 1)**: *β* = -0.38, *SE* = 0.400, *z* = -0.945, *p* = 0.345
- **Small (without 1) vs Crossover (with 1)**: *β* = 0.12, *SE* = 0.402, *z* = 0.308, *p* = 0.758
- **SNR**: *β* = 0.58, *SE* = 0.129, *z* = 4.458, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.24 | 0.40 | 0.59 | 0.554 | 0.911 | n.s. |
| Crossover (with 1) - Small (with 1) | 0.38 | 0.40 | 0.95 | 0.345 | 0.879 | n.s. |
| Crossover (with 1) - Small (without 1) | -0.12 | 0.40 | -0.31 | 0.758 | 0.919 | n.s. |
| Crossover (without 1) - Small (with 1) | 0.14 | 0.38 | 0.36 | 0.716 | 0.919 | n.s. |
| Crossover (without 1) - Small (without 1) | -0.36 | 0.39 | -0.94 | 0.350 | 0.879 | n.s. |
| Small (with 1) - Small (without 1) | -0.50 | 0.32 | -1.57 | 0.115 | 0.521 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.52, *p* = 0.124, η²_G = 0.257
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.69 | 3 | = 0.324 | 0.22 [-0.91, 1.66] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | -1.16 | 3 | = 0.329 | -0.28 [-1.51, 0.46] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | -1.56 | 3 | = 0.324 | -0.90 [-1.43, 0.73] | large | n.s. |
| Crossover (without 1) vs Small (with 1) | -3.03 | 3 | = 0.324 | -0.60 [-2.05, 0.70] | medium | n.s. |
| Crossover (without 1) vs Small (without 1) | -1.90 | 3 | = 0.324 | -1.08 [-2.87, 0.97] | large | n.s. |
| Small (with 1) vs Small (without 1) | -1.25 | 3 | = 0.329 | -0.80 [-0.93, 0.62] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 769.77, BIC = 787.27
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.96, *SE* = 3.599, *z* = -0.267, *p* = 0.790
- **Small (with 1) vs Crossover (with 1)**: *β* = 3.97, *SE* = 3.968, *z* = 1.001, *p* = 0.317
- **Small (without 1) vs Crossover (with 1)**: *β* = 7.47, *SE* = 4.779, *z* = 1.564, *p* = 0.118
- **SNR**: *β* = 0.74, *SE* = 0.452, *z* = 1.632, *p* = 0.103

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.96 | 3.60 | 0.27 | 0.790 | 0.790 | n.s. |
| Crossover (with 1) - Small (with 1) | -3.97 | 3.97 | -1.00 | 0.317 | 0.681 | n.s. |
| Crossover (with 1) - Small (without 1) | -7.47 | 4.78 | -1.56 | 0.118 | 0.466 | n.s. |
| Crossover (without 1) - Small (with 1) | -4.93 | 3.80 | -1.30 | 0.194 | 0.578 | n.s. |
| Crossover (without 1) - Small (without 1) | -8.43 | 4.49 | -1.88 | 0.060 | 0.312 | n.s. |
| Small (with 1) - Small (without 1) | -3.50 | 3.95 | -0.89 | 0.376 | 0.681 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.51, *p* = 0.678, η²_G = 0.011
- Greenhouse-Geisser corrected: *p* = 0.570 (ε = 0.549)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.78 | 20 | = 0.648 | 0.10 [-0.26, 0.62] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.22 | 20 | = 0.825 | -0.06 [-0.50, 0.39] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.62 | 20 | = 0.648 | -0.18 [-0.59, 0.32] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.64 | 20 | = 0.648 | -0.16 [-0.59, 0.30] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.99 | 20 | = 0.648 | -0.28 [-0.68, 0.24] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.79 | 20 | = 0.648 | -0.13 [-0.63, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 307.91, BIC = 325.41
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.08, *SE* = 0.272, *z* = -0.293, *p* = 0.770
- **Small (with 1) vs Crossover (with 1)**: *β* = -0.30, *SE* = 0.297, *z* = -1.009, *p* = 0.313
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.69, *SE* = 0.348, *z* = -1.997, *p* = 0.046
- **SNR**: *β* = -0.16, *SE* = 0.032, *z* = -4.910, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.08 | 0.27 | 0.29 | 0.770 | 0.770 | n.s. |
| Crossover (with 1) - Small (with 1) | 0.30 | 0.30 | 1.01 | 0.313 | 0.676 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.69 | 0.35 | 2.00 | 0.046 | 0.245 | n.s. |
| Crossover (without 1) - Small (with 1) | 0.22 | 0.29 | 0.77 | 0.441 | 0.688 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.61 | 0.33 | 1.87 | 0.062 | 0.272 | n.s. |
| Small (with 1) - Small (without 1) | 0.39 | 0.29 | 1.34 | 0.180 | 0.549 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.659, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.553 (ε = 0.541)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -1.94 | 20 | = 0.401 | -0.07 [-0.70, 0.18] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.81 | 20 | = 0.749 | -0.15 [-0.60, 0.29] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.93 | 20 | = 0.749 | -0.20 [-0.66, 0.26] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.47 | 20 | = 0.749 | -0.08 [-0.55, 0.34] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.68 | 20 | = 0.749 | -0.14 [-0.61, 0.31] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | -0.32 | 20 | = 0.749 | -0.05 [-0.53, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 393.50, BIC = 407.29
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.79, *SE* = 2.777, *z* = 0.285, *p* = 0.775
- **Small (with 1) vs Crossover (with 1)**: *β* = -1.25, *SE* = 2.942, *z* = -0.426, *p* = 0.670
- **Small (without 1) vs Crossover (with 1)**: *β* = -1.13, *SE* = 3.141, *z* = -0.360, *p* = 0.719
- **SNR**: *β* = 0.94, *SE* = 0.531, *z* = 1.777, *p* = 0.076

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.79 | 2.78 | -0.29 | 0.775 | 0.988 | n.s. |
| Crossover (with 1) - Small (with 1) | 1.25 | 2.94 | 0.43 | 0.670 | 0.988 | n.s. |
| Crossover (with 1) - Small (without 1) | 1.13 | 3.14 | 0.36 | 0.719 | 0.988 | n.s. |
| Crossover (without 1) - Small (with 1) | 2.05 | 2.88 | 0.71 | 0.478 | 0.980 | n.s. |
| Crossover (without 1) - Small (without 1) | 1.92 | 3.04 | 0.63 | 0.527 | 0.980 | n.s. |
| Small (with 1) - Small (without 1) | -0.12 | 3.11 | -0.04 | 0.968 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.86, *p* = 0.179, η²_G = 0.143
- Greenhouse-Geisser corrected: *p* = 0.211 (ε = 0.592)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.00 | 5 | = 1.000 | 0.00 [-0.85, 0.51] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.57 | 5 | = 0.714 | 0.34 [-0.52, 0.93] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 1.90 | 5 | = 0.348 | 0.85 [-0.43, 1.32] | large | n.s. |
| Crossover (without 1) vs Small (with 1) | 0.68 | 5 | = 0.714 | 0.36 [-0.46, 0.99] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 2.09 | 5 | = 0.348 | 0.87 [-0.36, 1.42] | large | n.s. |
| Small (with 1) vs Small (without 1) | 1.31 | 5 | = 0.496 | 0.46 [-0.47, 1.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 169.26, BIC = 183.06
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.07, *SE* = 0.381, *z* = 0.186, *p* = 0.852
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.36, *SE* = 0.401, *z* = 0.901, *p* = 0.367
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.88, *SE* = 0.417, *z* = 4.508, *p* < .001
- **SNR**: *β* = 0.43, *SE* = 0.073, *z* = 5.877, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.07 | 0.38 | -0.19 | 0.852 | 0.852 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.36 | 0.40 | -0.90 | 0.367 | 0.747 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.88 | 0.42 | -4.51 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.29 | 0.39 | -0.75 | 0.456 | 0.747 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.81 | 0.40 | -4.56 | < .001 | < .001 | *** |
| Small (with 1) - Small (without 1) | -1.52 | 0.41 | -3.66 | < .001 | 0.001 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.878, η²_G = 0.019
- Greenhouse-Geisser corrected: *p* = 0.682 (ε = 0.376)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.47 | 5 | = 0.826 | 0.06 [-0.59, 0.76] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.66 | 5 | = 0.826 | 0.25 [-0.40, 1.07] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.23 | 5 | = 0.826 | -0.14 [-1.16, 0.55] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | 0.35 | 5 | = 0.826 | 0.14 [-0.87, 0.57] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.31 | 5 | = 0.826 | -0.18 [-1.24, 0.49] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | -1.25 | 5 | = 0.826 | -0.46 [-1.46, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 768.12, BIC = 784.34
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 15.15, *SE* = 10.302, *z* = 1.470, *p* = 0.141
- **Small (with 1) vs Crossover (with 1)**: *β* = -2.41, *SE* = 10.349, *z* = -0.233, *p* = 0.816
- **Small (without 1) vs Crossover (with 1)**: *β* = -3.66, *SE* = 11.050, *z* = -0.331, *p* = 0.740
- **SNR**: *β* = 0.20, *SE* = 0.999, *z* = 0.197, *p* = 0.844

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -15.15 | 10.30 | -1.47 | 0.141 | 0.457 | n.s. |
| Crossover (with 1) - Small (with 1) | 2.41 | 10.35 | 0.23 | 0.816 | 0.982 | n.s. |
| Crossover (with 1) - Small (without 1) | 3.66 | 11.05 | 0.33 | 0.740 | 0.982 | n.s. |
| Crossover (without 1) - Small (with 1) | 17.56 | 10.35 | 1.70 | 0.090 | 0.398 | n.s. |
| Crossover (without 1) - Small (without 1) | 18.81 | 10.78 | 1.74 | 0.081 | 0.398 | n.s. |
| Small (with 1) - Small (without 1) | 1.25 | 10.82 | 0.12 | 0.908 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.44, *p* = 0.244, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -1.76 | 16 | = 0.194 | -0.41 [-0.91, 0.09] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.28 | 16 | = 0.941 | 0.09 [-0.49, 0.50] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.22 | 16 | = 0.941 | 0.07 [-0.46, 0.57] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | 1.96 | 16 | = 0.194 | 0.50 [-0.16, 0.87] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 1.93 | 16 | = 0.194 | 0.47 [-0.07, 1.01] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.08 | 16 | = 0.941 | -0.02 [-0.52, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 299.89, BIC = 316.11
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.08, *SE* = 0.384, *z* = 0.203, *p* = 0.839
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.49, *SE* = 0.386, *z* = 1.277, *p* = 0.202
- **Small (without 1) vs Crossover (with 1)**: *β* = 2.46, *SE* = 0.422, *z* = 5.829, *p* < .001
- **SNR**: *β* = 0.16, *SE* = 0.045, *z* = 3.510, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.08 | 0.38 | -0.20 | 0.839 | 0.839 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.49 | 0.39 | -1.28 | 0.202 | 0.491 | n.s. |
| Crossover (with 1) - Small (without 1) | -2.46 | 0.42 | -5.83 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.42 | 0.39 | -1.07 | 0.282 | 0.491 | n.s. |
| Crossover (without 1) - Small (without 1) | -2.38 | 0.41 | -5.85 | < .001 | < .001 | *** |
| Small (with 1) - Small (without 1) | -1.97 | 0.41 | -4.79 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.15, *p* < .001, η²_G = 0.074
- Greenhouse-Geisser corrected: *p* = 0.003 (ε = 0.532)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.62 | 16 | = 0.543 | 0.03 [-0.29, 0.68] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.96 | 16 | = 0.419 | -0.14 [-0.81, 0.20] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -3.31 | 16 | = 0.010 | -0.62 [-1.39, -0.21] | medium | ** |
| Crossover (without 1) vs Small (with 1) | -1.04 | 16 | = 0.419 | -0.16 [-0.83, 0.19] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -3.27 | 16 | = 0.010 | -0.66 [-1.38, -0.20] | medium | ** |
| Small (with 1) vs Small (without 1) | -3.45 | 16 | = 0.010 | -0.47 [-1.48, -0.31] | small | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Crossover (with 1) showed smaller amplitude than Small (without 1) (*d* = -0.62)
  - Crossover (without 1) showed smaller amplitude than Small (without 1) (*d* = -0.66)
  - Small (with 1) showed smaller amplitude than Small (without 1) (*d* = -0.47)

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
