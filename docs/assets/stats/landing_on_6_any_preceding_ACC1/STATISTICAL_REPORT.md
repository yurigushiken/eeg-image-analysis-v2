# Statistical Analysis Report: tables

**Generated:** 2025-10-20 22:01:41

---

## 1. Analysis Overview

**Total Measurements:** 264
**Number of Subjects:** 24
**Number of Conditions:** 4

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | -4.81 µV | 2.54 | 0.53 | [-10.71, -1.21] |
| 4 to 6 | 22 | -4.35 µV | 2.79 | 0.59 | [-12.58, 0.01] |
| 5 to 6 | 12 | -3.37 µV | 3.05 | 0.88 | [-9.34, -0.21] |
| 6 to 6 | 22 | -3.48 µV | 2.13 | 0.45 | [-7.46, -0.37] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 23 | 171.88 ms | 11.25 | 2.35 | [153.66, 194.64] |
| 4 to 6 | 22 | 172.61 ms | 12.07 | 2.57 | [150.60, 206.91] |
| 5 to 6 | 12 | 172.18 ms | 21.17 | 6.11 | [136.76, 203.68] |
| 6 to 6 | 22 | 173.41 ms | 12.91 | 2.75 | [154.01, 204.78] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 10 | 2.55 µV | 2.07 | 0.65 | [0.01, 7.02] |
| 4 to 6 | 13 | 2.38 µV | 1.21 | 0.33 | [0.70, 4.48] |
| 5 to 6 | 13 | 3.23 µV | 2.93 | 0.81 | [0.51, 8.80] |
| 6 to 6 | 13 | 1.49 µV | 1.29 | 0.36 | [-0.03, 3.81] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 10 | 90.74 ms | 6.63 | 2.10 | [80.88, 99.72] |
| 4 to 6 | 13 | 95.47 ms | 5.11 | 1.42 | [85.14, 104.40] |
| 5 to 6 | 13 | 96.98 ms | 5.62 | 1.56 | [89.52, 107.30] |
| 6 to 6 | 13 | 93.64 ms | 7.79 | 2.16 | [80.20, 107.82] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 3.05 µV | 1.97 | 0.45 | [0.47, 9.29] |
| 4 to 6 | 19 | 3.96 µV | 2.90 | 0.66 | [0.19, 9.35] |
| 5 to 6 | 9 | 4.10 µV | 2.18 | 0.73 | [1.62, 9.20] |
| 6 to 6 | 14 | 3.09 µV | 2.15 | 0.58 | [0.54, 8.23] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 6 | 19 | 473.58 ms | 10.80 | 2.48 | [451.04, 499.64] |
| 4 to 6 | 19 | 472.24 ms | 15.08 | 3.46 | [436.96, 500.57] |
| 5 to 6 | 9 | 476.24 ms | 11.77 | 3.92 | [456.69, 497.44] |
| 6 to 6 | 14 | 473.89 ms | 10.12 | 2.70 | [456.46, 497.37] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 320.34, BIC = 336.92
- **4 to 6 vs 3 to 6**: *β* = 0.92, *SE* = 0.487, *z* = 1.886, *p* = 0.059
- **5 to 6 vs 3 to 6**: *β* = -0.17, *SE* = 0.611, *z* = -0.271, *p* = 0.787
- **6 to 6 vs 3 to 6**: *β* = 0.88, *SE* = 0.487, *z* = 1.795, *p* = 0.073
- **SNR**: *β* = -0.74, *SE* = 0.080, *z* = -9.261, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.92 | 0.49 | -1.89 | 0.059 | 0.307 | n.s. |
| 3 to 6 - 5 to 6 | 0.17 | 0.61 | 0.27 | 0.787 | 0.954 | n.s. |
| 3 to 6 - 6 to 6 | -0.87 | 0.49 | -1.80 | 0.073 | 0.314 | n.s. |
| 4 to 6 - 5 to 6 | 1.08 | 0.63 | 1.72 | 0.085 | 0.314 | n.s. |
| 4 to 6 - 6 to 6 | 0.04 | 0.50 | 0.09 | 0.930 | 0.954 | n.s. |
| 5 to 6 - 6 to 6 | -1.04 | 0.60 | -1.72 | 0.086 | 0.314 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.56, *p* = 0.217, η²_G = 0.078
- Greenhouse-Geisser corrected: *p* = 0.238 (ε = 0.460)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -2.42 | 11 | = 0.102 | -0.63 [-0.59, 0.33] | medium | n.s. |
| 3 to 6 vs 5 to 6 | -1.26 | 11 | = 0.465 | -0.56 [-1.02, 0.29] | medium | n.s. |
| 3 to 6 vs 6 to 6 | -3.50 | 11 | = 0.030 | -0.72 [-1.23, -0.21] | medium | * |
| 4 to 6 vs 5 to 6 | -0.40 | 11 | = 0.837 | -0.15 [-0.75, 0.52] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | -0.86 | 11 | = 0.616 | -0.23 [-0.92, 0.03] | small | n.s. |
| 5 to 6 vs 6 to 6 | -0.01 | 11 | = 0.991 | -0.00 [-0.64, 0.63] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 615.16, BIC = 631.74
- **4 to 6 vs 3 to 6**: *β* = -1.08, *SE* = 2.499, *z* = -0.432, *p* = 0.665
- **5 to 6 vs 3 to 6**: *β* = -0.75, *SE* = 3.276, *z* = -0.229, *p* = 0.819
- **6 to 6 vs 3 to 6**: *β* = 0.71, *SE* = 2.485, *z* = 0.288, *p* = 0.774
- **SNR**: *β* = -0.05, *SE* = 0.577, *z* = -0.087, *p* = 0.931

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 1.08 | 2.50 | 0.43 | 0.665 | 0.994 | n.s. |
| 3 to 6 - 5 to 6 | 0.75 | 3.28 | 0.23 | 0.819 | 0.994 | n.s. |
| 3 to 6 - 6 to 6 | -0.72 | 2.48 | -0.29 | 0.774 | 0.994 | n.s. |
| 4 to 6 - 5 to 6 | -0.33 | 3.46 | -0.10 | 0.924 | 0.994 | n.s. |
| 4 to 6 - 6 to 6 | -1.80 | 2.59 | -0.69 | 0.488 | 0.982 | n.s. |
| 5 to 6 - 6 to 6 | -1.47 | 3.16 | -0.46 | 0.643 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.53, *p* = 0.665, η²_G = 0.015
- Greenhouse-Geisser corrected: *p* = 0.554 (ε = 0.517)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | 1.03 | 11 | = 0.689 | 0.17 [-0.19, 0.74] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | 0.03 | 11 | = 0.976 | 0.01 [-0.63, 0.64] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | -0.99 | 11 | = 0.689 | -0.26 [-0.57, 0.35] | small | n.s. |
| 4 to 6 vs 5 to 6 | -0.34 | 11 | = 0.891 | -0.10 [-0.73, 0.54] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | -2.31 | 11 | = 0.248 | -0.40 [-0.71, 0.22] | small | n.s. |
| 5 to 6 vs 6 to 6 | -0.58 | 11 | = 0.862 | -0.18 [-0.81, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 157.31, BIC = 170.55
- **4 to 6 vs 3 to 6**: *β* = 0.49, *SE* = 0.419, *z* = 1.159, *p* = 0.247
- **5 to 6 vs 3 to 6**: *β* = 0.94, *SE* = 0.440, *z* = 2.132, *p* = 0.033
- **6 to 6 vs 3 to 6**: *β* = -0.09, *SE* = 0.447, *z* = -0.204, *p* = 0.838
- **SNR**: *β* = 1.03, *SE* = 0.083, *z* = 12.323, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -0.49 | 0.42 | -1.16 | 0.247 | 0.572 | n.s. |
| 3 to 6 - 5 to 6 | -0.94 | 0.44 | -2.13 | 0.033 | 0.154 | n.s. |
| 3 to 6 - 6 to 6 | 0.09 | 0.45 | 0.20 | 0.838 | 0.838 | n.s. |
| 4 to 6 - 5 to 6 | -0.45 | 0.39 | -1.15 | 0.249 | 0.572 | n.s. |
| 4 to 6 - 6 to 6 | 0.58 | 0.40 | 1.45 | 0.146 | 0.468 | n.s. |
| 5 to 6 - 6 to 6 | 1.03 | 0.41 | 2.48 | 0.013 | 0.076 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.753, η²_G = 0.139
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.44 | 2 | = 0.832 | -0.32 [-0.75, 0.92] | small | n.s. |
| 3 to 6 vs 5 to 6 | -0.33 | 2 | = 0.832 | -0.36 [-1.29, 1.20] | small | n.s. |
| 3 to 6 vs 6 to 6 | 0.89 | 2 | = 0.832 | 0.59 [-0.61, 1.62] | medium | n.s. |
| 4 to 6 vs 5 to 6 | -0.24 | 2 | = 0.832 | -0.18 [-0.74, 0.94] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | 11.06 | 2 | = 0.048 | 1.08 [0.16, 2.88] | large | * |
| 5 to 6 vs 6 to 6 | 0.91 | 2 | = 0.832 | 0.74 [-0.53, 1.40] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 326.46, BIC = 339.70
- **4 to 6 vs 3 to 6**: *β* = 4.72, *SE* = 2.303, *z* = 2.051, *p* = 0.040
- **5 to 6 vs 3 to 6**: *β* = 5.82, *SE* = 2.356, *z* = 2.470, *p* = 0.014
- **6 to 6 vs 3 to 6**: *β* = 3.04, *SE* = 2.382, *z* = 1.278, *p* = 0.201
- **SNR**: *β* = 0.69, *SE* = 0.530, *z* = 1.301, *p* = 0.193

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | -4.72 | 2.30 | -2.05 | 0.040 | 0.186 | n.s. |
| 3 to 6 - 5 to 6 | -5.82 | 2.36 | -2.47 | 0.014 | 0.078 | n.s. |
| 3 to 6 - 6 to 6 | -3.04 | 2.38 | -1.28 | 0.201 | 0.592 | n.s. |
| 4 to 6 - 5 to 6 | -1.10 | 2.14 | -0.51 | 0.607 | 0.682 | n.s. |
| 4 to 6 - 6 to 6 | 1.68 | 2.16 | 0.78 | 0.436 | 0.682 | n.s. |
| 5 to 6 - 6 to 6 | 2.78 | 2.17 | 1.28 | 0.201 | 0.592 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.239, η²_G = 0.261
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -1.58 | 2 | = 0.364 | -0.84 [-1.50, 0.31] | large | n.s. |
| 3 to 6 vs 5 to 6 | -1.86 | 2 | = 0.364 | -1.06 [-2.39, 0.56] | large | n.s. |
| 3 to 6 vs 6 to 6 | 0.02 | 2 | = 0.986 | 0.02 [-1.21, 0.90] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -1.53 | 2 | = 0.364 | -0.47 [-1.75, 0.17] | small | n.s. |
| 4 to 6 vs 6 to 6 | 1.37 | 2 | = 0.364 | 0.83 [-0.65, 1.24] | large | n.s. |
| 5 to 6 vs 6 to 6 | 2.70 | 2 | = 0.364 | 1.05 [-0.69, 1.19] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 236.92, BIC = 251.70
- **4 to 6 vs 3 to 6**: *β* = -0.01, *SE* = 0.427, *z* = -0.015, *p* = 0.988
- **5 to 6 vs 3 to 6**: *β* = 1.46, *SE* = 0.529, *z* = 2.765, *p* = 0.006
- **6 to 6 vs 3 to 6**: *β* = -0.07, *SE* = 0.446, *z* = -0.168, *p* = 0.867
- **SNR**: *β* = 0.64, *SE* = 0.088, *z* = 7.345, *p* < .001

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 0.01 | 0.43 | 0.01 | 0.988 | 0.998 | n.s. |
| 3 to 6 - 5 to 6 | -1.46 | 0.53 | -2.77 | 0.006 | 0.034 | * |
| 3 to 6 - 6 to 6 | 0.07 | 0.45 | 0.17 | 0.867 | 0.998 | n.s. |
| 4 to 6 - 5 to 6 | -1.47 | 0.57 | -2.56 | 0.011 | 0.042 | * |
| 4 to 6 - 6 to 6 | 0.07 | 0.46 | 0.15 | 0.881 | 0.998 | n.s. |
| 5 to 6 - 6 to 6 | 1.54 | 0.57 | 2.71 | 0.007 | 0.034 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.42, *p* = 0.270, η²_G = 0.100
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -2.18 | 6 | = 0.435 | -0.79 [-0.98, 0.10] | medium | n.s. |
| 3 to 6 vs 5 to 6 | -0.82 | 6 | = 0.581 | -0.44 [-1.07, 0.50] | small | n.s. |
| 3 to 6 vs 6 to 6 | -0.58 | 6 | = 0.581 | -0.20 [-0.79, 0.43] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | 0.72 | 6 | = 0.581 | 0.32 [-0.43, 1.16] | small | n.s. |
| 4 to 6 vs 6 to 6 | 1.64 | 6 | = 0.458 | 0.63 [-0.11, 1.18] | medium | n.s. |
| 5 to 6 vs 6 to 6 | 0.68 | 6 | = 0.581 | 0.29 [-0.68, 1.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 489.07, BIC = 503.84
- **4 to 6 vs 3 to 6**: *β* = -0.96, *SE* = 3.940, *z* = -0.243, *p* = 0.808
- **5 to 6 vs 3 to 6**: *β* = 2.48, *SE* = 4.811, *z* = 0.516, *p* = 0.606
- **6 to 6 vs 3 to 6**: *β* = 0.48, *SE* = 4.159, *z* = 0.116, *p* = 0.908
- **SNR**: *β* = -0.19, *SE* = 0.653, *z* = -0.291, *p* = 0.771

_Reference condition: **3 to 6** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 6 - 4 to 6 | 0.96 | 3.94 | 0.24 | 0.808 | 0.992 | n.s. |
| 3 to 6 - 5 to 6 | -2.48 | 4.81 | -0.52 | 0.606 | 0.991 | n.s. |
| 3 to 6 - 6 to 6 | -0.48 | 4.16 | -0.12 | 0.908 | 0.992 | n.s. |
| 4 to 6 - 5 to 6 | -3.44 | 5.05 | -0.68 | 0.496 | 0.984 | n.s. |
| 4 to 6 - 6 to 6 | -1.44 | 4.19 | -0.34 | 0.731 | 0.992 | n.s. |
| 5 to 6 - 6 to 6 | 2.00 | 5.12 | 0.39 | 0.696 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.00, *p* = 1.000, η²_G = 0.001
- Greenhouse-Geisser corrected: *p* = 0.995 (ε = 0.639)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 6 vs 4 to 6 | -0.01 | 6 | = 0.991 | -0.01 [-0.63, 0.40] | negligible | n.s. |
| 3 to 6 vs 5 to 6 | -0.10 | 6 | = 0.991 | -0.06 [-1.04, 0.52] | negligible | n.s. |
| 3 to 6 vs 6 to 6 | -0.06 | 6 | = 0.991 | -0.03 [-0.64, 0.57] | negligible | n.s. |
| 4 to 6 vs 5 to 6 | -0.09 | 6 | = 0.991 | -0.04 [-0.87, 0.67] | negligible | n.s. |
| 4 to 6 vs 6 to 6 | -0.02 | 6 | = 0.991 | -0.01 [-0.77, 0.45] | negligible | n.s. |
| 5 to 6 vs 6 to 6 | 0.05 | 6 | = 0.991 | 0.04 [-0.90, 0.95] | negligible | n.s. |

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

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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

- Python 3.12.4
- MNE-Python 1.9.0
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
