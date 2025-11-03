# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:49:35

---

## 1. Analysis Overview

**Total Measurements:** 268
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
| Large Ratio 0.67 (4:6) | 7 | 108.00 ms | 11.31 | 4.28 | [92.00, 116.00] |
| Large Ratio 0.8 (4:5) | 9 | 98.67 ms | 13.27 | 4.42 | [88.00, 116.00] |
| Large Ratio 0.83 (5:6) | 5 | 97.60 ms | 10.81 | 4.83 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 7 | 3.41 µV | 1.35 | 0.51 | [0.91, 4.93] |
| Large Ratio 0.8 (4:5) | 9 | 2.11 µV | 1.43 | 0.48 | [0.69, 4.97] |
| Large Ratio 0.83 (5:6) | 5 | 4.00 µV | 1.68 | 0.75 | [1.99, 6.18] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 24 | 172.83 ms | 20.46 | 4.18 | [144.00, 204.00] |
| Large Ratio 0.8 (4:5) | 22 | 170.91 ms | 18.85 | 4.02 | [140.00, 204.00] |
| Large Ratio 0.83 (5:6) | 17 | 176.24 ms | 21.79 | 5.29 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 24 | -5.92 µV | 3.05 | 0.62 | [-12.83, -2.46] |
| Large Ratio 0.8 (4:5) | 22 | -6.06 µV | 2.68 | 0.57 | [-11.24, -2.10] |
| Large Ratio 0.83 (5:6) | 17 | -6.46 µV | 2.41 | 0.58 | [-11.29, -2.31] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 11 | 108.36 ms | 7.68 | 2.32 | [96.00, 116.00] |
| Large Ratio 0.8 (4:5) | 16 | 106.75 ms | 6.96 | 1.74 | [96.00, 116.00] |
| Large Ratio 0.83 (5:6) | 11 | 109.09 ms | 7.40 | 2.23 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 11 | 3.59 µV | 1.48 | 0.45 | [1.24, 5.85] |
| Large Ratio 0.8 (4:5) | 16 | 2.97 µV | 1.79 | 0.45 | [0.46, 6.17] |
| Large Ratio 0.83 (5:6) | 11 | 4.04 µV | 4.38 | 1.32 | [0.74, 16.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 18 | 516.00 ms | 13.02 | 3.07 | [504.00, 540.00] |
| Large Ratio 0.8 (4:5) | 19 | 518.32 ms | 13.75 | 3.15 | [504.00, 540.00] |
| Large Ratio 0.83 (5:6) | 12 | 527.67 ms | 13.15 | 3.80 | [504.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 18 | 5.03 µV | 2.53 | 0.60 | [2.01, 11.00] |
| Large Ratio 0.8 (4:5) | 19 | 5.05 µV | 2.97 | 0.68 | [0.40, 10.40] |
| Large Ratio 0.83 (5:6) | 12 | 6.06 µV | 4.87 | 1.41 | [0.81, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 119.08, BIC = 125.34
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 0.43, *SE* = 0.001, *z* = 501.064, *p* < .001
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = -2.52, *SE* = 0.001, *z* = -1971.299, *p* < .001
- **SNR**: *β* = -2.51, *SE* = 0.001, *z* = -2966.174, *p* < .001

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -0.43 | 0.00 | -501.06 | < .001 | < .001 | *** |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | 2.52 | 0.00 | 1971.30 | < .001 | < .001 | *** |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | 2.95 | 0.00 | 2432.97 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 61.29, BIC = 67.55
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 0.03, *SE* = 0.538, *z* = 0.050, *p* = 0.960
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 0.52, *SE* = 0.403, *z* = 1.299, *p* = 0.194
- **SNR**: *β* = 1.30, *SE* = 0.220, *z* = 5.912, *p* < .001

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -0.03 | 0.54 | -0.05 | 0.960 | 0.960 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -0.52 | 0.40 | -1.30 | 0.194 | 0.476 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | -0.50 | 0.61 | -0.81 | 0.418 | 0.661 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 550.12, BIC = 562.97
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = -0.45, *SE* = 3.905, *z* = -0.114, *p* = 0.909
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 4.73, *SE* = 4.490, *z* = 1.054, *p* = 0.292
- **SNR**: *β* = 0.69, *SE* = 0.542, *z* = 1.270, *p* = 0.204

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | 0.45 | 3.91 | 0.11 | 0.909 | 0.909 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -4.73 | 4.49 | -1.05 | 0.292 | 0.585 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | -5.18 | 4.54 | -1.14 | 0.254 | 0.585 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.34, *p* = 0.715, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | 0.43 | 15 | = 0.675 | 0.12 [-0.45, 0.43] | negligible | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | -0.43 | 15 | = 0.675 | -0.08 [-0.62, 0.41] | negligible | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | -0.78 | 15 | = 0.675 | -0.21 [-0.73, 0.34] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 271.81, BIC = 284.66
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = -0.11, *SE* = 0.428, *z* = -0.262, *p* = 0.793
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = -1.37, *SE* = 0.493, *z* = -2.784, *p* = 0.005
- **SNR**: *β* = -0.38, *SE* = 0.059, *z* = -6.382, *p* < .001

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | 0.11 | 0.43 | 0.26 | 0.793 | 0.793 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | 1.37 | 0.49 | 2.78 | 0.005 | 0.016 | * |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | 1.26 | 0.50 | 2.53 | 0.012 | 0.023 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.11, *p* = 0.894, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -0.01 | 15 | = 0.996 | -0.00 [-0.45, 0.44] | negligible | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | 0.42 | 15 | = 0.996 | 0.12 [-0.37, 0.66] | negligible | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | 0.41 | 15 | = 0.996 | 0.11 [-0.43, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 259.44, BIC = 269.26
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 1.29, *SE* = 2.067, *z* = 0.625, *p* = 0.532
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 4.32, *SE* = 2.538, *z* = 1.701, *p* = 0.089
- **SNR**: *β* = 0.79, *SE* = 0.557, *z* = 1.418, *p* = 0.156

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -1.29 | 2.07 | -0.62 | 0.532 | 0.532 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -4.32 | 2.54 | -1.70 | 0.089 | 0.244 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | -3.02 | 2.08 | -1.45 | 0.147 | 0.272 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.73, *p* = 0.508, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -1.00 | 5 | = 0.576 | -0.27 [-1.15, 0.43] | small | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | -0.88 | 5 | = 0.576 | -0.49 [-1.44, 0.72] | small | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | -0.60 | 5 | = 0.576 | -0.25 [-1.37, 0.55] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 189.93, BIC = 199.76
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 0.12, *SE* = 1.020, *z* = 0.121, *p* = 0.904
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 1.66, *SE* = 1.221, *z* = 1.355, *p* = 0.175
- **SNR**: *β* = 0.48, *SE* = 0.264, *z* = 1.824, *p* = 0.068

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -0.12 | 1.02 | -0.12 | 0.904 | 0.904 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -1.65 | 1.22 | -1.36 | 0.175 | 0.321 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | -1.53 | 0.99 | -1.55 | 0.121 | 0.321 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.666, η²_G = 0.054
- Greenhouse-Geisser corrected: *p* = 0.557 (ε = 0.540)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | 1.44 | 5 | = 0.625 | 0.61 [-0.41, 1.19] | medium | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | -0.36 | 5 | = 0.737 | -0.23 [-1.20, 0.91] | small | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | -0.82 | 5 | = 0.674 | -0.44 [-1.27, 0.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 400.08, BIC = 411.43
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 2.83, *SE* = 3.966, *z* = 0.714, *p* = 0.475
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 12.45, *SE* = 4.816, *z* = 2.585, *p* = 0.010
- **SNR**: *β* = 0.34, *SE* = 0.527, *z* = 0.643, *p* = 0.520

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -2.83 | 3.97 | -0.71 | 0.475 | 0.475 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -12.45 | 4.82 | -2.59 | 0.010 | 0.029 | * |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | -9.62 | 4.78 | -2.01 | 0.044 | 0.086 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.26, *p* = 0.130, η²_G = 0.112
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -0.77 | 10 | = 0.457 | -0.32 [-0.81, 0.27] | small | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | -1.90 | 10 | = 0.211 | -0.80 [-1.20, 0.16] | medium | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | -1.60 | 10 | = 0.211 | -0.52 [-1.19, 0.23] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 256.00, BIC = 267.35
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 0.34, *SE* = 0.842, *z* = 0.402, *p* = 0.688
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 1.61, *SE* = 1.027, *z* = 1.571, *p* = 0.116
- **SNR**: *β* = 0.30, *SE* = 0.109, *z* = 2.761, *p* = 0.006

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -0.34 | 0.84 | -0.40 | 0.688 | 0.688 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -1.61 | 1.03 | -1.57 | 0.116 | 0.310 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | -1.27 | 1.02 | -1.25 | 0.210 | 0.376 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.32, *p* = 0.728, η²_G = 0.014
- Greenhouse-Geisser corrected: *p* = 0.608 (ε = 0.564)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -1.36 | 10 | = 0.615 | -0.29 [-0.68, 0.39] | small | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | 0.07 | 10 | = 0.946 | 0.03 [-0.71, 0.56] | negligible | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | 0.73 | 10 | = 0.725 | 0.23 [-0.46, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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
