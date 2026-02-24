# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:27:35

---

## 1. Analysis Overview

**Total Measurements:** 480
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 1 to 2 | 24 | 105.83 ms | 9.29 | 1.90 | [96.00, 116.00] |
| 3 to 2 | 24 | 105.50 ms | 8.73 | 1.78 | [96.00, 116.00] |
| 4 to 2 | 24 | 107.50 ms | 7.49 | 1.53 | [96.00, 116.00] |
| 5 to 2 | 24 | 104.00 ms | 8.34 | 1.70 | [96.00, 116.00] |
| Cardinality2 | 24 | 108.33 ms | 7.91 | 1.61 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -0.23 µV | 2.47 | 0.50 | [-6.41, 5.38] |
| 3 to 2 | 24 | -1.13 µV | 2.30 | 0.47 | [-5.65, 2.93] |
| 4 to 2 | 24 | -0.66 µV | 2.51 | 0.51 | [-4.94, 4.79] |
| 5 to 2 | 24 | -2.02 µV | 2.53 | 0.52 | [-6.23, 2.53] |
| Cardinality2 | 24 | -0.92 µV | 2.16 | 0.44 | [-5.94, 4.65] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 170.50 ms | 18.19 | 3.71 | [144.00, 208.00] |
| 3 to 2 | 24 | 176.17 ms | 23.07 | 4.71 | [144.00, 212.00] |
| 4 to 2 | 24 | 174.83 ms | 15.22 | 3.11 | [148.00, 212.00] |
| 5 to 2 | 24 | 174.17 ms | 17.61 | 3.60 | [148.00, 212.00] |
| Cardinality2 | 24 | 175.00 ms | 21.01 | 4.29 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | -5.32 µV | 2.41 | 0.49 | [-9.95, -0.26] |
| 3 to 2 | 24 | -5.79 µV | 2.54 | 0.52 | [-10.33, -1.35] |
| 4 to 2 | 24 | -6.14 µV | 3.05 | 0.62 | [-11.92, -1.89] |
| 5 to 2 | 24 | -6.56 µV | 3.01 | 0.61 | [-11.17, -1.41] |
| Cardinality2 | 24 | -5.33 µV | 2.75 | 0.56 | [-10.50, -0.87] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 111.67 ms | 7.73 | 1.58 | [104.00, 120.00] |
| 3 to 2 | 24 | 113.33 ms | 7.04 | 1.44 | [104.00, 120.00] |
| 4 to 2 | 24 | 113.33 ms | 6.74 | 1.38 | [104.00, 120.00] |
| 5 to 2 | 24 | 111.50 ms | 6.91 | 1.41 | [104.00, 120.00] |
| Cardinality2 | 24 | 112.50 ms | 6.91 | 1.41 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 0.24 µV | 2.27 | 0.46 | [-4.56, 5.23] |
| 3 to 2 | 24 | 0.56 µV | 2.29 | 0.47 | [-2.89, 5.61] |
| 4 to 2 | 24 | 0.72 µV | 2.74 | 0.56 | [-5.85, 4.31] |
| 5 to 2 | 24 | 1.74 µV | 2.44 | 0.50 | [-3.27, 6.20] |
| Cardinality2 | 24 | 0.86 µV | 3.07 | 0.63 | [-7.98, 7.57] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 479.50 ms | 42.73 | 8.72 | [420.00, 540.00] |
| 3 to 2 | 24 | 485.83 ms | 36.01 | 7.35 | [432.00, 540.00] |
| 4 to 2 | 24 | 472.33 ms | 38.56 | 7.87 | [420.00, 540.00] |
| 5 to 2 | 24 | 479.00 ms | 37.92 | 7.74 | [420.00, 540.00] |
| Cardinality2 | 24 | 465.67 ms | 31.03 | 6.33 | [420.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 2 | 24 | 3.99 µV | 3.80 | 0.78 | [-3.51, 11.52] |
| 3 to 2 | 24 | 5.05 µV | 4.52 | 0.92 | [-2.08, 17.81] |
| 4 to 2 | 24 | 4.26 µV | 3.80 | 0.78 | [-3.50, 11.62] |
| 5 to 2 | 24 | 4.51 µV | 3.45 | 0.70 | [-2.27, 13.53] |
| Cardinality2 | 24 | 2.04 µV | 3.44 | 0.70 | [-5.35, 10.57] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 860.96, BIC = 883.26
- **3 to 2 vs 1 to 2**: *β* = -0.40, *SE* = 2.323, *z* = -0.173, *p* = 0.863
- **4 to 2 vs 1 to 2**: *β* = 1.69, *SE* = 2.317, *z* = 0.730, *p* = 0.465
- **5 to 2 vs 1 to 2**: *β* = -1.94, *SE* = 2.333, *z* = -0.833, *p* = 0.405
- **Cardinality2 vs 1 to 2**: *β* = 2.60, *SE* = 2.331, *z* = 1.117, *p* = 0.264
- **SNR**: *β* = 0.23, *SE* = 0.578, *z* = 0.391, *p* = 0.696

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | 0.40 | 2.32 | 0.17 | 0.863 | 0.937 | n.s. |
| 1 to 2 - 4 to 2 | -1.69 | 2.32 | -0.73 | 0.465 | 0.937 | n.s. |
| 1 to 2 - 5 to 2 | 1.94 | 2.33 | 0.83 | 0.405 | 0.937 | n.s. |
| 1 to 2 - Cardinality2 | -2.60 | 2.33 | -1.12 | 0.264 | 0.883 | n.s. |
| 3 to 2 - 4 to 2 | -2.09 | 2.33 | -0.90 | 0.369 | 0.937 | n.s. |
| 3 to 2 - 5 to 2 | 1.54 | 2.32 | 0.66 | 0.506 | 0.937 | n.s. |
| 3 to 2 - Cardinality2 | -3.01 | 2.36 | -1.27 | 0.202 | 0.836 | n.s. |
| 4 to 2 - 5 to 2 | 3.64 | 2.34 | 1.55 | 0.121 | 0.685 | n.s. |
| 4 to 2 - Cardinality2 | -0.91 | 2.32 | -0.39 | 0.695 | 0.937 | n.s. |
| 5 to 2 - Cardinality2 | -4.55 | 2.38 | -1.91 | 0.056 | 0.438 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.389, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | 0.14 | 23 | = 0.886 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -0.79 | 23 | = 0.713 | -0.20 [-0.59, 0.26] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | 0.69 | 23 | = 0.713 | 0.21 [-0.28, 0.56] | small | n.s. |
| 1 to 2 vs Cardinality2 | -1.02 | 23 | = 0.713 | -0.29 [-0.63, 0.22] | small | n.s. |
| 3 to 2 vs 4 to 2 | -0.79 | 23 | = 0.713 | -0.25 [-0.59, 0.26] | small | n.s. |
| 3 to 2 vs 5 to 2 | 0.54 | 23 | = 0.741 | 0.18 [-0.31, 0.53] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | -1.14 | 23 | = 0.713 | -0.34 [-0.66, 0.20] | small | n.s. |
| 4 to 2 vs 5 to 2 | 1.95 | 23 | = 0.314 | 0.44 [-0.04, 0.84] | small | n.s. |
| 4 to 2 vs Cardinality2 | -0.38 | 23 | = 0.790 | -0.11 [-0.50, 0.35] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -2.00 | 23 | = 0.314 | -0.53 [-0.85, 0.03] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 545.17, BIC = 567.47
- **3 to 2 vs 1 to 2**: *β* = -0.88, *SE* = 0.565, *z* = -1.562, *p* = 0.118
- **4 to 2 vs 1 to 2**: *β* = -0.43, *SE* = 0.563, *z* = -0.770, *p* = 0.441
- **5 to 2 vs 1 to 2**: *β* = -1.77, *SE* = 0.568, *z* = -3.113, *p* = 0.002
- **Cardinality2 vs 1 to 2**: *β* = -0.71, *SE* = 0.567, *z* = -1.247, *p* = 0.212
- **SNR**: *β* = -0.04, *SE* = 0.149, *z* = -0.257, *p* = 0.797

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | 0.88 | 0.56 | 1.56 | 0.118 | 0.580 | n.s. |
| 1 to 2 - 4 to 2 | 0.43 | 0.56 | 0.77 | 0.441 | 0.893 | n.s. |
| 1 to 2 - 5 to 2 | 1.77 | 0.57 | 3.11 | 0.002 | 0.018 | * |
| 1 to 2 - Cardinality2 | 0.71 | 0.57 | 1.25 | 0.212 | 0.697 | n.s. |
| 3 to 2 - 4 to 2 | -0.45 | 0.57 | -0.79 | 0.428 | 0.893 | n.s. |
| 3 to 2 - 5 to 2 | 0.88 | 0.56 | 1.57 | 0.117 | 0.580 | n.s. |
| 3 to 2 - Cardinality2 | -0.18 | 0.57 | -0.31 | 0.760 | 0.893 | n.s. |
| 4 to 2 - 5 to 2 | 1.33 | 0.57 | 2.34 | 0.019 | 0.161 | n.s. |
| 4 to 2 - Cardinality2 | 0.27 | 0.57 | 0.48 | 0.629 | 0.893 | n.s. |
| 5 to 2 - Cardinality2 | -1.06 | 0.58 | -1.83 | 0.068 | 0.430 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.66, *p* = 0.038, η²_G = 0.060
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | 1.58 | 23 | = 0.257 | 0.38 [-0.11, 0.75] | small | n.s. |
| 1 to 2 vs 4 to 2 | 0.72 | 23 | = 0.596 | 0.17 [-0.28, 0.57] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | 3.36 | 23 | = 0.027 | 0.71 [0.22, 1.15] | medium | * |
| 1 to 2 vs Cardinality2 | 1.21 | 23 | = 0.399 | 0.30 [-0.18, 0.68] | small | n.s. |
| 3 to 2 vs 4 to 2 | -0.80 | 23 | = 0.596 | -0.19 [-0.59, 0.26] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.76 | 23 | = 0.257 | 0.37 [-0.08, 0.80] | small | n.s. |
| 3 to 2 vs Cardinality2 | -0.40 | 23 | = 0.695 | -0.09 [-0.50, 0.34] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.95 | 23 | = 0.257 | 0.54 [-0.04, 0.84] | medium | n.s. |
| 4 to 2 vs Cardinality2 | 0.51 | 23 | = 0.680 | 0.11 [-0.32, 0.53] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -1.66 | 23 | = 0.257 | -0.47 [-0.77, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1043.31, BIC = 1065.61
- **3 to 2 vs 1 to 2**: *β* = 5.72, *SE* = 4.490, *z* = 1.274, *p* = 0.203
- **4 to 2 vs 1 to 2**: *β* = 4.32, *SE* = 4.475, *z* = 0.965, *p* = 0.335
- **5 to 2 vs 1 to 2**: *β* = 3.74, *SE* = 4.503, *z* = 0.830, *p* = 0.407
- **Cardinality2 vs 1 to 2**: *β* = 4.41, *SE* = 4.524, *z* = 0.974, *p* = 0.330
- **SNR**: *β* = -0.09, *SE* = 0.675, *z* = -0.135, *p* = 0.892

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -5.72 | 4.49 | -1.27 | 0.203 | 0.896 | n.s. |
| 1 to 2 - 4 to 2 | -4.32 | 4.47 | -0.96 | 0.335 | 0.973 | n.s. |
| 1 to 2 - 5 to 2 | -3.74 | 4.50 | -0.83 | 0.407 | 0.974 | n.s. |
| 1 to 2 - Cardinality2 | -4.41 | 4.52 | -0.97 | 0.330 | 0.973 | n.s. |
| 3 to 2 - 4 to 2 | 1.40 | 4.50 | 0.31 | 0.755 | 0.999 | n.s. |
| 3 to 2 - 5 to 2 | 1.98 | 4.47 | 0.44 | 0.658 | 0.998 | n.s. |
| 3 to 2 - Cardinality2 | 1.31 | 4.60 | 0.29 | 0.776 | 0.999 | n.s. |
| 4 to 2 - 5 to 2 | 0.58 | 4.52 | 0.13 | 0.898 | 0.999 | n.s. |
| 4 to 2 - Cardinality2 | -0.09 | 4.51 | -0.02 | 0.984 | 0.999 | n.s. |
| 5 to 2 - Cardinality2 | -0.67 | 4.63 | -0.15 | 0.885 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.45, *p* = 0.775, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -1.22 | 23 | = 0.965 | -0.27 [-0.68, 0.18] | small | n.s. |
| 1 to 2 vs 4 to 2 | -1.05 | 23 | = 0.965 | -0.26 [-0.64, 0.21] | small | n.s. |
| 1 to 2 vs 5 to 2 | -0.74 | 23 | = 0.965 | -0.20 [-0.58, 0.27] | small | n.s. |
| 1 to 2 vs Cardinality2 | -0.99 | 23 | = 0.965 | -0.23 [-0.63, 0.22] | small | n.s. |
| 3 to 2 vs 4 to 2 | 0.30 | 23 | = 0.965 | 0.07 [-0.36, 0.48] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 0.41 | 23 | = 0.965 | 0.10 [-0.34, 0.51] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | 0.21 | 23 | = 0.965 | 0.05 [-0.38, 0.46] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.17 | 23 | = 0.965 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | -0.04 | 23 | = 0.965 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -0.19 | 23 | = 0.965 | -0.04 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 501.11, BIC = 523.41
- **3 to 2 vs 1 to 2**: *β* = -0.21, *SE* = 0.437, *z* = -0.475, *p* = 0.635
- **4 to 2 vs 1 to 2**: *β* = -0.90, *SE* = 0.435, *z* = -2.066, *p* = 0.039
- **5 to 2 vs 1 to 2**: *β* = -0.90, *SE* = 0.438, *z* = -2.043, *p* = 0.041
- **Cardinality2 vs 1 to 2**: *β* = -0.46, *SE* = 0.440, *z* = -1.041, *p* = 0.298
- **SNR**: *β* = -0.45, *SE* = 0.072, *z* = -6.247, *p* < .001

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | 0.21 | 0.44 | 0.47 | 0.635 | 0.924 | n.s. |
| 1 to 2 - 4 to 2 | 0.90 | 0.43 | 2.07 | 0.039 | 0.327 | n.s. |
| 1 to 2 - 5 to 2 | 0.89 | 0.44 | 2.04 | 0.041 | 0.327 | n.s. |
| 1 to 2 - Cardinality2 | 0.46 | 0.44 | 1.04 | 0.298 | 0.880 | n.s. |
| 3 to 2 - 4 to 2 | 0.69 | 0.44 | 1.58 | 0.115 | 0.619 | n.s. |
| 3 to 2 - 5 to 2 | 0.69 | 0.43 | 1.58 | 0.114 | 0.619 | n.s. |
| 3 to 2 - Cardinality2 | 0.25 | 0.45 | 0.56 | 0.576 | 0.924 | n.s. |
| 4 to 2 - 5 to 2 | -0.00 | 0.44 | -0.01 | 0.994 | 0.994 | n.s. |
| 4 to 2 - Cardinality2 | -0.44 | 0.44 | -1.00 | 0.316 | 0.880 | n.s. |
| 5 to 2 - Cardinality2 | -0.44 | 0.45 | -0.96 | 0.335 | 0.880 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.26, *p* = 0.069, η²_G = 0.030
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | 1.31 | 23 | = 0.350 | 0.19 [-0.16, 0.70] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | 1.65 | 23 | = 0.339 | 0.30 [-0.10, 0.77] | small | n.s. |
| 1 to 2 vs 5 to 2 | 2.54 | 23 | = 0.184 | 0.45 [0.07, 0.97] | small | n.s. |
| 1 to 2 vs Cardinality2 | 0.02 | 23 | = 0.984 | 0.00 [-0.42, 0.43] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | 0.71 | 23 | = 0.536 | 0.12 [-0.28, 0.57] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.55 | 23 | = 0.339 | 0.28 [-0.12, 0.75] | small | n.s. |
| 3 to 2 vs Cardinality2 | -0.91 | 23 | = 0.464 | -0.17 [-0.61, 0.24] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.92 | 23 | = 0.464 | 0.14 [-0.24, 0.61] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | -1.29 | 23 | = 0.350 | -0.28 [-0.69, 0.17] | small | n.s. |
| 5 to 2 vs Cardinality2 | -2.04 | 23 | = 0.268 | -0.43 [-0.86, 0.02] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 795.84, BIC = 818.14
- **3 to 2 vs 1 to 2**: *β* = 1.65, *SE* = 1.562, *z* = 1.057, *p* = 0.290
- **4 to 2 vs 1 to 2**: *β* = 1.67, *SE* = 1.562, *z* = 1.071, *p* = 0.284
- **5 to 2 vs 1 to 2**: *β* = -0.11, *SE* = 1.566, *z* = -0.070, *p* = 0.944
- **Cardinality2 vs 1 to 2**: *β* = 0.89, *SE* = 1.567, *z* = 0.568, *p* = 0.570
- **SNR**: *β* = -0.16, *SE* = 0.362, *z* = -0.451, *p* = 0.652

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -1.65 | 1.56 | -1.06 | 0.290 | 0.947 | n.s. |
| 1 to 2 - 4 to 2 | -1.67 | 1.56 | -1.07 | 0.284 | 0.947 | n.s. |
| 1 to 2 - 5 to 2 | 0.11 | 1.57 | 0.07 | 0.944 | 0.997 | n.s. |
| 1 to 2 - Cardinality2 | -0.89 | 1.57 | -0.57 | 0.570 | 0.988 | n.s. |
| 3 to 2 - 4 to 2 | -0.02 | 1.56 | -0.01 | 0.989 | 0.997 | n.s. |
| 3 to 2 - 5 to 2 | 1.76 | 1.57 | 1.12 | 0.262 | 0.947 | n.s. |
| 3 to 2 - Cardinality2 | 0.76 | 1.57 | 0.49 | 0.628 | 0.988 | n.s. |
| 4 to 2 - 5 to 2 | 1.78 | 1.57 | 1.14 | 0.255 | 0.947 | n.s. |
| 4 to 2 - Cardinality2 | 0.78 | 1.57 | 0.50 | 0.617 | 0.988 | n.s. |
| 5 to 2 - Cardinality2 | -1.00 | 1.56 | -0.64 | 0.522 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.660, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -1.27 | 23 | = 0.810 | -0.23 [-0.69, 0.17] | small | n.s. |
| 1 to 2 vs 4 to 2 | -0.98 | 23 | = 0.810 | -0.23 [-0.63, 0.23] | small | n.s. |
| 1 to 2 vs 5 to 2 | 0.09 | 23 | = 1.000 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| 1 to 2 vs Cardinality2 | -0.46 | 23 | = 0.810 | -0.11 [-0.52, 0.33] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.09 | 23 | = 0.810 | 0.26 [-0.21, 0.65] | small | n.s. |
| 3 to 2 vs Cardinality2 | 0.51 | 23 | = 0.810 | 0.12 [-0.32, 0.53] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.39 | 23 | = 0.810 | 0.27 [-0.15, 0.71] | small | n.s. |
| 4 to 2 vs Cardinality2 | 0.51 | 23 | = 0.810 | 0.12 [-0.32, 0.53] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | -0.73 | 23 | = 0.810 | -0.14 [-0.57, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 543.32, BIC = 565.62
- **3 to 2 vs 1 to 2**: *β* = 0.30, *SE* = 0.534, *z* = 0.570, *p* = 0.569
- **4 to 2 vs 1 to 2**: *β* = 0.49, *SE* = 0.534, *z* = 0.918, *p* = 0.358
- **5 to 2 vs 1 to 2**: *β* = 1.56, *SE* = 0.536, *z* = 2.913, *p* = 0.004
- **Cardinality2 vs 1 to 2**: *β* = 0.69, *SE* = 0.536, *z* = 1.282, *p* = 0.200
- **SNR**: *β* = -0.18, *SE* = 0.125, *z* = -1.428, *p* = 0.153

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -0.30 | 0.53 | -0.57 | 0.569 | 0.925 | n.s. |
| 1 to 2 - 4 to 2 | -0.49 | 0.53 | -0.92 | 0.358 | 0.891 | n.s. |
| 1 to 2 - 5 to 2 | -1.56 | 0.54 | -2.91 | 0.004 | 0.035 | * |
| 1 to 2 - Cardinality2 | -0.69 | 0.54 | -1.28 | 0.200 | 0.737 | n.s. |
| 3 to 2 - 4 to 2 | -0.19 | 0.53 | -0.35 | 0.728 | 0.925 | n.s. |
| 3 to 2 - 5 to 2 | -1.26 | 0.54 | -2.34 | 0.019 | 0.161 | n.s. |
| 3 to 2 - Cardinality2 | -0.38 | 0.54 | -0.71 | 0.476 | 0.925 | n.s. |
| 4 to 2 - 5 to 2 | -1.07 | 0.54 | -2.00 | 0.046 | 0.312 | n.s. |
| 4 to 2 - Cardinality2 | -0.20 | 0.54 | -0.37 | 0.714 | 0.925 | n.s. |
| 5 to 2 - Cardinality2 | 0.87 | 0.53 | 1.64 | 0.102 | 0.529 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.09, *p* = 0.088, η²_G = 0.038
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -0.68 | 23 | = 0.717 | -0.14 [-0.56, 0.28] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | -0.85 | 23 | = 0.670 | -0.19 [-0.60, 0.25] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | -3.36 | 23 | = 0.027 | -0.64 [-1.15, -0.22] | medium | * |
| 1 to 2 vs Cardinality2 | -1.18 | 23 | = 0.501 | -0.23 [-0.67, 0.19] | small | n.s. |
| 3 to 2 vs 4 to 2 | -0.34 | 23 | = 0.817 | -0.06 [-0.49, 0.35] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | -2.32 | 23 | = 0.149 | -0.50 [-0.92, -0.03] | small | n.s. |
| 3 to 2 vs Cardinality2 | -0.48 | 23 | = 0.792 | -0.11 [-0.52, 0.32] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | -1.64 | 23 | = 0.383 | -0.39 [-0.77, 0.10] | small | n.s. |
| 4 to 2 vs Cardinality2 | -0.23 | 23 | = 0.817 | -0.05 [-0.47, 0.37] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | 1.45 | 23 | = 0.403 | 0.32 [-0.14, 0.73] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1211.23, BIC = 1233.53
- **3 to 2 vs 1 to 2**: *β* = 7.17, *SE* = 9.348, *z* = 0.766, *p* = 0.443
- **4 to 2 vs 1 to 2**: *β* = -6.50, *SE* = 9.339, *z* = -0.696, *p* = 0.486
- **5 to 2 vs 1 to 2**: *β* = -1.74, *SE* = 9.380, *z* = -0.186, *p* = 0.853
- **Cardinality2 vs 1 to 2**: *β* = -12.09, *SE* = 9.437, *z* = -1.281, *p* = 0.200
- **SNR**: *β* = 1.51, *SE* = 1.268, *z* = 1.189, *p* = 0.235

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -7.17 | 9.35 | -0.77 | 0.443 | 0.947 | n.s. |
| 1 to 2 - 4 to 2 | 6.50 | 9.34 | 0.70 | 0.486 | 0.947 | n.s. |
| 1 to 2 - 5 to 2 | 1.74 | 9.38 | 0.19 | 0.853 | 0.947 | n.s. |
| 1 to 2 - Cardinality2 | 12.09 | 9.44 | 1.28 | 0.200 | 0.833 | n.s. |
| 3 to 2 - 4 to 2 | 13.67 | 9.32 | 1.47 | 0.143 | 0.750 | n.s. |
| 3 to 2 - 5 to 2 | 8.91 | 9.48 | 0.94 | 0.348 | 0.923 | n.s. |
| 3 to 2 - Cardinality2 | 19.25 | 9.35 | 2.06 | 0.040 | 0.332 | n.s. |
| 4 to 2 - 5 to 2 | -4.76 | 9.46 | -0.50 | 0.615 | 0.947 | n.s. |
| 4 to 2 - Cardinality2 | 5.58 | 9.37 | 0.60 | 0.551 | 0.947 | n.s. |
| 5 to 2 - Cardinality2 | 10.34 | 9.66 | 1.07 | 0.284 | 0.904 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.279, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -0.58 | 23 | = 0.631 | -0.16 [-0.54, 0.31] | negligible | n.s. |
| 1 to 2 vs 4 to 2 | 0.62 | 23 | = 0.631 | 0.18 [-0.30, 0.55] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | 0.05 | 23 | = 0.962 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 1 to 2 vs Cardinality2 | 1.33 | 23 | = 0.570 | 0.37 [-0.16, 0.70] | small | n.s. |
| 3 to 2 vs 4 to 2 | 1.71 | 23 | = 0.500 | 0.36 [-0.09, 0.78] | small | n.s. |
| 3 to 2 vs 5 to 2 | 0.80 | 23 | = 0.626 | 0.18 [-0.26, 0.59] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | 2.57 | 23 | = 0.172 | 0.60 [0.07, 0.97] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -0.79 | 23 | = 0.626 | -0.17 [-0.59, 0.26] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | 0.82 | 23 | = 0.626 | 0.19 [-0.26, 0.59] | negligible | n.s. |
| 5 to 2 vs Cardinality2 | 1.24 | 23 | = 0.570 | 0.38 [-0.18, 0.68] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 603.83, BIC = 626.13
- **3 to 2 vs 1 to 2**: *β* = 1.20, *SE* = 0.656, *z* = 1.833, *p* = 0.067
- **4 to 2 vs 1 to 2**: *β* = 0.39, *SE* = 0.655, *z* = 0.589, *p* = 0.556
- **5 to 2 vs 1 to 2**: *β* = 0.31, *SE* = 0.659, *z* = 0.476, *p* = 0.634
- **Cardinality2 vs 1 to 2**: *β* = -1.66, *SE* = 0.664, *z* = -2.504, *p* = 0.012
- **SNR**: *β* = 0.25, *SE* = 0.096, *z* = 2.576, *p* = 0.010

_Reference condition: **1 to 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 2 - 3 to 2 | -1.20 | 0.66 | -1.83 | 0.067 | 0.339 | n.s. |
| 1 to 2 - 4 to 2 | -0.39 | 0.66 | -0.59 | 0.556 | 0.912 | n.s. |
| 1 to 2 - 5 to 2 | -0.31 | 0.66 | -0.48 | 0.634 | 0.912 | n.s. |
| 1 to 2 - Cardinality2 | 1.66 | 0.66 | 2.50 | 0.012 | 0.083 | n.s. |
| 3 to 2 - 4 to 2 | 0.82 | 0.65 | 1.25 | 0.212 | 0.635 | n.s. |
| 3 to 2 - 5 to 2 | 0.89 | 0.67 | 1.33 | 0.183 | 0.635 | n.s. |
| 3 to 2 - Cardinality2 | 2.86 | 0.66 | 4.36 | < .001 | < .001 | *** |
| 4 to 2 - 5 to 2 | 0.07 | 0.67 | 0.11 | 0.913 | 0.913 | n.s. |
| 4 to 2 - Cardinality2 | 2.05 | 0.66 | 3.11 | 0.002 | 0.017 | * |
| 5 to 2 - Cardinality2 | 1.97 | 0.68 | 2.90 | 0.004 | 0.030 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.70, *p* < .001, η²_G = 0.070
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 2 vs 3 to 2 | -1.45 | 23 | = 0.266 | -0.26 [-0.73, 0.13] | small | n.s. |
| 1 to 2 vs 4 to 2 | -0.37 | 23 | = 0.713 | -0.07 [-0.50, 0.35] | negligible | n.s. |
| 1 to 2 vs 5 to 2 | -0.83 | 23 | = 0.516 | -0.14 [-0.60, 0.26] | negligible | n.s. |
| 1 to 2 vs Cardinality2 | 2.58 | 23 | = 0.042 | 0.54 [0.08, 0.98] | medium | * |
| 3 to 2 vs 4 to 2 | 1.51 | 23 | = 0.266 | 0.19 [-0.12, 0.74] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.03 | 23 | = 0.447 | 0.14 [-0.22, 0.64] | negligible | n.s. |
| 3 to 2 vs Cardinality2 | 3.69 | 23 | = 0.012 | 0.75 [0.28, 1.23] | medium | * |
| 4 to 2 vs 5 to 2 | -0.47 | 23 | = 0.711 | -0.07 [-0.52, 0.33] | negligible | n.s. |
| 4 to 2 vs Cardinality2 | 3.25 | 23 | = 0.017 | 0.61 [0.20, 1.13] | medium | * |
| 5 to 2 vs Cardinality2 | 3.10 | 23 | = 0.017 | 0.72 [0.17, 1.09] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.038). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than 5 to 2 (*d* = 0.71)
**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.069)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.088)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 2 showed greater amplitude than Cardinality2 (*d* = 0.54)
  - 3 to 2 showed greater amplitude than Cardinality2 (*d* = 0.75)
  - 4 to 2 showed greater amplitude than Cardinality2 (*d* = 0.61)
  - 5 to 2 showed greater amplitude than Cardinality2 (*d* = 0.72)

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
