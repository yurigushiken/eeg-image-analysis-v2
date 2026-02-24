# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:27:16

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
| 2 to 1 | 24 | 119.33 ms | 16.50 | 3.37 | [92.00, 136.00] |
| 3 to 1 | 24 | 113.83 ms | 14.68 | 3.00 | [92.00, 136.00] |
| 4 to 1 | 24 | 115.17 ms | 16.64 | 3.40 | [92.00, 136.00] |
| Cardinality1 | 24 | 116.33 ms | 16.08 | 3.28 | [92.00, 136.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -2.61 µV | 2.03 | 0.41 | [-6.41, 2.51] |
| 3 to 1 | 24 | -2.07 µV | 2.03 | 0.41 | [-6.18, 1.52] |
| 4 to 1 | 24 | -3.18 µV | 2.62 | 0.53 | [-8.54, 2.33] |
| Cardinality1 | 24 | -2.42 µV | 2.57 | 0.52 | [-9.61, 3.80] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 181.83 ms | 12.76 | 2.60 | [160.00, 204.00] |
| 3 to 1 | 24 | 180.67 ms | 13.33 | 2.72 | [160.00, 204.00] |
| 4 to 1 | 24 | 183.67 ms | 12.20 | 2.49 | [160.00, 204.00] |
| Cardinality1 | 24 | 182.67 ms | 14.62 | 2.98 | [160.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -3.38 µV | 3.29 | 0.67 | [-10.79, 2.29] |
| 3 to 1 | 24 | -3.89 µV | 2.58 | 0.53 | [-10.41, -0.72] |
| 4 to 1 | 24 | -3.46 µV | 2.05 | 0.42 | [-8.09, 0.13] |
| Cardinality1 | 24 | -3.13 µV | 2.65 | 0.54 | [-9.64, 0.56] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 123.00 ms | 13.92 | 2.84 | [100.00, 144.00] |
| 3 to 1 | 24 | 119.83 ms | 13.42 | 2.74 | [100.00, 144.00] |
| 4 to 1 | 24 | 125.50 ms | 13.39 | 2.73 | [100.00, 144.00] |
| Cardinality1 | 24 | 120.83 ms | 14.45 | 2.95 | [100.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 3.96 µV | 2.66 | 0.54 | [-0.41, 9.13] |
| 3 to 1 | 24 | 3.64 µV | 2.31 | 0.47 | [-2.54, 9.14] |
| 4 to 1 | 24 | 4.27 µV | 3.04 | 0.62 | [0.32, 13.38] |
| Cardinality1 | 24 | 4.02 µV | 3.21 | 0.66 | [-1.81, 13.50] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 494.67 ms | 30.27 | 6.18 | [432.00, 532.00] |
| 3 to 1 | 24 | 478.17 ms | 28.23 | 5.76 | [432.00, 532.00] |
| 4 to 1 | 24 | 484.50 ms | 33.18 | 6.77 | [432.00, 532.00] |
| Cardinality1 | 24 | 479.33 ms | 33.25 | 6.79 | [432.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 4.75 µV | 3.32 | 0.68 | [-2.33, 11.08] |
| 3 to 1 | 24 | 4.82 µV | 3.51 | 0.72 | [-0.59, 14.34] |
| 4 to 1 | 24 | 5.18 µV | 3.59 | 0.73 | [-2.49, 12.03] |
| Cardinality1 | 24 | 1.77 µV | 2.66 | 0.54 | [-4.09, 7.06] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 811.07, BIC = 829.02
- **3 to 1 vs 2 to 1**: *β* = -5.66, *SE* = 4.142, *z* = -1.366, *p* = 0.172
- **4 to 1 vs 2 to 1**: *β* = -3.96, *SE* = 4.145, *z* = -0.955, *p* = 0.339
- **Cardinality1 vs 2 to 1**: *β* = -3.06, *SE* = 4.138, *z* = -0.741, *p* = 0.459
- **SNR**: *β* = -0.90, *SE* = 1.161, *z* = -0.773, *p* = 0.439

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 5.66 | 4.14 | 1.37 | 0.172 | 0.677 | n.s. |
| 2 to 1 - 4 to 1 | 3.96 | 4.15 | 0.96 | 0.339 | 0.874 | n.s. |
| 2 to 1 - Cardinality1 | 3.07 | 4.14 | 0.74 | 0.459 | 0.914 | n.s. |
| 3 to 1 - 4 to 1 | -1.70 | 4.16 | -0.41 | 0.683 | 0.914 | n.s. |
| 3 to 1 - Cardinality1 | -2.59 | 4.14 | -0.63 | 0.531 | 0.914 | n.s. |
| 4 to 1 - Cardinality1 | -0.89 | 4.15 | -0.22 | 0.829 | 0.914 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.610, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.28 | 23 | = 0.794 | 0.35 [-0.17, 0.69] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.89 | 23 | = 0.794 | 0.25 [-0.24, 0.61] | small | n.s. |
| 2 to 1 vs Cardinality1 | 0.79 | 23 | = 0.794 | 0.18 [-0.26, 0.59] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.34 | 23 | = 0.794 | -0.08 [-0.49, 0.35] | negligible | n.s. |
| 3 to 1 vs Cardinality1 | -0.59 | 23 | = 0.794 | -0.16 [-0.54, 0.30] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | -0.26 | 23 | = 0.794 | -0.07 [-0.48, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 430.84, BIC = 448.79
- **3 to 1 vs 2 to 1**: *β* = 0.47, *SE* = 0.544, *z* = 0.873, *p* = 0.383
- **4 to 1 vs 2 to 1**: *β* = -0.49, *SE* = 0.544, *z* = -0.902, *p* = 0.367
- **Cardinality1 vs 2 to 1**: *β* = 0.16, *SE* = 0.543, *z* = 0.292, *p* = 0.770
- **SNR**: *β* = -0.37, *SE* = 0.156, *z* = -2.369, *p* = 0.018

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | -0.47 | 0.54 | -0.87 | 0.383 | 0.839 | n.s. |
| 2 to 1 - 4 to 1 | 0.49 | 0.54 | 0.90 | 0.367 | 0.839 | n.s. |
| 2 to 1 - Cardinality1 | -0.16 | 0.54 | -0.29 | 0.770 | 0.839 | n.s. |
| 3 to 1 - 4 to 1 | 0.97 | 0.55 | 1.77 | 0.077 | 0.383 | n.s. |
| 3 to 1 - Cardinality1 | 0.32 | 0.54 | 0.58 | 0.561 | 0.839 | n.s. |
| 4 to 1 - Cardinality1 | -0.65 | 0.54 | -1.19 | 0.233 | 0.735 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.31, *p* = 0.277, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -0.97 | 23 | = 0.512 | -0.27 [-0.62, 0.23] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.97 | 23 | = 0.512 | 0.25 [-0.23, 0.62] | small | n.s. |
| 2 to 1 vs Cardinality1 | -0.37 | 23 | = 0.711 | -0.08 [-0.50, 0.35] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | 2.00 | 23 | = 0.345 | 0.48 [-0.03, 0.85] | small | n.s. |
| 3 to 1 vs Cardinality1 | 0.60 | 23 | = 0.663 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | -1.17 | 23 | = 0.512 | -0.29 [-0.67, 0.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 738.00, BIC = 755.95
- **3 to 1 vs 2 to 1**: *β* = -1.06, *SE* = 2.370, *z* = -0.446, *p* = 0.656
- **4 to 1 vs 2 to 1**: *β* = 1.80, *SE* = 2.369, *z* = 0.761, *p* = 0.447
- **Cardinality1 vs 2 to 1**: *β* = 0.84, *SE* = 2.369, *z* = 0.354, *p* = 0.724
- **SNR**: *β* = 0.76, *SE* = 0.347, *z* = 2.188, *p* = 0.029

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 1.06 | 2.37 | 0.45 | 0.656 | 0.959 | n.s. |
| 2 to 1 - 4 to 1 | -1.80 | 2.37 | -0.76 | 0.447 | 0.937 | n.s. |
| 2 to 1 - Cardinality1 | -0.84 | 2.37 | -0.35 | 0.724 | 0.959 | n.s. |
| 3 to 1 - 4 to 1 | -2.86 | 2.37 | -1.21 | 0.227 | 0.787 | n.s. |
| 3 to 1 - Cardinality1 | -1.89 | 2.37 | -0.80 | 0.424 | 0.937 | n.s. |
| 4 to 1 - Cardinality1 | 0.97 | 2.37 | 0.41 | 0.684 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.51, *p* = 0.679, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.60 | 23 | = 0.752 | 0.09 [-0.30, 0.55] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.98 | 23 | = 0.752 | -0.15 [-0.63, 0.23] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | -0.32 | 23 | = 0.752 | -0.06 [-0.49, 0.36] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.17 | 23 | = 0.752 | -0.23 [-0.67, 0.19] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.63 | 23 | = 0.752 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.36 | 23 | = 0.752 | 0.07 [-0.35, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 412.36, BIC = 430.31
- **3 to 1 vs 2 to 1**: *β* = -0.58, *SE* = 0.477, *z* = -1.209, *p* = 0.227
- **4 to 1 vs 2 to 1**: *β* = -0.07, *SE* = 0.477, *z* = -0.142, *p* = 0.887
- **Cardinality1 vs 2 to 1**: *β* = 0.24, *SE* = 0.477, *z* = 0.513, *p* = 0.608
- **SNR**: *β* = -0.42, *SE* = 0.069, *z* = -6.177, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.58 | 0.48 | 1.21 | 0.227 | 0.723 | n.s. |
| 2 to 1 - 4 to 1 | 0.07 | 0.48 | 0.14 | 0.887 | 0.887 | n.s. |
| 2 to 1 - Cardinality1 | -0.24 | 0.48 | -0.51 | 0.608 | 0.884 | n.s. |
| 3 to 1 - 4 to 1 | -0.51 | 0.48 | -1.07 | 0.286 | 0.740 | n.s. |
| 3 to 1 - Cardinality1 | -0.82 | 0.48 | -1.72 | 0.085 | 0.413 | n.s. |
| 4 to 1 - Cardinality1 | -0.31 | 0.48 | -0.66 | 0.512 | 0.884 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.65, *p* = 0.587, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.90 | 23 | = 0.761 | 0.17 [-0.24, 0.61] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | 0.15 | 23 | = 0.881 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | -0.41 | 23 | = 0.821 | -0.08 [-0.51, 0.34] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.89 | 23 | = 0.761 | -0.19 [-0.61, 0.24] | negligible | n.s. |
| 3 to 1 vs Cardinality1 | -1.27 | 23 | = 0.761 | -0.29 [-0.69, 0.17] | small | n.s. |
| 4 to 1 vs Cardinality1 | -0.63 | 23 | = 0.806 | -0.14 [-0.55, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 777.30, BIC = 795.25
- **3 to 1 vs 2 to 1**: *β* = -3.06, *SE* = 3.336, *z* = -0.917, *p* = 0.359
- **4 to 1 vs 2 to 1**: *β* = 2.52, *SE* = 3.314, *z* = 0.761, *p* = 0.447
- **Cardinality1 vs 2 to 1**: *β* = -2.08, *SE* = 3.327, *z* = -0.626, *p* = 0.531
- **SNR**: *β* = 0.16, *SE* = 0.573, *z* = 0.276, *p* = 0.783

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 3.06 | 3.34 | 0.92 | 0.359 | 0.831 | n.s. |
| 2 to 1 - 4 to 1 | -2.52 | 3.31 | -0.76 | 0.447 | 0.831 | n.s. |
| 2 to 1 - Cardinality1 | 2.08 | 3.33 | 0.63 | 0.531 | 0.831 | n.s. |
| 3 to 1 - 4 to 1 | -5.58 | 3.33 | -1.68 | 0.094 | 0.445 | n.s. |
| 3 to 1 - Cardinality1 | -0.98 | 3.31 | -0.29 | 0.768 | 0.831 | n.s. |
| 4 to 1 - Cardinality1 | 4.60 | 3.32 | 1.39 | 0.166 | 0.596 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.354, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.03 | 23 | = 0.605 | 0.23 [-0.22, 0.64] | small | n.s. |
| 2 to 1 vs 4 to 1 | -0.68 | 23 | = 0.605 | -0.18 [-0.56, 0.29] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 0.83 | 23 | = 0.605 | 0.15 [-0.26, 0.59] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.53 | 23 | = 0.605 | -0.42 [-0.74, 0.12] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.32 | 23 | = 0.755 | -0.07 [-0.49, 0.36] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 1.20 | 23 | = 0.605 | 0.34 [-0.18, 0.67] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 425.66, BIC = 443.61
- **3 to 1 vs 2 to 1**: *β* = -0.05, *SE* = 0.493, *z* = -0.101, *p* = 0.920
- **4 to 1 vs 2 to 1**: *β* = 0.36, *SE* = 0.488, *z* = 0.742, *p* = 0.458
- **Cardinality1 vs 2 to 1**: *β* = 0.27, *SE* = 0.491, *z* = 0.551, *p* = 0.581
- **SNR**: *β* = 0.39, *SE* = 0.097, *z* = 3.986, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.05 | 0.49 | 0.10 | 0.920 | 0.978 | n.s. |
| 2 to 1 - 4 to 1 | -0.36 | 0.49 | -0.74 | 0.458 | 0.954 | n.s. |
| 2 to 1 - Cardinality1 | -0.27 | 0.49 | -0.55 | 0.581 | 0.954 | n.s. |
| 3 to 1 - 4 to 1 | -0.41 | 0.49 | -0.84 | 0.401 | 0.954 | n.s. |
| 3 to 1 - Cardinality1 | -0.32 | 0.49 | -0.66 | 0.512 | 0.954 | n.s. |
| 4 to 1 - Cardinality1 | 0.09 | 0.49 | 0.19 | 0.851 | 0.978 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.49, *p* = 0.693, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.64 | 23 | = 0.786 | 0.13 [-0.29, 0.55] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.59 | 23 | = 0.786 | -0.11 [-0.54, 0.30] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | -0.14 | 23 | = 0.888 | -0.02 [-0.45, 0.39] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.09 | 23 | = 0.786 | -0.23 [-0.65, 0.20] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.72 | 23 | = 0.786 | -0.14 [-0.57, 0.28] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.45 | 23 | = 0.786 | 0.08 [-0.33, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 942.62, BIC = 960.57
- **3 to 1 vs 2 to 1**: *β* = -15.38, *SE* = 8.769, *z* = -1.754, *p* = 0.079
- **4 to 1 vs 2 to 1**: *β* = -8.72, *SE* = 8.824, *z* = -0.988, *p* = 0.323
- **Cardinality1 vs 2 to 1**: *β* = -16.32, *SE* = 8.751, *z* = -1.865, *p* = 0.062
- **SNR**: *β* = -0.48, *SE* = 0.510, *z* = -0.936, *p* = 0.350

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 15.38 | 8.77 | 1.75 | 0.079 | 0.339 | n.s. |
| 2 to 1 - 4 to 1 | 8.72 | 8.82 | 0.99 | 0.323 | 0.790 | n.s. |
| 2 to 1 - Cardinality1 | 16.32 | 8.75 | 1.86 | 0.062 | 0.320 | n.s. |
| 3 to 1 - 4 to 1 | -6.66 | 8.69 | -0.77 | 0.444 | 0.790 | n.s. |
| 3 to 1 - Cardinality1 | 0.94 | 8.97 | 0.10 | 0.917 | 0.917 | n.s. |
| 4 to 1 - Cardinality1 | 7.60 | 9.07 | 0.84 | 0.402 | 0.790 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.245, η²_G = 0.043
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 2.66 | 23 | = 0.084 | 0.56 [0.09, 1.00] | medium | n.s. |
| 2 to 1 vs 4 to 1 | 1.29 | 23 | = 0.422 | 0.32 [-0.17, 0.69] | small | n.s. |
| 2 to 1 vs Cardinality1 | 1.54 | 23 | = 0.414 | 0.48 [-0.12, 0.75] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.77 | 23 | = 0.671 | -0.21 [-0.58, 0.27] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.13 | 23 | = 0.899 | -0.04 [-0.45, 0.40] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.45 | 23 | = 0.785 | 0.16 [-0.33, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 464.69, BIC = 482.64
- **3 to 1 vs 2 to 1**: *β* = -0.20, *SE* = 0.584, *z* = -0.341, *p* = 0.733
- **4 to 1 vs 2 to 1**: *β* = 0.09, *SE* = 0.589, *z* = 0.146, *p* = 0.884
- **Cardinality1 vs 2 to 1**: *β* = -2.75, *SE* = 0.583, *z* = -4.723, *p* < .001
- **SNR**: *β* = 0.11, *SE* = 0.038, *z* = 2.917, *p* = 0.004

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.20 | 0.58 | 0.34 | 0.733 | 0.946 | n.s. |
| 2 to 1 - 4 to 1 | -0.09 | 0.59 | -0.15 | 0.884 | 0.946 | n.s. |
| 2 to 1 - Cardinality1 | 2.75 | 0.58 | 4.72 | < .001 | < .001 | *** |
| 3 to 1 - 4 to 1 | -0.29 | 0.58 | -0.49 | 0.622 | 0.946 | n.s. |
| 3 to 1 - Cardinality1 | 2.55 | 0.60 | 4.24 | < .001 | < .001 | *** |
| 4 to 1 - Cardinality1 | 2.84 | 0.61 | 4.66 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 13.21, *p* < .001, η²_G = 0.154
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | -0.11 | 23 | = 0.917 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.00 | 23 | = 0.494 | -0.12 [-0.63, 0.22] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 5.24 | 23 | < .001 | 0.99 [0.54, 1.60] | large | *** |
| 3 to 1 vs 4 to 1 | -0.56 | 23 | = 0.698 | -0.10 [-0.54, 0.31] | negligible | n.s. |
| 3 to 1 vs Cardinality1 | 3.91 | 23 | = 0.001 | 0.98 [0.31, 1.28] | large | ** |
| 4 to 1 vs Cardinality1 | 5.45 | 23 | < .001 | 1.08 [0.57, 1.65] | large | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than Cardinality1 (*d* = 0.99)
  - 3 to 1 showed greater amplitude than Cardinality1 (*d* = 0.98)
  - 4 to 1 showed greater amplitude than Cardinality1 (*d* = 1.08)

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
