# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:41:36

---

## 1. Analysis Overview

**Total Measurements:** 480
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
| 1 to 2 | 12 | 98.33 ms | 8.77 | 2.53 | [84.00, 108.00] |
| 2 to 3 | 7 | 98.29 ms | 12.19 | 4.61 | [84.00, 108.00] |
| 3 to 4 | 7 | 86.29 ms | 3.15 | 1.19 | [84.00, 92.00] |
| 4 to 5 | 10 | 102.40 ms | 8.68 | 2.75 | [84.00, 108.00] |
| 5 to 6 | 10 | 92.40 ms | 10.91 | 3.45 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 2.57 µV | 1.94 | 0.56 | [0.68, 5.82] |
| 2 to 3 | 7 | 2.41 µV | 1.21 | 0.46 | [0.66, 4.30] |
| 3 to 4 | 7 | 2.14 µV | 1.60 | 0.61 | [0.78, 5.42] |
| 4 to 5 | 10 | 2.44 µV | 1.48 | 0.47 | [0.73, 5.59] |
| 5 to 6 | 10 | 1.85 µV | 1.15 | 0.36 | [0.36, 3.74] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | 168.00 ms | 15.18 | 3.31 | [144.00, 196.00] |
| 2 to 3 | 22 | 171.09 ms | 18.64 | 3.97 | [140.00, 204.00] |
| 3 to 4 | 22 | 164.18 ms | 16.54 | 3.53 | [140.00, 204.00] |
| 4 to 5 | 23 | 166.78 ms | 19.24 | 4.01 | [140.00, 204.00] |
| 5 to 6 | 22 | 173.82 ms | 17.14 | 3.65 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | -5.63 µV | 2.29 | 0.50 | [-9.95, -2.19] |
| 2 to 3 | 22 | -5.26 µV | 1.96 | 0.42 | [-10.61, -0.91] |
| 3 to 4 | 22 | -5.67 µV | 2.24 | 0.48 | [-10.31, -2.95] |
| 4 to 5 | 23 | -5.78 µV | 2.73 | 0.57 | [-11.05, -1.20] |
| 5 to 6 | 22 | -6.17 µV | 2.42 | 0.52 | [-11.88, -2.32] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 99.38 ms | 11.18 | 3.10 | [84.00, 112.00] |
| 2 to 3 | 11 | 102.55 ms | 9.51 | 2.87 | [84.00, 112.00] |
| 3 to 4 | 16 | 97.75 ms | 11.68 | 2.92 | [84.00, 112.00] |
| 4 to 5 | 14 | 102.29 ms | 9.11 | 2.43 | [84.00, 112.00] |
| 5 to 6 | 12 | 96.00 ms | 9.50 | 2.74 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 2.14 µV | 1.54 | 0.43 | [0.56, 4.57] |
| 2 to 3 | 11 | 3.17 µV | 1.75 | 0.53 | [0.75, 6.87] |
| 3 to 4 | 16 | 3.26 µV | 1.82 | 0.45 | [0.56, 7.39] |
| 4 to 5 | 14 | 3.80 µV | 3.17 | 0.85 | [1.14, 13.41] |
| 5 to 6 | 12 | 2.67 µV | 1.18 | 0.34 | [0.84, 4.39] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 489.41 ms | 36.71 | 8.90 | [440.00, 536.00] |
| 2 to 3 | 18 | 483.56 ms | 42.06 | 9.91 | [432.00, 536.00] |
| 3 to 4 | 17 | 490.82 ms | 37.97 | 9.21 | [432.00, 536.00] |
| 4 to 5 | 16 | 495.25 ms | 36.05 | 9.01 | [436.00, 536.00] |
| 5 to 6 | 9 | 485.78 ms | 36.83 | 12.28 | [448.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 5.48 µV | 3.09 | 0.75 | [1.68, 11.52] |
| 2 to 3 | 18 | 5.84 µV | 3.58 | 0.84 | [1.73, 13.70] |
| 3 to 4 | 17 | 6.01 µV | 3.17 | 0.77 | [1.82, 12.86] |
| 4 to 5 | 16 | 6.00 µV | 3.96 | 0.99 | [1.66, 16.10] |
| 5 to 6 | 9 | 4.78 µV | 2.65 | 0.88 | [1.73, 9.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 345.72, BIC = 360.35
- **2 to 3 vs 1 to 2**: *β* = 0.05, *SE* = 3.867, *z* = 0.014, *p* = 0.989
- **3 to 4 vs 1 to 2**: *β* = -12.24, *SE* = 4.057, *z* = -3.018, *p* = 0.003
- **4 to 5 vs 1 to 2**: *β* = 4.08, *SE* = 3.725, *z* = 1.094, *p* = 0.274
- **5 to 6 vs 1 to 2**: *β* = -6.53, *SE* = 3.422, *z* = -1.909, *p* = 0.056
- **SNR**: *β* = -0.62, *SE* = 0.723, *z* = -0.854, *p* = 0.393

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.05 | 3.87 | -0.01 | 0.989 | 0.989 | n.s. |
| 1 to 2 - 3 to 4 | 12.25 | 4.06 | 3.02 | 0.003 | 0.020 | * |
| 1 to 2 - 4 to 5 | -4.07 | 3.73 | -1.09 | 0.274 | 0.617 | n.s. |
| 1 to 2 - 5 to 6 | 6.53 | 3.42 | 1.91 | 0.056 | 0.251 | n.s. |
| 2 to 3 - 3 to 4 | 12.30 | 4.02 | 3.06 | 0.002 | 0.020 | * |
| 2 to 3 - 4 to 5 | -4.02 | 4.10 | -0.98 | 0.327 | 0.617 | n.s. |
| 2 to 3 - 5 to 6 | 6.59 | 3.04 | 2.17 | 0.030 | 0.168 | n.s. |
| 3 to 4 - 4 to 5 | -16.32 | 4.16 | -3.92 | < .001 | < .001 | *** |
| 3 to 4 - 5 to 6 | -5.71 | 4.25 | -1.34 | 0.179 | 0.546 | n.s. |
| 4 to 5 - 5 to 6 | 10.61 | 3.50 | 3.03 | 0.002 | 0.020 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 145.59, BIC = 160.22
- **2 to 3 vs 1 to 2**: *β* = -0.23, *SE* = 0.431, *z* = -0.528, *p* = 0.598
- **3 to 4 vs 1 to 2**: *β* = -0.24, *SE* = 0.442, *z* = -0.550, *p* = 0.583
- **4 to 5 vs 1 to 2**: *β* = -0.26, *SE* = 0.370, *z* = -0.711, *p* = 0.477
- **5 to 6 vs 1 to 2**: *β* = -0.19, *SE* = 0.395, *z* = -0.473, *p* = 0.636
- **SNR**: *β* = 0.60, *SE* = 0.081, *z* = 7.392, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 0.23 | 0.43 | 0.53 | 0.598 | 1.000 | n.s. |
| 1 to 2 - 3 to 4 | 0.24 | 0.44 | 0.55 | 0.583 | 1.000 | n.s. |
| 1 to 2 - 4 to 5 | 0.26 | 0.37 | 0.71 | 0.477 | 0.998 | n.s. |
| 1 to 2 - 5 to 6 | 0.19 | 0.40 | 0.47 | 0.636 | 1.000 | n.s. |
| 2 to 3 - 3 to 4 | 0.02 | 0.50 | 0.03 | 0.976 | 1.000 | n.s. |
| 2 to 3 - 4 to 5 | 0.04 | 0.45 | 0.08 | 0.937 | 1.000 | n.s. |
| 2 to 3 - 5 to 6 | -0.04 | 0.46 | -0.09 | 0.929 | 1.000 | n.s. |
| 3 to 4 - 4 to 5 | 0.02 | 0.45 | 0.04 | 0.964 | 1.000 | n.s. |
| 3 to 4 - 5 to 6 | -0.06 | 0.46 | -0.12 | 0.903 | 1.000 | n.s. |
| 4 to 5 - 5 to 6 | -0.08 | 0.41 | -0.18 | 0.854 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 920.34, BIC = 941.94
- **2 to 3 vs 1 to 2**: *β* = 3.46, *SE* = 3.824, *z* = 0.906, *p* = 0.365
- **3 to 4 vs 1 to 2**: *β* = -2.96, *SE* = 3.832, *z* = -0.771, *p* = 0.441
- **4 to 5 vs 1 to 2**: *β* = -1.16, *SE* = 3.756, *z* = -0.310, *p* = 0.757
- **5 to 6 vs 1 to 2**: *β* = 5.67, *SE* = 3.819, *z* = 1.486, *p* = 0.137
- **SNR**: *β* = 0.44, *SE* = 0.566, *z* = 0.773, *p* = 0.439

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -3.46 | 3.82 | -0.91 | 0.365 | 0.897 | n.s. |
| 1 to 2 - 3 to 4 | 2.95 | 3.83 | 0.77 | 0.441 | 0.902 | n.s. |
| 1 to 2 - 4 to 5 | 1.16 | 3.76 | 0.31 | 0.757 | 0.917 | n.s. |
| 1 to 2 - 5 to 6 | -5.67 | 3.82 | -1.49 | 0.137 | 0.644 | n.s. |
| 2 to 3 - 3 to 4 | 6.42 | 3.75 | 1.71 | 0.087 | 0.517 | n.s. |
| 2 to 3 - 4 to 5 | 4.63 | 3.71 | 1.25 | 0.212 | 0.761 | n.s. |
| 2 to 3 - 5 to 6 | -2.21 | 3.82 | -0.58 | 0.563 | 0.917 | n.s. |
| 3 to 4 - 4 to 5 | -1.79 | 3.71 | -0.48 | 0.630 | 0.917 | n.s. |
| 3 to 4 - 5 to 6 | -8.63 | 3.84 | -2.25 | 0.025 | 0.220 | n.s. |
| 4 to 5 - 5 to 6 | -6.84 | 3.73 | -1.83 | 0.067 | 0.464 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.41, *p* = 0.240, η²_G = 0.032
- Greenhouse-Geisser corrected: *p* = 0.257 (ε = 0.554)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | 0.10 | 17 | = 0.919 | 0.03 [-0.55, 0.38] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | 1.30 | 17 | = 0.525 | 0.26 [-0.23, 0.72] | small | n.s. |
| 1 to 2 vs 4 to 5 | 1.74 | 17 | = 0.494 | 0.35 [-0.40, 0.51] | small | n.s. |
| 1 to 2 vs 5 to 6 | -0.65 | 17 | = 0.584 | -0.17 [-0.77, 0.19] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 0.72 | 17 | = 0.584 | 0.21 [-0.22, 0.71] | small | n.s. |
| 2 to 3 vs 4 to 5 | 1.03 | 17 | = 0.548 | 0.29 [-0.17, 0.73] | small | n.s. |
| 2 to 3 vs 5 to 6 | -1.01 | 17 | = 0.548 | -0.17 [-0.67, 0.25] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 0.75 | 17 | = 0.584 | 0.09 [-0.62, 0.28] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | -1.51 | 17 | = 0.494 | -0.40 [-0.94, 0.02] | small | n.s. |
| 4 to 5 vs 5 to 6 | -1.95 | 17 | = 0.494 | -0.49 [-0.90, 0.03] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 402.83, BIC = 424.43
- **2 to 3 vs 1 to 2**: *β* = 0.16, *SE* = 0.339, *z* = 0.476, *p* = 0.634
- **3 to 4 vs 1 to 2**: *β* = -0.23, *SE* = 0.339, *z* = -0.666, *p* = 0.506
- **4 to 5 vs 1 to 2**: *β* = -0.23, *SE* = 0.332, *z* = -0.683, *p* = 0.495
- **5 to 6 vs 1 to 2**: *β* = -0.11, *SE* = 0.338, *z* = -0.335, *p* = 0.738
- **SNR**: *β* = -0.48, *SE* = 0.051, *z* = -9.370, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.16 | 0.34 | -0.48 | 0.634 | 0.993 | n.s. |
| 1 to 2 - 3 to 4 | 0.23 | 0.34 | 0.67 | 0.506 | 0.992 | n.s. |
| 1 to 2 - 4 to 5 | 0.23 | 0.33 | 0.68 | 0.495 | 0.992 | n.s. |
| 1 to 2 - 5 to 6 | 0.11 | 0.34 | 0.33 | 0.738 | 0.995 | n.s. |
| 2 to 3 - 3 to 4 | 0.39 | 0.33 | 1.17 | 0.244 | 0.933 | n.s. |
| 2 to 3 - 4 to 5 | 0.39 | 0.33 | 1.18 | 0.237 | 0.933 | n.s. |
| 2 to 3 - 5 to 6 | 0.27 | 0.34 | 0.81 | 0.418 | 0.987 | n.s. |
| 3 to 4 - 4 to 5 | 0.00 | 0.33 | 0.00 | 0.998 | 0.998 | n.s. |
| 3 to 4 - 5 to 6 | -0.11 | 0.34 | -0.33 | 0.740 | 0.995 | n.s. |
| 4 to 5 - 5 to 6 | -0.11 | 0.33 | -0.34 | 0.731 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.465, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.64 | 17 | = 0.598 | -0.34 [-0.85, 0.12] | small | n.s. |
| 1 to 2 vs 3 to 4 | -0.83 | 17 | = 0.743 | -0.17 [-0.53, 0.40] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.26 | 17 | = 0.875 | 0.06 [-0.40, 0.51] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | 0.40 | 17 | = 0.864 | 0.11 [-0.33, 0.61] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 0.55 | 17 | = 0.842 | 0.13 [-0.34, 0.57] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 1.22 | 17 | = 0.598 | 0.35 [-0.19, 0.71] | small | n.s. |
| 2 to 3 vs 5 to 6 | 1.53 | 17 | = 0.598 | 0.42 [-0.08, 0.87] | small | n.s. |
| 3 to 4 vs 4 to 5 | 0.78 | 17 | = 0.743 | 0.21 [-0.32, 0.57] | small | n.s. |
| 3 to 4 vs 5 to 6 | 1.26 | 17 | = 0.598 | 0.26 [-0.16, 0.77] | small | n.s. |
| 4 to 5 vs 5 to 6 | 0.16 | 17 | = 0.875 | 0.04 [-0.34, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 504.77, BIC = 522.28
- **2 to 3 vs 1 to 2**: *β* = 2.91, *SE* = 3.750, *z* = 0.777, *p* = 0.437
- **3 to 4 vs 1 to 2**: *β* = -0.45, *SE* = 3.664, *z* = -0.122, *p* = 0.903
- **4 to 5 vs 1 to 2**: *β* = 2.84, *SE* = 3.554, *z* = 0.799, *p* = 0.425
- **5 to 6 vs 1 to 2**: *β* = -2.36, *SE* = 3.818, *z* = -0.619, *p* = 0.536
- **SNR**: *β* = -0.02, *SE* = 0.933, *z* = -0.025, *p* = 0.980

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -2.91 | 3.75 | -0.78 | 0.437 | 0.974 | n.s. |
| 1 to 2 - 3 to 4 | 0.45 | 3.66 | 0.12 | 0.903 | 0.991 | n.s. |
| 1 to 2 - 4 to 5 | -2.84 | 3.55 | -0.80 | 0.425 | 0.974 | n.s. |
| 1 to 2 - 5 to 6 | 2.36 | 3.82 | 0.62 | 0.536 | 0.974 | n.s. |
| 2 to 3 - 3 to 4 | 3.36 | 3.83 | 0.88 | 0.380 | 0.974 | n.s. |
| 2 to 3 - 4 to 5 | 0.08 | 3.73 | 0.02 | 0.984 | 0.991 | n.s. |
| 2 to 3 - 5 to 6 | 5.28 | 4.00 | 1.32 | 0.187 | 0.845 | n.s. |
| 3 to 4 - 4 to 5 | -3.29 | 3.63 | -0.91 | 0.365 | 0.974 | n.s. |
| 3 to 4 - 5 to 6 | 1.91 | 3.54 | 0.54 | 0.589 | 0.974 | n.s. |
| 4 to 5 - 5 to 6 | 5.20 | 3.77 | 1.38 | 0.168 | 0.841 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.320, η²_G = 0.285
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.30 | 2 | = 0.604 | -1.19 [-1.06, 0.51] | large | n.s. |
| 1 to 2 vs 3 to 4 | -2.08 | 2 | = 0.604 | -1.46 [-1.78, 0.31] | large | n.s. |
| 1 to 2 vs 4 to 5 | -1.51 | 2 | = 0.604 | -0.45 [-1.44, 0.23] | small | n.s. |
| 1 to 2 vs 5 to 6 | -5.00 | 2 | = 0.377 | -0.64 [-0.92, 0.92] | medium | n.s. |
| 2 to 3 vs 3 to 4 | -1.00 | 2 | = 0.604 | -0.32 [-1.16, 0.71] | small | n.s. |
| 2 to 3 vs 4 to 5 | 0.61 | 2 | = 0.671 | 0.65 [-0.70, 0.98] | medium | n.s. |
| 2 to 3 vs 5 to 6 | 0.66 | 2 | = 0.671 | 0.61 [-0.97, 1.13] | medium | n.s. |
| 3 to 4 vs 4 to 5 | 1.00 | 2 | = 0.604 | 0.90 [-0.70, 1.17] | large | n.s. |
| 3 to 4 vs 5 to 6 | 1.31 | 2 | = 0.604 | 0.91 [-0.35, 1.26] | large | n.s. |
| 4 to 5 vs 5 to 6 | -0.38 | 2 | = 0.742 | -0.12 [-0.92, 0.92] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 240.11, BIC = 257.63
- **2 to 3 vs 1 to 2**: *β* = 1.08, *SE* = 0.477, *z* = 2.260, *p* = 0.024
- **3 to 4 vs 1 to 2**: *β* = 1.51, *SE* = 0.453, *z* = 3.337, *p* = 0.001
- **4 to 5 vs 1 to 2**: *β* = 1.52, *SE* = 0.455, *z* = 3.342, *p* = 0.001
- **5 to 6 vs 1 to 2**: *β* = 0.58, *SE* = 0.478, *z* = 1.209, *p* = 0.227
- **SNR**: *β* = 1.06, *SE* = 0.122, *z* = 8.709, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -1.08 | 0.48 | -2.26 | 0.024 | 0.175 | n.s. |
| 1 to 2 - 3 to 4 | -1.51 | 0.45 | -3.34 | < .001 | 0.008 | ** |
| 1 to 2 - 4 to 5 | -1.52 | 0.45 | -3.34 | < .001 | 0.008 | ** |
| 1 to 2 - 5 to 6 | -0.58 | 0.48 | -1.21 | 0.227 | 0.723 | n.s. |
| 2 to 3 - 3 to 4 | -0.43 | 0.47 | -0.92 | 0.358 | 0.783 | n.s. |
| 2 to 3 - 4 to 5 | -0.44 | 0.48 | -0.92 | 0.356 | 0.783 | n.s. |
| 2 to 3 - 5 to 6 | 0.50 | 0.50 | 1.00 | 0.317 | 0.783 | n.s. |
| 3 to 4 - 4 to 5 | -0.01 | 0.45 | -0.02 | 0.986 | 0.986 | n.s. |
| 3 to 4 - 5 to 6 | 0.93 | 0.45 | 2.05 | 0.040 | 0.249 | n.s. |
| 4 to 5 - 5 to 6 | 0.94 | 0.47 | 1.99 | 0.047 | 0.250 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.588, η²_G = 0.155
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.62 | 2 | = 0.775 | -0.31 [-1.22, 0.38] | small | n.s. |
| 1 to 2 vs 3 to 4 | -1.49 | 2 | = 0.775 | -0.69 [-2.13, 0.13] | medium | n.s. |
| 1 to 2 vs 4 to 5 | 0.34 | 2 | = 0.851 | 0.08 [-1.47, 0.21] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | 1.04 | 2 | = 0.775 | 0.88 [-0.47, 1.49] | large | n.s. |
| 2 to 3 vs 3 to 4 | -0.07 | 2 | = 0.953 | -0.04 [-1.50, 0.47] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.58 | 2 | = 0.775 | 0.35 [-0.98, 0.70] | small | n.s. |
| 2 to 3 vs 5 to 6 | 0.81 | 2 | = 0.775 | 0.65 [-0.36, 2.10] | medium | n.s. |
| 3 to 4 vs 4 to 5 | 2.23 | 2 | = 0.775 | 0.86 [-0.67, 1.21] | large | n.s. |
| 3 to 4 vs 5 to 6 | 1.77 | 2 | = 0.775 | 1.71 [-0.52, 1.05] | large | n.s. |
| 4 to 5 vs 5 to 6 | 1.14 | 2 | = 0.775 | 1.04 [-0.63, 1.26] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 790.10, BIC = 808.85
- **2 to 3 vs 1 to 2**: *β* = -5.44, *SE* = 12.509, *z* = -0.435, *p* = 0.664
- **3 to 4 vs 1 to 2**: *β* = 1.87, *SE* = 12.687, *z* = 0.147, *p* = 0.883
- **4 to 5 vs 1 to 2**: *β* = 5.42, *SE* = 12.919, *z* = 0.419, *p* = 0.675
- **5 to 6 vs 1 to 2**: *β* = -4.56, *SE* = 15.337, *z* = -0.297, *p* = 0.766
- **SNR**: *β* = -0.64, *SE* = 1.341, *z* = -0.476, *p* = 0.634

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 5.44 | 12.51 | 0.43 | 0.664 | 1.000 | n.s. |
| 1 to 2 - 3 to 4 | -1.87 | 12.69 | -0.15 | 0.883 | 1.000 | n.s. |
| 1 to 2 - 4 to 5 | -5.42 | 12.92 | -0.42 | 0.675 | 1.000 | n.s. |
| 1 to 2 - 5 to 6 | 4.56 | 15.34 | 0.30 | 0.766 | 1.000 | n.s. |
| 2 to 3 - 3 to 4 | -7.31 | 12.49 | -0.59 | 0.559 | 0.999 | n.s. |
| 2 to 3 - 4 to 5 | -10.85 | 12.81 | -0.85 | 0.397 | 0.994 | n.s. |
| 2 to 3 - 5 to 6 | -0.88 | 15.31 | -0.06 | 0.954 | 1.000 | n.s. |
| 3 to 4 - 4 to 5 | -3.55 | 13.04 | -0.27 | 0.786 | 1.000 | n.s. |
| 3 to 4 - 5 to 6 | 6.43 | 15.49 | 0.41 | 0.678 | 1.000 | n.s. |
| 4 to 5 - 5 to 6 | 9.97 | 15.41 | 0.65 | 0.517 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.36, *p* = 0.838, η²_G = 0.042
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.64 | 6 | = 0.862 | -0.21 [-0.62, 0.49] | small | n.s. |
| 1 to 2 vs 3 to 4 | 0.38 | 6 | = 0.862 | 0.15 [-0.62, 0.49] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | -0.95 | 6 | = 0.862 | -0.53 [-0.88, 0.41] | medium | n.s. |
| 1 to 2 vs 5 to 6 | -0.30 | 6 | = 0.862 | -0.16 [-0.94, 0.73] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 0.59 | 6 | = 0.862 | 0.30 [-0.59, 0.52] | small | n.s. |
| 2 to 3 vs 4 to 5 | -0.39 | 6 | = 0.862 | -0.23 [-0.96, 0.29] | small | n.s. |
| 2 to 3 vs 5 to 6 | 0.10 | 6 | = 0.925 | 0.05 [-0.67, 1.02] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | -0.99 | 6 | = 0.862 | -0.55 [-0.85, 0.38] | medium | n.s. |
| 3 to 4 vs 5 to 6 | -0.57 | 6 | = 0.862 | -0.27 [-0.99, 0.69] | small | n.s. |
| 4 to 5 vs 5 to 6 | 0.48 | 6 | = 0.862 | 0.30 [-0.70, 0.98] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 373.45, BIC = 392.20
- **2 to 3 vs 1 to 2**: *β* = 0.25, *SE* = 0.714, *z* = 0.354, *p* = 0.723
- **3 to 4 vs 1 to 2**: *β* = 0.09, *SE* = 0.722, *z* = 0.124, *p* = 0.901
- **4 to 5 vs 1 to 2**: *β* = 0.90, *SE* = 0.745, *z* = 1.207, *p* = 0.227
- **5 to 6 vs 1 to 2**: *β* = -0.28, *SE* = 0.897, *z* = -0.307, *p* = 0.759
- **SNR**: *β* = 0.49, *SE* = 0.088, *z* = 5.606, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.25 | 0.71 | -0.35 | 0.723 | 0.997 | n.s. |
| 1 to 2 - 3 to 4 | -0.09 | 0.72 | -0.12 | 0.901 | 0.997 | n.s. |
| 1 to 2 - 4 to 5 | -0.90 | 0.74 | -1.21 | 0.227 | 0.902 | n.s. |
| 1 to 2 - 5 to 6 | 0.27 | 0.90 | 0.31 | 0.759 | 0.997 | n.s. |
| 2 to 3 - 3 to 4 | 0.16 | 0.71 | 0.23 | 0.818 | 0.997 | n.s. |
| 2 to 3 - 4 to 5 | -0.65 | 0.74 | -0.88 | 0.380 | 0.965 | n.s. |
| 2 to 3 - 5 to 6 | 0.53 | 0.91 | 0.58 | 0.561 | 0.993 | n.s. |
| 3 to 4 - 4 to 5 | -0.81 | 0.75 | -1.09 | 0.277 | 0.925 | n.s. |
| 3 to 4 - 5 to 6 | 0.36 | 0.91 | 0.40 | 0.689 | 0.997 | n.s. |
| 4 to 5 - 5 to 6 | 1.17 | 0.90 | 1.31 | 0.190 | 0.878 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.50, *p* = 0.234, η²_G = 0.120
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -3.25 | 6 | = 0.090 | -0.57 [-1.01, 0.15] | medium | n.s. |
| 1 to 2 vs 3 to 4 | -1.09 | 6 | = 0.577 | -0.34 [-0.72, 0.40] | small | n.s. |
| 1 to 2 vs 4 to 5 | -1.63 | 6 | = 0.517 | -0.71 [-0.92, 0.37] | medium | n.s. |
| 1 to 2 vs 5 to 6 | 0.27 | 6 | = 0.795 | 0.16 [-0.67, 1.02] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 0.61 | 6 | = 0.708 | 0.20 [-0.48, 0.63] | small | n.s. |
| 2 to 3 vs 4 to 5 | -0.33 | 6 | = 0.795 | -0.17 [-0.54, 0.67] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | 1.31 | 6 | = 0.577 | 0.83 [-0.42, 1.34] | large | n.s. |
| 3 to 4 vs 4 to 5 | -0.90 | 6 | = 0.577 | -0.36 [-0.78, 0.44] | small | n.s. |
| 3 to 4 vs 5 to 6 | 0.91 | 6 | = 0.577 | 0.55 [-0.47, 1.26] | medium | n.s. |
| 4 to 5 vs 5 to 6 | 3.23 | 6 | = 0.090 | 0.99 [-0.08, 1.91] | large | n.s. |

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
