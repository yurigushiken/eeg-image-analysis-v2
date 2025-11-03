# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:37:39

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
| 3 to 1 | 8 | 108.00 ms | 9.56 | 3.38 | [96.00, 120.00] |
| 4 to 2 | 10 | 108.80 ms | 10.96 | 3.47 | [96.00, 120.00] |
| 5 to 3 | 4 | 114.00 ms | 12.00 | 6.00 | [96.00, 120.00] |
| 6 to 4 | 7 | 111.43 ms | 11.41 | 4.31 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 8 | 2.81 µV | 1.37 | 0.48 | [1.30, 5.34] |
| 4 to 2 | 10 | 3.46 µV | 2.13 | 0.67 | [0.57, 6.68] |
| 5 to 3 | 4 | 3.58 µV | 1.43 | 0.72 | [1.88, 5.36] |
| 6 to 4 | 7 | 3.69 µV | 0.91 | 0.34 | [2.29, 5.06] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 19 | 184.00 ms | 15.08 | 3.46 | [156.00, 208.00] |
| 4 to 2 | 24 | 178.33 ms | 14.96 | 3.05 | [148.00, 208.00] |
| 5 to 3 | 24 | 174.50 ms | 15.86 | 3.24 | [148.00, 208.00] |
| 6 to 4 | 23 | 174.61 ms | 20.56 | 4.29 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 19 | -4.98 µV | 2.64 | 0.61 | [-10.41, -1.40] |
| 4 to 2 | 24 | -6.16 µV | 3.06 | 0.62 | [-12.20, -2.20] |
| 5 to 3 | 24 | -5.93 µV | 2.79 | 0.57 | [-12.11, -1.76] |
| 6 to 4 | 23 | -6.04 µV | 2.82 | 0.59 | [-12.20, -1.79] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 21 | 116.76 ms | 10.09 | 2.20 | [100.00, 128.00] |
| 4 to 2 | 14 | 120.86 ms | 7.05 | 1.88 | [108.00, 128.00] |
| 5 to 3 | 17 | 114.35 ms | 9.28 | 2.25 | [100.00, 128.00] |
| 6 to 4 | 15 | 114.67 ms | 9.52 | 2.46 | [100.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 21 | 3.82 µV | 1.76 | 0.38 | [1.64, 9.14] |
| 4 to 2 | 14 | 3.01 µV | 1.16 | 0.31 | [1.28, 4.87] |
| 5 to 3 | 17 | 3.11 µV | 1.30 | 0.31 | [1.10, 4.76] |
| 6 to 4 | 15 | 4.22 µV | 1.89 | 0.49 | [1.39, 7.45] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 484.20 ms | 27.42 | 6.13 | [444.00, 536.00] |
| 4 to 2 | 18 | 484.89 ms | 35.32 | 8.32 | [428.00, 536.00] |
| 5 to 3 | 17 | 467.53 ms | 19.33 | 4.69 | [428.00, 500.00] |
| 6 to 4 | 19 | 490.74 ms | 33.47 | 7.68 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 6.15 µV | 3.13 | 0.70 | [2.57, 16.27] |
| 4 to 2 | 18 | 5.97 µV | 3.63 | 0.85 | [0.66, 14.41] |
| 5 to 3 | 17 | 6.28 µV | 2.15 | 0.52 | [3.01, 10.28] |
| 6 to 4 | 19 | 6.01 µV | 2.72 | 0.62 | [2.97, 13.11] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 221.04, BIC = 230.61
- **4 to 2 vs 3 to 1**: *β* = 2.66, *SE* = 2.970, *z* = 0.896, *p* = 0.370
- **5 to 3 vs 3 to 1**: *β* = 2.30, *SE* = 4.094, *z* = 0.561, *p* = 0.575
- **6 to 4 vs 3 to 1**: *β* = 1.19, *SE* = 3.253, *z* = 0.366, *p* = 0.714
- **SNR**: *β* = 2.19, *SE* = 1.385, *z* = 1.583, *p* = 0.113

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -2.66 | 2.97 | -0.90 | 0.370 | 0.938 | n.s. |
| 3 to 1 - 5 to 3 | -2.30 | 4.09 | -0.56 | 0.575 | 0.986 | n.s. |
| 3 to 1 - 6 to 4 | -1.19 | 3.25 | -0.37 | 0.714 | 0.986 | n.s. |
| 4 to 2 - 5 to 3 | 0.36 | 4.21 | 0.09 | 0.931 | 0.986 | n.s. |
| 4 to 2 - 6 to 4 | 1.47 | 3.22 | 0.46 | 0.648 | 0.986 | n.s. |
| 5 to 3 - 6 to 4 | 1.11 | 3.32 | 0.33 | 0.739 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 113.40, BIC = 122.97
- **4 to 2 vs 3 to 1**: *β* = 0.49, *SE* = 0.647, *z* = 0.754, *p* = 0.451
- **5 to 3 vs 3 to 1**: *β* = 0.89, *SE* = 0.825, *z* = 1.079, *p* = 0.280
- **6 to 4 vs 3 to 1**: *β* = 1.13, *SE* = 0.709, *z* = 1.593, *p* = 0.111
- **SNR**: *β* = 0.53, *SE* = 0.210, *z* = 2.545, *p* = 0.011

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.49 | 0.65 | -0.75 | 0.451 | 0.839 | n.s. |
| 3 to 1 - 5 to 3 | -0.89 | 0.82 | -1.08 | 0.280 | 0.807 | n.s. |
| 3 to 1 - 6 to 4 | -1.13 | 0.71 | -1.59 | 0.111 | 0.507 | n.s. |
| 4 to 2 - 5 to 3 | -0.40 | 0.82 | -0.49 | 0.622 | 0.857 | n.s. |
| 4 to 2 - 6 to 4 | -0.64 | 0.71 | -0.90 | 0.366 | 0.839 | n.s. |
| 5 to 3 - 6 to 4 | -0.24 | 0.84 | -0.28 | 0.777 | 0.857 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 751.09, BIC = 768.58
- **4 to 2 vs 3 to 1**: *β* = -5.59, *SE* = 3.776, *z* = -1.480, *p* = 0.139
- **5 to 3 vs 3 to 1**: *β* = -9.94, *SE* = 3.853, *z* = -2.580, *p* = 0.010
- **6 to 4 vs 3 to 1**: *β* = -10.22, *SE* = 3.962, *z* = -2.579, *p* = 0.010
- **SNR**: *β* = 0.60, *SE* = 0.456, *z* = 1.324, *p* = 0.186

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 5.59 | 3.78 | 1.48 | 0.139 | 0.450 | n.s. |
| 3 to 1 - 5 to 3 | 9.94 | 3.85 | 2.58 | 0.010 | 0.058 | n.s. |
| 3 to 1 - 6 to 4 | 10.22 | 3.96 | 2.58 | 0.010 | 0.058 | n.s. |
| 4 to 2 - 5 to 3 | 4.36 | 3.48 | 1.25 | 0.211 | 0.476 | n.s. |
| 4 to 2 - 6 to 4 | 4.63 | 3.56 | 1.30 | 0.194 | 0.476 | n.s. |
| 5 to 3 - 6 to 4 | 0.28 | 3.52 | 0.08 | 0.937 | 0.937 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.58, *p* = 0.205, η²_G = 0.038
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.54 | 17 | = 0.286 | 0.37 [-0.12, 0.88] | small | n.s. |
| 3 to 1 vs 5 to 3 | 2.33 | 17 | = 0.195 | 0.50 [-0.02, 1.00] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.68 | 17 | = 0.286 | 0.45 [-0.12, 0.91] | small | n.s. |
| 4 to 2 vs 5 to 3 | 0.59 | 17 | = 0.754 | 0.14 [-0.18, 0.68] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.49 | 17 | = 0.754 | 0.14 [-0.24, 0.63] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.10 | 17 | = 0.922 | 0.02 [-0.46, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 408.57, BIC = 426.07
- **4 to 2 vs 3 to 1**: *β* = -1.02, *SE* = 0.571, *z* = -1.794, *p* = 0.073
- **5 to 3 vs 3 to 1**: *β* = -0.47, *SE* = 0.583, *z* = -0.802, *p* = 0.422
- **6 to 4 vs 3 to 1**: *β* = -0.43, *SE* = 0.600, *z* = -0.711, *p* = 0.477
- **SNR**: *β* = -0.37, *SE* = 0.069, *z* = -5.400, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 1.02 | 0.57 | 1.79 | 0.073 | 0.364 | n.s. |
| 3 to 1 - 5 to 3 | 0.47 | 0.58 | 0.80 | 0.422 | 0.807 | n.s. |
| 3 to 1 - 6 to 4 | 0.43 | 0.60 | 0.71 | 0.477 | 0.807 | n.s. |
| 4 to 2 - 5 to 3 | -0.56 | 0.53 | -1.06 | 0.290 | 0.788 | n.s. |
| 4 to 2 - 6 to 4 | -0.60 | 0.54 | -1.11 | 0.266 | 0.788 | n.s. |
| 5 to 3 - 6 to 4 | -0.04 | 0.53 | -0.08 | 0.938 | 0.938 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.61, *p* = 0.061, η²_G = 0.062
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 2.78 | 17 | = 0.077 | 0.65 [0.11, 1.17] | medium | n.s. |
| 3 to 1 vs 5 to 3 | 2.06 | 17 | = 0.164 | 0.58 [-0.13, 0.87] | medium | n.s. |
| 3 to 1 vs 6 to 4 | 1.85 | 17 | = 0.164 | 0.54 [-0.08, 0.96] | medium | n.s. |
| 4 to 2 vs 5 to 3 | -0.36 | 17 | = 0.865 | -0.09 [-0.50, 0.35] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -0.60 | 17 | = 0.831 | -0.11 [-0.44, 0.42] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | -0.09 | 17 | = 0.926 | -0.03 [-0.43, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 493.15, BIC = 508.59
- **4 to 2 vs 3 to 1**: *β* = 3.36, *SE* = 2.726, *z* = 1.234, *p* = 0.217
- **5 to 3 vs 3 to 1**: *β* = -2.93, *SE* = 2.550, *z* = -1.148, *p* = 0.251
- **6 to 4 vs 3 to 1**: *β* = -3.18, *SE* = 2.707, *z* = -1.173, *p* = 0.241
- **SNR**: *β* = -0.30, *SE* = 0.439, *z* = -0.686, *p* = 0.493

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -3.36 | 2.73 | -1.23 | 0.217 | 0.625 | n.s. |
| 3 to 1 - 5 to 3 | 2.93 | 2.55 | 1.15 | 0.251 | 0.625 | n.s. |
| 3 to 1 - 6 to 4 | 3.18 | 2.71 | 1.17 | 0.241 | 0.625 | n.s. |
| 4 to 2 - 5 to 3 | 6.29 | 2.87 | 2.19 | 0.028 | 0.158 | n.s. |
| 4 to 2 - 6 to 4 | 6.54 | 3.00 | 2.18 | 0.029 | 0.158 | n.s. |
| 5 to 3 - 6 to 4 | 0.25 | 2.80 | 0.09 | 0.929 | 0.929 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.07, *p* = 0.135, η²_G = 0.111
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -1.51 | 7 | = 0.351 | -0.58 [-0.83, 0.34] | medium | n.s. |
| 3 to 1 vs 5 to 3 | 0.51 | 7 | = 0.748 | 0.20 [-0.27, 0.81] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.88 | 7 | = 0.611 | 0.30 [-0.06, 1.18] | small | n.s. |
| 4 to 2 vs 5 to 3 | 1.67 | 7 | = 0.351 | 0.78 [0.05, 1.61] | medium | n.s. |
| 4 to 2 vs 6 to 4 | 2.58 | 7 | = 0.218 | 1.02 [0.18, 1.99] | large | n.s. |
| 5 to 3 vs 6 to 4 | 0.28 | 7 | = 0.785 | 0.07 [-0.66, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 210.51, BIC = 225.95
- **4 to 2 vs 3 to 1**: *β* = -0.54, *SE* = 0.311, *z* = -1.721, *p* = 0.085
- **5 to 3 vs 3 to 1**: *β* = -0.71, *SE* = 0.291, *z* = -2.449, *p* = 0.014
- **6 to 4 vs 3 to 1**: *β* = 0.18, *SE* = 0.306, *z* = 0.589, *p* = 0.556
- **SNR**: *β* = 0.41, *SE* = 0.051, *z* = 7.951, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 0.54 | 0.31 | 1.72 | 0.085 | 0.235 | n.s. |
| 3 to 1 - 5 to 3 | 0.71 | 0.29 | 2.45 | 0.014 | 0.070 | n.s. |
| 3 to 1 - 6 to 4 | -0.18 | 0.31 | -0.59 | 0.556 | 0.803 | n.s. |
| 4 to 2 - 5 to 3 | 0.18 | 0.33 | 0.54 | 0.591 | 0.803 | n.s. |
| 4 to 2 - 6 to 4 | -0.72 | 0.34 | -2.08 | 0.038 | 0.143 | n.s. |
| 5 to 3 - 6 to 4 | -0.89 | 0.32 | -2.79 | 0.005 | 0.031 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.61, *p* = 0.078, η²_G = 0.167
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.51 | 7 | = 0.326 | 0.79 [-0.24, 0.95] | medium | n.s. |
| 3 to 1 vs 5 to 3 | 1.35 | 7 | = 0.326 | 0.54 [-0.15, 0.96] | medium | n.s. |
| 3 to 1 vs 6 to 4 | -0.30 | 7 | = 0.773 | -0.12 [-0.83, 0.34] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | -0.93 | 7 | = 0.460 | -0.32 [-0.93, 0.43] | small | n.s. |
| 4 to 2 vs 6 to 4 | -3.63 | 7 | = 0.050 | -1.22 [-1.64, 0.01] | large | n.s. |
| 5 to 3 vs 6 to 4 | -1.95 | 7 | = 0.275 | -0.85 [-1.31, 0.08] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 718.43, BIC = 734.56
- **4 to 2 vs 3 to 1**: *β* = 0.29, *SE* = 8.915, *z* = 0.032, *p* = 0.974
- **5 to 3 vs 3 to 1**: *β* = -17.11, *SE* = 8.770, *z* = -1.951, *p* = 0.051
- **6 to 4 vs 3 to 1**: *β* = 5.90, *SE* = 8.748, *z* = 0.675, *p* = 0.500
- **SNR**: *β* = -0.18, *SE* = 0.724, *z* = -0.255, *p* = 0.799

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.29 | 8.91 | -0.03 | 0.974 | 0.974 | n.s. |
| 3 to 1 - 5 to 3 | 17.11 | 8.77 | 1.95 | 0.051 | 0.229 | n.s. |
| 3 to 1 - 6 to 4 | -5.90 | 8.75 | -0.67 | 0.500 | 0.875 | n.s. |
| 4 to 2 - 5 to 3 | 17.40 | 8.91 | 1.95 | 0.051 | 0.229 | n.s. |
| 4 to 2 - 6 to 4 | -5.61 | 8.59 | -0.65 | 0.513 | 0.875 | n.s. |
| 5 to 3 - 6 to 4 | -23.02 | 8.80 | -2.62 | 0.009 | 0.052 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.23, *p* = 0.100, η²_G = 0.092
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -1.34 | 13 | = 0.304 | -0.48 [-0.55, 0.48] | small | n.s. |
| 3 to 1 vs 5 to 3 | 0.82 | 13 | = 0.516 | 0.26 [-0.14, 0.97] | small | n.s. |
| 3 to 1 vs 6 to 4 | -1.38 | 13 | = 0.304 | -0.52 [-0.75, 0.26] | medium | n.s. |
| 4 to 2 vs 5 to 3 | 2.07 | 13 | = 0.177 | 0.68 [-0.10, 1.07] | medium | n.s. |
| 4 to 2 vs 6 to 4 | -0.06 | 13 | = 0.956 | -0.02 [-0.64, 0.43] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | -2.13 | 13 | = 0.177 | -0.74 [-1.24, -0.03] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 356.85, BIC = 372.98
- **4 to 2 vs 3 to 1**: *β* = 0.61, *SE* = 0.726, *z* = 0.839, *p* = 0.401
- **5 to 3 vs 3 to 1**: *β* = 0.59, *SE* = 0.713, *z* = 0.823, *p* = 0.410
- **6 to 4 vs 3 to 1**: *β* = 0.58, *SE* = 0.710, *z* = 0.810, *p* = 0.418
- **SNR**: *β* = 0.21, *SE* = 0.061, *z* = 3.493, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.61 | 0.73 | -0.84 | 0.401 | 0.954 | n.s. |
| 3 to 1 - 5 to 3 | -0.59 | 0.71 | -0.82 | 0.410 | 0.954 | n.s. |
| 3 to 1 - 6 to 4 | -0.58 | 0.71 | -0.81 | 0.418 | 0.954 | n.s. |
| 4 to 2 - 5 to 3 | 0.02 | 0.72 | 0.03 | 0.975 | 1.000 | n.s. |
| 4 to 2 - 6 to 4 | 0.03 | 0.70 | 0.05 | 0.961 | 1.000 | n.s. |
| 5 to 3 - 6 to 4 | 0.01 | 0.71 | 0.02 | 0.987 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.31, *p* = 0.816, η²_G = 0.011
- Greenhouse-Geisser corrected: *p* = 0.694 (ε = 0.552)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.82 | 13 | = 0.897 | 0.16 [-0.31, 0.73] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.45 | 13 | = 0.897 | 0.16 [-0.48, 0.59] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 0.71 | 13 | = 0.897 | 0.29 [-0.45, 0.55] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.13 | 13 | = 0.897 | -0.04 [-0.64, 0.47] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.29 | 13 | = 0.897 | 0.09 [-0.48, 0.59] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.88 | 13 | = 0.897 | 0.17 [-0.24, 0.89] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.061)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.078)

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
