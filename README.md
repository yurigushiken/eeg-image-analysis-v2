EEG Image Analysis – Data Overview and Usage

- Python: `3.12`
- Recommended env: `conda activate eeg-image`

If `conda` is not available on your PATH, you can still run the scripts with any Python 3.12 environment that has `mne`, `pandas`, `numpy`, and `matplotlib` installed.

Project structure
- Data: `data/hpf_1.5_lpf_35_baseline-on/` contains 24 preprocessed epoch FIF files (e.g., `sub-02_preprocessed-epo.fif`).
- Scripts: helper utilities to summarize and plot the data.
- Outputs: generated summaries and figures.

Quick start
1) Activate the environment
   - `conda activate numbers-eeg`

2) Summarize the dataset
   - `python scripts/summarize_epochs.py`
   - Writes `outputs/data_summary.csv`, `outputs/data_summary.json`, and `outputs/aggregates.json`.

3) Generate example plots (first few subjects)
   - `python scripts/plot_evoked.py`
   - Saves evoked overlays and sensor layout PNGs to `outputs/plots/`.

What’s in the data
This repository contains MNE-Python Epochs files (`*-epo.fif`). Each file represents one subject’s epoched EEG:
- Typical shape: `n_epochs x n_channels x n_times`
- Example (all 24 files are consistent):
  - `n_epochs ≈ 270`
  - `n_channels ≈ 129`
  - Sampling frequency `sfreq = 250 Hz`
  - Epoch duration `~0.696 s`

Epoch metadata columns
Each epochs file includes a `metadata` table with the following columns (present in all 24 files):
- `SubjectID` – participant identifier
- `Block` – experimental block index
- `Trial` – trial index within the block
- `Procedure` – task phase label (values observed: `BlockProc`, `BlockProc2`, `BlockProc3`, `BlockProc4`, `BlockProc5`)
- `Condition` – condition code for the trial (observed string codes: `11,12,13,14,21,22,23,24,25,31,32,33,34,35,36,41,42,43,44,45,46,52,53,54,55,56,63,64,65,66`)
- `Target.ACC` – target response accuracy (if present in the task design)
- `Target.RT` – target response time (ms)
- `Trial_Continuous` – continuous trial index across blocks
- `direction` – condition feature (values: `D`, `I`, `NC`)
- `change_group` – combined change category (values: `NC`, `dLL`, `dLS`, `dSS`, `iLL`, `iSL`, `iSS`)
- `size` – size-related feature (values: `LL`, `SS`, `cross`, `NC`)

Events and conditions
- The `event_id` mapping embedded in each epochs file contains 30 event labels named as numeric strings: `"0"` through `"29"`.
- These are valid for averaging/plotting in MNE, e.g. `epochs['0'].average()`.
- The metadata’s `Condition`, `direction`, `change_group`, and `size` provide human-readable descriptors of trials. If desired, we can remap the numeric event names to descriptive labels derived from these columns for clearer figures and group analyses.

Generated outputs
- Summary CSV/JSON: `outputs/data_summary.csv`, `outputs/data_summary.json` (one row per file), and `outputs/aggregates.json` (dataset-wide presence of metadata columns and event labels).
- Example figures: under `outputs/plots/`, for the first few subjects we save evoked overlays per event and a sensor layout PNG.

Scripts
- `scripts/summarize_epochs.py` – iterates all `*-epo.fif` under `data/`, extracts file-level stats, metadata columns, and event keys, and writes artifacts to `outputs/`.
- `scripts/plot_evoked.py` – produces evoked response plots per event for a few subjects and a channel layout plot; uses a non-interactive backend for headless runs.

Mentor notes (understanding the objects)
- MNE Epochs: an `Epochs` object holds many trials with aligned time windows relative to an event of interest. It includes:
  - `data`: the signal array per trial
  - `info`: measurement metadata (channel names/types, sampling rate, etc.)
  - `events`/`event_id`: numeric-coded events and a mapping of labels to event codes
  - `metadata`: a Pandas DataFrame of trial-wise descriptors (the “columns” described above)
- Typical analysis patterns:
  - Select trials by label: `epochs['22']` or by metadata query: `epochs[epochs.metadata['direction'] == 'I']`
  - Average to get ERPs/ERFs: `epochs['22'].average()`; compare conditions by overlaying evokeds
  - Time-frequency or decoding can build on these same selections

Next steps (optional)
- Map numeric event labels ("0"–"29") to descriptive names using combinations of `Condition`, `direction`, `change_group`, and `size` for clearer figures.
- Add group-level plots (e.g., grand averages across subjects) and basic QC (channel type counts, bad channels, etc.).

Website
- GitHub Pages serves from /docs
- Homepage (docs/index.md) shows a grid of analysis thumbnails:
  - Rows are analysis_id (alphabetical)
  - Columns per row are P1, N1, P3b thumbnails when present
  - Clicking a thumbnail opens a full-size overlay (lightbox)
- Figures are PNG at high DPI (configurable); thumbnails are smaller copies
- Each figure has a title (analysis id, response, component) and a subtitle (baseline, �peak window, ROI rule, condition summary)
