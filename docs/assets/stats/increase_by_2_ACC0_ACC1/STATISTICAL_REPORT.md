# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:43:10

---

## 1. Analysis Overview

**Total Measurements:** 176
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
| Increase by 2 (Correct) | 15 | 101.07 ms | 5.95 | 1.54 | [92.00, 108.00] |
| Increase by 2 (Incorrect) | 10 | 100.40 ms | 6.38 | 2.02 | [92.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 2 (Correct) | 15 | -1.47 µV | 1.13 | 0.29 | [-4.17, -0.21] |
| Increase by 2 (Incorrect) | 10 | -2.27 µV | 1.12 | 0.36 | [-4.08, -0.97] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 2 (Correct) | 24 | 168.50 ms | 18.96 | 3.87 | [136.00, 200.00] |
| Increase by 2 (Incorrect) | 18 | 170.22 ms | 20.08 | 4.73 | [136.00, 196.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 2 (Correct) | 24 | -5.50 µV | 2.44 | 0.50 | [-11.28, -1.22] |
| Increase by 2 (Incorrect) | 18 | -6.21 µV | 2.35 | 0.55 | [-11.62, -2.34] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 2 (Correct) | 15 | 94.13 ms | 16.48 | 4.26 | [68.00, 108.00] |
| Increase by 2 (Incorrect) | 9 | 77.33 ms | 16.37 | 5.46 | [60.00, 104.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 2 (Correct) | 15 | 1.90 µV | 1.20 | 0.31 | [0.67, 4.70] |
| Increase by 2 (Incorrect) | 9 | 2.82 µV | 1.37 | 0.46 | [1.46, 5.54] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 2 (Correct) | 18 | 481.33 ms | 27.16 | 6.40 | [428.00, 512.00] |
| Increase by 2 (Incorrect) | 13 | 468.92 ms | 21.30 | 5.91 | [428.00, 496.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 2 (Correct) | 18 | 5.34 µV | 2.72 | 0.64 | [1.31, 10.55] |
| Increase by 2 (Incorrect) | 13 | 5.77 µV | 3.19 | 0.88 | [2.41, 10.89] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 168.16, BIC = 174.25
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = -0.47, *SE* = 2.244, *z* = -0.211, *p* = 0.833

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 0.47 | 2.24 | 0.21 | 0.833 | 0.833 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.12, *p* = 0.741, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -0.35 | 5 | = 0.741 | -0.22 [-1.20, 0.91] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 56.04, BIC = 62.14
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = -0.92, *SE* = 0.185, *z* = -4.964, *p* < .001
- **SNR**: *β* = -0.47, *SE* = 0.082, *z* = -5.729, *p* < .001

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 0.92 | 0.18 | 4.96 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 21.37, *p* = 0.006, η²_G = 0.306
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 4.62 | 5 | = 0.006 | 1.21 [0.14, 3.64] | large | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 370.02, BIC = 378.70
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = -0.14, *SE* = 4.636, *z* = -0.031, *p* = 0.975
- **SNR**: *β* = -0.35, *SE* = 0.567, *z* = -0.614, *p* = 0.539

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 0.14 | 4.64 | 0.03 | 0.975 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.02, *p* = 0.881, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -0.15 | 17 | = 0.881 | -0.03 [-0.53, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 183.49, BIC = 192.18
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = -1.44, *SE* = 0.448, *z* = -3.200, *p* = 0.001
- **SNR**: *β* = -0.19, *SE* = 0.057, *z* = -3.312, *p* = 0.001

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 1.43 | 0.45 | 3.20 | 0.001 | 0.001 | ** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.13, *p* = 0.163, η²_G = 0.025
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 1.46 | 17 | = 0.163 | 0.31 [-0.17, 0.86] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 210.38, BIC = 216.27
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = -16.86, *SE* = 6.645, *z* = -2.537, *p* = 0.011
- **SNR**: *β* = -0.53, *SE* = 2.805, *z* = -0.190, *p* = 0.850

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 16.86 | 6.65 | 2.54 | 0.011 | 0.011 | * |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.346, η²_G = 0.155
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 1.07 | 4 | = 0.346 | 0.77 [-0.83, 1.79] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 84.40, BIC = 90.29
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = 1.00, *SE* = 0.468, *z* = 2.130, *p* = 0.033
- **SNR**: *β* = 0.31, *SE* = 0.256, *z* = 1.210, *p* = 0.226

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -1.00 | 0.47 | -2.13 | 0.033 | 0.033 | * |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.99, *p* = 0.030, η²_G = 0.454
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -3.31 | 4 | = 0.030 | -1.63 [-3.28, 0.32] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 293.72, BIC = 300.89
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = -19.50, *SE* = 10.955, *z* = -1.780, *p* = 0.075
- **SNR**: *β* = -1.15, *SE* = 1.129, *z* = -1.023, *p* = 0.306

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | 19.50 | 10.95 | 1.78 | 0.075 | 0.075 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.05, *p* = 0.180, η²_G = 0.070
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | 1.43 | 11 | = 0.180 | 0.53 [-0.25, 1.08] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 138.24, BIC = 145.41
- **Increase by 2 (Incorrect) vs Increase by 2 (Correct)**: *β* = 2.99, *SE* = 0.773, *z* = 3.871, *p* < .001
- **SNR**: *β* = 0.41, *SE* = 0.080, *z* = 5.161, *p* < .001

_Reference condition: **Increase by 2 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 2 (Correct) - Increase by 2 (Incorrect) | -2.99 | 0.77 | -3.87 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.26, *p* = 0.621, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 2 (Correct) vs Increase by 2 (Incorrect) | -0.51 | 11 | = 0.621 | -0.16 [-0.79, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.006). Post-hoc tests revealed:
  - Increase by 2 (Correct) showed greater amplitude than Increase by 2 (Incorrect) (*d* = 1.21)
**P1 amplitude:** Significant main effect of condition (*p* = 0.030). Post-hoc tests revealed:
  - Increase by 2 (Correct) showed smaller amplitude than Increase by 2 (Incorrect) (*d* = -1.63)

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
