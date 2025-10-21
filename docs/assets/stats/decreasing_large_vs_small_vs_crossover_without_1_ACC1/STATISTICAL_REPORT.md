# Statistical Analysis Report: tables

**Generated:** 2025-10-20 21:50:37

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
| Decreasing Crossover (no 1) | 24 | -4.04 µV | 1.82 | 0.37 | [-7.80, -0.58] |
| Decreasing Large (no 1) | 24 | -3.56 µV | 1.79 | 0.36 | [-7.92, -0.95] |
| Decreasing Small (no 1) | 22 | -3.91 µV | 2.03 | 0.43 | [-8.19, -0.50] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 24 | 176.96 ms | 9.07 | 1.85 | [161.73, 207.43] |
| Decreasing Large (no 1) | 24 | 177.54 ms | 10.71 | 2.19 | [160.39, 203.75] |
| Decreasing Small (no 1) | 22 | 174.68 ms | 9.94 | 2.12 | [157.64, 198.60] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 15 | 1.52 µV | 1.06 | 0.27 | [0.05, 3.33] |
| Decreasing Large (no 1) | 14 | 2.31 µV | 1.39 | 0.37 | [0.11, 4.44] |
| Decreasing Small (no 1) | 9 | 2.08 µV | 1.57 | 0.52 | [-0.06, 4.37] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 15 | 112.15 ms | 2.83 | 0.73 | [106.37, 116.23] |
| Decreasing Large (no 1) | 14 | 112.59 ms | 1.49 | 0.40 | [110.21, 114.80] |
| Decreasing Small (no 1) | 9 | 110.94 ms | 2.75 | 0.92 | [104.24, 113.65] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 3.58 µV | 2.39 | 0.54 | [0.10, 9.31] |
| Decreasing Large (no 1) | 19 | 3.17 µV | 2.07 | 0.47 | [0.49, 7.04] |
| Decreasing Small (no 1) | 18 | 4.36 µV | 3.22 | 0.76 | [0.42, 12.56] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover (no 1) | 20 | 482.03 ms | 14.22 | 3.18 | [449.27, 507.62] |
| Decreasing Large (no 1) | 19 | 489.35 ms | 19.68 | 4.52 | [446.09, 529.45] |
| Decreasing Small (no 1) | 18 | 489.04 ms | 18.02 | 4.25 | [444.22, 527.84] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 257.84, BIC = 271.33
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.08, *SE* = 0.343, *z* = -0.228, *p* = 0.820
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.50, *SE* = 0.381, *z* = -1.304, *p* = 0.192
- **SNR**: *β* = -0.16, *SE* = 0.038, *z* = -4.142, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | 0.08 | 0.34 | 0.23 | 0.820 | 0.820 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.50 | 0.38 | 1.30 | 0.192 | 0.473 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 0.42 | 0.33 | 1.26 | 0.206 | 0.473 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.09, *p* = 0.346, η²_G = 0.016
- Greenhouse-Geisser corrected: *p* = 0.332 (ε = 0.747)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.06 | 21 | = 0.155 | -0.31 [-0.86, 0.02] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.05 | 21 | = 0.458 | -0.22 [-0.67, 0.22] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.27 | 21 | = 0.790 | 0.07 [-0.39, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 500.62, BIC = 514.11
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.12, *SE* = 1.781, *z* = 0.068, *p* = 0.946
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -1.55, *SE* = 1.982, *z* = -0.783, *p* = 0.434
- **SNR**: *β* = -0.13, *SE* = 0.201, *z* = -0.641, *p* = 0.522

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.12 | 1.78 | -0.07 | 0.946 | 0.946 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 1.55 | 1.98 | 0.78 | 0.434 | 0.700 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 1.67 | 1.72 | 0.97 | 0.330 | 0.700 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.18, *p* = 0.838, η²_G = 0.003
- Greenhouse-Geisser corrected: *p* = 0.747 (ε = 0.665)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.29 | 21 | = 0.778 | -0.04 [-0.53, 0.31] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | 0.40 | 21 | = 0.778 | 0.08 [-0.36, 0.53] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.46 | 21 | = 0.778 | 0.11 [-0.35, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 120.69, BIC = 130.52
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.75, *SE* = 0.336, *z* = 2.239, *p* = 0.025
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.93, *SE* = 0.416, *z* = 2.228, *p* = 0.026
- **SNR**: *β* = 0.23, *SE* = 0.079, *z* = 2.897, *p* = 0.004

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.75 | 0.34 | -2.24 | 0.025 | 0.074 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -0.93 | 0.42 | -2.23 | 0.026 | 0.074 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -0.18 | 0.43 | -0.41 | 0.680 | 0.680 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.440, η²_G = 0.046
- Greenhouse-Geisser corrected: *p* = 0.395 (ε = 0.563)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -3.05 | 6 | = 0.067 | -0.47 [-2.44, -0.58] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.84 | 6 | = 0.648 | -0.37 [-1.27, 0.63] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.31 | 6 | = 0.769 | 0.14 [-0.81, 1.04] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 182.00, BIC = 191.83
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.31, *SE* = 0.726, *z* = 0.425, *p* = 0.671
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = -0.80, *SE* = 0.955, *z* = -0.832, *p* = 0.405
- **SNR**: *β* = -0.04, *SE* = 0.154, *z* = -0.224, *p* = 0.823

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.31 | 0.73 | -0.43 | 0.671 | 0.671 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | 0.79 | 0.96 | 0.83 | 0.405 | 0.646 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 1.10 | 1.01 | 1.09 | 0.276 | 0.621 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.10, *p* = 0.909, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.774 (ε = 0.515)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -0.31 | 6 | = 0.841 | -0.19 [-0.65, 0.62] | negligible | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -0.36 | 6 | = 0.841 | -0.14 [-1.07, 0.79] | negligible | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.21 | 6 | = 0.841 | 0.10 [-0.85, 1.01] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 241.48, BIC = 253.74
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 0.24, *SE* = 0.478, *z* = 0.509, *p* = 0.611
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 1.72, *SE* = 0.509, *z* = 3.375, *p* = 0.001
- **SNR**: *β* = 0.18, *SE* = 0.044, *z* = 4.213, *p* < .001

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -0.24 | 0.48 | -0.51 | 0.611 | 0.611 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -1.72 | 0.51 | -3.37 | < .001 | 0.002 | ** |
| Decreasing Large (no 1) - Decreasing Small (no 1) | -1.48 | 0.46 | -3.24 | 0.001 | 0.002 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.05, *p* = 0.062, η²_G = 0.051
- Greenhouse-Geisser corrected: *p* = 0.086 (ε = 0.670)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | 1.36 | 15 | = 0.194 | 0.34 [-0.27, 0.74] | small | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.76 | 15 | = 0.147 | -0.23 [-0.83, 0.19] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | -1.93 | 15 | = 0.147 | -0.52 [-1.05, 0.08] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 483.87, BIC = 496.13
- **Decreasing Large (no 1) vs Decreasing Crossover (no 1)**: *β* = 8.13, *SE* = 4.110, *z* = 1.979, *p* = 0.048
- **Decreasing Small (no 1) vs Decreasing Crossover (no 1)**: *β* = 6.43, *SE* = 4.372, *z* = 1.471, *p* = 0.141
- **SNR**: *β* = -0.03, *SE* = 0.366, *z* = -0.087, *p* = 0.931

_Reference condition: **Decreasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover (no 1) - Decreasing Large (no 1) | -8.13 | 4.11 | -1.98 | 0.048 | 0.137 | n.s. |
| Decreasing Crossover (no 1) - Decreasing Small (no 1) | -6.43 | 4.37 | -1.47 | 0.141 | 0.263 | n.s. |
| Decreasing Large (no 1) - Decreasing Small (no 1) | 1.71 | 3.97 | 0.43 | 0.667 | 0.667 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.77, *p* = 0.188, η²_G = 0.048
- Greenhouse-Geisser corrected: *p* = 0.200 (ε = 0.679)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover (no 1) vs Decreasing Large (no 1) | -2.12 | 15 | = 0.153 | -0.53 [-1.06, 0.00] | medium | n.s. |
| Decreasing Crossover (no 1) vs Decreasing Small (no 1) | -1.56 | 15 | = 0.210 | -0.39 [-1.04, 0.02] | small | n.s. |
| Decreasing Large (no 1) vs Decreasing Small (no 1) | 0.54 | 15 | = 0.596 | 0.17 [-0.40, 0.67] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.062)

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

- Python 3.12.4
- MNE-Python 1.9.0
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
