# ERP Analysis Methodology

## ERP Component Identification and Measurement

We use a **collapsed localizer** approach (Luck & Gaspelin, 2017) where data is averaged across all experimental conditions to identify component peaks and define measurement windows. This prevents circular analysis and the inflation of Type I error rates that can occur when analysis parameters are derived from the same data being tested (Kriegeskorte et al., 2009). For each ERP component of interest (P1, N1, and P3b), we first defined an a priori search range (P1 60-120ms, N1 125-200ms, P3b 320-590) based on prior literature, then computed either Global Field Power (GFP; Lehmann & Skrandies, 1980) or region-of-interest (ROI) mean amplitude from the collapsed grand average to objectively identify peak latency. We define measurement windows using Full Width at Half Maximum (FWHM), which adapts window width to the actual duration of each component.

Within FWHM-derived measurement windows, we quantify **mean amplitude** and **50% fractional area latency** (FAL) as our primary dependent variables. Mean amplitude has advantages over peak amplitude measures: it is insensitive to high-frequency noise (functioning as a low-pass filter), completely unaffected by trial-to-trial latency variability, represents a linear measure that can be meaningfully averaged, and provides an unbiased estimate equally likely to over- or under-estimate the true value (Luck, 2014). For quantifying latency, we use fractional area latency at the 50% criterion, which identifies the time point at which the cumulative area under the curve reaches half of the total area within the measurement window. FAL represents the temporal midpoint of the component and is less influencd by high-frequency noise than peak latency measures (Kiesel et al., 2008). 

We still record 'peak' amplitude and 'peak' latency as secondary metrics, for use if we want them. 

We use MNE-Python (Gramfort et al., 2013).

## Statistical Analysis

We perform statistical analyses using repeated-measures analysis of variance (ANOVA) with condition as a within-subjects factor, with the Pingouin statistical package in Python. When the assumption of sphericity is violated (as assessed by Mauchly's test), degrees of freedom are adjusted using the Greenhouse-Geisser correction to maintain appropriate Type I error rates. We perform pairwise comparisons between conditions using paired-samples *t*-tests with effect sizes using Cohen's *d* for repeated measures, which accounts for the correlation between measurements. To control for multiple comparisons, we applied the Benjamini-Hochberg False Discovery Rate (FDR) correction (Benjamini & Hochberg, 1995) separately within each component, treating each component as an independent family of tests. This approach balances statistical power against the risk of false positives more effectively than traditional Bonferroni correction while maintaining error control. We report both uncorrected *p*-values and FDR-corrected *q*-values, with statistical significance defined as *q* < .05.

---

## References

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological)*, *57*(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x

Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., Goj, R., Jas, M., Brooks, T., Parkkonen, L., & Hämäläinen, M. (2013). MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience*, *7*, 267. https://doi.org/10.3389/fnins.2013.00267

Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology*, *45*(2), 250–274. https://doi.org/10.1111/j.1469-8986.2007.00618.x

Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S. F., & Baker, C. I. (2009). Circular analysis in systems neuroscience: The dangers of double dipping. *Nature Neuroscience*, *12*(5), 535–540. https://doi.org/10.1038/nn.2303

Lehmann, D., & Skrandies, W. (1980). Reference-free identification of components of checkerboard-evoked multichannel potential fields. *Electroencephalography and Clinical Neurophysiology*, *48*(6), 609–621. https://doi.org/10.1016/0013-4694(80)90419-8

Luck, S. J. (2014). *An introduction to the event-related potential technique* (2nd ed.). MIT Press.

Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology*, *54*(1), 146–157. https://doi.org/10.1111/psyp.12639
