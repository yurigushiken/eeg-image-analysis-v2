# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:28:03

---

## 1. Analysis Overview

**Total Measurements:** 192
**Number of Subjects:** 24
**Number of Conditions:** 2

**Components Analyzed:** Fz, N1, P1, P3b
**Dependent Variables:** Latency (Peak), Amplitude (Peak)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** Peak latency within FWHM window
- **Amplitude Measure:** Peak amplitude within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 Fz Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 6 | 110.67 ms | 11.50 | 4.70 | [92.00, 120.00] |
| Increasing 1 to 3 | 17 | 107.06 ms | 11.88 | 2.88 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 6 | 2.42 µV | 0.66 | 0.27 | [1.65, 3.43] |
| Increasing 1 to 3 | 17 | 3.32 µV | 2.54 | 0.62 | [0.49, 9.00] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 19 | 184.84 ms | 18.60 | 4.27 | [156.00, 220.00] |
| Increasing 1 to 3 | 24 | 170.50 ms | 21.52 | 4.39 | [144.00, 220.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 19 | -4.63 µV | 2.43 | 0.56 | [-10.41, -1.40] |
| Increasing 1 to 3 | 24 | -6.60 µV | 2.52 | 0.51 | [-12.65, -2.71] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 22 | 116.73 ms | 10.23 | 2.18 | [100.00, 128.00] |
| Increasing 1 to 3 | 11 | 108.73 ms | 8.55 | 2.58 | [100.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 22 | 3.64 µV | 1.88 | 0.40 | [1.37, 9.14] |
| Increasing 1 to 3 | 11 | 2.97 µV | 1.92 | 0.58 | [0.96, 7.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 20 | 470.00 ms | 31.35 | 7.01 | [400.00, 520.00] |
| Increasing 1 to 3 | 20 | 473.40 ms | 38.24 | 8.55 | [404.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing 3 to 1 | 20 | 5.88 µV | 2.92 | 0.65 | [2.02, 14.34] |
| Increasing 1 to 3 | 20 | 5.93 µV | 3.64 | 0.81 | [1.71, 15.57] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 180.93, BIC = 186.61
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = -2.21, *SE* = 3.393, *z* = -0.651, *p* = 0.515
- **SNR**: *β* = 1.73, *SE* = 1.066, *z* = 1.625, *p* = 0.104

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | 2.21 | 3.39 | 0.65 | 0.515 | 0.515 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.477, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | 0.78 | 4 | = 0.477 | 0.28 [-0.93, 1.63] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 91.13, BIC = 96.80
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = 0.66, *SE* = 0.521, *z* = 1.268, *p* = 0.205
- **SNR**: *β* = 0.75, *SE* = 0.149, *z* = 5.046, *p* < .001

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.66 | 0.52 | -1.27 | 0.205 | 0.205 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.26, *p* = 0.639, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | 0.51 | 4 | = 0.639 | 0.22 [-1.03, 1.48] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 384.32, BIC = 393.12
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = -14.08, *SE* = 5.215, *z* = -2.700, *p* = 0.007
- **SNR**: *β* = -0.64, *SE* = 0.954, *z* = -0.670, *p* = 0.503

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | 14.08 | 5.21 | 2.70 | 0.007 | 0.007 | ** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 14.69, *p* = 0.001, η²_G = 0.187
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | 3.83 | 18 | = 0.001 | 0.94 [0.31, 1.45] | large | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 185.73, BIC = 194.53
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = -0.77, *SE* = 0.567, *z* = -1.356, *p* = 0.175
- **SNR**: *β* = -0.46, *SE* = 0.101, *z* = -4.522, *p* < .001

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.77 | 0.57 | 1.36 | 0.175 | 0.175 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 15.64, *p* < .001, η²_G = 0.189
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | 3.95 | 18 | < .001 | 0.94 [0.33, 1.48] | large | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 251.65, BIC = 259.14
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = -8.01, *SE* = 4.382, *z* = -1.828, *p* = 0.068
- **SNR**: *β* = -0.03, *SE* = 0.755, *z* = -0.036, *p* = 0.971

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | 8.01 | 4.38 | 1.83 | 0.068 | 0.068 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.86, *p* = 0.019, η²_G = 0.309
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | 2.80 | 10 | = 0.019 | 1.27 [0.06, 1.63] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 124.61, BIC = 132.09
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = -0.58, *SE* = 0.453, *z* = -1.289, *p* = 0.197
- **SNR**: *β* = 0.40, *SE* = 0.084, *z* = 4.758, *p* < .001

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | 0.58 | 0.45 | 1.29 | 0.197 | 0.197 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.98, *p* = 0.074, η²_G = 0.111
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | 1.99 | 10 | = 0.074 | 0.67 [-0.13, 1.33] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 405.77, BIC = 414.21
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = 3.04, *SE* = 11.006, *z* = 0.276, *p* = 0.782
- **SNR**: *β* = -0.21, *SE* = 1.143, *z* = -0.180, *p* = 0.857

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | -3.04 | 11.01 | -0.28 | 0.782 | 0.782 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.19, *p* = 0.670, η²_G = 0.006
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.43 | 17 | = 0.670 | -0.15 [-0.60, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 200.38, BIC = 208.82
- **Increasing 1 to 3 vs Decreasing 3 to 1**: *β* = 0.60, *SE* = 0.712, *z* = 0.850, *p* = 0.395
- **SNR**: *β* = 0.30, *SE* = 0.077, *z* = 3.851, *p* < .001

_Reference condition: **Decreasing 3 to 1** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing 3 to 1 - Increasing 1 to 3 | -0.61 | 0.71 | -0.85 | 0.395 | 0.395 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.854, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing 3 to 1 vs Increasing 1 to 3 | -0.19 | 17 | = 0.854 | -0.05 [-0.54, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.001). Post-hoc tests revealed:
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 3 (*d* = 0.94)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Decreasing 3 to 1 showed greater amplitude than Increasing 1 to 3 (*d* = 0.94)
**P1 latency:** Significant main effect of condition (*p* = 0.019). Post-hoc tests revealed:
  - Decreasing 3 to 1 showed greater latency than Increasing 1 to 3 (*d* = 1.27)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.074)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 Fz Component

#### Latency

#### Amplitude

### 5.2 N1 Component

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

### 5.3 P1 Component

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

### 5.4 P3b Component

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
