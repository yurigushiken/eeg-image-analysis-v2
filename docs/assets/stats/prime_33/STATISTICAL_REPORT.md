# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:30:55

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
| 3a | 24 | 106.67 ms | 12.12 | 2.47 | [88.00, 124.00] |
| 3b | 24 | 108.83 ms | 14.40 | 2.94 | [88.00, 124.00] |
| 3c | 24 | 104.17 ms | 13.27 | 2.71 | [88.00, 124.00] |
| 3d | 24 | 104.17 ms | 15.04 | 3.07 | [88.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 24 | -4.74 µV | 4.18 | 0.85 | [-13.07, 2.43] |
| 3b | 24 | -3.51 µV | 4.42 | 0.90 | [-17.04, 5.14] |
| 3c | 24 | -2.34 µV | 2.72 | 0.56 | [-7.26, 3.38] |
| 3d | 24 | -2.09 µV | 2.83 | 0.58 | [-5.97, 6.48] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 24 | 167.00 ms | 22.11 | 4.51 | [140.00, 208.00] |
| 3b | 24 | 181.17 ms | 17.83 | 3.64 | [144.00, 212.00] |
| 3c | 24 | 169.33 ms | 23.55 | 4.81 | [140.00, 212.00] |
| 3d | 24 | 178.17 ms | 21.65 | 4.42 | [140.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 24 | -5.42 µV | 1.85 | 0.38 | [-10.45, -2.70] |
| 3b | 24 | -5.21 µV | 3.44 | 0.70 | [-11.90, 3.65] |
| 3c | 24 | -5.80 µV | 2.73 | 0.56 | [-11.74, -1.10] |
| 3d | 24 | -6.11 µV | 2.70 | 0.55 | [-10.39, -0.32] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 24 | 106.17 ms | 13.86 | 2.83 | [80.00, 124.00] |
| 3b | 24 | 104.00 ms | 17.89 | 3.65 | [80.00, 124.00] |
| 3c | 24 | 102.33 ms | 17.21 | 3.51 | [80.00, 124.00] |
| 3d | 24 | 99.33 ms | 17.76 | 3.62 | [80.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 24 | 4.81 µV | 3.23 | 0.66 | [-0.77, 10.91] |
| 3b | 24 | 4.28 µV | 3.57 | 0.73 | [-1.46, 14.37] |
| 3c | 24 | 3.39 µV | 3.36 | 0.69 | [-3.75, 9.91] |
| 3d | 24 | 2.80 µV | 2.96 | 0.60 | [-3.06, 8.20] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 24 | 456.33 ms | 12.59 | 2.57 | [440.00, 480.00] |
| 3b | 24 | 462.17 ms | 14.83 | 3.03 | [440.00, 480.00] |
| 3c | 24 | 463.67 ms | 13.85 | 2.83 | [440.00, 480.00] |
| 3d | 24 | 455.83 ms | 15.26 | 3.12 | [440.00, 480.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 24 | 2.98 µV | 3.23 | 0.66 | [-3.16, 8.68] |
| 3b | 24 | 3.13 µV | 3.69 | 0.75 | [-7.98, 10.75] |
| 3c | 24 | 2.73 µV | 4.44 | 0.91 | [-9.02, 9.32] |
| 3d | 24 | 2.45 µV | 2.63 | 0.54 | [-1.99, 6.04] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 785.15, BIC = 803.10
- **3b vs 3a**: *β* = 1.62, *SE* = 3.963, *z* = 0.410, *p* = 0.682
- **3c vs 3a**: *β* = -3.23, *SE* = 4.033, *z* = -0.802, *p* = 0.423
- **3d vs 3a**: *β* = -2.80, *SE* = 3.904, *z* = -0.718, *p* = 0.473
- **SNR**: *β* = -0.72, *SE* = 1.085, *z* = -0.660, *p* = 0.509

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -1.63 | 3.96 | -0.41 | 0.682 | 0.899 | n.s. |
| 3a - 3c | 3.23 | 4.03 | 0.80 | 0.423 | 0.889 | n.s. |
| 3a - 3d | 2.80 | 3.90 | 0.72 | 0.473 | 0.889 | n.s. |
| 3b - 3c | 4.86 | 3.89 | 1.25 | 0.211 | 0.759 | n.s. |
| 3b - 3d | 4.43 | 3.89 | 1.14 | 0.255 | 0.771 | n.s. |
| 3c - 3d | -0.43 | 3.93 | -0.11 | 0.913 | 0.913 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.600, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.67 | 23 | = 0.663 | -0.16 [-0.56, 0.29] | negligible | n.s. |
| 3a vs 3c | 0.60 | 23 | = 0.663 | 0.20 [-0.30, 0.55] | negligible | n.s. |
| 3a vs 3d | 0.61 | 23 | = 0.663 | 0.18 [-0.30, 0.55] | negligible | n.s. |
| 3b vs 3c | 1.13 | 23 | = 0.663 | 0.34 [-0.20, 0.66] | small | n.s. |
| 3b vs 3d | 1.02 | 23 | = 0.663 | 0.32 [-0.22, 0.64] | small | n.s. |
| 3c vs 3d | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 519.35, BIC = 537.30
- **3b vs 3a**: *β* = 0.95, *SE* = 0.892, *z* = 1.070, *p* = 0.284
- **3c vs 3a**: *β* = 2.02, *SE* = 0.910, *z* = 2.222, *p* = 0.026
- **3d vs 3a**: *β* = 2.50, *SE* = 0.878, *z* = 2.847, *p* = 0.004
- **SNR**: *β* = -0.36, *SE* = 0.259, *z* = -1.404, *p* = 0.160

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.96 | 0.89 | -1.07 | 0.284 | 0.529 | n.s. |
| 3a - 3c | -2.02 | 0.91 | -2.22 | 0.026 | 0.125 | n.s. |
| 3a - 3d | -2.50 | 0.88 | -2.85 | 0.004 | 0.026 | * |
| 3b - 3c | -1.07 | 0.87 | -1.22 | 0.222 | 0.529 | n.s. |
| 3b - 3d | -1.54 | 0.87 | -1.76 | 0.078 | 0.276 | n.s. |
| 3c - 3d | -0.48 | 0.88 | -0.54 | 0.590 | 0.590 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.67, *p* = 0.016, η²_G = 0.081
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -1.20 | 23 | = 0.289 | -0.29 [-0.67, 0.18] | small | n.s. |
| 3a vs 3c | -3.03 | 23 | = 0.018 | -0.68 [-1.08, -0.16] | medium | * |
| 3a vs 3d | -3.07 | 23 | = 0.018 | -0.74 [-1.09, -0.17] | medium | * |
| 3b vs 3c | -1.26 | 23 | = 0.289 | -0.32 [-0.69, 0.17] | small | n.s. |
| 3b vs 3d | -1.42 | 23 | = 0.289 | -0.38 [-0.72, 0.14] | small | n.s. |
| 3c vs 3d | -0.35 | 23 | = 0.733 | -0.09 [-0.49, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 862.88, BIC = 880.83
- **3b vs 3a**: *β* = 14.11, *SE* = 5.221, *z* = 2.702, *p* = 0.007
- **3c vs 3a**: *β* = 2.35, *SE* = 5.209, *z* = 0.451, *p* = 0.652
- **3d vs 3a**: *β* = 10.99, *SE* = 5.308, *z* = 2.072, *p* = 0.038
- **SNR**: *β* = 0.20, *SE* = 1.212, *z* = 0.168, *p* = 0.867

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -14.11 | 5.22 | -2.70 | 0.007 | 0.041 | * |
| 3a - 3c | -2.35 | 5.21 | -0.45 | 0.652 | 0.801 | n.s. |
| 3a - 3d | -11.00 | 5.31 | -2.07 | 0.038 | 0.145 | n.s. |
| 3b - 3c | 11.76 | 5.23 | 2.25 | 0.025 | 0.117 | n.s. |
| 3b - 3d | 3.11 | 5.25 | 0.59 | 0.554 | 0.801 | n.s. |
| 3c - 3d | -8.65 | 5.32 | -1.62 | 0.104 | 0.282 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.27, *p* = 0.026, η²_G = 0.074
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -3.24 | 23 | = 0.021 | -0.71 [-1.13, -0.20] | medium | * |
| 3a vs 3c | -0.38 | 23 | = 0.710 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| 3a vs 3d | -2.20 | 23 | = 0.076 | -0.51 [-0.89, -0.01] | medium | n.s. |
| 3b vs 3c | 2.26 | 23 | = 0.076 | 0.57 [0.02, 0.90] | medium | n.s. |
| 3b vs 3d | 0.61 | 23 | = 0.658 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| 3c vs 3d | -1.48 | 23 | = 0.227 | -0.39 [-0.73, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 460.56, BIC = 478.51
- **3b vs 3a**: *β* = 0.36, *SE* = 0.673, *z* = 0.530, *p* = 0.596
- **3c vs 3a**: *β* = -0.42, *SE* = 0.671, *z* = -0.627, *p* = 0.530
- **3d vs 3a**: *β* = -0.26, *SE* = 0.682, *z* = -0.383, *p* = 0.702
- **SNR**: *β* = -0.51, *SE* = 0.142, *z* = -3.574, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.36 | 0.67 | -0.53 | 0.596 | 0.951 | n.s. |
| 3a - 3c | 0.42 | 0.67 | 0.63 | 0.530 | 0.951 | n.s. |
| 3a - 3d | 0.26 | 0.68 | 0.38 | 0.702 | 0.951 | n.s. |
| 3b - 3c | 0.78 | 0.67 | 1.15 | 0.248 | 0.819 | n.s. |
| 3b - 3d | 0.62 | 0.68 | 0.91 | 0.361 | 0.893 | n.s. |
| 3c - 3d | -0.16 | 0.68 | -0.23 | 0.815 | 0.951 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.612, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.27 | 23 | = 0.793 | -0.07 [-0.48, 0.37] | negligible | n.s. |
| 3a vs 3c | 0.70 | 23 | = 0.732 | 0.17 [-0.28, 0.57] | negligible | n.s. |
| 3a vs 3d | 1.10 | 23 | = 0.732 | 0.30 [-0.20, 0.65] | small | n.s. |
| 3b vs 3c | 0.87 | 23 | = 0.732 | 0.19 [-0.25, 0.60] | negligible | n.s. |
| 3b vs 3d | 0.98 | 23 | = 0.732 | 0.29 [-0.23, 0.63] | small | n.s. |
| 3c vs 3d | 0.41 | 23 | = 0.793 | 0.11 [-0.34, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 810.42, BIC = 828.37
- **3b vs 3a**: *β* = -3.49, *SE* = 3.921, *z* = -0.889, *p* = 0.374
- **3c vs 3a**: *β* = -5.05, *SE* = 3.916, *z* = -1.291, *p* = 0.197
- **3d vs 3a**: *β* = -8.63, *SE* = 3.953, *z* = -2.183, *p* = 0.029
- **SNR**: *β* = -2.87, *SE* = 1.180, *z* = -2.432, *p* = 0.015

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 3.49 | 3.92 | 0.89 | 0.374 | 0.736 | n.s. |
| 3a - 3c | 5.06 | 3.92 | 1.29 | 0.197 | 0.643 | n.s. |
| 3a - 3d | 8.63 | 3.95 | 2.18 | 0.029 | 0.162 | n.s. |
| 3b - 3c | 1.57 | 3.88 | 0.40 | 0.686 | 0.736 | n.s. |
| 3b - 3d | 5.14 | 3.89 | 1.32 | 0.186 | 0.643 | n.s. |
| 3c - 3d | 3.57 | 3.89 | 0.92 | 0.359 | 0.736 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.420, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.59 | 23 | = 0.671 | 0.14 [-0.30, 0.54] | negligible | n.s. |
| 3a vs 3c | 0.91 | 23 | = 0.671 | 0.25 [-0.24, 0.61] | small | n.s. |
| 3a vs 3d | 1.57 | 23 | = 0.671 | 0.43 [-0.11, 0.75] | small | n.s. |
| 3b vs 3c | 0.40 | 23 | = 0.695 | 0.09 [-0.34, 0.50] | negligible | n.s. |
| 3b vs 3d | 1.21 | 23 | = 0.671 | 0.26 [-0.18, 0.68] | small | n.s. |
| 3c vs 3d | 0.64 | 23 | = 0.671 | 0.17 [-0.29, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 490.66, BIC = 508.61
- **3b vs 3a**: *β* = -0.36, *SE* = 0.710, *z* = -0.504, *p* = 0.614
- **3c vs 3a**: *β* = -1.26, *SE* = 0.709, *z* = -1.781, *p* = 0.075
- **3d vs 3a**: *β* = -1.78, *SE* = 0.716, *z* = -2.487, *p* = 0.013
- **SNR**: *β* = 0.37, *SE* = 0.215, *z* = 1.704, *p* = 0.088

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.36 | 0.71 | 0.50 | 0.614 | 0.711 | n.s. |
| 3a - 3c | 1.26 | 0.71 | 1.78 | 0.075 | 0.268 | n.s. |
| 3a - 3d | 1.78 | 0.72 | 2.49 | 0.013 | 0.075 | n.s. |
| 3b - 3c | 0.91 | 0.70 | 1.29 | 0.198 | 0.484 | n.s. |
| 3b - 3d | 1.42 | 0.70 | 2.02 | 0.043 | 0.199 | n.s. |
| 3c - 3d | 0.52 | 0.70 | 0.73 | 0.463 | 0.711 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.96, *p* = 0.038, η²_G = 0.055
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.70 | 23 | = 0.493 | 0.15 [-0.28, 0.57] | negligible | n.s. |
| 3a vs 3c | 1.88 | 23 | = 0.147 | 0.43 [-0.05, 0.82] | small | n.s. |
| 3a vs 3d | 2.70 | 23 | = 0.077 | 0.65 [0.10, 1.00] | medium | n.s. |
| 3b vs 3c | 1.37 | 23 | = 0.278 | 0.26 [-0.15, 0.71] | small | n.s. |
| 3b vs 3d | 2.02 | 23 | = 0.147 | 0.45 [-0.03, 0.85] | small | n.s. |
| 3c vs 3d | 0.76 | 23 | = 0.493 | 0.19 [-0.27, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 791.20, BIC = 809.15
- **3b vs 3a**: *β* = 5.71, *SE* = 3.973, *z* = 1.439, *p* = 0.150
- **3c vs 3a**: *β* = 7.37, *SE* = 3.957, *z* = 1.862, *p* = 0.063
- **3d vs 3a**: *β* = -0.56, *SE* = 3.959, *z* = -0.140, *p* = 0.889
- **SNR**: *β* = -0.23, *SE* = 0.716, *z* = -0.325, *p* = 0.745

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -5.71 | 3.97 | -1.44 | 0.150 | 0.386 | n.s. |
| 3a - 3c | -7.37 | 3.96 | -1.86 | 0.063 | 0.276 | n.s. |
| 3a - 3d | 0.55 | 3.96 | 0.14 | 0.889 | 0.896 | n.s. |
| 3b - 3c | -1.65 | 3.98 | -0.41 | 0.678 | 0.896 | n.s. |
| 3b - 3d | 6.27 | 3.96 | 1.58 | 0.113 | 0.382 | n.s. |
| 3c - 3d | 7.92 | 3.97 | 2.00 | 0.046 | 0.245 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.95, *p* = 0.129, η²_G = 0.059
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -1.57 | 23 | = 0.232 | -0.42 [-0.75, 0.11] | small | n.s. |
| 3a vs 3c | -1.97 | 23 | = 0.232 | -0.55 [-0.84, 0.04] | medium | n.s. |
| 3a vs 3d | 0.14 | 23 | = 0.891 | 0.04 [-0.39, 0.45] | negligible | n.s. |
| 3b vs 3c | -0.36 | 23 | = 0.870 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| 3b vs 3d | 1.47 | 23 | = 0.232 | 0.42 [-0.13, 0.73] | small | n.s. |
| 3c vs 3d | 1.70 | 23 | = 0.232 | 0.54 [-0.09, 0.78] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 512.81, BIC = 530.76
- **3b vs 3a**: *β* = 0.13, *SE* = 0.821, *z* = 0.157, *p* = 0.875
- **3c vs 3a**: *β* = -0.24, *SE* = 0.817, *z* = -0.295, *p* = 0.768
- **3d vs 3a**: *β* = -0.54, *SE* = 0.818, *z* = -0.656, *p* = 0.512
- **SNR**: *β* = -0.05, *SE* = 0.168, *z* = -0.308, *p* = 0.758

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.13 | 0.82 | -0.16 | 0.875 | 0.986 | n.s. |
| 3a - 3c | 0.24 | 0.82 | 0.29 | 0.768 | 0.986 | n.s. |
| 3a - 3d | 0.54 | 0.82 | 0.66 | 0.512 | 0.972 | n.s. |
| 3b - 3c | 0.37 | 0.82 | 0.45 | 0.654 | 0.986 | n.s. |
| 3b - 3d | 0.67 | 0.82 | 0.81 | 0.416 | 0.960 | n.s. |
| 3c - 3d | 0.30 | 0.82 | 0.36 | 0.718 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.26, *p* = 0.857, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.26 | 23 | = 0.799 | -0.04 [-0.48, 0.37] | negligible | n.s. |
| 3a vs 3c | 0.28 | 23 | = 0.799 | 0.06 [-0.37, 0.48] | negligible | n.s. |
| 3a vs 3d | 0.62 | 23 | = 0.799 | 0.18 [-0.30, 0.55] | negligible | n.s. |
| 3b vs 3c | 0.53 | 23 | = 0.799 | 0.10 [-0.32, 0.53] | negligible | n.s. |
| 3b vs 3d | 0.73 | 23 | = 0.799 | 0.21 [-0.28, 0.57] | small | n.s. |
| 3c vs 3d | 0.30 | 23 | = 0.799 | 0.08 [-0.36, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.016). Post-hoc tests revealed:
  - 3a showed smaller amplitude than 3c (*d* = -0.68)
  - 3a showed smaller amplitude than 3d (*d* = -0.74)
**N1 latency:** Significant main effect of condition (*p* = 0.026). Post-hoc tests revealed:
  - 3a showed smaller latency than 3b (*d* = -0.71)
**P1 amplitude:** Significant main effect of condition (*p* = 0.038) (no significant pairwise comparisons)

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
