# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:28:48

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
| 1 to 4 | 24 | 105.17 ms | 8.54 | 1.74 | [96.00, 116.00] |
| 2 to 4 | 24 | 103.83 ms | 7.95 | 1.62 | [96.00, 116.00] |
| 3 to 4 | 24 | 104.33 ms | 7.82 | 1.60 | [96.00, 116.00] |
| 4 to 4 | 24 | 107.33 ms | 7.70 | 1.57 | [96.00, 116.00] |
| 5 to 4 | 24 | 106.67 ms | 7.70 | 1.57 | [96.00, 116.00] |
| 6 to 4 | 24 | 107.83 ms | 7.87 | 1.61 | [96.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -1.23 µV | 2.04 | 0.42 | [-4.46, 2.75] |
| 2 to 4 | 24 | -1.98 µV | 2.23 | 0.46 | [-6.14, 1.91] |
| 3 to 4 | 24 | -1.60 µV | 1.97 | 0.40 | [-5.42, 2.48] |
| 4 to 4 | 24 | -1.56 µV | 1.86 | 0.38 | [-6.84, 1.26] |
| 5 to 4 | 24 | -1.73 µV | 2.89 | 0.59 | [-8.72, 3.27] |
| 6 to 4 | 24 | -2.12 µV | 2.26 | 0.46 | [-8.69, 3.05] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 174.17 ms | 16.51 | 3.37 | [144.00, 204.00] |
| 2 to 4 | 24 | 173.00 ms | 17.02 | 3.47 | [144.00, 204.00] |
| 3 to 4 | 24 | 166.17 ms | 17.89 | 3.65 | [144.00, 204.00] |
| 4 to 4 | 24 | 172.00 ms | 19.77 | 4.04 | [144.00, 204.00] |
| 5 to 4 | 24 | 174.83 ms | 19.72 | 4.03 | [144.00, 204.00] |
| 6 to 4 | 24 | 174.00 ms | 20.12 | 4.11 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | -6.38 µV | 3.23 | 0.66 | [-13.14, -1.20] |
| 2 to 4 | 24 | -6.05 µV | 3.18 | 0.65 | [-15.66, 1.34] |
| 3 to 4 | 24 | -5.67 µV | 2.31 | 0.47 | [-10.53, -0.26] |
| 4 to 4 | 24 | -5.52 µV | 3.34 | 0.68 | [-13.09, 0.33] |
| 5 to 4 | 24 | -5.84 µV | 3.16 | 0.64 | [-14.15, 0.32] |
| 6 to 4 | 24 | -5.78 µV | 3.02 | 0.62 | [-12.20, -0.24] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 100.17 ms | 9.69 | 1.98 | [92.00, 120.00] |
| 2 to 4 | 24 | 104.33 ms | 11.00 | 2.24 | [92.00, 120.00] |
| 3 to 4 | 24 | 103.67 ms | 10.81 | 2.21 | [92.00, 120.00] |
| 4 to 4 | 24 | 109.67 ms | 11.31 | 2.31 | [92.00, 120.00] |
| 5 to 4 | 24 | 108.00 ms | 11.00 | 2.25 | [92.00, 120.00] |
| 6 to 4 | 24 | 109.50 ms | 10.86 | 2.22 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 1.87 µV | 2.35 | 0.48 | [-2.47, 6.92] |
| 2 to 4 | 24 | 2.37 µV | 2.22 | 0.45 | [-0.87, 7.56] |
| 3 to 4 | 24 | 2.25 µV | 2.25 | 0.46 | [-1.32, 7.39] |
| 4 to 4 | 24 | 1.78 µV | 2.33 | 0.48 | [-3.85, 6.93] |
| 5 to 4 | 24 | 1.76 µV | 2.43 | 0.50 | [-2.55, 6.01] |
| 6 to 4 | 24 | 2.65 µV | 2.61 | 0.53 | [-3.00, 7.45] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 490.33 ms | 31.32 | 6.39 | [444.00, 540.00] |
| 2 to 4 | 24 | 494.50 ms | 31.82 | 6.50 | [436.00, 540.00] |
| 3 to 4 | 24 | 496.83 ms | 34.87 | 7.12 | [436.00, 540.00] |
| 4 to 4 | 24 | 474.17 ms | 29.44 | 6.01 | [436.00, 524.00] |
| 5 to 4 | 24 | 494.00 ms | 33.07 | 6.75 | [440.00, 540.00] |
| 6 to 4 | 24 | 485.00 ms | 35.80 | 7.31 | [436.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 4 | 24 | 4.76 µV | 3.54 | 0.72 | [-0.58, 11.88] |
| 2 to 4 | 24 | 5.52 µV | 4.91 | 1.00 | [-4.11, 17.43] |
| 3 to 4 | 24 | 4.33 µV | 4.75 | 0.97 | [-5.10, 13.58] |
| 4 to 4 | 24 | 1.51 µV | 4.01 | 0.82 | [-9.95, 8.96] |
| 5 to 4 | 24 | 5.14 µV | 3.98 | 0.81 | [-3.32, 11.69] |
| 6 to 4 | 24 | 4.61 µV | 3.83 | 0.78 | [-3.09, 13.11] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 999.70, BIC = 1026.43
- **2 to 4 vs 1 to 4**: *β* = -1.19, *SE* = 1.927, *z* = -0.618, *p* = 0.537
- **3 to 4 vs 1 to 4**: *β* = -0.59, *SE* = 1.937, *z* = -0.307, *p* = 0.759
- **4 to 4 vs 1 to 4**: *β* = 2.29, *SE* = 1.926, *z* = 1.192, *p* = 0.233
- **5 to 4 vs 1 to 4**: *β* = 1.60, *SE* = 1.924, *z* = 0.833, *p* = 0.405
- **6 to 4 vs 1 to 4**: *β* = 2.73, *SE* = 1.922, *z* = 1.422, *p* = 0.155
- **SNR**: *β* = 0.46, *SE* = 0.484, *z* = 0.940, *p* = 0.347

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 1.19 | 1.93 | 0.62 | 0.537 | 0.990 | n.s. |
| 1 to 4 - 3 to 4 | 0.60 | 1.94 | 0.31 | 0.759 | 0.994 | n.s. |
| 1 to 4 - 4 to 4 | -2.30 | 1.93 | -1.19 | 0.233 | 0.908 | n.s. |
| 1 to 4 - 5 to 4 | -1.60 | 1.92 | -0.83 | 0.405 | 0.974 | n.s. |
| 1 to 4 - 6 to 4 | -2.73 | 1.92 | -1.42 | 0.155 | 0.824 | n.s. |
| 2 to 4 - 3 to 4 | -0.59 | 1.92 | -0.31 | 0.757 | 0.994 | n.s. |
| 2 to 4 - 4 to 4 | -3.49 | 1.92 | -1.81 | 0.070 | 0.636 | n.s. |
| 2 to 4 - 5 to 4 | -2.79 | 1.92 | -1.45 | 0.146 | 0.824 | n.s. |
| 2 to 4 - 6 to 4 | -3.92 | 1.92 | -2.04 | 0.041 | 0.469 | n.s. |
| 3 to 4 - 4 to 4 | -2.89 | 1.92 | -1.50 | 0.133 | 0.820 | n.s. |
| 3 to 4 - 5 to 4 | -2.20 | 1.93 | -1.14 | 0.254 | 0.908 | n.s. |
| 3 to 4 - 6 to 4 | -3.33 | 1.93 | -1.72 | 0.085 | 0.683 | n.s. |
| 4 to 4 - 5 to 4 | 0.69 | 1.92 | 0.36 | 0.718 | 0.994 | n.s. |
| 4 to 4 - 6 to 4 | -0.44 | 1.92 | -0.23 | 0.820 | 0.994 | n.s. |
| 5 to 4 - 6 to 4 | -1.13 | 1.92 | -0.59 | 0.556 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.41, *p* = 0.226, η²_G = 0.036
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.68 | 23 | = 0.690 | 0.16 [-0.28, 0.56] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 0.39 | 23 | = 0.815 | 0.10 [-0.34, 0.50] | negligible | n.s. |
| 1 to 4 vs 4 to 4 | -0.97 | 23 | = 0.641 | -0.27 [-0.62, 0.23] | small | n.s. |
| 1 to 4 vs 5 to 4 | -0.77 | 23 | = 0.690 | -0.18 [-0.58, 0.27] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -2.14 | 23 | = 0.321 | -0.32 [-0.88, 0.00] | small | n.s. |
| 2 to 4 vs 3 to 4 | -0.24 | 23 | = 0.815 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | -1.70 | 23 | = 0.403 | -0.45 [-0.78, 0.09] | small | n.s. |
| 2 to 4 vs 5 to 4 | -1.50 | 23 | = 0.429 | -0.36 [-0.74, 0.13] | small | n.s. |
| 2 to 4 vs 6 to 4 | -2.30 | 23 | = 0.321 | -0.51 [-0.92, -0.03] | medium | n.s. |
| 3 to 4 vs 4 to 4 | -1.32 | 23 | = 0.429 | -0.39 [-0.70, 0.16] | small | n.s. |
| 3 to 4 vs 5 to 4 | -1.32 | 23 | = 0.429 | -0.30 [-0.70, 0.16] | small | n.s. |
| 3 to 4 vs 6 to 4 | -1.68 | 23 | = 0.403 | -0.45 [-0.78, 0.09] | small | n.s. |
| 4 to 4 vs 5 to 4 | 0.32 | 23 | = 0.815 | 0.09 [-0.36, 0.49] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | -0.25 | 23 | = 0.815 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.68 | 23 | = 0.690 | -0.15 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 625.33, BIC = 652.06
- **2 to 4 vs 1 to 4**: *β* = -0.96, *SE* = 0.551, *z* = -1.753, *p* = 0.080
- **3 to 4 vs 1 to 4**: *β* = -0.72, *SE* = 0.553, *z* = -1.309, *p* = 0.191
- **4 to 4 vs 1 to 4**: *β* = -0.52, *SE* = 0.550, *z* = -0.946, *p* = 0.344
- **5 to 4 vs 1 to 4**: *β* = -0.65, *SE* = 0.550, *z* = -1.178, *p* = 0.239
- **6 to 4 vs 1 to 4**: *β* = -0.99, *SE* = 0.549, *z* = -1.804, *p* = 0.071
- **SNR**: *β* = -0.67, *SE* = 0.134, *z* = -4.997, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 0.97 | 0.55 | 1.75 | 0.080 | 0.687 | n.s. |
| 1 to 4 - 3 to 4 | 0.72 | 0.55 | 1.31 | 0.191 | 0.936 | n.s. |
| 1 to 4 - 4 to 4 | 0.52 | 0.55 | 0.95 | 0.344 | 0.990 | n.s. |
| 1 to 4 - 5 to 4 | 0.65 | 0.55 | 1.18 | 0.239 | 0.962 | n.s. |
| 1 to 4 - 6 to 4 | 0.99 | 0.55 | 1.80 | 0.071 | 0.670 | n.s. |
| 2 to 4 - 3 to 4 | -0.24 | 0.55 | -0.44 | 0.662 | 0.998 | n.s. |
| 2 to 4 - 4 to 4 | -0.44 | 0.55 | -0.81 | 0.418 | 0.993 | n.s. |
| 2 to 4 - 5 to 4 | -0.32 | 0.55 | -0.58 | 0.563 | 0.998 | n.s. |
| 2 to 4 - 6 to 4 | 0.03 | 0.55 | 0.05 | 0.962 | 0.998 | n.s. |
| 3 to 4 - 4 to 4 | -0.20 | 0.55 | -0.37 | 0.711 | 0.998 | n.s. |
| 3 to 4 - 5 to 4 | -0.08 | 0.55 | -0.14 | 0.889 | 0.998 | n.s. |
| 3 to 4 - 6 to 4 | 0.27 | 0.55 | 0.48 | 0.628 | 0.998 | n.s. |
| 4 to 4 - 5 to 4 | 0.13 | 0.55 | 0.23 | 0.817 | 0.998 | n.s. |
| 4 to 4 - 6 to 4 | 0.47 | 0.55 | 0.86 | 0.391 | 0.993 | n.s. |
| 5 to 4 - 6 to 4 | 0.34 | 0.55 | 0.63 | 0.532 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.55, *p* = 0.735, η²_G = 0.017
- Greenhouse-Geisser corrected: *p* = 0.684 (ε = 0.742)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 1.20 | 23 | = 0.839 | 0.35 [-0.18, 0.67] | small | n.s. |
| 1 to 4 vs 3 to 4 | 0.59 | 23 | = 0.839 | 0.19 [-0.30, 0.54] | negligible | n.s. |
| 1 to 4 vs 4 to 4 | 0.78 | 23 | = 0.839 | 0.17 [-0.27, 0.58] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | 0.67 | 23 | = 0.839 | 0.20 [-0.29, 0.56] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 1.44 | 23 | = 0.839 | 0.42 [-0.14, 0.73] | small | n.s. |
| 2 to 4 vs 3 to 4 | -0.73 | 23 | = 0.839 | -0.18 [-0.57, 0.28] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | -0.71 | 23 | = 0.839 | -0.21 [-0.57, 0.28] | small | n.s. |
| 2 to 4 vs 5 to 4 | -0.33 | 23 | = 0.906 | -0.10 [-0.49, 0.36] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 0.24 | 23 | = 0.906 | 0.06 [-0.37, 0.47] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | -0.10 | 23 | = 0.918 | -0.02 [-0.44, 0.40] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | 0.20 | 23 | = 0.906 | 0.05 [-0.38, 0.46] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 1.08 | 23 | = 0.839 | 0.25 [-0.21, 0.65] | small | n.s. |
| 4 to 4 vs 5 to 4 | 0.23 | 23 | = 0.906 | 0.07 [-0.38, 0.47] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | 0.94 | 23 | = 0.839 | 0.27 [-0.23, 0.62] | small | n.s. |
| 5 to 4 vs 6 to 4 | 0.65 | 23 | = 0.839 | 0.15 [-0.29, 0.56] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1203.71, BIC = 1230.44
- **2 to 4 vs 1 to 4**: *β* = -1.16, *SE* = 3.620, *z* = -0.319, *p* = 0.750
- **3 to 4 vs 1 to 4**: *β* = -7.90, *SE* = 3.636, *z* = -2.172, *p* = 0.030
- **4 to 4 vs 1 to 4**: *β* = -2.15, *SE* = 3.620, *z* = -0.595, *p* = 0.552
- **5 to 4 vs 1 to 4**: *β* = 0.69, *SE* = 3.621, *z* = 0.192, *p* = 0.848
- **6 to 4 vs 1 to 4**: *β* = -0.19, *SE* = 3.620, *z* = -0.053, *p* = 0.958
- **SNR**: *β* = 0.11, *SE* = 0.388, *z* = 0.295, *p* = 0.768

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | 1.15 | 3.62 | 0.32 | 0.750 | 1.000 | n.s. |
| 1 to 4 - 3 to 4 | 7.90 | 3.64 | 2.17 | 0.030 | 0.346 | n.s. |
| 1 to 4 - 4 to 4 | 2.15 | 3.62 | 0.60 | 0.552 | 0.999 | n.s. |
| 1 to 4 - 5 to 4 | -0.69 | 3.62 | -0.19 | 0.848 | 1.000 | n.s. |
| 1 to 4 - 6 to 4 | 0.19 | 3.62 | 0.05 | 0.958 | 1.000 | n.s. |
| 2 to 4 - 3 to 4 | 6.74 | 3.63 | 1.86 | 0.063 | 0.544 | n.s. |
| 2 to 4 - 4 to 4 | 1.00 | 3.62 | 0.28 | 0.783 | 1.000 | n.s. |
| 2 to 4 - 5 to 4 | -1.85 | 3.62 | -0.51 | 0.609 | 0.999 | n.s. |
| 2 to 4 - 6 to 4 | -0.96 | 3.62 | -0.27 | 0.790 | 1.000 | n.s. |
| 3 to 4 - 4 to 4 | -5.74 | 3.63 | -1.58 | 0.114 | 0.735 | n.s. |
| 3 to 4 - 5 to 4 | -8.59 | 3.63 | -2.37 | 0.018 | 0.237 | n.s. |
| 3 to 4 - 6 to 4 | -7.71 | 3.64 | -2.11 | 0.034 | 0.366 | n.s. |
| 4 to 4 - 5 to 4 | -2.85 | 3.62 | -0.79 | 0.431 | 0.996 | n.s. |
| 4 to 4 - 6 to 4 | -1.96 | 3.62 | -0.54 | 0.588 | 0.999 | n.s. |
| 5 to 4 - 6 to 4 | 0.89 | 3.62 | 0.24 | 0.807 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.49, *p* = 0.199, η²_G = 0.025
- Greenhouse-Geisser corrected: *p* = 0.216 (ε = 0.739)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | 0.32 | 23 | = 0.915 | 0.07 [-0.36, 0.49] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 1.96 | 23 | = 0.233 | 0.46 [-0.04, 0.84] | small | n.s. |
| 1 to 4 vs 4 to 4 | 0.72 | 23 | = 0.915 | 0.12 [-0.28, 0.57] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | -0.19 | 23 | = 0.915 | -0.04 [-0.46, 0.38] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.05 | 23 | = 0.961 | 0.01 [-0.41, 0.43] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 2.04 | 23 | = 0.233 | 0.39 [-0.02, 0.86] | small | n.s. |
| 2 to 4 vs 4 to 4 | 0.24 | 23 | = 0.915 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.42 | 23 | = 0.915 | -0.10 [-0.51, 0.34] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.27 | 23 | = 0.915 | -0.05 [-0.48, 0.37] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | -1.30 | 23 | = 0.615 | -0.31 [-0.70, 0.16] | small | n.s. |
| 3 to 4 vs 5 to 4 | -2.47 | 23 | = 0.233 | -0.46 [-0.95, -0.06] | small | n.s. |
| 3 to 4 vs 6 to 4 | -2.07 | 23 | = 0.233 | -0.41 [-0.86, 0.02] | small | n.s. |
| 4 to 4 vs 5 to 4 | -0.68 | 23 | = 0.915 | -0.14 [-0.56, 0.29] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | -0.83 | 23 | = 0.915 | -0.10 [-0.59, 0.26] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | 0.25 | 23 | = 0.915 | 0.04 [-0.37, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 644.76, BIC = 671.49
- **2 to 4 vs 1 to 4**: *β* = 0.28, *SE* = 0.522, *z* = 0.540, *p* = 0.589
- **3 to 4 vs 1 to 4**: *β* = 0.34, *SE* = 0.525, *z* = 0.655, *p* = 0.513
- **4 to 4 vs 1 to 4**: *β* = 0.82, *SE* = 0.522, *z* = 1.563, *p* = 0.118
- **5 to 4 vs 1 to 4**: *β* = 0.44, *SE* = 0.522, *z* = 0.851, *p* = 0.395
- **6 to 4 vs 1 to 4**: *β* = 0.69, *SE* = 0.522, *z* = 1.319, *p* = 0.187
- **SNR**: *β* = -0.41, *SE* = 0.056, *z* = -7.353, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.28 | 0.52 | -0.54 | 0.589 | 0.997 | n.s. |
| 1 to 4 - 3 to 4 | -0.34 | 0.52 | -0.65 | 0.513 | 0.997 | n.s. |
| 1 to 4 - 4 to 4 | -0.82 | 0.52 | -1.56 | 0.118 | 0.848 | n.s. |
| 1 to 4 - 5 to 4 | -0.44 | 0.52 | -0.85 | 0.395 | 0.996 | n.s. |
| 1 to 4 - 6 to 4 | -0.69 | 0.52 | -1.32 | 0.187 | 0.945 | n.s. |
| 2 to 4 - 3 to 4 | -0.06 | 0.52 | -0.12 | 0.907 | 0.997 | n.s. |
| 2 to 4 - 4 to 4 | -0.53 | 0.52 | -1.02 | 0.306 | 0.991 | n.s. |
| 2 to 4 - 5 to 4 | -0.16 | 0.52 | -0.31 | 0.756 | 0.997 | n.s. |
| 2 to 4 - 6 to 4 | -0.41 | 0.52 | -0.78 | 0.436 | 0.997 | n.s. |
| 3 to 4 - 4 to 4 | -0.47 | 0.52 | -0.90 | 0.367 | 0.996 | n.s. |
| 3 to 4 - 5 to 4 | -0.10 | 0.52 | -0.19 | 0.847 | 0.997 | n.s. |
| 3 to 4 - 6 to 4 | -0.35 | 0.53 | -0.66 | 0.511 | 0.997 | n.s. |
| 4 to 4 - 5 to 4 | 0.37 | 0.52 | 0.71 | 0.477 | 0.997 | n.s. |
| 4 to 4 - 6 to 4 | 0.13 | 0.52 | 0.24 | 0.808 | 0.997 | n.s. |
| 5 to 4 - 6 to 4 | -0.24 | 0.52 | -0.47 | 0.640 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.47, *p* = 0.795, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.55 | 23 | = 0.916 | -0.10 [-0.54, 0.31] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | -1.29 | 23 | = 0.916 | -0.25 [-0.69, 0.17] | small | n.s. |
| 1 to 4 vs 4 to 4 | -1.77 | 23 | = 0.916 | -0.26 [-0.80, 0.08] | small | n.s. |
| 1 to 4 vs 5 to 4 | -1.12 | 23 | = 0.916 | -0.17 [-0.66, 0.20] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -1.02 | 23 | = 0.916 | -0.19 [-0.64, 0.22] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | -0.54 | 23 | = 0.916 | -0.14 [-0.53, 0.31] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | -0.83 | 23 | = 0.916 | -0.16 [-0.59, 0.26] | negligible | n.s. |
| 2 to 4 vs 5 to 4 | -0.35 | 23 | = 0.916 | -0.07 [-0.49, 0.35] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | -0.32 | 23 | = 0.916 | -0.09 [-0.49, 0.36] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | -0.23 | 23 | = 0.916 | -0.05 [-0.47, 0.38] | negligible | n.s. |
| 3 to 4 vs 5 to 4 | 0.29 | 23 | = 0.916 | 0.06 [-0.36, 0.48] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 0.19 | 23 | = 0.916 | 0.04 [-0.38, 0.46] | negligible | n.s. |
| 4 to 4 vs 5 to 4 | 0.46 | 23 | = 0.916 | 0.10 [-0.33, 0.52] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | 0.43 | 23 | = 0.916 | 0.08 [-0.33, 0.51] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.08 | 23 | = 0.934 | -0.02 [-0.44, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1068.36, BIC = 1095.09
- **2 to 4 vs 1 to 4**: *β* = 4.29, *SE* = 2.347, *z* = 1.828, *p* = 0.068
- **3 to 4 vs 1 to 4**: *β* = 3.71, *SE* = 2.353, *z* = 1.575, *p* = 0.115
- **4 to 4 vs 1 to 4**: *β* = 9.52, *SE* = 2.344, *z* = 4.060, *p* < .001
- **5 to 4 vs 1 to 4**: *β* = 7.97, *SE* = 2.348, *z* = 3.395, *p* = 0.001
- **6 to 4 vs 1 to 4**: *β* = 9.17, *SE* = 2.350, *z* = 3.903, *p* < .001
- **SNR**: *β* = 0.52, *SE* = 0.529, *z* = 0.973, *p* = 0.331

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -4.29 | 2.35 | -1.83 | 0.068 | 0.429 | n.s. |
| 1 to 4 - 3 to 4 | -3.71 | 2.35 | -1.58 | 0.115 | 0.520 | n.s. |
| 1 to 4 - 4 to 4 | -9.52 | 2.34 | -4.06 | < .001 | < .001 | *** |
| 1 to 4 - 5 to 4 | -7.97 | 2.35 | -3.39 | < .001 | 0.009 | ** |
| 1 to 4 - 6 to 4 | -9.17 | 2.35 | -3.90 | < .001 | 0.001 | ** |
| 2 to 4 - 3 to 4 | 0.58 | 2.35 | 0.25 | 0.803 | 0.961 | n.s. |
| 2 to 4 - 4 to 4 | -5.23 | 2.35 | -2.23 | 0.026 | 0.231 | n.s. |
| 2 to 4 - 5 to 4 | -3.68 | 2.34 | -1.57 | 0.116 | 0.520 | n.s. |
| 2 to 4 - 6 to 4 | -4.88 | 2.36 | -2.07 | 0.039 | 0.300 | n.s. |
| 3 to 4 - 4 to 4 | -5.81 | 2.35 | -2.47 | 0.014 | 0.150 | n.s. |
| 3 to 4 - 5 to 4 | -4.26 | 2.34 | -1.82 | 0.069 | 0.429 | n.s. |
| 3 to 4 - 6 to 4 | -5.46 | 2.37 | -2.30 | 0.021 | 0.212 | n.s. |
| 4 to 4 - 5 to 4 | 1.55 | 2.35 | 0.66 | 0.510 | 0.942 | n.s. |
| 4 to 4 - 6 to 4 | 0.35 | 2.35 | 0.15 | 0.883 | 0.961 | n.s. |
| 5 to 4 - 6 to 4 | -1.20 | 2.36 | -0.51 | 0.612 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 5.01, *p* < .001, η²_G = 0.097
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -2.12 | 23 | = 0.102 | -0.40 [-0.87, 0.01] | small | n.s. |
| 1 to 4 vs 3 to 4 | -2.03 | 23 | = 0.102 | -0.34 [-0.85, 0.03] | small | n.s. |
| 1 to 4 vs 4 to 4 | -4.10 | 23 | = 0.004 | -0.90 [-1.33, -0.35] | large | ** |
| 1 to 4 vs 5 to 4 | -3.65 | 23 | = 0.007 | -0.76 [-1.22, -0.27] | medium | ** |
| 1 to 4 vs 6 to 4 | -4.03 | 23 | = 0.004 | -0.91 [-1.31, -0.33] | large | ** |
| 2 to 4 vs 3 to 4 | 0.31 | 23 | = 0.812 | 0.06 [-0.36, 0.49] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | -2.18 | 23 | = 0.102 | -0.48 [-0.89, -0.00] | small | n.s. |
| 2 to 4 vs 5 to 4 | -1.73 | 23 | = 0.133 | -0.33 [-0.79, 0.08] | small | n.s. |
| 2 to 4 vs 6 to 4 | -2.16 | 23 | = 0.102 | -0.47 [-0.88, 0.00] | small | n.s. |
| 3 to 4 vs 4 to 4 | -2.06 | 23 | = 0.102 | -0.54 [-0.86, 0.02] | medium | n.s. |
| 3 to 4 vs 5 to 4 | -1.80 | 23 | = 0.127 | -0.40 [-0.80, 0.07] | small | n.s. |
| 3 to 4 vs 6 to 4 | -1.88 | 23 | = 0.121 | -0.54 [-0.82, 0.05] | medium | n.s. |
| 4 to 4 vs 5 to 4 | 0.65 | 23 | = 0.654 | 0.15 [-0.29, 0.56] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | 0.07 | 23 | = 0.946 | 0.02 [-0.41, 0.44] | negligible | n.s. |
| 5 to 4 vs 6 to 4 | -0.58 | 23 | = 0.658 | -0.14 [-0.54, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 607.80, BIC = 634.53
- **2 to 4 vs 1 to 4**: *β* = 0.62, *SE* = 0.476, *z* = 1.300, *p* = 0.194
- **3 to 4 vs 1 to 4**: *β* = 0.57, *SE* = 0.477, *z* = 1.205, *p* = 0.228
- **4 to 4 vs 1 to 4**: *β* = -0.07, *SE* = 0.475, *z* = -0.147, *p* = 0.883
- **5 to 4 vs 1 to 4**: *β* = 0.03, *SE* = 0.476, *z* = 0.056, *p* = 0.956
- **6 to 4 vs 1 to 4**: *β* = 0.63, *SE* = 0.476, *z* = 1.317, *p* = 0.188
- **SNR**: *β* = 0.49, *SE* = 0.109, *z* = 4.471, *p* < .001

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.62 | 0.48 | -1.30 | 0.194 | 0.920 | n.s. |
| 1 to 4 - 3 to 4 | -0.57 | 0.48 | -1.20 | 0.228 | 0.920 | n.s. |
| 1 to 4 - 4 to 4 | 0.07 | 0.47 | 0.15 | 0.883 | 1.000 | n.s. |
| 1 to 4 - 5 to 4 | -0.03 | 0.48 | -0.06 | 0.956 | 1.000 | n.s. |
| 1 to 4 - 6 to 4 | -0.63 | 0.48 | -1.32 | 0.188 | 0.920 | n.s. |
| 2 to 4 - 3 to 4 | 0.04 | 0.48 | 0.09 | 0.927 | 1.000 | n.s. |
| 2 to 4 - 4 to 4 | 0.69 | 0.48 | 1.45 | 0.148 | 0.902 | n.s. |
| 2 to 4 - 5 to 4 | 0.59 | 0.47 | 1.25 | 0.213 | 0.920 | n.s. |
| 2 to 4 - 6 to 4 | -0.01 | 0.48 | -0.02 | 0.985 | 1.000 | n.s. |
| 3 to 4 - 4 to 4 | 0.64 | 0.48 | 1.35 | 0.176 | 0.920 | n.s. |
| 3 to 4 - 5 to 4 | 0.55 | 0.48 | 1.15 | 0.249 | 0.920 | n.s. |
| 3 to 4 - 6 to 4 | -0.05 | 0.48 | -0.11 | 0.913 | 1.000 | n.s. |
| 4 to 4 - 5 to 4 | -0.10 | 0.48 | -0.20 | 0.839 | 1.000 | n.s. |
| 4 to 4 - 6 to 4 | -0.70 | 0.48 | -1.46 | 0.143 | 0.902 | n.s. |
| 5 to 4 - 6 to 4 | -0.60 | 0.48 | -1.25 | 0.210 | 0.920 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.01, *p* = 0.413, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.28 | 23 | = 0.660 | -0.22 [-0.69, 0.17] | small | n.s. |
| 1 to 4 vs 3 to 4 | -0.61 | 23 | = 0.822 | -0.17 [-0.55, 0.30] | negligible | n.s. |
| 1 to 4 vs 4 to 4 | 0.20 | 23 | = 0.903 | 0.04 [-0.38, 0.46] | negligible | n.s. |
| 1 to 4 vs 5 to 4 | 0.21 | 23 | = 0.903 | 0.04 [-0.38, 0.47] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | -1.42 | 23 | = 0.660 | -0.32 [-0.72, 0.14] | small | n.s. |
| 2 to 4 vs 3 to 4 | 0.24 | 23 | = 0.903 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | 1.15 | 23 | = 0.660 | 0.26 [-0.19, 0.66] | small | n.s. |
| 2 to 4 vs 5 to 4 | 1.26 | 23 | = 0.660 | 0.26 [-0.17, 0.69] | small | n.s. |
| 2 to 4 vs 6 to 4 | -0.52 | 23 | = 0.829 | -0.12 [-0.53, 0.32] | negligible | n.s. |
| 3 to 4 vs 4 to 4 | 0.79 | 23 | = 0.731 | 0.20 [-0.26, 0.59] | small | n.s. |
| 3 to 4 vs 5 to 4 | 0.94 | 23 | = 0.731 | 0.21 [-0.23, 0.62] | small | n.s. |
| 3 to 4 vs 6 to 4 | -0.79 | 23 | = 0.731 | -0.16 [-0.59, 0.26] | negligible | n.s. |
| 4 to 4 vs 5 to 4 | 0.03 | 23 | = 0.975 | 0.01 [-0.42, 0.43] | negligible | n.s. |
| 4 to 4 vs 6 to 4 | -1.82 | 23 | = 0.615 | -0.35 [-0.81, 0.07] | small | n.s. |
| 5 to 4 vs 6 to 4 | -1.89 | 23 | = 0.615 | -0.35 [-0.82, 0.05] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1422.35, BIC = 1449.08
- **2 to 4 vs 1 to 4**: *β* = 4.10, *SE* = 8.760, *z* = 0.469, *p* = 0.639
- **3 to 4 vs 1 to 4**: *β* = 6.40, *SE* = 8.776, *z* = 0.730, *p* = 0.466
- **4 to 4 vs 1 to 4**: *β* = -16.05, *SE* = 8.787, *z* = -1.827, *p* = 0.068
- **5 to 4 vs 1 to 4**: *β* = 3.65, *SE* = 8.749, *z* = 0.417, *p* = 0.677
- **6 to 4 vs 1 to 4**: *β* = -5.29, *SE* = 8.754, *z* = -0.604, *p* = 0.546
- **SNR**: *β* = 0.12, *SE* = 0.833, *z* = 0.138, *p* = 0.891

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -4.10 | 8.76 | -0.47 | 0.639 | 0.994 | n.s. |
| 1 to 4 - 3 to 4 | -6.40 | 8.78 | -0.73 | 0.466 | 0.988 | n.s. |
| 1 to 4 - 4 to 4 | 16.05 | 8.79 | 1.83 | 0.068 | 0.569 | n.s. |
| 1 to 4 - 5 to 4 | -3.65 | 8.75 | -0.42 | 0.677 | 0.994 | n.s. |
| 1 to 4 - 6 to 4 | 5.29 | 8.75 | 0.60 | 0.546 | 0.991 | n.s. |
| 2 to 4 - 3 to 4 | -2.30 | 8.75 | -0.26 | 0.793 | 0.994 | n.s. |
| 2 to 4 - 4 to 4 | 20.16 | 8.84 | 2.28 | 0.023 | 0.274 | n.s. |
| 2 to 4 - 5 to 4 | 0.46 | 8.75 | 0.05 | 0.958 | 0.994 | n.s. |
| 2 to 4 - 6 to 4 | 9.39 | 8.78 | 1.07 | 0.285 | 0.951 | n.s. |
| 3 to 4 - 4 to 4 | 22.46 | 8.88 | 2.53 | 0.011 | 0.159 | n.s. |
| 3 to 4 - 5 to 4 | 2.76 | 8.77 | 0.31 | 0.753 | 0.994 | n.s. |
| 3 to 4 - 6 to 4 | 11.69 | 8.81 | 1.33 | 0.184 | 0.894 | n.s. |
| 4 to 4 - 5 to 4 | -19.70 | 8.80 | -2.24 | 0.025 | 0.282 | n.s. |
| 4 to 4 - 6 to 4 | -10.77 | 8.76 | -1.23 | 0.219 | 0.916 | n.s. |
| 5 to 4 - 6 to 4 | 8.93 | 8.76 | 1.02 | 0.308 | 0.951 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.77, *p* = 0.124, η²_G = 0.054
- Greenhouse-Geisser corrected: *p* = 0.154 (ε = 0.670)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -0.56 | 23 | = 0.796 | -0.13 [-0.54, 0.31] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | -0.67 | 23 | = 0.796 | -0.20 [-0.56, 0.29] | negligible | n.s. |
| 1 to 4 vs 4 to 4 | 1.65 | 23 | = 0.336 | 0.53 [-0.10, 0.77] | medium | n.s. |
| 1 to 4 vs 5 to 4 | -0.35 | 23 | = 0.839 | -0.11 [-0.49, 0.35] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.58 | 23 | = 0.796 | 0.16 [-0.30, 0.54] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | -0.22 | 23 | = 0.884 | -0.07 [-0.47, 0.38] | negligible | n.s. |
| 2 to 4 vs 4 to 4 | 2.63 | 23 | = 0.155 | 0.66 [0.08, 0.99] | medium | n.s. |
| 2 to 4 vs 5 to 4 | 0.05 | 23 | = 0.959 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 1.84 | 23 | = 0.297 | 0.28 [-0.06, 0.81] | small | n.s. |
| 3 to 4 vs 4 to 4 | 2.39 | 23 | = 0.155 | 0.70 [0.04, 0.93] | medium | n.s. |
| 3 to 4 vs 5 to 4 | 0.40 | 23 | = 0.839 | 0.08 [-0.34, 0.50] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | 1.08 | 23 | = 0.620 | 0.33 [-0.21, 0.65] | small | n.s. |
| 4 to 4 vs 5 to 4 | -2.30 | 23 | = 0.155 | -0.63 [-0.91, -0.02] | medium | n.s. |
| 4 to 4 vs 6 to 4 | -1.53 | 23 | = 0.350 | -0.33 [-0.74, 0.12] | small | n.s. |
| 5 to 4 vs 6 to 4 | 0.95 | 23 | = 0.664 | 0.26 [-0.23, 0.62] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 749.79, BIC = 776.52
- **2 to 4 vs 1 to 4**: *β* = 0.69, *SE* = 0.730, *z* = 0.948, *p* = 0.343
- **3 to 4 vs 1 to 4**: *β* = -0.54, *SE* = 0.732, *z* = -0.739, *p* = 0.460
- **4 to 4 vs 1 to 4**: *β* = -3.13, *SE* = 0.733, *z* = -4.268, *p* < .001
- **5 to 4 vs 1 to 4**: *β* = 0.36, *SE* = 0.729, *z* = 0.490, *p* = 0.624
- **6 to 4 vs 1 to 4**: *β* = -0.10, *SE* = 0.730, *z* = -0.142, *p* = 0.887
- **SNR**: *β* = 0.13, *SE* = 0.075, *z* = 1.697, *p* = 0.090

_Reference condition: **1 to 4** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 4 - 2 to 4 | -0.69 | 0.73 | -0.95 | 0.343 | 0.947 | n.s. |
| 1 to 4 - 3 to 4 | 0.54 | 0.73 | 0.74 | 0.460 | 0.975 | n.s. |
| 1 to 4 - 4 to 4 | 3.13 | 0.73 | 4.27 | < .001 | < .001 | *** |
| 1 to 4 - 5 to 4 | -0.36 | 0.73 | -0.49 | 0.624 | 0.977 | n.s. |
| 1 to 4 - 6 to 4 | 0.10 | 0.73 | 0.14 | 0.887 | 0.977 | n.s. |
| 2 to 4 - 3 to 4 | 1.23 | 0.73 | 1.69 | 0.091 | 0.615 | n.s. |
| 2 to 4 - 4 to 4 | 3.82 | 0.74 | 5.18 | < .001 | < .001 | *** |
| 2 to 4 - 5 to 4 | 0.33 | 0.73 | 0.46 | 0.646 | 0.977 | n.s. |
| 2 to 4 - 6 to 4 | 0.80 | 0.73 | 1.09 | 0.277 | 0.925 | n.s. |
| 3 to 4 - 4 to 4 | 2.59 | 0.74 | 3.49 | < .001 | 0.005 | ** |
| 3 to 4 - 5 to 4 | -0.90 | 0.73 | -1.23 | 0.219 | 0.892 | n.s. |
| 3 to 4 - 6 to 4 | -0.44 | 0.74 | -0.59 | 0.552 | 0.977 | n.s. |
| 4 to 4 - 5 to 4 | -3.49 | 0.73 | -4.75 | < .001 | < .001 | *** |
| 4 to 4 - 6 to 4 | -3.03 | 0.73 | -4.14 | < .001 | < .001 | *** |
| 5 to 4 - 6 to 4 | 0.46 | 0.73 | 0.63 | 0.528 | 0.977 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.31, *p* < .001, η²_G = 0.092
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 4 vs 2 to 4 | -1.08 | 23 | = 0.487 | -0.18 [-0.65, 0.21] | negligible | n.s. |
| 1 to 4 vs 3 to 4 | 0.62 | 23 | = 0.679 | 0.10 [-0.30, 0.55] | negligible | n.s. |
| 1 to 4 vs 4 to 4 | 4.51 | 23 | < .001 | 0.86 [0.42, 1.43] | large | *** |
| 1 to 4 vs 5 to 4 | -0.73 | 23 | = 0.641 | -0.10 [-0.57, 0.27] | negligible | n.s. |
| 1 to 4 vs 6 to 4 | 0.28 | 23 | = 0.780 | 0.04 [-0.36, 0.48] | negligible | n.s. |
| 2 to 4 vs 3 to 4 | 1.42 | 23 | = 0.425 | 0.25 [-0.14, 0.72] | small | n.s. |
| 2 to 4 vs 4 to 4 | 4.72 | 23 | < .001 | 0.90 [0.45, 1.47] | large | *** |
| 2 to 4 vs 5 to 4 | 0.48 | 23 | = 0.730 | 0.09 [-0.32, 0.52] | negligible | n.s. |
| 2 to 4 vs 6 to 4 | 1.08 | 23 | = 0.487 | 0.21 [-0.21, 0.65] | small | n.s. |
| 3 to 4 vs 4 to 4 | 2.99 | 23 | = 0.020 | 0.64 [0.15, 1.07] | medium | * |
| 3 to 4 vs 5 to 4 | -1.18 | 23 | = 0.487 | -0.19 [-0.67, 0.19] | negligible | n.s. |
| 3 to 4 vs 6 to 4 | -0.31 | 23 | = 0.780 | -0.06 [-0.49, 0.36] | negligible | n.s. |
| 4 to 4 vs 5 to 4 | -5.42 | 23 | < .001 | -0.91 [-1.64, -0.57] | large | *** |
| 4 to 4 vs 6 to 4 | -4.50 | 23 | < .001 | -0.79 [-1.42, -0.42] | medium | *** |
| 5 to 4 vs 6 to 4 | 0.76 | 23 | = 0.641 | 0.14 [-0.27, 0.58] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 4 showed smaller latency than 4 to 4 (*d* = -0.90)
  - 1 to 4 showed smaller latency than 5 to 4 (*d* = -0.76)
  - 1 to 4 showed smaller latency than 6 to 4 (*d* = -0.91)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - 1 to 4 showed greater amplitude than 4 to 4 (*d* = 0.86)
  - 2 to 4 showed greater amplitude than 4 to 4 (*d* = 0.90)
  - 3 to 4 showed greater amplitude than 4 to 4 (*d* = 0.64)
  - 4 to 4 showed smaller amplitude than 5 to 4 (*d* = -0.91)
  - 4 to 4 showed smaller amplitude than 6 to 4 (*d* = -0.79)

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
