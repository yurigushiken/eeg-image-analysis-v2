# Statistical Analysis Report: tables

**Generated:** 2025-10-18 17:02:44

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
| 4 to 1 | 17 | -2.00 µV | 1.58 | 0.38 | [-5.24, -0.25] |
| 5 to 2 | 24 | -4.65 µV | 2.56 | 0.52 | [-9.20, -0.37] |
| 6 to 3 | 24 | -4.12 µV | 2.14 | 0.44 | [-9.59, -0.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 17 | 183.53 ms | 13.27 | 3.22 | [162.61, 200.68] |
| 5 to 2 | 24 | 179.02 ms | 9.35 | 1.91 | [158.91, 196.99] |
| 6 to 3 | 24 | 181.34 ms | 12.14 | 2.48 | [166.10, 217.21] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 16 | 3.98 µV | 2.56 | 0.64 | [1.13, 10.85] |
| 5 to 2 | 15 | 1.98 µV | 1.47 | 0.38 | [0.14, 4.79] |
| 6 to 3 | 13 | 1.57 µV | 1.64 | 0.46 | [0.03, 4.85] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 16 | 115.17 ms | 3.70 | 0.93 | [108.83, 121.15] |
| 5 to 2 | 15 | 113.29 ms | 6.85 | 1.77 | [99.87, 125.15] |
| 6 to 3 | 13 | 110.49 ms | 8.61 | 2.39 | [98.24, 123.19] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 4.32 µV | 2.74 | 0.61 | [0.57, 8.86] |
| 5 to 2 | 17 | 3.62 µV | 2.42 | 0.59 | [0.23, 9.86] |
| 6 to 3 | 19 | 4.12 µV | 2.53 | 0.58 | [1.41, 11.02] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 1 | 20 | 465.83 ms | 21.68 | 4.85 | [439.26, 513.40] |
| 5 to 2 | 17 | 463.07 ms | 25.41 | 6.16 | [405.96, 518.66] |
| 6 to 3 | 19 | 457.76 ms | 23.24 | 5.33 | [402.54, 504.72] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 267.34, BIC = 280.39
- **5 to 2 vs 4 to 1**: *β* = -1.95, *SE* = 0.517, *z* = -3.774, *p* < .001
- **6 to 3 vs 4 to 1**: *β* = -1.49, *SE* = 0.511, *z* = -2.917, *p* = 0.004
- **SNR**: *β* = -0.38, *SE* = 0.081, *z* = -4.643, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 1.95 | 0.52 | 3.77 | < .001 | < .001 | *** |
| 4 to 1 - 6 to 3 | 1.49 | 0.51 | 2.92 | 0.004 | 0.007 | ** |
| 5 to 2 - 6 to 3 | -0.46 | 0.42 | -1.10 | 0.273 | 0.273 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 16.45, *p* < .001, η²_G = 0.316
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.734)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 5.22 | 16 | < .001 | 1.67 [0.58, 1.96] | large | *** |
| 4 to 1 vs 6 to 3 | 3.26 | 16 | = 0.007 | 1.16 [0.20, 1.38] | large | ** |
| 5 to 2 vs 6 to 3 | -2.62 | 16 | = 0.019 | -0.43 [-0.74, 0.13] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 500.62, BIC = 513.67
- **5 to 2 vs 4 to 1**: *β* = -4.09, *SE* = 2.998, *z* = -1.364, *p* = 0.173
- **6 to 3 vs 4 to 1**: *β* = -1.77, *SE* = 2.964, *z* = -0.596, *p* = 0.551
- **SNR**: *β* = -0.02, *SE* = 0.470, *z* = -0.043, *p* = 0.966

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 4.09 | 3.00 | 1.36 | 0.173 | 0.433 | n.s. |
| 4 to 1 - 6 to 3 | 1.77 | 2.96 | 0.60 | 0.551 | 0.572 | n.s. |
| 5 to 2 - 6 to 3 | -2.32 | 2.46 | -0.94 | 0.346 | 0.572 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.502, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.08 | 16 | = 0.616 | 0.32 [-0.26, 0.79] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.51 | 16 | = 0.616 | 0.13 [-0.39, 0.64] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -0.83 | 16 | = 0.616 | -0.16 [-0.66, 0.20] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 164.60, BIC = 175.30
- **5 to 2 vs 4 to 1**: *β* = -0.85, *SE* = 0.491, *z* = -1.730, *p* = 0.084
- **6 to 3 vs 4 to 1**: *β* = -0.91, *SE* = 0.538, *z* = -1.695, *p* = 0.090
- **SNR**: *β* = 0.67, *SE* = 0.108, *z* = 6.225, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.85 | 0.49 | 1.73 | 0.084 | 0.231 | n.s. |
| 4 to 1 - 6 to 3 | 0.91 | 0.54 | 1.70 | 0.090 | 0.231 | n.s. |
| 5 to 2 - 6 to 3 | 0.06 | 0.48 | 0.13 | 0.897 | 0.897 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.64, *p* = 0.028, η²_G = 0.253
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.04 | 7 | = 0.121 | 0.95 [-0.05, 1.46] | large | n.s. |
| 4 to 1 vs 6 to 3 | 2.84 | 7 | = 0.076 | 1.11 [0.01, 1.67] | large | n.s. |
| 5 to 2 vs 6 to 3 | 0.60 | 7 | = 0.565 | 0.29 [-0.51, 0.94] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 297.36, BIC = 308.07
- **5 to 2 vs 4 to 1**: *β* = -2.05, *SE* = 2.181, *z* = -0.939, *p* = 0.348
- **6 to 3 vs 4 to 1**: *β* = -3.72, *SE* = 2.402, *z* = -1.550, *p* = 0.121
- **SNR**: *β* = 0.28, *SE* = 0.512, *z* = 0.554, *p* = 0.580

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 2.05 | 2.18 | 0.94 | 0.348 | 0.575 | n.s. |
| 4 to 1 - 6 to 3 | 3.72 | 2.40 | 1.55 | 0.121 | 0.321 | n.s. |
| 5 to 2 - 6 to 3 | 1.68 | 2.27 | 0.74 | 0.461 | 0.575 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.71, *p* = 0.216, η²_G = 0.131
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 2.55 | 7 | = 0.115 | 1.06 [-0.06, 1.44] | large | n.s. |
| 4 to 1 vs 6 to 3 | 1.58 | 7 | = 0.238 | 0.76 [-0.15, 1.42] | medium | n.s. |
| 5 to 2 vs 6 to 3 | 0.13 | 7 | = 0.899 | 0.07 [-0.82, 0.61] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 239.32, BIC = 251.48
- **5 to 2 vs 4 to 1**: *β* = -0.64, *SE* = 0.491, *z* = -1.296, *p* = 0.195
- **6 to 3 vs 4 to 1**: *β* = 0.08, *SE* = 0.488, *z* = 0.159, *p* = 0.874
- **SNR**: *β* = 0.21, *SE* = 0.054, *z* = 3.860, *p* < .001

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 0.64 | 0.49 | 1.30 | 0.195 | 0.376 | n.s. |
| 4 to 1 - 6 to 3 | -0.08 | 0.49 | -0.16 | 0.874 | 0.874 | n.s. |
| 5 to 2 - 6 to 3 | -0.71 | 0.49 | -1.46 | 0.145 | 0.376 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.380, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.06 | 14 | = 0.463 | 0.27 [-0.22, 0.87] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.09 | 14 | = 0.932 | 0.02 [-0.42, 0.65] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -1.74 | 14 | = 0.309 | -0.27 [-1.03, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 512.78, BIC = 524.93
- **5 to 2 vs 4 to 1**: *β* = -4.31, *SE* = 5.808, *z* = -0.743, *p* = 0.458
- **6 to 3 vs 4 to 1**: *β* = -6.77, *SE* = 5.812, *z* = -1.164, *p* = 0.244
- **SNR**: *β* = -0.57, *SE* = 0.578, *z* = -0.991, *p* = 0.322

_Reference condition: **4 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 1 - 5 to 2 | 4.31 | 5.81 | 0.74 | 0.458 | 0.706 | n.s. |
| 4 to 1 - 6 to 3 | 6.77 | 5.81 | 1.16 | 0.244 | 0.568 | n.s. |
| 5 to 2 - 6 to 3 | 2.45 | 5.93 | 0.41 | 0.679 | 0.706 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.580, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 1 vs 5 to 2 | 1.06 | 14 | = 0.670 | 0.27 [-0.43, 0.64] | small | n.s. |
| 4 to 1 vs 6 to 3 | 0.60 | 14 | = 0.670 | 0.17 [-0.31, 0.77] | negligible | n.s. |
| 5 to 2 vs 6 to 3 | -0.44 | 14 | = 0.670 | -0.12 [-0.71, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 4 to 1 showed greater amplitude than 5 to 2 (*d* = 1.67)
  - 4 to 1 showed greater amplitude than 6 to 3 (*d* = 1.16)
  - 5 to 2 showed smaller amplitude than 6 to 3 (*d* = -0.43)
**P1 amplitude:** Significant main effect of condition (*p* = 0.028) (no significant pairwise comparisons)

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
