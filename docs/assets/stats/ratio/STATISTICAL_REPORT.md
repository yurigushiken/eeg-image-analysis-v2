# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:33:35

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
| Ratio 0.5 (1:2) | 24 | 102.00 ms | 8.67 | 1.77 | [92.00, 112.00] |
| Ratio 0.67 (2:3) | 24 | 103.33 ms | 7.04 | 1.44 | [92.00, 112.00] |
| Ratio 0.75 (3:4) | 24 | 103.00 ms | 8.28 | 1.69 | [92.00, 112.00] |
| Ratio 0.8 (4:5) | 24 | 104.17 ms | 7.41 | 1.51 | [92.00, 112.00] |
| Ratio 0.83 (5:6) | 24 | 102.00 ms | 7.17 | 1.46 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | -0.94 µV | 1.18 | 0.24 | [-4.19, 0.89] |
| Ratio 0.67 (2:3) | 24 | -1.03 µV | 1.35 | 0.28 | [-3.86, 1.46] |
| Ratio 0.75 (3:4) | 24 | -0.98 µV | 1.63 | 0.33 | [-5.60, 1.98] |
| Ratio 0.8 (4:5) | 24 | -1.36 µV | 2.26 | 0.46 | [-8.22, 2.18] |
| Ratio 0.83 (5:6) | 24 | -1.20 µV | 1.29 | 0.26 | [-4.39, 0.82] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 172.83 ms | 15.56 | 3.18 | [144.00, 204.00] |
| Ratio 0.67 (2:3) | 24 | 174.50 ms | 19.84 | 4.05 | [144.00, 204.00] |
| Ratio 0.75 (3:4) | 24 | 172.33 ms | 18.53 | 3.78 | [144.00, 204.00] |
| Ratio 0.8 (4:5) | 24 | 172.00 ms | 21.20 | 4.33 | [144.00, 204.00] |
| Ratio 0.83 (5:6) | 24 | 175.50 ms | 18.06 | 3.69 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | -5.07 µV | 2.11 | 0.43 | [-9.31, -1.91] |
| Ratio 0.67 (2:3) | 24 | -5.04 µV | 2.19 | 0.45 | [-9.87, -1.99] |
| Ratio 0.75 (3:4) | 24 | -5.41 µV | 2.15 | 0.44 | [-10.31, -0.44] |
| Ratio 0.8 (4:5) | 24 | -5.39 µV | 2.56 | 0.52 | [-10.71, -1.29] |
| Ratio 0.83 (5:6) | 24 | -5.52 µV | 1.99 | 0.41 | [-9.96, -2.06] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 103.67 ms | 8.42 | 1.72 | [92.00, 112.00] |
| Ratio 0.67 (2:3) | 24 | 104.50 ms | 7.85 | 1.60 | [92.00, 112.00] |
| Ratio 0.75 (3:4) | 24 | 102.67 ms | 8.23 | 1.68 | [92.00, 112.00] |
| Ratio 0.8 (4:5) | 24 | 104.67 ms | 8.48 | 1.73 | [92.00, 112.00] |
| Ratio 0.83 (5:6) | 24 | 102.67 ms | 8.40 | 1.71 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 1.04 µV | 1.48 | 0.30 | [-1.61, 5.34] |
| Ratio 0.67 (2:3) | 24 | 0.85 µV | 1.77 | 0.36 | [-2.36, 4.44] |
| Ratio 0.75 (3:4) | 24 | 1.15 µV | 1.78 | 0.36 | [-1.13, 5.67] |
| Ratio 0.8 (4:5) | 24 | 1.38 µV | 2.08 | 0.42 | [-1.45, 5.75] |
| Ratio 0.83 (5:6) | 24 | 1.04 µV | 1.84 | 0.38 | [-2.61, 4.00] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 479.17 ms | 33.57 | 6.85 | [436.00, 540.00] |
| Ratio 0.67 (2:3) | 24 | 485.50 ms | 35.79 | 7.31 | [436.00, 540.00] |
| Ratio 0.75 (3:4) | 24 | 491.33 ms | 33.56 | 6.85 | [436.00, 540.00] |
| Ratio 0.8 (4:5) | 24 | 497.67 ms | 28.48 | 5.81 | [448.00, 540.00] |
| Ratio 0.83 (5:6) | 24 | 493.67 ms | 39.49 | 8.06 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 3.38 µV | 3.02 | 0.62 | [-2.52, 8.88] |
| Ratio 0.67 (2:3) | 24 | 3.68 µV | 3.68 | 0.75 | [-2.06, 12.42] |
| Ratio 0.75 (3:4) | 24 | 3.85 µV | 3.71 | 0.76 | [-3.35, 11.73] |
| Ratio 0.8 (4:5) | 24 | 3.44 µV | 3.86 | 0.79 | [-3.97, 11.33] |
| Ratio 0.83 (5:6) | 24 | 1.50 µV | 3.11 | 0.64 | [-4.74, 9.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 804.02, BIC = 826.32
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 1.10, *SE* = 1.589, *z* = 0.695, *p* = 0.487
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.97, *SE* = 1.565, *z* = 0.618, *p* = 0.537
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 2.09, *SE* = 1.568, *z* = 1.332, *p* = 0.183
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.09, *SE* = 1.568, *z* = 0.054, *p* = 0.957
- **SNR**: *β* = 0.35, *SE* = 0.426, *z* = 0.831, *p* = 0.406

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -1.10 | 1.59 | -0.69 | 0.487 | 0.994 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.97 | 1.57 | -0.62 | 0.537 | 0.994 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -2.09 | 1.57 | -1.33 | 0.183 | 0.867 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.09 | 1.57 | -0.05 | 0.957 | 0.995 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.14 | 1.58 | 0.09 | 0.931 | 0.995 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.98 | 1.58 | -0.62 | 0.532 | 0.994 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 1.02 | 1.61 | 0.63 | 0.527 | 0.994 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -1.12 | 1.57 | -0.72 | 0.474 | 0.994 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.88 | 1.57 | 0.56 | 0.574 | 0.994 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 2.00 | 1.58 | 1.27 | 0.204 | 0.872 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.617, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.77 | 23 | = 0.737 | -0.17 [-0.58, 0.27] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -0.55 | 23 | = 0.737 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -1.41 | 23 | = 0.737 | -0.27 [-0.72, 0.14] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.18 | 23 | = 0.958 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.55 | 23 | = 0.737 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.77 | 23 | = 0.737 | 0.19 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.98 | 23 | = 0.737 | -0.15 [-0.63, 0.23] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.62 | 23 | = 0.737 | 0.13 [-0.30, 0.55] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 2.18 | 23 | = 0.394 | 0.30 [0.00, 0.89] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 409.17, BIC = 431.47
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.20, *SE* = 0.324, *z* = 0.607, *p* = 0.544
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.00, *SE* = 0.319, *z* = 0.011, *p* = 0.991
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.32, *SE* = 0.320, *z* = -1.013, *p* = 0.311
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -0.36, *SE* = 0.320, *z* = -1.123, *p* = 0.262
- **SNR**: *β* = -0.44, *SE* = 0.088, *z* = -4.973, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.20 | 0.32 | -0.61 | 0.544 | 0.957 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.00 | 0.32 | -0.01 | 0.991 | 0.992 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.32 | 0.32 | 1.01 | 0.311 | 0.908 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 0.36 | 0.32 | 1.12 | 0.262 | 0.908 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.19 | 0.32 | 0.60 | 0.550 | 0.957 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.52 | 0.32 | 1.62 | 0.105 | 0.632 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.56 | 0.33 | 1.69 | 0.091 | 0.614 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.33 | 0.32 | 1.03 | 0.305 | 0.908 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.36 | 0.32 | 1.13 | 0.258 | 0.908 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.04 | 0.32 | 0.11 | 0.913 | 0.992 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.52, *p* = 0.725, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.32 | 23 | = 0.884 | 0.07 [-0.36, 0.49] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.15 | 23 | = 0.884 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 1.06 | 23 | = 0.884 | 0.23 [-0.21, 0.64] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.83 | 23 | = 0.884 | 0.21 [-0.26, 0.59] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.18 | 23 | = 0.884 | -0.03 [-0.46, 0.39] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.93 | 23 | = 0.884 | 0.18 [-0.24, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.45 | 23 | = 0.884 | 0.13 [-0.33, 0.52] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 1.09 | 23 | = 0.884 | 0.20 [-0.20, 0.65] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.60 | 23 | = 0.884 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.36 | 23 | = 0.884 | -0.09 [-0.50, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 996.29, BIC = 1018.59
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 1.41, *SE* = 3.397, *z* = 0.414, *p* = 0.679
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.14, *SE* = 3.561, *z* = -0.319, *p* = 0.750
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.35, *SE* = 3.497, *z* = -0.387, *p* = 0.699
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 2.11, *SE* = 3.514, *z* = 0.601, *p* = 0.548
- **SNR**: *β* = -0.16, *SE* = 0.296, *z* = -0.544, *p* = 0.587

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -1.41 | 3.40 | -0.41 | 0.679 | 0.997 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.14 | 3.56 | 0.32 | 0.750 | 0.997 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.35 | 3.50 | 0.39 | 0.699 | 0.997 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -2.11 | 3.51 | -0.60 | 0.548 | 0.991 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 2.54 | 3.43 | 0.74 | 0.459 | 0.987 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 2.76 | 3.40 | 0.81 | 0.416 | 0.987 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.71 | 3.41 | -0.21 | 0.836 | 0.997 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.22 | 3.37 | 0.06 | 0.949 | 0.997 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -3.25 | 3.37 | -0.97 | 0.334 | 0.974 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -3.47 | 3.36 | -1.03 | 0.303 | 0.973 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.820, η²_G = 0.005
- Greenhouse-Geisser corrected: *p* = 0.748 (ε = 0.689)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.56 | 23 | = 0.933 | -0.09 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.14 | 23 | = 0.933 | 0.03 [-0.39, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.38 | 23 | = 0.933 | 0.04 [-0.35, 0.50] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.76 | 23 | = 0.933 | -0.16 [-0.58, 0.27] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.78 | 23 | = 0.933 | 0.11 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.72 | 23 | = 0.933 | 0.12 [-0.28, 0.57] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.30 | 23 | = 0.933 | -0.05 [-0.48, 0.36] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.09 | 23 | = 0.933 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.92 | 23 | = 0.933 | -0.17 [-0.61, 0.24] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.76 | 23 | = 0.933 | -0.18 [-0.58, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 414.97, BIC = 437.27
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.24, *SE* = 0.288, *z* = -0.843, *p* = 0.399
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -0.99, *SE* = 0.302, *z* = -3.280, *p* = 0.001
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.86, *SE* = 0.296, *z* = -2.903, *p* = 0.004
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.02, *SE* = 0.298, *z* = -3.428, *p* = 0.001
- **SNR**: *β* = -0.17, *SE* = 0.026, *z* = -6.446, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.24 | 0.29 | 0.84 | 0.399 | 0.870 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 0.99 | 0.30 | 3.28 | 0.001 | 0.009 | ** |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.86 | 0.30 | 2.90 | 0.004 | 0.029 | * |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.02 | 0.30 | 3.43 | < .001 | 0.006 | ** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.75 | 0.29 | 2.57 | 0.010 | 0.059 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.62 | 0.29 | 2.15 | 0.032 | 0.149 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.78 | 0.29 | 2.70 | 0.007 | 0.048 | * |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.13 | 0.29 | -0.46 | 0.648 | 0.922 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.03 | 0.28 | 0.11 | 0.915 | 0.922 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.16 | 0.28 | 0.56 | 0.572 | 0.922 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.83, *p* = 0.509, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.481 (ε = 0.747)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.14 | 23 | = 0.973 | -0.01 [-0.45, 0.39] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.99 | 23 | = 0.686 | 0.16 [-0.22, 0.63] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.84 | 23 | = 0.686 | 0.14 [-0.25, 0.60] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.61 | 23 | = 0.680 | 0.22 [-0.10, 0.76] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.96 | 23 | = 0.686 | 0.17 [-0.23, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.93 | 23 | = 0.686 | 0.15 [-0.24, 0.61] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.54 | 23 | = 0.680 | 0.23 [-0.12, 0.75] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.03 | 23 | = 0.973 | -0.01 [-0.43, 0.42] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.33 | 23 | = 0.927 | 0.06 [-0.35, 0.49] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.35 | 23 | = 0.927 | 0.06 [-0.35, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 815.32, BIC = 837.62
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.66, *SE* = 1.634, *z* = 0.405, *p* = 0.686
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.26, *SE* = 1.648, *z* = -0.767, *p* = 0.443
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.76, *SE* = 1.645, *z* = 0.459, *p* = 0.646
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.27, *SE* = 1.649, *z* = -0.768, *p* = 0.442
- **SNR**: *β* = -0.25, *SE* = 0.273, *z* = -0.908, *p* = 0.364

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.66 | 1.63 | -0.40 | 0.686 | 0.984 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.26 | 1.65 | 0.77 | 0.443 | 0.970 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.75 | 1.64 | -0.46 | 0.646 | 0.984 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.27 | 1.65 | 0.77 | 0.442 | 0.970 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 1.92 | 1.63 | 1.18 | 0.236 | 0.909 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.09 | 1.62 | -0.06 | 0.954 | 0.998 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 1.93 | 1.63 | 1.19 | 0.236 | 0.909 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -2.02 | 1.62 | -1.24 | 0.214 | 0.909 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.00 | 1.62 | 0.00 | 0.999 | 0.999 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 2.02 | 1.62 | 1.25 | 0.213 | 0.909 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.618, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.48 | 23 | = 0.795 | -0.10 [-0.52, 0.33] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.50 | 23 | = 0.795 | 0.12 [-0.32, 0.53] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.78 | 23 | = 0.795 | -0.12 [-0.58, 0.27] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.60 | 23 | = 0.795 | 0.12 [-0.30, 0.55] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.93 | 23 | = 0.795 | 0.23 [-0.24, 0.62] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.11 | 23 | = 1.000 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.37 | 23 | = 0.795 | 0.23 [-0.15, 0.71] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -1.02 | 23 | = 0.795 | -0.24 [-0.64, 0.22] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 1.91 | 23 | = 0.693 | 0.24 [-0.05, 0.83] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 437.93, BIC = 460.23
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.11, *SE* = 0.338, *z* = -0.330, *p* = 0.741
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.23, *SE* = 0.342, *z* = 0.661, *p* = 0.508
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.44, *SE* = 0.341, *z* = 1.301, *p* = 0.193
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.12, *SE* = 0.342, *z* = 0.345, *p* = 0.730
- **SNR**: *β* = 0.11, *SE* = 0.059, *z* = 1.838, *p* = 0.066

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.11 | 0.34 | 0.33 | 0.741 | 0.983 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.23 | 0.34 | -0.66 | 0.508 | 0.983 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.44 | 0.34 | -1.30 | 0.193 | 0.855 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.12 | 0.34 | -0.34 | 0.730 | 0.983 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.34 | 0.34 | -1.00 | 0.316 | 0.952 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.56 | 0.34 | -1.65 | 0.099 | 0.647 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.23 | 0.34 | -0.68 | 0.495 | 0.983 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.22 | 0.34 | -0.65 | 0.518 | 0.983 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.11 | 0.34 | 0.32 | 0.747 | 0.983 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.33 | 0.34 | 0.97 | 0.332 | 0.952 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.648, η²_G = 0.009
- Greenhouse-Geisser corrected: *p* = 0.558 (ε = 0.560)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.95 | 23 | = 0.789 | 0.11 [-0.23, 0.62] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -0.42 | 23 | = 0.789 | -0.07 [-0.51, 0.34] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -1.17 | 23 | = 0.789 | -0.19 [-0.67, 0.19] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.01 | 23 | = 0.996 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.93 | 23 | = 0.789 | -0.17 [-0.62, 0.24] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.90 | 23 | = 0.701 | -0.27 [-0.83, 0.05] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.44 | 23 | = 0.789 | -0.10 [-0.51, 0.33] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.56 | 23 | = 0.789 | -0.12 [-0.54, 0.31] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.38 | 23 | = 0.789 | 0.06 [-0.35, 0.50] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.68 | 23 | = 0.789 | 0.17 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1185.22, BIC = 1207.52
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 5.51, *SE* = 8.163, *z* = 0.676, *p* = 0.499
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 10.07, *SE* = 8.248, *z* = 1.220, *p* = 0.222
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 15.40, *SE* = 8.365, *z* = 1.841, *p* = 0.066
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 10.30, *SE* = 8.543, *z* = 1.205, *p* = 0.228
- **SNR**: *β* = -1.05, *SE* = 0.643, *z* = -1.636, *p* = 0.102

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -5.52 | 8.16 | -0.68 | 0.499 | 0.984 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -10.07 | 8.25 | -1.22 | 0.222 | 0.896 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -15.40 | 8.37 | -1.84 | 0.066 | 0.493 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -10.30 | 8.54 | -1.21 | 0.228 | 0.896 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -4.55 | 8.18 | -0.56 | 0.578 | 0.984 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -9.88 | 8.27 | -1.20 | 0.232 | 0.896 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -4.78 | 8.41 | -0.57 | 0.569 | 0.984 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -5.33 | 8.17 | -0.65 | 0.514 | 0.984 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -0.23 | 8.25 | -0.03 | 0.978 | 0.984 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 5.10 | 8.18 | 0.62 | 0.533 | 0.984 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.46, *p* = 0.221, η²_G = 0.036
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.79 | 23 | = 0.627 | -0.18 [-0.59, 0.26] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.70 | 23 | = 0.489 | -0.36 [-0.78, 0.09] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -3.13 | 23 | = 0.047 | -0.59 [-1.10, -0.17] | medium | * |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -1.50 | 23 | = 0.489 | -0.40 [-0.74, 0.13] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.68 | 23 | = 0.633 | -0.17 [-0.56, 0.29] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.28 | 23 | = 0.536 | -0.38 [-0.69, 0.17] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.85 | 23 | = 0.627 | -0.22 [-0.60, 0.25] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.83 | 23 | = 0.627 | -0.20 [-0.59, 0.26] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.25 | 23 | = 0.802 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.46 | 23 | = 0.721 | 0.12 [-0.33, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 530.13, BIC = 552.43
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.39, *SE* = 0.444, *z* = 0.868, *p* = 0.386
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.68, *SE* = 0.449, *z* = 1.515, *p* = 0.130
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.37, *SE* = 0.457, *z* = 0.817, *p* = 0.414
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.45, *SE* = 0.468, *z* = -3.098, *p* = 0.002
- **SNR**: *β* = 0.11, *SE* = 0.038, *z* = 2.858, *p* = 0.004

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.39 | 0.44 | -0.87 | 0.386 | 0.912 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.68 | 0.45 | -1.52 | 0.130 | 0.565 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.37 | 0.46 | -0.82 | 0.414 | 0.912 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.45 | 0.47 | 3.10 | 0.002 | 0.014 | * |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.30 | 0.45 | -0.66 | 0.507 | 0.912 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.01 | 0.45 | 0.03 | 0.979 | 0.979 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 1.83 | 0.46 | 3.99 | < .001 | < .001 | *** |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.31 | 0.44 | 0.69 | 0.489 | 0.912 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 2.13 | 0.45 | 4.74 | < .001 | < .001 | *** |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 1.82 | 0.44 | 4.10 | < .001 | < .001 | *** |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 8.30, *p* < .001, η²_G = 0.058
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.665)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -1.18 | 23 | = 0.417 | -0.09 [-0.67, 0.19] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.47 | 23 | = 0.308 | -0.14 [-0.73, 0.13] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.13 | 23 | = 0.899 | -0.02 [-0.45, 0.40] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 4.16 | 23 | = 0.004 | 0.61 [0.36, 1.34] | medium | ** |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.42 | 23 | = 0.757 | -0.04 [-0.51, 0.34] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.56 | 23 | = 0.726 | 0.07 [-0.31, 0.54] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 3.86 | 23 | = 0.004 | 0.64 [0.31, 1.27] | medium | ** |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.79 | 23 | = 0.629 | 0.11 [-0.26, 0.59] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 3.66 | 23 | = 0.004 | 0.69 [0.27, 1.22] | medium | ** |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 3.63 | 23 | = 0.004 | 0.55 [0.26, 1.22] | medium | ** |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Ratio 0.5 (1:2) showed greater amplitude than Ratio 0.83 (5:6) (*d* = 0.61)
  - Ratio 0.67 (2:3) showed greater amplitude than Ratio 0.83 (5:6) (*d* = 0.64)
  - Ratio 0.75 (3:4) showed greater amplitude than Ratio 0.83 (5:6) (*d* = 0.69)
  - Ratio 0.8 (4:5) showed greater amplitude than Ratio 0.83 (5:6) (*d* = 0.55)

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
