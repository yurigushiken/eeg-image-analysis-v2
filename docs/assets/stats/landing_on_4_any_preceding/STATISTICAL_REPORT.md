# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:28:37

---

## 1. Analysis Overview

**Total Measurements:** 576
**Number of Subjects:** 24
**Number of Conditions:** 6

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
| 1 to 4 | 24 | 105.00 ms | 8.53 | 1.74 | [96.00, 116.00] |
| 2 to 4 | 24 | 103.83 ms | 7.78 | 1.59 | [96.00, 116.00] |
| 3 to 4 | 24 | 106.17 ms | 8.59 | 1.75 | [96.00, 116.00] |
| 5 to 4 | 24 | 106.67 ms | 8.31 | 1.70 | [96.00, 116.00] |
| 6 to 4 | 24 | 108.00 ms | 8.09 | 1.65 | [96.00, 116.00] |
| Cardinality4 | 24 | 107.33 ms | 7.70 | 1.57 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -1.30 µV | 1.98 | 0.40 | [-4.46, 2.75] |
| 2 to 4 | 24 | -1.73 µV | 1.94 | 0.40 | [-6.14, 1.67] |
| 3 to 4 | 24 | -1.55 µV | 1.77 | 0.36 | [-5.42, 1.50] |
| 5 to 4 | 24 | -1.54 µV | 2.54 | 0.52 | [-7.02, 3.36] |
| 6 to 4 | 24 | -2.10 µV | 1.81 | 0.37 | [-7.38, 0.61] |
| Cardinality4 | 24 | -1.56 µV | 1.86 | 0.38 | [-6.84, 1.26] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 171.83 ms | 18.33 | 3.74 | [144.00, 204.00] |
| 2 to 4 | 24 | 173.17 ms | 16.41 | 3.35 | [144.00, 204.00] |
| 3 to 4 | 24 | 167.83 ms | 18.93 | 3.86 | [144.00, 204.00] |
| 5 to 4 | 24 | 174.67 ms | 19.65 | 4.01 | [144.00, 204.00] |
| 6 to 4 | 24 | 173.00 ms | 20.10 | 4.10 | [144.00, 204.00] |
| Cardinality4 | 24 | 172.00 ms | 19.77 | 4.04 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -6.31 µV | 2.98 | 0.61 | [-12.55, -1.25] |
| 2 to 4 | 24 | -6.19 µV | 2.98 | 0.61 | [-15.66, -0.75] |
| 3 to 4 | 24 | -5.37 µV | 2.45 | 0.50 | [-10.31, 0.32] |
| 5 to 4 | 24 | -5.89 µV | 2.79 | 0.57 | [-14.15, -1.72] |
| 6 to 4 | 24 | -5.41 µV | 2.71 | 0.55 | [-12.20, -1.17] |
| Cardinality4 | 24 | -5.52 µV | 3.34 | 0.68 | [-13.09, 0.33] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 100.67 ms | 10.40 | 2.12 | [92.00, 120.00] |
| 2 to 4 | 24 | 104.83 ms | 10.81 | 2.21 | [92.00, 120.00] |
| 3 to 4 | 24 | 104.83 ms | 11.31 | 2.31 | [92.00, 120.00] |
| 5 to 4 | 24 | 108.50 ms | 12.22 | 2.49 | [92.00, 120.00] |
| 6 to 4 | 24 | 110.00 ms | 10.42 | 2.13 | [92.00, 120.00] |
| Cardinality4 | 24 | 109.67 ms | 11.31 | 2.31 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 1.83 µV | 2.30 | 0.47 | [-2.47, 6.92] |
| 2 to 4 | 24 | 2.02 µV | 2.12 | 0.43 | [-2.77, 7.56] |
| 3 to 4 | 24 | 2.23 µV | 2.24 | 0.46 | [-0.20, 7.39] |
| 5 to 4 | 24 | 1.73 µV | 2.38 | 0.49 | [-2.44, 7.17] |
| 6 to 4 | 24 | 2.25 µV | 2.65 | 0.54 | [-3.00, 7.60] |
| Cardinality4 | 24 | 1.78 µV | 2.33 | 0.48 | [-3.85, 6.93] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 487.50 ms | 30.38 | 6.20 | [432.00, 536.00] |
| 2 to 4 | 24 | 483.83 ms | 34.26 | 6.99 | [432.00, 536.00] |
| 3 to 4 | 24 | 489.17 ms | 37.74 | 7.70 | [432.00, 536.00] |
| 5 to 4 | 24 | 492.50 ms | 33.51 | 6.84 | [440.00, 536.00] |
| 6 to 4 | 24 | 481.67 ms | 34.33 | 7.01 | [432.00, 536.00] |
| Cardinality4 | 24 | 473.50 ms | 30.37 | 6.20 | [432.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 4.59 µV | 3.53 | 0.72 | [-1.27, 11.88] |
| 2 to 4 | 24 | 5.17 µV | 4.86 | 0.99 | [-4.77, 17.43] |
| 3 to 4 | 24 | 3.95 µV | 4.31 | 0.88 | [-3.98, 12.86] |
| 5 to 4 | 24 | 4.49 µV | 4.09 | 0.83 | [-3.30, 11.49] |
| 6 to 4 | 24 | 4.10 µV | 3.62 | 0.74 | [-4.76, 9.62] |
| Cardinality4 | 24 | 1.55 µV | 3.99 | 0.81 | [-9.79, 8.96] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1004.85, BIC = 1031.58
- **2 to 4 vs 1 to 4**: *β* = -0.82, *SE* = 1.960, *z* = -0.421, *p* = 0.674
- **3 to 4 vs 1 to 4**: *β* = 1.55, *SE* = 1.964, *z* = 0.788, *p* = 0.431
- **5 to 4 vs 1 to 4**: *β* = 1.59, *SE* = 1.946, *z* = 0.817, *p* = 0.414
- **6 to 4 vs 1 to 4**: *β* = 3.18, *SE* = 1.950, *z* = 1.633, *p* = 0.102
- **Cardinality4 vs 1 to 4**: *β* = 2.49, *SE* = 1.949, *z* = 1.280, *p* = 0.201
- **SNR**: *β* = 0.68, *SE* = 0.480, *z* = 1.410, *p* = 0.159

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 0.83 | 1.96 | 0.42 | 0.674 | 0.993 | n.s. |
| 1 to 4 - 3 to 4 | -1.55 | 1.96 | -0.79 | 0.431 | 0.990 | n.s. |
| 1 to 4 - 5 to 4 | -1.59 | 1.95 | -0.82 | 0.414 | 0.990 | n.s. |
| 1 to 4 - 6 to 4 | -3.18 | 1.95 | -1.63 | 0.102 | 0.755 | n.s. |
| 1 to 4 - Cardinality4 | -2.49 | 1.95 | -1.28 | 0.201 | 0.932 | n.s. |
| 2 to 4 - 3 to 4 | -2.37 | 1.95 | -1.22 | 0.222 | 0.935 | n.s. |
| 2 to 4 - 5 to 4 | -2.42 | 1.97 | -1.23 | 0.220 | 0.935 | n.s. |
| 2 to 4 - 6 to 4 | -4.01 | 1.95 | -2.06 | 0.040 | 0.455 | n.s. |
| 2 to 4 - Cardinality4 | -3.32 | 1.95 | -1.70 | 0.089 | 0.727 | n.s. |
| 3 to 4 - 5 to 4 | -0.04 | 1.97 | -0.02 | 0.983 | 0.993 | n.s. |
| 3 to 4 - 6 to 4 | -1.64 | 1.95 | -0.84 | 0.402 | 0.990 | n.s. |
| 3 to 4 - Cardinality4 | -0.95 | 1.95 | -0.48 | 0.628 | 0.993 | n.s. |
| 5 to 4 - 6 to 4 | -1.59 | 1.95 | -0.82 | 0.415 | 0.990 | n.s. |
| 5 to 4 - Cardinality4 | -0.90 | 1.95 | -0.46 | 0.643 | 0.993 | n.s. |
| 6 to 4 - Cardinality4 | 0.69 | 1.95 | 0.35 | 0.723 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.18, *p* = 0.323, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.60 | 23 | = 0.761 | 0.14 [-0.30, 0.55] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | -0.59 | 23 | = 0.761 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -0.82 | 23 | = 0.718 | -0.20 [-0.59, 0.26] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -2.16 | 23 | = 0.310 | -0.36 [-0.88, 0.00] | small | n.s. |
| 1 to 4 vs Cardinality4 | -1.05 | 23 | = 0.718 | -0.29 [-0.64, 0.21] | small | n.s. |
| 2 to 4 vs 3 to 4 | -1.09 | 23 | = 0.718 | -0.28 [-0.65, 0.20] | small | n.s. |
| 2 to 4 vs 5 to 4 | -1.41 | 23 | = 0.643 | -0.35 [-0.72, 0.14] | small | n.s. |
| 2 to 4 vs 6 to 4 | -2.39 | 23 | = 0.310 | -0.53 [-0.93, -0.04] | medium | n.s. |
| 2 to 4 vs Cardinality4 | -1.68 | 23 | = 0.537 | -0.45 [-0.78, 0.09] | small | n.s. |
| 3 to 4 vs 5 to 4 | -0.26 | 23 | = 0.796 | -0.06 [-0.48, 0.37] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | -0.90 | 23 | = 0.718 | -0.22 [-0.61, 0.24] | small | n.s. |
| 3 to 4 vs Cardinality4 | -0.51 | 23 | = 0.767 | -0.14 [-0.53, 0.32] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.80 | 23 | = 0.718 | -0.16 [-0.59, 0.26] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | -0.30 | 23 | = 0.796 | -0.08 [-0.48, 0.36] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 0.31 | 23 | = 0.796 | 0.08 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 599.82, BIC = 626.55
- **2 to 4 vs 1 to 4**: *β* = -0.62, *SE* = 0.498, *z* = -1.249, *p* = 0.212
- **3 to 4 vs 1 to 4**: *β* = -0.46, *SE* = 0.499, *z* = -0.926, *p* = 0.354
- **5 to 4 vs 1 to 4**: *β* = -0.19, *SE* = 0.495, *z* = -0.388, *p* = 0.698
- **6 to 4 vs 1 to 4**: *β* = -0.91, *SE* = 0.496, *z* = -1.825, *p* = 0.068
- **Cardinality4 vs 1 to 4**: *β* = -0.35, *SE* = 0.495, *z* = -0.706, *p* = 0.480
- **SNR**: *β* = -0.39, *SE* = 0.121, *z* = -3.219, *p* = 0.001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 0.62 | 0.50 | 1.25 | 0.212 | 0.955 | n.s. |
| 1 to 4 - 3 to 4 | 0.46 | 0.50 | 0.93 | 0.354 | 0.992 | n.s. |
| 1 to 4 - 5 to 4 | 0.19 | 0.49 | 0.39 | 0.698 | 0.997 | n.s. |
| 1 to 4 - 6 to 4 | 0.90 | 0.50 | 1.83 | 0.068 | 0.652 | n.s. |
| 1 to 4 - Cardinality4 | 0.35 | 0.50 | 0.71 | 0.480 | 0.995 | n.s. |
| 2 to 4 - 3 to 4 | -0.16 | 0.49 | -0.32 | 0.746 | 0.997 | n.s. |
| 2 to 4 - 5 to 4 | -0.43 | 0.50 | -0.86 | 0.390 | 0.992 | n.s. |
| 2 to 4 - 6 to 4 | 0.28 | 0.50 | 0.57 | 0.569 | 0.997 | n.s. |
| 2 to 4 - Cardinality4 | -0.27 | 0.50 | -0.55 | 0.582 | 0.997 | n.s. |
| 3 to 4 - 5 to 4 | -0.27 | 0.50 | -0.54 | 0.590 | 0.997 | n.s. |
| 3 to 4 - 6 to 4 | 0.44 | 0.50 | 0.89 | 0.372 | 0.992 | n.s. |
| 3 to 4 - Cardinality4 | -0.11 | 0.50 | -0.23 | 0.820 | 0.997 | n.s. |
| 5 to 4 - 6 to 4 | 0.71 | 0.50 | 1.43 | 0.151 | 0.900 | n.s. |
| 5 to 4 - Cardinality4 | 0.16 | 0.50 | 0.32 | 0.751 | 0.997 | n.s. |
| 6 to 4 - Cardinality4 | -0.55 | 0.49 | -1.12 | 0.262 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.746, η²_G = 0.015
- Greenhouse-Geisser corrected: *p* = 0.685 (ε = 0.702)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.74 | 23 | = 0.950 | 0.22 [-0.27, 0.58] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.44 | 23 | = 0.950 | 0.13 [-0.33, 0.51] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | 0.35 | 23 | = 0.950 | 0.10 [-0.35, 0.50] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 1.57 | 23 | = 0.950 | 0.42 [-0.11, 0.75] | small | n.s. |
| 1 to 4 vs Cardinality4 | 0.60 | 23 | = 0.950 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | -0.46 | 23 | = 0.950 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.32 | 23 | = 0.950 | -0.08 [-0.49, 0.36] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 1.01 | 23 | = 0.950 | 0.20 [-0.22, 0.63] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | -0.31 | 23 | = 0.950 | -0.09 [-0.49, 0.36] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -0.01 | 23 | = 0.992 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 1.54 | 23 | = 0.950 | 0.31 [-0.12, 0.75] | small | n.s. |
| 3 to 4 vs Cardinality4 | 0.04 | 23 | = 0.992 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 1.11 | 23 | = 0.950 | 0.25 [-0.20, 0.65] | small | n.s. |
| 5 to 4 vs Cardinality4 | 0.03 | 23 | = 0.992 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | -1.08 | 23 | = 0.950 | -0.30 [-0.65, 0.21] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1182.94, BIC = 1209.66
- **2 to 4 vs 1 to 4**: *β* = 1.38, *SE* = 3.261, *z* = 0.422, *p* = 0.673
- **3 to 4 vs 1 to 4**: *β* = -3.73, *SE* = 3.278, *z* = -1.137, *p* = 0.256
- **5 to 4 vs 1 to 4**: *β* = 2.72, *SE* = 3.263, *z* = 0.834, *p* = 0.404
- **6 to 4 vs 1 to 4**: *β* = 1.18, *SE* = 3.260, *z* = 0.363, *p* = 0.717
- **Cardinality4 vs 1 to 4**: *β* = 0.22, *SE* = 3.261, *z* = 0.068, *p* = 0.945
- **SNR**: *β* = 0.28, *SE* = 0.348, *z* = 0.803, *p* = 0.422

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -1.38 | 3.26 | -0.42 | 0.673 | 1.000 | n.s. |
| 1 to 4 - 3 to 4 | 3.73 | 3.28 | 1.14 | 0.256 | 0.961 | n.s. |
| 1 to 4 - 5 to 4 | -2.72 | 3.26 | -0.83 | 0.404 | 0.994 | n.s. |
| 1 to 4 - 6 to 4 | -1.18 | 3.26 | -0.36 | 0.717 | 1.000 | n.s. |
| 1 to 4 - Cardinality4 | -0.22 | 3.26 | -0.07 | 0.945 | 1.000 | n.s. |
| 2 to 4 - 3 to 4 | 5.10 | 3.27 | 1.56 | 0.119 | 0.830 | n.s. |
| 2 to 4 - 5 to 4 | -1.35 | 3.27 | -0.41 | 0.680 | 1.000 | n.s. |
| 2 to 4 - 6 to 4 | 0.19 | 3.26 | 0.06 | 0.953 | 1.000 | n.s. |
| 2 to 4 - Cardinality4 | 1.15 | 3.26 | 0.35 | 0.724 | 1.000 | n.s. |
| 3 to 4 - 5 to 4 | -6.45 | 3.29 | -1.96 | 0.050 | 0.539 | n.s. |
| 3 to 4 - 6 to 4 | -4.91 | 3.28 | -1.50 | 0.134 | 0.846 | n.s. |
| 3 to 4 - Cardinality4 | -3.95 | 3.27 | -1.21 | 0.227 | 0.955 | n.s. |
| 5 to 4 - 6 to 4 | 1.54 | 3.26 | 0.47 | 0.637 | 1.000 | n.s. |
| 5 to 4 - Cardinality4 | 2.50 | 3.27 | 0.77 | 0.444 | 0.995 | n.s. |
| 6 to 4 - Cardinality4 | 0.96 | 3.26 | 0.29 | 0.768 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.96, *p* = 0.446, η²_G = 0.013
- Greenhouse-Geisser corrected: *p* = 0.418 (ε = 0.610)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.35 | 23 | = 0.896 | -0.08 [-0.49, 0.35] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 1.05 | 23 | = 0.815 | 0.21 [-0.21, 0.64] | small | n.s. |
| 1 to 4 vs 5 to 4 | -1.04 | 23 | = 0.815 | -0.15 [-0.64, 0.22] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -0.45 | 23 | = 0.896 | -0.06 [-0.51, 0.33] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | -0.07 | 23 | = 0.965 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 1.87 | 23 | = 0.552 | 0.30 [-0.05, 0.82] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.37 | 23 | = 0.896 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 0.04 | 23 | = 0.965 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | 0.29 | 23 | = 0.896 | 0.06 [-0.36, 0.48] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | -2.15 | 23 | = 0.552 | -0.35 [-0.88, 0.00] | small | n.s. |
| 3 to 4 vs 6 to 4 | -1.37 | 23 | = 0.815 | -0.26 [-0.71, 0.15] | small | n.s. |
| 3 to 4 vs Cardinality4 | -1.00 | 23 | = 0.815 | -0.22 [-0.63, 0.22] | small | n.s. |
| 5 to 4 vs 6 to 4 | 0.73 | 23 | = 0.882 | 0.08 [-0.27, 0.57] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | 0.80 | 23 | = 0.882 | 0.14 [-0.26, 0.59] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 0.39 | 23 | = 0.896 | 0.05 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 609.84, BIC = 636.57
- **2 to 4 vs 1 to 4**: *β* = 0.05, *SE* = 0.457, *z* = 0.113, *p* = 0.910
- **3 to 4 vs 1 to 4**: *β* = 0.53, *SE* = 0.459, *z* = 1.160, *p* = 0.246
- **5 to 4 vs 1 to 4**: *β* = 0.58, *SE* = 0.457, *z* = 1.278, *p* = 0.201
- **6 to 4 vs 1 to 4**: *β* = 0.87, *SE* = 0.457, *z* = 1.900, *p* = 0.057
- **Cardinality4 vs 1 to 4**: *β* = 0.71, *SE* = 0.457, *z* = 1.545, *p* = 0.122
- **SNR**: *β* = -0.42, *SE* = 0.048, *z* = -8.681, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.05 | 0.46 | -0.11 | 0.910 | 0.998 | n.s. |
| 1 to 4 - 3 to 4 | -0.53 | 0.46 | -1.16 | 0.246 | 0.939 | n.s. |
| 1 to 4 - 5 to 4 | -0.58 | 0.46 | -1.28 | 0.201 | 0.915 | n.s. |
| 1 to 4 - 6 to 4 | -0.87 | 0.46 | -1.90 | 0.057 | 0.588 | n.s. |
| 1 to 4 - Cardinality4 | -0.71 | 0.46 | -1.55 | 0.122 | 0.817 | n.s. |
| 2 to 4 - 3 to 4 | -0.48 | 0.46 | -1.05 | 0.294 | 0.939 | n.s. |
| 2 to 4 - 5 to 4 | -0.53 | 0.46 | -1.16 | 0.244 | 0.939 | n.s. |
| 2 to 4 - 6 to 4 | -0.82 | 0.46 | -1.79 | 0.074 | 0.659 | n.s. |
| 2 to 4 - Cardinality4 | -0.65 | 0.46 | -1.43 | 0.152 | 0.862 | n.s. |
| 3 to 4 - 5 to 4 | -0.05 | 0.46 | -0.11 | 0.911 | 0.998 | n.s. |
| 3 to 4 - 6 to 4 | -0.34 | 0.46 | -0.73 | 0.465 | 0.988 | n.s. |
| 3 to 4 - Cardinality4 | -0.17 | 0.46 | -0.38 | 0.706 | 0.998 | n.s. |
| 5 to 4 - 6 to 4 | -0.28 | 0.46 | -0.62 | 0.535 | 0.990 | n.s. |
| 5 to 4 - Cardinality4 | -0.12 | 0.46 | -0.27 | 0.790 | 0.998 | n.s. |
| 6 to 4 - Cardinality4 | 0.16 | 0.46 | 0.35 | 0.723 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.98, *p* = 0.432, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.22 | 23 | = 0.932 | -0.04 [-0.47, 0.38] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | -1.99 | 23 | = 0.596 | -0.35 [-0.85, 0.03] | small | n.s. |
| 1 to 4 vs 5 to 4 | -1.01 | 23 | = 0.604 | -0.15 [-0.63, 0.22] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -1.62 | 23 | = 0.596 | -0.31 [-0.76, 0.10] | small | n.s. |
| 1 to 4 vs Cardinality4 | -1.68 | 23 | = 0.596 | -0.25 [-0.78, 0.09] | small | n.s. |
| 2 to 4 vs 3 to 4 | -1.20 | 23 | = 0.604 | -0.30 [-0.67, 0.18] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.47 | 23 | = 0.879 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -1.06 | 23 | = 0.604 | -0.27 [-0.64, 0.21] | small | n.s. |
| 2 to 4 vs Cardinality4 | -1.15 | 23 | = 0.604 | -0.21 [-0.66, 0.19] | small | n.s. |
| 3 to 4 vs 5 to 4 | 1.12 | 23 | = 0.604 | 0.20 [-0.20, 0.66] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 0.09 | 23 | = 0.932 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| 3 to 4 vs Cardinality4 | 0.22 | 23 | = 0.932 | 0.05 [-0.38, 0.47] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.84 | 23 | = 0.683 | -0.17 [-0.60, 0.25] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | -0.58 | 23 | = 0.847 | -0.12 [-0.54, 0.30] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 0.16 | 23 | = 0.932 | 0.03 [-0.39, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1083.04, BIC = 1109.77
- **2 to 4 vs 1 to 4**: *β* = 4.34, *SE* = 2.500, *z* = 1.737, *p* = 0.082
- **3 to 4 vs 1 to 4**: *β* = 4.36, *SE* = 2.501, *z* = 1.744, *p* = 0.081
- **5 to 4 vs 1 to 4**: *β* = 7.77, *SE* = 2.495, *z* = 3.114, *p* = 0.002
- **6 to 4 vs 1 to 4**: *β* = 9.22, *SE* = 2.497, *z* = 3.693, *p* < .001
- **Cardinality4 vs 1 to 4**: *β* = 8.99, *SE* = 2.494, *z* = 3.603, *p* < .001
- **SNR**: *β* = 0.60, *SE* = 0.559, *z* = 1.067, *p* = 0.286

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -4.34 | 2.50 | -1.74 | 0.082 | 0.492 | n.s. |
| 1 to 4 - 3 to 4 | -4.36 | 2.50 | -1.74 | 0.081 | 0.492 | n.s. |
| 1 to 4 - 5 to 4 | -7.77 | 2.50 | -3.11 | 0.002 | 0.024 | * |
| 1 to 4 - 6 to 4 | -9.22 | 2.50 | -3.69 | < .001 | 0.003 | ** |
| 1 to 4 - Cardinality4 | -8.99 | 2.49 | -3.60 | < .001 | 0.004 | ** |
| 2 to 4 - 3 to 4 | -0.02 | 2.49 | -0.01 | 0.994 | 0.994 | n.s. |
| 2 to 4 - 5 to 4 | -3.43 | 2.50 | -1.37 | 0.171 | 0.676 | n.s. |
| 2 to 4 - 6 to 4 | -4.88 | 2.51 | -1.94 | 0.052 | 0.473 | n.s. |
| 2 to 4 - Cardinality4 | -4.64 | 2.50 | -1.86 | 0.063 | 0.480 | n.s. |
| 3 to 4 - 5 to 4 | -3.41 | 2.51 | -1.36 | 0.174 | 0.676 | n.s. |
| 3 to 4 - 6 to 4 | -4.86 | 2.51 | -1.93 | 0.053 | 0.473 | n.s. |
| 3 to 4 - Cardinality4 | -4.63 | 2.50 | -1.85 | 0.065 | 0.480 | n.s. |
| 5 to 4 - 6 to 4 | -1.45 | 2.49 | -0.58 | 0.561 | 0.963 | n.s. |
| 5 to 4 - Cardinality4 | -1.22 | 2.49 | -0.49 | 0.625 | 0.963 | n.s. |
| 6 to 4 - Cardinality4 | 0.23 | 2.50 | 0.09 | 0.926 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.03, *p* = 0.002, η²_G = 0.085
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -2.16 | 23 | = 0.121 | -0.39 [-0.88, 0.00] | small | n.s. |
| 1 to 4 vs 3 to 4 | -2.05 | 23 | = 0.121 | -0.38 [-0.86, 0.02] | small | n.s. |
| 1 to 4 vs 5 to 4 | -3.20 | 23 | = 0.020 | -0.69 [-1.12, -0.19] | medium | * |
| 1 to 4 vs 6 to 4 | -3.96 | 23 | = 0.006 | -0.90 [-1.30, -0.32] | large | ** |
| 1 to 4 vs Cardinality4 | -3.83 | 23 | = 0.006 | -0.83 [-1.26, -0.30] | large | ** |
| 2 to 4 vs 3 to 4 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -1.43 | 23 | = 0.228 | -0.32 [-0.72, 0.14] | small | n.s. |
| 2 to 4 vs 6 to 4 | -2.27 | 23 | = 0.121 | -0.49 [-0.91, -0.02] | small | n.s. |
| 2 to 4 vs Cardinality4 | -2.01 | 23 | = 0.121 | -0.44 [-0.85, 0.03] | small | n.s. |
| 3 to 4 vs 5 to 4 | -1.50 | 23 | = 0.220 | -0.31 [-0.74, 0.13] | small | n.s. |
| 3 to 4 vs 6 to 4 | -1.77 | 23 | = 0.168 | -0.48 [-0.80, 0.07] | small | n.s. |
| 3 to 4 vs Cardinality4 | -1.60 | 23 | = 0.206 | -0.43 [-0.76, 0.11] | small | n.s. |
| 5 to 4 vs 6 to 4 | -0.54 | 23 | = 0.739 | -0.13 [-0.53, 0.31] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | -0.35 | 23 | = 0.838 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 0.12 | 23 | = 0.971 | 0.03 [-0.40, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 598.31, BIC = 625.03
- **2 to 4 vs 1 to 4**: *β* = 0.30, *SE* = 0.451, *z* = 0.663, *p* = 0.508
- **3 to 4 vs 1 to 4**: *β* = 0.52, *SE* = 0.452, *z* = 1.153, *p* = 0.249
- **5 to 4 vs 1 to 4**: *β* = -0.15, *SE* = 0.450, *z* = -0.327, *p* = 0.744
- **6 to 4 vs 1 to 4**: *β* = 0.34, *SE* = 0.451, *z* = 0.762, *p* = 0.446
- **Cardinality4 vs 1 to 4**: *β* = -0.06, *SE* = 0.450, *z* = -0.135, *p* = 0.893
- **SNR**: *β* = 0.38, *SE* = 0.105, *z* = 3.665, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.30 | 0.45 | -0.66 | 0.508 | 0.993 | n.s. |
| 1 to 4 - 3 to 4 | -0.52 | 0.45 | -1.15 | 0.249 | 0.976 | n.s. |
| 1 to 4 - 5 to 4 | 0.15 | 0.45 | 0.33 | 0.744 | 0.997 | n.s. |
| 1 to 4 - 6 to 4 | -0.34 | 0.45 | -0.76 | 0.446 | 0.993 | n.s. |
| 1 to 4 - Cardinality4 | 0.06 | 0.45 | 0.13 | 0.893 | 0.997 | n.s. |
| 2 to 4 - 3 to 4 | -0.22 | 0.45 | -0.49 | 0.623 | 0.997 | n.s. |
| 2 to 4 - 5 to 4 | 0.45 | 0.45 | 0.99 | 0.324 | 0.986 | n.s. |
| 2 to 4 - 6 to 4 | -0.04 | 0.45 | -0.10 | 0.922 | 0.997 | n.s. |
| 2 to 4 - Cardinality4 | 0.36 | 0.45 | 0.80 | 0.426 | 0.993 | n.s. |
| 3 to 4 - 5 to 4 | 0.67 | 0.45 | 1.48 | 0.140 | 0.896 | n.s. |
| 3 to 4 - 6 to 4 | 0.18 | 0.45 | 0.39 | 0.696 | 0.997 | n.s. |
| 3 to 4 - Cardinality4 | 0.58 | 0.45 | 1.29 | 0.198 | 0.955 | n.s. |
| 5 to 4 - 6 to 4 | -0.49 | 0.45 | -1.09 | 0.276 | 0.979 | n.s. |
| 5 to 4 - Cardinality4 | -0.09 | 0.45 | -0.19 | 0.848 | 0.997 | n.s. |
| 6 to 4 - Cardinality4 | 0.40 | 0.45 | 0.90 | 0.370 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.804, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.49 | 23 | = 0.940 | -0.08 [-0.52, 0.32] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | -0.72 | 23 | = 0.940 | -0.17 [-0.57, 0.28] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | 0.24 | 23 | = 0.962 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -0.89 | 23 | = 0.940 | -0.17 [-0.61, 0.24] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | 0.14 | 23 | = 0.962 | 0.02 [-0.39, 0.45] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | -0.41 | 23 | = 0.940 | -0.10 [-0.51, 0.34] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | 0.67 | 23 | = 0.940 | 0.13 [-0.29, 0.56] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.47 | 23 | = 0.940 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | 0.47 | 23 | = 0.940 | 0.11 [-0.33, 0.52] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | 1.04 | 23 | = 0.940 | 0.22 [-0.21, 0.64] | small | n.s. |
| 3 to 4 vs 6 to 4 | -0.05 | 23 | = 0.962 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 3 to 4 vs Cardinality4 | 0.76 | 23 | = 0.940 | 0.20 [-0.27, 0.58] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -1.27 | 23 | = 0.940 | -0.21 [-0.69, 0.17] | small | n.s. |
| 5 to 4 vs Cardinality4 | -0.10 | 23 | = 0.962 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 6 to 4 vs Cardinality4 | 1.00 | 23 | = 0.940 | 0.19 [-0.22, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1430.11, BIC = 1456.84
- **2 to 4 vs 1 to 4**: *β* = -3.32, *SE* = 9.168, *z* = -0.362, *p* = 0.718
- **3 to 4 vs 1 to 4**: *β* = 1.96, *SE* = 9.165, *z* = 0.214, *p* = 0.831
- **5 to 4 vs 1 to 4**: *β* = 4.87, *SE* = 9.159, *z* = 0.532, *p* = 0.595
- **6 to 4 vs 1 to 4**: *β* = -5.99, *SE* = 9.160, *z* = -0.654, *p* = 0.513
- **Cardinality4 vs 1 to 4**: *β* = -14.72, *SE* = 9.201, *z* = -1.600, *p* = 0.110
- **SNR**: *β* = -0.69, *SE* = 0.854, *z* = -0.809, *p* = 0.419

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 3.32 | 9.17 | 0.36 | 0.718 | 0.994 | n.s. |
| 1 to 4 - 3 to 4 | -1.96 | 9.16 | -0.21 | 0.831 | 0.994 | n.s. |
| 1 to 4 - 5 to 4 | -4.87 | 9.16 | -0.53 | 0.595 | 0.993 | n.s. |
| 1 to 4 - 6 to 4 | 5.99 | 9.16 | 0.65 | 0.513 | 0.993 | n.s. |
| 1 to 4 - Cardinality4 | 14.73 | 9.20 | 1.60 | 0.110 | 0.779 | n.s. |
| 2 to 4 - 3 to 4 | -5.28 | 9.16 | -0.58 | 0.564 | 0.993 | n.s. |
| 2 to 4 - 5 to 4 | -8.19 | 9.18 | -0.89 | 0.372 | 0.985 | n.s. |
| 2 to 4 - 6 to 4 | 2.68 | 9.18 | 0.29 | 0.771 | 0.994 | n.s. |
| 2 to 4 - Cardinality4 | 11.41 | 9.25 | 1.23 | 0.218 | 0.947 | n.s. |
| 3 to 4 - 5 to 4 | -2.91 | 9.17 | -0.32 | 0.751 | 0.994 | n.s. |
| 3 to 4 - 6 to 4 | 7.96 | 9.17 | 0.87 | 0.386 | 0.985 | n.s. |
| 3 to 4 - Cardinality4 | 16.69 | 9.24 | 1.81 | 0.071 | 0.644 | n.s. |
| 5 to 4 - 6 to 4 | 10.87 | 9.16 | 1.19 | 0.235 | 0.948 | n.s. |
| 5 to 4 - Cardinality4 | 19.60 | 9.19 | 2.13 | 0.033 | 0.395 | n.s. |
| 6 to 4 - Cardinality4 | 8.73 | 9.18 | 0.95 | 0.342 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.02, *p* = 0.407, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.51 | 23 | = 0.784 | 0.11 [-0.32, 0.53] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | -0.16 | 23 | = 0.873 | -0.05 [-0.46, 0.39] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -0.49 | 23 | = 0.784 | -0.16 [-0.52, 0.32] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.70 | 23 | = 0.784 | 0.18 [-0.28, 0.57] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | 1.47 | 23 | = 0.771 | 0.46 [-0.13, 0.73] | small | n.s. |
| 2 to 4 vs 3 to 4 | -0.53 | 23 | = 0.784 | -0.15 [-0.53, 0.32] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.84 | 23 | = 0.784 | -0.26 [-0.60, 0.25] | small | n.s. |
| 2 to 4 vs 6 to 4 | 0.26 | 23 | = 0.855 | 0.06 [-0.37, 0.48] | negligible | n.s. |
| 2 to 4 vs Cardinality4 | 1.02 | 23 | = 0.784 | 0.32 [-0.22, 0.63] | small | n.s. |
| 3 to 4 vs 5 to 4 | -0.41 | 23 | = 0.791 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 0.67 | 23 | = 0.784 | 0.21 [-0.29, 0.56] | small | n.s. |
| 3 to 4 vs Cardinality4 | 1.60 | 23 | = 0.771 | 0.46 [-0.11, 0.76] | small | n.s. |
| 5 to 4 vs 6 to 4 | 1.07 | 23 | = 0.784 | 0.32 [-0.21, 0.64] | small | n.s. |
| 5 to 4 vs Cardinality4 | 2.21 | 23 | = 0.565 | 0.59 [0.01, 0.89] | medium | n.s. |
| 6 to 4 vs Cardinality4 | 1.20 | 23 | = 0.784 | 0.25 [-0.18, 0.67] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 724.55, BIC = 751.28
- **2 to 4 vs 1 to 4**: *β* = 0.49, *SE* = 0.661, *z* = 0.736, *p* = 0.461
- **3 to 4 vs 1 to 4**: *β* = -0.72, *SE* = 0.661, *z* = -1.095, *p* = 0.274
- **5 to 4 vs 1 to 4**: *β* = -0.07, *SE* = 0.660, *z* = -0.098, *p* = 0.922
- **6 to 4 vs 1 to 4**: *β* = -0.45, *SE* = 0.660, *z* = -0.675, *p* = 0.500
- **Cardinality4 vs 1 to 4**: *β* = -2.83, *SE* = 0.664, *z* = -4.263, *p* < .001
- **SNR**: *β* = 0.20, *SE* = 0.071, *z* = 2.771, *p* = 0.006

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.49 | 0.66 | -0.74 | 0.461 | 0.956 | n.s. |
| 1 to 4 - 3 to 4 | 0.72 | 0.66 | 1.09 | 0.274 | 0.923 | n.s. |
| 1 to 4 - 5 to 4 | 0.06 | 0.66 | 0.10 | 0.922 | 0.956 | n.s. |
| 1 to 4 - 6 to 4 | 0.45 | 0.66 | 0.67 | 0.500 | 0.956 | n.s. |
| 1 to 4 - Cardinality4 | 2.83 | 0.66 | 4.26 | < .001 | < .001 | *** |
| 2 to 4 - 3 to 4 | 1.21 | 0.66 | 1.83 | 0.067 | 0.499 | n.s. |
| 2 to 4 - 5 to 4 | 0.55 | 0.66 | 0.83 | 0.405 | 0.956 | n.s. |
| 2 to 4 - 6 to 4 | 0.93 | 0.66 | 1.41 | 0.159 | 0.790 | n.s. |
| 2 to 4 - Cardinality4 | 3.32 | 0.67 | 4.96 | < .001 | < .001 | *** |
| 3 to 4 - 5 to 4 | -0.66 | 0.66 | -1.00 | 0.319 | 0.932 | n.s. |
| 3 to 4 - 6 to 4 | -0.28 | 0.66 | -0.42 | 0.675 | 0.956 | n.s. |
| 3 to 4 - Cardinality4 | 2.11 | 0.67 | 3.15 | 0.002 | 0.018 | * |
| 5 to 4 - 6 to 4 | 0.38 | 0.66 | 0.58 | 0.564 | 0.956 | n.s. |
| 5 to 4 - Cardinality4 | 2.77 | 0.66 | 4.17 | < .001 | < .001 | *** |
| 6 to 4 - Cardinality4 | 2.39 | 0.66 | 3.60 | < .001 | 0.004 | ** |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.70, *p* < .001, η²_G = 0.076
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.85 | 23 | = 0.527 | -0.14 [-0.60, 0.25] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 1.02 | 23 | = 0.524 | 0.16 [-0.22, 0.63] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | 0.21 | 23 | = 0.841 | 0.03 [-0.38, 0.46] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 1.01 | 23 | = 0.524 | 0.14 [-0.22, 0.63] | negligible | n.s. |
| 1 to 4 vs Cardinality4 | 4.59 | 23 | < .001 | 0.81 [0.43, 1.44] | large | *** |
| 2 to 4 vs 3 to 4 | 1.63 | 23 | = 0.293 | 0.27 [-0.10, 0.77] | small | n.s. |
| 2 to 4 vs 5 to 4 | 0.96 | 23 | = 0.524 | 0.15 [-0.23, 0.62] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 1.31 | 23 | = 0.435 | 0.25 [-0.16, 0.70] | small | n.s. |
| 2 to 4 vs Cardinality4 | 4.36 | 23 | < .001 | 0.81 [0.39, 1.39] | large | *** |
| 3 to 4 vs 5 to 4 | -0.82 | 23 | = 0.527 | -0.13 [-0.59, 0.26] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | -0.20 | 23 | = 0.841 | -0.04 [-0.46, 0.38] | negligible | n.s. |
| 3 to 4 vs Cardinality4 | 2.73 | 23 | = 0.036 | 0.58 [0.10, 1.01] | medium | * |
| 5 to 4 vs 6 to 4 | 0.62 | 23 | = 0.627 | 0.10 [-0.30, 0.55] | negligible | n.s. |
| 5 to 4 vs Cardinality4 | 4.53 | 23 | < .001 | 0.73 [0.42, 1.43] | medium | *** |
| 6 to 4 vs Cardinality4 | 4.37 | 23 | < .001 | 0.67 [0.39, 1.39] | medium | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 1 to 4 showed smaller latency than 5 to 4 (*d* = -0.69)
  - 1 to 4 showed smaller latency than 6 to 4 (*d* = -0.90)
  - 1 to 4 showed smaller latency than Cardinality4 (*d* = -0.83)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 4 showed greater amplitude than Cardinality4 (*d* = 0.81)
  - 2 to 4 showed greater amplitude than Cardinality4 (*d* = 0.81)
  - 3 to 4 showed greater amplitude than Cardinality4 (*d* = 0.58)
  - 5 to 4 showed greater amplitude than Cardinality4 (*d* = 0.73)
  - 6 to 4 showed greater amplitude than Cardinality4 (*d* = 0.67)

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
