# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:50:04

---

## 1. Analysis Overview

**Total Measurements:** 480
**Number of Subjects:** 24
**Number of Conditions:** 5

**Components Analyzed:** Fz, N1, P1, P3b
**Dependent Variables:** Latency (Peak), Amplitude (Peak)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** Peak latency within FWHM window
- **Amplitude Measure:** Peak amplitude within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 Fz Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 10 | 101.20 ms | 9.62 | 3.04 | [92.00, 112.00] |
| Ratio 0.67 (2:3, no 1) | 8 | 104.50 ms | 8.93 | 3.16 | [92.00, 112.00] |
| Ratio 0.75 (3:4, no 1) | 11 | 101.09 ms | 9.48 | 2.86 | [92.00, 112.00] |
| Ratio 0.8 (4:5, no 1) | 9 | 101.33 ms | 10.20 | 3.40 | [92.00, 112.00] |
| Ratio 0.83 (5:6, no 1) | 11 | 104.73 ms | 10.09 | 3.04 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 10 | 1.54 µV | 0.83 | 0.26 | [0.42, 2.82] |
| Ratio 0.67 (2:3, no 1) | 8 | 1.59 µV | 0.69 | 0.24 | [0.50, 2.79] |
| Ratio 0.75 (3:4, no 1) | 11 | 1.43 µV | 1.17 | 0.35 | [0.66, 4.63] |
| Ratio 0.8 (4:5, no 1) | 9 | 2.03 µV | 1.34 | 0.45 | [0.65, 4.26] |
| Ratio 0.83 (5:6, no 1) | 11 | 1.48 µV | 1.07 | 0.32 | [0.39, 4.30] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 23 | 171.13 ms | 14.06 | 2.93 | [140.00, 196.00] |
| Ratio 0.67 (2:3, no 1) | 23 | 173.04 ms | 19.53 | 4.07 | [140.00, 204.00] |
| Ratio 0.75 (3:4, no 1) | 23 | 170.78 ms | 17.95 | 3.74 | [140.00, 204.00] |
| Ratio 0.8 (4:5, no 1) | 23 | 170.26 ms | 21.02 | 4.38 | [140.00, 204.00] |
| Ratio 0.83 (5:6, no 1) | 24 | 175.50 ms | 18.06 | 3.69 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 23 | -5.97 µV | 2.15 | 0.45 | [-10.62, -2.62] |
| Ratio 0.67 (2:3, no 1) | 23 | -5.13 µV | 2.19 | 0.46 | [-9.87, -1.99] |
| Ratio 0.75 (3:4, no 1) | 23 | -5.41 µV | 2.20 | 0.46 | [-10.31, -0.44] |
| Ratio 0.8 (4:5, no 1) | 23 | -5.57 µV | 2.47 | 0.52 | [-10.71, -1.29] |
| Ratio 0.83 (5:6, no 1) | 24 | -5.52 µV | 1.99 | 0.41 | [-9.96, -2.06] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 13 | 105.85 ms | 6.24 | 1.73 | [96.00, 112.00] |
| Ratio 0.67 (2:3, no 1) | 13 | 106.15 ms | 6.66 | 1.85 | [92.00, 112.00] |
| Ratio 0.75 (3:4, no 1) | 14 | 104.29 ms | 7.76 | 2.07 | [92.00, 112.00] |
| Ratio 0.8 (4:5, no 1) | 12 | 103.00 ms | 8.88 | 2.56 | [92.00, 112.00] |
| Ratio 0.83 (5:6, no 1) | 13 | 103.08 ms | 7.51 | 2.08 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 13 | 2.03 µV | 1.30 | 0.36 | [0.48, 5.22] |
| Ratio 0.67 (2:3, no 1) | 13 | 1.99 µV | 1.52 | 0.42 | [0.34, 4.44] |
| Ratio 0.75 (3:4, no 1) | 14 | 2.19 µV | 1.62 | 0.43 | [0.33, 5.67] |
| Ratio 0.8 (4:5, no 1) | 12 | 2.98 µV | 1.69 | 0.49 | [0.82, 5.75] |
| Ratio 0.83 (5:6, no 1) | 13 | 2.00 µV | 1.39 | 0.38 | [0.37, 4.00] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 484.40 ms | 33.11 | 7.40 | [436.00, 540.00] |
| Ratio 0.67 (2:3, no 1) | 18 | 491.11 ms | 35.55 | 8.38 | [436.00, 540.00] |
| Ratio 0.75 (3:4, no 1) | 18 | 491.11 ms | 34.59 | 8.15 | [436.00, 540.00] |
| Ratio 0.8 (4:5, no 1) | 16 | 500.25 ms | 28.79 | 7.20 | [452.00, 540.00] |
| Ratio 0.83 (5:6, no 1) | 12 | 490.33 ms | 42.45 | 12.25 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 20 | 4.51 µV | 2.69 | 0.60 | [0.56, 9.62] |
| Ratio 0.67 (2:3, no 1) | 18 | 5.06 µV | 3.12 | 0.73 | [1.19, 12.42] |
| Ratio 0.75 (3:4, no 1) | 18 | 5.30 µV | 2.95 | 0.69 | [1.66, 11.73] |
| Ratio 0.8 (4:5, no 1) | 16 | 5.39 µV | 3.04 | 0.76 | [1.32, 11.33] |
| Ratio 0.83 (5:6, no 1) | 12 | 3.56 µV | 2.55 | 0.74 | [1.14, 9.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 361.04, BIC = 376.17
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.57, *SE* = 3.178, *z* = 0.179, *p* = 0.858
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.91, *SE* = 3.141, *z* = -0.289, *p* = 0.772
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.41, *SE* = 3.173, *z* = -0.445, *p* = 0.656
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.60, *SE* = 3.307, *z* = 0.485, *p* = 0.627
- **SNR**: *β* = 1.30, *SE* = 1.409, *z* = 0.925, *p* = 0.355

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.57 | 3.18 | -0.18 | 0.858 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.91 | 3.14 | 0.29 | 0.772 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 1.41 | 3.17 | 0.45 | 0.656 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -1.60 | 3.31 | -0.49 | 0.627 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 1.48 | 3.25 | 0.46 | 0.649 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 1.98 | 3.38 | 0.59 | 0.557 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -1.04 | 3.43 | -0.30 | 0.763 | 0.999 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.50 | 3.21 | 0.16 | 0.875 | 0.999 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -2.51 | 3.20 | -0.78 | 0.433 | 0.994 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -3.02 | 3.48 | -0.87 | 0.385 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.500, η²_G = 0.186
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -1.00 | 1 | = 0.500 | -0.34 [-1.05, 1.05] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | nan | 1 | n/a | 0.00 [-0.86, 1.75] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | nan | 1 | n/a | 0.00 [-1.07, 1.43] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.00 | 1 | = 0.500 | -1.00 [-1.61, 0.94] | large | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 1.00 | 1 | = 0.500 | 0.34 [-0.68, 2.10] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 1.00 | 1 | = 0.500 | 0.34 [-1.41, 1.81] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -1.00 | 1 | = 0.500 | -1.00 [-2.19, 1.19] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | nan | 1 | n/a | 0.00 [-0.80, 1.33] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -1.00 | 1 | = 0.500 | -1.00 [-2.48, 2.48] | large | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -1.00 | 1 | = 0.500 | -1.00 [-1.24, 1.24] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 122.55, BIC = 137.68
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.08, *SE* = 0.311, *z* = -0.261, *p* = 0.794
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.32, *SE* = 0.299, *z* = 1.061, *p* = 0.289
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.32, *SE* = 0.308, *z* = 1.048, *p* = 0.294
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.57, *SE* = 0.308, *z* = 1.849, *p* = 0.064
- **SNR**: *β* = 0.73, *SE* = 0.133, *z* = 5.464, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.08 | 0.31 | 0.26 | 0.794 | 0.957 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.32 | 0.30 | -1.06 | 0.289 | 0.870 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.32 | 0.31 | -1.05 | 0.294 | 0.870 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -0.57 | 0.31 | -1.85 | 0.064 | 0.451 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.40 | 0.32 | -1.25 | 0.211 | 0.849 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.40 | 0.33 | -1.21 | 0.226 | 0.849 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -0.65 | 0.33 | -1.98 | 0.048 | 0.390 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.01 | 0.31 | -0.02 | 0.985 | 0.985 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -0.25 | 0.30 | -0.85 | 0.393 | 0.870 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -0.25 | 0.33 | -0.75 | 0.451 | 0.870 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.916, η²_G = 0.127
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 13.29 | 1 | = 0.478 | 1.90 [-0.02, 3.06] | large | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.76 | 1 | = 0.960 | 1.04 [-1.32, 1.17] | large | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.52 | 1 | = 0.960 | 0.27 [-2.14, 0.66] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.00 | 1 | = 0.998 | -0.00 [-1.29, 1.19] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.22 | 1 | = 0.960 | -0.29 [-1.42, 1.08] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.18 | 1 | = 0.960 | -0.72 [-3.66, 0.84] | medium | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.58 | 1 | = 0.960 | -0.48 [-1.83, 1.39] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.32 | 1 | = 0.960 | -0.45 [-1.09, 1.01] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.29 | 1 | = 0.960 | -0.37 [-2.75, 2.29] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.25 | 1 | = 0.960 | -0.13 [-0.96, 1.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 971.54, BIC = 993.57
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.78, *SE* = 3.648, *z* = 0.489, *p* = 0.625
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.70, *SE* = 3.811, *z* = -0.185, *p* = 0.854
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.16, *SE* = 3.752, *z* = -0.310, *p* = 0.757
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 3.40, *SE* = 3.750, *z* = 0.906, *p* = 0.365
- **SNR**: *β* = -0.10, *SE* = 0.316, *z* = -0.301, *p* = 0.763

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -1.78 | 3.65 | -0.49 | 0.625 | 0.993 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.70 | 3.81 | 0.18 | 0.854 | 0.993 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 1.16 | 3.75 | 0.31 | 0.757 | 0.993 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -3.40 | 3.75 | -0.91 | 0.365 | 0.974 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 2.49 | 3.70 | 0.67 | 0.501 | 0.985 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 2.95 | 3.67 | 0.80 | 0.421 | 0.978 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -1.61 | 3.66 | -0.44 | 0.659 | 0.993 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.46 | 3.63 | 0.13 | 0.899 | 0.993 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -4.10 | 3.61 | -1.14 | 0.256 | 0.930 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -4.56 | 3.61 | -1.26 | 0.206 | 0.901 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.794, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.718 (ε = 0.673)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.59 | 22 | = 0.914 | -0.11 [-0.56, 0.31] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.09 | 22 | = 0.928 | 0.02 [-0.41, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.38 | 22 | = 0.914 | 0.05 [-0.35, 0.51] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.78 | 22 | = 0.914 | -0.20 [-0.60, 0.27] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.77 | 22 | = 0.914 | 0.12 [-0.27, 0.60] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.75 | 22 | = 0.914 | 0.14 [-0.28, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.35 | 22 | = 0.914 | -0.07 [-0.51, 0.36] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.13 | 22 | = 0.928 | 0.03 [-0.41, 0.46] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.97 | 22 | = 0.914 | -0.20 [-0.64, 0.24] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.81 | 22 | = 0.914 | -0.21 [-0.60, 0.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 397.57, BIC = 419.60
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.61, *SE* = 0.287, *z* = 2.124, *p* = 0.034
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.08, *SE* = 0.300, *z* = -0.257, *p* = 0.797
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.12, *SE* = 0.295, *z* = -0.420, *p* = 0.674
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.16, *SE* = 0.296, *z* = -0.530, *p* = 0.596
- **SNR**: *β* = -0.17, *SE* = 0.026, *z* = -6.720, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.61 | 0.29 | -2.12 | 0.034 | 0.213 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.08 | 0.30 | 0.26 | 0.797 | 0.998 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.12 | 0.30 | 0.42 | 0.674 | 0.996 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.16 | 0.30 | 0.53 | 0.596 | 0.996 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.69 | 0.29 | 2.36 | 0.018 | 0.138 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.73 | 0.29 | 2.54 | 0.011 | 0.094 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.77 | 0.29 | 2.66 | 0.008 | 0.076 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.05 | 0.29 | 0.16 | 0.869 | 0.998 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.08 | 0.28 | 0.28 | 0.779 | 0.998 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.03 | 0.28 | 0.11 | 0.909 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.58, *p* = 0.187, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -4.04 | 22 | = 0.006 | -0.39 [-1.34, -0.34] | small | ** |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.49 | 22 | = 0.502 | -0.26 [-0.75, 0.13] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.06 | 22 | = 0.502 | -0.17 [-0.66, 0.22] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.32 | 22 | = 0.502 | -0.18 [-0.72, 0.17] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.72 | 22 | = 0.685 | 0.13 [-0.28, 0.58] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 1.12 | 22 | = 0.502 | 0.19 [-0.20, 0.67] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.42 | 22 | = 0.502 | 0.22 [-0.15, 0.74] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.50 | 22 | = 0.693 | 0.07 [-0.33, 0.54] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.51 | 22 | = 0.693 | 0.09 [-0.33, 0.54] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.06 | 22 | = 0.955 | 0.01 [-0.42, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 419.19, BIC = 436.59
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.29, *SE* = 1.518, *z* = -0.851, *p* = 0.394
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.44, *SE* = 1.542, *z* = -0.285, *p* = 0.776
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.35, *SE* = 1.578, *z* = -0.221, *p* = 0.825
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.28, *SE* = 1.608, *z* = -0.795, *p* = 0.427
- **SNR**: *β* = 0.36, *SE* = 0.300, *z* = 1.212, *p* = 0.226

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 1.29 | 1.52 | 0.85 | 0.394 | 0.993 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.44 | 1.54 | 0.29 | 0.776 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.35 | 1.58 | 0.22 | 0.825 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 1.28 | 1.61 | 0.80 | 0.427 | 0.993 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.85 | 1.58 | -0.54 | 0.590 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.94 | 1.62 | -0.58 | 0.561 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -0.01 | 1.61 | -0.01 | 0.993 | 0.999 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.09 | 1.58 | -0.06 | 0.954 | 0.999 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.84 | 1.56 | 0.54 | 0.592 | 0.999 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.93 | 1.58 | 0.59 | 0.557 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.03, *p* = 0.420, η²_G = 0.075
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.00 | 4 | = 1.000 | 0.00 [-0.42, 1.05] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 1.00 | 4 | = 0.609 | 0.41 [-0.77, 0.77] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.00 | 4 | = 0.609 | -0.34 [-0.64, 0.79] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.59 | 4 | = 0.734 | 0.27 [-0.48, 1.25] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.88 | 4 | = 0.609 | 0.41 [-0.84, 0.84] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.63 | 4 | = 0.609 | -0.34 [-1.45, 0.23] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.00 | 4 | = 0.609 | 0.27 [-0.57, 1.13] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -1.58 | 4 | = 0.609 | -0.80 [-0.91, 0.77] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.25 | 4 | = 0.905 | -0.13 [-0.91, 0.76] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 2.14 | 4 | = 0.609 | 0.64 [-0.35, 1.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 186.03, BIC = 203.42
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.00, *SE* = 0.282, *z* = -0.010, *p* = 0.992
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.34, *SE* = 0.285, *z* = 1.200, *p* = 0.230
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.09, *SE* = 0.293, *z* = 3.729, *p* < .001
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.31, *SE* = 0.298, *z* = 1.027, *p* = 0.305
- **SNR**: *β* = 0.30, *SE* = 0.057, *z* = 5.214, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.00 | 0.28 | 0.01 | 0.992 | 0.992 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.34 | 0.28 | -1.20 | 0.230 | 0.792 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -1.09 | 0.29 | -3.73 | < .001 | 0.002 | ** |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -0.31 | 0.30 | -1.03 | 0.305 | 0.792 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.34 | 0.29 | -1.19 | 0.234 | 0.792 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -1.10 | 0.30 | -3.68 | < .001 | 0.002 | ** |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -0.31 | 0.30 | -1.04 | 0.299 | 0.792 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.75 | 0.29 | -2.57 | 0.010 | 0.070 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.04 | 0.29 | 0.12 | 0.902 | 0.990 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.79 | 0.29 | 2.68 | 0.007 | 0.057 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.449, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.78 | 4 | = 0.802 | -0.25 [-0.65, 0.78] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.24 | 4 | = 0.696 | -0.32 [-1.11, 0.47] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.37 | 4 | = 0.696 | -0.45 [-1.44, 0.13] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.18 | 4 | = 0.868 | 0.05 [-1.01, 0.67] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.33 | 4 | = 0.844 | -0.10 [-0.94, 0.73] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.60 | 4 | = 0.833 | -0.22 [-1.22, 0.38] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.73 | 4 | = 0.696 | 0.32 [-0.04, 2.00] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.33 | 4 | = 0.844 | -0.11 [-1.14, 0.57] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 1.06 | 4 | = 0.696 | 0.38 [-0.53, 1.18] | small | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 1.71 | 4 | = 0.696 | 0.52 [-0.36, 1.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 828.53, BIC = 847.97
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 7.33, *SE* = 8.552, *z* = 0.857, *p* = 0.392
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 6.78, *SE* = 8.649, *z* = 0.783, *p* = 0.433
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 16.09, *SE* = 9.054, *z* = 1.777, *p* = 0.076
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.25, *SE* = 10.735, *z* = 0.117, *p* = 0.907
- **SNR**: *β* = -1.18, *SE* = 0.766, *z* = -1.544, *p* = 0.123

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -7.33 | 8.55 | -0.86 | 0.392 | 0.950 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -6.78 | 8.65 | -0.78 | 0.433 | 0.950 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -16.09 | 9.05 | -1.78 | 0.076 | 0.544 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -1.26 | 10.73 | -0.12 | 0.907 | 0.991 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.55 | 8.85 | 0.06 | 0.950 | 0.991 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -8.77 | 9.21 | -0.95 | 0.341 | 0.950 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 6.07 | 10.72 | 0.57 | 0.571 | 0.966 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -9.31 | 9.21 | -1.01 | 0.312 | 0.950 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 5.52 | 10.47 | 0.53 | 0.598 | 0.966 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 14.84 | 10.57 | 1.40 | 0.160 | 0.793 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.04, *p* = 0.029, η²_G = 0.113
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.23 | 9 | = 0.820 | -0.05 [-0.79, 0.22] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.60 | 9 | = 0.801 | -0.19 [-0.72, 0.32] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -3.55 | 9 | = 0.062 | -1.10 [-0.99, 0.12] | large | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.78 | 9 | = 0.759 | -0.28 [-1.08, 0.31] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.44 | 9 | = 0.820 | -0.14 [-0.54, 0.53] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -2.80 | 9 | = 0.099 | -1.00 [-0.83, 0.29] | large | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.89 | 9 | = 0.759 | -0.23 [-1.04, 0.34] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -2.58 | 9 | = 0.099 | -0.81 [-1.24, 0.01] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.34 | 9 | = 0.820 | -0.10 [-0.58, 0.69] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 1.91 | 9 | = 0.220 | 0.63 [-0.17, 1.38] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 354.22, BIC = 373.66
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.47, *SE* = 0.456, *z* = 1.034, *p* = 0.301
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.77, *SE* = 0.463, *z* = 1.662, *p* = 0.097
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.99, *SE* = 0.488, *z* = 2.030, *p* = 0.042
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.63, *SE* = 0.596, *z* = -1.064, *p* = 0.287
- **SNR**: *β* = 0.22, *SE* = 0.044, *z* = 5.007, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.47 | 0.46 | -1.03 | 0.301 | 0.816 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.77 | 0.46 | -1.66 | 0.097 | 0.456 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.99 | 0.49 | -2.03 | 0.042 | 0.292 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.63 | 0.60 | 1.06 | 0.287 | 0.816 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.30 | 0.47 | -0.63 | 0.527 | 0.816 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.52 | 0.49 | -1.05 | 0.292 | 0.816 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 1.11 | 0.59 | 1.88 | 0.060 | 0.352 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.22 | 0.49 | -0.45 | 0.655 | 0.816 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 1.40 | 0.57 | 2.47 | 0.014 | 0.117 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 1.62 | 0.57 | 2.84 | 0.004 | 0.044 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.27, *p* = 0.022, η²_G = 0.134
- Greenhouse-Geisser corrected: *p* = 0.065 (ε = 0.472)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.85 | 9 | = 0.838 | -0.15 [-0.67, 0.33] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.17 | 9 | = 0.915 | -0.05 [-0.72, 0.32] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.40 | 9 | = 0.915 | -0.11 [-0.72, 0.35] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 2.69 | 9 | = 0.124 | 0.97 [0.09, 1.68] | large | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.32 | 9 | = 0.915 | 0.07 [-0.62, 0.45] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.11 | 9 | = 0.915 | 0.04 [-0.51, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 2.37 | 9 | = 0.140 | 0.99 [0.02, 1.57] | large | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.13 | 9 | = 0.915 | -0.04 [-0.52, 0.63] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 1.79 | 9 | = 0.266 | 0.82 [-0.07, 1.32] | large | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 3.53 | 9 | = 0.064 | 0.98 [0.21, 2.03] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Significant main effect of condition (*p* = 0.029) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.022) (no significant pairwise comparisons)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 Fz Component

#### Latency

#### Amplitude

### 5.2 N1 Component

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

### 5.3 P1 Component

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

### 5.4 P3b Component

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
