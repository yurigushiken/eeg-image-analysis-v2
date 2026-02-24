# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:28:58

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
| 2 to 5 | 24 | 97.83 ms | 9.94 | 2.03 | [88.00, 112.00] |
| 3 to 5 | 24 | 101.83 ms | 8.98 | 1.83 | [88.00, 112.00] |
| 4 to 5 | 24 | 98.33 ms | 9.50 | 1.94 | [88.00, 112.00] |
| 6 to 5 | 24 | 101.17 ms | 9.25 | 1.89 | [88.00, 112.00] |
| Cardinality5 | 24 | 100.67 ms | 9.70 | 1.98 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | -1.05 µV | 2.27 | 0.46 | [-10.84, 1.14] |
| 3 to 5 | 24 | -1.72 µV | 2.01 | 0.41 | [-4.95, 2.58] |
| 4 to 5 | 24 | -1.90 µV | 3.25 | 0.66 | [-10.33, 4.96] |
| 6 to 5 | 24 | -1.53 µV | 2.20 | 0.45 | [-8.14, 0.91] |
| Cardinality5 | 24 | -2.02 µV | 2.23 | 0.46 | [-7.37, 0.84] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 169.67 ms | 21.39 | 4.37 | [132.00, 204.00] |
| 3 to 5 | 24 | 165.33 ms | 21.61 | 4.41 | [132.00, 204.00] |
| 4 to 5 | 24 | 167.50 ms | 20.06 | 4.10 | [132.00, 204.00] |
| 6 to 5 | 24 | 171.83 ms | 20.92 | 4.27 | [132.00, 204.00] |
| Cardinality5 | 24 | 170.83 ms | 17.71 | 3.62 | [132.00, 196.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | -6.05 µV | 2.54 | 0.52 | [-13.83, -1.66] |
| 3 to 5 | 24 | -5.27 µV | 2.69 | 0.55 | [-11.97, 0.73] |
| 4 to 5 | 24 | -5.57 µV | 2.89 | 0.59 | [-11.05, -0.28] |
| 6 to 5 | 24 | -5.93 µV | 2.12 | 0.43 | [-10.60, -2.05] |
| Cardinality5 | 24 | -6.04 µV | 2.55 | 0.52 | [-12.06, -1.67] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 95.17 ms | 10.68 | 2.18 | [84.00, 108.00] |
| 3 to 5 | 24 | 97.17 ms | 9.90 | 2.02 | [84.00, 108.00] |
| 4 to 5 | 24 | 95.33 ms | 10.33 | 2.11 | [84.00, 108.00] |
| 6 to 5 | 24 | 96.83 ms | 9.80 | 2.00 | [84.00, 108.00] |
| Cardinality5 | 24 | 98.17 ms | 10.35 | 2.11 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 1.61 µV | 2.62 | 0.53 | [-2.59, 10.47] |
| 3 to 5 | 24 | 1.64 µV | 2.41 | 0.49 | [-3.58, 5.64] |
| 4 to 5 | 24 | 1.97 µV | 3.38 | 0.69 | [-4.32, 13.41] |
| 6 to 5 | 24 | 1.38 µV | 2.86 | 0.58 | [-3.46, 9.47] |
| Cardinality5 | 24 | 1.95 µV | 1.71 | 0.35 | [-1.12, 5.37] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 446.50 ms | 50.73 | 10.36 | [368.00, 536.00] |
| 3 to 5 | 24 | 457.33 ms | 64.33 | 13.13 | [360.00, 540.00] |
| 4 to 5 | 24 | 464.83 ms | 62.00 | 12.66 | [356.00, 540.00] |
| 6 to 5 | 24 | 463.50 ms | 72.50 | 14.80 | [352.00, 540.00] |
| Cardinality5 | 24 | 444.33 ms | 62.85 | 12.83 | [352.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 5.26 µV | 2.83 | 0.58 | [0.82, 11.71] |
| 3 to 5 | 24 | 4.77 µV | 3.78 | 0.77 | [-2.99, 15.40] |
| 4 to 5 | 24 | 4.37 µV | 4.20 | 0.86 | [-3.06, 16.10] |
| 6 to 5 | 24 | 2.93 µV | 2.86 | 0.58 | [-1.98, 10.64] |
| Cardinality5 | 24 | 2.45 µV | 2.59 | 0.53 | [-5.03, 6.16] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 882.06, BIC = 904.36
- **3 to 5 vs 2 to 5**: *β* = 3.80, *SE* = 2.403, *z* = 1.583, *p* = 0.113
- **4 to 5 vs 2 to 5**: *β* = 0.12, *SE* = 2.419, *z* = 0.051, *p* = 0.959
- **6 to 5 vs 2 to 5**: *β* = 3.30, *SE* = 2.397, *z* = 1.376, *p* = 0.169
- **Cardinality5 vs 2 to 5**: *β* = 2.59, *SE* = 2.406, *z* = 1.078, *p* = 0.281
- **SNR**: *β* = 0.40, *SE* = 0.347, *z* = 1.144, *p* = 0.253

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -3.80 | 2.40 | -1.58 | 0.113 | 0.700 | n.s. |
| 2 to 5 - 4 to 5 | -0.12 | 2.42 | -0.05 | 0.959 | 0.988 | n.s. |
| 2 to 5 - 6 to 5 | -3.30 | 2.40 | -1.38 | 0.169 | 0.772 | n.s. |
| 2 to 5 - Cardinality5 | -2.59 | 2.41 | -1.08 | 0.281 | 0.862 | n.s. |
| 3 to 5 - 4 to 5 | 3.68 | 2.40 | 1.53 | 0.125 | 0.701 | n.s. |
| 3 to 5 - 6 to 5 | 0.51 | 2.40 | 0.21 | 0.833 | 0.988 | n.s. |
| 3 to 5 - Cardinality5 | 1.21 | 2.40 | 0.50 | 0.614 | 0.978 | n.s. |
| 4 to 5 - 6 to 5 | -3.17 | 2.42 | -1.31 | 0.189 | 0.772 | n.s. |
| 4 to 5 - Cardinality5 | -2.47 | 2.40 | -1.03 | 0.303 | 0.862 | n.s. |
| 6 to 5 - Cardinality5 | 0.70 | 2.40 | 0.29 | 0.770 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.378, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.76 | 23 | = 0.550 | -0.42 [-0.80, 0.08] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.23 | 23 | = 0.838 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -1.24 | 23 | = 0.550 | -0.35 [-0.68, 0.17] | small | n.s. |
| 2 to 5 vs Cardinality5 | -1.00 | 23 | = 0.550 | -0.29 [-0.63, 0.22] | small | n.s. |
| 3 to 5 vs 4 to 5 | 1.44 | 23 | = 0.550 | 0.38 [-0.14, 0.72] | small | n.s. |
| 3 to 5 vs 6 to 5 | 0.32 | 23 | = 0.838 | 0.07 [-0.36, 0.49] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | 0.49 | 23 | = 0.838 | 0.12 [-0.32, 0.52] | negligible | n.s. |
| 4 to 5 vs 6 to 5 | -1.09 | 23 | = 0.550 | -0.30 [-0.65, 0.21] | small | n.s. |
| 4 to 5 vs Cardinality5 | -0.99 | 23 | = 0.550 | -0.24 [-0.63, 0.22] | small | n.s. |
| 6 to 5 vs Cardinality5 | 0.21 | 23 | = 0.838 | 0.05 [-0.38, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 513.76, BIC = 536.06
- **3 to 5 vs 2 to 5**: *β* = -0.47, *SE* = 0.505, *z* = -0.931, *p* = 0.352
- **4 to 5 vs 2 to 5**: *β* = -0.47, *SE* = 0.509, *z* = -0.913, *p* = 0.361
- **6 to 5 vs 2 to 5**: *β* = -0.45, *SE* = 0.504, *z* = -0.895, *p* = 0.371
- **Cardinality5 vs 2 to 5**: *β* = -0.72, *SE* = 0.506, *z* = -1.424, *p* = 0.155
- **SNR**: *β* = -0.42, *SE* = 0.075, *z* = -5.522, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.47 | 0.51 | 0.93 | 0.352 | 0.980 | n.s. |
| 2 to 5 - 4 to 5 | 0.46 | 0.51 | 0.91 | 0.361 | 0.980 | n.s. |
| 2 to 5 - 6 to 5 | 0.45 | 0.50 | 0.90 | 0.371 | 0.980 | n.s. |
| 2 to 5 - Cardinality5 | 0.72 | 0.51 | 1.42 | 0.155 | 0.813 | n.s. |
| 3 to 5 - 4 to 5 | -0.01 | 0.50 | -0.01 | 0.991 | 1.000 | n.s. |
| 3 to 5 - 6 to 5 | -0.02 | 0.50 | -0.04 | 0.969 | 1.000 | n.s. |
| 3 to 5 - Cardinality5 | 0.25 | 0.50 | 0.50 | 0.620 | 0.996 | n.s. |
| 4 to 5 - 6 to 5 | -0.01 | 0.51 | -0.03 | 0.978 | 1.000 | n.s. |
| 4 to 5 - Cardinality5 | 0.26 | 0.50 | 0.51 | 0.613 | 0.996 | n.s. |
| 6 to 5 - Cardinality5 | 0.27 | 0.51 | 0.53 | 0.594 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.94, *p* = 0.443, η²_G = 0.020
- Greenhouse-Geisser corrected: *p* = 0.410 (ε = 0.599)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.34 | 23 | = 0.482 | 0.31 [-0.16, 0.70] | small | n.s. |
| 2 to 5 vs 4 to 5 | 1.52 | 23 | = 0.482 | 0.31 [-0.12, 0.74] | small | n.s. |
| 2 to 5 vs 6 to 5 | 1.40 | 23 | = 0.482 | 0.22 [-0.15, 0.72] | small | n.s. |
| 2 to 5 vs Cardinality5 | 1.99 | 23 | = 0.482 | 0.43 [-0.03, 0.85] | small | n.s. |
| 3 to 5 vs 4 to 5 | 0.25 | 23 | = 0.888 | 0.07 [-0.37, 0.47] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -0.44 | 23 | = 0.833 | -0.09 [-0.51, 0.33] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | 0.78 | 23 | = 0.744 | 0.14 [-0.27, 0.58] | negligible | n.s. |
| 4 to 5 vs 6 to 5 | -0.54 | 23 | = 0.833 | -0.13 [-0.53, 0.31] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 0.14 | 23 | = 0.888 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 1.01 | 23 | = 0.647 | 0.22 [-0.22, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1026.73, BIC = 1049.03
- **3 to 5 vs 2 to 5**: *β* = -4.57, *SE* = 3.916, *z* = -1.167, *p* = 0.243
- **4 to 5 vs 2 to 5**: *β* = -2.14, *SE* = 3.901, *z* = -0.549, *p* = 0.583
- **6 to 5 vs 2 to 5**: *β* = 2.11, *SE* = 3.902, *z* = 0.540, *p* = 0.589
- **Cardinality5 vs 2 to 5**: *β* = 1.28, *SE* = 3.905, *z* = 0.329, *p* = 0.742
- **SNR**: *β* = -0.45, *SE* = 0.642, *z* = -0.701, *p* = 0.483

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 4.57 | 3.92 | 1.17 | 0.243 | 0.893 | n.s. |
| 2 to 5 - 4 to 5 | 2.14 | 3.90 | 0.55 | 0.583 | 0.979 | n.s. |
| 2 to 5 - 6 to 5 | -2.11 | 3.90 | -0.54 | 0.589 | 0.979 | n.s. |
| 2 to 5 - Cardinality5 | -1.28 | 3.90 | -0.33 | 0.742 | 0.979 | n.s. |
| 3 to 5 - 4 to 5 | -2.42 | 3.92 | -0.62 | 0.536 | 0.979 | n.s. |
| 3 to 5 - 6 to 5 | -6.68 | 3.91 | -1.71 | 0.088 | 0.601 | n.s. |
| 3 to 5 - Cardinality5 | -5.85 | 3.93 | -1.49 | 0.137 | 0.734 | n.s. |
| 4 to 5 - 6 to 5 | -4.25 | 3.90 | -1.09 | 0.276 | 0.896 | n.s. |
| 4 to 5 - Cardinality5 | -3.43 | 3.90 | -0.88 | 0.380 | 0.943 | n.s. |
| 6 to 5 - Cardinality5 | 0.82 | 3.91 | 0.21 | 0.833 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.87, *p* = 0.483, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.04 | 23 | = 0.733 | 0.20 [-0.21, 0.64] | small | n.s. |
| 2 to 5 vs 4 to 5 | 0.79 | 23 | = 0.733 | 0.10 [-0.26, 0.59] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.53 | 23 | = 0.779 | -0.10 [-0.53, 0.32] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.32 | 23 | = 0.823 | -0.06 [-0.49, 0.36] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.50 | 23 | = 0.779 | -0.10 [-0.52, 0.32] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.41 | 23 | = 0.733 | -0.31 [-0.72, 0.14] | small | n.s. |
| 3 to 5 vs Cardinality5 | -1.94 | 23 | = 0.649 | -0.28 [-0.83, 0.04] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.98 | 23 | = 0.733 | -0.21 [-0.63, 0.23] | small | n.s. |
| 4 to 5 vs Cardinality5 | -0.85 | 23 | = 0.733 | -0.18 [-0.60, 0.25] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 0.23 | 23 | = 0.823 | 0.05 [-0.38, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 486.73, BIC = 509.03
- **3 to 5 vs 2 to 5**: *β* = 0.57, *SE* = 0.413, *z* = 1.390, *p* = 0.165
- **4 to 5 vs 2 to 5**: *β* = 0.50, *SE* = 0.411, *z* = 1.210, *p* = 0.226
- **6 to 5 vs 2 to 5**: *β* = 0.07, *SE* = 0.411, *z* = 0.163, *p* = 0.870
- **Cardinality5 vs 2 to 5**: *β* = 0.10, *SE* = 0.412, *z* = 0.248, *p* = 0.804
- **SNR**: *β* = -0.38, *SE* = 0.068, *z* = -5.634, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.57 | 0.41 | -1.39 | 0.165 | 0.834 | n.s. |
| 2 to 5 - 4 to 5 | -0.50 | 0.41 | -1.21 | 0.226 | 0.892 | n.s. |
| 2 to 5 - 6 to 5 | -0.07 | 0.41 | -0.16 | 0.870 | 0.999 | n.s. |
| 2 to 5 - Cardinality5 | -0.10 | 0.41 | -0.25 | 0.804 | 0.999 | n.s. |
| 3 to 5 - 4 to 5 | 0.08 | 0.41 | 0.18 | 0.854 | 0.999 | n.s. |
| 3 to 5 - 6 to 5 | 0.51 | 0.41 | 1.23 | 0.219 | 0.892 | n.s. |
| 3 to 5 - Cardinality5 | 0.47 | 0.41 | 1.14 | 0.255 | 0.892 | n.s. |
| 4 to 5 - 6 to 5 | 0.43 | 0.41 | 1.05 | 0.295 | 0.892 | n.s. |
| 4 to 5 - Cardinality5 | 0.40 | 0.41 | 0.96 | 0.336 | 0.892 | n.s. |
| 6 to 5 - Cardinality5 | -0.03 | 0.41 | -0.08 | 0.933 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.362, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.77 | 23 | = 0.346 | -0.30 [-0.80, 0.08] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.81 | 23 | = 0.731 | -0.18 [-0.59, 0.26] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.26 | 23 | = 0.882 | -0.05 [-0.48, 0.37] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.00 | 23 | = 0.997 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 0.79 | 23 | = 0.731 | 0.11 [-0.26, 0.59] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 1.69 | 23 | = 0.346 | 0.27 [-0.09, 0.78] | small | n.s. |
| 3 to 5 vs Cardinality5 | 2.06 | 23 | = 0.346 | 0.29 [-0.02, 0.86] | small | n.s. |
| 4 to 5 vs 6 to 5 | 0.65 | 23 | = 0.747 | 0.14 [-0.29, 0.56] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 0.97 | 23 | = 0.731 | 0.17 [-0.23, 0.62] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 0.30 | 23 | = 0.882 | 0.05 [-0.36, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 887.59, BIC = 909.89
- **3 to 5 vs 2 to 5**: *β* = 1.78, *SE* = 2.335, *z* = 0.763, *p* = 0.446
- **4 to 5 vs 2 to 5**: *β* = -0.03, *SE* = 2.333, *z* = -0.014, *p* = 0.989
- **6 to 5 vs 2 to 5**: *β* = 1.52, *SE* = 2.328, *z* = 0.653, *p* = 0.513
- **Cardinality5 vs 2 to 5**: *β* = 2.98, *SE* = 2.322, *z* = 1.282, *p* = 0.200
- **SNR**: *β* = 0.47, *SE* = 0.527, *z* = 0.892, *p* = 0.372

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -1.78 | 2.34 | -0.76 | 0.446 | 0.990 | n.s. |
| 2 to 5 - 4 to 5 | 0.03 | 2.33 | 0.01 | 0.989 | 0.992 | n.s. |
| 2 to 5 - 6 to 5 | -1.52 | 2.33 | -0.65 | 0.513 | 0.990 | n.s. |
| 2 to 5 - Cardinality5 | -2.98 | 2.32 | -1.28 | 0.200 | 0.888 | n.s. |
| 3 to 5 - 4 to 5 | 1.81 | 2.32 | 0.78 | 0.435 | 0.990 | n.s. |
| 3 to 5 - 6 to 5 | 0.26 | 2.32 | 0.11 | 0.911 | 0.992 | n.s. |
| 3 to 5 - Cardinality5 | -1.20 | 2.33 | -0.51 | 0.608 | 0.990 | n.s. |
| 4 to 5 - 6 to 5 | -1.55 | 2.32 | -0.67 | 0.503 | 0.990 | n.s. |
| 4 to 5 - Cardinality5 | -3.01 | 2.33 | -1.29 | 0.197 | 0.888 | n.s. |
| 6 to 5 - Cardinality5 | -1.46 | 2.33 | -0.63 | 0.532 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.58, *p* = 0.681, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.04 | 23 | = 0.784 | -0.19 [-0.64, 0.22] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -0.07 | 23 | = 0.946 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.70 | 23 | = 0.784 | -0.16 [-0.57, 0.28] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -1.50 | 23 | = 0.784 | -0.29 [-0.74, 0.13] | small | n.s. |
| 3 to 5 vs 4 to 5 | 0.68 | 23 | = 0.784 | 0.18 [-0.29, 0.56] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 0.14 | 23 | = 0.946 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | -0.52 | 23 | = 0.784 | -0.10 [-0.53, 0.32] | negligible | n.s. |
| 4 to 5 vs 6 to 5 | -0.49 | 23 | = 0.784 | -0.15 [-0.52, 0.32] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | -1.33 | 23 | = 0.784 | -0.27 [-0.70, 0.16] | small | n.s. |
| 6 to 5 vs Cardinality5 | -0.53 | 23 | = 0.784 | -0.13 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 551.43, BIC = 573.73
- **3 to 5 vs 2 to 5**: *β* = -0.18, *SE* = 0.574, *z* = -0.306, *p* = 0.760
- **4 to 5 vs 2 to 5**: *β* = 0.17, *SE* = 0.574, *z* = 0.298, *p* = 0.766
- **6 to 5 vs 2 to 5**: *β* = -0.37, *SE* = 0.573, *z* = -0.650, *p* = 0.516
- **Cardinality5 vs 2 to 5**: *β* = 0.32, *SE* = 0.571, *z* = 0.553, *p* = 0.581
- **SNR**: *β* = 0.43, *SE* = 0.129, *z* = 3.368, *p* = 0.001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.18 | 0.57 | 0.31 | 0.760 | 0.995 | n.s. |
| 2 to 5 - 4 to 5 | -0.17 | 0.57 | -0.30 | 0.766 | 0.995 | n.s. |
| 2 to 5 - 6 to 5 | 0.37 | 0.57 | 0.65 | 0.516 | 0.994 | n.s. |
| 2 to 5 - Cardinality5 | -0.32 | 0.57 | -0.55 | 0.581 | 0.994 | n.s. |
| 3 to 5 - 4 to 5 | -0.35 | 0.57 | -0.61 | 0.544 | 0.994 | n.s. |
| 3 to 5 - 6 to 5 | 0.20 | 0.57 | 0.34 | 0.731 | 0.995 | n.s. |
| 3 to 5 - Cardinality5 | -0.49 | 0.57 | -0.86 | 0.392 | 0.981 | n.s. |
| 4 to 5 - 6 to 5 | 0.54 | 0.57 | 0.95 | 0.342 | 0.977 | n.s. |
| 4 to 5 - Cardinality5 | -0.14 | 0.57 | -0.25 | 0.800 | 0.995 | n.s. |
| 6 to 5 - Cardinality5 | -0.69 | 0.57 | -1.20 | 0.229 | 0.926 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.34, *p* = 0.848, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.744 (ε = 0.583)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.06 | 23 | = 0.980 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -0.48 | 23 | = 0.845 | -0.12 [-0.52, 0.33] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 0.71 | 23 | = 0.845 | 0.09 [-0.28, 0.57] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.75 | 23 | = 0.845 | -0.15 [-0.58, 0.27] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.42 | 23 | = 0.845 | -0.11 [-0.51, 0.34] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 0.44 | 23 | = 0.845 | 0.10 [-0.33, 0.51] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | -0.94 | 23 | = 0.845 | -0.15 [-0.62, 0.23] | negligible | n.s. |
| 4 to 5 vs 6 to 5 | 0.71 | 23 | = 0.845 | 0.19 [-0.28, 0.57] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 0.03 | 23 | = 0.980 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | -1.11 | 23 | = 0.845 | -0.24 [-0.65, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1337.98, BIC = 1360.28
- **3 to 5 vs 2 to 5**: *β* = 10.80, *SE* = 15.907, *z* = 0.679, *p* = 0.497
- **4 to 5 vs 2 to 5**: *β* = 17.76, *SE* = 16.019, *z* = 1.109, *p* = 0.268
- **6 to 5 vs 2 to 5**: *β* = 16.43, *SE* = 16.020, *z* = 1.025, *p* = 0.305
- **Cardinality5 vs 2 to 5**: *β* = -2.77, *SE* = 16.034, *z* = -0.173, *p* = 0.863
- **SNR**: *β* = -0.60, *SE* = 1.992, *z* = -0.301, *p* = 0.763

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -10.80 | 15.91 | -0.68 | 0.497 | 0.968 | n.s. |
| 2 to 5 - 4 to 5 | -17.76 | 16.02 | -1.11 | 0.268 | 0.917 | n.s. |
| 2 to 5 - 6 to 5 | -16.43 | 16.02 | -1.03 | 0.305 | 0.922 | n.s. |
| 2 to 5 - Cardinality5 | 2.77 | 16.03 | 0.17 | 0.863 | 0.987 | n.s. |
| 3 to 5 - 4 to 5 | -6.96 | 16.01 | -0.44 | 0.663 | 0.987 | n.s. |
| 3 to 5 - 6 to 5 | -5.63 | 16.01 | -0.35 | 0.725 | 0.987 | n.s. |
| 3 to 5 - Cardinality5 | 13.57 | 16.02 | 0.85 | 0.397 | 0.952 | n.s. |
| 4 to 5 - 6 to 5 | 1.34 | 15.91 | 0.08 | 0.933 | 0.987 | n.s. |
| 4 to 5 - Cardinality5 | 20.54 | 15.91 | 1.29 | 0.197 | 0.888 | n.s. |
| 6 to 5 - Cardinality5 | 19.20 | 15.91 | 1.21 | 0.227 | 0.902 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.606, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.87 | 23 | = 0.783 | -0.19 [-0.60, 0.25] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -1.22 | 23 | = 0.783 | -0.32 [-0.68, 0.18] | small | n.s. |
| 2 to 5 vs 6 to 5 | -0.99 | 23 | = 0.783 | -0.27 [-0.63, 0.22] | small | n.s. |
| 2 to 5 vs Cardinality5 | 0.15 | 23 | = 0.941 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.51 | 23 | = 0.874 | -0.12 [-0.53, 0.32] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -0.36 | 23 | = 0.906 | -0.09 [-0.50, 0.35] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | 0.73 | 23 | = 0.783 | 0.20 [-0.27, 0.57] | small | n.s. |
| 4 to 5 vs 6 to 5 | 0.08 | 23 | = 0.941 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 1.09 | 23 | = 0.783 | 0.33 [-0.20, 0.65] | small | n.s. |
| 6 to 5 vs Cardinality5 | 1.19 | 23 | = 0.783 | 0.28 [-0.19, 0.67] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 582.63, BIC = 604.93
- **3 to 5 vs 2 to 5**: *β* = -0.47, *SE* = 0.612, *z* = -0.763, *p* = 0.446
- **4 to 5 vs 2 to 5**: *β* = -0.62, *SE* = 0.617, *z* = -1.002, *p* = 0.317
- **6 to 5 vs 2 to 5**: *β* = -2.06, *SE* = 0.617, *z* = -3.341, *p* = 0.001
- **Cardinality5 vs 2 to 5**: *β* = -2.52, *SE* = 0.618, *z* = -4.079, *p* < .001
- **SNR**: *β* = 0.28, *SE* = 0.081, *z* = 3.489, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.47 | 0.61 | 0.76 | 0.446 | 0.830 | n.s. |
| 2 to 5 - 4 to 5 | 0.62 | 0.62 | 1.00 | 0.317 | 0.782 | n.s. |
| 2 to 5 - 6 to 5 | 2.06 | 0.62 | 3.34 | < .001 | 0.008 | ** |
| 2 to 5 - Cardinality5 | 2.52 | 0.62 | 4.08 | < .001 | < .001 | *** |
| 3 to 5 - 4 to 5 | 0.15 | 0.62 | 0.24 | 0.807 | 0.830 | n.s. |
| 3 to 5 - 6 to 5 | 1.59 | 0.62 | 2.59 | 0.010 | 0.057 | n.s. |
| 3 to 5 - Cardinality5 | 2.05 | 0.62 | 3.33 | < .001 | 0.008 | ** |
| 4 to 5 - 6 to 5 | 1.44 | 0.61 | 2.36 | 0.018 | 0.089 | n.s. |
| 4 to 5 - Cardinality5 | 1.90 | 0.61 | 3.11 | 0.002 | 0.013 | * |
| 6 to 5 - Cardinality5 | 0.46 | 0.61 | 0.75 | 0.454 | 0.830 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.76, *p* < .001, η²_G = 0.100
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.73 | 23 | = 0.515 | 0.14 [-0.28, 0.57] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 1.23 | 23 | = 0.330 | 0.25 [-0.18, 0.68] | small | n.s. |
| 2 to 5 vs 6 to 5 | 3.54 | 23 | = 0.005 | 0.82 [0.25, 1.20] | large | ** |
| 2 to 5 vs Cardinality5 | 5.21 | 23 | < .001 | 1.03 [0.54, 1.59] | large | *** |
| 3 to 5 vs 4 to 5 | 0.66 | 23 | = 0.515 | 0.10 [-0.29, 0.56] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 3.53 | 23 | = 0.005 | 0.55 [0.25, 1.19] | medium | ** |
| 3 to 5 vs Cardinality5 | 3.46 | 23 | = 0.005 | 0.72 [0.23, 1.18] | medium | ** |
| 4 to 5 vs 6 to 5 | 1.96 | 23 | = 0.104 | 0.40 [-0.04, 0.84] | small | n.s. |
| 4 to 5 vs Cardinality5 | 2.36 | 23 | = 0.055 | 0.55 [0.03, 0.93] | medium | n.s. |
| 6 to 5 vs Cardinality5 | 0.81 | 23 | = 0.515 | 0.17 [-0.26, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 5 showed greater amplitude than 6 to 5 (*d* = 0.82)
  - 2 to 5 showed greater amplitude than Cardinality5 (*d* = 1.03)
  - 3 to 5 showed greater amplitude than 6 to 5 (*d* = 0.55)
  - 3 to 5 showed greater amplitude than Cardinality5 (*d* = 0.72)

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
