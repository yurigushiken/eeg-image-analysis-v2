# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:28:08

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
| 1 to 3 | 24 | 100.00 ms | 11.80 | 2.41 | [88.00, 116.00] |
| 2 to 3 | 24 | 100.17 ms | 11.34 | 2.32 | [88.00, 116.00] |
| 3 to 3 | 24 | 104.50 ms | 11.99 | 2.45 | [88.00, 116.00] |
| 4 to 3 | 24 | 104.17 ms | 9.54 | 1.95 | [88.00, 116.00] |
| 5 to 3 | 24 | 102.83 ms | 10.18 | 2.08 | [88.00, 116.00] |
| 6 to 3 | 24 | 103.33 ms | 10.05 | 2.05 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -0.38 µV | 2.49 | 0.51 | [-5.86, 4.93] |
| 2 to 3 | 24 | -1.42 µV | 2.20 | 0.45 | [-5.76, 2.45] |
| 3 to 3 | 24 | -1.43 µV | 2.62 | 0.54 | [-8.81, 1.87] |
| 4 to 3 | 24 | -0.79 µV | 2.18 | 0.44 | [-6.08, 2.67] |
| 5 to 3 | 24 | -2.76 µV | 2.09 | 0.43 | [-6.90, 1.42] |
| 6 to 3 | 24 | -1.91 µV | 1.63 | 0.33 | [-5.28, 1.40] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 170.50 ms | 23.88 | 4.87 | [140.00, 216.00] |
| 2 to 3 | 24 | 170.83 ms | 20.95 | 4.28 | [140.00, 208.00] |
| 3 to 3 | 24 | 172.17 ms | 21.25 | 4.34 | [140.00, 216.00] |
| 4 to 3 | 24 | 176.67 ms | 20.04 | 4.09 | [152.00, 216.00] |
| 5 to 3 | 24 | 173.83 ms | 17.13 | 3.50 | [140.00, 208.00] |
| 6 to 3 | 24 | 176.50 ms | 16.61 | 3.39 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.33 µV | 2.66 | 0.54 | [-12.51, -2.34] |
| 2 to 3 | 24 | -5.03 µV | 2.43 | 0.50 | [-10.61, 0.67] |
| 3 to 3 | 24 | -5.18 µV | 1.95 | 0.40 | [-10.83, -1.55] |
| 4 to 3 | 24 | -6.07 µV | 2.77 | 0.57 | [-10.92, 1.75] |
| 5 to 3 | 24 | -6.05 µV | 2.71 | 0.55 | [-12.11, -1.76] |
| 6 to 3 | 24 | -6.55 µV | 2.33 | 0.48 | [-11.28, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 102.17 ms | 10.21 | 2.08 | [92.00, 116.00] |
| 2 to 3 | 24 | 104.50 ms | 10.44 | 2.13 | [92.00, 116.00] |
| 3 to 3 | 24 | 106.33 ms | 10.54 | 2.15 | [92.00, 116.00] |
| 4 to 3 | 24 | 102.50 ms | 9.42 | 1.92 | [92.00, 116.00] |
| 5 to 3 | 24 | 107.83 ms | 9.10 | 1.86 | [92.00, 116.00] |
| 6 to 3 | 24 | 106.17 ms | 9.65 | 1.97 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 0.90 µV | 2.85 | 0.58 | [-6.53, 7.47] |
| 2 to 3 | 24 | 1.44 µV | 2.46 | 0.50 | [-4.20, 6.87] |
| 3 to 3 | 24 | 1.55 µV | 2.89 | 0.59 | [-3.19, 8.96] |
| 4 to 3 | 24 | 0.78 µV | 2.26 | 0.46 | [-3.29, 5.30] |
| 5 to 3 | 24 | 1.95 µV | 2.06 | 0.42 | [-3.07, 4.61] |
| 6 to 3 | 24 | 1.70 µV | 2.28 | 0.47 | [-3.06, 7.81] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 454.33 ms | 38.17 | 7.79 | [392.00, 516.00] |
| 2 to 3 | 24 | 452.83 ms | 43.58 | 8.90 | [392.00, 528.00] |
| 3 to 3 | 24 | 441.50 ms | 42.67 | 8.71 | [392.00, 528.00] |
| 4 to 3 | 24 | 464.17 ms | 39.85 | 8.13 | [392.00, 528.00] |
| 5 to 3 | 24 | 461.67 ms | 30.44 | 6.21 | [392.00, 528.00] |
| 6 to 3 | 24 | 461.00 ms | 33.53 | 6.85 | [396.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 5.35 µV | 4.13 | 0.84 | [-1.55, 14.25] |
| 2 to 3 | 24 | 4.88 µV | 4.16 | 0.85 | [-3.39, 13.70] |
| 3 to 3 | 24 | 3.31 µV | 3.27 | 0.67 | [-5.24, 9.60] |
| 4 to 3 | 24 | 5.08 µV | 3.49 | 0.71 | [-1.86, 11.65] |
| 5 to 3 | 24 | 4.85 µV | 3.24 | 0.66 | [-3.30, 10.28] |
| 6 to 3 | 24 | 5.34 µV | 4.25 | 0.87 | [-2.53, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1104.36, BIC = 1131.09
- **2 to 3 vs 1 to 3**: *β* = 0.39, *SE* = 2.943, *z* = 0.132, *p* = 0.895
- **3 to 3 vs 1 to 3**: *β* = 4.86, *SE* = 2.956, *z* = 1.643, *p* = 0.100
- **4 to 3 vs 1 to 3**: *β* = 4.59, *SE* = 2.966, *z* = 1.549, *p* = 0.121
- **5 to 3 vs 1 to 3**: *β* = 2.61, *SE* = 2.943, *z* = 0.888, *p* = 0.375
- **6 to 3 vs 1 to 3**: *β* = 3.69, *SE* = 2.957, *z* = 1.249, *p* = 0.212
- **SNR**: *β* = 0.71, *SE* = 0.723, *z* = 0.984, *p* = 0.325

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.39 | 2.94 | -0.13 | 0.895 | 0.997 | n.s. |
| 1 to 3 - 3 to 3 | -4.86 | 2.96 | -1.64 | 0.100 | 0.796 | n.s. |
| 1 to 3 - 4 to 3 | -4.59 | 2.97 | -1.55 | 0.121 | 0.837 | n.s. |
| 1 to 3 - 5 to 3 | -2.61 | 2.94 | -0.89 | 0.375 | 0.985 | n.s. |
| 1 to 3 - 6 to 3 | -3.69 | 2.96 | -1.25 | 0.212 | 0.927 | n.s. |
| 2 to 3 - 3 to 3 | -4.47 | 2.94 | -1.52 | 0.128 | 0.837 | n.s. |
| 2 to 3 - 4 to 3 | -4.20 | 2.94 | -1.43 | 0.153 | 0.864 | n.s. |
| 2 to 3 - 5 to 3 | -2.22 | 2.97 | -0.75 | 0.454 | 0.992 | n.s. |
| 2 to 3 - 6 to 3 | -3.30 | 2.94 | -1.12 | 0.261 | 0.951 | n.s. |
| 3 to 3 - 4 to 3 | 0.26 | 2.93 | 0.09 | 0.929 | 0.997 | n.s. |
| 3 to 3 - 5 to 3 | 2.24 | 2.99 | 0.75 | 0.453 | 0.992 | n.s. |
| 3 to 3 - 6 to 3 | 1.16 | 2.93 | 0.40 | 0.692 | 0.997 | n.s. |
| 4 to 3 - 5 to 3 | 1.98 | 3.01 | 0.66 | 0.510 | 0.992 | n.s. |
| 4 to 3 - 6 to 3 | 0.90 | 2.93 | 0.31 | 0.759 | 0.997 | n.s. |
| 5 to 3 - 6 to 3 | -1.08 | 2.99 | -0.36 | 0.718 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.513, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.05 | 23 | = 0.962 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | -1.34 | 23 | = 0.706 | -0.38 [-0.70, 0.16] | small | n.s. |
| 1 to 3 vs 4 to 3 | -1.30 | 23 | = 0.706 | -0.39 [-0.70, 0.16] | small | n.s. |
| 1 to 3 vs 5 to 3 | -0.90 | 23 | = 0.706 | -0.26 [-0.61, 0.24] | small | n.s. |
| 1 to 3 vs 6 to 3 | -1.10 | 23 | = 0.706 | -0.30 [-0.65, 0.20] | small | n.s. |
| 2 to 3 vs 3 to 3 | -1.21 | 23 | = 0.706 | -0.37 [-0.68, 0.18] | small | n.s. |
| 2 to 3 vs 4 to 3 | -1.61 | 23 | = 0.706 | -0.38 [-0.76, 0.10] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.98 | 23 | = 0.706 | -0.25 [-0.63, 0.23] | small | n.s. |
| 2 to 3 vs 6 to 3 | -1.06 | 23 | = 0.706 | -0.30 [-0.64, 0.21] | small | n.s. |
| 3 to 3 vs 4 to 3 | 0.12 | 23 | = 0.962 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| 3 to 3 vs 5 to 3 | 0.61 | 23 | = 0.913 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| 3 to 3 vs 6 to 3 | 0.37 | 23 | = 0.950 | 0.11 [-0.35, 0.50] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 0.50 | 23 | = 0.931 | 0.14 [-0.32, 0.53] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.31 | 23 | = 0.950 | 0.09 [-0.36, 0.49] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.19 | 23 | = 0.962 | -0.05 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 628.25, BIC = 654.98
- **2 to 3 vs 1 to 3**: *β* = -1.09, *SE* = 0.526, *z* = -2.079, *p* = 0.038
- **3 to 3 vs 1 to 3**: *β* = -1.14, *SE* = 0.528, *z* = -2.157, *p* = 0.031
- **4 to 3 vs 1 to 3**: *β* = -0.52, *SE* = 0.530, *z* = -0.981, *p* = 0.327
- **5 to 3 vs 1 to 3**: *β* = -2.32, *SE* = 0.526, *z* = -4.417, *p* < .001
- **6 to 3 vs 1 to 3**: *β* = -1.63, *SE* = 0.529, *z* = -3.078, *p* = 0.002
- **SNR**: *β* = -0.18, *SE* = 0.136, *z* = -1.332, *p* = 0.183

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 1.09 | 0.53 | 2.08 | 0.038 | 0.273 | n.s. |
| 1 to 3 - 3 to 3 | 1.14 | 0.53 | 2.16 | 0.031 | 0.270 | n.s. |
| 1 to 3 - 4 to 3 | 0.52 | 0.53 | 0.98 | 0.327 | 0.803 | n.s. |
| 1 to 3 - 5 to 3 | 2.32 | 0.53 | 4.42 | < .001 | < .001 | *** |
| 1 to 3 - 6 to 3 | 1.63 | 0.53 | 3.08 | 0.002 | 0.027 | * |
| 2 to 3 - 3 to 3 | 0.05 | 0.52 | 0.09 | 0.929 | 0.929 | n.s. |
| 2 to 3 - 4 to 3 | -0.57 | 0.53 | -1.09 | 0.276 | 0.803 | n.s. |
| 2 to 3 - 5 to 3 | 1.23 | 0.53 | 2.32 | 0.021 | 0.221 | n.s. |
| 2 to 3 - 6 to 3 | 0.53 | 0.52 | 1.02 | 0.309 | 0.803 | n.s. |
| 3 to 3 - 4 to 3 | -0.62 | 0.52 | -1.18 | 0.237 | 0.803 | n.s. |
| 3 to 3 - 5 to 3 | 1.18 | 0.54 | 2.21 | 0.027 | 0.262 | n.s. |
| 3 to 3 - 6 to 3 | 0.49 | 0.52 | 0.93 | 0.353 | 0.803 | n.s. |
| 4 to 3 - 5 to 3 | 1.80 | 0.54 | 3.35 | < .001 | 0.011 | * |
| 4 to 3 - 6 to 3 | 1.11 | 0.52 | 2.11 | 0.035 | 0.273 | n.s. |
| 5 to 3 - 6 to 3 | -0.70 | 0.54 | -1.30 | 0.194 | 0.780 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.86, *p* < .001, η²_G = 0.110
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 1.58 | 23 | = 0.213 | 0.44 [-0.11, 0.76] | small | n.s. |
| 1 to 3 vs 3 to 3 | 1.87 | 23 | = 0.159 | 0.41 [-0.06, 0.82] | small | n.s. |
| 1 to 3 vs 4 to 3 | 0.87 | 23 | = 0.421 | 0.18 [-0.25, 0.60] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 3.98 | 23 | = 0.009 | 1.03 [0.33, 1.30] | large | ** |
| 1 to 3 vs 6 to 3 | 3.21 | 23 | = 0.020 | 0.73 [0.19, 1.12] | medium | * |
| 2 to 3 vs 3 to 3 | 0.02 | 23 | = 0.984 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -0.94 | 23 | = 0.410 | -0.29 [-0.62, 0.23] | small | n.s. |
| 2 to 3 vs 5 to 3 | 2.40 | 23 | = 0.070 | 0.62 [0.04, 0.94] | medium | n.s. |
| 2 to 3 vs 6 to 3 | 1.02 | 23 | = 0.396 | 0.26 [-0.22, 0.64] | small | n.s. |
| 3 to 3 vs 4 to 3 | -1.49 | 23 | = 0.225 | -0.26 [-0.74, 0.13] | small | n.s. |
| 3 to 3 vs 5 to 3 | 2.35 | 23 | = 0.070 | 0.56 [0.03, 0.92] | medium | n.s. |
| 3 to 3 vs 6 to 3 | 1.14 | 23 | = 0.362 | 0.22 [-0.20, 0.66] | small | n.s. |
| 4 to 3 vs 5 to 3 | 3.66 | 23 | = 0.010 | 0.92 [0.27, 1.22] | large | ** |
| 4 to 3 vs 6 to 3 | 3.05 | 23 | = 0.021 | 0.58 [0.16, 1.08] | medium | * |
| 5 to 3 vs 6 to 3 | -1.69 | 23 | = 0.196 | -0.45 [-0.78, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1228.14, BIC = 1254.87
- **2 to 3 vs 1 to 3**: *β* = 1.32, *SE* = 3.982, *z* = 0.332, *p* = 0.740
- **3 to 3 vs 1 to 3**: *β* = 2.90, *SE* = 4.012, *z* = 0.723, *p* = 0.470
- **4 to 3 vs 1 to 3**: *β* = 6.52, *SE* = 3.934, *z* = 1.659, *p* = 0.097
- **5 to 3 vs 1 to 3**: *β* = 3.82, *SE* = 3.940, *z* = 0.970, *p* = 0.332
- **6 to 3 vs 1 to 3**: *β* = 6.11, *SE* = 3.927, *z* = 1.555, *p* = 0.120
- **SNR**: *β* = 0.78, *SE* = 0.521, *z* = 1.498, *p* = 0.134

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -1.32 | 3.98 | -0.33 | 0.740 | 0.994 | n.s. |
| 1 to 3 - 3 to 3 | -2.90 | 4.01 | -0.72 | 0.470 | 0.994 | n.s. |
| 1 to 3 - 4 to 3 | -6.52 | 3.93 | -1.66 | 0.097 | 0.784 | n.s. |
| 1 to 3 - 5 to 3 | -3.82 | 3.94 | -0.97 | 0.332 | 0.988 | n.s. |
| 1 to 3 - 6 to 3 | -6.11 | 3.93 | -1.55 | 0.120 | 0.833 | n.s. |
| 2 to 3 - 3 to 3 | -1.58 | 3.93 | -0.40 | 0.688 | 0.994 | n.s. |
| 2 to 3 - 4 to 3 | -5.20 | 3.95 | -1.32 | 0.188 | 0.933 | n.s. |
| 2 to 3 - 5 to 3 | -2.50 | 3.94 | -0.63 | 0.526 | 0.994 | n.s. |
| 2 to 3 - 6 to 3 | -4.78 | 3.97 | -1.20 | 0.228 | 0.955 | n.s. |
| 3 to 3 - 4 to 3 | -3.62 | 3.97 | -0.91 | 0.361 | 0.989 | n.s. |
| 3 to 3 - 5 to 3 | -0.92 | 3.96 | -0.23 | 0.816 | 0.994 | n.s. |
| 3 to 3 - 6 to 3 | -3.21 | 4.00 | -0.80 | 0.423 | 0.993 | n.s. |
| 4 to 3 - 5 to 3 | 2.70 | 3.93 | 0.69 | 0.492 | 0.994 | n.s. |
| 4 to 3 - 6 to 3 | 0.42 | 3.93 | 0.11 | 0.915 | 0.994 | n.s. |
| 5 to 3 - 6 to 3 | -2.28 | 3.93 | -0.58 | 0.562 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.89, *p* = 0.490, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.08 | 23 | = 0.957 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | -0.43 | 23 | = 0.835 | -0.07 [-0.51, 0.33] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | -1.36 | 23 | = 0.598 | -0.28 [-0.71, 0.15] | small | n.s. |
| 1 to 3 vs 5 to 3 | -0.80 | 23 | = 0.750 | -0.16 [-0.59, 0.26] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -1.42 | 23 | = 0.598 | -0.29 [-0.72, 0.14] | small | n.s. |
| 2 to 3 vs 3 to 3 | -0.26 | 23 | = 0.922 | -0.06 [-0.48, 0.37] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -1.21 | 23 | = 0.598 | -0.28 [-0.68, 0.18] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.75 | 23 | = 0.750 | -0.16 [-0.58, 0.27] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -1.28 | 23 | = 0.598 | -0.30 [-0.69, 0.17] | small | n.s. |
| 3 to 3 vs 4 to 3 | -1.27 | 23 | = 0.598 | -0.22 [-0.69, 0.17] | small | n.s. |
| 3 to 3 vs 5 to 3 | -0.44 | 23 | = 0.835 | -0.09 [-0.51, 0.33] | negligible | n.s. |
| 3 to 3 vs 6 to 3 | -1.27 | 23 | = 0.598 | -0.23 [-0.69, 0.17] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.69 | 23 | = 0.750 | 0.15 [-0.28, 0.56] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.05 | 23 | = 0.957 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.77 | 23 | = 0.750 | -0.16 [-0.58, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 616.64, BIC = 643.37
- **2 to 3 vs 1 to 3**: *β* = 0.76, *SE* = 0.513, *z* = 1.484, *p* = 0.138
- **3 to 3 vs 1 to 3**: *β* = 0.48, *SE* = 0.516, *z* = 0.928, *p* = 0.354
- **4 to 3 vs 1 to 3**: *β* = 0.07, *SE* = 0.507, *z* = 0.127, *p* = 0.899
- **5 to 3 vs 1 to 3**: *β* = 0.01, *SE* = 0.508, *z* = 0.030, *p* = 0.976
- **6 to 3 vs 1 to 3**: *β* = -0.28, *SE* = 0.506, *z* = -0.553, *p* = 0.580
- **SNR**: *β* = -0.42, *SE* = 0.064, *z* = -6.649, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.76 | 0.51 | -1.48 | 0.138 | 0.875 | n.s. |
| 1 to 3 - 3 to 3 | -0.48 | 0.52 | -0.93 | 0.354 | 0.987 | n.s. |
| 1 to 3 - 4 to 3 | -0.06 | 0.51 | -0.13 | 0.899 | 0.999 | n.s. |
| 1 to 3 - 5 to 3 | -0.02 | 0.51 | -0.03 | 0.976 | 0.999 | n.s. |
| 1 to 3 - 6 to 3 | 0.28 | 0.51 | 0.55 | 0.580 | 0.993 | n.s. |
| 2 to 3 - 3 to 3 | 0.28 | 0.51 | 0.56 | 0.578 | 0.993 | n.s. |
| 2 to 3 - 4 to 3 | 0.70 | 0.51 | 1.37 | 0.171 | 0.875 | n.s. |
| 2 to 3 - 5 to 3 | 0.75 | 0.51 | 1.47 | 0.142 | 0.875 | n.s. |
| 2 to 3 - 6 to 3 | 1.04 | 0.51 | 2.03 | 0.042 | 0.474 | n.s. |
| 3 to 3 - 4 to 3 | 0.41 | 0.51 | 0.81 | 0.418 | 0.987 | n.s. |
| 3 to 3 - 5 to 3 | 0.46 | 0.51 | 0.91 | 0.363 | 0.987 | n.s. |
| 3 to 3 - 6 to 3 | 0.76 | 0.51 | 1.47 | 0.140 | 0.875 | n.s. |
| 4 to 3 - 5 to 3 | 0.05 | 0.51 | 0.10 | 0.922 | 0.999 | n.s. |
| 4 to 3 - 6 to 3 | 0.34 | 0.51 | 0.68 | 0.497 | 0.992 | n.s. |
| 5 to 3 - 6 to 3 | 0.30 | 0.51 | 0.58 | 0.561 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.30, *p* = 0.049, η²_G = 0.051
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -2.90 | 23 | = 0.056 | -0.51 [-1.05, -0.13] | medium | n.s. |
| 1 to 3 vs 3 to 3 | -2.81 | 23 | = 0.056 | -0.49 [-1.03, -0.12] | small | n.s. |
| 1 to 3 vs 4 to 3 | -0.47 | 23 | = 0.808 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.40 | 23 | = 0.808 | -0.10 [-0.50, 0.34] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | 0.39 | 23 | = 0.808 | 0.09 [-0.34, 0.50] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 0.32 | 23 | = 0.809 | 0.07 [-0.36, 0.49] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 1.43 | 23 | = 0.310 | 0.40 [-0.14, 0.72] | small | n.s. |
| 2 to 3 vs 5 to 3 | 1.85 | 23 | = 0.231 | 0.39 [-0.06, 0.82] | small | n.s. |
| 2 to 3 vs 6 to 3 | 2.72 | 23 | = 0.056 | 0.64 [0.10, 1.01] | medium | n.s. |
| 3 to 3 vs 4 to 3 | 1.49 | 23 | = 0.310 | 0.37 [-0.13, 0.74] | small | n.s. |
| 3 to 3 vs 5 to 3 | 1.47 | 23 | = 0.310 | 0.37 [-0.13, 0.73] | small | n.s. |
| 3 to 3 vs 6 to 3 | 2.63 | 23 | = 0.056 | 0.64 [0.09, 0.99] | medium | n.s. |
| 4 to 3 vs 5 to 3 | -0.03 | 23 | = 0.974 | -0.01 [-0.43, 0.42] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.74 | 23 | = 0.701 | 0.19 [-0.27, 0.58] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.90 | 23 | = 0.629 | 0.20 [-0.24, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1067.36, BIC = 1094.08
- **2 to 3 vs 1 to 3**: *β* = 2.16, *SE* = 2.459, *z* = 0.878, *p* = 0.380
- **3 to 3 vs 1 to 3**: *β* = 4.02, *SE* = 2.455, *z* = 1.638, *p* = 0.101
- **4 to 3 vs 1 to 3**: *β* = 0.25, *SE* = 2.450, *z* = 0.103, *p* = 0.918
- **5 to 3 vs 1 to 3**: *β* = 5.69, *SE* = 2.447, *z* = 2.325, *p* = 0.020
- **6 to 3 vs 1 to 3**: *β* = 3.84, *SE* = 2.457, *z* = 1.561, *p* = 0.118
- **SNR**: *β* = -0.36, *SE* = 0.491, *z* = -0.740, *p* = 0.459

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -2.16 | 2.46 | -0.88 | 0.380 | 0.978 | n.s. |
| 1 to 3 - 3 to 3 | -4.02 | 2.46 | -1.64 | 0.101 | 0.751 | n.s. |
| 1 to 3 - 4 to 3 | -0.25 | 2.45 | -0.10 | 0.918 | 0.993 | n.s. |
| 1 to 3 - 5 to 3 | -5.69 | 2.45 | -2.32 | 0.020 | 0.262 | n.s. |
| 1 to 3 - 6 to 3 | -3.84 | 2.46 | -1.56 | 0.118 | 0.780 | n.s. |
| 2 to 3 - 3 to 3 | -1.86 | 2.45 | -0.76 | 0.446 | 0.982 | n.s. |
| 2 to 3 - 4 to 3 | 1.91 | 2.45 | 0.78 | 0.437 | 0.982 | n.s. |
| 2 to 3 - 5 to 3 | -3.53 | 2.46 | -1.43 | 0.151 | 0.787 | n.s. |
| 2 to 3 - 6 to 3 | -1.68 | 2.45 | -0.69 | 0.493 | 0.982 | n.s. |
| 3 to 3 - 4 to 3 | 3.77 | 2.45 | 1.54 | 0.124 | 0.780 | n.s. |
| 3 to 3 - 5 to 3 | -1.67 | 2.46 | -0.68 | 0.497 | 0.982 | n.s. |
| 3 to 3 - 6 to 3 | 0.19 | 2.45 | 0.08 | 0.940 | 0.993 | n.s. |
| 4 to 3 - 5 to 3 | -5.44 | 2.45 | -2.22 | 0.027 | 0.314 | n.s. |
| 4 to 3 - 6 to 3 | -3.58 | 2.45 | -1.46 | 0.143 | 0.787 | n.s. |
| 5 to 3 - 6 to 3 | 1.85 | 2.46 | 0.75 | 0.451 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.63, *p* = 0.157, η²_G = 0.043
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.78 | 23 | = 0.657 | -0.23 [-0.58, 0.27] | small | n.s. |
| 1 to 3 vs 3 to 3 | -1.54 | 23 | = 0.344 | -0.40 [-0.75, 0.12] | small | n.s. |
| 1 to 3 vs 4 to 3 | -0.13 | 23 | = 0.936 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -2.47 | 23 | = 0.153 | -0.59 [-0.95, -0.06] | medium | n.s. |
| 1 to 3 vs 6 to 3 | -2.30 | 23 | = 0.153 | -0.40 [-0.92, -0.03] | small | n.s. |
| 2 to 3 vs 3 to 3 | -0.59 | 23 | = 0.657 | -0.17 [-0.54, 0.30] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 0.64 | 23 | = 0.657 | 0.20 [-0.29, 0.55] | small | n.s. |
| 2 to 3 vs 5 to 3 | -1.08 | 23 | = 0.622 | -0.34 [-0.65, 0.21] | small | n.s. |
| 2 to 3 vs 6 to 3 | -0.58 | 23 | = 0.657 | -0.17 [-0.54, 0.31] | negligible | n.s. |
| 3 to 3 vs 4 to 3 | 1.82 | 23 | = 0.306 | 0.38 [-0.06, 0.81] | small | n.s. |
| 3 to 3 vs 5 to 3 | -0.83 | 23 | = 0.657 | -0.15 [-0.59, 0.26] | negligible | n.s. |
| 3 to 3 vs 6 to 3 | 0.08 | 23 | = 0.936 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -2.55 | 23 | = 0.153 | -0.58 [-0.97, -0.07] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -1.54 | 23 | = 0.344 | -0.38 [-0.75, 0.12] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.84 | 23 | = 0.657 | 0.18 [-0.25, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 652.32, BIC = 679.05
- **2 to 3 vs 1 to 3**: *β* = 0.63, *SE* = 0.563, *z* = 1.121, *p* = 0.262
- **3 to 3 vs 1 to 3**: *β* = 0.73, *SE* = 0.562, *z* = 1.296, *p* = 0.195
- **4 to 3 vs 1 to 3**: *β* = -0.08, *SE* = 0.561, *z* = -0.144, *p* = 0.886
- **5 to 3 vs 1 to 3**: *β* = 1.04, *SE* = 0.560, *z* = 1.859, *p* = 0.063
- **6 to 3 vs 1 to 3**: *β* = 0.89, *SE* = 0.563, *z* = 1.580, *p* = 0.114
- **SNR**: *β* = 0.19, *SE* = 0.114, *z* = 1.677, *p* = 0.093

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.63 | 0.56 | -1.12 | 0.262 | 0.912 | n.s. |
| 1 to 3 - 3 to 3 | -0.73 | 0.56 | -1.30 | 0.195 | 0.886 | n.s. |
| 1 to 3 - 4 to 3 | 0.08 | 0.56 | 0.14 | 0.886 | 0.997 | n.s. |
| 1 to 3 - 5 to 3 | -1.04 | 0.56 | -1.86 | 0.063 | 0.598 | n.s. |
| 1 to 3 - 6 to 3 | -0.89 | 0.56 | -1.58 | 0.114 | 0.766 | n.s. |
| 2 to 3 - 3 to 3 | -0.10 | 0.56 | -0.17 | 0.863 | 0.997 | n.s. |
| 2 to 3 - 4 to 3 | 0.71 | 0.56 | 1.27 | 0.204 | 0.886 | n.s. |
| 2 to 3 - 5 to 3 | -0.41 | 0.56 | -0.73 | 0.467 | 0.988 | n.s. |
| 2 to 3 - 6 to 3 | -0.26 | 0.56 | -0.46 | 0.645 | 0.994 | n.s. |
| 3 to 3 - 4 to 3 | 0.81 | 0.56 | 1.44 | 0.149 | 0.831 | n.s. |
| 3 to 3 - 5 to 3 | -0.31 | 0.56 | -0.56 | 0.578 | 0.994 | n.s. |
| 3 to 3 - 6 to 3 | -0.16 | 0.56 | -0.29 | 0.774 | 0.997 | n.s. |
| 4 to 3 - 5 to 3 | -1.12 | 0.56 | -2.00 | 0.046 | 0.503 | n.s. |
| 4 to 3 - 6 to 3 | -0.97 | 0.56 | -1.73 | 0.084 | 0.679 | n.s. |
| 5 to 3 - 6 to 3 | 0.15 | 0.56 | 0.27 | 0.787 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.27, *p* = 0.281, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.74 | 23 | = 0.780 | -0.20 [-0.58, 0.27] | small | n.s. |
| 1 to 3 vs 3 to 3 | -1.05 | 23 | = 0.676 | -0.23 [-0.64, 0.21] | small | n.s. |
| 1 to 3 vs 4 to 3 | 0.22 | 23 | = 0.867 | 0.05 [-0.38, 0.47] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -2.17 | 23 | = 0.389 | -0.42 [-0.88, 0.00] | small | n.s. |
| 1 to 3 vs 6 to 3 | -1.48 | 23 | = 0.545 | -0.31 [-0.73, 0.13] | small | n.s. |
| 2 to 3 vs 3 to 3 | -0.17 | 23 | = 0.867 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 0.99 | 23 | = 0.676 | 0.28 [-0.22, 0.63] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.93 | 23 | = 0.676 | -0.23 [-0.62, 0.24] | small | n.s. |
| 2 to 3 vs 6 to 3 | -0.52 | 23 | = 0.783 | -0.11 [-0.53, 0.32] | negligible | n.s. |
| 3 to 3 vs 4 to 3 | 1.38 | 23 | = 0.545 | 0.30 [-0.15, 0.71] | small | n.s. |
| 3 to 3 vs 5 to 3 | -0.63 | 23 | = 0.783 | -0.16 [-0.55, 0.29] | negligible | n.s. |
| 3 to 3 vs 6 to 3 | -0.32 | 23 | = 0.867 | -0.06 [-0.49, 0.36] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -2.05 | 23 | = 0.389 | -0.54 [-0.86, 0.02] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -1.83 | 23 | = 0.399 | -0.41 [-0.81, 0.06] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.49 | 23 | = 0.783 | 0.12 [-0.32, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1467.73, BIC = 1494.46
- **2 to 3 vs 1 to 3**: *β* = -1.49, *SE* = 10.275, *z* = -0.145, *p* = 0.885
- **3 to 3 vs 1 to 3**: *β* = -12.53, *SE* = 10.386, *z* = -1.206, *p* = 0.228
- **4 to 3 vs 1 to 3**: *β* = 9.91, *SE* = 10.281, *z* = 0.964, *p* = 0.335
- **5 to 3 vs 1 to 3**: *β* = 7.37, *SE* = 10.277, *z* = 0.718, *p* = 0.473
- **6 to 3 vs 1 to 3**: *β* = 6.70, *SE* = 10.276, *z* = 0.652, *p* = 0.514
- **SNR**: *β* = 0.20, *SE* = 0.985, *z* = 0.204, *p* = 0.839

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 1.49 | 10.27 | 0.15 | 0.885 | 0.996 | n.s. |
| 1 to 3 - 3 to 3 | 12.52 | 10.39 | 1.21 | 0.228 | 0.955 | n.s. |
| 1 to 3 - 4 to 3 | -9.91 | 10.28 | -0.96 | 0.335 | 0.975 | n.s. |
| 1 to 3 - 5 to 3 | -7.37 | 10.28 | -0.72 | 0.473 | 0.980 | n.s. |
| 1 to 3 - 6 to 3 | -6.70 | 10.28 | -0.65 | 0.514 | 0.980 | n.s. |
| 2 to 3 - 3 to 3 | 11.03 | 10.38 | 1.06 | 0.288 | 0.967 | n.s. |
| 2 to 3 - 4 to 3 | -11.40 | 10.28 | -1.11 | 0.267 | 0.967 | n.s. |
| 2 to 3 - 5 to 3 | -8.87 | 10.28 | -0.86 | 0.388 | 0.980 | n.s. |
| 2 to 3 - 6 to 3 | -8.19 | 10.28 | -0.80 | 0.425 | 0.980 | n.s. |
| 3 to 3 - 4 to 3 | -22.43 | 10.34 | -2.17 | 0.030 | 0.367 | n.s. |
| 3 to 3 - 5 to 3 | -19.90 | 10.36 | -1.92 | 0.055 | 0.545 | n.s. |
| 3 to 3 - 6 to 3 | -19.23 | 10.36 | -1.86 | 0.064 | 0.574 | n.s. |
| 4 to 3 - 5 to 3 | 2.53 | 10.28 | 0.25 | 0.805 | 0.996 | n.s. |
| 4 to 3 - 6 to 3 | 3.21 | 10.28 | 0.31 | 0.755 | 0.996 | n.s. |
| 5 to 3 - 6 to 3 | 0.67 | 10.27 | 0.07 | 0.948 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.26, *p* = 0.287, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.11 | 23 | = 0.937 | 0.04 [-0.40, 0.45] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | 0.98 | 23 | = 0.674 | 0.32 [-0.23, 0.63] | small | n.s. |
| 1 to 3 vs 4 to 3 | -0.89 | 23 | = 0.674 | -0.25 [-0.61, 0.24] | small | n.s. |
| 1 to 3 vs 5 to 3 | -0.87 | 23 | = 0.674 | -0.21 [-0.60, 0.25] | small | n.s. |
| 1 to 3 vs 6 to 3 | -0.69 | 23 | = 0.674 | -0.19 [-0.57, 0.28] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 0.99 | 23 | = 0.674 | 0.26 [-0.22, 0.63] | small | n.s. |
| 2 to 3 vs 4 to 3 | -1.16 | 23 | = 0.674 | -0.27 [-0.66, 0.19] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.77 | 23 | = 0.674 | -0.24 [-0.58, 0.27] | small | n.s. |
| 2 to 3 vs 6 to 3 | -0.80 | 23 | = 0.674 | -0.21 [-0.59, 0.26] | small | n.s. |
| 3 to 3 vs 4 to 3 | -1.94 | 23 | = 0.322 | -0.55 [-0.84, 0.04] | medium | n.s. |
| 3 to 3 vs 5 to 3 | -2.11 | 23 | = 0.322 | -0.54 [-0.87, 0.01] | medium | n.s. |
| 3 to 3 vs 6 to 3 | -2.33 | 23 | = 0.322 | -0.51 [-0.92, -0.03] | medium | n.s. |
| 4 to 3 vs 5 to 3 | 0.24 | 23 | = 0.937 | 0.07 [-0.37, 0.47] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.36 | 23 | = 0.905 | 0.09 [-0.35, 0.50] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.08 | 23 | = 0.937 | 0.02 [-0.41, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 691.22, BIC = 717.95
- **2 to 3 vs 1 to 3**: *β* = -0.46, *SE* = 0.586, *z* = -0.788, *p* = 0.431
- **3 to 3 vs 1 to 3**: *β* = -1.61, *SE* = 0.594, *z* = -2.710, *p* = 0.007
- **4 to 3 vs 1 to 3**: *β* = -0.17, *SE* = 0.587, *z* = -0.292, *p* = 0.770
- **5 to 3 vs 1 to 3**: *β* = -0.44, *SE* = 0.586, *z* = -0.757, *p* = 0.449
- **6 to 3 vs 1 to 3**: *β* = 0.03, *SE* = 0.586, *z* = 0.057, *p* = 0.955
- **SNR**: *β* = 0.28, *SE* = 0.064, *z* = 4.451, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.46 | 0.59 | 0.79 | 0.431 | 0.994 | n.s. |
| 1 to 3 - 3 to 3 | 1.61 | 0.59 | 2.71 | 0.007 | 0.090 | n.s. |
| 1 to 3 - 4 to 3 | 0.17 | 0.59 | 0.29 | 0.770 | 0.997 | n.s. |
| 1 to 3 - 5 to 3 | 0.44 | 0.59 | 0.76 | 0.449 | 0.994 | n.s. |
| 1 to 3 - 6 to 3 | -0.03 | 0.59 | -0.06 | 0.955 | 0.998 | n.s. |
| 2 to 3 - 3 to 3 | 1.15 | 0.59 | 1.93 | 0.053 | 0.452 | n.s. |
| 2 to 3 - 4 to 3 | -0.29 | 0.59 | -0.50 | 0.620 | 0.997 | n.s. |
| 2 to 3 - 5 to 3 | -0.02 | 0.59 | -0.03 | 0.976 | 0.998 | n.s. |
| 2 to 3 - 6 to 3 | -0.49 | 0.59 | -0.84 | 0.399 | 0.994 | n.s. |
| 3 to 3 - 4 to 3 | -1.44 | 0.59 | -2.44 | 0.015 | 0.177 | n.s. |
| 3 to 3 - 5 to 3 | -1.17 | 0.59 | -1.97 | 0.049 | 0.452 | n.s. |
| 3 to 3 - 6 to 3 | -1.64 | 0.59 | -2.77 | 0.006 | 0.080 | n.s. |
| 4 to 3 - 5 to 3 | 0.27 | 0.59 | 0.47 | 0.642 | 0.997 | n.s. |
| 4 to 3 - 6 to 3 | -0.20 | 0.59 | -0.35 | 0.727 | 0.997 | n.s. |
| 5 to 3 - 6 to 3 | -0.48 | 0.59 | -0.81 | 0.416 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.86, *p* = 0.018, η²_G = 0.034
- Greenhouse-Geisser corrected: *p* = 0.035 (ε = 0.694)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.69 | 23 | = 0.816 | 0.11 [-0.28, 0.56] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | 2.44 | 23 | = 0.086 | 0.55 [0.05, 0.95] | medium | n.s. |
| 1 to 3 vs 4 to 3 | 0.59 | 23 | = 0.816 | 0.07 [-0.30, 0.54] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 0.70 | 23 | = 0.816 | 0.14 [-0.28, 0.57] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | 0.03 | 23 | = 0.977 | 0.00 [-0.42, 0.43] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 1.98 | 23 | = 0.180 | 0.42 [-0.04, 0.84] | small | n.s. |
| 2 to 3 vs 4 to 3 | -0.32 | 23 | = 0.866 | -0.05 [-0.49, 0.36] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | 0.05 | 23 | = 0.977 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.73 | 23 | = 0.816 | -0.11 [-0.57, 0.28] | negligible | n.s. |
| 3 to 3 vs 4 to 3 | -2.44 | 23 | = 0.086 | -0.52 [-0.95, -0.05] | medium | n.s. |
| 3 to 3 vs 5 to 3 | -2.91 | 23 | = 0.064 | -0.48 [-1.05, -0.14] | small | n.s. |
| 3 to 3 vs 6 to 3 | -2.87 | 23 | = 0.064 | -0.54 [-1.04, -0.13] | medium | n.s. |
| 4 to 3 vs 5 to 3 | 0.46 | 23 | = 0.816 | 0.07 [-0.33, 0.52] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.47 | 23 | = 0.816 | -0.07 [-0.52, 0.33] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.78 | 23 | = 0.816 | -0.13 [-0.58, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 3 showed greater amplitude than 5 to 3 (*d* = 1.03)
  - 1 to 3 showed greater amplitude than 6 to 3 (*d* = 0.73)
  - 4 to 3 showed greater amplitude than 5 to 3 (*d* = 0.92)
  - 4 to 3 showed greater amplitude than 6 to 3 (*d* = 0.58)
**N1 amplitude:** Significant main effect of condition (*p* = 0.049) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.018) (no significant pairwise comparisons)

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
