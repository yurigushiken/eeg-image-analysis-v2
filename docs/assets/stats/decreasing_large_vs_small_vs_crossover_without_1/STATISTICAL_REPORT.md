# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:34:25

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
| Decreasing Crossover (no 1) | 5 | 99.20 ms | 10.73 | 4.80 | [92.00, 116.00] |
| Decreasing Large (no 1) | 10 | 107.60 ms | 11.38 | 3.60 | [92.00, 116.00] |
| Decreasing Small (no 1) | 11 | 103.27 ms | 10.56 | 3.18 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 5 | 1.93 µV | 0.85 | 0.38 | [1.01, 2.98] |
| Decreasing Large (no 1) | 10 | 1.97 µV | 1.04 | 0.33 | [0.49, 3.87] |
| Decreasing Small (no 1) | 11 | 2.97 µV | 1.90 | 0.57 | [0.87, 7.20] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 172.67 ms | 15.54 | 3.17 | [144.00, 208.00] |
| Decreasing Large (no 1) | 24 | 175.83 ms | 18.85 | 3.85 | [144.00, 212.00] |
| Decreasing Small (no 1) | 24 | 176.17 ms | 23.07 | 4.71 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | -5.84 µV | 2.00 | 0.41 | [-9.74, -2.14] |
| Decreasing Large (no 1) | 24 | -5.43 µV | 2.10 | 0.43 | [-10.35, -1.44] |
| Decreasing Small (no 1) | 24 | -5.79 µV | 2.54 | 0.52 | [-10.33, -1.35] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 16 | 112.75 ms | 7.04 | 1.76 | [100.00, 120.00] |
| Decreasing Large (no 1) | 13 | 112.62 ms | 7.97 | 2.21 | [100.00, 120.00] |
| Decreasing Small (no 1) | 11 | 108.36 ms | 6.80 | 2.05 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 16 | 1.99 µV | 1.28 | 0.32 | [0.21, 4.53] |
| Decreasing Large (no 1) | 13 | 2.94 µV | 2.13 | 0.59 | [0.68, 7.08] |
| Decreasing Small (no 1) | 11 | 2.54 µV | 1.70 | 0.51 | [0.54, 5.61] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 475.40 ms | 25.24 | 5.64 | [436.00, 536.00] |
| Decreasing Large (no 1) | 18 | 493.56 ms | 33.83 | 7.97 | [444.00, 540.00] |
| Decreasing Small (no 1) | 18 | 486.00 ms | 33.92 | 8.00 | [432.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 4.70 µV | 2.74 | 0.61 | [0.72, 10.85] |
| Decreasing Large (no 1) | 18 | 4.18 µV | 2.48 | 0.58 | [0.95, 8.30] |
| Decreasing Small (no 1) | 18 | 6.50 µV | 4.11 | 0.97 | [2.10, 17.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 205.58, BIC = 213.13
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 5.62, *SE* = 6.086, *z* = 0.924, *p* = 0.356
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.90, *SE* = 5.716, *z* = 0.332, *p* = 0.740
- **SNR**: *β* = -1.65, *SE* = 1.576, *z* = -1.046, *p* = 0.295

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -5.62 | 6.09 | -0.92 | 0.356 | 0.732 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -1.90 | 5.72 | -0.33 | 0.740 | 0.740 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 3.72 | 4.52 | 0.82 | 0.411 | 0.732 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.965, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | nan | 2 | n/a | 0.00 | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.19 | 2 | = 0.868 | -0.20 [-1.47, 1.04] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.19 | 2 | = 0.868 | -0.20 [-1.09, 1.01] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 91.47, BIC = 99.02
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.18, *SE* = 0.606, *z* = 1.951, *p* = 0.051
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.95, *SE* = 0.552, *z* = 3.523, *p* < .001
- **SNR**: *β* = 0.52, *SE* = 0.148, *z* = 3.477, *p* = 0.001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -1.18 | 0.61 | -1.95 | 0.051 | 0.100 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -1.95 | 0.55 | -3.52 | < .001 | 0.001 | ** |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.76 | 0.44 | -1.73 | 0.083 | 0.100 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.98, *p* = 0.452, η²_G = 0.219
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.74 | 2 | = 0.538 | -0.29 [-3.02, 2.17] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.08 | 2 | = 0.538 | -0.92 [-2.53, 0.52] | large | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.90 | 2 | = 0.538 | -0.68 [-1.44, 0.73] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 631.11, BIC = 644.77
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 2.91, *SE* = 4.637, *z* = 0.628, *p* = 0.530
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 3.12, *SE* = 4.970, *z* = 0.628, *p* = 0.530
- **SNR**: *β* = -0.07, *SE* = 0.424, *z* = -0.157, *p* = 0.875

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -2.91 | 4.64 | -0.63 | 0.530 | 0.896 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -3.12 | 4.97 | -0.63 | 0.530 | 0.896 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.21 | 4.41 | -0.05 | 0.962 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.685, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.625 (ε = 0.744)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -1.11 | 23 | = 0.742 | -0.18 [-0.65, 0.20] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.69 | 23 | = 0.742 | -0.18 [-0.57, 0.28] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.07 | 23 | = 0.948 | -0.02 [-0.44, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 293.31, BIC = 306.97
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.15, *SE* = 0.390, *z* = 0.379, *p* = 0.705
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.34, *SE* = 0.422, *z* = -0.810, *p* = 0.418
- **SNR**: *β* = -0.07, *SE* = 0.039, *z* = -1.793, *p* = 0.073

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.15 | 0.39 | -0.38 | 0.705 | 0.705 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.34 | 0.42 | 0.81 | 0.418 | 0.661 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.49 | 0.37 | 1.33 | 0.183 | 0.455 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.73, *p* = 0.488, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -1.48 | 23 | = 0.457 | -0.20 [-0.73, 0.13] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.13 | 23 | = 0.897 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.85 | 23 | = 0.609 | 0.15 [-0.25, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 269.41, BIC = 279.54
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -1.01, *SE* = 1.638, *z* = -0.620, *p* = 0.535
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -5.66, *SE* = 1.992, *z* = -2.844, *p* = 0.004
- **SNR**: *β* = -0.75, *SE* = 0.335, *z* = -2.235, *p* = 0.025

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 1.02 | 1.64 | 0.62 | 0.535 | 0.535 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 5.66 | 1.99 | 2.84 | 0.004 | 0.013 | * |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 4.65 | 2.16 | 2.15 | 0.032 | 0.062 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.641, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 0.70 | 6 | = 0.762 | 0.28 [-0.40, 0.89] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.76 | 6 | = 0.762 | 0.40 [-0.40, 1.20] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.26 | 6 | = 0.805 | 0.07 [-0.83, 1.02] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 145.57, BIC = 155.70
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.85, *SE* = 0.422, *z* = 2.024, *p* = 0.043
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.03, *SE* = 0.507, *z* = 2.023, *p* = 0.043
- **SNR**: *β* = 0.26, *SE* = 0.092, *z* = 2.809, *p* = 0.005

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.85 | 0.42 | -2.02 | 0.043 | 0.123 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -1.03 | 0.51 | -2.02 | 0.043 | 0.123 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.17 | 0.56 | -0.31 | 0.757 | 0.757 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.61, *p* = 0.019, η²_G = 0.141
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -3.37 | 6 | = 0.045 | -0.75 [-1.53, -0.07] | medium | * |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.37 | 6 | = 0.722 | 0.10 [-1.09, 0.48] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 2.42 | 6 | = 0.078 | 0.75 [-0.19, 2.02] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 539.34, BIC = 551.49
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 15.81, *SE* = 7.550, *z* = 2.094, *p* = 0.036
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 5.66, *SE* = 7.813, *z* = 0.724, *p* = 0.469
- **SNR**: *β* = -0.70, *SE* = 0.634, *z* = -1.110, *p* = 0.267

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -15.81 | 7.55 | -2.09 | 0.036 | 0.105 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -5.66 | 7.81 | -0.72 | 0.469 | 0.469 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 10.15 | 7.09 | 1.43 | 0.152 | 0.281 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.69, *p* = 0.037, η²_G = 0.083
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -3.09 | 15 | = 0.023 | -0.75 [-1.26, -0.15] | medium | * |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.21 | 15 | = 0.243 | -0.31 [-0.90, 0.13] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 1.35 | 15 | = 0.243 | 0.38 [-0.21, 0.88] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 262.88, BIC = 275.03
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.30, *SE* = 0.615, *z* = 0.494, *p* = 0.621
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 2.99, *SE* = 0.634, *z* = 4.708, *p* < .001
- **SNR**: *β* = 0.22, *SE* = 0.053, *z* = 4.100, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.30 | 0.62 | -0.49 | 0.621 | 0.621 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -2.99 | 0.63 | -4.71 | < .001 | < .001 | *** |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -2.68 | 0.57 | -4.69 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.05, *p* = 0.003, η²_G = 0.119
- Greenhouse-Geisser corrected: *p* = 0.008 (ε = 0.721)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 1.50 | 15 | = 0.154 | 0.38 [-0.18, 0.84] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -3.08 | 15 | = 0.016 | -0.51 [-1.29, -0.17] | medium | * |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -2.92 | 15 | = 0.016 | -0.80 [-1.33, -0.13] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.019). Post-hoc tests revealed:
  - Decreasing Crossover (no 1) showed smaller amplitude than Decreasing Large (no 1) (*d* = -0.75)
**P3b latency:** Significant main effect of condition (*p* = 0.037). Post-hoc tests revealed:
  - Decreasing Crossover (no 1) showed smaller latency than Decreasing Large (no 1) (*d* = -0.75)
**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - Decreasing Crossover (no 1) showed smaller amplitude than Decreasing Small (no 1) (*d* = -0.51)
  - Decreasing Large (no 1) showed smaller amplitude than Decreasing Small (no 1) (*d* = -0.80)

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
