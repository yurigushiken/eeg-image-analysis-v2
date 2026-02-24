# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:24:24

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
| 1 to 4 | 24 | 98.00 ms | 9.58 | 1.96 | [84.00, 108.00] |
| 2 to 5 | 24 | 95.83 ms | 10.91 | 2.23 | [84.00, 108.00] |
| 3 to 6 | 24 | 97.33 ms | 10.19 | 2.08 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -1.40 µV | 1.91 | 0.39 | [-4.44, 2.69] |
| 2 to 5 | 24 | -1.14 µV | 2.27 | 0.46 | [-10.84, 1.02] |
| 3 to 6 | 24 | -1.74 µV | 2.46 | 0.50 | [-4.88, 4.77] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 172.83 ms | 21.20 | 4.33 | [136.00, 216.00] |
| 2 to 5 | 24 | 170.50 ms | 22.93 | 4.68 | [132.00, 216.00] |
| 3 to 6 | 24 | 172.17 ms | 20.68 | 4.22 | [140.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -6.34 µV | 2.95 | 0.60 | [-12.55, -1.25] |
| 2 to 5 | 24 | -6.07 µV | 2.53 | 0.52 | [-13.83, -1.66] |
| 3 to 6 | 24 | -6.66 µV | 2.86 | 0.58 | [-12.81, -2.56] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 92.67 ms | 12.79 | 2.61 | [72.00, 108.00] |
| 2 to 5 | 24 | 90.67 ms | 14.53 | 2.97 | [72.00, 108.00] |
| 3 to 6 | 24 | 91.17 ms | 14.01 | 2.86 | [72.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 1.97 µV | 1.82 | 0.37 | [-0.89, 6.37] |
| 2 to 5 | 24 | 1.80 µV | 2.56 | 0.52 | [-1.93, 10.47] |
| 3 to 6 | 24 | 1.74 µV | 2.51 | 0.51 | [-2.13, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 452.50 ms | 59.73 | 12.19 | [352.00, 528.00] |
| 2 to 5 | 24 | 443.50 ms | 46.98 | 9.59 | [368.00, 528.00] |
| 3 to 6 | 24 | 466.50 ms | 56.47 | 11.53 | [352.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 5.03 µV | 3.68 | 0.75 | [-0.70, 13.02] |
| 2 to 5 | 24 | 5.24 µV | 2.82 | 0.58 | [0.82, 11.71] |
| 3 to 6 | 24 | 4.12 µV | 2.67 | 0.55 | [0.00, 10.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 545.49, BIC = 559.15
- **2 to 5 vs 1 to 4**: *β* = -1.93, *SE* = 2.842, *z* = -0.679, *p* = 0.497
- **3 to 6 vs 1 to 4**: *β* = -0.87, *SE* = 2.841, *z* = -0.306, *p* = 0.760
- **SNR**: *β* = 0.90, *SE* = 0.541, *z* = 1.661, *p* = 0.097

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 1.93 | 2.84 | 0.68 | 0.497 | 0.873 | n.s. |
| 1 to 4 - 3 to 6 | 0.87 | 2.84 | 0.31 | 0.760 | 0.916 | n.s. |
| 2 to 5 - 3 to 6 | -1.06 | 2.85 | -0.37 | 0.710 | 0.916 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.750, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.68 | 23 | = 0.802 | 0.21 [-0.29, 0.56] | small | n.s. |
| 1 to 4 vs 3 to 6 | 0.25 | 23 | = 0.802 | 0.07 [-0.37, 0.47] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.52 | 23 | = 0.802 | -0.14 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.97, BIC = 329.63
- **2 to 5 vs 1 to 4**: *β* = 0.14, *SE* = 0.577, *z* = 0.250, *p* = 0.802
- **3 to 6 vs 1 to 4**: *β* = -0.23, *SE* = 0.577, *z* = -0.392, *p* = 0.695
- **SNR**: *β* = -0.47, *SE* = 0.109, *z* = -4.325, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.14 | 0.58 | -0.25 | 0.802 | 0.907 | n.s. |
| 1 to 4 - 3 to 6 | 0.23 | 0.58 | 0.39 | 0.695 | 0.907 | n.s. |
| 2 to 5 - 3 to 6 | 0.37 | 0.58 | 0.64 | 0.522 | 0.891 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.47, *p* = 0.628, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.42 | 23 | = 0.679 | -0.13 [-0.51, 0.34] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.53 | 23 | = 0.679 | 0.15 [-0.32, 0.53] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 1.01 | 23 | = 0.679 | 0.25 [-0.22, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 642.49, BIC = 656.15
- **2 to 5 vs 1 to 4**: *β* = -2.42, *SE* = 4.562, *z* = -0.531, *p* = 0.595
- **3 to 6 vs 1 to 4**: *β* = -0.52, *SE* = 4.590, *z* = -0.112, *p* = 0.911
- **SNR**: *β* = -0.25, *SE* = 1.052, *z* = -0.240, *p* = 0.810

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 2.42 | 4.56 | 0.53 | 0.595 | 0.934 | n.s. |
| 1 to 4 - 3 to 6 | 0.52 | 4.59 | 0.11 | 0.911 | 0.934 | n.s. |
| 2 to 5 - 3 to 6 | -1.91 | 4.66 | -0.41 | 0.682 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.13, *p* = 0.874, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.44 | 23 | = 0.850 | 0.11 [-0.33, 0.51] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.19 | 23 | = 0.850 | 0.03 [-0.38, 0.46] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.34 | 23 | = 0.850 | -0.08 [-0.49, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 310.47, BIC = 324.13
- **2 to 5 vs 1 to 4**: *β* = 0.10, *SE* = 0.425, *z* = 0.248, *p* = 0.804
- **3 to 6 vs 1 to 4**: *β* = -0.03, *SE* = 0.428, *z* = -0.077, *p* = 0.939
- **SNR**: *β* = -0.48, *SE* = 0.103, *z* = -4.623, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.11 | 0.43 | -0.25 | 0.804 | 0.984 | n.s. |
| 1 to 4 - 3 to 6 | 0.03 | 0.43 | 0.08 | 0.939 | 0.984 | n.s. |
| 2 to 5 - 3 to 6 | 0.14 | 0.43 | 0.32 | 0.751 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.464, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.59 | 23 | = 0.561 | -0.10 [-0.54, 0.30] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.80 | 23 | = 0.561 | 0.11 [-0.26, 0.59] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 1.08 | 23 | = 0.561 | 0.22 [-0.21, 0.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 583.66, BIC = 597.32
- **2 to 5 vs 1 to 4**: *β* = -1.66, *SE* = 3.488, *z* = -0.475, *p* = 0.635
- **3 to 6 vs 1 to 4**: *β* = -2.29, *SE* = 3.500, *z* = -0.655, *p* = 0.512
- **SNR**: *β* = 2.71, *SE* = 1.067, *z* = 2.545, *p* = 0.011

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 1.66 | 3.49 | 0.48 | 0.635 | 0.884 | n.s. |
| 1 to 4 - 3 to 6 | 2.29 | 3.50 | 0.66 | 0.512 | 0.884 | n.s. |
| 2 to 5 - 3 to 6 | 0.64 | 3.51 | 0.18 | 0.857 | 0.884 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.854, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.56 | 23 | = 0.894 | 0.15 [-0.31, 0.54] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.40 | 23 | = 0.894 | 0.11 [-0.34, 0.50] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.13 | 23 | = 0.894 | -0.04 [-0.45, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 316.73, BIC = 330.39
- **2 to 5 vs 1 to 4**: *β* = -0.08, *SE* = 0.523, *z* = -0.153, *p* = 0.879
- **3 to 6 vs 1 to 4**: *β* = -0.42, *SE* = 0.524, *z* = -0.800, *p* = 0.423
- **SNR**: *β* = 0.66, *SE* = 0.166, *z* = 3.962, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 0.08 | 0.52 | 0.15 | 0.879 | 0.879 | n.s. |
| 1 to 4 - 3 to 6 | 0.42 | 0.52 | 0.80 | 0.423 | 0.808 | n.s. |
| 2 to 5 - 3 to 6 | 0.34 | 0.53 | 0.65 | 0.519 | 0.808 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.08, *p* = 0.923, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.26 | 23 | = 0.894 | 0.07 [-0.37, 0.48] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.35 | 23 | = 0.894 | 0.10 [-0.35, 0.49] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 0.13 | 23 | = 0.894 | 0.03 [-0.39, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 784.25, BIC = 797.91
- **2 to 5 vs 1 to 4**: *β* = -10.29, *SE* = 13.318, *z* = -0.772, *p* = 0.440
- **3 to 6 vs 1 to 4**: *β* = 9.67, *SE* = 13.787, *z* = 0.701, *p* = 0.483
- **SNR**: *β* = -2.83, *SE* = 2.438, *z* = -1.162, *p* = 0.245

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 10.28 | 13.32 | 0.77 | 0.440 | 0.686 | n.s. |
| 1 to 4 - 3 to 6 | -9.67 | 13.79 | -0.70 | 0.483 | 0.686 | n.s. |
| 2 to 5 - 3 to 6 | -19.95 | 13.53 | -1.47 | 0.140 | 0.365 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.251, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.60 | 23 | = 0.556 | 0.17 [-0.30, 0.55] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | -1.01 | 23 | = 0.481 | -0.24 [-0.63, 0.22] | small | n.s. |
| 2 to 5 vs 3 to 6 | -1.89 | 23 | = 0.214 | -0.44 [-0.82, 0.05] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 331.28, BIC = 344.94
- **2 to 5 vs 1 to 4**: *β* = 0.37, *SE* = 0.486, *z* = 0.769, *p* = 0.442
- **3 to 6 vs 1 to 4**: *β* = -0.36, *SE* = 0.512, *z* = -0.702, *p* = 0.482
- **SNR**: *β* = 0.36, *SE* = 0.110, *z* = 3.287, *p* = 0.001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.37 | 0.49 | -0.77 | 0.442 | 0.689 | n.s. |
| 1 to 4 - 3 to 6 | 0.36 | 0.51 | 0.70 | 0.482 | 0.689 | n.s. |
| 2 to 5 - 3 to 6 | 0.73 | 0.50 | 1.47 | 0.141 | 0.365 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.76, *p* = 0.074, η²_G = 0.025
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.37 | 23 | = 0.715 | -0.06 [-0.50, 0.35] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 1.91 | 23 | = 0.102 | 0.28 [-0.05, 0.83] | small | n.s. |
| 2 to 5 vs 3 to 6 | 2.36 | 23 | = 0.081 | 0.41 [0.04, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.074)

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
