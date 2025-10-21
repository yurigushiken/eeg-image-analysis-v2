# Statistical Analysis Report: tables

**Generated:** 2025-10-20 21:51:46

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
| 2 to 1 | 16 | -2.80 µV | 2.07 | 0.52 | [-8.56, -0.10] |
| 2 to 2 | 22 | -3.21 µV | 1.92 | 0.41 | [-7.72, -0.19] |
| 2 to 3 | 21 | -3.57 µV | 1.34 | 0.29 | [-5.98, -1.03] |
| 2 to 4 | 21 | -4.37 µV | 2.10 | 0.46 | [-10.88, -1.48] |
| 2 to 5 | 24 | -4.15 µV | 2.43 | 0.50 | [-11.24, -0.32] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 178.08 ms | 7.12 | 1.78 | [161.55, 186.09] |
| 2 to 2 | 22 | 172.57 ms | 12.17 | 2.60 | [150.03, 193.06] |
| 2 to 3 | 21 | 172.23 ms | 7.37 | 1.61 | [156.88, 189.35] |
| 2 to 4 | 21 | 171.85 ms | 7.11 | 1.55 | [154.05, 183.51] |
| 2 to 5 | 24 | 175.24 ms | 10.17 | 2.08 | [156.54, 196.90] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 3.13 µV | 2.38 | 0.58 | [0.68, 7.96] |
| 2 to 2 | 12 | 1.92 µV | 1.64 | 0.47 | [0.31, 5.63] |
| 2 to 3 | 13 | 1.91 µV | 1.22 | 0.34 | [0.18, 4.26] |
| 2 to 4 | 15 | 1.84 µV | 1.39 | 0.36 | [-0.09, 5.23] |
| 2 to 5 | 12 | 1.65 µV | 2.31 | 0.67 | [0.01, 8.46] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 109.94 ms | 4.81 | 1.17 | [101.46, 118.17] |
| 2 to 2 | 12 | 107.50 ms | 7.95 | 2.30 | [97.26, 122.18] |
| 2 to 3 | 13 | 108.31 ms | 7.51 | 2.08 | [98.69, 121.48] |
| 2 to 4 | 15 | 107.64 ms | 8.67 | 2.24 | [90.58, 123.94] |
| 2 to 5 | 12 | 106.17 ms | 8.11 | 2.34 | [94.22, 121.64] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 3.63 µV | 2.77 | 0.62 | [0.41, 9.51] |
| 2 to 2 | 13 | 2.17 µV | 1.80 | 0.50 | [0.03, 6.57] |
| 2 to 3 | 18 | 4.02 µV | 2.73 | 0.64 | [0.21, 9.67] |
| 2 to 4 | 19 | 4.58 µV | 3.60 | 0.82 | [0.37, 12.22] |
| 2 to 5 | 23 | 3.12 µV | 2.12 | 0.44 | [0.16, 7.51] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 473.63 ms | 17.85 | 3.99 | [447.39, 509.61] |
| 2 to 2 | 13 | 457.05 ms | 26.84 | 7.44 | [395.88, 500.68] |
| 2 to 3 | 18 | 456.83 ms | 20.41 | 4.81 | [414.10, 507.69] |
| 2 to 4 | 19 | 469.12 ms | 26.79 | 6.15 | [410.57, 516.45] |
| 2 to 5 | 23 | 455.16 ms | 27.13 | 5.66 | [395.43, 501.14] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 392.11, BIC = 413.26
- **2 to 2 vs 2 to 1**: *β* = -0.40, *SE* = 0.442, *z* = -0.903, *p* = 0.367
- **2 to 3 vs 2 to 1**: *β* = -0.34, *SE* = 0.451, *z* = -0.757, *p* = 0.449
- **2 to 4 vs 2 to 1**: *β* = -0.79, *SE* = 0.459, *z* = -1.719, *p* = 0.086
- **2 to 5 vs 2 to 1**: *β* = -1.04, *SE* = 0.440, *z* = -2.368, *p* = 0.018
- **SNR**: *β* = -0.50, *SE* = 0.061, *z* = -8.202, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.40 | 0.44 | 0.90 | 0.367 | 0.886 | n.s. |
| 2 to 1 - 2 to 3 | 0.34 | 0.45 | 0.76 | 0.449 | 0.886 | n.s. |
| 2 to 1 - 2 to 4 | 0.79 | 0.46 | 1.72 | 0.086 | 0.529 | n.s. |
| 2 to 1 - 2 to 5 | 1.04 | 0.44 | 2.37 | 0.018 | 0.165 | n.s. |
| 2 to 2 - 2 to 3 | -0.06 | 0.41 | -0.14 | 0.890 | 0.890 | n.s. |
| 2 to 2 - 2 to 4 | 0.39 | 0.42 | 0.93 | 0.352 | 0.886 | n.s. |
| 2 to 2 - 2 to 5 | 0.64 | 0.40 | 1.62 | 0.106 | 0.543 | n.s. |
| 2 to 3 - 2 to 4 | 0.45 | 0.41 | 1.08 | 0.280 | 0.861 | n.s. |
| 2 to 3 - 2 to 5 | 0.70 | 0.40 | 1.75 | 0.080 | 0.529 | n.s. |
| 2 to 4 - 2 to 5 | 0.25 | 0.40 | 0.63 | 0.530 | 0.886 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.54, *p* = 0.050, η²_G = 0.106
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 1.68 | 13 | = 0.261 | 0.47 [-0.24, 0.85] | small | n.s. |
| 2 to 1 vs 2 to 3 | 2.08 | 13 | = 0.194 | 0.69 [-0.15, 1.01] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 2.23 | 13 | = 0.194 | 0.78 [0.00, 1.21] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 3.14 | 13 | = 0.079 | 0.89 [-0.02, 1.12] | large | n.s. |
| 2 to 2 vs 2 to 3 | 0.42 | 13 | = 0.751 | 0.15 [-0.28, 0.67] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | 1.05 | 13 | = 0.447 | 0.36 [-0.06, 0.92] | small | n.s. |
| 2 to 2 vs 2 to 5 | 1.61 | 13 | = 0.261 | 0.46 [0.06, 1.00] | small | n.s. |
| 2 to 3 vs 2 to 4 | 0.70 | 13 | = 0.618 | 0.27 [-0.19, 0.76] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.07 | 13 | = 0.447 | 0.40 [-0.08, 0.87] | small | n.s. |
| 2 to 4 vs 2 to 5 | 0.32 | 13 | = 0.751 | 0.10 [-0.40, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 741.49, BIC = 762.64
- **2 to 2 vs 2 to 1**: *β* = -5.43, *SE* = 2.232, *z* = -2.435, *p* = 0.015
- **2 to 3 vs 2 to 1**: *β* = -4.42, *SE* = 2.285, *z* = -1.935, *p* = 0.053
- **2 to 4 vs 2 to 1**: *β* = -4.46, *SE* = 2.325, *z* = -1.918, *p* = 0.055
- **2 to 5 vs 2 to 1**: *β* = -2.24, *SE* = 2.228, *z* = -1.005, *p* = 0.315
- **SNR**: *β* = -0.39, *SE* = 0.324, *z* = -1.187, *p* = 0.235

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 5.43 | 2.23 | 2.43 | 0.015 | 0.139 | n.s. |
| 2 to 1 - 2 to 3 | 4.42 | 2.28 | 1.93 | 0.053 | 0.388 | n.s. |
| 2 to 1 - 2 to 4 | 4.46 | 2.33 | 1.92 | 0.055 | 0.388 | n.s. |
| 2 to 1 - 2 to 5 | 2.24 | 2.23 | 1.00 | 0.315 | 0.854 | n.s. |
| 2 to 2 - 2 to 3 | -1.01 | 2.08 | -0.49 | 0.626 | 0.948 | n.s. |
| 2 to 2 - 2 to 4 | -0.97 | 2.12 | -0.46 | 0.646 | 0.948 | n.s. |
| 2 to 2 - 2 to 5 | -3.19 | 2.01 | -1.59 | 0.111 | 0.562 | n.s. |
| 2 to 3 - 2 to 4 | 0.04 | 2.08 | 0.02 | 0.984 | 0.984 | n.s. |
| 2 to 3 - 2 to 5 | -2.18 | 2.02 | -1.08 | 0.280 | 0.854 | n.s. |
| 2 to 4 - 2 to 5 | -2.22 | 2.03 | -1.09 | 0.274 | 0.854 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.32, *p* = 0.069, η²_G = 0.072
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 2.07 | 13 | = 0.196 | 0.64 [-0.07, 1.06] | medium | n.s. |
| 2 to 1 vs 2 to 3 | 3.24 | 13 | = 0.064 | 0.83 [0.11, 1.36] | large | n.s. |
| 2 to 1 vs 2 to 4 | 2.24 | 13 | = 0.196 | 0.73 [0.00, 1.21] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 1.70 | 13 | = 0.229 | 0.41 [-0.27, 0.81] | small | n.s. |
| 2 to 2 vs 2 to 3 | -0.12 | 13 | = 0.929 | -0.03 [-0.48, 0.45] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | -0.15 | 13 | = 0.929 | -0.05 [-0.54, 0.39] | negligible | n.s. |
| 2 to 2 vs 2 to 5 | -0.99 | 13 | = 0.483 | -0.29 [-0.73, 0.17] | small | n.s. |
| 2 to 3 vs 2 to 4 | -0.09 | 13 | = 0.929 | -0.02 [-0.46, 0.47] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | -1.58 | 13 | = 0.229 | -0.34 [-0.60, 0.31] | small | n.s. |
| 2 to 4 vs 2 to 5 | -1.62 | 13 | = 0.229 | -0.29 [-0.75, 0.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 246.83, BIC = 264.71
- **2 to 2 vs 2 to 1**: *β* = -0.15, *SE* = 0.503, *z* = -0.296, *p* = 0.767
- **2 to 3 vs 2 to 1**: *β* = -0.23, *SE* = 0.495, *z* = -0.470, *p* = 0.638
- **2 to 4 vs 2 to 1**: *β* = -0.47, *SE* = 0.467, *z* = -1.003, *p* = 0.316
- **2 to 5 vs 2 to 1**: *β* = -0.20, *SE* = 0.521, *z* = -0.381, *p* = 0.703
- **SNR**: *β* = 0.61, *SE* = 0.087, *z* = 7.081, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.15 | 0.50 | 0.30 | 0.767 | 0.999 | n.s. |
| 2 to 1 - 2 to 3 | 0.23 | 0.49 | 0.47 | 0.638 | 0.999 | n.s. |
| 2 to 1 - 2 to 4 | 0.47 | 0.47 | 1.00 | 0.316 | 0.978 | n.s. |
| 2 to 1 - 2 to 5 | 0.20 | 0.52 | 0.38 | 0.703 | 0.999 | n.s. |
| 2 to 2 - 2 to 3 | 0.08 | 0.51 | 0.16 | 0.869 | 0.999 | n.s. |
| 2 to 2 - 2 to 4 | 0.32 | 0.49 | 0.65 | 0.517 | 0.999 | n.s. |
| 2 to 2 - 2 to 5 | 0.05 | 0.52 | 0.10 | 0.924 | 0.999 | n.s. |
| 2 to 3 - 2 to 4 | 0.24 | 0.48 | 0.49 | 0.625 | 0.999 | n.s. |
| 2 to 3 - 2 to 5 | -0.03 | 0.51 | -0.07 | 0.947 | 0.999 | n.s. |
| 2 to 4 - 2 to 5 | -0.27 | 0.50 | -0.54 | 0.588 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.37, *p* = 0.003, η²_G = 0.570
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 3.06 | 3 | = 0.138 | 1.83 [0.11, 2.05] | large | n.s. |
| 2 to 1 vs 2 to 3 | 4.32 | 3 | = 0.076 | 3.89 [-0.09, 1.51] | large | n.s. |
| 2 to 1 vs 2 to 4 | 4.81 | 3 | = 0.076 | 1.87 [-0.04, 1.76] | large | n.s. |
| 2 to 1 vs 2 to 5 | 16.65 | 3 | = 0.005 | 4.48 [0.08, 1.80] | large | ** |
| 2 to 2 vs 2 to 3 | 0.56 | 3 | = 0.747 | 0.34 [-0.56, 0.99] | small | n.s. |
| 2 to 2 vs 2 to 4 | -0.06 | 3 | = 0.953 | -0.03 [-1.04, 0.65] | negligible | n.s. |
| 2 to 2 vs 2 to 5 | 1.82 | 3 | = 0.276 | 0.84 [-0.66, 0.88] | large | n.s. |
| 2 to 3 vs 2 to 4 | -0.47 | 3 | = 0.747 | -0.40 [-1.10, 0.76] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.23 | 3 | = 0.438 | 0.93 [-0.68, 0.86] | large | n.s. |
| 2 to 4 vs 2 to 5 | 2.00 | 3 | = 0.276 | 0.93 [-0.12, 1.63] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 483.06, BIC = 500.93
- **2 to 2 vs 2 to 1**: *β* = -2.61, *SE* = 2.863, *z* = -0.911, *p* = 0.362
- **2 to 3 vs 2 to 1**: *β* = -1.79, *SE* = 2.792, *z* = -0.642, *p* = 0.521
- **2 to 4 vs 2 to 1**: *β* = -2.40, *SE* = 2.596, *z* = -0.927, *p* = 0.354
- **2 to 5 vs 2 to 1**: *β* = -3.95, *SE* = 2.889, *z* = -1.368, *p* = 0.171
- **SNR**: *β* = -0.07, *SE* = 0.436, *z* = -0.169, *p* = 0.865

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 2.61 | 2.86 | 0.91 | 0.362 | 0.980 | n.s. |
| 2 to 1 - 2 to 3 | 1.79 | 2.79 | 0.64 | 0.521 | 0.988 | n.s. |
| 2 to 1 - 2 to 4 | 2.41 | 2.60 | 0.93 | 0.354 | 0.980 | n.s. |
| 2 to 1 - 2 to 5 | 3.95 | 2.89 | 1.37 | 0.171 | 0.847 | n.s. |
| 2 to 2 - 2 to 3 | -0.82 | 2.85 | -0.29 | 0.775 | 0.989 | n.s. |
| 2 to 2 - 2 to 4 | -0.20 | 2.81 | -0.07 | 0.943 | 0.989 | n.s. |
| 2 to 2 - 2 to 5 | 1.34 | 2.91 | 0.46 | 0.645 | 0.988 | n.s. |
| 2 to 3 - 2 to 4 | 0.61 | 2.75 | 0.22 | 0.823 | 0.989 | n.s. |
| 2 to 3 - 2 to 5 | 2.16 | 2.86 | 0.76 | 0.450 | 0.985 | n.s. |
| 2 to 4 - 2 to 5 | 1.55 | 2.81 | 0.55 | 0.582 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.43, *p* = 0.284, η²_G = 0.286
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | -1.18 | 3 | = 0.548 | -0.92 [-0.63, 0.92] | large | n.s. |
| 2 to 1 vs 2 to 3 | 1.87 | 3 | = 0.548 | 1.23 [0.17, 1.97] | large | n.s. |
| 2 to 1 vs 2 to 4 | -0.81 | 3 | = 0.683 | -0.53 [-0.65, 0.89] | medium | n.s. |
| 2 to 1 vs 2 to 5 | -0.30 | 3 | = 0.870 | -0.22 [-0.23, 1.30] | small | n.s. |
| 2 to 2 vs 2 to 3 | 1.63 | 3 | = 0.548 | 1.55 [-0.67, 0.87] | large | n.s. |
| 2 to 2 vs 2 to 4 | 0.11 | 3 | = 0.920 | 0.07 [-1.26, 0.47] | negligible | n.s. |
| 2 to 2 vs 2 to 5 | 1.40 | 3 | = 0.548 | 0.63 [-0.68, 0.86] | medium | n.s. |
| 2 to 3 vs 2 to 4 | -1.59 | 3 | = 0.548 | -1.12 [-1.11, 0.76] | large | n.s. |
| 2 to 3 vs 2 to 5 | -1.16 | 3 | = 0.548 | -1.14 [-0.96, 0.59] | large | n.s. |
| 2 to 4 vs 2 to 5 | 0.54 | 3 | = 0.787 | 0.39 [-0.27, 1.38] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 374.15, BIC = 394.41
- **2 to 2 vs 2 to 1**: *β* = -0.65, *SE* = 0.528, *z* = -1.236, *p* = 0.216
- **2 to 3 vs 2 to 1**: *β* = -0.25, *SE* = 0.473, *z* = -0.527, *p* = 0.599
- **2 to 4 vs 2 to 1**: *β* = 0.11, *SE* = 0.465, *z* = 0.239, *p* = 0.811
- **2 to 5 vs 2 to 1**: *β* = -0.19, *SE* = 0.439, *z* = -0.437, *p* = 0.662
- **SNR**: *β* = 0.61, *SE* = 0.056, *z* = 11.019, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.65 | 0.53 | 1.24 | 0.216 | 0.888 | n.s. |
| 2 to 1 - 2 to 3 | 0.25 | 0.47 | 0.53 | 0.599 | 0.984 | n.s. |
| 2 to 1 - 2 to 4 | -0.11 | 0.46 | -0.24 | 0.811 | 0.984 | n.s. |
| 2 to 1 - 2 to 5 | 0.19 | 0.44 | 0.44 | 0.662 | 0.984 | n.s. |
| 2 to 2 - 2 to 3 | -0.40 | 0.55 | -0.73 | 0.463 | 0.984 | n.s. |
| 2 to 2 - 2 to 4 | -0.76 | 0.55 | -1.39 | 0.164 | 0.834 | n.s. |
| 2 to 2 - 2 to 5 | -0.46 | 0.52 | -0.89 | 0.373 | 0.976 | n.s. |
| 2 to 3 - 2 to 4 | -0.36 | 0.47 | -0.76 | 0.446 | 0.984 | n.s. |
| 2 to 3 - 2 to 5 | -0.06 | 0.46 | -0.12 | 0.902 | 0.984 | n.s. |
| 2 to 4 - 2 to 5 | 0.30 | 0.45 | 0.67 | 0.505 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.20, *p* = 0.022, η²_G = 0.151
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 3.27 | 11 | = 0.061 | 1.08 [0.08, 1.45] | large | n.s. |
| 2 to 1 vs 2 to 3 | -0.01 | 11 | = 0.994 | -0.00 [-0.54, 0.52] | negligible | n.s. |
| 2 to 1 vs 2 to 4 | -0.52 | 11 | = 0.684 | -0.20 [-0.70, 0.30] | small | n.s. |
| 2 to 1 vs 2 to 5 | 1.43 | 11 | = 0.362 | 0.37 [-0.39, 0.55] | small | n.s. |
| 2 to 2 vs 2 to 3 | -2.77 | 11 | = 0.061 | -1.15 [-1.53, -0.07] | large | n.s. |
| 2 to 2 vs 2 to 4 | -2.84 | 11 | = 0.061 | -1.02 [-1.36, -0.02] | large | n.s. |
| 2 to 2 vs 2 to 5 | -2.44 | 11 | = 0.082 | -0.85 [-1.29, 0.04] | large | n.s. |
| 2 to 3 vs 2 to 4 | -0.67 | 11 | = 0.646 | -0.21 [-0.75, 0.30] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.07 | 11 | = 0.442 | 0.40 [-0.37, 0.66] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.28 | 11 | = 0.377 | 0.50 [-0.22, 0.76] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 866.03, BIC = 886.29
- **2 to 2 vs 2 to 1**: *β* = -17.20, *SE* = 8.493, *z* = -2.025, *p* = 0.043
- **2 to 3 vs 2 to 1**: *β* = -16.38, *SE* = 7.795, *z* = -2.101, *p* = 0.036
- **2 to 4 vs 2 to 1**: *β* = -3.96, *SE* = 7.621, *z* = -0.520, *p* = 0.603
- **2 to 5 vs 2 to 1**: *β* = -18.63, *SE* = 7.165, *z* = -2.600, *p* = 0.009
- **SNR**: *β* = -0.39, *SE* = 0.809, *z* = -0.482, *p* = 0.630

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 17.20 | 8.49 | 2.03 | 0.043 | 0.296 | n.s. |
| 2 to 1 - 2 to 3 | 16.38 | 7.79 | 2.10 | 0.036 | 0.279 | n.s. |
| 2 to 1 - 2 to 4 | 3.96 | 7.62 | 0.52 | 0.603 | 0.975 | n.s. |
| 2 to 1 - 2 to 5 | 18.63 | 7.16 | 2.60 | 0.009 | 0.089 | n.s. |
| 2 to 2 - 2 to 3 | -0.82 | 8.76 | -0.09 | 0.925 | 0.987 | n.s. |
| 2 to 2 - 2 to 4 | -13.24 | 8.73 | -1.52 | 0.129 | 0.500 | n.s. |
| 2 to 2 - 2 to 5 | 1.43 | 8.17 | 0.17 | 0.861 | 0.987 | n.s. |
| 2 to 3 - 2 to 4 | -12.42 | 7.70 | -1.61 | 0.107 | 0.493 | n.s. |
| 2 to 3 - 2 to 5 | 2.25 | 7.50 | 0.30 | 0.764 | 0.987 | n.s. |
| 2 to 4 - 2 to 5 | 14.67 | 7.38 | 1.99 | 0.047 | 0.296 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.243, η²_G = 0.098
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 1.22 | 11 | = 0.518 | 0.61 [-0.26, 0.99] | medium | n.s. |
| 2 to 1 vs 2 to 3 | 2.36 | 11 | = 0.189 | 0.88 [-0.12, 1.00] | large | n.s. |
| 2 to 1 vs 2 to 4 | 0.66 | 11 | = 0.745 | 0.18 [-0.57, 0.43] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | 2.43 | 11 | = 0.189 | 0.99 [0.15, 1.19] | large | n.s. |
| 2 to 2 vs 2 to 3 | 0.14 | 11 | = 0.887 | 0.06 [-0.59, 0.68] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | -0.85 | 11 | = 0.693 | -0.38 [-0.94, 0.30] | small | n.s. |
| 2 to 2 vs 2 to 5 | 0.34 | 11 | = 0.822 | 0.15 [-0.51, 0.70] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -1.19 | 11 | = 0.518 | -0.52 [-0.77, 0.27] | medium | n.s. |
| 2 to 3 vs 2 to 5 | 0.35 | 11 | = 0.822 | 0.10 [-0.28, 0.76] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.35 | 11 | = 0.518 | 0.61 [-0.04, 0.98] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.050)
**N1 latency:** Marginal trend toward condition differences (*p* = 0.069)
**P1 amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 4.48)
**P3b amplitude:** Significant main effect of condition (*p* = 0.022) (no significant pairwise comparisons)

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
