# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:27:43

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
| Decreasing 2 to 1 | 7 | 100.57 ms | 14.50 | 5.48 | [88.00, 120.00] |
| Decreasing 3 to 1 | 10 | 106.40 ms | 12.54 | 3.96 | [88.00, 120.00] |
| Increasing 1 to 2 | 14 | 106.29 ms | 12.33 | 3.29 | [88.00, 120.00] |
| Increasing 1 to 3 | 18 | 107.11 ms | 13.20 | 3.11 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 7 | 4.34 µV | 1.88 | 0.71 | [1.14, 7.15] |
| Decreasing 3 to 1 | 10 | 2.61 µV | 1.28 | 0.40 | [1.23, 5.34] |
| Increasing 1 to 2 | 14 | 2.77 µV | 1.90 | 0.51 | [0.61, 5.82] |
| Increasing 1 to 3 | 18 | 2.91 µV | 2.26 | 0.53 | [0.53, 8.62] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 16 | 180.75 ms | 13.16 | 3.29 | [160.00, 212.00] |
| Decreasing 3 to 1 | 19 | 186.11 ms | 16.57 | 3.80 | [156.00, 212.00] |
| Increasing 1 to 2 | 22 | 171.82 ms | 17.57 | 3.74 | [148.00, 208.00] |
| Increasing 1 to 3 | 24 | 173.67 ms | 21.87 | 4.47 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 16 | -5.25 µV | 2.62 | 0.65 | [-10.79, -1.72] |
| Decreasing 3 to 1 | 19 | -4.99 µV | 2.64 | 0.60 | [-10.41, -1.40] |
| Increasing 1 to 2 | 22 | -5.81 µV | 2.13 | 0.45 | [-9.87, -2.38] |
| Increasing 1 to 3 | 24 | -6.15 µV | 2.65 | 0.54 | [-12.30, -2.18] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 18 | 119.33 ms | 9.53 | 2.25 | [100.00, 128.00] |
| Decreasing 3 to 1 | 21 | 116.76 ms | 10.09 | 2.20 | [100.00, 128.00] |
| Increasing 1 to 2 | 11 | 113.09 ms | 10.60 | 3.20 | [100.00, 128.00] |
| Increasing 1 to 3 | 11 | 108.00 ms | 8.58 | 2.59 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 18 | 4.64 µV | 2.47 | 0.58 | [1.48, 9.13] |
| Decreasing 3 to 1 | 21 | 3.82 µV | 1.76 | 0.38 | [1.64, 9.14] |
| Increasing 1 to 2 | 11 | 1.89 µV | 0.82 | 0.25 | [0.78, 3.14] |
| Increasing 1 to 3 | 11 | 3.10 µV | 2.03 | 0.61 | [0.91, 7.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 496.80 ms | 28.80 | 6.44 | [432.00, 536.00] |
| Decreasing 3 to 1 | 20 | 484.20 ms | 27.42 | 6.13 | [444.00, 536.00] |
| Increasing 1 to 2 | 16 | 475.00 ms | 44.41 | 11.10 | [416.00, 536.00] |
| Increasing 1 to 3 | 20 | 470.40 ms | 37.62 | 8.41 | [416.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 2 to 1 | 20 | 6.12 µV | 3.11 | 0.70 | [1.72, 11.08] |
| Decreasing 3 to 1 | 20 | 6.15 µV | 3.13 | 0.70 | [2.57, 16.27] |
| Increasing 1 to 2 | 16 | 6.05 µV | 2.79 | 0.70 | [2.32, 11.52] |
| Increasing 1 to 3 | 20 | 6.30 µV | 3.72 | 0.83 | [1.71, 14.25] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 398.90, BIC = 412.14
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 5.92, *SE* = 5.979, *z* = 0.990, *p* = 0.322
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = 6.65, *SE* = 5.529, *z* = 1.203, *p* = 0.229
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = 7.22, *SE* = 5.337, *z* = 1.353, *p* = 0.176
- **SNR**: *β* = 1.11, *SE* = 1.157, *z* = 0.962, *p* = 0.336

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -5.92 | 5.98 | -0.99 | 0.322 | 0.789 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | -6.65 | 5.53 | -1.20 | 0.229 | 0.727 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | -7.22 | 5.34 | -1.35 | 0.176 | 0.687 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -0.73 | 5.04 | -0.14 | 0.885 | 0.990 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -1.30 | 4.79 | -0.27 | 0.786 | 0.990 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.57 | 4.17 | -0.14 | 0.891 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 173.68, BIC = 186.92
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -1.47, *SE* = 0.545, *z* = -2.693, *p* = 0.007
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.94, *SE* = 0.492, *z* = -1.900, *p* = 0.057
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -1.15, *SE* = 0.478, *z* = -2.395, *p* = 0.017
- **SNR**: *β* = 0.87, *SE* = 0.106, *z* = 8.183, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 1.47 | 0.55 | 2.69 | 0.007 | 0.042 | * |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.93 | 0.49 | 1.90 | 0.057 | 0.211 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 1.15 | 0.48 | 2.40 | 0.017 | 0.080 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -0.53 | 0.45 | -1.18 | 0.239 | 0.560 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.32 | 0.42 | -0.77 | 0.439 | 0.685 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 0.21 | 0.37 | 0.58 | 0.565 | 0.685 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 686.03, BIC = 702.79
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = 4.79, *SE* = 4.335, *z* = 1.106, *p* = 0.269
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -10.13, *SE* = 4.259, *z* = -2.378, *p* = 0.017
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -8.11, *SE* = 4.318, *z* = -1.878, *p* = 0.060
- **SNR**: *β* = 0.20, *SE* = 0.704, *z* = 0.279, *p* = 0.781

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | -4.79 | 4.33 | -1.11 | 0.269 | 0.465 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 10.13 | 4.26 | 2.38 | 0.017 | 0.068 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 8.11 | 4.32 | 1.88 | 0.060 | 0.170 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 14.92 | 4.09 | 3.65 | < .001 | 0.002 | ** |
| Decreasing 3 to 1 - Increasing 1 to 3 | 12.90 | 4.24 | 3.04 | 0.002 | 0.012 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | -2.02 | 3.73 | -0.54 | 0.589 | 0.589 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.01, *p* = 0.014, η²_G = 0.089
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -1.46 | 13 | = 0.252 | -0.36 [-0.99, 0.21] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.07 | 13 | = 0.119 | 0.51 [0.01, 1.22] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 1.29 | 13 | = 0.265 | 0.37 [-0.12, 0.99] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 3.06 | 13 | = 0.054 | 0.78 [0.31, 1.44] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.65 | 13 | = 0.060 | 0.62 [0.12, 1.18] | medium | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -0.30 | 13 | = 0.766 | -0.07 [-0.59, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 338.71, BIC = 355.47
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.26, *SE* = 0.524, *z* = -0.490, *p* = 0.624
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.45, *SE* = 0.517, *z* = -0.865, *p* = 0.387
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.38, *SE* = 0.524, *z* = -0.727, *p* = 0.467
- **SNR**: *β* = -0.48, *SE* = 0.083, *z* = -5.769, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.26 | 0.52 | 0.49 | 0.624 | 0.980 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.45 | 0.52 | 0.86 | 0.387 | 0.947 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.38 | 0.52 | 0.73 | 0.467 | 0.957 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 0.19 | 0.49 | 0.39 | 0.699 | 0.980 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.12 | 0.51 | 0.24 | 0.808 | 0.980 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.07 | 0.45 | -0.15 | 0.882 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.79, *p* = 0.165, η²_G = 0.049
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.41 | 13 | = 0.688 | -0.09 [-0.69, 0.47] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.45 | 13 | = 0.303 | 0.39 [-0.12, 1.04] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 1.34 | 13 | = 0.303 | 0.40 [-0.09, 1.04] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.52 | 13 | = 0.303 | 0.47 [-0.14, 0.86] | small | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.57 | 13 | = 0.303 | 0.47 [-0.08, 0.93] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.42 | 13 | = 0.688 | 0.08 [-0.30, 0.59] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 458.76, BIC = 473.53
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -1.94, *SE* = 2.775, *z* = -0.700, *p* = 0.484
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -6.10, *SE* = 3.459, *z* = -1.762, *p* = 0.078
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -11.40, *SE* = 3.333, *z* = -3.421, *p* = 0.001
- **SNR**: *β* = 0.21, *SE* = 0.401, *z* = 0.515, *p* = 0.607

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 1.94 | 2.77 | 0.70 | 0.484 | 0.484 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 6.10 | 3.46 | 1.76 | 0.078 | 0.277 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 11.40 | 3.33 | 3.42 | < .001 | 0.004 | ** |
| Decreasing 3 to 1 - Increasing 1 to 2 | 4.15 | 3.28 | 1.27 | 0.206 | 0.381 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 9.46 | 3.22 | 2.94 | 0.003 | 0.016 | * |
| Increasing 1 to 2 - Increasing 1 to 3 | 5.31 | 3.66 | 1.45 | 0.148 | 0.381 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.81, *p* = 0.033, η²_G = 0.331
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.75 | 5 | = 0.486 | 0.50 [-0.45, 0.61] | small | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 2.36 | 5 | = 0.145 | 1.19 [-0.03, 1.78] | large | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 3.31 | 5 | = 0.127 | 1.67 [0.19, 1.99] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 1.08 | 5 | = 0.394 | 0.71 [-0.17, 1.38] | medium | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.27 | 5 | = 0.145 | 1.20 [0.09, 1.67] | large | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 1.15 | 5 | = 0.394 | 0.48 [-0.38, 1.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 231.13, BIC = 245.91
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.30, *SE* = 0.460, *z* = -0.643, *p* = 0.520
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -1.80, *SE* = 0.568, *z* = -3.174, *p* = 0.002
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.98, *SE* = 0.551, *z* = -1.774, *p* = 0.076
- **SNR**: *β* = 0.40, *SE* = 0.069, *z* = 5.866, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.30 | 0.46 | 0.64 | 0.520 | 0.520 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 1.80 | 0.57 | 3.17 | 0.002 | 0.009 | ** |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.98 | 0.55 | 1.77 | 0.076 | 0.271 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 1.51 | 0.53 | 2.83 | 0.005 | 0.023 | * |
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.68 | 0.53 | 1.30 | 0.194 | 0.433 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.83 | 0.60 | -1.36 | 0.172 | 0.433 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.12, *p* = 0.002, η²_G = 0.427
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 0.55 | 5 | = 0.606 | 0.17 [-0.19, 0.90] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 4.15 | 5 | = 0.027 | 2.15 [0.27, 2.38] | large | * |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 2.99 | 5 | = 0.061 | 1.02 [-0.06, 1.56] | large | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 4.59 | 5 | = 0.027 | 2.31 [0.22, 2.06] | large | * |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.83 | 5 | = 0.191 | 0.95 [-0.19, 1.25] | large | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.41 | 5 | = 0.260 | -0.84 [-1.39, 0.54] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 762.77, BIC = 779.08
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -11.95, *SE* = 10.195, *z* = -1.172, *p* = 0.241
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -20.02, *SE* = 10.624, *z* = -1.885, *p* = 0.059
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -25.01, *SE* = 10.035, *z* = -2.492, *p* = 0.013
- **SNR**: *β* = -0.26, *SE* = 0.834, *z* = -0.316, *p* = 0.752

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 11.95 | 10.19 | 1.17 | 0.241 | 0.587 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 20.02 | 10.62 | 1.88 | 0.059 | 0.264 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 25.01 | 10.04 | 2.49 | 0.013 | 0.074 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | 8.07 | 10.93 | 0.74 | 0.460 | 0.708 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | 13.06 | 10.16 | 1.29 | 0.198 | 0.587 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | 4.99 | 10.65 | 0.47 | 0.640 | 0.708 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.11, *p* = 0.114, η²_G = 0.107
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | 1.69 | 13 | = 0.230 | 0.62 [-0.11, 0.89] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 1.73 | 13 | = 0.230 | 0.63 [-0.16, 0.95] | medium | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | 3.26 | 13 | = 0.037 | 0.97 [-0.06, 1.03] | large | * |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 0.48 | 13 | = 0.671 | 0.19 [-0.46, 0.61] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.16 | 13 | = 0.403 | 0.46 [-0.30, 0.70] | small | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | 0.43 | 13 | = 0.671 | 0.18 [-0.46, 0.70] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 368.82, BIC = 385.13
- **Decreasing 3 to 1 vs Decreasing 2 to 1**: *β* = -0.69, *SE* = 0.690, *z* = -0.997, *p* = 0.319
- **Increasing 1 to 2 vs Decreasing 2 to 1**: *β* = -0.27, *SE* = 0.714, *z* = -0.377, *p* = 0.706
- **Increasing 1 to 3 vs Decreasing 2 to 1**: *β* = -0.01, *SE* = 0.682, *z* = -0.007, *p* = 0.994
- **SNR**: *β* = 0.29, *SE* = 0.060, *z* = 4.769, *p* < .001

_Reference condition: **Decreasing 2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 2 to 1 - Decreasing 3 to 1 | 0.69 | 0.69 | 1.00 | 0.319 | 0.900 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 2 | 0.27 | 0.71 | 0.38 | 0.706 | 0.975 | n.s. |
| Decreasing 2 to 1 - Increasing 1 to 3 | 0.00 | 0.68 | 0.01 | 0.994 | 0.994 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 2 | -0.42 | 0.74 | -0.57 | 0.569 | 0.966 | n.s. |
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.68 | 0.68 | -1.00 | 0.318 | 0.900 | n.s. |
| Increasing 1 to 2 - Increasing 1 to 3 | -0.26 | 0.73 | -0.36 | 0.717 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.759, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 2 to 1 vs Decreasing 3 to 1 | -0.12 | 13 | = 0.909 | -0.03 [-0.50, 0.46] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 2 | 0.50 | 13 | = 0.814 | 0.16 [-0.44, 0.63] | negligible | n.s. |
| Decreasing 2 to 1 vs Increasing 1 to 3 | -0.58 | 13 | = 0.814 | -0.16 [-0.60, 0.43] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 2 | 0.55 | 13 | = 0.814 | 0.18 [-0.39, 0.68] | negligible | n.s. |
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.42 | 13 | = 0.814 | -0.12 [-0.55, 0.45] | negligible | n.s. |
| Increasing 1 to 2 vs Increasing 1 to 3 | -1.33 | 13 | = 0.814 | -0.31 [-0.95, 0.24] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.014) (no significant pairwise comparisons)
**P1 latency:** Significant main effect of condition (*p* = 0.033) (no significant pairwise comparisons)
**P1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Decreasing 2 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 2.15)
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 2 (*d* = 2.31)

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
