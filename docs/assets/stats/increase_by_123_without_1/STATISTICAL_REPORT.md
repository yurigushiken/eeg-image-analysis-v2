# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:54:43

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
| Increase by 1 (no 1) | 23 | -3.42 µV | 1.60 | 0.33 | [-6.81, -0.18] |
| Increase by 2 (no 1) | 23 | -3.46 µV | 1.99 | 0.41 | [-8.05, -0.48] |
| Increase by 3 (no 1) | 23 | -4.17 µV | 2.03 | 0.42 | [-10.47, -1.23] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 23 | 171.18 ms | 9.02 | 1.88 | [147.82, 192.50] |
| Increase by 2 (no 1) | 23 | 171.33 ms | 11.73 | 2.45 | [151.87, 201.74] |
| Increase by 3 (no 1) | 23 | 171.92 ms | 9.72 | 2.03 | [158.01, 195.01] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 15 | 0.93 µV | 0.79 | 0.20 | [0.01, 2.52] |
| Increase by 2 (no 1) | 16 | 1.03 µV | 0.96 | 0.24 | [0.05, 3.25] |
| Increase by 3 (no 1) | 12 | 1.48 µV | 1.80 | 0.52 | [0.13, 6.81] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 15 | 96.89 ms | 5.91 | 1.53 | [82.78, 107.08] |
| Increase by 2 (no 1) | 16 | 96.37 ms | 6.33 | 1.58 | [83.99, 106.01] |
| Increase by 3 (no 1) | 12 | 94.30 ms | 7.11 | 2.05 | [82.78, 102.64] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 2.85 µV | 2.23 | 0.56 | [0.30, 7.45] |
| Increase by 2 (no 1) | 17 | 3.93 µV | 2.22 | 0.54 | [0.23, 8.39] |
| Increase by 3 (no 1) | 21 | 2.87 µV | 1.78 | 0.39 | [0.50, 6.24] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 472.82 ms | 18.50 | 4.62 | [431.76, 502.37] |
| Increase by 2 (no 1) | 17 | 476.30 ms | 15.86 | 3.85 | [453.77, 520.70] |
| Increase by 3 (no 1) | 21 | 467.76 ms | 16.53 | 3.61 | [425.35, 509.63] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 241.69, BIC = 255.10
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.08, *SE* = 0.273, *z* = -0.282, *p* = 0.778
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -0.88, *SE* = 0.272, *z* = -3.243, *p* = 0.001
- **SNR**: *β* = -0.14, *SE* = 0.040, *z* = -3.604, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.08 | 0.27 | 0.28 | 0.778 | 0.778 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.88 | 0.27 | 3.24 | 0.001 | 0.004 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.81 | 0.27 | 2.94 | 0.003 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.95, *p* = 0.027, η²_G = 0.036
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.13 | 21 | = 0.901 | 0.02 [-0.42, 0.47] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.62 | 21 | = 0.048 | 0.42 [0.11, 1.04] | small | * |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.26 | 21 | = 0.052 | 0.36 [0.01, 0.95] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 468.66, BIC = 482.06
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.36, *SE* = 1.193, *z* = -0.303, *p* = 0.762
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.58, *SE* = 1.184, *z* = 0.487, *p* = 0.626
- **SNR**: *β* = -0.17, *SE* = 0.173, *z* = -1.013, *p* = 0.311

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.36 | 1.19 | 0.30 | 0.762 | 0.860 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.58 | 1.18 | -0.49 | 0.626 | 0.860 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.94 | 1.20 | -0.78 | 0.433 | 0.818 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.68, *p* = 0.514, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.24 | 21 | = 0.811 | 0.03 [-0.39, 0.50] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.83 | 21 | = 0.622 | -0.12 [-0.56, 0.31] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -1.07 | 21 | = 0.622 | -0.14 [-0.68, 0.22] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 71.46, BIC = 82.03
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.10, *SE* = 0.155, *z* = 0.656, *p* = 0.512
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.40, *SE* = 0.164, *z* = 2.471, *p* = 0.013
- **SNR**: *β* = 0.69, *SE* = 0.057, *z* = 12.074, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.10 | 0.15 | -0.66 | 0.512 | 0.512 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.40 | 0.16 | -2.47 | 0.013 | 0.040 | * |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.30 | 0.16 | -1.85 | 0.065 | 0.125 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.479, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.02 | 6 | = 0.520 | -0.34 [-0.85, 0.59] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.05 | 6 | = 0.520 | -0.39 [-1.23, 0.28] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.54 | 6 | = 0.606 | -0.17 [-0.90, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.21, BIC = 290.77
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -1.51, *SE* = 1.545, *z* = -0.980, *p* = 0.327
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -2.87, *SE* = 1.598, *z* = -1.796, *p* = 0.073
- **SNR**: *β* = 0.21, *SE* = 0.628, *z* = 0.341, *p* = 0.733

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.51 | 1.54 | 0.98 | 0.327 | 0.547 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 2.87 | 1.60 | 1.80 | 0.073 | 0.202 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 1.36 | 1.62 | 0.84 | 0.403 | 0.547 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.36, *p* = 0.294, η²_G = 0.101
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.60 | 6 | = 0.572 | 0.34 [-0.49, 0.96] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.31 | 6 | = 0.357 | 0.69 [-0.28, 1.23] | medium | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.64 | 6 | = 0.357 | 0.44 [-0.36, 1.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 188.68, BIC = 200.61
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.75, *SE* = 0.348, *z* = 2.156, *p* = 0.031
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.66, *SE* = 0.328, *z* = 2.005, *p* = 0.045
- **SNR**: *β* = 0.31, *SE* = 0.056, *z* = 5.457, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.75 | 0.35 | -2.16 | 0.031 | 0.090 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.66 | 0.33 | -2.01 | 0.045 | 0.090 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.09 | 0.34 | 0.27 | 0.787 | 0.787 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.70, *p* = 0.017, η²_G = 0.072
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -3.61 | 14 | = 0.009 | -0.60 [-1.59, -0.27] | medium | ** |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.30 | 14 | = 0.214 | -0.32 [-0.90, 0.20] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.59 | 14 | = 0.201 | 0.37 [-0.17, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 463.27, BIC = 475.20
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 3.76, *SE* = 4.789, *z* = 0.785, *p* = 0.433
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -7.25, *SE* = 4.616, *z* = -1.570, *p* = 0.116
- **SNR**: *β* = -0.34, *SE* = 0.626, *z* = -0.536, *p* = 0.592

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -3.76 | 4.79 | -0.78 | 0.433 | 0.433 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 7.25 | 4.62 | 1.57 | 0.116 | 0.219 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 11.01 | 4.70 | 2.34 | 0.019 | 0.057 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.38, *p* = 0.111, η²_G = 0.073
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.50 | 14 | = 0.628 | -0.15 [-0.68, 0.43] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.64 | 14 | = 0.185 | 0.44 [-0.08, 1.05] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.05 | 14 | = 0.178 | 0.70 [0.04, 1.16] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.027). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.42)
**P3b amplitude:** Significant main effect of condition (*p* = 0.017). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -0.60)

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
