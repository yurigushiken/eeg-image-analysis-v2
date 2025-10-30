# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:58:58

---

## 1. Analysis Overview

**Total Measurements:** 273
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
| 3a | 19 | -4.14 µV | 3.05 | 0.70 | [-10.50, -0.30] |
| 3b | 10 | -3.12 µV | 1.86 | 0.59 | [-6.82, -0.61] |
| 3c | 18 | -3.52 µV | 1.82 | 0.43 | [-7.13, -0.12] |
| 3d | 7 | -6.23 µV | 3.84 | 1.45 | [-12.70, -2.99] |
| 3e | 17 | -5.72 µV | 3.87 | 0.94 | [-14.92, -1.69] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 19 | 163.13 ms | 13.69 | 3.14 | [137.13, 189.05] |
| 3b | 10 | 166.84 ms | 13.66 | 4.32 | [146.05, 190.39] |
| 3c | 18 | 166.37 ms | 14.37 | 3.39 | [146.06, 197.87] |
| 3d | 7 | 164.52 ms | 11.76 | 4.44 | [144.24, 180.43] |
| 3e | 17 | 167.21 ms | 10.64 | 2.58 | [143.52, 187.32] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 11 | 2.83 µV | 2.56 | 0.77 | [0.22, 9.04] |
| 3b | 8 | 2.29 µV | 1.34 | 0.48 | [-0.08, 3.94] |
| 3c | 12 | 3.14 µV | 3.07 | 0.89 | [-0.18, 11.15] |
| 3d | 9 | 1.79 µV | 1.65 | 0.55 | [0.21, 5.21] |
| 3e | 12 | 1.81 µV | 1.94 | 0.56 | [0.12, 6.91] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 11 | 85.46 ms | 11.55 | 3.48 | [69.17, 105.67] |
| 3b | 8 | 84.35 ms | 12.44 | 4.40 | [64.36, 97.88] |
| 3c | 12 | 91.51 ms | 10.09 | 2.91 | [72.64, 106.42] |
| 3d | 9 | 85.30 ms | 13.82 | 4.61 | [67.96, 102.08] |
| 3e | 12 | 87.51 ms | 15.36 | 4.44 | [64.27, 107.26] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 9 | 3.73 µV | 1.78 | 0.59 | [0.04, 5.71] |
| 3b | 9 | 3.54 µV | 2.15 | 0.72 | [1.11, 6.68] |
| 3c | 15 | 4.66 µV | 3.78 | 0.98 | [0.29, 12.27] |
| 3d | 5 | 2.74 µV | 1.61 | 0.72 | [0.68, 5.17] |
| 3e | 15 | 6.02 µV | 4.56 | 1.18 | [0.20, 14.45] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3a | 9 | 470.42 ms | 33.71 | 11.24 | [428.33, 543.16] |
| 3b | 9 | 453.10 ms | 39.42 | 13.14 | [395.77, 499.31] |
| 3c | 15 | 475.42 ms | 33.18 | 8.57 | [398.68, 519.98] |
| 3d | 5 | 443.47 ms | 37.35 | 16.71 | [399.02, 491.41] |
| 3e | 15 | 478.00 ms | 25.90 | 6.69 | [449.04, 539.11] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 326.31, BIC = 344.41
- **3b vs 3a**: *β* = 0.52, *SE* = 0.825, *z* = 0.628, *p* = 0.530
- **3c vs 3a**: *β* = 1.43, *SE* = 0.696, *z* = 2.051, *p* = 0.040
- **3d vs 3a**: *β* = -1.37, *SE* = 0.942, *z* = -1.458, *p* = 0.145
- **3e vs 3a**: *β* = 0.33, *SE* = 0.748, *z* = 0.437, *p* = 0.662
- **SNR**: *β* = -0.88, *SE* = 0.122, *z* = -7.162, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.52 | 0.82 | -0.63 | 0.530 | 0.896 | n.s. |
| 3a - 3c | -1.43 | 0.70 | -2.05 | 0.040 | 0.309 | n.s. |
| 3a - 3d | 1.37 | 0.94 | 1.46 | 0.145 | 0.575 | n.s. |
| 3a - 3e | -0.33 | 0.75 | -0.44 | 0.662 | 0.896 | n.s. |
| 3b - 3c | -0.91 | 0.85 | -1.07 | 0.284 | 0.738 | n.s. |
| 3b - 3d | 1.89 | 1.06 | 1.79 | 0.073 | 0.455 | n.s. |
| 3b - 3e | 0.19 | 0.91 | 0.21 | 0.832 | 0.896 | n.s. |
| 3c - 3d | 2.80 | 0.94 | 2.97 | 0.003 | 0.029 | * |
| 3c - 3e | 1.10 | 0.73 | 1.50 | 0.133 | 0.575 | n.s. |
| 3d - 3e | -1.70 | 0.97 | -1.75 | 0.080 | 0.455 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 573.51, BIC = 591.62
- **3b vs 3a**: *β* = 5.67, *SE* = 4.561, *z* = 1.244, *p* = 0.214
- **3c vs 3a**: *β* = 3.83, *SE* = 3.705, *z* = 1.034, *p* = 0.301
- **3d vs 3a**: *β* = 2.57, *SE* = 5.169, *z* = 0.497, *p* = 0.619
- **3e vs 3a**: *β* = 5.80, *SE* = 4.015, *z* = 1.444, *p* = 0.149
- **SNR**: *β* = -0.17, *SE* = 0.698, *z* = -0.237, *p* = 0.812

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -5.67 | 4.56 | -1.24 | 0.214 | 0.885 | n.s. |
| 3a - 3c | -3.83 | 3.71 | -1.03 | 0.301 | 0.943 | n.s. |
| 3a - 3d | -2.57 | 5.17 | -0.50 | 0.619 | 0.996 | n.s. |
| 3a - 3e | -5.80 | 4.01 | -1.44 | 0.149 | 0.800 | n.s. |
| 3b - 3c | 1.84 | 4.67 | 0.39 | 0.694 | 0.996 | n.s. |
| 3b - 3d | 3.11 | 5.79 | 0.54 | 0.591 | 0.996 | n.s. |
| 3b - 3e | -0.12 | 4.98 | -0.02 | 0.980 | 0.996 | n.s. |
| 3c - 3d | 1.27 | 5.13 | 0.25 | 0.805 | 0.996 | n.s. |
| 3c - 3e | -1.97 | 3.90 | -0.50 | 0.614 | 0.996 | n.s. |
| 3d - 3e | -3.23 | 5.35 | -0.60 | 0.546 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 208.47, BIC = 224.08
- **3b vs 3a**: *β* = -0.96, *SE* = 0.671, *z* = -1.434, *p* = 0.152
- **3c vs 3a**: *β* = -0.88, *SE* = 0.617, *z* = -1.423, *p* = 0.155
- **3d vs 3a**: *β* = -0.74, *SE* = 0.642, *z* = -1.154, *p* = 0.248
- **3e vs 3a**: *β* = -1.01, *SE* = 0.582, *z* = -1.729, *p* = 0.084
- **SNR**: *β* = 1.96, *SE* = 0.269, *z* = 7.281, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 0.96 | 0.67 | 1.43 | 0.152 | 0.772 | n.s. |
| 3a - 3c | 0.88 | 0.62 | 1.42 | 0.155 | 0.772 | n.s. |
| 3a - 3d | 0.74 | 0.64 | 1.15 | 0.248 | 0.864 | n.s. |
| 3a - 3e | 1.01 | 0.58 | 1.73 | 0.084 | 0.584 | n.s. |
| 3b - 3c | -0.08 | 0.65 | -0.13 | 0.896 | 0.999 | n.s. |
| 3b - 3d | -0.22 | 0.72 | -0.31 | 0.758 | 0.999 | n.s. |
| 3b - 3e | 0.04 | 0.66 | 0.07 | 0.947 | 0.999 | n.s. |
| 3c - 3d | -0.14 | 0.67 | -0.21 | 0.837 | 0.999 | n.s. |
| 3c - 3e | 0.13 | 0.62 | 0.21 | 0.835 | 0.999 | n.s. |
| 3d - 3e | 0.27 | 0.63 | 0.42 | 0.675 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 419.27, BIC = 434.88
- **3b vs 3a**: *β* = 1.27, *SE* = 5.053, *z* = 0.252, *p* = 0.801
- **3c vs 3a**: *β* = 5.71, *SE* = 4.559, *z* = 1.251, *p* = 0.211
- **3d vs 3a**: *β* = -0.16, *SE* = 4.745, *z* = -0.033, *p* = 0.973
- **3e vs 3a**: *β* = 3.70, *SE* = 4.345, *z* = 0.850, *p* = 0.395
- **SNR**: *β* = 0.50, *SE* = 2.012, *z* = 0.248, *p* = 0.804

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -1.27 | 5.05 | -0.25 | 0.801 | 0.992 | n.s. |
| 3a - 3c | -5.71 | 4.56 | -1.25 | 0.211 | 0.906 | n.s. |
| 3a - 3d | 0.16 | 4.75 | 0.03 | 0.973 | 0.992 | n.s. |
| 3a - 3e | -3.70 | 4.35 | -0.85 | 0.395 | 0.972 | n.s. |
| 3b - 3c | -4.43 | 4.86 | -0.91 | 0.362 | 0.972 | n.s. |
| 3b - 3d | 1.43 | 5.50 | 0.26 | 0.795 | 0.992 | n.s. |
| 3b - 3e | -2.42 | 4.90 | -0.49 | 0.621 | 0.992 | n.s. |
| 3c - 3d | 5.86 | 4.97 | 1.18 | 0.238 | 0.914 | n.s. |
| 3c - 3e | 2.01 | 4.65 | 0.43 | 0.666 | 0.992 | n.s. |
| 3d - 3e | -3.85 | 4.81 | -0.80 | 0.423 | 0.972 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 249.54, BIC = 265.30
- **3b vs 3a**: *β* = 0.46, *SE* = 0.968, *z* = 0.471, *p* = 0.638
- **3c vs 3a**: *β* = 0.70, *SE* = 0.875, *z* = 0.798, *p* = 0.425
- **3d vs 3a**: *β* = -0.10, *SE* = 1.183, *z* = -0.089, *p* = 0.929
- **3e vs 3a**: *β* = 0.69, *SE* = 0.889, *z* = 0.779, *p* = 0.436
- **SNR**: *β* = 0.76, *SE* = 0.095, *z* = 8.015, *p* < .001

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | -0.46 | 0.97 | -0.47 | 0.638 | 0.998 | n.s. |
| 3a - 3c | -0.70 | 0.88 | -0.80 | 0.425 | 0.996 | n.s. |
| 3a - 3d | 0.10 | 1.18 | 0.09 | 0.929 | 0.998 | n.s. |
| 3a - 3e | -0.69 | 0.89 | -0.78 | 0.436 | 0.996 | n.s. |
| 3b - 3c | -0.24 | 0.86 | -0.28 | 0.777 | 0.998 | n.s. |
| 3b - 3d | 0.56 | 1.20 | 0.47 | 0.639 | 0.998 | n.s. |
| 3b - 3e | -0.24 | 0.90 | -0.26 | 0.793 | 0.998 | n.s. |
| 3c - 3d | 0.80 | 1.12 | 0.72 | 0.474 | 0.996 | n.s. |
| 3c - 3e | 0.01 | 0.75 | 0.01 | 0.994 | 0.998 | n.s. |
| 3d - 3e | -0.80 | 1.15 | -0.69 | 0.488 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 522.02, BIC = 537.78
- **3b vs 3a**: *β* = -18.23, *SE* = 11.710, *z* = -1.557, *p* = 0.119
- **3c vs 3a**: *β* = 1.67, *SE* = 10.773, *z* = 0.155, *p* = 0.877
- **3d vs 3a**: *β* = -33.28, *SE* = 14.638, *z* = -2.273, *p* = 0.023
- **3e vs 3a**: *β* = 5.87, *SE* = 10.875, *z* = 0.540, *p* = 0.589
- **SNR**: *β* = -2.44, *SE* = 1.157, *z* = -2.111, *p* = 0.035

_Reference condition: **3a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3a - 3b | 18.23 | 11.71 | 1.56 | 0.119 | 0.471 | n.s. |
| 3a - 3c | -1.67 | 10.77 | -0.16 | 0.877 | 0.931 | n.s. |
| 3a - 3d | 33.28 | 14.64 | 2.27 | 0.023 | 0.170 | n.s. |
| 3a - 3e | -5.87 | 10.87 | -0.54 | 0.589 | 0.931 | n.s. |
| 3b - 3c | -19.91 | 10.26 | -1.94 | 0.052 | 0.276 | n.s. |
| 3b - 3d | 15.04 | 14.90 | 1.01 | 0.313 | 0.777 | n.s. |
| 3b - 3e | -24.11 | 10.93 | -2.21 | 0.027 | 0.177 | n.s. |
| 3c - 3d | 34.95 | 13.76 | 2.54 | 0.011 | 0.095 | n.s. |
| 3c - 3e | -4.20 | 8.95 | -0.47 | 0.639 | 0.931 | n.s. |
| 3d - 3e | -39.15 | 13.98 | -2.80 | 0.005 | 0.050 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


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
