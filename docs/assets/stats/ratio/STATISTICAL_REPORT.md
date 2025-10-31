# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:29:10

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
| Ratio 0.5 (1:2) | 23 | -3.58 µV | 1.76 | 0.37 | [-7.87, -0.39] |
| Ratio 0.67 (2:3) | 23 | -3.65 µV | 1.62 | 0.34 | [-7.94, -1.11] |
| Ratio 0.75 (3:4) | 23 | -3.65 µV | 1.80 | 0.38 | [-7.97, -0.11] |
| Ratio 0.8 (4:5) | 23 | -3.90 µV | 1.92 | 0.40 | [-7.70, -0.65] |
| Ratio 0.83 (5:6) | 24 | -3.86 µV | 1.91 | 0.39 | [-8.81, -0.38] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 23 | 174.56 ms | 8.43 | 1.76 | [160.92, 198.94] |
| Ratio 0.67 (2:3) | 23 | 172.93 ms | 6.65 | 1.39 | [156.83, 186.12] |
| Ratio 0.75 (3:4) | 23 | 171.00 ms | 8.15 | 1.70 | [151.26, 186.92] |
| Ratio 0.8 (4:5) | 23 | 174.11 ms | 7.09 | 1.48 | [160.93, 187.15] |
| Ratio 0.83 (5:6) | 24 | 174.08 ms | 9.51 | 1.94 | [154.71, 200.86] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 1.15 µV | 1.32 | 0.34 | [0.07, 4.95] |
| Ratio 0.67 (2:3) | 13 | 1.34 µV | 1.21 | 0.34 | [0.01, 3.62] |
| Ratio 0.75 (3:4) | 14 | 1.39 µV | 1.39 | 0.37 | [0.08, 4.96] |
| Ratio 0.8 (4:5) | 12 | 1.90 µV | 1.52 | 0.44 | [0.24, 4.99] |
| Ratio 0.83 (5:6) | 13 | 1.36 µV | 1.21 | 0.34 | [-0.00, 3.19] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 104.06 ms | 4.14 | 1.07 | [94.98, 111.59] |
| Ratio 0.67 (2:3) | 13 | 103.44 ms | 4.20 | 1.17 | [92.45, 109.17] |
| Ratio 0.75 (3:4) | 14 | 102.23 ms | 4.41 | 1.18 | [94.63, 109.62] |
| Ratio 0.8 (4:5) | 12 | 101.04 ms | 3.99 | 1.15 | [94.84, 104.96] |
| Ratio 0.83 (5:6) | 13 | 102.14 ms | 4.55 | 1.26 | [92.35, 108.21] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 3.24 µV | 2.34 | 0.52 | [0.14, 7.83] |
| Ratio 0.67 (2:3) | 18 | 3.62 µV | 2.41 | 0.57 | [0.42, 8.68] |
| Ratio 0.75 (3:4) | 18 | 3.69 µV | 2.47 | 0.58 | [0.44, 7.68] |
| Ratio 0.8 (4:5) | 16 | 3.76 µV | 2.71 | 0.68 | [0.24, 9.94] |
| Ratio 0.83 (5:6) | 12 | 2.10 µV | 2.29 | 0.66 | [0.07, 6.99] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 489.06 ms | 15.99 | 3.57 | [468.69, 527.12] |
| Ratio 0.67 (2:3) | 18 | 485.36 ms | 12.75 | 3.00 | [460.37, 506.50] |
| Ratio 0.75 (3:4) | 18 | 485.55 ms | 12.38 | 2.92 | [457.66, 500.92] |
| Ratio 0.8 (4:5) | 16 | 488.86 ms | 15.98 | 3.99 | [449.39, 514.14] |
| Ratio 0.83 (5:6) | 12 | 494.63 ms | 26.02 | 7.51 | [441.04, 531.50] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 360.34, BIC = 382.37
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.34, *SE* = 0.252, *z* = -1.348, *p* = 0.178
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -0.72, *SE* = 0.266, *z* = -2.729, *p* = 0.006
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.87, *SE* = 0.261, *z* = -3.328, *p* = 0.001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -0.96, *SE* = 0.261, *z* = -3.686, *p* < .001
- **SNR**: *β* = -0.16, *SE* = 0.022, *z* = -7.171, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.34 | 0.25 | 1.35 | 0.178 | 0.543 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 0.73 | 0.27 | 2.73 | 0.006 | 0.050 | * |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.87 | 0.26 | 3.33 | < .001 | 0.008 | ** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 0.96 | 0.26 | 3.69 | < .001 | 0.002 | ** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.39 | 0.26 | 1.51 | 0.131 | 0.505 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.53 | 0.25 | 2.09 | 0.036 | 0.199 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.62 | 0.25 | 2.47 | 0.014 | 0.092 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.14 | 0.25 | 0.57 | 0.566 | 0.812 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.24 | 0.25 | 0.95 | 0.342 | 0.715 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.09 | 0.25 | 0.38 | 0.707 | 0.812 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.561, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.43 | 22 | = 0.918 | 0.04 [-0.34, 0.52] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.21 | 22 | = 0.931 | 0.04 [-0.39, 0.48] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 1.04 | 22 | = 0.772 | 0.17 [-0.22, 0.65] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.45 | 22 | = 0.772 | 0.24 [-0.14, 0.75] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.02 | 22 | = 0.983 | -0.00 [-0.44, 0.43] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.76 | 22 | = 0.785 | 0.14 [-0.28, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.17 | 22 | = 0.772 | 0.21 [-0.20, 0.68] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.73 | 22 | = 0.785 | 0.14 [-0.28, 0.59] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 1.12 | 22 | = 0.772 | 0.20 [-0.20, 0.67] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.34 | 22 | = 0.918 | 0.06 [-0.36, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 731.57, BIC = 753.59
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -1.62, *SE* = 1.153, *z* = -1.401, *p* = 0.161
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -3.53, *SE* = 1.215, *z* = -2.908, *p* = 0.004
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.43, *SE* = 1.193, *z* = -0.360, *p* = 0.719
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.39, *SE* = 1.196, *z* = -1.164, *p* = 0.245
- **SNR**: *β* = 0.01, *SE* = 0.101, *z* = 0.064, *p* = 0.949

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 1.62 | 1.15 | 1.40 | 0.161 | 0.652 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 3.53 | 1.21 | 2.91 | 0.004 | 0.036 | * |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.43 | 1.19 | 0.36 | 0.719 | 0.921 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.39 | 1.20 | 1.16 | 0.245 | 0.754 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 1.92 | 1.17 | 1.64 | 0.101 | 0.524 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -1.19 | 1.16 | -1.03 | 0.304 | 0.765 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.22 | 1.16 | -0.19 | 0.846 | 0.921 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -3.10 | 1.14 | -2.72 | 0.007 | 0.058 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -2.14 | 1.14 | -1.87 | 0.061 | 0.395 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.96 | 1.14 | 0.84 | 0.398 | 0.782 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.84, *p* = 0.029, η²_G = 0.027
- Greenhouse-Geisser corrected: *p* = 0.051 (ε = 0.676)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 1.75 | 22 | = 0.214 | 0.21 [-0.08, 0.81] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 2.65 | 22 | = 0.145 | 0.43 [0.09, 1.02] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.50 | 22 | = 0.688 | 0.06 [-0.33, 0.54] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.18 | 22 | = 0.379 | 0.20 [-0.19, 0.69] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 2.01 | 22 | = 0.191 | 0.26 [-0.03, 0.87] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.14 | 22 | = 0.379 | -0.17 [-0.68, 0.20] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.02 | 22 | = 0.986 | 0.00 [-0.43, 0.44] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -2.23 | 22 | = 0.182 | -0.41 [-0.92, -0.01] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.68 | 22 | = 0.214 | -0.24 [-0.80, 0.09] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.83 | 22 | = 0.519 | 0.16 [-0.26, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 169.99, BIC = 187.63
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.35, *SE* = 0.243, *z* = 1.450, *p* = 0.147
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.56, *SE* = 0.247, *z* = 2.280, *p* = 0.023
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 1.04, *SE* = 0.254, *z* = 4.088, *p* < .001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.66, *SE* = 0.253, *z* = 2.601, *p* = 0.009
- **SNR**: *β* = 0.24, *SE* = 0.038, *z* = 6.412, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.35 | 0.24 | -1.45 | 0.147 | 0.540 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.56 | 0.25 | -2.28 | 0.023 | 0.148 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -1.04 | 0.25 | -4.09 | < .001 | < .001 | *** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.66 | 0.25 | -2.60 | 0.009 | 0.076 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.21 | 0.26 | -0.82 | 0.411 | 0.653 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.68 | 0.26 | -2.62 | 0.009 | 0.076 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.30 | 0.26 | -1.18 | 0.239 | 0.560 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.47 | 0.26 | -1.82 | 0.068 | 0.345 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -0.09 | 0.26 | -0.37 | 0.710 | 0.710 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.38 | 0.26 | 1.46 | 0.144 | 0.540 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.32, *p* = 0.862, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.02 | 4 | = 0.987 | 0.00 [-0.73, 0.62] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -0.86 | 4 | = 0.963 | -0.14 [-1.10, 0.38] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.48 | 4 | = 0.963 | -0.21 [-1.07, 0.32] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.27 | 4 | = 0.974 | 0.11 [-0.92, 0.53] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.58 | 4 | = 0.963 | -0.16 [-1.09, 0.61] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.54 | 4 | = 0.963 | -0.24 [-1.12, 0.46] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.45 | 4 | = 0.963 | 0.12 [-0.41, 1.36] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.17 | 4 | = 0.974 | -0.06 [-0.97, 0.71] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.85 | 4 | = 0.963 | 0.28 [-0.75, 0.93] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 1.12 | 4 | = 0.963 | 0.38 [-0.62, 1.07] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 375.20, BIC = 392.84
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -1.40, *SE* = 1.058, *z* = -1.324, *p* = 0.185
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -0.87, *SE* = 1.088, *z* = -0.803, *p* = 0.422
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.96, *SE* = 1.104, *z* = -1.770, *p* = 0.077
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.44, *SE* = 1.101, *z* = -1.303, *p* = 0.193
- **SNR**: *β* = -0.00, *SE* = 0.154, *z* = -0.016, *p* = 0.987

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 1.40 | 1.06 | 1.32 | 0.185 | 0.842 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 0.87 | 1.09 | 0.80 | 0.422 | 0.963 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.95 | 1.10 | 1.77 | 0.077 | 0.550 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.44 | 1.10 | 1.30 | 0.193 | 0.842 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.53 | 1.14 | -0.46 | 0.644 | 0.992 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.55 | 1.15 | 0.48 | 0.631 | 0.992 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.03 | 1.14 | 0.03 | 0.976 | 0.992 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 1.08 | 1.14 | 0.95 | 0.342 | 0.947 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.56 | 1.12 | 0.50 | 0.616 | 0.992 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -0.52 | 1.13 | -0.46 | 0.646 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.02, *p* = 0.429, η²_G = 0.129
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.39 | 4 | = 0.715 | -0.09 [-0.30, 1.10] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 1.19 | 4 | = 0.652 | 0.69 [-0.77, 0.66] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.54 | 4 | = 0.703 | 0.28 [-0.08, 1.40] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.37 | 4 | = 0.652 | 0.52 [-0.28, 1.23] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 1.10 | 4 | = 0.652 | 0.77 [-0.87, 0.80] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.78 | 4 | = 0.682 | 0.40 [-0.57, 0.98] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.62 | 4 | = 0.652 | 0.63 [-0.61, 1.08] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.96 | 4 | = 0.652 | -0.62 [-0.62, 1.07] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.52 | 4 | = 0.703 | -0.35 [-0.99, 0.69] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 1.45 | 4 | = 0.652 | 0.42 [-0.55, 1.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 324.37, BIC = 343.82
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.56, *SE* = 0.396, *z* = 1.418, *p* = 0.156
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.72, *SE* = 0.405, *z* = 1.771, *p* = 0.077
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.98, *SE* = 0.427, *z* = 2.283, *p* = 0.022
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -0.40, *SE* = 0.521, *z* = -0.776, *p* = 0.438
- **SNR**: *β* = 0.23, *SE* = 0.035, *z* = 6.537, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.56 | 0.40 | -1.42 | 0.156 | 0.572 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.72 | 0.40 | -1.77 | 0.077 | 0.380 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.98 | 0.43 | -2.28 | 0.022 | 0.175 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 0.40 | 0.52 | 0.78 | 0.438 | 0.822 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.15 | 0.41 | -0.38 | 0.705 | 0.822 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.41 | 0.42 | -0.98 | 0.329 | 0.797 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.97 | 0.50 | 1.93 | 0.053 | 0.318 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.26 | 0.42 | -0.61 | 0.541 | 0.822 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 1.12 | 0.49 | 2.31 | 0.021 | 0.175 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 1.38 | 0.49 | 2.82 | 0.005 | 0.047 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.12, *p* = 0.027, η²_G = 0.144
- Greenhouse-Geisser corrected: *p* = 0.085 (ε = 0.392)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.38 | 9 | = 0.977 | -0.03 [-0.56, 0.44] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.20 | 9 | = 0.977 | 0.04 [-0.56, 0.47] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.11 | 9 | = 0.977 | -0.04 [-0.59, 0.48] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 2.30 | 9 | = 0.157 | 1.00 [0.02, 1.55] | large | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.27 | 9 | = 0.977 | 0.07 [-0.54, 0.53] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.03 | 9 | = 0.977 | -0.01 [-0.49, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 2.35 | 9 | = 0.157 | 1.01 [0.03, 1.58] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.20 | 9 | = 0.977 | -0.07 [-0.52, 0.64] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 1.69 | 9 | = 0.315 | 0.86 [-0.09, 1.29] | large | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 4.16 | 9 | = 0.025 | 0.98 [0.34, 2.29] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 704.30, BIC = 723.75
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -2.74, *SE* = 4.019, *z* = -0.683, *p* = 0.495
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -3.18, *SE* = 4.082, *z* = -0.779, *p* = 0.436
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.57, *SE* = 4.294, *z* = 0.133, *p* = 0.894
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 4.72, *SE* = 5.125, *z* = 0.920, *p* = 0.358
- **SNR**: *β* = -0.40, *SE* = 0.342, *z* = -1.175, *p* = 0.240

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 2.74 | 4.02 | 0.68 | 0.495 | 0.971 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 3.18 | 4.08 | 0.78 | 0.436 | 0.971 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.57 | 4.29 | -0.13 | 0.894 | 0.989 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -4.72 | 5.13 | -0.92 | 0.358 | 0.971 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.44 | 4.12 | 0.11 | 0.916 | 0.989 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -3.32 | 4.29 | -0.77 | 0.439 | 0.971 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -7.46 | 4.98 | -1.50 | 0.134 | 0.726 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -3.75 | 4.30 | -0.87 | 0.382 | 0.971 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -7.90 | 4.86 | -1.62 | 0.104 | 0.668 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -4.14 | 4.92 | -0.84 | 0.400 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.35, *p* = 0.006, η²_G = 0.168
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.23 | 9 | = 0.972 | 0.05 [-0.52, 0.48] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.08 | 9 | = 0.972 | 0.03 [-0.40, 0.64] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -2.55 | 9 | = 0.077 | -1.01 [-0.76, 0.32] | large | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -2.00 | 9 | = 0.127 | -0.83 [-1.49, 0.02] | large | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.04 | 9 | = 0.972 | -0.01 [-0.45, 0.61] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -2.60 | 9 | = 0.077 | -0.92 [-0.80, 0.33] | large | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -2.37 | 9 | = 0.083 | -0.81 [-1.63, -0.06] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -3.18 | 9 | = 0.077 | -0.86 [-1.30, -0.03] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -2.87 | 9 | = 0.077 | -0.78 [-1.01, 0.30] | medium | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.73 | 9 | = 0.694 | -0.17 [-0.95, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.029) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.027). Post-hoc tests revealed:
  - Ratio 0.8 (4:5) showed greater amplitude than Ratio 0.83 (5:6) (*d* = 0.98)
**P3b latency:** Significant main effect of condition (*p* = 0.006) (no significant pairwise comparisons)

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
