# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:27:06

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
| Crossover (with 1) | 24 | 99.33 ms | 10.72 | 2.19 | [84.00, 112.00] |
| Crossover (without 1) | 24 | 101.00 ms | 9.96 | 2.03 | [84.00, 112.00] |
| Small (with 1) | 24 | 96.50 ms | 11.64 | 2.38 | [84.00, 112.00] |
| Small (without 1) | 24 | 96.17 ms | 11.16 | 2.28 | [84.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | -1.24 µV | 0.95 | 0.19 | [-4.07, 0.07] |
| Crossover (without 1) | 24 | -1.32 µV | 1.13 | 0.23 | [-4.95, 0.11] |
| Small (with 1) | 24 | -0.51 µV | 1.47 | 0.30 | [-3.77, 2.33] |
| Small (without 1) | 24 | -1.47 µV | 2.19 | 0.45 | [-5.76, 2.45] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 170.83 ms | 20.75 | 4.24 | [136.00, 208.00] |
| Crossover (without 1) | 24 | 169.17 ms | 20.51 | 4.19 | [136.00, 208.00] |
| Small (with 1) | 24 | 171.50 ms | 20.95 | 4.28 | [140.00, 208.00] |
| Small (without 1) | 24 | 170.50 ms | 21.49 | 4.39 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | -5.60 µV | 2.25 | 0.46 | [-10.54, -0.89] |
| Crossover (without 1) | 24 | -5.52 µV | 2.09 | 0.43 | [-9.99, -0.85] |
| Small (with 1) | 24 | -5.31 µV | 2.22 | 0.45 | [-10.86, -0.77] |
| Small (without 1) | 24 | -5.04 µV | 2.41 | 0.49 | [-10.61, 0.67] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 98.67 ms | 11.42 | 2.33 | [80.00, 112.00] |
| Crossover (without 1) | 24 | 99.17 ms | 11.43 | 2.33 | [80.00, 112.00] |
| Small (with 1) | 24 | 96.50 ms | 13.72 | 2.80 | [80.00, 112.00] |
| Small (without 1) | 24 | 96.83 ms | 13.86 | 2.83 | [80.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 1.54 µV | 1.38 | 0.28 | [-0.64, 5.19] |
| Crossover (without 1) | 24 | 1.49 µV | 1.59 | 0.32 | [-0.99, 6.32] |
| Small (with 1) | 24 | 0.95 µV | 1.48 | 0.30 | [-1.50, 3.56] |
| Small (without 1) | 24 | 1.72 µV | 2.21 | 0.45 | [-2.42, 6.87] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 471.00 ms | 39.51 | 8.07 | [396.00, 532.00] |
| Crossover (without 1) | 24 | 482.67 ms | 38.54 | 7.87 | [396.00, 532.00] |
| Small (with 1) | 24 | 460.50 ms | 37.57 | 7.67 | [396.00, 532.00] |
| Small (without 1) | 24 | 461.17 ms | 44.22 | 9.03 | [396.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Crossover (with 1) | 24 | 3.50 µV | 3.03 | 0.62 | [-1.79, 8.79] |
| Crossover (without 1) | 24 | 3.42 µV | 2.99 | 0.61 | [-2.20, 8.56] |
| Small (with 1) | 24 | 3.79 µV | 3.50 | 0.71 | [-2.21, 11.98] |
| Small (without 1) | 24 | 4.86 µV | 4.18 | 0.85 | [-3.39, 13.70] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 717.85, BIC = 735.80
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 1.61, *SE* = 2.288, *z* = 0.703, *p* = 0.482
- **Small (with 1) vs Crossover (with 1)**: *β* = -3.22, *SE* = 2.296, *z* = -1.403, *p* = 0.161
- **Small (without 1) vs Crossover (with 1)**: *β* = -3.18, *SE* = 2.288, *z* = -1.390, *p* = 0.165
- **SNR**: *β* = 1.42, *SE* = 0.699, *z* = 2.035, *p* = 0.042

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -1.61 | 2.29 | -0.70 | 0.482 | 0.732 | n.s. |
| Crossover (with 1) - Small (with 1) | 3.22 | 2.30 | 1.40 | 0.161 | 0.504 | n.s. |
| Crossover (with 1) - Small (without 1) | 3.18 | 2.29 | 1.39 | 0.165 | 0.504 | n.s. |
| Crossover (without 1) - Small (with 1) | 4.83 | 2.29 | 2.11 | 0.035 | 0.194 | n.s. |
| Crossover (without 1) - Small (without 1) | 4.79 | 2.29 | 2.09 | 0.036 | 0.194 | n.s. |
| Small (with 1) - Small (without 1) | -0.04 | 2.30 | -0.02 | 0.986 | 0.986 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.146, η²_G = 0.034
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -0.94 | 23 | = 0.427 | -0.16 [-0.62, 0.23] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 1.20 | 23 | = 0.427 | 0.25 [-0.18, 0.67] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 1.09 | 23 | = 0.427 | 0.29 [-0.20, 0.65] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | 2.04 | 23 | = 0.177 | 0.42 [-0.02, 0.86] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 1.99 | 23 | = 0.177 | 0.46 [-0.03, 0.85] | small | n.s. |
| Small (with 1) vs Small (without 1) | 0.13 | 23 | = 0.900 | 0.03 [-0.40, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 343.97, BIC = 361.92
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.07, *SE* = 0.339, *z* = -0.213, *p* = 0.831
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.79, *SE* = 0.340, *z* = 2.310, *p* = 0.021
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.23, *SE* = 0.339, *z* = -0.664, *p* = 0.507
- **SNR**: *β* = -0.20, *SE* = 0.101, *z* = -1.946, *p* = 0.052

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.07 | 0.34 | 0.21 | 0.831 | 0.880 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.79 | 0.34 | -2.31 | 0.021 | 0.081 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.23 | 0.34 | 0.66 | 0.507 | 0.880 | n.s. |
| Crossover (without 1) - Small (with 1) | -0.86 | 0.34 | -2.52 | 0.012 | 0.057 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.15 | 0.34 | 0.45 | 0.652 | 0.880 | n.s. |
| Small (with 1) - Small (without 1) | 1.01 | 0.34 | 2.97 | 0.003 | 0.018 | * |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.97, *p* = 0.038, η²_G = 0.059
- Greenhouse-Geisser corrected: *p* = 0.080 (ε = 0.483)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.80 | 23 | = 0.652 | 0.08 [-0.26, 0.59] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -2.63 | 23 | = 0.030 | -0.59 [-0.99, -0.09] | medium | * |
| Crossover (with 1) vs Small (without 1) | 0.48 | 23 | = 0.763 | 0.13 [-0.33, 0.52] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -3.04 | 23 | = 0.030 | -0.62 [-1.08, -0.16] | medium | * |
| Crossover (without 1) vs Small (without 1) | 0.30 | 23 | = 0.763 | 0.08 [-0.36, 0.48] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 2.71 | 23 | = 0.030 | 0.51 [0.10, 1.01] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 834.92, BIC = 852.88
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -1.41, *SE* = 4.053, *z* = -0.348, *p* = 0.728
- **Small (with 1) vs Crossover (with 1)**: *β* = 1.53, *SE* = 4.338, *z* = 0.352, *p* = 0.725
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.15, *SE* = 4.903, *z* = 0.235, *p* = 0.814
- **SNR**: *β* = 0.25, *SE* = 0.476, *z* = 0.531, *p* = 0.595

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 1.41 | 4.05 | 0.35 | 0.728 | 0.994 | n.s. |
| Crossover (with 1) - Small (with 1) | -1.53 | 4.34 | -0.35 | 0.725 | 0.994 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.15 | 4.90 | -0.24 | 0.814 | 0.994 | n.s. |
| Crossover (without 1) - Small (with 1) | -2.94 | 4.18 | -0.70 | 0.482 | 0.981 | n.s. |
| Crossover (without 1) - Small (without 1) | -2.56 | 4.64 | -0.55 | 0.581 | 0.987 | n.s. |
| Small (with 1) - Small (without 1) | 0.37 | 4.19 | 0.09 | 0.929 | 0.994 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.11, *p* = 0.953, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.859 (ε = 0.551)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.87 | 23 | = 0.952 | 0.08 [-0.25, 0.60] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.18 | 23 | = 0.952 | -0.03 [-0.46, 0.39] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.06 | 23 | = 0.952 | 0.02 [-0.41, 0.43] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.64 | 23 | = 0.952 | -0.11 [-0.55, 0.29] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.25 | 23 | = 0.952 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | 0.27 | 23 | = 0.952 | 0.05 [-0.37, 0.48] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 340.85, BIC = 358.80
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.05, *SE* = 0.282, *z* = -0.191, *p* = 0.849
- **Small (with 1) vs Crossover (with 1)**: *β* = -0.16, *SE* = 0.302, *z* = -0.537, *p* = 0.591
- **Small (without 1) vs Crossover (with 1)**: *β* = -0.23, *SE* = 0.342, *z* = -0.680, *p* = 0.497
- **SNR**: *β* = -0.14, *SE* = 0.033, *z* = -4.045, *p* < .001

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.05 | 0.28 | 0.19 | 0.849 | 0.987 | n.s. |
| Crossover (with 1) - Small (with 1) | 0.16 | 0.30 | 0.54 | 0.591 | 0.987 | n.s. |
| Crossover (with 1) - Small (without 1) | 0.23 | 0.34 | 0.68 | 0.497 | 0.984 | n.s. |
| Crossover (without 1) - Small (with 1) | 0.11 | 0.29 | 0.37 | 0.709 | 0.987 | n.s. |
| Crossover (without 1) - Small (without 1) | 0.18 | 0.32 | 0.55 | 0.581 | 0.987 | n.s. |
| Small (with 1) - Small (without 1) | 0.07 | 0.29 | 0.24 | 0.809 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.39, *p* = 0.252, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.258 (ε = 0.554)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -1.29 | 23 | = 0.422 | -0.04 [-0.69, 0.17] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.92 | 23 | = 0.443 | -0.13 [-0.61, 0.24] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -1.51 | 23 | = 0.422 | -0.24 [-0.74, 0.12] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | -0.69 | 23 | = 0.500 | -0.10 [-0.56, 0.28] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -1.36 | 23 | = 0.422 | -0.21 [-0.71, 0.15] | small | n.s. |
| Small (with 1) vs Small (without 1) | -0.98 | 23 | = 0.443 | -0.11 [-0.63, 0.23] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 746.44, BIC = 764.39
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.69, *SE* = 2.656, *z* = 0.262, *p* = 0.794
- **Small (with 1) vs Crossover (with 1)**: *β* = -2.12, *SE* = 2.649, *z* = -0.799, *p* = 0.424
- **Small (without 1) vs Crossover (with 1)**: *β* = -1.41, *SE* = 2.687, *z* = -0.523, *p* = 0.601
- **SNR**: *β* = 0.56, *SE* = 0.598, *z* = 0.937, *p* = 0.349

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.69 | 2.66 | -0.26 | 0.794 | 0.956 | n.s. |
| Crossover (with 1) - Small (with 1) | 2.12 | 2.65 | 0.80 | 0.424 | 0.937 | n.s. |
| Crossover (with 1) - Small (without 1) | 1.41 | 2.69 | 0.52 | 0.601 | 0.937 | n.s. |
| Crossover (without 1) - Small (with 1) | 2.81 | 2.65 | 1.06 | 0.289 | 0.871 | n.s. |
| Crossover (without 1) - Small (without 1) | 2.10 | 2.66 | 0.79 | 0.430 | 0.937 | n.s. |
| Small (with 1) - Small (without 1) | -0.71 | 2.68 | -0.26 | 0.791 | 0.956 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.47, *p* = 0.701, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.615 (ε = 0.632)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -1.14 | 23 | = 0.640 | -0.04 [-0.66, 0.20] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.82 | 23 | = 0.640 | 0.17 [-0.26, 0.59] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.63 | 23 | = 0.640 | 0.14 [-0.29, 0.55] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | 1.07 | 23 | = 0.640 | 0.21 [-0.21, 0.65] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | 0.78 | 23 | = 0.640 | 0.18 [-0.27, 0.58] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | -0.09 | 23 | = 0.928 | -0.02 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 350.93, BIC = 368.88
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 0.03, *SE* = 0.340, *z* = 0.074, *p* = 0.941
- **Small (with 1) vs Crossover (with 1)**: *β* = -0.57, *SE* = 0.339, *z* = -1.674, *p* = 0.094
- **Small (without 1) vs Crossover (with 1)**: *β* = 0.33, *SE* = 0.345, *z* = 0.969, *p* = 0.333
- **SNR**: *β* = 0.20, *SE* = 0.079, *z* = 2.537, *p* = 0.011

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -0.03 | 0.34 | -0.07 | 0.941 | 0.941 | n.s. |
| Crossover (with 1) - Small (with 1) | 0.57 | 0.34 | 1.67 | 0.094 | 0.345 | n.s. |
| Crossover (with 1) - Small (without 1) | -0.33 | 0.34 | -0.97 | 0.333 | 0.703 | n.s. |
| Crossover (without 1) - Small (with 1) | 0.59 | 0.34 | 1.74 | 0.081 | 0.345 | n.s. |
| Crossover (without 1) - Small (without 1) | -0.31 | 0.34 | -0.91 | 0.365 | 0.703 | n.s. |
| Small (with 1) - Small (without 1) | -0.90 | 0.34 | -2.63 | 0.009 | 0.051 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.78, *p* = 0.159, η²_G = 0.029
- Greenhouse-Geisser corrected: *p* = 0.192 (ε = 0.449)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.44 | 23 | = 0.696 | 0.03 [-0.33, 0.51] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | 2.06 | 23 | = 0.152 | 0.41 [-0.02, 0.86] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | -0.40 | 23 | = 0.696 | -0.10 [-0.50, 0.34] | negligible | n.s. |
| Crossover (without 1) vs Small (with 1) | 1.67 | 23 | = 0.215 | 0.35 [-0.09, 0.78] | small | n.s. |
| Crossover (without 1) vs Small (without 1) | -0.46 | 23 | = 0.696 | -0.12 [-0.52, 0.33] | negligible | n.s. |
| Small (with 1) vs Small (without 1) | -2.62 | 23 | = 0.093 | -0.41 [-0.99, -0.08] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 975.20, BIC = 993.15
- **Crossover (without 1) vs Crossover (with 1)**: *β* = 11.68, *SE* = 8.985, *z* = 1.300, *p* = 0.194
- **Small (with 1) vs Crossover (with 1)**: *β* = -10.49, *SE* = 8.972, *z* = -1.170, *p* = 0.242
- **Small (without 1) vs Crossover (with 1)**: *β* = -9.80, *SE* = 9.348, *z* = -1.048, *p* = 0.295
- **SNR**: *β* = 0.01, *SE* = 0.932, *z* = 0.013, *p* = 0.990

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | -11.68 | 8.98 | -1.30 | 0.194 | 0.577 | n.s. |
| Crossover (with 1) - Small (with 1) | 10.49 | 8.97 | 1.17 | 0.242 | 0.577 | n.s. |
| Crossover (with 1) - Small (without 1) | 9.80 | 9.35 | 1.05 | 0.295 | 0.577 | n.s. |
| Crossover (without 1) - Small (with 1) | 22.17 | 8.96 | 2.47 | 0.013 | 0.077 | n.s. |
| Crossover (without 1) - Small (without 1) | 21.47 | 9.17 | 2.34 | 0.019 | 0.092 | n.s. |
| Small (with 1) - Small (without 1) | -0.69 | 9.21 | -0.08 | 0.940 | 0.940 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.58, *p* = 0.060, η²_G = 0.050
- Greenhouse-Geisser corrected: *p* = 0.080 (ε = 0.742)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | -1.73 | 23 | = 0.194 | -0.30 [-0.79, 0.08] | small | n.s. |
| Crossover (with 1) vs Small (with 1) | 0.95 | 23 | = 0.452 | 0.27 [-0.23, 0.62] | small | n.s. |
| Crossover (with 1) vs Small (without 1) | 0.90 | 23 | = 0.452 | 0.23 [-0.24, 0.61] | small | n.s. |
| Crossover (without 1) vs Small (with 1) | 2.50 | 23 | = 0.060 | 0.58 [0.06, 0.96] | medium | n.s. |
| Crossover (without 1) vs Small (without 1) | 2.53 | 23 | = 0.060 | 0.52 [0.07, 0.97] | medium | n.s. |
| Small (with 1) vs Small (without 1) | -0.08 | 23 | = 0.934 | -0.02 [-0.44, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 406.80, BIC = 424.75
- **Crossover (without 1) vs Crossover (with 1)**: *β* = -0.00, *SE* = 0.369, *z* = -0.008, *p* = 0.993
- **Small (with 1) vs Crossover (with 1)**: *β* = 0.34, *SE* = 0.368, *z* = 0.936, *p* = 0.350
- **Small (without 1) vs Crossover (with 1)**: *β* = 1.65, *SE* = 0.390, *z* = 4.217, *p* < .001
- **SNR**: *β* = 0.10, *SE* = 0.046, *z* = 2.181, *p* = 0.029

_Reference condition: **Crossover (with 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Crossover (with 1) - Crossover (without 1) | 0.00 | 0.37 | 0.01 | 0.993 | 0.993 | n.s. |
| Crossover (with 1) - Small (with 1) | -0.34 | 0.37 | -0.94 | 0.350 | 0.718 | n.s. |
| Crossover (with 1) - Small (without 1) | -1.65 | 0.39 | -4.22 | < .001 | < .001 | *** |
| Crossover (without 1) - Small (with 1) | -0.35 | 0.37 | -0.95 | 0.344 | 0.718 | n.s. |
| Crossover (without 1) - Small (without 1) | -1.65 | 0.38 | -4.34 | < .001 | < .001 | *** |
| Small (with 1) - Small (without 1) | -1.30 | 0.38 | -3.40 | < .001 | 0.003 | ** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 6.13, *p* < .001, η²_G = 0.028
- Greenhouse-Geisser corrected: *p* = 0.008 (ε = 0.528)
- **Interpretation:** The main effect of condition was **highly significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Crossover (with 1) vs Crossover (without 1) | 0.99 | 23 | = 0.382 | 0.03 [-0.22, 0.63] | negligible | n.s. |
| Crossover (with 1) vs Small (with 1) | -0.89 | 23 | = 0.382 | -0.09 [-0.61, 0.24] | negligible | n.s. |
| Crossover (with 1) vs Small (without 1) | -2.79 | 23 | = 0.021 | -0.37 [-1.02, -0.11] | small | * |
| Crossover (without 1) vs Small (with 1) | -1.08 | 23 | = 0.382 | -0.11 [-0.65, 0.21] | negligible | n.s. |
| Crossover (without 1) vs Small (without 1) | -2.87 | 23 | = 0.021 | -0.40 [-1.04, -0.13] | small | * |
| Small (with 1) vs Small (without 1) | -2.81 | 23 | = 0.021 | -0.28 [-1.03, -0.12] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.038). Post-hoc tests revealed:
  - Crossover (with 1) showed smaller amplitude than Small (with 1) (*d* = -0.59)
  - Crossover (without 1) showed smaller amplitude than Small (with 1) (*d* = -0.62)
  - Small (with 1) showed greater amplitude than Small (without 1) (*d* = 0.51)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.060)
**P3b amplitude:** Significant main effect of condition (*p* < .001). Post-hoc tests revealed:
  - Crossover (with 1) showed smaller amplitude than Small (without 1) (*d* = -0.37)
  - Crossover (without 1) showed smaller amplitude than Small (without 1) (*d* = -0.40)
  - Small (with 1) showed smaller amplitude than Small (without 1) (*d* = -0.28)

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
