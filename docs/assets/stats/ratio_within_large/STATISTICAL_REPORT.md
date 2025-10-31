# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:29:40

---

## 1. Analysis Overview

**Total Measurements:** 216
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| Large Ratio 0.67 (4:6) | 24 | -3.51 µV | 2.07 | 0.42 | [-9.20, -0.08] |
| Large Ratio 0.8 (4:5) | 23 | -3.84 µV | 1.92 | 0.40 | [-7.66, -0.61] |
| Large Ratio 0.83 (5:6) | 24 | -3.80 µV | 1.92 | 0.39 | [-8.67, -0.14] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 24 | 172.29 ms | 11.25 | 2.30 | [153.47, 202.24] |
| Large Ratio 0.8 (4:5) | 23 | 172.86 ms | 8.00 | 1.67 | [158.51, 187.17] |
| Large Ratio 0.83 (5:6) | 24 | 173.00 ms | 10.22 | 2.09 | [152.27, 202.76] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 12 | 1.75 µV | 1.37 | 0.40 | [-0.01, 4.87] |
| Large Ratio 0.8 (4:5) | 12 | 1.65 µV | 1.28 | 0.37 | [0.01, 4.60] |
| Large Ratio 0.83 (5:6) | 14 | 1.20 µV | 1.15 | 0.31 | [0.04, 3.07] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 12 | 99.54 ms | 6.34 | 1.83 | [86.17, 108.76] |
| Large Ratio 0.8 (4:5) | 12 | 99.39 ms | 5.64 | 1.63 | [90.82, 105.36] |
| Large Ratio 0.83 (5:6) | 14 | 98.19 ms | 7.99 | 2.13 | [84.42, 110.22] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 18 | 3.50 µV | 2.19 | 0.52 | [0.10, 6.80] |
| Large Ratio 0.8 (4:5) | 16 | 3.86 µV | 2.74 | 0.69 | [0.31, 9.98] |
| Large Ratio 0.83 (5:6) | 13 | 1.95 µV | 2.26 | 0.63 | [-0.00, 6.97] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Large Ratio 0.67 (4:6) | 18 | 491.13 ms | 17.18 | 4.05 | [445.85, 528.77] |
| Large Ratio 0.8 (4:5) | 16 | 490.77 ms | 15.69 | 3.92 | [452.16, 513.56] |
| Large Ratio 0.83 (5:6) | 13 | 500.59 ms | 26.84 | 7.44 | [444.72, 537.31] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 231.20, BIC = 244.77
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = -0.04, *SE* = 0.241, *z* = -0.184, *p* = 0.854
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = -0.17, *SE* = 0.237, *z* = -0.710, *p* = 0.478
- **SNR**: *β* = -0.25, *SE* = 0.031, *z* = -8.215, *p* < .001

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | 0.04 | 0.24 | 0.18 | 0.854 | 0.858 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | 0.17 | 0.24 | 0.71 | 0.478 | 0.858 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | 0.12 | 0.24 | 0.52 | 0.606 | 0.858 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.34, *p* = 0.711, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | 0.46 | 22 | = 0.714 | 0.09 [-0.34, 0.53] | negligible | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | 0.80 | 22 | = 0.714 | 0.16 [-0.26, 0.59] | negligible | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | 0.37 | 22 | = 0.714 | 0.06 [-0.36, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 487.36, BIC = 500.93
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 1.64, *SE* = 1.287, *z* = 1.274, *p* = 0.203
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 0.62, *SE* = 1.265, *z* = 0.494, *p* = 0.621
- **SNR**: *β* = 0.18, *SE* = 0.169, *z* = 1.045, *p* = 0.296

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -1.64 | 1.29 | -1.27 | 0.203 | 0.493 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -0.62 | 1.27 | -0.49 | 0.621 | 0.674 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | 1.01 | 1.28 | 0.79 | 0.429 | 0.674 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.98, *p* = 0.385, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -1.46 | 22 | = 0.479 | -0.21 [-0.75, 0.14] | small | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | -0.57 | 22 | = 0.573 | -0.08 [-0.54, 0.30] | negligible | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | 0.77 | 22 | = 0.573 | 0.14 [-0.28, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 104.43, BIC = 114.26
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 0.02, *SE* = 0.285, *z* = 0.078, *p* = 0.938
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = -0.22, *SE* = 0.285, *z* = -0.781, *p* = 0.435
- **SNR**: *β* = 0.47, *SE* = 0.084, *z* = 5.592, *p* < .001

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -0.02 | 0.28 | -0.08 | 0.938 | 0.938 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | 0.22 | 0.29 | 0.78 | 0.435 | 0.751 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | 0.24 | 0.27 | 0.89 | 0.371 | 0.751 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.43, *p* = 0.283, η²_G = 0.071
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | 0.88 | 5 | = 0.421 | 0.37 [-0.73, 0.95] | small | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | 1.62 | 5 | = 0.421 | 0.66 [-0.58, 1.34] | medium | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | 0.97 | 5 | = 0.421 | 0.20 [-0.58, 0.98] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 239.83, BIC = 249.66
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 0.47, *SE* = 1.164, *z* = 0.408, *p* = 0.683
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = -0.50, *SE* = 1.203, *z* = -0.418, *p* = 0.676
- **SNR**: *β* = 0.08, *SE* = 0.339, *z* = 0.226, *p* = 0.821

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -0.47 | 1.16 | -0.41 | 0.683 | 0.895 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | 0.50 | 1.20 | 0.42 | 0.676 | 0.895 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | 0.98 | 1.11 | 0.88 | 0.378 | 0.760 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.52, *p* = 0.266, η²_G = 0.030
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -0.39 | 5 | = 0.716 | -0.11 [-0.95, 0.72] | negligible | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | 1.08 | 5 | = 0.497 | 0.26 [-0.78, 1.08] | small | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | 3.31 | 5 | = 0.064 | 0.40 [-0.28, 1.37] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 195.87, BIC = 206.98
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 0.32, *SE* = 0.450, *z* = 0.719, *p* = 0.472
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = -1.35, *SE* = 0.536, *z* = -2.525, *p* = 0.012
- **SNR**: *β* = 0.23, *SE* = 0.048, *z* = 4.850, *p* < .001

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -0.32 | 0.45 | -0.72 | 0.472 | 0.472 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | 1.35 | 0.54 | 2.52 | 0.012 | 0.023 | * |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | 1.68 | 0.53 | 3.15 | 0.002 | 0.005 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.05, *p* = 0.003, η²_G = 0.270
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -0.49 | 10 | = 0.634 | -0.19 [-0.58, 0.53] | negligible | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | 2.95 | 10 | = 0.022 | 1.19 [0.18, 1.72] | large | * |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | 4.20 | 10 | = 0.005 | 1.21 [0.37, 2.17] | large | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 419.37, BIC = 430.47
- **Large Ratio 0.8 (4:5) vs Large Ratio 0.67 (4:6)**: *β* = 1.09, *SE* = 5.131, *z* = 0.212, *p* = 0.832
- **Large Ratio 0.83 (5:6) vs Large Ratio 0.67 (4:6)**: *β* = 9.35, *SE* = 5.890, *z* = 1.588, *p* = 0.112
- **SNR**: *β* = -0.36, *SE* = 0.549, *z* = -0.665, *p* = 0.506

_Reference condition: **Large Ratio 0.67 (4:6)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Large Ratio 0.67 (4:6) - Large Ratio 0.8 (4:5) | -1.09 | 5.13 | -0.21 | 0.832 | 0.832 | n.s. |
| Large Ratio 0.67 (4:6) - Large Ratio 0.83 (5:6) | -9.35 | 5.89 | -1.59 | 0.112 | 0.301 | n.s. |
| Large Ratio 0.8 (4:5) - Large Ratio 0.83 (5:6) | -8.26 | 5.93 | -1.39 | 0.163 | 0.301 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.26, *p* = 0.029, η²_G = 0.146
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Large Ratio 0.67 (4:6) vs Large Ratio 0.8 (4:5) | -2.03 | 10 | = 0.105 | -0.71 [-0.67, 0.45] | medium | n.s. |
| Large Ratio 0.67 (4:6) vs Large Ratio 0.83 (5:6) | -2.57 | 10 | = 0.084 | -0.85 [-1.61, -0.12] | large | n.s. |
| Large Ratio 0.8 (4:5) vs Large Ratio 0.83 (5:6) | -1.36 | 10 | = 0.203 | -0.45 [-1.11, 0.29] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.003). Post-hoc tests revealed:
  - Large Ratio 0.67 (4:6) showed greater amplitude than Large Ratio 0.83 (5:6) (*d* = 1.19)
  - Large Ratio 0.8 (4:5) showed greater amplitude than Large Ratio 0.83 (5:6) (*d* = 1.21)
**P3b latency:** Significant main effect of condition (*p* = 0.029) (no significant pairwise comparisons)

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
