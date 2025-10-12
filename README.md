# EEG Image Analysis v2 – YAML-Driven ERP Pipeline

Download the data here https://drive.google.com/drive/folders/1mJu-efTMwXCqSteZpuZeM0nJjyMoPFPM?usp=drive_link

## Overview

This project implements a **declarative, YAML-driven ERP analysis pipeline** that transforms raw EEG epoch data into publication-ready figures and interactive web pages. Instead of writing custom analysis scripts for each research question, you define your analysis in a simple YAML configuration file.

**Key Features:**
- 🎯 **YAML-driven**: Define entire analyses in configuration files—no code changes needed
- 📊 **Multi-component support**: Analyze P1, N1, and P3b components in a single run
- 🔄 **Reproducible**: Deterministic outputs with pinned dependencies and seeded randomness
- 📈 **Publication-ready**: High-DPI figures (PNG) and CSV tables automatically generated
- 🌐 **Web publishing**: Automatic GitHub Pages integration with interactive lightbox gallery
- ✅ **Quality control**: Built-in QC reporting for subject inclusion and data quality
- 🎨 **Customizable styling**: Configure colors, line styles, and figure layout via YAML
 - 🧪 **GFP-based collapsed localizer**: Component peak and FWHM window are data-driven and shared across conditions, preventing circular analysis. Measurements are saved to CSV/JSON for stats.

## Project Philosophy

This project follows **Spec-Driven Development** principles with a strong constitution (see [.specify/memory/constitution.md](.specify/memory/constitution.md)) that enforces:

1. **Reproducible Environment**: All analyses run in a declared Python environment with pinned dependencies
2. **Data Governance**: Raw data never committed to Git; only published outputs in `docs/`
3. **Declarative Configuration**: Analyses defined via YAML, not imperative scripts
4. **ERP Standards**: Consistent component definitions, ROIs, and montage enforcement
5. **Documentation as Artifact**: Every analysis generates a Markdown page with figures and tables

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
```

**What happens:**
1. Loads 24 subject epoch files from `data/`
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
- Condition measurements CSV: `docs/assets/tables/small_increasing_vs_decreasing/condition_measurements.csv`

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
├── src/eeg/                          # Core analysis library
│   ├── config.py                     # YAML schema loading/validation
│   ├── io.py                         # Epochs I/O, montage enforcement
│   ├── select.py                     # Trial selection (ACC1 filter, condition sets)
│   ├── erp.py                        # Subject/grand average computation
│   ├── measures.py                   # Component metrics (peak amplitude/latency)
│   ├── plots.py                      # ERP overlays and topomaps
│   └── report.py                     # Markdown page generation
├── scripts/
│   └── run_analysis.py               # CLI entry point
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
├── .specify/                         # (local tooling; ignored in Git)
└── specs/                            # (design docs; ignored in Git)
```

## Understanding the YAML Configuration

Each analysis is defined by a YAML file with these key sections:

```yaml
# Dataset configuration
dataset:
  # Default dataset (FIFs converted from HAPPE-derived EEGLAB .set)
  root: "data/lab-data-original"
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
  page: "single"
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
- Epoch duration: ~0.696s (approximately -200 to 496 ms)

**Metadata columns** (in each epochs file):
- `Condition`: Two-digit code (e.g., "12", "23", "33")
- `Target.ACC`: Response accuracy (0 or 1)
- `direction`: Trial direction ("I"=increasing, "D"=decreasing, "NC"=no change)
- `change_group`: Combined category ("iSS", "dLL", "NC", etc.)
- `size`: Size feature ("SS", "LL", "cross", "NC")
- Plus: `SubjectID`, `Block`, `Trial`, `Procedure`, `Target.RT`, `Trial_Continuous`

**Why explicit numeric conditions?**
This pipeline uses explicit numeric condition codes (e.g., `["12", "13"]`) rather than metadata-based filters. This provides maximum clarity and reproducibility—you see exactly which trials are included in each analysis.

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
                  ├─ Detect cohort peak via GFP within configured search range
                  ├─ Compute FWHM window around that peak
                  ├─ Aggregate ROI channels
                  ├─ Compute mean amplitude within FWHM window
                  └─ Extract topomap averaged over FWHM window
                ↓
6. Plotting     → Generate composite figures:
                  ├─ Top panel: ERP overlay with SEM
                  └─ Bottom panels: Per-condition topomaps with peak labels
                ↓
7. Reporting    → Write analysis page (Markdown)
                  Update index.md with thumbnails
                  Save QC summary CSV
                  Record runtime metrics JSON
```

**Key architectural decisions (the "why"):**

- **Subject-first averaging**: We compute evoked responses per subject, then average subjects with equal weight. This prevents subjects with more trials from dominating the grand average.

- **ROI aggregation**: Instead of single-channel analysis, we average across predefined regions of interest (e.g., N1_L, N1_R for N1 component). This improves signal-to-noise and reflects the spatial distribution of components.

- **GFP-derived FWHM windows**: Component windows come from the GFP-based collapsed localizer (no manual ±20ms). All conditions share the same peak latency per component; amplitudes are measured within the component's FWHM window.
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

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test modules
pytest tests/test_select.py      # Trial selection logic
pytest tests/test_measures.py    # Peak detection and metrics
pytest tests/test_plots.py       # Figure generation
pytest tests/test_cli_smoke.py   # End-to-end smoke test
```

## Documentation and Links

- Website: docs/ (served via GitHub Pages)
- Analyses: `docs/analysis/` pages and thumbnails on `docs/index.md`

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

**From our specification ([specs/001-yaml-driven-erp/spec.md](specs/001-yaml-driven-erp/spec.md)):**

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

- Check the [Quickstart Guide](specs/001-yaml-driven-erp/quickstart.md) for step-by-step instructions
- Review [specs/001-yaml-driven-erp/spec.md](specs/001-yaml-driven-erp/spec.md) for edge cases and requirements
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
