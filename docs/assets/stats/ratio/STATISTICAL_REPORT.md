# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:48:48

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
| Ratio 0.5 (1:2) | 8 | 102.00 ms | 10.69 | 3.78 | [92.00, 112.00] |
| Ratio 0.67 (2:3) | 8 | 104.50 ms | 8.93 | 3.16 | [92.00, 112.00] |
| Ratio 0.75 (3:4) | 11 | 101.09 ms | 9.48 | 2.86 | [92.00, 112.00] |
| Ratio 0.8 (4:5) | 9 | 101.33 ms | 10.20 | 3.40 | [92.00, 112.00] |
| Ratio 0.83 (5:6) | 11 | 104.73 ms | 10.09 | 3.04 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 8 | 1.13 µV | 0.70 | 0.25 | [0.20, 2.19] |
| Ratio 0.67 (2:3) | 8 | 1.59 µV | 0.69 | 0.24 | [0.50, 2.79] |
| Ratio 0.75 (3:4) | 11 | 1.43 µV | 1.17 | 0.35 | [0.66, 4.63] |
| Ratio 0.8 (4:5) | 9 | 2.03 µV | 1.34 | 0.45 | [0.65, 4.26] |
| Ratio 0.83 (5:6) | 11 | 1.48 µV | 1.07 | 0.32 | [0.39, 4.30] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 23 | 171.48 ms | 14.39 | 3.00 | [144.00, 204.00] |
| Ratio 0.67 (2:3) | 23 | 173.22 ms | 19.24 | 4.01 | [144.00, 204.00] |
| Ratio 0.75 (3:4) | 23 | 170.96 ms | 17.65 | 3.68 | [144.00, 204.00] |
| Ratio 0.8 (4:5) | 23 | 170.61 ms | 20.52 | 4.28 | [144.00, 204.00] |
| Ratio 0.83 (5:6) | 24 | 175.50 ms | 18.06 | 3.69 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 23 | -5.12 µV | 2.14 | 0.45 | [-9.31, -1.91] |
| Ratio 0.67 (2:3) | 23 | -5.13 µV | 2.19 | 0.46 | [-9.87, -1.99] |
| Ratio 0.75 (3:4) | 23 | -5.41 µV | 2.20 | 0.46 | [-10.31, -0.44] |
| Ratio 0.8 (4:5) | 23 | -5.56 µV | 2.48 | 0.52 | [-10.71, -1.29] |
| Ratio 0.83 (5:6) | 24 | -5.52 µV | 1.99 | 0.41 | [-9.96, -2.06] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 105.60 ms | 7.38 | 1.90 | [92.00, 112.00] |
| Ratio 0.67 (2:3) | 13 | 106.15 ms | 6.66 | 1.85 | [92.00, 112.00] |
| Ratio 0.75 (3:4) | 14 | 104.29 ms | 7.76 | 2.07 | [92.00, 112.00] |
| Ratio 0.8 (4:5) | 12 | 103.00 ms | 8.88 | 2.56 | [92.00, 112.00] |
| Ratio 0.83 (5:6) | 13 | 103.08 ms | 7.51 | 2.08 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 15 | 1.78 µV | 1.32 | 0.34 | [0.26, 5.34] |
| Ratio 0.67 (2:3) | 13 | 1.99 µV | 1.52 | 0.42 | [0.34, 4.44] |
| Ratio 0.75 (3:4) | 14 | 2.19 µV | 1.62 | 0.43 | [0.33, 5.67] |
| Ratio 0.8 (4:5) | 12 | 2.98 µV | 1.69 | 0.49 | [0.82, 5.75] |
| Ratio 0.83 (5:6) | 13 | 2.00 µV | 1.39 | 0.38 | [0.37, 4.00] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 483.20 ms | 34.50 | 7.71 | [436.00, 540.00] |
| Ratio 0.67 (2:3) | 18 | 491.11 ms | 35.55 | 8.38 | [436.00, 540.00] |
| Ratio 0.75 (3:4) | 18 | 491.11 ms | 34.59 | 8.15 | [436.00, 540.00] |
| Ratio 0.8 (4:5) | 16 | 500.25 ms | 28.79 | 7.20 | [452.00, 540.00] |
| Ratio 0.83 (5:6) | 12 | 490.33 ms | 42.45 | 12.25 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 20 | 4.16 µV | 2.59 | 0.58 | [0.62, 8.88] |
| Ratio 0.67 (2:3) | 18 | 5.06 µV | 3.12 | 0.73 | [1.19, 12.42] |
| Ratio 0.75 (3:4) | 18 | 5.30 µV | 2.95 | 0.69 | [1.66, 11.73] |
| Ratio 0.8 (4:5) | 16 | 5.39 µV | 3.04 | 0.76 | [1.32, 11.33] |
| Ratio 0.83 (5:6) | 12 | 3.56 µV | 2.55 | 0.74 | [1.14, 9.58] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 352.78, BIC = 367.59
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.86, *SE* = 3.995, *z* = -0.216, *p* = 0.829
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -2.68, *SE* = 3.561, *z* = -0.752, *p* = 0.452
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -2.94, *SE* = 3.923, *z* = -0.749, *p* = 0.454
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.26, *SE* = 3.752, *z* = 0.070, *p* = 0.944
- **SNR**: *β* = 0.53, *SE* = 1.604, *z* = 0.330, *p* = 0.742

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.86 | 3.99 | 0.22 | 0.829 | 0.997 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 2.68 | 3.56 | 0.75 | 0.452 | 0.994 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 2.94 | 3.92 | 0.75 | 0.454 | 0.994 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.26 | 3.75 | -0.07 | 0.944 | 0.997 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 1.81 | 3.56 | 0.51 | 0.611 | 0.994 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 2.07 | 3.72 | 0.56 | 0.577 | 0.994 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -1.13 | 3.80 | -0.30 | 0.767 | 0.997 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.26 | 3.50 | 0.07 | 0.941 | 0.997 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -2.94 | 3.48 | -0.85 | 0.398 | 0.994 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -3.20 | 3.83 | -0.84 | 0.403 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.500, η²_G = 0.186
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -1.00 | 1 | = 0.500 | -0.34 [-2.48, 2.48] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | nan | 1 | n/a | 0.00 [-0.69, 2.08] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | nan | 1 | n/a | 0.00 [-2.11, 3.26] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -1.00 | 1 | = 0.500 | -1.00 [-2.19, 1.19] | large | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 1.00 | 1 | = 0.500 | 0.34 [-0.68, 2.10] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 1.00 | 1 | = 0.500 | 0.34 [-1.41, 1.81] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -1.00 | 1 | = 0.500 | -1.00 [-2.19, 1.19] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | nan | 1 | n/a | 0.00 [-0.80, 1.33] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.00 | 1 | = 0.500 | -1.00 [-2.48, 2.48] | large | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -1.00 | 1 | = 0.500 | -1.00 [-1.24, 1.24] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 117.58, BIC = 132.38
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.05, *SE* = 0.348, *z* = -0.132, *p* = 0.895
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.36, *SE* = 0.306, *z* = 1.188, *p* = 0.235
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.36, *SE* = 0.333, *z* = 1.075, *p* = 0.282
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.67, *SE* = 0.314, *z* = 2.138, *p* = 0.033
- **SNR**: *β* = 0.77, *SE* = 0.135, *z* = 5.661, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.05 | 0.35 | 0.13 | 0.895 | 0.989 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.36 | 0.31 | -1.19 | 0.235 | 0.822 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.36 | 0.33 | -1.08 | 0.282 | 0.822 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.67 | 0.31 | -2.14 | 0.033 | 0.270 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.41 | 0.31 | -1.31 | 0.190 | 0.815 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.40 | 0.33 | -1.23 | 0.218 | 0.822 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.72 | 0.33 | -2.16 | 0.031 | 0.270 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.01 | 0.30 | 0.02 | 0.984 | 0.989 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -0.31 | 0.29 | -1.05 | 0.293 | 0.822 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -0.31 | 0.33 | -0.96 | 0.335 | 0.822 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.16, *p* = 0.949, η²_G = 0.100
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 3.28 | 1 | = 0.864 | 1.41 [-2.37, 2.61] | large | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.39 | 1 | = 0.864 | 0.48 [-1.49, 1.02] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.25 | 1 | = 0.864 | -0.20 [-3.27, 2.10] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.25 | 1 | = 0.864 | -0.23 [-1.92, 1.33] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.22 | 1 | = 0.864 | -0.29 [-1.42, 1.08] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.18 | 1 | = 0.864 | -0.72 [-3.66, 0.84] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.58 | 1 | = 0.864 | -0.48 [-1.83, 1.39] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.32 | 1 | = 0.864 | -0.45 [-1.09, 1.01] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.29 | 1 | = 0.864 | -0.37 [-2.75, 2.29] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.25 | 1 | = 0.864 | -0.13 [-0.96, 1.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 966.09, BIC = 988.12
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 1.49, *SE* = 3.554, *z* = 0.420, *p* = 0.675
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.13, *SE* = 3.731, *z* = -0.304, *p* = 0.761
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.38, *SE* = 3.668, *z* = -0.376, *p* = 0.707
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 2.79, *SE* = 3.671, *z* = 0.761, *p* = 0.447
- **SNR**: *β* = -0.15, *SE* = 0.302, *z* = -0.493, *p* = 0.622

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -1.49 | 3.55 | -0.42 | 0.675 | 0.996 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.13 | 3.73 | 0.30 | 0.761 | 0.996 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.38 | 3.67 | 0.38 | 0.707 | 0.996 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -2.79 | 3.67 | -0.76 | 0.447 | 0.987 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 2.62 | 3.59 | 0.73 | 0.465 | 0.987 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 2.87 | 3.56 | 0.81 | 0.420 | 0.987 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -1.30 | 3.55 | -0.37 | 0.714 | 0.996 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.25 | 3.52 | 0.07 | 0.944 | 0.996 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -3.93 | 3.51 | -1.12 | 0.263 | 0.936 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -4.17 | 3.50 | -1.19 | 0.234 | 0.930 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.38, *p* = 0.820, η²_G = 0.006
- Greenhouse-Geisser corrected: *p* = 0.748 (ε = 0.689)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.56 | 22 | = 0.933 | -0.10 [-0.55, 0.32] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.14 | 22 | = 0.933 | 0.03 [-0.40, 0.46] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.38 | 22 | = 0.933 | 0.05 [-0.35, 0.51] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.76 | 22 | = 0.933 | -0.17 [-0.59, 0.28] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.78 | 22 | = 0.933 | 0.12 [-0.27, 0.60] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.72 | 22 | = 0.933 | 0.13 [-0.28, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.30 | 22 | = 0.933 | -0.06 [-0.50, 0.37] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.09 | 22 | = 0.933 | 0.02 [-0.41, 0.45] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.92 | 22 | = 0.933 | -0.19 [-0.63, 0.25] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.76 | 22 | = 0.933 | -0.19 [-0.59, 0.28] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 396.59, BIC = 418.62
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.30, *SE* = 0.285, *z* = -1.044, *p* = 0.297
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -0.98, *SE* = 0.300, *z* = -3.284, *p* = 0.001
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.02, *SE* = 0.294, *z* = -3.461, *p* = 0.001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.07, *SE* = 0.295, *z* = -3.617, *p* < .001
- **SNR**: *β* = -0.17, *SE* = 0.025, *z* = -6.722, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.30 | 0.28 | 1.04 | 0.297 | 0.755 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 0.98 | 0.30 | 3.28 | 0.001 | 0.008 | ** |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.02 | 0.29 | 3.46 | < .001 | 0.005 | ** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.07 | 0.30 | 3.62 | < .001 | 0.003 | ** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.69 | 0.29 | 2.38 | 0.017 | 0.083 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.72 | 0.29 | 2.53 | 0.011 | 0.066 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.77 | 0.29 | 2.70 | 0.007 | 0.047 | * |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.03 | 0.28 | 0.12 | 0.902 | 0.987 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.08 | 0.28 | 0.30 | 0.767 | 0.987 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.05 | 0.28 | 0.17 | 0.863 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.89, *p* = 0.474, η²_G = 0.009
- Greenhouse-Geisser corrected: *p* = 0.449 (ε = 0.725)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.10 | 22 | = 0.933 | 0.01 [-0.41, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.83 | 22 | = 0.796 | 0.14 [-0.26, 0.61] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 1.13 | 22 | = 0.710 | 0.19 [-0.20, 0.67] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.61 | 22 | = 0.710 | 0.23 [-0.11, 0.78] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.72 | 22 | = 0.796 | 0.13 [-0.28, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 1.10 | 22 | = 0.710 | 0.18 [-0.21, 0.67] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.42 | 22 | = 0.710 | 0.22 [-0.15, 0.74] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.46 | 22 | = 0.811 | 0.06 [-0.34, 0.53] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.51 | 22 | = 0.811 | 0.09 [-0.33, 0.54] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.09 | 22 | = 0.933 | 0.01 [-0.41, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 440.32, BIC = 457.96
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -1.25, *SE* = 1.623, *z* = -0.773, *p* = 0.440
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -0.47, *SE* = 1.664, *z* = -0.285, *p* = 0.775
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.65, *SE* = 1.691, *z* = -0.382, *p* = 0.702
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.17, *SE* = 1.692, *z* = -0.691, *p* = 0.490
- **SNR**: *β* = 0.20, *SE* = 0.239, *z* = 0.836, *p* = 0.403

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 1.25 | 1.62 | 0.77 | 0.440 | 0.997 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 0.47 | 1.66 | 0.29 | 0.775 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.65 | 1.69 | 0.38 | 0.702 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.17 | 1.69 | 0.69 | 0.490 | 0.998 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.78 | 1.74 | -0.45 | 0.654 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.61 | 1.76 | -0.34 | 0.731 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.08 | 1.75 | -0.05 | 0.961 | 1.000 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.17 | 1.76 | 0.10 | 0.922 | 1.000 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.69 | 1.72 | 0.40 | 0.687 | 1.000 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.52 | 1.74 | 0.30 | 0.763 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.35, *p* = 0.293, η²_G = 0.091
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 1.00 | 4 | = 0.467 | 0.16 [-0.22, 1.20] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 1.37 | 4 | = 0.467 | 0.60 [-0.76, 0.67] | medium | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -1.00 | 4 | = 0.467 | -0.20 [-0.43, 0.94] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.18 | 4 | = 0.467 | 0.45 [-0.54, 0.90] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.88 | 4 | = 0.474 | 0.41 [-0.84, 0.84] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.63 | 4 | = 0.467 | -0.34 [-1.45, 0.23] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.00 | 4 | = 0.467 | 0.27 [-0.57, 1.13] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -1.58 | 4 | = 0.467 | -0.80 [-0.91, 0.77] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.25 | 4 | = 0.815 | -0.13 [-0.91, 0.76] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 2.14 | 4 | = 0.467 | 0.64 [-0.35, 1.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 195.83, BIC = 213.46
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.37, *SE* = 0.286, *z* = 1.305, *p* = 0.192
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.67, *SE* = 0.291, *z* = 2.290, *p* = 0.022
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 1.40, *SE* = 0.298, *z* = 4.700, *p* < .001
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.57, *SE* = 0.298, *z* = 1.907, *p* = 0.057
- **SNR**: *β* = 0.23, *SE* = 0.043, *z* = 5.344, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.37 | 0.29 | -1.31 | 0.192 | 0.573 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.67 | 0.29 | -2.29 | 0.022 | 0.125 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -1.40 | 0.30 | -4.70 | < .001 | < .001 | *** |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.57 | 0.30 | -1.91 | 0.057 | 0.253 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.29 | 0.30 | -0.97 | 0.331 | 0.700 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -1.03 | 0.31 | -3.34 | < .001 | 0.007 | ** |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -0.20 | 0.31 | -0.64 | 0.523 | 0.773 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.74 | 0.31 | -2.39 | 0.017 | 0.111 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.10 | 0.30 | 0.33 | 0.745 | 0.773 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.83 | 0.31 | 2.73 | 0.006 | 0.050 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.73, *p* = 0.585, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.49 | 4 | = 0.793 | -0.18 [-0.71, 0.63] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.12 | 4 | = 0.793 | -0.26 [-1.19, 0.31] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.90 | 4 | = 0.793 | -0.39 [-1.42, 0.07] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.28 | 4 | = 0.793 | 0.11 [-0.87, 0.57] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.33 | 4 | = 0.793 | -0.10 [-0.94, 0.73] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.60 | 4 | = 0.793 | -0.22 [-1.22, 0.38] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.73 | 4 | = 0.793 | 0.32 [-0.04, 2.00] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.33 | 4 | = 0.793 | -0.11 [-1.14, 0.57] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 1.06 | 4 | = 0.793 | 0.38 [-0.53, 1.18] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 1.71 | 4 | = 0.793 | 0.52 [-0.36, 1.43] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 829.22, BIC = 848.66
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 8.63, *SE* = 8.579, *z* = 1.006, *p* = 0.314
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 7.07, *SE* = 8.707, *z* = 0.811, *p* = 0.417
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 17.47, *SE* = 9.161, *z* = 1.907, *p* = 0.056
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 1.04, *SE* = 10.898, *z* = 0.095, *p* = 0.924
- **SNR**: *β* = -1.16, *SE* = 0.721, *z* = -1.606, *p* = 0.108

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -8.63 | 8.58 | -1.01 | 0.314 | 0.929 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -7.07 | 8.71 | -0.81 | 0.417 | 0.933 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -17.47 | 9.16 | -1.91 | 0.056 | 0.441 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -1.04 | 10.90 | -0.10 | 0.924 | 0.980 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 1.57 | 8.81 | 0.18 | 0.859 | 0.980 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -8.84 | 9.15 | -0.97 | 0.334 | 0.929 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 7.60 | 10.62 | 0.72 | 0.474 | 0.933 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -10.41 | 9.17 | -1.13 | 0.257 | 0.907 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 6.03 | 10.37 | 0.58 | 0.561 | 0.933 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 16.43 | 10.51 | 1.56 | 0.118 | 0.677 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.56, *p* = 0.055, η²_G = 0.105
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.15 | 9 | = 0.883 | 0.05 [-0.86, 0.16] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -0.27 | 9 | = 0.882 | -0.09 [-0.78, 0.26] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -3.44 | 9 | = 0.074 | -0.99 [-1.44, -0.21] | large | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.51 | 9 | = 0.882 | -0.19 [-0.99, 0.39] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.44 | 9 | = 0.882 | -0.14 [-0.54, 0.53] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -2.80 | 9 | = 0.099 | -1.00 [-0.83, 0.29] | large | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.89 | 9 | = 0.790 | -0.23 [-1.04, 0.34] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -2.58 | 9 | = 0.099 | -0.81 [-1.24, 0.01] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.34 | 9 | = 0.882 | -0.10 [-0.58, 0.69] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 1.91 | 9 | = 0.220 | 0.63 [-0.17, 1.38] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 354.43, BIC = 373.88
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 1.00, *SE* = 0.460, *z* = 2.174, *p* = 0.030
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 1.30, *SE* = 0.469, *z* = 2.773, *p* = 0.006
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 1.51, *SE* = 0.496, *z* = 3.047, *p* = 0.002
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -0.18, *SE* = 0.606, *z* = -0.304, *p* = 0.761
- **SNR**: *β* = 0.20, *SE* = 0.042, *z* = 4.918, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -1.00 | 0.46 | -2.17 | 0.030 | 0.166 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -1.30 | 0.47 | -2.77 | 0.006 | 0.044 | * |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -1.51 | 0.50 | -3.05 | 0.002 | 0.023 | * |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 0.18 | 0.61 | 0.30 | 0.761 | 0.891 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.30 | 0.47 | -0.64 | 0.522 | 0.891 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.51 | 0.49 | -1.04 | 0.297 | 0.755 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 1.18 | 0.58 | 2.04 | 0.042 | 0.191 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.21 | 0.49 | -0.43 | 0.669 | 0.891 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 1.49 | 0.56 | 2.63 | 0.008 | 0.058 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 1.70 | 0.57 | 2.98 | 0.003 | 0.025 | * |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.22, *p* = 0.023, η²_G = 0.132
- Greenhouse-Geisser corrected: *p* = 0.069 (ε = 0.460)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -2.28 | 9 | = 0.163 | -0.35 [-0.99, 0.06] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -0.90 | 9 | = 0.563 | -0.22 [-0.98, 0.10] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -1.07 | 9 | = 0.520 | -0.32 [-0.95, 0.16] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 2.07 | 9 | = 0.171 | 0.78 [-0.04, 1.46] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.32 | 9 | = 0.915 | 0.07 [-0.62, 0.45] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.11 | 9 | = 0.915 | 0.04 [-0.51, 0.59] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 2.37 | 9 | = 0.163 | 0.99 [0.02, 1.57] | large | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.13 | 9 | = 0.915 | -0.04 [-0.52, 0.63] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 1.79 | 9 | = 0.213 | 0.82 [-0.07, 1.32] | large | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 3.53 | 9 | = 0.064 | 0.98 [0.21, 2.03] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Marginal trend toward condition differences (*p* = 0.055)
**P3b amplitude:** Significant main effect of condition (*p* = 0.023) (no significant pairwise comparisons)

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
