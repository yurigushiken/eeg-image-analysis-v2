# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:21:24

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
| 1 to 2 | 24 | 98.83 ms | 10.71 | 2.19 | [88.00, 112.00] |
| 1 to 3 | 24 | 99.67 ms | 10.41 | 2.13 | [88.00, 112.00] |
| 1 to 4 | 24 | 100.83 ms | 9.58 | 1.96 | [88.00, 112.00] |
| Cardinality1 | 24 | 102.17 ms | 9.65 | 1.97 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -0.33 µV | 2.42 | 0.49 | [-6.14, 5.05] |
| 1 to 3 | 24 | -0.09 µV | 2.40 | 0.49 | [-5.86, 3.53] |
| 1 to 4 | 24 | -1.41 µV | 1.88 | 0.38 | [-4.46, 2.21] |
| Cardinality1 | 24 | -1.52 µV | 2.13 | 0.44 | [-5.36, 3.66] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 170.50 ms | 18.19 | 3.71 | [144.00, 208.00] |
| 1 to 3 | 24 | 168.50 ms | 21.76 | 4.44 | [140.00, 208.00] |
| 1 to 4 | 24 | 172.50 ms | 19.92 | 4.07 | [140.00, 208.00] |
| Cardinality1 | 24 | 178.33 ms | 19.77 | 4.04 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -5.32 µV | 2.41 | 0.49 | [-9.95, -0.26] |
| 1 to 3 | 24 | -6.62 µV | 2.58 | 0.53 | [-12.65, -2.26] |
| 1 to 4 | 24 | -6.32 µV | 2.96 | 0.60 | [-12.55, -1.25] |
| Cardinality1 | 24 | -3.32 µV | 2.59 | 0.53 | [-9.64, 0.56] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 101.67 ms | 14.00 | 2.86 | [88.00, 120.00] |
| 1 to 3 | 24 | 103.50 ms | 11.33 | 2.31 | [88.00, 120.00] |
| 1 to 4 | 24 | 99.17 ms | 11.79 | 2.41 | [88.00, 120.00] |
| Cardinality1 | 24 | 112.33 ms | 10.74 | 2.19 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 1.15 µV | 1.95 | 0.40 | [-3.63, 5.23] |
| 1 to 3 | 24 | 0.98 µV | 2.52 | 0.51 | [-4.70, 7.47] |
| 1 to 4 | 24 | 1.99 µV | 2.20 | 0.45 | [-1.97, 6.92] |
| Cardinality1 | 24 | 3.57 µV | 3.08 | 0.63 | [-0.77, 13.26] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 451.17 ms | 59.36 | 12.12 | [360.00, 536.00] |
| 1 to 3 | 24 | 462.00 ms | 47.52 | 9.70 | [368.00, 536.00] |
| 1 to 4 | 24 | 460.33 ms | 58.26 | 11.89 | [356.00, 536.00] |
| Cardinality1 | 24 | 437.50 ms | 61.72 | 12.60 | [356.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 4.34 µV | 3.79 | 0.77 | [-3.36, 11.99] |
| 1 to 3 | 24 | 5.08 µV | 3.95 | 0.81 | [-1.07, 15.57] |
| 1 to 4 | 24 | 5.05 µV | 3.67 | 0.75 | [-0.70, 13.02] |
| Cardinality1 | 24 | 2.52 µV | 2.40 | 0.49 | [-2.10, 7.37] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 726.09, BIC = 744.04
- **1 to 3 vs 1 to 2**: *β* = 0.72, *SE* = 2.842, *z* = 0.255, *p* = 0.799
- **1 to 4 vs 1 to 2**: *β* = 1.99, *SE* = 2.803, *z* = 0.708, *p* = 0.479
- **Cardinality1 vs 1 to 2**: *β* = 3.32, *SE* = 2.803, *z* = 1.185, *p* = 0.236
- **SNR**: *β* = 0.16, *SE* = 0.701, *z* = 0.233, *p* = 0.816

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.72 | 2.84 | -0.25 | 0.799 | 0.951 | n.s. |
| 1 to 2 - 1 to 4 | -1.99 | 2.80 | -0.71 | 0.479 | 0.926 | n.s. |
| 1 to 2 - Cardinality1 | -3.32 | 2.80 | -1.18 | 0.236 | 0.801 | n.s. |
| 1 to 3 - 1 to 4 | -1.26 | 2.83 | -0.45 | 0.656 | 0.951 | n.s. |
| 1 to 3 - Cardinality1 | -2.60 | 2.83 | -0.92 | 0.359 | 0.892 | n.s. |
| 1 to 4 - Cardinality1 | -1.34 | 2.80 | -0.48 | 0.634 | 0.951 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.52, *p* = 0.673, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.26 | 23 | = 0.796 | -0.08 [-0.48, 0.37] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.69 | 23 | = 0.775 | -0.20 [-0.57, 0.28] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -1.08 | 23 | = 0.775 | -0.33 [-0.65, 0.21] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.47 | 23 | = 0.775 | -0.12 [-0.52, 0.33] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | -0.98 | 23 | = 0.775 | -0.25 [-0.63, 0.23] | small | n.s. |
| 1 to 4 vs Cardinality1 | -0.47 | 23 | = 0.775 | -0.14 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 434.20, BIC = 452.15
- **1 to 3 vs 1 to 2**: *β* = 0.23, *SE* = 0.604, *z* = 0.382, *p* = 0.702
- **1 to 4 vs 1 to 2**: *β* = -1.08, *SE* = 0.596, *z* = -1.815, *p* = 0.070
- **Cardinality1 vs 1 to 2**: *β* = -1.19, *SE* = 0.596, *z* = -1.997, *p* = 0.046
- **SNR**: *β* = 0.03, *SE* = 0.146, *z* = 0.180, *p* = 0.857

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.23 | 0.60 | -0.38 | 0.702 | 0.911 | n.s. |
| 1 to 2 - 1 to 4 | 1.08 | 0.60 | 1.82 | 0.070 | 0.194 | n.s. |
| 1 to 2 - Cardinality1 | 1.19 | 0.60 | 2.00 | 0.046 | 0.171 | n.s. |
| 1 to 3 - 1 to 4 | 1.31 | 0.60 | 2.18 | 0.029 | 0.138 | n.s. |
| 1 to 3 - Cardinality1 | 1.42 | 0.60 | 2.36 | 0.018 | 0.105 | n.s. |
| 1 to 4 - Cardinality1 | 0.11 | 0.60 | 0.18 | 0.856 | 0.911 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.91, *p* = 0.040, η²_G = 0.079
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.42 | 23 | = 0.817 | -0.10 [-0.51, 0.34] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 1.94 | 23 | = 0.117 | 0.50 [-0.04, 0.84] | small | n.s. |
| 1 to 2 vs Cardinality1 | 1.88 | 23 | = 0.117 | 0.52 [-0.05, 0.82] | medium | n.s. |
| 1 to 3 vs 1 to 4 | 1.84 | 23 | = 0.117 | 0.62 [-0.06, 0.81] | medium | n.s. |
| 1 to 3 vs Cardinality1 | 2.31 | 23 | = 0.117 | 0.63 [0.03, 0.92] | medium | n.s. |
| 1 to 4 vs Cardinality1 | 0.22 | 23 | = 0.831 | 0.05 [-0.38, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 839.85, BIC = 857.80
- **1 to 3 vs 1 to 2**: *β* = -2.44, *SE* = 4.505, *z* = -0.542, *p* = 0.588
- **1 to 4 vs 1 to 2**: *β* = 1.90, *SE* = 4.399, *z* = 0.432, *p* = 0.666
- **Cardinality1 vs 1 to 2**: *β* = 8.24, *SE* = 4.488, *z* = 1.836, *p* = 0.066
- **SNR**: *β* = 0.27, *SE* = 0.616, *z* = 0.442, *p* = 0.658

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 2.44 | 4.50 | 0.54 | 0.588 | 0.830 | n.s. |
| 1 to 2 - 1 to 4 | -1.90 | 4.40 | -0.43 | 0.666 | 0.830 | n.s. |
| 1 to 2 - Cardinality1 | -8.24 | 4.49 | -1.84 | 0.066 | 0.291 | n.s. |
| 1 to 3 - 1 to 4 | -4.34 | 4.46 | -0.97 | 0.330 | 0.700 | n.s. |
| 1 to 3 - Cardinality1 | -10.68 | 4.80 | -2.23 | 0.026 | 0.146 | n.s. |
| 1 to 4 - Cardinality1 | -6.34 | 4.54 | -1.40 | 0.162 | 0.508 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.78, *p* = 0.159, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.40 | 23 | = 0.694 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.42 | 23 | = 0.694 | -0.10 [-0.51, 0.34] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -1.55 | 23 | = 0.280 | -0.41 [-0.75, 0.12] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.31 | 23 | = 0.305 | -0.19 [-0.70, 0.16] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | -2.02 | 23 | = 0.280 | -0.47 [-0.85, 0.03] | small | n.s. |
| 1 to 4 vs Cardinality1 | -1.53 | 23 | = 0.280 | -0.29 [-0.74, 0.12] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 397.78, BIC = 415.73
- **1 to 3 vs 1 to 2**: *β* = -0.53, *SE* = 0.444, *z* = -1.186, *p* = 0.235
- **1 to 4 vs 1 to 2**: *β* = -0.83, *SE* = 0.433, *z* = -1.908, *p* = 0.056
- **Cardinality1 vs 1 to 2**: *β* = 1.29, *SE* = 0.442, *z* = 2.910, *p* = 0.004
- **SNR**: *β* = -0.48, *SE* = 0.062, *z* = -7.695, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.53 | 0.44 | 1.19 | 0.235 | 0.415 | n.s. |
| 1 to 2 - 1 to 4 | 0.83 | 0.43 | 1.91 | 0.056 | 0.160 | n.s. |
| 1 to 2 - Cardinality1 | -1.29 | 0.44 | -2.91 | 0.004 | 0.014 | * |
| 1 to 3 - 1 to 4 | 0.30 | 0.44 | 0.68 | 0.495 | 0.495 | n.s. |
| 1 to 3 - Cardinality1 | -1.81 | 0.47 | -3.83 | < .001 | < .001 | *** |
| 1 to 4 - Cardinality1 | -2.11 | 0.45 | -4.72 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 14.40, *p* < .001, η²_G = 0.199
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 3.15 | 23 | = 0.007 | 0.52 [0.18, 1.11] | medium | ** |
| 1 to 2 vs 1 to 4 | 1.97 | 23 | = 0.073 | 0.37 [-0.04, 0.84] | small | n.s. |
| 1 to 2 vs Cardinality1 | -3.83 | 23 | = 0.002 | -0.80 [-1.26, -0.30] | medium | ** |
| 1 to 3 vs 1 to 4 | -0.58 | 23 | = 0.565 | -0.11 [-0.54, 0.30] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | -5.71 | 23 | < .001 | -1.28 [-1.71, -0.62] | large | *** |
| 1 to 4 vs Cardinality1 | -4.02 | 23 | = 0.002 | -1.08 [-1.31, -0.33] | large | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 755.72, BIC = 773.67
- **1 to 3 vs 1 to 2**: *β* = 1.93, *SE* = 3.086, *z* = 0.625, *p* = 0.532
- **1 to 4 vs 1 to 2**: *β* = -2.50, *SE* = 3.066, *z* = -0.815, *p* = 0.415
- **Cardinality1 vs 1 to 2**: *β* = 10.68, *SE* = 3.066, *z* = 3.484, *p* < .001
- **SNR**: *β* = -0.22, *SE* = 0.805, *z* = -0.270, *p* = 0.787

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -1.93 | 3.09 | -0.63 | 0.532 | 0.658 | n.s. |
| 1 to 2 - 1 to 4 | 2.50 | 3.07 | 0.81 | 0.415 | 0.658 | n.s. |
| 1 to 2 - Cardinality1 | -10.68 | 3.07 | -3.48 | < .001 | 0.002 | ** |
| 1 to 3 - 1 to 4 | 4.43 | 3.09 | 1.44 | 0.151 | 0.389 | n.s. |
| 1 to 3 - Cardinality1 | -8.75 | 3.08 | -2.84 | 0.004 | 0.018 | * |
| 1 to 4 - Cardinality1 | -13.18 | 3.07 | -4.30 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.68, *p* < .001, η²_G = 0.151
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.63 | 23 | = 0.535 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 0.75 | 23 | = 0.535 | 0.19 [-0.27, 0.58] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | -3.02 | 23 | = 0.012 | -0.85 [-1.08, -0.16] | large | * |
| 1 to 3 vs 1 to 4 | 1.32 | 23 | = 0.302 | 0.37 [-0.16, 0.70] | small | n.s. |
| 1 to 3 vs Cardinality1 | -3.03 | 23 | = 0.012 | -0.80 [-1.08, -0.16] | large | * |
| 1 to 4 vs Cardinality1 | -4.82 | 23 | < .001 | -1.17 [-1.50, -0.47] | large | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 435.10, BIC = 453.05
- **1 to 3 vs 1 to 2**: *β* = -0.36, *SE* = 0.554, *z* = -0.643, *p* = 0.520
- **1 to 4 vs 1 to 2**: *β* = 0.84, *SE* = 0.550, *z* = 1.525, *p* = 0.127
- **Cardinality1 vs 1 to 2**: *β* = 2.39, *SE* = 0.550, *z* = 4.343, *p* < .001
- **SNR**: *β* = 0.42, *SE* = 0.152, *z* = 2.758, *p* = 0.006

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.36 | 0.55 | 0.64 | 0.520 | 0.520 | n.s. |
| 1 to 2 - 1 to 4 | -0.84 | 0.55 | -1.52 | 0.127 | 0.239 | n.s. |
| 1 to 2 - Cardinality1 | -2.39 | 0.55 | -4.34 | < .001 | < .001 | *** |
| 1 to 3 - 1 to 4 | -1.19 | 0.55 | -2.16 | 0.031 | 0.090 | n.s. |
| 1 to 3 - Cardinality1 | -2.75 | 0.55 | -4.97 | < .001 | < .001 | *** |
| 1 to 4 - Cardinality1 | -1.55 | 0.55 | -2.82 | 0.005 | 0.019 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.47, *p* < .001, η²_G = 0.152
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.29 | 23 | = 0.778 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.65 | 23 | = 0.134 | -0.40 [-0.77, 0.10] | small | n.s. |
| 1 to 2 vs Cardinality1 | -3.72 | 23 | = 0.003 | -0.94 [-1.24, -0.28] | large | ** |
| 1 to 3 vs 1 to 4 | -1.79 | 23 | = 0.130 | -0.43 [-0.80, 0.07] | small | n.s. |
| 1 to 3 vs Cardinality1 | -4.44 | 23 | = 0.001 | -0.92 [-1.41, -0.40] | large | ** |
| 1 to 4 vs Cardinality1 | -2.94 | 23 | = 0.015 | -0.59 [-1.06, -0.14] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1055.17, BIC = 1073.12
- **1 to 3 vs 1 to 2**: *β* = 12.55, *SE* = 15.403, *z* = 0.815, *p* = 0.415
- **1 to 4 vs 1 to 2**: *β* = 10.65, *SE* = 15.392, *z* = 0.692, *p* = 0.489
- **Cardinality1 vs 1 to 2**: *β* = -20.16, *SE* = 15.973, *z* = -1.262, *p* = 0.207
- **SNR**: *β* = -3.52, *SE* = 2.374, *z* = -1.481, *p* = 0.139

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -12.55 | 15.40 | -0.81 | 0.415 | 0.800 | n.s. |
| 1 to 2 - 1 to 4 | -10.65 | 15.39 | -0.69 | 0.489 | 0.800 | n.s. |
| 1 to 2 - Cardinality1 | 20.16 | 15.97 | 1.26 | 0.207 | 0.604 | n.s. |
| 1 to 3 - 1 to 4 | 1.90 | 15.36 | 0.12 | 0.902 | 0.902 | n.s. |
| 1 to 3 - Cardinality1 | 32.71 | 16.33 | 2.00 | 0.045 | 0.242 | n.s. |
| 1 to 4 - Cardinality1 | 30.81 | 16.28 | 1.89 | 0.058 | 0.260 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.03, *p* = 0.384, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.70 | 23 | = 0.673 | -0.20 [-0.57, 0.28] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.59 | 23 | = 0.673 | -0.16 [-0.54, 0.30] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | 0.73 | 23 | = 0.673 | 0.23 [-0.27, 0.57] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.13 | 23 | = 0.896 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | 1.63 | 23 | = 0.499 | 0.44 [-0.10, 0.77] | small | n.s. |
| 1 to 4 vs Cardinality1 | 1.43 | 23 | = 0.499 | 0.38 [-0.14, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 459.60, BIC = 477.55
- **1 to 3 vs 1 to 2**: *β* = 0.58, *SE* = 0.551, *z* = 1.048, *p* = 0.295
- **1 to 4 vs 1 to 2**: *β* = 0.57, *SE* = 0.550, *z* = 1.036, *p* = 0.300
- **Cardinality1 vs 1 to 2**: *β* = -1.22, *SE* = 0.580, *z* = -2.102, *p* = 0.036
- **SNR**: *β* = 0.32, *SE* = 0.102, *z* = 3.178, *p* = 0.001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.58 | 0.55 | -1.05 | 0.295 | 0.649 | n.s. |
| 1 to 2 - 1 to 4 | -0.57 | 0.55 | -1.04 | 0.300 | 0.649 | n.s. |
| 1 to 2 - Cardinality1 | 1.22 | 0.58 | 2.10 | 0.036 | 0.135 | n.s. |
| 1 to 3 - 1 to 4 | 0.01 | 0.55 | 0.01 | 0.989 | 0.989 | n.s. |
| 1 to 3 - Cardinality1 | 1.80 | 0.60 | 3.00 | 0.003 | 0.016 | * |
| 1 to 4 - Cardinality1 | 1.79 | 0.60 | 3.01 | 0.003 | 0.016 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.52, *p* < .001, η²_G = 0.084
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.31 | 23 | = 0.288 | -0.19 [-0.70, 0.16] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.21 | 23 | = 0.288 | -0.19 [-0.67, 0.18] | negligible | n.s. |
| 1 to 2 vs Cardinality1 | 2.85 | 23 | = 0.018 | 0.57 [0.13, 1.04] | medium | * |
| 1 to 3 vs 1 to 4 | 0.07 | 23 | = 0.948 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| 1 to 3 vs Cardinality1 | 3.80 | 23 | = 0.003 | 0.78 [0.29, 1.26] | medium | ** |
| 1 to 4 vs Cardinality1 | 4.48 | 23 | = 0.001 | 0.81 [0.41, 1.42] | large | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.040) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than 1 to 3 (*d* = 0.52)
  - 1 to 2 showed smaller amplitude than Cardinality1 (*d* = -0.80)
  - 1 to 3 showed smaller amplitude than Cardinality1 (*d* = -1.28)
  - 1 to 4 showed smaller amplitude than Cardinality1 (*d* = -1.08)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 2 showed smaller latency than Cardinality1 (*d* = -0.85)
  - 1 to 3 showed smaller latency than Cardinality1 (*d* = -0.80)
  - 1 to 4 showed smaller latency than Cardinality1 (*d* = -1.17)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 2 showed smaller amplitude than Cardinality1 (*d* = -0.94)
  - 1 to 3 showed smaller amplitude than Cardinality1 (*d* = -0.92)
  - 1 to 4 showed smaller amplitude than Cardinality1 (*d* = -0.59)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than Cardinality1 (*d* = 0.57)
  - 1 to 3 showed greater amplitude than Cardinality1 (*d* = 0.78)
  - 1 to 4 showed greater amplitude than Cardinality1 (*d* = 0.81)

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
