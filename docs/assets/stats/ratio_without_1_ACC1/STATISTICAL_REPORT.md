# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:37:02

---

## 1. Analysis Overview

**Total Measurements:** 460
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
| Ratio 0.5 (1:2, no 1) | 24 | 103.00 ms | 7.85 | 1.60 | [92.00, 112.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 102.83 ms | 7.78 | 1.59 | [92.00, 112.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 102.67 ms | 7.70 | 1.57 | [92.00, 112.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 103.33 ms | 7.33 | 1.50 | [92.00, 112.00] |
| Ratio 0.83 (5:6, no 1) | 19 | 102.32 ms | 7.92 | 1.82 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | -1.21 µV | 1.25 | 0.26 | [-3.53, 0.70] |
| Ratio 0.67 (2:3, no 1) | 24 | -1.04 µV | 1.38 | 0.28 | [-3.88, 1.37] |
| Ratio 0.75 (3:4, no 1) | 24 | -1.00 µV | 1.69 | 0.35 | [-5.60, 2.51] |
| Ratio 0.8 (4:5, no 1) | 24 | -2.08 µV | 2.59 | 0.53 | [-8.41, 1.59] |
| Ratio 0.83 (5:6, no 1) | 19 | -1.89 µV | 2.37 | 0.54 | [-6.40, 3.29] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 172.67 ms | 16.03 | 3.27 | [140.00, 204.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 173.17 ms | 19.33 | 3.95 | [144.00, 204.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 172.17 ms | 18.74 | 3.83 | [140.00, 204.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 172.50 ms | 19.25 | 3.93 | [140.00, 204.00] |
| Ratio 0.83 (5:6, no 1) | 19 | 176.42 ms | 22.31 | 5.12 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | -5.90 µV | 2.17 | 0.44 | [-10.43, -2.77] |
| Ratio 0.67 (2:3, no 1) | 24 | -5.22 µV | 2.36 | 0.48 | [-10.09, -2.11] |
| Ratio 0.75 (3:4, no 1) | 24 | -5.52 µV | 2.36 | 0.48 | [-10.31, -0.04] |
| Ratio 0.8 (4:5, no 1) | 24 | -5.66 µV | 2.94 | 0.60 | [-11.24, 0.46] |
| Ratio 0.83 (5:6, no 1) | 19 | -6.04 µV | 2.61 | 0.60 | [-11.29, -1.78] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 107.00 ms | 8.69 | 1.77 | [96.00, 116.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 108.00 ms | 8.42 | 1.72 | [96.00, 116.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 105.33 ms | 8.64 | 1.76 | [96.00, 116.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 107.00 ms | 7.85 | 1.60 | [96.00, 116.00] |
| Ratio 0.83 (5:6, no 1) | 19 | 105.89 ms | 8.26 | 1.89 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 1.16 µV | 1.73 | 0.35 | [-2.57, 4.97] |
| Ratio 0.67 (2:3, no 1) | 24 | 0.89 µV | 1.91 | 0.39 | [-2.21, 5.72] |
| Ratio 0.75 (3:4, no 1) | 24 | 1.12 µV | 1.83 | 0.37 | [-1.59, 5.67] |
| Ratio 0.8 (4:5, no 1) | 24 | 1.71 µV | 2.45 | 0.50 | [-2.97, 6.17] |
| Ratio 0.83 (5:6, no 1) | 19 | 2.38 µV | 3.96 | 0.91 | [-3.00, 16.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 489.67 ms | 31.82 | 6.50 | [444.00, 540.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 488.50 ms | 36.42 | 7.43 | [444.00, 540.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 494.33 ms | 31.80 | 6.49 | [444.00, 540.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 494.00 ms | 33.59 | 6.86 | [444.00, 540.00] |
| Ratio 0.83 (5:6, no 1) | 19 | 502.11 ms | 34.68 | 7.96 | [444.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 3.83 µV | 3.27 | 0.67 | [-2.11, 10.84] |
| Ratio 0.67 (2:3, no 1) | 24 | 4.01 µV | 3.78 | 0.77 | [-1.89, 14.05] |
| Ratio 0.75 (3:4, no 1) | 24 | 4.05 µV | 3.75 | 0.77 | [-3.66, 11.73] |
| Ratio 0.8 (4:5, no 1) | 24 | 4.25 µV | 3.81 | 0.78 | [-4.71, 10.40] |
| Ratio 0.83 (5:6, no 1) | 19 | 3.90 µV | 5.19 | 1.19 | [-3.89, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 776.81, BIC = 798.77
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.26, *SE* = 1.631, *z* = -0.158, *p* = 0.875
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.20, *SE* = 1.634, *z* = -0.123, *p* = 0.902
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.41, *SE* = 1.630, *z* = 0.253, *p* = 0.800
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.39, *SE* = 1.754, *z* = -0.219, *p* = 0.826
- **SNR**: *β* = 0.42, *SE* = 0.414, *z* = 1.014, *p* = 0.311

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.26 | 1.63 | 0.16 | 0.875 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.20 | 1.63 | 0.12 | 0.902 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.41 | 1.63 | -0.25 | 0.800 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.38 | 1.75 | 0.22 | 0.826 | 1.000 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.06 | 1.64 | -0.03 | 0.973 | 1.000 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.67 | 1.64 | -0.41 | 0.683 | 1.000 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.13 | 1.76 | 0.07 | 0.942 | 1.000 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.61 | 1.63 | -0.38 | 0.707 | 1.000 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.18 | 1.75 | 0.10 | 0.916 | 1.000 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.80 | 1.75 | 0.45 | 0.649 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.975, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.23 | 18 | = 0.920 | 0.05 [-0.40, 0.44] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.23 | 18 | = 0.920 | -0.05 [-0.38, 0.47] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.40 | 18 | = 0.920 | -0.08 [-0.47, 0.37] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.10 | 18 | = 0.920 | 0.03 [-0.46, 0.51] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.41 | 18 | = 0.920 | -0.11 [-0.40, 0.44] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.89 | 18 | = 0.920 | -0.14 [-0.49, 0.36] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.11 | 18 | = 0.920 | -0.03 [-0.51, 0.46] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.13 | 18 | = 0.920 | -0.03 [-0.52, 0.33] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.31 | 18 | = 0.920 | 0.08 [-0.41, 0.55] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.51 | 18 | = 0.920 | 0.11 [-0.37, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 455.52, BIC = 477.48
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.27, *SE* = 0.430, *z* = 0.625, *p* = 0.532
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.08, *SE* = 0.431, *z* = 0.184, *p* = 0.854
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.95, *SE* = 0.430, *z* = -2.206, *p* = 0.027
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.93, *SE* = 0.462, *z* = -2.008, *p* = 0.045
- **SNR**: *β* = -0.43, *SE* = 0.110, *z* = -3.900, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.27 | 0.43 | -0.62 | 0.532 | 0.952 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.08 | 0.43 | -0.18 | 0.854 | 0.979 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.95 | 0.43 | 2.21 | 0.027 | 0.176 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.93 | 0.46 | 2.01 | 0.045 | 0.204 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.19 | 0.43 | 0.44 | 0.662 | 0.961 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 1.22 | 0.43 | 2.82 | 0.005 | 0.047 | * |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 1.20 | 0.46 | 2.58 | 0.010 | 0.085 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 1.03 | 0.43 | 2.39 | 0.017 | 0.126 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 1.01 | 0.46 | 2.18 | 0.029 | 0.176 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -0.02 | 0.46 | -0.05 | 0.963 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.26, *p* = 0.071, η²_G = 0.067
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -1.26 | 18 | = 0.374 | -0.35 [-0.54, 0.31] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -2.04 | 18 | = 0.187 | -0.46 [-0.57, 0.28] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.39 | 18 | = 0.701 | 0.10 [-0.10, 0.77] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 1.12 | 18 | = 0.398 | 0.32 [-0.23, 0.75] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.53 | 18 | = 0.668 | -0.13 [-0.45, 0.40] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 1.67 | 18 | = 0.225 | 0.39 [-0.02, 0.86] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.73 | 18 | = 0.225 | 0.54 [-0.10, 0.90] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 2.06 | 18 | = 0.187 | 0.49 [0.07, 0.96] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 2.35 | 18 | = 0.187 | 0.61 [0.02, 1.05] | medium | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.70 | 18 | = 0.618 | 0.22 [-0.33, 0.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 970.25, BIC = 992.21
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.54, *SE* = 3.669, *z* = 0.147, *p* = 0.883
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.40, *SE* = 3.877, *z* = -0.104, *p* = 0.917
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.07, *SE* = 3.853, *z* = -0.019, *p* = 0.985
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 3.67, *SE* = 4.395, *z* = 0.836, *p* = 0.403
- **SNR**: *β* = 0.03, *SE* = 0.357, *z* = 0.071, *p* = 0.943

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.54 | 3.67 | -0.15 | 0.883 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.40 | 3.88 | 0.10 | 0.917 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.07 | 3.85 | 0.02 | 0.985 | 1.000 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -3.68 | 4.39 | -0.84 | 0.403 | 0.984 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.94 | 3.72 | 0.25 | 0.801 | 1.000 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.61 | 3.71 | 0.17 | 0.869 | 1.000 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -3.14 | 4.18 | -0.75 | 0.453 | 0.985 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.33 | 3.63 | -0.09 | 0.928 | 1.000 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -4.08 | 3.96 | -1.03 | 0.303 | 0.973 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -3.75 | 3.97 | -0.94 | 0.345 | 0.978 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.52, *p* = 0.719, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.38 | 18 | = 0.885 | -0.08 [-0.45, 0.39] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.60 | 18 | = 0.870 | 0.14 [-0.40, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.11 | 18 | = 0.911 | -0.02 [-0.41, 0.43] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.69 | 18 | = 0.870 | -0.17 [-0.64, 0.33] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 1.56 | 18 | = 0.870 | 0.21 [-0.35, 0.49] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.24 | 18 | = 0.899 | 0.05 [-0.39, 0.46] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.52 | 18 | = 0.870 | -0.09 [-0.60, 0.36] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.57 | 18 | = 0.870 | -0.15 [-0.44, 0.41] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.33 | 18 | = 0.870 | -0.29 [-0.80, 0.19] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.63 | 18 | = 0.870 | -0.14 [-0.63, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 468.25, BIC = 490.21
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.34, *SE* = 0.419, *z* = 0.814, *p* = 0.415
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.48, *SE* = 0.443, *z* = -1.084, *p* = 0.278
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.57, *SE* = 0.441, *z* = -1.302, *p* = 0.193
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.50, *SE* = 0.503, *z* = -2.984, *p* = 0.003
- **SNR**: *β* = -0.23, *SE* = 0.041, *z* = -5.501, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.34 | 0.42 | -0.81 | 0.415 | 0.658 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.48 | 0.44 | 1.08 | 0.278 | 0.624 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.57 | 0.44 | 1.30 | 0.193 | 0.576 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 1.50 | 0.50 | 2.98 | 0.003 | 0.025 | * |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.82 | 0.43 | 1.93 | 0.053 | 0.240 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.91 | 0.42 | 2.16 | 0.031 | 0.197 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 1.84 | 0.48 | 3.86 | < .001 | 0.001 | ** |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.09 | 0.41 | 0.22 | 0.823 | 0.823 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 1.02 | 0.45 | 2.25 | 0.024 | 0.178 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.93 | 0.45 | 2.04 | 0.041 | 0.223 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.01, *p* = 0.410, η²_G = 0.020
- Greenhouse-Geisser corrected: *p* = 0.394 (ε = 0.697)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -2.36 | 18 | = 0.275 | -0.26 [-1.03, -0.11] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.62 | 18 | = 0.746 | -0.15 [-0.59, 0.26] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.33 | 18 | = 0.746 | 0.06 [-0.55, 0.30] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.74 | 18 | = 0.746 | 0.16 [-0.32, 0.65] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.34 | 18 | = 0.746 | 0.09 [-0.31, 0.54] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 1.27 | 18 | = 0.688 | 0.28 [-0.24, 0.61] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 2.05 | 18 | = 0.275 | 0.39 [-0.04, 0.98] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.97 | 18 | = 0.688 | 0.19 [-0.37, 0.48] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 1.12 | 18 | = 0.688 | 0.29 [-0.23, 0.75] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.36 | 18 | = 0.746 | 0.09 [-0.40, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 780.04, BIC = 802.00
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.99, *SE* = 1.589, *z* = 0.625, *p* = 0.532
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.69, *SE* = 1.625, *z* = -1.041, *p* = 0.298
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.02, *SE* = 1.604, *z* = -0.010, *p* = 0.992
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.76, *SE* = 1.790, *z* = -0.422, *p* = 0.673
- **SNR**: *β* = -0.02, *SE* = 0.361, *z* = -0.067, *p* = 0.946

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.99 | 1.59 | -0.62 | 0.532 | 0.989 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 1.69 | 1.62 | 1.04 | 0.298 | 0.955 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.02 | 1.60 | 0.01 | 0.992 | 0.992 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.76 | 1.79 | 0.42 | 0.673 | 0.989 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 2.68 | 1.60 | 1.67 | 0.094 | 0.629 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 1.01 | 1.59 | 0.63 | 0.526 | 0.989 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 1.75 | 1.76 | 0.99 | 0.320 | 0.955 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -1.67 | 1.59 | -1.05 | 0.292 | 0.955 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -0.93 | 1.72 | -0.54 | 0.586 | 0.989 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.74 | 1.73 | 0.43 | 0.669 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.27, *p* = 0.895, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.806 (ε = 0.613)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.89 | 18 | = 0.915 | -0.12 [-0.63, 0.22] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.30 | 18 | = 0.915 | 0.07 [-0.24, 0.62] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.55 | 18 | = 0.915 | -0.07 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.10 | 18 | = 0.922 | 0.02 [-0.46, 0.50] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.70 | 18 | = 0.915 | 0.19 [-0.17, 0.69] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.35 | 18 | = 0.915 | 0.05 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 0.60 | 18 | = 0.915 | 0.15 [-0.35, 0.62] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.65 | 18 | = 0.915 | -0.15 [-0.62, 0.23] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.23 | 18 | = 0.915 | -0.05 [-0.53, 0.43] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.52 | 18 | = 0.915 | 0.10 [-0.36, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 517.20, BIC = 539.15
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.23, *SE* = 0.539, *z* = -0.420, *p* = 0.675
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.10, *SE* = 0.551, *z* = 0.172, *p* = 0.863
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.65, *SE* = 0.544, *z* = 1.187, *p* = 0.235
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.56, *SE* = 0.605, *z* = 2.572, *p* = 0.010
- **SNR**: *β* = 0.14, *SE* = 0.121, *z* = 1.110, *p* = 0.267

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.23 | 0.54 | 0.42 | 0.675 | 0.912 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.09 | 0.55 | -0.17 | 0.863 | 0.912 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.65 | 0.54 | -1.19 | 0.235 | 0.738 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -1.56 | 0.60 | -2.57 | 0.010 | 0.087 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.32 | 0.54 | -0.59 | 0.555 | 0.912 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.87 | 0.54 | -1.62 | 0.106 | 0.544 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -1.78 | 0.59 | -3.00 | 0.003 | 0.027 | * |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.55 | 0.54 | -1.02 | 0.306 | 0.769 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -1.46 | 0.58 | -2.52 | 0.012 | 0.091 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -0.91 | 0.59 | -1.55 | 0.120 | 0.544 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.94, *p* = 0.113, η²_G = 0.054
- Greenhouse-Geisser corrected: *p* = 0.165 (ε = 0.439)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.84 | 18 | = 0.557 | 0.13 [-0.21, 0.64] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.04 | 18 | = 0.971 | 0.01 [-0.39, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.89 | 18 | = 0.557 | -0.18 [-0.74, 0.12] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.61 | 18 | = 0.426 | -0.45 [-0.87, 0.13] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.59 | 18 | = 0.627 | -0.13 [-0.56, 0.29] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.35 | 18 | = 0.483 | -0.28 [-0.84, 0.04] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -1.80 | 18 | = 0.426 | -0.52 [-0.92, 0.09] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.78 | 18 | = 0.557 | -0.18 [-0.72, 0.14] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.60 | 18 | = 0.426 | -0.46 [-0.86, 0.13] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -1.01 | 18 | = 0.557 | -0.31 [-0.72, 0.26] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1113.46, BIC = 1135.42
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.01, *SE* = 6.940, *z* = -0.146, *p* = 0.884
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 4.47, *SE* = 6.944, *z* = 0.644, *p* = 0.520
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 3.64, *SE* = 7.051, *z* = 0.516, *p* = 0.606
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 10.60, *SE* = 8.011, *z* = 1.323, *p* = 0.186
- **SNR**: *β* = -0.36, *SE* = 0.667, *z* = -0.544, *p* = 0.587

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 1.01 | 6.94 | 0.15 | 0.884 | 0.987 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -4.47 | 6.94 | -0.64 | 0.520 | 0.981 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -3.64 | 7.05 | -0.52 | 0.606 | 0.981 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -10.60 | 8.01 | -1.32 | 0.186 | 0.843 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -5.48 | 6.96 | -0.79 | 0.431 | 0.981 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -4.65 | 7.11 | -0.65 | 0.513 | 0.981 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -11.61 | 8.12 | -1.43 | 0.152 | 0.809 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.83 | 6.99 | 0.12 | 0.905 | 0.987 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -6.13 | 7.89 | -0.78 | 0.437 | 0.981 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -6.96 | 7.64 | -0.91 | 0.362 | 0.973 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.80, *p* = 0.531, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.43 | 18 | = 0.824 | 0.07 [-0.38, 0.47] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.33 | 18 | = 0.824 | -0.09 [-0.56, 0.29] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.59 | 18 | = 0.805 | -0.14 [-0.56, 0.29] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.15 | 18 | = 0.786 | -0.34 [-0.75, 0.23] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.78 | 18 | = 0.786 | -0.16 [-0.64, 0.22] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.74 | 18 | = 0.786 | -0.20 [-0.56, 0.29] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -1.53 | 18 | = 0.786 | -0.39 [-0.85, 0.15] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.16 | 18 | = 0.878 | -0.05 [-0.41, 0.43] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.20 | 18 | = 0.786 | -0.26 [-0.77, 0.21] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.83 | 18 | = 0.786 | -0.20 [-0.68, 0.30] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 567.83, BIC = 589.78
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.11, *SE* = 0.597, *z* = 0.183, *p* = 0.855
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.31, *SE* = 0.597, *z* = 0.519, *p* = 0.604
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.74, *SE* = 0.607, *z* = 1.212, *p* = 0.225
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.02, *SE* = 0.700, *z* = -0.029, *p* = 0.977
- **SNR**: *β* = 0.17, *SE* = 0.061, *z* = 2.706, *p* = 0.007

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.11 | 0.60 | -0.18 | 0.855 | 0.997 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.31 | 0.60 | -0.52 | 0.604 | 0.996 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.74 | 0.61 | -1.21 | 0.225 | 0.922 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.02 | 0.70 | 0.03 | 0.977 | 0.997 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.20 | 0.60 | -0.33 | 0.738 | 0.996 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.63 | 0.61 | -1.02 | 0.306 | 0.946 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.13 | 0.71 | 0.18 | 0.855 | 0.997 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.43 | 0.60 | -0.71 | 0.479 | 0.990 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.33 | 0.69 | 0.48 | 0.631 | 0.996 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.76 | 0.66 | 1.14 | 0.253 | 0.928 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.96, *p* = 0.435, η²_G = 0.015
- Greenhouse-Geisser corrected: *p* = 0.379 (ε = 0.409)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -1.27 | 18 | = 0.682 | -0.12 [-0.55, 0.30] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.37 | 18 | = 0.739 | -0.05 [-0.53, 0.31] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.43 | 18 | = 0.682 | -0.16 [-0.65, 0.20] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.85 | 18 | = 0.682 | 0.18 [-0.29, 0.68] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.42 | 18 | = 0.739 | 0.06 [-0.44, 0.40] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.34 | 18 | = 0.739 | -0.03 [-0.56, 0.28] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.07 | 18 | = 0.682 | 0.27 [-0.24, 0.73] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.59 | 18 | = 0.739 | -0.09 [-0.50, 0.34] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.84 | 18 | = 0.682 | 0.21 [-0.29, 0.68] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 1.35 | 18 | = 0.682 | 0.30 [-0.18, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.071)

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
