# Statistical Analysis Report: tables

**Generated:** 2025-11-03 15:50:22

---

## 1. Analysis Overview

**Total Measurements:** 258
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
| 2a | 12 | 105.33 ms | 7.30 | 2.11 | [96.00, 116.00] |
| 2b | 12 | 109.33 ms | 9.08 | 2.62 | [96.00, 120.00] |
| 2c | 9 | 110.67 ms | 9.38 | 3.13 | [96.00, 120.00] |
| 2d | 13 | 107.69 ms | 8.40 | 2.33 | [96.00, 120.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 12 | -4.87 µV | 3.24 | 0.94 | [-10.36, -1.35] |
| 2b | 12 | -4.40 µV | 2.31 | 0.67 | [-7.71, -1.57] |
| 2c | 9 | -4.60 µV | 2.18 | 0.73 | [-8.76, -2.33] |
| 2d | 13 | -4.16 µV | 3.56 | 0.99 | [-13.12, -0.31] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 14 | 177.43 ms | 19.94 | 5.33 | [140.00, 212.00] |
| 2b | 19 | 168.21 ms | 24.05 | 5.52 | [140.00, 212.00] |
| 2c | 16 | 182.25 ms | 20.65 | 5.16 | [152.00, 212.00] |
| 2d | 18 | 176.22 ms | 22.85 | 5.39 | [140.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 14 | -9.23 µV | 4.57 | 1.22 | [-18.03, -5.04] |
| 2b | 19 | -8.53 µV | 3.14 | 0.72 | [-14.89, -2.25] |
| 2c | 16 | -6.63 µV | 3.69 | 0.92 | [-16.52, -1.80] |
| 2d | 18 | -6.60 µV | 3.55 | 0.84 | [-11.66, -1.09] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 12 | 102.00 ms | 18.49 | 5.34 | [72.00, 128.00] |
| 2b | 9 | 89.78 ms | 19.40 | 6.47 | [64.00, 120.00] |
| 2c | 10 | 102.40 ms | 21.43 | 6.78 | [64.00, 128.00] |
| 2d | 13 | 109.23 ms | 16.20 | 4.49 | [80.00, 128.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2a | 12 | 6.20 µV | 2.85 | 0.82 | [3.19, 12.01] |
| 2b | 9 | 5.61 µV | 4.20 | 1.40 | [2.22, 15.75] |
| 2c | 10 | 7.19 µV | 4.08 | 1.29 | [2.73, 15.84] |
| 2d | 13 | 5.90 µV | 3.88 | 1.08 | [1.35, 13.64] |


### 2.4 P3b Component

#### Latency (Peak)

_No descriptive statistics available._

#### Amplitude (Peak)

_No descriptive statistics available._


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 Fz Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 333.08, BIC = 345.88
- **2b vs 2a**: *β* = 3.94, *SE* = 2.954, *z* = 1.335, *p* = 0.182
- **2c vs 2a**: *β* = 4.94, *SE* = 3.229, *z* = 1.529, *p* = 0.126
- **2d vs 2a**: *β* = 1.49, *SE* = 2.996, *z* = 0.497, *p* = 0.619
- **SNR**: *β* = 1.09, *SE* = 0.741, *z* = 1.476, *p* = 0.140

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -3.94 | 2.95 | -1.33 | 0.182 | 0.634 | n.s. |
| 2a - 2c | -4.94 | 3.23 | -1.53 | 0.126 | 0.555 | n.s. |
| 2a - 2d | -1.49 | 3.00 | -0.50 | 0.619 | 0.855 | n.s. |
| 2b - 2c | -0.99 | 3.26 | -0.31 | 0.760 | 0.855 | n.s. |
| 2b - 2d | 2.45 | 3.02 | 0.81 | 0.416 | 0.801 | n.s. |
| 2c - 2d | 3.45 | 3.08 | 1.12 | 0.264 | 0.706 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 187.52, BIC = 200.32
- **2b vs 2a**: *β* = 0.55, *SE* = 0.611, *z* = 0.892, *p* = 0.373
- **2c vs 2a**: *β* = 1.46, *SE* = 0.663, *z* = 2.208, *p* = 0.027
- **2d vs 2a**: *β* = 2.75, *SE* = 0.610, *z* = 4.506, *p* < .001
- **SNR**: *β* = -1.55, *SE* = 0.151, *z* = -10.282, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -0.54 | 0.61 | -0.89 | 0.373 | 0.373 | n.s. |
| 2a - 2c | -1.46 | 0.66 | -2.21 | 0.027 | 0.105 | n.s. |
| 2a - 2d | -2.75 | 0.61 | -4.51 | < .001 | < .001 | *** |
| 2b - 2c | -0.92 | 0.66 | -1.39 | 0.165 | 0.303 | n.s. |
| 2b - 2d | -2.20 | 0.61 | -3.60 | < .001 | 0.002 | ** |
| 2c - 2d | -1.28 | 0.62 | -2.06 | 0.039 | 0.113 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 604.96, BIC = 620.39
- **2b vs 2a**: *β* = -9.16, *SE* = 6.001, *z* = -1.526, *p* = 0.127
- **2c vs 2a**: *β* = 2.98, *SE* = 6.282, *z* = 0.474, *p* = 0.635
- **2d vs 2a**: *β* = -1.44, *SE* = 6.099, *z* = -0.236, *p* = 0.813
- **SNR**: *β* = -0.33, *SE* = 1.234, *z* = -0.263, *p* = 0.792

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 9.16 | 6.00 | 1.53 | 0.127 | 0.493 | n.s. |
| 2a - 2c | -2.98 | 6.28 | -0.47 | 0.635 | 0.867 | n.s. |
| 2a - 2d | 1.44 | 6.10 | 0.24 | 0.813 | 0.867 | n.s. |
| 2b - 2c | -12.14 | 5.78 | -2.10 | 0.036 | 0.197 | n.s. |
| 2b - 2d | -7.72 | 5.54 | -1.39 | 0.164 | 0.511 | n.s. |
| 2c - 2d | 4.42 | 5.90 | 0.75 | 0.453 | 0.837 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.75, *p* = 0.539, η²_G = 0.078
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.75 | 5 | = 0.734 | 0.52 [-0.44, 0.84] | medium | n.s. |
| 2a vs 2c | -0.52 | 5 | = 0.752 | -0.21 [-0.72, 0.72] | small | n.s. |
| 2a vs 2d | 0.32 | 5 | = 0.759 | 0.17 [-0.62, 0.72] | negligible | n.s. |
| 2b vs 2c | -1.17 | 5 | = 0.734 | -0.64 [-1.19, 0.10] | medium | n.s. |
| 2b vs 2d | -1.12 | 5 | = 0.734 | -0.37 [-1.08, 0.09] | small | n.s. |
| 2c vs 2d | 0.85 | 5 | = 0.734 | 0.35 [-0.43, 0.85] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 352.98, BIC = 368.41
- **2b vs 2a**: *β* = 1.70, *SE* = 1.005, *z* = 1.690, *p* = 0.091
- **2c vs 2a**: *β* = 2.87, *SE* = 1.025, *z* = 2.796, *p* = 0.005
- **2d vs 2a**: *β* = 3.11, *SE* = 0.996, *z* = 3.124, *p* = 0.002
- **SNR**: *β* = -1.03, *SE* = 0.195, *z* = -5.288, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | -1.70 | 1.00 | -1.69 | 0.091 | 0.317 | n.s. |
| 2a - 2c | -2.87 | 1.03 | -2.80 | 0.005 | 0.026 | * |
| 2a - 2d | -3.11 | 1.00 | -3.12 | 0.002 | 0.011 | * |
| 2b - 2c | -1.17 | 0.94 | -1.24 | 0.214 | 0.382 | n.s. |
| 2b - 2d | -1.42 | 0.91 | -1.56 | 0.118 | 0.317 | n.s. |
| 2c - 2d | -0.25 | 0.95 | -0.26 | 0.795 | 0.795 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.11, *p* = 0.376, η²_G = 0.153
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | -1.46 | 5 | = 0.564 | -0.91 [-1.03, 0.28] | large | n.s. |
| 2a vs 2c | -1.21 | 5 | = 0.564 | -0.85 [-1.28, 0.24] | large | n.s. |
| 2a vs 2d | -1.47 | 5 | = 0.564 | -0.64 [-1.37, 0.10] | medium | n.s. |
| 2b vs 2c | 0.11 | 5 | = 0.920 | 0.05 [-0.67, 0.54] | negligible | n.s. |
| 2b vs 2d | 0.45 | 5 | = 0.920 | 0.26 [-1.00, 0.15] | small | n.s. |
| 2c vs 2d | 0.28 | 5 | = 0.920 | 0.21 [-0.45, 0.83] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 381.17, BIC = 393.66
- **2b vs 2a**: *β* = -15.12, *SE* = 5.798, *z* = -2.607, *p* = 0.009
- **2c vs 2a**: *β* = -4.01, *SE* = 6.014, *z* = -0.666, *p* = 0.505
- **2d vs 2a**: *β* = 3.01, *SE* = 5.678, *z* = 0.530, *p* = 0.596
- **SNR**: *β* = 4.14, *SE* = 2.916, *z* = 1.420, *p* = 0.156

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 15.12 | 5.80 | 2.61 | 0.009 | 0.045 | * |
| 2a - 2c | 4.01 | 6.01 | 0.67 | 0.505 | 0.755 | n.s. |
| 2a - 2d | -3.01 | 5.68 | -0.53 | 0.596 | 0.755 | n.s. |
| 2b - 2c | -11.11 | 6.99 | -1.59 | 0.112 | 0.379 | n.s. |
| 2b - 2d | -18.13 | 6.19 | -2.93 | 0.003 | 0.020 | * |
| 2c - 2d | -7.02 | 5.40 | -1.30 | 0.194 | 0.476 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.91, *p* = 0.202, η²_G = 0.744
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 2.00 | 1 | = 0.443 | 2.26 [-0.33, 2.18] | large | n.s. |
| 2a vs 2c | 0.40 | 1 | = 0.909 | 0.53 [-0.96, 0.89] | medium | n.s. |
| 2a vs 2d | -0.11 | 1 | = 0.930 | -0.14 [-1.05, 1.05] | negligible | n.s. |
| 2b vs 2c | -6.00 | 1 | = 0.251 | -3.79 [-4.27, 2.05] | large | n.s. |
| 2b vs 2d | -17.00 | 1 | = 0.224 | -7.60 [-2.72, 0.13] | large | n.s. |
| 2c vs 2d | -5.00 | 1 | = 0.251 | -1.39 [-1.95, 0.22] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 231.55, BIC = 244.04
- **2b vs 2a**: *β* = -0.45, *SE* = 1.162, *z* = -0.389, *p* = 0.697
- **2c vs 2a**: *β* = -0.59, *SE* = 1.218, *z* = -0.481, *p* = 0.630
- **2d vs 2a**: *β* = -1.29, *SE* = 1.123, *z* = -1.148, *p* = 0.251
- **SNR**: *β* = 2.10, *SE* = 0.569, *z* = 3.698, *p* < .001

_Reference condition: **2a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 2a - 2b | 0.45 | 1.16 | 0.39 | 0.697 | 0.966 | n.s. |
| 2a - 2c | 0.59 | 1.22 | 0.48 | 0.630 | 0.966 | n.s. |
| 2a - 2d | 1.29 | 1.12 | 1.15 | 0.251 | 0.824 | n.s. |
| 2b - 2c | 0.13 | 1.36 | 0.10 | 0.921 | 0.966 | n.s. |
| 2b - 2d | 0.84 | 1.22 | 0.69 | 0.492 | 0.966 | n.s. |
| 2c - 2d | 0.70 | 1.11 | 0.64 | 0.525 | 0.966 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.23, *p* = 0.870, η²_G = 0.159
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2a vs 2b | 0.36 | 1 | = 0.936 | 0.31 [-0.77, 1.38] | small | n.s. |
| 2a vs 2c | 0.75 | 1 | = 0.936 | 1.06 [-1.17, 0.70] | large | n.s. |
| 2a vs 2d | -1.17 | 1 | = 0.936 | -1.65 [-1.74, 0.54] | large | n.s. |
| 2b vs 2c | -0.09 | 1 | = 0.943 | -0.10 [-2.67, 2.33] | negligible | n.s. |
| 2b vs 2d | -0.53 | 1 | = 0.936 | -0.58 [-1.43, 0.73] | medium | n.s. |
| 2c vs 2d | -9.13 | 1 | = 0.417 | -2.58 [-0.80, 1.06] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.4 P3b Component

#### Latency (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._

#### Amplitude (Peak)

_LMM results not available._

_ANOVA results not available._

_Pairwise test results not available._


---

## 4. Overall Interpretation

### Key Findings

No significant main effects or interactions were detected at the α = .05 level.

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

#### Amplitude

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
