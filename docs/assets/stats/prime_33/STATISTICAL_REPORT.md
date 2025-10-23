# Statistical Analysis Report: tables

**Generated:** 2025-10-23 19:01:29

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
| 3a | 20 | -3.20 µV | 2.07 | 0.46 | [-8.22, -0.24] |
| 3b | 14 | -3.63 µV | 3.19 | 0.85 | [-12.36, -0.32] |
| 3c | 20 | -3.62 µV | 2.23 | 0.50 | [-7.86, -0.64] |
| 3d | 22 | -4.20 µV | 2.45 | 0.52 | [-8.94, -0.46] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 20 | 169.41 ms | 12.99 | 2.90 | [143.87, 190.62] |
| 3b | 14 | 179.47 ms | 11.24 | 3.00 | [160.69, 197.42] |
| 3c | 20 | 173.47 ms | 14.80 | 3.31 | [145.85, 204.52] |
| 3d | 22 | 175.28 ms | 13.12 | 2.80 | [143.94, 202.29] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 4.02 µV | 3.43 | 0.86 | [-0.21, 13.16] |
| 3b | 11 | 3.81 µV | 3.27 | 0.99 | [0.91, 11.51] |
| 3c | 12 | 2.47 µV | 1.46 | 0.42 | [0.09, 5.42] |
| 3d | 9 | 1.84 µV | 1.61 | 0.54 | [0.20, 5.27] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 106.46 ms | 5.19 | 1.30 | [97.60, 118.86] |
| 3b | 11 | 107.93 ms | 4.73 | 1.43 | [98.79, 115.49] |
| 3c | 12 | 107.70 ms | 6.58 | 1.90 | [93.08, 118.14] |
| 3d | 9 | 109.37 ms | 7.84 | 2.61 | [94.73, 117.61] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 4.34 µV | 3.17 | 0.79 | [0.14, 11.00] |
| 3b | 11 | 4.05 µV | 2.76 | 0.83 | [0.13, 8.01] |
| 3c | 11 | 4.79 µV | 1.70 | 0.51 | [1.22, 6.81] |
| 3d | 15 | 3.23 µV | 3.50 | 0.90 | [0.07, 14.17] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 16 | 455.68 ms | 11.40 | 2.85 | [432.15, 469.59] |
| 3b | 11 | 454.44 ms | 7.80 | 2.35 | [432.88, 461.30] |
| 3c | 11 | 456.29 ms | 6.54 | 1.97 | [441.04, 465.78] |
| 3d | 15 | 456.28 ms | 13.38 | 3.45 | [435.54, 478.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 320.31, BIC = 336.63
- **3b vs 3a**: *β* = -0.29, *SE* = 0.602, *z* = -0.487, *p* = 0.627
- **3c vs 3a**: *β* = -0.46, *SE* = 0.544, *z* = -0.849, *p* = 0.396
- **3d vs 3a**: *β* = -0.18, *SE* = 0.543, *z* = -0.330, *p* = 0.741
- **SNR**: *β* = -0.88, *SE* = 0.121, *z* = -7.265, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.29 | 0.60 | 0.49 | 0.627 | 0.990 | n.s. |
| 3a - 3c | 0.46 | 0.54 | 0.85 | 0.396 | 0.951 | n.s. |
| 3a - 3d | 0.18 | 0.54 | 0.33 | 0.741 | 0.990 | n.s. |
| 3b - 3c | 0.17 | 0.60 | 0.28 | 0.780 | 0.990 | n.s. |
| 3b - 3d | -0.11 | 0.61 | -0.19 | 0.852 | 0.990 | n.s. |
| 3c - 3d | -0.28 | 0.55 | -0.52 | 0.606 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.94, *p* = 0.437, η²_G = 0.066
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.38 | 9 | = 0.814 | 0.12 [-0.42, 0.74] | negligible | n.s. |
| 3a vs 3c | 1.55 | 9 | = 0.468 | 0.62 [-0.39, 0.65] | medium | n.s. |
| 3a vs 3d | 1.55 | 9 | = 0.468 | 0.77 [-0.15, 0.88] | medium | n.s. |
| 3b vs 3c | 0.80 | 9 | = 0.665 | 0.32 [-0.63, 0.64] | small | n.s. |
| 3b vs 3d | 0.87 | 9 | = 0.665 | 0.41 [-0.25, 1.07] | small | n.s. |
| 3c vs 3d | 0.24 | 9 | = 0.814 | 0.11 [-0.36, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 612.22, BIC = 628.54
- **3b vs 3a**: *β* = 9.91, *SE* = 3.833, *z* = 2.584, *p* = 0.010
- **3c vs 3a**: *β* = 4.20, *SE* = 3.478, *z* = 1.206, *p* = 0.228
- **3d vs 3a**: *β* = 6.18, *SE* = 3.501, *z* = 1.764, *p* = 0.078
- **SNR**: *β* = -0.42, *SE* = 0.835, *z* = -0.502, *p* = 0.616

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -9.91 | 3.83 | -2.58 | 0.010 | 0.057 | n.s. |
| 3a - 3c | -4.20 | 3.48 | -1.21 | 0.228 | 0.539 | n.s. |
| 3a - 3d | -6.18 | 3.50 | -1.76 | 0.078 | 0.333 | n.s. |
| 3b - 3c | 5.71 | 3.89 | 1.47 | 0.142 | 0.457 | n.s. |
| 3b - 3d | 3.73 | 3.91 | 0.95 | 0.340 | 0.564 | n.s. |
| 3c - 3d | -1.98 | 3.52 | -0.56 | 0.574 | 0.574 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.351, η²_G = 0.078
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -1.52 | 9 | = 0.486 | -0.73 [-1.23, 0.02] | medium | n.s. |
| 3a vs 3c | -0.37 | 9 | = 0.722 | -0.14 [-0.73, 0.31] | negligible | n.s. |
| 3a vs 3d | -0.81 | 9 | = 0.549 | -0.38 [-0.77, 0.24] | small | n.s. |
| 3b vs 3c | 1.55 | 9 | = 0.486 | 0.68 [-0.44, 0.84] | medium | n.s. |
| 3b vs 3d | 0.78 | 9 | = 0.549 | 0.28 [-0.21, 1.12] | small | n.s. |
| 3c vs 3d | -0.78 | 9 | = 0.549 | -0.29 [-0.72, 0.29] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 218.43, BIC = 231.53
- **3b vs 3a**: *β* = -0.39, *SE* = 0.569, *z* = -0.680, *p* = 0.497
- **3c vs 3a**: *β* = -0.32, *SE* = 0.611, *z* = -0.519, *p* = 0.604
- **3d vs 3a**: *β* = -1.07, *SE* = 0.625, *z* = -1.720, *p* = 0.085
- **SNR**: *β* = 0.71, *SE* = 0.156, *z* = 4.569, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.39 | 0.57 | 0.68 | 0.497 | 0.872 | n.s. |
| 3a - 3c | 0.32 | 0.61 | 0.52 | 0.604 | 0.872 | n.s. |
| 3a - 3d | 1.07 | 0.62 | 1.72 | 0.085 | 0.415 | n.s. |
| 3b - 3c | -0.07 | 0.69 | -0.10 | 0.919 | 0.919 | n.s. |
| 3b - 3d | 0.69 | 0.67 | 1.03 | 0.302 | 0.791 | n.s. |
| 3c - 3d | 0.76 | 0.69 | 1.11 | 0.269 | 0.791 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.87, *p* = 0.493, η²_G = 0.133
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.84 | 3 | = 0.790 | 0.52 [-0.53, 1.03] | medium | n.s. |
| 3a vs 3c | 1.16 | 3 | = 0.790 | 0.63 [-0.61, 1.08] | medium | n.s. |
| 3a vs 3d | 4.08 | 3 | = 0.159 | 2.28 [0.73, 3.98] | large | n.s. |
| 3b vs 3c | 0.11 | 3 | = 0.919 | 0.04 [-0.98, 1.55] | negligible | n.s. |
| 3b vs 3d | 0.49 | 3 | = 0.790 | 0.40 [-0.60, 1.31] | small | n.s. |
| 3c vs 3d | 0.57 | 3 | = 0.790 | 0.37 [-0.93, 1.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 317.87, BIC = 330.97
- **3d vs 3a**: *β* = 2.44, *SE* = 2.053, *z* = 1.186, *p* = 0.236
- **SNR**: *β* = -0.39, *SE* = 0.511, *z* = -0.758, *p* = 0.448

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -1.35 | nan | 0.00 | 1.000 | 1.000 | n.s. |
| 3a - 3c | -1.11 | nan | 0.00 | 1.000 | 1.000 | n.s. |
| 3a - 3d | -2.43 | 2.05 | -1.19 | 0.236 | 0.800 | n.s. |
| 3b - 3c | 0.24 | nan | 0.00 | 1.000 | 1.000 | n.s. |
| 3b - 3d | -1.08 | nan | 0.00 | 1.000 | 1.000 | n.s. |
| 3c - 3d | -1.32 | 2.03 | -0.65 | 0.515 | 0.973 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.33, *p* = 0.070, η²_G = 0.493
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -5.07 | 3 | = 0.089 | -0.91 [-1.39, 0.27] | large | n.s. |
| 3a vs 3c | 1.81 | 3 | = 0.252 | 1.45 [-0.62, 1.08] | large | n.s. |
| 3a vs 3d | -0.66 | 3 | = 0.668 | -0.59 [-1.41, 0.37] | medium | n.s. |
| 3b vs 3c | 2.41 | 3 | = 0.189 | 1.84 [-0.76, 1.93] | large | n.s. |
| 3b vs 3d | -0.06 | 3 | = 0.958 | -0.05 [-0.81, 1.04] | negligible | n.s. |
| 3c vs 3d | -2.53 | 3 | = 0.189 | -1.60 [-1.46, 1.05] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 233.81, BIC = 247.60
- **3b vs 3a**: *β* = 0.56, *SE* = 0.711, *z* = 0.789, *p* = 0.430
- **3c vs 3a**: *β* = 1.35, *SE* = 0.698, *z* = 1.929, *p* = 0.054
- **3d vs 3a**: *β* = 0.09, *SE* = 0.651, *z* = 0.140, *p* = 0.889
- **SNR**: *β* = 0.79, *SE* = 0.105, *z* = 7.557, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.56 | 0.71 | -0.79 | 0.430 | 0.815 | n.s. |
| 3a - 3c | -1.35 | 0.70 | -1.93 | 0.054 | 0.282 | n.s. |
| 3a - 3d | -0.09 | 0.65 | -0.14 | 0.889 | 0.889 | n.s. |
| 3b - 3c | -0.79 | 0.75 | -1.05 | 0.295 | 0.753 | n.s. |
| 3b - 3d | 0.47 | 0.72 | 0.66 | 0.512 | 0.815 | n.s. |
| 3c - 3d | 1.26 | 0.70 | 1.79 | 0.074 | 0.318 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.83, *p* = 0.510, η²_G = 0.096
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | -0.77 | 3 | = 0.706 | -0.19 [-0.67, 1.22] | negligible | n.s. |
| 3a vs 3c | -2.34 | 3 | = 0.491 | -1.53 [-1.21, 0.39] | large | n.s. |
| 3a vs 3d | -0.66 | 3 | = 0.706 | -0.31 [-0.51, 0.84] | small | n.s. |
| 3b vs 3c | -1.84 | 3 | = 0.491 | -1.09 [-0.95, 0.90] | large | n.s. |
| 3b vs 3d | -0.51 | 3 | = 0.706 | -0.21 [-1.12, 0.98] | small | n.s. |
| 3c vs 3d | 0.42 | 3 | = 0.706 | 0.26 [-0.48, 1.26] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 409.66, BIC = 423.45
- **3b vs 3a**: *β* = -0.56, *SE* = 3.946, *z* = -0.141, *p* = 0.888
- **3c vs 3a**: *β* = 1.46, *SE* = 3.936, *z* = 0.370, *p* = 0.711
- **3d vs 3a**: *β* = 0.93, *SE* = 3.572, *z* = 0.259, *p* = 0.796
- **SNR**: *β* = 0.27, *SE* = 0.546, *z* = 0.498, *p* = 0.619

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.56 | 3.95 | 0.14 | 0.888 | 0.998 | n.s. |
| 3a - 3c | -1.46 | 3.94 | -0.37 | 0.711 | 0.998 | n.s. |
| 3a - 3d | -0.92 | 3.57 | -0.26 | 0.796 | 0.998 | n.s. |
| 3b - 3c | -2.01 | 4.13 | -0.49 | 0.626 | 0.997 | n.s. |
| 3b - 3d | -1.48 | 4.01 | -0.37 | 0.712 | 0.998 | n.s. |
| 3c - 3d | 0.53 | 4.00 | 0.13 | 0.894 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.08, *p* = 0.969, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3a vs 3b | 0.37 | 3 | = 0.966 | 0.30 [-0.91, 0.94] | small | n.s. |
| 3a vs 3c | 0.05 | 3 | = 0.966 | 0.04 [-1.18, 0.41] | negligible | n.s. |
| 3a vs 3d | 0.59 | 3 | = 0.966 | 0.10 [-0.58, 0.77] | negligible | n.s. |
| 3b vs 3c | -1.86 | 3 | = 0.955 | -0.89 [-0.77, 1.10] | large | n.s. |
| 3b vs 3d | -0.21 | 3 | = 0.966 | -0.16 [-0.82, 1.31] | negligible | n.s. |
| 3c vs 3d | 0.13 | 3 | = 0.966 | 0.10 [-0.50, 1.23] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Marginal trend toward condition differences (*p* = 0.070)

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
