# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:18:25

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
| 4 to 1 | 24 | 106.83 ms | 13.21 | 2.70 | [88.00, 120.00] |
| 5 to 2 | 24 | 102.67 ms | 10.79 | 2.20 | [88.00, 120.00] |
| 6 to 3 | 24 | 104.17 ms | 11.22 | 2.29 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | -2.66 µV | 2.81 | 0.57 | [-8.54, 3.36] |
| 5 to 2 | 24 | -2.31 µV | 2.46 | 0.50 | [-6.65, 2.53] |
| 6 to 3 | 24 | -2.01 µV | 1.61 | 0.33 | [-5.28, 1.13] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 187.67 ms | 16.51 | 3.37 | [148.00, 220.00] |
| 5 to 2 | 24 | 174.50 ms | 19.12 | 3.90 | [148.00, 220.00] |
| 6 to 3 | 24 | 176.50 ms | 16.61 | 3.39 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | -3.73 µV | 2.13 | 0.44 | [-9.44, -0.12] |
| 5 to 2 | 24 | -7.01 µV | 3.01 | 0.61 | [-11.82, -1.41] |
| 6 to 3 | 24 | -6.55 µV | 2.33 | 0.48 | [-11.28, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 115.67 ms | 11.97 | 2.44 | [96.00, 128.00] |
| 5 to 2 | 24 | 110.83 ms | 11.16 | 2.28 | [96.00, 128.00] |
| 6 to 3 | 24 | 110.00 ms | 12.26 | 2.50 | [96.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 3.73 µV | 3.78 | 0.77 | [-4.26, 13.38] |
| 5 to 2 | 24 | 2.02 µV | 2.25 | 0.46 | [-1.58, 6.20] |
| 6 to 3 | 24 | 2.01 µV | 2.29 | 0.47 | [-1.01, 7.81] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 473.33 ms | 47.95 | 9.79 | [384.00, 528.00] |
| 5 to 2 | 24 | 469.67 ms | 43.27 | 8.83 | [392.00, 528.00] |
| 6 to 3 | 24 | 461.00 ms | 33.53 | 6.85 | [396.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 5.80 µV | 3.49 | 0.71 | [0.57, 12.03] |
| 5 to 2 | 24 | 4.54 µV | 3.60 | 0.73 | [-2.27, 13.53] |
| 6 to 3 | 24 | 5.34 µV | 4.25 | 0.87 | [-2.53, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 568.17, BIC = 581.83
- **5 to 2 vs 4 to 1**: *β* = -4.19, *SE* = 3.217, *z* = -1.301, *p* = 0.193
- **6 to 3 vs 4 to 1**: *β* = -2.61, *SE* = 3.246, *z* = -0.805, *p* = 0.421
- **SNR**: *β* = 0.13, *SE* = 1.141, *z* = 0.113, *p* = 0.910

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 4.19 | 3.22 | 1.30 | 0.193 | 0.475 | n.s. |
| 4 to 1 - 6 to 3 | 2.61 | 3.25 | 0.81 | 0.421 | 0.664 | n.s. |
| 5 to 2 - 6 to 3 | -1.57 | 3.28 | -0.48 | 0.631 | 0.664 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.83, *p* = 0.443, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.36 | 23 | = 0.559 | 0.35 [-0.15, 0.71] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.77 | 23 | = 0.656 | 0.22 [-0.27, 0.58] | small | n.s. |
| 5 to 2 vs 6 to 3 | -0.45 | 23 | = 0.656 | -0.14 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 320.47, BIC = 334.13
- **5 to 2 vs 4 to 1**: *β* = 0.45, *SE* = 0.515, *z* = 0.869, *p* = 0.385
- **6 to 3 vs 4 to 1**: *β* = 0.39, *SE* = 0.521, *z* = 0.740, *p* = 0.459
- **SNR**: *β* = -0.65, *SE* = 0.201, *z* = -3.250, *p* = 0.001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | -0.45 | 0.51 | -0.87 | 0.385 | 0.768 | n.s. |
| 4 to 1 - 6 to 3 | -0.39 | 0.52 | -0.74 | 0.459 | 0.768 | n.s. |
| 5 to 2 - 6 to 3 | 0.06 | 0.53 | 0.12 | 0.906 | 0.906 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.66, *p* = 0.521, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | -0.50 | 23 | = 0.620 | -0.13 [-0.53, 0.32] | negligible | n.s. |
| 4 to 1 vs 6 to 3 | -1.42 | 23 | = 0.509 | -0.29 [-0.72, 0.14] | small | n.s. |
| 5 to 2 vs 6 to 3 | -0.58 | 23 | = 0.620 | -0.15 [-0.54, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 610.38, BIC = 624.04
- **5 to 2 vs 4 to 1**: *β* = -13.36, *SE* = 4.043, *z* = -3.304, *p* = 0.001
- **6 to 3 vs 4 to 1**: *β* = -11.34, *SE* = 3.982, *z* = -2.849, *p* = 0.004
- **SNR**: *β* = 0.07, *SE* = 0.693, *z* = 0.102, *p* = 0.919

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 13.36 | 4.04 | 3.30 | < .001 | 0.003 | ** |
| 4 to 1 - 6 to 3 | 11.34 | 3.98 | 2.85 | 0.004 | 0.009 | ** |
| 5 to 2 - 6 to 3 | -2.01 | 3.58 | -0.56 | 0.574 | 0.574 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.50, *p* = 0.002, η²_G = 0.103
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 3.17 | 23 | = 0.006 | 0.74 [0.18, 1.11] | medium | ** |
| 4 to 1 vs 6 to 3 | 3.24 | 23 | = 0.006 | 0.67 [0.20, 1.13] | medium | ** |
| 5 to 2 vs 6 to 3 | -0.60 | 23 | = 0.555 | -0.11 [-0.55, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 314.86, BIC = 328.52
- **5 to 2 vs 4 to 1**: *β* = -2.37, *SE* = 0.511, *z* = -4.636, *p* < .001
- **6 to 3 vs 4 to 1**: *β* = -1.98, *SE* = 0.503, *z* = -3.931, *p* < .001
- **SNR**: *β* = -0.34, *SE* = 0.088, *z* = -3.830, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 2.37 | 0.51 | 4.64 | < .001 | < .001 | *** |
| 4 to 1 - 6 to 3 | 1.98 | 0.50 | 3.93 | < .001 | < .001 | *** |
| 5 to 2 - 6 to 3 | -0.39 | 0.45 | -0.86 | 0.389 | 0.389 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 24.66, *p* < .001, η²_G = 0.257
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 6.07 | 23 | < .001 | 1.26 [0.68, 1.80] | large | *** |
| 4 to 1 vs 6 to 3 | 5.05 | 23 | < .001 | 1.27 [0.51, 1.55] | large | *** |
| 5 to 2 vs 6 to 3 | -1.13 | 23 | = 0.272 | -0.17 [-0.66, 0.20] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.65, BIC = 564.31
- **5 to 2 vs 4 to 1**: *β* = -3.76, *SE* = 2.402, *z* = -1.566, *p* = 0.117
- **6 to 3 vs 4 to 1**: *β* = -4.36, *SE* = 2.447, *z* = -1.783, *p* = 0.075
- **SNR**: *β* = 0.97, *SE* = 0.613, *z* = 1.584, *p* = 0.113

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 3.76 | 2.40 | 1.57 | 0.117 | 0.221 | n.s. |
| 4 to 1 - 6 to 3 | 4.36 | 2.45 | 1.78 | 0.075 | 0.207 | n.s. |
| 5 to 2 - 6 to 3 | 0.60 | 2.31 | 0.26 | 0.794 | 0.794 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.14, *p* = 0.053, η²_G = 0.045
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.81 | 23 | = 0.030 | 0.42 [0.12, 1.03] | small | * |
| 4 to 1 vs 6 to 3 | 1.96 | 23 | = 0.094 | 0.47 [-0.04, 0.84] | small | n.s. |
| 5 to 2 vs 6 to 3 | 0.33 | 23 | = 0.748 | 0.07 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 343.32, BIC = 356.98
- **5 to 2 vs 4 to 1**: *β* = -1.04, *SE* = 0.619, *z* = -1.687, *p* = 0.092
- **6 to 3 vs 4 to 1**: *β* = -0.91, *SE* = 0.629, *z* = -1.452, *p* = 0.146
- **SNR**: *β* = 0.60, *SE* = 0.150, *z* = 4.004, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.04 | 0.62 | 1.69 | 0.092 | 0.251 | n.s. |
| 4 to 1 - 6 to 3 | 0.91 | 0.63 | 1.45 | 0.146 | 0.271 | n.s. |
| 5 to 2 - 6 to 3 | -0.13 | 0.60 | -0.22 | 0.828 | 0.828 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.26, *p* = 0.020, η²_G = 0.077
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.16 | 23 | = 0.063 | 0.55 [-0.00, 0.88] | medium | n.s. |
| 4 to 1 vs 6 to 3 | 2.62 | 23 | = 0.045 | 0.55 [0.08, 0.99] | medium | * |
| 5 to 2 vs 6 to 3 | 0.02 | 23 | = 0.982 | 0.01 [-0.42, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 745.30, BIC = 758.96
- **5 to 2 vs 4 to 1**: *β* = -3.73, *SE* = 9.920, *z* = -0.376, *p* = 0.707
- **6 to 3 vs 4 to 1**: *β* = -12.42, *SE* = 9.974, *z* = -1.245, *p* = 0.213
- **SNR**: *β* = -0.06, *SE* = 1.063, *z* = -0.058, *p* = 0.953

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 3.73 | 9.92 | 0.38 | 0.707 | 0.707 | n.s. |
| 4 to 1 - 6 to 3 | 12.42 | 9.97 | 1.25 | 0.213 | 0.513 | n.s. |
| 5 to 2 - 6 to 3 | 8.69 | 9.87 | 0.88 | 0.379 | 0.614 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.79, *p* = 0.460, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 0.35 | 23 | = 0.726 | 0.08 [-0.35, 0.50] | negligible | n.s. |
| 4 to 1 vs 6 to 3 | 1.17 | 23 | = 0.541 | 0.30 [-0.19, 0.67] | small | n.s. |
| 5 to 2 vs 6 to 3 | 0.93 | 23 | = 0.541 | 0.22 [-0.24, 0.62] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 369.32, BIC = 382.98
- **5 to 2 vs 4 to 1**: *β* = -1.01, *SE* = 0.661, *z* = -1.523, *p* = 0.128
- **6 to 3 vs 4 to 1**: *β* = -0.10, *SE* = 0.665, *z* = -0.158, *p* = 0.875
- **SNR**: *β* = 0.26, *SE* = 0.081, *z* = 3.226, *p* = 0.001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.01 | 0.66 | 1.52 | 0.128 | 0.337 | n.s. |
| 4 to 1 - 6 to 3 | 0.10 | 0.67 | 0.16 | 0.875 | 0.875 | n.s. |
| 5 to 2 - 6 to 3 | -0.90 | 0.66 | -1.37 | 0.170 | 0.337 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.72, *p* = 0.191, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.04 | 23 | = 0.158 | 0.36 [-0.02, 0.86] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.60 | 23 | = 0.555 | 0.12 [-0.30, 0.55] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -1.20 | 23 | = 0.366 | -0.20 [-0.67, 0.18] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 5 to 2 (*d* = 0.74)
  - 4 to 1 showed greater latency than 6 to 3 (*d* = 0.67)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 1.26)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.27)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.053)
**P1 amplitude:** Significant main effect of condition (*p* = 0.020). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 0.55)

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
