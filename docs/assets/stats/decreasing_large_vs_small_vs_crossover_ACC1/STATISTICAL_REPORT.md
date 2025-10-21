# Statistical Analysis Report: tables

**Generated:** 2025-10-20 21:50:04

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
| Decreasing Crossover | 24 | -3.75 µV | 1.62 | 0.33 | [-7.36, -0.84] |
| Decreasing Large | 24 | -3.71 µV | 1.86 | 0.38 | [-8.30, -0.97] |
| Decreasing Small | 21 | -2.73 µV | 2.11 | 0.46 | [-7.35, 0.06] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 177.59 ms | 7.74 | 1.58 | [165.21, 202.38] |
| Decreasing Large | 24 | 177.64 ms | 9.19 | 1.88 | [162.95, 200.04] |
| Decreasing Small | 21 | 177.64 ms | 9.19 | 2.01 | [162.08, 199.08] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 15 | 1.73 µV | 1.32 | 0.34 | [0.05, 4.63] |
| Decreasing Large | 14 | 2.13 µV | 1.31 | 0.35 | [0.11, 4.25] |
| Decreasing Small | 19 | 1.84 µV | 1.63 | 0.37 | [-0.06, 6.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 15 | 113.09 ms | 4.62 | 1.19 | [104.02, 123.07] |
| Decreasing Large | 14 | 113.04 ms | 2.80 | 0.75 | [108.26, 117.50] |
| Decreasing Small | 19 | 113.62 ms | 3.81 | 0.87 | [102.76, 118.08] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 21 | 3.50 µV | 2.49 | 0.54 | [0.10, 9.21] |
| Decreasing Large | 19 | 3.22 µV | 2.08 | 0.48 | [0.45, 7.08] |
| Decreasing Small | 20 | 4.01 µV | 2.46 | 0.55 | [1.05, 8.63] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 21 | 482.40 ms | 10.81 | 2.36 | [455.45, 497.35] |
| Decreasing Large | 19 | 490.10 ms | 18.95 | 4.35 | [447.40, 529.16] |
| Decreasing Small | 20 | 486.58 ms | 11.43 | 2.56 | [458.13, 500.67] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 251.13, BIC = 264.53
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.66, *SE* = 0.354, *z* = -1.856, *p* = 0.063
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.21, *SE* = 0.388, *z* = 0.537, *p* = 0.592
- **SNR**: *β* = -0.15, *SE* = 0.032, *z* = -4.815, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.66 | 0.35 | 1.86 | 0.063 | 0.123 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.21 | 0.39 | -0.54 | 0.592 | 0.592 | n.s. |
| Decreasing Large - Decreasing Small | -0.87 | 0.34 | -2.54 | 0.011 | 0.033 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.77, *p* = 0.006, η²_G = 0.081
- Greenhouse-Geisser corrected: *p* = 0.017 (ε = 0.647)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -0.30 | 20 | = 0.769 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -3.10 | 20 | = 0.017 | -0.63 [-1.18, -0.17] | medium | * |
| Decreasing Large vs Decreasing Small | -2.21 | 20 | = 0.058 | -0.56 [-0.96, -0.00] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 450.10, BIC = 463.50
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.69, *SE* = 1.191, *z* = -0.579, *p* = 0.563
- **Decreasing Small vs Decreasing Crossover**: *β* = -0.39, *SE* = 1.325, *z* = -0.293, *p* = 0.769
- **SNR**: *β* = -0.16, *SE* = 0.115, *z* = -1.413, *p* = 0.158

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.69 | 1.19 | 0.58 | 0.563 | 0.916 | n.s. |
| Decreasing Crossover - Decreasing Small | 0.39 | 1.32 | 0.29 | 0.769 | 0.947 | n.s. |
| Decreasing Large - Decreasing Small | -0.30 | 1.14 | -0.27 | 0.791 | 0.947 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.19, *p* = 0.825, η²_G = 0.001
- Greenhouse-Geisser corrected: *p* = 0.751 (ε = 0.715)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -0.06 | 20 | = 0.952 | -0.01 [-0.44, 0.41] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.63 | 20 | = 0.952 | -0.08 [-0.60, 0.32] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -0.40 | 20 | = 0.952 | -0.07 [-0.54, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 141.69, BIC = 152.92
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.60, *SE* = 0.280, *z* = 2.136, *p* = 0.033
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.51, *SE* = 0.259, *z* = 1.985, *p* = 0.047
- **SNR**: *β* = 0.23, *SE* = 0.060, *z* = 3.849, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.60 | 0.28 | -2.14 | 0.033 | 0.095 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.51 | 0.26 | -1.98 | 0.047 | 0.095 | n.s. |
| Decreasing Large - Decreasing Small | 0.09 | 0.26 | 0.32 | 0.746 | 0.746 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.27, *p* = 0.303, η²_G = 0.027
- Greenhouse-Geisser corrected: *p* = 0.294 (ε = 0.626)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.91 | 10 | = 0.202 | -0.35 [-1.30, 0.15] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.63 | 10 | = 0.202 | -0.33 [-1.09, 0.13] | small | n.s. |
| Decreasing Large vs Decreasing Small | -0.14 | 10 | = 0.894 | -0.04 [-0.60, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 270.02, BIC = 281.25
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.24, *SE* = 1.172, *z* = -0.201, *p* = 0.841
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.71, *SE* = 1.096, *z* = 0.652, *p* = 0.514
- **SNR**: *β* = -0.10, *SE* = 0.189, *z* = -0.531, *p* = 0.595

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.24 | 1.17 | 0.20 | 0.841 | 0.841 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.71 | 1.10 | -0.65 | 0.514 | 0.777 | n.s. |
| Decreasing Large - Decreasing Small | -0.95 | 1.11 | -0.85 | 0.393 | 0.777 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.145, η²_G = 0.060
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 2.04 | 10 | = 0.156 | 0.47 [-0.12, 1.35] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | 0.04 | 10 | = 0.966 | 0.01 [-0.96, 0.24] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.79 | 10 | = 0.156 | -0.57 [-0.78, 0.44] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 231.84, BIC = 244.40
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.42, *SE* = 0.395, *z* = 1.074, *p* = 0.283
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.99, *SE* = 0.361, *z* = 2.756, *p* = 0.006
- **SNR**: *β* = 0.17, *SE* = 0.030, *z* = 5.636, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.42 | 0.39 | -1.07 | 0.283 | 0.283 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.99 | 0.36 | -2.76 | 0.006 | 0.017 | * |
| Decreasing Large - Decreasing Small | -0.57 | 0.36 | -1.57 | 0.117 | 0.221 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.95, *p* = 0.158, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.20 | 17 | = 0.357 | 0.26 [-0.22, 0.79] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.95 | 17 | = 0.357 | -0.14 [-0.72, 0.23] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -1.66 | 17 | = 0.344 | -0.40 [-0.91, 0.12] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 486.05, BIC = 498.61
- **Decreasing Large vs Decreasing Crossover**: *β* = 8.57, *SE* = 3.581, *z* = 2.395, *p* = 0.017
- **Decreasing Small vs Decreasing Crossover**: *β* = 4.92, *SE* = 3.322, *z* = 1.482, *p* = 0.138
- **SNR**: *β* = 0.12, *SE* = 0.255, *z* = 0.474, *p* = 0.636

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -8.58 | 3.58 | -2.39 | 0.017 | 0.049 | * |
| Decreasing Crossover - Decreasing Small | -4.93 | 3.32 | -1.48 | 0.138 | 0.257 | n.s. |
| Decreasing Large - Decreasing Small | 3.65 | 3.37 | 1.08 | 0.279 | 0.279 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.11, *p* = 0.136, η²_G = 0.042
- Greenhouse-Geisser corrected: *p* = 0.154 (ε = 0.691)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -2.19 | 17 | = 0.129 | -0.46 [-1.04, 0.01] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.32 | 17 | = 0.309 | -0.29 [-0.93, 0.05] | small | n.s. |
| Decreasing Large vs Decreasing Small | 0.89 | 17 | = 0.387 | 0.25 [-0.29, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.006). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller amplitude than Decreasing Small (*d* = -0.63)

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
