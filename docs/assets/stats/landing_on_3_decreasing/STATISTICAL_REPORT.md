# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:28:17

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
| 4 to 3 | 24 | 103.83 ms | 9.54 | 1.95 | [88.00, 116.00] |
| 5 to 3 | 24 | 103.00 ms | 9.96 | 2.03 | [88.00, 116.00] |
| 6 to 3 | 24 | 102.83 ms | 10.32 | 2.11 | [88.00, 116.00] |
| Cardinality3 | 24 | 104.50 ms | 11.99 | 2.45 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | -0.84 µV | 2.13 | 0.43 | [-6.08, 3.45] |
| 5 to 3 | 24 | -2.47 µV | 2.03 | 0.41 | [-5.05, 1.51] |
| 6 to 3 | 24 | -1.76 µV | 1.75 | 0.36 | [-6.41, 1.40] |
| Cardinality3 | 24 | -1.43 µV | 2.62 | 0.54 | [-8.81, 1.87] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 176.33 ms | 18.23 | 3.72 | [148.00, 212.00] |
| 5 to 3 | 24 | 174.67 ms | 16.20 | 3.31 | [144.00, 208.00] |
| 6 to 3 | 24 | 176.00 ms | 16.76 | 3.42 | [152.00, 212.00] |
| Cardinality3 | 24 | 171.67 ms | 19.27 | 3.93 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | -6.08 µV | 2.69 | 0.55 | [-11.27, 1.75] |
| 5 to 3 | 24 | -5.90 µV | 2.73 | 0.56 | [-12.11, -1.76] |
| 6 to 3 | 24 | -6.44 µV | 2.17 | 0.44 | [-10.34, -1.59] |
| Cardinality3 | 24 | -5.17 µV | 1.95 | 0.40 | [-10.83, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 104.50 ms | 10.96 | 2.24 | [92.00, 120.00] |
| 5 to 3 | 24 | 109.33 ms | 10.59 | 2.16 | [92.00, 120.00] |
| 6 to 3 | 24 | 107.33 ms | 11.11 | 2.27 | [92.00, 120.00] |
| Cardinality3 | 24 | 107.50 ms | 11.75 | 2.40 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 0.90 µV | 2.20 | 0.45 | [-2.73, 5.30] |
| 5 to 3 | 24 | 1.94 µV | 2.20 | 0.45 | [-3.22, 4.61] |
| 6 to 3 | 24 | 1.88 µV | 2.22 | 0.45 | [-2.16, 8.17] |
| Cardinality3 | 24 | 1.69 µV | 2.84 | 0.58 | [-3.19, 8.96] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 461.17 ms | 42.36 | 8.65 | [388.00, 524.00] |
| 5 to 3 | 24 | 462.67 ms | 32.66 | 6.67 | [400.00, 524.00] |
| 6 to 3 | 24 | 462.50 ms | 35.05 | 7.15 | [396.00, 524.00] |
| Cardinality3 | 24 | 440.50 ms | 43.36 | 8.85 | [388.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 24 | 4.78 µV | 3.48 | 0.71 | [-1.86, 11.65] |
| 5 to 3 | 24 | 4.62 µV | 3.31 | 0.68 | [-3.30, 10.28] |
| 6 to 3 | 24 | 5.17 µV | 4.22 | 0.86 | [-2.21, 14.26] |
| Cardinality3 | 24 | 3.33 µV | 3.27 | 0.67 | [-5.21, 9.60] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 731.01, BIC = 748.96
- **5 to 3 vs 4 to 3**: *β* = -1.11, *SE* = 2.883, *z* = -0.384, *p* = 0.701
- **6 to 3 vs 4 to 3**: *β* = -1.05, *SE* = 2.755, *z* = -0.382, *p* = 0.703
- **Cardinality3 vs 4 to 3**: *β* = 0.65, *SE* = 2.750, *z* = 0.237, *p* = 0.812
- **SNR**: *β* = 0.34, *SE* = 1.066, *z* = 0.318, *p* = 0.751

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 1.11 | 2.88 | 0.38 | 0.701 | 0.992 | n.s. |
| 4 to 3 - 6 to 3 | 1.05 | 2.75 | 0.38 | 0.703 | 0.992 | n.s. |
| 4 to 3 - Cardinality3 | -0.65 | 2.75 | -0.24 | 0.812 | 0.992 | n.s. |
| 5 to 3 - 6 to 3 | -0.06 | 2.84 | -0.02 | 0.984 | 0.992 | n.s. |
| 5 to 3 - Cardinality3 | -1.76 | 2.87 | -0.61 | 0.539 | 0.990 | n.s. |
| 6 to 3 - Cardinality3 | -1.70 | 2.75 | -0.62 | 0.536 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.928, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.33 | 23 | = 0.953 | 0.09 [-0.36, 0.49] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.35 | 23 | = 0.953 | 0.10 [-0.35, 0.49] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -0.24 | 23 | = 0.953 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.06 | 23 | = 0.953 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -0.57 | 23 | = 0.953 | -0.14 [-0.54, 0.31] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | -0.52 | 23 | = 0.953 | -0.15 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 397.18, BIC = 415.13
- **5 to 3 vs 4 to 3**: *β* = -1.25, *SE* = 0.452, *z* = -2.768, *p* = 0.006
- **6 to 3 vs 4 to 3**: *β* = -0.85, *SE* = 0.428, *z* = -1.990, *p* = 0.047
- **Cardinality3 vs 4 to 3**: *β* = -0.57, *SE* = 0.427, *z* = -1.332, *p* = 0.183
- **SNR**: *β* = -0.47, *SE* = 0.183, *z* = -2.546, *p* = 0.011

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 1.25 | 0.45 | 2.77 | 0.006 | 0.033 | * |
| 4 to 3 - 6 to 3 | 0.85 | 0.43 | 1.99 | 0.047 | 0.212 | n.s. |
| 4 to 3 - Cardinality3 | 0.57 | 0.43 | 1.33 | 0.183 | 0.454 | n.s. |
| 5 to 3 - 6 to 3 | -0.40 | 0.44 | -0.90 | 0.368 | 0.601 | n.s. |
| 5 to 3 - Cardinality3 | -0.68 | 0.45 | -1.52 | 0.129 | 0.425 | n.s. |
| 6 to 3 - Cardinality3 | -0.28 | 0.43 | -0.66 | 0.508 | 0.601 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.64, *p* = 0.005, η²_G = 0.072
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 3.07 | 23 | = 0.016 | 0.78 [0.16, 1.09] | medium | * |
| 4 to 3 vs 6 to 3 | 3.25 | 23 | = 0.016 | 0.47 [0.20, 1.13] | small | * |
| 4 to 3 vs Cardinality3 | 1.36 | 23 | = 0.223 | 0.25 [-0.15, 0.71] | small | n.s. |
| 5 to 3 vs 6 to 3 | -1.66 | 23 | = 0.164 | -0.37 [-0.77, 0.09] | small | n.s. |
| 5 to 3 vs Cardinality3 | -1.91 | 23 | = 0.137 | -0.44 [-0.83, 0.05] | small | n.s. |
| 6 to 3 vs Cardinality3 | -0.81 | 23 | = 0.426 | -0.15 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 800.42, BIC = 818.37
- **5 to 3 vs 4 to 3**: *β* = -1.59, *SE* = 3.371, *z* = -0.471, *p* = 0.638
- **6 to 3 vs 4 to 3**: *β* = -0.33, *SE* = 3.364, *z* = -0.098, *p* = 0.922
- **Cardinality3 vs 4 to 3**: *β* = -4.36, *SE* = 3.464, *z* = -1.260, *p* = 0.208
- **SNR**: *β* = 0.20, *SE* = 0.538, *z* = 0.366, *p* = 0.714

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 1.59 | 3.37 | 0.47 | 0.638 | 0.952 | n.s. |
| 4 to 3 - 6 to 3 | 0.33 | 3.36 | 0.10 | 0.922 | 0.952 | n.s. |
| 4 to 3 - Cardinality3 | 4.36 | 3.46 | 1.26 | 0.208 | 0.753 | n.s. |
| 5 to 3 - 6 to 3 | -1.26 | 3.37 | -0.37 | 0.709 | 0.952 | n.s. |
| 5 to 3 - Cardinality3 | 2.78 | 3.42 | 0.81 | 0.417 | 0.884 | n.s. |
| 6 to 3 - Cardinality3 | 4.03 | 3.46 | 1.16 | 0.244 | 0.753 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.76, *p* = 0.521, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.41 | 23 | = 0.826 | 0.10 [-0.34, 0.51] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.12 | 23 | = 0.908 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.25 | 23 | = 0.669 | 0.25 [-0.17, 0.68] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.43 | 23 | = 0.826 | -0.08 [-0.51, 0.34] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.84 | 23 | = 0.822 | 0.17 [-0.25, 0.60] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 1.36 | 23 | = 0.669 | 0.24 [-0.15, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 409.56, BIC = 427.51
- **5 to 3 vs 4 to 3**: *β* = 0.00, *SE* = 0.490, *z* = 0.006, *p* = 0.995
- **6 to 3 vs 4 to 3**: *β* = -0.37, *SE* = 0.490, *z* = -0.748, *p* = 0.455
- **Cardinality3 vs 4 to 3**: *β* = 0.26, *SE* = 0.502, *z* = 0.508, *p* = 0.612
- **SNR**: *β* = -0.42, *SE* = 0.072, *z* = -5.911, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.00 | 0.49 | -0.01 | 0.995 | 0.995 | n.s. |
| 4 to 3 - 6 to 3 | 0.37 | 0.49 | 0.75 | 0.455 | 0.950 | n.s. |
| 4 to 3 - Cardinality3 | -0.25 | 0.50 | -0.51 | 0.612 | 0.950 | n.s. |
| 5 to 3 - 6 to 3 | 0.37 | 0.49 | 0.75 | 0.452 | 0.950 | n.s. |
| 5 to 3 - Cardinality3 | -0.25 | 0.50 | -0.51 | 0.612 | 0.950 | n.s. |
| 6 to 3 - Cardinality3 | -0.62 | 0.50 | -1.24 | 0.216 | 0.768 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.73, *p* = 0.170, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.27 | 23 | = 0.790 | -0.06 [-0.48, 0.37] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.60 | 23 | = 0.665 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -1.62 | 23 | = 0.354 | -0.39 [-0.77, 0.10] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.98 | 23 | = 0.502 | 0.22 [-0.23, 0.63] | small | n.s. |
| 5 to 3 vs Cardinality3 | -1.25 | 23 | = 0.451 | -0.31 [-0.68, 0.17] | small | n.s. |
| 6 to 3 vs Cardinality3 | -2.51 | 23 | = 0.118 | -0.61 [-0.96, -0.06] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 716.34, BIC = 734.29
- **5 to 3 vs 4 to 3**: *β* = 4.95, *SE* = 2.217, *z* = 2.233, *p* = 0.026
- **6 to 3 vs 4 to 3**: *β* = 2.74, *SE* = 2.216, *z* = 1.236, *p* = 0.216
- **Cardinality3 vs 4 to 3**: *β* = 2.85, *SE* = 2.218, *z* = 1.286, *p* = 0.199
- **SNR**: *β* = -0.69, *SE* = 0.587, *z* = -1.174, *p* = 0.240

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -4.95 | 2.22 | -2.23 | 0.026 | 0.144 | n.s. |
| 4 to 3 - 6 to 3 | -2.74 | 2.22 | -1.24 | 0.216 | 0.669 | n.s. |
| 4 to 3 - Cardinality3 | -2.85 | 2.22 | -1.29 | 0.199 | 0.669 | n.s. |
| 5 to 3 - 6 to 3 | 2.21 | 2.22 | 0.99 | 0.320 | 0.685 | n.s. |
| 5 to 3 - Cardinality3 | 2.10 | 2.23 | 0.94 | 0.346 | 0.685 | n.s. |
| 6 to 3 - Cardinality3 | -0.11 | 2.22 | -0.05 | 0.959 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.52, *p* = 0.216, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -2.20 | 23 | = 0.227 | -0.45 [-0.89, -0.01] | small | n.s. |
| 4 to 3 vs 6 to 3 | -1.09 | 23 | = 0.466 | -0.26 [-0.65, 0.21] | small | n.s. |
| 4 to 3 vs Cardinality3 | -1.32 | 23 | = 0.466 | -0.26 [-0.70, 0.16] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.92 | 23 | = 0.466 | 0.18 [-0.24, 0.61] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.88 | 23 | = 0.466 | 0.16 [-0.25, 0.61] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | -0.07 | 23 | = 0.944 | -0.01 [-0.44, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 420.18, BIC = 438.13
- **5 to 3 vs 4 to 3**: *β* = 0.98, *SE* = 0.484, *z* = 2.029, *p* = 0.042
- **6 to 3 vs 4 to 3**: *β* = 1.03, *SE* = 0.484, *z* = 2.141, *p* = 0.032
- **Cardinality3 vs 4 to 3**: *β* = 0.87, *SE* = 0.484, *z* = 1.800, *p* = 0.072
- **SNR**: *β* = 0.35, *SE* = 0.127, *z* = 2.781, *p* = 0.005

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.98 | 0.48 | -2.03 | 0.042 | 0.195 | n.s. |
| 4 to 3 - 6 to 3 | -1.04 | 0.48 | -2.14 | 0.032 | 0.179 | n.s. |
| 4 to 3 - Cardinality3 | -0.87 | 0.48 | -1.80 | 0.072 | 0.258 | n.s. |
| 5 to 3 - 6 to 3 | -0.05 | 0.48 | -0.11 | 0.911 | 0.981 | n.s. |
| 5 to 3 - Cardinality3 | 0.11 | 0.49 | 0.23 | 0.821 | 0.981 | n.s. |
| 6 to 3 - Cardinality3 | 0.16 | 0.48 | 0.34 | 0.735 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.75, *p* = 0.165, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -1.87 | 23 | = 0.222 | -0.47 [-0.82, 0.06] | small | n.s. |
| 4 to 3 vs 6 to 3 | -2.23 | 23 | = 0.215 | -0.45 [-0.90, -0.01] | small | n.s. |
| 4 to 3 vs Cardinality3 | -1.56 | 23 | = 0.265 | -0.31 [-0.75, 0.11] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.11 | 23 | = 0.911 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.38 | 23 | = 0.845 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 0.43 | 23 | = 0.845 | 0.08 [-0.33, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 975.09, BIC = 993.04
- **5 to 3 vs 4 to 3**: *β* = 1.90, *SE* = 9.360, *z* = 0.203, *p* = 0.839
- **6 to 3 vs 4 to 3**: *β* = 1.58, *SE* = 9.336, *z* = 0.169, *p* = 0.866
- **Cardinality3 vs 4 to 3**: *β* = -21.25, *SE* = 9.401, *z* = -2.261, *p* = 0.024
- **SNR**: *β* = -0.63, *SE* = 1.311, *z* = -0.481, *p* = 0.631

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -1.90 | 9.36 | -0.20 | 0.839 | 0.996 | n.s. |
| 4 to 3 - 6 to 3 | -1.58 | 9.34 | -0.17 | 0.866 | 0.996 | n.s. |
| 4 to 3 - Cardinality3 | 21.25 | 9.40 | 2.26 | 0.024 | 0.092 | n.s. |
| 5 to 3 - 6 to 3 | 0.32 | 9.33 | 0.03 | 0.972 | 0.996 | n.s. |
| 5 to 3 - Cardinality3 | 23.15 | 9.55 | 2.43 | 0.015 | 0.088 | n.s. |
| 6 to 3 - Cardinality3 | 22.83 | 9.48 | 2.41 | 0.016 | 0.088 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.59, *p* = 0.060, η²_G = 0.058
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.15 | 23 | = 0.984 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.15 | 23 | = 0.984 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.77 | 23 | = 0.180 | 0.48 [-0.07, 0.80] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.02 | 23 | = 0.984 | 0.00 [-0.42, 0.43] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 2.55 | 23 | = 0.054 | 0.58 [0.07, 0.97] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 2.56 | 23 | = 0.054 | 0.56 [0.07, 0.97] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 468.08, BIC = 486.03
- **5 to 3 vs 4 to 3**: *β* = -0.36, *SE* = 0.569, *z* = -0.631, *p* = 0.528
- **6 to 3 vs 4 to 3**: *β* = 0.26, *SE* = 0.567, *z* = 0.466, *p* = 0.641
- **Cardinality3 vs 4 to 3**: *β* = -1.15, *SE* = 0.572, *z* = -2.019, *p* = 0.044
- **SNR**: *β* = 0.32, *SE* = 0.087, *z* = 3.635, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.36 | 0.57 | 0.63 | 0.528 | 0.777 | n.s. |
| 4 to 3 - 6 to 3 | -0.26 | 0.57 | -0.47 | 0.641 | 0.777 | n.s. |
| 4 to 3 - Cardinality3 | 1.15 | 0.57 | 2.02 | 0.044 | 0.199 | n.s. |
| 5 to 3 - 6 to 3 | -0.62 | 0.57 | -1.10 | 0.271 | 0.613 | n.s. |
| 5 to 3 - Cardinality3 | 0.79 | 0.58 | 1.37 | 0.172 | 0.530 | n.s. |
| 6 to 3 - Cardinality3 | 1.42 | 0.58 | 2.46 | 0.014 | 0.081 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.25, *p* = 0.027, η²_G = 0.037
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.32 | 23 | = 0.754 | 0.05 [-0.36, 0.49] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.69 | 23 | = 0.598 | -0.10 [-0.56, 0.28] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 2.00 | 23 | = 0.114 | 0.43 [-0.03, 0.85] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.84 | 23 | = 0.598 | -0.14 [-0.60, 0.25] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 2.30 | 23 | = 0.092 | 0.39 [0.03, 0.92] | small | n.s. |
| 6 to 3 vs Cardinality3 | 2.55 | 23 | = 0.092 | 0.49 [0.07, 0.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - 4 to 3 showed greater amplitude than 5 to 3 (*d* = 0.78)
  - 4 to 3 showed greater amplitude than 6 to 3 (*d* = 0.47)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.060)
**P3b amplitude:** Significant main effect of condition (*p* = 0.027) (no significant pairwise comparisons)

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
