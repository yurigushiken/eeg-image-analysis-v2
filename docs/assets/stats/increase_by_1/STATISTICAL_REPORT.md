# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:22:44

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
| 1 to 2 | 24 | 93.33 ms | 9.77 | 2.00 | [84.00, 108.00] |
| 2 to 3 | 24 | 96.67 ms | 10.05 | 2.05 | [84.00, 108.00] |
| 3 to 4 | 24 | 98.50 ms | 10.07 | 2.05 | [84.00, 108.00] |
| 4 to 5 | 24 | 96.83 ms | 10.08 | 2.06 | [84.00, 108.00] |
| 5 to 6 | 24 | 97.00 ms | 9.08 | 1.85 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -0.40 µV | 2.30 | 0.47 | [-5.67, 4.51] |
| 2 to 3 | 24 | -1.43 µV | 1.96 | 0.40 | [-5.76, 2.45] |
| 3 to 4 | 24 | -1.54 µV | 1.62 | 0.33 | [-5.20, 1.86] |
| 4 to 5 | 24 | -1.97 µV | 3.20 | 0.65 | [-10.33, 5.09] |
| 5 to 6 | 24 | -1.64 µV | 1.85 | 0.38 | [-5.35, 1.09] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 170.33 ms | 17.85 | 3.64 | [144.00, 204.00] |
| 2 to 3 | 24 | 171.17 ms | 20.16 | 4.11 | [140.00, 204.00] |
| 3 to 4 | 24 | 167.50 ms | 19.39 | 3.96 | [140.00, 204.00] |
| 4 to 5 | 24 | 167.83 ms | 19.51 | 3.98 | [140.00, 204.00] |
| 5 to 6 | 24 | 174.33 ms | 17.92 | 3.66 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -5.30 µV | 2.42 | 0.49 | [-9.95, -0.26] |
| 2 to 3 | 24 | -4.94 µV | 2.20 | 0.45 | [-10.61, -0.11] |
| 3 to 4 | 24 | -5.38 µV | 2.47 | 0.50 | [-10.31, 0.32] |
| 4 to 5 | 24 | -5.55 µV | 2.90 | 0.59 | [-11.05, -0.28] |
| 5 to 6 | 24 | -5.77 µV | 2.68 | 0.55 | [-11.88, -0.44] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 98.00 ms | 12.48 | 2.55 | [84.00, 112.00] |
| 2 to 3 | 24 | 100.67 ms | 11.04 | 2.25 | [84.00, 112.00] |
| 3 to 4 | 24 | 99.67 ms | 11.43 | 2.33 | [84.00, 112.00] |
| 4 to 5 | 24 | 98.50 ms | 11.61 | 2.37 | [84.00, 112.00] |
| 5 to 6 | 24 | 98.83 ms | 11.03 | 2.25 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 1.02 µV | 2.06 | 0.42 | [-3.63, 4.57] |
| 2 to 3 | 24 | 1.51 µV | 2.12 | 0.43 | [-3.02, 6.87] |
| 3 to 4 | 24 | 2.22 µV | 2.17 | 0.44 | [-1.39, 7.39] |
| 4 to 5 | 24 | 2.06 µV | 3.32 | 0.68 | [-3.81, 13.41] |
| 5 to 6 | 24 | 1.46 µV | 2.21 | 0.45 | [-2.96, 6.38] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 484.50 ms | 37.25 | 7.60 | [432.00, 536.00] |
| 2 to 3 | 24 | 479.00 ms | 40.83 | 8.33 | [432.00, 536.00] |
| 3 to 4 | 24 | 489.17 ms | 37.74 | 7.70 | [432.00, 536.00] |
| 4 to 5 | 24 | 483.00 ms | 37.29 | 7.61 | [432.00, 536.00] |
| 5 to 6 | 24 | 485.33 ms | 36.14 | 7.38 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 3.90 µV | 3.77 | 0.77 | [-3.51, 11.52] |
| 2 to 3 | 24 | 4.25 µV | 4.37 | 0.89 | [-3.66, 13.70] |
| 3 to 4 | 24 | 3.95 µV | 4.31 | 0.88 | [-3.98, 12.86] |
| 4 to 5 | 24 | 3.96 µV | 4.45 | 0.91 | [-3.22, 16.10] |
| 5 to 6 | 24 | 1.64 µV | 3.40 | 0.70 | [-4.86, 9.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 892.51, BIC = 914.81
- **2 to 3 vs 1 to 2**: *β* = 3.61, *SE* = 2.574, *z* = 1.402, *p* = 0.161
- **3 to 4 vs 1 to 2**: *β* = 5.58, *SE* = 2.579, *z* = 2.164, *p* = 0.030
- **4 to 5 vs 1 to 2**: *β* = 2.87, *SE* = 2.590, *z* = 1.108, *p* = 0.268
- **5 to 6 vs 1 to 2**: *β* = 4.09, *SE* = 2.579, *z* = 1.584, *p* = 0.113
- **SNR**: *β* = 1.03, *SE* = 0.514, *z* = 2.015, *p* = 0.044

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -3.61 | 2.57 | -1.40 | 0.161 | 0.754 | n.s. |
| 1 to 2 - 3 to 4 | -5.58 | 2.58 | -2.16 | 0.030 | 0.266 | n.s. |
| 1 to 2 - 4 to 5 | -2.87 | 2.59 | -1.11 | 0.268 | 0.887 | n.s. |
| 1 to 2 - 5 to 6 | -4.09 | 2.58 | -1.58 | 0.113 | 0.661 | n.s. |
| 2 to 3 - 3 to 4 | -1.97 | 2.57 | -0.77 | 0.443 | 0.946 | n.s. |
| 2 to 3 - 4 to 5 | 0.74 | 2.61 | 0.28 | 0.777 | 0.963 | n.s. |
| 2 to 3 - 5 to 6 | -0.48 | 2.57 | -0.19 | 0.853 | 0.963 | n.s. |
| 3 to 4 - 4 to 5 | 2.71 | 2.62 | 1.03 | 0.301 | 0.887 | n.s. |
| 3 to 4 - 5 to 6 | 1.50 | 2.57 | 0.58 | 0.561 | 0.963 | n.s. |
| 4 to 5 - 5 to 6 | -1.22 | 2.62 | -0.46 | 0.642 | 0.963 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.03, *p* = 0.398, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.17 | 23 | = 0.634 | -0.34 [-0.67, 0.19] | small | n.s. |
| 1 to 2 vs 3 to 4 | -2.00 | 23 | = 0.578 | -0.52 [-0.85, 0.03] | medium | n.s. |
| 1 to 2 vs 4 to 5 | -1.24 | 23 | = 0.634 | -0.35 [-0.68, 0.18] | small | n.s. |
| 1 to 2 vs 5 to 6 | -1.36 | 23 | = 0.634 | -0.39 [-0.71, 0.15] | small | n.s. |
| 2 to 3 vs 3 to 4 | -0.60 | 23 | = 0.806 | -0.18 [-0.55, 0.30] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | -0.08 | 23 | = 0.940 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | -0.13 | 23 | = 0.940 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 0.59 | 23 | = 0.806 | 0.17 [-0.30, 0.54] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 0.59 | 23 | = 0.806 | 0.16 [-0.30, 0.54] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -0.08 | 23 | = 0.940 | -0.02 [-0.44, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 544.95, BIC = 567.25
- **2 to 3 vs 1 to 2**: *β* = -1.06, *SE* = 0.614, *z* = -1.724, *p* = 0.085
- **3 to 4 vs 1 to 2**: *β* = -1.19, *SE* = 0.615, *z* = -1.927, *p* = 0.054
- **4 to 5 vs 1 to 2**: *β* = -1.51, *SE* = 0.617, *z* = -2.453, *p* = 0.014
- **5 to 6 vs 1 to 2**: *β* = -1.28, *SE* = 0.615, *z* = -2.084, *p* = 0.037
- **SNR**: *β* = -0.10, *SE* = 0.120, *z* = -0.822, *p* = 0.411

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 1.06 | 0.61 | 1.72 | 0.085 | 0.462 | n.s. |
| 1 to 2 - 3 to 4 | 1.18 | 0.61 | 1.93 | 0.054 | 0.358 | n.s. |
| 1 to 2 - 4 to 5 | 1.51 | 0.62 | 2.45 | 0.014 | 0.133 | n.s. |
| 1 to 2 - 5 to 6 | 1.28 | 0.61 | 2.08 | 0.037 | 0.289 | n.s. |
| 2 to 3 - 3 to 4 | 0.13 | 0.61 | 0.21 | 0.836 | 0.993 | n.s. |
| 2 to 3 - 4 to 5 | 0.46 | 0.62 | 0.73 | 0.464 | 0.976 | n.s. |
| 2 to 3 - 5 to 6 | 0.22 | 0.61 | 0.36 | 0.716 | 0.993 | n.s. |
| 3 to 4 - 4 to 5 | 0.33 | 0.62 | 0.53 | 0.599 | 0.990 | n.s. |
| 3 to 4 - 5 to 6 | 0.10 | 0.61 | 0.16 | 0.875 | 0.993 | n.s. |
| 4 to 5 - 5 to 6 | -0.23 | 0.62 | -0.37 | 0.710 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.79, *p* = 0.138, η²_G = 0.055
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | 1.89 | 23 | = 0.179 | 0.48 [-0.05, 0.82] | small | n.s. |
| 1 to 2 vs 3 to 4 | 2.05 | 23 | = 0.179 | 0.58 [-0.02, 0.86] | medium | n.s. |
| 1 to 2 vs 4 to 5 | 2.40 | 23 | = 0.179 | 0.56 [0.04, 0.94] | medium | n.s. |
| 1 to 2 vs 5 to 6 | 1.97 | 23 | = 0.179 | 0.59 [-0.04, 0.84] | medium | n.s. |
| 2 to 3 vs 3 to 4 | 0.23 | 23 | = 0.852 | 0.06 [-0.38, 0.47] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.72 | 23 | = 0.824 | 0.20 [-0.28, 0.57] | small | n.s. |
| 2 to 3 vs 5 to 6 | 0.40 | 23 | = 0.852 | 0.11 [-0.34, 0.50] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 0.69 | 23 | = 0.824 | 0.17 [-0.28, 0.57] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 0.19 | 23 | = 0.852 | 0.06 [-0.38, 0.46] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -0.38 | 23 | = 0.852 | -0.13 [-0.50, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1024.81, BIC = 1047.11
- **2 to 3 vs 1 to 2**: *β* = 0.97, *SE* = 3.968, *z* = 0.245, *p* = 0.807
- **3 to 4 vs 1 to 2**: *β* = -2.68, *SE* = 3.971, *z* = -0.674, *p* = 0.500
- **4 to 5 vs 1 to 2**: *β* = -2.50, *SE* = 3.956, *z* = -0.633, *p* = 0.527
- **5 to 6 vs 1 to 2**: *β* = 3.79, *SE* = 3.983, *z* = 0.951, *p* = 0.341
- **SNR**: *β* = 0.28, *SE* = 0.616, *z* = 0.450, *p* = 0.653

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.97 | 3.97 | -0.24 | 0.807 | 0.965 | n.s. |
| 1 to 2 - 3 to 4 | 2.68 | 3.97 | 0.67 | 0.500 | 0.965 | n.s. |
| 1 to 2 - 4 to 5 | 2.50 | 3.96 | 0.63 | 0.527 | 0.965 | n.s. |
| 1 to 2 - 5 to 6 | -3.79 | 3.98 | -0.95 | 0.341 | 0.965 | n.s. |
| 2 to 3 - 3 to 4 | 3.65 | 3.96 | 0.92 | 0.356 | 0.965 | n.s. |
| 2 to 3 - 4 to 5 | 3.47 | 3.97 | 0.88 | 0.381 | 0.965 | n.s. |
| 2 to 3 - 5 to 6 | -2.82 | 4.03 | -0.70 | 0.484 | 0.965 | n.s. |
| 3 to 4 - 4 to 5 | -0.17 | 3.97 | -0.04 | 0.965 | 0.965 | n.s. |
| 3 to 4 - 5 to 6 | -6.47 | 4.04 | -1.60 | 0.109 | 0.686 | n.s. |
| 4 to 5 - 5 to 6 | -6.29 | 3.98 | -1.58 | 0.114 | 0.686 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.94, *p* = 0.445, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.21 | 23 | = 0.915 | -0.04 [-0.46, 0.38] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | 0.70 | 23 | = 0.741 | 0.15 [-0.28, 0.57] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.53 | 23 | = 0.749 | 0.13 [-0.31, 0.53] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -0.90 | 23 | = 0.741 | -0.22 [-0.61, 0.24] | small | n.s. |
| 2 to 3 vs 3 to 4 | 0.88 | 23 | = 0.741 | 0.19 [-0.25, 0.61] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.66 | 23 | = 0.741 | 0.17 [-0.29, 0.56] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | -1.03 | 23 | = 0.741 | -0.17 [-0.64, 0.22] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | -0.11 | 23 | = 0.915 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | -1.91 | 23 | = 0.569 | -0.37 [-0.83, 0.05] | small | n.s. |
| 4 to 5 vs 5 to 6 | -1.64 | 23 | = 0.569 | -0.35 [-0.77, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 463.19, BIC = 485.49
- **2 to 3 vs 1 to 2**: *β* = 0.11, *SE* = 0.363, *z* = 0.315, *p* = 0.753
- **3 to 4 vs 1 to 2**: *β* = -0.36, *SE* = 0.363, *z* = -1.006, *p* = 0.315
- **4 to 5 vs 1 to 2**: *β* = -0.24, *SE* = 0.362, *z* = -0.659, *p* = 0.510
- **5 to 6 vs 1 to 2**: *β* = -0.09, *SE* = 0.364, *z* = -0.232, *p* = 0.816
- **SNR**: *β* = -0.51, *SE* = 0.057, *z* = -8.946, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.11 | 0.36 | -0.31 | 0.753 | 0.989 | n.s. |
| 1 to 2 - 3 to 4 | 0.37 | 0.36 | 1.01 | 0.315 | 0.967 | n.s. |
| 1 to 2 - 4 to 5 | 0.24 | 0.36 | 0.66 | 0.510 | 0.986 | n.s. |
| 1 to 2 - 5 to 6 | 0.08 | 0.36 | 0.23 | 0.816 | 0.989 | n.s. |
| 2 to 3 - 3 to 4 | 0.48 | 0.36 | 1.33 | 0.185 | 0.871 | n.s. |
| 2 to 3 - 4 to 5 | 0.35 | 0.36 | 0.97 | 0.331 | 0.967 | n.s. |
| 2 to 3 - 5 to 6 | 0.20 | 0.37 | 0.54 | 0.590 | 0.988 | n.s. |
| 3 to 4 - 4 to 5 | -0.13 | 0.36 | -0.35 | 0.727 | 0.989 | n.s. |
| 3 to 4 - 5 to 6 | -0.28 | 0.37 | -0.76 | 0.448 | 0.984 | n.s. |
| 4 to 5 - 5 to 6 | -0.15 | 0.36 | -0.42 | 0.673 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.82, *p* = 0.516, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.89 | 23 | = 0.649 | -0.16 [-0.61, 0.24] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | 0.18 | 23 | = 0.860 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.50 | 23 | = 0.824 | 0.09 [-0.32, 0.52] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | 0.88 | 23 | = 0.649 | 0.18 [-0.25, 0.60] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 1.02 | 23 | = 0.649 | 0.19 [-0.22, 0.63] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 1.19 | 23 | = 0.649 | 0.24 [-0.19, 0.67] | small | n.s. |
| 2 to 3 vs 5 to 6 | 1.67 | 23 | = 0.649 | 0.34 [-0.09, 0.78] | small | n.s. |
| 3 to 4 vs 4 to 5 | 0.30 | 23 | = 0.853 | 0.06 [-0.36, 0.48] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 0.90 | 23 | = 0.649 | 0.15 [-0.24, 0.61] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | 0.45 | 23 | = 0.824 | 0.08 [-0.33, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 930.20, BIC = 952.50
- **2 to 3 vs 1 to 2**: *β* = 2.96, *SE* = 2.919, *z* = 1.012, *p* = 0.311
- **3 to 4 vs 1 to 2**: *β* = 1.93, *SE* = 2.915, *z* = 0.661, *p* = 0.508
- **4 to 5 vs 1 to 2**: *β* = 0.39, *SE* = 2.900, *z* = 0.135, *p* = 0.893
- **5 to 6 vs 1 to 2**: *β* = 1.11, *SE* = 2.918, *z* = 0.381, *p* = 0.703
- **SNR**: *β* = 0.63, *SE* = 0.780, *z* = 0.803, *p* = 0.422

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -2.96 | 2.92 | -1.01 | 0.311 | 0.976 | n.s. |
| 1 to 2 - 3 to 4 | -1.93 | 2.92 | -0.66 | 0.508 | 0.997 | n.s. |
| 1 to 2 - 4 to 5 | -0.39 | 2.90 | -0.13 | 0.893 | 0.998 | n.s. |
| 1 to 2 - 5 to 6 | -1.11 | 2.92 | -0.38 | 0.703 | 0.998 | n.s. |
| 2 to 3 - 3 to 4 | 1.03 | 2.90 | 0.35 | 0.723 | 0.998 | n.s. |
| 2 to 3 - 4 to 5 | 2.56 | 2.94 | 0.87 | 0.383 | 0.987 | n.s. |
| 2 to 3 - 5 to 6 | 1.84 | 2.90 | 0.64 | 0.525 | 0.997 | n.s. |
| 3 to 4 - 4 to 5 | 1.54 | 2.93 | 0.52 | 0.600 | 0.997 | n.s. |
| 3 to 4 - 5 to 6 | 0.82 | 2.90 | 0.28 | 0.778 | 0.998 | n.s. |
| 4 to 5 - 5 to 6 | -0.72 | 2.94 | -0.25 | 0.806 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.25, *p* = 0.909, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.75 | 23 | = 0.911 | -0.23 [-0.58, 0.27] | small | n.s. |
| 1 to 2 vs 3 to 4 | -0.60 | 23 | = 0.911 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | -0.20 | 23 | = 0.911 | -0.04 [-0.46, 0.38] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -0.28 | 23 | = 0.911 | -0.07 [-0.48, 0.36] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 0.37 | 23 | = 0.911 | 0.09 [-0.35, 0.50] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.70 | 23 | = 0.911 | 0.19 [-0.28, 0.57] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | 0.58 | 23 | = 0.911 | 0.17 [-0.31, 0.54] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 0.40 | 23 | = 0.911 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 0.28 | 23 | = 0.911 | 0.07 [-0.37, 0.48] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -0.11 | 23 | = 0.911 | -0.03 [-0.45, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 554.86, BIC = 577.16
- **2 to 3 vs 1 to 2**: *β* = 0.66, *SE* = 0.626, *z* = 1.057, *p* = 0.291
- **3 to 4 vs 1 to 2**: *β* = 1.35, *SE* = 0.626, *z* = 2.154, *p* = 0.031
- **4 to 5 vs 1 to 2**: *β* = 0.97, *SE* = 0.622, *z* = 1.553, *p* = 0.120
- **5 to 6 vs 1 to 2**: *β* = 0.60, *SE* = 0.626, *z* = 0.966, *p* = 0.334
- **SNR**: *β* = 0.37, *SE* = 0.164, *z* = 2.267, *p* = 0.023

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.66 | 0.63 | -1.06 | 0.291 | 0.890 | n.s. |
| 1 to 2 - 3 to 4 | -1.35 | 0.63 | -2.15 | 0.031 | 0.272 | n.s. |
| 1 to 2 - 4 to 5 | -0.97 | 0.62 | -1.55 | 0.120 | 0.685 | n.s. |
| 1 to 2 - 5 to 6 | -0.60 | 0.63 | -0.97 | 0.334 | 0.890 | n.s. |
| 2 to 3 - 3 to 4 | -0.69 | 0.62 | -1.10 | 0.270 | 0.890 | n.s. |
| 2 to 3 - 4 to 5 | -0.30 | 0.63 | -0.48 | 0.629 | 0.957 | n.s. |
| 2 to 3 - 5 to 6 | 0.06 | 0.62 | 0.09 | 0.927 | 0.957 | n.s. |
| 3 to 4 - 4 to 5 | 0.38 | 0.63 | 0.61 | 0.545 | 0.957 | n.s. |
| 3 to 4 - 5 to 6 | 0.74 | 0.62 | 1.19 | 0.232 | 0.879 | n.s. |
| 4 to 5 - 5 to 6 | 0.36 | 0.63 | 0.57 | 0.566 | 0.957 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.11, *p* = 0.356, η²_G = 0.032
- Greenhouse-Geisser corrected: *p* = 0.347 (ε = 0.665)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.11 | 23 | = 0.561 | -0.23 [-0.65, 0.20] | small | n.s. |
| 1 to 2 vs 3 to 4 | -2.48 | 23 | = 0.207 | -0.56 [-0.96, -0.06] | medium | n.s. |
| 1 to 2 vs 4 to 5 | -1.35 | 23 | = 0.478 | -0.37 [-0.71, 0.16] | small | n.s. |
| 1 to 2 vs 5 to 6 | -0.89 | 23 | = 0.617 | -0.21 [-0.61, 0.24] | small | n.s. |
| 2 to 3 vs 3 to 4 | -1.43 | 23 | = 0.478 | -0.33 [-0.72, 0.14] | small | n.s. |
| 2 to 3 vs 4 to 5 | -0.73 | 23 | = 0.617 | -0.19 [-0.57, 0.28] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | 0.08 | 23 | = 0.936 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 0.19 | 23 | = 0.936 | 0.06 [-0.38, 0.46] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 1.43 | 23 | = 0.478 | 0.34 [-0.14, 0.72] | small | n.s. |
| 4 to 5 vs 5 to 6 | 0.70 | 23 | = 0.617 | 0.21 [-0.28, 0.57] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1222.03, BIC = 1244.33
- **2 to 3 vs 1 to 2**: *β* = -4.60, *SE* = 10.653, *z* = -0.432, *p* = 0.666
- **3 to 4 vs 1 to 2**: *β* = 5.63, *SE* = 10.657, *z* = 0.529, *p* = 0.597
- **4 to 5 vs 1 to 2**: *β* = -1.65, *SE* = 10.631, *z* = -0.155, *p* = 0.877
- **5 to 6 vs 1 to 2**: *β* = -0.07, *SE* = 10.653, *z* = -0.006, *p* = 0.995
- **SNR**: *β* = -1.28, *SE* = 0.989, *z* = -1.290, *p* = 0.197

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 4.60 | 10.65 | 0.43 | 0.666 | 0.999 | n.s. |
| 1 to 2 - 3 to 4 | -5.63 | 10.66 | -0.53 | 0.597 | 0.999 | n.s. |
| 1 to 2 - 4 to 5 | 1.65 | 10.63 | 0.16 | 0.877 | 0.999 | n.s. |
| 1 to 2 - 5 to 6 | 0.07 | 10.65 | 0.01 | 0.995 | 0.999 | n.s. |
| 2 to 3 - 3 to 4 | -10.23 | 10.63 | -0.96 | 0.336 | 0.983 | n.s. |
| 2 to 3 - 4 to 5 | -2.95 | 10.66 | -0.28 | 0.782 | 0.999 | n.s. |
| 2 to 3 - 5 to 6 | -4.53 | 10.72 | -0.42 | 0.672 | 0.999 | n.s. |
| 3 to 4 - 4 to 5 | 7.28 | 10.67 | 0.68 | 0.495 | 0.998 | n.s. |
| 3 to 4 - 5 to 6 | 5.70 | 10.73 | 0.53 | 0.595 | 0.999 | n.s. |
| 4 to 5 - 5 to 6 | -1.58 | 10.65 | -0.15 | 0.882 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.929, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | 0.52 | 23 | = 0.934 | 0.14 [-0.32, 0.53] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -0.41 | 23 | = 0.934 | -0.12 [-0.51, 0.34] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.12 | 23 | = 0.934 | 0.04 [-0.40, 0.45] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -0.08 | 23 | = 0.934 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | -0.88 | 23 | = 0.934 | -0.26 [-0.61, 0.25] | small | n.s. |
| 2 to 3 vs 4 to 5 | -0.34 | 23 | = 0.934 | -0.10 [-0.49, 0.35] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | -0.52 | 23 | = 0.934 | -0.16 [-0.53, 0.32] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | 0.55 | 23 | = 0.934 | 0.16 [-0.31, 0.53] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 0.34 | 23 | = 0.934 | 0.10 [-0.35, 0.49] | negligible | n.s. |
| 4 to 5 vs 5 to 6 | -0.25 | 23 | = 0.934 | -0.06 [-0.47, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 611.22, BIC = 633.52
- **2 to 3 vs 1 to 2**: *β* = 0.14, *SE* = 0.658, *z* = 0.216, *p* = 0.829
- **3 to 4 vs 1 to 2**: *β* = -0.17, *SE* = 0.659, *z* = -0.265, *p* = 0.791
- **4 to 5 vs 1 to 2**: *β* = 0.10, *SE* = 0.656, *z* = 0.146, *p* = 0.884
- **5 to 6 vs 1 to 2**: *β* = -2.04, *SE* = 0.658, *z* = -3.104, *p* = 0.002
- **SNR**: *β* = 0.30, *SE* = 0.079, *z* = 3.750, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.14 | 0.66 | -0.22 | 0.829 | 0.998 | n.s. |
| 1 to 2 - 3 to 4 | 0.17 | 0.66 | 0.26 | 0.791 | 0.998 | n.s. |
| 1 to 2 - 4 to 5 | -0.10 | 0.66 | -0.15 | 0.884 | 0.998 | n.s. |
| 1 to 2 - 5 to 6 | 2.04 | 0.66 | 3.10 | 0.002 | 0.015 | * |
| 2 to 3 - 3 to 4 | 0.32 | 0.66 | 0.48 | 0.629 | 0.997 | n.s. |
| 2 to 3 - 4 to 5 | 0.05 | 0.66 | 0.07 | 0.944 | 0.998 | n.s. |
| 2 to 3 - 5 to 6 | 2.19 | 0.67 | 3.28 | 0.001 | 0.010 | * |
| 3 to 4 - 4 to 5 | -0.27 | 0.66 | -0.41 | 0.682 | 0.997 | n.s. |
| 3 to 4 - 5 to 6 | 1.87 | 0.67 | 2.81 | 0.005 | 0.035 | * |
| 4 to 5 - 5 to 6 | 2.14 | 0.66 | 3.25 | 0.001 | 0.010 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.41, *p* = 0.003, η²_G = 0.054
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.54 | 23 | = 0.968 | -0.09 [-0.53, 0.31] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -0.08 | 23 | = 0.989 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | -0.06 | 23 | = 0.989 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | 2.98 | 23 | = 0.017 | 0.63 [0.15, 1.07] | medium | * |
| 2 to 3 vs 3 to 4 | 0.54 | 23 | = 0.968 | 0.07 [-0.31, 0.53] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.42 | 23 | = 0.968 | 0.07 [-0.34, 0.51] | negligible | n.s. |
| 2 to 3 vs 5 to 6 | 3.41 | 23 | = 0.012 | 0.66 [0.23, 1.17] | medium | * |
| 3 to 4 vs 4 to 5 | -0.01 | 23 | = 0.989 | -0.00 [-0.43, 0.42] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | 3.07 | 23 | = 0.017 | 0.59 [0.17, 1.09] | medium | * |
| 4 to 5 vs 5 to 6 | 3.45 | 23 | = 0.012 | 0.58 [0.23, 1.17] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than 5 to 6 (*d* = 0.63)
  - 2 to 3 showed greater amplitude than 5 to 6 (*d* = 0.66)
  - 3 to 4 showed greater amplitude than 5 to 6 (*d* = 0.59)
  - 4 to 5 showed greater amplitude than 5 to 6 (*d* = 0.58)

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
