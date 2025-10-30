# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:16:58

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
| 3 to 1 | 19 | -2.83 µV | 2.30 | 0.53 | [-7.70, 0.04] |
| 4 to 2 | 24 | -4.16 µV | 2.50 | 0.51 | [-9.30, -0.77] |
| 5 to 3 | 24 | -3.79 µV | 2.43 | 0.50 | [-8.62, -0.11] |
| 6 to 4 | 23 | -3.74 µV | 2.24 | 0.47 | [-9.81, -0.79] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 19 | 182.30 ms | 11.43 | 2.62 | [162.94, 203.39] |
| 4 to 2 | 24 | 178.90 ms | 8.32 | 1.70 | [163.75, 199.96] |
| 5 to 3 | 24 | 176.65 ms | 10.82 | 2.21 | [157.35, 207.52] |
| 6 to 4 | 23 | 176.87 ms | 10.45 | 2.18 | [161.10, 201.71] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 21 | 2.23 µV | 1.76 | 0.39 | [0.18, 7.32] |
| 4 to 2 | 14 | 2.13 µV | 1.11 | 0.30 | [0.51, 4.30] |
| 5 to 3 | 17 | 1.94 µV | 1.25 | 0.30 | [-0.13, 3.48] |
| 6 to 4 | 15 | 2.89 µV | 1.30 | 0.34 | [1.24, 5.12] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 21 | 115.26 ms | 6.79 | 1.48 | [100.88, 125.41] |
| 4 to 2 | 14 | 116.43 ms | 2.90 | 0.77 | [110.37, 120.87] |
| 5 to 3 | 17 | 113.01 ms | 5.61 | 1.36 | [102.40, 123.96] |
| 6 to 4 | 15 | 115.16 ms | 3.59 | 0.93 | [109.17, 123.37] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 4.19 µV | 2.52 | 0.56 | [0.72, 10.89] |
| 4 to 2 | 18 | 3.81 µV | 2.66 | 0.63 | [0.22, 8.65] |
| 5 to 3 | 17 | 4.14 µV | 1.75 | 0.42 | [1.03, 8.32] |
| 6 to 4 | 19 | 3.55 µV | 2.34 | 0.54 | [0.05, 8.53] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 479.78 ms | 11.22 | 2.51 | [462.26, 503.57] |
| 4 to 2 | 18 | 478.99 ms | 17.41 | 4.10 | [436.38, 501.95] |
| 5 to 3 | 17 | 476.88 ms | 12.41 | 3.01 | [449.55, 496.77] |
| 6 to 4 | 19 | 485.84 ms | 22.81 | 5.23 | [431.12, 531.78] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 360.45, BIC = 377.95
- **4 to 2 vs 3 to 1**: *β* = -1.05, *SE* = 0.454, *z* = -2.305, *p* = 0.021
- **5 to 3 vs 3 to 1**: *β* = -0.31, *SE* = 0.464, *z* = -0.677, *p* = 0.498
- **6 to 4 vs 3 to 1**: *β* = -0.09, *SE* = 0.477, *z* = -0.188, *p* = 0.850
- **SNR**: *β* = -0.42, *SE* = 0.054, *z* = -7.834, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 1.05 | 0.45 | 2.31 | 0.021 | 0.120 | n.s. |
| 3 to 1 - 5 to 3 | 0.31 | 0.46 | 0.68 | 0.498 | 0.874 | n.s. |
| 3 to 1 - 6 to 4 | 0.09 | 0.48 | 0.19 | 0.850 | 0.874 | n.s. |
| 4 to 2 - 5 to 3 | -0.73 | 0.42 | -1.75 | 0.080 | 0.285 | n.s. |
| 4 to 2 - 6 to 4 | -0.96 | 0.43 | -2.23 | 0.026 | 0.122 | n.s. |
| 5 to 3 - 6 to 4 | -0.22 | 0.42 | -0.53 | 0.597 | 0.874 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.45, *p* = 0.023, η²_G = 0.091
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 3.37 | 17 | = 0.022 | 0.86 [0.20, 1.29] | large | * |
| 3 to 1 vs 5 to 3 | 1.85 | 17 | = 0.169 | 0.64 [-0.16, 0.84] | medium | n.s. |
| 3 to 1 vs 6 to 4 | 1.83 | 17 | = 0.169 | 0.59 [-0.09, 0.95] | medium | n.s. |
| 4 to 2 vs 5 to 3 | -0.82 | 17 | = 0.511 | -0.20 [-0.57, 0.28] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.11 | 17 | = 0.421 | -0.26 [-0.58, 0.29] | small | n.s. |
| 5 to 3 vs 6 to 4 | -0.27 | 17 | = 0.787 | -0.06 [-0.48, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 649.67, BIC = 667.17
- **4 to 2 vs 3 to 1**: *β* = -2.49, *SE* = 2.061, *z* = -1.208, *p* = 0.227
- **5 to 3 vs 3 to 1**: *β* = -4.46, *SE* = 2.106, *z* = -2.116, *p* = 0.034
- **6 to 4 vs 3 to 1**: *β* = -4.18, *SE* = 2.167, *z* = -1.929, *p* = 0.054
- **SNR**: *β* = -0.32, *SE* = 0.253, *z* = -1.277, *p* = 0.201

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 2.49 | 2.06 | 1.21 | 0.227 | 0.643 | n.s. |
| 3 to 1 - 5 to 3 | 4.46 | 2.11 | 2.12 | 0.034 | 0.189 | n.s. |
| 3 to 1 - 6 to 4 | 4.18 | 2.17 | 1.93 | 0.054 | 0.241 | n.s. |
| 4 to 2 - 5 to 3 | 1.97 | 1.90 | 1.04 | 0.300 | 0.657 | n.s. |
| 4 to 2 - 6 to 4 | 1.69 | 1.94 | 0.87 | 0.384 | 0.657 | n.s. |
| 5 to 3 - 6 to 4 | -0.28 | 1.91 | -0.14 | 0.885 | 0.885 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.83, *p* = 0.153, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.32 | 17 | = 0.409 | 0.35 [-0.17, 0.82] | small | n.s. |
| 3 to 1 vs 5 to 3 | 1.58 | 17 | = 0.396 | 0.38 [-0.13, 0.87] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.76 | 17 | = 0.396 | 0.42 [-0.10, 0.93] | small | n.s. |
| 4 to 2 vs 5 to 3 | 0.59 | 17 | = 0.672 | 0.10 [-0.15, 0.71] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.61 | 17 | = 0.672 | 0.13 [-0.18, 0.69] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.13 | 17 | = 0.901 | 0.02 [-0.47, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 190.83, BIC = 206.26
- **4 to 2 vs 3 to 1**: *β* = 0.17, *SE* = 0.312, *z* = 0.561, *p* = 0.575
- **5 to 3 vs 3 to 1**: *β* = -0.32, *SE* = 0.293, *z* = -1.105, *p* = 0.269
- **6 to 4 vs 3 to 1**: *β* = 0.39, *SE* = 0.305, *z* = 1.268, *p* = 0.205
- **SNR**: *β* = 0.44, *SE* = 0.050, *z* = 8.873, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.17 | 0.31 | -0.56 | 0.575 | 0.780 | n.s. |
| 3 to 1 - 5 to 3 | 0.32 | 0.29 | 1.11 | 0.269 | 0.609 | n.s. |
| 3 to 1 - 6 to 4 | -0.39 | 0.31 | -1.27 | 0.205 | 0.600 | n.s. |
| 4 to 2 - 5 to 3 | 0.50 | 0.33 | 1.53 | 0.127 | 0.492 | n.s. |
| 4 to 2 - 6 to 4 | -0.21 | 0.34 | -0.63 | 0.531 | 0.780 | n.s. |
| 5 to 3 - 6 to 4 | -0.71 | 0.32 | -2.23 | 0.026 | 0.147 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.83, *p* = 0.173, η²_G = 0.136
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.96 | 7 | = 0.550 | 0.50 [-0.55, 0.60] | medium | n.s. |
| 3 to 1 vs 5 to 3 | 1.12 | 7 | = 0.550 | 0.46 [-0.35, 0.73] | small | n.s. |
| 3 to 1 vs 6 to 4 | -0.57 | 7 | = 0.707 | -0.24 [-0.97, 0.23] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.02 | 7 | = 0.983 | -0.01 [-0.71, 0.63] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -3.00 | 7 | = 0.119 | -1.22 [-1.44, 0.14] | large | n.s. |
| 5 to 3 vs 6 to 4 | -2.01 | 7 | = 0.253 | -1.02 [-1.17, 0.18] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 417.82, BIC = 433.25
- **4 to 2 vs 3 to 1**: *β* = 0.97, *SE* = 1.560, *z* = 0.621, *p* = 0.534
- **5 to 3 vs 3 to 1**: *β* = -2.54, *SE* = 1.465, *z* = -1.732, *p* = 0.083
- **6 to 4 vs 3 to 1**: *β* = -0.64, *SE* = 1.553, *z* = -0.409, *p* = 0.682
- **SNR**: *β* = -0.17, *SE* = 0.251, *z* = -0.665, *p* = 0.506

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.97 | 1.56 | -0.62 | 0.534 | 0.783 | n.s. |
| 3 to 1 - 5 to 3 | 2.54 | 1.47 | 1.73 | 0.083 | 0.352 | n.s. |
| 3 to 1 - 6 to 4 | 0.64 | 1.55 | 0.41 | 0.682 | 0.783 | n.s. |
| 4 to 2 - 5 to 3 | 3.51 | 1.65 | 2.13 | 0.033 | 0.183 | n.s. |
| 4 to 2 - 6 to 4 | 1.60 | 1.73 | 0.93 | 0.353 | 0.730 | n.s. |
| 5 to 3 - 6 to 4 | -1.90 | 1.61 | -1.18 | 0.237 | 0.660 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.83, *p* = 0.493, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -0.26 | 7 | = 0.800 | -0.12 [-0.73, 0.44] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.93 | 7 | = 0.576 | 0.33 [-0.14, 0.97] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.95 | 7 | = 0.576 | 0.30 [-0.17, 1.04] | small | n.s. |
| 4 to 2 vs 5 to 3 | 1.14 | 7 | = 0.576 | 0.50 [-0.09, 1.39] | medium | n.s. |
| 4 to 2 vs 6 to 4 | 1.64 | 7 | = 0.576 | 0.76 [-0.11, 1.49] | medium | n.s. |
| 5 to 3 vs 6 to 4 | -0.38 | 7 | = 0.800 | -0.14 [-0.87, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 324.20, BIC = 340.33
- **4 to 2 vs 3 to 1**: *β* = 0.52, *SE* = 0.633, *z* = 0.822, *p* = 0.411
- **5 to 3 vs 3 to 1**: *β* = 0.46, *SE* = 0.623, *z* = 0.735, *p* = 0.462
- **6 to 4 vs 3 to 1**: *β* = 0.23, *SE* = 0.623, *z* = 0.365, *p* = 0.715
- **SNR**: *β* = 0.24, *SE* = 0.051, *z* = 4.644, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.52 | 0.63 | -0.82 | 0.411 | 0.958 | n.s. |
| 3 to 1 - 5 to 3 | -0.46 | 0.62 | -0.74 | 0.462 | 0.958 | n.s. |
| 3 to 1 - 6 to 4 | -0.23 | 0.62 | -0.36 | 0.715 | 0.982 | n.s. |
| 4 to 2 - 5 to 3 | 0.06 | 0.63 | 0.10 | 0.922 | 0.982 | n.s. |
| 4 to 2 - 6 to 4 | 0.29 | 0.61 | 0.48 | 0.631 | 0.982 | n.s. |
| 5 to 3 - 6 to 4 | 0.23 | 0.63 | 0.37 | 0.712 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.96, *p* = 0.421, η²_G = 0.043
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.30 | 13 | = 0.628 | 0.30 [-0.22, 0.83] | small | n.s. |
| 3 to 1 vs 5 to 3 | 0.76 | 13 | = 0.650 | 0.31 [-0.42, 0.65] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.33 | 13 | = 0.628 | 0.58 [-0.34, 0.66] | medium | n.s. |
| 4 to 2 vs 5 to 3 | -0.21 | 13 | = 0.839 | -0.06 [-0.67, 0.44] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.63 | 13 | = 0.650 | 0.20 [-0.36, 0.71] | small | n.s. |
| 5 to 3 vs 6 to 4 | 1.05 | 13 | = 0.628 | 0.35 [-0.21, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 626.57, BIC = 642.70
- **4 to 2 vs 3 to 1**: *β* = -0.85, *SE* = 4.551, *z* = -0.186, *p* = 0.852
- **5 to 3 vs 3 to 1**: *β* = -3.31, *SE* = 4.458, *z* = -0.744, *p* = 0.457
- **6 to 4 vs 3 to 1**: *β* = 5.60, *SE* = 4.457, *z* = 1.256, *p* = 0.209
- **SNR**: *β* = 0.04, *SE* = 0.383, *z* = 0.113, *p* = 0.910

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 0.85 | 4.55 | 0.19 | 0.852 | 0.852 | n.s. |
| 3 to 1 - 5 to 3 | 3.32 | 4.46 | 0.74 | 0.457 | 0.840 | n.s. |
| 3 to 1 - 6 to 4 | -5.60 | 4.46 | -1.26 | 0.209 | 0.609 | n.s. |
| 4 to 2 - 5 to 3 | 2.47 | 4.52 | 0.55 | 0.585 | 0.840 | n.s. |
| 4 to 2 - 6 to 4 | -6.45 | 4.35 | -1.48 | 0.139 | 0.526 | n.s. |
| 5 to 3 - 6 to 4 | -8.91 | 4.47 | -1.99 | 0.046 | 0.246 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.48, *p* = 0.236, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -0.41 | 13 | = 0.857 | -0.11 [-0.38, 0.65] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | -0.02 | 13 | = 0.986 | -0.01 [-0.41, 0.66] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | -1.40 | 13 | = 0.368 | -0.51 [-0.73, 0.28] | medium | n.s. |
| 4 to 2 vs 5 to 3 | 0.37 | 13 | = 0.857 | 0.10 [-0.49, 0.62] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.56 | 13 | = 0.368 | -0.35 [-0.79, 0.29] | small | n.s. |
| 5 to 3 vs 6 to 4 | -1.43 | 13 | = 0.368 | -0.50 [-1.02, 0.14] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.023). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 0.86)

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
