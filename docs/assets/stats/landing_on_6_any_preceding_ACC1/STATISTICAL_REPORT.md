# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:29:27

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
| 3 to 6 | 24 | 98.83 ms | 11.28 | 2.30 | [84.00, 112.00] |
| 4 to 6 | 24 | 100.67 ms | 11.35 | 2.32 | [84.00, 112.00] |
| 5 to 6 | 16 | 101.00 ms | 9.06 | 2.27 | [84.00, 112.00] |
| 6 to 6 | 24 | 98.67 ms | 10.72 | 2.19 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | -2.15 µV | 2.09 | 0.43 | [-5.36, 1.55] |
| 4 to 6 | 24 | -1.66 µV | 2.38 | 0.49 | [-5.80, 3.38] |
| 5 to 6 | 16 | -4.44 µV | 4.55 | 1.14 | [-17.83, 1.30] |
| 6 to 6 | 24 | -2.29 µV | 2.29 | 0.47 | [-7.15, 0.96] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 169.50 ms | 20.73 | 4.23 | [136.00, 208.00] |
| 4 to 6 | 24 | 166.83 ms | 20.58 | 4.20 | [136.00, 200.00] |
| 5 to 6 | 16 | 171.00 ms | 24.98 | 6.24 | [136.00, 208.00] |
| 6 to 6 | 24 | 175.67 ms | 17.13 | 3.50 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | -6.89 µV | 2.92 | 0.60 | [-12.76, -1.85] |
| 4 to 6 | 24 | -6.43 µV | 3.84 | 0.78 | [-16.09, 0.71] |
| 5 to 6 | 16 | -5.24 µV | 4.46 | 1.12 | [-12.77, 2.93] |
| 6 to 6 | 24 | -5.40 µV | 3.26 | 0.67 | [-11.14, 2.35] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 97.33 ms | 11.60 | 2.37 | [80.00, 108.00] |
| 4 to 6 | 24 | 94.50 ms | 11.36 | 2.32 | [80.00, 108.00] |
| 5 to 6 | 16 | 100.50 ms | 8.99 | 2.25 | [80.00, 108.00] |
| 6 to 6 | 24 | 95.83 ms | 11.47 | 2.34 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 1.72 µV | 2.58 | 0.53 | [-2.10, 8.13] |
| 4 to 6 | 24 | 2.05 µV | 2.72 | 0.56 | [-3.11, 7.49] |
| 5 to 6 | 16 | 3.87 µV | 4.33 | 1.08 | [-4.87, 11.93] |
| 6 to 6 | 24 | 1.44 µV | 1.96 | 0.40 | [-2.11, 7.50] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 477.00 ms | 30.54 | 6.23 | [432.00, 512.00] |
| 4 to 6 | 24 | 476.50 ms | 29.24 | 5.97 | [436.00, 512.00] |
| 5 to 6 | 16 | 473.50 ms | 32.66 | 8.16 | [432.00, 512.00] |
| 6 to 6 | 24 | 462.83 ms | 22.02 | 4.49 | [432.00, 500.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 24 | 3.56 µV | 2.99 | 0.61 | [-3.85, 11.34] |
| 4 to 6 | 24 | 4.86 µV | 3.67 | 0.75 | [-0.71, 12.37] |
| 5 to 6 | 16 | 3.37 µV | 5.29 | 1.32 | [-5.88, 14.63] |
| 6 to 6 | 24 | 2.28 µV | 3.58 | 0.73 | [-3.43, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 673.90, BIC = 691.24
- **4 to 6 vs 3 to 6**: *β* = 1.85, *SE* = 2.711, *z* = 0.683, *p* = 0.495
- **5 to 6 vs 3 to 6**: *β* = 1.38, *SE* = 3.096, *z* = 0.445, *p* = 0.657
- **6 to 6 vs 3 to 6**: *β* = -0.11, *SE* = 2.739, *z* = -0.040, *p* = 0.968
- **SNR**: *β* = -0.08, *SE* = 0.583, *z* = -0.137, *p* = 0.891

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -1.85 | 2.71 | -0.68 | 0.495 | 0.978 | n.s. |
| 3 to 6 - 5 to 6 | -1.38 | 3.10 | -0.44 | 0.657 | 0.981 | n.s. |
| 3 to 6 - 6 to 6 | 0.11 | 2.74 | 0.04 | 0.968 | 0.985 | n.s. |
| 4 to 6 - 5 to 6 | 0.47 | 3.09 | 0.15 | 0.878 | 0.985 | n.s. |
| 4 to 6 - 6 to 6 | 1.96 | 2.72 | 0.72 | 0.471 | 0.978 | n.s. |
| 5 to 6 - 6 to 6 | 1.49 | 3.10 | 0.48 | 0.631 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.881, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.18 | 15 | = 0.861 | 0.05 [-0.59, 0.26] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 0.36 | 15 | = 0.861 | 0.13 [-0.44, 0.62] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | 0.83 | 15 | = 0.861 | 0.23 [-0.41, 0.43] | small | n.s. |
| 4 to 6 vs 5 to 6 | 0.22 | 15 | = 0.861 | 0.07 [-0.48, 0.59] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | 0.56 | 15 | = 0.861 | 0.18 [-0.29, 0.56] | negligible | n.s. |
| 5 to 6 vs 6 to 6 | 0.39 | 15 | = 0.861 | 0.12 [-0.44, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 410.04, BIC = 427.38
- **4 to 6 vs 3 to 6**: *β* = 0.68, *SE* = 0.648, *z* = 1.051, *p* = 0.293
- **5 to 6 vs 3 to 6**: *β* = -1.98, *SE* = 0.731, *z* = -2.709, *p* = 0.007
- **6 to 6 vs 3 to 6**: *β* = 0.45, *SE* = 0.654, *z* = 0.691, *p* = 0.489
- **SNR**: *β* = -0.83, *SE* = 0.135, *z* = -6.150, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.68 | 0.65 | -1.05 | 0.293 | 0.647 | n.s. |
| 3 to 6 - 5 to 6 | 1.98 | 0.73 | 2.71 | 0.007 | 0.027 | * |
| 3 to 6 - 6 to 6 | -0.45 | 0.65 | -0.69 | 0.489 | 0.739 | n.s. |
| 4 to 6 - 5 to 6 | 2.66 | 0.73 | 3.65 | < .001 | 0.002 | ** |
| 4 to 6 - 6 to 6 | 0.23 | 0.65 | 0.35 | 0.725 | 0.739 | n.s. |
| 5 to 6 - 6 to 6 | -2.43 | 0.73 | -3.33 | < .001 | 0.004 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.05, *p* = 0.038, η²_G = 0.137
- Greenhouse-Geisser corrected: *p* = 0.070 (ε = 0.585)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.17 | 15 | = 0.870 | -0.05 [-0.59, 0.26] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 1.96 | 15 | = 0.208 | 0.75 [-0.07, 1.05] | medium | n.s. |
| 3 to 6 vs 6 to 6 | 0.46 | 15 | = 0.784 | 0.15 [-0.38, 0.47] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 2.43 | 15 | = 0.169 | 0.78 [0.03, 1.19] | medium | n.s. |
| 4 to 6 vs 6 to 6 | 0.57 | 15 | = 0.784 | 0.21 [-0.24, 0.61] | small | n.s. |
| 5 to 6 vs 6 to 6 | -1.63 | 15 | = 0.247 | -0.65 [-0.96, 0.15] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 759.10, BIC = 776.44
- **4 to 6 vs 3 to 6**: *β* = -2.70, *SE* = 3.781, *z* = -0.715, *p* = 0.475
- **5 to 6 vs 3 to 6**: *β* = 2.86, *SE* = 4.645, *z* = 0.615, *p* = 0.539
- **6 to 6 vs 3 to 6**: *β* = 6.25, *SE* = 3.824, *z* = 1.634, *p* = 0.102
- **SNR**: *β* = 0.11, *SE* = 0.838, *z* = 0.129, *p* = 0.898

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 2.70 | 3.78 | 0.71 | 0.475 | 0.830 | n.s. |
| 3 to 6 - 5 to 6 | -2.86 | 4.65 | -0.61 | 0.539 | 0.830 | n.s. |
| 3 to 6 - 6 to 6 | -6.25 | 3.82 | -1.63 | 0.102 | 0.417 | n.s. |
| 4 to 6 - 5 to 6 | -5.56 | 4.76 | -1.17 | 0.242 | 0.671 | n.s. |
| 4 to 6 - 6 to 6 | -8.95 | 3.88 | -2.31 | 0.021 | 0.120 | n.s. |
| 5 to 6 - 6 to 6 | -3.39 | 4.45 | -0.76 | 0.446 | 0.830 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.75, *p* = 0.169, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.14 | 15 | = 0.892 | 0.03 [-0.28, 0.57] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -1.66 | 15 | = 0.234 | -0.20 [-0.97, 0.14] | small | n.s. |
| 3 to 6 vs 6 to 6 | -1.74 | 15 | = 0.234 | -0.50 [-0.75, 0.12] | small | n.s. |
| 4 to 6 vs 5 to 6 | -1.14 | 15 | = 0.409 | -0.24 [-0.83, 0.26] | small | n.s. |
| 4 to 6 vs 6 to 6 | -1.84 | 15 | = 0.234 | -0.53 [-0.89, -0.00] | medium | n.s. |
| 5 to 6 vs 6 to 6 | -0.83 | 15 | = 0.505 | -0.23 [-0.75, 0.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 439.21, BIC = 456.56
- **4 to 6 vs 3 to 6**: *β* = 0.65, *SE* = 0.668, *z* = 0.978, *p* = 0.328
- **5 to 6 vs 3 to 6**: *β* = 0.21, *SE* = 0.811, *z* = 0.253, *p* = 0.800
- **6 to 6 vs 3 to 6**: *β* = 1.04, *SE* = 0.676, *z* = 1.542, *p* = 0.123
- **SNR**: *β* = -0.59, *SE* = 0.151, *z* = -3.901, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.65 | 0.67 | -0.98 | 0.328 | 0.811 | n.s. |
| 3 to 6 - 5 to 6 | -0.21 | 0.81 | -0.25 | 0.800 | 0.921 | n.s. |
| 3 to 6 - 6 to 6 | -1.04 | 0.68 | -1.54 | 0.123 | 0.545 | n.s. |
| 4 to 6 - 5 to 6 | 0.45 | 0.83 | 0.54 | 0.589 | 0.921 | n.s. |
| 4 to 6 - 6 to 6 | -0.39 | 0.69 | -0.57 | 0.572 | 0.921 | n.s. |
| 5 to 6 - 6 to 6 | -0.84 | 0.78 | -1.07 | 0.283 | 0.811 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.250, η²_G = 0.034
- Greenhouse-Geisser corrected: *p* = 0.259 (ε = 0.575)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -2.02 | 15 | = 0.185 | -0.42 [-0.57, 0.28] | small | n.s. |
| 3 to 6 vs 5 to 6 | -1.46 | 15 | = 0.332 | -0.39 [-0.91, 0.19] | small | n.s. |
| 3 to 6 vs 6 to 6 | -2.25 | 15 | = 0.185 | -0.49 [-0.99, -0.09] | small | n.s. |
| 4 to 6 vs 5 to 6 | -0.30 | 15 | = 0.920 | -0.09 [-0.61, 0.46] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | -0.91 | 15 | = 0.565 | -0.11 [-1.00, -0.09] | negligible | n.s. |
| 5 to 6 vs 6 to 6 | -0.00 | 15 | = 0.998 | -0.00 [-0.53, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 676.80, BIC = 694.15
- **4 to 6 vs 3 to 6**: *β* = -2.94, *SE* = 2.733, *z* = -1.075, *p* = 0.282
- **5 to 6 vs 3 to 6**: *β* = 1.81, *SE* = 3.138, *z* = 0.576, *p* = 0.564
- **6 to 6 vs 3 to 6**: *β* = -1.41, *SE* = 2.730, *z* = -0.517, *p* = 0.605
- **SNR**: *β* = 0.33, *SE* = 0.745, *z* = 0.441, *p* = 0.660

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 2.94 | 2.73 | 1.08 | 0.282 | 0.809 | n.s. |
| 3 to 6 - 5 to 6 | -1.81 | 3.14 | -0.58 | 0.564 | 0.917 | n.s. |
| 3 to 6 - 6 to 6 | 1.41 | 2.73 | 0.52 | 0.605 | 0.917 | n.s. |
| 4 to 6 - 5 to 6 | -4.75 | 3.12 | -1.52 | 0.128 | 0.560 | n.s. |
| 4 to 6 - 6 to 6 | -1.53 | 2.76 | -0.55 | 0.580 | 0.917 | n.s. |
| 5 to 6 - 6 to 6 | 3.22 | 3.17 | 1.02 | 0.309 | 0.809 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.383, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 1.47 | 15 | = 0.563 | 0.44 [-0.18, 0.67] | small | n.s. |
| 3 to 6 vs 5 to 6 | 0.09 | 15 | = 0.926 | 0.03 [-0.51, 0.56] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | 0.85 | 15 | = 0.563 | 0.24 [-0.33, 0.52] | small | n.s. |
| 4 to 6 vs 5 to 6 | -1.27 | 15 | = 0.563 | -0.43 [-0.86, 0.23] | small | n.s. |
| 4 to 6 vs 6 to 6 | -0.74 | 15 | = 0.563 | -0.19 [-0.51, 0.33] | negligible | n.s. |
| 5 to 6 vs 6 to 6 | 0.75 | 15 | = 0.563 | 0.22 [-0.35, 0.73] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 441.28, BIC = 458.62
- **4 to 6 vs 3 to 6**: *β* = 0.21, *SE* = 0.758, *z* = 0.281, *p* = 0.779
- **5 to 6 vs 3 to 6**: *β* = 1.98, *SE* = 0.859, *z* = 2.304, *p* = 0.021
- **6 to 6 vs 3 to 6**: *β* = -0.19, *SE* = 0.757, *z* = -0.251, *p* = 0.801
- **SNR**: *β* = 0.36, *SE* = 0.198, *z* = 1.817, *p* = 0.069

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.21 | 0.76 | -0.28 | 0.779 | 0.951 | n.s. |
| 3 to 6 - 5 to 6 | -1.98 | 0.86 | -2.30 | 0.021 | 0.102 | n.s. |
| 3 to 6 - 6 to 6 | 0.19 | 0.76 | 0.25 | 0.801 | 0.951 | n.s. |
| 4 to 6 - 5 to 6 | -1.77 | 0.85 | -2.07 | 0.039 | 0.145 | n.s. |
| 4 to 6 - 6 to 6 | 0.40 | 0.76 | 0.53 | 0.598 | 0.935 | n.s. |
| 5 to 6 - 6 to 6 | 2.17 | 0.87 | 2.50 | 0.012 | 0.072 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.81, *p* = 0.050, η²_G = 0.112
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.08 | 15 | = 0.443 | -0.26 [-0.54, 0.31] | small | n.s. |
| 3 to 6 vs 5 to 6 | -2.14 | 15 | = 0.193 | -0.71 [-1.11, 0.03] | medium | n.s. |
| 3 to 6 vs 6 to 6 | -0.04 | 15 | = 0.970 | -0.01 [-0.33, 0.51] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -1.77 | 15 | = 0.193 | -0.53 [-1.00, 0.12] | medium | n.s. |
| 4 to 6 vs 6 to 6 | 0.73 | 15 | = 0.574 | 0.27 [-0.26, 0.59] | small | n.s. |
| 5 to 6 vs 6 to 6 | 1.96 | 15 | = 0.193 | 0.73 [-0.07, 1.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 846.27, BIC = 863.61
- **4 to 6 vs 3 to 6**: *β* = 0.85, *SE* = 7.704, *z* = 0.111, *p* = 0.912
- **5 to 6 vs 3 to 6**: *β* = -4.16, *SE* = 8.607, *z* = -0.483, *p* = 0.629
- **6 to 6 vs 3 to 6**: *β* = -13.61, *SE* = 7.642, *z* = -1.780, *p* = 0.075
- **SNR**: *β* = -1.45, *SE* = 1.140, *z* = -1.267, *p* = 0.205

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.85 | 7.70 | -0.11 | 0.912 | 0.919 | n.s. |
| 3 to 6 - 5 to 6 | 4.16 | 8.61 | 0.48 | 0.629 | 0.919 | n.s. |
| 3 to 6 - 6 to 6 | 13.60 | 7.64 | 1.78 | 0.075 | 0.323 | n.s. |
| 4 to 6 - 5 to 6 | 5.01 | 8.75 | 0.57 | 0.567 | 0.919 | n.s. |
| 4 to 6 - 6 to 6 | 14.46 | 7.66 | 1.89 | 0.059 | 0.305 | n.s. |
| 5 to 6 - 6 to 6 | 9.45 | 8.65 | 1.09 | 0.275 | 0.723 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.726, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 0.17 | 15 | = 0.977 | 0.05 [-0.41, 0.43] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 0.15 | 15 | = 0.977 | 0.06 [-0.49, 0.57] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | 1.12 | 15 | = 0.747 | 0.36 [-0.02, 0.86] | small | n.s. |
| 4 to 6 vs 5 to 6 | 0.03 | 15 | = 0.977 | 0.01 [-0.53, 0.54] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | 0.98 | 15 | = 0.747 | 0.32 [-0.05, 0.83] | small | n.s. |
| 5 to 6 vs 6 to 6 | 0.92 | 15 | = 0.747 | 0.30 [-0.31, 0.77] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 466.57, BIC = 483.91
- **4 to 6 vs 3 to 6**: *β* = 1.08, *SE* = 0.738, *z* = 1.467, *p* = 0.142
- **5 to 6 vs 3 to 6**: *β* = -0.52, *SE* = 0.844, *z* = -0.616, *p* = 0.538
- **6 to 6 vs 3 to 6**: *β* = -1.37, *SE* = 0.729, *z* = -1.878, *p* = 0.060
- **SNR**: *β* = 0.23, *SE* = 0.136, *z* = 1.676, *p* = 0.094

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -1.08 | 0.74 | -1.47 | 0.142 | 0.369 | n.s. |
| 3 to 6 - 5 to 6 | 0.52 | 0.84 | 0.62 | 0.538 | 0.538 | n.s. |
| 3 to 6 - 6 to 6 | 1.37 | 0.73 | 1.88 | 0.060 | 0.268 | n.s. |
| 4 to 6 - 5 to 6 | 1.60 | 0.87 | 1.84 | 0.066 | 0.268 | n.s. |
| 4 to 6 - 6 to 6 | 2.45 | 0.73 | 3.35 | < .001 | 0.005 | ** |
| 5 to 6 - 6 to 6 | 0.85 | 0.85 | 0.99 | 0.320 | 0.538 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.66, *p* = 0.019, η²_G = 0.073
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -3.57 | 15 | = 0.008 | -0.69 [-0.95, -0.05] | medium | ** |
| 3 to 6 vs 5 to 6 | 0.32 | 15 | = 0.901 | 0.07 [-0.45, 0.61] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | 0.60 | 15 | = 0.837 | 0.13 [-0.10, 0.77] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 2.26 | 15 | = 0.078 | 0.56 [-0.01, 1.14] | medium | n.s. |
| 4 to 6 vs 6 to 6 | 4.02 | 15 | = 0.007 | 0.73 [0.34, 1.32] | medium | ** |
| 5 to 6 vs 6 to 6 | 0.09 | 15 | = 0.931 | 0.02 [-0.51, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.038) (no significant pairwise comparisons)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.050)
**P3b amplitude:** Significant main effect of condition (*p* = 0.019). Post-hoc tests revealed:
  - 3 to 6 showed smaller amplitude than 4 to 6 (*d* = -0.69)
  - 4 to 6 showed greater amplitude than 6 to 6 (*d* = 0.73)

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
