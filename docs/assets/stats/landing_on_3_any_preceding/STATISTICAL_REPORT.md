# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:45:07

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
| 1 to 3 | 17 | 104.94 ms | 11.36 | 2.76 | [88.00, 116.00] |
| 2 to 3 | 6 | 114.67 ms | 3.27 | 1.33 | [108.00, 116.00] |
| 4 to 3 | 12 | 100.00 ms | 11.05 | 3.19 | [88.00, 116.00] |
| 5 to 3 | 4 | 102.00 ms | 16.17 | 8.08 | [88.00, 116.00] |
| 6 to 3 | 8 | 103.00 ms | 10.64 | 3.76 | [88.00, 116.00] |
| Cardinality3 | 12 | 105.00 ms | 10.94 | 3.16 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 17 | 3.16 µV | 2.33 | 0.57 | [0.49, 9.00] |
| 2 to 3 | 6 | 2.91 µV | 2.04 | 0.83 | [0.58, 6.35] |
| 4 to 3 | 12 | 2.31 µV | 1.20 | 0.35 | [0.44, 4.24] |
| 5 to 3 | 4 | 3.30 µV | 1.44 | 0.72 | [1.38, 4.74] |
| 6 to 3 | 8 | 1.99 µV | 0.52 | 0.18 | [1.49, 2.89] |
| Cardinality3 | 12 | 2.32 µV | 0.86 | 0.25 | [0.99, 3.69] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | 168.83 ms | 22.44 | 4.58 | [140.00, 216.00] |
| 2 to 3 | 22 | 171.45 ms | 19.33 | 4.12 | [140.00, 208.00] |
| 4 to 3 | 23 | 177.74 ms | 20.35 | 4.24 | [148.00, 216.00] |
| 5 to 3 | 24 | 174.33 ms | 16.88 | 3.45 | [140.00, 208.00] |
| 6 to 3 | 23 | 174.96 ms | 16.46 | 3.43 | [152.00, 216.00] |
| Cardinality3 | 23 | 170.43 ms | 19.92 | 4.15 | [140.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 24 | -6.64 µV | 2.55 | 0.52 | [-12.65, -2.71] |
| 2 to 3 | 22 | -5.27 µV | 1.96 | 0.42 | [-10.61, -0.91] |
| 4 to 3 | 23 | -6.43 µV | 2.15 | 0.45 | [-11.27, -1.89] |
| 5 to 3 | 24 | -5.96 µV | 2.70 | 0.55 | [-12.11, -1.76] |
| 6 to 3 | 23 | -6.50 µV | 2.21 | 0.46 | [-10.34, -1.59] |
| Cardinality3 | 23 | -5.17 µV | 1.99 | 0.42 | [-10.83, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 11 | 107.27 ms | 8.55 | 2.58 | [92.00, 116.00] |
| 2 to 3 | 12 | 105.67 ms | 9.57 | 2.76 | [92.00, 116.00] |
| 4 to 3 | 11 | 104.73 ms | 8.36 | 2.52 | [92.00, 116.00] |
| 5 to 3 | 18 | 109.11 ms | 7.36 | 1.74 | [92.00, 116.00] |
| 6 to 3 | 15 | 106.40 ms | 7.68 | 1.98 | [92.00, 116.00] |
| Cardinality3 | 13 | 107.69 ms | 9.16 | 2.54 | [92.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 11 | 3.00 µV | 1.89 | 0.57 | [1.02, 7.47] |
| 2 to 3 | 12 | 3.06 µV | 1.84 | 0.53 | [0.49, 6.87] |
| 4 to 3 | 11 | 2.74 µV | 1.43 | 0.43 | [0.60, 5.30] |
| 5 to 3 | 18 | 2.80 µV | 1.15 | 0.27 | [0.79, 4.61] |
| 6 to 3 | 15 | 2.65 µV | 2.16 | 0.56 | [0.16, 8.17] |
| Cardinality3 | 13 | 3.42 µV | 2.33 | 0.65 | [0.79, 8.96] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 473.40 ms | 38.24 | 8.55 | [404.00, 528.00] |
| 2 to 3 | 15 | 460.00 ms | 53.81 | 13.89 | [388.00, 528.00] |
| 4 to 3 | 19 | 453.89 ms | 43.07 | 9.88 | [388.00, 528.00] |
| 5 to 3 | 20 | 459.80 ms | 33.20 | 7.42 | [400.00, 528.00] |
| 6 to 3 | 19 | 462.11 ms | 36.52 | 8.38 | [396.00, 524.00] |
| Cardinality3 | 15 | 439.47 ms | 38.30 | 9.89 | [388.00, 520.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1 to 3 | 20 | 5.93 µV | 3.64 | 0.81 | [1.71, 15.57] |
| 2 to 3 | 15 | 6.81 µV | 3.24 | 0.84 | [2.51, 13.70] |
| 4 to 3 | 19 | 5.84 µV | 3.02 | 0.69 | [1.17, 11.65] |
| 5 to 3 | 20 | 5.66 µV | 2.34 | 0.52 | [1.54, 10.28] |
| 6 to 3 | 19 | 6.78 µV | 3.04 | 0.70 | [3.51, 14.26] |
| Cardinality3 | 15 | 5.13 µV | 2.02 | 0.52 | [3.31, 9.60] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 458.42, BIC = 477.12
- **2 to 3 vs 1 to 3**: *β* = 8.46, *SE* = 4.624, *z* = 1.829, *p* = 0.067
- **4 to 3 vs 1 to 3**: *β* = -4.12, *SE* = 3.603, *z* = -1.144, *p* = 0.253
- **5 to 3 vs 1 to 3**: *β* = -2.74, *SE* = 5.458, *z* = -0.502, *p* = 0.616
- **6 to 3 vs 1 to 3**: *β* = -0.92, *SE* = 4.161, *z* = -0.220, *p* = 0.826
- **Cardinality3 vs 1 to 3**: *β* = 1.49, *SE* = 3.695, *z* = 0.404, *p* = 0.686
- **SNR**: *β* = 0.87, *SE* = 0.874, *z* = 0.996, *p* = 0.319

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -8.46 | 4.62 | -1.83 | 0.067 | 0.624 | n.s. |
| 1 to 3 - 4 to 3 | 4.12 | 3.60 | 1.14 | 0.253 | 0.927 | n.s. |
| 1 to 3 - 5 to 3 | 2.74 | 5.46 | 0.50 | 0.616 | 0.995 | n.s. |
| 1 to 3 - 6 to 3 | 0.92 | 4.16 | 0.22 | 0.826 | 0.995 | n.s. |
| 1 to 3 - Cardinality3 | -1.49 | 3.69 | -0.40 | 0.686 | 0.995 | n.s. |
| 2 to 3 - 4 to 3 | 12.58 | 5.03 | 2.50 | 0.012 | 0.170 | n.s. |
| 2 to 3 - 5 to 3 | 11.20 | 6.25 | 1.79 | 0.073 | 0.628 | n.s. |
| 2 to 3 - 6 to 3 | 9.37 | 5.35 | 1.75 | 0.080 | 0.631 | n.s. |
| 2 to 3 - Cardinality3 | 6.97 | 4.99 | 1.40 | 0.163 | 0.844 | n.s. |
| 4 to 3 - 5 to 3 | -1.38 | 5.64 | -0.24 | 0.807 | 0.995 | n.s. |
| 4 to 3 - 6 to 3 | -3.20 | 4.33 | -0.74 | 0.460 | 0.992 | n.s. |
| 4 to 3 - Cardinality3 | -5.61 | 3.95 | -1.42 | 0.156 | 0.844 | n.s. |
| 5 to 3 - 6 to 3 | -1.82 | 5.91 | -0.31 | 0.758 | 0.995 | n.s. |
| 5 to 3 - Cardinality3 | -4.23 | 5.65 | -0.75 | 0.454 | 0.992 | n.s. |
| 6 to 3 - Cardinality3 | -2.41 | 4.35 | -0.55 | 0.580 | 0.995 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 203.42, BIC = 222.12
- **2 to 3 vs 1 to 3**: *β* = -0.36, *SE* = 0.532, *z* = -0.672, *p* = 0.502
- **4 to 3 vs 1 to 3**: *β* = -0.23, *SE* = 0.420, *z* = -0.557, *p* = 0.578
- **5 to 3 vs 1 to 3**: *β* = 0.69, *SE* = 0.631, *z* = 1.095, *p* = 0.274
- **6 to 3 vs 1 to 3**: *β* = -0.56, *SE* = 0.484, *z* = -1.166, *p* = 0.244
- **Cardinality3 vs 1 to 3**: *β* = -0.11, *SE* = 0.431, *z* = -0.264, *p* = 0.792
- **SNR**: *β* = 0.68, *SE* = 0.101, *z* = 6.759, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 0.36 | 0.53 | 0.67 | 0.502 | 0.996 | n.s. |
| 1 to 3 - 4 to 3 | 0.23 | 0.42 | 0.56 | 0.578 | 0.996 | n.s. |
| 1 to 3 - 5 to 3 | -0.69 | 0.63 | -1.09 | 0.274 | 0.959 | n.s. |
| 1 to 3 - 6 to 3 | 0.56 | 0.48 | 1.17 | 0.244 | 0.954 | n.s. |
| 1 to 3 - Cardinality3 | 0.11 | 0.43 | 0.26 | 0.792 | 0.996 | n.s. |
| 2 to 3 - 4 to 3 | -0.12 | 0.58 | -0.21 | 0.832 | 0.996 | n.s. |
| 2 to 3 - 5 to 3 | -1.05 | 0.73 | -1.44 | 0.149 | 0.896 | n.s. |
| 2 to 3 - 6 to 3 | 0.21 | 0.62 | 0.34 | 0.737 | 0.996 | n.s. |
| 2 to 3 - Cardinality3 | -0.24 | 0.57 | -0.42 | 0.671 | 0.996 | n.s. |
| 4 to 3 - 5 to 3 | -0.92 | 0.65 | -1.41 | 0.157 | 0.896 | n.s. |
| 4 to 3 - 6 to 3 | 0.33 | 0.50 | 0.66 | 0.512 | 0.996 | n.s. |
| 4 to 3 - Cardinality3 | -0.12 | 0.46 | -0.26 | 0.793 | 0.996 | n.s. |
| 5 to 3 - 6 to 3 | 1.25 | 0.69 | 1.83 | 0.067 | 0.649 | n.s. |
| 5 to 3 - Cardinality3 | 0.80 | 0.65 | 1.23 | 0.218 | 0.948 | n.s. |
| 6 to 3 - Cardinality3 | -0.45 | 0.51 | -0.89 | 0.372 | 0.985 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

_Pairwise test results not available._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1178.91, BIC = 1205.32
- **2 to 3 vs 1 to 3**: *β* = 6.23, *SE* = 4.045, *z* = 1.541, *p* = 0.123
- **4 to 3 vs 1 to 3**: *β* = 9.10, *SE* = 3.880, *z* = 2.345, *p* = 0.019
- **5 to 3 vs 1 to 3**: *β* = 6.48, *SE* = 3.867, *z* = 1.676, *p* = 0.094
- **6 to 3 vs 1 to 3**: *β* = 7.98, *SE* = 3.886, *z* = 2.053, *p* = 0.040
- **Cardinality3 vs 1 to 3**: *β* = 4.16, *SE* = 4.035, *z* = 1.031, *p* = 0.302
- **SNR**: *β* = 0.75, *SE* = 0.503, *z* = 1.496, *p* = 0.135

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -6.23 | 4.04 | -1.54 | 0.123 | 0.794 | n.s. |
| 1 to 3 - 4 to 3 | -9.10 | 3.88 | -2.35 | 0.019 | 0.250 | n.s. |
| 1 to 3 - 5 to 3 | -6.48 | 3.87 | -1.68 | 0.094 | 0.722 | n.s. |
| 1 to 3 - 6 to 3 | -7.98 | 3.89 | -2.05 | 0.040 | 0.436 | n.s. |
| 1 to 3 - Cardinality3 | -4.16 | 4.04 | -1.03 | 0.302 | 0.973 | n.s. |
| 2 to 3 - 4 to 3 | -2.87 | 4.01 | -0.72 | 0.475 | 0.994 | n.s. |
| 2 to 3 - 5 to 3 | -0.25 | 3.93 | -0.06 | 0.949 | 0.994 | n.s. |
| 2 to 3 - 6 to 3 | -1.75 | 3.99 | -0.44 | 0.661 | 0.994 | n.s. |
| 2 to 3 - Cardinality3 | 2.07 | 3.95 | 0.52 | 0.600 | 0.994 | n.s. |
| 4 to 3 - 5 to 3 | 2.62 | 3.87 | 0.68 | 0.498 | 0.994 | n.s. |
| 4 to 3 - 6 to 3 | 1.12 | 3.91 | 0.29 | 0.774 | 0.994 | n.s. |
| 4 to 3 - Cardinality3 | 4.94 | 3.98 | 1.24 | 0.215 | 0.930 | n.s. |
| 5 to 3 - 6 to 3 | -1.50 | 3.87 | -0.39 | 0.698 | 0.994 | n.s. |
| 5 to 3 - Cardinality3 | 2.32 | 3.90 | 0.60 | 0.552 | 0.994 | n.s. |
| 6 to 3 - Cardinality3 | 3.82 | 3.98 | 0.96 | 0.337 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.88, *p* = 0.497, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -1.18 | 20 | = 0.752 | -0.20 [-0.76, 0.14] | small | n.s. |
| 1 to 3 vs 4 to 3 | -1.36 | 20 | = 0.752 | -0.36 [-0.77, 0.12] | small | n.s. |
| 1 to 3 vs 5 to 3 | -1.02 | 20 | = 0.752 | -0.23 [-0.72, 0.15] | small | n.s. |
| 1 to 3 vs 6 to 3 | -1.55 | 20 | = 0.752 | -0.35 [-0.85, 0.05] | small | n.s. |
| 1 to 3 vs Cardinality3 | -0.28 | 20 | = 0.899 | -0.06 [-0.57, 0.30] | negligible | n.s. |
| 2 to 3 vs 4 to 3 | -0.64 | 20 | = 0.752 | -0.16 [-0.60, 0.32] | negligible | n.s. |
| 2 to 3 vs 5 to 3 | -0.05 | 20 | = 0.962 | -0.01 [-0.47, 0.41] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.57 | 20 | = 0.752 | -0.14 [-0.57, 0.32] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 0.65 | 20 | = 0.752 | 0.16 [-0.32, 0.57] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | 0.53 | 20 | = 0.752 | 0.16 [-0.30, 0.57] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | 0.14 | 20 | = 0.950 | 0.03 [-0.39, 0.49] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.25 | 20 | = 0.752 | 0.32 [-0.18, 0.72] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.64 | 20 | = 0.752 | -0.14 [-0.57, 0.30] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.77 | 20 | = 0.752 | 0.19 [-0.27, 0.61] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | 1.54 | 20 | = 0.752 | 0.31 [-0.14, 0.77] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 554.62, BIC = 581.03
- **2 to 3 vs 1 to 3**: *β* = 0.65, *SE* = 0.446, *z* = 1.455, *p* = 0.146
- **4 to 3 vs 1 to 3**: *β* = -0.14, *SE* = 0.430, *z* = -0.325, *p* = 0.745
- **5 to 3 vs 1 to 3**: *β* = 0.17, *SE* = 0.428, *z* = 0.395, *p* = 0.693
- **6 to 3 vs 1 to 3**: *β* = -0.16, *SE* = 0.430, *z* = -0.366, *p* = 0.714
- **Cardinality3 vs 1 to 3**: *β* = 0.57, *SE* = 0.446, *z* = 1.276, *p* = 0.202
- **SNR**: *β* = -0.39, *SE* = 0.054, *z* = -7.263, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.65 | 0.45 | -1.45 | 0.146 | 0.823 | n.s. |
| 1 to 3 - 4 to 3 | 0.14 | 0.43 | 0.32 | 0.745 | 0.997 | n.s. |
| 1 to 3 - 5 to 3 | -0.17 | 0.43 | -0.39 | 0.693 | 0.997 | n.s. |
| 1 to 3 - 6 to 3 | 0.16 | 0.43 | 0.37 | 0.714 | 0.997 | n.s. |
| 1 to 3 - Cardinality3 | -0.57 | 0.45 | -1.28 | 0.202 | 0.895 | n.s. |
| 2 to 3 - 4 to 3 | 0.79 | 0.44 | 1.78 | 0.075 | 0.665 | n.s. |
| 2 to 3 - 5 to 3 | 0.48 | 0.43 | 1.10 | 0.270 | 0.941 | n.s. |
| 2 to 3 - 6 to 3 | 0.81 | 0.44 | 1.83 | 0.068 | 0.650 | n.s. |
| 2 to 3 - Cardinality3 | 0.08 | 0.44 | 0.18 | 0.854 | 0.997 | n.s. |
| 4 to 3 - 5 to 3 | -0.31 | 0.43 | -0.72 | 0.471 | 0.984 | n.s. |
| 4 to 3 - 6 to 3 | 0.02 | 0.43 | 0.04 | 0.967 | 0.997 | n.s. |
| 4 to 3 - Cardinality3 | -0.71 | 0.44 | -1.61 | 0.108 | 0.747 | n.s. |
| 5 to 3 - 6 to 3 | 0.33 | 0.43 | 0.76 | 0.446 | 0.984 | n.s. |
| 5 to 3 - Cardinality3 | -0.40 | 0.43 | -0.93 | 0.354 | 0.970 | n.s. |
| 6 to 3 - Cardinality3 | -0.73 | 0.44 | -1.65 | 0.099 | 0.743 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.90, *p* = 0.017, η²_G = 0.064
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -3.50 | 20 | = 0.017 | -0.63 [-1.17, -0.18] | medium | * |
| 1 to 3 vs 4 to 3 | -0.37 | 20 | = 0.829 | -0.08 [-0.54, 0.33] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.92 | 20 | = 0.555 | -0.25 [-0.63, 0.23] | small | n.s. |
| 1 to 3 vs 6 to 3 | -0.37 | 20 | = 0.829 | -0.09 [-0.50, 0.37] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | -3.49 | 20 | = 0.017 | -0.60 [-1.27, -0.28] | medium | * |
| 2 to 3 vs 4 to 3 | 2.48 | 20 | = 0.085 | 0.61 [0.05, 1.03] | medium | n.s. |
| 2 to 3 vs 5 to 3 | 1.30 | 20 | = 0.440 | 0.34 [-0.14, 0.77] | small | n.s. |
| 2 to 3 vs 6 to 3 | 2.37 | 20 | = 0.085 | 0.59 [0.03, 0.98] | medium | n.s. |
| 2 to 3 vs Cardinality3 | 0.08 | 20 | = 0.966 | 0.02 [-0.48, 0.41] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -1.08 | 20 | = 0.489 | -0.20 [-0.75, 0.14] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.04 | 20 | = 0.966 | -0.01 [-0.44, 0.45] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -2.46 | 20 | = 0.085 | -0.58 [-1.03, -0.07] | medium | n.s. |
| 5 to 3 vs 6 to 3 | 0.79 | 20 | = 0.595 | 0.19 [-0.26, 0.61] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | -1.23 | 20 | = 0.440 | -0.32 [-0.75, 0.14] | small | n.s. |
| 6 to 3 vs Cardinality3 | -2.16 | 20 | = 0.109 | -0.56 [-0.97, -0.03] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 566.76, BIC = 588.20
- **2 to 3 vs 1 to 3**: *β* = -1.32, *SE* = 2.897, *z* = -0.456, *p* = 0.648
- **4 to 3 vs 1 to 3**: *β* = -2.50, *SE* = 2.913, *z* = -0.860, *p* = 0.390
- **5 to 3 vs 1 to 3**: *β* = 2.30, *SE* = 2.588, *z* = 0.889, *p* = 0.374
- **6 to 3 vs 1 to 3**: *β* = -0.63, *SE* = 2.703, *z* = -0.233, *p* = 0.816
- **Cardinality3 vs 1 to 3**: *β* = 0.01, *SE* = 2.781, *z* = 0.003, *p* = 0.997
- **SNR**: *β* = -0.10, *SE* = 0.519, *z* = -0.187, *p* = 0.852

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 1.32 | 2.90 | 0.46 | 0.648 | 0.999 | n.s. |
| 1 to 3 - 4 to 3 | 2.50 | 2.91 | 0.86 | 0.390 | 0.995 | n.s. |
| 1 to 3 - 5 to 3 | -2.30 | 2.59 | -0.89 | 0.374 | 0.995 | n.s. |
| 1 to 3 - 6 to 3 | 0.63 | 2.70 | 0.23 | 0.816 | 0.999 | n.s. |
| 1 to 3 - Cardinality3 | -0.01 | 2.78 | -0.00 | 0.997 | 0.999 | n.s. |
| 2 to 3 - 4 to 3 | 1.18 | 2.88 | 0.41 | 0.682 | 0.999 | n.s. |
| 2 to 3 - 5 to 3 | -3.62 | 2.54 | -1.43 | 0.153 | 0.903 | n.s. |
| 2 to 3 - 6 to 3 | -0.69 | 2.61 | -0.26 | 0.791 | 0.999 | n.s. |
| 2 to 3 - Cardinality3 | -1.33 | 2.74 | -0.49 | 0.627 | 0.999 | n.s. |
| 4 to 3 - 5 to 3 | -4.80 | 2.56 | -1.87 | 0.061 | 0.611 | n.s. |
| 4 to 3 - 6 to 3 | -1.87 | 2.70 | -0.69 | 0.487 | 0.995 | n.s. |
| 4 to 3 - Cardinality3 | -2.51 | 2.77 | -0.91 | 0.364 | 0.995 | n.s. |
| 5 to 3 - 6 to 3 | 2.93 | 2.37 | 1.24 | 0.216 | 0.958 | n.s. |
| 5 to 3 - Cardinality3 | 2.29 | 2.46 | 0.93 | 0.353 | 0.995 | n.s. |
| 6 to 3 - Cardinality3 | -0.64 | 2.54 | -0.25 | 0.801 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.51, *p* = 0.271, η²_G = 0.137
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -1.00 | 2 | = 0.673 | -0.41 [-1.12, 1.37] | small | n.s. |
| 1 to 3 vs 4 to 3 | 0.76 | 2 | = 0.673 | 0.44 [-0.93, 1.18] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.00 | 2 | = 1.000 | 0.00 [-0.96, 0.49] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -1.00 | 2 | = 0.673 | -0.41 [-0.84, 0.84] | small | n.s. |
| 1 to 3 vs Cardinality3 | -2.00 | 2 | = 0.514 | -0.35 [-1.09, 0.77] | small | n.s. |
| 2 to 3 vs 4 to 3 | 4.00 | 2 | = 0.400 | 1.63 [-0.66, 1.54] | large | n.s. |
| 2 to 3 vs 5 to 3 | 0.76 | 2 | = 0.673 | 0.41 [-1.38, 0.18] | small | n.s. |
| 2 to 3 vs 6 to 3 | nan | 2 | n/a | 0.00 [-0.68, 0.86] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 0.00 | 2 | = 1.000 | 0.00 [-0.92, 0.92] | negligible | n.s. |
| 4 to 3 vs 5 to 3 | -0.76 | 2 | = 0.673 | -0.44 [-1.48, 0.11] | small | n.s. |
| 4 to 3 vs 6 to 3 | -4.00 | 2 | = 0.400 | -1.63 [-0.98, 0.57] | large | n.s. |
| 4 to 3 vs Cardinality3 | -2.00 | 2 | = 0.514 | -1.03 [-1.26, 0.47] | large | n.s. |
| 5 to 3 vs 6 to 3 | -0.76 | 2 | = 0.673 | -0.41 [-0.49, 0.73] | small | n.s. |
| 5 to 3 vs Cardinality3 | -2.00 | 2 | = 0.514 | -0.35 [-0.48, 0.87] | small | n.s. |
| 6 to 3 vs Cardinality3 | 0.00 | 2 | = 1.000 | 0.00 [-0.72, 0.72] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.04, BIC = 296.48
- **2 to 3 vs 1 to 3**: *β* = 0.08, *SE* = 0.456, *z* = 0.178, *p* = 0.859
- **4 to 3 vs 1 to 3**: *β* = -0.43, *SE* = 0.458, *z* = -0.935, *p* = 0.350
- **5 to 3 vs 1 to 3**: *β* = -0.43, *SE* = 0.405, *z* = -1.060, *p* = 0.289
- **6 to 3 vs 1 to 3**: *β* = -0.06, *SE* = 0.424, *z* = -0.134, *p* = 0.893
- **Cardinality3 vs 1 to 3**: *β* = 0.52, *SE* = 0.437, *z* = 1.185, *p* = 0.236
- **SNR**: *β* = 0.61, *SE* = 0.083, *z* = 7.332, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.08 | 0.46 | -0.18 | 0.859 | 0.997 | n.s. |
| 1 to 3 - 4 to 3 | 0.43 | 0.46 | 0.93 | 0.350 | 0.954 | n.s. |
| 1 to 3 - 5 to 3 | 0.43 | 0.41 | 1.06 | 0.289 | 0.954 | n.s. |
| 1 to 3 - 6 to 3 | 0.06 | 0.42 | 0.13 | 0.893 | 0.997 | n.s. |
| 1 to 3 - Cardinality3 | -0.52 | 0.44 | -1.18 | 0.236 | 0.948 | n.s. |
| 2 to 3 - 4 to 3 | 0.51 | 0.45 | 1.12 | 0.261 | 0.952 | n.s. |
| 2 to 3 - 5 to 3 | 0.51 | 0.40 | 1.28 | 0.200 | 0.931 | n.s. |
| 2 to 3 - 6 to 3 | 0.14 | 0.41 | 0.34 | 0.736 | 0.995 | n.s. |
| 2 to 3 - Cardinality3 | -0.44 | 0.43 | -1.02 | 0.309 | 0.954 | n.s. |
| 4 to 3 - 5 to 3 | 0.00 | 0.40 | 0.00 | 0.997 | 0.997 | n.s. |
| 4 to 3 - 6 to 3 | -0.37 | 0.42 | -0.88 | 0.381 | 0.954 | n.s. |
| 4 to 3 - Cardinality3 | -0.95 | 0.43 | -2.18 | 0.029 | 0.337 | n.s. |
| 5 to 3 - 6 to 3 | -0.37 | 0.37 | -1.00 | 0.315 | 0.954 | n.s. |
| 5 to 3 - Cardinality3 | -0.95 | 0.38 | -2.46 | 0.014 | 0.189 | n.s. |
| 6 to 3 - Cardinality3 | -0.57 | 0.40 | -1.45 | 0.147 | 0.874 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.79, *p* = 0.579, η²_G = 0.178
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 2.55 | 2 | = 0.812 | 1.90 [-0.93, 1.62] | large | n.s. |
| 1 to 3 vs 4 to 3 | 1.16 | 2 | = 0.812 | 0.80 [-0.52, 1.77] | large | n.s. |
| 1 to 3 vs 5 to 3 | 0.98 | 2 | = 0.812 | 0.96 [-0.85, 0.59] | large | n.s. |
| 1 to 3 vs 6 to 3 | 0.69 | 2 | = 0.812 | 0.15 [-0.44, 1.31] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 0.67 | 2 | = 0.812 | 0.25 [-1.21, 0.67] | small | n.s. |
| 2 to 3 vs 4 to 3 | -1.86 | 2 | = 0.812 | -1.15 [-1.25, 0.86] | large | n.s. |
| 2 to 3 vs 5 to 3 | -3.14 | 2 | = 0.812 | -2.18 [-0.49, 0.96] | large | n.s. |
| 2 to 3 vs 6 to 3 | -1.46 | 2 | = 0.812 | -1.13 [-0.76, 0.78] | large | n.s. |
| 2 to 3 vs Cardinality3 | -0.84 | 2 | = 0.812 | -0.65 [-1.36, 0.56] | medium | n.s. |
| 4 to 3 vs 5 to 3 | 0.01 | 2 | = 0.990 | 0.01 [-0.59, 0.84] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.60 | 2 | = 0.812 | -0.45 [-0.75, 0.79] | small | n.s. |
| 4 to 3 vs Cardinality3 | -0.28 | 2 | = 0.894 | -0.20 [-1.12, 0.59] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.53 | 2 | = 0.812 | -0.50 [-0.61, 0.60] | medium | n.s. |
| 5 to 3 vs Cardinality3 | -0.24 | 2 | = 0.894 | -0.21 [-0.84, 0.52] | small | n.s. |
| 6 to 3 vs Cardinality3 | 0.57 | 2 | = 0.812 | 0.12 [-0.95, 0.50] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1114.18, BIC = 1138.32
- **2 to 3 vs 1 to 3**: *β* = -12.14, *SE* = 12.657, *z* = -0.959, *p* = 0.338
- **4 to 3 vs 1 to 3**: *β* = -19.38, *SE* = 11.755, *z* = -1.649, *p* = 0.099
- **5 to 3 vs 1 to 3**: *β* = -14.04, *SE* = 11.630, *z* = -1.207, *p* = 0.227
- **6 to 3 vs 1 to 3**: *β* = -11.66, *SE* = 11.752, *z* = -0.992, *p* = 0.321
- **Cardinality3 vs 1 to 3**: *β* = -35.95, *SE* = 12.837, *z* = -2.800, *p* = 0.005
- **SNR**: *β* = -0.91, *SE* = 1.308, *z* = -0.694, *p* = 0.488

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | 12.14 | 12.66 | 0.96 | 0.338 | 0.955 | n.s. |
| 1 to 3 - 4 to 3 | 19.38 | 11.75 | 1.65 | 0.099 | 0.686 | n.s. |
| 1 to 3 - 5 to 3 | 14.04 | 11.63 | 1.21 | 0.227 | 0.902 | n.s. |
| 1 to 3 - 6 to 3 | 11.66 | 11.75 | 0.99 | 0.321 | 0.955 | n.s. |
| 1 to 3 - Cardinality3 | 35.95 | 12.84 | 2.80 | 0.005 | 0.074 | n.s. |
| 2 to 3 - 4 to 3 | 7.24 | 12.81 | 0.57 | 0.572 | 0.987 | n.s. |
| 2 to 3 - 5 to 3 | 1.90 | 12.67 | 0.15 | 0.881 | 0.996 | n.s. |
| 2 to 3 - 6 to 3 | -0.48 | 12.80 | -0.04 | 0.970 | 0.996 | n.s. |
| 2 to 3 - Cardinality3 | 23.81 | 13.98 | 1.70 | 0.088 | 0.686 | n.s. |
| 4 to 3 - 5 to 3 | -5.34 | 11.78 | -0.45 | 0.650 | 0.987 | n.s. |
| 4 to 3 - 6 to 3 | -7.72 | 11.92 | -0.65 | 0.517 | 0.987 | n.s. |
| 4 to 3 - Cardinality3 | 16.57 | 12.93 | 1.28 | 0.200 | 0.892 | n.s. |
| 5 to 3 - 6 to 3 | -2.38 | 11.76 | -0.20 | 0.840 | 0.996 | n.s. |
| 5 to 3 - Cardinality3 | 21.91 | 12.73 | 1.72 | 0.085 | 0.686 | n.s. |
| 6 to 3 - Cardinality3 | 24.29 | 12.92 | 1.88 | 0.060 | 0.580 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.591, η²_G = 0.060
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | 0.31 | 9 | = 0.908 | 0.16 [-0.55, 0.60] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.84 | 9 | = 0.825 | 0.43 [-0.19, 0.80] | small | n.s. |
| 1 to 3 vs 5 to 3 | 0.42 | 9 | = 0.908 | 0.18 [-0.14, 0.86] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.11 | 9 | = 0.928 | -0.05 [-0.29, 0.69] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 1.37 | 9 | = 0.791 | 0.61 [0.04, 1.25] | medium | n.s. |
| 2 to 3 vs 4 to 3 | 0.71 | 9 | = 0.825 | 0.23 [-0.36, 0.81] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.09 | 9 | = 0.928 | -0.04 [-0.58, 0.53] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | -0.55 | 9 | = 0.889 | -0.22 [-0.47, 0.69] | small | n.s. |
| 2 to 3 vs Cardinality3 | 0.89 | 9 | = 0.825 | 0.37 [-0.45, 1.01] | small | n.s. |
| 4 to 3 vs 5 to 3 | -0.81 | 9 | = 0.825 | -0.35 [-0.53, 0.46] | small | n.s. |
| 4 to 3 vs 6 to 3 | -1.35 | 9 | = 0.791 | -0.52 [-0.57, 0.43] | medium | n.s. |
| 4 to 3 vs Cardinality3 | 0.28 | 9 | = 0.908 | 0.13 [-0.39, 0.77] | negligible | n.s. |
| 5 to 3 vs 6 to 3 | -0.77 | 9 | = 0.825 | -0.30 [-0.59, 0.38] | small | n.s. |
| 5 to 3 vs Cardinality3 | 1.57 | 9 | = 0.791 | 0.57 [-0.06, 1.12] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 1.89 | 9 | = 0.791 | 0.75 [0.07, 1.30] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 464.63, BIC = 488.77
- **2 to 3 vs 1 to 3**: *β* = 0.28, *SE* = 0.558, *z* = 0.497, *p* = 0.619
- **4 to 3 vs 1 to 3**: *β* = 0.01, *SE* = 0.512, *z* = 0.019, *p* = 0.985
- **5 to 3 vs 1 to 3**: *β* = -0.09, *SE* = 0.509, *z* = -0.177, *p* = 0.860
- **6 to 3 vs 1 to 3**: *β* = 0.82, *SE* = 0.513, *z* = 1.605, *p* = 0.108
- **Cardinality3 vs 1 to 3**: *β* = 0.11, *SE* = 0.568, *z* = 0.192, *p* = 0.848
- **SNR**: *β* = 0.46, *SE* = 0.064, *z* = 7.179, *p* < .001

_Reference condition: **1 to 3** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 3 - 2 to 3 | -0.28 | 0.56 | -0.50 | 0.619 | 1.000 | n.s. |
| 1 to 3 - 4 to 3 | -0.01 | 0.51 | -0.02 | 0.985 | 1.000 | n.s. |
| 1 to 3 - 5 to 3 | 0.09 | 0.51 | 0.18 | 0.860 | 1.000 | n.s. |
| 1 to 3 - 6 to 3 | -0.82 | 0.51 | -1.61 | 0.108 | 0.800 | n.s. |
| 1 to 3 - Cardinality3 | -0.11 | 0.57 | -0.19 | 0.848 | 1.000 | n.s. |
| 2 to 3 - 4 to 3 | 0.27 | 0.56 | 0.47 | 0.635 | 1.000 | n.s. |
| 2 to 3 - 5 to 3 | 0.37 | 0.55 | 0.66 | 0.508 | 0.999 | n.s. |
| 2 to 3 - 6 to 3 | -0.55 | 0.56 | -0.97 | 0.332 | 0.988 | n.s. |
| 2 to 3 - Cardinality3 | 0.17 | 0.62 | 0.27 | 0.787 | 1.000 | n.s. |
| 4 to 3 - 5 to 3 | 0.10 | 0.52 | 0.19 | 0.847 | 1.000 | n.s. |
| 4 to 3 - 6 to 3 | -0.81 | 0.52 | -1.56 | 0.118 | 0.805 | n.s. |
| 4 to 3 - Cardinality3 | -0.10 | 0.57 | -0.17 | 0.862 | 1.000 | n.s. |
| 5 to 3 - 6 to 3 | -0.91 | 0.51 | -1.78 | 0.075 | 0.689 | n.s. |
| 5 to 3 - Cardinality3 | -0.20 | 0.56 | -0.35 | 0.723 | 1.000 | n.s. |
| 6 to 3 - Cardinality3 | 0.71 | 0.57 | 1.26 | 0.208 | 0.939 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.97, *p* = 0.448, η²_G = 0.037
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1 to 3 vs 2 to 3 | -0.41 | 9 | = 0.935 | -0.08 [-0.69, 0.47] | negligible | n.s. |
| 1 to 3 vs 4 to 3 | 0.71 | 9 | = 0.934 | 0.16 [-0.36, 0.61] | negligible | n.s. |
| 1 to 3 vs 5 to 3 | -0.32 | 9 | = 0.935 | -0.10 [-0.39, 0.58] | negligible | n.s. |
| 1 to 3 vs 6 to 3 | -0.38 | 9 | = 0.935 | -0.05 [-0.81, 0.18] | negligible | n.s. |
| 1 to 3 vs Cardinality3 | 0.99 | 9 | = 0.866 | 0.38 [-0.34, 0.78] | small | n.s. |
| 2 to 3 vs 4 to 3 | 1.10 | 9 | = 0.866 | 0.28 [-0.31, 0.87] | small | n.s. |
| 2 to 3 vs 5 to 3 | -0.08 | 9 | = 0.935 | -0.02 [-0.28, 0.85] | negligible | n.s. |
| 2 to 3 vs 6 to 3 | 0.14 | 9 | = 0.935 | 0.03 [-0.74, 0.43] | negligible | n.s. |
| 2 to 3 vs Cardinality3 | 1.70 | 9 | = 0.866 | 0.57 [-0.23, 1.30] | medium | n.s. |
| 4 to 3 vs 5 to 3 | -1.19 | 9 | = 0.866 | -0.35 [-0.41, 0.59] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.77 | 9 | = 0.934 | -0.24 [-0.79, 0.22] | small | n.s. |
| 4 to 3 vs Cardinality3 | 0.59 | 9 | = 0.935 | 0.24 [-0.29, 0.89] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.16 | 9 | = 0.935 | 0.05 [-0.81, 0.18] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 1.70 | 9 | = 0.866 | 0.74 [-0.24, 0.89] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 1.33 | 9 | = 0.866 | 0.50 [-0.19, 0.96] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.017). Post-hoc tests revealed:
  - 1 to 3 showed smaller amplitude than 2 to 3 (*d* = -0.63)
  - 1 to 3 showed smaller amplitude than Cardinality3 (*d* = -0.60)

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
