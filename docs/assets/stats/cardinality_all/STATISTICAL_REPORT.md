# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:15:40

---

## 1. Analysis Overview

**Total Measurements:** 576
**Number of Subjects:** 24
**Number of Conditions:** 6

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
| Cardinality1 | 24 | 107.83 ms | 11.28 | 2.30 | [92.00, 120.00] |
| Cardinality2 | 24 | 108.83 ms | 10.28 | 2.10 | [92.00, 120.00] |
| Cardinality3 | 24 | 107.33 ms | 11.72 | 2.39 | [92.00, 120.00] |
| Cardinality4 | 24 | 109.00 ms | 9.45 | 1.93 | [92.00, 120.00] |
| Cardinality5 | 24 | 102.50 ms | 9.71 | 1.98 | [92.00, 120.00] |
| Cardinality6 | 24 | 104.50 ms | 10.03 | 2.05 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | -1.87 µV | 2.48 | 0.51 | [-7.82, 3.80] |
| Cardinality2 | 24 | -1.13 µV | 2.11 | 0.43 | [-5.94, 3.96] |
| Cardinality3 | 24 | -1.49 µV | 2.63 | 0.54 | [-8.81, 2.43] |
| Cardinality4 | 24 | -1.71 µV | 1.81 | 0.37 | [-6.84, 1.09] |
| Cardinality5 | 24 | -2.05 µV | 2.20 | 0.45 | [-7.37, 0.84] |
| Cardinality6 | 24 | -2.19 µV | 2.35 | 0.48 | [-7.15, 1.49] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 178.17 ms | 18.35 | 3.75 | [144.00, 204.00] |
| Cardinality2 | 24 | 174.33 ms | 19.87 | 4.06 | [144.00, 204.00] |
| Cardinality3 | 24 | 171.17 ms | 18.27 | 3.73 | [144.00, 204.00] |
| Cardinality4 | 24 | 172.00 ms | 19.77 | 4.04 | [144.00, 204.00] |
| Cardinality5 | 24 | 171.67 ms | 16.04 | 3.27 | [144.00, 196.00] |
| Cardinality6 | 24 | 175.50 ms | 16.82 | 3.43 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | -3.26 µV | 2.63 | 0.54 | [-9.64, 0.56] |
| Cardinality2 | 24 | -5.25 µV | 2.68 | 0.55 | [-10.50, -0.87] |
| Cardinality3 | 24 | -5.11 µV | 1.96 | 0.40 | [-10.83, -1.55] |
| Cardinality4 | 24 | -5.52 µV | 3.34 | 0.68 | [-13.09, 0.33] |
| Cardinality5 | 24 | -5.96 µV | 2.55 | 0.52 | [-12.06, -1.67] |
| Cardinality6 | 24 | -5.39 µV | 3.28 | 0.67 | [-11.14, 2.47] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 113.00 ms | 9.31 | 1.90 | [96.00, 120.00] |
| Cardinality2 | 24 | 107.67 ms | 10.48 | 2.14 | [96.00, 120.00] |
| Cardinality3 | 24 | 109.33 ms | 9.85 | 2.01 | [96.00, 120.00] |
| Cardinality4 | 24 | 110.33 ms | 10.28 | 2.10 | [96.00, 120.00] |
| Cardinality5 | 24 | 103.50 ms | 8.28 | 1.69 | [96.00, 120.00] |
| Cardinality6 | 24 | 106.33 ms | 9.28 | 1.89 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 3.48 µV | 3.16 | 0.64 | [-0.77, 13.26] |
| Cardinality2 | 24 | 1.13 µV | 2.84 | 0.58 | [-6.89, 7.57] |
| Cardinality3 | 24 | 1.57 µV | 2.93 | 0.60 | [-3.51, 8.96] |
| Cardinality4 | 24 | 1.67 µV | 2.31 | 0.47 | [-3.85, 6.93] |
| Cardinality5 | 24 | 1.57 µV | 1.92 | 0.39 | [-0.85, 5.37] |
| Cardinality6 | 24 | 1.36 µV | 2.40 | 0.49 | [-2.94, 8.25] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 462.00 ms | 15.11 | 3.08 | [440.00, 480.00] |
| Cardinality2 | 24 | 459.67 ms | 16.80 | 3.43 | [440.00, 480.00] |
| Cardinality3 | 24 | 456.50 ms | 13.46 | 2.75 | [440.00, 480.00] |
| Cardinality4 | 24 | 459.83 ms | 14.28 | 2.91 | [440.00, 480.00] |
| Cardinality5 | 24 | 460.67 ms | 17.24 | 3.52 | [440.00, 480.00] |
| Cardinality6 | 24 | 459.67 ms | 16.17 | 3.30 | [440.00, 480.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 24 | 1.20 µV | 2.97 | 0.61 | [-4.98, 7.06] |
| Cardinality2 | 24 | 1.69 µV | 3.19 | 0.65 | [-5.35, 8.49] |
| Cardinality3 | 24 | 2.63 µV | 3.52 | 0.72 | [-6.78, 9.60] |
| Cardinality4 | 24 | 1.17 µV | 4.09 | 0.83 | [-10.16, 8.96] |
| Cardinality5 | 24 | 0.92 µV | 2.83 | 0.58 | [-6.19, 5.39] |
| Cardinality6 | 24 | 1.97 µV | 3.75 | 0.76 | [-4.76, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1082.78, BIC = 1109.50
- **Cardinality2 vs Cardinality1**: *β* = 0.64, *SE* = 2.592, *z* = 0.249, *p* = 0.804
- **Cardinality3 vs Cardinality1**: *β* = -0.64, *SE* = 2.577, *z* = -0.248, *p* = 0.804
- **Cardinality4 vs Cardinality1**: *β* = 1.03, *SE* = 2.576, *z* = 0.401, *p* = 0.689
- **Cardinality5 vs Cardinality1**: *β* = -5.21, *SE* = 2.576, *z* = -2.024, *p* = 0.043
- **Cardinality6 vs Cardinality1**: *β* = -3.04, *SE* = 2.586, *z* = -1.176, *p* = 0.240
- **SNR**: *β* = -0.56, *SE* = 0.488, *z* = -1.152, *p* = 0.249

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | -0.64 | 2.59 | -0.25 | 0.804 | 0.992 | n.s. |
| Cardinality1 - Cardinality3 | 0.64 | 2.58 | 0.25 | 0.804 | 0.992 | n.s. |
| Cardinality1 - Cardinality4 | -1.03 | 2.58 | -0.40 | 0.689 | 0.992 | n.s. |
| Cardinality1 - Cardinality5 | 5.21 | 2.58 | 2.02 | 0.043 | 0.435 | n.s. |
| Cardinality1 - Cardinality6 | 3.04 | 2.59 | 1.18 | 0.240 | 0.915 | n.s. |
| Cardinality2 - Cardinality3 | 1.28 | 2.58 | 0.50 | 0.619 | 0.992 | n.s. |
| Cardinality2 - Cardinality4 | -0.39 | 2.58 | -0.15 | 0.881 | 0.992 | n.s. |
| Cardinality2 - Cardinality5 | 5.86 | 2.61 | 2.25 | 0.025 | 0.295 | n.s. |
| Cardinality2 - Cardinality6 | 3.68 | 2.63 | 1.40 | 0.162 | 0.829 | n.s. |
| Cardinality3 - Cardinality4 | -1.67 | 2.57 | -0.65 | 0.516 | 0.987 | n.s. |
| Cardinality3 - Cardinality5 | 4.58 | 2.58 | 1.77 | 0.077 | 0.615 | n.s. |
| Cardinality3 - Cardinality6 | 2.40 | 2.60 | 0.92 | 0.356 | 0.970 | n.s. |
| Cardinality4 - Cardinality5 | 6.25 | 2.58 | 2.42 | 0.016 | 0.210 | n.s. |
| Cardinality4 - Cardinality6 | 4.07 | 2.60 | 1.57 | 0.117 | 0.747 | n.s. |
| Cardinality5 - Cardinality6 | -2.17 | 2.58 | -0.84 | 0.399 | 0.972 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.92, *p* = 0.096, η²_G = 0.051
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | -0.30 | 23 | = 0.882 | -0.09 [-0.48, 0.36] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 0.23 | 23 | = 0.882 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| Cardinality1 vs Cardinality4 | -0.45 | 23 | = 0.824 | -0.11 [-0.51, 0.33] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | 2.56 | 23 | = 0.130 | 0.51 [0.07, 0.97] | medium | n.s. |
| Cardinality1 vs Cardinality6 | 1.23 | 23 | = 0.499 | 0.31 [-0.18, 0.68] | small | n.s. |
| Cardinality2 vs Cardinality3 | 0.49 | 23 | = 0.824 | 0.14 [-0.32, 0.52] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -0.07 | 23 | = 0.946 | -0.02 [-0.44, 0.41] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 2.09 | 23 | = 0.195 | 0.63 [-0.01, 0.87] | medium | n.s. |
| Cardinality2 vs Cardinality6 | 1.83 | 23 | = 0.242 | 0.43 [-0.06, 0.81] | small | n.s. |
| Cardinality3 vs Cardinality4 | -0.57 | 23 | = 0.824 | -0.16 [-0.54, 0.31] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | 2.05 | 23 | = 0.195 | 0.45 [-0.02, 0.86] | small | n.s. |
| Cardinality3 vs Cardinality6 | 1.03 | 23 | = 0.591 | 0.26 [-0.22, 0.64] | small | n.s. |
| Cardinality4 vs Cardinality5 | 2.69 | 23 | = 0.130 | 0.68 [0.10, 1.00] | medium | n.s. |
| Cardinality4 vs Cardinality6 | 1.67 | 23 | = 0.271 | 0.46 [-0.09, 0.78] | small | n.s. |
| Cardinality5 vs Cardinality6 | -0.76 | 23 | = 0.760 | -0.20 [-0.58, 0.27] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 623.22, BIC = 649.95
- **Cardinality2 vs Cardinality1**: *β* = 0.46, *SE* = 0.529, *z* = 0.864, *p* = 0.387
- **Cardinality3 vs Cardinality1**: *β* = 0.28, *SE* = 0.526, *z* = 0.526, *p* = 0.599
- **Cardinality4 vs Cardinality1**: *β* = 0.06, *SE* = 0.526, *z* = 0.107, *p* = 0.915
- **Cardinality5 vs Cardinality1**: *β* = -0.08, *SE* = 0.526, *z* = -0.159, *p* = 0.874
- **Cardinality6 vs Cardinality1**: *β* = -0.10, *SE* = 0.528, *z* = -0.182, *p* = 0.856
- **SNR**: *β* = -0.44, *SE* = 0.098, *z* = -4.474, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | -0.46 | 0.53 | -0.86 | 0.387 | 0.998 | n.s. |
| Cardinality1 - Cardinality3 | -0.28 | 0.53 | -0.53 | 0.599 | 1.000 | n.s. |
| Cardinality1 - Cardinality4 | -0.06 | 0.53 | -0.11 | 0.915 | 1.000 | n.s. |
| Cardinality1 - Cardinality5 | 0.08 | 0.53 | 0.16 | 0.874 | 1.000 | n.s. |
| Cardinality1 - Cardinality6 | 0.10 | 0.53 | 0.18 | 0.856 | 1.000 | n.s. |
| Cardinality2 - Cardinality3 | 0.18 | 0.53 | 0.34 | 0.732 | 1.000 | n.s. |
| Cardinality2 - Cardinality4 | 0.40 | 0.53 | 0.76 | 0.446 | 0.999 | n.s. |
| Cardinality2 - Cardinality5 | 0.54 | 0.53 | 1.02 | 0.309 | 0.996 | n.s. |
| Cardinality2 - Cardinality6 | 0.55 | 0.54 | 1.03 | 0.303 | 0.996 | n.s. |
| Cardinality3 - Cardinality4 | 0.22 | 0.53 | 0.42 | 0.674 | 1.000 | n.s. |
| Cardinality3 - Cardinality5 | 0.36 | 0.53 | 0.68 | 0.494 | 0.999 | n.s. |
| Cardinality3 - Cardinality6 | 0.37 | 0.53 | 0.70 | 0.482 | 0.999 | n.s. |
| Cardinality4 - Cardinality5 | 0.14 | 0.53 | 0.26 | 0.791 | 1.000 | n.s. |
| Cardinality4 - Cardinality6 | 0.15 | 0.53 | 0.29 | 0.775 | 1.000 | n.s. |
| Cardinality5 - Cardinality6 | 0.01 | 0.53 | 0.02 | 0.981 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.93, *p* = 0.465, η²_G = 0.024
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | -1.40 | 23 | = 0.661 | -0.32 [-0.72, 0.14] | small | n.s. |
| Cardinality1 vs Cardinality3 | -0.53 | 23 | = 0.781 | -0.15 [-0.53, 0.31] | negligible | n.s. |
| Cardinality1 vs Cardinality4 | -0.28 | 23 | = 0.781 | -0.07 [-0.48, 0.37] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | 0.29 | 23 | = 0.781 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| Cardinality1 vs Cardinality6 | 0.52 | 23 | = 0.781 | 0.13 [-0.32, 0.53] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.67 | 23 | = 0.781 | 0.15 [-0.29, 0.56] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | 1.38 | 23 | = 0.661 | 0.29 [-0.15, 0.71] | small | n.s. |
| Cardinality2 vs Cardinality5 | 1.64 | 23 | = 0.661 | 0.42 [-0.10, 0.77] | small | n.s. |
| Cardinality2 vs Cardinality6 | 1.90 | 23 | = 0.661 | 0.48 [-0.05, 0.82] | small | n.s. |
| Cardinality3 vs Cardinality4 | 0.36 | 23 | = 0.781 | 0.10 [-0.35, 0.50] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | 1.05 | 23 | = 0.765 | 0.23 [-0.21, 0.64] | small | n.s. |
| Cardinality3 vs Cardinality6 | 1.26 | 23 | = 0.661 | 0.28 [-0.17, 0.69] | small | n.s. |
| Cardinality4 vs Cardinality5 | 0.65 | 23 | = 0.781 | 0.17 [-0.29, 0.56] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | 0.80 | 23 | = 0.781 | 0.23 [-0.26, 0.59] | small | n.s. |
| Cardinality5 vs Cardinality6 | 0.29 | 23 | = 0.781 | 0.06 [-0.36, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1190.92, BIC = 1217.65
- **Cardinality2 vs Cardinality1**: *β* = -3.88, *SE* = 3.431, *z* = -1.129, *p* = 0.259
- **Cardinality3 vs Cardinality1**: *β* = -7.08, *SE* = 3.441, *z* = -2.058, *p* = 0.040
- **Cardinality4 vs Cardinality1**: *β* = -6.37, *SE* = 3.511, *z* = -1.815, *p* = 0.070
- **Cardinality5 vs Cardinality1**: *β* = -6.71, *SE* = 3.517, *z* = -1.908, *p* = 0.056
- **Cardinality6 vs Cardinality1**: *β* = -2.79, *SE* = 3.460, *z* = -0.808, *p* = 0.419
- **SNR**: *β* = 0.12, *SE* = 0.449, *z* = 0.268, *p* = 0.789

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 3.87 | 3.43 | 1.13 | 0.259 | 0.961 | n.s. |
| Cardinality1 - Cardinality3 | 7.08 | 3.44 | 2.06 | 0.040 | 0.454 | n.s. |
| Cardinality1 - Cardinality4 | 6.37 | 3.51 | 1.81 | 0.070 | 0.608 | n.s. |
| Cardinality1 - Cardinality5 | 6.71 | 3.52 | 1.91 | 0.056 | 0.556 | n.s. |
| Cardinality1 - Cardinality6 | 2.79 | 3.46 | 0.81 | 0.419 | 0.977 | n.s. |
| Cardinality2 - Cardinality3 | 3.21 | 3.43 | 0.93 | 0.350 | 0.968 | n.s. |
| Cardinality2 - Cardinality4 | 2.50 | 3.48 | 0.72 | 0.473 | 0.977 | n.s. |
| Cardinality2 - Cardinality5 | 2.84 | 3.49 | 0.81 | 0.416 | 0.977 | n.s. |
| Cardinality2 - Cardinality6 | -1.08 | 3.44 | -0.31 | 0.754 | 0.996 | n.s. |
| Cardinality3 - Cardinality4 | -0.71 | 3.46 | -0.21 | 0.837 | 0.996 | n.s. |
| Cardinality3 - Cardinality5 | -0.37 | 3.46 | -0.11 | 0.915 | 0.996 | n.s. |
| Cardinality3 - Cardinality6 | -4.29 | 3.43 | -1.25 | 0.212 | 0.942 | n.s. |
| Cardinality4 - Cardinality5 | 0.34 | 3.43 | 0.10 | 0.921 | 0.996 | n.s. |
| Cardinality4 - Cardinality6 | -3.58 | 3.44 | -1.04 | 0.298 | 0.961 | n.s. |
| Cardinality5 - Cardinality6 | -3.92 | 3.44 | -1.14 | 0.255 | 0.961 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.20, *p* = 0.312, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.83 | 23 | = 0.752 | 0.20 [-0.26, 0.60] | small | n.s. |
| Cardinality1 vs Cardinality3 | 2.77 | 23 | = 0.164 | 0.38 [0.11, 1.02] | small | n.s. |
| Cardinality1 vs Cardinality4 | 1.78 | 23 | = 0.441 | 0.32 [-0.07, 0.80] | small | n.s. |
| Cardinality1 vs Cardinality5 | 2.41 | 23 | = 0.184 | 0.38 [0.04, 0.94] | small | n.s. |
| Cardinality1 vs Cardinality6 | 0.73 | 23 | = 0.752 | 0.15 [-0.28, 0.57] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.85 | 23 | = 0.752 | 0.17 [-0.25, 0.60] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | 0.57 | 23 | = 0.784 | 0.12 [-0.31, 0.54] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 0.68 | 23 | = 0.752 | 0.15 [-0.28, 0.56] | negligible | n.s. |
| Cardinality2 vs Cardinality6 | -0.30 | 23 | = 0.920 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.25 | 23 | = 0.920 | -0.04 [-0.47, 0.37] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | -0.18 | 23 | = 0.920 | -0.03 [-0.46, 0.39] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -1.35 | 23 | = 0.571 | -0.25 [-0.71, 0.15] | small | n.s. |
| Cardinality4 vs Cardinality5 | 0.09 | 23 | = 0.928 | 0.02 [-0.40, 0.44] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -1.42 | 23 | = 0.571 | -0.19 [-0.72, 0.14] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -1.02 | 23 | = 0.752 | -0.23 [-0.63, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 615.84, BIC = 642.56
- **Cardinality2 vs Cardinality1**: *β* = -1.83, *SE* = 0.486, *z* = -3.765, *p* < .001
- **Cardinality3 vs Cardinality1**: *β* = -1.54, *SE* = 0.488, *z* = -3.162, *p* = 0.002
- **Cardinality4 vs Cardinality1**: *β* = -1.47, *SE* = 0.497, *z* = -2.950, *p* = 0.003
- **Cardinality5 vs Cardinality1**: *β* = -1.88, *SE* = 0.498, *z* = -3.767, *p* < .001
- **Cardinality6 vs Cardinality1**: *β* = -1.64, *SE* = 0.490, *z* = -3.343, *p* = 0.001
- **SNR**: *β* = -0.47, *SE* = 0.062, *z* = -7.491, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 1.83 | 0.49 | 3.76 | < .001 | 0.002 | ** |
| Cardinality1 - Cardinality3 | 1.54 | 0.49 | 3.16 | 0.002 | 0.019 | * |
| Cardinality1 - Cardinality4 | 1.47 | 0.50 | 2.95 | 0.003 | 0.034 | * |
| Cardinality1 - Cardinality5 | 1.88 | 0.50 | 3.77 | < .001 | 0.002 | ** |
| Cardinality1 - Cardinality6 | 1.64 | 0.49 | 3.34 | < .001 | 0.011 | * |
| Cardinality2 - Cardinality3 | -0.29 | 0.49 | -0.59 | 0.553 | 0.996 | n.s. |
| Cardinality2 - Cardinality4 | -0.36 | 0.49 | -0.74 | 0.461 | 0.996 | n.s. |
| Cardinality2 - Cardinality5 | 0.05 | 0.49 | 0.09 | 0.927 | 0.997 | n.s. |
| Cardinality2 - Cardinality6 | -0.19 | 0.49 | -0.39 | 0.694 | 0.997 | n.s. |
| Cardinality3 - Cardinality4 | -0.08 | 0.49 | -0.15 | 0.878 | 0.997 | n.s. |
| Cardinality3 - Cardinality5 | 0.33 | 0.49 | 0.68 | 0.496 | 0.996 | n.s. |
| Cardinality3 - Cardinality6 | 0.10 | 0.49 | 0.20 | 0.842 | 0.997 | n.s. |
| Cardinality4 - Cardinality5 | 0.41 | 0.49 | 0.84 | 0.400 | 0.994 | n.s. |
| Cardinality4 - Cardinality6 | 0.17 | 0.49 | 0.35 | 0.724 | 0.997 | n.s. |
| Cardinality5 - Cardinality6 | -0.24 | 0.49 | -0.49 | 0.627 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.37, *p* < .001, η²_G = 0.090
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 2.95 | 23 | = 0.022 | 0.75 [0.14, 1.06] | medium | * |
| Cardinality1 vs Cardinality3 | 3.59 | 23 | = 0.012 | 0.80 [0.26, 1.21] | medium | * |
| Cardinality1 vs Cardinality4 | 2.97 | 23 | = 0.022 | 0.75 [0.15, 1.07] | medium | * |
| Cardinality1 vs Cardinality5 | 4.19 | 23 | = 0.005 | 1.04 [0.36, 1.35] | large | ** |
| Cardinality1 vs Cardinality6 | 3.16 | 23 | = 0.022 | 0.72 [0.18, 1.11] | medium | * |
| Cardinality2 vs Cardinality3 | -0.29 | 23 | = 0.778 | -0.06 [-0.48, 0.36] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | 0.61 | 23 | = 0.749 | 0.09 [-0.30, 0.55] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 1.19 | 23 | = 0.529 | 0.27 [-0.19, 0.67] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.29 | 23 | = 0.778 | 0.05 [-0.36, 0.48] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | 0.68 | 23 | = 0.749 | 0.15 [-0.29, 0.56] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | 1.65 | 23 | = 0.281 | 0.37 [-0.10, 0.77] | small | n.s. |
| Cardinality3 vs Cardinality6 | 0.50 | 23 | = 0.776 | 0.10 [-0.32, 0.53] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.76 | 23 | = 0.749 | 0.15 [-0.27, 0.58] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -0.31 | 23 | = 0.778 | -0.04 [-0.49, 0.36] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -1.03 | 23 | = 0.590 | -0.19 [-0.64, 0.22] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1059.89, BIC = 1086.62
- **Cardinality2 vs Cardinality1**: *β* = -5.33, *SE* = 2.395, *z* = -2.227, *p* = 0.026
- **Cardinality3 vs Cardinality1**: *β* = -3.66, *SE* = 2.397, *z* = -1.527, *p* = 0.127
- **Cardinality4 vs Cardinality1**: *β* = -2.66, *SE* = 2.395, *z* = -1.112, *p* = 0.266
- **Cardinality5 vs Cardinality1**: *β* = -9.50, *SE* = 2.395, *z* = -3.968, *p* < .001
- **Cardinality6 vs Cardinality1**: *β* = -6.66, *SE* = 2.398, *z* = -2.779, *p* = 0.005
- **SNR**: *β* = 0.02, *SE* = 0.426, *z* = 0.038, *p* = 0.969

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 5.33 | 2.39 | 2.23 | 0.026 | 0.251 | n.s. |
| Cardinality1 - Cardinality3 | 3.66 | 2.40 | 1.53 | 0.127 | 0.662 | n.s. |
| Cardinality1 - Cardinality4 | 2.66 | 2.40 | 1.11 | 0.266 | 0.808 | n.s. |
| Cardinality1 - Cardinality5 | 9.50 | 2.39 | 3.97 | < .001 | 0.001 | ** |
| Cardinality1 - Cardinality6 | 6.66 | 2.40 | 2.78 | 0.005 | 0.069 | n.s. |
| Cardinality2 - Cardinality3 | -1.67 | 2.40 | -0.70 | 0.486 | 0.864 | n.s. |
| Cardinality2 - Cardinality4 | -2.67 | 2.39 | -1.11 | 0.265 | 0.808 | n.s. |
| Cardinality2 - Cardinality5 | 4.17 | 2.40 | 1.74 | 0.082 | 0.574 | n.s. |
| Cardinality2 - Cardinality6 | 1.33 | 2.40 | 0.56 | 0.579 | 0.864 | n.s. |
| Cardinality3 - Cardinality4 | -1.00 | 2.39 | -0.42 | 0.677 | 0.864 | n.s. |
| Cardinality3 - Cardinality5 | 5.84 | 2.40 | 2.43 | 0.015 | 0.165 | n.s. |
| Cardinality3 - Cardinality6 | 3.00 | 2.39 | 1.25 | 0.210 | 0.808 | n.s. |
| Cardinality4 - Cardinality5 | 6.84 | 2.40 | 2.85 | 0.004 | 0.059 | n.s. |
| Cardinality4 - Cardinality6 | 4.00 | 2.39 | 1.67 | 0.095 | 0.593 | n.s. |
| Cardinality5 - Cardinality6 | -2.84 | 2.40 | -1.18 | 0.237 | 0.808 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.65, *p* = 0.004, η²_G = 0.093
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.81 | 23 | = 0.224 | 0.54 [-0.07, 0.81] | medium | n.s. |
| Cardinality1 vs Cardinality3 | 1.27 | 23 | = 0.325 | 0.38 [-0.17, 0.69] | small | n.s. |
| Cardinality1 vs Cardinality4 | 1.18 | 23 | = 0.327 | 0.27 [-0.19, 0.67] | small | n.s. |
| Cardinality1 vs Cardinality5 | 3.99 | 23 | = 0.009 | 1.08 [0.33, 1.30] | large | ** |
| Cardinality1 vs Cardinality6 | 2.89 | 23 | = 0.041 | 0.72 [0.13, 1.05] | medium | * |
| Cardinality2 vs Cardinality3 | -0.64 | 23 | = 0.610 | -0.16 [-0.55, 0.29] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -1.15 | 23 | = 0.327 | -0.26 [-0.66, 0.19] | small | n.s. |
| Cardinality2 vs Cardinality5 | 1.51 | 23 | = 0.272 | 0.44 [-0.12, 0.74] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.53 | 23 | = 0.643 | 0.13 [-0.32, 0.53] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.37 | 23 | = 0.715 | -0.10 [-0.50, 0.35] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | 2.88 | 23 | = 0.041 | 0.64 [0.13, 1.04] | medium | * |
| Cardinality3 vs Cardinality6 | 1.33 | 23 | = 0.325 | 0.31 [-0.16, 0.70] | small | n.s. |
| Cardinality4 vs Cardinality5 | 2.76 | 23 | = 0.041 | 0.73 [0.11, 1.02] | medium | * |
| Cardinality4 vs Cardinality6 | 1.77 | 23 | = 0.224 | 0.41 [-0.07, 0.80] | small | n.s. |
| Cardinality5 vs Cardinality6 | -1.69 | 23 | = 0.224 | -0.32 [-0.78, 0.09] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 651.11, BIC = 677.84
- **Cardinality2 vs Cardinality1**: *β* = -2.34, *SE* = 0.543, *z* = -4.302, *p* < .001
- **Cardinality3 vs Cardinality1**: *β* = -1.86, *SE* = 0.544, *z* = -3.426, *p* = 0.001
- **Cardinality4 vs Cardinality1**: *β* = -1.79, *SE* = 0.543, *z* = -3.287, *p* = 0.001
- **Cardinality5 vs Cardinality1**: *β* = -1.92, *SE* = 0.543, *z* = -3.539, *p* < .001
- **Cardinality6 vs Cardinality1**: *β* = -2.07, *SE* = 0.544, *z* = -3.801, *p* < .001
- **SNR**: *β* = 0.18, *SE* = 0.100, *z* = 1.817, *p* = 0.069

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 2.34 | 0.54 | 4.30 | < .001 | < .001 | *** |
| Cardinality1 - Cardinality3 | 1.86 | 0.54 | 3.43 | < .001 | 0.007 | ** |
| Cardinality1 - Cardinality4 | 1.79 | 0.54 | 3.29 | 0.001 | 0.011 | * |
| Cardinality1 - Cardinality5 | 1.92 | 0.54 | 3.54 | < .001 | 0.005 | ** |
| Cardinality1 - Cardinality6 | 2.07 | 0.54 | 3.80 | < .001 | 0.002 | ** |
| Cardinality2 - Cardinality3 | -0.47 | 0.54 | -0.87 | 0.383 | 0.987 | n.s. |
| Cardinality2 - Cardinality4 | -0.55 | 0.54 | -1.01 | 0.311 | 0.976 | n.s. |
| Cardinality2 - Cardinality5 | -0.41 | 0.54 | -0.76 | 0.445 | 0.991 | n.s. |
| Cardinality2 - Cardinality6 | -0.27 | 0.54 | -0.50 | 0.620 | 0.998 | n.s. |
| Cardinality3 - Cardinality4 | -0.08 | 0.54 | -0.14 | 0.887 | 0.998 | n.s. |
| Cardinality3 - Cardinality5 | 0.06 | 0.54 | 0.11 | 0.914 | 0.998 | n.s. |
| Cardinality3 - Cardinality6 | 0.20 | 0.54 | 0.38 | 0.707 | 0.998 | n.s. |
| Cardinality4 - Cardinality5 | 0.14 | 0.54 | 0.25 | 0.803 | 0.998 | n.s. |
| Cardinality4 - Cardinality6 | 0.28 | 0.54 | 0.52 | 0.605 | 0.998 | n.s. |
| Cardinality5 - Cardinality6 | 0.15 | 0.54 | 0.27 | 0.790 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.59, *p* < .001, η²_G = 0.083
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 4.14 | 23 | = 0.006 | 0.78 [0.35, 1.34] | medium | ** |
| Cardinality1 vs Cardinality3 | 2.95 | 23 | = 0.022 | 0.63 [0.14, 1.06] | medium | * |
| Cardinality1 vs Cardinality4 | 3.20 | 23 | = 0.020 | 0.66 [0.19, 1.12] | medium | * |
| Cardinality1 vs Cardinality5 | 2.99 | 23 | = 0.022 | 0.73 [0.15, 1.07] | medium | * |
| Cardinality1 vs Cardinality6 | 3.32 | 23 | = 0.020 | 0.76 [0.21, 1.15] | medium | * |
| Cardinality2 vs Cardinality3 | -0.68 | 23 | = 0.839 | -0.15 [-0.56, 0.29] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -1.33 | 23 | = 0.495 | -0.21 [-0.70, 0.16] | small | n.s. |
| Cardinality2 vs Cardinality5 | -0.91 | 23 | = 0.801 | -0.18 [-0.61, 0.24] | negligible | n.s. |
| Cardinality2 vs Cardinality6 | -0.41 | 23 | = 0.900 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.17 | 23 | = 0.926 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | -0.01 | 23 | = 0.992 | -0.00 [-0.42, 0.42] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | 0.36 | 23 | = 0.900 | 0.08 [-0.35, 0.50] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.19 | 23 | = 0.926 | 0.04 [-0.38, 0.46] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | 0.71 | 23 | = 0.839 | 0.13 [-0.28, 0.57] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | 0.39 | 23 | = 0.900 | 0.10 [-0.34, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1210.97, BIC = 1237.70
- **Cardinality2 vs Cardinality1**: *β* = -2.15, *SE* = 4.418, *z* = -0.486, *p* = 0.627
- **Cardinality3 vs Cardinality1**: *β* = -5.13, *SE* = 4.479, *z* = -1.145, *p* = 0.252
- **Cardinality4 vs Cardinality1**: *β* = -1.87, *SE* = 4.448, *z* = -0.421, *p* = 0.674
- **Cardinality5 vs Cardinality1**: *β* = -1.06, *SE* = 4.439, *z* = -0.240, *p* = 0.810
- **Cardinality6 vs Cardinality1**: *β* = -1.95, *SE* = 4.485, *z* = -0.434, *p* = 0.665
- **SNR**: *β* = -0.23, *SE* = 0.526, *z* = -0.439, *p* = 0.661

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 2.15 | 4.42 | 0.49 | 0.627 | 1.000 | n.s. |
| Cardinality1 - Cardinality3 | 5.13 | 4.48 | 1.14 | 0.252 | 0.987 | n.s. |
| Cardinality1 - Cardinality4 | 1.87 | 4.45 | 0.42 | 0.674 | 1.000 | n.s. |
| Cardinality1 - Cardinality5 | 1.07 | 4.44 | 0.24 | 0.810 | 1.000 | n.s. |
| Cardinality1 - Cardinality6 | 1.94 | 4.49 | 0.43 | 0.665 | 1.000 | n.s. |
| Cardinality2 - Cardinality3 | 2.98 | 4.42 | 0.67 | 0.500 | 1.000 | n.s. |
| Cardinality2 - Cardinality4 | -0.28 | 4.40 | -0.06 | 0.950 | 1.000 | n.s. |
| Cardinality2 - Cardinality5 | -1.08 | 4.40 | -0.25 | 0.806 | 1.000 | n.s. |
| Cardinality2 - Cardinality6 | -0.20 | 4.42 | -0.05 | 0.964 | 1.000 | n.s. |
| Cardinality3 - Cardinality4 | -3.26 | 4.40 | -0.74 | 0.459 | 1.000 | n.s. |
| Cardinality3 - Cardinality5 | -4.06 | 4.40 | -0.92 | 0.356 | 0.998 | n.s. |
| Cardinality3 - Cardinality6 | -3.18 | 4.40 | -0.72 | 0.469 | 1.000 | n.s. |
| Cardinality4 - Cardinality5 | -0.81 | 4.40 | -0.18 | 0.855 | 1.000 | n.s. |
| Cardinality4 - Cardinality6 | 0.07 | 4.40 | 0.02 | 0.987 | 1.000 | n.s. |
| Cardinality5 - Cardinality6 | 0.88 | 4.41 | 0.20 | 0.842 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.32, *p* = 0.897, η²_G = 0.012
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.52 | 23 | = 1.000 | 0.15 [-0.32, 0.53] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 1.25 | 23 | = 1.000 | 0.38 [-0.17, 0.68] | small | n.s. |
| Cardinality1 vs Cardinality4 | 0.45 | 23 | = 1.000 | 0.15 [-0.33, 0.52] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | 0.26 | 23 | = 1.000 | 0.08 [-0.37, 0.48] | negligible | n.s. |
| Cardinality1 vs Cardinality6 | 0.46 | 23 | = 1.000 | 0.15 [-0.33, 0.52] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.67 | 23 | = 1.000 | 0.21 [-0.29, 0.56] | small | n.s. |
| Cardinality2 vs Cardinality4 | -0.04 | 23 | = 1.000 | -0.01 [-0.43, 0.42] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | -0.24 | 23 | = 1.000 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| Cardinality2 vs Cardinality6 | 0.00 | 23 | = 1.000 | 0.00 [-0.42, 0.42] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.86 | 23 | = 1.000 | -0.24 [-0.60, 0.25] | small | n.s. |
| Cardinality3 vs Cardinality5 | -0.90 | 23 | = 1.000 | -0.27 [-0.61, 0.24] | small | n.s. |
| Cardinality3 vs Cardinality6 | -0.67 | 23 | = 1.000 | -0.21 [-0.56, 0.29] | small | n.s. |
| Cardinality4 vs Cardinality5 | -0.22 | 23 | = 1.000 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | 0.05 | 23 | = 1.000 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | 0.21 | 23 | = 1.000 | 0.06 [-0.38, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 703.03, BIC = 729.75
- **Cardinality2 vs Cardinality1**: *β* = 0.46, *SE* = 0.630, *z* = 0.734, *p* = 0.463
- **Cardinality3 vs Cardinality1**: *β* = 1.38, *SE* = 0.646, *z* = 2.127, *p* = 0.033
- **Cardinality4 vs Cardinality1**: *β* = -0.07, *SE* = 0.638, *z* = -0.112, *p* = 0.911
- **Cardinality5 vs Cardinality1**: *β* = -0.32, *SE* = 0.636, *z* = -0.504, *p* = 0.614
- **Cardinality6 vs Cardinality1**: *β* = 0.72, *SE* = 0.648, *z* = 1.112, *p* = 0.266
- **SNR**: *β* = 0.03, *SE* = 0.102, *z* = 0.334, *p* = 0.738

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | -0.46 | 0.63 | -0.73 | 0.463 | 0.955 | n.s. |
| Cardinality1 - Cardinality3 | -1.37 | 0.65 | -2.13 | 0.033 | 0.357 | n.s. |
| Cardinality1 - Cardinality4 | 0.07 | 0.64 | 0.11 | 0.911 | 0.978 | n.s. |
| Cardinality1 - Cardinality5 | 0.32 | 0.64 | 0.50 | 0.614 | 0.978 | n.s. |
| Cardinality1 - Cardinality6 | -0.72 | 0.65 | -1.11 | 0.266 | 0.916 | n.s. |
| Cardinality2 - Cardinality3 | -0.91 | 0.63 | -1.45 | 0.148 | 0.828 | n.s. |
| Cardinality2 - Cardinality4 | 0.53 | 0.63 | 0.85 | 0.394 | 0.951 | n.s. |
| Cardinality2 - Cardinality5 | 0.78 | 0.63 | 1.25 | 0.211 | 0.900 | n.s. |
| Cardinality2 - Cardinality6 | -0.26 | 0.63 | -0.41 | 0.683 | 0.978 | n.s. |
| Cardinality3 - Cardinality4 | 1.45 | 0.63 | 2.31 | 0.021 | 0.255 | n.s. |
| Cardinality3 - Cardinality5 | 1.70 | 0.63 | 2.71 | 0.007 | 0.097 | n.s. |
| Cardinality3 - Cardinality6 | 0.65 | 0.62 | 1.05 | 0.295 | 0.916 | n.s. |
| Cardinality4 - Cardinality5 | 0.25 | 0.62 | 0.40 | 0.690 | 0.978 | n.s. |
| Cardinality4 - Cardinality6 | -0.79 | 0.63 | -1.26 | 0.206 | 0.900 | n.s. |
| Cardinality5 - Cardinality6 | -1.04 | 0.63 | -1.66 | 0.097 | 0.705 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.97, *p* = 0.088, η²_G = 0.029
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | -0.86 | 23 | = 0.636 | -0.16 [-0.60, 0.25] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | -2.15 | 23 | = 0.317 | -0.44 [-0.88, 0.00] | small | n.s. |
| Cardinality1 vs Cardinality4 | 0.04 | 23 | = 0.965 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | 0.60 | 23 | = 0.692 | 0.10 [-0.30, 0.55] | negligible | n.s. |
| Cardinality1 vs Cardinality6 | -1.34 | 23 | = 0.437 | -0.23 [-0.70, 0.16] | small | n.s. |
| Cardinality2 vs Cardinality3 | -1.64 | 23 | = 0.372 | -0.28 [-0.77, 0.10] | small | n.s. |
| Cardinality2 vs Cardinality4 | 0.71 | 23 | = 0.665 | 0.14 [-0.28, 0.57] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 1.31 | 23 | = 0.437 | 0.26 [-0.16, 0.70] | small | n.s. |
| Cardinality2 vs Cardinality6 | -0.48 | 23 | = 0.726 | -0.08 [-0.52, 0.33] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | 1.92 | 23 | = 0.335 | 0.38 [-0.05, 0.83] | small | n.s. |
| Cardinality3 vs Cardinality5 | 2.75 | 23 | = 0.171 | 0.54 [0.11, 1.02] | medium | n.s. |
| Cardinality3 vs Cardinality6 | 0.81 | 23 | = 0.636 | 0.18 [-0.26, 0.59] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.42 | 23 | = 0.726 | 0.07 [-0.34, 0.51] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -1.21 | 23 | = 0.446 | -0.21 [-0.68, 0.18] | small | n.s. |
| Cardinality5 vs Cardinality6 | -1.60 | 23 | = 0.372 | -0.32 [-0.76, 0.11] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz latency:** Marginal trend toward condition differences (*p* = 0.096)
**N1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality1 showed greater amplitude than Cardinality2 (*d* = 0.75)
  - Cardinality1 showed greater amplitude than Cardinality3 (*d* = 0.80)
  - Cardinality1 showed greater amplitude than Cardinality4 (*d* = 0.75)
  - Cardinality1 showed greater amplitude than Cardinality5 (*d* = 1.04)
  - Cardinality1 showed greater amplitude than Cardinality6 (*d* = 0.72)
**P1 latency:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Cardinality1 showed greater latency than Cardinality5 (*d* = 1.08)
  - Cardinality1 showed greater latency than Cardinality6 (*d* = 0.72)
  - Cardinality3 showed greater latency than Cardinality5 (*d* = 0.64)
  - Cardinality4 showed greater latency than Cardinality5 (*d* = 0.73)
**P1 amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Cardinality1 showed greater amplitude than Cardinality2 (*d* = 0.78)
  - Cardinality1 showed greater amplitude than Cardinality3 (*d* = 0.63)
  - Cardinality1 showed greater amplitude than Cardinality4 (*d* = 0.66)
  - Cardinality1 showed greater amplitude than Cardinality5 (*d* = 0.73)
  - Cardinality1 showed greater amplitude than Cardinality6 (*d* = 0.76)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.088)

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
