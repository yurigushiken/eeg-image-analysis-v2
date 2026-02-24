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
| Change by 1 | 24 | 103.83 ms | 9.32 | 1.90 | [92.00, 116.00] |
| Change by 2 | 24 | 106.83 ms | 8.30 | 1.69 | [92.00, 116.00] |
| Change by 3 | 24 | 105.33 ms | 8.64 | 1.76 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | -0.92 µV | 1.13 | 0.23 | [-4.37, 0.55] |
| Change by 2 | 24 | -1.07 µV | 1.15 | 0.23 | [-4.03, 0.97] |
| Change by 3 | 24 | -1.22 µV | 1.49 | 0.30 | [-5.30, 1.76] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 176.83 ms | 18.16 | 3.71 | [144.00, 208.00] |
| Change by 2 | 24 | 174.33 ms | 16.21 | 3.31 | [144.00, 204.00] |
| Change by 3 | 24 | 174.00 ms | 16.64 | 3.40 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | -4.82 µV | 1.97 | 0.40 | [-8.71, -1.09] |
| Change by 2 | 24 | -5.06 µV | 2.01 | 0.41 | [-9.94, -1.00] |
| Change by 3 | 24 | -5.39 µV | 1.98 | 0.40 | [-9.83, -2.09] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 105.83 ms | 9.94 | 2.03 | [92.00, 116.00] |
| Change by 2 | 24 | 107.83 ms | 8.86 | 1.81 | [92.00, 116.00] |
| Change by 3 | 24 | 104.17 ms | 9.02 | 1.84 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 0.99 µV | 1.60 | 0.33 | [-1.28, 4.67] |
| Change by 2 | 24 | 1.12 µV | 1.64 | 0.34 | [-2.38, 4.77] |
| Change by 3 | 24 | 1.38 µV | 1.78 | 0.36 | [-1.28, 6.73] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 487.83 ms | 31.99 | 6.53 | [420.00, 532.00] |
| Change by 2 | 24 | 473.83 ms | 27.76 | 5.67 | [428.00, 532.00] |
| Change by 3 | 24 | 476.50 ms | 34.03 | 6.95 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Change by 1 | 24 | 2.75 µV | 3.20 | 0.65 | [-3.12, 8.78] |
| Change by 2 | 24 | 3.48 µV | 3.13 | 0.64 | [-1.51, 8.36] |
| Change by 3 | 24 | 3.83 µV | 2.96 | 0.60 | [-0.66, 11.10] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 489.74, BIC = 503.40
- **Change by 2 vs Change by 1**: *β* = 2.94, *SE* = 1.377, *z* = 2.133, *p* = 0.033
- **Change by 3 vs Change by 1**: *β* = 1.13, *SE* = 1.418, *z* = 0.796, *p* = 0.426
- **SNR**: *β* = 0.48, *SE* = 0.441, *z* = 1.089, *p* = 0.276

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | -2.94 | 1.38 | -2.13 | 0.033 | 0.096 | n.s. |
| Change by 1 - Change by 3 | -1.13 | 1.42 | -0.80 | 0.426 | 0.426 | n.s. |
| Change by 2 - Change by 3 | 1.81 | 1.41 | 1.29 | 0.198 | 0.356 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.24, *p* = 0.118, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | -2.30 | 23 | = 0.092 | -0.34 [-0.92, -0.03] | small | n.s. |
| Change by 1 vs Change by 3 | -0.93 | 23 | = 0.362 | -0.17 [-0.62, 0.24] | negligible | n.s. |
| Change by 2 vs Change by 3 | 1.14 | 23 | = 0.362 | 0.18 [-0.20, 0.66] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 209.66, BIC = 223.32
- **Change by 2 vs Change by 1**: *β* = -0.13, *SE* = 0.212, *z* = -0.602, *p* = 0.547
- **Change by 3 vs Change by 1**: *β* = -0.19, *SE* = 0.220, *z* = -0.844, *p* = 0.398
- **SNR**: *β* = -0.15, *SE* = 0.076, *z* = -2.019, *p* = 0.043

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 0.13 | 0.21 | 0.60 | 0.547 | 0.795 | n.s. |
| Change by 1 - Change by 3 | 0.19 | 0.22 | 0.84 | 0.398 | 0.782 | n.s. |
| Change by 2 - Change by 3 | 0.06 | 0.22 | 0.27 | 0.790 | 0.795 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.352, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 0.89 | 23 | = 0.545 | 0.13 [-0.24, 0.61] | negligible | n.s. |
| Change by 1 vs Change by 3 | 1.57 | 23 | = 0.392 | 0.23 [-0.11, 0.75] | small | n.s. |
| Change by 2 vs Change by 3 | 0.61 | 23 | = 0.545 | 0.12 [-0.30, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 557.60, BIC = 571.26
- **Change by 2 vs Change by 1**: *β* = -2.58, *SE* = 1.941, *z* = -1.330, *p* = 0.183
- **Change by 3 vs Change by 1**: *β* = -2.93, *SE* = 1.942, *z* = -1.507, *p* = 0.132
- **SNR**: *β* = -0.14, *SE* = 0.203, *z* = -0.700, *p* = 0.484

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 2.58 | 1.94 | 1.33 | 0.183 | 0.346 | n.s. |
| Change by 1 - Change by 3 | 2.93 | 1.94 | 1.51 | 0.132 | 0.346 | n.s. |
| Change by 2 - Change by 3 | 0.34 | 1.94 | 0.18 | 0.859 | 0.859 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.22, *p* = 0.306, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 1.52 | 23 | = 0.354 | 0.15 [-0.12, 0.74] | negligible | n.s. |
| Change by 1 vs Change by 3 | 1.22 | 23 | = 0.354 | 0.16 [-0.18, 0.68] | negligible | n.s. |
| Change by 2 vs Change by 3 | 0.17 | 23 | = 0.864 | 0.02 [-0.39, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 222.60, BIC = 236.26
- **Change by 2 vs Change by 1**: *β* = -0.26, *SE* = 0.175, *z* = -1.478, *p* = 0.139
- **Change by 3 vs Change by 1**: *β* = -0.59, *SE* = 0.175, *z* = -3.366, *p* = 0.001
- **SNR**: *β* = -0.03, *SE* = 0.019, *z* = -1.574, *p* = 0.115

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 0.26 | 0.17 | 1.48 | 0.139 | 0.139 | n.s. |
| Change by 1 - Change by 3 | 0.59 | 0.17 | 3.37 | < .001 | 0.002 | ** |
| Change by 2 - Change by 3 | 0.33 | 0.17 | 1.89 | 0.058 | 0.113 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.09, *p* = 0.010, η²_G = 0.014
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 1.36 | 23 | = 0.188 | 0.12 [-0.15, 0.71] | negligible | n.s. |
| Change by 1 vs Change by 3 | 2.97 | 23 | = 0.021 | 0.29 [0.15, 1.06] | small | * |
| Change by 2 vs Change by 3 | 1.96 | 23 | = 0.093 | 0.16 [-0.04, 0.84] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 507.78, BIC = 521.44
- **Change by 2 vs Change by 1**: *β* = 2.00, *SE* = 1.633, *z* = 1.225, *p* = 0.221
- **Change by 3 vs Change by 1**: *β* = -1.67, *SE* = 1.634, *z* = -1.022, *p* = 0.307
- **SNR**: *β* = 0.01, *SE* = 0.303, *z* = 0.044, *p* = 0.965

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | -2.00 | 1.63 | -1.22 | 0.221 | 0.393 | n.s. |
| Change by 1 - Change by 3 | 1.67 | 1.63 | 1.02 | 0.307 | 0.393 | n.s. |
| Change by 2 - Change by 3 | 3.67 | 1.63 | 2.25 | 0.025 | 0.072 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.43, *p* = 0.100, η²_G = 0.026
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | -1.49 | 23 | = 0.224 | -0.21 [-0.74, 0.13] | small | n.s. |
| Change by 1 vs Change by 3 | 0.85 | 23 | = 0.406 | 0.18 [-0.25, 0.60] | negligible | n.s. |
| Change by 2 vs Change by 3 | 2.25 | 23 | = 0.104 | 0.41 [0.01, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 221.47, BIC = 235.13
- **Change by 2 vs Change by 1**: *β* = 0.13, *SE* = 0.195, *z* = 0.657, *p* = 0.511
- **Change by 3 vs Change by 1**: *β* = 0.37, *SE* = 0.196, *z* = 1.872, *p* = 0.061
- **SNR**: *β* = 0.09, *SE* = 0.042, *z* = 2.016, *p* = 0.044

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | -0.13 | 0.20 | -0.66 | 0.511 | 0.511 | n.s. |
| Change by 1 - Change by 3 | -0.37 | 0.20 | -1.87 | 0.061 | 0.173 | n.s. |
| Change by 2 - Change by 3 | -0.24 | 0.20 | -1.22 | 0.224 | 0.398 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.96, *p* = 0.152, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | -0.59 | 23 | = 0.563 | -0.08 [-0.54, 0.30] | negligible | n.s. |
| Change by 1 vs Change by 3 | -2.52 | 23 | = 0.057 | -0.23 [-0.96, -0.07] | small | n.s. |
| Change by 2 vs Change by 3 | -1.21 | 23 | = 0.360 | -0.15 [-0.67, 0.18] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 701.19, BIC = 714.85
- **Change by 2 vs Change by 1**: *β* = -13.62, *SE* = 7.102, *z* = -1.918, *p* = 0.055
- **Change by 3 vs Change by 1**: *β* = -10.61, *SE* = 7.180, *z* = -1.478, *p* = 0.139
- **SNR**: *β* = 0.27, *SE* = 0.465, *z* = 0.582, *p* = 0.560

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | 13.62 | 7.10 | 1.92 | 0.055 | 0.156 | n.s. |
| Change by 1 - Change by 3 | 10.61 | 7.18 | 1.48 | 0.139 | 0.259 | n.s. |
| Change by 2 - Change by 3 | -3.01 | 7.10 | -0.42 | 0.671 | 0.671 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.07, *p* = 0.137, η²_G = 0.038
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | 2.20 | 23 | = 0.115 | 0.47 [0.01, 0.89] | small | n.s. |
| Change by 1 vs Change by 3 | 1.32 | 23 | = 0.299 | 0.34 [-0.16, 0.70] | small | n.s. |
| Change by 2 vs Change by 3 | -0.39 | 23 | = 0.697 | -0.09 [-0.50, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.39, BIC = 289.05
- **Change by 2 vs Change by 1**: *β* = 0.70, *SE* = 0.234, *z* = 2.988, *p* = 0.003
- **Change by 3 vs Change by 1**: *β* = 1.02, *SE* = 0.238, *z* = 4.272, *p* < .001
- **SNR**: *β* = -0.02, *SE* = 0.019, *z* = -1.219, *p* = 0.223

_Reference condition: **Change by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Change by 1 - Change by 2 | -0.70 | 0.23 | -2.99 | 0.003 | 0.006 | ** |
| Change by 1 - Change by 3 | -1.02 | 0.24 | -4.27 | < .001 | < .001 | *** |
| Change by 2 - Change by 3 | -0.32 | 0.23 | -1.36 | 0.175 | 0.175 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.12, *p* < .001, η²_G = 0.022
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Change by 1 vs Change by 2 | -3.88 | 23 | = 0.001 | -0.23 [-1.28, -0.31] | small | ** |
| Change by 1 vs Change by 3 | -3.99 | 23 | = 0.001 | -0.35 [-1.30, -0.33] | small | ** |
| Change by 2 vs Change by 3 | -1.30 | 23 | = 0.206 | -0.11 [-0.70, 0.16] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - Change by 1 showed greater amplitude than Change by 3 (*d* = 0.29)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.100)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Change by 1 showed smaller amplitude than Change by 2 (*d* = -0.23)
  - Change by 1 showed smaller amplitude than Change by 3 (*d* = -0.35)

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
