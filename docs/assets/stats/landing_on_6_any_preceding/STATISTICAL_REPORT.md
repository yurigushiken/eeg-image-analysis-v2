# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:45:36

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
| 3 to 6 | 9 | 94.22 ms | 11.51 | 3.84 | [84.00, 108.00] |
| 4 to 6 | 8 | 98.50 ms | 10.46 | 3.70 | [84.00, 108.00] |
| 5 to 6 | 10 | 92.40 ms | 10.91 | 3.45 | [84.00, 108.00] |
| Cardinality6 | 9 | 96.89 ms | 10.15 | 3.38 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 9 | 2.45 µV | 1.45 | 0.48 | [1.17, 5.95] |
| 4 to 6 | 8 | 3.30 µV | 1.69 | 0.60 | [0.85, 5.65] |
| 5 to 6 | 10 | 1.85 µV | 1.15 | 0.36 | [0.36, 3.74] |
| Cardinality6 | 9 | 1.78 µV | 1.14 | 0.38 | [0.70, 4.37] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | 170.43 ms | 19.29 | 4.02 | [140.00, 208.00] |
| 4 to 6 | 22 | 167.82 ms | 22.37 | 4.77 | [136.00, 204.00] |
| 5 to 6 | 22 | 173.82 ms | 17.14 | 3.65 | [140.00, 204.00] |
| Cardinality6 | 22 | 173.09 ms | 15.38 | 3.28 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | -6.82 µV | 2.82 | 0.59 | [-12.81, -2.56] |
| 4 to 6 | 22 | -6.33 µV | 2.98 | 0.64 | [-13.20, -2.83] |
| 5 to 6 | 22 | -6.17 µV | 2.42 | 0.52 | [-11.88, -2.32] |
| Cardinality6 | 22 | -5.96 µV | 2.74 | 0.58 | [-11.14, -1.04] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 11 | 93.09 ms | 12.14 | 3.66 | [76.00, 108.00] |
| 4 to 6 | 13 | 96.92 ms | 9.82 | 2.72 | [76.00, 108.00] |
| 5 to 6 | 12 | 93.67 ms | 8.61 | 2.48 | [84.00, 108.00] |
| Cardinality6 | 13 | 94.46 ms | 11.95 | 3.31 | [76.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 11 | 3.66 µV | 2.05 | 0.62 | [1.16, 8.13] |
| 4 to 6 | 13 | 3.25 µV | 1.28 | 0.36 | [1.15, 5.39] |
| 5 to 6 | 12 | 3.14 µV | 1.45 | 0.42 | [1.09, 6.38] |
| Cardinality6 | 13 | 2.66 µV | 1.77 | 0.49 | [0.53, 7.50] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 469.47 ms | 26.10 | 5.99 | [432.00, 508.00] |
| 4 to 6 | 18 | 471.33 ms | 25.93 | 6.11 | [436.00, 508.00] |
| 5 to 6 | 8 | 462.50 ms | 19.59 | 6.93 | [432.00, 496.00] |
| Cardinality6 | 14 | 468.00 ms | 17.68 | 4.73 | [432.00, 492.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 4.49 µV | 2.20 | 0.50 | [1.70, 10.29] |
| 4 to 6 | 18 | 5.46 µV | 3.01 | 0.71 | [0.88, 9.55] |
| 5 to 6 | 8 | 4.50 µV | 3.03 | 1.07 | [1.73, 9.81] |
| Cardinality6 | 14 | 4.71 µV | 2.44 | 0.65 | [1.85, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 273.23, BIC = 284.31
- **4 to 6 vs 3 to 6**: *β* = 3.74, *SE* = 3.758, *z* = 0.995, *p* = 0.320
- **5 to 6 vs 3 to 6**: *β* = -8.45, *SE* = 3.882, *z* = -2.177, *p* = 0.029
- **Cardinality6 vs 3 to 6**: *β* = -1.06, *SE* = 3.747, *z* = -0.282, *p* = 0.778
- **SNR**: *β* = -3.38, *SE* = 1.521, *z* = -2.222, *p* = 0.026

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -3.74 | 3.76 | -0.99 | 0.320 | 0.566 | n.s. |
| 3 to 6 - 5 to 6 | 8.45 | 3.88 | 2.18 | 0.029 | 0.135 | n.s. |
| 3 to 6 - Cardinality6 | 1.06 | 3.75 | 0.28 | 0.778 | 0.778 | n.s. |
| 4 to 6 - 5 to 6 | 12.19 | 4.29 | 2.84 | 0.004 | 0.026 | * |
| 4 to 6 - Cardinality6 | 4.80 | 4.11 | 1.17 | 0.243 | 0.566 | n.s. |
| 5 to 6 - Cardinality6 | -7.39 | 3.38 | -2.19 | 0.029 | 0.135 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 105.18, BIC = 116.27
- **4 to 6 vs 3 to 6**: *β* = 0.66, *SE* = 0.363, *z* = 1.813, *p* = 0.070
- **5 to 6 vs 3 to 6**: *β* = 0.56, *SE* = 0.367, *z* = 1.528, *p* = 0.126
- **Cardinality6 vs 3 to 6**: *β* = 0.14, *SE* = 0.368, *z* = 0.372, *p* = 0.710
- **SNR**: *β* = 1.00, *SE* = 0.148, *z* = 6.800, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.66 | 0.36 | -1.81 | 0.070 | 0.352 | n.s. |
| 3 to 6 - 5 to 6 | -0.56 | 0.37 | -1.53 | 0.126 | 0.491 | n.s. |
| 3 to 6 - Cardinality6 | -0.14 | 0.37 | -0.37 | 0.710 | 0.916 | n.s. |
| 4 to 6 - 5 to 6 | 0.10 | 0.42 | 0.23 | 0.820 | 0.916 | n.s. |
| 4 to 6 - Cardinality6 | 0.52 | 0.40 | 1.31 | 0.189 | 0.567 | n.s. |
| 5 to 6 - Cardinality6 | 0.42 | 0.33 | 1.28 | 0.202 | 0.567 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 753.18, BIC = 770.60
- **4 to 6 vs 3 to 6**: *β* = -2.76, *SE* = 3.645, *z* = -0.757, *p* = 0.449
- **5 to 6 vs 3 to 6**: *β* = 3.06, *SE* = 3.640, *z* = 0.840, *p* = 0.401
- **Cardinality6 vs 3 to 6**: *β* = 4.10, *SE* = 3.816, *z* = 1.073, *p* = 0.283
- **SNR**: *β* = 0.76, *SE* = 0.709, *z* = 1.076, *p* = 0.282

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 2.76 | 3.64 | 0.76 | 0.449 | 0.785 | n.s. |
| 3 to 6 - 5 to 6 | -3.06 | 3.64 | -0.84 | 0.401 | 0.785 | n.s. |
| 3 to 6 - Cardinality6 | -4.10 | 3.82 | -1.07 | 0.283 | 0.736 | n.s. |
| 4 to 6 - 5 to 6 | -5.82 | 3.66 | -1.59 | 0.112 | 0.448 | n.s. |
| 4 to 6 - Cardinality6 | -6.85 | 3.78 | -1.81 | 0.070 | 0.353 | n.s. |
| 5 to 6 - Cardinality6 | -1.04 | 3.83 | -0.27 | 0.786 | 0.786 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.11, *p* = 0.354, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.81 | 20 | = 0.517 | 0.14 [-0.24, 0.65] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -0.80 | 20 | = 0.517 | -0.20 [-0.59, 0.30] | negligible | n.s. |
| 3 to 6 vs Cardinality6 | -0.89 | 20 | = 0.517 | -0.18 [-0.65, 0.27] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -1.22 | 20 | = 0.517 | -0.32 [-0.71, 0.19] | small | n.s. |
| 4 to 6 vs Cardinality6 | -1.45 | 20 | = 0.517 | -0.31 [-0.78, 0.15] | small | n.s. |
| 5 to 6 vs Cardinality6 | 0.13 | 20 | = 0.897 | 0.02 [-0.43, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 351.35, BIC = 368.77
- **4 to 6 vs 3 to 6**: *β* = 0.40, *SE* = 0.362, *z* = 1.111, *p* = 0.267
- **5 to 6 vs 3 to 6**: *β* = 0.68, *SE* = 0.362, *z* = 1.880, *p* = 0.060
- **Cardinality6 vs 3 to 6**: *β* = 0.38, *SE* = 0.381, *z* = 0.999, *p* = 0.318
- **SNR**: *β* = -0.47, *SE* = 0.072, *z* = -6.561, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.40 | 0.36 | -1.11 | 0.267 | 0.788 | n.s. |
| 3 to 6 - 5 to 6 | -0.68 | 0.36 | -1.88 | 0.060 | 0.311 | n.s. |
| 3 to 6 - Cardinality6 | -0.38 | 0.38 | -1.00 | 0.318 | 0.788 | n.s. |
| 4 to 6 - 5 to 6 | -0.28 | 0.36 | -0.76 | 0.445 | 0.818 | n.s. |
| 4 to 6 - Cardinality6 | 0.02 | 0.38 | 0.06 | 0.955 | 0.955 | n.s. |
| 5 to 6 - Cardinality6 | 0.30 | 0.38 | 0.78 | 0.433 | 0.818 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.92, *p* = 0.136, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.10 | 20 | = 0.427 | -0.19 [-0.71, 0.19] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -1.37 | 20 | = 0.375 | -0.27 [-0.78, 0.13] | small | n.s. |
| 3 to 6 vs Cardinality6 | -2.45 | 20 | = 0.142 | -0.39 [-1.02, -0.05] | small | n.s. |
| 4 to 6 vs 5 to 6 | -0.28 | 20 | = 0.785 | -0.06 [-0.51, 0.37] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | -1.81 | 20 | = 0.254 | -0.20 [-0.87, 0.08] | negligible | n.s. |
| 5 to 6 vs Cardinality6 | -0.87 | 20 | = 0.472 | -0.16 [-0.65, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 376.85, BIC = 390.09
- **4 to 6 vs 3 to 6**: *β* = 5.60, *SE* = 3.950, *z* = 1.417, *p* = 0.156
- **5 to 6 vs 3 to 6**: *β* = 1.99, *SE* = 4.039, *z* = 0.493, *p* = 0.622
- **Cardinality6 vs 3 to 6**: *β* = 3.39, *SE* = 4.028, *z* = 0.843, *p* = 0.399
- **SNR**: *β* = 2.26, *SE* = 1.235, *z* = 1.828, *p* = 0.068

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -5.60 | 3.95 | -1.42 | 0.156 | 0.640 | n.s. |
| 3 to 6 - 5 to 6 | -1.99 | 4.04 | -0.49 | 0.622 | 0.911 | n.s. |
| 3 to 6 - Cardinality6 | -3.39 | 4.03 | -0.84 | 0.399 | 0.881 | n.s. |
| 4 to 6 - 5 to 6 | 3.61 | 3.84 | 0.94 | 0.347 | 0.881 | n.s. |
| 4 to 6 - Cardinality6 | 2.20 | 3.72 | 0.59 | 0.553 | 0.911 | n.s. |
| 5 to 6 - Cardinality6 | -1.40 | 3.83 | -0.37 | 0.714 | 0.911 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.57, *p* = 0.264, η²_G = 0.200
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.58 | 3 | = 0.718 | -0.33 [-1.01, 0.55] | small | n.s. |
| 3 to 6 vs 5 to 6 | -2.04 | 3 | = 0.403 | -1.30 [-1.82, 0.50] | large | n.s. |
| 3 to 6 vs Cardinality6 | -0.40 | 3 | = 0.718 | -0.20 [-1.13, 0.97] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -0.98 | 3 | = 0.718 | -0.74 [-1.15, 0.72] | medium | n.s. |
| 4 to 6 vs Cardinality6 | 0.52 | 3 | = 0.718 | 0.17 [-0.59, 1.32] | negligible | n.s. |
| 5 to 6 vs Cardinality6 | 2.10 | 3 | = 0.403 | 1.14 [-0.89, 0.96] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 165.65, BIC = 178.89
- **4 to 6 vs 3 to 6**: *β* = 0.45, *SE* = 0.414, *z* = 1.096, *p* = 0.273
- **5 to 6 vs 3 to 6**: *β* = 0.04, *SE* = 0.433, *z* = 0.099, *p* = 0.921
- **Cardinality6 vs 3 to 6**: *β* = -0.04, *SE* = 0.432, *z* = -0.090, *p* = 0.928
- **SNR**: *β* = 0.96, *SE* = 0.139, *z* = 6.903, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.45 | 0.41 | -1.10 | 0.273 | 0.797 | n.s. |
| 3 to 6 - 5 to 6 | -0.04 | 0.43 | -0.10 | 0.921 | 0.996 | n.s. |
| 3 to 6 - Cardinality6 | 0.04 | 0.43 | 0.09 | 0.928 | 0.996 | n.s. |
| 4 to 6 - 5 to 6 | 0.41 | 0.40 | 1.02 | 0.306 | 0.797 | n.s. |
| 4 to 6 - Cardinality6 | 0.49 | 0.39 | 1.25 | 0.210 | 0.758 | n.s. |
| 5 to 6 - Cardinality6 | 0.08 | 0.40 | 0.20 | 0.838 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.93, *p* = 0.465, η²_G = 0.167
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.24 | 3 | = 0.828 | -0.17 [-0.61, 0.94] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 0.50 | 3 | = 0.781 | 0.47 [-1.01, 1.08] | small | n.s. |
| 3 to 6 vs Cardinality6 | 2.23 | 3 | = 0.457 | 1.00 [-0.48, 1.86] | large | n.s. |
| 4 to 6 vs 5 to 6 | 1.16 | 3 | = 0.663 | 0.56 [-0.97, 0.88] | medium | n.s. |
| 4 to 6 vs Cardinality6 | 1.91 | 3 | = 0.457 | 0.97 [-0.02, 2.40] | large | n.s. |
| 5 to 6 vs Cardinality6 | 0.56 | 3 | = 0.781 | 0.41 [-1.26, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 549.92, BIC = 564.46
- **4 to 6 vs 3 to 6**: *β* = 2.12, *SE* = 7.622, *z* = 0.278, *p* = 0.781
- **5 to 6 vs 3 to 6**: *β* = -6.99, *SE* = 9.520, *z* = -0.734, *p* = 0.463
- **Cardinality6 vs 3 to 6**: *β* = -1.37, *SE* = 7.961, *z* = -0.172, *p* = 0.864
- **SNR**: *β* = -0.15, *SE* = 1.226, *z* = -0.120, *p* = 0.904

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -2.12 | 7.62 | -0.28 | 0.781 | 0.968 | n.s. |
| 3 to 6 - 5 to 6 | 6.98 | 9.52 | 0.73 | 0.463 | 0.955 | n.s. |
| 3 to 6 - Cardinality6 | 1.37 | 7.96 | 0.17 | 0.864 | 0.968 | n.s. |
| 4 to 6 - 5 to 6 | 9.11 | 9.78 | 0.93 | 0.352 | 0.926 | n.s. |
| 4 to 6 - Cardinality6 | 3.49 | 8.16 | 0.43 | 0.669 | 0.968 | n.s. |
| 5 to 6 - Cardinality6 | -5.62 | 10.03 | -0.56 | 0.575 | 0.968 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.583, η²_G = 0.103
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.86 | 5 | = 0.866 | 0.61 [-0.64, 0.43] | medium | n.s. |
| 3 to 6 vs 5 to 6 | 1.27 | 5 | = 0.866 | 0.83 [-0.54, 1.17] | large | n.s. |
| 3 to 6 vs Cardinality6 | 0.76 | 5 | = 0.866 | 0.52 [-0.54, 0.67] | medium | n.s. |
| 4 to 6 vs 5 to 6 | 0.11 | 5 | = 0.916 | 0.07 [-0.59, 1.11] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | -0.38 | 5 | = 0.866 | -0.14 [-0.58, 0.70] | negligible | n.s. |
| 5 to 6 vs Cardinality6 | -0.45 | 5 | = 0.866 | -0.26 [-1.24, 0.88] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 237.06, BIC = 251.60
- **4 to 6 vs 3 to 6**: *β* = 0.07, *SE* = 0.431, *z* = 0.152, *p* = 0.879
- **5 to 6 vs 3 to 6**: *β* = -0.30, *SE* = 0.532, *z* = -0.573, *p* = 0.566
- **Cardinality6 vs 3 to 6**: *β* = -0.01, *SE* = 0.438, *z* = -0.025, *p* = 0.980
- **SNR**: *β* = 0.63, *SE* = 0.093, *z* = 6.774, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.07 | 0.43 | -0.15 | 0.879 | 0.998 | n.s. |
| 3 to 6 - 5 to 6 | 0.31 | 0.53 | 0.57 | 0.566 | 0.985 | n.s. |
| 3 to 6 - Cardinality6 | 0.01 | 0.44 | 0.03 | 0.980 | 0.998 | n.s. |
| 4 to 6 - 5 to 6 | 0.37 | 0.55 | 0.67 | 0.503 | 0.985 | n.s. |
| 4 to 6 - Cardinality6 | 0.08 | 0.47 | 0.16 | 0.869 | 0.998 | n.s. |
| 5 to 6 - Cardinality6 | -0.29 | 0.56 | -0.52 | 0.601 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.79, *p* = 0.520, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.19 | 5 | = 0.715 | -0.34 [-1.23, -0.06] | small | n.s. |
| 3 to 6 vs 5 to 6 | -0.70 | 5 | = 0.739 | -0.23 [-0.62, 1.07] | small | n.s. |
| 3 to 6 vs Cardinality6 | 0.35 | 5 | = 0.739 | 0.14 [-0.83, 0.39] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 0.40 | 5 | = 0.739 | 0.07 [-0.40, 1.37] | negligible | n.s. |
| 4 to 6 vs Cardinality6 | 1.04 | 5 | = 0.715 | 0.45 [-0.14, 1.21] | small | n.s. |
| 5 to 6 vs Cardinality6 | 1.01 | 5 | = 0.715 | 0.33 [-0.68, 1.51] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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
