# Quickstart

1) Activate env: conda activate numbers-eeg\n2) Create a YAML under configs/analyses/ with:\n   - components: [P1, N1, P3b] to generate all three figures per run\n   - 
esponse: ALL | ACC1 where ACC1 filters metadata['Target.ACC'] == 1\n   - explicit include_groups listing the exact conditions used\n3) Run: python scripts/run_analysis.py --config configs/analyses/your-analysis.yaml\n4) Website output:\n   - Full pages: docs/analysis/<analysis_id>.md\n   - Figures (PNG, 300 DPI): docs/assets/plots/<analysis_id>/\n   - Thumbnails (for index grid): docs/assets/plots/<analysis_id>/thumbs/\n   - Tables (CSV): docs/assets/tables/<analysis_id>/\n   - Homepage grid: docs/index.md shows rows per analysis (alphabetical), with P1/N1/P3b thumbnails per row; clicking a thumb opens a full-size overlay. New analyses are inserted into the correct sorted position automatically.


