# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:55:05

---

## 1. Analysis Overview

**Total Measurements:** 288
**Number of Subjects:** 24
**Number of Conditions:** 3

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
| Small Ratio 0.33 (1:3) | 8 | 109.00 ms | 9.01 | 3.18 | [96.00, 120.00] |
| Small Ratio 0.5 (1:2) | 12 | 103.00 ms | 12.08 | 3.49 | [88.00, 120.00] |
| Small Ratio 0.67 (2:3) | 13 | 107.08 ms | 10.35 | 2.87 | [88.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small Ratio 0.33 (1:3) | 8 | -2.73 µV | 1.46 | 0.52 | [-4.26, -0.48] |
| Small Ratio 0.5 (1:2) | 12 | -2.18 µV | 1.41 | 0.41 | [-4.97, -0.59] |
| Small Ratio 0.67 (2:3) | 13 | -2.28 µV | 1.22 | 0.34 | [-4.98, -0.83] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small Ratio 0.33 (1:3) | 24 | 173.67 ms | 17.33 | 3.54 | [144.00, 212.00] |
| Small Ratio 0.5 (1:2) | 19 | 176.42 ms | 14.10 | 3.24 | [152.00, 208.00] |
| Small Ratio 0.67 (2:3) | 24 | 174.67 ms | 20.96 | 4.28 | [144.00, 212.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small Ratio 0.33 (1:3) | 24 | -4.78 µV | 2.15 | 0.44 | [-10.80, -1.76] |
| Small Ratio 0.5 (1:2) | 19 | -4.84 µV | 2.32 | 0.53 | [-10.24, -1.45] |
| Small Ratio 0.67 (2:3) | 24 | -4.98 µV | 2.04 | 0.42 | [-9.83, -2.06] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small Ratio 0.33 (1:3) | 13 | 116.31 ms | 7.39 | 2.05 | [100.00, 124.00] |
| Small Ratio 0.5 (1:2) | 14 | 113.71 ms | 10.95 | 2.93 | [96.00, 124.00] |
| Small Ratio 0.67 (2:3) | 10 | 114.00 ms | 8.49 | 2.68 | [104.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small Ratio 0.33 (1:3) | 13 | 2.90 µV | 1.66 | 0.46 | [0.82, 7.25] |
| Small Ratio 0.5 (1:2) | 14 | 3.06 µV | 1.71 | 0.46 | [0.72, 5.97] |
| Small Ratio 0.67 (2:3) | 10 | 2.54 µV | 1.41 | 0.44 | [1.30, 6.13] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small Ratio 0.33 (1:3) | 21 | 476.57 ms | 29.78 | 6.50 | [432.00, 532.00] |
| Small Ratio 0.5 (1:2) | 20 | 486.40 ms | 33.02 | 7.38 | [424.00, 532.00] |
| Small Ratio 0.67 (2:3) | 19 | 488.00 ms | 35.13 | 8.06 | [436.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small Ratio 0.33 (1:3) | 21 | 5.08 µV | 2.93 | 0.64 | [0.86, 10.71] |
| Small Ratio 0.5 (1:2) | 20 | 4.60 µV | 2.52 | 0.56 | [1.04, 8.69] |
| Small Ratio 0.67 (2:3) | 19 | 5.64 µV | 3.80 | 0.87 | [1.57, 16.31] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 259.01, BIC = 267.99
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = -6.21, *SE* = 5.331, *z* = -1.166, *p* = 0.244
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = -2.16, *SE* = 5.246, *z* = -0.412, *p* = 0.680
- **SNR**: *β* = -0.41, *SE* = 1.164, *z* = -0.348, *p* = 0.728

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | 6.21 | 5.33 | 1.17 | 0.244 | 0.567 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | 2.16 | 5.25 | 0.41 | 0.680 | 0.680 | n.s. |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | -4.05 | 4.09 | -0.99 | 0.322 | 0.567 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.15, *p* = 0.197, η²_G = 0.320
- Greenhouse-Geisser corrected: *p* = 0.238 (ε = 0.506)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | 1.41 | 3 | = 0.378 | 1.23 [-0.79, 1.87] | large | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | 2.18 | 3 | = 0.351 | 1.21 [-0.29, 2.28] | large | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | -0.68 | 3 | = 0.547 | -0.36 [-1.65, 0.59] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 98.52, BIC = 107.50
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = 0.40, *SE* = 0.404, *z* = 0.988, *p* = 0.323
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = 0.19, *SE* = 0.373, *z* = 0.518, *p* = 0.604
- **SNR**: *β* = -0.55, *SE* = 0.092, *z* = -5.898, *p* < .001

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | -0.40 | 0.40 | -0.99 | 0.323 | 0.690 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | -0.19 | 0.37 | -0.52 | 0.604 | 0.795 | n.s. |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | 0.21 | 0.34 | 0.60 | 0.547 | 0.795 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.50, *p* = 0.631, η²_G = 0.123
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | -0.88 | 3 | = 0.666 | -0.64 [-1.81, 0.82] | medium | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | -0.93 | 3 | = 0.666 | -0.87 [-1.63, 0.60] | large | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | -0.13 | 3 | = 0.903 | -0.10 [-0.99, 1.11] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 561.71, BIC = 574.94
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = 4.04, *SE* = 3.456, *z* = 1.169, *p* = 0.242
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = 1.62, *SE* = 3.164, *z* = 0.512, *p* = 0.609
- **SNR**: *β* = -1.11, *SE* = 0.687, *z* = -1.616, *p* = 0.106

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | -4.04 | 3.46 | -1.17 | 0.242 | 0.565 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | -1.62 | 3.16 | -0.51 | 0.609 | 0.743 | n.s. |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | 2.42 | 3.53 | 0.69 | 0.493 | 0.743 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.51, *p* = 0.096, η²_G = 0.032
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | -0.93 | 18 | = 0.364 | -0.19 [-0.70, 0.27] | negligible | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | 1.08 | 18 | = 0.364 | 0.24 [-0.47, 0.37] | small | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | 3.01 | 18 | = 0.023 | 0.44 [0.15, 1.23] | small | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 240.67, BIC = 253.90
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = -0.03, *SE* = 0.317, *z* = -0.082, *p* = 0.935
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = -0.00, *SE* = 0.289, *z* = -0.011, *p* = 0.991
- **SNR**: *β* = -0.35, *SE* = 0.069, *z* = -5.105, *p* < .001

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | 0.03 | 0.32 | 0.08 | 0.935 | 1.000 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | 0.00 | 0.29 | 0.01 | 0.991 | 1.000 | n.s. |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | -0.02 | 0.33 | -0.07 | 0.944 | 1.000 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.14, *p* = 0.331, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | -0.93 | 18 | = 0.547 | -0.13 [-0.70, 0.27] | negligible | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | 0.61 | 18 | = 0.547 | 0.12 [-0.31, 0.54] | negligible | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | 1.53 | 18 | = 0.428 | 0.25 [-0.15, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 270.57, BIC = 280.23
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = -2.94, *SE* = 2.494, *z* = -1.178, *p* = 0.239
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = -5.12, *SE* = 3.054, *z* = -1.675, *p* = 0.094
- **SNR**: *β* = -1.52, *SE* = 0.625, *z* = -2.430, *p* = 0.015

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | 2.94 | 2.49 | 1.18 | 0.239 | 0.420 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | 5.12 | 3.05 | 1.68 | 0.094 | 0.256 | n.s. |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | 2.18 | 2.81 | 0.78 | 0.438 | 0.438 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.15, *p* = 0.354, η²_G = 0.092
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | 1.10 | 5 | = 0.456 | 0.67 [-0.46, 0.99] | medium | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | 1.12 | 5 | = 0.456 | 0.61 [-0.65, 1.56] | medium | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | -0.81 | 5 | = 0.456 | -0.20 [-0.85, 0.69] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 121.59, BIC = 131.26
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = -0.15, *SE* = 0.364, *z* = -0.412, *p* = 0.680
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = -0.17, *SE* = 0.421, *z* = -0.406, *p* = 0.685
- **SNR**: *β* = 0.52, *SE* = 0.085, *z* = 6.186, *p* < .001

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | 0.15 | 0.36 | 0.41 | 0.680 | 0.967 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | 0.17 | 0.42 | 0.41 | 0.685 | 0.967 | n.s. |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | 0.02 | 0.40 | 0.05 | 0.958 | 0.967 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.66, *p* = 0.064, η²_G = 0.225
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | -0.97 | 5 | = 0.378 | -0.35 [-0.56, 0.88] | small | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | 1.51 | 5 | = 0.288 | 0.78 [-0.53, 1.76] | medium | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | 3.11 | 5 | = 0.079 | 1.52 [-0.25, 1.42] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 590.32, BIC = 602.88
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = 6.33, *SE* = 8.486, *z* = 0.746, *p* = 0.456
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = 9.60, *SE* = 8.349, *z* = 1.150, *p* = 0.250
- **SNR**: *β* = -1.83, *SE* = 1.140, *z* = -1.610, *p* = 0.107

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | -6.33 | 8.49 | -0.75 | 0.456 | 0.704 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | -9.60 | 8.35 | -1.15 | 0.250 | 0.578 | n.s. |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | -3.27 | 8.27 | -0.40 | 0.692 | 0.704 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.97, *p* = 0.155, η²_G = 0.055
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | -1.12 | 16 | = 0.416 | -0.37 [-0.84, 0.18] | small | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | -2.22 | 16 | = 0.124 | -0.57 [-0.93, 0.08] | medium | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | -0.74 | 16 | = 0.472 | -0.21 [-0.70, 0.34] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 253.44, BIC = 266.00
- **Small Ratio 0.5 (1:2) vs Small Ratio 0.33 (1:3)**: *β* = 0.47, *SE* = 0.466, *z* = 0.996, *p* = 0.319
- **Small Ratio 0.67 (2:3) vs Small Ratio 0.33 (1:3)**: *β* = 1.31, *SE* = 0.454, *z* = 2.890, *p* = 0.004
- **SNR**: *β* = 0.44, *SE* = 0.074, *z* = 5.981, *p* < .001

_Reference condition: **Small Ratio 0.33 (1:3)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Small Ratio 0.33 (1:3) - Small Ratio 0.5 (1:2) | -0.46 | 0.47 | -1.00 | 0.319 | 0.319 | n.s. |
| Small Ratio 0.33 (1:3) - Small Ratio 0.67 (2:3) | -1.31 | 0.45 | -2.89 | 0.004 | 0.012 | * |
| Small Ratio 0.5 (1:2) - Small Ratio 0.67 (2:3) | -0.85 | 0.44 | -1.92 | 0.055 | 0.106 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.54, *p* = 0.230, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small Ratio 0.33 (1:3) vs Small Ratio 0.5 (1:2) | 1.44 | 16 | = 0.253 | 0.27 [-0.22, 0.80] | small | n.s. |
| Small Ratio 0.33 (1:3) vs Small Ratio 0.67 (2:3) | -0.43 | 16 | = 0.672 | -0.08 [-0.59, 0.37] | negligible | n.s. |
| Small Ratio 0.5 (1:2) vs Small Ratio 0.67 (2:3) | -1.59 | 16 | = 0.253 | -0.31 [-0.92, 0.15] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Marginal trend toward condition differences (*p* = 0.096)
**P1 amplitude:** Marginal trend toward condition differences (*p* = 0.064)

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
