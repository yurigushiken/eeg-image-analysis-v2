# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:24:34

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
| 2 to 2 | 22 | -3.10 µV | 1.79 | 0.38 | [-7.17, -0.12] |
| 3 to 2 | 22 | -3.91 µV | 2.03 | 0.43 | [-8.19, -0.50] |
| 4 to 2 | 24 | -3.96 µV | 2.47 | 0.51 | [-9.12, -0.67] |
| 5 to 2 | 24 | -4.76 µV | 2.59 | 0.53 | [-9.27, -0.25] |
| increasing 1 to 2 | 22 | -3.33 µV | 1.68 | 0.36 | [-6.38, -0.56] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 22 | 176.30 ms | 13.10 | 2.79 | [157.20, 197.73] |
| 3 to 2 | 22 | 174.68 ms | 9.94 | 2.12 | [157.64, 198.60] |
| 4 to 2 | 24 | 178.94 ms | 9.66 | 1.97 | [161.63, 204.46] |
| 5 to 2 | 24 | 175.83 ms | 9.21 | 1.88 | [155.87, 195.17] |
| increasing 1 to 2 | 22 | 175.42 ms | 13.35 | 2.85 | [154.07, 206.25] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 13 | 2.11 µV | 1.84 | 0.51 | [0.55, 6.85] |
| 3 to 2 | 9 | 2.08 µV | 1.57 | 0.52 | [-0.06, 4.37] |
| 4 to 2 | 14 | 2.23 µV | 1.19 | 0.32 | [0.29, 4.35] |
| 5 to 2 | 16 | 2.14 µV | 1.67 | 0.42 | [0.19, 5.35] |
| increasing 1 to 2 | 11 | 1.18 µV | 0.80 | 0.24 | [0.17, 2.68] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 13 | 112.52 ms | 2.84 | 0.79 | [107.32, 117.60] |
| 3 to 2 | 9 | 110.94 ms | 2.75 | 0.92 | [104.24, 113.65] |
| 4 to 2 | 14 | 112.86 ms | 1.20 | 0.32 | [110.58, 114.35] |
| 5 to 2 | 16 | 112.08 ms | 3.37 | 0.84 | [105.01, 118.47] |
| increasing 1 to 2 | 11 | 111.96 ms | 3.02 | 0.91 | [106.47, 116.79] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 11 | 2.64 µV | 1.81 | 0.55 | [0.77, 7.26] |
| 3 to 2 | 18 | 4.22 µV | 3.18 | 0.75 | [0.31, 12.11] |
| 4 to 2 | 18 | 3.73 µV | 2.61 | 0.62 | [0.17, 8.65] |
| 5 to 2 | 18 | 3.61 µV | 2.47 | 0.58 | [0.49, 10.08] |
| increasing 1 to 2 | 17 | 3.53 µV | 2.82 | 0.68 | [0.03, 10.36] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 11 | 473.22 ms | 14.15 | 4.27 | [443.18, 497.35] |
| 3 to 2 | 18 | 486.67 ms | 20.69 | 4.88 | [441.16, 530.94] |
| 4 to 2 | 18 | 478.48 ms | 19.50 | 4.60 | [431.61, 509.82] |
| 5 to 2 | 18 | 477.93 ms | 20.13 | 4.74 | [426.64, 514.84] |
| increasing 1 to 2 | 17 | 485.13 ms | 25.19 | 6.11 | [436.18, 536.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 427.83, BIC = 449.72
- **3 to 2 vs 2 to 2**: *β* = -0.16, *SE* = 0.390, *z* = -0.411, *p* = 0.681
- **4 to 2 vs 2 to 2**: *β* = -0.83, *SE* = 0.374, *z* = -2.213, *p* = 0.027
- **5 to 2 vs 2 to 2**: *β* = -0.87, *SE* = 0.391, *z* = -2.219, *p* = 0.026
- **increasing 1 to 2 vs 2 to 2**: *β* = 0.14, *SE* = 0.387, *z* = 0.367, *p* = 0.713
- **SNR**: *β* = -0.49, *SE* = 0.061, *z* = -7.917, *p* < .001

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | 0.16 | 0.39 | 0.41 | 0.681 | 0.967 | n.s. |
| 2 to 2 - 4 to 2 | 0.83 | 0.37 | 2.21 | 0.027 | 0.193 | n.s. |
| 2 to 2 - 5 to 2 | 0.87 | 0.39 | 2.22 | 0.026 | 0.193 | n.s. |
| 2 to 2 - increasing 1 to 2 | -0.14 | 0.39 | -0.37 | 0.713 | 0.967 | n.s. |
| 3 to 2 - 4 to 2 | 0.67 | 0.38 | 1.77 | 0.077 | 0.332 | n.s. |
| 3 to 2 - 5 to 2 | 0.71 | 0.38 | 1.89 | 0.059 | 0.305 | n.s. |
| 3 to 2 - increasing 1 to 2 | -0.30 | 0.38 | -0.79 | 0.431 | 0.895 | n.s. |
| 4 to 2 - 5 to 2 | 0.04 | 0.38 | 0.11 | 0.913 | 0.967 | n.s. |
| 4 to 2 - increasing 1 to 2 | -0.97 | 0.37 | -2.59 | 0.010 | 0.083 | n.s. |
| 5 to 2 - increasing 1 to 2 | -1.01 | 0.38 | -2.67 | 0.008 | 0.073 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.21, *p* = 0.004, η²_G = 0.093
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 2.09 | 18 | = 0.127 | 0.45 [0.05, 1.03] | small | n.s. |
| 2 to 2 vs 4 to 2 | 2.31 | 18 | = 0.110 | 0.63 [-0.06, 0.86] | medium | n.s. |
| 2 to 2 vs 5 to 2 | 3.72 | 18 | = 0.016 | 0.84 [0.27, 1.28] | large | * |
| 2 to 2 vs increasing 1 to 2 | 1.04 | 18 | = 0.391 | 0.22 [-0.36, 0.58] | small | n.s. |
| 3 to 2 vs 4 to 2 | 0.87 | 18 | = 0.439 | 0.20 [-0.29, 0.60] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.74 | 18 | = 0.183 | 0.42 [0.01, 0.95] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | -1.59 | 18 | = 0.183 | -0.27 [-0.88, 0.09] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.79 | 18 | = 0.443 | 0.22 [-0.15, 0.71] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | -1.60 | 18 | = 0.183 | -0.46 [-0.79, 0.12] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -3.19 | 18 | = 0.025 | -0.69 [-1.17, -0.19] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 849.65, BIC = 871.54
- **3 to 2 vs 2 to 2**: *β* = 0.03, *SE* = 2.432, *z* = 0.011, *p* = 0.991
- **4 to 2 vs 2 to 2**: *β* = 3.17, *SE* = 2.331, *z* = 1.360, *p* = 0.174
- **5 to 2 vs 2 to 2**: *β* = 0.55, *SE* = 2.442, *z* = 0.225, *p* = 0.822
- **increasing 1 to 2 vs 2 to 2**: *β* = -0.07, *SE* = 2.414, *z* = -0.029, *p* = 0.977
- **SNR**: *β* = -0.32, *SE* = 0.389, *z* = -0.817, *p* = 0.414

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -0.03 | 2.43 | -0.01 | 0.991 | 1.000 | n.s. |
| 2 to 2 - 4 to 2 | -3.17 | 2.33 | -1.36 | 0.174 | 0.836 | n.s. |
| 2 to 2 - 5 to 2 | -0.55 | 2.44 | -0.22 | 0.822 | 1.000 | n.s. |
| 2 to 2 - increasing 1 to 2 | 0.07 | 2.41 | 0.03 | 0.977 | 1.000 | n.s. |
| 3 to 2 - 4 to 2 | -3.14 | 2.36 | -1.33 | 0.183 | 0.836 | n.s. |
| 3 to 2 - 5 to 2 | -0.52 | 2.34 | -0.22 | 0.824 | 1.000 | n.s. |
| 3 to 2 - increasing 1 to 2 | 0.10 | 2.39 | 0.04 | 0.967 | 1.000 | n.s. |
| 4 to 2 - 5 to 2 | 2.62 | 2.34 | 1.12 | 0.264 | 0.883 | n.s. |
| 4 to 2 - increasing 1 to 2 | 3.24 | 2.34 | 1.39 | 0.165 | 0.836 | n.s. |
| 5 to 2 - increasing 1 to 2 | 0.62 | 2.36 | 0.26 | 0.793 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.92, *p* = 0.459, η²_G = 0.021
- Greenhouse-Geisser corrected: *p* = 0.433 (ε = 0.692)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 0.98 | 18 | = 0.683 | 0.21 [-0.42, 0.49] | small | n.s. |
| 2 to 2 vs 4 to 2 | -0.56 | 18 | = 0.774 | -0.16 [-0.63, 0.27] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 0.17 | 18 | = 0.870 | 0.04 [-0.51, 0.38] | negligible | n.s. |
| 2 to 2 vs increasing 1 to 2 | 0.77 | 18 | = 0.755 | 0.15 [-0.37, 0.57] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -1.95 | 18 | = 0.526 | -0.50 [-0.68, 0.22] | small | n.s. |
| 3 to 2 vs 5 to 2 | -1.71 | 18 | = 0.526 | -0.23 [-0.58, 0.31] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.25 | 18 | = 0.870 | -0.05 [-0.48, 0.46] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.08 | 18 | = 0.683 | 0.27 [-0.13, 0.74] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.29 | 18 | = 0.683 | 0.36 [-0.12, 0.79] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.51 | 18 | = 0.774 | 0.14 [-0.44, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 177.43, BIC = 194.57
- **3 to 2 vs 2 to 2**: *β* = -0.15, *SE* = 0.349, *z* = -0.438, *p* = 0.662
- **4 to 2 vs 2 to 2**: *β* = 0.02, *SE* = 0.307, *z* = 0.074, *p* = 0.941
- **5 to 2 vs 2 to 2**: *β* = -0.30, *SE* = 0.300, *z* = -0.994, *p* = 0.320
- **increasing 1 to 2 vs 2 to 2**: *β* = -0.72, *SE* = 0.329, *z* = -2.190, *p* = 0.029
- **SNR**: *β* = 0.86, *SE* = 0.085, *z* = 10.086, *p* < .001

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | 0.15 | 0.35 | 0.44 | 0.662 | 0.977 | n.s. |
| 2 to 2 - 4 to 2 | -0.02 | 0.31 | -0.07 | 0.941 | 0.977 | n.s. |
| 2 to 2 - 5 to 2 | 0.30 | 0.30 | 0.99 | 0.320 | 0.857 | n.s. |
| 2 to 2 - increasing 1 to 2 | 0.72 | 0.33 | 2.19 | 0.029 | 0.229 | n.s. |
| 3 to 2 - 4 to 2 | -0.18 | 0.34 | -0.51 | 0.611 | 0.977 | n.s. |
| 3 to 2 - 5 to 2 | 0.15 | 0.34 | 0.43 | 0.668 | 0.977 | n.s. |
| 3 to 2 - increasing 1 to 2 | 0.57 | 0.36 | 1.57 | 0.117 | 0.631 | n.s. |
| 4 to 2 - 5 to 2 | 0.32 | 0.30 | 1.09 | 0.277 | 0.857 | n.s. |
| 4 to 2 - increasing 1 to 2 | 0.74 | 0.32 | 2.31 | 0.021 | 0.192 | n.s. |
| 5 to 2 - increasing 1 to 2 | 0.42 | 0.32 | 1.32 | 0.188 | 0.767 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.22, *p* = 0.340, η²_G = 0.197
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 0.98 | 4 | = 0.636 | 0.64 [-0.85, 1.00] | medium | n.s. |
| 2 to 2 vs 4 to 2 | 0.75 | 4 | = 0.707 | 0.41 [-0.81, 0.63] | small | n.s. |
| 2 to 2 vs 5 to 2 | 0.35 | 4 | = 0.828 | 0.26 [-0.62, 0.73] | small | n.s. |
| 2 to 2 vs increasing 1 to 2 | 1.75 | 4 | = 0.384 | 1.18 [-0.24, 1.62] | large | n.s. |
| 3 to 2 vs 4 to 2 | -0.48 | 4 | = 0.820 | -0.37 [-0.99, 0.86] | small | n.s. |
| 3 to 2 vs 5 to 2 | -1.78 | 4 | = 0.384 | -0.45 [-1.36, 0.56] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.75 | 4 | = 0.384 | 0.71 [-0.59, 1.65] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -0.22 | 4 | = 0.837 | -0.16 [-0.97, 0.40] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.57 | 4 | = 0.384 | 1.30 [-0.29, 1.36] | large | n.s. |
| 5 to 2 vs increasing 1 to 2 | 2.12 | 4 | = 0.384 | 1.15 [-0.09, 1.67] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 289.68, BIC = 306.82
- **3 to 2 vs 2 to 2**: *β* = -0.10, *SE* = 0.687, *z* = -0.146, *p* = 0.884
- **4 to 2 vs 2 to 2**: *β* = 0.49, *SE* = 0.597, *z* = 0.825, *p* = 0.409
- **5 to 2 vs 2 to 2**: *β* = -0.53, *SE* = 0.580, *z* = -0.918, *p* = 0.358
- **increasing 1 to 2 vs 2 to 2**: *β* = 0.69, *SE* = 0.643, *z* = 1.079, *p* = 0.281
- **SNR**: *β* = -0.13, *SE* = 0.181, *z* = -0.722, *p* = 0.470

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | 0.10 | 0.69 | 0.15 | 0.884 | 0.937 | n.s. |
| 2 to 2 - 4 to 2 | -0.49 | 0.60 | -0.83 | 0.409 | 0.930 | n.s. |
| 2 to 2 - 5 to 2 | 0.53 | 0.58 | 0.92 | 0.358 | 0.930 | n.s. |
| 2 to 2 - increasing 1 to 2 | -0.69 | 0.64 | -1.08 | 0.281 | 0.909 | n.s. |
| 3 to 2 - 4 to 2 | -0.59 | 0.68 | -0.87 | 0.383 | 0.930 | n.s. |
| 3 to 2 - 5 to 2 | 0.43 | 0.68 | 0.64 | 0.523 | 0.930 | n.s. |
| 3 to 2 - increasing 1 to 2 | -0.79 | 0.70 | -1.13 | 0.259 | 0.909 | n.s. |
| 4 to 2 - 5 to 2 | 1.03 | 0.58 | 1.76 | 0.078 | 0.517 | n.s. |
| 4 to 2 - increasing 1 to 2 | -0.20 | 0.63 | -0.32 | 0.748 | 0.937 | n.s. |
| 5 to 2 - increasing 1 to 2 | -1.23 | 0.64 | -1.93 | 0.054 | 0.425 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.17, *p* = 0.951, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 1.23 | 4 | = 0.952 | 0.63 [-0.89, 0.96] | medium | n.s. |
| 2 to 2 vs 4 to 2 | 0.19 | 4 | = 0.952 | 0.08 [-0.98, 0.47] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 0.63 | 4 | = 0.952 | 0.25 [-0.44, 0.92] | small | n.s. |
| 2 to 2 vs increasing 1 to 2 | -0.06 | 4 | = 0.952 | -0.04 [-1.12, 0.59] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -1.51 | 4 | = 0.952 | -0.49 [-1.56, 0.43] | small | n.s. |
| 3 to 2 vs 5 to 2 | -0.21 | 4 | = 0.952 | -0.13 [-0.67, 1.22] | negligible | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.58 | 4 | = 0.952 | -0.28 [-1.50, 0.69] | small | n.s. |
| 4 to 2 vs 5 to 2 | 0.33 | 4 | = 0.952 | 0.20 [-0.43, 0.94] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | -0.11 | 4 | = 0.952 | -0.07 [-0.68, 0.86] | negligible | n.s. |
| 5 to 2 vs increasing 1 to 2 | -0.36 | 4 | = 0.952 | -0.17 [-1.48, 0.21] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.98, BIC = 317.23
- **3 to 2 vs 2 to 2**: *β* = 0.91, *SE* = 0.428, *z* = 2.131, *p* = 0.033
- **4 to 2 vs 2 to 2**: *β* = 0.81, *SE* = 0.426, *z* = 1.906, *p* = 0.057
- **5 to 2 vs 2 to 2**: *β* = -0.66, *SE* = 0.456, *z* = -1.435, *p* = 0.151
- **increasing 1 to 2 vs 2 to 2**: *β* = 0.17, *SE* = 0.443, *z* = 0.382, *p* = 0.703
- **SNR**: *β* = 0.64, *SE* = 0.065, *z* = 9.761, *p* < .001

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -0.91 | 0.43 | -2.13 | 0.033 | 0.235 | n.s. |
| 2 to 2 - 4 to 2 | -0.81 | 0.43 | -1.91 | 0.057 | 0.256 | n.s. |
| 2 to 2 - 5 to 2 | 0.65 | 0.46 | 1.43 | 0.151 | 0.389 | n.s. |
| 2 to 2 - increasing 1 to 2 | -0.17 | 0.44 | -0.38 | 0.703 | 0.912 | n.s. |
| 3 to 2 - 4 to 2 | 0.10 | 0.36 | 0.28 | 0.781 | 0.912 | n.s. |
| 3 to 2 - 5 to 2 | 1.57 | 0.38 | 4.17 | < .001 | < .001 | *** |
| 3 to 2 - increasing 1 to 2 | 0.74 | 0.38 | 1.98 | 0.048 | 0.256 | n.s. |
| 4 to 2 - 5 to 2 | 1.47 | 0.38 | 3.84 | < .001 | 0.001 | ** |
| 4 to 2 - increasing 1 to 2 | 0.64 | 0.38 | 1.71 | 0.088 | 0.308 | n.s. |
| 5 to 2 - increasing 1 to 2 | -0.82 | 0.39 | -2.13 | 0.033 | 0.235 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.92, *p* = 0.016, η²_G = 0.213
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | -4.18 | 5 | = 0.087 | -1.42 [-1.47, 0.12] | large | n.s. |
| 2 to 2 vs 4 to 2 | -2.17 | 5 | = 0.206 | -0.98 [-1.46, 0.12] | large | n.s. |
| 2 to 2 vs 5 to 2 | -1.19 | 5 | = 0.360 | -0.67 [-1.07, 0.40] | medium | n.s. |
| 2 to 2 vs increasing 1 to 2 | -1.11 | 5 | = 0.360 | -0.53 [-1.32, 0.43] | medium | n.s. |
| 3 to 2 vs 4 to 2 | 1.09 | 5 | = 0.360 | 0.24 [-0.31, 0.76] | small | n.s. |
| 3 to 2 vs 5 to 2 | 2.83 | 5 | = 0.165 | 0.87 [-0.20, 0.90] | large | n.s. |
| 3 to 2 vs increasing 1 to 2 | 2.58 | 5 | = 0.165 | 0.89 [-0.25, 1.00] | large | n.s. |
| 4 to 2 vs 5 to 2 | 1.53 | 5 | = 0.360 | 0.46 [-0.36, 0.71] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.40 | 5 | = 0.360 | 0.52 [-0.37, 0.86] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.38 | 5 | = 0.722 | 0.10 [-0.38, 0.78] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 723.59, BIC = 742.84
- **3 to 2 vs 2 to 2**: *β* = 7.38, *SE* = 5.887, *z* = 1.254, *p* = 0.210
- **4 to 2 vs 2 to 2**: *β* = 0.07, *SE* = 5.840, *z* = 0.012, *p* = 0.991
- **5 to 2 vs 2 to 2**: *β* = -1.89, *SE* = 6.293, *z* = -0.301, *p* = 0.763
- **increasing 1 to 2 vs 2 to 2**: *β* = 5.00, *SE* = 6.162, *z* = 0.811, *p* = 0.418
- **SNR**: *β* = 0.53, *SE* = 0.863, *z* = 0.615, *p* = 0.539

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -7.38 | 5.89 | -1.25 | 0.210 | 0.815 | n.s. |
| 2 to 2 - 4 to 2 | -0.07 | 5.84 | -0.01 | 0.991 | 0.991 | n.s. |
| 2 to 2 - 5 to 2 | 1.89 | 6.29 | 0.30 | 0.763 | 0.984 | n.s. |
| 2 to 2 - increasing 1 to 2 | -5.00 | 6.16 | -0.81 | 0.418 | 0.933 | n.s. |
| 3 to 2 - 4 to 2 | 7.31 | 4.94 | 1.48 | 0.139 | 0.739 | n.s. |
| 3 to 2 - 5 to 2 | 9.27 | 5.13 | 1.81 | 0.070 | 0.518 | n.s. |
| 3 to 2 - increasing 1 to 2 | 2.38 | 5.15 | 0.46 | 0.643 | 0.984 | n.s. |
| 4 to 2 - 5 to 2 | 1.96 | 5.22 | 0.38 | 0.707 | 0.984 | n.s. |
| 4 to 2 - increasing 1 to 2 | -4.93 | 5.16 | -0.95 | 0.340 | 0.917 | n.s. |
| 5 to 2 - increasing 1 to 2 | -6.89 | 5.26 | -1.31 | 0.190 | 0.815 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.614, η²_G = 0.084
- Greenhouse-Geisser corrected: *p* = 0.492 (ε = 0.367)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | -0.83 | 5 | = 0.738 | -0.55 [-1.02, 0.44] | medium | n.s. |
| 2 to 2 vs 4 to 2 | -0.50 | 5 | = 0.798 | -0.32 [-0.69, 0.74] | small | n.s. |
| 2 to 2 vs 5 to 2 | -0.56 | 5 | = 0.798 | -0.37 [-0.77, 0.66] | small | n.s. |
| 2 to 2 vs increasing 1 to 2 | 0.08 | 5 | = 0.939 | 0.05 [-0.79, 0.88] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | 1.08 | 5 | = 0.658 | 0.37 [-0.08, 1.04] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.14 | 5 | = 0.658 | 0.21 [-0.19, 0.91] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | 2.43 | 5 | = 0.297 | 0.89 [-0.61, 0.60] | large | n.s. |
| 4 to 2 vs 5 to 2 | -0.26 | 5 | = 0.891 | -0.11 [-0.43, 0.64] | negligible | n.s. |
| 4 to 2 vs increasing 1 to 2 | 4.39 | 5 | = 0.071 | 0.59 [-0.57, 0.64] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | 1.28 | 5 | = 0.658 | 0.60 [-0.87, 0.30] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - 2 to 2 showed greater amplitude than 5 to 2 (*d* = 0.84)
  - 5 to 2 showed smaller amplitude than increasing 1 to 2 (*d* = -0.69)
**P3b amplitude:** Significant main effect of condition (*p* = 0.016) (no significant pairwise comparisons)

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
