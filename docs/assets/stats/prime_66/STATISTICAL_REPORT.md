# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:52:29

---

## 1. Analysis Overview

**Total Measurements:** 340
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
| 6a | 12 | 91.67 ms | 18.64 | 5.38 | [56.00, 112.00] |
| 6b | 14 | 92.29 ms | 19.69 | 5.26 | [68.00, 120.00] |
| 6c | 12 | 92.33 ms | 19.18 | 5.54 | [64.00, 116.00] |
| 6d | 15 | 100.53 ms | 17.75 | 4.58 | [56.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 12 | -6.01 µV | 3.50 | 1.01 | [-13.64, -1.63] |
| 6b | 14 | -5.43 µV | 2.35 | 0.63 | [-10.13, -2.18] |
| 6c | 12 | -8.74 µV | 5.73 | 1.66 | [-24.65, -3.18] |
| 6d | 15 | -4.58 µV | 2.12 | 0.55 | [-8.93, -2.02] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 22 | 171.45 ms | 15.68 | 3.34 | [144.00, 200.00] |
| 6b | 18 | 167.56 ms | 18.09 | 4.26 | [144.00, 200.00] |
| 6c | 12 | 181.00 ms | 21.92 | 6.33 | [144.00, 200.00] |
| 6d | 19 | 170.53 ms | 15.96 | 3.66 | [144.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 22 | -7.34 µV | 3.29 | 0.70 | [-14.89, -1.22] |
| 6b | 18 | -6.56 µV | 3.56 | 0.84 | [-14.94, -1.82] |
| 6c | 12 | -9.29 µV | 5.42 | 1.56 | [-21.03, -1.28] |
| 6d | 19 | -7.14 µV | 3.77 | 0.86 | [-13.68, -0.99] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 7 | 97.14 ms | 20.62 | 7.79 | [60.00, 116.00] |
| 6b | 15 | 82.93 ms | 20.53 | 5.30 | [56.00, 116.00] |
| 6c | 10 | 98.40 ms | 17.61 | 5.57 | [68.00, 116.00] |
| 6d | 12 | 96.00 ms | 20.82 | 6.01 | [56.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 7 | 5.56 µV | 2.28 | 0.86 | [3.16, 9.90] |
| 6b | 15 | 5.53 µV | 3.51 | 0.91 | [1.49, 13.85] |
| 6c | 10 | 8.78 µV | 7.25 | 2.29 | [3.89, 28.64] |
| 6d | 12 | 5.39 µV | 2.93 | 0.85 | [2.12, 12.88] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 12 | 380.33 ms | 25.09 | 7.24 | [340.00, 408.00] |
| 6b | 11 | 383.64 ms | 20.59 | 6.21 | [348.00, 408.00] |
| 6c | 5 | 366.40 ms | 30.01 | 13.42 | [340.00, 408.00] |
| 6d | 14 | 380.00 ms | 20.64 | 5.52 | [352.00, 408.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 6a | 12 | 5.80 µV | 4.03 | 1.16 | [1.89, 12.79] |
| 6b | 11 | 4.87 µV | 2.08 | 0.63 | [1.89, 8.34] |
| 6c | 5 | 7.03 µV | 1.35 | 0.60 | [5.65, 8.75] |
| 6d | 14 | 6.36 µV | 2.01 | 0.54 | [3.10, 10.10] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 469.65, BIC = 483.44
- **6b vs 6a**: *β* = 1.23, *SE* = 7.015, *z* = 0.175, *p* = 0.861
- **6c vs 6a**: *β* = 2.45, *SE* = 7.266, *z* = 0.337, *p* = 0.736
- **6d vs 6a**: *β* = 10.62, *SE* = 7.106, *z* = 1.495, *p* = 0.135
- **SNR**: *β* = 2.71, *SE* = 2.252, *z* = 1.204, *p* = 0.229

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -1.22 | 7.02 | -0.17 | 0.861 | 0.982 | n.s. |
| 6a - 6c | -2.45 | 7.27 | -0.34 | 0.736 | 0.982 | n.s. |
| 6a - 6d | -10.63 | 7.11 | -1.50 | 0.135 | 0.581 | n.s. |
| 6b - 6c | -1.22 | 6.96 | -0.18 | 0.860 | 0.982 | n.s. |
| 6b - 6d | -9.40 | 6.58 | -1.43 | 0.153 | 0.581 | n.s. |
| 6c - 6d | -8.18 | 6.88 | -1.19 | 0.235 | 0.657 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.216, η²_G = 0.172
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | 0.05 | 6 | = 0.964 | 0.03 [-0.91, 0.94] | negligible | n.s. |
| 6a vs 6c | 0.39 | 6 | = 0.868 | 0.18 [-0.79, 0.75] | negligible | n.s. |
| 6a vs 6d | -1.52 | 6 | = 0.360 | -0.97 [-1.24, 0.37] | large | n.s. |
| 6b vs 6c | 0.37 | 6 | = 0.868 | 0.16 [-0.60, 0.83] | negligible | n.s. |
| 6b vs 6d | -2.37 | 6 | = 0.232 | -1.09 [-1.52, 0.09] | large | n.s. |
| 6c vs 6d | -2.13 | 6 | = 0.232 | -1.20 [-1.44, 0.23] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 291.85, BIC = 305.64
- **6b vs 6a**: *β* = 0.49, *SE* = 1.336, *z* = 0.364, *p* = 0.716
- **6c vs 6a**: *β* = -3.22, *SE* = 1.384, *z* = -2.325, *p* = 0.020
- **6d vs 6a**: *β* = 1.03, *SE* = 1.309, *z* = 0.788, *p* = 0.431
- **SNR**: *β* = -0.75, *SE* = 0.375, *z* = -1.996, *p* = 0.046

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -0.49 | 1.34 | -0.36 | 0.716 | 0.888 | n.s. |
| 6a - 6c | 3.22 | 1.38 | 2.33 | 0.020 | 0.078 | n.s. |
| 6a - 6d | -1.03 | 1.31 | -0.79 | 0.431 | 0.816 | n.s. |
| 6b - 6c | 3.70 | 1.34 | 2.77 | 0.006 | 0.027 | * |
| 6b - 6d | -0.54 | 1.26 | -0.43 | 0.665 | 0.888 | n.s. |
| 6c - 6d | -4.25 | 1.29 | -3.29 | < .001 | 0.006 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.278, η²_G = 0.143
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | -0.91 | 6 | = 0.599 | -0.58 [-1.29, 0.61] | medium | n.s. |
| 6a vs 6c | 0.45 | 6 | = 0.769 | 0.24 [-0.34, 1.28] | small | n.s. |
| 6a vs 6d | -1.01 | 6 | = 0.599 | -0.43 [-1.21, 0.39] | small | n.s. |
| 6b vs 6c | 2.77 | 6 | = 0.195 | 1.29 [-0.13, 1.44] | large | n.s. |
| 6b vs 6d | 0.31 | 6 | = 0.769 | 0.16 [-0.84, 0.59] | negligible | n.s. |
| 6c vs 6d | -1.76 | 6 | = 0.386 | -0.92 [-1.49, 0.20] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 606.04, BIC = 621.88
- **6b vs 6a**: *β* = -2.73, *SE* = 4.255, *z* = -0.642, *p* = 0.521
- **6c vs 6a**: *β* = 9.92, *SE* = 4.931, *z* = 2.011, *p* = 0.044
- **6d vs 6a**: *β* = -0.59, *SE* = 4.174, *z* = -0.141, *p* = 0.888
- **SNR**: *β* = -0.06, *SE* = 0.903, *z* = -0.062, *p* = 0.951

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 2.73 | 4.26 | 0.64 | 0.521 | 0.890 | n.s. |
| 6a - 6c | -9.92 | 4.93 | -2.01 | 0.044 | 0.173 | n.s. |
| 6a - 6d | 0.59 | 4.17 | 0.14 | 0.888 | 0.890 | n.s. |
| 6b - 6c | -12.65 | 5.20 | -2.43 | 0.015 | 0.087 | n.s. |
| 6b - 6d | -2.14 | 4.39 | -0.49 | 0.625 | 0.890 | n.s. |
| 6c - 6d | 10.51 | 5.04 | 2.08 | 0.037 | 0.173 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.38, *p* = 0.273, η²_G = 0.075
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | 0.48 | 8 | = 0.773 | 0.21 [-0.33, 0.71] | small | n.s. |
| 6a vs 6c | -0.83 | 8 | = 0.644 | -0.38 [-1.05, 0.34] | small | n.s. |
| 6a vs 6d | 1.08 | 8 | = 0.627 | 0.31 [-0.56, 0.43] | small | n.s. |
| 6b vs 6c | -2.21 | 8 | = 0.347 | -0.55 [-1.60, 0.13] | medium | n.s. |
| 6b vs 6d | 0.16 | 8 | = 0.879 | 0.06 [-0.54, 0.49] | negligible | n.s. |
| 6c vs 6d | 1.74 | 8 | = 0.360 | 0.67 [-0.25, 1.28] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 362.62, BIC = 378.46
- **6b vs 6a**: *β* = 1.23, *SE* = 0.720, *z* = 1.702, *p* = 0.089
- **6c vs 6a**: *β* = -1.35, *SE* = 0.844, *z* = -1.595, *p* = 0.111
- **6d vs 6a**: *β* = 0.13, *SE* = 0.707, *z* = 0.178, *p* = 0.858
- **SNR**: *β* = -0.71, *SE* = 0.156, *z* = -4.563, *p* < .001

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -1.22 | 0.72 | -1.70 | 0.089 | 0.364 | n.s. |
| 6a - 6c | 1.35 | 0.84 | 1.60 | 0.111 | 0.364 | n.s. |
| 6a - 6d | -0.13 | 0.71 | -0.18 | 0.858 | 0.858 | n.s. |
| 6b - 6c | 2.57 | 0.89 | 2.89 | 0.004 | 0.023 | * |
| 6b - 6d | 1.10 | 0.74 | 1.48 | 0.138 | 0.364 | n.s. |
| 6c - 6d | -1.47 | 0.86 | -1.71 | 0.087 | 0.364 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.608, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 6a vs 6b | -0.77 | 8 | = 0.770 | -0.28 [-0.82, 0.23] | small | n.s. |
| 6a vs 6c | 0.48 | 8 | = 0.770 | 0.21 [-0.56, 0.79] | small | n.s. |
| 6a vs 6d | -0.29 | 8 | = 0.777 | -0.12 [-0.59, 0.41] | negligible | n.s. |
| 6b vs 6c | 1.19 | 8 | = 0.770 | 0.39 [-0.40, 1.20] | small | n.s. |
| 6b vs 6d | 0.52 | 8 | = 0.770 | 0.15 [-0.36, 0.68] | negligible | n.s. |
| 6c vs 6d | -1.08 | 8 | = 0.770 | -0.28 [-1.18, 0.32] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 388.38, BIC = 400.87
- **6b vs 6a**: *β* = -9.82, *SE* = 6.606, *z* = -1.486, *p* = 0.137
- **6c vs 6a**: *β* = 2.31, *SE* = 6.832, *z* = 0.339, *p* = 0.735
- **6d vs 6a**: *β* = 4.22, *SE* = 6.779, *z* = 0.622, *p* = 0.534
- **SNR**: *β* = 3.46, *SE* = 2.895, *z* = 1.196, *p* = 0.232

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 9.82 | 6.61 | 1.49 | 0.137 | 0.446 | n.s. |
| 6a - 6c | -2.31 | 6.83 | -0.34 | 0.735 | 0.930 | n.s. |
| 6a - 6d | -4.22 | 6.78 | -0.62 | 0.534 | 0.899 | n.s. |
| 6b - 6c | -12.13 | 6.26 | -1.94 | 0.052 | 0.236 | n.s. |
| 6b - 6d | -14.03 | 5.65 | -2.49 | 0.013 | 0.075 | n.s. |
| 6c - 6d | -1.90 | 6.45 | -0.29 | 0.768 | 0.930 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 257.69, BIC = 270.18
- **6b vs 6a**: *β* = -0.46, *SE* = 1.792, *z* = -0.254, *p* = 0.799
- **6c vs 6a**: *β* = 3.82, *SE* = 1.952, *z* = 1.958, *p* = 0.050
- **6d vs 6a**: *β* = 0.60, *SE* = 1.956, *z* = 0.308, *p* = 0.758
- **SNR**: *β* = 1.97, *SE* = 0.706, *z* = 2.789, *p* = 0.005

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 0.46 | 1.79 | 0.25 | 0.799 | 0.941 | n.s. |
| 6a - 6c | -3.82 | 1.95 | -1.96 | 0.050 | 0.227 | n.s. |
| 6a - 6d | -0.60 | 1.96 | -0.31 | 0.758 | 0.941 | n.s. |
| 6b - 6c | -4.28 | 1.61 | -2.65 | 0.008 | 0.047 | * |
| 6b - 6d | -1.06 | 1.58 | -0.67 | 0.502 | 0.876 | n.s. |
| 6c - 6d | 3.22 | 1.66 | 1.94 | 0.052 | 0.227 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 389.39, BIC = 401.55
- **6b vs 6a**: *β* = 3.06, *SE* = 8.815, *z* = 0.347, *p* = 0.728
- **6c vs 6a**: *β* = -13.09, *SE* = 13.763, *z* = -0.951, *p* = 0.342
- **6d vs 6a**: *β* = -4.51, *SE* = 8.626, *z* = -0.523, *p* = 0.601
- **SNR**: *β* = 3.54, *SE* = 2.620, *z* = 1.350, *p* = 0.177

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | -3.06 | 8.82 | -0.35 | 0.728 | 0.892 | n.s. |
| 6a - 6c | 13.09 | 13.76 | 0.95 | 0.342 | 0.876 | n.s. |
| 6a - 6d | 4.51 | 8.63 | 0.52 | 0.601 | 0.892 | n.s. |
| 6b - 6c | 16.15 | 13.95 | 1.16 | 0.247 | 0.818 | n.s. |
| 6b - 6d | 7.57 | 8.80 | 0.86 | 0.389 | 0.876 | n.s. |
| 6c - 6d | -8.58 | 13.44 | -0.64 | 0.523 | 0.892 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 204.81, BIC = 216.97
- **6b vs 6a**: *β* = -0.91, *SE* = 0.967, *z* = -0.944, *p* = 0.345
- **6c vs 6a**: *β* = 1.34, *SE* = 1.237, *z* = 1.086, *p* = 0.278
- **6d vs 6a**: *β* = -0.24, *SE* = 0.939, *z* = -0.254, *p* = 0.799
- **SNR**: *β* = 0.65, *SE* = 0.224, *z* = 2.919, *p* = 0.004

_Reference condition: **6a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 6a - 6b | 0.91 | 0.97 | 0.94 | 0.345 | 0.728 | n.s. |
| 6a - 6c | -1.34 | 1.24 | -1.09 | 0.278 | 0.728 | n.s. |
| 6a - 6d | 0.24 | 0.94 | 0.25 | 0.799 | 0.799 | n.s. |
| 6b - 6c | -2.26 | 1.27 | -1.77 | 0.077 | 0.380 | n.s. |
| 6b - 6d | -0.67 | 0.99 | -0.68 | 0.498 | 0.747 | n.s. |
| 6c - 6d | 1.58 | 1.24 | 1.28 | 0.202 | 0.676 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


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
