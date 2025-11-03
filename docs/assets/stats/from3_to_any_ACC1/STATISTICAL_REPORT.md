# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:39:56

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
| 3 to 1 | 11 | 101.09 ms | 11.88 | 3.58 | [88.00, 116.00] |
| 3 to 2 | 10 | 106.40 ms | 9.83 | 3.11 | [92.00, 116.00] |
| 3 to 3 | 12 | 105.00 ms | 10.94 | 3.16 | [88.00, 116.00] |
| 3 to 4 | 9 | 102.67 ms | 14.14 | 4.71 | [88.00, 116.00] |
| 3 to 5 | 9 | 107.56 ms | 11.22 | 3.74 | [88.00, 116.00] |
| 3 to 6 | 11 | 101.09 ms | 13.40 | 4.04 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 11 | 2.40 µV | 1.30 | 0.39 | [1.06, 5.32] |
| 3 to 2 | 10 | 2.69 µV | 1.21 | 0.38 | [1.11, 4.23] |
| 3 to 3 | 12 | 2.32 µV | 0.86 | 0.25 | [0.99, 3.69] |
| 3 to 4 | 9 | 2.62 µV | 1.88 | 0.63 | [1.03, 6.90] |
| 3 to 5 | 9 | 3.84 µV | 2.24 | 0.75 | [1.21, 7.66] |
| 3 to 6 | 11 | 2.91 µV | 1.82 | 0.55 | [0.65, 6.17] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 183.78 ms | 15.49 | 3.65 | [156.00, 208.00] |
| 3 to 2 | 22 | 172.36 ms | 22.04 | 4.70 | [140.00, 208.00] |
| 3 to 3 | 22 | 167.82 ms | 16.54 | 3.53 | [140.00, 200.00] |
| 3 to 4 | 23 | 166.78 ms | 18.15 | 3.78 | [140.00, 204.00] |
| 3 to 5 | 22 | 166.55 ms | 22.17 | 4.73 | [140.00, 208.00] |
| 3 to 6 | 23 | 168.00 ms | 19.18 | 4.00 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | -5.14 µV | 2.62 | 0.62 | [-10.41, -1.40] |
| 3 to 2 | 22 | -6.15 µV | 2.54 | 0.54 | [-10.33, -1.67] |
| 3 to 3 | 22 | -5.19 µV | 2.03 | 0.43 | [-10.83, -1.55] |
| 3 to 4 | 23 | -5.92 µV | 2.07 | 0.43 | [-10.53, -2.95] |
| 3 to 5 | 22 | -5.92 µV | 2.63 | 0.56 | [-13.75, -1.70] |
| 3 to 6 | 23 | -7.08 µV | 2.77 | 0.58 | [-12.76, -3.05] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 108.22 ms | 8.51 | 2.01 | [92.00, 116.00] |
| 3 to 2 | 10 | 102.00 ms | 8.69 | 2.75 | [92.00, 116.00] |
| 3 to 3 | 13 | 107.69 ms | 9.16 | 2.54 | [92.00, 116.00] |
| 3 to 4 | 14 | 104.29 ms | 8.37 | 2.24 | [92.00, 116.00] |
| 3 to 5 | 11 | 105.45 ms | 8.63 | 2.60 | [92.00, 116.00] |
| 3 to 6 | 10 | 102.80 ms | 9.05 | 2.86 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 18 | 3.53 µV | 1.99 | 0.47 | [0.80, 9.14] |
| 3 to 2 | 10 | 2.63 µV | 1.90 | 0.60 | [0.60, 5.61] |
| 3 to 3 | 13 | 3.42 µV | 2.33 | 0.65 | [0.79, 8.96] |
| 3 to 4 | 14 | 3.36 µV | 2.00 | 0.54 | [1.27, 7.39] |
| 3 to 5 | 11 | 3.18 µV | 1.49 | 0.45 | [1.14, 5.64] |
| 3 to 6 | 10 | 3.90 µV | 2.28 | 0.72 | [0.83, 8.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 484.40 ms | 27.83 | 6.22 | [444.00, 540.00] |
| 3 to 2 | 18 | 490.00 ms | 32.12 | 7.57 | [432.00, 540.00] |
| 3 to 3 | 15 | 472.27 ms | 28.78 | 7.43 | [448.00, 532.00] |
| 3 to 4 | 16 | 496.25 ms | 41.22 | 10.31 | [428.00, 540.00] |
| 3 to 5 | 16 | 491.50 ms | 34.41 | 8.60 | [432.00, 540.00] |
| 3 to 6 | 19 | 486.95 ms | 36.56 | 8.39 | [428.00, 540.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 6.16 µV | 3.13 | 0.70 | [2.57, 16.27] |
| 3 to 2 | 18 | 6.73 µV | 4.05 | 0.96 | [2.10, 17.81] |
| 3 to 3 | 15 | 4.59 µV | 2.25 | 0.58 | [1.81, 9.60] |
| 3 to 4 | 16 | 7.01 µV | 3.08 | 0.77 | [2.36, 13.58] |
| 3 to 5 | 16 | 6.33 µV | 3.54 | 0.88 | [1.91, 16.52] |
| 3 to 6 | 19 | 5.01 µV | 2.27 | 0.52 | [1.70, 11.34] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 494.28, BIC = 513.42
- **3 to 2 vs 3 to 1**: *β* = 5.87, *SE* = 4.873, *z* = 1.204, *p* = 0.229
- **3 to 3 vs 3 to 1**: *β* = 4.45, *SE* = 4.629, *z* = 0.962, *p* = 0.336
- **3 to 4 vs 3 to 1**: *β* = 2.15, *SE* = 5.032, *z* = 0.427, *p* = 0.669
- **3 to 5 vs 3 to 1**: *β* = 6.99, *SE* = 5.049, *z* = 1.385, *p* = 0.166
- **3 to 6 vs 3 to 1**: *β* = 0.02, *SE* = 4.740, *z* = 0.005, *p* = 0.996
- **SNR**: *β* = -0.48, *SE* = 1.243, *z* = -0.390, *p* = 0.697

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -5.87 | 4.87 | -1.20 | 0.229 | 0.966 | n.s. |
| 3 to 1 - 3 to 3 | -4.45 | 4.63 | -0.96 | 0.336 | 0.989 | n.s. |
| 3 to 1 - 3 to 4 | -2.15 | 5.03 | -0.43 | 0.669 | 0.999 | n.s. |
| 3 to 1 - 3 to 5 | -6.99 | 5.05 | -1.38 | 0.166 | 0.935 | n.s. |
| 3 to 1 - 3 to 6 | -0.02 | 4.74 | -0.00 | 0.996 | 0.999 | n.s. |
| 3 to 2 - 3 to 3 | 1.42 | 4.74 | 0.30 | 0.765 | 0.999 | n.s. |
| 3 to 2 - 3 to 4 | 3.72 | 5.08 | 0.73 | 0.464 | 0.993 | n.s. |
| 3 to 2 - 3 to 5 | -1.12 | 5.12 | -0.22 | 0.827 | 0.999 | n.s. |
| 3 to 2 - 3 to 6 | 5.85 | 4.86 | 1.20 | 0.229 | 0.966 | n.s. |
| 3 to 3 - 3 to 4 | 2.30 | 4.81 | 0.48 | 0.633 | 0.999 | n.s. |
| 3 to 3 - 3 to 5 | -2.54 | 5.00 | -0.51 | 0.612 | 0.999 | n.s. |
| 3 to 3 - 3 to 6 | 4.43 | 4.62 | 0.96 | 0.337 | 0.989 | n.s. |
| 3 to 4 - 3 to 5 | -4.84 | 5.37 | -0.90 | 0.367 | 0.989 | n.s. |
| 3 to 4 - 3 to 6 | 2.13 | 4.98 | 0.43 | 0.669 | 0.999 | n.s. |
| 3 to 5 - 3 to 6 | 6.97 | 5.18 | 1.34 | 0.179 | 0.936 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 216.34, BIC = 235.49
- **3 to 2 vs 3 to 1**: *β* = 0.23, *SE* = 0.513, *z* = 0.451, *p* = 0.652
- **3 to 3 vs 3 to 1**: *β* = 0.02, *SE* = 0.477, *z* = 0.040, *p* = 0.968
- **3 to 4 vs 3 to 1**: *β* = 0.50, *SE* = 0.528, *z* = 0.939, *p* = 0.348
- **3 to 5 vs 3 to 1**: *β* = 1.02, *SE* = 0.529, *z* = 1.935, *p* = 0.053
- **3 to 6 vs 3 to 1**: *β* = 0.88, *SE* = 0.498, *z* = 1.760, *p* = 0.078
- **SNR**: *β* = 0.74, *SE* = 0.129, *z* = 5.750, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -0.23 | 0.51 | -0.45 | 0.652 | 0.991 | n.s. |
| 3 to 1 - 3 to 3 | -0.02 | 0.48 | -0.04 | 0.968 | 0.991 | n.s. |
| 3 to 1 - 3 to 4 | -0.50 | 0.53 | -0.94 | 0.348 | 0.973 | n.s. |
| 3 to 1 - 3 to 5 | -1.02 | 0.53 | -1.93 | 0.053 | 0.543 | n.s. |
| 3 to 1 - 3 to 6 | -0.88 | 0.50 | -1.76 | 0.078 | 0.625 | n.s. |
| 3 to 2 - 3 to 3 | 0.21 | 0.49 | 0.44 | 0.663 | 0.991 | n.s. |
| 3 to 2 - 3 to 4 | -0.26 | 0.52 | -0.51 | 0.611 | 0.991 | n.s. |
| 3 to 2 - 3 to 5 | -0.79 | 0.53 | -1.50 | 0.134 | 0.793 | n.s. |
| 3 to 2 - 3 to 6 | -0.64 | 0.50 | -1.30 | 0.194 | 0.885 | n.s. |
| 3 to 3 - 3 to 4 | -0.48 | 0.49 | -0.97 | 0.330 | 0.973 | n.s. |
| 3 to 3 - 3 to 5 | -1.00 | 0.51 | -1.95 | 0.051 | 0.543 | n.s. |
| 3 to 3 - 3 to 6 | -0.86 | 0.47 | -1.82 | 0.069 | 0.607 | n.s. |
| 3 to 4 - 3 to 5 | -0.53 | 0.55 | -0.96 | 0.339 | 0.973 | n.s. |
| 3 to 4 - 3 to 6 | -0.38 | 0.51 | -0.74 | 0.457 | 0.974 | n.s. |
| 3 to 5 - 3 to 6 | 0.15 | 0.54 | 0.27 | 0.785 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1116.23, BIC = 1142.03
- **3 to 2 vs 3 to 1**: *β* = -9.72, *SE* = 4.727, *z* = -2.057, *p* = 0.040
- **3 to 3 vs 3 to 1**: *β* = -14.19, *SE* = 4.620, *z* = -3.071, *p* = 0.002
- **3 to 4 vs 3 to 1**: *β* = -16.00, *SE* = 4.544, *z* = -3.521, *p* < .001
- **3 to 5 vs 3 to 1**: *β* = -15.51, *SE* = 4.709, *z* = -3.294, *p* = 0.001
- **3 to 6 vs 3 to 1**: *β* = -15.14, *SE* = 4.693, *z* = -3.226, *p* = 0.001
- **SNR**: *β* = 0.28, *SE* = 0.600, *z* = 0.464, *p* = 0.643

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 9.72 | 4.73 | 2.06 | 0.040 | 0.359 | n.s. |
| 3 to 1 - 3 to 3 | 14.19 | 4.62 | 3.07 | 0.002 | 0.025 | * |
| 3 to 1 - 3 to 4 | 16.00 | 4.54 | 3.52 | < .001 | 0.006 | ** |
| 3 to 1 - 3 to 5 | 15.51 | 4.71 | 3.29 | < .001 | 0.014 | * |
| 3 to 1 - 3 to 6 | 15.14 | 4.69 | 3.23 | 0.001 | 0.016 | * |
| 3 to 2 - 3 to 3 | 4.46 | 4.31 | 1.03 | 0.301 | 0.918 | n.s. |
| 3 to 2 - 3 to 4 | 6.28 | 4.24 | 1.48 | 0.139 | 0.776 | n.s. |
| 3 to 2 - 3 to 5 | 5.79 | 4.24 | 1.36 | 0.173 | 0.818 | n.s. |
| 3 to 2 - 3 to 6 | 5.41 | 4.21 | 1.28 | 0.199 | 0.830 | n.s. |
| 3 to 3 - 3 to 4 | 1.81 | 4.24 | 0.43 | 0.669 | 0.999 | n.s. |
| 3 to 3 - 3 to 5 | 1.33 | 4.30 | 0.31 | 0.758 | 0.999 | n.s. |
| 3 to 3 - 3 to 6 | 0.95 | 4.25 | 0.22 | 0.823 | 0.999 | n.s. |
| 3 to 4 - 3 to 5 | -0.49 | 4.24 | -0.12 | 0.908 | 0.999 | n.s. |
| 3 to 4 - 3 to 6 | -0.86 | 4.21 | -0.20 | 0.838 | 0.999 | n.s. |
| 3 to 5 - 3 to 6 | -0.37 | 4.21 | -0.09 | 0.929 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.67, *p* = 0.005, η²_G = 0.096
- Greenhouse-Geisser corrected: *p* = 0.014 (ε = 0.686)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 2.41 | 15 | = 0.088 | 0.73 [0.01, 1.11] | medium | n.s. |
| 3 to 1 vs 3 to 3 | 3.45 | 15 | = 0.018 | 0.87 [0.24, 1.49] | large | * |
| 3 to 1 vs 3 to 4 | 3.53 | 15 | = 0.018 | 0.92 [0.32, 1.50] | large | * |
| 3 to 1 vs 3 to 5 | 3.86 | 15 | = 0.018 | 0.91 [0.28, 1.49] | large | * |
| 3 to 1 vs 3 to 6 | 2.62 | 15 | = 0.073 | 0.92 [0.10, 1.24] | large | n.s. |
| 3 to 2 vs 3 to 3 | 0.25 | 15 | = 0.866 | 0.05 [-0.24, 0.68] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | 0.66 | 15 | = 0.866 | 0.16 [-0.13, 0.78] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | 0.83 | 15 | = 0.866 | 0.22 [-0.24, 0.66] | small | n.s. |
| 3 to 2 vs 3 to 6 | 0.55 | 15 | = 0.866 | 0.14 [-0.12, 0.79] | negligible | n.s. |
| 3 to 3 vs 3 to 4 | 1.17 | 15 | = 0.653 | 0.13 [-0.31, 0.60] | negligible | n.s. |
| 3 to 3 vs 3 to 5 | 0.71 | 15 | = 0.866 | 0.19 [-0.38, 0.53] | negligible | n.s. |
| 3 to 3 vs 3 to 6 | 0.41 | 15 | = 0.866 | 0.10 [-0.39, 0.50] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | 0.25 | 15 | = 0.866 | 0.07 [-0.50, 0.39] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | -0.12 | 15 | = 0.904 | -0.03 [-0.50, 0.38] | negligible | n.s. |
| 3 to 5 vs 3 to 6 | -0.37 | 15 | = 0.866 | -0.10 [-0.43, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 532.71, BIC = 558.52
- **3 to 2 vs 3 to 1**: *β* = -0.10, *SE* = 0.509, *z* = -0.201, *p* = 0.840
- **3 to 3 vs 3 to 1**: *β* = 0.38, *SE* = 0.497, *z* = 0.768, *p* = 0.443
- **3 to 4 vs 3 to 1**: *β* = -0.27, *SE* = 0.490, *z* = -0.554, *p* = 0.579
- **3 to 5 vs 3 to 1**: *β* = 0.07, *SE* = 0.507, *z* = 0.131, *p* = 0.896
- **3 to 6 vs 3 to 1**: *β* = -1.09, *SE* = 0.506, *z* = -2.160, *p* = 0.031
- **SNR**: *β* = -0.47, *SE* = 0.064, *z* = -7.253, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.10 | 0.51 | 0.20 | 0.840 | 0.993 | n.s. |
| 3 to 1 - 3 to 3 | -0.38 | 0.50 | -0.77 | 0.443 | 0.991 | n.s. |
| 3 to 1 - 3 to 4 | 0.27 | 0.49 | 0.55 | 0.579 | 0.991 | n.s. |
| 3 to 1 - 3 to 5 | -0.07 | 0.51 | -0.13 | 0.896 | 0.993 | n.s. |
| 3 to 1 - 3 to 6 | 1.09 | 0.51 | 2.16 | 0.031 | 0.321 | n.s. |
| 3 to 2 - 3 to 3 | -0.48 | 0.46 | -1.04 | 0.297 | 0.958 | n.s. |
| 3 to 2 - 3 to 4 | 0.17 | 0.46 | 0.37 | 0.712 | 0.993 | n.s. |
| 3 to 2 - 3 to 5 | -0.17 | 0.46 | -0.37 | 0.712 | 0.993 | n.s. |
| 3 to 2 - 3 to 6 | 0.99 | 0.45 | 2.18 | 0.029 | 0.321 | n.s. |
| 3 to 3 - 3 to 4 | 0.65 | 0.46 | 1.43 | 0.152 | 0.809 | n.s. |
| 3 to 3 - 3 to 5 | 0.32 | 0.46 | 0.68 | 0.496 | 0.991 | n.s. |
| 3 to 3 - 3 to 6 | 1.47 | 0.46 | 3.22 | 0.001 | 0.019 | * |
| 3 to 4 - 3 to 5 | -0.34 | 0.46 | -0.74 | 0.459 | 0.991 | n.s. |
| 3 to 4 - 3 to 6 | 0.82 | 0.45 | 1.81 | 0.071 | 0.553 | n.s. |
| 3 to 5 - 3 to 6 | 1.16 | 0.45 | 2.55 | 0.011 | 0.140 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.52, *p* = 0.036, η²_G = 0.069
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 1.44 | 15 | = 0.318 | 0.41 [-0.13, 0.94] | small | n.s. |
| 3 to 1 vs 3 to 3 | 0.10 | 15 | = 0.922 | 0.03 [-0.51, 0.56] | negligible | n.s. |
| 3 to 1 vs 3 to 4 | 1.54 | 15 | = 0.316 | 0.37 [-0.05, 1.00] | small | n.s. |
| 3 to 1 vs 3 to 5 | 0.85 | 15 | = 0.554 | 0.27 [-0.32, 0.71] | small | n.s. |
| 3 to 1 vs 3 to 6 | 2.23 | 15 | = 0.223 | 0.75 [-0.02, 1.08] | medium | n.s. |
| 3 to 2 vs 3 to 3 | -2.18 | 15 | = 0.223 | -0.41 [-0.93, 0.03] | small | n.s. |
| 3 to 2 vs 3 to 4 | -0.40 | 15 | = 0.804 | -0.09 [-0.59, 0.30] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -0.55 | 15 | = 0.739 | -0.13 [-0.53, 0.36] | negligible | n.s. |
| 3 to 2 vs 3 to 6 | 1.53 | 15 | = 0.316 | 0.34 [-0.05, 0.87] | small | n.s. |
| 3 to 3 vs 3 to 4 | 1.34 | 15 | = 0.318 | 0.37 [-0.20, 0.73] | small | n.s. |
| 3 to 3 vs 3 to 5 | 1.30 | 15 | = 0.318 | 0.26 [-0.06, 0.88] | small | n.s. |
| 3 to 3 vs 3 to 6 | 2.97 | 15 | = 0.144 | 0.78 [0.33, 1.36] | medium | n.s. |
| 3 to 4 vs 3 to 5 | -0.23 | 15 | = 0.881 | -0.06 [-0.42, 0.47] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 2.01 | 15 | = 0.223 | 0.46 [0.08, 1.03] | small | n.s. |
| 3 to 5 vs 3 to 6 | 1.92 | 15 | = 0.223 | 0.46 [0.02, 0.95] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 553.23, BIC = 574.21
- **3 to 2 vs 3 to 1**: *β* = -6.16, *SE* = 3.131, *z* = -1.967, *p* = 0.049
- **3 to 3 vs 3 to 1**: *β* = -0.43, *SE* = 2.877, *z* = -0.151, *p* = 0.880
- **3 to 4 vs 3 to 1**: *β* = -3.53, *SE* = 2.829, *z* = -1.249, *p* = 0.212
- **3 to 5 vs 3 to 1**: *β* = -3.30, *SE* = 3.069, *z* = -1.075, *p* = 0.282
- **3 to 6 vs 3 to 1**: *β* = -5.42, *SE* = 3.133, *z* = -1.729, *p* = 0.084
- **SNR**: *β* = 0.46, *SE* = 0.502, *z* = 0.915, *p* = 0.360

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 6.16 | 3.13 | 1.97 | 0.049 | 0.531 | n.s. |
| 3 to 1 - 3 to 3 | 0.43 | 2.88 | 0.15 | 0.880 | 0.995 | n.s. |
| 3 to 1 - 3 to 4 | 3.53 | 2.83 | 1.25 | 0.212 | 0.927 | n.s. |
| 3 to 1 - 3 to 5 | 3.30 | 3.07 | 1.08 | 0.282 | 0.964 | n.s. |
| 3 to 1 - 3 to 6 | 5.42 | 3.13 | 1.73 | 0.084 | 0.705 | n.s. |
| 3 to 2 - 3 to 3 | -5.73 | 3.31 | -1.73 | 0.084 | 0.705 | n.s. |
| 3 to 2 - 3 to 4 | -2.63 | 3.28 | -0.80 | 0.424 | 0.978 | n.s. |
| 3 to 2 - 3 to 5 | -2.86 | 3.47 | -0.82 | 0.410 | 0.978 | n.s. |
| 3 to 2 - 3 to 6 | -0.74 | 3.55 | -0.21 | 0.835 | 0.995 | n.s. |
| 3 to 3 - 3 to 4 | 3.10 | 3.05 | 1.02 | 0.310 | 0.964 | n.s. |
| 3 to 3 - 3 to 5 | 2.87 | 3.26 | 0.88 | 0.379 | 0.978 | n.s. |
| 3 to 3 - 3 to 6 | 4.98 | 3.32 | 1.50 | 0.133 | 0.819 | n.s. |
| 3 to 4 - 3 to 5 | -0.23 | 3.23 | -0.07 | 0.942 | 0.995 | n.s. |
| 3 to 4 - 3 to 6 | 1.88 | 3.31 | 0.57 | 0.569 | 0.980 | n.s. |
| 3 to 5 - 3 to 6 | 2.12 | 3.49 | 0.61 | 0.544 | 0.980 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.00, *p* = 0.500, η²_G = 0.457
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.00 | 1 | = 0.545 | -1.34 [-0.35, 1.26] | large | n.s. |
| 3 to 1 vs 3 to 3 | -1.00 | 1 | = 0.545 | -1.34 [-0.87, 0.48] | large | n.s. |
| 3 to 1 vs 3 to 4 | -1.00 | 1 | = 0.545 | -1.34 [-0.69, 0.74] | large | n.s. |
| 3 to 1 vs 3 to 5 | -1.40 | 1 | = 0.545 | -1.70 [-0.50, 1.23] | large | n.s. |
| 3 to 1 vs 3 to 6 | -0.71 | 1 | = 0.605 | -1.00 [-0.97, 0.88] | large | n.s. |
| 3 to 2 vs 3 to 3 | nan | 1 | n/a | 0.00 [-1.24, 0.49] | negligible | n.s. |
| 3 to 2 vs 3 to 4 | nan | 1 | n/a | 0.00 [-1.31, 0.60] | negligible | n.s. |
| 3 to 2 vs 3 to 5 | -1.00 | 1 | = 0.545 | -0.45 [-1.27, 0.85] | small | n.s. |
| 3 to 2 vs 3 to 6 | 1.00 | 1 | = 0.545 | 0.28 [-1.15, 0.96] | small | n.s. |
| 3 to 3 vs 3 to 4 | nan | 1 | n/a | 0.00 [-1.01, 0.68] | negligible | n.s. |
| 3 to 3 vs 3 to 5 | -1.00 | 1 | = 0.545 | -0.45 [-0.55, 1.38] | small | n.s. |
| 3 to 3 vs 3 to 6 | 1.00 | 1 | = 0.545 | 0.28 [-0.44, 1.30] | small | n.s. |
| 3 to 4 vs 3 to 5 | -1.00 | 1 | = 0.545 | -0.45 [-1.30, 0.61] | small | n.s. |
| 3 to 4 vs 3 to 6 | 1.00 | 1 | = 0.545 | 0.28 [-0.56, 2.41] | small | n.s. |
| 3 to 5 vs 3 to 6 | 1.00 | 1 | = 0.545 | 0.63 [-1.05, 1.05] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 264.29, BIC = 285.27
- **3 to 2 vs 3 to 1**: *β* = -0.81, *SE* = 0.427, *z* = -1.888, *p* = 0.059
- **3 to 3 vs 3 to 1**: *β* = 0.02, *SE* = 0.392, *z* = 0.058, *p* = 0.953
- **3 to 4 vs 3 to 1**: *β* = 0.11, *SE* = 0.386, *z* = 0.274, *p* = 0.784
- **3 to 5 vs 3 to 1**: *β* = -0.47, *SE* = 0.417, *z* = -1.127, *p* = 0.260
- **3 to 6 vs 3 to 1**: *β* = 0.07, *SE* = 0.432, *z* = 0.171, *p* = 0.864
- **SNR**: *β* = 0.67, *SE* = 0.069, *z* = 9.634, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | 0.81 | 0.43 | 1.89 | 0.059 | 0.574 | n.s. |
| 3 to 1 - 3 to 3 | -0.02 | 0.39 | -0.06 | 0.953 | 1.000 | n.s. |
| 3 to 1 - 3 to 4 | -0.11 | 0.39 | -0.27 | 0.784 | 1.000 | n.s. |
| 3 to 1 - 3 to 5 | 0.47 | 0.42 | 1.13 | 0.260 | 0.942 | n.s. |
| 3 to 1 - 3 to 6 | -0.07 | 0.43 | -0.17 | 0.864 | 1.000 | n.s. |
| 3 to 2 - 3 to 3 | -0.83 | 0.44 | -1.86 | 0.062 | 0.574 | n.s. |
| 3 to 2 - 3 to 4 | -0.91 | 0.45 | -2.04 | 0.042 | 0.471 | n.s. |
| 3 to 2 - 3 to 5 | -0.34 | 0.47 | -0.72 | 0.474 | 0.989 | n.s. |
| 3 to 2 - 3 to 6 | -0.88 | 0.48 | -1.84 | 0.066 | 0.574 | n.s. |
| 3 to 3 - 3 to 4 | -0.08 | 0.42 | -0.20 | 0.842 | 1.000 | n.s. |
| 3 to 3 - 3 to 5 | 0.49 | 0.44 | 1.12 | 0.263 | 0.942 | n.s. |
| 3 to 3 - 3 to 6 | -0.05 | 0.45 | -0.11 | 0.909 | 1.000 | n.s. |
| 3 to 4 - 3 to 5 | 0.58 | 0.44 | 1.32 | 0.187 | 0.897 | n.s. |
| 3 to 4 - 3 to 6 | 0.03 | 0.46 | 0.07 | 0.944 | 1.000 | n.s. |
| 3 to 5 - 3 to 6 | -0.54 | 0.47 | -1.16 | 0.247 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.545, η²_G = 0.463
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.91 | 1 | = 0.921 | -2.66 [-0.43, 1.16] | large | n.s. |
| 3 to 1 vs 3 to 3 | -0.71 | 1 | = 0.978 | -0.91 [-0.38, 0.99] | large | n.s. |
| 3 to 1 vs 3 to 4 | -0.40 | 1 | = 0.978 | -0.51 [-0.42, 1.05] | medium | n.s. |
| 3 to 1 vs 3 to 5 | -84.51 | 1 | = 0.113 | -1.72 [-0.51, 1.21] | large | n.s. |
| 3 to 1 vs 3 to 6 | -2.91 | 1 | = 0.789 | -2.34 [-1.03, 0.82] | large | n.s. |
| 3 to 2 vs 3 to 3 | 0.36 | 1 | = 0.978 | 0.25 [-1.21, 0.51] | small | n.s. |
| 3 to 2 vs 3 to 4 | 7.61 | 1 | = 0.624 | 3.46 [-1.32, 0.59] | large | n.s. |
| 3 to 2 vs 3 to 5 | 0.51 | 1 | = 0.978 | 0.71 [-1.38, 0.77] | medium | n.s. |
| 3 to 2 vs 3 to 6 | 0.99 | 1 | = 0.978 | 1.20 [-1.59, 0.63] | large | n.s. |
| 3 to 3 vs 3 to 4 | 0.89 | 1 | = 0.978 | 0.76 [-0.65, 1.04] | medium | n.s. |
| 3 to 3 vs 3 to 5 | 0.05 | 1 | = 0.987 | 0.06 [-0.78, 1.07] | negligible | n.s. |
| 3 to 3 vs 3 to 6 | 0.07 | 1 | = 0.987 | 0.07 [-0.94, 0.74] | negligible | n.s. |
| 3 to 4 vs 3 to 5 | -1.41 | 1 | = 0.978 | -1.80 [-0.52, 1.43] | large | n.s. |
| 3 to 4 vs 3 to 6 | -3.48 | 1 | = 0.789 | -4.70 [-1.32, 1.17] | large | n.s. |
| 3 to 5 vs 3 to 6 | 0.02 | 1 | = 0.987 | 0.02 [-0.82, 1.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1031.29, BIC = 1055.09
- **3 to 2 vs 3 to 1**: *β* = 2.43, *SE* = 9.853, *z* = 0.247, *p* = 0.805
- **3 to 3 vs 3 to 1**: *β* = -15.50, *SE* = 10.514, *z* = -1.474, *p* = 0.140
- **3 to 4 vs 3 to 1**: *β* = 10.64, *SE* = 10.080, *z* = 1.056, *p* = 0.291
- **3 to 5 vs 3 to 1**: *β* = 6.86, *SE* = 10.291, *z* = 0.666, *p* = 0.505
- **3 to 6 vs 3 to 1**: *β* = -0.99, *SE* = 9.939, *z* = -0.099, *p* = 0.921
- **SNR**: *β* = -0.65, *SE* = 0.770, *z* = -0.849, *p* = 0.396

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -2.43 | 9.85 | -0.25 | 0.805 | 0.996 | n.s. |
| 3 to 1 - 3 to 3 | 15.50 | 10.51 | 1.47 | 0.140 | 0.837 | n.s. |
| 3 to 1 - 3 to 4 | -10.64 | 10.08 | -1.06 | 0.291 | 0.955 | n.s. |
| 3 to 1 - 3 to 5 | -6.86 | 10.29 | -0.67 | 0.505 | 0.987 | n.s. |
| 3 to 1 - 3 to 6 | 0.99 | 9.94 | 0.10 | 0.921 | 0.996 | n.s. |
| 3 to 2 - 3 to 3 | 17.93 | 10.33 | 1.74 | 0.083 | 0.674 | n.s. |
| 3 to 2 - 3 to 4 | -8.21 | 10.14 | -0.81 | 0.418 | 0.987 | n.s. |
| 3 to 2 - 3 to 5 | -4.42 | 10.17 | -0.43 | 0.664 | 0.996 | n.s. |
| 3 to 2 - 3 to 6 | 3.42 | 9.68 | 0.35 | 0.724 | 0.996 | n.s. |
| 3 to 3 - 3 to 4 | -26.14 | 10.78 | -2.42 | 0.015 | 0.207 | n.s. |
| 3 to 3 - 3 to 5 | -22.36 | 10.65 | -2.10 | 0.036 | 0.400 | n.s. |
| 3 to 3 - 3 to 6 | -14.51 | 10.17 | -1.43 | 0.153 | 0.840 | n.s. |
| 3 to 4 - 3 to 5 | 3.79 | 10.47 | 0.36 | 0.718 | 0.996 | n.s. |
| 3 to 4 - 3 to 6 | 11.63 | 10.06 | 1.16 | 0.248 | 0.942 | n.s. |
| 3 to 5 - 3 to 6 | 7.84 | 10.02 | 0.78 | 0.434 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.70, *p* = 0.160, η²_G = 0.135
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | 0.26 | 7 | = 0.857 | 0.11 [-0.61, 0.42] | negligible | n.s. |
| 3 to 1 vs 3 to 3 | 0.61 | 7 | = 0.763 | 0.40 [-0.23, 0.91] | small | n.s. |
| 3 to 1 vs 3 to 4 | -1.47 | 7 | = 0.479 | -0.77 [-0.97, 0.22] | medium | n.s. |
| 3 to 1 vs 3 to 5 | -1.20 | 7 | = 0.505 | -0.64 [-0.86, 0.27] | medium | n.s. |
| 3 to 1 vs 3 to 6 | -0.03 | 7 | = 0.981 | -0.01 [-0.63, 0.40] | negligible | n.s. |
| 3 to 2 vs 3 to 3 | 0.48 | 7 | = 0.806 | 0.25 [-0.20, 1.06] | small | n.s. |
| 3 to 2 vs 3 to 4 | -2.12 | 7 | = 0.269 | -0.78 [-0.83, 0.34] | medium | n.s. |
| 3 to 2 vs 3 to 5 | -2.28 | 7 | = 0.269 | -0.66 [-0.88, 0.30] | medium | n.s. |
| 3 to 2 vs 3 to 6 | -0.29 | 7 | = 0.857 | -0.10 [-0.54, 0.53] | negligible | n.s. |
| 3 to 3 vs 3 to 4 | -2.23 | 7 | = 0.269 | -1.07 [-1.37, 0.18] | large | n.s. |
| 3 to 3 vs 3 to 5 | -2.15 | 7 | = 0.269 | -0.97 [-1.42, 0.00] | large | n.s. |
| 3 to 3 vs 3 to 6 | -0.70 | 7 | = 0.756 | -0.32 [-0.76, 0.41] | small | n.s. |
| 3 to 4 vs 3 to 5 | 0.82 | 7 | = 0.735 | 0.18 [-0.55, 0.66] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.45 | 7 | = 0.479 | 0.61 [-0.40, 0.71] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 1.33 | 7 | = 0.483 | 0.48 [-0.33, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 494.04, BIC = 517.84
- **3 to 2 vs 3 to 1**: *β* = 1.45, *SE* = 0.698, *z* = 2.070, *p* = 0.038
- **3 to 3 vs 3 to 1**: *β* = -0.62, *SE* = 0.746, *z* = -0.825, *p* = 0.409
- **3 to 4 vs 3 to 1**: *β* = 1.23, *SE* = 0.718, *z* = 1.718, *p* = 0.086
- **3 to 5 vs 3 to 1**: *β* = 0.79, *SE* = 0.733, *z* = 1.076, *p* = 0.282
- **3 to 6 vs 3 to 1**: *β* = -0.13, *SE* = 0.707, *z* = -0.185, *p* = 0.853
- **SNR**: *β* = 0.25, *SE* = 0.058, *z* = 4.398, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 3 to 2 | -1.45 | 0.70 | -2.07 | 0.038 | 0.375 | n.s. |
| 3 to 1 - 3 to 3 | 0.62 | 0.75 | 0.82 | 0.409 | 0.931 | n.s. |
| 3 to 1 - 3 to 4 | -1.23 | 0.72 | -1.72 | 0.086 | 0.554 | n.s. |
| 3 to 1 - 3 to 5 | -0.79 | 0.73 | -1.08 | 0.282 | 0.901 | n.s. |
| 3 to 1 - 3 to 6 | 0.13 | 0.71 | 0.19 | 0.853 | 0.945 | n.s. |
| 3 to 2 - 3 to 3 | 2.06 | 0.73 | 2.82 | 0.005 | 0.070 | n.s. |
| 3 to 2 - 3 to 4 | 0.21 | 0.72 | 0.30 | 0.766 | 0.945 | n.s. |
| 3 to 2 - 3 to 5 | 0.66 | 0.72 | 0.92 | 0.359 | 0.931 | n.s. |
| 3 to 2 - 3 to 6 | 1.58 | 0.68 | 2.31 | 0.021 | 0.242 | n.s. |
| 3 to 3 - 3 to 4 | -1.85 | 0.77 | -2.41 | 0.016 | 0.200 | n.s. |
| 3 to 3 - 3 to 5 | -1.40 | 0.75 | -1.87 | 0.062 | 0.472 | n.s. |
| 3 to 3 - 3 to 6 | -0.48 | 0.72 | -0.67 | 0.500 | 0.937 | n.s. |
| 3 to 4 - 3 to 5 | 0.44 | 0.74 | 0.60 | 0.548 | 0.937 | n.s. |
| 3 to 4 - 3 to 6 | 1.36 | 0.71 | 1.92 | 0.054 | 0.460 | n.s. |
| 3 to 5 - 3 to 6 | 0.92 | 0.70 | 1.31 | 0.192 | 0.818 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.93, *p* = 0.006, η²_G = 0.186
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 3 to 2 | -1.39 | 7 | = 0.346 | -0.56 [-0.70, 0.33] | medium | n.s. |
| 3 to 1 vs 3 to 3 | 3.90 | 7 | = 0.029 | 0.90 [-0.17, 0.98] | large | * |
| 3 to 1 vs 3 to 4 | -0.50 | 7 | = 0.705 | -0.20 [-0.61, 0.54] | negligible | n.s. |
| 3 to 1 vs 3 to 5 | 0.01 | 7 | = 0.993 | 0.00 [-0.45, 0.66] | negligible | n.s. |
| 3 to 1 vs 3 to 6 | 0.55 | 7 | = 0.705 | 0.25 [-0.22, 0.84] | small | n.s. |
| 3 to 2 vs 3 to 3 | 4.25 | 7 | = 0.029 | 1.54 [-0.10, 1.20] | large | * |
| 3 to 2 vs 3 to 4 | 1.16 | 7 | = 0.424 | 0.42 [-0.42, 0.75] | small | n.s. |
| 3 to 2 vs 3 to 5 | 1.64 | 7 | = 0.312 | 0.53 [-0.20, 1.00] | medium | n.s. |
| 3 to 2 vs 3 to 6 | 4.04 | 7 | = 0.029 | 0.91 [0.25, 1.51] | large | * |
| 3 to 3 vs 3 to 4 | -3.65 | 7 | = 0.030 | -1.32 [-1.91, -0.14] | large | * |
| 3 to 3 vs 3 to 5 | -2.97 | 7 | = 0.063 | -0.83 [-1.19, 0.16] | large | n.s. |
| 3 to 3 vs 3 to 6 | -2.19 | 7 | = 0.161 | -0.89 [-0.86, 0.32] | large | n.s. |
| 3 to 4 vs 3 to 5 | 0.46 | 7 | = 0.705 | 0.19 [-0.38, 0.85] | negligible | n.s. |
| 3 to 4 vs 3 to 6 | 1.44 | 7 | = 0.346 | 0.55 [0.10, 1.35] | medium | n.s. |
| 3 to 5 vs 3 to 6 | 0.60 | 7 | = 0.705 | 0.23 [-0.20, 0.95] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.005). Post-hoc tests revealed:
  - 3 to 1 showed greater latency than 3 to 3 (*d* = 0.87)
  - 3 to 1 showed greater latency than 3 to 4 (*d* = 0.92)
  - 3 to 1 showed greater latency than 3 to 5 (*d* = 0.91)
**N1 amplitude:** Significant main effect of condition (*p* = 0.036) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.006). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 3 to 3 (*d* = 0.90)
  - 3 to 2 showed greater amplitude than 3 to 3 (*d* = 1.54)
  - 3 to 2 showed greater amplitude than 3 to 6 (*d* = 0.91)
  - 3 to 3 showed smaller amplitude than 3 to 4 (*d* = -1.32)

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
