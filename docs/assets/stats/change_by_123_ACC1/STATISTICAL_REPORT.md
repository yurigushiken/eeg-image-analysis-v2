# Statistical Analysis Report: tables

**Generated:** 2026-02-23 20:23:05

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
| Change by 1 | 24 | 104.00 ms | 9.29 | 1.90 | [92.00, 116.00] |
| Change by 2 | 24 | 104.50 ms | 9.31 | 1.90 | [92.00, 116.00] |
| Change by 3 | 24 | 103.33 ms | 9.03 | 1.84 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | -0.98 µV | 1.17 | 0.24 | [-4.18, 0.62] |
| Change by 2 | 24 | -1.18 µV | 1.11 | 0.23 | [-4.07, 1.09] |
| Change by 3 | 24 | -1.32 µV | 1.34 | 0.27 | [-5.00, 1.56] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 175.67 ms | 19.23 | 3.93 | [144.00, 208.00] |
| Change by 2 | 24 | 174.00 ms | 16.13 | 3.29 | [144.00, 204.00] |
| Change by 3 | 24 | 173.67 ms | 16.97 | 3.46 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | -4.87 µV | 1.97 | 0.40 | [-8.75, -1.00] |
| Change by 2 | 24 | -5.21 µV | 2.05 | 0.42 | [-10.24, -1.34] |
| Change by 3 | 24 | -5.49 µV | 1.99 | 0.41 | [-9.77, -2.42] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 108.17 ms | 11.28 | 2.30 | [92.00, 120.00] |
| Change by 2 | 24 | 107.83 ms | 10.78 | 2.20 | [92.00, 120.00] |
| Change by 3 | 24 | 106.00 ms | 10.68 | 2.18 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 1.11 µV | 1.65 | 0.34 | [-1.26, 4.75] |
| Change by 2 | 24 | 1.30 µV | 1.67 | 0.34 | [-2.34, 4.85] |
| Change by 3 | 24 | 1.56 µV | 1.79 | 0.37 | [-1.25, 6.63] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 493.00 ms | 33.74 | 6.89 | [420.00, 536.00] |
| Change by 2 | 24 | 481.50 ms | 32.04 | 6.54 | [428.00, 536.00] |
| Change by 3 | 24 | 476.67 ms | 34.96 | 7.14 | [420.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 3.42 µV | 3.29 | 0.67 | [-2.69, 9.94] |
| Change by 2 | 24 | 3.77 µV | 3.09 | 0.63 | [-1.10, 8.80] |
| Change by 3 | 24 | 4.03 µV | 2.98 | 0.61 | [-0.37, 11.25] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 516.13, BIC = 529.79
- **Change by 2 vs Change by 1**: *β* = 0.36, *SE* = 1.865, *z* = 0.195, *p* = 0.845
- **Change by 3 vs Change by 1**: *β* = -0.87, *SE* = 1.882, *z* = -0.461, *p* = 0.645
- **SNR**: *β* = 0.29, *SE* = 0.498, *z* = 0.589, *p* = 0.556

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | -0.36 | 1.87 | -0.20 | 0.845 | 0.880 | n.s. |
| Change by 1 - Change by 3 | 0.87 | 1.88 | 0.46 | 0.645 | 0.880 | n.s. |
| Change by 2 - Change by 3 | 1.23 | 1.85 | 0.66 | 0.506 | 0.880 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.19, *p* = 0.825, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | -0.26 | 23 | = 0.799 | -0.05 [-0.48, 0.37] | negligible | n.s. |
| Change by 1 vs Change by 3 | 0.35 | 23 | = 0.799 | 0.07 [-0.35, 0.49] | negligible | n.s. |
| Change by 2 vs Change by 3 | 0.65 | 23 | = 0.799 | 0.13 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 210.69, BIC = 224.35
- **Change by 2 vs Change by 1**: *β* = -0.15, *SE* = 0.216, *z* = -0.714, *p* = 0.475
- **Change by 3 vs Change by 1**: *β* = -0.28, *SE* = 0.219, *z* = -1.285, *p* = 0.199
- **SNR**: *β* = -0.09, *SE* = 0.070, *z* = -1.215, *p* = 0.225

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 0.15 | 0.22 | 0.71 | 0.475 | 0.724 | n.s. |
| Change by 1 - Change by 3 | 0.28 | 0.22 | 1.28 | 0.199 | 0.486 | n.s. |
| Change by 2 - Change by 3 | 0.13 | 0.21 | 0.59 | 0.553 | 0.724 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.30, *p* = 0.282, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 1.18 | 23 | = 0.375 | 0.17 [-0.19, 0.67] | negligible | n.s. |
| Change by 1 vs Change by 3 | 1.52 | 23 | = 0.375 | 0.27 [-0.12, 0.74] | small | n.s. |
| Change by 2 vs Change by 3 | 0.61 | 23 | = 0.548 | 0.12 [-0.30, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 564.78, BIC = 578.44
- **Change by 2 vs Change by 1**: *β* = -1.89, *SE* = 2.100, *z* = -0.900, *p* = 0.368
- **Change by 3 vs Change by 1**: *β* = -2.04, *SE* = 2.059, *z* = -0.992, *p* = 0.321
- **SNR**: *β* = 0.08, *SE* = 0.151, *z* = 0.535, *p* = 0.593

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 1.89 | 2.10 | 0.90 | 0.368 | 0.687 | n.s. |
| Change by 1 - Change by 3 | 2.04 | 2.06 | 0.99 | 0.321 | 0.687 | n.s. |
| Change by 2 - Change by 3 | 0.15 | 2.09 | 0.07 | 0.942 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.51, *p* = 0.601, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 0.93 | 23 | = 0.648 | 0.09 [-0.24, 0.62] | negligible | n.s. |
| Change by 1 vs Change by 3 | 0.80 | 23 | = 0.648 | 0.11 [-0.26, 0.59] | negligible | n.s. |
| Change by 2 vs Change by 3 | 0.17 | 23 | = 0.868 | 0.02 [-0.39, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 236.54, BIC = 250.20
- **Change by 2 vs Change by 1**: *β* = -0.32, *SE* = 0.202, *z* = -1.596, *p* = 0.111
- **Change by 3 vs Change by 1**: *β* = -0.62, *SE* = 0.198, *z* = -3.132, *p* = 0.002
- **SNR**: *β* = -0.01, *SE* = 0.015, *z* = -0.353, *p* = 0.724

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 0.32 | 0.20 | 1.60 | 0.111 | 0.209 | n.s. |
| Change by 1 - Change by 3 | 0.62 | 0.20 | 3.13 | 0.002 | 0.005 | ** |
| Change by 2 - Change by 3 | 0.30 | 0.20 | 1.48 | 0.138 | 0.209 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.78, *p* = 0.013, η²_G = 0.017
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 1.71 | 23 | = 0.101 | 0.17 [-0.09, 0.78] | negligible | n.s. |
| Change by 1 vs Change by 3 | 2.64 | 23 | = 0.044 | 0.32 [0.09, 0.99] | small | * |
| Change by 2 vs Change by 3 | 1.73 | 23 | = 0.101 | 0.14 [-0.08, 0.79] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 538.44, BIC = 552.10
- **Change by 2 vs Change by 1**: *β* = -0.33, *SE* = 2.108, *z* = -0.155, *p* = 0.877
- **Change by 3 vs Change by 1**: *β* = -2.18, *SE* = 2.109, *z* = -1.033, *p* = 0.302
- **SNR**: *β* = -0.07, *SE* = 0.397, *z* = -0.165, *p* = 0.869

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 0.33 | 2.11 | 0.15 | 0.877 | 0.877 | n.s. |
| Change by 1 - Change by 3 | 2.18 | 2.11 | 1.03 | 0.302 | 0.660 | n.s. |
| Change by 2 - Change by 3 | 1.85 | 2.11 | 0.88 | 0.380 | 0.660 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.58, *p* = 0.561, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 0.16 | 23 | = 0.873 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| Change by 1 vs Change by 3 | 0.92 | 23 | = 0.568 | 0.20 [-0.24, 0.61] | negligible | n.s. |
| Change by 2 vs Change by 3 | 0.90 | 23 | = 0.568 | 0.17 [-0.24, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 226.44, BIC = 240.10
- **Change by 2 vs Change by 1**: *β* = 0.18, *SE* = 0.196, *z* = 0.915, *p* = 0.360
- **Change by 3 vs Change by 1**: *β* = 0.45, *SE* = 0.196, *z* = 2.271, *p* = 0.023
- **SNR**: *β* = 0.02, *SE* = 0.043, *z* = 0.556, *p* = 0.578

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | -0.18 | 0.20 | -0.91 | 0.360 | 0.360 | n.s. |
| Change by 1 - Change by 3 | -0.45 | 0.20 | -2.27 | 0.023 | 0.068 | n.s. |
| Change by 2 - Change by 3 | -0.27 | 0.20 | -1.35 | 0.176 | 0.320 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.49, *p* = 0.094, η²_G = 0.012
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | -0.91 | 23 | = 0.372 | -0.11 [-0.61, 0.24] | negligible | n.s. |
| Change by 1 vs Change by 3 | -2.51 | 23 | = 0.058 | -0.26 [-0.96, -0.06] | small | n.s. |
| Change by 2 vs Change by 3 | -1.19 | 23 | = 0.370 | -0.15 [-0.67, 0.19] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 702.14, BIC = 715.80
- **Change by 2 vs Change by 1**: *β* = -11.03, *SE* = 6.591, *z* = -1.673, *p* = 0.094
- **Change by 3 vs Change by 1**: *β* = -14.80, *SE* = 6.704, *z* = -2.208, *p* = 0.027
- **SNR**: *β* = 0.57, *SE* = 0.481, *z* = 1.191, *p* = 0.234

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 11.03 | 6.59 | 1.67 | 0.094 | 0.180 | n.s. |
| Change by 1 - Change by 3 | 14.80 | 6.70 | 2.21 | 0.027 | 0.080 | n.s. |
| Change by 2 - Change by 3 | 3.77 | 6.64 | 0.57 | 0.570 | 0.570 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.93, *p* = 0.064, η²_G = 0.042
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 1.99 | 23 | = 0.088 | 0.35 [-0.03, 0.85] | small | n.s. |
| Change by 1 vs Change by 3 | 2.09 | 23 | = 0.088 | 0.48 [-0.01, 0.87] | small | n.s. |
| Change by 2 vs Change by 3 | 0.68 | 23 | = 0.501 | 0.14 [-0.28, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 279.41, BIC = 293.07
- **Change by 2 vs Change by 1**: *β* = 0.34, *SE* = 0.243, *z* = 1.390, *p* = 0.165
- **Change by 3 vs Change by 1**: *β* = 0.56, *SE* = 0.248, *z* = 2.246, *p* = 0.025
- **SNR**: *β* = -0.02, *SE* = 0.020, *z* = -0.933, *p* = 0.351

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | -0.34 | 0.24 | -1.39 | 0.165 | 0.302 | n.s. |
| Change by 1 - Change by 3 | -0.56 | 0.25 | -2.25 | 0.025 | 0.072 | n.s. |
| Change by 2 - Change by 3 | -0.22 | 0.24 | -0.90 | 0.369 | 0.369 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.92, *p* = 0.064, η²_G = 0.007
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | -1.55 | 23 | = 0.203 | -0.11 [-0.75, 0.12] | negligible | n.s. |
| Change by 1 vs Change by 3 | -2.31 | 23 | = 0.091 | -0.19 [-0.92, -0.03] | negligible | n.s. |
| Change by 2 vs Change by 3 | -0.96 | 23 | = 0.346 | -0.08 [-0.62, 0.23] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.013). Post-hoc tests revealed:
  - Change by 1 showed greater amplitude than Change by 3 (*d* = 0.32)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.094)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.064)
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

#### Amplitude

### 5.3 P1 Component

#### Latency

#### Amplitude

### 5.4 P3b Component

#### Latency

#### Amplitude

---

## 6. Methods Summary (for Publication)

### ERP Measurement

ERP components were measured using a collapsed localizer approach, where component peaks were identified from the grand average of all conditions combined to avoid circular analysis (Luck & Gaspelin, 2017). Measurement windows were defined as the full-width at half-maximum (FWHM) around each peak. Component latency was quantified using the 50% fractional area latency (FAL), which represents the time point at which the cumulative area under the curve reaches 50% of its total value within the measurement window. This metric provides a robust estimate of component timing with lower measurement error than peak latency (Kiesel et al., 2008). Mean amplitude was computed as the average voltage within the FWHM window across predefined regions of interest (ROI).

### Statistical Analysis

Linear mixed-effects models (LMM) with random intercepts for subjects were used as the primary analysis, as they optimally handle missing data via maximum likelihood estimation (Baayen et al., 2008). 
For comparison with traditional approaches, repeated-measures ANOVA and pairwise t-tests were also performed on complete cases; however, power was substantially reduced by listwise deletion. Therefore, LMM results are emphasized in interpretation.

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.4
- MNE-Python 1.9.0
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
