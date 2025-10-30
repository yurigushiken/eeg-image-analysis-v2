# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:55:41

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
| Increasing Crossover | 22 | -3.85 µV | 1.68 | 0.36 | [-8.18, -1.37] |
| Increasing Large | 22 | -3.98 µV | 1.75 | 0.37 | [-8.26, -1.29] |
| Increasing Small | 24 | -3.35 µV | 1.52 | 0.31 | [-6.89, -0.13] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 22 | 170.92 ms | 8.71 | 1.86 | [153.84, 189.27] |
| Increasing Large | 22 | 171.16 ms | 8.39 | 1.79 | [149.79, 188.10] |
| Increasing Small | 24 | 172.36 ms | 10.52 | 2.15 | [151.31, 207.36] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 0.91 µV | 1.14 | 0.29 | [0.04, 4.13] |
| Increasing Large | 13 | 1.22 µV | 0.72 | 0.20 | [0.16, 2.43] |
| Increasing Small | 11 | 1.25 µV | 0.85 | 0.26 | [0.27, 2.58] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 97.06 ms | 7.57 | 1.95 | [80.88, 107.41] |
| Increasing Large | 13 | 95.08 ms | 5.93 | 1.65 | [83.29, 103.45] |
| Increasing Small | 11 | 96.77 ms | 4.42 | 1.33 | [87.62, 104.20] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 3.37 µV | 2.19 | 0.50 | [0.18, 7.30] |
| Increasing Large | 15 | 2.91 µV | 2.20 | 0.57 | [0.10, 7.95] |
| Increasing Small | 19 | 3.58 µV | 2.89 | 0.66 | [0.00, 11.60] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 477.85 ms | 12.18 | 2.80 | [459.41, 515.63] |
| Increasing Large | 15 | 480.06 ms | 18.20 | 4.70 | [442.60, 506.38] |
| Increasing Small | 19 | 472.45 ms | 11.53 | 2.65 | [451.47, 501.80] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 204.63, BIC = 217.94
- **Increasing Large vs Increasing Crossover**: *β* = -0.72, *SE* = 0.229, *z* = -3.146, *p* = 0.002
- **Increasing Small vs Increasing Crossover**: *β* = -0.20, *SE* = 0.220, *z* = -0.906, *p* = 0.365
- **SNR**: *β* = -0.17, *SE* = 0.028, *z* = -6.013, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.72 | 0.23 | 3.15 | 0.002 | 0.005 | ** |
| Increasing Crossover - Increasing Small | 0.20 | 0.22 | 0.91 | 0.365 | 0.365 | n.s. |
| Increasing Large - Increasing Small | -0.52 | 0.21 | -2.53 | 0.011 | 0.023 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.308, η²_G = 0.013
- Greenhouse-Geisser corrected: *p* = 0.300 (ε = 0.734)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.83 | 20 | = 0.414 | 0.09 [-0.28, 0.64] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.90 | 20 | = 0.414 | -0.19 [-0.62, 0.27] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.32 | 20 | = 0.414 | -0.28 [-0.75, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 449.63, BIC = 462.95
- **Increasing Large vs Increasing Crossover**: *β* = -0.09, *SE* = 1.158, *z* = -0.078, *p* = 0.938
- **Increasing Small vs Increasing Crossover**: *β* = -0.12, *SE* = 1.111, *z* = -0.113, *p* = 0.910
- **SNR**: *β* = 0.10, *SE* = 0.147, *z* = 0.712, *p* = 0.477

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.09 | 1.16 | 0.08 | 0.938 | 0.999 | n.s. |
| Increasing Crossover - Increasing Small | 0.13 | 1.11 | 0.11 | 0.910 | 0.999 | n.s. |
| Increasing Large - Increasing Small | 0.04 | 1.03 | 0.03 | 0.973 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.86, *p* = 0.432, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.93 | 20 | = 0.534 | 0.09 [-0.26, 0.66] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 1.06 | 20 | = 0.534 | 0.17 [-0.33, 0.55] | negligible | n.s. |
| Increasing Large vs Increasing Small | 0.63 | 20 | = 0.534 | 0.08 [-0.34, 0.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 82.74, BIC = 92.73
- **Increasing Large vs Increasing Crossover**: *β* = 0.51, *SE* = 0.205, *z* = 2.500, *p* = 0.012
- **Increasing Small vs Increasing Crossover**: *β* = 0.40, *SE* = 0.199, *z* = 1.991, *p* = 0.046
- **SNR**: *β* = 0.29, *SE* = 0.051, *z* = 5.629, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.51 | 0.21 | -2.50 | 0.012 | 0.037 | * |
| Increasing Crossover - Increasing Small | -0.40 | 0.20 | -1.99 | 0.046 | 0.091 | n.s. |
| Increasing Large - Increasing Small | 0.12 | 0.21 | 0.55 | 0.584 | 0.584 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.05, *p* = 0.384, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.80 | 5 | = 0.572 | 0.24 [-0.81, 0.73] | small | n.s. |
| Increasing Crossover vs Increasing Small | 1.46 | 5 | = 0.572 | 0.37 [-0.73, 0.70] | small | n.s. |
| Increasing Large vs Increasing Small | 0.60 | 5 | = 0.572 | 0.19 [-0.99, 0.86] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 260.47, BIC = 270.45
- **Increasing Large vs Increasing Crossover**: *β* = -1.59, *SE* = 1.953, *z* = -0.813, *p* = 0.416
- **Increasing Small vs Increasing Crossover**: *β* = -0.14, *SE* = 1.920, *z* = -0.072, *p* = 0.942
- **SNR**: *β* = 0.13, *SE* = 0.489, *z* = 0.270, *p* = 0.788

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.59 | 1.95 | 0.81 | 0.416 | 0.801 | n.s. |
| Increasing Crossover - Increasing Small | 0.14 | 1.92 | 0.07 | 0.942 | 0.942 | n.s. |
| Increasing Large - Increasing Small | -1.45 | 2.06 | -0.70 | 0.483 | 0.801 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.63, *p* = 0.553, η²_G = 0.075
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.26 | 5 | = 0.803 | 0.15 [-0.67, 0.87] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.85 | 5 | = 0.650 | -0.48 [-0.64, 0.80] | small | n.s. |
| Increasing Large vs Increasing Small | -1.27 | 5 | = 0.650 | -0.72 [-1.48, 0.48] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 198.47, BIC = 210.29
- **Increasing Large vs Increasing Crossover**: *β* = 0.78, *SE* = 0.445, *z* = 1.742, *p* = 0.081
- **Increasing Small vs Increasing Crossover**: *β* = 0.75, *SE* = 0.358, *z* = 2.099, *p* = 0.036
- **SNR**: *β* = 0.36, *SE* = 0.051, *z* = 7.113, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.77 | 0.44 | -1.74 | 0.081 | 0.156 | n.s. |
| Increasing Crossover - Increasing Small | -0.75 | 0.36 | -2.10 | 0.036 | 0.104 | n.s. |
| Increasing Large - Increasing Small | 0.02 | 0.42 | 0.06 | 0.953 | 0.953 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.10, *p* = 0.062, η²_G = 0.064
- Greenhouse-Geisser corrected: *p* = 0.091 (ε = 0.618)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 2.51 | 13 | = 0.078 | 0.59 [0.01, 1.21] | medium | n.s. |
| Increasing Crossover vs Increasing Small | -0.26 | 13 | = 0.799 | -0.05 [-0.66, 0.34] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.68 | 13 | = 0.175 | -0.51 [-1.06, 0.16] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 437.25, BIC = 449.07
- **Increasing Large vs Increasing Crossover**: *β* = 3.29, *SE* = 4.715, *z* = 0.697, *p* = 0.486
- **Increasing Small vs Increasing Crossover**: *β* = -5.32, *SE* = 4.032, *z* = -1.320, *p* = 0.187
- **SNR**: *β* = 0.07, *SE* = 0.458, *z* = 0.154, *p* = 0.878

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -3.28 | 4.72 | -0.70 | 0.486 | 0.486 | n.s. |
| Increasing Crossover - Increasing Small | 5.32 | 4.03 | 1.32 | 0.187 | 0.339 | n.s. |
| Increasing Large - Increasing Small | 8.61 | 4.50 | 1.91 | 0.056 | 0.158 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.88, *p* = 0.173, η²_G = 0.076
- Greenhouse-Geisser corrected: *p* = 0.191 (ε = 0.582)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -0.87 | 13 | = 0.402 | -0.33 [-0.84, 0.29] | small | n.s. |
| Increasing Crossover vs Increasing Small | 2.20 | 13 | = 0.140 | 0.47 [-0.08, 0.96] | small | n.s. |
| Increasing Large vs Increasing Small | 1.67 | 13 | = 0.177 | 0.59 [-0.16, 1.05] | medium | n.s. |

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
