# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:21:23

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 4

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 14 | -2.53 µV | 2.33 | 0.62 | [-8.11, -0.19] |
| 1 to 2 | 22 | -3.43 µV | 1.73 | 0.37 | [-6.54, -0.48] |
| 1 to 3 | 24 | -3.97 µV | 1.94 | 0.40 | [-8.85, -0.77] |
| 1 to 4 | 22 | -4.57 µV | 2.79 | 0.59 | [-10.64, -0.11] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 14 | 179.65 ms | 15.68 | 4.19 | [155.91, 205.68] |
| 1 to 2 | 22 | 174.61 ms | 12.58 | 2.68 | [155.23, 204.22] |
| 1 to 3 | 24 | 175.58 ms | 10.13 | 2.07 | [155.17, 201.36] |
| 1 to 4 | 22 | 174.18 ms | 10.02 | 2.14 | [158.11, 198.25] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 17 | 2.08 µV | 2.18 | 0.53 | [0.00, 8.50] |
| 1 to 2 | 13 | 1.11 µV | 0.84 | 0.23 | [0.00, 2.53] |
| 1 to 3 | 12 | 1.65 µV | 1.36 | 0.39 | [0.19, 4.96] |
| 1 to 4 | 12 | 2.06 µV | 1.35 | 0.39 | [0.16, 4.44] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 17 | 109.57 ms | 10.32 | 2.50 | [92.30, 123.78] |
| 1 to 2 | 13 | 97.87 ms | 9.01 | 2.50 | [82.03, 110.25] |
| 1 to 3 | 12 | 100.66 ms | 10.84 | 3.13 | [81.30, 113.41] |
| 1 to 4 | 12 | 99.88 ms | 10.69 | 3.09 | [81.41, 117.45] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 11 | 1.56 µV | 1.32 | 0.40 | [0.17, 3.65] |
| 1 to 2 | 15 | 3.58 µV | 2.66 | 0.69 | [0.30, 10.14] |
| 1 to 3 | 20 | 3.99 µV | 3.20 | 0.72 | [0.36, 12.18] |
| 1 to 4 | 20 | 3.76 µV | 2.77 | 0.62 | [0.38, 10.25] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 11 | 437.39 ms | 47.60 | 14.35 | [366.48, 526.82] |
| 1 to 2 | 15 | 448.52 ms | 34.08 | 8.80 | [383.98, 498.06] |
| 1 to 3 | 20 | 451.69 ms | 25.65 | 5.74 | [393.40, 485.95] |
| 1 to 4 | 20 | 448.95 ms | 31.57 | 7.06 | [389.96, 508.75] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 313.22, BIC = 330.07
- **1 to 2 vs 1 to 1**: *β* = -0.69, *SE* = 0.467, *z* = -1.472, *p* = 0.141
- **1 to 3 vs 1 to 1**: *β* = -0.89, *SE* = 0.462, *z* = -1.915, *p* = 0.056
- **1 to 4 vs 1 to 1**: *β* = -1.50, *SE* = 0.469, *z* = -3.203, *p* = 0.001
- **SNR**: *β* = -0.46, *SE* = 0.056, *z* = -8.190, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 0.69 | 0.47 | 1.47 | 0.141 | 0.314 | n.s. |
| 1 to 1 - 1 to 3 | 0.89 | 0.46 | 1.91 | 0.056 | 0.204 | n.s. |
| 1 to 1 - 1 to 4 | 1.50 | 0.47 | 3.20 | 0.001 | 0.008 | ** |
| 1 to 2 - 1 to 3 | 0.20 | 0.40 | 0.50 | 0.618 | 0.618 | n.s. |
| 1 to 2 - 1 to 4 | 0.82 | 0.41 | 2.01 | 0.044 | 0.203 | n.s. |
| 1 to 3 - 1 to 4 | 0.62 | 0.39 | 1.56 | 0.118 | 0.314 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.49, *p* = 0.236, η²_G = 0.060
- Greenhouse-Geisser corrected: *p* = 0.250 (ε = 0.553)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 0.97 | 11 | = 0.525 | 0.36 [-0.34, 0.89] | small | n.s. |
| 1 to 1 vs 1 to 3 | 1.42 | 11 | = 0.432 | 0.61 [-0.13, 1.09] | medium | n.s. |
| 1 to 1 vs 1 to 4 | 1.31 | 11 | = 0.432 | 0.51 [-0.17, 1.11] | medium | n.s. |
| 1 to 2 vs 1 to 3 | 1.47 | 11 | = 0.432 | 0.31 [-0.17, 0.73] | small | n.s. |
| 1 to 2 vs 1 to 4 | 0.81 | 11 | = 0.525 | 0.20 [-0.13, 0.84] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.45 | 11 | = 0.662 | -0.08 [-0.30, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 601.67, BIC = 618.52
- **1 to 2 vs 1 to 1**: *β* = -4.51, *SE* = 2.257, *z* = -2.000, *p* = 0.045
- **1 to 3 vs 1 to 1**: *β* = -3.31, *SE* = 2.237, *z* = -1.480, *p* = 0.139
- **1 to 4 vs 1 to 1**: *β* = -3.16, *SE* = 2.265, *z* = -1.395, *p* = 0.163
- **SNR**: *β* = 0.24, *SE* = 0.306, *z* = 0.790, *p* = 0.430

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 4.51 | 2.26 | 2.00 | 0.045 | 0.244 | n.s. |
| 1 to 1 - 1 to 3 | 3.31 | 2.24 | 1.48 | 0.139 | 0.526 | n.s. |
| 1 to 1 - 1 to 4 | 3.16 | 2.27 | 1.40 | 0.163 | 0.526 | n.s. |
| 1 to 2 - 1 to 3 | -1.20 | 1.89 | -0.64 | 0.524 | 0.864 | n.s. |
| 1 to 2 - 1 to 4 | -1.35 | 1.94 | -0.70 | 0.485 | 0.864 | n.s. |
| 1 to 3 - 1 to 4 | -0.15 | 1.88 | -0.08 | 0.937 | 0.937 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.79, *p* = 0.168, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.90 | 11 | = 0.282 | 0.38 [-0.12, 1.17] | small | n.s. |
| 1 to 1 vs 1 to 3 | 1.83 | 11 | = 0.282 | 0.48 [-0.22, 0.97] | small | n.s. |
| 1 to 1 vs 1 to 4 | 1.16 | 11 | = 0.427 | 0.26 [-0.45, 0.77] | small | n.s. |
| 1 to 2 vs 1 to 3 | 0.13 | 11 | = 0.902 | 0.03 [-0.55, 0.34] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.91 | 11 | = 0.461 | -0.15 [-0.66, 0.28] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.13 | 11 | = 0.427 | -0.21 [-0.51, 0.38] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 157.48, BIC = 171.40
- **1 to 2 vs 1 to 1**: *β* = -0.78, *SE* = 0.332, *z* = -2.335, *p* = 0.020
- **1 to 3 vs 1 to 1**: *β* = -0.26, *SE* = 0.338, *z* = -0.776, *p* = 0.438
- **1 to 4 vs 1 to 1**: *β* = -0.31, *SE* = 0.338, *z* = -0.922, *p* = 0.357
- **SNR**: *β* = 0.78, *SE* = 0.083, *z* = 9.424, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 0.78 | 0.33 | 2.34 | 0.020 | 0.112 | n.s. |
| 1 to 1 - 1 to 3 | 0.26 | 0.34 | 0.78 | 0.438 | 0.734 | n.s. |
| 1 to 1 - 1 to 4 | 0.31 | 0.34 | 0.92 | 0.357 | 0.734 | n.s. |
| 1 to 2 - 1 to 3 | -0.51 | 0.36 | -1.43 | 0.152 | 0.562 | n.s. |
| 1 to 2 - 1 to 4 | -0.46 | 0.36 | -1.28 | 0.200 | 0.591 | n.s. |
| 1 to 3 - 1 to 4 | 0.05 | 0.37 | 0.13 | 0.893 | 0.893 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.48, *p* = 0.008, η²_G = 0.449
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 2.99 | 3 | = 0.158 | 1.76 [-0.23, 1.44] | large | n.s. |
| 1 to 1 vs 1 to 3 | 3.52 | 3 | = 0.158 | 1.65 [-0.43, 1.04] | large | n.s. |
| 1 to 1 vs 1 to 4 | 2.32 | 3 | = 0.158 | 0.95 [-0.19, 1.35] | large | n.s. |
| 1 to 2 vs 1 to 3 | -0.52 | 3 | = 0.639 | -0.23 [-1.12, 0.58] | small | n.s. |
| 1 to 2 vs 1 to 4 | -2.29 | 3 | = 0.158 | -0.84 [-2.70, -0.27] | large | n.s. |
| 1 to 3 vs 1 to 4 | -1.53 | 3 | = 0.269 | -0.70 [-1.24, 0.88] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 411.29, BIC = 425.22
- **1 to 2 vs 1 to 1**: *β* = -11.32, *SE* = 3.547, *z* = -3.192, *p* = 0.001
- **1 to 3 vs 1 to 1**: *β* = -8.58, *SE* = 3.620, *z* = -2.370, *p* = 0.018
- **1 to 4 vs 1 to 1**: *β* = -10.21, *SE* = 3.626, *z* = -2.817, *p* = 0.005
- **SNR**: *β* = 1.45, *SE* = 0.964, *z* = 1.498, *p* = 0.134

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 11.32 | 3.55 | 3.19 | 0.001 | 0.008 | ** |
| 1 to 1 - 1 to 3 | 8.58 | 3.62 | 2.37 | 0.018 | 0.069 | n.s. |
| 1 to 1 - 1 to 4 | 10.21 | 3.63 | 2.82 | 0.005 | 0.024 | * |
| 1 to 2 - 1 to 3 | -2.74 | 3.86 | -0.71 | 0.477 | 0.857 | n.s. |
| 1 to 2 - 1 to 4 | -1.11 | 3.89 | -0.28 | 0.776 | 0.897 | n.s. |
| 1 to 3 - 1 to 4 | 1.63 | 3.94 | 0.41 | 0.679 | 0.897 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.362, η²_G = 0.197
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 2.89 | 3 | = 0.378 | 1.03 [-0.15, 1.57] | large | n.s. |
| 1 to 1 vs 1 to 3 | 0.38 | 3 | = 0.731 | 0.28 [-0.18, 1.38] | small | n.s. |
| 1 to 1 vs 1 to 4 | 1.91 | 3 | = 0.456 | 0.99 [-0.07, 1.54] | large | n.s. |
| 1 to 2 vs 1 to 3 | -0.76 | 3 | = 0.731 | -0.62 [-1.12, 0.58] | medium | n.s. |
| 1 to 2 vs 1 to 4 | 0.56 | 3 | = 0.731 | 0.25 [-1.22, 0.50] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.91 | 3 | = 0.731 | 0.72 [-0.57, 1.68] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 262.37, BIC = 277.69
- **1 to 2 vs 1 to 1**: *β* = 0.60, *SE* = 0.579, *z* = 1.032, *p* = 0.302
- **1 to 3 vs 1 to 1**: *β* = 0.81, *SE* = 0.588, *z* = 1.375, *p* = 0.169
- **1 to 4 vs 1 to 1**: *β* = 0.65, *SE* = 0.581, *z* = 1.121, *p* = 0.262
- **SNR**: *β* = 0.67, *SE* = 0.079, *z* = 8.386, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | -0.60 | 0.58 | -1.03 | 0.302 | 0.781 | n.s. |
| 1 to 1 - 1 to 3 | -0.81 | 0.59 | -1.38 | 0.169 | 0.671 | n.s. |
| 1 to 1 - 1 to 4 | -0.65 | 0.58 | -1.12 | 0.262 | 0.781 | n.s. |
| 1 to 2 - 1 to 3 | -0.21 | 0.47 | -0.45 | 0.653 | 0.958 | n.s. |
| 1 to 2 - 1 to 4 | -0.05 | 0.46 | -0.12 | 0.907 | 0.958 | n.s. |
| 1 to 3 - 1 to 4 | 0.16 | 0.42 | 0.37 | 0.708 | 0.958 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.87, *p* = 0.004, η²_G = 0.243
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -2.23 | 8 | = 0.112 | -1.02 [-1.61, 0.12] | large | n.s. |
| 1 to 1 vs 1 to 3 | -2.72 | 8 | = 0.079 | -1.42 [-1.64, -0.07] | large | n.s. |
| 1 to 1 vs 1 to 4 | -3.00 | 8 | = 0.079 | -1.48 [-1.89, -0.21] | large | n.s. |
| 1 to 2 vs 1 to 3 | -1.65 | 8 | = 0.164 | -0.51 [-1.09, 0.13] | medium | n.s. |
| 1 to 2 vs 1 to 4 | -1.71 | 8 | = 0.164 | -0.44 [-0.92, 0.22] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.62 | 8 | = 0.555 | 0.10 [-0.32, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 660.30, BIC = 675.63
- **1 to 2 vs 1 to 1**: *β* = 10.42, *SE* = 12.828, *z* = 0.812, *p* = 0.417
- **1 to 3 vs 1 to 1**: *β* = 12.99, *SE* = 12.578, *z* = 1.033, *p* = 0.302
- **1 to 4 vs 1 to 1**: *β* = 10.58, *SE* = 12.495, *z* = 0.847, *p* = 0.397
- **SNR**: *β* = 0.32, *SE* = 1.582, *z* = 0.205, *p* = 0.838

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | -10.42 | 12.83 | -0.81 | 0.417 | 0.920 | n.s. |
| 1 to 1 - 1 to 3 | -12.99 | 12.58 | -1.03 | 0.302 | 0.884 | n.s. |
| 1 to 1 - 1 to 4 | -10.58 | 12.49 | -0.85 | 0.397 | 0.920 | n.s. |
| 1 to 2 - 1 to 3 | -2.57 | 10.53 | -0.24 | 0.807 | 0.992 | n.s. |
| 1 to 2 - 1 to 4 | -0.16 | 10.46 | -0.02 | 0.988 | 0.992 | n.s. |
| 1 to 3 - 1 to 4 | 2.41 | 9.60 | 0.25 | 0.802 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.658, η²_G = 0.050
- Greenhouse-Geisser corrected: *p* = 0.599 (ε = 0.699)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -0.38 | 8 | = 0.735 | -0.18 [-0.90, 0.65] | negligible | n.s. |
| 1 to 1 vs 1 to 3 | -1.29 | 8 | = 0.735 | -0.56 [-0.97, 0.40] | medium | n.s. |
| 1 to 1 vs 1 to 4 | -0.78 | 8 | = 0.735 | -0.37 [-0.99, 0.39] | small | n.s. |
| 1 to 2 vs 1 to 3 | -0.72 | 8 | = 0.735 | -0.41 [-0.76, 0.40] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.35 | 8 | = 0.735 | -0.20 [-0.49, 0.62] | small | n.s. |
| 1 to 3 vs 1 to 4 | 1.11 | 8 | = 0.735 | 0.24 [-0.51, 0.45] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.008) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.004) (no significant pairwise comparisons)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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
