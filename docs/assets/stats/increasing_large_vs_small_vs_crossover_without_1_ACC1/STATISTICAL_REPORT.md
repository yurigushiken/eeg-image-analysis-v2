# Statistical Analysis Report: tables

**Generated:** 2025-10-30 17:56:03

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
| Increasing Crossover (no 1) | 23 | -3.71 µV | 1.72 | 0.36 | [-7.84, -0.43] |
| Increasing Large (no 1) | 22 | -4.35 µV | 2.29 | 0.49 | [-10.54, -2.20] |
| Increasing Small (no 1) | 21 | -3.35 µV | 1.36 | 0.30 | [-5.70, -0.81] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 23 | 172.35 ms | 11.90 | 2.48 | [152.31, 204.66] |
| Increasing Large (no 1) | 22 | 169.74 ms | 9.31 | 1.98 | [150.97, 186.52] |
| Increasing Small (no 1) | 21 | 171.07 ms | 9.22 | 2.01 | [151.68, 195.11] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 0.92 µV | 1.34 | 0.35 | [0.02, 4.72] |
| Increasing Large (no 1) | 13 | 1.80 µV | 1.45 | 0.40 | [0.21, 4.39] |
| Increasing Small (no 1) | 12 | 1.91 µV | 1.35 | 0.39 | [0.05, 4.56] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 15 | 99.67 ms | 8.15 | 2.10 | [82.74, 110.18] |
| Increasing Large (no 1) | 13 | 98.29 ms | 7.69 | 2.13 | [83.07, 110.35] |
| Increasing Small (no 1) | 12 | 98.24 ms | 5.07 | 1.46 | [89.58, 106.20] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 20 | 3.23 µV | 2.18 | 0.49 | [-0.02, 6.93] |
| Increasing Large (no 1) | 15 | 3.97 µV | 2.20 | 0.57 | [0.66, 8.71] |
| Increasing Small (no 1) | 19 | 3.98 µV | 2.96 | 0.68 | [-0.01, 9.90] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover (no 1) | 20 | 480.85 ms | 17.19 | 3.84 | [446.53, 527.71] |
| Increasing Large (no 1) | 15 | 479.85 ms | 15.01 | 3.88 | [449.94, 503.32] |
| Increasing Small (no 1) | 19 | 469.41 ms | 18.10 | 4.15 | [425.64, 519.73] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 224.82, BIC = 237.96
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -1.19, *SE* = 0.328, *z* = -3.616, *p* < .001
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -0.93, *SE* = 0.370, *z* = -2.521, *p* = 0.012
- **SNR**: *β* = -0.27, *SE* = 0.036, *z* = -7.408, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 1.18 | 0.33 | 3.62 | < .001 | < .001 | *** |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 0.93 | 0.37 | 2.52 | 0.012 | 0.023 | * |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.25 | 0.34 | -0.74 | 0.456 | 0.456 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.78, *p* = 0.075, η²_G = 0.053
- Greenhouse-Geisser corrected: *p* = 0.104 (ε = 0.602)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.31 | 19 | = 0.206 | 0.17 [-0.10, 0.84] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -1.63 | 19 | = 0.178 | -0.46 [-0.84, 0.10] | small | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -1.75 | 19 | = 0.178 | -0.52 [-0.88, 0.09] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 463.22, BIC = 476.36
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -0.62, *SE* = 1.432, *z* = -0.431, *p* = 0.666
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 3.30, *SE* = 1.704, *z* = 1.936, *p* = 0.053
- **SNR**: *β* = 0.49, *SE* = 0.186, *z* = 2.632, *p* = 0.008

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 0.62 | 1.43 | 0.43 | 0.666 | 0.666 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -3.30 | 1.70 | -1.94 | 0.053 | 0.103 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -3.92 | 1.49 | -2.63 | 0.008 | 0.025 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.414, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.369 (ε = 0.589)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.77 | 19 | = 0.278 | 0.16 [-0.04, 0.92] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.26 | 19 | = 0.801 | -0.04 [-0.64, 0.28] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.95 | 19 | = 0.530 | -0.18 [-0.69, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 113.70, BIC = 123.84
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 1.02, *SE* = 0.329, *z* = 3.095, *p* = 0.002
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.27, *SE* = 0.331, *z* = 3.840, *p* < .001
- **SNR**: *β* = 0.51, *SE* = 0.072, *z* = 7.087, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -1.02 | 0.33 | -3.09 | 0.002 | 0.004 | ** |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.27 | 0.33 | -3.84 | < .001 | < .001 | *** |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.25 | 0.35 | -0.72 | 0.472 | 0.472 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.392, η²_G = 0.131
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.29 | 3 | = 0.788 | 0.07 [-1.37, 0.28] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 1.09 | 3 | = 0.535 | 0.82 [-1.08, 0.61] | large | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | 1.09 | 3 | = 0.535 | 0.82 [-0.54, 1.75] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.84, BIC = 285.97
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = -3.83, *SE* = 2.103, *z* = -1.824, *p* = 0.068
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -2.40, *SE* = 2.098, *z* = -1.145, *p* = 0.252
- **SNR**: *β* = -0.34, *SE* = 0.484, *z* = -0.695, *p* = 0.487

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | 3.83 | 2.10 | 1.82 | 0.068 | 0.191 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 2.40 | 2.10 | 1.15 | 0.252 | 0.441 | n.s. |
| Increasing Large (no 1) - Increasing Small (no 1) | -1.43 | 2.20 | -0.65 | 0.515 | 0.515 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.59, *p* = 0.585, η²_G = 0.093
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 1.97 | 3 | = 0.430 | 0.51 [0.08, 1.98] | medium | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 0.04 | 3 | = 0.968 | 0.04 [-0.65, 1.04] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.69 | 3 | = 0.813 | -0.56 [-1.39, 0.76] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 225.55, BIC = 237.48
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.84, *SE* = 0.493, *z* = 1.697, *p* = 0.090
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = 1.29, *SE* = 0.466, *z* = 2.766, *p* = 0.006
- **SNR**: *β* = 0.29, *SE* = 0.068, *z* = 4.310, *p* < .001

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.84 | 0.49 | -1.70 | 0.090 | 0.171 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | -1.29 | 0.47 | -2.77 | 0.006 | 0.017 | * |
| Increasing Large (no 1) - Increasing Small (no 1) | -0.45 | 0.48 | -0.94 | 0.346 | 0.346 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.19, *p* = 0.826, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | 0.48 | 13 | = 0.813 | 0.11 [-0.48, 0.63] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | -0.24 | 13 | = 0.813 | -0.05 [-0.73, 0.28] | negligible | n.s. |
| Increasing Large (no 1) vs Increasing Small (no 1) | -0.51 | 13 | = 0.813 | -0.13 [-0.72, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 465.03, BIC = 476.96
- **Increasing Large (no 1) vs Increasing Crossover (no 1)**: *β* = 0.16, *SE* = 4.954, *z* = 0.033, *p* = 0.974
- **Increasing Small (no 1) vs Increasing Crossover (no 1)**: *β* = -11.34, *SE* = 4.673, *z* = -2.427, *p* = 0.015
- **SNR**: *β* = -0.33, *SE* = 0.603, *z* = -0.538, *p* = 0.591

_Reference condition: **Increasing Crossover (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover (no 1) - Increasing Large (no 1) | -0.16 | 4.95 | -0.03 | 0.974 | 0.974 | n.s. |
| Increasing Crossover (no 1) - Increasing Small (no 1) | 11.34 | 4.67 | 2.43 | 0.015 | 0.045 | * |
| Increasing Large (no 1) - Increasing Small (no 1) | 11.50 | 4.88 | 2.36 | 0.018 | 0.045 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.79, *p* = 0.008, η²_G = 0.177
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover (no 1) vs Increasing Large (no 1) | -0.31 | 13 | = 0.764 | -0.11 [-0.70, 0.41] | negligible | n.s. |
| Increasing Crossover (no 1) vs Increasing Small (no 1) | 2.91 | 13 | = 0.018 | 1.01 [-0.09, 0.95] | large | * |
| Increasing Large (no 1) vs Increasing Small (no 1) | 2.97 | 13 | = 0.018 | 0.85 [0.13, 1.46] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.075)
**P3b latency:** Significant main effect of condition (*p* = 0.008). Post-hoc tests revealed:
  - Increasing Crossover (no 1) showed greater latency than Increasing Small (no 1) (*d* = 1.01)
  - Increasing Large (no 1) showed greater latency than Increasing Small (no 1) (*d* = 0.85)

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
