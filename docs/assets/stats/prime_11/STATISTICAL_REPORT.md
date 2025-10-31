# Statistical Analysis Report: tables

**Generated:** 2025-10-30 19:27:41

---

## 1. Analysis Overview

**Total Measurements:** 170
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
| 1a | 10 | -4.32 µV | 3.20 | 1.01 | [-8.83, -0.12] |
| 1b | 14 | -2.75 µV | 2.26 | 0.60 | [-6.94, -0.31] |
| 1c | 14 | -3.41 µV | 2.41 | 0.64 | [-7.51, -0.45] |
| 1d | 18 | -2.48 µV | 2.66 | 0.63 | [-10.58, -0.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 10 | 176.47 ms | 8.98 | 2.84 | [157.51, 186.05] |
| 1b | 14 | 177.11 ms | 10.03 | 2.68 | [159.57, 194.65] |
| 1c | 14 | 176.88 ms | 10.10 | 2.70 | [162.29, 191.83] |
| 1d | 18 | 182.84 ms | 10.35 | 2.44 | [168.90, 201.58] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 3.77 µV | 2.72 | 0.76 | [0.25, 10.03] |
| 1b | 17 | 3.59 µV | 2.64 | 0.64 | [0.46, 10.88] |
| 1c | 16 | 3.26 µV | 3.68 | 0.92 | [0.06, 13.09] |
| 1d | 14 | 4.02 µV | 2.28 | 0.61 | [0.32, 7.31] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 124.82 ms | 9.18 | 2.54 | [102.58, 138.20] |
| 1b | 17 | 124.18 ms | 7.05 | 1.71 | [110.85, 136.06] |
| 1c | 16 | 123.59 ms | 12.44 | 3.11 | [100.54, 142.85] |
| 1d | 14 | 122.87 ms | 6.91 | 1.85 | [106.78, 134.76] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

_No descriptive statistics available._

#### Latency (50% Fractional Area)

_No descriptive statistics available._


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 239.23, BIC = 253.40
- **1b vs 1a**: *β* = 1.76, *SE* = 0.660, *z* = 2.661, *p* = 0.008
- **1c vs 1a**: *β* = 1.43, *SE* = 0.641, *z* = 2.229, *p* = 0.026
- **1d vs 1a**: *β* = 1.58, *SE* = 0.616, *z* = 2.568, *p* = 0.010
- **SNR**: *β* = -0.91, *SE* = 0.143, *z* = -6.366, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -1.76 | 0.66 | -2.66 | 0.008 | 0.046 | * |
| 1a - 1c | -1.43 | 0.64 | -2.23 | 0.026 | 0.099 | n.s. |
| 1a - 1d | -1.58 | 0.62 | -2.57 | 0.010 | 0.050 | n.s. |
| 1b - 1c | 0.33 | 0.59 | 0.56 | 0.578 | 0.925 | n.s. |
| 1b - 1d | 0.18 | 0.56 | 0.31 | 0.754 | 0.940 | n.s. |
| 1c - 1d | -0.15 | 0.56 | -0.27 | 0.784 | 0.940 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.99, *p* = 0.186, η²_G = 0.294
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.06 | 3 | = 0.958 | 0.03 [-1.22, 0.89] | negligible | n.s. |
| 1a vs 1c | 2.46 | 3 | = 0.273 | 1.29 [-0.90, 0.77] | large | n.s. |
| 1a vs 1d | -0.26 | 3 | = 0.958 | -0.14 [-1.28, 0.46] | negligible | n.s. |
| 1b vs 1c | 1.28 | 3 | = 0.584 | 1.11 [-0.44, 1.15] | large | n.s. |
| 1b vs 1d | -0.18 | 3 | = 0.958 | -0.15 [-0.95, 0.42] | negligible | n.s. |
| 1c vs 1d | -7.96 | 3 | = 0.025 | -1.59 [-0.75, 0.60] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 421.81, BIC = 435.99
- **1b vs 1a**: *β* = -1.79, *SE* = 3.600, *z* = -0.496, *p* = 0.620
- **1c vs 1a**: *β* = -1.09, *SE* = 3.465, *z* = -0.314, *p* = 0.754
- **1d vs 1a**: *β* = 4.17, *SE* = 3.416, *z* = 1.220, *p* = 0.222
- **SNR**: *β* = 0.79, *SE* = 0.755, *z* = 1.051, *p* = 0.293

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 1.79 | 3.60 | 0.50 | 0.620 | 0.945 | n.s. |
| 1a - 1c | 1.09 | 3.47 | 0.31 | 0.754 | 0.945 | n.s. |
| 1a - 1d | -4.17 | 3.42 | -1.22 | 0.222 | 0.634 | n.s. |
| 1b - 1c | -0.70 | 3.16 | -0.22 | 0.825 | 0.945 | n.s. |
| 1b - 1d | -5.96 | 2.99 | -1.99 | 0.046 | 0.248 | n.s. |
| 1c - 1d | -5.26 | 3.02 | -1.74 | 0.082 | 0.348 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.33, *p* = 0.801, η²_G = 0.067
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 1.35 | 3 | = 0.903 | 0.58 [-0.61, 1.62] | medium | n.s. |
| 1a vs 1c | 1.04 | 3 | = 0.903 | 0.66 [-0.70, 0.98] | medium | n.s. |
| 1a vs 1d | 0.54 | 3 | = 0.903 | 0.27 [-1.00, 0.68] | small | n.s. |
| 1b vs 1c | -0.13 | 3 | = 0.903 | -0.05 [-1.22, 0.38] | negligible | n.s. |
| 1b vs 1d | -0.30 | 3 | = 0.903 | -0.25 [-0.86, 0.50] | small | n.s. |
| 1c vs 1d | -0.27 | 3 | = 0.903 | -0.24 [-1.15, 0.26] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 284.42, BIC = 299.08
- **1b vs 1a**: *β* = -0.44, *SE* = 0.748, *z* = -0.589, *p* = 0.556
- **1c vs 1a**: *β* = -0.39, *SE* = 0.738, *z* = -0.533, *p* = 0.594
- **1d vs 1a**: *β* = 0.62, *SE* = 0.764, *z* = 0.806, *p* = 0.420
- **SNR**: *β* = 0.26, *SE* = 0.105, *z* = 2.454, *p* = 0.014

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 0.44 | 0.75 | 0.59 | 0.556 | 0.912 | n.s. |
| 1a - 1c | 0.39 | 0.74 | 0.53 | 0.594 | 0.912 | n.s. |
| 1a - 1d | -0.62 | 0.76 | -0.81 | 0.420 | 0.887 | n.s. |
| 1b - 1c | -0.05 | 0.70 | -0.07 | 0.946 | 0.946 | n.s. |
| 1b - 1d | -1.06 | 0.71 | -1.49 | 0.136 | 0.584 | n.s. |
| 1c - 1d | -1.01 | 0.73 | -1.39 | 0.164 | 0.592 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.92, *p* = 0.163, η²_G = 0.132
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -1.09 | 6 | = 0.478 | -0.53 [-1.04, 0.35] | medium | n.s. |
| 1a vs 1c | 0.35 | 6 | = 0.737 | 0.10 [-0.63, 0.91] | negligible | n.s. |
| 1a vs 1d | -1.87 | 6 | = 0.383 | -0.81 [-1.25, 0.27] | large | n.s. |
| 1b vs 1c | 1.47 | 6 | = 0.383 | 0.58 [-0.59, 0.68] | medium | n.s. |
| 1b vs 1d | -0.68 | 6 | = 0.623 | -0.30 [-1.05, 0.33] | small | n.s. |
| 1c vs 1d | -1.66 | 6 | = 0.383 | -0.84 [-1.43, 0.14] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 430.97, BIC = 445.63
- **1b vs 1a**: *β* = -0.54, *SE* = 2.324, *z* = -0.231, *p* = 0.817
- **1c vs 1a**: *β* = -2.17, *SE* = 2.319, *z* = -0.933, *p* = 0.351
- **1d vs 1a**: *β* = -1.35, *SE* = 2.349, *z* = -0.575, *p* = 0.565
- **SNR**: *β* = -0.10, *SE* = 0.302, *z* = -0.318, *p* = 0.750

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 0.54 | 2.32 | 0.23 | 0.817 | 0.977 | n.s. |
| 1a - 1c | 2.16 | 2.32 | 0.93 | 0.351 | 0.925 | n.s. |
| 1a - 1d | 1.35 | 2.35 | 0.58 | 0.565 | 0.964 | n.s. |
| 1b - 1c | 1.63 | 2.19 | 0.74 | 0.457 | 0.953 | n.s. |
| 1b - 1d | 0.81 | 2.22 | 0.37 | 0.714 | 0.977 | n.s. |
| 1c - 1d | -0.81 | 2.26 | -0.36 | 0.719 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.928, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.30 | 6 | = 0.929 | 0.16 [-0.61, 0.74] | negligible | n.s. |
| 1a vs 1c | 0.41 | 6 | = 0.929 | 0.14 [-0.51, 1.05] | negligible | n.s. |
| 1a vs 1d | 0.78 | 6 | = 0.929 | 0.29 [-0.47, 0.99] | small | n.s. |
| 1b vs 1c | 0.03 | 6 | = 0.975 | 0.02 [-0.58, 0.69] | negligible | n.s. |
| 1b vs 1d | 0.42 | 6 | = 0.929 | 0.21 [-0.47, 0.89] | small | n.s. |
| 1c vs 1d | 0.31 | 6 | = 0.929 | 0.10 [-0.88, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Latency (50% Fractional Area)

_LMM results not available._

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

#### Amplitude

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
