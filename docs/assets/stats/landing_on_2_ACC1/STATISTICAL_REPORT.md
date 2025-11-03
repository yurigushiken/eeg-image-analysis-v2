# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:44:55

---

## 1. Analysis Overview

**Total Measurements:** 480
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| 2 to 2 | 10 | 100.00 ms | 9.43 | 2.98 | [92.00, 116.00] |
| 3 to 2 | 10 | 106.40 ms | 9.83 | 3.11 | [92.00, 116.00] |
| 4 to 2 | 11 | 101.45 ms | 9.84 | 2.97 | [92.00, 116.00] |
| 5 to 2 | 7 | 112.00 ms | 7.66 | 2.89 | [96.00, 116.00] |
| increasing 1 to 2 | 13 | 104.62 ms | 9.64 | 2.67 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 10 | 2.45 µV | 1.50 | 0.47 | [0.81, 6.00] |
| 3 to 2 | 10 | 2.69 µV | 1.21 | 0.38 | [1.11, 4.23] |
| 4 to 2 | 11 | 3.40 µV | 1.84 | 0.56 | [0.57, 6.56] |
| 5 to 2 | 7 | 4.47 µV | 2.34 | 0.88 | [1.56, 9.12] |
| increasing 1 to 2 | 13 | 2.64 µV | 1.91 | 0.53 | [0.61, 5.82] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 22 | 175.09 ms | 21.91 | 4.67 | [144.00, 212.00] |
| 3 to 2 | 22 | 173.27 ms | 23.04 | 4.91 | [144.00, 212.00] |
| 4 to 2 | 24 | 178.50 ms | 15.33 | 3.13 | [148.00, 212.00] |
| 5 to 2 | 24 | 174.17 ms | 18.35 | 3.75 | [148.00, 212.00] |
| increasing 1 to 2 | 22 | 171.64 ms | 17.84 | 3.80 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 22 | -5.73 µV | 2.50 | 0.53 | [-10.50, -1.57] |
| 3 to 2 | 22 | -6.17 µV | 2.56 | 0.55 | [-10.33, -1.67] |
| 4 to 2 | 24 | -6.17 µV | 3.05 | 0.62 | [-12.20, -2.20] |
| 5 to 2 | 24 | -6.98 µV | 2.97 | 0.61 | [-11.17, -1.41] |
| increasing 1 to 2 | 22 | -5.81 µV | 2.14 | 0.46 | [-10.03, -2.38] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 13 | 112.62 ms | 7.09 | 1.97 | [104.00, 120.00] |
| 3 to 2 | 9 | 111.56 ms | 6.77 | 2.26 | [104.00, 120.00] |
| 4 to 2 | 14 | 116.00 ms | 5.66 | 1.51 | [104.00, 120.00] |
| 5 to 2 | 16 | 113.00 ms | 7.23 | 1.81 | [104.00, 120.00] |
| increasing 1 to 2 | 11 | 112.73 ms | 7.34 | 2.21 | [104.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 13 | 2.97 µV | 1.81 | 0.50 | [1.11, 7.57] |
| 3 to 2 | 9 | 2.74 µV | 1.87 | 0.62 | [0.51, 6.10] |
| 4 to 2 | 14 | 2.76 µV | 1.19 | 0.32 | [0.45, 4.59] |
| 5 to 2 | 16 | 3.08 µV | 1.56 | 0.39 | [0.75, 6.20] |
| increasing 1 to 2 | 11 | 1.75 µV | 0.80 | 0.24 | [0.48, 3.14] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 11 | 465.82 ms | 33.53 | 10.11 | [420.00, 536.00] |
| 3 to 2 | 18 | 490.00 ms | 32.12 | 7.57 | [432.00, 540.00] |
| 4 to 2 | 18 | 484.44 ms | 36.11 | 8.51 | [420.00, 536.00] |
| 5 to 2 | 18 | 477.78 ms | 37.85 | 8.92 | [420.00, 540.00] |
| increasing 1 to 2 | 17 | 481.41 ms | 43.45 | 10.54 | [420.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 2 | 11 | 4.56 µV | 2.39 | 0.72 | [1.28, 10.57] |
| 3 to 2 | 18 | 6.73 µV | 4.05 | 0.96 | [2.10, 17.81] |
| 4 to 2 | 18 | 6.00 µV | 3.62 | 0.85 | [0.66, 14.41] |
| 5 to 2 | 18 | 5.90 µV | 2.71 | 0.64 | [3.15, 13.53] |
| increasing 1 to 2 | 17 | 5.80 µV | 2.98 | 0.72 | [1.85, 11.52] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 383.01, BIC = 398.46
- **3 to 2 vs 2 to 2**: *β* = 7.45, *SE* = 3.853, *z* = 1.933, *p* = 0.053
- **4 to 2 vs 2 to 2**: *β* = 2.20, *SE* = 3.784, *z* = 0.582, *p* = 0.561
- **5 to 2 vs 2 to 2**: *β* = 12.63, *SE* = 4.222, *z* = 2.992, *p* = 0.003
- **increasing 1 to 2 vs 2 to 2**: *β* = 4.75, *SE* = 3.562, *z* = 1.334, *p* = 0.182
- **SNR**: *β* = -0.59, *SE* = 0.896, *z* = -0.655, *p* = 0.512

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -7.45 | 3.85 | -1.93 | 0.053 | 0.325 | n.s. |
| 2 to 2 - 4 to 2 | -2.20 | 3.78 | -0.58 | 0.561 | 0.841 | n.s. |
| 2 to 2 - 5 to 2 | -12.63 | 4.22 | -2.99 | 0.003 | 0.027 | * |
| 2 to 2 - increasing 1 to 2 | -4.75 | 3.56 | -1.33 | 0.182 | 0.649 | n.s. |
| 3 to 2 - 4 to 2 | 5.25 | 3.73 | 1.41 | 0.160 | 0.649 | n.s. |
| 3 to 2 - 5 to 2 | -5.18 | 4.23 | -1.23 | 0.220 | 0.649 | n.s. |
| 3 to 2 - increasing 1 to 2 | 2.69 | 3.64 | 0.74 | 0.459 | 0.841 | n.s. |
| 4 to 2 - 5 to 2 | -10.43 | 4.12 | -2.53 | 0.011 | 0.098 | n.s. |
| 4 to 2 - increasing 1 to 2 | -2.55 | 3.50 | -0.73 | 0.467 | 0.841 | n.s. |
| 5 to 2 - increasing 1 to 2 | 7.88 | 3.98 | 1.98 | 0.048 | 0.325 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 197.49, BIC = 212.94
- **3 to 2 vs 2 to 2**: *β* = -0.02, *SE* = 0.660, *z* = -0.030, *p* = 0.976
- **4 to 2 vs 2 to 2**: *β* = 0.51, *SE* = 0.636, *z* = 0.799, *p* = 0.424
- **5 to 2 vs 2 to 2**: *β* = 1.59, *SE* = 0.714, *z* = 2.228, *p* = 0.026
- **increasing 1 to 2 vs 2 to 2**: *β* = -0.03, *SE* = 0.610, *z* = -0.051, *p* = 0.960
- **SNR**: *β* = 0.63, *SE* = 0.147, *z* = 4.271, *p* < .001

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | 0.02 | 0.66 | 0.03 | 0.976 | 1.000 | n.s. |
| 2 to 2 - 4 to 2 | -0.51 | 0.64 | -0.80 | 0.424 | 0.932 | n.s. |
| 2 to 2 - 5 to 2 | -1.59 | 0.71 | -2.23 | 0.026 | 0.204 | n.s. |
| 2 to 2 - increasing 1 to 2 | 0.03 | 0.61 | 0.05 | 0.960 | 1.000 | n.s. |
| 3 to 2 - 4 to 2 | -0.53 | 0.64 | -0.83 | 0.407 | 0.932 | n.s. |
| 3 to 2 - 5 to 2 | -1.61 | 0.72 | -2.24 | 0.025 | 0.204 | n.s. |
| 3 to 2 - increasing 1 to 2 | 0.01 | 0.61 | 0.02 | 0.985 | 1.000 | n.s. |
| 4 to 2 - 5 to 2 | -1.08 | 0.69 | -1.56 | 0.119 | 0.587 | n.s. |
| 4 to 2 - increasing 1 to 2 | 0.54 | 0.59 | 0.91 | 0.361 | 0.932 | n.s. |
| 5 to 2 - increasing 1 to 2 | 1.62 | 0.68 | 2.40 | 0.016 | 0.153 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 992.79, BIC = 1014.68
- **3 to 2 vs 2 to 2**: *β* = 0.04, *SE* = 4.769, *z* = 0.008, *p* = 0.993
- **4 to 2 vs 2 to 2**: *β* = 4.10, *SE* = 4.581, *z* = 0.896, *p* = 0.370
- **5 to 2 vs 2 to 2**: *β* = 0.35, *SE* = 4.777, *z* = 0.074, *p* = 0.941
- **increasing 1 to 2 vs 2 to 2**: *β* = -1.96, *SE* = 4.738, *z* = -0.413, *p* = 0.680
- **SNR**: *β* = -0.38, *SE* = 0.736, *z* = -0.509, *p* = 0.611

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -0.04 | 4.77 | -0.01 | 0.993 | 1.000 | n.s. |
| 2 to 2 - 4 to 2 | -4.10 | 4.58 | -0.90 | 0.370 | 0.984 | n.s. |
| 2 to 2 - 5 to 2 | -0.35 | 4.78 | -0.07 | 0.941 | 1.000 | n.s. |
| 2 to 2 - increasing 1 to 2 | 1.96 | 4.74 | 0.41 | 0.680 | 0.997 | n.s. |
| 3 to 2 - 4 to 2 | -4.06 | 4.63 | -0.88 | 0.380 | 0.984 | n.s. |
| 3 to 2 - 5 to 2 | -0.31 | 4.60 | -0.07 | 0.945 | 1.000 | n.s. |
| 3 to 2 - increasing 1 to 2 | 2.00 | 4.70 | 0.42 | 0.671 | 0.997 | n.s. |
| 4 to 2 - 5 to 2 | 3.75 | 4.60 | 0.81 | 0.415 | 0.984 | n.s. |
| 4 to 2 - increasing 1 to 2 | 6.06 | 4.59 | 1.32 | 0.187 | 0.874 | n.s. |
| 5 to 2 - increasing 1 to 2 | 2.31 | 4.63 | 0.50 | 0.618 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.95, *p* = 0.440, η²_G = 0.027
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 0.96 | 18 | = 0.585 | 0.25 [-0.50, 0.41] | small | n.s. |
| 2 to 2 vs 4 to 2 | -0.29 | 18 | = 0.858 | -0.08 [-0.61, 0.29] | negligible | n.s. |
| 2 to 2 vs 5 to 2 | 1.16 | 18 | = 0.526 | 0.22 [-0.47, 0.42] | small | n.s. |
| 2 to 2 vs increasing 1 to 2 | 1.34 | 18 | = 0.526 | 0.30 [-0.17, 0.79] | small | n.s. |
| 3 to 2 vs 4 to 2 | -1.55 | 18 | = 0.526 | -0.38 [-0.60, 0.29] | small | n.s. |
| 3 to 2 vs 5 to 2 | -0.19 | 18 | = 0.858 | -0.06 [-0.48, 0.40] | negligible | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.18 | 18 | = 0.858 | 0.03 [-0.49, 0.44] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.17 | 18 | = 0.526 | 0.36 [-0.23, 0.62] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.55 | 18 | = 0.526 | 0.46 [-0.07, 0.85] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.33 | 18 | = 0.858 | 0.10 [-0.45, 0.43] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 481.84, BIC = 503.73
- **3 to 2 vs 2 to 2**: *β* = 0.11, *SE* = 0.478, *z* = 0.224, *p* = 0.823
- **4 to 2 vs 2 to 2**: *β* = -0.45, *SE* = 0.458, *z* = -0.990, *p* = 0.322
- **5 to 2 vs 2 to 2**: *β* = -0.58, *SE* = 0.481, *z* = -1.198, *p* = 0.231
- **increasing 1 to 2 vs 2 to 2**: *β* = 0.20, *SE* = 0.474, *z* = 0.427, *p* = 0.670
- **SNR**: *β* = -0.44, *SE* = 0.078, *z* = -5.658, *p* < .001

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -0.11 | 0.48 | -0.22 | 0.823 | 0.991 | n.s. |
| 2 to 2 - 4 to 2 | 0.45 | 0.46 | 0.99 | 0.322 | 0.857 | n.s. |
| 2 to 2 - 5 to 2 | 0.58 | 0.48 | 1.20 | 0.231 | 0.834 | n.s. |
| 2 to 2 - increasing 1 to 2 | -0.20 | 0.47 | -0.43 | 0.670 | 0.988 | n.s. |
| 3 to 2 - 4 to 2 | 0.56 | 0.46 | 1.21 | 0.226 | 0.834 | n.s. |
| 3 to 2 - 5 to 2 | 0.68 | 0.46 | 1.49 | 0.137 | 0.734 | n.s. |
| 3 to 2 - increasing 1 to 2 | -0.10 | 0.47 | -0.20 | 0.839 | 0.991 | n.s. |
| 4 to 2 - 5 to 2 | 0.12 | 0.46 | 0.27 | 0.789 | 0.991 | n.s. |
| 4 to 2 - increasing 1 to 2 | -0.66 | 0.46 | -1.43 | 0.153 | 0.735 | n.s. |
| 5 to 2 - increasing 1 to 2 | -0.78 | 0.46 | -1.68 | 0.093 | 0.622 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.84, *p* = 0.030, η²_G = 0.048
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 1.42 | 18 | = 0.344 | 0.29 [-0.12, 0.81] | small | n.s. |
| 2 to 2 vs 4 to 2 | 1.74 | 18 | = 0.271 | 0.40 [-0.25, 0.65] | small | n.s. |
| 2 to 2 vs 5 to 2 | 3.04 | 18 | = 0.071 | 0.63 [0.03, 0.97] | medium | n.s. |
| 2 to 2 vs increasing 1 to 2 | 1.08 | 18 | = 0.418 | 0.19 [-0.35, 0.59] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | 0.61 | 18 | = 0.550 | 0.13 [-0.33, 0.56] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 1.69 | 18 | = 0.271 | 0.35 [0.00, 0.94] | small | n.s. |
| 3 to 2 vs increasing 1 to 2 | -0.79 | 18 | = 0.489 | -0.13 [-0.65, 0.30] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 0.92 | 18 | = 0.465 | 0.20 [-0.13, 0.73] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | -1.15 | 18 | = 0.418 | -0.26 [-0.66, 0.24] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -2.69 | 18 | = 0.075 | -0.50 [-1.00, -0.06] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 410.46, BIC = 427.61
- **3 to 2 vs 2 to 2**: *β* = 1.37, *SE* = 1.911, *z* = 0.715, *p* = 0.475
- **4 to 2 vs 2 to 2**: *β* = 3.96, *SE* = 1.664, *z* = 2.377, *p* = 0.017
- **5 to 2 vs 2 to 2**: *β* = -0.90, *SE* = 1.621, *z* = -0.553, *p* = 0.580
- **increasing 1 to 2 vs 2 to 2**: *β* = 1.89, *SE* = 1.787, *z* = 1.056, *p* = 0.291
- **SNR**: *β* = -0.04, *SE* = 0.496, *z* = -0.070, *p* = 0.944

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -1.37 | 1.91 | -0.71 | 0.475 | 0.855 | n.s. |
| 2 to 2 - 4 to 2 | -3.96 | 1.66 | -2.38 | 0.017 | 0.147 | n.s. |
| 2 to 2 - 5 to 2 | 0.90 | 1.62 | 0.55 | 0.580 | 0.855 | n.s. |
| 2 to 2 - increasing 1 to 2 | -1.89 | 1.79 | -1.06 | 0.291 | 0.798 | n.s. |
| 3 to 2 - 4 to 2 | -2.59 | 1.88 | -1.38 | 0.169 | 0.726 | n.s. |
| 3 to 2 - 5 to 2 | 2.26 | 1.90 | 1.19 | 0.234 | 0.798 | n.s. |
| 3 to 2 - increasing 1 to 2 | -0.52 | 1.96 | -0.27 | 0.790 | 0.855 | n.s. |
| 4 to 2 - 5 to 2 | 4.85 | 1.63 | 2.98 | 0.003 | 0.029 | * |
| 4 to 2 - increasing 1 to 2 | 2.07 | 1.74 | 1.19 | 0.234 | 0.798 | n.s. |
| 5 to 2 - increasing 1 to 2 | -2.78 | 1.78 | -1.56 | 0.118 | 0.633 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.04, *p* = 0.418, η²_G = 0.092
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 0.00 | 4 | = 1.000 | 0.00 [-1.22, 0.67] | negligible | n.s. |
| 2 to 2 vs 4 to 2 | -0.78 | 4 | = 0.905 | -0.33 [-1.42, 0.15] | small | n.s. |
| 2 to 2 vs 5 to 2 | 2.24 | 4 | = 0.674 | 0.63 [-0.51, 0.84] | medium | n.s. |
| 2 to 2 vs increasing 1 to 2 | 0.25 | 4 | = 0.905 | 0.12 [-0.92, 0.76] | negligible | n.s. |
| 3 to 2 vs 4 to 2 | -0.49 | 4 | = 0.905 | -0.28 [-1.36, 0.56] | small | n.s. |
| 3 to 2 vs 5 to 2 | 1.20 | 4 | = 0.745 | 0.57 [-0.45, 1.54] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | 0.34 | 4 | = 0.905 | 0.11 [-0.91, 1.20] | negligible | n.s. |
| 4 to 2 vs 5 to 2 | 1.87 | 4 | = 0.674 | 0.84 [0.10, 1.69] | large | n.s. |
| 4 to 2 vs increasing 1 to 2 | 0.65 | 4 | = 0.905 | 0.35 [-0.43, 1.16] | small | n.s. |
| 5 to 2 vs increasing 1 to 2 | -1.37 | 4 | = 0.745 | -0.40 [-2.20, -0.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 199.33, BIC = 216.48
- **3 to 2 vs 2 to 2**: *β* = -0.34, *SE* = 0.418, *z* = -0.801, *p* = 0.423
- **4 to 2 vs 2 to 2**: *β* = -0.26, *SE* = 0.369, *z* = -0.717, *p* = 0.474
- **5 to 2 vs 2 to 2**: *β* = -0.20, *SE* = 0.360, *z* = -0.545, *p* = 0.585
- **increasing 1 to 2 vs 2 to 2**: *β* = -0.98, *SE* = 0.396, *z* = -2.485, *p* = 0.013
- **SNR**: *β* = 0.78, *SE* = 0.104, *z* = 7.498, *p* < .001

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | 0.33 | 0.42 | 0.80 | 0.423 | 0.963 | n.s. |
| 2 to 2 - 4 to 2 | 0.26 | 0.37 | 0.72 | 0.474 | 0.963 | n.s. |
| 2 to 2 - 5 to 2 | 0.20 | 0.36 | 0.55 | 0.585 | 0.970 | n.s. |
| 2 to 2 - increasing 1 to 2 | 0.98 | 0.40 | 2.48 | 0.013 | 0.122 | n.s. |
| 3 to 2 - 4 to 2 | -0.07 | 0.41 | -0.17 | 0.864 | 0.981 | n.s. |
| 3 to 2 - 5 to 2 | -0.14 | 0.41 | -0.34 | 0.733 | 0.981 | n.s. |
| 3 to 2 - increasing 1 to 2 | 0.65 | 0.44 | 1.49 | 0.136 | 0.641 | n.s. |
| 4 to 2 - 5 to 2 | -0.07 | 0.35 | -0.19 | 0.847 | 0.981 | n.s. |
| 4 to 2 - increasing 1 to 2 | 0.72 | 0.39 | 1.86 | 0.063 | 0.405 | n.s. |
| 5 to 2 - increasing 1 to 2 | 0.79 | 0.39 | 2.04 | 0.041 | 0.314 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.37, *p* = 0.289, η²_G = 0.212
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | 1.02 | 4 | = 0.609 | 0.67 [-0.93, 0.92] | medium | n.s. |
| 2 to 2 vs 4 to 2 | 0.87 | 4 | = 0.621 | 0.49 [-0.74, 0.69] | small | n.s. |
| 2 to 2 vs 5 to 2 | 0.23 | 4 | = 0.829 | 0.17 [-0.61, 0.74] | negligible | n.s. |
| 2 to 2 vs increasing 1 to 2 | 1.70 | 4 | = 0.421 | 1.15 [-0.16, 1.77] | large | n.s. |
| 3 to 2 vs 4 to 2 | -0.44 | 4 | = 0.760 | -0.34 [-0.89, 0.96] | small | n.s. |
| 3 to 2 vs 5 to 2 | -2.17 | 4 | = 0.421 | -0.62 [-1.71, 0.35] | medium | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.68 | 4 | = 0.421 | 0.63 [-0.72, 1.44] | medium | n.s. |
| 4 to 2 vs 5 to 2 | -0.61 | 4 | = 0.722 | -0.40 [-1.10, 0.30] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.49 | 4 | = 0.423 | 1.24 [-0.29, 1.35] | large | n.s. |
| 5 to 2 vs increasing 1 to 2 | 2.71 | 4 | = 0.421 | 1.31 [0.17, 2.17] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 825.61, BIC = 844.86
- **3 to 2 vs 2 to 2**: *β* = 19.32, *SE* = 11.678, *z* = 1.654, *p* = 0.098
- **4 to 2 vs 2 to 2**: *β* = 14.93, *SE* = 11.605, *z* = 1.286, *p* = 0.198
- **5 to 2 vs 2 to 2**: *β* = 4.56, *SE* = 12.320, *z* = 0.370, *p* = 0.712
- **increasing 1 to 2 vs 2 to 2**: *β* = 9.33, *SE* = 12.055, *z* = 0.774, *p* = 0.439
- **SNR**: *β* = 1.28, *SE* = 1.577, *z* = 0.814, *p* = 0.415

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -19.32 | 11.68 | -1.65 | 0.098 | 0.644 | n.s. |
| 2 to 2 - 4 to 2 | -14.93 | 11.60 | -1.29 | 0.198 | 0.829 | n.s. |
| 2 to 2 - 5 to 2 | -4.56 | 12.32 | -0.37 | 0.712 | 0.970 | n.s. |
| 2 to 2 - increasing 1 to 2 | -9.33 | 12.05 | -0.77 | 0.439 | 0.944 | n.s. |
| 3 to 2 - 4 to 2 | 4.39 | 9.90 | 0.44 | 0.657 | 0.970 | n.s. |
| 3 to 2 - 5 to 2 | 14.76 | 10.20 | 1.45 | 0.148 | 0.763 | n.s. |
| 3 to 2 - increasing 1 to 2 | 9.99 | 10.23 | 0.98 | 0.329 | 0.931 | n.s. |
| 4 to 2 - 5 to 2 | 10.37 | 10.36 | 1.00 | 0.317 | 0.931 | n.s. |
| 4 to 2 - increasing 1 to 2 | 5.60 | 10.25 | 0.55 | 0.585 | 0.970 | n.s. |
| 5 to 2 - increasing 1 to 2 | -4.77 | 10.44 | -0.46 | 0.648 | 0.970 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.45, *p* = 0.256, η²_G = 0.134
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | -1.16 | 5 | = 0.518 | -0.42 [-1.38, 0.18] | small | n.s. |
| 2 to 2 vs 4 to 2 | -2.18 | 5 | = 0.404 | -0.50 [-1.08, 0.39] | medium | n.s. |
| 2 to 2 vs 5 to 2 | -0.52 | 5 | = 0.811 | -0.33 [-0.97, 0.48] | small | n.s. |
| 2 to 2 vs increasing 1 to 2 | 1.16 | 5 | = 0.518 | 0.44 [-0.80, 0.87] | small | n.s. |
| 3 to 2 vs 4 to 2 | -0.25 | 5 | = 0.811 | -0.08 [-0.42, 0.65] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 0.27 | 5 | = 0.811 | 0.12 [-0.26, 0.82] | negligible | n.s. |
| 3 to 2 vs increasing 1 to 2 | 1.89 | 5 | = 0.404 | 0.91 [-0.33, 0.90] | large | n.s. |
| 4 to 2 vs 5 to 2 | 0.44 | 5 | = 0.811 | 0.21 [-0.20, 0.89] | small | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.86 | 5 | = 0.404 | 1.00 [-0.34, 0.89] | large | n.s. |
| 5 to 2 vs increasing 1 to 2 | 1.13 | 5 | = 0.518 | 0.83 [-0.55, 0.61] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 371.84, BIC = 391.10
- **3 to 2 vs 2 to 2**: *β* = 1.66, *SE* = 0.695, *z* = 2.386, *p* = 0.017
- **4 to 2 vs 2 to 2**: *β* = 1.32, *SE* = 0.691, *z* = 1.910, *p* = 0.056
- **5 to 2 vs 2 to 2**: *β* = -0.19, *SE* = 0.737, *z* = -0.260, *p* = 0.795
- **increasing 1 to 2 vs 2 to 2**: *β* = 0.61, *SE* = 0.717, *z* = 0.847, *p* = 0.397
- **SNR**: *β* = 0.64, *SE* = 0.102, *z* = 6.307, *p* < .001

_Reference condition: **2 to 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 2 - 3 to 2 | -1.66 | 0.69 | -2.39 | 0.017 | 0.128 | n.s. |
| 2 to 2 - 4 to 2 | -1.32 | 0.69 | -1.91 | 0.056 | 0.333 | n.s. |
| 2 to 2 - 5 to 2 | 0.19 | 0.74 | 0.26 | 0.795 | 0.810 | n.s. |
| 2 to 2 - increasing 1 to 2 | -0.61 | 0.72 | -0.85 | 0.397 | 0.781 | n.s. |
| 3 to 2 - 4 to 2 | 0.34 | 0.59 | 0.58 | 0.565 | 0.810 | n.s. |
| 3 to 2 - 5 to 2 | 1.85 | 0.61 | 3.05 | 0.002 | 0.023 | * |
| 3 to 2 - increasing 1 to 2 | 1.05 | 0.61 | 1.73 | 0.084 | 0.410 | n.s. |
| 4 to 2 - 5 to 2 | 1.51 | 0.62 | 2.45 | 0.014 | 0.121 | n.s. |
| 4 to 2 - increasing 1 to 2 | 0.71 | 0.61 | 1.17 | 0.242 | 0.673 | n.s. |
| 5 to 2 - increasing 1 to 2 | -0.80 | 0.62 | -1.28 | 0.200 | 0.673 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.14, *p* = 0.013, η²_G = 0.202
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 2 vs 3 to 2 | -3.51 | 5 | = 0.086 | -1.30 [-1.58, 0.05] | large | n.s. |
| 2 to 2 vs 4 to 2 | -2.38 | 5 | = 0.158 | -0.89 [-1.68, -0.01] | large | n.s. |
| 2 to 2 vs 5 to 2 | -1.09 | 5 | = 0.467 | -0.58 [-1.32, 0.22] | medium | n.s. |
| 2 to 2 vs increasing 1 to 2 | -0.72 | 5 | = 0.560 | -0.31 [-1.23, 0.49] | small | n.s. |
| 3 to 2 vs 4 to 2 | 0.28 | 5 | = 0.790 | 0.07 [-0.28, 0.80] | negligible | n.s. |
| 3 to 2 vs 5 to 2 | 2.66 | 5 | = 0.149 | 0.81 [-0.13, 0.98] | large | n.s. |
| 3 to 2 vs increasing 1 to 2 | 4.31 | 5 | = 0.076 | 1.08 [-0.29, 0.96] | large | n.s. |
| 4 to 2 vs 5 to 2 | 1.58 | 5 | = 0.291 | 0.51 [-0.38, 0.70] | medium | n.s. |
| 4 to 2 vs increasing 1 to 2 | 1.89 | 5 | = 0.235 | 0.70 [-0.36, 0.87] | medium | n.s. |
| 5 to 2 vs increasing 1 to 2 | 0.77 | 5 | = 0.560 | 0.30 [-0.47, 0.69] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.030) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.013) (no significant pairwise comparisons)

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
