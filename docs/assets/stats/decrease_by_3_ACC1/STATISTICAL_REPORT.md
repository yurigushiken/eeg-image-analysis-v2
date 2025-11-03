# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:38:22

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
| 4 to 1 | 16 | 112.50 ms | 9.89 | 2.47 | [88.00, 120.00] |
| 5 to 2 | 17 | 104.94 ms | 10.25 | 2.49 | [88.00, 120.00] |
| 6 to 3 | 16 | 102.00 ms | 10.63 | 2.66 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 16 | -3.86 µV | 2.37 | 0.59 | [-8.54, -0.87] |
| 5 to 2 | 17 | -3.38 µV | 1.71 | 0.41 | [-6.65, -0.53] |
| 6 to 3 | 16 | -2.87 µV | 1.17 | 0.29 | [-5.28, -1.17] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 188.00 ms | 14.49 | 3.51 | [168.00, 216.00] |
| 5 to 2 | 24 | 174.50 ms | 19.12 | 3.90 | [148.00, 220.00] |
| 6 to 3 | 24 | 176.50 ms | 16.61 | 3.39 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | -4.54 µV | 1.93 | 0.47 | [-9.44, -1.54] |
| 5 to 2 | 24 | -7.01 µV | 3.01 | 0.61 | [-11.82, -1.41] |
| 6 to 3 | 24 | -6.55 µV | 2.33 | 0.48 | [-11.28, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 16 | 119.75 ms | 7.79 | 1.95 | [108.00, 128.00] |
| 5 to 2 | 15 | 114.67 ms | 9.76 | 2.52 | [100.00, 128.00] |
| 6 to 3 | 13 | 112.31 ms | 10.89 | 3.02 | [96.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 16 | 5.76 µV | 2.68 | 0.67 | [2.46, 13.38] |
| 5 to 2 | 15 | 3.31 µV | 1.58 | 0.41 | [0.75, 6.20] |
| 6 to 3 | 13 | 3.26 µV | 2.25 | 0.62 | [0.16, 7.81] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 474.60 ms | 45.61 | 10.20 | [384.00, 528.00] |
| 5 to 2 | 17 | 466.12 ms | 40.50 | 9.82 | [392.00, 524.00] |
| 6 to 3 | 19 | 459.37 ms | 33.26 | 7.63 | [396.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 6.74 µV | 3.02 | 0.68 | [2.92, 12.03] |
| 5 to 2 | 17 | 6.16 µV | 2.77 | 0.67 | [3.00, 13.53] |
| 6 to 3 | 19 | 7.03 µV | 2.89 | 0.66 | [3.79, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 7.72 | 3.80 | 2.03 | 0.042 | 0.082 | n.s. |
| 4 to 1 - 6 to 3 | 10.90 | 3.77 | 2.89 | 0.004 | 0.011 | * |
| 5 to 2 - 6 to 3 | 3.17 | 3.53 | 0.90 | 0.368 | 0.368 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.35, *p* = 0.017, η²_G = 0.335
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 3.83 | 8 | = 0.015 | 1.50 [0.00, 1.42] | large | * |
| 4 to 1 vs 6 to 3 | 3.09 | 8 | = 0.022 | 1.58 [0.18, 1.71] | large | * |
| 5 to 2 vs 6 to 3 | 0.08 | 8 | = 0.935 | 0.05 [-0.62, 0.66] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 169.57, BIC = 180.92
- **5 to 2 vs 4 to 1**: *β* = 0.35, *SE* = 0.363, *z* = 0.958, *p* = 0.338
- **6 to 3 vs 4 to 1**: *β* = 0.35, *SE* = 0.379, *z* = 0.927, *p* = 0.354
- **SNR**: *β* = -0.95, *SE* = 0.136, *z* = -6.991, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | -0.35 | 0.36 | -0.96 | 0.338 | 0.710 | n.s. |
| 4 to 1 - 6 to 3 | -0.35 | 0.38 | -0.93 | 0.354 | 0.710 | n.s. |
| 5 to 2 - 6 to 3 | -0.00 | 0.36 | -0.01 | 0.992 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.95, *p* = 0.040, η²_G = 0.191
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | -1.89 | 8 | = 0.142 | -0.82 [-1.16, 0.19] | large | n.s. |
| 4 to 1 vs 6 to 3 | -3.50 | 8 | = 0.024 | -1.02 [-1.52, -0.06] | large | * |
| 5 to 2 vs 6 to 3 | -0.31 | 8 | = 0.766 | -0.14 [-0.80, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 552.46, BIC = 565.51
- **5 to 2 vs 4 to 1**: *β* = -13.45, *SE* = 4.471, *z* = -3.008, *p* = 0.003
- **6 to 3 vs 4 to 1**: *β* = -11.43, *SE* = 4.419, *z* = -2.587, *p* = 0.010
- **SNR**: *β* = 0.10, *SE* = 0.717, *z* = 0.139, *p* = 0.889

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 13.45 | 4.47 | 3.01 | 0.003 | 0.008 | ** |
| 4 to 1 - 6 to 3 | 11.43 | 4.42 | 2.59 | 0.010 | 0.019 | * |
| 5 to 2 - 6 to 3 | -2.02 | 3.66 | -0.55 | 0.581 | 0.581 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.79, *p* = 0.015, η²_G = 0.100
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.47 | 16 | = 0.038 | 0.77 [0.04, 1.16] | medium | * |
| 4 to 1 vs 6 to 3 | 2.51 | 16 | = 0.038 | 0.63 [0.05, 1.17] | medium | * |
| 5 to 2 vs 6 to 3 | -0.72 | 16 | = 0.482 | -0.15 [-0.55, 0.30] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 287.22, BIC = 300.27
- **5 to 2 vs 4 to 1**: *β* = -2.13, *SE* = 0.559, *z* = -3.805, *p* < .001
- **6 to 3 vs 4 to 1**: *β* = -1.74, *SE* = 0.552, *z* = -3.145, *p* = 0.002
- **SNR**: *β* = -0.33, *SE* = 0.089, *z* = -3.714, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 2.13 | 0.56 | 3.81 | < .001 | < .001 | *** |
| 4 to 1 - 6 to 3 | 1.74 | 0.55 | 3.14 | 0.002 | 0.003 | ** |
| 5 to 2 - 6 to 3 | -0.39 | 0.45 | -0.87 | 0.382 | 0.382 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 17.18, *p* < .001, η²_G = 0.316
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 5.41 | 16 | < .001 | 1.54 [0.61, 2.01] | large | *** |
| 4 to 1 vs 6 to 3 | 3.52 | 16 | = 0.004 | 1.22 [0.25, 1.45] | large | ** |
| 5 to 2 vs 6 to 3 | -2.15 | 16 | = 0.047 | -0.41 [-0.66, 0.20] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 329.51, BIC = 340.22
- **5 to 2 vs 4 to 1**: *β* = -6.08, *SE* = 3.130, *z* = -1.942, *p* = 0.052
- **6 to 3 vs 4 to 1**: *β* = -6.69, *SE* = 3.395, *z* = -1.970, *p* = 0.049
- **SNR**: *β* = 0.26, *SE* = 0.749, *z* = 0.350, *p* = 0.727

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 6.08 | 3.13 | 1.94 | 0.052 | 0.139 | n.s. |
| 4 to 1 - 6 to 3 | 6.69 | 3.39 | 1.97 | 0.049 | 0.139 | n.s. |
| 5 to 2 - 6 to 3 | 0.61 | 3.24 | 0.19 | 0.851 | 0.851 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.68, *p* = 0.016, η²_G = 0.299
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 6.52 | 7 | < .001 | 1.65 [0.21, 1.88] | large | *** |
| 4 to 1 vs 6 to 3 | 2.20 | 7 | = 0.096 | 1.14 [-0.02, 1.62] | large | n.s. |
| 5 to 2 vs 6 to 3 | -0.43 | 7 | = 0.677 | -0.20 [-1.03, 0.43] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 184.22, BIC = 194.92
- **5 to 2 vs 4 to 1**: *β* = -1.46, *SE* = 0.593, *z* = -2.465, *p* = 0.014
- **6 to 3 vs 4 to 1**: *β* = -1.14, *SE* = 0.643, *z* = -1.769, *p* = 0.077
- **SNR**: *β* = 0.62, *SE* = 0.135, *z* = 4.575, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.46 | 0.59 | 2.47 | 0.014 | 0.040 | * |
| 4 to 1 - 6 to 3 | 1.14 | 0.64 | 1.77 | 0.077 | 0.148 | n.s. |
| 5 to 2 - 6 to 3 | -0.32 | 0.58 | -0.56 | 0.577 | 0.577 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.69, *p* = 0.009, η²_G = 0.291
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.66 | 7 | = 0.049 | 1.26 [0.11, 1.70] | large | * |
| 4 to 1 vs 6 to 3 | 3.60 | 7 | = 0.026 | 1.12 [0.04, 1.72] | large | * |
| 5 to 2 vs 6 to 3 | -0.01 | 7 | = 0.992 | -0.00 [-0.71, 0.72] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 578.41, BIC = 590.57
- **5 to 2 vs 4 to 1**: *β* = -10.57, *SE* = 11.206, *z* = -0.944, *p* = 0.345
- **6 to 3 vs 4 to 1**: *β* = -14.45, *SE* = 11.027, *z* = -1.310, *p* = 0.190
- **SNR**: *β* = 0.02, *SE* = 1.062, *z* = 0.019, *p* = 0.985

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 10.57 | 11.21 | 0.94 | 0.345 | 0.571 | n.s. |
| 4 to 1 - 6 to 3 | 14.45 | 11.03 | 1.31 | 0.190 | 0.469 | n.s. |
| 5 to 2 - 6 to 3 | 3.87 | 11.35 | 0.34 | 0.733 | 0.733 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.356, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.20 | 14 | = 0.383 | 0.30 [-0.31, 0.77] | small | n.s. |
| 4 to 1 vs 6 to 3 | 1.19 | 14 | = 0.383 | 0.41 [-0.19, 0.91] | small | n.s. |
| 5 to 2 vs 6 to 3 | 0.24 | 14 | = 0.810 | 0.07 [-0.63, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 250.41, BIC = 262.56
- **5 to 2 vs 4 to 1**: *β* = -0.54, *SE* = 0.523, *z* = -1.040, *p* = 0.298
- **6 to 3 vs 4 to 1**: *β* = 0.53, *SE* = 0.522, *z* = 1.022, *p* = 0.307
- **SNR**: *β* = 0.25, *SE* = 0.056, *z* = 4.422, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.54 | 0.52 | 1.04 | 0.298 | 0.507 | n.s. |
| 4 to 1 - 6 to 3 | -0.53 | 0.52 | -1.02 | 0.307 | 0.507 | n.s. |
| 5 to 2 - 6 to 3 | -1.08 | 0.52 | -2.07 | 0.039 | 0.112 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.353, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 0.91 | 14 | = 0.568 | 0.24 [-0.28, 0.80] | small | n.s. |
| 4 to 1 vs 6 to 3 | -0.29 | 14 | = 0.774 | -0.06 [-0.50, 0.56] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -1.81 | 14 | = 0.273 | -0.32 [-1.10, 0.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.017). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 5 to 2 (*d* = 1.50)
  - 4 to 1 showed greater latency than 6 to 3 (*d* = 1.58)
**Fz amplitude:** Significant main effect of condition (*p* = 0.040). Post-hoc tests revealed:
  - 4 to 1 showed smaller amplitude than 6 to 3 (*d* = -1.02)
**N1 latency:** Significant main effect of condition (*p* = 0.015). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 5 to 2 (*d* = 0.77)
  - 4 to 1 showed greater latency than 6 to 3 (*d* = 0.63)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 1.54)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.22)
  - 5 to 2 showed smaller amplitude than 6 to 3 (*d* = -0.41)
**P1 latency:** Significant main effect of condition (*p* = 0.016). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 5 to 2 (*d* = 1.65)
**P1 amplitude:** Significant main effect of condition (*p* = 0.009). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 1.26)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.12)

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
