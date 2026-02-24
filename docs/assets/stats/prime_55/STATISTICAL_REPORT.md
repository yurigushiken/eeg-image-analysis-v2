# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:32:01

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
| 5a | 24 | 106.17 ms | 8.34 | 1.70 | [92.00, 116.00] |
| 5b | 24 | 105.83 ms | 8.83 | 1.80 | [92.00, 116.00] |
| 5c | 24 | 103.17 ms | 9.58 | 1.96 | [92.00, 116.00] |
| 5d | 24 | 103.50 ms | 9.31 | 1.90 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 24 | -4.29 µV | 6.11 | 1.25 | [-24.72, 4.01] |
| 5b | 24 | -3.53 µV | 3.79 | 0.77 | [-14.79, 3.24] |
| 5c | 24 | -4.27 µV | 4.63 | 0.95 | [-14.70, 6.28] |
| 5d | 24 | -2.21 µV | 3.27 | 0.67 | [-8.22, 4.63] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 24 | 173.17 ms | 22.46 | 4.58 | [132.00, 204.00] |
| 5b | 24 | 168.67 ms | 20.35 | 4.15 | [132.00, 204.00] |
| 5c | 24 | 166.00 ms | 21.20 | 4.33 | [132.00, 204.00] |
| 5d | 24 | 171.50 ms | 19.57 | 4.00 | [132.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 24 | -5.62 µV | 6.20 | 1.27 | [-19.03, 6.70] |
| 5b | 24 | -5.13 µV | 3.53 | 0.72 | [-12.77, 1.54] |
| 5c | 24 | -7.19 µV | 3.13 | 0.64 | [-12.80, 1.97] |
| 5d | 24 | -6.45 µV | 3.01 | 0.61 | [-13.37, 0.35] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 24 | 68.17 ms | 34.80 | 7.10 | [12.00, 112.00] |
| 5b | 24 | 64.67 ms | 33.27 | 6.79 | [12.00, 112.00] |
| 5c | 24 | 70.17 ms | 36.41 | 7.43 | [12.00, 112.00] |
| 5d | 24 | 75.17 ms | 31.10 | 6.35 | [12.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 24 | 6.66 µV | 5.35 | 1.09 | [-1.91, 21.05] |
| 5b | 24 | 4.25 µV | 2.74 | 0.56 | [0.12, 9.32] |
| 5c | 24 | 4.19 µV | 3.37 | 0.69 | [-1.56, 8.61] |
| 5d | 24 | 3.70 µV | 2.39 | 0.49 | [-0.31, 8.70] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 24 | 358.33 ms | 11.73 | 2.39 | [340.00, 372.00] |
| 5b | 24 | 359.00 ms | 12.22 | 2.49 | [340.00, 372.00] |
| 5c | 24 | 354.83 ms | 11.88 | 2.43 | [340.00, 372.00] |
| 5d | 24 | 355.67 ms | 13.39 | 2.73 | [340.00, 372.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a | 24 | 4.01 µV | 6.21 | 1.27 | [-7.39, 23.34] |
| 5b | 24 | 1.74 µV | 2.19 | 0.45 | [-2.50, 6.37] |
| 5c | 24 | 1.80 µV | 2.90 | 0.59 | [-3.06, 8.04] |
| 5d | 24 | 1.40 µV | 2.94 | 0.60 | [-5.04, 6.83] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 699.72, BIC = 717.67
- **5b vs 5a**: *β* = -0.35, *SE* = 2.279, *z* = -0.154, *p* = 0.877
- **5c vs 5a**: *β* = -3.06, *SE* = 2.280, *z* = -1.341, *p* = 0.180
- **5d vs 5a**: *β* = -2.77, *SE* = 2.284, *z* = -1.212, *p* = 0.225
- **SNR**: *β* = 0.33, *SE* = 0.517, *z* = 0.646, *p* = 0.518

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 0.35 | 2.28 | 0.15 | 0.877 | 0.985 | n.s. |
| 5a - 5c | 3.06 | 2.28 | 1.34 | 0.180 | 0.696 | n.s. |
| 5a - 5d | 2.77 | 2.28 | 1.21 | 0.225 | 0.721 | n.s. |
| 5b - 5c | 2.71 | 2.28 | 1.19 | 0.235 | 0.721 | n.s. |
| 5b - 5d | 2.42 | 2.28 | 1.06 | 0.290 | 0.721 | n.s. |
| 5c - 5d | -0.29 | 2.28 | -0.13 | 0.899 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.454, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | 0.13 | 23 | = 0.895 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 5a vs 5c | 1.30 | 23 | = 0.487 | 0.33 [-0.16, 0.69] | small | n.s. |
| 5a vs 5d | 1.24 | 23 | = 0.487 | 0.30 [-0.18, 0.68] | small | n.s. |
| 5b vs 5c | 1.20 | 23 | = 0.487 | 0.29 [-0.18, 0.67] | small | n.s. |
| 5b vs 5d | 1.01 | 23 | = 0.488 | 0.26 [-0.22, 0.63] | small | n.s. |
| 5c vs 5d | -0.13 | 23 | = 0.895 | -0.04 [-0.45, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 569.42, BIC = 587.37
- **5b vs 5a**: *β* = 0.79, *SE* = 1.223, *z* = 0.649, *p* = 0.517
- **5c vs 5a**: *β* = 0.11, *SE* = 1.224, *z* = 0.091, *p* = 0.927
- **5d vs 5a**: *β* = 2.24, *SE* = 1.226, *z* = 1.825, *p* = 0.068
- **SNR**: *β* = -0.53, *SE* = 0.267, *z* = -1.985, *p* = 0.047

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -0.79 | 1.22 | -0.65 | 0.517 | 0.887 | n.s. |
| 5a - 5c | -0.11 | 1.22 | -0.09 | 0.927 | 0.927 | n.s. |
| 5a - 5d | -2.24 | 1.23 | -1.83 | 0.068 | 0.344 | n.s. |
| 5b - 5c | 0.68 | 1.22 | 0.56 | 0.577 | 0.887 | n.s. |
| 5b - 5d | -1.44 | 1.23 | -1.18 | 0.238 | 0.664 | n.s. |
| 5c - 5d | -2.13 | 1.22 | -1.74 | 0.082 | 0.349 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.20, *p* = 0.317, η²_G = 0.034
- Greenhouse-Geisser corrected: *p* = 0.313 (ε = 0.713)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | -0.52 | 23 | = 0.729 | -0.15 [-0.53, 0.32] | negligible | n.s. |
| 5a vs 5c | -0.01 | 23 | = 0.991 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| 5a vs 5d | -1.56 | 23 | = 0.385 | -0.42 [-0.75, 0.11] | small | n.s. |
| 5b vs 5c | 0.83 | 23 | = 0.623 | 0.18 [-0.26, 0.59] | negligible | n.s. |
| 5b vs 5d | -1.34 | 23 | = 0.385 | -0.37 [-0.70, 0.16] | small | n.s. |
| 5c vs 5d | -1.91 | 23 | = 0.385 | -0.51 [-0.83, 0.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 861.97, BIC = 879.92
- **5b vs 5a**: *β* = -4.45, *SE* = 5.340, *z* = -0.834, *p* = 0.404
- **5c vs 5a**: *β* = -7.10, *SE* = 5.345, *z* = -1.329, *p* = 0.184
- **5d vs 5a**: *β* = -1.53, *SE* = 5.381, *z* = -0.284, *p* = 0.776
- **SNR**: *β* = -0.26, *SE* = 1.327, *z* = -0.196, *p* = 0.845

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 4.45 | 5.34 | 0.83 | 0.404 | 0.874 | n.s. |
| 5a - 5c | 7.10 | 5.34 | 1.33 | 0.184 | 0.705 | n.s. |
| 5a - 5d | 1.53 | 5.38 | 0.28 | 0.776 | 0.928 | n.s. |
| 5b - 5c | 2.65 | 5.34 | 0.50 | 0.620 | 0.928 | n.s. |
| 5b - 5d | -2.93 | 5.36 | -0.55 | 0.585 | 0.928 | n.s. |
| 5c - 5d | -5.57 | 5.35 | -1.04 | 0.297 | 0.829 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.572, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | 0.69 | 23 | = 0.655 | 0.21 [-0.28, 0.56] | small | n.s. |
| 5a vs 5c | 1.09 | 23 | = 0.655 | 0.33 [-0.21, 0.65] | small | n.s. |
| 5a vs 5d | 0.28 | 23 | = 0.778 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| 5b vs 5c | 0.61 | 23 | = 0.655 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| 5b vs 5d | -0.63 | 23 | = 0.655 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 5c vs 5d | -1.29 | 23 | = 0.655 | -0.27 [-0.69, 0.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 540.94, BIC = 558.89
- **5b vs 5a**: *β* = 0.63, *SE* = 1.005, *z* = 0.629, *p* = 0.529
- **5c vs 5a**: *β* = -1.36, *SE* = 1.006, *z* = -1.348, *p* = 0.178
- **5d vs 5a**: *β* = -0.37, *SE* = 1.013, *z* = -0.368, *p* = 0.713
- **SNR**: *β* = -0.86, *SE* = 0.250, *z* = -3.444, *p* = 0.001

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -0.63 | 1.00 | -0.63 | 0.529 | 0.785 | n.s. |
| 5a - 5c | 1.36 | 1.01 | 1.35 | 0.178 | 0.624 | n.s. |
| 5a - 5d | 0.37 | 1.01 | 0.37 | 0.713 | 0.785 | n.s. |
| 5b - 5c | 1.99 | 1.00 | 1.98 | 0.048 | 0.254 | n.s. |
| 5b - 5d | 1.00 | 1.01 | 1.00 | 0.319 | 0.785 | n.s. |
| 5c - 5d | -0.98 | 1.01 | -0.98 | 0.329 | 0.785 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.41, *p* = 0.246, η²_G = 0.036
- Greenhouse-Geisser corrected: *p* = 0.254 (ε = 0.617)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | -0.36 | 23 | = 0.723 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| 5a vs 5c | 1.28 | 23 | = 0.425 | 0.32 [-0.17, 0.69] | small | n.s. |
| 5a vs 5d | 0.58 | 23 | = 0.682 | 0.17 [-0.31, 0.54] | negligible | n.s. |
| 5b vs 5c | 2.87 | 23 | = 0.052 | 0.61 [0.13, 1.04] | medium | n.s. |
| 5b vs 5d | 1.64 | 23 | = 0.343 | 0.40 [-0.10, 0.77] | small | n.s. |
| 5c vs 5d | -1.07 | 23 | = 0.445 | -0.24 [-0.65, 0.21] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 955.53, BIC = 973.48
- **5b vs 5a**: *β* = -3.58, *SE* = 8.802, *z* = -0.407, *p* = 0.684
- **5c vs 5a**: *β* = 2.73, *SE* = 8.818, *z* = 0.309, *p* = 0.757
- **5d vs 5a**: *β* = 6.25, *SE* = 8.819, *z* = 0.709, *p* = 0.478
- **SNR**: *β* = -5.49, *SE* = 3.952, *z* = -1.388, *p* = 0.165

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 3.58 | 8.80 | 0.41 | 0.684 | 0.968 | n.s. |
| 5a - 5c | -2.72 | 8.82 | -0.31 | 0.757 | 0.968 | n.s. |
| 5a - 5d | -6.25 | 8.82 | -0.71 | 0.478 | 0.960 | n.s. |
| 5b - 5c | -6.31 | 8.82 | -0.71 | 0.475 | 0.960 | n.s. |
| 5b - 5d | -9.83 | 8.82 | -1.12 | 0.265 | 0.842 | n.s. |
| 5c - 5d | -3.53 | 8.87 | -0.40 | 0.691 | 0.968 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.45, *p* = 0.716, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | 0.38 | 23 | = 0.838 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| 5a vs 5c | -0.21 | 23 | = 0.838 | -0.06 [-0.46, 0.38] | negligible | n.s. |
| 5a vs 5d | -0.88 | 23 | = 0.838 | -0.21 [-0.60, 0.25] | small | n.s. |
| 5b vs 5c | -0.62 | 23 | = 0.838 | -0.16 [-0.55, 0.30] | negligible | n.s. |
| 5b vs 5d | -1.15 | 23 | = 0.838 | -0.33 [-0.66, 0.19] | small | n.s. |
| 5c vs 5d | -0.48 | 23 | = 0.838 | -0.15 [-0.52, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 527.49, BIC = 545.44
- **5b vs 5a**: *β* = -2.40, *SE* = 0.968, *z* = -2.476, *p* = 0.013
- **5c vs 5a**: *β* = -2.54, *SE* = 0.969, *z* = -2.626, *p* = 0.009
- **5d vs 5a**: *β* = -2.88, *SE* = 0.969, *z* = -2.968, *p* = 0.003
- **SNR**: *β* = 0.60, *SE* = 0.415, *z* = 1.444, *p* = 0.149

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 2.40 | 0.97 | 2.48 | 0.013 | 0.052 | n.s. |
| 5a - 5c | 2.55 | 0.97 | 2.63 | 0.009 | 0.042 | * |
| 5a - 5d | 2.88 | 0.97 | 2.97 | 0.003 | 0.018 | * |
| 5b - 5c | 0.15 | 0.97 | 0.15 | 0.877 | 0.945 | n.s. |
| 5b - 5d | 0.48 | 0.97 | 0.50 | 0.619 | 0.945 | n.s. |
| 5c - 5d | 0.33 | 0.97 | 0.34 | 0.733 | 0.945 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.52, *p* = 0.019, η²_G = 0.094
- Greenhouse-Geisser corrected: *p* = 0.034 (ε = 0.720)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | 1.99 | 23 | = 0.118 | 0.57 [-0.03, 0.84] | medium | n.s. |
| 5a vs 5c | 1.99 | 23 | = 0.118 | 0.55 [-0.03, 0.84] | medium | n.s. |
| 5a vs 5d | 2.64 | 23 | = 0.088 | 0.71 [0.09, 0.99] | medium | n.s. |
| 5b vs 5c | 0.07 | 23 | = 0.943 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 5b vs 5d | 0.72 | 23 | = 0.575 | 0.22 [-0.28, 0.57] | small | n.s. |
| 5c vs 5d | 0.76 | 23 | = 0.575 | 0.17 [-0.27, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 762.82, BIC = 780.77
- **5b vs 5a**: *β* = 0.45, *SE* = 3.355, *z* = 0.135, *p* = 0.892
- **5c vs 5a**: *β* = -3.36, *SE* = 3.351, *z* = -1.003, *p* = 0.316
- **5d vs 5a**: *β* = -3.03, *SE* = 3.369, *z* = -0.900, *p* = 0.368
- **SNR**: *β* = 0.80, *SE* = 0.818, *z* = 0.983, *p* = 0.326

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | -0.45 | 3.36 | -0.14 | 0.892 | 0.988 | n.s. |
| 5a - 5c | 3.36 | 3.35 | 1.00 | 0.316 | 0.832 | n.s. |
| 5a - 5d | 3.03 | 3.37 | 0.90 | 0.368 | 0.832 | n.s. |
| 5b - 5c | 3.82 | 3.37 | 1.13 | 0.257 | 0.832 | n.s. |
| 5b - 5d | 3.49 | 3.35 | 1.04 | 0.298 | 0.832 | n.s. |
| 5c - 5d | -0.33 | 3.39 | -0.10 | 0.923 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.556, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | -0.20 | 23 | = 0.846 | -0.06 [-0.46, 0.38] | negligible | n.s. |
| 5a vs 5c | 1.03 | 23 | = 0.658 | 0.30 [-0.22, 0.64] | small | n.s. |
| 5a vs 5d | 0.68 | 23 | = 0.754 | 0.21 [-0.29, 0.56] | small | n.s. |
| 5b vs 5c | 1.40 | 23 | = 0.658 | 0.35 [-0.14, 0.72] | small | n.s. |
| 5b vs 5d | 1.00 | 23 | = 0.658 | 0.26 [-0.22, 0.63] | small | n.s. |
| 5c vs 5d | -0.24 | 23 | = 0.846 | -0.07 [-0.47, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 530.47, BIC = 548.42
- **5b vs 5a**: *β* = -2.43, *SE* = 0.930, *z* = -2.613, *p* = 0.009
- **5c vs 5a**: *β* = -2.10, *SE* = 0.929, *z* = -2.258, *p* = 0.024
- **5d vs 5a**: *β* = -2.89, *SE* = 0.934, *z* = -3.094, *p* = 0.002
- **SNR**: *β* = 0.62, *SE* = 0.237, *z* = 2.612, *p* = 0.009

_Reference condition: **5a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a - 5b | 2.43 | 0.93 | 2.61 | 0.009 | 0.044 | * |
| 5a - 5c | 2.10 | 0.93 | 2.26 | 0.024 | 0.092 | n.s. |
| 5a - 5d | 2.89 | 0.93 | 3.09 | 0.002 | 0.012 | * |
| 5b - 5c | -0.33 | 0.93 | -0.36 | 0.721 | 0.856 | n.s. |
| 5b - 5d | 0.46 | 0.93 | 0.50 | 0.620 | 0.856 | n.s. |
| 5c - 5d | 0.79 | 0.94 | 0.84 | 0.399 | 0.782 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.91, *p* = 0.041, η²_G = 0.069
- Greenhouse-Geisser corrected: *p* = 0.075 (ε = 0.562)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a vs 5b | 1.81 | 23 | = 0.166 | 0.49 [-0.07, 0.81] | small | n.s. |
| 5a vs 5c | 2.00 | 23 | = 0.166 | 0.45 [-0.03, 0.85] | small | n.s. |
| 5a vs 5d | 1.96 | 23 | = 0.166 | 0.54 [-0.04, 0.84] | medium | n.s. |
| 5b vs 5c | -0.09 | 23 | = 0.928 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 5b vs 5d | 0.77 | 23 | = 0.675 | 0.13 [-0.27, 0.58] | negligible | n.s. |
| 5c vs 5d | 0.51 | 23 | = 0.741 | 0.14 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.019) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.041) (no significant pairwise comparisons)

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
