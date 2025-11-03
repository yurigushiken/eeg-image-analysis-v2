# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:45:39

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| 4 to 3 | 12 | 97.33 ms | 10.70 | 3.09 | [88.00, 116.00] |
| 5 to 3 | 4 | 102.00 ms | 16.17 | 8.08 | [88.00, 116.00] |
| 6 to 3 | 8 | 103.00 ms | 10.64 | 3.76 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 2.49 µV | 1.32 | 0.38 | [0.44, 4.24] |
| 5 to 3 | 4 | 3.50 µV | 1.58 | 0.79 | [1.58, 5.34] |
| 6 to 3 | 8 | 1.76 µV | 0.31 | 0.11 | [1.44, 2.31] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | 176.70 ms | 21.15 | 4.41 | [152.00, 220.00] |
| 5 to 3 | 24 | 173.83 ms | 17.13 | 3.50 | [140.00, 208.00] |
| 6 to 3 | 23 | 175.30 ms | 15.89 | 3.31 | [152.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | -6.44 µV | 2.28 | 0.47 | [-10.92, -1.44] |
| 5 to 3 | 24 | -6.05 µV | 2.71 | 0.55 | [-12.11, -1.76] |
| 6 to 3 | 23 | -6.61 µV | 2.36 | 0.49 | [-11.28, -1.59] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 107.33 ms | 9.00 | 2.60 | [96.00, 120.00] |
| 5 to 3 | 16 | 112.50 ms | 7.57 | 1.89 | [100.00, 120.00] |
| 6 to 3 | 14 | 109.43 ms | 8.96 | 2.39 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 2.69 µV | 1.42 | 0.41 | [0.60, 5.30] |
| 5 to 3 | 16 | 3.04 µV | 1.24 | 0.31 | [0.96, 4.61] |
| 6 to 3 | 14 | 3.01 µV | 2.18 | 0.58 | [0.16, 7.81] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 20 | 476.00 ms | 35.71 | 7.98 | [424.00, 532.00] |
| 5 to 3 | 19 | 460.84 ms | 26.69 | 6.12 | [412.00, 500.00] |
| 6 to 3 | 19 | 460.42 ms | 32.22 | 7.39 | [412.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 20 | 5.97 µV | 2.98 | 0.67 | [1.17, 11.65] |
| 5 to 3 | 19 | 6.03 µV | 2.15 | 0.49 | [3.01, 10.28] |
| 6 to 3 | 19 | 6.82 µV | 2.93 | 0.67 | [3.79, 14.26] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 190.91, BIC = 197.98
- **5 to 3 vs 4 to 3**: *β* = 0.77, *SE* = 5.148, *z* = 0.150, *p* = 0.881
- **6 to 3 vs 4 to 3**: *β* = 5.44, *SE* = 3.444, *z* = 1.581, *p* = 0.114
- **SNR**: *β* = 1.00, *SE* = 2.027, *z* = 0.495, *p* = 0.621

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.77 | 5.15 | -0.15 | 0.881 | 0.881 | n.s. |
| 4 to 3 - 6 to 3 | -5.44 | 3.44 | -1.58 | 0.114 | 0.304 | n.s. |
| 5 to 3 - 6 to 3 | -4.67 | 5.26 | -0.89 | 0.375 | 0.609 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 80.03, BIC = 87.10
- **5 to 3 vs 4 to 3**: *β* = 0.71, *SE* = 0.507, *z* = 1.397, *p* = 0.162
- **6 to 3 vs 4 to 3**: *β* = -0.80, *SE* = 0.365, *z* = -2.196, *p* = 0.028
- **SNR**: *β* = 0.44, *SE* = 0.217, *z* = 2.008, *p* = 0.045

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.71 | 0.51 | -1.40 | 0.162 | 0.162 | n.s. |
| 4 to 3 - 6 to 3 | 0.80 | 0.36 | 2.20 | 0.028 | 0.055 | n.s. |
| 5 to 3 - 6 to 3 | 1.51 | 0.52 | 2.89 | 0.004 | 0.012 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 598.49, BIC = 611.98
- **5 to 3 vs 4 to 3**: *β* = -2.64, *SE* = 3.692, *z* = -0.715, *p* = 0.474
- **6 to 3 vs 4 to 3**: *β* = -0.24, *SE* = 3.750, *z* = -0.065, *p* = 0.948
- **SNR**: *β* = 0.06, *SE* = 0.671, *z* = 0.093, *p* = 0.926

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 2.64 | 3.69 | 0.72 | 0.474 | 0.855 | n.s. |
| 4 to 3 - 6 to 3 | 0.24 | 3.75 | 0.07 | 0.948 | 0.948 | n.s. |
| 5 to 3 - 6 to 3 | -2.40 | 3.71 | -0.65 | 0.518 | 0.855 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.44, *p* = 0.645, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.63 | 21 | = 0.806 | 0.16 [-0.30, 0.57] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.16 | 21 | = 0.873 | -0.03 [-0.48, 0.41] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.93 | 21 | = 0.806 | -0.21 [-0.61, 0.26] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 306.08, BIC = 319.57
- **5 to 3 vs 4 to 3**: *β* = 0.36, *SE* = 0.477, *z* = 0.766, *p* = 0.443
- **6 to 3 vs 4 to 3**: *β* = 0.02, *SE* = 0.483, *z* = 0.037, *p* = 0.970
- **SNR**: *β* = -0.34, *SE* = 0.084, *z* = -4.083, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.37 | 0.48 | -0.77 | 0.443 | 0.828 | n.s. |
| 4 to 3 - 6 to 3 | -0.02 | 0.48 | -0.04 | 0.970 | 0.970 | n.s. |
| 5 to 3 - 6 to 3 | 0.35 | 0.48 | 0.73 | 0.468 | 0.828 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.518, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.95 | 21 | = 0.532 | -0.18 [-0.69, 0.19] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.29 | 21 | = 0.774 | 0.07 [-0.38, 0.51] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | 1.04 | 21 | = 0.532 | 0.24 [-0.26, 0.61] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 280.71, BIC = 291.13
- **5 to 3 vs 4 to 3**: *β* = 5.89, *SE* = 1.438, *z* = 4.100, *p* < .001
- **6 to 3 vs 4 to 3**: *β* = 3.14, *SE* = 1.488, *z* = 2.113, *p* = 0.035
- **SNR**: *β* = -1.06, *SE* = 0.510, *z* = -2.089, *p* = 0.037

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -5.89 | 1.44 | -4.10 | < .001 | < .001 | *** |
| 4 to 3 - 6 to 3 | -3.14 | 1.49 | -2.11 | 0.035 | 0.068 | n.s. |
| 5 to 3 - 6 to 3 | 2.75 | 1.48 | 1.86 | 0.064 | 0.068 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.76, *p* = 0.060, η²_G = 0.097
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -2.67 | 5 | = 0.134 | -0.73 [-1.87, -0.02] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -1.94 | 5 | = 0.165 | -0.52 [-1.89, 0.09] | medium | n.s. |
| 5 to 3 vs 6 to 3 | 0.60 | 5 | = 0.576 | 0.15 [-0.48, 0.88] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 147.60, BIC = 158.03
- **5 to 3 vs 4 to 3**: *β* = -0.04, *SE* = 0.430, *z* = -0.080, *p* = 0.936
- **6 to 3 vs 4 to 3**: *β* = 0.60, *SE* = 0.437, *z* = 1.384, *p* = 0.166
- **SNR**: *β* = 0.51, *SE* = 0.115, *z* = 4.461, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.03 | 0.43 | 0.08 | 0.936 | 0.936 | n.s. |
| 4 to 3 - 6 to 3 | -0.61 | 0.44 | -1.38 | 0.166 | 0.351 | n.s. |
| 5 to 3 - 6 to 3 | -0.64 | 0.43 | -1.50 | 0.134 | 0.351 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.25, *p* = 0.785, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.13 | 5 | = 0.904 | 0.05 [-0.87, 0.67] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.55 | 5 | = 0.904 | -0.15 [-1.12, 0.58] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.77 | 5 | = 0.904 | -0.23 [-0.63, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 571.24, BIC = 583.60
- **5 to 3 vs 4 to 3**: *β* = -16.34, *SE* = 8.615, *z* = -1.897, *p* = 0.058
- **6 to 3 vs 4 to 3**: *β* = -16.78, *SE* = 8.533, *z* = -1.967, *p* = 0.049
- **SNR**: *β* = 0.48, *SE* = 1.146, *z* = 0.418, *p* = 0.676

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 16.34 | 8.62 | 1.90 | 0.058 | 0.140 | n.s. |
| 4 to 3 - 6 to 3 | 16.78 | 8.53 | 1.97 | 0.049 | 0.140 | n.s. |
| 5 to 3 - 6 to 3 | 0.44 | 8.61 | 0.05 | 0.959 | 0.959 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.30, *p* = 0.116, η²_G = 0.064
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 2.05 | 16 | = 0.127 | 0.59 [-0.05, 1.04] | medium | n.s. |
| 4 to 3 vs 6 to 3 | 1.84 | 16 | = 0.127 | 0.46 [-0.01, 1.05] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.26 | 16 | = 0.794 | -0.09 [-0.57, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 255.85, BIC = 268.21
- **5 to 3 vs 4 to 3**: *β* = 0.01, *SE* = 0.524, *z* = 0.023, *p* = 0.981
- **6 to 3 vs 4 to 3**: *β* = 0.64, *SE* = 0.517, *z* = 1.232, *p* = 0.218
- **SNR**: *β* = 0.37, *SE* = 0.078, *z* = 4.753, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.01 | 0.52 | -0.02 | 0.981 | 0.981 | n.s. |
| 4 to 3 - 6 to 3 | -0.64 | 0.52 | -1.23 | 0.218 | 0.521 | n.s. |
| 5 to 3 - 6 to 3 | -0.63 | 0.52 | -1.20 | 0.228 | 0.521 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.397, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.64 | 16 | = 0.529 | 0.15 [-0.36, 0.67] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.82 | 16 | = 0.529 | -0.17 [-0.67, 0.33] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -1.23 | 16 | = 0.529 | -0.34 [-0.78, 0.23] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Marginal trend toward condition differences (*p* = 0.060)

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
