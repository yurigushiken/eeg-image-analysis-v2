# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:43:38

---

## 1. Analysis Overview

**Total Measurements:** 180
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
| Increase by 3 (Correct) | 12 | 102.00 ms | 6.93 | 2.00 | [92.00, 112.00] |
| Increase by 3 (Incorrect) | 12 | 101.00 ms | 6.85 | 1.98 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 3 (Correct) | 12 | -1.98 µV | 0.97 | 0.28 | [-3.35, -0.70] |
| Increase by 3 (Incorrect) | 12 | -3.54 µV | 3.06 | 0.88 | [-8.80, -0.28] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 3 (Correct) | 23 | 169.91 ms | 19.89 | 4.15 | [136.00, 212.00] |
| Increase by 3 (Incorrect) | 20 | 167.40 ms | 23.94 | 5.35 | [136.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 3 (Correct) | 23 | -6.31 µV | 2.51 | 0.52 | [-12.86, -2.20] |
| Increase by 3 (Incorrect) | 20 | -6.77 µV | 3.15 | 0.70 | [-13.73, -1.60] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 3 (Correct) | 16 | 99.25 ms | 7.76 | 1.94 | [88.00, 108.00] |
| Increase by 3 (Incorrect) | 10 | 98.00 ms | 7.83 | 2.48 | [88.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 3 (Correct) | 16 | 2.04 µV | 1.39 | 0.35 | [0.46, 5.27] |
| Increase by 3 (Incorrect) | 10 | 4.55 µV | 2.49 | 0.79 | [0.78, 8.76] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 3 (Correct) | 19 | 453.26 ms | 54.29 | 12.46 | [356.00, 524.00] |
| Increase by 3 (Incorrect) | 14 | 440.29 ms | 60.12 | 16.07 | [336.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 3 (Correct) | 19 | 4.92 µV | 2.53 | 0.58 | [1.25, 10.15] |
| Increase by 3 (Incorrect) | 14 | 5.92 µV | 2.60 | 0.70 | [3.30, 12.49] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 165.88, BIC = 171.77
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = 0.34, *SE* = 2.366, *z* = 0.142, *p* = 0.887
- **SNR**: *β* = 0.49, *SE* = 0.915, *z* = 0.534, *p* = 0.593

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -0.34 | 2.37 | -0.14 | 0.887 | 0.887 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.06, *p* = 0.809, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | -0.25 | 5 | = 0.809 | -0.10 [-1.16, 0.95] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 102.10, BIC = 107.99
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = -2.57, *SE* = 0.658, *z* = -3.909, *p* < .001
- **SNR**: *β* = -0.89, *SE* = 0.263, *z* = -3.373, *p* = 0.001

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 2.57 | 0.66 | 3.91 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.64, *p* = 0.084, η²_G = 0.155
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 2.15 | 5 | = 0.084 | 0.78 [-0.36, 2.12] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 390.96, BIC = 399.77
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = -3.51, *SE* = 6.109, *z* = -0.574, *p* = 0.566
- **SNR**: *β* = 0.03, *SE* = 0.757, *z* = 0.036, *p* = 0.972

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 3.51 | 6.11 | 0.57 | 0.566 | 0.566 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.337, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.99 | 18 | = 0.337 | 0.24 [-0.26, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 195.60, BIC = 204.40
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = -1.74, *SE* = 0.616, *z* = -2.829, *p* = 0.005
- **SNR**: *β* = -0.28, *SE* = 0.081, *z* = -3.476, *p* = 0.001

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 1.74 | 0.62 | 2.83 | 0.005 | 0.005 | ** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.47, *p* = 0.501, η²_G = 0.004
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.69 | 18 | = 0.501 | 0.13 [-0.33, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 182.25, BIC = 188.54
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = -0.57, *SE* = 1.908, *z* = -0.300, *p* = 0.764
- **SNR**: *β* = 0.29, *SE* = 0.320, *z* = 0.924, *p* = 0.356

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 0.57 | 1.91 | 0.30 | 0.764 | 0.764 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.30, *p* = 0.604, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 0.55 | 6 | = 0.604 | 0.16 [-0.73, 1.14] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 104.93, BIC = 111.22
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = 2.92, *SE* = 0.617, *z* = 4.724, *p* < .001
- **SNR**: *β* = 0.31, *SE* = 0.161, *z* = 1.922, *p* = 0.055

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -2.92 | 0.62 | -4.72 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 12.41, *p* = 0.012, η²_G = 0.284
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | -3.52 | 6 | = 0.012 | -1.16 [-2.60, -0.06] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 368.18, BIC = 375.66
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = -11.40, *SE* = 25.992, *z* = -0.438, *p* = 0.661
- **SNR**: *β* = 0.54, *SE* = 4.154, *z* = 0.131, *p* = 0.896

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | 11.40 | 25.99 | 0.44 | 0.661 | 0.661 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.19, *p* = 0.298, η²_G = 0.056
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | 1.09 | 12 | = 0.298 | 0.47 [-0.32, 0.92] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 138.67, BIC = 146.15
- **Increase by 3 (Incorrect) vs Increase by 3 (Correct)**: *β* = 2.24, *SE* = 0.504, *z* = 4.446, *p* < .001
- **SNR**: *β* = 0.46, *SE* = 0.093, *z* = 4.972, *p* < .001

_Reference condition: **Increase by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 3 (Correct) - Increase by 3 (Incorrect) | -2.24 | 0.50 | -4.45 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.11, *p* = 0.172, η²_G = 0.035
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 3 (Correct) vs Increase by 3 (Incorrect) | -1.45 | 12 | = 0.172 | -0.37 [-1.03, 0.23] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.084)
**P1 amplitude:** Significant main effect of condition (*p* = 0.012). Post-hoc tests revealed:
  - Increase by 3 (Correct) showed smaller amplitude than Increase by 3 (Incorrect) (*d* = -1.16)

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

#### Amplitude

### 5.3 P1 Component

#### Latency

#### Amplitude

### 5.4 P3b Component

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
