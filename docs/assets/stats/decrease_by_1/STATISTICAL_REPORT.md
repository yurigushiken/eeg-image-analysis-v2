# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:15:59

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
| 2 to 1 | 24 | 108.00 ms | 9.44 | 1.93 | [92.00, 116.00] |
| 3 to 2 | 24 | 104.33 ms | 10.14 | 2.07 | [92.00, 116.00] |
| 4 to 3 | 24 | 104.33 ms | 8.74 | 1.78 | [92.00, 116.00] |
| 5 to 4 | 24 | 105.67 ms | 9.72 | 1.98 | [92.00, 116.00] |
| 6 to 5 | 24 | 103.00 ms | 9.00 | 1.84 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -1.96 µV | 1.91 | 0.39 | [-6.41, 2.51] |
| 3 to 2 | 24 | -1.21 µV | 2.23 | 0.46 | [-5.65, 2.93] |
| 4 to 3 | 24 | -0.82 µV | 2.13 | 0.44 | [-6.08, 3.45] |
| 5 to 4 | 24 | -1.60 µV | 2.52 | 0.51 | [-7.02, 3.36] |
| 6 to 5 | 24 | -1.54 µV | 2.26 | 0.46 | [-8.14, 1.09] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 181.83 ms | 12.76 | 2.60 | [160.00, 204.00] |
| 3 to 2 | 24 | 176.83 ms | 19.31 | 3.94 | [148.00, 204.00] |
| 4 to 3 | 24 | 175.17 ms | 16.30 | 3.33 | [148.00, 204.00] |
| 5 to 4 | 24 | 177.50 ms | 18.83 | 3.84 | [148.00, 204.00] |
| 6 to 5 | 24 | 172.83 ms | 19.35 | 3.95 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -3.38 µV | 3.29 | 0.67 | [-10.79, 2.29] |
| 3 to 2 | 24 | -5.66 µV | 2.58 | 0.53 | [-10.33, -1.35] |
| 4 to 3 | 24 | -6.05 µV | 2.68 | 0.55 | [-11.27, 1.75] |
| 5 to 4 | 24 | -5.85 µV | 2.82 | 0.58 | [-14.15, -1.72] |
| 6 to 5 | 24 | -5.89 µV | 2.12 | 0.43 | [-10.60, -2.05] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 114.67 ms | 7.88 | 1.61 | [96.00, 120.00] |
| 3 to 2 | 24 | 108.67 ms | 10.19 | 2.08 | [96.00, 120.00] |
| 4 to 3 | 24 | 107.67 ms | 9.93 | 2.03 | [96.00, 120.00] |
| 5 to 4 | 24 | 109.67 ms | 10.61 | 2.17 | [96.00, 120.00] |
| 6 to 5 | 24 | 104.67 ms | 9.19 | 1.88 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 3.37 µV | 2.55 | 0.52 | [-0.61, 9.13] |
| 3 to 2 | 24 | 0.72 µV | 2.27 | 0.46 | [-2.89, 5.61] |
| 4 to 3 | 24 | 0.82 µV | 2.20 | 0.45 | [-2.73, 5.30] |
| 5 to 4 | 24 | 1.57 µV | 2.51 | 0.51 | [-2.96, 7.17] |
| 6 to 5 | 24 | 1.21 µV | 3.02 | 0.62 | [-2.63, 9.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 500.67 ms | 35.18 | 7.18 | [436.00, 548.00] |
| 3 to 2 | 24 | 491.50 ms | 36.99 | 7.55 | [436.00, 548.00] |
| 4 to 3 | 24 | 479.83 ms | 30.52 | 6.23 | [436.00, 536.00] |
| 5 to 4 | 24 | 497.17 ms | 34.60 | 7.06 | [440.00, 548.00] |
| 6 to 5 | 24 | 499.17 ms | 39.96 | 8.16 | [436.00, 548.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 4.95 µV | 3.31 | 0.68 | [-2.33, 11.08] |
| 3 to 2 | 24 | 5.13 µV | 4.47 | 0.91 | [-1.66, 17.81] |
| 4 to 3 | 24 | 4.66 µV | 3.52 | 0.72 | [-1.86, 11.65] |
| 5 to 4 | 24 | 4.50 µV | 4.08 | 0.83 | [-3.30, 11.49] |
| 6 to 5 | 24 | 2.54 µV | 3.33 | 0.68 | [-4.88, 10.64] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 885.07, BIC = 907.37
- **3 to 2 vs 2 to 1**: *β* = -3.75, *SE* = 2.449, *z* = -1.533, *p* = 0.125
- **4 to 3 vs 2 to 1**: *β* = -3.46, *SE* = 2.455, *z* = -1.408, *p* = 0.159
- **5 to 4 vs 2 to 1**: *β* = -2.42, *SE* = 2.449, *z* = -0.990, *p* = 0.322
- **6 to 5 vs 2 to 1**: *β* = -4.84, *SE* = 2.451, *z* = -1.975, *p* = 0.048
- **SNR**: *β* = 0.64, *SE* = 0.575, *z* = 1.108, *p* = 0.268

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.75 | 2.45 | 1.53 | 0.125 | 0.700 | n.s. |
| 2 to 1 - 4 to 3 | 3.46 | 2.45 | 1.41 | 0.159 | 0.750 | n.s. |
| 2 to 1 - 5 to 4 | 2.42 | 2.45 | 0.99 | 0.322 | 0.934 | n.s. |
| 2 to 1 - 6 to 5 | 4.84 | 2.45 | 1.97 | 0.048 | 0.390 | n.s. |
| 3 to 2 - 4 to 3 | -0.30 | 2.46 | -0.12 | 0.903 | 0.986 | n.s. |
| 3 to 2 - 5 to 4 | -1.33 | 2.45 | -0.54 | 0.587 | 0.986 | n.s. |
| 3 to 2 - 6 to 5 | 1.09 | 2.46 | 0.44 | 0.658 | 0.986 | n.s. |
| 4 to 3 - 5 to 4 | -1.03 | 2.46 | -0.42 | 0.675 | 0.986 | n.s. |
| 4 to 3 - 6 to 5 | 1.39 | 2.45 | 0.57 | 0.571 | 0.986 | n.s. |
| 5 to 4 - 6 to 5 | 2.42 | 2.46 | 0.98 | 0.325 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.12, *p* = 0.354, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.11 | 23 | = 0.699 | 0.37 [-0.20, 0.65] | small | n.s. |
| 2 to 1 vs 4 to 3 | 1.29 | 23 | = 0.697 | 0.40 [-0.17, 0.69] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.82 | 23 | = 0.699 | 0.24 [-0.26, 0.59] | small | n.s. |
| 2 to 1 vs 6 to 5 | 2.05 | 23 | = 0.515 | 0.54 [-0.02, 0.86] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.54 | 23 | = 0.699 | -0.13 [-0.53, 0.31] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.49 | 23 | = 0.699 | 0.14 [-0.32, 0.52] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -0.62 | 23 | = 0.699 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.56 | 23 | = 0.699 | 0.15 [-0.31, 0.54] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 1.68 | 23 | = 0.536 | 0.28 [-0.09, 0.78] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 521.62, BIC = 543.92
- **3 to 2 vs 2 to 1**: *β* = 0.79, *SE* = 0.517, *z* = 1.525, *p* = 0.127
- **4 to 3 vs 2 to 1**: *β* = 1.05, *SE* = 0.518, *z* = 2.028, *p* = 0.043
- **5 to 4 vs 2 to 1**: *β* = 0.40, *SE* = 0.517, *z* = 0.780, *p* = 0.435
- **6 to 5 vs 2 to 1**: *β* = 0.36, *SE* = 0.517, *z* = 0.689, *p* = 0.491
- **SNR**: *β* = -0.27, *SE* = 0.126, *z* = -2.175, *p* = 0.030

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.79 | 0.52 | -1.53 | 0.127 | 0.706 | n.s. |
| 2 to 1 - 4 to 3 | -1.05 | 0.52 | -2.03 | 0.043 | 0.352 | n.s. |
| 2 to 1 - 5 to 4 | -0.40 | 0.52 | -0.78 | 0.435 | 0.956 | n.s. |
| 2 to 1 - 6 to 5 | -0.36 | 0.52 | -0.69 | 0.491 | 0.956 | n.s. |
| 3 to 2 - 4 to 3 | -0.26 | 0.52 | -0.51 | 0.613 | 0.956 | n.s. |
| 3 to 2 - 5 to 4 | 0.38 | 0.52 | 0.75 | 0.456 | 0.956 | n.s. |
| 3 to 2 - 6 to 5 | 0.43 | 0.52 | 0.83 | 0.405 | 0.956 | n.s. |
| 4 to 3 - 5 to 4 | 0.65 | 0.52 | 1.25 | 0.213 | 0.813 | n.s. |
| 4 to 3 - 6 to 5 | 0.69 | 0.52 | 1.34 | 0.179 | 0.793 | n.s. |
| 5 to 4 - 6 to 5 | 0.05 | 0.52 | 0.09 | 0.928 | 0.956 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.31, *p* = 0.271, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -1.21 | 23 | = 0.600 | -0.36 [-0.67, 0.18] | small | n.s. |
| 2 to 1 vs 4 to 3 | -2.14 | 23 | = 0.436 | -0.56 [-0.88, 0.01] | medium | n.s. |
| 2 to 1 vs 5 to 4 | -0.60 | 23 | = 0.668 | -0.16 [-0.55, 0.30] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | -0.86 | 23 | = 0.661 | -0.20 [-0.60, 0.25] | small | n.s. |
| 3 to 2 vs 4 to 3 | -0.97 | 23 | = 0.661 | -0.18 [-0.62, 0.23] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.69 | 23 | = 0.668 | 0.16 [-0.28, 0.57] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.53 | 23 | = 0.668 | 0.14 [-0.32, 0.53] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 1.56 | 23 | = 0.465 | 0.33 [-0.11, 0.75] | small | n.s. |
| 4 to 3 vs 6 to 5 | 1.53 | 23 | = 0.465 | 0.33 [-0.12, 0.74] | small | n.s. |
| 5 to 4 vs 6 to 5 | -0.13 | 23 | = 0.898 | -0.03 [-0.45, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1016.88, BIC = 1039.18
- **3 to 2 vs 2 to 1**: *β* = -3.17, *SE* = 4.159, *z* = -0.763, *p* = 0.445
- **4 to 3 vs 2 to 1**: *β* = -4.62, *SE* = 4.191, *z* = -1.102, *p* = 0.271
- **5 to 4 vs 2 to 1**: *β* = -2.22, *SE* = 4.200, *z* = -0.529, *p* = 0.597
- **6 to 5 vs 2 to 1**: *β* = -7.78, *SE* = 4.090, *z* = -1.901, *p* = 0.057
- **SNR**: *β* = -0.88, *SE* = 0.488, *z* = -1.800, *p* = 0.072

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.17 | 4.16 | 0.76 | 0.445 | 0.968 | n.s. |
| 2 to 1 - 4 to 3 | 4.62 | 4.19 | 1.10 | 0.271 | 0.906 | n.s. |
| 2 to 1 - 5 to 4 | 2.22 | 4.20 | 0.53 | 0.597 | 0.968 | n.s. |
| 2 to 1 - 6 to 5 | 7.77 | 4.09 | 1.90 | 0.057 | 0.446 | n.s. |
| 3 to 2 - 4 to 3 | 1.44 | 4.04 | 0.36 | 0.721 | 0.968 | n.s. |
| 3 to 2 - 5 to 4 | -0.95 | 4.04 | -0.24 | 0.814 | 0.968 | n.s. |
| 3 to 2 - 6 to 5 | 4.60 | 4.05 | 1.14 | 0.256 | 0.906 | n.s. |
| 4 to 3 - 5 to 4 | -2.39 | 4.03 | -0.59 | 0.553 | 0.968 | n.s. |
| 4 to 3 - 6 to 5 | 3.16 | 4.06 | 0.78 | 0.437 | 0.968 | n.s. |
| 5 to 4 - 6 to 5 | 5.55 | 4.06 | 1.37 | 0.172 | 0.817 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.279, η²_G = 0.029
- Greenhouse-Geisser corrected: *p* = 0.285 (ε = 0.685)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.50 | 23 | = 0.493 | 0.31 [-0.13, 0.74] | small | n.s. |
| 2 to 1 vs 4 to 3 | 2.40 | 23 | = 0.123 | 0.46 [0.04, 0.94] | small | n.s. |
| 2 to 1 vs 5 to 4 | 1.22 | 23 | = 0.585 | 0.27 [-0.18, 0.68] | small | n.s. |
| 2 to 1 vs 6 to 5 | 2.47 | 23 | = 0.123 | 0.55 [0.06, 0.95] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.52 | 23 | = 0.687 | 0.09 [-0.32, 0.53] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.13 | 23 | = 0.899 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.74 | 23 | = 0.687 | 0.21 [-0.27, 0.58] | small | n.s. |
| 4 to 3 vs 5 to 4 | -0.54 | 23 | = 0.687 | -0.13 [-0.53, 0.31] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.50 | 23 | = 0.687 | 0.13 [-0.32, 0.53] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 1.06 | 23 | = 0.601 | 0.24 [-0.21, 0.64] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 521.48, BIC = 543.78
- **3 to 2 vs 2 to 1**: *β* = -1.40, *SE* = 0.514, *z* = -2.718, *p* = 0.007
- **4 to 3 vs 2 to 1**: *β* = -1.68, *SE* = 0.518, *z* = -3.242, *p* = 0.001
- **5 to 4 vs 2 to 1**: *β* = -1.45, *SE* = 0.519, *z* = -2.790, *p* = 0.005
- **6 to 5 vs 2 to 1**: *β* = -1.92, *SE* = 0.505, *z* = -3.802, *p* < .001
- **SNR**: *β* = -0.42, *SE* = 0.061, *z* = -6.939, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 1.40 | 0.51 | 2.72 | 0.007 | 0.045 | * |
| 2 to 1 - 4 to 3 | 1.68 | 0.52 | 3.24 | 0.001 | 0.011 | * |
| 2 to 1 - 5 to 4 | 1.45 | 0.52 | 2.79 | 0.005 | 0.041 | * |
| 2 to 1 - 6 to 5 | 1.92 | 0.50 | 3.80 | < .001 | 0.001 | ** |
| 3 to 2 - 4 to 3 | 0.28 | 0.50 | 0.57 | 0.571 | 0.966 | n.s. |
| 3 to 2 - 5 to 4 | 0.05 | 0.50 | 0.10 | 0.917 | 0.966 | n.s. |
| 3 to 2 - 6 to 5 | 0.52 | 0.50 | 1.05 | 0.295 | 0.877 | n.s. |
| 4 to 3 - 5 to 4 | -0.23 | 0.50 | -0.46 | 0.643 | 0.966 | n.s. |
| 4 to 3 - 6 to 5 | 0.24 | 0.50 | 0.48 | 0.630 | 0.966 | n.s. |
| 5 to 4 - 6 to 5 | 0.47 | 0.50 | 0.94 | 0.347 | 0.881 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.06, *p* < .001, η²_G = 0.123
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 4.07 | 23 | = 0.002 | 0.77 [0.34, 1.32] | medium | ** |
| 2 to 1 vs 4 to 3 | 3.36 | 23 | = 0.007 | 0.89 [0.22, 1.15] | large | ** |
| 2 to 1 vs 5 to 4 | 3.73 | 23 | = 0.004 | 0.81 [0.28, 1.24] | large | ** |
| 2 to 1 vs 6 to 5 | 4.11 | 23 | = 0.002 | 0.91 [0.35, 1.33] | large | ** |
| 3 to 2 vs 4 to 3 | 0.60 | 23 | = 0.853 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.38 | 23 | = 0.853 | 0.07 [-0.35, 0.50] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.46 | 23 | = 0.853 | 0.10 [-0.33, 0.52] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -0.32 | 23 | = 0.853 | -0.07 [-0.49, 0.36] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | -0.30 | 23 | = 0.853 | -0.07 [-0.48, 0.36] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 0.10 | 23 | = 0.923 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 885.91, BIC = 908.21
- **3 to 2 vs 2 to 1**: *β* = -5.88, *SE* = 2.464, *z* = -2.385, *p* = 0.017
- **4 to 3 vs 2 to 1**: *β* = -6.91, *SE* = 2.434, *z* = -2.839, *p* = 0.005
- **5 to 4 vs 2 to 1**: *β* = -4.92, *SE* = 2.427, *z* = -2.028, *p* = 0.043
- **6 to 5 vs 2 to 1**: *β* = -9.91, *SE* = 2.434, *z* = -4.071, *p* < .001
- **SNR**: *β* = 0.11, *SE* = 0.496, *z* = 0.223, *p* = 0.823

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 5.88 | 2.46 | 2.39 | 0.017 | 0.129 | n.s. |
| 2 to 1 - 4 to 3 | 6.91 | 2.43 | 2.84 | 0.005 | 0.040 | * |
| 2 to 1 - 5 to 4 | 4.92 | 2.43 | 2.03 | 0.043 | 0.236 | n.s. |
| 2 to 1 - 6 to 5 | 9.91 | 2.43 | 4.07 | < .001 | < .001 | *** |
| 3 to 2 - 4 to 3 | 1.03 | 2.41 | 0.43 | 0.667 | 0.889 | n.s. |
| 3 to 2 - 5 to 4 | -0.96 | 2.41 | -0.40 | 0.692 | 0.889 | n.s. |
| 3 to 2 - 6 to 5 | 4.03 | 2.41 | 1.68 | 0.094 | 0.388 | n.s. |
| 4 to 3 - 5 to 4 | -1.99 | 2.40 | -0.83 | 0.407 | 0.792 | n.s. |
| 4 to 3 - 6 to 5 | 3.00 | 2.40 | 1.25 | 0.212 | 0.614 | n.s. |
| 5 to 4 - 6 to 5 | 4.99 | 2.40 | 2.08 | 0.038 | 0.236 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.42, *p* = 0.003, η²_G = 0.107
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.57 | 23 | = 0.057 | 0.66 [0.07, 0.98] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 2.85 | 23 | = 0.046 | 0.78 [0.12, 1.04] | medium | * |
| 2 to 1 vs 5 to 4 | 1.83 | 23 | = 0.159 | 0.53 [-0.06, 0.81] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 4.22 | 23 | = 0.003 | 1.17 [0.37, 1.36] | large | ** |
| 3 to 2 vs 4 to 3 | 0.39 | 23 | = 0.704 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.43 | 23 | = 0.704 | -0.10 [-0.51, 0.34] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 1.58 | 23 | = 0.214 | 0.41 [-0.11, 0.75] | small | n.s. |
| 4 to 3 vs 5 to 4 | -0.81 | 23 | = 0.530 | -0.19 [-0.59, 0.26] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.21 | 23 | = 0.341 | 0.31 [-0.18, 0.68] | small | n.s. |
| 5 to 4 vs 6 to 5 | 2.28 | 23 | = 0.081 | 0.50 [0.02, 0.91] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 537.20, BIC = 559.50
- **3 to 2 vs 2 to 1**: *β* = -2.41, *SE* = 0.544, *z* = -4.430, *p* < .001
- **4 to 3 vs 2 to 1**: *β* = -2.38, *SE* = 0.536, *z* = -4.432, *p* < .001
- **5 to 4 vs 2 to 1**: *β* = -1.65, *SE* = 0.534, *z* = -3.083, *p* = 0.002
- **6 to 5 vs 2 to 1**: *β* = -1.98, *SE* = 0.536, *z* = -3.698, *p* < .001
- **SNR**: *β* = 0.21, *SE* = 0.120, *z* = 1.776, *p* = 0.076

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 2.41 | 0.54 | 4.43 | < .001 | < .001 | *** |
| 2 to 1 - 4 to 3 | 2.38 | 0.54 | 4.43 | < .001 | < .001 | *** |
| 2 to 1 - 5 to 4 | 1.65 | 0.53 | 3.08 | 0.002 | 0.014 | * |
| 2 to 1 - 6 to 5 | 1.98 | 0.54 | 3.70 | < .001 | 0.002 | ** |
| 3 to 2 - 4 to 3 | -0.03 | 0.53 | -0.06 | 0.950 | 0.950 | n.s. |
| 3 to 2 - 5 to 4 | -0.76 | 0.53 | -1.44 | 0.150 | 0.623 | n.s. |
| 3 to 2 - 6 to 5 | -0.43 | 0.53 | -0.81 | 0.420 | 0.887 | n.s. |
| 4 to 3 - 5 to 4 | -0.73 | 0.53 | -1.38 | 0.167 | 0.623 | n.s. |
| 4 to 3 - 6 to 5 | -0.39 | 0.53 | -0.75 | 0.456 | 0.887 | n.s. |
| 5 to 4 - 6 to 5 | 0.34 | 0.53 | 0.64 | 0.524 | 0.887 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.02, *p* < .001, η²_G = 0.131
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 4.33 | 23 | = 0.001 | 1.10 [0.39, 1.38] | large | ** |
| 2 to 1 vs 4 to 3 | 4.78 | 23 | < .001 | 1.07 [0.46, 1.49] | large | *** |
| 2 to 1 vs 5 to 4 | 3.29 | 23 | = 0.008 | 0.71 [0.20, 1.14] | medium | ** |
| 2 to 1 vs 6 to 5 | 4.24 | 23 | = 0.001 | 0.77 [0.37, 1.36] | medium | ** |
| 3 to 2 vs 4 to 3 | -0.27 | 23 | = 0.791 | -0.04 [-0.48, 0.37] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -1.79 | 23 | = 0.172 | -0.35 [-0.80, 0.07] | small | n.s. |
| 3 to 2 vs 6 to 5 | -0.73 | 23 | = 0.593 | -0.18 [-0.57, 0.28] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -1.49 | 23 | = 0.251 | -0.32 [-0.74, 0.13] | small | n.s. |
| 4 to 3 vs 6 to 5 | -0.75 | 23 | = 0.593 | -0.15 [-0.58, 0.27] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 0.62 | 23 | = 0.602 | 0.13 [-0.30, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1195.35, BIC = 1217.65
- **3 to 2 vs 2 to 1**: *β* = -10.86, *SE* = 8.589, *z* = -1.265, *p* = 0.206
- **4 to 3 vs 2 to 1**: *β* = -20.64, *SE* = 8.555, *z* = -2.413, *p* = 0.016
- **5 to 4 vs 2 to 1**: *β* = -3.80, *SE* = 8.556, *z* = -0.444, *p* = 0.657
- **6 to 5 vs 2 to 1**: *β* = -3.79, *SE* = 8.616, *z* = -0.439, *p* = 0.660
- **SNR**: *β* = -2.14, *SE* = 0.962, *z* = -2.222, *p* = 0.026

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 10.86 | 8.59 | 1.26 | 0.206 | 0.801 | n.s. |
| 2 to 1 - 4 to 3 | 20.64 | 8.56 | 2.41 | 0.016 | 0.148 | n.s. |
| 2 to 1 - 5 to 4 | 3.80 | 8.56 | 0.44 | 0.657 | 0.960 | n.s. |
| 2 to 1 - 6 to 5 | 3.79 | 8.62 | 0.44 | 0.660 | 0.960 | n.s. |
| 3 to 2 - 4 to 3 | 9.78 | 8.60 | 1.14 | 0.255 | 0.830 | n.s. |
| 3 to 2 - 5 to 4 | -7.06 | 8.58 | -0.82 | 0.410 | 0.927 | n.s. |
| 3 to 2 - 6 to 5 | -7.08 | 8.56 | -0.83 | 0.408 | 0.927 | n.s. |
| 4 to 3 - 5 to 4 | -16.84 | 8.56 | -1.97 | 0.049 | 0.364 | n.s. |
| 4 to 3 - 6 to 5 | -16.86 | 8.63 | -1.95 | 0.051 | 0.364 | n.s. |
| 5 to 4 - 6 to 5 | -0.01 | 8.60 | -0.00 | 0.999 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.74, *p* = 0.147, η²_G = 0.045
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.09 | 23 | = 0.570 | 0.25 [-0.20, 0.65] | small | n.s. |
| 2 to 1 vs 4 to 3 | 3.01 | 23 | = 0.063 | 0.63 [0.15, 1.07] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 0.35 | 23 | = 0.868 | 0.10 [-0.35, 0.50] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 0.17 | 23 | = 0.868 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| 3 to 2 vs 4 to 3 | 1.72 | 23 | = 0.249 | 0.34 [-0.08, 0.79] | small | n.s. |
| 3 to 2 vs 5 to 4 | -0.60 | 23 | = 0.791 | -0.16 [-0.55, 0.30] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -0.72 | 23 | = 0.791 | -0.20 [-0.57, 0.28] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -2.09 | 23 | = 0.171 | -0.53 [-0.87, 0.02] | medium | n.s. |
| 4 to 3 vs 6 to 5 | -2.06 | 23 | = 0.171 | -0.54 [-0.86, 0.02] | medium | n.s. |
| 5 to 4 vs 6 to 5 | -0.18 | 23 | = 0.868 | -0.05 [-0.46, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 588.95, BIC = 611.25
- **3 to 2 vs 2 to 1**: *β* = 0.44, *SE* = 0.608, *z* = 0.731, *p* = 0.465
- **4 to 3 vs 2 to 1**: *β* = -0.31, *SE* = 0.606, *z* = -0.516, *p* = 0.606
- **5 to 4 vs 2 to 1**: *β* = -0.40, *SE* = 0.606, *z* = -0.658, *p* = 0.511
- **6 to 5 vs 2 to 1**: *β* = -2.05, *SE* = 0.610, *z* = -3.367, *p* = 0.001
- **SNR**: *β* = 0.33, *SE* = 0.070, *z* = 4.698, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.44 | 0.61 | -0.73 | 0.465 | 0.918 | n.s. |
| 2 to 1 - 4 to 3 | 0.31 | 0.61 | 0.52 | 0.606 | 0.918 | n.s. |
| 2 to 1 - 5 to 4 | 0.40 | 0.61 | 0.66 | 0.511 | 0.918 | n.s. |
| 2 to 1 - 6 to 5 | 2.05 | 0.61 | 3.37 | < .001 | 0.007 | ** |
| 3 to 2 - 4 to 3 | 0.76 | 0.61 | 1.24 | 0.214 | 0.699 | n.s. |
| 3 to 2 - 5 to 4 | 0.84 | 0.61 | 1.39 | 0.165 | 0.662 | n.s. |
| 3 to 2 - 6 to 5 | 2.50 | 0.61 | 4.12 | < .001 | < .001 | *** |
| 4 to 3 - 5 to 4 | 0.09 | 0.61 | 0.14 | 0.887 | 0.918 | n.s. |
| 4 to 3 - 6 to 5 | 1.74 | 0.61 | 2.85 | 0.004 | 0.034 | * |
| 5 to 4 - 6 to 5 | 1.66 | 0.61 | 2.72 | 0.007 | 0.045 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.72, *p* = 0.002, η²_G = 0.060
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.24 | 23 | = 0.815 | -0.05 [-0.47, 0.37] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 0.44 | 23 | = 0.815 | 0.08 [-0.33, 0.51] | negligible | n.s. |
| 2 to 1 vs 5 to 4 | 0.59 | 23 | = 0.800 | 0.12 [-0.30, 0.54] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 4.06 | 23 | = 0.004 | 0.73 [0.34, 1.32] | medium | ** |
| 3 to 2 vs 4 to 3 | 0.79 | 23 | = 0.733 | 0.12 [-0.26, 0.59] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.84 | 23 | = 0.733 | 0.15 [-0.25, 0.60] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 3.22 | 23 | = 0.013 | 0.66 [0.19, 1.12] | medium | * |
| 4 to 3 vs 5 to 4 | 0.26 | 23 | = 0.815 | 0.04 [-0.37, 0.48] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 2.97 | 23 | = 0.017 | 0.62 [0.15, 1.07] | medium | * |
| 5 to 4 vs 6 to 5 | 3.87 | 23 | = 0.004 | 0.53 [0.31, 1.27] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 0.77)
  - 2 to 1 showed greater amplitude than 4 to 3 (*d* = 0.89)
  - 2 to 1 showed greater amplitude than 5 to 4 (*d* = 0.81)
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 0.91)
**P1 latency:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 2 to 1 showed greater latency than 4 to 3 (*d* = 0.78)
  - 2 to 1 showed greater latency than 6 to 5 (*d* = 1.17)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 1.10)
  - 2 to 1 showed greater amplitude than 4 to 3 (*d* = 1.07)
  - 2 to 1 showed greater amplitude than 5 to 4 (*d* = 0.71)
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 0.77)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 0.73)
  - 3 to 2 showed greater amplitude than 6 to 5 (*d* = 0.66)
  - 4 to 3 showed greater amplitude than 6 to 5 (*d* = 0.62)
  - 5 to 4 showed greater amplitude than 6 to 5 (*d* = 0.53)

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
