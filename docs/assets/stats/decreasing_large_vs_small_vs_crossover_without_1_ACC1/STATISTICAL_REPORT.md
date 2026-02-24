# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:19:16

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
| Decreasing Crossover (no 1) | 24 | 106.17 ms | 7.82 | 1.60 | [96.00, 116.00] |
| Decreasing Large (no 1) | 24 | 107.50 ms | 7.58 | 1.55 | [96.00, 116.00] |
| Decreasing Small (no 1) | 24 | 105.83 ms | 8.98 | 1.83 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | -1.32 µV | 1.42 | 0.29 | [-5.22, 1.43] |
| Decreasing Large (no 1) | 24 | -1.71 µV | 1.97 | 0.40 | [-7.59, 1.04] |
| Decreasing Small (no 1) | 24 | -1.31 µV | 2.28 | 0.46 | [-5.62, 2.93] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 172.83 ms | 14.92 | 3.05 | [148.00, 208.00] |
| Decreasing Large (no 1) | 24 | 177.33 ms | 19.33 | 3.95 | [144.00, 212.00] |
| Decreasing Small (no 1) | 24 | 176.17 ms | 24.13 | 4.93 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | -5.88 µV | 1.98 | 0.40 | [-9.79, -2.32] |
| Decreasing Large (no 1) | 24 | -5.75 µV | 2.36 | 0.48 | [-11.18, -2.00] |
| Decreasing Small (no 1) | 24 | -5.94 µV | 2.56 | 0.52 | [-10.33, -1.67] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 111.33 ms | 7.14 | 1.46 | [104.00, 120.00] |
| Decreasing Large (no 1) | 24 | 112.50 ms | 7.01 | 1.43 | [104.00, 120.00] |
| Decreasing Small (no 1) | 24 | 112.83 ms | 7.27 | 1.48 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 1.13 µV | 1.76 | 0.36 | [-2.63, 4.25] |
| Decreasing Large (no 1) | 24 | 1.34 µV | 2.65 | 0.54 | [-4.36, 6.31] |
| Decreasing Small (no 1) | 24 | 0.51 µV | 2.31 | 0.47 | [-2.89, 6.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 473.83 ms | 25.19 | 5.14 | [436.00, 540.00] |
| Decreasing Large (no 1) | 24 | 489.33 ms | 36.27 | 7.40 | [432.00, 540.00] |
| Decreasing Small (no 1) | 24 | 488.50 ms | 34.35 | 7.01 | [432.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 4.00 µV | 3.28 | 0.67 | [-1.77, 10.85] |
| Decreasing Large (no 1) | 24 | 3.75 µV | 3.43 | 0.70 | [-4.03, 9.67] |
| Decreasing Small (no 1) | 24 | 5.31 µV | 4.41 | 0.90 | [-1.20, 17.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 506.51, BIC = 520.17
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.43, *SE* = 1.849, *z* = 0.773, *p* = 0.440
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.08, *SE* = 1.877, *z* = -0.045, *p* = 0.964
- **SNR**: *β* = 0.35, *SE* = 0.487, *z* = 0.714, *p* = 0.476

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -1.43 | 1.85 | -0.77 | 0.440 | 0.800 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.08 | 1.88 | 0.04 | 0.964 | 0.964 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 1.51 | 1.86 | 0.81 | 0.415 | 0.800 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.648, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.95 | 23 | = 0.686 | -0.17 [-0.62, 0.23] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.17 | 23 | = 0.866 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.76 | 23 | = 0.686 | 0.20 [-0.27, 0.58] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 290.85, BIC = 304.51
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.50, *SE* = 0.445, *z* = -1.124, *p* = 0.261
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.28, *SE* = 0.451, *z* = -0.613, *p* = 0.540
- **SNR**: *β* = -0.41, *SE* = 0.110, *z* = -3.704, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.50 | 0.45 | 1.12 | 0.261 | 0.597 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.28 | 0.45 | 0.61 | 0.540 | 0.789 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.22 | 0.45 | -0.50 | 0.616 | 0.789 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.45, *p* = 0.639, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 1.02 | 23 | = 0.750 | 0.23 [-0.22, 0.63] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.03 | 23 | = 0.974 | -0.01 [-0.43, 0.42] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.68 | 23 | = 0.750 | -0.19 [-0.56, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 633.70, BIC = 647.36
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 4.97, *SE* = 4.723, *z* = 1.053, *p* = 0.292
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 4.01, *SE* = 5.068, *z* = 0.792, *p* = 0.428
- **SNR**: *β* = 0.13, *SE* = 0.500, *z* = 0.266, *p* = 0.790

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -4.97 | 4.72 | -1.05 | 0.292 | 0.646 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -4.02 | 5.07 | -0.79 | 0.428 | 0.673 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.96 | 4.44 | 0.22 | 0.829 | 0.829 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.586, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -1.49 | 23 | = 0.449 | -0.26 [-0.74, 0.13] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.66 | 23 | = 0.776 | -0.17 [-0.56, 0.29] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.23 | 23 | = 0.820 | 0.05 [-0.38, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 298.83, BIC = 312.49
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.32, *SE* = 0.418, *z* = -0.766, *p* = 0.443
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.72, *SE* = 0.451, *z* = -1.589, *p* = 0.112
- **SNR**: *β* = -0.13, *SE* = 0.046, *z* = -2.769, *p* = 0.006

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.32 | 0.42 | 0.77 | 0.443 | 0.524 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.72 | 0.45 | 1.59 | 0.112 | 0.300 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.40 | 0.39 | 1.02 | 0.310 | 0.524 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.885, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.44 | 23 | = 0.888 | -0.06 [-0.51, 0.33] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.14 | 23 | = 0.888 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.41 | 23 | = 0.888 | 0.08 [-0.34, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 476.67, BIC = 490.33
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.08, *SE* = 1.378, *z* = 0.784, *p* = 0.433
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.15, *SE* = 1.486, *z* = 0.774, *p* = 0.439
- **SNR**: *β* = -0.20, *SE* = 0.325, *z* = -0.607, *p* = 0.544

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -1.08 | 1.38 | -0.78 | 0.433 | 0.818 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -1.15 | 1.49 | -0.77 | 0.439 | 0.818 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.07 | 1.44 | -0.05 | 0.961 | 0.961 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.538, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.84 | 23 | = 0.616 | -0.16 [-0.60, 0.25] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.44 | 23 | = 0.493 | -0.21 [-0.72, 0.14] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.20 | 23 | = 0.846 | -0.05 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 308.85, BIC = 322.51
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.23, *SE* = 0.425, *z* = 0.537, *p* = 0.591
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.56, *SE* = 0.465, *z* = -1.209, *p* = 0.227
- **SNR**: *β* = 0.03, *SE* = 0.109, *z* = 0.272, *p* = 0.786

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.23 | 0.43 | -0.54 | 0.591 | 0.591 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.56 | 0.46 | 1.21 | 0.227 | 0.402 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.79 | 0.45 | 1.77 | 0.077 | 0.213 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.02, *p* = 0.145, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.66 | 23 | = 0.518 | -0.10 [-0.56, 0.29] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 1.50 | 23 | = 0.220 | 0.30 [-0.13, 0.74] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 1.58 | 23 | = 0.220 | 0.33 [-0.11, 0.76] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 699.20, BIC = 712.86
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 12.89, *SE* = 7.197, *z* = 1.792, *p* = 0.073
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 11.27, *SE* = 7.555, *z* = 1.492, *p* = 0.136
- **SNR**: *β* = -0.62, *SE* = 0.653, *z* = -0.947, *p* = 0.344

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -12.90 | 7.20 | -1.79 | 0.073 | 0.204 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -11.27 | 7.55 | -1.49 | 0.136 | 0.253 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 1.62 | 6.70 | 0.24 | 0.809 | 0.809 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.21, *p* = 0.050, η²_G = 0.048
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.26 | 23 | = 0.051 | -0.50 [-0.90, -0.02] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -2.51 | 23 | = 0.051 | -0.49 [-0.96, -0.06] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.11 | 23 | = 0.916 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 354.69, BIC = 368.35
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.35, *SE* = 0.577, *z* = 0.609, *p* = 0.542
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 2.09, *SE* = 0.609, *z* = 3.440, *p* = 0.001
- **SNR**: *β* = 0.14, *SE* = 0.055, *z* = 2.565, *p* = 0.010

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.35 | 0.58 | -0.61 | 0.542 | 0.542 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -2.09 | 0.61 | -3.44 | < .001 | 0.002 | ** |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -1.74 | 0.53 | -3.28 | 0.001 | 0.002 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.55, *p* = 0.016, η²_G = 0.034
- Greenhouse-Geisser corrected: *p* = 0.027 (ε = 0.745)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 0.49 | 23 | = 0.631 | 0.07 [-0.32, 0.52] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -3.06 | 23 | = 0.017 | -0.34 [-1.09, -0.16] | small | * |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -2.24 | 23 | = 0.053 | -0.40 [-0.90, -0.01] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Significant main effect of condition (*p* = 0.050) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.016). Post-hoc tests revealed:
  - Decreasing Crossover (no 1) showed smaller amplitude than Decreasing Small (no 1) (*d* = -0.34)

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
