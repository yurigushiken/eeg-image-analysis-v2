# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:16:31

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
| Decrease by 1 (no 1) | 24 | 104.17 ms | 8.54 | 1.74 | [92.00, 116.00] |
| Decrease by 2 (no 1) | 24 | 106.17 ms | 8.67 | 1.77 | [92.00, 116.00] |
| Decrease by 3 (no 1) | 24 | 104.50 ms | 9.39 | 1.92 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | -0.93 µV | 1.74 | 0.35 | [-5.59, 2.13] |
| Decrease by 2 (no 1) | 24 | -1.54 µV | 1.50 | 0.31 | [-5.60, 2.21] |
| Decrease by 3 (no 1) | 24 | -1.73 µV | 1.80 | 0.37 | [-6.28, 2.33] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 174.33 ms | 17.81 | 3.63 | [144.00, 212.00] |
| Decrease by 2 (no 1) | 24 | 173.17 ms | 16.19 | 3.31 | [144.00, 212.00] |
| Decrease by 3 (no 1) | 24 | 175.33 ms | 17.68 | 3.61 | [148.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | -5.36 µV | 2.03 | 0.41 | [-9.50, -2.05] |
| Decrease by 2 (no 1) | 24 | -5.48 µV | 2.17 | 0.44 | [-9.98, -1.47] |
| Decrease by 3 (no 1) | 24 | -6.25 µV | 2.42 | 0.49 | [-10.38, -1.96] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 110.17 ms | 8.17 | 1.67 | [100.00, 120.00] |
| Decrease by 2 (no 1) | 24 | 112.67 ms | 7.14 | 1.46 | [100.00, 120.00] |
| Decrease by 3 (no 1) | 24 | 109.83 ms | 8.75 | 1.79 | [100.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 0.64 µV | 2.14 | 0.44 | [-2.52, 5.95] |
| Decrease by 2 (no 1) | 24 | 1.31 µV | 2.04 | 0.42 | [-3.30, 4.83] |
| Decrease by 3 (no 1) | 24 | 1.57 µV | 2.01 | 0.41 | [-2.73, 6.10] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 488.83 ms | 31.27 | 6.38 | [424.00, 532.00] |
| Decrease by 2 (no 1) | 24 | 475.17 ms | 31.32 | 6.39 | [436.00, 536.00] |
| Decrease by 3 (no 1) | 24 | 478.00 ms | 32.37 | 6.61 | [428.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 3.30 µV | 3.26 | 0.66 | [-2.96, 9.46] |
| Decrease by 2 (no 1) | 24 | 3.58 µV | 3.09 | 0.63 | [-1.49, 8.89] |
| Decrease by 3 (no 1) | 24 | 4.15 µV | 3.75 | 0.77 | [-1.41, 13.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 514.88, BIC = 528.54
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 2.48, *SE* = 1.969, *z* = 1.259, *p* = 0.208
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 1.02, *SE* = 1.979, *z* = 0.515, *p* = 0.607
- **SNR**: *β* = 1.23, *SE* = 0.503, *z* = 2.443, *p* = 0.015

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -2.48 | 1.97 | -1.26 | 0.208 | 0.503 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.02 | 1.98 | -0.51 | 0.607 | 0.704 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.46 | 1.96 | 0.75 | 0.456 | 0.704 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.52, *p* = 0.597, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.17 | 23 | = 0.740 | -0.23 [-0.67, 0.19] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.16 | 23 | = 0.878 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.70 | 23 | = 0.740 | 0.18 [-0.28, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 267.15, BIC = 280.81
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.66, *SE* = 0.327, *z* = -2.024, *p* = 0.043
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.88, *SE* = 0.329, *z* = -2.663, *p* = 0.008
- **SNR**: *β* = -0.14, *SE* = 0.088, *z* = -1.622, *p* = 0.105

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.66 | 0.33 | 2.02 | 0.043 | 0.084 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.88 | 0.33 | 2.66 | 0.008 | 0.023 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.21 | 0.33 | 0.66 | 0.511 | 0.511 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.10, *p* = 0.055, η²_G = 0.041
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.85 | 23 | = 0.116 | 0.37 [-0.06, 0.81] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.63 | 23 | = 0.045 | 0.45 [0.09, 0.99] | small | * |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.52 | 23 | = 0.611 | 0.11 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 589.48, BIC = 603.14
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -1.19, *SE* = 2.771, *z* = -0.428, *p* = 0.669
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.87, *SE* = 2.822, *z* = 0.307, *p* = 0.759
- **SNR**: *β* = -0.10, *SE* = 0.392, *z* = -0.248, *p* = 0.804

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 1.19 | 2.77 | 0.43 | 0.669 | 0.890 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.87 | 2.82 | -0.31 | 0.759 | 0.890 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.05 | 2.81 | -0.73 | 0.465 | 0.847 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.747, η²_G = 0.003
- Greenhouse-Geisser corrected: *p* = 0.658 (ε = 0.670)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.75 | 23 | = 0.762 | 0.07 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.30 | 23 | = 0.768 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.67 | 23 | = 0.762 | -0.13 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.84, BIC = 294.50
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.14, *SE* = 0.324, *z* = -0.448, *p* = 0.654
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -1.09, *SE* = 0.330, *z* = -3.306, *p* = 0.001
- **SNR**: *β* = -0.15, *SE* = 0.046, *z* = -3.325, *p* = 0.001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.15 | 0.32 | 0.45 | 0.654 | 0.654 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.09 | 0.33 | 3.31 | < .001 | 0.003 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.95 | 0.33 | 2.88 | 0.004 | 0.008 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.72, *p* = 0.032, η²_G = 0.032
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.33 | 23 | = 0.741 | 0.06 [-0.35, 0.49] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.30 | 23 | = 0.047 | 0.39 [0.02, 0.91] | small | * |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.38 | 23 | = 0.047 | 0.33 [0.04, 0.93] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 477.87, BIC = 491.53
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 2.48, *SE* = 1.264, *z* = 1.959, *p* = 0.050
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.41, *SE* = 1.282, *z* = -0.316, *p* = 0.752
- **SNR**: *β* = -0.07, *SE* = 0.227, *z* = -0.309, *p* = 0.757

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -2.48 | 1.26 | -1.96 | 0.050 | 0.098 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.40 | 1.28 | 0.32 | 0.752 | 0.752 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 2.88 | 1.27 | 2.27 | 0.023 | 0.068 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.88, *p* = 0.066, η²_G = 0.025
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -2.01 | 23 | = 0.085 | -0.33 [-0.85, 0.03] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.22 | 23 | = 0.828 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.67 | 23 | = 0.041 | 0.35 [0.09, 1.00] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 273.12, BIC = 286.78
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.70, *SE* = 0.297, *z* = 2.354, *p* = 0.019
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 1.00, *SE* = 0.302, *z* = 3.305, *p* = 0.001
- **SNR**: *β* = 0.06, *SE* = 0.055, *z* = 1.173, *p* = 0.241

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.70 | 0.30 | -2.35 | 0.019 | 0.037 | * |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.00 | 0.30 | -3.30 | < .001 | 0.003 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.30 | 0.30 | -1.00 | 0.319 | 0.319 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.05, *p* = 0.010, η²_G = 0.036
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -2.18 | 23 | = 0.059 | -0.32 [-0.89, -0.00] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -3.00 | 23 | = 0.019 | -0.45 [-1.07, -0.15] | small | * |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.89 | 23 | = 0.384 | -0.13 [-0.61, 0.24] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 702.22, BIC = 715.88
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -14.40, *SE* = 7.285, *z* = -1.977, *p* = 0.048
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -11.49, *SE* = 7.271, *z* = -1.581, *p* = 0.114
- **SNR**: *β* = -0.64, *SE* = 0.905, *z* = -0.709, *p* = 0.478

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 14.40 | 7.28 | 1.98 | 0.048 | 0.137 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 11.49 | 7.27 | 1.58 | 0.114 | 0.215 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.91 | 7.21 | -0.40 | 0.687 | 0.687 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.92, *p* = 0.157, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 2.52 | 23 | = 0.058 | 0.44 [0.06, 0.96] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 1.43 | 23 | = 0.251 | 0.34 [-0.14, 0.72] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.33 | 23 | = 0.747 | -0.09 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 316.30, BIC = 329.96
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.46, *SE* = 0.373, *z* = 1.222, *p* = 0.222
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 1.01, *SE* = 0.372, *z* = 2.721, *p* = 0.007
- **SNR**: *β* = 0.16, *SE* = 0.059, *z* = 2.709, *p* = 0.007

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.46 | 0.37 | -1.22 | 0.222 | 0.242 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.01 | 0.37 | -2.72 | 0.007 | 0.019 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.56 | 0.37 | -1.52 | 0.130 | 0.242 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.49, *p* = 0.094, η²_G = 0.011
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.89 | 23 | = 0.380 | -0.09 [-0.61, 0.24] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -1.94 | 23 | = 0.194 | -0.24 [-0.83, 0.04] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.41 | 23 | = 0.259 | -0.17 [-0.72, 0.14] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.055)
**N1 amplitude:** Significant main effect of condition (*p* = 0.032). Post-hoc tests revealed:
  - Decrease by 1 (no 1) showed greater amplitude than Decrease by 3 (no 1) (*d* = 0.39)
  - Decrease by 2 (no 1) showed greater amplitude than Decrease by 3 (no 1) (*d* = 0.33)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.066)
**P1 amplitude:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - Decrease by 1 (no 1) showed smaller amplitude than Decrease by 3 (no 1) (*d* = -0.45)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.094)

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
