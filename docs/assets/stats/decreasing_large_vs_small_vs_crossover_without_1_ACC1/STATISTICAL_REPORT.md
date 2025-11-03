# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:39:01

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
| Decreasing Crossover (no 1) | 18 | 105.33 ms | 7.13 | 1.68 | [96.00, 116.00] |
| Decreasing Large (no 1) | 17 | 109.41 ms | 6.62 | 1.61 | [96.00, 116.00] |
| Decreasing Small (no 1) | 14 | 105.43 ms | 8.39 | 2.24 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 18 | -1.86 µV | 1.12 | 0.26 | [-5.22, -0.28] |
| Decreasing Large (no 1) | 17 | -2.39 µV | 1.94 | 0.47 | [-7.59, -0.37] |
| Decreasing Small (no 1) | 14 | -2.76 µV | 1.68 | 0.45 | [-5.62, -0.69] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 172.83 ms | 14.92 | 3.05 | [148.00, 208.00] |
| Decreasing Large (no 1) | 24 | 177.33 ms | 19.33 | 3.95 | [144.00, 212.00] |
| Decreasing Small (no 1) | 22 | 173.27 ms | 23.04 | 4.91 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | -5.88 µV | 1.98 | 0.40 | [-9.79, -2.32] |
| Decreasing Large (no 1) | 24 | -5.75 µV | 2.36 | 0.48 | [-11.18, -2.00] |
| Decreasing Small (no 1) | 22 | -6.17 µV | 2.56 | 0.55 | [-10.33, -1.67] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 15 | 113.07 ms | 7.00 | 1.81 | [104.00, 120.00] |
| Decreasing Large (no 1) | 14 | 114.29 ms | 6.02 | 1.61 | [104.00, 120.00] |
| Decreasing Small (no 1) | 9 | 111.56 ms | 6.77 | 2.26 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 15 | 2.15 µV | 1.21 | 0.31 | [0.25, 4.25] |
| Decreasing Large (no 1) | 14 | 3.05 µV | 1.86 | 0.50 | [0.17, 6.31] |
| Decreasing Small (no 1) | 9 | 2.74 µV | 1.87 | 0.62 | [0.51, 6.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 476.40 ms | 25.56 | 5.72 | [436.00, 540.00] |
| Decreasing Large (no 1) | 19 | 494.11 ms | 34.91 | 8.01 | [436.00, 540.00] |
| Decreasing Small (no 1) | 18 | 490.00 ms | 32.12 | 7.57 | [432.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 4.88 µV | 2.77 | 0.62 | [0.59, 10.85] |
| Decreasing Large (no 1) | 19 | 5.03 µV | 2.37 | 0.54 | [1.97, 9.67] |
| Decreasing Small (no 1) | 18 | 6.73 µV | 4.05 | 0.96 | [2.10, 17.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 331.13, BIC = 342.49
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 3.21, *SE* = 1.655, *z* = 1.941, *p* = 0.052
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.17, *SE* = 1.755, *z* = 0.096, *p* = 0.923
- **SNR**: *β* = 0.25, *SE* = 0.461, *z* = 0.539, *p* = 0.590

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -3.21 | 1.65 | -1.94 | 0.052 | 0.149 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -0.17 | 1.75 | -0.10 | 0.923 | 0.923 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 3.04 | 1.82 | 1.68 | 0.094 | 0.179 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.89, *p* = 0.184, η²_G = 0.064
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -1.90 | 8 | = 0.283 | -0.66 [-1.06, 0.20] | medium | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.41 | 8 | = 0.695 | -0.12 [-0.68, 0.59] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 1.42 | 8 | = 0.289 | 0.43 [-0.25, 1.28] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 159.53, BIC = 170.88
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.46, *SE* = 0.342, *z* = -1.335, *p* = 0.182
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -1.20, *SE* = 0.370, *z* = -3.247, *p* = 0.001
- **SNR**: *β* = -0.56, *SE* = 0.082, *z* = -6.780, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.46 | 0.34 | 1.33 | 0.182 | 0.182 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 1.20 | 0.37 | 3.25 | 0.001 | 0.003 | ** |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.74 | 0.37 | 1.99 | 0.046 | 0.090 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.64, *p* = 0.539, η²_G = 0.036
- Greenhouse-Geisser corrected: *p* = 0.474 (ε = 0.616)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 1.57 | 8 | = 0.466 | 0.39 [-0.20, 1.06] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 1.04 | 8 | = 0.492 | 0.41 [-0.44, 0.84] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.04 | 8 | = 0.965 | -0.02 [-0.58, 0.86] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 616.05, BIC = 629.54
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 4.90, *SE* = 4.822, *z* = 1.016, *p* = 0.310
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 2.12, *SE* = 5.292, *z* = 0.401, *p* = 0.688
- **SNR**: *β* = 0.11, *SE* = 0.496, *z* = 0.226, *p* = 0.821

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -4.90 | 4.82 | -1.02 | 0.310 | 0.671 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -2.12 | 5.29 | -0.40 | 0.688 | 0.801 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 2.78 | 4.70 | 0.59 | 0.554 | 0.801 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.32, *p* = 0.731, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -1.19 | 21 | = 0.746 | -0.24 [-0.74, 0.13] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.43 | 21 | = 0.795 | -0.13 [-0.54, 0.35] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.26 | 21 | = 0.795 | 0.07 [-0.39, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 292.95, BIC = 306.44
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.32, *SE* = 0.425, *z* = -0.763, *p* = 0.445
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.77, *SE* = 0.470, *z* = -1.635, *p* = 0.102
- **SNR**: *β* = -0.13, *SE* = 0.047, *z* = -2.758, *p* = 0.006

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.32 | 0.42 | 0.76 | 0.445 | 0.480 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.77 | 0.47 | 1.63 | 0.102 | 0.276 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.44 | 0.41 | 1.08 | 0.279 | 0.480 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.08, *p* = 0.923, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.35 | 21 | = 0.903 | -0.06 [-0.51, 0.33] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.12 | 21 | = 0.903 | 0.03 [-0.42, 0.47] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.34 | 21 | = 0.903 | 0.07 [-0.37, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 255.58, BIC = 265.41
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.15, *SE* = 1.838, *z* = 0.623, *p* = 0.533
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.44, *SE* = 2.381, *z* = -0.187, *p* = 0.852
- **SNR**: *β* = -0.17, *SE* = 0.400, *z* = -0.436, *p* = 0.663

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -1.15 | 1.84 | -0.62 | 0.533 | 0.885 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.44 | 2.38 | 0.19 | 0.852 | 0.885 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 1.59 | 2.43 | 0.65 | 0.514 | 0.885 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.852, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.32 | 6 | = 0.881 | -0.16 [-0.78, 0.50] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.16 | 6 | = 0.868 | -0.24 [-1.41, 0.53] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.16 | 6 | = 0.881 | -0.08 [-0.98, 0.87] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 139.36, BIC = 149.18
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.90, *SE* = 0.408, *z* = 2.198, *p* = 0.028
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.95, *SE* = 0.513, *z* = 1.845, *p* = 0.065
- **SNR**: *β* = 0.22, *SE* = 0.096, *z* = 2.253, *p* = 0.024

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.90 | 0.41 | -2.20 | 0.028 | 0.081 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -0.95 | 0.51 | -1.85 | 0.065 | 0.126 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.05 | 0.53 | -0.09 | 0.925 | 0.925 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.428, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.47 | 6 | = 0.144 | -0.47 [-2.10, -0.41] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.78 | 6 | = 0.681 | -0.32 [-1.24, 0.65] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.43 | 6 | = 0.681 | 0.18 [-0.77, 1.09] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 548.76, BIC = 561.02
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 16.35, *SE* = 7.362, *z* = 2.220, *p* = 0.026
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 10.43, *SE* = 7.820, *z* = 1.333, *p* = 0.182
- **SNR**: *β* = -0.41, *SE* = 0.652, *z* = -0.627, *p* = 0.531

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -16.35 | 7.36 | -2.22 | 0.026 | 0.077 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -10.43 | 7.82 | -1.33 | 0.182 | 0.332 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 5.92 | 7.10 | 0.83 | 0.404 | 0.404 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.19, *p* = 0.056, η²_G = 0.071
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.28 | 15 | = 0.087 | -0.66 [-1.05, 0.01] | medium | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -2.05 | 15 | = 0.087 | -0.43 [-1.14, -0.06] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.88 | 15 | = 0.391 | 0.23 [-0.32, 0.76] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 263.78, BIC = 276.04
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.85, *SE* = 0.562, *z* = 1.510, *p* = 0.131
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 2.96, *SE* = 0.599, *z* = 4.944, *p* < .001
- **SNR**: *β* = 0.21, *SE* = 0.051, *z* = 4.087, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.85 | 0.56 | -1.51 | 0.131 | 0.131 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -2.96 | 0.60 | -4.94 | < .001 | < .001 | *** |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -2.11 | 0.54 | -3.92 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.25, *p* = 0.011, η²_G = 0.082
- Greenhouse-Geisser corrected: *p* = 0.021 (ε = 0.729)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 0.42 | 15 | = 0.682 | 0.10 [-0.49, 0.51] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -3.24 | 15 | = 0.017 | -0.53 [-1.31, -0.18] | medium | * |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -2.34 | 15 | = 0.050 | -0.61 [-1.16, -0.01] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Marginal trend toward condition differences (*p* = 0.056)
**P3b amplitude:** Significant main effect of condition (*p* = 0.011). Post-hoc tests revealed:
  - Decreasing Crossover (no 1) showed smaller amplitude than Decreasing Small (no 1) (*d* = -0.53)

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
