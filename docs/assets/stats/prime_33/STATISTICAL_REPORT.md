# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:46:52

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
| 3a | 8 | 109.50 ms | 12.99 | 4.59 | [88.00, 120.00] |
| 3b | 9 | 102.22 ms | 9.82 | 3.27 | [88.00, 120.00] |
| 3c | 12 | 104.33 ms | 13.15 | 3.80 | [88.00, 120.00] |
| 3d | 12 | 102.67 ms | 14.20 | 4.10 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 8 | 4.96 µV | 1.67 | 0.59 | [2.79, 7.39] |
| 3b | 9 | 4.23 µV | 1.46 | 0.49 | [1.84, 6.27] |
| 3c | 12 | 6.03 µV | 3.05 | 0.88 | [1.36, 10.49] |
| 3d | 12 | 4.21 µV | 1.84 | 0.53 | [1.11, 8.31] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 20 | 167.60 ms | 19.89 | 4.45 | [140.00, 208.00] |
| 3b | 14 | 180.86 ms | 17.06 | 4.56 | [148.00, 200.00] |
| 3c | 20 | 169.20 ms | 21.37 | 4.78 | [140.00, 208.00] |
| 3d | 22 | 175.27 ms | 21.01 | 4.48 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 20 | -5.96 µV | 2.45 | 0.55 | [-10.33, -2.67] |
| 3b | 14 | -6.63 µV | 4.57 | 1.22 | [-20.82, -1.79] |
| 3c | 20 | -6.76 µV | 2.68 | 0.60 | [-12.64, -2.69] |
| 3d | 22 | -7.44 µV | 2.58 | 0.55 | [-12.45, -2.61] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 104.50 ms | 11.21 | 2.80 | [92.00, 120.00] |
| 3b | 11 | 106.55 ms | 10.92 | 3.29 | [92.00, 120.00] |
| 3c | 12 | 106.00 ms | 12.71 | 3.67 | [92.00, 120.00] |
| 3d | 9 | 108.89 ms | 11.62 | 3.87 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 5.93 µV | 4.31 | 1.08 | [1.26, 18.79] |
| 3b | 11 | 6.06 µV | 3.73 | 1.13 | [2.33, 15.17] |
| 3c | 12 | 4.76 µV | 2.03 | 0.59 | [1.71, 8.13] |
| 3d | 9 | 4.39 µV | 3.09 | 1.03 | [0.95, 10.87] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 456.75 ms | 15.12 | 3.78 | [432.00, 480.00] |
| 3b | 11 | 449.45 ms | 11.90 | 3.59 | [432.00, 468.00] |
| 3c | 11 | 458.55 ms | 14.23 | 4.29 | [432.00, 480.00] |
| 3d | 15 | 455.73 ms | 15.30 | 3.95 | [432.00, 480.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 7.34 µV | 2.97 | 0.74 | [2.32, 13.95] |
| 3b | 11 | 5.58 µV | 2.92 | 0.88 | [2.15, 11.07] |
| 3c | 11 | 7.14 µV | 2.44 | 0.74 | [3.91, 11.93] |
| 3d | 15 | 6.00 µV | 3.56 | 0.92 | [1.83, 17.08] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 333.74, BIC = 345.74
- **3b vs 3a**: *β* = -7.84, *SE* = 5.736, *z* = -1.366, *p* = 0.172
- **3c vs 3a**: *β* = -4.21, *SE* = 5.484, *z* = -0.767, *p* = 0.443
- **3d vs 3a**: *β* = -6.77, *SE* = 5.477, *z* = -1.236, *p* = 0.217
- **SNR**: *β* = 2.22, *SE* = 1.792, *z* = 1.238, *p* = 0.216

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 7.84 | 5.74 | 1.37 | 0.172 | 0.677 | n.s. |
| 3a - 3c | 4.21 | 5.48 | 0.77 | 0.443 | 0.904 | n.s. |
| 3a - 3d | 6.77 | 5.48 | 1.24 | 0.217 | 0.705 | n.s. |
| 3b - 3c | -3.63 | 5.42 | -0.67 | 0.503 | 0.904 | n.s. |
| 3b - 3d | -1.07 | 5.34 | -0.20 | 0.841 | 0.904 | n.s. |
| 3c - 3d | 2.56 | 4.91 | 0.52 | 0.602 | 0.904 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 175.85, BIC = 187.85
- **3b vs 3a**: *β* = -1.32, *SE* = 0.676, *z* = -1.951, *p* = 0.051
- **3c vs 3a**: *β* = 0.96, *SE* = 0.673, *z* = 1.429, *p* = 0.153
- **3d vs 3a**: *β* = -1.44, *SE* = 0.669, *z* = -2.148, *p* = 0.032
- **SNR**: *β* = 1.10, *SE* = 0.253, *z* = 4.336, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 1.32 | 0.68 | 1.95 | 0.051 | 0.145 | n.s. |
| 3a - 3c | -0.96 | 0.67 | -1.43 | 0.153 | 0.282 | n.s. |
| 3a - 3d | 1.44 | 0.67 | 2.15 | 0.032 | 0.121 | n.s. |
| 3b - 3c | -2.28 | 0.67 | -3.41 | < .001 | 0.003 | ** |
| 3b - 3d | 0.12 | 0.62 | 0.19 | 0.850 | 0.850 | n.s. |
| 3c - 3d | 2.40 | 0.64 | 3.77 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 681.78, BIC = 698.09
- **3b vs 3a**: *β* = 13.12, *SE* = 6.648, *z* = 1.974, *p* = 0.048
- **3c vs 3a**: *β* = 1.71, *SE* = 6.030, *z* = 0.284, *p* = 0.776
- **3d vs 3a**: *β* = 7.75, *SE* = 6.021, *z* = 1.286, *p* = 0.198
- **SNR**: *β* = 0.00, *SE* = 1.378, *z* = 0.001, *p* = 0.999

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -13.12 | 6.65 | -1.97 | 0.048 | 0.257 | n.s. |
| 3a - 3c | -1.71 | 6.03 | -0.28 | 0.776 | 0.776 | n.s. |
| 3a - 3d | -7.75 | 6.02 | -1.29 | 0.198 | 0.587 | n.s. |
| 3b - 3c | 11.41 | 6.69 | 1.71 | 0.088 | 0.369 | n.s. |
| 3b - 3d | 5.38 | 6.65 | 0.81 | 0.419 | 0.686 | n.s. |
| 3c - 3d | -6.03 | 6.07 | -0.99 | 0.320 | 0.686 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.58, *p* = 0.217, η²_G = 0.113
- Greenhouse-Geisser corrected: *p* = 0.238 (ε = 0.534)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -1.25 | 9 | = 0.485 | -0.55 [-1.10, 0.12] | medium | n.s. |
| 3a vs 3c | 0.72 | 9 | = 0.622 | 0.27 [-0.53, 0.50] | small | n.s. |
| 3a vs 3d | -0.67 | 9 | = 0.622 | -0.37 [-0.70, 0.30] | small | n.s. |
| 3b vs 3c | 2.69 | 9 | = 0.149 | 1.16 [-0.27, 1.05] | large | n.s. |
| 3b vs 3d | 0.38 | 9 | = 0.712 | 0.13 [-0.44, 0.84] | negligible | n.s. |
| 3c vs 3d | -1.81 | 9 | = 0.312 | -0.75 [-0.75, 0.26] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 369.90, BIC = 386.21
- **3b vs 3a**: *β* = -0.50, *SE* = 0.818, *z* = -0.615, *p* = 0.539
- **3c vs 3a**: *β* = -0.79, *SE* = 0.742, *z* = -1.064, *p* = 0.288
- **3d vs 3a**: *β* = -0.68, *SE* = 0.741, *z* = -0.912, *p* = 0.362
- **SNR**: *β* = -0.85, *SE* = 0.169, *z* = -5.036, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.50 | 0.82 | 0.61 | 0.539 | 0.955 | n.s. |
| 3a - 3c | 0.79 | 0.74 | 1.06 | 0.288 | 0.869 | n.s. |
| 3a - 3d | 0.68 | 0.74 | 0.91 | 0.362 | 0.894 | n.s. |
| 3b - 3c | 0.29 | 0.82 | 0.35 | 0.728 | 0.980 | n.s. |
| 3b - 3d | 0.17 | 0.83 | 0.21 | 0.834 | 0.980 | n.s. |
| 3c - 3d | -0.11 | 0.75 | -0.15 | 0.880 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.391, η²_G = 0.066
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.49 | 9 | = 0.636 | 0.16 [-0.41, 0.76] | negligible | n.s. |
| 3a vs 3c | 1.71 | 9 | = 0.367 | 0.61 [-0.30, 0.75] | medium | n.s. |
| 3a vs 3d | 1.91 | 9 | = 0.367 | 1.05 [-0.11, 0.92] | large | n.s. |
| 3b vs 3c | 0.50 | 9 | = 0.636 | 0.18 [-0.63, 0.64] | negligible | n.s. |
| 3b vs 3d | 0.84 | 9 | = 0.636 | 0.39 [-0.30, 1.01] | small | n.s. |
| 3c vs 3d | 0.78 | 9 | = 0.636 | 0.37 [-0.32, 0.68] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 380.93, BIC = 394.03
- **3b vs 3a**: *β* = 1.84, *SE* = 4.345, *z* = 0.424, *p* = 0.671
- **3c vs 3a**: *β* = 1.27, *SE* = 4.386, *z* = 0.290, *p* = 0.772
- **3d vs 3a**: *β* = 3.52, *SE* = 4.859, *z* = 0.724, *p* = 0.469
- **SNR**: *β* = -0.71, *SE* = 0.997, *z* = -0.710, *p* = 0.478

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -1.84 | 4.34 | -0.42 | 0.671 | 0.995 | n.s. |
| 3a - 3c | -1.27 | 4.39 | -0.29 | 0.772 | 0.995 | n.s. |
| 3a - 3d | -3.52 | 4.86 | -0.72 | 0.469 | 0.978 | n.s. |
| 3b - 3c | 0.57 | 4.72 | 0.12 | 0.903 | 0.995 | n.s. |
| 3b - 3d | -1.67 | 5.12 | -0.33 | 0.744 | 0.995 | n.s. |
| 3c - 3d | -2.25 | 4.96 | -0.45 | 0.651 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.02, *p* = 0.182, η²_G = 0.354
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.21 | 3 | = 0.846 | 0.17 [-0.73, 0.81] | negligible | n.s. |
| 3a vs 3c | 1.75 | 3 | = 0.363 | 1.59 [-0.59, 1.11] | large | n.s. |
| 3a vs 3d | 0.34 | 3 | = 0.846 | 0.28 [-1.02, 0.66] | small | n.s. |
| 3b vs 3c | 2.72 | 3 | = 0.363 | 1.49 [-0.58, 2.35] | large | n.s. |
| 3b vs 3d | 0.22 | 3 | = 0.846 | 0.19 [-0.76, 1.10] | negligible | n.s. |
| 3c vs 3d | -1.73 | 3 | = 0.363 | -1.00 [-1.50, 1.02] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 252.51, BIC = 265.61
- **3b vs 3a**: *β* = -0.18, *SE* = 0.875, *z* = -0.209, *p* = 0.835
- **3c vs 3a**: *β* = 0.28, *SE* = 0.943, *z* = 0.298, *p* = 0.766
- **3d vs 3a**: *β* = -0.44, *SE* = 0.960, *z* = -0.462, *p* = 0.644
- **SNR**: *β* = 0.69, *SE* = 0.234, *z* = 2.926, *p* = 0.003

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.18 | 0.88 | 0.21 | 0.835 | 0.994 | n.s. |
| 3a - 3c | -0.28 | 0.94 | -0.30 | 0.766 | 0.994 | n.s. |
| 3a - 3d | 0.44 | 0.96 | 0.46 | 0.644 | 0.994 | n.s. |
| 3b - 3c | -0.46 | 1.07 | -0.43 | 0.664 | 0.994 | n.s. |
| 3b - 3d | 0.26 | 1.03 | 0.25 | 0.799 | 0.994 | n.s. |
| 3c - 3d | 0.72 | 1.06 | 0.69 | 0.493 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.835, η²_G = 0.055
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.21 | 3 | = 0.849 | 0.18 [-0.62, 0.93] | negligible | n.s. |
| 3a vs 3c | 0.49 | 3 | = 0.849 | 0.39 [-0.77, 0.91] | small | n.s. |
| 3a vs 3d | 1.09 | 3 | = 0.849 | 0.76 [-0.54, 1.18] | medium | n.s. |
| 3b vs 3c | 0.35 | 3 | = 0.849 | 0.13 [-1.39, 1.10] | negligible | n.s. |
| 3b vs 3d | 0.51 | 3 | = 0.849 | 0.34 [-0.75, 1.11] | small | n.s. |
| 3c vs 3d | 0.62 | 3 | = 0.849 | 0.25 [-0.78, 1.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 442.66, BIC = 456.45
- **3b vs 3a**: *β* = -6.67, *SE* = 5.456, *z* = -1.223, *p* = 0.221
- **3c vs 3a**: *β* = 2.25, *SE* = 5.377, *z* = 0.419, *p* = 0.675
- **3d vs 3a**: *β* = -0.71, *SE* = 4.977, *z* = -0.143, *p* = 0.886
- **SNR**: *β* = 0.23, *SE* = 0.744, *z* = 0.303, *p* = 0.762

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 6.68 | 5.46 | 1.22 | 0.221 | 0.713 | n.s. |
| 3a - 3c | -2.25 | 5.38 | -0.42 | 0.675 | 0.928 | n.s. |
| 3a - 3d | 0.71 | 4.98 | 0.14 | 0.886 | 0.928 | n.s. |
| 3b - 3c | -8.93 | 5.78 | -1.54 | 0.123 | 0.544 | n.s. |
| 3b - 3d | -5.96 | 5.52 | -1.08 | 0.280 | 0.731 | n.s. |
| 3c - 3d | 2.97 | 5.41 | 0.55 | 0.584 | 0.928 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.489, η²_G = 0.173
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 1.21 | 3 | = 0.627 | 1.13 [-0.64, 1.25] | large | n.s. |
| 3a vs 3c | 0.63 | 3 | = 0.757 | 0.52 [-0.96, 0.59] | medium | n.s. |
| 3a vs 3d | 2.63 | 3 | = 0.234 | 0.64 [-0.46, 0.90] | medium | n.s. |
| 3b vs 3c | -2.78 | 3 | = 0.234 | -0.74 [-0.96, 0.89] | medium | n.s. |
| 3b vs 3d | -0.38 | 3 | = 0.757 | -0.32 [-1.22, 0.89] | small | n.s. |
| 3c vs 3d | 0.34 | 3 | = 0.757 | 0.24 [-0.43, 1.32] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 243.84, BIC = 257.63
- **3b vs 3a**: *β* = -0.99, *SE* = 0.780, *z* = -1.268, *p* = 0.205
- **3c vs 3a**: *β* = 0.60, *SE* = 0.766, *z* = 0.781, *p* = 0.435
- **3d vs 3a**: *β* = -0.24, *SE* = 0.713, *z* = -0.331, *p* = 0.741
- **SNR**: *β* = 0.74, *SE* = 0.115, *z* = 6.479, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.99 | 0.78 | 1.27 | 0.205 | 0.682 | n.s. |
| 3a - 3c | -0.60 | 0.77 | -0.78 | 0.435 | 0.730 | n.s. |
| 3a - 3d | 0.24 | 0.71 | 0.33 | 0.741 | 0.741 | n.s. |
| 3b - 3c | -1.59 | 0.82 | -1.93 | 0.054 | 0.282 | n.s. |
| 3b - 3d | -0.75 | 0.79 | -0.96 | 0.338 | 0.730 | n.s. |
| 3c - 3d | 0.83 | 0.77 | 1.08 | 0.279 | 0.730 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.404, η²_G = 0.125
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.62 | 3 | = 0.728 | 0.38 [-0.49, 1.46] | small | n.s. |
| 3a vs 3c | -1.13 | 3 | = 0.682 | -0.81 [-1.05, 0.51] | large | n.s. |
| 3a vs 3d | -0.57 | 3 | = 0.728 | -0.33 [-0.39, 0.99] | small | n.s. |
| 3b vs 3c | -5.48 | 3 | = 0.072 | -1.29 [-1.33, 0.58] | large | n.s. |
| 3b vs 3d | -1.16 | 3 | = 0.682 | -0.54 [-1.64, 0.60] | medium | n.s. |
| 3c vs 3d | 0.31 | 3 | = 0.779 | 0.13 [-0.64, 1.05] | negligible | n.s. |

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
