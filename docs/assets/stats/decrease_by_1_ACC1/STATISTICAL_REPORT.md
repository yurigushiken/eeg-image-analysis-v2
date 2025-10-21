# Statistical Analysis Report: tables

**Generated:** 2025-10-20 21:48:24

---

## 1. Analysis Overview

**Total Measurements:** 336
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
| 2 to 1 | 15 | -2.86 µV | 1.99 | 0.51 | [-8.13, -0.37] |
| 3 to 2 | 22 | -3.91 µV | 2.03 | 0.43 | [-8.19, -0.50] |
| 4 to 3 | 23 | -3.97 µV | 1.91 | 0.40 | [-8.43, -0.78] |
| 5 to 4 | 22 | -3.91 µV | 2.14 | 0.46 | [-7.91, -0.71] |
| 6 to 5 | 15 | -4.38 µV | 1.58 | 0.41 | [-6.46, -1.57] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 15 | 179.53 ms | 8.82 | 2.28 | [159.73, 191.09] |
| 3 to 2 | 22 | 174.68 ms | 9.94 | 2.12 | [157.64, 198.60] |
| 4 to 3 | 23 | 175.50 ms | 10.78 | 2.25 | [157.10, 205.65] |
| 5 to 4 | 22 | 178.53 ms | 9.85 | 2.10 | [164.00, 200.92] |
| 6 to 5 | 15 | 174.56 ms | 12.97 | 3.35 | [155.42, 197.03] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 3.57 µV | 2.54 | 0.62 | [1.07, 8.49] |
| 3 to 2 | 9 | 2.06 µV | 1.50 | 0.50 | [0.01, 4.07] |
| 4 to 3 | 11 | 1.79 µV | 1.29 | 0.39 | [0.28, 4.76] |
| 5 to 4 | 16 | 2.06 µV | 1.81 | 0.45 | [0.02, 5.16] |
| 6 to 5 | 4 | 1.92 µV | 1.07 | 0.53 | [0.91, 2.93] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 111.04 ms | 2.05 | 0.50 | [106.76, 114.36] |
| 3 to 2 | 9 | 109.04 ms | 3.00 | 1.00 | [102.34, 113.00] |
| 4 to 3 | 11 | 109.49 ms | 3.44 | 1.04 | [104.03, 115.03] |
| 5 to 4 | 16 | 110.07 ms | 4.57 | 1.14 | [100.12, 118.16] |
| 6 to 5 | 4 | 112.99 ms | 3.67 | 1.84 | [110.29, 118.33] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 22 | 3.85 µV | 3.03 | 0.65 | [0.08, 9.97] |
| 3 to 2 | 17 | 4.56 µV | 3.01 | 0.73 | [0.92, 12.40] |
| 4 to 3 | 19 | 4.12 µV | 2.78 | 0.64 | [0.19, 9.37] |
| 5 to 4 | 21 | 3.66 µV | 2.72 | 0.59 | [0.71, 8.99] |
| 6 to 5 | 11 | 3.04 µV | 1.67 | 0.50 | [0.20, 5.70] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 22 | 500.85 ms | 22.90 | 4.88 | [444.20, 545.91] |
| 3 to 2 | 17 | 499.09 ms | 15.40 | 3.73 | [473.82, 538.95] |
| 4 to 3 | 19 | 495.04 ms | 13.27 | 3.04 | [468.16, 524.69] |
| 5 to 4 | 21 | 497.08 ms | 18.21 | 3.97 | [461.59, 534.43] |
| 6 to 5 | 11 | 510.37 ms | 29.57 | 8.92 | [464.74, 554.28] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 356.70, BIC = 377.30
- **3 to 2 vs 2 to 1**: *β* = -0.73, *SE* = 0.432, *z* = -1.682, *p* = 0.093
- **4 to 3 vs 2 to 1**: *β* = -0.84, *SE* = 0.432, *z* = -1.949, *p* = 0.051
- **5 to 4 vs 2 to 1**: *β* = -0.83, *SE* = 0.433, *z* = -1.912, *p* = 0.056
- **6 to 5 vs 2 to 1**: *β* = -1.83, *SE* = 0.468, *z* = -3.906, *p* < .001
- **SNR**: *β* = -0.43, *SE* = 0.056, *z* = -7.712, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.73 | 0.43 | 1.68 | 0.093 | 0.322 | n.s. |
| 2 to 1 - 4 to 3 | 0.84 | 0.43 | 1.95 | 0.051 | 0.271 | n.s. |
| 2 to 1 - 5 to 4 | 0.83 | 0.43 | 1.91 | 0.056 | 0.271 | n.s. |
| 2 to 1 - 6 to 5 | 1.83 | 0.47 | 3.91 | < .001 | < .001 | *** |
| 3 to 2 - 4 to 3 | 0.12 | 0.37 | 0.31 | 0.754 | 0.985 | n.s. |
| 3 to 2 - 5 to 4 | 0.10 | 0.37 | 0.27 | 0.788 | 0.985 | n.s. |
| 3 to 2 - 6 to 5 | 1.10 | 0.43 | 2.59 | 0.010 | 0.083 | n.s. |
| 4 to 3 - 5 to 4 | -0.02 | 0.37 | -0.04 | 0.967 | 0.985 | n.s. |
| 4 to 3 - 6 to 5 | 0.99 | 0.42 | 2.34 | 0.019 | 0.137 | n.s. |
| 5 to 4 - 6 to 5 | 1.00 | 0.42 | 2.36 | 0.018 | 0.137 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.82, *p* = 0.041, η²_G = 0.189
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 6.00 | 8 | = 0.003 | 1.24 [0.39, 1.86] | large | ** |
| 2 to 1 vs 4 to 3 | 2.40 | 8 | = 0.145 | 1.08 [-0.06, 1.18] | large | n.s. |
| 2 to 1 vs 5 to 4 | 2.17 | 8 | = 0.154 | 1.26 [0.03, 1.31] | large | n.s. |
| 2 to 1 vs 6 to 5 | 3.92 | 8 | = 0.022 | 1.38 [0.34, 2.29] | large | * |
| 3 to 2 vs 4 to 3 | -0.23 | 8 | = 1.000 | -0.10 [-0.28, 0.64] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.12 | 8 | = 1.000 | 0.06 [-0.42, 0.49] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.00 | 8 | = 1.000 | 0.00 [-0.29, 0.89] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 0.40 | 8 | = 1.000 | 0.16 [-0.54, 0.37] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.41 | 8 | = 1.000 | 0.11 [-0.29, 0.83] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.14 | 8 | = 1.000 | -0.07 [-0.41, 0.75] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 713.40, BIC = 734.00
- **3 to 2 vs 2 to 1**: *β* = -2.88, *SE* = 2.531, *z* = -1.137, *p* = 0.256
- **4 to 3 vs 2 to 1**: *β* = -3.32, *SE* = 2.522, *z* = -1.316, *p* = 0.188
- **5 to 4 vs 2 to 1**: *β* = 1.03, *SE* = 2.525, *z* = 0.406, *p* = 0.685
- **6 to 5 vs 2 to 1**: *β* = -4.90, *SE* = 2.731, *z* = -1.795, *p* = 0.073
- **SNR**: *β* = -0.30, *SE* = 0.341, *z* = -0.877, *p* = 0.380

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 2.88 | 2.53 | 1.14 | 0.256 | 0.771 | n.s. |
| 2 to 1 - 4 to 3 | 3.32 | 2.52 | 1.32 | 0.188 | 0.713 | n.s. |
| 2 to 1 - 5 to 4 | -1.03 | 2.52 | -0.41 | 0.685 | 0.901 | n.s. |
| 2 to 1 - 6 to 5 | 4.90 | 2.73 | 1.80 | 0.073 | 0.453 | n.s. |
| 3 to 2 - 4 to 3 | 0.44 | 2.18 | 0.20 | 0.839 | 0.901 | n.s. |
| 3 to 2 - 5 to 4 | -3.90 | 2.19 | -1.78 | 0.075 | 0.453 | n.s. |
| 3 to 2 - 6 to 5 | 2.03 | 2.51 | 0.81 | 0.420 | 0.887 | n.s. |
| 4 to 3 - 5 to 4 | -4.35 | 2.18 | -1.99 | 0.046 | 0.346 | n.s. |
| 4 to 3 - 6 to 5 | 1.58 | 2.49 | 0.64 | 0.524 | 0.892 | n.s. |
| 5 to 4 - 6 to 5 | 5.93 | 2.51 | 2.36 | 0.018 | 0.168 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.401, η²_G = 0.045
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.68 | 8 | = 0.736 | 0.26 [-0.26, 0.92] | small | n.s. |
| 2 to 1 vs 4 to 3 | 2.73 | 8 | = 0.129 | 0.67 [-0.11, 1.11] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 0.13 | 8 | = 0.942 | 0.03 [-0.54, 0.62] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 0.86 | 8 | = 0.736 | 0.26 [-0.40, 1.07] | small | n.s. |
| 3 to 2 vs 4 to 3 | 0.86 | 8 | = 0.736 | 0.36 [-0.33, 0.58] | small | n.s. |
| 3 to 2 vs 5 to 4 | -0.54 | 8 | = 0.756 | -0.20 [-0.81, 0.13] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.08 | 8 | = 0.942 | 0.03 [-0.48, 0.68] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -3.58 | 8 | = 0.072 | -0.55 [-1.17, -0.17] | medium | n.s. |
| 4 to 3 vs 6 to 5 | -1.12 | 8 | = 0.736 | -0.28 [-0.47, 0.64] | small | n.s. |
| 5 to 4 vs 6 to 5 | 0.80 | 8 | = 0.736 | 0.21 [-0.07, 1.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 204.13, BIC = 220.47
- **3 to 2 vs 2 to 1**: *β* = -0.64, *SE* = 0.526, *z* = -1.217, *p* = 0.224
- **4 to 3 vs 2 to 1**: *β* = -1.02, *SE* = 0.491, *z* = -2.082, *p* = 0.037
- **5 to 4 vs 2 to 1**: *β* = -0.56, *SE* = 0.447, *z* = -1.244, *p* = 0.214
- **6 to 5 vs 2 to 1**: *β* = -0.98, *SE* = 0.766, *z* = -1.282, *p* = 0.200
- **SNR**: *β* = 0.53, *SE* = 0.080, *z* = 6.644, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.64 | 0.53 | 1.22 | 0.224 | 0.865 | n.s. |
| 2 to 1 - 4 to 3 | 1.02 | 0.49 | 2.08 | 0.037 | 0.317 | n.s. |
| 2 to 1 - 5 to 4 | 0.56 | 0.45 | 1.24 | 0.214 | 0.865 | n.s. |
| 2 to 1 - 6 to 5 | 0.98 | 0.77 | 1.28 | 0.200 | 0.865 | n.s. |
| 3 to 2 - 4 to 3 | 0.38 | 0.53 | 0.72 | 0.468 | 0.958 | n.s. |
| 3 to 2 - 5 to 4 | -0.08 | 0.49 | -0.17 | 0.866 | 0.982 | n.s. |
| 3 to 2 - 6 to 5 | 0.34 | 0.74 | 0.46 | 0.643 | 0.958 | n.s. |
| 4 to 3 - 5 to 4 | -0.47 | 0.46 | -1.02 | 0.307 | 0.889 | n.s. |
| 4 to 3 - 6 to 5 | -0.04 | 0.72 | -0.06 | 0.956 | 0.982 | n.s. |
| 5 to 4 - 6 to 5 | 0.43 | 0.70 | 0.61 | 0.542 | 0.958 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.18, *p* = 0.145, η²_G = 0.669
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.11 | 1 | = 0.563 | 2.97 [0.01, 2.48] | large | n.s. |
| 2 to 1 vs 4 to 3 | 6.71 | 1 | = 0.374 | 2.10 [0.13, 2.36] | large | n.s. |
| 2 to 1 vs 5 to 4 | 5.90 | 1 | = 0.374 | 2.40 [0.01, 1.44] | large | n.s. |
| 2 to 1 vs 6 to 5 | 4.60 | 1 | = 0.374 | 4.19 [-3.37, 11.14] | large | n.s. |
| 3 to 2 vs 4 to 3 | 0.04 | 1 | = 0.972 | 0.06 [-0.90, 1.21] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.47 | 1 | = 0.932 | 0.62 [-0.97, 0.88] | medium | n.s. |
| 3 to 2 vs 6 to 5 | 0.42 | 1 | = 0.932 | 0.46 [-2.07, 3.50] | small | n.s. |
| 4 to 3 vs 5 to 4 | 4.18 | 1 | = 0.374 | 0.47 [-0.99, 0.46] | small | n.s. |
| 4 to 3 vs 6 to 5 | 0.18 | 1 | = 0.972 | 0.17 [-1.25, 2.07] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | -0.49 | 1 | = 0.932 | -0.47 [-1.30, 1.97] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 311.73, BIC = 328.08
- **3 to 2 vs 2 to 1**: *β* = -1.89, *SE* = 1.333, *z* = -1.419, *p* = 0.156
- **4 to 3 vs 2 to 1**: *β* = -1.63, *SE* = 1.251, *z* = -1.306, *p* = 0.192
- **5 to 4 vs 2 to 1**: *β* = -0.98, *SE* = 1.135, *z* = -0.865, *p* = 0.387
- **6 to 5 vs 2 to 1**: *β* = 1.86, *SE* = 1.815, *z* = 1.028, *p* = 0.304
- **SNR**: *β* = 0.08, *SE* = 0.195, *z* = 0.403, *p* = 0.687

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 1.89 | 1.33 | 1.42 | 0.156 | 0.695 | n.s. |
| 2 to 1 - 4 to 3 | 1.63 | 1.25 | 1.31 | 0.192 | 0.721 | n.s. |
| 2 to 1 - 5 to 4 | 0.98 | 1.13 | 0.86 | 0.387 | 0.859 | n.s. |
| 2 to 1 - 6 to 5 | -1.86 | 1.81 | -1.03 | 0.304 | 0.837 | n.s. |
| 3 to 2 - 4 to 3 | -0.26 | 1.39 | -0.19 | 0.853 | 0.859 | n.s. |
| 3 to 2 - 5 to 4 | -0.91 | 1.29 | -0.71 | 0.479 | 0.859 | n.s. |
| 3 to 2 - 6 to 5 | -3.76 | 1.86 | -2.02 | 0.044 | 0.361 | n.s. |
| 4 to 3 - 5 to 4 | -0.65 | 1.19 | -0.55 | 0.585 | 0.859 | n.s. |
| 4 to 3 - 6 to 5 | -3.50 | 1.80 | -1.95 | 0.052 | 0.380 | n.s. |
| 5 to 4 - 6 to 5 | -2.85 | 1.74 | -1.64 | 0.101 | 0.574 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.76, *p* = 0.601, η²_G = 0.328
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.49 | 1 | = 0.745 | 2.03 [-0.17, 2.06] | large | n.s. |
| 2 to 1 vs 4 to 3 | 1.76 | 1 | = 0.745 | 1.97 [-0.47, 1.27] | large | n.s. |
| 2 to 1 vs 5 to 4 | 0.80 | 1 | = 0.745 | 0.83 [-0.39, 0.90] | large | n.s. |
| 2 to 1 vs 6 to 5 | 0.57 | 1 | = 0.745 | 0.78 [-2.92, 2.20] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 1.89 | 1 | = 0.745 | 1.40 [-0.78, 1.36] | large | n.s. |
| 3 to 2 vs 5 to 4 | 0.71 | 1 | = 0.745 | 0.66 [-0.83, 1.02] | medium | n.s. |
| 3 to 2 vs 6 to 5 | -18.79 | 1 | = 0.338 | -1.09 [-3.57, 2.06] | large | n.s. |
| 4 to 3 vs 5 to 4 | 0.30 | 1 | = 0.814 | 0.20 [-0.95, 0.50] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | -2.29 | 1 | = 0.745 | -1.75 [-4.48, 0.77] | large | n.s. |
| 5 to 4 vs 6 to 5 | -0.82 | 1 | = 0.745 | -0.77 [-2.95, 0.95] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 368.74, BIC = 388.74
- **3 to 2 vs 2 to 1**: *β* = 0.45, *SE* = 0.468, *z* = 0.952, *p* = 0.341
- **4 to 3 vs 2 to 1**: *β* = -0.35, *SE* = 0.460, *z* = -0.770, *p* = 0.441
- **5 to 4 vs 2 to 1**: *β* = -0.41, *SE* = 0.440, *z* = -0.928, *p* = 0.353
- **6 to 5 vs 2 to 1**: *β* = -1.02, *SE* = 0.563, *z* = -1.815, *p* = 0.070
- **SNR**: *β* = 0.45, *SE* = 0.055, *z* = 8.257, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.45 | 0.47 | -0.95 | 0.341 | 0.844 | n.s. |
| 2 to 1 - 4 to 3 | 0.35 | 0.46 | 0.77 | 0.441 | 0.844 | n.s. |
| 2 to 1 - 5 to 4 | 0.41 | 0.44 | 0.93 | 0.353 | 0.844 | n.s. |
| 2 to 1 - 6 to 5 | 1.02 | 0.56 | 1.81 | 0.070 | 0.477 | n.s. |
| 3 to 2 - 4 to 3 | 0.80 | 0.49 | 1.64 | 0.102 | 0.528 | n.s. |
| 3 to 2 - 5 to 4 | 0.85 | 0.48 | 1.80 | 0.072 | 0.477 | n.s. |
| 3 to 2 - 6 to 5 | 1.47 | 0.58 | 2.51 | 0.012 | 0.115 | n.s. |
| 4 to 3 - 5 to 4 | 0.05 | 0.46 | 0.12 | 0.906 | 0.906 | n.s. |
| 4 to 3 - 6 to 5 | 0.67 | 0.60 | 1.11 | 0.266 | 0.844 | n.s. |
| 5 to 4 - 6 to 5 | 0.61 | 0.57 | 1.07 | 0.283 | 0.844 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.35, *p* = 0.023, η²_G = 0.219
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.18 | 7 | = 0.859 | 0.10 [-0.54, 0.49] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 0.58 | 7 | = 0.642 | 0.28 [-0.59, 0.41] | small | n.s. |
| 2 to 1 vs 5 to 4 | 1.04 | 7 | = 0.478 | 0.54 [-0.42, 0.52] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 3.37 | 7 | = 0.059 | 1.79 [-0.02, 1.49] | large | n.s. |
| 3 to 2 vs 4 to 3 | 0.67 | 7 | = 0.642 | 0.18 [-0.59, 0.48] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 1.36 | 7 | = 0.433 | 0.43 [-0.21, 0.89] | small | n.s. |
| 3 to 2 vs 6 to 5 | 3.54 | 7 | = 0.059 | 1.56 [0.16, 2.13] | large | n.s. |
| 4 to 3 vs 5 to 4 | 1.08 | 7 | = 0.478 | 0.25 [-0.29, 0.71] | small | n.s. |
| 4 to 3 vs 6 to 5 | 2.73 | 7 | = 0.097 | 1.25 [-0.18, 1.52] | large | n.s. |
| 5 to 4 vs 6 to 5 | 1.74 | 7 | = 0.314 | 0.85 [-0.14, 1.31] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 798.22, BIC = 818.22
- **3 to 2 vs 2 to 1**: *β* = -3.40, *SE* = 5.500, *z* = -0.619, *p* = 0.536
- **4 to 3 vs 2 to 1**: *β* = -5.80, *SE* = 5.375, *z* = -1.079, *p* = 0.281
- **5 to 4 vs 2 to 1**: *β* = -2.98, *SE* = 5.164, *z* = -0.578, *p* = 0.563
- **6 to 5 vs 2 to 1**: *β* = 10.59, *SE* = 6.452, *z* = 1.642, *p* = 0.101
- **SNR**: *β* = -0.46, *SE* = 0.589, *z* = -0.778, *p* = 0.437

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.40 | 5.50 | 0.62 | 0.536 | 0.979 | n.s. |
| 2 to 1 - 4 to 3 | 5.80 | 5.37 | 1.08 | 0.281 | 0.861 | n.s. |
| 2 to 1 - 5 to 4 | 2.98 | 5.16 | 0.58 | 0.563 | 0.979 | n.s. |
| 2 to 1 - 6 to 5 | -10.59 | 6.45 | -1.64 | 0.101 | 0.524 | n.s. |
| 3 to 2 - 4 to 3 | 2.40 | 5.72 | 0.42 | 0.675 | 0.979 | n.s. |
| 3 to 2 - 5 to 4 | -0.42 | 5.60 | -0.07 | 0.940 | 0.979 | n.s. |
| 3 to 2 - 6 to 5 | -14.00 | 6.82 | -2.05 | 0.040 | 0.289 | n.s. |
| 4 to 3 - 5 to 4 | -2.81 | 5.39 | -0.52 | 0.602 | 0.979 | n.s. |
| 4 to 3 - 6 to 5 | -16.39 | 6.82 | -2.40 | 0.016 | 0.151 | n.s. |
| 5 to 4 - 6 to 5 | -13.58 | 6.52 | -2.08 | 0.037 | 0.289 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.34, *p* = 0.003, η²_G = 0.401
- Greenhouse-Geisser corrected: *p* = 0.036 (ε = 0.346)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.00 | 7 | = 0.997 | 0.00 [-0.27, 0.78] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | -0.02 | 7 | = 0.997 | -0.01 [-0.21, 0.81] | negligible | n.s. |
| 2 to 1 vs 5 to 4 | -0.77 | 7 | = 0.664 | -0.37 [-0.39, 0.55] | small | n.s. |
| 2 to 1 vs 6 to 5 | -2.93 | 7 | = 0.109 | -1.53 [-1.34, 0.12] | large | n.s. |
| 3 to 2 vs 4 to 3 | -0.05 | 7 | = 0.997 | -0.01 [-0.46, 0.61] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.89 | 7 | = 0.664 | -0.32 [-0.55, 0.51] | small | n.s. |
| 3 to 2 vs 6 to 5 | -2.65 | 7 | = 0.109 | -1.46 [-1.49, 0.20] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.94 | 7 | = 0.664 | -0.36 [-0.68, 0.32] | small | n.s. |
| 4 to 3 vs 6 to 5 | -2.80 | 7 | = 0.109 | -1.52 [-1.90, -0.04] | large | n.s. |
| 5 to 4 vs 6 to 5 | -1.91 | 7 | = 0.243 | -1.23 [-1.19, 0.23] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.041). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 3 to 2 (*d* = 1.24)
  - 2 to 1 showed greater amplitude than 6 to 5 (*d* = 1.38)
**P3b amplitude:** Significant main effect of condition (*p* = 0.023) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.003) (no significant pairwise comparisons)

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
