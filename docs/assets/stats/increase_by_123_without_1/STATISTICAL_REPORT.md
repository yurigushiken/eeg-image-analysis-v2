# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:42:05

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
| Increase by 1 (no 1) | 7 | 96.57 ms | 10.69 | 4.04 | [88.00, 108.00] |
| Increase by 2 (no 1) | 9 | 99.56 ms | 10.09 | 3.36 | [88.00, 108.00] |
| Increase by 3 (no 1) | 11 | 96.00 ms | 9.63 | 2.90 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 7 | 1.18 µV | 0.62 | 0.24 | [0.52, 2.15] |
| Increase by 2 (no 1) | 9 | 1.28 µV | 0.69 | 0.23 | [0.48, 2.52] |
| Increase by 3 (no 1) | 11 | 1.65 µV | 0.90 | 0.27 | [0.21, 3.46] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 23 | 169.04 ms | 19.04 | 3.97 | [136.00, 208.00] |
| Increase by 2 (no 1) | 23 | 168.00 ms | 18.13 | 3.78 | [136.00, 200.00] |
| Increase by 3 (no 1) | 23 | 168.35 ms | 19.56 | 4.08 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 23 | -5.20 µV | 2.17 | 0.45 | [-9.40, -0.93] |
| Increase by 2 (no 1) | 23 | -5.49 µV | 2.46 | 0.51 | [-10.89, -2.86] |
| Increase by 3 (no 1) | 23 | -6.18 µV | 2.45 | 0.51 | [-13.18, -2.28] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 15 | 99.20 ms | 8.44 | 2.18 | [80.00, 108.00] |
| Increase by 2 (no 1) | 16 | 99.00 ms | 9.63 | 2.41 | [80.00, 108.00] |
| Increase by 3 (no 1) | 12 | 95.00 ms | 10.80 | 3.12 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 15 | 1.78 µV | 1.26 | 0.32 | [0.51, 4.01] |
| Increase by 2 (no 1) | 16 | 1.87 µV | 1.23 | 0.31 | [0.30, 4.54] |
| Increase by 3 (no 1) | 12 | 2.81 µV | 2.25 | 0.65 | [0.54, 9.07] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 487.75 ms | 41.71 | 10.43 | [408.00, 532.00] |
| Increase by 2 (no 1) | 17 | 479.76 ms | 40.36 | 9.79 | [408.00, 532.00] |
| Increase by 3 (no 1) | 21 | 464.76 ms | 39.16 | 8.55 | [408.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 4.21 µV | 2.61 | 0.65 | [0.98, 8.98] |
| Increase by 2 (no 1) | 17 | 5.52 µV | 2.53 | 0.61 | [1.49, 10.75] |
| Increase by 3 (no 1) | 21 | 4.43 µV | 2.22 | 0.48 | [1.74, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 198.50, BIC = 206.27
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -2.56, *SE* = 2.692, *z* = -0.949, *p* = 0.342
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.06, *SE* = 2.342, *z* = 0.027, *p* = 0.979
- **SNR**: *β* = -0.97, *SE* = 1.085, *z* = -0.894, *p* = 0.371

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 2.56 | 2.69 | 0.95 | 0.342 | 0.678 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.06 | 2.34 | -0.03 | 0.979 | 0.979 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -2.62 | 2.60 | -1.01 | 0.314 | 0.678 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.32, *p* = 0.363, η²_G = 0.183
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 1.00 | 2 | = 0.423 | 0.82 [-1.19, 2.19] | large | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.00 | 2 | = 0.423 | -0.12 [-1.50, 0.68] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -1.31 | 2 | = 0.423 | -1.07 [-1.89, 0.78] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 59.07, BIC = 66.85
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.23, *SE* = 0.244, *z* = 0.938, *p* = 0.348
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.45, *SE* = 0.223, *z* = 1.995, *p* = 0.046
- **SNR**: *β* = 0.43, *SE* = 0.101, *z* = 4.303, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.23 | 0.24 | -0.94 | 0.348 | 0.553 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.45 | 0.22 | -1.99 | 0.046 | 0.132 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.22 | 0.22 | -0.97 | 0.331 | 0.553 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.862, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.59 | 2 | = 0.841 | -0.54 [-1.84, 1.39] | medium | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.23 | 2 | = 0.841 | -0.09 [-1.56, 0.64] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.30 | 2 | = 0.841 | 0.27 [-1.48, 1.03] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 567.90, BIC = 581.31
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.62, *SE* = 2.727, *z* = -0.229, *p* = 0.819
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -1.07, *SE* = 2.712, *z* = -0.396, *p* = 0.692
- **SNR**: *β* = -0.40, *SE* = 0.386, *z* = -1.043, *p* = 0.297

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.62 | 2.73 | 0.23 | 0.819 | 0.971 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.07 | 2.71 | 0.40 | 0.692 | 0.971 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.45 | 2.73 | 0.16 | 0.869 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.965, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.19 | 21 | = 0.951 | 0.03 [-0.40, 0.48] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.27 | 21 | = 0.951 | 0.04 [-0.38, 0.49] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.06 | 21 | = 0.951 | 0.01 [-0.43, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 277.62, BIC = 291.03
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.24, *SE* = 0.358, *z* = -0.685, *p* = 0.493
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -1.13, *SE* = 0.356, *z* = -3.173, *p* = 0.002
- **SNR**: *β* = -0.15, *SE* = 0.052, *z* = -2.934, *p* = 0.003

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.25 | 0.36 | 0.69 | 0.493 | 0.493 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.13 | 0.36 | 3.17 | 0.002 | 0.005 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.89 | 0.36 | 2.47 | 0.013 | 0.027 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.76, *p* = 0.031, η²_G = 0.035
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.41 | 21 | = 0.683 | 0.07 [-0.36, 0.53] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.55 | 21 | = 0.056 | 0.44 [0.10, 1.03] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.19 | 21 | = 0.060 | 0.33 [-0.00, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.01, BIC = 312.58
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -2.59, *SE* = 1.735, *z* = -1.494, *p* = 0.135
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -5.43, *SE* = 1.767, *z* = -3.071, *p* = 0.002
- **SNR**: *β* = 0.87, *SE* = 0.758, *z* = 1.144, *p* = 0.253

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 2.59 | 1.74 | 1.49 | 0.135 | 0.220 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 5.43 | 1.77 | 3.07 | 0.002 | 0.006 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 2.83 | 1.81 | 1.57 | 0.117 | 0.220 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.235, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.00 | 6 | = 1.000 | 0.00 [-0.43, 1.04] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.44 | 6 | = 0.299 | 0.35 [-0.01, 1.64] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.69 | 6 | = 0.299 | 0.41 [-0.20, 1.49] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 114.79, BIC = 125.36
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.19, *SE* = 0.230, *z* = 0.816, *p* = 0.415
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.89, *SE* = 0.237, *z* = 3.767, *p* < .001
- **SNR**: *β* = 0.81, *SE* = 0.092, *z* = 8.832, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.19 | 0.23 | -0.82 | 0.415 | 0.415 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.89 | 0.24 | -3.77 | < .001 | < .001 | *** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.70 | 0.24 | -2.93 | 0.003 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.18, *p* = 0.341, η²_G = 0.048
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.20 | 6 | = 0.412 | -0.29 [-0.89, 0.55] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.36 | 6 | = 0.412 | -0.46 [-1.54, 0.07] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.76 | 6 | = 0.476 | -0.27 [-0.99, 0.57] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 558.79, BIC = 570.73
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -8.34, *SE* = 12.263, *z* = -0.680, *p* = 0.497
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -22.17, *SE* = 11.697, *z* = -1.895, *p* = 0.058
- **SNR**: *β* = 0.72, *SE* = 1.500, *z* = 0.482, *p* = 0.630

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 8.34 | 12.26 | 0.68 | 0.497 | 0.497 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 22.17 | 11.70 | 1.90 | 0.058 | 0.164 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 13.83 | 11.96 | 1.16 | 0.247 | 0.434 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.79, *p* = 0.186, η²_G = 0.060
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 1.13 | 14 | = 0.321 | 0.26 [-0.27, 0.86] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.59 | 14 | = 0.321 | 0.60 [-0.20, 0.90] | medium | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.03 | 14 | = 0.321 | 0.35 [-0.16, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 209.61, BIC = 221.55
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 1.00, *SE* = 0.412, *z* = 2.442, *p* = 0.015
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.91, *SE* = 0.387, *z* = 2.357, *p* = 0.018
- **SNR**: *β* = 0.31, *SE* = 0.069, *z* = 4.512, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -1.01 | 0.41 | -2.44 | 0.015 | 0.043 | * |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.91 | 0.39 | -2.36 | 0.018 | 0.043 | * |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.09 | 0.40 | 0.23 | 0.817 | 0.817 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.44, *p* = 0.010, η²_G = 0.074
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -4.00 | 14 | = 0.004 | -0.62 [-1.72, -0.35] | medium | ** |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -2.02 | 14 | = 0.095 | -0.40 [-1.08, 0.05] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.12 | 14 | = 0.281 | 0.28 [-0.24, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.031) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -0.62)

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
