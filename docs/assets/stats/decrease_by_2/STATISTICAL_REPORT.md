# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:32:56

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
| 3 to 1 | 6 | 111.33 ms | 10.25 | 4.18 | [96.00, 120.00] |
| 4 to 2 | 9 | 110.22 ms | 10.60 | 3.53 | [96.00, 120.00] |
| 5 to 3 | 4 | 114.00 ms | 12.00 | 6.00 | [96.00, 120.00] |
| 6 to 4 | 7 | 109.71 ms | 12.83 | 4.85 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 6 | 2.36 µV | 0.75 | 0.31 | [1.30, 3.43] |
| 4 to 2 | 9 | 3.62 µV | 2.13 | 0.71 | [0.57, 6.68] |
| 5 to 3 | 4 | 3.38 µV | 1.31 | 0.66 | [1.64, 4.79] |
| 6 to 4 | 7 | 2.95 µV | 1.43 | 0.54 | [1.05, 5.06] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 182.60 ms | 15.37 | 3.44 | [156.00, 208.00] |
| 4 to 2 | 24 | 174.67 ms | 14.81 | 3.02 | [148.00, 208.00] |
| 5 to 3 | 24 | 175.00 ms | 15.57 | 3.18 | [148.00, 208.00] |
| 6 to 4 | 24 | 174.50 ms | 21.03 | 4.29 | [148.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | -4.43 µV | 2.50 | 0.56 | [-10.41, -1.36] |
| 4 to 2 | 24 | -6.13 µV | 3.05 | 0.62 | [-11.92, -1.89] |
| 5 to 3 | 24 | -5.84 µV | 2.77 | 0.57 | [-12.11, -1.76] |
| 6 to 4 | 24 | -5.44 µV | 2.66 | 0.54 | [-12.20, -1.44] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 22 | 116.73 ms | 10.23 | 2.18 | [100.00, 128.00] |
| 4 to 2 | 15 | 120.27 ms | 7.17 | 1.85 | [108.00, 128.00] |
| 5 to 3 | 17 | 114.82 ms | 9.77 | 2.37 | [100.00, 128.00] |
| 6 to 4 | 15 | 113.33 ms | 8.77 | 2.26 | [100.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 22 | 3.64 µV | 1.88 | 0.40 | [1.37, 9.14] |
| 4 to 2 | 15 | 2.66 µV | 1.19 | 0.31 | [1.28, 4.87] |
| 5 to 3 | 17 | 2.98 µV | 1.30 | 0.32 | [0.85, 4.76] |
| 6 to 4 | 15 | 3.75 µV | 2.13 | 0.55 | [0.71, 7.60] |


### 2.4 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 475.60 ms | 27.00 | 6.04 | [420.00, 536.00] |
| 4 to 2 | 19 | 474.74 ms | 38.07 | 8.73 | [420.00, 536.00] |
| 5 to 3 | 20 | 465.00 ms | 27.65 | 6.18 | [420.00, 528.00] |
| 6 to 4 | 19 | 487.37 ms | 32.31 | 7.41 | [432.00, 536.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 3 to 1 | 20 | 5.77 µV | 3.01 | 0.67 | [1.30, 14.34] |
| 4 to 2 | 19 | 5.47 µV | 3.07 | 0.70 | [1.15, 11.62] |
| 5 to 3 | 20 | 5.53 µV | 2.46 | 0.55 | [1.54, 10.28] |
| 6 to 4 | 19 | 5.40 µV | 2.49 | 0.57 | [1.73, 9.62] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 200.87, BIC = 209.68
- **4 to 2 vs 3 to 1**: *β* = 1.81, *SE* = 3.024, *z* = 0.598, *p* = 0.550
- **5 to 3 vs 3 to 1**: *β* = -0.52, *SE* = 4.090, *z* = -0.127, *p* = 0.899
- **6 to 4 vs 3 to 1**: *β* = -1.67, *SE* = 3.729, *z* = -0.447, *p* = 0.655
- **SNR**: *β* = 1.89, *SE* = 1.332, *z* = 1.421, *p* = 0.155

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -1.81 | 3.02 | -0.60 | 0.550 | 0.981 | n.s. |
| 3 to 1 - 5 to 3 | 0.52 | 4.09 | 0.13 | 0.899 | 0.981 | n.s. |
| 3 to 1 - 6 to 4 | 1.67 | 3.73 | 0.45 | 0.655 | 0.981 | n.s. |
| 4 to 2 - 5 to 3 | 2.33 | 3.87 | 0.60 | 0.548 | 0.981 | n.s. |
| 4 to 2 - 6 to 4 | 3.48 | 3.08 | 1.13 | 0.259 | 0.834 | n.s. |
| 5 to 3 - 6 to 4 | 1.15 | 3.28 | 0.35 | 0.726 | 0.981 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 96.22, BIC = 105.03
- **4 to 2 vs 3 to 1**: *β* = 1.60, *SE* = 0.587, *z* = 2.731, *p* = 0.006
- **5 to 3 vs 3 to 1**: *β* = 1.42, *SE* = 0.692, *z* = 2.047, *p* = 0.041
- **6 to 4 vs 3 to 1**: *β* = 1.14, *SE* = 0.646, *z* = 1.772, *p* = 0.076
- **SNR**: *β* = 0.78, *SE* = 0.226, *z* = 3.464, *p* = 0.001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -1.60 | 0.59 | -2.73 | 0.006 | 0.037 | * |
| 3 to 1 - 5 to 3 | -1.42 | 0.69 | -2.05 | 0.041 | 0.187 | n.s. |
| 3 to 1 - 6 to 4 | -1.14 | 0.65 | -1.77 | 0.076 | 0.272 | n.s. |
| 4 to 2 - 5 to 3 | 0.19 | 0.72 | 0.26 | 0.796 | 0.873 | n.s. |
| 4 to 2 - 6 to 4 | 0.46 | 0.67 | 0.69 | 0.490 | 0.868 | n.s. |
| 5 to 3 - 6 to 4 | 0.27 | 0.59 | 0.46 | 0.644 | 0.873 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 771.25, BIC = 788.90
- **4 to 2 vs 3 to 1**: *β* = -7.61, *SE* = 3.828, *z* = -1.988, *p* = 0.047
- **5 to 3 vs 3 to 1**: *β* = -7.52, *SE* = 3.879, *z* = -1.940, *p* = 0.052
- **6 to 4 vs 3 to 1**: *β* = -8.02, *SE* = 3.877, *z* = -2.067, *p* = 0.039
- **SNR**: *β* = 0.42, *SE* = 0.449, *z* = 0.940, *p* = 0.347

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 7.61 | 3.83 | 1.99 | 0.047 | 0.213 | n.s. |
| 3 to 1 - 5 to 3 | 7.52 | 3.88 | 1.94 | 0.052 | 0.213 | n.s. |
| 3 to 1 - 6 to 4 | 8.02 | 3.88 | 2.07 | 0.039 | 0.211 | n.s. |
| 4 to 2 - 5 to 3 | -0.09 | 3.57 | -0.02 | 0.980 | 0.999 | n.s. |
| 4 to 2 - 6 to 4 | 0.40 | 3.57 | 0.11 | 0.910 | 0.999 | n.s. |
| 5 to 3 - 6 to 4 | 0.49 | 3.56 | 0.14 | 0.890 | 0.999 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.38, *p* = 0.259, η²_G = 0.031
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 2.02 | 19 | = 0.299 | 0.48 [-0.04, 0.94] | small | n.s. |
| 3 to 1 vs 5 to 3 | 1.67 | 19 | = 0.299 | 0.35 [-0.11, 0.86] | small | n.s. |
| 3 to 1 vs 6 to 4 | 1.50 | 19 | = 0.299 | 0.39 [-0.15, 0.82] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.47 | 19 | = 0.855 | -0.13 [-0.44, 0.40] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -0.09 | 19 | = 0.929 | -0.02 [-0.41, 0.43] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 0.37 | 19 | = 0.855 | 0.09 [-0.40, 0.45] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 405.19, BIC = 422.84
- **4 to 2 vs 3 to 1**: *β* = -1.37, *SE* = 0.531, *z* = -2.584, *p* = 0.010
- **5 to 3 vs 3 to 1**: *β* = -0.84, *SE* = 0.538, *z* = -1.567, *p* = 0.117
- **6 to 4 vs 3 to 1**: *β* = -0.46, *SE* = 0.538, *z* = -0.848, *p* = 0.397
- **SNR**: *β* = -0.40, *SE* = 0.062, *z* = -6.471, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 1.37 | 0.53 | 2.58 | 0.010 | 0.057 | n.s. |
| 3 to 1 - 5 to 3 | 0.84 | 0.54 | 1.57 | 0.117 | 0.393 | n.s. |
| 3 to 1 - 6 to 4 | 0.46 | 0.54 | 0.85 | 0.397 | 0.636 | n.s. |
| 4 to 2 - 5 to 3 | -0.53 | 0.49 | -1.07 | 0.285 | 0.635 | n.s. |
| 4 to 2 - 6 to 4 | -0.92 | 0.49 | -1.85 | 0.064 | 0.283 | n.s. |
| 5 to 3 - 6 to 4 | -0.39 | 0.49 | -0.78 | 0.433 | 0.636 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.50, *p* = 0.021, η²_G = 0.079
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 3.55 | 19 | = 0.013 | 0.76 [0.26, 1.33] | medium | * |
| 3 to 1 vs 5 to 3 | 2.36 | 19 | = 0.088 | 0.65 [0.03, 1.03] | medium | n.s. |
| 3 to 1 vs 6 to 4 | 1.54 | 19 | = 0.272 | 0.46 [-0.14, 0.83] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.56 | 19 | = 0.582 | -0.13 [-0.52, 0.32] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.39 | 19 | = 0.272 | -0.31 [-0.68, 0.18] | small | n.s. |
| 5 to 3 vs 6 to 4 | -0.74 | 19 | = 0.565 | -0.18 [-0.56, 0.29] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 507.37, BIC = 523.01
- **4 to 2 vs 3 to 1**: *β* = 2.85, *SE* = 2.651, *z* = 1.075, *p* = 0.283
- **5 to 3 vs 3 to 1**: *β* = -2.34, *SE* = 2.506, *z* = -0.933, *p* = 0.351
- **6 to 4 vs 3 to 1**: *β* = -4.86, *SE* = 2.665, *z* = -1.824, *p* = 0.068
- **SNR**: *β* = -0.30, *SE* = 0.455, *z* = -0.653, *p* = 0.514

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -2.85 | 2.65 | -1.07 | 0.283 | 0.631 | n.s. |
| 3 to 1 - 5 to 3 | 2.34 | 2.51 | 0.93 | 0.351 | 0.631 | n.s. |
| 3 to 1 - 6 to 4 | 4.86 | 2.67 | 1.82 | 0.068 | 0.279 | n.s. |
| 4 to 2 - 5 to 3 | 5.19 | 2.79 | 1.86 | 0.063 | 0.279 | n.s. |
| 4 to 2 - 6 to 4 | 7.71 | 2.91 | 2.65 | 0.008 | 0.047 | * |
| 5 to 3 - 6 to 4 | 2.52 | 2.79 | 0.91 | 0.365 | 0.631 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.88, *p* = 0.057, η²_G = 0.157
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -1.71 | 8 | = 0.221 | -0.77 [-0.86, 0.27] | medium | n.s. |
| 3 to 1 vs 5 to 3 | -0.38 | 8 | = 0.715 | -0.16 [-0.34, 0.74] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 1.07 | 8 | = 0.379 | 0.35 [0.00, 1.27] | small | n.s. |
| 4 to 2 vs 5 to 3 | 1.60 | 8 | = 0.221 | 0.61 [-0.05, 1.34] | medium | n.s. |
| 4 to 2 vs 6 to 4 | 3.33 | 8 | = 0.062 | 1.39 [0.34, 2.12] | large | n.s. |
| 5 to 3 vs 6 to 4 | 1.66 | 8 | = 0.221 | 0.55 [-0.49, 0.78] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 213.66, BIC = 229.30
- **4 to 2 vs 3 to 1**: *β* = -0.55, *SE* = 0.287, *z* = -1.895, *p* = 0.058
- **5 to 3 vs 3 to 1**: *β* = -0.55, *SE* = 0.271, *z* = -2.023, *p* = 0.043
- **6 to 4 vs 3 to 1**: *β* = 0.12, *SE* = 0.284, *z* = 0.438, *p* = 0.661
- **SNR**: *β* = 0.45, *SE* = 0.051, *z* = 8.806, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | 0.54 | 0.29 | 1.89 | 0.058 | 0.165 | n.s. |
| 3 to 1 - 5 to 3 | 0.55 | 0.27 | 2.02 | 0.043 | 0.161 | n.s. |
| 3 to 1 - 6 to 4 | -0.12 | 0.28 | -0.44 | 0.661 | 0.885 | n.s. |
| 4 to 2 - 5 to 3 | 0.00 | 0.30 | 0.01 | 0.989 | 0.989 | n.s. |
| 4 to 2 - 6 to 4 | -0.67 | 0.32 | -2.12 | 0.034 | 0.158 | n.s. |
| 5 to 3 - 6 to 4 | -0.67 | 0.30 | -2.25 | 0.024 | 0.137 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.59, *p* = 0.028, η²_G = 0.159
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 1.98 | 8 | = 0.165 | 0.98 [-0.16, 1.00] | large | n.s. |
| 3 to 1 vs 5 to 3 | 1.40 | 8 | = 0.239 | 0.48 [-0.10, 1.02] | small | n.s. |
| 3 to 1 vs 6 to 4 | 0.12 | 8 | = 0.908 | 0.03 [-0.60, 0.56] | negligible | n.s. |
| 4 to 2 vs 5 to 3 | -2.10 | 8 | = 0.165 | -0.72 [-1.13, 0.20] | medium | n.s. |
| 4 to 2 vs 6 to 4 | -2.90 | 8 | = 0.120 | -1.04 [-1.57, -0.02] | large | n.s. |
| 5 to 3 vs 6 to 4 | -1.62 | 8 | = 0.217 | -0.49 [-1.09, 0.24] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 767.33, BIC = 783.82
- **4 to 2 vs 3 to 1**: *β* = 0.65, *SE* = 9.701, *z* = 0.067, *p* = 0.946
- **5 to 3 vs 3 to 1**: *β* = -8.89, *SE* = 9.298, *z* = -0.956, *p* = 0.339
- **6 to 4 vs 3 to 1**: *β* = 14.10, *SE* = 9.610, *z* = 1.467, *p* = 0.142
- **SNR**: *β* = 0.53, *SE* = 0.773, *z* = 0.690, *p* = 0.490

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.65 | 9.70 | -0.07 | 0.946 | 0.946 | n.s. |
| 3 to 1 - 5 to 3 | 8.89 | 9.30 | 0.96 | 0.339 | 0.666 | n.s. |
| 3 to 1 - 6 to 4 | -14.10 | 9.61 | -1.47 | 0.142 | 0.536 | n.s. |
| 4 to 2 - 5 to 3 | 9.54 | 9.32 | 1.02 | 0.306 | 0.666 | n.s. |
| 4 to 2 - 6 to 4 | -13.44 | 9.40 | -1.43 | 0.152 | 0.536 | n.s. |
| 5 to 3 - 6 to 4 | -22.98 | 9.25 | -2.48 | 0.013 | 0.076 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.85, *p* = 0.151, η²_G = 0.068
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | -0.23 | 16 | = 0.949 | -0.07 [-0.44, 0.55] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.07 | 16 | = 0.949 | 0.02 [-0.28, 0.70] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | -1.84 | 16 | = 0.253 | -0.65 [-0.93, 0.11] | medium | n.s. |
| 4 to 2 vs 5 to 3 | 0.27 | 16 | = 0.949 | 0.09 [-0.46, 0.54] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | -1.58 | 16 | = 0.269 | -0.47 [-0.91, 0.15] | small | n.s. |
| 5 to 3 vs 6 to 4 | -2.31 | 16 | = 0.208 | -0.66 [-1.16, -0.07] | medium | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 349.97, BIC = 366.47
- **4 to 2 vs 3 to 1**: *β* = 0.48, *SE* = 0.584, *z* = 0.827, *p* = 0.408
- **5 to 3 vs 3 to 1**: *β* = 0.31, *SE* = 0.555, *z* = 0.565, *p* = 0.572
- **6 to 4 vs 3 to 1**: *β* = 0.32, *SE* = 0.577, *z* = 0.560, *p* = 0.576
- **SNR**: *β* = 0.21, *SE* = 0.051, *z* = 4.177, *p* < .001

_Reference condition: **3 to 1** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 3 to 1 - 4 to 2 | -0.48 | 0.58 | -0.83 | 0.408 | 0.957 | n.s. |
| 3 to 1 - 5 to 3 | -0.31 | 0.56 | -0.56 | 0.572 | 0.986 | n.s. |
| 3 to 1 - 6 to 4 | -0.32 | 0.58 | -0.56 | 0.576 | 0.986 | n.s. |
| 4 to 2 - 5 to 3 | 0.17 | 0.55 | 0.31 | 0.760 | 0.986 | n.s. |
| 4 to 2 - 6 to 4 | 0.16 | 0.56 | 0.29 | 0.775 | 0.986 | n.s. |
| 5 to 3 - 6 to 4 | -0.01 | 0.55 | -0.02 | 0.987 | 0.987 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.40, *p* = 0.753, η²_G = 0.008
- Greenhouse-Geisser corrected: *p* = 0.666 (ε = 0.643)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 3 to 1 vs 4 to 2 | 0.69 | 16 | = 0.845 | 0.11 [-0.29, 0.72] | negligible | n.s. |
| 3 to 1 vs 5 to 3 | 0.20 | 16 | = 0.845 | 0.06 [-0.41, 0.55] | negligible | n.s. |
| 3 to 1 vs 6 to 4 | 0.84 | 16 | = 0.845 | 0.24 [-0.38, 0.61] | small | n.s. |
| 4 to 2 vs 5 to 3 | -0.31 | 16 | = 0.845 | -0.07 [-0.63, 0.37] | negligible | n.s. |
| 4 to 2 vs 6 to 4 | 0.56 | 16 | = 0.845 | 0.11 [-0.38, 0.65] | negligible | n.s. |
| 5 to 3 vs 6 to 4 | 1.12 | 16 | = 0.845 | 0.21 [-0.45, 0.54] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.021). Post-hoc tests revealed:
  - 3 to 1 showed greater amplitude than 4 to 2 (*d* = 0.76)
**P1 latency:** Marginal trend toward condition differences (*p* = 0.057)
**P1 amplitude:** Significant main effect of condition (*p* = 0.028) (no significant pairwise comparisons)

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
