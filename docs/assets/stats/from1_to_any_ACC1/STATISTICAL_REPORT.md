# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:39:10

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
| 1 to 2 | 12 | 92.33 ms | 10.85 | 3.13 | [76.00, 104.00] |
| 1 to 3 | 15 | 94.13 ms | 11.80 | 3.05 | [76.00, 104.00] |
| 1 to 4 | 11 | 85.82 ms | 11.91 | 3.59 | [76.00, 104.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 2.80 µV | 1.82 | 0.53 | [0.61, 5.82] |
| 1 to 3 | 15 | 2.66 µV | 1.52 | 0.39 | [0.87, 6.24] |
| 1 to 4 | 11 | 2.34 µV | 1.10 | 0.33 | [1.13, 4.34] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | 171.64 ms | 17.84 | 3.80 | [144.00, 208.00] |
| 1 to 3 | 24 | 170.00 ms | 24.57 | 5.02 | [136.00, 216.00] |
| 1 to 4 | 21 | 171.62 ms | 20.74 | 4.53 | [136.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 22 | -5.81 µV | 2.14 | 0.46 | [-10.03, -2.38] |
| 1 to 3 | 24 | -6.37 µV | 2.63 | 0.54 | [-12.53, -2.34] |
| 1 to 4 | 21 | -7.07 µV | 2.85 | 0.62 | [-13.14, -2.90] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 87.33 ms | 10.76 | 3.11 | [68.00, 100.00] |
| 1 to 3 | 9 | 84.00 ms | 11.49 | 3.83 | [72.00, 100.00] |
| 1 to 4 | 15 | 92.00 ms | 8.28 | 2.14 | [80.00, 100.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 12 | 2.58 µV | 1.32 | 0.38 | [0.62, 4.29] |
| 1 to 3 | 9 | 3.15 µV | 2.00 | 0.67 | [1.64, 7.47] |
| 1 to 4 | 15 | 2.72 µV | 1.22 | 0.32 | [0.81, 4.28] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 448.75 ms | 55.35 | 13.84 | [368.00, 536.00] |
| 1 to 3 | 20 | 451.00 ms | 44.18 | 9.88 | [368.00, 516.00] |
| 1 to 4 | 20 | 461.80 ms | 57.09 | 12.77 | [376.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 16 | 6.10 µV | 2.84 | 0.71 | [2.09, 11.99] |
| 1 to 3 | 20 | 6.49 µV | 3.60 | 0.81 | [1.71, 14.25] |
| 1 to 4 | 20 | 6.17 µV | 3.19 | 0.71 | [2.01, 13.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.83, BIC = 307.65
- **1 to 3 vs 1 to 2**: *β* = -0.39, *SE* = 3.342, *z* = -0.117, *p* = 0.907
- **1 to 4 vs 1 to 2**: *β* = -10.33, *SE* = 4.046, *z* = -2.554, *p* = 0.011
- **SNR**: *β* = 1.73, *SE* = 1.092, *z* = 1.584, *p* = 0.113

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.39 | 3.34 | 0.12 | 0.907 | 0.907 | n.s. |
| 1 to 2 - 1 to 4 | 10.33 | 4.05 | 2.55 | 0.011 | 0.021 | * |
| 1 to 3 - 1 to 4 | 9.94 | 3.56 | 2.79 | 0.005 | 0.016 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.09, *p* = 0.420, η²_G = 0.219
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.71 | 2 | = 0.596 | 0.60 [-0.67, 1.01] | medium | n.s. |
| 1 to 2 vs 1 to 4 | 2.00 | 2 | = 0.551 | 1.20 [-0.82, 3.78] | large | n.s. |
| 1 to 3 vs 1 to 4 | 0.62 | 2 | = 0.596 | 0.44 [-0.46, 1.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 109.43, BIC = 119.26
- **1 to 3 vs 1 to 2**: *β* = -0.28, *SE* = 0.338, *z* = -0.834, *p* = 0.404
- **1 to 4 vs 1 to 2**: *β* = -0.39, *SE* = 0.364, *z* = -1.063, *p* = 0.288
- **SNR**: *β* = 0.83, *SE* = 0.100, *z* = 8.249, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.28 | 0.34 | 0.83 | 0.404 | 0.645 | n.s. |
| 1 to 2 - 1 to 4 | 0.39 | 0.36 | 1.06 | 0.288 | 0.639 | n.s. |
| 1 to 3 - 1 to 4 | 0.11 | 0.35 | 0.30 | 0.762 | 0.762 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.02, *p* = 0.440, η²_G = 0.273
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.23 | 2 | = 0.465 | 0.98 [-0.82, 0.86] | large | n.s. |
| 1 to 2 vs 1 to 4 | 0.84 | 2 | = 0.732 | 0.89 [-1.26, 2.05] | large | n.s. |
| 1 to 3 vs 1 to 4 | -0.13 | 2 | = 0.912 | -0.14 [-1.05, 1.05] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 587.15, BIC = 600.37
- **1 to 3 vs 1 to 2**: *β* = -0.52, *SE* = 3.967, *z* = -0.131, *p* = 0.896
- **1 to 4 vs 1 to 2**: *β* = 2.91, *SE* = 4.130, *z* = 0.705, *p* = 0.481
- **SNR**: *β* = -0.72, *SE* = 0.897, *z* = -0.805, *p* = 0.421

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.52 | 3.97 | 0.13 | 0.896 | 0.896 | n.s. |
| 1 to 2 - 1 to 4 | -2.91 | 4.13 | -0.71 | 0.481 | 0.773 | n.s. |
| 1 to 3 - 1 to 4 | -3.43 | 3.99 | -0.86 | 0.390 | 0.773 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.387, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 0.88 | 18 | = 0.588 | 0.18 [-0.40, 0.49] | negligible | n.s. |
| 1 to 2 vs 1 to 4 | -0.51 | 18 | = 0.613 | -0.12 [-0.60, 0.37] | negligible | n.s. |
| 1 to 3 vs 1 to 4 | -1.41 | 18 | = 0.525 | -0.27 [-0.78, 0.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.78, BIC = 294.01
- **1 to 3 vs 1 to 2**: *β* = -0.22, *SE* = 0.407, *z* = -0.531, *p* = 0.596
- **1 to 4 vs 1 to 2**: *β* = -0.82, *SE* = 0.423, *z* = -1.943, *p* = 0.052
- **SNR**: *β* = -0.37, *SE* = 0.096, *z* = -3.851, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 0.22 | 0.41 | 0.53 | 0.596 | 0.596 | n.s. |
| 1 to 2 - 1 to 4 | 0.82 | 0.42 | 1.94 | 0.052 | 0.148 | n.s. |
| 1 to 3 - 1 to 4 | 0.61 | 0.41 | 1.48 | 0.140 | 0.260 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.71, *p* = 0.195, η²_G = 0.021
- Greenhouse-Geisser corrected: *p* = 0.204 (ε = 0.716)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 1.66 | 18 | = 0.171 | 0.21 [-0.12, 0.79] | small | n.s. |
| 1 to 2 vs 1 to 4 | 1.73 | 18 | = 0.171 | 0.35 [-0.10, 0.90] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.66 | 18 | = 0.518 | 0.14 [-0.30, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 276.56, BIC = 286.06
- **1 to 3 vs 1 to 2**: *β* = -3.52, *SE* = 4.265, *z* = -0.824, *p* = 0.410
- **1 to 4 vs 1 to 2**: *β* = 4.49, *SE* = 3.718, *z* = 1.207, *p* = 0.227
- **SNR**: *β* = -0.37, *SE* = 0.990, *z* = -0.377, *p* = 0.706

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | 3.52 | 4.26 | 0.82 | 0.410 | 0.410 | n.s. |
| 1 to 2 - 1 to 4 | -4.49 | 3.72 | -1.21 | 0.227 | 0.403 | n.s. |
| 1 to 3 - 1 to 4 | -8.00 | 4.02 | -1.99 | 0.046 | 0.133 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.83, *p* = 0.065, η²_G = 0.604
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | 2.52 | 2 | = 0.191 | 1.37 [-0.70, 1.48] | large | n.s. |
| 1 to 2 vs 1 to 4 | -0.76 | 2 | = 0.525 | -0.67 [-1.60, 0.41] | medium | n.s. |
| 1 to 3 vs 1 to 4 | -6.05 | 2 | = 0.079 | -4.62 [-1.67, 0.58] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 128.40, BIC = 137.90
- **1 to 3 vs 1 to 2**: *β* = 0.90, *SE* = 0.525, *z* = 1.709, *p* = 0.087
- **1 to 4 vs 1 to 2**: *β* = 0.47, *SE* = 0.487, *z* = 0.967, *p* = 0.334
- **SNR**: *β* = 0.44, *SE* = 0.123, *z* = 3.538, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.90 | 0.52 | -1.71 | 0.087 | 0.240 | n.s. |
| 1 to 2 - 1 to 4 | -0.47 | 0.49 | -0.97 | 0.334 | 0.556 | n.s. |
| 1 to 3 - 1 to 4 | 0.43 | 0.50 | 0.86 | 0.392 | 0.556 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.18, *p* = 0.229, η²_G = 0.140
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.84 | 2 | = 0.312 | -0.41 [-1.59, 0.63] | small | n.s. |
| 1 to 2 vs 1 to 4 | -2.23 | 2 | = 0.312 | -0.75 [-1.70, 0.35] | medium | n.s. |
| 1 to 3 vs 1 to 4 | -0.83 | 2 | = 0.493 | -0.44 [-1.75, 0.54] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 610.61, BIC = 622.77
- **1 to 3 vs 1 to 2**: *β* = 1.43, *SE* = 16.555, *z* = 0.086, *p* = 0.931
- **1 to 4 vs 1 to 2**: *β* = 12.49, *SE* = 16.461, *z* = 0.759, *p* = 0.448
- **SNR**: *β* = 1.27, *SE* = 2.612, *z* = 0.485, *p* = 0.627

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -1.43 | 16.56 | -0.09 | 0.931 | 0.931 | n.s. |
| 1 to 2 - 1 to 4 | -12.49 | 16.46 | -0.76 | 0.448 | 0.832 | n.s. |
| 1 to 3 - 1 to 4 | -11.06 | 15.39 | -0.72 | 0.472 | 0.832 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.89, *p* = 0.422, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -0.97 | 13 | = 0.527 | -0.35 [-0.85, 0.33] | small | n.s. |
| 1 to 2 vs 1 to 4 | -1.22 | 13 | = 0.527 | -0.41 [-0.72, 0.39] | small | n.s. |
| 1 to 3 vs 1 to 4 | -0.35 | 13 | = 0.733 | -0.12 [-0.70, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 251.95, BIC = 264.11
- **1 to 3 vs 1 to 2**: *β* = 0.19, *SE* = 0.574, *z* = 0.328, *p* = 0.743
- **1 to 4 vs 1 to 2**: *β* = 0.04, *SE* = 0.561, *z* = 0.069, *p* = 0.945
- **SNR**: *β* = 0.55, *SE* = 0.110, *z* = 5.036, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 1 to 3 | -0.19 | 0.57 | -0.33 | 0.743 | 0.983 | n.s. |
| 1 to 2 - 1 to 4 | -0.04 | 0.56 | -0.07 | 0.945 | 0.983 | n.s. |
| 1 to 3 - 1 to 4 | 0.15 | 0.51 | 0.29 | 0.768 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.33, *p* = 0.281, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 1 to 3 | -1.39 | 13 | = 0.422 | -0.35 [-0.97, 0.23] | small | n.s. |
| 1 to 2 vs 1 to 4 | -0.97 | 13 | = 0.422 | -0.21 [-0.82, 0.31] | small | n.s. |
| 1 to 3 vs 1 to 4 | 0.83 | 13 | = 0.422 | 0.14 [-0.34, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Marginal trend toward condition differences (*p* = 0.065)

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
