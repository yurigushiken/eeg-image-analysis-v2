# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:50:46

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
| Decrease by 1 (no 1) | 24 | -3.66 µV | 1.65 | 0.34 | [-7.35, -0.81] |
| Decrease by 2 (no 1) | 24 | -3.63 µV | 1.86 | 0.38 | [-8.20, -0.51] |
| Decrease by 3 (no 1) | 24 | -4.26 µV | 2.05 | 0.42 | [-8.18, -0.66] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 24 | 177.19 ms | 9.43 | 1.92 | [160.83, 206.12] |
| Decrease by 2 (no 1) | 24 | 177.03 ms | 9.76 | 1.99 | [158.87, 206.60] |
| Decrease by 3 (no 1) | 24 | 177.39 ms | 9.21 | 1.88 | [161.70, 206.74] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 10 | 1.88 µV | 1.48 | 0.47 | [0.27, 3.86] |
| Decrease by 2 (no 1) | 17 | 1.60 µV | 1.02 | 0.25 | [0.17, 3.79] |
| Decrease by 3 (no 1) | 16 | 1.59 µV | 1.46 | 0.36 | [-0.07, 5.37] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 10 | 110.75 ms | 1.76 | 0.56 | [107.87, 113.57] |
| Decrease by 2 (no 1) | 17 | 111.19 ms | 2.29 | 0.56 | [106.62, 113.93] |
| Decrease by 3 (no 1) | 16 | 109.87 ms | 4.77 | 1.19 | [100.53, 117.00] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 3.00 µV | 2.04 | 0.47 | [0.06, 7.15] |
| Decrease by 2 (no 1) | 18 | 3.45 µV | 1.77 | 0.42 | [1.15, 6.62] |
| Decrease by 3 (no 1) | 19 | 3.70 µV | 2.70 | 0.62 | [0.09, 10.95] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 1 (no 1) | 19 | 476.93 ms | 19.39 | 4.45 | [427.28, 509.24] |
| Decrease by 2 (no 1) | 18 | 475.42 ms | 13.04 | 3.07 | [449.12, 490.16] |
| Decrease by 3 (no 1) | 19 | 474.15 ms | 16.90 | 3.88 | [444.22, 509.16] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 247.11, BIC = 260.77
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.01, *SE* = 0.260, *z* = -0.021, *p* = 0.983
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.82, *SE* = 0.265, *z* = -3.096, *p* = 0.002
- **SNR**: *β* = -0.16, *SE* = 0.037, *z* = -4.268, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.01 | 0.26 | 0.02 | 0.983 | 0.983 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.82 | 0.27 | 3.10 | 0.002 | 0.006 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.82 | 0.26 | 3.09 | 0.002 | 0.006 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.06, *p* = 0.057, η²_G = 0.025
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.09 | 23 | = 0.929 | -0.01 [-0.44, 0.40] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.04 | 23 | = 0.080 | 0.32 [-0.02, 0.86] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.20 | 23 | = 0.080 | 0.32 [0.01, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 455.78, BIC = 469.44
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.17, *SE* = 0.892, *z* = -0.192, *p* = 0.848
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.11, *SE* = 0.912, *z* = 0.119, *p* = 0.905
- **SNR**: *β* = -0.07, *SE* = 0.140, *z* = -0.477, *p* = 0.633

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.17 | 0.89 | 0.19 | 0.848 | 0.986 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.11 | 0.91 | -0.12 | 0.905 | 0.986 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.28 | 0.91 | -0.31 | 0.758 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.08, *p* = 0.925, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.17 | 23 | = 0.869 | 0.02 [-0.39, 0.46] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.23 | 23 | = 0.869 | -0.02 [-0.47, 0.38] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.40 | 23 | = 0.869 | -0.04 [-0.50, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 117.21, BIC = 127.78
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.15, *SE* = 0.270, *z* = 0.540, *p* = 0.589
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.21, *SE* = 0.278, *z* = 0.768, *p* = 0.442
- **SNR**: *β* = 0.21, *SE* = 0.045, *z* = 4.591, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.15 | 0.27 | -0.54 | 0.589 | 0.831 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.21 | 0.28 | -0.77 | 0.442 | 0.827 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.07 | 0.23 | -0.29 | 0.768 | 0.831 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.03, *p* = 0.966, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.34 | 7 | = 0.933 | -0.09 [-0.94, 0.61] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.09 | 7 | = 0.933 | -0.02 [-0.87, 0.81] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.14 | 7 | = 0.933 | 0.06 [-0.61, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 228.86, BIC = 239.43
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.66, *SE* = 0.925, *z* = 0.718, *p* = 0.473
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.11, *SE* = 0.979, *z* = 0.111, *p* = 0.911
- **SNR**: *β* = 0.06, *SE* = 0.139, *z* = 0.438, *p* = 0.661

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.66 | 0.93 | -0.72 | 0.473 | 0.853 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.11 | 0.98 | -0.11 | 0.911 | 0.911 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.56 | 0.80 | 0.69 | 0.488 | 0.853 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.493, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.75 | 7 | = 0.369 | -0.32 [-1.46, 0.22] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -1.03 | 7 | = 0.503 | -0.33 [-1.23, 0.50] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.27 | 7 | = 0.797 | -0.08 [-0.55, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 198.66, BIC = 210.81
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = 0.87, *SE* = 0.321, *z* = 2.705, *p* = 0.007
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = 1.02, *SE* = 0.306, *z* = 3.334, *p* = 0.001
- **SNR**: *β* = 0.27, *SE* = 0.047, *z* = 5.628, *p* < .001

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.87 | 0.32 | -2.70 | 0.007 | 0.014 | * |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.02 | 0.31 | -3.33 | < .001 | 0.003 | ** |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.15 | 0.31 | -0.49 | 0.626 | 0.626 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.54, *p* = 0.229, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.95 | 16 | = 0.396 | -0.15 [-0.75, 0.29] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -1.71 | 16 | = 0.323 | -0.29 [-0.98, 0.06] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.87 | 16 | = 0.396 | -0.17 [-0.73, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 468.30, BIC = 480.45
- **Decrease by 2 (no 1) vs Decrease by 1 (no 1)**: *β* = -0.95, *SE* = 3.693, *z* = -0.256, *p* = 0.798
- **Decrease by 3 (no 1) vs Decrease by 1 (no 1)**: *β* = -4.31, *SE* = 3.578, *z* = -1.203, *p* = 0.229
- **SNR**: *β* = 0.63, *SE* = 0.493, *z* = 1.272, *p* = 0.203

_Reference condition: **Decrease by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.95 | 3.69 | 0.26 | 0.798 | 0.798 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 4.31 | 3.58 | 1.20 | 0.229 | 0.541 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 3.36 | 3.60 | 0.93 | 0.351 | 0.579 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.05, *p* = 0.360, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.58 | 16 | = 0.570 | 0.15 [-0.38, 0.66] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 1.55 | 16 | = 0.423 | 0.32 [-0.07, 0.97] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.83 | 16 | = 0.570 | 0.21 [-0.32, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.057)

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
