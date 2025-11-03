# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:37:03

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| Decrease by 1 (no 1) | 13 | 104.31 ms | 8.24 | 2.29 | [92.00, 116.00] |
| Decrease by 2 (no 1) | 19 | 107.79 ms | 7.71 | 1.77 | [92.00, 116.00] |
| Decrease by 3 (no 1) | 17 | 104.94 ms | 8.07 | 1.96 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 13 | -2.13 µV | 1.29 | 0.36 | [-4.76, -0.33] |
| Decrease by 2 (no 1) | 19 | -2.15 µV | 1.18 | 0.27 | [-6.06, -0.36] |
| Decrease by 3 (no 1) | 17 | -2.60 µV | 1.32 | 0.32 | [-5.62, -0.62] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 177.50 ms | 19.23 | 3.93 | [144.00, 212.00] |
| Decrease by 2 (no 1) | 24 | 173.83 ms | 15.33 | 3.13 | [144.00, 212.00] |
| Decrease by 3 (no 1) | 24 | 176.17 ms | 18.02 | 3.68 | [152.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | -5.51 µV | 2.09 | 0.43 | [-9.73, -1.93] |
| Decrease by 2 (no 1) | 24 | -5.66 µV | 2.23 | 0.45 | [-10.30, -1.75] |
| Decrease by 3 (no 1) | 24 | -6.45 µV | 2.42 | 0.49 | [-10.69, -1.96] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 11 | 110.55 ms | 7.43 | 2.24 | [100.00, 120.00] |
| Decrease by 2 (no 1) | 17 | 113.18 ms | 7.32 | 1.77 | [100.00, 120.00] |
| Decrease by 3 (no 1) | 16 | 111.25 ms | 7.62 | 1.91 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 11 | 2.35 µV | 1.67 | 0.50 | [0.44, 5.74] |
| Decrease by 2 (no 1) | 17 | 2.37 µV | 1.32 | 0.32 | [0.28, 4.48] |
| Decrease by 3 (no 1) | 16 | 2.51 µV | 1.47 | 0.37 | [0.47, 5.70] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 486.32 ms | 30.18 | 6.92 | [440.00, 540.00] |
| Decrease by 2 (no 1) | 19 | 481.26 ms | 33.28 | 7.64 | [440.00, 540.00] |
| Decrease by 3 (no 1) | 19 | 482.95 ms | 33.59 | 7.71 | [432.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 5.25 µV | 2.59 | 0.59 | [1.84, 11.40] |
| Decrease by 2 (no 1) | 19 | 4.93 µV | 2.32 | 0.53 | [1.12, 9.01] |
| Decrease by 3 (no 1) | 19 | 5.63 µV | 3.00 | 0.69 | [1.12, 13.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 344.26, BIC = 355.61
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 2.67, *SE* = 2.313, *z* = 1.155, *p* = 0.248
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.15, *SE* = 2.317, *z* = 0.067, *p* = 0.947
- **SNR**: *β* = 1.06, *SE* = 0.581, *z* = 1.823, *p* = 0.068

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -2.67 | 2.31 | -1.15 | 0.248 | 0.538 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.15 | 2.32 | -0.07 | 0.947 | 0.947 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 2.52 | 2.08 | 1.21 | 0.227 | 0.538 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.54, *p* = 0.592, η²_G = 0.027
- Greenhouse-Geisser corrected: *p* = 0.518 (ε = 0.630)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.00 | 8 | = 1.000 | 0.00 [-0.87, 0.57] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.87 | 8 | = 0.749 | 0.33 [-0.59, 0.75] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.71 | 8 | = 0.749 | 0.31 [-0.32, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 146.60, BIC = 157.95
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.12, *SE* = 0.285, *z* = -0.411, *p* = 0.681
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.69, *SE* = 0.285, *z* = -2.438, *p* = 0.015
- **SNR**: *β* = -0.28, *SE* = 0.074, *z* = -3.798, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.12 | 0.29 | 0.41 | 0.681 | 0.681 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.69 | 0.28 | 2.44 | 0.015 | 0.044 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.58 | 0.26 | 2.25 | 0.024 | 0.048 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.90, *p* = 0.182, η²_G = 0.063
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.44 | 8 | = 0.670 | 0.15 [-0.50, 0.95] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.41 | 8 | = 0.127 | 0.60 [0.08, 1.66] | medium | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.30 | 8 | = 0.347 | 0.43 [-0.18, 1.03] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 592.84, BIC = 606.50
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -3.65, *SE* = 2.828, *z* = -1.291, *p* = 0.197
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -1.28, *SE* = 2.833, *z* = -0.451, *p* = 0.652
- **SNR**: *β* = 0.14, *SE* = 0.445, *z* = 0.319, *p* = 0.750

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 3.65 | 2.83 | 1.29 | 0.197 | 0.482 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.28 | 2.83 | 0.45 | 0.652 | 0.652 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.37 | 2.83 | -0.84 | 0.402 | 0.642 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.82, *p* = 0.447, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.48 | 23 | = 0.458 | 0.21 [-0.13, 0.73] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.44 | 23 | = 0.664 | 0.07 [-0.33, 0.51] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.74 | 23 | = 0.664 | -0.14 [-0.58, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 286.28, BIC = 299.94
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.18, *SE* = 0.346, *z* = -0.509, *p* = 0.611
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -1.02, *SE* = 0.347, *z* = -2.956, *p* = 0.003
- **SNR**: *β* = -0.22, *SE* = 0.053, *z* = -4.148, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.18 | 0.35 | 0.51 | 0.611 | 0.611 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.02 | 0.35 | 2.96 | 0.003 | 0.009 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.85 | 0.35 | 2.45 | 0.014 | 0.028 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.26, *p* = 0.047, η²_G = 0.034
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.39 | 23 | = 0.700 | 0.07 [-0.34, 0.50] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.19 | 23 | = 0.059 | 0.41 [0.00, 0.89] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.18 | 23 | = 0.059 | 0.34 [0.00, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 300.14, BIC = 310.85
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 1.57, *SE* = 2.013, *z* = 0.779, *p* = 0.436
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.08, *SE* = 2.015, *z* = -0.040, *p* = 0.968
- **SNR**: *β* = 0.24, *SE* = 0.296, *z* = 0.796, *p* = 0.426

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -1.57 | 2.01 | -0.78 | 0.436 | 0.714 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.08 | 2.02 | 0.04 | 0.968 | 0.968 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.65 | 1.73 | 0.95 | 0.341 | 0.714 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.68, *p* = 0.222, η²_G = 0.060
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.87 | 7 | = 0.207 | -0.32 [-1.45, 0.23] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.73 | 7 | = 0.487 | 0.28 [-0.60, 0.95] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.67 | 7 | = 0.207 | 0.56 [-0.38, 0.79] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 141.80, BIC = 152.50
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.35, *SE* = 0.332, *z* = 1.070, *p* = 0.285
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.50, *SE* = 0.330, *z* = 1.530, *p* = 0.126
- **SNR**: *β* = 0.18, *SE* = 0.050, *z* = 3.588, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.35 | 0.33 | -1.07 | 0.285 | 0.488 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.50 | 0.33 | -1.53 | 0.126 | 0.333 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.15 | 0.28 | -0.53 | 0.599 | 0.599 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.59, *p* = 0.568, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.34 | 7 | = 0.662 | -0.39 [-1.44, 0.23] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.76 | 7 | = 0.710 | -0.22 [-1.12, 0.46] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.25 | 7 | = 0.808 | 0.11 [-0.61, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 561.63, BIC = 573.89
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -7.15, *SE* = 8.756, *z* = -0.817, *p* = 0.414
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -4.81, *SE* = 8.503, *z* = -0.566, *p* = 0.572
- **SNR**: *β* = -0.41, *SE* = 1.071, *z* = -0.380, *p* = 0.704

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 7.15 | 8.76 | 0.82 | 0.414 | 0.799 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 4.81 | 8.50 | 0.57 | 0.572 | 0.817 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.35 | 8.53 | -0.28 | 0.783 | 0.817 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.582, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.03 | 17 | = 0.546 | 0.28 [-0.26, 0.75] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.93 | 17 | = 0.546 | 0.21 [-0.28, 0.72] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.21 | 17 | = 0.834 | -0.07 [-0.55, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 229.94, BIC = 242.20
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.33, *SE* = 0.406, *z* = 0.801, *p* = 0.423
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.76, *SE* = 0.385, *z* = 1.960, *p* = 0.050
- **SNR**: *β* = 0.26, *SE* = 0.065, *z* = 3.981, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.33 | 0.41 | -0.80 | 0.423 | 0.469 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.75 | 0.39 | -1.96 | 0.050 | 0.143 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.43 | 0.39 | -1.10 | 0.271 | 0.469 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.94, *p* = 0.159, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.61 | 17 | = 0.549 | 0.10 [-0.36, 0.64] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -1.37 | 17 | = 0.284 | -0.20 [-0.83, 0.19] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.78 | 17 | = 0.281 | -0.31 [-0.94, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.047) (no significant pairwise comparisons)

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
