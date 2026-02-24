# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:31:13

---

## 1. Analysis Overview

**Total Measurements:** 436
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
| 3a | 23 | 91.48 ms | 23.11 | 4.82 | [48.00, 124.00] |
| 3b | 19 | 79.79 ms | 29.47 | 6.76 | [48.00, 124.00] |
| 3c | 23 | 91.13 ms | 23.88 | 4.98 | [48.00, 124.00] |
| 3d | 20 | 88.20 ms | 24.71 | 5.52 | [48.00, 124.00] |
| 3e | 24 | 85.00 ms | 25.74 | 5.25 | [48.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 23 | -5.11 µV | 3.44 | 0.72 | [-14.13, 2.50] |
| 3b | 19 | -5.00 µV | 4.23 | 0.97 | [-11.12, 5.67] |
| 3c | 23 | -4.09 µV | 3.37 | 0.70 | [-9.54, 1.00] |
| 3d | 20 | -5.86 µV | 3.24 | 0.72 | [-12.18, -0.70] |
| 3e | 24 | -4.90 µV | 5.83 | 1.19 | [-20.15, 3.91] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 23 | 166.26 ms | 21.80 | 4.55 | [128.00, 204.00] |
| 3b | 19 | 172.42 ms | 24.03 | 5.51 | [128.00, 216.00] |
| 3c | 23 | 164.17 ms | 23.65 | 4.93 | [128.00, 200.00] |
| 3d | 20 | 167.80 ms | 31.70 | 7.09 | [128.00, 212.00] |
| 3e | 24 | 174.33 ms | 25.27 | 5.16 | [128.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 23 | -6.71 µV | 3.15 | 0.66 | [-13.35, -0.61] |
| 3b | 19 | -6.85 µV | 3.80 | 0.87 | [-17.23, -2.60] |
| 3c | 23 | -6.08 µV | 2.97 | 0.62 | [-10.68, 0.24] |
| 3d | 20 | -6.53 µV | 4.82 | 1.08 | [-15.16, 3.10] |
| 3e | 24 | -7.15 µV | 4.05 | 0.83 | [-19.22, 0.10] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 23 | 84.35 ms | 21.67 | 4.52 | [52.00, 116.00] |
| 3b | 19 | 91.58 ms | 25.54 | 5.86 | [52.00, 116.00] |
| 3c | 23 | 94.26 ms | 22.27 | 4.64 | [52.00, 116.00] |
| 3d | 20 | 87.80 ms | 20.12 | 4.50 | [52.00, 116.00] |
| 3e | 24 | 81.17 ms | 24.64 | 5.03 | [52.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 23 | 4.84 µV | 3.17 | 0.66 | [-3.49, 11.87] |
| 3b | 19 | 4.83 µV | 2.90 | 0.67 | [-0.33, 10.86] |
| 3c | 23 | 4.01 µV | 3.26 | 0.68 | [-1.52, 11.34] |
| 3d | 20 | 6.53 µV | 4.51 | 1.01 | [-1.05, 17.68] |
| 3e | 24 | 5.16 µV | 4.89 | 1.00 | [-3.66, 16.59] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 23 | 473.91 ms | 2.04 | 0.43 | [472.00, 476.00] |
| 3b | 19 | 474.11 ms | 2.05 | 0.47 | [472.00, 476.00] |
| 3c | 23 | 473.91 ms | 2.04 | 0.43 | [472.00, 476.00] |
| 3d | 20 | 474.40 ms | 2.01 | 0.45 | [472.00, 476.00] |
| 3e | 24 | 474.00 ms | 2.04 | 0.42 | [472.00, 476.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 23 | 2.18 µV | 4.17 | 0.87 | [-5.85, 10.37] |
| 3b | 19 | 2.63 µV | 5.88 | 1.35 | [-6.09, 14.24] |
| 3c | 23 | 1.56 µV | 3.30 | 0.69 | [-5.03, 8.41] |
| 3d | 20 | 1.63 µV | 3.86 | 0.86 | [-7.13, 10.32] |
| 3e | 24 | 2.59 µV | 5.09 | 1.04 | [-10.80, 14.49] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1016.04, BIC = 1037.57
- **3b vs 3a**: *β* = -12.53, *SE* = 6.773, *z* = -1.850, *p* = 0.064
- **3c vs 3a**: *β* = -1.61, *SE* = 6.445, *z* = -0.250, *p* = 0.802
- **3d vs 3a**: *β* = -2.76, *SE* = 6.669, *z* = -0.414, *p* = 0.679
- **3e vs 3a**: *β* = -6.98, *SE* = 6.360, *z* = -1.098, *p* = 0.272
- **SNR**: *β* = 3.28, *SE* = 2.354, *z* = 1.392, *p* = 0.164

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 12.53 | 6.77 | 1.85 | 0.064 | 0.485 | n.s. |
| 3a - 3c | 1.61 | 6.44 | 0.25 | 0.802 | 0.967 | n.s. |
| 3a - 3d | 2.76 | 6.67 | 0.41 | 0.679 | 0.967 | n.s. |
| 3a - 3e | 6.98 | 6.36 | 1.10 | 0.272 | 0.892 | n.s. |
| 3b - 3c | -10.92 | 6.82 | -1.60 | 0.109 | 0.648 | n.s. |
| 3b - 3d | -9.77 | 7.04 | -1.39 | 0.165 | 0.764 | n.s. |
| 3b - 3e | -5.55 | 6.77 | -0.82 | 0.412 | 0.952 | n.s. |
| 3c - 3d | 1.15 | 6.77 | 0.17 | 0.866 | 0.967 | n.s. |
| 3c - 3e | 5.37 | 6.33 | 0.85 | 0.397 | 0.952 | n.s. |
| 3d - 3e | 4.22 | 6.68 | 0.63 | 0.528 | 0.952 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.35, *p* = 0.264, η²_G = 0.054
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 2.47 | 15 | = 0.179 | 0.67 [0.10, 1.15] | medium | n.s. |
| 3a vs 3c | 0.79 | 15 | = 0.671 | 0.31 [-0.41, 0.48] | small | n.s. |
| 3a vs 3d | 0.91 | 15 | = 0.671 | 0.28 [-0.33, 0.61] | small | n.s. |
| 3a vs 3e | 2.31 | 15 | = 0.179 | 0.51 [-0.21, 0.67] | medium | n.s. |
| 3b vs 3c | -1.18 | 15 | = 0.644 | -0.39 [-0.88, 0.12] | small | n.s. |
| 3b vs 3d | -1.53 | 15 | = 0.486 | -0.40 [-0.94, 0.17] | small | n.s. |
| 3b vs 3e | -0.64 | 15 | = 0.671 | -0.20 [-0.64, 0.33] | negligible | n.s. |
| 3c vs 3d | -0.07 | 15 | = 0.948 | -0.02 [-0.44, 0.52] | negligible | n.s. |
| 3c vs 3e | 0.52 | 15 | = 0.678 | 0.20 [-0.31, 0.55] | small | n.s. |
| 3d vs 3e | 0.63 | 15 | = 0.671 | 0.22 [-0.43, 0.50] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 622.94, BIC = 644.47
- **3b vs 3a**: *β* = -0.06, *SE* = 1.215, *z* = -0.050, *p* = 0.960
- **3c vs 3a**: *β* = 1.32, *SE* = 1.160, *z* = 1.140, *p* = 0.254
- **3d vs 3a**: *β* = -1.03, *SE* = 1.199, *z* = -0.856, *p* = 0.392
- **3e vs 3a**: *β* = 0.49, *SE* = 1.145, *z* = 0.427, *p* = 0.669
- **SNR**: *β* = -1.17, *SE* = 0.387, *z* = -3.009, *p* = 0.003

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.06 | 1.21 | 0.05 | 0.960 | 0.960 | n.s. |
| 3a - 3c | -1.32 | 1.16 | -1.14 | 0.254 | 0.905 | n.s. |
| 3a - 3d | 1.03 | 1.20 | 0.86 | 0.392 | 0.950 | n.s. |
| 3a - 3e | -0.49 | 1.15 | -0.43 | 0.669 | 0.957 | n.s. |
| 3b - 3c | -1.38 | 1.22 | -1.13 | 0.258 | 0.905 | n.s. |
| 3b - 3d | 0.97 | 1.25 | 0.77 | 0.442 | 0.950 | n.s. |
| 3b - 3e | -0.55 | 1.21 | -0.45 | 0.650 | 0.957 | n.s. |
| 3c - 3d | 2.35 | 1.21 | 1.94 | 0.053 | 0.418 | n.s. |
| 3c - 3e | 0.83 | 1.14 | 0.73 | 0.466 | 0.950 | n.s. |
| 3d - 3e | -1.51 | 1.20 | -1.26 | 0.206 | 0.875 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.593, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.17 | 15 | = 0.984 | -0.06 [-0.49, 0.47] | negligible | n.s. |
| 3a vs 3c | -1.49 | 15 | = 0.779 | -0.44 [-0.70, 0.20] | small | n.s. |
| 3a vs 3d | 0.66 | 15 | = 0.837 | 0.24 [-0.35, 0.59] | small | n.s. |
| 3a vs 3e | 0.02 | 15 | = 0.984 | 0.01 [-0.49, 0.38] | negligible | n.s. |
| 3b vs 3c | -1.08 | 15 | = 0.779 | -0.36 [-0.73, 0.24] | small | n.s. |
| 3b vs 3d | 0.89 | 15 | = 0.779 | 0.29 [-0.32, 0.76] | small | n.s. |
| 3b vs 3e | 0.13 | 15 | = 0.984 | 0.05 [-0.43, 0.53] | negligible | n.s. |
| 3c vs 3d | 2.00 | 15 | = 0.645 | 0.73 [-0.11, 0.89] | medium | n.s. |
| 3c vs 3e | 0.95 | 15 | = 0.779 | 0.33 [-0.29, 0.58] | small | n.s. |
| 3d vs 3e | -0.56 | 15 | = 0.837 | -0.17 [-0.71, 0.24] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1015.29, BIC = 1036.82
- **3b vs 3a**: *β* = 4.56, *SE* = 7.112, *z* = 0.641, *p* = 0.521
- **3c vs 3a**: *β* = 0.48, *SE* = 6.799, *z* = 0.070, *p* = 0.944
- **3d vs 3a**: *β* = 2.35, *SE* = 6.992, *z* = 0.336, *p* = 0.737
- **3e vs 3a**: *β* = 12.90, *SE* = 6.872, *z* = 1.877, *p* = 0.060
- **SNR**: *β* = -3.72, *SE* = 1.353, *z* = -2.746, *p* = 0.006

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -4.56 | 7.11 | -0.64 | 0.521 | 0.988 | n.s. |
| 3a - 3c | -0.48 | 6.80 | -0.07 | 0.944 | 0.995 | n.s. |
| 3a - 3d | -2.35 | 6.99 | -0.34 | 0.737 | 0.995 | n.s. |
| 3a - 3e | -12.90 | 6.87 | -1.88 | 0.060 | 0.464 | n.s. |
| 3b - 3c | 4.08 | 7.24 | 0.56 | 0.573 | 0.988 | n.s. |
| 3b - 3d | 2.21 | 7.38 | 0.30 | 0.765 | 0.995 | n.s. |
| 3b - 3e | -8.34 | 7.38 | -1.13 | 0.258 | 0.876 | n.s. |
| 3c - 3d | -1.87 | 7.04 | -0.27 | 0.790 | 0.995 | n.s. |
| 3c - 3e | -12.42 | 6.70 | -1.85 | 0.064 | 0.464 | n.s. |
| 3d - 3e | -10.55 | 7.09 | -1.49 | 0.137 | 0.692 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.650, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.24 | 15 | = 0.816 | -0.09 [-0.67, 0.31] | negligible | n.s. |
| 3a vs 3c | 0.74 | 15 | = 0.816 | 0.15 [-0.41, 0.47] | negligible | n.s. |
| 3a vs 3d | -0.55 | 15 | = 0.816 | -0.17 [-0.52, 0.42] | negligible | n.s. |
| 3a vs 3e | -1.15 | 15 | = 0.816 | -0.36 [-0.70, 0.18] | small | n.s. |
| 3b vs 3c | 0.63 | 15 | = 0.816 | 0.25 [-0.22, 0.76] | small | n.s. |
| 3b vs 3d | -0.26 | 15 | = 0.816 | -0.10 [-0.60, 0.47] | negligible | n.s. |
| 3b vs 3e | -1.29 | 15 | = 0.816 | -0.29 [-0.66, 0.31] | small | n.s. |
| 3c vs 3d | -0.89 | 15 | = 0.816 | -0.29 [-0.54, 0.42] | small | n.s. |
| 3c vs 3e | -1.53 | 15 | = 0.816 | -0.49 [-0.79, 0.10] | small | n.s. |
| 3d vs 3e | -0.39 | 15 | = 0.816 | -0.14 [-0.59, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 571.50, BIC = 593.03
- **3b vs 3a**: *β* = -0.50, *SE* = 0.863, *z* = -0.583, *p* = 0.560
- **3c vs 3a**: *β* = 1.28, *SE* = 0.827, *z* = 1.550, *p* = 0.121
- **3d vs 3a**: *β* = 0.51, *SE* = 0.848, *z* = 0.600, *p* = 0.549
- **3e vs 3a**: *β* = 0.66, *SE* = 0.837, *z* = 0.787, *p* = 0.431
- **SNR**: *β* = -0.87, *SE* = 0.176, *z* = -4.953, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.50 | 0.86 | 0.58 | 0.560 | 0.941 | n.s. |
| 3a - 3c | -1.28 | 0.83 | -1.55 | 0.121 | 0.687 | n.s. |
| 3a - 3d | -0.51 | 0.85 | -0.60 | 0.549 | 0.941 | n.s. |
| 3a - 3e | -0.66 | 0.84 | -0.79 | 0.431 | 0.941 | n.s. |
| 3b - 3c | -1.78 | 0.88 | -2.03 | 0.043 | 0.354 | n.s. |
| 3b - 3d | -1.01 | 0.90 | -1.13 | 0.260 | 0.879 | n.s. |
| 3b - 3e | -1.16 | 0.90 | -1.29 | 0.196 | 0.826 | n.s. |
| 3c - 3d | 0.77 | 0.86 | 0.90 | 0.368 | 0.936 | n.s. |
| 3c - 3e | 0.62 | 0.81 | 0.77 | 0.442 | 0.941 | n.s. |
| 3d - 3e | -0.15 | 0.87 | -0.17 | 0.863 | 0.941 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.51, *p* = 0.728, η²_G = 0.017
- Greenhouse-Geisser corrected: *p* = 0.655 (ε = 0.663)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.53 | 15 | = 0.882 | -0.14 [-0.51, 0.45] | negligible | n.s. |
| 3a vs 3c | -1.00 | 15 | = 0.871 | -0.24 [-0.72, 0.18] | small | n.s. |
| 3a vs 3d | -1.36 | 15 | = 0.871 | -0.36 [-0.61, 0.33] | small | n.s. |
| 3a vs 3e | -1.11 | 15 | = 0.871 | -0.27 [-0.31, 0.56] | small | n.s. |
| 3b vs 3c | -0.15 | 15 | = 0.882 | -0.05 [-0.63, 0.34] | negligible | n.s. |
| 3b vs 3d | -0.93 | 15 | = 0.871 | -0.21 [-0.77, 0.31] | small | n.s. |
| 3b vs 3e | -0.35 | 15 | = 0.882 | -0.10 [-0.55, 0.42] | negligible | n.s. |
| 3c vs 3d | -0.80 | 15 | = 0.871 | -0.20 [-0.53, 0.43] | negligible | n.s. |
| 3c vs 3e | -0.19 | 15 | = 0.882 | -0.07 [-0.23, 0.64] | negligible | n.s. |
| 3d vs 3e | 0.40 | 15 | = 0.882 | 0.13 [-0.30, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 994.53, BIC = 1016.06
- **3b vs 3a**: *β* = 6.23, *SE* = 6.106, *z* = 1.020, *p* = 0.308
- **3c vs 3a**: *β* = 9.85, *SE* = 5.785, *z* = 1.703, *p* = 0.089
- **3d vs 3a**: *β* = 4.15, *SE* = 6.007, *z* = 0.691, *p* = 0.490
- **3e vs 3a**: *β* = -2.45, *SE* = 5.773, *z* = -0.425, *p* = 0.671
- **SNR**: *β* = -0.75, *SE* = 2.290, *z* = -0.326, *p* = 0.744

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -6.23 | 6.11 | -1.02 | 0.308 | 0.893 | n.s. |
| 3a - 3c | -9.85 | 5.78 | -1.70 | 0.089 | 0.566 | n.s. |
| 3a - 3d | -4.15 | 6.01 | -0.69 | 0.490 | 0.932 | n.s. |
| 3a - 3e | 2.45 | 5.77 | 0.42 | 0.671 | 0.932 | n.s. |
| 3b - 3c | -3.63 | 6.11 | -0.59 | 0.553 | 0.932 | n.s. |
| 3b - 3d | 2.08 | 6.36 | 0.33 | 0.744 | 0.932 | n.s. |
| 3b - 3e | 8.68 | 6.13 | 1.42 | 0.157 | 0.744 | n.s. |
| 3c - 3d | 5.70 | 6.03 | 0.95 | 0.344 | 0.893 | n.s. |
| 3c - 3e | 12.30 | 5.77 | 2.13 | 0.033 | 0.286 | n.s. |
| 3d - 3e | 6.60 | 6.02 | 1.10 | 0.273 | 0.893 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.570, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.28 | 15 | = 0.864 | -0.07 [-0.68, 0.29] | negligible | n.s. |
| 3a vs 3c | -1.15 | 15 | = 0.703 | -0.38 [-0.83, 0.08] | small | n.s. |
| 3a vs 3d | -0.42 | 15 | = 0.849 | -0.13 [-0.61, 0.33] | negligible | n.s. |
| 3a vs 3e | 0.45 | 15 | = 0.849 | 0.15 [-0.35, 0.51] | negligible | n.s. |
| 3b vs 3c | -0.96 | 15 | = 0.703 | -0.27 [-0.72, 0.26] | small | n.s. |
| 3b vs 3d | -0.17 | 15 | = 0.864 | -0.05 [-0.58, 0.49] | negligible | n.s. |
| 3b vs 3e | 0.55 | 15 | = 0.849 | 0.21 [-0.26, 0.72] | small | n.s. |
| 3c vs 3d | 1.13 | 15 | = 0.703 | 0.25 [-0.25, 0.73] | small | n.s. |
| 3c vs 3e | 1.74 | 15 | = 0.703 | 0.52 [-0.06, 0.83] | medium | n.s. |
| 3d vs 3e | 1.00 | 15 | = 0.703 | 0.29 [-0.24, 0.70] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 609.72, BIC = 631.25
- **3b vs 3a**: *β* = -0.10, *SE* = 1.075, *z* = -0.097, *p* = 0.923
- **3c vs 3a**: *β* = -0.92, *SE* = 1.020, *z* = -0.904, *p* = 0.366
- **3d vs 3a**: *β* = 1.67, *SE* = 1.058, *z* = 1.582, *p* = 0.114
- **3e vs 3a**: *β* = 0.17, *SE* = 1.018, *z* = 0.163, *p* = 0.871
- **SNR**: *β* = 0.32, *SE* = 0.397, *z* = 0.805, *p* = 0.421

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.10 | 1.08 | 0.10 | 0.923 | 0.992 | n.s. |
| 3a - 3c | 0.92 | 1.02 | 0.90 | 0.366 | 0.897 | n.s. |
| 3a - 3d | -1.67 | 1.06 | -1.58 | 0.114 | 0.653 | n.s. |
| 3a - 3e | -0.17 | 1.02 | -0.16 | 0.871 | 0.992 | n.s. |
| 3b - 3c | 0.82 | 1.07 | 0.76 | 0.446 | 0.906 | n.s. |
| 3b - 3d | -1.78 | 1.12 | -1.59 | 0.111 | 0.653 | n.s. |
| 3b - 3e | -0.27 | 1.08 | -0.25 | 0.802 | 0.992 | n.s. |
| 3c - 3d | -2.60 | 1.06 | -2.45 | 0.014 | 0.136 | n.s. |
| 3c - 3e | -1.09 | 1.02 | -1.07 | 0.285 | 0.866 | n.s. |
| 3d - 3e | 1.51 | 1.06 | 1.42 | 0.155 | 0.693 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.69, *p* = 0.163, η²_G = 0.064
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.05 | 15 | = 0.958 | -0.02 [-0.45, 0.51] | negligible | n.s. |
| 3a vs 3c | 1.24 | 15 | = 0.388 | 0.32 [-0.23, 0.67] | small | n.s. |
| 3a vs 3d | -1.50 | 15 | = 0.388 | -0.43 [-0.84, 0.12] | small | n.s. |
| 3a vs 3e | -0.65 | 15 | = 0.659 | -0.19 [-0.43, 0.43] | negligible | n.s. |
| 3b vs 3c | 1.25 | 15 | = 0.388 | 0.38 [-0.21, 0.78] | small | n.s. |
| 3b vs 3d | -1.46 | 15 | = 0.388 | -0.45 [-0.91, 0.19] | small | n.s. |
| 3b vs 3e | -0.53 | 15 | = 0.671 | -0.20 [-0.62, 0.35] | negligible | n.s. |
| 3c vs 3d | -2.29 | 15 | = 0.373 | -0.74 [-0.98, 0.03] | medium | n.s. |
| 3c vs 3e | -1.50 | 15 | = 0.388 | -0.50 [-0.65, 0.22] | small | n.s. |
| 3d vs 3e | 0.80 | 15 | = 0.620 | 0.23 [-0.16, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 474.42, BIC = 495.95
- **3b vs 3a**: *β* = 0.17, *SE* = 0.616, *z* = 0.279, *p* = 0.780
- **3c vs 3a**: *β* = 0.02, *SE* = 0.585, *z* = 0.027, *p* = 0.979
- **3d vs 3a**: *β* = 0.42, *SE* = 0.609, *z* = 0.692, *p* = 0.489
- **3e vs 3a**: *β* = 0.14, *SE* = 0.580, *z* = 0.234, *p* = 0.815
- **SNR**: *β* = -0.09, *SE* = 0.087, *z* = -1.016, *p* = 0.310

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.17 | 0.62 | -0.28 | 0.780 | 1.000 | n.s. |
| 3a - 3c | -0.02 | 0.58 | -0.03 | 0.979 | 1.000 | n.s. |
| 3a - 3d | -0.42 | 0.61 | -0.69 | 0.489 | 0.999 | n.s. |
| 3a - 3e | -0.14 | 0.58 | -0.23 | 0.815 | 1.000 | n.s. |
| 3b - 3c | 0.16 | 0.62 | 0.25 | 0.800 | 1.000 | n.s. |
| 3b - 3d | -0.25 | 0.64 | -0.39 | 0.695 | 1.000 | n.s. |
| 3b - 3e | 0.04 | 0.61 | 0.06 | 0.953 | 1.000 | n.s. |
| 3c - 3d | -0.41 | 0.61 | -0.66 | 0.507 | 0.999 | n.s. |
| 3c - 3e | -0.12 | 0.58 | -0.21 | 0.836 | 1.000 | n.s. |
| 3d - 3e | 0.29 | 0.61 | 0.47 | 0.639 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.881, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.00 | 15 | = 1.000 | 0.00 [-0.69, 0.28] | negligible | n.s. |
| 3a vs 3c | 0.00 | 15 | = 1.000 | 0.00 [-0.44, 0.44] | negligible | n.s. |
| 3a vs 3d | -0.62 | 15 | = 0.907 | -0.24 [-0.53, 0.40] | small | n.s. |
| 3a vs 3e | -0.70 | 15 | = 0.907 | -0.24 [-0.49, 0.37] | small | n.s. |
| 3b vs 3c | 0.00 | 15 | = 1.000 | 0.00 [-0.38, 0.58] | negligible | n.s. |
| 3b vs 3d | -0.70 | 15 | = 0.907 | -0.24 [-0.71, 0.36] | small | n.s. |
| 3b vs 3e | -0.70 | 15 | = 0.907 | -0.24 [-0.48, 0.48] | small | n.s. |
| 3c vs 3d | -0.62 | 15 | = 0.907 | -0.24 [-0.76, 0.22] | small | n.s. |
| 3c vs 3e | -0.70 | 15 | = 0.907 | -0.24 [-0.49, 0.38] | small | n.s. |
| 3d vs 3e | 0.00 | 15 | = 1.000 | 0.00 [-0.40, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 622.45, BIC = 643.98
- **3b vs 3a**: *β* = 0.58, *SE* = 1.136, *z* = 0.511, *p* = 0.609
- **3c vs 3a**: *β* = -0.85, *SE* = 1.078, *z* = -0.787, *p* = 0.431
- **3d vs 3a**: *β* = 0.03, *SE* = 1.125, *z* = 0.026, *p* = 0.980
- **3e vs 3a**: *β* = -0.08, *SE* = 1.068, *z* = -0.076, *p* = 0.940
- **SNR**: *β* = 0.78, *SE* = 0.169, *z* = 4.614, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.58 | 1.14 | -0.51 | 0.609 | 0.994 | n.s. |
| 3a - 3c | 0.85 | 1.08 | 0.79 | 0.431 | 0.994 | n.s. |
| 3a - 3d | -0.03 | 1.12 | -0.03 | 0.980 | 1.000 | n.s. |
| 3a - 3e | 0.08 | 1.07 | 0.08 | 0.940 | 1.000 | n.s. |
| 3b - 3c | 1.43 | 1.14 | 1.26 | 0.209 | 0.904 | n.s. |
| 3b - 3d | 0.55 | 1.18 | 0.47 | 0.640 | 0.994 | n.s. |
| 3b - 3e | 0.66 | 1.13 | 0.58 | 0.560 | 0.994 | n.s. |
| 3c - 3d | -0.88 | 1.13 | -0.77 | 0.438 | 0.994 | n.s. |
| 3c - 3e | -0.77 | 1.07 | -0.72 | 0.471 | 0.994 | n.s. |
| 3d - 3e | 0.11 | 1.13 | 0.10 | 0.923 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.34, *p* = 0.849, η²_G = 0.014
- Greenhouse-Geisser corrected: *p* = 0.775 (ε = 0.676)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -1.46 | 15 | = 0.932 | -0.27 [-0.57, 0.40] | small | n.s. |
| 3a vs 3c | -0.00 | 15 | = 0.999 | -0.00 [-0.25, 0.65] | negligible | n.s. |
| 3a vs 3d | -0.21 | 15 | = 0.932 | -0.08 [-0.45, 0.49] | negligible | n.s. |
| 3a vs 3e | -0.82 | 15 | = 0.932 | -0.18 [-0.48, 0.38] | negligible | n.s. |
| 3b vs 3c | 0.85 | 15 | = 0.932 | 0.29 [-0.31, 0.66] | small | n.s. |
| 3b vs 3d | 0.61 | 15 | = 0.932 | 0.22 [-0.38, 0.69] | small | n.s. |
| 3b vs 3e | 0.26 | 15 | = 0.932 | 0.08 [-0.48, 0.49] | negligible | n.s. |
| 3c vs 3d | -0.30 | 15 | = 0.932 | -0.09 [-0.53, 0.43] | negligible | n.s. |
| 3c vs 3e | -0.55 | 15 | = 0.932 | -0.20 [-0.62, 0.26] | negligible | n.s. |
| 3d vs 3e | -0.35 | 15 | = 0.932 | -0.13 [-0.59, 0.35] | negligible | n.s. |

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
