# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:40:19

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
| 4 to 1 | 8 | 109.50 ms | 10.89 | 3.85 | [92.00, 116.00] |
| 4 to 2 | 11 | 101.45 ms | 9.84 | 2.97 | [92.00, 116.00] |
| 4 to 3 | 12 | 103.00 ms | 10.53 | 3.04 | [92.00, 116.00] |
| 4 to 4 | 10 | 104.40 ms | 11.07 | 3.50 | [92.00, 116.00] |
| 4 to 5 | 8 | 109.00 ms | 8.75 | 3.09 | [96.00, 116.00] |
| 4 to 6 | 10 | 107.60 ms | 9.51 | 3.01 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 8 | 2.69 µV | 1.36 | 0.48 | [1.11, 5.17] |
| 4 to 2 | 11 | 3.40 µV | 1.84 | 0.56 | [0.57, 6.56] |
| 4 to 3 | 12 | 2.49 µV | 1.07 | 0.31 | [1.08, 3.91] |
| 4 to 4 | 10 | 1.94 µV | 1.29 | 0.41 | [0.58, 4.79] |
| 4 to 5 | 8 | 3.26 µV | 1.75 | 0.62 | [1.39, 6.78] |
| 4 to 6 | 10 | 3.59 µV | 1.37 | 0.43 | [1.78, 5.29] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 184.80 ms | 15.22 | 3.40 | [144.00, 208.00] |
| 4 to 2 | 24 | 178.33 ms | 14.96 | 3.05 | [148.00, 208.00] |
| 4 to 3 | 23 | 173.39 ms | 16.48 | 3.44 | [152.00, 208.00] |
| 4 to 4 | 22 | 171.45 ms | 20.26 | 4.32 | [144.00, 208.00] |
| 4 to 5 | 22 | 170.36 ms | 20.20 | 4.31 | [144.00, 208.00] |
| 4 to 6 | 22 | 171.27 ms | 20.35 | 4.34 | [144.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | -4.12 µV | 2.04 | 0.46 | [-9.44, -0.51] |
| 4 to 2 | 24 | -6.16 µV | 3.06 | 0.62 | [-12.20, -2.20] |
| 4 to 3 | 23 | -6.36 µV | 2.24 | 0.47 | [-10.92, -1.44] |
| 4 to 4 | 22 | -5.96 µV | 3.11 | 0.66 | [-13.09, -1.82] |
| 4 to 5 | 22 | -7.35 µV | 3.56 | 0.76 | [-16.53, -2.79] |
| 4 to 6 | 22 | -6.82 µV | 3.60 | 0.77 | [-16.09, -3.11] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 113.18 ms | 5.25 | 1.27 | [96.00, 116.00] |
| 4 to 2 | 14 | 113.43 ms | 4.86 | 1.30 | [100.00, 116.00] |
| 4 to 3 | 12 | 104.67 ms | 7.40 | 2.14 | [96.00, 116.00] |
| 4 to 4 | 12 | 108.33 ms | 8.08 | 2.33 | [96.00, 116.00] |
| 4 to 5 | 13 | 106.46 ms | 5.78 | 1.60 | [96.00, 116.00] |
| 4 to 6 | 13 | 106.77 ms | 8.85 | 2.46 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 4.72 µV | 3.09 | 0.75 | [1.46, 13.38] |
| 4 to 2 | 14 | 2.63 µV | 1.21 | 0.32 | [0.46, 4.55] |
| 4 to 3 | 12 | 2.55 µV | 1.34 | 0.39 | [0.60, 5.30] |
| 4 to 4 | 12 | 3.20 µV | 1.82 | 0.53 | [0.96, 6.90] |
| 4 to 5 | 13 | 5.98 µV | 5.46 | 1.51 | [1.25, 19.20] |
| 4 to 6 | 13 | 3.62 µV | 1.54 | 0.43 | [1.77, 6.93] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 488.80 ms | 33.18 | 7.42 | [432.00, 540.00] |
| 4 to 2 | 18 | 484.89 ms | 35.32 | 8.32 | [428.00, 536.00] |
| 4 to 3 | 20 | 477.00 ms | 36.15 | 8.08 | [428.00, 540.00] |
| 4 to 4 | 12 | 483.67 ms | 33.14 | 9.57 | [428.00, 524.00] |
| 4 to 5 | 15 | 506.40 ms | 27.50 | 7.10 | [456.00, 540.00] |
| 4 to 6 | 20 | 494.20 ms | 37.13 | 8.30 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 6.60 µV | 3.32 | 0.74 | [1.12, 12.03] |
| 4 to 2 | 18 | 5.97 µV | 3.63 | 0.85 | [0.66, 14.41] |
| 4 to 3 | 20 | 5.99 µV | 2.98 | 0.67 | [1.17, 11.65] |
| 4 to 4 | 12 | 4.25 µV | 2.49 | 0.72 | [2.14, 8.96] |
| 4 to 5 | 15 | 7.93 µV | 3.60 | 0.93 | [1.95, 13.88] |
| 4 to 6 | 20 | 6.14 µV | 3.45 | 0.77 | [1.80, 12.37] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 448.29, BIC = 466.99
- **4 to 2 vs 4 to 1**: *β* = -6.67, *SE* = 4.169, *z* = -1.599, *p* = 0.110
- **4 to 3 vs 4 to 1**: *β* = -6.00, *SE* = 3.947, *z* = -1.520, *p* = 0.128
- **4 to 4 vs 4 to 1**: *β* = -5.81, *SE* = 4.287, *z* = -1.355, *p* = 0.176
- **4 to 5 vs 4 to 1**: *β* = -0.31, *SE* = 4.467, *z* = -0.069, *p* = 0.945
- **4 to 6 vs 4 to 1**: *β* = -2.21, *SE* = 4.545, *z* = -0.485, *p* = 0.627
- **SNR**: *β* = -1.36, *SE* = 0.933, *z* = -1.453, *p* = 0.146

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 6.66 | 4.17 | 1.60 | 0.110 | 0.826 | n.s. |
| 4 to 1 - 4 to 3 | 6.00 | 3.95 | 1.52 | 0.128 | 0.833 | n.s. |
| 4 to 1 - 4 to 4 | 5.81 | 4.29 | 1.35 | 0.176 | 0.880 | n.s. |
| 4 to 1 - 4 to 5 | 0.31 | 4.47 | 0.07 | 0.945 | 0.999 | n.s. |
| 4 to 1 - 4 to 6 | 2.21 | 4.55 | 0.49 | 0.627 | 0.997 | n.s. |
| 4 to 2 - 4 to 3 | -0.66 | 3.70 | -0.18 | 0.857 | 0.999 | n.s. |
| 4 to 2 - 4 to 4 | -0.86 | 3.97 | -0.22 | 0.829 | 0.999 | n.s. |
| 4 to 2 - 4 to 5 | -6.36 | 4.08 | -1.56 | 0.120 | 0.832 | n.s. |
| 4 to 2 - 4 to 6 | -4.46 | 4.04 | -1.10 | 0.270 | 0.941 | n.s. |
| 4 to 3 - 4 to 4 | -0.19 | 3.81 | -0.05 | 0.960 | 0.999 | n.s. |
| 4 to 3 - 4 to 5 | -5.69 | 3.99 | -1.43 | 0.154 | 0.865 | n.s. |
| 4 to 3 - 4 to 6 | -3.80 | 4.03 | -0.94 | 0.346 | 0.966 | n.s. |
| 4 to 4 - 4 to 5 | -5.50 | 4.16 | -1.32 | 0.186 | 0.880 | n.s. |
| 4 to 4 - 4 to 6 | -3.60 | 4.07 | -0.88 | 0.376 | 0.966 | n.s. |
| 4 to 5 - 4 to 6 | 1.90 | 4.27 | 0.44 | 0.657 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 197.44, BIC = 216.13
- **4 to 2 vs 4 to 1**: *β* = 0.13, *SE* = 0.467, *z* = 0.286, *p* = 0.775
- **4 to 3 vs 4 to 1**: *β* = -0.30, *SE* = 0.436, *z* = -0.694, *p* = 0.488
- **4 to 4 vs 4 to 1**: *β* = -0.58, *SE* = 0.477, *z* = -1.219, *p* = 0.223
- **4 to 5 vs 4 to 1**: *β* = 0.32, *SE* = 0.499, *z* = 0.647, *p* = 0.518
- **4 to 6 vs 4 to 1**: *β* = 0.45, *SE* = 0.508, *z* = 0.885, *p* = 0.376
- **SNR**: *β* = 0.61, *SE* = 0.107, *z* = 5.706, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.13 | 0.47 | -0.29 | 0.775 | 0.989 | n.s. |
| 4 to 1 - 4 to 3 | 0.30 | 0.44 | 0.69 | 0.488 | 0.989 | n.s. |
| 4 to 1 - 4 to 4 | 0.58 | 0.48 | 1.22 | 0.223 | 0.920 | n.s. |
| 4 to 1 - 4 to 5 | -0.32 | 0.50 | -0.65 | 0.518 | 0.989 | n.s. |
| 4 to 1 - 4 to 6 | -0.45 | 0.51 | -0.88 | 0.376 | 0.977 | n.s. |
| 4 to 2 - 4 to 3 | 0.44 | 0.41 | 1.06 | 0.290 | 0.954 | n.s. |
| 4 to 2 - 4 to 4 | 0.72 | 0.44 | 1.64 | 0.102 | 0.725 | n.s. |
| 4 to 2 - 4 to 5 | -0.19 | 0.45 | -0.42 | 0.674 | 0.989 | n.s. |
| 4 to 2 - 4 to 6 | -0.32 | 0.44 | -0.71 | 0.476 | 0.989 | n.s. |
| 4 to 3 - 4 to 4 | 0.28 | 0.42 | 0.67 | 0.505 | 0.989 | n.s. |
| 4 to 3 - 4 to 5 | -0.63 | 0.44 | -1.42 | 0.156 | 0.845 | n.s. |
| 4 to 3 - 4 to 6 | -0.75 | 0.44 | -1.69 | 0.090 | 0.708 | n.s. |
| 4 to 4 - 4 to 5 | -0.90 | 0.46 | -1.97 | 0.049 | 0.505 | n.s. |
| 4 to 4 - 4 to 6 | -1.03 | 0.46 | -2.24 | 0.025 | 0.315 | n.s. |
| 4 to 5 - 4 to 6 | -0.13 | 0.47 | -0.27 | 0.790 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1118.04, BIC = 1144.05
- **4 to 2 vs 4 to 1**: *β* = -8.56, *SE* = 3.964, *z* = -2.159, *p* = 0.031
- **4 to 3 vs 4 to 1**: *β* = -14.79, *SE* = 4.109, *z* = -3.599, *p* < .001
- **4 to 4 vs 4 to 1**: *β* = -15.61, *SE* = 4.162, *z* = -3.749, *p* < .001
- **4 to 5 vs 4 to 1**: *β* = -15.77, *SE* = 4.143, *z* = -3.806, *p* < .001
- **4 to 6 vs 4 to 1**: *β* = -17.56, *SE* = 4.217, *z* = -4.164, *p* < .001
- **SNR**: *β* = 0.83, *SE* = 0.465, *z* = 1.782, *p* = 0.075

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 8.56 | 3.96 | 2.16 | 0.031 | 0.269 | n.s. |
| 4 to 1 - 4 to 3 | 14.79 | 4.11 | 3.60 | < .001 | 0.004 | ** |
| 4 to 1 - 4 to 4 | 15.61 | 4.16 | 3.75 | < .001 | 0.002 | ** |
| 4 to 1 - 4 to 5 | 15.77 | 4.14 | 3.81 | < .001 | 0.002 | ** |
| 4 to 1 - 4 to 6 | 17.56 | 4.22 | 4.16 | < .001 | < .001 | *** |
| 4 to 2 - 4 to 3 | 6.23 | 3.80 | 1.64 | 0.101 | 0.525 | n.s. |
| 4 to 2 - 4 to 4 | 7.05 | 3.85 | 1.83 | 0.067 | 0.430 | n.s. |
| 4 to 2 - 4 to 5 | 7.21 | 3.84 | 1.88 | 0.061 | 0.430 | n.s. |
| 4 to 2 - 4 to 6 | 9.00 | 3.88 | 2.32 | 0.020 | 0.203 | n.s. |
| 4 to 3 - 4 to 4 | 0.82 | 3.86 | 0.21 | 0.832 | 0.992 | n.s. |
| 4 to 3 - 4 to 5 | 0.98 | 3.86 | 0.25 | 0.800 | 0.992 | n.s. |
| 4 to 3 - 4 to 6 | 2.77 | 3.87 | 0.72 | 0.473 | 0.979 | n.s. |
| 4 to 4 - 4 to 5 | 0.16 | 3.91 | 0.04 | 0.967 | 0.992 | n.s. |
| 4 to 4 - 4 to 6 | 1.95 | 3.90 | 0.50 | 0.617 | 0.992 | n.s. |
| 4 to 5 - 4 to 6 | 1.79 | 3.92 | 0.46 | 0.648 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.93, *p* = 0.019, η²_G = 0.119
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.43 | 13 | = 0.315 | 0.52 [-0.05, 0.93] | medium | n.s. |
| 4 to 1 vs 4 to 3 | 1.91 | 13 | = 0.235 | 0.66 [0.10, 1.16] | medium | n.s. |
| 4 to 1 vs 4 to 4 | 2.07 | 13 | = 0.222 | 0.61 [0.08, 1.17] | medium | n.s. |
| 4 to 1 vs 4 to 5 | 3.53 | 13 | = 0.052 | 1.12 [0.31, 1.49] | large | n.s. |
| 4 to 1 vs 4 to 6 | 3.20 | 13 | = 0.052 | 1.00 [0.23, 1.38] | large | n.s. |
| 4 to 2 vs 4 to 3 | 0.45 | 13 | = 0.758 | 0.15 [-0.13, 0.76] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 0.52 | 13 | = 0.758 | 0.19 [-0.17, 0.74] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 2.70 | 13 | = 0.091 | 0.66 [-0.07, 0.85] | medium | n.s. |
| 4 to 2 vs 4 to 6 | 1.32 | 13 | = 0.315 | 0.56 [-0.10, 0.81] | medium | n.s. |
| 4 to 3 vs 4 to 4 | 0.21 | 13 | = 0.896 | 0.06 [-0.36, 0.55] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 1.45 | 13 | = 0.315 | 0.49 [-0.46, 0.46] | small | n.s. |
| 4 to 3 vs 4 to 6 | 1.37 | 13 | = 0.315 | 0.41 [-0.26, 0.66] | small | n.s. |
| 4 to 4 vs 4 to 5 | 1.25 | 13 | = 0.317 | 0.36 [-0.41, 0.53] | small | n.s. |
| 4 to 4 vs 4 to 6 | 1.70 | 13 | = 0.282 | 0.30 [-0.26, 0.66] | small | n.s. |
| 4 to 5 vs 4 to 6 | -0.13 | 13 | = 0.896 | -0.05 [-0.40, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 587.96, BIC = 613.97
- **4 to 2 vs 4 to 1**: *β* = -1.58, *SE* = 0.522, *z* = -3.020, *p* = 0.003
- **4 to 3 vs 4 to 1**: *β* = -1.34, *SE* = 0.542, *z* = -2.484, *p* = 0.013
- **4 to 4 vs 4 to 1**: *β* = -0.97, *SE* = 0.549, *z* = -1.764, *p* = 0.078
- **4 to 5 vs 4 to 1**: *β* = -2.26, *SE* = 0.547, *z* = -4.141, *p* < .001
- **4 to 6 vs 4 to 1**: *β* = -1.54, *SE* = 0.556, *z* = -2.770, *p* = 0.006
- **SNR**: *β* = -0.43, *SE* = 0.062, *z* = -6.900, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 1.58 | 0.52 | 3.02 | 0.003 | 0.035 | * |
| 4 to 1 - 4 to 3 | 1.35 | 0.54 | 2.48 | 0.013 | 0.135 | n.s. |
| 4 to 1 - 4 to 4 | 0.97 | 0.55 | 1.76 | 0.078 | 0.522 | n.s. |
| 4 to 1 - 4 to 5 | 2.26 | 0.55 | 4.14 | < .001 | < .001 | *** |
| 4 to 1 - 4 to 6 | 1.54 | 0.56 | 2.77 | 0.006 | 0.071 | n.s. |
| 4 to 2 - 4 to 3 | -0.23 | 0.50 | -0.46 | 0.642 | 0.954 | n.s. |
| 4 to 2 - 4 to 4 | -0.61 | 0.51 | -1.20 | 0.230 | 0.791 | n.s. |
| 4 to 2 - 4 to 5 | 0.69 | 0.51 | 1.36 | 0.175 | 0.754 | n.s. |
| 4 to 2 - 4 to 6 | -0.04 | 0.51 | -0.08 | 0.940 | 0.954 | n.s. |
| 4 to 3 - 4 to 4 | -0.38 | 0.51 | -0.74 | 0.459 | 0.914 | n.s. |
| 4 to 3 - 4 to 5 | 0.92 | 0.51 | 1.80 | 0.071 | 0.522 | n.s. |
| 4 to 3 - 4 to 6 | 0.19 | 0.51 | 0.38 | 0.704 | 0.954 | n.s. |
| 4 to 4 - 4 to 5 | 1.30 | 0.52 | 2.51 | 0.012 | 0.135 | n.s. |
| 4 to 4 - 4 to 6 | 0.57 | 0.51 | 1.11 | 0.267 | 0.791 | n.s. |
| 4 to 5 - 4 to 6 | -0.72 | 0.52 | -1.40 | 0.161 | 0.754 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.70, *p* = 0.001, η²_G = 0.140
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 3.80 | 13 | = 0.013 | 1.15 [0.21, 1.26] | large | * |
| 4 to 1 vs 4 to 3 | 4.25 | 13 | = 0.013 | 1.43 [0.39, 1.55] | large | * |
| 4 to 1 vs 4 to 4 | 2.77 | 13 | = 0.048 | 0.89 [0.09, 1.18] | large | * |
| 4 to 1 vs 4 to 5 | 3.59 | 13 | = 0.013 | 1.41 [0.37, 1.58] | large | * |
| 4 to 1 vs 4 to 6 | 3.56 | 13 | = 0.013 | 1.05 [0.19, 1.32] | large | * |
| 4 to 2 vs 4 to 3 | -0.08 | 13 | = 0.940 | -0.02 [-0.30, 0.57] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | -0.56 | 13 | = 0.782 | -0.11 [-0.48, 0.41] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 0.67 | 13 | = 0.782 | 0.23 [-0.19, 0.72] | small | n.s. |
| 4 to 2 vs 4 to 6 | 0.40 | 13 | = 0.782 | 0.09 [-0.23, 0.66] | negligible | n.s. |
| 4 to 3 vs 4 to 4 | -0.41 | 13 | = 0.782 | -0.11 [-0.59, 0.33] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 1.07 | 13 | = 0.628 | 0.28 [-0.15, 0.79] | small | n.s. |
| 4 to 3 vs 4 to 6 | 0.46 | 13 | = 0.782 | 0.11 [-0.32, 0.59] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | 1.00 | 13 | = 0.628 | 0.32 [-0.14, 0.82] | small | n.s. |
| 4 to 4 vs 4 to 6 | 1.43 | 13 | = 0.440 | 0.18 [-0.11, 0.83] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -0.35 | 13 | = 0.782 | -0.11 [-0.56, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 546.94, BIC = 568.49
- **4 to 2 vs 4 to 1**: *β* = 0.80, *SE* = 2.293, *z* = 0.347, *p* = 0.729
- **4 to 3 vs 4 to 1**: *β* = -7.93, *SE* = 2.302, *z* = -3.445, *p* = 0.001
- **4 to 4 vs 4 to 1**: *β* = -5.33, *SE* = 2.325, *z* = -2.293, *p* = 0.022
- **4 to 5 vs 4 to 1**: *β* = -6.24, *SE* = 2.259, *z* = -2.764, *p* = 0.006
- **4 to 6 vs 4 to 1**: *β* = -6.11, *SE* = 2.283, *z* = -2.675, *p* = 0.007
- **SNR**: *β* = 0.53, *SE* = 0.433, *z* = 1.234, *p* = 0.217

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.80 | 2.29 | -0.35 | 0.729 | 0.993 | n.s. |
| 4 to 1 - 4 to 3 | 7.93 | 2.30 | 3.45 | < .001 | 0.008 | ** |
| 4 to 1 - 4 to 4 | 5.33 | 2.32 | 2.29 | 0.022 | 0.162 | n.s. |
| 4 to 1 - 4 to 5 | 6.24 | 2.26 | 2.76 | 0.006 | 0.061 | n.s. |
| 4 to 1 - 4 to 6 | 6.11 | 2.28 | 2.67 | 0.007 | 0.072 | n.s. |
| 4 to 2 - 4 to 3 | 8.73 | 2.35 | 3.71 | < .001 | 0.003 | ** |
| 4 to 2 - 4 to 4 | 6.13 | 2.42 | 2.53 | 0.011 | 0.097 | n.s. |
| 4 to 2 - 4 to 5 | 7.04 | 2.33 | 3.02 | 0.003 | 0.032 | * |
| 4 to 2 - 4 to 6 | 6.90 | 2.32 | 2.98 | 0.003 | 0.034 | * |
| 4 to 3 - 4 to 4 | -2.60 | 2.51 | -1.04 | 0.300 | 0.917 | n.s. |
| 4 to 3 - 4 to 5 | -1.69 | 2.40 | -0.70 | 0.482 | 0.972 | n.s. |
| 4 to 3 - 4 to 6 | -1.82 | 2.41 | -0.76 | 0.449 | 0.972 | n.s. |
| 4 to 4 - 4 to 5 | 0.91 | 2.47 | 0.37 | 0.711 | 0.993 | n.s. |
| 4 to 4 - 4 to 6 | 0.78 | 2.44 | 0.32 | 0.750 | 0.993 | n.s. |
| 4 to 5 - 4 to 6 | -0.14 | 2.36 | -0.06 | 0.953 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.15, *p* = 0.398, η²_G = 0.255
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | nan | 2 | n/a | 0.00 [-0.68, 0.59] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | 1.31 | 2 | = 0.657 | 1.10 [0.41, 2.45] | large | n.s. |
| 4 to 1 vs 4 to 4 | 1.00 | 2 | = 0.657 | 0.82 [-0.13, 1.61] | large | n.s. |
| 4 to 1 vs 4 to 5 | 1.11 | 2 | = 0.657 | 1.15 [-0.19, 1.50] | large | n.s. |
| 4 to 1 vs 4 to 6 | 0.55 | 2 | = 0.718 | 0.52 [-0.20, 1.35] | medium | n.s. |
| 4 to 2 vs 4 to 3 | 1.31 | 2 | = 0.657 | 1.10 [-0.00, 1.52] | large | n.s. |
| 4 to 2 vs 4 to 4 | 1.00 | 2 | = 0.657 | 0.82 [-0.10, 1.65] | large | n.s. |
| 4 to 2 vs 4 to 5 | 1.11 | 2 | = 0.657 | 1.15 [0.01, 1.68] | large | n.s. |
| 4 to 2 vs 4 to 6 | 0.55 | 2 | = 0.718 | 0.52 [-0.10, 1.65] | medium | n.s. |
| 4 to 3 vs 4 to 4 | -1.51 | 2 | = 0.657 | -0.70 [-1.00, 0.86] | medium | n.s. |
| 4 to 3 vs 4 to 5 | -0.50 | 2 | = 0.718 | -0.32 [-1.05, 0.64] | small | n.s. |
| 4 to 3 vs 4 to 6 | -2.00 | 2 | = 0.657 | -0.62 [-1.36, 0.41] | medium | n.s. |
| 4 to 4 vs 4 to 5 | 0.76 | 2 | = 0.718 | 0.52 [-0.72, 1.45] | medium | n.s. |
| 4 to 4 vs 4 to 6 | 0.00 | 2 | = 1.000 | 0.00 [-0.92, 0.92] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -1.00 | 2 | = 0.657 | -0.41 [-0.64, 0.91] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 378.37, BIC = 399.92
- **4 to 2 vs 4 to 1**: *β* = -0.44, *SE* = 0.838, *z* = -0.523, *p* = 0.601
- **4 to 3 vs 4 to 1**: *β* = -1.27, *SE* = 0.851, *z* = -1.491, *p* = 0.136
- **4 to 4 vs 4 to 1**: *β* = -0.82, *SE* = 0.842, *z* = -0.970, *p* = 0.332
- **4 to 5 vs 4 to 1**: *β* = 2.10, *SE* = 0.827, *z* = 2.532, *p* = 0.011
- **4 to 6 vs 4 to 1**: *β* = 0.14, *SE* = 0.836, *z* = 0.161, *p* = 0.872
- **SNR**: *β* = 0.96, *SE* = 0.151, *z* = 6.363, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 0.44 | 0.84 | 0.52 | 0.601 | 0.975 | n.s. |
| 4 to 1 - 4 to 3 | 1.27 | 0.85 | 1.49 | 0.136 | 0.732 | n.s. |
| 4 to 1 - 4 to 4 | 0.82 | 0.84 | 0.97 | 0.332 | 0.941 | n.s. |
| 4 to 1 - 4 to 5 | -2.09 | 0.83 | -2.53 | 0.011 | 0.128 | n.s. |
| 4 to 1 - 4 to 6 | -0.13 | 0.84 | -0.16 | 0.872 | 0.975 | n.s. |
| 4 to 2 - 4 to 3 | 0.83 | 0.87 | 0.95 | 0.341 | 0.941 | n.s. |
| 4 to 2 - 4 to 4 | 0.38 | 0.88 | 0.43 | 0.667 | 0.975 | n.s. |
| 4 to 2 - 4 to 5 | -2.53 | 0.86 | -2.96 | 0.003 | 0.039 | * |
| 4 to 2 - 4 to 6 | -0.57 | 0.85 | -0.67 | 0.500 | 0.969 | n.s. |
| 4 to 3 - 4 to 4 | -0.45 | 0.90 | -0.50 | 0.616 | 0.975 | n.s. |
| 4 to 3 - 4 to 5 | -3.36 | 0.88 | -3.81 | < .001 | 0.002 | ** |
| 4 to 3 - 4 to 6 | -1.40 | 0.88 | -1.59 | 0.113 | 0.697 | n.s. |
| 4 to 4 - 4 to 5 | -2.91 | 0.88 | -3.29 | < .001 | 0.014 | * |
| 4 to 4 - 4 to 6 | -0.95 | 0.89 | -1.07 | 0.284 | 0.931 | n.s. |
| 4 to 5 - 4 to 6 | 1.96 | 0.86 | 2.27 | 0.023 | 0.229 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.611, η²_G = 0.263
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.95 | 2 | = 0.700 | 1.53 [-0.08, 1.31] | large | n.s. |
| 4 to 1 vs 4 to 3 | 1.69 | 2 | = 0.700 | 0.98 [-0.01, 1.65] | large | n.s. |
| 4 to 1 vs 4 to 4 | 2.10 | 2 | = 0.700 | 1.10 [-0.29, 1.36] | large | n.s. |
| 4 to 1 vs 4 to 5 | 0.45 | 2 | = 0.895 | 0.50 [-0.37, 1.23] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 0.80 | 2 | = 0.844 | 0.84 [-0.49, 0.96] | large | n.s. |
| 4 to 2 vs 4 to 3 | -2.15 | 2 | = 0.700 | -1.43 [-0.59, 0.75] | large | n.s. |
| 4 to 2 vs 4 to 4 | -1.20 | 2 | = 0.758 | -0.83 [-0.93, 0.61] | large | n.s. |
| 4 to 2 vs 4 to 5 | -0.86 | 2 | = 0.844 | -0.71 [-1.48, 0.11] | medium | n.s. |
| 4 to 2 vs 4 to 6 | -1.20 | 2 | = 0.758 | -1.08 [-1.43, 0.24] | large | n.s. |
| 4 to 3 vs 4 to 4 | 2.61 | 2 | = 0.700 | 0.28 [-0.86, 1.00] | small | n.s. |
| 4 to 3 vs 4 to 5 | -0.27 | 2 | = 0.895 | -0.24 [-1.72, 0.18] | small | n.s. |
| 4 to 3 vs 4 to 6 | -0.11 | 2 | = 0.921 | -0.13 [-1.08, 0.61] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | -0.40 | 2 | = 0.895 | -0.37 [-1.60, 0.62] | small | n.s. |
| 4 to 4 vs 4 to 6 | -0.30 | 2 | = 0.895 | -0.35 [-1.09, 0.77] | small | n.s. |
| 4 to 5 vs 4 to 6 | 0.24 | 2 | = 0.895 | 0.16 [-0.53, 1.03] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1045.09, BIC = 1068.98
- **4 to 2 vs 4 to 1**: *β* = -6.51, *SE* = 10.028, *z* = -0.649, *p* = 0.516
- **4 to 3 vs 4 to 1**: *β* = -13.24, *SE* = 9.558, *z* = -1.386, *p* = 0.166
- **4 to 4 vs 4 to 1**: *β* = -4.46, *SE* = 11.629, *z* = -0.384, *p* = 0.701
- **4 to 5 vs 4 to 1**: *β* = 17.71, *SE* = 10.569, *z* = 1.676, *p* = 0.094
- **4 to 6 vs 4 to 1**: *β* = 4.75, *SE* = 9.644, *z* = 0.493, *p* = 0.622
- **SNR**: *β* = -0.19, *SE* = 0.723, *z* = -0.265, *p* = 0.791

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 6.51 | 10.03 | 0.65 | 0.516 | 0.974 | n.s. |
| 4 to 1 - 4 to 3 | 13.24 | 9.56 | 1.39 | 0.166 | 0.837 | n.s. |
| 4 to 1 - 4 to 4 | 4.46 | 11.63 | 0.38 | 0.701 | 0.974 | n.s. |
| 4 to 1 - 4 to 5 | -17.71 | 10.57 | -1.68 | 0.094 | 0.662 | n.s. |
| 4 to 1 - 4 to 6 | -4.75 | 9.64 | -0.49 | 0.622 | 0.974 | n.s. |
| 4 to 2 - 4 to 3 | 6.73 | 9.81 | 0.69 | 0.493 | 0.974 | n.s. |
| 4 to 2 - 4 to 4 | -2.05 | 11.44 | -0.18 | 0.858 | 0.974 | n.s. |
| 4 to 2 - 4 to 5 | -24.22 | 10.54 | -2.30 | 0.022 | 0.263 | n.s. |
| 4 to 2 - 4 to 6 | -11.26 | 9.77 | -1.15 | 0.249 | 0.899 | n.s. |
| 4 to 3 - 4 to 4 | -8.78 | 11.31 | -0.78 | 0.437 | 0.974 | n.s. |
| 4 to 3 - 4 to 5 | -30.95 | 10.36 | -2.99 | 0.003 | 0.041 | * |
| 4 to 3 - 4 to 6 | -18.00 | 9.43 | -1.91 | 0.056 | 0.530 | n.s. |
| 4 to 4 - 4 to 5 | -22.17 | 11.77 | -1.88 | 0.060 | 0.530 | n.s. |
| 4 to 4 - 4 to 6 | -9.22 | 11.14 | -0.83 | 0.408 | 0.974 | n.s. |
| 4 to 5 - 4 to 6 | 12.96 | 10.29 | 1.26 | 0.208 | 0.878 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.523, η²_G = 0.124
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | -1.24 | 5 | = 0.717 | -0.45 [-0.47, 0.59] | small | n.s. |
| 4 to 1 vs 4 to 3 | -0.18 | 5 | = 0.861 | -0.13 [-0.20, 0.86] | negligible | n.s. |
| 4 to 1 vs 4 to 4 | -0.33 | 5 | = 0.861 | -0.24 [-0.61, 0.82] | small | n.s. |
| 4 to 1 vs 4 to 5 | -1.57 | 5 | = 0.698 | -0.91 [-1.26, 0.00] | large | n.s. |
| 4 to 1 vs 4 to 6 | -1.53 | 5 | = 0.698 | -0.60 [-0.64, 0.39] | medium | n.s. |
| 4 to 2 vs 4 to 3 | 0.58 | 5 | = 0.861 | 0.40 [-0.52, 0.55] | small | n.s. |
| 4 to 2 vs 4 to 4 | 0.35 | 5 | = 0.861 | 0.25 [-0.60, 0.95] | small | n.s. |
| 4 to 2 vs 4 to 5 | -0.86 | 5 | = 0.717 | -0.59 [-1.43, -0.07] | medium | n.s. |
| 4 to 2 vs 4 to 6 | -0.39 | 5 | = 0.861 | -0.23 [-0.82, 0.27] | small | n.s. |
| 4 to 3 vs 4 to 4 | -0.21 | 5 | = 0.861 | -0.13 [-0.96, 0.41] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | -1.64 | 5 | = 0.698 | -0.98 [-1.24, 0.02] | large | n.s. |
| 4 to 3 vs 4 to 6 | -0.86 | 5 | = 0.717 | -0.58 [-0.98, 0.04] | medium | n.s. |
| 4 to 4 vs 4 to 5 | -2.48 | 5 | = 0.698 | -0.81 [-1.48, 0.21] | large | n.s. |
| 4 to 4 vs 4 to 6 | -0.90 | 5 | = 0.717 | -0.44 [-0.64, 0.64] | small | n.s. |
| 4 to 5 vs 4 to 6 | 1.12 | 5 | = 0.717 | 0.29 [-0.23, 0.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 485.14, BIC = 509.03
- **4 to 2 vs 4 to 1**: *β* = 0.34, *SE* = 0.626, *z* = 0.546, *p* = 0.585
- **4 to 3 vs 4 to 1**: *β* = 0.03, *SE* = 0.595, *z* = 0.054, *p* = 0.957
- **4 to 4 vs 4 to 1**: *β* = -1.34, *SE* = 0.743, *z* = -1.805, *p* = 0.071
- **4 to 5 vs 4 to 1**: *β* = 1.71, *SE* = 0.669, *z* = 2.550, *p* = 0.011
- **4 to 6 vs 4 to 1**: *β* = 0.28, *SE* = 0.603, *z* = 0.466, *p* = 0.641
- **SNR**: *β* = 0.30, *SE* = 0.050, *z* = 5.967, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.34 | 0.63 | -0.55 | 0.585 | 0.995 | n.s. |
| 4 to 1 - 4 to 3 | -0.03 | 0.60 | -0.05 | 0.957 | 0.995 | n.s. |
| 4 to 1 - 4 to 4 | 1.34 | 0.74 | 1.80 | 0.071 | 0.403 | n.s. |
| 4 to 1 - 4 to 5 | -1.71 | 0.67 | -2.55 | 0.011 | 0.131 | n.s. |
| 4 to 1 - 4 to 6 | -0.28 | 0.60 | -0.47 | 0.641 | 0.995 | n.s. |
| 4 to 2 - 4 to 3 | 0.31 | 0.61 | 0.51 | 0.612 | 0.995 | n.s. |
| 4 to 2 - 4 to 4 | 1.68 | 0.72 | 2.35 | 0.019 | 0.204 | n.s. |
| 4 to 2 - 4 to 5 | -1.36 | 0.65 | -2.09 | 0.037 | 0.288 | n.s. |
| 4 to 2 - 4 to 6 | 0.06 | 0.61 | 0.10 | 0.920 | 0.995 | n.s. |
| 4 to 3 - 4 to 4 | 1.37 | 0.71 | 1.93 | 0.053 | 0.355 | n.s. |
| 4 to 3 - 4 to 5 | -1.67 | 0.65 | -2.58 | 0.010 | 0.129 | n.s. |
| 4 to 3 - 4 to 6 | -0.25 | 0.58 | -0.43 | 0.669 | 0.995 | n.s. |
| 4 to 4 - 4 to 5 | -3.05 | 0.73 | -4.15 | < .001 | < .001 | *** |
| 4 to 4 - 4 to 6 | -1.62 | 0.70 | -2.33 | 0.020 | 0.204 | n.s. |
| 4 to 5 - 4 to 6 | 1.43 | 0.64 | 2.22 | 0.026 | 0.234 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.29, *p* = 0.002, η²_G = 0.201
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.12 | 5 | = 0.472 | 0.36 [-0.43, 0.64] | small | n.s. |
| 4 to 1 vs 4 to 3 | 1.12 | 5 | = 0.472 | 0.32 [-0.36, 0.67] | small | n.s. |
| 4 to 1 vs 4 to 4 | 4.26 | 5 | = 0.107 | 1.94 [0.49, 2.60] | large | n.s. |
| 4 to 1 vs 4 to 5 | 1.97 | 5 | = 0.226 | 0.53 [-0.68, 0.48] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 1.42 | 5 | = 0.402 | 0.30 [-0.39, 0.64] | small | n.s. |
| 4 to 2 vs 4 to 3 | -0.14 | 5 | = 0.943 | -0.06 [-0.54, 0.52] | negligible | n.s. |
| 4 to 2 vs 4 to 4 | 3.46 | 5 | = 0.107 | 1.14 [-0.18, 1.52] | large | n.s. |
| 4 to 2 vs 4 to 5 | 0.94 | 5 | = 0.535 | 0.14 [-0.99, 0.26] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | -0.35 | 5 | = 0.854 | -0.07 [-0.49, 0.57] | negligible | n.s. |
| 4 to 3 vs 4 to 4 | 2.42 | 5 | = 0.151 | 1.34 [0.10, 1.68] | large | n.s. |
| 4 to 3 vs 4 to 5 | 0.71 | 5 | = 0.637 | 0.21 [-0.83, 0.34] | small | n.s. |
| 4 to 3 vs 4 to 6 | -0.08 | 5 | = 0.943 | -0.02 [-0.45, 0.51] | negligible | n.s. |
| 4 to 4 vs 4 to 5 | -2.74 | 5 | = 0.140 | -1.01 [-1.74, 0.05] | large | n.s. |
| 4 to 4 vs 4 to 6 | -3.31 | 5 | = 0.107 | -1.34 [-1.52, -0.06] | large | n.s. |
| 4 to 5 vs 4 to 6 | -2.63 | 5 | = 0.140 | -0.22 [-0.55, 0.60] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.019) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 2 (*d* = 1.15)
  - 4 to 1 showed greater amplitude than 4 to 3 (*d* = 1.43)
  - 4 to 1 showed greater amplitude than 4 to 4 (*d* = 0.89)
  - 4 to 1 showed greater amplitude than 4 to 5 (*d* = 1.41)
  - 4 to 1 showed greater amplitude than 4 to 6 (*d* = 1.05)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002) (no significant pairwise comparisons)

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
