# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:36:45

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
| Decrease by 1 | 17 | 107.29 ms | 9.41 | 2.28 | [92.00, 120.00] |
| Decrease by 2 | 20 | 109.60 ms | 9.48 | 2.12 | [92.00, 120.00] |
| Decrease by 3 | 18 | 106.67 ms | 9.31 | 2.19 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 17 | -1.61 µV | 1.19 | 0.29 | [-4.56, -0.23] |
| Decrease by 2 | 20 | -1.79 µV | 1.01 | 0.23 | [-4.30, -0.45] |
| Decrease by 3 | 18 | -2.49 µV | 1.51 | 0.36 | [-6.39, -0.79] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 23 | 178.26 ms | 14.86 | 3.10 | [152.00, 212.00] |
| Decrease by 2 | 24 | 177.67 ms | 14.54 | 2.97 | [148.00, 212.00] |
| Decrease by 3 | 24 | 177.00 ms | 15.02 | 3.07 | [152.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 23 | -5.06 µV | 1.94 | 0.40 | [-9.90, -2.24] |
| Decrease by 2 | 24 | -5.12 µV | 2.11 | 0.43 | [-9.59, -1.53] |
| Decrease by 3 | 24 | -5.22 µV | 1.97 | 0.40 | [-8.60, -1.48] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 14 | 114.29 ms | 8.70 | 2.32 | [100.00, 124.00] |
| Decrease by 2 | 17 | 114.82 ms | 8.92 | 2.16 | [100.00, 124.00] |
| Decrease by 3 | 17 | 115.06 ms | 7.55 | 1.83 | [104.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 14 | 2.36 µV | 1.78 | 0.47 | [0.61, 5.67] |
| Decrease by 2 | 17 | 2.54 µV | 1.31 | 0.32 | [0.71, 5.74] |
| Decrease by 3 | 17 | 2.96 µV | 1.86 | 0.45 | [1.02, 8.15] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 20 | 491.40 ms | 32.92 | 7.36 | [436.00, 536.00] |
| Decrease by 2 | 19 | 471.58 ms | 26.19 | 6.01 | [436.00, 536.00] |
| Decrease by 3 | 20 | 482.40 ms | 30.67 | 6.86 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 | 20 | 4.99 µV | 2.52 | 0.56 | [1.41, 9.87] |
| Decrease by 2 | 19 | 4.93 µV | 2.07 | 0.48 | [1.69, 8.68] |
| Decrease by 3 | 20 | 5.30 µV | 3.03 | 0.68 | [0.72, 12.38] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 398.42, BIC = 410.46
- **Decrease by 2 vs Decrease by 1**: *β* = 0.70, *SE* = 2.213, *z* = 0.317, *p* = 0.751
- **Decrease by 3 vs Decrease by 1**: *β* = -2.78, *SE* = 2.357, *z* = -1.181, *p* = 0.238
- **SNR**: *β* = 1.95, *SE* = 0.632, *z* = 3.088, *p* = 0.002

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.70 | 2.21 | -0.32 | 0.751 | 0.751 | n.s. |
| Decrease by 1 - Decrease by 3 | 2.78 | 2.36 | 1.18 | 0.238 | 0.419 | n.s. |
| Decrease by 2 - Decrease by 3 | 3.48 | 2.11 | 1.65 | 0.099 | 0.268 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.802, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.707 (ε = 0.651)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -0.89 | 11 | = 0.838 | -0.15 [-0.58, 0.58] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -0.60 | 11 | = 0.838 | -0.19 [-0.87, 0.36] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.10 | 11 | = 0.922 | -0.04 [-0.29, 0.79] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 159.01, BIC = 171.05
- **Decrease by 2 vs Decrease by 1**: *β* = 0.02, *SE* = 0.259, *z* = 0.075, *p* = 0.940
- **Decrease by 3 vs Decrease by 1**: *β* = -0.61, *SE* = 0.278, *z* = -2.202, *p* = 0.028
- **SNR**: *β* = -0.30, *SE* = 0.071, *z* = -4.210, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.02 | 0.26 | -0.08 | 0.940 | 0.940 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.61 | 0.28 | 2.20 | 0.028 | 0.055 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.63 | 0.25 | 2.54 | 0.011 | 0.033 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.05, *p* = 0.016, η²_G = 0.109
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.41 | 11 | = 0.687 | 0.11 [-0.45, 0.71] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 2.88 | 11 | = 0.045 | 0.70 [0.17, 1.60] | medium | * |
| Decrease by 2 vs Decrease by 3 | 2.44 | 11 | = 0.049 | 0.64 [0.10, 1.28] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 558.18, BIC = 571.75
- **Decrease by 2 vs Decrease by 1**: *β* = -1.24, *SE* = 2.359, *z* = -0.525, *p* = 0.600
- **Decrease by 3 vs Decrease by 1**: *β* = -1.95, *SE* = 2.372, *z* = -0.821, *p* = 0.412
- **SNR**: *β* = 0.12, *SE* = 0.275, *z* = 0.441, *p* = 0.659

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 1.24 | 2.36 | 0.52 | 0.600 | 0.840 | n.s. |
| Decrease by 1 - Decrease by 3 | 1.95 | 2.37 | 0.82 | 0.412 | 0.796 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.71 | 2.31 | 0.31 | 0.758 | 0.840 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.695, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.46 | 22 | = 0.710 | 0.07 [-0.34, 0.53] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.93 | 22 | = 0.710 | 0.14 [-0.24, 0.63] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.38 | 22 | = 0.710 | 0.07 [-0.37, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 253.59, BIC = 267.17
- **Decrease by 2 vs Decrease by 1**: *β* = -0.02, *SE* = 0.272, *z* = -0.071, *p* = 0.943
- **Decrease by 3 vs Decrease by 1**: *β* = -0.07, *SE* = 0.273, *z* = -0.241, *p* = 0.810
- **SNR**: *β* = -0.14, *SE* = 0.032, *z* = -4.541, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.02 | 0.27 | 0.07 | 0.943 | 0.993 | n.s. |
| Decrease by 1 - Decrease by 3 | 0.07 | 0.27 | 0.24 | 0.810 | 0.993 | n.s. |
| Decrease by 2 - Decrease by 3 | 0.05 | 0.27 | 0.17 | 0.861 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.35, *p* = 0.704, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.67 | 22 | = 0.767 | 0.11 [-0.30, 0.57] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | 0.76 | 22 | = 0.767 | 0.12 [-0.28, 0.59] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | 0.08 | 22 | = 0.935 | 0.01 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 334.67, BIC = 345.89
- **Decrease by 2 vs Decrease by 1**: *β* = -0.19, *SE* = 1.937, *z* = -0.096, *p* = 0.923
- **Decrease by 3 vs Decrease by 1**: *β* = 0.51, *SE* = 1.919, *z* = 0.266, *p* = 0.790
- **SNR**: *β* = 0.47, *SE* = 0.390, *z* = 1.199, *p* = 0.231

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.19 | 1.94 | 0.10 | 0.923 | 0.972 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.51 | 1.92 | -0.27 | 0.790 | 0.972 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.70 | 1.78 | -0.39 | 0.695 | 0.972 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.72, *p* = 0.498, η²_G = 0.018
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 0.44 | 10 | = 0.669 | 0.13 [-0.51, 0.77] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.08 | 10 | = 0.461 | -0.19 [-1.04, 0.27] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.08 | 10 | = 0.461 | -0.32 [-0.58, 0.52] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 156.46, BIC = 167.69
- **Decrease by 2 vs Decrease by 1**: *β* = 0.20, *SE* = 0.306, *z* = 0.653, *p* = 0.514
- **Decrease by 3 vs Decrease by 1**: *β* = 0.75, *SE* = 0.304, *z* = 2.455, *p* = 0.014
- **SNR**: *β* = 0.30, *SE* = 0.061, *z* = 4.952, *p* < .001

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | -0.20 | 0.31 | -0.65 | 0.514 | 0.514 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.75 | 0.30 | -2.46 | 0.014 | 0.042 | * |
| Decrease by 2 - Decrease by 3 | -0.55 | 0.28 | -1.95 | 0.051 | 0.100 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.98, *p* = 0.165, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | -1.10 | 10 | = 0.446 | -0.33 [-0.96, 0.34] | small | n.s. |
| Decrease by 1 vs Decrease by 3 | -2.75 | 10 | = 0.061 | -0.48 [-1.67, -0.16] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.73 | 10 | = 0.482 | -0.25 [-0.79, 0.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 569.58, BIC = 582.05
- **Decrease by 2 vs Decrease by 1**: *β* = -20.38, *SE* = 7.201, *z* = -2.830, *p* = 0.005
- **Decrease by 3 vs Decrease by 1**: *β* = -10.76, *SE* = 7.184, *z* = -1.497, *p* = 0.134
- **SNR**: *β* = 0.06, *SE* = 0.793, *z* = 0.075, *p* = 0.941

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 20.38 | 7.20 | 2.83 | 0.005 | 0.014 | * |
| Decrease by 1 - Decrease by 3 | 10.76 | 7.18 | 1.50 | 0.134 | 0.251 | n.s. |
| Decrease by 2 - Decrease by 3 | -9.62 | 7.23 | -1.33 | 0.183 | 0.251 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.92, *p* = 0.068, η²_G = 0.068
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 2.80 | 16 | = 0.039 | 0.65 [0.15, 1.27] | medium | * |
| Decrease by 1 vs Decrease by 3 | 1.34 | 16 | = 0.300 | 0.37 [-0.19, 0.82] | small | n.s. |
| Decrease by 2 vs Decrease by 3 | -0.90 | 16 | = 0.382 | -0.25 [-0.72, 0.28] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 240.54, BIC = 253.01
- **Decrease by 2 vs Decrease by 1**: *β* = -0.15, *SE* = 0.370, *z* = -0.406, *p* = 0.685
- **Decrease by 3 vs Decrease by 1**: *β* = 0.27, *SE* = 0.371, *z* = 0.720, *p* = 0.471
- **SNR**: *β* = 0.13, *SE* = 0.054, *z* = 2.439, *p* = 0.015

_Reference condition: **Decrease by 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 - Decrease by 2 | 0.15 | 0.37 | 0.41 | 0.685 | 0.721 | n.s. |
| Decrease by 1 - Decrease by 3 | -0.27 | 0.37 | -0.72 | 0.471 | 0.721 | n.s. |
| Decrease by 2 - Decrease by 3 | -0.42 | 0.37 | -1.11 | 0.265 | 0.603 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.31, *p* = 0.115, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 vs Decrease by 2 | 1.02 | 16 | = 0.323 | 0.15 [-0.30, 0.70] | negligible | n.s. |
| Decrease by 1 vs Decrease by 3 | -1.38 | 16 | = 0.281 | -0.19 [-0.80, 0.21] | negligible | n.s. |
| Decrease by 2 vs Decrease by 3 | -1.79 | 16 | = 0.277 | -0.34 [-0.84, 0.18] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.016). Post-hoc tests revealed:
  - Decrease by 1 showed greater amplitude than Decrease by 3 (*d* = 0.70)
  - Decrease by 2 showed greater amplitude than Decrease by 3 (*d* = 0.64)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.068)

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
