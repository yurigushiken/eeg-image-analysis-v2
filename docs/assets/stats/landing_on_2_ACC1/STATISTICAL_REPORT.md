# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:27:45

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
| 1 to 2 | 24 | 103.33 ms | 10.79 | 2.20 | [92.00, 116.00] |
| 2 to 2 | 24 | 107.67 ms | 9.05 | 1.85 | [92.00, 116.00] |
| 3 to 2 | 24 | 104.67 ms | 10.40 | 2.12 | [92.00, 116.00] |
| 4 to 2 | 24 | 106.83 ms | 9.25 | 1.89 | [92.00, 116.00] |
| 5 to 2 | 24 | 102.83 ms | 9.62 | 1.96 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -0.19 µV | 2.18 | 0.44 | [-3.35, 5.38] |
| 2 to 2 | 24 | -1.01 µV | 2.07 | 0.42 | [-5.94, 3.96] |
| 3 to 2 | 24 | -1.40 µV | 2.20 | 0.45 | [-5.62, 2.93] |
| 4 to 2 | 24 | -0.82 µV | 2.70 | 0.55 | [-4.94, 5.89] |
| 5 to 2 | 24 | -2.23 µV | 2.52 | 0.51 | [-6.65, 2.53] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 172.33 ms | 19.09 | 3.90 | [144.00, 208.00] |
| 2 to 2 | 24 | 175.00 ms | 21.01 | 4.29 | [144.00, 212.00] |
| 3 to 2 | 24 | 176.17 ms | 24.13 | 4.93 | [144.00, 212.00] |
| 4 to 2 | 24 | 178.50 ms | 15.33 | 3.13 | [148.00, 212.00] |
| 5 to 2 | 24 | 174.17 ms | 18.35 | 3.75 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -5.53 µV | 2.35 | 0.48 | [-10.03, -0.26] |
| 2 to 2 | 24 | -5.33 µV | 2.75 | 0.56 | [-10.50, -0.87] |
| 3 to 2 | 24 | -5.94 µV | 2.56 | 0.52 | [-10.33, -1.67] |
| 4 to 2 | 24 | -6.17 µV | 3.05 | 0.62 | [-12.20, -2.20] |
| 5 to 2 | 24 | -6.98 µV | 2.97 | 0.61 | [-11.17, -1.41] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 111.33 ms | 7.43 | 1.52 | [104.00, 120.00] |
| 2 to 2 | 24 | 112.50 ms | 6.91 | 1.41 | [104.00, 120.00] |
| 3 to 2 | 24 | 112.83 ms | 7.27 | 1.48 | [104.00, 120.00] |
| 4 to 2 | 24 | 113.50 ms | 6.65 | 1.36 | [104.00, 120.00] |
| 5 to 2 | 24 | 111.33 ms | 7.04 | 1.44 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 0.15 µV | 2.06 | 0.42 | [-4.56, 3.14] |
| 2 to 2 | 24 | 0.86 µV | 3.07 | 0.63 | [-7.98, 7.57] |
| 3 to 2 | 24 | 0.51 µV | 2.31 | 0.47 | [-2.89, 6.10] |
| 4 to 2 | 24 | 0.78 µV | 2.88 | 0.59 | [-5.85, 4.59] |
| 5 to 2 | 24 | 1.53 µV | 2.69 | 0.55 | [-3.90, 6.20] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 477.83 ms | 42.72 | 8.72 | [420.00, 540.00] |
| 2 to 2 | 24 | 465.67 ms | 31.03 | 6.33 | [420.00, 536.00] |
| 3 to 2 | 24 | 488.50 ms | 34.35 | 7.01 | [432.00, 540.00] |
| 4 to 2 | 24 | 477.50 ms | 38.85 | 7.93 | [420.00, 540.00] |
| 5 to 2 | 24 | 477.33 ms | 39.52 | 8.07 | [420.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 4.11 µV | 3.82 | 0.78 | [-3.51, 11.52] |
| 2 to 2 | 24 | 2.04 µV | 3.44 | 0.70 | [-5.35, 10.57] |
| 3 to 2 | 24 | 5.31 µV | 4.41 | 0.90 | [-1.20, 17.81] |
| 4 to 2 | 24 | 4.47 µV | 4.24 | 0.87 | [-3.50, 14.41] |
| 5 to 2 | 24 | 4.38 µV | 3.63 | 0.74 | [-2.27, 13.53] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 898.78, BIC = 921.08
- **2 to 2 vs 1 to 2**: *β* = 4.50, *SE* = 2.695, *z* = 1.670, *p* = 0.095
- **3 to 2 vs 1 to 2**: *β* = 1.16, *SE* = 2.696, *z* = 0.431, *p* = 0.667
- **4 to 2 vs 1 to 2**: *β* = 3.44, *SE* = 2.689, *z* = 1.279, *p* = 0.201
- **5 to 2 vs 1 to 2**: *β* = -0.83, *SE* = 2.716, *z* = -0.307, *p* = 0.759
- **SNR**: *β* = 0.58, *SE* = 0.669, *z* = 0.870, *p* = 0.385

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | -4.50 | 2.70 | -1.67 | 0.095 | 0.592 | n.s. |
| 1 to 2 - 3 to 2 | -1.16 | 2.70 | -0.43 | 0.667 | 0.963 | n.s. |
| 1 to 2 - 4 to 2 | -3.44 | 2.69 | -1.28 | 0.201 | 0.792 | n.s. |
| 1 to 2 - 5 to 2 | 0.83 | 2.72 | 0.31 | 0.759 | 0.963 | n.s. |
| 2 to 2 - 3 to 2 | 3.34 | 2.72 | 1.23 | 0.219 | 0.792 | n.s. |
| 2 to 2 - 4 to 2 | 1.06 | 2.70 | 0.39 | 0.695 | 0.963 | n.s. |
| 2 to 2 - 5 to 2 | 5.34 | 2.75 | 1.94 | 0.052 | 0.416 | n.s. |
| 3 to 2 - 4 to 2 | -2.28 | 2.69 | -0.85 | 0.397 | 0.920 | n.s. |
| 3 to 2 - 5 to 2 | 2.00 | 2.69 | 0.74 | 0.459 | 0.920 | n.s. |
| 4 to 2 - 5 to 2 | 4.27 | 2.71 | 1.58 | 0.114 | 0.621 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.19, *p* = 0.322, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -1.47 | 23 | = 0.517 | -0.44 [-0.73, 0.13] | small | n.s. |
| 1 to 2 vs 3 to 2 | -0.50 | 23 | = 0.774 | -0.13 [-0.53, 0.32] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -1.30 | 23 | = 0.517 | -0.35 [-0.69, 0.16] | small | n.s. |
| 1 to 2 vs 5 to 2 | 0.17 | 23 | = 0.866 | 0.05 [-0.39, 0.46] | negligible | n.s. |
| 2 to 2 vs 3 to 2 | 1.16 | 23 | = 0.519 | 0.31 [-0.19, 0.66] | small | n.s. |
| 2 to 2 vs 4 to 2 | 0.31 | 23 | = 0.846 | 0.09 [-0.36, 0.49] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 1.86 | 23 | = 0.415 | 0.52 [-0.06, 0.82] | medium | n.s. |
| 3 to 2 vs 4 to 2 | -0.71 | 23 | = 0.774 | -0.22 [-0.57, 0.28] | small | n.s. |
| 3 to 2 vs 5 to 2 | 0.59 | 23 | = 0.774 | 0.18 [-0.30, 0.54] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.81 | 23 | = 0.415 | 0.42 [-0.07, 0.81] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 546.50, BIC = 568.80
- **2 to 2 vs 1 to 2**: *β* = -0.80, *SE* = 0.584, *z* = -1.369, *p* = 0.171
- **3 to 2 vs 1 to 2**: *β* = -1.23, *SE* = 0.584, *z* = -2.101, *p* = 0.036
- **4 to 2 vs 1 to 2**: *β* = -0.63, *SE* = 0.583, *z* = -1.084, *p* = 0.279
- **5 to 2 vs 1 to 2**: *β* = -2.07, *SE* = 0.589, *z* = -3.519, *p* < .001
- **SNR**: *β* = 0.06, *SE* = 0.151, *z* = 0.427, *p* = 0.669

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 0.80 | 0.58 | 1.37 | 0.171 | 0.617 | n.s. |
| 1 to 2 - 3 to 2 | 1.23 | 0.58 | 2.10 | 0.036 | 0.235 | n.s. |
| 1 to 2 - 4 to 2 | 0.63 | 0.58 | 1.08 | 0.279 | 0.729 | n.s. |
| 1 to 2 - 5 to 2 | 2.07 | 0.59 | 3.52 | < .001 | 0.004 | ** |
| 2 to 2 - 3 to 2 | 0.43 | 0.59 | 0.73 | 0.468 | 0.729 | n.s. |
| 2 to 2 - 4 to 2 | -0.17 | 0.59 | -0.29 | 0.774 | 0.774 | n.s. |
| 2 to 2 - 5 to 2 | 1.27 | 0.60 | 2.13 | 0.033 | 0.235 | n.s. |
| 3 to 2 - 4 to 2 | -0.60 | 0.58 | -1.02 | 0.307 | 0.729 | n.s. |
| 3 to 2 - 5 to 2 | 0.85 | 0.58 | 1.45 | 0.148 | 0.617 | n.s. |
| 4 to 2 - 5 to 2 | 1.44 | 0.59 | 2.46 | 0.014 | 0.120 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.21, *p* = 0.016, η²_G = 0.079
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | 1.46 | 23 | = 0.262 | 0.39 [-0.13, 0.73] | small | n.s. |
| 1 to 2 vs 3 to 2 | 2.22 | 23 | = 0.180 | 0.55 [0.01, 0.90] | medium | n.s. |
| 1 to 2 vs 4 to 2 | 0.96 | 23 | = 0.493 | 0.25 [-0.23, 0.62] | small | n.s. |
| 1 to 2 vs 5 to 2 | 4.18 | 23 | = 0.004 | 0.86 [0.36, 1.35] | large | ** |
| 2 to 2 vs 3 to 2 | 0.76 | 23 | = 0.503 | 0.18 [-0.27, 0.58] | negligible | n.s. |
| 2 to 2 vs 4 to 2 | -0.36 | 23 | = 0.722 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 1.85 | 23 | = 0.193 | 0.53 [-0.06, 0.81] | medium | n.s. |
| 3 to 2 vs 4 to 2 | -0.83 | 23 | = 0.503 | -0.24 [-0.60, 0.26] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.48 | 23 | = 0.262 | 0.35 [-0.13, 0.73] | small | n.s. |
| 4 to 2 vs 5 to 2 | 2.03 | 23 | = 0.180 | 0.54 [-0.03, 0.85] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1049.25, BIC = 1071.55
- **2 to 2 vs 1 to 2**: *β* = 2.12, *SE* = 4.640, *z* = 0.457, *p* = 0.648
- **3 to 2 vs 1 to 2**: *β* = 4.04, *SE* = 4.604, *z* = 0.878, *p* = 0.380
- **4 to 2 vs 1 to 2**: *β* = 5.88, *SE* = 4.609, *z* = 1.276, *p* = 0.202
- **5 to 2 vs 1 to 2**: *β* = 2.57, *SE* = 4.672, *z* = 0.549, *p* = 0.583
- **SNR**: *β* = -0.65, *SE* = 0.739, *z* = -0.882, *p* = 0.378

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | -2.12 | 4.64 | -0.46 | 0.648 | 0.995 | n.s. |
| 1 to 2 - 3 to 2 | -4.04 | 4.60 | -0.88 | 0.380 | 0.986 | n.s. |
| 1 to 2 - 4 to 2 | -5.88 | 4.61 | -1.28 | 0.202 | 0.895 | n.s. |
| 1 to 2 - 5 to 2 | -2.57 | 4.67 | -0.55 | 0.583 | 0.995 | n.s. |
| 2 to 2 - 3 to 2 | -1.92 | 4.68 | -0.41 | 0.681 | 0.995 | n.s. |
| 2 to 2 - 4 to 2 | -3.76 | 4.61 | -0.82 | 0.414 | 0.986 | n.s. |
| 2 to 2 - 5 to 2 | -0.45 | 4.82 | -0.09 | 0.926 | 0.995 | n.s. |
| 3 to 2 - 4 to 2 | -1.84 | 4.63 | -0.40 | 0.691 | 0.995 | n.s. |
| 3 to 2 - 5 to 2 | 1.48 | 4.64 | 0.32 | 0.750 | 0.995 | n.s. |
| 4 to 2 - 5 to 2 | 3.32 | 4.74 | 0.70 | 0.484 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.48, *p* = 0.750, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -0.60 | 23 | = 0.855 | -0.13 [-0.55, 0.30] | negligible | n.s. |
| 1 to 2 vs 3 to 2 | -0.96 | 23 | = 0.855 | -0.18 [-0.62, 0.23] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -1.33 | 23 | = 0.855 | -0.36 [-0.70, 0.16] | small | n.s. |
| 1 to 2 vs 5 to 2 | -0.38 | 23 | = 0.855 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| 2 to 2 vs 3 to 2 | -0.20 | 23 | = 0.855 | -0.05 [-0.46, 0.38] | negligible | n.s. |
| 2 to 2 vs 4 to 2 | -0.82 | 23 | = 0.855 | -0.19 [-0.59, 0.26] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 0.18 | 23 | = 0.855 | 0.04 [-0.38, 0.46] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -0.50 | 23 | = 0.855 | -0.12 [-0.53, 0.32] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 0.40 | 23 | = 0.855 | 0.09 [-0.34, 0.50] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.97 | 23 | = 0.855 | 0.26 [-0.23, 0.62] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 509.03, BIC = 531.33
- **2 to 2 vs 1 to 2**: *β* = -0.18, *SE* = 0.457, *z* = -0.403, *p* = 0.687
- **3 to 2 vs 1 to 2**: *β* = -0.27, *SE* = 0.453, *z* = -0.595, *p* = 0.552
- **4 to 2 vs 1 to 2**: *β* = -0.83, *SE* = 0.453, *z* = -1.842, *p* = 0.065
- **5 to 2 vs 1 to 2**: *β* = -0.94, *SE* = 0.461, *z* = -2.037, *p* = 0.042
- **SNR**: *β* = -0.46, *SE* = 0.079, *z* = -5.796, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 0.18 | 0.46 | 0.40 | 0.687 | 0.969 | n.s. |
| 1 to 2 - 3 to 2 | 0.27 | 0.45 | 0.59 | 0.552 | 0.960 | n.s. |
| 1 to 2 - 4 to 2 | 0.84 | 0.45 | 1.84 | 0.065 | 0.456 | n.s. |
| 1 to 2 - 5 to 2 | 0.94 | 0.46 | 2.04 | 0.042 | 0.347 | n.s. |
| 2 to 2 - 3 to 2 | 0.09 | 0.46 | 0.19 | 0.853 | 0.970 | n.s. |
| 2 to 2 - 4 to 2 | 0.65 | 0.45 | 1.44 | 0.151 | 0.660 | n.s. |
| 2 to 2 - 5 to 2 | 0.75 | 0.48 | 1.58 | 0.114 | 0.621 | n.s. |
| 3 to 2 - 4 to 2 | 0.57 | 0.46 | 1.24 | 0.215 | 0.701 | n.s. |
| 3 to 2 - 5 to 2 | 0.67 | 0.46 | 1.47 | 0.143 | 0.660 | n.s. |
| 4 to 2 - 5 to 2 | 0.10 | 0.47 | 0.22 | 0.826 | 0.970 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.15, *p* = 0.018, η²_G = 0.044
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -0.46 | 23 | = 0.669 | -0.08 [-0.52, 0.33] | negligible | n.s. |
| 1 to 2 vs 3 to 2 | 1.11 | 23 | = 0.347 | 0.17 [-0.20, 0.65] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | 1.24 | 23 | = 0.347 | 0.23 [-0.18, 0.68] | small | n.s. |
| 1 to 2 vs 5 to 2 | 3.06 | 23 | = 0.054 | 0.54 [0.16, 1.09] | medium | n.s. |
| 2 to 2 vs 3 to 2 | 1.20 | 23 | = 0.347 | 0.23 [-0.18, 0.67] | small | n.s. |
| 2 to 2 vs 4 to 2 | 1.33 | 23 | = 0.347 | 0.29 [-0.16, 0.70] | small | n.s. |
| 2 to 2 vs 5 to 2 | 2.77 | 23 | = 0.054 | 0.58 [0.11, 1.02] | medium | n.s. |
| 3 to 2 vs 4 to 2 | 0.43 | 23 | = 0.669 | 0.08 [-0.33, 0.51] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 2.14 | 23 | = 0.144 | 0.37 [-0.00, 0.88] | small | n.s. |
| 4 to 2 vs 5 to 2 | 1.46 | 23 | = 0.347 | 0.27 [-0.13, 0.73] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 786.41, BIC = 808.71
- **2 to 2 vs 1 to 2**: *β* = 1.29, *SE* = 1.477, *z* = 0.871, *p* = 0.384
- **3 to 2 vs 1 to 2**: *β* = 1.49, *SE* = 1.469, *z* = 1.017, *p* = 0.309
- **4 to 2 vs 1 to 2**: *β* = 2.24, *SE* = 1.472, *z* = 1.521, *p* = 0.128
- **5 to 2 vs 1 to 2**: *β* = 0.11, *SE* = 1.475, *z* = 0.072, *p* = 0.943
- **SNR**: *β* = -0.27, *SE* = 0.359, *z* = -0.749, *p* = 0.454

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | -1.29 | 1.48 | -0.87 | 0.384 | 0.950 | n.s. |
| 1 to 2 - 3 to 2 | -1.49 | 1.47 | -1.02 | 0.309 | 0.948 | n.s. |
| 1 to 2 - 4 to 2 | -2.24 | 1.47 | -1.52 | 0.128 | 0.747 | n.s. |
| 1 to 2 - 5 to 2 | -0.11 | 1.48 | -0.07 | 0.943 | 0.988 | n.s. |
| 2 to 2 - 3 to 2 | -0.21 | 1.48 | -0.14 | 0.889 | 0.988 | n.s. |
| 2 to 2 - 4 to 2 | -0.95 | 1.47 | -0.65 | 0.517 | 0.950 | n.s. |
| 2 to 2 - 5 to 2 | 1.18 | 1.47 | 0.80 | 0.421 | 0.950 | n.s. |
| 3 to 2 - 4 to 2 | -0.75 | 1.47 | -0.51 | 0.613 | 0.950 | n.s. |
| 3 to 2 - 5 to 2 | 1.39 | 1.48 | 0.94 | 0.347 | 0.950 | n.s. |
| 4 to 2 - 5 to 2 | 2.13 | 1.47 | 1.45 | 0.147 | 0.760 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.80, *p* = 0.525, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -0.64 | 23 | = 0.728 | -0.16 [-0.56, 0.29] | negligible | n.s. |
| 1 to 2 vs 3 to 2 | -1.12 | 23 | = 0.728 | -0.20 [-0.66, 0.20] | small | n.s. |
| 1 to 2 vs 4 to 2 | -1.42 | 23 | = 0.728 | -0.31 [-0.72, 0.14] | small | n.s. |
| 1 to 2 vs 5 to 2 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 2 to 2 vs 3 to 2 | -0.22 | 23 | = 0.916 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| 2 to 2 vs 4 to 2 | -0.65 | 23 | = 0.728 | -0.15 [-0.56, 0.29] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 0.86 | 23 | = 0.728 | 0.17 [-0.25, 0.60] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -0.56 | 23 | = 0.728 | -0.10 [-0.54, 0.31] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 0.98 | 23 | = 0.728 | 0.21 [-0.23, 0.63] | small | n.s. |
| 4 to 2 vs 5 to 2 | 1.64 | 23 | = 0.728 | 0.32 [-0.10, 0.77] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.00, BIC = 572.30
- **2 to 2 vs 1 to 2**: *β* = 0.79, *SE* = 0.554, *z* = 1.433, *p* = 0.152
- **3 to 2 vs 1 to 2**: *β* = 0.36, *SE* = 0.550, *z* = 0.652, *p* = 0.514
- **4 to 2 vs 1 to 2**: *β* = 0.68, *SE* = 0.552, *z* = 1.237, *p* = 0.216
- **5 to 2 vs 1 to 2**: *β* = 1.45, *SE* = 0.553, *z* = 2.620, *p* = 0.009
- **SNR**: *β* = -0.17, *SE* = 0.134, *z* = -1.289, *p* = 0.197

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | -0.79 | 0.55 | -1.43 | 0.152 | 0.732 | n.s. |
| 1 to 2 - 3 to 2 | -0.36 | 0.55 | -0.65 | 0.514 | 0.897 | n.s. |
| 1 to 2 - 4 to 2 | -0.68 | 0.55 | -1.24 | 0.216 | 0.768 | n.s. |
| 1 to 2 - 5 to 2 | -1.45 | 0.55 | -2.62 | 0.009 | 0.085 | n.s. |
| 2 to 2 - 3 to 2 | 0.43 | 0.55 | 0.78 | 0.433 | 0.897 | n.s. |
| 2 to 2 - 4 to 2 | 0.11 | 0.55 | 0.20 | 0.840 | 0.897 | n.s. |
| 2 to 2 - 5 to 2 | -0.66 | 0.55 | -1.19 | 0.234 | 0.768 | n.s. |
| 3 to 2 - 4 to 2 | -0.32 | 0.55 | -0.59 | 0.558 | 0.897 | n.s. |
| 3 to 2 - 5 to 2 | -1.09 | 0.55 | -1.97 | 0.049 | 0.363 | n.s. |
| 4 to 2 - 5 to 2 | -0.77 | 0.55 | -1.39 | 0.164 | 0.732 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.62, *p* = 0.176, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | -1.28 | 23 | = 0.498 | -0.27 [-0.69, 0.17] | small | n.s. |
| 1 to 2 vs 3 to 2 | -0.79 | 23 | = 0.627 | -0.17 [-0.59, 0.26] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -1.10 | 23 | = 0.498 | -0.25 [-0.65, 0.20] | small | n.s. |
| 1 to 2 vs 5 to 2 | -3.19 | 23 | = 0.040 | -0.58 [-1.12, -0.19] | medium | * |
| 2 to 2 vs 3 to 2 | 0.57 | 23 | = 0.656 | 0.13 [-0.31, 0.54] | negligible | n.s. |
| 2 to 2 vs 4 to 2 | 0.14 | 23 | = 0.893 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | -1.06 | 23 | = 0.498 | -0.23 [-0.64, 0.21] | small | n.s. |
| 3 to 2 vs 4 to 2 | -0.55 | 23 | = 0.656 | -0.10 [-0.54, 0.31] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | -1.71 | 23 | = 0.498 | -0.41 [-0.78, 0.09] | small | n.s. |
| 4 to 2 vs 5 to 2 | -1.11 | 23 | = 0.498 | -0.27 [-0.65, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1207.79, BIC = 1230.09
- **2 to 2 vs 1 to 2**: *β* = -10.41, *SE* = 9.135, *z* = -1.139, *p* = 0.255
- **3 to 2 vs 1 to 2**: *β* = 11.35, *SE* = 9.053, *z* = 1.254, *p* = 0.210
- **4 to 2 vs 1 to 2**: *β* = 0.46, *SE* = 9.058, *z* = 0.050, *p* = 0.960
- **5 to 2 vs 1 to 2**: *β* = -2.30, *SE* = 9.140, *z* = -0.252, *p* = 0.801
- **SNR**: *β* = 1.69, *SE* = 1.276, *z* = 1.327, *p* = 0.185

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 10.41 | 9.13 | 1.14 | 0.255 | 0.848 | n.s. |
| 1 to 2 - 3 to 2 | -11.35 | 9.05 | -1.25 | 0.210 | 0.848 | n.s. |
| 1 to 2 - 4 to 2 | -0.46 | 9.06 | -0.05 | 0.960 | 0.987 | n.s. |
| 1 to 2 - 5 to 2 | 2.30 | 9.14 | 0.25 | 0.801 | 0.987 | n.s. |
| 2 to 2 - 3 to 2 | -21.76 | 9.07 | -2.40 | 0.016 | 0.153 | n.s. |
| 2 to 2 - 4 to 2 | -10.86 | 9.07 | -1.20 | 0.231 | 0.848 | n.s. |
| 2 to 2 - 5 to 2 | -8.11 | 9.43 | -0.86 | 0.390 | 0.862 | n.s. |
| 3 to 2 - 4 to 2 | 10.90 | 9.04 | 1.21 | 0.228 | 0.848 | n.s. |
| 3 to 2 - 5 to 2 | 13.65 | 9.23 | 1.48 | 0.139 | 0.740 | n.s. |
| 4 to 2 - 5 to 2 | 2.76 | 9.25 | 0.30 | 0.765 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.207, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | 1.18 | 23 | = 0.446 | 0.33 [-0.19, 0.67] | small | n.s. |
| 1 to 2 vs 3 to 2 | -1.03 | 23 | = 0.446 | -0.28 [-0.64, 0.22] | small | n.s. |
| 1 to 2 vs 4 to 2 | 0.03 | 23 | = 0.985 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | 0.05 | 23 | = 0.985 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 2 to 2 vs 3 to 2 | -3.12 | 23 | = 0.048 | -0.70 [-1.10, -0.17] | medium | * |
| 2 to 2 vs 4 to 2 | -1.40 | 23 | = 0.446 | -0.34 [-0.72, 0.14] | small | n.s. |
| 2 to 2 vs 5 to 2 | -1.08 | 23 | = 0.446 | -0.33 [-0.65, 0.21] | small | n.s. |
| 3 to 2 vs 4 to 2 | 1.55 | 23 | = 0.446 | 0.30 [-0.12, 0.75] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.24 | 23 | = 0.446 | 0.30 [-0.18, 0.68] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.02 | 23 | = 0.985 | 0.00 [-0.42, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 613.18, BIC = 635.48
- **2 to 2 vs 1 to 2**: *β* = -1.75, *SE* = 0.695, *z* = -2.515, *p* = 0.012
- **3 to 2 vs 1 to 2**: *β* = 1.33, *SE* = 0.688, *z* = 1.933, *p* = 0.053
- **4 to 2 vs 1 to 2**: *β* = 0.51, *SE* = 0.688, *z* = 0.738, *p* = 0.460
- **5 to 2 vs 1 to 2**: *β* = -0.05, *SE* = 0.695, *z* = -0.077, *p* = 0.938
- **SNR**: *β* = 0.31, *SE* = 0.103, *z* = 2.977, *p* = 0.003

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 2 | 1.75 | 0.69 | 2.52 | 0.012 | 0.091 | n.s. |
| 1 to 2 - 3 to 2 | -1.33 | 0.69 | -1.93 | 0.053 | 0.261 | n.s. |
| 1 to 2 - 4 to 2 | -0.51 | 0.69 | -0.74 | 0.460 | 0.810 | n.s. |
| 1 to 2 - 5 to 2 | 0.05 | 0.70 | 0.08 | 0.938 | 0.938 | n.s. |
| 2 to 2 - 3 to 2 | -3.08 | 0.69 | -4.46 | < .001 | < .001 | *** |
| 2 to 2 - 4 to 2 | -2.26 | 0.69 | -3.27 | 0.001 | 0.010 | ** |
| 2 to 2 - 5 to 2 | -1.69 | 0.72 | -2.35 | 0.019 | 0.123 | n.s. |
| 3 to 2 - 4 to 2 | 0.82 | 0.69 | 1.20 | 0.232 | 0.652 | n.s. |
| 3 to 2 - 5 to 2 | 1.38 | 0.70 | 1.97 | 0.049 | 0.261 | n.s. |
| 4 to 2 - 5 to 2 | 0.56 | 0.70 | 0.80 | 0.425 | 0.810 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.71, *p* < .001, η²_G = 0.074
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 2 | 2.53 | 23 | = 0.047 | 0.57 [0.07, 0.97] | medium | * |
| 1 to 2 vs 3 to 2 | -1.57 | 23 | = 0.211 | -0.29 [-0.75, 0.11] | small | n.s. |
| 1 to 2 vs 4 to 2 | -0.42 | 23 | = 0.763 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | -0.41 | 23 | = 0.763 | -0.07 [-0.51, 0.34] | negligible | n.s. |
| 2 to 2 vs 3 to 2 | -4.15 | 23 | = 0.004 | -0.83 [-1.34, -0.36] | large | ** |
| 2 to 2 vs 4 to 2 | -3.54 | 23 | = 0.009 | -0.63 [-1.20, -0.25] | medium | ** |
| 2 to 2 vs 5 to 2 | -2.88 | 23 | = 0.028 | -0.66 [-1.05, -0.13] | medium | * |
| 3 to 2 vs 4 to 2 | 1.50 | 23 | = 0.211 | 0.19 [-0.13, 0.74] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.67 | 23 | = 0.211 | 0.23 [-0.09, 0.78] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.15 | 23 | = 0.879 | 0.02 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.016). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than 5 to 2 (*d* = 0.86)
**N1 amplitude:** Significant main effect of condition (*p* = 0.018) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than 2 to 2 (*d* = 0.57)
  - 2 to 2 showed smaller amplitude than 3 to 2 (*d* = -0.83)
  - 2 to 2 showed smaller amplitude than 4 to 2 (*d* = -0.63)
  - 2 to 2 showed smaller amplitude than 5 to 2 (*d* = -0.66)

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
