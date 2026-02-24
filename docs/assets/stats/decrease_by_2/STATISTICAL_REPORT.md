# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:17:15

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
| 3 to 1 | 24 | 109.67 ms | 9.50 | 1.94 | [96.00, 120.00] |
| 4 to 2 | 24 | 108.17 ms | 8.38 | 1.71 | [96.00, 120.00] |
| 5 to 3 | 24 | 106.00 ms | 9.21 | 1.88 | [96.00, 120.00] |
| 6 to 4 | 24 | 108.83 ms | 9.06 | 1.85 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -1.79 µV | 2.10 | 0.43 | [-6.18, 1.52] |
| 4 to 2 | 24 | -0.71 µV | 2.54 | 0.52 | [-4.94, 4.79] |
| 5 to 3 | 24 | -2.48 µV | 2.07 | 0.42 | [-5.05, 1.68] |
| 6 to 4 | 24 | -2.19 µV | 1.88 | 0.38 | [-7.38, 0.61] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 181.50 ms | 14.72 | 3.01 | [156.00, 208.00] |
| 4 to 2 | 24 | 174.67 ms | 14.81 | 3.02 | [148.00, 208.00] |
| 5 to 3 | 24 | 175.00 ms | 15.57 | 3.18 | [148.00, 208.00] |
| 6 to 4 | 24 | 174.50 ms | 21.03 | 4.29 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | -3.92 µV | 2.56 | 0.52 | [-10.41, -0.72] |
| 4 to 2 | 24 | -6.13 µV | 3.05 | 0.62 | [-11.92, -1.89] |
| 5 to 3 | 24 | -5.84 µV | 2.77 | 0.57 | [-12.11, -1.76] |
| 6 to 4 | 24 | -5.44 µV | 2.66 | 0.54 | [-12.20, -1.44] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 117.33 ms | 10.05 | 2.05 | [100.00, 128.00] |
| 4 to 2 | 24 | 115.33 ms | 10.26 | 2.09 | [100.00, 128.00] |
| 5 to 3 | 24 | 114.67 ms | 10.85 | 2.22 | [100.00, 128.00] |
| 6 to 4 | 24 | 112.83 ms | 10.21 | 2.08 | [100.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 3.41 µV | 2.20 | 0.45 | [-2.54, 9.14] |
| 4 to 2 | 24 | 0.96 µV | 2.64 | 0.54 | [-4.63, 4.87] |
| 5 to 3 | 24 | 1.99 µV | 2.30 | 0.47 | [-3.43, 4.76] |
| 6 to 4 | 24 | 2.24 µV | 2.72 | 0.55 | [-2.71, 7.60] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 473.83 ms | 30.69 | 6.26 | [420.00, 536.00] |
| 4 to 2 | 24 | 472.17 ms | 38.27 | 7.81 | [420.00, 536.00] |
| 5 to 3 | 24 | 467.67 ms | 29.18 | 5.96 | [420.00, 536.00] |
| 6 to 4 | 24 | 481.50 ms | 34.59 | 7.06 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 24 | 4.89 µV | 3.42 | 0.70 | [-0.59, 14.34] |
| 4 to 2 | 24 | 4.26 µV | 3.81 | 0.78 | [-3.59, 11.62] |
| 5 to 3 | 24 | 4.57 µV | 3.26 | 0.67 | [-3.30, 10.28] |
| 6 to 4 | 24 | 4.10 µV | 3.62 | 0.74 | [-4.76, 9.62] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 702.69, BIC = 720.64
- **4 to 2 vs 3 to 1**: *β* = -1.51, *SE* = 2.377, *z* = -0.636, *p* = 0.525
- **5 to 3 vs 3 to 1**: *β* = -3.94, *SE* = 2.432, *z* = -1.619, *p* = 0.105
- **6 to 4 vs 3 to 1**: *β* = -0.88, *SE* = 2.379, *z* = -0.371, *p* = 0.711
- **SNR**: *β* = 0.36, *SE* = 0.682, *z* = 0.526, *p* = 0.599

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 1.51 | 2.38 | 0.64 | 0.525 | 0.893 | n.s. |
| 3 to 1 - 5 to 3 | 3.94 | 2.43 | 1.62 | 0.105 | 0.488 | n.s. |
| 3 to 1 - 6 to 4 | 0.88 | 2.38 | 0.37 | 0.711 | 0.916 | n.s. |
| 4 to 2 - 5 to 3 | 2.43 | 2.43 | 1.00 | 0.318 | 0.783 | n.s. |
| 4 to 2 - 6 to 4 | -0.63 | 2.38 | -0.26 | 0.792 | 0.916 | n.s. |
| 5 to 3 - 6 to 4 | -3.05 | 2.41 | -1.27 | 0.206 | 0.684 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.83, *p* = 0.479, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.65 | 23 | = 0.783 | 0.17 [-0.29, 0.56] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 1.33 | 23 | = 0.616 | 0.39 [-0.16, 0.70] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.35 | 23 | = 0.786 | 0.09 [-0.35, 0.49] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | 0.87 | 23 | = 0.782 | 0.25 [-0.25, 0.60] | small | n.s. |
| 4 to 2 vs 6 to 4 | -0.27 | 23 | = 0.786 | -0.08 [-0.48, 0.37] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | -1.30 | 23 | = 0.616 | -0.31 [-0.70, 0.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 421.31, BIC = 439.27
- **4 to 2 vs 3 to 1**: *β* = 1.09, *SE* = 0.526, *z* = 2.072, *p* = 0.038
- **5 to 3 vs 3 to 1**: *β* = -0.53, *SE* = 0.539, *z* = -0.986, *p* = 0.324
- **6 to 4 vs 3 to 1**: *β* = -0.38, *SE* = 0.526, *z* = -0.713, *p* = 0.476
- **SNR**: *β* = -0.21, *SE* = 0.155, *z* = -1.385, *p* = 0.166

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -1.09 | 0.53 | -2.07 | 0.038 | 0.145 | n.s. |
| 3 to 1 - 5 to 3 | 0.53 | 0.54 | 0.99 | 0.324 | 0.691 | n.s. |
| 3 to 1 - 6 to 4 | 0.38 | 0.53 | 0.71 | 0.476 | 0.725 | n.s. |
| 4 to 2 - 5 to 3 | 1.62 | 0.54 | 3.01 | 0.003 | 0.015 | * |
| 4 to 2 - 6 to 4 | 1.46 | 0.53 | 2.78 | 0.005 | 0.027 | * |
| 5 to 3 - 6 to 4 | -0.16 | 0.53 | -0.29 | 0.770 | 0.770 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.12, *p* = 0.010, η²_G = 0.092
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -1.78 | 23 | = 0.175 | -0.46 [-0.80, 0.07] | small | n.s. |
| 3 to 1 vs 5 to 3 | 1.40 | 23 | = 0.262 | 0.33 [-0.14, 0.72] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.91 | 23 | = 0.448 | 0.20 [-0.24, 0.61] | small | n.s. |
| 4 to 2 vs 5 to 3 | 2.72 | 23 | = 0.045 | 0.77 [0.10, 1.01] | medium | * |
| 4 to 2 vs 6 to 4 | 2.63 | 23 | = 0.045 | 0.67 [0.09, 0.99] | medium | * |
| 5 to 3 vs 6 to 4 | -0.64 | 23 | = 0.531 | -0.15 [-0.55, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 799.66, BIC = 817.61
- **4 to 2 vs 3 to 1**: *β* = -7.42, *SE* = 3.528, *z* = -2.104, *p* = 0.035
- **5 to 3 vs 3 to 1**: *β* = -7.34, *SE* = 3.580, *z* = -2.050, *p* = 0.040
- **6 to 4 vs 3 to 1**: *β* = -7.83, *SE* = 3.578, *z* = -2.188, *p* = 0.029
- **SNR**: *β* = 0.43, *SE* = 0.439, *z* = 0.978, *p* = 0.328

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 7.42 | 3.53 | 2.10 | 0.035 | 0.165 | n.s. |
| 3 to 1 - 5 to 3 | 7.34 | 3.58 | 2.05 | 0.040 | 0.165 | n.s. |
| 3 to 1 - 6 to 4 | 7.83 | 3.58 | 2.19 | 0.029 | 0.160 | n.s. |
| 4 to 2 - 5 to 3 | -0.08 | 3.49 | -0.02 | 0.981 | 0.999 | n.s. |
| 4 to 2 - 6 to 4 | 0.41 | 3.48 | 0.12 | 0.907 | 0.999 | n.s. |
| 5 to 3 - 6 to 4 | 0.49 | 3.48 | 0.14 | 0.888 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.80, *p* = 0.155, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 2.21 | 23 | = 0.113 | 0.46 [0.01, 0.89] | small | n.s. |
| 3 to 1 vs 5 to 3 | 2.33 | 23 | = 0.113 | 0.43 [0.03, 0.92] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.73 | 23 | = 0.193 | 0.39 [-0.08, 0.79] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.09 | 23 | = 0.967 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.04 | 23 | = 0.967 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.13 | 23 | = 0.967 | 0.03 [-0.40, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 422.44, BIC = 440.39
- **4 to 2 vs 3 to 1**: *β* = -1.66, *SE* = 0.504, *z* = -3.295, *p* = 0.001
- **5 to 3 vs 3 to 1**: *β* = -1.13, *SE* = 0.511, *z* = -2.212, *p* = 0.027
- **6 to 4 vs 3 to 1**: *β* = -0.74, *SE* = 0.511, *z* = -1.456, *p* = 0.145
- **SNR**: *β* = -0.40, *SE* = 0.063, *z* = -6.436, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 1.66 | 0.50 | 3.30 | < .001 | 0.006 | ** |
| 3 to 1 - 5 to 3 | 1.13 | 0.51 | 2.21 | 0.027 | 0.128 | n.s. |
| 3 to 1 - 6 to 4 | 0.74 | 0.51 | 1.46 | 0.145 | 0.376 | n.s. |
| 4 to 2 - 5 to 3 | -0.53 | 0.50 | -1.06 | 0.288 | 0.493 | n.s. |
| 4 to 2 - 6 to 4 | -0.92 | 0.50 | -1.84 | 0.066 | 0.238 | n.s. |
| 5 to 3 - 6 to 4 | -0.39 | 0.50 | -0.78 | 0.435 | 0.493 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.30, *p* = 0.002, η²_G = 0.090
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 4.25 | 23 | = 0.002 | 0.79 [0.37, 1.36] | medium | ** |
| 3 to 1 vs 5 to 3 | 3.00 | 23 | = 0.019 | 0.72 [0.15, 1.07] | medium | * |
| 3 to 1 vs 6 to 4 | 2.19 | 23 | = 0.078 | 0.58 [0.00, 0.89] | medium | n.s. |
| 4 to 2 vs 5 to 3 | -0.48 | 23 | = 0.632 | -0.10 [-0.52, 0.32] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.24 | 23 | = 0.344 | -0.24 [-0.68, 0.18] | small | n.s. |
| 5 to 3 vs 6 to 4 | -0.67 | 23 | = 0.614 | -0.15 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 717.94, BIC = 735.89
- **4 to 2 vs 3 to 1**: *β* = -2.41, *SE* = 2.405, *z* = -1.004, *p* = 0.315
- **5 to 3 vs 3 to 1**: *β* = -2.82, *SE* = 2.388, *z* = -1.182, *p* = 0.237
- **6 to 4 vs 3 to 1**: *β* = -4.61, *SE* = 2.386, *z* = -1.933, *p* = 0.053
- **SNR**: *β* = -0.59, *SE* = 0.437, *z* = -1.352, *p* = 0.176

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 2.41 | 2.40 | 1.00 | 0.315 | 0.780 | n.s. |
| 3 to 1 - 5 to 3 | 2.82 | 2.39 | 1.18 | 0.237 | 0.742 | n.s. |
| 3 to 1 - 6 to 4 | 4.61 | 2.39 | 1.93 | 0.053 | 0.280 | n.s. |
| 4 to 2 - 5 to 3 | 0.41 | 2.39 | 0.17 | 0.865 | 0.865 | n.s. |
| 4 to 2 - 6 to 4 | 2.20 | 2.40 | 0.92 | 0.359 | 0.780 | n.s. |
| 5 to 3 - 6 to 4 | 1.79 | 2.39 | 0.75 | 0.453 | 0.780 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.13, *p* = 0.343, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.84 | 23 | = 0.582 | 0.20 [-0.25, 0.60] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 1.08 | 23 | = 0.582 | 0.25 [-0.21, 0.65] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.69 | 23 | = 0.582 | 0.44 [-0.09, 0.78] | small | n.s. |
| 4 to 2 vs 5 to 3 | 0.31 | 23 | = 0.761 | 0.06 [-0.36, 0.49] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.98 | 23 | = 0.582 | 0.24 [-0.23, 0.63] | small | n.s. |
| 5 to 3 vs 6 to 4 | 0.71 | 23 | = 0.582 | 0.17 [-0.28, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 436.98, BIC = 454.93
- **4 to 2 vs 3 to 1**: *β* = -2.29, *SE* = 0.557, *z* = -4.106, *p* < .001
- **5 to 3 vs 3 to 1**: *β* = -1.35, *SE* = 0.553, *z* = -2.451, *p* = 0.014
- **6 to 4 vs 3 to 1**: *β* = -1.12, *SE* = 0.553, *z* = -2.030, *p* = 0.042
- **SNR**: *β* = 0.23, *SE* = 0.103, *z* = 2.195, *p* = 0.028

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 2.29 | 0.56 | 4.11 | < .001 | < .001 | *** |
| 3 to 1 - 5 to 3 | 1.36 | 0.55 | 2.45 | 0.014 | 0.069 | n.s. |
| 3 to 1 - 6 to 4 | 1.12 | 0.55 | 2.03 | 0.042 | 0.135 | n.s. |
| 4 to 2 - 5 to 3 | -0.93 | 0.55 | -1.68 | 0.093 | 0.177 | n.s. |
| 4 to 2 - 6 to 4 | -1.17 | 0.55 | -2.10 | 0.036 | 0.135 | n.s. |
| 5 to 3 - 6 to 4 | -0.23 | 0.55 | -0.42 | 0.673 | 0.673 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.18, *p* < .001, η²_G = 0.114
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 3.49 | 23 | = 0.012 | 1.00 [0.24, 1.18] | large | * |
| 3 to 1 vs 5 to 3 | 3.00 | 23 | = 0.019 | 0.63 [0.15, 1.07] | medium | * |
| 3 to 1 vs 6 to 4 | 2.35 | 23 | = 0.041 | 0.47 [0.03, 0.93] | small | * |
| 4 to 2 vs 5 to 3 | -1.48 | 23 | = 0.183 | -0.42 [-0.73, 0.13] | small | n.s. |
| 4 to 2 vs 6 to 4 | -2.39 | 23 | = 0.041 | -0.48 [-0.93, -0.04] | small | * |
| 5 to 3 vs 6 to 4 | -0.52 | 23 | = 0.606 | -0.10 [-0.53, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 951.89, BIC = 969.84
- **4 to 2 vs 3 to 1**: *β* = -0.62, *SE* = 8.833, *z* = -0.071, *p* = 0.944
- **5 to 3 vs 3 to 1**: *β* = -5.60, *SE* = 8.654, *z* = -0.647, *p* = 0.518
- **6 to 4 vs 3 to 1**: *β* = 8.52, *SE* = 8.749, *z* = 0.974, *p* = 0.330
- **SNR**: *β* = 0.37, *SE* = 0.754, *z* = 0.496, *p* = 0.620

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 0.62 | 8.83 | 0.07 | 0.944 | 0.944 | n.s. |
| 3 to 1 - 5 to 3 | 5.60 | 8.65 | 0.65 | 0.518 | 0.888 | n.s. |
| 3 to 1 - 6 to 4 | -8.52 | 8.75 | -0.97 | 0.330 | 0.816 | n.s. |
| 4 to 2 - 5 to 3 | 4.98 | 8.63 | 0.58 | 0.564 | 0.888 | n.s. |
| 4 to 2 - 6 to 4 | -9.14 | 8.59 | -1.06 | 0.287 | 0.816 | n.s. |
| 5 to 3 - 6 to 4 | -14.12 | 8.60 | -1.64 | 0.101 | 0.470 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.87, *p* = 0.463, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.18 | 23 | = 0.859 | 0.05 [-0.39, 0.46] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.75 | 23 | = 0.690 | 0.21 [-0.27, 0.58] | small | n.s. |
| 3 to 1 vs 6 to 4 | -0.80 | 23 | = 0.690 | -0.23 [-0.59, 0.26] | small | n.s. |
| 4 to 2 vs 5 to 3 | 0.57 | 23 | = 0.692 | 0.13 [-0.31, 0.54] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -0.98 | 23 | = 0.690 | -0.26 [-0.63, 0.23] | small | n.s. |
| 5 to 3 vs 6 to 4 | -1.76 | 23 | = 0.552 | -0.43 [-0.79, 0.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 480.24, BIC = 498.19
- **4 to 2 vs 3 to 1**: *β* = -0.39, *SE* = 0.646, *z* = -0.603, *p* = 0.546
- **5 to 3 vs 3 to 1**: *β* = -0.19, *SE* = 0.631, *z* = -0.301, *p* = 0.763
- **6 to 4 vs 3 to 1**: *β* = -0.60, *SE* = 0.639, *z* = -0.932, *p* = 0.351
- **SNR**: *β* = 0.09, *SE* = 0.060, *z* = 1.455, *p* = 0.146

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 0.39 | 0.65 | 0.60 | 0.546 | 0.974 | n.s. |
| 3 to 1 - 5 to 3 | 0.19 | 0.63 | 0.30 | 0.763 | 0.983 | n.s. |
| 3 to 1 - 6 to 4 | 0.60 | 0.64 | 0.93 | 0.351 | 0.925 | n.s. |
| 4 to 2 - 5 to 3 | -0.20 | 0.63 | -0.32 | 0.750 | 0.983 | n.s. |
| 4 to 2 - 6 to 4 | 0.21 | 0.62 | 0.33 | 0.742 | 0.983 | n.s. |
| 5 to 3 - 6 to 4 | 0.41 | 0.63 | 0.65 | 0.517 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.613, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.22 | 23 | = 0.752 | 0.18 [-0.18, 0.68] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.49 | 23 | = 0.752 | 0.10 [-0.32, 0.52] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 1.15 | 23 | = 0.752 | 0.23 [-0.19, 0.66] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.62 | 23 | = 0.752 | -0.09 [-0.55, 0.30] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.22 | 23 | = 0.829 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.68 | 23 | = 0.752 | 0.14 [-0.28, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - 4 to 2 showed greater amplitude than 5 to 3 (*d* = 0.77)
  - 4 to 2 showed greater amplitude than 6 to 4 (*d* = 0.67)
**N1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 0.79)
  - 3 to 1 showed greater amplitude than 5 to 3 (*d* = 0.72)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 1.00)
  - 3 to 1 showed greater amplitude than 5 to 3 (*d* = 0.63)
  - 3 to 1 showed greater amplitude than 6 to 4 (*d* = 0.47)
  - 4 to 2 showed smaller amplitude than 6 to 4 (*d* = -0.48)

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
