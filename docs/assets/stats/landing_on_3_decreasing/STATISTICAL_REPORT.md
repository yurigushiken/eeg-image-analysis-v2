# Statistical Analysis Report: tables

**Generated:** 2025-10-23 18:59:14

---

## 1. Analysis Overview

**Total Measurements:** 288
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
| 4 to 3 | 23 | -4.05 µV | 1.92 | 0.40 | [-8.43, -0.80] |
| 5 to 3 | 24 | -3.70 µV | 2.30 | 0.47 | [-8.52, -0.14] |
| 6 to 3 | 23 | -4.26 µV | 1.88 | 0.39 | [-8.14, -0.89] |
| Cardinality3 | 23 | -3.06 µV | 1.76 | 0.37 | [-7.52, -0.40] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | 176.78 ms | 10.81 | 2.25 | [157.10, 207.20] |
| 5 to 3 | 24 | 176.27 ms | 10.94 | 2.23 | [153.65, 210.96] |
| 6 to 3 | 23 | 176.80 ms | 9.33 | 1.95 | [161.46, 203.24] |
| Cardinality3 | 23 | 175.90 ms | 12.73 | 2.65 | [151.93, 209.22] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 11 | 1.73 µV | 1.24 | 0.37 | [0.17, 4.40] |
| 5 to 3 | 17 | 1.81 µV | 1.17 | 0.28 | [0.25, 3.56] |
| 6 to 3 | 14 | 1.58 µV | 1.79 | 0.48 | [0.05, 6.60] |
| Cardinality3 | 13 | 2.24 µV | 1.94 | 0.54 | [0.09, 7.05] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 11 | 105.26 ms | 5.31 | 1.60 | [94.84, 112.76] |
| 5 to 3 | 17 | 108.07 ms | 4.34 | 1.05 | [98.40, 115.86] |
| 6 to 3 | 14 | 107.65 ms | 7.13 | 1.91 | [95.27, 119.64] |
| Cardinality3 | 13 | 106.75 ms | 5.04 | 1.40 | [95.89, 114.48] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 19 | 3.54 µV | 2.52 | 0.58 | [0.53, 8.69] |
| 5 to 3 | 20 | 3.39 µV | 1.64 | 0.37 | [0.40, 6.85] |
| 6 to 3 | 19 | 4.06 µV | 2.65 | 0.61 | [1.25, 11.29] |
| Cardinality3 | 15 | 2.61 µV | 1.92 | 0.50 | [0.28, 6.74] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 19 | 458.05 ms | 22.20 | 5.09 | [409.15, 495.67] |
| 5 to 3 | 20 | 460.14 ms | 20.30 | 4.54 | [407.46, 491.60] |
| 6 to 3 | 19 | 458.80 ms | 22.11 | 5.07 | [406.41, 502.51] |
| Cardinality3 | 15 | 448.46 ms | 20.38 | 5.26 | [410.44, 472.66] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 328.68, BIC = 346.41
- **5 to 3 vs 4 to 3**: *β* = 0.18, *SE* = 0.320, *z* = 0.570, *p* = 0.568
- **6 to 3 vs 4 to 3**: *β* = -0.11, *SE* = 0.323, *z* = -0.332, *p* = 0.740
- **Cardinality3 vs 4 to 3**: *β* = 0.47, *SE* = 0.333, *z* = 1.399, *p* = 0.162
- **SNR**: *β* = -0.36, *SE* = 0.051, *z* = -7.175, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.18 | 0.32 | -0.57 | 0.568 | 0.837 | n.s. |
| 4 to 3 - 6 to 3 | 0.11 | 0.32 | 0.33 | 0.740 | 0.837 | n.s. |
| 4 to 3 - Cardinality3 | -0.47 | 0.33 | -1.40 | 0.162 | 0.586 | n.s. |
| 5 to 3 - 6 to 3 | 0.29 | 0.32 | 0.91 | 0.364 | 0.837 | n.s. |
| 5 to 3 - Cardinality3 | -0.28 | 0.32 | -0.88 | 0.380 | 0.837 | n.s. |
| 6 to 3 - Cardinality3 | -0.57 | 0.33 | -1.73 | 0.084 | 0.409 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.16, *p* = 0.031, η²_G = 0.056
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -1.22 | 20 | = 0.296 | -0.21 [-0.73, 0.15] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.45 | 20 | = 0.657 | 0.10 [-0.40, 0.49] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -2.64 | 20 | = 0.061 | -0.56 [-1.05, -0.09] | medium | n.s. |
| 5 to 3 vs 6 to 3 | 1.48 | 20 | = 0.296 | 0.30 [-0.24, 0.63] | small | n.s. |
| 5 to 3 vs Cardinality3 | -1.19 | 20 | = 0.296 | -0.28 [-0.75, 0.14] | small | n.s. |
| 6 to 3 vs Cardinality3 | -2.52 | 20 | = 0.061 | -0.66 [-1.04, -0.08] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 667.42, BIC = 685.15
- **5 to 3 vs 4 to 3**: *β* = -0.27, *SE* = 1.757, *z* = -0.152, *p* = 0.879
- **6 to 3 vs 4 to 3**: *β* = 1.48, *SE* = 1.777, *z* = 0.834, *p* = 0.404
- **Cardinality3 vs 4 to 3**: *β* = -0.09, *SE* = 1.834, *z* = -0.046, *p* = 0.963
- **SNR**: *β* = 0.06, *SE* = 0.285, *z* = 0.214, *p* = 0.831

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.27 | 1.76 | 0.15 | 0.879 | 0.998 | n.s. |
| 4 to 3 - 6 to 3 | -1.48 | 1.78 | -0.83 | 0.404 | 0.916 | n.s. |
| 4 to 3 - Cardinality3 | 0.09 | 1.83 | 0.05 | 0.963 | 0.998 | n.s. |
| 5 to 3 - 6 to 3 | -1.75 | 1.76 | -1.00 | 0.319 | 0.900 | n.s. |
| 5 to 3 - Cardinality3 | -0.18 | 1.78 | -0.10 | 0.918 | 0.998 | n.s. |
| 6 to 3 - Cardinality3 | 1.57 | 1.83 | 0.86 | 0.391 | 0.916 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.33, *p* = 0.804, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.723 (ε = 0.673)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.14 | 20 | = 0.895 | 0.03 [-0.38, 0.48] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.78 | 20 | = 0.888 | -0.15 [-0.70, 0.20] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 0.21 | 20 | = 0.895 | 0.05 [-0.41, 0.48] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -1.03 | 20 | = 0.888 | -0.18 [-0.70, 0.18] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.13 | 20 | = 0.895 | 0.03 [-0.41, 0.46] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 1.09 | 20 | = 0.888 | 0.18 [-0.28, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 158.26, BIC = 172.31
- **5 to 3 vs 4 to 3**: *β* = -0.07, *SE* = 0.328, *z* = -0.227, *p* = 0.821
- **6 to 3 vs 4 to 3**: *β* = 0.19, *SE* = 0.345, *z* = 0.550, *p* = 0.582
- **Cardinality3 vs 4 to 3**: *β* = 0.69, *SE* = 0.348, *z* = 1.972, *p* = 0.049
- **SNR**: *β* = 0.67, *SE* = 0.075, *z* = 8.938, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.07 | 0.33 | 0.23 | 0.821 | 0.825 | n.s. |
| 4 to 3 - 6 to 3 | -0.19 | 0.34 | -0.55 | 0.582 | 0.825 | n.s. |
| 4 to 3 - Cardinality3 | -0.69 | 0.35 | -1.97 | 0.049 | 0.221 | n.s. |
| 5 to 3 - 6 to 3 | -0.26 | 0.31 | -0.85 | 0.394 | 0.777 | n.s. |
| 5 to 3 - Cardinality3 | -0.76 | 0.31 | -2.43 | 0.015 | 0.088 | n.s. |
| 6 to 3 - Cardinality3 | -0.50 | 0.32 | -1.53 | 0.125 | 0.414 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.27, *p* = 0.846, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.77 | 5 | = 0.938 | 0.34 [-0.65, 0.78] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.08 | 5 | = 0.938 | 0.04 [-0.74, 0.94] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -0.48 | 5 | = 0.938 | -0.25 [-1.07, 0.63] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.24 | 5 | = 0.938 | -0.17 [-0.57, 0.70] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -0.66 | 5 | = 0.938 | -0.44 [-0.82, 0.53] | small | n.s. |
| 6 to 3 vs Cardinality3 | -0.90 | 5 | = 0.938 | -0.24 [-1.12, 0.28] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 341.67, BIC = 355.72
- **5 to 3 vs 4 to 3**: *β* = 2.39, *SE* = 1.532, *z* = 1.562, *p* = 0.118
- **6 to 3 vs 4 to 3**: *β* = 2.42, *SE* = 1.627, *z* = 1.487, *p* = 0.137
- **Cardinality3 vs 4 to 3**: *β* = 0.71, *SE* = 1.640, *z* = 0.432, *p* = 0.666
- **SNR**: *β* = -0.43, *SE* = 0.358, *z* = -1.195, *p* = 0.232

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -2.39 | 1.53 | -1.56 | 0.118 | 0.530 | n.s. |
| 4 to 3 - 6 to 3 | -2.42 | 1.63 | -1.49 | 0.137 | 0.530 | n.s. |
| 4 to 3 - Cardinality3 | -0.71 | 1.64 | -0.43 | 0.666 | 0.888 | n.s. |
| 5 to 3 - 6 to 3 | -0.02 | 1.45 | -0.02 | 0.987 | 0.987 | n.s. |
| 5 to 3 - Cardinality3 | 1.68 | 1.47 | 1.14 | 0.252 | 0.688 | n.s. |
| 6 to 3 - Cardinality3 | 1.71 | 1.51 | 1.13 | 0.258 | 0.688 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.13, *p* = 0.942, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.12 | 5 | = 0.911 | 0.05 [-1.03, 0.43] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.41 | 5 | = 0.911 | -0.14 [-1.29, 0.46] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -0.41 | 5 | = 0.911 | -0.14 [-0.94, 0.74] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.39 | 5 | = 0.911 | -0.17 [-0.82, 0.46] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -0.51 | 5 | = 0.911 | -0.19 [-0.65, 0.69] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 0.15 | 5 | = 0.911 | 0.04 [-0.25, 1.17] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.00, BIC = 291.04
- **5 to 3 vs 4 to 3**: *β* = -0.11, *SE* = 0.405, *z* = -0.264, *p* = 0.792
- **6 to 3 vs 4 to 3**: *β* = 0.38, *SE* = 0.408, *z* = 0.928, *p* = 0.354
- **Cardinality3 vs 4 to 3**: *β* = -0.20, *SE* = 0.449, *z* = -0.447, *p* = 0.655
- **SNR**: *β* = 0.50, *SE* = 0.061, *z* = 8.270, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.11 | 0.40 | 0.26 | 0.792 | 0.959 | n.s. |
| 4 to 3 - 6 to 3 | -0.38 | 0.41 | -0.93 | 0.354 | 0.825 | n.s. |
| 4 to 3 - Cardinality3 | 0.20 | 0.45 | 0.45 | 0.655 | 0.959 | n.s. |
| 5 to 3 - 6 to 3 | -0.49 | 0.40 | -1.21 | 0.227 | 0.731 | n.s. |
| 5 to 3 - Cardinality3 | 0.09 | 0.44 | 0.21 | 0.831 | 0.959 | n.s. |
| 6 to 3 - Cardinality3 | 0.58 | 0.45 | 1.29 | 0.197 | 0.731 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.58, *p* = 0.211, η²_G = 0.058
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.07 | 13 | = 0.942 | -0.02 [-0.41, 0.59] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.69 | 13 | = 0.747 | -0.16 [-0.73, 0.28] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.54 | 13 | = 0.318 | 0.48 [-0.19, 1.01] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.50 | 13 | = 0.747 | -0.15 [-0.72, 0.26] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 1.49 | 13 | = 0.318 | 0.59 [-0.17, 0.98] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 1.83 | 13 | = 0.318 | 0.59 [-0.13, 1.03] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 659.06, BIC = 675.10
- **5 to 3 vs 4 to 3**: *β* = 1.78, *SE* = 5.922, *z* = 0.301, *p* = 0.764
- **6 to 3 vs 4 to 3**: *β* = 0.41, *SE* = 5.981, *z* = 0.069, *p* = 0.945
- **Cardinality3 vs 4 to 3**: *β* = -9.11, *SE* = 6.553, *z* = -1.391, *p* = 0.164
- **SNR**: *β* = 0.88, *SE* = 0.840, *z* = 1.043, *p* = 0.297

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -1.78 | 5.92 | -0.30 | 0.764 | 0.987 | n.s. |
| 4 to 3 - 6 to 3 | -0.41 | 5.98 | -0.07 | 0.945 | 0.987 | n.s. |
| 4 to 3 - Cardinality3 | 9.11 | 6.55 | 1.39 | 0.164 | 0.547 | n.s. |
| 5 to 3 - 6 to 3 | 1.37 | 5.90 | 0.23 | 0.817 | 0.987 | n.s. |
| 5 to 3 - Cardinality3 | 10.89 | 6.44 | 1.69 | 0.091 | 0.435 | n.s. |
| 6 to 3 - Cardinality3 | 9.53 | 6.56 | 1.45 | 0.147 | 0.547 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.57, *p* = 0.211, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.45 | 13 | = 0.657 | -0.17 [-0.54, 0.46] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -1.03 | 13 | = 0.539 | -0.32 [-0.47, 0.52] | small | n.s. |
| 4 to 3 vs Cardinality3 | 0.95 | 13 | = 0.539 | 0.36 [-0.33, 0.84] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.46 | 13 | = 0.657 | -0.16 [-0.48, 0.48] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 1.94 | 13 | = 0.224 | 0.58 [-0.10, 1.07] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 2.05 | 13 | = 0.224 | 0.76 [-0.00, 1.20] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.031) (no significant pairwise comparisons)

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
