# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:34:11

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
| Decreasing Crossover | 7 | 107.43 ms | 12.09 | 4.57 | [96.00, 120.00] |
| Decreasing Large | 9 | 114.67 ms | 10.58 | 3.53 | [96.00, 120.00] |
| Decreasing Small | 8 | 111.00 ms | 10.20 | 3.61 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 7 | 1.61 µV | 0.87 | 0.33 | [0.58, 3.39] |
| Decreasing Large | 9 | 2.34 µV | 1.37 | 0.46 | [0.84, 5.04] |
| Decreasing Small | 8 | 1.57 µV | 1.20 | 0.43 | [0.63, 4.14] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 174.50 ms | 14.24 | 2.91 | [152.00, 208.00] |
| Decreasing Large | 24 | 177.50 ms | 18.46 | 3.77 | [148.00, 208.00] |
| Decreasing Small | 21 | 179.62 ms | 12.64 | 2.76 | [156.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | -5.32 µV | 1.84 | 0.37 | [-8.96, -2.04] |
| Decreasing Large | 24 | -5.74 µV | 2.36 | 0.48 | [-11.18, -2.00] |
| Decreasing Small | 21 | -4.42 µV | 2.54 | 0.55 | [-9.67, -0.98] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 15 | 115.47 ms | 7.84 | 2.02 | [104.00, 124.00] |
| Decreasing Large | 14 | 113.43 ms | 7.62 | 2.04 | [100.00, 124.00] |
| Decreasing Small | 19 | 117.05 ms | 6.65 | 1.52 | [104.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 15 | 2.56 µV | 1.46 | 0.38 | [1.10, 5.67] |
| Decreasing Large | 14 | 3.10 µV | 1.91 | 0.51 | [0.19, 6.60] |
| Decreasing Small | 19 | 2.64 µV | 1.72 | 0.40 | [0.60, 7.19] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 21 | 482.10 ms | 26.91 | 5.87 | [436.00, 540.00] |
| Decreasing Large | 19 | 494.11 ms | 34.91 | 8.01 | [436.00, 540.00] |
| Decreasing Small | 20 | 484.20 ms | 22.04 | 4.93 | [436.00, 512.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 21 | 4.72 µV | 2.81 | 0.61 | [0.94, 10.69] |
| Decreasing Large | 19 | 5.03 µV | 2.37 | 0.54 | [1.97, 9.67] |
| Decreasing Small | 20 | 5.33 µV | 2.73 | 0.61 | [2.17, 12.20] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 186.56, BIC = 193.63
- **Decreasing Large vs Decreasing Crossover**: *β* = 6.29, *SE* = 4.462, *z* = 1.410, *p* = 0.158
- **Decreasing Small vs Decreasing Crossover**: *β* = 4.29, *SE* = 4.018, *z* = 1.067, *p* = 0.286
- **SNR**: *β* = 1.49, *SE* = 1.124, *z* = 1.327, *p* = 0.184

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -6.29 | 4.46 | -1.41 | 0.158 | 0.404 | n.s. |
| Decreasing Crossover - Decreasing Small | -4.29 | 4.02 | -1.07 | 0.286 | 0.490 | n.s. |
| Decreasing Large - Decreasing Small | 2.01 | 3.77 | 0.53 | 0.594 | 0.594 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 73.72, BIC = 80.79
- **Decreasing Large vs Decreasing Crossover**: *β* = 1.17, *SE* = 0.452, *z* = 2.589, *p* = 0.010
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.38, *SE* = 0.489, *z* = 0.776, *p* = 0.438
- **SNR**: *β* = 0.38, *SE* = 0.108, *z* = 3.531, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -1.17 | 0.45 | -2.59 | 0.010 | 0.029 | * |
| Decreasing Crossover - Decreasing Small | -0.38 | 0.49 | -0.78 | 0.438 | 0.438 | n.s. |
| Decreasing Large - Decreasing Small | 0.79 | 0.48 | 1.66 | 0.096 | 0.183 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.96, BIC = 564.36
- **Decreasing Large vs Decreasing Crossover**: *β* = 3.15, *SE* = 2.736, *z* = 1.150, *p* = 0.250
- **Decreasing Small vs Decreasing Crossover**: *β* = 6.24, *SE* = 3.025, *z* = 2.061, *p* = 0.039
- **SNR**: *β* = 0.03, *SE* = 0.255, *z* = 0.124, *p* = 0.901

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -3.15 | 2.74 | -1.15 | 0.250 | 0.420 | n.s. |
| Decreasing Crossover - Decreasing Small | -6.24 | 3.02 | -2.06 | 0.039 | 0.113 | n.s. |
| Decreasing Large - Decreasing Small | -3.09 | 2.62 | -1.18 | 0.239 | 0.420 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.59, *p* = 0.087, η²_G = 0.028
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.02 | 20 | = 0.328 | -0.18 [-0.66, 0.20] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -3.37 | 20 | = 0.009 | -0.46 [-1.25, -0.22] | small | ** |
| Decreasing Large vs Decreasing Small | -1.00 | 20 | = 0.328 | -0.20 [-0.68, 0.24] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 285.86, BIC = 299.26
- **Decreasing Large vs Decreasing Crossover**: *β* = -1.00, *SE* = 0.434, *z* = -2.317, *p* = 0.020
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.29, *SE* = 0.477, *z* = 0.613, *p* = 0.540
- **SNR**: *β* = -0.13, *SE* = 0.039, *z* = -3.269, *p* = 0.001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 1.01 | 0.43 | 2.32 | 0.020 | 0.041 | * |
| Decreasing Crossover - Decreasing Small | -0.29 | 0.48 | -0.61 | 0.540 | 0.540 | n.s. |
| Decreasing Large - Decreasing Small | -1.30 | 0.42 | -3.11 | 0.002 | 0.006 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.18, *p* = 0.005, η²_G = 0.083
- Greenhouse-Geisser corrected: *p* = 0.011 (ε = 0.705)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.06 | 20 | = 0.300 | 0.19 [-0.18, 0.68] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -2.96 | 20 | = 0.023 | -0.53 [-1.15, -0.14] | medium | * |
| Decreasing Large vs Decreasing Small | -2.63 | 20 | = 0.024 | -0.64 [-1.07, -0.08] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 330.59, BIC = 341.82
- **Decreasing Large vs Decreasing Crossover**: *β* = -1.64, *SE* = 2.121, *z* = -0.774, *p* = 0.439
- **Decreasing Small vs Decreasing Crossover**: *β* = 2.85, *SE* = 2.007, *z* = 1.420, *p* = 0.156
- **SNR**: *β* = 0.07, *SE* = 0.356, *z* = 0.203, *p* = 0.839

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 1.64 | 2.12 | 0.77 | 0.439 | 0.439 | n.s. |
| Decreasing Crossover - Decreasing Small | -2.85 | 2.01 | -1.42 | 0.156 | 0.287 | n.s. |
| Decreasing Large - Decreasing Small | -4.49 | 2.00 | -2.24 | 0.025 | 0.073 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.91, *p* = 0.174, η²_G = 0.069
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.49 | 10 | = 0.250 | 0.42 [-0.26, 1.15] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.58 | 10 | = 0.574 | -0.18 [-1.12, 0.11] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.62 | 10 | = 0.250 | -0.63 [-1.18, 0.11] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 162.76, BIC = 173.99
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.76, *SE* = 0.339, *z* = 2.239, *p* = 0.025
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.53, *SE* = 0.313, *z* = 1.684, *p* = 0.092
- **SNR**: *β* = 0.23, *SE* = 0.068, *z* = 3.362, *p* = 0.001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.76 | 0.34 | -2.24 | 0.025 | 0.074 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.53 | 0.31 | -1.68 | 0.092 | 0.176 | n.s. |
| Decreasing Large - Decreasing Small | 0.23 | 0.32 | 0.73 | 0.466 | 0.466 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.63, *p* = 0.222, η²_G = 0.040
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -2.64 | 10 | = 0.074 | -0.45 [-1.57, -0.02] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.36 | 10 | = 0.304 | -0.37 [-0.93, 0.26] | small | n.s. |
| Decreasing Large vs Decreasing Small | 0.24 | 10 | = 0.812 | 0.08 [-0.53, 0.68] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 567.46, BIC = 580.03
- **Decreasing Large vs Decreasing Crossover**: *β* = 10.95, *SE* = 6.923, *z* = 1.582, *p* = 0.114
- **Decreasing Small vs Decreasing Crossover**: *β* = 2.22, *SE* = 6.415, *z* = 0.346, *p* = 0.729
- **SNR**: *β* = -0.13, *SE* = 0.493, *z* = -0.256, *p* = 0.798

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -10.95 | 6.92 | -1.58 | 0.114 | 0.303 | n.s. |
| Decreasing Crossover - Decreasing Small | -2.22 | 6.41 | -0.35 | 0.729 | 0.729 | n.s. |
| Decreasing Large - Decreasing Small | 8.74 | 6.50 | 1.34 | 0.179 | 0.326 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.38, *p* = 0.265, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.67 | 17 | = 0.338 | -0.32 [-0.91, 0.12] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.13 | 17 | = 0.898 | -0.03 [-0.58, 0.36] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | 1.25 | 17 | = 0.341 | 0.31 [-0.21, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 254.06, BIC = 266.62
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.92, *SE* = 0.467, *z* = 1.979, *p* = 0.048
- **Decreasing Small vs Decreasing Crossover**: *β* = 1.04, *SE* = 0.427, *z* = 2.440, *p* = 0.015
- **SNR**: *β* = 0.16, *SE* = 0.035, *z* = 4.573, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.92 | 0.47 | -1.98 | 0.048 | 0.093 | n.s. |
| Decreasing Crossover - Decreasing Small | -1.04 | 0.43 | -2.44 | 0.015 | 0.043 | * |
| Decreasing Large - Decreasing Small | -0.12 | 0.43 | -0.28 | 0.783 | 0.783 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.658, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.10 | 17 | = 0.919 | 0.02 [-0.47, 0.52] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.97 | 17 | = 0.726 | -0.15 [-0.74, 0.22] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -0.72 | 17 | = 0.726 | -0.18 [-0.67, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Marginal trend toward condition differences (*p* = 0.087)
**N1 amplitude:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller amplitude than Decreasing Small (*d* = -0.53)
  - Decreasing Large showed smaller amplitude than Decreasing Small (*d* = -0.64)

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
