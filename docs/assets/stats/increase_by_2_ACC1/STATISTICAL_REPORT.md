# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:40:19

---

## 1. Analysis Overview

**Total Measurements:** 384
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 1 to 3 | 15 | 94.40 ms | 18.69 | 4.83 | [68.00, 112.00] |
| 2 to 4 | 7 | 88.57 ms | 12.53 | 4.74 | [76.00, 112.00] |
| 3 to 5 | 10 | 91.60 ms | 16.59 | 5.25 | [68.00, 112.00] |
| 4 to 6 | 9 | 92.00 ms | 19.18 | 6.39 | [68.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 15 | 2.99 µV | 1.82 | 0.47 | [0.92, 7.03] |
| 2 to 4 | 7 | 2.40 µV | 1.20 | 0.46 | [1.04, 4.01] |
| 3 to 5 | 10 | 3.18 µV | 2.23 | 0.71 | [0.94, 7.66] |
| 4 to 6 | 9 | 3.64 µV | 1.43 | 0.48 | [1.32, 5.29] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 169.67 ms | 23.97 | 4.89 | [136.00, 208.00] |
| 2 to 4 | 22 | 170.91 ms | 17.29 | 3.69 | [136.00, 208.00] |
| 3 to 5 | 22 | 163.09 ms | 21.87 | 4.66 | [136.00, 208.00] |
| 4 to 6 | 22 | 168.00 ms | 21.13 | 4.50 | [136.00, 200.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.35 µV | 2.66 | 0.54 | [-12.53, -1.95] |
| 2 to 4 | 22 | -6.65 µV | 2.70 | 0.57 | [-15.66, -2.93] |
| 3 to 5 | 22 | -5.99 µV | 2.58 | 0.55 | [-13.75, -1.70] |
| 4 to 6 | 22 | -6.92 µV | 3.59 | 0.77 | [-16.09, -3.11] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 12 | 93.33 ms | 14.51 | 4.19 | [76.00, 108.00] |
| 2 to 4 | 16 | 89.50 ms | 15.79 | 3.95 | [68.00, 108.00] |
| 3 to 5 | 13 | 91.69 ms | 14.09 | 3.91 | [68.00, 108.00] |
| 4 to 6 | 15 | 93.33 ms | 13.75 | 3.55 | [68.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 12 | 3.15 µV | 1.92 | 0.55 | [0.62, 7.47] |
| 2 to 4 | 16 | 3.28 µV | 1.62 | 0.41 | [1.12, 7.11] |
| 3 to 5 | 13 | 3.46 µV | 1.71 | 0.47 | [1.18, 6.32] |
| 4 to 6 | 15 | 3.93 µV | 2.01 | 0.52 | [1.36, 7.49] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 454.60 ms | 39.24 | 8.77 | [388.00, 516.00] |
| 2 to 4 | 19 | 468.21 ms | 53.72 | 12.32 | [388.00, 536.00] |
| 3 to 5 | 16 | 470.75 ms | 51.84 | 12.96 | [388.00, 536.00] |
| 4 to 6 | 18 | 479.33 ms | 52.52 | 12.38 | [388.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 6.44 µV | 3.61 | 0.81 | [1.71, 14.25] |
| 2 to 4 | 19 | 7.32 µV | 4.34 | 0.99 | [1.60, 17.43] |
| 3 to 5 | 16 | 6.44 µV | 3.41 | 0.85 | [1.91, 16.52] |
| 4 to 6 | 18 | 6.77 µV | 3.53 | 0.83 | [1.86, 12.37] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 356.98, BIC = 368.98
- **2 to 4 vs 1 to 3**: *β* = -3.58, *SE* = 7.029, *z* = -0.509, *p* = 0.611
- **3 to 5 vs 1 to 3**: *β* = -2.11, *SE* = 6.258, *z* = -0.337, *p* = 0.736
- **4 to 6 vs 1 to 3**: *β* = -3.12, *SE* = 6.511, *z* = -0.480, *p* = 0.631
- **SNR**: *β* = 3.47, *SE* = 1.856, *z* = 1.868, *p* = 0.062

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 3.58 | 7.03 | 0.51 | 0.611 | 0.997 | n.s. |
| 1 to 3 - 3 to 5 | 2.11 | 6.26 | 0.34 | 0.736 | 0.997 | n.s. |
| 1 to 3 - 4 to 6 | 3.12 | 6.51 | 0.48 | 0.631 | 0.997 | n.s. |
| 2 to 4 - 3 to 5 | -1.46 | 7.61 | -0.19 | 0.847 | 0.997 | n.s. |
| 2 to 4 - 4 to 6 | -0.45 | 7.88 | -0.06 | 0.954 | 0.997 | n.s. |
| 3 to 5 - 4 to 6 | 1.01 | 7.06 | 0.14 | 0.886 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 142.72, BIC = 154.71
- **2 to 4 vs 1 to 3**: *β* = 0.10, *SE* = 0.516, *z* = 0.190, *p* = 0.849
- **3 to 5 vs 1 to 3**: *β* = 0.52, *SE* = 0.457, *z* = 1.137, *p* = 0.256
- **4 to 6 vs 1 to 3**: *β* = 0.61, *SE* = 0.476, *z* = 1.293, *p* = 0.196
- **SNR**: *β* = 0.97, *SE* = 0.141, *z* = 6.875, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -0.10 | 0.52 | -0.19 | 0.849 | 0.977 | n.s. |
| 1 to 3 - 3 to 5 | -0.52 | 0.46 | -1.14 | 0.256 | 0.771 | n.s. |
| 1 to 3 - 4 to 6 | -0.62 | 0.48 | -1.29 | 0.196 | 0.730 | n.s. |
| 2 to 4 - 3 to 5 | -0.42 | 0.56 | -0.76 | 0.450 | 0.848 | n.s. |
| 2 to 4 - 4 to 6 | -0.52 | 0.58 | -0.89 | 0.376 | 0.848 | n.s. |
| 3 to 5 - 4 to 6 | -0.10 | 0.52 | -0.18 | 0.855 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 794.56, BIC = 812.06
- **2 to 4 vs 1 to 3**: *β* = 3.53, *SE* = 4.490, *z* = 0.787, *p* = 0.431
- **3 to 5 vs 1 to 3**: *β* = -4.31, *SE* = 4.486, *z* = -0.960, *p* = 0.337
- **4 to 6 vs 1 to 3**: *β* = -2.83, *SE* = 4.452, *z* = -0.636, *p* = 0.525
- **SNR**: *β* = 0.50, *SE* = 0.728, *z* = 0.687, *p* = 0.492

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -3.53 | 4.49 | -0.79 | 0.431 | 0.816 | n.s. |
| 1 to 3 - 3 to 5 | 4.31 | 4.49 | 0.96 | 0.337 | 0.807 | n.s. |
| 1 to 3 - 4 to 6 | 2.83 | 4.45 | 0.64 | 0.525 | 0.816 | n.s. |
| 2 to 4 - 3 to 5 | 7.84 | 4.55 | 1.73 | 0.084 | 0.411 | n.s. |
| 2 to 4 - 4 to 6 | 6.37 | 4.64 | 1.37 | 0.170 | 0.606 | n.s. |
| 3 to 5 - 4 to 6 | -1.48 | 4.64 | -0.32 | 0.750 | 0.816 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.99, *p* = 0.403, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.93 | 18 | = 0.728 | -0.25 [-0.62, 0.28] | small | n.s. |
| 1 to 3 vs 3 to 5 | 0.56 | 18 | = 0.835 | 0.16 [-0.32, 0.57] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | 0.37 | 18 | = 0.835 | 0.10 [-0.32, 0.57] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.97 | 18 | = 0.236 | 0.45 [0.03, 1.00] | small | n.s. |
| 2 to 4 vs 4 to 6 | 1.86 | 18 | = 0.236 | 0.38 [-0.10, 0.87] | small | n.s. |
| 3 to 5 vs 4 to 6 | -0.21 | 18 | = 0.835 | -0.06 [-0.48, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 394.27, BIC = 411.77
- **2 to 4 vs 1 to 3**: *β* = -0.46, *SE* = 0.483, *z* = -0.954, *p* = 0.340
- **3 to 5 vs 1 to 3**: *β* = 0.18, *SE* = 0.483, *z* = 0.381, *p* = 0.703
- **4 to 6 vs 1 to 3**: *β* = -0.47, *SE* = 0.480, *z* = -0.984, *p* = 0.325
- **SNR**: *β* = -0.54, *SE* = 0.076, *z* = -7.131, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.46 | 0.48 | 0.95 | 0.340 | 0.792 | n.s. |
| 1 to 3 - 3 to 5 | -0.18 | 0.48 | -0.38 | 0.703 | 0.912 | n.s. |
| 1 to 3 - 4 to 6 | 0.47 | 0.48 | 0.98 | 0.325 | 0.792 | n.s. |
| 2 to 4 - 3 to 5 | -0.64 | 0.49 | -1.31 | 0.189 | 0.711 | n.s. |
| 2 to 4 - 4 to 6 | 0.01 | 0.50 | 0.02 | 0.981 | 0.981 | n.s. |
| 3 to 5 - 4 to 6 | 0.66 | 0.50 | 1.32 | 0.187 | 0.711 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.74, *p* = 0.534, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.15 | 18 | = 0.885 | -0.04 [-0.46, 0.43] | negligible | n.s. |
| 1 to 3 vs 3 to 5 | -1.22 | 18 | = 0.698 | -0.24 [-0.72, 0.18] | small | n.s. |
| 1 to 3 vs 4 to 6 | 0.56 | 18 | = 0.698 | 0.13 [-0.26, 0.63] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | -0.65 | 18 | = 0.698 | -0.19 [-0.60, 0.31] | negligible | n.s. |
| 2 to 4 vs 4 to 6 | 0.66 | 18 | = 0.698 | 0.16 [-0.37, 0.56] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 2.06 | 18 | = 0.326 | 0.32 [0.03, 1.03] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 467.44, BIC = 481.62
- **2 to 4 vs 1 to 3**: *β* = -4.18, *SE* = 5.239, *z* = -0.797, *p* = 0.425
- **3 to 5 vs 1 to 3**: *β* = -1.86, *SE* = 5.491, *z* = -0.339, *p* = 0.734
- **4 to 6 vs 1 to 3**: *β* = 0.11, *SE* = 5.271, *z* = 0.020, *p* = 0.984
- **SNR**: *β* = 2.53, *SE* = 2.163, *z* = 1.171, *p* = 0.242

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 4.18 | 5.24 | 0.80 | 0.425 | 0.947 | n.s. |
| 1 to 3 - 3 to 5 | 1.86 | 5.49 | 0.34 | 0.734 | 0.985 | n.s. |
| 1 to 3 - 4 to 6 | -0.11 | 5.27 | -0.02 | 0.984 | 0.985 | n.s. |
| 2 to 4 - 3 to 5 | -2.31 | 5.11 | -0.45 | 0.650 | 0.985 | n.s. |
| 2 to 4 - 4 to 6 | -4.28 | 4.95 | -0.87 | 0.387 | 0.947 | n.s. |
| 3 to 5 - 4 to 6 | -1.97 | 5.19 | -0.38 | 0.704 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 219.94, BIC = 234.12
- **2 to 4 vs 1 to 3**: *β* = -0.07, *SE* = 0.543, *z* = -0.136, *p* = 0.892
- **3 to 5 vs 1 to 3**: *β* = 0.07, *SE* = 0.578, *z* = 0.122, *p* = 0.903
- **4 to 6 vs 1 to 3**: *β* = 0.74, *SE* = 0.544, *z* = 1.360, *p* = 0.174
- **SNR**: *β* = 0.97, *SE* = 0.237, *z* = 4.072, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | 0.07 | 0.54 | 0.14 | 0.892 | 0.990 | n.s. |
| 1 to 3 - 3 to 5 | -0.07 | 0.58 | -0.12 | 0.903 | 0.990 | n.s. |
| 1 to 3 - 4 to 6 | -0.74 | 0.54 | -1.36 | 0.174 | 0.615 | n.s. |
| 2 to 4 - 3 to 5 | -0.14 | 0.53 | -0.27 | 0.787 | 0.990 | n.s. |
| 2 to 4 - 4 to 6 | -0.81 | 0.52 | -1.58 | 0.115 | 0.519 | n.s. |
| 3 to 5 - 4 to 6 | -0.67 | 0.54 | -1.23 | 0.217 | 0.625 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 786.32, BIC = 802.35
- **2 to 4 vs 1 to 3**: *β* = 13.32, *SE* = 15.393, *z* = 0.866, *p* = 0.387
- **3 to 5 vs 1 to 3**: *β* = 17.05, *SE* = 16.443, *z* = 1.037, *p* = 0.300
- **4 to 6 vs 1 to 3**: *β* = 24.97, *SE* = 15.623, *z* = 1.598, *p* = 0.110
- **SNR**: *β* = 0.67, *SE* = 1.915, *z* = 0.348, *p* = 0.728

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -13.32 | 15.39 | -0.87 | 0.387 | 0.859 | n.s. |
| 1 to 3 - 3 to 5 | -17.04 | 16.44 | -1.04 | 0.300 | 0.832 | n.s. |
| 1 to 3 - 4 to 6 | -24.97 | 15.62 | -1.60 | 0.110 | 0.503 | n.s. |
| 2 to 4 - 3 to 5 | -3.72 | 16.74 | -0.22 | 0.824 | 0.866 | n.s. |
| 2 to 4 - 4 to 6 | -11.65 | 15.86 | -0.73 | 0.463 | 0.859 | n.s. |
| 3 to 5 - 4 to 6 | -7.93 | 16.65 | -0.48 | 0.634 | 0.866 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.17, *p* = 0.333, η²_G = 0.063
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -1.19 | 14 | = 0.504 | -0.42 [-0.72, 0.29] | small | n.s. |
| 1 to 3 vs 3 to 5 | -1.69 | 14 | = 0.504 | -0.70 [-0.83, 0.26] | medium | n.s. |
| 1 to 3 vs 4 to 6 | -1.42 | 14 | = 0.504 | -0.62 [-0.90, 0.13] | medium | n.s. |
| 2 to 4 vs 3 to 5 | -0.56 | 14 | = 0.703 | -0.23 [-0.56, 0.50] | small | n.s. |
| 2 to 4 vs 4 to 6 | -0.56 | 14 | = 0.703 | -0.19 [-0.72, 0.32] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | 0.09 | 14 | = 0.928 | 0.03 [-0.53, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 335.48, BIC = 351.51
- **2 to 4 vs 1 to 3**: *β* = 0.55, *SE* = 0.567, *z* = 0.971, *p* = 0.332
- **3 to 5 vs 1 to 3**: *β* = 0.73, *SE* = 0.613, *z* = 1.198, *p* = 0.231
- **4 to 6 vs 1 to 3**: *β* = 0.57, *SE* = 0.570, *z* = 1.009, *p* = 0.313
- **SNR**: *β* = 0.72, *SE* = 0.082, *z* = 8.785, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 4 | -0.55 | 0.57 | -0.97 | 0.332 | 0.847 | n.s. |
| 1 to 3 - 3 to 5 | -0.73 | 0.61 | -1.20 | 0.231 | 0.793 | n.s. |
| 1 to 3 - 4 to 6 | -0.58 | 0.57 | -1.01 | 0.313 | 0.847 | n.s. |
| 2 to 4 - 3 to 5 | -0.18 | 0.62 | -0.30 | 0.768 | 0.987 | n.s. |
| 2 to 4 - 4 to 6 | -0.03 | 0.58 | -0.04 | 0.965 | 0.987 | n.s. |
| 3 to 5 - 4 to 6 | 0.16 | 0.62 | 0.26 | 0.797 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.529, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 4 | -0.69 | 14 | = 0.667 | -0.21 [-0.67, 0.33] | small | n.s. |
| 1 to 3 vs 3 to 5 | 0.60 | 14 | = 0.667 | 0.18 [-0.35, 0.73] | negligible | n.s. |
| 1 to 3 vs 4 to 6 | -0.22 | 14 | = 0.830 | -0.05 [-0.56, 0.43] | negligible | n.s. |
| 2 to 4 vs 3 to 5 | 1.49 | 14 | = 0.667 | 0.38 [-0.13, 0.99] | small | n.s. |
| 2 to 4 vs 4 to 6 | 0.67 | 14 | = 0.667 | 0.17 [-0.38, 0.65] | negligible | n.s. |
| 3 to 5 vs 4 to 6 | -0.97 | 14 | = 0.667 | -0.24 [-0.81, 0.31] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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
