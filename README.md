# EEG Image Analysis v2 – YAML-Driven ERP Pipeline

Download the data here https://drive.google.com/drive/folders/1mJu-efTMwXCqSteZpuZeM0nJjyMoPFPM?usp=drive_link

# ERP Analysis Methodology

## ERP Component Identification and Measurement

We use a **collapsed localizer** approach (Luck & Gaspelin, 2017) where data is averaged across all experimental conditions to identify component peaks and define measurement windows. This prevents circular analysis and the inflation of Type I error rates that can occur when analysis parameters are derived from the same data being tested (Kriegeskorte et al., 2009). For each ERP component of interest (P1, N1, and P3b), we first defined an a priori search range (P1 60-120ms, N1 125-200ms, P3b 320-590) based on prior literature, then computed either Global Field Power (GFP; Lehmann & Skrandies, 1980) or region-of-interest (ROI) mean amplitude from the collapsed grand average to objectively identify peak latency. We define measurement windows using Full Width at Half Maximum (FWHM), which adapts window width to the actual duration of each component.

Within FWHM-derived measurement windows, we quantify either **mean amplitude** and **50% fractional area latency** (FAL) as our primary dependent variables. Mean amplitude has advantages over peak amplitude measures: it is insensitive to high-frequency noise (functioning as a low-pass filter), completely unaffected by trial-to-trial latency variability, represents a linear measure that can be meaningfully averaged, and provides an unbiased estimate equally likely to over- or under-estimate the true value (Luck, 2014). For quantifying latency, we use fractional area latency at the 50% criterion, which identifies the time point at which the cumulative area under the curve reaches half of the total area within the measurement window. FAL represents the temporal midpoint of the component and is less influencd by high-frequency noise than peak latency measures (Kiesel et al., 2008). 

We still record 'peak' amplitude and 'peak' latency as secondary metrics for comparison purposes. All preprocessing and analysis are conducted using MNE-Python (Gramfort et al., 2013), with baseline correction applied to a -100 to 0 ms prestimulus interval to remove DC offsets and slow drifts.

## Statistical Analysis

We perform statistical analyses using repeated-measures analysis of variance (ANOVA) with condition as a within-subjects factor, with the Pingouin statistical package in Python. When the assumption of sphericity is violated (as assessed by Mauchly's test), degrees of freedom are adjusted using the Greenhouse-Geisser correction to maintain appropriate Type I error rates. We perform pairwise comparisons between conditions using paired-samples *t*-tests with effect sizes using Cohen's *d* for repeated measures, which accounts for the correlation between measurements. To control for multiple comparisons, we applied the Benjamini-Hochberg False Discovery Rate (FDR) correction (Benjamini & Hochberg, 1995) separately within each component, treating each component as an independent family of tests. This approach balances statistical power against the risk of false positives more effectively than traditional Bonferroni correction while maintaining rigorous error control. We report both uncorrected *p*-values and FDR-corrected *q*-values, with statistical significance defined as *q* < .05.

---

## References

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological)*, *57*(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x

Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., Goj, R., Jas, M., Brooks, T., Parkkonen, L., & Hämäläinen, M. (2013). MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience*, *7*, 267. https://doi.org/10.3389/fnins.2013.00267

Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology*, *45*(2), 250–274. https://doi.org/10.1111/j.1469-8986.2007.00618.x

Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S. F., & Baker, C. I. (2009). Circular analysis in systems neuroscience: The dangers of double dipping. *Nature Neuroscience*, *12*(5), 535–540. https://doi.org/10.1038/nn.2303

Lehmann, D., & Skrandies, W. (1980). Reference-free identification of components of checkerboard-evoked multichannel potential fields. *Electroencephalography and Clinical Neurophysiology*, *48*(6), 609–621. https://doi.org/10.1016/0013-4694(80)90419-8

Luck, S. J. (2014). *An introduction to the event-related potential technique* (2nd ed.). MIT Press.

Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology*, *54*(1), 146–157. https://doi.org/10.1111/psyp.12639


## Overview

This project implements a **declarative, YAML-driven ERP analysis pipeline** that transforms raw EEG epoch data into publication-ready figures, subject- and condition-level measurements, and an analysis website. You define each analysis in a simple YAML configuration file (Phase 1/2A), then run inferential statistics and plots from subject-level measurements (Phases 2B–2C).

## Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone <repository-url>
cd eeg-image-analysis-v2

# Create and activate the conda environment
conda env create -f environment.yml
conda activate eeg-image

# Verify installation
python -c "import mne; print(f'MNE version: {mne.__version__}')"
```

**Environment details:**
- Python: `3.12`
- Key dependencies: `mne==1.10.1`, `numpy`, `pandas`, `matplotlib`, `pyyaml`, `pytest`
- See [environment.yml](environment.yml) for complete pinned dependencies

### 2. Run Your First Analysis

```bash
# Run the sample "Small Increasing vs Decreasing" analysis (default dataset)
python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing.yaml

# (Optional) Run statistics for that analysis using the default stats config
# Update input_csv in configs/statistics/default.yaml if needed
python scripts/run_statistics.py --config configs/statistics/default.yaml
```

**What happens:**
1. Loads subject epoch files from `data/`
2. Selects trials by condition codes (e.g., "12", "13" for increasing)
3. Computes P1, N1, P3b component ERPs with ROI aggregation
4. Generates overlay plots and peak-locked topomaps
5. Writes figures to `docs/assets/plots/small_increasing_vs_decreasing/`
6. Creates analysis page at `docs/analysis/small_increasing_vs_decreasing.md`
7. Updates `docs/index.md` with thumbnails and lightbox

**Expected outputs:**
- Figures: `docs/assets/plots/small_increasing_vs_decreasing/{P1,N1,P3b}.png`
- Collapsed localizer figure: `docs/assets/plots/small_increasing_vs_decreasing-collapsed_localizer.png`
- Analysis page: `docs/analysis/small_increasing_vs_decreasing.md`
- QC report: `docs/assets/tables/small_increasing_vs_decreasing/qc_summary.csv`
- Runtime metrics: `docs/assets/tables/small_increasing_vs_decreasing/run_metrics.json`
- Collapsed localizer JSON: `docs/assets/tables/small_increasing_vs_decreasing/collapsed_localizer_results.json`
- Subject-level measurements (Phase 2A): `docs/assets/tables/small_increasing_vs_decreasing/subject_measurements.csv`
  - Per subject × component × condition: `latency_frac_area_ms`, `mean_amplitude_roi`, `snr`, window metadata
- Condition-level summary (descriptive): `docs/assets/tables/small_increasing_vs_decreasing/condition_measurements.csv`
  - Per component × condition: `mean_amplitude_roi`, `latency_frac_area_ms`, window metadata

### 3. View the Website

```bash
# Serve locally with Python's built-in server
cd docs
python -m http.server 8000

# Open http://localhost:8000 in your browser
# Or publish to GitHub Pages (see documentation)
```

## Project Structure

```
eeg-image-analysis-v2/
├── configs/                          # Configuration files
│   ├── electrodes.yaml               # ROI electrode mappings (N1_L, N1_R, P1, P3B)
│   ├── components.yaml               # Component time windows (P1, N1, P3b)
│   └── analyses/                     # Analysis YAML configurations
│       ├── small_increasing_vs_decreasing.yaml
│       ├── cardinality_within_small.yaml
│       └── from1_to_any.yaml
├── src/eeg/                          # Core analysis & statistics library
│   ├── config.py                     # YAML schema loading/validation
│   ├── io.py                         # Epochs I/O, montage enforcement
│   ├── select.py                     # Trial selection (ACC1 filter, condition sets)
│   ├── erp.py                        # Subject/grand average computation
│   ├── measures.py                   # Component metrics (peak amplitude/latency)
│   ├── plots.py                      # ERP overlays and topomaps
│   ├── report.py                     # Markdown page generation and index grid
│   ├── statistics.py                 # Phase 2B: ANOVA, pairwise tests, LMM, descriptives
│   └── stats_plots.py                # Phase 2C: Boxplot, violin, and effect size plots
├── scripts/
│   ├── run_analysis.py               # Run a single analysis from YAML (Phase 1/2A)
│   ├── run_all_analyses.py           # Batch all YAMLs in configs/analyses/
│   ├── run_statistics.py             # Run inferential stats + plots (Phases 2B–2C)
│   ├── run_all_statistics.py         # Batch stats for all completed analyses
│   └── create_stat_configs.py        # Generate per-analysis stats YAMLs
├── docs/                             # Published website (GitHub Pages)
│   ├── index.md                      # Auto-generated analysis gallery
│   ├── analysis/                     # Per-analysis pages
│   └── assets/                       # Figures and tables
│       ├── plots/<analysis_id>/      # PNG figures
│       └── tables/<analysis_id>/     # CSV tables and QC reports
├── tests/                            # Unit and smoke tests
├── data/                             # Raw epoch files (gitignored)
├── assets/net/                       # Montage file
│   └── AdultAverageNet128_v1.sfp
├── environment.yml                   # Conda environment specification
├── STATISTICS_WORKFLOW.md            # Stats workflow overview
├── PHASE2_ENHANCED_SPEC.md           # Phase 2C enhancements and rationale
└── PHASE2_IMPLEMENTATION_PLAN.md     # Implementation notes
```

## Understanding the YAML Configuration

Each analysis is defined by a YAML file with these key sections:

```yaml
dataset:
  root: "data/hpf_1.5_lpf_35_baseline-on"   # or your own dataset root
  pattern: "sub-*_preprocessed-epo.fif"
  montage_sfp: "assets/net/AdultAverageNet128_v1.sfp"

# Trial selection
selection:
  response: "ALL"  # or "ACC1" for Target.ACC == 1
  min_epochs_per_set: 8
  condition_sets:
    - name: "Small_Increasing"
      conditions: ["12", "13", "23"]  # Explicit numeric condition codes
    - name: "Small_Decreasing"
      conditions: ["32", "31", "21"]

# Components to analyze
components: ["P1", "N1", "P3b"]

# Preprocessing
preprocessing:
  baseline_ms: [-100, 0]

# ROI configuration
roi:
  min_channels: 4  # Minimum channels required for ROI inclusion

# Plotting options
plots:
  dpi: 300
  colors: ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#6a3d9a", "#ffff33"]
  linestyles:
    NC: "-"
    Decrease: ":"
    Increasing: "--"

# Output paths
outputs:
  plots_dir: "docs/assets/plots/small_increasing_vs_decreasing"
  tables_dir: "docs/assets/tables/small_increasing_vs_decreasing"
  page: "docs/analysis/small_increasing_vs_decreasing.md"
  # Figures are saved as <analysis_id>-<Component>.png (e.g., small_increasing_vs_decreasing-P1.png)
```

See [configs/analyses/](configs/analyses/) for complete examples.

## The Data

This repository analyzes preprocessed EEG epochs in MNE-Python FIF format:

### Dataset options
- Default: `data/lab-data-original` (empty in Git; place your converted FIFs here)
- Alternate: `data/hpf_1.5_lpf_35_baseline-on` (empty in Git)

Both directories include a small README placeholder and are kept empty in version control. Real data are gitignored. To switch datasets, edit `dataset.root` in the YAML(s) under `configs/analyses/`.

**Dataset characteristics:**
- 24 subjects (files like `sub-02_preprocessed-epo.fif`)
- ~270 epochs per subject
- 129 channels (128-channel EGI net + 1 reference)
- 250 Hz sampling rate
- Epoch duration: ~0.696s (-100 to 496 ms for )

**Metadata columns** (in each epochs file):
- `Condition`: Two-digit code (e.g., "12", "23", "33")
- `Target.ACC`: Response accuracy (0 or 1)
- `direction`: Trial direction ("I"=increasing, "D"=decreasing, "NC"=no change)
- `change_group`: Combined category ("iSS", "dLL", "NC", etc.)
- `size`: Size feature ("SS", "LL", "cross", "NC")
- Plus: `SubjectID`, `Block`, `Trial`, `Procedure`, `Target.RT`, `Trial_Continuous`

**Why explicit numeric conditions?**
This pipeline uses explicit numeric condition codes (e.g., `["12", "13"]`) rather than metadata-only filters. This provides maximum clarity and reproducibility—you see exactly which trials are included in each analysis.

## How It Works: The Pipeline Flow

```
1. YAML Config → Load analysis configuration
                ↓
2. Discovery   → Find all subject epoch files matching pattern
                ↓
3. Subject Loop → For each subject:
                  ├─ Load epochs from FIF
                  ├─ Apply montage (enforce E-code mapping)
                  ├─ Filter by response (ALL or ACC1)
                  ├─ Apply baseline correction
                  ├─ Select trials by condition codes
                  └─ Compute subject-level evoked per condition set
                ↓
4. Grand Average → Equal-weight averaging across subjects
                   Compute SEM for uncertainty bands
                ↓
5. Metrics      → For each component (P1, N1, P3b):
                 ├─ Detect cohort peak via collapsed localizer within the configured search range
                 │    - Default: ROI-based (per `configs/components.yaml`)
                 │    - Optional: Global GFP if `localizer.method: gfp`
                 ├─ Compute FWHM window around that peak
                 ├─ Aggregate ROI channels
                 ├─ Compute amplitude/latency metrics within the FWHM window
                 └─ Extract topomap averaged over ±FWHM/2 centered on the selected latency
                ↓
6. Plotting     → Generate composite figures:
                  ├─ Top panel: ERP overlay with SEM; colored vertical lines mark the selected latency (Peak by default)
                  └─ Bottom panels: Per-condition topomaps averaged over ±FWHM/2 centered on the selected latency; subtitle notes ROI- or GFP-derived window
                ↓
7. Reporting    → Write analysis page (Markdown)
                  Update index.md with thumbnails
                  Save QC summary CSV
                  Record runtime metrics JSON
```

**Measurement defaults (peak-first) and architectural decisions (the "why"):**

- **Subject-first averaging**: We compute evoked responses per subject, then average subjects with equal weight. This prevents subjects with more trials from dominating the grand average.

- **ROI aggregation**: Instead of single-channel analysis, we average across predefined regions of interest (e.g., N1_L, N1_R for N1 component). This improves signal-to-noise and reflects the spatial distribution of components.

- **Collapsed localizer FWHM windows**: Component windows come from a collapsed localizer (no manual ±20 ms). By default we use ROI-based localizer peaks specified in `configs/components.yaml`; you can switch to global GFP by setting `localizer.method: gfp`. All conditions share the same cohort window per component; amplitudes and latencies are measured within this unbiased window. ERP figure subtitles indicate whether the window is ROI-derived or GFP-derived.
- **Peak-first defaults (new):** By default, subject-level latency and amplitude now use peak-based measurements within the unbiased FWHM window:
  - `peak_latency_ms`: time of signed extremum (P*=maximum, N*=minimum)
  - `peak_amplitude_roi`: signed amplitude at that extremum
  You can switch to the previous behavior (FAL + Mean) via YAML (see below).
  Topomaps are averaged over ±FWHM/2 centered on the selected latency (Peak by default).

- **Fractional Area Latency (FAL)**: You can alternatively measure component timing using the 50% fractional area latency—the time point where cumulative area under the curve reaches 50%. This is robust and noise-resistant and remains available.
- **Graceful fallback for visuals**: If a component's GFP window cannot be detected (e.g., near epoch edge), the ERP overlay is still rendered (no dashed line/topomaps). Statistical measurements are recorded only when a valid GFP window exists.

- **Deterministic design**: NumPy random seed is set, dependencies are pinned, and outputs are bit-identical across runs—critical for scientific reproducibility.

## Common Use Cases

### Run analysis with accurate responses only (ACC1 filter)
```bash
python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing_ACC1.yaml
```

### Analyze cardinality effects (same-number pairs)
```bash
python scripts/run_analysis.py --config configs/analyses/cardinality_within_small.yaml
```

### Create a new analysis
1. Copy an existing YAML from `configs/analyses/`
2. Edit the `condition_sets` to define your trial groups
3. Adjust `components`, `baseline_ms`, `plots` as needed
4. Run: `python scripts/run_analysis.py --config configs/analyses/your_analysis.yaml`

## Statistical Analysis Ready

The pipeline now generates both:
- **Subject-level measurements (Phase 2A)** for inferential statistics: `docs/assets/tables/<analysis_id>/subject_measurements.csv`
- **Condition-level summaries** for descriptive stats/figures: `docs/assets/tables/<analysis_id>/condition_measurements.csv`

### Subject-level measurements (Phase 2A)

Each `subject_measurements.csv` row (subject × component × condition) contains at least:
- `peak_latency_ms`: Peak latency within FWHM window (default DV for timing)
- `peak_amplitude_roi`: Peak amplitude within FWHM window (default DV for amplitude)
- `latency_frac_area_ms`, `mean_amplitude_roi`: Alternative DVs (enabled for backward compatibility)
- `snr`, `baseline_noise_uv`: QC metrics
- `collapsed_peak_latency_ms`, `window_start_ms`, `window_end_ms`, `fwhm_ms`: Window metadata (collapsed localizer)

**Example (N1)**:
```csv
subject_id,component,condition,latency_frac_area_ms,mean_amplitude_roi,peak_latency_ms,window_start_ms,window_end_ms,fwhm_ms,snr
02,N1,Cardinality1,172.8,-2.72,168.0,140.2,212.6,72.4,3.1
03,N1,Cardinality2,174.6,-2.45,168.0,140.2,212.6,72.4,2.7
04,N1,Cardinality3,175.9,-3.19,168.0,140.2,212.6,72.4,3.4
```

**Key insight**: `collapsed_peak_latency_ms` is constant per component (from collapsed localizer), while subject-level `peak_latency_ms` and/or `latency_frac_area_ms` are computed within that component’s FWHM window.

### Condition-level summaries (descriptive)
`condition_measurements.csv` summarizes per-component × condition means to support descriptive tables/figures. Use `subject_measurements.csv` for inferential tests.

### Phase 2B: Statistical Testing Module

The pipeline includes a complete statistical analysis module that automatically generates:
- **Repeated-measures ANOVA** (within-subjects designs)
- **Pairwise t-tests** with multiple comparison correction (FDR, Bonferroni, Holm)
- **Linear Mixed-Effects Models (LMM)** for complex designs and missing data
- **Descriptive statistics** by condition

#### Run Statistical Analysis

```bash
# Run statistics using default configuration
python scripts/run_statistics.py --config configs/statistics/default.yaml

# Results are saved to: docs/assets/stats/<analysis_id>/
 
# Batch all analyses that have subject_measurements.csv:
python scripts/run_all_statistics.py

# Generate per-analysis stats configs (optional):
python scripts/create_stat_configs.py
```

**What it generates:**
- `anova_<component>_<measure>.csv` - ANOVA F-tests with effect sizes
- `pairwise_<component>_<measure>.csv` - All pairwise comparisons with corrections
- `lmm_<component>_<measure>.json` - Mixed model summaries with AIC/BIC
- `descriptives_<component>_<measure>.csv` - Means, SDs, SEMs by condition
- `statistical_summary.json` - Combined results summary

#### Configure Statistical Tests

Edit `configs/statistics/default.yaml` to control:

```yaml
# Input data
input_csv: "docs/assets/tables/landing_on_2/subject_measurements.csv"

# Quality control filters
filters:
  min_snr: 2.0  # Minimum signal-to-noise ratio

# Which tests to run
tests:
  anova:
    enabled: true
  pairwise:
    enabled: true
    correction: fdr_bh  # or 'bonf', 'holm', 'none'
  lmm:
    enabled: true
    fixed: condition  # Can add covariates: 'condition + snr'

# Components and dependent variables
components: ["N1", "P1", "P3b"]
dependent_variables:
  - peak_latency_ms
  - peak_amplitude_roi
```

## Configuring measurement methods (per analysis)

Each analysis YAML can optionally set measurement modes (defaults shown):

```yaml
measurement:
  latency: peak      # options: peak | fal
  amplitude: peak    # options: peak | mean
```

Plots respect this choice: colored verticals and topomap captions show “Peak” or “FAL” latency, and topomap averaging is centered on that same latency.

#### Example Results

**ANOVA on N1 Latency** (from landing_on_2 analysis):
- F(4,24) = 2.49, p = .070, η²_G = 0.064
- Suggests trend toward latency differences between conditions

**Pairwise Comparisons** (FDR-corrected):
- 3→2 vs 4→2: t(6) = -1.14, p = .546 (n.s.)
- 3→2 vs increasing 1→2: t(6) = 1.02, p = .546 (n.s.)

**Descriptive Statistics:**
```
Condition           Mean (ms)   SD      SEM     N
3 to 2              174.0       7.3     1.8     17
4 to 2              175.7       7.1     1.8     16
increasing 1 to 2   173.1       9.1     2.2     17
```

**Scientific Reference**: Kiesel et al. (2008) found fractional area latency has lower measurement error than peak latency, making it ideal for detecting subtle timing differences.

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test modules
pytest tests/test_measures.py            # Phase 1: Fractional area latency functions (17 tests)
pytest tests/test_subject_measurements.py # Phase 2A: Subject-level data collection (19 tests)
pytest tests/test_statistics.py          # Phase 2B: Statistical analysis functions (23 tests)
```

**Test Coverage:**
- **Phase 1**: Fractional area latency computation, polarity handling, edge cases
- **Phase 2A**: Subject measurement collection, QC metrics (SNR, baseline noise), CSV structure
- **Phase 2B**: ANOVA, pairwise t-tests, LMM, data filtering, output formatting

## Documentation and Links

- Website: `docs/` (served via GitHub Pages)
- Analyses: `docs/analysis/` pages and thumbnails on `docs/index.md`
- Guides: `docs/GFP_ANALYSIS_GUIDE.md`, `docs/DATA_OUTPUTS_GUIDE.md`, `STATISTICS_WORKFLOW.md`

## Website Publishing (GitHub Pages)

The `docs/` directory is ready for GitHub Pages deployment:

1. **Enable GitHub Pages** in your repository settings
2. **Set source to**: `main` branch, `/docs` folder
3. **Access your site at**: `https://<username>.github.io/<repository>/`

The homepage ([docs/index.md](docs/index.md)) displays an auto-generated grid:
- Each row = one analysis (sorted alphabetically)
- Each column = component thumbnail (P1, N1, P3b)
- Click thumbnail → full-size overlay with accessibility features

## Performance and Success Criteria

**From our specification (see `PHASE2_ENHANCED_SPEC.md`):**

- ✅ **SC-001**: End-to-end run completes in <10 minutes on 24 subjects (typical laptop: 16GB RAM, 4-core CPU)
- ✅ **SC-002**: Bit-identical outputs on re-runs (deterministic, reproducible)
- ✅ **SC-003**: Condition sets have ≥8 epochs per subject (median); empty sets reported clearly

**Asset size constraints:**
- Individual PNG ≤ 2 MB
- Total analysis assets ≤ 20 MB
- Verified via `run_metrics.json` in each analysis

## Troubleshooting

### Common Issues

**1. "Montage cannot be applied"**
- Ensure `assets/net/AdultAverageNet128_v1.sfp` exists
- Check that your epochs use standard EGI 128-channel naming

**2. "Required metadata columns missing: ['Target.ACC']"**
- You're using `response: "ACC1"` but epochs don't have `Target.ACC` column
- Solution: Use `response: "ALL"` or verify your epochs metadata

**3. "No subjects met inclusion criteria"**
- Your `min_epochs_per_set` threshold is too high
- Lower the threshold in your YAML or check your condition codes

**4. Empty plots directory**
- Check that `data/` contains `.fif` files matching your `pattern`
- Verify file paths are correct in the YAML

### Get Help

- See `docs/GFP_ANALYSIS_GUIDE.md` for the analysis method and decisions
- See `docs/DATA_OUTPUTS_GUIDE.md` for a map of generated files
- See `STATISTICS_WORKFLOW.md` for Phases 2B–2C usage and examples
- Open an issue with your YAML configuration and error messages

## Contributing

Please propose changes via YAML configuration when possible; open issues/PRs for code changes.

## License

[Add your license here]

## Citation

If you use this pipeline in your research, please cite:

```
[Add citation information when published]
```

---

**Built with**: [Spec-Driven Development](https://github.com/github/spec-kit) | **Powered by**: [MNE-Python](https://mne.tools) | **Hosted on**: GitHub Pages
