# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:44:16

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
| 1 to 3 | 18 | 105.33 ms | 11.40 | 2.69 | [88.00, 116.00] |
| 2 to 3 | 10 | 106.80 ms | 11.48 | 3.63 | [88.00, 116.00] |
| 3 to 3 | 12 | 105.00 ms | 10.94 | 3.16 | [88.00, 116.00] |
| 4 to 3 | 12 | 97.33 ms | 10.70 | 3.09 | [88.00, 116.00] |
| 5 to 3 | 4 | 102.00 ms | 16.17 | 8.08 | [88.00, 116.00] |
| 6 to 3 | 8 | 103.00 ms | 10.64 | 3.76 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 18 | 2.70 µV | 1.99 | 0.47 | [0.53, 7.33] |
| 2 to 3 | 10 | 2.42 µV | 1.70 | 0.54 | [0.52, 6.35] |
| 3 to 3 | 12 | 2.32 µV | 0.86 | 0.25 | [0.99, 3.69] |
| 4 to 3 | 12 | 2.49 µV | 1.32 | 0.38 | [0.44, 4.24] |
| 5 to 3 | 4 | 3.50 µV | 1.58 | 0.79 | [1.58, 5.34] |
| 6 to 3 | 8 | 1.76 µV | 0.31 | 0.11 | [1.44, 2.31] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 170.50 ms | 23.88 | 4.87 | [140.00, 216.00] |
| 2 to 3 | 21 | 169.14 ms | 18.51 | 4.04 | [140.00, 208.00] |
| 3 to 3 | 23 | 170.43 ms | 19.92 | 4.15 | [140.00, 216.00] |
| 4 to 3 | 23 | 176.35 ms | 20.43 | 4.26 | [152.00, 216.00] |
| 5 to 3 | 24 | 173.83 ms | 17.13 | 3.50 | [140.00, 208.00] |
| 6 to 3 | 23 | 175.30 ms | 15.89 | 3.31 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.33 µV | 2.66 | 0.54 | [-12.51, -2.34] |
| 2 to 3 | 21 | -5.65 µV | 1.80 | 0.39 | [-10.61, -2.59] |
| 3 to 3 | 23 | -5.17 µV | 1.99 | 0.42 | [-10.83, -1.55] |
| 4 to 3 | 23 | -6.41 µV | 2.27 | 0.47 | [-10.92, -1.44] |
| 5 to 3 | 24 | -6.05 µV | 2.71 | 0.55 | [-12.11, -1.76] |
| 6 to 3 | 23 | -6.61 µV | 2.36 | 0.49 | [-11.28, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 14 | 103.43 ms | 9.78 | 2.61 | [92.00, 116.00] |
| 2 to 3 | 12 | 105.67 ms | 10.01 | 2.89 | [92.00, 116.00] |
| 3 to 3 | 13 | 107.69 ms | 9.16 | 2.54 | [92.00, 116.00] |
| 4 to 3 | 12 | 103.67 ms | 8.77 | 2.53 | [92.00, 116.00] |
| 5 to 3 | 18 | 109.11 ms | 7.36 | 1.74 | [92.00, 116.00] |
| 6 to 3 | 14 | 106.00 ms | 7.65 | 2.04 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 14 | 2.69 µV | 1.97 | 0.53 | [0.62, 7.47] |
| 2 to 3 | 12 | 3.35 µV | 1.73 | 0.50 | [1.46, 6.87] |
| 3 to 3 | 13 | 3.42 µV | 2.33 | 0.65 | [0.79, 8.96] |
| 4 to 3 | 12 | 2.68 µV | 1.35 | 0.39 | [0.60, 5.30] |
| 5 to 3 | 18 | 2.90 µV | 1.15 | 0.27 | [0.79, 4.61] |
| 6 to 3 | 14 | 2.80 µV | 2.20 | 0.59 | [0.16, 7.81] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 455.00 ms | 38.54 | 8.62 | [392.00, 516.00] |
| 2 to 3 | 18 | 450.00 ms | 40.59 | 9.57 | [392.00, 528.00] |
| 3 to 3 | 15 | 440.00 ms | 37.55 | 9.70 | [392.00, 520.00] |
| 4 to 3 | 19 | 463.37 ms | 38.70 | 8.88 | [392.00, 528.00] |
| 5 to 3 | 19 | 459.37 ms | 29.79 | 6.83 | [392.00, 500.00] |
| 6 to 3 | 19 | 459.37 ms | 33.26 | 7.63 | [396.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 6.40 µV | 3.65 | 0.82 | [1.71, 14.25] |
| 2 to 3 | 18 | 6.51 µV | 3.27 | 0.77 | [1.82, 13.70] |
| 3 to 3 | 15 | 5.11 µV | 2.03 | 0.52 | [3.31, 9.60] |
| 4 to 3 | 19 | 6.19 µV | 2.92 | 0.67 | [1.17, 11.65] |
| 5 to 3 | 19 | 6.10 µV | 2.08 | 0.48 | [3.01, 10.28] |
| 6 to 3 | 19 | 7.03 µV | 2.89 | 0.66 | [3.79, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 502.22, BIC = 521.65
- **2 to 3 vs 1 to 3**: *β* = 0.74, *SE* = 4.108, *z* = 0.180, *p* = 0.857
- **3 to 3 vs 1 to 3**: *β* = 0.15, *SE* = 3.851, *z* = 0.040, *p* = 0.968
- **4 to 3 vs 1 to 3**: *β* = -7.21, *SE* = 3.831, *z* = -1.881, *p* = 0.060
- **5 to 3 vs 1 to 3**: *β* = -3.65, *SE* = 5.837, *z* = -0.625, *p* = 0.532
- **6 to 3 vs 1 to 3**: *β* = -1.43, *SE* = 4.428, *z* = -0.323, *p* = 0.747
- **SNR**: *β* = 1.39, *SE* = 1.124, *z* = 1.233, *p* = 0.218

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.74 | 4.11 | -0.18 | 0.857 | 1.000 | n.s. |
| 1 to 3 - 3 to 3 | -0.15 | 3.85 | -0.04 | 0.968 | 1.000 | n.s. |
| 1 to 3 - 4 to 3 | 7.21 | 3.83 | 1.88 | 0.060 | 0.604 | n.s. |
| 1 to 3 - 5 to 3 | 3.65 | 5.84 | 0.62 | 0.532 | 0.999 | n.s. |
| 1 to 3 - 6 to 3 | 1.43 | 4.43 | 0.32 | 0.747 | 1.000 | n.s. |
| 2 to 3 - 3 to 3 | 0.59 | 4.47 | 0.13 | 0.896 | 1.000 | n.s. |
| 2 to 3 - 4 to 3 | 7.94 | 4.55 | 1.74 | 0.081 | 0.694 | n.s. |
| 2 to 3 - 5 to 3 | 4.38 | 6.14 | 0.71 | 0.475 | 0.999 | n.s. |
| 2 to 3 - 6 to 3 | 2.17 | 5.02 | 0.43 | 0.666 | 1.000 | n.s. |
| 3 to 3 - 4 to 3 | 7.36 | 4.24 | 1.74 | 0.083 | 0.694 | n.s. |
| 3 to 3 - 5 to 3 | 3.80 | 6.05 | 0.63 | 0.530 | 0.999 | n.s. |
| 3 to 3 - 6 to 3 | 1.58 | 4.71 | 0.34 | 0.737 | 1.000 | n.s. |
| 4 to 3 - 5 to 3 | -3.56 | 6.13 | -0.58 | 0.561 | 0.999 | n.s. |
| 4 to 3 - 6 to 3 | -5.78 | 4.70 | -1.23 | 0.219 | 0.949 | n.s. |
| 5 to 3 - 6 to 3 | -2.22 | 6.46 | -0.34 | 0.732 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 213.61, BIC = 233.04
- **2 to 3 vs 1 to 3**: *β* = -0.35, *SE* = 0.407, *z* = -0.858, *p* = 0.391
- **3 to 3 vs 1 to 3**: *β* = -0.07, *SE* = 0.388, *z* = -0.174, *p* = 0.862
- **4 to 3 vs 1 to 3**: *β* = 0.08, *SE* = 0.382, *z* = 0.202, *p* = 0.840
- **5 to 3 vs 1 to 3**: *β* = 0.88, *SE* = 0.586, *z* = 1.508, *p* = 0.132
- **6 to 3 vs 1 to 3**: *β* = -0.68, *SE* = 0.447, *z* = -1.517, *p* = 0.129
- **SNR**: *β* = 0.70, *SE* = 0.113, *z* = 6.219, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.35 | 0.41 | 0.86 | 0.391 | 0.950 | n.s. |
| 1 to 3 - 3 to 3 | 0.07 | 0.39 | 0.17 | 0.862 | 0.982 | n.s. |
| 1 to 3 - 4 to 3 | -0.08 | 0.38 | -0.20 | 0.840 | 0.982 | n.s. |
| 1 to 3 - 5 to 3 | -0.88 | 0.59 | -1.51 | 0.132 | 0.782 | n.s. |
| 1 to 3 - 6 to 3 | 0.68 | 0.45 | 1.52 | 0.129 | 0.782 | n.s. |
| 2 to 3 - 3 to 3 | -0.28 | 0.45 | -0.63 | 0.529 | 0.972 | n.s. |
| 2 to 3 - 4 to 3 | -0.43 | 0.45 | -0.94 | 0.348 | 0.950 | n.s. |
| 2 to 3 - 5 to 3 | -1.23 | 0.62 | -2.00 | 0.046 | 0.482 | n.s. |
| 2 to 3 - 6 to 3 | 0.33 | 0.50 | 0.66 | 0.510 | 0.972 | n.s. |
| 3 to 3 - 4 to 3 | -0.14 | 0.43 | -0.34 | 0.736 | 0.982 | n.s. |
| 3 to 3 - 5 to 3 | -0.95 | 0.61 | -1.56 | 0.119 | 0.782 | n.s. |
| 3 to 3 - 6 to 3 | 0.61 | 0.47 | 1.29 | 0.197 | 0.849 | n.s. |
| 4 to 3 - 5 to 3 | -0.81 | 0.61 | -1.31 | 0.190 | 0.849 | n.s. |
| 4 to 3 - 6 to 3 | 0.75 | 0.47 | 1.60 | 0.111 | 0.782 | n.s. |
| 5 to 3 - 6 to 3 | 1.56 | 0.64 | 2.43 | 0.015 | 0.205 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1165.99, BIC = 1192.34
- **2 to 3 vs 1 to 3**: *β* = 2.77, *SE* = 3.912, *z* = 0.709, *p* = 0.478
- **3 to 3 vs 1 to 3**: *β* = 2.08, *SE* = 3.829, *z* = 0.542, *p* = 0.588
- **4 to 3 vs 1 to 3**: *β* = 5.76, *SE* = 3.753, *z* = 1.535, *p* = 0.125
- **5 to 3 vs 1 to 3**: *β* = 3.86, *SE* = 3.714, *z* = 1.039, *p* = 0.299
- **6 to 3 vs 1 to 3**: *β* = 6.16, *SE* = 3.750, *z* = 1.642, *p* = 0.101
- **SNR**: *β* = 0.84, *SE* = 0.493, *z* = 1.699, *p* = 0.089

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -2.77 | 3.91 | -0.71 | 0.478 | 0.995 | n.s. |
| 1 to 3 - 3 to 3 | -2.08 | 3.83 | -0.54 | 0.588 | 0.996 | n.s. |
| 1 to 3 - 4 to 3 | -5.76 | 3.75 | -1.53 | 0.125 | 0.845 | n.s. |
| 1 to 3 - 5 to 3 | -3.86 | 3.71 | -1.04 | 0.299 | 0.989 | n.s. |
| 1 to 3 - 6 to 3 | -6.16 | 3.75 | -1.64 | 0.101 | 0.796 | n.s. |
| 2 to 3 - 3 to 3 | 0.70 | 3.89 | 0.18 | 0.858 | 0.996 | n.s. |
| 2 to 3 - 4 to 3 | -2.98 | 3.93 | -0.76 | 0.448 | 0.995 | n.s. |
| 2 to 3 - 5 to 3 | -1.08 | 3.87 | -0.28 | 0.780 | 0.996 | n.s. |
| 2 to 3 - 6 to 3 | -3.38 | 3.93 | -0.86 | 0.389 | 0.993 | n.s. |
| 3 to 3 - 4 to 3 | -3.68 | 3.84 | -0.96 | 0.338 | 0.989 | n.s. |
| 3 to 3 - 5 to 3 | -1.78 | 3.78 | -0.47 | 0.637 | 0.996 | n.s. |
| 3 to 3 - 6 to 3 | -4.08 | 3.87 | -1.06 | 0.291 | 0.989 | n.s. |
| 4 to 3 - 5 to 3 | 1.90 | 3.75 | 0.51 | 0.612 | 0.996 | n.s. |
| 4 to 3 - 6 to 3 | -0.40 | 3.80 | -0.11 | 0.916 | 0.996 | n.s. |
| 5 to 3 - 6 to 3 | -2.30 | 3.76 | -0.61 | 0.541 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.451, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.63 | 19 | = 0.801 | -0.12 [-0.66, 0.26] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | -0.05 | 19 | = 0.962 | -0.01 [-0.47, 0.40] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | -1.25 | 19 | = 0.753 | -0.29 [-0.65, 0.22] | small | n.s. |
| 1 to 3 vs 5 to 3 | -0.99 | 19 | = 0.753 | -0.22 [-0.59, 0.26] | small | n.s. |
| 1 to 3 vs 6 to 3 | -1.57 | 19 | = 0.753 | -0.39 [-0.75, 0.14] | small | n.s. |
| 2 to 3 vs 3 to 3 | 0.44 | 19 | = 0.801 | 0.12 [-0.37, 0.54] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -0.73 | 19 | = 0.787 | -0.18 [-0.64, 0.31] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | -0.47 | 19 | = 0.801 | -0.10 [-0.58, 0.33] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -1.10 | 19 | = 0.753 | -0.28 [-0.70, 0.22] | small | n.s. |
| 3 to 3 vs 4 to 3 | -1.38 | 19 | = 0.753 | -0.30 [-0.69, 0.21] | small | n.s. |
| 3 to 3 vs 5 to 3 | -0.96 | 19 | = 0.753 | -0.23 [-0.58, 0.29] | small | n.s. |
| 3 to 3 vs 6 to 3 | -1.85 | 19 | = 0.753 | -0.41 [-0.78, 0.13] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.33 | 19 | = 0.801 | 0.09 [-0.32, 0.55] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.40 | 19 | = 0.801 | -0.08 [-0.50, 0.38] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.73 | 19 | = 0.787 | -0.19 [-0.61, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 566.26, BIC = 592.61
- **2 to 3 vs 1 to 3**: *β* = 0.38, *SE* = 0.475, *z* = 0.808, *p* = 0.419
- **3 to 3 vs 1 to 3**: *β* = 0.59, *SE* = 0.466, *z* = 1.259, *p* = 0.208
- **4 to 3 vs 1 to 3**: *β* = -0.27, *SE* = 0.458, *z* = -0.589, *p* = 0.556
- **5 to 3 vs 1 to 3**: *β* = 0.03, *SE* = 0.453, *z* = 0.071, *p* = 0.943
- **6 to 3 vs 1 to 3**: *β* = -0.28, *SE* = 0.457, *z* = -0.620, *p* = 0.535
- **SNR**: *β* = -0.40, *SE* = 0.058, *z* = -6.879, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.38 | 0.47 | -0.81 | 0.419 | 0.992 | n.s. |
| 1 to 3 - 3 to 3 | -0.59 | 0.47 | -1.26 | 0.208 | 0.923 | n.s. |
| 1 to 3 - 4 to 3 | 0.27 | 0.46 | 0.59 | 0.556 | 0.992 | n.s. |
| 1 to 3 - 5 to 3 | -0.03 | 0.45 | -0.07 | 0.943 | 0.997 | n.s. |
| 1 to 3 - 6 to 3 | 0.28 | 0.46 | 0.62 | 0.535 | 0.992 | n.s. |
| 2 to 3 - 3 to 3 | -0.20 | 0.47 | -0.43 | 0.669 | 0.992 | n.s. |
| 2 to 3 - 4 to 3 | 0.65 | 0.48 | 1.37 | 0.172 | 0.901 | n.s. |
| 2 to 3 - 5 to 3 | 0.35 | 0.47 | 0.75 | 0.456 | 0.992 | n.s. |
| 2 to 3 - 6 to 3 | 0.67 | 0.48 | 1.39 | 0.163 | 0.901 | n.s. |
| 3 to 3 - 4 to 3 | 0.86 | 0.47 | 1.83 | 0.067 | 0.633 | n.s. |
| 3 to 3 - 5 to 3 | 0.55 | 0.46 | 1.20 | 0.228 | 0.925 | n.s. |
| 3 to 3 - 6 to 3 | 0.87 | 0.47 | 1.85 | 0.065 | 0.633 | n.s. |
| 4 to 3 - 5 to 3 | -0.30 | 0.46 | -0.66 | 0.510 | 0.992 | n.s. |
| 4 to 3 - 6 to 3 | 0.01 | 0.46 | 0.03 | 0.976 | 0.997 | n.s. |
| 5 to 3 - 6 to 3 | 0.32 | 0.46 | 0.69 | 0.491 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.54, *p* = 0.034, η²_G = 0.065
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -3.04 | 19 | = 0.050 | -0.60 [-0.95, 0.01] | medium | n.s. |
| 1 to 3 vs 3 to 3 | -3.77 | 19 | = 0.019 | -0.67 [-1.16, -0.20] | medium | * |
| 1 to 3 vs 4 to 3 | -0.34 | 19 | = 0.790 | -0.08 [-0.44, 0.43] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.71 | 19 | = 0.725 | -0.22 [-0.50, 0.34] | small | n.s. |
| 1 to 3 vs 6 to 3 | -0.43 | 19 | = 0.776 | -0.10 [-0.35, 0.52] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | -0.62 | 19 | = 0.737 | -0.13 [-0.67, 0.25] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | 1.92 | 19 | = 0.176 | 0.58 [-0.06, 0.92] | medium | n.s. |
| 2 to 3 vs 5 to 3 | 1.20 | 19 | = 0.462 | 0.35 [-0.18, 0.75] | small | n.s. |
| 2 to 3 vs 6 to 3 | 2.04 | 19 | = 0.167 | 0.49 [-0.06, 0.89] | small | n.s. |
| 3 to 3 vs 4 to 3 | 2.43 | 19 | = 0.127 | 0.64 [0.02, 0.96] | medium | n.s. |
| 3 to 3 vs 5 to 3 | 1.57 | 19 | = 0.287 | 0.43 [-0.11, 0.78] | small | n.s. |
| 3 to 3 vs 6 to 3 | 2.10 | 19 | = 0.167 | 0.56 [0.05, 1.00] | medium | n.s. |
| 4 to 3 vs 5 to 3 | -0.72 | 19 | = 0.725 | -0.15 [-0.68, 0.20] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.11 | 19 | = 0.912 | -0.03 [-0.37, 0.52] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.50 | 19 | = 0.776 | 0.12 [-0.26, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 596.76, BIC = 618.53
- **2 to 3 vs 1 to 3**: *β* = 1.47, *SE* = 2.887, *z* = 0.507, *p* = 0.612
- **3 to 3 vs 1 to 3**: *β* = 3.22, *SE* = 2.796, *z* = 1.153, *p* = 0.249
- **4 to 3 vs 1 to 3**: *β* = -0.67, *SE* = 2.873, *z* = -0.234, *p* = 0.815
- **5 to 3 vs 1 to 3**: *β* = 4.96, *SE* = 2.593, *z* = 1.913, *p* = 0.056
- **6 to 3 vs 1 to 3**: *β* = 2.40, *SE* = 2.735, *z* = 0.879, *p* = 0.380
- **SNR**: *β* = 0.41, *SE* = 0.521, *z* = 0.781, *p* = 0.435

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -1.46 | 2.89 | -0.51 | 0.612 | 0.989 | n.s. |
| 1 to 3 - 3 to 3 | -3.22 | 2.80 | -1.15 | 0.249 | 0.957 | n.s. |
| 1 to 3 - 4 to 3 | 0.67 | 2.87 | 0.23 | 0.815 | 0.989 | n.s. |
| 1 to 3 - 5 to 3 | -4.96 | 2.59 | -1.91 | 0.056 | 0.552 | n.s. |
| 1 to 3 - 6 to 3 | -2.40 | 2.74 | -0.88 | 0.380 | 0.978 | n.s. |
| 2 to 3 - 3 to 3 | -1.76 | 2.93 | -0.60 | 0.548 | 0.989 | n.s. |
| 2 to 3 - 4 to 3 | 2.14 | 3.00 | 0.71 | 0.476 | 0.989 | n.s. |
| 2 to 3 - 5 to 3 | -3.50 | 2.71 | -1.29 | 0.198 | 0.929 | n.s. |
| 2 to 3 - 6 to 3 | -0.94 | 2.83 | -0.33 | 0.740 | 0.989 | n.s. |
| 3 to 3 - 4 to 3 | 3.90 | 2.92 | 1.34 | 0.182 | 0.926 | n.s. |
| 3 to 3 - 5 to 3 | -1.74 | 2.65 | -0.65 | 0.513 | 0.989 | n.s. |
| 3 to 3 - 6 to 3 | 0.82 | 2.80 | 0.29 | 0.770 | 0.989 | n.s. |
| 4 to 3 - 5 to 3 | -5.63 | 2.71 | -2.08 | 0.037 | 0.436 | n.s. |
| 4 to 3 - 6 to 3 | -3.08 | 2.88 | -1.07 | 0.285 | 0.965 | n.s. |
| 5 to 3 - 6 to 3 | 2.56 | 2.62 | 0.97 | 0.330 | 0.973 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.15, *p* = 0.142, η²_G = 0.164
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -1.73 | 2 | = 0.483 | -0.59 [-0.98, 0.87] | medium | n.s. |
| 1 to 3 vs 3 to 3 | -2.00 | 2 | = 0.483 | -0.35 [-1.20, 0.40] | small | n.s. |
| 1 to 3 vs 4 to 3 | 0.76 | 2 | = 0.610 | 0.44 [-0.73, 0.95] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.00 | 2 | = 1.000 | 0.00 [-1.00, 0.31] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -1.00 | 2 | = 0.610 | -0.41 [-0.99, 0.46] | small | n.s. |
| 2 to 3 vs 3 to 3 | 1.00 | 2 | = 0.610 | 0.23 [-0.88, 0.97] | small | n.s. |
| 2 to 3 vs 4 to 3 | 5.00 | 2 | = 0.429 | 1.83 [-0.86, 0.99] | large | n.s. |
| 2 to 3 vs 5 to 3 | 1.73 | 2 | = 0.483 | 0.59 [-1.38, 0.09] | medium | n.s. |
| 2 to 3 vs 6 to 3 | 1.00 | 2 | = 0.610 | 0.31 [-0.63, 0.81] | small | n.s. |
| 3 to 3 vs 4 to 3 | 2.00 | 2 | = 0.483 | 1.03 [-0.47, 1.26] | large | n.s. |
| 3 to 3 vs 5 to 3 | 2.00 | 2 | = 0.483 | 0.35 [-0.87, 0.48] | small | n.s. |
| 3 to 3 vs 6 to 3 | 0.00 | 2 | = 1.000 | 0.00 [-0.77, 0.77] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -0.76 | 2 | = 0.610 | -0.44 [-1.48, 0.11] | small | n.s. |
| 4 to 3 vs 6 to 3 | -4.00 | 2 | = 0.429 | -1.63 [-0.98, 0.57] | large | n.s. |
| 5 to 3 vs 6 to 3 | -0.76 | 2 | = 0.610 | -0.41 [-0.55, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.82, BIC = 319.59
- **2 to 3 vs 1 to 3**: *β* = 0.64, *SE* = 0.462, *z* = 1.390, *p* = 0.164
- **3 to 3 vs 1 to 3**: *β* = 0.79, *SE* = 0.446, *z* = 1.770, *p* = 0.077
- **4 to 3 vs 1 to 3**: *β* = -0.18, *SE* = 0.459, *z* = -0.388, *p* = 0.698
- **5 to 3 vs 1 to 3**: *β* = -0.10, *SE* = 0.414, *z* = -0.243, *p* = 0.808
- **6 to 3 vs 1 to 3**: *β* = 0.49, *SE* = 0.438, *z* = 1.130, *p* = 0.258
- **SNR**: *β* = 0.59, *SE* = 0.084, *z* = 7.048, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.64 | 0.46 | -1.39 | 0.164 | 0.792 | n.s. |
| 1 to 3 - 3 to 3 | -0.79 | 0.45 | -1.77 | 0.077 | 0.646 | n.s. |
| 1 to 3 - 4 to 3 | 0.18 | 0.46 | 0.39 | 0.698 | 0.997 | n.s. |
| 1 to 3 - 5 to 3 | 0.10 | 0.41 | 0.24 | 0.808 | 0.997 | n.s. |
| 1 to 3 - 6 to 3 | -0.50 | 0.44 | -1.13 | 0.258 | 0.877 | n.s. |
| 2 to 3 - 3 to 3 | -0.15 | 0.47 | -0.31 | 0.755 | 0.997 | n.s. |
| 2 to 3 - 4 to 3 | 0.82 | 0.48 | 1.71 | 0.088 | 0.663 | n.s. |
| 2 to 3 - 5 to 3 | 0.74 | 0.43 | 1.71 | 0.087 | 0.663 | n.s. |
| 2 to 3 - 6 to 3 | 0.15 | 0.45 | 0.33 | 0.744 | 0.997 | n.s. |
| 3 to 3 - 4 to 3 | 0.97 | 0.47 | 2.07 | 0.038 | 0.423 | n.s. |
| 3 to 3 - 5 to 3 | 0.89 | 0.42 | 2.10 | 0.036 | 0.422 | n.s. |
| 3 to 3 - 6 to 3 | 0.29 | 0.45 | 0.66 | 0.511 | 0.986 | n.s. |
| 4 to 3 - 5 to 3 | -0.08 | 0.43 | -0.18 | 0.858 | 0.997 | n.s. |
| 4 to 3 - 6 to 3 | -0.67 | 0.46 | -1.46 | 0.145 | 0.792 | n.s. |
| 5 to 3 - 6 to 3 | -0.60 | 0.42 | -1.42 | 0.156 | 0.792 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.542, η²_G = 0.217
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 2.41 | 2 | = 0.813 | 1.87 [-0.92, 0.93] | large | n.s. |
| 1 to 3 vs 3 to 3 | 0.67 | 2 | = 0.813 | 0.25 [-1.29, 0.33] | small | n.s. |
| 1 to 3 vs 4 to 3 | 1.16 | 2 | = 0.813 | 0.80 [-0.34, 1.45] | large | n.s. |
| 1 to 3 vs 5 to 3 | 0.99 | 2 | = 0.813 | 1.05 [-0.98, 0.32] | large | n.s. |
| 1 to 3 vs 6 to 3 | -0.05 | 2 | = 0.961 | -0.01 [-0.89, 0.55] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | -0.80 | 2 | = 0.813 | -0.63 [-1.35, 0.57] | medium | n.s. |
| 2 to 3 vs 4 to 3 | -1.64 | 2 | = 0.813 | -1.11 [-1.01, 0.84] | large | n.s. |
| 2 to 3 vs 5 to 3 | -1.48 | 2 | = 0.813 | -1.15 [-0.37, 1.01] | large | n.s. |
| 2 to 3 vs 6 to 3 | -2.04 | 2 | = 0.813 | -1.67 [-0.68, 0.75] | large | n.s. |
| 3 to 3 vs 4 to 3 | 0.28 | 2 | = 0.866 | 0.20 [-0.57, 1.14] | negligible | n.s. |
| 3 to 3 vs 5 to 3 | 0.31 | 2 | = 0.866 | 0.30 [-0.58, 0.77] | small | n.s. |
| 3 to 3 vs 6 to 3 | -0.62 | 2 | = 0.813 | -0.25 [-0.65, 0.90] | small | n.s. |
| 4 to 3 vs 5 to 3 | 0.30 | 2 | = 0.866 | 0.20 [-0.61, 0.83] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.87 | 2 | = 0.813 | -0.75 [-0.85, 0.69] | medium | n.s. |
| 5 to 3 vs 6 to 3 | -0.89 | 2 | = 0.813 | -0.97 [-0.81, 0.47] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1114.41, BIC = 1138.71
- **2 to 3 vs 1 to 3**: *β* = -4.82, *SE* = 11.190, *z* = -0.431, *p* = 0.667
- **3 to 3 vs 1 to 3**: *β* = -14.27, *SE* = 11.954, *z* = -1.194, *p* = 0.233
- **4 to 3 vs 1 to 3**: *β* = 8.79, *SE* = 11.030, *z* = 0.797, *p* = 0.426
- **5 to 3 vs 1 to 3**: *β* = 4.40, *SE* = 11.050, *z* = 0.398, *p* = 0.690
- **6 to 3 vs 1 to 3**: *β* = 4.32, *SE* = 11.010, *z* = 0.392, *p* = 0.695
- **SNR**: *β* = 0.46, *SE* = 1.078, *z* = 0.424, *p* = 0.672

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 4.82 | 11.19 | 0.43 | 0.667 | 0.999 | n.s. |
| 1 to 3 - 3 to 3 | 14.27 | 11.95 | 1.19 | 0.233 | 0.957 | n.s. |
| 1 to 3 - 4 to 3 | -8.79 | 11.03 | -0.80 | 0.426 | 0.995 | n.s. |
| 1 to 3 - 5 to 3 | -4.40 | 11.05 | -0.40 | 0.690 | 0.999 | n.s. |
| 1 to 3 - 6 to 3 | -4.32 | 11.01 | -0.39 | 0.695 | 0.999 | n.s. |
| 2 to 3 - 3 to 3 | 9.45 | 12.24 | 0.77 | 0.440 | 0.995 | n.s. |
| 2 to 3 - 4 to 3 | -13.61 | 11.36 | -1.20 | 0.231 | 0.957 | n.s. |
| 2 to 3 - 5 to 3 | -9.22 | 11.33 | -0.81 | 0.416 | 0.995 | n.s. |
| 2 to 3 - 6 to 3 | -9.14 | 11.32 | -0.81 | 0.420 | 0.995 | n.s. |
| 3 to 3 - 4 to 3 | -23.06 | 12.12 | -1.90 | 0.057 | 0.587 | n.s. |
| 3 to 3 - 5 to 3 | -18.67 | 11.99 | -1.56 | 0.120 | 0.832 | n.s. |
| 3 to 3 - 6 to 3 | -18.59 | 12.05 | -1.54 | 0.123 | 0.832 | n.s. |
| 4 to 3 - 5 to 3 | 4.39 | 11.23 | 0.39 | 0.696 | 0.999 | n.s. |
| 4 to 3 - 6 to 3 | 4.47 | 11.18 | 0.40 | 0.689 | 0.999 | n.s. |
| 5 to 3 - 6 to 3 | 0.08 | 11.17 | 0.01 | 0.994 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.64, *p* = 0.671, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.13 | 10 | = 0.967 | -0.07 [-0.49, 0.54] | negligible | n.s. |
| 1 to 3 vs 3 to 3 | 0.88 | 10 | = 0.967 | 0.42 [-0.32, 0.81] | small | n.s. |
| 1 to 3 vs 4 to 3 | -0.39 | 10 | = 0.967 | -0.18 [-0.68, 0.33] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.16 | 10 | = 0.967 | -0.07 [-0.47, 0.52] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.30 | 10 | = 0.967 | -0.15 [-0.58, 0.39] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 1.28 | 10 | = 0.863 | 0.50 [-0.40, 0.82] | small | n.s. |
| 2 to 3 vs 4 to 3 | -0.40 | 10 | = 0.967 | -0.13 [-0.69, 0.42] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | 0.00 | 10 | = 1.000 | 0.00 [-0.67, 0.33] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.24 | 10 | = 0.967 | -0.08 [-0.60, 0.43] | negligible | n.s. |
| 3 to 3 vs 4 to 3 | -1.42 | 10 | = 0.863 | -0.58 [-1.04, 0.21] | medium | n.s. |
| 3 to 3 vs 5 to 3 | -1.32 | 10 | = 0.863 | -0.54 [-1.07, 0.14] | medium | n.s. |
| 3 to 3 vs 6 to 3 | -1.77 | 10 | = 0.863 | -0.65 [-1.23, -0.02] | medium | n.s. |
| 4 to 3 vs 5 to 3 | 0.30 | 10 | = 0.967 | 0.14 [-0.31, 0.77] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.21 | 10 | = 0.967 | 0.07 [-0.26, 0.79] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.19 | 10 | = 0.967 | -0.09 [-0.58, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 471.07, BIC = 495.37
- **2 to 3 vs 1 to 3**: *β* = 0.04, *SE* = 0.522, *z* = 0.081, *p* = 0.936
- **3 to 3 vs 1 to 3**: *β* = -0.51, *SE* = 0.561, *z* = -0.904, *p* = 0.366
- **4 to 3 vs 1 to 3**: *β* = -0.20, *SE* = 0.512, *z* = -0.387, *p* = 0.699
- **5 to 3 vs 1 to 3**: *β* = -0.15, *SE* = 0.515, *z* = -0.299, *p* = 0.765
- **6 to 3 vs 1 to 3**: *β* = 0.57, *SE* = 0.509, *z* = 1.127, *p* = 0.260
- **SNR**: *β* = 0.41, *SE* = 0.057, *z* = 7.155, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.04 | 0.52 | -0.08 | 0.936 | 0.998 | n.s. |
| 1 to 3 - 3 to 3 | 0.51 | 0.56 | 0.90 | 0.366 | 0.984 | n.s. |
| 1 to 3 - 4 to 3 | 0.20 | 0.51 | 0.39 | 0.699 | 0.998 | n.s. |
| 1 to 3 - 5 to 3 | 0.15 | 0.51 | 0.30 | 0.765 | 0.998 | n.s. |
| 1 to 3 - 6 to 3 | -0.57 | 0.51 | -1.13 | 0.260 | 0.973 | n.s. |
| 2 to 3 - 3 to 3 | 0.55 | 0.57 | 0.96 | 0.338 | 0.984 | n.s. |
| 2 to 3 - 4 to 3 | 0.24 | 0.54 | 0.45 | 0.653 | 0.998 | n.s. |
| 2 to 3 - 5 to 3 | 0.20 | 0.52 | 0.38 | 0.707 | 0.998 | n.s. |
| 2 to 3 - 6 to 3 | -0.53 | 0.53 | -1.01 | 0.312 | 0.984 | n.s. |
| 3 to 3 - 4 to 3 | -0.31 | 0.58 | -0.54 | 0.591 | 0.998 | n.s. |
| 3 to 3 - 5 to 3 | -0.35 | 0.56 | -0.63 | 0.529 | 0.998 | n.s. |
| 3 to 3 - 6 to 3 | -1.08 | 0.56 | -1.92 | 0.054 | 0.568 | n.s. |
| 4 to 3 - 5 to 3 | -0.04 | 0.53 | -0.08 | 0.933 | 0.998 | n.s. |
| 4 to 3 - 6 to 3 | -0.77 | 0.52 | -1.48 | 0.139 | 0.877 | n.s. |
| 5 to 3 - 6 to 3 | -0.73 | 0.52 | -1.41 | 0.160 | 0.896 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.07, *p* = 0.084, η²_G = 0.069
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.93 | 10 | = 0.921 | 0.21 [-0.44, 0.59] | small | n.s. |
| 1 to 3 vs 3 to 3 | 2.34 | 10 | = 0.217 | 0.75 [-0.23, 0.91] | medium | n.s. |
| 1 to 3 vs 4 to 3 | 0.78 | 10 | = 0.921 | 0.17 [-0.31, 0.70] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | 0.59 | 10 | = 0.921 | 0.20 [-0.37, 0.63] | small | n.s. |
| 1 to 3 vs 6 to 3 | 0.57 | 10 | = 0.921 | 0.10 [-0.68, 0.29] | negligible | n.s. |
| 2 to 3 vs 3 to 3 | 1.93 | 10 | = 0.248 | 0.62 [-0.24, 1.01] | medium | n.s. |
| 2 to 3 vs 4 to 3 | -0.25 | 10 | = 0.921 | -0.06 [-0.65, 0.46] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | -0.18 | 10 | = 0.921 | -0.04 [-0.30, 0.70] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.51 | 10 | = 0.921 | -0.12 [-0.83, 0.22] | negligible | n.s. |
| 3 to 3 vs 4 to 3 | -2.39 | 10 | = 0.217 | -0.79 [-1.45, -0.08] | medium | n.s. |
| 3 to 3 vs 5 to 3 | -2.31 | 10 | = 0.217 | -0.88 [-1.20, 0.05] | large | n.s. |
| 3 to 3 vs 6 to 3 | -2.08 | 10 | = 0.242 | -0.75 [-1.09, 0.08] | medium | n.s. |
| 4 to 3 vs 5 to 3 | 0.10 | 10 | = 0.921 | 0.03 [-0.31, 0.77] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.28 | 10 | = 0.921 | -0.08 [-0.67, 0.36] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.30 | 10 | = 0.921 | -0.11 [-0.82, 0.20] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.034). Post-hoc tests revealed:
  - 1 to 3 showed smaller amplitude than 3 to 3 (*d* = -0.67)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.084)

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
