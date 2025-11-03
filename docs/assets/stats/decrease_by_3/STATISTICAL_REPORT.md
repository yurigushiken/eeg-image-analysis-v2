# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:37:49

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
| 4 to 1 | 7 | 112.57 ms | 9.64 | 3.64 | [92.00, 120.00] |
| 5 to 2 | 7 | 113.71 ms | 8.90 | 3.36 | [96.00, 120.00] |
| 6 to 3 | 8 | 104.50 ms | 11.40 | 4.03 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 7 | 2.14 µV | 0.96 | 0.36 | [1.11, 4.00] |
| 5 to 2 | 7 | 3.66 µV | 1.58 | 0.60 | [1.56, 6.32] |
| 6 to 3 | 8 | 2.07 µV | 0.42 | 0.15 | [1.59, 2.56] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 18 | 184.44 ms | 11.95 | 2.82 | [168.00, 208.00] |
| 5 to 2 | 24 | 174.50 ms | 18.42 | 3.76 | [148.00, 220.00] |
| 6 to 3 | 24 | 176.17 ms | 17.15 | 3.50 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 18 | -4.25 µV | 1.70 | 0.40 | [-8.09, -1.54] |
| 5 to 2 | 24 | -6.58 µV | 3.05 | 0.62 | [-11.82, -1.41] |
| 6 to 3 | 24 | -6.45 µV | 2.18 | 0.44 | [-10.34, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 119.76 ms | 7.55 | 1.83 | [108.00, 128.00] |
| 5 to 2 | 15 | 114.40 ms | 9.54 | 2.46 | [100.00, 128.00] |
| 6 to 3 | 12 | 112.00 ms | 11.05 | 3.19 | [96.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 5.28 µV | 2.85 | 0.69 | [1.45, 13.38] |
| 5 to 2 | 15 | 3.35 µV | 1.59 | 0.41 | [0.75, 6.20] |
| 6 to 3 | 12 | 3.40 µV | 2.25 | 0.65 | [0.16, 8.17] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 21 | 469.52 ms | 44.69 | 9.75 | [384.00, 528.00] |
| 5 to 2 | 18 | 463.78 ms | 38.53 | 9.08 | [392.00, 524.00] |
| 6 to 3 | 19 | 462.11 ms | 36.52 | 8.38 | [396.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 21 | 6.06 µV | 2.95 | 0.64 | [1.64, 12.03] |
| 5 to 2 | 18 | 5.95 µV | 2.82 | 0.67 | [2.00, 13.53] |
| 6 to 3 | 19 | 6.78 µV | 3.04 | 0.70 | [3.51, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 166.26, BIC = 172.81
- **5 to 2 vs 4 to 1**: *β* = -3.37, *SE* = 3.166, *z* = -1.065, *p* = 0.287
- **6 to 3 vs 4 to 1**: *β* = -7.46, *SE* = 2.683, *z* = -2.779, *p* = 0.005
- **SNR**: *β* = 4.25, *SE* = 1.689, *z* = 2.518, *p* = 0.012

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 3.37 | 3.17 | 1.07 | 0.287 | 0.378 | n.s. |
| 4 to 1 - 6 to 3 | 7.46 | 2.68 | 2.78 | 0.005 | 0.016 | * |
| 5 to 2 - 6 to 3 | 4.08 | 3.27 | 1.25 | 0.211 | 0.378 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.00 | 1 | = 0.500 | 0.63 [-2.30, 2.73] | medium | n.s. |
| 4 to 1 vs 6 to 3 | 1.00 | 1 | = 0.500 | 0.78 [-1.17, 2.23] | medium | n.s. |
| 5 to 2 vs 6 to 3 | 1.00 | 1 | = 0.500 | 0.34 [-2.04, 4.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 71.88, BIC = 78.43
- **5 to 2 vs 4 to 1**: *β* = 1.18, *SE* = 0.383, *z* = 3.085, *p* = 0.002
- **6 to 3 vs 4 to 1**: *β* = -0.19, *SE* = 0.488, *z* = -0.385, *p* = 0.701
- **SNR**: *β* = 0.28, *SE* = 0.037, *z* = 7.590, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | -1.18 | 0.38 | -3.08 | 0.002 | 0.004 | ** |
| 4 to 1 - 6 to 3 | 0.19 | 0.49 | 0.38 | 0.701 | 0.701 | n.s. |
| 5 to 2 - 6 to 3 | 1.37 | 0.40 | 3.44 | < .001 | 0.002 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 0.09 | 1 | = 0.940 | 0.13 [-2.69, 2.32] | negligible | n.s. |
| 4 to 1 vs 6 to 3 | 0.47 | 1 | = 0.940 | 0.61 [-1.34, 1.90] | medium | n.s. |
| 5 to 2 vs 6 to 3 | 0.95 | 1 | = 0.940 | 0.47 [-2.05, 4.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 552.18, BIC = 565.32
- **5 to 2 vs 4 to 1**: *β* = -10.62, *SE* = 3.920, *z* = -2.710, *p* = 0.007
- **6 to 3 vs 4 to 1**: *β* = -8.97, *SE* = 3.928, *z* = -2.283, *p* = 0.022
- **SNR**: *β* = 0.28, *SE* = 0.645, *z* = 0.439, *p* = 0.660

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 10.62 | 3.92 | 2.71 | 0.007 | 0.020 | * |
| 4 to 1 - 6 to 3 | 8.97 | 3.93 | 2.28 | 0.022 | 0.044 | * |
| 5 to 2 - 6 to 3 | -1.66 | 3.32 | -0.50 | 0.617 | 0.617 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.76, *p* = 0.034, η²_G = 0.067
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.36 | 17 | = 0.045 | 0.64 [0.02, 1.09] | medium | * |
| 4 to 1 vs 6 to 3 | 2.43 | 17 | = 0.045 | 0.53 [0.04, 1.11] | medium | * |
| 5 to 2 vs 6 to 3 | -0.39 | 17 | = 0.704 | -0.08 [-0.52, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 278.39, BIC = 291.53
- **5 to 2 vs 4 to 1**: *β* = -1.97, *SE* = 0.472, *z* = -4.162, *p* < .001
- **6 to 3 vs 4 to 1**: *β* = -1.81, *SE* = 0.473, *z* = -3.836, *p* < .001
- **SNR**: *β* = -0.38, *SE* = 0.078, *z* = -4.878, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.97 | 0.47 | 4.16 | < .001 | < .001 | *** |
| 4 to 1 - 6 to 3 | 1.81 | 0.47 | 3.84 | < .001 | < .001 | *** |
| 5 to 2 - 6 to 3 | -0.15 | 0.39 | -0.38 | 0.703 | 0.703 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 19.63, *p* < .001, η²_G = 0.321
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 5.63 | 17 | < .001 | 1.48 [0.64, 2.01] | large | *** |
| 4 to 1 vs 6 to 3 | 4.30 | 17 | < .001 | 1.43 [0.40, 1.63] | large | *** |
| 5 to 2 vs 6 to 3 | -1.50 | 17 | = 0.151 | -0.30 [-0.49, 0.36] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 328.31, BIC = 339.02
- **5 to 2 vs 4 to 1**: *β* = -5.61, *SE* = 3.017, *z* = -1.858, *p* = 0.063
- **6 to 3 vs 4 to 1**: *β* = -6.48, *SE* = 3.341, *z* = -1.939, *p* = 0.053
- **SNR**: *β* = 0.51, *SE* = 0.739, *z* = 0.693, *p* = 0.488

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 5.60 | 3.02 | 1.86 | 0.063 | 0.149 | n.s. |
| 4 to 1 - 6 to 3 | 6.48 | 3.34 | 1.94 | 0.053 | 0.149 | n.s. |
| 5 to 2 - 6 to 3 | 0.87 | 3.29 | 0.27 | 0.791 | 0.791 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.86, *p* = 0.046, η²_G = 0.237
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 4.92 | 7 | = 0.005 | 1.47 [0.23, 1.79] | large | ** |
| 4 to 1 vs 6 to 3 | 1.71 | 7 | = 0.198 | 0.94 [-0.14, 1.43] | large | n.s. |
| 5 to 2 vs 6 to 3 | -0.44 | 7 | = 0.673 | -0.19 [-1.00, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 185.85, BIC = 196.55
- **5 to 2 vs 4 to 1**: *β* = -1.04, *SE* = 0.596, *z* = -1.741, *p* = 0.082
- **6 to 3 vs 4 to 1**: *β* = -0.78, *SE* = 0.648, *z* = -1.203, *p* = 0.229
- **SNR**: *β* = 0.62, *SE* = 0.135, *z* = 4.625, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.04 | 0.60 | 1.74 | 0.082 | 0.226 | n.s. |
| 4 to 1 - 6 to 3 | 0.78 | 0.65 | 1.20 | 0.229 | 0.406 | n.s. |
| 5 to 2 - 6 to 3 | -0.26 | 0.61 | -0.42 | 0.673 | 0.673 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.98, *p* = 0.013, η²_G = 0.226
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.46 | 7 | = 0.065 | 1.07 [0.05, 1.50] | large | n.s. |
| 4 to 1 vs 6 to 3 | 3.41 | 7 | = 0.034 | 0.90 [-0.04, 1.59] | large | * |
| 5 to 2 vs 6 to 3 | -0.41 | 7 | = 0.694 | -0.15 [-0.77, 0.76] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 600.13, BIC = 612.50
- **5 to 2 vs 4 to 1**: *β* = -6.38, *SE* = 11.250, *z* = -0.568, *p* = 0.570
- **6 to 3 vs 4 to 1**: *β* = -6.39, *SE* = 11.281, *z* = -0.567, *p* = 0.571
- **SNR**: *β* = -0.00, *SE* = 1.052, *z* = -0.002, *p* = 0.999

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 6.39 | 11.25 | 0.57 | 0.570 | 0.921 | n.s. |
| 4 to 1 - 6 to 3 | 6.39 | 11.28 | 0.57 | 0.571 | 0.921 | n.s. |
| 5 to 2 - 6 to 3 | 0.01 | 11.55 | 0.00 | 0.999 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.634, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.04 | 16 | = 0.712 | 0.28 [-0.33, 0.68] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.38 | 16 | = 0.712 | 0.12 [-0.42, 0.61] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -0.55 | 16 | = 0.712 | -0.18 [-0.65, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 251.92, BIC = 264.29
- **5 to 2 vs 4 to 1**: *β* = -0.05, *SE* = 0.444, *z* = -0.104, *p* = 0.917
- **6 to 3 vs 4 to 1**: *β* = 0.84, *SE* = 0.452, *z* = 1.865, *p* = 0.062
- **SNR**: *β* = 0.22, *SE* = 0.048, *z* = 4.497, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.05 | 0.44 | 0.10 | 0.917 | 0.917 | n.s. |
| 4 to 1 - 6 to 3 | -0.84 | 0.45 | -1.87 | 0.062 | 0.137 | n.s. |
| 5 to 2 - 6 to 3 | -0.89 | 0.45 | -1.98 | 0.048 | 0.137 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.384, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 0.63 | 16 | = 0.541 | 0.13 [-0.35, 0.65] | negligible | n.s. |
| 4 to 1 vs 6 to 3 | -0.68 | 16 | = 0.541 | -0.13 [-0.68, 0.35] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -1.73 | 16 | = 0.311 | -0.26 [-0.95, 0.12] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.034). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 5 to 2 (*d* = 0.64)
  - 4 to 1 showed greater latency than 6 to 3 (*d* = 0.53)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 1.48)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.43)
**P1 latency:** Significant main effect of condition (*p* = 0.046). Post-hoc tests revealed:
  - 4 to 1 showed greater latency than 5 to 2 (*d* = 1.47)
**P1 amplitude:** Significant main effect of condition (*p* = 0.013). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 0.90)

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
