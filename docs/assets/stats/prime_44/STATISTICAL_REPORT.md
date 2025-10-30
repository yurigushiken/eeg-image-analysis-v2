# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:59:05

---

## 1. Analysis Overview

**Total Measurements:** 246
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
| 4a | 19 | -4.77 µV | 3.47 | 0.80 | [-13.94, -0.35] |
| 4b | 20 | -4.51 µV | 2.59 | 0.58 | [-9.56, -0.71] |
| 4c | 11 | -4.62 µV | 2.87 | 0.87 | [-11.12, -0.82] |
| 4d | 17 | -4.23 µV | 3.00 | 0.73 | [-10.32, -0.68] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 19 | 173.51 ms | 12.60 | 2.89 | [146.25, 205.76] |
| 4b | 20 | 174.80 ms | 10.65 | 2.38 | [152.32, 194.94] |
| 4c | 11 | 174.83 ms | 11.35 | 3.42 | [160.15, 198.60] |
| 4d | 17 | 174.46 ms | 11.32 | 2.75 | [155.58, 200.95] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 10 | 2.75 µV | 2.79 | 0.88 | [0.28, 8.93] |
| 4b | 14 | 2.11 µV | 1.82 | 0.49 | [-0.02, 5.70] |
| 4c | 11 | 2.59 µV | 1.89 | 0.57 | [0.42, 5.23] |
| 4d | 15 | 2.82 µV | 2.97 | 0.77 | [0.20, 10.03] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 10 | 110.10 ms | 8.26 | 2.61 | [98.13, 121.51] |
| 4b | 14 | 109.13 ms | 7.15 | 1.91 | [96.43, 120.64] |
| 4c | 11 | 111.24 ms | 6.20 | 1.87 | [98.73, 120.98] |
| 4d | 15 | 113.84 ms | 6.51 | 1.68 | [102.83, 122.50] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 12 | 3.88 µV | 3.21 | 0.93 | [0.61, 10.08] |
| 4b | 13 | 2.32 µV | 1.44 | 0.40 | [0.60, 4.82] |
| 4c | 6 | 1.88 µV | 1.55 | 0.63 | [0.09, 4.44] |
| 4d | 11 | 3.73 µV | 2.92 | 0.88 | [0.53, 8.33] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 12 | 450.85 ms | 24.69 | 7.13 | [406.26, 498.98] |
| 4b | 13 | 449.46 ms | 35.08 | 9.73 | [379.34, 495.04] |
| 4c | 6 | 451.13 ms | 51.25 | 20.92 | [388.38, 513.07] |
| 4d | 11 | 431.71 ms | 36.99 | 11.15 | [378.79, 486.28] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 309.01, BIC = 324.44
- **4b vs 4a**: *β* = 1.43, *SE* = 0.586, *z* = 2.446, *p* = 0.014
- **4c vs 4a**: *β* = 0.90, *SE* = 0.707, *z* = 1.271, *p* = 0.204
- **4d vs 4a**: *β* = 0.51, *SE* = 0.607, *z* = 0.832, *p* = 0.405
- **SNR**: *β* = -0.84, *SE* = 0.124, *z* = -6.765, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -1.43 | 0.59 | -2.45 | 0.014 | 0.084 | n.s. |
| 4a - 4c | -0.90 | 0.71 | -1.27 | 0.204 | 0.598 | n.s. |
| 4a - 4d | -0.51 | 0.61 | -0.83 | 0.405 | 0.790 | n.s. |
| 4b - 4c | 0.53 | 0.69 | 0.78 | 0.435 | 0.790 | n.s. |
| 4b - 4d | 0.93 | 0.61 | 1.53 | 0.126 | 0.489 | n.s. |
| 4c - 4d | 0.39 | 0.72 | 0.55 | 0.584 | 0.790 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.21, *p* = 0.888, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -0.67 | 5 | = 0.931 | -0.46 [-0.56, 0.47] | small | n.s. |
| 4a vs 4c | -0.19 | 5 | = 0.931 | -0.09 [-0.77, 0.77] | negligible | n.s. |
| 4a vs 4d | -0.23 | 5 | = 0.931 | -0.12 [-0.82, 0.40] | negligible | n.s. |
| 4b vs 4c | 0.92 | 5 | = 0.931 | 0.46 [-0.33, 1.17] | small | n.s. |
| 4b vs 4d | 0.53 | 5 | = 0.931 | 0.26 [-0.40, 0.76] | small | n.s. |
| 4c vs 4d | -0.09 | 5 | = 0.931 | -0.06 [-0.71, 0.97] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 520.24, BIC = 535.67
- **4b vs 4a**: *β* = 1.56, *SE* = 3.052, *z* = 0.512, *p* = 0.609
- **4c vs 4a**: *β* = 1.77, *SE* = 3.654, *z* = 0.484, *p* = 0.629
- **4d vs 4a**: *β* = 1.94, *SE* = 3.158, *z* = 0.613, *p* = 0.540
- **SNR**: *β* = 0.14, *SE* = 0.630, *z* = 0.230, *p* = 0.818

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -1.56 | 3.05 | -0.51 | 0.609 | 0.991 | n.s. |
| 4a - 4c | -1.77 | 3.65 | -0.48 | 0.629 | 0.991 | n.s. |
| 4a - 4d | -1.94 | 3.16 | -0.61 | 0.540 | 0.990 | n.s. |
| 4b - 4c | -0.21 | 3.55 | -0.06 | 0.954 | 0.999 | n.s. |
| 4b - 4d | -0.37 | 3.13 | -0.12 | 0.905 | 0.999 | n.s. |
| 4c - 4d | -0.17 | 3.70 | -0.05 | 0.964 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.91, *p* = 0.460, η²_G = 0.065
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -1.59 | 5 | = 0.590 | -0.69 [-0.76, 0.29] | medium | n.s. |
| 4a vs 4c | -0.74 | 5 | = 0.736 | -0.36 [-0.92, 0.62] | small | n.s. |
| 4a vs 4d | -1.06 | 5 | = 0.673 | -0.43 [-0.78, 0.44] | small | n.s. |
| 4b vs 4c | 1.49 | 5 | = 0.590 | 0.35 [-0.68, 0.75] | small | n.s. |
| 4b vs 4d | 0.36 | 5 | = 0.768 | 0.13 [-0.76, 0.41] | negligible | n.s. |
| 4c vs 4d | -0.31 | 5 | = 0.768 | -0.13 [-0.75, 0.93] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 193.63, BIC = 207.02
- **4b vs 4a**: *β* = -0.81, *SE* = 0.588, *z* = -1.380, *p* = 0.168
- **4c vs 4a**: *β* = -0.07, *SE* = 0.623, *z* = -0.104, *p* = 0.917
- **4d vs 4a**: *β* = 0.20, *SE* = 0.586, *z* = 0.346, *p* = 0.729
- **SNR**: *β* = 1.32, *SE* = 0.149, *z* = 8.893, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 0.81 | 0.59 | 1.38 | 0.168 | 0.601 | n.s. |
| 4a - 4c | 0.06 | 0.62 | 0.10 | 0.917 | 0.949 | n.s. |
| 4a - 4d | -0.20 | 0.59 | -0.35 | 0.729 | 0.949 | n.s. |
| 4b - 4c | -0.75 | 0.58 | -1.29 | 0.196 | 0.601 | n.s. |
| 4b - 4d | -1.01 | 0.53 | -1.93 | 0.054 | 0.284 | n.s. |
| 4c - 4d | -0.27 | 0.56 | -0.48 | 0.630 | 0.949 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.459, η²_G = 0.532
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -5.85 | 1 | = 0.483 | -0.41 [-0.83, 1.79] | small | n.s. |
| 4a vs 4c | -0.11 | 1 | = 0.937 | -0.16 [-1.24, 0.88] | negligible | n.s. |
| 4a vs 4d | -2.57 | 1 | = 0.483 | -3.06 [-1.81, 0.82] | large | n.s. |
| 4b vs 4c | 0.10 | 1 | = 0.937 | 0.14 [-1.07, 1.03] | negligible | n.s. |
| 4b vs 4d | -1.91 | 1 | = 0.483 | -2.25 [-1.23, 0.37] | large | n.s. |
| 4c vs 4d | -1.81 | 1 | = 0.483 | -1.57 [-0.84, 0.70] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 345.51, BIC = 358.90
- **4b vs 4a**: *β* = -0.65, *SE* = 2.763, *z* = -0.235, *p* = 0.814
- **4c vs 4a**: *β* = 1.25, *SE* = 2.854, *z* = 0.438, *p* = 0.661
- **4d vs 4a**: *β* = 3.85, *SE* = 2.693, *z* = 1.432, *p* = 0.152
- **SNR**: *β* = -0.65, *SE* = 0.699, *z* = -0.928, *p* = 0.353

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 0.65 | 2.76 | 0.23 | 0.814 | 0.885 | n.s. |
| 4a - 4c | -1.25 | 2.85 | -0.44 | 0.661 | 0.885 | n.s. |
| 4a - 4d | -3.85 | 2.69 | -1.43 | 0.152 | 0.562 | n.s. |
| 4b - 4c | -1.90 | 2.64 | -0.72 | 0.473 | 0.853 | n.s. |
| 4b - 4d | -4.50 | 2.42 | -1.86 | 0.063 | 0.324 | n.s. |
| 4c - 4d | -2.60 | 2.57 | -1.01 | 0.311 | 0.774 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.05, *p* = 0.484, η²_G = 0.508
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | 3.72 | 1 | = 0.369 | 3.36 [-1.37, 1.13] | large | n.s. |
| 4a vs 4c | 0.33 | 1 | = 0.795 | 0.44 [-0.68, 1.51] | small | n.s. |
| 4a vs 4d | 3.35 | 1 | = 0.369 | 1.82 [-1.65, 0.92] | large | n.s. |
| 4b vs 4c | -1.02 | 1 | = 0.743 | -1.06 [-2.00, 0.41] | large | n.s. |
| 4b vs 4d | -4.41 | 1 | = 0.369 | -3.33 [-1.06, 0.50] | large | n.s. |
| 4c vs 4d | 0.35 | 1 | = 0.795 | 0.41 [-1.17, 0.42] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 161.42, BIC = 173.58
- **4b vs 4a**: *β* = -0.99, *SE* = 0.500, *z* = -1.973, *p* = 0.048
- **4c vs 4a**: *β* = -0.44, *SE* = 0.675, *z* = -0.649, *p* = 0.517
- **4d vs 4a**: *β* = 0.35, *SE* = 0.546, *z* = 0.638, *p* = 0.523
- **SNR**: *β* = 1.29, *SE* = 0.165, *z* = 7.786, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 0.99 | 0.50 | 1.97 | 0.048 | 0.220 | n.s. |
| 4a - 4c | 0.44 | 0.67 | 0.65 | 0.517 | 0.796 | n.s. |
| 4a - 4d | -0.35 | 0.55 | -0.64 | 0.523 | 0.796 | n.s. |
| 4b - 4c | -0.55 | 0.67 | -0.82 | 0.411 | 0.796 | n.s. |
| 4b - 4d | -1.33 | 0.51 | -2.61 | 0.009 | 0.053 | n.s. |
| 4c - 4d | -0.79 | 0.66 | -1.19 | 0.235 | 0.658 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 428.32, BIC = 440.49
- **4b vs 4a**: *β* = 1.40, *SE* = 13.205, *z* = 0.106, *p* = 0.916
- **4c vs 4a**: *β* = 0.47, *SE* = 17.296, *z* = 0.027, *p* = 0.979
- **4d vs 4a**: *β* = -16.74, *SE* = 13.890, *z* = -1.205, *p* = 0.228
- **SNR**: *β* = 1.99, *SE* = 4.216, *z* = 0.471, *p* = 0.637

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -1.40 | 13.21 | -0.11 | 0.916 | 0.999 | n.s. |
| 4a - 4c | -0.47 | 17.30 | -0.03 | 0.979 | 0.999 | n.s. |
| 4a - 4d | 16.74 | 13.89 | 1.21 | 0.228 | 0.726 | n.s. |
| 4b - 4c | 0.93 | 17.60 | 0.05 | 0.958 | 0.999 | n.s. |
| 4b - 4d | 18.14 | 13.26 | 1.37 | 0.171 | 0.676 | n.s. |
| 4c - 4d | 17.21 | 17.62 | 0.98 | 0.329 | 0.797 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


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
