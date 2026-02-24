# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:17:43

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
| 3 to 1 | 24 | 110.50 ms | 9.50 | 1.94 | [96.00, 120.00] |
| 4 to 2 | 24 | 109.33 ms | 8.31 | 1.70 | [96.00, 120.00] |
| 5 to 3 | 24 | 106.00 ms | 9.21 | 1.88 | [96.00, 120.00] |
| 6 to 4 | 24 | 108.67 ms | 8.88 | 1.81 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -1.82 µV | 2.16 | 0.44 | [-6.48, 1.38] |
| 4 to 2 | 24 | -0.81 µV | 2.79 | 0.57 | [-4.94, 5.95] |
| 5 to 3 | 24 | -2.75 µV | 2.15 | 0.44 | [-6.90, 1.42] |
| 6 to 4 | 24 | -2.25 µV | 2.24 | 0.46 | [-8.69, 1.93] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 182.67 ms | 14.09 | 2.88 | [156.00, 208.00] |
| 4 to 2 | 24 | 178.33 ms | 14.96 | 3.05 | [148.00, 208.00] |
| 5 to 3 | 24 | 174.50 ms | 15.86 | 3.24 | [148.00, 208.00] |
| 6 to 4 | 24 | 174.33 ms | 20.15 | 4.11 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -4.20 µV | 2.81 | 0.57 | [-10.41, -0.12] |
| 4 to 2 | 24 | -6.16 µV | 3.06 | 0.62 | [-12.20, -2.20] |
| 5 to 3 | 24 | -5.93 µV | 2.79 | 0.57 | [-12.11, -1.76] |
| 6 to 4 | 24 | -5.80 µV | 3.00 | 0.61 | [-12.20, -0.24] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 116.33 ms | 10.34 | 2.11 | [100.00, 128.00] |
| 4 to 2 | 24 | 116.50 ms | 10.03 | 2.05 | [100.00, 128.00] |
| 5 to 3 | 24 | 114.33 ms | 10.54 | 2.15 | [100.00, 128.00] |
| 6 to 4 | 24 | 112.50 ms | 10.57 | 2.16 | [100.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 3.42 µV | 2.27 | 0.46 | [-3.47, 9.14] |
| 4 to 2 | 24 | 1.08 µV | 2.76 | 0.56 | [-4.63, 4.87] |
| 5 to 3 | 24 | 2.10 µV | 2.21 | 0.45 | [-3.07, 4.76] |
| 6 to 4 | 24 | 2.63 µV | 2.72 | 0.55 | [-2.71, 7.45] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 484.17 ms | 30.88 | 6.30 | [428.00, 536.00] |
| 4 to 2 | 24 | 478.00 ms | 37.60 | 7.67 | [428.00, 536.00] |
| 5 to 3 | 24 | 465.67 ms | 24.80 | 5.06 | [428.00, 536.00] |
| 6 to 4 | 24 | 484.17 ms | 36.04 | 7.36 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 5.17 µV | 3.65 | 0.75 | [-1.29, 16.27] |
| 4 to 2 | 24 | 4.36 µV | 4.35 | 0.89 | [-3.59, 14.41] |
| 5 to 3 | 24 | 4.68 µV | 3.29 | 0.67 | [-3.30, 10.28] |
| 6 to 4 | 24 | 4.62 µV | 3.82 | 0.78 | [-3.09, 13.11] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 700.22, BIC = 718.17
- **4 to 2 vs 3 to 1**: *β* = -1.24, *SE* = 2.324, *z* = -0.532, *p* = 0.595
- **5 to 3 vs 3 to 1**: *β* = -4.93, *SE* = 2.394, *z* = -2.058, *p* = 0.040
- **6 to 4 vs 3 to 1**: *β* = -2.03, *SE* = 2.338, *z* = -0.868, *p* = 0.385
- **SNR**: *β* = 0.49, *SE* = 0.672, *z* = 0.734, *p* = 0.463

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 1.24 | 2.32 | 0.53 | 0.595 | 0.836 | n.s. |
| 3 to 1 - 5 to 3 | 4.93 | 2.39 | 2.06 | 0.040 | 0.215 | n.s. |
| 3 to 1 - 6 to 4 | 2.03 | 2.34 | 0.87 | 0.385 | 0.768 | n.s. |
| 4 to 2 - 5 to 3 | 3.69 | 2.37 | 1.56 | 0.120 | 0.472 | n.s. |
| 4 to 2 - 6 to 4 | 0.79 | 2.33 | 0.34 | 0.734 | 0.836 | n.s. |
| 5 to 3 - 6 to 4 | -2.90 | 2.34 | -1.24 | 0.216 | 0.623 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.286, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.52 | 23 | = 0.729 | 0.13 [-0.32, 0.53] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 1.57 | 23 | = 0.454 | 0.48 [-0.11, 0.75] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.82 | 23 | = 0.634 | 0.20 [-0.26, 0.59] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | 1.35 | 23 | = 0.454 | 0.38 [-0.15, 0.71] | small | n.s. |
| 4 to 2 vs 6 to 4 | 0.30 | 23 | = 0.768 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | -1.24 | 23 | = 0.454 | -0.29 [-0.68, 0.18] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 439.64, BIC = 457.59
- **4 to 2 vs 3 to 1**: *β* = 1.05, *SE* = 0.593, *z* = 1.768, *p* = 0.077
- **5 to 3 vs 3 to 1**: *β* = -0.66, *SE* = 0.611, *z* = -1.073, *p* = 0.283
- **6 to 4 vs 3 to 1**: *β* = -0.31, *SE* = 0.596, *z* = -0.523, *p* = 0.601
- **SNR**: *β* = -0.32, *SE* = 0.172, *z* = -1.855, *p* = 0.064

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -1.05 | 0.59 | -1.77 | 0.077 | 0.275 | n.s. |
| 3 to 1 - 5 to 3 | 0.66 | 0.61 | 1.07 | 0.283 | 0.632 | n.s. |
| 3 to 1 - 6 to 4 | 0.31 | 0.60 | 0.52 | 0.601 | 0.812 | n.s. |
| 4 to 2 - 5 to 3 | 1.70 | 0.61 | 2.81 | 0.005 | 0.029 | * |
| 4 to 2 - 6 to 4 | 1.36 | 0.59 | 2.29 | 0.022 | 0.105 | n.s. |
| 5 to 3 - 6 to 4 | -0.34 | 0.60 | -0.57 | 0.566 | 0.812 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.54, *p* = 0.019, η²_G = 0.087
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -1.49 | 23 | = 0.224 | -0.40 [-0.74, 0.13] | small | n.s. |
| 3 to 1 vs 5 to 3 | 1.70 | 23 | = 0.203 | 0.43 [-0.09, 0.78] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.78 | 23 | = 0.443 | 0.20 [-0.27, 0.58] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | 2.81 | 23 | = 0.060 | 0.78 [0.12, 1.03] | medium | n.s. |
| 4 to 2 vs 6 to 4 | 2.16 | 23 | = 0.124 | 0.57 [-0.00, 0.88] | medium | n.s. |
| 5 to 3 vs 6 to 4 | -0.88 | 23 | = 0.443 | -0.22 [-0.61, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 794.39, BIC = 812.34
- **4 to 2 vs 3 to 1**: *β* = -5.10, *SE* = 3.406, *z* = -1.497, *p* = 0.134
- **5 to 3 vs 3 to 1**: *β* = -9.48, *SE* = 3.486, *z* = -2.719, *p* = 0.007
- **6 to 4 vs 3 to 1**: *β* = -9.86, *SE* = 3.529, *z* = -2.795, *p* = 0.005
- **SNR**: *β* = 0.63, *SE* = 0.440, *z* = 1.432, *p* = 0.152

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 5.10 | 3.41 | 1.50 | 0.134 | 0.438 | n.s. |
| 3 to 1 - 5 to 3 | 9.48 | 3.49 | 2.72 | 0.007 | 0.032 | * |
| 3 to 1 - 6 to 4 | 9.86 | 3.53 | 2.79 | 0.005 | 0.031 | * |
| 4 to 2 - 5 to 3 | 4.38 | 3.38 | 1.29 | 0.196 | 0.438 | n.s. |
| 4 to 2 - 6 to 4 | 4.76 | 3.41 | 1.40 | 0.162 | 0.438 | n.s. |
| 5 to 3 - 6 to 4 | 0.39 | 3.37 | 0.11 | 0.909 | 0.909 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.54, *p* = 0.064, η²_G = 0.043
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.37 | 23 | = 0.355 | 0.30 [-0.15, 0.71] | small | n.s. |
| 3 to 1 vs 5 to 3 | 2.96 | 23 | = 0.042 | 0.54 [0.14, 1.06] | medium | * |
| 3 to 1 vs 6 to 4 | 2.16 | 23 | = 0.123 | 0.48 [-0.00, 0.88] | small | n.s. |
| 4 to 2 vs 5 to 3 | 1.22 | 23 | = 0.355 | 0.25 [-0.18, 0.68] | small | n.s. |
| 4 to 2 vs 6 to 4 | 0.93 | 23 | = 0.433 | 0.23 [-0.24, 0.62] | small | n.s. |
| 5 to 3 vs 6 to 4 | 0.05 | 23 | = 0.963 | 0.01 [-0.41, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 441.24, BIC = 459.19
- **4 to 2 vs 3 to 1**: *β* = -1.48, *SE* = 0.555, *z* = -2.663, *p* = 0.008
- **5 to 3 vs 3 to 1**: *β* = -0.90, *SE* = 0.568, *z* = -1.589, *p* = 0.112
- **6 to 4 vs 3 to 1**: *β* = -0.64, *SE* = 0.575, *z* = -1.107, *p* = 0.268
- **SNR**: *β* = -0.39, *SE* = 0.071, *z* = -5.526, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 1.48 | 0.56 | 2.66 | 0.008 | 0.046 | * |
| 3 to 1 - 5 to 3 | 0.90 | 0.57 | 1.59 | 0.112 | 0.448 | n.s. |
| 3 to 1 - 6 to 4 | 0.64 | 0.57 | 1.11 | 0.268 | 0.608 | n.s. |
| 4 to 2 - 5 to 3 | -0.58 | 0.55 | -1.04 | 0.297 | 0.608 | n.s. |
| 4 to 2 - 6 to 4 | -0.84 | 0.55 | -1.52 | 0.130 | 0.448 | n.s. |
| 5 to 3 - 6 to 4 | -0.27 | 0.55 | -0.48 | 0.628 | 0.628 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.87, *p* = 0.013, η²_G = 0.068
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 3.69 | 23 | = 0.007 | 0.67 [0.28, 1.23] | medium | ** |
| 3 to 1 vs 5 to 3 | 2.55 | 23 | = 0.053 | 0.61 [0.07, 0.97] | medium | n.s. |
| 3 to 1 vs 6 to 4 | 2.05 | 23 | = 0.104 | 0.55 [-0.02, 0.86] | medium | n.s. |
| 4 to 2 vs 5 to 3 | -0.37 | 23 | = 0.837 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -0.63 | 23 | = 0.806 | -0.12 [-0.55, 0.30] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | -0.21 | 23 | = 0.837 | -0.04 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 719.53, BIC = 737.48
- **4 to 2 vs 3 to 1**: *β* = -0.00, *SE* = 2.413, *z* = -0.002, *p* = 0.999
- **5 to 3 vs 3 to 1**: *β* = -2.00, *SE* = 2.408, *z* = -0.831, *p* = 0.406
- **6 to 4 vs 3 to 1**: *β* = -3.69, *SE* = 2.412, *z* = -1.529, *p* = 0.126
- **SNR**: *β* = -0.48, *SE* = 0.429, *z* = -1.111, *p* = 0.267

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 0.00 | 2.41 | 0.00 | 0.999 | 0.999 | n.s. |
| 3 to 1 - 5 to 3 | 2.00 | 2.41 | 0.83 | 0.406 | 0.876 | n.s. |
| 3 to 1 - 6 to 4 | 3.69 | 2.41 | 1.53 | 0.126 | 0.555 | n.s. |
| 4 to 2 - 5 to 3 | 2.00 | 2.41 | 0.83 | 0.408 | 0.876 | n.s. |
| 4 to 2 - 6 to 4 | 3.68 | 2.43 | 1.52 | 0.129 | 0.555 | n.s. |
| 5 to 3 - 6 to 4 | 1.69 | 2.41 | 0.70 | 0.484 | 0.876 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.15, *p* = 0.336, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -0.07 | 23 | = 0.949 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.77 | 23 | = 0.575 | 0.19 [-0.27, 0.58] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 1.69 | 23 | = 0.434 | 0.37 [-0.09, 0.78] | small | n.s. |
| 4 to 2 vs 5 to 3 | 0.93 | 23 | = 0.575 | 0.21 [-0.24, 0.62] | small | n.s. |
| 4 to 2 vs 6 to 4 | 1.51 | 23 | = 0.434 | 0.39 [-0.12, 0.74] | small | n.s. |
| 5 to 3 vs 6 to 4 | 0.72 | 23 | = 0.575 | 0.17 [-0.28, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 437.84, BIC = 455.79
- **4 to 2 vs 3 to 1**: *β* = -2.23, *SE* = 0.560, *z* = -3.990, *p* < .001
- **5 to 3 vs 3 to 1**: *β* = -1.31, *SE* = 0.559, *z* = -2.348, *p* = 0.019
- **6 to 4 vs 3 to 1**: *β* = -0.88, *SE* = 0.560, *z* = -1.565, *p* = 0.118
- **SNR**: *β* = 0.28, *SE* = 0.100, *z* = 2.863, *p* = 0.004

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 2.23 | 0.56 | 3.99 | < .001 | < .001 | *** |
| 3 to 1 - 5 to 3 | 1.31 | 0.56 | 2.35 | 0.019 | 0.077 | n.s. |
| 3 to 1 - 6 to 4 | 0.88 | 0.56 | 1.57 | 0.118 | 0.270 | n.s. |
| 4 to 2 - 5 to 3 | -0.92 | 0.56 | -1.65 | 0.100 | 0.270 | n.s. |
| 4 to 2 - 6 to 4 | -1.36 | 0.56 | -2.41 | 0.016 | 0.077 | n.s. |
| 5 to 3 - 6 to 4 | -0.44 | 0.56 | -0.78 | 0.436 | 0.436 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.53, *p* = 0.002, η²_G = 0.107
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 3.30 | 23 | = 0.019 | 0.92 [0.21, 1.14] | large | * |
| 3 to 1 vs 5 to 3 | 2.71 | 23 | = 0.025 | 0.59 [0.10, 1.01] | medium | * |
| 3 to 1 vs 6 to 4 | 1.41 | 23 | = 0.205 | 0.32 [-0.14, 0.72] | small | n.s. |
| 4 to 2 vs 5 to 3 | -1.49 | 23 | = 0.205 | -0.41 [-0.74, 0.13] | small | n.s. |
| 4 to 2 vs 6 to 4 | -2.87 | 23 | = 0.025 | -0.56 [-1.04, -0.13] | medium | * |
| 5 to 3 vs 6 to 4 | -1.01 | 23 | = 0.323 | -0.21 [-0.63, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 943.11, BIC = 961.06
- **4 to 2 vs 3 to 1**: *β* = -6.48, *SE* = 8.137, *z* = -0.796, *p* = 0.426
- **5 to 3 vs 3 to 1**: *β* = -18.69, *SE* = 7.958, *z* = -2.348, *p* = 0.019
- **6 to 4 vs 3 to 1**: *β* = -0.27, *SE* = 8.075, *z* = -0.034, *p* = 0.973
- **SNR**: *β* = -0.11, *SE* = 0.727, *z* = -0.145, *p* = 0.884

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 6.48 | 8.14 | 0.80 | 0.426 | 0.811 | n.s. |
| 3 to 1 - 5 to 3 | 18.69 | 7.96 | 2.35 | 0.019 | 0.108 | n.s. |
| 3 to 1 - 6 to 4 | 0.27 | 8.07 | 0.03 | 0.973 | 0.973 | n.s. |
| 4 to 2 - 5 to 3 | 12.21 | 7.90 | 1.55 | 0.122 | 0.406 | n.s. |
| 4 to 2 - 6 to 4 | -6.20 | 7.86 | -0.79 | 0.430 | 0.811 | n.s. |
| 5 to 3 - 6 to 4 | -18.41 | 7.87 | -2.34 | 0.019 | 0.108 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.36, *p* = 0.079, η²_G = 0.053
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.66 | 23 | = 0.622 | 0.18 [-0.29, 0.56] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 2.74 | 23 | = 0.054 | 0.66 [0.11, 1.01] | medium | n.s. |
| 3 to 1 vs 6 to 4 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | 1.82 | 23 | = 0.165 | 0.39 [-0.07, 0.81] | small | n.s. |
| 4 to 2 vs 6 to 4 | -0.68 | 23 | = 0.622 | -0.17 [-0.56, 0.29] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | -2.54 | 23 | = 0.054 | -0.60 [-0.97, -0.07] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 502.77, BIC = 520.72
- **4 to 2 vs 3 to 1**: *β* = -0.39, *SE* = 0.754, *z* = -0.522, *p* = 0.602
- **5 to 3 vs 3 to 1**: *β* = -0.24, *SE* = 0.736, *z* = -0.325, *p* = 0.745
- **6 to 4 vs 3 to 1**: *β* = -0.18, *SE* = 0.748, *z* = -0.241, *p* = 0.810
- **SNR**: *β* = 0.14, *SE* = 0.071, *z* = 1.970, *p* = 0.049

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 0.39 | 0.75 | 0.52 | 0.602 | 0.996 | n.s. |
| 3 to 1 - 5 to 3 | 0.24 | 0.74 | 0.32 | 0.745 | 0.999 | n.s. |
| 3 to 1 - 6 to 4 | 0.18 | 0.75 | 0.24 | 0.810 | 0.999 | n.s. |
| 4 to 2 - 5 to 3 | -0.15 | 0.73 | -0.21 | 0.832 | 0.999 | n.s. |
| 4 to 2 - 6 to 4 | -0.21 | 0.73 | -0.29 | 0.768 | 0.999 | n.s. |
| 5 to 3 - 6 to 4 | -0.06 | 0.73 | -0.08 | 0.936 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.40, *p* = 0.752, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.34 | 23 | = 0.926 | 0.20 [-0.16, 0.70] | small | n.s. |
| 3 to 1 vs 5 to 3 | 0.71 | 23 | = 0.926 | 0.14 [-0.28, 0.57] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 0.64 | 23 | = 0.926 | 0.15 [-0.29, 0.55] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | -0.46 | 23 | = 0.926 | -0.08 [-0.52, 0.33] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -0.29 | 23 | = 0.926 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.07 | 23 | = 0.942 | 0.02 [-0.41, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.019) (no significant pairwise comparisons)
**N1 latency:** Marginal trend toward condition differences (*p* = 0.064)
**N1 amplitude:** Significant main effect of condition (*p* = 0.013). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 0.67)
**P1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 0.92)
  - 3 to 1 showed greater amplitude than 5 to 3 (*d* = 0.59)
  - 4 to 2 showed smaller amplitude than 6 to 4 (*d* = -0.56)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.079)

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
