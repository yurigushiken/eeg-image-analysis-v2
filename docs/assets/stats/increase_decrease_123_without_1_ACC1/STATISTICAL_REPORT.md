# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:25:41

---

## 1. Analysis Overview

**Total Measurements:** 672
**Number of Subjects:** 24
**Number of Conditions:** 7

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
| Cardinality (no change, no 1) | 24 | 105.83 ms | 7.27 | 1.48 | [92.00, 112.00] |
| Decrease by 1 (no 1) | 24 | 103.50 ms | 7.67 | 1.57 | [92.00, 112.00] |
| Decrease by 2 (no 1) | 24 | 105.50 ms | 7.35 | 1.50 | [92.00, 112.00] |
| Decrease by 3 (no 1) | 24 | 103.50 ms | 7.85 | 1.60 | [92.00, 112.00] |
| Increase by 1 (no 1) | 24 | 101.00 ms | 7.58 | 1.55 | [92.00, 112.00] |
| Increase by 2 (no 1) | 24 | 101.67 ms | 8.08 | 1.65 | [92.00, 112.00] |
| Increase by 3 (no 1) | 24 | 101.50 ms | 8.16 | 1.66 | [92.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | -1.22 µV | 1.53 | 0.31 | [-4.72, 0.98] |
| Decrease by 1 (no 1) | 24 | -0.90 µV | 1.68 | 0.34 | [-4.76, 1.82] |
| Decrease by 2 (no 1) | 24 | -1.64 µV | 1.50 | 0.31 | [-6.06, 2.21] |
| Decrease by 3 (no 1) | 24 | -1.71 µV | 1.87 | 0.38 | [-5.62, 2.33] |
| Increase by 1 (no 1) | 24 | -1.48 µV | 1.47 | 0.30 | [-3.95, 1.21] |
| Increase by 2 (no 1) | 24 | -1.40 µV | 1.31 | 0.27 | [-3.67, 0.32] |
| Increase by 3 (no 1) | 24 | -1.32 µV | 1.66 | 0.34 | [-5.70, 1.08] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 173.00 ms | 19.25 | 3.93 | [140.00, 208.00] |
| Decrease by 1 (no 1) | 24 | 176.83 ms | 18.65 | 3.81 | [140.00, 208.00] |
| Decrease by 2 (no 1) | 24 | 173.50 ms | 15.28 | 3.12 | [140.00, 208.00] |
| Decrease by 3 (no 1) | 24 | 175.83 ms | 17.35 | 3.54 | [152.00, 208.00] |
| Increase by 1 (no 1) | 24 | 165.33 ms | 19.30 | 3.94 | [140.00, 208.00] |
| Increase by 2 (no 1) | 24 | 169.17 ms | 18.14 | 3.70 | [140.00, 200.00] |
| Increase by 3 (no 1) | 24 | 169.50 ms | 21.16 | 4.32 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | -5.08 µV | 2.35 | 0.48 | [-10.60, -0.82] |
| Decrease by 1 (no 1) | 24 | -5.50 µV | 2.10 | 0.43 | [-9.73, -1.93] |
| Decrease by 2 (no 1) | 24 | -5.67 µV | 2.22 | 0.45 | [-10.30, -1.75] |
| Decrease by 3 (no 1) | 24 | -6.44 µV | 2.41 | 0.49 | [-10.52, -1.96] |
| Increase by 1 (no 1) | 24 | -5.18 µV | 2.22 | 0.45 | [-9.45, -0.49] |
| Increase by 2 (no 1) | 24 | -5.45 µV | 2.62 | 0.53 | [-10.99, -1.19] |
| Increase by 3 (no 1) | 24 | -6.33 µV | 2.50 | 0.51 | [-13.29, -2.62] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 105.00 ms | 10.57 | 2.16 | [92.00, 116.00] |
| Decrease by 1 (no 1) | 24 | 107.00 ms | 9.23 | 1.88 | [92.00, 116.00] |
| Decrease by 2 (no 1) | 24 | 107.83 ms | 8.79 | 1.79 | [92.00, 116.00] |
| Decrease by 3 (no 1) | 24 | 104.83 ms | 10.42 | 2.13 | [92.00, 116.00] |
| Increase by 1 (no 1) | 24 | 104.33 ms | 9.28 | 1.89 | [92.00, 116.00] |
| Increase by 2 (no 1) | 24 | 103.17 ms | 10.21 | 2.08 | [92.00, 116.00] |
| Increase by 3 (no 1) | 24 | 100.83 ms | 8.42 | 1.72 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 1.13 µV | 1.86 | 0.38 | [-1.43, 5.25] |
| Decrease by 1 (no 1) | 24 | 0.67 µV | 1.93 | 0.39 | [-1.87, 5.06] |
| Decrease by 2 (no 1) | 24 | 1.36 µV | 1.92 | 0.39 | [-3.30, 4.48] |
| Decrease by 3 (no 1) | 24 | 1.63 µV | 1.69 | 0.34 | [-1.66, 5.70] |
| Increase by 1 (no 1) | 24 | 1.62 µV | 1.88 | 0.38 | [-1.16, 5.16] |
| Increase by 2 (no 1) | 24 | 1.42 µV | 1.61 | 0.33 | [-1.36, 4.87] |
| Increase by 3 (no 1) | 24 | 1.42 µV | 2.40 | 0.49 | [-1.42, 8.91] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 465.00 ms | 26.36 | 5.38 | [420.00, 516.00] |
| Decrease by 1 (no 1) | 24 | 485.50 ms | 28.18 | 5.75 | [440.00, 536.00] |
| Decrease by 2 (no 1) | 24 | 478.00 ms | 33.94 | 6.93 | [436.00, 536.00] |
| Decrease by 3 (no 1) | 24 | 478.50 ms | 34.49 | 7.04 | [420.00, 536.00] |
| Increase by 1 (no 1) | 24 | 488.67 ms | 38.63 | 7.89 | [420.00, 536.00] |
| Increase by 2 (no 1) | 24 | 492.83 ms | 34.29 | 7.00 | [428.00, 536.00] |
| Increase by 3 (no 1) | 24 | 472.33 ms | 39.60 | 8.08 | [420.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality (no change, no 1) | 24 | 1.31 µV | 2.80 | 0.57 | [-4.73, 6.88] |
| Decrease by 1 (no 1) | 24 | 4.06 µV | 3.35 | 0.68 | [-2.22, 11.40] |
| Decrease by 2 (no 1) | 24 | 3.82 µV | 3.02 | 0.62 | [-1.29, 8.89] |
| Decrease by 3 (no 1) | 24 | 4.31 µV | 3.75 | 0.76 | [-1.53, 13.58] |
| Increase by 1 (no 1) | 24 | 3.28 µV | 3.85 | 0.78 | [-4.39, 9.74] |
| Increase by 2 (no 1) | 24 | 4.03 µV | 3.62 | 0.74 | [-3.39, 9.72] |
| Increase by 3 (no 1) | 24 | 4.15 µV | 2.48 | 0.51 | [0.70, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1117.75, BIC = 1148.99
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.01, *SE* = 1.612, *z* = -1.247, *p* = 0.212
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.43, *SE* = 1.609, *z* = -0.268, *p* = 0.788
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -2.16, *SE* = 1.609, *z* = -1.342, *p* = 0.180
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.73, *SE* = 1.609, *z* = -2.941, *p* = 0.003
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.94, *SE* = 1.610, *z* = -2.447, *p* = 0.014
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.80, *SE* = 1.618, *z* = -2.347, *p* = 0.019
- **SNR**: *β* = 0.84, *SE* = 0.278, *z* = 3.007, *p* = 0.003

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 2.01 | 1.61 | 1.25 | 0.212 | 0.943 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.43 | 1.61 | 0.27 | 0.788 | 0.991 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 2.16 | 1.61 | 1.34 | 0.180 | 0.924 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 4.73 | 1.61 | 2.94 | 0.003 | 0.066 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 3.94 | 1.61 | 2.45 | 0.014 | 0.241 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 3.80 | 1.62 | 2.35 | 0.019 | 0.291 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -1.58 | 1.61 | -0.98 | 0.328 | 0.955 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.15 | 1.61 | 0.09 | 0.926 | 0.994 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 2.72 | 1.61 | 1.69 | 0.091 | 0.761 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 1.93 | 1.61 | 1.20 | 0.230 | 0.944 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 1.79 | 1.61 | 1.11 | 0.266 | 0.955 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 1.73 | 1.61 | 1.07 | 0.283 | 0.955 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 4.30 | 1.61 | 2.67 | 0.008 | 0.141 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 3.51 | 1.61 | 2.18 | 0.029 | 0.399 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 3.37 | 1.62 | 2.08 | 0.038 | 0.461 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 2.57 | 1.61 | 1.60 | 0.110 | 0.804 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 1.78 | 1.61 | 1.11 | 0.268 | 0.955 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 1.64 | 1.61 | 1.02 | 0.310 | 0.955 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.79 | 1.61 | -0.49 | 0.623 | 0.984 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.93 | 1.61 | -0.58 | 0.563 | 0.984 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.14 | 1.61 | -0.09 | 0.930 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.63, *p* = 0.019, η²_G = 0.053
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 1.55 | 23 | = 0.324 | 0.31 [-0.12, 0.75] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 0.23 | 23 | = 0.903 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 1.46 | 23 | = 0.324 | 0.31 [-0.13, 0.73] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 3.14 | 23 | = 0.085 | 0.65 [0.18, 1.10] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 2.72 | 23 | = 0.085 | 0.54 [0.10, 1.01] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 2.89 | 23 | = 0.085 | 0.56 [0.13, 1.05] | medium | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -1.15 | 23 | = 0.422 | -0.27 [-0.66, 0.19] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.90 | 23 | = 0.209 | 0.33 [-0.05, 0.83] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.07 | 23 | = 0.435 | 0.23 [-0.21, 0.64] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.37 | 23 | = 0.324 | 0.25 [-0.15, 0.71] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.99 | 23 | = 0.435 | 0.26 [-0.22, 0.63] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 2.23 | 23 | = 0.188 | 0.60 [0.01, 0.90] | medium | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 1.98 | 23 | = 0.209 | 0.50 [-0.03, 0.84] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.97 | 23 | = 0.209 | 0.52 [-0.04, 0.84] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 1.40 | 23 | = 0.324 | 0.32 [-0.14, 0.72] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 1.39 | 23 | = 0.324 | 0.23 [-0.15, 0.71] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.03 | 23 | = 0.435 | 0.25 [-0.22, 0.64] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.39 | 23 | = 0.838 | -0.09 [-0.50, 0.34] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.37 | 23 | = 0.838 | -0.06 [-0.50, 0.35] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.10 | 23 | = 0.964 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 572.60, BIC = 603.84
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.21, *SE* = 0.325, *z* = 0.647, *p* = 0.518
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.39, *SE* = 0.325, *z* = -1.206, *p* = 0.228
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.55, *SE* = 0.325, *z* = -1.696, *p* = 0.090
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.30, *SE* = 0.325, *z* = -0.921, *p* = 0.357
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.26, *SE* = 0.325, *z* = -0.805, *p* = 0.421
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.28, *SE* = 0.327, *z* = -0.866, *p* = 0.386
- **SNR**: *β* = -0.28, *SE* = 0.058, *z* = -4.864, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -0.21 | 0.33 | -0.65 | 0.518 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.39 | 0.32 | 1.21 | 0.228 | 0.979 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 0.55 | 0.32 | 1.70 | 0.090 | 0.833 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.30 | 0.32 | 0.92 | 0.357 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.26 | 0.33 | 0.80 | 0.421 | 0.998 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 0.28 | 0.33 | 0.87 | 0.386 | 0.998 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.60 | 0.33 | 1.85 | 0.065 | 0.738 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 0.76 | 0.32 | 2.34 | 0.019 | 0.332 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.51 | 0.33 | 1.57 | 0.117 | 0.893 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.47 | 0.32 | 1.45 | 0.146 | 0.920 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 0.49 | 0.33 | 1.52 | 0.129 | 0.904 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.16 | 0.33 | 0.49 | 0.624 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.09 | 0.33 | -0.28 | 0.776 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.13 | 0.33 | -0.40 | 0.690 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.11 | 0.33 | -0.33 | 0.741 | 0.999 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -0.25 | 0.32 | -0.78 | 0.438 | 0.998 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -0.29 | 0.32 | -0.89 | 0.373 | 0.998 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.27 | 0.33 | -0.82 | 0.410 | 0.998 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.04 | 0.32 | -0.12 | 0.908 | 0.999 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.02 | 0.33 | -0.05 | 0.961 | 0.999 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.02 | 0.33 | 0.07 | 0.947 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.24, *p* = 0.289, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -1.06 | 23 | = 0.723 | -0.20 [-0.64, 0.21] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 1.43 | 23 | = 0.575 | 0.28 [-0.14, 0.72] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 1.50 | 23 | = 0.575 | 0.29 [-0.13, 0.74] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.90 | 23 | = 0.723 | 0.18 [-0.24, 0.61] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 0.71 | 23 | = 0.753 | 0.13 [-0.28, 0.57] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 0.29 | 23 | = 0.867 | 0.06 [-0.36, 0.48] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 2.14 | 23 | = 0.468 | 0.47 [-0.00, 0.88] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.12 | 23 | = 0.468 | 0.46 [-0.01, 0.88] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.81 | 23 | = 0.575 | 0.37 [-0.07, 0.81] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 1.55 | 23 | = 0.575 | 0.34 [-0.12, 0.75] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.35 | 23 | = 0.575 | 0.25 [-0.16, 0.70] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 0.17 | 23 | = 0.867 | 0.04 [-0.39, 0.46] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -0.49 | 23 | = 0.823 | -0.11 [-0.52, 0.32] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.68 | 23 | = 0.753 | -0.17 [-0.56, 0.29] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -0.77 | 23 | = 0.753 | -0.20 [-0.58, 0.27] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -0.60 | 23 | = 0.777 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -0.90 | 23 | = 0.723 | -0.19 [-0.61, 0.24] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.93 | 23 | = 0.723 | -0.22 [-0.62, 0.24] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.25 | 23 | = 0.867 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.41 | 23 | = 0.845 | -0.10 [-0.51, 0.34] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.22 | 23 | = 0.867 | -0.06 [-0.47, 0.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1374.91, BIC = 1406.15
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 3.83, *SE* = 3.310, *z* = 1.158, *p* = 0.247
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.50, *SE* = 3.309, *z* = 0.151, *p* = 0.880
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.83, *SE* = 3.308, *z* = 0.856, *p* = 0.392
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -7.67, *SE* = 3.310, *z* = -2.316, *p* = 0.021
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.83, *SE* = 3.308, *z* = -1.159, *p* = 0.247
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -3.50, *SE* = 3.313, *z* = -1.056, *p* = 0.291
- **SNR**: *β* = 0.00, *SE* = 0.273, *z* = 0.002, *p* = 0.998

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -3.83 | 3.31 | -1.16 | 0.247 | 0.942 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -0.50 | 3.31 | -0.15 | 0.880 | 0.987 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -2.83 | 3.31 | -0.86 | 0.392 | 0.942 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 7.67 | 3.31 | 2.32 | 0.021 | 0.312 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 3.83 | 3.31 | 1.16 | 0.247 | 0.942 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 3.50 | 3.31 | 1.06 | 0.291 | 0.942 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 3.33 | 3.31 | 1.01 | 0.314 | 0.942 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.00 | 3.31 | 0.30 | 0.763 | 0.987 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 11.50 | 3.32 | 3.47 | < .001 | 0.011 | * |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 7.67 | 3.31 | 2.32 | 0.021 | 0.312 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 7.33 | 3.32 | 2.21 | 0.027 | 0.357 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -2.33 | 3.31 | -0.71 | 0.481 | 0.942 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 8.17 | 3.31 | 2.46 | 0.014 | 0.231 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 4.33 | 3.31 | 1.31 | 0.190 | 0.936 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 4.00 | 3.32 | 1.21 | 0.228 | 0.942 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 10.50 | 3.31 | 3.17 | 0.002 | 0.030 | * |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 6.67 | 3.31 | 2.02 | 0.044 | 0.490 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 6.33 | 3.31 | 1.91 | 0.056 | 0.553 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -3.83 | 3.31 | -1.16 | 0.247 | 0.942 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -4.17 | 3.31 | -1.26 | 0.208 | 0.939 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.33 | 3.31 | -0.10 | 0.920 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.92, *p* = 0.010, η²_G = 0.042
- Greenhouse-Geisser corrected: *p* = 0.027 (ε = 0.650)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -1.71 | 23 | = 0.291 | -0.20 [-0.78, 0.09] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.25 | 23 | = 0.847 | -0.03 [-0.47, 0.37] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -0.83 | 23 | = 0.508 | -0.15 [-0.59, 0.26] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 2.03 | 23 | = 0.215 | 0.40 [-0.03, 0.85] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 1.14 | 23 | = 0.435 | 0.20 [-0.20, 0.66] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 0.99 | 23 | = 0.435 | 0.17 [-0.22, 0.63] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.42 | 23 | = 0.352 | 0.20 [-0.14, 0.72] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.36 | 23 | = 0.797 | 0.06 [-0.35, 0.50] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 2.87 | 23 | = 0.163 | 0.61 [0.13, 1.04] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 2.29 | 23 | = 0.165 | 0.42 [0.02, 0.91] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.97 | 23 | = 0.215 | 0.37 [-0.04, 0.84] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.79 | 23 | = 0.508 | -0.14 [-0.59, 0.26] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 2.50 | 23 | = 0.163 | 0.47 [0.06, 0.96] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 1.37 | 23 | = 0.352 | 0.26 [-0.15, 0.71] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.12 | 23 | = 0.435 | 0.22 [-0.20, 0.66] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 2.43 | 23 | = 0.163 | 0.57 [0.05, 0.94] | medium | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 1.66 | 23 | = 0.291 | 0.38 [-0.10, 0.77] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.58 | 23 | = 0.296 | 0.33 [-0.11, 0.76] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.08 | 23 | = 0.435 | -0.20 [-0.65, 0.21] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.02 | 23 | = 0.435 | -0.21 [-0.64, 0.22] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.15 | 23 | = 0.880 | -0.02 [-0.45, 0.39] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 613.14, BIC = 644.38
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.35, *SE* = 0.336, *z* = -1.048, *p* = 0.294
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.55, *SE* = 0.335, *z* = -1.629, *p* = 0.103
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.36, *SE* = 0.335, *z* = -4.063, *p* < .001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.16, *SE* = 0.336, *z* = -0.483, *p* = 0.629
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.36, *SE* = 0.335, *z* = -1.079, *p* = 0.280
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.36, *SE* = 0.336, *z* = -4.041, *p* < .001
- **SNR**: *β* = -0.16, *SE* = 0.028, *z* = -5.804, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.35 | 0.34 | 1.05 | 0.294 | 0.948 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | 0.55 | 0.34 | 1.63 | 0.103 | 0.698 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 1.36 | 0.34 | 4.06 | < .001 | 0.001 | ** |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.16 | 0.34 | 0.48 | 0.629 | 0.996 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 0.36 | 0.34 | 1.08 | 0.280 | 0.948 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 1.36 | 0.34 | 4.04 | < .001 | 0.001 | ** |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.19 | 0.34 | 0.58 | 0.561 | 0.996 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 1.01 | 0.34 | 3.01 | 0.003 | 0.043 | * |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -0.19 | 0.34 | -0.56 | 0.572 | 0.996 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 0.01 | 0.34 | 0.03 | 0.976 | 0.999 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 1.01 | 0.34 | 2.99 | 0.003 | 0.044 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 0.82 | 0.34 | 2.43 | 0.015 | 0.178 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.38 | 0.34 | -1.14 | 0.252 | 0.945 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.18 | 0.34 | -0.55 | 0.582 | 0.996 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 0.81 | 0.34 | 2.41 | 0.016 | 0.178 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -1.20 | 0.34 | -3.58 | < .001 | 0.007 | ** |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -1.00 | 0.34 | -2.98 | 0.003 | 0.044 | * |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.01 | 0.34 | -0.02 | 0.987 | 0.999 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.20 | 0.34 | 0.60 | 0.552 | 0.996 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.20 | 0.34 | 3.56 | < .001 | 0.007 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 1.00 | 0.34 | 2.96 | 0.003 | 0.044 | * |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.05, *p* < .001, η²_G = 0.044
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 1.29 | 23 | = 0.316 | 0.19 [-0.17, 0.69] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | 1.75 | 23 | = 0.186 | 0.26 [-0.08, 0.79] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 3.49 | 23 | = 0.021 | 0.57 [0.24, 1.19] | medium | * |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.33 | 23 | = 0.821 | 0.04 [-0.35, 0.49] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 1.41 | 23 | = 0.299 | 0.15 [-0.14, 0.72] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 3.65 | 23 | = 0.021 | 0.52 [0.27, 1.22] | medium | * |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.44 | 23 | = 0.774 | 0.08 [-0.33, 0.51] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 2.21 | 23 | = 0.111 | 0.42 [0.01, 0.89] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.89 | 23 | = 0.534 | -0.15 [-0.61, 0.24] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.14 | 23 | = 0.888 | -0.02 [-0.45, 0.39] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 1.86 | 23 | = 0.175 | 0.36 [-0.06, 0.82] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 2.15 | 23 | = 0.111 | 0.33 [-0.00, 0.88] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -1.33 | 23 | = 0.316 | -0.22 [-0.70, 0.16] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.61 | 23 | = 0.674 | -0.09 [-0.55, 0.30] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 1.73 | 23 | = 0.186 | 0.28 [-0.08, 0.79] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -3.02 | 23 | = 0.032 | -0.54 [-1.08, -0.16] | medium | * |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -2.68 | 23 | = 0.056 | -0.39 [-1.00, -0.09] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | -0.22 | 23 | = 0.872 | -0.04 [-0.47, 0.38] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.71 | 23 | = 0.634 | 0.11 [-0.28, 0.57] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 3.02 | 23 | = 0.032 | 0.49 [0.16, 1.08] | small | * |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.28 | 23 | = 0.111 | 0.35 [0.02, 0.91] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1189.50, BIC = 1220.74
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.04, *SE* = 1.973, *z* = 1.036, *p* = 0.300
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.89, *SE* = 1.975, *z* = 1.462, *p* = 0.144
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.06, *SE* = 1.990, *z* = -0.029, *p* = 0.977
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.57, *SE* = 1.986, *z* = -0.288, *p* = 0.774
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = -1.72, *SE* = 1.994, *z* = -0.861, *p* = 0.389
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = -4.03, *SE* = 2.003, *z* = -2.012, *p* = 0.044
- **SNR**: *β* = 0.10, *SE* = 0.273, *z* = 0.386, *p* = 0.699

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -2.04 | 1.97 | -1.04 | 0.300 | 0.953 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -2.89 | 1.98 | -1.46 | 0.144 | 0.851 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | 0.06 | 1.99 | 0.03 | 0.977 | 0.988 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | 0.57 | 1.99 | 0.29 | 0.774 | 0.988 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | 1.72 | 1.99 | 0.86 | 0.389 | 0.968 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | 4.03 | 2.00 | 2.01 | 0.044 | 0.555 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.84 | 1.97 | -0.43 | 0.669 | 0.988 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 2.10 | 1.98 | 1.06 | 0.288 | 0.953 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 2.62 | 1.97 | 1.32 | 0.185 | 0.895 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | 3.76 | 1.98 | 1.90 | 0.058 | 0.612 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 6.07 | 1.99 | 3.06 | 0.002 | 0.044 | * |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | 2.94 | 1.98 | 1.49 | 0.136 | 0.851 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 3.46 | 1.97 | 1.75 | 0.080 | 0.712 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | 4.60 | 1.98 | 2.33 | 0.020 | 0.318 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 6.92 | 1.98 | 3.49 | < .001 | 0.010 | * |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.51 | 1.97 | 0.26 | 0.794 | 0.988 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 1.66 | 1.97 | 0.84 | 0.400 | 0.968 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 3.97 | 1.97 | 2.01 | 0.044 | 0.555 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.14 | 1.97 | 0.58 | 0.561 | 0.984 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 3.46 | 1.97 | 1.75 | 0.080 | 0.712 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 2.31 | 1.97 | 1.17 | 0.241 | 0.936 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.69, *p* = 0.017, η²_G = 0.050
- Greenhouse-Geisser corrected: *p* = 0.035 (ε = 0.681)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -1.30 | 23 | = 0.328 | -0.20 [-0.69, 0.16] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -1.27 | 23 | = 0.328 | -0.29 [-0.69, 0.17] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | 0.07 | 23 | = 0.946 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | 0.35 | 23 | = 0.807 | 0.07 [-0.35, 0.49] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | 1.41 | 23 | = 0.328 | 0.18 [-0.14, 0.72] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | 2.87 | 23 | = 0.061 | 0.44 [0.13, 1.04] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -0.46 | 23 | = 0.759 | -0.09 [-0.52, 0.33] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.91 | 23 | = 0.518 | 0.22 [-0.24, 0.61] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 1.40 | 23 | = 0.328 | 0.29 [-0.15, 0.72] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 2.05 | 23 | = 0.183 | 0.39 [-0.02, 0.86] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 3.36 | 23 | = 0.039 | 0.70 [0.22, 1.16] | medium | * |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | 1.49 | 23 | = 0.328 | 0.31 [-0.13, 0.74] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 1.40 | 23 | = 0.328 | 0.39 [-0.15, 0.72] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | 2.41 | 23 | = 0.102 | 0.49 [0.04, 0.94] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 3.23 | 23 | = 0.039 | 0.81 [0.19, 1.12] | large | * |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 0.21 | 23 | = 0.873 | 0.05 [-0.38, 0.47] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.74 | 23 | = 0.614 | 0.16 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 1.62 | 23 | = 0.328 | 0.42 [-0.10, 0.76] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.56 | 23 | = 0.716 | 0.12 [-0.31, 0.54] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.41 | 23 | = 0.102 | 0.39 [0.05, 0.94] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.34 | 23 | = 0.328 | 0.25 [-0.16, 0.70] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 613.58, BIC = 644.82
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = -0.39, *SE* = 0.349, *z* = -1.105, *p* = 0.269
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.32, *SE* = 0.350, *z* = 0.907, *p* = 0.365
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.68, *SE* = 0.352, *z* = 1.915, *p* = 0.055
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.65, *SE* = 0.352, *z* = 1.846, *p* = 0.065
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.48, *SE* = 0.353, *z* = 1.351, *p* = 0.177
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 0.52, *SE* = 0.355, *z* = 1.458, *p* = 0.145
- **SNR**: *β* = 0.17, *SE* = 0.049, *z* = 3.454, *p* = 0.001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | 0.39 | 0.35 | 1.10 | 0.269 | 0.977 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -0.32 | 0.35 | -0.91 | 0.365 | 0.985 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -0.68 | 0.35 | -1.92 | 0.055 | 0.599 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -0.65 | 0.35 | -1.85 | 0.065 | 0.634 | n.s. |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -0.48 | 0.35 | -1.35 | 0.177 | 0.920 | n.s. |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -0.52 | 0.35 | -1.46 | 0.145 | 0.888 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | -0.70 | 0.35 | -2.02 | 0.044 | 0.534 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -1.06 | 0.35 | -3.03 | 0.002 | 0.050 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -1.04 | 0.35 | -2.96 | 0.003 | 0.060 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -0.86 | 0.35 | -2.46 | 0.014 | 0.221 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.90 | 0.35 | -2.57 | 0.010 | 0.177 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.36 | 0.35 | -1.02 | 0.306 | 0.982 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -0.33 | 0.35 | -0.95 | 0.342 | 0.985 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.16 | 0.35 | -0.46 | 0.648 | 0.999 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.20 | 0.35 | -0.57 | 0.568 | 0.999 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.03 | 0.35 | 0.07 | 0.941 | 0.999 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.20 | 0.35 | 0.57 | 0.570 | 0.999 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 0.16 | 0.35 | 0.45 | 0.651 | 0.999 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.17 | 0.35 | 0.49 | 0.622 | 0.999 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.13 | 0.35 | 0.38 | 0.706 | 0.999 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.04 | 0.35 | -0.12 | 0.908 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.65, *p* = 0.139, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | 1.30 | 23 | = 0.545 | 0.24 [-0.17, 0.69] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -0.89 | 23 | = 0.732 | -0.12 [-0.61, 0.24] | negligible | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -1.63 | 23 | = 0.405 | -0.28 [-0.77, 0.10] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -1.45 | 23 | = 0.483 | -0.27 [-0.73, 0.14] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -0.91 | 23 | = 0.732 | -0.17 [-0.61, 0.24] | negligible | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.61 | 23 | = 0.782 | -0.14 [-0.55, 0.30] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | -2.17 | 23 | = 0.215 | -0.36 [-0.88, 0.00] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -2.78 | 23 | = 0.132 | -0.53 [-1.02, -0.11] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -2.53 | 23 | = 0.132 | -0.50 [-0.97, -0.07] | medium | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -2.61 | 23 | = 0.132 | -0.42 [-0.98, -0.08] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -1.81 | 23 | = 0.353 | -0.35 [-0.80, 0.07] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.91 | 23 | = 0.732 | -0.15 [-0.61, 0.24] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -0.66 | 23 | = 0.782 | -0.14 [-0.56, 0.29] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.16 | 23 | = 0.992 | -0.03 [-0.45, 0.39] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -0.12 | 23 | = 0.992 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 0.01 | 23 | = 0.992 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.77 | 23 | = 0.782 | 0.13 [-0.27, 0.58] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.52 | 23 | = 0.782 | 0.10 [-0.32, 0.53] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.54 | 23 | = 0.782 | 0.12 [-0.31, 0.53] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 0.48 | 23 | = 0.782 | 0.09 [-0.32, 0.52] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.02 | 23 | = 0.992 | -0.00 [-0.43, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1641.68, BIC = 1672.92
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 21.01, *SE* = 7.946, *z* = 2.644, *p* = 0.008
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 13.23, *SE* = 7.859, *z* = 1.684, *p* = 0.092
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 13.89, *SE* = 7.901, *z* = 1.758, *p* = 0.079
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 23.93, *SE* = 7.865, *z* = 3.042, *p* = 0.002
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 28.19, *SE* = 7.890, *z* = 3.573, *p* < .001
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 7.28, *SE* = 7.837, *z* = 0.930, *p* = 0.353
- **SNR**: *β* = -0.23, *SE* = 0.588, *z* = -0.383, *p* = 0.702

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -21.01 | 7.95 | -2.64 | 0.008 | 0.145 | n.s. |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -13.23 | 7.86 | -1.68 | 0.092 | 0.687 | n.s. |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -13.89 | 7.90 | -1.76 | 0.079 | 0.683 | n.s. |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -23.93 | 7.87 | -3.04 | 0.002 | 0.046 | * |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -28.19 | 7.89 | -3.57 | < .001 | 0.007 | ** |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -7.28 | 7.84 | -0.93 | 0.353 | 0.970 | n.s. |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 7.77 | 7.87 | 0.99 | 0.323 | 0.970 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | 7.12 | 7.84 | 0.91 | 0.364 | 0.970 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | -2.92 | 7.86 | -0.37 | 0.710 | 0.970 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -7.18 | 7.85 | -0.92 | 0.360 | 0.970 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | 13.72 | 7.97 | 1.72 | 0.085 | 0.685 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.66 | 7.85 | -0.08 | 0.933 | 0.970 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | -10.69 | 7.84 | -1.36 | 0.172 | 0.875 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -14.95 | 7.84 | -1.91 | 0.057 | 0.606 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | 5.95 | 7.87 | 0.76 | 0.450 | 0.970 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | -10.04 | 7.84 | -1.28 | 0.201 | 0.893 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | -14.30 | 7.84 | -1.82 | 0.068 | 0.653 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | 6.61 | 7.92 | 0.83 | 0.404 | 0.970 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -4.26 | 7.84 | -0.54 | 0.587 | 0.970 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 16.64 | 7.88 | 2.11 | 0.035 | 0.451 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 20.90 | 7.91 | 2.64 | 0.008 | 0.145 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.92, *p* = 0.010, η²_G = 0.068
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -3.19 | 23 | = 0.058 | -0.75 [-1.12, -0.19] | medium | n.s. |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -1.71 | 23 | = 0.236 | -0.43 [-0.78, 0.09] | small | n.s. |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -1.93 | 23 | = 0.174 | -0.44 [-0.83, 0.04] | small | n.s. |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -2.89 | 23 | = 0.058 | -0.72 [-1.05, -0.13] | medium | n.s. |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -2.95 | 23 | = 0.058 | -0.91 [-1.06, -0.14] | large | n.s. |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -0.89 | 23 | = 0.505 | -0.22 [-0.61, 0.24] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 1.35 | 23 | = 0.361 | 0.24 [-0.15, 0.71] | small | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | 0.93 | 23 | = 0.505 | 0.22 [-0.24, 0.62] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | -0.42 | 23 | = 0.716 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | -0.90 | 23 | = 0.505 | -0.23 [-0.61, 0.24] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | 2.02 | 23 | = 0.174 | 0.38 [-0.03, 0.85] | small | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -0.06 | 23 | = 0.955 | -0.01 [-0.43, 0.41] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | -1.27 | 23 | = 0.382 | -0.29 [-0.69, 0.17] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -1.54 | 23 | = 0.287 | -0.43 [-0.75, 0.12] | small | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | 0.70 | 23 | = 0.575 | 0.15 [-0.28, 0.57] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | -1.09 | 23 | = 0.460 | -0.28 [-0.65, 0.20] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | -1.93 | 23 | = 0.174 | -0.42 [-0.83, 0.04] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.81 | 23 | = 0.525 | 0.17 [-0.26, 0.59] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.53 | 23 | = 0.668 | -0.11 [-0.53, 0.32] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.96 | 23 | = 0.174 | 0.42 [-0.04, 0.84] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.29 | 23 | = 0.165 | 0.55 [0.02, 0.91] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 701.58, BIC = 732.82
- **Decrease by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.40, *SE* = 0.429, *z* = 5.612, *p* < .001
- **Decrease by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.35, *SE* = 0.423, *z* = 5.551, *p* < .001
- **Decrease by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.73, *SE* = 0.426, *z* = 6.416, *p* < .001
- **Increase by 1 (no 1) vs Cardinality (no change, no 1)**: *β* = 1.79, *SE* = 0.424, *z* = 4.236, *p* < .001
- **Increase by 2 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.48, *SE* = 0.425, *z* = 5.823, *p* < .001
- **Increase by 3 (no 1) vs Cardinality (no change, no 1)**: *β* = 2.87, *SE* = 0.422, *z* = 6.798, *p* < .001
- **SNR**: *β* = 0.15, *SE* = 0.034, *z* = 4.542, *p* < .001

_Reference condition: **Cardinality (no change, no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality (no change, no 1) - Decrease by 1 (no 1) | -2.41 | 0.43 | -5.61 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Decrease by 2 (no 1) | -2.35 | 0.42 | -5.55 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Decrease by 3 (no 1) | -2.73 | 0.43 | -6.42 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 1 (no 1) | -1.79 | 0.42 | -4.24 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 2 (no 1) | -2.48 | 0.43 | -5.82 | < .001 | < .001 | *** |
| Cardinality (no change, no 1) - Increase by 3 (no 1) | -2.87 | 0.42 | -6.80 | < .001 | < .001 | *** |
| Decrease by 1 (no 1) - Decrease by 2 (no 1) | 0.06 | 0.42 | 0.13 | 0.896 | 0.996 | n.s. |
| Decrease by 1 (no 1) - Decrease by 3 (no 1) | -0.33 | 0.42 | -0.77 | 0.438 | 0.971 | n.s. |
| Decrease by 1 (no 1) - Increase by 1 (no 1) | 0.61 | 0.42 | 1.44 | 0.149 | 0.856 | n.s. |
| Decrease by 1 (no 1) - Increase by 2 (no 1) | -0.07 | 0.42 | -0.17 | 0.867 | 0.996 | n.s. |
| Decrease by 1 (no 1) - Increase by 3 (no 1) | -0.46 | 0.43 | -1.08 | 0.281 | 0.949 | n.s. |
| Decrease by 2 (no 1) - Decrease by 3 (no 1) | -0.38 | 0.42 | -0.91 | 0.365 | 0.971 | n.s. |
| Decrease by 2 (no 1) - Increase by 1 (no 1) | 0.56 | 0.42 | 1.32 | 0.188 | 0.899 | n.s. |
| Decrease by 2 (no 1) - Increase by 2 (no 1) | -0.13 | 0.42 | -0.30 | 0.766 | 0.996 | n.s. |
| Decrease by 2 (no 1) - Increase by 3 (no 1) | -0.52 | 0.42 | -1.22 | 0.221 | 0.918 | n.s. |
| Decrease by 3 (no 1) - Increase by 1 (no 1) | 0.94 | 0.42 | 2.22 | 0.026 | 0.312 | n.s. |
| Decrease by 3 (no 1) - Increase by 2 (no 1) | 0.26 | 0.42 | 0.61 | 0.543 | 0.980 | n.s. |
| Decrease by 3 (no 1) - Increase by 3 (no 1) | -0.14 | 0.43 | -0.32 | 0.750 | 0.996 | n.s. |
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.68 | 0.42 | -1.61 | 0.107 | 0.769 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -1.07 | 0.42 | -2.53 | 0.011 | 0.158 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.39 | 0.43 | -0.92 | 0.357 | 0.971 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 21 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 10.45, *p* < .001, η²_G = 0.082
- Greenhouse-Geisser corrected: *p* < .001 (ε = 0.633)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality (no change, no 1) vs Decrease by 1 (no 1) | -5.10 | 23 | < .001 | -0.89 [-1.56, -0.52] | large | *** |
| Cardinality (no change, no 1) vs Decrease by 2 (no 1) | -5.36 | 23 | < .001 | -0.86 [-1.63, -0.56] | large | *** |
| Cardinality (no change, no 1) vs Decrease by 3 (no 1) | -4.48 | 23 | < .001 | -0.91 [-1.42, -0.41] | large | *** |
| Cardinality (no change, no 1) vs Increase by 1 (no 1) | -3.27 | 23 | = 0.012 | -0.59 [-1.13, -0.20] | medium | * |
| Cardinality (no change, no 1) vs Increase by 2 (no 1) | -5.43 | 23 | < .001 | -0.84 [-1.65, -0.57] | large | *** |
| Cardinality (no change, no 1) vs Increase by 3 (no 1) | -5.00 | 23 | < .001 | -1.07 [-1.54, -0.50] | large | *** |
| Decrease by 1 (no 1) vs Decrease by 2 (no 1) | 0.71 | 23 | = 0.725 | 0.07 [-0.28, 0.57] | negligible | n.s. |
| Decrease by 1 (no 1) vs Decrease by 3 (no 1) | -0.58 | 23 | = 0.746 | -0.07 [-0.54, 0.31] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 1 (no 1) | 2.47 | 23 | = 0.064 | 0.22 [0.06, 0.95] | small | n.s. |
| Decrease by 1 (no 1) vs Increase by 2 (no 1) | 0.09 | 23 | = 0.930 | 0.01 [-0.40, 0.44] | negligible | n.s. |
| Decrease by 1 (no 1) vs Increase by 3 (no 1) | -0.22 | 23 | = 0.866 | -0.03 [-0.47, 0.38] | negligible | n.s. |
| Decrease by 2 (no 1) vs Decrease by 3 (no 1) | -1.23 | 23 | = 0.403 | -0.14 [-0.68, 0.18] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 1 (no 1) | 1.69 | 23 | = 0.200 | 0.16 [-0.09, 0.78] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 2 (no 1) | -0.58 | 23 | = 0.746 | -0.06 [-0.54, 0.31] | negligible | n.s. |
| Decrease by 2 (no 1) vs Increase by 3 (no 1) | -0.99 | 23 | = 0.534 | -0.12 [-0.63, 0.22] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 1 (no 1) | 2.01 | 23 | = 0.132 | 0.27 [-0.03, 0.85] | small | n.s. |
| Decrease by 3 (no 1) vs Increase by 2 (no 1) | 0.52 | 23 | = 0.749 | 0.08 [-0.32, 0.53] | negligible | n.s. |
| Decrease by 3 (no 1) vs Increase by 3 (no 1) | 0.35 | 23 | = 0.852 | 0.05 [-0.35, 0.49] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -2.36 | 23 | = 0.071 | -0.20 [-0.93, -0.04] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.85 | 23 | = 0.163 | -0.27 [-0.81, 0.06] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.24 | 23 | = 0.866 | -0.04 [-0.47, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Significant main effect of condition (*p* = 0.019) (no significant pairwise comparisons)
**N1 latency:** Significant main effect of condition (*p* = 0.010) (no significant pairwise comparisons)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed greater amplitude than Decrease by 3 (no 1) (*d* = 0.57)
  - Cardinality (no change, no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.52)
  - Decrease by 3 (no 1) showed smaller amplitude than Increase by 1 (no 1) (*d* = -0.54)
  - Increase by 1 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.49)
**P1 latency:** Significant main effect of condition (*p* = 0.017). Post-hoc tests revealed:
  - Decrease by 1 (no 1) showed greater latency than Increase by 3 (no 1) (*d* = 0.70)
  - Decrease by 2 (no 1) showed greater latency than Increase by 3 (no 1) (*d* = 0.81)
**P3b latency:** Significant main effect of condition (*p* = 0.010) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 1 (no 1) (*d* = -0.89)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 2 (no 1) (*d* = -0.86)
  - Cardinality (no change, no 1) showed smaller amplitude than Decrease by 3 (no 1) (*d* = -0.91)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 1 (no 1) (*d* = -0.59)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 2 (no 1) (*d* = -0.84)
  - Cardinality (no change, no 1) showed smaller amplitude than Increase by 3 (no 1) (*d* = -1.07)

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
