# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:26:31

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
| Increasing Crossover | 24 | 98.67 ms | 8.88 | 1.81 | [84.00, 108.00] |
| Increasing Large | 24 | 97.33 ms | 9.11 | 1.86 | [84.00, 108.00] |
| Increasing Small | 24 | 95.00 ms | 10.16 | 2.07 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | -1.09 µV | 1.00 | 0.20 | [-4.26, 0.46] |
| Increasing Large | 24 | -1.23 µV | 1.34 | 0.27 | [-3.44, 1.53] |
| Increasing Small | 24 | -0.47 µV | 1.37 | 0.28 | [-3.30, 2.56] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 170.83 ms | 20.45 | 4.17 | [136.00, 208.00] |
| Increasing Large | 24 | 168.67 ms | 19.23 | 3.92 | [136.00, 200.00] |
| Increasing Small | 24 | 169.67 ms | 20.73 | 4.23 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | -5.48 µV | 2.23 | 0.46 | [-10.48, -0.86] |
| Increasing Large | 24 | -5.43 µV | 2.57 | 0.53 | [-10.36, 0.02] |
| Increasing Small | 24 | -5.28 µV | 2.12 | 0.43 | [-10.78, -1.55] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 97.33 ms | 11.11 | 2.27 | [80.00, 108.00] |
| Increasing Large | 24 | 95.67 ms | 10.74 | 2.19 | [80.00, 108.00] |
| Increasing Small | 24 | 94.67 ms | 12.69 | 2.59 | [80.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 1.35 µV | 1.39 | 0.28 | [-0.57, 5.41] |
| Increasing Large | 24 | 1.27 µV | 1.73 | 0.35 | [-2.05, 4.42] |
| Increasing Small | 24 | 0.76 µV | 1.46 | 0.30 | [-1.26, 3.66] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 480.33 ms | 32.43 | 6.62 | [420.00, 532.00] |
| Increasing Large | 24 | 488.67 ms | 36.04 | 7.36 | [420.00, 532.00] |
| Increasing Small | 24 | 472.83 ms | 29.58 | 6.04 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increasing Crossover | 24 | 3.32 µV | 3.00 | 0.61 | [-1.70, 8.36] |
| Increasing Large | 24 | 2.67 µV | 3.26 | 0.66 | [-2.73, 10.38] |
| Increasing Small | 24 | 3.61 µV | 3.60 | 0.73 | [-2.27, 12.65] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 526.12, BIC = 539.78
- **Increasing Large vs Increasing Crossover**: *β* = -1.44, *SE* = 2.116, *z* = -0.682, *p* = 0.495
- **Increasing Small vs Increasing Crossover**: *β* = -3.83, *SE* = 2.119, *z* = -1.807, *p* = 0.071
- **SNR**: *β* = 0.81, *SE* = 0.689, *z* = 1.173, *p* = 0.241

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.44 | 2.12 | 0.68 | 0.495 | 0.495 | n.s. |
| Increasing Crossover - Increasing Small | 3.83 | 2.12 | 1.81 | 0.071 | 0.198 | n.s. |
| Increasing Large - Increasing Small | 2.39 | 2.11 | 1.13 | 0.259 | 0.451 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.46, *p* = 0.242, η²_G = 0.026
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.62 | 23 | = 0.541 | 0.15 [-0.30, 0.55] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 1.71 | 23 | = 0.300 | 0.38 [-0.09, 0.78] | small | n.s. |
| Increasing Large vs Increasing Small | 1.05 | 23 | = 0.456 | 0.24 [-0.21, 0.64] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 234.30, BIC = 247.96
- **Increasing Large vs Increasing Crossover**: *β* = -0.11, *SE* = 0.286, *z* = -0.393, *p* = 0.694
- **Increasing Small vs Increasing Crossover**: *β* = 0.66, *SE* = 0.286, *z* = 2.292, *p* = 0.022
- **SNR**: *β* = -0.17, *SE* = 0.093, *z* = -1.849, *p* = 0.064

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.11 | 0.29 | 0.39 | 0.694 | 0.694 | n.s. |
| Increasing Crossover - Increasing Small | -0.66 | 0.29 | -2.29 | 0.022 | 0.043 | * |
| Increasing Large - Increasing Small | -0.77 | 0.29 | -2.69 | 0.007 | 0.021 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.78, *p* = 0.030, η²_G = 0.068
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.53 | 23 | = 0.603 | 0.11 [-0.32, 0.53] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -2.42 | 23 | = 0.066 | -0.52 [-0.94, -0.05] | medium | n.s. |
| Increasing Large vs Increasing Small | -2.13 | 23 | = 0.066 | -0.56 [-0.88, 0.01] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 622.17, BIC = 635.83
- **Increasing Large vs Increasing Crossover**: *β* = -3.09, *SE* = 3.970, *z* = -0.779, *p* = 0.436
- **Increasing Small vs Increasing Crossover**: *β* = -1.97, *SE* = 3.908, *z* = -0.503, *p* = 0.615
- **SNR**: *β* = -0.31, *SE* = 0.468, *z* = -0.670, *p* = 0.503

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 3.09 | 3.97 | 0.78 | 0.436 | 0.821 | n.s. |
| Increasing Crossover - Increasing Small | 1.97 | 3.91 | 0.50 | 0.615 | 0.852 | n.s. |
| Increasing Large - Increasing Small | -1.13 | 3.73 | -0.30 | 0.762 | 0.852 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.17, *p* = 0.848, η²_G = 0.002
- Greenhouse-Geisser corrected: *p* = 0.763 (ε = 0.679)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.01 | 23 | = 0.814 | 0.11 [-0.22, 0.63] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 0.26 | 23 | = 0.814 | 0.06 [-0.37, 0.48] | negligible | n.s. |
| Increasing Large vs Increasing Small | -0.24 | 23 | = 0.814 | -0.05 [-0.47, 0.37] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 265.00, BIC = 278.66
- **Increasing Large vs Increasing Crossover**: *β* = -0.42, *SE* = 0.298, *z* = -1.403, *p* = 0.160
- **Increasing Small vs Increasing Crossover**: *β* = -0.21, *SE* = 0.293, *z* = -0.728, *p* = 0.466
- **SNR**: *β* = -0.16, *SE* = 0.039, *z* = -4.174, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.42 | 0.30 | 1.40 | 0.160 | 0.408 | n.s. |
| Increasing Crossover - Increasing Small | 0.21 | 0.29 | 0.73 | 0.466 | 0.705 | n.s. |
| Increasing Large - Increasing Small | -0.21 | 0.28 | -0.74 | 0.457 | 0.705 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.22, *p* = 0.803, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -0.21 | 23 | = 0.835 | -0.02 [-0.47, 0.38] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | -0.65 | 23 | = 0.835 | -0.09 [-0.56, 0.29] | negligible | n.s. |
| Increasing Large vs Increasing Small | -0.41 | 23 | = 0.835 | -0.06 [-0.51, 0.34] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 555.77, BIC = 569.43
- **Increasing Large vs Increasing Crossover**: *β* = -1.39, *SE* = 2.588, *z* = -0.537, *p* = 0.591
- **Increasing Small vs Increasing Crossover**: *β* = -2.63, *SE* = 2.557, *z* = -1.027, *p* = 0.305
- **SNR**: *β* = 0.50, *SE* = 0.722, *z* = 0.693, *p* = 0.489

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 1.39 | 2.59 | 0.54 | 0.591 | 0.833 | n.s. |
| Increasing Crossover - Increasing Small | 2.63 | 2.56 | 1.03 | 0.305 | 0.664 | n.s. |
| Increasing Large - Increasing Small | 1.24 | 2.58 | 0.48 | 0.632 | 0.833 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.52, *p* = 0.595, η²_G = 0.009
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.68 | 23 | = 0.753 | 0.15 [-0.29, 0.56] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 1.20 | 23 | = 0.723 | 0.22 [-0.18, 0.67] | small | n.s. |
| Increasing Large vs Increasing Small | 0.32 | 23 | = 0.753 | 0.09 [-0.36, 0.49] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 262.00, BIC = 275.66
- **Increasing Large vs Increasing Crossover**: *β* = 0.03, *SE* = 0.343, *z* = 0.082, *p* = 0.934
- **Increasing Small vs Increasing Crossover**: *β* = -0.57, *SE* = 0.339, *z* = -1.691, *p* = 0.091
- **SNR**: *β* = 0.19, *SE* = 0.095, *z* = 2.027, *p* = 0.043

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -0.03 | 0.34 | -0.08 | 0.934 | 0.934 | n.s. |
| Increasing Crossover - Increasing Small | 0.57 | 0.34 | 1.69 | 0.091 | 0.218 | n.s. |
| Increasing Large - Increasing Small | 0.60 | 0.34 | 1.76 | 0.079 | 0.218 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.65, *p* = 0.203, η²_G = 0.029
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 0.24 | 23 | = 0.813 | 0.05 [-0.37, 0.47] | negligible | n.s. |
| Increasing Crossover vs Increasing Small | 2.00 | 23 | = 0.172 | 0.41 [-0.03, 0.85] | small | n.s. |
| Increasing Large vs Increasing Small | 1.22 | 23 | = 0.354 | 0.32 [-0.18, 0.68] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 709.69, BIC = 723.35
- **Increasing Large vs Increasing Crossover**: *β* = 4.75, *SE* = 8.305, *z* = 0.572, *p* = 0.568
- **Increasing Small vs Increasing Crossover**: *β* = -9.15, *SE* = 8.035, *z* = -1.139, *p* = 0.255
- **SNR**: *β* = -1.35, *SE* = 0.893, *z* = -1.516, *p* = 0.129

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | -4.75 | 8.30 | -0.57 | 0.568 | 0.568 | n.s. |
| Increasing Crossover - Increasing Small | 9.15 | 8.03 | 1.14 | 0.255 | 0.445 | n.s. |
| Increasing Large - Increasing Small | 13.90 | 8.06 | 1.72 | 0.085 | 0.233 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.168, η²_G = 0.039
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | -1.00 | 23 | = 0.326 | -0.24 [-0.63, 0.22] | small | n.s. |
| Increasing Crossover vs Increasing Small | 1.15 | 23 | = 0.326 | 0.24 [-0.19, 0.66] | small | n.s. |
| Increasing Large vs Increasing Small | 1.65 | 23 | = 0.326 | 0.48 [-0.10, 0.77] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 309.54, BIC = 323.20
- **Increasing Large vs Increasing Crossover**: *β* = -0.17, *SE* = 0.376, *z* = -0.444, *p* = 0.657
- **Increasing Small vs Increasing Crossover**: *β* = 0.51, *SE* = 0.355, *z* = 1.445, *p* = 0.149
- **SNR**: *β* = 0.18, *SE* = 0.052, *z* = 3.510, *p* < .001

_Reference condition: **Increasing Crossover** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increasing Crossover - Increasing Large | 0.17 | 0.38 | 0.44 | 0.657 | 0.657 | n.s. |
| Increasing Crossover - Increasing Small | -0.51 | 0.36 | -1.44 | 0.149 | 0.275 | n.s. |
| Increasing Large - Increasing Small | -0.68 | 0.36 | -1.90 | 0.057 | 0.162 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.15, *p* = 0.052, η²_G = 0.015
- Greenhouse-Geisser corrected: *p* = 0.071 (ε = 0.725)
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increasing Crossover vs Increasing Large | 1.99 | 23 | = 0.099 | 0.21 [-0.03, 0.84] | small | n.s. |
| Increasing Crossover vs Increasing Small | -0.94 | 23 | = 0.359 | -0.09 [-0.62, 0.23] | negligible | n.s. |
| Increasing Large vs Increasing Small | -1.93 | 23 | = 0.099 | -0.27 [-0.83, 0.04] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**Fz amplitude:** Significant main effect of condition (*p* = 0.030) (no significant pairwise comparisons)
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
