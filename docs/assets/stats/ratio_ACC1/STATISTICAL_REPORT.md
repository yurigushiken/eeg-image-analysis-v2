# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:33:59

---

## 1. Analysis Overview

**Total Measurements:** 460
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
| Ratio 0.5 (1:2) | 24 | 103.50 ms | 8.37 | 1.71 | [92.00, 112.00] |
| Ratio 0.67 (2:3) | 24 | 102.83 ms | 7.78 | 1.59 | [92.00, 112.00] |
| Ratio 0.75 (3:4) | 24 | 102.67 ms | 7.70 | 1.57 | [92.00, 112.00] |
| Ratio 0.8 (4:5) | 24 | 103.33 ms | 7.33 | 1.50 | [92.00, 112.00] |
| Ratio 0.83 (5:6) | 19 | 102.32 ms | 7.92 | 1.82 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | -1.01 µV | 1.08 | 0.22 | [-3.83, 0.61] |
| Ratio 0.67 (2:3) | 24 | -1.04 µV | 1.38 | 0.28 | [-3.88, 1.37] |
| Ratio 0.75 (3:4) | 24 | -1.00 µV | 1.69 | 0.35 | [-5.60, 2.51] |
| Ratio 0.8 (4:5) | 24 | -2.08 µV | 2.59 | 0.53 | [-8.41, 1.59] |
| Ratio 0.83 (5:6) | 19 | -1.89 µV | 2.37 | 0.54 | [-6.40, 3.29] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 173.00 ms | 15.97 | 3.26 | [140.00, 204.00] |
| Ratio 0.67 (2:3) | 24 | 173.17 ms | 19.33 | 3.95 | [144.00, 204.00] |
| Ratio 0.75 (3:4) | 24 | 172.17 ms | 18.74 | 3.83 | [140.00, 204.00] |
| Ratio 0.8 (4:5) | 24 | 172.50 ms | 19.25 | 3.93 | [140.00, 204.00] |
| Ratio 0.83 (5:6) | 19 | 176.42 ms | 22.31 | 5.12 | [140.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | -5.11 µV | 2.10 | 0.43 | [-9.37, -1.80] |
| Ratio 0.67 (2:3) | 24 | -5.22 µV | 2.36 | 0.48 | [-10.09, -2.11] |
| Ratio 0.75 (3:4) | 24 | -5.52 µV | 2.36 | 0.48 | [-10.31, -0.04] |
| Ratio 0.8 (4:5) | 24 | -5.66 µV | 2.94 | 0.60 | [-11.24, 0.46] |
| Ratio 0.83 (5:6) | 19 | -6.04 µV | 2.61 | 0.60 | [-11.29, -1.78] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 108.17 ms | 8.54 | 1.74 | [96.00, 116.00] |
| Ratio 0.67 (2:3) | 24 | 108.00 ms | 8.42 | 1.72 | [96.00, 116.00] |
| Ratio 0.75 (3:4) | 24 | 105.33 ms | 8.64 | 1.76 | [96.00, 116.00] |
| Ratio 0.8 (4:5) | 24 | 107.00 ms | 7.85 | 1.60 | [96.00, 116.00] |
| Ratio 0.83 (5:6) | 19 | 105.89 ms | 8.26 | 1.89 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 1.17 µV | 1.59 | 0.32 | [-1.81, 5.03] |
| Ratio 0.67 (2:3) | 24 | 0.89 µV | 1.91 | 0.39 | [-2.21, 5.72] |
| Ratio 0.75 (3:4) | 24 | 1.12 µV | 1.83 | 0.37 | [-1.59, 5.67] |
| Ratio 0.8 (4:5) | 24 | 1.71 µV | 2.45 | 0.50 | [-2.97, 6.17] |
| Ratio 0.83 (5:6) | 19 | 2.38 µV | 3.96 | 0.91 | [-3.00, 16.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 485.33 ms | 34.12 | 6.96 | [444.00, 540.00] |
| Ratio 0.67 (2:3) | 24 | 488.50 ms | 36.42 | 7.43 | [444.00, 540.00] |
| Ratio 0.75 (3:4) | 24 | 494.33 ms | 31.80 | 6.49 | [444.00, 540.00] |
| Ratio 0.8 (4:5) | 24 | 494.00 ms | 33.59 | 6.86 | [444.00, 540.00] |
| Ratio 0.83 (5:6) | 19 | 502.11 ms | 34.68 | 7.96 | [444.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Ratio 0.5 (1:2) | 24 | 3.58 µV | 3.06 | 0.62 | [-2.52, 9.90] |
| Ratio 0.67 (2:3) | 24 | 4.01 µV | 3.78 | 0.77 | [-1.89, 14.05] |
| Ratio 0.75 (3:4) | 24 | 4.05 µV | 3.75 | 0.77 | [-3.66, 11.73] |
| Ratio 0.8 (4:5) | 24 | 4.25 µV | 3.81 | 0.78 | [-4.71, 10.40] |
| Ratio 0.83 (5:6) | 19 | 3.90 µV | 5.19 | 1.19 | [-3.89, 18.02] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 782.87, BIC = 804.82
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.75, *SE* = 1.697, *z* = -0.444, *p* = 0.657
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -0.84, *SE* = 1.680, *z* = -0.498, *p* = 0.619
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.19, *SE* = 1.681, *z* = -0.113, *p* = 0.910
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -1.11, *SE* = 1.807, *z* = -0.612, *p* = 0.541
- **SNR**: *β* = 0.16, *SE* = 0.437, *z* = 0.361, *p* = 0.718

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.75 | 1.70 | 0.44 | 0.657 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 0.84 | 1.68 | 0.50 | 0.619 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.19 | 1.68 | 0.11 | 0.910 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 1.11 | 1.81 | 0.61 | 0.541 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.08 | 1.70 | 0.05 | 0.961 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.56 | 1.69 | -0.33 | 0.739 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.35 | 1.82 | 0.19 | 0.846 | 1.000 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.65 | 1.68 | -0.38 | 0.701 | 1.000 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.27 | 1.81 | 0.15 | 0.882 | 1.000 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.92 | 1.81 | 0.51 | 0.612 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.928, η²_G = 0.005
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.72 | 18 | = 0.913 | 0.18 [-0.36, 0.49] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.33 | 18 | = 0.913 | 0.08 [-0.32, 0.53] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.25 | 18 | = 0.913 | 0.05 [-0.40, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.59 | 18 | = 0.913 | 0.15 [-0.35, 0.62] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.41 | 18 | = 0.913 | -0.11 [-0.40, 0.44] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.89 | 18 | = 0.913 | -0.14 [-0.49, 0.36] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.11 | 18 | = 0.913 | -0.03 [-0.51, 0.46] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.13 | 18 | = 0.913 | -0.03 [-0.52, 0.33] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.31 | 18 | = 0.913 | 0.08 [-0.41, 0.55] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.51 | 18 | = 0.913 | 0.11 [-0.37, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 455.13, BIC = 477.09
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.20, *SE* = 0.440, *z* = 0.464, *p* = 0.642
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.02, *SE* = 0.435, *z* = 0.041, *p* = 0.967
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.01, *SE* = 0.435, *z* = -2.325, *p* = 0.020
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -0.97, *SE* = 0.468, *z* = -2.085, *p* = 0.037
- **SNR**: *β* = -0.42, *SE* = 0.116, *z* = -3.654, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.20 | 0.44 | -0.46 | 0.642 | 0.984 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.02 | 0.43 | -0.04 | 0.967 | 0.996 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.01 | 0.44 | 2.32 | 0.020 | 0.135 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 0.98 | 0.47 | 2.09 | 0.037 | 0.186 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.19 | 0.44 | 0.42 | 0.671 | 0.984 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 1.22 | 0.44 | 2.78 | 0.005 | 0.053 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 1.18 | 0.47 | 2.52 | 0.012 | 0.102 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 1.03 | 0.44 | 2.37 | 0.018 | 0.135 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.99 | 0.47 | 2.12 | 0.034 | 0.186 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -0.04 | 0.47 | -0.08 | 0.937 | 0.996 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.29, *p* = 0.068, η²_G = 0.071
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.57 | 18 | = 0.601 | -0.17 [-0.40, 0.44] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.24 | 18 | = 0.383 | -0.30 [-0.43, 0.42] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.98 | 18 | = 0.483 | 0.30 [-0.01, 0.87] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.56 | 18 | = 0.271 | 0.47 [-0.14, 0.86] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.53 | 18 | = 0.601 | -0.13 [-0.45, 0.40] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 1.67 | 18 | = 0.271 | 0.39 [-0.02, 0.86] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.73 | 18 | = 0.271 | 0.54 [-0.10, 0.90] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 2.06 | 18 | = 0.271 | 0.49 [0.07, 0.96] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 2.35 | 18 | = 0.271 | 0.61 [0.02, 1.05] | medium | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.70 | 18 | = 0.601 | 0.22 [-0.33, 0.65] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 968.11, BIC = 990.07
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.11, *SE* = 3.678, *z* = -0.029, *p* = 0.977
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.34, *SE* = 3.888, *z* = -0.346, *p* = 0.730
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -0.99, *SE* = 3.866, *z* = -0.256, *p* = 0.798
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 2.62, *SE* = 4.362, *z* = 0.600, *p* = 0.548
- **SNR**: *β* = -0.10, *SE* = 0.299, *z* = -0.342, *p* = 0.732

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.11 | 3.68 | 0.03 | 0.977 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.34 | 3.89 | 0.35 | 0.730 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 0.99 | 3.87 | 0.26 | 0.798 | 1.000 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -2.62 | 4.36 | -0.60 | 0.548 | 0.996 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 1.24 | 3.66 | 0.34 | 0.735 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.88 | 3.65 | 0.24 | 0.808 | 1.000 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -2.72 | 4.05 | -0.67 | 0.502 | 0.996 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.35 | 3.59 | -0.10 | 0.922 | 1.000 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -3.96 | 3.90 | -1.02 | 0.310 | 0.975 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -3.61 | 3.91 | -0.92 | 0.356 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.697, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.629 (ε = 0.669)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.45 | 18 | = 0.819 | -0.09 [-0.43, 0.41] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.56 | 18 | = 0.819 | 0.13 [-0.38, 0.47] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.21 | 18 | = 0.834 | -0.03 [-0.38, 0.46] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -0.73 | 18 | = 0.819 | -0.18 [-0.65, 0.32] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 1.56 | 18 | = 0.819 | 0.21 [-0.35, 0.49] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.24 | 18 | = 0.834 | 0.05 [-0.39, 0.46] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -0.52 | 18 | = 0.819 | -0.09 [-0.60, 0.36] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.57 | 18 | = 0.819 | -0.15 [-0.44, 0.41] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.33 | 18 | = 0.819 | -0.29 [-0.80, 0.19] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.63 | 18 | = 0.819 | -0.14 [-0.63, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 473.40, BIC = 495.36
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.57, *SE* = 0.434, *z* = -1.311, *p* = 0.190
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -1.26, *SE* = 0.460, *z* = -2.731, *p* = 0.006
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.36, *SE* = 0.457, *z* = -2.974, *p* = 0.003
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -2.15, *SE* = 0.516, *z* = -4.176, *p* < .001
- **SNR**: *β* = -0.17, *SE* = 0.036, *z* = -4.682, *p* < .001

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.57 | 0.43 | 1.31 | 0.190 | 0.344 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 1.26 | 0.46 | 2.73 | 0.006 | 0.043 | * |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.36 | 0.46 | 2.97 | 0.003 | 0.023 | * |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 2.16 | 0.52 | 4.18 | < .001 | < .001 | *** |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 0.69 | 0.43 | 1.59 | 0.111 | 0.298 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 0.79 | 0.43 | 1.84 | 0.066 | 0.289 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 1.59 | 0.48 | 3.32 | < .001 | 0.008 | ** |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 0.10 | 0.42 | 0.25 | 0.806 | 0.806 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.90 | 0.46 | 1.96 | 0.050 | 0.266 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.80 | 0.46 | 1.73 | 0.084 | 0.296 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.67, *p* = 0.166, η²_G = 0.033
- Greenhouse-Geisser corrected: *p* = 0.190 (ε = 0.668)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 1.37 | 18 | = 0.439 | 0.11 [-0.31, 0.54] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.78 | 18 | = 0.556 | 0.19 [-0.24, 0.61] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 1.79 | 18 | = 0.299 | 0.39 [-0.17, 0.68] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 2.51 | 18 | = 0.216 | 0.51 [0.06, 1.10] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.34 | 18 | = 0.740 | 0.09 [-0.31, 0.54] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 1.27 | 18 | = 0.439 | 0.28 [-0.24, 0.61] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 2.05 | 18 | = 0.275 | 0.39 [-0.04, 0.98] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | 0.97 | 18 | = 0.492 | 0.19 [-0.37, 0.48] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 1.12 | 18 | = 0.462 | 0.29 [-0.23, 0.75] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.36 | 18 | = 0.740 | 0.09 [-0.40, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 779.65, BIC = 801.61
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.38, *SE* = 1.601, *z* = -0.235, *p* = 0.814
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = -3.25, *SE* = 1.649, *z* = -1.971, *p* = 0.049
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = -1.49, *SE* = 1.624, *z* = -0.919, *p* = 0.358
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = -2.51, *SE* = 1.811, *z* = -1.384, *p* = 0.166
- **SNR**: *β* = -0.31, *SE* = 0.336, *z* = -0.912, *p* = 0.362

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.38 | 1.60 | 0.24 | 0.814 | 0.928 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | 3.25 | 1.65 | 1.97 | 0.049 | 0.393 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | 1.49 | 1.62 | 0.92 | 0.358 | 0.891 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | 2.51 | 1.81 | 1.38 | 0.166 | 0.766 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | 2.87 | 1.60 | 1.80 | 0.073 | 0.492 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | 1.12 | 1.59 | 0.70 | 0.483 | 0.928 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 2.13 | 1.75 | 1.22 | 0.223 | 0.828 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -1.76 | 1.59 | -1.11 | 0.268 | 0.846 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -0.74 | 1.71 | -0.43 | 0.664 | 0.928 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 1.02 | 1.72 | 0.59 | 0.556 | 0.928 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.765, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.25 | 18 | = 0.823 | 0.05 [-0.40, 0.45] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 1.11 | 18 | = 0.823 | 0.24 [-0.08, 0.79] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | 0.54 | 18 | = 0.823 | 0.10 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 1.03 | 18 | = 0.823 | 0.19 [-0.25, 0.73] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.70 | 18 | = 0.823 | 0.19 [-0.17, 0.69] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | 0.35 | 18 | = 0.823 | 0.05 [-0.27, 0.58] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 0.60 | 18 | = 0.823 | 0.15 [-0.35, 0.62] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.65 | 18 | = 0.823 | -0.15 [-0.62, 0.23] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -0.23 | 18 | = 0.823 | -0.05 [-0.53, 0.43] | negligible | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 0.52 | 18 | = 0.823 | 0.10 [-0.36, 0.60] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 515.73, BIC = 537.69
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = -0.15, *SE* = 0.547, *z* = -0.272, *p* = 0.786
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.21, *SE* = 0.563, *z* = 0.377, *p* = 0.706
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 0.75, *SE* = 0.555, *z* = 1.345, *p* = 0.179
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 1.69, *SE* = 0.616, *z* = 2.742, *p* = 0.006
- **SNR**: *β* = 0.19, *SE* = 0.113, *z* = 1.712, *p* = 0.087

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | 0.15 | 0.55 | 0.27 | 0.786 | 0.914 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.21 | 0.56 | -0.38 | 0.706 | 0.914 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -0.75 | 0.55 | -1.34 | 0.179 | 0.626 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -1.69 | 0.62 | -2.74 | 0.006 | 0.054 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.36 | 0.55 | -0.66 | 0.509 | 0.882 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.89 | 0.54 | -1.65 | 0.100 | 0.520 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -1.84 | 0.59 | -3.09 | 0.002 | 0.020 | * |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.53 | 0.54 | -0.98 | 0.325 | 0.793 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -1.48 | 0.58 | -2.53 | 0.011 | 0.088 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -0.94 | 0.59 | -1.61 | 0.108 | 0.520 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.90, *p* = 0.121, η²_G = 0.054
- Greenhouse-Geisser corrected: *p* = 0.171 (ε = 0.440)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | 0.97 | 18 | = 0.569 | 0.15 [-0.18, 0.68] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | 0.07 | 18 | = 0.946 | 0.01 [-0.38, 0.46] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -0.76 | 18 | = 0.569 | -0.18 [-0.71, 0.15] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -1.53 | 18 | = 0.477 | -0.46 [-0.85, 0.15] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.59 | 18 | = 0.627 | -0.13 [-0.56, 0.29] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -1.35 | 18 | = 0.483 | -0.28 [-0.84, 0.04] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -1.80 | 18 | = 0.477 | -0.52 [-0.92, 0.09] | medium | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.78 | 18 | = 0.569 | -0.18 [-0.72, 0.14] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.60 | 18 | = 0.477 | -0.46 [-0.86, 0.13] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -1.01 | 18 | = 0.569 | -0.31 [-0.72, 0.26] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1117.36, BIC = 1139.32
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 2.65, *SE* = 7.080, *z* = 0.374, *p* = 0.708
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 7.51, *SE* = 7.139, *z* = 1.052, *p* = 0.293
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 5.80, *SE* = 7.319, *z* = 0.792, *p* = 0.428
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 12.14, *SE* = 8.388, *z* = 1.448, *p* = 0.148
- **SNR**: *β* = -1.00, *SE* = 0.660, *z* = -1.522, *p* = 0.128

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -2.65 | 7.08 | -0.37 | 0.708 | 0.977 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -7.51 | 7.14 | -1.05 | 0.293 | 0.937 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -5.80 | 7.32 | -0.79 | 0.428 | 0.977 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -12.14 | 8.39 | -1.45 | 0.148 | 0.798 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -4.86 | 7.10 | -0.68 | 0.493 | 0.977 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -3.15 | 7.24 | -0.44 | 0.663 | 0.977 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | -9.49 | 8.25 | -1.15 | 0.250 | 0.925 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | 1.71 | 7.13 | 0.24 | 0.810 | 0.977 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | -4.63 | 8.03 | -0.58 | 0.564 | 0.977 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | -6.34 | 7.78 | -0.81 | 0.415 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.66, *p* = 0.170, η²_G = 0.044
- Greenhouse-Geisser corrected: *p* = 0.190 (ε = 0.709)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -0.99 | 18 | = 0.524 | -0.20 [-0.53, 0.31] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.26 | 18 | = 0.488 | -0.39 [-0.66, 0.20] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -1.93 | 18 | = 0.345 | -0.42 [-0.69, 0.17] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | -2.00 | 18 | = 0.345 | -0.62 [-0.97, 0.05] | medium | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | -0.78 | 18 | = 0.524 | -0.16 [-0.64, 0.22] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.74 | 18 | = 0.524 | -0.20 [-0.56, 0.29] | small | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | -1.53 | 18 | = 0.480 | -0.39 [-0.85, 0.15] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.16 | 18 | = 0.878 | -0.05 [-0.41, 0.43] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | -1.20 | 18 | = 0.488 | -0.26 [-0.77, 0.21] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | -0.83 | 18 | = 0.524 | -0.20 [-0.68, 0.30] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 569.04, BIC = 591.00
- **Ratio 0.67 (2:3) vs Ratio 0.5 (1:2)**: *β* = 0.50, *SE* = 0.602, *z* = 0.832, *p* = 0.406
- **Ratio 0.75 (3:4) vs Ratio 0.5 (1:2)**: *β* = 0.68, *SE* = 0.608, *z* = 1.115, *p* = 0.265
- **Ratio 0.8 (4:5) vs Ratio 0.5 (1:2)**: *β* = 1.07, *SE* = 0.625, *z* = 1.713, *p* = 0.087
- **Ratio 0.83 (5:6) vs Ratio 0.5 (1:2)**: *β* = 0.28, *SE* = 0.728, *z* = 0.383, *p* = 0.702
- **SNR**: *β* = 0.14, *SE* = 0.060, *z* = 2.353, *p* = 0.019

_Reference condition: **Ratio 0.5 (1:2)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Ratio 0.5 (1:2) - Ratio 0.67 (2:3) | -0.50 | 0.60 | -0.83 | 0.406 | 0.956 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.75 (3:4) | -0.68 | 0.61 | -1.12 | 0.265 | 0.915 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.8 (4:5) | -1.07 | 0.63 | -1.71 | 0.087 | 0.596 | n.s. |
| Ratio 0.5 (1:2) - Ratio 0.83 (5:6) | -0.28 | 0.73 | -0.38 | 0.702 | 0.974 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.75 (3:4) | -0.18 | 0.60 | -0.29 | 0.769 | 0.974 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.8 (4:5) | -0.57 | 0.62 | -0.92 | 0.356 | 0.954 | n.s. |
| Ratio 0.67 (2:3) - Ratio 0.83 (5:6) | 0.22 | 0.71 | 0.31 | 0.756 | 0.974 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.8 (4:5) | -0.39 | 0.61 | -0.65 | 0.517 | 0.974 | n.s. |
| Ratio 0.75 (3:4) - Ratio 0.83 (5:6) | 0.40 | 0.69 | 0.58 | 0.564 | 0.974 | n.s. |
| Ratio 0.8 (4:5) - Ratio 0.83 (5:6) | 0.79 | 0.67 | 1.19 | 0.236 | 0.911 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.374, η²_G = 0.017
- Greenhouse-Geisser corrected: *p* = 0.341 (ε = 0.399)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Ratio 0.5 (1:2) vs Ratio 0.67 (2:3) | -2.52 | 18 | = 0.140 | -0.22 [-0.75, 0.11] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.75 (3:4) | -1.15 | 18 | = 0.596 | -0.15 [-0.69, 0.17] | negligible | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.8 (4:5) | -2.39 | 18 | = 0.140 | -0.27 [-0.78, 0.09] | small | n.s. |
| Ratio 0.5 (1:2) vs Ratio 0.83 (5:6) | 0.49 | 18 | = 0.739 | 0.11 [-0.37, 0.60] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.75 (3:4) | 0.42 | 18 | = 0.739 | 0.06 [-0.44, 0.40] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.8 (4:5) | -0.34 | 18 | = 0.739 | -0.03 [-0.56, 0.28] | negligible | n.s. |
| Ratio 0.67 (2:3) vs Ratio 0.83 (5:6) | 1.07 | 18 | = 0.596 | 0.27 [-0.24, 0.73] | small | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.8 (4:5) | -0.59 | 18 | = 0.739 | -0.09 [-0.50, 0.34] | negligible | n.s. |
| Ratio 0.75 (3:4) vs Ratio 0.83 (5:6) | 0.84 | 18 | = 0.682 | 0.21 [-0.29, 0.68] | small | n.s. |
| Ratio 0.8 (4:5) vs Ratio 0.83 (5:6) | 1.35 | 18 | = 0.596 | 0.30 [-0.18, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Marginal trend toward condition differences (*p* = 0.068)

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
