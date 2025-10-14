# Statistical Analysis Report: tables

**Generated:** 2025-10-14 00:16:10

---

## 1. Analysis Overview

**Total Measurements:** 144
**Number of Subjects:** 24
**Number of Conditions:** 2

**Components Analyzed:** N1, P1, P3b
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

### 2.1 N1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small_Decreasing | 20 | 180.20 ms | 13.33 | 2.98 | [156.00, 212.00] |
| Small_Increasing | 23 | 170.43 ms | 20.24 | 4.22 | [144.00, 208.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small_Decreasing | 20 | -4.58 µV | 2.51 | 0.56 | [-9.67, -0.98] |
| Small_Increasing | 23 | -5.49 µV | 2.02 | 0.42 | [-10.66, -1.45] |


### 2.2 P1 Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small_Decreasing | 18 | 117.33 ms | 6.72 | 1.58 | [104.00, 124.00] |
| Small_Increasing | 13 | 108.92 ms | 11.91 | 3.30 | [96.00, 124.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small_Decreasing | 18 | 2.74 µV | 1.72 | 0.40 | [0.60, 7.19] |
| Small_Increasing | 13 | 2.19 µV | 1.06 | 0.29 | [0.44, 3.87] |


### 2.3 P3b Component

#### Latency (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small_Decreasing | 20 | 484.00 ms | 22.52 | 5.03 | [432.00, 512.00] |
| Small_Increasing | 20 | 467.20 ms | 34.45 | 7.70 | [420.00, 532.00] |

#### Amplitude (Peak)

| Condition | N | Mean | SD | SEM | Range |
|-----------|---|------|----|----|-------|
| Small_Decreasing | 20 | 5.33 µV | 2.73 | 0.61 | [2.17, 12.20] |
| Small_Increasing | 20 | 4.70 µV | 2.99 | 0.67 | [0.63, 11.98] |


---

## 3. Inferential Statistics

This section presents the results of repeated-measures statistical tests.

### 3.1 N1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 10.84, *p* = 0.004, η²_G = 0.114
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with uncorrected correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small_Decreasing vs Small_Increasing | 3.29 | 19 | = 0.004 | 0.70 [0.21, 1.26] | medium | ** |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 366.31, BIC = 373.36
- Condition effect: *β* = -10.93, *SE* = 3.499, *z* = -3.124, *p* = 0.002

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 8.25, *p* = 0.010, η²_G = 0.082
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with uncorrected correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small_Decreasing vs Small_Increasing | 2.87 | 19 | = 0.010 | 0.58 [0.13, 1.16] | medium | ** |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 189.74, BIC = 196.78
- Condition effect: *β* = -1.14, *SE* = 0.439, *z* = -2.597, *p* = 0.009


### 3.2 P1 Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 7.55, *p* = 0.019, η²_G = 0.281
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with uncorrected correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small_Decreasing vs Small_Increasing | 2.75 | 11 | = 0.019 | 1.20 [0.06, 1.52] | large | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 231.68, BIC = 237.41
- Condition effect: *β* = -8.41, *SE* = 3.342, *z* = -2.517, *p* = 0.012

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 5.13, *p* = 0.045, η²_G = 0.127
- **Interpretation:** The main effect of condition was **significant**.

**Pairwise Comparisons:**

_Post-hoc tests with uncorrected correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small_Decreasing vs Small_Increasing | 2.26 | 11 | = 0.045 | 0.73 [-0.05, 1.35] | medium | * |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 115.97, BIC = 121.70
- Condition effect: *β* = -0.76, *SE* = 0.426, *z* = -1.786, *p* = 0.074


### 3.3 P3b Component

#### Latency (Peak)

**Repeated-Measures ANOVA:**

- *F* = 2.38, *p* = 0.141, η²_G = 0.050
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with uncorrected correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small_Decreasing vs Small_Increasing | 1.54 | 17 | = 0.141 | 0.45 [-0.15, 0.88] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 388.01, BIC = 394.77
- Condition effect: *β* = -16.05, *SE* = 7.962, *z* = -2.016, *p* = 0.044

#### Amplitude (Peak)

**Repeated-Measures ANOVA:**

- *F* = 1.94, *p* = 0.182, η²_G = 0.013
- **Interpretation:** The main effect of condition was **not significant**.

**Pairwise Comparisons:**

_Post-hoc tests with uncorrected correction for multiple comparisons:_

| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |
|------------|-----|------|----------------|-------------|-------------|------|
| Small_Decreasing vs Small_Increasing | 1.39 | 17 | = 0.182 | 0.22 [-0.18, 0.84] | small | n.s. |

_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_

**Linear Mixed-Effects Model:**

- Model converged successfully
- AIC = 186.98, BIC = 193.74
- Condition effect: *β* = -0.63, *SE* = 0.435, *z* = -1.450, *p* = 0.147


---

## 4. Overall Interpretation

### Key Findings

**N1 latency:** Significant main effect of condition (*p* = 0.004). Post-hoc tests revealed:
  - Small_Decreasing showed greater latency than Small_Increasing (*d* = 0.70)
**N1 amplitude:** Significant main effect of condition (*p* = 0.010). Post-hoc tests revealed:
  - Small_Decreasing showed greater amplitude than Small_Increasing (*d* = 0.58)
**P1 latency:** Significant main effect of condition (*p* = 0.019). Post-hoc tests revealed:
  - Small_Decreasing showed greater latency than Small_Increasing (*d* = 1.20)
**P1 amplitude:** Significant main effect of condition (*p* = 0.045). Post-hoc tests revealed:
  - Small_Decreasing showed greater amplitude than Small_Increasing (*d* = 0.73)

### Research Implications

_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_

---

## 5. Visualizations

The following plots are available in the `plots/` subdirectory:

### 5.1 N1 Component

#### Latency

#### Amplitude

### 5.2 P1 Component

#### Latency

#### Amplitude

### 5.3 P3b Component

#### Latency

#### Amplitude

---

## 6. Methods Summary (for Publication)

### ERP Measurement

ERP components were measured using a collapsed localizer approach, where component peaks were identified from the grand average of all conditions combined to avoid circular analysis (Luck & Gaspelin, 2017). Measurement windows were defined as the full-width at half-maximum (FWHM) around each peak. Component latency was quantified using the 50% fractional area latency (FAL), which represents the time point at which the cumulative area under the curve reaches 50% of its total value within the measurement window. This metric provides a robust estimate of component timing with lower measurement error than peak latency (Kiesel et al., 2008). Mean amplitude was computed as the average voltage within the FWHM window across predefined regions of interest (ROI).

### Statistical Analysis

Within-subjects repeated-measures analyses were conducted using:
- Repeated-measures ANOVA with Greenhouse-Geisser correction for sphericity violations (ε < 0.75)
- Post-hoc pairwise t-tests with false discovery rate (FDR) correction for multiple comparisons
- Linear mixed-effects models (LMM) with random intercepts for subjects to handle missing data

Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.

### Software

- Python 3.12.11
- MNE-Python 1.10.1
- Statsmodels 0.14.5
- Pingouin 0.5.5

### References

- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.

---

---

*Report generated automatically by EEG Image Analysis Pipeline v2*
*For questions about this analysis, please refer to the YAML configuration and statistical output files.*
