# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:23:04

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
| Increase by 1 | 24 | 98.67 ms | 8.06 | 1.64 | [88.00, 108.00] |
| Increase by 2 | 24 | 98.67 ms | 8.14 | 1.66 | [88.00, 108.00] |
| Increase by 3 | 24 | 99.50 ms | 8.69 | 1.77 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | -1.10 µV | 1.28 | 0.26 | [-3.74, 1.19] |
| Increase by 2 | 24 | -0.95 µV | 1.15 | 0.23 | [-4.17, 0.52] |
| Increase by 3 | 24 | -1.14 µV | 1.22 | 0.25 | [-3.35, 1.12] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 167.67 ms | 20.60 | 4.20 | [136.00, 208.00] |
| Increase by 2 | 24 | 168.50 ms | 18.96 | 3.87 | [136.00, 200.00] |
| Increase by 3 | 24 | 171.33 ms | 20.62 | 4.21 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | -5.09 µV | 2.11 | 0.43 | [-9.57, -0.81] |
| Increase by 2 | 24 | -5.50 µV | 2.44 | 0.50 | [-11.28, -1.22] |
| Increase by 3 | 24 | -6.19 µV | 2.53 | 0.52 | [-12.86, -2.17] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 98.83 ms | 10.91 | 2.23 | [80.00, 108.00] |
| Increase by 2 | 24 | 97.00 ms | 11.51 | 2.35 | [80.00, 108.00] |
| Increase by 3 | 24 | 95.83 ms | 11.53 | 2.35 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 1.29 µV | 1.47 | 0.30 | [-1.33, 4.44] |
| Increase by 2 | 24 | 1.21 µV | 1.35 | 0.28 | [-1.42, 4.70] |
| Increase by 3 | 24 | 1.55 µV | 1.46 | 0.30 | [-0.71, 5.27] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 477.50 ms | 45.98 | 9.39 | [396.00, 536.00] |
| Increase by 2 | 24 | 486.83 ms | 37.07 | 7.57 | [396.00, 536.00] |
| Increase by 3 | 24 | 474.17 ms | 43.98 | 8.98 | [396.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 24 | 3.14 µV | 3.59 | 0.73 | [-3.53, 10.19] |
| Increase by 2 | 24 | 4.08 µV | 3.44 | 0.70 | [-2.36, 10.55] |
| Increase by 3 | 24 | 4.12 µV | 2.68 | 0.55 | [0.31, 10.15] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 501.92, BIC = 515.58
- **Increase by 2 vs Increase by 1**: *β* = 0.48, *SE* = 1.732, *z* = 0.278, *p* = 0.781
- **Increase by 3 vs Increase by 1**: *β* = 1.01, *SE* = 1.719, *z* = 0.589, *p* = 0.556
- **SNR**: *β* = 1.25, *SE* = 0.604, *z* = 2.068, *p* = 0.039

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.48 | 1.73 | -0.28 | 0.781 | 0.941 | n.s. |
| Increase by 1 - Increase by 3 | -1.01 | 1.72 | -0.59 | 0.556 | 0.912 | n.s. |
| Increase by 2 - Increase by 3 | -0.53 | 1.72 | -0.31 | 0.758 | 0.941 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.869, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.52 | 23 | = 0.922 | -0.10 [-0.53, 0.32] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -0.51 | 23 | = 0.922 | -0.10 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 204.32, BIC = 217.98
- **Increase by 2 vs Increase by 1**: *β* = -0.04, *SE* = 0.245, *z* = -0.148, *p* = 0.883
- **Increase by 3 vs Increase by 1**: *β* = -0.10, *SE* = 0.244, *z* = -0.422, *p* = 0.673
- **SNR**: *β* = -0.50, *SE* = 0.080, *z* = -6.207, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.04 | 0.25 | 0.15 | 0.883 | 0.965 | n.s. |
| Increase by 1 - Increase by 3 | 0.10 | 0.24 | 0.42 | 0.673 | 0.965 | n.s. |
| Increase by 2 - Increase by 3 | 0.07 | 0.24 | 0.27 | 0.785 | 0.965 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.23, *p* = 0.795, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.59 | 23 | = 0.839 | -0.13 [-0.54, 0.30] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.10 | 23 | = 0.920 | 0.03 [-0.40, 0.44] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.61 | 23 | = 0.839 | 0.16 [-0.30, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 608.11, BIC = 621.77
- **Increase by 2 vs Increase by 1**: *β* = 0.80, *SE* = 3.111, *z* = 0.256, *p* = 0.798
- **Increase by 3 vs Increase by 1**: *β* = 3.55, *SE* = 3.125, *z* = 1.137, *p* = 0.256
- **SNR**: *β* = -0.12, *SE* = 0.337, *z* = -0.365, *p* = 0.715

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.80 | 3.11 | -0.26 | 0.798 | 0.798 | n.s. |
| Increase by 1 - Increase by 3 | -3.55 | 3.12 | -1.14 | 0.256 | 0.587 | n.s. |
| Increase by 2 - Increase by 3 | -2.76 | 3.12 | -0.88 | 0.377 | 0.611 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.484, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.425 (ε = 0.614)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.24 | 23 | = 0.813 | -0.04 [-0.47, 0.37] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.93 | 23 | = 0.545 | -0.18 [-0.62, 0.24] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.85 | 23 | = 0.232 | -0.14 [-0.81, 0.06] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 284.73, BIC = 298.39
- **Increase by 2 vs Increase by 1**: *β* = -0.44, *SE* = 0.326, *z* = -1.346, *p* = 0.178
- **Increase by 3 vs Increase by 1**: *β* = -1.20, *SE* = 0.327, *z* = -3.663, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.036, *z* = -2.993, *p* = 0.003

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.44 | 0.33 | 1.35 | 0.178 | 0.178 | n.s. |
| Increase by 1 - Increase by 3 | 1.20 | 0.33 | 3.66 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.76 | 0.33 | 2.33 | 0.020 | 0.039 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.19, *p* = 0.009, η²_G = 0.037
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.29 | 23 | = 0.209 | 0.18 [-0.17, 0.69] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 2.86 | 23 | = 0.027 | 0.47 [0.13, 1.04] | small | * |
| Increase by 2 vs Increase by 3 | 2.09 | 23 | = 0.072 | 0.28 [-0.01, 0.87] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 549.79, BIC = 563.45
- **Increase by 2 vs Increase by 1**: *β* = -1.81, *SE* = 2.403, *z* = -0.753, *p* = 0.451
- **Increase by 3 vs Increase by 1**: *β* = -3.02, *SE* = 2.397, *z* = -1.259, *p* = 0.208
- **SNR**: *β* = 0.06, *SE* = 0.612, *z* = 0.095, *p* = 0.924

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 1.81 | 2.40 | 0.75 | 0.451 | 0.699 | n.s. |
| Increase by 1 - Increase by 3 | 3.02 | 2.40 | 1.26 | 0.208 | 0.503 | n.s. |
| Increase by 2 - Increase by 3 | 1.21 | 2.43 | 0.50 | 0.619 | 0.699 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.77, *p* = 0.469, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.62 | 23 | = 0.585 | 0.16 [-0.30, 0.55] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.41 | 23 | = 0.517 | 0.27 [-0.14, 0.72] | small | n.s. |
| Increase by 2 vs Increase by 3 | 0.55 | 23 | = 0.585 | 0.10 [-0.31, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 226.01, BIC = 239.67
- **Increase by 2 vs Increase by 1**: *β* = 0.02, *SE* = 0.245, *z* = 0.092, *p* = 0.926
- **Increase by 3 vs Increase by 1**: *β* = 0.17, *SE* = 0.245, *z* = 0.708, *p* = 0.479
- **SNR**: *β* = 0.26, *SE* = 0.066, *z* = 3.867, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.02 | 0.25 | -0.09 | 0.926 | 0.926 | n.s. |
| Increase by 1 - Increase by 3 | -0.17 | 0.24 | -0.71 | 0.479 | 0.858 | n.s. |
| Increase by 2 - Increase by 3 | -0.15 | 0.25 | -0.61 | 0.544 | 0.858 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.415, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.28 | 23 | = 0.780 | 0.06 [-0.36, 0.48] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.90 | 23 | = 0.568 | -0.17 [-0.61, 0.24] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.70 | 23 | = 0.308 | -0.24 [-0.78, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 749.13, BIC = 762.79
- **Increase by 2 vs Increase by 1**: *β* = 9.91, *SE* = 10.604, *z* = 0.934, *p* = 0.350
- **Increase by 3 vs Increase by 1**: *β* = -4.72, *SE* = 10.703, *z* = -0.441, *p* = 0.659
- **SNR**: *β* = -0.84, *SE* = 0.963, *z* = -0.871, *p* = 0.384

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -9.91 | 10.60 | -0.93 | 0.350 | 0.578 | n.s. |
| Increase by 1 - Increase by 3 | 4.72 | 10.70 | 0.44 | 0.659 | 0.659 | n.s. |
| Increase by 2 - Increase by 3 | 14.63 | 10.82 | 1.35 | 0.176 | 0.441 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.483, η²_G = 0.016
- Greenhouse-Geisser corrected: *p* = 0.443 (ε = 0.722)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.83 | 23 | = 0.620 | -0.22 [-0.60, 0.26] | small | n.s. |
| Increase by 1 vs Increase by 3 | 0.25 | 23 | = 0.803 | 0.07 [-0.37, 0.47] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 1.80 | 23 | = 0.257 | 0.31 [-0.07, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.37, BIC = 316.03
- **Increase by 2 vs Increase by 1**: *β* = 0.92, *SE* = 0.312, *z* = 2.950, *p* = 0.003
- **Increase by 3 vs Increase by 1**: *β* = 1.04, *SE* = 0.317, *z* = 3.278, *p* = 0.001
- **SNR**: *β* = 0.03, *SE* = 0.038, *z* = 0.809, *p* = 0.418

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.92 | 0.31 | -2.95 | 0.003 | 0.006 | ** |
| Increase by 1 - Increase by 3 | -1.04 | 0.32 | -3.28 | 0.001 | 0.003 | ** |
| Increase by 2 - Increase by 3 | -0.12 | 0.32 | -0.37 | 0.713 | 0.713 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.25, *p* = 0.004, η²_G = 0.020
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -3.23 | 23 | = 0.006 | -0.27 [-1.13, -0.19] | small | ** |
| Increase by 1 vs Increase by 3 | -3.24 | 23 | = 0.006 | -0.31 [-1.13, -0.20] | small | ** |
| Increase by 2 vs Increase by 3 | -0.14 | 23 | = 0.892 | -0.02 [-0.45, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.009). Post-hoc tests revealed:
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.47)
**P3b amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.27)
  - Increase by 1 showed smaller amplitude than Increase by 3 (*d* = -0.31)

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
