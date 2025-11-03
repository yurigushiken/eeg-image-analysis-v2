# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:44:32

---

## 1. Analysis Overview

**Total Measurements:** 384
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| 4 to 3 | 12 | 100.00 ms | 11.05 | 3.19 | [88.00, 116.00] |
| 5 to 3 | 4 | 102.00 ms | 16.17 | 8.08 | [88.00, 116.00] |
| 6 to 3 | 8 | 103.00 ms | 10.64 | 3.76 | [88.00, 116.00] |
| Cardinality3 | 12 | 105.00 ms | 10.94 | 3.16 | [88.00, 116.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 12 | 2.31 µV | 1.20 | 0.35 | [0.44, 4.24] |
| 5 to 3 | 4 | 3.30 µV | 1.44 | 0.72 | [1.38, 4.74] |
| 6 to 3 | 8 | 1.99 µV | 0.52 | 0.18 | [1.49, 2.89] |
| Cardinality3 | 12 | 2.32 µV | 0.86 | 0.25 | [0.99, 3.69] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | 176.00 ms | 18.57 | 3.87 | [148.00, 212.00] |
| 5 to 3 | 24 | 174.67 ms | 16.20 | 3.31 | [144.00, 208.00] |
| 6 to 3 | 23 | 174.78 ms | 16.02 | 3.34 | [152.00, 212.00] |
| Cardinality3 | 23 | 169.91 ms | 17.64 | 3.68 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 23 | -6.42 µV | 2.16 | 0.45 | [-11.27, -1.89] |
| 5 to 3 | 24 | -5.90 µV | 2.73 | 0.56 | [-12.11, -1.76] |
| 6 to 3 | 23 | -6.49 µV | 2.21 | 0.46 | [-10.34, -1.59] |
| Cardinality3 | 23 | -5.16 µV | 1.99 | 0.42 | [-10.83, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 11 | 105.45 ms | 9.51 | 2.87 | [92.00, 120.00] |
| 5 to 3 | 17 | 111.76 ms | 7.93 | 1.92 | [100.00, 120.00] |
| 6 to 3 | 14 | 108.86 ms | 9.44 | 2.52 | [92.00, 120.00] |
| Cardinality3 | 13 | 108.62 ms | 10.18 | 2.82 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 11 | 2.85 µV | 1.52 | 0.46 | [0.60, 5.30] |
| 5 to 3 | 17 | 2.90 µV | 1.20 | 0.29 | [0.85, 4.61] |
| 6 to 3 | 14 | 2.97 µV | 2.18 | 0.58 | [0.16, 8.17] |
| Cardinality3 | 13 | 3.47 µV | 2.35 | 0.65 | [0.79, 8.96] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 19 | 453.68 ms | 42.69 | 9.79 | [388.00, 524.00] |
| 5 to 3 | 20 | 459.60 ms | 32.78 | 7.33 | [400.00, 524.00] |
| 6 to 3 | 19 | 462.11 ms | 36.52 | 8.38 | [396.00, 524.00] |
| Cardinality3 | 15 | 439.47 ms | 38.30 | 9.89 | [388.00, 520.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4 to 3 | 19 | 5.82 µV | 3.01 | 0.69 | [1.17, 11.65] |
| 5 to 3 | 20 | 5.66 µV | 2.35 | 0.52 | [1.51, 10.28] |
| 6 to 3 | 19 | 6.78 µV | 3.04 | 0.70 | [3.51, 14.26] |
| Cardinality3 | 15 | 5.13 µV | 2.02 | 0.52 | [3.31, 9.60] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 283.22, BIC = 294.30
- **5 to 3 vs 4 to 3**: *β* = 2.06, *SE* = 5.263, *z* = 0.391, *p* = 0.696
- **6 to 3 vs 4 to 3**: *β* = 2.01, *SE* = 3.980, *z* = 0.506, *p* = 0.613
- **Cardinality3 vs 4 to 3**: *β* = 4.70, *SE* = 3.690, *z* = 1.273, *p* = 0.203
- **SNR**: *β* = -0.69, *SE* = 1.752, *z* = -0.397, *p* = 0.692

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -2.06 | 5.26 | -0.39 | 0.696 | 0.976 | n.s. |
| 4 to 3 - 6 to 3 | -2.01 | 3.98 | -0.51 | 0.613 | 0.976 | n.s. |
| 4 to 3 - Cardinality3 | -4.70 | 3.69 | -1.27 | 0.203 | 0.744 | n.s. |
| 5 to 3 - 6 to 3 | 0.04 | 5.44 | 0.01 | 0.994 | 0.994 | n.s. |
| 5 to 3 - Cardinality3 | -2.64 | 5.15 | -0.51 | 0.608 | 0.976 | n.s. |
| 6 to 3 - Cardinality3 | -2.68 | 3.94 | -0.68 | 0.496 | 0.967 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 89.86, BIC = 100.94
- **5 to 3 vs 4 to 3**: *β* = 0.98, *SE* = 0.307, *z* = 3.184, *p* = 0.001
- **6 to 3 vs 4 to 3**: *β* = -0.45, *SE* = 0.230, *z* = -1.948, *p* = 0.051
- **Cardinality3 vs 4 to 3**: *β* = 0.11, *SE* = 0.222, *z* = 0.492, *p* = 0.622
- **SNR**: *β* = 0.36, *SE* = 0.103, *z* = 3.439, *p* = 0.001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.98 | 0.31 | -3.18 | 0.001 | 0.007 | ** |
| 4 to 3 - 6 to 3 | 0.45 | 0.23 | 1.95 | 0.051 | 0.100 | n.s. |
| 4 to 3 - Cardinality3 | -0.11 | 0.22 | -0.49 | 0.622 | 0.622 | n.s. |
| 5 to 3 - 6 to 3 | 1.43 | 0.31 | 4.55 | < .001 | < .001 | *** |
| 5 to 3 - Cardinality3 | 0.87 | 0.30 | 2.91 | 0.004 | 0.015 | * |
| 6 to 3 - Cardinality3 | -0.56 | 0.22 | -2.48 | 0.013 | 0.039 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 775.63, BIC = 793.36
- **5 to 3 vs 4 to 3**: *β* = -1.00, *SE* = 3.431, *z* = -0.292, *p* = 0.770
- **6 to 3 vs 4 to 3**: *β* = 0.14, *SE* = 3.469, *z* = 0.041, *p* = 0.967
- **Cardinality3 vs 4 to 3**: *β* = -4.63, *SE* = 3.577, *z* = -1.295, *p* = 0.195
- **SNR**: *β* = 0.27, *SE* = 0.541, *z* = 0.505, *p* = 0.613

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 1.00 | 3.43 | 0.29 | 0.770 | 0.982 | n.s. |
| 4 to 3 - 6 to 3 | -0.14 | 3.47 | -0.04 | 0.967 | 0.982 | n.s. |
| 4 to 3 - Cardinality3 | 4.63 | 3.58 | 1.29 | 0.195 | 0.696 | n.s. |
| 5 to 3 - 6 to 3 | -1.15 | 3.43 | -0.33 | 0.738 | 0.982 | n.s. |
| 5 to 3 - Cardinality3 | 3.63 | 3.47 | 1.04 | 0.296 | 0.754 | n.s. |
| 6 to 3 - Cardinality3 | 4.78 | 3.56 | 1.34 | 0.180 | 0.696 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.90, *p* = 0.446, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.12 | 20 | = 0.903 | 0.04 [-0.37, 0.49] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.37 | 20 | = 0.858 | -0.07 [-0.50, 0.39] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.13 | 20 | = 0.600 | 0.29 [-0.21, 0.69] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.49 | 20 | = 0.858 | -0.11 [-0.53, 0.33] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 1.06 | 20 | = 0.600 | 0.27 [-0.21, 0.67] | small | n.s. |
| 6 to 3 vs Cardinality3 | 1.69 | 20 | = 0.600 | 0.37 [-0.11, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 380.05, BIC = 397.77
- **5 to 3 vs 4 to 3**: *β* = 0.36, *SE* = 0.433, *z* = 0.823, *p* = 0.410
- **6 to 3 vs 4 to 3**: *β* = -0.02, *SE* = 0.438, *z* = -0.051, *p* = 0.959
- **Cardinality3 vs 4 to 3**: *β* = 0.70, *SE* = 0.450, *z* = 1.554, *p* = 0.120
- **SNR**: *β* = -0.39, *SE* = 0.066, *z* = -5.901, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -0.36 | 0.43 | -0.82 | 0.410 | 0.853 | n.s. |
| 4 to 3 - 6 to 3 | 0.02 | 0.44 | 0.05 | 0.959 | 0.959 | n.s. |
| 4 to 3 - Cardinality3 | -0.70 | 0.45 | -1.55 | 0.120 | 0.497 | n.s. |
| 5 to 3 - 6 to 3 | 0.38 | 0.43 | 0.88 | 0.381 | 0.853 | n.s. |
| 5 to 3 - Cardinality3 | -0.34 | 0.44 | -0.78 | 0.434 | 0.853 | n.s. |
| 6 to 3 - Cardinality3 | -0.72 | 0.45 | -1.61 | 0.108 | 0.497 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.29, *p* = 0.087, η²_G = 0.047
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -1.21 | 20 | = 0.408 | -0.21 [-0.78, 0.11] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.04 | 20 | = 0.971 | -0.01 [-0.44, 0.45] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | -2.45 | 20 | = 0.131 | -0.58 [-1.03, -0.07] | medium | n.s. |
| 5 to 3 vs 6 to 3 | 0.88 | 20 | = 0.468 | 0.21 [-0.25, 0.62] | small | n.s. |
| 5 to 3 vs Cardinality3 | -1.13 | 20 | = 0.408 | -0.30 [-0.73, 0.16] | small | n.s. |
| 6 to 3 vs Cardinality3 | -2.16 | 20 | = 0.131 | -0.56 [-0.97, -0.03] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 384.07, BIC = 398.12
- **5 to 3 vs 4 to 3**: *β* = 5.97, *SE* = 2.021, *z* = 2.956, *p* = 0.003
- **6 to 3 vs 4 to 3**: *β* = 3.99, *SE* = 2.156, *z* = 1.852, *p* = 0.064
- **Cardinality3 vs 4 to 3**: *β* = 2.49, *SE* = 2.166, *z* = 1.151, *p* = 0.250
- **SNR**: *β* = -0.70, *SE* = 0.490, *z* = -1.436, *p* = 0.151

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -5.97 | 2.02 | -2.96 | 0.003 | 0.019 | * |
| 4 to 3 - 6 to 3 | -3.99 | 2.16 | -1.85 | 0.064 | 0.282 | n.s. |
| 4 to 3 - Cardinality3 | -2.49 | 2.17 | -1.15 | 0.250 | 0.578 | n.s. |
| 5 to 3 - 6 to 3 | 1.98 | 1.92 | 1.03 | 0.302 | 0.578 | n.s. |
| 5 to 3 - Cardinality3 | 3.48 | 1.95 | 1.79 | 0.074 | 0.282 | n.s. |
| 6 to 3 - Cardinality3 | 1.50 | 1.98 | 0.76 | 0.448 | 0.578 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.24, *p* = 0.330, η²_G = 0.043
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -1.47 | 5 | = 0.512 | -0.51 [-1.51, 0.09] | medium | n.s. |
| 4 to 3 vs 6 to 3 | -1.29 | 5 | = 0.512 | -0.40 [-1.61, 0.24] | small | n.s. |
| 4 to 3 vs Cardinality3 | -1.28 | 5 | = 0.512 | -0.46 [-1.30, 0.44] | small | n.s. |
| 5 to 3 vs 6 to 3 | 0.22 | 5 | = 0.999 | 0.07 [-0.49, 0.79] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 0.00 | 5 | = 1.000 | 0.00 [-0.42, 0.94] | negligible | n.s. |
| 6 to 3 vs Cardinality3 | -0.35 | 5 | = 0.999 | -0.06 [-0.41, 0.95] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 187.95, BIC = 202.00
- **5 to 3 vs 4 to 3**: *β* = -0.12, *SE* = 0.382, *z* = -0.300, *p* = 0.764
- **6 to 3 vs 4 to 3**: *β* = 0.51, *SE* = 0.406, *z* = 1.261, *p* = 0.207
- **Cardinality3 vs 4 to 3**: *β* = 0.79, *SE* = 0.409, *z* = 1.936, *p* = 0.053
- **SNR**: *β* = 0.60, *SE* = 0.091, *z* = 6.629, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.11 | 0.38 | 0.30 | 0.764 | 0.764 | n.s. |
| 4 to 3 - 6 to 3 | -0.51 | 0.41 | -1.26 | 0.207 | 0.502 | n.s. |
| 4 to 3 - Cardinality3 | -0.79 | 0.41 | -1.94 | 0.053 | 0.238 | n.s. |
| 5 to 3 - 6 to 3 | -0.63 | 0.36 | -1.73 | 0.083 | 0.294 | n.s. |
| 5 to 3 - Cardinality3 | -0.91 | 0.37 | -2.46 | 0.014 | 0.079 | n.s. |
| 6 to 3 - Cardinality3 | -0.28 | 0.38 | -0.74 | 0.457 | 0.705 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.39, *p* = 0.763, η²_G = 0.033
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | 0.63 | 5 | = 0.816 | 0.30 [-0.63, 0.81] | small | n.s. |
| 4 to 3 vs 6 to 3 | -0.65 | 5 | = 0.816 | -0.27 [-0.99, 0.69] | small | n.s. |
| 4 to 3 vs Cardinality3 | -0.44 | 5 | = 0.816 | -0.20 [-1.09, 0.61] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.91 | 5 | = 0.816 | -0.49 [-0.89, 0.40] | small | n.s. |
| 5 to 3 vs Cardinality3 | -0.62 | 5 | = 0.816 | -0.36 [-0.82, 0.53] | small | n.s. |
| 6 to 3 vs Cardinality3 | 0.02 | 5 | = 0.987 | 0.00 [-0.92, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 742.03, BIC = 758.06
- **5 to 3 vs 4 to 3**: *β* = 4.34, *SE* = 10.328, *z* = 0.420, *p* = 0.674
- **6 to 3 vs 4 to 3**: *β* = 7.42, *SE* = 10.417, *z* = 0.713, *p* = 0.476
- **Cardinality3 vs 4 to 3**: *β* = -16.18, *SE* = 11.430, *z* = -1.416, *p* = 0.157
- **SNR**: *β* = -0.25, *SE* = 1.482, *z* = -0.166, *p* = 0.868

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | -4.34 | 10.33 | -0.42 | 0.674 | 0.894 | n.s. |
| 4 to 3 - 6 to 3 | -7.42 | 10.42 | -0.71 | 0.476 | 0.856 | n.s. |
| 4 to 3 - Cardinality3 | 16.18 | 11.43 | 1.42 | 0.157 | 0.495 | n.s. |
| 5 to 3 - 6 to 3 | -3.08 | 10.26 | -0.30 | 0.764 | 0.894 | n.s. |
| 5 to 3 - Cardinality3 | 20.52 | 11.23 | 1.83 | 0.068 | 0.295 | n.s. |
| 6 to 3 - Cardinality3 | 23.61 | 11.42 | 2.07 | 0.039 | 0.211 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.66, *p* = 0.191, η²_G = 0.069
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.57 | 13 | = 0.579 | -0.21 [-0.53, 0.46] | small | n.s. |
| 4 to 3 vs 6 to 3 | -1.34 | 13 | = 0.406 | -0.41 [-0.57, 0.42] | small | n.s. |
| 4 to 3 vs Cardinality3 | 0.69 | 13 | = 0.579 | 0.26 [-0.40, 0.77] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.71 | 13 | = 0.579 | -0.24 [-0.60, 0.37] | small | n.s. |
| 5 to 3 vs Cardinality3 | 1.93 | 13 | = 0.229 | 0.52 [-0.06, 1.12] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 2.31 | 13 | = 0.229 | 0.74 [0.07, 1.30] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 321.02, BIC = 337.05
- **5 to 3 vs 4 to 3**: *β* = -0.13, *SE* = 0.543, *z* = -0.246, *p* = 0.805
- **6 to 3 vs 4 to 3**: *β* = 0.79, *SE* = 0.547, *z* = 1.442, *p* = 0.149
- **Cardinality3 vs 4 to 3**: *β* = 0.07, *SE* = 0.604, *z* = 0.108, *p* = 0.914
- **SNR**: *β* = 0.48, *SE* = 0.082, *z* = 5.862, *p* < .001

_Reference condition: **4 to 3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4 to 3 - 5 to 3 | 0.13 | 0.54 | 0.25 | 0.805 | 0.982 | n.s. |
| 4 to 3 - 6 to 3 | -0.79 | 0.55 | -1.44 | 0.149 | 0.554 | n.s. |
| 4 to 3 - Cardinality3 | -0.07 | 0.60 | -0.11 | 0.914 | 0.982 | n.s. |
| 5 to 3 - 6 to 3 | -0.92 | 0.54 | -1.71 | 0.087 | 0.420 | n.s. |
| 5 to 3 - Cardinality3 | -0.20 | 0.59 | -0.34 | 0.738 | 0.982 | n.s. |
| 6 to 3 - Cardinality3 | 0.72 | 0.60 | 1.20 | 0.229 | 0.647 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.23, *p* = 0.311, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4 to 3 vs 5 to 3 | -0.38 | 13 | = 0.727 | -0.10 [-0.41, 0.58] | negligible | n.s. |
| 4 to 3 vs 6 to 3 | -0.73 | 13 | = 0.716 | -0.19 [-0.80, 0.22] | negligible | n.s. |
| 4 to 3 vs Cardinality3 | 1.10 | 13 | = 0.584 | 0.37 [-0.30, 0.88] | small | n.s. |
| 5 to 3 vs 6 to 3 | -0.36 | 13 | = 0.727 | -0.11 [-0.81, 0.18] | negligible | n.s. |
| 5 to 3 vs Cardinality3 | 1.48 | 13 | = 0.487 | 0.50 [-0.24, 0.89] | medium | n.s. |
| 6 to 3 vs Cardinality3 | 1.72 | 13 | = 0.487 | 0.54 [-0.19, 0.96] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.087)

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
