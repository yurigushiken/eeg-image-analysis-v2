# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:44:29

---

## 1. Analysis Overview

**Total Measurements:** 672
**Number of Subjects:** 24
**Number of Conditions:** 7

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
| Cardinality (no change) | 18 | 110.89 ms | 6.26 | 1.48 | [92.00, 116.00] |
| Decrease by 1 | 13 | 105.54 ms | 8.09 | 2.24 | [96.00, 116.00] |
| Decrease by 2 | 21 | 108.19 ms | 7.85 | 1.71 | [92.00, 116.00] |
| Decrease by 3 | 17 | 105.18 ms | 8.22 | 1.99 | [92.00, 116.00] |
| Increase by 1 | 17 | 102.82 ms | 8.57 | 2.08 | [92.00, 116.00] |
| Increase by 2 | 13 | 105.23 ms | 8.39 | 2.33 | [92.00, 116.00] |
| Increase by 3 | 13 | 103.38 ms | 6.90 | 1.91 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 18 | -1.77 µV | 1.24 | 0.29 | [-4.83, -0.25] |
| Decrease by 1 | 13 | -2.00 µV | 1.29 | 0.36 | [-5.36, -0.84] |
| Decrease by 2 | 21 | -1.64 µV | 1.06 | 0.23 | [-4.58, -0.40] |
| Decrease by 3 | 17 | -2.46 µV | 1.59 | 0.39 | [-6.67, -0.87] |
| Increase by 1 | 17 | -1.41 µV | 0.85 | 0.21 | [-3.28, -0.44] |
| Increase by 2 | 13 | -1.70 µV | 1.22 | 0.34 | [-4.17, -0.46] |
| Increase by 3 | 13 | -1.78 µV | 1.06 | 0.29 | [-3.87, -0.59] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | 176.17 ms | 17.41 | 3.63 | [144.00, 208.00] |
| Decrease by 1 | 24 | 178.00 ms | 15.83 | 3.23 | [144.00, 208.00] |
| Decrease by 2 | 24 | 177.50 ms | 14.82 | 3.02 | [144.00, 208.00] |
| Decrease by 3 | 24 | 177.67 ms | 14.59 | 2.98 | [156.00, 208.00] |
| Increase by 1 | 23 | 169.74 ms | 18.52 | 3.86 | [144.00, 208.00] |
| Increase by 2 | 24 | 168.50 ms | 19.46 | 3.97 | [144.00, 208.00] |
| Increase by 3 | 24 | 171.00 ms | 19.53 | 3.99 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 23 | -4.80 µV | 2.00 | 0.42 | [-9.57, -1.40] |
| Decrease by 1 | 24 | -4.85 µV | 2.02 | 0.41 | [-9.17, -1.44] |
| Decrease by 2 | 24 | -4.95 µV | 2.01 | 0.41 | [-9.37, -1.43] |
| Decrease by 3 | 24 | -5.07 µV | 1.98 | 0.40 | [-8.57, -1.48] |
| Increase by 1 | 23 | -5.10 µV | 2.17 | 0.45 | [-9.36, -1.04] |
| Increase by 2 | 24 | -5.39 µV | 2.36 | 0.48 | [-10.65, -0.86] |
| Increase by 3 | 24 | -6.05 µV | 2.46 | 0.50 | [-12.86, -1.94] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 111.38 ms | 6.50 | 1.80 | [100.00, 116.00] |
| Decrease by 1 | 13 | 108.00 ms | 9.24 | 2.56 | [92.00, 116.00] |
| Decrease by 2 | 16 | 111.25 ms | 6.23 | 1.56 | [96.00, 116.00] |
| Decrease by 3 | 18 | 110.89 ms | 5.95 | 1.40 | [100.00, 116.00] |
| Increase by 1 | 15 | 106.93 ms | 8.88 | 2.29 | [92.00, 116.00] |
| Increase by 2 | 13 | 106.77 ms | 8.06 | 2.24 | [92.00, 116.00] |
| Increase by 3 | 13 | 104.00 ms | 10.07 | 2.79 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 13 | 2.47 µV | 1.69 | 0.47 | [0.70, 5.73] |
| Decrease by 1 | 13 | 2.29 µV | 1.85 | 0.51 | [0.52, 5.89] |
| Decrease by 2 | 16 | 2.37 µV | 1.32 | 0.33 | [0.64, 5.51] |
| Decrease by 3 | 18 | 2.52 µV | 1.90 | 0.45 | [0.56, 8.21] |
| Increase by 1 | 15 | 1.77 µV | 1.28 | 0.33 | [0.26, 4.07] |
| Increase by 2 | 13 | 2.05 µV | 1.38 | 0.38 | [0.36, 4.70] |
| Increase by 3 | 13 | 2.25 µV | 1.46 | 0.40 | [0.51, 5.72] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 470.57 ms | 23.14 | 6.19 | [436.00, 516.00] |
| Decrease by 1 | 18 | 488.00 ms | 31.62 | 7.45 | [436.00, 528.00] |
| Decrease by 2 | 19 | 469.47 ms | 26.84 | 6.16 | [416.00, 532.00] |
| Decrease by 3 | 19 | 477.26 ms | 30.49 | 7.00 | [428.00, 524.00] |
| Increase by 1 | 16 | 484.25 ms | 40.17 | 10.04 | [416.00, 532.00] |
| Increase by 2 | 18 | 482.44 ms | 29.84 | 7.03 | [432.00, 532.00] |
| Increase by 3 | 20 | 473.60 ms | 41.33 | 9.24 | [416.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change) | 14 | 2.75 µV | 1.66 | 0.44 | [0.90, 5.95] |
| Decrease by 1 | 18 | 4.69 µV | 2.34 | 0.55 | [1.85, 8.87] |
| Decrease by 2 | 19 | 4.67 µV | 2.14 | 0.49 | [1.58, 8.53] |
| Decrease by 3 | 19 | 5.34 µV | 3.01 | 0.69 | [0.72, 12.38] |
| Increase by 1 | 16 | 4.11 µV | 2.54 | 0.64 | [0.78, 8.79] |
| Increase by 2 | 18 | 5.18 µV | 2.62 | 0.62 | [1.07, 9.72] |
| Increase by 3 | 20 | 4.37 µV | 2.48 | 0.55 | [1.27, 9.96] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 765.82, BIC = 793.01
- **Decrease by 1 vs Cardinality (no change)**: *β* = -4.52, *SE* = 2.208, *z* = -2.048, *p* = 0.041
- **Decrease by 2 vs Cardinality (no change)**: *β* = -1.57, *SE* = 1.946, *z* = -0.805, *p* = 0.421
- **Decrease by 3 vs Cardinality (no change)**: *β* = -5.26, *SE* = 2.072, *z* = -2.538, *p* = 0.011
- **Increase by 1 vs Cardinality (no change)**: *β* = -7.07, *SE* = 2.032, *z* = -3.477, *p* = 0.001
- **Increase by 2 vs Cardinality (no change)**: *β* = -4.43, *SE* = 2.205, *z* = -2.009, *p* = 0.045
- **Increase by 3 vs Cardinality (no change)**: *β* = -6.69, *SE* = 2.199, *z* = -3.041, *p* = 0.002
- **SNR**: *β* = 0.52, *SE* = 0.322, *z* = 1.610, *p* = 0.107

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 4.52 | 2.21 | 2.05 | 0.041 | 0.485 | n.s. |
| Cardinality (no change) - Decrease by 2 | 1.57 | 1.95 | 0.81 | 0.421 | 0.977 | n.s. |
| Cardinality (no change) - Decrease by 3 | 5.26 | 2.07 | 2.54 | 0.011 | 0.183 | n.s. |
| Cardinality (no change) - Increase by 1 | 7.07 | 2.03 | 3.48 | < .001 | 0.011 | * |
| Cardinality (no change) - Increase by 2 | 4.43 | 2.20 | 2.01 | 0.045 | 0.495 | n.s. |
| Cardinality (no change) - Increase by 3 | 6.69 | 2.20 | 3.04 | 0.002 | 0.046 | * |
| Decrease by 1 - Decrease by 2 | -2.95 | 2.13 | -1.38 | 0.166 | 0.906 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.74 | 2.26 | 0.33 | 0.745 | 0.994 | n.s. |
| Decrease by 1 - Increase by 1 | 2.54 | 2.24 | 1.13 | 0.257 | 0.951 | n.s. |
| Decrease by 1 - Increase by 2 | -0.09 | 2.39 | -0.04 | 0.969 | 0.994 | n.s. |
| Decrease by 1 - Increase by 3 | 2.17 | 2.39 | 0.91 | 0.365 | 0.977 | n.s. |
| Decrease by 2 - Decrease by 3 | 3.69 | 2.00 | 1.85 | 0.065 | 0.609 | n.s. |
| Decrease by 2 - Increase by 1 | 5.50 | 1.97 | 2.79 | 0.005 | 0.097 | n.s. |
| Decrease by 2 - Increase by 2 | 2.86 | 2.15 | 1.33 | 0.183 | 0.911 | n.s. |
| Decrease by 2 - Increase by 3 | 5.12 | 2.15 | 2.39 | 0.017 | 0.253 | n.s. |
| Decrease by 3 - Increase by 1 | 1.81 | 2.10 | 0.86 | 0.390 | 0.977 | n.s. |
| Decrease by 3 - Increase by 2 | -0.83 | 2.31 | -0.36 | 0.719 | 0.994 | n.s. |
| Decrease by 3 - Increase by 3 | 1.43 | 2.27 | 0.63 | 0.528 | 0.977 | n.s. |
| Increase by 1 - Increase by 2 | -2.64 | 2.24 | -1.17 | 0.240 | 0.951 | n.s. |
| Increase by 1 - Increase by 3 | -0.38 | 2.22 | -0.17 | 0.865 | 0.994 | n.s. |
| Increase by 2 - Increase by 3 | 2.26 | 2.38 | 0.95 | 0.343 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.27, *p* = 0.308, η²_G = 0.091
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 2.06 | 4 | = 0.604 | 0.76 [-0.12, 1.34] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 | 1.83 | 4 | = 0.604 | 0.55 [-0.41, 0.65] | medium | n.s. |
| Cardinality (no change) vs Decrease by 3 | 0.00 | 4 | = 1.000 | 0.00 [-0.24, 1.01] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.37 | 4 | = 0.604 | 0.60 [0.17, 1.44] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | 1.37 | 4 | = 0.604 | 0.44 [-0.26, 1.06] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 3.50 | 4 | = 0.523 | 1.02 [0.55, 2.37] | large | n.s. |
| Decrease by 1 vs Decrease by 2 | -0.34 | 4 | = 0.874 | -0.09 [-0.76, 0.45] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.18 | 4 | = 0.604 | -0.69 [-1.14, 0.35] | medium | n.s. |
| Decrease by 1 vs Increase by 1 | -1.00 | 4 | = 0.604 | -0.23 [-0.40, 1.08] | small | n.s. |
| Decrease by 1 vs Increase by 2 | -1.00 | 4 | = 0.604 | -0.19 [-1.32, 0.31] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 1.00 | 4 | = 0.604 | 0.11 [-0.07, 1.94] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.77 | 4 | = 0.672 | -0.51 [-0.28, 0.80] | medium | n.s. |
| Decrease by 2 vs Increase by 1 | -0.23 | 4 | = 0.915 | -0.10 [-0.09, 1.08] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | -0.53 | 4 | = 0.767 | -0.09 [-0.26, 1.06] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | 0.78 | 4 | = 0.672 | 0.20 [-0.15, 1.21] | small | n.s. |
| Decrease by 3 vs Increase by 1 | 1.21 | 4 | = 0.604 | 0.53 [-0.50, 0.66] | medium | n.s. |
| Decrease by 3 vs Increase by 2 | 0.72 | 4 | = 0.672 | 0.41 [-0.57, 0.99] | small | n.s. |
| Decrease by 3 vs Increase by 3 | 1.51 | 4 | = 0.604 | 0.90 [-0.44, 0.92] | large | n.s. |
| Increase by 1 vs Increase by 2 | 0.00 | 4 | = 1.000 | 0.00 [-1.10, 0.38] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.50 | 4 | = 0.604 | 0.39 [-0.24, 1.09] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.50 | 4 | = 0.604 | 0.30 [-0.21, 1.47] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.47, BIC = 307.66
- **Decrease by 1 vs Cardinality (no change)**: *β* = -0.05, *SE* = 0.245, *z* = -0.214, *p* = 0.831
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.01, *SE* = 0.215, *z* = -0.033, *p* = 0.974
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.47, *SE* = 0.230, *z* = -2.037, *p* = 0.042
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.30, *SE* = 0.225, *z* = 1.331, *p* = 0.183
- **Increase by 2 vs Cardinality (no change)**: *β* = 0.03, *SE* = 0.244, *z* = 0.131, *p* = 0.896
- **Increase by 3 vs Cardinality (no change)**: *β* = -0.04, *SE* = 0.244, *z* = -0.186, *p* = 0.853
- **SNR**: *β* = -0.27, *SE* = 0.037, *z* = -7.234, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 0.05 | 0.24 | 0.21 | 0.831 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.01 | 0.22 | 0.03 | 0.974 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.47 | 0.23 | 2.04 | 0.042 | 0.554 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.30 | 0.22 | -1.33 | 0.183 | 0.924 | n.s. |
| Cardinality (no change) - Increase by 2 | -0.03 | 0.24 | -0.13 | 0.896 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 3 | 0.05 | 0.24 | 0.19 | 0.853 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.05 | 0.24 | -0.19 | 0.849 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.42 | 0.25 | 1.65 | 0.099 | 0.812 | n.s. |
| Decrease by 1 - Increase by 1 | -0.35 | 0.25 | -1.41 | 0.158 | 0.924 | n.s. |
| Decrease by 1 - Increase by 2 | -0.08 | 0.26 | -0.32 | 0.750 | 1.000 | n.s. |
| Decrease by 1 - Increase by 3 | -0.01 | 0.27 | -0.03 | 0.979 | 1.000 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.46 | 0.22 | 2.08 | 0.038 | 0.537 | n.s. |
| Decrease by 2 - Increase by 1 | -0.31 | 0.22 | -1.40 | 0.162 | 0.924 | n.s. |
| Decrease by 2 - Increase by 2 | -0.04 | 0.24 | -0.16 | 0.870 | 1.000 | n.s. |
| Decrease by 2 - Increase by 3 | 0.04 | 0.24 | 0.16 | 0.873 | 1.000 | n.s. |
| Decrease by 3 - Increase by 1 | -0.77 | 0.23 | -3.28 | 0.001 | 0.021 | * |
| Decrease by 3 - Increase by 2 | -0.50 | 0.26 | -1.95 | 0.052 | 0.616 | n.s. |
| Decrease by 3 - Increase by 3 | -0.42 | 0.25 | -1.68 | 0.094 | 0.812 | n.s. |
| Increase by 1 - Increase by 2 | 0.27 | 0.25 | 1.07 | 0.283 | 0.974 | n.s. |
| Increase by 1 - Increase by 3 | 0.34 | 0.25 | 1.40 | 0.160 | 0.924 | n.s. |
| Increase by 2 - Increase by 3 | 0.08 | 0.26 | 0.29 | 0.770 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.92, *p* = 0.028, η²_G = 0.182
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -0.67 | 4 | = 0.665 | -0.32 [-0.65, 0.69] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | -3.57 | 4 | = 0.164 | -0.32 [-0.60, 0.47] | small | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.23 | 4 | = 0.429 | 0.39 [-0.21, 1.05] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | -4.33 | 4 | = 0.130 | -1.26 [-1.07, 0.10] | large | n.s. |
| Cardinality (no change) vs Increase by 2 | -1.24 | 4 | = 0.429 | -0.48 [-0.80, 0.48] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | -1.51 | 4 | = 0.429 | -0.81 [-0.88, 0.41] | large | n.s. |
| Decrease by 1 vs Decrease by 2 | 0.06 | 4 | = 0.956 | 0.03 [-0.63, 0.58] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.99 | 4 | = 0.307 | 0.60 [0.03, 1.71] | medium | n.s. |
| Decrease by 1 vs Increase by 1 | -1.77 | 4 | = 0.352 | -0.70 [-1.19, 0.31] | medium | n.s. |
| Decrease by 1 vs Increase by 2 | -0.46 | 4 | = 0.702 | -0.13 [-1.02, 0.54] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | -1.23 | 4 | = 0.429 | -0.37 [-1.24, 0.49] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | 2.16 | 4 | = 0.307 | 0.62 [0.27, 1.54] | medium | n.s. |
| Decrease by 2 vs Increase by 1 | -2.54 | 4 | = 0.307 | -0.81 [-0.67, 0.45] | large | n.s. |
| Decrease by 2 vs Increase by 2 | -0.49 | 4 | = 0.702 | -0.17 [-0.83, 0.45] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | -0.79 | 4 | = 0.619 | -0.44 [-0.66, 0.61] | small | n.s. |
| Decrease by 3 vs Increase by 1 | -4.94 | 4 | = 0.130 | -1.32 [-1.91, -0.41] | large | n.s. |
| Decrease by 3 vs Increase by 2 | -2.02 | 4 | = 0.307 | -0.74 [-2.26, -0.22] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | -2.40 | 4 | = 0.307 | -1.00 [-1.09, 0.31] | large | n.s. |
| Increase by 1 vs Increase by 2 | 1.29 | 4 | = 0.429 | 0.59 [-0.57, 0.87] | medium | n.s. |
| Increase by 1 vs Increase by 3 | 0.88 | 4 | = 0.601 | 0.36 [-0.25, 1.07] | small | n.s. |
| Increase by 2 vs Increase by 3 | -0.47 | 4 | = 0.702 | -0.25 [-0.95, 0.60] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1326.26, BIC = 1357.38
- **Decrease by 1 vs Cardinality (no change)**: *β* = 2.32, *SE* = 3.021, *z* = 0.768, *p* = 0.442
- **Decrease by 2 vs Cardinality (no change)**: *β* = 1.82, *SE* = 3.020, *z* = 0.601, *p* = 0.548
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.01, *SE* = 3.027, *z* = 0.665, *p* = 0.506
- **Increase by 1 vs Cardinality (no change)**: *β* = -4.42, *SE* = 3.156, *z* = -1.402, *p* = 0.161
- **Increase by 2 vs Cardinality (no change)**: *β* = -7.14, *SE* = 3.030, *z* = -2.358, *p* = 0.018
- **Increase by 3 vs Cardinality (no change)**: *β* = -4.67, *SE* = 3.022, *z* = -1.546, *p* = 0.122
- **SNR**: *β* = -0.10, *SE* = 0.222, *z* = -0.453, *p* = 0.651

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -2.32 | 3.02 | -0.77 | 0.442 | 0.985 | n.s. |
| Cardinality (no change) - Decrease by 2 | -1.82 | 3.02 | -0.60 | 0.548 | 0.985 | n.s. |
| Cardinality (no change) - Decrease by 3 | -2.01 | 3.03 | -0.67 | 0.506 | 0.985 | n.s. |
| Cardinality (no change) - Increase by 1 | 4.43 | 3.16 | 1.40 | 0.161 | 0.827 | n.s. |
| Cardinality (no change) - Increase by 2 | 7.14 | 3.03 | 2.36 | 0.018 | 0.284 | n.s. |
| Cardinality (no change) - Increase by 3 | 4.67 | 3.02 | 1.55 | 0.122 | 0.761 | n.s. |
| Decrease by 1 - Decrease by 2 | 0.50 | 2.97 | 0.17 | 0.865 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.31 | 2.97 | 0.10 | 0.918 | 1.000 | n.s. |
| Decrease by 1 - Increase by 1 | 6.75 | 3.06 | 2.21 | 0.027 | 0.341 | n.s. |
| Decrease by 1 - Increase by 2 | 9.46 | 2.97 | 3.18 | 0.001 | 0.030 | * |
| Decrease by 1 - Increase by 3 | 6.99 | 2.97 | 2.35 | 0.019 | 0.284 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.20 | 2.97 | -0.07 | 0.947 | 1.000 | n.s. |
| Decrease by 2 - Increase by 1 | 6.24 | 3.06 | 2.04 | 0.041 | 0.398 | n.s. |
| Decrease by 2 - Increase by 2 | 8.96 | 2.97 | 3.01 | 0.003 | 0.048 | * |
| Decrease by 2 - Increase by 3 | 6.49 | 2.97 | 2.18 | 0.029 | 0.341 | n.s. |
| Decrease by 3 - Increase by 1 | 6.44 | 3.05 | 2.11 | 0.035 | 0.368 | n.s. |
| Decrease by 3 - Increase by 2 | 9.16 | 2.97 | 3.08 | 0.002 | 0.040 | * |
| Decrease by 3 - Increase by 3 | 6.69 | 2.97 | 2.25 | 0.024 | 0.327 | n.s. |
| Increase by 1 - Increase by 2 | 2.72 | 3.04 | 0.89 | 0.372 | 0.985 | n.s. |
| Increase by 1 - Increase by 3 | 0.25 | 3.06 | 0.08 | 0.935 | 1.000 | n.s. |
| Increase by 2 - Increase by 3 | -2.47 | 2.97 | -0.83 | 0.406 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.96, *p* = 0.010, η²_G = 0.049
- Greenhouse-Geisser corrected: *p* = 0.036 (ε = 0.526)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.20 | 21 | = 0.381 | -0.15 [-0.69, 0.19] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.70 | 21 | = 0.643 | -0.12 [-0.58, 0.29] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.55 | 21 | = 0.723 | -0.13 [-0.55, 0.32] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.48 | 21 | = 0.270 | 0.27 [-0.14, 0.77] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.15 | 21 | = 0.182 | 0.41 [0.01, 0.93] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 1.55 | 21 | = 0.258 | 0.28 [-0.12, 0.77] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 0.30 | 21 | = 0.894 | 0.04 [-0.36, 0.48] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.11 | 21 | = 0.954 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 1.98 | 21 | = 0.182 | 0.42 [-0.03, 0.88] | small | n.s. |
| Decrease by 1 vs Increase by 2 | 2.66 | 21 | = 0.182 | 0.56 [0.13, 1.04] | medium | n.s. |
| Decrease by 1 vs Increase by 3 | 2.06 | 21 | = 0.182 | 0.43 [-0.00, 0.88] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.06 | 21 | = 0.954 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 1.57 | 21 | = 0.258 | 0.40 [-0.11, 0.78] | small | n.s. |
| Decrease by 2 vs Increase by 2 | 2.46 | 21 | = 0.182 | 0.55 [0.09, 1.00] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 1.73 | 21 | = 0.258 | 0.41 [-0.06, 0.81] | small | n.s. |
| Decrease by 3 vs Increase by 1 | 1.56 | 21 | = 0.258 | 0.41 [-0.11, 0.78] | small | n.s. |
| Decrease by 3 vs Increase by 2 | 2.33 | 21 | = 0.182 | 0.56 [0.06, 0.96] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | 1.99 | 21 | = 0.182 | 0.42 [-0.01, 0.87] | small | n.s. |
| Increase by 1 vs Increase by 2 | 1.03 | 21 | = 0.442 | 0.13 [-0.21, 0.67] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.07 | 21 | = 0.954 | 0.01 [-0.40, 0.46] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.17 | 21 | = 0.381 | -0.13 [-0.70, 0.16] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 560.29, BIC = 591.41
- **Decrease by 1 vs Cardinality (no change)**: *β* = 0.01, *SE* = 0.292, *z* = 0.043, *p* = 0.965
- **Decrease by 2 vs Cardinality (no change)**: *β* = -0.09, *SE* = 0.292, *z* = -0.311, *p* = 0.756
- **Decrease by 3 vs Cardinality (no change)**: *β* = -0.18, *SE* = 0.293, *z* = -0.605, *p* = 0.545
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.07, *SE* = 0.306, *z* = 0.218, *p* = 0.828
- **Increase by 2 vs Cardinality (no change)**: *β* = -0.49, *SE* = 0.293, *z* = -1.686, *p* = 0.092
- **Increase by 3 vs Cardinality (no change)**: *β* = -1.18, *SE* = 0.292, *z* = -4.031, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.022, *z* = -4.961, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -0.01 | 0.29 | -0.04 | 0.965 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 2 | 0.09 | 0.29 | 0.31 | 0.756 | 1.000 | n.s. |
| Cardinality (no change) - Decrease by 3 | 0.18 | 0.29 | 0.61 | 0.545 | 0.998 | n.s. |
| Cardinality (no change) - Increase by 1 | -0.07 | 0.31 | -0.22 | 0.828 | 1.000 | n.s. |
| Cardinality (no change) - Increase by 2 | 0.49 | 0.29 | 1.69 | 0.092 | 0.714 | n.s. |
| Cardinality (no change) - Increase by 3 | 1.18 | 0.29 | 4.03 | < .001 | 0.001 | ** |
| Decrease by 1 - Decrease by 2 | 0.10 | 0.29 | 0.36 | 0.719 | 1.000 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.19 | 0.29 | 0.66 | 0.509 | 0.998 | n.s. |
| Decrease by 1 - Increase by 1 | -0.05 | 0.30 | -0.18 | 0.855 | 1.000 | n.s. |
| Decrease by 1 - Increase by 2 | 0.51 | 0.29 | 1.76 | 0.078 | 0.679 | n.s. |
| Decrease by 1 - Increase by 3 | 1.19 | 0.29 | 4.15 | < .001 | < .001 | *** |
| Decrease by 2 - Decrease by 3 | 0.09 | 0.29 | 0.30 | 0.763 | 1.000 | n.s. |
| Decrease by 2 - Increase by 1 | -0.16 | 0.30 | -0.53 | 0.595 | 0.998 | n.s. |
| Decrease by 2 - Increase by 2 | 0.40 | 0.29 | 1.40 | 0.161 | 0.878 | n.s. |
| Decrease by 2 - Increase by 3 | 1.09 | 0.29 | 3.79 | < .001 | 0.003 | ** |
| Decrease by 3 - Increase by 1 | -0.24 | 0.29 | -0.83 | 0.408 | 0.995 | n.s. |
| Decrease by 3 - Increase by 2 | 0.32 | 0.29 | 1.10 | 0.270 | 0.969 | n.s. |
| Decrease by 3 - Increase by 3 | 1.00 | 0.29 | 3.48 | < .001 | 0.008 | ** |
| Increase by 1 - Increase by 2 | 0.56 | 0.29 | 1.90 | 0.057 | 0.585 | n.s. |
| Increase by 1 - Increase by 3 | 1.24 | 0.30 | 4.21 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.68 | 0.29 | 2.38 | 0.017 | 0.243 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.43, *p* < .001, η²_G = 0.043
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.42 | 21 | = 0.749 | 0.05 [-0.36, 0.50] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | 0.92 | 21 | = 0.538 | 0.14 [-0.31, 0.56] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 1.15 | 21 | = 0.503 | 0.18 [-0.21, 0.67] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.84 | 21 | = 0.185 | 0.22 [-0.07, 0.85] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.90 | 21 | = 0.045 | 0.33 [0.11, 1.04] | small | * |
| Cardinality (no change) vs Increase by 3 | 4.72 | 21 | = 0.002 | 0.64 [0.38, 1.41] | medium | ** |
| Decrease by 1 vs Decrease by 2 | 0.62 | 21 | = 0.668 | 0.09 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.84 | 21 | = 0.542 | 0.13 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 vs Increase by 1 | 1.29 | 21 | = 0.444 | 0.16 [-0.25, 0.62] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 2.20 | 21 | = 0.104 | 0.28 [-0.03, 0.85] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 4.29 | 21 | = 0.003 | 0.59 [0.31, 1.28] | medium | ** |
| Decrease by 2 vs Decrease by 3 | 0.32 | 21 | = 0.789 | 0.04 [-0.33, 0.52] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 0.48 | 21 | = 0.744 | 0.08 [-0.39, 0.48] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | 1.08 | 21 | = 0.514 | 0.20 [-0.19, 0.66] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 2.70 | 21 | = 0.056 | 0.52 [0.10, 1.01] | medium | n.s. |
| Decrease by 3 vs Increase by 1 | 0.22 | 21 | = 0.827 | 0.04 [-0.42, 0.44] | negligible | n.s. |
| Decrease by 3 vs Increase by 2 | 0.89 | 21 | = 0.538 | 0.16 [-0.25, 0.60] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 2.40 | 21 | = 0.090 | 0.48 [0.03, 0.92] | small | n.s. |
| Increase by 1 vs Increase by 2 | 0.93 | 21 | = 0.538 | 0.13 [-0.21, 0.67] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 2.93 | 21 | = 0.045 | 0.44 [0.18, 1.13] | small | * |
| Increase by 2 vs Increase by 3 | 2.32 | 21 | = 0.092 | 0.30 [0.01, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 679.28, BIC = 705.43
- **Decrease by 1 vs Cardinality (no change)**: *β* = -2.07, *SE* = 2.114, *z* = -0.977, *p* = 0.328
- **Decrease by 2 vs Cardinality (no change)**: *β* = 1.15, *SE* = 2.046, *z* = 0.562, *p* = 0.574
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.22, *SE* = 2.047, *z* = 1.083, *p* = 0.279
- **Increase by 1 vs Cardinality (no change)**: *β* = -1.85, *SE* = 2.133, *z* = -0.867, *p* = 0.386
- **Increase by 2 vs Cardinality (no change)**: *β* = -4.42, *SE* = 2.171, *z* = -2.035, *p* = 0.042
- **Increase by 3 vs Cardinality (no change)**: *β* = -6.49, *SE* = 2.158, *z* = -3.006, *p* = 0.003
- **SNR**: *β* = 0.12, *SE* = 0.229, *z* = 0.546, *p* = 0.585

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | 2.07 | 2.11 | 0.98 | 0.328 | 0.919 | n.s. |
| Cardinality (no change) - Decrease by 2 | -1.15 | 2.05 | -0.56 | 0.574 | 0.921 | n.s. |
| Cardinality (no change) - Decrease by 3 | -2.22 | 2.05 | -1.08 | 0.279 | 0.919 | n.s. |
| Cardinality (no change) - Increase by 1 | 1.85 | 2.13 | 0.87 | 0.386 | 0.919 | n.s. |
| Cardinality (no change) - Increase by 2 | 4.42 | 2.17 | 2.04 | 0.042 | 0.401 | n.s. |
| Cardinality (no change) - Increase by 3 | 6.49 | 2.16 | 3.01 | 0.003 | 0.047 | * |
| Decrease by 1 - Decrease by 2 | -3.22 | 2.03 | -1.58 | 0.113 | 0.733 | n.s. |
| Decrease by 1 - Decrease by 3 | -4.28 | 2.00 | -2.14 | 0.032 | 0.386 | n.s. |
| Decrease by 1 - Increase by 1 | -0.22 | 2.08 | -0.10 | 0.917 | 0.921 | n.s. |
| Decrease by 1 - Increase by 2 | 2.35 | 2.13 | 1.10 | 0.270 | 0.919 | n.s. |
| Decrease by 1 - Increase by 3 | 4.42 | 2.14 | 2.07 | 0.039 | 0.400 | n.s. |
| Decrease by 2 - Decrease by 3 | -1.07 | 1.88 | -0.57 | 0.571 | 0.921 | n.s. |
| Decrease by 2 - Increase by 1 | 3.00 | 1.96 | 1.53 | 0.126 | 0.740 | n.s. |
| Decrease by 2 - Increase by 2 | 5.57 | 2.04 | 2.73 | 0.006 | 0.103 | n.s. |
| Decrease by 2 - Increase by 3 | 7.64 | 2.03 | 3.76 | < .001 | 0.003 | ** |
| Decrease by 3 - Increase by 1 | 4.07 | 1.92 | 2.12 | 0.034 | 0.386 | n.s. |
| Decrease by 3 - Increase by 2 | 6.64 | 2.05 | 3.24 | 0.001 | 0.023 | * |
| Decrease by 3 - Increase by 3 | 8.70 | 2.03 | 4.28 | < .001 | < .001 | *** |
| Increase by 1 - Increase by 2 | 2.57 | 2.05 | 1.26 | 0.209 | 0.879 | n.s. |
| Increase by 1 - Increase by 3 | 4.64 | 2.03 | 2.29 | 0.022 | 0.302 | n.s. |
| Increase by 2 - Increase by 3 | 2.07 | 2.09 | 0.99 | 0.322 | 0.919 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.87, *p* = 0.114, η²_G = 0.111
- Greenhouse-Geisser corrected: *p* = 0.200 (ε = 0.312)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 1.55 | 6 | = 0.525 | 0.24 [-0.08, 1.40] | small | n.s. |
| Cardinality (no change) vs Decrease by 2 | 1.00 | 6 | = 0.598 | 0.12 [-0.76, 0.59] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | 0.00 | 6 | = 1.000 | 0.00 [-1.17, 0.32] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.00 | 6 | = 0.598 | 0.10 [-0.48, 0.97] | negligible | n.s. |
| Cardinality (no change) vs Increase by 2 | 2.25 | 6 | = 0.525 | 0.74 [0.01, 1.55] | medium | n.s. |
| Cardinality (no change) vs Increase by 3 | 1.38 | 6 | = 0.525 | 0.66 [-0.07, 1.42] | medium | n.s. |
| Decrease by 1 vs Decrease by 2 | -0.55 | 6 | = 0.792 | -0.12 [-1.19, 0.23] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.79 | 6 | = 0.686 | -0.29 [-1.52, 0.01] | small | n.s. |
| Decrease by 1 vs Increase by 1 | -0.55 | 6 | = 0.792 | -0.11 [-0.67, 0.76] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 1.35 | 6 | = 0.525 | 0.57 [-0.30, 1.10] | medium | n.s. |
| Decrease by 1 vs Increase by 3 | 0.97 | 6 | = 0.598 | 0.50 [-0.25, 1.27] | medium | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.42 | 6 | = 0.851 | -0.14 [-0.83, 0.35] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | 0.00 | 6 | = 1.000 | 0.00 [-0.29, 1.02] | negligible | n.s. |
| Decrease by 2 vs Increase by 2 | 2.29 | 6 | = 0.525 | 0.66 [0.21, 1.88] | medium | n.s. |
| Decrease by 2 vs Increase by 3 | 1.45 | 6 | = 0.525 | 0.58 [-0.02, 1.50] | medium | n.s. |
| Decrease by 3 vs Increase by 1 | 0.35 | 6 | = 0.858 | 0.12 [-0.18, 1.09] | negligible | n.s. |
| Decrease by 3 vs Increase by 2 | 1.92 | 6 | = 0.525 | 0.84 [0.10, 1.84] | large | n.s. |
| Decrease by 3 vs Increase by 3 | 1.62 | 6 | = 0.525 | 0.72 [0.08, 1.80] | medium | n.s. |
| Increase by 1 vs Increase by 2 | 1.87 | 6 | = 0.525 | 0.62 [0.06, 1.63] | medium | n.s. |
| Increase by 1 vs Increase by 3 | 1.15 | 6 | = 0.598 | 0.55 [-0.05, 1.35] | medium | n.s. |
| Increase by 2 vs Increase by 3 | 0.00 | 6 | = 1.000 | 0.00 [-0.50, 0.85] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 257.24, BIC = 283.39
- **Decrease by 1 vs Cardinality (no change)**: *β* = 0.13, *SE* = 0.255, *z* = 0.511, *p* = 0.610
- **Decrease by 2 vs Cardinality (no change)**: *β* = 0.50, *SE* = 0.247, *z* = 2.036, *p* = 0.042
- **Decrease by 3 vs Cardinality (no change)**: *β* = 0.77, *SE* = 0.247, *z* = 3.116, *p* = 0.002
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.10, *SE* = 0.258, *z* = 0.403, *p* = 0.687
- **Increase by 2 vs Cardinality (no change)**: *β* = 0.34, *SE* = 0.263, *z* = 1.276, *p* = 0.202
- **Increase by 3 vs Cardinality (no change)**: *β* = 0.43, *SE* = 0.261, *z* = 1.652, *p* = 0.098
- **SNR**: *β* = 0.29, *SE* = 0.029, *z* = 10.101, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -0.13 | 0.26 | -0.51 | 0.610 | 0.991 | n.s. |
| Cardinality (no change) - Decrease by 2 | -0.50 | 0.25 | -2.04 | 0.042 | 0.536 | n.s. |
| Cardinality (no change) - Decrease by 3 | -0.77 | 0.25 | -3.12 | 0.002 | 0.038 | * |
| Cardinality (no change) - Increase by 1 | -0.10 | 0.26 | -0.40 | 0.687 | 0.991 | n.s. |
| Cardinality (no change) - Increase by 2 | -0.34 | 0.26 | -1.28 | 0.202 | 0.916 | n.s. |
| Cardinality (no change) - Increase by 3 | -0.43 | 0.26 | -1.65 | 0.098 | 0.789 | n.s. |
| Decrease by 1 - Decrease by 2 | -0.37 | 0.25 | -1.52 | 0.128 | 0.854 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.64 | 0.24 | -2.64 | 0.008 | 0.147 | n.s. |
| Decrease by 1 - Increase by 1 | 0.03 | 0.25 | 0.10 | 0.916 | 0.991 | n.s. |
| Decrease by 1 - Increase by 2 | -0.20 | 0.26 | -0.80 | 0.425 | 0.979 | n.s. |
| Decrease by 1 - Increase by 3 | -0.30 | 0.26 | -1.17 | 0.243 | 0.938 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.26 | 0.23 | -1.17 | 0.243 | 0.938 | n.s. |
| Decrease by 2 - Increase by 1 | 0.40 | 0.24 | 1.68 | 0.092 | 0.787 | n.s. |
| Decrease by 2 - Increase by 2 | 0.17 | 0.25 | 0.68 | 0.496 | 0.984 | n.s. |
| Decrease by 2 - Increase by 3 | 0.07 | 0.25 | 0.29 | 0.771 | 0.991 | n.s. |
| Decrease by 3 - Increase by 1 | 0.66 | 0.23 | 2.85 | 0.004 | 0.083 | n.s. |
| Decrease by 3 - Increase by 2 | 0.43 | 0.25 | 1.75 | 0.080 | 0.758 | n.s. |
| Decrease by 3 - Increase by 3 | 0.34 | 0.25 | 1.37 | 0.172 | 0.914 | n.s. |
| Increase by 1 - Increase by 2 | -0.23 | 0.25 | -0.94 | 0.347 | 0.967 | n.s. |
| Increase by 1 - Increase by 3 | -0.33 | 0.24 | -1.34 | 0.180 | 0.914 | n.s. |
| Increase by 2 - Increase by 3 | -0.10 | 0.25 | -0.38 | 0.702 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.79, *p* = 0.128, η²_G = 0.095
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | 0.11 | 6 | = 0.916 | 0.05 [-0.66, 0.69] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 2 | 0.60 | 6 | = 0.669 | 0.13 [-0.75, 0.59] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.68 | 6 | = 0.669 | -0.30 [-0.94, 0.51] | small | n.s. |
| Cardinality (no change) vs Increase by 1 | 1.81 | 6 | = 0.361 | 0.72 [-0.19, 1.36] | medium | n.s. |
| Cardinality (no change) vs Increase by 2 | 1.00 | 6 | = 0.612 | 0.45 [-0.48, 0.88] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 0.60 | 6 | = 0.669 | 0.28 [-0.50, 0.85] | small | n.s. |
| Decrease by 1 vs Decrease by 2 | 0.16 | 6 | = 0.916 | 0.06 [-0.95, 0.41] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.14 | 6 | = 0.308 | -0.33 [-1.71, -0.11] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 2.34 | 6 | = 0.304 | 0.61 [-0.16, 1.40] | medium | n.s. |
| Decrease by 1 vs Increase by 2 | 2.03 | 6 | = 0.308 | 0.37 [-0.17, 1.27] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 0.95 | 6 | = 0.612 | 0.21 [-0.47, 0.99] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.03 | 6 | = 0.612 | -0.44 [-0.79, 0.38] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 1.69 | 6 | = 0.372 | 0.69 [-0.22, 1.11] | medium | n.s. |
| Decrease by 2 vs Increase by 2 | 0.98 | 6 | = 0.612 | 0.38 [-0.16, 1.28] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 0.38 | 6 | = 0.795 | 0.18 [-0.54, 0.81] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | 2.88 | 6 | = 0.207 | 0.95 [0.09, 1.48] | large | n.s. |
| Decrease by 3 vs Increase by 2 | 3.06 | 6 | = 0.207 | 0.71 [0.09, 1.82] | medium | n.s. |
| Decrease by 3 vs Increase by 3 | 2.84 | 6 | = 0.207 | 0.56 [0.11, 1.85] | medium | n.s. |
| Increase by 1 vs Increase by 2 | -0.69 | 6 | = 0.669 | -0.24 [-0.89, 0.47] | small | n.s. |
| Increase by 1 vs Increase by 3 | -1.51 | 6 | = 0.422 | -0.43 [-1.21, 0.15] | small | n.s. |
| Increase by 2 vs Increase by 3 | -0.75 | 6 | = 0.669 | -0.18 [-0.70, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1216.02, BIC = 1244.22
- **Decrease by 1 vs Cardinality (no change)**: *β* = 20.13, *SE* = 10.482, *z* = 1.920, *p* = 0.055
- **Decrease by 2 vs Cardinality (no change)**: *β* = 0.08, *SE* = 10.209, *z* = 0.008, *p* = 0.993
- **Decrease by 3 vs Cardinality (no change)**: *β* = 8.47, *SE* = 10.470, *z* = 0.809, *p* = 0.418
- **Increase by 1 vs Cardinality (no change)**: *β* = 17.41, *SE* = 10.559, *z* = 1.649, *p* = 0.099
- **Increase by 2 vs Cardinality (no change)**: *β* = 14.71, *SE* = 10.596, *z* = 1.389, *p* = 0.165
- **Increase by 3 vs Cardinality (no change)**: *β* = 4.46, *SE* = 9.967, *z* = 0.447, *p* = 0.655
- **SNR**: *β* = -0.29, *SE* = 0.644, *z* = -0.451, *p* = 0.652

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -20.13 | 10.48 | -1.92 | 0.055 | 0.676 | n.s. |
| Cardinality (no change) - Decrease by 2 | -0.08 | 10.21 | -0.01 | 0.993 | 0.997 | n.s. |
| Cardinality (no change) - Decrease by 3 | -8.47 | 10.47 | -0.81 | 0.418 | 0.992 | n.s. |
| Cardinality (no change) - Increase by 1 | -17.41 | 10.56 | -1.65 | 0.099 | 0.831 | n.s. |
| Cardinality (no change) - Increase by 2 | -14.72 | 10.60 | -1.39 | 0.165 | 0.933 | n.s. |
| Cardinality (no change) - Increase by 3 | -4.46 | 9.97 | -0.45 | 0.655 | 0.997 | n.s. |
| Decrease by 1 - Decrease by 2 | 20.05 | 9.13 | 2.19 | 0.028 | 0.451 | n.s. |
| Decrease by 1 - Decrease by 3 | 11.66 | 9.14 | 1.28 | 0.202 | 0.947 | n.s. |
| Decrease by 1 - Increase by 1 | 2.72 | 9.52 | 0.29 | 0.775 | 0.997 | n.s. |
| Decrease by 1 - Increase by 2 | 5.41 | 9.23 | 0.59 | 0.558 | 0.997 | n.s. |
| Decrease by 1 - Increase by 3 | 15.67 | 9.05 | 1.73 | 0.083 | 0.791 | n.s. |
| Decrease by 2 - Decrease by 3 | -8.39 | 9.01 | -0.93 | 0.352 | 0.991 | n.s. |
| Decrease by 2 - Increase by 1 | -17.32 | 9.46 | -1.83 | 0.067 | 0.732 | n.s. |
| Decrease by 2 - Increase by 2 | -14.63 | 9.17 | -1.60 | 0.110 | 0.846 | n.s. |
| Decrease by 2 - Increase by 3 | -4.37 | 8.86 | -0.49 | 0.622 | 0.997 | n.s. |
| Decrease by 3 - Increase by 1 | -8.94 | 9.50 | -0.94 | 0.347 | 0.991 | n.s. |
| Decrease by 3 - Increase by 2 | -6.24 | 9.17 | -0.68 | 0.496 | 0.996 | n.s. |
| Decrease by 3 - Increase by 3 | 4.01 | 8.98 | 0.45 | 0.655 | 0.997 | n.s. |
| Increase by 1 - Increase by 2 | 2.69 | 9.56 | 0.28 | 0.778 | 0.997 | n.s. |
| Increase by 1 - Increase by 3 | 12.95 | 9.34 | 1.39 | 0.165 | 0.933 | n.s. |
| Increase by 2 - Increase by 3 | 10.26 | 9.12 | 1.12 | 0.261 | 0.973 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.277, η²_G = 0.056
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -1.92 | 12 | = 0.552 | -0.68 [-1.18, 0.11] | medium | n.s. |
| Cardinality (no change) vs Decrease by 2 | -0.34 | 12 | = 0.779 | -0.11 [-0.63, 0.53] | negligible | n.s. |
| Cardinality (no change) vs Decrease by 3 | -0.45 | 12 | = 0.768 | -0.17 [-0.73, 0.48] | negligible | n.s. |
| Cardinality (no change) vs Increase by 1 | -1.08 | 12 | = 0.632 | -0.43 [-0.92, 0.32] | small | n.s. |
| Cardinality (no change) vs Increase by 2 | -0.83 | 12 | = 0.704 | -0.32 [-0.92, 0.27] | small | n.s. |
| Cardinality (no change) vs Increase by 3 | 0.35 | 12 | = 0.779 | 0.13 [-0.60, 0.56] | negligible | n.s. |
| Decrease by 1 vs Decrease by 2 | 2.36 | 12 | = 0.552 | 0.57 [0.08, 1.22] | medium | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.44 | 12 | = 0.632 | 0.46 [-0.06, 1.02] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 0.52 | 12 | = 0.768 | 0.10 [-0.50, 0.57] | negligible | n.s. |
| Decrease by 1 vs Increase by 2 | 1.23 | 12 | = 0.632 | 0.32 [-0.34, 0.69] | small | n.s. |
| Decrease by 1 vs Increase by 3 | 1.93 | 12 | = 0.552 | 0.66 [-0.16, 0.86] | medium | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.25 | 12 | = 0.808 | -0.07 [-0.69, 0.32] | negligible | n.s. |
| Decrease by 2 vs Increase by 1 | -1.08 | 12 | = 0.632 | -0.35 [-1.01, 0.15] | small | n.s. |
| Decrease by 2 vs Increase by 2 | -0.89 | 12 | = 0.704 | -0.22 [-0.98, 0.10] | small | n.s. |
| Decrease by 2 vs Increase by 3 | 0.73 | 12 | = 0.704 | 0.22 [-0.58, 0.39] | small | n.s. |
| Decrease by 3 vs Increase by 1 | -0.74 | 12 | = 0.704 | -0.28 [-0.86, 0.28] | small | n.s. |
| Decrease by 3 vs Increase by 2 | -0.69 | 12 | = 0.704 | -0.14 [-0.67, 0.40] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 1.41 | 12 | = 0.632 | 0.26 [-0.36, 0.64] | small | n.s. |
| Increase by 1 vs Increase by 2 | 0.47 | 12 | = 0.768 | 0.16 [-0.45, 0.62] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.27 | 12 | = 0.632 | 0.47 [-0.20, 0.90] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.47 | 12 | = 0.632 | 0.38 [-0.25, 0.76] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 447.10, BIC = 475.30
- **Decrease by 1 vs Cardinality (no change)**: *β* = 1.41, *SE* = 0.427, *z* = 3.298, *p* = 0.001
- **Decrease by 2 vs Cardinality (no change)**: *β* = 1.68, *SE* = 0.415, *z* = 4.053, *p* < .001
- **Decrease by 3 vs Cardinality (no change)**: *β* = 2.15, *SE* = 0.433, *z* = 4.949, *p* < .001
- **Increase by 1 vs Cardinality (no change)**: *β* = 0.75, *SE* = 0.425, *z* = 1.762, *p* = 0.078
- **Increase by 2 vs Cardinality (no change)**: *β* = 1.73, *SE* = 0.433, *z* = 4.004, *p* < .001
- **Increase by 3 vs Cardinality (no change)**: *β* = 1.65, *SE* = 0.404, *z* = 4.075, *p* < .001
- **SNR**: *β* = 0.20, *SE* = 0.029, *z* = 6.714, *p* < .001

_Reference condition: **Cardinality (no change)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change) - Decrease by 1 | -1.41 | 0.43 | -3.30 | < .001 | 0.015 | * |
| Cardinality (no change) - Decrease by 2 | -1.68 | 0.42 | -4.05 | < .001 | < .001 | *** |
| Cardinality (no change) - Decrease by 3 | -2.15 | 0.43 | -4.95 | < .001 | < .001 | *** |
| Cardinality (no change) - Increase by 1 | -0.75 | 0.42 | -1.76 | 0.078 | 0.591 | n.s. |
| Cardinality (no change) - Increase by 2 | -1.73 | 0.43 | -4.00 | < .001 | 0.001 | ** |
| Cardinality (no change) - Increase by 3 | -1.65 | 0.40 | -4.08 | < .001 | < .001 | *** |
| Decrease by 1 - Decrease by 2 | -0.27 | 0.36 | -0.76 | 0.450 | 0.950 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.74 | 0.36 | -2.02 | 0.044 | 0.414 | n.s. |
| Decrease by 1 - Increase by 1 | 0.66 | 0.38 | 1.75 | 0.080 | 0.591 | n.s. |
| Decrease by 1 - Increase by 2 | -0.32 | 0.37 | -0.88 | 0.378 | 0.942 | n.s. |
| Decrease by 1 - Increase by 3 | -0.24 | 0.36 | -0.66 | 0.506 | 0.950 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.46 | 0.36 | -1.29 | 0.198 | 0.830 | n.s. |
| Decrease by 2 - Increase by 1 | 0.93 | 0.38 | 2.49 | 0.013 | 0.166 | n.s. |
| Decrease by 2 - Increase by 2 | -0.05 | 0.36 | -0.13 | 0.893 | 0.994 | n.s. |
| Decrease by 2 - Increase by 3 | 0.04 | 0.35 | 0.10 | 0.920 | 0.994 | n.s. |
| Decrease by 3 - Increase by 1 | 1.40 | 0.38 | 3.67 | < .001 | 0.004 | ** |
| Decrease by 3 - Increase by 2 | 0.41 | 0.37 | 1.13 | 0.260 | 0.878 | n.s. |
| Decrease by 3 - Increase by 3 | 0.50 | 0.36 | 1.39 | 0.166 | 0.805 | n.s. |
| Increase by 1 - Increase by 2 | -0.98 | 0.38 | -2.59 | 0.010 | 0.134 | n.s. |
| Increase by 1 - Increase by 3 | -0.90 | 0.37 | -2.43 | 0.015 | 0.180 | n.s. |
| Increase by 2 - Increase by 3 | 0.08 | 0.36 | 0.23 | 0.816 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.40, *p* < .001, η²_G = 0.198
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change) vs Decrease by 1 | -4.22 | 12 | = 0.008 | -1.39 [-1.95, -0.39] | large | ** |
| Cardinality (no change) vs Decrease by 2 | -4.22 | 12 | = 0.008 | -1.55 [-1.80, -0.35] | large | ** |
| Cardinality (no change) vs Decrease by 3 | -4.02 | 12 | = 0.009 | -1.58 [-1.88, -0.35] | large | ** |
| Cardinality (no change) vs Increase by 1 | -2.48 | 12 | = 0.056 | -0.86 [-1.36, -0.01] | large | n.s. |
| Cardinality (no change) vs Increase by 2 | -4.41 | 12 | = 0.008 | -1.44 [-1.85, -0.38] | large | ** |
| Cardinality (no change) vs Increase by 3 | -3.23 | 12 | = 0.030 | -1.24 [-1.51, -0.17] | large | * |
| Decrease by 1 vs Decrease by 2 | -0.15 | 12 | = 0.883 | -0.03 [-0.63, 0.40] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.83 | 12 | = 0.160 | -0.39 [-1.12, -0.01] | small | n.s. |
| Decrease by 1 vs Increase by 1 | 2.72 | 12 | = 0.043 | 0.38 [0.15, 1.36] | small | * |
| Decrease by 1 vs Increase by 2 | -1.31 | 12 | = 0.280 | -0.19 [-1.01, 0.07] | negligible | n.s. |
| Decrease by 1 vs Increase by 3 | 0.39 | 12 | = 0.736 | 0.06 [-0.47, 0.52] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.69 | 12 | = 0.176 | -0.39 [-0.89, 0.14] | small | n.s. |
| Decrease by 2 vs Increase by 1 | 2.99 | 12 | = 0.036 | 0.43 [0.17, 1.44] | small | * |
| Decrease by 2 vs Increase by 2 | -0.85 | 12 | = 0.483 | -0.18 [-0.72, 0.31] | negligible | n.s. |
| Decrease by 2 vs Increase by 3 | 0.51 | 12 | = 0.686 | 0.09 [-0.31, 0.66] | negligible | n.s. |
| Decrease by 3 vs Increase by 1 | 2.92 | 12 | = 0.036 | 0.70 [0.21, 1.50] | medium | * |
| Decrease by 3 vs Increase by 2 | 0.89 | 12 | = 0.482 | 0.19 [-0.29, 0.79] | negligible | n.s. |
| Decrease by 3 vs Increase by 3 | 2.64 | 12 | = 0.045 | 0.42 [0.10, 1.20] | small | * |
| Increase by 1 vs Increase by 2 | -2.88 | 12 | = 0.036 | -0.53 [-1.51, -0.25] | medium | * |
| Increase by 1 vs Increase by 3 | -1.79 | 12 | = 0.160 | -0.31 [-1.24, -0.07] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.32 | 12 | = 0.280 | 0.24 [-0.17, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.028) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* = 0.010) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed greater amplitude than Increase by 2 (*d* = 0.33)
  - Cardinality (no change) showed greater amplitude than Increase by 3 (*d* = 0.64)
  - Decrease by 1 showed greater amplitude than Increase by 3 (*d* = 0.59)
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.44)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change) showed smaller amplitude than Decrease by 1 (*d* = -1.39)
  - Cardinality (no change) showed smaller amplitude than Decrease by 2 (*d* = -1.55)
  - Cardinality (no change) showed smaller amplitude than Decrease by 3 (*d* = -1.58)
  - Cardinality (no change) showed smaller amplitude than Increase by 2 (*d* = -1.44)
  - Cardinality (no change) showed smaller amplitude than Increase by 3 (*d* = -1.24)
  - Decrease by 1 showed greater amplitude than Increase by 1 (*d* = 0.38)
  - Decrease by 2 showed greater amplitude than Increase by 1 (*d* = 0.43)
  - Decrease by 3 showed greater amplitude than Increase by 1 (*d* = 0.70)
  - Decrease by 3 showed greater amplitude than Increase by 3 (*d* = 0.42)
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.53)

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

#### Amplitude

### 5.3 P1 Component

#### Latency

#### Amplitude

### 5.4 P3b Component

#### Latency

#### Amplitude

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
