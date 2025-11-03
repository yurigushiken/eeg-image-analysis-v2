# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:32:19

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
| Decrease by 1 (no 1) | 11 | 103.64 ms | 12.06 | 3.64 | [92.00, 116.00] |
| Decrease by 2 (no 1) | 5 | 106.40 ms | 13.15 | 5.88 | [92.00, 116.00] |
| Decrease by 3 (no 1) | 7 | 106.29 ms | 10.29 | 3.89 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 11 | 1.68 µV | 0.71 | 0.21 | [0.56, 2.90] |
| Decrease by 2 (no 1) | 5 | 2.79 µV | 1.31 | 0.58 | [1.17, 4.05] |
| Decrease by 3 (no 1) | 7 | 2.15 µV | 0.80 | 0.30 | [0.86, 3.19] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 174.33 ms | 17.81 | 3.63 | [144.00, 212.00] |
| Decrease by 2 (no 1) | 24 | 173.17 ms | 16.19 | 3.31 | [144.00, 212.00] |
| Decrease by 3 (no 1) | 24 | 175.33 ms | 17.68 | 3.61 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | -5.36 µV | 2.03 | 0.41 | [-9.50, -2.05] |
| Decrease by 2 (no 1) | 24 | -5.48 µV | 2.17 | 0.44 | [-9.98, -1.47] |
| Decrease by 3 (no 1) | 24 | -6.25 µV | 2.42 | 0.49 | [-10.38, -1.96] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 10 | 112.80 ms | 6.20 | 1.96 | [104.00, 120.00] |
| Decrease by 2 (no 1) | 17 | 114.59 ms | 6.32 | 1.53 | [100.00, 120.00] |
| Decrease by 3 (no 1) | 16 | 112.25 ms | 7.66 | 1.91 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 10 | 2.43 µV | 1.98 | 0.62 | [0.45, 5.95] |
| Decrease by 2 (no 1) | 17 | 2.30 µV | 1.40 | 0.34 | [0.41, 4.83] |
| Decrease by 3 (no 1) | 16 | 2.52 µV | 1.54 | 0.38 | [1.00, 6.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 485.89 ms | 28.14 | 6.46 | [440.00, 532.00] |
| Decrease by 2 (no 1) | 18 | 478.44 ms | 29.59 | 6.97 | [440.00, 536.00] |
| Decrease by 3 (no 1) | 19 | 475.79 ms | 30.24 | 6.94 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 4.48 µV | 2.50 | 0.57 | [1.07, 9.46] |
| Decrease by 2 (no 1) | 18 | 4.91 µV | 2.22 | 0.52 | [2.16, 8.89] |
| Decrease by 3 (no 1) | 19 | 5.43 µV | 3.11 | 0.71 | [1.12, 13.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 175.40, BIC = 182.21
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 3.11, *SE* = 2.692, *z* = 1.154, *p* = 0.249
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 3.88, *SE* = 2.233, *z* = 1.736, *p* = 0.083
- **SNR**: *β* = -0.92, *SE* = 0.613, *z* = -1.505, *p* = 0.132

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -3.11 | 2.69 | -1.15 | 0.249 | 0.436 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -3.88 | 2.23 | -1.74 | 0.083 | 0.228 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.77 | 2.87 | -0.27 | 0.788 | 0.788 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 62.02, BIC = 68.83
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 1.08, *SE* = 0.459, *z* = 2.350, *p* = 0.019
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.62, *SE* = 0.353, *z* = 1.748, *p* = 0.080
- **SNR**: *β* = 0.23, *SE* = 0.096, *z* = 2.437, *p* = 0.015

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -1.08 | 0.46 | -2.35 | 0.019 | 0.055 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.62 | 0.35 | -1.75 | 0.080 | 0.154 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.46 | 0.51 | 0.90 | 0.368 | 0.368 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 589.48, BIC = 603.14
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -1.19, *SE* = 2.771, *z* = -0.428, *p* = 0.669
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.87, *SE* = 2.822, *z* = 0.307, *p* = 0.759
- **SNR**: *β* = -0.10, *SE* = 0.392, *z* = -0.248, *p* = 0.804

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 1.19 | 2.77 | 0.43 | 0.669 | 0.890 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.87 | 2.82 | -0.31 | 0.759 | 0.890 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.05 | 2.81 | -0.73 | 0.465 | 0.847 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.747, η²_G = 0.003
- Greenhouse-Geisser corrected: *p* = 0.658 (ε = 0.670)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.75 | 23 | = 0.762 | 0.07 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.30 | 23 | = 0.768 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.67 | 23 | = 0.762 | -0.13 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.84, BIC = 294.50
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.14, *SE* = 0.324, *z* = -0.448, *p* = 0.654
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -1.09, *SE* = 0.330, *z* = -3.306, *p* = 0.001
- **SNR**: *β* = -0.15, *SE* = 0.046, *z* = -3.325, *p* = 0.001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.15 | 0.32 | 0.45 | 0.654 | 0.654 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.09 | 0.33 | 3.31 | < .001 | 0.003 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.95 | 0.33 | 2.88 | 0.004 | 0.008 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.72, *p* = 0.032, η²_G = 0.032
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.33 | 23 | = 0.741 | 0.06 [-0.35, 0.49] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.30 | 23 | = 0.047 | 0.39 [0.02, 0.91] | small | * |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.38 | 23 | = 0.047 | 0.33 [0.04, 0.93] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 267.48, BIC = 278.05
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 2.10, *SE* = 1.157, *z* = 1.815, *p* = 0.069
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.22, *SE* = 1.195, *z* = 0.181, *p* = 0.856
- **SNR**: *β* = -0.15, *SE* = 0.184, *z* = -0.834, *p* = 0.405

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -2.10 | 1.16 | -1.82 | 0.069 | 0.145 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.22 | 1.20 | -0.18 | 0.856 | 0.856 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.88 | 0.97 | 1.95 | 0.051 | 0.145 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.54, *p* = 0.248, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.53 | 7 | = 0.427 | -0.32 [-1.47, 0.21] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.55 | 7 | = 0.598 | -0.07 [-1.04, 0.65] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.16 | 7 | = 0.427 | 0.23 [-0.21, 0.99] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 140.10, BIC = 150.67
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.38, *SE* = 0.345, *z* = 1.093, *p* = 0.274
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.61, *SE* = 0.354, *z* = 1.724, *p* = 0.085
- **SNR**: *β* = 0.21, *SE* = 0.055, *z* = 3.836, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.38 | 0.35 | -1.09 | 0.274 | 0.473 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.61 | 0.35 | -1.72 | 0.085 | 0.233 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.23 | 0.29 | -0.80 | 0.423 | 0.473 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.711, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.75 | 7 | = 0.714 | -0.21 [-1.11, 0.47] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.84 | 7 | = 0.714 | -0.19 [-1.15, 0.56] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.01 | 7 | = 0.992 | -0.00 [-0.69, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 543.92, BIC = 556.07
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -7.45, *SE* = 8.459, *z* = -0.880, *p* = 0.379
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -10.95, *SE* = 8.247, *z* = -1.328, *p* = 0.184
- **SNR**: *β* = -0.00, *SE* = 0.960, *z* = -0.001, *p* = 0.999

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 7.44 | 8.46 | 0.88 | 0.379 | 0.614 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 10.95 | 8.25 | 1.33 | 0.184 | 0.457 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 3.50 | 8.32 | 0.42 | 0.674 | 0.674 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.258, η²_G = 0.046
- Greenhouse-Geisser corrected: *p* = 0.258 (ε = 0.720)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.74 | 16 | = 0.254 | 0.34 [-0.11, 0.96] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 1.44 | 16 | = 0.254 | 0.53 [-0.17, 0.85] | medium | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.52 | 16 | = 0.612 | 0.18 [-0.39, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 229.11, BIC = 241.27
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.85, *SE* = 0.417, *z* = 2.046, *p* = 0.041
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 1.31, *SE* = 0.398, *z* = 3.294, *p* = 0.001
- **SNR**: *β* = 0.24, *SE* = 0.063, *z* = 3.889, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.85 | 0.42 | -2.05 | 0.041 | 0.080 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.31 | 0.40 | -3.29 | < .001 | 0.003 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.46 | 0.40 | -1.13 | 0.260 | 0.260 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.00, *p* = 0.064, η²_G = 0.031
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.03 | 16 | = 0.318 | -0.16 [-0.77, 0.27] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -2.18 | 16 | = 0.134 | -0.39 [-1.08, -0.01] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.49 | 16 | = 0.233 | -0.27 [-0.89, 0.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.032). Post-hoc tests revealed:
  - Decrease by 1 (no 1) showed greater amplitude than Decrease by 3 (no 1) (*d* = 0.39)
  - Decrease by 2 (no 1) showed greater amplitude than Decrease by 3 (no 1) (*d* = 0.33)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.064)

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
