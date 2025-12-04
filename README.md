# EEG Numerical Change Detection Analysis Pipeline

**[Download the data (LCN Lab members only)](https://drive.google.com/drive/folders/1mJu-efTMwXCqSteZpuZeM0nJjyMoPFPM?usp=drive_link)**

## Scientific Motivation

An automated ERP analysis pipeline for investigating neural signatures of numerical change detection from 128-channel EEG data, examining how the brain processes numerical transitions within and across the Parallel Individuation (PI) and Approximate Number System (ANS) ranges (1-6).

## Study Background

**Paradigm:** Visual oddball numerical change detection task
- **Participants:** 24 adults
- **Stimuli:** Dot arrays (1-6 dots, non-symbolic)
- **Task:** Detect changes in numerosity after 3-5 prime presentations
- **Data:** ~3000 usable trials, 128-channel EGI HydroCel EEG

**Key Manipulations:**
- **Numerical transitions:** e.g., 2→3, 4→5, 1→4 (±3 range)
- **Direction effects:** Increasing vs. Decreasing
- **System crossover:** Small (1-3, PI) vs. Large (4-6, ANS)
- **Response accuracy:** Correct (ACC1) vs. All responses (ALL)

**Theoretical Framework:**
- **Parallel Individuation (PI):** Precise tracking of small quantities (1-3)
- **Approximate Number System (ANS):** Ratio-dependent estimation for larger quantities (4-6)
- **Research Question:** Do PI and ANS show distinct neural signatures during numerical change detection?

## What This Pipeline Does

**Input:** Preprocessed EEG epochs (`.fif` files)
**Output:** Publication-ready figures, statistical analyses, and interactive website

**Core Functions:**
- Extracts ERP components (P1, N1, P3b, Fz) with data-driven windows
- Runs statistical analyses (Linear Mixed Models, ANOVA, pairwise tests)
- Generates publication figures (waveforms, topographies, stats plots)
- Creates interactive website gallery of all analyses

**Key Features:**
- YAML-driven configuration (no code editing needed)
- Reproducible and deterministic outputs
- Handles missing data optimally (LMM)
- Quality control metrics (SNR, trial counts)

## Quick Start

### Installation

```bash
# Clone and setup environment
git clone <repository-url>
cd eeg-image-analysis-v2
conda env create -f environment.yml
conda activate eeg-image
```

### Run an Analysis

```bash
# Run ERP analysis
python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing.yaml

# Run statistics
python scripts/run_statistics.py --config configs/statistics/default.yaml

# View results
cd docs && python -m http.server 8000
# Open http://localhost:8000
```

## Data Requirements

**Format:** Preprocessed EEG epochs in MNE-Python `.fif` format
**Montage:** 128-channel EGI HydroCel
**Metadata:** Condition codes, accuracy (`Target.ACC`)

Place your preprocessed data in:
```
data/hpf_1.5_lpf_35_baseline-on/
├── sub-02_preprocessed-epo.fif
├── sub-03_preprocessed-epo.fif
└── ...
```

## Project Structure

```
eeg-image-analysis-v2/
├── configs/
│   ├── analyses/              # ~80 analysis configurations (YAML)
│   ├── electrodes.yaml        # ROI electrode definitions
│   ├── components.yaml        # Component time windows
│   └── statistics/
├── src/eeg/                   # Core analysis library
├── scripts/                   # Run scripts
├── docs/                      # Generated website (GitHub Pages)
└── data/                      # Your preprocessed epochs (gitignored)
```

## Key Methods

**Component Detection:**
- Collapsed localizer with FWHM windowing (avoids circularity)
- ROI-based averaging (14 electrodes for N1)

**Statistics:**
- LMM-first approach (optimal for missing data)
- Complete reporting: LMM, ANOVA, pairwise comparisons

**Measurements:**
- Peak amplitude/latency (default)
- Fractional area latency (alternative)
- Peak-to-peak (P1-N1)

## Example Analyses

Browse [configs/analyses/](configs/analyses/) for ~80 pre-configured analyses:

- `increase_by_1.yaml` - Small transitions (1→2, 2→3)
- `from1_to_any.yaml` - All transitions from 1
- `landing_on_3_any_preceding.yaml` - All transitions ending at 3
- `cardinality_within_small.yaml` - Within PI range (1-3)
- `ALL_CONDITIONS_ACC0_ACC1.yaml` - Error vs. correct comparison

## Creating New Analyses

1. Copy an existing YAML: `cp configs/analyses/example.yaml configs/analyses/my_analysis.yaml`
2. Edit condition codes and output paths
3. Run: `python scripts/run_analysis.py --config configs/analyses/my_analysis.yaml`

See [methodology.md](methodology.md) for detailed documentation.

## Batch Processing

```bash
# Run all analyses
python scripts/run_all_analyses.py

# Run all statistics
python scripts/run_all_statistics.py

# Rebuild website
python scripts/rebuild_website_index.py
```

## Website Publishing

Enable GitHub Pages: Repository Settings → Pages → Source: `main` branch, `/docs` folder

Access at: `https://<username>.github.io/<repository>/`

## Citation

```
[Citation information will be added upon publication]
```

---

**Built with:** MNE-Python | **Statistics:** statsmodels + pingouin | **Powered by:** Python 3.12
