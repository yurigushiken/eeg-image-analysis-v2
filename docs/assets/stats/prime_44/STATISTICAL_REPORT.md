# Statistical Analysis Report: tables

**Generated:** 2026-02-23 19:31:29

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
| 4a | 24 | 105.83 ms | 14.73 | 3.01 | [88.00, 128.00] |
| 4b | 24 | 108.33 ms | 12.42 | 2.54 | [88.00, 128.00] |
| 4c | 24 | 106.83 ms | 12.57 | 2.56 | [88.00, 128.00] |
| 4d | 24 | 112.00 ms | 12.81 | 2.62 | [88.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 24 | -3.38 µV | 3.51 | 0.72 | [-12.21, 2.05] |
| 4b | 24 | -3.25 µV | 2.62 | 0.54 | [-8.65, 0.78] |
| 4c | 24 | -5.28 µV | 5.43 | 1.11 | [-21.64, 3.41] |
| 4d | 24 | -4.13 µV | 3.71 | 0.76 | [-10.42, 1.91] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 24 | 170.83 ms | 19.82 | 4.05 | [140.00, 208.00] |
| 4b | 24 | 174.00 ms | 18.20 | 3.71 | [140.00, 208.00] |
| 4c | 24 | 173.50 ms | 20.25 | 4.13 | [144.00, 208.00] |
| 4d | 24 | 178.67 ms | 20.21 | 4.13 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 24 | -5.95 µV | 3.03 | 0.62 | [-13.75, -1.18] |
| 4b | 24 | -4.83 µV | 3.55 | 0.72 | [-13.32, 2.27] |
| 4c | 24 | -7.36 µV | 5.19 | 1.06 | [-22.56, -0.19] |
| 4d | 24 | -5.53 µV | 4.06 | 0.83 | [-15.00, 4.01] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 24 | 103.50 ms | 14.75 | 3.01 | [88.00, 128.00] |
| 4b | 24 | 107.17 ms | 13.60 | 2.78 | [88.00, 128.00] |
| 4c | 24 | 105.33 ms | 15.04 | 3.07 | [88.00, 128.00] |
| 4d | 24 | 112.00 ms | 13.55 | 2.77 | [88.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 24 | 3.46 µV | 3.01 | 0.61 | [-0.48, 9.99] |
| 4b | 24 | 3.09 µV | 2.26 | 0.46 | [-0.18, 8.53] |
| 4c | 24 | 4.43 µV | 4.03 | 0.82 | [-3.20, 16.98] |
| 4d | 24 | 4.00 µV | 4.41 | 0.90 | [-4.24, 13.40] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 24 | 454.33 ms | 7.26 | 1.48 | [448.00, 464.00] |
| 4b | 24 | 456.33 ms | 7.55 | 1.54 | [448.00, 464.00] |
| 4c | 24 | 457.00 ms | 7.20 | 1.47 | [448.00, 464.00] |
| 4d | 24 | 455.83 ms | 7.12 | 1.45 | [448.00, 464.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 4a | 24 | 1.86 µV | 5.08 | 1.04 | [-9.30, 15.92] |
| 4b | 24 | 1.12 µV | 3.57 | 0.73 | [-8.09, 6.41] |
| 4c | 24 | 1.27 µV | 4.25 | 0.87 | [-7.72, 10.67] |
| 4d | 24 | 2.67 µV | 4.77 | 0.97 | [-5.44, 16.06] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 772.99, BIC = 790.94
- **4b vs 4a**: *β* = 2.56, *SE* = 3.391, *z* = 0.756, *p* = 0.450
- **4c vs 4a**: *β* = 0.98, *SE* = 3.391, *z* = 0.288, *p* = 0.774
- **4d vs 4a**: *β* = 6.29, *SE* = 3.393, *z* = 1.854, *p* = 0.064
- **SNR**: *β* = 1.11, *SE* = 1.121, *z* = 0.992, *p* = 0.321

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -2.56 | 3.39 | -0.76 | 0.450 | 0.833 | n.s. |
| 4a - 4c | -0.98 | 3.39 | -0.29 | 0.774 | 0.870 | n.s. |
| 4a - 4d | -6.29 | 3.39 | -1.85 | 0.064 | 0.326 | n.s. |
| 4b - 4c | 1.59 | 3.39 | 0.47 | 0.640 | 0.870 | n.s. |
| 4b - 4d | -3.73 | 3.39 | -1.10 | 0.272 | 0.718 | n.s. |
| 4c - 4d | -5.32 | 3.39 | -1.57 | 0.117 | 0.464 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.21, *p* = 0.313, η²_G = 0.032
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -0.78 | 23 | = 0.664 | -0.18 [-0.58, 0.27] | negligible | n.s. |
| 4a vs 4c | -0.29 | 23 | = 0.778 | -0.07 [-0.48, 0.36] | negligible | n.s. |
| 4a vs 4d | -1.63 | 23 | = 0.352 | -0.45 [-0.77, 0.10] | small | n.s. |
| 4b vs 4c | 0.43 | 23 | = 0.778 | 0.12 [-0.34, 0.51] | negligible | n.s. |
| 4b vs 4d | -1.00 | 23 | = 0.659 | -0.29 [-0.63, 0.22] | small | n.s. |
| 4c vs 4d | -1.66 | 23 | = 0.352 | -0.41 [-0.77, 0.10] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

_LMM did not converge or had numerical issues._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -0.03 | 0.89 | -0.03 | 0.975 | 0.975 | n.s. |
| 4a - 4c | 1.85 | 0.89 | 2.09 | 0.037 | 0.187 | n.s. |
| 4a - 4d | 0.96 | 0.89 | 1.08 | 0.281 | 0.711 | n.s. |
| 4b - 4c | 1.88 | 0.89 | 2.12 | 0.034 | 0.187 | n.s. |
| 4b - 4d | 0.99 | 0.89 | 1.11 | 0.267 | 0.711 | n.s. |
| 4c - 4d | -0.90 | 0.89 | -1.01 | 0.313 | 0.711 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.76, *p* = 0.163, η²_G = 0.042
- Greenhouse-Geisser corrected: *p* = 0.180 (ε = 0.729)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -0.18 | 23 | = 0.860 | -0.04 [-0.46, 0.39] | negligible | n.s. |
| 4a vs 4c | 1.44 | 23 | = 0.434 | 0.41 [-0.14, 0.72] | small | n.s. |
| 4a vs 4d | 0.85 | 23 | = 0.483 | 0.21 [-0.25, 0.60] | small | n.s. |
| 4b vs 4c | 1.93 | 23 | = 0.396 | 0.48 [-0.04, 0.83] | small | n.s. |
| 4b vs 4d | 1.14 | 23 | = 0.434 | 0.27 [-0.20, 0.66] | small | n.s. |
| 4c vs 4d | -1.08 | 23 | = 0.434 | -0.25 [-0.65, 0.21] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 840.56, BIC = 858.51
- **4b vs 4a**: *β* = 4.36, *SE* = 4.611, *z* = 0.945, *p* = 0.345
- **4c vs 4a**: *β* = 2.66, *SE* = 4.516, *z* = 0.590, *p* = 0.555
- **4d vs 4a**: *β* = 7.92, *SE* = 4.517, *z* = 1.752, *p* = 0.080
- **SNR**: *β* = -1.51, *SE* = 1.183, *z* = -1.280, *p* = 0.201

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -4.36 | 4.61 | -0.94 | 0.345 | 0.816 | n.s. |
| 4a - 4c | -2.66 | 4.52 | -0.59 | 0.555 | 0.823 | n.s. |
| 4a - 4d | -7.91 | 4.52 | -1.75 | 0.080 | 0.393 | n.s. |
| 4b - 4c | 1.69 | 4.61 | 0.37 | 0.714 | 0.823 | n.s. |
| 4b - 4d | -3.56 | 4.60 | -0.77 | 0.439 | 0.823 | n.s. |
| 4c - 4d | -5.25 | 4.52 | -1.16 | 0.245 | 0.755 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.98, *p* = 0.410, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -0.70 | 23 | = 0.590 | -0.17 [-0.57, 0.28] | negligible | n.s. |
| 4a vs 4c | -0.85 | 23 | = 0.590 | -0.13 [-0.60, 0.25] | negligible | n.s. |
| 4a vs 4d | -1.45 | 23 | = 0.590 | -0.39 [-0.73, 0.14] | small | n.s. |
| 4b vs 4c | 0.12 | 23 | = 0.909 | 0.03 [-0.40, 0.45] | negligible | n.s. |
| 4b vs 4d | -0.92 | 23 | = 0.590 | -0.24 [-0.61, 0.24] | small | n.s. |
| 4c vs 4d | -1.00 | 23 | = 0.590 | -0.26 [-0.63, 0.22] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 520.40, BIC = 538.35
- **4b vs 4a**: *β* = 1.94, *SE* = 0.870, *z* = 2.228, *p* = 0.026
- **4c vs 4a**: *β* = -1.41, *SE* = 0.852, *z* = -1.655, *p* = 0.098
- **4d vs 4a**: *β* = 0.48, *SE* = 0.852, *z* = 0.559, *p* = 0.576
- **SNR**: *β* = -1.04, *SE* = 0.223, *z* = -4.669, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -1.94 | 0.87 | -2.23 | 0.026 | 0.123 | n.s. |
| 4a - 4c | 1.41 | 0.85 | 1.66 | 0.098 | 0.251 | n.s. |
| 4a - 4d | -0.48 | 0.85 | -0.56 | 0.576 | 0.576 | n.s. |
| 4b - 4c | 3.35 | 0.87 | 3.85 | < .001 | < .001 | *** |
| 4b - 4d | 1.46 | 0.87 | 1.69 | 0.092 | 0.251 | n.s. |
| 4c - 4d | -1.89 | 0.85 | -2.21 | 0.027 | 0.123 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.39, *p* = 0.076, η²_G = 0.052
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -1.58 | 23 | = 0.270 | -0.34 [-0.76, 0.11] | small | n.s. |
| 4a vs 4c | 1.38 | 23 | = 0.270 | 0.33 [-0.15, 0.71] | small | n.s. |
| 4a vs 4d | -0.48 | 23 | = 0.632 | -0.12 [-0.52, 0.32] | negligible | n.s. |
| 4b vs 4c | 2.87 | 23 | = 0.052 | 0.57 [0.13, 1.04] | medium | n.s. |
| 4b vs 4d | 0.69 | 23 | = 0.598 | 0.18 [-0.28, 0.56] | negligible | n.s. |
| 4c vs 4d | -1.44 | 23 | = 0.270 | -0.39 [-0.73, 0.14] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 788.34, BIC = 806.29
- **4b vs 4a**: *β* = 3.67, *SE* = 3.647, *z* = 1.005, *p* = 0.315
- **4c vs 4a**: *β* = 1.83, *SE* = 3.637, *z* = 0.504, *p* = 0.614
- **4d vs 4a**: *β* = 8.50, *SE* = 3.691, *z* = 2.303, *p* = 0.021
- **SNR**: *β* = 0.00, *SE* = 1.028, *z* = 0.001, *p* = 0.999

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -3.67 | 3.65 | -1.01 | 0.315 | 0.678 | n.s. |
| 4a - 4c | -1.83 | 3.64 | -0.50 | 0.614 | 0.851 | n.s. |
| 4a - 4d | -8.50 | 3.69 | -2.30 | 0.021 | 0.121 | n.s. |
| 4b - 4c | 1.83 | 3.64 | 0.50 | 0.615 | 0.851 | n.s. |
| 4b - 4d | -4.83 | 3.65 | -1.32 | 0.186 | 0.561 | n.s. |
| 4c - 4d | -6.67 | 3.68 | -1.81 | 0.070 | 0.304 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.94, *p* = 0.132, η²_G = 0.049
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -1.14 | 23 | = 0.398 | -0.26 [-0.66, 0.19] | small | n.s. |
| 4a vs 4c | -0.42 | 23 | = 0.680 | -0.12 [-0.51, 0.34] | negligible | n.s. |
| 4a vs 4d | -2.34 | 23 | = 0.158 | -0.60 [-0.92, -0.03] | medium | n.s. |
| 4b vs 4c | 0.42 | 23 | = 0.680 | 0.13 [-0.34, 0.51] | negligible | n.s. |
| 4b vs 4d | -1.51 | 23 | = 0.290 | -0.36 [-0.74, 0.12] | small | n.s. |
| 4c vs 4d | -2.04 | 23 | = 0.158 | -0.47 [-0.86, 0.02] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 503.62, BIC = 521.57
- **4b vs 4a**: *β* = -0.66, *SE* = 0.839, *z* = -0.786, *p* = 0.432
- **4c vs 4a**: *β* = 0.89, *SE* = 0.837, *z* = 1.067, *p* = 0.286
- **4d vs 4a**: *β* = -0.11, *SE* = 0.849, *z* = -0.129, *p* = 0.898
- **SNR**: *β* = 1.06, *SE* = 0.233, *z* = 4.523, *p* < .001

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 0.66 | 0.84 | 0.79 | 0.432 | 0.817 | n.s. |
| 4a - 4c | -0.89 | 0.84 | -1.07 | 0.286 | 0.740 | n.s. |
| 4a - 4d | 0.11 | 0.85 | 0.13 | 0.898 | 0.898 | n.s. |
| 4b - 4c | -1.55 | 0.84 | -1.85 | 0.064 | 0.327 | n.s. |
| 4b - 4d | -0.55 | 0.84 | -0.65 | 0.513 | 0.817 | n.s. |
| 4c - 4d | 1.00 | 0.85 | 1.18 | 0.236 | 0.740 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.78, *p* = 0.511, η²_G = 0.021
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | 0.60 | 23 | = 0.664 | 0.14 [-0.30, 0.55] | negligible | n.s. |
| 4a vs 4c | -0.91 | 23 | = 0.664 | -0.27 [-0.61, 0.24] | small | n.s. |
| 4a vs 4d | -0.52 | 23 | = 0.664 | -0.14 [-0.53, 0.32] | negligible | n.s. |
| 4b vs 4c | -1.38 | 23 | = 0.664 | -0.41 [-0.71, 0.15] | small | n.s. |
| 4b vs 4d | -0.95 | 23 | = 0.664 | -0.26 [-0.62, 0.23] | small | n.s. |
| 4c vs 4d | 0.44 | 23 | = 0.664 | 0.10 [-0.33, 0.51] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 660.90, BIC = 678.85
- **4b vs 4a**: *β* = 1.75, *SE* = 1.954, *z* = 0.893, *p* = 0.372
- **4c vs 4a**: *β* = 3.02, *SE* = 1.961, *z* = 1.540, *p* = 0.124
- **4d vs 4a**: *β* = 1.41, *SE* = 1.948, *z* = 0.726, *p* = 0.468
- **SNR**: *β* = 0.65, *SE* = 0.431, *z* = 1.512, *p* = 0.131

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | -1.75 | 1.95 | -0.89 | 0.372 | 0.902 | n.s. |
| 4a - 4c | -3.02 | 1.96 | -1.54 | 0.124 | 0.547 | n.s. |
| 4a - 4d | -1.41 | 1.95 | -0.73 | 0.468 | 0.902 | n.s. |
| 4b - 4c | -1.27 | 1.99 | -0.64 | 0.522 | 0.902 | n.s. |
| 4b - 4d | 0.33 | 1.95 | 0.17 | 0.865 | 0.902 | n.s. |
| 4c - 4d | 1.61 | 1.97 | 0.82 | 0.415 | 0.902 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.62, *p* = 0.606, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | -0.91 | 23 | = 0.815 | -0.27 [-0.61, 0.24] | small | n.s. |
| 4a vs 4c | -1.29 | 23 | = 0.815 | -0.37 [-0.69, 0.17] | small | n.s. |
| 4a vs 4d | -0.69 | 23 | = 0.815 | -0.21 [-0.57, 0.28] | small | n.s. |
| 4b vs 4c | -0.42 | 23 | = 0.815 | -0.09 [-0.51, 0.34] | negligible | n.s. |
| 4b vs 4d | 0.23 | 23 | = 0.817 | 0.07 [-0.37, 0.47] | negligible | n.s. |
| 4c vs 4d | 0.58 | 23 | = 0.815 | 0.16 [-0.31, 0.54] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 555.10, BIC = 573.05
- **4b vs 4a**: *β* = -0.99, *SE* = 1.053, *z* = -0.938, *p* = 0.348
- **4c vs 4a**: *β* = -0.24, *SE* = 1.057, *z* = -0.231, *p* = 0.817
- **4d vs 4a**: *β* = 0.72, *SE* = 1.050, *z* = 0.687, *p* = 0.492
- **SNR**: *β* = 0.64, *SE* = 0.240, *z* = 2.679, *p* = 0.007

_Reference condition: **4a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 4a - 4b | 0.99 | 1.05 | 0.94 | 0.348 | 0.882 | n.s. |
| 4a - 4c | 0.24 | 1.06 | 0.23 | 0.817 | 0.882 | n.s. |
| 4a - 4d | -0.72 | 1.05 | -0.69 | 0.492 | 0.882 | n.s. |
| 4b - 4c | -0.74 | 1.07 | -0.69 | 0.488 | 0.882 | n.s. |
| 4b - 4d | -1.71 | 1.05 | -1.63 | 0.104 | 0.482 | n.s. |
| 4c - 4d | -0.97 | 1.06 | -0.91 | 0.363 | 0.882 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.79, *p* = 0.503, η²_G = 0.019
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 4a vs 4b | 0.90 | 23 | = 0.720 | 0.17 [-0.24, 0.61] | negligible | n.s. |
| 4a vs 4c | 0.53 | 23 | = 0.720 | 0.13 [-0.31, 0.53] | negligible | n.s. |
| 4a vs 4d | -0.69 | 23 | = 0.720 | -0.16 [-0.56, 0.28] | negligible | n.s. |
| 4b vs 4c | -0.14 | 23 | = 0.888 | -0.04 [-0.45, 0.39] | negligible | n.s. |
| 4b vs 4d | -1.57 | 23 | = 0.720 | -0.37 [-0.75, 0.11] | small | n.s. |
| 4c vs 4d | -0.95 | 23 | = 0.720 | -0.31 [-0.62, 0.23] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.076)

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
