# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:13:21

---

## 1. Analysis Overview

**Total Measurements:** 291
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
| 5a3 | 19 | -4.42 µV | 2.32 | 0.53 | [-8.14, -0.91] |
| 5b3 | 14 | -5.87 µV | 4.05 | 1.08 | [-14.84, -0.24] |
| 5c3 | 16 | -4.45 µV | 3.23 | 0.81 | [-11.40, -0.87] |
| 5d3 | 20 | -4.20 µV | 2.45 | 0.55 | [-9.48, -0.10] |
| 5e3 | 14 | -5.50 µV | 3.20 | 0.85 | [-12.47, -0.91] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 19 | 178.01 ms | 11.85 | 2.72 | [156.43, 206.84] |
| 5b3 | 14 | 180.64 ms | 10.36 | 2.77 | [164.23, 197.46] |
| 5c3 | 16 | 176.80 ms | 8.56 | 2.14 | [165.66, 197.69] |
| 5d3 | 20 | 175.85 ms | 10.79 | 2.41 | [157.48, 210.54] |
| 5e3 | 14 | 181.80 ms | 10.42 | 2.78 | [166.33, 205.22] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 15 | 2.86 µV | 2.06 | 0.53 | [0.68, 6.99] |
| 5b3 | 8 | 3.60 µV | 3.70 | 1.31 | [0.36, 11.35] |
| 5c3 | 12 | 3.75 µV | 3.20 | 0.93 | [0.19, 9.77] |
| 5d3 | 12 | 1.86 µV | 1.56 | 0.45 | [0.11, 4.72] |
| 5e3 | 7 | 5.73 µV | 3.84 | 1.45 | [1.03, 11.92] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 15 | 101.38 ms | 7.89 | 2.04 | [85.30, 113.47] |
| 5b3 | 8 | 101.50 ms | 11.48 | 4.06 | [85.11, 118.69] |
| 5c3 | 12 | 102.38 ms | 9.89 | 2.86 | [80.04, 114.10] |
| 5d3 | 12 | 104.82 ms | 11.94 | 3.45 | [82.53, 118.83] |
| 5e3 | 7 | 104.57 ms | 6.32 | 2.39 | [98.02, 115.79] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 18 | 3.64 µV | 3.10 | 0.73 | [0.10, 11.74] |
| 5b3 | 11 | 4.11 µV | 2.41 | 0.73 | [1.75, 8.79] |
| 5c3 | 18 | 4.65 µV | 2.82 | 0.67 | [0.96, 10.41] |
| 5d3 | 18 | 5.90 µV | 2.44 | 0.58 | [1.70, 10.21] |
| 5e3 | 10 | 5.19 µV | 3.63 | 1.15 | [0.67, 13.30] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 18 | 472.77 ms | 17.24 | 4.06 | [433.11, 505.43] |
| 5b3 | 11 | 475.51 ms | 8.00 | 2.41 | [461.76, 488.10] |
| 5c3 | 18 | 475.67 ms | 10.86 | 2.56 | [454.22, 500.34] |
| 5d3 | 18 | 474.28 ms | 13.49 | 3.18 | [452.84, 509.28] |
| 5e3 | 10 | 469.21 ms | 18.99 | 6.01 | [433.26, 497.53] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 379.11, BIC = 398.46
- **5b3 vs 5a3**: *β* = -1.49, *SE* = 0.722, *z* = -2.064, *p* = 0.039
- **5c3 vs 5a3**: *β* = -0.54, *SE* = 0.706, *z* = -0.765, *p* = 0.444
- **5d3 vs 5a3**: *β* = -0.04, *SE* = 0.654, *z* = -0.067, *p* = 0.946
- **5e3 vs 5a3**: *β* = -1.34, *SE* = 0.727, *z* = -1.847, *p* = 0.065
- **SNR**: *β* = -0.98, *SE* = 0.123, *z* = -7.970, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 1.49 | 0.72 | 2.06 | 0.039 | 0.329 | n.s. |
| 5a3 - 5c3 | 0.54 | 0.71 | 0.76 | 0.444 | 0.905 | n.s. |
| 5a3 - 5d3 | 0.04 | 0.65 | 0.07 | 0.946 | 0.978 | n.s. |
| 5a3 - 5e3 | 1.34 | 0.73 | 1.85 | 0.065 | 0.415 | n.s. |
| 5b3 - 5c3 | -0.95 | 0.76 | -1.25 | 0.212 | 0.760 | n.s. |
| 5b3 - 5d3 | -1.45 | 0.71 | -2.03 | 0.043 | 0.329 | n.s. |
| 5b3 - 5e3 | -0.15 | 0.79 | -0.19 | 0.852 | 0.978 | n.s. |
| 5c3 - 5d3 | -0.50 | 0.69 | -0.72 | 0.473 | 0.905 | n.s. |
| 5c3 - 5e3 | 0.80 | 0.78 | 1.03 | 0.303 | 0.836 | n.s. |
| 5d3 - 5e3 | 1.30 | 0.72 | 1.79 | 0.073 | 0.415 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.18, *p* = 0.943, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.15 | 3 | = 0.889 | 0.11 [-0.06, 1.34] | negligible | n.s. |
| 5a3 vs 5c3 | -0.28 | 3 | = 0.889 | -0.19 [-0.75, 0.52] | negligible | n.s. |
| 5a3 vs 5d3 | 0.29 | 3 | = 0.889 | 0.19 [-0.60, 0.47] | negligible | n.s. |
| 5a3 vs 5e3 | 0.32 | 3 | = 0.889 | 0.28 [-0.42, 0.87] | small | n.s. |
| 5b3 vs 5c3 | -0.45 | 3 | = 0.889 | -0.24 [-0.90, 0.65] | small | n.s. |
| 5b3 vs 5d3 | 0.32 | 3 | = 0.889 | 0.09 [-1.07, 0.20] | negligible | n.s. |
| 5b3 vs 5e3 | 0.43 | 3 | = 0.889 | 0.20 [-0.86, 0.68] | negligible | n.s. |
| 5c3 vs 5d3 | 0.79 | 3 | = 0.889 | 0.28 [-0.63, 0.57] | small | n.s. |
| 5c3 vs 5e3 | 0.59 | 3 | = 0.889 | 0.34 [-0.87, 0.81] | small | n.s. |
| 5d3 vs 5e3 | 0.24 | 3 | = 0.889 | 0.12 [-0.36, 0.93] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 632.50, BIC = 651.85
- **5b3 vs 5a3**: *β* = 2.87, *SE* = 3.321, *z* = 0.865, *p* = 0.387
- **5c3 vs 5a3**: *β* = -1.44, *SE* = 3.214, *z* = -0.448, *p* = 0.654
- **5d3 vs 5a3**: *β* = -2.60, *SE* = 3.007, *z* = -0.865, *p* = 0.387
- **5e3 vs 5a3**: *β* = 3.01, *SE* = 3.328, *z* = 0.904, *p* = 0.366
- **SNR**: *β* = -0.85, *SE* = 0.564, *z* = -1.512, *p* = 0.130

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -2.87 | 3.32 | -0.86 | 0.387 | 0.935 | n.s. |
| 5a3 - 5c3 | 1.44 | 3.21 | 0.45 | 0.654 | 0.959 | n.s. |
| 5a3 - 5d3 | 2.60 | 3.01 | 0.87 | 0.387 | 0.935 | n.s. |
| 5a3 - 5e3 | -3.01 | 3.33 | -0.90 | 0.366 | 0.935 | n.s. |
| 5b3 - 5c3 | 4.31 | 3.48 | 1.24 | 0.216 | 0.838 | n.s. |
| 5b3 - 5d3 | 5.48 | 3.29 | 1.66 | 0.096 | 0.602 | n.s. |
| 5b3 - 5e3 | -0.14 | 3.60 | -0.04 | 0.970 | 0.970 | n.s. |
| 5c3 - 5d3 | 1.16 | 3.17 | 0.37 | 0.714 | 0.959 | n.s. |
| 5c3 - 5e3 | -4.45 | 3.50 | -1.27 | 0.203 | 0.838 | n.s. |
| 5d3 - 5e3 | -5.61 | 3.29 | -1.71 | 0.088 | 0.602 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.65, *p* = 0.639, η²_G = 0.073
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.50 | 3 | = 0.816 | 0.16 [-0.73, 0.54] | negligible | n.s. |
| 5a3 vs 5c3 | 1.26 | 3 | = 0.816 | 0.45 [-0.42, 0.87] | small | n.s. |
| 5a3 vs 5d3 | -0.66 | 3 | = 0.816 | -0.36 [-0.42, 0.65] | small | n.s. |
| 5a3 vs 5e3 | 1.16 | 3 | = 0.816 | 0.27 [-0.68, 0.59] | small | n.s. |
| 5b3 vs 5c3 | 0.67 | 3 | = 0.816 | 0.19 [0.00, 1.83] | negligible | n.s. |
| 5b3 vs 5d3 | -0.61 | 3 | = 0.816 | -0.44 [-0.24, 1.01] | small | n.s. |
| 5b3 vs 5e3 | 0.23 | 3 | = 0.835 | 0.06 [-0.98, 0.58] | negligible | n.s. |
| 5c3 vs 5d3 | -1.16 | 3 | = 0.816 | -0.86 [-0.58, 0.63] | large | n.s. |
| 5c3 vs 5e3 | -0.36 | 3 | = 0.822 | -0.14 [-1.26, 0.48] | negligible | n.s. |
| 5d3 vs 5e3 | 0.88 | 3 | = 0.816 | 0.62 [-0.92, 0.37] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 225.61, BIC = 241.52
- **5b3 vs 5a3**: *β* = 0.65, *SE* = 0.724, *z* = 0.903, *p* = 0.367
- **5c3 vs 5a3**: *β* = 0.66, *SE* = 0.637, *z* = 1.042, *p* = 0.297
- **5d3 vs 5a3**: *β* = 0.17, *SE* = 0.654, *z* = 0.263, *p* = 0.792
- **5e3 vs 5a3**: *β* = 2.40, *SE* = 0.763, *z* = 3.149, *p* = 0.002
- **SNR**: *β* = 1.80, *SE* = 0.197, *z* = 9.165, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -0.65 | 0.72 | -0.90 | 0.367 | 0.898 | n.s. |
| 5a3 - 5c3 | -0.66 | 0.64 | -1.04 | 0.297 | 0.880 | n.s. |
| 5a3 - 5d3 | -0.17 | 0.65 | -0.26 | 0.792 | 0.957 | n.s. |
| 5a3 - 5e3 | -2.40 | 0.76 | -3.15 | 0.002 | 0.016 | * |
| 5b3 - 5c3 | -0.01 | 0.76 | -0.01 | 0.990 | 0.990 | n.s. |
| 5b3 - 5d3 | 0.48 | 0.79 | 0.61 | 0.542 | 0.924 | n.s. |
| 5b3 - 5e3 | -1.75 | 0.87 | -2.01 | 0.044 | 0.272 | n.s. |
| 5c3 - 5d3 | 0.49 | 0.69 | 0.71 | 0.476 | 0.924 | n.s. |
| 5c3 - 5e3 | -1.74 | 0.79 | -2.20 | 0.028 | 0.202 | n.s. |
| 5d3 - 5e3 | -2.23 | 0.81 | -2.74 | 0.006 | 0.055 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 410.05, BIC = 425.96
- **5b3 vs 5a3**: *β* = 0.13, *SE* = 4.016, *z* = 0.033, *p* = 0.973
- **5c3 vs 5a3**: *β* = 1.05, *SE* = 3.557, *z* = 0.295, *p* = 0.768
- **5d3 vs 5a3**: *β* = 3.27, *SE* = 3.619, *z* = 0.902, *p* = 0.367
- **5e3 vs 5a3**: *β* = 3.12, *SE* = 4.253, *z* = 0.732, *p* = 0.464
- **SNR**: *β* = -0.26, *SE* = 1.129, *z* = -0.229, *p* = 0.819

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -0.13 | 4.02 | -0.03 | 0.973 | 0.999 | n.s. |
| 5a3 - 5c3 | -1.05 | 3.56 | -0.30 | 0.768 | 0.997 | n.s. |
| 5a3 - 5d3 | -3.27 | 3.62 | -0.90 | 0.367 | 0.990 | n.s. |
| 5a3 - 5e3 | -3.12 | 4.25 | -0.73 | 0.464 | 0.996 | n.s. |
| 5b3 - 5c3 | -0.92 | 4.21 | -0.22 | 0.828 | 0.997 | n.s. |
| 5b3 - 5d3 | -3.13 | 4.27 | -0.73 | 0.463 | 0.996 | n.s. |
| 5b3 - 5e3 | -2.98 | 4.82 | -0.62 | 0.536 | 0.996 | n.s. |
| 5c3 - 5d3 | -2.21 | 3.84 | -0.58 | 0.564 | 0.996 | n.s. |
| 5c3 - 5e3 | -2.06 | 4.41 | -0.47 | 0.640 | 0.996 | n.s. |
| 5d3 - 5e3 | 0.15 | 4.49 | 0.03 | 0.973 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 351.80, BIC = 370.34
- **5b3 vs 5a3**: *β* = 0.83, *SE* = 0.826, *z* = 1.006, *p* = 0.314
- **5c3 vs 5a3**: *β* = 1.21, *SE* = 0.707, *z* = 1.706, *p* = 0.088
- **5d3 vs 5a3**: *β* = 1.85, *SE* = 0.708, *z* = 2.610, *p* = 0.009
- **5e3 vs 5a3**: *β* = 2.04, *SE* = 0.854, *z* = 2.383, *p* = 0.017
- **SNR**: *β* = 0.64, *SE* = 0.115, *z* = 5.541, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -0.83 | 0.83 | -1.01 | 0.314 | 0.848 | n.s. |
| 5a3 - 5c3 | -1.21 | 0.71 | -1.71 | 0.088 | 0.521 | n.s. |
| 5a3 - 5d3 | -1.85 | 0.71 | -2.61 | 0.009 | 0.087 | n.s. |
| 5a3 - 5e3 | -2.04 | 0.85 | -2.38 | 0.017 | 0.144 | n.s. |
| 5b3 - 5c3 | -0.38 | 0.82 | -0.46 | 0.648 | 0.876 | n.s. |
| 5b3 - 5d3 | -1.02 | 0.83 | -1.22 | 0.223 | 0.792 | n.s. |
| 5b3 - 5e3 | -1.20 | 0.94 | -1.28 | 0.201 | 0.792 | n.s. |
| 5c3 - 5d3 | -0.64 | 0.70 | -0.91 | 0.363 | 0.848 | n.s. |
| 5c3 - 5e3 | -0.83 | 0.85 | -0.97 | 0.332 | 0.848 | n.s. |
| 5d3 - 5e3 | -0.19 | 0.86 | -0.22 | 0.828 | 0.876 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.25, *p* = 0.907, η²_G = 0.049
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.39 | 3 | = 0.993 | 0.32 [-0.75, 0.78] | small | n.s. |
| 5a3 vs 5c3 | -0.01 | 3 | = 0.993 | -0.01 [-0.86, 0.27] | negligible | n.s. |
| 5a3 vs 5d3 | -0.28 | 3 | = 0.993 | -0.21 [-1.01, 0.15] | small | n.s. |
| 5a3 vs 5e3 | -0.23 | 3 | = 0.993 | -0.19 [-0.79, 0.64] | negligible | n.s. |
| 5b3 vs 5c3 | -0.66 | 3 | = 0.993 | -0.37 [-1.07, 0.50] | small | n.s. |
| 5b3 vs 5d3 | -1.55 | 3 | = 0.993 | -0.74 [-2.21, -0.07] | medium | n.s. |
| 5b3 vs 5e3 | -0.77 | 3 | = 0.993 | -0.55 [-1.31, 0.82] | medium | n.s. |
| 5c3 vs 5d3 | -1.03 | 3 | = 0.993 | -0.23 [-1.03, 0.06] | small | n.s. |
| 5c3 vs 5e3 | -0.61 | 3 | = 0.993 | -0.19 [-1.21, 0.52] | negligible | n.s. |
| 5d3 vs 5e3 | -0.05 | 3 | = 0.993 | -0.02 [-0.89, 0.79] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 620.94, BIC = 639.48
- **5b3 vs 5a3**: *β* = 3.01, *SE* = 5.263, *z* = 0.571, *p* = 0.568
- **5c3 vs 5a3**: *β* = 3.05, *SE* = 4.564, *z* = 0.669, *p* = 0.503
- **5d3 vs 5a3**: *β* = 1.33, *SE* = 4.604, *z* = 0.289, *p* = 0.772
- **5e3 vs 5a3**: *β* = -3.14, *SE* = 5.483, *z* = -0.572, *p* = 0.567
- **SNR**: *β* = 0.39, *SE* = 0.700, *z* = 0.553, *p* = 0.580

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -3.01 | 5.26 | -0.57 | 0.568 | 0.993 | n.s. |
| 5a3 - 5c3 | -3.05 | 4.56 | -0.67 | 0.503 | 0.993 | n.s. |
| 5a3 - 5d3 | -1.33 | 4.60 | -0.29 | 0.772 | 0.993 | n.s. |
| 5a3 - 5e3 | 3.14 | 5.48 | 0.57 | 0.567 | 0.993 | n.s. |
| 5b3 - 5c3 | -0.05 | 5.27 | -0.01 | 0.993 | 0.993 | n.s. |
| 5b3 - 5d3 | 1.68 | 5.38 | 0.31 | 0.756 | 0.993 | n.s. |
| 5b3 - 5e3 | 6.15 | 6.08 | 1.01 | 0.312 | 0.965 | n.s. |
| 5c3 - 5d3 | 1.72 | 4.61 | 0.37 | 0.709 | 0.993 | n.s. |
| 5c3 - 5e3 | 6.19 | 5.43 | 1.14 | 0.254 | 0.947 | n.s. |
| 5d3 - 5e3 | 4.47 | 5.49 | 0.81 | 0.416 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.767, η²_G = 0.126
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -1.36 | 3 | = 0.881 | -1.18 [-0.93, 0.62] | large | n.s. |
| 5a3 vs 5c3 | -0.65 | 3 | = 0.881 | -0.49 [-0.61, 0.50] | small | n.s. |
| 5a3 vs 5d3 | -1.47 | 3 | = 0.881 | -1.05 [-0.65, 0.46] | large | n.s. |
| 5a3 vs 5e3 | -0.71 | 3 | = 0.881 | -0.61 [-0.61, 0.83] | medium | n.s. |
| 5b3 vs 5c3 | 0.39 | 3 | = 0.881 | 0.33 [-0.55, 1.01] | small | n.s. |
| 5b3 vs 5d3 | -0.41 | 3 | = 0.881 | -0.20 [-1.01, 0.68] | negligible | n.s. |
| 5b3 vs 5e3 | 0.16 | 3 | = 0.881 | 0.12 [-0.59, 1.65] | negligible | n.s. |
| 5c3 vs 5d3 | -0.41 | 3 | = 0.881 | -0.41 [-0.22, 0.84] | small | n.s. |
| 5c3 vs 5e3 | -0.59 | 3 | = 0.881 | -0.14 [-0.67, 1.02] | negligible | n.s. |
| 5d3 vs 5e3 | 0.25 | 3 | = 0.881 | 0.23 [-0.73, 0.94] | small | n.s. |

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
