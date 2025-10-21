# Statistical Analysis Report: tables

**Generated:** 2025-10-20 21:57:46

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
| Increasing Crossover (no 1) | 22 | -3.85 µV | 1.58 | 0.34 | [-7.96, -1.85] |
| Increasing Large (no 1) | 22 | -4.07 µV | 1.79 | 0.38 | [-8.42, -1.27] |
| Increasing Small (no 1) | 22 | -3.28 µV | 1.45 | 0.31 | [-5.76, -0.26] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 22 | 169.53 ms | 8.36 | 1.78 | [153.85, 186.34] |
| Increasing Large (no 1) | 22 | 169.97 ms | 7.93 | 1.69 | [150.14, 185.59] |
| Increasing Small (no 1) | 22 | 170.13 ms | 7.88 | 1.68 | [151.61, 185.99] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 0.96 µV | 1.43 | 0.37 | [-0.04, 5.23] |
| Increasing Large (no 1) | 14 | 1.19 µV | 0.96 | 0.26 | [0.10, 2.50] |
| Increasing Small (no 1) | 11 | 1.91 µV | 1.37 | 0.41 | [0.04, 5.13] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 100.97 ms | 6.58 | 1.70 | [89.74, 111.22] |
| Increasing Large (no 1) | 14 | 99.62 ms | 6.61 | 1.77 | [88.99, 110.81] |
| Increasing Small (no 1) | 11 | 100.17 ms | 4.65 | 1.40 | [93.02, 107.38] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 18 | 3.46 µV | 2.01 | 0.47 | [0.13, 6.48] |
| Increasing Large (no 1) | 15 | 2.90 µV | 2.21 | 0.57 | [0.11, 8.06] |
| Increasing Small (no 1) | 18 | 3.93 µV | 2.94 | 0.69 | [0.09, 9.80] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 18 | 473.70 ms | 12.71 | 3.00 | [439.75, 500.29] |
| Increasing Large (no 1) | 15 | 478.47 ms | 17.46 | 4.51 | [443.23, 506.81] |
| Increasing Small (no 1) | 18 | 472.30 ms | 20.80 | 4.90 | [428.70, 520.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 210.16, BIC = 223.30
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.82, *SE* = 0.270, *z* = -3.046, *p* = 0.002
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.85, *SE* = 0.337, *z* = -2.509, *p* = 0.012
- **SNR**: *β* = -0.23, *SE* = 0.038, *z* = -6.187, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.82 | 0.27 | 3.05 | 0.002 | 0.007 | ** |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.85 | 0.34 | 2.51 | 0.012 | 0.024 | * |
| Increasing Large (no 1) - Increasing Small (no 1) | 0.02 | 0.29 | 0.08 | 0.934 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.51, *p* = 0.095, η²_G = 0.044
- Greenhouse-Geisser corrected: *p* = 0.120 (ε = 0.644)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.31 | 19 | = 0.206 | 0.14 [-0.14, 0.80] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -1.34 | 19 | = 0.206 | -0.38 [-0.77, 0.16] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.81 | 19 | = 0.206 | -0.50 [-0.90, 0.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 435.68, BIC = 448.82
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 1.04, *SE* = 1.324, *z* = 0.785, *p* = 0.432
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 2.72, *SE* = 1.707, *z* = 1.591, *p* = 0.112
- **SNR**: *β* = 0.30, *SE* = 0.198, *z* = 1.537, *p* = 0.124

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -1.04 | 1.32 | -0.79 | 0.432 | 0.432 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -2.72 | 1.71 | -1.59 | 0.112 | 0.299 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.68 | 1.42 | -1.18 | 0.237 | 0.417 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.17, *p* = 0.844, η²_G = 0.001
- Greenhouse-Geisser corrected: *p* = 0.738 (ε = 0.621)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.01 | 19 | = 0.994 | 0.00 [-0.32, 0.59] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.41 | 19 | = 0.994 | -0.07 [-0.66, 0.26] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.44 | 19 | = 0.994 | -0.07 [-0.46, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 103.99, BIC = 114.13
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.67, *SE* = 0.291, *z* = 2.302, *p* = 0.021
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.37, *SE* = 0.309, *z* = 4.439, *p* < .001
- **SNR**: *β* = 0.41, *SE* = 0.053, *z* = 7.790, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.67 | 0.29 | -2.30 | 0.021 | 0.042 | * |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.37 | 0.31 | -4.44 | < .001 | < .001 | *** |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.70 | 0.31 | -2.27 | 0.023 | 0.042 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.957, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.31 | 6 | = 0.917 | 0.12 [-0.91, 0.45] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.11 | 6 | = 0.917 | 0.06 [-0.86, 0.82] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.26 | 6 | = 0.917 | -0.12 [-1.23, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 259.98, BIC = 270.12
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -1.65, *SE* = 1.570, *z* = -1.048, *p* = 0.294
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.30, *SE* = 1.764, *z* = -0.173, *p* = 0.863
- **SNR**: *β* = -0.07, *SE* = 0.321, *z* = -0.215, *p* = 0.830

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 1.65 | 1.57 | 1.05 | 0.294 | 0.649 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.31 | 1.76 | 0.17 | 0.863 | 0.863 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.34 | 1.72 | -0.78 | 0.436 | 0.682 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.864, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -0.25 | 6 | = 0.810 | -0.10 [-0.47, 0.89] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.58 | 6 | = 0.810 | -0.21 [-0.97, 0.71] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.28 | 6 | = 0.810 | -0.13 [-1.13, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 208.15, BIC = 219.74
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.16, *SE* = 0.512, *z* = 0.312, *p* = 0.755
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.39, *SE* = 0.473, *z* = 2.949, *p* = 0.003
- **SNR**: *β* = 0.28, *SE* = 0.071, *z* = 3.980, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.16 | 0.51 | -0.31 | 0.755 | 0.755 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.39 | 0.47 | -2.95 | 0.003 | 0.010 | ** |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.23 | 0.46 | -2.71 | 0.007 | 0.013 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.33, *p* = 0.025, η²_G = 0.077
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 2.13 | 12 | = 0.082 | 0.50 [-0.02, 1.17] | small | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -1.32 | 12 | = 0.211 | -0.24 [-0.90, 0.20] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -2.30 | 12 | = 0.082 | -0.60 [-1.30, 0.02] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 444.38, BIC = 455.97
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 5.18, *SE* = 4.671, *z* = 1.109, *p* = 0.268
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -1.01, *SE* = 5.850, *z* = -0.172, *p* = 0.863
- **SNR**: *β* = 0.13, *SE* = 0.605, *z* = 0.213, *p* = 0.832

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -5.18 | 4.67 | -1.11 | 0.268 | 0.464 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 1.01 | 5.85 | 0.17 | 0.863 | 0.863 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | 6.19 | 3.41 | 1.82 | 0.069 | 0.194 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.355, η²_G = 0.071
- Greenhouse-Geisser corrected: *p* = 0.336 (ε = 0.667)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -1.24 | 12 | = 0.458 | -0.52 [-0.89, 0.24] | medium | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.39 | 12 | = 0.703 | 0.14 [-0.50, 0.56] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 1.07 | 12 | = 0.458 | 0.53 [-0.32, 0.91] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.095)
**P3b amplitude:** Significant main effect of condition (*p* = 0.025) (no significant pairwise comparisons)

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
