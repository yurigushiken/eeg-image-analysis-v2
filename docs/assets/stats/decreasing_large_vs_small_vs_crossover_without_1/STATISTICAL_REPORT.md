# Statistical Analysis Report: tables

**Generated:** 2025-10-23 18:52:00

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
| Decreasing Crossover (no 1) | 24 | -4.00 µV | 1.81 | 0.37 | [-7.73, -0.59] |
| Decreasing Large (no 1) | 24 | -3.48 µV | 1.65 | 0.34 | [-7.01, -0.85] |
| Decreasing Small (no 1) | 24 | -3.67 µV | 2.08 | 0.42 | [-8.19, -0.60] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 176.99 ms | 8.92 | 1.82 | [161.00, 207.27] |
| Decreasing Large (no 1) | 24 | 177.14 ms | 10.25 | 2.09 | [160.19, 204.33] |
| Decreasing Small (no 1) | 24 | 177.49 ms | 11.02 | 2.25 | [160.15, 207.30] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 16 | 1.29 µV | 1.12 | 0.28 | [0.01, 3.51] |
| Decreasing Large (no 1) | 13 | 2.13 µV | 1.60 | 0.44 | [0.38, 5.08] |
| Decreasing Small (no 1) | 11 | 1.80 µV | 1.41 | 0.43 | [0.01, 4.07] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 16 | 111.03 ms | 4.28 | 1.07 | [104.35, 118.99] |
| Decreasing Large (no 1) | 13 | 110.71 ms | 2.60 | 0.72 | [105.89, 114.86] |
| Decreasing Small (no 1) | 11 | 108.71 ms | 3.20 | 0.97 | [102.34, 112.90] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 3.41 µV | 2.36 | 0.53 | [0.16, 9.23] |
| Decreasing Large (no 1) | 18 | 2.74 µV | 2.16 | 0.51 | [0.23, 6.23] |
| Decreasing Small (no 1) | 18 | 4.23 µV | 3.27 | 0.77 | [0.12, 12.41] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 479.95 ms | 14.74 | 3.30 | [448.03, 507.86] |
| Decreasing Large (no 1) | 18 | 486.75 ms | 21.14 | 4.98 | [447.09, 527.81] |
| Decreasing Small (no 1) | 18 | 488.63 ms | 19.67 | 4.64 | [442.81, 529.06] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 260.20, BIC = 273.86
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.18, *SE* = 0.312, *z* = 0.569, *p* = 0.569
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.17, *SE* = 0.339, *z* = -0.500, *p* = 0.617
- **SNR**: *β* = -0.09, *SE* = 0.031, *z* = -2.798, *p* = 0.005

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.18 | 0.31 | -0.57 | 0.569 | 0.814 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.17 | 0.34 | 0.50 | 0.617 | 0.814 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.35 | 0.29 | 1.18 | 0.237 | 0.556 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.49, *p* = 0.236, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.41 | 23 | = 0.073 | -0.30 [-0.94, -0.04] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.05 | 23 | = 0.457 | -0.17 [-0.64, 0.21] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.51 | 23 | = 0.614 | 0.10 [-0.32, 0.53] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 494.35, BIC = 508.01
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.18, *SE* = 1.429, *z* = -0.127, *p* = 0.899
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.01, *SE* = 1.553, *z* = 0.004, *p* = 0.996
- **SNR**: *β* = -0.09, *SE* = 0.144, *z* = -0.604, *p* = 0.546

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.18 | 1.43 | 0.13 | 0.899 | 0.999 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -0.01 | 1.55 | -0.00 | 0.996 | 0.999 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.19 | 1.34 | -0.14 | 0.889 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.07, *p* = 0.929, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.16 | 23 | = 0.878 | -0.02 [-0.45, 0.39] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.38 | 23 | = 0.878 | -0.05 [-0.50, 0.35] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.21 | 23 | = 0.878 | -0.03 [-0.47, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 123.45, BIC = 133.58
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.72, *SE* = 0.318, *z* = 2.277, *p* = 0.023
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.95, *SE* = 0.383, *z* = 2.485, *p* = 0.013
- **SNR**: *β* = 0.23, *SE* = 0.072, *z* = 3.250, *p* = 0.001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.72 | 0.32 | -2.28 | 0.023 | 0.045 | * |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -0.95 | 0.38 | -2.49 | 0.013 | 0.038 | * |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.23 | 0.42 | -0.55 | 0.586 | 0.586 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.66, *p* = 0.032, η²_G = 0.140
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -4.23 | 6 | = 0.016 | -0.84 [-1.70, -0.18] | large | * |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.39 | 6 | = 0.710 | -0.12 [-1.18, 0.41] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 1.89 | 6 | = 0.162 | 0.71 [-0.32, 1.75] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 215.50, BIC = 225.63
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -1.01, *SE* = 0.869, *z* = -1.165, *p* = 0.244
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -2.69, *SE* = 1.036, *z* = -2.591, *p* = 0.010
- **SNR**: *β* = -0.35, *SE* = 0.174, *z* = -2.033, *p* = 0.042

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 1.01 | 0.87 | 1.17 | 0.244 | 0.263 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 2.69 | 1.04 | 2.59 | 0.010 | 0.028 | * |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 1.67 | 1.14 | 1.47 | 0.142 | 0.263 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.286, η²_G = 0.118
- Greenhouse-Geisser corrected: *p* = 0.284 (ε = 0.527)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 1.21 | 6 | = 0.402 | 0.66 [-0.24, 1.09] | medium | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 1.15 | 6 | = 0.402 | 0.59 [-0.44, 1.14] | medium | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -0.90 | 6 | = 0.402 | -0.20 [-1.29, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 238.81, BIC = 250.96
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.10, *SE* = 0.506, *z* = 0.206, *p* = 0.837
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.86, *SE* = 0.521, *z* = 3.575, *p* < .001
- **SNR**: *β* = 0.20, *SE* = 0.043, *z* = 4.495, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.10 | 0.51 | -0.21 | 0.837 | 0.837 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -1.86 | 0.52 | -3.57 | < .001 | < .001 | *** |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -1.76 | 0.47 | -3.76 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.76, *p* = 0.016, η²_G = 0.082
- Greenhouse-Geisser corrected: *p* = 0.030 (ε = 0.697)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 1.89 | 15 | = 0.096 | 0.50 [-0.13, 0.91] | medium | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.78 | 15 | = 0.096 | -0.25 [-0.86, 0.16] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -2.44 | 15 | = 0.082 | -0.66 [-1.19, -0.03] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 485.22, BIC = 497.37
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 7.59, *SE* = 4.755, *z* = 1.596, *p* = 0.110
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 7.58, *SE* = 4.906, *z* = 1.544, *p* = 0.122
- **SNR**: *β* = -0.15, *SE* = 0.394, *z* = -0.377, *p* = 0.706

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -7.59 | 4.76 | -1.60 | 0.110 | 0.296 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -7.58 | 4.91 | -1.54 | 0.122 | 0.296 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.01 | 4.48 | 0.00 | 0.998 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.67, *p* = 0.206, η²_G = 0.046
- Greenhouse-Geisser corrected: *p* = 0.216 (ε = 0.653)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.09 | 15 | = 0.149 | -0.50 [-1.06, 0.01] | medium | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.76 | 15 | = 0.149 | -0.45 [-1.10, -0.03] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.31 | 15 | = 0.758 | 0.10 [-0.46, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Significant main effect of condition (*p* = 0.032). Post-hoc tests revealed:
  - Decreasing Crossover (no 1) showed smaller amplitude than Decreasing Large (no 1) (*d* = -0.84)
**P3b amplitude:** Significant main effect of condition (*p* = 0.016) (no significant pairwise comparisons)

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
