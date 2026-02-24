# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:21:46

---

## 1. Analysis Overview

**Total Measurements:** 576
**Number of Subjects:** 24
**Number of Conditions:** 6

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
| from 1 | 24 | 104.17 ms | 10.11 | 2.06 | [92.00, 116.00] |
| from 2 | 24 | 104.50 ms | 9.01 | 1.84 | [92.00, 116.00] |
| from 3 | 24 | 104.17 ms | 9.54 | 1.95 | [92.00, 116.00] |
| from 4 | 24 | 105.83 ms | 8.08 | 1.65 | [92.00, 116.00] |
| from 5 | 24 | 104.33 ms | 8.58 | 1.75 | [92.00, 116.00] |
| from 6 | 24 | 106.00 ms | 8.34 | 1.70 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | -0.62 µV | 1.21 | 0.25 | [-3.28, 1.03] |
| from 2 | 24 | -0.95 µV | 1.21 | 0.25 | [-4.25, 0.99] |
| from 3 | 24 | -1.05 µV | 1.42 | 0.29 | [-4.01, 1.33] |
| from 4 | 24 | -0.96 µV | 1.50 | 0.31 | [-4.52, 1.60] |
| from 5 | 24 | -1.62 µV | 1.28 | 0.26 | [-4.87, 0.96] |
| from 6 | 24 | -1.59 µV | 1.68 | 0.34 | [-7.02, 0.48] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 173.00 ms | 18.28 | 3.73 | [144.00, 204.00] |
| from 2 | 24 | 175.50 ms | 16.82 | 3.43 | [144.00, 204.00] |
| from 3 | 24 | 174.17 ms | 18.39 | 3.75 | [144.00, 204.00] |
| from 4 | 24 | 175.00 ms | 16.98 | 3.47 | [144.00, 204.00] |
| from 5 | 24 | 174.50 ms | 15.05 | 3.07 | [144.00, 204.00] |
| from 6 | 24 | 173.50 ms | 16.16 | 3.30 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | -4.89 µV | 2.05 | 0.42 | [-9.98, -1.35] |
| from 2 | 24 | -4.46 µV | 1.92 | 0.39 | [-8.54, -0.21] |
| from 3 | 24 | -4.80 µV | 2.00 | 0.41 | [-9.13, -1.64] |
| from 4 | 24 | -4.84 µV | 2.05 | 0.42 | [-9.57, -1.72] |
| from 5 | 24 | -5.55 µV | 2.21 | 0.45 | [-9.69, -1.15] |
| from 6 | 24 | -5.42 µV | 2.08 | 0.42 | [-9.40, -2.21] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 104.67 ms | 9.77 | 2.00 | [92.00, 116.00] |
| from 2 | 24 | 105.83 ms | 10.55 | 2.15 | [92.00, 116.00] |
| from 3 | 24 | 106.00 ms | 9.73 | 1.99 | [92.00, 116.00] |
| from 4 | 24 | 107.83 ms | 8.04 | 1.64 | [92.00, 116.00] |
| from 5 | 24 | 105.50 ms | 10.00 | 2.04 | [92.00, 116.00] |
| from 6 | 24 | 106.00 ms | 9.65 | 1.97 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 1.17 µV | 1.89 | 0.39 | [-2.15, 6.82] |
| from 2 | 24 | 1.30 µV | 1.81 | 0.37 | [-1.64, 5.63] |
| from 3 | 24 | 1.11 µV | 1.80 | 0.37 | [-1.90, 5.48] |
| from 4 | 24 | 1.02 µV | 1.72 | 0.35 | [-1.36, 4.49] |
| from 5 | 24 | 1.39 µV | 1.44 | 0.29 | [-0.81, 4.51] |
| from 6 | 24 | 1.31 µV | 1.98 | 0.40 | [-2.10, 6.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 472.00 ms | 31.87 | 6.51 | [420.00, 532.00] |
| from 2 | 24 | 482.67 ms | 35.04 | 7.15 | [424.00, 532.00] |
| from 3 | 24 | 483.00 ms | 31.59 | 6.45 | [432.00, 532.00] |
| from 4 | 24 | 483.67 ms | 33.46 | 6.83 | [424.00, 532.00] |
| from 5 | 24 | 474.00 ms | 29.68 | 6.06 | [420.00, 524.00] |
| from 6 | 24 | 467.83 ms | 33.37 | 6.81 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 2.82 µV | 2.98 | 0.61 | [-2.10, 9.68] |
| from 2 | 24 | 3.19 µV | 2.73 | 0.56 | [-2.18, 7.14] |
| from 3 | 24 | 3.08 µV | 3.05 | 0.62 | [-3.38, 9.05] |
| from 4 | 24 | 3.06 µV | 2.90 | 0.59 | [-1.51, 8.07] |
| from 5 | 24 | 2.50 µV | 2.83 | 0.58 | [-2.98, 6.53] |
| from 6 | 24 | 2.53 µV | 2.98 | 0.61 | [-4.12, 8.95] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 962.30, BIC = 989.03
- **from 2 vs from 1**: *β* = 0.33, *SE* = 1.513, *z* = 0.218, *p* = 0.827
- **from 3 vs from 1**: *β* = 0.00, *SE* = 1.508, *z* = 0.000, *p* = 1.000
- **from 4 vs from 1**: *β* = 1.67, *SE* = 1.508, *z* = 1.106, *p* = 0.269
- **from 5 vs from 1**: *β* = 0.17, *SE* = 1.528, *z* = 0.113, *p* = 0.910
- **from 6 vs from 1**: *β* = 1.83, *SE* = 1.508, *z* = 1.216, *p* = 0.224
- **SNR**: *β* = -0.01, *SE* = 0.285, *z* = -0.025, *p* = 0.980

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.33 | 1.51 | -0.22 | 0.827 | 1.000 | n.s. |
| from 1 - from 3 | -0.00 | 1.51 | -0.00 | 1.000 | 1.000 | n.s. |
| from 1 - from 4 | -1.67 | 1.51 | -1.11 | 0.269 | 0.983 | n.s. |
| from 1 - from 5 | -0.17 | 1.53 | -0.11 | 0.910 | 1.000 | n.s. |
| from 1 - from 6 | -1.83 | 1.51 | -1.22 | 0.224 | 0.978 | n.s. |
| from 2 - from 3 | 0.33 | 1.51 | 0.22 | 0.827 | 1.000 | n.s. |
| from 2 - from 4 | -1.34 | 1.51 | -0.88 | 0.377 | 0.983 | n.s. |
| from 2 - from 5 | 0.16 | 1.55 | 0.10 | 0.919 | 1.000 | n.s. |
| from 2 - from 6 | -1.50 | 1.52 | -0.99 | 0.321 | 0.983 | n.s. |
| from 3 - from 4 | -1.67 | 1.51 | -1.11 | 0.269 | 0.983 | n.s. |
| from 3 - from 5 | -0.17 | 1.53 | -0.11 | 0.910 | 1.000 | n.s. |
| from 3 - from 6 | -1.83 | 1.51 | -1.22 | 0.224 | 0.978 | n.s. |
| from 4 - from 5 | 1.49 | 1.53 | 0.98 | 0.328 | 0.983 | n.s. |
| from 4 - from 6 | -0.17 | 1.51 | -0.11 | 0.912 | 1.000 | n.s. |
| from 5 - from 6 | -1.66 | 1.52 | -1.09 | 0.275 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.693, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.612 (ε = 0.601)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.18 | 23 | = 1.000 | -0.03 [-0.46, 0.39] | negligible | n.s. |
| from 1 vs from 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| from 1 vs from 4 | -1.14 | 23 | = 0.614 | -0.18 [-0.66, 0.20] | negligible | n.s. |
| from 1 vs from 5 | -0.08 | 23 | = 1.000 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| from 1 vs from 6 | -1.19 | 23 | = 0.614 | -0.20 [-0.67, 0.19] | negligible | n.s. |
| from 2 vs from 3 | 0.18 | 23 | = 1.000 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| from 2 vs from 4 | -1.05 | 23 | = 0.614 | -0.16 [-0.64, 0.21] | negligible | n.s. |
| from 2 vs from 5 | 0.11 | 23 | = 1.000 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| from 2 vs from 6 | -1.16 | 23 | = 0.614 | -0.17 [-0.67, 0.19] | negligible | n.s. |
| from 3 vs from 4 | -1.36 | 23 | = 0.614 | -0.19 [-0.71, 0.15] | negligible | n.s. |
| from 3 vs from 5 | -0.08 | 23 | = 1.000 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| from 3 vs from 6 | -1.24 | 23 | = 0.614 | -0.20 [-0.68, 0.18] | small | n.s. |
| from 4 vs from 5 | 1.00 | 23 | = 0.614 | 0.18 [-0.22, 0.63] | negligible | n.s. |
| from 4 vs from 6 | -0.21 | 23 | = 1.000 | -0.02 [-0.47, 0.38] | negligible | n.s. |
| from 5 vs from 6 | -1.17 | 23 | = 0.614 | -0.20 [-0.67, 0.19] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 431.48, BIC = 458.21
- **from 2 vs from 1**: *β* = -0.44, *SE* = 0.250, *z* = -1.757, *p* = 0.079
- **from 3 vs from 1**: *β* = -0.42, *SE* = 0.249, *z* = -1.704, *p* = 0.088
- **from 4 vs from 1**: *β* = -0.34, *SE* = 0.249, *z* = -1.366, *p* = 0.172
- **from 5 vs from 1**: *β* = -0.80, *SE* = 0.252, *z* = -3.151, *p* = 0.002
- **from 6 vs from 1**: *β* = -0.94, *SE* = 0.249, *z* = -3.768, *p* < .001
- **SNR**: *β* = -0.24, *SE* = 0.047, *z* = -5.203, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.44 | 0.25 | 1.76 | 0.079 | 0.523 | n.s. |
| from 1 - from 3 | 0.42 | 0.25 | 1.70 | 0.088 | 0.523 | n.s. |
| from 1 - from 4 | 0.34 | 0.25 | 1.37 | 0.172 | 0.662 | n.s. |
| from 1 - from 5 | 0.79 | 0.25 | 3.15 | 0.002 | 0.023 | * |
| from 1 - from 6 | 0.94 | 0.25 | 3.77 | < .001 | 0.002 | ** |
| from 2 - from 3 | -0.01 | 0.25 | -0.06 | 0.953 | 0.971 | n.s. |
| from 2 - from 4 | -0.10 | 0.25 | -0.40 | 0.692 | 0.971 | n.s. |
| from 2 - from 5 | 0.36 | 0.26 | 1.39 | 0.165 | 0.662 | n.s. |
| from 2 - from 6 | 0.50 | 0.25 | 1.99 | 0.046 | 0.405 | n.s. |
| from 3 - from 4 | -0.08 | 0.25 | -0.34 | 0.735 | 0.971 | n.s. |
| from 3 - from 5 | 0.37 | 0.25 | 1.47 | 0.142 | 0.657 | n.s. |
| from 3 - from 6 | 0.51 | 0.25 | 2.06 | 0.039 | 0.380 | n.s. |
| from 4 - from 5 | 0.45 | 0.25 | 1.80 | 0.071 | 0.522 | n.s. |
| from 4 - from 6 | 0.60 | 0.25 | 2.40 | 0.016 | 0.192 | n.s. |
| from 5 - from 6 | 0.14 | 0.25 | 0.57 | 0.568 | 0.965 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.14, *p* = 0.002, η²_G = 0.066
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 1.37 | 23 | = 0.251 | 0.27 [-0.15, 0.71] | small | n.s. |
| from 1 vs from 3 | 1.55 | 23 | = 0.223 | 0.33 [-0.12, 0.75] | small | n.s. |
| from 1 vs from 4 | 1.45 | 23 | = 0.243 | 0.25 [-0.14, 0.73] | small | n.s. |
| from 1 vs from 5 | 3.17 | 23 | = 0.053 | 0.81 [0.18, 1.11] | large | n.s. |
| from 1 vs from 6 | 2.95 | 23 | = 0.053 | 0.66 [0.14, 1.06] | medium | n.s. |
| from 2 vs from 3 | 0.37 | 23 | = 0.826 | 0.08 [-0.35, 0.50] | negligible | n.s. |
| from 2 vs from 4 | 0.06 | 23 | = 0.956 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| from 2 vs from 5 | 2.66 | 23 | = 0.070 | 0.54 [0.09, 1.00] | medium | n.s. |
| from 2 vs from 6 | 2.11 | 23 | = 0.119 | 0.44 [-0.01, 0.87] | small | n.s. |
| from 3 vs from 4 | -0.44 | 23 | = 0.826 | -0.06 [-0.51, 0.33] | negligible | n.s. |
| from 3 vs from 5 | 2.47 | 23 | = 0.081 | 0.43 [0.06, 0.95] | small | n.s. |
| from 3 vs from 6 | 1.97 | 23 | = 0.119 | 0.35 [-0.04, 0.84] | small | n.s. |
| from 4 vs from 5 | 2.08 | 23 | = 0.119 | 0.47 [-0.02, 0.87] | small | n.s. |
| from 4 vs from 6 | 1.95 | 23 | = 0.119 | 0.39 [-0.04, 0.84] | small | n.s. |
| from 5 vs from 6 | -0.12 | 23 | = 0.956 | -0.02 [-0.45, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1048.57, BIC = 1075.29
- **from 2 vs from 1**: *β* = 2.47, *SE* = 1.857, *z* = 1.329, *p* = 0.184
- **from 3 vs from 1**: *β* = 0.84, *SE* = 1.869, *z* = 0.449, *p* = 0.654
- **from 4 vs from 1**: *β* = 1.71, *SE* = 1.867, *z* = 0.914, *p* = 0.361
- **from 5 vs from 1**: *β* = 0.97, *SE* = 1.890, *z* = 0.513, *p* = 0.608
- **from 6 vs from 1**: *β* = 0.39, *SE* = 1.858, *z* = 0.207, *p* = 0.836
- **SNR**: *β* = 0.20, *SE* = 0.132, *z* = 1.503, *p* = 0.133

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -2.47 | 1.86 | -1.33 | 0.184 | 0.952 | n.s. |
| from 1 - from 3 | -0.84 | 1.87 | -0.45 | 0.654 | 1.000 | n.s. |
| from 1 - from 4 | -1.71 | 1.87 | -0.91 | 0.361 | 0.997 | n.s. |
| from 1 - from 5 | -0.97 | 1.89 | -0.51 | 0.608 | 1.000 | n.s. |
| from 1 - from 6 | -0.39 | 1.86 | -0.21 | 0.836 | 1.000 | n.s. |
| from 2 - from 3 | 1.63 | 1.87 | 0.87 | 0.383 | 0.997 | n.s. |
| from 2 - from 4 | 0.76 | 1.86 | 0.41 | 0.683 | 1.000 | n.s. |
| from 2 - from 5 | 1.50 | 1.89 | 0.79 | 0.427 | 0.998 | n.s. |
| from 2 - from 6 | 2.08 | 1.86 | 1.12 | 0.262 | 0.986 | n.s. |
| from 3 - from 4 | -0.87 | 1.86 | -0.47 | 0.641 | 1.000 | n.s. |
| from 3 - from 5 | -0.13 | 1.86 | -0.07 | 0.944 | 1.000 | n.s. |
| from 3 - from 6 | 0.45 | 1.86 | 0.24 | 0.808 | 1.000 | n.s. |
| from 4 - from 5 | 0.74 | 1.86 | 0.40 | 0.692 | 1.000 | n.s. |
| from 4 - from 6 | 1.32 | 1.86 | 0.71 | 0.478 | 0.998 | n.s. |
| from 5 - from 6 | 0.58 | 1.88 | 0.31 | 0.756 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.47, *p* = 0.799, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.14 | 23 | = 0.833 | -0.14 [-0.66, 0.20] | negligible | n.s. |
| from 1 vs from 3 | -0.56 | 23 | = 0.833 | -0.06 [-0.54, 0.31] | negligible | n.s. |
| from 1 vs from 4 | -1.22 | 23 | = 0.833 | -0.11 [-0.68, 0.18] | negligible | n.s. |
| from 1 vs from 5 | -0.59 | 23 | = 0.833 | -0.09 [-0.54, 0.30] | negligible | n.s. |
| from 1 vs from 6 | -0.26 | 23 | = 0.833 | -0.03 [-0.48, 0.37] | negligible | n.s. |
| from 2 vs from 3 | 0.73 | 23 | = 0.833 | 0.08 [-0.28, 0.57] | negligible | n.s. |
| from 2 vs from 4 | 0.22 | 23 | = 0.833 | 0.03 [-0.38, 0.47] | negligible | n.s. |
| from 2 vs from 5 | 0.53 | 23 | = 0.833 | 0.06 [-0.32, 0.53] | negligible | n.s. |
| from 2 vs from 6 | 1.47 | 23 | = 0.833 | 0.12 [-0.13, 0.73] | negligible | n.s. |
| from 3 vs from 4 | -0.45 | 23 | = 0.833 | -0.05 [-0.52, 0.33] | negligible | n.s. |
| from 3 vs from 5 | -0.21 | 23 | = 0.833 | -0.02 [-0.47, 0.38] | negligible | n.s. |
| from 3 vs from 6 | 0.41 | 23 | = 0.833 | 0.04 [-0.34, 0.51] | negligible | n.s. |
| from 4 vs from 5 | 0.23 | 23 | = 0.833 | 0.03 [-0.38, 0.47] | negligible | n.s. |
| from 4 vs from 6 | 0.91 | 23 | = 0.833 | 0.09 [-0.24, 0.61] | negligible | n.s. |
| from 5 vs from 6 | 0.55 | 23 | = 0.833 | 0.06 [-0.31, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 426.93, BIC = 453.65
- **from 2 vs from 1**: *β* = 0.45, *SE* = 0.217, *z* = 2.068, *p* = 0.039
- **from 3 vs from 1**: *β* = 0.22, *SE* = 0.219, *z* = 1.000, *p* = 0.317
- **from 4 vs from 1**: *β* = 0.16, *SE* = 0.219, *z* = 0.732, *p* = 0.464
- **from 5 vs from 1**: *β* = -0.46, *SE* = 0.221, *z* = -2.073, *p* = 0.038
- **from 6 vs from 1**: *β* = -0.49, *SE* = 0.218, *z* = -2.235, *p* = 0.025
- **SNR**: *β* = -0.07, *SE* = 0.016, *z* = -4.774, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.45 | 0.22 | -2.07 | 0.039 | 0.268 | n.s. |
| from 1 - from 3 | -0.22 | 0.22 | -1.00 | 0.317 | 0.821 | n.s. |
| from 1 - from 4 | -0.16 | 0.22 | -0.73 | 0.464 | 0.846 | n.s. |
| from 1 - from 5 | 0.46 | 0.22 | 2.07 | 0.038 | 0.268 | n.s. |
| from 1 - from 6 | 0.49 | 0.22 | 2.23 | 0.025 | 0.207 | n.s. |
| from 2 - from 3 | 0.23 | 0.22 | 1.06 | 0.291 | 0.821 | n.s. |
| from 2 - from 4 | 0.29 | 0.22 | 1.33 | 0.185 | 0.707 | n.s. |
| from 2 - from 5 | 0.91 | 0.22 | 4.11 | < .001 | < .001 | *** |
| from 2 - from 6 | 0.94 | 0.22 | 4.30 | < .001 | < .001 | *** |
| from 3 - from 4 | 0.06 | 0.22 | 0.27 | 0.787 | 0.955 | n.s. |
| from 3 - from 5 | 0.68 | 0.22 | 3.11 | 0.002 | 0.022 | * |
| from 3 - from 6 | 0.70 | 0.22 | 3.23 | 0.001 | 0.016 | * |
| from 4 - from 5 | 0.62 | 0.22 | 2.84 | 0.005 | 0.045 | * |
| from 4 - from 6 | 0.65 | 0.22 | 2.97 | 0.003 | 0.033 | * |
| from 5 - from 6 | 0.03 | 0.22 | 0.12 | 0.901 | 0.955 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.02, *p* < .001, η²_G = 0.034
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -2.17 | 23 | = 0.087 | -0.22 [-0.89, -0.00] | small | n.s. |
| from 1 vs from 3 | -0.53 | 23 | = 0.693 | -0.05 [-0.53, 0.32] | negligible | n.s. |
| from 1 vs from 4 | -0.21 | 23 | = 0.833 | -0.02 [-0.47, 0.38] | negligible | n.s. |
| from 1 vs from 5 | 2.67 | 23 | = 0.041 | 0.31 [0.09, 1.00] | small | * |
| from 1 vs from 6 | 1.86 | 23 | = 0.127 | 0.26 [-0.06, 0.82] | small | n.s. |
| from 2 vs from 3 | 1.58 | 23 | = 0.173 | 0.17 [-0.11, 0.76] | negligible | n.s. |
| from 2 vs from 4 | 1.64 | 23 | = 0.172 | 0.20 [-0.10, 0.77] | negligible | n.s. |
| from 2 vs from 5 | 4.13 | 23 | = 0.004 | 0.53 [0.35, 1.33] | medium | ** |
| from 2 vs from 6 | 4.00 | 23 | = 0.004 | 0.48 [0.33, 1.30] | small | ** |
| from 3 vs from 4 | 0.25 | 23 | = 0.833 | 0.02 [-0.37, 0.47] | negligible | n.s. |
| from 3 vs from 5 | 2.98 | 23 | = 0.033 | 0.36 [0.15, 1.07] | small | * |
| from 3 vs from 6 | 2.34 | 23 | = 0.071 | 0.31 [0.03, 0.92] | small | n.s. |
| from 4 vs from 5 | 2.77 | 23 | = 0.041 | 0.33 [0.11, 1.02] | small | * |
| from 4 vs from 6 | 2.09 | 23 | = 0.089 | 0.28 [-0.01, 0.87] | small | n.s. |
| from 5 vs from 6 | -0.65 | 23 | = 0.653 | -0.06 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 996.07, BIC = 1022.80
- **from 2 vs from 1**: *β* = 1.08, *SE* = 1.725, *z* = 0.626, *p* = 0.531
- **from 3 vs from 1**: *β* = 1.32, *SE* = 1.721, *z* = 0.769, *p* = 0.442
- **from 4 vs from 1**: *β* = 3.18, *SE* = 1.721, *z* = 1.848, *p* = 0.065
- **from 5 vs from 1**: *β* = 0.88, *SE* = 1.722, *z* = 0.509, *p* = 0.611
- **from 6 vs from 1**: *β* = 1.34, *SE* = 1.721, *z* = 0.781, *p* = 0.435
- **SNR**: *β* = 0.13, *SE* = 0.170, *z* = 0.740, *p* = 0.460

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -1.08 | 1.73 | -0.63 | 0.531 | 0.998 | n.s. |
| from 1 - from 3 | -1.32 | 1.72 | -0.77 | 0.442 | 0.997 | n.s. |
| from 1 - from 4 | -3.18 | 1.72 | -1.85 | 0.065 | 0.633 | n.s. |
| from 1 - from 5 | -0.88 | 1.72 | -0.51 | 0.611 | 0.999 | n.s. |
| from 1 - from 6 | -1.34 | 1.72 | -0.78 | 0.435 | 0.997 | n.s. |
| from 2 - from 3 | -0.24 | 1.72 | -0.14 | 0.887 | 1.000 | n.s. |
| from 2 - from 4 | -2.10 | 1.73 | -1.22 | 0.224 | 0.963 | n.s. |
| from 2 - from 5 | 0.20 | 1.73 | 0.12 | 0.906 | 1.000 | n.s. |
| from 2 - from 6 | -0.26 | 1.73 | -0.15 | 0.879 | 1.000 | n.s. |
| from 3 - from 4 | -1.86 | 1.72 | -1.08 | 0.281 | 0.981 | n.s. |
| from 3 - from 5 | 0.45 | 1.72 | 0.26 | 0.795 | 1.000 | n.s. |
| from 3 - from 6 | -0.02 | 1.72 | -0.01 | 0.991 | 1.000 | n.s. |
| from 4 - from 5 | 2.30 | 1.72 | 1.34 | 0.181 | 0.939 | n.s. |
| from 4 - from 6 | 1.84 | 1.72 | 1.07 | 0.286 | 0.981 | n.s. |
| from 5 - from 6 | -0.47 | 1.72 | -0.27 | 0.786 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.626, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.563 (ε = 0.630)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.49 | 23 | = 1.000 | -0.11 [-0.52, 0.32] | negligible | n.s. |
| from 1 vs from 3 | -1.14 | 23 | = 0.707 | -0.14 [-0.66, 0.20] | negligible | n.s. |
| from 1 vs from 4 | -2.53 | 23 | = 0.279 | -0.35 [-0.97, -0.07] | small | n.s. |
| from 1 vs from 5 | -0.41 | 23 | = 1.000 | -0.08 [-0.51, 0.34] | negligible | n.s. |
| from 1 vs from 6 | -0.83 | 23 | = 0.891 | -0.14 [-0.59, 0.26] | negligible | n.s. |
| from 2 vs from 3 | -0.07 | 23 | = 1.000 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| from 2 vs from 4 | -1.10 | 23 | = 0.707 | -0.21 [-0.65, 0.20] | small | n.s. |
| from 2 vs from 5 | 0.14 | 23 | = 1.000 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| from 2 vs from 6 | -0.11 | 23 | = 1.000 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| from 3 vs from 4 | -1.16 | 23 | = 0.707 | -0.21 [-0.67, 0.19] | small | n.s. |
| from 3 vs from 5 | 0.29 | 23 | = 1.000 | 0.05 [-0.36, 0.48] | negligible | n.s. |
| from 3 vs from 6 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| from 4 vs from 5 | 1.34 | 23 | = 0.707 | 0.26 [-0.16, 0.70] | small | n.s. |
| from 4 vs from 6 | 1.41 | 23 | = 0.707 | 0.21 [-0.14, 0.72] | small | n.s. |
| from 5 vs from 6 | -0.31 | 23 | = 1.000 | -0.05 [-0.48, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 456.00, BIC = 482.73
- **from 2 vs from 1**: *β* = 0.08, *SE* = 0.255, *z* = 0.314, *p* = 0.753
- **from 3 vs from 1**: *β* = -0.07, *SE* = 0.255, *z* = -0.255, *p* = 0.798
- **from 4 vs from 1**: *β* = -0.13, *SE* = 0.255, *z* = -0.517, *p* = 0.605
- **from 5 vs from 1**: *β* = 0.25, *SE* = 0.255, *z* = 0.983, *p* = 0.326
- **from 6 vs from 1**: *β* = 0.15, *SE* = 0.255, *z* = 0.582, *p* = 0.561
- **SNR**: *β* = 0.09, *SE* = 0.026, *z* = 3.265, *p* = 0.001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.08 | 0.26 | -0.31 | 0.753 | 0.999 | n.s. |
| from 1 - from 3 | 0.06 | 0.25 | 0.26 | 0.798 | 0.999 | n.s. |
| from 1 - from 4 | 0.13 | 0.25 | 0.52 | 0.605 | 0.999 | n.s. |
| from 1 - from 5 | -0.25 | 0.25 | -0.98 | 0.326 | 0.991 | n.s. |
| from 1 - from 6 | -0.15 | 0.25 | -0.58 | 0.561 | 0.999 | n.s. |
| from 2 - from 3 | 0.15 | 0.26 | 0.57 | 0.569 | 0.999 | n.s. |
| from 2 - from 4 | 0.21 | 0.26 | 0.83 | 0.407 | 0.997 | n.s. |
| from 2 - from 5 | -0.17 | 0.26 | -0.66 | 0.506 | 0.998 | n.s. |
| from 2 - from 6 | -0.07 | 0.26 | -0.27 | 0.790 | 0.999 | n.s. |
| from 3 - from 4 | 0.07 | 0.25 | 0.26 | 0.794 | 0.999 | n.s. |
| from 3 - from 5 | -0.32 | 0.25 | -1.24 | 0.216 | 0.967 | n.s. |
| from 3 - from 6 | -0.21 | 0.25 | -0.84 | 0.403 | 0.997 | n.s. |
| from 4 - from 5 | -0.38 | 0.25 | -1.50 | 0.134 | 0.884 | n.s. |
| from 4 - from 6 | -0.28 | 0.25 | -1.10 | 0.272 | 0.984 | n.s. |
| from 5 - from 6 | 0.10 | 0.25 | 0.40 | 0.688 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.745, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.687 (ε = 0.715)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.52 | 23 | = 0.861 | -0.07 [-0.53, 0.32] | negligible | n.s. |
| from 1 vs from 3 | 0.18 | 23 | = 0.918 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| from 1 vs from 4 | 0.46 | 23 | = 0.861 | 0.08 [-0.33, 0.52] | negligible | n.s. |
| from 1 vs from 5 | -0.70 | 23 | = 0.861 | -0.13 [-0.57, 0.28] | negligible | n.s. |
| from 1 vs from 6 | -0.44 | 23 | = 0.861 | -0.07 [-0.51, 0.33] | negligible | n.s. |
| from 2 vs from 3 | 0.79 | 23 | = 0.861 | 0.11 [-0.26, 0.59] | negligible | n.s. |
| from 2 vs from 4 | 1.05 | 23 | = 0.861 | 0.16 [-0.21, 0.64] | negligible | n.s. |
| from 2 vs from 5 | -0.33 | 23 | = 0.861 | -0.05 [-0.49, 0.36] | negligible | n.s. |
| from 2 vs from 6 | -0.01 | 23 | = 0.988 | -0.00 [-0.43, 0.42] | negligible | n.s. |
| from 3 vs from 4 | 0.53 | 23 | = 0.861 | 0.05 [-0.31, 0.53] | negligible | n.s. |
| from 3 vs from 5 | -1.05 | 23 | = 0.861 | -0.17 [-0.64, 0.21] | negligible | n.s. |
| from 3 vs from 6 | -1.03 | 23 | = 0.861 | -0.11 [-0.64, 0.22] | negligible | n.s. |
| from 4 vs from 5 | -1.18 | 23 | = 0.861 | -0.23 [-0.67, 0.19] | small | n.s. |
| from 4 vs from 6 | -1.04 | 23 | = 0.861 | -0.15 [-0.64, 0.22] | negligible | n.s. |
| from 5 vs from 6 | 0.33 | 23 | = 0.861 | 0.05 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1391.84, BIC = 1418.57
- **from 2 vs from 1**: *β* = 10.67, *SE* = 7.235, *z* = 1.475, *p* = 0.140
- **from 3 vs from 1**: *β* = 10.70, *SE* = 7.283, *z* = 1.469, *p* = 0.142
- **from 4 vs from 1**: *β* = 11.23, *SE* = 7.338, *z* = 1.530, *p* = 0.126
- **from 5 vs from 1**: *β* = 2.01, *SE* = 7.235, *z* = 0.277, *p* = 0.781
- **from 6 vs from 1**: *β* = -4.34, *SE* = 7.251, *z* = -0.598, *p* = 0.550
- **SNR**: *β* = 0.20, *SE* = 0.552, *z* = 0.359, *p* = 0.719

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -10.67 | 7.24 | -1.47 | 0.140 | 0.810 | n.s. |
| from 1 - from 3 | -10.70 | 7.28 | -1.47 | 0.142 | 0.810 | n.s. |
| from 1 - from 4 | -11.23 | 7.34 | -1.53 | 0.126 | 0.801 | n.s. |
| from 1 - from 5 | -2.01 | 7.24 | -0.28 | 0.781 | 0.998 | n.s. |
| from 1 - from 6 | 4.34 | 7.25 | 0.60 | 0.550 | 0.981 | n.s. |
| from 2 - from 3 | -0.03 | 7.28 | -0.00 | 0.997 | 1.000 | n.s. |
| from 2 - from 4 | -0.56 | 7.34 | -0.08 | 0.939 | 1.000 | n.s. |
| from 2 - from 5 | 8.66 | 7.24 | 1.20 | 0.231 | 0.879 | n.s. |
| from 2 - from 6 | 15.01 | 7.25 | 2.07 | 0.038 | 0.418 | n.s. |
| from 3 - from 4 | -0.53 | 7.25 | -0.07 | 0.942 | 1.000 | n.s. |
| from 3 - from 5 | 8.69 | 7.29 | 1.19 | 0.233 | 0.879 | n.s. |
| from 3 - from 6 | 15.04 | 7.24 | 2.08 | 0.038 | 0.418 | n.s. |
| from 4 - from 5 | 9.22 | 7.34 | 1.26 | 0.209 | 0.879 | n.s. |
| from 4 - from 6 | 15.57 | 7.27 | 2.14 | 0.032 | 0.389 | n.s. |
| from 5 - from 6 | 6.35 | 7.25 | 0.87 | 0.382 | 0.944 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.68, *p* = 0.145, η²_G = 0.036
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.31 | 23 | = 0.380 | -0.32 [-0.70, 0.16] | small | n.s. |
| from 1 vs from 3 | -1.32 | 23 | = 0.380 | -0.35 [-0.70, 0.16] | small | n.s. |
| from 1 vs from 4 | -1.78 | 23 | = 0.380 | -0.36 [-0.80, 0.07] | small | n.s. |
| from 1 vs from 5 | -0.24 | 23 | = 0.965 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| from 1 vs from 6 | 0.60 | 23 | = 0.757 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| from 2 vs from 3 | -0.04 | 23 | = 0.965 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| from 2 vs from 4 | -0.16 | 23 | = 0.965 | -0.03 [-0.46, 0.39] | negligible | n.s. |
| from 2 vs from 5 | 1.11 | 23 | = 0.462 | 0.27 [-0.20, 0.65] | small | n.s. |
| from 2 vs from 6 | 2.39 | 23 | = 0.214 | 0.43 [0.04, 0.93] | small | n.s. |
| from 3 vs from 4 | -0.10 | 23 | = 0.965 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| from 3 vs from 5 | 1.35 | 23 | = 0.380 | 0.29 [-0.16, 0.71] | small | n.s. |
| from 3 vs from 6 | 1.68 | 23 | = 0.380 | 0.47 [-0.09, 0.78] | small | n.s. |
| from 4 vs from 5 | 1.33 | 23 | = 0.380 | 0.31 [-0.16, 0.70] | small | n.s. |
| from 4 vs from 6 | 2.34 | 23 | = 0.214 | 0.47 [0.03, 0.92] | small | n.s. |
| from 5 vs from 6 | 0.78 | 23 | = 0.668 | 0.20 [-0.27, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 518.12, BIC = 544.85
- **from 2 vs from 1**: *β* = 0.37, *SE* = 0.292, *z* = 1.265, *p* = 0.206
- **from 3 vs from 1**: *β* = 0.14, *SE* = 0.294, *z* = 0.474, *p* = 0.635
- **from 4 vs from 1**: *β* = 0.07, *SE* = 0.297, *z* = 0.248, *p* = 0.804
- **from 5 vs from 1**: *β* = -0.32, *SE* = 0.292, *z* = -1.098, *p* = 0.272
- **from 6 vs from 1**: *β* = -0.36, *SE* = 0.293, *z* = -1.222, *p* = 0.222
- **SNR**: *β* = 0.08, *SE* = 0.024, *z* = 3.201, *p* = 0.001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.37 | 0.29 | -1.27 | 0.206 | 0.874 | n.s. |
| from 1 - from 3 | -0.14 | 0.29 | -0.47 | 0.635 | 0.982 | n.s. |
| from 1 - from 4 | -0.07 | 0.30 | -0.25 | 0.804 | 0.993 | n.s. |
| from 1 - from 5 | 0.32 | 0.29 | 1.10 | 0.272 | 0.892 | n.s. |
| from 1 - from 6 | 0.36 | 0.29 | 1.22 | 0.222 | 0.874 | n.s. |
| from 2 - from 3 | 0.23 | 0.29 | 0.78 | 0.435 | 0.942 | n.s. |
| from 2 - from 4 | 0.30 | 0.30 | 1.00 | 0.319 | 0.900 | n.s. |
| from 2 - from 5 | 0.69 | 0.29 | 2.36 | 0.018 | 0.226 | n.s. |
| from 2 - from 6 | 0.73 | 0.29 | 2.48 | 0.013 | 0.178 | n.s. |
| from 3 - from 4 | 0.07 | 0.29 | 0.23 | 0.821 | 0.993 | n.s. |
| from 3 - from 5 | 0.46 | 0.29 | 1.56 | 0.118 | 0.778 | n.s. |
| from 3 - from 6 | 0.50 | 0.29 | 1.70 | 0.089 | 0.703 | n.s. |
| from 4 - from 5 | 0.39 | 0.30 | 1.33 | 0.184 | 0.870 | n.s. |
| from 4 - from 6 | 0.43 | 0.29 | 1.47 | 0.142 | 0.815 | n.s. |
| from 5 - from 6 | 0.04 | 0.29 | 0.13 | 0.900 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.84, *p* = 0.110, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.21 | 23 | = 0.508 | -0.13 [-0.68, 0.18] | negligible | n.s. |
| from 1 vs from 3 | -0.76 | 23 | = 0.617 | -0.08 [-0.58, 0.27] | negligible | n.s. |
| from 1 vs from 4 | -0.84 | 23 | = 0.617 | -0.08 [-0.60, 0.25] | negligible | n.s. |
| from 1 vs from 5 | 1.04 | 23 | = 0.580 | 0.11 [-0.21, 0.64] | negligible | n.s. |
| from 1 vs from 6 | 0.81 | 23 | = 0.617 | 0.10 [-0.26, 0.59] | negligible | n.s. |
| from 2 vs from 3 | 0.43 | 23 | = 0.771 | 0.04 [-0.33, 0.51] | negligible | n.s. |
| from 2 vs from 4 | 0.61 | 23 | = 0.681 | 0.04 [-0.30, 0.55] | negligible | n.s. |
| from 2 vs from 5 | 2.73 | 23 | = 0.180 | 0.25 [0.10, 1.01] | small | n.s. |
| from 2 vs from 6 | 1.76 | 23 | = 0.345 | 0.23 [-0.08, 0.79] | small | n.s. |
| from 3 vs from 4 | 0.06 | 23 | = 0.951 | 0.00 [-0.41, 0.43] | negligible | n.s. |
| from 3 vs from 5 | 2.33 | 23 | = 0.218 | 0.20 [0.03, 0.92] | negligible | n.s. |
| from 3 vs from 6 | 1.33 | 23 | = 0.493 | 0.18 [-0.16, 0.70] | negligible | n.s. |
| from 4 vs from 5 | 2.11 | 23 | = 0.228 | 0.20 [-0.01, 0.87] | negligible | n.s. |
| from 4 vs from 6 | 1.43 | 23 | = 0.493 | 0.18 [-0.14, 0.72] | negligible | n.s. |
| from 5 vs from 6 | -0.09 | 23 | = 0.951 | -0.01 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.002) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed greater amplitude than from 5 (*d* = 0.31)
  - from 2 showed greater amplitude than from 5 (*d* = 0.53)
  - from 2 showed greater amplitude than from 6 (*d* = 0.48)
  - from 3 showed greater amplitude than from 5 (*d* = 0.36)
  - from 4 showed greater amplitude than from 5 (*d* = 0.33)

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
