# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:16:04

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
| Decrease by 1 (no 1) | 24 | -3.64 µV | 1.76 | 0.36 | [-7.23, -0.61] |
| Decrease by 2 (no 1) | 24 | -3.71 µV | 1.88 | 0.38 | [-8.28, -0.51] |
| Decrease by 3 (no 1) | 24 | -4.44 µV | 2.20 | 0.45 | [-8.89, -0.48] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 177.16 ms | 11.05 | 2.26 | [160.15, 206.93] |
| Decrease by 2 (no 1) | 24 | 176.99 ms | 9.58 | 1.96 | [160.35, 206.60] |
| Decrease by 3 (no 1) | 24 | 177.42 ms | 9.64 | 1.97 | [162.97, 208.13] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 11 | 1.65 µV | 1.40 | 0.42 | [0.00, 3.69] |
| Decrease by 2 (no 1) | 17 | 1.64 µV | 1.01 | 0.24 | [0.12, 3.95] |
| Decrease by 3 (no 1) | 16 | 1.61 µV | 1.39 | 0.35 | [-0.07, 5.05] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 11 | 109.25 ms | 5.11 | 1.54 | [100.21, 117.82] |
| Decrease by 2 (no 1) | 17 | 110.98 ms | 2.46 | 0.60 | [107.09, 114.77] |
| Decrease by 3 (no 1) | 16 | 109.57 ms | 4.58 | 1.14 | [100.53, 117.00] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 3.58 µV | 2.22 | 0.51 | [0.68, 8.14] |
| Decrease by 2 (no 1) | 19 | 3.39 µV | 1.87 | 0.43 | [0.09, 6.88] |
| Decrease by 3 (no 1) | 19 | 3.74 µV | 2.69 | 0.62 | [0.22, 10.89] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 480.68 ms | 17.23 | 3.95 | [442.98, 511.56] |
| Decrease by 2 (no 1) | 19 | 477.06 ms | 15.28 | 3.51 | [445.07, 493.39] |
| Decrease by 3 (no 1) | 19 | 475.94 ms | 17.46 | 4.00 | [442.84, 506.51] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 247.74, BIC = 261.40
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.10, *SE* = 0.261, *z* = -0.368, *p* = 0.713
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.90, *SE* = 0.261, *z* = -3.429, *p* = 0.001
- **SNR**: *β* = -0.25, *SE* = 0.040, *z* = -6.113, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.10 | 0.26 | 0.37 | 0.713 | 0.713 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.90 | 0.26 | 3.43 | < .001 | 0.002 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.80 | 0.26 | 3.06 | 0.002 | 0.004 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.63, *p* = 0.034, η²_G = 0.034
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.23 | 23 | = 0.819 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.42 | 23 | = 0.072 | 0.40 [0.05, 0.94] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.08 | 23 | = 0.073 | 0.36 [-0.02, 0.87] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 478.64, BIC = 492.30
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.18, *SE* = 1.105, *z* = -0.167, *p* = 0.868
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.19, *SE* = 1.107, *z* = 0.175, *p* = 0.861
- **SNR**: *β* = -0.18, *SE* = 0.185, *z* = -0.979, *p* = 0.328

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.18 | 1.11 | 0.17 | 0.868 | 0.981 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.19 | 1.11 | -0.17 | 0.861 | 0.981 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.38 | 1.11 | -0.34 | 0.733 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.07, *p* = 0.930, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.12 | 23 | = 0.903 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.25 | 23 | = 0.903 | -0.03 [-0.47, 0.37] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.43 | 23 | = 0.903 | -0.04 [-0.51, 0.33] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 120.28, BIC = 130.99
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.19, *SE* = 0.261, *z* = 0.724, *p* = 0.469
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.24, *SE* = 0.261, *z* = 0.909, *p* = 0.363
- **SNR**: *β* = 0.19, *SE* = 0.041, *z* = 4.590, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.19 | 0.26 | -0.72 | 0.469 | 0.742 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.24 | 0.26 | -0.91 | 0.363 | 0.742 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.05 | 0.22 | -0.21 | 0.831 | 0.831 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.37, *p* = 0.694, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.31 | 7 | = 0.699 | -0.33 [-1.43, 0.24] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.47 | 7 | = 0.767 | -0.14 [-0.92, 0.62] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.31 | 7 | = 0.767 | 0.13 [-0.58, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 236.07, BIC = 246.77
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.88, *SE* = 0.852, *z* = 1.029, *p* = 0.303
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.13, *SE* = 0.849, *z* = -0.158, *p* = 0.875
- **SNR**: *β* = 0.20, *SE* = 0.130, *z* = 1.554, *p* = 0.120

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.88 | 0.85 | -1.03 | 0.303 | 0.515 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.13 | 0.85 | 0.16 | 0.875 | 0.875 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.01 | 0.73 | 1.39 | 0.165 | 0.417 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.48, *p* = 0.629, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.02 | 7 | = 0.985 | -0.00 [-1.05, 0.51] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.91 | 7 | = 0.753 | 0.20 [-0.50, 1.07] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.71 | 7 | = 0.753 | 0.24 [-0.34, 0.83] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 201.64, BIC = 213.90
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.45, *SE* = 0.329, *z* = 1.366, *p* = 0.172
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.47, *SE* = 0.312, *z* = 1.523, *p* = 0.128
- **SNR**: *β* = 0.30, *SE* = 0.052, *z* = 5.844, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.45 | 0.33 | -1.37 | 0.172 | 0.337 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.47 | 0.31 | -1.52 | 0.128 | 0.337 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.03 | 0.32 | -0.08 | 0.935 | 0.935 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.72, *p* = 0.494, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.83 | 17 | = 0.588 | 0.12 [-0.31, 0.70] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.55 | 17 | = 0.588 | -0.08 [-0.63, 0.37] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.00 | 17 | = 0.588 | -0.20 [-0.74, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 478.94, BIC = 491.20
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -2.65, *SE* = 3.994, *z* = -0.663, *p* = 0.508
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -5.54, *SE* = 3.879, *z* = -1.428, *p* = 0.153
- **SNR**: *β* = 1.03, *SE* = 0.530, *z* = 1.950, *p* = 0.051

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 2.65 | 3.99 | 0.66 | 0.508 | 0.701 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 5.54 | 3.88 | 1.43 | 0.153 | 0.393 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 2.89 | 3.86 | 0.75 | 0.454 | 0.701 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.55, *p* = 0.093, η²_G = 0.054
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.49 | 17 | = 0.232 | 0.42 [-0.16, 0.86] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.66 | 17 | = 0.049 | 0.54 [0.08, 1.17] | medium | * |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.51 | 17 | = 0.616 | 0.14 [-0.38, 0.62] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.034) (no significant pairwise comparisons)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.093)

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
