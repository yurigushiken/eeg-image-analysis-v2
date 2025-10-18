# Statistical Analysis Report: tables

**Generated:** 2025-10-18 13:33:27

---

## 1. Analysis Overview

**Total Measurements:** 336
**Number of Subjects:** 24
**Number of Conditions:** 5

**Components Analyzed:** N1, P1, P3b
**Dependent Variables:** Mean Amplitude (ROI), Latency (50% Fractional Area)

### 1.1 Measurement Methodology

- **Component Detection:** collapsed_localizer_fwhm
- **Latency Measure:** 50% Fractional Area Latency (temporal midpoint)
- **Amplitude Measure:** Mean amplitude in ROI within FWHM window
- **Baseline Period:** [-100, 0] ms

### 1.2 Quality Control Filters

- **Minimum SNR:** ≥ None
- **Missing Data:** Excluded listwise for ANOVA/pairwise

### 1.3 Missing Data Policy

ANOVA and pairwise tests were run on complete cases. Subject-condition combinations with missing latency values or below-threshold SNR were excluded listwise. Linear mixed-effects models retained all subjects with valid measurements to optimally handle missing data.

---

## 2. Descriptive Statistics

This section presents means, standard deviations, and sample sizes for each condition.

### 2.1 N1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | -3.81 µV | 2.28 | 0.46 | [-10.19, 0.01] |
| 3 to 5 | 22 | -3.56 µV | 2.30 | 0.49 | [-10.07, -0.45] |
| 4 to 5 | 22 | -4.58 µV | 3.06 | 0.65 | [-12.04, -1.15] |
| 5 to 5 | 23 | -3.67 µV | 2.29 | 0.48 | [-8.89, -0.38] |
| 6 to 5 | 15 | -4.27 µV | 1.45 | 0.37 | [-6.59, -2.20] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 24 | 173.23 ms | 13.91 | 2.84 | [149.58, 203.95] |
| 3 to 5 | 22 | 167.14 ms | 12.33 | 2.63 | [144.53, 197.29] |
| 4 to 5 | 22 | 168.88 ms | 12.27 | 2.62 | [144.32, 193.68] |
| 5 to 5 | 23 | 171.63 ms | 12.98 | 2.71 | [140.71, 196.48] |
| 6 to 5 | 15 | 170.83 ms | 13.32 | 3.44 | [149.25, 192.24] |


### 2.2 P1 Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 11 | 1.88 µV | 2.14 | 0.65 | [0.07, 7.57] |
| 3 to 5 | 13 | 1.82 µV | 1.52 | 0.42 | [0.11, 4.75] |
| 4 to 5 | 16 | 3.70 µV | 4.39 | 1.10 | [0.21, 14.96] |
| 5 to 5 | 15 | 1.68 µV | 1.35 | 0.35 | [0.14, 4.26] |
| 6 to 5 | 4 | 1.80 µV | 0.97 | 0.48 | [1.09, 3.16] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 11 | 99.09 ms | 4.76 | 1.43 | [91.21, 107.01] |
| 3 to 5 | 13 | 97.68 ms | 5.23 | 1.45 | [88.64, 105.75] |
| 4 to 5 | 16 | 99.13 ms | 3.87 | 0.97 | [93.40, 105.73] |
| 5 to 5 | 15 | 99.62 ms | 3.40 | 0.88 | [94.30, 106.01] |
| 6 to 5 | 4 | 98.49 ms | 4.87 | 2.44 | [93.27, 104.08] |


### 2.3 P3b Component

#### Mean Amplitude (ROI)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 19 | 3.38 µV | 1.90 | 0.44 | [0.46, 7.23] |
| 3 to 5 | 16 | 3.29 µV | 2.29 | 0.57 | [0.33, 7.96] |
| 4 to 5 | 15 | 3.93 µV | 2.60 | 0.67 | [0.24, 10.15] |
| 5 to 5 | 13 | 1.32 µV | 1.10 | 0.30 | [0.04, 3.68] |
| 6 to 5 | 12 | 2.07 µV | 1.54 | 0.44 | [0.05, 5.00] |

#### Latency (50% Fractional Area)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| 2 to 5 | 19 | 455.26 ms | 34.18 | 7.84 | [389.39, 510.22] |
| 3 to 5 | 16 | 474.39 ms | 41.41 | 10.35 | [385.96, 556.12] |
| 4 to 5 | 15 | 488.24 ms | 42.17 | 10.89 | [366.16, 532.25] |
| 5 to 5 | 13 | 458.73 ms | 67.39 | 18.69 | [358.82, 571.28] |
| 6 to 5 | 12 | 499.09 ms | 56.06 | 16.18 | [384.12, 571.55] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 425.06, BIC = 446.37
- **3 to 5 vs 2 to 5**: *β* = 0.57, *SE* = 0.416, *z* = 1.383, *p* = 0.167
- **4 to 5 vs 2 to 5**: *β* = -0.47, *SE* = 0.418, *z* = -1.116, *p* = 0.264
- **5 to 5 vs 2 to 5**: *β* = 0.42, *SE* = 0.411, *z* = 1.025, *p* = 0.305
- **6 to 5 vs 2 to 5**: *β* = -0.66, *SE* = 0.474, *z* = -1.398, *p* = 0.162
- **SNR**: *β* = -0.39, *SE* = 0.063, *z* = -6.274, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.24, *p* = 0.005, η²_G = 0.121
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -0.96 | 13 | = 0.442 | -0.17 [-0.75, 0.16] | negligible | n.s. |
| 2 to 5 vs 4 to 5 | 2.71 | 13 | = 0.059 | 0.60 [-0.17, 0.74] | medium | n.s. |
| 2 to 5 vs 5 to 5 | -1.20 | 13 | = 0.360 | -0.28 [-0.58, 0.29] | small | n.s. |
| 2 to 5 vs 6 to 5 | 0.55 | 13 | = 0.656 | 0.16 [-0.33, 0.79] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 2.77 | 13 | = 0.059 | 0.78 [-0.03, 0.93] | medium | n.s. |
| 3 to 5 vs 5 to 5 | -0.45 | 13 | = 0.663 | -0.14 [-0.32, 0.57] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | 1.37 | 13 | = 0.321 | 0.39 [-0.23, 0.96] | small | n.s. |
| 4 to 5 vs 5 to 5 | -3.06 | 13 | = 0.059 | -0.87 [-0.78, 0.13] | large | n.s. |
| 4 to 5 vs 6 to 5 | -1.63 | 13 | = 0.253 | -0.55 [-1.04, 0.17] | medium | n.s. |
| 5 to 5 vs 6 to 5 | 1.65 | 13 | = 0.253 | 0.53 [-0.16, 1.05] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 807.09, BIC = 828.40
- **3 to 5 vs 2 to 5**: *β* = -5.12, *SE* = 2.412, *z* = -2.122, *p* = 0.034
- **4 to 5 vs 2 to 5**: *β* = -3.53, *SE* = 2.423, *z* = -1.456, *p* = 0.145
- **5 to 5 vs 2 to 5**: *β* = -0.73, *SE* = 2.383, *z* = -0.306, *p* = 0.760
- **6 to 5 vs 2 to 5**: *β* = -2.73, *SE* = 2.754, *z* = -0.992, *p* = 0.321
- **SNR**: *β* = -0.33, *SE* = 0.372, *z* = -0.899, *p* = 0.369

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 1.08, *p* = 0.376, η²_G = 0.020
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.53 | 13 | = 0.621 | 0.29 [0.01, 0.94] | small | n.s. |
| 2 to 5 vs 4 to 5 | 2.10 | 13 | = 0.561 | 0.42 [-0.20, 0.70] | small | n.s. |
| 2 to 5 vs 5 to 5 | 0.77 | 13 | = 0.663 | 0.10 [-0.38, 0.48] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | 0.64 | 13 | = 0.663 | 0.16 [-0.31, 0.81] | negligible | n.s. |
| 3 to 5 vs 4 to 5 | 0.45 | 13 | = 0.736 | 0.10 [-0.58, 0.34] | negligible | n.s. |
| 3 to 5 vs 5 to 5 | -0.94 | 13 | = 0.663 | -0.18 [-0.85, 0.07] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -0.67 | 13 | = 0.663 | -0.13 [-0.76, 0.40] | negligible | n.s. |
| 4 to 5 vs 5 to 5 | -1.40 | 13 | = 0.621 | -0.30 [-0.65, 0.25] | small | n.s. |
| 4 to 5 vs 6 to 5 | -0.81 | 13 | = 0.663 | -0.25 [-0.80, 0.37] | small | n.s. |
| 5 to 5 vs 6 to 5 | 0.28 | 13 | = 0.784 | 0.05 [-0.50, 0.65] | negligible | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


### 3.2 P1 Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 252.63, BIC = 269.25
- **3 to 5 vs 2 to 5**: *β* = -0.61, *SE* = 0.669, *z* = -0.911, *p* = 0.362
- **4 to 5 vs 2 to 5**: *β* = 1.03, *SE* = 0.663, *z* = 1.555, *p* = 0.120
- **5 to 5 vs 2 to 5**: *β* = -1.09, *SE* = 0.664, *z* = -1.643, *p* = 0.100
- **6 to 5 vs 2 to 5**: *β* = 0.56, *SE* = 1.014, *z* = 0.552, *p* = 0.581
- **SNR**: *β* = 1.46, *SE* = 0.195, *z* = 7.508, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 347.81, BIC = 364.43
- **3 to 5 vs 2 to 5**: *β* = -1.01, *SE* = 1.484, *z* = -0.682, *p* = 0.495
- **4 to 5 vs 2 to 5**: *β* = -0.26, *SE* = 1.471, *z* = -0.174, *p* = 0.862
- **5 to 5 vs 2 to 5**: *β* = 0.21, *SE* = 1.469, *z* = 0.141, *p* = 0.888
- **6 to 5 vs 2 to 5**: *β* = 0.21, *SE* = 2.314, *z* = 0.093, *p* = 0.926
- **SNR**: *β* = -0.02, *SE* = 0.435, *z* = -0.036, *p* = 0.972

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

_ANOVA results not available._

**Pairwise Comparisons (Supplementary Analysis):**

_Pairwise tests could not be computed (insufficient paired samples)._


### 3.3 P3b Component

#### Mean Amplitude (ROI)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 286.77, BIC = 305.31
- **3 to 5 vs 2 to 5**: *β* = 0.22, *SE* = 0.473, *z* = 0.460, *p* = 0.646
- **4 to 5 vs 2 to 5**: *β* = 0.84, *SE* = 0.481, *z* = 1.758, *p* = 0.079
- **5 to 5 vs 2 to 5**: *β* = -1.15, *SE* = 0.518, *z* = -2.228, *p* = 0.026
- **6 to 5 vs 2 to 5**: *β* = -0.47, *SE* = 0.530, *z* = -0.882, *p* = 0.378
- **SNR**: *β* = 0.51, *SE* = 0.070, *z* = 7.308, *p* < .001

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 4.02, *p* = 0.012, η²_G = 0.372
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | 1.46 | 6 | = 0.277 | 0.86 [-0.47, 0.69] | large | n.s. |
| 2 to 5 vs 4 to 5 | 0.30 | 6 | = 0.776 | 0.18 [-0.73, 0.43] | negligible | n.s. |
| 2 to 5 vs 5 to 5 | 5.64 | 6 | = 0.013 | 2.62 [0.11, 1.60] | large | * |
| 2 to 5 vs 6 to 5 | 2.66 | 6 | = 0.098 | 1.18 [0.26, 1.97] | large | n.s. |
| 3 to 5 vs 4 to 5 | -0.75 | 6 | = 0.598 | -0.43 [-0.73, 0.55] | small | n.s. |
| 3 to 5 vs 5 to 5 | 3.45 | 6 | = 0.068 | 2.07 [0.18, 1.99] | large | n.s. |
| 3 to 5 vs 6 to 5 | 0.65 | 6 | = 0.598 | 0.45 [-0.32, 1.07] | small | n.s. |
| 4 to 5 vs 5 to 5 | 2.62 | 6 | = 0.098 | 1.56 [-0.14, 1.43] | large | n.s. |
| 4 to 5 vs 6 to 5 | 1.46 | 6 | = 0.277 | 0.70 [-0.28, 1.24] | medium | n.s. |
| 5 to 5 vs 6 to 5 | -2.06 | 6 | = 0.171 | -1.23 [-1.00, 0.45] | large | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

#### Latency (50% Fractional Area)

**Linear Mixed-Effects Model (Primary Analysis):**

- Model converged successfully
- AIC = 802.78, BIC = 821.32
- **3 to 5 vs 2 to 5**: *β* = 19.02, *SE* = 15.026, *z* = 1.265, *p* = 0.206
- **4 to 5 vs 2 to 5**: *β* = 34.71, *SE* = 15.296, *z* = 2.269, *p* = 0.023
- **5 to 5 vs 2 to 5**: *β* = 7.10, *SE* = 16.407, *z* = 0.433, *p* = 0.665
- **6 to 5 vs 2 to 5**: *β* = 46.52, *SE* = 16.753, *z* = 2.777, *p* = 0.005
- **SNR**: *β* = 1.08, *SE* = 2.191, *z* = 0.491, *p* = 0.623

_Reference condition: **2 to 5** (all condition effects are contrasts vs. this baseline)._
_Note: LMM uses all available subject data via maximum likelihood estimation._

**Repeated-Measures ANOVA (Supplementary Analysis):**

- *F* = 2.96, *p* = 0.040, η²_G = 0.214
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons (Supplementary Analysis):**

_Post-hoc tests with FDR correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| 2 to 5 vs 3 to 5 | -2.24 | 6 | = 0.132 | -0.35 [-1.44, -0.12] | small | n.s. |
| 2 to 5 vs 4 to 5 | -3.78 | 6 | = 0.085 | -1.79 [-1.39, -0.09] | large | n.s. |
| 2 to 5 vs 5 to 5 | -0.13 | 6 | = 0.903 | -0.07 [-0.64, 0.64] | negligible | n.s. |
| 2 to 5 vs 6 to 5 | -2.51 | 6 | = 0.132 | -0.92 [-1.94, -0.24] | large | n.s. |
| 3 to 5 vs 4 to 5 | -3.28 | 6 | = 0.085 | -1.65 [-1.06, 0.26] | large | n.s. |
| 3 to 5 vs 5 to 5 | 0.25 | 6 | = 0.899 | 0.14 [-0.73, 0.70] | negligible | n.s. |
| 3 to 5 vs 6 to 5 | -1.77 | 6 | = 0.207 | -0.70 [-1.91, -0.22] | medium | n.s. |
| 4 to 5 vs 5 to 5 | 2.26 | 6 | = 0.132 | 0.98 [-0.36, 1.12] | large | n.s. |
| 4 to 5 vs 6 to 5 | 1.42 | 6 | = 0.255 | 0.44 [-0.64, 0.80] | small | n.s. |
| 5 to 5 vs 6 to 5 | -1.68 | 6 | = 0.207 | -0.58 [-1.05, 0.42] | medium | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_


---

## 4. Overall Interpretation

### Key Findings

**N1 amplitude:** Significant main effect of condition (*p* = 0.005) (no significant pairwise comparisons)
**P3b amplitude:** Significant main effect of condition (*p* = 0.012). Post-hoc tests revealed:
  - 2 to 5 showed greater amplitude than 5 to 5 (*d* = 2.62)
**P3b latency:** Significant main effect of condition (*p* = 0.040) (no significant pairwise comparisons)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

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

### 5.2 P1 Component

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

### 5.3 P3b Component

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
