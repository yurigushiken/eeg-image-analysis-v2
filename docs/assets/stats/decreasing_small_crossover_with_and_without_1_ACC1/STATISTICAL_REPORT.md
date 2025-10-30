# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:18:37

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
| Crossover (with 1) | 24 | -3.51 µV | 1.56 | 0.32 | [-7.02, -0.97] |
| Crossover (without 1) | 24 | -3.96 µV | 1.79 | 0.37 | [-7.80, -0.75] |
| Small (with 1) | 20 | -2.62 µV | 2.01 | 0.45 | [-7.09, -0.23] |
| Small (without 1) | 23 | -3.67 µV | 2.11 | 0.44 | [-8.17, -0.09] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 178.55 ms | 9.33 | 1.90 | [162.89, 207.74] |
| Crossover (without 1) | 24 | 177.96 ms | 9.50 | 1.94 | [161.73, 209.25] |
| Small (with 1) | 20 | 178.98 ms | 10.98 | 2.45 | [159.47, 205.59] |
| Small (without 1) | 23 | 177.45 ms | 13.41 | 2.80 | [156.58, 214.51] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 15 | 1.73 µV | 1.32 | 0.34 | [0.05, 4.63] |
| Crossover (without 1) | 14 | 1.50 µV | 0.99 | 0.26 | [0.33, 3.11] |
| Small (with 1) | 19 | 1.84 µV | 1.63 | 0.37 | [-0.06, 6.21] |
| Small (without 1) | 8 | 2.22 µV | 1.43 | 0.50 | [0.46, 4.14] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 15 | 113.09 ms | 4.62 | 1.19 | [104.02, 123.07] |
| Crossover (without 1) | 14 | 112.92 ms | 4.60 | 1.23 | [105.73, 119.24] |
| Small (with 1) | 19 | 113.62 ms | 3.81 | 0.87 | [102.76, 118.08] |
| Small (without 1) | 8 | 111.33 ms | 2.73 | 0.97 | [107.76, 115.36] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 21 | 3.49 µV | 2.48 | 0.54 | [0.10, 9.16] |
| Crossover (without 1) | 20 | 3.59 µV | 2.39 | 0.53 | [0.08, 9.31] |
| Small (with 1) | 20 | 3.96 µV | 2.44 | 0.55 | [1.02, 8.62] |
| Small (without 1) | 18 | 4.35 µV | 3.22 | 0.76 | [0.31, 12.41] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 21 | 478.99 ms | 12.10 | 2.64 | [451.55, 498.94] |
| Crossover (without 1) | 20 | 479.95 ms | 15.47 | 3.46 | [447.81, 513.93] |
| Small (with 1) | 20 | 483.09 ms | 12.01 | 2.69 | [456.72, 501.11] |
| Small (without 1) | 18 | 486.94 ms | 18.13 | 4.27 | [445.00, 526.49] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 301.17, BIC = 318.75
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.59, *SE* = 0.258, *z* = -2.299, *p* = 0.021
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.02, *SE* = 0.324, *z* = 0.051, *p* = 0.959
- **Small (without 1) vs Crossover (with 1)**: *β* = -1.18, *SE* = 0.315, *z* = -3.733, *p* < .001
- **SNR**: *β* = -0.19, *SE* = 0.030, *z* = -6.252, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.59 | 0.26 | 2.30 | 0.021 | 0.083 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.02 | 0.32 | -0.05 | 0.959 | 0.959 | n.s. |
| Crossover (with 1) - Small (without 1) | 1.17 | 0.31 | 3.73 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.61 | 0.31 | -1.95 | 0.051 | 0.145 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.58 | 0.30 | 1.92 | 0.054 | 0.145 | n.s. |
| Small (with 1) - Small (without 1) | 1.19 | 0.28 | 4.30 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.65, *p* < .001, η²_G = 0.109
- Greenhouse-Geisser corrected: *p* = 0.005 (ε = 0.501)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 5.32 | 18 | < .001 | 0.30 [0.62, 1.71] | small | *** |
| Crossover (with 1) vs Small (with 1) | -2.93 | 18 | = 0.013 | -0.68 [-1.15, -0.12] | medium | * |
| Crossover (with 1) vs Small (without 1) | 0.28 | 18 | = 0.784 | 0.06 [-0.40, 0.46] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -3.61 | 18 | = 0.004 | -0.89 [-1.30, -0.24] | large | ** |
| Crossover (without 1) vs Small (without 1) | -0.81 | 18 | = 0.511 | -0.19 [-0.68, 0.19] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 4.61 | 18 | < .001 | 0.63 [0.46, 1.66] | medium | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 637.95, BIC = 655.53
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.70, *SE* = 1.540, *z* = -0.456, *p* = 0.648
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.37, *SE* = 1.964, *z* = 0.190, *p* = 0.849
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.82, *SE* = 1.906, *z* = -0.433, *p* = 0.665
- **SNR**: *β* = -0.15, *SE* = 0.187, *z* = -0.786, *p* = 0.432

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.70 | 1.54 | 0.46 | 0.648 | 0.985 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.37 | 1.96 | -0.19 | 0.849 | 0.985 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.82 | 1.91 | 0.43 | 0.665 | 0.985 | n.s. |
| Crossover (without 1) - Small (with 1) | -1.08 | 1.89 | -0.57 | 0.568 | 0.985 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.12 | 1.83 | 0.07 | 0.947 | 0.985 | n.s. |
| Small (with 1) - Small (without 1) | 1.20 | 1.65 | 0.73 | 0.468 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.01, *p* = 0.396, η²_G = 0.012
- Greenhouse-Geisser corrected: *p* = 0.358 (ε = 0.509)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.86 | 18 | = 0.505 | 0.04 [-0.13, 0.73] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.84 | 18 | = 0.505 | -0.13 [-0.64, 0.30] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.82 | 18 | = 0.505 | 0.17 [-0.45, 0.41] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.93 | 18 | = 0.505 | -0.17 [-0.65, 0.30] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.60 | 18 | = 0.553 | 0.14 [-0.51, 0.36] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 1.82 | 18 | = 0.505 | 0.26 [-0.08, 0.92] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 142.36, BIC = 156.54
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.00, *SE* = 0.235, *z* = -0.012, *p* = 0.991
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.60, *SE* = 0.227, *z* = 2.653, *p* = 0.008
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.10, *SE* = 0.324, *z* = 3.411, *p* = 0.001
- **SNR**: *β* = 0.36, *SE* = 0.044, *z* = 8.079, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.00 | 0.24 | 0.01 | 0.991 | 0.991 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.60 | 0.23 | -2.65 | 0.008 | 0.032 | * |
| Crossover (with 1) - Small (without 1) | -1.11 | 0.32 | -3.41 | < .001 | 0.003 | ** |
| Crossover (without 1) - Small (with 1) | -0.60 | 0.23 | -2.63 | 0.008 | 0.032 | * |
| Crossover (without 1) - Small (without 1) | -1.11 | 0.31 | -3.54 | < .001 | 0.002 | ** |
| Small (with 1) - Small (without 1) | -0.50 | 0.30 | -1.68 | 0.092 | 0.176 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.47, *p* = 0.262, η²_G = 0.102
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 2.14 | 5 | = 0.410 | 0.52 [-0.04, 1.20] | medium | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.99 | 5 | = 0.549 | -0.31 [-1.09, 0.13] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.77 | 5 | = 0.572 | 0.36 [-0.76, 1.39] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.77 | 5 | = 0.410 | -0.75 [-1.34, -0.00] | medium | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.19 | 5 | = 0.856 | -0.08 [-1.13, 0.97] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 1.21 | 5 | = 0.549 | 0.60 [-0.59, 1.12] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 314.27, BIC = 328.44
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.41, *SE* = 1.023, *z* = -0.398, *p* = 0.691
- **Small (with 1) vs Crossover (with 1)**: *β* = 1.21, *SE* = 1.002, *z* = 1.211, *p* = 0.226
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.43, *SE* = 1.449, *z* = -0.294, *p* = 0.769
- **SNR**: *β* = 0.04, *SE* = 0.199, *z* = 0.178, *p* = 0.858

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.41 | 1.02 | 0.40 | 0.691 | 0.970 | n.s. |
| Crossover (with 1) - Small (with 1) | -1.21 | 1.00 | -1.21 | 0.226 | 0.687 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.43 | 1.45 | 0.29 | 0.769 | 0.970 | n.s. |
| Crossover (without 1) - Small (with 1) | -1.62 | 1.01 | -1.60 | 0.110 | 0.501 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.02 | 1.40 | 0.01 | 0.990 | 0.990 | n.s. |
| Small (with 1) - Small (without 1) | 1.64 | 1.30 | 1.26 | 0.207 | 0.687 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.01, *p* = 0.416, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.28 | 5 | = 0.788 | 0.06 [-0.14, 1.08] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -1.40 | 5 | = 0.656 | -0.36 [-0.96, 0.24] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 1.02 | 5 | = 0.656 | 0.28 [-0.68, 1.51] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.84 | 5 | = 0.656 | -0.32 [-1.03, 0.22] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.40 | 5 | = 0.788 | 0.14 [-0.89, 1.22] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 2.13 | 5 | = 0.518 | 0.64 [-0.59, 1.11] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 276.58, BIC = 293.16
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.08, *SE* = 0.264, *z* = 0.313, *p* = 0.754
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.71, *SE* = 0.275, *z* = 2.574, *p* = 0.010
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.27, *SE* = 0.318, *z* = 3.985, *p* < .001
- **SNR**: *β* = 0.11, *SE* = 0.023, *z* = 4.853, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.08 | 0.26 | -0.31 | 0.754 | 0.754 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.71 | 0.27 | -2.57 | 0.010 | 0.040 | * |
| Crossover (with 1) - Small (without 1) | -1.27 | 0.32 | -3.99 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.62 | 0.27 | -2.28 | 0.022 | 0.066 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.19 | 0.31 | -3.85 | < .001 | < .001 | *** |
| Small (with 1) - Small (without 1) | -0.56 | 0.29 | -1.94 | 0.053 | 0.103 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.81, *p* = 0.496, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.456 (ε = 0.677)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.40 | 16 | = 0.698 | 0.02 [-0.28, 0.67] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.47 | 16 | = 0.698 | -0.08 [-0.69, 0.26] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -1.12 | 16 | = 0.698 | -0.16 [-0.76, 0.25] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.61 | 16 | = 0.698 | -0.09 [-0.71, 0.27] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -1.32 | 16 | = 0.698 | -0.18 [-0.82, 0.20] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | -0.70 | 16 | = 0.698 | -0.09 [-0.69, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 614.68, BIC = 631.26
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 1.16, *SE* = 2.528, *z* = 0.459, *p* = 0.646
- **Small (with 1) vs Crossover (with 1)**: *β* = 5.40, *SE* = 2.614, *z* = 2.067, *p* = 0.039
- **Small (without 1) vs Crossover (with 1)**: *β* = 7.80, *SE* = 2.977, *z* = 2.620, *p* = 0.009
- **SNR**: *β* = 0.01, *SE* = 0.202, *z* = 0.025, *p* = 0.980

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -1.16 | 2.53 | -0.46 | 0.646 | 0.646 | n.s. |
| Crossover (with 1) - Small (with 1) | -5.40 | 2.61 | -2.07 | 0.039 | 0.146 | n.s. |
| Crossover (with 1) - Small (without 1) | -7.80 | 2.98 | -2.62 | 0.009 | 0.052 | n.s. |
| Crossover (without 1) - Small (with 1) | -4.24 | 2.61 | -1.63 | 0.104 | 0.281 | n.s. |
| Crossover (without 1) - Small (without 1) | -6.64 | 2.90 | -2.29 | 0.022 | 0.106 | n.s. |
| Small (with 1) - Small (without 1) | -2.40 | 2.75 | -0.87 | 0.383 | 0.620 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.84, *p* = 0.047, η²_G = 0.058
- Greenhouse-Geisser corrected: *p* = 0.095 (ε = 0.465)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.63 | 16 | = 0.540 | 0.04 [-0.63, 0.32] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -1.51 | 16 | = 0.226 | -0.45 [-0.91, 0.07] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | -1.72 | 16 | = 0.208 | -0.47 [-1.01, 0.04] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -1.77 | 16 | = 0.208 | -0.49 [-0.81, 0.18] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | -1.95 | 16 | = 0.208 | -0.50 [-1.05, 0.01] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.78 | 16 | = 0.534 | -0.11 [-0.71, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Crossover (with 1) showed greater amplitude than Crossover (without 1) (*d* = 0.30)
  - Crossover (with 1) showed smaller amplitude than Small (with 1) (*d* = -0.68)
  - Crossover (without 1) showed smaller amplitude than Small (with 1) (*d* = -0.89)
  - Small (with 1) showed greater amplitude than Small (without 1) (*d* = 0.63)
**P3b latency:** Significant main effect of condition (*p* = 0.047) (no significant pairwise comparisons)

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
