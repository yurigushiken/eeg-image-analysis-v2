# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:29:21

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
| Ratio 0.5 (1:2, no 1) | 23 | -4.26 µV | 1.83 | 0.38 | [-7.67, -1.43] |
| Ratio 0.67 (2:3, no 1) | 23 | -3.73 µV | 1.75 | 0.37 | [-8.21, -0.82] |
| Ratio 0.75 (3:4, no 1) | 22 | -3.88 µV | 1.64 | 0.35 | [-7.79, -0.85] |
| Ratio 0.8 (4:5, no 1) | 22 | -4.15 µV | 2.02 | 0.43 | [-7.75, -1.22] |
| Ratio 0.83 (5:6, no 1) | 17 | -3.71 µV | 2.26 | 0.55 | [-8.42, -0.57] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 23 | 173.05 ms | 7.47 | 1.56 | [160.84, 188.18] |
| Ratio 0.67 (2:3, no 1) | 23 | 171.31 ms | 7.63 | 1.59 | [155.32, 192.28] |
| Ratio 0.75 (3:4, no 1) | 22 | 170.98 ms | 10.02 | 2.14 | [149.08, 200.27] |
| Ratio 0.8 (4:5, no 1) | 22 | 172.12 ms | 6.78 | 1.45 | [158.78, 187.94] |
| Ratio 0.83 (5:6, no 1) | 17 | 173.28 ms | 12.92 | 3.13 | [151.22, 194.30] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 14 | 1.45 µV | 1.15 | 0.31 | [-0.03, 4.14] |
| Ratio 0.67 (2:3, no 1) | 11 | 1.72 µV | 1.15 | 0.35 | [0.43, 3.50] |
| Ratio 0.75 (3:4, no 1) | 11 | 1.82 µV | 1.38 | 0.42 | [0.70, 4.93] |
| Ratio 0.8 (4:5, no 1) | 16 | 2.10 µV | 1.75 | 0.44 | [0.08, 5.05] |
| Ratio 0.83 (5:6, no 1) | 11 | 2.07 µV | 2.52 | 0.76 | [0.13, 9.04] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 14 | 106.56 ms | 4.07 | 1.09 | [96.15, 112.81] |
| Ratio 0.67 (2:3, no 1) | 11 | 107.50 ms | 2.41 | 0.73 | [103.50, 111.02] |
| Ratio 0.75 (3:4, no 1) | 11 | 106.56 ms | 3.34 | 1.01 | [100.26, 111.38] |
| Ratio 0.8 (4:5, no 1) | 16 | 105.11 ms | 4.05 | 1.01 | [97.50, 111.88] |
| Ratio 0.83 (5:6, no 1) | 11 | 107.63 ms | 4.40 | 1.33 | [96.62, 113.86] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 3.48 µV | 2.45 | 0.55 | [0.06, 9.38] |
| Ratio 0.67 (2:3, no 1) | 19 | 3.73 µV | 2.52 | 0.58 | [0.20, 9.88] |
| Ratio 0.75 (3:4, no 1) | 18 | 4.02 µV | 2.43 | 0.57 | [0.50, 7.67] |
| Ratio 0.8 (4:5, no 1) | 19 | 3.66 µV | 2.58 | 0.59 | [0.31, 7.71] |
| Ratio 0.83 (5:6, no 1) | 12 | 3.31 µV | 2.57 | 0.74 | [0.86, 10.16] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 491.18 ms | 11.71 | 2.62 | [471.37, 514.96] |
| Ratio 0.67 (2:3, no 1) | 19 | 491.44 ms | 13.63 | 3.13 | [465.09, 518.71] |
| Ratio 0.75 (3:4, no 1) | 18 | 490.72 ms | 11.52 | 2.72 | [470.82, 513.47] |
| Ratio 0.8 (4:5, no 1) | 19 | 496.43 ms | 11.60 | 2.66 | [473.52, 514.64] |
| Ratio 0.83 (5:6, no 1) | 12 | 497.97 ms | 19.76 | 5.70 | [463.15, 529.90] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 368.63, BIC = 390.01
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.20, *SE* = 0.316, *z* = 0.648, *p* = 0.517
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.42, *SE* = 0.341, *z* = -1.232, *p* = 0.218
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.64, *SE* = 0.338, *z* = -1.882, *p* = 0.060
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.76, *SE* = 0.393, *z* = -1.942, *p* = 0.052
- **SNR**: *β* = -0.21, *SE* = 0.032, *z* = -6.732, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.20 | 0.32 | -0.65 | 0.517 | 0.878 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.42 | 0.34 | 1.23 | 0.218 | 0.707 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.64 | 0.34 | 1.88 | 0.060 | 0.348 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.76 | 0.39 | 1.94 | 0.052 | 0.348 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.62 | 0.33 | 1.91 | 0.056 | 0.348 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.84 | 0.32 | 2.60 | 0.009 | 0.089 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.97 | 0.37 | 2.60 | 0.009 | 0.089 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.22 | 0.32 | 0.67 | 0.503 | 0.878 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.34 | 0.35 | 0.97 | 0.332 | 0.800 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.13 | 0.35 | 0.36 | 0.720 | 0.878 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.796, η²_G = 0.014
- Greenhouse-Geisser corrected: *p* = 0.709 (ε = 0.631)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -1.44 | 14 | = 0.857 | -0.27 [-0.92, -0.01] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.87 | 14 | = 0.857 | -0.23 [-0.70, 0.23] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.36 | 14 | = 0.857 | 0.08 [-0.60, 0.29] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.30 | 14 | = 0.857 | -0.09 [-0.71, 0.36] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.07 | 14 | = 0.949 | 0.02 [-0.29, 0.63] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.96 | 14 | = 0.857 | 0.31 [-0.25, 0.65] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 0.36 | 14 | = 0.857 | 0.11 [-0.57, 0.50] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.96 | 14 | = 0.857 | 0.28 [-0.34, 0.60] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.39 | 14 | = 0.857 | 0.09 [-0.41, 0.66] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.46 | 14 | = 0.857 | -0.15 [-0.73, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 710.72, BIC = 732.11
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.72, *SE* = 1.377, *z* = -1.250, *p* = 0.211
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -2.31, *SE* = 1.490, *z* = -1.547, *p* = 0.122
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.66, *SE* = 1.473, *z* = -0.450, *p* = 0.653
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.70, *SE* = 1.726, *z* = -0.404, *p* = 0.686
- **SNR**: *β* = 0.01, *SE* = 0.136, *z* = 0.063, *p* = 0.950

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 1.72 | 1.38 | 1.25 | 0.211 | 0.882 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 2.31 | 1.49 | 1.55 | 0.122 | 0.727 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.66 | 1.47 | 0.45 | 0.653 | 0.985 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.70 | 1.73 | 0.40 | 0.686 | 0.985 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.58 | 1.43 | 0.41 | 0.682 | 0.985 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -1.06 | 1.41 | -0.75 | 0.454 | 0.973 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -1.02 | 1.64 | -0.63 | 0.531 | 0.977 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -1.64 | 1.41 | -1.16 | 0.245 | 0.894 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -1.61 | 1.55 | -1.04 | 0.299 | 0.917 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.03 | 1.56 | 0.02 | 0.982 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.482, η²_G = 0.013
- Greenhouse-Geisser corrected: *p* = 0.414 (ε = 0.437)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 1.36 | 14 | = 0.489 | 0.16 [-0.03, 0.88] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 2.42 | 14 | = 0.274 | 0.35 [0.07, 1.05] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.26 | 14 | = 0.888 | 0.03 [-0.35, 0.54] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.54 | 14 | = 0.858 | 0.12 [-0.51, 0.56] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 1.55 | 14 | = 0.477 | 0.21 [-0.28, 0.64] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.93 | 14 | = 0.740 | -0.13 [-0.62, 0.27] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 0.05 | 14 | = 0.963 | 0.01 [-0.63, 0.44] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -2.10 | 14 | = 0.274 | -0.32 [-0.95, 0.03] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.68 | 14 | = 0.841 | -0.15 [-0.63, 0.44] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.40 | 14 | = 0.871 | 0.10 [-0.53, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 226.79, BIC = 243.94
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.16, *SE* = 0.500, *z* = -0.328, *p* = 0.743
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.35, *SE* = 0.499, *z* = 0.697, *p* = 0.486
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.01, *SE* = 0.450, *z* = 2.245, *p* = 0.025
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.45, *SE* = 0.522, *z* = 2.772, *p* = 0.006
- **SNR**: *β* = 0.49, *SE* = 0.096, *z* = 5.179, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.16 | 0.50 | 0.33 | 0.743 | 0.811 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.35 | 0.50 | -0.70 | 0.486 | 0.811 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -1.01 | 0.45 | -2.25 | 0.025 | 0.161 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -1.45 | 0.52 | -2.77 | 0.006 | 0.049 | * |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.51 | 0.54 | -0.95 | 0.340 | 0.811 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -1.17 | 0.50 | -2.33 | 0.020 | 0.146 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -1.61 | 0.57 | -2.81 | 0.005 | 0.048 | * |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.66 | 0.49 | -1.36 | 0.173 | 0.613 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -1.10 | 0.55 | -1.99 | 0.046 | 0.248 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -0.44 | 0.49 | -0.88 | 0.377 | 0.811 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.814, η²_G = 0.111
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.41 | 3 | = 0.775 | -0.25 [-0.71, 0.83] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.38 | 3 | = 0.775 | 0.26 [-1.13, 0.45] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.48 | 3 | = 0.775 | -0.41 [-1.02, 0.24] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.80 | 3 | = 0.775 | -0.57 [-1.26, 0.63] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.55 | 3 | = 0.775 | 0.38 [-1.22, 1.27] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.31 | 3 | = 0.775 | -0.22 [-1.10, 0.60] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.56 | 3 | = 0.775 | -0.47 [-1.36, 0.78] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.65 | 3 | = 0.775 | -0.50 [-1.13, 0.36] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.80 | 3 | = 0.775 | -0.63 [-1.31, 0.82] | medium | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.43 | 3 | = 0.775 | -0.34 [-1.05, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 341.50, BIC = 358.65
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.21, *SE* = 1.036, *z* = 0.205, *p* = 0.838
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.28, *SE* = 1.029, *z* = 0.274, *p* = 0.784
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.12, *SE* = 0.925, *z* = -1.213, *p* = 0.225
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.49, *SE* = 1.138, *z* = 1.306, *p* = 0.192
- **SNR**: *β* = 0.23, *SE* = 0.221, *z* = 1.057, *p* = 0.291

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.21 | 1.04 | -0.20 | 0.838 | 0.990 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.28 | 1.03 | -0.27 | 0.784 | 0.990 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 1.12 | 0.93 | 1.21 | 0.225 | 0.817 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -1.49 | 1.14 | -1.31 | 0.192 | 0.817 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.07 | 1.16 | -0.06 | 0.952 | 0.990 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 1.33 | 1.08 | 1.24 | 0.215 | 0.817 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -1.27 | 1.25 | -1.02 | 0.308 | 0.841 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 1.40 | 1.00 | 1.40 | 0.162 | 0.796 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -1.20 | 1.18 | -1.02 | 0.309 | 0.841 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -2.61 | 1.08 | -2.41 | 0.016 | 0.149 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.27, *p* = 0.335, η²_G = 0.138
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.94 | 3 | = 0.586 | 0.40 [-0.68, 0.86] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.61 | 3 | = 0.651 | -0.15 [-0.91, 0.64] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 1.14 | 3 | = 0.562 | 0.48 [-0.31, 0.92] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.32 | 3 | = 0.562 | -0.51 [-1.54, 0.44] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.83 | 3 | = 0.586 | -0.50 [-1.72, 0.88] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.08 | 3 | = 0.942 | -0.05 [-0.50, 1.23] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -1.37 | 3 | = 0.562 | -0.80 [-1.43, 0.73] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 1.19 | 3 | = 0.562 | 0.58 [-0.35, 1.13] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.23 | 3 | = 0.562 | -0.34 [-1.95, 0.43] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -1.42 | 3 | = 0.562 | -0.94 [-1.84, 0.27] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 344.78, BIC = 364.60
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.17, *SE* = 0.394, *z* = 0.430, *p* = 0.667
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.54, *SE* = 0.404, *z* = 1.331, *p* = 0.183
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.62, *SE* = 0.413, *z* = 1.496, *p* = 0.135
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.09, *SE* = 0.533, *z* = -0.176, *p* = 0.861
- **SNR**: *β* = 0.20, *SE* = 0.042, *z* = 4.770, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.17 | 0.39 | -0.43 | 0.667 | 0.979 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.54 | 0.40 | -1.33 | 0.183 | 0.802 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.62 | 0.41 | -1.50 | 0.135 | 0.765 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.09 | 0.53 | 0.18 | 0.861 | 0.979 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.37 | 0.41 | -0.89 | 0.371 | 0.901 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.45 | 0.41 | -1.09 | 0.278 | 0.858 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.26 | 0.53 | 0.50 | 0.619 | 0.979 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.08 | 0.42 | -0.19 | 0.849 | 0.979 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.63 | 0.54 | 1.17 | 0.241 | 0.855 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.71 | 0.49 | 1.45 | 0.148 | 0.765 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.05, *p* = 0.029, η²_G = 0.113
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.80 | 9 | = 0.741 | -0.10 [-0.56, 0.40] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.04 | 9 | = 0.655 | -0.19 [-0.79, 0.25] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.38 | 9 | = 0.887 | -0.11 [-0.59, 0.41] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 1.87 | 9 | = 0.237 | 0.68 [-0.15, 1.21] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.47 | 9 | = 0.887 | -0.08 [-0.76, 0.32] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.02 | 9 | = 0.985 | -0.00 [-0.49, 0.50] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.98 | 9 | = 0.237 | 0.78 [-0.15, 1.21] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.26 | 9 | = 0.888 | 0.08 [-0.21, 0.89] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 2.20 | 9 | = 0.237 | 0.88 [-0.15, 1.29] | large | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 2.28 | 9 | = 0.237 | 0.80 [-0.03, 1.48] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 696.61, BIC = 716.42
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.77, *SE* = 3.122, *z* = 0.247, *p* = 0.805
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.04, *SE* = 3.194, *z* = -0.012, *p* = 0.990
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 5.66, *SE* = 3.242, *z* = 1.746, *p* = 0.081
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 7.52, *SE* = 4.020, *z* = 1.871, *p* = 0.061
- **SNR**: *β* = -0.10, *SE* = 0.297, *z* = -0.328, *p* = 0.743

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.77 | 3.12 | -0.25 | 0.805 | 0.992 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.04 | 3.19 | 0.01 | 0.990 | 0.992 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -5.66 | 3.24 | -1.75 | 0.081 | 0.491 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -7.52 | 4.02 | -1.87 | 0.061 | 0.469 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.81 | 3.25 | 0.25 | 0.803 | 0.992 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -4.89 | 3.26 | -1.50 | 0.133 | 0.511 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -6.75 | 4.01 | -1.68 | 0.093 | 0.491 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -5.70 | 3.33 | -1.71 | 0.087 | 0.491 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -7.56 | 4.07 | -1.86 | 0.063 | 0.469 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -1.86 | 3.80 | -0.49 | 0.624 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.70, *p* = 0.046, η²_G = 0.105
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.96 | 9 | = 0.405 | -0.18 [-0.65, 0.32] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.68 | 9 | = 0.212 | -0.47 [-0.57, 0.46] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -2.97 | 9 | = 0.157 | -1.03 [-1.26, -0.15] | large | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.80 | 9 | = 0.212 | -0.69 [-1.19, 0.16] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -1.15 | 9 | = 0.350 | -0.24 [-0.55, 0.52] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -2.25 | 9 | = 0.212 | -0.71 [-0.92, 0.12] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -1.90 | 9 | = 0.212 | -0.53 [-1.24, 0.12] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -1.71 | 9 | = 0.212 | -0.50 [-0.82, 0.27] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.20 | 9 | = 0.350 | -0.37 [-1.20, 0.22] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.12 | 9 | = 0.911 | -0.04 [-0.67, 0.67] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.029) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.046) (no significant pairwise comparisons)

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
