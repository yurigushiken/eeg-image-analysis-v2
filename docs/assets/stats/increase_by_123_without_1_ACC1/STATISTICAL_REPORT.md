# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:22:39

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
| Increase by 1 (no 1) | 22 | -3.52 µV | 1.52 | 0.32 | [-6.76, -0.36] |
| Increase by 2 (no 1) | 24 | -3.42 µV | 2.15 | 0.44 | [-8.62, -0.33] |
| Increase by 3 (no 1) | 23 | -4.33 µV | 2.22 | 0.46 | [-10.60, -1.05] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 22 | 168.91 ms | 8.32 | 1.77 | [147.98, 186.54] |
| Increase by 2 (no 1) | 24 | 172.37 ms | 12.49 | 2.55 | [152.30, 199.82] |
| Increase by 3 (no 1) | 23 | 172.68 ms | 10.81 | 2.25 | [155.64, 195.69] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 1.35 µV | 1.35 | 0.34 | [0.12, 4.48] |
| Increase by 2 (no 1) | 15 | 1.08 µV | 1.09 | 0.28 | [0.01, 3.78] |
| Increase by 3 (no 1) | 13 | 1.64 µV | 1.88 | 0.52 | [0.17, 7.11] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 98.24 ms | 4.91 | 1.23 | [88.16, 106.23] |
| Increase by 2 (no 1) | 15 | 97.36 ms | 6.21 | 1.60 | [85.13, 105.67] |
| Increase by 3 (no 1) | 13 | 96.00 ms | 5.44 | 1.51 | [84.82, 103.88] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 18 | 3.12 µV | 2.36 | 0.56 | [0.04, 7.20] |
| Increase by 2 (no 1) | 18 | 3.97 µV | 2.45 | 0.58 | [0.15, 8.68] |
| Increase by 3 (no 1) | 22 | 2.84 µV | 1.83 | 0.39 | [0.01, 6.45] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 18 | 477.41 ms | 19.74 | 4.65 | [421.66, 508.54] |
| Increase by 2 (no 1) | 18 | 480.57 ms | 14.46 | 3.41 | [458.21, 511.49] |
| Increase by 3 (no 1) | 22 | 473.46 ms | 19.28 | 4.11 | [429.83, 530.35] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 252.86, BIC = 266.26
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.06, *SE* = 0.304, *z* = -0.183, *p* = 0.855
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -0.97, *SE* = 0.304, *z* = -3.196, *p* = 0.001
- **SNR**: *β* = -0.14, *SE* = 0.036, *z* = -3.894, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.06 | 0.30 | 0.18 | 0.855 | 0.855 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.97 | 0.30 | 3.20 | 0.001 | 0.004 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.92 | 0.30 | 3.06 | 0.002 | 0.004 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.67, *p* = 0.015, η²_G = 0.048
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.52 | 21 | = 0.612 | 0.09 [-0.33, 0.55] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.87 | 21 | = 0.027 | 0.52 [0.13, 1.10] | medium | * |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.30 | 21 | = 0.047 | 0.38 [0.04, 0.96] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 488.46, BIC = 501.86
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 1.64, *SE* = 1.473, *z* = 1.116, *p* = 0.265
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 2.86, *SE* = 1.470, *z* = 1.944, *p* = 0.052
- **SNR**: *β* = -0.10, *SE* = 0.171, *z* = -0.593, *p* = 0.553

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -1.64 | 1.47 | -1.12 | 0.265 | 0.459 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -2.86 | 1.47 | -1.94 | 0.052 | 0.148 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -1.21 | 1.45 | -0.84 | 0.402 | 0.459 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.88, *p* = 0.165, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.75 | 21 | = 0.459 | -0.12 [-0.61, 0.29] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.58 | 21 | = 0.192 | -0.31 [-0.79, 0.12] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -1.66 | 21 | = 0.192 | -0.17 [-0.75, 0.14] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 120.69, BIC = 131.40
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.05, *SE* = 0.293, *z* = 0.179, *p* = 0.858
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.45, *SE* = 0.303, *z* = 1.470, *p* = 0.142
- **SNR**: *β* = 0.72, *SE* = 0.092, *z* = 7.863, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.05 | 0.29 | -0.18 | 0.858 | 0.858 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.45 | 0.30 | -1.47 | 0.142 | 0.367 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.39 | 0.31 | -1.28 | 0.201 | 0.367 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.654, η²_G = 0.027
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.25 | 5 | = 0.811 | 0.11 [-0.54, 0.90] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.60 | 5 | = 0.811 | -0.24 [-1.06, 0.51] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.99 | 5 | = 0.811 | -0.34 [-1.22, 0.39] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 270.94, BIC = 281.65
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -1.62, *SE* = 1.262, *z* = -1.283, *p* = 0.199
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -1.82, *SE* = 1.281, *z* = -1.417, *p* = 0.156
- **SNR**: *β* = 0.23, *SE* = 0.514, *z* = 0.441, *p* = 0.659

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.62 | 1.26 | 1.28 | 0.199 | 0.400 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.82 | 1.28 | 1.42 | 0.156 | 0.400 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.20 | 1.30 | 0.15 | 0.880 | 0.880 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.96, *p* = 0.098, η²_G = 0.139
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.06 | 5 | = 0.956 | -0.02 [-0.50, 0.95] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 3.33 | 5 | = 0.062 | 0.69 [0.19, 2.21] | medium | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.78 | 5 | = 0.202 | 0.82 [-0.72, 0.81] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 202.53, BIC = 214.89
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.35, *SE* = 0.303, *z* = 1.170, *p* = 0.242
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.12, *SE* = 0.283, *z* = 0.444, *p* = 0.657
- **SNR**: *β* = 0.24, *SE* = 0.049, *z* = 4.978, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.35 | 0.30 | -1.17 | 0.242 | 0.564 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.13 | 0.28 | -0.44 | 0.657 | 0.690 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.23 | 0.30 | 0.77 | 0.443 | 0.690 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.61, *p* = 0.089, η²_G = 0.025
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -2.33 | 16 | = 0.100 | -0.32 [-1.12, -0.01] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.49 | 16 | = 0.629 | -0.09 [-0.60, 0.39] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.55 | 16 | = 0.211 | 0.29 [-0.10, 0.93] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 502.74, BIC = 515.10
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 4.92, *SE* = 4.690, *z* = 1.048, *p* = 0.295
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -6.58, *SE* = 4.472, *z* = -1.472, *p* = 0.141
- **SNR**: *β* = -0.75, *SE* = 0.609, *z* = -1.239, *p* = 0.215

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -4.92 | 4.69 | -1.05 | 0.295 | 0.295 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 6.58 | 4.47 | 1.47 | 0.141 | 0.262 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 11.50 | 4.72 | 2.44 | 0.015 | 0.044 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.97, *p* = 0.029, η²_G = 0.097
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.02 | 16 | = 0.324 | -0.31 [-0.77, 0.27] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.90 | 16 | = 0.113 | 0.44 [-0.00, 1.06] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.90 | 16 | = 0.032 | 0.86 [0.12, 1.22] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.015). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.52)
  - Increase by 2 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.38)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.098)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.089)
**P3b latency:** Significant main effect of condition (*p* = 0.029). Post-hoc tests revealed:
  - Increase by 2 (no 1) showed greater latency than Increase by 3 (no 1) (*d* = 0.86)

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
