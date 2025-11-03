# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:31:58

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
| Decrease by 1 | 12 | 107.33 ms | 13.63 | 3.93 | [92.00, 120.00] |
| Decrease by 2 | 5 | 107.20 ms | 14.25 | 6.37 | [92.00, 120.00] |
| Decrease by 3 | 6 | 112.00 ms | 9.12 | 3.72 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 12 | 1.69 µV | 0.76 | 0.22 | [0.59, 2.87] |
| Decrease by 2 | 5 | 2.37 µV | 1.78 | 0.80 | [0.32, 4.54] |
| Decrease by 3 | 6 | 1.97 µV | 0.63 | 0.26 | [1.23, 2.86] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | 178.17 ms | 15.47 | 3.16 | [148.00, 208.00] |
| Decrease by 2 | 24 | 177.67 ms | 14.44 | 2.95 | [148.00, 208.00] |
| Decrease by 3 | 24 | 177.67 ms | 14.59 | 2.98 | [156.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 24 | -4.83 µV | 2.03 | 0.41 | [-9.17, -1.44] |
| Decrease by 2 | 24 | -4.93 µV | 2.02 | 0.41 | [-9.37, -1.43] |
| Decrease by 3 | 24 | -5.07 µV | 1.98 | 0.40 | [-8.57, -1.48] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 13 | 112.92 ms | 7.33 | 2.03 | [100.00, 124.00] |
| Decrease by 2 | 17 | 115.53 ms | 7.47 | 1.81 | [104.00, 124.00] |
| Decrease by 3 | 17 | 115.29 ms | 7.51 | 1.82 | [104.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 13 | 2.37 µV | 2.00 | 0.56 | [0.38, 5.89] |
| Decrease by 2 | 17 | 2.50 µV | 1.38 | 0.33 | [0.64, 5.51] |
| Decrease by 3 | 17 | 2.92 µV | 1.87 | 0.45 | [0.87, 8.21] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 18 | 488.00 ms | 31.62 | 7.45 | [436.00, 528.00] |
| Decrease by 2 | 19 | 473.26 ms | 24.22 | 5.56 | [440.00, 536.00] |
| Decrease by 3 | 20 | 480.20 ms | 32.46 | 7.26 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 18 | 4.69 µV | 2.34 | 0.55 | [1.85, 8.87] |
| Decrease by 2 | 19 | 4.68 µV | 2.15 | 0.49 | [1.58, 8.53] |
| Decrease by 3 | 20 | 5.11 µV | 3.11 | 0.69 | [0.66, 12.38] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 189.44, BIC = 196.26
- **Decrease by 2 vs Decrease by 1**: *β* = -0.50, *SE* = 5.294, *z* = -0.094, *p* = 0.925
- **Decrease by 3 vs Decrease by 1**: *β* = 3.65, *SE* = 5.078, *z* = 0.718, *p* = 0.473
- **SNR**: *β* = -0.09, *SE* = 1.435, *z* = -0.063, *p* = 0.950

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.50 | 5.29 | 0.09 | 0.925 | 0.925 | n.s. |
| Decrease by 1 - Decrease by 3 | -3.65 | 5.08 | -0.72 | 0.473 | 0.853 | n.s. |
| Decrease by 2 - Decrease by 3 | -4.14 | 6.18 | -0.67 | 0.502 | 0.853 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -1.00 | 1 | = 0.500 | -0.63 [-1.44, 1.77] | medium | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.00 | 1 | = 0.500 | -0.28 [-2.60, 1.04] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | 1.00 | 1 | = 0.500 | 0.45 [-9.34, 10.75] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 62.33, BIC = 69.14
- **Decrease by 2 vs Decrease by 1**: *β* = 0.58, *SE* = 0.270, *z* = 2.166, *p* = 0.030
- **Decrease by 3 vs Decrease by 1**: *β* = 0.22, *SE* = 0.262, *z* = 0.824, *p* = 0.410
- **SNR**: *β* = 0.32, *SE* = 0.072, *z* = 4.449, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.59 | 0.27 | -2.17 | 0.030 | 0.088 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.22 | 0.26 | -0.82 | 0.410 | 0.436 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.37 | 0.32 | 1.15 | 0.249 | 0.436 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.77 | 1 | = 0.872 | -0.39 [-2.07, 1.24] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.00 | 1 | = 0.872 | -0.81 [-2.16, 1.20] | large | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.07 | 1 | = 0.957 | 0.06 [-8.94, 9.04] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 568.35, BIC = 582.01
- **Decrease by 2 vs Decrease by 1**: *β* = -0.50, *SE* = 2.392, *z* = -0.209, *p* = 0.834
- **Decrease by 3 vs Decrease by 1**: *β* = -0.51, *SE* = 2.393, *z* = -0.212, *p* = 0.832
- **SNR**: *β* = 0.03, *SE* = 0.261, *z* = 0.103, *p* = 0.918

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.50 | 2.39 | 0.21 | 0.834 | 0.995 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.51 | 2.39 | 0.21 | 0.832 | 0.995 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.01 | 2.39 | 0.00 | 0.997 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.03, *p* = 0.973, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.30 | 23 | = 1.000 | 0.03 [-0.36, 0.48] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.18 | 23 | = 1.000 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 249.08, BIC = 262.74
- **Decrease by 2 vs Decrease by 1**: *β* = -0.09, *SE* = 0.241, *z* = -0.392, *p* = 0.695
- **Decrease by 3 vs Decrease by 1**: *β* = -0.20, *SE* = 0.241, *z* = -0.815, *p* = 0.415
- **SNR**: *β* = -0.11, *SE* = 0.027, *z* = -4.229, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.09 | 0.24 | 0.39 | 0.695 | 0.892 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.20 | 0.24 | 0.82 | 0.415 | 0.800 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.10 | 0.24 | 0.42 | 0.672 | 0.892 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.706, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.35 | 23 | = 0.726 | 0.05 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.78 | 23 | = 0.726 | 0.12 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.52 | 23 | = 0.726 | 0.07 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 309.80, BIC = 320.90
- **Decrease by 2 vs Decrease by 1**: *β* = 3.08, *SE* = 1.520, *z* = 2.025, *p* = 0.043
- **Decrease by 3 vs Decrease by 1**: *β* = 3.38, *SE* = 1.551, *z* = 2.181, *p* = 0.029
- **SNR**: *β* = 0.23, *SE* = 0.252, *z* = 0.926, *p* = 0.355

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -3.08 | 1.52 | -2.02 | 0.043 | 0.085 | n.s. |
| Decrease by 1 - Decrease by 3 | -3.38 | 1.55 | -2.18 | 0.029 | 0.085 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.30 | 1.40 | -0.22 | 0.828 | 0.828 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.75, *p* = 0.041, η²_G = 0.046
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -1.90 | 10 | = 0.131 | -0.38 [-1.31, 0.08] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.19 | 10 | = 0.131 | -0.49 [-1.40, 0.08] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.80 | 10 | = 0.441 | -0.10 [-0.64, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 155.08, BIC = 166.18
- **Decrease by 2 vs Decrease by 1**: *β* = 0.47, *SE* = 0.321, *z* = 1.471, *p* = 0.141
- **Decrease by 3 vs Decrease by 1**: *β* = 0.84, *SE* = 0.326, *z* = 2.565, *p* = 0.010
- **SNR**: *β* = 0.25, *SE* = 0.058, *z* = 4.351, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.47 | 0.32 | -1.47 | 0.141 | 0.262 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.84 | 0.33 | -2.57 | 0.010 | 0.031 | * |
| Decrease by 2 - Decrease by 3 | -0.36 | 0.29 | -1.24 | 0.216 | 0.262 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.88, *p* = 0.179, η²_G = 0.039
- Greenhouse-Geisser corrected: *p* = 0.195 (ε = 0.665)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -1.04 | 10 | = 0.484 | -0.30 [-0.95, 0.35] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -3.47 | 10 | = 0.018 | -0.42 [-1.88, -0.21] | small | * |
| Decrease by 2 vs Decrease by 3 | -0.64 | 10 | = 0.536 | -0.20 [-0.79, 0.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 548.17, BIC = 560.43
- **Decrease by 2 vs Decrease by 1**: *β* = -16.75, *SE* = 7.138, *z* = -2.347, *p* = 0.019
- **Decrease by 3 vs Decrease by 1**: *β* = -12.24, *SE* = 7.153, *z* = -1.711, *p* = 0.087
- **SNR**: *β* = -0.21, *SE* = 0.818, *z* = -0.256, *p* = 0.798

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 16.76 | 7.14 | 2.35 | 0.019 | 0.056 | n.s. |
| Decrease by 1 - Decrease by 3 | 12.24 | 7.15 | 1.71 | 0.087 | 0.166 | n.s. |
| Decrease by 2 - Decrease by 3 | -4.52 | 6.98 | -0.65 | 0.518 | 0.518 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.64, *p* = 0.038, η²_G = 0.081
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 2.64 | 16 | = 0.054 | 0.66 [0.08, 1.20] | medium | n.s. |
| Decrease by 1 vs Decrease by 3 | 1.98 | 16 | = 0.098 | 0.55 [-0.06, 1.02] | medium | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.17 | 16 | = 0.867 | -0.04 [-0.55, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 228.52, BIC = 240.78
- **Decrease by 2 vs Decrease by 1**: *β* = 0.35, *SE* = 0.364, *z* = 0.952, *p* = 0.341
- **Decrease by 3 vs Decrease by 1**: *β* = 0.79, *SE* = 0.361, *z* = 2.198, *p* = 0.028
- **SNR**: *β* = 0.18, *SE* = 0.051, *z* = 3.429, *p* = 0.001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.35 | 0.36 | -0.95 | 0.341 | 0.377 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.79 | 0.36 | -2.20 | 0.028 | 0.082 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.45 | 0.36 | -1.25 | 0.210 | 0.377 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.80, *p* = 0.033, η²_G = 0.032
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.49 | 16 | = 0.631 | -0.06 [-0.63, 0.40] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.34 | 16 | = 0.098 | -0.38 [-1.12, -0.01] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.93 | 16 | = 0.107 | -0.34 [-0.89, 0.14] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Significant main effect of condition (*p* = 0.041) (no significant pairwise comparisons)
**P3b latency:** Significant main effect of condition (*p* = 0.038) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.033) (no significant pairwise comparisons)

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
