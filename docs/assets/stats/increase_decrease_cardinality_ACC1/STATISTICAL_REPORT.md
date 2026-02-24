# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:26:12

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
| Decreasing (any step) | 24 | 107.17 ms | 7.82 | 1.60 | [96.00, 116.00] |
| Increasing (any step) | 24 | 102.50 ms | 9.35 | 1.91 | [92.00, 116.00] |
| No Change | 24 | 107.17 ms | 8.98 | 1.83 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing (any step) | 24 | -1.25 µV | 1.23 | 0.25 | [-4.87, 0.33] |
| Increasing (any step) | 24 | -1.03 µV | 0.96 | 0.20 | [-3.80, 0.33] |
| No Change | 24 | -1.28 µV | 1.38 | 0.28 | [-4.83, 0.55] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing (any step) | 24 | 177.17 ms | 14.85 | 3.03 | [144.00, 204.00] |
| Increasing (any step) | 24 | 171.17 ms | 19.02 | 3.88 | [144.00, 204.00] |
| No Change | 24 | 175.67 ms | 16.80 | 3.43 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing (any step) | 24 | -4.92 µV | 1.92 | 0.39 | [-9.28, -1.69] |
| Increasing (any step) | 24 | -5.42 µV | 2.16 | 0.44 | [-9.98, -1.28] |
| No Change | 24 | -4.62 µV | 2.14 | 0.44 | [-9.57, -0.60] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing (any step) | 24 | 111.67 ms | 8.58 | 1.75 | [96.00, 120.00] |
| Increasing (any step) | 24 | 104.17 ms | 9.10 | 1.86 | [96.00, 120.00] |
| No Change | 24 | 108.50 ms | 10.44 | 2.13 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing (any step) | 24 | 1.46 µV | 1.87 | 0.38 | [-2.11, 5.27] |
| Increasing (any step) | 24 | 1.04 µV | 1.62 | 0.33 | [-1.34, 4.54] |
| No Change | 24 | 1.30 µV | 1.94 | 0.40 | [-1.32, 5.73] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing (any step) | 24 | 481.00 ms | 30.35 | 6.20 | [420.00, 532.00] |
| Increasing (any step) | 24 | 481.33 ms | 34.94 | 7.13 | [420.00, 532.00] |
| No Change | 24 | 463.50 ms | 24.86 | 5.08 | [420.00, 516.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing (any step) | 24 | 3.80 µV | 2.95 | 0.60 | [-1.54, 9.02] |
| Increasing (any step) | 24 | 3.28 µV | 3.05 | 0.62 | [-1.58, 8.85] |
| No Change | 24 | 1.14 µV | 2.72 | 0.56 | [-4.85, 5.95] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 484.84, BIC = 498.50
- **Increasing (any step) vs Decreasing (any step)**: *β* = -4.72, *SE* = 1.341, *z* = -3.523, *p* < .001
- **No Change vs Decreasing (any step)**: *β* = -0.07, *SE* = 1.360, *z* = -0.051, *p* = 0.959
- **SNR**: *β* = -0.05, *SE* = 0.311, *z* = -0.163, *p* = 0.871

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 4.73 | 1.34 | 3.52 | < .001 | < .001 | *** |
| Decreasing (any step) - No Change | 0.07 | 1.36 | 0.05 | 0.959 | 0.959 | n.s. |
| Increasing (any step) - No Change | -4.66 | 1.29 | -3.60 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.32, *p* < .001, η²_G = 0.062
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | 3.16 | 23 | = 0.007 | 0.54 [0.18, 1.11] | medium | ** |
| Decreasing (any step) vs No Change | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Increasing (any step) vs No Change | -3.20 | 23 | = 0.007 | -0.51 [-1.12, -0.19] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 174.22, BIC = 187.88
- **Increasing (any step) vs Decreasing (any step)**: *β* = -0.02, *SE* = 0.172, *z* = -0.113, *p* = 0.910
- **No Change vs Decreasing (any step)**: *β* = -0.32, *SE* = 0.175, *z* = -1.803, *p* = 0.071
- **SNR**: *β* = -0.21, *SE* = 0.039, *z* = -5.344, *p* < .001

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 0.02 | 0.17 | 0.11 | 0.910 | 0.910 | n.s. |
| Decreasing (any step) - No Change | 0.31 | 0.17 | 1.80 | 0.071 | 0.199 | n.s. |
| Increasing (any step) - No Change | 0.30 | 0.17 | 1.77 | 0.076 | 0.199 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.15, *p* = 0.325, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | -1.47 | 23 | = 0.296 | -0.20 [-0.73, 0.13] | small | n.s. |
| Decreasing (any step) vs No Change | 0.14 | 23 | = 0.888 | 0.02 [-0.39, 0.45] | negligible | n.s. |
| Increasing (any step) vs No Change | 1.33 | 23 | = 0.296 | 0.21 [-0.16, 0.70] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 584.40, BIC = 598.06
- **Increasing (any step) vs Decreasing (any step)**: *β* = -5.99, *SE* = 2.639, *z* = -2.270, *p* = 0.023
- **No Change vs Decreasing (any step)**: *β* = -1.63, *SE* = 3.124, *z* = -0.520, *p* = 0.603
- **SNR**: *β* = -0.02, *SE* = 0.224, *z* = -0.075, *p* = 0.940

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 5.99 | 2.64 | 2.27 | 0.023 | 0.068 | n.s. |
| Decreasing (any step) - No Change | 1.63 | 3.12 | 0.52 | 0.603 | 0.603 | n.s. |
| Increasing (any step) - No Change | -4.36 | 3.20 | -1.36 | 0.173 | 0.316 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.70, *p* = 0.078, η²_G = 0.023
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | 1.79 | 23 | = 0.133 | 0.35 [-0.07, 0.80] | small | n.s. |
| Decreasing (any step) vs No Change | 0.74 | 23 | = 0.467 | 0.09 [-0.27, 0.58] | negligible | n.s. |
| Increasing (any step) vs No Change | -1.78 | 23 | = 0.133 | -0.25 [-0.80, 0.07] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 243.72, BIC = 257.38
- **Increasing (any step) vs Decreasing (any step)**: *β* = -0.47, *SE* = 0.224, *z* = -2.105, *p* = 0.035
- **No Change vs Decreasing (any step)**: *β* = -0.09, *SE* = 0.275, *z* = -0.338, *p* = 0.736
- **SNR**: *β* = -0.05, *SE* = 0.021, *z* = -2.441, *p* = 0.015

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 0.47 | 0.22 | 2.11 | 0.035 | 0.102 | n.s. |
| Decreasing (any step) - No Change | 0.09 | 0.28 | 0.34 | 0.736 | 0.736 | n.s. |
| Increasing (any step) - No Change | -0.38 | 0.28 | -1.34 | 0.181 | 0.329 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.31, *p* = 0.004, η²_G = 0.026
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | 2.17 | 23 | = 0.060 | 0.25 [0.00, 0.89] | small | n.s. |
| Decreasing (any step) vs No Change | -1.22 | 23 | = 0.233 | -0.15 [-0.68, 0.18] | negligible | n.s. |
| Increasing (any step) vs No Change | -3.86 | 23 | = 0.002 | -0.37 [-1.27, -0.30] | small | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 510.81, BIC = 524.47
- **Increasing (any step) vs Decreasing (any step)**: *β* = -7.48, *SE* = 1.686, *z* = -4.438, *p* < .001
- **No Change vs Decreasing (any step)**: *β* = -3.13, *SE* = 1.692, *z* = -1.852, *p* = 0.064
- **SNR**: *β* = 0.04, *SE* = 0.214, *z* = 0.175, *p* = 0.861

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 7.48 | 1.69 | 4.44 | < .001 | < .001 | *** |
| Decreasing (any step) - No Change | 3.13 | 1.69 | 1.85 | 0.064 | 0.064 | n.s. |
| Increasing (any step) - No Change | -4.35 | 1.68 | -2.58 | 0.010 | 0.020 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 9.64, *p* < .001, η²_G = 0.100
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | 4.01 | 23 | = 0.002 | 0.85 [0.33, 1.31] | large | ** |
| Decreasing (any step) vs No Change | 2.08 | 23 | = 0.049 | 0.33 [-0.02, 0.87] | small | * |
| Increasing (any step) vs No Change | -2.50 | 23 | = 0.030 | -0.44 [-0.96, -0.06] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 220.68, BIC = 234.34
- **Increasing (any step) vs Decreasing (any step)**: *β* = -0.35, *SE* = 0.193, *z* = -1.827, *p* = 0.068
- **No Change vs Decreasing (any step)**: *β* = -0.05, *SE* = 0.194, *z* = -0.250, *p* = 0.803
- **SNR**: *β* = 0.12, *SE* = 0.026, *z* = 4.684, *p* < .001

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 0.35 | 0.19 | 1.83 | 0.068 | 0.190 | n.s. |
| Decreasing (any step) - No Change | 0.05 | 0.19 | 0.25 | 0.803 | 0.803 | n.s. |
| Increasing (any step) - No Change | -0.30 | 0.19 | -1.58 | 0.115 | 0.216 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.76, *p* = 0.183, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | 2.30 | 23 | = 0.092 | 0.24 [0.03, 0.92] | small | n.s. |
| Decreasing (any step) vs No Change | 0.65 | 23 | = 0.522 | 0.08 [-0.29, 0.56] | negligible | n.s. |
| Increasing (any step) vs No Change | -1.06 | 23 | = 0.450 | -0.15 [-0.64, 0.21] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 695.00, BIC = 708.66
- **Increasing (any step) vs Decreasing (any step)**: *β* = -1.83, *SE* = 7.170, *z* = -0.255, *p* = 0.798
- **No Change vs Decreasing (any step)**: *β* = -24.36, *SE* = 8.077, *z* = -3.016, *p* = 0.003
- **SNR**: *β* = -0.78, *SE* = 0.447, *z* = -1.750, *p* = 0.080

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 1.83 | 7.17 | 0.26 | 0.798 | 0.798 | n.s. |
| Decreasing (any step) - No Change | 24.36 | 8.08 | 3.02 | 0.003 | 0.008 | ** |
| Increasing (any step) - No Change | 22.53 | 7.55 | 2.98 | 0.003 | 0.008 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.99, *p* = 0.025, η²_G = 0.073
- Greenhouse-Geisser corrected: *p* = 0.039 (ε = 0.734)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | -0.07 | 23 | = 0.945 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| Decreasing (any step) vs No Change | 2.33 | 23 | = 0.081 | 0.63 [0.03, 0.92] | medium | n.s. |
| Increasing (any step) vs No Change | 2.03 | 23 | = 0.081 | 0.59 [-0.03, 0.86] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 306.37, BIC = 320.03
- **Increasing (any step) vs Decreasing (any step)**: *β* = -0.30, *SE* = 0.359, *z* = -0.836, *p* = 0.403
- **No Change vs Decreasing (any step)**: *β* = -1.96, *SE* = 0.416, *z* = -4.700, *p* < .001
- **SNR**: *β* = 0.08, *SE* = 0.025, *z* = 3.166, *p* = 0.002

_Reference condition: **Decreasing (any step)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing (any step) - Increasing (any step) | 0.30 | 0.36 | 0.84 | 0.403 | 0.403 | n.s. |
| Decreasing (any step) - No Change | 1.96 | 0.42 | 4.70 | < .001 | < .001 | *** |
| Increasing (any step) - No Change | 1.66 | 0.38 | 4.32 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 26.30, *p* < .001, η²_G = 0.140
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.608)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing (any step) vs Increasing (any step) | 3.02 | 23 | = 0.006 | 0.17 [0.16, 1.08] | negligible | ** |
| Decreasing (any step) vs No Change | 5.81 | 23 | < .001 | 0.94 [0.64, 1.74] | large | *** |
| Increasing (any step) vs No Change | 4.62 | 23 | < .001 | 0.74 [0.44, 1.45] | medium | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing (any step) showed greater latency than Increasing (any step) (*d* = 0.54)
  - Increasing (any step) showed smaller latency than No Change (*d* = -0.51)
**N1 latency:** Marginal trend toward condition differences (*p* = 0.078)
**N1 amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Increasing (any step) showed smaller amplitude than No Change (*d* = -0.37)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing (any step) showed greater latency than Increasing (any step) (*d* = 0.85)
  - Decreasing (any step) showed greater latency than No Change (*d* = 0.33)
  - Increasing (any step) showed smaller latency than No Change (*d* = -0.44)
**P3b latency:** Significant main effect of condition (*p* = 0.025) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing (any step) showed greater amplitude than Increasing (any step) (*d* = 0.17)
  - Decreasing (any step) showed greater amplitude than No Change (*d* = 0.94)
  - Increasing (any step) showed greater amplitude than No Change (*d* = 0.74)

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
