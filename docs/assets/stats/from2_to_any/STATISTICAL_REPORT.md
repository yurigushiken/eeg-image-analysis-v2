# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:39:43

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
| 2 to 1 | 17 | 108.47 ms | 8.82 | 2.14 | [92.00, 116.00] |
| 2 to 3 | 18 | 105.11 ms | 9.78 | 2.30 | [92.00, 116.00] |
| 2 to 4 | 16 | 104.25 ms | 8.94 | 2.24 | [92.00, 116.00] |
| 2 to 5 | 13 | 104.31 ms | 7.74 | 2.15 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | -2.75 µV | 1.55 | 0.38 | [-6.41, -0.16] |
| 2 to 3 | 18 | -2.17 µV | 1.54 | 0.36 | [-5.76, -0.37] |
| 2 to 4 | 16 | -2.72 µV | 1.57 | 0.39 | [-6.14, -0.67] |
| 2 to 5 | 13 | -1.88 µV | 2.77 | 0.77 | [-10.84, -0.69] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 15 | 178.93 ms | 10.42 | 2.69 | [160.00, 200.00] |
| 2 to 3 | 22 | 171.27 ms | 18.34 | 3.91 | [144.00, 204.00] |
| 2 to 4 | 22 | 171.27 ms | 15.50 | 3.30 | [144.00, 196.00] |
| 2 to 5 | 24 | 170.67 ms | 19.87 | 4.06 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 15 | -5.05 µV | 2.75 | 0.71 | [-10.79, -1.30] |
| 2 to 3 | 22 | -5.24 µV | 1.91 | 0.41 | [-10.20, -0.91] |
| 2 to 4 | 22 | -6.66 µV | 2.63 | 0.56 | [-15.66, -2.59] |
| 2 to 5 | 24 | -5.99 µV | 2.55 | 0.52 | [-13.83, -1.66] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 116.22 ms | 8.84 | 2.08 | [96.00, 124.00] |
| 2 to 3 | 12 | 111.00 ms | 12.43 | 3.59 | [88.00, 124.00] |
| 2 to 4 | 16 | 109.00 ms | 13.27 | 3.32 | [88.00, 124.00] |
| 2 to 5 | 12 | 102.00 ms | 10.99 | 3.17 | [88.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 4.51 µV | 2.19 | 0.52 | [2.23, 9.13] |
| 2 to 3 | 12 | 3.34 µV | 1.74 | 0.50 | [1.17, 6.87] |
| 2 to 4 | 16 | 2.93 µV | 1.93 | 0.48 | [1.12, 7.56] |
| 2 to 5 | 12 | 2.75 µV | 2.64 | 0.76 | [0.58, 10.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 488.00 ms | 40.94 | 9.39 | [396.00, 532.00] |
| 2 to 3 | 16 | 467.75 ms | 52.08 | 13.02 | [396.00, 532.00] |
| 2 to 4 | 18 | 470.44 ms | 51.37 | 12.11 | [396.00, 532.00] |
| 2 to 5 | 21 | 451.43 ms | 39.64 | 8.65 | [396.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 5.92 µV | 2.62 | 0.60 | [1.72, 11.08] |
| 2 to 3 | 16 | 6.46 µV | 3.44 | 0.86 | [1.61, 13.70] |
| 2 to 4 | 18 | 7.15 µV | 4.24 | 1.00 | [1.60, 17.43] |
| 2 to 5 | 21 | 5.40 µV | 2.56 | 0.56 | [2.17, 11.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 470.54, BIC = 485.65
- **2 to 3 vs 2 to 1**: *β* = -3.31, *SE* = 2.815, *z* = -1.177, *p* = 0.239
- **2 to 4 vs 2 to 1**: *β* = -4.01, *SE* = 2.882, *z* = -1.391, *p* = 0.164
- **2 to 5 vs 2 to 1**: *β* = -4.30, *SE* = 3.073, *z* = -1.399, *p* = 0.162
- **SNR**: *β* = 0.43, *SE* = 0.444, *z* = 0.980, *p* = 0.327

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 3.31 | 2.82 | 1.18 | 0.239 | 0.665 | n.s. |
| 2 to 1 - 2 to 4 | 4.01 | 2.88 | 1.39 | 0.164 | 0.653 | n.s. |
| 2 to 1 - 2 to 5 | 4.30 | 3.07 | 1.40 | 0.162 | 0.653 | n.s. |
| 2 to 3 - 2 to 4 | 0.70 | 2.87 | 0.24 | 0.808 | 0.983 | n.s. |
| 2 to 3 - 2 to 5 | 0.99 | 3.02 | 0.33 | 0.744 | 0.983 | n.s. |
| 2 to 4 - 2 to 5 | 0.29 | 3.11 | 0.09 | 0.926 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.727, η²_G = 0.054
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | -0.82 | 4 | = 0.775 | -0.45 [-0.27, 1.05] | small | n.s. |
| 2 to 1 vs 2 to 4 | -1.18 | 4 | = 0.775 | -0.26 [-0.50, 0.78] | small | n.s. |
| 2 to 1 vs 2 to 5 | -0.75 | 4 | = 0.775 | -0.51 [-0.77, 0.91] | medium | n.s. |
| 2 to 3 vs 2 to 4 | 0.50 | 4 | = 0.775 | 0.26 [-0.67, 0.67] | small | n.s. |
| 2 to 3 vs 2 to 5 | 0.00 | 4 | = 1.000 | 0.00 [-0.47, 0.89] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | -0.53 | 4 | = 0.775 | -0.31 [-0.63, 0.81] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 202.34, BIC = 217.46
- **2 to 3 vs 2 to 1**: *β* = 0.22, *SE* = 0.333, *z* = 0.652, *p* = 0.514
- **2 to 4 vs 2 to 1**: *β* = -0.21, *SE* = 0.342, *z* = -0.606, *p* = 0.545
- **2 to 5 vs 2 to 1**: *β* = 0.87, *SE* = 0.369, *z* = 2.347, *p* = 0.019
- **SNR**: *β* = -0.56, *SE* = 0.052, *z* = -10.817, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | -0.22 | 0.33 | -0.65 | 0.514 | 0.764 | n.s. |
| 2 to 1 - 2 to 4 | 0.21 | 0.34 | 0.61 | 0.545 | 0.764 | n.s. |
| 2 to 1 - 2 to 5 | -0.87 | 0.37 | -2.35 | 0.019 | 0.091 | n.s. |
| 2 to 3 - 2 to 4 | 0.42 | 0.34 | 1.25 | 0.210 | 0.507 | n.s. |
| 2 to 3 - 2 to 5 | -0.65 | 0.36 | -1.81 | 0.070 | 0.252 | n.s. |
| 2 to 4 - 2 to 5 | -1.07 | 0.37 | -2.92 | 0.003 | 0.021 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.03, *p* = 0.992, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 0.08 | 4 | = 0.986 | 0.06 [-0.65, 0.62] | negligible | n.s. |
| 2 to 1 vs 2 to 4 | 0.38 | 4 | = 0.986 | 0.22 [-0.70, 0.57] | small | n.s. |
| 2 to 1 vs 2 to 5 | 0.39 | 4 | = 0.986 | 0.12 [-0.99, 0.69] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | 0.26 | 4 | = 0.986 | 0.14 [-0.30, 1.10] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 0.11 | 4 | = 0.986 | 0.08 [-0.75, 0.59] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | -0.02 | 4 | = 0.986 | -0.01 [-0.93, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 698.84, BIC = 715.77
- **2 to 3 vs 2 to 1**: *β* = -7.49, *SE* = 4.406, *z* = -1.700, *p* = 0.089
- **2 to 4 vs 2 to 1**: *β* = -6.97, *SE* = 4.531, *z* = -1.539, *p* = 0.124
- **2 to 5 vs 2 to 1**: *β* = -9.06, *SE* = 4.439, *z* = -2.040, *p* = 0.041
- **SNR**: *β* = -0.96, *SE* = 0.662, *z* = -1.452, *p* = 0.146

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 7.49 | 4.41 | 1.70 | 0.089 | 0.373 | n.s. |
| 2 to 1 - 2 to 4 | 6.97 | 4.53 | 1.54 | 0.124 | 0.411 | n.s. |
| 2 to 1 - 2 to 5 | 9.06 | 4.44 | 2.04 | 0.041 | 0.224 | n.s. |
| 2 to 3 - 2 to 4 | -0.52 | 3.88 | -0.13 | 0.894 | 0.927 | n.s. |
| 2 to 3 - 2 to 5 | 1.57 | 3.79 | 0.41 | 0.679 | 0.927 | n.s. |
| 2 to 4 - 2 to 5 | 2.08 | 3.78 | 0.55 | 0.582 | 0.927 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.05, *p* = 0.039, η²_G = 0.091
- Greenhouse-Geisser corrected: *p* = 0.075 (ε = 0.552)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.12 | 14 | = 0.105 | 0.58 [-0.05, 1.14] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 1.65 | 14 | = 0.182 | 0.53 [-0.15, 1.00] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 3.32 | 14 | = 0.018 | 0.97 [0.21, 1.50] | large | * |
| 2 to 3 vs 2 to 4 | -0.20 | 14 | = 0.841 | -0.07 [-0.49, 0.42] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 0.93 | 14 | = 0.443 | 0.28 [-0.27, 0.62] | small | n.s. |
| 2 to 4 vs 2 to 5 | 3.25 | 14 | = 0.018 | 0.37 [-0.27, 0.62] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 359.19, BIC = 376.12
- **2 to 3 vs 2 to 1**: *β* = 0.16, *SE* = 0.600, *z* = 0.267, *p* = 0.789
- **2 to 4 vs 2 to 1**: *β* = -0.76, *SE* = 0.612, *z* = -1.233, *p* = 0.218
- **2 to 5 vs 2 to 1**: *β* = -0.43, *SE* = 0.595, *z* = -0.725, *p* = 0.469
- **SNR**: *β* = -0.54, *SE* = 0.084, *z* = -6.432, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | -0.16 | 0.60 | -0.27 | 0.789 | 0.850 | n.s. |
| 2 to 1 - 2 to 4 | 0.75 | 0.61 | 1.23 | 0.218 | 0.707 | n.s. |
| 2 to 1 - 2 to 5 | 0.43 | 0.60 | 0.72 | 0.469 | 0.850 | n.s. |
| 2 to 3 - 2 to 4 | 0.92 | 0.53 | 1.72 | 0.086 | 0.416 | n.s. |
| 2 to 3 - 2 to 5 | 0.59 | 0.52 | 1.14 | 0.253 | 0.707 | n.s. |
| 2 to 4 - 2 to 5 | -0.32 | 0.52 | -0.62 | 0.533 | 0.850 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.64, *p* = 0.194, η²_G = 0.075
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 1.12 | 14 | = 0.382 | 0.36 [-0.28, 0.85] | small | n.s. |
| 2 to 1 vs 2 to 4 | 1.70 | 14 | = 0.382 | 0.71 [-0.14, 1.02] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 1.17 | 14 | = 0.382 | 0.42 [-0.26, 0.87] | small | n.s. |
| 2 to 3 vs 2 to 4 | 1.34 | 14 | = 0.382 | 0.48 [-0.07, 0.87] | small | n.s. |
| 2 to 3 vs 2 to 5 | 0.39 | 14 | = 0.702 | 0.14 [-0.20, 0.70] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | -1.03 | 14 | = 0.382 | -0.30 [-0.63, 0.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 455.63, BIC = 470.06
- **2 to 3 vs 2 to 1**: *β* = -4.45, *SE* = 4.159, *z* = -1.070, *p* = 0.285
- **2 to 4 vs 2 to 1**: *β* = -6.33, *SE* = 3.836, *z* = -1.650, *p* = 0.099
- **2 to 5 vs 2 to 1**: *β* = -13.40, *SE* = 4.136, *z* = -3.239, *p* = 0.001
- **SNR**: *β* = 0.65, *SE* = 0.670, *z* = 0.965, *p* = 0.334

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 4.45 | 4.16 | 1.07 | 0.285 | 0.488 | n.s. |
| 2 to 1 - 2 to 4 | 6.33 | 3.84 | 1.65 | 0.099 | 0.308 | n.s. |
| 2 to 1 - 2 to 5 | 13.40 | 4.14 | 3.24 | 0.001 | 0.007 | ** |
| 2 to 3 - 2 to 4 | 1.88 | 4.18 | 0.45 | 0.652 | 0.652 | n.s. |
| 2 to 3 - 2 to 5 | 8.95 | 4.44 | 2.02 | 0.044 | 0.200 | n.s. |
| 2 to 4 - 2 to 5 | 7.07 | 4.14 | 1.71 | 0.088 | 0.308 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.139, η²_G = 0.222
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.19 | 5 | = 0.241 | 1.38 [-0.04, 1.59] | large | n.s. |
| 2 to 1 vs 2 to 4 | 0.60 | 5 | = 0.693 | 0.32 [-0.39, 0.98] | small | n.s. |
| 2 to 1 vs 2 to 5 | 2.20 | 5 | = 0.241 | 1.31 [0.31, 2.06] | large | n.s. |
| 2 to 3 vs 2 to 4 | -1.32 | 5 | = 0.486 | -0.72 [-1.08, 0.78] | medium | n.s. |
| 2 to 3 vs 2 to 5 | -0.18 | 5 | = 0.862 | -0.06 [-0.61, 1.09] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.06 | 5 | = 0.505 | 0.67 [-0.22, 1.31] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 211.30, BIC = 225.72
- **2 to 3 vs 2 to 1**: *β* = -0.32, *SE* = 0.482, *z* = -0.671, *p* = 0.502
- **2 to 4 vs 2 to 1**: *β* = -0.59, *SE* = 0.441, *z* = -1.333, *p* = 0.183
- **2 to 5 vs 2 to 1**: *β* = -0.90, *SE* = 0.478, *z* = -1.873, *p* = 0.061
- **SNR**: *β* = 0.71, *SE* = 0.083, *z* = 8.502, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 0.32 | 0.48 | 0.67 | 0.502 | 0.877 | n.s. |
| 2 to 1 - 2 to 4 | 0.59 | 0.44 | 1.33 | 0.183 | 0.635 | n.s. |
| 2 to 1 - 2 to 5 | 0.89 | 0.48 | 1.87 | 0.061 | 0.315 | n.s. |
| 2 to 3 - 2 to 4 | 0.26 | 0.48 | 0.55 | 0.585 | 0.877 | n.s. |
| 2 to 3 - 2 to 5 | 0.57 | 0.51 | 1.13 | 0.260 | 0.701 | n.s. |
| 2 to 4 - 2 to 5 | 0.31 | 0.48 | 0.64 | 0.519 | 0.877 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.66, *p* = 0.017, η²_G = 0.340
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 2.11 | 5 | = 0.207 | 1.35 [-0.20, 1.35] | large | n.s. |
| 2 to 1 vs 2 to 4 | 1.66 | 5 | = 0.207 | 0.82 [-0.10, 1.38] | large | n.s. |
| 2 to 1 vs 2 to 5 | 4.10 | 5 | = 0.056 | 2.23 [0.20, 1.86] | large | n.s. |
| 2 to 3 vs 2 to 4 | -0.50 | 5 | = 0.636 | -0.23 [-1.12, 0.74] | small | n.s. |
| 2 to 3 vs 2 to 5 | 1.59 | 5 | = 0.207 | 0.76 [-0.84, 0.83] | medium | n.s. |
| 2 to 4 vs 2 to 5 | 1.95 | 5 | = 0.207 | 0.74 [0.05, 1.75] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 785.23, BIC = 801.36
- **2 to 3 vs 2 to 1**: *β* = -19.89, *SE* = 14.730, *z* = -1.350, *p* = 0.177
- **2 to 4 vs 2 to 1**: *β* = -17.35, *SE* = 14.301, *z* = -1.213, *p* = 0.225
- **2 to 5 vs 2 to 1**: *β* = -36.29, *SE* = 13.547, *z* = -2.678, *p* = 0.007
- **SNR**: *β* = 0.59, *SE* = 1.575, *z* = 0.377, *p* = 0.706

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 19.89 | 14.73 | 1.35 | 0.177 | 0.613 | n.s. |
| 2 to 1 - 2 to 4 | 17.35 | 14.30 | 1.21 | 0.225 | 0.613 | n.s. |
| 2 to 1 - 2 to 5 | 36.29 | 13.55 | 2.68 | 0.007 | 0.044 | * |
| 2 to 3 - 2 to 4 | -2.54 | 14.67 | -0.17 | 0.863 | 0.863 | n.s. |
| 2 to 3 - 2 to 5 | 16.40 | 14.34 | 1.14 | 0.253 | 0.613 | n.s. |
| 2 to 4 - 2 to 5 | 18.94 | 13.90 | 1.36 | 0.173 | 0.613 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.259, η²_G = 0.064
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | 0.78 | 14 | = 0.540 | 0.32 [-0.36, 0.76] | small | n.s. |
| 2 to 1 vs 2 to 4 | 1.38 | 14 | = 0.385 | 0.31 [-0.30, 0.75] | small | n.s. |
| 2 to 1 vs 2 to 5 | 2.32 | 14 | = 0.214 | 0.81 [0.12, 1.23] | large | n.s. |
| 2 to 3 vs 2 to 4 | -0.05 | 14 | = 0.961 | -0.02 [-0.51, 0.56] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 1.30 | 14 | = 0.385 | 0.39 [-0.20, 0.90] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.18 | 14 | = 0.385 | 0.43 [-0.13, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 336.51, BIC = 352.64
- **2 to 3 vs 2 to 1**: *β* = -0.09, *SE* = 0.615, *z* = -0.147, *p* = 0.883
- **2 to 4 vs 2 to 1**: *β* = 0.43, *SE* = 0.595, *z* = 0.728, *p* = 0.467
- **2 to 5 vs 2 to 1**: *β* = -0.50, *SE* = 0.568, *z* = -0.882, *p* = 0.378
- **SNR**: *β* = 0.54, *SE* = 0.075, *z* = 7.284, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 3 | 0.09 | 0.61 | 0.15 | 0.883 | 0.907 | n.s. |
| 2 to 1 - 2 to 4 | -0.43 | 0.60 | -0.73 | 0.467 | 0.907 | n.s. |
| 2 to 1 - 2 to 5 | 0.50 | 0.57 | 0.88 | 0.378 | 0.907 | n.s. |
| 2 to 3 - 2 to 4 | -0.52 | 0.61 | -0.86 | 0.388 | 0.907 | n.s. |
| 2 to 3 - 2 to 5 | 0.41 | 0.60 | 0.69 | 0.493 | 0.907 | n.s. |
| 2 to 4 - 2 to 5 | 0.93 | 0.58 | 1.62 | 0.106 | 0.489 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.319, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 3 | -0.87 | 14 | = 0.601 | -0.21 [-0.78, 0.34] | small | n.s. |
| 2 to 1 vs 2 to 4 | -1.07 | 14 | = 0.601 | -0.34 [-0.82, 0.23] | small | n.s. |
| 2 to 1 vs 2 to 5 | 0.50 | 14 | = 0.624 | 0.11 [-0.39, 0.61] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -0.60 | 14 | = 0.624 | -0.16 [-0.71, 0.37] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 1.63 | 14 | = 0.503 | 0.32 [-0.26, 0.83] | small | n.s. |
| 2 to 4 vs 2 to 5 | 1.46 | 14 | = 0.503 | 0.43 [-0.19, 0.83] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.039). Post-hoc tests revealed:
  - 2 to 1 showed greater latency than 2 to 5 (*d* = 0.97)
  - 2 to 4 showed greater latency than 2 to 5 (*d* = 0.37)
**P1 amplitude:** Significant main effect of condition (*p* = 0.017) (no significant pairwise comparisons)

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
