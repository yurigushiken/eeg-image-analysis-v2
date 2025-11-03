# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:42:14

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
| Increase by 1 | 17 | 98.35 ms | 7.08 | 1.72 | [88.00, 108.00] |
| Increase by 2 | 14 | 100.29 ms | 6.37 | 1.70 | [88.00, 108.00] |
| Increase by 3 | 14 | 99.14 ms | 7.71 | 2.06 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 17 | -1.66 µV | 1.01 | 0.24 | [-3.74, -0.54] |
| Increase by 2 | 14 | -1.50 µV | 1.17 | 0.31 | [-4.17, -0.22] |
| Increase by 3 | 14 | -1.83 µV | 0.98 | 0.26 | [-3.35, -0.70] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 23 | 165.91 ms | 19.14 | 3.99 | [136.00, 204.00] |
| Increase by 2 | 24 | 168.50 ms | 18.96 | 3.87 | [136.00, 200.00] |
| Increase by 3 | 23 | 169.74 ms | 19.52 | 4.07 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 23 | -5.12 µV | 2.16 | 0.45 | [-9.57, -0.81] |
| Increase by 2 | 24 | -5.50 µV | 2.44 | 0.50 | [-11.28, -1.22] |
| Increase by 3 | 23 | -6.31 µV | 2.52 | 0.52 | [-12.86, -2.17] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 14 | 98.29 ms | 9.11 | 2.43 | [84.00, 108.00] |
| Increase by 2 | 15 | 99.20 ms | 10.60 | 2.74 | [80.00, 108.00] |
| Increase by 3 | 13 | 97.85 ms | 9.75 | 2.70 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 14 | 2.06 µV | 1.34 | 0.36 | [0.56, 4.44] |
| Increase by 2 | 15 | 1.71 µV | 1.30 | 0.34 | [0.31, 4.70] |
| Increase by 3 | 13 | 2.36 µV | 1.37 | 0.38 | [0.70, 5.27] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 17 | 488.71 ms | 43.59 | 10.57 | [396.00, 536.00] |
| Increase by 2 | 18 | 486.00 ms | 36.31 | 8.56 | [396.00, 536.00] |
| Increase by 3 | 19 | 473.05 ms | 43.59 | 10.00 | [400.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 17 | 4.81 µV | 2.66 | 0.64 | [1.47, 10.19] |
| Increase by 2 | 18 | 5.53 µV | 2.60 | 0.61 | [1.31, 10.55] |
| Increase by 3 | 19 | 4.88 µV | 2.48 | 0.57 | [1.25, 10.15] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.00, BIC = 312.84
- **Increase by 2 vs Increase by 1**: *β* = 0.75, *SE* = 1.730, *z* = 0.436, *p* = 0.663
- **Increase by 3 vs Increase by 1**: *β* = 0.24, *SE* = 1.732, *z* = 0.139, *p* = 0.889
- **SNR**: *β* = 1.75, *SE* = 0.594, *z* = 2.948, *p* = 0.003

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.75 | 1.73 | -0.44 | 0.663 | 0.962 | n.s. |
| Increase by 1 - Increase by 3 | -0.24 | 1.73 | -0.14 | 0.889 | 0.962 | n.s. |
| Increase by 2 - Increase by 3 | 0.51 | 1.84 | 0.28 | 0.780 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.33, *p* = 0.300, η²_G = 0.072
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.00 | 6 | = 0.534 | 0.38 [-0.93, 0.43] | small | n.s. |
| Increase by 1 vs Increase by 3 | -0.51 | 6 | = 0.631 | -0.23 [-0.52, 0.83] | small | n.s. |
| Increase by 2 vs Increase by 3 | -1.87 | 6 | = 0.334 | -0.62 [-1.63, 0.12] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 94.54, BIC = 105.38
- **Increase by 2 vs Increase by 1**: *β* = 0.01, *SE* = 0.183, *z* = 0.039, *p* = 0.969
- **Increase by 3 vs Increase by 1**: *β* = -0.21, *SE* = 0.186, *z* = -1.107, *p* = 0.268
- **SNR**: *β* = -0.46, *SE* = 0.059, *z* = -7.773, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.01 | 0.18 | -0.04 | 0.969 | 0.969 | n.s. |
| Increase by 1 - Increase by 3 | 0.21 | 0.19 | 1.11 | 0.268 | 0.608 | n.s. |
| Increase by 2 - Increase by 3 | 0.21 | 0.19 | 1.11 | 0.268 | 0.608 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.74, *p* = 0.216, η²_G = 0.057
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.10 | 6 | = 0.925 | 0.03 [-0.51, 0.84] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.42 | 6 | = 0.310 | 0.56 [-0.33, 1.06] | medium | n.s. |
| Increase by 2 vs Increase by 3 | 1.83 | 6 | = 0.310 | 0.45 [-0.15, 1.57] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 591.86, BIC = 605.35
- **Increase by 2 vs Increase by 1**: *β* = 1.63, *SE* = 3.239, *z* = 0.505, *p* = 0.614
- **Increase by 3 vs Increase by 1**: *β* = 3.72, *SE* = 3.262, *z* = 1.140, *p* = 0.254
- **SNR**: *β* = -0.11, *SE* = 0.340, *z* = -0.322, *p* = 0.747

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -1.63 | 3.24 | -0.50 | 0.614 | 0.770 | n.s. |
| Increase by 1 - Increase by 3 | -3.72 | 3.26 | -1.14 | 0.254 | 0.585 | n.s. |
| Increase by 2 - Increase by 3 | -2.09 | 3.24 | -0.64 | 0.520 | 0.770 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.500, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.437 (ε = 0.611)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.34 | 22 | = 0.739 | -0.07 [-0.50, 0.36] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -0.93 | 22 | = 0.546 | -0.20 [-0.63, 0.24] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.65 | 22 | = 0.341 | -0.14 [-0.79, 0.10] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 277.50, BIC = 290.99
- **Increase by 2 vs Increase by 1**: *β* = -0.46, *SE* = 0.331, *z* = -1.376, *p* = 0.169
- **Increase by 3 vs Increase by 1**: *β* = -1.29, *SE* = 0.334, *z* = -3.871, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.036, *z* = -3.001, *p* = 0.003

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.46 | 0.33 | 1.38 | 0.169 | 0.169 | n.s. |
| Increase by 1 - Increase by 3 | 1.29 | 0.33 | 3.87 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.84 | 0.33 | 2.52 | 0.012 | 0.023 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.77, *p* = 0.006, η²_G = 0.042
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.30 | 22 | = 0.208 | 0.18 [-0.17, 0.71] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 3.03 | 22 | = 0.018 | 0.51 [0.16, 1.11] | medium | * |
| Increase by 2 vs Increase by 3 | 2.25 | 22 | = 0.052 | 0.30 [0.01, 0.92] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 317.84, BIC = 328.27
- **Increase by 2 vs Increase by 1**: *β* = 0.95, *SE* = 3.274, *z* = 0.291, *p* = 0.771
- **Increase by 3 vs Increase by 1**: *β* = -1.26, *SE* = 3.325, *z* = -0.378, *p* = 0.706
- **SNR**: *β* = 0.55, *SE* = 0.626, *z* = 0.873, *p* = 0.382

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.95 | 3.27 | -0.29 | 0.771 | 0.913 | n.s. |
| Increase by 1 - Increase by 3 | 1.26 | 3.33 | 0.38 | 0.706 | 0.913 | n.s. |
| Increase by 2 - Increase by 3 | 2.21 | 3.34 | 0.66 | 0.509 | 0.881 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.395, η²_G = 0.046
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.49 | 8 | = 0.640 | -0.23 [-0.66, 0.78] | small | n.s. |
| Increase by 1 vs Increase by 3 | 1.21 | 8 | = 0.393 | 0.28 [-0.50, 0.95] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.27 | 8 | = 0.393 | 0.48 [-0.43, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 118.43, BIC = 128.86
- **Increase by 2 vs Increase by 1**: *β* = 0.02, *SE* = 0.349, *z* = 0.061, *p* = 0.952
- **Increase by 3 vs Increase by 1**: *β* = 0.05, *SE* = 0.363, *z* = 0.131, *p* = 0.895
- **SNR**: *β* = 0.39, *SE* = 0.180, *z* = 2.171, *p* = 0.030

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.02 | 0.35 | -0.06 | 0.952 | 0.999 | n.s. |
| Increase by 1 - Increase by 3 | -0.05 | 0.36 | -0.13 | 0.895 | 0.999 | n.s. |
| Increase by 2 - Increase by 3 | -0.03 | 0.44 | -0.06 | 0.952 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.09, *p* = 0.156, η²_G = 0.045
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.58 | 8 | = 0.578 | 0.16 [-0.55, 0.89] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -1.26 | 8 | = 0.367 | -0.35 [-1.25, 0.27] | small | n.s. |
| Increase by 2 vs Increase by 3 | -2.80 | 8 | = 0.070 | -0.47 [-1.37, 0.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 559.41, BIC = 571.35
- **Increase by 2 vs Increase by 1**: *β* = -7.31, *SE* = 11.663, *z* = -0.627, *p* = 0.531
- **Increase by 3 vs Increase by 1**: *β* = -18.83, *SE* = 11.130, *z* = -1.692, *p* = 0.091
- **SNR**: *β* = 0.29, *SE* = 1.221, *z* = 0.239, *p* = 0.811

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 7.31 | 11.66 | 0.63 | 0.531 | 0.531 | n.s. |
| Increase by 1 - Increase by 3 | 18.83 | 11.13 | 1.69 | 0.091 | 0.248 | n.s. |
| Increase by 2 - Increase by 3 | 11.52 | 11.41 | 1.01 | 0.313 | 0.528 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.353, η²_G = 0.033
- Greenhouse-Geisser corrected: *p* = 0.336 (ε = 0.704)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.54 | 15 | = 0.596 | 0.17 [-0.40, 0.67] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.21 | 15 | = 0.366 | 0.41 [-0.15, 0.92] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.43 | 15 | = 0.366 | 0.28 [-0.17, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 194.54, BIC = 206.48
- **Increase by 2 vs Increase by 1**: *β* = 0.58, *SE* = 0.280, *z* = 2.091, *p* = 0.037
- **Increase by 3 vs Increase by 1**: *β* = 0.37, *SE* = 0.261, *z* = 1.415, *p* = 0.157
- **SNR**: *β* = 0.11, *SE* = 0.037, *z* = 3.008, *p* = 0.003

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.59 | 0.28 | -2.09 | 0.037 | 0.106 | n.s. |
| Increase by 1 - Increase by 3 | -0.37 | 0.26 | -1.42 | 0.157 | 0.289 | n.s. |
| Increase by 2 - Increase by 3 | 0.22 | 0.28 | 0.78 | 0.436 | 0.436 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.83, *p* = 0.033, η²_G = 0.018
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -2.42 | 15 | = 0.086 | -0.31 [-1.18, -0.03] | small | n.s. |
| Increase by 1 vs Increase by 3 | -1.79 | 15 | = 0.141 | -0.14 [-1.01, 0.08] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 1.40 | 15 | = 0.181 | 0.18 [-0.12, 0.91] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.006). Post-hoc tests revealed:
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.51)
**P3b amplitude:** Significant main effect of condition (*p* = 0.033) (no significant pairwise comparisons)

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
