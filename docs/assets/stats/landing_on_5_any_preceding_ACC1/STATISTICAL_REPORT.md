# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:29:08

---

## 1. Analysis Overview

**Total Measurements:** 448
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
| 2 to 5 | 24 | 98.17 ms | 11.19 | 2.28 | [84.00, 112.00] |
| 3 to 5 | 24 | 100.00 ms | 10.55 | 2.15 | [84.00, 112.00] |
| 4 to 5 | 24 | 95.83 ms | 9.32 | 1.90 | [84.00, 112.00] |
| 5 to 5 | 24 | 99.83 ms | 10.91 | 2.23 | [84.00, 112.00] |
| 6 to 5 | 16 | 97.75 ms | 12.39 | 3.10 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | -1.44 µV | 2.86 | 0.58 | [-12.97, 1.02] |
| 3 to 5 | 24 | -1.50 µV | 2.32 | 0.47 | [-4.98, 4.56] |
| 4 to 5 | 24 | -4.18 µV | 5.10 | 1.04 | [-18.83, 3.46] |
| 5 to 5 | 24 | -2.05 µV | 2.23 | 0.45 | [-7.37, 0.84] |
| 6 to 5 | 16 | -0.91 µV | 2.52 | 0.63 | [-4.24, 4.81] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 172.83 ms | 20.43 | 4.17 | [132.00, 208.00] |
| 3 to 5 | 24 | 165.83 ms | 24.37 | 4.98 | [132.00, 208.00] |
| 4 to 5 | 24 | 169.33 ms | 21.45 | 4.38 | [132.00, 208.00] |
| 5 to 5 | 24 | 170.83 ms | 17.71 | 3.62 | [132.00, 196.00] |
| 6 to 5 | 16 | 178.75 ms | 25.95 | 6.49 | [132.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | -6.40 µV | 2.60 | 0.53 | [-13.83, -1.17] |
| 3 to 5 | 24 | -5.70 µV | 2.73 | 0.56 | [-13.75, -0.84] |
| 4 to 5 | 24 | -6.80 µV | 3.96 | 0.81 | [-16.53, 0.62] |
| 5 to 5 | 24 | -6.04 µV | 2.55 | 0.52 | [-12.06, -1.67] |
| 6 to 5 | 16 | -7.46 µV | 2.06 | 0.52 | [-10.73, -3.38] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 97.17 ms | 8.79 | 1.79 | [88.00, 108.00] |
| 3 to 5 | 24 | 98.17 ms | 8.75 | 1.79 | [88.00, 108.00] |
| 4 to 5 | 24 | 98.00 ms | 8.51 | 1.74 | [88.00, 108.00] |
| 5 to 5 | 24 | 99.17 ms | 8.98 | 1.83 | [88.00, 108.00] |
| 6 to 5 | 16 | 100.75 ms | 8.91 | 2.23 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 1.71 µV | 2.87 | 0.59 | [-2.79, 11.63] |
| 3 to 5 | 24 | 1.22 µV | 2.53 | 0.52 | [-3.58, 5.64] |
| 4 to 5 | 24 | 3.38 µV | 5.12 | 1.05 | [-4.56, 19.20] |
| 5 to 5 | 24 | 1.85 µV | 1.72 | 0.35 | [-1.12, 5.37] |
| 6 to 5 | 16 | 0.56 µV | 2.10 | 0.53 | [-2.94, 5.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 460.83 ms | 66.15 | 13.50 | [364.00, 572.00] |
| 3 to 5 | 24 | 472.00 ms | 71.60 | 14.62 | [360.00, 572.00] |
| 4 to 5 | 24 | 467.83 ms | 77.74 | 15.87 | [360.00, 572.00] |
| 5 to 5 | 24 | 460.67 ms | 77.52 | 15.82 | [356.00, 564.00] |
| 6 to 5 | 16 | 504.00 ms | 71.49 | 17.87 | [368.00, 572.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 6.01 µV | 2.91 | 0.59 | [0.88, 11.71] |
| 3 to 5 | 24 | 5.00 µV | 3.75 | 0.77 | [-2.85, 16.52] |
| 4 to 5 | 24 | 5.85 µV | 4.57 | 0.93 | [-2.82, 13.88] |
| 5 to 5 | 24 | 2.65 µV | 2.52 | 0.51 | [-3.99, 5.39] |
| 6 to 5 | 16 | 5.46 µV | 3.39 | 0.85 | [-2.57, 10.24] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 858.88, BIC = 880.63
- **3 to 5 vs 2 to 5**: *β* = 2.06, *SE* = 2.862, *z* = 0.720, *p* = 0.472
- **4 to 5 vs 2 to 5**: *β* = -2.12, *SE* = 2.859, *z* = -0.741, *p* = 0.459
- **5 to 5 vs 2 to 5**: *β* = 1.94, *SE* = 2.872, *z* = 0.674, *p* = 0.501
- **6 to 5 vs 2 to 5**: *β* = -0.07, *SE* = 3.210, *z* = -0.022, *p* = 0.983
- **SNR**: *β* = -0.33, *SE* = 0.560, *z* = -0.580, *p* = 0.562

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -2.06 | 2.86 | -0.72 | 0.472 | 0.993 | n.s. |
| 2 to 5 - 4 to 5 | 2.12 | 2.86 | 0.74 | 0.459 | 0.993 | n.s. |
| 2 to 5 - 5 to 5 | -1.93 | 2.87 | -0.67 | 0.501 | 0.993 | n.s. |
| 2 to 5 - 6 to 5 | 0.07 | 3.21 | 0.02 | 0.983 | 0.999 | n.s. |
| 3 to 5 - 4 to 5 | 4.18 | 2.84 | 1.47 | 0.141 | 0.780 | n.s. |
| 3 to 5 - 5 to 5 | 0.13 | 2.84 | 0.04 | 0.965 | 0.999 | n.s. |
| 3 to 5 - 6 to 5 | 2.13 | 3.21 | 0.66 | 0.507 | 0.993 | n.s. |
| 4 to 5 - 5 to 5 | -4.05 | 2.84 | -1.43 | 0.153 | 0.780 | n.s. |
| 4 to 5 - 6 to 5 | -2.05 | 3.21 | -0.64 | 0.523 | 0.993 | n.s. |
| 5 to 5 - 6 to 5 | 2.00 | 3.21 | 0.62 | 0.533 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.612, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.35 | 15 | = 0.808 | -0.44 [-0.55, 0.30] | small | n.s. |
| 2 to 5 vs 4 to 5 | 0.00 | 15 | = 1.000 | 0.00 [-0.24, 0.61] | negligible | n.s. |
| 2 to 5 vs 5 to 5 | -0.81 | 15 | = 0.808 | -0.29 [-0.53, 0.32] | small | n.s. |
| 2 to 5 vs 6 to 5 | -0.47 | 15 | = 0.808 | -0.17 [-0.65, 0.42] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 1.27 | 15 | = 0.808 | 0.48 [-0.15, 0.71] | small | n.s. |
| 3 to 5 vs 5 to 5 | 0.51 | 15 | = 0.808 | 0.16 [-0.41, 0.44] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 0.88 | 15 | = 0.808 | 0.26 [-0.32, 0.76] | small | n.s. |
| 4 to 5 vs 5 to 5 | -1.13 | 15 | = 0.808 | -0.31 [-0.78, 0.09] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.52 | 15 | = 0.808 | -0.18 [-0.67, 0.40] | negligible | n.s. |
| 5 to 5 vs 6 to 5 | 0.31 | 15 | = 0.847 | 0.11 [-0.46, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 565.18, BIC = 586.93
- **3 to 5 vs 2 to 5**: *β* = 0.41, *SE* = 0.774, *z* = 0.526, *p* = 0.599
- **4 to 5 vs 2 to 5**: *β* = -2.29, *SE* = 0.773, *z* = -2.966, *p* = 0.003
- **5 to 5 vs 2 to 5**: *β* = -0.06, *SE* = 0.777, *z* = -0.073, *p* = 0.941
- **6 to 5 vs 2 to 5**: *β* = 0.45, *SE* = 0.875, *z* = 0.510, *p* = 0.610
- **SNR**: *β* = -0.67, *SE* = 0.149, *z* = -4.474, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.41 | 0.77 | -0.53 | 0.599 | 0.991 | n.s. |
| 2 to 5 - 4 to 5 | 2.29 | 0.77 | 2.97 | 0.003 | 0.024 | * |
| 2 to 5 - 5 to 5 | 0.06 | 0.78 | 0.07 | 0.941 | 0.997 | n.s. |
| 2 to 5 - 6 to 5 | -0.45 | 0.87 | -0.51 | 0.610 | 0.991 | n.s. |
| 3 to 5 - 4 to 5 | 2.70 | 0.77 | 3.52 | < .001 | 0.004 | ** |
| 3 to 5 - 5 to 5 | 0.46 | 0.77 | 0.60 | 0.545 | 0.991 | n.s. |
| 3 to 5 - 6 to 5 | -0.04 | 0.87 | -0.05 | 0.964 | 0.997 | n.s. |
| 4 to 5 - 5 to 5 | -2.24 | 0.77 | -2.92 | 0.004 | 0.025 | * |
| 4 to 5 - 6 to 5 | -2.74 | 0.87 | -3.14 | 0.002 | 0.015 | * |
| 5 to 5 - 6 to 5 | -0.50 | 0.87 | -0.58 | 0.564 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.46, *p* = 0.055, η²_G = 0.111
- Greenhouse-Geisser corrected: *p* = 0.095 (ε = 0.558)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.21 | 15 | = 0.351 | 0.36 [-0.40, 0.44] | small | n.s. |
| 2 to 5 vs 4 to 5 | 2.80 | 15 | = 0.135 | 0.90 [0.29, 1.25] | large | n.s. |
| 2 to 5 vs 5 to 5 | 2.37 | 15 | = 0.159 | 0.82 [-0.23, 0.62] | large | n.s. |
| 2 to 5 vs 6 to 5 | 0.35 | 15 | = 0.752 | 0.13 [-0.45, 0.62] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 1.86 | 15 | = 0.250 | 0.63 [0.04, 0.93] | medium | n.s. |
| 3 to 5 vs 5 to 5 | 1.60 | 15 | = 0.250 | 0.41 [-0.17, 0.69] | small | n.s. |
| 3 to 5 vs 6 to 5 | -0.32 | 15 | = 0.752 | -0.11 [-0.61, 0.45] | negligible | n.s. |
| 4 to 5 vs 5 to 5 | -0.77 | 15 | = 0.564 | -0.32 [-0.80, 0.07] | small | n.s. |
| 4 to 5 vs 6 to 5 | -1.71 | 15 | = 0.250 | -0.62 [-0.98, 0.13] | medium | n.s. |
| 5 to 5 vs 6 to 5 | -1.52 | 15 | = 0.250 | -0.42 [-0.93, 0.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 966.70, BIC = 988.45
- **3 to 5 vs 2 to 5**: *β* = -7.37, *SE* = 3.880, *z* = -1.899, *p* = 0.058
- **4 to 5 vs 2 to 5**: *β* = -4.02, *SE* = 3.885, *z* = -1.034, *p* = 0.301
- **5 to 5 vs 2 to 5**: *β* = -2.58, *SE* = 3.887, *z* = -0.662, *p* = 0.508
- **6 to 5 vs 2 to 5**: *β* = 6.10, *SE* = 4.461, *z* = 1.367, *p* = 0.172
- **SNR**: *β* = 1.16, *SE* = 0.609, *z* = 1.910, *p* = 0.056

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 7.37 | 3.88 | 1.90 | 0.058 | 0.361 | n.s. |
| 2 to 5 - 4 to 5 | 4.02 | 3.88 | 1.03 | 0.301 | 0.761 | n.s. |
| 2 to 5 - 5 to 5 | 2.57 | 3.89 | 0.66 | 0.508 | 0.770 | n.s. |
| 2 to 5 - 6 to 5 | -6.10 | 4.46 | -1.37 | 0.172 | 0.677 | n.s. |
| 3 to 5 - 4 to 5 | -3.35 | 3.88 | -0.87 | 0.387 | 0.770 | n.s. |
| 3 to 5 - 5 to 5 | -4.80 | 3.88 | -1.24 | 0.216 | 0.704 | n.s. |
| 3 to 5 - 6 to 5 | -13.47 | 4.49 | -3.00 | 0.003 | 0.027 | * |
| 4 to 5 - 5 to 5 | -1.44 | 3.88 | -0.37 | 0.710 | 0.770 | n.s. |
| 4 to 5 - 6 to 5 | -10.12 | 4.50 | -2.25 | 0.025 | 0.201 | n.s. |
| 5 to 5 - 6 to 5 | -8.67 | 4.51 | -1.92 | 0.054 | 0.361 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.363, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.63 | 15 | = 0.782 | 0.15 [-0.10, 0.77] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 0.23 | 15 | = 0.909 | 0.05 [-0.26, 0.59] | negligible | n.s. |
| 2 to 5 vs 5 to 5 | 0.25 | 15 | = 0.909 | 0.05 [-0.29, 0.56] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -1.07 | 15 | = 0.754 | -0.26 [-0.81, 0.27] | small | n.s. |
| 3 to 5 vs 4 to 5 | -0.62 | 15 | = 0.782 | -0.10 [-0.64, 0.21] | negligible | n.s. |
| 3 to 5 vs 5 to 5 | -0.69 | 15 | = 0.782 | -0.12 [-0.71, 0.15] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.74 | 15 | = 0.754 | -0.39 [-0.99, 0.12] | small | n.s. |
| 4 to 5 vs 5 to 5 | -0.09 | 15 | = 0.932 | -0.01 [-0.51, 0.34] | negligible | n.s. |
| 4 to 5 vs 6 to 5 | -1.25 | 15 | = 0.754 | -0.31 [-0.86, 0.23] | small | n.s. |
| 5 to 5 vs 6 to 5 | -1.28 | 15 | = 0.754 | -0.33 [-0.87, 0.23] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 508.74, BIC = 530.49
- **3 to 5 vs 2 to 5**: *β* = 0.81, *SE* = 0.527, *z* = 1.540, *p* = 0.123
- **4 to 5 vs 2 to 5**: *β* = -0.24, *SE* = 0.527, *z* = -0.464, *p* = 0.642
- **5 to 5 vs 2 to 5**: *β* = 0.53, *SE* = 0.528, *z* = 0.995, *p* = 0.320
- **6 to 5 vs 2 to 5**: *β* = -1.42, *SE* = 0.604, *z* = -2.347, *p* = 0.019
- **SNR**: *β* = -0.35, *SE* = 0.079, *z* = -4.400, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.81 | 0.53 | -1.54 | 0.123 | 0.483 | n.s. |
| 2 to 5 - 4 to 5 | 0.24 | 0.53 | 0.46 | 0.642 | 0.829 | n.s. |
| 2 to 5 - 5 to 5 | -0.52 | 0.53 | -1.00 | 0.320 | 0.685 | n.s. |
| 2 to 5 - 6 to 5 | 1.42 | 0.60 | 2.35 | 0.019 | 0.142 | n.s. |
| 3 to 5 - 4 to 5 | 1.06 | 0.53 | 2.01 | 0.045 | 0.274 | n.s. |
| 3 to 5 - 5 to 5 | 0.29 | 0.53 | 0.54 | 0.586 | 0.829 | n.s. |
| 3 to 5 - 6 to 5 | 2.23 | 0.61 | 3.67 | < .001 | 0.002 | ** |
| 4 to 5 - 5 to 5 | -0.77 | 0.53 | -1.46 | 0.143 | 0.483 | n.s. |
| 4 to 5 - 6 to 5 | 1.17 | 0.61 | 1.93 | 0.054 | 0.284 | n.s. |
| 5 to 5 - 6 to 5 | 1.94 | 0.61 | 3.19 | 0.001 | 0.013 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.76, *p* = 0.009, η²_G = 0.080
- Greenhouse-Geisser corrected: *p* = 0.027 (ε = 0.592)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.29 | 15 | = 0.309 | -0.25 [-0.70, 0.16] | small | n.s. |
| 2 to 5 vs 4 to 5 | 1.34 | 15 | = 0.309 | 0.32 [-0.30, 0.54] | small | n.s. |
| 2 to 5 vs 5 to 5 | -0.99 | 15 | = 0.421 | -0.21 [-0.58, 0.27] | small | n.s. |
| 2 to 5 vs 6 to 5 | 1.90 | 15 | = 0.153 | 0.50 [-0.09, 1.04] | medium | n.s. |
| 3 to 5 vs 4 to 5 | 2.48 | 15 | = 0.085 | 0.53 [-0.09, 0.78] | medium | n.s. |
| 3 to 5 vs 5 to 5 | 0.28 | 15 | = 0.870 | 0.04 [-0.23, 0.62] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 4.40 | 15 | = 0.005 | 0.89 [0.42, 1.77] | large | ** |
| 4 to 5 vs 5 to 5 | -2.31 | 15 | = 0.089 | -0.50 [-0.66, 0.19] | medium | n.s. |
| 4 to 5 vs 6 to 5 | 0.08 | 15 | = 0.934 | 0.02 [-0.51, 0.55] | negligible | n.s. |
| 5 to 5 vs 6 to 5 | 3.10 | 15 | = 0.036 | 0.82 [0.17, 1.38] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 782.86, BIC = 804.61
- **3 to 5 vs 2 to 5**: *β* = 0.97, *SE* = 1.842, *z* = 0.529, *p* = 0.597
- **4 to 5 vs 2 to 5**: *β* = 0.81, *SE* = 1.831, *z* = 0.443, *p* = 0.658
- **5 to 5 vs 2 to 5**: *β* = 1.99, *SE* = 1.813, *z* = 1.095, *p* = 0.274
- **6 to 5 vs 2 to 5**: *β* = 4.17, *SE* = 2.050, *z* = 2.033, *p* = 0.042
- **SNR**: *β* = 0.04, *SE* = 0.556, *z* = 0.064, *p* = 0.949

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.97 | 1.84 | -0.53 | 0.597 | 0.973 | n.s. |
| 2 to 5 - 4 to 5 | -0.81 | 1.83 | -0.44 | 0.658 | 0.973 | n.s. |
| 2 to 5 - 5 to 5 | -1.98 | 1.81 | -1.09 | 0.274 | 0.893 | n.s. |
| 2 to 5 - 6 to 5 | -4.17 | 2.05 | -2.03 | 0.042 | 0.349 | n.s. |
| 3 to 5 - 4 to 5 | 0.16 | 1.80 | 0.09 | 0.928 | 0.973 | n.s. |
| 3 to 5 - 5 to 5 | -1.01 | 1.81 | -0.56 | 0.576 | 0.973 | n.s. |
| 3 to 5 - 6 to 5 | -3.19 | 2.08 | -1.53 | 0.125 | 0.656 | n.s. |
| 4 to 5 - 5 to 5 | -1.17 | 1.80 | -0.65 | 0.515 | 0.973 | n.s. |
| 4 to 5 - 6 to 5 | -3.36 | 2.07 | -1.62 | 0.105 | 0.633 | n.s. |
| 5 to 5 - 6 to 5 | -2.18 | 2.06 | -1.06 | 0.289 | 0.893 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.32, *p* = 0.067, η²_G = 0.057
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.54 | 15 | = 0.287 | -0.38 [-0.54, 0.31] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.72 | 15 | = 0.559 | -0.18 [-0.51, 0.34] | negligible | n.s. |
| 2 to 5 vs 5 to 5 | -2.45 | 15 | = 0.136 | -0.55 [-0.65, 0.20] | medium | n.s. |
| 2 to 5 vs 6 to 5 | -2.70 | 15 | = 0.136 | -0.67 [-1.27, -0.08] | medium | n.s. |
| 3 to 5 vs 4 to 5 | 0.71 | 15 | = 0.559 | 0.20 [-0.41, 0.44] | negligible | n.s. |
| 3 to 5 vs 5 to 5 | -0.69 | 15 | = 0.559 | -0.17 [-0.54, 0.31] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.05 | 15 | = 0.521 | -0.28 [-0.80, 0.28] | small | n.s. |
| 4 to 5 vs 5 to 5 | -1.93 | 15 | = 0.241 | -0.37 [-0.59, 0.26] | small | n.s. |
| 4 to 5 vs 6 to 5 | -1.71 | 15 | = 0.271 | -0.49 [-0.98, 0.13] | small | n.s. |
| 5 to 5 vs 6 to 5 | -0.47 | 15 | = 0.643 | -0.11 [-0.65, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 574.78, BIC = 596.52
- **3 to 5 vs 2 to 5**: *β* = -0.68, *SE* = 0.776, *z* = -0.877, *p* = 0.380
- **4 to 5 vs 2 to 5**: *β* = 1.50, *SE* = 0.772, *z* = 1.944, *p* = 0.052
- **5 to 5 vs 2 to 5**: *β* = 0.03, *SE* = 0.765, *z* = 0.039, *p* = 0.969
- **6 to 5 vs 2 to 5**: *β* = -0.71, *SE* = 0.866, *z* = -0.823, *p* = 0.410
- **SNR**: *β* = 0.27, *SE* = 0.221, *z* = 1.236, *p* = 0.216

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 0.68 | 0.78 | 0.88 | 0.380 | 0.925 | n.s. |
| 2 to 5 - 4 to 5 | -1.50 | 0.77 | -1.94 | 0.052 | 0.347 | n.s. |
| 2 to 5 - 5 to 5 | -0.03 | 0.76 | -0.04 | 0.969 | 0.999 | n.s. |
| 2 to 5 - 6 to 5 | 0.71 | 0.87 | 0.82 | 0.410 | 0.925 | n.s. |
| 3 to 5 - 4 to 5 | -2.18 | 0.76 | -2.87 | 0.004 | 0.040 | * |
| 3 to 5 - 5 to 5 | -0.71 | 0.76 | -0.93 | 0.351 | 0.925 | n.s. |
| 3 to 5 - 6 to 5 | 0.03 | 0.88 | 0.04 | 0.970 | 0.999 | n.s. |
| 4 to 5 - 5 to 5 | 1.47 | 0.76 | 1.93 | 0.053 | 0.347 | n.s. |
| 4 to 5 - 6 to 5 | 2.21 | 0.87 | 2.53 | 0.011 | 0.098 | n.s. |
| 5 to 5 - 6 to 5 | 0.74 | 0.87 | 0.85 | 0.393 | 0.925 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.20, *p* = 0.318, η²_G = 0.043
- Greenhouse-Geisser corrected: *p* = 0.316 (ε = 0.559)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.79 | 15 | = 0.635 | 0.22 [-0.24, 0.62] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.79 | 15 | = 0.635 | -0.24 [-0.78, 0.09] | small | n.s. |
| 2 to 5 vs 5 to 5 | -0.22 | 15 | = 0.826 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 1.81 | 15 | = 0.352 | 0.33 [-0.11, 1.01] | small | n.s. |
| 3 to 5 vs 4 to 5 | -1.12 | 15 | = 0.557 | -0.41 [-0.82, 0.05] | small | n.s. |
| 3 to 5 vs 5 to 5 | -1.61 | 15 | = 0.352 | -0.30 [-0.79, 0.08] | small | n.s. |
| 3 to 5 vs 6 to 5 | 0.39 | 15 | = 0.780 | 0.10 [-0.44, 0.63] | negligible | n.s. |
| 4 to 5 vs 5 to 5 | 0.60 | 15 | = 0.695 | 0.21 [-0.15, 0.71] | small | n.s. |
| 4 to 5 vs 6 to 5 | 1.63 | 15 | = 0.352 | 0.51 [-0.15, 0.96] | medium | n.s. |
| 5 to 5 vs 6 to 5 | 1.56 | 15 | = 0.352 | 0.43 [-0.16, 0.94] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1286.42, BIC = 1308.16
- **3 to 5 vs 2 to 5**: *β* = 10.95, *SE* = 19.251, *z* = 0.569, *p* = 0.570
- **4 to 5 vs 2 to 5**: *β* = 7.19, *SE* = 19.250, *z* = 0.373, *p* = 0.709
- **5 to 5 vs 2 to 5**: *β* = -1.05, *SE* = 19.278, *z* = -0.055, *p* = 0.957
- **6 to 5 vs 2 to 5**: *β* = 41.73, *SE* = 21.757, *z* = 1.918, *p* = 0.055
- **SNR**: *β* = -2.18, *SE* = 2.639, *z* = -0.827, *p* = 0.408

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -10.95 | 19.25 | -0.57 | 0.570 | 0.990 | n.s. |
| 2 to 5 - 4 to 5 | -7.19 | 19.25 | -0.37 | 0.709 | 0.990 | n.s. |
| 2 to 5 - 5 to 5 | 1.05 | 19.28 | 0.05 | 0.957 | 0.990 | n.s. |
| 2 to 5 - 6 to 5 | -41.73 | 21.76 | -1.92 | 0.055 | 0.399 | n.s. |
| 3 to 5 - 4 to 5 | 3.76 | 19.25 | 0.20 | 0.845 | 0.990 | n.s. |
| 3 to 5 - 5 to 5 | 12.00 | 19.27 | 0.62 | 0.534 | 0.990 | n.s. |
| 3 to 5 - 6 to 5 | -30.79 | 21.74 | -1.42 | 0.157 | 0.697 | n.s. |
| 4 to 5 - 5 to 5 | 8.24 | 19.29 | 0.43 | 0.669 | 0.990 | n.s. |
| 4 to 5 - 6 to 5 | -34.55 | 21.77 | -1.59 | 0.113 | 0.615 | n.s. |
| 5 to 5 - 6 to 5 | -42.78 | 21.71 | -1.97 | 0.049 | 0.394 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.32, *p* = 0.067, η²_G = 0.086
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.57 | 15 | = 0.670 | -0.17 [-0.56, 0.28] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -2.44 | 15 | = 0.101 | -0.62 [-0.50, 0.35] | medium | n.s. |
| 2 to 5 vs 5 to 5 | -0.67 | 15 | = 0.670 | -0.20 [-0.42, 0.42] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -2.39 | 15 | = 0.101 | -0.80 [-1.18, -0.02] | large | n.s. |
| 3 to 5 vs 4 to 5 | -1.38 | 15 | = 0.315 | -0.47 [-0.38, 0.46] | small | n.s. |
| 3 to 5 vs 5 to 5 | -0.12 | 15 | = 0.910 | -0.05 [-0.33, 0.52] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -2.54 | 15 | = 0.101 | -0.65 [-1.22, -0.05] | medium | n.s. |
| 4 to 5 vs 5 to 5 | 1.40 | 15 | = 0.315 | 0.40 [-0.35, 0.49] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.53 | 15 | = 0.670 | -0.14 [-0.67, 0.40] | negligible | n.s. |
| 5 to 5 vs 6 to 5 | -1.72 | 15 | = 0.267 | -0.56 [-0.99, 0.13] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 581.14, BIC = 602.89
- **3 to 5 vs 2 to 5**: *β* = -1.00, *SE* = 0.736, *z* = -1.355, *p* = 0.176
- **4 to 5 vs 2 to 5**: *β* = -0.17, *SE* = 0.736, *z* = -0.230, *p* = 0.818
- **5 to 5 vs 2 to 5**: *β* = -3.31, *SE* = 0.737, *z* = -4.485, *p* < .001
- **6 to 5 vs 2 to 5**: *β* = -0.96, *SE* = 0.842, *z* = -1.139, *p* = 0.255
- **SNR**: *β* = 0.13, *SE* = 0.107, *z* = 1.221, *p* = 0.222

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 1.00 | 0.74 | 1.35 | 0.176 | 0.686 | n.s. |
| 2 to 5 - 4 to 5 | 0.17 | 0.74 | 0.23 | 0.818 | 0.967 | n.s. |
| 2 to 5 - 5 to 5 | 3.31 | 0.74 | 4.48 | < .001 | < .001 | *** |
| 2 to 5 - 6 to 5 | 0.96 | 0.84 | 1.14 | 0.255 | 0.770 | n.s. |
| 3 to 5 - 4 to 5 | -0.83 | 0.74 | -1.12 | 0.261 | 0.770 | n.s. |
| 3 to 5 - 5 to 5 | 2.31 | 0.74 | 3.13 | 0.002 | 0.014 | * |
| 3 to 5 - 6 to 5 | -0.04 | 0.84 | -0.04 | 0.965 | 0.967 | n.s. |
| 4 to 5 - 5 to 5 | 3.14 | 0.74 | 4.25 | < .001 | < .001 | *** |
| 4 to 5 - 6 to 5 | 0.79 | 0.84 | 0.94 | 0.349 | 0.770 | n.s. |
| 5 to 5 - 6 to 5 | -2.35 | 0.84 | -2.79 | 0.005 | 0.036 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.89, *p* = 0.002, η²_G = 0.123
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 3.60 | 15 | = 0.013 | 0.59 [-0.12, 0.74] | medium | * |
| 2 to 5 vs 4 to 5 | 0.59 | 15 | = 0.624 | 0.11 [-0.38, 0.47] | negligible | n.s. |
| 2 to 5 vs 5 to 5 | 4.04 | 15 | = 0.011 | 1.26 [0.61, 1.70] | large | * |
| 2 to 5 vs 6 to 5 | 1.78 | 15 | = 0.137 | 0.41 [-0.11, 1.00] | small | n.s. |
| 3 to 5 vs 4 to 5 | -1.91 | 15 | = 0.135 | -0.41 [-0.64, 0.21] | small | n.s. |
| 3 to 5 vs 5 to 5 | 2.21 | 15 | = 0.107 | 0.68 [0.16, 1.08] | medium | n.s. |
| 3 to 5 vs 6 to 5 | -0.40 | 15 | = 0.698 | -0.11 [-0.63, 0.44] | negligible | n.s. |
| 4 to 5 vs 5 to 5 | 3.05 | 15 | = 0.027 | 0.94 [0.25, 1.20] | large | * |
| 4 to 5 vs 6 to 5 | 0.97 | 15 | = 0.434 | 0.27 [-0.30, 0.78] | small | n.s. |
| 5 to 5 vs 6 to 5 | -1.87 | 15 | = 0.135 | -0.65 [-1.03, 0.09] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.055)
**N1 amplitude:** Significant main effect of condition (*p* = 0.009). Post-hoc tests revealed:
  - 3 to 5 showed greater amplitude than 6 to 5 (*d* = 0.89)
  - 5 to 5 showed greater amplitude than 6 to 5 (*d* = 0.82)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.067)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.067)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 2 to 5 showed greater amplitude than 3 to 5 (*d* = 0.59)
  - 2 to 5 showed greater amplitude than 5 to 5 (*d* = 1.26)
  - 4 to 5 showed greater amplitude than 5 to 5 (*d* = 0.94)

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
