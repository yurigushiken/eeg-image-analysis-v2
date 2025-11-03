# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:43:47

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
| 1 to 4 | 10 | 103.20 ms | 9.20 | 2.91 | [84.00, 112.00] |
| 2 to 5 | 9 | 103.11 ms | 7.94 | 2.65 | [84.00, 108.00] |
| 3 to 6 | 15 | 96.53 ms | 10.46 | 2.70 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 10 | -3.23 µV | 1.24 | 0.39 | [-4.46, -0.79] |
| 2 to 5 | 9 | -3.26 µV | 4.01 | 1.34 | [-12.97, -0.70] |
| 3 to 6 | 15 | -3.52 µV | 1.23 | 0.32 | [-5.36, -1.51] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 21 | 171.62 ms | 20.74 | 4.53 | [136.00, 216.00] |
| 2 to 5 | 24 | 173.17 ms | 20.41 | 4.17 | [136.00, 212.00] |
| 3 to 6 | 23 | 168.00 ms | 19.85 | 4.14 | [136.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 21 | -7.07 µV | 2.85 | 0.62 | [-13.14, -2.90] |
| 2 to 5 | 24 | -6.39 µV | 2.61 | 0.53 | [-13.83, -1.17] |
| 3 to 6 | 23 | -7.11 µV | 2.77 | 0.58 | [-12.76, -3.05] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 98.15 ms | 9.75 | 2.70 | [80.00, 108.00] |
| 2 to 5 | 11 | 90.18 ms | 12.18 | 3.67 | [76.00, 108.00] |
| 3 to 6 | 10 | 93.20 ms | 12.51 | 3.96 | [76.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 13 | 3.30 µV | 1.59 | 0.44 | [0.90, 6.37] |
| 2 to 5 | 11 | 3.46 µV | 3.17 | 0.96 | [0.98, 11.63] |
| 3 to 6 | 10 | 4.20 µV | 2.04 | 0.64 | [0.78, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 454.40 ms | 56.04 | 12.53 | [376.00, 528.00] |
| 2 to 5 | 23 | 441.57 ms | 50.19 | 10.47 | [364.00, 528.00] |
| 3 to 6 | 18 | 474.00 ms | 52.70 | 12.42 | [360.00, 528.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 20 | 6.13 µV | 3.21 | 0.72 | [2.01, 13.02] |
| 2 to 5 | 23 | 5.98 µV | 2.57 | 0.54 | [2.56, 11.71] |
| 3 to 6 | 18 | 5.25 µV | 2.27 | 0.53 | [2.46, 11.34] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 257.92, BIC = 267.08
- **2 to 5 vs 1 to 4**: *β* = 0.08, *SE* = 4.151, *z* = 0.020, *p* = 0.984
- **3 to 6 vs 1 to 4**: *β* = -6.32, *SE* = 3.964, *z* = -1.594, *p* = 0.111
- **SNR**: *β* = 0.51, *SE* = 0.717, *z* = 0.718, *p* = 0.473

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.08 | 4.15 | -0.02 | 0.984 | 0.984 | n.s. |
| 1 to 4 - 3 to 6 | 6.32 | 3.96 | 1.59 | 0.111 | 0.289 | n.s. |
| 2 to 5 - 3 to 6 | 6.40 | 3.98 | 1.61 | 0.107 | 0.289 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.06, *p* = 0.939, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.24 | 3 | = 1.000 | -0.15 [-0.89, 0.78] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.00 | 3 | = 1.000 | 0.00 [-0.87, 1.73] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 0.27 | 3 | = 1.000 | 0.17 [-1.12, 1.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 123.76, BIC = 132.92
- **2 to 5 vs 1 to 4**: *β* = 0.07, *SE* = 0.481, *z* = 0.134, *p* = 0.893
- **3 to 6 vs 1 to 4**: *β* = -0.52, *SE* = 0.417, *z* = -1.244, *p* = 0.214
- **SNR**: *β* = -0.88, *SE* = 0.101, *z* = -8.699, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.06 | 0.48 | -0.13 | 0.893 | 0.893 | n.s. |
| 1 to 4 - 3 to 6 | 0.52 | 0.42 | 1.24 | 0.214 | 0.448 | n.s. |
| 2 to 5 - 3 to 6 | 0.58 | 0.43 | 1.34 | 0.180 | 0.448 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.40, *p* = 0.685, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.70 | 3 | = 0.744 | 0.31 [-0.74, 0.94] | small | n.s. |
| 1 to 4 vs 3 to 6 | 0.92 | 3 | = 0.744 | 0.16 [-0.70, 2.04] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.36 | 3 | = 0.744 | -0.14 [-1.46, 1.05] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 602.03, BIC = 615.34
- **2 to 5 vs 1 to 4**: *β* = 0.41, *SE* = 4.685, *z* = 0.088, *p* = 0.930
- **3 to 6 vs 1 to 4**: *β* = -3.95, *SE* = 4.632, *z* = -0.853, *p* = 0.394
- **SNR**: *β* = -0.15, *SE* = 1.065, *z* = -0.139, *p* = 0.889

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.41 | 4.69 | -0.09 | 0.930 | 0.930 | n.s. |
| 1 to 4 - 3 to 6 | 3.95 | 4.63 | 0.85 | 0.394 | 0.703 | n.s. |
| 2 to 5 - 3 to 6 | 4.36 | 4.51 | 0.97 | 0.333 | 0.703 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.422, η²_G = 0.017
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.08 | 20 | = 0.938 | -0.02 [-0.47, 0.44] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 1.09 | 20 | = 0.432 | 0.26 [-0.22, 0.70] | small | n.s. |
| 2 to 5 vs 3 to 6 | 1.27 | 20 | = 0.432 | 0.29 [-0.27, 0.60] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 295.23, BIC = 308.55
- **2 to 5 vs 1 to 4**: *β* = 0.06, *SE* = 0.453, *z* = 0.133, *p* = 0.894
- **3 to 6 vs 1 to 4**: *β* = -0.37, *SE* = 0.448, *z* = -0.834, *p* = 0.404
- **SNR**: *β* = -0.51, *SE* = 0.111, *z* = -4.576, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.06 | 0.45 | -0.13 | 0.894 | 0.894 | n.s. |
| 1 to 4 - 3 to 6 | 0.37 | 0.45 | 0.83 | 0.404 | 0.686 | n.s. |
| 2 to 5 - 3 to 6 | 0.43 | 0.44 | 0.99 | 0.321 | 0.686 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.69, *p* = 0.508, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | -0.63 | 20 | = 0.562 | -0.12 [-0.60, 0.32] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 0.59 | 20 | = 0.562 | 0.10 [-0.33, 0.59] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | 1.09 | 20 | = 0.562 | 0.24 [-0.15, 0.73] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 263.94, BIC = 273.10
- **2 to 5 vs 1 to 4**: *β* = -4.88, *SE* = 3.942, *z* = -1.237, *p* = 0.216
- **3 to 6 vs 1 to 4**: *β* = -6.42, *SE* = 3.925, *z* = -1.635, *p* = 0.102
- **SNR**: *β* = 3.18, *SE* = 1.429, *z* = 2.227, *p* = 0.026

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 4.88 | 3.94 | 1.24 | 0.216 | 0.385 | n.s. |
| 1 to 4 - 3 to 6 | 6.42 | 3.93 | 1.63 | 0.102 | 0.276 | n.s. |
| 2 to 5 - 3 to 6 | 1.54 | 4.38 | 0.35 | 0.725 | 0.725 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 1.29 | 1 | = 0.631 | 1.48 [-0.50, 1.81] | large | n.s. |
| 1 to 4 vs 3 to 6 | 0.43 | 1 | = 0.742 | 0.49 [-0.76, 1.92] | small | n.s. |
| 2 to 5 vs 3 to 6 | -inf | 1 | < .001 | -4.24 [-1.78, 1.43] | large | *** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 146.10, BIC = 155.26
- **2 to 5 vs 1 to 4**: *β* = 0.48, *SE* = 0.596, *z* = 0.799, *p* = 0.425
- **3 to 6 vs 1 to 4**: *β* = -0.42, *SE* = 0.641, *z* = -0.649, *p* = 0.516
- **SNR**: *β* = 0.69, *SE* = 0.259, *z* = 2.673, *p* = 0.008

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.48 | 0.60 | -0.80 | 0.425 | 0.669 | n.s. |
| 1 to 4 - 3 to 6 | 0.42 | 0.64 | 0.65 | 0.516 | 0.669 | n.s. |
| 2 to 5 - 3 to 6 | 0.89 | 0.69 | 1.29 | 0.198 | 0.484 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.51 | 1 | = 0.771 | 0.71 [-0.75, 1.41] | medium | n.s. |
| 1 to 4 vs 3 to 6 | 0.53 | 1 | = 0.771 | 0.12 [-0.53, 2.48] | negligible | n.s. |
| 2 to 5 vs 3 to 6 | -0.38 | 1 | = 0.771 | -0.53 [-1.16, 2.24] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 663.55, BIC = 676.22
- **2 to 5 vs 1 to 4**: *β* = -14.07, *SE* = 14.236, *z* = -0.988, *p* = 0.323
- **3 to 6 vs 1 to 4**: *β* = 17.60, *SE* = 15.676, *z* = 1.122, *p* = 0.262
- **SNR**: *β* = -0.20, *SE* = 2.716, *z* = -0.073, *p* = 0.942

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | 14.07 | 14.24 | 0.99 | 0.323 | 0.455 | n.s. |
| 1 to 4 - 3 to 6 | -17.60 | 15.68 | -1.12 | 0.262 | 0.455 | n.s. |
| 2 to 5 - 3 to 6 | -31.67 | 14.62 | -2.17 | 0.030 | 0.088 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.95, *p* = 0.158, η²_G = 0.059
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.75 | 16 | = 0.462 | 0.22 [-0.22, 0.77] | small | n.s. |
| 1 to 4 vs 3 to 6 | -1.14 | 16 | = 0.407 | -0.35 [-0.80, 0.25] | small | n.s. |
| 2 to 5 vs 3 to 6 | -2.05 | 16 | = 0.171 | -0.62 [-1.00, 0.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 250.83, BIC = 263.50
- **2 to 5 vs 1 to 4**: *β* = 0.35, *SE* = 0.398, *z* = 0.892, *p* = 0.372
- **3 to 6 vs 1 to 4**: *β* = -0.10, *SE* = 0.448, *z* = -0.233, *p* = 0.816
- **SNR**: *β* = 0.53, *SE* = 0.090, *z* = 5.848, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 5 | -0.35 | 0.40 | -0.89 | 0.372 | 0.609 | n.s. |
| 1 to 4 - 3 to 6 | 0.10 | 0.45 | 0.23 | 0.816 | 0.816 | n.s. |
| 2 to 5 - 3 to 6 | 0.46 | 0.42 | 1.11 | 0.269 | 0.609 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.69, *p* = 0.036, η²_G = 0.046
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 5 | 0.38 | 16 | = 0.709 | 0.07 [-0.48, 0.48] | negligible | n.s. |
| 1 to 4 vs 3 to 6 | 2.36 | 16 | = 0.056 | 0.47 [0.02, 1.13] | small | n.s. |
| 2 to 5 vs 3 to 6 | 2.27 | 16 | = 0.056 | 0.45 [0.01, 1.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* = 0.036) (no significant pairwise comparisons)

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
