# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:16:21

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
| Decrease by 1 | 24 | 106.83 ms | 9.76 | 1.99 | [92.00, 120.00] |
| Decrease by 2 | 24 | 108.00 ms | 10.22 | 2.09 | [92.00, 120.00] |
| Decrease by 3 | 24 | 106.83 ms | 10.38 | 2.12 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | -1.06 µV | 1.38 | 0.28 | [-4.56, 1.16] |
| Decrease by 2 | 24 | -1.50 µV | 1.26 | 0.26 | [-4.30, 2.02] |
| Decrease by 3 | 24 | -1.85 µV | 1.81 | 0.37 | [-6.39, 1.47] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 179.33 ms | 15.45 | 3.15 | [152.00, 212.00] |
| Decrease by 2 | 24 | 177.67 ms | 14.54 | 2.97 | [148.00, 212.00] |
| Decrease by 3 | 24 | 177.00 ms | 15.02 | 3.07 | [152.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | -4.90 µV | 2.05 | 0.42 | [-9.90, -1.23] |
| Decrease by 2 | 24 | -5.12 µV | 2.11 | 0.43 | [-9.59, -1.53] |
| Decrease by 3 | 24 | -5.22 µV | 1.97 | 0.40 | [-8.60, -1.48] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 113.33 ms | 9.34 | 1.91 | [100.00, 124.00] |
| Decrease by 2 | 24 | 113.00 ms | 9.08 | 1.85 | [100.00, 124.00] |
| Decrease by 3 | 24 | 112.83 ms | 9.29 | 1.90 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 1.22 µV | 1.94 | 0.40 | [-1.26, 5.67] |
| Decrease by 2 | 24 | 1.69 µV | 1.80 | 0.37 | [-2.32, 5.74] |
| Decrease by 3 | 24 | 2.11 µV | 2.15 | 0.44 | [-1.35, 8.15] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 490.83 ms | 31.59 | 6.45 | [436.00, 536.00] |
| Decrease by 2 | 24 | 473.67 ms | 31.89 | 6.51 | [432.00, 536.00] |
| Decrease by 3 | 24 | 480.83 ms | 33.05 | 6.75 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 4.12 µV | 3.07 | 0.63 | [-2.28, 9.87] |
| Decrease by 2 | 24 | 3.82 µV | 2.89 | 0.59 | [-1.38, 8.68] |
| Decrease by 3 | 24 | 4.37 µV | 3.49 | 0.71 | [-1.21, 12.38] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 525.46, BIC = 539.12
- **Decrease by 2 vs Decrease by 1**: *β* = 0.02, *SE* = 2.013, *z* = 0.012, *p* = 0.991
- **Decrease by 3 vs Decrease by 1**: *β* = -1.73, *SE* = 2.050, *z* = -0.845, *p* = 0.398
- **SNR**: *β* = 1.85, *SE* = 0.548, *z* = 3.375, *p* = 0.001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.02 | 2.01 | -0.01 | 0.991 | 0.991 | n.s. |
| Decrease by 1 - Decrease by 3 | 1.73 | 2.05 | 0.85 | 0.398 | 0.759 | n.s. |
| Decrease by 2 - Decrease by 3 | 1.76 | 1.99 | 0.88 | 0.378 | 0.759 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.18, *p* = 0.836, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.62 | 23 | = 0.982 | -0.12 [-0.55, 0.30] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.45 | 23 | = 0.982 | 0.11 [-0.33, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 255.55, BIC = 269.21
- **Decrease by 2 vs Decrease by 1**: *β* = -0.34, *SE* = 0.321, *z* = -1.069, *p* = 0.285
- **Decrease by 3 vs Decrease by 1**: *β* = -0.65, *SE* = 0.327, *z* = -1.980, *p* = 0.048
- **SNR**: *β* = -0.15, *SE* = 0.090, *z* = -1.682, *p* = 0.093

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.34 | 0.32 | 1.07 | 0.285 | 0.489 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.65 | 0.33 | 1.98 | 0.048 | 0.136 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.30 | 0.32 | 0.96 | 0.337 | 0.489 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.03, *p* = 0.058, η²_G = 0.046
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 1.58 | 23 | = 0.190 | 0.33 [-0.11, 0.76] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | 2.42 | 23 | = 0.072 | 0.49 [0.05, 0.94] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.99 | 23 | = 0.333 | 0.23 [-0.22, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 566.41, BIC = 580.07
- **Decrease by 2 vs Decrease by 1**: *β* = -1.78, *SE* = 2.330, *z* = -0.762, *p* = 0.446
- **Decrease by 3 vs Decrease by 1**: *β* = -2.48, *SE* = 2.344, *z* = -1.058, *p* = 0.290
- **SNR**: *β* = 0.10, *SE* = 0.276, *z* = 0.372, *p* = 0.710

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 1.78 | 2.33 | 0.76 | 0.446 | 0.693 | n.s. |
| Decrease by 1 - Decrease by 3 | 2.48 | 2.34 | 1.06 | 0.290 | 0.642 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.70 | 2.31 | 0.30 | 0.761 | 0.761 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.51, *p* = 0.602, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.74 | 23 | = 0.698 | 0.11 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.08 | 23 | = 0.698 | 0.15 [-0.21, 0.65] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.25 | 23 | = 0.806 | 0.05 [-0.37, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 256.61, BIC = 270.27
- **Decrease by 2 vs Decrease by 1**: *β* = -0.07, *SE* = 0.266, *z* = -0.243, *p* = 0.808
- **Decrease by 3 vs Decrease by 1**: *β* = -0.11, *SE* = 0.268, *z* = -0.413, *p* = 0.679
- **SNR**: *β* = -0.15, *SE* = 0.032, *z* = -4.602, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.06 | 0.27 | 0.24 | 0.808 | 0.967 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.11 | 0.27 | 0.41 | 0.679 | 0.967 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.05 | 0.26 | 0.17 | 0.862 | 0.967 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.56, *p* = 0.577, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.71 | 23 | = 0.729 | 0.11 [-0.28, 0.57] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.01 | 23 | = 0.729 | 0.16 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.33 | 23 | = 0.746 | 0.05 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 494.92, BIC = 508.58
- **Decrease by 2 vs Decrease by 1**: *β* = -0.48, *SE* = 1.411, *z* = -0.340, *p* = 0.734
- **Decrease by 3 vs Decrease by 1**: *β* = -0.57, *SE* = 1.406, *z* = -0.408, *p* = 0.683
- **SNR**: *β* = 0.34, *SE* = 0.330, *z* = 1.029, *p* = 0.304

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.48 | 1.41 | 0.34 | 0.734 | 0.968 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.57 | 1.41 | 0.41 | 0.683 | 0.968 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.09 | 1.41 | 0.07 | 0.947 | 0.968 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.06, *p* = 0.940, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.21 | 23 | = 0.916 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.44 | 23 | = 0.916 | 0.05 [-0.33, 0.51] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.11 | 23 | = 0.916 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 257.97, BIC = 271.63
- **Decrease by 2 vs Decrease by 1**: *β* = 0.40, *SE* = 0.270, *z* = 1.469, *p* = 0.142
- **Decrease by 3 vs Decrease by 1**: *β* = 0.85, *SE* = 0.269, *z* = 3.149, *p* = 0.002
- **SNR**: *β* = 0.18, *SE* = 0.066, *z* = 2.673, *p* = 0.008

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.40 | 0.27 | -1.47 | 0.142 | 0.180 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.85 | 0.27 | -3.15 | 0.002 | 0.005 | ** |
| Decrease by 2 - Decrease by 3 | -0.45 | 0.27 | -1.67 | 0.094 | 0.180 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.01, *p* = 0.011, η²_G = 0.034
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -1.78 | 23 | = 0.132 | -0.25 [-0.80, 0.07] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -3.42 | 23 | = 0.007 | -0.43 [-1.17, -0.23] | small | ** |
| Decrease by 2 vs Decrease by 3 | -1.32 | 23 | = 0.199 | -0.21 [-0.70, 0.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 695.82, BIC = 709.48
- **Decrease by 2 vs Decrease by 1**: *β* = -17.12, *SE* = 6.397, *z* = -2.676, *p* = 0.007
- **Decrease by 3 vs Decrease by 1**: *β* = -9.76, *SE* = 6.445, *z* = -1.514, *p* = 0.130
- **SNR**: *β* = -0.23, *SE* = 0.767, *z* = -0.304, *p* = 0.761

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 17.12 | 6.40 | 2.68 | 0.007 | 0.022 | * |
| Decrease by 1 - Decrease by 3 | 9.76 | 6.44 | 1.51 | 0.130 | 0.243 | n.s. |
| Decrease by 2 - Decrease by 3 | -7.36 | 6.43 | -1.15 | 0.252 | 0.252 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.50, *p* = 0.038, η²_G = 0.048
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 2.63 | 23 | = 0.045 | 0.54 [0.09, 0.99] | medium | * |
| Decrease by 1 vs Decrease by 3 | 1.65 | 23 | = 0.168 | 0.31 [-0.10, 0.77] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.03 | 23 | = 0.313 | -0.22 [-0.64, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 304.48, BIC = 318.14
- **Decrease by 2 vs Decrease by 1**: *β* = -0.32, *SE* = 0.330, *z* = -0.958, *p* = 0.338
- **Decrease by 3 vs Decrease by 1**: *β* = 0.17, *SE* = 0.334, *z* = 0.493, *p* = 0.622
- **SNR**: *β* = 0.08, *SE* = 0.050, *z* = 1.687, *p* = 0.092

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.32 | 0.33 | 0.96 | 0.338 | 0.562 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.16 | 0.33 | -0.49 | 0.622 | 0.622 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.48 | 0.33 | -1.45 | 0.148 | 0.382 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.271, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 1.02 | 23 | = 0.452 | 0.10 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.76 | 23 | = 0.452 | -0.08 [-0.58, 0.27] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.45 | 23 | = 0.452 | -0.17 [-0.73, 0.14] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.058)
**P1 amplitude:** Significant main effect of condition (*p* = 0.011). Post-hoc tests revealed:
  - Decrease by 1 showed smaller amplitude than Decrease by 3 (*d* = -0.43)
**P3b latency:** Significant main effect of condition (*p* = 0.038). Post-hoc tests revealed:
  - Decrease by 1 showed greater latency than Decrease by 2 (*d* = 0.54)

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
