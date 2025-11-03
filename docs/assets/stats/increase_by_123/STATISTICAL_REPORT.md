# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:41:46

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| Increase by 1 | 7 | 100.00 ms | 10.07 | 3.80 | [88.00, 108.00] |
| Increase by 2 | 10 | 100.80 ms | 9.58 | 3.03 | [88.00, 108.00] |
| Increase by 3 | 9 | 98.22 ms | 9.61 | 3.20 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 7 | 1.19 µV | 0.63 | 0.24 | [0.54, 2.00] |
| Increase by 2 | 10 | 1.35 µV | 0.67 | 0.21 | [0.24, 2.31] |
| Increase by 3 | 9 | 1.76 µV | 0.92 | 0.31 | [0.47, 2.87] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 23 | 169.22 ms | 19.35 | 4.03 | [136.00, 208.00] |
| Increase by 2 | 24 | 168.17 ms | 19.96 | 4.08 | [136.00, 208.00] |
| Increase by 3 | 23 | 168.87 ms | 19.11 | 3.98 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 23 | -5.11 µV | 2.18 | 0.45 | [-9.51, -1.04] |
| Increase by 2 | 24 | -5.43 µV | 2.36 | 0.48 | [-10.65, -0.86] |
| Increase by 3 | 23 | -6.15 µV | 2.47 | 0.51 | [-12.86, -1.94] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 13 | 98.15 ms | 8.89 | 2.46 | [84.00, 108.00] |
| Increase by 2 | 15 | 99.20 ms | 10.16 | 2.62 | [80.00, 108.00] |
| Increase by 3 | 12 | 97.00 ms | 11.20 | 3.23 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 13 | 1.88 µV | 1.08 | 0.30 | [0.63, 3.90] |
| Increase by 2 | 15 | 1.71 µV | 1.24 | 0.32 | [0.36, 4.70] |
| Increase by 3 | 12 | 2.29 µV | 1.44 | 0.42 | [0.51, 5.72] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 16 | 481.50 ms | 45.51 | 11.38 | [392.00, 532.00] |
| Increase by 2 | 18 | 472.67 ms | 37.63 | 8.87 | [392.00, 528.00] |
| Increase by 3 | 19 | 468.84 ms | 42.64 | 9.78 | [400.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 | 16 | 4.17 µV | 2.54 | 0.63 | [0.78, 8.79] |
| Increase by 2 | 18 | 5.22 µV | 2.59 | 0.61 | [1.07, 9.72] |
| Increase by 3 | 19 | 4.60 µV | 2.38 | 0.55 | [1.27, 9.96] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 194.45, BIC = 202.00
- **Increase by 2 vs Increase by 1**: *β* = -3.76, *SE* = 4.202, *z* = -0.895, *p* = 0.371
- **Increase by 3 vs Increase by 1**: *β* = -4.19, *SE* = 3.726, *z* = -1.126, *p* = 0.260
- **SNR**: *β* = -1.83, *SE* = 1.401, *z* = -1.310, *p* = 0.190

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 3.76 | 4.20 | 0.89 | 0.371 | 0.604 | n.s. |
| Increase by 1 - Increase by 3 | 4.19 | 3.73 | 1.13 | 0.260 | 0.595 | n.s. |
| Increase by 2 - Increase by 3 | 0.43 | 3.09 | 0.14 | 0.888 | 0.888 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.00 | 1 | = 0.500 | 1.00 [-2.05, 4.36] | large | n.s. |
| Increase by 1 vs Increase by 3 | 1.00 | 1 | = 0.500 | 1.00 [-1.11, 2.37] | large | n.s. |
| Increase by 2 vs Increase by 3 | nan | 1 | n/a | 0.00 | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 53.34, BIC = 60.89
- **Increase by 2 vs Increase by 1**: *β* = 0.41, *SE* = 0.188, *z* = 2.173, *p* = 0.030
- **Increase by 3 vs Increase by 1**: *β* = 0.41, *SE* = 0.185, *z* = 2.228, *p* = 0.026
- **SNR**: *β* = 0.39, *SE* = 0.092, *z* = 4.274, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.41 | 0.19 | -2.17 | 0.030 | 0.076 | n.s. |
| Increase by 1 - Increase by 3 | -0.41 | 0.18 | -2.23 | 0.026 | 0.076 | n.s. |
| Increase by 2 - Increase by 3 | -0.00 | 0.15 | -0.02 | 0.988 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -1.31 | 1 | = 0.721 | -0.75 [-3.08, 2.15] | medium | n.s. |
| Increase by 1 vs Increase by 3 | -0.76 | 1 | = 0.721 | -0.18 [-2.96, 0.95] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | 0.47 | 1 | = 0.721 | 0.33 [-0.74, 1.42] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 560.13, BIC = 573.62
- **Increase by 2 vs Increase by 1**: *β* = -3.40, *SE* = 2.294, *z* = -1.484, *p* = 0.138
- **Increase by 3 vs Increase by 1**: *β* = -1.65, *SE* = 2.315, *z* = -0.713, *p* = 0.476
- **SNR**: *β* = -0.56, *SE* = 0.291, *z* = -1.911, *p* = 0.056

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 3.41 | 2.29 | 1.48 | 0.138 | 0.359 | n.s. |
| Increase by 1 - Increase by 3 | 1.65 | 2.32 | 0.71 | 0.476 | 0.672 | n.s. |
| Increase by 2 - Increase by 3 | -1.75 | 2.21 | -0.79 | 0.428 | 0.672 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.64, *p* = 0.530, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.02 | 22 | = 0.477 | 0.13 [-0.22, 0.65] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 0.13 | 22 | = 0.894 | 0.02 [-0.40, 0.46] | negligible | n.s. |
| Increase by 2 vs Increase by 3 | -1.07 | 22 | = 0.477 | -0.11 [-0.66, 0.21] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 266.63, BIC = 280.12
- **Increase by 2 vs Increase by 1**: *β* = -0.59, *SE* = 0.305, *z* = -1.937, *p* = 0.053
- **Increase by 3 vs Increase by 1**: *β* = -1.31, *SE* = 0.308, *z* = -4.239, *p* < .001
- **SNR**: *β* = -0.11, *SE* = 0.039, *z* = -2.930, *p* = 0.003

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 0.59 | 0.31 | 1.94 | 0.053 | 0.053 | n.s. |
| Increase by 1 - Increase by 3 | 1.31 | 0.31 | 4.24 | < .001 | < .001 | *** |
| Increase by 2 - Increase by 3 | 0.71 | 0.29 | 2.43 | 0.015 | 0.030 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.71, *p* = 0.006, η²_G = 0.034
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.16 | 22 | = 0.258 | 0.15 [-0.20, 0.68] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 3.15 | 22 | = 0.014 | 0.45 [0.18, 1.13] | small | * |
| Increase by 2 vs Increase by 3 | 2.27 | 22 | = 0.050 | 0.28 [0.02, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 286.28, BIC = 296.41
- **Increase by 2 vs Increase by 1**: *β* = -3.08, *SE* = 2.057, *z* = -1.499, *p* = 0.134
- **Increase by 3 vs Increase by 1**: *β* = -4.24, *SE* = 1.988, *z* = -2.133, *p* = 0.033
- **SNR**: *β* = -0.05, *SE* = 0.914, *z* = -0.055, *p* = 0.956

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 3.08 | 2.06 | 1.50 | 0.134 | 0.250 | n.s. |
| Increase by 1 - Increase by 3 | 4.24 | 1.99 | 2.13 | 0.033 | 0.096 | n.s. |
| Increase by 2 - Increase by 3 | 1.16 | 1.95 | 0.59 | 0.553 | 0.553 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.275, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 1.26 | 7 | = 0.374 | 0.27 [-0.26, 1.39] | small | n.s. |
| Increase by 1 vs Increase by 3 | 1.66 | 7 | = 0.374 | 0.30 [-0.16, 1.56] | small | n.s. |
| Increase by 2 vs Increase by 3 | 0.26 | 7 | = 0.802 | 0.05 [-0.43, 0.94] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 90.85, BIC = 100.98
- **Increase by 2 vs Increase by 1**: *β* = 0.43, *SE* = 0.202, *z* = 2.151, *p* = 0.032
- **Increase by 3 vs Increase by 1**: *β* = 0.61, *SE* = 0.207, *z* = 2.950, *p* = 0.003
- **SNR**: *β* = 0.51, *SE* = 0.084, *z* = 5.998, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.43 | 0.20 | -2.15 | 0.032 | 0.062 | n.s. |
| Increase by 1 - Increase by 3 | -0.61 | 0.21 | -2.95 | 0.003 | 0.009 | ** |
| Increase by 2 - Increase by 3 | -0.18 | 0.19 | -0.92 | 0.360 | 0.360 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.90, *p* = 0.005, η²_G = 0.099
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -0.70 | 7 | = 0.507 | -0.15 [-1.02, 0.54] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | -3.23 | 7 | = 0.022 | -0.79 [-2.29, -0.23] | medium | * |
| Increase by 2 vs Increase by 3 | -4.25 | 7 | = 0.011 | -0.51 [-1.28, 0.16] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 554.78, BIC = 566.61
- **Increase by 2 vs Increase by 1**: *β* = -8.82, *SE* = 13.385, *z* = -0.659, *p* = 0.510
- **Increase by 3 vs Increase by 1**: *β* = -12.47, *SE* = 13.140, *z* = -0.949, *p* = 0.342
- **SNR**: *β* = -0.11, *SE* = 1.210, *z* = -0.092, *p* = 0.927

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | 8.82 | 13.39 | 0.66 | 0.510 | 0.760 | n.s. |
| Increase by 1 - Increase by 3 | 12.47 | 13.14 | 0.95 | 0.342 | 0.716 | n.s. |
| Increase by 2 - Increase by 3 | 3.66 | 12.95 | 0.28 | 0.778 | 0.778 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.02, *p* = 0.374, η²_G = 0.034
- Greenhouse-Geisser corrected: *p* = 0.356 (ε = 0.741)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | 0.23 | 15 | = 0.825 | 0.08 [-0.48, 0.59] | negligible | n.s. |
| Increase by 1 vs Increase by 3 | 1.14 | 15 | = 0.408 | 0.39 [-0.26, 0.83] | small | n.s. |
| Increase by 2 vs Increase by 3 | 1.69 | 15 | = 0.335 | 0.38 [-0.50, 0.50] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 199.66, BIC = 211.48
- **Increase by 2 vs Increase by 1**: *β* = 0.97, *SE* = 0.353, *z* = 2.762, *p* = 0.006
- **Increase by 3 vs Increase by 1**: *β* = 0.82, *SE* = 0.335, *z* = 2.443, *p* = 0.015
- **SNR**: *β* = 0.19, *SE* = 0.053, *z* = 3.535, *p* < .001

_Reference condition: **Increase by 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 - Increase by 2 | -0.97 | 0.35 | -2.76 | 0.006 | 0.017 | * |
| Increase by 1 - Increase by 3 | -0.82 | 0.33 | -2.44 | 0.015 | 0.029 | * |
| Increase by 2 - Increase by 3 | 0.16 | 0.34 | 0.46 | 0.643 | 0.643 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.80, *p* = 0.004, η²_G = 0.052
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 vs Increase by 2 | -3.48 | 15 | = 0.010 | -0.53 [-1.49, -0.24] | medium | * |
| Increase by 1 vs Increase by 3 | -2.59 | 15 | = 0.031 | -0.37 [-1.23, -0.06] | small | * |
| Increase by 2 vs Increase by 3 | 1.17 | 15 | = 0.261 | 0.18 [-0.17, 0.85] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.006). Post-hoc tests revealed:
  - Increase by 1 showed greater amplitude than Increase by 3 (*d* = 0.45)
**P1 amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - Increase by 1 showed smaller amplitude than Increase by 3 (*d* = -0.79)
  - Increase by 2 showed smaller amplitude than Increase by 3 (*d* = -0.51)
**P3b amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Increase by 1 showed smaller amplitude than Increase by 2 (*d* = -0.53)
  - Increase by 1 showed smaller amplitude than Increase by 3 (*d* = -0.37)

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
