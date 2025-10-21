# Statistical Analysis Report: tables

**Generated:** 2025-10-20 22:50:25

---

## 1. Analysis Overview

**Total Measurements:** 360
**Number of Subjects:** 24
**Number of Conditions:** 5

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
| from 2 | 24 | -3.37 µV | 1.66 | 0.34 | [-6.66, -0.03] |
| from 3 | 23 | -3.61 µV | 1.70 | 0.35 | [-8.10, -0.12] |
| from 4 | 23 | -3.88 µV | 1.94 | 0.41 | [-8.93, -0.83] |
| from 5 | 23 | -4.07 µV | 1.85 | 0.38 | [-8.04, -0.59] |
| from 6 | 24 | -3.61 µV | 1.80 | 0.37 | [-7.04, -1.01] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 24 | 173.67 ms | 9.52 | 1.94 | [155.77, 195.06] |
| from 3 | 23 | 171.49 ms | 9.33 | 1.95 | [156.25, 202.17] |
| from 4 | 23 | 171.30 ms | 6.91 | 1.44 | [155.42, 186.68] |
| from 5 | 23 | 172.96 ms | 7.00 | 1.46 | [154.85, 186.81] |
| from 6 | 24 | 173.08 ms | 9.94 | 2.03 | [157.60, 196.19] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 14 | 1.16 µV | 1.24 | 0.33 | [0.13, 3.80] |
| from 3 | 14 | 1.28 µV | 1.55 | 0.42 | [0.14, 5.81] |
| from 4 | 9 | 1.82 µV | 1.12 | 0.37 | [0.23, 3.64] |
| from 5 | 15 | 1.37 µV | 1.01 | 0.26 | [0.16, 3.05] |
| from 6 | 13 | 1.62 µV | 1.46 | 0.40 | [0.12, 5.79] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 14 | 102.41 ms | 4.60 | 1.23 | [93.03, 109.31] |
| from 3 | 14 | 103.40 ms | 4.14 | 1.11 | [97.20, 109.50] |
| from 4 | 9 | 104.07 ms | 2.49 | 0.83 | [100.98, 109.16] |
| from 5 | 15 | 103.06 ms | 4.36 | 1.13 | [93.87, 109.79] |
| from 6 | 13 | 104.02 ms | 3.82 | 1.06 | [93.33, 108.46] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 19 | 2.97 µV | 2.01 | 0.46 | [0.16, 6.28] |
| from 3 | 18 | 3.12 µV | 2.05 | 0.48 | [0.65, 7.39] |
| from 4 | 19 | 2.72 µV | 2.00 | 0.46 | [0.06, 6.82] |
| from 5 | 18 | 2.56 µV | 1.63 | 0.38 | [0.05, 5.36] |
| from 6 | 18 | 2.55 µV | 1.88 | 0.44 | [0.06, 6.21] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| from 2 | 19 | 472.44 ms | 13.25 | 3.04 | [430.74, 492.79] |
| from 3 | 18 | 475.50 ms | 10.21 | 2.41 | [457.90, 490.18] |
| from 4 | 19 | 478.41 ms | 19.46 | 4.46 | [425.11, 520.46] |
| from 5 | 18 | 473.37 ms | 10.66 | 2.51 | [446.77, 486.80] |
| from 6 | 18 | 474.66 ms | 20.89 | 4.92 | [426.95, 523.62] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 330.99, BIC = 353.09
- **from 3 vs from 2**: *β* = -0.09, *SE* = 0.200, *z* = -0.451, *p* = 0.652
- **from 4 vs from 2**: *β* = -0.38, *SE* = 0.199, *z* = -1.892, *p* = 0.058
- **from 5 vs from 2**: *β* = -0.50, *SE* = 0.201, *z* = -2.472, *p* = 0.013
- **from 6 vs from 2**: *β* = -0.28, *SE* = 0.196, *z* = -1.402, *p* = 0.161
- **SNR**: *β* = -0.07, *SE* = 0.014, *z* = -4.937, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.09 | 0.20 | 0.45 | 0.652 | 0.912 | n.s. |
| from 2 - from 4 | 0.38 | 0.20 | 1.89 | 0.058 | 0.382 | n.s. |
| from 2 - from 5 | 0.50 | 0.20 | 2.47 | 0.013 | 0.126 | n.s. |
| from 2 - from 6 | 0.28 | 0.20 | 1.40 | 0.161 | 0.684 | n.s. |
| from 3 - from 4 | 0.29 | 0.20 | 1.43 | 0.152 | 0.684 | n.s. |
| from 3 - from 5 | 0.41 | 0.20 | 2.02 | 0.043 | 0.327 | n.s. |
| from 3 - from 6 | 0.19 | 0.20 | 0.93 | 0.355 | 0.827 | n.s. |
| from 4 - from 5 | 0.12 | 0.20 | 0.59 | 0.555 | 0.912 | n.s. |
| from 4 - from 6 | -0.10 | 0.20 | -0.51 | 0.609 | 0.912 | n.s. |
| from 5 - from 6 | -0.22 | 0.20 | -1.10 | 0.273 | 0.797 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.28, *p* = 0.067, η²_G = 0.015
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 0.69 | 22 | = 0.610 | 0.09 [-0.29, 0.58] | negligible | n.s. |
| from 2 vs from 4 | 2.04 | 22 | = 0.164 | 0.24 [-0.03, 0.88] | small | n.s. |
| from 2 vs from 5 | 2.63 | 22 | = 0.152 | 0.35 [0.08, 1.01] | small | n.s. |
| from 2 vs from 6 | 1.24 | 22 | = 0.383 | 0.16 [-0.19, 0.66] | negligible | n.s. |
| from 3 vs from 4 | 1.38 | 22 | = 0.362 | 0.15 [-0.15, 0.73] | negligible | n.s. |
| from 3 vs from 5 | 1.94 | 22 | = 0.164 | 0.26 [-0.05, 0.85] | small | n.s. |
| from 3 vs from 6 | 0.52 | 22 | = 0.610 | 0.07 [-0.33, 0.54] | negligible | n.s. |
| from 4 vs from 5 | 0.76 | 22 | = 0.610 | 0.10 [-0.28, 0.59] | negligible | n.s. |
| from 4 vs from 6 | -0.60 | 22 | = 0.610 | -0.09 [-0.56, 0.31] | negligible | n.s. |
| from 5 vs from 6 | -2.02 | 22 | = 0.164 | -0.20 [-0.87, 0.03] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 707.09, BIC = 729.19
- **from 3 vs from 2**: *β* = -1.27, *SE* = 0.950, *z* = -1.337, *p* = 0.181
- **from 4 vs from 2**: *β* = -1.46, *SE* = 0.949, *z* = -1.541, *p* = 0.123
- **from 5 vs from 2**: *β* = 0.20, *SE* = 0.955, *z* = 0.211, *p* = 0.833
- **from 6 vs from 2**: *β* = -0.59, *SE* = 0.934, *z* = -0.630, *p* = 0.528
- **SNR**: *β* = -0.00, *SE* = 0.068, *z* = -0.038, *p* = 0.969

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 1.27 | 0.95 | 1.34 | 0.181 | 0.753 | n.s. |
| from 2 - from 4 | 1.46 | 0.95 | 1.54 | 0.123 | 0.694 | n.s. |
| from 2 - from 5 | -0.20 | 0.96 | -0.21 | 0.833 | 0.972 | n.s. |
| from 2 - from 6 | 0.59 | 0.93 | 0.63 | 0.528 | 0.930 | n.s. |
| from 3 - from 4 | 0.19 | 0.95 | 0.20 | 0.840 | 0.972 | n.s. |
| from 3 - from 5 | -1.47 | 0.96 | -1.54 | 0.123 | 0.694 | n.s. |
| from 3 - from 6 | -0.68 | 0.95 | -0.72 | 0.474 | 0.930 | n.s. |
| from 4 - from 5 | -1.66 | 0.96 | -1.74 | 0.082 | 0.574 | n.s. |
| from 4 - from 6 | -0.87 | 0.95 | -0.92 | 0.358 | 0.930 | n.s. |
| from 5 - from 6 | 0.79 | 0.96 | 0.82 | 0.410 | 0.930 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.13, *p* = 0.349, η²_G = 0.007
- Greenhouse-Geisser corrected: *p* = 0.344 (ε = 0.721)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 1.20 | 22 | = 0.607 | 0.14 [-0.19, 0.69] | negligible | n.s. |
| from 2 vs from 4 | 1.69 | 22 | = 0.529 | 0.18 [-0.09, 0.80] | negligible | n.s. |
| from 2 vs from 5 | -0.24 | 22 | = 0.862 | -0.03 [-0.48, 0.38] | negligible | n.s. |
| from 2 vs from 6 | 0.81 | 22 | = 0.609 | 0.08 [-0.27, 0.58] | negligible | n.s. |
| from 3 vs from 4 | 0.18 | 22 | = 0.862 | 0.02 [-0.40, 0.47] | negligible | n.s. |
| from 3 vs from 5 | -1.43 | 22 | = 0.558 | -0.18 [-0.74, 0.14] | negligible | n.s. |
| from 3 vs from 6 | -0.44 | 22 | = 0.833 | -0.06 [-0.52, 0.34] | negligible | n.s. |
| from 4 vs from 5 | -2.73 | 22 | = 0.122 | -0.24 [-1.04, -0.10] | small | n.s. |
| from 4 vs from 6 | -0.88 | 22 | = 0.609 | -0.10 [-0.62, 0.25] | negligible | n.s. |
| from 5 vs from 6 | 0.87 | 22 | = 0.609 | 0.11 [-0.26, 0.62] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 175.25, BIC = 192.65
- **from 3 vs from 2**: *β* = 0.02, *SE* = 0.265, *z* = 0.070, *p* = 0.944
- **from 4 vs from 2**: *β* = 0.32, *SE* = 0.299, *z* = 1.075, *p* = 0.283
- **from 5 vs from 2**: *β* = 0.18, *SE* = 0.267, *z* = 0.669, *p* = 0.503
- **from 6 vs from 2**: *β* = 0.26, *SE* = 0.274, *z* = 0.951, *p* = 0.342
- **SNR**: *β* = 0.20, *SE* = 0.045, *z* = 4.390, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.02 | 0.26 | -0.07 | 0.944 | 0.985 | n.s. |
| from 2 - from 4 | -0.32 | 0.30 | -1.07 | 0.283 | 0.964 | n.s. |
| from 2 - from 5 | -0.18 | 0.27 | -0.67 | 0.503 | 0.985 | n.s. |
| from 2 - from 6 | -0.26 | 0.27 | -0.95 | 0.342 | 0.965 | n.s. |
| from 3 - from 4 | -0.30 | 0.30 | -1.01 | 0.311 | 0.965 | n.s. |
| from 3 - from 5 | -0.16 | 0.26 | -0.61 | 0.544 | 0.985 | n.s. |
| from 3 - from 6 | -0.24 | 0.27 | -0.90 | 0.368 | 0.965 | n.s. |
| from 4 - from 5 | 0.14 | 0.30 | 0.47 | 0.638 | 0.985 | n.s. |
| from 4 - from 6 | 0.06 | 0.31 | 0.20 | 0.845 | 0.985 | n.s. |
| from 5 - from 6 | -0.08 | 0.26 | -0.31 | 0.754 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.28, *p* = 0.885, η²_G = 0.023
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.49 | 4 | = 0.988 | -0.20 [-0.76, 0.58] | small | n.s. |
| from 2 vs from 4 | 0.32 | 4 | = 0.988 | 0.13 [-1.14, 0.57] | negligible | n.s. |
| from 2 vs from 5 | -0.48 | 4 | = 0.988 | -0.25 [-0.87, 0.57] | small | n.s. |
| from 2 vs from 6 | -0.68 | 4 | = 0.988 | -0.20 [-1.19, 0.31] | small | n.s. |
| from 3 vs from 4 | 0.69 | 4 | = 0.988 | 0.33 [-0.88, 0.79] | small | n.s. |
| from 3 vs from 5 | 0.09 | 4 | = 0.988 | 0.04 [-0.89, 0.55] | negligible | n.s. |
| from 3 vs from 6 | -0.02 | 4 | = 0.988 | -0.00 [-1.13, 0.36] | negligible | n.s. |
| from 4 vs from 5 | -2.25 | 4 | = 0.879 | -0.65 [-2.12, 0.14] | medium | n.s. |
| from 4 vs from 6 | -0.72 | 4 | = 0.988 | -0.34 [-1.27, 0.63] | small | n.s. |
| from 5 vs from 6 | -0.09 | 4 | = 0.988 | -0.05 [-0.84, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 361.38, BIC = 378.77
- **from 3 vs from 2**: *β* = 0.65, *SE* = 1.042, *z* = 0.628, *p* = 0.530
- **from 4 vs from 2**: *β* = 1.02, *SE* = 1.174, *z* = 0.866, *p* = 0.386
- **from 5 vs from 2**: *β* = 0.57, *SE* = 1.051, *z* = 0.544, *p* = 0.586
- **from 6 vs from 2**: *β* = 1.36, *SE* = 1.077, *z* = 1.268, *p* = 0.205
- **SNR**: *β* = 0.03, *SE* = 0.164, *z* = 0.150, *p* = 0.881

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -0.65 | 1.04 | -0.63 | 0.530 | 0.992 | n.s. |
| from 2 - from 4 | -1.02 | 1.17 | -0.87 | 0.386 | 0.988 | n.s. |
| from 2 - from 5 | -0.57 | 1.05 | -0.54 | 0.586 | 0.992 | n.s. |
| from 2 - from 6 | -1.36 | 1.08 | -1.27 | 0.205 | 0.899 | n.s. |
| from 3 - from 4 | -0.36 | 1.17 | -0.31 | 0.755 | 0.993 | n.s. |
| from 3 - from 5 | 0.08 | 1.04 | 0.08 | 0.937 | 0.993 | n.s. |
| from 3 - from 6 | -0.71 | 1.06 | -0.67 | 0.501 | 0.992 | n.s. |
| from 4 - from 5 | 0.45 | 1.19 | 0.37 | 0.708 | 0.993 | n.s. |
| from 4 - from 6 | -0.35 | 1.21 | -0.29 | 0.773 | 0.993 | n.s. |
| from 5 - from 6 | -0.79 | 1.03 | -0.77 | 0.443 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.39, *p* = 0.094, η²_G = 0.073
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | 1.42 | 4 | = 0.326 | 0.27 [-0.58, 0.77] | small | n.s. |
| from 2 vs from 4 | 1.87 | 4 | = 0.326 | 0.50 [-0.90, 0.77] | medium | n.s. |
| from 2 vs from 5 | 1.75 | 4 | = 0.326 | 0.63 [-0.97, 0.48] | medium | n.s. |
| from 2 vs from 6 | 0.27 | 4 | = 0.798 | 0.04 [-1.14, 0.35] | negligible | n.s. |
| from 3 vs from 4 | 1.80 | 4 | = 0.326 | 0.29 [-0.86, 0.81] | small | n.s. |
| from 3 vs from 5 | 1.99 | 4 | = 0.326 | 0.43 [-0.75, 0.69] | small | n.s. |
| from 3 vs from 6 | -1.05 | 4 | = 0.441 | -0.22 [-0.90, 0.54] | small | n.s. |
| from 4 vs from 5 | 0.31 | 4 | = 0.798 | 0.06 [-0.65, 1.24] | negligible | n.s. |
| from 4 vs from 6 | -1.56 | 4 | = 0.326 | -0.46 [-1.79, 0.30] | small | n.s. |
| from 5 vs from 6 | -1.50 | 4 | = 0.326 | -0.58 [-0.79, 0.55] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 262.46, BIC = 282.63
- **from 3 vs from 2**: *β* = -0.09, *SE* = 0.222, *z* = -0.421, *p* = 0.674
- **from 4 vs from 2**: *β* = -0.32, *SE* = 0.219, *z* = -1.439, *p* = 0.150
- **from 5 vs from 2**: *β* = -0.45, *SE* = 0.223, *z* = -2.035, *p* = 0.042
- **from 6 vs from 2**: *β* = -0.52, *SE* = 0.220, *z* = -2.346, *p* = 0.019
- **SNR**: *β* = 0.13, *SE* = 0.019, *z* = 6.974, *p* < .001

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | 0.09 | 0.22 | 0.42 | 0.674 | 0.898 | n.s. |
| from 2 - from 4 | 0.32 | 0.22 | 1.44 | 0.150 | 0.623 | n.s. |
| from 2 - from 5 | 0.45 | 0.22 | 2.03 | 0.042 | 0.319 | n.s. |
| from 2 - from 6 | 0.52 | 0.22 | 2.35 | 0.019 | 0.174 | n.s. |
| from 3 - from 4 | 0.22 | 0.22 | 1.01 | 0.311 | 0.845 | n.s. |
| from 3 - from 5 | 0.36 | 0.23 | 1.60 | 0.110 | 0.559 | n.s. |
| from 3 - from 6 | 0.42 | 0.22 | 1.91 | 0.056 | 0.370 | n.s. |
| from 4 - from 5 | 0.14 | 0.22 | 0.62 | 0.532 | 0.898 | n.s. |
| from 4 - from 6 | 0.20 | 0.22 | 0.92 | 0.359 | 0.845 | n.s. |
| from 5 - from 6 | 0.06 | 0.22 | 0.29 | 0.774 | 0.898 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.77, *p* = 0.146, η²_G = 0.019
- Greenhouse-Geisser corrected: *p* = 0.181 (ε = 0.568)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.22 | 16 | = 0.920 | -0.03 [-0.57, 0.43] | negligible | n.s. |
| from 2 vs from 4 | 0.81 | 16 | = 0.539 | 0.09 [-0.30, 0.71] | negligible | n.s. |
| from 2 vs from 5 | 2.94 | 16 | = 0.096 | 0.30 [0.14, 1.29] | small | n.s. |
| from 2 vs from 6 | 1.24 | 16 | = 0.389 | 0.28 [-0.22, 0.80] | small | n.s. |
| from 3 vs from 4 | 1.37 | 16 | = 0.378 | 0.12 [-0.14, 0.88] | negligible | n.s. |
| from 3 vs from 5 | 2.36 | 16 | = 0.156 | 0.33 [0.02, 1.13] | small | n.s. |
| from 3 vs from 6 | 1.47 | 16 | = 0.378 | 0.30 [-0.15, 0.87] | small | n.s. |
| from 4 vs from 5 | 1.54 | 16 | = 0.378 | 0.21 [-0.18, 0.84] | small | n.s. |
| from 4 vs from 6 | 0.95 | 16 | = 0.510 | 0.19 [-0.29, 0.72] | negligible | n.s. |
| from 5 vs from 6 | -0.03 | 16 | = 0.979 | -0.01 [-0.52, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 750.39, BIC = 770.56
- **from 3 vs from 2**: *β* = 2.40, *SE* = 3.663, *z* = 0.655, *p* = 0.513
- **from 4 vs from 2**: *β* = 4.86, *SE* = 3.616, *z* = 1.343, *p* = 0.179
- **from 5 vs from 2**: *β* = -1.20, *SE* = 3.677, *z* = -0.328, *p* = 0.743
- **from 6 vs from 2**: *β* = 2.13, *SE* = 3.640, *z* = 0.585, *p* = 0.558
- **SNR**: *β* = 0.50, *SE* = 0.296, *z* = 1.697, *p* = 0.090

_Reference condition: **from 2** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| from 2 - from 3 | -2.40 | 3.66 | -0.65 | 0.513 | 0.974 | n.s. |
| from 2 - from 4 | -4.85 | 3.62 | -1.34 | 0.179 | 0.831 | n.s. |
| from 2 - from 5 | 1.20 | 3.68 | 0.33 | 0.743 | 0.974 | n.s. |
| from 2 - from 6 | -2.13 | 3.64 | -0.59 | 0.558 | 0.974 | n.s. |
| from 3 - from 4 | -2.46 | 3.64 | -0.68 | 0.500 | 0.974 | n.s. |
| from 3 - from 5 | 3.60 | 3.74 | 0.96 | 0.335 | 0.962 | n.s. |
| from 3 - from 6 | 0.27 | 3.68 | 0.07 | 0.942 | 0.974 | n.s. |
| from 4 - from 5 | 6.06 | 3.65 | 1.66 | 0.097 | 0.638 | n.s. |
| from 4 - from 6 | 2.72 | 3.64 | 0.75 | 0.454 | 0.974 | n.s. |
| from 5 - from 6 | -3.34 | 3.71 | -0.90 | 0.368 | 0.962 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.69, *p* = 0.605, η²_G = 0.023
- Greenhouse-Geisser corrected: *p* = 0.510 (ε = 0.496)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| from 2 vs from 3 | -0.49 | 16 | = 0.705 | -0.14 [-0.73, 0.27] | negligible | n.s. |
| from 2 vs from 4 | -2.14 | 16 | = 0.240 | -0.41 [-0.97, 0.07] | small | n.s. |
| from 2 vs from 5 | 0.50 | 16 | = 0.705 | 0.13 [-0.39, 0.64] | negligible | n.s. |
| from 2 vs from 6 | -0.49 | 16 | = 0.705 | -0.14 [-0.64, 0.36] | negligible | n.s. |
| from 3 vs from 4 | -1.06 | 16 | = 0.705 | -0.26 [-0.54, 0.46] | small | n.s. |
| from 3 vs from 5 | 1.17 | 16 | = 0.705 | 0.25 [-0.24, 0.81] | small | n.s. |
| from 3 vs from 6 | -0.12 | 16 | = 0.902 | -0.04 [-0.46, 0.53] | negligible | n.s. |
| from 4 vs from 5 | 2.27 | 16 | = 0.240 | 0.49 [0.03, 1.10] | small | n.s. |
| from 4 vs from 6 | 0.49 | 16 | = 0.705 | 0.14 [-0.42, 0.57] | negligible | n.s. |
| from 5 vs from 6 | -0.68 | 16 | = 0.705 | -0.21 [-0.68, 0.35] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.067)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.094)

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

- Python 3.12.4
- MNE-Python 1.9.0
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
