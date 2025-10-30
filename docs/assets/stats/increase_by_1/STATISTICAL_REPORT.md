# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:54:21

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
| 1 to 2 | 21 | -3.54 µV | 1.78 | 0.39 | [-7.64, -0.32] |
| 2 to 3 | 22 | -3.36 µV | 1.43 | 0.30 | [-5.80, -0.29] |
| 3 to 4 | 22 | -3.42 µV | 1.49 | 0.32 | [-7.23, -1.10] |
| 4 to 5 | 23 | -3.76 µV | 2.35 | 0.49 | [-8.48, -0.69] |
| 5 to 6 | 22 | -4.21 µV | 2.15 | 0.46 | [-8.79, -0.97] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | 169.20 ms | 9.97 | 2.18 | [143.27, 188.66] |
| 2 to 3 | 22 | 170.92 ms | 7.29 | 1.55 | [154.19, 186.31] |
| 3 to 4 | 22 | 168.01 ms | 8.20 | 1.75 | [144.71, 181.63] |
| 4 to 5 | 23 | 170.80 ms | 10.66 | 2.22 | [148.65, 192.37] |
| 5 to 6 | 22 | 173.28 ms | 9.68 | 2.06 | [145.04, 192.36] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 1.34 µV | 1.07 | 0.30 | [0.08, 3.30] |
| 2 to 3 | 11 | 1.91 µV | 1.37 | 0.41 | [0.04, 5.13] |
| 3 to 4 | 16 | 1.63 µV | 1.55 | 0.39 | [0.11, 6.03] |
| 4 to 5 | 14 | 2.18 µV | 2.31 | 0.62 | [0.28, 8.84] |
| 5 to 6 | 12 | 1.63 µV | 0.96 | 0.28 | [0.08, 3.14] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 99.17 ms | 5.92 | 1.64 | [90.99, 110.28] |
| 2 to 3 | 11 | 100.17 ms | 4.65 | 1.40 | [93.02, 107.38] |
| 3 to 4 | 16 | 97.77 ms | 7.00 | 1.75 | [85.61, 109.33] |
| 4 to 5 | 14 | 100.33 ms | 5.35 | 1.43 | [90.92, 109.78] |
| 5 to 6 | 12 | 97.22 ms | 6.11 | 1.76 | [90.57, 111.17] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 3.48 µV | 2.80 | 0.68 | [0.21, 10.31] |
| 2 to 3 | 18 | 3.90 µV | 2.98 | 0.70 | [0.18, 10.23] |
| 3 to 4 | 17 | 3.67 µV | 2.44 | 0.59 | [0.19, 6.97] |
| 4 to 5 | 16 | 3.51 µV | 3.14 | 0.78 | [0.58, 12.01] |
| 5 to 6 | 9 | 2.84 µV | 2.81 | 0.94 | [0.31, 7.73] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 486.81 ms | 18.95 | 4.60 | [455.32, 531.57] |
| 2 to 3 | 18 | 479.70 ms | 18.99 | 4.47 | [442.28, 520.61] |
| 3 to 4 | 17 | 483.42 ms | 16.05 | 3.89 | [454.80, 509.48] |
| 4 to 5 | 16 | 493.49 ms | 18.17 | 4.54 | [446.39, 515.87] |
| 5 to 6 | 9 | 484.84 ms | 25.91 | 8.64 | [454.57, 526.77] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 358.10, BIC = 379.71
- **2 to 3 vs 1 to 2**: *β* = -0.07, *SE* = 0.295, *z* = -0.221, *p* = 0.825
- **3 to 4 vs 1 to 2**: *β* = -0.14, *SE* = 0.295, *z* = -0.485, *p* = 0.628
- **4 to 5 vs 1 to 2**: *β* = -0.33, *SE* = 0.289, *z* = -1.137, *p* = 0.256
- **5 to 6 vs 1 to 2**: *β* = -0.28, *SE* = 0.294, *z* = -0.937, *p* = 0.349
- **SNR**: *β* = -0.47, *SE* = 0.043, *z* = -10.791, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 0.06 | 0.29 | 0.22 | 0.825 | 0.993 | n.s. |
| 1 to 2 - 3 to 4 | 0.14 | 0.30 | 0.48 | 0.628 | 0.993 | n.s. |
| 1 to 2 - 4 to 5 | 0.33 | 0.29 | 1.14 | 0.256 | 0.948 | n.s. |
| 1 to 2 - 5 to 6 | 0.28 | 0.29 | 0.94 | 0.349 | 0.979 | n.s. |
| 2 to 3 - 3 to 4 | 0.08 | 0.29 | 0.27 | 0.787 | 0.993 | n.s. |
| 2 to 3 - 4 to 5 | 0.26 | 0.29 | 0.92 | 0.355 | 0.979 | n.s. |
| 2 to 3 - 5 to 6 | 0.21 | 0.29 | 0.72 | 0.474 | 0.989 | n.s. |
| 3 to 4 - 4 to 5 | 0.19 | 0.29 | 0.65 | 0.516 | 0.989 | n.s. |
| 3 to 4 - 5 to 6 | 0.13 | 0.30 | 0.45 | 0.654 | 0.993 | n.s. |
| 4 to 5 - 5 to 6 | -0.05 | 0.29 | -0.19 | 0.853 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.22, *p* = 0.311, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -1.27 | 17 | = 0.564 | -0.32 [-0.75, 0.20] | small | n.s. |
| 1 to 2 vs 3 to 4 | -1.12 | 17 | = 0.564 | -0.27 [-0.57, 0.37] | small | n.s. |
| 1 to 2 vs 4 to 5 | 0.29 | 17 | = 0.858 | 0.09 [-0.38, 0.53] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | 0.87 | 17 | = 0.564 | 0.26 [-0.23, 0.72] | small | n.s. |
| 2 to 3 vs 3 to 4 | 0.09 | 17 | = 0.928 | 0.03 [-0.51, 0.40] | negligible | n.s. |
| 2 to 3 vs 4 to 5 | 0.98 | 17 | = 0.564 | 0.33 [-0.23, 0.67] | small | n.s. |
| 2 to 3 vs 5 to 6 | 1.66 | 17 | = 0.564 | 0.53 [-0.10, 0.84] | medium | n.s. |
| 3 to 4 vs 4 to 5 | 1.07 | 17 | = 0.564 | 0.29 [-0.24, 0.66] | small | n.s. |
| 3 to 4 vs 5 to 6 | 2.19 | 17 | = 0.431 | 0.48 [-0.01, 0.95] | small | n.s. |
| 4 to 5 vs 5 to 6 | 0.57 | 17 | = 0.717 | 0.14 [-0.30, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 783.55, BIC = 805.15
- **2 to 3 vs 1 to 2**: *β* = 1.75, *SE* = 2.072, *z* = 0.842, *p* = 0.400
- **3 to 4 vs 1 to 2**: *β* = -0.94, *SE* = 2.076, *z* = -0.452, *p* = 0.651
- **4 to 5 vs 1 to 2**: *β* = 1.57, *SE* = 2.037, *z* = 0.772, *p* = 0.440
- **5 to 6 vs 1 to 2**: *β* = 4.00, *SE* = 2.070, *z* = 1.929, *p* = 0.054
- **SNR**: *β* = 0.19, *SE* = 0.302, *z* = 0.642, *p* = 0.521

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -1.75 | 2.07 | -0.84 | 0.400 | 0.870 | n.s. |
| 1 to 2 - 3 to 4 | 0.94 | 2.08 | 0.45 | 0.651 | 0.878 | n.s. |
| 1 to 2 - 4 to 5 | -1.57 | 2.04 | -0.77 | 0.440 | 0.870 | n.s. |
| 1 to 2 - 5 to 6 | -3.99 | 2.07 | -1.93 | 0.054 | 0.391 | n.s. |
| 2 to 3 - 3 to 4 | 2.68 | 2.03 | 1.32 | 0.187 | 0.809 | n.s. |
| 2 to 3 - 4 to 5 | 0.17 | 2.01 | 0.09 | 0.931 | 0.931 | n.s. |
| 2 to 3 - 5 to 6 | -2.25 | 2.07 | -1.09 | 0.278 | 0.812 | n.s. |
| 3 to 4 - 4 to 5 | -2.51 | 2.01 | -1.25 | 0.212 | 0.812 | n.s. |
| 3 to 4 - 5 to 6 | -4.93 | 2.08 | -2.37 | 0.018 | 0.163 | n.s. |
| 4 to 5 - 5 to 6 | -2.42 | 2.02 | -1.20 | 0.231 | 0.812 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.431, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.12 | 17 | = 0.976 | -0.02 [-0.51, 0.43] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | 1.02 | 17 | = 0.697 | 0.20 [-0.41, 0.52] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.84 | 17 | = 0.697 | 0.18 [-0.58, 0.34] | negligible | n.s. |
| 1 to 2 vs 5 to 6 | -0.65 | 17 | = 0.697 | -0.12 [-0.81, 0.15] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | 1.12 | 17 | = 0.697 | 0.23 [-0.06, 0.89] | small | n.s. |
| 2 to 3 vs 4 to 5 | 0.79 | 17 | = 0.697 | 0.21 [-0.32, 0.57] | small | n.s. |
| 2 to 3 vs 5 to 6 | -0.60 | 17 | = 0.697 | -0.11 [-0.80, 0.13] | negligible | n.s. |
| 3 to 4 vs 4 to 5 | -0.03 | 17 | = 0.976 | -0.01 [-0.74, 0.16] | negligible | n.s. |
| 3 to 4 vs 5 to 6 | -2.06 | 17 | = 0.553 | -0.32 [-1.12, -0.13] | small | n.s. |
| 4 to 5 vs 5 to 6 | -1.33 | 17 | = 0.697 | -0.29 [-0.78, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 196.91, BIC = 214.43
- **2 to 3 vs 1 to 2**: *β* = 0.65, *SE* = 0.365, *z* = 1.773, *p* = 0.076
- **3 to 4 vs 1 to 2**: *β* = 0.66, *SE* = 0.342, *z* = 1.920, *p* = 0.055
- **4 to 5 vs 1 to 2**: *β* = 0.72, *SE* = 0.347, *z* = 2.069, *p* = 0.039
- **5 to 6 vs 1 to 2**: *β* = 0.44, *SE* = 0.362, *z* = 1.224, *p* = 0.221
- **SNR**: *β* = 0.90, *SE* = 0.091, *z* = 9.850, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.65 | 0.37 | -1.77 | 0.076 | 0.470 | n.s. |
| 1 to 2 - 3 to 4 | -0.66 | 0.34 | -1.92 | 0.055 | 0.398 | n.s. |
| 1 to 2 - 4 to 5 | -0.72 | 0.35 | -2.07 | 0.039 | 0.325 | n.s. |
| 1 to 2 - 5 to 6 | -0.44 | 0.36 | -1.22 | 0.221 | 0.826 | n.s. |
| 2 to 3 - 3 to 4 | -0.01 | 0.36 | -0.03 | 0.979 | 0.997 | n.s. |
| 2 to 3 - 4 to 5 | -0.07 | 0.36 | -0.19 | 0.849 | 0.997 | n.s. |
| 2 to 3 - 5 to 6 | 0.20 | 0.38 | 0.54 | 0.590 | 0.979 | n.s. |
| 3 to 4 - 4 to 5 | -0.06 | 0.34 | -0.18 | 0.859 | 0.997 | n.s. |
| 3 to 4 - 5 to 6 | 0.21 | 0.34 | 0.62 | 0.536 | 0.979 | n.s. |
| 4 to 5 - 5 to 6 | 0.27 | 0.36 | 0.76 | 0.445 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.527, η²_G = 0.196
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.45 | 2 | = 0.769 | -0.27 [-1.05, 0.51] | small | n.s. |
| 1 to 2 vs 3 to 4 | -0.34 | 2 | = 0.769 | -0.09 [-1.66, 0.37] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | 0.84 | 2 | = 0.753 | 0.46 [-1.33, 0.31] | small | n.s. |
| 1 to 2 vs 5 to 6 | 1.74 | 2 | = 0.753 | 1.94 [-0.39, 1.64] | large | n.s. |
| 2 to 3 vs 3 to 4 | 0.43 | 2 | = 0.769 | 0.23 [-1.27, 0.62] | small | n.s. |
| 2 to 3 vs 4 to 5 | 0.76 | 2 | = 0.753 | 0.45 [-0.98, 0.70] | small | n.s. |
| 2 to 3 vs 5 to 6 | 0.92 | 2 | = 0.753 | 0.86 [-0.51, 1.80] | large | n.s. |
| 3 to 4 vs 4 to 5 | 1.59 | 2 | = 0.753 | 0.51 [-0.88, 0.97] | medium | n.s. |
| 3 to 4 vs 5 to 6 | 1.66 | 2 | = 0.753 | 1.81 [-0.84, 0.70] | large | n.s. |
| 4 to 5 vs 5 to 6 | 1.09 | 2 | = 0.753 | 1.09 [-1.11, 0.76] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 426.79, BIC = 444.31
- **2 to 3 vs 1 to 2**: *β* = 1.19, *SE* = 1.914, *z* = 0.619, *p* = 0.536
- **3 to 4 vs 1 to 2**: *β* = -0.37, *SE* = 1.883, *z* = -0.196, *p* = 0.845
- **4 to 5 vs 1 to 2**: *β* = 1.30, *SE* = 1.823, *z* = 0.711, *p* = 0.477
- **5 to 6 vs 1 to 2**: *β* = -0.63, *SE* = 1.973, *z* = -0.319, *p* = 0.749
- **SNR**: *β* = -0.65, *SE* = 0.498, *z* = -1.306, *p* = 0.191

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -1.18 | 1.91 | -0.62 | 0.536 | 0.985 | n.s. |
| 1 to 2 - 3 to 4 | 0.37 | 1.88 | 0.20 | 0.845 | 0.996 | n.s. |
| 1 to 2 - 4 to 5 | -1.30 | 1.82 | -0.71 | 0.477 | 0.985 | n.s. |
| 1 to 2 - 5 to 6 | 0.63 | 1.97 | 0.32 | 0.749 | 0.996 | n.s. |
| 2 to 3 - 3 to 4 | 1.55 | 1.93 | 0.81 | 0.420 | 0.985 | n.s. |
| 2 to 3 - 4 to 5 | -0.11 | 1.92 | -0.06 | 0.954 | 0.996 | n.s. |
| 2 to 3 - 5 to 6 | 1.81 | 2.03 | 0.89 | 0.372 | 0.985 | n.s. |
| 3 to 4 - 4 to 5 | -1.67 | 1.87 | -0.89 | 0.372 | 0.985 | n.s. |
| 3 to 4 - 5 to 6 | 0.26 | 1.82 | 0.14 | 0.886 | 0.996 | n.s. |
| 4 to 5 - 5 to 6 | 1.93 | 1.95 | 0.99 | 0.322 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.47, *p* = 0.297, η²_G = 0.260
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -2.01 | 2 | = 0.554 | -1.68 [-1.42, 0.24] | large | n.s. |
| 1 to 2 vs 3 to 4 | -2.53 | 2 | = 0.554 | -1.89 [-1.42, 0.52] | large | n.s. |
| 1 to 2 vs 4 to 5 | -1.40 | 2 | = 0.554 | -0.55 [-0.94, 0.61] | medium | n.s. |
| 1 to 2 vs 5 to 6 | -0.44 | 2 | = 0.705 | -0.20 [-1.03, 0.82] | negligible | n.s. |
| 2 to 3 vs 3 to 4 | -2.11 | 2 | = 0.554 | -0.30 [-1.24, 0.65] | small | n.s. |
| 2 to 3 vs 4 to 5 | 0.59 | 2 | = 0.680 | 0.53 [-0.62, 1.07] | medium | n.s. |
| 2 to 3 vs 5 to 6 | 0.94 | 2 | = 0.589 | 0.75 [-0.99, 1.11] | medium | n.s. |
| 3 to 4 vs 4 to 5 | 0.88 | 2 | = 0.589 | 0.72 [-0.58, 1.34] | medium | n.s. |
| 3 to 4 vs 5 to 6 | 1.27 | 2 | = 0.554 | 0.91 [-0.73, 0.81] | large | n.s. |
| 4 to 5 vs 5 to 6 | 1.31 | 2 | = 0.554 | 0.24 [-0.53, 1.41] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 328.46, BIC = 347.21
- **2 to 3 vs 1 to 2**: *β* = 0.21, *SE* = 0.527, *z* = 0.394, *p* = 0.694
- **3 to 4 vs 1 to 2**: *β* = -0.23, *SE* = 0.532, *z* = -0.426, *p* = 0.670
- **4 to 5 vs 1 to 2**: *β* = 0.27, *SE* = 0.550, *z* = 0.485, *p* = 0.628
- **5 to 6 vs 1 to 2**: *β* = -0.38, *SE* = 0.664, *z* = -0.566, *p* = 0.571
- **SNR**: *β* = 0.49, *SE* = 0.066, *z* = 7.411, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | -0.21 | 0.53 | -0.39 | 0.694 | 0.994 | n.s. |
| 1 to 2 - 3 to 4 | 0.23 | 0.53 | 0.43 | 0.670 | 0.994 | n.s. |
| 1 to 2 - 4 to 5 | -0.27 | 0.55 | -0.48 | 0.628 | 0.994 | n.s. |
| 1 to 2 - 5 to 6 | 0.38 | 0.66 | 0.57 | 0.571 | 0.994 | n.s. |
| 2 to 3 - 3 to 4 | 0.43 | 0.52 | 0.83 | 0.406 | 0.984 | n.s. |
| 2 to 3 - 4 to 5 | -0.06 | 0.54 | -0.11 | 0.913 | 0.994 | n.s. |
| 2 to 3 - 5 to 6 | 0.58 | 0.67 | 0.87 | 0.386 | 0.984 | n.s. |
| 3 to 4 - 4 to 5 | -0.49 | 0.55 | -0.90 | 0.369 | 0.984 | n.s. |
| 3 to 4 - 5 to 6 | 0.15 | 0.67 | 0.22 | 0.825 | 0.994 | n.s. |
| 4 to 5 - 5 to 6 | 0.64 | 0.66 | 0.97 | 0.331 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.98, *p* = 0.439, η²_G = 0.082
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -2.20 | 6 | = 0.320 | -0.44 [-1.17, 0.02] | small | n.s. |
| 1 to 2 vs 3 to 4 | -0.02 | 6 | = 0.986 | -0.01 [-0.64, 0.47] | negligible | n.s. |
| 1 to 2 vs 4 to 5 | -0.44 | 6 | = 0.753 | -0.21 [-0.67, 0.60] | small | n.s. |
| 1 to 2 vs 5 to 6 | 0.59 | 6 | = 0.753 | 0.34 [-0.56, 1.15] | small | n.s. |
| 2 to 3 vs 3 to 4 | 1.97 | 6 | = 0.320 | 0.50 [-0.29, 0.84] | small | n.s. |
| 2 to 3 vs 4 to 5 | 0.48 | 6 | = 0.753 | 0.24 [-0.42, 0.80] | small | n.s. |
| 2 to 3 vs 5 to 6 | 1.45 | 6 | = 0.490 | 0.85 [-0.37, 1.41] | large | n.s. |
| 3 to 4 vs 4 to 5 | -0.53 | 6 | = 0.753 | -0.24 [-0.63, 0.58] | small | n.s. |
| 3 to 4 vs 5 to 6 | 0.70 | 6 | = 0.753 | 0.41 [-0.52, 1.20] | small | n.s. |
| 4 to 5 vs 5 to 6 | 2.70 | 6 | = 0.320 | 0.60 [-0.13, 1.81] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 683.64, BIC = 702.39
- **2 to 3 vs 1 to 2**: *β* = -7.24, *SE* = 6.265, *z* = -1.156, *p* = 0.248
- **3 to 4 vs 1 to 2**: *β* = -3.53, *SE* = 6.356, *z* = -0.556, *p* = 0.578
- **4 to 5 vs 1 to 2**: *β* = 6.81, *SE* = 6.612, *z* = 1.031, *p* = 0.303
- **5 to 6 vs 1 to 2**: *β* = -1.67, *SE* = 7.785, *z* = -0.214, *p* = 0.830
- **SNR**: *β* = 0.21, *SE* = 0.716, *z* = 0.289, *p* = 0.773

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 2 to 3 | 7.24 | 6.26 | 1.16 | 0.248 | 0.897 | n.s. |
| 1 to 2 - 3 to 4 | 3.53 | 6.36 | 0.56 | 0.578 | 0.960 | n.s. |
| 1 to 2 - 4 to 5 | -6.81 | 6.61 | -1.03 | 0.303 | 0.897 | n.s. |
| 1 to 2 - 5 to 6 | 1.67 | 7.79 | 0.21 | 0.830 | 0.965 | n.s. |
| 2 to 3 - 3 to 4 | -3.71 | 6.25 | -0.59 | 0.553 | 0.960 | n.s. |
| 2 to 3 - 4 to 5 | -14.06 | 6.60 | -2.13 | 0.033 | 0.287 | n.s. |
| 2 to 3 - 5 to 6 | -5.57 | 7.80 | -0.71 | 0.475 | 0.960 | n.s. |
| 3 to 4 - 4 to 5 | -10.35 | 6.69 | -1.55 | 0.122 | 0.690 | n.s. |
| 3 to 4 - 5 to 6 | -1.86 | 7.88 | -0.24 | 0.813 | 0.965 | n.s. |
| 4 to 5 - 5 to 6 | 8.48 | 7.72 | 1.10 | 0.272 | 0.897 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.433, η²_G = 0.114
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 2 to 3 | -0.07 | 6 | = 0.946 | -0.02 [-0.47, 0.64] | negligible | n.s. |
| 1 to 2 vs 3 to 4 | -0.49 | 6 | = 0.907 | -0.25 [-0.51, 0.59] | small | n.s. |
| 1 to 2 vs 4 to 5 | -1.88 | 6 | = 0.757 | -1.01 [-0.94, 0.35] | large | n.s. |
| 1 to 2 vs 5 to 6 | -1.08 | 6 | = 0.757 | -0.60 [-1.11, 0.59] | medium | n.s. |
| 2 to 3 vs 3 to 4 | -0.37 | 6 | = 0.907 | -0.22 [-0.64, 0.47] | small | n.s. |
| 2 to 3 vs 4 to 5 | -1.43 | 6 | = 0.757 | -0.91 [-1.76, -0.27] | large | n.s. |
| 2 to 3 vs 5 to 6 | -0.90 | 6 | = 0.757 | -0.56 [-0.91, 0.77] | medium | n.s. |
| 3 to 4 vs 4 to 5 | -1.23 | 6 | = 0.757 | -0.61 [-1.10, 0.17] | medium | n.s. |
| 3 to 4 vs 5 to 6 | -0.80 | 6 | = 0.757 | -0.37 [-0.97, 0.71] | small | n.s. |
| 4 to 5 vs 5 to 6 | 0.23 | 6 | = 0.920 | 0.11 [-0.66, 1.03] | negligible | n.s. |

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
