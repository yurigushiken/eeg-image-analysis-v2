# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:27:25

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
| 1 to 1 | 24 | 116.33 ms | 16.08 | 3.28 | [92.00, 136.00] |
| 2 to 1 | 24 | 117.17 ms | 16.19 | 3.31 | [92.00, 136.00] |
| 3 to 1 | 24 | 114.17 ms | 14.49 | 2.96 | [92.00, 136.00] |
| 4 to 1 | 24 | 115.83 ms | 15.89 | 3.24 | [92.00, 136.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | -2.42 µV | 2.57 | 0.52 | [-9.61, 3.80] |
| 2 to 1 | 24 | -2.38 µV | 2.12 | 0.43 | [-6.40, 2.51] |
| 3 to 1 | 24 | -2.17 µV | 2.04 | 0.42 | [-6.48, 1.33] |
| 4 to 1 | 24 | -3.15 µV | 2.59 | 0.53 | [-8.54, 2.33] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 182.67 ms | 14.62 | 2.98 | [160.00, 204.00] |
| 2 to 1 | 24 | 182.00 ms | 12.87 | 2.63 | [160.00, 204.00] |
| 3 to 1 | 24 | 182.67 ms | 13.48 | 2.75 | [160.00, 204.00] |
| 4 to 1 | 24 | 185.00 ms | 12.44 | 2.54 | [160.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | -3.13 µV | 2.65 | 0.54 | [-9.64, 0.56] |
| 2 to 1 | 24 | -3.49 µV | 3.38 | 0.69 | [-10.79, 2.29] |
| 3 to 1 | 24 | -4.18 µV | 2.82 | 0.58 | [-10.41, -0.12] |
| 4 to 1 | 24 | -3.59 µV | 2.20 | 0.45 | [-9.44, -0.12] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 120.83 ms | 14.45 | 2.95 | [100.00, 144.00] |
| 2 to 1 | 24 | 121.67 ms | 12.37 | 2.52 | [100.00, 140.00] |
| 3 to 1 | 24 | 118.83 ms | 13.93 | 2.84 | [100.00, 144.00] |
| 4 to 1 | 24 | 125.33 ms | 13.28 | 2.71 | [100.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 4.02 µV | 3.21 | 0.66 | [-1.81, 13.50] |
| 2 to 1 | 24 | 3.91 µV | 2.81 | 0.57 | [-1.05, 9.13] |
| 3 to 1 | 24 | 3.69 µV | 2.40 | 0.49 | [-3.47, 9.14] |
| 4 to 1 | 24 | 4.33 µV | 3.11 | 0.63 | [0.52, 13.38] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 478.83 ms | 32.44 | 6.62 | [432.00, 528.00] |
| 2 to 1 | 24 | 491.00 ms | 30.35 | 6.20 | [432.00, 528.00] |
| 3 to 1 | 24 | 483.33 ms | 28.88 | 5.90 | [432.00, 528.00] |
| 4 to 1 | 24 | 485.67 ms | 33.11 | 6.76 | [432.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 24 | 1.74 µV | 2.67 | 0.55 | [-4.09, 7.06] |
| 2 to 1 | 24 | 5.14 µV | 3.58 | 0.73 | [-2.33, 11.08] |
| 3 to 1 | 24 | 5.06 µV | 3.80 | 0.78 | [-2.73, 16.27] |
| 4 to 1 | 24 | 5.61 µV | 3.64 | 0.74 | [-0.34, 12.03] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 808.34, BIC = 826.29
- **2 to 1 vs 1 to 1**: *β* = 0.83, *SE* = 4.113, *z* = 0.203, *p* = 0.839
- **3 to 1 vs 1 to 1**: *β* = -2.17, *SE* = 4.114, *z* = -0.527, *p* = 0.598
- **4 to 1 vs 1 to 1**: *β* = -0.50, *SE* = 4.120, *z* = -0.121, *p* = 0.904
- **SNR**: *β* = -0.01, *SE* = 1.117, *z* = -0.008, *p* = 0.994

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -0.84 | 4.11 | -0.20 | 0.839 | 0.990 | n.s. |
| 1 to 1 - 3 to 1 | 2.17 | 4.11 | 0.53 | 0.598 | 0.990 | n.s. |
| 1 to 1 - 4 to 1 | 0.50 | 4.12 | 0.12 | 0.904 | 0.990 | n.s. |
| 2 to 1 - 3 to 1 | 3.00 | 4.13 | 0.73 | 0.467 | 0.977 | n.s. |
| 2 to 1 - 4 to 1 | 1.33 | 4.11 | 0.32 | 0.746 | 0.990 | n.s. |
| 3 to 1 - 4 to 1 | -1.67 | 4.15 | -0.40 | 0.687 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.18, *p* = 0.908, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -0.20 | 23 | = 0.911 | -0.05 [-0.46, 0.38] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 0.52 | 23 | = 0.911 | 0.14 [-0.32, 0.53] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | 0.11 | 23 | = 0.911 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | 0.77 | 23 | = 0.911 | 0.20 [-0.27, 0.58] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | 0.29 | 23 | = 0.911 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.44 | 23 | = 0.911 | -0.11 [-0.51, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 429.05, BIC = 447.00
- **2 to 1 vs 1 to 1**: *β* = 0.13, *SE* = 0.536, *z* = 0.244, *p* = 0.807
- **3 to 1 vs 1 to 1**: *β* = 0.16, *SE* = 0.536, *z* = 0.296, *p* = 0.768
- **4 to 1 vs 1 to 1**: *β* = -0.59, *SE* = 0.537, *z* = -1.100, *p* = 0.272
- **SNR**: *β* = -0.46, *SE* = 0.150, *z* = -3.053, *p* = 0.002

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -0.13 | 0.54 | -0.24 | 0.807 | 0.987 | n.s. |
| 1 to 1 - 3 to 1 | -0.16 | 0.54 | -0.30 | 0.768 | 0.987 | n.s. |
| 1 to 1 - 4 to 1 | 0.59 | 0.54 | 1.10 | 0.272 | 0.718 | n.s. |
| 2 to 1 - 3 to 1 | -0.03 | 0.54 | -0.05 | 0.959 | 0.987 | n.s. |
| 2 to 1 - 4 to 1 | 0.72 | 0.54 | 1.35 | 0.178 | 0.663 | n.s. |
| 3 to 1 - 4 to 1 | 0.75 | 0.54 | 1.39 | 0.166 | 0.663 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.366, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -0.08 | 23 | = 0.939 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | -0.43 | 23 | = 0.866 | -0.11 [-0.51, 0.33] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | 1.14 | 23 | = 0.533 | 0.28 [-0.20, 0.66] | small | n.s. |
| 2 to 1 vs 3 to 1 | -0.36 | 23 | = 0.866 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | 1.35 | 23 | = 0.533 | 0.32 [-0.15, 0.71] | small | n.s. |
| 3 to 1 vs 4 to 1 | 1.71 | 23 | = 0.533 | 0.42 [-0.09, 0.78] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 744.18, BIC = 762.13
- **2 to 1 vs 1 to 1**: *β* = -0.73, *SE* = 2.490, *z* = -0.292, *p* = 0.770
- **3 to 1 vs 1 to 1**: *β* = 0.37, *SE* = 2.495, *z* = 0.149, *p* = 0.882
- **4 to 1 vs 1 to 1**: *β* = 2.56, *SE* = 2.492, *z* = 1.029, *p* = 0.303
- **SNR**: *β* = 0.85, *SE* = 0.375, *z* = 2.252, *p* = 0.024

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | 0.73 | 2.49 | 0.29 | 0.770 | 0.961 | n.s. |
| 1 to 1 - 3 to 1 | -0.37 | 2.49 | -0.15 | 0.882 | 0.961 | n.s. |
| 1 to 1 - 4 to 1 | -2.56 | 2.49 | -1.03 | 0.303 | 0.836 | n.s. |
| 2 to 1 - 3 to 1 | -1.10 | 2.50 | -0.44 | 0.660 | 0.961 | n.s. |
| 2 to 1 - 4 to 1 | -3.29 | 2.49 | -1.32 | 0.187 | 0.711 | n.s. |
| 3 to 1 - 4 to 1 | -2.19 | 2.49 | -0.88 | 0.378 | 0.851 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.49, *p* = 0.689, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 0.24 | 23 | = 0.979 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.79 | 23 | = 0.873 | -0.17 [-0.59, 0.26] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | -0.37 | 23 | = 0.979 | -0.05 [-0.50, 0.35] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.23 | 23 | = 0.873 | -0.24 [-0.68, 0.18] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.87 | 23 | = 0.873 | -0.18 [-0.60, 0.25] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 419.26, BIC = 437.21
- **2 to 1 vs 1 to 1**: *β* = -0.33, *SE* = 0.481, *z* = -0.690, *p* = 0.490
- **3 to 1 vs 1 to 1**: *β* = -1.24, *SE* = 0.482, *z* = -2.581, *p* = 0.010
- **4 to 1 vs 1 to 1**: *β* = -0.58, *SE* = 0.481, *z* = -1.205, *p* = 0.228
- **SNR**: *β* = -0.44, *SE* = 0.072, *z* = -6.105, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | 0.33 | 0.48 | 0.69 | 0.490 | 0.740 | n.s. |
| 1 to 1 - 3 to 1 | 1.24 | 0.48 | 2.58 | 0.010 | 0.058 | n.s. |
| 1 to 1 - 4 to 1 | 0.58 | 0.48 | 1.21 | 0.228 | 0.540 | n.s. |
| 2 to 1 - 3 to 1 | 0.91 | 0.48 | 1.89 | 0.059 | 0.261 | n.s. |
| 2 to 1 - 4 to 1 | 0.25 | 0.48 | 0.52 | 0.606 | 0.740 | n.s. |
| 3 to 1 - 4 to 1 | -0.66 | 0.48 | -1.38 | 0.168 | 0.520 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.16, *p* = 0.330, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 0.61 | 23 | = 0.659 | 0.12 [-0.30, 0.55] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 1.77 | 23 | = 0.543 | 0.38 [-0.08, 0.80] | small | n.s. |
| 1 to 1 vs 4 to 1 | 0.83 | 23 | = 0.620 | 0.19 [-0.26, 0.60] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | 1.20 | 23 | = 0.581 | 0.22 [-0.18, 0.67] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.17 | 23 | = 0.865 | 0.03 [-0.39, 0.46] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.08 | 23 | = 0.581 | -0.23 [-0.65, 0.21] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 772.37, BIC = 790.32
- **2 to 1 vs 1 to 1**: *β* = 0.83, *SE* = 3.218, *z* = 0.260, *p* = 0.795
- **3 to 1 vs 1 to 1**: *β* = -2.00, *SE* = 3.211, *z* = -0.623, *p* = 0.533
- **4 to 1 vs 1 to 1**: *β* = 4.50, *SE* = 3.210, *z* = 1.402, *p* = 0.161
- **SNR**: *β* = -0.00, *SE* = 0.529, *z* = -0.007, *p* = 0.995

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -0.84 | 3.22 | -0.26 | 0.795 | 0.795 | n.s. |
| 1 to 1 - 3 to 1 | 2.00 | 3.21 | 0.62 | 0.533 | 0.782 | n.s. |
| 1 to 1 - 4 to 1 | -4.50 | 3.21 | -1.40 | 0.161 | 0.584 | n.s. |
| 2 to 1 - 3 to 1 | 2.84 | 3.24 | 0.88 | 0.381 | 0.763 | n.s. |
| 2 to 1 - 4 to 1 | -3.67 | 3.21 | -1.14 | 0.253 | 0.689 | n.s. |
| 3 to 1 - 4 to 1 | -6.50 | 3.23 | -2.02 | 0.044 | 0.236 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.38, *p* = 0.257, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -0.38 | 23 | = 0.704 | -0.06 [-0.50, 0.34] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 0.69 | 23 | = 0.600 | 0.14 [-0.28, 0.56] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -1.13 | 23 | = 0.509 | -0.32 [-0.66, 0.20] | small | n.s. |
| 2 to 1 vs 3 to 1 | 0.98 | 23 | = 0.509 | 0.22 [-0.23, 0.63] | small | n.s. |
| 2 to 1 vs 4 to 1 | -1.09 | 23 | = 0.509 | -0.29 [-0.65, 0.20] | small | n.s. |
| 3 to 1 vs 4 to 1 | -1.65 | 23 | = 0.509 | -0.48 [-0.77, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 430.90, BIC = 448.85
- **2 to 1 vs 1 to 1**: *β* = -0.36, *SE* = 0.515, *z* = -0.695, *p* = 0.487
- **3 to 1 vs 1 to 1**: *β* = -0.17, *SE* = 0.513, *z* = -0.332, *p* = 0.740
- **4 to 1 vs 1 to 1**: *β* = 0.17, *SE* = 0.513, *z* = 0.327, *p* = 0.744
- **SNR**: *β* = 0.44, *SE* = 0.094, *z* = 4.701, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | 0.36 | 0.51 | 0.69 | 0.487 | 0.965 | n.s. |
| 1 to 1 - 3 to 1 | 0.17 | 0.51 | 0.33 | 0.740 | 0.978 | n.s. |
| 1 to 1 - 4 to 1 | -0.17 | 0.51 | -0.33 | 0.744 | 0.978 | n.s. |
| 2 to 1 - 3 to 1 | -0.19 | 0.52 | -0.36 | 0.719 | 0.978 | n.s. |
| 2 to 1 - 4 to 1 | -0.53 | 0.51 | -1.02 | 0.305 | 0.888 | n.s. |
| 3 to 1 - 4 to 1 | -0.34 | 0.52 | -0.66 | 0.512 | 0.965 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.712, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 0.21 | 23 | = 0.836 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 0.62 | 23 | = 0.836 | 0.12 [-0.30, 0.55] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.55 | 23 | = 0.836 | -0.10 [-0.54, 0.31] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | 0.38 | 23 | = 0.836 | 0.08 [-0.35, 0.50] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.76 | 23 | = 0.836 | -0.14 [-0.58, 0.27] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.12 | 23 | = 0.836 | -0.23 [-0.66, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 941.94, BIC = 959.89
- **2 to 1 vs 1 to 1**: *β* = 13.39, *SE* = 8.802, *z* = 1.521, *p* = 0.128
- **3 to 1 vs 1 to 1**: *β* = 7.08, *SE* = 9.034, *z* = 0.783, *p* = 0.434
- **4 to 1 vs 1 to 1**: *β* = 9.39, *SE* = 9.029, *z* = 1.040, *p* = 0.298
- **SNR**: *β* = -0.59, *SE* = 0.527, *z* = -1.114, *p* = 0.265

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -13.39 | 8.80 | -1.52 | 0.128 | 0.561 | n.s. |
| 1 to 1 - 3 to 1 | -7.08 | 9.03 | -0.78 | 0.434 | 0.897 | n.s. |
| 1 to 1 - 4 to 1 | -9.39 | 9.03 | -1.04 | 0.298 | 0.830 | n.s. |
| 2 to 1 - 3 to 1 | 6.32 | 8.82 | 0.72 | 0.474 | 0.897 | n.s. |
| 2 to 1 - 4 to 1 | 4.00 | 8.81 | 0.45 | 0.650 | 0.897 | n.s. |
| 3 to 1 - 4 to 1 | -2.31 | 8.73 | -0.26 | 0.791 | 0.897 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.596, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -1.17 | 23 | = 0.739 | -0.39 [-0.67, 0.19] | small | n.s. |
| 1 to 1 vs 3 to 1 | -0.47 | 23 | = 0.739 | -0.15 [-0.52, 0.33] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.60 | 23 | = 0.739 | -0.21 [-0.55, 0.30] | small | n.s. |
| 2 to 1 vs 3 to 1 | 1.14 | 23 | = 0.739 | 0.26 [-0.20, 0.66] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.68 | 23 | = 0.739 | 0.17 [-0.29, 0.56] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.34 | 23 | = 0.739 | -0.08 [-0.49, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 478.88, BIC = 496.83
- **2 to 1 vs 1 to 1**: *β* = 3.06, *SE* = 0.654, *z* = 4.676, *p* < .001
- **3 to 1 vs 1 to 1**: *β* = 2.59, *SE* = 0.676, *z* = 3.829, *p* < .001
- **4 to 1 vs 1 to 1**: *β* = 3.15, *SE* = 0.675, *z* = 4.657, *p* < .001
- **SNR**: *β* = 0.17, *SE* = 0.044, *z* = 3.771, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -3.06 | 0.65 | -4.68 | < .001 | < .001 | *** |
| 1 to 1 - 3 to 1 | -2.59 | 0.68 | -3.83 | < .001 | < .001 | *** |
| 1 to 1 - 4 to 1 | -3.14 | 0.68 | -4.66 | < .001 | < .001 | *** |
| 2 to 1 - 3 to 1 | 0.47 | 0.65 | 0.72 | 0.474 | 0.772 | n.s. |
| 2 to 1 - 4 to 1 | -0.09 | 0.65 | -0.14 | 0.892 | 0.892 | n.s. |
| 3 to 1 - 4 to 1 | -0.56 | 0.65 | -0.86 | 0.389 | 0.772 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 12.80, *p* < .001, η²_G = 0.173
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -5.35 | 23 | < .001 | -1.08 [-1.62, -0.56] | large | *** |
| 1 to 1 vs 3 to 1 | -3.89 | 23 | = 0.001 | -1.01 [-1.28, -0.31] | large | ** |
| 1 to 1 vs 4 to 1 | -6.20 | 23 | < .001 | -1.21 [-1.83, -0.70] | large | *** |
| 2 to 1 vs 3 to 1 | 0.12 | 23 | = 0.907 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.84 | 23 | = 0.600 | -0.13 [-0.60, 0.25] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.69 | 23 | = 0.600 | -0.15 [-0.56, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 1 showed smaller amplitude than 2 to 1 (*d* = -1.08)
  - 1 to 1 showed smaller amplitude than 3 to 1 (*d* = -1.01)
  - 1 to 1 showed smaller amplitude than 4 to 1 (*d* = -1.21)

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
