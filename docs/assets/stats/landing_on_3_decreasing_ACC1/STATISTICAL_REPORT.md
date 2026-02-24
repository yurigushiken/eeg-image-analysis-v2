# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:28:26

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
| 4 to 3 | 24 | 104.17 ms | 9.54 | 1.95 | [88.00, 116.00] |
| 5 to 3 | 24 | 102.83 ms | 10.18 | 2.08 | [88.00, 116.00] |
| 6 to 3 | 24 | 103.33 ms | 10.05 | 2.05 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | -0.79 µV | 2.18 | 0.44 | [-6.08, 2.67] |
| 5 to 3 | 24 | -2.76 µV | 2.09 | 0.43 | [-6.90, 1.42] |
| 6 to 3 | 24 | -1.91 µV | 1.63 | 0.33 | [-5.28, 1.40] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 177.00 ms | 20.74 | 4.23 | [152.00, 220.00] |
| 5 to 3 | 24 | 173.83 ms | 17.13 | 3.50 | [140.00, 208.00] |
| 6 to 3 | 24 | 176.50 ms | 16.61 | 3.39 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | -6.10 µV | 2.78 | 0.57 | [-10.92, 1.75] |
| 5 to 3 | 24 | -6.05 µV | 2.71 | 0.55 | [-12.11, -1.76] |
| 6 to 3 | 24 | -6.55 µV | 2.33 | 0.48 | [-11.28, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 109.17 ms | 9.54 | 1.95 | [96.00, 120.00] |
| 5 to 3 | 24 | 110.00 ms | 9.51 | 1.94 | [96.00, 120.00] |
| 6 to 3 | 24 | 108.33 ms | 10.00 | 2.04 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 0.82 µV | 2.24 | 0.46 | [-3.29, 5.30] |
| 5 to 3 | 24 | 2.02 µV | 2.15 | 0.44 | [-3.07, 4.61] |
| 6 to 3 | 24 | 1.77 µV | 2.33 | 0.48 | [-2.16, 7.81] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 472.67 ms | 35.42 | 7.23 | [412.00, 532.00] |
| 5 to 3 | 24 | 463.00 ms | 28.41 | 5.80 | [412.00, 532.00] |
| 6 to 3 | 24 | 461.83 ms | 32.69 | 6.67 | [412.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 4.98 µV | 3.56 | 0.73 | [-1.86, 11.65] |
| 5 to 3 | 24 | 4.82 µV | 3.22 | 0.66 | [-3.30, 10.28] |
| 6 to 3 | 24 | 5.17 µV | 4.21 | 0.86 | [-2.53, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 541.46, BIC = 555.12
- **5 to 3 vs 4 to 3**: *β* = -2.50, *SE* = 2.825, *z* = -0.886, *p* = 0.375
- **6 to 3 vs 4 to 3**: *β* = -0.95, *SE* = 2.636, *z* = -0.361, *p* = 0.718
- **SNR**: *β* = 1.29, *SE* = 1.123, *z* = 1.147, *p* = 0.251

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 2.50 | 2.83 | 0.89 | 0.375 | 0.756 | n.s. |
| 4 to 3 - 6 to 3 | 0.95 | 2.64 | 0.36 | 0.718 | 0.822 | n.s. |
| 5 to 3 - 6 to 3 | -1.55 | 2.79 | -0.56 | 0.578 | 0.822 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.13, *p* = 0.882, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.50 | 23 | = 0.854 | 0.14 [-0.32, 0.53] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.31 | 23 | = 0.854 | 0.09 [-0.36, 0.49] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.19 | 23 | = 0.854 | -0.05 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 293.12, BIC = 306.78
- **5 to 3 vs 4 to 3**: *β* = -1.32, *SE* = 0.456, *z* = -2.900, *p* = 0.004
- **6 to 3 vs 4 to 3**: *β* = -1.06, *SE* = 0.421, *z* = -2.511, *p* = 0.012
- **SNR**: *β* = -0.71, *SE* = 0.193, *z* = -3.658, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 1.32 | 0.46 | 2.90 | 0.004 | 0.011 | * |
| 4 to 3 - 6 to 3 | 1.06 | 0.42 | 2.51 | 0.012 | 0.024 | * |
| 5 to 3 - 6 to 3 | -0.27 | 0.45 | -0.59 | 0.555 | 0.555 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.67, *p* < .001, η²_G = 0.147
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 3.66 | 23 | = 0.004 | 0.92 [0.27, 1.22] | large | ** |
| 4 to 3 vs 6 to 3 | 3.05 | 23 | = 0.009 | 0.58 [0.16, 1.08] | medium | ** |
| 5 to 3 vs 6 to 3 | -1.69 | 23 | = 0.105 | -0.45 [-0.78, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 613.71, BIC = 627.37
- **5 to 3 vs 4 to 3**: *β* = -3.16, *SE* = 3.591, *z* = -0.881, *p* = 0.378
- **6 to 3 vs 4 to 3**: *β* = -0.50, *SE* = 3.595, *z* = -0.140, *p* = 0.889
- **SNR**: *β* = 0.01, *SE* = 0.662, *z* = 0.019, *p* = 0.985

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 3.16 | 3.59 | 0.88 | 0.378 | 0.760 | n.s. |
| 4 to 3 - 6 to 3 | 0.50 | 3.60 | 0.14 | 0.889 | 0.889 | n.s. |
| 5 to 3 - 6 to 3 | -2.66 | 3.60 | -0.74 | 0.460 | 0.760 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.43, *p* = 0.652, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.74 | 23 | = 0.697 | 0.17 [-0.27, 0.58] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.16 | 23 | = 0.878 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.77 | 23 | = 0.697 | -0.16 [-0.58, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 330.42, BIC = 344.08
- **5 to 3 vs 4 to 3**: *β* = -0.02, *SE* = 0.572, *z* = -0.032, *p* = 0.974
- **6 to 3 vs 4 to 3**: *β* = -0.33, *SE* = 0.572, *z* = -0.577, *p* = 0.564
- **SNR**: *β* = -0.39, *SE* = 0.095, *z* = -4.133, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.02 | 0.57 | 0.03 | 0.974 | 0.974 | n.s. |
| 4 to 3 - 6 to 3 | 0.33 | 0.57 | 0.58 | 0.564 | 0.917 | n.s. |
| 5 to 3 - 6 to 3 | 0.31 | 0.57 | 0.54 | 0.587 | 0.917 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.683, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.07 | 23 | = 0.941 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.69 | 23 | = 0.743 | 0.18 [-0.28, 0.57] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.90 | 23 | = 0.743 | 0.20 [-0.24, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 517.06, BIC = 530.72
- **5 to 3 vs 4 to 3**: *β* = 1.09, *SE* = 1.799, *z* = 0.604, *p* = 0.546
- **6 to 3 vs 4 to 3**: *β* = -0.88, *SE* = 1.781, *z* = -0.497, *p* = 0.619
- **SNR**: *β* = -0.51, *SE* = 0.532, *z* = -0.965, *p* = 0.335

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -1.09 | 1.80 | -0.60 | 0.546 | 0.794 | n.s. |
| 4 to 3 - 6 to 3 | 0.88 | 1.78 | 0.50 | 0.619 | 0.794 | n.s. |
| 5 to 3 - 6 to 3 | 1.97 | 1.81 | 1.09 | 0.276 | 0.620 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.664, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.48 | 23 | = 0.669 | -0.09 [-0.52, 0.33] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.43 | 23 | = 0.669 | 0.09 [-0.33, 0.51] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.91 | 23 | = 0.669 | 0.17 [-0.24, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.00, BIC = 328.66
- **5 to 3 vs 4 to 3**: *β* = 1.05, *SE* = 0.485, *z* = 2.161, *p* = 0.031
- **6 to 3 vs 4 to 3**: *β* = 0.98, *SE* = 0.481, *z* = 2.042, *p* = 0.041
- **SNR**: *β* = 0.29, *SE* = 0.138, *z* = 2.135, *p* = 0.033

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -1.05 | 0.49 | -2.16 | 0.031 | 0.089 | n.s. |
| 4 to 3 - 6 to 3 | -0.98 | 0.48 | -2.04 | 0.041 | 0.089 | n.s. |
| 5 to 3 - 6 to 3 | 0.07 | 0.49 | 0.14 | 0.891 | 0.891 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.13, *p* = 0.053, η²_G = 0.052
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -2.14 | 23 | = 0.091 | -0.54 [-0.88, 0.00] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -1.97 | 23 | = 0.091 | -0.42 [-0.84, 0.04] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.51 | 23 | = 0.613 | 0.11 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 712.07, BIC = 725.73
- **5 to 3 vs 4 to 3**: *β* = -9.74, *SE* = 8.468, *z* = -1.150, *p* = 0.250
- **6 to 3 vs 4 to 3**: *β* = -10.97, *SE* = 8.469, *z* = -1.295, *p* = 0.195
- **SNR**: *β* = 1.00, *SE* = 1.118, *z* = 0.895, *p* = 0.371

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 9.74 | 8.47 | 1.15 | 0.250 | 0.479 | n.s. |
| 4 to 3 - 6 to 3 | 10.97 | 8.47 | 1.30 | 0.195 | 0.479 | n.s. |
| 5 to 3 - 6 to 3 | 1.23 | 8.47 | 0.14 | 0.885 | 0.885 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.409, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.99 | 23 | = 0.497 | 0.30 [-0.22, 0.63] | small | n.s. |
| 4 to 3 vs 6 to 3 | 1.25 | 23 | = 0.497 | 0.32 [-0.17, 0.68] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.15 | 23 | = 0.884 | 0.04 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 350.98, BIC = 364.64
- **5 to 3 vs 4 to 3**: *β* = -0.18, *SE* = 0.521, *z* = -0.354, *p* = 0.724
- **6 to 3 vs 4 to 3**: *β* = 0.15, *SE* = 0.522, *z* = 0.295, *p* = 0.768
- **SNR**: *β* = 0.31, *SE* = 0.089, *z* = 3.441, *p* = 0.001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.18 | 0.52 | 0.35 | 0.724 | 0.924 | n.s. |
| 4 to 3 - 6 to 3 | -0.15 | 0.52 | -0.29 | 0.768 | 0.924 | n.s. |
| 5 to 3 - 6 to 3 | -0.34 | 0.52 | -0.65 | 0.516 | 0.887 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.20, *p* = 0.822, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.29 | 23 | = 0.772 | 0.05 [-0.36, 0.48] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.35 | 23 | = 0.772 | -0.05 [-0.50, 0.35] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.59 | 23 | = 0.772 | -0.10 [-0.55, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 3 showed greater amplitude than 5 to 3 (*d* = 0.92)
  - 4 to 3 showed greater amplitude than 6 to 3 (*d* = 0.58)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.053)

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
