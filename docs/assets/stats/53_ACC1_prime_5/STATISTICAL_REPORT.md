# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:14:16

---

## 1. Analysis Overview

**Total Measurements:** 291
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

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 23 | 175.83 ms | 20.13 | 4.20 | [144.00, 212.00] |
| 5b3 | 17 | 178.82 ms | 20.53 | 4.98 | [148.00, 212.00] |
| 5c3 | 21 | 175.43 ms | 16.01 | 3.49 | [144.00, 200.00] |
| 5d3 | 21 | 176.19 ms | 16.12 | 3.52 | [144.00, 212.00] |
| 5e3 | 15 | 182.40 ms | 17.02 | 4.40 | [152.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 23 | -6.39 µV | 3.37 | 0.70 | [-12.31, -1.32] |
| 5b3 | 17 | -7.87 µV | 4.67 | 1.13 | [-17.81, -0.91] |
| 5c3 | 21 | -6.45 µV | 4.39 | 0.96 | [-16.11, 0.21] |
| 5d3 | 21 | -6.75 µV | 2.85 | 0.62 | [-12.24, -2.19] |
| 5e3 | 15 | -9.14 µV | 4.18 | 1.08 | [-17.26, 0.77] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 23 | 100.52 ms | 13.50 | 2.82 | [80.00, 120.00] |
| 5b3 | 17 | 101.18 ms | 15.41 | 3.74 | [80.00, 120.00] |
| 5c3 | 21 | 106.48 ms | 14.00 | 3.05 | [80.00, 120.00] |
| 5d3 | 21 | 100.76 ms | 16.33 | 3.56 | [80.00, 120.00] |
| 5e3 | 15 | 100.27 ms | 13.48 | 3.48 | [80.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 23 | 3.73 µV | 3.12 | 0.65 | [-0.76, 11.41] |
| 5b3 | 17 | 2.67 µV | 5.82 | 1.41 | [-8.18, 15.68] |
| 5c3 | 21 | 4.66 µV | 3.76 | 0.82 | [-0.47, 12.00] |
| 5d3 | 21 | 2.69 µV | 2.77 | 0.60 | [-2.12, 7.51] |
| 5e3 | 15 | 3.43 µV | 5.74 | 1.48 | [-7.39, 13.79] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 23 | 477.39 ms | 26.41 | 5.51 | [432.00, 524.00] |
| 5b3 | 17 | 471.29 ms | 28.01 | 6.79 | [428.00, 524.00] |
| 5c3 | 21 | 473.90 ms | 33.46 | 7.30 | [428.00, 524.00] |
| 5d3 | 21 | 472.19 ms | 32.26 | 7.04 | [428.00, 524.00] |
| 5e3 | 15 | 477.87 ms | 31.56 | 8.15 | [428.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 23 | 5.08 µV | 4.47 | 0.93 | [-2.92, 15.42] |
| 5b3 | 17 | 5.21 µV | 4.65 | 1.13 | [-5.83, 12.00] |
| 5c3 | 21 | 6.97 µV | 4.85 | 1.06 | [-1.92, 20.14] |
| 5d3 | 21 | 7.68 µV | 4.16 | 0.91 | [-1.55, 14.21] |
| 5e3 | 15 | 6.39 µV | 6.02 | 1.55 | [-5.37, 18.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 846.56, BIC = 867.16
- **5b3 vs 5a3**: *β* = 3.03, *SE* = 5.427, *z* = 0.558, *p* = 0.577
- **5c3 vs 5a3**: *β* = -0.57, *SE* = 5.118, *z* = -0.111, *p* = 0.912
- **5d3 vs 5a3**: *β* = 0.33, *SE* = 5.093, *z* = 0.064, *p* = 0.949
- **5e3 vs 5a3**: *β* = 6.08, *SE* = 5.648, *z* = 1.077, *p* = 0.282
- **SNR**: *β* = -0.26, *SE* = 0.931, *z* = -0.279, *p* = 0.780

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -3.03 | 5.43 | -0.56 | 0.577 | 0.994 | n.s. |
| 5a3 - 5c3 | 0.57 | 5.12 | 0.11 | 0.912 | 0.998 | n.s. |
| 5a3 - 5d3 | -0.33 | 5.09 | -0.06 | 0.949 | 0.998 | n.s. |
| 5a3 - 5e3 | -6.08 | 5.65 | -1.08 | 0.282 | 0.949 | n.s. |
| 5b3 - 5c3 | 3.60 | 5.56 | 0.65 | 0.518 | 0.994 | n.s. |
| 5b3 - 5d3 | 2.70 | 5.54 | 0.49 | 0.626 | 0.994 | n.s. |
| 5b3 - 5e3 | -3.05 | 6.05 | -0.50 | 0.614 | 0.994 | n.s. |
| 5c3 - 5d3 | -0.89 | 5.23 | -0.17 | 0.864 | 0.998 | n.s. |
| 5c3 - 5e3 | -6.65 | 5.78 | -1.15 | 0.250 | 0.944 | n.s. |
| 5d3 - 5e3 | -5.76 | 5.76 | -1.00 | 0.318 | 0.953 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.73, *p* = 0.581, η²_G = 0.061
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -0.43 | 7 | = 0.814 | -0.17 [-0.63, 0.44] | negligible | n.s. |
| 5a3 vs 5c3 | -0.53 | 7 | = 0.814 | -0.32 [-0.42, 0.52] | small | n.s. |
| 5a3 vs 5d3 | -1.68 | 7 | = 0.706 | -0.49 [-0.46, 0.45] | small | n.s. |
| 5a3 vs 5e3 | -1.66 | 7 | = 0.706 | -0.75 [-0.69, 0.42] | medium | n.s. |
| 5b3 vs 5c3 | -0.18 | 7 | = 0.863 | -0.09 [-0.46, 0.65] | negligible | n.s. |
| 5b3 vs 5d3 | -0.68 | 7 | = 0.814 | -0.25 [-0.35, 0.77] | small | n.s. |
| 5b3 vs 5e3 | -1.26 | 7 | = 0.742 | -0.45 [-1.12, 0.28] | small | n.s. |
| 5c3 vs 5d3 | -0.36 | 7 | = 0.814 | -0.21 [-0.59, 0.37] | small | n.s. |
| 5c3 vs 5e3 | -1.13 | 7 | = 0.742 | -0.50 [-0.73, 0.55] | medium | n.s. |
| 5d3 vs 5e3 | -0.68 | 7 | = 0.814 | -0.26 [-0.67, 0.54] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 510.25, BIC = 530.85
- **5b3 vs 5a3**: *β* = -1.35, *SE* = 0.920, *z* = -1.462, *p* = 0.144
- **5c3 vs 5a3**: *β* = -0.68, *SE* = 0.868, *z* = -0.781, *p* = 0.435
- **5d3 vs 5a3**: *β* = -0.38, *SE* = 0.859, *z* = -0.445, *p* = 0.656
- **5e3 vs 5a3**: *β* = -2.73, *SE* = 0.956, *z* = -2.852, *p* = 0.004
- **SNR**: *β* = -1.06, *SE* = 0.169, *z* = -6.274, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 1.35 | 0.92 | 1.46 | 0.144 | 0.662 | n.s. |
| 5a3 - 5c3 | 0.68 | 0.87 | 0.78 | 0.435 | 0.898 | n.s. |
| 5a3 - 5d3 | 0.38 | 0.86 | 0.45 | 0.656 | 0.898 | n.s. |
| 5a3 - 5e3 | 2.73 | 0.96 | 2.85 | 0.004 | 0.043 | * |
| 5b3 - 5c3 | -0.67 | 0.95 | -0.71 | 0.480 | 0.898 | n.s. |
| 5b3 - 5d3 | -0.96 | 0.94 | -1.03 | 0.305 | 0.838 | n.s. |
| 5b3 - 5e3 | 1.38 | 1.03 | 1.34 | 0.179 | 0.693 | n.s. |
| 5c3 - 5d3 | -0.30 | 0.88 | -0.33 | 0.739 | 0.898 | n.s. |
| 5c3 - 5e3 | 2.05 | 0.99 | 2.07 | 0.039 | 0.272 | n.s. |
| 5d3 - 5e3 | 2.34 | 0.98 | 2.39 | 0.017 | 0.142 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.37, *p* = 0.023, η²_G = 0.194
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.60 | 7 | = 0.630 | 0.22 [-0.10, 1.02] | small | n.s. |
| 5a3 vs 5c3 | -1.37 | 7 | = 0.303 | -0.56 [-0.42, 0.52] | medium | n.s. |
| 5a3 vs 5d3 | 0.28 | 7 | = 0.789 | 0.09 [-0.31, 0.60] | negligible | n.s. |
| 5a3 vs 5e3 | 2.81 | 7 | = 0.161 | 1.17 [-0.01, 1.19] | large | n.s. |
| 5b3 vs 5c3 | -1.41 | 7 | = 0.303 | -0.60 [-0.75, 0.36] | medium | n.s. |
| 5b3 vs 5d3 | -0.84 | 7 | = 0.538 | -0.14 [-1.22, -0.01] | negligible | n.s. |
| 5b3 vs 5e3 | 1.58 | 7 | = 0.303 | 0.62 [-0.31, 1.09] | medium | n.s. |
| 5c3 vs 5d3 | 1.45 | 7 | = 0.303 | 0.56 [-0.33, 0.64] | medium | n.s. |
| 5c3 vs 5e3 | 2.67 | 7 | = 0.161 | 1.37 [-0.32, 0.98] | large | n.s. |
| 5d3 vs 5e3 | 1.99 | 7 | = 0.288 | 0.91 [-0.15, 1.12] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 805.42, BIC = 826.02
- **5b3 vs 5a3**: *β* = 0.74, *SE* = 4.444, *z* = 0.166, *p* = 0.868
- **5c3 vs 5a3**: *β* = 5.92, *SE* = 4.167, *z* = 1.420, *p* = 0.156
- **5d3 vs 5a3**: *β* = 0.53, *SE* = 4.184, *z* = 0.126, *p* = 0.900
- **5e3 vs 5a3**: *β* = -0.20, *SE* = 4.606, *z* = -0.043, *p* = 0.965
- **SNR**: *β* = 0.65, *SE* = 1.495, *z* = 0.434, *p* = 0.664

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -0.74 | 4.44 | -0.17 | 0.868 | 1.000 | n.s. |
| 5a3 - 5c3 | -5.92 | 4.17 | -1.42 | 0.156 | 0.816 | n.s. |
| 5a3 - 5d3 | -0.53 | 4.18 | -0.13 | 0.900 | 1.000 | n.s. |
| 5a3 - 5e3 | 0.20 | 4.61 | 0.04 | 0.965 | 1.000 | n.s. |
| 5b3 - 5c3 | -5.18 | 4.53 | -1.14 | 0.253 | 0.870 | n.s. |
| 5b3 - 5d3 | 0.21 | 4.58 | 0.05 | 0.963 | 1.000 | n.s. |
| 5b3 - 5e3 | 0.94 | 4.92 | 0.19 | 0.849 | 1.000 | n.s. |
| 5c3 - 5d3 | 5.39 | 4.29 | 1.26 | 0.209 | 0.856 | n.s. |
| 5c3 - 5e3 | 6.12 | 4.70 | 1.30 | 0.194 | 0.856 | n.s. |
| 5d3 - 5e3 | 0.73 | 4.74 | 0.15 | 0.878 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.974, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.13 | 7 | = 1.000 | 0.07 [-0.66, 0.41] | negligible | n.s. |
| 5a3 vs 5c3 | -0.69 | 7 | = 1.000 | -0.31 [-0.72, 0.23] | small | n.s. |
| 5a3 vs 5d3 | -0.10 | 7 | = 1.000 | -0.03 [-0.53, 0.38] | negligible | n.s. |
| 5a3 vs 5e3 | 0.00 | 7 | = 1.000 | 0.00 [-0.54, 0.57] | negligible | n.s. |
| 5b3 vs 5c3 | -0.64 | 7 | = 1.000 | -0.35 [-0.74, 0.37] | small | n.s. |
| 5b3 vs 5d3 | -0.15 | 7 | = 1.000 | -0.10 [-0.45, 0.66] | negligible | n.s. |
| 5b3 vs 5e3 | -0.25 | 7 | = 1.000 | -0.07 [-0.82, 0.53] | negligible | n.s. |
| 5c3 vs 5d3 | 0.49 | 7 | = 1.000 | 0.23 [-0.20, 0.78] | small | n.s. |
| 5c3 vs 5e3 | 0.51 | 7 | = 1.000 | 0.27 [-0.31, 1.00] | small | n.s. |
| 5d3 vs 5e3 | 0.05 | 7 | = 1.000 | 0.03 [-0.63, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 551.68, BIC = 572.28
- **5b3 vs 5a3**: *β* = -1.31, *SE* = 1.210, *z* = -1.080, *p* = 0.280
- **5c3 vs 5a3**: *β* = 0.81, *SE* = 1.141, *z* = 0.707, *p* = 0.479
- **5d3 vs 5a3**: *β* = -0.56, *SE* = 1.143, *z* = -0.490, *p* = 0.624
- **5e3 vs 5a3**: *β* = -0.53, *SE* = 1.255, *z* = -0.423, *p* = 0.672
- **SNR**: *β* = 1.54, *SE* = 0.389, *z* = 3.971, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 1.31 | 1.21 | 1.08 | 0.280 | 0.928 | n.s. |
| 5a3 - 5c3 | -0.81 | 1.14 | -0.71 | 0.479 | 0.980 | n.s. |
| 5a3 - 5d3 | 0.56 | 1.14 | 0.49 | 0.624 | 0.981 | n.s. |
| 5a3 - 5e3 | 0.53 | 1.26 | 0.42 | 0.672 | 0.981 | n.s. |
| 5b3 - 5c3 | -2.11 | 1.23 | -1.71 | 0.087 | 0.595 | n.s. |
| 5b3 - 5d3 | -0.75 | 1.25 | -0.60 | 0.549 | 0.981 | n.s. |
| 5b3 - 5e3 | -0.78 | 1.34 | -0.58 | 0.562 | 0.981 | n.s. |
| 5c3 - 5d3 | 1.37 | 1.18 | 1.16 | 0.245 | 0.920 | n.s. |
| 5c3 - 5e3 | 1.34 | 1.28 | 1.05 | 0.296 | 0.928 | n.s. |
| 5d3 - 5e3 | -0.03 | 1.29 | -0.02 | 0.982 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.566, η²_G = 0.075
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.12 | 7 | = 0.933 | 0.04 [-0.27, 0.82] | negligible | n.s. |
| 5a3 vs 5c3 | 0.30 | 7 | = 0.933 | 0.11 [-0.59, 0.34] | negligible | n.s. |
| 5a3 vs 5d3 | 1.61 | 7 | = 0.772 | 0.83 [-0.20, 0.72] | large | n.s. |
| 5a3 vs 5e3 | 0.81 | 7 | = 0.772 | 0.53 [-0.51, 0.60] | medium | n.s. |
| 5b3 vs 5c3 | 0.09 | 7 | = 0.933 | 0.03 [-0.82, 0.30] | negligible | n.s. |
| 5b3 vs 5d3 | 0.95 | 7 | = 0.772 | 0.53 [-0.47, 0.64] | medium | n.s. |
| 5b3 vs 5e3 | 0.64 | 7 | = 0.772 | 0.34 [-0.67, 0.67] | small | n.s. |
| 5c3 vs 5d3 | 1.53 | 7 | = 0.772 | 0.77 [-0.14, 0.85] | medium | n.s. |
| 5c3 vs 5e3 | 0.77 | 7 | = 0.772 | 0.45 [-0.63, 0.64] | small | n.s. |
| 5d3 vs 5e3 | -0.65 | 7 | = 0.772 | -0.29 [-0.64, 0.57] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 947.28, BIC = 967.87
- **5b3 vs 5a3**: *β* = -5.58, *SE* = 9.419, *z* = -0.592, *p* = 0.554
- **5c3 vs 5a3**: *β* = -3.96, *SE* = 8.888, *z* = -0.445, *p* = 0.656
- **5d3 vs 5a3**: *β* = -4.45, *SE* = 8.905, *z* = -0.500, *p* = 0.617
- **5e3 vs 5a3**: *β* = -0.56, *SE* = 9.805, *z* = -0.057, *p* = 0.954
- **SNR**: *β* = -1.43, *SE* = 1.248, *z* = -1.143, *p* = 0.253

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 5.58 | 9.42 | 0.59 | 0.554 | 1.000 | n.s. |
| 5a3 - 5c3 | 3.96 | 8.89 | 0.45 | 0.656 | 1.000 | n.s. |
| 5a3 - 5d3 | 4.45 | 8.91 | 0.50 | 0.617 | 1.000 | n.s. |
| 5a3 - 5e3 | 0.56 | 9.80 | 0.06 | 0.954 | 1.000 | n.s. |
| 5b3 - 5c3 | -1.62 | 9.64 | -0.17 | 0.866 | 1.000 | n.s. |
| 5b3 - 5d3 | -1.13 | 9.60 | -0.12 | 0.906 | 1.000 | n.s. |
| 5b3 - 5e3 | -5.02 | 10.51 | -0.48 | 0.633 | 1.000 | n.s. |
| 5c3 - 5d3 | 0.49 | 9.14 | 0.05 | 0.957 | 1.000 | n.s. |
| 5c3 - 5e3 | -3.39 | 9.96 | -0.34 | 0.733 | 1.000 | n.s. |
| 5d3 - 5e3 | -3.89 | 10.07 | -0.39 | 0.699 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.612, η²_G = 0.076
- Greenhouse-Geisser corrected: *p* = 0.547 (ε = 0.607)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 1.57 | 7 | = 0.532 | 0.81 [-0.30, 0.78] | large | n.s. |
| 5a3 vs 5c3 | -0.03 | 7 | = 0.979 | -0.01 [-0.38, 0.56] | negligible | n.s. |
| 5a3 vs 5d3 | 0.54 | 7 | = 0.944 | 0.22 [-0.36, 0.56] | small | n.s. |
| 5a3 vs 5e3 | -0.20 | 7 | = 0.944 | -0.13 [-0.60, 0.51] | negligible | n.s. |
| 5b3 vs 5c3 | -1.23 | 7 | = 0.648 | -0.66 [-0.58, 0.52] | medium | n.s. |
| 5b3 vs 5d3 | -1.93 | 7 | = 0.532 | -0.45 [-0.79, 0.33] | small | n.s. |
| 5b3 vs 5e3 | -1.68 | 7 | = 0.532 | -0.81 [-0.83, 0.53] | large | n.s. |
| 5c3 vs 5d3 | 0.33 | 7 | = 0.944 | 0.20 [-0.36, 0.61] | negligible | n.s. |
| 5c3 vs 5e3 | -0.20 | 7 | = 0.944 | -0.09 [-0.71, 0.56] | negligible | n.s. |
| 5d3 vs 5e3 | -0.53 | 7 | = 0.944 | -0.30 [-0.76, 0.45] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 574.53, BIC = 595.13
- **5b3 vs 5a3**: *β* = 0.29, *SE* = 1.232, *z* = 0.234, *p* = 0.815
- **5c3 vs 5a3**: *β* = 1.97, *SE* = 1.151, *z* = 1.714, *p* = 0.086
- **5d3 vs 5a3**: *β* = 2.40, *SE* = 1.144, *z* = 2.095, *p* = 0.036
- **5e3 vs 5a3**: *β* = 1.05, *SE* = 1.280, *z* = 0.822, *p* = 0.411
- **SNR**: *β* = 0.21, *SE* = 0.175, *z* = 1.183, *p* = 0.237

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -0.29 | 1.23 | -0.23 | 0.815 | 0.929 | n.s. |
| 5a3 - 5c3 | -1.97 | 1.15 | -1.71 | 0.086 | 0.557 | n.s. |
| 5a3 - 5d3 | -2.40 | 1.14 | -2.10 | 0.036 | 0.308 | n.s. |
| 5a3 - 5e3 | -1.05 | 1.28 | -0.82 | 0.411 | 0.929 | n.s. |
| 5b3 - 5c3 | -1.68 | 1.26 | -1.33 | 0.182 | 0.755 | n.s. |
| 5b3 - 5d3 | -2.11 | 1.26 | -1.68 | 0.093 | 0.557 | n.s. |
| 5b3 - 5e3 | -0.76 | 1.39 | -0.55 | 0.583 | 0.929 | n.s. |
| 5c3 - 5d3 | -0.42 | 1.18 | -0.36 | 0.720 | 0.929 | n.s. |
| 5c3 - 5e3 | 0.92 | 1.32 | 0.70 | 0.484 | 0.929 | n.s. |
| 5d3 - 5e3 | 1.35 | 1.32 | 1.02 | 0.308 | 0.890 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.76, *p* = 0.166, η²_G = 0.098
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -0.20 | 7 | = 0.918 | -0.08 [-0.56, 0.51] | negligible | n.s. |
| 5a3 vs 5c3 | -1.43 | 7 | = 0.349 | -0.59 [-1.09, -0.07] | medium | n.s. |
| 5a3 vs 5d3 | -1.81 | 7 | = 0.314 | -0.75 [-0.91, 0.05] | medium | n.s. |
| 5a3 vs 5e3 | 0.13 | 7 | = 0.918 | 0.05 [-0.63, 0.48] | negligible | n.s. |
| 5b3 vs 5c3 | -1.76 | 7 | = 0.314 | -0.56 [-0.79, 0.34] | medium | n.s. |
| 5b3 vs 5d3 | -2.41 | 7 | = 0.314 | -0.75 [-1.02, 0.14] | medium | n.s. |
| 5b3 vs 5e3 | 0.35 | 7 | = 0.918 | 0.12 [-0.77, 0.57] | negligible | n.s. |
| 5c3 vs 5d3 | -0.11 | 7 | = 0.918 | -0.02 [-0.72, 0.26] | negligible | n.s. |
| 5c3 vs 5e3 | 1.38 | 7 | = 0.349 | 0.57 [-0.40, 0.89] | medium | n.s. |
| 5d3 vs 5e3 | 1.74 | 7 | = 0.314 | 0.68 [-0.37, 0.86] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.023) (no significant pairwise comparisons)

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
