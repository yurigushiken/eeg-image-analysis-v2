# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:40:37

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
| 1 to 4 | 12 | 93.67 ms | 11.50 | 3.32 | [84.00, 108.00] |
| 2 to 5 | 13 | 96.62 ms | 12.20 | 3.38 | [84.00, 108.00] |
| 3 to 6 | 9 | 94.22 ms | 11.51 | 3.84 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 12 | 2.21 µV | 1.27 | 0.37 | [0.70, 4.46] |
| 2 to 5 | 13 | 1.96 µV | 0.57 | 0.16 | [1.14, 3.11] |
| 3 to 6 | 9 | 2.45 µV | 1.45 | 0.48 | [1.17, 5.95] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 21 | 170.29 ms | 20.57 | 4.49 | [136.00, 216.00] |
| 2 to 5 | 24 | 170.50 ms | 22.93 | 4.68 | [132.00, 216.00] |
| 3 to 6 | 23 | 170.61 ms | 19.66 | 4.10 | [140.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 21 | -6.94 µV | 2.64 | 0.58 | [-12.55, -2.71] |
| 2 to 5 | 24 | -6.07 µV | 2.53 | 0.52 | [-13.83, -1.66] |
| 3 to 6 | 23 | -6.82 µV | 2.81 | 0.59 | [-12.81, -2.56] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 14 | 93.14 ms | 12.69 | 3.39 | [72.00, 108.00] |
| 2 to 5 | 13 | 88.00 ms | 14.14 | 3.92 | [72.00, 108.00] |
| 3 to 6 | 12 | 91.33 ms | 13.08 | 3.78 | [72.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 14 | 3.04 µV | 1.54 | 0.41 | [1.16, 6.37] |
| 2 to 5 | 13 | 3.03 µV | 2.71 | 0.75 | [0.58, 10.47] |
| 3 to 6 | 12 | 3.69 µV | 1.99 | 0.57 | [1.16, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 452.80 ms | 59.41 | 13.28 | [352.00, 528.00] |
| 2 to 5 | 22 | 437.64 ms | 44.12 | 9.41 | [368.00, 520.00] |
| 3 to 6 | 18 | 466.00 ms | 51.94 | 12.24 | [360.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 6.03 µV | 3.15 | 0.70 | [2.27, 13.02] |
| 2 to 5 | 22 | 5.64 µV | 2.59 | 0.55 | [2.17, 11.71] |
| 3 to 6 | 18 | 5.08 µV | 2.36 | 0.56 | [1.96, 10.29] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 271.63, BIC = 280.79
- **2 to 5 vs 1 to 4**: *β* = 3.30, *SE* = 4.102, *z* = 0.805, *p* = 0.421
- **3 to 6 vs 1 to 4**: *β* = 0.74, *SE* = 4.678, *z* = 0.158, *p* = 0.874
- **SNR**: *β* = 0.18, *SE* = 1.835, *z* = 0.100, *p* = 0.920

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -3.30 | 4.10 | -0.80 | 0.421 | 0.806 | n.s. |
| 1 to 4 - 3 to 6 | -0.74 | 4.68 | -0.16 | 0.874 | 0.874 | n.s. |
| 2 to 5 - 3 to 6 | 2.56 | 4.67 | 0.55 | 0.583 | 0.826 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.766, η²_G = 0.067
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.10 | 2 | = 0.926 | 0.10 [-1.29, 0.61] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 1.00 | 2 | = 0.821 | 0.50 [-2.11, 3.26] | small | n.s. |
| 2 to 5 vs 3 to 6 | 0.72 | 2 | = 0.821 | 0.41 [-1.05, 1.05] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 74.61, BIC = 83.77
- **2 to 5 vs 1 to 4**: *β* = 0.14, *SE* = 0.245, *z* = 0.557, *p* = 0.578
- **3 to 6 vs 1 to 4**: *β* = -0.19, *SE* = 0.271, *z* = -0.689, *p* = 0.491
- **SNR**: *β* = 0.84, *SE* = 0.108, *z* = 7.811, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.14 | 0.24 | -0.56 | 0.578 | 0.741 | n.s. |
| 1 to 4 - 3 to 6 | 0.19 | 0.27 | 0.69 | 0.491 | 0.741 | n.s. |
| 2 to 5 - 3 to 6 | 0.32 | 0.28 | 1.16 | 0.245 | 0.570 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.25, *p* = 0.378, η²_G = 0.376
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 2.92 | 2 | = 0.300 | 1.99 [-0.75, 1.11] | large | n.s. |
| 1 to 4 vs 3 to 6 | -0.08 | 2 | = 0.945 | -0.08 [-2.53, 2.44] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -1.42 | 2 | = 0.439 | -1.32 [-1.55, 0.65] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 609.79, BIC = 623.11
- **2 to 5 vs 1 to 4**: *β* = -0.82, *SE* = 5.052, *z* = -0.163, *p* = 0.870
- **3 to 6 vs 1 to 4**: *β* = 0.13, *SE* = 5.058, *z* = 0.025, *p* = 0.980
- **SNR**: *β* = -0.19, *SE* = 1.072, *z* = -0.174, *p* = 0.862

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 0.82 | 5.05 | 0.16 | 0.870 | 0.997 | n.s. |
| 1 to 4 - 3 to 6 | -0.13 | 5.06 | -0.02 | 0.980 | 0.997 | n.s. |
| 2 to 5 - 3 to 6 | -0.95 | 4.97 | -0.19 | 0.849 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.964, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.22 | 20 | = 0.942 | 0.06 [-0.41, 0.50] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.24 | 20 | = 0.942 | 0.05 [-0.40, 0.51] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.07 | 20 | = 0.942 | -0.02 [-0.51, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 289.87, BIC = 303.19
- **2 to 5 vs 1 to 4**: *β* = 0.46, *SE* = 0.424, *z* = 1.084, *p* = 0.278
- **3 to 6 vs 1 to 4**: *β* = 0.12, *SE* = 0.426, *z* = 0.271, *p* = 0.787
- **SNR**: *β* = -0.43, *SE* = 0.098, *z* = -4.392, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.46 | 0.42 | -1.08 | 0.278 | 0.624 | n.s. |
| 1 to 4 - 3 to 6 | -0.12 | 0.43 | -0.27 | 0.787 | 0.787 | n.s. |
| 2 to 5 - 3 to 6 | 0.34 | 0.42 | 0.82 | 0.412 | 0.654 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.16, *p* = 0.324, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -1.28 | 20 | = 0.367 | -0.23 [-0.74, 0.19] | small | n.s. |
| 1 to 4 vs 3 to 6 | 0.24 | 20 | = 0.811 | 0.04 [-0.40, 0.51] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 1.20 | 20 | = 0.367 | 0.26 [-0.14, 0.75] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 308.28, BIC = 318.26
- **2 to 5 vs 1 to 4**: *β* = -3.68, *SE* = 3.980, *z* = -0.924, *p* = 0.356
- **3 to 6 vs 1 to 4**: *β* = -2.85, *SE* = 4.012, *z* = -0.710, *p* = 0.477
- **SNR**: *β* = 4.09, *SE* = 1.071, *z* = 3.821, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 3.68 | 3.98 | 0.92 | 0.356 | 0.732 | n.s. |
| 1 to 4 - 3 to 6 | 2.85 | 4.01 | 0.71 | 0.477 | 0.732 | n.s. |
| 2 to 5 - 3 to 6 | -0.83 | 4.14 | -0.20 | 0.842 | 0.842 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.761, η²_G = 0.064
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.62 | 3 | = 0.715 | 0.50 [-0.78, 1.36] | medium | n.s. |
| 1 to 4 vs 3 to 6 | 0.40 | 3 | = 0.715 | 0.37 [-0.91, 0.76] | small | n.s. |
| 2 to 5 vs 3 to 6 | -0.68 | 3 | = 0.715 | -0.22 [-0.86, 0.99] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 139.57, BIC = 149.55
- **2 to 5 vs 1 to 4**: *β* = 0.17, *SE* = 0.441, *z* = 0.375, *p* = 0.708
- **3 to 6 vs 1 to 4**: *β* = 0.26, *SE* = 0.439, *z* = 0.601, *p* = 0.548
- **SNR**: *β* = 0.99, *SE* = 0.121, *z* = 8.211, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.17 | 0.44 | -0.37 | 0.708 | 0.915 | n.s. |
| 1 to 4 - 3 to 6 | -0.26 | 0.44 | -0.60 | 0.548 | 0.908 | n.s. |
| 2 to 5 - 3 to 6 | -0.10 | 0.45 | -0.22 | 0.825 | 0.915 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.403, η²_G = 0.152
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.83 | 3 | = 0.698 | -0.67 [-1.35, 0.79] | medium | n.s. |
| 1 to 4 vs 3 to 6 | -1.51 | 3 | = 0.685 | -1.30 [-1.27, 0.47] | large | n.s. |
| 2 to 5 vs 3 to 6 | -0.36 | 3 | = 0.744 | -0.10 [-1.33, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 651.28, BIC = 663.85
- **2 to 5 vs 1 to 4**: *β* = -16.19, *SE* = 14.190, *z* = -1.141, *p* = 0.254
- **3 to 6 vs 1 to 4**: *β* = 11.03, *SE* = 15.519, *z* = 0.711, *p* = 0.477
- **SNR**: *β* = -0.86, *SE* = 2.526, *z* = -0.342, *p* = 0.732

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 16.19 | 14.19 | 1.14 | 0.254 | 0.443 | n.s. |
| 1 to 4 - 3 to 6 | -11.03 | 15.52 | -0.71 | 0.477 | 0.477 | n.s. |
| 2 to 5 - 3 to 6 | -27.22 | 14.95 | -1.82 | 0.069 | 0.192 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.47, *p* = 0.244, η²_G = 0.046
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.88 | 16 | = 0.446 | 0.28 [-0.22, 0.76] | small | n.s. |
| 1 to 4 vs 3 to 6 | -0.78 | 16 | = 0.446 | -0.22 [-0.71, 0.33] | small | n.s. |
| 2 to 5 vs 3 to 6 | -1.84 | 16 | = 0.255 | -0.58 [-0.98, 0.09] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 253.55, BIC = 266.12
- **2 to 5 vs 1 to 4**: *β* = -0.18, *SE* = 0.420, *z* = -0.421, *p* = 0.674
- **3 to 6 vs 1 to 4**: *β* = -0.34, *SE* = 0.471, *z* = -0.721, *p* = 0.471
- **SNR**: *β* = 0.45, *SE* = 0.089, *z* = 5.044, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 0.18 | 0.42 | 0.42 | 0.674 | 0.894 | n.s. |
| 1 to 4 - 3 to 6 | 0.34 | 0.47 | 0.72 | 0.471 | 0.852 | n.s. |
| 2 to 5 - 3 to 6 | 0.16 | 0.46 | 0.36 | 0.722 | 0.894 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.60, *p* = 0.039, η²_G = 0.044
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.89 | 16 | = 0.388 | 0.18 [-0.37, 0.60] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 2.74 | 16 | = 0.044 | 0.49 [0.10, 1.23] | small | * |
| 2 to 5 vs 3 to 6 | 1.90 | 16 | = 0.113 | 0.34 [-0.08, 1.00] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.039). Post-hoc tests revealed:
  - 1 to 4 showed greater amplitude than 3 to 6 (*d* = 0.49)

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
