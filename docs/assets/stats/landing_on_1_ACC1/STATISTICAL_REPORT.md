# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:46:21

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
| 1 to 1 | 16 | 119.75 ms | 11.54 | 2.89 | [100.00, 136.00] |
| 2 to 1 | 17 | 117.88 ms | 16.92 | 4.10 | [92.00, 136.00] |
| 3 to 1 | 14 | 116.86 ms | 14.48 | 3.87 | [92.00, 136.00] |
| 4 to 1 | 17 | 119.53 ms | 12.32 | 2.99 | [92.00, 136.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 16 | -3.33 µV | 2.30 | 0.58 | [-9.61, -0.50] |
| 2 to 1 | 17 | -3.27 µV | 1.61 | 0.39 | [-6.40, -0.68] |
| 3 to 1 | 14 | -3.36 µV | 1.78 | 0.48 | [-6.48, -1.60] |
| 4 to 1 | 17 | -4.12 µV | 2.26 | 0.55 | [-8.54, -1.75] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 16 | 181.75 ms | 13.70 | 3.42 | [160.00, 204.00] |
| 2 to 1 | 17 | 180.47 ms | 11.65 | 2.83 | [160.00, 204.00] |
| 3 to 1 | 21 | 183.24 ms | 13.89 | 3.03 | [160.00, 204.00] |
| 4 to 1 | 20 | 186.60 ms | 11.11 | 2.48 | [168.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 16 | -4.44 µV | 2.20 | 0.55 | [-9.64, -0.89] |
| 2 to 1 | 17 | -4.94 µV | 2.71 | 0.66 | [-10.79, -0.76] |
| 3 to 1 | 21 | -4.63 µV | 2.72 | 0.59 | [-10.41, -1.32] |
| 4 to 1 | 20 | -4.08 µV | 2.04 | 0.46 | [-9.44, -0.51] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 18 | 123.56 ms | 12.11 | 2.85 | [100.00, 144.00] |
| 2 to 1 | 18 | 123.11 ms | 12.08 | 2.85 | [100.00, 140.00] |
| 3 to 1 | 20 | 122.00 ms | 12.88 | 2.88 | [100.00, 144.00] |
| 4 to 1 | 16 | 121.50 ms | 10.42 | 2.60 | [108.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 18 | 5.04 µV | 2.87 | 0.68 | [1.65, 13.50] |
| 2 to 1 | 18 | 4.93 µV | 2.36 | 0.56 | [1.50, 9.13] |
| 3 to 1 | 20 | 4.27 µV | 1.86 | 0.42 | [1.64, 9.14] |
| 4 to 1 | 16 | 5.91 µV | 2.60 | 0.65 | [2.46, 13.38] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 10 | 479.60 ms | 35.25 | 11.15 | [432.00, 528.00] |
| 2 to 1 | 21 | 493.52 ms | 27.61 | 6.03 | [432.00, 528.00] |
| 3 to 1 | 20 | 483.40 ms | 25.90 | 5.79 | [444.00, 528.00] |
| 4 to 1 | 21 | 488.19 ms | 30.55 | 6.67 | [432.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 1 | 10 | 3.96 µV | 1.77 | 0.56 | [1.31, 7.06] |
| 2 to 1 | 21 | 5.79 µV | 3.25 | 0.71 | [1.47, 11.08] |
| 3 to 1 | 20 | 6.11 µV | 3.17 | 0.71 | [2.57, 16.27] |
| 4 to 1 | 21 | 6.38 µV | 3.21 | 0.70 | [1.12, 12.03] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 529.06, BIC = 544.17
- **2 to 1 vs 1 to 1**: *β* = -1.98, *SE* = 4.693, *z* = -0.423, *p* = 0.673
- **3 to 1 vs 1 to 1**: *β* = -2.92, *SE* = 4.988, *z* = -0.585, *p* = 0.559
- **4 to 1 vs 1 to 1**: *β* = -0.46, *SE* = 4.750, *z* = -0.098, *p* = 0.922
- **SNR**: *β* = 0.31, *SE* = 1.230, *z* = 0.249, *p* = 0.803

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | 1.98 | 4.69 | 0.42 | 0.673 | 0.993 | n.s. |
| 1 to 1 - 3 to 1 | 2.92 | 4.99 | 0.58 | 0.559 | 0.993 | n.s. |
| 1 to 1 - 4 to 1 | 0.46 | 4.75 | 0.10 | 0.922 | 0.993 | n.s. |
| 2 to 1 - 3 to 1 | 0.93 | 4.92 | 0.19 | 0.850 | 0.993 | n.s. |
| 2 to 1 - 4 to 1 | -1.52 | 4.62 | -0.33 | 0.742 | 0.993 | n.s. |
| 3 to 1 - 4 to 1 | -2.45 | 4.96 | -0.49 | 0.621 | 0.993 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.17, *p* = 0.916, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -0.38 | 8 | = 1.000 | -0.23 [-0.49, 0.72] | small | n.s. |
| 1 to 1 vs 3 to 1 | 0.00 | 8 | = 1.000 | 0.00 [-0.49, 0.87] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.54 | 8 | = 1.000 | -0.30 [-0.87, 0.42] | small | n.s. |
| 2 to 1 vs 3 to 1 | 0.42 | 8 | = 1.000 | 0.21 [-0.58, 0.85] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.00 | 8 | = 1.000 | 0.00 [-0.54, 0.57] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.65 | 8 | = 1.000 | -0.27 [-0.78, 0.57] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 237.39, BIC = 252.50
- **2 to 1 vs 1 to 1**: *β* = 0.14, *SE* = 0.413, *z* = 0.339, *p* = 0.734
- **3 to 1 vs 1 to 1**: *β* = -0.21, *SE* = 0.436, *z* = -0.478, *p* = 0.633
- **4 to 1 vs 1 to 1**: *β* = -0.53, *SE* = 0.421, *z* = -1.255, *p* = 0.210
- **SNR**: *β* = -0.83, *SE* = 0.113, *z* = -7.345, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -0.14 | 0.41 | -0.34 | 0.734 | 0.895 | n.s. |
| 1 to 1 - 3 to 1 | 0.21 | 0.44 | 0.48 | 0.633 | 0.895 | n.s. |
| 1 to 1 - 4 to 1 | 0.53 | 0.42 | 1.25 | 0.210 | 0.691 | n.s. |
| 2 to 1 - 3 to 1 | 0.35 | 0.44 | 0.79 | 0.431 | 0.895 | n.s. |
| 2 to 1 - 4 to 1 | 0.67 | 0.40 | 1.67 | 0.094 | 0.448 | n.s. |
| 3 to 1 - 4 to 1 | 0.32 | 0.45 | 0.72 | 0.473 | 0.895 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.17, *p* = 0.342, η²_G = 0.063
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 0.09 | 8 | = 0.927 | 0.04 [-0.54, 0.67] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | -0.70 | 8 | = 0.608 | -0.21 [-0.76, 0.59] | small | n.s. |
| 1 to 1 vs 4 to 1 | 1.16 | 8 | = 0.608 | 0.38 [-0.20, 1.14] | small | n.s. |
| 2 to 1 vs 3 to 1 | -0.80 | 8 | = 0.608 | -0.35 [-1.09, 0.38] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.96 | 8 | = 0.608 | 0.43 [-0.27, 0.86] | small | n.s. |
| 3 to 1 vs 4 to 1 | 2.80 | 8 | = 0.139 | 0.67 [-0.02, 1.50] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 559.37, BIC = 575.50
- **2 to 1 vs 1 to 1**: *β* = -1.84, *SE* = 2.590, *z* = -0.711, *p* = 0.477
- **3 to 1 vs 1 to 1**: *β* = 1.26, *SE* = 2.488, *z* = 0.508, *p* = 0.612
- **4 to 1 vs 1 to 1**: *β* = 4.87, *SE* = 2.487, *z* = 1.960, *p* = 0.050
- **SNR**: *β* = 0.91, *SE* = 0.334, *z* = 2.717, *p* = 0.007

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | 1.84 | 2.59 | 0.71 | 0.477 | 0.727 | n.s. |
| 1 to 1 - 3 to 1 | -1.26 | 2.49 | -0.51 | 0.612 | 0.727 | n.s. |
| 1 to 1 - 4 to 1 | -4.87 | 2.49 | -1.96 | 0.050 | 0.226 | n.s. |
| 2 to 1 - 3 to 1 | -3.10 | 2.41 | -1.29 | 0.198 | 0.484 | n.s. |
| 2 to 1 - 4 to 1 | -6.71 | 2.45 | -2.74 | 0.006 | 0.036 | * |
| 3 to 1 - 4 to 1 | -3.61 | 2.27 | -1.59 | 0.112 | 0.379 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.00, *p* = 0.136, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 1.09 | 10 | = 0.432 | 0.24 [-0.49, 0.72] | small | n.s. |
| 1 to 1 vs 3 to 1 | 0.42 | 10 | = 0.684 | 0.11 [-0.47, 0.64] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -1.06 | 10 | = 0.432 | -0.31 [-0.80, 0.32] | small | n.s. |
| 2 to 1 vs 3 to 1 | -0.96 | 10 | = 0.432 | -0.13 [-0.89, 0.20] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -2.16 | 10 | = 0.216 | -0.53 [-1.31, -0.08] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -2.01 | 10 | = 0.216 | -0.41 [-0.95, 0.06] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 305.00, BIC = 321.13
- **2 to 1 vs 1 to 1**: *β* = -0.93, *SE* = 0.509, *z* = -1.820, *p* = 0.069
- **3 to 1 vs 1 to 1**: *β* = -1.03, *SE* = 0.489, *z* = -2.107, *p* = 0.035
- **4 to 1 vs 1 to 1**: *β* = -0.21, *SE* = 0.488, *z* = -0.436, *p* = 0.663
- **SNR**: *β* = -0.42, *SE* = 0.063, *z* = -6.587, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | 0.93 | 0.51 | 1.82 | 0.069 | 0.295 | n.s. |
| 1 to 1 - 3 to 1 | 1.03 | 0.49 | 2.11 | 0.035 | 0.193 | n.s. |
| 1 to 1 - 4 to 1 | 0.21 | 0.49 | 0.44 | 0.663 | 0.886 | n.s. |
| 2 to 1 - 3 to 1 | 0.10 | 0.47 | 0.22 | 0.824 | 0.886 | n.s. |
| 2 to 1 - 4 to 1 | -0.71 | 0.48 | -1.49 | 0.137 | 0.358 | n.s. |
| 3 to 1 - 4 to 1 | -0.82 | 0.45 | -1.83 | 0.068 | 0.295 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.56, *p* = 0.221, η²_G = 0.068
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 2.03 | 10 | = 0.211 | 0.60 [-0.11, 1.18] | medium | n.s. |
| 1 to 1 vs 3 to 1 | 0.84 | 10 | = 0.537 | 0.34 [-0.40, 0.71] | small | n.s. |
| 1 to 1 vs 4 to 1 | -0.12 | 10 | = 0.911 | -0.05 [-0.57, 0.54] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | -0.79 | 10 | = 0.537 | -0.21 [-0.55, 0.51] | small | n.s. |
| 2 to 1 vs 4 to 1 | -2.37 | 10 | = 0.211 | -0.66 [-1.06, 0.11] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -1.14 | 10 | = 0.537 | -0.39 [-0.77, 0.21] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 553.21, BIC = 569.15
- **2 to 1 vs 1 to 1**: *β* = 0.48, *SE* = 2.778, *z* = 0.173, *p* = 0.862
- **3 to 1 vs 1 to 1**: *β* = -0.31, *SE* = 2.688, *z* = -0.116, *p* = 0.908
- **4 to 1 vs 1 to 1**: *β* = 1.14, *SE* = 2.939, *z* = 0.388, *p* = 0.698
- **SNR**: *β* = -0.08, *SE* = 0.433, *z* = -0.186, *p* = 0.853

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -0.48 | 2.78 | -0.17 | 0.862 | 0.998 | n.s. |
| 1 to 1 - 3 to 1 | 0.31 | 2.69 | 0.12 | 0.908 | 0.998 | n.s. |
| 1 to 1 - 4 to 1 | -1.14 | 2.94 | -0.39 | 0.698 | 0.998 | n.s. |
| 2 to 1 - 3 to 1 | 0.79 | 2.73 | 0.29 | 0.772 | 0.998 | n.s. |
| 2 to 1 - 4 to 1 | -0.66 | 2.87 | -0.23 | 0.819 | 0.998 | n.s. |
| 3 to 1 - 4 to 1 | -1.45 | 2.85 | -0.51 | 0.611 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.13, *p* = 0.943, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 0.18 | 13 | = 0.929 | 0.05 [-0.55, 0.47] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | -0.09 | 13 | = 0.929 | -0.03 [-0.54, 0.46] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.37 | 13 | = 0.929 | -0.13 [-0.68, 0.48] | negligible | n.s. |
| 2 to 1 vs 3 to 1 | -0.24 | 13 | = 0.929 | -0.08 [-0.46, 0.53] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.72 | 13 | = 0.929 | -0.19 [-0.74, 0.37] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -0.36 | 13 | = 0.929 | -0.11 [-0.69, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 301.88, BIC = 317.82
- **2 to 1 vs 1 to 1**: *β* = -0.41, *SE* = 0.506, *z* = -0.808, *p* = 0.419
- **3 to 1 vs 1 to 1**: *β* = -0.50, *SE* = 0.489, *z* = -1.024, *p* = 0.306
- **4 to 1 vs 1 to 1**: *β* = 0.65, *SE* = 0.530, *z* = 1.216, *p* = 0.224
- **SNR**: *β* = 0.38, *SE* = 0.080, *z* = 4.794, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | 0.41 | 0.51 | 0.81 | 0.419 | 0.666 | n.s. |
| 1 to 1 - 3 to 1 | 0.50 | 0.49 | 1.02 | 0.306 | 0.666 | n.s. |
| 1 to 1 - 4 to 1 | -0.64 | 0.53 | -1.22 | 0.224 | 0.638 | n.s. |
| 2 to 1 - 3 to 1 | 0.09 | 0.50 | 0.18 | 0.853 | 0.853 | n.s. |
| 2 to 1 - 4 to 1 | -1.05 | 0.52 | -2.02 | 0.043 | 0.198 | n.s. |
| 3 to 1 - 4 to 1 | -1.15 | 0.52 | -2.21 | 0.027 | 0.151 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.27, *p* = 0.031, η²_G = 0.077
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | 0.34 | 13 | = 0.741 | 0.08 [-0.53, 0.50] | negligible | n.s. |
| 1 to 1 vs 3 to 1 | 1.36 | 13 | = 0.295 | 0.31 [-0.20, 0.81] | small | n.s. |
| 1 to 1 vs 4 to 1 | -1.58 | 13 | = 0.276 | -0.39 [-1.02, 0.18] | small | n.s. |
| 2 to 1 vs 3 to 1 | 0.86 | 13 | = 0.486 | 0.27 [-0.31, 0.69] | small | n.s. |
| 2 to 1 vs 4 to 1 | -2.55 | 13 | = 0.072 | -0.56 [-1.27, -0.05] | medium | n.s. |
| 3 to 1 vs 4 to 1 | -3.34 | 13 | = 0.032 | -0.87 [-1.31, -0.12] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 698.66, BIC = 714.60
- **2 to 1 vs 1 to 1**: *β* = 15.30, *SE* = 10.890, *z* = 1.405, *p* = 0.160
- **3 to 1 vs 1 to 1**: *β* = 7.04, *SE* = 11.301, *z* = 0.623, *p* = 0.534
- **4 to 1 vs 1 to 1**: *β* = 11.38, *SE* = 11.098, *z* = 1.026, *p* = 0.305
- **SNR**: *β* = -0.57, *SE* = 0.507, *z* = -1.128, *p* = 0.259

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -15.30 | 10.89 | -1.40 | 0.160 | 0.649 | n.s. |
| 1 to 1 - 3 to 1 | -7.04 | 11.30 | -0.62 | 0.534 | 0.898 | n.s. |
| 1 to 1 - 4 to 1 | -11.38 | 11.10 | -1.03 | 0.305 | 0.838 | n.s. |
| 2 to 1 - 3 to 1 | 8.26 | 8.94 | 0.92 | 0.355 | 0.838 | n.s. |
| 2 to 1 - 4 to 1 | 3.91 | 8.76 | 0.45 | 0.655 | 0.898 | n.s. |
| 3 to 1 - 4 to 1 | -4.35 | 8.79 | -0.49 | 0.621 | 0.898 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.40, *p* = 0.751, η²_G = 0.038
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -0.61 | 9 | = 0.866 | -0.33 [-0.91, 0.53] | small | n.s. |
| 1 to 1 vs 3 to 1 | 0.24 | 9 | = 0.866 | 0.12 [-0.64, 0.79] | negligible | n.s. |
| 1 to 1 vs 4 to 1 | -0.43 | 9 | = 0.866 | -0.22 [-0.85, 0.58] | small | n.s. |
| 2 to 1 vs 3 to 1 | 1.18 | 9 | = 0.866 | 0.65 [-0.10, 0.90] | medium | n.s. |
| 2 to 1 vs 4 to 1 | 0.17 | 9 | = 0.866 | 0.07 [-0.35, 0.58] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.01 | 9 | = 0.866 | -0.41 [-0.63, 0.34] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 344.83, BIC = 360.76
- **2 to 1 vs 1 to 1**: *β* = 1.81, *SE* = 0.822, *z* = 2.200, *p* = 0.028
- **3 to 1 vs 1 to 1**: *β* = 1.53, *SE* = 0.861, *z* = 1.774, *p* = 0.076
- **4 to 1 vs 1 to 1**: *β* = 1.98, *SE* = 0.849, *z* = 2.336, *p* = 0.019
- **SNR**: *β* = 0.18, *SE* = 0.041, *z* = 4.403, *p* < .001

_Reference condition: **1 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 2 to 1 | -1.81 | 0.82 | -2.20 | 0.028 | 0.132 | n.s. |
| 1 to 1 - 3 to 1 | -1.53 | 0.86 | -1.77 | 0.076 | 0.271 | n.s. |
| 1 to 1 - 4 to 1 | -1.98 | 0.85 | -2.34 | 0.019 | 0.111 | n.s. |
| 2 to 1 - 3 to 1 | 0.28 | 0.64 | 0.44 | 0.663 | 0.886 | n.s. |
| 2 to 1 - 4 to 1 | -0.18 | 0.63 | -0.28 | 0.779 | 0.886 | n.s. |
| 3 to 1 - 4 to 1 | -0.46 | 0.63 | -0.72 | 0.470 | 0.851 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.85, *p* = 0.001, η²_G = 0.273
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 1 vs 2 to 1 | -4.07 | 9 | = 0.008 | -1.45 [-2.25, -0.32] | large | ** |
| 1 to 1 vs 3 to 1 | -1.88 | 9 | = 0.145 | -0.86 [-1.37, 0.18] | large | n.s. |
| 1 to 1 vs 4 to 1 | -5.43 | 9 | = 0.002 | -1.52 [-2.84, -0.59] | large | ** |
| 2 to 1 vs 3 to 1 | 1.59 | 9 | = 0.176 | 0.57 [-0.52, 0.44] | medium | n.s. |
| 2 to 1 vs 4 to 1 | -0.55 | 9 | = 0.596 | -0.19 [-0.69, 0.25] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -1.85 | 9 | = 0.145 | -0.72 [-0.59, 0.38] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.031). Post-hoc tests revealed:
  - 3 to 1 showed smaller amplitude than 4 to 1 (*d* = -0.87)
**P3b amplitude:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - 1 to 1 showed smaller amplitude than 2 to 1 (*d* = -1.45)
  - 1 to 1 showed smaller amplitude than 4 to 1 (*d* = -1.52)

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
