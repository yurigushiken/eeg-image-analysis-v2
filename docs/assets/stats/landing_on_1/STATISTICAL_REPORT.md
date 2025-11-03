# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:42:39

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
| 2 to 1 | 7 | 117.14 ms | 20.10 | 7.60 | [92.00, 136.00] |
| 3 to 1 | 10 | 125.20 ms | 16.98 | 5.37 | [92.00, 136.00] |
| 4 to 1 | 6 | 124.67 ms | 11.15 | 4.55 | [112.00, 136.00] |
| Cardinality1 | 8 | 121.00 ms | 16.66 | 5.89 | [92.00, 136.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 7 | 3.54 µV | 3.07 | 1.16 | [0.36, 7.97] |
| 3 to 1 | 10 | 2.98 µV | 1.21 | 0.38 | [1.19, 4.79] |
| 4 to 1 | 6 | 2.94 µV | 0.98 | 0.40 | [1.79, 4.26] |
| Cardinality1 | 8 | 3.58 µV | 1.30 | 0.46 | [2.17, 5.37] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 180.50 ms | 11.85 | 2.96 | [160.00, 204.00] |
| 3 to 1 | 22 | 181.64 ms | 13.50 | 2.88 | [160.00, 204.00] |
| 4 to 1 | 20 | 184.80 ms | 11.06 | 2.47 | [168.00, 204.00] |
| Cardinality1 | 16 | 181.75 ms | 13.70 | 3.42 | [160.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | -4.98 µV | 2.67 | 0.67 | [-10.79, -1.30] |
| 3 to 1 | 22 | -4.16 µV | 2.53 | 0.54 | [-10.41, -1.36] |
| 4 to 1 | 20 | -3.95 µV | 1.85 | 0.41 | [-8.09, -0.51] |
| Cardinality1 | 16 | -4.44 µV | 2.20 | 0.55 | [-9.64, -0.89] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 125.05 ms | 13.59 | 3.12 | [100.00, 144.00] |
| 3 to 1 | 22 | 120.00 ms | 14.02 | 2.99 | [100.00, 144.00] |
| 4 to 1 | 16 | 122.25 ms | 10.43 | 2.61 | [108.00, 144.00] |
| Cardinality1 | 18 | 123.56 ms | 12.11 | 2.85 | [100.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 4.81 µV | 2.24 | 0.51 | [2.23, 9.13] |
| 3 to 1 | 22 | 4.02 µV | 1.91 | 0.41 | [1.37, 9.14] |
| 4 to 1 | 16 | 5.65 µV | 2.75 | 0.69 | [1.45, 13.38] |
| Cardinality1 | 18 | 5.04 µV | 2.87 | 0.68 | [1.65, 13.50] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 496.20 ms | 26.80 | 5.99 | [432.00, 532.00] |
| 3 to 1 | 20 | 480.40 ms | 24.93 | 5.57 | [448.00, 532.00] |
| 4 to 1 | 21 | 486.67 ms | 30.47 | 6.65 | [432.00, 532.00] |
| Cardinality1 | 10 | 480.40 ms | 36.49 | 11.54 | [432.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 5.63 µV | 2.80 | 0.63 | [1.47, 11.08] |
| 3 to 1 | 20 | 5.75 µV | 3.05 | 0.68 | [0.90, 14.34] |
| 4 to 1 | 21 | 5.97 µV | 3.03 | 0.66 | [1.64, 12.03] |
| Cardinality1 | 10 | 3.98 µV | 1.76 | 0.56 | [1.31, 7.06] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 268.21, BIC = 278.25
- **3 to 1 vs 2 to 1**: *β* = 13.36, *SE* = 6.296, *z* = 2.122, *p* = 0.034
- **4 to 1 vs 2 to 1**: *β* = 9.14, *SE* = 6.895, *z* = 1.326, *p* = 0.185
- **Cardinality1 vs 2 to 1**: *β* = 8.27, *SE* = 6.419, *z* = 1.288, *p* = 0.198
- **SNR**: *β* = 1.53, *SE* = 2.051, *z* = 0.748, *p* = 0.455

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | -13.36 | 6.30 | -2.12 | 0.034 | 0.187 | n.s. |
| 2 to 1 - 4 to 1 | -9.14 | 6.89 | -1.33 | 0.185 | 0.640 | n.s. |
| 2 to 1 - Cardinality1 | -8.27 | 6.42 | -1.29 | 0.198 | 0.640 | n.s. |
| 3 to 1 - 4 to 1 | 4.21 | 6.47 | 0.65 | 0.515 | 0.777 | n.s. |
| 3 to 1 - Cardinality1 | 5.09 | 5.96 | 0.85 | 0.394 | 0.777 | n.s. |
| 4 to 1 - Cardinality1 | 0.87 | 6.78 | 0.13 | 0.898 | 0.898 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 116.37, BIC = 126.41
- **3 to 1 vs 2 to 1**: *β* = -0.53, *SE* = 0.569, *z* = -0.921, *p* = 0.357
- **4 to 1 vs 2 to 1**: *β* = -0.74, *SE* = 0.631, *z* = -1.181, *p* = 0.238
- **Cardinality1 vs 2 to 1**: *β* = 0.09, *SE* = 0.584, *z* = 0.147, *p* = 0.884
- **SNR**: *β* = 0.76, *SE* = 0.174, *z* = 4.353, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.52 | 0.57 | 0.92 | 0.357 | 0.743 | n.s. |
| 2 to 1 - 4 to 1 | 0.74 | 0.63 | 1.18 | 0.238 | 0.743 | n.s. |
| 2 to 1 - Cardinality1 | -0.09 | 0.58 | -0.15 | 0.884 | 0.919 | n.s. |
| 3 to 1 - 4 to 1 | 0.22 | 0.60 | 0.36 | 0.716 | 0.919 | n.s. |
| 3 to 1 - Cardinality1 | -0.61 | 0.54 | -1.13 | 0.259 | 0.743 | n.s. |
| 4 to 1 - Cardinality1 | -0.83 | 0.64 | -1.30 | 0.195 | 0.727 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 558.72, BIC = 574.84
- **3 to 1 vs 2 to 1**: *β* = 0.10, *SE* = 2.407, *z* = 0.043, *p* = 0.965
- **4 to 1 vs 2 to 1**: *β* = 4.03, *SE* = 2.431, *z* = 1.658, *p* = 0.097
- **Cardinality1 vs 2 to 1**: *β* = 1.71, *SE* = 2.596, *z* = 0.659, *p* = 0.510
- **SNR**: *β* = 0.71, *SE* = 0.315, *z* = 2.270, *p* = 0.023

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | -0.10 | 2.41 | -0.04 | 0.965 | 0.965 | n.s. |
| 2 to 1 - 4 to 1 | -4.03 | 2.43 | -1.66 | 0.097 | 0.401 | n.s. |
| 2 to 1 - Cardinality1 | -1.71 | 2.60 | -0.66 | 0.510 | 0.879 | n.s. |
| 3 to 1 - 4 to 1 | -3.92 | 2.22 | -1.76 | 0.078 | 0.385 | n.s. |
| 3 to 1 - Cardinality1 | -1.61 | 2.42 | -0.67 | 0.506 | 0.879 | n.s. |
| 4 to 1 - Cardinality1 | 2.32 | 2.43 | 0.95 | 0.341 | 0.811 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.201, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.66 | 10 | = 0.632 | 0.14 [-0.40, 0.71] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.91 | 10 | = 0.255 | -0.27 [-1.26, -0.04] | small | n.s. |
| 2 to 1 vs Cardinality1 | -1.04 | 10 | = 0.487 | -0.22 [-0.81, 0.47] | small | n.s. |
| 3 to 1 vs 4 to 1 | -2.78 | 10 | = 0.118 | -0.43 [-1.05, -0.02] | small | n.s. |
| 3 to 1 vs Cardinality1 | -1.22 | 10 | = 0.487 | -0.37 [-0.83, 0.30] | small | n.s. |
| 4 to 1 vs Cardinality1 | 0.24 | 10 | = 0.816 | 0.06 [-0.47, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.88, BIC = 314.01
- **3 to 1 vs 2 to 1**: *β* = 0.46, *SE* = 0.476, *z* = 0.962, *p* = 0.336
- **4 to 1 vs 2 to 1**: *β* = 0.94, *SE* = 0.482, *z* = 1.946, *p* = 0.052
- **Cardinality1 vs 2 to 1**: *β* = 0.83, *SE* = 0.514, *z* = 1.625, *p* = 0.104
- **SNR**: *β* = -0.40, *SE* = 0.059, *z* = -6.842, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | -0.46 | 0.48 | -0.96 | 0.336 | 0.728 | n.s. |
| 2 to 1 - 4 to 1 | -0.94 | 0.48 | -1.95 | 0.052 | 0.272 | n.s. |
| 2 to 1 - Cardinality1 | -0.83 | 0.51 | -1.62 | 0.104 | 0.423 | n.s. |
| 3 to 1 - 4 to 1 | -0.48 | 0.44 | -1.09 | 0.278 | 0.728 | n.s. |
| 3 to 1 - Cardinality1 | -0.38 | 0.48 | -0.79 | 0.432 | 0.728 | n.s. |
| 4 to 1 - Cardinality1 | 0.10 | 0.48 | 0.21 | 0.831 | 0.831 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.16, *p* = 0.342, η²_G = 0.055
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -1.13 | 10 | = 0.571 | -0.30 [-0.69, 0.42] | small | n.s. |
| 2 to 1 vs 4 to 1 | -2.08 | 10 | = 0.384 | -0.65 [-1.01, 0.15] | medium | n.s. |
| 2 to 1 vs Cardinality1 | -1.66 | 10 | = 0.384 | -0.50 [-1.22, 0.14] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -0.83 | 10 | = 0.638 | -0.28 [-0.71, 0.27] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.37 | 10 | = 0.794 | -0.16 [-0.59, 0.51] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.27 | 10 | = 0.794 | 0.11 [-0.50, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 589.68, BIC = 605.90
- **3 to 1 vs 2 to 1**: *β* = -3.26, *SE* = 2.965, *z* = -1.100, *p* = 0.271
- **4 to 1 vs 2 to 1**: *β* = -0.97, *SE* = 3.117, *z* = -0.313, *p* = 0.755
- **Cardinality1 vs 2 to 1**: *β* = -2.06, *SE* = 3.010, *z* = -0.685, *p* = 0.493
- **SNR**: *β* = 0.16, *SE* = 0.517, *z* = 0.312, *p* = 0.755

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 3.26 | 2.97 | 1.10 | 0.271 | 0.850 | n.s. |
| 2 to 1 - 4 to 1 | 0.97 | 3.12 | 0.31 | 0.755 | 0.970 | n.s. |
| 2 to 1 - Cardinality1 | 2.06 | 3.01 | 0.68 | 0.493 | 0.957 | n.s. |
| 3 to 1 - 4 to 1 | -2.29 | 3.14 | -0.73 | 0.467 | 0.957 | n.s. |
| 3 to 1 - Cardinality1 | -1.20 | 2.98 | -0.40 | 0.688 | 0.970 | n.s. |
| 4 to 1 - Cardinality1 | 1.09 | 3.22 | 0.34 | 0.736 | 0.970 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.791, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.77 | 14 | = 0.844 | 0.24 [-0.34, 0.63] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.21 | 14 | = 1.000 | 0.07 [-0.48, 0.59] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 0.73 | 14 | = 0.844 | 0.24 [-0.33, 0.67] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.67 | 14 | = 0.844 | -0.20 [-0.71, 0.37] | small | n.s. |
| 3 to 1 vs Cardinality1 | 0.00 | 14 | = 1.000 | 0.00 [-0.46, 0.54] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.59 | 14 | = 0.844 | 0.20 [-0.40, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 309.60, BIC = 325.82
- **3 to 1 vs 2 to 1**: *β* = -0.25, *SE* = 0.458, *z* = -0.550, *p* = 0.582
- **4 to 1 vs 2 to 1**: *β* = 0.72, *SE* = 0.484, *z* = 1.496, *p* = 0.135
- **Cardinality1 vs 2 to 1**: *β* = 0.45, *SE* = 0.469, *z* = 0.955, *p* = 0.340
- **SNR**: *β* = 0.39, *SE* = 0.083, *z* = 4.660, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.25 | 0.46 | 0.55 | 0.582 | 0.823 | n.s. |
| 2 to 1 - 4 to 1 | -0.72 | 0.48 | -1.50 | 0.135 | 0.493 | n.s. |
| 2 to 1 - Cardinality1 | -0.45 | 0.47 | -0.96 | 0.340 | 0.712 | n.s. |
| 3 to 1 - 4 to 1 | -0.98 | 0.49 | -2.00 | 0.046 | 0.246 | n.s. |
| 3 to 1 - Cardinality1 | -0.70 | 0.46 | -1.53 | 0.127 | 0.493 | n.s. |
| 4 to 1 - Cardinality1 | 0.28 | 0.50 | 0.55 | 0.579 | 0.823 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.70, *p* = 0.057, η²_G = 0.051
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.31 | 14 | = 0.316 | 0.34 [-0.23, 0.75] | small | n.s. |
| 2 to 1 vs 4 to 1 | -1.67 | 14 | = 0.249 | -0.35 [-0.98, 0.13] | small | n.s. |
| 2 to 1 vs Cardinality1 | -0.48 | 14 | = 0.635 | -0.09 [-0.56, 0.43] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -2.79 | 14 | = 0.086 | -0.66 [-1.25, -0.07] | medium | n.s. |
| 3 to 1 vs Cardinality1 | -1.63 | 14 | = 0.249 | -0.36 [-0.84, 0.18] | small | n.s. |
| 4 to 1 vs Cardinality1 | 0.96 | 14 | = 0.425 | 0.22 [-0.31, 0.81] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 688.70, BIC = 704.54
- **3 to 1 vs 2 to 1**: *β* = -14.75, *SE* = 9.011, *z* = -1.637, *p* = 0.102
- **4 to 1 vs 2 to 1**: *β* = -8.70, *SE* = 8.850, *z* = -0.983, *p* = 0.326
- **Cardinality1 vs 2 to 1**: *β* = -16.58, *SE* = 10.933, *z* = -1.517, *p* = 0.129
- **SNR**: *β* = -0.32, *SE* = 0.511, *z* = -0.626, *p* = 0.531

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 14.75 | 9.01 | 1.64 | 0.102 | 0.474 | n.s. |
| 2 to 1 - 4 to 1 | 8.70 | 8.85 | 0.98 | 0.326 | 0.793 | n.s. |
| 2 to 1 - Cardinality1 | 16.58 | 10.93 | 1.52 | 0.129 | 0.500 | n.s. |
| 3 to 1 - 4 to 1 | -6.05 | 8.76 | -0.69 | 0.489 | 0.857 | n.s. |
| 3 to 1 - Cardinality1 | 1.83 | 11.24 | 0.16 | 0.871 | 0.871 | n.s. |
| 4 to 1 - Cardinality1 | 7.88 | 11.08 | 0.71 | 0.477 | 0.857 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.93, *p* = 0.441, η²_G = 0.075
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 2.04 | 9 | = 0.430 | 1.04 [0.07, 1.16] | large | n.s. |
| 2 to 1 vs 4 to 1 | 0.98 | 9 | = 0.529 | 0.32 [-0.26, 0.69] | small | n.s. |
| 2 to 1 vs Cardinality1 | 1.16 | 9 | = 0.529 | 0.54 [-0.37, 1.11] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -1.05 | 9 | = 0.529 | -0.43 [-0.64, 0.33] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.24 | 9 | = 0.814 | -0.11 [-0.79, 0.64] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.43 | 9 | = 0.814 | 0.22 [-0.58, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 322.43, BIC = 338.27
- **3 to 1 vs 2 to 1**: *β* = -0.32, *SE* = 0.548, *z* = -0.574, *p* = 0.566
- **4 to 1 vs 2 to 1**: *β* = 0.08, *SE* = 0.530, *z* = 0.146, *p* = 0.884
- **Cardinality1 vs 2 to 1**: *β* = -1.73, *SE* = 0.691, *z* = -2.510, *p* = 0.012
- **SNR**: *β* = 0.15, *SE* = 0.035, *z* = 4.322, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.31 | 0.55 | 0.57 | 0.566 | 0.841 | n.s. |
| 2 to 1 - 4 to 1 | -0.08 | 0.53 | -0.15 | 0.884 | 0.884 | n.s. |
| 2 to 1 - Cardinality1 | 1.73 | 0.69 | 2.51 | 0.012 | 0.065 | n.s. |
| 3 to 1 - 4 to 1 | -0.39 | 0.53 | -0.74 | 0.458 | 0.841 | n.s. |
| 3 to 1 - Cardinality1 | 1.42 | 0.72 | 1.96 | 0.050 | 0.185 | n.s. |
| 4 to 1 - Cardinality1 | 1.81 | 0.71 | 2.54 | 0.011 | 0.065 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.50, *p* = 0.002, η²_G = 0.221
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.39 | 9 | = 0.239 | 0.42 [-0.53, 0.47] | small | n.s. |
| 2 to 1 vs 4 to 1 | -0.49 | 9 | = 0.638 | -0.13 [-0.73, 0.22] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 4.14 | 9 | = 0.012 | 1.30 [0.33, 2.29] | large | * |
| 3 to 1 vs 4 to 1 | -1.59 | 9 | = 0.219 | -0.52 [-0.58, 0.39] | medium | n.s. |
| 3 to 1 vs Cardinality1 | 2.07 | 9 | = 0.137 | 0.89 [-0.13, 1.44] | large | n.s. |
| 4 to 1 vs Cardinality1 | 3.84 | 9 | = 0.012 | 1.31 [0.27, 2.16] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.057)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than Cardinality1 (*d* = 1.30)
  - 4 to 1 showed greater amplitude than Cardinality1 (*d* = 1.31)

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
