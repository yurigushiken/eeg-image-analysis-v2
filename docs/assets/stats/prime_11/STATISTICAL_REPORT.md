# Statistical Analysis Report: tables

**Generated:** 2025-11-03 13:46:13

---

## 1. Analysis Overview

**Total Measurements:** 255
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
| 1a | 11 | 120.36 ms | 15.74 | 4.75 | [96.00, 136.00] |
| 1b | 8 | 106.50 ms | 18.63 | 6.59 | [92.00, 136.00] |
| 1c | 8 | 118.50 ms | 20.16 | 7.13 | [92.00, 136.00] |
| 1d | 6 | 113.33 ms | 14.90 | 6.08 | [92.00, 132.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 11 | 7.78 µV | 4.87 | 1.47 | [2.81, 16.66] |
| 1b | 8 | 5.47 µV | 4.14 | 1.46 | [1.69, 14.77] |
| 1c | 8 | 3.89 µV | 1.56 | 0.55 | [1.54, 5.92] |
| 1d | 6 | 4.11 µV | 2.32 | 0.95 | [1.83, 7.69] |


### 2.2 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 10 | 175.60 ms | 13.91 | 4.40 | [156.00, 196.00] |
| 1b | 14 | 176.29 ms | 12.10 | 3.23 | [156.00, 204.00] |
| 1c | 14 | 175.43 ms | 16.14 | 4.31 | [156.00, 204.00] |
| 1d | 18 | 184.00 ms | 14.26 | 3.36 | [156.00, 204.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 10 | -6.40 µV | 3.40 | 1.07 | [-11.90, -1.82] |
| 1b | 14 | -4.73 µV | 2.12 | 0.57 | [-9.09, -1.66] |
| 1c | 14 | -6.34 µV | 3.06 | 0.82 | [-10.02, -1.58] |
| 1d | 18 | -5.36 µV | 3.21 | 0.76 | [-12.98, -1.28] |


### 2.3 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 128.62 ms | 12.20 | 3.38 | [108.00, 144.00] |
| 1b | 17 | 123.29 ms | 13.28 | 3.22 | [100.00, 144.00] |
| 1c | 16 | 123.00 ms | 16.75 | 4.19 | [100.00, 144.00] |
| 1d | 14 | 125.43 ms | 10.94 | 2.92 | [108.00, 144.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 1a | 13 | 6.72 µV | 3.58 | 0.99 | [2.63, 15.32] |
| 1b | 17 | 6.01 µV | 3.14 | 0.76 | [2.13, 13.34] |
| 1c | 16 | 6.05 µV | 3.89 | 0.97 | [1.42, 15.74] |
| 1d | 14 | 6.21 µV | 2.99 | 0.80 | [1.34, 10.50] |


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
- AIC = 287.37, BIC = 297.84
- **1b vs 1a**: *β* = -15.87, *SE* = 6.900, *z* = -2.299, *p* = 0.021
- **1c vs 1a**: *β* = -4.07, *SE* = 7.231, *z* = -0.563, *p* = 0.573
- **1d vs 1a**: *β* = -12.31, *SE* = 7.767, *z* = -1.585, *p* = 0.113
- **SNR**: *β* = -3.58, *SE* = 2.192, *z* = -1.635, *p* = 0.102

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 15.87 | 6.90 | 2.30 | 0.021 | 0.122 | n.s. |
| 1a - 1c | 4.07 | 7.23 | 0.56 | 0.573 | 0.818 | n.s. |
| 1a - 1d | 12.31 | 7.77 | 1.58 | 0.113 | 0.381 | n.s. |
| 1b - 1c | -11.79 | 6.48 | -1.82 | 0.069 | 0.300 | n.s. |
| 1b - 1d | -3.56 | 7.29 | -0.49 | 0.626 | 0.818 | n.s. |
| 1c - 1d | 8.24 | 7.43 | 1.11 | 0.268 | 0.607 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 173.90, BIC = 184.38
- **1b vs 1a**: *β* = 0.28, *SE* = 1.234, *z* = 0.225, *p* = 0.822
- **1c vs 1a**: *β* = -1.16, *SE* = 1.399, *z* = -0.830, *p* = 0.407
- **1d vs 1a**: *β* = -0.90, *SE* = 1.509, *z* = -0.599, *p* = 0.549
- **SNR**: *β* = 1.93, *SE* = 0.416, *z* = 4.629, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -0.28 | 1.23 | -0.23 | 0.822 | 0.968 | n.s. |
| 1a - 1c | 1.16 | 1.40 | 0.83 | 0.407 | 0.913 | n.s. |
| 1a - 1d | 0.90 | 1.51 | 0.60 | 0.549 | 0.913 | n.s. |
| 1b - 1c | 1.44 | 1.25 | 1.15 | 0.249 | 0.820 | n.s. |
| 1b - 1d | 1.18 | 1.36 | 0.87 | 0.386 | 0.913 | n.s. |
| 1c - 1d | -0.26 | 1.47 | -0.17 | 0.862 | 0.968 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.2 N1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 463.57, BIC = 477.75
- **1b vs 1a**: *β* = -1.21, *SE* = 5.336, *z* = -0.227, *p* = 0.821
- **1c vs 1a**: *β* = -1.31, *SE* = 5.196, *z* = -0.253, *p* = 0.800
- **1d vs 1a**: *β* = 6.18, *SE* = 5.103, *z* = 1.211, *p* = 0.226
- **SNR**: *β* = 0.13, *SE* = 1.092, *z* = 0.121, *p* = 0.904

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 1.21 | 5.34 | 0.23 | 0.821 | 0.992 | n.s. |
| 1a - 1c | 1.32 | 5.20 | 0.25 | 0.800 | 0.992 | n.s. |
| 1a - 1d | -6.18 | 5.10 | -1.21 | 0.226 | 0.641 | n.s. |
| 1b - 1c | 0.11 | 4.72 | 0.02 | 0.982 | 0.992 | n.s. |
| 1b - 1d | -7.39 | 4.48 | -1.65 | 0.099 | 0.461 | n.s. |
| 1c - 1d | -7.50 | 4.53 | -1.65 | 0.098 | 0.461 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.07, *p* = 0.410, η²_G = 0.168
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 1.48 | 3 | = 0.433 | 0.48 [-0.61, 1.62] | small | n.s. |
| 1a vs 1c | 3.83 | 3 | = 0.188 | 1.22 [-0.62, 1.08] | large | n.s. |
| 1a vs 1d | 1.29 | 3 | = 0.433 | 0.91 [-0.76, 0.91] | large | n.s. |
| 1b vs 1c | 2.18 | 3 | = 0.351 | 0.51 [-0.85, 0.69] | medium | n.s. |
| 1b vs 1d | 0.40 | 3 | = 0.852 | 0.32 [-0.82, 0.53] | small | n.s. |
| 1c vs 1d | -0.20 | 3 | = 0.852 | -0.18 [-1.07, 0.32] | negligible | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 269.43, BIC = 283.61
- **1b vs 1a**: *β* = 1.83, *SE* = 0.881, *z* = 2.073, *p* = 0.038
- **1c vs 1a**: *β* = 0.58, *SE* = 0.859, *z* = 0.678, *p* = 0.498
- **1d vs 1a**: *β* = 0.83, *SE* = 0.824, *z* = 1.009, *p* = 0.313
- **SNR**: *β* = -0.87, *SE* = 0.188, *z* = -4.605, *p* < .001

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | -1.83 | 0.88 | -2.07 | 0.038 | 0.208 | n.s. |
| 1a - 1c | -0.58 | 0.86 | -0.68 | 0.498 | 0.747 | n.s. |
| 1a - 1d | -0.83 | 0.82 | -1.01 | 0.313 | 0.675 | n.s. |
| 1b - 1c | 1.24 | 0.79 | 1.57 | 0.115 | 0.459 | n.s. |
| 1b - 1d | 0.99 | 0.75 | 1.33 | 0.184 | 0.557 | n.s. |
| 1c - 1d | -0.25 | 0.75 | -0.33 | 0.740 | 0.747 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 3.36, *p* = 0.069, η²_G = 0.458
- **Interpretation:** The main effect of condition was **marginally significant trend**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.34 | 3 | = 0.906 | 0.29 [-1.12, 0.98] | small | n.s. |
| 1a vs 1c | 3.23 | 3 | = 0.145 | 1.91 [-0.64, 1.05] | large | n.s. |
| 1a vs 1d | 0.76 | 3 | = 0.755 | 0.30 [-1.12, 0.58] | small | n.s. |
| 1b vs 1c | 1.69 | 3 | = 0.379 | 1.64 [-0.26, 1.39] | large | n.s. |
| 1b vs 1d | 0.07 | 3 | = 0.949 | 0.07 [-0.55, 0.80] | negligible | n.s. |
| 1c vs 1d | -4.18 | 3 | = 0.145 | -1.41 [-0.76, 0.59] | large | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.3 P1 Component

#### Latency (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 485.65, BIC = 500.31
- **1b vs 1a**: *β* = -5.04, *SE* = 3.964, *z* = -1.271, *p* = 0.204
- **1c vs 1a**: *β* = -6.58, *SE* = 3.955, *z* = -1.663, *p* = 0.096
- **1d vs 1a**: *β* = -1.90, *SE* = 4.036, *z* = -0.471, *p* = 0.638
- **SNR**: *β* = 0.28, *SE* = 0.510, *z* = 0.539, *p* = 0.590

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 5.04 | 3.96 | 1.27 | 0.204 | 0.680 | n.s. |
| 1a - 1c | 6.58 | 3.96 | 1.66 | 0.096 | 0.456 | n.s. |
| 1a - 1d | 1.90 | 4.04 | 0.47 | 0.638 | 0.869 | n.s. |
| 1b - 1c | 1.54 | 3.74 | 0.41 | 0.681 | 0.869 | n.s. |
| 1b - 1d | -3.14 | 3.80 | -0.83 | 0.409 | 0.794 | n.s. |
| 1c - 1d | -4.68 | 3.90 | -1.20 | 0.230 | 0.680 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 0.92, *p* = 0.452, η²_G = 0.081
- Greenhouse-Geisser corrected: *p* = 0.389 (ε = 0.399)
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | 0.98 | 6 | = 0.549 | 0.59 [-0.44, 0.92] | medium | n.s. |
| 1a vs 1c | 3.38 | 6 | = 0.089 | 0.68 [0.19, 2.20] | medium | n.s. |
| 1a vs 1d | 1.92 | 6 | = 0.268 | 0.44 [-0.59, 0.85] | small | n.s. |
| 1b vs 1c | 0.07 | 6 | = 0.948 | 0.04 [-0.46, 0.82] | negligible | n.s. |
| 1b vs 1d | -0.50 | 6 | = 0.764 | -0.28 [-0.95, 0.42] | small | n.s. |
| 1c vs 1d | -1.73 | 6 | = 0.268 | -0.36 [-1.19, 0.31] | small | n.s. |

_Note: These are paired t-tests restricted to subjects with all conditions (listwise deletion). LMM pairwise (if present above) uses all available data via mixed models._
_Legend: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Amplitude (Peak)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 313.46, BIC = 328.12
- **1b vs 1a**: *β* = -1.07, *SE* = 0.968, *z* = -1.109, *p* = 0.267
- **1c vs 1a**: *β* = -0.87, *SE* = 0.963, *z* = -0.903, *p* = 0.367
- **1d vs 1a**: *β* = -0.23, *SE* = 0.991, *z* = -0.232, *p* = 0.816
- **SNR**: *β* = 0.19, *SE* = 0.132, *z* = 1.446, *p* = 0.148

_Reference condition: **1a** (all condition effects are contrasts vs. this baseline)._
_For complete inference across all condition pairs, see the LMM Pairwise Comparisons below._

_Note: LMM uses all available subject data via maximum likelihood estimation._

**LMM Pairwise Comparisons:**

All pairwise comparisons between conditions (Holm-Sidak correction):

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1a - 1b | 1.07 | 0.97 | 1.11 | 0.267 | 0.845 | n.s. |
| 1a - 1c | 0.87 | 0.96 | 0.90 | 0.367 | 0.896 | n.s. |
| 1a - 1d | 0.23 | 0.99 | 0.23 | 0.816 | 0.966 | n.s. |
| 1b - 1c | -0.20 | 0.92 | -0.22 | 0.824 | 0.966 | n.s. |
| 1b - 1d | -0.84 | 0.93 | -0.91 | 0.364 | 0.896 | n.s. |
| 1c - 1d | -0.64 | 0.96 | -0.67 | 0.504 | 0.896 | n.s. |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
_Tests use Wald z-statistics on fixed-effect contrasts (MixedLM)._


**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.06, *p* = 0.392, η²_G = 0.086
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc paired t-tests on complete cases with FDR correction:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 1a vs 1b | -0.24 | 6 | = 0.821 | -0.12 [-0.59, 0.76] | negligible | n.s. |
| 1a vs 1c | 0.55 | 6 | = 0.720 | 0.18 [-0.44, 1.14] | negligible | n.s. |
| 1a vs 1d | -1.10 | 6 | = 0.628 | -0.54 [-0.88, 0.56] | medium | n.s. |
| 1b vs 1c | 0.66 | 6 | = 0.720 | 0.33 [-0.59, 0.68] | small | n.s. |
| 1b vs 1d | -1.27 | 6 | = 0.628 | -0.48 [-1.20, 0.22] | small | n.s. |
| 1c vs 1d | -1.52 | 6 | = 0.628 | -0.73 [-1.16, 0.33] | medium | n.s. |

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

**N1 amplitude:** Marginal trend toward condition differences (*p* = 0.069)

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
