# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:29:06

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
| Ratio 0.5 (1:2, no 1) | 23 | -4.28 µV | 1.75 | 0.37 | [-7.59, -1.22] |
| Ratio 0.67 (2:3, no 1) | 23 | -3.60 µV | 1.60 | 0.33 | [-7.82, -1.05] |
| Ratio 0.75 (3:4, no 1) | 23 | -3.59 µV | 1.76 | 0.37 | [-7.79, -0.05] |
| Ratio 0.8 (4:5, no 1) | 23 | -3.84 µV | 1.92 | 0.40 | [-7.66, -0.61] |
| Ratio 0.83 (5:6, no 1) | 24 | -3.80 µV | 1.92 | 0.39 | [-8.67, -0.14] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 23 | 172.86 ms | 7.20 | 1.50 | [160.16, 189.59] |
| Ratio 0.67 (2:3, no 1) | 23 | 171.68 ms | 7.08 | 1.48 | [154.47, 186.07] |
| Ratio 0.75 (3:4, no 1) | 23 | 170.04 ms | 8.93 | 1.86 | [149.08, 191.26] |
| Ratio 0.8 (4:5, no 1) | 23 | 172.86 ms | 8.00 | 1.67 | [158.51, 187.17] |
| Ratio 0.83 (5:6, no 1) | 24 | 173.00 ms | 10.22 | 2.09 | [152.27, 202.76] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 13 | 1.41 µV | 1.18 | 0.33 | [0.20, 4.62] |
| Ratio 0.67 (2:3, no 1) | 13 | 1.34 µV | 1.21 | 0.34 | [0.01, 3.62] |
| Ratio 0.75 (3:4, no 1) | 14 | 1.39 µV | 1.39 | 0.37 | [0.08, 4.96] |
| Ratio 0.8 (4:5, no 1) | 12 | 1.90 µV | 1.52 | 0.44 | [0.24, 4.99] |
| Ratio 0.83 (5:6, no 1) | 13 | 1.36 µV | 1.21 | 0.34 | [-0.00, 3.19] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 13 | 103.80 ms | 2.84 | 0.79 | [99.73, 108.22] |
| Ratio 0.67 (2:3, no 1) | 13 | 103.44 ms | 4.20 | 1.17 | [92.45, 109.17] |
| Ratio 0.75 (3:4, no 1) | 14 | 102.23 ms | 4.41 | 1.18 | [94.63, 109.62] |
| Ratio 0.8 (4:5, no 1) | 12 | 101.04 ms | 3.99 | 1.15 | [94.84, 104.96] |
| Ratio 0.83 (5:6, no 1) | 13 | 102.14 ms | 4.55 | 1.26 | [92.35, 108.21] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 3.30 µV | 2.37 | 0.53 | [0.04, 8.40] |
| Ratio 0.67 (2:3, no 1) | 18 | 3.62 µV | 2.41 | 0.57 | [0.42, 8.68] |
| Ratio 0.75 (3:4, no 1) | 18 | 3.69 µV | 2.47 | 0.58 | [0.44, 7.68] |
| Ratio 0.8 (4:5, no 1) | 16 | 3.76 µV | 2.71 | 0.68 | [0.24, 9.94] |
| Ratio 0.83 (5:6, no 1) | 12 | 2.10 µV | 2.29 | 0.66 | [0.07, 6.99] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 487.49 ms | 14.37 | 3.21 | [467.87, 520.91] |
| Ratio 0.67 (2:3, no 1) | 18 | 485.36 ms | 12.75 | 3.00 | [460.37, 506.50] |
| Ratio 0.75 (3:4, no 1) | 18 | 485.55 ms | 12.38 | 2.92 | [457.66, 500.92] |
| Ratio 0.8 (4:5, no 1) | 16 | 488.86 ms | 15.98 | 3.99 | [449.39, 514.14] |
| Ratio 0.83 (5:6, no 1) | 12 | 494.63 ms | 26.02 | 7.51 | [441.04, 531.50] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 357.20, BIC = 379.23
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.47, *SE* = 0.248, *z* = 1.905, *p* = 0.057
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.10, *SE* = 0.260, *z* = 0.371, *p* = 0.711
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.05, *SE* = 0.255, *z* = -0.192, *p* = 0.848
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.14, *SE* = 0.255, *z* = -0.555, *p* = 0.579
- **SNR**: *β* = -0.16, *SE* = 0.022, *z* = -7.137, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.47 | 0.25 | -1.90 | 0.057 | 0.374 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.10 | 0.26 | -0.37 | 0.711 | 0.983 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.05 | 0.26 | 0.19 | 0.848 | 0.983 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.14 | 0.25 | 0.56 | 0.579 | 0.983 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.38 | 0.25 | 1.49 | 0.136 | 0.640 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.52 | 0.25 | 2.09 | 0.036 | 0.284 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.61 | 0.25 | 2.47 | 0.014 | 0.128 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.15 | 0.25 | 0.59 | 0.555 | 0.983 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.24 | 0.25 | 0.97 | 0.332 | 0.911 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.09 | 0.24 | 0.38 | 0.706 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.88, *p* = 0.121, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -3.48 | 22 | = 0.021 | -0.41 [-1.21, -0.24] | small | * |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -2.25 | 22 | = 0.172 | -0.40 [-0.93, -0.01] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.59 | 22 | = 0.417 | -0.24 [-0.78, 0.11] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.17 | 22 | = 0.436 | -0.19 [-0.68, 0.19] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.03 | 22 | = 0.978 | -0.00 [-0.44, 0.43] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.75 | 22 | = 0.586 | 0.14 [-0.28, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.18 | 22 | = 0.436 | 0.21 [-0.19, 0.68] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.74 | 22 | = 0.586 | 0.14 [-0.28, 0.59] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 1.15 | 22 | = 0.436 | 0.21 [-0.20, 0.68] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.37 | 22 | = 0.794 | 0.06 [-0.36, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 730.95, BIC = 752.98
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.10, *SE* = 1.120, *z* = -0.979, *p* = 0.328
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -2.58, *SE* = 1.173, *z* = -2.198, *p* = 0.028
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.21, *SE* = 1.154, *z* = 0.180, *p* = 0.857
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.74, *SE* = 1.156, *z* = -0.640, *p* = 0.522
- **SNR**: *β* = 0.07, *SE* = 0.100, *z* = 0.659, *p* = 0.510

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 1.10 | 1.12 | 0.98 | 0.328 | 0.863 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 2.58 | 1.17 | 2.20 | 0.028 | 0.225 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.21 | 1.15 | -0.18 | 0.857 | 0.938 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.74 | 1.16 | 0.64 | 0.522 | 0.891 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 1.48 | 1.14 | 1.30 | 0.192 | 0.776 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -1.30 | 1.13 | -1.16 | 0.247 | 0.817 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -0.36 | 1.13 | -0.32 | 0.752 | 0.938 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -2.79 | 1.11 | -2.50 | 0.012 | 0.117 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -1.84 | 1.11 | -1.65 | 0.099 | 0.564 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.95 | 1.11 | 0.85 | 0.394 | 0.865 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.09, *p* = 0.088, η²_G = 0.018
- Greenhouse-Geisser corrected: *p* = 0.122 (ε = 0.618)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 1.82 | 22 | = 0.272 | 0.17 [-0.07, 0.83] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 2.57 | 22 | = 0.174 | 0.35 [0.07, 1.00] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.00 | 22 | = 0.996 | -0.00 [-0.43, 0.43] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 1.01 | 22 | = 0.464 | 0.15 [-0.23, 0.65] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 1.58 | 22 | = 0.323 | 0.20 [-0.12, 0.77] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.06 | 22 | = 0.464 | -0.16 [-0.66, 0.22] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.03 | 22 | = 0.996 | -0.00 [-0.44, 0.43] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -1.85 | 22 | = 0.272 | -0.33 [-0.83, 0.06] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.34 | 22 | = 0.390 | -0.19 [-0.72, 0.16] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.77 | 22 | = 0.564 | 0.14 [-0.28, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 159.77, BIC = 177.17
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.01, *SE* = 0.240, *z* = -0.024, *p* = 0.981
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.29, *SE* = 0.241, *z* = 1.187, *p* = 0.235
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.78, *SE* = 0.248, *z* = 3.135, *p* = 0.002
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.44, *SE* = 0.252, *z* = 1.747, *p* = 0.081
- **SNR**: *β* = 0.32, *SE* = 0.050, *z* = 6.397, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.01 | 0.24 | 0.02 | 0.981 | 0.981 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.29 | 0.24 | -1.19 | 0.235 | 0.652 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.78 | 0.25 | -3.14 | 0.002 | 0.017 | * |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -0.44 | 0.25 | -1.75 | 0.081 | 0.424 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.29 | 0.24 | -1.19 | 0.232 | 0.652 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.78 | 0.25 | -3.12 | 0.002 | 0.017 | * |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -0.45 | 0.25 | -1.78 | 0.076 | 0.424 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.49 | 0.25 | -1.98 | 0.048 | 0.323 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -0.15 | 0.24 | -0.63 | 0.531 | 0.780 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.34 | 0.25 | 1.36 | 0.175 | 0.617 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.47, *p* = 0.758, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.46 | 4 | = 0.843 | -0.10 [-0.64, 0.79] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.21 | 4 | = 0.843 | -0.24 [-1.13, 0.45] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.85 | 4 | = 0.843 | -0.32 [-1.14, 0.35] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.02 | 4 | = 0.988 | -0.01 [-1.03, 0.66] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.58 | 4 | = 0.843 | -0.16 [-1.09, 0.61] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.54 | 4 | = 0.843 | -0.24 [-1.12, 0.46] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 0.45 | 4 | = 0.843 | 0.12 [-0.41, 1.36] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.17 | 4 | = 0.974 | -0.06 [-0.97, 0.71] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.85 | 4 | = 0.843 | 0.28 [-0.75, 0.93] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 1.12 | 4 | = 0.843 | 0.38 [-0.62, 1.07] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 356.33, BIC = 373.72
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.00, *SE* = 1.013, *z* = -0.989, *p* = 0.323
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.80, *SE* = 1.029, *z* = -0.776, *p* = 0.438
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.65, *SE* = 1.053, *z* = -1.563, *p* = 0.118
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.23, *SE* = 1.067, *z* = -1.155, *p* = 0.248
- **SNR**: *β* = 0.12, *SE* = 0.196, *z* = 0.638, *p* = 0.524

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 1.00 | 1.01 | 0.99 | 0.323 | 0.956 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.80 | 1.03 | 0.78 | 0.438 | 0.978 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 1.65 | 1.05 | 1.56 | 0.118 | 0.715 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 1.23 | 1.07 | 1.15 | 0.248 | 0.923 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.20 | 1.06 | -0.19 | 0.847 | 0.989 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.64 | 1.08 | 0.59 | 0.552 | 0.982 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.23 | 1.07 | 0.21 | 0.830 | 0.989 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.85 | 1.05 | 0.81 | 0.419 | 0.978 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.43 | 1.04 | 0.42 | 0.676 | 0.989 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -0.41 | 1.06 | -0.39 | 0.695 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.96, *p* = 0.454, η²_G = 0.128
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -1.00 | 4 | = 0.559 | -0.11 [-0.45, 1.01] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 1.02 | 4 | = 0.559 | 0.68 [-0.63, 0.92] | medium | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.49 | 4 | = 0.652 | 0.26 [-0.18, 1.37] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 1.32 | 4 | = 0.559 | 0.50 [-0.16, 1.76] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 1.10 | 4 | = 0.559 | 0.77 [-0.87, 0.80] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.78 | 4 | = 0.597 | 0.40 [-0.57, 0.98] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.62 | 4 | = 0.559 | 0.63 [-0.61, 1.08] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.96 | 4 | = 0.559 | -0.62 [-0.62, 1.07] | medium | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.52 | 4 | = 0.652 | -0.35 [-0.99, 0.69] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 1.45 | 4 | = 0.559 | 0.42 [-0.55, 1.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 322.36, BIC = 341.81
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.30, *SE* = 0.391, *z* = 0.759, *p* = 0.448
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.47, *SE* = 0.397, *z* = 1.193, *p* = 0.233
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.74, *SE* = 0.418, *z* = 1.758, *p* = 0.079
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.55, *SE* = 0.509, *z* = -1.072, *p* = 0.284
- **SNR**: *β* = 0.26, *SE* = 0.037, *z* = 6.871, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.30 | 0.39 | -0.76 | 0.448 | 0.832 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.47 | 0.40 | -1.19 | 0.233 | 0.796 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.74 | 0.42 | -1.76 | 0.079 | 0.481 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.55 | 0.51 | 1.07 | 0.284 | 0.812 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.18 | 0.41 | -0.44 | 0.662 | 0.832 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.44 | 0.42 | -1.04 | 0.300 | 0.812 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.84 | 0.50 | 1.68 | 0.094 | 0.498 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.26 | 0.42 | -0.62 | 0.537 | 0.832 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 1.02 | 0.49 | 2.09 | 0.037 | 0.285 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 1.28 | 0.49 | 2.62 | 0.009 | 0.085 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.22, *p* = 0.023, η²_G = 0.148
- Greenhouse-Geisser corrected: *p* = 0.077 (ε = 0.406)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.62 | 9 | = 0.977 | 0.06 [-0.51, 0.48] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.51 | 9 | = 0.977 | 0.12 [-0.55, 0.48] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.14 | 9 | = 0.977 | 0.05 [-0.52, 0.55] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 2.45 | 9 | = 0.144 | 1.08 [0.04, 1.59] | large | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.27 | 9 | = 0.977 | 0.07 [-0.54, 0.53] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.03 | 9 | = 0.977 | -0.01 [-0.49, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 2.35 | 9 | = 0.144 | 1.01 [0.03, 1.58] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.20 | 9 | = 0.977 | -0.07 [-0.52, 0.64] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 1.69 | 9 | = 0.315 | 0.86 [-0.09, 1.29] | large | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 4.16 | 9 | = 0.025 | 0.98 [0.34, 2.29] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 700.69, BIC = 720.14
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.24, *SE* = 3.920, *z* = -0.315, *p* = 0.753
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.67, *SE* = 3.966, *z* = -0.421, *p* = 0.674
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 2.76, *SE* = 4.157, *z* = 0.665, *p* = 0.506
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 6.59, *SE* = 4.943, *z* = 1.334, *p* = 0.182
- **SNR**: *β* = -0.35, *SE* = 0.356, *z* = -0.992, *p* = 0.321

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 1.24 | 3.92 | 0.32 | 0.753 | 0.965 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 1.67 | 3.97 | 0.42 | 0.674 | 0.965 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -2.76 | 4.16 | -0.66 | 0.506 | 0.941 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -6.60 | 4.94 | -1.33 | 0.182 | 0.800 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.43 | 4.06 | 0.11 | 0.915 | 0.965 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -4.00 | 4.22 | -0.95 | 0.343 | 0.920 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -7.83 | 4.93 | -1.59 | 0.112 | 0.657 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -4.43 | 4.23 | -1.05 | 0.294 | 0.913 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -8.26 | 4.81 | -1.72 | 0.086 | 0.591 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -3.83 | 4.85 | -0.79 | 0.430 | 0.940 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.45, *p* = 0.005, η²_G = 0.173
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.08 | 9 | = 0.972 | -0.02 [-0.52, 0.47] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.07 | 9 | = 0.972 | -0.03 [-0.39, 0.64] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -2.67 | 9 | = 0.072 | -1.06 [-0.94, 0.17] | large | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -2.09 | 9 | = 0.111 | -0.87 [-1.52, 0.00] | large | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.04 | 9 | = 0.972 | -0.01 [-0.45, 0.61] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -2.60 | 9 | = 0.072 | -0.92 [-0.80, 0.33] | large | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -2.37 | 9 | = 0.083 | -0.81 [-1.63, -0.06] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -3.18 | 9 | = 0.072 | -0.86 [-1.30, -0.03] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -2.87 | 9 | = 0.072 | -0.78 [-1.01, 0.30] | medium | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.73 | 9 | = 0.694 | -0.17 [-0.95, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Marginal trend toward condition differences (*p* = 0.088)
**P3b amplitude:** Significant main effect of condition (*p* = 0.023). Post-hoc tests revealed:
  - Ratio 0.8 (4:5, no 1) showed greater amplitude than Ratio 0.83 (5:6, no 1) (*d* = 0.98)
**P3b latency:** Significant main effect of condition (*p* = 0.005) (no significant pairwise comparisons)

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
