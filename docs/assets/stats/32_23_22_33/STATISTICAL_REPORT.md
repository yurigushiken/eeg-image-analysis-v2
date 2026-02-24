# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:13:33

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
| Cardinality2 | 24 | 108.17 ms | 11.47 | 2.34 | [88.00, 120.00] |
| Cardinality3 | 24 | 106.50 ms | 12.91 | 2.64 | [88.00, 120.00] |
| Decreasing 3 to 2 | 24 | 104.67 ms | 11.89 | 2.43 | [88.00, 120.00] |
| Increasing 2 to 3 | 24 | 102.17 ms | 12.54 | 2.56 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 24 | -1.24 µV | 2.02 | 0.41 | [-5.94, 3.09] |
| Cardinality3 | 24 | -1.52 µV | 2.60 | 0.53 | [-8.81, 1.87] |
| Decreasing 3 to 2 | 24 | -1.29 µV | 2.17 | 0.44 | [-5.65, 2.81] |
| Increasing 2 to 3 | 24 | -1.49 µV | 2.05 | 0.42 | [-5.76, 2.45] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 24 | 174.33 ms | 20.97 | 4.28 | [140.00, 208.00] |
| Cardinality3 | 24 | 171.17 ms | 19.45 | 3.97 | [140.00, 208.00] |
| Decreasing 3 to 2 | 24 | 175.33 ms | 22.28 | 4.55 | [140.00, 208.00] |
| Increasing 2 to 3 | 24 | 171.67 ms | 21.03 | 4.29 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 24 | -5.35 µV | 2.76 | 0.56 | [-10.78, -0.87] |
| Cardinality3 | 24 | -5.16 µV | 1.95 | 0.40 | [-10.83, -1.55] |
| Decreasing 3 to 2 | 24 | -5.77 µV | 2.55 | 0.52 | [-10.33, -1.35] |
| Increasing 2 to 3 | 24 | -4.95 µV | 2.20 | 0.45 | [-10.61, -0.11] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 24 | 111.33 ms | 8.48 | 1.73 | [100.00, 120.00] |
| Cardinality3 | 24 | 111.33 ms | 8.14 | 1.66 | [100.00, 120.00] |
| Decreasing 3 to 2 | 24 | 110.17 ms | 8.50 | 1.74 | [100.00, 120.00] |
| Increasing 2 to 3 | 24 | 110.00 ms | 8.91 | 1.82 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 24 | 0.99 µV | 2.98 | 0.61 | [-7.62, 7.57] |
| Cardinality3 | 24 | 1.45 µV | 2.97 | 0.61 | [-3.67, 8.96] |
| Decreasing 3 to 2 | 24 | 0.65 µV | 2.28 | 0.46 | [-2.89, 5.61] |
| Increasing 2 to 3 | 24 | 1.41 µV | 2.41 | 0.49 | [-5.00, 6.63] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 24 | 462.33 ms | 27.20 | 5.55 | [420.00, 520.00] |
| Cardinality3 | 24 | 469.83 ms | 31.98 | 6.53 | [420.00, 528.00] |
| Decreasing 3 to 2 | 24 | 480.50 ms | 30.68 | 6.26 | [432.00, 528.00] |
| Increasing 2 to 3 | 24 | 473.00 ms | 43.71 | 8.92 | [420.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 24 | 2.04 µV | 3.44 | 0.70 | [-5.35, 10.57] |
| Cardinality3 | 24 | 2.85 µV | 3.37 | 0.69 | [-6.17, 9.60] |
| Decreasing 3 to 2 | 24 | 4.99 µV | 4.58 | 0.94 | [-2.80, 17.81] |
| Increasing 2 to 3 | 24 | 4.29 µV | 4.27 | 0.87 | [-3.54, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 761.50, BIC = 779.45
- **Cardinality3 vs Cardinality2**: *β* = -2.10, *SE* = 3.409, *z* = -0.617, *p* = 0.537
- **Decreasing 3 to 2 vs Cardinality2**: *β* = -4.28, *SE* = 3.457, *z* = -1.239, *p* = 0.215
- **Increasing 2 to 3 vs Cardinality2**: *β* = -6.48, *SE* = 3.414, *z* = -1.899, *p* = 0.058
- **SNR**: *β* = 1.18, *SE* = 1.042, *z* = 1.131, *p* = 0.258

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 2.10 | 3.41 | 0.62 | 0.537 | 0.888 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | 4.28 | 3.46 | 1.24 | 0.215 | 0.664 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 6.48 | 3.41 | 1.90 | 0.058 | 0.300 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | 2.18 | 3.40 | 0.64 | 0.522 | 0.888 | n.s. |
| Cardinality3 - Increasing 2 to 3 | 4.38 | 3.39 | 1.29 | 0.196 | 0.664 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 2.20 | 3.40 | 0.65 | 0.518 | 0.888 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.09, *p* = 0.359, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.49 | 23 | = 0.632 | 0.14 [-0.32, 0.52] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.98 | 23 | = 0.610 | 0.30 [-0.23, 0.63] | small | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 1.70 | 23 | = 0.610 | 0.50 [-0.09, 0.78] | small | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.49 | 23 | = 0.632 | 0.15 [-0.32, 0.52] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 1.20 | 23 | = 0.610 | 0.34 [-0.18, 0.67] | small | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.85 | 23 | = 0.610 | 0.20 [-0.25, 0.60] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 422.37, BIC = 440.32
- **Cardinality3 vs Cardinality2**: *β* = -0.33, *SE* = 0.513, *z* = -0.646, *p* = 0.518
- **Decreasing 3 to 2 vs Cardinality2**: *β* = -0.13, *SE* = 0.522, *z* = -0.250, *p* = 0.802
- **Increasing 2 to 3 vs Cardinality2**: *β* = -0.30, *SE* = 0.513, *z* = -0.595, *p* = 0.552
- **SNR**: *β* = 0.12, *SE* = 0.178, *z* = 0.652, *p* = 0.514

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 0.33 | 0.51 | 0.65 | 0.518 | 0.987 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | 0.13 | 0.52 | 0.25 | 0.802 | 0.991 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 0.31 | 0.51 | 0.59 | 0.552 | 0.987 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -0.20 | 0.51 | -0.39 | 0.695 | 0.991 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -0.03 | 0.51 | -0.05 | 0.960 | 0.991 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 0.17 | 0.51 | 0.34 | 0.732 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.927, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.59 | 23 | = 0.962 | 0.12 [-0.30, 0.54] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.11 | 23 | = 0.962 | 0.03 [-0.40, 0.44] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.52 | 23 | = 0.962 | 0.13 [-0.32, 0.53] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -0.48 | 23 | = 0.962 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.05 | 23 | = 0.962 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.39 | 23 | = 0.962 | 0.10 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 850.09, BIC = 868.04
- **Cardinality3 vs Cardinality2**: *β* = -3.06, *SE* = 4.680, *z* = -0.653, *p* = 0.514
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 1.65, *SE* = 4.852, *z* = 0.340, *p* = 0.734
- **Increasing 2 to 3 vs Cardinality2**: *β* = -2.41, *SE* = 4.702, *z* = -0.513, *p* = 0.608
- **SNR**: *β* = -0.41, *SE* = 0.817, *z* = -0.500, *p* = 0.617

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 3.06 | 4.68 | 0.65 | 0.514 | 0.944 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -1.65 | 4.85 | -0.34 | 0.734 | 0.944 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 2.41 | 4.70 | 0.51 | 0.608 | 0.944 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -4.71 | 4.80 | -0.98 | 0.327 | 0.907 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -0.64 | 4.68 | -0.14 | 0.891 | 0.944 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 4.06 | 4.74 | 0.86 | 0.391 | 0.916 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.36, *p* = 0.781, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.82 | 23 | = 0.823 | 0.16 [-0.26, 0.59] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -0.18 | 23 | = 0.922 | -0.05 [-0.46, 0.39] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.61 | 23 | = 0.823 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.12 | 23 | = 0.823 | -0.20 [-0.66, 0.20] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.10 | 23 | = 0.922 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.66 | 23 | = 0.823 | 0.17 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 375.09, BIC = 393.04
- **Cardinality3 vs Cardinality2**: *β* = 0.32, *SE* = 0.381, *z* = 0.841, *p* = 0.401
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 0.37, *SE* = 0.396, *z* = 0.941, *p* = 0.347
- **Increasing 2 to 3 vs Cardinality2**: *β* = 0.71, *SE* = 0.383, *z* = 1.843, *p* = 0.065
- **SNR**: *β* = -0.50, *SE* = 0.069, *z* = -7.224, *p* < .001

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | -0.32 | 0.38 | -0.84 | 0.401 | 0.846 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -0.37 | 0.40 | -0.94 | 0.347 | 0.846 | n.s. |
| Cardinality2 - Increasing 2 to 3 | -0.71 | 0.38 | -1.84 | 0.065 | 0.334 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -0.05 | 0.39 | -0.13 | 0.894 | 0.894 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -0.39 | 0.38 | -1.01 | 0.312 | 0.846 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | -0.33 | 0.39 | -0.86 | 0.389 | 0.846 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.09, *p* = 0.359, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.38 | 23 | = 0.704 | -0.08 [-0.50, 0.34] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.82 | 23 | = 0.660 | 0.16 [-0.26, 0.59] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.79 | 23 | = 0.660 | -0.16 [-0.59, 0.26] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 1.56 | 23 | = 0.397 | 0.27 [-0.11, 0.75] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.48 | 23 | = 0.704 | -0.10 [-0.52, 0.32] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -1.70 | 23 | = 0.397 | -0.34 [-0.78, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 688.89, BIC = 706.84
- **Cardinality3 vs Cardinality2**: *β* = -0.02, *SE* = 2.163, *z* = -0.009, *p* = 0.993
- **Decreasing 3 to 2 vs Cardinality2**: *β* = -1.21, *SE* = 2.169, *z* = -0.556, *p* = 0.578
- **Increasing 2 to 3 vs Cardinality2**: *β* = -1.36, *SE* = 2.165, *z* = -0.629, *p* = 0.529
- **SNR**: *β* = -0.10, *SE* = 0.503, *z* = -0.204, *p* = 0.838

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 0.02 | 2.16 | 0.01 | 0.993 | 0.997 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | 1.21 | 2.17 | 0.56 | 0.578 | 0.989 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 1.36 | 2.17 | 0.63 | 0.529 | 0.989 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | 1.19 | 2.16 | 0.55 | 0.583 | 0.989 | n.s. |
| Cardinality3 - Increasing 2 to 3 | 1.34 | 2.16 | 0.62 | 0.535 | 0.989 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 0.16 | 2.16 | 0.07 | 0.942 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.885, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.67 | 23 | = 0.901 | 0.14 [-0.29, 0.56] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.53 | 23 | = 0.901 | 0.15 [-0.32, 0.53] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.59 | 23 | = 0.901 | 0.14 [-0.30, 0.54] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.54 | 23 | = 0.901 | 0.16 [-0.31, 0.53] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.07 | 23 | = 1.000 | 0.02 [-0.41, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 449.89, BIC = 467.84
- **Cardinality3 vs Cardinality2**: *β* = 0.41, *SE* = 0.571, *z* = 0.722, *p* = 0.470
- **Decreasing 3 to 2 vs Cardinality2**: *β* = -0.42, *SE* = 0.573, *z* = -0.740, *p* = 0.459
- **Increasing 2 to 3 vs Cardinality2**: *β* = 0.35, *SE* = 0.572, *z* = 0.618, *p* = 0.537
- **SNR**: *β* = -0.23, *SE* = 0.139, *z* = -1.618, *p* = 0.106

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | -0.41 | 0.57 | -0.72 | 0.470 | 0.914 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | 0.42 | 0.57 | 0.74 | 0.459 | 0.914 | n.s. |
| Cardinality2 - Increasing 2 to 3 | -0.35 | 0.57 | -0.62 | 0.537 | 0.914 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | 0.84 | 0.57 | 1.47 | 0.143 | 0.604 | n.s. |
| Cardinality3 - Increasing 2 to 3 | 0.06 | 0.57 | 0.10 | 0.917 | 0.917 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | -0.78 | 0.57 | -1.36 | 0.173 | 0.613 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.81, *p* = 0.495, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.68 | 23 | = 0.715 | -0.15 [-0.56, 0.29] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.54 | 23 | = 0.715 | 0.13 [-0.31, 0.53] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.76 | 23 | = 0.715 | -0.15 [-0.58, 0.27] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 1.54 | 23 | = 0.530 | 0.30 [-0.12, 0.75] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.06 | 23 | = 0.950 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -1.39 | 23 | = 0.530 | -0.32 [-0.72, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 957.15, BIC = 975.10
- **Cardinality3 vs Cardinality2**: *β* = 7.90, *SE* = 9.023, *z* = 0.875, *p* = 0.381
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 18.95, *SE* = 9.051, *z* = 2.094, *p* = 0.036
- **Increasing 2 to 3 vs Cardinality2**: *β* = 12.95, *SE* = 9.324, *z* = 1.389, *p* = 0.165
- **SNR**: *β* = -1.22, *SE* = 1.275, *z* = -0.958, *p* = 0.338

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | -7.90 | 9.02 | -0.88 | 0.381 | 0.763 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -18.95 | 9.05 | -2.09 | 0.036 | 0.199 | n.s. |
| Cardinality2 - Increasing 2 to 3 | -12.95 | 9.32 | -1.39 | 0.165 | 0.594 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -11.05 | 9.02 | -1.23 | 0.221 | 0.631 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -5.06 | 9.23 | -0.55 | 0.584 | 0.763 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 6.00 | 9.15 | 0.66 | 0.512 | 0.763 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.30, *p* = 0.281, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.83 | 23 | = 0.509 | -0.25 [-0.59, 0.26] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -2.39 | 23 | = 0.153 | -0.63 [-0.93, -0.04] | medium | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -1.07 | 23 | = 0.509 | -0.29 [-0.64, 0.21] | small | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.35 | 23 | = 0.509 | -0.34 [-0.71, 0.15] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.27 | 23 | = 0.787 | -0.08 [-0.48, 0.37] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.81 | 23 | = 0.509 | 0.20 [-0.26, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 501.14, BIC = 519.09
- **Cardinality3 vs Cardinality2**: *β* = 0.71, *SE* = 0.694, *z* = 1.025, *p* = 0.305
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 2.75, *SE* = 0.697, *z* = 3.951, *p* < .001
- **Increasing 2 to 3 vs Cardinality2**: *β* = 1.69, *SE* = 0.722, *z* = 2.334, *p* = 0.020
- **SNR**: *β* = 0.31, *SE* = 0.108, *z* = 2.825, *p* = 0.005

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | -0.71 | 0.69 | -1.02 | 0.305 | 0.343 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -2.75 | 0.70 | -3.95 | < .001 | < .001 | *** |
| Cardinality2 - Increasing 2 to 3 | -1.69 | 0.72 | -2.33 | 0.020 | 0.076 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -2.04 | 0.69 | -2.94 | 0.003 | 0.016 | * |
| Cardinality3 - Increasing 2 to 3 | -0.97 | 0.71 | -1.37 | 0.172 | 0.343 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 1.07 | 0.71 | 1.51 | 0.131 | 0.343 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.49, *p* < .001, η²_G = 0.083
- Greenhouse-Geisser corrected: *p* = 0.003 (ε = 0.688)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -1.47 | 23 | = 0.185 | -0.24 [-0.73, 0.13] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -3.56 | 23 | = 0.010 | -0.73 [-1.20, -0.25] | medium | * |
| Cardinality2 vs Increasing 2 to 3 | -3.07 | 23 | = 0.016 | -0.58 [-1.09, -0.17] | medium | * |
| Cardinality3 vs Decreasing 3 to 2 | -2.44 | 23 | = 0.045 | -0.53 [-0.95, -0.05] | medium | * |
| Cardinality3 vs Increasing 2 to 3 | -1.69 | 23 | = 0.156 | -0.38 [-0.78, 0.09] | small | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 1.27 | 23 | = 0.218 | 0.16 [-0.17, 0.69] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality2 showed smaller amplitude than Decreasing 3 to 2 (*d* = -0.73)
  - Cardinality2 showed smaller amplitude than Increasing 2 to 3 (*d* = -0.58)
  - Cardinality3 showed smaller amplitude than Decreasing 3 to 2 (*d* = -0.53)

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
