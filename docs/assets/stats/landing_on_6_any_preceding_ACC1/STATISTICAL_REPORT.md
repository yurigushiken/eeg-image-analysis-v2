# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:48:36

---

## 1. Analysis Overview

**Total Measurements:** 352
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
| 3 to 6 | 15 | 96.53 ms | 10.46 | 2.70 | [84.00, 112.00] |
| 4 to 6 | 14 | 104.57 ms | 9.39 | 2.51 | [84.00, 112.00] |
| 5 to 6 | 13 | 101.23 ms | 9.71 | 2.69 | [84.00, 112.00] |
| 6 to 6 | 15 | 98.93 ms | 10.08 | 2.60 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 15 | -3.52 µV | 1.23 | 0.32 | [-5.36, -1.51] |
| 4 to 6 | 14 | -3.26 µV | 1.31 | 0.35 | [-5.80, -1.58] |
| 5 to 6 | 13 | -5.58 µV | 4.27 | 1.18 | [-17.83, -0.47] |
| 6 to 6 | 15 | -3.60 µV | 1.82 | 0.47 | [-7.15, -1.12] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | 167.83 ms | 19.46 | 4.06 | [136.00, 208.00] |
| 4 to 6 | 22 | 168.00 ms | 21.13 | 4.50 | [136.00, 200.00] |
| 5 to 6 | 12 | 169.67 ms | 24.57 | 7.09 | [136.00, 200.00] |
| 6 to 6 | 22 | 173.09 ms | 15.38 | 3.28 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | -7.11 µV | 2.77 | 0.58 | [-12.76, -3.05] |
| 4 to 6 | 22 | -6.92 µV | 3.59 | 0.77 | [-16.09, -3.11] |
| 5 to 6 | 12 | -7.26 µV | 2.89 | 0.83 | [-12.77, -1.43] |
| 6 to 6 | 22 | -5.96 µV | 2.74 | 0.58 | [-11.14, -1.04] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 10 | 94.00 ms | 11.35 | 3.59 | [80.00, 108.00] |
| 4 to 6 | 13 | 97.54 ms | 9.32 | 2.58 | [80.00, 108.00] |
| 5 to 6 | 13 | 98.77 ms | 9.15 | 2.54 | [80.00, 108.00] |
| 6 to 6 | 13 | 95.08 ms | 10.97 | 3.04 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 10 | 4.11 µV | 2.07 | 0.65 | [0.78, 8.13] |
| 4 to 6 | 13 | 4.11 µV | 1.65 | 0.46 | [1.88, 7.49] |
| 5 to 6 | 13 | 5.30 µV | 3.28 | 0.91 | [1.02, 11.93] |
| 6 to 6 | 13 | 2.62 µV | 1.79 | 0.50 | [0.53, 7.50] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 476.63 ms | 28.14 | 6.45 | [432.00, 512.00] |
| 4 to 6 | 19 | 474.32 ms | 30.15 | 6.92 | [436.00, 512.00] |
| 5 to 6 | 9 | 483.56 ms | 30.75 | 10.25 | [432.00, 512.00] |
| 6 to 6 | 14 | 468.00 ms | 17.68 | 4.73 | [432.00, 492.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 4.65 µV | 2.13 | 0.49 | [1.70, 11.34] |
| 4 to 6 | 19 | 5.93 µV | 3.35 | 0.77 | [0.88, 12.37] |
| 5 to 6 | 9 | 7.28 µV | 3.04 | 1.01 | [4.06, 14.63] |
| 6 to 6 | 14 | 4.71 µV | 2.44 | 0.65 | [1.85, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 433.34, BIC = 447.64
- **4 to 6 vs 3 to 6**: *β* = 8.05, *SE* = 3.560, *z* = 2.260, *p* = 0.024
- **5 to 6 vs 3 to 6**: *β* = 4.75, *SE* = 3.638, *z* = 1.306, *p* = 0.191
- **6 to 6 vs 3 to 6**: *β* = 2.59, *SE* = 3.588, *z* = 0.721, *p* = 0.471
- **SNR**: *β* = -0.15, *SE* = 0.600, *z* = -0.243, *p* = 0.808

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -8.05 | 3.56 | -2.26 | 0.024 | 0.135 | n.s. |
| 3 to 6 - 5 to 6 | -4.75 | 3.64 | -1.31 | 0.191 | 0.572 | n.s. |
| 3 to 6 - 6 to 6 | -2.59 | 3.59 | -0.72 | 0.471 | 0.753 | n.s. |
| 4 to 6 - 5 to 6 | 3.29 | 3.70 | 0.89 | 0.373 | 0.753 | n.s. |
| 4 to 6 - 6 to 6 | 5.46 | 3.65 | 1.50 | 0.134 | 0.513 | n.s. |
| 5 to 6 - 6 to 6 | 2.17 | 3.67 | 0.59 | 0.555 | 0.753 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.63, *p* = 0.145, η²_G = 0.371
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -3.02 | 2 | = 0.283 | -1.23 [-2.09, -0.01] | large | n.s. |
| 3 to 6 vs 5 to 6 | -1.44 | 2 | = 0.575 | -1.39 [-1.80, 0.83] | large | n.s. |
| 3 to 6 vs 6 to 6 | -3.50 | 2 | = 0.283 | -1.12 [-1.04, 0.43] | large | n.s. |
| 4 to 6 vs 5 to 6 | 0.00 | 2 | = 1.000 | 0.00 [-0.55, 0.89] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | 1.00 | 2 | = 0.634 | 0.20 [-0.41, 1.05] | small | n.s. |
| 5 to 6 vs 6 to 6 | 0.28 | 2 | = 0.969 | 0.26 [-0.60, 1.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 239.05, BIC = 253.35
- **4 to 6 vs 3 to 6**: *β* = 0.27, *SE* = 0.613, *z* = 0.445, *p* = 0.656
- **5 to 6 vs 3 to 6**: *β* = -1.85, *SE* = 0.636, *z* = -2.913, *p* = 0.004
- **6 to 6 vs 3 to 6**: *β* = 0.67, *SE* = 0.639, *z* = 1.053, *p* = 0.293
- **SNR**: *β* = -0.72, *SE* = 0.110, *z* = -6.547, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.27 | 0.61 | -0.45 | 0.656 | 0.776 | n.s. |
| 3 to 6 - 5 to 6 | 1.85 | 0.64 | 2.91 | 0.004 | 0.014 | * |
| 3 to 6 - 6 to 6 | -0.67 | 0.64 | -1.05 | 0.293 | 0.646 | n.s. |
| 4 to 6 - 5 to 6 | 2.13 | 0.62 | 3.42 | < .001 | 0.003 | ** |
| 4 to 6 - 6 to 6 | -0.40 | 0.63 | -0.63 | 0.527 | 0.776 | n.s. |
| 5 to 6 - 6 to 6 | -2.53 | 0.65 | -3.91 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.76, *p* = 0.134, η²_G = 0.283
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.88 | 2 | = 0.565 | -0.31 [-0.49, 1.23] | small | n.s. |
| 3 to 6 vs 5 to 6 | 0.53 | 2 | = 0.650 | 0.25 [-0.66, 2.14] | small | n.s. |
| 3 to 6 vs 6 to 6 | 2.84 | 2 | = 0.502 | 0.94 [-0.34, 1.14] | large | n.s. |
| 4 to 6 vs 5 to 6 | 1.26 | 2 | = 0.502 | 0.61 [0.08, 1.80] | medium | n.s. |
| 4 to 6 vs 6 to 6 | 1.85 | 2 | = 0.502 | 1.17 [-0.58, 0.86] | large | n.s. |
| 5 to 6 vs 6 to 6 | 1.41 | 2 | = 0.502 | 0.93 [-1.05, 0.64] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 678.29, BIC = 694.88
- **4 to 6 vs 3 to 6**: *β* = -0.70, *SE* = 3.859, *z* = -0.181, *p* = 0.856
- **5 to 6 vs 3 to 6**: *β* = 2.34, *SE* = 5.055, *z* = 0.463, *p* = 0.643
- **6 to 6 vs 3 to 6**: *β* = 5.08, *SE* = 3.855, *z* = 1.318, *p* = 0.187
- **SNR**: *β* = -0.46, *SE* = 0.850, *z* = -0.545, *p* = 0.586

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 0.70 | 3.86 | 0.18 | 0.856 | 0.965 | n.s. |
| 3 to 6 - 5 to 6 | -2.34 | 5.05 | -0.46 | 0.643 | 0.965 | n.s. |
| 3 to 6 - 6 to 6 | -5.08 | 3.85 | -1.32 | 0.187 | 0.646 | n.s. |
| 4 to 6 - 5 to 6 | -3.04 | 5.31 | -0.57 | 0.567 | 0.965 | n.s. |
| 4 to 6 - 6 to 6 | -5.78 | 4.00 | -1.45 | 0.148 | 0.618 | n.s. |
| 5 to 6 - 6 to 6 | -2.74 | 4.89 | -0.56 | 0.575 | 0.965 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.298, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.29 | 11 | = 0.781 | 0.10 [-0.36, 0.55] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -1.33 | 11 | = 0.421 | -0.21 [-1.04, 0.27] | small | n.s. |
| 3 to 6 vs 6 to 6 | -1.43 | 11 | = 0.421 | -0.47 [-0.81, 0.12] | small | n.s. |
| 4 to 6 vs 5 to 6 | -1.04 | 11 | = 0.479 | -0.29 [-0.95, 0.35] | small | n.s. |
| 4 to 6 vs 6 to 6 | -1.76 | 11 | = 0.421 | -0.56 [-0.83, 0.11] | medium | n.s. |
| 5 to 6 vs 6 to 6 | -0.64 | 11 | = 0.645 | -0.19 [-0.82, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 350.32, BIC = 366.91
- **4 to 6 vs 3 to 6**: *β* = 0.65, *SE* = 0.507, *z* = 1.279, *p* = 0.201
- **5 to 6 vs 3 to 6**: *β* = -1.64, *SE* = 0.659, *z* = -2.493, *p* = 0.013
- **6 to 6 vs 3 to 6**: *β* = 0.83, *SE* = 0.508, *z* = 1.638, *p* = 0.101
- **SNR**: *β* = -0.64, *SE* = 0.111, *z* = -5.716, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.65 | 0.51 | -1.28 | 0.201 | 0.361 | n.s. |
| 3 to 6 - 5 to 6 | 1.64 | 0.66 | 2.49 | 0.013 | 0.050 | * |
| 3 to 6 - 6 to 6 | -0.83 | 0.51 | -1.64 | 0.101 | 0.274 | n.s. |
| 4 to 6 - 5 to 6 | 2.29 | 0.69 | 3.33 | < .001 | 0.004 | ** |
| 4 to 6 - 6 to 6 | -0.18 | 0.53 | -0.35 | 0.725 | 0.725 | n.s. |
| 5 to 6 - 6 to 6 | -2.48 | 0.64 | -3.88 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.22, *p* = 0.105, η²_G = 0.060
- Greenhouse-Geisser corrected: *p* = 0.136 (ε = 0.635)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.70 | 11 | = 0.234 | -0.41 [-0.50, 0.41] | small | n.s. |
| 3 to 6 vs 5 to 6 | -0.06 | 11 | = 0.955 | -0.02 [-0.65, 0.62] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | -2.99 | 11 | = 0.074 | -0.54 [-1.12, -0.13] | medium | n.s. |
| 4 to 6 vs 5 to 6 | 1.09 | 11 | = 0.357 | 0.39 [-0.34, 0.97] | small | n.s. |
| 4 to 6 vs 6 to 6 | -1.34 | 11 | = 0.310 | -0.20 [-0.95, 0.01] | negligible | n.s. |
| 5 to 6 vs 6 to 6 | -1.84 | 11 | = 0.234 | -0.52 [-1.21, 0.15] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 373.21, BIC = 386.45
- **4 to 6 vs 3 to 6**: *β* = 2.92, *SE* = 3.660, *z* = 0.797, *p* = 0.425
- **5 to 6 vs 3 to 6**: *β* = 3.13, *SE* = 3.811, *z* = 0.821, *p* = 0.412
- **6 to 6 vs 3 to 6**: *β* = 0.33, *SE* = 3.827, *z* = 0.087, *p* = 0.930
- **SNR**: *β* = 0.48, *SE* = 0.847, *z* = 0.564, *p* = 0.573

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -2.92 | 3.66 | -0.80 | 0.425 | 0.959 | n.s. |
| 3 to 6 - 5 to 6 | -3.13 | 3.81 | -0.82 | 0.412 | 0.959 | n.s. |
| 3 to 6 - 6 to 6 | -0.33 | 3.83 | -0.09 | 0.930 | 0.995 | n.s. |
| 4 to 6 - 5 to 6 | -0.21 | 3.39 | -0.06 | 0.951 | 0.995 | n.s. |
| 4 to 6 - 6 to 6 | 2.58 | 3.42 | 0.75 | 0.450 | 0.959 | n.s. |
| 5 to 6 - 6 to 6 | 2.79 | 3.44 | 0.81 | 0.417 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.68, *p* = 0.269, η²_G = 0.245
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 1.00 | 2 | = 0.634 | 0.90 [-0.76, 0.92] | large | n.s. |
| 3 to 6 vs 5 to 6 | 0.38 | 2 | = 0.742 | 0.16 [-1.10, 1.40] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | 1.51 | 2 | = 0.634 | 1.06 [-0.82, 1.31] | large | n.s. |
| 4 to 6 vs 5 to 6 | -1.31 | 2 | = 0.634 | -0.78 [-1.23, 0.50] | medium | n.s. |
| 4 to 6 vs 6 to 6 | 0.38 | 2 | = 0.742 | 0.11 [-0.60, 1.31] | negligible | n.s. |
| 5 to 6 vs 6 to 6 | 2.65 | 2 | = 0.634 | 0.94 [-0.65, 1.25] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 213.77, BIC = 227.01
- **4 to 6 vs 3 to 6**: *β* = 0.57, *SE* = 0.773, *z* = 0.737, *p* = 0.461
- **5 to 6 vs 3 to 6**: *β* = 1.44, *SE* = 0.772, *z* = 1.864, *p* = 0.062
- **6 to 6 vs 3 to 6**: *β* = -0.63, *SE* = 0.812, *z* = -0.778, *p* = 0.436
- **SNR**: *β* = 0.77, *SE* = 0.170, *z* = 4.497, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.57 | 0.77 | -0.74 | 0.461 | 0.682 | n.s. |
| 3 to 6 - 5 to 6 | -1.44 | 0.77 | -1.86 | 0.062 | 0.275 | n.s. |
| 3 to 6 - 6 to 6 | 0.63 | 0.81 | 0.78 | 0.436 | 0.682 | n.s. |
| 4 to 6 - 5 to 6 | -0.87 | 0.71 | -1.22 | 0.222 | 0.528 | n.s. |
| 4 to 6 - 6 to 6 | 1.20 | 0.72 | 1.67 | 0.095 | 0.329 | n.s. |
| 5 to 6 - 6 to 6 | 2.07 | 0.73 | 2.83 | 0.005 | 0.028 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.64, *p* = 0.615, η²_G = 0.211
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.95 | 2 | = 0.735 | -0.85 [-0.91, 0.76] | large | n.s. |
| 3 to 6 vs 5 to 6 | -0.32 | 2 | = 0.779 | -0.35 [-1.74, 0.86] | small | n.s. |
| 3 to 6 vs 6 to 6 | 0.94 | 2 | = 0.735 | 0.52 [-0.54, 1.75] | medium | n.s. |
| 4 to 6 vs 5 to 6 | 0.34 | 2 | = 0.779 | 0.21 [-1.10, 0.59] | small | n.s. |
| 4 to 6 vs 6 to 6 | 3.41 | 2 | = 0.457 | 1.96 [0.31, 3.31] | large | n.s. |
| 5 to 6 vs 6 to 6 | 0.84 | 2 | = 0.735 | 0.74 [-0.64, 1.25] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 585.18, BIC = 599.96
- **4 to 6 vs 3 to 6**: *β* = -3.31, *SE* = 8.435, *z* = -0.392, *p* = 0.695
- **5 to 6 vs 3 to 6**: *β* = 8.14, *SE* = 10.416, *z* = 0.781, *p* = 0.435
- **6 to 6 vs 3 to 6**: *β* = -8.46, *SE* = 8.921, *z* = -0.948, *p* = 0.343
- **SNR**: *β* = 0.87, *SE* = 1.476, *z* = 0.587, *p* = 0.557

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 3.31 | 8.44 | 0.39 | 0.695 | 0.828 | n.s. |
| 3 to 6 - 5 to 6 | -8.14 | 10.42 | -0.78 | 0.435 | 0.828 | n.s. |
| 3 to 6 - 6 to 6 | 8.46 | 8.92 | 0.95 | 0.343 | 0.828 | n.s. |
| 4 to 6 - 5 to 6 | -11.45 | 10.96 | -1.04 | 0.296 | 0.828 | n.s. |
| 4 to 6 - 6 to 6 | 5.15 | 9.06 | 0.57 | 0.569 | 0.828 | n.s. |
| 5 to 6 - 6 to 6 | 16.60 | 11.07 | 1.50 | 0.134 | 0.577 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.18, *p* = 0.910, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.51 | 6 | = 0.892 | 0.26 [-0.54, 0.49] | small | n.s. |
| 3 to 6 vs 5 to 6 | 0.03 | 6 | = 0.977 | 0.02 [-1.02, 0.54] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | 0.34 | 6 | = 0.892 | 0.17 [-0.27, 0.98] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -0.67 | 6 | = 0.892 | -0.26 [-1.06, 0.51] | small | n.s. |
| 4 to 6 vs 6 to 6 | -0.61 | 6 | = 0.892 | -0.17 [-0.55, 0.66] | negligible | n.s. |
| 5 to 6 vs 6 to 6 | 0.37 | 6 | = 0.892 | 0.16 [-0.79, 1.07] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 256.53, BIC = 271.30
- **4 to 6 vs 3 to 6**: *β* = 0.41, *SE* = 0.463, *z* = 0.889, *p* = 0.374
- **5 to 6 vs 3 to 6**: *β* = 2.94, *SE* = 0.569, *z* = 5.177, *p* < .001
- **6 to 6 vs 3 to 6**: *β* = -0.13, *SE* = 0.479, *z* = -0.265, *p* = 0.791
- **SNR**: *β* = 0.64, *SE* = 0.100, *z* = 6.334, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.41 | 0.46 | -0.89 | 0.374 | 0.622 | n.s. |
| 3 to 6 - 5 to 6 | -2.94 | 0.57 | -5.18 | < .001 | < .001 | *** |
| 3 to 6 - 6 to 6 | 0.13 | 0.48 | 0.26 | 0.791 | 0.791 | n.s. |
| 4 to 6 - 5 to 6 | -2.53 | 0.63 | -4.04 | < .001 | < .001 | *** |
| 4 to 6 - 6 to 6 | 0.54 | 0.50 | 1.09 | 0.277 | 0.622 | n.s. |
| 5 to 6 - 6 to 6 | 3.07 | 0.61 | 5.04 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.08, *p* = 0.022, η²_G = 0.189
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -3.41 | 6 | = 0.086 | -1.00 [-1.16, -0.04] | large | n.s. |
| 3 to 6 vs 5 to 6 | -2.46 | 6 | = 0.137 | -1.01 [-1.76, 0.04] | large | n.s. |
| 3 to 6 vs 6 to 6 | -0.83 | 6 | = 0.526 | -0.24 [-0.72, 0.50] | small | n.s. |
| 4 to 6 vs 5 to 6 | -0.27 | 6 | = 0.795 | -0.10 [-0.81, 0.73] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | 2.01 | 6 | = 0.137 | 0.75 [0.07, 1.45] | medium | n.s. |
| 5 to 6 vs 6 to 6 | 2.13 | 6 | = 0.137 | 0.79 [-0.26, 1.87] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.022) (no significant pairwise comparisons)

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
