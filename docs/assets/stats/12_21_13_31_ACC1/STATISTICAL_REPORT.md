# Statistical Analysis Report: tables

**Generated:** 2025-10-23 18:46:22

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| Decreasing 2 to 1 | 16 | -2.80 µV | 2.10 | 0.52 | [-8.27, 0.09] |
| Decreasing 3 to 1 | 19 | -2.78 µV | 2.31 | 0.53 | [-7.74, 0.11] |
| Increasing 1 to 2 | 22 | -3.37 µV | 1.73 | 0.37 | [-6.71, -0.58] |
| Increasing 1 to 3 | 24 | -3.92 µV | 1.90 | 0.39 | [-8.45, -0.95] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 16 | 179.01 ms | 8.32 | 2.08 | [160.92, 190.53] |
| Decreasing 3 to 1 | 19 | 183.00 ms | 12.05 | 2.76 | [162.68, 205.19] |
| Increasing 1 to 2 | 22 | 176.69 ms | 12.68 | 2.70 | [155.82, 205.51] |
| Increasing 1 to 3 | 24 | 178.26 ms | 10.04 | 2.05 | [158.09, 202.59] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 18 | 3.45 µV | 2.56 | 0.60 | [0.13, 8.35] |
| Decreasing 3 to 1 | 21 | 2.23 µV | 1.76 | 0.39 | [0.18, 7.32] |
| Increasing 1 to 2 | 11 | 1.02 µV | 0.83 | 0.25 | [0.01, 2.62] |
| Increasing 1 to 3 | 11 | 2.10 µV | 1.48 | 0.45 | [0.49, 4.40] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 18 | 115.49 ms | 4.89 | 1.15 | [105.44, 127.12] |
| Decreasing 3 to 1 | 21 | 115.26 ms | 6.79 | 1.48 | [100.88, 125.41] |
| Increasing 1 to 2 | 11 | 111.99 ms | 6.92 | 2.09 | [101.81, 122.29] |
| Increasing 1 to 3 | 11 | 111.53 ms | 3.26 | 0.98 | [106.58, 115.42] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 3.90 µV | 2.86 | 0.64 | [0.32, 9.60] |
| Decreasing 3 to 1 | 20 | 4.11 µV | 2.43 | 0.54 | [0.66, 10.32] |
| Increasing 1 to 2 | 16 | 3.74 µV | 2.73 | 0.68 | [0.17, 10.35] |
| Increasing 1 to 3 | 20 | 4.36 µV | 3.62 | 0.81 | [0.11, 12.40] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 484.71 ms | 16.01 | 3.58 | [458.72, 520.23] |
| Decreasing 3 to 1 | 20 | 475.94 ms | 12.17 | 2.72 | [457.21, 502.27] |
| Increasing 1 to 2 | 16 | 479.11 ms | 22.84 | 5.71 | [433.98, 532.95] |
| Increasing 1 to 3 | 20 | 472.79 ms | 17.93 | 4.01 | [418.51, 495.14] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.93, BIC = 297.69
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.45, *SE* = 0.377, *z* = -1.191, *p* = 0.234
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.33, *SE* = 0.372, *z* = -0.890, *p* = 0.373
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.49, *SE* = 0.377, *z* = -1.289, *p* = 0.197
- **SNR**: *β* = -0.48, *SE* = 0.059, *z* = -8.040, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.45 | 0.38 | 1.19 | 0.234 | 0.736 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.33 | 0.37 | 0.89 | 0.373 | 0.846 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.49 | 0.38 | 1.29 | 0.197 | 0.733 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -0.12 | 0.35 | -0.33 | 0.740 | 0.950 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.04 | 0.37 | 0.10 | 0.919 | 0.950 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.15 | 0.32 | 0.48 | 0.633 | 0.950 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.111, η²_G = 0.055
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.08 | 13 | = 0.941 | 0.02 [-0.56, 0.60] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.24 | 13 | = 0.357 | 0.35 [-0.16, 1.00] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.20 | 13 | = 0.238 | 0.57 [0.12, 1.32] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 0.92 | 13 | = 0.447 | 0.29 [-0.21, 0.77] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.90 | 13 | = 0.238 | 0.49 [0.06, 1.10] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 1.41 | 13 | = 0.357 | 0.29 [-0.16, 0.74] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 591.77, BIC = 608.53
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 4.18, *SE* = 2.274, *z* = 1.837, *p* = 0.066
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -2.25, *SE* = 2.236, *z* = -1.006, *p* = 0.314
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.67, *SE* = 2.275, *z* = -0.292, *p* = 0.770
- **SNR**: *β* = 0.04, *SE* = 0.386, *z* = 0.115, *p* = 0.909

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -4.18 | 2.27 | -1.84 | 0.066 | 0.240 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 2.25 | 2.24 | 1.01 | 0.314 | 0.678 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.66 | 2.27 | 0.29 | 0.770 | 0.770 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 6.43 | 2.15 | 2.99 | 0.003 | 0.017 | * |
| Decreasing 3 to 1 - Increasing 1 to 3 | 4.84 | 2.24 | 2.16 | 0.031 | 0.146 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -1.58 | 1.95 | -0.81 | 0.418 | 0.678 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.81, *p* = 0.052, η²_G = 0.048
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -1.88 | 13 | = 0.167 | -0.45 [-1.11, 0.11] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.70 | 13 | = 0.623 | 0.16 [-0.33, 0.79] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 0.12 | 13 | = 0.909 | 0.03 [-0.44, 0.63] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 2.57 | 13 | = 0.073 | 0.54 [0.15, 1.23] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.55 | 13 | = 0.073 | 0.44 [0.02, 1.05] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.66 | 13 | = 0.623 | -0.13 [-0.60, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 213.65, BIC = 228.43
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.62, *SE* = 0.403, *z* = -1.533, *p* = 0.125
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -1.35, *SE* = 0.496, *z* = -2.721, *p* = 0.007
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.70, *SE* = 0.489, *z* = -1.437, *p* = 0.151
- **SNR**: *β* = 0.46, *SE* = 0.061, *z* = 7.489, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.62 | 0.40 | 1.53 | 0.125 | 0.461 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 1.35 | 0.50 | 2.72 | 0.007 | 0.038 | * |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.70 | 0.49 | 1.44 | 0.151 | 0.461 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 0.73 | 0.47 | 1.57 | 0.116 | 0.461 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.08 | 0.47 | 0.18 | 0.856 | 0.856 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.65 | 0.53 | -1.22 | 0.221 | 0.461 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.43, *p* = 0.020, η²_G = 0.344
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.73 | 5 | = 0.497 | 0.36 [-0.14, 0.97] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.75 | 5 | = 0.083 | 1.59 [0.18, 2.19] | large | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.72 | 5 | = 0.083 | 1.04 [-0.06, 1.55] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 3.25 | 5 | = 0.083 | 1.55 [0.08, 1.79] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.38 | 5 | = 0.305 | 0.81 [-0.33, 1.06] | large | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.29 | 5 | = 0.305 | -0.85 [-1.43, 0.51] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 397.32, BIC = 412.10
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.18, *SE* = 1.833, *z* = -0.096, *p* = 0.923
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -3.41, *SE* = 2.271, *z* = -1.500, *p* = 0.134
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -3.90, *SE* = 2.274, *z* = -1.713, *p* = 0.087
- **SNR**: *β* = 0.04, *SE* = 0.250, *z* = 0.161, *p* = 0.872

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.18 | 1.83 | 0.10 | 0.923 | 0.974 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 3.41 | 2.27 | 1.50 | 0.134 | 0.437 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 3.90 | 2.27 | 1.71 | 0.087 | 0.420 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 3.23 | 2.19 | 1.48 | 0.140 | 0.437 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 3.72 | 2.24 | 1.66 | 0.096 | 0.420 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.49 | 2.41 | 0.20 | 0.839 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.51, *p* = 0.098, η²_G = 0.293
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.03 | 5 | = 0.976 | 0.02 [-0.65, 0.42] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.95 | 5 | = 0.265 | 1.14 [-0.09, 1.67] | large | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.42 | 5 | = 0.265 | 1.43 [-0.15, 1.42] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.40 | 5 | = 0.333 | 1.03 [-0.29, 1.21] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.79 | 5 | = 0.265 | 1.22 [0.03, 1.57] | large | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.21 | 5 | = 0.976 | -0.06 [-0.65, 1.24] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 354.40, BIC = 370.72
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.62, *SE* = 0.655, *z* = -0.951, *p* = 0.342
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.31, *SE* = 0.677, *z* = -0.460, *p* = 0.646
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = 0.27, *SE* = 0.645, *z* = 0.411, *p* = 0.681
- **SNR**: *β* = 0.30, *SE* = 0.057, *z* = 5.382, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.62 | 0.65 | 0.95 | 0.342 | 0.876 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.31 | 0.68 | 0.46 | 0.646 | 0.955 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | -0.27 | 0.64 | -0.41 | 0.681 | 0.955 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -0.31 | 0.70 | -0.45 | 0.656 | 0.955 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.89 | 0.65 | -1.37 | 0.170 | 0.674 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.58 | 0.69 | -0.83 | 0.404 | 0.876 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.87, *p* = 0.466, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.17 | 13 | = 0.864 | -0.05 [-0.54, 0.42] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.46 | 13 | = 0.782 | 0.15 [-0.44, 0.63] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | -0.96 | 13 | = 0.782 | -0.31 [-0.67, 0.36] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 0.60 | 13 | = 0.782 | 0.21 [-0.33, 0.75] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.88 | 13 | = 0.782 | -0.27 [-0.65, 0.35] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.90 | 13 | = 0.476 | -0.44 [-1.12, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 650.31, BIC = 666.62
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -9.18, *SE* = 4.497, *z* = -2.041, *p* = 0.041
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -4.63, *SE* = 4.665, *z* = -0.992, *p* = 0.321
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -10.06, *SE* = 4.485, *z* = -2.244, *p* = 0.025
- **SNR**: *β* = 0.18, *SE* = 0.383, *z* = 0.471, *p* = 0.638

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 9.18 | 4.50 | 2.04 | 0.041 | 0.190 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 4.63 | 4.66 | 0.99 | 0.321 | 0.688 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 10.06 | 4.48 | 2.24 | 0.025 | 0.140 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -4.55 | 4.79 | -0.95 | 0.343 | 0.688 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.89 | 4.50 | 0.20 | 0.844 | 0.844 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 5.44 | 4.75 | 1.14 | 0.253 | 0.688 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.788, η²_G = 0.013
- Greenhouse-Geisser corrected: *p* = 0.704 (ε = 0.660)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 1.80 | 13 | = 0.568 | 0.39 [0.09, 1.15] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.50 | 13 | = 0.947 | 0.17 [-0.38, 0.69] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 1.12 | 13 | = 0.843 | 0.31 [-0.20, 0.86] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | -0.23 | 13 | = 0.947 | -0.08 [-0.73, 0.35] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 0.07 | 13 | = 0.947 | 0.02 [-0.46, 0.53] | negligible | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.29 | 13 | = 0.947 | 0.09 [-0.50, 0.66] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Marginal trend toward condition differences (*p* = 0.052)
**P1 amplitude:** Significant main effect of condition (*p* = 0.020) (no significant pairwise comparisons)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.098)

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
