# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:29:59

---

## 1. Analysis Overview

**Total Measurements:** 192
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
| 1a | 24 | 106.33 ms | 2.01 | 0.41 | [104.00, 108.00] |
| 1b | 24 | 105.83 ms | 2.04 | 0.42 | [104.00, 108.00] |
| 1c | 24 | 106.17 ms | 2.04 | 0.42 | [104.00, 108.00] |
| 1d | 24 | 106.17 ms | 2.04 | 0.42 | [104.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | -2.08 µV | 5.13 | 1.05 | [-13.01, 12.78] |
| 1b | 24 | -0.85 µV | 4.26 | 0.87 | [-8.31, 12.09] |
| 1c | 24 | -0.56 µV | 3.45 | 0.70 | [-6.47, 7.95] |
| 1d | 24 | -3.36 µV | 3.49 | 0.71 | [-13.43, 2.22] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | 176.00 ms | 16.43 | 3.35 | [152.00, 200.00] |
| 1b | 24 | 178.00 ms | 14.45 | 2.95 | [152.00, 200.00] |
| 1c | 24 | 176.67 ms | 17.16 | 3.50 | [152.00, 200.00] |
| 1d | 24 | 180.17 ms | 15.31 | 3.13 | [152.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 24 | -2.97 µV | 3.97 | 0.81 | [-10.68, 3.48] |
| 1b | 24 | -3.07 µV | 4.15 | 0.85 | [-16.54, 4.63] |
| 1c | 24 | -4.40 µV | 3.37 | 0.69 | [-10.88, 1.05] |
| 1d | 24 | -3.43 µV | 3.25 | 0.66 | [-11.92, 4.70] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 128.62 ms | 12.20 | 3.38 | [108.00, 144.00] |
| 1b | 17 | 123.29 ms | 13.28 | 3.22 | [100.00, 144.00] |
| 1c | 16 | 123.00 ms | 16.75 | 4.19 | [100.00, 144.00] |
| 1d | 14 | 125.43 ms | 10.94 | 2.92 | [108.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 6.72 µV | 3.58 | 0.99 | [2.63, 15.32] |
| 1b | 17 | 6.01 µV | 3.14 | 0.76 | [2.13, 13.34] |
| 1c | 16 | 6.05 µV | 3.89 | 0.97 | [1.42, 15.74] |
| 1d | 14 | 6.21 µV | 2.99 | 0.80 | [1.34, 10.50] |


### 2.4 P3b Component

#### Latency (Peak)

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 417.42, BIC = 435.37
- **1b vs 1a**: *β* = -0.48, *SE* = 0.549, *z* = -0.867, *p* = 0.386
- **1c vs 1a**: *β* = -0.18, *SE* = 0.548, *z* = -0.331, *p* = 0.741
- **1d vs 1a**: *β* = -0.15, *SE* = 0.548, *z* = -0.280, *p* = 0.780
- **SNR**: *β* = -0.08, *SE* = 0.152, *z* = -0.540, *p* = 0.589

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 0.48 | 0.55 | 0.87 | 0.386 | 0.946 | n.s. |
| 1a - 1c | 0.18 | 0.55 | 0.33 | 0.741 | 0.983 | n.s. |
| 1a - 1d | 0.15 | 0.55 | 0.28 | 0.780 | 0.983 | n.s. |
| 1b - 1c | -0.29 | 0.55 | -0.53 | 0.594 | 0.983 | n.s. |
| 1b - 1d | -0.32 | 0.55 | -0.59 | 0.556 | 0.983 | n.s. |
| 1c - 1d | -0.03 | 0.55 | -0.05 | 0.959 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.843, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.83 | 23 | = 0.924 | 0.25 [-0.26, 0.59] | small | n.s. |
| 1a vs 1c | 0.33 | 23 | = 0.924 | 0.08 [-0.36, 0.49] | negligible | n.s. |
| 1a vs 1d | 0.30 | 23 | = 0.924 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| 1b vs 1c | -0.57 | 23 | = 0.924 | -0.16 [-0.54, 0.31] | negligible | n.s. |
| 1b vs 1d | -0.53 | 23 | = 0.924 | -0.16 [-0.53, 0.32] | negligible | n.s. |
| 1c vs 1d | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 553.27, BIC = 571.22
- **1b vs 1a**: *β* = 1.32, *SE* = 1.127, *z* = 1.170, *p* = 0.242
- **1c vs 1a**: *β* = 1.48, *SE* = 1.125, *z* = 1.313, *p* = 0.189
- **1d vs 1a**: *β* = -1.23, *SE* = 1.124, *z* = -1.091, *p* = 0.275
- **SNR**: *β* = -0.29, *SE* = 0.286, *z* = -1.013, *p* = 0.311

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -1.32 | 1.13 | -1.17 | 0.242 | 0.568 | n.s. |
| 1a - 1c | -1.48 | 1.12 | -1.31 | 0.189 | 0.568 | n.s. |
| 1a - 1d | 1.23 | 1.12 | 1.09 | 0.275 | 0.568 | n.s. |
| 1b - 1c | -0.16 | 1.13 | -0.14 | 0.889 | 0.889 | n.s. |
| 1b - 1d | 2.55 | 1.12 | 2.26 | 0.024 | 0.112 | n.s. |
| 1c - 1d | 2.70 | 1.13 | 2.40 | 0.017 | 0.095 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.50, *p* = 0.067, η²_G = 0.070
- Greenhouse-Geisser corrected: *p* = 0.088 (ε = 0.724)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.82 | 23 | = 0.504 | -0.26 [-0.59, 0.26] | small | n.s. |
| 1a vs 1c | -1.31 | 23 | = 0.305 | -0.35 [-0.70, 0.16] | small | n.s. |
| 1a vs 1d | 1.37 | 23 | = 0.305 | 0.29 [-0.15, 0.71] | small | n.s. |
| 1b vs 1c | -0.31 | 23 | = 0.762 | -0.08 [-0.49, 0.36] | negligible | n.s. |
| 1b vs 1d | 2.04 | 23 | = 0.158 | 0.64 [-0.02, 0.86] | medium | n.s. |
| 1c vs 1d | 2.84 | 23 | = 0.056 | 0.81 [0.12, 1.04] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 798.58, BIC = 816.53
- **1b vs 1a**: *β* = 2.79, *SE* = 3.689, *z* = 0.757, *p* = 0.449
- **1c vs 1a**: *β* = 1.15, *SE* = 3.651, *z* = 0.315, *p* = 0.753
- **1d vs 1a**: *β* = 4.36, *SE* = 3.633, *z* = 1.200, *p* = 0.230
- **SNR**: *β* = -1.09, *SE* = 0.907, *z* = -1.205, *p* = 0.228

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -2.79 | 3.69 | -0.76 | 0.449 | 0.908 | n.s. |
| 1a - 1c | -1.15 | 3.65 | -0.32 | 0.753 | 0.958 | n.s. |
| 1a - 1d | -4.36 | 3.63 | -1.20 | 0.230 | 0.792 | n.s. |
| 1b - 1c | 1.64 | 3.64 | 0.45 | 0.652 | 0.958 | n.s. |
| 1b - 1d | -1.57 | 3.66 | -0.43 | 0.669 | 0.958 | n.s. |
| 1c - 1d | -3.21 | 3.64 | -0.88 | 0.378 | 0.907 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.49, *p* = 0.692, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.60 | 23 | = 0.831 | -0.13 [-0.55, 0.30] | negligible | n.s. |
| 1a vs 1c | -0.14 | 23 | = 0.888 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| 1a vs 1d | -1.09 | 23 | = 0.831 | -0.26 [-0.65, 0.20] | small | n.s. |
| 1b vs 1c | 0.39 | 23 | = 0.841 | 0.08 [-0.34, 0.50] | negligible | n.s. |
| 1b vs 1d | -0.77 | 23 | = 0.831 | -0.15 [-0.58, 0.27] | negligible | n.s. |
| 1c vs 1d | -0.88 | 23 | = 0.831 | -0.22 [-0.61, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 515.22, BIC = 533.17
- **1b vs 1a**: *β* = 0.21, *SE* = 0.845, *z* = 0.249, *p* = 0.803
- **1c vs 1a**: *β* = -1.24, *SE* = 0.836, *z* = -1.483, *p* = 0.138
- **1d vs 1a**: *β* = -0.38, *SE* = 0.832, *z* = -0.460, *p* = 0.645
- **SNR**: *β* = -0.43, *SE* = 0.210, *z* = -2.031, *p* = 0.042

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -0.21 | 0.84 | -0.25 | 0.803 | 0.874 | n.s. |
| 1a - 1c | 1.24 | 0.84 | 1.48 | 0.138 | 0.524 | n.s. |
| 1a - 1d | 0.38 | 0.83 | 0.46 | 0.645 | 0.874 | n.s. |
| 1b - 1c | 1.45 | 0.83 | 1.74 | 0.082 | 0.400 | n.s. |
| 1b - 1d | 0.59 | 0.84 | 0.71 | 0.479 | 0.859 | n.s. |
| 1c - 1d | -0.86 | 0.83 | -1.03 | 0.303 | 0.764 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.16, *p* = 0.331, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.11 | 23 | = 0.915 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| 1a vs 1c | 1.62 | 23 | = 0.364 | 0.39 [-0.10, 0.76] | small | n.s. |
| 1a vs 1d | 0.49 | 23 | = 0.785 | 0.13 [-0.32, 0.52] | negligible | n.s. |
| 1b vs 1c | 1.51 | 23 | = 0.364 | 0.35 [-0.12, 0.74] | small | n.s. |
| 1b vs 1d | 0.45 | 23 | = 0.785 | 0.10 [-0.33, 0.52] | negligible | n.s. |
| 1c vs 1d | -1.38 | 23 | = 0.364 | -0.29 [-0.71, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 485.65, BIC = 500.31
- **1b vs 1a**: *β* = -5.04, *SE* = 3.964, *z* = -1.271, *p* = 0.204
- **1c vs 1a**: *β* = -6.58, *SE* = 3.955, *z* = -1.663, *p* = 0.096
- **1d vs 1a**: *β* = -1.90, *SE* = 4.036, *z* = -0.471, *p* = 0.638
- **SNR**: *β* = 0.28, *SE* = 0.510, *z* = 0.539, *p* = 0.590

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 5.04 | 3.96 | 1.27 | 0.204 | 0.680 | n.s. |
| 1a - 1c | 6.58 | 3.96 | 1.66 | 0.096 | 0.456 | n.s. |
| 1a - 1d | 1.90 | 4.04 | 0.47 | 0.638 | 0.869 | n.s. |
| 1b - 1c | 1.54 | 3.74 | 0.41 | 0.681 | 0.869 | n.s. |
| 1b - 1d | -3.14 | 3.80 | -0.83 | 0.409 | 0.794 | n.s. |
| 1c - 1d | -4.68 | 3.90 | -1.20 | 0.230 | 0.680 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.92, *p* = 0.452, η²_G = 0.081
- Greenhouse-Geisser corrected: *p* = 0.389 (ε = 0.399)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.98 | 6 | = 0.549 | 0.59 [-0.44, 0.92] | medium | n.s. |
| 1a vs 1c | 3.38 | 6 | = 0.089 | 0.68 [0.19, 2.20] | medium | n.s. |
| 1a vs 1d | 1.92 | 6 | = 0.268 | 0.44 [-0.59, 0.85] | small | n.s. |
| 1b vs 1c | 0.07 | 6 | = 0.948 | 0.04 [-0.46, 0.82] | negligible | n.s. |
| 1b vs 1d | -0.50 | 6 | = 0.764 | -0.28 [-0.95, 0.42] | small | n.s. |
| 1c vs 1d | -1.73 | 6 | = 0.268 | -0.36 [-1.19, 0.31] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 313.46, BIC = 328.12
- **1b vs 1a**: *β* = -1.07, *SE* = 0.968, *z* = -1.109, *p* = 0.267
- **1c vs 1a**: *β* = -0.87, *SE* = 0.963, *z* = -0.903, *p* = 0.367
- **1d vs 1a**: *β* = -0.23, *SE* = 0.991, *z* = -0.232, *p* = 0.816
- **SNR**: *β* = 0.19, *SE* = 0.132, *z* = 1.446, *p* = 0.148

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 1.07 | 0.97 | 1.11 | 0.267 | 0.845 | n.s. |
| 1a - 1c | 0.87 | 0.96 | 0.90 | 0.367 | 0.896 | n.s. |
| 1a - 1d | 0.23 | 0.99 | 0.23 | 0.816 | 0.966 | n.s. |
| 1b - 1c | -0.20 | 0.92 | -0.22 | 0.824 | 0.966 | n.s. |
| 1b - 1d | -0.84 | 0.93 | -0.91 | 0.364 | 0.896 | n.s. |
| 1c - 1d | -0.64 | 0.96 | -0.67 | 0.504 | 0.896 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.392, η²_G = 0.086
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.24 | 6 | = 0.821 | -0.12 [-0.59, 0.76] | negligible | n.s. |
| 1a vs 1c | 0.55 | 6 | = 0.720 | 0.18 [-0.44, 1.14] | negligible | n.s. |
| 1a vs 1d | -1.10 | 6 | = 0.628 | -0.54 [-0.88, 0.56] | medium | n.s. |
| 1b vs 1c | 0.66 | 6 | = 0.720 | 0.33 [-0.59, 0.68] | small | n.s. |
| 1b vs 1d | -1.27 | 6 | = 0.628 | -0.48 [-1.20, 0.22] | small | n.s. |
| 1c vs 1d | -1.52 | 6 | = 0.628 | -0.73 [-1.16, 0.33] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.067)

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
