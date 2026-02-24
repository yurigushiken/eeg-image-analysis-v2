# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:23:23

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
| Increase by 1 (no 1) | 24 | 100.17 ms | 8.71 | 1.78 | [88.00, 112.00] |
| Increase by 2 (no 1) | 24 | 100.67 ms | 9.41 | 1.92 | [88.00, 112.00] |
| Increase by 3 (no 1) | 24 | 100.50 ms | 9.46 | 1.93 | [88.00, 112.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | -1.52 µV | 1.45 | 0.30 | [-3.96, 1.21] |
| Increase by 2 (no 1) | 24 | -1.45 µV | 1.26 | 0.26 | [-3.67, 0.21] |
| Increase by 3 (no 1) | 24 | -1.42 µV | 1.66 | 0.34 | [-5.70, 0.75] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 165.00 ms | 19.78 | 4.04 | [136.00, 208.00] |
| Increase by 2 (no 1) | 24 | 169.00 ms | 18.43 | 3.76 | [136.00, 200.00] |
| Increase by 3 (no 1) | 24 | 169.17 ms | 21.67 | 4.42 | [136.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | -5.20 µV | 2.20 | 0.45 | [-9.45, -0.73] |
| Increase by 2 (no 1) | 24 | -5.46 µV | 2.63 | 0.54 | [-10.99, -1.19] |
| Increase by 3 (no 1) | 24 | -6.34 µV | 2.50 | 0.51 | [-13.29, -2.62] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 100.00 ms | 8.98 | 1.83 | [84.00, 108.00] |
| Increase by 2 (no 1) | 24 | 97.67 ms | 10.14 | 2.07 | [84.00, 108.00] |
| Increase by 3 (no 1) | 24 | 97.33 ms | 10.12 | 2.07 | [84.00, 108.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 1.55 µV | 1.68 | 0.34 | [-1.16, 5.16] |
| Increase by 2 (no 1) | 24 | 1.47 µV | 1.52 | 0.31 | [-1.09, 4.87] |
| Increase by 3 (no 1) | 24 | 1.60 µV | 2.36 | 0.48 | [-1.57, 8.91] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 487.83 ms | 38.65 | 7.89 | [416.00, 532.00] |
| Increase by 2 (no 1) | 24 | 485.83 ms | 36.28 | 7.41 | [416.00, 532.00] |
| Increase by 3 (no 1) | 24 | 468.33 ms | 40.89 | 8.35 | [416.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Increase by 1 (no 1) | 24 | 3.26 µV | 3.79 | 0.77 | [-4.39, 9.74] |
| Increase by 2 (no 1) | 24 | 3.99 µV | 3.63 | 0.74 | [-3.39, 9.72] |
| Increase by 3 (no 1) | 24 | 4.16 µV | 2.44 | 0.50 | [0.81, 9.40] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 510.57, BIC = 524.23
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.66, *SE* = 1.744, *z* = 0.377, *p* = 0.706
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.71, *SE* = 1.758, *z* = 0.405, *p* = 0.686
- **SNR**: *β* = 0.83, *SE* = 0.525, *z* = 1.591, *p* = 0.112

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.66 | 1.74 | -0.38 | 0.706 | 0.969 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.71 | 1.76 | -0.40 | 0.686 | 0.969 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.05 | 1.75 | -0.03 | 0.975 | 0.975 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.961, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.25 | 23 | = 0.933 | -0.06 [-0.47, 0.37] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.24 | 23 | = 0.933 | -0.04 [-0.47, 0.37] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.09 | 23 | = 0.933 | 0.02 [-0.40, 0.44] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 227.23, BIC = 240.89
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.04, *SE* = 0.274, *z* = -0.127, *p* = 0.899
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -0.14, *SE* = 0.276, *z* = -0.504, *p* = 0.614
- **SNR**: *β* = -0.53, *SE* = 0.077, *z* = -6.811, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.03 | 0.27 | 0.13 | 0.899 | 0.942 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 0.14 | 0.28 | 0.50 | 0.614 | 0.942 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.10 | 0.27 | 0.38 | 0.704 | 0.942 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.04, *p* = 0.962, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -0.21 | 23 | = 0.929 | -0.05 [-0.46, 0.38] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.26 | 23 | = 0.929 | -0.06 [-0.48, 0.37] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.09 | 23 | = 0.929 | -0.02 [-0.44, 0.40] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 614.82, BIC = 628.48
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 4.13, *SE* = 3.411, *z* = 1.212, *p* = 0.225
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 4.08, *SE* = 3.408, *z* = 1.198, *p* = 0.231
- **SNR**: *β* = -0.33, *SE* = 0.395, *z* = -0.841, *p* = 0.400

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -4.13 | 3.41 | -1.21 | 0.225 | 0.535 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -4.08 | 3.41 | -1.20 | 0.231 | 0.535 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.05 | 3.42 | 0.02 | 0.988 | 0.988 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.92, *p* = 0.404, η²_G = 0.010
- Greenhouse-Geisser corrected: *p* = 0.377 (ε = 0.715)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -1.10 | 23 | = 0.502 | -0.21 [-0.65, 0.20] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.99 | 23 | = 0.502 | -0.20 [-0.63, 0.23] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.08 | 23 | = 0.941 | -0.01 [-0.44, 0.41] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 296.22, BIC = 309.88
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -0.22, *SE* = 0.364, *z* = -0.595, *p* = 0.552
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -1.18, *SE* = 0.364, *z* = -3.238, *p* = 0.001
- **SNR**: *β* = -0.13, *SE* = 0.044, *z* = -2.896, *p* = 0.004

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 0.22 | 0.36 | 0.59 | 0.552 | 0.552 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 1.18 | 0.36 | 3.24 | 0.001 | 0.004 | ** |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.96 | 0.36 | 2.64 | 0.008 | 0.017 | * |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.89, *p* = 0.012, η²_G = 0.040
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.71 | 23 | = 0.486 | 0.11 [-0.28, 0.57] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 3.01 | 23 | = 0.019 | 0.49 [0.15, 1.08] | small | * |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 2.25 | 23 | = 0.052 | 0.34 [0.01, 0.90] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 518.27, BIC = 531.93
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -1.88, *SE* = 1.848, *z* = -1.016, *p* = 0.309
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -2.38, *SE* = 1.837, *z* = -1.297, *p* = 0.195
- **SNR**: *β* = 1.36, *SE* = 0.790, *z* = 1.722, *p* = 0.085

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.88 | 1.85 | 1.02 | 0.309 | 0.523 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 2.38 | 1.84 | 1.30 | 0.195 | 0.478 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 0.50 | 1.83 | 0.28 | 0.783 | 0.783 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.17, *p* = 0.319, η²_G = 0.015
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 1.27 | 23 | = 0.323 | 0.24 [-0.17, 0.69] | small | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 1.38 | 23 | = 0.323 | 0.28 [-0.15, 0.71] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 0.17 | 23 | = 0.864 | 0.03 [-0.39, 0.46] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 272.93, BIC = 286.59
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.13, *SE* = 0.355, *z* = 0.368, *p* = 0.713
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 0.18, *SE* = 0.353, *z* = 0.515, *p* = 0.607
- **SNR**: *β* = 0.62, *SE* = 0.144, *z* = 4.341, *p* < .001

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.13 | 0.36 | -0.37 | 0.713 | 0.939 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -0.18 | 0.35 | -0.51 | 0.607 | 0.939 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.05 | 0.35 | -0.14 | 0.885 | 0.939 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.05, *p* = 0.947, η²_G = 0.001
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.20 | 23 | = 0.899 | 0.05 [-0.38, 0.46] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -0.13 | 23 | = 0.899 | -0.03 [-0.45, 0.40] | negligible | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.33 | 23 | = 0.899 | -0.07 [-0.49, 0.36] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 729.08, BIC = 742.74
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = -1.48, *SE* = 8.587, *z* = -0.173, *p* = 0.863
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = -20.95, *SE* = 8.669, *z* = -2.417, *p* = 0.016
- **SNR**: *β* = -1.12, *SE* = 0.978, *z* = -1.143, *p* = 0.253

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | 1.48 | 8.59 | 0.17 | 0.863 | 0.863 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | 20.95 | 8.67 | 2.42 | 0.016 | 0.046 | * |
| Increase by 2 (no 1) - Increase by 3 (no 1) | 19.47 | 8.75 | 2.23 | 0.026 | 0.051 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.96, *p* = 0.062, η²_G = 0.051
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | 0.27 | 23 | = 0.787 | 0.05 [-0.37, 0.48] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | 2.11 | 23 | = 0.127 | 0.49 [-0.01, 0.87] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | 1.80 | 23 | = 0.127 | 0.45 [-0.07, 0.80] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 330.53, BIC = 344.19
- **Increase by 2 (no 1) vs Increase by 1 (no 1)**: *β* = 0.69, *SE* = 0.423, *z* = 1.640, *p* = 0.101
- **Increase by 3 (no 1) vs Increase by 1 (no 1)**: *β* = 1.02, *SE* = 0.428, *z* = 2.380, *p* = 0.017
- **SNR**: *β* = 0.09, *SE* = 0.057, *z* = 1.569, *p* = 0.117

_Reference condition: **Increase by 1 (no 1)** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| Increase by 1 (no 1) - Increase by 2 (no 1) | -0.69 | 0.42 | -1.64 | 0.101 | 0.192 | n.s. |
| Increase by 1 (no 1) - Increase by 3 (no 1) | -1.02 | 0.43 | -2.38 | 0.017 | 0.051 | n.s. |
| Increase by 2 (no 1) - Increase by 3 (no 1) | -0.33 | 0.43 | -0.75 | 0.452 | 0.452 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 3 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.46, *p* = 0.096, η²_G = 0.014
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Increase by 1 (no 1) vs Increase by 2 (no 1) | -2.44 | 23 | = 0.069 | -0.20 [-0.95, -0.05] | negligible | n.s. |
| Increase by 1 (no 1) vs Increase by 3 (no 1) | -1.95 | 23 | = 0.095 | -0.28 [-0.84, 0.04] | small | n.s. |
| Increase by 2 (no 1) vs Increase by 3 (no 1) | -0.33 | 23 | = 0.742 | -0.05 [-0.49, 0.35] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.012). Post-hoc tests revealed:
  - Increase by 1 (no 1) showed greater amplitude than Increase by 3 (no 1) (*d* = 0.49)
**P3b latency:** Marginal trend toward condition differences (*p* = 0.062)
**P3b amplitude:** Marginal trend toward condition differences (*p* = 0.096)

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
