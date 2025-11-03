# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:42:36

---

## 1. Analysis Overview

**Total Measurements:** 448
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 1 to 2 | 12 | 101.67 ms | 9.72 | 2.81 | [84.00, 112.00] |
| 2 to 3 | 11 | 96.73 ms | 11.43 | 3.45 | [84.00, 112.00] |
| 3 to 4 | 8 | 99.00 ms | 12.96 | 4.58 | [84.00, 112.00] |
| 4 to 5 | 7 | 102.29 ms | 10.55 | 3.99 | [84.00, 112.00] |
| 5 to 6 | 3 | 93.33 ms | 16.17 | 9.33 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 2.65 µV | 1.96 | 0.57 | [0.61, 5.82] |
| 2 to 3 | 11 | 2.17 µV | 1.44 | 0.44 | [0.25, 5.40] |
| 3 to 4 | 8 | 2.35 µV | 1.93 | 0.68 | [0.94, 6.90] |
| 4 to 5 | 7 | 3.26 µV | 1.55 | 0.59 | [1.77, 5.87] |
| 5 to 6 | 3 | 2.87 µV | 1.30 | 0.75 | [1.59, 4.19] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | 171.45 ms | 17.47 | 3.72 | [144.00, 204.00] |
| 2 to 3 | 21 | 168.57 ms | 18.03 | 3.94 | [136.00, 204.00] |
| 3 to 4 | 23 | 166.78 ms | 18.15 | 3.78 | [140.00, 204.00] |
| 4 to 5 | 22 | 167.09 ms | 19.75 | 4.21 | [136.00, 196.00] |
| 5 to 6 | 12 | 169.67 ms | 24.57 | 7.09 | [136.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | -5.80 µV | 2.14 | 0.46 | [-10.03, -2.38] |
| 2 to 3 | 21 | -5.64 µV | 1.80 | 0.39 | [-10.61, -2.59] |
| 3 to 4 | 23 | -5.92 µV | 2.07 | 0.43 | [-10.53, -2.95] |
| 4 to 5 | 22 | -7.36 µV | 3.59 | 0.76 | [-16.53, -2.59] |
| 5 to 6 | 12 | -7.26 µV | 2.89 | 0.83 | [-12.77, -1.43] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 97.23 ms | 13.60 | 3.77 | [84.00, 116.00] |
| 2 to 3 | 11 | 102.18 ms | 13.07 | 3.94 | [84.00, 116.00] |
| 3 to 4 | 15 | 102.13 ms | 10.78 | 2.78 | [84.00, 116.00] |
| 4 to 5 | 15 | 100.53 ms | 9.18 | 2.37 | [84.00, 116.00] |
| 5 to 6 | 13 | 100.62 ms | 10.56 | 2.93 | [84.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 2.26 µV | 1.26 | 0.35 | [0.62, 4.29] |
| 2 to 3 | 11 | 3.61 µV | 1.78 | 0.54 | [1.63, 6.87] |
| 3 to 4 | 15 | 3.39 µV | 1.92 | 0.50 | [1.27, 7.39] |
| 4 to 5 | 15 | 5.60 µV | 5.16 | 1.33 | [1.25, 19.20] |
| 5 to 6 | 13 | 5.69 µV | 4.08 | 1.13 | [1.02, 16.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 488.00 ms | 34.41 | 8.35 | [440.00, 536.00] |
| 2 to 3 | 18 | 474.00 ms | 33.13 | 7.81 | [440.00, 536.00] |
| 3 to 4 | 16 | 499.25 ms | 34.39 | 8.60 | [440.00, 536.00] |
| 4 to 5 | 16 | 507.00 ms | 26.31 | 6.58 | [456.00, 536.00] |
| 5 to 6 | 9 | 498.22 ms | 38.01 | 12.67 | [440.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 5.69 µV | 2.95 | 0.72 | [1.78, 11.52] |
| 2 to 3 | 18 | 6.11 µV | 3.49 | 0.82 | [1.82, 13.70] |
| 3 to 4 | 16 | 6.90 µV | 3.00 | 0.75 | [2.27, 12.86] |
| 4 to 5 | 16 | 7.49 µV | 3.86 | 0.97 | [1.17, 13.88] |
| 5 to 6 | 9 | 8.09 µV | 3.98 | 1.33 | [5.11, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 326.34, BIC = 340.05
- **2 to 3 vs 1 to 2**: *β* = -4.98, *SE* = 4.446, *z* = -1.119, *p* = 0.263
- **3 to 4 vs 1 to 2**: *β* = -2.99, *SE* = 4.414, *z* = -0.678, *p* = 0.498
- **4 to 5 vs 1 to 2**: *β* = 0.48, *SE* = 5.053, *z* = 0.095, *p* = 0.924
- **5 to 6 vs 1 to 2**: *β* = -8.77, *SE* = 6.814, *z* = -1.287, *p* = 0.198
- **SNR**: *β* = -0.83, *SE* = 1.125, *z* = -0.739, *p* = 0.460

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 4.98 | 4.45 | 1.12 | 0.263 | 0.913 | n.s. |
| 1 to 2 - 3 to 4 | 2.99 | 4.41 | 0.68 | 0.498 | 0.968 | n.s. |
| 1 to 2 - 4 to 5 | -0.48 | 5.05 | -0.10 | 0.924 | 0.968 | n.s. |
| 1 to 2 - 5 to 6 | 8.77 | 6.81 | 1.29 | 0.198 | 0.890 | n.s. |
| 2 to 3 - 3 to 4 | -1.98 | 4.52 | -0.44 | 0.661 | 0.968 | n.s. |
| 2 to 3 - 4 to 5 | -5.46 | 5.14 | -1.06 | 0.288 | 0.913 | n.s. |
| 2 to 3 - 5 to 6 | 3.79 | 6.87 | 0.55 | 0.581 | 0.968 | n.s. |
| 3 to 4 - 4 to 5 | -3.47 | 5.26 | -0.66 | 0.509 | 0.968 | n.s. |
| 3 to 4 - 5 to 6 | 5.78 | 6.47 | 0.89 | 0.372 | 0.939 | n.s. |
| 4 to 5 - 5 to 6 | 9.25 | 7.21 | 1.28 | 0.199 | 0.890 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 141.54, BIC = 155.25
- **2 to 3 vs 1 to 2**: *β* = -0.48, *SE* = 0.449, *z* = -1.070, *p* = 0.285
- **3 to 4 vs 1 to 2**: *β* = 0.04, *SE* = 0.496, *z* = 0.086, *p* = 0.932
- **4 to 5 vs 1 to 2**: *β* = 0.64, *SE* = 0.523, *z* = 1.220, *p* = 0.222
- **5 to 6 vs 1 to 2**: *β* = 0.79, *SE* = 0.743, *z* = 1.063, *p* = 0.288
- **SNR**: *β* = 0.83, *SE* = 0.127, *z* = 6.531, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 0.48 | 0.45 | 1.07 | 0.285 | 0.904 | n.s. |
| 1 to 2 - 3 to 4 | -0.04 | 0.50 | -0.09 | 0.932 | 0.979 | n.s. |
| 1 to 2 - 4 to 5 | -0.64 | 0.52 | -1.22 | 0.222 | 0.866 | n.s. |
| 1 to 2 - 5 to 6 | -0.79 | 0.74 | -1.06 | 0.288 | 0.904 | n.s. |
| 2 to 3 - 3 to 4 | -0.52 | 0.51 | -1.02 | 0.307 | 0.904 | n.s. |
| 2 to 3 - 4 to 5 | -1.12 | 0.53 | -2.10 | 0.036 | 0.306 | n.s. |
| 2 to 3 - 5 to 6 | -1.27 | 0.76 | -1.67 | 0.095 | 0.593 | n.s. |
| 3 to 4 - 4 to 5 | -0.60 | 0.58 | -1.02 | 0.308 | 0.904 | n.s. |
| 3 to 4 - 5 to 6 | -0.75 | 0.74 | -1.01 | 0.315 | 0.904 | n.s. |
| 4 to 5 - 5 to 6 | -0.15 | 0.84 | -0.18 | 0.856 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 856.05, BIC = 876.89
- **2 to 3 vs 1 to 2**: *β* = -1.23, *SE* = 4.111, *z* = -0.299, *p* = 0.765
- **3 to 4 vs 1 to 2**: *β* = -4.50, *SE* = 3.988, *z* = -1.127, *p* = 0.260
- **4 to 5 vs 1 to 2**: *β* = -3.84, *SE* = 4.042, *z* = -0.949, *p* = 0.342
- **5 to 6 vs 1 to 2**: *β* = 0.36, *SE* = 5.101, *z* = 0.071, *p* = 0.943
- **SNR**: *β* = 0.90, *SE* = 0.587, *z* = 1.533, *p* = 0.125

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 1.23 | 4.11 | 0.30 | 0.765 | 0.996 | n.s. |
| 1 to 2 - 3 to 4 | 4.50 | 3.99 | 1.13 | 0.260 | 0.950 | n.s. |
| 1 to 2 - 4 to 5 | 3.84 | 4.04 | 0.95 | 0.342 | 0.973 | n.s. |
| 1 to 2 - 5 to 6 | -0.36 | 5.10 | -0.07 | 0.943 | 0.996 | n.s. |
| 2 to 3 - 3 to 4 | 3.26 | 4.02 | 0.81 | 0.417 | 0.977 | n.s. |
| 2 to 3 - 4 to 5 | 2.61 | 4.10 | 0.64 | 0.524 | 0.977 | n.s. |
| 2 to 3 - 5 to 6 | -1.59 | 5.04 | -0.32 | 0.752 | 0.996 | n.s. |
| 3 to 4 - 4 to 5 | -0.66 | 4.02 | -0.16 | 0.870 | 0.996 | n.s. |
| 3 to 4 - 5 to 6 | -4.86 | 4.98 | -0.98 | 0.329 | 0.973 | n.s. |
| 4 to 5 - 5 to 6 | -4.20 | 5.16 | -0.81 | 0.416 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.11, *p* = 0.367, η²_G = 0.042
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.97 | 9 | = 0.578 | -0.28 [-0.48, 0.48] | small | n.s. |
| 1 to 2 vs 3 to 4 | 1.33 | 9 | = 0.578 | 0.30 [-0.20, 0.73] | small | n.s. |
| 1 to 2 vs 4 to 5 | 0.95 | 9 | = 0.578 | 0.30 [-0.34, 0.60] | small | n.s. |
| 1 to 2 vs 5 to 6 | 0.10 | 9 | = 1.000 | 0.04 [-0.61, 0.73] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 1.53 | 9 | = 0.578 | 0.55 [-0.31, 0.61] | medium | n.s. |
| 2 to 3 vs 4 to 5 | 1.69 | 9 | = 0.578 | 0.55 [-0.38, 0.56] | medium | n.s. |
| 2 to 3 vs 5 to 6 | 0.77 | 9 | = 0.578 | 0.27 [-0.46, 0.82] | small | n.s. |
| 3 to 4 vs 4 to 5 | 0.00 | 9 | = 1.000 | 0.00 [-0.67, 0.25] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | -0.86 | 9 | = 0.578 | -0.22 [-0.83, 0.45] | small | n.s. |
| 4 to 5 vs 5 to 6 | -1.19 | 9 | = 0.578 | -0.22 [-1.14, 0.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 441.22, BIC = 462.06
- **2 to 3 vs 1 to 2**: *β* = 0.24, *SE* = 0.528, *z* = 0.461, *p* = 0.645
- **3 to 4 vs 1 to 2**: *β* = -0.14, *SE* = 0.514, *z* = -0.273, *p* = 0.785
- **4 to 5 vs 1 to 2**: *β* = -1.40, *SE* = 0.520, *z* = -2.690, *p* = 0.007
- **5 to 6 vs 1 to 2**: *β* = -2.07, *SE* = 0.653, *z* = -3.162, *p* = 0.002
- **SNR**: *β* = -0.34, *SE* = 0.074, *z* = -4.622, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.24 | 0.53 | -0.46 | 0.645 | 0.874 | n.s. |
| 1 to 2 - 3 to 4 | 0.14 | 0.51 | 0.27 | 0.785 | 0.874 | n.s. |
| 1 to 2 - 4 to 5 | 1.40 | 0.52 | 2.69 | 0.007 | 0.042 | * |
| 1 to 2 - 5 to 6 | 2.07 | 0.65 | 3.16 | 0.002 | 0.014 | * |
| 2 to 3 - 3 to 4 | 0.38 | 0.52 | 0.74 | 0.459 | 0.841 | n.s. |
| 2 to 3 - 4 to 5 | 1.64 | 0.53 | 3.12 | 0.002 | 0.015 | * |
| 2 to 3 - 5 to 6 | 2.31 | 0.65 | 3.56 | < .001 | 0.004 | ** |
| 3 to 4 - 4 to 5 | 1.26 | 0.52 | 2.43 | 0.015 | 0.072 | n.s. |
| 3 to 4 - 5 to 6 | 1.93 | 0.64 | 3.02 | 0.003 | 0.018 | * |
| 4 to 5 - 5 to 6 | 0.67 | 0.66 | 1.01 | 0.313 | 0.778 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.65, *p* = 0.183, η²_G = 0.068
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.21 | 9 | = 0.839 | -0.05 [-0.79, 0.20] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -1.11 | 9 | = 0.448 | -0.20 [-0.44, 0.47] | small | n.s. |
| 1 to 2 vs 4 to 5 | 1.51 | 9 | = 0.448 | 0.47 [-0.03, 0.96] | small | n.s. |
| 1 to 2 vs 5 to 6 | 1.10 | 9 | = 0.448 | 0.35 [-0.37, 1.01] | small | n.s. |
| 2 to 3 vs 3 to 4 | -0.62 | 9 | = 0.685 | -0.17 [-0.33, 0.59] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 1.39 | 9 | = 0.448 | 0.54 [0.04, 1.04] | medium | n.s. |
| 2 to 3 vs 5 to 6 | 1.07 | 9 | = 0.448 | 0.41 [-0.24, 1.08] | small | n.s. |
| 3 to 4 vs 4 to 5 | 1.91 | 9 | = 0.448 | 0.64 [0.08, 1.06] | medium | n.s. |
| 3 to 4 vs 5 to 6 | 1.52 | 9 | = 0.448 | 0.51 [-0.09, 1.29] | medium | n.s. |
| 4 to 5 vs 5 to 6 | -0.33 | 9 | = 0.829 | -0.10 [-0.65, 0.69] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 522.22, BIC = 539.85
- **2 to 3 vs 1 to 2**: *β* = 4.23, *SE* = 3.786, *z* = 1.118, *p* = 0.264
- **3 to 4 vs 1 to 2**: *β* = 6.02, *SE* = 3.619, *z* = 1.663, *p* = 0.096
- **4 to 5 vs 1 to 2**: *β* = 2.76, *SE* = 3.567, *z* = 0.775, *p* = 0.438
- **5 to 6 vs 1 to 2**: *β* = 2.21, *SE* = 3.808, *z* = 0.580, *p* = 0.562
- **SNR**: *β* = -0.61, *SE* = 0.832, *z* = -0.737, *p* = 0.461

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -4.23 | 3.79 | -1.12 | 0.264 | 0.936 | n.s. |
| 1 to 2 - 3 to 4 | -6.02 | 3.62 | -1.66 | 0.096 | 0.637 | n.s. |
| 1 to 2 - 4 to 5 | -2.76 | 3.57 | -0.77 | 0.438 | 0.969 | n.s. |
| 1 to 2 - 5 to 6 | -2.21 | 3.81 | -0.58 | 0.562 | 0.984 | n.s. |
| 2 to 3 - 3 to 4 | -1.79 | 3.81 | -0.47 | 0.639 | 0.984 | n.s. |
| 2 to 3 - 4 to 5 | 1.47 | 3.75 | 0.39 | 0.695 | 0.984 | n.s. |
| 2 to 3 - 5 to 6 | 2.02 | 4.00 | 0.51 | 0.613 | 0.984 | n.s. |
| 3 to 4 - 4 to 5 | 3.25 | 3.51 | 0.93 | 0.354 | 0.953 | n.s. |
| 3 to 4 - 5 to 6 | 3.81 | 3.80 | 1.00 | 0.316 | 0.952 | n.s. |
| 4 to 5 - 5 to 6 | 0.56 | 3.63 | 0.15 | 0.878 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.02, *p* = 0.045, η²_G = 0.621
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -5.20 | 2 | = 0.175 | -3.29 [-1.10, 0.47] | large | n.s. |
| 1 to 2 vs 3 to 4 | -5.20 | 2 | = 0.175 | -5.20 [-1.88, -0.03] | large | n.s. |
| 1 to 2 vs 4 to 5 | -1.96 | 2 | = 0.471 | -1.24 [-1.25, 0.36] | large | n.s. |
| 1 to 2 vs 5 to 6 | -3.05 | 2 | = 0.309 | -2.18 [-1.28, 0.84] | large | n.s. |
| 2 to 3 vs 3 to 4 | 0.00 | 2 | = 1.000 | 0.00 [-1.11, 0.59] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 1.13 | 2 | = 0.528 | 1.07 [-0.65, 1.04] | large | n.s. |
| 2 to 3 vs 5 to 6 | 1.00 | 2 | = 0.528 | 1.06 [-0.94, 1.61] | large | n.s. |
| 3 to 4 vs 4 to 5 | 1.19 | 2 | = 0.528 | 1.24 [-0.11, 1.47] | large | n.s. |
| 3 to 4 vs 5 to 6 | 1.26 | 2 | = 0.528 | 1.39 [-0.19, 2.02] | large | n.s. |
| 4 to 5 vs 5 to 6 | -0.76 | 2 | = 0.587 | -0.25 [-0.72, 0.96] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 314.56, BIC = 332.20
- **2 to 3 vs 1 to 2**: *β* = 1.11, *SE* = 0.654, *z* = 1.700, *p* = 0.089
- **3 to 4 vs 1 to 2**: *β* = 0.74, *SE* = 0.629, *z* = 1.175, *p* = 0.240
- **4 to 5 vs 1 to 2**: *β* = 2.42, *SE* = 0.629, *z* = 3.854, *p* < .001
- **5 to 6 vs 1 to 2**: *β* = 2.10, *SE* = 0.687, *z* = 3.058, *p* = 0.002
- **SNR**: *β* = 0.86, *SE* = 0.148, *z* = 5.840, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -1.11 | 0.65 | -1.70 | 0.089 | 0.373 | n.s. |
| 1 to 2 - 3 to 4 | -0.74 | 0.63 | -1.18 | 0.240 | 0.561 | n.s. |
| 1 to 2 - 4 to 5 | -2.42 | 0.63 | -3.85 | < .001 | 0.001 | ** |
| 1 to 2 - 5 to 6 | -2.10 | 0.69 | -3.06 | 0.002 | 0.020 | * |
| 2 to 3 - 3 to 4 | 0.37 | 0.66 | 0.57 | 0.571 | 0.816 | n.s. |
| 2 to 3 - 4 to 5 | -1.31 | 0.66 | -1.98 | 0.047 | 0.265 | n.s. |
| 2 to 3 - 5 to 6 | -0.99 | 0.72 | -1.36 | 0.173 | 0.532 | n.s. |
| 3 to 4 - 4 to 5 | -1.69 | 0.61 | -2.77 | 0.006 | 0.044 | * |
| 3 to 4 - 5 to 6 | -1.36 | 0.67 | -2.02 | 0.043 | 0.265 | n.s. |
| 4 to 5 - 5 to 6 | 0.32 | 0.65 | 0.50 | 0.617 | 0.816 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.19, *p* = 0.938, η²_G = 0.053
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.16 | 2 | = 0.923 | -0.16 [-1.38, 0.27] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -0.43 | 2 | = 0.923 | -0.26 [-1.45, 0.22] | small | n.s. |
| 1 to 2 vs 4 to 5 | -0.13 | 2 | = 0.923 | -0.04 [-1.41, 0.25] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -0.91 | 2 | = 0.923 | -0.57 [-1.76, 0.53] | medium | n.s. |
| 2 to 3 vs 3 to 4 | -0.26 | 2 | = 0.923 | -0.20 [-0.85, 0.83] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.17 | 2 | = 0.923 | 0.16 [-1.20, 0.52] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | -0.78 | 2 | = 0.923 | -0.90 [-2.08, 0.69] | large | n.s. |
| 3 to 4 vs 4 to 5 | 0.49 | 2 | = 0.923 | 0.26 [-1.09, 0.39] | small | n.s. |
| 3 to 4 vs 5 to 6 | -0.11 | 2 | = 0.923 | -0.10 [-1.81, 0.29] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -1.09 | 2 | = 0.923 | -0.74 [-0.77, 0.91] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 756.71, BIC = 775.36
- **2 to 3 vs 1 to 2**: *β* = -14.17, *SE* = 10.367, *z* = -1.367, *p* = 0.172
- **3 to 4 vs 1 to 2**: *β* = 11.05, *SE* = 10.692, *z* = 1.034, *p* = 0.301
- **4 to 5 vs 1 to 2**: *β* = 20.06, *SE* = 10.678, *z* = 1.879, *p* = 0.060
- **5 to 6 vs 1 to 2**: *β* = 11.96, *SE* = 12.939, *z* = 0.924, *p* = 0.355
- **SNR**: *β* = 0.49, *SE* = 1.181, *z* = 0.419, *p* = 0.676

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 14.17 | 10.37 | 1.37 | 0.172 | 0.677 | n.s. |
| 1 to 2 - 3 to 4 | -11.05 | 10.69 | -1.03 | 0.301 | 0.833 | n.s. |
| 1 to 2 - 4 to 5 | -20.06 | 10.68 | -1.88 | 0.060 | 0.353 | n.s. |
| 1 to 2 - 5 to 6 | -11.96 | 12.94 | -0.92 | 0.355 | 0.833 | n.s. |
| 2 to 3 - 3 to 4 | -25.23 | 10.46 | -2.41 | 0.016 | 0.134 | n.s. |
| 2 to 3 - 4 to 5 | -34.23 | 10.64 | -3.22 | 0.001 | 0.013 | * |
| 2 to 3 - 5 to 6 | -26.13 | 13.06 | -2.00 | 0.045 | 0.310 | n.s. |
| 3 to 4 - 4 to 5 | -9.01 | 10.94 | -0.82 | 0.410 | 0.833 | n.s. |
| 3 to 4 - 5 to 6 | -0.91 | 13.36 | -0.07 | 0.946 | 0.946 | n.s. |
| 4 to 5 - 5 to 6 | 8.10 | 12.87 | 0.63 | 0.529 | 0.833 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.231, η²_G = 0.155
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.15 | 6 | = 0.884 | -0.05 [-0.48, 0.67] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -1.16 | 6 | = 0.564 | -0.53 [-0.87, 0.36] | medium | n.s. |
| 1 to 2 vs 4 to 5 | -2.72 | 6 | = 0.348 | -1.49 [-1.27, 0.05] | large | n.s. |
| 1 to 2 vs 5 to 6 | -1.15 | 6 | = 0.564 | -0.70 [-1.33, 0.42] | medium | n.s. |
| 2 to 3 vs 3 to 4 | -0.77 | 6 | = 0.639 | -0.40 [-0.99, 0.21] | small | n.s. |
| 2 to 3 vs 4 to 5 | -1.95 | 6 | = 0.495 | -1.07 [-1.63, -0.19] | large | n.s. |
| 2 to 3 vs 5 to 6 | -1.13 | 6 | = 0.564 | -0.55 [-1.42, 0.37] | medium | n.s. |
| 3 to 4 vs 4 to 5 | -1.04 | 6 | = 0.564 | -0.59 [-0.72, 0.49] | medium | n.s. |
| 3 to 4 vs 5 to 6 | -0.31 | 6 | = 0.851 | -0.15 [-1.05, 0.81] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | 0.70 | 6 | = 0.639 | 0.40 [-0.44, 1.14] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 389.70, BIC = 408.35
- **2 to 3 vs 1 to 2**: *β* = 0.15, *SE* = 0.861, *z* = 0.179, *p* = 0.858
- **3 to 4 vs 1 to 2**: *β* = 0.61, *SE* = 0.890, *z* = 0.687, *p* = 0.492
- **4 to 5 vs 1 to 2**: *β* = 2.06, *SE* = 0.881, *z* = 2.337, *p* = 0.019
- **5 to 6 vs 1 to 2**: *β* = 2.96, *SE* = 1.081, *z* = 2.738, *p* = 0.006
- **SNR**: *β* = 0.45, *SE* = 0.105, *z* = 4.218, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.15 | 0.86 | -0.18 | 0.858 | 0.869 | n.s. |
| 1 to 2 - 3 to 4 | -0.61 | 0.89 | -0.69 | 0.492 | 0.869 | n.s. |
| 1 to 2 - 4 to 5 | -2.06 | 0.88 | -2.34 | 0.019 | 0.145 | n.s. |
| 1 to 2 - 5 to 6 | -2.96 | 1.08 | -2.74 | 0.006 | 0.060 | n.s. |
| 2 to 3 - 3 to 4 | -0.46 | 0.86 | -0.53 | 0.597 | 0.869 | n.s. |
| 2 to 3 - 4 to 5 | -1.90 | 0.88 | -2.16 | 0.031 | 0.197 | n.s. |
| 2 to 3 - 5 to 6 | -2.80 | 1.10 | -2.54 | 0.011 | 0.095 | n.s. |
| 3 to 4 - 4 to 5 | -1.45 | 0.91 | -1.60 | 0.110 | 0.443 | n.s. |
| 3 to 4 - 5 to 6 | -2.35 | 1.13 | -2.08 | 0.038 | 0.206 | n.s. |
| 4 to 5 - 5 to 6 | -0.90 | 1.07 | -0.84 | 0.399 | 0.869 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.42, *p* = 0.076, η²_G = 0.170
- Greenhouse-Geisser corrected: *p* = 0.149 (ε = 0.383)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -3.19 | 6 | = 0.063 | -1.06 [-1.01, 0.19] | large | n.s. |
| 1 to 2 vs 3 to 4 | -4.90 | 6 | = 0.014 | -1.05 [-0.82, 0.40] | large | * |
| 1 to 2 vs 4 to 5 | -4.90 | 6 | = 0.014 | -1.69 [-1.04, 0.22] | large | * |
| 1 to 2 vs 5 to 6 | -1.91 | 6 | = 0.261 | -0.81 [-1.79, 0.15] | large | n.s. |
| 2 to 3 vs 3 to 4 | -0.27 | 6 | = 0.993 | -0.08 [-0.74, 0.42] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | -0.98 | 6 | = 0.730 | -0.42 [-0.82, 0.40] | small | n.s. |
| 2 to 3 vs 5 to 6 | -0.12 | 6 | = 0.996 | -0.06 [-0.92, 0.75] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | -0.59 | 6 | = 0.843 | -0.29 [-0.78, 0.44] | small | n.s. |
| 3 to 4 vs 5 to 6 | -0.00 | 6 | = 0.996 | -0.00 [-0.93, 0.92] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | 0.57 | 6 | = 0.843 | 0.21 [-0.51, 1.05] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Significant main effect of condition (*p* = 0.045) (no significant pairwise comparisons)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.076)

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
