# Quickstart

1) Activate environment
- `conda env create -f environment.yml`
- `conda activate eeg-image`

2) Create a YAML under `configs/analyses/` with:
- `components: [P1, N1, P3b]` to generate all three figures per run
- `response: ALL | ACC1` where ACC1 filters `metadata['Target.ACC'] == 1`
- `condition_sets`: define named sets using numeric Condition codes (e.g., `conditions: ["12", "13"]`)

3) Run the pipeline
- `python scripts/run_analysis.py --config configs/analyses/your-analysis.yaml`

4) Website output
- Full page: `docs/analysis/<analysis_id>.md`
- Figures (PNG, 300 DPI): `docs/assets/plots/<analysis_id>/`
- Thumbnails: `docs/assets/plots/<analysis_id>/thumbs/`
- Tables (CSV): `docs/assets/tables/<analysis_id>/`
- Homepage grid: `docs/index.md` shows rows per analysis (alphabetical), with P1/N1/P3b thumbnails; clicking a thumb opens a full-size overlay. New analyses insert in sorted order automatically.

5) Expected outputs (US1 example)
- `docs/analysis/erp_increasing_vs_decreasing.md`
- `docs/assets/plots/erp_increasing_vs_decreasing/*.png`
- `docs/assets/tables/erp_increasing_vs_decreasing/*.csv`
