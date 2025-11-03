# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:37:22

---

## 1. Analysis Overview

**Total Measurements:** 448
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
| 2 to 1 | 17 | 109.65 ms | 8.01 | 1.94 | [96.00, 116.00] |
| 3 to 2 | 14 | 105.43 ms | 8.39 | 2.24 | [96.00, 116.00] |
| 4 to 3 | 11 | 104.36 ms | 6.05 | 1.83 | [96.00, 116.00] |
| 5 to 4 | 17 | 106.12 ms | 7.23 | 1.75 | [96.00, 116.00] |
| 6 to 5 | 8 | 108.50 ms | 7.84 | 2.77 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | -2.66 µV | 1.59 | 0.39 | [-5.91, -0.16] |
| 3 to 2 | 14 | -2.76 µV | 1.68 | 0.45 | [-5.62, -0.69] |
| 4 to 3 | 11 | -2.25 µV | 1.74 | 0.52 | [-6.08, -0.30] |
| 5 to 4 | 17 | -2.96 µV | 2.28 | 0.55 | [-8.72, -0.40] |
| 6 to 5 | 8 | -2.36 µV | 0.94 | 0.33 | [-4.24, -1.12] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 15 | 180.80 ms | 13.62 | 3.52 | [160.00, 212.00] |
| 3 to 2 | 22 | 173.27 ms | 23.04 | 4.91 | [144.00, 212.00] |
| 4 to 3 | 23 | 174.43 ms | 18.12 | 3.78 | [152.00, 212.00] |
| 5 to 4 | 22 | 176.18 ms | 20.78 | 4.43 | [144.00, 212.00] |
| 6 to 5 | 15 | 178.93 ms | 23.40 | 6.04 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 15 | -5.49 µV | 2.53 | 0.65 | [-10.79, -2.73] |
| 3 to 2 | 22 | -6.17 µV | 2.56 | 0.55 | [-10.33, -1.67] |
| 4 to 3 | 23 | -6.36 µV | 2.25 | 0.47 | [-10.92, -1.44] |
| 5 to 4 | 22 | -6.24 µV | 2.95 | 0.63 | [-14.15, -1.51] |
| 6 to 5 | 15 | -7.60 µV | 2.03 | 0.52 | [-10.73, -4.01] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 115.53 ms | 6.62 | 1.60 | [100.00, 120.00] |
| 3 to 2 | 9 | 108.89 ms | 7.42 | 2.47 | [100.00, 120.00] |
| 4 to 3 | 11 | 108.73 ms | 8.16 | 2.46 | [100.00, 120.00] |
| 5 to 4 | 16 | 111.50 ms | 7.14 | 1.78 | [100.00, 120.00] |
| 6 to 5 | 4 | 115.00 ms | 3.83 | 1.91 | [112.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | 4.46 µV | 2.44 | 0.59 | [1.50, 9.13] |
| 3 to 2 | 9 | 2.80 µV | 1.91 | 0.64 | [0.54, 6.10] |
| 4 to 3 | 11 | 2.63 µV | 1.48 | 0.45 | [0.60, 5.30] |
| 5 to 4 | 16 | 2.95 µV | 1.80 | 0.45 | [0.70, 6.01] |
| 6 to 5 | 4 | 3.72 µV | 1.85 | 0.93 | [1.90, 6.31] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 22 | 511.27 ms | 36.32 | 7.74 | [440.00, 556.00] |
| 3 to 2 | 17 | 497.41 ms | 34.70 | 8.42 | [440.00, 556.00] |
| 4 to 3 | 19 | 486.11 ms | 30.59 | 7.02 | [444.00, 544.00] |
| 5 to 4 | 21 | 499.62 ms | 34.10 | 7.44 | [440.00, 556.00] |
| 6 to 5 | 11 | 523.27 ms | 42.02 | 12.67 | [448.00, 556.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 22 | 6.02 µV | 3.18 | 0.68 | [1.72, 11.21] |
| 3 to 2 | 17 | 7.12 µV | 3.94 | 0.96 | [2.10, 17.81] |
| 4 to 3 | 19 | 6.14 µV | 2.98 | 0.68 | [1.06, 11.65] |
| 5 to 4 | 21 | 6.25 µV | 2.87 | 0.63 | [2.51, 11.69] |
| 6 to 5 | 11 | 6.78 µV | 2.14 | 0.65 | [2.47, 10.24] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 472.43, BIC = 490.07
- **3 to 2 vs 2 to 1**: *β* = -4.19, *SE* = 2.604, *z* = -1.610, *p* = 0.107
- **4 to 3 vs 2 to 1**: *β* = -5.24, *SE* = 2.797, *z* = -1.873, *p* = 0.061
- **5 to 4 vs 2 to 1**: *β* = -3.49, *SE* = 2.473, *z* = -1.410, *p* = 0.159
- **6 to 5 vs 2 to 1**: *β* = -0.91, *SE* = 3.153, *z* = -0.289, *p* = 0.773
- **SNR**: *β* = 0.15, *SE* = 0.581, *z* = 0.252, *p* = 0.801

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 4.19 | 2.60 | 1.61 | 0.107 | 0.640 | n.s. |
| 2 to 1 - 4 to 3 | 5.24 | 2.80 | 1.87 | 0.061 | 0.467 | n.s. |
| 2 to 1 - 5 to 4 | 3.49 | 2.47 | 1.41 | 0.159 | 0.749 | n.s. |
| 2 to 1 - 6 to 5 | 0.91 | 3.15 | 0.29 | 0.773 | 0.978 | n.s. |
| 3 to 2 - 4 to 3 | 1.05 | 2.91 | 0.36 | 0.719 | 0.978 | n.s. |
| 3 to 2 - 5 to 4 | -0.71 | 2.61 | -0.27 | 0.786 | 0.978 | n.s. |
| 3 to 2 - 6 to 5 | -3.28 | 3.25 | -1.01 | 0.313 | 0.895 | n.s. |
| 4 to 3 - 5 to 4 | -1.75 | 2.79 | -0.63 | 0.530 | 0.951 | n.s. |
| 4 to 3 - 6 to 5 | -4.33 | 3.41 | -1.27 | 0.204 | 0.797 | n.s. |
| 5 to 4 - 6 to 5 | -2.58 | 3.14 | -0.82 | 0.412 | 0.930 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 231.35, BIC = 248.99
- **3 to 2 vs 2 to 1**: *β* = -0.06, *SE* = 0.410, *z* = -0.139, *p* = 0.890
- **4 to 3 vs 2 to 1**: *β* = 0.23, *SE* = 0.438, *z* = 0.526, *p* = 0.599
- **5 to 4 vs 2 to 1**: *β* = -0.50, *SE* = 0.385, *z* = -1.303, *p* = 0.193
- **6 to 5 vs 2 to 1**: *β* = -0.32, *SE* = 0.488, *z* = -0.656, *p* = 0.512
- **SNR**: *β* = -0.76, *SE* = 0.097, *z* = -7.906, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.06 | 0.41 | 0.14 | 0.890 | 0.986 | n.s. |
| 2 to 1 - 4 to 3 | -0.23 | 0.44 | -0.53 | 0.599 | 0.986 | n.s. |
| 2 to 1 - 5 to 4 | 0.50 | 0.38 | 1.30 | 0.193 | 0.854 | n.s. |
| 2 to 1 - 6 to 5 | 0.32 | 0.49 | 0.66 | 0.512 | 0.986 | n.s. |
| 3 to 2 - 4 to 3 | -0.29 | 0.46 | -0.63 | 0.528 | 0.986 | n.s. |
| 3 to 2 - 5 to 4 | 0.44 | 0.41 | 1.08 | 0.281 | 0.929 | n.s. |
| 3 to 2 - 6 to 5 | 0.26 | 0.52 | 0.51 | 0.611 | 0.986 | n.s. |
| 4 to 3 - 5 to 4 | 0.73 | 0.44 | 1.66 | 0.096 | 0.637 | n.s. |
| 4 to 3 - 6 to 5 | 0.55 | 0.54 | 1.02 | 0.307 | 0.929 | n.s. |
| 5 to 4 - 6 to 5 | -0.18 | 0.49 | -0.37 | 0.711 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 847.89, BIC = 868.48
- **3 to 2 vs 2 to 1**: *β* = -4.87, *SE* = 5.174, *z* = -0.942, *p* = 0.346
- **4 to 3 vs 2 to 1**: *β* = -5.37, *SE* = 5.159, *z* = -1.040, *p* = 0.298
- **5 to 4 vs 2 to 1**: *β* = -1.41, *SE* = 5.164, *z* = -0.274, *p* = 0.784
- **6 to 5 vs 2 to 1**: *β* = -1.94, *SE* = 5.588, *z* = -0.347, *p* = 0.729
- **SNR**: *β* = -0.53, *SE* = 0.698, *z* = -0.753, *p* = 0.451

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 4.87 | 5.17 | 0.94 | 0.346 | 0.978 | n.s. |
| 2 to 1 - 4 to 3 | 5.37 | 5.16 | 1.04 | 0.298 | 0.971 | n.s. |
| 2 to 1 - 5 to 4 | 1.41 | 5.16 | 0.27 | 0.784 | 0.995 | n.s. |
| 2 to 1 - 6 to 5 | 1.94 | 5.59 | 0.35 | 0.729 | 0.995 | n.s. |
| 3 to 2 - 4 to 3 | 0.49 | 4.46 | 0.11 | 0.912 | 0.995 | n.s. |
| 3 to 2 - 5 to 4 | -3.46 | 4.49 | -0.77 | 0.441 | 0.983 | n.s. |
| 3 to 2 - 6 to 5 | -2.94 | 5.14 | -0.57 | 0.568 | 0.985 | n.s. |
| 4 to 3 - 5 to 4 | -3.95 | 4.47 | -0.88 | 0.376 | 0.978 | n.s. |
| 4 to 3 - 6 to 5 | -3.43 | 5.09 | -0.67 | 0.500 | 0.984 | n.s. |
| 5 to 4 - 6 to 5 | 0.52 | 5.14 | 0.10 | 0.919 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.651, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.64 | 8 | = 0.911 | 0.22 [-0.23, 0.96] | small | n.s. |
| 2 to 1 vs 4 to 3 | 2.30 | 8 | = 0.252 | 0.60 [-0.08, 1.15] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 0.12 | 8 | = 0.911 | 0.04 [-0.51, 0.65] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | -0.17 | 8 | = 0.911 | -0.05 [-0.77, 0.66] | negligible | n.s. |
| 3 to 2 vs 4 to 3 | 0.54 | 8 | = 0.911 | 0.22 [-0.40, 0.51] | small | n.s. |
| 3 to 2 vs 5 to 4 | -0.29 | 8 | = 0.911 | -0.13 [-0.59, 0.33] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -0.52 | 8 | = 0.911 | -0.22 [-0.55, 0.60] | small | n.s. |
| 4 to 3 vs 5 to 4 | -1.47 | 8 | = 0.601 | -0.35 [-0.78, 0.16] | small | n.s. |
| 4 to 3 vs 6 to 5 | -2.34 | 8 | = 0.252 | -0.49 [-0.97, 0.18] | small | n.s. |
| 5 to 4 vs 6 to 5 | -0.34 | 8 | = 0.911 | -0.07 [-0.58, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 417.52, BIC = 438.12
- **3 to 2 vs 2 to 1**: *β* = -0.48, *SE* = 0.577, *z* = -0.836, *p* = 0.403
- **4 to 3 vs 2 to 1**: *β* = -0.76, *SE* = 0.578, *z* = -1.318, *p* = 0.188
- **5 to 4 vs 2 to 1**: *β* = -0.72, *SE* = 0.579, *z* = -1.242, *p* = 0.214
- **6 to 5 vs 2 to 1**: *β* = -2.52, *SE* = 0.623, *z* = -4.049, *p* < .001
- **SNR**: *β* = -0.46, *SE* = 0.076, *z* = -6.017, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.48 | 0.58 | 0.84 | 0.403 | 0.873 | n.s. |
| 2 to 1 - 4 to 3 | 0.76 | 0.58 | 1.32 | 0.188 | 0.712 | n.s. |
| 2 to 1 - 5 to 4 | 0.72 | 0.58 | 1.24 | 0.214 | 0.712 | n.s. |
| 2 to 1 - 6 to 5 | 2.52 | 0.62 | 4.05 | < .001 | < .001 | *** |
| 3 to 2 - 4 to 3 | 0.28 | 0.49 | 0.56 | 0.572 | 0.922 | n.s. |
| 3 to 2 - 5 to 4 | 0.24 | 0.50 | 0.47 | 0.635 | 0.922 | n.s. |
| 3 to 2 - 6 to 5 | 2.04 | 0.57 | 3.58 | < .001 | 0.003 | ** |
| 4 to 3 - 5 to 4 | -0.04 | 0.49 | -0.09 | 0.932 | 0.932 | n.s. |
| 4 to 3 - 6 to 5 | 1.76 | 0.56 | 3.13 | 0.002 | 0.012 | * |
| 5 to 4 - 6 to 5 | 1.80 | 0.57 | 3.17 | 0.002 | 0.012 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.45, *p* = 0.066, η²_G = 0.151
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 3.05 | 8 | = 0.080 | 0.91 [0.20, 1.56] | large | n.s. |
| 2 to 1 vs 4 to 3 | 1.87 | 8 | = 0.259 | 0.81 [-0.06, 1.19] | large | n.s. |
| 2 to 1 vs 5 to 4 | 1.84 | 8 | = 0.259 | 0.89 [-0.11, 1.11] | large | n.s. |
| 2 to 1 vs 6 to 5 | 3.59 | 8 | = 0.070 | 1.46 [0.15, 1.93] | large | n.s. |
| 3 to 2 vs 4 to 3 | -0.30 | 8 | = 0.775 | -0.14 [-0.28, 0.64] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.35 | 8 | = 0.775 | 0.12 [-0.35, 0.56] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 1.10 | 8 | = 0.508 | 0.37 [0.10, 1.40] | small | n.s. |
| 4 to 3 vs 5 to 4 | 0.63 | 8 | = 0.775 | 0.25 [-0.47, 0.44] | small | n.s. |
| 4 to 3 vs 6 to 5 | 1.33 | 8 | = 0.438 | 0.54 [-0.13, 1.03] | medium | n.s. |
| 5 to 4 vs 6 to 5 | 0.44 | 8 | = 0.775 | 0.18 [-0.21, 0.99] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 393.79, BIC = 410.14
- **3 to 2 vs 2 to 1**: *β* = -6.02, *SE* = 2.734, *z* = -2.203, *p* = 0.028
- **4 to 3 vs 2 to 1**: *β* = -6.76, *SE* = 2.577, *z* = -2.624, *p* = 0.009
- **5 to 4 vs 2 to 1**: *β* = -3.90, *SE* = 2.347, *z* = -1.661, *p* = 0.097
- **6 to 5 vs 2 to 1**: *β* = -1.47, *SE* = 3.858, *z* = -0.382, *p* = 0.703
- **SNR**: *β* = 0.29, *SE* = 0.397, *z* = 0.725, *p* = 0.468

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 6.02 | 2.73 | 2.20 | 0.028 | 0.223 | n.s. |
| 2 to 1 - 4 to 3 | 6.76 | 2.58 | 2.62 | 0.009 | 0.084 | n.s. |
| 2 to 1 - 5 to 4 | 3.90 | 2.35 | 1.66 | 0.097 | 0.556 | n.s. |
| 2 to 1 - 6 to 5 | 1.47 | 3.86 | 0.38 | 0.703 | 0.912 | n.s. |
| 3 to 2 - 4 to 3 | 0.74 | 2.86 | 0.26 | 0.796 | 0.912 | n.s. |
| 3 to 2 - 5 to 4 | -2.12 | 2.66 | -0.80 | 0.425 | 0.891 | n.s. |
| 3 to 2 - 6 to 5 | -4.55 | 3.97 | -1.15 | 0.251 | 0.809 | n.s. |
| 4 to 3 - 5 to 4 | -2.86 | 2.44 | -1.17 | 0.241 | 0.809 | n.s. |
| 4 to 3 - 6 to 5 | -5.29 | 3.75 | -1.41 | 0.159 | 0.702 | n.s. |
| 5 to 4 - 6 to 5 | -2.43 | 3.63 | -0.67 | 0.503 | 0.891 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.91, *p* = 0.163, η²_G = 0.585
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.50 | 1 | = 0.783 | 0.63 [-0.23, 1.92] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 2.33 | 1 | = 0.625 | 3.13 [-0.29, 1.54] | large | n.s. |
| 2 to 1 vs 5 to 4 | 1.00 | 1 | = 0.625 | 1.34 [-0.08, 1.30] | large | n.s. |
| 2 to 1 vs 6 to 5 | 1.00 | 1 | = 0.625 | 1.41 [-2.11, 3.26] | large | n.s. |
| 3 to 2 vs 4 to 3 | 5.00 | 1 | = 0.419 | 1.39 [-0.47, 1.88] | large | n.s. |
| 3 to 2 vs 5 to 4 | 1.00 | 1 | = 0.625 | 0.28 [-0.92, 0.92] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.00 | 1 | = 1.000 | 0.00 [-2.48, 2.48] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -inf | 1 | < .001 | -1.41 [-1.33, 0.21] | large | *** |
| 4 to 3 vs 6 to 5 | -5.00 | 1 | = 0.419 | -2.24 [-1.97, 1.30] | large | n.s. |
| 5 to 4 vs 6 to 5 | -1.00 | 1 | = 0.625 | -0.45 [-2.19, 1.19] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 214.44, BIC = 230.78
- **3 to 2 vs 2 to 1**: *β* = -1.20, *SE* = 0.542, *z* = -2.212, *p* = 0.027
- **4 to 3 vs 2 to 1**: *β* = -1.44, *SE* = 0.511, *z* = -2.814, *p* = 0.005
- **5 to 4 vs 2 to 1**: *β* = -0.95, *SE* = 0.463, *z* = -2.057, *p* = 0.040
- **6 to 5 vs 2 to 1**: *β* = -0.81, *SE* = 0.771, *z* = -1.045, *p* = 0.296
- **SNR**: *β* = 0.44, *SE* = 0.084, *z* = 5.221, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 1.20 | 0.54 | 2.21 | 0.027 | 0.218 | n.s. |
| 2 to 1 - 4 to 3 | 1.44 | 0.51 | 2.81 | 0.005 | 0.048 | * |
| 2 to 1 - 5 to 4 | 0.95 | 0.46 | 2.06 | 0.040 | 0.277 | n.s. |
| 2 to 1 - 6 to 5 | 0.81 | 0.77 | 1.04 | 0.296 | 0.911 | n.s. |
| 3 to 2 - 4 to 3 | 0.24 | 0.54 | 0.45 | 0.656 | 0.972 | n.s. |
| 3 to 2 - 5 to 4 | -0.25 | 0.50 | -0.49 | 0.622 | 0.972 | n.s. |
| 3 to 2 - 6 to 5 | -0.39 | 0.73 | -0.54 | 0.592 | 0.972 | n.s. |
| 4 to 3 - 5 to 4 | -0.49 | 0.46 | -1.05 | 0.293 | 0.911 | n.s. |
| 4 to 3 - 6 to 5 | -0.63 | 0.71 | -0.89 | 0.374 | 0.911 | n.s. |
| 5 to 4 - 6 to 5 | -0.15 | 0.69 | -0.21 | 0.832 | 0.972 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.77, *p* = 0.114, η²_G = 0.711
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.64 | 1 | = 0.576 | 3.70 [0.11, 2.73] | large | n.s. |
| 2 to 1 vs 4 to 3 | 12.50 | 1 | = 0.441 | 2.49 [0.28, 2.72] | large | n.s. |
| 2 to 1 vs 5 to 4 | 5.05 | 1 | = 0.441 | 2.34 [0.09, 1.55] | large | n.s. |
| 2 to 1 vs 6 to 5 | 4.74 | 1 | = 0.441 | 4.78 [-3.94, 13.41] | large | n.s. |
| 3 to 2 vs 4 to 3 | -0.23 | 1 | = 0.874 | -0.31 [-0.95, 1.15] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.26 | 1 | = 0.874 | 0.33 [-1.02, 0.84] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.20 | 1 | = 0.874 | 0.20 [-2.45, 2.52] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 1.65 | 1 | = 0.694 | 0.49 [-1.02, 0.44] | small | n.s. |
| 4 to 3 vs 6 to 5 | 0.46 | 1 | = 0.874 | 0.47 [-1.62, 1.56] | small | n.s. |
| 5 to 4 vs 6 to 5 | -0.28 | 1 | = 0.874 | -0.28 [-1.66, 1.53] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 899.82, BIC = 919.81
- **3 to 2 vs 2 to 1**: *β* = -15.79, *SE* = 9.570, *z* = -1.650, *p* = 0.099
- **4 to 3 vs 2 to 1**: *β* = -25.00, *SE* = 9.377, *z* = -2.666, *p* = 0.008
- **5 to 4 vs 2 to 1**: *β* = -8.78, *SE* = 9.044, *z* = -0.971, *p* = 0.331
- **6 to 5 vs 2 to 1**: *β* = 12.97, *SE* = 11.251, *z* = 1.153, *p* = 0.249
- **SNR**: *β* = -1.03, *SE* = 1.035, *z* = -0.994, *p* = 0.320

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 15.79 | 9.57 | 1.65 | 0.099 | 0.416 | n.s. |
| 2 to 1 - 4 to 3 | 25.00 | 9.38 | 2.67 | 0.008 | 0.067 | n.s. |
| 2 to 1 - 5 to 4 | 8.78 | 9.04 | 0.97 | 0.331 | 0.701 | n.s. |
| 2 to 1 - 6 to 5 | -12.97 | 11.25 | -1.15 | 0.249 | 0.682 | n.s. |
| 3 to 2 - 4 to 3 | 9.21 | 9.96 | 0.92 | 0.355 | 0.701 | n.s. |
| 3 to 2 - 5 to 4 | -7.01 | 9.79 | -0.72 | 0.474 | 0.701 | n.s. |
| 3 to 2 - 6 to 5 | -28.76 | 11.84 | -2.43 | 0.015 | 0.115 | n.s. |
| 4 to 3 - 5 to 4 | -16.22 | 9.44 | -1.72 | 0.086 | 0.416 | n.s. |
| 4 to 3 - 6 to 5 | -37.97 | 11.89 | -3.19 | 0.001 | 0.014 | * |
| 5 to 4 - 6 to 5 | -21.75 | 11.36 | -1.91 | 0.056 | 0.330 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.92, *p* = 0.012, η²_G = 0.309
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 0.59 | 7 | = 0.636 | 0.30 [-0.21, 0.85] | small | n.s. |
| 2 to 1 vs 4 to 3 | 1.09 | 7 | = 0.454 | 0.60 [0.07, 1.16] | medium | n.s. |
| 2 to 1 vs 5 to 4 | -0.24 | 7 | = 0.820 | -0.15 [-0.36, 0.58] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | -2.39 | 7 | = 0.120 | -1.36 [-1.27, 0.17] | large | n.s. |
| 3 to 2 vs 4 to 3 | 0.97 | 7 | = 0.454 | 0.26 [-0.35, 0.73] | small | n.s. |
| 3 to 2 vs 5 to 4 | -0.99 | 7 | = 0.454 | -0.47 [-0.82, 0.26] | small | n.s. |
| 3 to 2 vs 6 to 5 | -3.06 | 7 | = 0.076 | -1.67 [-1.50, 0.20] | large | n.s. |
| 4 to 3 vs 5 to 4 | -2.14 | 7 | = 0.140 | -0.84 [-1.02, 0.03] | large | n.s. |
| 4 to 3 vs 6 to 5 | -4.81 | 7 | = 0.019 | -2.46 [-2.40, -0.28] | large | * |
| 5 to 4 vs 6 to 5 | -2.91 | 7 | = 0.076 | -1.42 [-1.52, 0.01] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 411.15, BIC = 431.15
- **3 to 2 vs 2 to 1**: *β* = 0.86, *SE* = 0.590, *z* = 1.463, *p* = 0.143
- **4 to 3 vs 2 to 1**: *β* = -0.58, *SE* = 0.580, *z* = -0.998, *p* = 0.318
- **5 to 4 vs 2 to 1**: *β* = -0.04, *SE* = 0.554, *z* = -0.066, *p* = 0.947
- **6 to 5 vs 2 to 1**: *β* = 0.29, *SE* = 0.707, *z* = 0.417, *p* = 0.676
- **SNR**: *β* = 0.44, *SE* = 0.067, *z* = 6.480, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.86 | 0.59 | -1.46 | 0.143 | 0.722 | n.s. |
| 2 to 1 - 4 to 3 | 0.58 | 0.58 | 1.00 | 0.318 | 0.900 | n.s. |
| 2 to 1 - 5 to 4 | 0.04 | 0.55 | 0.07 | 0.947 | 0.954 | n.s. |
| 2 to 1 - 6 to 5 | -0.29 | 0.71 | -0.42 | 0.676 | 0.954 | n.s. |
| 3 to 2 - 4 to 3 | 1.44 | 0.61 | 2.35 | 0.019 | 0.174 | n.s. |
| 3 to 2 - 5 to 4 | 0.90 | 0.60 | 1.50 | 0.133 | 0.722 | n.s. |
| 3 to 2 - 6 to 5 | 0.57 | 0.74 | 0.77 | 0.440 | 0.902 | n.s. |
| 4 to 3 - 5 to 4 | -0.54 | 0.58 | -0.94 | 0.349 | 0.900 | n.s. |
| 4 to 3 - 6 to 5 | -0.87 | 0.75 | -1.16 | 0.244 | 0.859 | n.s. |
| 5 to 4 - 6 to 5 | -0.33 | 0.71 | -0.46 | 0.643 | 0.954 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.16, *p* = 0.349, η²_G = 0.102
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.22 | 7 | = 0.882 | -0.13 [-0.67, 0.36] | negligible | n.s. |
| 2 to 1 vs 4 to 3 | 0.45 | 7 | = 0.836 | 0.25 [-0.49, 0.51] | small | n.s. |
| 2 to 1 vs 5 to 4 | 1.06 | 7 | = 0.502 | 0.59 [-0.52, 0.42] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 1.83 | 7 | = 0.502 | 1.06 [-0.24, 1.17] | large | n.s. |
| 3 to 2 vs 4 to 3 | 1.00 | 7 | = 0.502 | 0.30 [-0.36, 0.71] | small | n.s. |
| 3 to 2 vs 5 to 4 | 1.82 | 7 | = 0.502 | 0.56 [-0.17, 0.93] | medium | n.s. |
| 3 to 2 vs 6 to 5 | 1.43 | 7 | = 0.502 | 0.79 [-0.35, 1.26] | medium | n.s. |
| 4 to 3 vs 5 to 4 | 1.36 | 7 | = 0.502 | 0.33 [-0.47, 0.53] | small | n.s. |
| 4 to 3 vs 6 to 5 | 1.09 | 7 | = 0.502 | 0.56 [-0.56, 1.00] | medium | n.s. |
| 5 to 4 vs 6 to 5 | 0.15 | 7 | = 0.882 | 0.08 [-0.55, 0.80] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.066)
**P3b latency:** Significant main effect of condition (*p* = 0.012). Post-hoc tests revealed:
  - 4 to 3 showed smaller latency than 6 to 5 (*d* = -2.46)

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
