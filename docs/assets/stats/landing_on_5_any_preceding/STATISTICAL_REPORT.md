# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:57:37

---

## 1. Analysis Overview

**Total Measurements:** 360
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 2 to 5 | 24 | -3.67 µV | 2.22 | 0.45 | [-10.37, 0.03] |
| 3 to 5 | 22 | -3.34 µV | 2.35 | 0.50 | [-9.83, -0.49] |
| 4 to 5 | 23 | -3.67 µV | 2.37 | 0.49 | [-8.46, -0.52] |
| 6 to 5 | 24 | -3.64 µV | 1.83 | 0.37 | [-8.32, -0.05] |
| Cardinality5 | 23 | -3.76 µV | 2.32 | 0.48 | [-9.01, -0.42] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 171.16 ms | 13.03 | 2.66 | [153.26, 202.93] |
| 3 to 5 | 22 | 166.99 ms | 13.83 | 2.95 | [140.33, 195.88] |
| 4 to 5 | 23 | 168.71 ms | 12.60 | 2.63 | [143.65, 192.63] |
| 6 to 5 | 24 | 171.09 ms | 12.08 | 2.47 | [153.45, 201.31] |
| Cardinality5 | 23 | 170.86 ms | 12.59 | 2.63 | [141.58, 194.82] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 13 | 1.42 µV | 1.92 | 0.53 | [0.05, 7.23] |
| 3 to 5 | 15 | 1.78 µV | 1.31 | 0.34 | [0.29, 4.47] |
| 4 to 5 | 14 | 2.19 µV | 2.28 | 0.61 | [0.01, 8.63] |
| 6 to 5 | 14 | 1.92 µV | 2.24 | 0.60 | [0.06, 8.06] |
| Cardinality5 | 13 | 1.78 µV | 1.22 | 0.34 | [0.22, 3.87] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 13 | 95.50 ms | 6.51 | 1.81 | [84.09, 106.98] |
| 3 to 5 | 15 | 97.97 ms | 5.37 | 1.39 | [87.18, 105.91] |
| 4 to 5 | 14 | 98.94 ms | 4.41 | 1.18 | [92.55, 107.78] |
| 6 to 5 | 14 | 96.57 ms | 5.78 | 1.54 | [86.90, 104.60] |
| Cardinality5 | 13 | 97.54 ms | 3.40 | 0.94 | [92.16, 103.48] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 22 | 2.87 µV | 1.97 | 0.42 | [0.09, 6.73] |
| 3 to 5 | 16 | 3.60 µV | 2.26 | 0.57 | [0.84, 9.10] |
| 4 to 5 | 16 | 2.83 µV | 2.84 | 0.71 | [0.36, 11.12] |
| 6 to 5 | 12 | 2.30 µV | 2.00 | 0.58 | [0.29, 5.87] |
| Cardinality5 | 12 | 1.42 µV | 0.98 | 0.28 | [0.27, 3.44] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 22 | 444.74 ms | 39.38 | 8.40 | [365.91, 524.09] |
| 3 to 5 | 16 | 453.91 ms | 26.08 | 6.52 | [398.61, 498.83] |
| 4 to 5 | 16 | 482.77 ms | 24.77 | 6.19 | [438.04, 520.99] |
| 6 to 5 | 12 | 457.78 ms | 49.06 | 14.16 | [361.04, 526.22] |
| Cardinality5 | 12 | 441.35 ms | 54.39 | 15.70 | [361.74, 525.22] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 417.43, BIC = 439.46
- **3 to 5 vs 2 to 5**: *β* = 0.24, *SE* = 0.341, *z* = 0.711, *p* = 0.477
- **4 to 5 vs 2 to 5**: *β* = 0.09, *SE* = 0.335, *z* = 0.268, *p* = 0.789
- **6 to 5 vs 2 to 5**: *β* = -0.03, *SE* = 0.330, *z* = -0.080, *p* = 0.936
- **Cardinality5 vs 2 to 5**: *β* = 0.13, *SE* = 0.335, *z* = 0.393, *p* = 0.694
- **SNR**: *β* = -0.45, *SE* = 0.054, *z* = -8.271, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.24 | 0.34 | -0.71 | 0.477 | 0.997 | n.s. |
| 2 to 5 - 4 to 5 | -0.09 | 0.33 | -0.27 | 0.789 | 1.000 | n.s. |
| 2 to 5 - 6 to 5 | 0.03 | 0.33 | 0.08 | 0.936 | 1.000 | n.s. |
| 2 to 5 - Cardinality5 | -0.13 | 0.34 | -0.39 | 0.694 | 1.000 | n.s. |
| 3 to 5 - 4 to 5 | 0.15 | 0.34 | 0.44 | 0.657 | 1.000 | n.s. |
| 3 to 5 - 6 to 5 | 0.27 | 0.34 | 0.79 | 0.430 | 0.996 | n.s. |
| 3 to 5 - Cardinality5 | 0.11 | 0.35 | 0.32 | 0.749 | 1.000 | n.s. |
| 4 to 5 - 6 to 5 | 0.12 | 0.33 | 0.35 | 0.729 | 1.000 | n.s. |
| 4 to 5 - Cardinality5 | -0.04 | 0.34 | -0.12 | 0.901 | 1.000 | n.s. |
| 6 to 5 - Cardinality5 | -0.16 | 0.34 | -0.47 | 0.638 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.59, *p* = 0.673, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -1.64 | 21 | = 0.816 | -0.26 [-0.81, 0.11] | small | n.s. |
| 2 to 5 vs 4 to 5 | -0.29 | 21 | = 0.988 | -0.06 [-0.50, 0.37] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.28 | 21 | = 0.988 | -0.06 [-0.44, 0.40] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.02 | 21 | = 0.988 | -0.00 [-0.45, 0.42] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 1.08 | 21 | = 0.816 | 0.19 [-0.22, 0.68] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 1.00 | 21 | = 0.816 | 0.22 [-0.23, 0.66] | small | n.s. |
| 3 to 5 vs Cardinality5 | 1.23 | 21 | = 0.816 | 0.25 [-0.19, 0.71] | small | n.s. |
| 4 to 5 vs 6 to 5 | 0.02 | 21 | = 0.988 | 0.01 [-0.42, 0.44] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 0.23 | 21 | = 0.988 | 0.05 [-0.39, 0.47] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 0.25 | 21 | = 0.988 | 0.05 [-0.40, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 878.65, BIC = 900.68
- **3 to 5 vs 2 to 5**: *β* = -3.68, *SE* = 2.432, *z* = -1.513, *p* = 0.130
- **4 to 5 vs 2 to 5**: *β* = -1.72, *SE* = 2.387, *z* = -0.719, *p* = 0.472
- **6 to 5 vs 2 to 5**: *β* = -0.15, *SE* = 2.352, *z* = -0.065, *p* = 0.949
- **Cardinality5 vs 2 to 5**: *β* = 0.63, *SE* = 2.390, *z* = 0.264, *p* = 0.791
- **SNR**: *β* = -0.69, *SE* = 0.389, *z* = -1.758, *p* = 0.079

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | 3.68 | 2.43 | 1.51 | 0.130 | 0.715 | n.s. |
| 2 to 5 - 4 to 5 | 1.72 | 2.39 | 0.72 | 0.472 | 0.963 | n.s. |
| 2 to 5 - 6 to 5 | 0.15 | 2.35 | 0.06 | 0.949 | 0.983 | n.s. |
| 2 to 5 - Cardinality5 | -0.63 | 2.39 | -0.26 | 0.791 | 0.983 | n.s. |
| 3 to 5 - 4 to 5 | -1.96 | 2.45 | -0.80 | 0.423 | 0.963 | n.s. |
| 3 to 5 - 6 to 5 | -3.53 | 2.43 | -1.45 | 0.146 | 0.718 | n.s. |
| 3 to 5 - Cardinality5 | -4.31 | 2.46 | -1.75 | 0.080 | 0.565 | n.s. |
| 4 to 5 - 6 to 5 | -1.57 | 2.39 | -0.66 | 0.512 | 0.963 | n.s. |
| 4 to 5 - Cardinality5 | -2.35 | 2.40 | -0.98 | 0.329 | 0.938 | n.s. |
| 6 to 5 - Cardinality5 | -0.78 | 2.39 | -0.33 | 0.743 | 0.983 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.59, *p* = 0.673, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.32 | 21 | = 0.844 | 0.24 [-0.17, 0.73] | small | n.s. |
| 2 to 5 vs 4 to 5 | 0.55 | 21 | = 0.955 | 0.10 [-0.32, 0.55] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 0.04 | 21 | = 0.991 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | 0.06 | 21 | = 0.991 | 0.01 [-0.55, 0.32] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.60 | 21 | = 0.955 | -0.14 [-0.57, 0.32] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.18 | 21 | = 0.844 | -0.23 [-0.70, 0.20] | small | n.s. |
| 3 to 5 vs Cardinality5 | -1.31 | 21 | = 0.844 | -0.23 [-0.73, 0.17] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.43 | 21 | = 0.955 | -0.09 [-0.57, 0.30] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | -0.44 | 21 | = 0.955 | -0.09 [-0.60, 0.27] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | -0.01 | 21 | = 0.991 | -0.00 [-0.47, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 206.28, BIC = 224.15
- **3 to 5 vs 2 to 5**: *β* = 0.03, *SE* = 0.333, *z* = 0.103, *p* = 0.918
- **4 to 5 vs 2 to 5**: *β* = 0.61, *SE* = 0.342, *z* = 1.772, *p* = 0.076
- **6 to 5 vs 2 to 5**: *β* = 0.48, *SE* = 0.342, *z* = 1.400, *p* = 0.161
- **Cardinality5 vs 2 to 5**: *β* = 0.05, *SE* = 0.347, *z* = 0.156, *p* = 0.876
- **SNR**: *β* = 0.70, *SE* = 0.069, *z* = 10.163, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.03 | 0.33 | -0.10 | 0.918 | 0.998 | n.s. |
| 2 to 5 - 4 to 5 | -0.61 | 0.34 | -1.77 | 0.076 | 0.548 | n.s. |
| 2 to 5 - 6 to 5 | -0.48 | 0.34 | -1.40 | 0.161 | 0.709 | n.s. |
| 2 to 5 - Cardinality5 | -0.05 | 0.35 | -0.16 | 0.876 | 0.998 | n.s. |
| 3 to 5 - 4 to 5 | -0.57 | 0.33 | -1.75 | 0.081 | 0.548 | n.s. |
| 3 to 5 - 6 to 5 | -0.44 | 0.33 | -1.37 | 0.172 | 0.709 | n.s. |
| 3 to 5 - Cardinality5 | -0.02 | 0.33 | -0.06 | 0.951 | 0.998 | n.s. |
| 4 to 5 - 6 to 5 | 0.13 | 0.33 | 0.39 | 0.699 | 0.992 | n.s. |
| 4 to 5 - Cardinality5 | 0.55 | 0.34 | 1.63 | 0.104 | 0.585 | n.s. |
| 6 to 5 - Cardinality5 | 0.42 | 0.33 | 1.27 | 0.205 | 0.709 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.09, *p* = 0.983, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.12 | 4 | = 0.983 | 0.05 [-0.98, 0.47] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | -0.02 | 4 | = 0.983 | -0.01 [-1.25, 0.36] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -0.17 | 4 | = 0.983 | -0.02 [-1.14, 0.44] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | -0.32 | 4 | = 0.983 | -0.17 [-0.90, 0.65] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | -0.21 | 4 | = 0.983 | -0.08 [-1.18, 0.42] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -0.18 | 4 | = 0.983 | -0.07 [-0.95, 0.50] | negligible | n.s. |
| 3 to 5 vs Cardinality5 | -1.04 | 4 | = 0.983 | -0.37 [-0.52, 0.83] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.07 | 4 | = 0.983 | -0.02 [-0.83, 0.70] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | -0.41 | 4 | = 0.983 | -0.24 [-1.01, 0.67] | small | n.s. |
| 6 to 5 vs Cardinality5 | -0.25 | 4 | = 0.983 | -0.13 [-0.58, 0.85] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 423.72, BIC = 441.59
- **3 to 5 vs 2 to 5**: *β* = 2.47, *SE* = 1.517, *z* = 1.629, *p* = 0.103
- **4 to 5 vs 2 to 5**: *β* = 3.15, *SE* = 1.560, *z* = 2.019, *p* = 0.044
- **6 to 5 vs 2 to 5**: *β* = 1.31, *SE* = 1.541, *z* = 0.851, *p* = 0.395
- **Cardinality5 vs 2 to 5**: *β* = 1.66, *SE* = 1.575, *z* = 1.056, *p* = 0.291
- **SNR**: *β* = -0.15, *SE* = 0.301, *z* = -0.493, *p* = 0.622

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -2.47 | 1.52 | -1.63 | 0.103 | 0.626 | n.s. |
| 2 to 5 - 4 to 5 | -3.15 | 1.56 | -2.02 | 0.044 | 0.359 | n.s. |
| 2 to 5 - 6 to 5 | -1.31 | 1.54 | -0.85 | 0.395 | 0.919 | n.s. |
| 2 to 5 - Cardinality5 | -1.66 | 1.58 | -1.06 | 0.291 | 0.910 | n.s. |
| 3 to 5 - 4 to 5 | -0.68 | 1.50 | -0.45 | 0.652 | 0.928 | n.s. |
| 3 to 5 - 6 to 5 | 1.16 | 1.47 | 0.79 | 0.432 | 0.919 | n.s. |
| 3 to 5 - Cardinality5 | 0.81 | 1.48 | 0.55 | 0.585 | 0.928 | n.s. |
| 4 to 5 - 6 to 5 | 1.84 | 1.53 | 1.20 | 0.228 | 0.874 | n.s. |
| 4 to 5 - Cardinality5 | 1.49 | 1.56 | 0.95 | 0.340 | 0.918 | n.s. |
| 6 to 5 - Cardinality5 | -0.35 | 1.53 | -0.23 | 0.818 | 0.928 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.817, η²_G = 0.063
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.34 | 4 | = 0.941 | 0.17 [-1.00, 0.45] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 1.22 | 4 | = 0.941 | 0.39 [-0.98, 0.57] | small | n.s. |
| 2 to 5 vs 6 to 5 | -0.12 | 4 | = 0.987 | -0.07 [-1.32, 0.31] | negligible | n.s. |
| 2 to 5 vs Cardinality5 | 0.83 | 4 | = 0.941 | 0.51 [-0.97, 0.59] | medium | n.s. |
| 3 to 5 vs 4 to 5 | 0.35 | 4 | = 0.941 | 0.25 [-0.66, 0.88] | small | n.s. |
| 3 to 5 vs 6 to 5 | -0.46 | 4 | = 0.941 | -0.29 [-0.59, 0.84] | small | n.s. |
| 3 to 5 vs Cardinality5 | 0.40 | 4 | = 0.941 | 0.34 [-0.62, 0.72] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.80 | 4 | = 0.941 | -0.53 [-0.59, 0.96] | medium | n.s. |
| 4 to 5 vs Cardinality5 | 0.02 | 4 | = 0.987 | 0.01 [-0.50, 1.23] | negligible | n.s. |
| 6 to 5 vs Cardinality5 | 1.40 | 4 | = 0.941 | 0.81 [-0.31, 1.19] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 289.60, BIC = 308.45
- **3 to 5 vs 2 to 5**: *β* = 0.38, *SE* = 0.390, *z* = 0.979, *p* = 0.327
- **4 to 5 vs 2 to 5**: *β* = 0.28, *SE* = 0.400, *z* = 0.695, *p* = 0.487
- **6 to 5 vs 2 to 5**: *β* = -0.33, *SE* = 0.440, *z* = -0.759, *p* = 0.448
- **Cardinality5 vs 2 to 5**: *β* = -0.60, *SE* = 0.442, *z* = -1.350, *p* = 0.177
- **SNR**: *β* = 0.44, *SE* = 0.054, *z* = 8.258, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -0.38 | 0.39 | -0.98 | 0.327 | 0.862 | n.s. |
| 2 to 5 - 4 to 5 | -0.28 | 0.40 | -0.70 | 0.487 | 0.907 | n.s. |
| 2 to 5 - 6 to 5 | 0.33 | 0.44 | 0.76 | 0.448 | 0.907 | n.s. |
| 2 to 5 - Cardinality5 | 0.60 | 0.44 | 1.35 | 0.177 | 0.744 | n.s. |
| 3 to 5 - 4 to 5 | 0.10 | 0.43 | 0.24 | 0.808 | 0.907 | n.s. |
| 3 to 5 - 6 to 5 | 0.72 | 0.46 | 1.55 | 0.120 | 0.640 | n.s. |
| 3 to 5 - Cardinality5 | 0.98 | 0.47 | 2.08 | 0.037 | 0.315 | n.s. |
| 4 to 5 - 6 to 5 | 0.61 | 0.46 | 1.33 | 0.184 | 0.744 | n.s. |
| 4 to 5 - Cardinality5 | 0.87 | 0.46 | 1.89 | 0.059 | 0.424 | n.s. |
| 6 to 5 - Cardinality5 | 0.26 | 0.50 | 0.53 | 0.599 | 0.907 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.46, *p* = 0.078, η²_G = 0.319
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 0.73 | 5 | = 0.552 | 0.53 [-0.60, 0.47] | medium | n.s. |
| 2 to 5 vs 4 to 5 | 1.52 | 5 | = 0.400 | 0.89 [-0.44, 0.67] | large | n.s. |
| 2 to 5 vs 6 to 5 | 1.37 | 5 | = 0.400 | 0.86 [-0.28, 1.12] | large | n.s. |
| 2 to 5 vs Cardinality5 | 4.16 | 5 | = 0.044 | 2.74 [0.12, 1.61] | large | * |
| 3 to 5 vs 4 to 5 | 0.73 | 5 | = 0.552 | 0.51 [-0.27, 1.05] | medium | n.s. |
| 3 to 5 vs 6 to 5 | 0.79 | 5 | = 0.552 | 0.47 [-0.30, 1.20] | small | n.s. |
| 3 to 5 vs Cardinality5 | 6.36 | 5 | = 0.014 | 2.16 [0.20, 2.03] | large | * |
| 4 to 5 vs 6 to 5 | -0.07 | 5 | = 0.948 | -0.04 [-0.52, 1.05] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 1.33 | 5 | = 0.400 | 0.87 [-0.56, 0.99] | large | n.s. |
| 6 to 5 vs Cardinality5 | 1.35 | 5 | = 0.400 | 0.94 [-0.46, 1.51] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 803.67, BIC = 822.52
- **3 to 5 vs 2 to 5**: *β* = 9.11, *SE* = 12.414, *z* = 0.733, *p* = 0.463
- **4 to 5 vs 2 to 5**: *β* = 38.20, *SE* = 12.493, *z* = 3.058, *p* = 0.002
- **6 to 5 vs 2 to 5**: *β* = 13.19, *SE* = 14.002, *z* = 0.942, *p* = 0.346
- **Cardinality5 vs 2 to 5**: *β* = -3.15, *SE* = 13.844, *z* = -0.227, *p* = 0.820
- **SNR**: *β* = 0.16, *SE* = 1.600, *z* = 0.101, *p* = 0.919

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 5 - 3 to 5 | -9.11 | 12.41 | -0.73 | 0.463 | 0.881 | n.s. |
| 2 to 5 - 4 to 5 | -38.21 | 12.49 | -3.06 | 0.002 | 0.022 | * |
| 2 to 5 - 6 to 5 | -13.19 | 14.00 | -0.94 | 0.346 | 0.881 | n.s. |
| 2 to 5 - Cardinality5 | 3.15 | 13.84 | 0.23 | 0.820 | 0.953 | n.s. |
| 3 to 5 - 4 to 5 | -29.10 | 13.53 | -2.15 | 0.031 | 0.226 | n.s. |
| 3 to 5 - 6 to 5 | -4.08 | 14.85 | -0.27 | 0.783 | 0.953 | n.s. |
| 3 to 5 - Cardinality5 | 12.25 | 14.77 | 0.83 | 0.407 | 0.881 | n.s. |
| 4 to 5 - 6 to 5 | 25.02 | 14.83 | 1.69 | 0.092 | 0.490 | n.s. |
| 4 to 5 - Cardinality5 | 41.35 | 14.57 | 2.84 | 0.005 | 0.040 | * |
| 6 to 5 - Cardinality5 | 16.33 | 15.50 | 1.05 | 0.292 | 0.874 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.05, *p* = 0.126, η²_G = 0.254
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -2.45 | 5 | = 0.281 | -0.51 [-1.20, -0.04] | medium | n.s. |
| 2 to 5 vs 4 to 5 | -1.75 | 5 | = 0.281 | -1.09 [-1.49, -0.20] | large | n.s. |
| 2 to 5 vs 6 to 5 | -1.78 | 5 | = 0.281 | -1.02 [-1.11, 0.29] | large | n.s. |
| 2 to 5 vs Cardinality5 | 0.54 | 5 | = 0.682 | 0.38 [-0.67, 0.60] | small | n.s. |
| 3 to 5 vs 4 to 5 | -0.83 | 5 | = 0.560 | -0.60 [-1.14, 0.20] | medium | n.s. |
| 3 to 5 vs 6 to 5 | -0.82 | 5 | = 0.560 | -0.53 [-1.07, 0.40] | medium | n.s. |
| 3 to 5 vs Cardinality5 | 1.07 | 5 | = 0.553 | 0.76 [-0.65, 0.78] | medium | n.s. |
| 4 to 5 vs 6 to 5 | 0.30 | 5 | = 0.778 | 0.07 [-0.30, 1.33] | negligible | n.s. |
| 4 to 5 vs Cardinality5 | 2.30 | 5 | = 0.281 | 1.18 [0.06, 1.95] | large | n.s. |
| 6 to 5 vs Cardinality5 | 2.13 | 5 | = 0.281 | 1.13 [-0.33, 1.73] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.078)

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
