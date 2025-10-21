# Statistical Analysis Report: tables

**Generated:** 2025-10-20 21:54:00

---

## 1. Analysis Overview

**Total Measurements:** 432
**Number of Subjects:** 24
**Number of Conditions:** 6

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
| from 1 | 24 | -3.24 µV | 1.78 | 0.36 | [-8.35, -0.15] |
| from 2 | 23 | -3.06 µV | 1.51 | 0.32 | [-6.77, 0.01] |
| from 3 | 22 | -3.48 µV | 1.52 | 0.33 | [-7.59, -1.60] |
| from 4 | 24 | -3.36 µV | 1.81 | 0.37 | [-8.29, 0.02] |
| from 5 | 23 | -4.17 µV | 1.85 | 0.39 | [-8.17, -0.65] |
| from 6 | 24 | -3.69 µV | 1.79 | 0.37 | [-7.18, -1.27] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 24 | 175.22 ms | 10.09 | 2.06 | [157.81, 201.97] |
| from 2 | 23 | 175.00 ms | 9.93 | 2.07 | [158.97, 203.64] |
| from 3 | 22 | 172.75 ms | 6.89 | 1.47 | [158.77, 187.36] |
| from 4 | 24 | 175.20 ms | 8.72 | 1.78 | [159.50, 203.96] |
| from 5 | 23 | 173.93 ms | 6.37 | 1.33 | [157.22, 186.57] |
| from 6 | 24 | 174.00 ms | 9.13 | 1.86 | [159.91, 194.67] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 15 | 1.39 µV | 1.36 | 0.35 | [0.17, 4.89] |
| from 2 | 15 | 1.45 µV | 1.51 | 0.39 | [0.08, 4.92] |
| from 3 | 16 | 1.21 µV | 1.30 | 0.33 | [0.11, 4.87] |
| from 4 | 13 | 1.50 µV | 1.35 | 0.38 | [0.02, 3.71] |
| from 5 | 15 | 1.38 µV | 1.01 | 0.26 | [0.14, 3.20] |
| from 6 | 12 | 1.83 µV | 1.34 | 0.39 | [0.58, 5.50] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 15 | 105.50 ms | 4.46 | 1.15 | [98.94, 113.70] |
| from 2 | 15 | 104.99 ms | 4.73 | 1.22 | [96.28, 112.44] |
| from 3 | 16 | 105.37 ms | 5.22 | 1.30 | [94.79, 112.73] |
| from 4 | 13 | 106.26 ms | 4.60 | 1.27 | [94.17, 114.71] |
| from 5 | 15 | 104.50 ms | 5.69 | 1.47 | [93.76, 112.51] |
| from 6 | 12 | 107.09 ms | 2.65 | 0.77 | [103.57, 111.38] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 17 | 3.21 µV | 2.27 | 0.55 | [0.37, 8.57] |
| from 2 | 19 | 3.07 µV | 2.00 | 0.46 | [0.04, 6.09] |
| from 3 | 19 | 3.06 µV | 2.05 | 0.47 | [0.08, 7.58] |
| from 4 | 17 | 3.22 µV | 1.97 | 0.48 | [0.12, 6.49] |
| from 5 | 18 | 2.53 µV | 1.61 | 0.38 | [0.01, 5.26] |
| from 6 | 18 | 2.53 µV | 1.86 | 0.44 | [0.11, 6.18] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 1 | 17 | 473.52 ms | 10.32 | 2.50 | [447.42, 494.73] |
| from 2 | 19 | 472.72 ms | 14.18 | 3.25 | [422.58, 485.84] |
| from 3 | 19 | 476.61 ms | 15.42 | 3.54 | [456.92, 527.62] |
| from 4 | 17 | 479.96 ms | 13.37 | 3.24 | [454.86, 509.96] |
| from 5 | 18 | 472.22 ms | 10.95 | 2.58 | [448.53, 486.88] |
| from 6 | 18 | 473.52 ms | 21.27 | 5.01 | [425.11, 524.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 375.61, BIC = 402.09
- **from 2 vs from 1**: *β* = 0.32, *SE* = 0.192, *z* = 1.654, *p* = 0.098
- **from 3 vs from 1**: *β* = 0.13, *SE* = 0.196, *z* = 0.644, *p* = 0.520
- **from 4 vs from 1**: *β* = -0.01, *SE* = 0.190, *z* = -0.076, *p* = 0.939
- **from 5 vs from 1**: *β* = -0.61, *SE* = 0.196, *z* = -3.139, *p* = 0.002
- **from 6 vs from 1**: *β* = -0.40, *SE* = 0.189, *z* = -2.118, *p* = 0.034
- **SNR**: *β* = -0.07, *SE* = 0.014, *z* = -5.185, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.32 | 0.19 | -1.65 | 0.098 | 0.463 | n.s. |
| from 1 - from 3 | -0.13 | 0.20 | -0.64 | 0.520 | 0.851 | n.s. |
| from 1 - from 4 | 0.01 | 0.19 | 0.08 | 0.939 | 0.939 | n.s. |
| from 1 - from 5 | 0.61 | 0.20 | 3.14 | 0.002 | 0.020 | * |
| from 1 - from 6 | 0.40 | 0.19 | 2.12 | 0.034 | 0.269 | n.s. |
| from 2 - from 3 | 0.19 | 0.20 | 0.97 | 0.333 | 0.802 | n.s. |
| from 2 - from 4 | 0.33 | 0.19 | 1.72 | 0.085 | 0.463 | n.s. |
| from 2 - from 5 | 0.93 | 0.20 | 4.71 | < .001 | < .001 | *** |
| from 2 - from 6 | 0.72 | 0.19 | 3.74 | < .001 | 0.002 | ** |
| from 3 - from 4 | 0.14 | 0.19 | 0.72 | 0.469 | 0.851 | n.s. |
| from 3 - from 5 | 0.74 | 0.20 | 3.77 | < .001 | 0.002 | ** |
| from 3 - from 6 | 0.53 | 0.20 | 2.70 | 0.007 | 0.067 | n.s. |
| from 4 - from 5 | 0.60 | 0.19 | 3.11 | 0.002 | 0.020 | * |
| from 4 - from 6 | 0.39 | 0.19 | 2.04 | 0.041 | 0.287 | n.s. |
| from 5 - from 6 | -0.21 | 0.19 | -1.09 | 0.274 | 0.798 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.73, *p* < .001, η²_G = 0.052
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.689)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -2.21 | 21 | = 0.071 | -0.24 [-0.84, 0.05] | small | n.s. |
| from 1 vs from 3 | -0.17 | 21 | = 0.867 | -0.02 [-0.48, 0.41] | negligible | n.s. |
| from 1 vs from 4 | 0.45 | 21 | = 0.703 | 0.06 [-0.31, 0.54] | negligible | n.s. |
| from 1 vs from 5 | 3.47 | 21 | = 0.011 | 0.49 [0.26, 1.23] | small | * |
| from 1 vs from 6 | 1.42 | 21 | = 0.234 | 0.23 [-0.08, 0.80] | small | n.s. |
| from 2 vs from 3 | 1.85 | 21 | = 0.130 | 0.23 [-0.07, 0.86] | small | n.s. |
| from 2 vs from 4 | 2.41 | 21 | = 0.058 | 0.30 [-0.03, 0.87] | small | n.s. |
| from 2 vs from 5 | 5.22 | 21 | < .001 | 0.73 [0.55, 1.68] | medium | *** |
| from 2 vs from 6 | 3.67 | 21 | = 0.011 | 0.47 [0.27, 1.26] | small | * |
| from 3 vs from 4 | 0.83 | 21 | = 0.481 | 0.09 [-0.27, 0.62] | negligible | n.s. |
| from 3 vs from 5 | 3.12 | 21 | = 0.020 | 0.52 [0.17, 1.15] | medium | * |
| from 3 vs from 6 | 1.66 | 21 | = 0.169 | 0.26 [-0.10, 0.81] | small | n.s. |
| from 4 vs from 5 | 2.97 | 21 | = 0.022 | 0.42 [0.12, 1.06] | small | * |
| from 4 vs from 6 | 1.11 | 21 | = 0.351 | 0.17 [-0.15, 0.71] | negligible | n.s. |
| from 5 vs from 6 | -2.37 | 21 | = 0.058 | -0.25 [-0.89, 0.01] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 828.88, BIC = 855.35
- **from 2 vs from 1**: *β* = 0.35, *SE* = 0.931, *z* = 0.376, *p* = 0.707
- **from 3 vs from 1**: *β* = -0.82, *SE* = 0.952, *z* = -0.857, *p* = 0.391
- **from 4 vs from 1**: *β* = -0.03, *SE* = 0.924, *z* = -0.037, *p* = 0.970
- **from 5 vs from 1**: *β* = -0.29, *SE* = 0.949, *z* = -0.303, *p* = 0.762
- **from 6 vs from 1**: *β* = -1.22, *SE* = 0.919, *z* = -1.328, *p* = 0.184
- **SNR**: *β* = 0.01, *SE* = 0.066, *z* = 0.111, *p* = 0.912

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.35 | 0.93 | -0.38 | 0.707 | 0.999 | n.s. |
| from 1 - from 3 | 0.82 | 0.95 | 0.86 | 0.391 | 0.993 | n.s. |
| from 1 - from 4 | 0.03 | 0.92 | 0.04 | 0.970 | 0.999 | n.s. |
| from 1 - from 5 | 0.29 | 0.95 | 0.30 | 0.762 | 0.999 | n.s. |
| from 1 - from 6 | 1.22 | 0.92 | 1.33 | 0.184 | 0.942 | n.s. |
| from 2 - from 3 | 1.17 | 0.96 | 1.22 | 0.223 | 0.952 | n.s. |
| from 2 - from 4 | 0.38 | 0.93 | 0.41 | 0.680 | 0.999 | n.s. |
| from 2 - from 5 | 0.64 | 0.96 | 0.67 | 0.505 | 0.996 | n.s. |
| from 2 - from 6 | 1.57 | 0.93 | 1.69 | 0.091 | 0.763 | n.s. |
| from 3 - from 4 | -0.78 | 0.94 | -0.83 | 0.408 | 0.993 | n.s. |
| from 3 - from 5 | -0.53 | 0.95 | -0.55 | 0.579 | 0.998 | n.s. |
| from 3 - from 6 | 0.40 | 0.95 | 0.43 | 0.670 | 0.999 | n.s. |
| from 4 - from 5 | 0.25 | 0.93 | 0.27 | 0.786 | 0.999 | n.s. |
| from 4 - from 6 | 1.19 | 0.92 | 1.29 | 0.197 | 0.943 | n.s. |
| from 5 - from 6 | 0.93 | 0.94 | 0.99 | 0.322 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.637, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.542 (ε = 0.503)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -1.32 | 21 | = 0.782 | -0.15 [-0.64, 0.23] | negligible | n.s. |
| from 1 vs from 3 | 0.15 | 21 | = 0.983 | 0.01 [-0.41, 0.47] | negligible | n.s. |
| from 1 vs from 4 | -0.93 | 21 | = 0.782 | -0.09 [-0.42, 0.43] | negligible | n.s. |
| from 1 vs from 5 | -0.74 | 21 | = 0.782 | -0.09 [-0.41, 0.46] | negligible | n.s. |
| from 1 vs from 6 | 0.27 | 21 | = 0.983 | 0.02 [-0.18, 0.68] | negligible | n.s. |
| from 2 vs from 3 | 1.32 | 21 | = 0.782 | 0.16 [-0.17, 0.73] | negligible | n.s. |
| from 2 vs from 4 | 0.47 | 21 | = 0.920 | 0.08 [-0.39, 0.47] | negligible | n.s. |
| from 2 vs from 5 | 0.43 | 21 | = 0.920 | 0.08 [-0.35, 0.54] | negligible | n.s. |
| from 2 vs from 6 | 1.65 | 21 | = 0.782 | 0.16 [-0.08, 0.81] | negligible | n.s. |
| from 3 vs from 4 | -0.86 | 21 | = 0.782 | -0.10 [-0.63, 0.26] | negligible | n.s. |
| from 3 vs from 5 | -0.84 | 21 | = 0.782 | -0.10 [-0.63, 0.27] | negligible | n.s. |
| from 3 vs from 6 | 0.10 | 21 | = 0.983 | 0.01 [-0.42, 0.47] | negligible | n.s. |
| from 4 vs from 5 | -0.02 | 21 | = 0.983 | -0.00 [-0.43, 0.44] | negligible | n.s. |
| from 4 vs from 6 | 0.81 | 21 | = 0.782 | 0.10 [-0.16, 0.70] | negligible | n.s. |
| from 5 vs from 6 | 0.74 | 21 | = 0.782 | 0.11 [-0.26, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 223.19, BIC = 245.27
- **from 2 vs from 1**: *β* = -0.15, *SE* = 0.245, *z* = -0.597, *p* = 0.550
- **from 3 vs from 1**: *β* = -0.18, *SE* = 0.242, *z* = -0.737, *p* = 0.461
- **from 4 vs from 1**: *β* = -0.00, *SE* = 0.253, *z* = -0.007, *p* = 0.995
- **from 5 vs from 1**: *β* = -0.00, *SE* = 0.244, *z* = -0.000, *p* = 1.000
- **from 6 vs from 1**: *β* = 0.20, *SE* = 0.259, *z* = 0.756, *p* = 0.449
- **SNR**: *β* = 0.12, *SE* = 0.021, *z* = 5.589, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.15 | 0.24 | 0.60 | 0.550 | 1.000 | n.s. |
| from 1 - from 3 | 0.18 | 0.24 | 0.74 | 0.461 | 1.000 | n.s. |
| from 1 - from 4 | 0.00 | 0.25 | 0.01 | 0.995 | 1.000 | n.s. |
| from 1 - from 5 | 0.00 | 0.24 | 0.00 | 1.000 | 1.000 | n.s. |
| from 1 - from 6 | -0.20 | 0.26 | -0.76 | 0.449 | 1.000 | n.s. |
| from 2 - from 3 | 0.03 | 0.24 | 0.13 | 0.896 | 1.000 | n.s. |
| from 2 - from 4 | -0.14 | 0.26 | -0.56 | 0.573 | 1.000 | n.s. |
| from 2 - from 5 | -0.15 | 0.25 | -0.58 | 0.559 | 1.000 | n.s. |
| from 2 - from 6 | -0.34 | 0.26 | -1.32 | 0.187 | 0.945 | n.s. |
| from 3 - from 4 | -0.18 | 0.25 | -0.71 | 0.476 | 1.000 | n.s. |
| from 3 - from 5 | -0.18 | 0.24 | -0.73 | 0.463 | 1.000 | n.s. |
| from 3 - from 6 | -0.37 | 0.25 | -1.47 | 0.142 | 0.900 | n.s. |
| from 4 - from 5 | -0.00 | 0.26 | -0.01 | 0.995 | 1.000 | n.s. |
| from 4 - from 6 | -0.20 | 0.27 | -0.74 | 0.460 | 1.000 | n.s. |
| from 5 - from 6 | -0.20 | 0.26 | -0.76 | 0.447 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.593, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.14 | 5 | = 0.919 | -0.05 [-0.64, 0.63] | negligible | n.s. |
| from 1 vs from 3 | 0.58 | 5 | = 0.907 | 0.29 [-0.54, 0.74] | small | n.s. |
| from 1 vs from 4 | 0.81 | 5 | = 0.851 | 0.38 [-0.61, 0.74] | small | n.s. |
| from 1 vs from 5 | 1.08 | 5 | = 0.710 | 0.53 [-0.43, 0.85] | medium | n.s. |
| from 1 vs from 6 | 0.11 | 5 | = 0.919 | 0.05 [-0.76, 0.68] | negligible | n.s. |
| from 2 vs from 3 | 1.36 | 5 | = 0.710 | 0.30 [-0.42, 0.87] | small | n.s. |
| from 2 vs from 4 | 1.50 | 5 | = 0.710 | 0.38 [-0.65, 0.69] | small | n.s. |
| from 2 vs from 5 | 1.35 | 5 | = 0.710 | 0.50 [-0.51, 0.84] | medium | n.s. |
| from 2 vs from 6 | 0.43 | 5 | = 0.907 | 0.09 [-0.66, 0.68] | negligible | n.s. |
| from 3 vs from 4 | 0.27 | 5 | = 0.919 | 0.06 [-0.82, 0.46] | negligible | n.s. |
| from 3 vs from 5 | 0.49 | 5 | = 0.907 | 0.15 [-0.93, 0.36] | negligible | n.s. |
| from 3 vs from 6 | -1.97 | 5 | = 0.710 | -0.22 [-1.61, -0.05] | small | n.s. |
| from 4 vs from 5 | 0.37 | 5 | = 0.907 | 0.09 [-1.04, 0.43] | negligible | n.s. |
| from 4 vs from 6 | -1.31 | 5 | = 0.710 | -0.30 [-1.06, 0.51] | small | n.s. |
| from 5 vs from 6 | -1.17 | 5 | = 0.710 | -0.42 [-0.87, 0.48] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 502.82, BIC = 524.90
- **from 2 vs from 1**: *β* = -0.78, *SE* = 1.243, *z* = -0.631, *p* = 0.528
- **from 3 vs from 1**: *β* = -0.14, *SE* = 1.228, *z* = -0.112, *p* = 0.911
- **from 4 vs from 1**: *β* = 0.48, *SE* = 1.286, *z* = 0.376, *p* = 0.707
- **from 5 vs from 1**: *β* = -0.99, *SE* = 1.240, *z* = -0.803, *p* = 0.422
- **from 6 vs from 1**: *β* = 0.98, *SE* = 1.316, *z* = 0.746, *p* = 0.456
- **SNR**: *β* = -0.02, *SE* = 0.100, *z* = -0.174, *p* = 0.862

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.78 | 1.24 | 0.63 | 0.528 | 0.996 | n.s. |
| from 1 - from 3 | 0.14 | 1.23 | 0.11 | 0.911 | 0.996 | n.s. |
| from 1 - from 4 | -0.48 | 1.29 | -0.38 | 0.707 | 0.996 | n.s. |
| from 1 - from 5 | 1.00 | 1.24 | 0.80 | 0.422 | 0.996 | n.s. |
| from 1 - from 6 | -0.98 | 1.32 | -0.75 | 0.456 | 0.996 | n.s. |
| from 2 - from 3 | -0.65 | 1.24 | -0.52 | 0.603 | 0.996 | n.s. |
| from 2 - from 4 | -1.27 | 1.30 | -0.98 | 0.329 | 0.992 | n.s. |
| from 2 - from 5 | 0.21 | 1.27 | 0.17 | 0.868 | 0.996 | n.s. |
| from 2 - from 6 | -1.77 | 1.32 | -1.34 | 0.180 | 0.938 | n.s. |
| from 3 - from 4 | -0.62 | 1.26 | -0.49 | 0.621 | 0.996 | n.s. |
| from 3 - from 5 | 0.86 | 1.23 | 0.70 | 0.487 | 0.996 | n.s. |
| from 3 - from 6 | -1.12 | 1.30 | -0.86 | 0.388 | 0.995 | n.s. |
| from 4 - from 5 | 1.48 | 1.30 | 1.14 | 0.256 | 0.979 | n.s. |
| from 4 - from 6 | -0.50 | 1.36 | -0.37 | 0.714 | 0.996 | n.s. |
| from 5 - from 6 | -1.98 | 1.32 | -1.50 | 0.133 | 0.882 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.36, *p* = 0.274, η²_G = 0.104
- Greenhouse-Geisser corrected: *p* = 0.302 (ε = 0.379)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | 1.01 | 5 | = 0.505 | 0.42 [-0.56, 0.71] | small | n.s. |
| from 1 vs from 3 | -1.47 | 5 | = 0.505 | -0.66 [-0.68, 0.59] | medium | n.s. |
| from 1 vs from 4 | -0.98 | 5 | = 0.505 | -0.47 [-1.24, 0.19] | small | n.s. |
| from 1 vs from 5 | -0.57 | 5 | = 0.687 | -0.25 [-0.47, 0.81] | small | n.s. |
| from 1 vs from 6 | -0.67 | 5 | = 0.669 | -0.21 [-1.21, 0.30] | small | n.s. |
| from 2 vs from 3 | -1.33 | 5 | = 0.505 | -0.89 [-0.69, 0.58] | large | n.s. |
| from 2 vs from 4 | -1.62 | 5 | = 0.505 | -0.72 [-0.82, 0.53] | medium | n.s. |
| from 2 vs from 5 | -1.07 | 5 | = 0.505 | -0.55 [-0.85, 0.50] | medium | n.s. |
| from 2 vs from 6 | -1.31 | 5 | = 0.505 | -0.56 [-1.19, 0.23] | medium | n.s. |
| from 3 vs from 4 | 0.20 | 5 | = 0.852 | 0.08 [-0.62, 0.65] | negligible | n.s. |
| from 3 vs from 5 | 1.09 | 5 | = 0.505 | 0.33 [-0.51, 0.77] | small | n.s. |
| from 3 vs from 6 | 1.24 | 5 | = 0.505 | 0.45 [-0.96, 0.41] | small | n.s. |
| from 4 vs from 5 | 1.43 | 5 | = 0.505 | 0.22 [-0.17, 1.39] | small | n.s. |
| from 4 vs from 6 | 1.14 | 5 | = 0.505 | 0.30 [-0.72, 0.81] | small | n.s. |
| from 5 vs from 6 | 0.33 | 5 | = 0.808 | 0.07 [-0.86, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 323.62, BIC = 347.76
- **from 2 vs from 1**: *β* = -0.03, *SE* = 0.259, *z* = -0.097, *p* = 0.922
- **from 3 vs from 1**: *β* = -0.20, *SE* = 0.261, *z* = -0.753, *p* = 0.451
- **from 4 vs from 1**: *β* = -0.48, *SE* = 0.273, *z* = -1.743, *p* = 0.081
- **from 5 vs from 1**: *β* = -0.54, *SE* = 0.259, *z* = -2.075, *p* = 0.038
- **from 6 vs from 1**: *β* = -0.61, *SE* = 0.259, *z* = -2.354, *p* = 0.019
- **SNR**: *β* = 0.15, *SE* = 0.021, *z* = 7.032, *p* < .001

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | 0.03 | 0.26 | 0.10 | 0.922 | 0.989 | n.s. |
| from 1 - from 3 | 0.20 | 0.26 | 0.75 | 0.451 | 0.973 | n.s. |
| from 1 - from 4 | 0.48 | 0.27 | 1.74 | 0.081 | 0.607 | n.s. |
| from 1 - from 5 | 0.54 | 0.26 | 2.07 | 0.038 | 0.396 | n.s. |
| from 1 - from 6 | 0.61 | 0.26 | 2.35 | 0.019 | 0.245 | n.s. |
| from 2 - from 3 | 0.17 | 0.25 | 0.68 | 0.498 | 0.973 | n.s. |
| from 2 - from 4 | 0.45 | 0.27 | 1.69 | 0.090 | 0.611 | n.s. |
| from 2 - from 5 | 0.51 | 0.26 | 2.00 | 0.046 | 0.428 | n.s. |
| from 2 - from 6 | 0.59 | 0.25 | 2.31 | 0.021 | 0.257 | n.s. |
| from 3 - from 4 | 0.28 | 0.26 | 1.09 | 0.278 | 0.897 | n.s. |
| from 3 - from 5 | 0.34 | 0.26 | 1.33 | 0.183 | 0.802 | n.s. |
| from 3 - from 6 | 0.41 | 0.25 | 1.63 | 0.104 | 0.627 | n.s. |
| from 4 - from 5 | 0.06 | 0.27 | 0.23 | 0.820 | 0.989 | n.s. |
| from 4 - from 6 | 0.13 | 0.27 | 0.50 | 0.617 | 0.978 | n.s. |
| from 5 - from 6 | 0.07 | 0.26 | 0.28 | 0.776 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.36, *p* = 0.048, η²_G = 0.035
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.42 | 15 | = 0.877 | -0.08 [-0.60, 0.43] | negligible | n.s. |
| from 1 vs from 3 | -0.39 | 15 | = 0.877 | -0.08 [-0.63, 0.40] | negligible | n.s. |
| from 1 vs from 4 | -0.09 | 15 | = 0.976 | -0.02 [-0.55, 0.51] | negligible | n.s. |
| from 1 vs from 5 | 1.57 | 15 | = 0.296 | 0.31 [-0.14, 0.93] | small | n.s. |
| from 1 vs from 6 | 1.40 | 15 | = 0.343 | 0.32 [-0.24, 0.81] | small | n.s. |
| from 2 vs from 3 | 0.03 | 15 | = 0.976 | 0.00 [-0.56, 0.43] | negligible | n.s. |
| from 2 vs from 4 | 0.60 | 15 | = 0.836 | 0.07 [-0.39, 0.69] | negligible | n.s. |
| from 2 vs from 5 | 3.14 | 15 | = 0.100 | 0.46 [0.17, 1.33] | small | n.s. |
| from 2 vs from 6 | 2.08 | 15 | = 0.189 | 0.45 [-0.12, 0.91] | small | n.s. |
| from 3 vs from 4 | 0.68 | 15 | = 0.836 | 0.07 [-0.36, 0.68] | negligible | n.s. |
| from 3 vs from 5 | 2.69 | 15 | = 0.126 | 0.44 [0.09, 1.18] | small | n.s. |
| from 3 vs from 6 | 2.01 | 15 | = 0.189 | 0.44 [-0.08, 0.96] | small | n.s. |
| from 4 vs from 5 | 2.33 | 15 | = 0.170 | 0.36 [-0.02, 1.08] | small | n.s. |
| from 4 vs from 6 | 1.81 | 15 | = 0.226 | 0.37 [-0.11, 1.01] | small | n.s. |
| from 5 vs from 6 | 0.23 | 15 | = 0.952 | 0.05 [-0.53, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 872.58, BIC = 896.72
- **from 2 vs from 1**: *β* = 0.43, *SE* = 3.606, *z* = 0.118, *p* = 0.906
- **from 3 vs from 1**: *β* = 3.01, *SE* = 3.633, *z* = 0.828, *p* = 0.408
- **from 4 vs from 1**: *β* = 3.94, *SE* = 3.804, *z* = 1.035, *p* = 0.301
- **from 5 vs from 1**: *β* = -2.43, *SE* = 3.624, *z* = -0.671, *p* = 0.502
- **from 6 vs from 1**: *β* = 1.44, *SE* = 3.628, *z* = 0.397, *p* = 0.692
- **SNR**: *β* = 0.22, *SE* = 0.276, *z* = 0.801, *p* = 0.423

_Reference condition: **from 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 1 - from 2 | -0.43 | 3.61 | -0.12 | 0.906 | 0.995 | n.s. |
| from 1 - from 3 | -3.01 | 3.63 | -0.83 | 0.408 | 0.995 | n.s. |
| from 1 - from 4 | -3.94 | 3.80 | -1.04 | 0.301 | 0.987 | n.s. |
| from 1 - from 5 | 2.43 | 3.62 | 0.67 | 0.502 | 0.995 | n.s. |
| from 1 - from 6 | -1.44 | 3.63 | -0.40 | 0.692 | 0.995 | n.s. |
| from 2 - from 3 | -2.58 | 3.52 | -0.73 | 0.463 | 0.995 | n.s. |
| from 2 - from 4 | -3.51 | 3.71 | -0.95 | 0.344 | 0.990 | n.s. |
| from 2 - from 5 | 2.86 | 3.57 | 0.80 | 0.424 | 0.995 | n.s. |
| from 2 - from 6 | -1.01 | 3.53 | -0.29 | 0.774 | 0.995 | n.s. |
| from 3 - from 4 | -0.93 | 3.61 | -0.26 | 0.797 | 0.995 | n.s. |
| from 3 - from 5 | 5.44 | 3.58 | 1.52 | 0.128 | 0.853 | n.s. |
| from 3 - from 6 | 1.57 | 3.55 | 0.44 | 0.659 | 0.995 | n.s. |
| from 4 - from 5 | 6.37 | 3.74 | 1.70 | 0.089 | 0.752 | n.s. |
| from 4 - from 6 | 2.50 | 3.75 | 0.67 | 0.505 | 0.995 | n.s. |
| from 5 - from 6 | -3.87 | 3.60 | -1.08 | 0.282 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.33, *p* = 0.896, η²_G = 0.012
- Greenhouse-Geisser corrected: *p* = 0.738 (ε = 0.428)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 1 vs from 2 | -0.21 | 15 | = 0.997 | -0.05 [-0.71, 0.33] | negligible | n.s. |
| from 1 vs from 3 | -0.06 | 15 | = 0.997 | -0.02 [-0.64, 0.39] | negligible | n.s. |
| from 1 vs from 4 | -1.11 | 15 | = 0.997 | -0.30 [-0.82, 0.27] | small | n.s. |
| from 1 vs from 5 | 0.57 | 15 | = 0.997 | 0.15 [-0.39, 0.65] | negligible | n.s. |
| from 1 vs from 6 | -0.03 | 15 | = 0.997 | -0.01 [-0.61, 0.42] | negligible | n.s. |
| from 2 vs from 3 | 0.14 | 15 | = 0.997 | 0.03 [-0.62, 0.38] | negligible | n.s. |
| from 2 vs from 4 | -1.33 | 15 | = 0.997 | -0.26 [-0.88, 0.22] | small | n.s. |
| from 2 vs from 5 | 0.70 | 15 | = 0.997 | 0.20 [-0.25, 0.80] | negligible | n.s. |
| from 2 vs from 6 | 0.06 | 15 | = 0.997 | 0.02 [-0.56, 0.44] | negligible | n.s. |
| from 3 vs from 4 | -0.91 | 15 | = 0.997 | -0.28 [-0.64, 0.39] | small | n.s. |
| from 3 vs from 5 | 0.70 | 15 | = 0.997 | 0.16 [-0.16, 0.86] | negligible | n.s. |
| from 3 vs from 6 | -0.00 | 15 | = 0.997 | -0.00 [-0.49, 0.51] | negligible | n.s. |
| from 4 vs from 5 | 1.65 | 15 | = 0.997 | 0.40 [-0.06, 1.02] | small | n.s. |
| from 4 vs from 6 | 0.62 | 15 | = 0.997 | 0.17 [-0.38, 0.69] | negligible | n.s. |
| from 5 vs from 6 | -0.31 | 15 | = 0.997 | -0.09 [-0.68, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - from 1 showed greater amplitude than from 5 (*d* = 0.49)
  - from 2 showed greater amplitude than from 5 (*d* = 0.73)
  - from 2 showed greater amplitude than from 6 (*d* = 0.47)
  - from 3 showed greater amplitude than from 5 (*d* = 0.52)
  - from 4 showed greater amplitude than from 5 (*d* = 0.42)
**P3b amplitude:** Significant main effect of condition (*p* = 0.048) (no significant pairwise comparisons)

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

- Python 3.12.4
- MNE-Python 1.9.0
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
