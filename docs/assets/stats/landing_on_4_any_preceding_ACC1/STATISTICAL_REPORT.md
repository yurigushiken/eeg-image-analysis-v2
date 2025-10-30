# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:57:29

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
| 1 to 4 | 22 | -4.69 µV | 2.82 | 0.60 | [-10.85, -0.31] |
| 2 to 4 | 21 | -4.37 µV | 2.10 | 0.46 | [-10.88, -1.48] |
| 3 to 4 | 23 | -3.53 µV | 1.79 | 0.37 | [-7.41, -0.90] |
| 4 to 4 | 22 | -3.94 µV | 2.41 | 0.51 | [-9.95, -1.01] |
| 5 to 4 | 22 | -4.08 µV | 2.30 | 0.49 | [-8.57, -0.83] |
| 6 to 4 | 23 | -3.74 µV | 2.20 | 0.46 | [-9.80, -0.48] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 22 | 173.27 ms | 9.00 | 1.92 | [158.31, 195.92] |
| 2 to 4 | 21 | 171.85 ms | 7.11 | 1.55 | [154.05, 183.51] |
| 3 to 4 | 23 | 170.44 ms | 10.06 | 2.10 | [146.84, 197.14] |
| 4 to 4 | 22 | 174.23 ms | 9.22 | 1.97 | [155.68, 192.80] |
| 5 to 4 | 22 | 176.45 ms | 8.67 | 1.85 | [163.05, 196.79] |
| 6 to 4 | 23 | 174.75 ms | 10.70 | 2.23 | [158.72, 199.51] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 2.14 µV | 1.65 | 0.46 | [0.05, 5.24] |
| 2 to 4 | 17 | 1.74 µV | 1.43 | 0.35 | [0.00, 5.30] |
| 3 to 4 | 14 | 1.96 µV | 2.00 | 0.53 | [0.07, 6.16] |
| 4 to 4 | 12 | 2.04 µV | 1.49 | 0.43 | [0.33, 4.41] |
| 5 to 4 | 14 | 2.06 µV | 1.62 | 0.43 | [-0.07, 4.48] |
| 6 to 4 | 16 | 2.35 µV | 1.46 | 0.37 | [0.56, 5.94] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 103.90 ms | 6.09 | 1.69 | [92.84, 115.61] |
| 2 to 4 | 17 | 105.75 ms | 7.01 | 1.70 | [93.65, 118.57] |
| 3 to 4 | 14 | 105.62 ms | 7.36 | 1.97 | [93.48, 119.04] |
| 4 to 4 | 12 | 106.50 ms | 5.74 | 1.66 | [97.47, 116.00] |
| 5 to 4 | 14 | 107.09 ms | 5.02 | 1.34 | [95.91, 113.95] |
| 6 to 4 | 16 | 108.19 ms | 5.90 | 1.47 | [94.68, 115.00] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 3.92 µV | 2.92 | 0.65 | [0.44, 10.49] |
| 2 to 4 | 19 | 4.65 µV | 3.33 | 0.76 | [0.04, 10.61] |
| 3 to 4 | 16 | 4.33 µV | 2.28 | 0.57 | [0.34, 7.20] |
| 4 to 4 | 12 | 2.43 µV | 2.15 | 0.62 | [0.41, 7.30] |
| 5 to 4 | 21 | 3.71 µV | 2.73 | 0.60 | [0.68, 8.55] |
| 6 to 4 | 18 | 3.85 µV | 2.28 | 0.54 | [0.75, 8.75] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 484.13 ms | 13.64 | 3.05 | [459.19, 501.90] |
| 2 to 4 | 19 | 490.54 ms | 18.28 | 4.19 | [449.00, 533.01] |
| 3 to 4 | 16 | 490.99 ms | 13.29 | 3.32 | [460.00, 515.20] |
| 4 to 4 | 12 | 486.63 ms | 20.36 | 5.88 | [463.15, 526.16] |
| 5 to 4 | 21 | 491.49 ms | 17.66 | 3.85 | [453.80, 525.42] |
| 6 to 4 | 18 | 492.32 ms | 17.32 | 4.08 | [464.31, 532.07] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 511.34, BIC = 537.36
- **2 to 4 vs 1 to 4**: *β* = 0.35, *SE* = 0.408, *z* = 0.865, *p* = 0.387
- **3 to 4 vs 1 to 4**: *β* = 0.71, *SE* = 0.399, *z* = 1.777, *p* = 0.076
- **4 to 4 vs 1 to 4**: *β* = 0.69, *SE* = 0.404, *z* = 1.712, *p* = 0.087
- **5 to 4 vs 1 to 4**: *β* = 0.46, *SE* = 0.403, *z* = 1.136, *p* = 0.256
- **6 to 4 vs 1 to 4**: *β* = 0.85, *SE* = 0.399, *z* = 2.141, *p* = 0.032
- **SNR**: *β* = -0.37, *SE* = 0.042, *z* = -8.899, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.35 | 0.41 | -0.87 | 0.387 | 0.986 | n.s. |
| 1 to 4 - 3 to 4 | -0.71 | 0.40 | -1.78 | 0.076 | 0.667 | n.s. |
| 1 to 4 - 4 to 4 | -0.69 | 0.40 | -1.71 | 0.087 | 0.694 | n.s. |
| 1 to 4 - 5 to 4 | -0.46 | 0.40 | -1.14 | 0.256 | 0.961 | n.s. |
| 1 to 4 - 6 to 4 | -0.85 | 0.40 | -2.14 | 0.032 | 0.388 | n.s. |
| 2 to 4 - 3 to 4 | -0.36 | 0.40 | -0.88 | 0.378 | 0.986 | n.s. |
| 2 to 4 - 4 to 4 | -0.34 | 0.41 | -0.83 | 0.407 | 0.986 | n.s. |
| 2 to 4 - 5 to 4 | -0.10 | 0.41 | -0.26 | 0.798 | 0.990 | n.s. |
| 2 to 4 - 6 to 4 | -0.50 | 0.40 | -1.24 | 0.216 | 0.946 | n.s. |
| 3 to 4 - 4 to 4 | 0.02 | 0.40 | 0.05 | 0.964 | 0.990 | n.s. |
| 3 to 4 - 5 to 4 | 0.25 | 0.40 | 0.63 | 0.528 | 0.989 | n.s. |
| 3 to 4 - 6 to 4 | -0.14 | 0.40 | -0.36 | 0.716 | 0.990 | n.s. |
| 4 to 4 - 5 to 4 | 0.23 | 0.40 | 0.58 | 0.562 | 0.989 | n.s. |
| 4 to 4 - 6 to 4 | -0.16 | 0.40 | -0.41 | 0.684 | 0.990 | n.s. |
| 5 to 4 - 6 to 4 | -0.40 | 0.40 | -0.99 | 0.321 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.158, η²_G = 0.043
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.89 | 17 | = 0.349 | -0.40 [-0.74, 0.21] | small | n.s. |
| 1 to 4 vs 3 to 4 | -3.34 | 17 | = 0.058 | -0.70 [-0.94, -0.01] | medium | n.s. |
| 1 to 4 vs 4 to 4 | -1.80 | 17 | = 0.349 | -0.31 [-0.95, 0.03] | small | n.s. |
| 1 to 4 vs 5 to 4 | -1.36 | 17 | = 0.394 | -0.31 [-0.74, 0.19] | small | n.s. |
| 1 to 4 vs 6 to 4 | -1.42 | 17 | = 0.394 | -0.38 [-0.70, 0.22] | small | n.s. |
| 2 to 4 vs 3 to 4 | -1.23 | 17 | = 0.394 | -0.33 [-0.92, 0.04] | small | n.s. |
| 2 to 4 vs 4 to 4 | 0.28 | 17 | = 0.969 | 0.07 [-0.58, 0.36] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | 0.27 | 17 | = 0.969 | 0.08 [-0.46, 0.47] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 0.07 | 17 | = 0.969 | 0.02 [-0.53, 0.41] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | 1.78 | 17 | = 0.349 | 0.37 [-0.18, 0.74] | small | n.s. |
| 3 to 4 vs 5 to 4 | 1.26 | 17 | = 0.394 | 0.39 [-0.25, 0.67] | small | n.s. |
| 3 to 4 vs 6 to 4 | 1.31 | 17 | = 0.394 | 0.35 [-0.32, 0.57] | small | n.s. |
| 4 to 4 vs 5 to 4 | 0.04 | 17 | = 0.969 | 0.01 [-0.43, 0.51] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | -0.18 | 17 | = 0.969 | -0.04 [-0.51, 0.40] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.21 | 17 | = 0.969 | -0.06 [-0.52, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 907.61, BIC = 933.62
- **2 to 4 vs 1 to 4**: *β* = -0.99, *SE* = 1.693, *z* = -0.582, *p* = 0.560
- **3 to 4 vs 1 to 4**: *β* = -3.71, *SE* = 1.657, *z* = -2.240, *p* = 0.025
- **4 to 4 vs 1 to 4**: *β* = 0.06, *SE* = 1.678, *z* = 0.033, *p* = 0.974
- **5 to 4 vs 1 to 4**: *β* = 3.19, *SE* = 1.671, *z* = 1.911, *p* = 0.056
- **6 to 4 vs 1 to 4**: *β* = 0.46, *SE* = 1.656, *z* = 0.276, *p* = 0.783
- **SNR**: *β* = -0.13, *SE* = 0.175, *z* = -0.766, *p* = 0.443

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 0.99 | 1.69 | 0.58 | 0.560 | 0.979 | n.s. |
| 1 to 4 - 3 to 4 | 3.71 | 1.66 | 2.24 | 0.025 | 0.249 | n.s. |
| 1 to 4 - 4 to 4 | -0.06 | 1.68 | -0.03 | 0.974 | 0.990 | n.s. |
| 1 to 4 - 5 to 4 | -3.19 | 1.67 | -1.91 | 0.056 | 0.438 | n.s. |
| 1 to 4 - 6 to 4 | -0.46 | 1.66 | -0.28 | 0.783 | 0.990 | n.s. |
| 2 to 4 - 3 to 4 | 2.73 | 1.68 | 1.62 | 0.105 | 0.563 | n.s. |
| 2 to 4 - 4 to 4 | -1.04 | 1.69 | -0.61 | 0.539 | 0.979 | n.s. |
| 2 to 4 - 5 to 4 | -4.18 | 1.70 | -2.47 | 0.014 | 0.164 | n.s. |
| 2 to 4 - 6 to 4 | -1.44 | 1.68 | -0.86 | 0.391 | 0.949 | n.s. |
| 3 to 4 - 4 to 4 | -3.77 | 1.66 | -2.26 | 0.024 | 0.249 | n.s. |
| 3 to 4 - 5 to 4 | -6.91 | 1.66 | -4.16 | < .001 | < .001 | *** |
| 3 to 4 - 6 to 4 | -4.17 | 1.65 | -2.53 | 0.011 | 0.147 | n.s. |
| 4 to 4 - 5 to 4 | -3.14 | 1.68 | -1.87 | 0.061 | 0.438 | n.s. |
| 4 to 4 - 6 to 4 | -0.40 | 1.65 | -0.24 | 0.808 | 0.990 | n.s. |
| 5 to 4 - 6 to 4 | 2.74 | 1.66 | 1.65 | 0.098 | 0.563 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.40, *p* = 0.044, η²_G = 0.056
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.40 | 17 | = 0.893 | 0.12 [-0.44, 0.50] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 2.17 | 17 | = 0.168 | 0.40 [0.03, 0.97] | small | n.s. |
| 1 to 4 vs 4 to 4 | 0.03 | 17 | = 0.991 | 0.01 [-0.42, 0.51] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -2.32 | 17 | = 0.165 | -0.42 [-1.14, -0.14] | small | n.s. |
| 1 to 4 vs 6 to 4 | -0.01 | 17 | = 0.991 | -0.00 [-0.48, 0.43] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 1.21 | 17 | = 0.403 | 0.30 [-0.25, 0.67] | small | n.s. |
| 2 to 4 vs 4 to 4 | -0.37 | 17 | = 0.893 | -0.11 [-0.55, 0.38] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -2.45 | 17 | = 0.165 | -0.56 [-1.01, -0.01] | medium | n.s. |
| 2 to 4 vs 6 to 4 | -0.53 | 17 | = 0.893 | -0.11 [-0.65, 0.29] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | -1.67 | 17 | = 0.276 | -0.39 [-0.82, 0.12] | small | n.s. |
| 3 to 4 vs 5 to 4 | -3.58 | 17 | = 0.034 | -0.82 [-1.45, -0.37] | large | * |
| 3 to 4 vs 6 to 4 | -1.74 | 17 | = 0.276 | -0.38 [-1.01, -0.06] | small | n.s. |
| 4 to 4 vs 5 to 4 | -1.53 | 17 | = 0.276 | -0.43 [-0.92, 0.06] | small | n.s. |
| 4 to 4 vs 6 to 4 | -0.04 | 17 | = 0.991 | -0.01 [-0.41, 0.50] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 1.52 | 17 | = 0.276 | 0.40 [-0.10, 0.84] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 243.95, BIC = 266.04
- **2 to 4 vs 1 to 4**: *β* = 0.02, *SE* = 0.328, *z* = 0.057, *p* = 0.954
- **3 to 4 vs 1 to 4**: *β* = 0.32, *SE* = 0.345, *z* = 0.914, *p* = 0.361
- **4 to 4 vs 1 to 4**: *β* = -0.04, *SE* = 0.353, *z* = -0.105, *p* = 0.917
- **5 to 4 vs 1 to 4**: *β* = 0.36, *SE* = 0.342, *z* = 1.050, *p* = 0.294
- **6 to 4 vs 1 to 4**: *β* = 0.10, *SE* = 0.329, *z* = 0.294, *p* = 0.769
- **SNR**: *β* = 0.77, *SE* = 0.063, *z* = 12.329, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.02 | 0.33 | -0.06 | 0.954 | 1.000 | n.s. |
| 1 to 4 - 3 to 4 | -0.32 | 0.35 | -0.91 | 0.361 | 0.992 | n.s. |
| 1 to 4 - 4 to 4 | 0.04 | 0.35 | 0.10 | 0.917 | 1.000 | n.s. |
| 1 to 4 - 5 to 4 | -0.36 | 0.34 | -1.05 | 0.294 | 0.991 | n.s. |
| 1 to 4 - 6 to 4 | -0.10 | 0.33 | -0.29 | 0.769 | 1.000 | n.s. |
| 2 to 4 - 3 to 4 | -0.30 | 0.32 | -0.93 | 0.353 | 0.992 | n.s. |
| 2 to 4 - 4 to 4 | 0.06 | 0.34 | 0.17 | 0.869 | 1.000 | n.s. |
| 2 to 4 - 5 to 4 | -0.34 | 0.32 | -1.07 | 0.286 | 0.991 | n.s. |
| 2 to 4 - 6 to 4 | -0.08 | 0.31 | -0.25 | 0.803 | 1.000 | n.s. |
| 3 to 4 - 4 to 4 | 0.35 | 0.35 | 0.99 | 0.320 | 0.991 | n.s. |
| 3 to 4 - 5 to 4 | -0.04 | 0.34 | -0.13 | 0.897 | 1.000 | n.s. |
| 3 to 4 - 6 to 4 | 0.22 | 0.33 | 0.66 | 0.508 | 0.997 | n.s. |
| 4 to 4 - 5 to 4 | -0.40 | 0.35 | -1.13 | 0.258 | 0.989 | n.s. |
| 4 to 4 - 6 to 4 | -0.13 | 0.34 | -0.40 | 0.691 | 1.000 | n.s. |
| 5 to 4 - 6 to 4 | 0.26 | 0.33 | 0.80 | 0.422 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.26, *p* = 0.351, η²_G = 0.233
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.87 | 2 | = 0.793 | -0.33 [-0.70, 0.64] | small | n.s. |
| 1 to 4 vs 3 to 4 | 2.31 | 2 | = 0.369 | 0.99 [-0.46, 1.12] | large | n.s. |
| 1 to 4 vs 4 to 4 | 0.75 | 2 | = 0.795 | 0.39 [-0.83, 0.71] | small | n.s. |
| 1 to 4 vs 5 to 4 | 0.46 | 2 | = 0.795 | 0.44 [-0.63, 0.92] | small | n.s. |
| 1 to 4 vs 6 to 4 | -0.00 | 2 | = 0.999 | -0.00 [-0.91, 0.45] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 15.73 | 2 | = 0.060 | 1.75 [-0.80, 0.64] | large | n.s. |
| 2 to 4 vs 4 to 4 | 4.31 | 2 | = 0.187 | 0.95 [-1.08, 0.62] | large | n.s. |
| 2 to 4 vs 5 to 4 | 1.01 | 2 | = 0.784 | 0.78 [-0.64, 0.70] | medium | n.s. |
| 2 to 4 vs 6 to 4 | 2.74 | 2 | = 0.335 | 0.48 [-1.03, 0.35] | small | n.s. |
| 3 to 4 vs 4 to 4 | -6.79 | 2 | = 0.157 | -0.78 [-1.72, 0.55] | medium | n.s. |
| 3 to 4 vs 5 to 4 | -0.50 | 2 | = 0.795 | -0.36 [-0.63, 1.06] | small | n.s. |
| 3 to 4 vs 6 to 4 | -5.13 | 2 | = 0.180 | -1.43 [-1.75, -0.06] | large | n.s. |
| 4 to 4 vs 5 to 4 | 0.26 | 2 | = 0.877 | 0.17 [-1.26, 0.63] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | -1.51 | 2 | = 0.580 | -0.56 [-0.72, 0.62] | medium | n.s. |
| 5 to 4 vs 6 to 4 | -0.62 | 2 | = 0.795 | -0.52 [-0.98, 0.47] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 556.83, BIC = 578.92
- **2 to 4 vs 1 to 4**: *β* = 2.54, *SE* = 1.856, *z* = 1.367, *p* = 0.171
- **3 to 4 vs 1 to 4**: *β* = 2.71, *SE* = 1.964, *z* = 1.381, *p* = 0.167
- **4 to 4 vs 1 to 4**: *β* = 1.84, *SE* = 2.006, *z* = 0.915, *p* = 0.360
- **5 to 4 vs 1 to 4**: *β* = 3.82, *SE* = 1.949, *z* = 1.958, *p* = 0.050
- **6 to 4 vs 1 to 4**: *β* = 4.24, *SE* = 1.862, *z* = 2.278, *p* = 0.023
- **SNR**: *β* = 0.63, *SE* = 0.406, *z* = 1.547, *p* = 0.122

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -2.54 | 1.86 | -1.37 | 0.171 | 0.907 | n.s. |
| 1 to 4 - 3 to 4 | -2.71 | 1.96 | -1.38 | 0.167 | 0.907 | n.s. |
| 1 to 4 - 4 to 4 | -1.84 | 2.01 | -0.92 | 0.360 | 0.981 | n.s. |
| 1 to 4 - 5 to 4 | -3.82 | 1.95 | -1.96 | 0.050 | 0.514 | n.s. |
| 1 to 4 - 6 to 4 | -4.24 | 1.86 | -2.28 | 0.023 | 0.292 | n.s. |
| 2 to 4 - 3 to 4 | -0.17 | 1.83 | -0.10 | 0.924 | 0.988 | n.s. |
| 2 to 4 - 4 to 4 | 0.70 | 1.95 | 0.36 | 0.719 | 0.988 | n.s. |
| 2 to 4 - 5 to 4 | -1.28 | 1.82 | -0.70 | 0.482 | 0.981 | n.s. |
| 2 to 4 - 6 to 4 | -1.70 | 1.78 | -0.95 | 0.340 | 0.981 | n.s. |
| 3 to 4 - 4 to 4 | 0.88 | 2.06 | 0.42 | 0.671 | 0.988 | n.s. |
| 3 to 4 - 5 to 4 | -1.10 | 1.93 | -0.57 | 0.568 | 0.985 | n.s. |
| 3 to 4 - 6 to 4 | -1.53 | 1.88 | -0.81 | 0.417 | 0.981 | n.s. |
| 4 to 4 - 5 to 4 | -1.98 | 2.02 | -0.98 | 0.327 | 0.981 | n.s. |
| 4 to 4 - 6 to 4 | -2.40 | 1.91 | -1.26 | 0.208 | 0.923 | n.s. |
| 5 to 4 - 6 to 4 | -0.42 | 1.87 | -0.23 | 0.820 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.69, *p* = 0.225, η²_G = 0.160
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 1.49 | 2 | = 0.556 | 0.43 [-1.47, 0.03] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.06 | 2 | = 0.955 | 0.02 [-1.38, 0.27] | negligible | n.s. |
| 1 to 4 vs 4 to 4 | 1.60 | 2 | = 0.556 | 1.05 [-0.63, 0.91] | large | n.s. |
| 1 to 4 vs 5 to 4 | 1.26 | 2 | = 0.556 | 0.76 [-1.16, 0.43] | medium | n.s. |
| 1 to 4 vs 6 to 4 | 0.93 | 2 | = 0.615 | 0.18 [-1.47, 0.04] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | -1.38 | 2 | = 0.556 | -0.46 [-0.97, 0.48] | small | n.s. |
| 2 to 4 vs 4 to 4 | 0.46 | 2 | = 0.803 | 0.30 [-0.68, 1.00] | small | n.s. |
| 2 to 4 vs 5 to 4 | 0.45 | 2 | = 0.803 | 0.19 [-0.92, 0.44] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -1.32 | 2 | = 0.556 | -0.30 [-0.65, 0.69] | small | n.s. |
| 3 to 4 vs 4 to 4 | 2.92 | 2 | = 0.556 | 1.46 [-0.29, 2.26] | large | n.s. |
| 3 to 4 vs 5 to 4 | 2.82 | 2 | = 0.556 | 0.91 [-0.60, 1.10] | large | n.s. |
| 3 to 4 vs 6 to 4 | 0.94 | 2 | = 0.615 | 0.19 [-0.93, 0.52] | negligible | n.s. |
| 4 to 4 vs 5 to 4 | -0.20 | 2 | = 0.921 | -0.12 [-1.09, 0.78] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | -1.60 | 2 | = 0.556 | -0.94 [-1.28, 0.17] | large | n.s. |
| 5 to 4 vs 6 to 4 | -1.42 | 2 | = 0.556 | -0.63 [-0.76, 0.67] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 428.86, BIC = 452.83
- **2 to 4 vs 1 to 4**: *β* = 0.24, *SE* = 0.471, *z* = 0.517, *p* = 0.605
- **3 to 4 vs 1 to 4**: *β* = 0.04, *SE* = 0.497, *z* = 0.073, *p* = 0.942
- **4 to 4 vs 1 to 4**: *β* = -0.44, *SE* = 0.555, *z* = -0.795, *p* = 0.427
- **5 to 4 vs 1 to 4**: *β* = -0.14, *SE* = 0.454, *z* = -0.299, *p* = 0.765
- **6 to 4 vs 1 to 4**: *β* = 0.30, *SE* = 0.479, *z* = 0.619, *p* = 0.536
- **SNR**: *β* = 0.54, *SE* = 0.060, *z* = 9.031, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.24 | 0.47 | -0.52 | 0.605 | 0.999 | n.s. |
| 1 to 4 - 3 to 4 | -0.04 | 0.50 | -0.07 | 0.942 | 0.999 | n.s. |
| 1 to 4 - 4 to 4 | 0.44 | 0.55 | 0.80 | 0.427 | 0.998 | n.s. |
| 1 to 4 - 5 to 4 | 0.14 | 0.45 | 0.30 | 0.765 | 0.999 | n.s. |
| 1 to 4 - 6 to 4 | -0.30 | 0.48 | -0.62 | 0.536 | 0.999 | n.s. |
| 2 to 4 - 3 to 4 | 0.21 | 0.50 | 0.41 | 0.680 | 0.999 | n.s. |
| 2 to 4 - 4 to 4 | 0.68 | 0.58 | 1.19 | 0.234 | 0.976 | n.s. |
| 2 to 4 - 5 to 4 | 0.38 | 0.46 | 0.82 | 0.414 | 0.998 | n.s. |
| 2 to 4 - 6 to 4 | -0.05 | 0.49 | -0.11 | 0.915 | 0.999 | n.s. |
| 3 to 4 - 4 to 4 | 0.48 | 0.59 | 0.81 | 0.417 | 0.998 | n.s. |
| 3 to 4 - 5 to 4 | 0.17 | 0.49 | 0.35 | 0.727 | 0.999 | n.s. |
| 3 to 4 - 6 to 4 | -0.26 | 0.51 | -0.51 | 0.613 | 0.999 | n.s. |
| 4 to 4 - 5 to 4 | -0.31 | 0.55 | -0.55 | 0.580 | 0.999 | n.s. |
| 4 to 4 - 6 to 4 | -0.74 | 0.56 | -1.32 | 0.188 | 0.956 | n.s. |
| 5 to 4 - 6 to 4 | -0.43 | 0.47 | -0.91 | 0.361 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.66, *p* = 0.039, η²_G = 0.161
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.86 | 7 | = 0.267 | -0.39 [-0.87, 0.15] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.04 | 7 | = 0.972 | 0.01 [-0.58, 0.53] | negligible | n.s. |
| 1 to 4 vs 4 to 4 | 1.83 | 7 | = 0.267 | 0.87 [-0.22, 1.11] | large | n.s. |
| 1 to 4 vs 5 to 4 | 0.49 | 7 | = 0.727 | 0.13 [-0.43, 0.51] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.88 | 7 | = 0.558 | 0.38 [-0.38, 0.66] | small | n.s. |
| 2 to 4 vs 3 to 4 | 1.33 | 7 | = 0.425 | 0.52 [-0.36, 0.81] | medium | n.s. |
| 2 to 4 vs 4 to 4 | 3.71 | 7 | = 0.114 | 1.62 [0.12, 1.73] | large | n.s. |
| 2 to 4 vs 5 to 4 | 1.78 | 7 | = 0.267 | 0.55 [-0.20, 0.79] | medium | n.s. |
| 2 to 4 vs 6 to 4 | 1.74 | 7 | = 0.267 | 0.91 [-0.22, 0.83] | large | n.s. |
| 3 to 4 vs 4 to 4 | 2.49 | 7 | = 0.267 | 1.23 [0.11, 1.85] | large | n.s. |
| 3 to 4 vs 5 to 4 | 0.43 | 7 | = 0.727 | 0.14 [-0.44, 0.67] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 1.07 | 7 | = 0.479 | 0.48 [-0.30, 0.88] | small | n.s. |
| 4 to 4 vs 5 to 4 | -1.81 | 7 | = 0.267 | -0.75 [-1.16, 0.19] | medium | n.s. |
| 4 to 4 vs 6 to 4 | -1.20 | 7 | = 0.451 | -0.56 [-1.21, 0.29] | medium | n.s. |
| 5 to 4 vs 6 to 4 | 0.58 | 7 | = 0.725 | 0.25 [-0.48, 0.52] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 909.93, BIC = 933.90
- **2 to 4 vs 1 to 4**: *β* = 6.66, *SE* = 5.188, *z* = 1.284, *p* = 0.199
- **3 to 4 vs 1 to 4**: *β* = 6.99, *SE* = 5.420, *z* = 1.289, *p* = 0.197
- **4 to 4 vs 1 to 4**: *β* = 1.94, *SE* = 6.001, *z* = 0.323, *p* = 0.747
- **5 to 4 vs 1 to 4**: *β* = 7.34, *SE* = 5.037, *z* = 1.457, *p* = 0.145
- **6 to 4 vs 1 to 4**: *β* = 7.89, *SE* = 5.267, *z* = 1.499, *p* = 0.134
- **SNR**: *β* = -0.27, *SE* = 0.542, *z* = -0.504, *p* = 0.614

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -6.66 | 5.19 | -1.28 | 0.199 | 0.943 | n.s. |
| 1 to 4 - 3 to 4 | -6.99 | 5.42 | -1.29 | 0.197 | 0.943 | n.s. |
| 1 to 4 - 4 to 4 | -1.94 | 6.00 | -0.32 | 0.747 | 1.000 | n.s. |
| 1 to 4 - 5 to 4 | -7.34 | 5.04 | -1.46 | 0.145 | 0.889 | n.s. |
| 1 to 4 - 6 to 4 | -7.89 | 5.27 | -1.50 | 0.134 | 0.884 | n.s. |
| 2 to 4 - 3 to 4 | -0.33 | 5.48 | -0.06 | 0.952 | 1.000 | n.s. |
| 2 to 4 - 4 to 4 | 4.72 | 6.16 | 0.77 | 0.444 | 0.993 | n.s. |
| 2 to 4 - 5 to 4 | -0.68 | 5.13 | -0.13 | 0.895 | 1.000 | n.s. |
| 2 to 4 - 6 to 4 | -1.23 | 5.39 | -0.23 | 0.819 | 1.000 | n.s. |
| 3 to 4 - 4 to 4 | 5.05 | 6.32 | 0.80 | 0.424 | 0.993 | n.s. |
| 3 to 4 - 5 to 4 | -0.35 | 5.36 | -0.07 | 0.948 | 1.000 | n.s. |
| 3 to 4 - 6 to 4 | -0.90 | 5.59 | -0.16 | 0.871 | 1.000 | n.s. |
| 4 to 4 - 5 to 4 | -5.40 | 5.95 | -0.91 | 0.364 | 0.989 | n.s. |
| 4 to 4 - 6 to 4 | -5.95 | 6.08 | -0.98 | 0.328 | 0.987 | n.s. |
| 5 to 4 - 6 to 4 | -0.56 | 5.20 | -0.11 | 0.915 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.52, *p* = 0.209, η²_G = 0.144
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.10 | 7 | = 0.555 | -0.44 [-0.94, 0.09] | small | n.s. |
| 1 to 4 vs 3 to 4 | -0.54 | 7 | = 0.809 | -0.25 [-0.96, 0.19] | small | n.s. |
| 1 to 4 vs 4 to 4 | -0.35 | 7 | = 0.809 | -0.18 [-0.78, 0.49] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -1.44 | 7 | = 0.494 | -0.88 [-0.69, 0.25] | large | n.s. |
| 1 to 4 vs 6 to 4 | -2.19 | 7 | = 0.486 | -0.98 [-0.81, 0.24] | large | n.s. |
| 2 to 4 vs 3 to 4 | 0.32 | 7 | = 0.809 | 0.17 [-0.71, 0.45] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | 0.38 | 7 | = 0.809 | 0.19 [-0.51, 0.84] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -1.04 | 7 | = 0.555 | -0.56 [-0.50, 0.47] | medium | n.s. |
| 2 to 4 vs 6 to 4 | -1.79 | 7 | = 0.494 | -0.71 [-0.50, 0.53] | medium | n.s. |
| 3 to 4 vs 4 to 4 | 0.10 | 7 | = 0.927 | 0.04 [-0.73, 0.70] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -1.40 | 7 | = 0.494 | -0.66 [-0.62, 0.49] | medium | n.s. |
| 3 to 4 vs 6 to 4 | -1.31 | 7 | = 0.494 | -0.79 [-0.64, 0.52] | medium | n.s. |
| 4 to 4 vs 5 to 4 | -2.63 | 7 | = 0.486 | -0.62 [-0.99, 0.31] | medium | n.s. |
| 4 to 4 vs 6 to 4 | -1.57 | 7 | = 0.494 | -0.75 [-1.02, 0.44] | medium | n.s. |
| 5 to 4 vs 6 to 4 | -0.48 | 7 | = 0.809 | -0.23 [-0.55, 0.44] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.044). Post-hoc tests revealed:
  - 3 to 4 showed smaller latency than 5 to 4 (*d* = -0.82)
**P3b amplitude:** Significant main effect of condition (*p* = 0.039) (no significant pairwise comparisons)

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
