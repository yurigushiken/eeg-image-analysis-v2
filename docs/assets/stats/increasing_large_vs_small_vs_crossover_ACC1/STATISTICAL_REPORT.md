# Statistical Analysis Report: tables

**Generated:** 2025-10-23 18:57:21

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
| Increasing Crossover | 23 | -3.78 µV | 1.89 | 0.39 | [-8.17, -0.22] |
| Increasing Large | 22 | -4.35 µV | 2.29 | 0.49 | [-10.54, -2.20] |
| Increasing Small | 23 | -3.40 µV | 1.44 | 0.30 | [-6.17, -0.12] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 23 | 172.89 ms | 11.86 | 2.47 | [152.58, 206.00] |
| Increasing Large | 22 | 169.74 ms | 9.31 | 1.98 | [150.97, 186.52] |
| Increasing Small | 23 | 172.54 ms | 11.44 | 2.38 | [151.42, 207.50] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 0.98 µV | 1.12 | 0.29 | [0.03, 3.87] |
| Increasing Large | 14 | 1.65 µV | 1.44 | 0.38 | [-0.07, 4.22] |
| Increasing Small | 12 | 1.34 µV | 0.86 | 0.25 | [0.09, 2.58] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 15 | 95.55 ms | 7.46 | 1.93 | [81.52, 106.23] |
| Increasing Large | 14 | 93.43 ms | 7.82 | 2.09 | [80.26, 107.91] |
| Increasing Small | 12 | 95.01 ms | 5.44 | 1.57 | [81.34, 102.03] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 3.51 µV | 2.19 | 0.50 | [0.32, 7.83] |
| Increasing Large | 15 | 4.02 µV | 2.22 | 0.57 | [0.41, 8.48] |
| Increasing Small | 20 | 3.46 µV | 2.97 | 0.66 | [0.11, 11.22] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 19 | 483.34 ms | 10.69 | 2.45 | [457.98, 508.20] |
| Increasing Large | 15 | 484.22 ms | 17.45 | 4.50 | [443.08, 505.59] |
| Increasing Small | 20 | 475.38 ms | 17.18 | 3.84 | [441.84, 505.88] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 230.17, BIC = 243.48
- **Increasing Large vs Increasing Crossover**: *β* = -1.21, *SE* = 0.308, *z* = -3.939, *p* < .001
- **Increasing Small vs Increasing Crossover**: *β* = -0.43, *SE* = 0.305, *z* = -1.421, *p* = 0.155
- **SNR**: *β* = -0.21, *SE* = 0.033, *z* = -6.437, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.21 | 0.31 | 3.94 | < .001 | < .001 | *** |
| Increasing Crossover - Increasing Small | 0.43 | 0.30 | 1.42 | 0.155 | 0.155 | n.s. |
| Increasing Large - Increasing Small | -0.78 | 0.29 | -2.73 | 0.006 | 0.012 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.73, *p* = 0.192, η²_G = 0.025
- Greenhouse-Geisser corrected: *p* = 0.202 (ε = 0.674)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.83 | 19 | = 0.419 | 0.11 [-0.18, 0.74] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -1.36 | 19 | = 0.282 | -0.32 [-0.72, 0.18] | small | n.s. |
| Increasing Large vs Increasing Small | -1.41 | 19 | = 0.282 | -0.36 [-0.81, 0.13] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 467.91, BIC = 481.22
- **Increasing Large vs Increasing Crossover**: *β* = -1.72, *SE* = 1.332, *z* = -1.291, *p* = 0.197
- **Increasing Small vs Increasing Crossover**: *β* = 0.59, *SE* = 1.317, *z* = 0.449, *p* = 0.653
- **SNR**: *β* = 0.24, *SE* = 0.153, *z* = 1.567, *p* = 0.117

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.72 | 1.33 | 1.29 | 0.197 | 0.355 | n.s. |
| Increasing Crossover - Increasing Small | -0.59 | 1.32 | -0.45 | 0.653 | 0.653 | n.s. |
| Increasing Large - Increasing Small | -2.31 | 1.21 | -1.90 | 0.057 | 0.162 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.32, *p* = 0.279, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.273 (ε = 0.670)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 2.01 | 19 | = 0.177 | 0.21 [0.00, 0.96] | small | n.s. |
| Increasing Crossover vs Increasing Small | 0.98 | 19 | = 0.508 | 0.11 [-0.41, 0.47] | negligible | n.s. |
| Increasing Large vs Increasing Small | -0.64 | 19 | = 0.528 | -0.11 [-0.68, 0.24] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 103.52, BIC = 113.80
- **Increasing Large vs Increasing Crossover**: *β* = 1.02, *SE* = 0.230, *z* = 4.433, *p* < .001
- **Increasing Small vs Increasing Crossover**: *β* = 0.56, *SE* = 0.222, *z* = 2.506, *p* = 0.012
- **SNR**: *β* = 0.34, *SE* = 0.063, *z* = 5.368, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -1.02 | 0.23 | -4.43 | < .001 | < .001 | *** |
| Increasing Crossover - Increasing Small | -0.56 | 0.22 | -2.51 | 0.012 | 0.024 | * |
| Increasing Large - Increasing Small | 0.46 | 0.24 | 1.93 | 0.053 | 0.053 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.28, *p* = 0.080, η²_G = 0.068
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -0.86 | 5 | = 0.429 | -0.16 [-1.52, 0.18] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 2.30 | 5 | = 0.163 | 0.44 [-0.83, 0.52] | small | n.s. |
| Increasing Large vs Increasing Small | 1.95 | 5 | = 0.163 | 0.61 [-0.49, 1.47] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 282.27, BIC = 292.56
- **Increasing Large vs Increasing Crossover**: *β* = -1.83, *SE* = 2.260, *z* = -0.809, *p* = 0.419
- **Increasing Small vs Increasing Crossover**: *β* = -0.25, *SE* = 2.226, *z* = -0.112, *p* = 0.911
- **SNR**: *β* = 0.79, *SE* = 0.529, *z* = 1.491, *p* = 0.136

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.83 | 2.26 | 0.81 | 0.419 | 0.804 | n.s. |
| Increasing Crossover - Increasing Small | 0.25 | 2.23 | 0.11 | 0.911 | 0.911 | n.s. |
| Increasing Large - Increasing Small | -1.58 | 2.35 | -0.67 | 0.502 | 0.804 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.76, *p* = 0.493, η²_G = 0.099
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.26 | 5 | = 0.667 | 0.80 [-0.32, 1.30] | medium | n.s. |
| Increasing Crossover vs Increasing Small | 0.33 | 5 | = 0.755 | 0.18 [-0.55, 0.80] | negligible | n.s. |
| Increasing Large vs Increasing Small | -0.83 | 5 | = 0.667 | -0.52 [-1.13, 0.74] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 211.74, BIC = 223.68
- **Increasing Large vs Increasing Crossover**: *β* = 0.80, *SE* = 0.416, *z* = 1.926, *p* = 0.054
- **Increasing Small vs Increasing Crossover**: *β* = 0.20, *SE* = 0.355, *z* = 0.556, *p* = 0.579
- **SNR**: *β* = 0.24, *SE* = 0.047, *z* = 5.088, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.80 | 0.42 | -1.93 | 0.054 | 0.154 | n.s. |
| Increasing Crossover - Increasing Small | -0.20 | 0.36 | -0.56 | 0.579 | 0.579 | n.s. |
| Increasing Large - Increasing Small | 0.60 | 0.42 | 1.45 | 0.148 | 0.275 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.13, *p* = 0.883, η²_G = 0.002
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.56 | 13 | = 0.876 | 0.13 [-0.45, 0.66] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 0.16 | 13 | = 0.876 | 0.03 [-0.62, 0.38] | negligible | n.s. |
| Increasing Large vs Increasing Small | -0.28 | 13 | = 0.876 | -0.07 [-0.65, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 442.11, BIC = 454.05
- **Increasing Large vs Increasing Crossover**: *β* = 3.70, *SE* = 3.679, *z* = 1.006, *p* = 0.314
- **Increasing Small vs Increasing Crossover**: *β* = -5.91, *SE* = 3.258, *z* = -1.815, *p* = 0.070
- **SNR**: *β* = 0.55, *SE* = 0.387, *z* = 1.411, *p* = 0.158

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -3.70 | 3.68 | -1.01 | 0.314 | 0.314 | n.s. |
| Increasing Crossover - Increasing Small | 5.91 | 3.26 | 1.81 | 0.070 | 0.134 | n.s. |
| Increasing Large - Increasing Small | 9.61 | 3.68 | 2.61 | 0.009 | 0.027 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.36, *p* = 0.051, η²_G = 0.075
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -0.23 | 13 | = 0.825 | -0.08 [-0.62, 0.49] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 2.58 | 13 | = 0.034 | 0.65 [-0.15, 0.87] | medium | * |
| Increasing Large vs Increasing Small | 2.78 | 13 | = 0.034 | 0.53 [0.09, 1.40] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.080)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.051)

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
