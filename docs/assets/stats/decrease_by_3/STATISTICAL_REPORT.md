# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:17:57

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
| 4 to 1 | 24 | 107.33 ms | 12.24 | 2.50 | [92.00, 120.00] |
| 5 to 2 | 24 | 103.17 ms | 10.15 | 2.07 | [92.00, 120.00] |
| 6 to 3 | 24 | 105.33 ms | 10.53 | 2.15 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | -2.65 µV | 2.68 | 0.55 | [-8.54, 2.69] |
| 5 to 2 | 24 | -2.14 µV | 2.45 | 0.50 | [-6.23, 2.53] |
| 6 to 3 | 24 | -1.83 µV | 1.76 | 0.36 | [-6.41, 1.13] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 185.50 ms | 15.19 | 3.10 | [148.00, 220.00] |
| 5 to 2 | 24 | 174.50 ms | 18.42 | 3.76 | [148.00, 220.00] |
| 6 to 3 | 24 | 176.17 ms | 17.15 | 3.50 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | -3.57 µV | 1.96 | 0.40 | [-8.09, 0.13] |
| 5 to 2 | 24 | -6.58 µV | 3.05 | 0.62 | [-11.82, -1.41] |
| 6 to 3 | 24 | -6.45 µV | 2.18 | 0.44 | [-10.34, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 117.00 ms | 11.45 | 2.34 | [96.00, 128.00] |
| 5 to 2 | 24 | 111.17 ms | 10.55 | 2.15 | [96.00, 128.00] |
| 6 to 3 | 24 | 111.00 ms | 12.22 | 2.49 | [96.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 3.73 µV | 3.46 | 0.71 | [-1.66, 13.38] |
| 5 to 2 | 24 | 2.08 µV | 2.22 | 0.45 | [-1.41, 6.20] |
| 6 to 3 | 24 | 2.04 µV | 2.23 | 0.46 | [-1.00, 8.17] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 467.33 ms | 47.19 | 9.63 | [384.00, 528.00] |
| 5 to 2 | 24 | 471.00 ms | 40.23 | 8.21 | [392.00, 528.00] |
| 6 to 3 | 24 | 462.50 ms | 35.05 | 7.15 | [396.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 5.30 µV | 3.45 | 0.70 | [-1.20, 12.03] |
| 5 to 2 | 24 | 4.53 µV | 3.59 | 0.73 | [-2.27, 13.53] |
| 6 to 3 | 24 | 5.17 µV | 4.22 | 0.86 | [-2.21, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 557.50, BIC = 571.16
- **5 to 2 vs 4 to 1**: *β* = -4.10, *SE* = 2.912, *z* = -1.409, *p* = 0.159
- **6 to 3 vs 4 to 1**: *β* = -2.23, *SE* = 2.946, *z* = -0.757, *p* = 0.449
- **SNR**: *β* = -0.50, *SE* = 1.026, *z* = -0.490, *p* = 0.624

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 4.10 | 2.91 | 1.41 | 0.159 | 0.405 | n.s. |
| 4 to 1 - 6 to 3 | 2.23 | 2.95 | 0.76 | 0.449 | 0.696 | n.s. |
| 5 to 2 - 6 to 3 | -1.87 | 2.97 | -0.63 | 0.529 | 0.696 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.385, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.55 | 23 | = 0.404 | 0.37 [-0.12, 0.75] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.59 | 23 | = 0.563 | 0.18 [-0.30, 0.54] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -0.77 | 23 | = 0.563 | -0.21 [-0.58, 0.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 314.22, BIC = 327.88
- **5 to 2 vs 4 to 1**: *β* = 0.58, *SE* = 0.478, *z* = 1.217, *p* = 0.224
- **6 to 3 vs 4 to 1**: *β* = 0.54, *SE* = 0.485, *z* = 1.119, *p* = 0.263
- **SNR**: *β* = -0.60, *SE* = 0.186, *z* = -3.218, *p* = 0.001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | -0.58 | 0.48 | -1.22 | 0.224 | 0.532 | n.s. |
| 4 to 1 - 6 to 3 | -0.54 | 0.48 | -1.12 | 0.263 | 0.532 | n.s. |
| 5 to 2 - 6 to 3 | 0.04 | 0.49 | 0.08 | 0.936 | 0.936 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.289, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | -0.84 | 23 | = 0.563 | -0.20 [-0.60, 0.25] | negligible | n.s. |
| 4 to 1 vs 6 to 3 | -2.06 | 23 | = 0.153 | -0.36 [-0.86, 0.02] | small | n.s. |
| 5 to 2 vs 6 to 3 | -0.59 | 23 | = 0.563 | -0.15 [-0.54, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 603.69, BIC = 617.35
- **5 to 2 vs 4 to 1**: *β* = -11.52, *SE* = 3.623, *z* = -3.181, *p* = 0.001
- **6 to 3 vs 4 to 1**: *β* = -9.87, *SE* = 3.631, *z* = -2.717, *p* = 0.007
- **SNR**: *β* = 0.24, *SE* = 0.639, *z* = 0.379, *p* = 0.705

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 11.52 | 3.62 | 3.18 | 0.001 | 0.004 | ** |
| 4 to 1 - 6 to 3 | 9.87 | 3.63 | 2.72 | 0.007 | 0.013 | * |
| 5 to 2 - 6 to 3 | -1.66 | 3.35 | -0.50 | 0.620 | 0.620 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.95, *p* = 0.005, η²_G = 0.078
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 3.08 | 23 | = 0.012 | 0.65 [0.17, 1.09] | medium | * |
| 4 to 1 vs 6 to 3 | 2.91 | 23 | = 0.012 | 0.58 [0.14, 1.05] | medium | * |
| 5 to 2 vs 6 to 3 | -0.47 | 23 | = 0.640 | -0.09 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 305.86, BIC = 319.52
- **5 to 2 vs 4 to 1**: *β* = -2.23, *SE* = 0.454, *z* = -4.917, *p* < .001
- **6 to 3 vs 4 to 1**: *β* = -2.08, *SE* = 0.455, *z* = -4.577, *p* < .001
- **SNR**: *β* = -0.36, *SE* = 0.080, *z* = -4.548, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 2.23 | 0.45 | 4.92 | < .001 | < .001 | *** |
| 4 to 1 - 6 to 3 | 2.08 | 0.45 | 4.58 | < .001 | < .001 | *** |
| 5 to 2 - 6 to 3 | -0.15 | 0.42 | -0.36 | 0.721 | 0.721 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 24.04, *p* < .001, η²_G = 0.252
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 5.81 | 23 | < .001 | 1.17 [0.64, 1.74] | large | *** |
| 4 to 1 vs 6 to 3 | 5.49 | 23 | < .001 | 1.39 [0.58, 1.66] | large | *** |
| 5 to 2 vs 6 to 3 | -0.32 | 23 | = 0.749 | -0.05 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 554.97, BIC = 568.63
- **5 to 2 vs 4 to 1**: *β* = -4.72, *SE* = 2.657, *z* = -1.778, *p* = 0.075
- **6 to 3 vs 4 to 1**: *β* = -4.78, *SE* = 2.679, *z* = -1.784, *p* = 0.074
- **SNR**: *β* = 0.98, *SE* = 0.666, *z* = 1.466, *p* = 0.143

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 4.72 | 2.66 | 1.78 | 0.075 | 0.207 | n.s. |
| 4 to 1 - 6 to 3 | 4.78 | 2.68 | 1.78 | 0.074 | 0.207 | n.s. |
| 5 to 2 - 6 to 3 | 0.06 | 2.55 | 0.02 | 0.982 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.19, *p* = 0.050, η²_G = 0.059
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.84 | 23 | = 0.028 | 0.53 [0.12, 1.04] | medium | * |
| 4 to 1 vs 6 to 3 | 1.95 | 23 | = 0.096 | 0.51 [-0.04, 0.84] | medium | n.s. |
| 5 to 2 vs 6 to 3 | 0.06 | 23 | = 0.954 | 0.01 [-0.41, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 332.20, BIC = 345.86
- **5 to 2 vs 4 to 1**: *β* = -0.98, *SE* = 0.578, *z* = -1.703, *p* = 0.089
- **6 to 3 vs 4 to 1**: *β* = -0.97, *SE* = 0.583, *z* = -1.661, *p* = 0.097
- **SNR**: *β* = 0.58, *SE* = 0.139, *z* = 4.169, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.99 | 0.58 | 1.70 | 0.089 | 0.243 | n.s. |
| 4 to 1 - 6 to 3 | 0.97 | 0.58 | 1.66 | 0.097 | 0.243 | n.s. |
| 5 to 2 - 6 to 3 | -0.02 | 0.56 | -0.03 | 0.976 | 0.976 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.77, *p* = 0.013, η²_G = 0.081
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.28 | 23 | = 0.048 | 0.57 [0.02, 0.91] | medium | * |
| 4 to 1 vs 6 to 3 | 2.94 | 23 | = 0.022 | 0.58 [0.14, 1.06] | medium | * |
| 5 to 2 vs 6 to 3 | 0.09 | 23 | = 0.932 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 744.00, BIC = 757.66
- **5 to 2 vs 4 to 1**: *β* = 2.52, *SE* = 10.259, *z* = 0.246, *p* = 0.806
- **6 to 3 vs 4 to 1**: *β* = -6.22, *SE* = 10.322, *z* = -0.603, *p* = 0.547
- **SNR**: *β* = -0.69, *SE* = 0.994, *z* = -0.692, *p* = 0.489

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | -2.52 | 10.26 | -0.25 | 0.806 | 0.806 | n.s. |
| 4 to 1 - 6 to 3 | 6.22 | 10.32 | 0.60 | 0.547 | 0.794 | n.s. |
| 5 to 2 - 6 to 3 | 8.75 | 10.13 | 0.86 | 0.388 | 0.771 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.34, *p* = 0.712, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | -0.37 | 23 | = 0.717 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 4 to 1 vs 6 to 3 | 0.44 | 23 | = 0.717 | 0.12 [-0.33, 0.51] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | 0.85 | 23 | = 0.717 | 0.23 [-0.25, 0.60] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 368.43, BIC = 382.09
- **5 to 2 vs 4 to 1**: *β* = -0.50, *SE* = 0.631, *z* = -0.797, *p* = 0.426
- **6 to 3 vs 4 to 1**: *β* = 0.19, *SE* = 0.636, *z* = 0.295, *p* = 0.768
- **SNR**: *β* = 0.16, *SE* = 0.070, *z* = 2.251, *p* = 0.024

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.50 | 0.63 | 0.80 | 0.426 | 0.670 | n.s. |
| 4 to 1 - 6 to 3 | -0.19 | 0.64 | -0.30 | 0.768 | 0.768 | n.s. |
| 5 to 2 - 6 to 3 | -0.69 | 0.62 | -1.11 | 0.266 | 0.604 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.81, *p* = 0.449, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.39 | 23 | = 0.517 | 0.22 [-0.15, 0.71] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.19 | 23 | = 0.855 | 0.03 [-0.38, 0.46] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -0.96 | 23 | = 0.517 | -0.16 [-0.62, 0.23] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 5 to 2 (*d* = 0.65)
  - 4 to 1 showed greater latency than 6 to 3 (*d* = 0.58)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 1.17)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.39)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.050)
**P1 amplitude:** Significant main effect of condition (*p* = 0.013). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 0.57)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 0.58)

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
