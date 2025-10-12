---
layout: default
title: EEG ERP Analyses
---

# EEG ERP Analyses

Welcome to the **EEG ERP Analysis Pipeline** - a YAML-driven, reproducible system for analyzing event-related potentials.

## Analysis Gallery

Click any thumbnail to view the full-size ERP plot with topographic maps.

<!-- AUTO-GENERATED START -->
<table class="grid-table">
<thead>
  <tr><th>Analysis</th><th>P1</th><th>N1</th><th>P3b</th></tr>
</thead>
<tbody>
<tr><td>erp_from1_to_any</td><td><a href='assets/plots/erp_from1_to_any/P1.png' data-lightbox aria-label='ERP overlay for P1 in erp_from1_to_any'><img class='thumb' src='assets/plots/erp_from1_to_any/P1.png' alt='ERP overlay for P1 in erp_from1_to_any' /></a></td><td><a href='assets/plots/erp_from1_to_any/N1.png' data-lightbox aria-label='ERP overlay for N1 in erp_from1_to_any'><img class='thumb' src='assets/plots/erp_from1_to_any/N1.png' alt='ERP overlay for N1 in erp_from1_to_any' /></a></td><td><a href='assets/plots/erp_from1_to_any/P3b.png' data-lightbox aria-label='ERP overlay for P3b in erp_from1_to_any'><img class='thumb' src='assets/plots/erp_from1_to_any/P3b.png' alt='ERP overlay for P3b in erp_from1_to_any' /></a></td></tr>
<tr><td>sample_smoke</td><td><a href='assets/plots/sample_smoke/P1_overlay.png' data-lightbox aria-label='ERP overlay for P1 in sample_smoke'><img class='thumb' src='assets/plots/sample_smoke/P1_overlay.png' alt='ERP overlay for P1 in sample_smoke' /></a></td><td></td><td></td></tr>
<tr><td>small_increasing_vs_decreasing</td><td><a href='assets/plots/small_increasing_vs_decreasing/P1.png' data-lightbox aria-label='ERP overlay for P1 in small_increasing_vs_decreasing'><img class='thumb' src='assets/plots/small_increasing_vs_decreasing/P1.png' alt='ERP overlay for P1 in small_increasing_vs_decreasing' /></a></td><td><a href='assets/plots/small_increasing_vs_decreasing/N1.png' data-lightbox aria-label='ERP overlay for N1 in small_increasing_vs_decreasing'><img class='thumb' src='assets/plots/small_increasing_vs_decreasing/N1.png' alt='ERP overlay for N1 in small_increasing_vs_decreasing' /></a></td><td><a href='assets/plots/small_increasing_vs_decreasing/P3b.png' data-lightbox aria-label='ERP overlay for P3b in small_increasing_vs_decreasing'><img class='thumb' src='assets/plots/small_increasing_vs_decreasing/P3b.png' alt='ERP overlay for P3b in small_increasing_vs_decreasing' /></a></td></tr>
<tr><td>small_increasing_vs_decreasing_ACC1</td><td><a href='assets/plots/small_increasing_vs_decreasing_ACC1/P1.png' data-lightbox aria-label='ERP overlay for P1 in small_increasing_vs_decreasing_ACC1'><img class='thumb' src='assets/plots/small_increasing_vs_decreasing_ACC1/P1.png' alt='ERP overlay for P1 in small_increasing_vs_decreasing_ACC1' /></a></td><td><a href='assets/plots/small_increasing_vs_decreasing_ACC1/N1.png' data-lightbox aria-label='ERP overlay for N1 in small_increasing_vs_decreasing_ACC1'><img class='thumb' src='assets/plots/small_increasing_vs_decreasing_ACC1/N1.png' alt='ERP overlay for N1 in small_increasing_vs_decreasing_ACC1' /></a></td><td><a href='assets/plots/small_increasing_vs_decreasing_ACC1/P3b.png' data-lightbox aria-label='ERP overlay for P3b in small_increasing_vs_decreasing_ACC1'><img class='thumb' src='assets/plots/small_increasing_vs_decreasing_ACC1/P3b.png' alt='ERP overlay for P3b in small_increasing_vs_decreasing_ACC1' /></a></td></tr>
</tbody>
</table>
<!-- AUTO-GENERATED END -->

## About This Pipeline

This analysis pipeline is:
- **YAML-driven**: Configure analyses via simple YAML files
- **Reproducible**: Deterministic outputs with pinned dependencies
- **Publication-ready**: High-DPI figures and CSV tables
- **Automated**: Run analysis → push to GitHub → website updates automatically

### Documentation

- [GitHub Repository](https://github.com/yurigushiken/eeg-image-analysis-v2)
- [Project README](https://github.com/yurigushiken/eeg-image-analysis-v2/blob/main/README.md)
- [Constitution (Project Principles)](https://github.com/yurigushiken/eeg-image-analysis-v2/blob/main/.specify/memory/constitution.md)
- [Feature Specification](https://github.com/yurigushiken/eeg-image-analysis-v2/blob/main/specs/001-yaml-driven-erp/spec.md)

### Quick Start

```bash
# Clone and setup
git clone https://github.com/yurigushiken/eeg-image-analysis-v2.git
cd eeg-image-analysis-v2
conda env create -f environment.yml
conda activate eeg-image

# Run analysis
python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing.yaml

# Push to GitHub - website updates automatically!
git add docs/
git commit -m "Add new analysis results"
git push
```
