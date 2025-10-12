# Quickstart

0) Clone the repository
- `git clone https://github.com/<org>/eeg-image-analysis-v2.git`
- `cd eeg-image-analysis-v2`

1) Activate environment
- `conda env create -f environment.yml`
- `conda activate eeg-image`

2) Create a YAML under `configs/analyses/` with:
- `components: [P1, N1, P3b]` to generate all three figures per run
- `response: ALL | ACC1` where ACC1 filters `metadata['Target.ACC'] == 1`
- `condition_sets`: define named sets using numeric Condition codes (e.g., `conditions: ["12", "13"]`)

3) Run the pipeline (deterministic)
- ALL responses:
  - `python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing.yaml`
- ACC1 responses only:
  - `python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing_ACC1.yaml`
- Note: the CLI seeds NumPy for deterministic outputs; reruns should produce bit-identical PNGs.

4) Website output
- Full page: `docs/analysis/<analysis_id>.md`
- Figures (PNG, 300 DPI): `docs/assets/plots/<analysis_id>/` (composite images; overlay + topomaps)
- Tables (CSV): `docs/assets/tables/<analysis_id>/`
- Homepage grid: `docs/index.md` shows rows per analysis (alphabetical), with P1/N1/P3b thumbnails generated via CSS scaling (no separate files). Clicking a thumb opens a full-size overlay (accessible lightbox). New analyses insert in sorted order automatically.

5) Expected outputs (US1 example)
- Page:
  - `docs/analysis/small_increasing_vs_decreasing.md`
- Plots (composite images):
  - `docs/assets/plots/small_increasing_vs_decreasing/P1.png`
  - `docs/assets/plots/small_increasing_vs_decreasing/N1.png`
  - `docs/assets/plots/small_increasing_vs_decreasing/P3b.png`
- Index updated row with thumbnails/lightbox:
  - `docs/index.md`
- Tables (CSV; if enabled in future steps):
  - `docs/assets/tables/small_increasing_vs_decreasing/*.csv`
