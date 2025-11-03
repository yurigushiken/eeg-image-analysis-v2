# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:40:41

---

## 1. Analysis Overview

**Total Measurements:** 384
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 1 to 1 | 10 | 101.20 ms | 10.67 | 3.38 | [88.00, 112.00] |
| 1 to 2 | 12 | 102.00 ms | 9.11 | 2.63 | [88.00, 112.00] |
| 1 to 3 | 17 | 103.06 ms | 9.75 | 2.36 | [88.00, 112.00] |
| 1 to 4 | 13 | 101.54 ms | 10.78 | 2.99 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 10 | 2.87 µV | 2.31 | 0.73 | [0.62, 8.77] |
| 1 to 2 | 12 | 2.61 µV | 1.98 | 0.57 | [0.61, 5.82] |
| 1 to 3 | 17 | 2.53 µV | 1.82 | 0.44 | [0.53, 7.03] |
| 1 to 4 | 13 | 2.46 µV | 1.28 | 0.36 | [0.85, 5.41] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 14 | 179.71 ms | 19.31 | 5.16 | [144.00, 208.00] |
| 1 to 2 | 22 | 171.64 ms | 17.84 | 3.80 | [144.00, 208.00] |
| 1 to 3 | 24 | 170.67 ms | 22.62 | 4.62 | [144.00, 208.00] |
| 1 to 4 | 22 | 173.64 ms | 17.96 | 3.83 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 14 | -5.05 µV | 1.82 | 0.49 | [-9.64, -2.66] |
| 1 to 2 | 22 | -5.81 µV | 2.14 | 0.46 | [-10.03, -2.38] |
| 1 to 3 | 24 | -6.24 µV | 2.69 | 0.55 | [-12.30, -1.95] |
| 1 to 4 | 22 | -6.86 µV | 2.94 | 0.63 | [-13.14, -2.87] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 17 | 114.12 ms | 12.26 | 2.97 | [84.00, 124.00] |
| 1 to 2 | 13 | 100.00 ms | 17.28 | 4.79 | [80.00, 124.00] |
| 1 to 3 | 12 | 97.67 ms | 16.49 | 4.76 | [80.00, 124.00] |
| 1 to 4 | 12 | 101.00 ms | 13.66 | 3.94 | [80.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 17 | 4.91 µV | 2.92 | 0.71 | [1.20, 13.50] |
| 1 to 2 | 13 | 2.33 µV | 1.29 | 0.36 | [0.71, 4.29] |
| 1 to 3 | 12 | 3.32 µV | 1.83 | 0.53 | [1.61, 7.47] |
| 1 to 4 | 12 | 3.98 µV | 1.62 | 0.47 | [1.16, 6.92] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 11 | 444.73 ms | 57.68 | 17.39 | [356.00, 532.00] |
| 1 to 2 | 15 | 443.73 ms | 53.40 | 13.79 | [368.00, 536.00] |
| 1 to 3 | 20 | 443.80 ms | 50.87 | 11.37 | [356.00, 516.00] |
| 1 to 4 | 20 | 461.80 ms | 57.09 | 12.77 | [376.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 11 | 4.43 µV | 1.78 | 0.54 | [2.13, 7.37] |
| 1 to 2 | 15 | 6.18 µV | 2.92 | 0.75 | [2.09, 11.99] |
| 1 to 3 | 20 | 6.51 µV | 3.59 | 0.80 | [1.71, 14.25] |
| 1 to 4 | 20 | 6.17 µV | 3.19 | 0.71 | [2.01, 13.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 389.29, BIC = 402.95
- **1 to 2 vs 1 to 1**: *β* = -1.26, *SE* = 3.376, *z* = -0.374, *p* = 0.709
- **1 to 3 vs 1 to 1**: *β* = 0.12, *SE* = 3.109, *z* = 0.040, *p* = 0.968
- **1 to 4 vs 1 to 1**: *β* = -1.34, *SE* = 3.213, *z* = -0.416, *p* = 0.677
- **SNR**: *β* = 0.94, *SE* = 0.787, *z* = 1.190, *p* = 0.234

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 1.26 | 3.38 | 0.37 | 0.709 | 0.996 | n.s. |
| 1 to 1 - 1 to 3 | -0.13 | 3.11 | -0.04 | 0.968 | 0.999 | n.s. |
| 1 to 1 - 1 to 4 | 1.34 | 3.21 | 0.42 | 0.677 | 0.996 | n.s. |
| 1 to 2 - 1 to 3 | -1.39 | 2.82 | -0.49 | 0.622 | 0.996 | n.s. |
| 1 to 2 - 1 to 4 | 0.08 | 3.05 | 0.02 | 0.980 | 0.999 | n.s. |
| 1 to 3 - 1 to 4 | 1.46 | 2.80 | 0.52 | 0.602 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.927, η²_G = 0.033
- Greenhouse-Geisser corrected: *p* = 0.739 (ε = 0.357)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -0.30 | 3 | = 0.903 | -0.29 [-1.20, 1.28] | small | n.s. |
| 1 to 1 vs 1 to 3 | -1.41 | 3 | = 0.782 | -0.41 [-0.80, 1.06] | small | n.s. |
| 1 to 1 vs 1 to 4 | -1.00 | 3 | = 0.782 | -0.09 [-0.92, 0.92] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | -0.13 | 3 | = 0.903 | -0.13 [-0.81, 0.54] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 0.21 | 3 | = 0.903 | 0.20 [-0.77, 0.91] | small | n.s. |
| 1 to 3 vs 1 to 4 | 1.00 | 3 | = 0.782 | 0.32 [-0.42, 1.05] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 173.93, BIC = 187.59
- **1 to 2 vs 1 to 1**: *β* = -0.32, *SE* = 0.425, *z* = -0.744, *p* = 0.457
- **1 to 3 vs 1 to 1**: *β* = -0.52, *SE* = 0.391, *z* = -1.337, *p* = 0.181
- **1 to 4 vs 1 to 1**: *β* = -0.42, *SE* = 0.407, *z* = -1.042, *p* = 0.297
- **SNR**: *β* = 0.92, *SE* = 0.099, *z* = 9.280, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 0.32 | 0.42 | 0.74 | 0.457 | 0.913 | n.s. |
| 1 to 1 - 1 to 3 | 0.52 | 0.39 | 1.34 | 0.181 | 0.699 | n.s. |
| 1 to 1 - 1 to 4 | 0.42 | 0.41 | 1.04 | 0.297 | 0.829 | n.s. |
| 1 to 2 - 1 to 3 | 0.21 | 0.36 | 0.58 | 0.565 | 0.917 | n.s. |
| 1 to 2 - 1 to 4 | 0.11 | 0.40 | 0.27 | 0.785 | 0.954 | n.s. |
| 1 to 3 - 1 to 4 | -0.10 | 0.36 | -0.27 | 0.785 | 0.954 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.60, *p* = 0.633, η²_G = 0.090
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -0.31 | 3 | = 0.895 | -0.20 [-1.08, 1.42] | small | n.s. |
| 1 to 1 vs 1 to 3 | -0.14 | 3 | = 0.895 | -0.10 [-1.18, 0.70] | negligible | n.s. |
| 1 to 1 vs 1 to 4 | 1.70 | 3 | = 0.755 | 0.76 [-0.60, 1.31] | medium | n.s. |
| 1 to 2 vs 1 to 3 | 0.76 | 3 | = 0.755 | 0.10 [-0.56, 0.78] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 1.04 | 3 | = 0.755 | 0.70 [-0.45, 1.29] | medium | n.s. |
| 1 to 3 vs 1 to 4 | 0.96 | 3 | = 0.755 | 0.67 [-0.76, 0.67] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 692.28, BIC = 709.12
- **1 to 2 vs 1 to 1**: *β* = -6.65, *SE* = 4.022, *z* = -1.654, *p* = 0.098
- **1 to 3 vs 1 to 1**: *β* = -6.85, *SE* = 3.986, *z* = -1.718, *p* = 0.086
- **1 to 4 vs 1 to 1**: *β* = -1.72, *SE* = 4.040, *z* = -0.425, *p* = 0.671
- **SNR**: *β* = 0.28, *SE* = 0.541, *z* = 0.523, *p* = 0.601

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 6.65 | 4.02 | 1.65 | 0.098 | 0.416 | n.s. |
| 1 to 1 - 1 to 3 | 6.85 | 3.99 | 1.72 | 0.086 | 0.416 | n.s. |
| 1 to 1 - 1 to 4 | 1.72 | 4.04 | 0.43 | 0.671 | 0.892 | n.s. |
| 1 to 2 - 1 to 3 | 0.19 | 3.37 | 0.06 | 0.954 | 0.954 | n.s. |
| 1 to 2 - 1 to 4 | -4.94 | 3.46 | -1.43 | 0.154 | 0.419 | n.s. |
| 1 to 3 - 1 to 4 | -5.13 | 3.36 | -1.53 | 0.127 | 0.419 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.254, η²_G = 0.035
- Greenhouse-Geisser corrected: *p* = 0.264 (ε = 0.580)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.33 | 11 | = 0.331 | 0.33 [-0.26, 0.99] | small | n.s. |
| 1 to 1 vs 1 to 3 | 1.30 | 11 | = 0.331 | 0.48 [-0.25, 0.94] | small | n.s. |
| 1 to 1 vs 1 to 4 | 0.44 | 11 | = 0.667 | 0.11 [-0.57, 0.64] | negligible | n.s. |
| 1 to 2 vs 1 to 3 | 0.76 | 11 | = 0.557 | 0.18 [-0.43, 0.45] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -1.69 | 11 | = 0.331 | -0.19 [-0.90, 0.08] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.46 | 11 | = 0.331 | -0.34 [-0.89, 0.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 343.05, BIC = 359.90
- **1 to 2 vs 1 to 1**: *β* = -0.80, *SE* = 0.531, *z* = -1.504, *p* = 0.133
- **1 to 3 vs 1 to 1**: *β* = -0.92, *SE* = 0.526, *z* = -1.750, *p* = 0.080
- **1 to 4 vs 1 to 1**: *β* = -1.55, *SE* = 0.532, *z* = -2.914, *p* = 0.004
- **SNR**: *β* = -0.40, *SE* = 0.067, *z* = -5.951, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 0.80 | 0.53 | 1.50 | 0.133 | 0.347 | n.s. |
| 1 to 1 - 1 to 3 | 0.92 | 0.53 | 1.75 | 0.080 | 0.341 | n.s. |
| 1 to 1 - 1 to 4 | 1.55 | 0.53 | 2.91 | 0.004 | 0.021 | * |
| 1 to 2 - 1 to 3 | 0.12 | 0.45 | 0.27 | 0.783 | 0.783 | n.s. |
| 1 to 2 - 1 to 4 | 0.75 | 0.46 | 1.65 | 0.099 | 0.342 | n.s. |
| 1 to 3 - 1 to 4 | 0.63 | 0.44 | 1.42 | 0.156 | 0.347 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.229, η²_G = 0.045
- Greenhouse-Geisser corrected: *p* = 0.246 (ε = 0.485)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.35 | 11 | = 0.427 | 0.49 [-0.20, 1.06] | small | n.s. |
| 1 to 1 vs 1 to 3 | 1.32 | 11 | = 0.427 | 0.54 [-0.14, 1.07] | medium | n.s. |
| 1 to 1 vs 1 to 4 | 1.39 | 11 | = 0.427 | 0.48 [-0.15, 1.13] | small | n.s. |
| 1 to 2 vs 1 to 3 | 0.90 | 11 | = 0.579 | 0.13 [-0.24, 0.66] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | 0.08 | 11 | = 0.937 | 0.01 [-0.13, 0.83] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -0.63 | 11 | = 0.653 | -0.12 [-0.29, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 450.96, BIC = 464.89
- **1 to 2 vs 1 to 1**: *β* = -13.50, *SE* = 5.128, *z* = -2.632, *p* = 0.008
- **1 to 3 vs 1 to 1**: *β* = -15.92, *SE* = 5.224, *z* = -3.047, *p* = 0.002
- **1 to 4 vs 1 to 1**: *β* = -13.96, *SE* = 5.263, *z* = -2.653, *p* = 0.008
- **SNR**: *β* = 2.33, *SE* = 1.237, *z* = 1.884, *p* = 0.060

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 13.50 | 5.13 | 2.63 | 0.008 | 0.039 | * |
| 1 to 1 - 1 to 3 | 15.92 | 5.22 | 3.05 | 0.002 | 0.014 | * |
| 1 to 1 - 1 to 4 | 13.96 | 5.26 | 2.65 | 0.008 | 0.039 | * |
| 1 to 2 - 1 to 3 | 2.42 | 5.57 | 0.44 | 0.664 | 0.962 | n.s. |
| 1 to 2 - 1 to 4 | 0.46 | 5.59 | 0.08 | 0.934 | 0.962 | n.s. |
| 1 to 3 - 1 to 4 | -1.96 | 5.73 | -0.34 | 0.732 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.479, η²_G = 0.199
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 1.71 | 3 | = 0.560 | 1.07 [-0.06, 1.73] | large | n.s. |
| 1 to 1 vs 1 to 3 | 1.10 | 3 | = 0.702 | 0.78 [-0.00, 1.65] | medium | n.s. |
| 1 to 1 vs 1 to 4 | 2.71 | 3 | = 0.438 | 1.27 [0.09, 1.81] | large | n.s. |
| 1 to 2 vs 1 to 3 | -0.33 | 3 | = 0.893 | -0.28 [-0.79, 0.88] | small | n.s. |
| 1 to 2 vs 1 to 4 | 0.15 | 3 | = 0.893 | 0.11 [-0.98, 0.70] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | 0.47 | 3 | = 0.893 | 0.40 [-0.77, 1.38] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 217.70, BIC = 231.62
- **1 to 2 vs 1 to 1**: *β* = -2.37, *SE* = 0.553, *z* = -4.290, *p* < .001
- **1 to 3 vs 1 to 1**: *β* = -1.43, *SE* = 0.560, *z* = -2.558, *p* = 0.011
- **1 to 4 vs 1 to 1**: *β* = -1.18, *SE* = 0.559, *z* = -2.105, *p* = 0.035
- **SNR**: *β* = 0.76, *SE* = 0.144, *z* = 5.244, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 2.37 | 0.55 | 4.29 | < .001 | < .001 | *** |
| 1 to 1 - 1 to 3 | 1.43 | 0.56 | 2.56 | 0.011 | 0.052 | n.s. |
| 1 to 1 - 1 to 4 | 1.18 | 0.56 | 2.11 | 0.035 | 0.134 | n.s. |
| 1 to 2 - 1 to 3 | -0.94 | 0.59 | -1.59 | 0.113 | 0.213 | n.s. |
| 1 to 2 - 1 to 4 | -1.20 | 0.60 | -1.99 | 0.046 | 0.134 | n.s. |
| 1 to 3 - 1 to 4 | -0.26 | 0.62 | -0.41 | 0.680 | 0.680 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.11, *p* = 0.003, η²_G = 0.508
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 3.56 | 3 | = 0.077 | 1.79 [0.07, 1.97] | large | n.s. |
| 1 to 1 vs 1 to 3 | 3.19 | 3 | = 0.077 | 1.62 [-0.12, 1.46] | large | n.s. |
| 1 to 1 vs 1 to 4 | 2.37 | 3 | = 0.118 | 0.90 [-0.20, 1.35] | large | n.s. |
| 1 to 2 vs 1 to 3 | -0.89 | 3 | = 0.440 | -0.41 [-1.26, 0.48] | small | n.s. |
| 1 to 2 vs 1 to 4 | -4.87 | 3 | = 0.077 | -1.60 [-2.34, -0.12] | large | n.s. |
| 1 to 3 vs 1 to 4 | -3.15 | 3 | = 0.077 | -1.29 [-1.32, 0.81] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 723.43, BIC = 738.76
- **1 to 2 vs 1 to 1**: *β* = -4.63, *SE* = 20.771, *z* = -0.223, *p* = 0.824
- **1 to 3 vs 1 to 1**: *β* = -5.77, *SE* = 20.402, *z* = -0.283, *p* = 0.777
- **1 to 4 vs 1 to 1**: *β* = 12.42, *SE* = 20.280, *z* = 0.612, *p* = 0.540
- **SNR**: *β* = 1.27, *SE* = 2.584, *z* = 0.494, *p* = 0.622

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | 4.63 | 20.77 | 0.22 | 0.824 | 0.989 | n.s. |
| 1 to 1 - 1 to 3 | 5.77 | 20.40 | 0.28 | 0.777 | 0.989 | n.s. |
| 1 to 1 - 1 to 4 | -12.42 | 20.28 | -0.61 | 0.540 | 0.955 | n.s. |
| 1 to 2 - 1 to 3 | 1.14 | 17.00 | 0.07 | 0.947 | 0.989 | n.s. |
| 1 to 2 - 1 to 4 | -17.05 | 16.91 | -1.01 | 0.313 | 0.847 | n.s. |
| 1 to 3 - 1 to 4 | -18.19 | 15.51 | -1.17 | 0.241 | 0.809 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.927, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | 0.07 | 8 | = 0.986 | 0.02 [-0.74, 0.79] | negligible | n.s. |
| 1 to 1 vs 1 to 3 | 0.05 | 8 | = 0.986 | 0.02 [-0.46, 0.90] | negligible | n.s. |
| 1 to 1 vs 1 to 4 | -0.50 | 8 | = 0.986 | -0.20 [-0.99, 0.39] | small | n.s. |
| 1 to 2 vs 1 to 3 | -0.02 | 8 | = 0.986 | -0.01 [-0.69, 0.47] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.58 | 8 | = 0.986 | -0.20 [-0.72, 0.39] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.63 | 8 | = 0.986 | -0.23 [-0.81, 0.18] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 287.84, BIC = 303.16
- **1 to 2 vs 1 to 1**: *β* = 0.60, *SE* = 0.670, *z* = 0.893, *p* = 0.372
- **1 to 3 vs 1 to 1**: *β* = 0.82, *SE* = 0.685, *z* = 1.192, *p* = 0.233
- **1 to 4 vs 1 to 1**: *β* = 0.60, *SE* = 0.676, *z* = 0.889, *p* = 0.374
- **SNR**: *β* = 0.60, *SE* = 0.094, *z* = 6.440, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | -0.60 | 0.67 | -0.89 | 0.372 | 0.902 | n.s. |
| 1 to 1 - 1 to 3 | -0.82 | 0.68 | -1.19 | 0.233 | 0.797 | n.s. |
| 1 to 1 - 1 to 4 | -0.60 | 0.68 | -0.89 | 0.374 | 0.902 | n.s. |
| 1 to 2 - 1 to 3 | -0.22 | 0.54 | -0.40 | 0.688 | 0.959 | n.s. |
| 1 to 2 - 1 to 4 | -0.00 | 0.53 | -0.01 | 0.996 | 0.996 | n.s. |
| 1 to 3 - 1 to 4 | 0.21 | 0.48 | 0.45 | 0.656 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.44, *p* = 0.013, η²_G = 0.182
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 1 to 2 | -2.12 | 8 | = 0.133 | -0.75 [-1.57, 0.15] | medium | n.s. |
| 1 to 1 vs 1 to 3 | -2.66 | 8 | = 0.086 | -1.24 [-1.63, -0.06] | large | n.s. |
| 1 to 1 vs 1 to 4 | -2.86 | 8 | = 0.086 | -1.16 [-1.87, -0.20] | large | n.s. |
| 1 to 2 vs 1 to 3 | -1.34 | 8 | = 0.271 | -0.48 [-0.98, 0.22] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.31 | 8 | = 0.271 | -0.36 [-0.82, 0.31] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.56 | 8 | = 0.593 | 0.13 [-0.33, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.003) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.013) (no significant pairwise comparisons)

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
