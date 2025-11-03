# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:38:12

---

## 1. Analysis Overview

**Total Measurements:** 152
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
| Decrease by 3 (Correct) | 18 | 104.89 ms | 8.52 | 2.01 | [88.00, 116.00] |
| Decrease by 3 (Incorrect) | 7 | 99.43 ms | 8.77 | 3.32 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 3 (Correct) | 18 | -2.41 µV | 1.59 | 0.37 | [-6.39, -0.34] |
| Decrease by 3 (Incorrect) | 7 | -6.97 µV | 4.55 | 1.72 | [-15.27, -1.35] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 3 (Correct) | 24 | 177.00 ms | 15.02 | 3.07 | [152.00, 208.00] |
| Decrease by 3 (Incorrect) | 9 | 181.33 ms | 17.32 | 5.77 | [160.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 3 (Correct) | 24 | -5.22 µV | 1.97 | 0.40 | [-8.60, -1.48] |
| Decrease by 3 (Incorrect) | 9 | -7.62 µV | 5.47 | 1.82 | [-16.59, -0.49] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 3 (Correct) | 17 | 115.53 ms | 8.23 | 2.00 | [104.00, 128.00] |
| Decrease by 3 (Incorrect) | 8 | 113.00 ms | 11.86 | 4.19 | [96.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 3 (Correct) | 17 | 3.00 µV | 1.87 | 0.45 | [1.02, 8.15] |
| Decrease by 3 (Incorrect) | 8 | 5.39 µV | 4.71 | 1.67 | [1.16, 13.25] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 3 (Correct) | 19 | 474.11 ms | 31.93 | 7.32 | [408.00, 524.00] |
| Decrease by 3 (Incorrect) | 5 | 479.20 ms | 43.58 | 19.49 | [420.00, 524.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decrease by 3 (Correct) | 19 | 5.54 µV | 2.91 | 0.67 | [0.74, 12.38] |
| Decrease by 3 (Incorrect) | 5 | 5.47 µV | 3.93 | 1.76 | [2.16, 10.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 184.20, BIC = 190.29
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = -5.23, *SE* = 3.492, *z* = -1.498, *p* = 0.134
- **SNR**: *β* = 1.34, *SE* = 0.895, *z* = 1.501, *p* = 0.133

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 5.23 | 3.49 | 1.50 | 0.134 | 0.134 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.43, *p* = 0.542, η²_G = 0.041
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.65 | 5 | = 0.542 | 0.38 [-0.80, 1.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 123.79, BIC = 129.88
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = -4.58, *SE* = 0.938, *z* = -4.884, *p* < .001
- **SNR**: *β* = -0.45, *SE* = 0.271, *z* = -1.662, *p* = 0.097

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 4.58 | 0.94 | 4.88 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.23, *p* = 0.024, η²_G = 0.339
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 3.20 | 5 | = 0.024 | 1.31 [-0.12, 2.73] | large | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 282.48, BIC = 289.97
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = 3.39, *SE* = 5.838, *z* = 0.580, *p* = 0.562
- **SNR**: *β* = -0.18, *SE* = 0.509, *z* = -0.360, *p* = 0.719

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -3.39 | 5.84 | -0.58 | 0.562 | 0.562 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.15, *p* = 0.712, η²_G = 0.007
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | -0.38 | 8 | = 0.712 | -0.16 [-0.90, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 166.10, BIC = 173.58
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = -3.56, *SE* = 1.013, *z* = -3.517, *p* < .001
- **SNR**: *β* = -0.33, *SE* = 0.081, *z* = -4.037, *p* < .001

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 3.56 | 1.01 | 3.52 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.16, *p* = 0.313, η²_G = 0.067
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 1.08 | 8 | = 0.313 | 0.50 [-0.43, 1.15] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 190.20, BIC = 196.30
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = -0.86, *SE* = 4.102, *z* = -0.209, *p* = 0.835
- **SNR**: *β* = 0.90, *SE* = 0.933, *z* = 0.966, *p* = 0.334

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | 0.86 | 4.10 | 0.21 | 0.835 | 0.835 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.655, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | 0.47 | 5 | = 0.655 | 0.26 [-0.87, 1.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 131.76, BIC = 137.86
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = 3.28, *SE* = 1.277, *z* = 2.568, *p* = 0.010
- **SNR**: *β* = 0.42, *SE* = 0.289, *z* = 1.470, *p* = 0.142

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -3.28 | 1.28 | -2.57 | 0.010 | 0.010 | * |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.02, *p* = 0.214, η²_G = 0.140
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | -1.42 | 5 | = 0.214 | -0.74 [-1.72, 0.55] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 242.48, BIC = 248.37
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = 4.30, *SE* = 12.441, *z* = 0.346, *p* = 0.730
- **SNR**: *β* = 0.16, *SE* = 1.218, *z* = 0.130, *p* = 0.897

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -4.30 | 12.44 | -0.35 | 0.730 | 0.730 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.01, *p* = 0.943, η²_G = 0.000
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | -0.08 | 3 | = 0.943 | -0.03 [-1.63, 1.55] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 120.28, BIC = 126.17
- **Decrease by 3 (Incorrect) vs Decrease by 3 (Correct)**: *β* = 2.87, *SE* = 1.416, *z* = 2.027, *p* = 0.043
- **SNR**: *β* = 0.34, *SE* = 0.098, *z* = 3.503, *p* < .001

_Reference condition: **Decrease by 3 (Correct)** (all condition effects are contrasts vs. this baseline)._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decrease by 3 (Correct) - Decrease by 3 (Incorrect) | -2.87 | 1.42 | -2.03 | 0.043 | 0.043 | * |

_Note: p-values adjusted using Holm-Sidak method for 1 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.443, η²_G = 0.083
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with uncorrected correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decrease by 3 (Correct) vs Decrease by 3 (Incorrect) | -0.88 | 3 | = 0.443 | -0.52 [-2.11, 1.23] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.024). Post-hoc tests revealed:
  - Decrease by 3 (Correct) showed greater amplitude than Decrease by 3 (Incorrect) (*d* = 1.31)

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
