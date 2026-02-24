# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:19:44

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
| 1 to 2 | 24 | 90.17 ms | 9.87 | 2.01 | [80.00, 104.00] |
| 1 to 3 | 24 | 91.67 ms | 10.54 | 2.15 | [80.00, 104.00] |
| 1 to 4 | 24 | 96.17 ms | 9.10 | 1.86 | [80.00, 104.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -0.52 µV | 2.16 | 0.44 | [-5.08, 4.02] |
| 1 to 3 | 24 | -0.21 µV | 2.26 | 0.46 | [-5.86, 3.15] |
| 1 to 4 | 24 | -1.31 µV | 1.90 | 0.39 | [-4.33, 3.17] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 173.17 ms | 19.96 | 4.08 | [144.00, 216.00] |
| 1 to 3 | 24 | 168.50 ms | 22.91 | 4.68 | [136.00, 216.00] |
| 1 to 4 | 24 | 172.83 ms | 21.20 | 4.33 | [136.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -5.32 µV | 2.41 | 0.49 | [-9.95, -0.30] |
| 1 to 3 | 24 | -6.66 µV | 2.55 | 0.52 | [-12.65, -2.71] |
| 1 to 4 | 24 | -6.34 µV | 2.95 | 0.60 | [-12.55, -1.25] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 84.50 ms | 12.72 | 2.60 | [68.00, 100.00] |
| 1 to 3 | 24 | 83.83 ms | 13.37 | 2.73 | [68.00, 100.00] |
| 1 to 4 | 24 | 90.00 ms | 11.38 | 2.32 | [68.00, 100.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 1.11 µV | 1.96 | 0.40 | [-2.48, 4.45] |
| 1 to 3 | 24 | 0.97 µV | 2.07 | 0.42 | [-2.33, 7.47] |
| 1 to 4 | 24 | 1.68 µV | 1.61 | 0.33 | [-1.51, 4.28] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 455.50 ms | 56.13 | 11.46 | [368.00, 536.00] |
| 1 to 3 | 24 | 462.00 ms | 47.52 | 9.70 | [368.00, 536.00] |
| 1 to 4 | 24 | 465.50 ms | 53.95 | 11.01 | [376.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 4.33 µV | 3.81 | 0.78 | [-3.51, 11.99] |
| 1 to 3 | 24 | 5.08 µV | 3.95 | 0.81 | [-1.07, 15.57] |
| 1 to 4 | 24 | 5.02 µV | 3.71 | 0.76 | [-1.27, 13.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 532.27, BIC = 545.93
- **1 to 3 vs 1 to 2**: *β* = 1.60, *SE* = 2.162, *z* = 0.743, *p* = 0.458
- **1 to 4 vs 1 to 2**: *β* = 6.00, *SE* = 2.144, *z* = 2.798, *p* = 0.005
- **SNR**: *β* = -0.30, *SE* = 0.789, *z* = -0.381, *p* = 0.703

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -1.61 | 2.16 | -0.74 | 0.458 | 0.458 | n.s. |
| 1 to 2 - 1 to 4 | -6.00 | 2.14 | -2.80 | 0.005 | 0.015 | * |
| 1 to 3 - 1 to 4 | -4.39 | 2.16 | -2.03 | 0.042 | 0.082 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.00, *p* = 0.025, η²_G = 0.065
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.87 | 23 | = 0.396 | -0.15 [-0.60, 0.25] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -2.70 | 23 | = 0.038 | -0.63 [-1.00, -0.10] | medium | * |
| 1 to 3 vs 1 to 4 | -1.74 | 23 | = 0.143 | -0.46 [-0.79, 0.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 319.94, BIC = 333.60
- **1 to 3 vs 1 to 2**: *β* = 0.25, *SE* = 0.584, *z* = 0.436, *p* = 0.663
- **1 to 4 vs 1 to 2**: *β* = -0.79, *SE* = 0.580, *z* = -1.353, *p* = 0.176
- **SNR**: *β* = 0.16, *SE* = 0.178, *z* = 0.888, *p* = 0.374

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.25 | 0.58 | -0.44 | 0.663 | 0.663 | n.s. |
| 1 to 2 - 1 to 4 | 0.79 | 0.58 | 1.35 | 0.176 | 0.321 | n.s. |
| 1 to 3 - 1 to 4 | 1.04 | 0.58 | 1.78 | 0.075 | 0.208 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.80, *p* = 0.176, η²_G = 0.047
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.62 | 23 | = 0.538 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 1.35 | 23 | = 0.286 | 0.39 [-0.16, 0.71] | small | n.s. |
| 1 to 3 vs 1 to 4 | 1.59 | 23 | = 0.286 | 0.52 [-0.11, 0.76] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 642.63, BIC = 656.29
- **1 to 3 vs 1 to 2**: *β* = -3.45, *SE* = 4.826, *z* = -0.716, *p* = 0.474
- **1 to 4 vs 1 to 2**: *β* = -0.00, *SE* = 4.613, *z* = -0.001, *p* = 0.999
- **SNR**: *β* = -0.72, *SE* = 0.877, *z* = -0.823, *p* = 0.410

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 3.45 | 4.83 | 0.72 | 0.474 | 0.847 | n.s. |
| 1 to 2 - 1 to 4 | 0.00 | 4.61 | 0.00 | 0.999 | 0.999 | n.s. |
| 1 to 3 - 1 to 4 | -3.45 | 4.72 | -0.73 | 0.465 | 0.847 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.60, *p* = 0.551, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.90 | 23 | = 0.568 | 0.22 [-0.24, 0.61] | small | n.s. |
| 1 to 2 vs 1 to 4 | 0.06 | 23 | = 0.951 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.31 | 23 | = 0.568 | -0.20 [-0.70, 0.16] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 299.50, BIC = 313.16
- **1 to 3 vs 1 to 2**: *β* = -0.55, *SE* = 0.424, *z* = -1.300, *p* = 0.194
- **1 to 4 vs 1 to 2**: *β* = -0.81, *SE* = 0.402, *z* = -2.004, *p* = 0.045
- **SNR**: *β* = -0.47, *SE* = 0.083, *z* = -5.640, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.55 | 0.42 | 1.30 | 0.194 | 0.350 | n.s. |
| 1 to 2 - 1 to 4 | 0.81 | 0.40 | 2.00 | 0.045 | 0.129 | n.s. |
| 1 to 3 - 1 to 4 | 0.26 | 0.41 | 0.62 | 0.537 | 0.537 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.35, *p* = 0.019, η²_G = 0.046
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 3.27 | 23 | = 0.010 | 0.54 [0.20, 1.14] | medium | ** |
| 1 to 2 vs 1 to 4 | 2.02 | 23 | = 0.082 | 0.38 [-0.03, 0.85] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.63 | 23 | = 0.534 | -0.11 [-0.55, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 575.70, BIC = 589.36
- **1 to 3 vs 1 to 2**: *β* = -0.46, *SE* = 3.441, *z* = -0.132, *p* = 0.895
- **1 to 4 vs 1 to 2**: *β* = 5.69, *SE* = 3.440, *z* = 1.654, *p* = 0.098
- **SNR**: *β* = 1.28, *SE* = 1.128, *z* = 1.131, *p* = 0.258

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.46 | 3.44 | 0.13 | 0.895 | 0.895 | n.s. |
| 1 to 2 - 1 to 4 | -5.69 | 3.44 | -1.65 | 0.098 | 0.205 | n.s. |
| 1 to 3 - 1 to 4 | -6.15 | 3.44 | -1.79 | 0.074 | 0.205 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.169, η²_G = 0.048
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.21 | 23 | = 0.834 | 0.05 [-0.38, 0.47] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.60 | 23 | = 0.195 | -0.46 [-0.76, 0.11] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.57 | 23 | = 0.195 | -0.50 [-0.75, 0.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.40, BIC = 316.06
- **1 to 3 vs 1 to 2**: *β* = -0.10, *SE* = 0.502, *z* = -0.207, *p* = 0.836
- **1 to 4 vs 1 to 2**: *β* = 0.60, *SE* = 0.502, *z* = 1.204, *p* = 0.229
- **SNR**: *β* = 0.23, *SE* = 0.168, *z* = 1.366, *p* = 0.172

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.10 | 0.50 | 0.21 | 0.836 | 0.836 | n.s. |
| 1 to 2 - 1 to 4 | -0.60 | 0.50 | -1.20 | 0.229 | 0.405 | n.s. |
| 1 to 3 - 1 to 4 | -0.71 | 0.50 | -1.41 | 0.158 | 0.403 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.354, η²_G = 0.027
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.27 | 23 | = 0.793 | 0.07 [-0.37, 0.48] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.15 | 23 | = 0.392 | -0.32 [-0.66, 0.19] | small | n.s. |
| 1 to 3 vs 1 to 4 | -1.37 | 23 | = 0.392 | -0.38 [-0.71, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 781.45, BIC = 795.11
- **1 to 3 vs 1 to 2**: *β* = 7.95, *SE* = 14.119, *z* = 0.563, *p* = 0.574
- **1 to 4 vs 1 to 2**: *β* = 11.05, *SE* = 14.090, *z* = 0.784, *p* = 0.433
- **SNR**: *β* = -2.58, *SE* = 2.367, *z* = -1.092, *p* = 0.275

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -7.95 | 14.12 | -0.56 | 0.574 | 0.818 | n.s. |
| 1 to 2 - 1 to 4 | -11.05 | 14.09 | -0.78 | 0.433 | 0.818 | n.s. |
| 1 to 3 - 1 to 4 | -3.10 | 14.06 | -0.22 | 0.825 | 0.825 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.26, *p* = 0.771, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.42 | 23 | = 0.771 | -0.12 [-0.51, 0.34] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.69 | 23 | = 0.771 | -0.18 [-0.56, 0.28] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -0.29 | 23 | = 0.771 | -0.07 [-0.48, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 355.28, BIC = 368.94
- **1 to 3 vs 1 to 2**: *β* = 0.62, *SE* = 0.533, *z* = 1.156, *p* = 0.248
- **1 to 4 vs 1 to 2**: *β* = 0.60, *SE* = 0.531, *z* = 1.127, *p* = 0.260
- **SNR**: *β* = 0.22, *SE* = 0.121, *z* = 1.852, *p* = 0.064

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.62 | 0.53 | -1.16 | 0.248 | 0.574 | n.s. |
| 1 to 2 - 1 to 4 | -0.60 | 0.53 | -1.13 | 0.260 | 0.574 | n.s. |
| 1 to 3 - 1 to 4 | 0.02 | 0.53 | 0.03 | 0.973 | 0.973 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.20, *p* = 0.309, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.32 | 23 | = 0.383 | -0.19 [-0.70, 0.16] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.17 | 23 | = 0.383 | -0.18 [-0.67, 0.19] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.12 | 23 | = 0.905 | 0.01 [-0.40, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.025). Post-hoc tests revealed:
  - 1 to 2 showed smaller latency than 1 to 4 (*d* = -0.63)
**N1 amplitude:** Significant main effect of condition (*p* = 0.019). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than 1 to 3 (*d* = 0.54)

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
