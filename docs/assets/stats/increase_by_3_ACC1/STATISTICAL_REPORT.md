# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:24:44

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
| 1 to 4 | 24 | 100.17 ms | 10.91 | 2.23 | [84.00, 112.00] |
| 2 to 5 | 24 | 98.17 ms | 11.19 | 2.28 | [84.00, 112.00] |
| 3 to 6 | 24 | 98.83 ms | 11.28 | 2.30 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -1.43 µV | 1.91 | 0.39 | [-4.46, 2.21] |
| 2 to 5 | 24 | -1.44 µV | 2.86 | 0.58 | [-12.97, 1.02] |
| 3 to 6 | 24 | -2.15 µV | 2.09 | 0.43 | [-5.36, 1.55] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 173.00 ms | 20.13 | 4.11 | [136.00, 216.00] |
| 2 to 5 | 24 | 173.17 ms | 20.41 | 4.17 | [136.00, 212.00] |
| 3 to 6 | 24 | 169.67 ms | 21.06 | 4.30 | [136.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -6.41 µV | 3.21 | 0.65 | [-13.14, -1.20] |
| 2 to 5 | 24 | -6.39 µV | 2.61 | 0.53 | [-13.83, -1.17] |
| 3 to 6 | 24 | -6.89 µV | 2.91 | 0.59 | [-12.76, -1.85] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 94.83 ms | 11.34 | 2.32 | [76.00, 108.00] |
| 2 to 5 | 24 | 92.83 ms | 13.24 | 2.70 | [76.00, 108.00] |
| 3 to 6 | 24 | 94.17 ms | 13.55 | 2.77 | [76.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 1.97 µV | 1.96 | 0.40 | [-0.89, 6.37] |
| 2 to 5 | 24 | 2.02 µV | 2.86 | 0.58 | [-2.14, 11.63] |
| 3 to 6 | 24 | 1.82 µV | 2.56 | 0.52 | [-1.77, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 459.00 ms | 53.23 | 10.86 | [376.00, 528.00] |
| 2 to 5 | 24 | 445.17 ms | 52.16 | 10.65 | [364.00, 528.00] |
| 3 to 6 | 24 | 472.83 ms | 56.32 | 11.50 | [360.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 5.14 µV | 3.71 | 0.76 | [-0.58, 13.02] |
| 2 to 5 | 24 | 5.77 µV | 2.72 | 0.56 | [0.85, 11.71] |
| 3 to 6 | 24 | 4.30 µV | 2.61 | 0.53 | [0.00, 11.34] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 559.23, BIC = 572.89
- **2 to 5 vs 1 to 4**: *β* = -1.70, *SE* = 3.067, *z* = -0.553, *p* = 0.580
- **3 to 6 vs 1 to 4**: *β* = -1.21, *SE* = 3.049, *z* = -0.397, *p* = 0.691
- **SNR**: *β* = 0.64, *SE* = 0.759, *z* = 0.838, *p* = 0.402

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 1.70 | 3.07 | 0.55 | 0.580 | 0.926 | n.s. |
| 1 to 4 - 3 to 6 | 1.21 | 3.05 | 0.40 | 0.691 | 0.926 | n.s. |
| 2 to 5 - 3 to 6 | -0.49 | 3.05 | -0.16 | 0.874 | 0.926 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.21, *p* = 0.808, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.64 | 23 | = 0.824 | 0.18 [-0.29, 0.55] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.41 | 23 | = 0.824 | 0.12 [-0.34, 0.51] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.23 | 23 | = 0.824 | -0.06 [-0.47, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 302.04, BIC = 315.70
- **2 to 5 vs 1 to 4**: *β* = -0.39, *SE* = 0.527, *z* = -0.748, *p* = 0.455
- **3 to 6 vs 1 to 4**: *β* = -0.88, *SE* = 0.524, *z* = -1.673, *p* = 0.094
- **SNR**: *β* = -0.82, *SE* = 0.127, *z* = -6.433, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 0.39 | 0.53 | 0.75 | 0.455 | 0.587 | n.s. |
| 1 to 4 - 3 to 6 | 0.88 | 0.52 | 1.67 | 0.094 | 0.257 | n.s. |
| 2 to 5 - 3 to 6 | 0.48 | 0.52 | 0.92 | 0.358 | 0.587 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.73, *p* = 0.485, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.00 | 23 | = 0.996 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 1.23 | 23 | = 0.434 | 0.36 [-0.18, 0.68] | small | n.s. |
| 2 to 5 vs 3 to 6 | 1.08 | 23 | = 0.434 | 0.29 [-0.21, 0.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 634.55, BIC = 648.21
- **2 to 5 vs 1 to 4**: *β* = 0.10, *SE* = 4.307, *z* = 0.024, *p* = 0.981
- **3 to 6 vs 1 to 4**: *β* = -3.33, *SE* = 4.271, *z* = -0.779, *p* = 0.436
- **SNR**: *β* = -0.12, *SE* = 1.036, *z* = -0.112, *p* = 0.911

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.10 | 4.31 | -0.02 | 0.981 | 0.981 | n.s. |
| 1 to 4 - 3 to 6 | 3.33 | 4.27 | 0.78 | 0.436 | 0.811 | n.s. |
| 2 to 5 - 3 to 6 | 3.43 | 4.31 | 0.80 | 0.426 | 0.811 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.666, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.04 | 23 | = 0.971 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.76 | 23 | = 0.681 | 0.16 [-0.27, 0.58] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 0.84 | 23 | = 0.681 | 0.17 [-0.25, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 318.44, BIC = 332.10
- **2 to 5 vs 1 to 4**: *β* = -0.28, *SE* = 0.458, *z* = -0.608, *p* = 0.543
- **3 to 6 vs 1 to 4**: *β* = -0.46, *SE* = 0.454, *z* = -1.002, *p* = 0.316
- **SNR**: *β* = -0.56, *SE* = 0.117, *z* = -4.739, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 0.28 | 0.46 | 0.61 | 0.543 | 0.791 | n.s. |
| 1 to 4 - 3 to 6 | 0.45 | 0.45 | 1.00 | 0.316 | 0.680 | n.s. |
| 2 to 5 - 3 to 6 | 0.18 | 0.46 | 0.38 | 0.701 | 0.791 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.543, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.04 | 23 | = 0.969 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 1.06 | 23 | = 0.570 | 0.16 [-0.21, 0.64] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 0.89 | 23 | = 0.570 | 0.18 [-0.24, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 571.92, BIC = 585.58
- **2 to 5 vs 1 to 4**: *β* = -1.26, *SE* = 3.045, *z* = -0.413, *p* = 0.680
- **3 to 6 vs 1 to 4**: *β* = -0.74, *SE* = 3.003, *z* = -0.248, *p* = 0.804
- **SNR**: *β* = 1.68, *SE* = 1.151, *z* = 1.460, *p* = 0.144

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 1.26 | 3.05 | 0.41 | 0.680 | 0.967 | n.s. |
| 1 to 4 - 3 to 6 | 0.74 | 3.00 | 0.25 | 0.804 | 0.967 | n.s. |
| 2 to 5 - 3 to 6 | -0.51 | 3.05 | -0.17 | 0.867 | 0.967 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.805, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.65 | 23 | = 0.819 | 0.16 [-0.29, 0.56] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.23 | 23 | = 0.819 | 0.05 [-0.38, 0.47] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.40 | 23 | = 0.819 | -0.10 [-0.51, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 331.33, BIC = 344.99
- **2 to 5 vs 1 to 4**: *β* = 0.39, *SE* = 0.593, *z* = 0.656, *p* = 0.512
- **3 to 6 vs 1 to 4**: *β* = -0.18, *SE* = 0.586, *z* = -0.312, *p* = 0.755
- **SNR**: *β* = 0.77, *SE* = 0.218, *z* = 3.539, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.39 | 0.59 | -0.66 | 0.512 | 0.762 | n.s. |
| 1 to 4 - 3 to 6 | 0.18 | 0.59 | 0.31 | 0.755 | 0.762 | n.s. |
| 2 to 5 - 3 to 6 | 0.57 | 0.60 | 0.96 | 0.336 | 0.708 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.05, *p* = 0.954, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.06 | 23 | = 0.949 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.21 | 23 | = 0.949 | 0.06 [-0.38, 0.46] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 0.39 | 23 | = 0.949 | 0.07 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 779.02, BIC = 792.68
- **2 to 5 vs 1 to 4**: *β* = -15.59, *SE* = 12.444, *z* = -1.253, *p* = 0.210
- **3 to 6 vs 1 to 4**: *β* = 10.20, *SE* = 12.865, *z* = 0.793, *p* = 0.428
- **SNR**: *β* = -2.41, *SE* = 2.472, *z* = -0.974, *p* = 0.330

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 15.59 | 12.44 | 1.25 | 0.210 | 0.376 | n.s. |
| 1 to 4 - 3 to 6 | -10.20 | 12.86 | -0.79 | 0.428 | 0.428 | n.s. |
| 2 to 5 - 3 to 6 | -25.79 | 12.46 | -2.07 | 0.038 | 0.111 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.40, *p* = 0.102, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 1.09 | 23 | = 0.302 | 0.26 [-0.20, 0.65] | small | n.s. |
| 1 to 4 vs 3 to 6 | -1.06 | 23 | = 0.302 | -0.25 [-0.64, 0.21] | small | n.s. |
| 2 to 5 vs 3 to 6 | -2.27 | 23 | = 0.098 | -0.51 [-0.91, -0.02] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 328.21, BIC = 341.87
- **2 to 5 vs 1 to 4**: *β* = 0.93, *SE* = 0.485, *z* = 1.910, *p* = 0.056
- **3 to 6 vs 1 to 4**: *β* = -0.22, *SE* = 0.507, *z* = -0.432, *p* = 0.666
- **SNR**: *β* = 0.41, *SE* = 0.113, *z* = 3.618, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.93 | 0.48 | -1.91 | 0.056 | 0.109 | n.s. |
| 1 to 4 - 3 to 6 | 0.22 | 0.51 | 0.43 | 0.666 | 0.666 | n.s. |
| 2 to 5 - 3 to 6 | 1.15 | 0.49 | 2.36 | 0.018 | 0.054 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.19, *p* = 0.021, η²_G = 0.039
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -1.13 | 23 | = 0.272 | -0.19 [-0.66, 0.20] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 1.69 | 23 | = 0.156 | 0.26 [-0.09, 0.78] | small | n.s. |
| 2 to 5 vs 3 to 6 | 3.13 | 23 | = 0.014 | 0.55 [0.18, 1.10] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.021). Post-hoc tests revealed:
  - 2 to 5 showed greater amplitude than 3 to 6 (*d* = 0.55)

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
