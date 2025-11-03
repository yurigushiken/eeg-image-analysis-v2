# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:46:32

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
| 1 to 2 | 10 | 105.20 ms | 9.05 | 2.86 | [96.00, 116.00] |
| 3 to 2 | 13 | 104.92 ms | 7.86 | 2.18 | [96.00, 116.00] |
| 4 to 2 | 14 | 108.86 ms | 5.48 | 1.46 | [96.00, 116.00] |
| 5 to 2 | 17 | 105.88 ms | 8.14 | 1.97 | [96.00, 116.00] |
| Cardinality2 | 14 | 108.57 ms | 7.17 | 1.91 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 10 | -2.15 µV | 1.75 | 0.55 | [-6.41, -0.72] |
| 3 to 2 | 13 | -2.77 µV | 1.64 | 0.46 | [-5.65, -0.61] |
| 4 to 2 | 14 | -2.26 µV | 1.30 | 0.35 | [-4.94, -0.24] |
| 5 to 2 | 17 | -3.32 µV | 1.65 | 0.40 | [-6.23, -0.53] |
| Cardinality2 | 14 | -2.22 µV | 1.33 | 0.36 | [-5.94, -0.68] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | 168.00 ms | 15.18 | 3.31 | [144.00, 196.00] |
| 3 to 2 | 24 | 176.17 ms | 23.07 | 4.71 | [144.00, 212.00] |
| 4 to 2 | 24 | 174.83 ms | 15.22 | 3.11 | [148.00, 212.00] |
| 5 to 2 | 24 | 174.17 ms | 17.61 | 3.60 | [148.00, 212.00] |
| Cardinality2 | 22 | 175.09 ms | 21.91 | 4.67 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 21 | -5.63 µV | 2.29 | 0.50 | [-9.95, -2.19] |
| 3 to 2 | 24 | -5.79 µV | 2.54 | 0.52 | [-10.33, -1.35] |
| 4 to 2 | 24 | -6.14 µV | 3.05 | 0.62 | [-11.92, -1.89] |
| 5 to 2 | 24 | -6.56 µV | 3.01 | 0.61 | [-11.17, -1.41] |
| Cardinality2 | 22 | -5.73 µV | 2.50 | 0.53 | [-10.50, -1.57] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 112.92 ms | 7.69 | 2.13 | [104.00, 120.00] |
| 3 to 2 | 11 | 110.55 ms | 6.52 | 1.96 | [104.00, 120.00] |
| 4 to 2 | 14 | 116.29 ms | 5.08 | 1.36 | [108.00, 120.00] |
| 5 to 2 | 16 | 113.00 ms | 7.23 | 1.81 | [104.00, 120.00] |
| Cardinality2 | 13 | 112.62 ms | 7.09 | 1.97 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 13 | 1.69 µV | 1.27 | 0.35 | [0.48, 5.23] |
| 3 to 2 | 11 | 2.49 µV | 1.65 | 0.50 | [0.51, 5.61] |
| 4 to 2 | 14 | 2.57 µV | 1.03 | 0.28 | [1.28, 4.31] |
| 5 to 2 | 16 | 3.13 µV | 1.56 | 0.39 | [0.75, 6.20] |
| Cardinality2 | 13 | 2.97 µV | 1.81 | 0.50 | [1.11, 7.57] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 483.06 ms | 44.17 | 10.71 | [420.00, 540.00] |
| 3 to 2 | 18 | 486.00 ms | 33.92 | 8.00 | [432.00, 540.00] |
| 4 to 2 | 19 | 474.74 ms | 38.07 | 8.73 | [420.00, 536.00] |
| 5 to 2 | 19 | 476.63 ms | 37.03 | 8.49 | [420.00, 540.00] |
| Cardinality2 | 11 | 465.82 ms | 33.53 | 10.11 | [420.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 17 | 5.58 µV | 3.12 | 0.76 | [1.70, 11.52] |
| 3 to 2 | 18 | 6.50 µV | 4.11 | 0.97 | [2.10, 17.81] |
| 4 to 2 | 19 | 5.47 µV | 3.07 | 0.70 | [1.15, 11.62] |
| 5 to 2 | 19 | 5.67 µV | 2.78 | 0.64 | [2.00, 13.53] |
| Cardinality2 | 11 | 4.56 µV | 2.39 | 0.72 | [1.28, 10.57] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 473.65, BIC = 491.40
- **3 to 2 vs 1 to 2**: *β* = -0.24, *SE* = 2.757, *z* = -0.087, *p* = 0.930
- **4 to 2 vs 1 to 2**: *β* = 3.50, *SE* = 2.705, *z* = 1.294, *p* = 0.196
- **5 to 2 vs 1 to 2**: *β* = 0.14, *SE* = 2.625, *z* = 0.054, *p* = 0.957
- **Cardinality2 vs 1 to 2**: *β* = 3.34, *SE* = 2.694, *z* = 1.242, *p* = 0.214
- **SNR**: *β* = 0.20, *SE* = 0.694, *z* = 0.284, *p* = 0.777

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | 0.24 | 2.76 | 0.09 | 0.930 | 1.000 | n.s. |
| 1 to 2 - 4 to 2 | -3.50 | 2.71 | -1.29 | 0.196 | 0.800 | n.s. |
| 1 to 2 - 5 to 2 | -0.14 | 2.62 | -0.05 | 0.957 | 1.000 | n.s. |
| 1 to 2 - Cardinality2 | -3.34 | 2.69 | -1.24 | 0.214 | 0.800 | n.s. |
| 3 to 2 - 4 to 2 | -3.74 | 2.57 | -1.45 | 0.146 | 0.793 | n.s. |
| 3 to 2 - 5 to 2 | -0.38 | 2.37 | -0.16 | 0.872 | 1.000 | n.s. |
| 3 to 2 - Cardinality2 | -3.59 | 2.58 | -1.39 | 0.164 | 0.800 | n.s. |
| 4 to 2 - 5 to 2 | 3.36 | 2.41 | 1.39 | 0.164 | 0.800 | n.s. |
| 4 to 2 - Cardinality2 | 0.16 | 2.44 | 0.06 | 0.949 | 1.000 | n.s. |
| 5 to 2 - Cardinality2 | -3.20 | 2.43 | -1.32 | 0.188 | 0.800 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.69, *p* = 0.613, η²_G = 0.133
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -1.41 | 3 | = 0.742 | -0.50 [-1.42, 0.52] | medium | n.s. |
| 1 to 2 vs 4 to 2 | -1.00 | 3 | = 0.782 | -0.52 [-1.31, 0.60] | medium | n.s. |
| 1 to 2 vs 5 to 2 | 0.35 | 3 | = 1.000 | 0.30 [-0.55, 1.16] | small | n.s. |
| 1 to 2 vs Cardinality2 | -0.58 | 3 | = 1.000 | -0.52 [-1.05, 0.64] | medium | n.s. |
| 3 to 2 vs 4 to 2 | 0.00 | 3 | = 1.000 | 0.00 [-1.51, 0.19] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.26 | 3 | = 0.742 | 0.84 [-0.79, 0.56] | large | n.s. |
| 3 to 2 vs Cardinality2 | 0.00 | 3 | = 1.000 | 0.00 [-0.78, 0.65] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.73 | 3 | = 0.742 | 0.89 [-0.35, 1.03] | large | n.s. |
| 4 to 2 vs Cardinality2 | 0.00 | 3 | = 1.000 | 0.00 [-0.77, 0.77] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -1.44 | 3 | = 0.742 | -0.89 [-1.31, 0.15] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 221.34, BIC = 239.10
- **3 to 2 vs 1 to 2**: *β* = -0.18, *SE* = 0.446, *z* = -0.413, *p* = 0.679
- **4 to 2 vs 1 to 2**: *β* = -0.46, *SE* = 0.438, *z* = -1.039, *p* = 0.299
- **5 to 2 vs 1 to 2**: *β* = -0.77, *SE* = 0.426, *z* = -1.797, *p* = 0.072
- **Cardinality2 vs 1 to 2**: *β* = -0.38, *SE* = 0.435, *z* = -0.868, *p* = 0.385
- **SNR**: *β* = -0.82, *SE* = 0.109, *z* = -7.476, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | 0.18 | 0.45 | 0.41 | 0.679 | 0.954 | n.s. |
| 1 to 2 - 4 to 2 | 0.46 | 0.44 | 1.04 | 0.299 | 0.941 | n.s. |
| 1 to 2 - 5 to 2 | 0.77 | 0.43 | 1.80 | 0.072 | 0.528 | n.s. |
| 1 to 2 - Cardinality2 | 0.38 | 0.44 | 0.87 | 0.385 | 0.946 | n.s. |
| 3 to 2 - 4 to 2 | 0.27 | 0.42 | 0.65 | 0.515 | 0.946 | n.s. |
| 3 to 2 - 5 to 2 | 0.58 | 0.38 | 1.51 | 0.131 | 0.716 | n.s. |
| 3 to 2 - Cardinality2 | 0.19 | 0.42 | 0.46 | 0.642 | 0.954 | n.s. |
| 4 to 2 - 5 to 2 | 0.31 | 0.39 | 0.80 | 0.426 | 0.946 | n.s. |
| 4 to 2 - Cardinality2 | -0.08 | 0.40 | -0.19 | 0.846 | 0.954 | n.s. |
| 5 to 2 - Cardinality2 | -0.39 | 0.40 | -0.98 | 0.327 | 0.941 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.31, *p* = 0.320, η²_G = 0.297
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | 1.42 | 3 | = 0.749 | 0.98 [-0.30, 1.80] | large | n.s. |
| 1 to 2 vs 4 to 2 | 0.02 | 3 | = 0.984 | 0.01 [-1.07, 0.79] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | 3.78 | 3 | = 0.162 | 1.59 [-0.41, 1.35] | large | n.s. |
| 1 to 2 vs Cardinality2 | 0.09 | 3 | = 0.984 | 0.08 [-0.78, 0.89] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -0.94 | 3 | = 0.749 | -0.91 [-1.12, 0.46] | large | n.s. |
| 3 to 2 vs 5 to 2 | 0.81 | 3 | = 0.749 | 0.69 [-0.17, 1.27] | medium | n.s. |
| 3 to 2 vs Cardinality2 | -0.72 | 3 | = 0.749 | -0.56 [-1.19, 0.31] | medium | n.s. |
| 4 to 2 vs 5 to 2 | 4.46 | 3 | = 0.162 | 1.52 [0.20, 1.87] | large | n.s. |
| 4 to 2 vs Cardinality2 | 0.09 | 3 | = 0.984 | 0.07 [-0.87, 0.67] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -1.14 | 3 | = 0.749 | -1.06 [-1.27, 0.17] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 997.81, BIC = 1019.77
- **3 to 2 vs 1 to 2**: *β* = 6.79, *SE* = 4.600, *z* = 1.476, *p* = 0.140
- **4 to 2 vs 1 to 2**: *β* = 5.46, *SE* = 4.601, *z* = 1.187, *p* = 0.235
- **5 to 2 vs 1 to 2**: *β* = 4.79, *SE* = 4.608, *z* = 1.039, *p* = 0.299
- **Cardinality2 vs 1 to 2**: *β* = 5.44, *SE* = 4.777, *z* = 1.140, *p* = 0.254
- **SNR**: *β* = 0.00, *SE* = 0.671, *z* = 0.006, *p* = 0.995

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -6.79 | 4.60 | -1.48 | 0.140 | 0.778 | n.s. |
| 1 to 2 - 4 to 2 | -5.46 | 4.60 | -1.19 | 0.235 | 0.911 | n.s. |
| 1 to 2 - 5 to 2 | -4.79 | 4.61 | -1.04 | 0.299 | 0.917 | n.s. |
| 1 to 2 - Cardinality2 | -5.44 | 4.78 | -1.14 | 0.254 | 0.911 | n.s. |
| 3 to 2 - 4 to 2 | 1.33 | 4.44 | 0.30 | 0.764 | 0.999 | n.s. |
| 3 to 2 - 5 to 2 | 2.00 | 4.41 | 0.45 | 0.650 | 0.998 | n.s. |
| 3 to 2 - Cardinality2 | 1.35 | 4.64 | 0.29 | 0.772 | 0.999 | n.s. |
| 4 to 2 - 5 to 2 | 0.67 | 4.45 | 0.15 | 0.880 | 0.999 | n.s. |
| 4 to 2 - Cardinality2 | 0.02 | 4.55 | 0.00 | 0.997 | 0.999 | n.s. |
| 5 to 2 - Cardinality2 | -0.65 | 4.67 | -0.14 | 0.889 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.83, *p* = 0.510, η²_G = 0.023
- Greenhouse-Geisser corrected: *p* = 0.481 (ε = 0.735)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -0.79 | 18 | = 0.729 | -0.21 [-0.61, 0.30] | small | n.s. |
| 1 to 2 vs 4 to 2 | -1.38 | 18 | = 0.729 | -0.38 [-0.83, 0.11] | small | n.s. |
| 1 to 2 vs 5 to 2 | -0.83 | 18 | = 0.729 | -0.27 [-0.58, 0.33] | small | n.s. |
| 1 to 2 vs Cardinality2 | -1.86 | 18 | = 0.729 | -0.44 [-0.93, 0.08] | small | n.s. |
| 3 to 2 vs 4 to 2 | -0.46 | 18 | = 0.811 | -0.11 [-0.36, 0.48] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | -0.11 | 18 | = 0.912 | -0.04 [-0.34, 0.51] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | -0.81 | 18 | = 0.729 | -0.21 [-0.38, 0.51] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.35 | 18 | = 0.811 | 0.08 [-0.39, 0.46] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | -0.50 | 18 | = 0.811 | -0.13 [-0.48, 0.41] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -1.09 | 18 | = 0.729 | -0.20 [-0.42, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 477.13, BIC = 499.09
- **3 to 2 vs 1 to 2**: *β* = -0.09, *SE* = 0.444, *z* = -0.206, *p* = 0.837
- **4 to 2 vs 1 to 2**: *β* = -0.78, *SE* = 0.445, *z* = -1.749, *p* = 0.080
- **5 to 2 vs 1 to 2**: *β* = -0.78, *SE* = 0.445, *z* = -1.752, *p* = 0.080
- **Cardinality2 vs 1 to 2**: *β* = -0.55, *SE* = 0.464, *z* = -1.182, *p* = 0.237
- **SNR**: *β* = -0.44, *SE* = 0.070, *z* = -6.258, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | 0.09 | 0.44 | 0.21 | 0.837 | 0.975 | n.s. |
| 1 to 2 - 4 to 2 | 0.78 | 0.44 | 1.75 | 0.080 | 0.564 | n.s. |
| 1 to 2 - 5 to 2 | 0.78 | 0.45 | 1.75 | 0.080 | 0.564 | n.s. |
| 1 to 2 - Cardinality2 | 0.55 | 0.46 | 1.18 | 0.237 | 0.803 | n.s. |
| 3 to 2 - 4 to 2 | 0.69 | 0.43 | 1.60 | 0.110 | 0.591 | n.s. |
| 3 to 2 - 5 to 2 | 0.69 | 0.43 | 1.62 | 0.106 | 0.591 | n.s. |
| 3 to 2 - Cardinality2 | 0.46 | 0.45 | 1.01 | 0.312 | 0.846 | n.s. |
| 4 to 2 - 5 to 2 | 0.00 | 0.43 | 0.01 | 0.995 | 0.995 | n.s. |
| 4 to 2 - Cardinality2 | -0.23 | 0.44 | -0.52 | 0.603 | 0.975 | n.s. |
| 5 to 2 - Cardinality2 | -0.23 | 0.46 | -0.51 | 0.610 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.01, *p* = 0.102, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | 0.53 | 18 | = 0.670 | 0.09 [-0.28, 0.63] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | 1.33 | 18 | = 0.414 | 0.29 [-0.13, 0.80] | small | n.s. |
| 1 to 2 vs 5 to 2 | 1.88 | 18 | = 0.337 | 0.37 [-0.01, 0.94] | small | n.s. |
| 1 to 2 vs Cardinality2 | -0.87 | 18 | = 0.496 | -0.15 [-0.69, 0.29] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | 0.96 | 18 | = 0.496 | 0.19 [-0.28, 0.57] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.31 | 18 | = 0.414 | 0.27 [-0.12, 0.75] | small | n.s. |
| 3 to 2 vs Cardinality2 | -1.05 | 18 | = 0.496 | -0.21 [-0.55, 0.34] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.39 | 18 | = 0.702 | 0.07 [-0.24, 0.61] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | -1.73 | 18 | = 0.337 | -0.40 [-0.65, 0.25] | small | n.s. |
| 5 to 2 vs Cardinality2 | -2.21 | 18 | = 0.337 | -0.47 [-0.81, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 436.91, BIC = 454.54
- **3 to 2 vs 1 to 2**: *β* = -1.76, *SE* = 1.898, *z* = -0.927, *p* = 0.354
- **4 to 2 vs 1 to 2**: *β* = 2.37, *SE* = 1.724, *z* = 1.374, *p* = 0.169
- **5 to 2 vs 1 to 2**: *β* = -2.88, *SE* = 1.835, *z* = -1.568, *p* = 0.117
- **Cardinality2 vs 1 to 2**: *β* = -1.81, *SE* = 1.794, *z* = -1.008, *p* = 0.314
- **SNR**: *β* = 0.39, *SE* = 0.495, *z* = 0.779, *p* = 0.436

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | 1.76 | 1.90 | 0.93 | 0.354 | 0.848 | n.s. |
| 1 to 2 - 4 to 2 | -2.37 | 1.72 | -1.37 | 0.169 | 0.672 | n.s. |
| 1 to 2 - 5 to 2 | 2.88 | 1.83 | 1.57 | 0.117 | 0.581 | n.s. |
| 1 to 2 - Cardinality2 | 1.81 | 1.79 | 1.01 | 0.314 | 0.848 | n.s. |
| 3 to 2 - 4 to 2 | -4.13 | 1.83 | -2.25 | 0.024 | 0.178 | n.s. |
| 3 to 2 - 5 to 2 | 1.12 | 1.92 | 0.58 | 0.560 | 0.899 | n.s. |
| 3 to 2 - Cardinality2 | 0.05 | 1.93 | 0.02 | 0.980 | 0.980 | n.s. |
| 4 to 2 - 5 to 2 | 5.25 | 1.74 | 3.01 | 0.003 | 0.026 | * |
| 4 to 2 - Cardinality2 | 4.18 | 1.75 | 2.39 | 0.017 | 0.143 | n.s. |
| 5 to 2 - Cardinality2 | -1.07 | 1.72 | -0.62 | 0.534 | 0.899 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.79, *p* = 0.551, η²_G = 0.073
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -0.34 | 4 | = 0.941 | -0.11 [-1.06, 0.80] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -0.39 | 4 | = 0.941 | -0.22 [-1.01, 0.37] | small | n.s. |
| 1 to 2 vs 5 to 2 | 1.37 | 4 | = 0.745 | 0.40 [0.15, 1.93] | small | n.s. |
| 1 to 2 vs Cardinality2 | -0.25 | 4 | = 0.941 | -0.12 [-0.64, 0.79] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -0.21 | 4 | = 0.941 | -0.13 [-1.32, 0.32] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.20 | 4 | = 0.745 | 0.57 [-0.66, 1.03] | medium | n.s. |
| 3 to 2 vs Cardinality2 | 0.00 | 4 | = 1.000 | 0.00 [-0.67, 1.22] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.63 | 4 | = 0.745 | 0.69 [0.06, 1.63] | medium | n.s. |
| 4 to 2 vs Cardinality2 | 0.41 | 4 | = 0.941 | 0.15 [-0.21, 1.33] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -2.24 | 4 | = 0.745 | -0.63 [-0.84, 0.51] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 212.83, BIC = 230.47
- **3 to 2 vs 1 to 2**: *β* = 0.50, *SE* = 0.415, *z* = 1.205, *p* = 0.228
- **4 to 2 vs 1 to 2**: *β* = 0.57, *SE* = 0.385, *z* = 1.472, *p* = 0.141
- **5 to 2 vs 1 to 2**: *β* = 0.66, *SE* = 0.390, *z* = 1.681, *p* = 0.093
- **Cardinality2 vs 1 to 2**: *β* = 0.89, *SE* = 0.395, *z* = 2.257, *p* = 0.024
- **SNR**: *β* = 0.75, *SE* = 0.101, *z* = 7.451, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -0.50 | 0.41 | -1.21 | 0.228 | 0.837 | n.s. |
| 1 to 2 - 4 to 2 | -0.57 | 0.39 | -1.47 | 0.141 | 0.703 | n.s. |
| 1 to 2 - 5 to 2 | -0.66 | 0.39 | -1.68 | 0.093 | 0.584 | n.s. |
| 1 to 2 - Cardinality2 | -0.89 | 0.40 | -2.26 | 0.024 | 0.216 | n.s. |
| 3 to 2 - 4 to 2 | -0.07 | 0.40 | -0.17 | 0.868 | 0.973 | n.s. |
| 3 to 2 - 5 to 2 | -0.16 | 0.40 | -0.39 | 0.699 | 0.973 | n.s. |
| 3 to 2 - Cardinality2 | -0.39 | 0.41 | -0.95 | 0.344 | 0.920 | n.s. |
| 4 to 2 - 5 to 2 | -0.09 | 0.37 | -0.24 | 0.813 | 0.973 | n.s. |
| 4 to 2 - Cardinality2 | -0.33 | 0.39 | -0.84 | 0.399 | 0.922 | n.s. |
| 5 to 2 - Cardinality2 | -0.24 | 0.38 | -0.63 | 0.531 | 0.952 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.246, η²_G = 0.235
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -1.70 | 4 | = 0.413 | -0.69 [-1.55, 0.43] | medium | n.s. |
| 1 to 2 vs 4 to 2 | -1.00 | 4 | = 0.470 | -0.87 [-1.12, 0.28] | large | n.s. |
| 1 to 2 vs 5 to 2 | -2.63 | 4 | = 0.413 | -1.38 [-1.72, -0.04] | large | n.s. |
| 1 to 2 vs Cardinality2 | -1.80 | 4 | = 0.413 | -1.19 [-1.60, 0.03] | large | n.s. |
| 3 to 2 vs 4 to 2 | 0.09 | 4 | = 0.934 | 0.07 [-0.64, 0.90] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | -2.17 | 4 | = 0.413 | -0.62 [-1.93, 0.07] | medium | n.s. |
| 3 to 2 vs Cardinality2 | -1.02 | 4 | = 0.470 | -0.67 [-0.95, 0.90] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -1.21 | 4 | = 0.470 | -0.80 [-1.43, 0.06] | medium | n.s. |
| 4 to 2 vs Cardinality2 | -1.22 | 4 | = 0.470 | -0.78 [-0.81, 0.62] | medium | n.s. |
| 5 to 2 vs Cardinality2 | -0.23 | 4 | = 0.921 | -0.17 [-0.71, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 853.12, BIC = 872.57
- **3 to 2 vs 1 to 2**: *β* = 2.93, *SE* = 10.975, *z* = 0.267, *p* = 0.789
- **4 to 2 vs 1 to 2**: *β* = -7.36, *SE* = 10.823, *z* = -0.680, *p* = 0.496
- **5 to 2 vs 1 to 2**: *β* = -8.18, *SE* = 10.965, *z* = -0.746, *p* = 0.456
- **Cardinality2 vs 1 to 2**: *β* = -13.47, *SE* = 12.851, *z* = -1.048, *p* = 0.295
- **SNR**: *β* = 1.38, *SE* = 1.564, *z* = 0.883, *p* = 0.377

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -2.93 | 10.97 | -0.27 | 0.789 | 0.980 | n.s. |
| 1 to 2 - 4 to 2 | 7.36 | 10.82 | 0.68 | 0.496 | 0.974 | n.s. |
| 1 to 2 - 5 to 2 | 8.18 | 10.96 | 0.75 | 0.456 | 0.974 | n.s. |
| 1 to 2 - Cardinality2 | 13.47 | 12.85 | 1.05 | 0.295 | 0.957 | n.s. |
| 3 to 2 - 4 to 2 | 10.29 | 10.56 | 0.97 | 0.330 | 0.957 | n.s. |
| 3 to 2 - 5 to 2 | 11.11 | 10.77 | 1.03 | 0.302 | 0.957 | n.s. |
| 3 to 2 - Cardinality2 | 16.40 | 12.60 | 1.30 | 0.193 | 0.883 | n.s. |
| 4 to 2 - 5 to 2 | 0.82 | 10.76 | 0.08 | 0.939 | 0.980 | n.s. |
| 4 to 2 - Cardinality2 | 6.11 | 12.44 | 0.49 | 0.623 | 0.980 | n.s. |
| 5 to 2 - Cardinality2 | 5.29 | 12.97 | 0.41 | 0.683 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.45, *p* = 0.771, η²_G = 0.046
- Greenhouse-Geisser corrected: *p* = 0.649 (ε = 0.504)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -1.11 | 6 | = 0.895 | -0.53 [-0.65, 0.51] | medium | n.s. |
| 1 to 2 vs 4 to 2 | -0.57 | 6 | = 0.895 | -0.35 [-0.55, 0.56] | small | n.s. |
| 1 to 2 vs 5 to 2 | -0.57 | 6 | = 0.895 | -0.38 [-0.50, 0.61] | small | n.s. |
| 1 to 2 vs Cardinality2 | -0.21 | 6 | = 0.935 | -0.09 [-0.65, 0.89] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | 0.38 | 6 | = 0.895 | 0.14 [-0.26, 0.79] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 0.43 | 6 | = 0.895 | 0.18 [-0.29, 0.76] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | 1.42 | 6 | = 0.895 | 0.48 [-0.19, 1.36] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.03 | 6 | = 0.974 | 0.01 [-0.43, 0.60] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | 1.04 | 6 | = 0.895 | 0.29 [-0.68, 0.75] | small | n.s. |
| 5 to 2 vs Cardinality2 | 0.56 | 6 | = 0.895 | 0.32 [-0.50, 0.95] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 371.56, BIC = 391.01
- **3 to 2 vs 1 to 2**: *β* = 1.17, *SE* = 0.571, *z* = 2.041, *p* = 0.041
- **4 to 2 vs 1 to 2**: *β* = 0.50, *SE* = 0.561, *z* = 0.896, *p* = 0.370
- **5 to 2 vs 1 to 2**: *β* = -0.46, *SE* = 0.575, *z* = -0.795, *p* = 0.426
- **Cardinality2 vs 1 to 2**: *β* = -0.33, *SE* = 0.672, *z* = -0.491, *p* = 0.624
- **SNR**: *β* = 0.60, *SE* = 0.094, *z* = 6.372, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -1.17 | 0.57 | -2.04 | 0.041 | 0.286 | n.s. |
| 1 to 2 - 4 to 2 | -0.50 | 0.56 | -0.90 | 0.370 | 0.843 | n.s. |
| 1 to 2 - 5 to 2 | 0.46 | 0.58 | 0.80 | 0.426 | 0.843 | n.s. |
| 1 to 2 - Cardinality2 | 0.33 | 0.67 | 0.49 | 0.624 | 0.858 | n.s. |
| 3 to 2 - 4 to 2 | 0.66 | 0.54 | 1.22 | 0.224 | 0.738 | n.s. |
| 3 to 2 - 5 to 2 | 1.62 | 0.56 | 2.89 | 0.004 | 0.038 | * |
| 3 to 2 - Cardinality2 | 1.50 | 0.66 | 2.28 | 0.023 | 0.186 | n.s. |
| 4 to 2 - 5 to 2 | 0.96 | 0.56 | 1.71 | 0.087 | 0.471 | n.s. |
| 4 to 2 - Cardinality2 | 0.83 | 0.65 | 1.28 | 0.200 | 0.738 | n.s. |
| 5 to 2 - Cardinality2 | -0.13 | 0.68 | -0.19 | 0.852 | 0.858 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.21, *p* = 0.004, η²_G = 0.174
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -4.56 | 6 | = 0.033 | -1.06 [-0.99, 0.20] | large | * |
| 1 to 2 vs 4 to 2 | -1.96 | 6 | = 0.162 | -0.55 [-0.76, 0.36] | medium | n.s. |
| 1 to 2 vs 5 to 2 | -1.03 | 6 | = 0.382 | -0.31 [-0.64, 0.47] | small | n.s. |
| 1 to 2 vs Cardinality2 | 0.61 | 6 | = 0.567 | 0.22 [-0.43, 1.16] | small | n.s. |
| 3 to 2 vs 4 to 2 | 2.18 | 6 | = 0.162 | 0.35 [-0.17, 0.89] | small | n.s. |
| 3 to 2 vs 5 to 2 | 3.01 | 6 | = 0.079 | 0.77 [-0.16, 0.90] | medium | n.s. |
| 3 to 2 vs Cardinality2 | 4.08 | 6 | = 0.033 | 1.26 [-0.12, 1.46] | large | * |
| 4 to 2 vs 5 to 2 | 1.53 | 6 | = 0.252 | 0.30 [-0.43, 0.60] | small | n.s. |
| 4 to 2 vs Cardinality2 | 2.01 | 6 | = 0.162 | 0.72 [-0.18, 1.37] | medium | n.s. |
| 5 to 2 vs Cardinality2 | 1.17 | 6 | = 0.359 | 0.52 [-0.19, 1.36] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - 1 to 2 showed smaller amplitude than 3 to 2 (*d* = -1.06)
  - 3 to 2 showed greater amplitude than Cardinality2 (*d* = 1.26)

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
