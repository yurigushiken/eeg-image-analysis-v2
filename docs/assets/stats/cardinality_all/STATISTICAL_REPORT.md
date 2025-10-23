# Statistical Analysis Report: tables

**Generated:** 2025-10-23 18:50:00

---

## 1. Analysis Overview

**Total Measurements:** 432
**Number of Subjects:** 24
**Number of Conditions:** 6

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | -2.43 µV | 2.41 | 0.62 | [-8.29, -0.01] |
| Cardinality2 | 22 | -3.21 µV | 1.92 | 0.41 | [-7.72, -0.19] |
| Cardinality3 | 22 | -3.37 µV | 1.70 | 0.36 | [-7.86, -1.05] |
| Cardinality4 | 22 | -3.94 µV | 2.41 | 0.51 | [-9.95, -1.01] |
| Cardinality5 | 24 | -3.82 µV | 2.50 | 0.51 | [-9.48, -0.00] |
| Cardinality6 | 23 | -3.56 µV | 2.30 | 0.48 | [-7.83, 0.01] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | 177.49 ms | 15.59 | 4.03 | [152.29, 203.67] |
| Cardinality2 | 22 | 172.57 ms | 12.17 | 2.60 | [150.03, 193.06] |
| Cardinality3 | 22 | 172.69 ms | 8.86 | 1.89 | [156.19, 194.49] |
| Cardinality4 | 22 | 174.23 ms | 9.22 | 1.97 | [155.68, 192.80] |
| Cardinality5 | 24 | 174.90 ms | 11.35 | 2.32 | [148.04, 203.01] |
| Cardinality6 | 23 | 175.51 ms | 12.05 | 2.51 | [157.54, 203.60] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 2.65 µV | 2.51 | 0.57 | [0.17, 10.40] |
| Cardinality2 | 12 | 2.08 µV | 1.77 | 0.51 | [0.46, 6.44] |
| Cardinality3 | 14 | 2.20 µV | 2.07 | 0.55 | [0.10, 7.31] |
| Cardinality4 | 12 | 2.13 µV | 1.52 | 0.44 | [0.24, 4.82] |
| Cardinality5 | 14 | 1.90 µV | 1.53 | 0.41 | [-0.04, 4.57] |
| Cardinality6 | 12 | 1.93 µV | 1.87 | 0.54 | [0.12, 6.89] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 110.14 ms | 5.50 | 1.26 | [98.41, 118.85] |
| Cardinality2 | 12 | 109.06 ms | 4.24 | 1.22 | [102.40, 118.25] |
| Cardinality3 | 14 | 108.59 ms | 4.99 | 1.33 | [98.69, 119.31] |
| Cardinality4 | 12 | 107.52 ms | 4.81 | 1.39 | [99.51, 114.92] |
| Cardinality5 | 14 | 106.86 ms | 3.88 | 1.04 | [96.17, 112.33] |
| Cardinality6 | 12 | 108.49 ms | 5.07 | 1.46 | [100.34, 118.88] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 1.57 µV | 1.71 | 0.46 | [0.18, 5.50] |
| Cardinality2 | 13 | 2.62 µV | 1.70 | 0.47 | [0.21, 6.61] |
| Cardinality3 | 16 | 3.19 µV | 2.03 | 0.51 | [0.84, 8.10] |
| Cardinality4 | 11 | 3.30 µV | 2.61 | 0.79 | [0.21, 8.28] |
| Cardinality5 | 14 | 1.81 µV | 1.38 | 0.37 | [-0.02, 5.00] |
| Cardinality6 | 14 | 3.40 µV | 2.42 | 0.65 | [0.08, 9.36] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 457.62 ms | 10.14 | 2.71 | [442.18, 478.70] |
| Cardinality2 | 13 | 458.10 ms | 6.39 | 1.77 | [445.04, 468.12] |
| Cardinality3 | 16 | 459.15 ms | 5.71 | 1.43 | [449.70, 469.63] |
| Cardinality4 | 11 | 457.62 ms | 4.43 | 1.33 | [448.03, 463.60] |
| Cardinality5 | 14 | 457.01 ms | 7.91 | 2.11 | [440.76, 468.56] |
| Cardinality6 | 14 | 463.25 ms | 6.17 | 1.65 | [456.48, 479.55] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 468.71, BIC = 494.38
- **Cardinality2 vs Cardinality1**: *β* = -0.94, *SE* = 0.415, *z* = -2.263, *p* = 0.024
- **Cardinality3 vs Cardinality1**: *β* = -0.94, *SE* = 0.419, *z* = -2.249, *p* = 0.025
- **Cardinality4 vs Cardinality1**: *β* = -1.07, *SE* = 0.420, *z* = -2.543, *p* = 0.011
- **Cardinality5 vs Cardinality1**: *β* = -1.06, *SE* = 0.412, *z* = -2.581, *p* = 0.010
- **Cardinality6 vs Cardinality1**: *β* = -1.08, *SE* = 0.412, *z* = -2.633, *p* = 0.008
- **SNR**: *β* = -0.44, *SE* = 0.046, *z* = -9.570, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.94 | 0.41 | 2.26 | 0.024 | 0.250 | n.s. |
| Cardinality1 - Cardinality3 | 0.94 | 0.42 | 2.25 | 0.025 | 0.250 | n.s. |
| Cardinality1 - Cardinality4 | 1.07 | 0.42 | 2.54 | 0.011 | 0.134 | n.s. |
| Cardinality1 - Cardinality5 | 1.06 | 0.41 | 2.58 | 0.010 | 0.129 | n.s. |
| Cardinality1 - Cardinality6 | 1.09 | 0.41 | 2.63 | 0.008 | 0.120 | n.s. |
| Cardinality2 - Cardinality3 | 0.00 | 0.37 | 0.01 | 0.994 | 1.000 | n.s. |
| Cardinality2 - Cardinality4 | 0.13 | 0.38 | 0.34 | 0.730 | 1.000 | n.s. |
| Cardinality2 - Cardinality5 | 0.13 | 0.37 | 0.34 | 0.733 | 1.000 | n.s. |
| Cardinality2 - Cardinality6 | 0.15 | 0.37 | 0.40 | 0.690 | 1.000 | n.s. |
| Cardinality3 - Cardinality4 | 0.13 | 0.38 | 0.34 | 0.735 | 1.000 | n.s. |
| Cardinality3 - Cardinality5 | 0.12 | 0.36 | 0.34 | 0.737 | 1.000 | n.s. |
| Cardinality3 - Cardinality6 | 0.14 | 0.37 | 0.39 | 0.696 | 1.000 | n.s. |
| Cardinality4 - Cardinality5 | -0.00 | 0.36 | -0.01 | 0.990 | 1.000 | n.s. |
| Cardinality4 - Cardinality6 | 0.02 | 0.37 | 0.04 | 0.964 | 1.000 | n.s. |
| Cardinality5 - Cardinality6 | 0.02 | 0.36 | 0.06 | 0.954 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.316, η²_G = 0.048
- Greenhouse-Geisser corrected: *p* = 0.321 (ε = 0.588)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.55 | 11 | = 0.740 | 0.24 [-0.28, 0.85] | small | n.s. |
| Cardinality1 vs Cardinality3 | 0.82 | 11 | = 0.643 | 0.30 [-0.29, 0.95] | small | n.s. |
| Cardinality1 vs Cardinality4 | 1.29 | 11 | = 0.544 | 0.51 [-0.19, 1.01] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 1.54 | 11 | = 0.544 | 0.61 [-0.09, 1.08] | medium | n.s. |
| Cardinality1 vs Cardinality6 | 1.25 | 11 | = 0.544 | 0.45 [-0.11, 1.06] | small | n.s. |
| Cardinality2 vs Cardinality3 | 0.37 | 11 | = 0.765 | 0.06 [-0.30, 0.65] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | 1.44 | 11 | = 0.544 | 0.32 [-0.07, 0.87] | small | n.s. |
| Cardinality2 vs Cardinality5 | 1.28 | 11 | = 0.544 | 0.42 [-0.12, 0.79] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.84 | 11 | = 0.643 | 0.25 [-0.22, 0.67] | small | n.s. |
| Cardinality3 vs Cardinality4 | 1.20 | 11 | = 0.544 | 0.28 [-0.09, 0.88] | small | n.s. |
| Cardinality3 vs Cardinality5 | 1.46 | 11 | = 0.544 | 0.38 [-0.12, 0.79] | small | n.s. |
| Cardinality3 vs Cardinality6 | 0.85 | 11 | = 0.643 | 0.21 [-0.32, 0.60] | small | n.s. |
| Cardinality4 vs Cardinality5 | 0.35 | 11 | = 0.765 | 0.08 [-0.50, 0.39] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -0.31 | 11 | = 0.765 | -0.07 [-0.66, 0.24] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -0.63 | 11 | = 0.736 | -0.15 [-0.60, 0.27] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 938.67, BIC = 964.34
- **Cardinality2 vs Cardinality1**: *β* = -4.93, *SE* = 2.459, *z* = -2.005, *p* = 0.045
- **Cardinality3 vs Cardinality1**: *β* = -3.72, *SE* = 2.489, *z* = -1.496, *p* = 0.135
- **Cardinality4 vs Cardinality1**: *β* = -3.05, *SE* = 2.495, *z* = -1.224, *p* = 0.221
- **Cardinality5 vs Cardinality1**: *β* = -2.56, *SE* = 2.449, *z* = -1.045, *p* = 0.296
- **Cardinality6 vs Cardinality1**: *β* = -2.50, *SE* = 2.444, *z* = -1.023, *p* = 0.306
- **SNR**: *β* = -0.27, *SE* = 0.283, *z* = -0.956, *p* = 0.339

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 4.93 | 2.46 | 2.00 | 0.045 | 0.499 | n.s. |
| Cardinality1 - Cardinality3 | 3.72 | 2.49 | 1.50 | 0.135 | 0.868 | n.s. |
| Cardinality1 - Cardinality4 | 3.05 | 2.50 | 1.22 | 0.221 | 0.961 | n.s. |
| Cardinality1 - Cardinality5 | 2.56 | 2.45 | 1.05 | 0.296 | 0.974 | n.s. |
| Cardinality1 - Cardinality6 | 2.50 | 2.44 | 1.02 | 0.306 | 0.974 | n.s. |
| Cardinality2 - Cardinality3 | -1.21 | 2.20 | -0.55 | 0.584 | 0.997 | n.s. |
| Cardinality2 - Cardinality4 | -1.88 | 2.23 | -0.84 | 0.400 | 0.983 | n.s. |
| Cardinality2 - Cardinality5 | -2.37 | 2.18 | -1.09 | 0.277 | 0.974 | n.s. |
| Cardinality2 - Cardinality6 | -2.43 | 2.17 | -1.12 | 0.262 | 0.974 | n.s. |
| Cardinality3 - Cardinality4 | -0.67 | 2.23 | -0.30 | 0.764 | 0.997 | n.s. |
| Cardinality3 - Cardinality5 | -1.16 | 2.16 | -0.54 | 0.590 | 0.997 | n.s. |
| Cardinality3 - Cardinality6 | -1.22 | 2.18 | -0.56 | 0.574 | 0.997 | n.s. |
| Cardinality4 - Cardinality5 | -0.49 | 2.14 | -0.23 | 0.818 | 0.997 | n.s. |
| Cardinality4 - Cardinality6 | -0.55 | 2.17 | -0.26 | 0.799 | 0.997 | n.s. |
| Cardinality5 - Cardinality6 | -0.06 | 2.12 | -0.03 | 0.977 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.29, *p* = 0.916, η²_G = 0.010
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.57 | 11 | = 0.923 | 0.21 [-0.18, 0.97] | small | n.s. |
| Cardinality1 vs Cardinality3 | 0.25 | 11 | = 0.923 | 0.06 [-0.38, 0.84] | negligible | n.s. |
| Cardinality1 vs Cardinality4 | 0.34 | 11 | = 0.923 | 0.12 [-0.36, 0.81] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | 0.21 | 11 | = 0.923 | 0.06 [-0.30, 0.83] | negligible | n.s. |
| Cardinality1 vs Cardinality6 | -0.34 | 11 | = 0.923 | -0.09 [-0.38, 0.74] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | -0.67 | 11 | = 0.923 | -0.15 [-0.48, 0.45] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -0.31 | 11 | = 0.923 | -0.11 [-0.64, 0.28] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | -0.57 | 11 | = 0.923 | -0.14 [-0.60, 0.29] | negligible | n.s. |
| Cardinality2 vs Cardinality6 | -1.10 | 11 | = 0.923 | -0.29 [-0.58, 0.31] | small | n.s. |
| Cardinality3 vs Cardinality4 | 0.18 | 11 | = 0.923 | 0.05 [-0.44, 0.50] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | 0.02 | 11 | = 0.985 | 0.00 [-0.51, 0.37] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -0.92 | 11 | = 0.923 | -0.16 [-0.58, 0.33] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | -0.20 | 11 | = 0.923 | -0.05 [-0.57, 0.32] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -0.70 | 11 | = 0.923 | -0.22 [-0.54, 0.35] | small | n.s. |
| Cardinality5 vs Cardinality6 | -0.80 | 11 | = 0.923 | -0.16 [-0.44, 0.42] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 272.06, BIC = 293.83
- **Cardinality2 vs Cardinality1**: *β* = -0.27, *SE* = 0.365, *z* = -0.735, *p* = 0.462
- **Cardinality3 vs Cardinality1**: *β* = -0.24, *SE* = 0.351, *z* = -0.694, *p* = 0.488
- **Cardinality4 vs Cardinality1**: *β* = -0.50, *SE* = 0.362, *z* = -1.378, *p* = 0.168
- **Cardinality5 vs Cardinality1**: *β* = -0.73, *SE* = 0.347, *z* = -2.112, *p* = 0.035
- **Cardinality6 vs Cardinality1**: *β* = -0.46, *SE* = 0.371, *z* = -1.225, *p* = 0.221
- **SNR**: *β* = 0.77, *SE* = 0.069, *z* = 11.175, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.27 | 0.36 | 0.74 | 0.462 | 0.998 | n.s. |
| Cardinality1 - Cardinality3 | 0.24 | 0.35 | 0.69 | 0.488 | 0.998 | n.s. |
| Cardinality1 - Cardinality4 | 0.50 | 0.36 | 1.38 | 0.168 | 0.924 | n.s. |
| Cardinality1 - Cardinality5 | 0.73 | 0.35 | 2.11 | 0.035 | 0.411 | n.s. |
| Cardinality1 - Cardinality6 | 0.45 | 0.37 | 1.22 | 0.221 | 0.950 | n.s. |
| Cardinality2 - Cardinality3 | -0.02 | 0.39 | -0.06 | 0.949 | 0.998 | n.s. |
| Cardinality2 - Cardinality4 | 0.23 | 0.40 | 0.57 | 0.568 | 0.998 | n.s. |
| Cardinality2 - Cardinality5 | 0.46 | 0.39 | 1.20 | 0.230 | 0.950 | n.s. |
| Cardinality2 - Cardinality6 | 0.19 | 0.40 | 0.46 | 0.644 | 0.998 | n.s. |
| Cardinality3 - Cardinality4 | 0.25 | 0.39 | 0.65 | 0.518 | 0.998 | n.s. |
| Cardinality3 - Cardinality5 | 0.49 | 0.38 | 1.29 | 0.196 | 0.942 | n.s. |
| Cardinality3 - Cardinality6 | 0.21 | 0.39 | 0.54 | 0.587 | 0.998 | n.s. |
| Cardinality4 - Cardinality5 | 0.23 | 0.39 | 0.61 | 0.545 | 0.998 | n.s. |
| Cardinality4 - Cardinality6 | -0.04 | 0.41 | -0.11 | 0.915 | 0.998 | n.s. |
| Cardinality5 - Cardinality6 | -0.28 | 0.38 | -0.72 | 0.470 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.456, η²_G = 0.110
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 2.14 | 5 | = 0.812 | 0.58 [-0.21, 1.13] | medium | n.s. |
| Cardinality1 vs Cardinality3 | 1.24 | 5 | = 0.812 | 0.74 [-0.41, 0.88] | medium | n.s. |
| Cardinality1 vs Cardinality4 | 1.45 | 5 | = 0.812 | 0.55 [-0.23, 1.10] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 1.29 | 5 | = 0.812 | 0.77 [-0.30, 0.94] | medium | n.s. |
| Cardinality1 vs Cardinality6 | 1.34 | 5 | = 0.812 | 0.61 [-0.21, 1.32] | medium | n.s. |
| Cardinality2 vs Cardinality3 | 0.40 | 5 | = 0.924 | 0.21 [-0.92, 0.52] | small | n.s. |
| Cardinality2 vs Cardinality4 | -0.37 | 5 | = 0.924 | -0.10 [-1.26, 0.35] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 0.41 | 5 | = 0.924 | 0.27 [-0.58, 0.86] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.16 | 5 | = 0.924 | 0.08 [-0.68, 1.00] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.77 | 5 | = 0.924 | -0.35 [-1.10, 0.60] | small | n.s. |
| Cardinality3 vs Cardinality5 | 0.10 | 5 | = 0.924 | 0.07 [-0.61, 0.94] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -0.24 | 5 | = 0.924 | -0.11 [-0.56, 1.00] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.58 | 5 | = 0.924 | 0.41 [-0.51, 0.94] | small | n.s. |
| Cardinality4 vs Cardinality6 | 0.54 | 5 | = 0.924 | 0.18 [-0.82, 0.85] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -0.26 | 5 | = 0.924 | -0.16 [-0.66, 0.69] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 505.55, BIC = 527.32
- **Cardinality2 vs Cardinality1**: *β* = -0.81, *SE* = 1.617, *z* = -0.502, *p* = 0.615
- **Cardinality3 vs Cardinality1**: *β* = -1.56, *SE* = 1.546, *z* = -1.011, *p* = 0.312
- **Cardinality4 vs Cardinality1**: *β* = -2.77, *SE* = 1.607, *z* = -1.727, *p* = 0.084
- **Cardinality5 vs Cardinality1**: *β* = -3.30, *SE* = 1.534, *z* = -2.151, *p* = 0.031
- **Cardinality6 vs Cardinality1**: *β* = -1.63, *SE* = 1.625, *z* = -1.005, *p* = 0.315
- **SNR**: *β* = 0.28, *SE* = 0.290, *z* = 0.963, *p* = 0.336

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.81 | 1.62 | 0.50 | 0.615 | 0.992 | n.s. |
| Cardinality1 - Cardinality3 | 1.56 | 1.55 | 1.01 | 0.312 | 0.979 | n.s. |
| Cardinality1 - Cardinality4 | 2.77 | 1.61 | 1.73 | 0.084 | 0.708 | n.s. |
| Cardinality1 - Cardinality5 | 3.30 | 1.53 | 2.15 | 0.031 | 0.381 | n.s. |
| Cardinality1 - Cardinality6 | 1.63 | 1.63 | 1.00 | 0.315 | 0.979 | n.s. |
| Cardinality2 - Cardinality3 | 0.75 | 1.72 | 0.44 | 0.663 | 0.992 | n.s. |
| Cardinality2 - Cardinality4 | 1.96 | 1.79 | 1.09 | 0.274 | 0.979 | n.s. |
| Cardinality2 - Cardinality5 | 2.49 | 1.72 | 1.45 | 0.148 | 0.876 | n.s. |
| Cardinality2 - Cardinality6 | 0.82 | 1.79 | 0.46 | 0.646 | 0.992 | n.s. |
| Cardinality3 - Cardinality4 | 1.21 | 1.73 | 0.70 | 0.484 | 0.990 | n.s. |
| Cardinality3 - Cardinality5 | 1.74 | 1.66 | 1.05 | 0.296 | 0.979 | n.s. |
| Cardinality3 - Cardinality6 | 0.07 | 1.72 | 0.04 | 0.967 | 0.992 | n.s. |
| Cardinality4 - Cardinality5 | 0.53 | 1.71 | 0.31 | 0.759 | 0.992 | n.s. |
| Cardinality4 - Cardinality6 | -1.14 | 1.79 | -0.64 | 0.525 | 0.990 | n.s. |
| Cardinality5 - Cardinality6 | -1.67 | 1.71 | -0.97 | 0.330 | 0.979 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.10, *p* = 0.099, η²_G = 0.180
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.93 | 5 | = 0.543 | 0.65 [-0.57, 0.71] | medium | n.s. |
| Cardinality1 vs Cardinality3 | 1.87 | 5 | = 0.480 | 0.93 [-0.26, 1.07] | large | n.s. |
| Cardinality1 vs Cardinality4 | 1.19 | 5 | = 0.480 | 0.55 [-0.10, 1.27] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 2.48 | 5 | = 0.480 | 1.21 [-0.26, 0.99] | large | n.s. |
| Cardinality1 vs Cardinality6 | 0.87 | 5 | = 0.543 | 0.32 [-0.49, 0.97] | small | n.s. |
| Cardinality2 vs Cardinality3 | 0.85 | 5 | = 0.543 | 0.49 [-0.34, 1.15] | small | n.s. |
| Cardinality2 vs Cardinality4 | -0.25 | 5 | = 0.816 | -0.10 [-0.38, 1.22] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 1.36 | 5 | = 0.480 | 0.83 [-0.37, 1.11] | large | n.s. |
| Cardinality2 vs Cardinality6 | -0.27 | 5 | = 0.816 | -0.14 [-0.73, 0.95] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -1.21 | 5 | = 0.480 | -0.56 [-1.07, 0.63] | medium | n.s. |
| Cardinality3 vs Cardinality5 | 1.43 | 5 | = 0.480 | 0.31 [-0.40, 1.20] | small | n.s. |
| Cardinality3 vs Cardinality6 | -1.30 | 5 | = 0.480 | -0.50 [-0.63, 0.91] | medium | n.s. |
| Cardinality4 vs Cardinality5 | 1.68 | 5 | = 0.480 | 0.88 [-0.53, 0.91] | large | n.s. |
| Cardinality4 vs Cardinality6 | -0.25 | 5 | = 0.816 | -0.07 [-1.40, 0.38] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -1.90 | 5 | = 0.480 | -0.78 [-1.23, 0.20] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.55, BIC = 297.21
- **Cardinality2 vs Cardinality1**: *β* = 0.21, *SE* = 0.397, *z* = 0.520, *p* = 0.603
- **Cardinality3 vs Cardinality1**: *β* = 0.19, *SE* = 0.395, *z* = 0.480, *p* = 0.631
- **Cardinality4 vs Cardinality1**: *β* = 0.85, *SE* = 0.427, *z* = 1.999, *p* = 0.046
- **Cardinality5 vs Cardinality1**: *β* = -0.32, *SE* = 0.395, *z* = -0.811, *p* = 0.417
- **Cardinality6 vs Cardinality1**: *β* = 0.40, *SE* = 0.405, *z* = 0.995, *p* = 0.320
- **SNR**: *β* = 0.74, *SE* = 0.070, *z* = 10.480, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | -0.21 | 0.40 | -0.52 | 0.603 | 0.985 | n.s. |
| Cardinality1 - Cardinality3 | -0.19 | 0.39 | -0.48 | 0.631 | 0.985 | n.s. |
| Cardinality1 - Cardinality4 | -0.85 | 0.43 | -2.00 | 0.046 | 0.479 | n.s. |
| Cardinality1 - Cardinality5 | 0.32 | 0.40 | 0.81 | 0.417 | 0.961 | n.s. |
| Cardinality1 - Cardinality6 | -0.40 | 0.41 | -1.00 | 0.320 | 0.933 | n.s. |
| Cardinality2 - Cardinality3 | 0.02 | 0.38 | 0.04 | 0.965 | 0.985 | n.s. |
| Cardinality2 - Cardinality4 | -0.65 | 0.43 | -1.52 | 0.130 | 0.783 | n.s. |
| Cardinality2 - Cardinality5 | 0.53 | 0.39 | 1.36 | 0.173 | 0.850 | n.s. |
| Cardinality2 - Cardinality6 | -0.20 | 0.40 | -0.49 | 0.622 | 0.985 | n.s. |
| Cardinality3 - Cardinality4 | -0.66 | 0.41 | -1.62 | 0.105 | 0.734 | n.s. |
| Cardinality3 - Cardinality5 | 0.51 | 0.37 | 1.36 | 0.173 | 0.850 | n.s. |
| Cardinality3 - Cardinality6 | -0.21 | 0.38 | -0.57 | 0.570 | 0.985 | n.s. |
| Cardinality4 - Cardinality5 | 1.17 | 0.41 | 2.85 | 0.004 | 0.065 | n.s. |
| Cardinality4 - Cardinality6 | 0.45 | 0.41 | 1.10 | 0.273 | 0.922 | n.s. |
| Cardinality5 - Cardinality6 | -0.72 | 0.39 | -1.85 | 0.065 | 0.580 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.907, η²_G = 0.189
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.88 | 1 | = 0.990 | 0.79 [-0.97, 0.48] | medium | n.s. |
| Cardinality1 vs Cardinality3 | -0.13 | 1 | = 0.990 | -0.18 [-1.30, 0.15] | negligible | n.s. |
| Cardinality1 vs Cardinality4 | -7.44 | 1 | = 0.990 | -0.06 [-2.25, 0.30] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | -0.03 | 1 | = 0.990 | -0.04 [-1.23, 0.38] | negligible | n.s. |
| Cardinality1 vs Cardinality6 | -0.98 | 1 | = 0.990 | -0.45 [-1.57, 0.05] | small | n.s. |
| Cardinality2 vs Cardinality3 | -0.73 | 1 | = 0.990 | -0.98 [-0.95, 0.35] | large | n.s. |
| Cardinality2 vs Cardinality4 | -2.09 | 1 | = 0.990 | -0.87 [-1.84, 0.48] | large | n.s. |
| Cardinality2 vs Cardinality5 | -0.78 | 1 | = 0.990 | -1.10 [-0.45, 0.91] | large | n.s. |
| Cardinality2 vs Cardinality6 | -1.27 | 1 | = 0.990 | -0.91 [-0.99, 0.56] | large | n.s. |
| Cardinality3 vs Cardinality4 | 0.09 | 1 | = 0.990 | 0.13 [-0.82, 0.85] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | 0.57 | 1 | = 0.990 | 0.17 [-0.11, 1.26] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -0.24 | 1 | = 0.990 | -0.32 [-0.74, 0.69] | small | n.s. |
| Cardinality4 vs Cardinality5 | 0.02 | 1 | = 0.990 | 0.02 [-0.56, 1.14] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -0.90 | 1 | = 0.990 | -0.41 [-0.90, 0.65] | small | n.s. |
| Cardinality5 vs Cardinality6 | -0.35 | 1 | = 0.990 | -0.45 [-1.19, 0.41] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 563.83, BIC = 585.49
- **Cardinality2 vs Cardinality1**: *β* = -0.08, *SE* = 2.605, *z* = -0.031, *p* = 0.975
- **Cardinality3 vs Cardinality1**: *β* = 0.51, *SE* = 2.565, *z* = 0.200, *p* = 0.841
- **Cardinality4 vs Cardinality1**: *β* = -0.54, *SE* = 2.780, *z* = -0.196, *p* = 0.845
- **Cardinality5 vs Cardinality1**: *β* = -1.07, *SE* = 2.554, *z* = -0.419, *p* = 0.675
- **Cardinality6 vs Cardinality1**: *β* = 4.67, *SE* = 2.656, *z* = 1.758, *p* = 0.079
- **SNR**: *β* = 0.53, *SE* = 0.405, *z* = 1.301, *p* = 0.193

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.08 | 2.60 | 0.03 | 0.975 | 1.000 | n.s. |
| Cardinality1 - Cardinality3 | -0.51 | 2.57 | -0.20 | 0.841 | 1.000 | n.s. |
| Cardinality1 - Cardinality4 | 0.54 | 2.78 | 0.20 | 0.845 | 1.000 | n.s. |
| Cardinality1 - Cardinality5 | 1.07 | 2.55 | 0.42 | 0.675 | 1.000 | n.s. |
| Cardinality1 - Cardinality6 | -4.67 | 2.66 | -1.76 | 0.079 | 0.627 | n.s. |
| Cardinality2 - Cardinality3 | -0.59 | 2.52 | -0.24 | 0.813 | 1.000 | n.s. |
| Cardinality2 - Cardinality4 | 0.46 | 2.78 | 0.17 | 0.868 | 1.000 | n.s. |
| Cardinality2 - Cardinality5 | 0.99 | 2.57 | 0.39 | 0.700 | 1.000 | n.s. |
| Cardinality2 - Cardinality6 | -4.75 | 2.61 | -1.82 | 0.069 | 0.605 | n.s. |
| Cardinality3 - Cardinality4 | 1.06 | 2.66 | 0.40 | 0.691 | 1.000 | n.s. |
| Cardinality3 - Cardinality5 | 1.58 | 2.47 | 0.64 | 0.522 | 0.999 | n.s. |
| Cardinality3 - Cardinality6 | -4.15 | 2.46 | -1.69 | 0.091 | 0.648 | n.s. |
| Cardinality4 - Cardinality5 | 0.53 | 2.72 | 0.19 | 0.847 | 1.000 | n.s. |
| Cardinality4 - Cardinality6 | -5.21 | 2.71 | -1.92 | 0.054 | 0.543 | n.s. |
| Cardinality5 - Cardinality6 | -5.74 | 2.57 | -2.24 | 0.025 | 0.320 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.79, *p* = 0.269, η²_G = 0.519
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.55 | 1 | = 0.785 | 0.69 [-0.40, 1.07] | medium | n.s. |
| Cardinality1 vs Cardinality3 | 1.44 | 1 | = 0.713 | 1.75 [-0.62, 0.72] | large | n.s. |
| Cardinality1 vs Cardinality4 | 2.74 | 1 | = 0.669 | 3.59 [-1.58, 0.63] | large | n.s. |
| Cardinality1 vs Cardinality5 | 4.43 | 1 | = 0.535 | 2.58 [-0.84, 0.70] | large | n.s. |
| Cardinality1 vs Cardinality6 | -0.25 | 1 | = 0.902 | -0.31 [-1.66, 0.00] | small | n.s. |
| Cardinality2 vs Cardinality3 | 5.08 | 1 | = 0.535 | 1.00 [-0.90, 0.39] | large | n.s. |
| Cardinality2 vs Cardinality4 | 0.64 | 1 | = 0.785 | 0.54 [-0.77, 1.38] | medium | n.s. |
| Cardinality2 vs Cardinality5 | 0.16 | 1 | = 0.902 | 0.17 [-0.54, 0.81] | negligible | n.s. |
| Cardinality2 vs Cardinality6 | -4.39 | 1 | = 0.535 | -0.70 [-1.43, 0.24] | medium | n.s. |
| Cardinality3 vs Cardinality4 | -0.93 | 1 | = 0.713 | -0.83 [-0.51, 1.21] | large | n.s. |
| Cardinality3 vs Cardinality5 | -1.02 | 1 | = 0.713 | -1.11 [-0.52, 0.75] | large | n.s. |
| Cardinality3 vs Cardinality6 | -40.54 | 1 | = 0.236 | -1.52 [-1.94, -0.16] | large | n.s. |
| Cardinality4 vs Cardinality5 | -1.43 | 1 | = 0.713 | -2.01 [-1.19, 0.53] | large | n.s. |
| Cardinality4 vs Cardinality6 | -1.50 | 1 | = 0.713 | -1.33 [-1.40, 0.26] | large | n.s. |
| Cardinality5 vs Cardinality6 | -0.94 | 1 | = 0.713 | -1.03 [-1.94, -0.06] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P1 latency:** Marginal trend toward condition differences (*p* = 0.099)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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
