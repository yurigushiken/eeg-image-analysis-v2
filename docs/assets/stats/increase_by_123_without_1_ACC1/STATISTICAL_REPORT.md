# Statistical Analysis Report: tables

**Generated:** 2025-11-03 02:42:15

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
| Increase by 1 (no 1) | 7 | 98.86 ms | 12.38 | 4.68 | [88.00, 112.00] |
| Increase by 2 (no 1) | 8 | 103.00 ms | 12.42 | 4.39 | [88.00, 112.00] |
| Increase by 3 (no 1) | 11 | 101.09 ms | 12.53 | 3.78 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 7 | 1.69 µV | 0.74 | 0.28 | [0.92, 2.78] |
| Increase by 2 (no 1) | 8 | 1.53 µV | 1.08 | 0.38 | [0.45, 3.54] |
| Increase by 3 (no 1) | 11 | 1.80 µV | 1.25 | 0.38 | [0.36, 4.25] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 22 | 164.36 ms | 17.32 | 3.69 | [136.00, 200.00] |
| Increase by 2 (no 1) | 24 | 169.00 ms | 18.43 | 3.76 | [136.00, 200.00] |
| Increase by 3 (no 1) | 23 | 167.48 ms | 20.48 | 4.27 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 22 | -5.46 µV | 2.04 | 0.44 | [-9.45, -1.12] |
| Increase by 2 (no 1) | 24 | -5.46 µV | 2.63 | 0.54 | [-10.99, -1.19] |
| Increase by 3 (no 1) | 23 | -6.42 µV | 2.52 | 0.53 | [-13.29, -2.62] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 100.50 ms | 8.37 | 2.09 | [84.00, 108.00] |
| Increase by 2 (no 1) | 15 | 100.53 ms | 9.18 | 2.37 | [84.00, 108.00] |
| Increase by 3 (no 1) | 13 | 96.62 ms | 9.64 | 2.67 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 16 | 2.20 µV | 1.55 | 0.39 | [0.43, 5.16] |
| Increase by 2 (no 1) | 15 | 1.97 µV | 1.26 | 0.32 | [0.20, 4.87] |
| Increase by 3 (no 1) | 13 | 2.95 µV | 2.36 | 0.66 | [0.38, 8.91] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 18 | 491.78 ms | 36.03 | 8.49 | [416.00, 532.00] |
| Increase by 2 (no 1) | 18 | 485.78 ms | 35.12 | 8.28 | [416.00, 532.00] |
| Increase by 3 (no 1) | 22 | 467.82 ms | 38.83 | 8.28 | [416.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 18 | 4.77 µV | 2.93 | 0.69 | [0.74, 9.74] |
| Increase by 2 (no 1) | 18 | 5.50 µV | 2.71 | 0.64 | [0.78, 9.72] |
| Increase by 3 (no 1) | 22 | 4.43 µV | 2.36 | 0.50 | [0.84, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 203.15, BIC = 210.70
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -1.47, *SE* = 3.494, *z* = -0.421, *p* = 0.674
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 1.39, *SE* = 2.940, *z* = 0.473, *p* = 0.636
- **SNR**: *β* = -1.30, *SE* = 2.967, *z* = -0.438, *p* = 0.661

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.47 | 3.49 | 0.42 | 0.674 | 0.867 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -1.39 | 2.94 | -0.47 | 0.636 | 0.867 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -2.86 | 3.17 | -0.90 | 0.366 | 0.745 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 80.65, BIC = 88.20
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.01, *SE* = 0.418, *z* = 0.015, *p* = 0.988
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.39, *SE* = 0.382, *z* = 1.029, *p* = 0.303
- **SNR**: *β* = 0.62, *SE* = 0.328, *z* = 1.889, *p* = 0.059

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.01 | 0.42 | -0.01 | 0.988 | 0.988 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.39 | 0.38 | -1.03 | 0.303 | 0.662 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.39 | 0.38 | -1.02 | 0.307 | 0.662 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.44 | 1 | = 0.426 | -1.29 [-5.13, 2.12] | large | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.30 | 1 | = 0.426 | -1.63 [-1.73, 0.87] | large | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -1.26 | 1 | = 0.426 | -1.30 [-3.04, 0.93] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 571.12, BIC = 584.52
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 2.62, *SE* = 2.852, *z* = 0.920, *p* = 0.358
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 1.79, *SE* = 2.854, *z* = 0.628, *p* = 0.530
- **SNR**: *β* = -0.28, *SE* = 0.326, *z* = -0.873, *p* = 0.382

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -2.62 | 2.85 | -0.92 | 0.358 | 0.735 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -1.79 | 2.85 | -0.63 | 0.530 | 0.779 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.83 | 2.81 | 0.30 | 0.768 | 0.779 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.33, *p* = 0.719, η²_G = 0.003
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.77 | 21 | = 0.705 | -0.14 [-0.61, 0.28] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.38 | 21 | = 0.705 | -0.07 [-0.53, 0.36] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.49 | 21 | = 0.705 | 0.06 [-0.40, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 287.22, BIC = 300.62
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.15, *SE* = 0.388, *z* = -0.378, *p* = 0.706
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -1.14, *SE* = 0.389, *z* = -2.938, *p* = 0.003
- **SNR**: *β* = -0.13, *SE* = 0.045, *z* = -2.841, *p* = 0.004

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.15 | 0.39 | 0.38 | 0.706 | 0.706 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.14 | 0.39 | 2.94 | 0.003 | 0.010 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 1.00 | 0.38 | 2.61 | 0.009 | 0.018 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.06, *p* = 0.024, η²_G = 0.043
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.62 | 21 | = 0.542 | 0.11 [-0.31, 0.58] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.74 | 21 | = 0.036 | 0.51 [0.11, 1.06] | medium | * |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.06 | 21 | = 0.077 | 0.35 [0.01, 0.92] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 313.98, BIC = 324.68
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -1.44, *SE* = 2.088, *z* = -0.689, *p* = 0.491
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -4.02, *SE* = 2.116, *z* = -1.901, *p* = 0.057
- **SNR**: *β* = 0.86, *SE* = 0.839, *z* = 1.023, *p* = 0.306

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.44 | 2.09 | 0.69 | 0.491 | 0.491 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 4.02 | 2.12 | 1.90 | 0.057 | 0.162 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 2.58 | 2.15 | 1.20 | 0.228 | 0.404 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.91, *p* = 0.198, η²_G = 0.173
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.89 | 5 | = 0.415 | -0.51 [-0.47, 0.98] | medium | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.58 | 5 | = 0.322 | 0.58 [-0.19, 1.50] | medium | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.42 | 5 | = 0.322 | 0.90 [-0.42, 1.17] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 148.54, BIC = 159.25
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.17, *SE* = 0.389, *z* = 0.433, *p* = 0.665
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.95, *SE* = 0.399, *z* = 2.374, *p* = 0.018
- **SNR**: *β* = 0.79, *SE* = 0.124, *z* = 6.353, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.17 | 0.39 | -0.43 | 0.665 | 0.665 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.95 | 0.40 | -2.37 | 0.018 | 0.052 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.78 | 0.40 | -1.94 | 0.053 | 0.103 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.61, *p* = 0.561, η²_G = 0.036
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.05 | 5 | = 0.959 | 0.02 [-0.57, 0.86] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.04 | 5 | = 0.667 | -0.33 [-1.59, 0.14] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.83 | 5 | = 0.667 | -0.36 [-1.12, 0.46] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 589.82, BIC = 602.18
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -6.15, *SE* = 11.049, *z* = -0.556, *p* = 0.578
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -23.98, *SE* = 10.368, *z* = -2.313, *p* = 0.021
- **SNR**: *β* = 0.35, *SE* = 1.310, *z* = 0.265, *p* = 0.791

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 6.15 | 11.05 | 0.56 | 0.578 | 0.578 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 23.98 | 10.37 | 2.31 | 0.021 | 0.061 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 17.83 | 10.92 | 1.63 | 0.102 | 0.194 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.29, *p* = 0.118, η²_G = 0.069
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.23 | 16 | = 0.823 | 0.07 [-0.46, 0.57] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.98 | 16 | = 0.191 | 0.58 [0.02, 1.08] | medium | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.61 | 16 | = 0.191 | 0.52 [-0.10, 0.93] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 227.06, BIC = 239.42
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.19, *SE* = 0.363, *z* = 0.525, *p* = 0.600
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.07, *SE* = 0.339, *z* = 0.191, *p* = 0.848
- **SNR**: *β* = 0.25, *SE* = 0.058, *z* = 4.226, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.19 | 0.36 | -0.52 | 0.600 | 0.936 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.06 | 0.34 | -0.19 | 0.848 | 0.936 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.13 | 0.36 | 0.35 | 0.726 | 0.936 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.34, *p* = 0.277, η²_G = 0.011
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.64 | 16 | = 0.359 | -0.22 [-0.93, 0.14] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.32 | 16 | = 0.754 | -0.04 [-0.55, 0.45] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.06 | 16 | = 0.454 | 0.21 [-0.22, 0.79] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.024). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.51)

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
