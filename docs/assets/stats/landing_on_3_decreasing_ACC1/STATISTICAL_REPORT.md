# Statistical Analysis Report: tables

**Generated:** 2025-10-30 18:25:21

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
| 4 to 3 | 23 | -3.78 µV | 1.84 | 0.38 | [-8.01, -0.64] |
| 5 to 3 | 24 | -3.42 µV | 2.26 | 0.46 | [-8.30, -0.20] |
| 6 to 3 | 23 | -4.15 µV | 2.05 | 0.43 | [-9.49, -0.82] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | 176.52 ms | 12.73 | 2.66 | [153.98, 210.92] |
| 5 to 3 | 24 | 177.19 ms | 13.54 | 2.76 | [149.19, 216.16] |
| 6 to 3 | 23 | 177.82 ms | 11.17 | 2.33 | [162.68, 208.58] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 1.61 µV | 1.28 | 0.37 | [0.16, 4.63] |
| 5 to 3 | 16 | 2.12 µV | 1.13 | 0.28 | [0.44, 3.80] |
| 6 to 3 | 14 | 1.72 µV | 1.84 | 0.49 | [0.07, 6.32] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 107.07 ms | 4.98 | 1.44 | [97.03, 115.73] |
| 5 to 3 | 16 | 109.44 ms | 2.71 | 0.68 | [105.56, 114.90] |
| 6 to 3 | 14 | 108.84 ms | 6.26 | 1.67 | [97.43, 118.94] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 20 | 3.77 µV | 2.75 | 0.61 | [0.11, 9.18] |
| 5 to 3 | 19 | 3.63 µV | 1.86 | 0.43 | [0.37, 7.76] |
| 6 to 3 | 19 | 4.29 µV | 2.78 | 0.64 | [0.50, 11.72] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 20 | 474.69 ms | 21.74 | 4.86 | [423.11, 529.59] |
| 5 to 3 | 19 | 465.98 ms | 21.21 | 4.87 | [418.41, 491.72] |
| 6 to 3 | 19 | 467.91 ms | 19.04 | 4.37 | [421.90, 507.55] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 265.77, BIC = 279.26
- **5 to 3 vs 4 to 3**: *β* = 0.29, *SE* = 0.354, *z* = 0.826, *p* = 0.409
- **6 to 3 vs 4 to 3**: *β* = -0.17, *SE* = 0.359, *z* = -0.481, *p* = 0.630
- **SNR**: *β* = -0.34, *SE* = 0.066, *z* = -5.222, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.29 | 0.35 | -0.83 | 0.409 | 0.650 | n.s. |
| 4 to 3 - 6 to 3 | 0.17 | 0.36 | 0.48 | 0.630 | 0.650 | n.s. |
| 5 to 3 - 6 to 3 | 0.46 | 0.36 | 1.31 | 0.190 | 0.469 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.46, *p* = 0.243, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -1.06 | 21 | = 0.455 | -0.20 [-0.69, 0.19] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.73 | 21 | = 0.471 | 0.16 [-0.29, 0.60] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 1.60 | 21 | = 0.376 | 0.34 [-0.17, 0.72] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 512.87, BIC = 526.36
- **5 to 3 vs 4 to 3**: *β* = 1.09, *SE* = 1.617, *z* = 0.677, *p* = 0.498
- **6 to 3 vs 4 to 3**: *β* = 3.11, *SE* = 1.645, *z* = 1.891, *p* = 0.059
- **SNR**: *β* = 0.11, *SE* = 0.310, *z* = 0.357, *p* = 0.721

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -1.10 | 1.62 | -0.68 | 0.498 | 0.498 | n.s. |
| 4 to 3 - 6 to 3 | -3.11 | 1.64 | -1.89 | 0.059 | 0.166 | n.s. |
| 5 to 3 - 6 to 3 | -2.02 | 1.62 | -1.24 | 0.215 | 0.383 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.32, *p* = 0.111, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.43 | 21 | = 0.674 | -0.07 [-0.55, 0.32] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -2.65 | 21 | = 0.045 | -0.32 [-1.04, -0.09] | small | * |
| 5 to 3 vs 6 to 3 | -1.35 | 21 | = 0.289 | -0.25 [-0.68, 0.20] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 122.54, BIC = 132.96
- **5 to 3 vs 4 to 3**: *β* = 0.03, *SE* = 0.357, *z* = 0.079, *p* = 0.937
- **6 to 3 vs 4 to 3**: *β* = 0.40, *SE* = 0.357, *z* = 1.123, *p* = 0.261
- **SNR**: *β* = 0.59, *SE* = 0.083, *z* = 7.062, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.03 | 0.36 | -0.08 | 0.937 | 0.937 | n.s. |
| 4 to 3 - 6 to 3 | -0.40 | 0.36 | -1.12 | 0.261 | 0.597 | n.s. |
| 5 to 3 - 6 to 3 | -0.37 | 0.35 | -1.05 | 0.293 | 0.597 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.31, *p* = 0.741, η²_G = 0.022
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.84 | 5 | = 0.707 | -0.21 [-1.43, 0.24] | small | n.s. |
| 4 to 3 vs 6 to 3 | 0.23 | 5 | = 0.831 | 0.11 [-0.88, 0.79] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.78 | 5 | = 0.707 | 0.36 [-0.25, 1.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 250.88, BIC = 261.31
- **5 to 3 vs 4 to 3**: *β* = 2.40, *SE* = 1.343, *z* = 1.787, *p* = 0.074
- **6 to 3 vs 4 to 3**: *β* = 1.42, *SE* = 1.374, *z* = 1.030, *p* = 0.303
- **SNR**: *β* = -0.40, *SE* = 0.390, *z* = -1.014, *p* = 0.310

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -2.40 | 1.34 | -1.79 | 0.074 | 0.206 | n.s. |
| 4 to 3 - 6 to 3 | -1.41 | 1.37 | -1.03 | 0.303 | 0.514 | n.s. |
| 5 to 3 - 6 to 3 | 0.98 | 1.35 | 0.73 | 0.466 | 0.514 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.23, *p* = 0.798, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.82 | 5 | = 0.836 | -0.36 [-1.31, 0.32] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.42 | 5 | = 0.836 | -0.14 [-1.09, 0.60] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 0.22 | 5 | = 0.836 | 0.10 [-0.70, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 236.31, BIC = 248.67
- **5 to 3 vs 4 to 3**: *β* = -0.09, *SE* = 0.468, *z* = -0.182, *p* = 0.855
- **6 to 3 vs 4 to 3**: *β* = 0.40, *SE* = 0.463, *z* = 0.873, *p* = 0.383
- **SNR**: *β* = 0.42, *SE* = 0.067, *z* = 6.268, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.09 | 0.47 | 0.18 | 0.855 | 0.855 | n.s. |
| 4 to 3 - 6 to 3 | -0.40 | 0.46 | -0.87 | 0.383 | 0.649 | n.s. |
| 5 to 3 - 6 to 3 | -0.49 | 0.47 | -1.05 | 0.294 | 0.649 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.65, *p* = 0.529, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.66 | 16 | = 0.635 | 0.18 [-0.36, 0.68] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.48 | 16 | = 0.635 | -0.09 [-0.58, 0.42] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -1.07 | 16 | = 0.635 | -0.28 [-0.78, 0.24] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 516.07, BIC = 528.43
- **5 to 3 vs 4 to 3**: *β* = -9.89, *SE* = 5.017, *z* = -1.972, *p* = 0.049
- **6 to 3 vs 4 to 3**: *β* = -7.13, *SE* = 4.944, *z* = -1.441, *p* = 0.150
- **SNR**: *β* = 0.10, *SE* = 0.725, *z* = 0.133, *p* = 0.894

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 9.89 | 5.02 | 1.97 | 0.049 | 0.139 | n.s. |
| 4 to 3 - 6 to 3 | 7.13 | 4.94 | 1.44 | 0.150 | 0.277 | n.s. |
| 5 to 3 - 6 to 3 | -2.77 | 5.00 | -0.55 | 0.580 | 0.580 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.135, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 1.90 | 16 | = 0.226 | 0.52 [-0.08, 1.00] | medium | n.s. |
| 4 to 3 vs 6 to 3 | 1.42 | 16 | = 0.264 | 0.34 [-0.16, 0.86] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.75 | 16 | = 0.463 | -0.21 [-0.67, 0.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


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
