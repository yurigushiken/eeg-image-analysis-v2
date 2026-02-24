# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:36:36

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
| Ratio 0.5 (1:2, no 1) | 24 | 102.00 ms | 8.17 | 1.67 | [92.00, 112.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 103.33 ms | 7.04 | 1.44 | [92.00, 112.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 103.00 ms | 8.28 | 1.69 | [92.00, 112.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 104.17 ms | 7.41 | 1.51 | [92.00, 112.00] |
| Ratio 0.83 (5:6, no 1) | 24 | 102.00 ms | 7.17 | 1.46 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | -1.03 µV | 1.34 | 0.27 | [-4.02, 1.18] |
| Ratio 0.67 (2:3, no 1) | 24 | -1.03 µV | 1.35 | 0.28 | [-3.86, 1.46] |
| Ratio 0.75 (3:4, no 1) | 24 | -0.98 µV | 1.63 | 0.33 | [-5.60, 1.98] |
| Ratio 0.8 (4:5, no 1) | 24 | -1.36 µV | 2.26 | 0.46 | [-8.22, 2.18] |
| Ratio 0.83 (5:6, no 1) | 24 | -1.20 µV | 1.29 | 0.26 | [-4.39, 0.82] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 172.50 ms | 15.30 | 3.12 | [140.00, 204.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 174.33 ms | 20.12 | 4.11 | [140.00, 204.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 172.17 ms | 18.82 | 3.84 | [140.00, 204.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 171.67 ms | 21.68 | 4.43 | [140.00, 204.00] |
| Ratio 0.83 (5:6, no 1) | 24 | 175.50 ms | 18.06 | 3.69 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | -5.88 µV | 2.15 | 0.44 | [-10.62, -2.62] |
| Ratio 0.67 (2:3, no 1) | 24 | -5.04 µV | 2.19 | 0.45 | [-9.87, -1.99] |
| Ratio 0.75 (3:4, no 1) | 24 | -5.41 µV | 2.15 | 0.44 | [-10.31, -0.44] |
| Ratio 0.8 (4:5, no 1) | 24 | -5.40 µV | 2.55 | 0.52 | [-10.71, -1.29] |
| Ratio 0.83 (5:6, no 1) | 24 | -5.52 µV | 1.99 | 0.41 | [-9.96, -2.06] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 103.50 ms | 8.45 | 1.72 | [92.00, 112.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 104.50 ms | 7.85 | 1.60 | [92.00, 112.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 102.67 ms | 8.23 | 1.68 | [92.00, 112.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 104.67 ms | 8.48 | 1.73 | [92.00, 112.00] |
| Ratio 0.83 (5:6, no 1) | 24 | 102.67 ms | 8.40 | 1.71 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 0.97 µV | 1.61 | 0.33 | [-2.35, 5.22] |
| Ratio 0.67 (2:3, no 1) | 24 | 0.85 µV | 1.77 | 0.36 | [-2.36, 4.44] |
| Ratio 0.75 (3:4, no 1) | 24 | 1.15 µV | 1.78 | 0.36 | [-1.13, 5.67] |
| Ratio 0.8 (4:5, no 1) | 24 | 1.38 µV | 2.08 | 0.42 | [-1.45, 5.75] |
| Ratio 0.83 (5:6, no 1) | 24 | 1.04 µV | 1.84 | 0.38 | [-2.61, 4.00] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 480.00 ms | 32.71 | 6.68 | [436.00, 540.00] |
| Ratio 0.67 (2:3, no 1) | 24 | 485.50 ms | 35.79 | 7.31 | [436.00, 540.00] |
| Ratio 0.75 (3:4, no 1) | 24 | 491.33 ms | 33.56 | 6.85 | [436.00, 540.00] |
| Ratio 0.8 (4:5, no 1) | 24 | 497.67 ms | 28.48 | 5.81 | [448.00, 540.00] |
| Ratio 0.83 (5:6, no 1) | 24 | 493.67 ms | 39.49 | 8.06 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2, no 1) | 24 | 3.63 µV | 3.21 | 0.66 | [-2.11, 9.62] |
| Ratio 0.67 (2:3, no 1) | 24 | 3.68 µV | 3.68 | 0.75 | [-2.06, 12.42] |
| Ratio 0.75 (3:4, no 1) | 24 | 3.85 µV | 3.71 | 0.76 | [-3.35, 11.73] |
| Ratio 0.8 (4:5, no 1) | 24 | 3.44 µV | 3.86 | 0.79 | [-3.97, 11.33] |
| Ratio 0.83 (5:6, no 1) | 24 | 1.50 µV | 3.11 | 0.64 | [-4.74, 9.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 799.24, BIC = 821.54
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.20, *SE* = 1.533, *z* = 0.781, *p* = 0.435
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.17, *SE* = 1.535, *z* = 0.762, *p* = 0.446
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 2.27, *SE* = 1.531, *z* = 1.479, *p* = 0.139
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.35, *SE* = 1.552, *z* = 0.228, *p* = 0.820
- **SNR**: *β* = 0.55, *SE* = 0.412, *z* = 1.339, *p* = 0.181

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -1.20 | 1.53 | -0.78 | 0.435 | 0.990 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -1.17 | 1.53 | -0.76 | 0.446 | 0.990 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -2.27 | 1.53 | -1.48 | 0.139 | 0.776 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -0.35 | 1.55 | -0.23 | 0.820 | 0.990 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.03 | 1.55 | 0.02 | 0.986 | 0.990 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -1.07 | 1.54 | -0.69 | 0.488 | 0.990 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.84 | 1.57 | 0.54 | 0.592 | 0.990 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -1.09 | 1.53 | -0.72 | 0.474 | 0.990 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.82 | 1.54 | 0.53 | 0.595 | 0.990 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 1.91 | 1.54 | 1.24 | 0.215 | 0.887 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.69, *p* = 0.602, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.82 | 23 | = 0.737 | -0.17 [-0.59, 0.26] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.56 | 23 | = 0.737 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.41 | 23 | = 0.737 | -0.28 [-0.72, 0.14] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.18 | 23 | = 0.958 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.55 | 23 | = 0.737 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 0.77 | 23 | = 0.737 | 0.19 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.98 | 23 | = 0.737 | -0.15 [-0.63, 0.23] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.62 | 23 | = 0.737 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 2.18 | 23 | = 0.394 | 0.30 [0.00, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 406.15, BIC = 428.45
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.12, *SE* = 0.308, *z* = 0.373, *p* = 0.709
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.09, *SE* = 0.309, *z* = -0.292, *p* = 0.770
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.41, *SE* = 0.308, *z* = -1.349, *p* = 0.177
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.46, *SE* = 0.312, *z* = -1.474, *p* = 0.140
- **SNR**: *β* = -0.46, *SE* = 0.083, *z* = -5.535, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.11 | 0.31 | -0.37 | 0.709 | 0.975 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.09 | 0.31 | 0.29 | 0.770 | 0.975 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.42 | 0.31 | 1.35 | 0.177 | 0.745 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.46 | 0.31 | 1.47 | 0.140 | 0.702 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.20 | 0.31 | 0.66 | 0.510 | 0.942 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.53 | 0.31 | 1.71 | 0.087 | 0.558 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.57 | 0.32 | 1.82 | 0.069 | 0.511 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.32 | 0.31 | 1.06 | 0.291 | 0.821 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.37 | 0.31 | 1.20 | 0.231 | 0.793 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.04 | 0.31 | 0.14 | 0.885 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.793, η²_G = 0.008
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.00 | 23 | = 0.997 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.21 | 23 | = 0.952 | -0.03 [-0.47, 0.38] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.83 | 23 | = 0.952 | 0.18 [-0.25, 0.60] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.50 | 23 | = 0.952 | 0.13 [-0.32, 0.52] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.18 | 23 | = 0.952 | -0.03 [-0.46, 0.39] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.93 | 23 | = 0.952 | 0.18 [-0.24, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 0.45 | 23 | = 0.952 | 0.13 [-0.33, 0.52] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 1.09 | 23 | = 0.952 | 0.20 [-0.20, 0.65] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.60 | 23 | = 0.952 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.36 | 23 | = 0.952 | -0.09 [-0.50, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1002.12, BIC = 1024.42
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 1.70, *SE* = 3.487, *z* = 0.489, *p* = 0.625
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.69, *SE* = 3.638, *z* = -0.190, *p* = 0.849
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.12, *SE* = 3.579, *z* = -0.314, *p* = 0.754
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 2.69, *SE* = 3.593, *z* = 0.749, *p* = 0.454
- **SNR**: *β* = -0.10, *SE* = 0.310, *z* = -0.321, *p* = 0.748

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -1.70 | 3.49 | -0.49 | 0.625 | 0.993 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.69 | 3.64 | 0.19 | 0.849 | 0.996 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 1.12 | 3.58 | 0.31 | 0.754 | 0.996 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -2.69 | 3.59 | -0.75 | 0.454 | 0.987 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 2.39 | 3.54 | 0.68 | 0.498 | 0.987 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 2.83 | 3.50 | 0.81 | 0.419 | 0.987 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -0.99 | 3.51 | -0.28 | 0.778 | 0.996 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.43 | 3.47 | 0.12 | 0.901 | 0.996 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -3.38 | 3.47 | -0.98 | 0.329 | 0.972 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | -3.82 | 3.46 | -1.10 | 0.271 | 0.957 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.42, *p* = 0.794, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.718 (ε = 0.673)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.59 | 23 | = 0.913 | -0.10 [-0.54, 0.30] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.09 | 23 | = 0.928 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.38 | 23 | = 0.913 | 0.04 [-0.35, 0.50] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.78 | 23 | = 0.913 | -0.18 [-0.58, 0.27] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.77 | 23 | = 0.913 | 0.11 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.75 | 23 | = 0.913 | 0.13 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.35 | 23 | = 0.913 | -0.06 [-0.49, 0.35] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.13 | 23 | = 0.928 | 0.02 [-0.40, 0.45] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.97 | 23 | = 0.913 | -0.18 [-0.62, 0.23] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | -0.81 | 23 | = 0.913 | -0.19 [-0.59, 0.26] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 414.62, BIC = 436.92
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.62, *SE* = 0.287, *z* = 2.145, *p* = 0.032
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.14, *SE* = 0.300, *z* = -0.453, *p* = 0.651
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.02, *SE* = 0.295, *z* = -0.058, *p* = 0.954
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.17, *SE* = 0.296, *z* = -0.558, *p* = 0.577
- **SNR**: *β* = -0.17, *SE* = 0.026, *z* = -6.566, *p* < .001

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.62 | 0.29 | -2.15 | 0.032 | 0.203 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 0.14 | 0.30 | 0.45 | 0.651 | 0.994 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | 0.02 | 0.30 | 0.06 | 0.954 | 0.994 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 0.17 | 0.30 | 0.56 | 0.577 | 0.994 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 0.75 | 0.29 | 2.58 | 0.010 | 0.085 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | 0.63 | 0.29 | 2.20 | 0.028 | 0.203 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 0.78 | 0.29 | 2.70 | 0.007 | 0.066 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.12 | 0.29 | -0.42 | 0.678 | 0.994 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.03 | 0.29 | 0.10 | 0.918 | 0.994 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.15 | 0.29 | 0.52 | 0.604 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.57, *p* = 0.189, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -4.21 | 23 | = 0.003 | -0.39 [-1.35, -0.36] | small | ** |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.28 | 23 | = 0.426 | -0.22 [-0.69, 0.17] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.28 | 23 | = 0.426 | -0.20 [-0.69, 0.17] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.29 | 23 | = 0.426 | -0.17 [-0.69, 0.17] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.96 | 23 | = 0.503 | 0.17 [-0.23, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.95 | 23 | = 0.503 | 0.15 [-0.23, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.54 | 23 | = 0.426 | 0.23 [-0.12, 0.75] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.01 | 23 | = 0.995 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.33 | 23 | = 0.835 | 0.06 [-0.35, 0.49] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.32 | 23 | = 0.835 | 0.05 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 811.87, BIC = 834.17
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.82, *SE* = 1.599, *z* = 0.512, *p* = 0.609
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.15, *SE* = 1.616, *z* = -0.710, *p* = 0.478
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.88, *SE* = 1.612, *z* = 0.546, *p* = 0.585
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.15, *SE* = 1.616, *z* = -0.712, *p* = 0.476
- **SNR**: *β* = -0.36, *SE* = 0.326, *z* = -1.105, *p* = 0.269

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.82 | 1.60 | -0.51 | 0.609 | 0.979 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | 1.15 | 1.62 | 0.71 | 0.478 | 0.979 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.88 | 1.61 | -0.55 | 0.585 | 0.979 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 1.15 | 1.62 | 0.71 | 0.476 | 0.979 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | 1.97 | 1.60 | 1.23 | 0.218 | 0.895 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.06 | 1.59 | -0.04 | 0.970 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 1.97 | 1.60 | 1.23 | 0.217 | 0.895 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -2.03 | 1.59 | -1.27 | 0.203 | 0.895 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.00 | 1.59 | 0.00 | 0.998 | 0.999 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 2.03 | 1.59 | 1.28 | 0.202 | 0.895 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.69, *p* = 0.598, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.65 | 23 | = 0.806 | -0.12 [-0.56, 0.29] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | 0.51 | 23 | = 0.806 | 0.10 [-0.32, 0.53] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -0.79 | 23 | = 0.806 | -0.14 [-0.59, 0.26] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 0.47 | 23 | = 0.806 | 0.10 [-0.33, 0.52] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | 0.93 | 23 | = 0.806 | 0.23 [-0.24, 0.62] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -0.11 | 23 | = 1.000 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 1.37 | 23 | = 0.806 | 0.23 [-0.15, 0.71] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -1.02 | 23 | = 0.806 | -0.24 [-0.64, 0.22] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 1.91 | 23 | = 0.693 | 0.24 [-0.05, 0.83] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 444.20, BIC = 466.50
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -0.07, *SE* = 0.346, *z* = -0.197, *p* = 0.844
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.27, *SE* = 0.350, *z* = 0.755, *p* = 0.450
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.48, *SE* = 0.349, *z* = 1.383, *p* = 0.167
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.16, *SE* = 0.350, *z* = 0.446, *p* = 0.656
- **SNR**: *β* = 0.10, *SE* = 0.073, *z* = 1.298, *p* = 0.194

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | 0.07 | 0.35 | 0.20 | 0.844 | 0.973 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.26 | 0.35 | -0.76 | 0.450 | 0.972 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.48 | 0.35 | -1.38 | 0.167 | 0.806 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -0.16 | 0.35 | -0.45 | 0.656 | 0.973 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.33 | 0.35 | -0.96 | 0.335 | 0.962 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.55 | 0.35 | -1.60 | 0.110 | 0.689 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -0.22 | 0.35 | -0.65 | 0.516 | 0.973 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -0.22 | 0.34 | -0.63 | 0.526 | 0.973 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 0.11 | 0.34 | 0.31 | 0.753 | 0.973 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 0.33 | 0.34 | 0.95 | 0.343 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.64, *p* = 0.634, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.550 (ε = 0.570)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | 0.53 | 23 | = 0.789 | 0.07 [-0.32, 0.53] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.57 | 23 | = 0.789 | -0.11 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -1.55 | 23 | = 0.677 | -0.22 [-0.75, 0.12] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -0.18 | 23 | = 0.857 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.93 | 23 | = 0.789 | -0.17 [-0.62, 0.24] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.90 | 23 | = 0.677 | -0.27 [-0.83, 0.05] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.44 | 23 | = 0.789 | -0.10 [-0.51, 0.33] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.56 | 23 | = 0.789 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 0.38 | 23 | = 0.789 | 0.06 [-0.35, 0.50] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.68 | 23 | = 0.789 | 0.17 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1184.31, BIC = 1206.61
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 5.60, *SE* = 8.109, *z* = 0.690, *p* = 0.490
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 10.22, *SE* = 8.143, *z* = 1.254, *p* = 0.210
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 15.60, *SE* = 8.227, *z* = 1.896, *p* = 0.058
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 10.56, *SE* = 8.375, *z* = 1.261, *p* = 0.207
- **SNR**: *β* = -0.99, *SE* = 0.671, *z* = -1.483, *p* = 0.138

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -5.60 | 8.11 | -0.69 | 0.490 | 0.982 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -10.22 | 8.14 | -1.25 | 0.210 | 0.876 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -15.60 | 8.23 | -1.90 | 0.058 | 0.449 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | -10.56 | 8.37 | -1.26 | 0.207 | 0.876 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -4.62 | 8.15 | -0.57 | 0.571 | 0.982 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -10.00 | 8.24 | -1.21 | 0.225 | 0.876 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | -4.96 | 8.39 | -0.59 | 0.554 | 0.982 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | -5.38 | 8.13 | -0.66 | 0.508 | 0.982 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | -0.34 | 8.22 | -0.04 | 0.967 | 0.982 | n.s. |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 5.04 | 8.14 | 0.62 | 0.536 | 0.982 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.36, *p* = 0.253, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.98 | 23 | = 0.592 | -0.16 [-0.63, 0.23] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -1.45 | 23 | = 0.536 | -0.34 [-0.73, 0.13] | small | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | -2.47 | 23 | = 0.215 | -0.58 [-0.95, -0.06] | medium | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | -1.43 | 23 | = 0.536 | -0.38 [-0.72, 0.14] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.68 | 23 | = 0.633 | -0.17 [-0.56, 0.29] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | -1.28 | 23 | = 0.536 | -0.38 [-0.69, 0.17] | small | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | -0.85 | 23 | = 0.592 | -0.22 [-0.60, 0.25] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | -0.83 | 23 | = 0.592 | -0.20 [-0.59, 0.26] | small | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | -0.25 | 23 | = 0.802 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 0.46 | 23 | = 0.721 | 0.12 [-0.33, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 529.90, BIC = 552.20
- **Ratio 0.67 (2:3, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.04, *SE* = 0.442, *z* = 0.084, *p* = 0.933
- **Ratio 0.75 (3:4, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.35, *SE* = 0.444, *z* = 0.787, *p* = 0.431
- **Ratio 0.8 (4:5, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = 0.05, *SE* = 0.449, *z* = 0.121, *p* = 0.904
- **Ratio 0.83 (5:6, no 1) vs Ratio 0.5 (1:2, no 1)**: *β* = -1.75, *SE* = 0.459, *z* = -3.826, *p* < .001
- **SNR**: *β* = 0.12, *SE* = 0.039, *z* = 3.084, *p* = 0.002

_Reference condition: **Ratio 0.5 (1:2, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2, no 1) - Ratio 0.67 (2:3, no 1) | -0.04 | 0.44 | -0.08 | 0.933 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.75 (3:4, no 1) | -0.35 | 0.44 | -0.79 | 0.431 | 0.966 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.8 (4:5, no 1) | -0.05 | 0.45 | -0.12 | 0.904 | 0.999 | n.s. |
| Ratio 0.5 (1:2, no 1) - Ratio 0.83 (5:6, no 1) | 1.75 | 0.46 | 3.83 | < .001 | < .001 | *** |
| Ratio 0.67 (2:3, no 1) - Ratio 0.75 (3:4, no 1) | -0.31 | 0.44 | -0.70 | 0.482 | 0.966 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.8 (4:5, no 1) | -0.02 | 0.45 | -0.04 | 0.969 | 0.999 | n.s. |
| Ratio 0.67 (2:3, no 1) - Ratio 0.83 (5:6, no 1) | 1.79 | 0.46 | 3.90 | < .001 | < .001 | *** |
| Ratio 0.75 (3:4, no 1) - Ratio 0.8 (4:5, no 1) | 0.29 | 0.44 | 0.67 | 0.506 | 0.966 | n.s. |
| Ratio 0.75 (3:4, no 1) - Ratio 0.83 (5:6, no 1) | 2.10 | 0.45 | 4.69 | < .001 | < .001 | *** |
| Ratio 0.8 (4:5, no 1) - Ratio 0.83 (5:6, no 1) | 1.81 | 0.44 | 4.08 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.62, *p* < .001, η²_G = 0.060
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.685)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2, no 1) vs Ratio 0.67 (2:3, no 1) | -0.18 | 23 | = 0.859 | -0.01 [-0.46, 0.39] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.75 (3:4, no 1) | -0.61 | 23 | = 0.757 | -0.06 [-0.55, 0.30] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.8 (4:5, no 1) | 0.52 | 23 | = 0.757 | 0.06 [-0.32, 0.53] | negligible | n.s. |
| Ratio 0.5 (1:2, no 1) vs Ratio 0.83 (5:6, no 1) | 4.57 | 23 | = 0.001 | 0.67 [0.43, 1.44] | medium | ** |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.75 (3:4, no 1) | -0.42 | 23 | = 0.757 | -0.04 [-0.51, 0.34] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.8 (4:5, no 1) | 0.56 | 23 | = 0.757 | 0.07 [-0.31, 0.54] | negligible | n.s. |
| Ratio 0.67 (2:3, no 1) vs Ratio 0.83 (5:6, no 1) | 3.86 | 23 | = 0.004 | 0.64 [0.31, 1.27] | medium | ** |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.8 (4:5, no 1) | 0.79 | 23 | = 0.757 | 0.11 [-0.26, 0.59] | negligible | n.s. |
| Ratio 0.75 (3:4, no 1) vs Ratio 0.83 (5:6, no 1) | 3.66 | 23 | = 0.004 | 0.69 [0.27, 1.22] | medium | ** |
| Ratio 0.8 (4:5, no 1) vs Ratio 0.83 (5:6, no 1) | 3.63 | 23 | = 0.004 | 0.55 [0.26, 1.22] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Ratio 0.5 (1:2, no 1) showed greater amplitude than Ratio 0.83 (5:6, no 1) (*d* = 0.67)
  - Ratio 0.67 (2:3, no 1) showed greater amplitude than Ratio 0.83 (5:6, no 1) (*d* = 0.64)
  - Ratio 0.75 (3:4, no 1) showed greater amplitude than Ratio 0.83 (5:6, no 1) (*d* = 0.69)
  - Ratio 0.8 (4:5, no 1) showed greater amplitude than Ratio 0.83 (5:6, no 1) (*d* = 0.55)

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
