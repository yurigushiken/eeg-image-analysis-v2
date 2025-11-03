# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:40:03

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
| 1 to 3 | 17 | 104.00 ms | 8.60 | 2.09 | [92.00, 112.00] |
| 2 to 4 | 8 | 105.00 ms | 9.74 | 3.44 | [92.00, 112.00] |
| 3 to 5 | 7 | 103.43 ms | 10.69 | 4.04 | [92.00, 112.00] |
| 4 to 6 | 10 | 105.60 ms | 8.26 | 2.61 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 17 | 2.91 µV | 2.20 | 0.53 | [0.49, 8.95] |
| 2 to 4 | 8 | 1.42 µV | 0.89 | 0.31 | [0.26, 3.09] |
| 3 to 5 | 7 | 3.24 µV | 1.82 | 0.69 | [1.02, 5.99] |
| 4 to 6 | 10 | 3.13 µV | 1.68 | 0.53 | [0.85, 5.74] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 168.17 ms | 22.24 | 4.54 | [136.00, 208.00] |
| 2 to 4 | 22 | 170.91 ms | 16.24 | 3.46 | [136.00, 196.00] |
| 3 to 5 | 22 | 164.36 ms | 21.05 | 4.49 | [136.00, 208.00] |
| 4 to 6 | 22 | 167.82 ms | 22.37 | 4.77 | [136.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.64 µV | 2.58 | 0.53 | [-12.65, -2.26] |
| 2 to 4 | 22 | -6.71 µV | 2.66 | 0.57 | [-15.66, -2.59] |
| 3 to 5 | 22 | -5.60 µV | 2.41 | 0.51 | [-11.97, -1.70] |
| 4 to 6 | 22 | -6.33 µV | 2.98 | 0.64 | [-13.20, -2.83] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 10 | 94.00 ms | 14.39 | 4.55 | [72.00, 108.00] |
| 2 to 4 | 16 | 90.50 ms | 14.08 | 3.52 | [72.00, 108.00] |
| 3 to 5 | 14 | 94.57 ms | 12.51 | 3.34 | [72.00, 108.00] |
| 4 to 6 | 13 | 96.62 ms | 10.56 | 2.93 | [72.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 10 | 2.74 µV | 1.92 | 0.61 | [0.93, 7.47] |
| 2 to 4 | 16 | 2.54 µV | 1.15 | 0.29 | [1.12, 5.61] |
| 3 to 5 | 14 | 3.41 µV | 1.55 | 0.42 | [1.48, 6.29] |
| 4 to 6 | 13 | 3.32 µV | 1.37 | 0.38 | [1.15, 5.39] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 474.20 ms | 39.50 | 8.83 | [404.00, 536.00] |
| 2 to 4 | 18 | 470.22 ms | 52.36 | 12.34 | [392.00, 536.00] |
| 3 to 5 | 17 | 470.82 ms | 49.81 | 12.08 | [388.00, 536.00] |
| 4 to 6 | 18 | 472.44 ms | 56.85 | 13.40 | [388.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 5.98 µV | 3.60 | 0.81 | [1.71, 15.57] |
| 2 to 4 | 18 | 7.17 µV | 4.23 | 1.00 | [1.60, 17.43] |
| 3 to 5 | 17 | 6.24 µV | 3.15 | 0.76 | [2.79, 15.27] |
| 4 to 6 | 18 | 5.86 µV | 3.07 | 0.72 | [1.67, 9.75] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 312.38, BIC = 324.54
- **2 to 4 vs 1 to 3**: *β* = 1.03, *SE* = 3.739, *z* = 0.275, *p* = 0.783
- **3 to 5 vs 1 to 3**: *β* = -1.23, *SE* = 3.795, *z* = -0.324, *p* = 0.746
- **4 to 6 vs 1 to 3**: *β* = 1.60, *SE* = 3.265, *z* = 0.489, *p* = 0.625
- **SNR**: *β* = 0.68, *SE* = 0.815, *z* = 0.830, *p* = 0.406

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -1.03 | 3.74 | -0.27 | 0.783 | 0.989 | n.s. |
| 1 to 3 - 3 to 5 | 1.23 | 3.80 | 0.32 | 0.746 | 0.989 | n.s. |
| 1 to 3 - 4 to 6 | -1.60 | 3.26 | -0.49 | 0.625 | 0.989 | n.s. |
| 2 to 4 - 3 to 5 | 2.26 | 4.21 | 0.54 | 0.592 | 0.989 | n.s. |
| 2 to 4 - 4 to 6 | -0.57 | 3.92 | -0.15 | 0.885 | 0.989 | n.s. |
| 3 to 5 - 4 to 6 | -2.83 | 3.95 | -0.72 | 0.474 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 135.24, BIC = 147.41
- **2 to 4 vs 1 to 3**: *β* = -0.46, *SE* = 0.376, *z* = -1.221, *p* = 0.222
- **3 to 5 vs 1 to 3**: *β* = 1.26, *SE* = 0.372, *z* = 3.390, *p* = 0.001
- **4 to 6 vs 1 to 3**: *β* = 0.52, *SE* = 0.334, *z* = 1.544, *p* = 0.122
- **SNR**: *β* = 0.91, *SE* = 0.084, *z* = 10.817, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.46 | 0.38 | 1.22 | 0.222 | 0.230 | n.s. |
| 1 to 3 - 3 to 5 | -1.26 | 0.37 | -3.39 | < .001 | 0.003 | ** |
| 1 to 3 - 4 to 6 | -0.52 | 0.33 | -1.54 | 0.122 | 0.230 | n.s. |
| 2 to 4 - 3 to 5 | -1.72 | 0.42 | -4.07 | < .001 | < .001 | *** |
| 2 to 4 - 4 to 6 | -0.97 | 0.40 | -2.46 | 0.014 | 0.054 | n.s. |
| 3 to 5 - 4 to 6 | 0.74 | 0.38 | 1.94 | 0.052 | 0.149 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 789.48, BIC = 806.98
- **2 to 4 vs 1 to 3**: *β* = 4.97, *SE* = 4.463, *z* = 1.113, *p* = 0.266
- **3 to 5 vs 1 to 3**: *β* = -1.51, *SE* = 4.644, *z* = -0.325, *p* = 0.745
- **4 to 6 vs 1 to 3**: *β* = 0.46, *SE* = 4.407, *z* = 0.103, *p* = 0.918
- **SNR**: *β* = 0.25, *SE* = 0.737, *z* = 0.340, *p* = 0.734

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -4.97 | 4.46 | -1.11 | 0.266 | 0.786 | n.s. |
| 1 to 3 - 3 to 5 | 1.51 | 4.64 | 0.32 | 0.745 | 0.963 | n.s. |
| 1 to 3 - 4 to 6 | -0.45 | 4.41 | -0.10 | 0.918 | 0.963 | n.s. |
| 2 to 4 - 3 to 5 | 6.48 | 4.50 | 1.44 | 0.150 | 0.624 | n.s. |
| 2 to 4 - 4 to 6 | 4.51 | 4.50 | 1.00 | 0.316 | 0.786 | n.s. |
| 3 to 5 - 4 to 6 | -1.96 | 4.56 | -0.43 | 0.667 | 0.963 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.443, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.35 | 19 | = 0.462 | -0.36 [-0.71, 0.19] | small | n.s. |
| 1 to 3 vs 3 to 5 | 0.11 | 19 | = 0.913 | 0.03 [-0.43, 0.46] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.38 | 19 | = 0.851 | -0.09 [-0.50, 0.39] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.63 | 19 | = 0.462 | 0.40 [-0.07, 0.87] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.24 | 19 | = 0.462 | 0.24 [-0.20, 0.75] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.51 | 19 | = 0.851 | -0.13 [-0.52, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 365.22, BIC = 382.71
- **2 to 4 vs 1 to 3**: *β* = -0.64, *SE* = 0.409, *z* = -1.554, *p* = 0.120
- **3 to 5 vs 1 to 3**: *β* = -0.06, *SE* = 0.426, *z* = -0.133, *p* = 0.894
- **4 to 6 vs 1 to 3**: *β* = -0.17, *SE* = 0.405, *z* = -0.411, *p* = 0.681
- **SNR**: *β* = -0.58, *SE* = 0.069, *z* = -8.389, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.64 | 0.41 | 1.55 | 0.120 | 0.536 | n.s. |
| 1 to 3 - 3 to 5 | 0.06 | 0.43 | 0.13 | 0.894 | 0.967 | n.s. |
| 1 to 3 - 4 to 6 | 0.17 | 0.40 | 0.41 | 0.681 | 0.967 | n.s. |
| 2 to 4 - 3 to 5 | -0.58 | 0.41 | -1.40 | 0.162 | 0.586 | n.s. |
| 2 to 4 - 4 to 6 | -0.47 | 0.41 | -1.14 | 0.256 | 0.693 | n.s. |
| 3 to 5 - 4 to 6 | 0.11 | 0.42 | 0.26 | 0.793 | 0.967 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.54, *p* = 0.214, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.28 | 19 | = 0.783 | -0.08 [-0.47, 0.42] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -2.34 | 19 | = 0.181 | -0.49 [-1.00, -0.05] | small | n.s. |
| 1 to 3 vs 4 to 6 | -0.68 | 19 | = 0.754 | -0.15 [-0.60, 0.29] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -1.50 | 19 | = 0.300 | -0.39 [-0.79, 0.14] | small | n.s. |
| 2 to 4 vs 4 to 6 | -0.38 | 19 | = 0.783 | -0.07 [-0.55, 0.38] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 1.84 | 19 | = 0.244 | 0.29 [-0.02, 0.94] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 429.22, BIC = 443.02
- **2 to 4 vs 1 to 3**: *β* = -1.29, *SE* = 4.663, *z* = -0.276, *p* = 0.782
- **3 to 5 vs 1 to 3**: *β* = 5.05, *SE* = 5.410, *z* = 0.934, *p* = 0.350
- **4 to 6 vs 1 to 3**: *β* = 5.50, *SE* = 4.979, *z* = 1.105, *p* = 0.269
- **SNR**: *β* = -0.89, *SE* = 1.308, *z* = -0.683, *p* = 0.495

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 1.29 | 4.66 | 0.28 | 0.782 | 0.953 | n.s. |
| 1 to 3 - 3 to 5 | -5.05 | 5.41 | -0.93 | 0.350 | 0.726 | n.s. |
| 1 to 3 - 4 to 6 | -5.50 | 4.98 | -1.10 | 0.269 | 0.715 | n.s. |
| 2 to 4 - 3 to 5 | -6.34 | 4.49 | -1.41 | 0.157 | 0.575 | n.s. |
| 2 to 4 - 4 to 6 | -6.79 | 4.21 | -1.61 | 0.107 | 0.493 | n.s. |
| 3 to 5 - 4 to 6 | -0.45 | 4.48 | -0.10 | 0.920 | 0.953 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 190.59, BIC = 204.38
- **2 to 4 vs 1 to 3**: *β* = -0.21, *SE* = 0.465, *z* = -0.453, *p* = 0.650
- **3 to 5 vs 1 to 3**: *β* = 0.18, *SE* = 0.506, *z* = 0.350, *p* = 0.726
- **4 to 6 vs 1 to 3**: *β* = 0.43, *SE* = 0.488, *z* = 0.890, *p* = 0.373
- **SNR**: *β* = 0.32, *SE* = 0.130, *z* = 2.481, *p* = 0.013

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.21 | 0.46 | 0.45 | 0.650 | 0.917 | n.s. |
| 1 to 3 - 3 to 5 | -0.18 | 0.51 | -0.35 | 0.726 | 0.917 | n.s. |
| 1 to 3 - 4 to 6 | -0.43 | 0.49 | -0.89 | 0.373 | 0.903 | n.s. |
| 2 to 4 - 3 to 5 | -0.39 | 0.44 | -0.88 | 0.379 | 0.903 | n.s. |
| 2 to 4 - 4 to 6 | -0.65 | 0.43 | -1.51 | 0.131 | 0.570 | n.s. |
| 3 to 5 - 4 to 6 | -0.26 | 0.45 | -0.58 | 0.564 | 0.917 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 787.49, BIC = 803.53
- **2 to 4 vs 1 to 3**: *β* = -3.80, *SE* = 15.750, *z* = -0.242, *p* = 0.809
- **3 to 5 vs 1 to 3**: *β* = -3.50, *SE* = 15.978, *z* = -0.219, *p* = 0.827
- **4 to 6 vs 1 to 3**: *β* = -1.89, *SE* = 15.744, *z* = -0.120, *p* = 0.904
- **SNR**: *β* = -0.28, *SE* = 1.723, *z* = -0.162, *p* = 0.871

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 3.80 | 15.75 | 0.24 | 0.809 | 1.000 | n.s. |
| 1 to 3 - 3 to 5 | 3.50 | 15.98 | 0.22 | 0.827 | 1.000 | n.s. |
| 1 to 3 - 4 to 6 | 1.89 | 15.74 | 0.12 | 0.904 | 1.000 | n.s. |
| 2 to 4 - 3 to 5 | -0.30 | 16.45 | -0.02 | 0.985 | 1.000 | n.s. |
| 2 to 4 - 4 to 6 | -1.91 | 16.23 | -0.12 | 0.906 | 1.000 | n.s. |
| 3 to 5 - 4 to 6 | -1.61 | 16.36 | -0.10 | 0.922 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.02, *p* = 0.995, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.03 | 14 | = 0.979 | -0.01 [-0.48, 0.55] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -0.20 | 14 | = 0.979 | -0.07 [-0.46, 0.57] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.19 | 14 | = 0.979 | -0.08 [-0.50, 0.50] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -0.14 | 14 | = 0.979 | -0.05 [-0.46, 0.61] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | -0.22 | 14 | = 0.979 | -0.06 [-0.69, 0.38] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -0.03 | 14 | = 0.979 | -0.01 [-0.42, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.23, BIC = 331.26
- **2 to 4 vs 1 to 3**: *β* = 0.71, *SE* = 0.495, *z* = 1.440, *p* = 0.150
- **3 to 5 vs 1 to 3**: *β* = 0.33, *SE* = 0.503, *z* = 0.661, *p* = 0.509
- **4 to 6 vs 1 to 3**: *β* = 0.16, *SE* = 0.490, *z* = 0.324, *p* = 0.746
- **SNR**: *β* = 0.62, *SE* = 0.065, *z* = 9.641, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -0.71 | 0.50 | -1.44 | 0.150 | 0.622 | n.s. |
| 1 to 3 - 3 to 5 | -0.33 | 0.50 | -0.66 | 0.509 | 0.916 | n.s. |
| 1 to 3 - 4 to 6 | -0.16 | 0.49 | -0.32 | 0.746 | 0.929 | n.s. |
| 2 to 4 - 3 to 5 | 0.38 | 0.52 | 0.74 | 0.462 | 0.916 | n.s. |
| 2 to 4 - 4 to 6 | 0.55 | 0.51 | 1.09 | 0.277 | 0.802 | n.s. |
| 3 to 5 - 4 to 6 | 0.17 | 0.51 | 0.34 | 0.734 | 0.929 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.77, *p* = 0.519, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.84 | 14 | = 0.825 | -0.24 [-0.72, 0.31] | small | n.s. |
| 1 to 3 vs 3 to 5 | 0.21 | 14 | = 0.971 | 0.06 [-0.42, 0.61] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | 0.37 | 14 | = 0.971 | 0.07 [-0.37, 0.62] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.19 | 14 | = 0.763 | 0.31 [-0.19, 0.91] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.39 | 14 | = 0.763 | 0.33 [-0.22, 0.88] | small | n.s. |
| 3 to 5 vs 4 to 6 | 0.04 | 14 | = 0.971 | 0.01 [-0.50, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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
