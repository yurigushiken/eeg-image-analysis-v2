# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:23:14

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
| Increase by 1 (no 1) | 24 | 99.33 ms | 8.06 | 1.64 | [88.00, 108.00] |
| Increase by 2 (no 1) | 24 | 99.50 ms | 7.49 | 1.53 | [88.00, 108.00] |
| Increase by 3 (no 1) | 24 | 99.67 ms | 8.50 | 1.73 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | -1.14 µV | 1.08 | 0.22 | [-3.26, 1.02] |
| Increase by 2 (no 1) | 24 | -1.28 µV | 1.19 | 0.24 | [-3.67, 0.34] |
| Increase by 3 (no 1) | 24 | -1.11 µV | 1.74 | 0.36 | [-6.02, 3.19] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 170.67 ms | 20.25 | 4.13 | [136.00, 208.00] |
| Increase by 2 (no 1) | 24 | 168.33 ms | 17.81 | 3.63 | [136.00, 200.00] |
| Increase by 3 (no 1) | 24 | 170.00 ms | 20.77 | 4.24 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | -5.09 µV | 2.19 | 0.45 | [-9.40, -0.93] |
| Increase by 2 (no 1) | 24 | -5.28 µV | 2.62 | 0.53 | [-10.89, -0.50] |
| Increase by 3 (no 1) | 24 | -6.13 µV | 2.41 | 0.49 | [-13.18, -2.28] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 98.67 ms | 10.33 | 2.11 | [80.00, 108.00] |
| Increase by 2 (no 1) | 24 | 97.50 ms | 11.05 | 2.26 | [80.00, 108.00] |
| Increase by 3 (no 1) | 24 | 95.50 ms | 11.52 | 2.35 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 1.21 µV | 1.32 | 0.27 | [-0.83, 4.01] |
| Increase by 2 (no 1) | 24 | 1.42 µV | 1.53 | 0.31 | [-1.61, 4.54] |
| Increase by 3 (no 1) | 24 | 1.45 µV | 2.22 | 0.45 | [-1.32, 9.07] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 478.00 ms | 41.17 | 8.40 | [408.00, 532.00] |
| Increase by 2 (no 1) | 24 | 482.67 ms | 39.17 | 8.00 | [408.00, 532.00] |
| Increase by 3 (no 1) | 24 | 466.50 ms | 41.35 | 8.44 | [408.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 2.42 µV | 3.44 | 0.70 | [-3.76, 8.98] |
| Increase by 2 (no 1) | 24 | 3.82 µV | 3.53 | 0.72 | [-3.29, 10.75] |
| Increase by 3 (no 1) | 24 | 4.01 µV | 2.36 | 0.48 | [0.84, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 496.25, BIC = 509.91
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.04, *SE* = 1.634, *z* = 0.025, *p* = 0.980
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.35, *SE* = 1.632, *z* = 0.218, *p* = 0.828
- **SNR**: *β* = 0.89, *SE* = 0.511, *z* = 1.739, *p* = 0.082

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.04 | 1.63 | -0.02 | 0.980 | 0.995 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.36 | 1.63 | -0.22 | 0.828 | 0.995 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.31 | 1.63 | -0.19 | 0.847 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.02, *p* = 0.981, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.09 | 23 | = 0.932 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.25 | 23 | = 0.932 | -0.04 [-0.47, 0.37] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.09 | 23 | = 0.932 | -0.02 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 238.36, BIC = 252.02
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.09, *SE* = 0.296, *z* = -0.317, *p* = 0.752
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.03, *SE* = 0.296, *z* = 0.085, *p* = 0.932
- **SNR**: *β* = -0.34, *SE* = 0.089, *z* = -3.774, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.09 | 0.30 | 0.32 | 0.752 | 0.970 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.03 | 0.30 | -0.09 | 0.932 | 0.970 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.12 | 0.30 | -0.40 | 0.688 | 0.970 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.850, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.54 | 23 | = 0.918 | 0.12 [-0.31, 0.53] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.10 | 23 | = 0.918 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.46 | 23 | = 0.918 | -0.12 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 596.31, BIC = 609.97
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -2.50, *SE* = 2.784, *z* = -0.896, *p* = 0.370
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -1.05, *SE* = 2.807, *z* = -0.373, *p* = 0.709
- **SNR**: *β* = -0.39, *SE* = 0.406, *z* = -0.970, *p* = 0.332

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 2.50 | 2.78 | 0.90 | 0.370 | 0.750 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.05 | 2.81 | 0.37 | 0.709 | 0.843 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -1.45 | 2.79 | -0.52 | 0.603 | 0.843 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.36, *p* = 0.699, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.78 | 23 | = 0.786 | 0.12 [-0.27, 0.58] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.27 | 23 | = 0.786 | 0.03 [-0.37, 0.48] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.55 | 23 | = 0.786 | -0.09 [-0.54, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 287.41, BIC = 301.07
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.26, *SE* = 0.340, *z* = -0.767, *p* = 0.443
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -1.19, *SE* = 0.343, *z* = -3.471, *p* = 0.001
- **SNR**: *β* = -0.15, *SE* = 0.051, *z* = -2.981, *p* = 0.003

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.26 | 0.34 | 0.77 | 0.443 | 0.443 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.19 | 0.34 | 3.47 | < .001 | 0.002 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.93 | 0.34 | 2.73 | 0.006 | 0.013 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.96, *p* = 0.011, η²_G = 0.035
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.55 | 23 | = 0.588 | 0.08 [-0.31, 0.54] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.95 | 23 | = 0.022 | 0.45 [0.14, 1.06] | small | * |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.48 | 23 | = 0.032 | 0.34 [0.06, 0.95] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 538.55, BIC = 552.21
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -1.18, *SE* = 2.133, *z* = -0.551, *p* = 0.582
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -3.36, *SE* = 2.137, *z* = -1.572, *p* = 0.116
- **SNR**: *β* = 1.36, *SE* = 0.887, *z* = 1.535, *p* = 0.125

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.18 | 2.13 | 0.55 | 0.582 | 0.582 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 3.36 | 2.14 | 1.57 | 0.116 | 0.309 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 2.18 | 2.14 | 1.02 | 0.307 | 0.519 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.361, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.52 | 23 | = 0.609 | 0.11 [-0.32, 0.53] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.38 | 23 | = 0.526 | 0.29 [-0.15, 0.71] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.95 | 23 | = 0.526 | 0.18 [-0.23, 0.62] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 260.98, BIC = 274.64
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.21, *SE* = 0.317, *z* = 0.653, *p* = 0.514
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.18, *SE* = 0.318, *z* = 0.559, *p* = 0.576
- **SNR**: *β* = 0.49, *SE* = 0.132, *z* = 3.724, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.21 | 0.32 | -0.65 | 0.514 | 0.885 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.18 | 0.32 | -0.56 | 0.576 | 0.885 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.03 | 0.32 | 0.09 | 0.926 | 0.926 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.30, *p* = 0.743, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.64 | 23 | = 0.789 | -0.15 [-0.56, 0.29] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.72 | 23 | = 0.789 | -0.14 [-0.57, 0.28] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.10 | 23 | = 0.920 | -0.02 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 740.95, BIC = 754.61
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 3.76, *SE* = 9.981, *z* = 0.377, *p* = 0.706
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -14.13, *SE* = 10.146, *z* = -1.393, *p* = 0.164
- **SNR**: *β* = -1.06, *SE* = 0.785, *z* = -1.355, *p* = 0.175

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -3.76 | 9.98 | -0.38 | 0.706 | 0.706 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 14.13 | 10.15 | 1.39 | 0.164 | 0.301 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 17.89 | 10.04 | 1.78 | 0.075 | 0.208 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.33, *p* = 0.275, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.56 | 23 | = 0.580 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.95 | 23 | = 0.528 | 0.28 [-0.23, 0.62] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.64 | 23 | = 0.345 | 0.40 [-0.10, 0.77] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 320.82, BIC = 334.48
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 1.41, *SE* = 0.386, *z* = 3.659, *p* < .001
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 1.63, *SE* = 0.395, *z* = 4.136, *p* < .001
- **SNR**: *β* = 0.02, *SE* = 0.037, *z* = 0.454, *p* = 0.650

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -1.41 | 0.39 | -3.66 | < .001 | < .001 | *** |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -1.63 | 0.40 | -4.14 | < .001 | < .001 | *** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.22 | 0.39 | -0.57 | 0.567 | 0.567 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.81, *p* < .001, η²_G = 0.050
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -4.99 | 23 | < .001 | -0.40 [-1.54, -0.50] | small | *** |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -3.97 | 23 | < .001 | -0.54 [-1.30, -0.32] | medium | *** |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.41 | 23 | = 0.682 | -0.07 [-0.51, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.011). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.45)
  - Increase by 2 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.34)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -0.40)
  - Increase by 1 (no 1) showed smaller amplitude than Increase by 3 (no 1) (*d* = -0.54)

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
