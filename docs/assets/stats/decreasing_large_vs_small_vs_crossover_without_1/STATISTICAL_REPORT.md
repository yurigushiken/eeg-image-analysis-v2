# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:19:03

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
| Decreasing Crossover (no 1) | 24 | 104.67 ms | 8.48 | 1.73 | [92.00, 116.00] |
| Decreasing Large (no 1) | 24 | 105.17 ms | 8.86 | 1.81 | [92.00, 116.00] |
| Decreasing Small (no 1) | 24 | 104.33 ms | 10.14 | 2.07 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | -1.26 µV | 1.45 | 0.30 | [-5.50, 1.09] |
| Decreasing Large (no 1) | 24 | -1.54 µV | 1.84 | 0.38 | [-7.43, 1.09] |
| Decreasing Small (no 1) | 24 | -1.21 µV | 2.23 | 0.46 | [-5.65, 2.93] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 172.67 ms | 15.54 | 3.17 | [144.00, 208.00] |
| Decreasing Large (no 1) | 24 | 175.83 ms | 18.85 | 3.85 | [144.00, 212.00] |
| Decreasing Small (no 1) | 24 | 176.17 ms | 23.07 | 4.71 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | -5.84 µV | 2.00 | 0.41 | [-9.74, -2.14] |
| Decreasing Large (no 1) | 24 | -5.43 µV | 2.10 | 0.43 | [-10.35, -1.44] |
| Decreasing Small (no 1) | 24 | -5.79 µV | 2.54 | 0.52 | [-10.33, -1.35] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 110.33 ms | 8.33 | 1.70 | [100.00, 120.00] |
| Decreasing Large (no 1) | 24 | 109.17 ms | 8.79 | 1.79 | [100.00, 120.00] |
| Decreasing Small (no 1) | 24 | 110.17 ms | 8.50 | 1.74 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 1.15 µV | 1.71 | 0.35 | [-2.54, 4.53] |
| Decreasing Large (no 1) | 24 | 1.12 µV | 2.66 | 0.54 | [-3.63, 7.08] |
| Decreasing Small (no 1) | 24 | 0.65 µV | 2.28 | 0.46 | [-2.89, 5.61] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 473.00 ms | 24.83 | 5.07 | [436.00, 536.00] |
| Decreasing Large (no 1) | 24 | 489.00 ms | 36.89 | 7.53 | [428.00, 540.00] |
| Decreasing Small (no 1) | 24 | 485.83 ms | 36.01 | 7.35 | [432.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 3.81 µV | 3.25 | 0.66 | [-1.77, 10.85] |
| Decreasing Large (no 1) | 24 | 2.83 µV | 3.35 | 0.68 | [-4.81, 8.30] |
| Decreasing Small (no 1) | 24 | 5.05 µV | 4.52 | 0.92 | [-2.08, 17.81] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 527.52, BIC = 541.18
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.43, *SE* = 2.260, *z* = 0.191, *p* = 0.848
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.14, *SE* = 2.289, *z* = 0.062, *p* = 0.950
- **SNR**: *β* = 0.66, *SE* = 0.508, *z* = 1.294, *p* = 0.196

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.43 | 2.26 | -0.19 | 0.848 | 0.997 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -0.14 | 2.29 | -0.06 | 0.950 | 0.997 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.29 | 2.30 | 0.13 | 0.900 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.06, *p* = 0.937, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.28 | 23 | = 0.898 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.13 | 23 | = 0.898 | 0.04 [-0.40, 0.45] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.33 | 23 | = 0.898 | 0.09 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 278.08, BIC = 291.74
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.25, *SE* = 0.373, *z* = -0.660, *p* = 0.509
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.19, *SE* = 0.378, *z* = -0.506, *p* = 0.613
- **SNR**: *β* = -0.34, *SE* = 0.091, *z* = -3.716, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.25 | 0.37 | 0.66 | 0.509 | 0.882 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.19 | 0.38 | 0.51 | 0.613 | 0.882 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.05 | 0.38 | -0.14 | 0.886 | 0.886 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.680, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 0.87 | 23 | = 0.773 | 0.17 [-0.25, 0.60] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.14 | 23 | = 0.889 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.66 | 23 | = 0.773 | -0.16 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 631.11, BIC = 644.77
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 2.91, *SE* = 4.637, *z* = 0.628, *p* = 0.530
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 3.12, *SE* = 4.970, *z* = 0.628, *p* = 0.530
- **SNR**: *β* = -0.07, *SE* = 0.424, *z* = -0.157, *p* = 0.875

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -2.91 | 4.64 | -0.63 | 0.530 | 0.896 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -3.12 | 4.97 | -0.63 | 0.530 | 0.896 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.21 | 4.41 | -0.05 | 0.962 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.685, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.625 (ε = 0.744)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -1.11 | 23 | = 0.742 | -0.18 [-0.65, 0.20] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.69 | 23 | = 0.742 | -0.18 [-0.57, 0.28] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.07 | 23 | = 0.948 | -0.02 [-0.44, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 293.31, BIC = 306.97
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.15, *SE* = 0.390, *z* = 0.379, *p* = 0.705
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.34, *SE* = 0.422, *z* = -0.810, *p* = 0.418
- **SNR**: *β* = -0.07, *SE* = 0.039, *z* = -1.793, *p* = 0.073

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.15 | 0.39 | -0.38 | 0.705 | 0.705 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.34 | 0.42 | 0.81 | 0.418 | 0.661 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.49 | 0.37 | 1.33 | 0.183 | 0.455 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.73, *p* = 0.488, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -1.48 | 23 | = 0.457 | -0.20 [-0.73, 0.13] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.13 | 23 | = 0.897 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.85 | 23 | = 0.609 | 0.15 [-0.25, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 510.11, BIC = 523.77
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -1.26, *SE* = 1.821, *z* = -0.693, *p* = 0.488
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.69, *SE* = 1.968, *z* = -0.351, *p* = 0.725
- **SNR**: *β* = -0.26, *SE* = 0.376, *z* = -0.692, *p* = 0.489

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 1.26 | 1.82 | 0.69 | 0.488 | 0.866 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.69 | 1.97 | 0.35 | 0.725 | 0.925 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.57 | 1.92 | -0.30 | 0.766 | 0.925 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.23, *p* = 0.798, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 0.64 | 23 | = 0.927 | 0.14 [-0.29, 0.56] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.09 | 23 | = 0.927 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.50 | 23 | = 0.927 | -0.12 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.64, BIC = 316.30
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.01, *SE* = 0.400, *z* = -0.017, *p* = 0.987
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.36, *SE* = 0.440, *z* = -0.816, *p* = 0.415
- **SNR**: *β* = 0.07, *SE* = 0.092, *z* = 0.753, *p* = 0.452

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.01 | 0.40 | 0.02 | 0.987 | 0.987 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.36 | 0.44 | 0.82 | 0.415 | 0.794 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.35 | 0.43 | 0.83 | 0.409 | 0.794 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.388, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 0.10 | 23 | = 0.923 | 0.01 [-0.40, 0.44] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 1.31 | 23 | = 0.514 | 0.25 [-0.16, 0.70] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.97 | 23 | = 0.514 | 0.19 [-0.23, 0.62] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 700.94, BIC = 714.60
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 11.55, *SE* = 7.128, *z* = 1.621, *p* = 0.105
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 6.90, *SE* = 7.483, *z* = 0.922, *p* = 0.357
- **SNR**: *β* = -1.06, *SE* = 0.611, *z* = -1.728, *p* = 0.084

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -11.55 | 7.13 | -1.62 | 0.105 | 0.283 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -6.90 | 7.48 | -0.92 | 0.357 | 0.586 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 4.66 | 6.70 | 0.69 | 0.487 | 0.586 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.86, *p* = 0.068, η²_G = 0.044
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.59 | 23 | = 0.049 | -0.51 [-0.98, -0.08] | medium | * |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.95 | 23 | = 0.096 | -0.41 [-0.84, 0.04] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.38 | 23 | = 0.707 | 0.09 [-0.35, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 361.20, BIC = 374.86
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.58, *SE* = 0.600, *z* = -0.974, *p* = 0.330
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.77, *SE* = 0.631, *z* = 2.798, *p* = 0.005
- **SNR**: *β* = 0.09, *SE* = 0.053, *z* = 1.756, *p* = 0.079

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.58 | 0.60 | 0.97 | 0.330 | 0.330 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -1.77 | 0.63 | -2.80 | 0.005 | 0.010 | * |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -2.35 | 0.56 | -4.19 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.47, *p* = 0.002, η²_G = 0.058
- Greenhouse-Geisser corrected: *p* = 0.005 (ε = 0.712)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 1.93 | 23 | = 0.066 | 0.30 [-0.04, 0.83] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -2.79 | 23 | = 0.016 | -0.32 [-1.02, -0.11] | small | * |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -3.02 | 23 | = 0.016 | -0.56 [-1.08, -0.16] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Marginal trend toward condition differences (*p* = 0.068)
**P3b amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Decreasing Crossover (no 1) showed smaller amplitude than Decreasing Small (no 1) (*d* = -0.32)
  - Decreasing Large (no 1) showed smaller amplitude than Decreasing Small (no 1) (*d* = -0.56)

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
