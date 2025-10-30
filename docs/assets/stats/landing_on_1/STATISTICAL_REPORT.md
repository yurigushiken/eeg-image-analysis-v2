# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:56:18

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
| 2 to 1 | 16 | -3.03 µV | 2.22 | 0.55 | [-8.83, -0.60] |
| 3 to 1 | 22 | -2.69 µV | 2.30 | 0.49 | [-8.63, 0.06] |
| 4 to 1 | 20 | -2.32 µV | 1.53 | 0.34 | [-6.07, -0.22] |
| Cardinality1 | 16 | -2.62 µV | 2.41 | 0.60 | [-8.67, 0.02] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 181.13 ms | 7.55 | 1.89 | [168.30, 197.67] |
| 3 to 1 | 22 | 182.64 ms | 8.60 | 1.83 | [170.03, 203.49] |
| 4 to 1 | 20 | 183.61 ms | 7.34 | 1.64 | [170.47, 195.68] |
| Cardinality1 | 16 | 180.55 ms | 10.69 | 2.67 | [161.47, 201.34] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 3.20 µV | 2.07 | 0.47 | [0.24, 7.58] |
| 3 to 1 | 22 | 2.09 µV | 1.43 | 0.30 | [0.02, 6.21] |
| 4 to 1 | 16 | 3.78 µV | 2.22 | 0.56 | [0.48, 9.21] |
| Cardinality1 | 18 | 3.11 µV | 2.65 | 0.63 | [0.42, 10.97] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 123.51 ms | 7.58 | 1.74 | [106.89, 136.60] |
| 3 to 1 | 22 | 120.62 ms | 10.22 | 2.18 | [101.03, 138.29] |
| 4 to 1 | 16 | 121.23 ms | 6.20 | 1.55 | [105.91, 128.54] |
| Cardinality1 | 18 | 122.88 ms | 9.09 | 2.14 | [105.02, 141.27] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 3.77 µV | 2.68 | 0.60 | [0.11, 9.98] |
| 3 to 1 | 20 | 4.01 µV | 2.38 | 0.53 | [0.24, 9.51] |
| 4 to 1 | 21 | 4.14 µV | 2.78 | 0.61 | [0.04, 9.14] |
| Cardinality1 | 10 | 1.74 µV | 1.41 | 0.45 | [0.02, 3.73] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 20 | 484.48 ms | 15.06 | 3.37 | [449.26, 522.08] |
| 3 to 1 | 20 | 482.02 ms | 12.90 | 2.88 | [464.00, 517.00] |
| 4 to 1 | 21 | 483.84 ms | 14.11 | 3.08 | [460.20, 526.37] |
| Cardinality1 | 10 | 479.21 ms | 27.44 | 8.68 | [432.67, 524.59] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 265.75, BIC = 281.88
- **3 to 1 vs 2 to 1**: *β* = -0.05, *SE* = 0.394, *z* = -0.119, *p* = 0.906
- **4 to 1 vs 2 to 1**: *β* = 0.58, *SE* = 0.399, *z* = 1.454, *p* = 0.146
- **Cardinality1 vs 2 to 1**: *β* = 0.62, *SE* = 0.424, *z* = 1.456, *p* = 0.145
- **SNR**: *β* = -0.44, *SE* = 0.048, *z* = -9.098, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.05 | 0.39 | 0.12 | 0.906 | 0.991 | n.s. |
| 2 to 1 - 4 to 1 | -0.58 | 0.40 | -1.45 | 0.146 | 0.467 | n.s. |
| 2 to 1 - Cardinality1 | -0.62 | 0.42 | -1.46 | 0.145 | 0.467 | n.s. |
| 3 to 1 - 4 to 1 | -0.63 | 0.37 | -1.71 | 0.087 | 0.421 | n.s. |
| 3 to 1 - Cardinality1 | -0.66 | 0.40 | -1.68 | 0.094 | 0.421 | n.s. |
| 4 to 1 - Cardinality1 | -0.04 | 0.40 | -0.09 | 0.926 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.58, *p* = 0.635, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.02 | 10 | = 0.981 | 0.01 [-0.47, 0.64] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -1.50 | 10 | = 0.837 | -0.43 [-0.93, 0.22] | small | n.s. |
| 2 to 1 vs Cardinality1 | -0.84 | 10 | = 0.837 | -0.28 [-0.89, 0.40] | small | n.s. |
| 3 to 1 vs 4 to 1 | -1.12 | 10 | = 0.837 | -0.40 [-0.78, 0.20] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.61 | 10 | = 0.837 | -0.27 [-0.70, 0.41] | small | n.s. |
| 4 to 1 vs Cardinality1 | 0.16 | 10 | = 0.981 | 0.07 [-0.55, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 520.63, BIC = 536.76
- **3 to 1 vs 2 to 1**: *β* = 1.12, *SE* = 2.003, *z* = 0.561, *p* = 0.575
- **4 to 1 vs 2 to 1**: *β* = 2.85, *SE* = 2.025, *z* = 1.407, *p* = 0.159
- **Cardinality1 vs 2 to 1**: *β* = 0.28, *SE* = 2.162, *z* = 0.128, *p* = 0.898
- **SNR**: *β* = 0.18, *SE* = 0.258, *z* = 0.704, *p* = 0.481

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | -1.12 | 2.00 | -0.56 | 0.575 | 0.923 | n.s. |
| 2 to 1 - 4 to 1 | -2.85 | 2.03 | -1.41 | 0.159 | 0.647 | n.s. |
| 2 to 1 - Cardinality1 | -0.28 | 2.16 | -0.13 | 0.898 | 0.923 | n.s. |
| 3 to 1 - 4 to 1 | -1.73 | 1.86 | -0.93 | 0.353 | 0.825 | n.s. |
| 3 to 1 - Cardinality1 | 0.85 | 2.02 | 0.42 | 0.675 | 0.923 | n.s. |
| 4 to 1 - Cardinality1 | 2.57 | 2.03 | 1.27 | 0.204 | 0.681 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.27, *p* = 0.850, η²_G = 0.009
- Greenhouse-Geisser corrected: *p* = 0.673 (ε = 0.428)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.56 | 10 | = 0.837 | 0.10 [-0.52, 0.58] | negligible | n.s. |
| 2 to 1 vs 4 to 1 | -0.97 | 10 | = 0.837 | -0.18 [-0.99, 0.17] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | -0.21 | 10 | = 0.837 | -0.06 [-0.74, 0.54] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -2.21 | 10 | = 0.312 | -0.31 [-0.90, 0.11] | small | n.s. |
| 3 to 1 vs Cardinality1 | -0.38 | 10 | = 0.837 | -0.14 [-0.53, 0.58] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.23 | 10 | = 0.837 | 0.08 [-0.47, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 283.51, BIC = 299.73
- **3 to 1 vs 2 to 1**: *β* = -0.55, *SE* = 0.405, *z* = -1.365, *p* = 0.172
- **4 to 1 vs 2 to 1**: *β* = 0.35, *SE* = 0.429, *z* = 0.827, *p* = 0.408
- **Cardinality1 vs 2 to 1**: *β* = 0.14, *SE* = 0.416, *z* = 0.349, *p* = 0.727
- **SNR**: *β* = 0.44, *SE* = 0.073, *z* = 6.010, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.55 | 0.40 | 1.37 | 0.172 | 0.530 | n.s. |
| 2 to 1 - 4 to 1 | -0.35 | 0.43 | -0.83 | 0.408 | 0.793 | n.s. |
| 2 to 1 - Cardinality1 | -0.15 | 0.42 | -0.35 | 0.727 | 0.867 | n.s. |
| 3 to 1 - 4 to 1 | -0.91 | 0.43 | -2.10 | 0.036 | 0.196 | n.s. |
| 3 to 1 - Cardinality1 | -0.70 | 0.40 | -1.72 | 0.085 | 0.358 | n.s. |
| 4 to 1 - Cardinality1 | 0.21 | 0.44 | 0.47 | 0.635 | 0.867 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.91, *p* = 0.046, η²_G = 0.067
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 2.07 | 14 | = 0.173 | 0.62 [-0.04, 0.98] | medium | n.s. |
| 2 to 1 vs 4 to 1 | -1.10 | 14 | = 0.349 | -0.24 [-0.81, 0.27] | small | n.s. |
| 2 to 1 vs Cardinality1 | 0.43 | 14 | = 0.676 | 0.09 [-0.41, 0.59] | negligible | n.s. |
| 3 to 1 vs 4 to 1 | -3.08 | 14 | = 0.049 | -0.82 [-1.30, -0.11] | large | * |
| 3 to 1 vs Cardinality1 | -1.47 | 14 | = 0.327 | -0.37 [-0.89, 0.14] | small | n.s. |
| 4 to 1 vs Cardinality1 | 1.10 | 14 | = 0.349 | 0.28 [-0.28, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 528.15, BIC = 544.38
- **3 to 1 vs 2 to 1**: *β* = -1.77, *SE* = 1.923, *z* = -0.922, *p* = 0.356
- **4 to 1 vs 2 to 1**: *β* = -0.72, *SE* = 2.024, *z* = -0.355, *p* = 0.723
- **Cardinality1 vs 2 to 1**: *β* = -1.31, *SE* = 1.955, *z* = -0.671, *p* = 0.502
- **SNR**: *β* = -0.02, *SE* = 0.340, *z* = -0.053, *p* = 0.958

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 1.77 | 1.92 | 0.92 | 0.356 | 0.929 | n.s. |
| 2 to 1 - 4 to 1 | 0.72 | 2.02 | 0.35 | 0.723 | 0.979 | n.s. |
| 2 to 1 - Cardinality1 | 1.31 | 1.95 | 0.67 | 0.502 | 0.969 | n.s. |
| 3 to 1 - 4 to 1 | -1.06 | 2.04 | -0.52 | 0.605 | 0.976 | n.s. |
| 3 to 1 - Cardinality1 | -0.46 | 1.94 | -0.24 | 0.811 | 0.979 | n.s. |
| 4 to 1 - Cardinality1 | 0.59 | 2.10 | 0.28 | 0.777 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.839, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 0.79 | 14 | = 0.951 | 0.25 [-0.37, 0.60] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.23 | 14 | = 0.951 | 0.08 [-0.47, 0.60] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 0.74 | 14 | = 0.951 | 0.21 [-0.32, 0.68] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.62 | 14 | = 0.951 | -0.19 [-0.65, 0.42] | negligible | n.s. |
| 3 to 1 vs Cardinality1 | -0.06 | 14 | = 0.951 | -0.02 [-0.45, 0.54] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.48 | 14 | = 0.951 | 0.16 [-0.43, 0.68] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 315.21, BIC = 331.05
- **3 to 1 vs 2 to 1**: *β* = -0.30, *SE* = 0.589, *z* = -0.505, *p* = 0.614
- **4 to 1 vs 2 to 1**: *β* = -0.01, *SE* = 0.575, *z* = -0.010, *p* = 0.992
- **Cardinality1 vs 2 to 1**: *β* = -1.89, *SE* = 0.743, *z* = -2.540, *p* = 0.011
- **SNR**: *β* = 0.17, *SE* = 0.037, *z* = 4.461, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 0.30 | 0.59 | 0.50 | 0.614 | 0.940 | n.s. |
| 2 to 1 - 4 to 1 | 0.01 | 0.57 | 0.01 | 0.992 | 0.992 | n.s. |
| 2 to 1 - Cardinality1 | 1.89 | 0.74 | 2.54 | 0.011 | 0.065 | n.s. |
| 3 to 1 - 4 to 1 | -0.29 | 0.57 | -0.51 | 0.608 | 0.940 | n.s. |
| 3 to 1 - Cardinality1 | 1.59 | 0.78 | 2.04 | 0.041 | 0.154 | n.s. |
| 4 to 1 - Cardinality1 | 1.88 | 0.77 | 2.44 | 0.015 | 0.071 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.02, *p* = 0.003, η²_G = 0.275
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.10 | 9 | = 0.360 | 0.37 [-0.55, 0.45] | small | n.s. |
| 2 to 1 vs 4 to 1 | -0.44 | 9 | = 0.671 | -0.16 [-0.67, 0.28] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 3.85 | 9 | = 0.012 | 1.52 [0.27, 2.16] | large | * |
| 3 to 1 vs 4 to 1 | -1.43 | 9 | = 0.282 | -0.51 [-0.55, 0.42] | medium | n.s. |
| 3 to 1 vs Cardinality1 | 2.27 | 9 | = 0.099 | 1.20 [-0.09, 1.52] | large | n.s. |
| 4 to 1 vs Cardinality1 | 3.91 | 9 | = 0.012 | 1.56 [0.29, 2.19] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 608.08, BIC = 623.92
- **3 to 1 vs 2 to 1**: *β* = -2.39, *SE* = 4.855, *z* = -0.491, *p* = 0.623
- **4 to 1 vs 2 to 1**: *β* = -0.33, *SE* = 4.745, *z* = -0.070, *p* = 0.944
- **Cardinality1 vs 2 to 1**: *β* = -5.53, *SE* = 5.961, *z* = -0.928, *p* = 0.353
- **SNR**: *β* = -0.09, *SE* = 0.285, *z* = -0.322, *p* = 0.747

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 1 | 2.39 | 4.85 | 0.49 | 0.623 | 0.977 | n.s. |
| 2 to 1 - 4 to 1 | 0.33 | 4.74 | 0.07 | 0.944 | 0.977 | n.s. |
| 2 to 1 - Cardinality1 | 5.53 | 5.96 | 0.93 | 0.353 | 0.927 | n.s. |
| 3 to 1 - 4 to 1 | -2.05 | 4.71 | -0.44 | 0.663 | 0.977 | n.s. |
| 3 to 1 - Cardinality1 | 3.15 | 6.16 | 0.51 | 0.609 | 0.977 | n.s. |
| 4 to 1 - Cardinality1 | 5.20 | 6.07 | 0.86 | 0.392 | 0.927 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.838, η²_G = 0.019
- Greenhouse-Geisser corrected: *p* = 0.714 (ε = 0.542)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 1 | 1.36 | 9 | = 0.874 | 0.38 [-0.13, 0.90] | small | n.s. |
| 2 to 1 vs 4 to 1 | 0.16 | 9 | = 0.874 | 0.06 [-0.47, 0.47] | negligible | n.s. |
| 2 to 1 vs Cardinality1 | 0.66 | 9 | = 0.874 | 0.27 [-0.51, 0.93] | small | n.s. |
| 3 to 1 vs 4 to 1 | -0.59 | 9 | = 0.874 | -0.25 [-0.64, 0.33] | small | n.s. |
| 3 to 1 vs Cardinality1 | 0.20 | 9 | = 0.874 | 0.09 [-0.65, 0.78] | negligible | n.s. |
| 4 to 1 vs Cardinality1 | 0.55 | 9 | = 0.874 | 0.22 [-0.55, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.046). Post-hoc tests revealed:
  - 3 to 1 showed smaller amplitude than 4 to 1 (*d* = -0.82)
**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - 2 to 1 showed greater amplitude than Cardinality1 (*d* = 1.52)
  - 4 to 1 showed greater amplitude than Cardinality1 (*d* = 1.56)

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
