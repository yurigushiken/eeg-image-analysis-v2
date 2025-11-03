# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:29:37

---

## 1. Analysis Overview

**Total Measurements:** 291
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

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 19 | 178.32 ms | 20.28 | 4.65 | [148.00, 212.00] |
| 5b3 | 14 | 177.43 ms | 18.54 | 4.95 | [148.00, 212.00] |
| 5c3 | 16 | 176.75 ms | 14.25 | 3.56 | [144.00, 200.00] |
| 5d3 | 20 | 176.60 ms | 16.43 | 3.67 | [144.00, 212.00] |
| 5e3 | 14 | 184.29 ms | 15.96 | 4.27 | [152.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 19 | -7.34 µV | 2.88 | 0.66 | [-12.31, -2.61] |
| 5b3 | 14 | -8.84 µV | 4.51 | 1.20 | [-17.81, -1.14] |
| 5c3 | 16 | -7.89 µV | 3.93 | 0.98 | [-16.11, -2.81] |
| 5d3 | 20 | -6.95 µV | 2.76 | 0.62 | [-12.24, -2.19] |
| 5e3 | 14 | -9.85 µV | 3.27 | 0.87 | [-17.26, -5.15] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 15 | 104.53 ms | 10.13 | 2.61 | [84.00, 120.00] |
| 5b3 | 8 | 99.50 ms | 15.03 | 5.32 | [80.00, 120.00] |
| 5c3 | 12 | 107.33 ms | 11.80 | 3.41 | [80.00, 120.00] |
| 5d3 | 12 | 106.67 ms | 14.80 | 4.27 | [80.00, 120.00] |
| 5e3 | 7 | 101.71 ms | 13.24 | 5.00 | [80.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 15 | 5.28 µV | 2.70 | 0.70 | [1.15, 11.41] |
| 5b3 | 8 | 6.88 µV | 4.99 | 1.76 | [1.53, 15.68] |
| 5c3 | 12 | 6.87 µV | 3.31 | 0.96 | [2.47, 12.00] |
| 5d3 | 12 | 4.63 µV | 1.82 | 0.53 | [2.03, 7.51] |
| 5e3 | 7 | 8.36 µV | 3.72 | 1.40 | [4.73, 13.79] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 18 | 475.11 ms | 26.90 | 6.34 | [432.00, 524.00] |
| 5b3 | 11 | 473.82 ms | 18.19 | 5.48 | [444.00, 500.00] |
| 5c3 | 18 | 477.33 ms | 33.07 | 7.79 | [428.00, 524.00] |
| 5d3 | 18 | 477.33 ms | 31.07 | 7.32 | [436.00, 524.00] |
| 5e3 | 10 | 474.80 ms | 30.11 | 9.52 | [428.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 18 | 6.51 µV | 3.77 | 0.89 | [1.05, 15.42] |
| 5b3 | 11 | 6.86 µV | 2.38 | 0.72 | [4.21, 12.00] |
| 5c3 | 18 | 7.98 µV | 4.42 | 1.04 | [2.42, 20.14] |
| 5d3 | 18 | 8.90 µV | 2.94 | 0.69 | [3.06, 14.21] |
| 5e3 | 10 | 9.63 µV | 3.79 | 1.20 | [5.18, 18.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 718.05, BIC = 737.40
- **5b3 vs 5a3**: *β* = -0.26, *SE* = 5.753, *z* = -0.045, *p* = 0.964
- **5c3 vs 5a3**: *β* = -1.56, *SE* = 5.527, *z* = -0.283, *p* = 0.777
- **5d3 vs 5a3**: *β* = -1.84, *SE* = 5.178, *z* = -0.356, *p* = 0.722
- **5e3 vs 5a3**: *β* = 5.57, *SE* = 5.712, *z* = 0.976, *p* = 0.329
- **SNR**: *β* = -0.86, *SE* = 0.927, *z* = -0.925, *p* = 0.355

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 0.26 | 5.75 | 0.05 | 0.964 | 1.000 | n.s. |
| 5a3 - 5c3 | 1.56 | 5.53 | 0.28 | 0.777 | 1.000 | n.s. |
| 5a3 - 5d3 | 1.84 | 5.18 | 0.36 | 0.722 | 1.000 | n.s. |
| 5a3 - 5e3 | -5.57 | 5.71 | -0.98 | 0.329 | 0.959 | n.s. |
| 5b3 - 5c3 | 1.31 | 5.97 | 0.22 | 0.827 | 1.000 | n.s. |
| 5b3 - 5d3 | 1.58 | 5.68 | 0.28 | 0.780 | 1.000 | n.s. |
| 5b3 - 5e3 | -5.83 | 6.20 | -0.94 | 0.347 | 0.959 | n.s. |
| 5c3 - 5d3 | 0.28 | 5.44 | 0.05 | 0.959 | 1.000 | n.s. |
| 5c3 - 5e3 | -7.14 | 5.98 | -1.19 | 0.232 | 0.908 | n.s. |
| 5d3 - 5e3 | -7.42 | 5.65 | -1.31 | 0.189 | 0.877 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.58, *p* = 0.682, η²_G = 0.064
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 1.06 | 3 | = 0.862 | 0.36 [-0.87, 0.42] | small | n.s. |
| 5a3 vs 5c3 | -0.48 | 3 | = 0.862 | -0.21 [-0.46, 0.82] | small | n.s. |
| 5a3 vs 5d3 | -0.44 | 3 | = 0.862 | -0.23 [-0.48, 0.59] | small | n.s. |
| 5a3 vs 5e3 | 0.00 | 3 | = 1.000 | 0.00 [-0.85, 0.43] | negligible | n.s. |
| 5b3 vs 5c3 | -1.51 | 3 | = 0.862 | -0.52 [-1.00, 0.56] | medium | n.s. |
| 5b3 vs 5d3 | -0.99 | 3 | = 0.862 | -0.50 [-0.45, 0.76] | medium | n.s. |
| 5b3 vs 5e3 | -0.93 | 3 | = 0.862 | -0.39 [-1.32, 0.31] | small | n.s. |
| 5c3 vs 5d3 | -0.08 | 3 | = 1.000 | -0.06 [-0.74, 0.48] | negligible | n.s. |
| 5c3 vs 5e3 | 0.60 | 3 | = 0.862 | 0.26 [-0.68, 1.01] | small | n.s. |
| 5d3 vs 5e3 | 0.48 | 3 | = 0.862 | 0.25 [-0.80, 0.48] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 415.87, BIC = 435.22
- **5b3 vs 5a3**: *β* = -1.52, *SE* = 0.843, *z* = -1.800, *p* = 0.072
- **5c3 vs 5a3**: *β* = -1.21, *SE* = 0.823, *z* = -1.466, *p* = 0.143
- **5d3 vs 5a3**: *β* = 0.16, *SE* = 0.761, *z* = 0.210, *p* = 0.834
- **5e3 vs 5a3**: *β* = -2.60, *SE* = 0.845, *z* = -3.076, *p* = 0.002
- **SNR**: *β* = -0.88, *SE* = 0.156, *z* = -5.643, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 1.52 | 0.84 | 1.80 | 0.072 | 0.407 | n.s. |
| 5a3 - 5c3 | 1.21 | 0.82 | 1.47 | 0.143 | 0.481 | n.s. |
| 5a3 - 5d3 | -0.16 | 0.76 | -0.21 | 0.834 | 0.926 | n.s. |
| 5a3 - 5e3 | 2.60 | 0.85 | 3.08 | 0.002 | 0.019 | * |
| 5b3 - 5c3 | -0.31 | 0.89 | -0.35 | 0.727 | 0.926 | n.s. |
| 5b3 - 5d3 | -1.68 | 0.83 | -2.02 | 0.044 | 0.300 | n.s. |
| 5b3 - 5e3 | 1.08 | 0.92 | 1.18 | 0.237 | 0.556 | n.s. |
| 5c3 - 5d3 | -1.37 | 0.81 | -1.69 | 0.090 | 0.434 | n.s. |
| 5c3 - 5e3 | 1.39 | 0.90 | 1.54 | 0.123 | 0.481 | n.s. |
| 5d3 - 5e3 | 2.76 | 0.84 | 3.28 | 0.001 | 0.010 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.356, η²_G = 0.114
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.54 | 3 | = 0.696 | 0.27 [-0.02, 1.39] | small | n.s. |
| 5a3 vs 5c3 | -0.54 | 3 | = 0.696 | -0.30 [-0.69, 0.58] | small | n.s. |
| 5a3 vs 5d3 | -0.17 | 3 | = 0.879 | -0.06 [-0.66, 0.41] | negligible | n.s. |
| 5a3 vs 5e3 | 1.33 | 3 | = 0.524 | 0.90 [-0.09, 1.30] | large | n.s. |
| 5b3 vs 5c3 | -1.26 | 3 | = 0.524 | -0.42 [-0.86, 0.68] | small | n.s. |
| 5b3 vs 5d3 | -1.21 | 3 | = 0.524 | -0.26 [-1.33, 0.01] | small | n.s. |
| 5b3 vs 5e3 | 1.22 | 3 | = 0.524 | 0.43 [-0.52, 1.04] | small | n.s. |
| 5c3 vs 5d3 | 0.66 | 3 | = 0.696 | 0.24 [-0.80, 0.42] | small | n.s. |
| 5c3 vs 5e3 | 1.39 | 3 | = 0.524 | 0.75 [-0.71, 0.97] | medium | n.s. |
| 5d3 vs 5e3 | 1.41 | 3 | = 0.524 | 0.75 [0.00, 1.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 439.13, BIC = 455.04
- **5b3 vs 5a3**: *β* = -5.04, *SE* = 5.392, *z* = -0.934, *p* = 0.350
- **5c3 vs 5a3**: *β* = 2.74, *SE* = 4.718, *z* = 0.581, *p* = 0.561
- **5d3 vs 5a3**: *β* = 2.40, *SE* = 4.815, *z* = 0.498, *p* = 0.619
- **5e3 vs 5a3**: *β* = -2.92, *SE* = 5.594, *z* = -0.523, *p* = 0.601
- **SNR**: *β* = 0.43, *SE* = 1.480, *z* = 0.288, *p* = 0.773

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 5.04 | 5.39 | 0.93 | 0.350 | 0.959 | n.s. |
| 5a3 - 5c3 | -2.74 | 4.72 | -0.58 | 0.561 | 0.984 | n.s. |
| 5a3 - 5d3 | -2.40 | 4.81 | -0.50 | 0.619 | 0.984 | n.s. |
| 5a3 - 5e3 | 2.93 | 5.59 | 0.52 | 0.601 | 0.984 | n.s. |
| 5b3 - 5c3 | -7.78 | 5.63 | -1.38 | 0.167 | 0.839 | n.s. |
| 5b3 - 5d3 | -7.43 | 5.77 | -1.29 | 0.197 | 0.862 | n.s. |
| 5b3 - 5e3 | -2.11 | 6.42 | -0.33 | 0.742 | 0.984 | n.s. |
| 5c3 - 5d3 | 0.35 | 5.10 | 0.07 | 0.946 | 0.984 | n.s. |
| 5c3 - 5e3 | 5.67 | 5.80 | 0.98 | 0.328 | 0.959 | n.s. |
| 5d3 - 5e3 | 5.32 | 5.92 | 0.90 | 0.369 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 267.46, BIC = 283.37
- **5b3 vs 5a3**: *β* = 1.49, *SE* = 0.986, *z* = 1.515, *p* = 0.130
- **5c3 vs 5a3**: *β* = 1.31, *SE* = 0.880, *z* = 1.493, *p* = 0.135
- **5d3 vs 5a3**: *β* = 0.58, *SE* = 0.892, *z* = 0.653, *p* = 0.514
- **5e3 vs 5a3**: *β* = 2.75, *SE* = 1.084, *z* = 2.536, *p* = 0.011
- **SNR**: *β* = 1.59, *SE* = 0.276, *z* = 5.757, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -1.49 | 0.99 | -1.51 | 0.130 | 0.671 | n.s. |
| 5a3 - 5c3 | -1.31 | 0.88 | -1.49 | 0.135 | 0.671 | n.s. |
| 5a3 - 5d3 | -0.58 | 0.89 | -0.65 | 0.514 | 0.866 | n.s. |
| 5a3 - 5e3 | -2.75 | 1.08 | -2.54 | 0.011 | 0.107 | n.s. |
| 5b3 - 5c3 | 0.18 | 1.05 | 0.17 | 0.864 | 0.866 | n.s. |
| 5b3 - 5d3 | 0.91 | 1.07 | 0.85 | 0.395 | 0.866 | n.s. |
| 5b3 - 5e3 | -1.25 | 1.24 | -1.01 | 0.310 | 0.844 | n.s. |
| 5c3 - 5d3 | 0.73 | 0.95 | 0.77 | 0.439 | 0.866 | n.s. |
| 5c3 - 5e3 | -1.44 | 1.12 | -1.28 | 0.199 | 0.737 | n.s. |
| 5d3 - 5e3 | -2.17 | 1.14 | -1.91 | 0.057 | 0.408 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 727.97, BIC = 746.51
- **5b3 vs 5a3**: *β* = -0.50, *SE* = 10.947, *z* = -0.046, *p* = 0.964
- **5c3 vs 5a3**: *β* = 2.68, *SE* = 9.433, *z* = 0.284, *p* = 0.776
- **5d3 vs 5a3**: *β* = 1.68, *SE* = 9.600, *z* = 0.175, *p* = 0.861
- **5e3 vs 5a3**: *β* = 0.98, *SE* = 11.319, *z* = 0.086, *p* = 0.931
- **SNR**: *β* = 1.18, *SE* = 1.459, *z* = 0.809, *p* = 0.418

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 0.50 | 10.95 | 0.05 | 0.964 | 1.000 | n.s. |
| 5a3 - 5c3 | -2.68 | 9.43 | -0.28 | 0.776 | 1.000 | n.s. |
| 5a3 - 5d3 | -1.68 | 9.60 | -0.18 | 0.861 | 1.000 | n.s. |
| 5a3 - 5e3 | -0.98 | 11.32 | -0.09 | 0.931 | 1.000 | n.s. |
| 5b3 - 5c3 | -3.18 | 11.34 | -0.28 | 0.779 | 1.000 | n.s. |
| 5b3 - 5d3 | -2.18 | 11.73 | -0.19 | 0.852 | 1.000 | n.s. |
| 5b3 - 5e3 | -1.48 | 12.99 | -0.11 | 0.909 | 1.000 | n.s. |
| 5c3 - 5d3 | 1.00 | 9.40 | 0.11 | 0.916 | 1.000 | n.s. |
| 5c3 - 5e3 | 1.70 | 11.06 | 0.15 | 0.878 | 1.000 | n.s. |
| 5d3 - 5e3 | 0.71 | 11.21 | 0.06 | 0.950 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.972, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.08 | 3 | = 1.000 | 0.05 [-0.82, 0.72] | negligible | n.s. |
| 5a3 vs 5c3 | 0.03 | 3 | = 1.000 | 0.03 [-0.45, 0.66] | negligible | n.s. |
| 5a3 vs 5d3 | -0.86 | 3 | = 1.000 | -0.36 [-0.51, 0.60] | small | n.s. |
| 5a3 vs 5e3 | -0.31 | 3 | = 1.000 | -0.28 [-0.81, 0.63] | small | n.s. |
| 5b3 vs 5c3 | 0.00 | 3 | = 1.000 | 0.00 [-0.58, 0.97] | negligible | n.s. |
| 5b3 vs 5d3 | -0.91 | 3 | = 1.000 | -0.44 [-1.38, 0.39] | small | n.s. |
| 5b3 vs 5e3 | -0.41 | 3 | = 1.000 | -0.36 [-0.84, 1.28] | small | n.s. |
| 5c3 vs 5d3 | -0.36 | 3 | = 1.000 | -0.35 [-0.42, 0.61] | small | n.s. |
| 5c3 vs 5e3 | -1.15 | 3 | = 1.000 | -0.28 [-1.05, 0.64] | small | n.s. |
| 5d3 vs 5e3 | 0.08 | 3 | = 1.000 | 0.08 [-0.80, 0.87] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 388.91, BIC = 407.45
- **5b3 vs 5a3**: *β* = 0.81, *SE* = 0.981, *z* = 0.830, *p* = 0.407
- **5c3 vs 5a3**: *β* = 1.66, *SE* = 0.830, *z* = 1.996, *p* = 0.046
- **5d3 vs 5a3**: *β* = 1.90, *SE* = 0.828, *z* = 2.298, *p* = 0.022
- **5e3 vs 5a3**: *β* = 3.23, *SE* = 1.000, *z* = 3.226, *p* = 0.001
- **SNR**: *β* = 0.59, *SE* = 0.139, *z* = 4.277, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -0.81 | 0.98 | -0.83 | 0.407 | 0.770 | n.s. |
| 5a3 - 5c3 | -1.66 | 0.83 | -2.00 | 0.046 | 0.281 | n.s. |
| 5a3 - 5d3 | -1.90 | 0.83 | -2.30 | 0.022 | 0.178 | n.s. |
| 5a3 - 5e3 | -3.23 | 1.00 | -3.23 | 0.001 | 0.012 | * |
| 5b3 - 5c3 | -0.84 | 0.98 | -0.86 | 0.388 | 0.770 | n.s. |
| 5b3 - 5d3 | -1.09 | 0.99 | -1.10 | 0.273 | 0.721 | n.s. |
| 5b3 - 5e3 | -2.41 | 1.12 | -2.16 | 0.031 | 0.220 | n.s. |
| 5c3 - 5d3 | -0.25 | 0.82 | -0.30 | 0.763 | 0.770 | n.s. |
| 5c3 - 5e3 | -1.57 | 1.01 | -1.56 | 0.120 | 0.534 | n.s. |
| 5d3 - 5e3 | -1.32 | 1.02 | -1.30 | 0.195 | 0.662 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.24, *p* = 0.909, η²_G = 0.047
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.45 | 3 | = 0.915 | 0.30 [-0.76, 0.78] | small | n.s. |
| 5a3 vs 5c3 | -0.12 | 3 | = 0.915 | -0.08 [-0.96, 0.19] | negligible | n.s. |
| 5a3 vs 5d3 | -0.15 | 3 | = 0.915 | -0.11 [-1.04, 0.12] | negligible | n.s. |
| 5a3 vs 5e3 | -0.29 | 3 | = 0.915 | -0.23 [-1.03, 0.43] | small | n.s. |
| 5b3 vs 5c3 | -0.85 | 3 | = 0.915 | -0.47 [-1.01, 0.55] | small | n.s. |
| 5b3 vs 5d3 | -1.21 | 3 | = 0.915 | -0.60 [-1.93, 0.07] | medium | n.s. |
| 5b3 vs 5e3 | -0.79 | 3 | = 0.915 | -0.58 [-1.53, 0.66] | medium | n.s. |
| 5c3 vs 5d3 | -0.17 | 3 | = 0.915 | -0.03 [-0.82, 0.23] | negligible | n.s. |
| 5c3 vs 5e3 | -0.56 | 3 | = 0.915 | -0.18 [-1.43, 0.36] | negligible | n.s. |
| 5d3 vs 5e3 | -0.44 | 3 | = 0.915 | -0.18 [-1.15, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


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
