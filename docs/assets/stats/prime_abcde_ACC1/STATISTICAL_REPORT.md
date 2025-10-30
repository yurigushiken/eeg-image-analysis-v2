# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:28:07

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
| a | 24 | -3.50 µV | 1.78 | 0.36 | [-7.77, -0.14] |
| b | 23 | -3.69 µV | 2.02 | 0.42 | [-9.26, -0.98] |
| c | 23 | -3.11 µV | 1.59 | 0.33 | [-6.96, -0.10] |
| d | 24 | -3.40 µV | 1.55 | 0.32 | [-6.71, -0.36] |
| e | 24 | -3.84 µV | 1.96 | 0.40 | [-9.10, -0.77] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 24 | 176.26 ms | 10.11 | 2.06 | [158.61, 206.90] |
| b | 23 | 175.71 ms | 9.33 | 1.94 | [159.34, 199.21] |
| c | 23 | 175.83 ms | 10.73 | 2.24 | [154.81, 207.56] |
| d | 24 | 175.98 ms | 10.31 | 2.10 | [160.43, 204.58] |
| e | 24 | 176.08 ms | 9.50 | 1.94 | [160.65, 202.77] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 14 | 1.63 µV | 1.43 | 0.38 | [0.08, 5.12] |
| b | 14 | 1.45 µV | 1.27 | 0.34 | [-0.05, 4.24] |
| c | 17 | 1.76 µV | 1.63 | 0.40 | [-0.04, 6.42] |
| d | 11 | 1.19 µV | 1.31 | 0.40 | [0.13, 3.82] |
| e | 15 | 1.33 µV | 1.05 | 0.27 | [0.02, 3.07] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 14 | 106.53 ms | 4.45 | 1.19 | [99.91, 114.82] |
| b | 14 | 104.78 ms | 5.75 | 1.54 | [92.16, 110.68] |
| c | 17 | 104.38 ms | 4.23 | 1.03 | [94.38, 110.94] |
| d | 11 | 106.32 ms | 5.69 | 1.72 | [97.17, 115.79] |
| e | 15 | 103.95 ms | 4.95 | 1.28 | [92.49, 114.23] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 19 | 3.33 µV | 2.08 | 0.48 | [0.04, 6.92] |
| b | 17 | 4.44 µV | 2.60 | 0.63 | [0.10, 10.02] |
| c | 22 | 2.90 µV | 1.98 | 0.42 | [0.28, 6.40] |
| d | 19 | 3.25 µV | 2.22 | 0.51 | [0.19, 8.71] |
| e | 18 | 4.19 µV | 2.36 | 0.56 | [1.43, 9.59] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| a | 19 | 474.41 ms | 13.04 | 2.99 | [431.10, 489.78] |
| b | 17 | 478.47 ms | 11.61 | 2.82 | [449.57, 495.28] |
| c | 22 | 476.83 ms | 13.29 | 2.83 | [439.14, 497.74] |
| d | 19 | 484.35 ms | 14.85 | 3.41 | [450.91, 519.24] |
| e | 18 | 480.19 ms | 10.13 | 2.39 | [457.70, 501.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 365.37, BIC = 387.54
- **b vs a**: *β* = -0.08, *SE* = 0.243, *z* = -0.344, *p* = 0.731
- **c vs a**: *β* = 0.53, *SE* = 0.243, *z* = 2.156, *p* = 0.031
- **d vs a**: *β* = 0.12, *SE* = 0.240, *z* = 0.481, *p* = 0.631
- **e vs a**: *β* = -0.04, *SE* = 0.247, *z* = -0.160, *p* = 0.873
- **SNR**: *β* = -0.10, *SE* = 0.021, *z* = -4.942, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.08 | 0.24 | 0.34 | 0.731 | 0.981 | n.s. |
| a - c | -0.52 | 0.24 | -2.16 | 0.031 | 0.223 | n.s. |
| a - d | -0.12 | 0.24 | -0.48 | 0.631 | 0.981 | n.s. |
| a - e | 0.04 | 0.25 | 0.16 | 0.873 | 0.981 | n.s. |
| b - c | -0.61 | 0.25 | -2.48 | 0.013 | 0.123 | n.s. |
| b - d | -0.20 | 0.24 | -0.82 | 0.413 | 0.959 | n.s. |
| b - e | -0.04 | 0.25 | -0.18 | 0.861 | 0.981 | n.s. |
| c - d | 0.41 | 0.24 | 1.68 | 0.092 | 0.493 | n.s. |
| c - e | 0.56 | 0.25 | 2.27 | 0.023 | 0.192 | n.s. |
| d - e | 0.15 | 0.25 | 0.63 | 0.529 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.62, *p* = 0.040, η²_G = 0.025
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.31 | 22 | = 0.762 | 0.04 [-0.37, 0.50] | negligible | n.s. |
| a vs c | -1.96 | 22 | = 0.245 | -0.30 [-0.86, 0.04] | small | n.s. |
| a vs d | -0.63 | 22 | = 0.597 | -0.07 [-0.53, 0.31] | negligible | n.s. |
| a vs e | 1.12 | 22 | = 0.458 | 0.19 [-0.19, 0.66] | negligible | n.s. |
| b vs c | -1.87 | 22 | = 0.245 | -0.32 [-0.84, 0.06] | small | n.s. |
| b vs d | -0.70 | 22 | = 0.597 | -0.11 [-0.58, 0.29] | negligible | n.s. |
| b vs e | 1.01 | 22 | = 0.461 | 0.14 [-0.23, 0.65] | negligible | n.s. |
| c vs d | 1.57 | 22 | = 0.262 | 0.25 [-0.12, 0.77] | small | n.s. |
| c vs e | 2.50 | 22 | = 0.204 | 0.48 [0.06, 0.98] | small | n.s. |
| d vs e | 1.73 | 22 | = 0.245 | 0.27 [-0.09, 0.78] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 725.23, BIC = 747.40
- **b vs a**: *β* = 0.10, *SE* = 0.986, *z* = 0.103, *p* = 0.918
- **c vs a**: *β* = 0.21, *SE* = 0.986, *z* = 0.209, *p* = 0.835
- **d vs a**: *β* = -0.29, *SE* = 0.972, *z* = -0.298, *p* = 0.766
- **e vs a**: *β* = -0.27, *SE* = 1.003, *z* = -0.268, *p* = 0.788
- **SNR**: *β* = 0.03, *SE* = 0.086, *z* = 0.343, *p* = 0.732

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.10 | 0.99 | -0.10 | 0.918 | 1.000 | n.s. |
| a - c | -0.21 | 0.99 | -0.21 | 0.835 | 1.000 | n.s. |
| a - d | 0.29 | 0.97 | 0.30 | 0.766 | 1.000 | n.s. |
| a - e | 0.27 | 1.00 | 0.27 | 0.788 | 1.000 | n.s. |
| b - c | -0.10 | 0.99 | -0.10 | 0.917 | 1.000 | n.s. |
| b - d | 0.39 | 0.99 | 0.40 | 0.692 | 1.000 | n.s. |
| b - e | 0.37 | 1.02 | 0.37 | 0.715 | 1.000 | n.s. |
| c - d | 0.50 | 0.99 | 0.50 | 0.615 | 1.000 | n.s. |
| c - e | 0.47 | 1.01 | 0.47 | 0.638 | 1.000 | n.s. |
| d - e | -0.02 | 1.00 | -0.02 | 0.984 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.977, η²_G = 0.001
- Greenhouse-Geisser corrected: *p* = 0.941 (ε = 0.691)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.04 | 22 | = 0.966 | -0.00 [-0.44, 0.42] | negligible | n.s. |
| a vs c | -0.14 | 22 | = 0.966 | -0.02 [-0.46, 0.40] | negligible | n.s. |
| a vs d | 0.38 | 22 | = 0.966 | 0.04 [-0.37, 0.48] | negligible | n.s. |
| a vs e | 0.48 | 22 | = 0.966 | 0.03 [-0.36, 0.48] | negligible | n.s. |
| b vs c | -0.09 | 22 | = 0.966 | -0.01 [-0.45, 0.41] | negligible | n.s. |
| b vs d | 0.65 | 22 | = 0.966 | 0.05 [-0.30, 0.57] | negligible | n.s. |
| b vs e | 0.40 | 22 | = 0.966 | 0.04 [-0.35, 0.52] | negligible | n.s. |
| c vs d | 0.46 | 22 | = 0.966 | 0.06 [-0.34, 0.53] | negligible | n.s. |
| c vs e | 0.48 | 22 | = 0.966 | 0.05 [-0.33, 0.53] | negligible | n.s. |
| d vs e | -0.11 | 22 | = 0.966 | -0.01 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 170.06, BIC = 188.16
- **b vs a**: *β* = -0.19, *SE* = 0.230, *z* = -0.836, *p* = 0.403
- **c vs a**: *β* = -0.06, *SE* = 0.218, *z* = -0.251, *p* = 0.802
- **d vs a**: *β* = -0.45, *SE* = 0.242, *z* = -1.855, *p* = 0.064
- **e vs a**: *β* = -0.31, *SE* = 0.220, *z* = -1.405, *p* = 0.160
- **SNR**: *β* = 0.27, *SE* = 0.032, *z* = 8.458, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.19 | 0.23 | 0.84 | 0.403 | 0.924 | n.s. |
| a - c | 0.05 | 0.22 | 0.25 | 0.802 | 0.951 | n.s. |
| a - d | 0.45 | 0.24 | 1.86 | 0.064 | 0.481 | n.s. |
| a - e | 0.31 | 0.22 | 1.40 | 0.160 | 0.752 | n.s. |
| b - c | -0.14 | 0.22 | -0.63 | 0.529 | 0.951 | n.s. |
| b - d | 0.26 | 0.25 | 1.01 | 0.313 | 0.895 | n.s. |
| b - e | 0.12 | 0.23 | 0.51 | 0.612 | 0.951 | n.s. |
| c - d | 0.39 | 0.24 | 1.62 | 0.106 | 0.635 | n.s. |
| c - e | 0.25 | 0.21 | 1.18 | 0.236 | 0.848 | n.s. |
| d - e | -0.14 | 0.24 | -0.58 | 0.562 | 0.951 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.282, η²_G = 0.118
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.24 | 4 | = 0.823 | 0.08 [-0.72, 0.71] | negligible | n.s. |
| a vs c | -1.51 | 4 | = 0.421 | -0.42 [-0.98, 0.27] | small | n.s. |
| a vs d | 1.49 | 4 | = 0.421 | 0.40 [-0.02, 1.63] | small | n.s. |
| a vs e | 0.46 | 4 | = 0.823 | 0.32 [-0.40, 0.89] | small | n.s. |
| b vs c | -1.52 | 4 | = 0.421 | -0.56 [-0.98, 0.33] | medium | n.s. |
| b vs d | 3.18 | 4 | = 0.298 | 0.37 [0.27, 3.20] | small | n.s. |
| b vs e | 0.48 | 4 | = 0.823 | 0.29 [-0.52, 1.04] | small | n.s. |
| c vs d | 2.61 | 4 | = 0.298 | 0.85 [0.14, 1.91] | large | n.s. |
| c vs e | 1.18 | 4 | = 0.504 | 0.88 [-0.20, 1.06] | large | n.s. |
| d vs e | -0.32 | 4 | = 0.823 | -0.20 [-0.95, 0.60] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 411.67, BIC = 429.78
- **b vs a**: *β* = -0.46, *SE* = 1.172, *z* = -0.395, *p* = 0.693
- **c vs a**: *β* = -1.15, *SE* = 1.103, *z* = -1.038, *p* = 0.299
- **d vs a**: *β* = -0.33, *SE* = 1.204, *z* = -0.271, *p* = 0.786
- **e vs a**: *β* = -1.54, *SE* = 1.103, *z* = -1.401, *p* = 0.161
- **SNR**: *β* = -0.06, *SE* = 0.159, *z* = -0.359, *p* = 0.719

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | 0.46 | 1.17 | 0.40 | 0.693 | 0.991 | n.s. |
| a - c | 1.14 | 1.10 | 1.04 | 0.299 | 0.959 | n.s. |
| a - d | 0.33 | 1.20 | 0.27 | 0.786 | 0.991 | n.s. |
| a - e | 1.54 | 1.10 | 1.40 | 0.161 | 0.828 | n.s. |
| b - c | 0.68 | 1.11 | 0.61 | 0.539 | 0.985 | n.s. |
| b - d | -0.14 | 1.28 | -0.11 | 0.915 | 0.991 | n.s. |
| b - e | 1.08 | 1.16 | 0.93 | 0.353 | 0.959 | n.s. |
| c - d | -0.82 | 1.22 | -0.67 | 0.504 | 0.985 | n.s. |
| c - e | 0.40 | 1.08 | 0.37 | 0.711 | 0.991 | n.s. |
| d - e | 1.22 | 1.20 | 1.01 | 0.312 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.88, *p* = 0.163, η²_G = 0.091
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | 0.06 | 4 | = 0.955 | 0.02 [-0.96, 0.49] | negligible | n.s. |
| a vs c | 2.03 | 4 | = 0.284 | 0.40 [-0.32, 0.91] | small | n.s. |
| a vs d | -0.82 | 4 | = 0.593 | -0.25 [-0.64, 0.79] | small | n.s. |
| a vs e | 1.97 | 4 | = 0.284 | 0.47 [-0.26, 1.06] | small | n.s. |
| b vs c | 1.84 | 4 | = 0.284 | 0.53 [-0.42, 0.87] | medium | n.s. |
| b vs d | -0.79 | 4 | = 0.593 | -0.30 [-1.49, 0.47] | small | n.s. |
| b vs e | 2.49 | 4 | = 0.284 | 0.60 [-0.01, 1.81] | medium | n.s. |
| c vs d | -1.46 | 4 | = 0.365 | -0.59 [-1.24, 0.27] | medium | n.s. |
| c vs e | 0.29 | 4 | = 0.872 | 0.10 [-0.32, 0.92] | negligible | n.s. |
| d vs e | 1.82 | 4 | = 0.284 | 0.64 [-0.73, 0.81] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.32, BIC = 335.75
- **b vs a**: *β* = 0.59, *SE* = 0.289, *z* = 2.056, *p* = 0.040
- **c vs a**: *β* = -0.29, *SE* = 0.271, *z* = -1.059, *p* = 0.289
- **d vs a**: *β* = -0.08, *SE* = 0.274, *z* = -0.286, *p* = 0.775
- **e vs a**: *β* = 0.43, *SE* = 0.286, *z* = 1.512, *p* = 0.130
- **SNR**: *β* = 0.09, *SE* = 0.021, *z* = 4.306, *p* < .001

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -0.59 | 0.29 | -2.06 | 0.040 | 0.247 | n.s. |
| a - c | 0.29 | 0.27 | 1.06 | 0.289 | 0.745 | n.s. |
| a - d | 0.08 | 0.27 | 0.29 | 0.775 | 0.827 | n.s. |
| a - e | -0.43 | 0.29 | -1.51 | 0.130 | 0.503 | n.s. |
| b - c | 0.88 | 0.28 | 3.16 | 0.002 | 0.016 | * |
| b - d | 0.67 | 0.29 | 2.34 | 0.019 | 0.145 | n.s. |
| b - e | 0.16 | 0.29 | 0.57 | 0.572 | 0.827 | n.s. |
| c - d | -0.21 | 0.27 | -0.77 | 0.443 | 0.827 | n.s. |
| c - e | -0.72 | 0.28 | -2.61 | 0.009 | 0.078 | n.s. |
| d - e | -0.51 | 0.29 | -1.76 | 0.078 | 0.385 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.69, *p* = 0.009, η²_G = 0.038
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -2.28 | 15 | = 0.090 | -0.36 [-1.14, 0.01] | small | n.s. |
| a vs c | 0.87 | 15 | = 0.570 | 0.09 [-0.35, 0.62] | negligible | n.s. |
| a vs d | 0.18 | 15 | = 0.860 | 0.03 [-0.40, 0.60] | negligible | n.s. |
| a vs e | -1.73 | 15 | = 0.174 | -0.33 [-0.98, 0.06] | small | n.s. |
| b vs c | 3.03 | 15 | = 0.084 | 0.44 [0.15, 1.31] | small | n.s. |
| b vs d | 2.19 | 15 | = 0.090 | 0.37 [0.02, 1.13] | small | n.s. |
| b vs e | 0.28 | 15 | = 0.860 | 0.05 [-0.46, 0.60] | negligible | n.s. |
| c vs d | -0.45 | 15 | = 0.821 | -0.06 [-0.45, 0.51] | negligible | n.s. |
| c vs e | -2.39 | 15 | = 0.090 | -0.42 [-1.18, -0.09] | small | n.s. |
| d vs e | -2.44 | 15 | = 0.090 | -0.34 [-1.23, -0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 724.88, BIC = 745.31
- **b vs a**: *β* = 2.00, *SE* = 2.755, *z* = 0.728, *p* = 0.467
- **c vs a**: *β* = 0.90, *SE* = 2.565, *z* = 0.350, *p* = 0.726
- **d vs a**: *β* = 7.71, *SE* = 2.616, *z* = 2.946, *p* = 0.003
- **e vs a**: *β* = 5.52, *SE* = 2.720, *z* = 2.029, *p* = 0.042
- **SNR**: *β* = 0.19, *SE* = 0.183, *z* = 1.022, *p* = 0.307

_Reference condition: **a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| a - b | -2.01 | 2.75 | -0.73 | 0.467 | 0.893 | n.s. |
| a - c | -0.90 | 2.56 | -0.35 | 0.726 | 0.895 | n.s. |
| a - d | -7.71 | 2.62 | -2.95 | 0.003 | 0.032 | * |
| a - e | -5.52 | 2.72 | -2.03 | 0.042 | 0.265 | n.s. |
| b - c | 1.11 | 2.65 | 0.42 | 0.676 | 0.895 | n.s. |
| b - d | -5.70 | 2.74 | -2.08 | 0.038 | 0.265 | n.s. |
| b - e | -3.51 | 2.74 | -1.28 | 0.200 | 0.672 | n.s. |
| c - d | -6.81 | 2.57 | -2.65 | 0.008 | 0.070 | n.s. |
| c - e | -4.62 | 2.63 | -1.76 | 0.079 | 0.388 | n.s. |
| d - e | 2.19 | 2.76 | 0.79 | 0.428 | 0.893 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.30, *p* = 0.281, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| a vs b | -0.20 | 15 | = 0.843 | -0.06 [-0.58, 0.48] | negligible | n.s. |
| a vs c | 0.45 | 15 | = 0.729 | 0.08 [-0.55, 0.42] | negligible | n.s. |
| a vs d | -1.09 | 15 | = 0.488 | -0.28 [-0.97, 0.07] | small | n.s. |
| a vs e | -1.55 | 15 | = 0.400 | -0.46 [-1.02, 0.03] | small | n.s. |
| b vs c | 0.48 | 15 | = 0.729 | 0.12 [-0.45, 0.58] | negligible | n.s. |
| b vs d | -1.12 | 15 | = 0.488 | -0.19 [-0.89, 0.17] | negligible | n.s. |
| b vs e | -1.50 | 15 | = 0.400 | -0.32 [-0.93, 0.18] | small | n.s. |
| c vs d | -1.48 | 15 | = 0.400 | -0.33 [-0.98, 0.03] | small | n.s. |
| c vs e | -1.59 | 15 | = 0.400 | -0.50 [-1.04, 0.02] | medium | n.s. |
| d vs e | -0.57 | 15 | = 0.729 | -0.12 [-0.45, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.040) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.009) (no significant pairwise comparisons)

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
