# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:59:42

---

## 1. Analysis Overview

**Total Measurements:** 360
**Number of Subjects:** 24
**Number of Conditions:** 5

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | -3.36 µV | 1.69 | 0.34 | [-7.51, -0.18] |
| b | 23 | -3.63 µV | 1.96 | 0.41 | [-9.16, -0.67] |
| c | 23 | -3.08 µV | 1.52 | 0.32 | [-6.62, -0.12] |
| d | 24 | -3.43 µV | 1.59 | 0.33 | [-7.06, -0.08] |
| e | 24 | -3.85 µV | 1.94 | 0.40 | [-9.14, -0.41] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 176.07 ms | 9.95 | 2.03 | [157.64, 206.76] |
| b | 23 | 175.24 ms | 9.16 | 1.91 | [158.99, 201.74] |
| c | 23 | 176.21 ms | 9.53 | 1.99 | [155.13, 200.42] |
| d | 24 | 176.08 ms | 10.13 | 2.07 | [161.57, 207.12] |
| e | 24 | 175.77 ms | 9.46 | 1.93 | [159.89, 204.87] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 13 | 1.53 µV | 1.32 | 0.36 | [0.12, 4.69] |
| b | 16 | 1.29 µV | 1.31 | 0.33 | [-0.01, 4.56] |
| c | 16 | 1.82 µV | 1.49 | 0.37 | [0.27, 6.21] |
| d | 11 | 1.28 µV | 1.27 | 0.38 | [0.11, 4.00] |
| e | 15 | 1.15 µV | 0.99 | 0.25 | [-0.02, 3.22] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 13 | 105.72 ms | 4.45 | 1.24 | [98.06, 112.34] |
| b | 16 | 106.19 ms | 6.06 | 1.52 | [92.58, 115.14] |
| c | 16 | 103.94 ms | 3.25 | 0.81 | [96.72, 108.20] |
| d | 11 | 105.70 ms | 5.57 | 1.68 | [97.01, 113.22] |
| e | 15 | 105.06 ms | 4.34 | 1.12 | [97.69, 115.93] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 18 | 3.14 µV | 1.92 | 0.45 | [0.10, 5.95] |
| b | 17 | 4.11 µV | 2.53 | 0.61 | [0.34, 9.56] |
| c | 20 | 2.71 µV | 1.85 | 0.41 | [0.40, 5.86] |
| d | 19 | 2.96 µV | 2.16 | 0.50 | [0.22, 7.92] |
| e | 19 | 3.75 µV | 2.31 | 0.53 | [0.16, 7.90] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 18 | 475.37 ms | 11.42 | 2.69 | [445.32, 489.95] |
| b | 17 | 479.39 ms | 9.86 | 2.39 | [461.30, 497.98] |
| c | 20 | 475.06 ms | 14.01 | 3.13 | [443.04, 497.08] |
| d | 19 | 484.22 ms | 13.77 | 3.16 | [458.69, 517.49] |
| e | 19 | 482.56 ms | 14.27 | 3.27 | [458.82, 526.91] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 346.32, BIC = 368.48
- **b vs a**: *β* = 0.02, *SE* = 0.222, *z* = 0.103, *p* = 0.918
- **c vs a**: *β* = 0.48, *SE* = 0.220, *z* = 2.210, *p* = 0.027
- **d vs a**: *β* = 0.05, *SE* = 0.218, *z* = 0.214, *p* = 0.830
- **e vs a**: *β* = -0.15, *SE* = 0.227, *z* = -0.675, *p* = 0.499
- **SNR**: *β* = -0.09, *SE* = 0.018, *z* = -4.990, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.02 | 0.22 | -0.10 | 0.918 | 0.995 | n.s. |
| a - c | -0.49 | 0.22 | -2.21 | 0.027 | 0.219 | n.s. |
| a - d | -0.05 | 0.22 | -0.21 | 0.830 | 0.995 | n.s. |
| a - e | 0.15 | 0.23 | 0.68 | 0.499 | 0.938 | n.s. |
| b - c | -0.46 | 0.22 | -2.07 | 0.038 | 0.268 | n.s. |
| b - d | -0.02 | 0.22 | -0.11 | 0.914 | 0.995 | n.s. |
| b - e | 0.18 | 0.22 | 0.79 | 0.427 | 0.938 | n.s. |
| c - d | 0.44 | 0.22 | 2.00 | 0.046 | 0.279 | n.s. |
| c - e | 0.64 | 0.23 | 2.83 | 0.005 | 0.046 | * |
| d - e | 0.20 | 0.22 | 0.91 | 0.365 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.33, *p* = 0.014, η²_G = 0.034
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.67 | 21 | = 0.634 | 0.08 [-0.27, 0.60] | negligible | n.s. |
| a vs c | -1.79 | 21 | = 0.176 | -0.29 [-0.85, 0.05] | small | n.s. |
| a vs d | 0.31 | 21 | = 0.807 | 0.05 [-0.35, 0.50] | negligible | n.s. |
| a vs e | 1.73 | 21 | = 0.176 | 0.31 [-0.07, 0.81] | small | n.s. |
| b vs c | -2.09 | 21 | = 0.162 | -0.33 [-0.91, 0.02] | small | n.s. |
| b vs d | -0.25 | 21 | = 0.807 | -0.04 [-0.51, 0.36] | negligible | n.s. |
| b vs e | 1.43 | 21 | = 0.240 | 0.20 [-0.15, 0.73] | small | n.s. |
| c vs d | 2.13 | 21 | = 0.162 | 0.35 [0.02, 0.94] | small | n.s. |
| c vs e | 2.92 | 21 | = 0.082 | 0.58 [0.16, 1.11] | medium | n.s. |
| d vs e | 1.69 | 21 | = 0.176 | 0.28 [-0.08, 0.79] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 728.89, BIC = 751.05
- **b vs a**: *β* = -0.18, *SE* = 1.021, *z* = -0.178, *p* = 0.859
- **c vs a**: *β* = 1.37, *SE* = 1.010, *z* = 1.359, *p* = 0.174
- **d vs a**: *β* = 0.02, *SE* = 1.001, *z* = 0.020, *p* = 0.984
- **e vs a**: *β* = -0.28, *SE* = 1.041, *z* = -0.271, *p* = 0.786
- **SNR**: *β* = -0.00, *SE* = 0.080, *z* = -0.051, *p* = 0.960

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.18 | 1.02 | 0.18 | 0.859 | 1.000 | n.s. |
| a - c | -1.37 | 1.01 | -1.36 | 0.174 | 0.784 | n.s. |
| a - d | -0.02 | 1.00 | -0.02 | 0.984 | 1.000 | n.s. |
| a - e | 0.28 | 1.04 | 0.27 | 0.786 | 1.000 | n.s. |
| b - c | -1.55 | 1.03 | -1.52 | 0.130 | 0.714 | n.s. |
| b - d | -0.20 | 1.01 | -0.20 | 0.841 | 1.000 | n.s. |
| b - e | 0.10 | 1.02 | 0.10 | 0.922 | 1.000 | n.s. |
| c - d | 1.35 | 1.01 | 1.34 | 0.180 | 0.784 | n.s. |
| c - e | 1.66 | 1.04 | 1.60 | 0.110 | 0.689 | n.s. |
| d - e | 0.30 | 1.01 | 0.30 | 0.765 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.50, *p* = 0.736, η²_G = 0.004
- Greenhouse-Geisser corrected: *p* = 0.669 (ε = 0.691)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.28 | 21 | = 0.923 | 0.03 [-0.32, 0.55] | negligible | n.s. |
| a vs c | -0.69 | 21 | = 0.923 | -0.11 [-0.67, 0.20] | negligible | n.s. |
| a vs d | 0.22 | 21 | = 0.923 | 0.03 [-0.43, 0.42] | negligible | n.s. |
| a vs e | 0.85 | 21 | = 0.923 | 0.07 [-0.32, 0.52] | negligible | n.s. |
| b vs c | -0.90 | 21 | = 0.923 | -0.14 [-0.64, 0.26] | negligible | n.s. |
| b vs d | 0.01 | 21 | = 0.995 | 0.00 [-0.50, 0.37] | negligible | n.s. |
| b vs e | 0.29 | 21 | = 0.923 | 0.04 [-0.40, 0.46] | negligible | n.s. |
| c vs d | 0.84 | 21 | = 0.923 | 0.14 [-0.20, 0.68] | negligible | n.s. |
| c vs e | 1.23 | 21 | = 0.923 | 0.18 [-0.12, 0.77] | negligible | n.s. |
| d vs e | 0.24 | 21 | = 0.923 | 0.04 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 146.12, BIC = 164.22
- **b vs a**: *β* = -0.19, *SE* = 0.180, *z* = -1.038, *p* = 0.299
- **c vs a**: *β* = -0.10, *SE* = 0.185, *z* = -0.522, *p* = 0.602
- **d vs a**: *β* = -0.34, *SE* = 0.193, *z* = -1.768, *p* = 0.077
- **e vs a**: *β* = -0.38, *SE* = 0.178, *z* = -2.102, *p* = 0.036
- **SNR**: *β* = 0.17, *SE* = 0.020, *z* = 8.699, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.19 | 0.18 | 1.04 | 0.299 | 0.868 | n.s. |
| a - c | 0.10 | 0.19 | 0.52 | 0.602 | 0.935 | n.s. |
| a - d | 0.34 | 0.19 | 1.77 | 0.077 | 0.514 | n.s. |
| a - e | 0.37 | 0.18 | 2.10 | 0.036 | 0.304 | n.s. |
| b - c | -0.09 | 0.17 | -0.53 | 0.599 | 0.935 | n.s. |
| b - d | 0.16 | 0.19 | 0.80 | 0.424 | 0.890 | n.s. |
| b - e | 0.19 | 0.18 | 1.07 | 0.286 | 0.868 | n.s. |
| c - d | 0.25 | 0.20 | 1.23 | 0.219 | 0.823 | n.s. |
| c - e | 0.28 | 0.18 | 1.56 | 0.119 | 0.638 | n.s. |
| d - e | 0.03 | 0.19 | 0.17 | 0.863 | 0.935 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.160, η²_G = 0.090
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.10 | 5 | = 0.921 | 0.03 [-0.78, 0.56] | negligible | n.s. |
| a vs c | -1.39 | 5 | = 0.374 | -0.39 [-1.14, 0.20] | small | n.s. |
| a vs d | 1.96 | 5 | = 0.358 | 0.38 [-0.04, 1.77] | small | n.s. |
| a vs e | 0.76 | 5 | = 0.603 | 0.38 [-0.42, 0.95] | small | n.s. |
| b vs c | -1.44 | 5 | = 0.374 | -0.41 [-1.01, 0.19] | small | n.s. |
| b vs d | 2.41 | 5 | = 0.305 | 0.34 [-0.03, 2.02] | small | n.s. |
| b vs e | 0.97 | 5 | = 0.539 | 0.33 [-0.51, 0.93] | small | n.s. |
| c vs d | 2.68 | 5 | = 0.305 | 0.73 [0.08, 1.80] | medium | n.s. |
| c vs e | 1.46 | 5 | = 0.374 | 0.77 [-0.13, 1.24] | medium | n.s. |
| d vs e | -0.13 | 5 | = 0.921 | -0.06 [-0.85, 0.69] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 405.34, BIC = 423.44
- **b vs a**: *β* = 1.26, *SE* = 1.110, *z* = 1.137, *p* = 0.256
- **c vs a**: *β* = -1.29, *SE* = 1.133, *z* = -1.138, *p* = 0.255
- **d vs a**: *β* = 0.05, *SE* = 1.187, *z* = 0.044, *p* = 0.965
- **e vs a**: *β* = -0.45, *SE* = 1.096, *z* = -0.411, *p* = 0.681
- **SNR**: *β* = -0.03, *SE* = 0.117, *z* = -0.243, *p* = 0.808

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -1.26 | 1.11 | -1.14 | 0.256 | 0.905 | n.s. |
| a - c | 1.29 | 1.13 | 1.14 | 0.255 | 0.905 | n.s. |
| a - d | -0.05 | 1.19 | -0.04 | 0.965 | 0.965 | n.s. |
| a - e | 0.45 | 1.10 | 0.41 | 0.681 | 0.963 | n.s. |
| b - c | 2.55 | 1.05 | 2.43 | 0.015 | 0.141 | n.s. |
| b - d | 1.21 | 1.19 | 1.02 | 0.310 | 0.905 | n.s. |
| b - e | 1.71 | 1.09 | 1.57 | 0.117 | 0.675 | n.s. |
| c - d | -1.34 | 1.21 | -1.11 | 0.268 | 0.905 | n.s. |
| c - e | -0.84 | 1.10 | -0.77 | 0.444 | 0.905 | n.s. |
| d - e | 0.50 | 1.16 | 0.43 | 0.665 | 0.963 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.44, *p* = 0.258, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.62 | 5 | = 0.700 | -0.25 [-0.94, 0.42] | small | n.s. |
| a vs c | 2.16 | 5 | = 0.429 | 0.59 [-0.31, 0.99] | medium | n.s. |
| a vs d | -1.02 | 5 | = 0.611 | -0.31 [-0.97, 0.58] | small | n.s. |
| a vs e | -0.14 | 5 | = 0.897 | -0.05 [-0.59, 0.75] | negligible | n.s. |
| b vs c | 2.08 | 5 | = 0.429 | 0.85 [0.12, 1.44] | large | n.s. |
| b vs d | -0.34 | 5 | = 0.830 | -0.10 [-0.76, 0.92] | negligible | n.s. |
| b vs e | 0.97 | 5 | = 0.611 | 0.15 [-0.12, 1.47] | negligible | n.s. |
| c vs d | -1.82 | 5 | = 0.429 | -0.79 [-1.11, 0.37] | medium | n.s. |
| c vs e | -1.09 | 5 | = 0.611 | -0.48 [-0.81, 0.47] | small | n.s. |
| d vs e | 0.86 | 5 | = 0.611 | 0.22 [-0.73, 0.81] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 282.09, BIC = 302.35
- **b vs a**: *β* = 0.60, *SE* = 0.248, *z* = 2.429, *p* = 0.015
- **c vs a**: *β* = -0.28, *SE* = 0.235, *z* = -1.177, *p* = 0.239
- **d vs a**: *β* = -0.00, *SE* = 0.236, *z* = -0.001, *p* = 0.999
- **e vs a**: *β* = 0.44, *SE* = 0.244, *z* = 1.815, *p* = 0.070
- **SNR**: *β* = 0.09, *SE* = 0.019, *z* = 4.508, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.60 | 0.25 | -2.43 | 0.015 | 0.109 | n.s. |
| a - c | 0.28 | 0.23 | 1.18 | 0.239 | 0.655 | n.s. |
| a - d | 0.00 | 0.24 | 0.00 | 0.999 | 0.999 | n.s. |
| a - e | -0.44 | 0.24 | -1.81 | 0.070 | 0.351 | n.s. |
| b - c | 0.88 | 0.24 | 3.67 | < .001 | 0.002 | ** |
| b - d | 0.60 | 0.25 | 2.45 | 0.014 | 0.109 | n.s. |
| b - e | 0.16 | 0.24 | 0.66 | 0.510 | 0.760 | n.s. |
| c - d | -0.28 | 0.23 | -1.19 | 0.233 | 0.655 | n.s. |
| c - e | -0.72 | 0.23 | -3.08 | 0.002 | 0.019 | * |
| d - e | -0.44 | 0.25 | -1.81 | 0.071 | 0.351 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.44, *p* < .001, η²_G = 0.053
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -3.01 | 15 | = 0.022 | -0.42 [-1.35, -0.15] | small | * |
| a vs c | 1.12 | 15 | = 0.398 | 0.14 [-0.24, 0.77] | negligible | n.s. |
| a vs d | 0.05 | 15 | = 0.962 | 0.01 [-0.45, 0.55] | negligible | n.s. |
| a vs e | -2.54 | 15 | = 0.045 | -0.40 [-1.15, -0.07] | small | * |
| b vs c | 4.00 | 15 | = 0.011 | 0.55 [0.25, 1.45] | medium | * |
| b vs d | 3.17 | 15 | = 0.021 | 0.41 [0.16, 1.32] | small | * |
| b vs e | 0.27 | 15 | = 0.876 | 0.04 [-0.47, 0.60] | negligible | n.s. |
| c vs d | -1.03 | 15 | = 0.399 | -0.13 [-0.63, 0.34] | negligible | n.s. |
| c vs e | -3.67 | 15 | = 0.011 | -0.54 [-1.45, -0.31] | medium | * |
| d vs e | -2.44 | 15 | = 0.046 | -0.39 [-1.15, -0.07] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 738.25, BIC = 758.51
- **b vs a**: *β* = 3.90, *SE* = 3.536, *z* = 1.104, *p* = 0.269
- **c vs a**: *β* = -0.14, *SE* = 3.346, *z* = -0.042, *p* = 0.966
- **d vs a**: *β* = 8.31, *SE* = 3.378, *z* = 2.460, *p* = 0.014
- **e vs a**: *β* = 7.79, *SE* = 3.459, *z* = 2.252, *p* = 0.024
- **SNR**: *β* = 0.07, *SE* = 0.235, *z* = 0.289, *p* = 0.773

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -3.90 | 3.54 | -1.10 | 0.269 | 0.757 | n.s. |
| a - c | 0.14 | 3.35 | 0.04 | 0.966 | 0.986 | n.s. |
| a - d | -8.31 | 3.38 | -2.46 | 0.014 | 0.118 | n.s. |
| a - e | -7.79 | 3.46 | -2.25 | 0.024 | 0.158 | n.s. |
| b - c | 4.05 | 3.43 | 1.18 | 0.238 | 0.757 | n.s. |
| b - d | -4.40 | 3.52 | -1.25 | 0.210 | 0.757 | n.s. |
| b - e | -3.88 | 3.46 | -1.12 | 0.262 | 0.757 | n.s. |
| c - d | -8.45 | 3.31 | -2.56 | 0.011 | 0.101 | n.s. |
| c - e | -7.93 | 3.34 | -2.38 | 0.018 | 0.132 | n.s. |
| d - e | 0.52 | 3.47 | 0.15 | 0.881 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.130, η²_G = 0.046
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.54 | 15 | = 0.661 | -0.16 [-0.67, 0.40] | negligible | n.s. |
| a vs c | 0.30 | 15 | = 0.765 | 0.07 [-0.51, 0.48] | negligible | n.s. |
| a vs d | -1.18 | 15 | = 0.432 | -0.34 [-0.96, 0.08] | small | n.s. |
| a vs e | -1.52 | 15 | = 0.372 | -0.52 [-0.91, 0.12] | medium | n.s. |
| b vs c | 1.10 | 15 | = 0.432 | 0.23 [-0.25, 0.80] | small | n.s. |
| b vs d | -1.07 | 15 | = 0.432 | -0.18 [-0.76, 0.28] | negligible | n.s. |
| b vs e | -1.61 | 15 | = 0.372 | -0.36 [-0.96, 0.15] | small | n.s. |
| c vs d | -1.91 | 15 | = 0.372 | -0.39 [-0.97, 0.04] | small | n.s. |
| c vs e | -2.04 | 15 | = 0.372 | -0.57 [-1.21, -0.14] | medium | n.s. |
| d vs e | -0.92 | 15 | = 0.465 | -0.18 [-0.53, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.014) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - a showed smaller amplitude than b (*d* = -0.42)
  - a showed smaller amplitude than e (*d* = -0.40)
  - b showed greater amplitude than c (*d* = 0.55)
  - b showed greater amplitude than d (*d* = 0.41)
  - c showed smaller amplitude than e (*d* = -0.54)
  - d showed smaller amplitude than e (*d* = -0.39)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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
