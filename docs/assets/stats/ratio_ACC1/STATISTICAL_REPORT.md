# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:29:18

---

## 1. Analysis Overview

**Total Measurements:** 345
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
| Ratio 0.5 (1:2) | 23 | -3.51 µV | 1.77 | 0.37 | [-7.61, -0.08] |
| Ratio 0.67 (2:3) | 23 | -3.73 µV | 1.75 | 0.37 | [-8.21, -0.82] |
| Ratio 0.75 (3:4) | 22 | -3.88 µV | 1.64 | 0.35 | [-7.79, -0.85] |
| Ratio 0.8 (4:5) | 22 | -4.15 µV | 2.02 | 0.43 | [-7.75, -1.22] |
| Ratio 0.83 (5:6) | 17 | -3.71 µV | 2.26 | 0.55 | [-8.42, -0.57] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 23 | 173.79 ms | 9.62 | 2.01 | [159.33, 203.46] |
| Ratio 0.67 (2:3) | 23 | 171.31 ms | 7.63 | 1.59 | [155.32, 192.28] |
| Ratio 0.75 (3:4) | 22 | 170.98 ms | 10.02 | 2.14 | [149.08, 200.27] |
| Ratio 0.8 (4:5) | 22 | 172.12 ms | 6.78 | 1.45 | [158.78, 187.94] |
| Ratio 0.83 (5:6) | 17 | 173.28 ms | 12.92 | 3.13 | [151.22, 194.30] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 1.35 µV | 1.24 | 0.32 | [0.35, 4.51] |
| Ratio 0.67 (2:3) | 11 | 1.72 µV | 1.15 | 0.35 | [0.43, 3.50] |
| Ratio 0.75 (3:4) | 11 | 1.82 µV | 1.38 | 0.42 | [0.70, 4.93] |
| Ratio 0.8 (4:5) | 16 | 2.10 µV | 1.75 | 0.44 | [0.08, 5.05] |
| Ratio 0.83 (5:6) | 11 | 2.07 µV | 2.52 | 0.76 | [0.13, 9.04] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 108.47 ms | 2.90 | 0.75 | [103.96, 113.19] |
| Ratio 0.67 (2:3) | 11 | 107.50 ms | 2.41 | 0.73 | [103.50, 111.02] |
| Ratio 0.75 (3:4) | 11 | 106.56 ms | 3.34 | 1.01 | [100.26, 111.38] |
| Ratio 0.8 (4:5) | 16 | 105.11 ms | 4.05 | 1.01 | [97.50, 111.88] |
| Ratio 0.83 (5:6) | 11 | 107.63 ms | 4.40 | 1.33 | [96.62, 113.86] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 3.43 µV | 2.39 | 0.53 | [0.39, 8.60] |
| Ratio 0.67 (2:3) | 19 | 3.73 µV | 2.52 | 0.58 | [0.20, 9.88] |
| Ratio 0.75 (3:4) | 18 | 4.02 µV | 2.43 | 0.57 | [0.50, 7.67] |
| Ratio 0.8 (4:5) | 19 | 3.66 µV | 2.58 | 0.59 | [0.31, 7.71] |
| Ratio 0.83 (5:6) | 12 | 3.31 µV | 2.57 | 0.74 | [0.86, 10.16] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 492.07 ms | 12.26 | 2.74 | [473.00, 518.61] |
| Ratio 0.67 (2:3) | 19 | 491.44 ms | 13.63 | 3.13 | [465.09, 518.71] |
| Ratio 0.75 (3:4) | 18 | 490.72 ms | 11.52 | 2.72 | [470.82, 513.47] |
| Ratio 0.8 (4:5) | 19 | 496.43 ms | 11.60 | 2.66 | [473.52, 514.64] |
| Ratio 0.83 (5:6) | 12 | 497.97 ms | 19.76 | 5.70 | [463.15, 529.90] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 375.01, BIC = 396.39
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.62, *SE* = 0.332, *z* = -1.862, *p* = 0.063
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.13, *SE* = 0.357, *z* = -3.152, *p* = 0.002
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.36, *SE* = 0.355, *z* = -3.824, *p* < .001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.37, *SE* = 0.404, *z* = -3.378, *p* = 0.001
- **SNR**: *β* = -0.16, *SE* = 0.028, *z* = -5.756, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.62 | 0.33 | 1.86 | 0.063 | 0.276 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.13 | 0.36 | 3.15 | 0.002 | 0.013 | * |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.36 | 0.35 | 3.82 | < .001 | 0.001 | ** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.37 | 0.40 | 3.38 | < .001 | 0.007 | ** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.51 | 0.33 | 1.53 | 0.126 | 0.417 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.74 | 0.33 | 2.24 | 0.025 | 0.164 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.75 | 0.37 | 2.00 | 0.045 | 0.242 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.23 | 0.33 | 0.70 | 0.485 | 0.863 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.24 | 0.36 | 0.66 | 0.506 | 0.863 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.01 | 0.36 | 0.02 | 0.980 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.94, *p* = 0.450, η²_G = 0.031
- Greenhouse-Geisser corrected: *p* = 0.419 (ε = 0.620)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 2.34 | 14 | = 0.345 | 0.31 [-0.31, 0.58] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 1.25 | 14 | = 0.590 | 0.30 [-0.19, 0.74] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 1.91 | 14 | = 0.382 | 0.53 [-0.16, 0.75] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.08 | 14 | = 0.590 | 0.32 [-0.35, 0.69] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.07 | 14 | = 0.949 | 0.02 [-0.29, 0.63] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.96 | 14 | = 0.590 | 0.31 [-0.25, 0.65] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.36 | 14 | = 0.807 | 0.11 [-0.57, 0.50] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.96 | 14 | = 0.590 | 0.28 [-0.34, 0.60] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.39 | 14 | = 0.807 | 0.09 [-0.41, 0.66] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.46 | 14 | = 0.807 | -0.15 [-0.73, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 708.16, BIC = 729.54
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -1.59, *SE* = 1.375, *z* = -1.158, *p* = 0.247
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -2.40, *SE* = 1.473, *z* = -1.628, *p* = 0.104
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.80, *SE* = 1.462, *z* = -0.547, *p* = 0.584
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.10, *SE* = 1.670, *z* = -0.656, *p* = 0.512
- **SNR**: *β* = -0.04, *SE* = 0.113, *z* = -0.334, *p* = 0.738

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 1.59 | 1.38 | 1.16 | 0.247 | 0.920 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 2.40 | 1.47 | 1.63 | 0.104 | 0.665 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.80 | 1.46 | 0.55 | 0.584 | 0.986 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.10 | 1.67 | 0.66 | 0.512 | 0.986 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.81 | 1.38 | 0.59 | 0.558 | 0.986 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.79 | 1.37 | -0.58 | 0.562 | 0.986 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.50 | 1.55 | -0.32 | 0.749 | 0.986 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -1.60 | 1.37 | -1.16 | 0.245 | 0.920 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -1.30 | 1.50 | -0.87 | 0.386 | 0.967 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.30 | 1.50 | 0.20 | 0.844 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.89, *p* = 0.474, η²_G = 0.013
- Greenhouse-Geisser corrected: *p* = 0.403 (ε = 0.406)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 1.46 | 14 | = 0.418 | 0.15 [-0.04, 0.89] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 2.75 | 14 | = 0.157 | 0.35 [0.08, 1.07] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.32 | 14 | = 0.837 | 0.02 [-0.35, 0.54] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.52 | 14 | = 0.837 | 0.12 [-0.43, 0.60] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 1.55 | 14 | = 0.418 | 0.21 [-0.28, 0.64] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.93 | 14 | = 0.740 | -0.13 [-0.62, 0.27] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.05 | 14 | = 0.963 | 0.01 [-0.63, 0.44] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -2.10 | 14 | = 0.274 | -0.32 [-0.95, 0.03] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.68 | 14 | = 0.837 | -0.15 [-0.63, 0.44] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.40 | 14 | = 0.837 | 0.10 [-0.53, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 230.91, BIC = 248.19
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.40, *SE* = 0.499, *z* = 0.801, *p* = 0.423
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.83, *SE* = 0.512, *z* = 1.631, *p* = 0.103
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 1.43, *SE* = 0.467, *z* = 3.059, *p* = 0.002
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 1.79, *SE* = 0.537, *z* = 3.329, *p* = 0.001
- **SNR**: *β* = 0.42, *SE* = 0.079, *z* = 5.354, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.40 | 0.50 | -0.80 | 0.423 | 0.808 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.83 | 0.51 | -1.63 | 0.103 | 0.424 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -1.43 | 0.47 | -3.06 | 0.002 | 0.020 | * |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -1.79 | 0.54 | -3.33 | < .001 | 0.009 | ** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.43 | 0.55 | -0.80 | 0.426 | 0.808 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -1.03 | 0.51 | -2.03 | 0.043 | 0.263 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -1.39 | 0.57 | -2.44 | 0.015 | 0.112 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.59 | 0.50 | -1.19 | 0.234 | 0.655 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -0.95 | 0.56 | -1.71 | 0.088 | 0.424 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -0.36 | 0.50 | -0.72 | 0.474 | 0.808 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.795, η²_G = 0.119
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.79 | 3 | = 0.861 | -0.42 [-0.81, 0.62] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -0.05 | 3 | = 0.961 | -0.02 [-1.17, 0.42] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.58 | 3 | = 0.861 | -0.53 [-0.99, 0.26] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.82 | 3 | = 0.861 | -0.65 [-1.25, 0.48] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.55 | 3 | = 0.861 | 0.38 [-1.22, 1.27] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.31 | 3 | = 0.861 | -0.22 [-1.10, 0.60] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.56 | 3 | = 0.861 | -0.47 [-1.36, 0.78] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.65 | 3 | = 0.861 | -0.50 [-1.13, 0.36] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.80 | 3 | = 0.861 | -0.63 [-1.31, 0.82] | medium | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.43 | 3 | = 0.861 | -0.34 [-1.05, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 332.73, BIC = 350.00
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -1.41, *SE* = 0.846, *z* = -1.671, *p* = 0.095
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.63, *SE* = 0.886, *z* = -1.835, *p* = 0.066
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -3.13, *SE* = 0.811, *z* = -3.861, *p* < .001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -0.67, *SE* = 0.988, *z* = -0.678, *p* = 0.498
- **SNR**: *β* = -0.14, *SE* = 0.164, *z* = -0.884, *p* = 0.377

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 1.41 | 0.85 | 1.67 | 0.095 | 0.392 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.63 | 0.89 | 1.84 | 0.066 | 0.382 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 3.13 | 0.81 | 3.86 | < .001 | 0.001 | ** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 0.67 | 0.99 | 0.68 | 0.498 | 0.854 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.21 | 0.98 | 0.22 | 0.829 | 0.854 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 1.72 | 0.90 | 1.91 | 0.057 | 0.372 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.74 | 1.04 | -0.72 | 0.474 | 0.854 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 1.51 | 0.85 | 1.78 | 0.076 | 0.382 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -0.96 | 0.99 | -0.96 | 0.336 | 0.806 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -2.46 | 0.92 | -2.68 | 0.007 | 0.064 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.37, *p* = 0.303, η²_G = 0.141
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 1.34 | 3 | = 0.533 | 0.63 [-0.29, 1.21] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.80 | 3 | = 0.534 | 0.16 [-0.35, 1.27] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 1.32 | 3 | = 0.533 | 0.73 [0.16, 1.59] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.87 | 3 | = 0.534 | -0.18 [-0.90, 0.78] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.83 | 3 | = 0.534 | -0.50 [-1.72, 0.88] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.08 | 3 | = 0.942 | -0.05 [-0.50, 1.23] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -1.37 | 3 | = 0.533 | -0.80 [-1.43, 0.73] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 1.19 | 3 | = 0.533 | 0.58 [-0.35, 1.13] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.23 | 3 | = 0.533 | -0.34 [-1.95, 0.43] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -1.42 | 3 | = 0.533 | -0.94 [-1.84, 0.27] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 343.66, BIC = 363.48
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.37, *SE* = 0.393, *z* = 0.953, *p* = 0.341
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.73, *SE* = 0.403, *z* = 1.817, *p* = 0.069
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.79, *SE* = 0.419, *z* = 1.893, *p* = 0.058
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.04, *SE* = 0.544, *z* = 0.079, *p* = 0.937
- **SNR**: *β* = 0.19, *SE* = 0.041, *z* = 4.618, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.37 | 0.39 | -0.95 | 0.341 | 0.888 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.73 | 0.40 | -1.82 | 0.069 | 0.476 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.79 | 0.42 | -1.89 | 0.058 | 0.452 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.04 | 0.54 | -0.08 | 0.937 | 0.986 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.36 | 0.41 | -0.88 | 0.381 | 0.888 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.42 | 0.41 | -1.02 | 0.306 | 0.888 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.33 | 0.52 | 0.63 | 0.527 | 0.894 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.06 | 0.42 | -0.15 | 0.882 | 0.986 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.69 | 0.53 | 1.29 | 0.196 | 0.783 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.75 | 0.49 | 1.54 | 0.124 | 0.654 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.17, *p* = 0.025, η²_G = 0.116
- Greenhouse-Geisser corrected: *p* = 0.068 (ε = 0.483)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -1.00 | 9 | = 0.572 | -0.10 [-0.70, 0.27] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.41 | 9 | = 0.385 | -0.19 [-0.87, 0.19] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.37 | 9 | = 0.888 | -0.11 [-0.62, 0.38] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.94 | 9 | = 0.211 | 0.70 [-0.16, 1.19] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.47 | 9 | = 0.888 | -0.08 [-0.76, 0.32] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.02 | 9 | = 0.985 | -0.00 [-0.49, 0.50] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.98 | 9 | = 0.211 | 0.78 [-0.15, 1.21] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.26 | 9 | = 0.888 | 0.08 [-0.21, 0.89] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 2.20 | 9 | = 0.211 | 0.88 [-0.15, 1.29] | large | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 2.28 | 9 | = 0.211 | 0.80 [-0.03, 1.48] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 695.56, BIC = 715.38
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.27, *SE* = 3.082, *z* = -0.089, *p* = 0.929
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -0.81, *SE* = 3.156, *z* = -0.258, *p* = 0.796
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 4.39, *SE* = 3.249, *z* = 1.351, *p* = 0.177
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 6.36, *SE* = 4.053, *z* = 1.570, *p* = 0.116
- **SNR**: *β* = -0.17, *SE* = 0.287, *z* = -0.607, *p* = 0.544

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.27 | 3.08 | 0.09 | 0.929 | 0.992 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 0.82 | 3.16 | 0.26 | 0.796 | 0.992 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -4.39 | 3.25 | -1.35 | 0.177 | 0.622 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -6.36 | 4.05 | -1.57 | 0.116 | 0.611 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.54 | 3.20 | 0.17 | 0.865 | 0.992 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -4.66 | 3.20 | -1.46 | 0.145 | 0.611 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -6.64 | 3.95 | -1.68 | 0.093 | 0.584 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -5.20 | 3.27 | -1.59 | 0.111 | 0.611 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -7.18 | 4.00 | -1.80 | 0.073 | 0.529 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -1.97 | 3.74 | -0.53 | 0.597 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.79, *p* = 0.041, η²_G = 0.108
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.96 | 9 | = 0.400 | -0.19 [-0.55, 0.41] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.83 | 9 | = 0.201 | -0.50 [-0.59, 0.44] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -3.37 | 9 | = 0.082 | -1.09 [-1.07, -0.00] | large | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -1.83 | 9 | = 0.201 | -0.71 [-1.21, 0.15] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -1.15 | 9 | = 0.350 | -0.24 [-0.55, 0.52] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -2.25 | 9 | = 0.201 | -0.71 [-0.92, 0.12] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -1.90 | 9 | = 0.201 | -0.53 [-1.24, 0.12] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -1.71 | 9 | = 0.203 | -0.50 [-0.82, 0.27] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.20 | 9 | = 0.350 | -0.37 [-1.20, 0.22] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.12 | 9 | = 0.911 | -0.04 [-0.67, 0.67] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.025) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.041) (no significant pairwise comparisons)

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
