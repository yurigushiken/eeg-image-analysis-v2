# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:48:00

---

## 1. Analysis Overview

**Total Measurements:** 328
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
| 4a | 10 | 110.80 ms | 10.51 | 3.32 | [92.00, 120.00] |
| 4b | 11 | 102.91 ms | 10.60 | 3.20 | [92.00, 120.00] |
| 4c | 2 | 106.00 ms | 19.80 | 14.00 | [92.00, 120.00] |
| 4d | 11 | 100.73 ms | 10.71 | 3.23 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 10 | 4.10 µV | 2.09 | 0.66 | [1.91, 8.80] |
| 4b | 11 | 3.55 µV | 2.96 | 0.89 | [0.93, 9.56] |
| 4c | 2 | 2.74 µV | 0.36 | 0.26 | [2.49, 3.00] |
| 4d | 11 | 4.87 µV | 2.97 | 0.90 | [1.26, 11.82] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 19 | 171.37 ms | 20.58 | 4.72 | [144.00, 208.00] |
| 4b | 20 | 174.20 ms | 20.95 | 4.68 | [144.00, 208.00] |
| 4c | 11 | 173.09 ms | 22.28 | 6.72 | [144.00, 208.00] |
| 4d | 17 | 171.06 ms | 17.35 | 4.21 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 19 | -7.79 µV | 4.41 | 1.01 | [-23.00, -2.44] |
| 4b | 20 | -6.80 µV | 3.34 | 0.75 | [-14.00, -2.57] |
| 4c | 11 | -7.61 µV | 3.81 | 1.15 | [-17.20, -2.73] |
| 4d | 17 | -7.32 µV | 3.79 | 0.92 | [-16.45, -3.30] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 10 | 110.00 ms | 12.11 | 3.83 | [96.00, 124.00] |
| 4b | 14 | 110.29 ms | 10.49 | 2.80 | [96.00, 124.00] |
| 4c | 11 | 107.27 ms | 10.09 | 3.04 | [96.00, 120.00] |
| 4d | 15 | 113.87 ms | 8.93 | 2.30 | [96.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 10 | 4.81 µV | 2.54 | 0.80 | [1.89, 9.80] |
| 4b | 14 | 3.74 µV | 1.85 | 0.50 | [1.62, 7.69] |
| 4c | 11 | 4.01 µV | 1.96 | 0.59 | [1.42, 7.04] |
| 4d | 15 | 5.15 µV | 3.20 | 0.83 | [1.01, 11.61] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 12 | 468.67 ms | 45.82 | 13.23 | [380.00, 524.00] |
| 4b | 13 | 456.31 ms | 62.66 | 17.38 | [364.00, 528.00] |
| 4c | 6 | 444.00 ms | 57.13 | 23.32 | [380.00, 512.00] |
| 4d | 11 | 446.55 ms | 59.93 | 18.07 | [368.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 12 | 7.51 µV | 3.60 | 1.04 | [2.74, 13.26] |
| 4b | 13 | 6.08 µV | 2.42 | 0.67 | [2.04, 10.90] |
| 4c | 6 | 5.67 µV | 2.24 | 0.92 | [2.89, 9.63] |
| 4d | 11 | 8.14 µV | 4.24 | 1.28 | [3.07, 15.73] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 269.45, BIC = 280.13
- **4b vs 4a**: *β* = -7.81, *SE* = 4.515, *z* = -1.729, *p* = 0.084
- **4c vs 4a**: *β* = -4.77, *SE* = 7.865, *z* = -0.606, *p* = 0.545
- **4d vs 4a**: *β* = -9.99, *SE* = 4.492, *z* = -2.224, *p* = 0.026
- **SNR**: *β* = 0.95, *SE* = 2.383, *z* = 0.397, *p* = 0.691

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 7.81 | 4.51 | 1.73 | 0.084 | 0.355 | n.s. |
| 4a - 4c | 4.77 | 7.86 | 0.61 | 0.545 | 0.935 | n.s. |
| 4a - 4d | 9.99 | 4.49 | 2.22 | 0.026 | 0.147 | n.s. |
| 4b - 4c | -3.04 | 7.86 | -0.39 | 0.699 | 0.935 | n.s. |
| 4b - 4d | 2.19 | 4.32 | 0.51 | 0.613 | 0.935 | n.s. |
| 4c - 4d | 5.23 | 7.67 | 0.68 | 0.496 | 0.935 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 150.43, BIC = 161.11
- **4b vs 4a**: *β* = -0.33, *SE* = 0.806, *z* = -0.404, *p* = 0.686
- **4c vs 4a**: *β* = -1.32, *SE* = 1.431, *z* = -0.926, *p* = 0.354
- **4d vs 4a**: *β* = 1.02, *SE* = 0.793, *z* = 1.288, *p* = 0.198
- **SNR**: *β* = 2.63, *SE* = 0.473, *z* = 5.547, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 0.33 | 0.81 | 0.40 | 0.686 | 0.746 | n.s. |
| 4a - 4c | 1.33 | 1.43 | 0.93 | 0.354 | 0.731 | n.s. |
| 4a - 4d | -1.02 | 0.79 | -1.29 | 0.198 | 0.586 | n.s. |
| 4b - 4c | 1.00 | 1.47 | 0.68 | 0.496 | 0.746 | n.s. |
| 4b - 4d | -1.35 | 0.77 | -1.75 | 0.081 | 0.397 | n.s. |
| 4c - 4d | -2.35 | 1.45 | -1.62 | 0.104 | 0.424 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 596.70, BIC = 612.13
- **4b vs 4a**: *β* = 4.60, *SE* = 5.429, *z* = 0.847, *p* = 0.397
- **4c vs 4a**: *β* = 2.21, *SE* = 6.474, *z* = 0.342, *p* = 0.732
- **4d vs 4a**: *β* = 1.15, *SE* = 5.595, *z* = 0.206, *p* = 0.837
- **SNR**: *β* = -0.73, *SE* = 1.122, *z* = -0.648, *p* = 0.517

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -4.60 | 5.43 | -0.85 | 0.397 | 0.952 | n.s. |
| 4a - 4c | -2.21 | 6.47 | -0.34 | 0.732 | 0.992 | n.s. |
| 4a - 4d | -1.15 | 5.59 | -0.21 | 0.837 | 0.992 | n.s. |
| 4b - 4c | 2.38 | 6.30 | 0.38 | 0.705 | 0.992 | n.s. |
| 4b - 4d | 3.44 | 5.55 | 0.62 | 0.535 | 0.978 | n.s. |
| 4c - 4d | 1.06 | 6.57 | 0.16 | 0.872 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.35, *p* = 0.114, η²_G = 0.175
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -3.71 | 5 | = 0.083 | -1.21 [-0.82, 0.23] | large | n.s. |
| 4a vs 4c | -0.67 | 5 | = 0.532 | -0.40 [-0.83, 0.71] | small | n.s. |
| 4a vs 4d | -1.86 | 5 | = 0.365 | -0.80 [-0.77, 0.45] | large | n.s. |
| 4b vs 4c | 1.24 | 5 | = 0.423 | 0.70 [-0.53, 0.91] | medium | n.s. |
| 4b vs 4d | 1.21 | 5 | = 0.423 | 0.39 [-0.53, 0.62] | small | n.s. |
| 4c vs 4d | -0.92 | 5 | = 0.479 | -0.34 [-0.73, 0.95] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 356.94, BIC = 372.37
- **4b vs 4a**: *β* = 2.23, *SE* = 0.836, *z* = 2.667, *p* = 0.008
- **4c vs 4a**: *β* = 0.98, *SE* = 1.008, *z* = 0.974, *p* = 0.330
- **4d vs 4a**: *β* = 0.38, *SE* = 0.863, *z* = 0.441, *p* = 0.660
- **SNR**: *β* = -0.76, *SE* = 0.177, *z* = -4.316, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -2.23 | 0.84 | -2.67 | 0.008 | 0.045 | * |
| 4a - 4c | -0.98 | 1.01 | -0.97 | 0.330 | 0.699 | n.s. |
| 4a - 4d | -0.38 | 0.86 | -0.44 | 0.660 | 0.803 | n.s. |
| 4b - 4c | 1.25 | 0.98 | 1.28 | 0.202 | 0.594 | n.s. |
| 4b - 4d | 1.85 | 0.86 | 2.14 | 0.032 | 0.151 | n.s. |
| 4c - 4d | 0.60 | 1.02 | 0.59 | 0.556 | 0.803 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.57, *p* = 0.239, η²_G = 0.172
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -2.22 | 5 | = 0.302 | -1.46 [-0.78, 0.27] | large | n.s. |
| 4a vs 4c | -1.06 | 5 | = 0.509 | -0.32 [-0.86, 0.68] | small | n.s. |
| 4a vs 4d | -0.17 | 5 | = 0.870 | -0.11 [-0.86, 0.37] | negligible | n.s. |
| 4b vs 4c | 1.69 | 5 | = 0.302 | 0.85 [-0.24, 1.29] | large | n.s. |
| 4b vs 4d | 1.96 | 5 | = 0.302 | 0.85 [-0.19, 1.02] | large | n.s. |
| 4c vs 4d | 0.22 | 5 | = 0.870 | 0.13 [-0.58, 1.12] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 384.59, BIC = 397.98
- **4b vs 4a**: *β* = 0.76, *SE* = 4.099, *z* = 0.186, *p* = 0.853
- **4c vs 4a**: *β* = -2.28, *SE* = 4.332, *z* = -0.525, *p* = 0.599
- **4d vs 4a**: *β* = 4.28, *SE* = 4.083, *z* = 1.049, *p* = 0.294
- **SNR**: *β* = -0.65, *SE* = 1.066, *z* = -0.610, *p* = 0.542

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -0.76 | 4.10 | -0.19 | 0.853 | 0.853 | n.s. |
| 4a - 4c | 2.28 | 4.33 | 0.53 | 0.599 | 0.839 | n.s. |
| 4a - 4d | -4.28 | 4.08 | -1.05 | 0.294 | 0.825 | n.s. |
| 4b - 4c | 3.04 | 3.88 | 0.78 | 0.434 | 0.825 | n.s. |
| 4b - 4d | -3.52 | 3.56 | -0.99 | 0.323 | 0.825 | n.s. |
| 4c - 4d | -6.56 | 3.79 | -1.73 | 0.084 | 0.407 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.20, *p* = 0.135, η²_G = 0.808
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | 3.00 | 1 | = 0.307 | 4.02 [-1.15, 1.34] | large | n.s. |
| 4a vs 4c | 1.00 | 1 | = 0.600 | 1.41 [-0.90, 1.21] | large | n.s. |
| 4a vs 4d | 3.00 | 1 | = 0.307 | 1.34 [-1.67, 0.90] | large | n.s. |
| 4b vs 4c | -5.00 | 1 | = 0.307 | -2.24 [-1.54, 0.66] | large | n.s. |
| 4b vs 4d | -3.00 | 1 | = 0.307 | -4.24 [-0.97, 0.59] | large | n.s. |
| 4c vs 4d | -0.33 | 1 | = 0.795 | -0.45 [-1.51, 0.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 215.61, BIC = 229.00
- **4b vs 4a**: *β* = -1.20, *SE* = 0.740, *z* = -1.614, *p* = 0.107
- **4c vs 4a**: *β* = -0.72, *SE* = 0.784, *z* = -0.919, *p* = 0.358
- **4d vs 4a**: *β* = 0.46, *SE* = 0.740, *z* = 0.620, *p* = 0.535
- **SNR**: *β* = 1.11, *SE* = 0.187, *z* = 5.934, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 1.19 | 0.74 | 1.61 | 0.107 | 0.382 | n.s. |
| 4a - 4c | 0.72 | 0.78 | 0.92 | 0.358 | 0.735 | n.s. |
| 4a - 4d | -0.46 | 0.74 | -0.62 | 0.535 | 0.760 | n.s. |
| 4b - 4c | -0.47 | 0.72 | -0.66 | 0.510 | 0.760 | n.s. |
| 4b - 4d | -1.65 | 0.66 | -2.50 | 0.012 | 0.072 | n.s. |
| 4c - 4d | -1.18 | 0.70 | -1.69 | 0.092 | 0.382 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.652, η²_G = 0.379
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -0.03 | 1 | = 0.978 | -0.01 [-0.69, 2.07] | negligible | n.s. |
| 4a vs 4c | -0.07 | 1 | = 0.978 | -0.09 [-1.02, 1.08] | negligible | n.s. |
| 4a vs 4d | -1.45 | 1 | = 0.978 | -2.04 [-1.95, 0.75] | large | n.s. |
| 4b vs 4c | -0.05 | 1 | = 0.978 | -0.07 [-1.06, 1.03] | negligible | n.s. |
| 4b vs 4d | -1.03 | 1 | = 0.978 | -1.38 [-1.42, 0.25] | large | n.s. |
| 4c vs 4d | -2.35 | 1 | = 0.978 | -1.17 [-1.14, 0.44] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 468.24, BIC = 480.40
- **4b vs 4a**: *β* = -11.89, *SE* = 23.075, *z* = -0.515, *p* = 0.606
- **4c vs 4a**: *β* = -23.90, *SE* = 32.630, *z* = -0.732, *p* = 0.464
- **4d vs 4a**: *β* = -21.71, *SE* = 29.209, *z* = -0.743, *p* = 0.457
- **SNR**: *β* = 0.89, *SE* = 9.572, *z* = 0.093, *p* = 0.926

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 11.89 | 23.07 | 0.52 | 0.606 | 0.976 | n.s. |
| 4a - 4c | 23.90 | 32.63 | 0.73 | 0.464 | 0.974 | n.s. |
| 4a - 4d | 21.71 | 29.21 | 0.74 | 0.457 | 0.974 | n.s. |
| 4b - 4c | 12.01 | 36.55 | 0.33 | 0.743 | 0.983 | n.s. |
| 4b - 4d | 9.82 | 33.95 | 0.29 | 0.772 | 0.983 | n.s. |
| 4c - 4d | -2.19 | 27.52 | -0.08 | 0.937 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 196.20, BIC = 208.36
- **4b vs 4a**: *β* = -1.06, *SE* = 0.660, *z* = -1.602, *p* = 0.109
- **4c vs 4a**: *β* = 0.22, *SE* = 0.906, *z* = 0.243, *p* = 0.808
- **4d vs 4a**: *β* = 0.67, *SE* = 0.750, *z* = 0.897, *p* = 0.370
- **SNR**: *β* = 1.35, *SE* = 0.233, *z* = 5.785, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 1.06 | 0.66 | 1.60 | 0.109 | 0.439 | n.s. |
| 4a - 4c | -0.22 | 0.91 | -0.24 | 0.808 | 0.841 | n.s. |
| 4a - 4d | -0.67 | 0.75 | -0.90 | 0.370 | 0.750 | n.s. |
| 4b - 4c | -1.28 | 0.88 | -1.46 | 0.145 | 0.466 | n.s. |
| 4b - 4d | -1.73 | 0.68 | -2.54 | 0.011 | 0.064 | n.s. |
| 4c - 4d | -0.45 | 0.86 | -0.52 | 0.601 | 0.841 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


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
