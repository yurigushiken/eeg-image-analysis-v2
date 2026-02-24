# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:20:12

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
| 2 to 1 | 24 | 108.00 ms | 9.44 | 1.93 | [92.00, 116.00] |
| 2 to 3 | 24 | 102.50 ms | 10.07 | 2.05 | [92.00, 116.00] |
| 2 to 4 | 24 | 102.67 ms | 9.11 | 1.86 | [92.00, 116.00] |
| 2 to 5 | 24 | 102.33 ms | 9.58 | 1.95 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -1.96 µV | 1.91 | 0.39 | [-6.41, 2.51] |
| 2 to 3 | 24 | -1.35 µV | 2.03 | 0.41 | [-5.76, 2.45] |
| 2 to 4 | 24 | -1.80 µV | 1.89 | 0.39 | [-6.14, 1.36] |
| 2 to 5 | 24 | -0.91 µV | 2.31 | 0.47 | [-10.84, 1.43] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 181.83 ms | 12.76 | 2.60 | [160.00, 204.00] |
| 2 to 3 | 24 | 171.50 ms | 19.64 | 4.01 | [144.00, 204.00] |
| 2 to 4 | 24 | 173.17 ms | 16.41 | 3.35 | [144.00, 204.00] |
| 2 to 5 | 24 | 170.67 ms | 19.87 | 4.06 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -3.38 µV | 3.29 | 0.67 | [-10.79, 2.29] |
| 2 to 3 | 24 | -4.91 µV | 2.18 | 0.44 | [-10.20, 0.13] |
| 2 to 4 | 24 | -6.19 µV | 2.98 | 0.61 | [-15.66, -0.75] |
| 2 to 5 | 24 | -5.99 µV | 2.55 | 0.52 | [-13.83, -1.66] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 116.17 ms | 9.62 | 1.96 | [92.00, 124.00] |
| 2 to 3 | 24 | 109.17 ms | 12.73 | 2.60 | [88.00, 124.00] |
| 2 to 4 | 24 | 104.17 ms | 13.16 | 2.69 | [88.00, 124.00] |
| 2 to 5 | 24 | 99.33 ms | 11.72 | 2.39 | [88.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 3.63 µV | 2.54 | 0.52 | [-0.51, 9.13] |
| 2 to 3 | 24 | 1.69 µV | 2.28 | 0.47 | [-3.64, 6.87] |
| 2 to 4 | 24 | 2.17 µV | 2.10 | 0.43 | [-2.67, 7.56] |
| 2 to 5 | 24 | 1.58 µV | 2.61 | 0.53 | [-2.11, 10.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 478.83 ms | 46.25 | 9.44 | [396.00, 532.00] |
| 2 to 3 | 24 | 468.83 ms | 51.12 | 10.43 | [396.00, 532.00] |
| 2 to 4 | 24 | 468.00 ms | 47.27 | 9.65 | [396.00, 532.00] |
| 2 to 5 | 24 | 455.33 ms | 41.41 | 8.45 | [396.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 4.94 µV | 3.09 | 0.63 | [-0.66, 11.08] |
| 2 to 3 | 24 | 4.53 µV | 4.15 | 0.85 | [-3.39, 13.70] |
| 2 to 4 | 24 | 5.57 µV | 4.82 | 0.98 | [-4.77, 17.43] |
| 2 to 5 | 24 | 4.99 µV | 2.71 | 0.55 | [0.82, 11.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 713.66, BIC = 731.62
- **2 to 3 vs 2 to 1**: *β* = -5.44, *SE* = 2.532, *z* = -2.150, *p* = 0.032
- **2 to 4 vs 2 to 1**: *β* = -5.23, *SE* = 2.539, *z* = -2.058, *p* = 0.040
- **2 to 5 vs 2 to 1**: *β* = -5.61, *SE* = 2.532, *z* = -2.216, *p* = 0.027
- **SNR**: *β* = 0.21, *SE* = 0.434, *z* = 0.493, *p* = 0.622

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 5.44 | 2.53 | 2.15 | 0.032 | 0.150 | n.s. |
| 2 to 1 - 2 to 4 | 5.23 | 2.54 | 2.06 | 0.040 | 0.150 | n.s. |
| 2 to 1 - 2 to 5 | 5.61 | 2.53 | 2.22 | 0.027 | 0.150 | n.s. |
| 2 to 3 - 2 to 4 | -0.22 | 2.53 | -0.09 | 0.931 | 0.998 | n.s. |
| 2 to 3 - 2 to 5 | 0.17 | 2.53 | 0.07 | 0.948 | 0.998 | n.s. |
| 2 to 4 - 2 to 5 | 0.38 | 2.53 | 0.15 | 0.879 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.26, *p* = 0.089, η²_G = 0.061
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 1.84 | 23 | = 0.157 | 0.56 [-0.06, 0.81] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 2.24 | 23 | = 0.157 | 0.58 [0.01, 0.90] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 1.88 | 23 | = 0.157 | 0.60 [-0.05, 0.82] | medium | n.s. |
| 2 to 3 vs 2 to 4 | -0.06 | 23 | = 0.950 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 0.07 | 23 | = 0.950 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 0.16 | 23 | = 0.950 | 0.04 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 388.61, BIC = 406.56
- **2 to 3 vs 2 to 1**: *β* = 0.50, *SE* = 0.468, *z* = 1.065, *p* = 0.287
- **2 to 4 vs 2 to 1**: *β* = -0.06, *SE* = 0.469, *z* = -0.132, *p* = 0.895
- **2 to 5 vs 2 to 1**: *β* = 0.93, *SE* = 0.468, *z* = 1.991, *p* = 0.047
- **SNR**: *β* = -0.45, *SE* = 0.081, *z* = -5.544, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | -0.50 | 0.47 | -1.07 | 0.287 | 0.650 | n.s. |
| 2 to 1 - 2 to 4 | 0.06 | 0.47 | 0.13 | 0.895 | 0.895 | n.s. |
| 2 to 1 - 2 to 5 | -0.93 | 0.47 | -1.99 | 0.047 | 0.212 | n.s. |
| 2 to 3 - 2 to 4 | 0.56 | 0.47 | 1.20 | 0.231 | 0.650 | n.s. |
| 2 to 3 - 2 to 5 | -0.43 | 0.47 | -0.93 | 0.354 | 0.650 | n.s. |
| 2 to 4 - 2 to 5 | -0.99 | 0.47 | -2.12 | 0.034 | 0.186 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.57, *p* = 0.204, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | -0.99 | 23 | = 0.578 | -0.31 [-0.63, 0.22] | small | n.s. |
| 2 to 1 vs 2 to 4 | -0.38 | 23 | = 0.705 | -0.09 [-0.50, 0.34] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | -2.32 | 23 | = 0.178 | -0.49 [-0.92, -0.03] | small | n.s. |
| 2 to 3 vs 2 to 4 | 0.81 | 23 | = 0.578 | 0.23 [-0.26, 0.59] | small | n.s. |
| 2 to 3 vs 2 to 5 | -0.72 | 23 | = 0.578 | -0.20 [-0.57, 0.28] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | -1.75 | 23 | = 0.282 | -0.42 [-0.79, 0.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 813.24, BIC = 831.19
- **2 to 3 vs 2 to 1**: *β* = -9.45, *SE* = 3.970, *z* = -2.379, *p* = 0.017
- **2 to 4 vs 2 to 1**: *β* = -7.21, *SE* = 4.091, *z* = -1.762, *p* = 0.078
- **2 to 5 vs 2 to 1**: *β* = -9.91, *SE* = 4.042, *z* = -2.452, *p* = 0.014
- **SNR**: *β* = -0.78, *SE* = 0.666, *z* = -1.175, *p* = 0.240

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 9.45 | 3.97 | 2.38 | 0.017 | 0.084 | n.s. |
| 2 to 1 - 2 to 4 | 7.21 | 4.09 | 1.76 | 0.078 | 0.277 | n.s. |
| 2 to 1 - 2 to 5 | 9.91 | 4.04 | 2.45 | 0.014 | 0.082 | n.s. |
| 2 to 3 - 2 to 4 | -2.24 | 3.93 | -0.57 | 0.569 | 0.866 | n.s. |
| 2 to 3 - 2 to 5 | 0.46 | 3.91 | 0.12 | 0.906 | 0.906 | n.s. |
| 2 to 4 - 2 to 5 | 2.70 | 3.90 | 0.69 | 0.489 | 0.866 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.37, *p* = 0.023, η²_G = 0.064
- Greenhouse-Geisser corrected: *p* = 0.041 (ε = 0.689)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.63 | 23 | = 0.032 | 0.62 [0.09, 0.99] | medium | * |
| 2 to 1 vs 2 to 4 | 2.61 | 23 | = 0.032 | 0.59 [0.08, 0.98] | medium | * |
| 2 to 1 vs 2 to 5 | 3.03 | 23 | = 0.032 | 0.67 [0.16, 1.08] | medium | * |
| 2 to 3 vs 2 to 4 | -0.34 | 23 | = 0.865 | -0.09 [-0.49, 0.35] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 0.17 | 23 | = 0.865 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.02 | 23 | = 0.475 | 0.14 [-0.22, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 433.30, BIC = 451.25
- **2 to 3 vs 2 to 1**: *β* = -0.90, *SE* = 0.555, *z* = -1.624, *p* = 0.104
- **2 to 4 vs 2 to 1**: *β* = -1.78, *SE* = 0.571, *z* = -3.120, *p* = 0.002
- **2 to 5 vs 2 to 1**: *β* = -1.72, *SE* = 0.564, *z* = -3.046, *p* = 0.002
- **SNR**: *β* = -0.55, *SE* = 0.088, *z* = -6.281, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 0.90 | 0.56 | 1.62 | 0.104 | 0.357 | n.s. |
| 2 to 1 - 2 to 4 | 1.78 | 0.57 | 3.12 | 0.002 | 0.011 | * |
| 2 to 1 - 2 to 5 | 1.72 | 0.56 | 3.05 | 0.002 | 0.012 | * |
| 2 to 3 - 2 to 4 | 0.88 | 0.55 | 1.60 | 0.111 | 0.357 | n.s. |
| 2 to 3 - 2 to 5 | 0.82 | 0.55 | 1.49 | 0.136 | 0.357 | n.s. |
| 2 to 4 - 2 to 5 | -0.06 | 0.55 | -0.11 | 0.911 | 0.911 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.65, *p* < .001, η²_G = 0.144
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.82 | 23 | = 0.019 | 0.55 [0.12, 1.03] | medium | * |
| 2 to 1 vs 2 to 4 | 3.55 | 23 | = 0.008 | 0.90 [0.25, 1.20] | large | ** |
| 2 to 1 vs 2 to 5 | 3.36 | 23 | = 0.008 | 0.89 [0.22, 1.16] | large | ** |
| 2 to 3 vs 2 to 4 | 2.21 | 23 | = 0.056 | 0.49 [0.01, 0.89] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.79 | 23 | = 0.104 | 0.46 [-0.07, 0.80] | small | n.s. |
| 2 to 4 vs 2 to 5 | -0.33 | 23 | = 0.743 | -0.07 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 755.15, BIC = 773.10
- **2 to 3 vs 2 to 1**: *β* = -6.62, *SE* = 3.177, *z* = -2.084, *p* = 0.037
- **2 to 4 vs 2 to 1**: *β* = -11.57, *SE* = 3.191, *z* = -3.627, *p* < .001
- **2 to 5 vs 2 to 1**: *β* = -16.49, *SE* = 3.168, *z* = -5.205, *p* < .001
- **SNR**: *β* = 0.40, *SE* = 0.623, *z* = 0.647, *p* = 0.518

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 6.62 | 3.18 | 2.08 | 0.037 | 0.107 | n.s. |
| 2 to 1 - 2 to 4 | 11.57 | 3.19 | 3.63 | < .001 | 0.001 | ** |
| 2 to 1 - 2 to 5 | 16.49 | 3.17 | 5.20 | < .001 | < .001 | *** |
| 2 to 3 - 2 to 4 | 4.95 | 3.12 | 1.59 | 0.113 | 0.213 | n.s. |
| 2 to 3 - 2 to 5 | 9.87 | 3.12 | 3.16 | 0.002 | 0.006 | ** |
| 2 to 4 - 2 to 5 | 4.91 | 3.12 | 1.57 | 0.116 | 0.213 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.08, *p* < .001, η²_G = 0.223
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.31 | 23 | = 0.045 | 0.62 [0.03, 0.92] | medium | * |
| 2 to 1 vs 2 to 4 | 3.59 | 23 | = 0.005 | 1.04 [0.26, 1.21] | large | ** |
| 2 to 1 vs 2 to 5 | 5.32 | 23 | < .001 | 1.57 [0.55, 1.62] | large | *** |
| 2 to 3 vs 2 to 4 | 1.36 | 23 | = 0.187 | 0.39 [-0.15, 0.71] | small | n.s. |
| 2 to 3 vs 2 to 5 | 3.09 | 23 | = 0.010 | 0.80 [0.17, 1.09] | large | * |
| 2 to 4 vs 2 to 5 | 1.75 | 23 | = 0.111 | 0.39 [-0.08, 0.79] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 419.31, BIC = 437.26
- **2 to 3 vs 2 to 1**: *β* = -1.47, *SE* = 0.531, *z* = -2.776, *p* = 0.006
- **2 to 4 vs 2 to 1**: *β* = -0.93, *SE* = 0.534, *z* = -1.740, *p* = 0.082
- **2 to 5 vs 2 to 1**: *β* = -1.62, *SE* = 0.529, *z* = -3.055, *p* = 0.002
- **SNR**: *β* = 0.49, *SE* = 0.111, *z* = 4.458, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 1.47 | 0.53 | 2.78 | 0.006 | 0.027 | * |
| 2 to 1 - 2 to 4 | 0.93 | 0.53 | 1.74 | 0.082 | 0.289 | n.s. |
| 2 to 1 - 2 to 5 | 1.62 | 0.53 | 3.05 | 0.002 | 0.013 | * |
| 2 to 3 - 2 to 4 | -0.55 | 0.52 | -1.05 | 0.295 | 0.503 | n.s. |
| 2 to 3 - 2 to 5 | 0.14 | 0.52 | 0.27 | 0.784 | 0.784 | n.s. |
| 2 to 4 - 2 to 5 | 0.69 | 0.52 | 1.32 | 0.187 | 0.462 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.50, *p* = 0.002, η²_G = 0.108
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 3.53 | 23 | = 0.005 | 0.80 [0.25, 1.19] | large | ** |
| 2 to 1 vs 2 to 4 | 2.75 | 23 | = 0.023 | 0.62 [0.11, 1.02] | medium | * |
| 2 to 1 vs 2 to 5 | 4.08 | 23 | = 0.003 | 0.79 [0.34, 1.32] | medium | ** |
| 2 to 3 vs 2 to 4 | -0.79 | 23 | = 0.528 | -0.22 [-0.59, 0.26] | small | n.s. |
| 2 to 3 vs 2 to 5 | 0.16 | 23 | = 0.872 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.02 | 23 | = 0.476 | 0.25 [-0.22, 0.64] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1017.01, BIC = 1034.96
- **2 to 3 vs 2 to 1**: *β* = -9.95, *SE* = 12.131, *z* = -0.820, *p* = 0.412
- **2 to 4 vs 2 to 1**: *β* = -10.75, *SE* = 12.172, *z* = -0.884, *p* = 0.377
- **2 to 5 vs 2 to 1**: *β* = -23.51, *SE* = 12.092, *z* = -1.944, *p* = 0.052
- **SNR**: *β* = -0.08, *SE* = 1.448, *z* = -0.056, *p* = 0.955

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 9.94 | 12.13 | 0.82 | 0.412 | 0.784 | n.s. |
| 2 to 1 - 2 to 4 | 10.75 | 12.17 | 0.88 | 0.377 | 0.784 | n.s. |
| 2 to 1 - 2 to 5 | 23.51 | 12.09 | 1.94 | 0.052 | 0.274 | n.s. |
| 2 to 3 - 2 to 4 | 0.81 | 12.10 | 0.07 | 0.947 | 0.947 | n.s. |
| 2 to 3 - 2 to 5 | 13.56 | 12.14 | 1.12 | 0.264 | 0.784 | n.s. |
| 2 to 4 - 2 to 5 | 12.75 | 12.19 | 1.05 | 0.295 | 0.784 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.22, *p* = 0.311, η²_G = 0.032
- Greenhouse-Geisser corrected: *p* = 0.307 (ε = 0.716)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 0.69 | 23 | = 0.597 | 0.21 [-0.28, 0.57] | small | n.s. |
| 2 to 1 vs 2 to 4 | 1.35 | 23 | = 0.487 | 0.23 [-0.15, 0.71] | small | n.s. |
| 2 to 1 vs 2 to 5 | 2.21 | 23 | = 0.226 | 0.54 [0.01, 0.89] | medium | n.s. |
| 2 to 3 vs 2 to 4 | 0.05 | 23 | = 0.957 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 1.16 | 23 | = 0.487 | 0.29 [-0.19, 0.66] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.01 | 23 | = 0.487 | 0.29 [-0.22, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 476.68, BIC = 494.63
- **2 to 3 vs 2 to 1**: *β* = -0.71, *SE* = 0.628, *z* = -1.125, *p* = 0.261
- **2 to 4 vs 2 to 1**: *β* = 0.21, *SE* = 0.630, *z* = 0.336, *p* = 0.737
- **2 to 5 vs 2 to 1**: *β* = 0.08, *SE* = 0.625, *z* = 0.124, *p* = 0.901
- **SNR**: *β* = 0.43, *SE* = 0.087, *z* = 4.937, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 0.71 | 0.63 | 1.12 | 0.261 | 0.701 | n.s. |
| 2 to 1 - 2 to 4 | -0.21 | 0.63 | -0.34 | 0.737 | 0.982 | n.s. |
| 2 to 1 - 2 to 5 | -0.08 | 0.62 | -0.12 | 0.901 | 0.982 | n.s. |
| 2 to 3 - 2 to 4 | -0.92 | 0.63 | -1.47 | 0.142 | 0.601 | n.s. |
| 2 to 3 - 2 to 5 | -0.78 | 0.63 | -1.25 | 0.212 | 0.697 | n.s. |
| 2 to 4 - 2 to 5 | 0.13 | 0.63 | 0.21 | 0.831 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.533, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 0.62 | 23 | = 0.653 | 0.11 [-0.30, 0.55] | negligible | n.s. |
| 2 to 1 vs 2 to 4 | -0.70 | 23 | = 0.653 | -0.15 [-0.57, 0.28] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | -0.09 | 23 | = 0.931 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -1.48 | 23 | = 0.653 | -0.23 [-0.73, 0.13] | small | n.s. |
| 2 to 3 vs 2 to 5 | -0.80 | 23 | = 0.653 | -0.13 [-0.59, 0.26] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 0.73 | 23 | = 0.653 | 0.15 [-0.28, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Marginal trend toward condition differences (*p* = 0.089)
**N1 latency:** Significant main effect of condition (*p* = 0.023). Post-hoc tests revealed:
  - 2 to 1 showed greater latency than 2 to 3 (*d* = 0.62)
  - 2 to 1 showed greater latency than 2 to 4 (*d* = 0.59)
  - 2 to 1 showed greater latency than 2 to 5 (*d* = 0.67)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 3 (*d* = 0.55)
  - 2 to 1 showed greater amplitude than 2 to 4 (*d* = 0.90)
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 0.89)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater latency than 2 to 3 (*d* = 0.62)
  - 2 to 1 showed greater latency than 2 to 4 (*d* = 1.04)
  - 2 to 1 showed greater latency than 2 to 5 (*d* = 1.57)
  - 2 to 3 showed greater latency than 2 to 5 (*d* = 0.80)
**P1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 3 (*d* = 0.80)
  - 2 to 1 showed greater amplitude than 2 to 4 (*d* = 0.62)
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 0.79)

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
