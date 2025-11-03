# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:32:16

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
| Cardinality2 | 14 | 108.86 ms | 9.44 | 2.52 | [88.00, 120.00] |
| Cardinality3 | 12 | 109.00 ms | 11.33 | 3.27 | [88.00, 120.00] |
| Decreasing 3 to 2 | 13 | 104.62 ms | 9.22 | 2.56 | [92.00, 120.00] |
| Increasing 2 to 3 | 16 | 105.50 ms | 13.38 | 3.34 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 14 | -2.40 µV | 1.34 | 0.36 | [-5.94, -0.68] |
| Cardinality3 | 12 | -3.68 µV | 1.84 | 0.53 | [-8.81, -1.48] |
| Decreasing 3 to 2 | 13 | -2.79 µV | 1.63 | 0.45 | [-5.65, -0.61] |
| Increasing 2 to 3 | 16 | -2.55 µV | 1.49 | 0.37 | [-5.76, -0.43] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 22 | 174.36 ms | 21.86 | 4.66 | [140.00, 208.00] |
| Cardinality3 | 22 | 167.82 ms | 16.54 | 3.53 | [140.00, 200.00] |
| Decreasing 3 to 2 | 24 | 175.33 ms | 22.28 | 4.55 | [140.00, 208.00] |
| Increasing 2 to 3 | 22 | 171.45 ms | 19.33 | 4.12 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 22 | -5.75 µV | 2.52 | 0.54 | [-10.78, -1.57] |
| Cardinality3 | 22 | -5.19 µV | 2.03 | 0.43 | [-10.83, -1.55] |
| Decreasing 3 to 2 | 24 | -5.77 µV | 2.55 | 0.52 | [-10.33, -1.35] |
| Increasing 2 to 3 | 22 | -5.27 µV | 1.96 | 0.42 | [-10.61, -0.91] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 13 | 111.69 ms | 8.40 | 2.33 | [100.00, 120.00] |
| Cardinality3 | 15 | 111.47 ms | 7.98 | 2.06 | [100.00, 120.00] |
| Decreasing 3 to 2 | 11 | 108.36 ms | 6.80 | 2.05 | [100.00, 120.00] |
| Increasing 2 to 3 | 14 | 111.14 ms | 8.76 | 2.34 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 13 | 3.04 µV | 1.79 | 0.50 | [1.11, 7.57] |
| Cardinality3 | 15 | 3.02 µV | 2.39 | 0.62 | [0.79, 8.96] |
| Decreasing 3 to 2 | 11 | 2.54 µV | 1.70 | 0.51 | [0.54, 5.61] |
| Increasing 2 to 3 | 14 | 2.77 µV | 1.86 | 0.50 | [0.49, 6.63] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 12 | 461.33 ms | 24.97 | 7.21 | [420.00, 496.00] |
| Cardinality3 | 16 | 467.00 ms | 31.45 | 7.86 | [420.00, 528.00] |
| Decreasing 3 to 2 | 19 | 481.68 ms | 33.02 | 7.58 | [432.00, 528.00] |
| Increasing 2 to 3 | 18 | 478.44 ms | 44.55 | 10.50 | [420.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality2 | 12 | 4.50 µV | 2.29 | 0.66 | [1.28, 10.57] |
| Cardinality3 | 16 | 4.51 µV | 2.20 | 0.55 | [1.80, 9.60] |
| Decreasing 3 to 2 | 19 | 6.30 µV | 4.09 | 0.94 | [1.68, 17.81] |
| Increasing 2 to 3 | 18 | 5.85 µV | 3.54 | 0.83 | [1.42, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 423.44, BIC = 437.49
- **Cardinality3 vs Cardinality2**: *β* = -0.42, *SE* = 3.785, *z* = -0.110, *p* = 0.913
- **Decreasing 3 to 2 vs Cardinality2**: *β* = -5.98, *SE* = 3.728, *z* = -1.603, *p* = 0.109
- **Increasing 2 to 3 vs Cardinality2**: *β* = -4.83, *SE* = 3.458, *z* = -1.397, *p* = 0.162
- **SNR**: *β* = 2.95, *SE* = 1.265, *z* = 2.332, *p* = 0.020

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 0.42 | 3.78 | 0.11 | 0.913 | 0.939 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | 5.98 | 3.73 | 1.60 | 0.109 | 0.499 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 4.83 | 3.46 | 1.40 | 0.162 | 0.525 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | 5.56 | 3.75 | 1.48 | 0.138 | 0.525 | n.s. |
| Cardinality3 - Increasing 2 to 3 | 4.41 | 3.78 | 1.17 | 0.243 | 0.566 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | -1.15 | 3.65 | -0.31 | 0.754 | 0.939 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.43, *p* = 0.733, η²_G = 0.062
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.52 | 5 | = 0.894 | -0.31 [-1.01, 0.54] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -0.34 | 5 | = 0.894 | -0.26 [-0.69, 0.74] | small | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.54 | 5 | = 0.894 | 0.32 [-0.47, 1.10] | small | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.12 | 5 | = 0.910 | 0.07 [-0.68, 1.00] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 1.03 | 5 | = 0.894 | 0.51 [-0.15, 1.58] | medium | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.86 | 5 | = 0.894 | 0.48 [-0.50, 1.06] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 202.24, BIC = 216.29
- **Cardinality3 vs Cardinality2**: *β* = -0.94, *SE* = 0.504, *z* = -1.870, *p* = 0.061
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 0.04, *SE* = 0.506, *z* = 0.087, *p* = 0.931
- **Increasing 2 to 3 vs Cardinality2**: *β* = -0.12, *SE* = 0.476, *z* = -0.255, *p* = 0.799
- **SNR**: *β* = -0.61, *SE* = 0.169, *z* = -3.625, *p* < .001

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 0.94 | 0.50 | 1.87 | 0.061 | 0.277 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -0.04 | 0.51 | -0.09 | 0.931 | 0.981 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 0.12 | 0.48 | 0.25 | 0.799 | 0.981 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -0.99 | 0.51 | -1.94 | 0.053 | 0.277 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -0.82 | 0.49 | -1.68 | 0.094 | 0.325 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 0.17 | 0.49 | 0.34 | 0.734 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.881, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.56 | 5 | = 0.943 | 0.27 [-0.25, 1.41] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.55 | 5 | = 0.943 | 0.35 [-0.36, 1.12] | small | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.47 | 5 | = 0.943 | 0.35 [-0.61, 0.94] | small | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.44 | 5 | = 0.943 | 0.16 [-1.05, 0.64] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.27 | 5 | = 0.943 | 0.15 [-0.87, 0.67] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -0.08 | 5 | = 0.943 | -0.02 [-0.94, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 792.25, BIC = 809.75
- **Cardinality3 vs Cardinality2**: *β* = -5.47, *SE* = 4.752, *z* = -1.152, *p* = 0.249
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 1.17, *SE* = 4.772, *z* = 0.244, *p* = 0.807
- **Increasing 2 to 3 vs Cardinality2**: *β* = -1.69, *SE* = 4.776, *z* = -0.353, *p* = 0.724
- **SNR**: *β* = -0.41, *SE* = 0.792, *z* = -0.524, *p* = 0.600

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 5.47 | 4.75 | 1.15 | 0.249 | 0.762 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -1.17 | 4.77 | -0.24 | 0.807 | 0.924 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 1.69 | 4.78 | 0.35 | 0.724 | 0.924 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -6.64 | 4.73 | -1.40 | 0.160 | 0.649 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -3.79 | 4.69 | -0.81 | 0.419 | 0.886 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 2.85 | 4.67 | 0.61 | 0.542 | 0.904 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.577, η²_G = 0.018
- Greenhouse-Geisser corrected: *p* = 0.535 (ε = 0.744)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 1.36 | 19 | = 0.565 | 0.31 [-0.17, 0.78] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -0.09 | 19 | = 0.928 | -0.03 [-0.50, 0.39] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.57 | 19 | = 0.694 | 0.13 [-0.34, 0.60] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.52 | 19 | = 0.565 | -0.35 [-0.69, 0.21] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.65 | 19 | = 0.694 | -0.19 [-0.62, 0.27] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 0.59 | 19 | = 0.694 | 0.16 [-0.41, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 339.49, BIC = 356.99
- **Cardinality3 vs Cardinality2**: *β* = 0.56, *SE* = 0.363, *z* = 1.535, *p* = 0.125
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 0.58, *SE* = 0.366, *z* = 1.581, *p* = 0.114
- **Increasing 2 to 3 vs Cardinality2**: *β* = 0.66, *SE* = 0.366, *z* = 1.799, *p* = 0.072
- **SNR**: *β* = -0.47, *SE* = 0.063, *z* = -7.414, *p* < .001

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | -0.56 | 0.36 | -1.54 | 0.125 | 0.454 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -0.58 | 0.37 | -1.58 | 0.114 | 0.454 | n.s. |
| Cardinality2 - Increasing 2 to 3 | -0.66 | 0.37 | -1.80 | 0.072 | 0.361 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -0.02 | 0.36 | -0.06 | 0.956 | 0.989 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -0.10 | 0.36 | -0.28 | 0.779 | 0.989 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | -0.08 | 0.36 | -0.22 | 0.822 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.445, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.78 | 19 | = 0.621 | -0.16 [-0.65, 0.30] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.79 | 19 | = 0.621 | 0.15 [-0.36, 0.53] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.18 | 19 | = 0.856 | -0.04 [-0.51, 0.43] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 1.67 | 19 | = 0.621 | 0.31 [-0.14, 0.77] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.66 | 19 | = 0.621 | 0.14 [-0.41, 0.48] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -0.97 | 19 | = 0.621 | -0.21 [-0.70, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 379.91, BIC = 393.71
- **Cardinality3 vs Cardinality2**: *β* = -0.41, *SE* = 2.921, *z* = -0.142, *p* = 0.887
- **Decreasing 3 to 2 vs Cardinality2**: *β* = -3.35, *SE* = 3.127, *z* = -1.071, *p* = 0.284
- **Increasing 2 to 3 vs Cardinality2**: *β* = -0.59, *SE* = 3.002, *z* = -0.197, *p* = 0.844
- **SNR**: *β* = 1.04, *SE* = 0.768, *z* = 1.353, *p* = 0.176

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 0.41 | 2.92 | 0.14 | 0.887 | 0.996 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | 3.35 | 3.13 | 1.07 | 0.284 | 0.866 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 0.59 | 3.00 | 0.20 | 0.844 | 0.996 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | 2.93 | 3.05 | 0.96 | 0.336 | 0.871 | n.s. |
| Cardinality3 - Increasing 2 to 3 | 0.18 | 2.85 | 0.06 | 0.951 | 0.996 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | -2.76 | 3.13 | -0.88 | 0.378 | 0.871 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.987, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | 0.00 | 5 | = 1.000 | 0.00 [-0.56, 0.88] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.00 | 5 | = 1.000 | 0.00 [-0.88, 0.97] | negligible | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.29 | 5 | = 1.000 | -0.18 [-0.68, 0.86] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.00 | 5 | = 1.000 | 0.00 [-0.34, 1.28] | negligible | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.32 | 5 | = 1.000 | -0.16 [-0.72, 0.81] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -0.34 | 5 | = 1.000 | -0.17 [-0.99, 0.86] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 204.71, BIC = 218.51
- **Cardinality3 vs Cardinality2**: *β* = -0.02, *SE* = 0.508, *z* = -0.032, *p* = 0.974
- **Decreasing 3 to 2 vs Cardinality2**: *β* = -0.47, *SE* = 0.552, *z* = -0.851, *p* = 0.395
- **Increasing 2 to 3 vs Cardinality2**: *β* = -0.28, *SE* = 0.515, *z* = -0.553, *p* = 0.580
- **SNR**: *β* = 0.81, *SE* = 0.144, *z* = 5.605, *p* < .001

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | 0.02 | 0.51 | 0.03 | 0.974 | 0.974 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | 0.47 | 0.55 | 0.85 | 0.395 | 0.950 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 0.28 | 0.51 | 0.55 | 0.580 | 0.969 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | 0.45 | 0.53 | 0.86 | 0.392 | 0.950 | n.s. |
| Cardinality3 - Increasing 2 to 3 | 0.27 | 0.50 | 0.53 | 0.593 | 0.969 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | -0.19 | 0.54 | -0.34 | 0.734 | 0.969 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.884, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.24 | 5 | = 0.822 | -0.13 [-0.96, 0.49] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | 0.40 | 5 | = 0.822 | 0.26 [-0.92, 0.93] | small | n.s. |
| Cardinality2 vs Increasing 2 to 3 | 0.28 | 5 | = 0.822 | 0.17 [-0.56, 1.00] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | 0.81 | 5 | = 0.822 | 0.33 [-0.58, 0.97] | small | n.s. |
| Cardinality3 vs Increasing 2 to 3 | 0.59 | 5 | = 0.822 | 0.27 [-0.53, 1.03] | small | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | -0.29 | 5 | = 0.822 | -0.11 [-1.34, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 650.93, BIC = 666.15
- **Cardinality3 vs Cardinality2**: *β* = 3.53, *SE* = 11.021, *z* = 0.320, *p* = 0.749
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 19.45, *SE* = 10.842, *z* = 1.794, *p* = 0.073
- **Increasing 2 to 3 vs Cardinality2**: *β* = 19.45, *SE* = 11.581, *z* = 1.679, *p* = 0.093
- **SNR**: *β* = -1.70, *SE* = 1.528, *z* = -1.110, *p* = 0.267

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | -3.53 | 11.02 | -0.32 | 0.749 | 0.937 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -19.45 | 10.84 | -1.79 | 0.073 | 0.365 | n.s. |
| Cardinality2 - Increasing 2 to 3 | -19.45 | 11.58 | -1.68 | 0.093 | 0.386 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -15.91 | 9.73 | -1.64 | 0.102 | 0.386 | n.s. |
| Cardinality3 - Increasing 2 to 3 | -15.92 | 10.39 | -1.53 | 0.126 | 0.386 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | -0.00 | 9.59 | -0.00 | 1.000 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.381, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -0.16 | 8 | = 0.879 | -0.07 [-0.75, 0.60] | negligible | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -1.79 | 8 | = 0.482 | -0.80 [-1.21, 0.15] | large | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -0.42 | 8 | = 0.879 | -0.15 [-0.84, 0.60] | negligible | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.55 | 8 | = 0.482 | -0.63 [-1.04, 0.13] | medium | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -0.18 | 8 | = 0.879 | -0.08 [-0.95, 0.29] | negligible | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 1.20 | 8 | = 0.530 | 0.45 [-0.57, 0.49] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 294.22, BIC = 309.45
- **Cardinality3 vs Cardinality2**: *β* = 0.16, *SE* = 0.681, *z* = 0.235, *p* = 0.815
- **Decreasing 3 to 2 vs Cardinality2**: *β* = 1.27, *SE* = 0.673, *z* = 1.896, *p* = 0.058
- **Increasing 2 to 3 vs Cardinality2**: *β* = -0.09, *SE* = 0.727, *z* = -0.121, *p* = 0.904
- **SNR**: *β* = 0.73, *SE* = 0.097, *z* = 7.488, *p* < .001

_Reference condition: **Cardinality2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality2 - Cardinality3 | -0.16 | 0.68 | -0.23 | 0.815 | 0.972 | n.s. |
| Cardinality2 - Decreasing 3 to 2 | -1.28 | 0.67 | -1.90 | 0.058 | 0.258 | n.s. |
| Cardinality2 - Increasing 2 to 3 | 0.09 | 0.73 | 0.12 | 0.904 | 0.972 | n.s. |
| Cardinality3 - Decreasing 3 to 2 | -1.12 | 0.60 | -1.86 | 0.062 | 0.258 | n.s. |
| Cardinality3 - Increasing 2 to 3 | 0.25 | 0.64 | 0.39 | 0.698 | 0.972 | n.s. |
| Decreasing 3 to 2 - Increasing 2 to 3 | 1.36 | 0.59 | 2.32 | 0.020 | 0.116 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.70, *p* = 0.025, η²_G = 0.172
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality2 vs Cardinality3 | -1.46 | 8 | = 0.256 | -0.41 [-0.99, 0.38] | small | n.s. |
| Cardinality2 vs Decreasing 3 to 2 | -2.53 | 8 | = 0.109 | -0.95 [-1.32, 0.07] | large | n.s. |
| Cardinality2 vs Increasing 2 to 3 | -2.51 | 8 | = 0.109 | -0.97 [-1.80, -0.08] | large | n.s. |
| Cardinality3 vs Decreasing 3 to 2 | -1.59 | 8 | = 0.256 | -0.70 [-0.95, 0.20] | medium | n.s. |
| Cardinality3 vs Increasing 2 to 3 | -1.35 | 8 | = 0.256 | -0.64 [-0.84, 0.38] | medium | n.s. |
| Decreasing 3 to 2 vs Increasing 2 to 3 | 1.11 | 8 | = 0.300 | 0.22 [-0.18, 0.92] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.025) (no significant pairwise comparisons)

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
