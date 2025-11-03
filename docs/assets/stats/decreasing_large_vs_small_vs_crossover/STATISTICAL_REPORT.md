# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:33:57

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
| Decreasing Crossover | 7 | 106.29 ms | 14.02 | 5.30 | [92.00, 120.00] |
| Decreasing Large | 10 | 111.60 ms | 13.53 | 4.28 | [92.00, 120.00] |
| Decreasing Small | 9 | 111.56 ms | 10.85 | 3.62 | [92.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 7 | 1.71 µV | 0.76 | 0.29 | [0.68, 3.03] |
| Decreasing Large | 10 | 2.31 µV | 1.19 | 0.38 | [0.49, 4.52] |
| Decreasing Small | 9 | 1.42 µV | 0.75 | 0.25 | [0.63, 2.68] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | 175.00 ms | 14.41 | 2.94 | [148.00, 208.00] |
| Decreasing Large | 24 | 176.00 ms | 17.97 | 3.67 | [148.00, 208.00] |
| Decreasing Small | 21 | 179.81 ms | 11.90 | 2.60 | [156.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 24 | -5.28 µV | 1.87 | 0.38 | [-8.89, -1.81] |
| Decreasing Large | 24 | -5.42 µV | 2.11 | 0.43 | [-10.35, -1.44] |
| Decreasing Small | 21 | -4.24 µV | 2.44 | 0.53 | [-9.67, -0.79] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 16 | 116.00 ms | 7.87 | 1.97 | [104.00, 124.00] |
| Decreasing Large | 13 | 113.23 ms | 8.70 | 2.41 | [100.00, 124.00] |
| Decreasing Small | 19 | 117.05 ms | 7.52 | 1.73 | [104.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 16 | 2.39 µV | 1.47 | 0.37 | [0.92, 5.79] |
| Decreasing Large | 13 | 2.96 µV | 2.17 | 0.60 | [0.68, 7.08] |
| Decreasing Small | 19 | 2.64 µV | 1.75 | 0.40 | [0.60, 7.19] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 20 | 479.60 ms | 27.77 | 6.21 | [432.00, 540.00] |
| Decreasing Large | 18 | 493.56 ms | 33.83 | 7.97 | [444.00, 540.00] |
| Decreasing Small | 20 | 484.80 ms | 23.38 | 5.23 | [432.00, 516.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Decreasing Crossover | 20 | 4.70 µV | 2.73 | 0.61 | [1.10, 10.69] |
| Decreasing Large | 18 | 4.18 µV | 2.48 | 0.58 | [0.95, 8.30] |
| Decreasing Small | 20 | 5.07 µV | 2.68 | 0.60 | [1.41, 10.71] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 207.48, BIC = 215.03
- **Decreasing Large vs Decreasing Crossover**: *β* = 1.05, *SE* = 4.643, *z* = 0.225, *p* = 0.822
- **Decreasing Small vs Decreasing Crossover**: *β* = 1.25, *SE* = 4.492, *z* = 0.277, *p* = 0.781
- **SNR**: *β* = -1.86, *SE* = 1.785, *z* = -1.040, *p* = 0.298

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -1.05 | 4.64 | -0.23 | 0.822 | 0.990 | n.s. |
| Decreasing Crossover - Decreasing Small | -1.25 | 4.49 | -0.28 | 0.781 | 0.990 | n.s. |
| Decreasing Large - Decreasing Small | -0.20 | 3.78 | -0.05 | 0.958 | 0.990 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 69.09, BIC = 76.64
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.77, *SE* = 0.328, *z* = 2.348, *p* = 0.019
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.07, *SE* = 0.325, *z* = 0.230, *p* = 0.818
- **SNR**: *β* = 0.31, *SE* = 0.125, *z* = 2.498, *p* = 0.012

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.77 | 0.33 | -2.35 | 0.019 | 0.037 | * |
| Decreasing Crossover - Decreasing Small | -0.07 | 0.33 | -0.23 | 0.818 | 0.818 | n.s. |
| Decreasing Large - Decreasing Small | 0.69 | 0.28 | 2.50 | 0.012 | 0.036 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -0.85 | 1 | = 0.550 | -0.34 [-4.04, 2.04] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | 0.93 | 1 | = 0.550 | 0.29 [-0.57, 2.37] | small | n.s. |
| Decreasing Large vs Decreasing Small | 0.88 | 1 | = 0.550 | 0.55 [-0.63, 1.58] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 544.76, BIC = 558.17
- **Decreasing Large vs Decreasing Crossover**: *β* = 1.27, *SE* = 2.561, *z* = 0.494, *p* = 0.621
- **Decreasing Small vs Decreasing Crossover**: *β* = 5.97, *SE* = 2.919, *z* = 2.046, *p* = 0.041
- **SNR**: *β* = 0.06, *SE* = 0.227, *z* = 0.247, *p* = 0.805

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -1.27 | 2.56 | -0.49 | 0.621 | 0.621 | n.s. |
| Decreasing Crossover - Decreasing Small | -5.97 | 2.92 | -2.05 | 0.041 | 0.117 | n.s. |
| Decreasing Large - Decreasing Small | -4.71 | 2.50 | -1.89 | 0.059 | 0.117 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.71, *p* = 0.079, η²_G = 0.027
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -0.34 | 20 | = 0.740 | -0.06 [-0.51, 0.34] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -2.86 | 20 | = 0.029 | -0.43 [-1.12, -0.13] | small | * |
| Decreasing Large vs Decreasing Small | -1.61 | 20 | = 0.184 | -0.31 [-0.82, 0.12] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 275.79, BIC = 289.20
- **Decreasing Large vs Decreasing Crossover**: *β* = -0.54, *SE* = 0.384, *z* = -1.408, *p* = 0.159
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.62, *SE* = 0.438, *z* = 1.408, *p* = 0.159
- **SNR**: *β* = -0.08, *SE* = 0.034, *z* = -2.497, *p* = 0.013

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 0.54 | 0.38 | 1.41 | 0.159 | 0.293 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.62 | 0.44 | -1.41 | 0.159 | 0.293 | n.s. |
| Decreasing Large - Decreasing Small | -1.16 | 0.37 | -3.09 | 0.002 | 0.006 | ** |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 7.62, *p* = 0.002, η²_G = 0.087
- Greenhouse-Geisser corrected: *p* = 0.005 (ε = 0.696)
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 0.36 | 20 | = 0.721 | 0.06 [-0.33, 0.52] | negligible | n.s. |
| Decreasing Crossover vs Decreasing Small | -3.89 | 20 | = 0.003 | -0.59 [-1.38, -0.32] | medium | ** |
| Decreasing Large vs Decreasing Small | -2.73 | 20 | = 0.019 | -0.62 [-1.09, -0.10] | medium | * |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 339.47, BIC = 350.69
- **Decreasing Large vs Decreasing Crossover**: *β* = -3.21, *SE* = 2.284, *z* = -1.406, *p* = 0.160
- **Decreasing Small vs Decreasing Crossover**: *β* = 2.21, *SE* = 2.216, *z* = 0.996, *p* = 0.319
- **SNR**: *β* = -0.26, *SE* = 0.330, *z* = -0.774, *p* = 0.439

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | 3.21 | 2.28 | 1.41 | 0.160 | 0.294 | n.s. |
| Decreasing Crossover - Decreasing Small | -2.21 | 2.22 | -1.00 | 0.319 | 0.319 | n.s. |
| Decreasing Large - Decreasing Small | -5.42 | 2.33 | -2.32 | 0.020 | 0.059 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.10, *p* = 0.031, η²_G = 0.123
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.82 | 11 | = 0.145 | 0.49 [-0.15, 1.20] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.47 | 11 | = 0.171 | -0.37 [-1.22, 0.03] | small | n.s. |
| Decreasing Large vs Decreasing Small | -2.29 | 11 | = 0.128 | -0.85 [-1.38, -0.03] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 160.21, BIC = 171.44
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.56, *SE* = 0.315, *z* = 1.777, *p* = 0.076
- **Decreasing Small vs Decreasing Crossover**: *β* = 0.58, *SE* = 0.292, *z* = 1.972, *p* = 0.049
- **SNR**: *β* = 0.19, *SE* = 0.058, *z* = 3.303, *p* = 0.001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.56 | 0.32 | -1.78 | 0.076 | 0.146 | n.s. |
| Decreasing Crossover - Decreasing Small | -0.58 | 0.29 | -1.97 | 0.049 | 0.139 | n.s. |
| Decreasing Large - Decreasing Small | -0.02 | 0.30 | -0.05 | 0.956 | 0.956 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.10, *p* = 0.349, η²_G = 0.016
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.77 | 11 | = 0.312 | -0.23 [-1.19, 0.16] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.28 | 11 | = 0.338 | -0.30 [-0.99, 0.21] | small | n.s. |
| Decreasing Large vs Decreasing Small | -0.21 | 11 | = 0.838 | -0.05 [-0.69, 0.52] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 552.91, BIC = 565.28
- **Decreasing Large vs Decreasing Crossover**: *β* = 9.48, *SE* = 7.729, *z* = 1.226, *p* = 0.220
- **Decreasing Small vs Decreasing Crossover**: *β* = 2.16, *SE* = 7.102, *z* = 0.304, *p* = 0.761
- **SNR**: *β* = -0.66, *SE* = 0.517, *z* = -1.280, *p* = 0.200

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -9.48 | 7.73 | -1.23 | 0.220 | 0.526 | n.s. |
| Decreasing Crossover - Decreasing Small | -2.16 | 7.10 | -0.30 | 0.761 | 0.761 | n.s. |
| Decreasing Large - Decreasing Small | 7.32 | 6.98 | 1.05 | 0.294 | 0.526 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.80, *p* = 0.181, η²_G = 0.042
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | -1.64 | 17 | = 0.274 | -0.45 [-0.90, 0.13] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -0.67 | 17 | = 0.514 | -0.19 [-0.65, 0.32] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | 1.39 | 17 | = 0.274 | 0.32 [-0.18, 0.84] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 237.23, BIC = 249.59
- **Decreasing Large vs Decreasing Crossover**: *β* = 0.24, *SE* = 0.436, *z* = 0.555, *p* = 0.579
- **Decreasing Small vs Decreasing Crossover**: *β* = 1.01, *SE* = 0.397, *z* = 2.547, *p* = 0.011
- **SNR**: *β* = 0.15, *SE* = 0.030, *z* = 4.887, *p* < .001

_Reference condition: **Decreasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Decreasing Crossover - Decreasing Large | -0.24 | 0.44 | -0.56 | 0.579 | 0.579 | n.s. |
| Decreasing Crossover - Decreasing Small | -1.01 | 0.40 | -2.55 | 0.011 | 0.032 | * |
| Decreasing Large - Decreasing Small | -0.77 | 0.39 | -1.98 | 0.047 | 0.092 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.22, *p* = 0.052, η²_G = 0.038
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Decreasing Crossover vs Decreasing Large | 1.44 | 17 | = 0.251 | 0.32 [-0.17, 0.85] | small | n.s. |
| Decreasing Crossover vs Decreasing Small | -1.00 | 17 | = 0.331 | -0.13 [-0.69, 0.28] | negligible | n.s. |
| Decreasing Large vs Decreasing Small | -2.46 | 17 | = 0.075 | -0.47 [-1.12, -0.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Marginal trend toward condition differences (*p* = 0.079)
**N1 amplitude:** Significant main effect of condition (*p* = 0.002). Post-hoc tests revealed:
  - Decreasing Crossover showed smaller amplitude than Decreasing Small (*d* = -0.59)
  - Decreasing Large showed smaller amplitude than Decreasing Small (*d* = -0.62)
**P1 latency:** Significant main effect of condition (*p* = 0.031) (no significant pairwise comparisons)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.052)

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
