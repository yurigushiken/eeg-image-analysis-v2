# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:21:10

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
| 4 to 1 | 24 | 105.67 ms | 10.54 | 2.15 | [92.00, 116.00] |
| 4 to 2 | 24 | 106.83 ms | 9.25 | 1.89 | [92.00, 116.00] |
| 4 to 3 | 24 | 105.67 ms | 8.58 | 1.75 | [92.00, 116.00] |
| 4 to 4 | 24 | 106.83 ms | 8.54 | 1.74 | [92.00, 116.00] |
| 4 to 5 | 24 | 99.00 ms | 7.76 | 1.58 | [92.00, 116.00] |
| 4 to 6 | 24 | 103.83 ms | 9.10 | 1.86 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | -2.43 µV | 2.86 | 0.58 | [-8.54, 3.59] |
| 4 to 2 | 24 | -0.82 µV | 2.70 | 0.55 | [-4.94, 5.89] |
| 4 to 3 | 24 | -0.76 µV | 2.17 | 0.44 | [-6.08, 2.67] |
| 4 to 4 | 24 | -1.60 µV | 1.83 | 0.37 | [-6.84, 1.26] |
| 4 to 5 | 24 | -3.83 µV | 5.32 | 1.09 | [-18.83, 3.58] |
| 4 to 6 | 24 | -1.53 µV | 2.52 | 0.51 | [-5.80, 3.38] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 184.67 ms | 14.67 | 2.99 | [144.00, 208.00] |
| 4 to 2 | 24 | 178.33 ms | 14.96 | 3.05 | [148.00, 208.00] |
| 4 to 3 | 24 | 173.83 ms | 16.26 | 3.32 | [152.00, 208.00] |
| 4 to 4 | 24 | 172.17 ms | 20.07 | 4.10 | [144.00, 208.00] |
| 4 to 5 | 24 | 170.17 ms | 20.19 | 4.12 | [144.00, 208.00] |
| 4 to 6 | 24 | 169.83 ms | 20.05 | 4.09 | [144.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | -3.66 µV | 2.18 | 0.44 | [-9.44, -0.12] |
| 4 to 2 | 24 | -6.16 µV | 3.06 | 0.62 | [-12.20, -2.20] |
| 4 to 3 | 24 | -6.02 µV | 2.75 | 0.56 | [-10.92, 1.75] |
| 4 to 4 | 24 | -5.53 µV | 3.33 | 0.68 | [-13.09, 0.33] |
| 4 to 5 | 24 | -6.75 µV | 3.97 | 0.81 | [-16.53, 0.62] |
| 4 to 6 | 24 | -6.34 µV | 3.84 | 0.78 | [-16.09, 0.71] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 110.00 ms | 8.26 | 1.69 | [96.00, 116.00] |
| 4 to 2 | 24 | 110.00 ms | 7.46 | 1.52 | [96.00, 116.00] |
| 4 to 3 | 24 | 106.00 ms | 8.00 | 1.63 | [96.00, 116.00] |
| 4 to 4 | 24 | 108.50 ms | 8.53 | 1.74 | [96.00, 116.00] |
| 4 to 5 | 24 | 104.00 ms | 7.37 | 1.50 | [96.00, 116.00] |
| 4 to 6 | 24 | 103.83 ms | 8.46 | 1.73 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 3.05 µV | 3.83 | 0.78 | [-4.26, 13.38] |
| 4 to 2 | 24 | 0.78 µV | 2.66 | 0.54 | [-5.66, 4.55] |
| 4 to 3 | 24 | 0.67 µV | 2.23 | 0.45 | [-3.29, 5.30] |
| 4 to 4 | 24 | 1.50 µV | 2.34 | 0.48 | [-3.85, 6.90] |
| 4 to 5 | 24 | 2.92 µV | 5.44 | 1.11 | [-3.43, 19.20] |
| 4 to 6 | 24 | 1.51 µV | 2.95 | 0.60 | [-4.27, 6.93] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 487.33 ms | 35.71 | 7.29 | [428.00, 540.00] |
| 4 to 2 | 24 | 478.17 ms | 37.87 | 7.73 | [428.00, 540.00] |
| 4 to 3 | 24 | 475.83 ms | 33.43 | 6.82 | [428.00, 540.00] |
| 4 to 4 | 24 | 473.00 ms | 31.10 | 6.35 | [428.00, 524.00] |
| 4 to 5 | 24 | 490.83 ms | 37.70 | 7.70 | [428.00, 540.00] |
| 4 to 6 | 24 | 494.67 ms | 35.22 | 7.19 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 24 | 5.74 µV | 3.66 | 0.75 | [0.28, 12.03] |
| 4 to 2 | 24 | 4.37 µV | 4.34 | 0.89 | [-3.50, 14.41] |
| 4 to 3 | 24 | 4.97 µV | 3.60 | 0.73 | [-1.86, 11.65] |
| 4 to 4 | 24 | 1.58 µV | 3.98 | 0.81 | [-9.78, 8.96] |
| 4 to 5 | 24 | 4.65 µV | 5.32 | 1.09 | [-5.31, 13.88] |
| 4 to 6 | 24 | 5.29 µV | 3.69 | 0.75 | [0.59, 12.37] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1050.59, BIC = 1077.32
- **4 to 2 vs 4 to 1**: *β* = 1.35, *SE* = 2.452, *z* = 0.551, *p* = 0.581
- **4 to 3 vs 4 to 1**: *β* = 0.32, *SE* = 2.460, *z* = 0.131, *p* = 0.895
- **4 to 4 vs 4 to 1**: *β* = 1.34, *SE* = 2.452, *z* = 0.545, *p* = 0.586
- **4 to 5 vs 4 to 1**: *β* = -6.74, *SE* = 2.449, *z* = -2.752, *p* = 0.006
- **4 to 6 vs 4 to 1**: *β* = -1.89, *SE* = 2.449, *z* = -0.771, *p* = 0.441
- **SNR**: *β* = 0.76, *SE* = 0.556, *z* = 1.357, *p* = 0.175

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -1.35 | 2.45 | -0.55 | 0.581 | 0.995 | n.s. |
| 4 to 1 - 4 to 3 | -0.32 | 2.46 | -0.13 | 0.895 | 0.995 | n.s. |
| 4 to 1 - 4 to 4 | -1.34 | 2.45 | -0.54 | 0.586 | 0.995 | n.s. |
| 4 to 1 - 4 to 5 | 6.74 | 2.45 | 2.75 | 0.006 | 0.069 | n.s. |
| 4 to 1 - 4 to 6 | 1.89 | 2.45 | 0.77 | 0.441 | 0.983 | n.s. |
| 4 to 2 - 4 to 3 | 1.03 | 2.45 | 0.42 | 0.675 | 0.995 | n.s. |
| 4 to 2 - 4 to 4 | 0.02 | 2.45 | 0.01 | 0.995 | 0.995 | n.s. |
| 4 to 2 - 4 to 5 | 8.09 | 2.46 | 3.29 | < .001 | 0.015 | * |
| 4 to 2 - 4 to 6 | 3.24 | 2.46 | 1.32 | 0.187 | 0.874 | n.s. |
| 4 to 3 - 4 to 4 | -1.01 | 2.45 | -0.41 | 0.680 | 0.995 | n.s. |
| 4 to 3 - 4 to 5 | 7.06 | 2.47 | 2.86 | 0.004 | 0.053 | n.s. |
| 4 to 3 - 4 to 6 | 2.21 | 2.46 | 0.90 | 0.369 | 0.975 | n.s. |
| 4 to 4 - 4 to 5 | 8.08 | 2.46 | 3.29 | 0.001 | 0.015 | * |
| 4 to 4 - 4 to 6 | 3.22 | 2.45 | 1.31 | 0.189 | 0.874 | n.s. |
| 4 to 5 - 4 to 6 | -4.85 | 2.45 | -1.98 | 0.048 | 0.415 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.77, *p* = 0.021, η²_G = 0.087
- Greenhouse-Geisser corrected: *p* = 0.040 (ε = 0.684)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | -0.51 | 23 | = 0.779 | -0.12 [-0.53, 0.32] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 4 to 1 vs 4 to 4 | -0.42 | 23 | = 0.779 | -0.12 [-0.51, 0.34] | negligible | n.s. |
| 4 to 1 vs 4 to 5 | 2.26 | 23 | = 0.125 | 0.72 [0.02, 0.91] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 0.58 | 23 | = 0.779 | 0.19 [-0.31, 0.54] | negligible | n.s. |
| 4 to 2 vs 4 to 3 | 0.44 | 23 | = 0.779 | 0.13 [-0.33, 0.51] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 3.10 | 23 | = 0.026 | 0.92 [0.17, 1.09] | large | * |
| 4 to 2 vs 4 to 6 | 1.27 | 23 | = 0.465 | 0.33 [-0.17, 0.69] | small | n.s. |
| 4 to 3 vs 4 to 4 | -0.47 | 23 | = 0.779 | -0.14 [-0.52, 0.33] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 3.55 | 23 | = 0.025 | 0.82 [0.25, 1.20] | large | * |
| 4 to 3 vs 4 to 6 | 0.89 | 23 | = 0.722 | 0.21 [-0.24, 0.61] | small | n.s. |
| 4 to 4 vs 4 to 5 | 3.17 | 23 | = 0.026 | 0.96 [0.18, 1.11] | large | * |
| 4 to 4 vs 4 to 6 | 1.87 | 23 | = 0.185 | 0.34 [-0.06, 0.82] | small | n.s. |
| 4 to 5 vs 4 to 6 | -2.13 | 23 | = 0.133 | -0.57 [-0.88, 0.01] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 729.06, BIC = 755.79
- **4 to 2 vs 4 to 1**: *β* = 1.46, *SE* = 0.773, *z* = 1.889, *p* = 0.059
- **4 to 3 vs 4 to 1**: *β* = 1.40, *SE* = 0.776, *z* = 1.805, *p* = 0.071
- **4 to 4 vs 4 to 1**: *β* = 0.69, *SE* = 0.773, *z* = 0.890, *p* = 0.373
- **4 to 5 vs 4 to 1**: *β* = -1.34, *SE* = 0.772, *z* = -1.733, *p* = 0.083
- **4 to 6 vs 4 to 1**: *β* = 0.94, *SE* = 0.772, *z* = 1.224, *p* = 0.221
- **SNR**: *β* = -0.64, *SE* = 0.180, *z* = -3.528, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -1.46 | 0.77 | -1.89 | 0.059 | 0.487 | n.s. |
| 4 to 1 - 4 to 3 | -1.40 | 0.78 | -1.81 | 0.071 | 0.521 | n.s. |
| 4 to 1 - 4 to 4 | -0.69 | 0.77 | -0.89 | 0.373 | 0.931 | n.s. |
| 4 to 1 - 4 to 5 | 1.34 | 0.77 | 1.73 | 0.083 | 0.542 | n.s. |
| 4 to 1 - 4 to 6 | -0.95 | 0.77 | -1.22 | 0.221 | 0.864 | n.s. |
| 4 to 2 - 4 to 3 | 0.06 | 0.77 | 0.08 | 0.938 | 0.940 | n.s. |
| 4 to 2 - 4 to 4 | 0.77 | 0.77 | 1.00 | 0.317 | 0.931 | n.s. |
| 4 to 2 - 4 to 5 | 2.80 | 0.77 | 3.61 | < .001 | 0.005 | ** |
| 4 to 2 - 4 to 6 | 0.52 | 0.77 | 0.67 | 0.506 | 0.940 | n.s. |
| 4 to 3 - 4 to 4 | 0.71 | 0.77 | 0.92 | 0.357 | 0.931 | n.s. |
| 4 to 3 - 4 to 5 | 2.74 | 0.78 | 3.52 | < .001 | 0.006 | ** |
| 4 to 3 - 4 to 6 | 0.46 | 0.78 | 0.59 | 0.558 | 0.940 | n.s. |
| 4 to 4 - 4 to 5 | 2.03 | 0.77 | 2.62 | 0.009 | 0.101 | n.s. |
| 4 to 4 - 4 to 6 | -0.26 | 0.77 | -0.33 | 0.740 | 0.940 | n.s. |
| 4 to 5 - 4 to 6 | -2.28 | 0.77 | -2.96 | 0.003 | 0.040 | * |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.93, *p* = 0.003, η²_G = 0.107
- Greenhouse-Geisser corrected: *p* = 0.014 (ε = 0.568)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | -2.56 | 23 | = 0.065 | -0.58 [-0.97, -0.07] | medium | n.s. |
| 4 to 1 vs 4 to 3 | -3.31 | 23 | = 0.023 | -0.66 [-1.14, -0.21] | medium | * |
| 4 to 1 vs 4 to 4 | -1.30 | 23 | = 0.323 | -0.35 [-0.69, 0.17] | small | n.s. |
| 4 to 1 vs 4 to 5 | 1.34 | 23 | = 0.323 | 0.33 [-0.16, 0.70] | small | n.s. |
| 4 to 1 vs 4 to 6 | -1.00 | 23 | = 0.411 | -0.33 [-0.63, 0.22] | small | n.s. |
| 4 to 2 vs 4 to 3 | -0.09 | 23 | = 0.926 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 1.19 | 23 | = 0.335 | 0.34 [-0.19, 0.67] | small | n.s. |
| 4 to 2 vs 4 to 5 | 2.92 | 23 | = 0.039 | 0.71 [0.14, 1.05] | medium | * |
| 4 to 2 vs 4 to 6 | 0.86 | 23 | = 0.458 | 0.27 [-0.25, 0.60] | small | n.s. |
| 4 to 3 vs 4 to 4 | 1.49 | 23 | = 0.320 | 0.42 [-0.13, 0.74] | small | n.s. |
| 4 to 3 vs 4 to 5 | 3.47 | 23 | = 0.023 | 0.76 [0.24, 1.18] | medium | * |
| 4 to 3 vs 4 to 6 | 1.27 | 23 | = 0.323 | 0.33 [-0.17, 0.69] | small | n.s. |
| 4 to 4 vs 4 to 5 | 1.92 | 23 | = 0.177 | 0.56 [-0.05, 0.83] | medium | n.s. |
| 4 to 4 vs 4 to 6 | -0.11 | 23 | = 0.926 | -0.03 [-0.44, 0.40] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -1.90 | 23 | = 0.177 | -0.55 [-0.82, 0.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1207.68, BIC = 1234.40
- **4 to 2 vs 4 to 1**: *β* = -7.56, *SE* = 3.793, *z* = -1.993, *p* = 0.046
- **4 to 3 vs 4 to 1**: *β* = -13.01, *SE* = 3.892, *z* = -3.342, *p* = 0.001
- **4 to 4 vs 4 to 1**: *β* = -14.56, *SE* = 3.877, *z* = -3.756, *p* < .001
- **4 to 5 vs 4 to 1**: *β* = -16.46, *SE* = 3.865, *z* = -4.259, *p* < .001
- **4 to 6 vs 4 to 1**: *β* = -17.32, *SE* = 3.936, *z* = -4.401, *p* < .001
- **SNR**: *β* = 0.94, *SE* = 0.455, *z* = 2.057, *p* = 0.040

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 7.56 | 3.79 | 1.99 | 0.046 | 0.347 | n.s. |
| 4 to 1 - 4 to 3 | 13.01 | 3.89 | 3.34 | < .001 | 0.010 | ** |
| 4 to 1 - 4 to 4 | 14.56 | 3.88 | 3.76 | < .001 | 0.002 | ** |
| 4 to 1 - 4 to 5 | 16.46 | 3.86 | 4.26 | < .001 | < .001 | *** |
| 4 to 1 - 4 to 6 | 17.32 | 3.94 | 4.40 | < .001 | < .001 | *** |
| 4 to 2 - 4 to 3 | 5.45 | 3.77 | 1.44 | 0.149 | 0.676 | n.s. |
| 4 to 2 - 4 to 4 | 7.00 | 3.77 | 1.86 | 0.063 | 0.406 | n.s. |
| 4 to 2 - 4 to 5 | 8.90 | 3.76 | 2.37 | 0.018 | 0.166 | n.s. |
| 4 to 2 - 4 to 6 | 9.76 | 3.80 | 2.57 | 0.010 | 0.106 | n.s. |
| 4 to 3 - 4 to 4 | 1.55 | 3.75 | 0.41 | 0.678 | 0.942 | n.s. |
| 4 to 3 - 4 to 5 | 3.45 | 3.75 | 0.92 | 0.357 | 0.890 | n.s. |
| 4 to 3 - 4 to 6 | 4.31 | 3.75 | 1.15 | 0.250 | 0.822 | n.s. |
| 4 to 4 - 4 to 5 | 1.89 | 3.75 | 0.51 | 0.613 | 0.942 | n.s. |
| 4 to 4 - 4 to 6 | 2.76 | 3.75 | 0.73 | 0.462 | 0.917 | n.s. |
| 4 to 5 - 4 to 6 | 0.86 | 3.75 | 0.23 | 0.818 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.28, *p* = 0.001, η²_G = 0.082
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.70 | 23 | = 0.219 | 0.43 [-0.09, 0.78] | small | n.s. |
| 4 to 1 vs 4 to 3 | 2.94 | 23 | = 0.027 | 0.70 [0.14, 1.06] | medium | * |
| 4 to 1 vs 4 to 4 | 3.47 | 23 | = 0.010 | 0.71 [0.24, 1.18] | medium | * |
| 4 to 1 vs 4 to 5 | 3.51 | 23 | = 0.010 | 0.82 [0.24, 1.19] | large | * |
| 4 to 1 vs 4 to 6 | 3.88 | 23 | = 0.010 | 0.84 [0.31, 1.28] | large | * |
| 4 to 2 vs 4 to 3 | 1.33 | 23 | = 0.325 | 0.29 [-0.16, 0.70] | small | n.s. |
| 4 to 2 vs 4 to 4 | 1.45 | 23 | = 0.303 | 0.35 [-0.14, 0.73] | small | n.s. |
| 4 to 2 vs 4 to 5 | 2.40 | 23 | = 0.074 | 0.46 [0.04, 0.94] | small | n.s. |
| 4 to 2 vs 4 to 6 | 1.88 | 23 | = 0.184 | 0.48 [-0.05, 0.82] | small | n.s. |
| 4 to 3 vs 4 to 4 | 0.46 | 23 | = 0.694 | 0.09 [-0.33, 0.52] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 0.78 | 23 | = 0.558 | 0.20 [-0.27, 0.58] | small | n.s. |
| 4 to 3 vs 4 to 6 | 1.15 | 23 | = 0.393 | 0.22 [-0.19, 0.66] | small | n.s. |
| 4 to 4 vs 4 to 5 | 0.46 | 23 | = 0.694 | 0.10 [-0.33, 0.52] | negligible | n.s. |
| 4 to 4 vs 4 to 6 | 0.81 | 23 | = 0.558 | 0.12 [-0.26, 0.59] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 0.07 | 23 | = 0.943 | 0.02 [-0.41, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 680.16, BIC = 706.89
- **4 to 2 vs 4 to 1**: *β* = -1.82, *SE* = 0.611, *z* = -2.970, *p* = 0.003
- **4 to 3 vs 4 to 1**: *β* = -1.15, *SE* = 0.627, *z* = -1.832, *p* = 0.067
- **4 to 4 vs 4 to 1**: *β* = -0.71, *SE* = 0.625, *z* = -1.145, *p* = 0.252
- **4 to 5 vs 4 to 1**: *β* = -2.00, *SE* = 0.623, *z* = -3.203, *p* = 0.001
- **4 to 6 vs 4 to 1**: *β* = -1.29, *SE* = 0.634, *z* = -2.040, *p* = 0.041
- **SNR**: *β* = -0.52, *SE* = 0.073, *z* = -7.185, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 1.82 | 0.61 | 2.97 | 0.003 | 0.041 | * |
| 4 to 1 - 4 to 3 | 1.15 | 0.63 | 1.83 | 0.067 | 0.533 | n.s. |
| 4 to 1 - 4 to 4 | 0.72 | 0.62 | 1.14 | 0.252 | 0.896 | n.s. |
| 4 to 1 - 4 to 5 | 2.00 | 0.62 | 3.20 | 0.001 | 0.020 | * |
| 4 to 1 - 4 to 6 | 1.29 | 0.63 | 2.04 | 0.041 | 0.398 | n.s. |
| 4 to 2 - 4 to 3 | -0.67 | 0.61 | -1.10 | 0.273 | 0.896 | n.s. |
| 4 to 2 - 4 to 4 | -1.10 | 0.61 | -1.81 | 0.070 | 0.533 | n.s. |
| 4 to 2 - 4 to 5 | 0.18 | 0.61 | 0.30 | 0.768 | 0.946 | n.s. |
| 4 to 2 - 4 to 6 | -0.52 | 0.61 | -0.85 | 0.393 | 0.896 | n.s. |
| 4 to 3 - 4 to 4 | -0.43 | 0.60 | -0.72 | 0.473 | 0.896 | n.s. |
| 4 to 3 - 4 to 5 | 0.85 | 0.60 | 1.40 | 0.161 | 0.795 | n.s. |
| 4 to 3 - 4 to 6 | 0.14 | 0.60 | 0.24 | 0.811 | 0.946 | n.s. |
| 4 to 4 - 4 to 5 | 1.28 | 0.60 | 2.12 | 0.034 | 0.363 | n.s. |
| 4 to 4 - 4 to 6 | 0.58 | 0.60 | 0.96 | 0.339 | 0.896 | n.s. |
| 4 to 5 - 4 to 6 | -0.70 | 0.61 | -1.16 | 0.247 | 0.896 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.58, *p* < .001, η²_G = 0.090
- Greenhouse-Geisser corrected: *p* = 0.003 (ε = 0.702)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 3.90 | 23 | = 0.008 | 0.94 [0.31, 1.28] | large | ** |
| 4 to 1 vs 4 to 3 | 3.73 | 23 | = 0.008 | 0.95 [0.28, 1.24] | large | ** |
| 4 to 1 vs 4 to 4 | 2.29 | 23 | = 0.095 | 0.66 [0.02, 0.91] | medium | n.s. |
| 4 to 1 vs 4 to 5 | 3.35 | 23 | = 0.013 | 0.96 [0.22, 1.15] | large | * |
| 4 to 1 vs 4 to 6 | 3.25 | 23 | = 0.013 | 0.86 [0.20, 1.13] | large | * |
| 4 to 2 vs 4 to 3 | -0.22 | 23 | = 0.827 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | -1.06 | 23 | = 0.565 | -0.20 [-0.64, 0.21] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 0.84 | 23 | = 0.613 | 0.17 [-0.25, 0.60] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | 0.31 | 23 | = 0.816 | 0.05 [-0.36, 0.49] | negligible | n.s. |
| 4 to 3 vs 4 to 4 | -0.70 | 23 | = 0.667 | -0.16 [-0.57, 0.28] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 0.94 | 23 | = 0.592 | 0.21 [-0.23, 0.62] | small | n.s. |
| 4 to 3 vs 4 to 6 | 0.43 | 23 | = 0.771 | 0.10 [-0.33, 0.51] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | 1.35 | 23 | = 0.410 | 0.33 [-0.16, 0.71] | small | n.s. |
| 4 to 4 vs 4 to 6 | 2.04 | 23 | = 0.132 | 0.23 [-0.02, 0.86] | small | n.s. |
| 4 to 5 vs 4 to 6 | -0.49 | 23 | = 0.771 | -0.10 [-0.52, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1011.02, BIC = 1037.75
- **4 to 2 vs 4 to 1**: *β* = 0.40, *SE* = 2.090, *z* = 0.192, *p* = 0.848
- **4 to 3 vs 4 to 1**: *β* = -3.69, *SE* = 2.072, *z* = -1.779, *p* = 0.075
- **4 to 4 vs 4 to 1**: *β* = -1.21, *SE* = 2.068, *z* = -0.586, *p* = 0.558
- **4 to 5 vs 4 to 1**: *β* = -5.72, *SE* = 2.067, *z* = -2.769, *p* = 0.006
- **4 to 6 vs 4 to 1**: *β* = -6.00, *SE* = 2.053, *z* = -2.922, *p* = 0.003
- **SNR**: *β* = 0.36, *SE* = 0.395, *z* = 0.919, *p* = 0.358

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.40 | 2.09 | -0.19 | 0.848 | 0.977 | n.s. |
| 4 to 1 - 4 to 3 | 3.69 | 2.07 | 1.78 | 0.075 | 0.465 | n.s. |
| 4 to 1 - 4 to 4 | 1.21 | 2.07 | 0.59 | 0.558 | 0.914 | n.s. |
| 4 to 1 - 4 to 5 | 5.72 | 2.07 | 2.77 | 0.006 | 0.065 | n.s. |
| 4 to 1 - 4 to 6 | 6.00 | 2.05 | 2.92 | 0.003 | 0.044 | * |
| 4 to 2 - 4 to 3 | 4.09 | 2.05 | 2.00 | 0.046 | 0.344 | n.s. |
| 4 to 2 - 4 to 4 | 1.61 | 2.05 | 0.79 | 0.431 | 0.895 | n.s. |
| 4 to 2 - 4 to 5 | 6.12 | 2.05 | 2.99 | 0.003 | 0.038 | * |
| 4 to 2 - 4 to 6 | 6.40 | 2.06 | 3.11 | 0.002 | 0.028 | * |
| 4 to 3 - 4 to 4 | -2.48 | 2.04 | -1.21 | 0.226 | 0.833 | n.s. |
| 4 to 3 - 4 to 5 | 2.03 | 2.04 | 1.00 | 0.320 | 0.854 | n.s. |
| 4 to 3 - 4 to 6 | 2.31 | 2.05 | 1.13 | 0.260 | 0.836 | n.s. |
| 4 to 4 - 4 to 5 | 4.51 | 2.04 | 2.21 | 0.027 | 0.242 | n.s. |
| 4 to 4 - 4 to 6 | 4.79 | 2.05 | 2.34 | 0.019 | 0.194 | n.s. |
| 4 to 5 - 4 to 6 | 0.28 | 2.05 | 0.13 | 0.893 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.66, *p* = 0.004, η²_G = 0.098
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | 1.46 | 23 | = 0.297 | 0.49 [-0.13, 0.73] | small | n.s. |
| 4 to 1 vs 4 to 4 | 0.67 | 23 | = 0.586 | 0.18 [-0.29, 0.56] | negligible | n.s. |
| 4 to 1 vs 4 to 5 | 2.48 | 23 | = 0.078 | 0.77 [0.06, 0.95] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 2.34 | 23 | = 0.078 | 0.74 [0.03, 0.92] | medium | n.s. |
| 4 to 2 vs 4 to 3 | 1.94 | 23 | = 0.138 | 0.52 [-0.04, 0.84] | medium | n.s. |
| 4 to 2 vs 4 to 4 | 0.73 | 23 | = 0.586 | 0.19 [-0.28, 0.57] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 3.19 | 23 | = 0.035 | 0.81 [0.19, 1.12] | large | * |
| 4 to 2 vs 4 to 6 | 3.13 | 23 | = 0.035 | 0.77 [0.18, 1.10] | medium | * |
| 4 to 3 vs 4 to 4 | -1.09 | 23 | = 0.392 | -0.30 [-0.65, 0.21] | small | n.s. |
| 4 to 3 vs 4 to 5 | 1.17 | 23 | = 0.392 | 0.26 [-0.19, 0.67] | small | n.s. |
| 4 to 3 vs 4 to 6 | 1.14 | 23 | = 0.392 | 0.26 [-0.19, 0.66] | small | n.s. |
| 4 to 4 vs 4 to 5 | 2.30 | 23 | = 0.078 | 0.56 [0.02, 0.91] | medium | n.s. |
| 4 to 4 vs 4 to 6 | 2.62 | 23 | = 0.076 | 0.55 [0.08, 0.99] | medium | n.s. |
| 4 to 5 vs 4 to 6 | 0.10 | 23 | = 0.990 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 760.99, BIC = 787.72
- **4 to 2 vs 4 to 1**: *β* = -1.78, *SE* = 0.888, *z* = -2.005, *p* = 0.045
- **4 to 3 vs 4 to 1**: *β* = -1.99, *SE* = 0.881, *z* = -2.263, *p* = 0.024
- **4 to 4 vs 4 to 1**: *β* = -1.20, *SE* = 0.879, *z* = -1.360, *p* = 0.174
- **4 to 5 vs 4 to 1**: *β* = 0.21, *SE* = 0.878, *z* = 0.244, *p* = 0.808
- **4 to 6 vs 4 to 1**: *β* = -1.33, *SE* = 0.872, *z* = -1.524, *p* = 0.127
- **SNR**: *β* = 0.44, *SE* = 0.168, *z* = 2.639, *p* = 0.008

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 1.78 | 0.89 | 2.00 | 0.045 | 0.425 | n.s. |
| 4 to 1 - 4 to 3 | 1.99 | 0.88 | 2.26 | 0.024 | 0.268 | n.s. |
| 4 to 1 - 4 to 4 | 1.19 | 0.88 | 1.36 | 0.174 | 0.783 | n.s. |
| 4 to 1 - 4 to 5 | -0.21 | 0.88 | -0.24 | 0.808 | 0.993 | n.s. |
| 4 to 1 - 4 to 6 | 1.33 | 0.87 | 1.52 | 0.127 | 0.707 | n.s. |
| 4 to 2 - 4 to 3 | 0.21 | 0.87 | 0.24 | 0.808 | 0.993 | n.s. |
| 4 to 2 - 4 to 4 | -0.59 | 0.87 | -0.67 | 0.501 | 0.971 | n.s. |
| 4 to 2 - 4 to 5 | -1.99 | 0.87 | -2.29 | 0.022 | 0.267 | n.s. |
| 4 to 2 - 4 to 6 | -0.45 | 0.88 | -0.52 | 0.606 | 0.976 | n.s. |
| 4 to 3 - 4 to 4 | -0.80 | 0.87 | -0.92 | 0.359 | 0.955 | n.s. |
| 4 to 3 - 4 to 5 | -2.21 | 0.87 | -2.54 | 0.011 | 0.154 | n.s. |
| 4 to 3 - 4 to 6 | -0.66 | 0.87 | -0.76 | 0.447 | 0.971 | n.s. |
| 4 to 4 - 4 to 5 | -1.41 | 0.87 | -1.62 | 0.105 | 0.670 | n.s. |
| 4 to 4 - 4 to 6 | 0.13 | 0.87 | 0.15 | 0.877 | 0.993 | n.s. |
| 4 to 5 - 4 to 6 | 1.54 | 0.87 | 1.77 | 0.076 | 0.581 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.60, *p* = 0.029, η²_G = 0.072
- Greenhouse-Geisser corrected: *p* = 0.059 (ε = 0.608)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 2.92 | 23 | = 0.057 | 0.69 [0.14, 1.06] | medium | n.s. |
| 4 to 1 vs 4 to 3 | 3.40 | 23 | = 0.037 | 0.76 [0.22, 1.17] | medium | * |
| 4 to 1 vs 4 to 4 | 1.77 | 23 | = 0.272 | 0.49 [-0.08, 0.80] | small | n.s. |
| 4 to 1 vs 4 to 5 | 0.09 | 23 | = 0.989 | 0.03 [-0.40, 0.44] | negligible | n.s. |
| 4 to 1 vs 4 to 6 | 1.60 | 23 | = 0.306 | 0.45 [-0.11, 0.76] | small | n.s. |
| 4 to 2 vs 4 to 3 | 0.20 | 23 | = 0.971 | 0.04 [-0.38, 0.46] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | -1.27 | 23 | = 0.344 | -0.29 [-0.69, 0.17] | small | n.s. |
| 4 to 2 vs 4 to 5 | -2.04 | 23 | = 0.198 | -0.50 [-0.86, 0.02] | medium | n.s. |
| 4 to 2 vs 4 to 6 | -0.98 | 23 | = 0.424 | -0.26 [-0.63, 0.23] | small | n.s. |
| 4 to 3 vs 4 to 4 | -1.28 | 23 | = 0.344 | -0.36 [-0.69, 0.17] | small | n.s. |
| 4 to 3 vs 4 to 5 | -2.15 | 23 | = 0.198 | -0.54 [-0.88, 0.00] | medium | n.s. |
| 4 to 3 vs 4 to 6 | -1.45 | 23 | = 0.344 | -0.32 [-0.73, 0.14] | small | n.s. |
| 4 to 4 vs 4 to 5 | -1.21 | 23 | = 0.344 | -0.34 [-0.68, 0.18] | small | n.s. |
| 4 to 4 vs 4 to 6 | -0.01 | 23 | = 0.989 | -0.00 [-0.43, 0.42] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 1.17 | 23 | = 0.344 | 0.32 [-0.19, 0.67] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1433.27, BIC = 1460.00
- **4 to 2 vs 4 to 1**: *β* = -12.22, *SE* = 8.975, *z* = -1.361, *p* = 0.173
- **4 to 3 vs 4 to 1**: *β* = -13.31, *SE* = 8.851, *z* = -1.504, *p* = 0.133
- **4 to 4 vs 4 to 1**: *β* = -17.57, *SE* = 8.998, *z* = -1.952, *p* = 0.051
- **4 to 5 vs 4 to 1**: *β* = 1.15, *SE* = 8.898, *z* = 0.129, *p* = 0.898
- **4 to 6 vs 4 to 1**: *β* = 5.28, *SE* = 8.870, *z* = 0.595, *p* = 0.552
- **SNR**: *β* = -1.07, *SE* = 0.647, *z* = -1.657, *p* = 0.098

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 12.22 | 8.97 | 1.36 | 0.173 | 0.736 | n.s. |
| 4 to 1 - 4 to 3 | 13.31 | 8.85 | 1.50 | 0.133 | 0.710 | n.s. |
| 4 to 1 - 4 to 4 | 17.57 | 9.00 | 1.95 | 0.051 | 0.438 | n.s. |
| 4 to 1 - 4 to 5 | -1.15 | 8.90 | -0.13 | 0.898 | 0.991 | n.s. |
| 4 to 1 - 4 to 6 | -5.28 | 8.87 | -0.60 | 0.552 | 0.991 | n.s. |
| 4 to 2 - 4 to 3 | 1.09 | 8.82 | 0.12 | 0.902 | 0.991 | n.s. |
| 4 to 2 - 4 to 4 | 5.35 | 8.78 | 0.61 | 0.543 | 0.991 | n.s. |
| 4 to 2 - 4 to 5 | -13.36 | 8.79 | -1.52 | 0.129 | 0.710 | n.s. |
| 4 to 2 - 4 to 6 | -17.50 | 8.80 | -1.99 | 0.047 | 0.438 | n.s. |
| 4 to 3 - 4 to 4 | 4.26 | 8.83 | 0.48 | 0.629 | 0.991 | n.s. |
| 4 to 3 - 4 to 5 | -14.45 | 8.79 | -1.64 | 0.100 | 0.652 | n.s. |
| 4 to 3 - 4 to 6 | -18.59 | 8.78 | -2.12 | 0.034 | 0.379 | n.s. |
| 4 to 4 - 4 to 5 | -18.71 | 8.80 | -2.13 | 0.033 | 0.379 | n.s. |
| 4 to 4 - 4 to 6 | -22.85 | 8.81 | -2.59 | 0.010 | 0.134 | n.s. |
| 4 to 5 - 4 to 6 | -4.14 | 8.79 | -0.47 | 0.638 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.90, *p* = 0.100, η²_G = 0.052
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.23 | 23 | = 0.383 | 0.25 [-0.18, 0.68] | small | n.s. |
| 4 to 1 vs 4 to 3 | 1.31 | 23 | = 0.378 | 0.33 [-0.16, 0.70] | small | n.s. |
| 4 to 1 vs 4 to 4 | 1.46 | 23 | = 0.378 | 0.43 [-0.13, 0.73] | small | n.s. |
| 4 to 1 vs 4 to 5 | -0.35 | 23 | = 0.807 | -0.10 [-0.49, 0.35] | negligible | n.s. |
| 4 to 1 vs 4 to 6 | -0.89 | 23 | = 0.577 | -0.21 [-0.61, 0.24] | small | n.s. |
| 4 to 2 vs 4 to 3 | 0.25 | 23 | = 0.807 | 0.07 [-0.37, 0.47] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 0.54 | 23 | = 0.807 | 0.15 [-0.31, 0.53] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | -1.33 | 23 | = 0.378 | -0.34 [-0.70, 0.16] | small | n.s. |
| 4 to 2 vs 4 to 6 | -1.96 | 23 | = 0.283 | -0.45 [-0.84, 0.04] | small | n.s. |
| 4 to 3 vs 4 to 4 | 0.31 | 23 | = 0.807 | 0.09 [-0.36, 0.49] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | -1.72 | 23 | = 0.295 | -0.42 [-0.79, 0.08] | small | n.s. |
| 4 to 3 vs 4 to 6 | -2.20 | 23 | = 0.283 | -0.55 [-0.89, -0.01] | medium | n.s. |
| 4 to 4 vs 4 to 5 | -1.86 | 23 | = 0.283 | -0.52 [-0.82, 0.06] | medium | n.s. |
| 4 to 4 vs 4 to 6 | -2.66 | 23 | = 0.212 | -0.65 [-0.99, -0.09] | medium | n.s. |
| 4 to 5 vs 4 to 6 | -0.37 | 23 | = 0.807 | -0.11 [-0.50, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 762.15, BIC = 788.88
- **4 to 2 vs 4 to 1**: *β* = -0.93, *SE* = 0.800, *z* = -1.158, *p* = 0.247
- **4 to 3 vs 4 to 1**: *β* = -0.50, *SE* = 0.787, *z* = -0.638, *p* = 0.523
- **4 to 4 vs 4 to 1**: *β* = -3.68, *SE* = 0.803, *z* = -4.587, *p* < .001
- **4 to 5 vs 4 to 1**: *β* = -0.75, *SE* = 0.792, *z* = -0.943, *p* = 0.346
- **4 to 6 vs 4 to 1**: *β* = -0.15, *SE* = 0.789, *z* = -0.187, *p* = 0.852
- **SNR**: *β* = 0.16, *SE* = 0.062, *z* = 2.531, *p* = 0.011

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 0.93 | 0.80 | 1.16 | 0.247 | 0.941 | n.s. |
| 4 to 1 - 4 to 3 | 0.50 | 0.79 | 0.64 | 0.523 | 0.988 | n.s. |
| 4 to 1 - 4 to 4 | 3.68 | 0.80 | 4.59 | < .001 | < .001 | *** |
| 4 to 1 - 4 to 5 | 0.75 | 0.79 | 0.94 | 0.346 | 0.969 | n.s. |
| 4 to 1 - 4 to 6 | 0.15 | 0.79 | 0.19 | 0.852 | 0.988 | n.s. |
| 4 to 2 - 4 to 3 | -0.42 | 0.78 | -0.54 | 0.589 | 0.988 | n.s. |
| 4 to 2 - 4 to 4 | 2.75 | 0.78 | 3.53 | < .001 | 0.005 | ** |
| 4 to 2 - 4 to 5 | -0.18 | 0.78 | -0.23 | 0.818 | 0.988 | n.s. |
| 4 to 2 - 4 to 6 | -0.78 | 0.78 | -1.00 | 0.319 | 0.969 | n.s. |
| 4 to 3 - 4 to 4 | 3.18 | 0.78 | 4.05 | < .001 | < .001 | *** |
| 4 to 3 - 4 to 5 | 0.24 | 0.78 | 0.31 | 0.755 | 0.988 | n.s. |
| 4 to 3 - 4 to 6 | -0.36 | 0.78 | -0.45 | 0.649 | 0.988 | n.s. |
| 4 to 4 - 4 to 5 | -2.93 | 0.78 | -3.75 | < .001 | 0.002 | ** |
| 4 to 4 - 4 to 6 | -3.53 | 0.78 | -4.51 | < .001 | < .001 | *** |
| 4 to 5 - 4 to 6 | -0.60 | 0.78 | -0.77 | 0.443 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.60, *p* < .001, η²_G = 0.100
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.622)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.67 | 23 | = 0.273 | 0.34 [-0.09, 0.77] | small | n.s. |
| 4 to 1 vs 4 to 3 | 1.08 | 23 | = 0.485 | 0.21 [-0.21, 0.65] | small | n.s. |
| 4 to 1 vs 4 to 4 | 5.75 | 23 | < .001 | 1.09 [0.63, 1.72] | large | *** |
| 4 to 1 vs 4 to 5 | 1.19 | 23 | = 0.463 | 0.24 [-0.19, 0.67] | small | n.s. |
| 4 to 1 vs 4 to 6 | 0.95 | 23 | = 0.508 | 0.12 [-0.23, 0.62] | negligible | n.s. |
| 4 to 2 vs 4 to 3 | -0.91 | 23 | = 0.508 | -0.15 [-0.61, 0.24] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 2.82 | 23 | = 0.036 | 0.67 [0.12, 1.03] | medium | * |
| 4 to 2 vs 4 to 5 | -0.36 | 23 | = 0.755 | -0.06 [-0.50, 0.35] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | -1.42 | 23 | = 0.359 | -0.23 [-0.72, 0.14] | small | n.s. |
| 4 to 3 vs 4 to 4 | 3.76 | 23 | = 0.005 | 0.89 [0.29, 1.25] | large | ** |
| 4 to 3 vs 4 to 5 | 0.32 | 23 | = 0.755 | 0.07 [-0.36, 0.49] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | -0.55 | 23 | = 0.675 | -0.09 [-0.54, 0.31] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | -2.58 | 23 | = 0.050 | -0.65 [-0.98, -0.08] | medium | * |
| 4 to 4 vs 4 to 6 | -5.60 | 23 | < .001 | -0.97 [-1.69, -0.60] | large | *** |
| 4 to 5 vs 4 to 6 | -0.80 | 23 | = 0.538 | -0.14 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.021). Post-hoc tests revealed:
  - 4 to 2 showed greater latency than 4 to 5 (*d* = 0.92)
  - 4 to 3 showed greater latency than 4 to 5 (*d* = 0.82)
  - 4 to 4 showed greater latency than 4 to 5 (*d* = 0.96)
**Fz amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 4 to 1 showed smaller amplitude than 4 to 3 (*d* = -0.66)
  - 4 to 2 showed greater amplitude than 4 to 5 (*d* = 0.71)
  - 4 to 3 showed greater amplitude than 4 to 5 (*d* = 0.76)
**N1 latency:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 4 to 3 (*d* = 0.70)
  - 4 to 1 showed greater latency than 4 to 4 (*d* = 0.71)
  - 4 to 1 showed greater latency than 4 to 5 (*d* = 0.82)
  - 4 to 1 showed greater latency than 4 to 6 (*d* = 0.84)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 2 (*d* = 0.94)
  - 4 to 1 showed greater amplitude than 4 to 3 (*d* = 0.95)
  - 4 to 1 showed greater amplitude than 4 to 5 (*d* = 0.96)
  - 4 to 1 showed greater amplitude than 4 to 6 (*d* = 0.86)
**P1 latency:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - 4 to 2 showed greater latency than 4 to 5 (*d* = 0.81)
  - 4 to 2 showed greater latency than 4 to 6 (*d* = 0.77)
**P1 amplitude:** Significant main effect of condition (*p* = 0.029). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 3 (*d* = 0.76)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 4 (*d* = 1.09)
  - 4 to 2 showed greater amplitude than 4 to 4 (*d* = 0.67)
  - 4 to 3 showed greater amplitude than 4 to 4 (*d* = 0.89)
  - 4 to 4 showed smaller amplitude than 4 to 5 (*d* = -0.65)
  - 4 to 4 showed smaller amplitude than 4 to 6 (*d* = -0.97)

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
