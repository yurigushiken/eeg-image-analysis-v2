# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:23:54

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
| 1 to 3 | 24 | 102.00 ms | 8.83 | 1.80 | [92.00, 112.00] |
| 2 to 4 | 24 | 101.83 ms | 7.91 | 1.61 | [92.00, 112.00] |
| 3 to 5 | 24 | 102.50 ms | 7.98 | 1.63 | [92.00, 112.00] |
| 4 to 6 | 24 | 101.50 ms | 8.07 | 1.65 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 0.03 µV | 2.52 | 0.51 | [-5.86, 4.12] |
| 2 to 4 | 24 | -1.72 µV | 1.83 | 0.37 | [-6.04, 1.36] |
| 3 to 5 | 24 | -1.69 µV | 2.04 | 0.42 | [-4.95, 2.64] |
| 4 to 6 | 24 | -1.09 µV | 2.18 | 0.45 | [-4.45, 2.92] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 168.17 ms | 22.24 | 4.54 | [136.00, 208.00] |
| 2 to 4 | 24 | 173.00 ms | 17.43 | 3.56 | [136.00, 208.00] |
| 3 to 5 | 24 | 167.50 ms | 22.82 | 4.66 | [136.00, 208.00] |
| 4 to 6 | 24 | 168.50 ms | 22.30 | 4.55 | [136.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.64 µV | 2.58 | 0.53 | [-12.65, -2.26] |
| 2 to 4 | 24 | -6.24 µV | 2.99 | 0.61 | [-15.66, -0.96] |
| 3 to 5 | 24 | -5.25 µV | 2.63 | 0.54 | [-11.97, 0.09] |
| 4 to 6 | 24 | -5.97 µV | 3.18 | 0.65 | [-13.20, 0.34] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 90.33 ms | 15.60 | 3.18 | [72.00, 108.00] |
| 2 to 4 | 24 | 92.83 ms | 14.20 | 2.90 | [72.00, 108.00] |
| 3 to 5 | 24 | 91.00 ms | 13.87 | 2.83 | [72.00, 108.00] |
| 4 to 6 | 24 | 91.67 ms | 13.75 | 2.81 | [72.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 1.22 µV | 2.16 | 0.44 | [-2.33, 7.47] |
| 2 to 4 | 24 | 2.27 µV | 1.45 | 0.30 | [-0.56, 5.61] |
| 3 to 5 | 24 | 1.99 µV | 2.39 | 0.49 | [-3.58, 6.29] |
| 4 to 6 | 24 | 1.72 µV | 2.19 | 0.45 | [-1.72, 5.39] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 465.17 ms | 42.65 | 8.71 | [388.00, 536.00] |
| 2 to 4 | 24 | 467.67 ms | 48.32 | 9.86 | [392.00, 536.00] |
| 3 to 5 | 24 | 468.33 ms | 54.24 | 11.07 | [388.00, 536.00] |
| 4 to 6 | 24 | 472.50 ms | 52.56 | 10.73 | [388.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 5.03 µV | 3.96 | 0.81 | [-1.07, 15.57] |
| 2 to 4 | 24 | 5.59 µV | 4.82 | 0.98 | [-4.77, 17.43] |
| 3 to 5 | 24 | 4.55 µV | 3.87 | 0.79 | [-2.99, 15.27] |
| 4 to 6 | 24 | 4.60 µV | 3.49 | 0.71 | [-1.42, 9.75] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 682.72, BIC = 700.68
- **2 to 4 vs 1 to 3**: *β* = -0.08, *SE* = 2.182, *z* = -0.037, *p* = 0.971
- **3 to 5 vs 1 to 3**: *β* = 0.53, *SE* = 2.115, *z* = 0.249, *p* = 0.803
- **4 to 6 vs 1 to 3**: *β* = -0.47, *SE* = 2.118, *z* = -0.221, *p* = 0.825
- **SNR**: *β* = 0.08, *SE* = 0.509, *z* = 0.154, *p* = 0.877

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.08 | 2.18 | 0.04 | 0.971 | 0.999 | n.s. |
| 1 to 3 - 3 to 5 | -0.53 | 2.12 | -0.25 | 0.803 | 0.999 | n.s. |
| 1 to 3 - 4 to 6 | 0.47 | 2.12 | 0.22 | 0.825 | 0.999 | n.s. |
| 2 to 4 - 3 to 5 | -0.61 | 2.14 | -0.28 | 0.777 | 0.999 | n.s. |
| 2 to 4 - 4 to 6 | 0.39 | 2.14 | 0.18 | 0.856 | 0.999 | n.s. |
| 3 to 5 - 4 to 6 | 0.99 | 2.11 | 0.47 | 0.637 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.08, *p* = 0.973, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | 0.08 | 23 | = 0.941 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.25 | 23 | = 0.941 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | 0.20 | 23 | = 0.941 | 0.06 [-0.38, 0.46] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -0.31 | 23 | = 0.941 | -0.08 [-0.49, 0.36] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 0.16 | 23 | = 0.941 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 0.54 | 23 | = 0.941 | 0.12 [-0.31, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 427.10, BIC = 445.05
- **2 to 4 vs 1 to 3**: *β* = -1.94, *SE* = 0.595, *z* = -3.260, *p* = 0.001
- **3 to 5 vs 1 to 3**: *β* = -1.78, *SE* = 0.578, *z* = -3.090, *p* = 0.002
- **4 to 6 vs 1 to 3**: *β* = -1.19, *SE* = 0.578, *z* = -2.054, *p* = 0.040
- **SNR**: *β* = -0.17, *SE* = 0.136, *z* = -1.216, *p* = 0.224

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 1.94 | 0.59 | 3.26 | 0.001 | 0.007 | ** |
| 1 to 3 - 3 to 5 | 1.78 | 0.58 | 3.09 | 0.002 | 0.010 | ** |
| 1 to 3 - 4 to 6 | 1.19 | 0.58 | 2.05 | 0.040 | 0.151 | n.s. |
| 2 to 4 - 3 to 5 | -0.15 | 0.58 | -0.26 | 0.792 | 0.792 | n.s. |
| 2 to 4 - 4 to 6 | -0.75 | 0.58 | -1.29 | 0.198 | 0.484 | n.s. |
| 3 to 5 - 4 to 6 | -0.60 | 0.58 | -1.04 | 0.300 | 0.510 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.90, *p* = 0.012, η²_G = 0.102
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | 3.01 | 23 | = 0.023 | 0.80 [0.15, 1.07] | medium | * |
| 1 to 3 vs 3 to 5 | 2.92 | 23 | = 0.023 | 0.75 [0.14, 1.05] | medium | * |
| 1 to 3 vs 4 to 6 | 1.67 | 23 | = 0.218 | 0.47 [-0.09, 0.77] | small | n.s. |
| 2 to 4 vs 3 to 5 | -0.05 | 23 | = 0.960 | -0.02 [-0.43, 0.41] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | -1.24 | 23 | = 0.339 | -0.32 [-0.68, 0.17] | small | n.s. |
| 3 to 5 vs 4 to 6 | -1.05 | 23 | = 0.366 | -0.29 [-0.64, 0.21] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 838.13, BIC = 856.08
- **2 to 4 vs 1 to 3**: *β* = 5.13, *SE* = 4.241, *z* = 1.209, *p* = 0.227
- **3 to 5 vs 1 to 3**: *β* = -0.23, *SE* = 4.377, *z* = -0.053, *p* = 0.958
- **4 to 6 vs 1 to 3**: *β* = 0.55, *SE* = 4.186, *z* = 0.131, *p* = 0.895
- **SNR**: *β* = 0.21, *SE* = 0.707, *z* = 0.296, *p* = 0.768

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -5.13 | 4.24 | -1.21 | 0.227 | 0.731 | n.s. |
| 1 to 3 - 3 to 5 | 0.23 | 4.38 | 0.05 | 0.958 | 0.997 | n.s. |
| 1 to 3 - 4 to 6 | -0.55 | 4.19 | -0.13 | 0.895 | 0.997 | n.s. |
| 2 to 4 - 3 to 5 | 5.36 | 4.15 | 1.29 | 0.196 | 0.731 | n.s. |
| 2 to 4 - 4 to 6 | 4.58 | 4.13 | 1.11 | 0.268 | 0.731 | n.s. |
| 3 to 5 - 4 to 6 | -0.78 | 4.19 | -0.19 | 0.852 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.71, *p* = 0.552, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.10 | 23 | = 0.563 | -0.24 [-0.65, 0.20] | small | n.s. |
| 1 to 3 vs 3 to 5 | 0.14 | 23 | = 0.941 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.07 | 23 | = 0.941 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.38 | 23 | = 0.563 | 0.27 [-0.15, 0.71] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.36 | 23 | = 0.563 | 0.22 [-0.15, 0.71] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.23 | 23 | = 0.941 | -0.04 [-0.47, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 401.82, BIC = 419.77
- **2 to 4 vs 1 to 3**: *β* = -0.47, *SE* = 0.436, *z* = -1.086, *p* = 0.277
- **3 to 5 vs 1 to 3**: *β* = 0.11, *SE* = 0.450, *z* = 0.245, *p* = 0.807
- **4 to 6 vs 1 to 3**: *β* = 0.03, *SE* = 0.430, *z* = 0.076, *p* = 0.940
- **SNR**: *β* = -0.61, *SE* = 0.072, *z* = -8.474, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.47 | 0.44 | 1.09 | 0.277 | 0.735 | n.s. |
| 1 to 3 - 3 to 5 | -0.11 | 0.45 | -0.24 | 0.807 | 0.993 | n.s. |
| 1 to 3 - 4 to 6 | -0.03 | 0.43 | -0.08 | 0.940 | 0.993 | n.s. |
| 2 to 4 - 3 to 5 | -0.58 | 0.43 | -1.37 | 0.171 | 0.676 | n.s. |
| 2 to 4 - 4 to 6 | -0.51 | 0.42 | -1.19 | 0.233 | 0.735 | n.s. |
| 3 to 5 - 4 to 6 | 0.08 | 0.43 | 0.18 | 0.857 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.03, *p* = 0.117, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.55 | 23 | = 0.651 | -0.14 [-0.54, 0.31] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -2.92 | 23 | = 0.047 | -0.53 [-1.05, -0.14] | medium | * |
| 1 to 3 vs 4 to 6 | -1.19 | 23 | = 0.370 | -0.23 [-0.67, 0.19] | small | n.s. |
| 2 to 4 vs 3 to 5 | -1.65 | 23 | = 0.309 | -0.35 [-0.77, 0.10] | small | n.s. |
| 2 to 4 vs 4 to 6 | -0.46 | 23 | = 0.651 | -0.09 [-0.52, 0.33] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 1.47 | 23 | = 0.309 | 0.25 [-0.13, 0.73] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 793.69, BIC = 811.64
- **2 to 4 vs 1 to 3**: *β* = 2.44, *SE* = 3.982, *z* = 0.612, *p* = 0.541
- **3 to 5 vs 1 to 3**: *β* = 0.71, *SE* = 3.961, *z* = 0.179, *p* = 0.858
- **4 to 6 vs 1 to 3**: *β* = 1.34, *SE* = 3.946, *z* = 0.340, *p* = 0.734
- **SNR**: *β* = -0.14, *SE* = 1.174, *z* = -0.120, *p* = 0.904

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -2.44 | 3.98 | -0.61 | 0.541 | 0.991 | n.s. |
| 1 to 3 - 3 to 5 | -0.71 | 3.96 | -0.18 | 0.858 | 0.996 | n.s. |
| 1 to 3 - 4 to 6 | -1.34 | 3.95 | -0.34 | 0.734 | 0.996 | n.s. |
| 2 to 4 - 3 to 5 | 1.73 | 4.04 | 0.43 | 0.669 | 0.996 | n.s. |
| 2 to 4 - 4 to 6 | 1.09 | 3.99 | 0.27 | 0.785 | 0.996 | n.s. |
| 3 to 5 - 4 to 6 | -0.63 | 3.95 | -0.16 | 0.872 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.14, *p* = 0.936, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.61 | 23 | = 0.880 | -0.17 [-0.55, 0.30] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.15 | 23 | = 0.880 | -0.05 [-0.45, 0.39] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.35 | 23 | = 0.880 | -0.09 [-0.49, 0.35] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 0.52 | 23 | = 0.880 | 0.13 [-0.32, 0.53] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 0.28 | 23 | = 0.880 | 0.08 [-0.37, 0.48] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -0.16 | 23 | = 0.880 | -0.05 [-0.45, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 420.23, BIC = 438.18
- **2 to 4 vs 1 to 3**: *β* = 1.02, *SE* = 0.550, *z* = 1.864, *p* = 0.062
- **3 to 5 vs 1 to 3**: *β* = 0.79, *SE* = 0.547, *z* = 1.437, *p* = 0.151
- **4 to 6 vs 1 to 3**: *β* = 0.50, *SE* = 0.545, *z* = 0.921, *p* = 0.357
- **SNR**: *β* = -0.06, *SE* = 0.164, *z* = -0.364, *p* = 0.716

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -1.02 | 0.55 | -1.86 | 0.062 | 0.321 | n.s. |
| 1 to 3 - 3 to 5 | -0.79 | 0.55 | -1.44 | 0.151 | 0.558 | n.s. |
| 1 to 3 - 4 to 6 | -0.50 | 0.54 | -0.92 | 0.357 | 0.814 | n.s. |
| 2 to 4 - 3 to 5 | 0.24 | 0.56 | 0.43 | 0.669 | 0.842 | n.s. |
| 2 to 4 - 4 to 6 | 0.52 | 0.55 | 0.95 | 0.343 | 0.814 | n.s. |
| 3 to 5 - 4 to 6 | 0.28 | 0.55 | 0.52 | 0.602 | 0.842 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.284, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -2.22 | 23 | = 0.218 | -0.57 [-0.90, -0.01] | medium | n.s. |
| 1 to 3 vs 3 to 5 | -1.24 | 23 | = 0.505 | -0.34 [-0.68, 0.18] | small | n.s. |
| 1 to 3 vs 4 to 6 | -0.79 | 23 | = 0.634 | -0.23 [-0.59, 0.26] | small | n.s. |
| 2 to 4 vs 3 to 5 | 0.50 | 23 | = 0.634 | 0.14 [-0.32, 0.53] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 1.17 | 23 | = 0.505 | 0.30 [-0.19, 0.67] | small | n.s. |
| 3 to 5 vs 4 to 6 | 0.48 | 23 | = 0.634 | 0.12 [-0.32, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1032.48, BIC = 1050.43
- **2 to 4 vs 1 to 3**: *β* = 2.56, *SE* = 13.402, *z* = 0.191, *p* = 0.848
- **3 to 5 vs 1 to 3**: *β* = 2.97, *SE* = 13.437, *z* = 0.221, *p* = 0.825
- **4 to 6 vs 1 to 3**: *β* = 7.20, *SE* = 13.417, *z* = 0.536, *p* = 0.592
- **SNR**: *β* = -0.30, *SE* = 1.584, *z* = -0.192, *p* = 0.848

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -2.56 | 13.40 | -0.19 | 0.848 | 0.999 | n.s. |
| 1 to 3 - 3 to 5 | -2.97 | 13.44 | -0.22 | 0.825 | 0.999 | n.s. |
| 1 to 3 - 4 to 6 | -7.20 | 13.42 | -0.54 | 0.592 | 0.995 | n.s. |
| 2 to 4 - 3 to 5 | -0.41 | 13.47 | -0.03 | 0.976 | 0.999 | n.s. |
| 2 to 4 - 4 to 6 | -4.63 | 13.44 | -0.34 | 0.730 | 0.999 | n.s. |
| 3 to 5 - 4 to 6 | -4.23 | 13.40 | -0.32 | 0.752 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.09, *p* = 0.963, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.17 | 23 | = 0.966 | -0.05 [-0.46, 0.39] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.23 | 23 | = 0.966 | -0.06 [-0.47, 0.38] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.48 | 23 | = 0.966 | -0.15 [-0.52, 0.33] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -0.04 | 23 | = 0.966 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | -0.43 | 23 | = 0.966 | -0.10 [-0.51, 0.33] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -0.32 | 23 | = 0.966 | -0.08 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 451.36, BIC = 469.31
- **2 to 4 vs 1 to 3**: *β* = 0.46, *SE* = 0.509, *z* = 0.897, *p* = 0.370
- **3 to 5 vs 1 to 3**: *β* = -0.16, *SE* = 0.511, *z* = -0.313, *p* = 0.754
- **4 to 6 vs 1 to 3**: *β* = -0.20, *SE* = 0.510, *z* = -0.402, *p* = 0.688
- **SNR**: *β* = 0.49, *SE* = 0.072, *z* = 6.861, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -0.46 | 0.51 | -0.90 | 0.370 | 0.842 | n.s. |
| 1 to 3 - 3 to 5 | 0.16 | 0.51 | 0.31 | 0.754 | 0.969 | n.s. |
| 1 to 3 - 4 to 6 | 0.20 | 0.51 | 0.40 | 0.688 | 0.969 | n.s. |
| 2 to 4 - 3 to 5 | 0.62 | 0.51 | 1.20 | 0.229 | 0.729 | n.s. |
| 2 to 4 - 4 to 6 | 0.66 | 0.51 | 1.29 | 0.195 | 0.729 | n.s. |
| 3 to 5 - 4 to 6 | 0.04 | 0.51 | 0.09 | 0.930 | 0.969 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.340, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.70 | 23 | = 0.590 | -0.13 [-0.57, 0.28] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | 0.70 | 23 | = 0.590 | 0.12 [-0.28, 0.57] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | 0.89 | 23 | = 0.590 | 0.11 [-0.24, 0.61] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.52 | 23 | = 0.427 | 0.24 [-0.12, 0.74] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.56 | 23 | = 0.427 | 0.23 [-0.11, 0.75] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.10 | 23 | = 0.918 | -0.01 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.012). Post-hoc tests revealed:
  - 1 to 3 showed greater amplitude than 2 to 4 (*d* = 0.80)
  - 1 to 3 showed greater amplitude than 3 to 5 (*d* = 0.75)

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
