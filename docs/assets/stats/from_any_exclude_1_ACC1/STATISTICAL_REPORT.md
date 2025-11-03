# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:41:45

---

## 1. Analysis Overview

**Total Measurements:** 480
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| from 2 | 13 | 103.08 ms | 7.33 | 2.03 | [92.00, 112.00] |
| from 3 | 14 | 102.86 ms | 7.09 | 1.90 | [92.00, 112.00] |
| from 4 | 13 | 104.92 ms | 6.76 | 1.88 | [92.00, 112.00] |
| from 5 | 21 | 103.43 ms | 7.30 | 1.59 | [92.00, 112.00] |
| from 6 | 18 | 104.00 ms | 7.00 | 1.65 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 13 | -1.92 µV | 1.29 | 0.36 | [-4.46, -0.38] |
| from 3 | 14 | -1.93 µV | 0.98 | 0.26 | [-3.47, -0.37] |
| from 4 | 13 | -1.88 µV | 1.35 | 0.38 | [-4.85, -0.35] |
| from 5 | 21 | -2.21 µV | 1.23 | 0.27 | [-6.01, -0.40] |
| from 6 | 18 | -2.12 µV | 1.45 | 0.34 | [-6.83, -0.38] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 22 | 168.18 ms | 17.95 | 3.83 | [140.00, 208.00] |
| from 3 | 22 | 167.45 ms | 17.99 | 3.83 | [140.00, 208.00] |
| from 4 | 24 | 172.17 ms | 18.02 | 3.68 | [140.00, 208.00] |
| from 5 | 23 | 168.17 ms | 14.04 | 2.93 | [140.00, 196.00] |
| from 6 | 24 | 173.50 ms | 17.37 | 3.55 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 22 | -5.78 µV | 1.69 | 0.36 | [-10.28, -3.40] |
| from 3 | 22 | -5.69 µV | 1.99 | 0.42 | [-9.91, -2.34] |
| from 4 | 24 | -5.72 µV | 2.56 | 0.52 | [-12.11, -2.09] |
| from 5 | 23 | -5.84 µV | 2.28 | 0.48 | [-9.50, -1.21] |
| from 6 | 24 | -5.96 µV | 2.12 | 0.43 | [-10.13, -3.03] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 15 | 105.87 ms | 7.54 | 1.95 | [96.00, 116.00] |
| from 3 | 11 | 107.27 ms | 7.55 | 2.28 | [96.00, 116.00] |
| from 4 | 12 | 108.67 ms | 5.87 | 1.69 | [100.00, 116.00] |
| from 5 | 16 | 109.00 ms | 7.66 | 1.91 | [96.00, 116.00] |
| from 6 | 16 | 109.75 ms | 7.59 | 1.90 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 15 | 1.97 µV | 1.49 | 0.38 | [0.22, 5.24] |
| from 3 | 11 | 2.15 µV | 1.84 | 0.56 | [0.16, 6.01] |
| from 4 | 12 | 2.23 µV | 1.25 | 0.36 | [0.36, 3.65] |
| from 5 | 16 | 2.52 µV | 1.13 | 0.28 | [0.25, 4.48] |
| from 6 | 16 | 2.70 µV | 1.71 | 0.43 | [1.09, 7.46] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 18 | 469.56 ms | 38.00 | 8.96 | [428.00, 536.00] |
| from 3 | 18 | 483.11 ms | 29.54 | 6.96 | [432.00, 536.00] |
| from 4 | 19 | 484.63 ms | 30.91 | 7.09 | [436.00, 536.00] |
| from 5 | 18 | 481.56 ms | 28.16 | 6.64 | [432.00, 536.00] |
| from 6 | 19 | 488.21 ms | 34.70 | 7.96 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 18 | 5.38 µV | 2.66 | 0.63 | [1.67, 10.63] |
| from 3 | 18 | 4.89 µV | 2.83 | 0.67 | [1.33, 10.28] |
| from 4 | 19 | 4.99 µV | 2.75 | 0.63 | [0.73, 9.14] |
| from 5 | 18 | 5.08 µV | 2.36 | 0.56 | [2.17, 10.98] |
| from 6 | 19 | 4.97 µV | 2.46 | 0.56 | [0.61, 9.98] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 520.26, BIC = 539.21
- **from 3 vs from 2**: *β* = 0.12, *SE* = 1.856, *z* = 0.063, *p* = 0.950
- **from 4 vs from 2**: *β* = 1.77, *SE* = 1.902, *z* = 0.929, *p* = 0.353
- **from 5 vs from 2**: *β* = 0.83, *SE* = 1.765, *z* = 0.469, *p* = 0.639
- **from 6 vs from 2**: *β* = 1.26, *SE* = 1.771, *z* = 0.709, *p* = 0.478
- **SNR**: *β* = -0.10, *SE* = 0.377, *z* = -0.270, *p* = 0.787

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.12 | 1.86 | -0.06 | 0.950 | 0.995 | n.s. |
| from 2 - from 4 | -1.77 | 1.90 | -0.93 | 0.353 | 0.987 | n.s. |
| from 2 - from 5 | -0.83 | 1.76 | -0.47 | 0.639 | 0.995 | n.s. |
| from 2 - from 6 | -1.26 | 1.77 | -0.71 | 0.478 | 0.995 | n.s. |
| from 3 - from 4 | -1.65 | 1.85 | -0.89 | 0.374 | 0.987 | n.s. |
| from 3 - from 5 | -0.71 | 1.69 | -0.42 | 0.674 | 0.995 | n.s. |
| from 3 - from 6 | -1.14 | 1.75 | -0.65 | 0.516 | 0.995 | n.s. |
| from 4 - from 5 | 0.94 | 1.75 | 0.54 | 0.591 | 0.995 | n.s. |
| from 4 - from 6 | 0.51 | 1.80 | 0.28 | 0.776 | 0.995 | n.s. |
| from 5 - from 6 | -0.43 | 1.61 | -0.27 | 0.791 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.27, *p* = 0.091, η²_G = 0.068
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -2.29 | 6 | = 0.260 | -0.54 [-0.91, 0.54] | medium | n.s. |
| from 2 vs from 4 | -2.83 | 6 | = 0.260 | -0.63 [-1.94, -0.06] | medium | n.s. |
| from 2 vs from 5 | -2.12 | 6 | = 0.260 | -0.48 [-0.64, 0.64] | small | n.s. |
| from 2 vs from 6 | -1.55 | 6 | = 0.431 | -0.47 [-0.87, 0.49] | small | n.s. |
| from 3 vs from 4 | -0.55 | 6 | = 0.862 | -0.10 [-0.58, 0.85] | negligible | n.s. |
| from 3 vs from 5 | 0.35 | 6 | = 0.909 | 0.10 [-0.74, 0.48] | negligible | n.s. |
| from 3 vs from 6 | 0.24 | 6 | = 0.909 | 0.10 [-0.91, 0.45] | negligible | n.s. |
| from 4 vs from 5 | 1.00 | 6 | = 0.712 | 0.21 [-0.55, 0.72] | small | n.s. |
| from 4 vs from 6 | 0.60 | 6 | = 0.862 | 0.20 [-0.49, 0.96] | negligible | n.s. |
| from 5 vs from 6 | 0.00 | 6 | = 1.000 | 0.00 [-0.61, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 204.48, BIC = 223.44
- **from 3 vs from 2**: *β* = 0.26, *SE* = 0.259, *z* = 1.017, *p* = 0.309
- **from 4 vs from 2**: *β* = 0.14, *SE* = 0.265, *z* = 0.523, *p* = 0.601
- **from 5 vs from 2**: *β* = -0.07, *SE* = 0.247, *z* = -0.262, *p* = 0.794
- **from 6 vs from 2**: *β* = -0.36, *SE* = 0.247, *z* = -1.464, *p* = 0.143
- **SNR**: *β* = -0.34, *SE* = 0.053, *z* = -6.502, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.26 | 0.26 | -1.02 | 0.309 | 0.843 | n.s. |
| from 2 - from 4 | -0.14 | 0.26 | -0.52 | 0.601 | 0.936 | n.s. |
| from 2 - from 5 | 0.06 | 0.25 | 0.26 | 0.794 | 0.936 | n.s. |
| from 2 - from 6 | 0.36 | 0.25 | 1.46 | 0.143 | 0.710 | n.s. |
| from 3 - from 4 | 0.12 | 0.26 | 0.48 | 0.631 | 0.936 | n.s. |
| from 3 - from 5 | 0.33 | 0.24 | 1.37 | 0.170 | 0.729 | n.s. |
| from 3 - from 6 | 0.62 | 0.24 | 2.55 | 0.011 | 0.103 | n.s. |
| from 4 - from 5 | 0.20 | 0.24 | 0.83 | 0.405 | 0.875 | n.s. |
| from 4 - from 6 | 0.50 | 0.25 | 2.00 | 0.046 | 0.343 | n.s. |
| from 5 - from 6 | 0.30 | 0.23 | 1.32 | 0.188 | 0.729 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.98, *p* = 0.130, η²_G = 0.061
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.24 | 6 | = 0.864 | -0.09 [-0.70, 0.73] | negligible | n.s. |
| from 2 vs from 4 | -0.32 | 6 | = 0.864 | -0.12 [-0.61, 0.94] | negligible | n.s. |
| from 2 vs from 5 | 1.00 | 6 | = 0.507 | 0.25 [-0.32, 0.99] | small | n.s. |
| from 2 vs from 6 | 1.62 | 6 | = 0.373 | 0.49 [-0.63, 0.72] | small | n.s. |
| from 3 vs from 4 | -0.18 | 6 | = 0.864 | -0.05 [-0.61, 0.82] | negligible | n.s. |
| from 3 vs from 5 | 1.36 | 6 | = 0.373 | 0.34 [0.16, 1.59] | small | n.s. |
| from 3 vs from 6 | 2.11 | 6 | = 0.373 | 0.61 [-0.17, 1.27] | medium | n.s. |
| from 4 vs from 5 | 1.44 | 6 | = 0.373 | 0.34 [-0.07, 1.32] | small | n.s. |
| from 4 vs from 6 | 3.32 | 6 | = 0.160 | 0.58 [-0.07, 1.54] | medium | n.s. |
| from 5 vs from 6 | 1.50 | 6 | = 0.373 | 0.23 [-0.62, 0.42] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 913.08, BIC = 935.04
- **from 3 vs from 2**: *β* = -1.71, *SE* = 2.768, *z* = -0.617, *p* = 0.537
- **from 4 vs from 2**: *β* = 2.22, *SE* = 2.685, *z* = 0.827, *p* = 0.408
- **from 5 vs from 2**: *β* = -0.97, *SE* = 2.733, *z* = -0.357, *p* = 0.721
- **from 6 vs from 2**: *β* = 3.83, *SE* = 2.683, *z* = 1.427, *p* = 0.154
- **SNR**: *β* = 1.03, *SE* = 0.295, *z* = 3.513, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 1.71 | 2.77 | 0.62 | 0.537 | 0.954 | n.s. |
| from 2 - from 4 | -2.22 | 2.68 | -0.83 | 0.408 | 0.928 | n.s. |
| from 2 - from 5 | 0.97 | 2.73 | 0.36 | 0.721 | 0.954 | n.s. |
| from 2 - from 6 | -3.83 | 2.68 | -1.43 | 0.154 | 0.716 | n.s. |
| from 3 - from 4 | -3.93 | 2.70 | -1.45 | 0.146 | 0.716 | n.s. |
| from 3 - from 5 | -0.73 | 2.71 | -0.27 | 0.787 | 0.954 | n.s. |
| from 3 - from 6 | -5.54 | 2.71 | -2.04 | 0.041 | 0.342 | n.s. |
| from 4 - from 5 | 3.19 | 2.65 | 1.21 | 0.228 | 0.789 | n.s. |
| from 4 - from 6 | -1.61 | 2.61 | -0.62 | 0.538 | 0.954 | n.s. |
| from 5 - from 6 | -4.80 | 2.66 | -1.81 | 0.071 | 0.483 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.561, η²_G = 0.012
- Greenhouse-Geisser corrected: *p* = 0.510 (ε = 0.651)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.27 | 20 | = 0.881 | 0.05 [-0.40, 0.51] | negligible | n.s. |
| from 2 vs from 4 | -0.61 | 20 | = 0.782 | -0.10 [-0.58, 0.31] | negligible | n.s. |
| from 2 vs from 5 | -0.45 | 20 | = 0.820 | -0.11 [-0.55, 0.36] | negligible | n.s. |
| from 2 vs from 6 | -1.12 | 20 | = 0.750 | -0.25 [-0.69, 0.21] | small | n.s. |
| from 3 vs from 4 | -1.06 | 20 | = 0.750 | -0.15 [-0.68, 0.22] | negligible | n.s. |
| from 3 vs from 5 | -0.77 | 20 | = 0.761 | -0.16 [-0.51, 0.38] | negligible | n.s. |
| from 3 vs from 6 | -1.58 | 20 | = 0.750 | -0.30 [-0.72, 0.18] | small | n.s. |
| from 4 vs from 5 | -0.06 | 20 | = 0.951 | -0.01 [-0.28, 0.59] | negligible | n.s. |
| from 4 vs from 6 | -0.76 | 20 | = 0.761 | -0.16 [-0.52, 0.33] | negligible | n.s. |
| from 5 vs from 6 | -1.15 | 20 | = 0.750 | -0.15 [-0.82, 0.08] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 399.73, BIC = 421.69
- **from 3 vs from 2**: *β* = 0.35, *SE* = 0.301, *z* = 1.157, *p* = 0.247
- **from 4 vs from 2**: *β* = -0.07, *SE* = 0.292, *z* = -0.225, *p* = 0.822
- **from 5 vs from 2**: *β* = -0.02, *SE* = 0.297, *z* = -0.070, *p* = 0.944
- **from 6 vs from 2**: *β* = -0.36, *SE* = 0.291, *z* = -1.232, *p* = 0.218
- **SNR**: *β* = -0.19, *SE* = 0.032, *z* = -5.884, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.35 | 0.30 | -1.16 | 0.247 | 0.848 | n.s. |
| from 2 - from 4 | 0.07 | 0.29 | 0.22 | 0.822 | 0.994 | n.s. |
| from 2 - from 5 | 0.02 | 0.30 | 0.07 | 0.944 | 0.994 | n.s. |
| from 2 - from 6 | 0.36 | 0.29 | 1.23 | 0.218 | 0.848 | n.s. |
| from 3 - from 4 | 0.41 | 0.29 | 1.41 | 0.158 | 0.788 | n.s. |
| from 3 - from 5 | 0.37 | 0.29 | 1.25 | 0.210 | 0.848 | n.s. |
| from 3 - from 6 | 0.71 | 0.29 | 2.40 | 0.016 | 0.151 | n.s. |
| from 4 - from 5 | -0.04 | 0.29 | -0.16 | 0.877 | 0.994 | n.s. |
| from 4 - from 6 | 0.29 | 0.28 | 1.04 | 0.301 | 0.848 | n.s. |
| from 5 - from 6 | 0.34 | 0.29 | 1.17 | 0.241 | 0.848 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.51, *p* = 0.731, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.18 | 20 | = 0.928 | -0.03 [-0.50, 0.42] | negligible | n.s. |
| from 2 vs from 4 | 0.35 | 20 | = 0.917 | 0.07 [-0.38, 0.50] | negligible | n.s. |
| from 2 vs from 5 | 1.02 | 20 | = 0.917 | 0.18 [-0.24, 0.68] | negligible | n.s. |
| from 2 vs from 6 | 0.91 | 20 | = 0.917 | 0.16 [-0.25, 0.64] | negligible | n.s. |
| from 3 vs from 4 | 0.63 | 20 | = 0.917 | 0.09 [-0.27, 0.62] | negligible | n.s. |
| from 3 vs from 5 | 1.48 | 20 | = 0.917 | 0.20 [-0.16, 0.74] | negligible | n.s. |
| from 3 vs from 6 | 1.15 | 20 | = 0.917 | 0.18 [-0.15, 0.75] | negligible | n.s. |
| from 4 vs from 5 | 0.47 | 20 | = 0.917 | 0.08 [-0.41, 0.46] | negligible | n.s. |
| from 4 vs from 6 | 0.36 | 20 | = 0.917 | 0.07 [-0.30, 0.55] | negligible | n.s. |
| from 5 vs from 6 | -0.09 | 20 | = 0.928 | -0.01 [-0.31, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 464.01, BIC = 482.00
- **from 3 vs from 2**: *β* = 0.75, *SE* = 1.993, *z* = 0.374, *p* = 0.708
- **from 4 vs from 2**: *β* = 2.01, *SE* = 1.911, *z* = 1.052, *p* = 0.293
- **from 5 vs from 2**: *β* = 2.56, *SE* = 1.815, *z* = 1.410, *p* = 0.158
- **from 6 vs from 2**: *β* = 3.08, *SE* = 1.782, *z* = 1.730, *p* = 0.084
- **SNR**: *β* = 0.64, *SE* = 0.415, *z* = 1.548, *p* = 0.122

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.75 | 1.99 | -0.37 | 0.708 | 0.980 | n.s. |
| from 2 - from 4 | -2.01 | 1.91 | -1.05 | 0.293 | 0.911 | n.s. |
| from 2 - from 5 | -2.56 | 1.82 | -1.41 | 0.158 | 0.788 | n.s. |
| from 2 - from 6 | -3.08 | 1.78 | -1.73 | 0.084 | 0.582 | n.s. |
| from 3 - from 4 | -1.27 | 2.09 | -0.61 | 0.545 | 0.980 | n.s. |
| from 3 - from 5 | -1.81 | 1.97 | -0.92 | 0.358 | 0.930 | n.s. |
| from 3 - from 6 | -2.34 | 1.99 | -1.18 | 0.239 | 0.888 | n.s. |
| from 4 - from 5 | -0.55 | 1.94 | -0.28 | 0.777 | 0.980 | n.s. |
| from 4 - from 6 | -1.07 | 1.89 | -0.57 | 0.571 | 0.980 | n.s. |
| from 5 - from 6 | -0.52 | 1.79 | -0.29 | 0.770 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.59, *p* = 0.226, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.41 | 4 | = 0.792 | -0.12 [-0.81, 0.63] | negligible | n.s. |
| from 2 vs from 4 | 2.45 | 4 | = 0.298 | 0.35 [-0.91, 0.45] | small | n.s. |
| from 2 vs from 5 | 0.00 | 4 | = 1.000 | 0.00 [-1.04, 0.17] | negligible | n.s. |
| from 2 vs from 6 | -0.41 | 4 | = 0.792 | -0.12 [-1.04, 0.22] | negligible | n.s. |
| from 3 vs from 4 | 2.14 | 4 | = 0.298 | 0.52 [-0.84, 0.84] | medium | n.s. |
| from 3 vs from 5 | 1.00 | 4 | = 0.561 | 0.15 [-1.24, 0.37] | negligible | n.s. |
| from 3 vs from 6 | nan | 4 | n/a | 0.00 [-0.53, 1.03] | negligible | n.s. |
| from 4 vs from 5 | -1.50 | 4 | = 0.468 | -0.40 [-1.03, 0.43] | small | n.s. |
| from 4 vs from 6 | -2.14 | 4 | = 0.298 | -0.52 [-0.87, 0.49] | medium | n.s. |
| from 5 vs from 6 | -1.00 | 4 | = 0.561 | -0.15 [-0.87, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 182.60, BIC = 200.59
- **from 3 vs from 2**: *β* = -0.42, *SE* = 0.254, *z* = -1.661, *p* = 0.097
- **from 4 vs from 2**: *β* = 0.07, *SE* = 0.244, *z* = 0.298, *p* = 0.765
- **from 5 vs from 2**: *β* = 0.18, *SE* = 0.232, *z* = 0.755, *p* = 0.450
- **from 6 vs from 2**: *β* = 0.76, *SE* = 0.228, *z* = 3.331, *p* = 0.001
- **SNR**: *β* = 0.42, *SE* = 0.056, *z* = 7.537, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.42 | 0.25 | 1.66 | 0.097 | 0.334 | n.s. |
| from 2 - from 4 | -0.07 | 0.24 | -0.30 | 0.765 | 0.896 | n.s. |
| from 2 - from 5 | -0.18 | 0.23 | -0.76 | 0.450 | 0.834 | n.s. |
| from 2 - from 6 | -0.76 | 0.23 | -3.33 | < .001 | 0.008 | ** |
| from 3 - from 4 | -0.49 | 0.27 | -1.86 | 0.063 | 0.279 | n.s. |
| from 3 - from 5 | -0.60 | 0.25 | -2.37 | 0.018 | 0.103 | n.s. |
| from 3 - from 6 | -1.18 | 0.25 | -4.66 | < .001 | < .001 | *** |
| from 4 - from 5 | -0.10 | 0.25 | -0.42 | 0.678 | 0.896 | n.s. |
| from 4 - from 6 | -0.69 | 0.24 | -2.84 | 0.005 | 0.036 | * |
| from 5 - from 6 | -0.58 | 0.23 | -2.55 | 0.011 | 0.072 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.78, *p* = 0.183, η²_G = 0.160
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.07 | 4 | = 0.951 | -0.03 [-0.65, 0.78] | negligible | n.s. |
| from 2 vs from 4 | 0.55 | 4 | = 0.872 | 0.24 [-0.81, 0.54] | small | n.s. |
| from 2 vs from 5 | -0.34 | 4 | = 0.937 | -0.16 [-1.21, 0.04] | negligible | n.s. |
| from 2 vs from 6 | -1.75 | 4 | = 0.384 | -0.77 [-1.56, -0.15] | medium | n.s. |
| from 3 vs from 4 | 0.58 | 4 | = 0.872 | 0.25 [-1.08, 0.61] | small | n.s. |
| from 3 vs from 5 | -0.17 | 4 | = 0.951 | -0.10 [-1.20, 0.40] | negligible | n.s. |
| from 3 vs from 6 | -2.17 | 4 | = 0.384 | -0.69 [-1.66, 0.10] | medium | n.s. |
| from 4 vs from 5 | -1.60 | 4 | = 0.384 | -0.79 [-2.03, -0.21] | medium | n.s. |
| from 4 vs from 6 | -2.22 | 4 | = 0.384 | -1.20 [-1.18, 0.24] | large | n.s. |
| from 5 vs from 6 | -1.57 | 4 | = 0.384 | -0.85 [-1.04, 0.22] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 894.50, BIC = 914.68
- **from 3 vs from 2**: *β* = 13.05, *SE* = 8.443, *z* = 1.546, *p* = 0.122
- **from 4 vs from 2**: *β* = 12.59, *SE* = 8.476, *z* = 1.486, *p* = 0.137
- **from 5 vs from 2**: *β* = 10.27, *SE* = 8.475, *z* = 1.212, *p* = 0.225
- **from 6 vs from 2**: *β* = 18.10, *SE* = 8.343, *z* = 2.170, *p* = 0.030
- **SNR**: *β* = 1.05, *SE* = 0.681, *z* = 1.538, *p* = 0.124

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -13.05 | 8.44 | -1.55 | 0.122 | 0.690 | n.s. |
| from 2 - from 4 | -12.59 | 8.48 | -1.49 | 0.137 | 0.693 | n.s. |
| from 2 - from 5 | -10.27 | 8.47 | -1.21 | 0.225 | 0.833 | n.s. |
| from 2 - from 6 | -18.10 | 8.34 | -2.17 | 0.030 | 0.263 | n.s. |
| from 3 - from 4 | 0.46 | 8.38 | 0.05 | 0.956 | 0.983 | n.s. |
| from 3 - from 5 | 2.78 | 8.49 | 0.33 | 0.743 | 0.983 | n.s. |
| from 3 - from 6 | -5.05 | 8.35 | -0.61 | 0.545 | 0.970 | n.s. |
| from 4 - from 5 | 2.32 | 8.36 | 0.28 | 0.781 | 0.983 | n.s. |
| from 4 - from 6 | -5.51 | 8.26 | -0.67 | 0.505 | 0.970 | n.s. |
| from 5 - from 6 | -7.83 | 8.32 | -0.94 | 0.346 | 0.922 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.98, *p* = 0.426, η²_G = 0.028
- Greenhouse-Geisser corrected: *p* = 0.392 (ε = 0.542)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.92 | 15 | = 0.752 | -0.33 [-0.83, 0.22] | small | n.s. |
| from 2 vs from 4 | -1.82 | 15 | = 0.445 | -0.45 [-1.01, 0.11] | small | n.s. |
| from 2 vs from 5 | -0.91 | 15 | = 0.752 | -0.23 [-0.80, 0.25] | small | n.s. |
| from 2 vs from 6 | -2.31 | 15 | = 0.356 | -0.35 [-1.03, 0.05] | small | n.s. |
| from 3 vs from 4 | -0.55 | 15 | = 0.764 | -0.13 [-0.60, 0.43] | negligible | n.s. |
| from 3 vs from 5 | 0.42 | 15 | = 0.764 | 0.12 [-0.43, 0.64] | negligible | n.s. |
| from 3 vs from 6 | -0.09 | 15 | = 0.928 | -0.03 [-0.63, 0.40] | negligible | n.s. |
| from 4 vs from 5 | 1.38 | 15 | = 0.624 | 0.26 [-0.31, 0.73] | small | n.s. |
| from 4 vs from 6 | 0.41 | 15 | = 0.764 | 0.10 [-0.68, 0.32] | negligible | n.s. |
| from 5 vs from 6 | -0.56 | 15 | = 0.764 | -0.14 [-0.61, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 340.71, BIC = 360.89
- **from 3 vs from 2**: *β* = -0.64, *SE* = 0.354, *z* = -1.818, *p* = 0.069
- **from 4 vs from 2**: *β* = -0.56, *SE* = 0.360, *z* = -1.562, *p* = 0.118
- **from 5 vs from 2**: *β* = -0.47, *SE* = 0.357, *z* = -1.326, *p* = 0.185
- **from 6 vs from 2**: *β* = -0.25, *SE* = 0.351, *z* = -0.717, *p* = 0.474
- **SNR**: *β* = 0.19, *SE* = 0.032, *z* = 5.999, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.64 | 0.35 | 1.82 | 0.069 | 0.511 | n.s. |
| from 2 - from 4 | 0.56 | 0.36 | 1.56 | 0.118 | 0.678 | n.s. |
| from 2 - from 5 | 0.47 | 0.36 | 1.33 | 0.185 | 0.805 | n.s. |
| from 2 - from 6 | 0.25 | 0.35 | 0.72 | 0.474 | 0.960 | n.s. |
| from 3 - from 4 | -0.08 | 0.35 | -0.23 | 0.818 | 0.960 | n.s. |
| from 3 - from 5 | -0.17 | 0.36 | -0.48 | 0.631 | 0.960 | n.s. |
| from 3 - from 6 | -0.39 | 0.35 | -1.12 | 0.263 | 0.882 | n.s. |
| from 4 - from 5 | -0.09 | 0.35 | -0.26 | 0.798 | 0.960 | n.s. |
| from 4 - from 6 | -0.31 | 0.35 | -0.89 | 0.372 | 0.939 | n.s. |
| from 5 - from 6 | -0.22 | 0.35 | -0.63 | 0.526 | 0.960 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.33, *p* = 0.854, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.772 (ε = 0.648)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 1.15 | 15 | = 0.945 | 0.16 [-0.24, 0.81] | negligible | n.s. |
| from 2 vs from 4 | 0.26 | 15 | = 0.945 | 0.04 [-0.47, 0.60] | negligible | n.s. |
| from 2 vs from 5 | 1.25 | 15 | = 0.945 | 0.12 [-0.19, 0.87] | negligible | n.s. |
| from 2 vs from 6 | 0.07 | 15 | = 0.945 | 0.02 [-0.43, 0.60] | negligible | n.s. |
| from 3 vs from 4 | -1.08 | 15 | = 0.945 | -0.12 [-0.84, 0.21] | negligible | n.s. |
| from 3 vs from 5 | -0.32 | 15 | = 0.945 | -0.05 [-0.61, 0.45] | negligible | n.s. |
| from 3 vs from 6 | -0.65 | 15 | = 0.945 | -0.16 [-0.69, 0.34] | negligible | n.s. |
| from 4 vs from 5 | 0.43 | 15 | = 0.945 | 0.08 [-0.50, 0.53] | negligible | n.s. |
| from 4 vs from 6 | -0.13 | 15 | = 0.945 | -0.03 [-0.55, 0.45] | negligible | n.s. |
| from 5 vs from 6 | -0.51 | 15 | = 0.945 | -0.12 [-0.52, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Marginal trend toward condition differences (*p* = 0.091)

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
