# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:36:26

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
| 2 to 1 | 17 | 108.47 ms | 8.82 | 2.14 | [92.00, 116.00] |
| 3 to 2 | 13 | 104.31 ms | 8.71 | 2.42 | [92.00, 116.00] |
| 4 to 3 | 12 | 103.33 ms | 6.79 | 1.96 | [92.00, 116.00] |
| 5 to 4 | 14 | 105.14 ms | 9.34 | 2.50 | [92.00, 116.00] |
| 6 to 5 | 12 | 104.67 ms | 7.00 | 2.02 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 17 | -2.75 µV | 1.55 | 0.38 | [-6.41, -0.16] |
| 3 to 2 | 13 | -2.78 µV | 1.64 | 0.45 | [-5.65, -0.61] |
| 4 to 3 | 12 | -2.26 µV | 1.66 | 0.48 | [-6.08, -0.30] |
| 5 to 4 | 14 | -3.15 µV | 1.78 | 0.48 | [-7.02, -1.08] |
| 6 to 5 | 12 | -2.91 µV | 2.19 | 0.63 | [-8.14, -0.31] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | 180.50 ms | 11.85 | 2.96 | [160.00, 204.00] |
| 3 to 2 | 24 | 176.83 ms | 19.31 | 3.94 | [148.00, 204.00] |
| 4 to 3 | 23 | 174.78 ms | 16.56 | 3.45 | [148.00, 204.00] |
| 5 to 4 | 23 | 176.35 ms | 18.37 | 3.83 | [148.00, 204.00] |
| 6 to 5 | 24 | 172.83 ms | 19.35 | 3.95 | [148.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 16 | -4.98 µV | 2.67 | 0.67 | [-10.79, -1.30] |
| 3 to 2 | 24 | -5.66 µV | 2.58 | 0.53 | [-10.33, -1.35] |
| 4 to 3 | 23 | -6.39 µV | 2.15 | 0.45 | [-11.27, -1.89] |
| 5 to 4 | 23 | -5.97 µV | 2.82 | 0.59 | [-14.15, -1.72] |
| 6 to 5 | 24 | -5.89 µV | 2.12 | 0.43 | [-10.60, -2.05] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 114.67 ms | 7.51 | 1.77 | [96.00, 120.00] |
| 3 to 2 | 12 | 105.67 ms | 8.77 | 2.53 | [96.00, 120.00] |
| 4 to 3 | 11 | 106.18 ms | 8.46 | 2.55 | [96.00, 120.00] |
| 5 to 4 | 15 | 111.20 ms | 9.59 | 2.48 | [96.00, 120.00] |
| 6 to 5 | 12 | 108.33 ms | 8.94 | 2.58 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 18 | 4.27 µV | 2.22 | 0.52 | [2.23, 9.13] |
| 3 to 2 | 12 | 2.43 µV | 1.75 | 0.50 | [0.60, 5.61] |
| 4 to 3 | 11 | 2.79 µV | 1.50 | 0.45 | [0.60, 5.30] |
| 5 to 4 | 15 | 2.96 µV | 1.82 | 0.47 | [0.98, 7.17] |
| 6 to 5 | 12 | 3.26 µV | 2.65 | 0.77 | [0.58, 9.47] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 505.05 ms | 31.49 | 7.22 | [436.00, 548.00] |
| 3 to 2 | 18 | 492.89 ms | 34.78 | 8.20 | [436.00, 548.00] |
| 4 to 3 | 21 | 480.38 ms | 31.47 | 6.87 | [436.00, 536.00] |
| 5 to 4 | 18 | 503.56 ms | 30.86 | 7.27 | [440.00, 548.00] |
| 6 to 5 | 13 | 515.38 ms | 33.82 | 9.38 | [460.00, 548.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 1 | 19 | 6.06 µV | 2.64 | 0.61 | [1.72, 11.08] |
| 3 to 2 | 18 | 6.58 µV | 4.05 | 0.96 | [2.10, 17.81] |
| 4 to 3 | 21 | 5.40 µV | 3.08 | 0.67 | [1.06, 11.65] |
| 5 to 4 | 18 | 6.12 µV | 3.10 | 0.73 | [1.76, 11.49] |
| 6 to 5 | 13 | 4.85 µV | 2.32 | 0.64 | [2.38, 10.64] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 487.30, BIC = 505.05
- **3 to 2 vs 2 to 1**: *β* = -3.96, *SE* = 2.637, *z* = -1.500, *p* = 0.134
- **4 to 3 vs 2 to 1**: *β* = -4.56, *SE* = 2.689, *z* = -1.696, *p* = 0.090
- **5 to 4 vs 2 to 1**: *β* = -2.35, *SE* = 2.615, *z* = -0.898, *p* = 0.369
- **6 to 5 vs 2 to 1**: *β* = -3.36, *SE* = 2.699, *z* = -1.246, *p* = 0.213
- **SNR**: *β* = 0.37, *SE* = 0.643, *z* = 0.576, *p* = 0.565

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 3.96 | 2.64 | 1.50 | 0.134 | 0.725 | n.s. |
| 2 to 1 - 4 to 3 | 4.56 | 2.69 | 1.70 | 0.090 | 0.610 | n.s. |
| 2 to 1 - 5 to 4 | 2.35 | 2.61 | 0.90 | 0.369 | 0.960 | n.s. |
| 2 to 1 - 6 to 5 | 3.36 | 2.70 | 1.25 | 0.213 | 0.852 | n.s. |
| 3 to 2 - 4 to 3 | 0.61 | 2.87 | 0.21 | 0.833 | 0.989 | n.s. |
| 3 to 2 - 5 to 4 | -1.61 | 2.78 | -0.58 | 0.563 | 0.984 | n.s. |
| 3 to 2 - 6 to 5 | -0.59 | 2.87 | -0.21 | 0.836 | 0.989 | n.s. |
| 4 to 3 - 5 to 4 | -2.21 | 2.82 | -0.79 | 0.432 | 0.966 | n.s. |
| 4 to 3 - 6 to 5 | -1.20 | 2.88 | -0.42 | 0.677 | 0.989 | n.s. |
| 5 to 4 - 6 to 5 | 1.02 | 2.79 | 0.36 | 0.716 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.65, *p* = 0.641, η²_G = 0.244
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.00 | 2 | = 0.741 | 1.10 [-0.36, 1.25] | large | n.s. |
| 2 to 1 vs 4 to 3 | 0.65 | 2 | = 0.741 | 0.71 [-0.33, 1.17] | medium | n.s. |
| 2 to 1 vs 5 to 4 | 0.64 | 2 | = 0.741 | 0.58 [-0.81, 0.62] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 0.50 | 2 | = 0.741 | 0.41 [-0.41, 1.19] | small | n.s. |
| 3 to 2 vs 4 to 3 | -1.73 | 2 | = 0.741 | -0.53 [-0.70, 0.98] | medium | n.s. |
| 3 to 2 vs 5 to 4 | -1.00 | 2 | = 0.741 | -0.70 [-0.90, 0.64] | medium | n.s. |
| 3 to 2 vs 6 to 5 | -2.00 | 2 | = 0.741 | -1.63 [-1.34, 0.58] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.18 | 2 | = 0.874 | -0.16 [-0.97, 0.71] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | -0.87 | 2 | = 0.741 | -0.71 [-0.98, 0.57] | medium | n.s. |
| 5 to 4 vs 6 to 5 | -0.55 | 2 | = 0.741 | -0.45 [-0.59, 0.96] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 212.87, BIC = 230.63
- **3 to 2 vs 2 to 1**: *β* = 0.11, *SE* = 0.343, *z* = 0.326, *p* = 0.745
- **4 to 3 vs 2 to 1**: *β* = 0.22, *SE* = 0.346, *z* = 0.640, *p* = 0.522
- **5 to 4 vs 2 to 1**: *β* = -0.36, *SE* = 0.334, *z* = -1.079, *p* = 0.281
- **6 to 5 vs 2 to 1**: *β* = -0.12, *SE* = 0.351, *z* = -0.346, *p* = 0.729
- **SNR**: *β* = -0.75, *SE* = 0.082, *z* = -9.114, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.11 | 0.34 | -0.33 | 0.745 | 0.985 | n.s. |
| 2 to 1 - 4 to 3 | -0.22 | 0.35 | -0.64 | 0.522 | 0.985 | n.s. |
| 2 to 1 - 5 to 4 | 0.36 | 0.33 | 1.08 | 0.281 | 0.928 | n.s. |
| 2 to 1 - 6 to 5 | 0.12 | 0.35 | 0.35 | 0.729 | 0.985 | n.s. |
| 3 to 2 - 4 to 3 | -0.11 | 0.37 | -0.30 | 0.764 | 0.985 | n.s. |
| 3 to 2 - 5 to 4 | 0.47 | 0.35 | 1.34 | 0.182 | 0.836 | n.s. |
| 3 to 2 - 6 to 5 | 0.23 | 0.37 | 0.63 | 0.528 | 0.985 | n.s. |
| 4 to 3 - 5 to 4 | 0.58 | 0.36 | 1.61 | 0.108 | 0.681 | n.s. |
| 4 to 3 - 6 to 5 | 0.34 | 0.37 | 0.93 | 0.354 | 0.953 | n.s. |
| 5 to 4 - 6 to 5 | -0.24 | 0.36 | -0.67 | 0.505 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.43, *p* = 0.784, η²_G = 0.056
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.66 | 2 | = 0.868 | -0.49 [-0.66, 0.88] | small | n.s. |
| 2 to 1 vs 4 to 3 | -0.58 | 2 | = 0.868 | -0.14 [-1.06, 0.40] | negligible | n.s. |
| 2 to 1 vs 5 to 4 | -0.19 | 2 | = 0.868 | -0.08 [-0.45, 1.00] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 1.28 | 2 | = 0.868 | 0.19 [-0.85, 0.69] | negligible | n.s. |
| 3 to 2 vs 4 to 3 | 0.47 | 2 | = 0.868 | 0.37 [-1.02, 0.67] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.43 | 2 | = 0.868 | 0.37 [-0.71, 0.82] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.82 | 2 | = 0.868 | 0.64 [-0.61, 1.29] | medium | n.s. |
| 4 to 3 vs 5 to 4 | 0.19 | 2 | = 0.868 | 0.05 [-0.37, 1.42] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.26 | 2 | = 0.868 | 0.32 [-0.42, 1.17] | small | n.s. |
| 5 to 4 vs 6 to 5 | 0.70 | 2 | = 0.868 | 0.26 [-0.70, 0.84] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 938.43, BIC = 960.04
- **3 to 2 vs 2 to 1**: *β* = -2.01, *SE* = 4.835, *z* = -0.416, *p* = 0.678
- **4 to 3 vs 2 to 1**: *β* = -3.70, *SE* = 4.928, *z* = -0.751, *p* = 0.453
- **5 to 4 vs 2 to 1**: *β* = -1.56, *SE* = 4.929, *z* = -0.316, *p* = 0.752
- **6 to 5 vs 2 to 1**: *β* = -6.68, *SE* = 4.776, *z* = -1.399, *p* = 0.162
- **SNR**: *β* = -0.98, *SE* = 0.509, *z* = -1.924, *p* = 0.054

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 2.01 | 4.84 | 0.42 | 0.678 | 0.992 | n.s. |
| 2 to 1 - 4 to 3 | 3.70 | 4.93 | 0.75 | 0.453 | 0.985 | n.s. |
| 2 to 1 - 5 to 4 | 1.56 | 4.93 | 0.32 | 0.752 | 0.992 | n.s. |
| 2 to 1 - 6 to 5 | 6.68 | 4.78 | 1.40 | 0.162 | 0.829 | n.s. |
| 3 to 2 - 4 to 3 | 1.69 | 4.23 | 0.40 | 0.690 | 0.992 | n.s. |
| 3 to 2 - 5 to 4 | -0.45 | 4.23 | -0.11 | 0.915 | 0.992 | n.s. |
| 3 to 2 - 6 to 5 | 4.67 | 4.19 | 1.12 | 0.264 | 0.914 | n.s. |
| 4 to 3 - 5 to 4 | -2.14 | 4.28 | -0.50 | 0.617 | 0.992 | n.s. |
| 4 to 3 - 6 to 5 | 2.98 | 4.26 | 0.70 | 0.483 | 0.985 | n.s. |
| 5 to 4 - 6 to 5 | 5.12 | 4.26 | 1.20 | 0.229 | 0.904 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.598, η²_G = 0.028
- Greenhouse-Geisser corrected: *p* = 0.510 (ε = 0.510)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.40 | 13 | = 0.612 | 0.39 [-0.17, 0.94] | small | n.s. |
| 2 to 1 vs 4 to 3 | 1.53 | 13 | = 0.612 | 0.44 [-0.18, 0.97] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.80 | 13 | = 0.854 | 0.23 [-0.39, 0.73] | small | n.s. |
| 2 to 1 vs 6 to 5 | 1.91 | 13 | = 0.612 | 0.52 [-0.12, 1.00] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.00 | 13 | = 1.000 | 0.00 [-0.26, 0.61] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -0.30 | 13 | = 0.854 | -0.12 [-0.46, 0.41] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | 0.39 | 13 | = 0.854 | 0.14 [-0.27, 0.58] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | -0.40 | 13 | = 0.854 | -0.12 [-0.57, 0.32] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 0.40 | 13 | = 0.854 | 0.15 [-0.31, 0.55] | negligible | n.s. |
| 5 to 4 vs 6 to 5 | 1.15 | 13 | = 0.681 | 0.25 [-0.26, 0.61] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 435.64, BIC = 457.25
- **3 to 2 vs 2 to 1**: *β* = -0.34, *SE* = 0.456, *z* = -0.736, *p* = 0.462
- **4 to 3 vs 2 to 1**: *β* = -0.98, *SE* = 0.466, *z* = -2.100, *p* = 0.036
- **5 to 4 vs 2 to 1**: *β* = -0.47, *SE* = 0.466, *z* = -1.004, *p* = 0.315
- **6 to 5 vs 2 to 1**: *β* = -0.85, *SE* = 0.449, *z* = -1.891, *p* = 0.059
- **SNR**: *β* = -0.41, *SE* = 0.050, *z* = -8.204, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.34 | 0.46 | 0.74 | 0.462 | 0.850 | n.s. |
| 2 to 1 - 4 to 3 | 0.98 | 0.47 | 2.10 | 0.036 | 0.305 | n.s. |
| 2 to 1 - 5 to 4 | 0.47 | 0.47 | 1.00 | 0.315 | 0.850 | n.s. |
| 2 to 1 - 6 to 5 | 0.85 | 0.45 | 1.89 | 0.059 | 0.419 | n.s. |
| 3 to 2 - 4 to 3 | 0.64 | 0.39 | 1.63 | 0.102 | 0.578 | n.s. |
| 3 to 2 - 5 to 4 | 0.13 | 0.39 | 0.34 | 0.737 | 0.931 | n.s. |
| 3 to 2 - 6 to 5 | 0.51 | 0.39 | 1.32 | 0.187 | 0.765 | n.s. |
| 4 to 3 - 5 to 4 | -0.51 | 0.40 | -1.28 | 0.199 | 0.765 | n.s. |
| 4 to 3 - 6 to 5 | -0.13 | 0.40 | -0.33 | 0.745 | 0.931 | n.s. |
| 5 to 4 - 6 to 5 | 0.38 | 0.40 | 0.96 | 0.336 | 0.850 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.57, *p* = 0.012, η²_G = 0.101
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 2.73 | 13 | = 0.083 | 0.74 [0.06, 1.23] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 3.25 | 13 | = 0.063 | 0.84 [0.24, 1.55] | large | n.s. |
| 2 to 1 vs 5 to 4 | 2.53 | 13 | = 0.083 | 0.82 [-0.07, 1.11] | large | n.s. |
| 2 to 1 vs 6 to 5 | 1.91 | 13 | = 0.196 | 0.59 [-0.11, 1.01] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.32 | 13 | = 0.838 | 0.08 [-0.08, 0.82] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | 0.50 | 13 | = 0.784 | 0.12 [-0.34, 0.53] | negligible | n.s. |
| 3 to 2 vs 6 to 5 | -0.81 | 13 | = 0.617 | -0.19 [-0.33, 0.52] | negligible | n.s. |
| 4 to 3 vs 5 to 4 | 0.16 | 13 | = 0.874 | 0.05 [-0.59, 0.30] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | -1.15 | 13 | = 0.454 | -0.28 [-0.71, 0.17] | small | n.s. |
| 5 to 4 vs 6 to 5 | -1.45 | 13 | = 0.342 | -0.31 [-0.47, 0.39] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 494.21, BIC = 511.96
- **3 to 2 vs 2 to 1**: *β* = -8.79, *SE* = 3.058, *z* = -2.875, *p* = 0.004
- **4 to 3 vs 2 to 1**: *β* = -8.64, *SE* = 3.042, *z* = -2.841, *p* = 0.005
- **5 to 4 vs 2 to 1**: *β* = -3.29, *SE* = 2.822, *z* = -1.164, *p* = 0.244
- **6 to 5 vs 2 to 1**: *β* = -6.64, *SE* = 2.982, *z* = -2.227, *p* = 0.026
- **SNR**: *β* = 0.11, *SE* = 0.552, *z* = 0.205, *p* = 0.837

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 8.79 | 3.06 | 2.87 | 0.004 | 0.040 | * |
| 2 to 1 - 4 to 3 | 8.64 | 3.04 | 2.84 | 0.005 | 0.040 | * |
| 2 to 1 - 5 to 4 | 3.28 | 2.82 | 1.16 | 0.244 | 0.754 | n.s. |
| 2 to 1 - 6 to 5 | 6.64 | 2.98 | 2.23 | 0.026 | 0.190 | n.s. |
| 3 to 2 - 4 to 3 | -0.15 | 3.22 | -0.05 | 0.963 | 0.963 | n.s. |
| 3 to 2 - 5 to 4 | -5.51 | 2.99 | -1.84 | 0.065 | 0.376 | n.s. |
| 3 to 2 - 6 to 5 | -2.15 | 3.18 | -0.68 | 0.498 | 0.874 | n.s. |
| 4 to 3 - 5 to 4 | -5.36 | 3.06 | -1.75 | 0.080 | 0.393 | n.s. |
| 4 to 3 - 6 to 5 | -2.00 | 3.23 | -0.62 | 0.535 | 0.874 | n.s. |
| 5 to 4 - 6 to 5 | 3.35 | 2.97 | 1.13 | 0.259 | 0.754 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.49, *p* = 0.084, η²_G = 0.195
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.09 | 4 | = 0.448 | 0.65 [-0.18, 1.37] | medium | n.s. |
| 2 to 1 vs 4 to 3 | 2.59 | 4 | = 0.304 | 1.46 [-0.10, 1.66] | large | n.s. |
| 2 to 1 vs 5 to 4 | 1.43 | 4 | = 0.384 | 0.94 [-0.33, 0.98] | large | n.s. |
| 2 to 1 vs 6 to 5 | 1.04 | 4 | = 0.448 | 0.74 [-0.24, 1.29] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 2.67 | 4 | = 0.304 | 0.86 [-0.66, 1.03] | large | n.s. |
| 3 to 2 vs 5 to 4 | 1.50 | 4 | = 0.384 | 0.35 [-1.06, 0.51] | small | n.s. |
| 3 to 2 vs 6 to 5 | 0.53 | 4 | = 0.690 | 0.22 [-1.20, 0.68] | small | n.s. |
| 4 to 3 vs 5 to 4 | -1.41 | 4 | = 0.384 | -0.49 [-1.51, 0.19] | small | n.s. |
| 4 to 3 vs 6 to 5 | -1.50 | 4 | = 0.384 | -0.56 [-1.08, 0.78] | medium | n.s. |
| 5 to 4 vs 6 to 5 | -0.41 | 4 | = 0.704 | -0.10 [-0.17, 1.38] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 232.50, BIC = 250.26
- **3 to 2 vs 2 to 1**: *β* = -0.49, *SE* = 0.417, *z* = -1.173, *p* = 0.241
- **4 to 3 vs 2 to 1**: *β* = -0.71, *SE* = 0.411, *z* = -1.735, *p* = 0.083
- **5 to 4 vs 2 to 1**: *β* = -0.23, *SE* = 0.384, *z* = -0.595, *p* = 0.552
- **6 to 5 vs 2 to 1**: *β* = -0.13, *SE* = 0.405, *z* = -0.311, *p* = 0.756
- **SNR**: *β* = 0.72, *SE* = 0.082, *z* = 8.890, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 0.49 | 0.42 | 1.17 | 0.241 | 0.878 | n.s. |
| 2 to 1 - 4 to 3 | 0.71 | 0.41 | 1.74 | 0.083 | 0.578 | n.s. |
| 2 to 1 - 5 to 4 | 0.23 | 0.38 | 0.59 | 0.552 | 0.972 | n.s. |
| 2 to 1 - 6 to 5 | 0.13 | 0.40 | 0.31 | 0.756 | 0.972 | n.s. |
| 3 to 2 - 4 to 3 | 0.22 | 0.43 | 0.53 | 0.598 | 0.972 | n.s. |
| 3 to 2 - 5 to 4 | -0.26 | 0.40 | -0.66 | 0.511 | 0.972 | n.s. |
| 3 to 2 - 6 to 5 | -0.36 | 0.42 | -0.86 | 0.391 | 0.949 | n.s. |
| 4 to 3 - 5 to 4 | -0.49 | 0.41 | -1.20 | 0.232 | 0.878 | n.s. |
| 4 to 3 - 6 to 5 | -0.59 | 0.43 | -1.37 | 0.172 | 0.818 | n.s. |
| 5 to 4 - 6 to 5 | -0.10 | 0.39 | -0.26 | 0.794 | 0.972 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.28, *p* = 0.320, η²_G = 0.167
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.76 | 4 | = 0.653 | 1.19 [0.09, 1.81] | large | n.s. |
| 2 to 1 vs 4 to 3 | 2.04 | 4 | = 0.653 | 1.05 [0.02, 1.86] | large | n.s. |
| 2 to 1 vs 5 to 4 | 0.86 | 4 | = 0.653 | 0.63 [-0.21, 1.13] | medium | n.s. |
| 2 to 1 vs 6 to 5 | 1.16 | 4 | = 0.653 | 0.53 [-0.07, 1.54] | medium | n.s. |
| 3 to 2 vs 4 to 3 | -0.69 | 4 | = 0.660 | -0.32 [-0.78, 0.89] | small | n.s. |
| 3 to 2 vs 5 to 4 | -1.14 | 4 | = 0.653 | -0.66 [-1.13, 0.45] | medium | n.s. |
| 3 to 2 vs 6 to 5 | -0.82 | 4 | = 0.653 | -0.42 [-1.36, 0.56] | small | n.s. |
| 4 to 3 vs 5 to 4 | -0.84 | 4 | = 0.653 | -0.46 [-0.95, 0.60] | small | n.s. |
| 4 to 3 vs 6 to 5 | -0.50 | 4 | = 0.713 | -0.27 [-1.11, 0.76] | small | n.s. |
| 5 to 4 vs 6 to 5 | 0.06 | 4 | = 0.957 | 0.03 [-0.78, 0.65] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 861.94, BIC = 881.85
- **3 to 2 vs 2 to 1**: *β* = -14.43, *SE* = 7.939, *z* = -1.818, *p* = 0.069
- **4 to 3 vs 2 to 1**: *β* = -22.17, *SE* = 7.688, *z* = -2.884, *p* = 0.004
- **5 to 4 vs 2 to 1**: *β* = 0.69, *SE* = 7.866, *z* = 0.088, *p* = 0.930
- **6 to 5 vs 2 to 1**: *β* = 10.39, *SE* = 8.915, *z* = 1.166, *p* = 0.244
- **SNR**: *β* = -2.18, *SE* = 0.913, *z* = -2.386, *p* = 0.017

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | 14.43 | 7.94 | 1.82 | 0.069 | 0.307 | n.s. |
| 2 to 1 - 4 to 3 | 22.17 | 7.69 | 2.88 | 0.004 | 0.031 | * |
| 2 to 1 - 5 to 4 | -0.69 | 7.87 | -0.09 | 0.930 | 0.930 | n.s. |
| 2 to 1 - 6 to 5 | -10.39 | 8.91 | -1.17 | 0.244 | 0.673 | n.s. |
| 3 to 2 - 4 to 3 | 7.74 | 7.73 | 1.00 | 0.316 | 0.673 | n.s. |
| 3 to 2 - 5 to 4 | -15.12 | 8.02 | -1.89 | 0.059 | 0.307 | n.s. |
| 3 to 2 - 6 to 5 | -24.83 | 8.94 | -2.78 | 0.006 | 0.038 | * |
| 4 to 3 - 5 to 4 | -22.86 | 7.73 | -2.96 | 0.003 | 0.028 | * |
| 4 to 3 - 6 to 5 | -32.57 | 8.74 | -3.73 | < .001 | 0.002 | ** |
| 5 to 4 - 6 to 5 | -9.70 | 8.98 | -1.08 | 0.280 | 0.673 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.52, *p* = 0.056, η²_G = 0.124
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | 1.18 | 10 | = 0.378 | 0.30 [-0.22, 0.87] | small | n.s. |
| 2 to 1 vs 4 to 3 | 1.02 | 10 | = 0.412 | 0.38 [0.04, 1.16] | small | n.s. |
| 2 to 1 vs 5 to 4 | -0.57 | 10 | = 0.643 | -0.24 [-0.60, 0.43] | small | n.s. |
| 2 to 1 vs 6 to 5 | -2.07 | 10 | = 0.218 | -0.67 [-1.37, 0.04] | medium | n.s. |
| 3 to 2 vs 4 to 3 | 0.18 | 10 | = 0.859 | 0.04 [-0.27, 0.74] | negligible | n.s. |
| 3 to 2 vs 5 to 4 | -1.21 | 10 | = 0.378 | -0.49 [-0.95, 0.16] | small | n.s. |
| 3 to 2 vs 6 to 5 | -2.37 | 10 | = 0.197 | -0.85 [-1.47, 0.04] | large | n.s. |
| 4 to 3 vs 5 to 4 | -1.32 | 10 | = 0.378 | -0.58 [-1.06, 0.04] | medium | n.s. |
| 4 to 3 vs 6 to 5 | -2.41 | 10 | = 0.197 | -0.97 [-1.53, -0.13] | large | n.s. |
| 5 to 4 vs 6 to 5 | -1.25 | 10 | = 0.378 | -0.40 [-1.07, 0.25] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 398.99, BIC = 418.90
- **3 to 2 vs 2 to 1**: *β* = 0.85, *SE* = 0.572, *z* = 1.480, *p* = 0.139
- **4 to 3 vs 2 to 1**: *β* = -0.60, *SE* = 0.553, *z* = -1.094, *p* = 0.274
- **5 to 4 vs 2 to 1**: *β* = 0.00, *SE* = 0.565, *z* = 0.000, *p* = 1.000
- **6 to 5 vs 2 to 1**: *β* = -1.10, *SE* = 0.645, *z* = -1.709, *p* = 0.088
- **SNR**: *β* = 0.54, *SE* = 0.066, *z* = 8.246, *p* < .001

_Reference condition: **2 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2 to 1 - 3 to 2 | -0.85 | 0.57 | -1.48 | 0.139 | 0.592 | n.s. |
| 2 to 1 - 4 to 3 | 0.61 | 0.55 | 1.09 | 0.274 | 0.722 | n.s. |
| 2 to 1 - 5 to 4 | -0.00 | 0.57 | -0.00 | 1.000 | 1.000 | n.s. |
| 2 to 1 - 6 to 5 | 1.10 | 0.65 | 1.71 | 0.088 | 0.519 | n.s. |
| 3 to 2 - 4 to 3 | 1.45 | 0.55 | 2.62 | 0.009 | 0.077 | n.s. |
| 3 to 2 - 5 to 4 | 0.85 | 0.58 | 1.47 | 0.142 | 0.592 | n.s. |
| 3 to 2 - 6 to 5 | 1.95 | 0.65 | 3.01 | 0.003 | 0.026 | * |
| 4 to 3 - 5 to 4 | -0.61 | 0.56 | -1.09 | 0.277 | 0.722 | n.s. |
| 4 to 3 - 6 to 5 | 0.50 | 0.64 | 0.78 | 0.434 | 0.722 | n.s. |
| 5 to 4 - 6 to 5 | 1.10 | 0.65 | 1.69 | 0.090 | 0.519 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.44, *p* = 0.063, η²_G = 0.133
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 1 vs 3 to 2 | -0.59 | 10 | = 0.707 | -0.25 [-0.70, 0.37] | small | n.s. |
| 2 to 1 vs 4 to 3 | 0.65 | 10 | = 0.707 | 0.26 [-0.41, 0.62] | small | n.s. |
| 2 to 1 vs 5 to 4 | 0.31 | 10 | = 0.765 | 0.12 [-0.53, 0.50] | negligible | n.s. |
| 2 to 1 vs 6 to 5 | 2.56 | 10 | = 0.120 | 1.17 [0.03, 1.47] | large | n.s. |
| 3 to 2 vs 4 to 3 | 1.50 | 10 | = 0.382 | 0.41 [-0.28, 0.72] | small | n.s. |
| 3 to 2 vs 5 to 4 | 0.87 | 10 | = 0.678 | 0.31 [-0.36, 0.71] | small | n.s. |
| 3 to 2 vs 6 to 5 | 2.42 | 10 | = 0.120 | 1.02 [-0.03, 1.49] | large | n.s. |
| 4 to 3 vs 5 to 4 | -0.40 | 10 | = 0.765 | -0.12 [-0.63, 0.40] | negligible | n.s. |
| 4 to 3 vs 6 to 5 | 1.40 | 10 | = 0.382 | 0.67 [-0.26, 0.99] | medium | n.s. |
| 5 to 4 vs 6 to 5 | 2.84 | 10 | = 0.120 | 0.82 [0.17, 1.69] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.012) (no significant pairwise comparisons)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.084)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.056)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.063)

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
