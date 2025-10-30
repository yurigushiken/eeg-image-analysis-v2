# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:53:18

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
| 4 to 1 | 20 | -1.71 µV | 1.46 | 0.33 | [-5.32, 0.01] |
| 4 to 2 | 24 | -4.13 µV | 2.46 | 0.50 | [-9.26, -0.51] |
| 4 to 3 | 23 | -4.12 µV | 1.97 | 0.41 | [-8.55, -0.51] |
| 4 to 5 | 23 | -3.68 µV | 2.28 | 0.47 | [-8.19, -0.69] |
| 4 to 6 | 23 | -3.92 µV | 2.27 | 0.47 | [-8.86, -0.34] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 182.40 ms | 13.16 | 2.94 | [148.70, 203.39] |
| 4 to 2 | 24 | 177.23 ms | 9.12 | 1.86 | [161.53, 202.22] |
| 4 to 3 | 23 | 175.67 ms | 10.07 | 2.10 | [157.54, 205.20] |
| 4 to 5 | 23 | 173.24 ms | 9.99 | 2.08 | [152.07, 194.76] |
| 4 to 6 | 23 | 174.24 ms | 11.16 | 2.33 | [150.86, 202.61] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 18 | 3.24 µV | 2.69 | 0.63 | [0.36, 10.41] |
| 4 to 2 | 14 | 1.50 µV | 1.09 | 0.29 | [0.16, 3.80] |
| 4 to 3 | 11 | 1.91 µV | 1.31 | 0.39 | [0.29, 4.76] |
| 4 to 5 | 13 | 2.71 µV | 2.93 | 0.81 | [0.27, 11.07] |
| 4 to 6 | 12 | 2.01 µV | 1.40 | 0.40 | [0.09, 4.66] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 18 | 107.94 ms | 2.86 | 0.68 | [99.58, 113.17] |
| 4 to 2 | 14 | 109.56 ms | 2.62 | 0.70 | [106.40, 114.77] |
| 4 to 3 | 11 | 105.51 ms | 3.12 | 0.94 | [99.06, 109.76] |
| 4 to 5 | 13 | 104.89 ms | 3.40 | 0.94 | [97.98, 107.98] |
| 4 to 6 | 12 | 106.11 ms | 4.46 | 1.29 | [97.03, 113.59] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 4.27 µV | 2.65 | 0.59 | [0.79, 8.70] |
| 4 to 2 | 19 | 3.42 µV | 2.52 | 0.58 | [0.25, 7.61] |
| 4 to 3 | 21 | 3.53 µV | 2.77 | 0.60 | [0.22, 9.37] |
| 4 to 5 | 16 | 3.48 µV | 3.12 | 0.78 | [0.50, 11.89] |
| 4 to 6 | 18 | 3.59 µV | 2.40 | 0.57 | [0.38, 7.53] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 483.03 ms | 12.02 | 2.69 | [457.26, 507.96] |
| 4 to 2 | 19 | 479.43 ms | 18.10 | 4.15 | [435.99, 503.79] |
| 4 to 3 | 21 | 480.04 ms | 19.25 | 4.20 | [431.27, 525.07] |
| 4 to 5 | 16 | 494.42 ms | 19.64 | 4.91 | [441.95, 516.54] |
| 4 to 6 | 18 | 490.07 ms | 19.79 | 4.66 | [462.54, 527.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 405.59, BIC = 427.41
- **4 to 2 vs 4 to 1**: *β* = -1.86, *SE* = 0.348, *z* = -5.342, *p* < .001
- **4 to 3 vs 4 to 1**: *β* = -1.40, *SE* = 0.365, *z* = -3.827, *p* < .001
- **4 to 5 vs 4 to 1**: *β* = -1.22, *SE* = 0.354, *z* = -3.434, *p* = 0.001
- **4 to 6 vs 4 to 1**: *β* = -1.29, *SE* = 0.361, *z* = -3.582, *p* < .001
- **SNR**: *β* = -0.40, *SE* = 0.048, *z* = -8.275, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 1.86 | 0.35 | 5.34 | < .001 | < .001 | *** |
| 4 to 1 - 4 to 3 | 1.40 | 0.37 | 3.83 | < .001 | 0.001 | ** |
| 4 to 1 - 4 to 5 | 1.22 | 0.35 | 3.43 | < .001 | 0.004 | ** |
| 4 to 1 - 4 to 6 | 1.29 | 0.36 | 3.58 | < .001 | 0.003 | ** |
| 4 to 2 - 4 to 3 | -0.46 | 0.33 | -1.39 | 0.164 | 0.512 | n.s. |
| 4 to 2 - 4 to 5 | -0.64 | 0.33 | -1.96 | 0.050 | 0.264 | n.s. |
| 4 to 2 - 4 to 6 | -0.57 | 0.33 | -1.72 | 0.086 | 0.361 | n.s. |
| 4 to 3 - 4 to 5 | -0.18 | 0.33 | -0.54 | 0.588 | 0.930 | n.s. |
| 4 to 3 - 4 to 6 | -0.10 | 0.33 | -0.32 | 0.752 | 0.938 | n.s. |
| 4 to 5 - 4 to 6 | 0.08 | 0.33 | 0.23 | 0.819 | 0.938 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.91, *p* < .001, η²_G = 0.199
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 4.15 | 16 | = 0.002 | 1.28 [0.45, 1.61] | large | ** |
| 4 to 1 vs 4 to 3 | 5.14 | 16 | < .001 | 1.56 [0.56, 1.83] | large | *** |
| 4 to 1 vs 4 to 5 | 4.26 | 16 | = 0.002 | 1.23 [0.38, 1.54] | large | ** |
| 4 to 1 vs 4 to 6 | 4.00 | 16 | = 0.003 | 1.20 [0.35, 1.50] | large | ** |
| 4 to 2 vs 4 to 3 | -0.13 | 16 | = 0.972 | -0.03 [-0.41, 0.46] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | -0.40 | 16 | = 0.867 | -0.12 [-0.68, 0.20] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | -0.59 | 16 | = 0.867 | -0.13 [-0.57, 0.30] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | -0.43 | 16 | = 0.867 | -0.11 [-0.70, 0.20] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | -0.68 | 16 | = 0.867 | -0.12 [-0.58, 0.31] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | -0.04 | 16 | = 0.972 | -0.01 [-0.34, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 837.93, BIC = 859.75
- **4 to 2 vs 4 to 1**: *β* = -5.41, *SE* = 2.409, *z* = -2.244, *p* = 0.025
- **4 to 3 vs 4 to 1**: *β* = -7.12, *SE* = 2.527, *z* = -2.819, *p* = 0.005
- **4 to 5 vs 4 to 1**: *β* = -8.49, *SE* = 2.453, *z* = -3.461, *p* = 0.001
- **4 to 6 vs 4 to 1**: *β* = -8.16, *SE* = 2.497, *z* = -3.269, *p* = 0.001
- **SNR**: *β* = -0.17, *SE* = 0.321, *z* = -0.540, *p* = 0.589

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 5.41 | 2.41 | 2.24 | 0.025 | 0.161 | n.s. |
| 4 to 1 - 4 to 3 | 7.12 | 2.53 | 2.82 | 0.005 | 0.038 | * |
| 4 to 1 - 4 to 5 | 8.49 | 2.45 | 3.46 | < .001 | 0.005 | ** |
| 4 to 1 - 4 to 6 | 8.16 | 2.50 | 3.27 | 0.001 | 0.010 | ** |
| 4 to 2 - 4 to 3 | 1.72 | 2.29 | 0.75 | 0.454 | 0.911 | n.s. |
| 4 to 2 - 4 to 5 | 3.08 | 2.27 | 1.36 | 0.174 | 0.683 | n.s. |
| 4 to 2 - 4 to 6 | 2.75 | 2.28 | 1.21 | 0.227 | 0.725 | n.s. |
| 4 to 3 - 4 to 5 | 1.37 | 2.31 | 0.59 | 0.555 | 0.912 | n.s. |
| 4 to 3 - 4 to 6 | 1.04 | 2.30 | 0.45 | 0.652 | 0.912 | n.s. |
| 4 to 5 - 4 to 6 | -0.33 | 2.30 | -0.14 | 0.886 | 0.912 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.42, *p* = 0.014, η²_G = 0.106
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.77 | 16 | = 0.226 | 0.59 [-0.03, 0.96] | medium | n.s. |
| 4 to 1 vs 4 to 3 | 2.26 | 16 | = 0.128 | 0.61 [0.05, 1.09] | medium | n.s. |
| 4 to 1 vs 4 to 5 | 2.56 | 16 | = 0.128 | 0.79 [0.11, 1.16] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 2.43 | 16 | = 0.128 | 0.80 [0.04, 1.08] | medium | n.s. |
| 4 to 2 vs 4 to 3 | 0.21 | 16 | = 0.930 | 0.07 [-0.23, 0.64] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 1.57 | 16 | = 0.226 | 0.35 [-0.13, 0.76] | small | n.s. |
| 4 to 2 vs 4 to 6 | 1.61 | 16 | = 0.226 | 0.35 [-0.02, 0.89] | small | n.s. |
| 4 to 3 vs 4 to 5 | 1.08 | 16 | = 0.423 | 0.28 [-0.38, 0.51] | small | n.s. |
| 4 to 3 vs 4 to 6 | 0.93 | 16 | = 0.459 | 0.28 [-0.28, 0.61] | small | n.s. |
| 4 to 5 vs 4 to 6 | -0.03 | 16 | = 0.980 | -0.01 [-0.49, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 255.43, BIC = 273.19
- **4 to 2 vs 4 to 1**: *β* = -0.23, *SE* = 0.527, *z* = -0.447, *p* = 0.655
- **4 to 3 vs 4 to 1**: *β* = -0.76, *SE* = 0.535, *z* = -1.422, *p* = 0.155
- **4 to 5 vs 4 to 1**: *β* = 0.00, *SE* = 0.506, *z* = 0.005, *p* = 0.996
- **4 to 6 vs 4 to 1**: *β* = -0.25, *SE* = 0.536, *z* = -0.472, *p* = 0.637
- **SNR**: *β* = 0.79, *SE* = 0.099, *z* = 7.942, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 0.24 | 0.53 | 0.45 | 0.655 | 0.998 | n.s. |
| 4 to 1 - 4 to 3 | 0.76 | 0.54 | 1.42 | 0.155 | 0.815 | n.s. |
| 4 to 1 - 4 to 5 | -0.00 | 0.51 | -0.00 | 0.996 | 0.999 | n.s. |
| 4 to 1 - 4 to 6 | 0.25 | 0.54 | 0.47 | 0.637 | 0.998 | n.s. |
| 4 to 2 - 4 to 3 | 0.53 | 0.55 | 0.95 | 0.343 | 0.965 | n.s. |
| 4 to 2 - 4 to 5 | -0.24 | 0.54 | -0.44 | 0.658 | 0.998 | n.s. |
| 4 to 2 - 4 to 6 | 0.02 | 0.54 | 0.03 | 0.973 | 0.999 | n.s. |
| 4 to 3 - 4 to 5 | -0.76 | 0.56 | -1.37 | 0.171 | 0.815 | n.s. |
| 4 to 3 - 4 to 6 | -0.51 | 0.57 | -0.89 | 0.374 | 0.965 | n.s. |
| 4 to 5 - 4 to 6 | 0.26 | 0.55 | 0.47 | 0.640 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.43, *p* = 0.091, η²_G = 0.297
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 2.39 | 4 | = 0.251 | 1.33 [-0.04, 1.37] | large | n.s. |
| 4 to 1 vs 4 to 3 | 1.69 | 4 | = 0.414 | 0.82 [-0.04, 1.76] | large | n.s. |
| 4 to 1 vs 4 to 5 | 1.47 | 4 | = 0.421 | 0.71 [-0.15, 1.30] | medium | n.s. |
| 4 to 1 vs 4 to 6 | 1.29 | 4 | = 0.421 | 0.95 [-0.36, 1.25] | large | n.s. |
| 4 to 2 vs 4 to 3 | -2.81 | 4 | = 0.251 | -1.50 [-0.91, 0.53] | large | n.s. |
| 4 to 2 vs 4 to 5 | -2.46 | 4 | = 0.251 | -1.16 [-1.45, 0.13] | large | n.s. |
| 4 to 2 vs 4 to 6 | -1.20 | 4 | = 0.421 | -0.89 [-1.56, 0.28] | large | n.s. |
| 4 to 3 vs 4 to 5 | -0.21 | 4 | = 0.845 | -0.14 [-1.34, 0.42] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | 0.41 | 4 | = 0.783 | 0.33 [-0.81, 1.04] | small | n.s. |
| 4 to 5 vs 4 to 6 | 0.60 | 4 | = 0.725 | 0.39 [-0.53, 1.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 363.41, BIC = 381.16
- **4 to 2 vs 4 to 1**: *β* = 1.52, *SE* = 1.116, *z* = 1.367, *p* = 0.172
- **4 to 3 vs 4 to 1**: *β* = -2.27, *SE* = 1.134, *z* = -2.004, *p* = 0.045
- **4 to 5 vs 4 to 1**: *β* = -3.05, *SE* = 1.055, *z* = -2.886, *p* = 0.004
- **4 to 6 vs 4 to 1**: *β* = -1.57, *SE* = 1.131, *z* = -1.391, *p* = 0.164
- **SNR**: *β* = 0.09, *SE* = 0.220, *z* = 0.397, *p* = 0.692

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -1.53 | 1.12 | -1.37 | 0.172 | 0.592 | n.s. |
| 4 to 1 - 4 to 3 | 2.27 | 1.13 | 2.00 | 0.045 | 0.242 | n.s. |
| 4 to 1 - 4 to 5 | 3.05 | 1.06 | 2.89 | 0.004 | 0.031 | * |
| 4 to 1 - 4 to 6 | 1.57 | 1.13 | 1.39 | 0.164 | 0.592 | n.s. |
| 4 to 2 - 4 to 3 | 3.80 | 1.17 | 3.24 | 0.001 | 0.011 | * |
| 4 to 2 - 4 to 5 | 4.57 | 1.14 | 4.02 | < .001 | < .001 | *** |
| 4 to 2 - 4 to 6 | 3.10 | 1.16 | 2.68 | 0.007 | 0.051 | n.s. |
| 4 to 3 - 4 to 5 | 0.77 | 1.18 | 0.66 | 0.512 | 0.762 | n.s. |
| 4 to 3 - 4 to 6 | -0.70 | 1.21 | -0.58 | 0.563 | 0.762 | n.s. |
| 4 to 5 - 4 to 6 | -1.47 | 1.16 | -1.27 | 0.204 | 0.592 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.552, η²_G = 0.120
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.45 | 4 | = 0.768 | 0.13 [-1.14, 0.20] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | 1.36 | 4 | = 0.613 | 1.10 [-0.06, 1.72] | large | n.s. |
| 4 to 1 vs 4 to 5 | 1.65 | 4 | = 0.613 | 0.95 [-0.18, 1.25] | large | n.s. |
| 4 to 1 vs 4 to 6 | 0.48 | 4 | = 0.768 | 0.34 [-0.47, 1.11] | small | n.s. |
| 4 to 2 vs 4 to 3 | 1.46 | 4 | = 0.613 | 0.97 [-0.07, 1.54] | large | n.s. |
| 4 to 2 vs 4 to 5 | 1.95 | 4 | = 0.613 | 0.78 [0.24, 2.09] | medium | n.s. |
| 4 to 2 vs 4 to 6 | 0.43 | 4 | = 0.768 | 0.27 [-0.36, 1.42] | small | n.s. |
| 4 to 3 vs 4 to 5 | -0.86 | 4 | = 0.768 | -0.45 [-0.77, 0.91] | small | n.s. |
| 4 to 3 vs 4 to 6 | -0.69 | 4 | = 0.768 | -0.34 [-1.12, 0.74] | small | n.s. |
| 4 to 5 vs 4 to 6 | -0.21 | 4 | = 0.840 | -0.11 [-1.13, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 387.96, BIC = 408.31
- **4 to 2 vs 4 to 1**: *β* = 0.13, *SE* = 0.483, *z* = 0.273, *p* = 0.785
- **4 to 3 vs 4 to 1**: *β* = 0.02, *SE* = 0.461, *z* = 0.038, *p* = 0.970
- **4 to 5 vs 4 to 1**: *β* = -0.01, *SE* = 0.506, *z* = -0.019, *p* = 0.984
- **4 to 6 vs 4 to 1**: *β* = -0.07, *SE* = 0.484, *z* = -0.138, *p* = 0.890
- **SNR**: *β* = 0.26, *SE* = 0.040, *z* = 6.527, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | -0.13 | 0.48 | -0.27 | 0.785 | 1.000 | n.s. |
| 4 to 1 - 4 to 3 | -0.02 | 0.46 | -0.04 | 0.970 | 1.000 | n.s. |
| 4 to 1 - 4 to 5 | 0.01 | 0.51 | 0.02 | 0.984 | 1.000 | n.s. |
| 4 to 1 - 4 to 6 | 0.07 | 0.48 | 0.14 | 0.890 | 1.000 | n.s. |
| 4 to 2 - 4 to 3 | 0.11 | 0.46 | 0.25 | 0.803 | 1.000 | n.s. |
| 4 to 2 - 4 to 5 | 0.14 | 0.49 | 0.29 | 0.772 | 1.000 | n.s. |
| 4 to 2 - 4 to 6 | 0.20 | 0.48 | 0.42 | 0.677 | 1.000 | n.s. |
| 4 to 3 - 4 to 5 | 0.03 | 0.48 | 0.06 | 0.955 | 1.000 | n.s. |
| 4 to 3 - 4 to 6 | 0.08 | 0.46 | 0.18 | 0.855 | 1.000 | n.s. |
| 4 to 5 - 4 to 6 | 0.06 | 0.49 | 0.11 | 0.908 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.20, *p* = 0.940, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.826 (ε = 0.504)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 0.60 | 12 | = 0.883 | 0.11 [-0.20, 0.85] | negligible | n.s. |
| 4 to 1 vs 4 to 3 | 0.26 | 12 | = 0.883 | 0.06 [-0.32, 0.69] | negligible | n.s. |
| 4 to 1 vs 4 to 5 | 0.44 | 12 | = 0.883 | 0.14 [-0.35, 0.76] | negligible | n.s. |
| 4 to 1 vs 4 to 6 | 1.21 | 12 | = 0.883 | 0.21 [-0.14, 0.98] | small | n.s. |
| 4 to 2 vs 4 to 3 | -0.33 | 12 | = 0.883 | -0.05 [-0.61, 0.38] | negligible | n.s. |
| 4 to 2 vs 4 to 5 | 0.15 | 12 | = 0.883 | 0.04 [-0.49, 0.62] | negligible | n.s. |
| 4 to 2 vs 4 to 6 | 0.56 | 12 | = 0.883 | 0.10 [-0.49, 0.57] | negligible | n.s. |
| 4 to 3 vs 4 to 5 | 0.24 | 12 | = 0.883 | 0.09 [-0.40, 0.67] | negligible | n.s. |
| 4 to 3 vs 4 to 6 | 0.55 | 12 | = 0.883 | 0.15 [-0.33, 0.67] | negligible | n.s. |
| 4 to 5 vs 4 to 6 | 0.20 | 12 | = 0.883 | 0.05 [-0.62, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 814.73, BIC = 835.08
- **4 to 2 vs 4 to 1**: *β* = -4.73, *SE* = 5.197, *z* = -0.910, *p* = 0.363
- **4 to 3 vs 4 to 1**: *β* = -2.76, *SE* = 4.964, *z* = -0.555, *p* = 0.579
- **4 to 5 vs 4 to 1**: *β* = 11.33, *SE* = 5.415, *z* = 2.092, *p* = 0.036
- **4 to 6 vs 4 to 1**: *β* = 8.22, *SE* = 5.208, *z* = 1.578, *p* = 0.115
- **SNR**: *β* = -0.08, *SE* = 0.390, *z* = -0.206, *p* = 0.837

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 4 to 2 | 4.73 | 5.20 | 0.91 | 0.363 | 0.835 | n.s. |
| 4 to 1 - 4 to 3 | 2.76 | 4.96 | 0.56 | 0.579 | 0.917 | n.s. |
| 4 to 1 - 4 to 5 | -11.33 | 5.42 | -2.09 | 0.036 | 0.200 | n.s. |
| 4 to 1 - 4 to 6 | -8.22 | 5.21 | -1.58 | 0.115 | 0.456 | n.s. |
| 4 to 2 - 4 to 3 | -1.97 | 4.98 | -0.40 | 0.692 | 0.917 | n.s. |
| 4 to 2 - 4 to 5 | -16.06 | 5.32 | -3.02 | 0.003 | 0.025 | * |
| 4 to 2 - 4 to 6 | -12.95 | 5.23 | -2.48 | 0.013 | 0.101 | n.s. |
| 4 to 3 - 4 to 5 | -14.09 | 5.20 | -2.71 | 0.007 | 0.059 | n.s. |
| 4 to 3 - 4 to 6 | -10.98 | 5.01 | -2.19 | 0.028 | 0.183 | n.s. |
| 4 to 5 - 4 to 6 | 3.11 | 5.39 | 0.58 | 0.564 | 0.917 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.58, *p* = 0.003, η²_G = 0.204
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 4 to 2 | 1.58 | 12 | = 0.200 | 0.49 [-0.36, 0.67] | small | n.s. |
| 4 to 1 vs 4 to 3 | 0.40 | 12 | = 0.693 | 0.16 [-0.43, 0.57] | negligible | n.s. |
| 4 to 1 vs 4 to 5 | -2.25 | 12 | = 0.088 | -0.97 [-1.00, 0.15] | large | n.s. |
| 4 to 1 vs 4 to 6 | -1.72 | 12 | = 0.184 | -0.70 [-0.87, 0.22] | medium | n.s. |
| 4 to 2 vs 4 to 3 | -0.82 | 12 | = 0.534 | -0.25 [-0.71, 0.30] | small | n.s. |
| 4 to 2 vs 4 to 5 | -3.47 | 12 | = 0.046 | -1.38 [-1.73, -0.35] | large | * |
| 4 to 2 vs 4 to 6 | -2.78 | 12 | = 0.056 | -1.10 [-1.23, -0.06] | large | n.s. |
| 4 to 3 vs 4 to 5 | -2.46 | 12 | = 0.075 | -0.93 [-1.16, -0.01] | large | n.s. |
| 4 to 3 vs 4 to 6 | -3.00 | 12 | = 0.056 | -0.73 [-1.15, -0.06] | medium | n.s. |
| 4 to 5 vs 4 to 6 | 0.42 | 12 | = 0.693 | 0.15 [-0.60, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 4 to 2 (*d* = 1.28)
  - 4 to 1 showed greater amplitude than 4 to 3 (*d* = 1.56)
  - 4 to 1 showed greater amplitude than 4 to 5 (*d* = 1.23)
  - 4 to 1 showed greater amplitude than 4 to 6 (*d* = 1.20)
**N1 latency:** Significant main effect of condition (*p* = 0.014) (no significant pairwise comparisons)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.091)
**P3b latency:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 4 to 2 showed smaller latency than 4 to 5 (*d* = -1.38)

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
