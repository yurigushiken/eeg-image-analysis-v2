# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:31:13

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
| Cardinality1 | 8 | 106.50 ms | 13.17 | 4.66 | [92.00, 120.00] |
| Cardinality2 | 10 | 104.00 ms | 12.36 | 3.91 | [92.00, 120.00] |
| Cardinality3 | 12 | 106.67 ms | 11.98 | 3.46 | [92.00, 120.00] |
| Cardinality4 | 8 | 107.50 ms | 13.60 | 4.81 | [92.00, 120.00] |
| Cardinality5 | 10 | 114.00 ms | 11.66 | 3.69 | [92.00, 120.00] |
| Cardinality6 | 9 | 112.44 ms | 11.57 | 3.86 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 8 | 3.58 µV | 2.16 | 0.76 | [1.49, 8.10] |
| Cardinality2 | 10 | 2.56 µV | 1.72 | 0.54 | [0.81, 6.80] |
| Cardinality3 | 12 | 2.41 µV | 1.03 | 0.30 | [0.99, 4.66] |
| Cardinality4 | 8 | 2.54 µV | 1.61 | 0.57 | [0.69, 5.93] |
| Cardinality5 | 10 | 2.22 µV | 1.50 | 0.47 | [0.63, 5.06] |
| Cardinality6 | 9 | 2.47 µV | 1.19 | 0.40 | [0.70, 3.62] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | 177.87 ms | 19.18 | 4.95 | [144.00, 204.00] |
| Cardinality2 | 22 | 174.36 ms | 20.72 | 4.42 | [144.00, 204.00] |
| Cardinality3 | 22 | 168.18 ms | 15.93 | 3.40 | [144.00, 200.00] |
| Cardinality4 | 22 | 171.27 ms | 19.93 | 4.25 | [144.00, 204.00] |
| Cardinality5 | 24 | 171.67 ms | 16.04 | 3.27 | [144.00, 196.00] |
| Cardinality6 | 23 | 174.26 ms | 16.04 | 3.34 | [144.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 15 | -4.90 µV | 1.85 | 0.48 | [-9.64, -2.66] |
| Cardinality2 | 22 | -5.64 µV | 2.44 | 0.52 | [-10.50, -1.57] |
| Cardinality3 | 22 | -5.19 µV | 2.04 | 0.43 | [-10.83, -1.55] |
| Cardinality4 | 22 | -5.95 µV | 3.12 | 0.67 | [-13.09, -1.82] |
| Cardinality5 | 24 | -5.96 µV | 2.55 | 0.52 | [-12.06, -1.67] |
| Cardinality6 | 23 | -5.73 µV | 2.88 | 0.60 | [-11.14, -0.87] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 113.68 ms | 8.88 | 2.04 | [96.00, 120.00] |
| Cardinality2 | 12 | 107.00 ms | 10.25 | 2.96 | [96.00, 120.00] |
| Cardinality3 | 14 | 110.00 ms | 9.25 | 2.47 | [96.00, 120.00] |
| Cardinality4 | 12 | 109.67 ms | 9.57 | 2.76 | [96.00, 120.00] |
| Cardinality5 | 14 | 106.00 ms | 7.32 | 1.96 | [96.00, 120.00] |
| Cardinality6 | 12 | 109.00 ms | 8.20 | 2.37 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 19 | 4.41 µV | 2.89 | 0.66 | [1.20, 13.26] |
| Cardinality2 | 12 | 3.07 µV | 1.84 | 0.53 | [1.36, 7.57] |
| Cardinality3 | 14 | 3.25 µV | 2.36 | 0.63 | [0.79, 8.96] |
| Cardinality4 | 12 | 3.28 µV | 1.83 | 0.53 | [0.96, 6.93] |
| Cardinality5 | 14 | 2.66 µV | 1.69 | 0.45 | [0.35, 5.37] |
| Cardinality6 | 12 | 2.97 µV | 2.08 | 0.60 | [0.77, 8.25] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 461.71 ms | 14.53 | 3.88 | [440.00, 480.00] |
| Cardinality2 | 13 | 456.31 ms | 15.36 | 4.26 | [440.00, 480.00] |
| Cardinality3 | 16 | 458.25 ms | 11.59 | 2.90 | [440.00, 476.00] |
| Cardinality4 | 11 | 455.27 ms | 8.73 | 2.63 | [440.00, 472.00] |
| Cardinality5 | 14 | 455.14 ms | 16.17 | 4.32 | [440.00, 480.00] |
| Cardinality6 | 14 | 466.57 ms | 14.09 | 3.76 | [440.00, 480.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Cardinality1 | 14 | 3.04 µV | 1.84 | 0.49 | [1.05, 7.06] |
| Cardinality2 | 13 | 3.78 µV | 2.08 | 0.58 | [0.41, 8.49] |
| Cardinality3 | 16 | 4.49 µV | 2.23 | 0.56 | [1.30, 9.60] |
| Cardinality4 | 11 | 4.18 µV | 2.57 | 0.78 | [0.65, 8.96] |
| Cardinality5 | 14 | 2.64 µV | 1.36 | 0.36 | [0.35, 5.39] |
| Cardinality6 | 14 | 4.55 µV | 2.34 | 0.63 | [1.85, 9.61] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 456.09, BIC = 474.48
- **Cardinality2 vs Cardinality1**: *β* = -0.46, *SE* = 5.332, *z* = -0.087, *p* = 0.931
- **Cardinality3 vs Cardinality1**: *β* = 1.33, *SE* = 5.154, *z* = 0.258, *p* = 0.797
- **Cardinality4 vs Cardinality1**: *β* = 2.54, *SE* = 5.536, *z* = 0.460, *p* = 0.646
- **Cardinality5 vs Cardinality1**: *β* = 10.01, *SE* = 5.411, *z* = 1.850, *p* = 0.064
- **Cardinality6 vs Cardinality1**: *β* = 7.98, *SE* = 5.625, *z* = 1.418, *p* = 0.156
- **SNR**: *β* = 2.60, *SE* = 1.827, *z* = 1.425, *p* = 0.154

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.46 | 5.33 | 0.09 | 0.931 | 0.998 | n.s. |
| Cardinality1 - Cardinality3 | -1.33 | 5.15 | -0.26 | 0.797 | 0.998 | n.s. |
| Cardinality1 - Cardinality4 | -2.54 | 5.54 | -0.46 | 0.646 | 0.998 | n.s. |
| Cardinality1 - Cardinality5 | -10.01 | 5.41 | -1.85 | 0.064 | 0.606 | n.s. |
| Cardinality1 - Cardinality6 | -7.98 | 5.62 | -1.42 | 0.156 | 0.845 | n.s. |
| Cardinality2 - Cardinality3 | -1.79 | 4.69 | -0.38 | 0.703 | 0.998 | n.s. |
| Cardinality2 - Cardinality4 | -3.01 | 5.20 | -0.58 | 0.563 | 0.997 | n.s. |
| Cardinality2 - Cardinality5 | -10.47 | 4.95 | -2.12 | 0.034 | 0.408 | n.s. |
| Cardinality2 - Cardinality6 | -8.44 | 5.13 | -1.65 | 0.100 | 0.716 | n.s. |
| Cardinality3 - Cardinality4 | -1.22 | 5.05 | -0.24 | 0.810 | 0.998 | n.s. |
| Cardinality3 - Cardinality5 | -8.68 | 4.79 | -1.81 | 0.070 | 0.611 | n.s. |
| Cardinality3 - Cardinality6 | -6.65 | 4.91 | -1.35 | 0.176 | 0.845 | n.s. |
| Cardinality4 - Cardinality5 | -7.46 | 5.27 | -1.42 | 0.157 | 0.845 | n.s. |
| Cardinality4 - Cardinality6 | -5.43 | 5.45 | -1.00 | 0.319 | 0.954 | n.s. |
| Cardinality5 - Cardinality6 | 2.03 | 5.02 | 0.40 | 0.686 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 182.79, BIC = 201.17
- **Cardinality2 vs Cardinality1**: *β* = -0.14, *SE* = 0.416, *z* = -0.341, *p* = 0.733
- **Cardinality3 vs Cardinality1**: *β* = -0.56, *SE* = 0.428, *z* = -1.318, *p* = 0.187
- **Cardinality4 vs Cardinality1**: *β* = -0.91, *SE* = 0.418, *z* = -2.168, *p* = 0.030
- **Cardinality5 vs Cardinality1**: *β* = -0.30, *SE* = 0.415, *z* = -0.728, *p* = 0.467
- **Cardinality6 vs Cardinality1**: *β* = -0.35, *SE* = 0.445, *z* = -0.787, *p* = 0.431
- **SNR**: *β* = 0.83, *SE* = 0.141, *z* = 5.922, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.14 | 0.42 | 0.34 | 0.733 | 0.989 | n.s. |
| Cardinality1 - Cardinality3 | 0.56 | 0.43 | 1.32 | 0.187 | 0.898 | n.s. |
| Cardinality1 - Cardinality4 | 0.91 | 0.42 | 2.17 | 0.030 | 0.368 | n.s. |
| Cardinality1 - Cardinality5 | 0.30 | 0.41 | 0.73 | 0.467 | 0.989 | n.s. |
| Cardinality1 - Cardinality6 | 0.35 | 0.45 | 0.79 | 0.431 | 0.989 | n.s. |
| Cardinality2 - Cardinality3 | 0.42 | 0.35 | 1.20 | 0.232 | 0.929 | n.s. |
| Cardinality2 - Cardinality4 | 0.76 | 0.39 | 1.95 | 0.051 | 0.521 | n.s. |
| Cardinality2 - Cardinality5 | 0.16 | 0.37 | 0.43 | 0.667 | 0.989 | n.s. |
| Cardinality2 - Cardinality6 | 0.21 | 0.38 | 0.54 | 0.588 | 0.989 | n.s. |
| Cardinality3 - Cardinality4 | 0.34 | 0.40 | 0.86 | 0.392 | 0.989 | n.s. |
| Cardinality3 - Cardinality5 | -0.26 | 0.38 | -0.69 | 0.491 | 0.989 | n.s. |
| Cardinality3 - Cardinality6 | -0.21 | 0.38 | -0.56 | 0.577 | 0.989 | n.s. |
| Cardinality4 - Cardinality5 | -0.60 | 0.39 | -1.54 | 0.125 | 0.823 | n.s. |
| Cardinality4 - Cardinality6 | -0.56 | 0.40 | -1.38 | 0.167 | 0.889 | n.s. |
| Cardinality5 - Cardinality6 | 0.05 | 0.38 | 0.13 | 0.898 | 0.989 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1055.35, BIC = 1081.02
- **Cardinality2 vs Cardinality1**: *β* = -3.17, *SE* = 3.884, *z* = -0.816, *p* = 0.414
- **Cardinality3 vs Cardinality1**: *β* = -8.07, *SE* = 3.930, *z* = -2.053, *p* = 0.040
- **Cardinality4 vs Cardinality1**: *β* = -6.50, *SE* = 3.941, *z* = -1.649, *p* = 0.099
- **Cardinality5 vs Cardinality1**: *β* = -6.50, *SE* = 3.867, *z* = -1.682, *p* = 0.093
- **Cardinality6 vs Cardinality1**: *β* = -4.33, *SE* = 3.859, *z* = -1.123, *p* = 0.262
- **SNR**: *β* = 0.16, *SE* = 0.447, *z* = 0.362, *p* = 0.717

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 3.17 | 3.88 | 0.82 | 0.414 | 0.976 | n.s. |
| Cardinality1 - Cardinality3 | 8.07 | 3.93 | 2.05 | 0.040 | 0.459 | n.s. |
| Cardinality1 - Cardinality4 | 6.50 | 3.94 | 1.65 | 0.099 | 0.743 | n.s. |
| Cardinality1 - Cardinality5 | 6.50 | 3.87 | 1.68 | 0.093 | 0.743 | n.s. |
| Cardinality1 - Cardinality6 | 4.33 | 3.86 | 1.12 | 0.262 | 0.964 | n.s. |
| Cardinality2 - Cardinality3 | 4.90 | 3.48 | 1.41 | 0.159 | 0.875 | n.s. |
| Cardinality2 - Cardinality4 | 3.33 | 3.52 | 0.95 | 0.345 | 0.974 | n.s. |
| Cardinality2 - Cardinality5 | 3.33 | 3.44 | 0.97 | 0.333 | 0.974 | n.s. |
| Cardinality2 - Cardinality6 | 1.16 | 3.42 | 0.34 | 0.734 | 0.987 | n.s. |
| Cardinality3 - Cardinality4 | -1.57 | 3.52 | -0.45 | 0.656 | 0.987 | n.s. |
| Cardinality3 - Cardinality5 | -1.56 | 3.41 | -0.46 | 0.647 | 0.987 | n.s. |
| Cardinality3 - Cardinality6 | -3.74 | 3.43 | -1.09 | 0.277 | 0.964 | n.s. |
| Cardinality4 - Cardinality5 | 0.00 | 3.39 | 0.00 | 0.999 | 0.999 | n.s. |
| Cardinality4 - Cardinality6 | -2.17 | 3.43 | -0.63 | 0.527 | 0.987 | n.s. |
| Cardinality5 - Cardinality6 | -2.17 | 3.36 | -0.65 | 0.517 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.394, η²_G = 0.032
- Greenhouse-Geisser corrected: *p* = 0.372 (ε = 0.477)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.25 | 11 | = 0.869 | 0.09 [-0.43, 0.68] | negligible | n.s. |
| Cardinality1 vs Cardinality3 | 1.81 | 11 | = 0.488 | 0.43 [-0.09, 1.21] | small | n.s. |
| Cardinality1 vs Cardinality4 | 2.05 | 11 | = 0.488 | 0.52 [-0.06, 1.18] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 1.05 | 11 | = 0.666 | 0.30 [-0.10, 1.07] | small | n.s. |
| Cardinality1 vs Cardinality6 | 0.48 | 11 | = 0.743 | 0.15 [-0.32, 0.80] | negligible | n.s. |
| Cardinality2 vs Cardinality3 | 0.90 | 11 | = 0.666 | 0.26 [-0.17, 0.78] | small | n.s. |
| Cardinality2 vs Cardinality4 | 1.05 | 11 | = 0.666 | 0.35 [-0.31, 0.60] | small | n.s. |
| Cardinality2 vs Cardinality5 | 0.64 | 11 | = 0.668 | 0.15 [-0.33, 0.56] | negligible | n.s. |
| Cardinality2 vs Cardinality6 | 0.13 | 11 | = 0.900 | 0.04 [-0.37, 0.52] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | 0.79 | 11 | = 0.668 | 0.13 [-0.53, 0.40] | negligible | n.s. |
| Cardinality3 vs Cardinality5 | -0.88 | 11 | = 0.666 | -0.14 [-0.64, 0.26] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -1.62 | 11 | = 0.497 | -0.28 [-0.73, 0.19] | small | n.s. |
| Cardinality4 vs Cardinality5 | -1.12 | 11 | = 0.666 | -0.26 [-0.47, 0.41] | small | n.s. |
| Cardinality4 vs Cardinality6 | -2.05 | 11 | = 0.488 | -0.37 [-0.68, 0.22] | small | n.s. |
| Cardinality5 vs Cardinality6 | -0.69 | 11 | = 0.668 | -0.14 [-0.53, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 523.91, BIC = 549.58
- **Cardinality2 vs Cardinality1**: *β* = -1.09, *SE* = 0.506, *z* = -2.156, *p* = 0.031
- **Cardinality3 vs Cardinality1**: *β* = -0.55, *SE* = 0.512, *z* = -1.078, *p* = 0.281
- **Cardinality4 vs Cardinality1**: *β* = -0.88, *SE* = 0.514, *z* = -1.717, *p* = 0.086
- **Cardinality5 vs Cardinality1**: *β* = -0.95, *SE* = 0.504, *z* = -1.895, *p* = 0.058
- **Cardinality6 vs Cardinality1**: *β* = -1.02, *SE* = 0.503, *z* = -2.035, *p* = 0.042
- **SNR**: *β* = -0.41, *SE* = 0.057, *z* = -7.224, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 1.09 | 0.51 | 2.16 | 0.031 | 0.377 | n.s. |
| Cardinality1 - Cardinality3 | 0.55 | 0.51 | 1.08 | 0.281 | 0.963 | n.s. |
| Cardinality1 - Cardinality4 | 0.88 | 0.51 | 1.72 | 0.086 | 0.660 | n.s. |
| Cardinality1 - Cardinality5 | 0.96 | 0.50 | 1.89 | 0.058 | 0.541 | n.s. |
| Cardinality1 - Cardinality6 | 1.02 | 0.50 | 2.03 | 0.042 | 0.451 | n.s. |
| Cardinality2 - Cardinality3 | -0.54 | 0.45 | -1.19 | 0.234 | 0.946 | n.s. |
| Cardinality2 - Cardinality4 | -0.21 | 0.46 | -0.46 | 0.648 | 0.998 | n.s. |
| Cardinality2 - Cardinality5 | -0.14 | 0.45 | -0.31 | 0.760 | 0.999 | n.s. |
| Cardinality2 - Cardinality6 | -0.07 | 0.45 | -0.15 | 0.879 | 0.999 | n.s. |
| Cardinality3 - Cardinality4 | 0.33 | 0.46 | 0.72 | 0.470 | 0.988 | n.s. |
| Cardinality3 - Cardinality5 | 0.40 | 0.44 | 0.91 | 0.364 | 0.973 | n.s. |
| Cardinality3 - Cardinality6 | 0.47 | 0.45 | 1.06 | 0.291 | 0.963 | n.s. |
| Cardinality4 - Cardinality5 | 0.07 | 0.44 | 0.16 | 0.869 | 0.999 | n.s. |
| Cardinality4 - Cardinality6 | 0.14 | 0.45 | 0.32 | 0.751 | 0.999 | n.s. |
| Cardinality5 - Cardinality6 | 0.07 | 0.44 | 0.16 | 0.874 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.29, *p* = 0.280, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.90 | 11 | = 0.632 | 0.39 [-0.25, 0.89] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.07 | 11 | = 0.632 | 0.36 [-0.26, 0.98] | small | n.s. |
| Cardinality1 vs Cardinality4 | 1.30 | 11 | = 0.632 | 0.50 [-0.24, 0.95] | small | n.s. |
| Cardinality1 vs Cardinality5 | 2.33 | 11 | = 0.593 | 0.87 [-0.06, 1.12] | large | n.s. |
| Cardinality1 vs Cardinality6 | 1.19 | 11 | = 0.632 | 0.40 [-0.17, 0.98] | small | n.s. |
| Cardinality2 vs Cardinality3 | -0.34 | 11 | = 0.792 | -0.07 [-0.61, 0.33] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | 0.82 | 11 | = 0.632 | 0.18 [-0.27, 0.65] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 1.11 | 11 | = 0.632 | 0.36 [-0.27, 0.62] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.25 | 11 | = 0.804 | 0.06 [-0.32, 0.57] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | 0.93 | 11 | = 0.632 | 0.24 [-0.14, 0.82] | small | n.s. |
| Cardinality3 vs Cardinality5 | 1.65 | 11 | = 0.632 | 0.47 [-0.04, 0.89] | small | n.s. |
| Cardinality3 vs Cardinality6 | 0.51 | 11 | = 0.779 | 0.12 [-0.24, 0.68] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.39 | 11 | = 0.792 | 0.10 [-0.46, 0.43] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -0.76 | 11 | = 0.632 | -0.10 [-0.56, 0.33] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -1.05 | 11 | = 0.632 | -0.24 [-0.53, 0.33] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 601.11, BIC = 622.88
- **Cardinality2 vs Cardinality1**: *β* = -5.90, *SE* = 2.852, *z* = -2.069, *p* = 0.039
- **Cardinality3 vs Cardinality1**: *β* = -3.45, *SE* = 2.734, *z* = -1.263, *p* = 0.207
- **Cardinality4 vs Cardinality1**: *β* = -4.53, *SE* = 2.839, *z* = -1.596, *p* = 0.111
- **Cardinality5 vs Cardinality1**: *β* = -7.93, *SE* = 2.713, *z* = -2.923, *p* = 0.003
- **Cardinality6 vs Cardinality1**: *β* = -4.69, *SE* = 2.883, *z* = -1.627, *p* = 0.104
- **SNR**: *β* = 1.27, *SE* = 0.519, *z* = 2.456, *p* = 0.014

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 5.90 | 2.85 | 2.07 | 0.039 | 0.423 | n.s. |
| Cardinality1 - Cardinality3 | 3.45 | 2.73 | 1.26 | 0.207 | 0.901 | n.s. |
| Cardinality1 - Cardinality4 | 4.53 | 2.84 | 1.60 | 0.111 | 0.759 | n.s. |
| Cardinality1 - Cardinality5 | 7.93 | 2.71 | 2.92 | 0.003 | 0.051 | n.s. |
| Cardinality1 - Cardinality6 | 4.69 | 2.88 | 1.63 | 0.104 | 0.759 | n.s. |
| Cardinality2 - Cardinality3 | -2.45 | 3.03 | -0.81 | 0.420 | 0.978 | n.s. |
| Cardinality2 - Cardinality4 | -1.37 | 3.16 | -0.43 | 0.665 | 0.996 | n.s. |
| Cardinality2 - Cardinality5 | 2.03 | 3.04 | 0.67 | 0.504 | 0.985 | n.s. |
| Cardinality2 - Cardinality6 | -1.21 | 3.17 | -0.38 | 0.703 | 0.996 | n.s. |
| Cardinality3 - Cardinality4 | 1.08 | 3.06 | 0.35 | 0.725 | 0.996 | n.s. |
| Cardinality3 - Cardinality5 | 4.48 | 2.93 | 1.53 | 0.127 | 0.776 | n.s. |
| Cardinality3 - Cardinality6 | 1.24 | 3.04 | 0.41 | 0.684 | 0.996 | n.s. |
| Cardinality4 - Cardinality5 | 3.40 | 3.02 | 1.12 | 0.261 | 0.934 | n.s. |
| Cardinality4 - Cardinality6 | 0.16 | 3.17 | 0.05 | 0.959 | 0.996 | n.s. |
| Cardinality5 - Cardinality6 | -3.24 | 3.02 | -1.07 | 0.283 | 0.934 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.68, *p* = 0.176, η²_G = 0.218
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.69 | 5 | = 0.441 | 1.01 [-0.25, 1.07] | large | n.s. |
| Cardinality1 vs Cardinality3 | 1.51 | 5 | = 0.441 | 0.89 [-0.10, 1.28] | large | n.s. |
| Cardinality1 vs Cardinality4 | 1.35 | 5 | = 0.441 | 0.69 [-0.17, 1.17] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 3.00 | 5 | = 0.316 | 1.82 [-0.10, 1.20] | large | n.s. |
| Cardinality1 vs Cardinality6 | 2.09 | 5 | = 0.441 | 1.18 [-0.30, 1.20] | large | n.s. |
| Cardinality2 vs Cardinality3 | -0.10 | 5 | = 0.988 | -0.07 [-0.85, 0.59] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -0.94 | 5 | = 0.533 | -0.54 [-0.81, 0.73] | medium | n.s. |
| Cardinality2 vs Cardinality5 | 0.75 | 5 | = 0.610 | 0.53 [-0.60, 0.84] | medium | n.s. |
| Cardinality2 vs Cardinality6 | -0.13 | 5 | = 0.988 | -0.08 [-0.98, 0.70] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.96 | 5 | = 0.533 | -0.45 [-1.02, 0.66] | small | n.s. |
| Cardinality3 vs Cardinality5 | 1.35 | 5 | = 0.441 | 0.60 [-0.38, 1.23] | medium | n.s. |
| Cardinality3 vs Cardinality6 | 0.00 | 5 | = 1.000 | 0.00 [-0.42, 1.18] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 1.86 | 5 | = 0.441 | 1.23 [-0.43, 1.03] | large | n.s. |
| Cardinality4 vs Cardinality6 | 2.71 | 5 | = 0.316 | 0.55 [-0.90, 0.77] | medium | n.s. |
| Cardinality5 vs Cardinality6 | -1.14 | 5 | = 0.512 | -0.69 [-1.14, 0.26] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 313.10, BIC = 334.87
- **Cardinality2 vs Cardinality1**: *β* = -1.09, *SE* = 0.475, *z* = -2.287, *p* = 0.022
- **Cardinality3 vs Cardinality1**: *β* = -0.97, *SE* = 0.456, *z* = -2.128, *p* = 0.033
- **Cardinality4 vs Cardinality1**: *β* = -1.11, *SE* = 0.470, *z* = -2.369, *p* = 0.018
- **Cardinality5 vs Cardinality1**: *β* = -1.75, *SE* = 0.450, *z* = -3.877, *p* < .001
- **Cardinality6 vs Cardinality1**: *β* = -1.16, *SE* = 0.482, *z* = -2.401, *p* = 0.016
- **SNR**: *β* = 0.80, *SE* = 0.089, *z* = 8.967, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 1.09 | 0.47 | 2.29 | 0.022 | 0.236 | n.s. |
| Cardinality1 - Cardinality3 | 0.97 | 0.46 | 2.13 | 0.033 | 0.311 | n.s. |
| Cardinality1 - Cardinality4 | 1.11 | 0.47 | 2.37 | 0.018 | 0.209 | n.s. |
| Cardinality1 - Cardinality5 | 1.75 | 0.45 | 3.88 | < .001 | 0.002 | ** |
| Cardinality1 - Cardinality6 | 1.16 | 0.48 | 2.40 | 0.016 | 0.206 | n.s. |
| Cardinality2 - Cardinality3 | -0.12 | 0.50 | -0.23 | 0.817 | 0.999 | n.s. |
| Cardinality2 - Cardinality4 | 0.03 | 0.53 | 0.05 | 0.959 | 0.999 | n.s. |
| Cardinality2 - Cardinality5 | 0.66 | 0.50 | 1.31 | 0.189 | 0.849 | n.s. |
| Cardinality2 - Cardinality6 | 0.07 | 0.53 | 0.13 | 0.893 | 0.999 | n.s. |
| Cardinality3 - Cardinality4 | 0.14 | 0.51 | 0.28 | 0.780 | 0.999 | n.s. |
| Cardinality3 - Cardinality5 | 0.78 | 0.49 | 1.58 | 0.114 | 0.701 | n.s. |
| Cardinality3 - Cardinality6 | 0.19 | 0.51 | 0.37 | 0.712 | 0.999 | n.s. |
| Cardinality4 - Cardinality5 | 0.63 | 0.50 | 1.26 | 0.207 | 0.849 | n.s. |
| Cardinality4 - Cardinality6 | 0.04 | 0.53 | 0.08 | 0.934 | 0.999 | n.s. |
| Cardinality5 - Cardinality6 | -0.59 | 0.50 | -1.18 | 0.238 | 0.850 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.38, *p* = 0.265, η²_G = 0.151
- Greenhouse-Geisser corrected: *p* = 0.293 (ε = 0.472)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 2.95 | 5 | = 0.480 | 0.75 [0.07, 1.53] | medium | n.s. |
| Cardinality1 vs Cardinality3 | 1.49 | 5 | = 0.647 | 0.84 [-0.17, 1.19] | large | n.s. |
| Cardinality1 vs Cardinality4 | 1.70 | 5 | = 0.647 | 0.70 [-0.12, 1.25] | medium | n.s. |
| Cardinality1 vs Cardinality5 | 1.61 | 5 | = 0.647 | 0.96 [-0.03, 1.29] | large | n.s. |
| Cardinality1 vs Cardinality6 | 1.42 | 5 | = 0.647 | 0.72 [-0.15, 1.42] | medium | n.s. |
| Cardinality2 vs Cardinality3 | 0.24 | 5 | = 0.909 | 0.13 [-1.01, 0.45] | negligible | n.s. |
| Cardinality2 vs Cardinality4 | -0.40 | 5 | = 0.909 | -0.13 [-1.17, 0.42] | negligible | n.s. |
| Cardinality2 vs Cardinality5 | 0.46 | 5 | = 0.909 | 0.29 [-0.52, 0.92] | small | n.s. |
| Cardinality2 vs Cardinality6 | 0.00 | 5 | = 0.997 | 0.00 [-0.73, 0.95] | negligible | n.s. |
| Cardinality3 vs Cardinality4 | -0.70 | 5 | = 0.909 | -0.27 [-1.22, 0.50] | small | n.s. |
| Cardinality3 vs Cardinality5 | 0.20 | 5 | = 0.909 | 0.15 [-0.55, 1.00] | negligible | n.s. |
| Cardinality3 vs Cardinality6 | -0.36 | 5 | = 0.909 | -0.11 [-0.54, 1.02] | negligible | n.s. |
| Cardinality4 vs Cardinality5 | 0.65 | 5 | = 0.909 | 0.46 [-0.41, 1.06] | small | n.s. |
| Cardinality4 vs Cardinality6 | 0.44 | 5 | = 0.909 | 0.12 [-0.92, 0.75] | negligible | n.s. |
| Cardinality5 vs Cardinality6 | -0.37 | 5 | = 0.909 | -0.26 [-0.75, 0.59] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 670.96, BIC = 692.62
- **Cardinality2 vs Cardinality1**: *β* = -6.87, *SE* = 5.071, *z* = -1.356, *p* = 0.175
- **Cardinality3 vs Cardinality1**: *β* = -6.15, *SE* = 4.980, *z* = -1.236, *p* = 0.217
- **Cardinality4 vs Cardinality1**: *β* = -8.28, *SE* = 5.348, *z* = -1.549, *p* = 0.121
- **Cardinality5 vs Cardinality1**: *β* = -7.82, *SE* = 4.951, *z* = -1.579, *p* = 0.114
- **Cardinality6 vs Cardinality1**: *β* = 2.11, *SE* = 5.137, *z* = 0.411, *p* = 0.681
- **SNR**: *β* = 1.38, *SE* = 0.772, *z* = 1.786, *p* = 0.074

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 6.87 | 5.07 | 1.36 | 0.175 | 0.823 | n.s. |
| Cardinality1 - Cardinality3 | 6.15 | 4.98 | 1.24 | 0.217 | 0.858 | n.s. |
| Cardinality1 - Cardinality4 | 8.28 | 5.35 | 1.55 | 0.121 | 0.737 | n.s. |
| Cardinality1 - Cardinality5 | 7.82 | 4.95 | 1.58 | 0.114 | 0.737 | n.s. |
| Cardinality1 - Cardinality6 | -2.11 | 5.14 | -0.41 | 0.681 | 1.000 | n.s. |
| Cardinality2 - Cardinality3 | -0.72 | 4.89 | -0.15 | 0.883 | 1.000 | n.s. |
| Cardinality2 - Cardinality4 | 1.41 | 5.38 | 0.26 | 0.793 | 1.000 | n.s. |
| Cardinality2 - Cardinality5 | 0.94 | 5.01 | 0.19 | 0.850 | 1.000 | n.s. |
| Cardinality2 - Cardinality6 | -8.99 | 5.06 | -1.78 | 0.076 | 0.640 | n.s. |
| Cardinality3 - Cardinality4 | 2.13 | 5.14 | 0.41 | 0.679 | 1.000 | n.s. |
| Cardinality3 - Cardinality5 | 1.67 | 4.82 | 0.35 | 0.730 | 1.000 | n.s. |
| Cardinality3 - Cardinality6 | -8.26 | 4.75 | -1.74 | 0.082 | 0.641 | n.s. |
| Cardinality4 - Cardinality5 | -0.46 | 5.26 | -0.09 | 0.930 | 1.000 | n.s. |
| Cardinality4 - Cardinality6 | -10.39 | 5.27 | -1.97 | 0.049 | 0.505 | n.s. |
| Cardinality5 - Cardinality6 | -9.93 | 4.97 | -2.00 | 0.046 | 0.505 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.67, *p* = 0.090, η²_G = 0.675
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 0.40 | 1 | = 0.758 | 0.44 [-0.25, 1.28] | small | n.s. |
| Cardinality1 vs Cardinality3 | 1.80 | 1 | = 0.536 | 2.18 [-0.53, 0.83] | large | n.s. |
| Cardinality1 vs Cardinality4 | 2.50 | 1 | = 0.536 | 3.16 [-0.82, 1.31] | large | n.s. |
| Cardinality1 vs Cardinality5 | 13.00 | 1 | = 0.339 | 13.00 [-0.55, 1.01] | large | n.s. |
| Cardinality1 vs Cardinality6 | -1.67 | 1 | = 0.536 | -2.24 [-0.98, 0.48] | large | n.s. |
| Cardinality2 vs Cardinality3 | 1.00 | 1 | = 0.536 | 0.51 [-0.74, 0.53] | medium | n.s. |
| Cardinality2 vs Cardinality4 | 1.00 | 1 | = 0.536 | 0.63 [-0.33, 2.18] | medium | n.s. |
| Cardinality2 vs Cardinality5 | 1.00 | 1 | = 0.536 | 1.00 [-0.70, 0.64] | large | n.s. |
| Cardinality2 vs Cardinality6 | -1.29 | 1 | = 0.536 | -0.98 [-1.38, 0.27] | large | n.s. |
| Cardinality3 vs Cardinality4 | 1.00 | 1 | = 0.536 | 0.20 [-0.57, 1.14] | small | n.s. |
| Cardinality3 vs Cardinality5 | 1.00 | 1 | = 0.536 | 1.00 [-0.62, 0.65] | large | n.s. |
| Cardinality3 vs Cardinality6 | -7.00 | 1 | = 0.339 | -3.13 [-1.43, 0.14] | large | n.s. |
| Cardinality4 vs Cardinality5 | 1.00 | 1 | = 0.536 | 1.00 [-0.86, 0.81] | large | n.s. |
| Cardinality4 vs Cardinality6 | -15.00 | 1 | = 0.339 | -4.16 [-1.25, 0.36] | large | n.s. |
| Cardinality5 vs Cardinality6 | -9.00 | 1 | = 0.339 | -9.00 [-1.73, 0.06] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 299.79, BIC = 321.45
- **Cardinality2 vs Cardinality1**: *β* = -0.00, *SE* = 0.457, *z* = -0.008, *p* = 0.994
- **Cardinality3 vs Cardinality1**: *β* = 0.22, *SE* = 0.455, *z* = 0.491, *p* = 0.623
- **Cardinality4 vs Cardinality1**: *β* = 0.47, *SE* = 0.493, *z* = 0.955, *p* = 0.340
- **Cardinality5 vs Cardinality1**: *β* = -0.78, *SE* = 0.456, *z* = -1.699, *p* = 0.089
- **Cardinality6 vs Cardinality1**: *β* = 0.23, *SE* = 0.466, *z* = 0.502, *p* = 0.616
- **SNR**: *β* = 0.68, *SE* = 0.081, *z* = 8.314, *p* < .001

_Reference condition: **Cardinality1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Cardinality1 - Cardinality2 | 0.00 | 0.46 | 0.01 | 0.994 | 1.000 | n.s. |
| Cardinality1 - Cardinality3 | -0.22 | 0.46 | -0.49 | 0.623 | 0.999 | n.s. |
| Cardinality1 - Cardinality4 | -0.47 | 0.49 | -0.96 | 0.340 | 0.983 | n.s. |
| Cardinality1 - Cardinality5 | 0.78 | 0.46 | 1.70 | 0.089 | 0.646 | n.s. |
| Cardinality1 - Cardinality6 | -0.23 | 0.47 | -0.50 | 0.616 | 0.999 | n.s. |
| Cardinality2 - Cardinality3 | -0.23 | 0.44 | -0.52 | 0.606 | 0.999 | n.s. |
| Cardinality2 - Cardinality4 | -0.47 | 0.49 | -0.96 | 0.336 | 0.983 | n.s. |
| Cardinality2 - Cardinality5 | 0.77 | 0.44 | 1.73 | 0.083 | 0.646 | n.s. |
| Cardinality2 - Cardinality6 | -0.24 | 0.46 | -0.52 | 0.606 | 0.999 | n.s. |
| Cardinality3 - Cardinality4 | -0.25 | 0.47 | -0.52 | 0.600 | 0.999 | n.s. |
| Cardinality3 - Cardinality5 | 1.00 | 0.43 | 2.32 | 0.020 | 0.250 | n.s. |
| Cardinality3 - Cardinality6 | -0.01 | 0.43 | -0.02 | 0.981 | 1.000 | n.s. |
| Cardinality4 - Cardinality5 | 1.25 | 0.48 | 2.62 | 0.009 | 0.123 | n.s. |
| Cardinality4 - Cardinality6 | 0.24 | 0.47 | 0.50 | 0.618 | 0.999 | n.s. |
| Cardinality5 - Cardinality6 | -1.01 | 0.45 | -2.24 | 0.025 | 0.283 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 15 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.41, *p* = 0.827, η²_G = 0.220
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Cardinality1 vs Cardinality2 | 1.76 | 1 | = 0.824 | 0.60 [-0.86, 0.58] | medium | n.s. |
| Cardinality1 vs Cardinality3 | -0.25 | 1 | = 0.985 | -0.34 [-1.28, 0.16] | small | n.s. |
| Cardinality1 vs Cardinality4 | 0.66 | 1 | = 0.985 | 0.06 [-1.45, 0.72] | negligible | n.s. |
| Cardinality1 vs Cardinality5 | 0.04 | 1 | = 0.985 | 0.05 [-0.85, 0.69] | negligible | n.s. |
| Cardinality1 vs Cardinality6 | -2.75 | 1 | = 0.824 | -0.46 [-1.42, 0.15] | small | n.s. |
| Cardinality2 vs Cardinality3 | -0.93 | 1 | = 0.985 | -1.32 [-0.95, 0.35] | large | n.s. |
| Cardinality2 vs Cardinality4 | -2.23 | 1 | = 0.824 | -0.58 [-1.92, 0.45] | medium | n.s. |
| Cardinality2 vs Cardinality5 | -0.66 | 1 | = 0.985 | -0.91 [-0.43, 0.93] | large | n.s. |
| Cardinality2 vs Cardinality6 | -2.16 | 1 | = 0.824 | -1.03 [-1.04, 0.52] | large | n.s. |
| Cardinality3 vs Cardinality4 | 0.32 | 1 | = 0.985 | 0.45 [-0.69, 0.99] | small | n.s. |
| Cardinality3 vs Cardinality5 | 2.36 | 1 | = 0.824 | 0.64 [-0.02, 1.39] | medium | n.s. |
| Cardinality3 vs Cardinality6 | -0.19 | 1 | = 0.985 | -0.25 [-0.65, 0.78] | small | n.s. |
| Cardinality4 vs Cardinality5 | -0.02 | 1 | = 0.985 | -0.03 [-0.45, 1.30] | negligible | n.s. |
| Cardinality4 vs Cardinality6 | -2.10 | 1 | = 0.824 | -0.53 [-0.90, 0.64] | medium | n.s. |
| Cardinality5 vs Cardinality6 | -0.48 | 1 | = 0.985 | -0.60 [-1.39, 0.26] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**P3b latency:** Marginal trend toward condition differences (*p* = 0.090)

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
