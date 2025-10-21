# Statistical Analysis Report: tables

**Generated:** 2025-10-20 22:52:49

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 4

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
| Crossover (with 1) | 23 | -3.78 µV | 1.89 | 0.39 | [-8.17, -0.22] |
| Crossover (without 1) | 23 | -3.71 µV | 1.72 | 0.36 | [-7.84, -0.43] |
| Small (with 1) | 23 | -3.40 µV | 1.44 | 0.30 | [-6.17, -0.12] |
| Small (without 1) | 21 | -3.35 µV | 1.36 | 0.30 | [-5.70, -0.81] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 23 | 172.89 ms | 11.86 | 2.47 | [152.58, 206.00] |
| Crossover (without 1) | 23 | 172.35 ms | 11.90 | 2.48 | [152.31, 204.66] |
| Small (with 1) | 23 | 172.54 ms | 11.44 | 2.38 | [151.42, 207.50] |
| Small (without 1) | 21 | 171.07 ms | 9.22 | 2.01 | [151.68, 195.11] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 14 | 1.04 µV | 1.19 | 0.32 | [-0.09, 3.90] |
| Crossover (without 1) | 15 | 0.92 µV | 1.34 | 0.35 | [0.02, 4.72] |
| Small (with 1) | 12 | 1.33 µV | 0.82 | 0.24 | [0.08, 2.61] |
| Small (without 1) | 12 | 1.91 µV | 1.35 | 0.39 | [0.05, 4.56] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 14 | 99.57 ms | 7.62 | 2.04 | [80.98, 111.97] |
| Crossover (without 1) | 15 | 99.67 ms | 8.15 | 2.10 | [82.74, 110.18] |
| Small (with 1) | 12 | 96.69 ms | 6.23 | 1.80 | [81.19, 104.60] |
| Small (without 1) | 12 | 98.24 ms | 5.07 | 1.46 | [89.58, 106.20] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 19 | 3.41 µV | 2.10 | 0.48 | [0.37, 7.71] |
| Crossover (without 1) | 19 | 3.30 µV | 2.02 | 0.46 | [0.08, 6.78] |
| Small (with 1) | 19 | 3.57 µV | 2.87 | 0.66 | [0.02, 11.11] |
| Small (without 1) | 18 | 4.02 µV | 2.77 | 0.65 | [0.18, 9.71] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 19 | 468.66 ms | 11.71 | 2.69 | [446.03, 498.13] |
| Crossover (without 1) | 19 | 469.21 ms | 18.56 | 4.26 | [427.14, 526.61] |
| Small (with 1) | 19 | 463.97 ms | 15.41 | 3.54 | [437.44, 497.37] |
| Small (without 1) | 18 | 458.98 ms | 20.96 | 4.94 | [409.15, 506.22] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 270.08, BIC = 287.58
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.12, *SE* = 0.238, *z* = -0.524, *p* = 0.601
- **Small (with 1) vs Crossover (with 1)**: *β* = -0.30, *SE* = 0.258, *z* = -1.148, *p* = 0.251
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.56, *SE* = 0.303, *z* = -1.832, *p* = 0.067
- **SNR**: *β* = -0.19, *SE* = 0.027, *z* = -6.845, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.12 | 0.24 | 0.52 | 0.601 | 0.739 | n.s. |
| Crossover (with 1) - Small (with 1) | 0.30 | 0.26 | 1.15 | 0.251 | 0.685 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.56 | 0.30 | 1.83 | 0.067 | 0.340 | n.s. |
| Crossover (without 1) - Small (with 1) | 0.17 | 0.25 | 0.69 | 0.489 | 0.739 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.43 | 0.29 | 1.50 | 0.133 | 0.510 | n.s. |
| Small (with 1) - Small (without 1) | 0.26 | 0.26 | 1.01 | 0.314 | 0.685 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.41, *p* = 0.076, η²_G = 0.040
- Greenhouse-Geisser corrected: *p* = 0.120 (ε = 0.494)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -1.51 | 20 | = 0.257 | -0.06 [-0.69, 0.19] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -1.24 | 20 | = 0.274 | -0.27 [-0.72, 0.18] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | -1.88 | 20 | = 0.257 | -0.48 [-0.88, 0.06] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.97 | 20 | = 0.343 | -0.22 [-0.67, 0.23] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | -1.70 | 20 | = 0.257 | -0.44 [-0.84, 0.10] | small | n.s. |
| Small (with 1) vs Small (without 1) | -1.42 | 20 | = 0.257 | -0.28 [-0.78, 0.16] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 582.72, BIC = 600.22
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.22, *SE* = 1.013, *z* = -0.214, *p* = 0.831
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.98, *SE* = 1.122, *z* = 0.873, *p* = 0.383
- **Small (without 1) vs Crossover (with 1)**: *β* = 2.78, *SE* = 1.334, *z* = 2.085, *p* = 0.037
- **SNR**: *β* = 0.30, *SE* = 0.126, *z* = 2.414, *p* = 0.016

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.22 | 1.01 | 0.21 | 0.831 | 0.831 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.98 | 1.12 | -0.87 | 0.383 | 0.619 | n.s. |
| Crossover (with 1) - Small (without 1) | -2.78 | 1.33 | -2.08 | 0.037 | 0.172 | n.s. |
| Crossover (without 1) - Small (with 1) | -1.20 | 1.07 | -1.11 | 0.265 | 0.603 | n.s. |
| Crossover (without 1) - Small (without 1) | -3.00 | 1.25 | -2.39 | 0.017 | 0.097 | n.s. |
| Small (with 1) - Small (without 1) | -1.80 | 1.11 | -1.63 | 0.104 | 0.354 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.48, *p* = 0.696, η²_G = 0.004
- Greenhouse-Geisser corrected: *p* = 0.550 (ε = 0.451)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.24 | 20 | = 0.700 | 0.05 [-0.11, 0.78] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.21 | 20 | = 0.839 | 0.03 [-0.41, 0.47] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.55 | 20 | = 0.839 | -0.10 [-0.58, 0.34] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.21 | 20 | = 0.839 | -0.03 [-0.51, 0.37] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.84 | 20 | = 0.820 | -0.15 [-0.64, 0.28] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | -1.23 | 20 | = 0.700 | -0.13 [-0.73, 0.20] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 127.74, BIC = 141.53
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.16, *SE* = 0.256, *z* = 0.623, *p* = 0.533
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.53, *SE* = 0.272, *z* = 1.961, *p* = 0.050
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.36, *SE* = 0.280, *z* = 4.882, *p* < .001
- **SNR**: *β* = 0.39, *SE* = 0.047, *z* = 8.202, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.16 | 0.26 | -0.62 | 0.533 | 0.533 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.53 | 0.27 | -1.96 | 0.050 | 0.142 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.37 | 0.28 | -4.88 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.37 | 0.26 | -1.41 | 0.158 | 0.291 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.21 | 0.27 | -4.49 | < .001 | < .001 | *** |
| Small (with 1) - Small (without 1) | -0.83 | 0.28 | -2.97 | 0.003 | 0.012 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.10, *p* = 0.959, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.804 (ε = 0.397)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.30 | 5 | = 0.908 | 0.04 [-0.57, 0.78] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.87 | 5 | = 0.908 | 0.29 [-0.65, 0.78] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.22 | 5 | = 0.908 | 0.13 [-1.02, 0.67] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | 0.48 | 5 | = 0.908 | 0.19 [-0.85, 0.59] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.12 | 5 | = 0.908 | 0.07 [-1.08, 0.61] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | -0.25 | 5 | = 0.908 | -0.14 [-1.14, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 358.57, BIC = 372.36
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.01, *SE* = 1.926, *z* = 0.007, *p* = 0.994
- **Small (with 1) vs Crossover (with 1)**: *β* = -1.93, *SE* = 2.047, *z* = -0.941, *p* = 0.347
- **Small (without 1) vs Crossover (with 1)**: *β* = -1.20, *SE* = 2.191, *z* = -0.550, *p* = 0.583
- **SNR**: *β* = 0.02, *SE* = 0.375, *z* = 0.064, *p* = 0.949

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.01 | 1.93 | -0.01 | 0.994 | 0.994 | n.s. |
| Crossover (with 1) - Small (with 1) | 1.93 | 2.05 | 0.94 | 0.347 | 0.913 | n.s. |
| Crossover (with 1) - Small (without 1) | 1.20 | 2.19 | 0.55 | 0.583 | 0.964 | n.s. |
| Crossover (without 1) - Small (with 1) | 1.94 | 2.01 | 0.96 | 0.335 | 0.913 | n.s. |
| Crossover (without 1) - Small (without 1) | 1.22 | 2.12 | 0.58 | 0.565 | 0.964 | n.s. |
| Small (with 1) - Small (without 1) | -0.72 | 2.14 | -0.34 | 0.736 | 0.964 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.70, *p* = 0.567, η²_G = 0.065
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -0.95 | 5 | = 0.673 | -0.34 [-0.63, 0.72] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.83 | 5 | = 0.673 | 0.47 [-0.57, 0.86] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.47 | 5 | = 0.777 | 0.18 [-0.58, 1.12] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | 1.23 | 5 | = 0.673 | 0.68 [-0.35, 1.13] | medium | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.82 | 5 | = 0.673 | 0.40 [-0.65, 1.04] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.30 | 5 | = 0.777 | -0.14 [-0.91, 0.64] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 266.59, BIC = 282.81
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.13, *SE* = 0.307, *z* = 0.413, *p* = 0.680
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.28, *SE* = 0.309, *z* = 0.894, *p* = 0.371
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.31, *SE* = 0.337, *z* = 3.887, *p* < .001
- **SNR**: *β* = 0.23, *SE* = 0.035, *z* = 6.493, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.13 | 0.31 | -0.41 | 0.680 | 0.862 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.28 | 0.31 | -0.89 | 0.371 | 0.752 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.31 | 0.34 | -3.89 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.15 | 0.31 | -0.48 | 0.629 | 0.862 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.18 | 0.33 | -3.63 | < .001 | 0.001 | ** |
| Small (with 1) - Small (without 1) | -1.03 | 0.33 | -3.15 | 0.002 | 0.006 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.67, *p* = 0.576, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.509 (ε = 0.619)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 1.12 | 16 | = 0.607 | 0.06 [-0.23, 0.75] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.54 | 16 | = 0.607 | -0.08 [-0.65, 0.35] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.90 | 16 | = 0.607 | -0.18 [-0.74, 0.30] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.73 | 16 | = 0.607 | -0.13 [-0.69, 0.31] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -1.05 | 16 | = 0.607 | -0.23 [-0.78, 0.27] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.53 | 16 | = 0.607 | -0.09 [-0.69, 0.31] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 624.97, BIC = 641.20
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.46, *SE* = 3.770, *z* = 0.121, *p* = 0.903
- **Small (with 1) vs Crossover (with 1)**: *β* = -4.79, *SE* = 3.788, *z* = -1.265, *p* = 0.206
- **Small (without 1) vs Crossover (with 1)**: *β* = -9.48, *SE* = 4.068, *z* = -2.330, *p* = 0.020
- **SNR**: *β* = -0.09, *SE* = 0.384, *z* = -0.239, *p* = 0.811

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.46 | 3.77 | -0.12 | 0.903 | 0.903 | n.s. |
| Crossover (with 1) - Small (with 1) | 4.79 | 3.79 | 1.26 | 0.206 | 0.516 | n.s. |
| Crossover (with 1) - Small (without 1) | 9.48 | 4.07 | 2.33 | 0.020 | 0.095 | n.s. |
| Crossover (without 1) - Small (with 1) | 5.25 | 3.79 | 1.39 | 0.166 | 0.516 | n.s. |
| Crossover (without 1) - Small (without 1) | 9.94 | 3.96 | 2.51 | 0.012 | 0.070 | n.s. |
| Small (with 1) - Small (without 1) | 4.69 | 3.98 | 1.18 | 0.239 | 0.516 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.03, *p* = 0.038, η²_G = 0.063
- Greenhouse-Geisser corrected: *p* = 0.079 (ε = 0.511)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -0.50 | 16 | = 0.626 | -0.07 [-0.55, 0.42] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 2.80 | 16 | = 0.076 | 0.45 [-0.10, 0.94] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 1.90 | 16 | = 0.133 | 0.54 [-0.08, 1.00] | medium | n.s. |
| Crossover (without 1) vs Small (with 1) | 2.25 | 16 | = 0.118 | 0.41 [-0.16, 0.87] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 1.81 | 16 | = 0.133 | 0.51 [-0.10, 0.98] | medium | n.s. |
| Small (with 1) vs Small (without 1) | 0.78 | 16 | = 0.534 | 0.20 [-0.33, 0.67] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.076)
**P3b latency:** Significant main effect of condition (*p* = 0.038) (no significant pairwise comparisons)

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
