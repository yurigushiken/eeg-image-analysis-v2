# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:29:17

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
| 3 to 6 | 24 | 97.33 ms | 10.19 | 2.08 | [84.00, 108.00] |
| 4 to 6 | 24 | 98.00 ms | 9.29 | 1.90 | [84.00, 108.00] |
| 5 to 6 | 24 | 97.00 ms | 9.08 | 1.85 | [84.00, 108.00] |
| Cardinality6 | 24 | 97.83 ms | 9.73 | 1.99 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | -1.74 µV | 2.46 | 0.50 | [-4.88, 4.77] |
| 4 to 6 | 24 | -1.15 µV | 2.14 | 0.44 | [-4.45, 3.10] |
| 5 to 6 | 24 | -1.64 µV | 1.85 | 0.38 | [-5.35, 1.09] |
| Cardinality6 | 24 | -2.20 µV | 2.31 | 0.47 | [-7.15, 0.96] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 172.00 ms | 20.36 | 4.16 | [140.00, 208.00] |
| 4 to 6 | 24 | 168.50 ms | 22.30 | 4.55 | [136.00, 204.00] |
| 5 to 6 | 24 | 174.50 ms | 18.23 | 3.72 | [140.00, 208.00] |
| Cardinality6 | 24 | 175.67 ms | 17.13 | 3.50 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | -6.66 µV | 2.86 | 0.58 | [-12.81, -2.56] |
| 4 to 6 | 24 | -5.97 µV | 3.18 | 0.65 | [-13.20, 0.34] |
| 5 to 6 | 24 | -5.78 µV | 2.67 | 0.55 | [-11.88, -0.44] |
| Cardinality6 | 24 | -5.40 µV | 3.26 | 0.67 | [-11.14, 2.35] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 91.83 ms | 13.11 | 2.68 | [76.00, 108.00] |
| 4 to 6 | 24 | 95.33 ms | 11.83 | 2.42 | [76.00, 108.00] |
| 5 to 6 | 24 | 95.00 ms | 10.89 | 2.22 | [76.00, 108.00] |
| Cardinality6 | 24 | 93.67 ms | 12.97 | 2.65 | [76.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 1.64 µV | 2.53 | 0.52 | [-2.13, 8.13] |
| 4 to 6 | 24 | 1.62 µV | 2.17 | 0.44 | [-1.72, 5.39] |
| 5 to 6 | 24 | 1.43 µV | 2.17 | 0.44 | [-2.96, 6.38] |
| Cardinality6 | 24 | 1.57 µV | 1.89 | 0.39 | [-1.34, 7.50] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 471.17 ms | 29.08 | 5.94 | [432.00, 508.00] |
| 4 to 6 | 24 | 472.83 ms | 25.05 | 5.11 | [436.00, 508.00] |
| 5 to 6 | 24 | 470.83 ms | 26.23 | 5.35 | [432.00, 508.00] |
| Cardinality6 | 24 | 462.83 ms | 22.02 | 4.49 | [432.00, 500.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 3.46 µV | 2.95 | 0.60 | [-3.85, 10.29] |
| 4 to 6 | 24 | 4.17 µV | 3.49 | 0.71 | [-1.42, 9.55] |
| 5 to 6 | 24 | 1.27 µV | 3.35 | 0.68 | [-4.86, 9.81] |
| Cardinality6 | 24 | 2.28 µV | 3.58 | 0.73 | [-3.43, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 713.26, BIC = 731.21
- **4 to 6 vs 3 to 6**: *β* = 0.75, *SE* = 2.545, *z* = 0.293, *p* = 0.770
- **5 to 6 vs 3 to 6**: *β* = 0.14, *SE* = 2.574, *z* = 0.055, *p* = 0.956
- **Cardinality6 vs 3 to 6**: *β* = 0.28, *SE* = 2.551, *z* = 0.108, *p* = 0.914
- **SNR**: *β* = 0.73, *SE* = 0.599, *z* = 1.220, *p* = 0.223

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.75 | 2.55 | -0.29 | 0.770 | 1.000 | n.s. |
| 3 to 6 - 5 to 6 | -0.14 | 2.57 | -0.05 | 0.956 | 1.000 | n.s. |
| 3 to 6 - Cardinality6 | -0.28 | 2.55 | -0.11 | 0.914 | 1.000 | n.s. |
| 4 to 6 - 5 to 6 | 0.60 | 2.56 | 0.24 | 0.814 | 1.000 | n.s. |
| 4 to 6 - Cardinality6 | 0.47 | 2.56 | 0.18 | 0.854 | 1.000 | n.s. |
| 5 to 6 - Cardinality6 | -0.13 | 2.61 | -0.05 | 0.959 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.06, *p* = 0.980, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.27 | 23 | = 0.946 | -0.07 [-0.48, 0.37] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 0.13 | 23 | = 0.946 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| 3 to 6 vs Cardinality6 | -0.20 | 23 | = 0.946 | -0.05 [-0.46, 0.38] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 0.34 | 23 | = 0.946 | 0.11 [-0.35, 0.49] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | 0.07 | 23 | = 0.946 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 5 to 6 vs Cardinality6 | -0.32 | 23 | = 0.946 | -0.09 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 422.33, BIC = 440.28
- **4 to 6 vs 3 to 6**: *β* = 0.54, *SE* = 0.563, *z* = 0.956, *p* = 0.339
- **5 to 6 vs 3 to 6**: *β* = -0.17, *SE* = 0.570, *z* = -0.307, *p* = 0.758
- **Cardinality6 vs 3 to 6**: *β* = -0.34, *SE* = 0.565, *z* = -0.598, *p* = 0.550
- **SNR**: *β* = -0.42, *SE* = 0.135, *z* = -3.121, *p* = 0.002

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.54 | 0.56 | -0.96 | 0.339 | 0.809 | n.s. |
| 3 to 6 - 5 to 6 | 0.18 | 0.57 | 0.31 | 0.758 | 0.942 | n.s. |
| 3 to 6 - Cardinality6 | 0.34 | 0.56 | 0.60 | 0.550 | 0.909 | n.s. |
| 4 to 6 - 5 to 6 | 0.71 | 0.57 | 1.26 | 0.209 | 0.690 | n.s. |
| 4 to 6 - Cardinality6 | 0.88 | 0.57 | 1.55 | 0.122 | 0.541 | n.s. |
| 5 to 6 - Cardinality6 | 0.16 | 0.58 | 0.28 | 0.779 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.373, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.98 | 23 | = 0.506 | -0.25 [-0.63, 0.23] | small | n.s. |
| 3 to 6 vs 5 to 6 | -0.16 | 23 | = 0.871 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| 3 to 6 vs Cardinality6 | 0.82 | 23 | = 0.506 | 0.20 [-0.26, 0.59] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 0.87 | 23 | = 0.506 | 0.24 [-0.25, 0.60] | small | n.s. |
| 4 to 6 vs Cardinality6 | 1.60 | 23 | = 0.506 | 0.47 [-0.11, 0.76] | small | n.s. |
| 5 to 6 vs Cardinality6 | 0.98 | 23 | = 0.506 | 0.27 [-0.23, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 819.07, BIC = 837.02
- **4 to 6 vs 3 to 6**: *β* = -3.15, *SE* = 3.667, *z* = -0.859, *p* = 0.390
- **5 to 6 vs 3 to 6**: *β* = 2.65, *SE* = 3.656, *z* = 0.725, *p* = 0.468
- **Cardinality6 vs 3 to 6**: *β* = 4.82, *SE* = 3.796, *z* = 1.269, *p* = 0.204
- **SNR**: *β* = 0.83, *SE* = 0.746, *z* = 1.118, *p* = 0.264

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 3.15 | 3.67 | 0.86 | 0.390 | 0.773 | n.s. |
| 3 to 6 - 5 to 6 | -2.65 | 3.66 | -0.73 | 0.468 | 0.773 | n.s. |
| 3 to 6 - Cardinality6 | -4.82 | 3.80 | -1.27 | 0.204 | 0.599 | n.s. |
| 4 to 6 - 5 to 6 | -5.80 | 3.66 | -1.59 | 0.113 | 0.450 | n.s. |
| 4 to 6 - Cardinality6 | -7.97 | 3.72 | -2.14 | 0.032 | 0.179 | n.s. |
| 5 to 6 - Cardinality6 | -2.17 | 3.76 | -0.58 | 0.565 | 0.773 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.38, *p* = 0.257, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 1.12 | 23 | = 0.517 | 0.16 [-0.20, 0.66] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -0.66 | 23 | = 0.617 | -0.13 [-0.56, 0.29] | negligible | n.s. |
| 3 to 6 vs Cardinality6 | -0.97 | 23 | = 0.517 | -0.19 [-0.62, 0.23] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -1.33 | 23 | = 0.517 | -0.29 [-0.70, 0.16] | small | n.s. |
| 4 to 6 vs Cardinality6 | -1.75 | 23 | = 0.517 | -0.36 [-0.79, 0.08] | small | n.s. |
| 5 to 6 vs Cardinality6 | -0.34 | 23 | = 0.739 | -0.07 [-0.49, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 398.01, BIC = 415.96
- **4 to 6 vs 3 to 6**: *β* = 0.49, *SE* = 0.394, *z* = 1.242, *p* = 0.214
- **5 to 6 vs 3 to 6**: *β* = 0.79, *SE* = 0.393, *z* = 2.006, *p* = 0.045
- **Cardinality6 vs 3 to 6**: *β* = 0.61, *SE* = 0.408, *z* = 1.486, *p* = 0.137
- **SNR**: *β* = -0.47, *SE* = 0.081, *z* = -5.845, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.49 | 0.39 | -1.24 | 0.214 | 0.619 | n.s. |
| 3 to 6 - 5 to 6 | -0.79 | 0.39 | -2.01 | 0.045 | 0.241 | n.s. |
| 3 to 6 - Cardinality6 | -0.61 | 0.41 | -1.49 | 0.137 | 0.522 | n.s. |
| 4 to 6 - 5 to 6 | -0.30 | 0.39 | -0.76 | 0.448 | 0.831 | n.s. |
| 4 to 6 - Cardinality6 | -0.12 | 0.40 | -0.29 | 0.770 | 0.880 | n.s. |
| 5 to 6 - Cardinality6 | 0.18 | 0.40 | 0.45 | 0.654 | 0.880 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.68, *p* = 0.054, η²_G = 0.023
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.44 | 23 | = 0.246 | -0.23 [-0.72, 0.14] | small | n.s. |
| 3 to 6 vs 5 to 6 | -1.87 | 23 | = 0.153 | -0.32 [-0.82, 0.06] | small | n.s. |
| 3 to 6 vs Cardinality6 | -2.45 | 23 | = 0.134 | -0.41 [-0.95, -0.05] | small | n.s. |
| 4 to 6 vs 5 to 6 | -0.40 | 23 | = 0.693 | -0.06 [-0.50, 0.34] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | -1.86 | 23 | = 0.153 | -0.18 [-0.82, 0.06] | negligible | n.s. |
| 5 to 6 vs Cardinality6 | -0.82 | 23 | = 0.504 | -0.13 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 758.02, BIC = 775.97
- **4 to 6 vs 3 to 6**: *β* = 4.05, *SE* = 3.314, *z* = 1.222, *p* = 0.222
- **5 to 6 vs 3 to 6**: *β* = 4.06, *SE* = 3.329, *z* = 1.221, *p* = 0.222
- **Cardinality6 vs 3 to 6**: *β* = 2.96, *SE* = 3.342, *z* = 0.887, *p* = 0.375
- **SNR**: *β* = 2.39, *SE* = 1.039, *z* = 2.296, *p* = 0.022

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -4.05 | 3.31 | -1.22 | 0.222 | 0.778 | n.s. |
| 3 to 6 - 5 to 6 | -4.06 | 3.33 | -1.22 | 0.222 | 0.778 | n.s. |
| 3 to 6 - Cardinality6 | -2.97 | 3.34 | -0.89 | 0.375 | 0.847 | n.s. |
| 4 to 6 - 5 to 6 | -0.01 | 3.31 | -0.00 | 0.997 | 0.997 | n.s. |
| 4 to 6 - Cardinality6 | 1.08 | 3.32 | 0.33 | 0.744 | 0.982 | n.s. |
| 5 to 6 - Cardinality6 | 1.10 | 3.31 | 0.33 | 0.740 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.747, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.06 | 23 | = 0.864 | -0.28 [-0.64, 0.21] | small | n.s. |
| 3 to 6 vs 5 to 6 | -1.02 | 23 | = 0.864 | -0.26 [-0.64, 0.22] | small | n.s. |
| 3 to 6 vs Cardinality6 | -0.44 | 23 | = 0.864 | -0.14 [-0.51, 0.33] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 0.10 | 23 | = 0.921 | 0.03 [-0.40, 0.44] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | 0.48 | 23 | = 0.864 | 0.13 [-0.33, 0.52] | negligible | n.s. |
| 5 to 6 vs Cardinality6 | 0.36 | 23 | = 0.864 | 0.11 [-0.35, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 424.45, BIC = 442.40
- **4 to 6 vs 3 to 6**: *β* = 0.06, *SE* = 0.537, *z* = 0.110, *p* = 0.913
- **5 to 6 vs 3 to 6**: *β* = -0.07, *SE* = 0.539, *z* = -0.132, *p* = 0.895
- **Cardinality6 vs 3 to 6**: *β* = 0.11, *SE* = 0.542, *z* = 0.205, *p* = 0.838
- **SNR**: *β* = 0.38, *SE* = 0.179, *z* = 2.120, *p* = 0.034

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.06 | 0.54 | -0.11 | 0.913 | 1.000 | n.s. |
| 3 to 6 - 5 to 6 | 0.07 | 0.54 | 0.13 | 0.895 | 1.000 | n.s. |
| 3 to 6 - Cardinality6 | -0.11 | 0.54 | -0.20 | 0.838 | 1.000 | n.s. |
| 4 to 6 - 5 to 6 | 0.13 | 0.54 | 0.24 | 0.808 | 1.000 | n.s. |
| 4 to 6 - Cardinality6 | -0.05 | 0.54 | -0.10 | 0.923 | 1.000 | n.s. |
| 5 to 6 - Cardinality6 | -0.18 | 0.54 | -0.34 | 0.734 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.06, *p* = 0.982, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.07 | 23 | = 0.950 | 0.01 [-0.41, 0.44] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 0.35 | 23 | = 0.950 | 0.09 [-0.35, 0.49] | negligible | n.s. |
| 3 to 6 vs Cardinality6 | 0.11 | 23 | = 0.950 | 0.03 [-0.40, 0.44] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 0.36 | 23 | = 0.950 | 0.09 [-0.35, 0.50] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | 0.06 | 23 | = 0.950 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 5 to 6 vs Cardinality6 | -0.26 | 23 | = 0.950 | -0.07 [-0.48, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 901.10, BIC = 919.05
- **4 to 6 vs 3 to 6**: *β* = 3.46, *SE* = 6.970, *z* = 0.497, *p* = 0.619
- **5 to 6 vs 3 to 6**: *β* = -0.70, *SE* = 6.917, *z* = -0.101, *p* = 0.920
- **Cardinality6 vs 3 to 6**: *β* = -7.56, *SE* = 6.925, *z* = -1.092, *p* = 0.275
- **SNR**: *β* = -1.97, *SE* = 0.961, *z* = -2.050, *p* = 0.040

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -3.46 | 6.97 | -0.50 | 0.619 | 0.910 | n.s. |
| 3 to 6 - 5 to 6 | 0.70 | 6.92 | 0.10 | 0.920 | 0.920 | n.s. |
| 3 to 6 - Cardinality6 | 7.56 | 6.92 | 1.09 | 0.275 | 0.799 | n.s. |
| 4 to 6 - 5 to 6 | 4.16 | 6.99 | 0.60 | 0.552 | 0.910 | n.s. |
| 4 to 6 - Cardinality6 | 11.03 | 6.93 | 1.59 | 0.112 | 0.509 | n.s. |
| 5 to 6 - Cardinality6 | 6.86 | 6.94 | 0.99 | 0.322 | 0.799 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.509, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.20 | 23 | = 0.966 | -0.06 [-0.46, 0.38] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 0.04 | 23 | = 0.966 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 3 to 6 vs Cardinality6 | 1.14 | 23 | = 0.530 | 0.32 [-0.19, 0.66] | small | n.s. |
| 4 to 6 vs 5 to 6 | 0.32 | 23 | = 0.966 | 0.08 [-0.36, 0.49] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | 1.64 | 23 | = 0.530 | 0.42 [-0.10, 0.77] | small | n.s. |
| 5 to 6 vs Cardinality6 | 1.18 | 23 | = 0.530 | 0.33 [-0.19, 0.67] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 464.62, BIC = 482.57
- **4 to 6 vs 3 to 6**: *β* = 0.49, *SE* = 0.568, *z* = 0.868, *p* = 0.385
- **5 to 6 vs 3 to 6**: *β* = -2.14, *SE* = 0.562, *z* = -3.806, *p* < .001
- **Cardinality6 vs 3 to 6**: *β* = -1.27, *SE* = 0.563, *z* = -2.258, *p* = 0.024
- **SNR**: *β* = 0.24, *SE* = 0.095, *z* = 2.541, *p* = 0.011

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.49 | 0.57 | -0.87 | 0.385 | 0.385 | n.s. |
| 3 to 6 - 5 to 6 | 2.14 | 0.56 | 3.81 | < .001 | < .001 | *** |
| 3 to 6 - Cardinality6 | 1.27 | 0.56 | 2.26 | 0.024 | 0.070 | n.s. |
| 4 to 6 - 5 to 6 | 2.63 | 0.57 | 4.61 | < .001 | < .001 | *** |
| 4 to 6 - Cardinality6 | 1.76 | 0.56 | 3.13 | 0.002 | 0.007 | ** |
| 5 to 6 - Cardinality6 | -0.87 | 0.56 | -1.54 | 0.124 | 0.233 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.11, *p* < .001, η²_G = 0.102
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.54 | 23 | = 0.136 | -0.22 [-0.75, 0.12] | small | n.s. |
| 3 to 6 vs 5 to 6 | 4.04 | 23 | = 0.002 | 0.69 [0.34, 1.31] | medium | ** |
| 3 to 6 vs Cardinality6 | 1.58 | 23 | = 0.136 | 0.36 [-0.11, 0.76] | small | n.s. |
| 4 to 6 vs 5 to 6 | 5.14 | 23 | < .001 | 0.85 [0.52, 1.58] | large | *** |
| 4 to 6 vs Cardinality6 | 3.01 | 23 | = 0.012 | 0.53 [0.15, 1.08] | medium | * |
| 5 to 6 vs Cardinality6 | -1.62 | 23 | = 0.136 | -0.29 [-0.76, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.054)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 3 to 6 showed greater amplitude than 5 to 6 (*d* = 0.69)
  - 4 to 6 showed greater amplitude than 5 to 6 (*d* = 0.85)
  - 4 to 6 showed greater amplitude than Cardinality6 (*d* = 0.53)

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
