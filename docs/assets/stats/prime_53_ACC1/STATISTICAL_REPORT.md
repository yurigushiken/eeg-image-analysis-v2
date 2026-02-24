# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:31:46

---

## 1. Analysis Overview

**Total Measurements:** 456
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
| 5a3 | 24 | 102.83 ms | 13.63 | 2.78 | [80.00, 124.00] |
| 5b3 | 23 | 100.70 ms | 13.14 | 2.74 | [80.00, 124.00] |
| 5c3 | 24 | 105.50 ms | 14.77 | 3.02 | [80.00, 124.00] |
| 5d3 | 24 | 102.00 ms | 16.00 | 3.27 | [80.00, 124.00] |
| 5e3 | 19 | 101.26 ms | 15.49 | 3.55 | [80.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 24 | -4.15 µV | 3.36 | 0.69 | [-9.35, 2.70] |
| 5b3 | 23 | -5.03 µV | 3.94 | 0.82 | [-14.12, 0.92] |
| 5c3 | 24 | -5.79 µV | 4.76 | 0.97 | [-18.37, 0.22] |
| 5d3 | 24 | -3.56 µV | 3.57 | 0.73 | [-9.85, 1.93] |
| 5e3 | 19 | -6.22 µV | 5.41 | 1.24 | [-22.32, 2.45] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 24 | 174.00 ms | 20.29 | 4.14 | [136.00, 220.00] |
| 5b3 | 23 | 180.17 ms | 26.41 | 5.51 | [140.00, 220.00] |
| 5c3 | 24 | 172.67 ms | 22.25 | 4.54 | [136.00, 220.00] |
| 5d3 | 24 | 175.50 ms | 22.76 | 4.65 | [136.00, 220.00] |
| 5e3 | 19 | 177.89 ms | 21.84 | 5.01 | [136.00, 216.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 24 | -6.30 µV | 2.90 | 0.59 | [-12.02, -0.83] |
| 5b3 | 23 | -7.46 µV | 4.96 | 1.03 | [-20.37, -0.83] |
| 5c3 | 24 | -6.20 µV | 3.75 | 0.76 | [-13.02, -0.12] |
| 5d3 | 24 | -6.48 µV | 2.71 | 0.55 | [-12.07, -0.94] |
| 5e3 | 19 | -9.03 µV | 3.64 | 0.84 | [-16.13, -0.27] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 24 | 96.67 ms | 15.41 | 3.15 | [72.00, 116.00] |
| 5b3 | 23 | 101.04 ms | 17.53 | 3.65 | [72.00, 120.00] |
| 5c3 | 24 | 105.17 ms | 15.13 | 3.09 | [72.00, 120.00] |
| 5d3 | 24 | 100.17 ms | 19.15 | 3.91 | [72.00, 120.00] |
| 5e3 | 19 | 92.00 ms | 17.89 | 4.10 | [72.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 24 | 3.45 µV | 3.74 | 0.76 | [-4.59, 12.41] |
| 5b3 | 23 | 4.22 µV | 5.30 | 1.11 | [-6.79, 16.29] |
| 5c3 | 24 | 4.51 µV | 3.59 | 0.73 | [-2.01, 15.66] |
| 5d3 | 24 | 3.71 µV | 3.49 | 0.71 | [-1.92, 12.45] |
| 5e3 | 19 | 4.82 µV | 4.63 | 1.06 | [-4.11, 12.68] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 24 | 469.00 ms | 13.04 | 2.66 | [452.00, 488.00] |
| 5b3 | 23 | 470.09 ms | 13.85 | 2.89 | [452.00, 488.00] |
| 5c3 | 24 | 472.00 ms | 13.96 | 2.85 | [452.00, 488.00] |
| 5d3 | 24 | 468.17 ms | 12.17 | 2.48 | [452.00, 488.00] |
| 5e3 | 19 | 471.16 ms | 12.69 | 2.91 | [452.00, 488.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 5a3 | 24 | 4.19 µV | 2.48 | 0.51 | [-0.43, 9.34] |
| 5b3 | 23 | 5.08 µV | 5.47 | 1.14 | [-9.40, 15.91] |
| 5c3 | 24 | 5.11 µV | 3.01 | 0.62 | [-1.50, 10.99] |
| 5d3 | 24 | 5.68 µV | 3.58 | 0.73 | [-0.81, 12.97] |
| 5e3 | 19 | 5.42 µV | 5.50 | 1.26 | [-3.60, 13.24] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 944.08, BIC = 965.97
- **5b3 vs 5a3**: *β* = -1.30, *SE* = 4.160, *z* = -0.313, *p* = 0.754
- **5c3 vs 5a3**: *β* = 3.06, *SE* = 4.002, *z* = 0.764, *p* = 0.445
- **5d3 vs 5a3**: *β* = 0.01, *SE* = 4.097, *z* = 0.002, *p* = 0.998
- **5e3 vs 5a3**: *β* = -0.65, *SE* = 4.337, *z* = -0.151, *p* = 0.880
- **SNR**: *β* = 0.77, *SE* = 0.904, *z* = 0.847, *p* = 0.397

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 1.30 | 4.16 | 0.31 | 0.754 | 1.000 | n.s. |
| 5a3 - 5c3 | -3.06 | 4.00 | -0.76 | 0.445 | 0.991 | n.s. |
| 5a3 - 5d3 | -0.01 | 4.10 | -0.00 | 0.998 | 1.000 | n.s. |
| 5a3 - 5e3 | 0.65 | 4.34 | 0.15 | 0.880 | 1.000 | n.s. |
| 5b3 - 5c3 | -4.36 | 4.07 | -1.07 | 0.284 | 0.964 | n.s. |
| 5b3 - 5d3 | -1.31 | 4.02 | -0.33 | 0.745 | 1.000 | n.s. |
| 5b3 - 5e3 | -0.65 | 4.29 | -0.15 | 0.880 | 1.000 | n.s. |
| 5c3 - 5d3 | 3.05 | 4.01 | 0.76 | 0.447 | 0.991 | n.s. |
| 5c3 - 5e3 | 3.71 | 4.27 | 0.87 | 0.384 | 0.987 | n.s. |
| 5d3 - 5e3 | 0.66 | 4.25 | 0.16 | 0.876 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.46, *p* = 0.761, η²_G = 0.018
- Greenhouse-Geisser corrected: *p* = 0.662 (ε = 0.587)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.91 | 18 | = 0.876 | 0.33 [-0.29, 0.58] | small | n.s. |
| 5a3 vs 5c3 | -0.18 | 18 | = 0.884 | -0.06 [-0.56, 0.29] | negligible | n.s. |
| 5a3 vs 5d3 | 1.20 | 18 | = 0.876 | 0.22 [-0.36, 0.48] | small | n.s. |
| 5a3 vs 5e3 | 0.46 | 18 | = 0.884 | 0.17 [-0.38, 0.59] | negligible | n.s. |
| 5b3 vs 5c3 | -1.30 | 18 | = 0.876 | -0.36 [-0.77, 0.12] | small | n.s. |
| 5b3 vs 5d3 | -0.18 | 18 | = 0.884 | -0.06 [-0.48, 0.38] | negligible | n.s. |
| 5b3 vs 5e3 | -0.56 | 18 | = 0.884 | -0.12 [-0.61, 0.36] | negligible | n.s. |
| 5c3 vs 5d3 | 0.79 | 18 | = 0.876 | 0.26 [-0.27, 0.58] | small | n.s. |
| 5c3 vs 5e3 | 0.84 | 18 | = 0.876 | 0.22 [-0.29, 0.68] | small | n.s. |
| 5d3 vs 5e3 | -0.15 | 18 | = 0.884 | -0.05 [-0.52, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 635.33, BIC = 657.22
- **5b3 vs 5a3**: *β* = -2.21, *SE* = 1.018, *z* = -2.173, *p* = 0.030
- **5c3 vs 5a3**: *β* = -2.26, *SE* = 0.978, *z* = -2.308, *p* = 0.021
- **5d3 vs 5a3**: *β* = -0.73, *SE* = 1.004, *z* = -0.724, *p* = 0.469
- **5e3 vs 5a3**: *β* = -3.27, *SE* = 1.068, *z* = -3.064, *p* = 0.002
- **SNR**: *β* = -1.20, *SE* = 0.232, *z* = -5.152, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 2.21 | 1.02 | 2.17 | 0.030 | 0.191 | n.s. |
| 5a3 - 5c3 | 2.26 | 0.98 | 2.31 | 0.021 | 0.156 | n.s. |
| 5a3 - 5d3 | 0.73 | 1.00 | 0.72 | 0.469 | 0.776 | n.s. |
| 5a3 - 5e3 | 3.27 | 1.07 | 3.06 | 0.002 | 0.022 | * |
| 5b3 - 5c3 | 0.04 | 0.99 | 0.04 | 0.965 | 0.965 | n.s. |
| 5b3 - 5d3 | -1.49 | 0.98 | -1.51 | 0.131 | 0.531 | n.s. |
| 5b3 - 5e3 | 1.06 | 1.05 | 1.01 | 0.312 | 0.776 | n.s. |
| 5c3 - 5d3 | -1.53 | 0.98 | -1.56 | 0.119 | 0.531 | n.s. |
| 5c3 - 5e3 | 1.02 | 1.05 | 0.97 | 0.332 | 0.776 | n.s. |
| 5d3 - 5e3 | 2.55 | 1.04 | 2.45 | 0.014 | 0.122 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.18, *p* = 0.326, η²_G = 0.045
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 0.33 | 18 | = 0.786 | 0.09 [-0.30, 0.57] | negligible | n.s. |
| 5a3 vs 5c3 | 1.04 | 18 | = 0.534 | 0.29 [-0.10, 0.77] | small | n.s. |
| 5a3 vs 5d3 | -1.02 | 18 | = 0.534 | -0.27 [-0.57, 0.28] | small | n.s. |
| 5a3 vs 5e3 | 1.14 | 18 | = 0.534 | 0.37 [-0.23, 0.75] | small | n.s. |
| 5b3 vs 5c3 | 0.63 | 18 | = 0.674 | 0.19 [-0.28, 0.59] | negligible | n.s. |
| 5b3 vs 5d3 | -1.15 | 18 | = 0.534 | -0.33 [-0.78, 0.11] | small | n.s. |
| 5b3 vs 5e3 | 0.73 | 18 | = 0.674 | 0.27 [-0.32, 0.65] | small | n.s. |
| 5c3 vs 5d3 | -2.28 | 18 | = 0.353 | -0.50 [-1.02, -0.11] | small | n.s. |
| 5c3 vs 5e3 | 0.28 | 18 | = 0.786 | 0.09 [-0.42, 0.55] | negligible | n.s. |
| 5d3 vs 5e3 | 1.74 | 18 | = 0.495 | 0.56 [-0.10, 0.90] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 1035.29, BIC = 1057.18
- **5b3 vs 5a3**: *β* = 7.67, *SE* = 5.773, *z* = 1.328, *p* = 0.184
- **5c3 vs 5a3**: *β* = 0.17, *SE* = 5.697, *z* = 0.030, *p* = 0.976
- **5d3 vs 5a3**: *β* = 2.42, *SE* = 5.577, *z* = 0.433, *p* = 0.665
- **5e3 vs 5a3**: *β* = 5.45, *SE* = 6.028, *z* = 0.904, *p* = 0.366
- **SNR**: *β* = 1.33, *SE* = 1.301, *z* = 1.023, *p* = 0.306

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -7.67 | 5.77 | -1.33 | 0.184 | 0.860 | n.s. |
| 5a3 - 5c3 | -0.17 | 5.70 | -0.03 | 0.976 | 0.991 | n.s. |
| 5a3 - 5d3 | -2.42 | 5.58 | -0.43 | 0.665 | 0.991 | n.s. |
| 5a3 - 5e3 | -5.45 | 6.03 | -0.90 | 0.366 | 0.968 | n.s. |
| 5b3 - 5c3 | 7.50 | 5.57 | 1.34 | 0.179 | 0.860 | n.s. |
| 5b3 - 5d3 | 5.25 | 5.61 | 0.94 | 0.349 | 0.968 | n.s. |
| 5b3 - 5e3 | 2.21 | 5.96 | 0.37 | 0.710 | 0.991 | n.s. |
| 5c3 - 5d3 | -2.25 | 5.53 | -0.41 | 0.685 | 0.991 | n.s. |
| 5c3 - 5e3 | -5.28 | 5.91 | -0.89 | 0.372 | 0.968 | n.s. |
| 5d3 - 5e3 | -3.04 | 5.92 | -0.51 | 0.608 | 0.991 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.45, *p* = 0.772, η²_G = 0.014
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -0.59 | 18 | = 0.856 | -0.16 [-0.65, 0.23] | negligible | n.s. |
| 5a3 vs 5c3 | 0.71 | 18 | = 0.856 | 0.14 [-0.35, 0.49] | negligible | n.s. |
| 5a3 vs 5d3 | -0.54 | 18 | = 0.856 | -0.16 [-0.48, 0.37] | negligible | n.s. |
| 5a3 vs 5e3 | -0.57 | 18 | = 0.856 | -0.18 [-0.61, 0.35] | negligible | n.s. |
| 5b3 vs 5c3 | 0.93 | 18 | = 0.856 | 0.27 [-0.19, 0.69] | small | n.s. |
| 5b3 vs 5d3 | 0.06 | 18 | = 1.000 | 0.02 [-0.28, 0.59] | negligible | n.s. |
| 5b3 vs 5e3 | 0.00 | 18 | = 1.000 | 0.00 [-0.48, 0.48] | negligible | n.s. |
| 5c3 vs 5d3 | -1.08 | 18 | = 0.856 | -0.28 [-0.53, 0.31] | small | n.s. |
| 5c3 vs 5e3 | -1.13 | 18 | = 0.856 | -0.31 [-0.75, 0.23] | small | n.s. |
| 5d3 vs 5e3 | -0.07 | 18 | = 1.000 | -0.02 [-0.50, 0.47] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 581.33, BIC = 603.22
- **5b3 vs 5a3**: *β* = -2.38, *SE* = 0.762, *z* = -3.121, *p* = 0.002
- **5c3 vs 5a3**: *β* = -1.08, *SE* = 0.752, *z* = -1.431, *p* = 0.152
- **5d3 vs 5a3**: *β* = -0.90, *SE* = 0.735, *z* = -1.221, *p* = 0.222
- **5e3 vs 5a3**: *β* = -3.58, *SE* = 0.796, *z* = -4.492, *p* < .001
- **SNR**: *β* = -1.04, *SE* = 0.180, *z* = -5.813, *p* < .001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | 2.38 | 0.76 | 3.12 | 0.002 | 0.013 | * |
| 5a3 - 5c3 | 1.08 | 0.75 | 1.43 | 0.152 | 0.422 | n.s. |
| 5a3 - 5d3 | 0.90 | 0.73 | 1.22 | 0.222 | 0.422 | n.s. |
| 5a3 - 5e3 | 3.58 | 0.80 | 4.49 | < .001 | < .001 | *** |
| 5b3 - 5c3 | -1.30 | 0.73 | -1.78 | 0.076 | 0.326 | n.s. |
| 5b3 - 5d3 | -1.48 | 0.74 | -2.01 | 0.045 | 0.241 | n.s. |
| 5b3 - 5e3 | 1.20 | 0.79 | 1.52 | 0.128 | 0.422 | n.s. |
| 5c3 - 5d3 | -0.18 | 0.73 | -0.25 | 0.806 | 0.806 | n.s. |
| 5c3 - 5e3 | 2.50 | 0.78 | 3.20 | 0.001 | 0.011 | * |
| 5d3 - 5e3 | 2.68 | 0.78 | 3.43 | < .001 | 0.005 | ** |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.39, *p* = 0.013, η²_G = 0.087
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | 1.68 | 18 | = 0.222 | 0.43 [-0.14, 0.74] | small | n.s. |
| 5a3 vs 5c3 | 0.00 | 18 | = 0.998 | 0.00 [-0.45, 0.40] | negligible | n.s. |
| 5a3 vs 5d3 | 1.47 | 18 | = 0.266 | 0.29 [-0.36, 0.49] | small | n.s. |
| 5a3 vs 5e3 | 3.27 | 18 | = 0.042 | 0.87 [0.20, 1.30] | large | * |
| 5b3 vs 5c3 | -1.89 | 18 | = 0.186 | -0.40 [-0.71, 0.17] | small | n.s. |
| 5b3 vs 5d3 | -1.01 | 18 | = 0.406 | -0.24 [-0.70, 0.18] | small | n.s. |
| 5b3 vs 5e3 | 0.85 | 18 | = 0.450 | 0.24 [-0.29, 0.68] | small | n.s. |
| 5c3 vs 5d3 | 1.03 | 18 | = 0.406 | 0.26 [-0.35, 0.50] | small | n.s. |
| 5c3 vs 5e3 | 2.64 | 18 | = 0.079 | 0.80 [0.08, 1.13] | medium | n.s. |
| 5d3 vs 5e3 | 2.47 | 18 | = 0.079 | 0.65 [0.05, 1.09] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 978.85, BIC = 1000.74
- **5b3 vs 5a3**: *β* = 5.54, *SE* = 4.824, *z* = 1.147, *p* = 0.251
- **5c3 vs 5a3**: *β* = 9.77, *SE* = 4.794, *z* = 2.037, *p* = 0.042
- **5d3 vs 5a3**: *β* = 5.00, *SE* = 4.840, *z* = 1.034, *p* = 0.301
- **5e3 vs 5a3**: *β* = -3.36, *SE* = 5.070, *z* = -0.662, *p* = 0.508
- **SNR**: *β* = 1.71, *SE* = 1.405, *z* = 1.215, *p* = 0.224

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -5.54 | 4.82 | -1.15 | 0.251 | 0.824 | n.s. |
| 5a3 - 5c3 | -9.77 | 4.79 | -2.04 | 0.042 | 0.318 | n.s. |
| 5a3 - 5d3 | -5.00 | 4.84 | -1.03 | 0.301 | 0.833 | n.s. |
| 5a3 - 5e3 | 3.36 | 5.07 | 0.66 | 0.508 | 0.833 | n.s. |
| 5b3 - 5c3 | -4.23 | 4.73 | -0.89 | 0.371 | 0.833 | n.s. |
| 5b3 - 5d3 | 0.53 | 4.74 | 0.11 | 0.911 | 0.911 | n.s. |
| 5b3 - 5e3 | 8.89 | 5.04 | 1.76 | 0.078 | 0.478 | n.s. |
| 5c3 - 5d3 | 4.76 | 4.68 | 1.02 | 0.309 | 0.833 | n.s. |
| 5c3 - 5e3 | 13.12 | 5.00 | 2.62 | 0.009 | 0.084 | n.s. |
| 5d3 - 5e3 | 8.36 | 5.01 | 1.67 | 0.095 | 0.505 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.364, η²_G = 0.044
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -0.71 | 18 | = 0.684 | -0.23 [-0.60, 0.27] | small | n.s. |
| 5a3 vs 5c3 | -1.34 | 18 | = 0.653 | -0.41 [-0.87, 0.02] | small | n.s. |
| 5a3 vs 5d3 | -0.57 | 18 | = 0.684 | -0.13 [-0.62, 0.23] | negligible | n.s. |
| 5a3 vs 5e3 | 0.70 | 18 | = 0.684 | 0.25 [-0.33, 0.64] | small | n.s. |
| 5b3 vs 5c3 | -0.51 | 18 | = 0.684 | -0.17 [-0.60, 0.27] | negligible | n.s. |
| 5b3 vs 5d3 | 0.24 | 18 | = 0.816 | 0.08 [-0.38, 0.48] | negligible | n.s. |
| 5b3 vs 5e3 | 1.41 | 18 | = 0.653 | 0.46 [-0.17, 0.82] | small | n.s. |
| 5c3 vs 5d3 | 0.83 | 18 | = 0.684 | 0.24 [-0.20, 0.66] | small | n.s. |
| 5c3 vs 5e3 | 2.19 | 18 | = 0.420 | 0.63 [-0.01, 1.01] | medium | n.s. |
| 5d3 vs 5e3 | 0.98 | 18 | = 0.684 | 0.35 [-0.26, 0.71] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 649.46, BIC = 671.35
- **5b3 vs 5a3**: *β* = 1.51, *SE* = 1.121, *z* = 1.343, *p* = 0.179
- **5c3 vs 5a3**: *β* = 1.88, *SE* = 1.114, *z* = 1.690, *p* = 0.091
- **5d3 vs 5a3**: *β* = 1.24, *SE* = 1.125, *z* = 1.098, *p* = 0.272
- **5e3 vs 5a3**: *β* = 2.10, *SE* = 1.180, *z* = 1.783, *p* = 0.075
- **SNR**: *β* = 1.11, *SE* = 0.330, *z* = 3.361, *p* = 0.001

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -1.51 | 1.12 | -1.34 | 0.179 | 0.794 | n.s. |
| 5a3 - 5c3 | -1.88 | 1.11 | -1.69 | 0.091 | 0.576 | n.s. |
| 5a3 - 5d3 | -1.23 | 1.13 | -1.10 | 0.272 | 0.892 | n.s. |
| 5a3 - 5e3 | -2.10 | 1.18 | -1.78 | 0.075 | 0.540 | n.s. |
| 5b3 - 5c3 | -0.38 | 1.10 | -0.34 | 0.732 | 0.982 | n.s. |
| 5b3 - 5d3 | 0.27 | 1.10 | 0.25 | 0.806 | 0.982 | n.s. |
| 5b3 - 5e3 | -0.60 | 1.17 | -0.51 | 0.610 | 0.982 | n.s. |
| 5c3 - 5d3 | 0.65 | 1.09 | 0.60 | 0.551 | 0.982 | n.s. |
| 5c3 - 5e3 | -0.22 | 1.16 | -0.19 | 0.849 | 0.982 | n.s. |
| 5d3 - 5e3 | -0.87 | 1.16 | -0.75 | 0.455 | 0.974 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.48, *p* = 0.752, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -0.47 | 18 | = 0.874 | -0.15 [-0.54, 0.33] | negligible | n.s. |
| 5a3 vs 5c3 | -0.82 | 18 | = 0.874 | -0.25 [-0.65, 0.21] | small | n.s. |
| 5a3 vs 5d3 | 0.40 | 18 | = 0.874 | 0.13 [-0.47, 0.37] | negligible | n.s. |
| 5a3 vs 5e3 | -0.79 | 18 | = 0.874 | -0.29 [-0.67, 0.30] | small | n.s. |
| 5b3 vs 5c3 | -0.17 | 18 | = 0.874 | -0.05 [-0.49, 0.37] | negligible | n.s. |
| 5b3 vs 5d3 | 0.71 | 18 | = 0.874 | 0.24 [-0.35, 0.52] | small | n.s. |
| 5b3 vs 5e3 | -0.27 | 18 | = 0.874 | -0.09 [-0.54, 0.42] | negligible | n.s. |
| 5c3 vs 5d3 | 1.95 | 18 | = 0.665 | 0.37 [-0.17, 0.69] | small | n.s. |
| 5c3 vs 5e3 | -0.16 | 18 | = 0.874 | -0.05 [-0.52, 0.45] | negligible | n.s. |
| 5d3 vs 5e3 | -1.17 | 18 | = 0.874 | -0.39 [-0.76, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 921.70, BIC = 943.59
- **5b3 vs 5a3**: *β* = 1.07, *SE* = 3.751, *z* = 0.285, *p* = 0.776
- **5c3 vs 5a3**: *β* = 2.77, *SE* = 3.723, *z* = 0.744, *p* = 0.457
- **5d3 vs 5a3**: *β* = -0.83, *SE* = 3.710, *z* = -0.223, *p* = 0.823
- **5e3 vs 5a3**: *β* = 1.76, *SE* = 3.991, *z* = 0.441, *p* = 0.659
- **SNR**: *β* = -0.58, *SE* = 0.784, *z* = -0.736, *p* = 0.462

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -1.07 | 3.75 | -0.29 | 0.776 | 0.999 | n.s. |
| 5a3 - 5c3 | -2.77 | 3.72 | -0.74 | 0.457 | 0.996 | n.s. |
| 5a3 - 5d3 | 0.83 | 3.71 | 0.22 | 0.823 | 0.999 | n.s. |
| 5a3 - 5e3 | -1.76 | 3.99 | -0.44 | 0.659 | 0.999 | n.s. |
| 5b3 - 5c3 | -1.70 | 3.76 | -0.45 | 0.651 | 0.999 | n.s. |
| 5b3 - 5d3 | 1.90 | 3.75 | 0.51 | 0.613 | 0.999 | n.s. |
| 5b3 - 5e3 | -0.69 | 4.02 | -0.17 | 0.863 | 0.999 | n.s. |
| 5c3 - 5d3 | 3.60 | 3.72 | 0.97 | 0.334 | 0.983 | n.s. |
| 5c3 - 5e3 | 1.01 | 3.96 | 0.26 | 0.799 | 0.999 | n.s. |
| 5d3 - 5e3 | -2.59 | 3.99 | -0.65 | 0.517 | 0.997 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.64, *p* = 0.637, η²_G = 0.028
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -0.61 | 18 | = 0.782 | -0.19 [-0.54, 0.32] | negligible | n.s. |
| 5a3 vs 5c3 | -1.25 | 18 | = 0.782 | -0.44 [-0.58, 0.27] | small | n.s. |
| 5a3 vs 5d3 | -0.21 | 18 | = 0.837 | -0.05 [-0.36, 0.48] | negligible | n.s. |
| 5a3 vs 5e3 | -0.92 | 18 | = 0.782 | -0.33 [-0.70, 0.28] | small | n.s. |
| 5b3 vs 5c3 | -0.68 | 18 | = 0.782 | -0.24 [-0.51, 0.35] | small | n.s. |
| 5b3 vs 5d3 | 0.62 | 18 | = 0.782 | 0.14 [-0.30, 0.57] | negligible | n.s. |
| 5b3 vs 5e3 | -0.32 | 18 | = 0.837 | -0.13 [-0.56, 0.41] | negligible | n.s. |
| 5c3 vs 5d3 | 1.18 | 18 | = 0.782 | 0.39 [-0.21, 0.64] | small | n.s. |
| 5c3 vs 5e3 | 0.43 | 18 | = 0.837 | 0.13 [-0.38, 0.58] | negligible | n.s. |
| 5d3 vs 5e3 | -0.76 | 18 | = 0.782 | -0.28 [-0.66, 0.31] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 637.18, BIC = 659.07
- **5b3 vs 5a3**: *β* = 0.88, *SE* = 0.963, *z* = 0.910, *p* = 0.363
- **5c3 vs 5a3**: *β* = 1.13, *SE* = 0.955, *z* = 1.179, *p* = 0.238
- **5d3 vs 5a3**: *β* = 1.49, *SE* = 0.951, *z* = 1.561, *p* = 0.119
- **5e3 vs 5a3**: *β* = 1.27, *SE* = 1.035, *z* = 1.227, *p* = 0.220
- **SNR**: *β* = 0.50, *SE* = 0.219, *z* = 2.300, *p* = 0.021

_Reference condition: **5a3** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 5a3 - 5b3 | -0.88 | 0.96 | -0.91 | 0.363 | 0.957 | n.s. |
| 5a3 - 5c3 | -1.13 | 0.96 | -1.18 | 0.238 | 0.893 | n.s. |
| 5a3 - 5d3 | -1.48 | 0.95 | -1.56 | 0.119 | 0.717 | n.s. |
| 5a3 - 5e3 | -1.27 | 1.03 | -1.23 | 0.220 | 0.893 | n.s. |
| 5b3 - 5c3 | -0.25 | 0.97 | -0.26 | 0.796 | 0.998 | n.s. |
| 5b3 - 5d3 | -0.61 | 0.96 | -0.63 | 0.528 | 0.989 | n.s. |
| 5b3 - 5e3 | -0.39 | 1.04 | -0.38 | 0.706 | 0.998 | n.s. |
| 5c3 - 5d3 | -0.36 | 0.96 | -0.38 | 0.707 | 0.998 | n.s. |
| 5c3 - 5e3 | -0.14 | 1.03 | -0.14 | 0.889 | 0.998 | n.s. |
| 5d3 - 5e3 | 0.22 | 1.04 | 0.21 | 0.835 | 0.998 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 10 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.50, *p* = 0.738, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 5a3 vs 5b3 | -1.24 | 18 | = 0.775 | -0.36 [-0.59, 0.28] | small | n.s. |
| 5a3 vs 5c3 | -1.39 | 18 | = 0.775 | -0.39 [-0.71, 0.15] | small | n.s. |
| 5a3 vs 5d3 | -1.41 | 18 | = 0.775 | -0.41 [-0.86, 0.02] | small | n.s. |
| 5a3 vs 5e3 | -0.67 | 18 | = 0.934 | -0.20 [-0.64, 0.33] | negligible | n.s. |
| 5b3 vs 5c3 | 0.22 | 18 | = 0.934 | 0.07 [-0.44, 0.43] | negligible | n.s. |
| 5b3 vs 5d3 | 0.05 | 18 | = 0.964 | 0.01 [-0.58, 0.29] | negligible | n.s. |
| 5b3 vs 5e3 | 0.34 | 18 | = 0.934 | 0.09 [-0.40, 0.56] | negligible | n.s. |
| 5c3 vs 5d3 | -0.26 | 18 | = 0.934 | -0.07 [-0.56, 0.29] | negligible | n.s. |
| 5c3 vs 5e3 | 0.20 | 18 | = 0.934 | 0.05 [-0.44, 0.53] | negligible | n.s. |
| 5d3 vs 5e3 | 0.36 | 18 | = 0.934 | 0.09 [-0.40, 0.57] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.013). Post-hoc tests revealed:
  - 5a3 showed greater amplitude than 5e3 (*d* = 0.87)

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
