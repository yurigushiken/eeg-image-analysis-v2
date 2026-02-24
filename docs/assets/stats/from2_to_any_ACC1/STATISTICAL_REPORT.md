# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:20:23

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
| 2 to 1 | 24 | 108.50 ms | 9.53 | 1.95 | [92.00, 116.00] |
| 2 to 2 | 24 | 107.67 ms | 9.05 | 1.85 | [92.00, 116.00] |
| 2 to 3 | 24 | 102.33 ms | 10.34 | 2.11 | [92.00, 116.00] |
| 2 to 4 | 24 | 102.67 ms | 9.26 | 1.89 | [92.00, 116.00] |
| 2 to 5 | 24 | 101.33 ms | 8.48 | 1.73 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -1.73 µV | 2.26 | 0.46 | [-6.40, 3.96] |
| 2 to 2 | 24 | -1.01 µV | 2.07 | 0.42 | [-5.94, 3.96] |
| 2 to 3 | 24 | -1.31 µV | 2.19 | 0.45 | [-5.76, 2.45] |
| 2 to 4 | 24 | -2.05 µV | 2.19 | 0.45 | [-6.14, 1.91] |
| 2 to 5 | 24 | -1.20 µV | 2.92 | 0.60 | [-12.97, 1.43] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 182.00 ms | 12.87 | 2.63 | [160.00, 204.00] |
| 2 to 2 | 24 | 174.33 ms | 19.87 | 4.06 | [144.00, 204.00] |
| 2 to 3 | 24 | 170.67 ms | 19.55 | 3.99 | [144.00, 204.00] |
| 2 to 4 | 24 | 173.00 ms | 17.02 | 3.47 | [144.00, 204.00] |
| 2 to 5 | 24 | 173.50 ms | 18.64 | 3.81 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | -3.49 µV | 3.38 | 0.69 | [-10.79, 2.29] |
| 2 to 2 | 24 | -5.25 µV | 2.68 | 0.55 | [-10.50, -0.87] |
| 2 to 3 | 24 | -4.99 µV | 2.41 | 0.49 | [-10.20, 0.67] |
| 2 to 4 | 24 | -6.05 µV | 3.18 | 0.65 | [-15.66, 1.34] |
| 2 to 5 | 24 | -6.33 µV | 2.61 | 0.53 | [-13.83, -1.17] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 115.33 ms | 11.29 | 2.31 | [88.00, 124.00] |
| 2 to 2 | 24 | 103.33 ms | 15.04 | 3.07 | [88.00, 124.00] |
| 2 to 3 | 24 | 109.50 ms | 13.59 | 2.77 | [88.00, 124.00] |
| 2 to 4 | 24 | 104.33 ms | 12.86 | 2.63 | [88.00, 124.00] |
| 2 to 5 | 24 | 99.83 ms | 11.71 | 2.39 | [88.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 3.65 µV | 2.71 | 0.55 | [-1.05, 9.13] |
| 2 to 2 | 24 | 1.62 µV | 2.53 | 0.52 | [-4.25, 7.57] |
| 2 to 3 | 24 | 1.76 µV | 2.42 | 0.49 | [-3.64, 6.87] |
| 2 to 4 | 24 | 2.58 µV | 2.16 | 0.44 | [-0.56, 7.56] |
| 2 to 5 | 24 | 1.85 µV | 2.88 | 0.59 | [-2.11, 11.82] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 474.83 ms | 45.09 | 9.20 | [392.00, 528.00] |
| 2 to 2 | 24 | 451.67 ms | 38.89 | 7.94 | [392.00, 520.00] |
| 2 to 3 | 24 | 452.83 ms | 43.58 | 8.90 | [392.00, 528.00] |
| 2 to 4 | 24 | 470.50 ms | 47.08 | 9.61 | [392.00, 528.00] |
| 2 to 5 | 24 | 453.33 ms | 43.14 | 8.81 | [392.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 24 | 5.33 µV | 3.36 | 0.69 | [-0.66, 11.08] |
| 2 to 2 | 24 | 2.38 µV | 3.44 | 0.70 | [-4.81, 10.57] |
| 2 to 3 | 24 | 4.88 µV | 4.16 | 0.85 | [-3.39, 13.70] |
| 2 to 4 | 24 | 5.85 µV | 4.96 | 1.01 | [-4.11, 17.43] |
| 2 to 5 | 24 | 5.51 µV | 2.63 | 0.54 | [0.85, 11.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 886.56, BIC = 908.86
- **2 to 2 vs 2 to 1**: *β* = -0.76, *SE* = 2.554, *z* = -0.296, *p* = 0.768
- **2 to 3 vs 2 to 1**: *β* = -6.14, *SE* = 2.532, *z* = -2.426, *p* = 0.015
- **2 to 4 vs 2 to 1**: *β* = -5.79, *SE* = 2.536, *z* = -2.284, *p* = 0.022
- **2 to 5 vs 2 to 1**: *β* = -7.12, *SE* = 2.540, *z* = -2.801, *p* = 0.005
- **SNR**: *β* = 0.11, *SE* = 0.496, *z* = 0.220, *p* = 0.826

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 0.76 | 2.55 | 0.30 | 0.768 | 0.975 | n.s. |
| 2 to 1 - 2 to 3 | 6.14 | 2.53 | 2.43 | 0.015 | 0.116 | n.s. |
| 2 to 1 - 2 to 4 | 5.79 | 2.54 | 2.28 | 0.022 | 0.146 | n.s. |
| 2 to 1 - 2 to 5 | 7.11 | 2.54 | 2.80 | 0.005 | 0.050 | * |
| 2 to 2 - 2 to 3 | 5.39 | 2.54 | 2.12 | 0.034 | 0.187 | n.s. |
| 2 to 2 - 2 to 4 | 5.04 | 2.54 | 1.99 | 0.047 | 0.214 | n.s. |
| 2 to 2 - 2 to 5 | 6.36 | 2.53 | 2.51 | 0.012 | 0.103 | n.s. |
| 2 to 3 - 2 to 4 | -0.35 | 2.53 | -0.14 | 0.890 | 0.975 | n.s. |
| 2 to 3 - 2 to 5 | 0.97 | 2.53 | 0.38 | 0.701 | 0.975 | n.s. |
| 2 to 4 - 2 to 5 | 1.32 | 2.53 | 0.52 | 0.601 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.30, *p* = 0.014, η²_G = 0.095
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 0.34 | 23 | = 0.817 | 0.09 [-0.35, 0.49] | negligible | n.s. |
| 2 to 1 vs 2 to 3 | 2.00 | 23 | = 0.112 | 0.62 [-0.03, 0.85] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 2.49 | 23 | = 0.085 | 0.62 [0.06, 0.96] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 2.39 | 23 | = 0.085 | 0.79 [0.04, 0.93] | medium | n.s. |
| 2 to 2 vs 2 to 3 | 1.92 | 23 | = 0.112 | 0.55 [-0.05, 0.83] | medium | n.s. |
| 2 to 2 vs 2 to 4 | 2.01 | 23 | = 0.112 | 0.55 [-0.03, 0.85] | medium | n.s. |
| 2 to 2 vs 2 to 5 | 2.64 | 23 | = 0.085 | 0.72 [0.09, 0.99] | medium | n.s. |
| 2 to 3 vs 2 to 4 | -0.12 | 23 | = 0.902 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | 0.40 | 23 | = 0.817 | 0.11 [-0.34, 0.51] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 0.66 | 23 | = 0.734 | 0.15 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 528.61, BIC = 550.91
- **2 to 2 vs 2 to 1**: *β* = 0.30, *SE* = 0.574, *z* = 0.529, *p* = 0.597
- **2 to 3 vs 2 to 1**: *β* = 0.29, *SE* = 0.569, *z* = 0.505, *p* = 0.614
- **2 to 4 vs 2 to 1**: *β* = -0.53, *SE* = 0.569, *z* = -0.936, *p* = 0.349
- **2 to 5 vs 2 to 1**: *β* = 0.25, *SE* = 0.570, *z* = 0.440, *p* = 0.660
- **SNR**: *β* = -0.58, *SE* = 0.111, *z* = -5.249, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | -0.30 | 0.57 | -0.53 | 0.597 | 0.996 | n.s. |
| 2 to 1 - 2 to 3 | -0.29 | 0.57 | -0.50 | 0.614 | 0.996 | n.s. |
| 2 to 1 - 2 to 4 | 0.53 | 0.57 | 0.94 | 0.349 | 0.951 | n.s. |
| 2 to 1 - 2 to 5 | -0.25 | 0.57 | -0.44 | 0.660 | 0.996 | n.s. |
| 2 to 2 - 2 to 3 | 0.02 | 0.57 | 0.03 | 0.977 | 1.000 | n.s. |
| 2 to 2 - 2 to 4 | 0.84 | 0.57 | 1.47 | 0.142 | 0.783 | n.s. |
| 2 to 2 - 2 to 5 | 0.05 | 0.57 | 0.09 | 0.927 | 1.000 | n.s. |
| 2 to 3 - 2 to 4 | 0.82 | 0.57 | 1.44 | 0.149 | 0.783 | n.s. |
| 2 to 3 - 2 to 5 | 0.04 | 0.57 | 0.06 | 0.949 | 1.000 | n.s. |
| 2 to 4 - 2 to 5 | -0.78 | 0.57 | -1.38 | 0.167 | 0.783 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.481, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | -1.19 | 23 | = 0.616 | -0.33 [-0.67, 0.19] | small | n.s. |
| 2 to 1 vs 2 to 3 | -0.57 | 23 | = 0.756 | -0.19 [-0.54, 0.31] | negligible | n.s. |
| 2 to 1 vs 2 to 4 | 0.52 | 23 | = 0.756 | 0.14 [-0.32, 0.53] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | -0.85 | 23 | = 0.756 | -0.20 [-0.60, 0.25] | small | n.s. |
| 2 to 2 vs 2 to 3 | 0.59 | 23 | = 0.756 | 0.14 [-0.30, 0.54] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | 1.78 | 23 | = 0.616 | 0.49 [-0.07, 0.80] | small | n.s. |
| 2 to 2 vs 2 to 5 | 0.30 | 23 | = 0.855 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | 1.21 | 23 | = 0.616 | 0.34 [-0.18, 0.68] | small | n.s. |
| 2 to 3 vs 2 to 5 | -0.15 | 23 | = 0.885 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | -1.26 | 23 | = 0.616 | -0.33 [-0.69, 0.17] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1016.00, BIC = 1038.30
- **2 to 2 vs 2 to 1**: *β* = -7.58, *SE* = 3.908, *z* = -1.940, *p* = 0.052
- **2 to 3 vs 2 to 1**: *β* = -11.05, *SE* = 3.952, *z* = -2.796, *p* = 0.005
- **2 to 4 vs 2 to 1**: *β* = -8.52, *SE* = 4.038, *z* = -2.111, *p* = 0.035
- **2 to 5 vs 2 to 1**: *β* = -8.16, *SE* = 3.972, *z* = -2.055, *p* = 0.040
- **SNR**: *β* = -0.29, *SE* = 0.621, *z* = -0.461, *p* = 0.645

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 7.58 | 3.91 | 1.94 | 0.052 | 0.314 | n.s. |
| 2 to 1 - 2 to 3 | 11.05 | 3.95 | 2.80 | 0.005 | 0.051 | n.s. |
| 2 to 1 - 2 to 4 | 8.52 | 4.04 | 2.11 | 0.035 | 0.273 | n.s. |
| 2 to 1 - 2 to 5 | 8.16 | 3.97 | 2.05 | 0.040 | 0.278 | n.s. |
| 2 to 2 - 2 to 3 | 3.47 | 3.93 | 0.88 | 0.377 | 0.942 | n.s. |
| 2 to 2 - 2 to 4 | 0.94 | 3.99 | 0.24 | 0.813 | 0.994 | n.s. |
| 2 to 2 - 2 to 5 | 0.58 | 3.94 | 0.15 | 0.883 | 0.994 | n.s. |
| 2 to 3 - 2 to 4 | -2.53 | 3.93 | -0.64 | 0.520 | 0.954 | n.s. |
| 2 to 3 - 2 to 5 | -2.89 | 3.91 | -0.74 | 0.460 | 0.954 | n.s. |
| 2 to 4 - 2 to 5 | -0.36 | 3.91 | -0.09 | 0.926 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.34, *p* = 0.061, η²_G = 0.047
- Greenhouse-Geisser corrected: *p* = 0.086 (ε = 0.704)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 2.61 | 23 | = 0.052 | 0.46 [0.08, 0.98] | small | n.s. |
| 2 to 1 vs 2 to 3 | 2.82 | 23 | = 0.052 | 0.68 [0.12, 1.03] | medium | n.s. |
| 2 to 1 vs 2 to 4 | 2.62 | 23 | = 0.052 | 0.60 [0.08, 0.99] | medium | n.s. |
| 2 to 1 vs 2 to 5 | 2.41 | 23 | = 0.061 | 0.53 [0.04, 0.94] | medium | n.s. |
| 2 to 2 vs 2 to 3 | 0.87 | 23 | = 0.789 | 0.19 [-0.25, 0.60] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | 0.29 | 23 | = 0.851 | 0.07 [-0.36, 0.48] | negligible | n.s. |
| 2 to 2 vs 2 to 5 | 0.21 | 23 | = 0.851 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -0.48 | 23 | = 0.851 | -0.13 [-0.52, 0.33] | negligible | n.s. |
| 2 to 3 vs 2 to 5 | -0.57 | 23 | = 0.851 | -0.15 [-0.54, 0.31] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | -0.19 | 23 | = 0.851 | -0.03 [-0.46, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 543.89, BIC = 566.19
- **2 to 2 vs 2 to 1**: *β* = -1.59, *SE* = 0.547, *z* = -2.901, *p* = 0.004
- **2 to 3 vs 2 to 1**: *β* = -0.95, *SE* = 0.553, *z* = -1.721, *p* = 0.085
- **2 to 4 vs 2 to 1**: *β* = -1.64, *SE* = 0.565, *z* = -2.911, *p* = 0.004
- **2 to 5 vs 2 to 1**: *β* = -2.19, *SE* = 0.556, *z* = -3.935, *p* < .001
- **SNR**: *β* = -0.55, *SE* = 0.085, *z* = -6.432, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 1.59 | 0.55 | 2.90 | 0.004 | 0.032 | * |
| 2 to 1 - 2 to 3 | 0.95 | 0.55 | 1.72 | 0.085 | 0.414 | n.s. |
| 2 to 1 - 2 to 4 | 1.64 | 0.56 | 2.91 | 0.004 | 0.032 | * |
| 2 to 1 - 2 to 5 | 2.19 | 0.56 | 3.93 | < .001 | < .001 | *** |
| 2 to 2 - 2 to 3 | -0.64 | 0.55 | -1.16 | 0.248 | 0.688 | n.s. |
| 2 to 2 - 2 to 4 | 0.06 | 0.56 | 0.10 | 0.919 | 0.919 | n.s. |
| 2 to 2 - 2 to 5 | 0.60 | 0.55 | 1.09 | 0.277 | 0.688 | n.s. |
| 2 to 3 - 2 to 4 | 0.69 | 0.55 | 1.26 | 0.208 | 0.688 | n.s. |
| 2 to 3 - 2 to 5 | 1.24 | 0.55 | 2.26 | 0.024 | 0.156 | n.s. |
| 2 to 4 - 2 to 5 | 0.54 | 0.55 | 0.99 | 0.322 | 0.688 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.95, *p* < .001, η²_G = 0.111
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 2.90 | 23 | = 0.027 | 0.57 [0.13, 1.05] | medium | * |
| 2 to 1 vs 2 to 3 | 2.64 | 23 | = 0.037 | 0.51 [0.09, 0.99] | medium | * |
| 2 to 1 vs 2 to 4 | 3.23 | 23 | = 0.018 | 0.78 [0.19, 1.13] | medium | * |
| 2 to 1 vs 2 to 5 | 3.79 | 23 | = 0.010 | 0.94 [0.29, 1.25] | large | ** |
| 2 to 2 vs 2 to 3 | -0.49 | 23 | = 0.695 | -0.10 [-0.52, 0.32] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | 1.23 | 23 | = 0.289 | 0.27 [-0.18, 0.68] | small | n.s. |
| 2 to 2 vs 2 to 5 | 1.82 | 23 | = 0.137 | 0.41 [-0.07, 0.81] | small | n.s. |
| 2 to 3 vs 2 to 4 | 1.72 | 23 | = 0.141 | 0.38 [-0.08, 0.79] | small | n.s. |
| 2 to 3 vs 2 to 5 | 2.22 | 23 | = 0.073 | 0.53 [0.01, 0.90] | medium | n.s. |
| 2 to 4 vs 2 to 5 | 0.40 | 23 | = 0.695 | 0.10 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 955.61, BIC = 977.91
- **2 to 2 vs 2 to 1**: *β* = -11.78, *SE* = 3.207, *z* = -3.673, *p* < .001
- **2 to 3 vs 2 to 1**: *β* = -5.57, *SE* = 3.221, *z* = -1.729, *p* = 0.084
- **2 to 4 vs 2 to 1**: *β* = -10.71, *SE* = 3.229, *z* = -3.317, *p* = 0.001
- **2 to 5 vs 2 to 1**: *β* = -15.17, *SE* = 3.245, *z* = -4.675, *p* < .001
- **SNR**: *β* = 0.28, *SE* = 0.566, *z* = 0.499, *p* = 0.618

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 11.78 | 3.21 | 3.67 | < .001 | 0.002 | ** |
| 2 to 1 - 2 to 3 | 5.57 | 3.22 | 1.73 | 0.084 | 0.355 | n.s. |
| 2 to 1 - 2 to 4 | 10.71 | 3.23 | 3.32 | < .001 | 0.007 | ** |
| 2 to 1 - 2 to 5 | 15.17 | 3.24 | 4.67 | < .001 | < .001 | *** |
| 2 to 2 - 2 to 3 | -6.21 | 3.18 | -1.95 | 0.051 | 0.268 | n.s. |
| 2 to 2 - 2 to 4 | -1.07 | 3.18 | -0.34 | 0.737 | 0.737 | n.s. |
| 2 to 2 - 2 to 5 | 3.39 | 3.18 | 1.06 | 0.287 | 0.492 | n.s. |
| 2 to 3 - 2 to 4 | 5.14 | 3.18 | 1.62 | 0.105 | 0.360 | n.s. |
| 2 to 3 - 2 to 5 | 9.60 | 3.18 | 3.02 | 0.003 | 0.018 | * |
| 2 to 4 - 2 to 5 | 4.46 | 3.18 | 1.40 | 0.161 | 0.408 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.91, *p* < .001, η²_G = 0.154
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 3.78 | 23 | = 0.005 | 0.90 [0.29, 1.25] | large | ** |
| 2 to 1 vs 2 to 3 | 1.74 | 23 | = 0.172 | 0.47 [-0.08, 0.79] | small | n.s. |
| 2 to 1 vs 2 to 4 | 3.42 | 23 | = 0.008 | 0.91 [0.23, 1.17] | large | ** |
| 2 to 1 vs 2 to 5 | 5.22 | 23 | < .001 | 1.35 [0.54, 1.59] | large | *** |
| 2 to 2 vs 2 to 3 | -1.57 | 23 | = 0.186 | -0.43 [-0.75, 0.11] | small | n.s. |
| 2 to 2 vs 2 to 4 | -0.31 | 23 | = 0.762 | -0.07 [-0.49, 0.36] | negligible | n.s. |
| 2 to 2 vs 2 to 5 | 1.10 | 23 | = 0.315 | 0.26 [-0.20, 0.65] | small | n.s. |
| 2 to 3 vs 2 to 4 | 1.41 | 23 | = 0.215 | 0.39 [-0.14, 0.72] | small | n.s. |
| 2 to 3 vs 2 to 5 | 3.28 | 23 | = 0.008 | 0.76 [0.20, 1.14] | medium | ** |
| 2 to 4 vs 2 to 5 | 1.70 | 23 | = 0.172 | 0.37 [-0.09, 0.78] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.00, BIC = 572.30
- **2 to 2 vs 2 to 1**: *β* = -1.87, *SE* = 0.572, *z* = -3.276, *p* = 0.001
- **2 to 3 vs 2 to 1**: *β* = -1.70, *SE* = 0.575, *z* = -2.966, *p* = 0.003
- **2 to 4 vs 2 to 1**: *β* = -0.87, *SE* = 0.576, *z* = -1.512, *p* = 0.131
- **2 to 5 vs 2 to 1**: *β* = -1.57, *SE* = 0.579, *z* = -2.718, *p* = 0.007
- **SNR**: *β* = 0.20, *SE* = 0.103, *z* = 1.890, *p* = 0.059

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 1.87 | 0.57 | 3.28 | 0.001 | 0.010 | * |
| 2 to 1 - 2 to 3 | 1.70 | 0.57 | 2.97 | 0.003 | 0.027 | * |
| 2 to 1 - 2 to 4 | 0.87 | 0.58 | 1.51 | 0.131 | 0.568 | n.s. |
| 2 to 1 - 2 to 5 | 1.57 | 0.58 | 2.72 | 0.007 | 0.051 | n.s. |
| 2 to 2 - 2 to 3 | -0.17 | 0.57 | -0.30 | 0.764 | 0.944 | n.s. |
| 2 to 2 - 2 to 4 | -1.00 | 0.57 | -1.77 | 0.077 | 0.429 | n.s. |
| 2 to 2 - 2 to 5 | -0.30 | 0.57 | -0.53 | 0.597 | 0.935 | n.s. |
| 2 to 3 - 2 to 4 | -0.83 | 0.57 | -1.47 | 0.141 | 0.568 | n.s. |
| 2 to 3 - 2 to 5 | -0.13 | 0.57 | -0.23 | 0.818 | 0.944 | n.s. |
| 2 to 4 - 2 to 5 | 0.70 | 0.57 | 1.24 | 0.215 | 0.620 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.18, *p* = 0.004, η²_G = 0.084
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 4.61 | 23 | = 0.001 | 0.77 [0.43, 1.45] | medium | ** |
| 2 to 1 vs 2 to 3 | 3.13 | 23 | = 0.023 | 0.74 [0.18, 1.10] | medium | * |
| 2 to 1 vs 2 to 4 | 2.04 | 23 | = 0.131 | 0.44 [-0.02, 0.86] | small | n.s. |
| 2 to 1 vs 2 to 5 | 2.76 | 23 | = 0.037 | 0.64 [0.11, 1.02] | medium | * |
| 2 to 2 vs 2 to 3 | -0.28 | 23 | = 0.870 | -0.06 [-0.48, 0.37] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | -1.87 | 23 | = 0.150 | -0.41 [-0.82, 0.06] | small | n.s. |
| 2 to 2 vs 2 to 5 | -0.35 | 23 | = 0.870 | -0.08 [-0.49, 0.35] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -1.44 | 23 | = 0.272 | -0.36 [-0.73, 0.14] | small | n.s. |
| 2 to 3 vs 2 to 5 | -0.12 | 23 | = 0.903 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.12 | 23 | = 0.391 | 0.29 [-0.20, 0.66] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1256.70, BIC = 1279.00
- **2 to 2 vs 2 to 1**: *β* = -23.46, *SE* = 12.022, *z* = -1.952, *p* = 0.051
- **2 to 3 vs 2 to 1**: *β* = -21.80, *SE* = 11.973, *z* = -1.820, *p* = 0.069
- **2 to 4 vs 2 to 1**: *β* = -4.07, *SE* = 12.005, *z* = -0.339, *p* = 0.735
- **2 to 5 vs 2 to 1**: *β* = -21.60, *SE* = 11.940, *z* = -1.809, *p* = 0.070
- **SNR**: *β* = -0.27, *SE* = 1.329, *z* = -0.199, *p* = 0.842

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 23.46 | 12.02 | 1.95 | 0.051 | 0.407 | n.s. |
| 2 to 1 - 2 to 3 | 21.80 | 11.97 | 1.82 | 0.069 | 0.473 | n.s. |
| 2 to 1 - 2 to 4 | 4.07 | 12.00 | 0.34 | 0.735 | 0.995 | n.s. |
| 2 to 1 - 2 to 5 | 21.60 | 11.94 | 1.81 | 0.070 | 0.473 | n.s. |
| 2 to 2 - 2 to 3 | -1.67 | 12.19 | -0.14 | 0.891 | 0.998 | n.s. |
| 2 to 2 - 2 to 4 | -19.40 | 12.26 | -1.58 | 0.114 | 0.570 | n.s. |
| 2 to 2 - 2 to 5 | -1.87 | 11.97 | -0.16 | 0.876 | 0.998 | n.s. |
| 2 to 3 - 2 to 4 | -17.73 | 11.93 | -1.49 | 0.137 | 0.588 | n.s. |
| 2 to 3 - 2 to 5 | -0.20 | 12.02 | -0.02 | 0.987 | 0.998 | n.s. |
| 2 to 4 - 2 to 5 | 17.53 | 12.07 | 1.45 | 0.146 | 0.588 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.66, *p* = 0.165, η²_G = 0.051
- Greenhouse-Geisser corrected: *p* = 0.185 (ε = 0.712)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 1.76 | 23 | = 0.354 | 0.55 [-0.08, 0.80] | medium | n.s. |
| 2 to 1 vs 2 to 3 | 1.58 | 23 | = 0.354 | 0.50 [-0.11, 0.76] | small | n.s. |
| 2 to 1 vs 2 to 4 | 0.61 | 23 | = 0.780 | 0.09 [-0.30, 0.55] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | 1.93 | 23 | = 0.354 | 0.49 [-0.04, 0.83] | small | n.s. |
| 2 to 2 vs 2 to 3 | -0.11 | 23 | = 0.966 | -0.03 [-0.44, 0.40] | negligible | n.s. |
| 2 to 2 vs 2 to 4 | -1.39 | 23 | = 0.354 | -0.44 [-0.72, 0.15] | small | n.s. |
| 2 to 2 vs 2 to 5 | -0.14 | 23 | = 0.966 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| 2 to 3 vs 2 to 4 | -1.20 | 23 | = 0.403 | -0.39 [-0.67, 0.18] | small | n.s. |
| 2 to 3 vs 2 to 5 | -0.04 | 23 | = 0.966 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 1.43 | 23 | = 0.354 | 0.38 [-0.14, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 606.50, BIC = 628.80
- **2 to 2 vs 2 to 1**: *β* = -2.48, *SE* = 0.683, *z* = -3.634, *p* < .001
- **2 to 3 vs 2 to 1**: *β* = -0.78, *SE* = 0.679, *z* = -1.141, *p* = 0.254
- **2 to 4 vs 2 to 1**: *β* = 0.10, *SE* = 0.682, *z* = 0.143, *p* = 0.886
- **2 to 5 vs 2 to 1**: *β* = 0.33, *SE* = 0.677, *z* = 0.486, *p* = 0.627
- **SNR**: *β* = 0.42, *SE* = 0.084, *z* = 4.998, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 2 to 2 | 2.48 | 0.68 | 3.63 | < .001 | 0.002 | ** |
| 2 to 1 - 2 to 3 | 0.78 | 0.68 | 1.14 | 0.254 | 0.690 | n.s. |
| 2 to 1 - 2 to 4 | -0.10 | 0.68 | -0.14 | 0.886 | 0.948 | n.s. |
| 2 to 1 - 2 to 5 | -0.33 | 0.68 | -0.49 | 0.627 | 0.948 | n.s. |
| 2 to 2 - 2 to 3 | -1.71 | 0.69 | -2.46 | 0.014 | 0.094 | n.s. |
| 2 to 2 - 2 to 4 | -2.58 | 0.70 | -3.69 | < .001 | 0.002 | ** |
| 2 to 2 - 2 to 5 | -2.81 | 0.68 | -4.14 | < .001 | < .001 | *** |
| 2 to 3 - 2 to 4 | -0.87 | 0.68 | -1.29 | 0.197 | 0.666 | n.s. |
| 2 to 3 - 2 to 5 | -1.10 | 0.68 | -1.62 | 0.106 | 0.490 | n.s. |
| 2 to 4 - 2 to 5 | -0.23 | 0.69 | -0.34 | 0.736 | 0.948 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.64, *p* < .001, η²_G = 0.101
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 2 to 2 | 4.24 | 23 | = 0.001 | 0.87 [0.37, 1.36] | large | ** |
| 2 to 1 vs 2 to 3 | 0.61 | 23 | = 0.743 | 0.12 [-0.30, 0.55] | negligible | n.s. |
| 2 to 1 vs 2 to 4 | -0.54 | 23 | = 0.743 | -0.12 [-0.53, 0.31] | negligible | n.s. |
| 2 to 1 vs 2 to 5 | -0.33 | 23 | = 0.746 | -0.06 [-0.49, 0.36] | negligible | n.s. |
| 2 to 2 vs 2 to 3 | -3.38 | 23 | = 0.007 | -0.65 [-1.16, -0.22] | medium | ** |
| 2 to 2 vs 2 to 4 | -4.27 | 23 | = 0.001 | -0.81 [-1.37, -0.38] | large | ** |
| 2 to 2 vs 2 to 5 | -4.11 | 23 | = 0.001 | -1.02 [-1.33, -0.35] | large | ** |
| 2 to 3 vs 2 to 4 | -1.25 | 23 | = 0.451 | -0.21 [-0.68, 0.17] | small | n.s. |
| 2 to 3 vs 2 to 5 | -0.93 | 23 | = 0.601 | -0.18 [-0.62, 0.24] | negligible | n.s. |
| 2 to 4 vs 2 to 5 | 0.40 | 23 | = 0.746 | 0.09 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.014) (no significant pairwise comparisons)
**N1 latency:** Marginal trend toward condition differences (*p* = 0.061)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 2 (*d* = 0.57)
  - 2 to 1 showed greater amplitude than 2 to 3 (*d* = 0.51)
  - 2 to 1 showed greater amplitude than 2 to 4 (*d* = 0.78)
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 0.94)
**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater latency than 2 to 2 (*d* = 0.90)
  - 2 to 1 showed greater latency than 2 to 4 (*d* = 0.91)
  - 2 to 1 showed greater latency than 2 to 5 (*d* = 1.35)
  - 2 to 3 showed greater latency than 2 to 5 (*d* = 0.76)
**P1 amplitude:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 2 (*d* = 0.77)
  - 2 to 1 showed greater amplitude than 2 to 3 (*d* = 0.74)
  - 2 to 1 showed greater amplitude than 2 to 5 (*d* = 0.64)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than 2 to 2 (*d* = 0.87)
  - 2 to 2 showed smaller amplitude than 2 to 3 (*d* = -0.65)
  - 2 to 2 showed smaller amplitude than 2 to 4 (*d* = -0.81)
  - 2 to 2 showed smaller amplitude than 2 to 5 (*d* = -1.02)

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
