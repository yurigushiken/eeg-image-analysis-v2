# Implementation Plan: YAML-Driven ERP Analysis v1 (Inc vs Dec)

**Branch**: 001-yaml-driven-erp | **Date**: 2025-10-11 | **Spec**: specs/001-yaml-driven-erp/spec.md
**Input**: Feature specification from specs/001-yaml-driven-erp/spec.md

## Summary

Deliver a YAML-driven ERP pipeline that:
- Loads subject Epochs, enforces the AdultAverageNet128_v1 montage, and selects trials by metadata.
- Computes P1, N1, and P3b in one run when listed in the YAML (components: ["P1","N1","P3b"]).
- Supports response filtering: response: ALL | ACC1 (ACC1 means Target.ACC == 1).
- Uses explicit numeric condition lists per analysis YAML (no shared global conditions file).
- Produces PNG figures and CSV tables under docs/ and renders a single analysis page by default.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: mne==1.10.1, numpy, pandas, matplotlib (Agg)  
**Storage**: Local files; raw FIF in data/ (ignored), published assets in docs/  
**Testing**: pytest (unit on selection/metrics; smoke on small sample)  
**Target Platform**: Local Python; GitHub Pages for docs  
**Project Type**: Single repo, library + CLI  
**Performance Goals**: End-to-end on 24 subjects = 10 minutes; memory bounded by per-subject processing  
**Constraints**: Reproducible env (eeg-image), YAML-driven, commit only docs assets  
**Scale/Scope**: 24±100 subjects; three core components (P1, N1, P3b)

## Constitution Check

Gates from constitution and status:
- Reproducible Environment: environment.yml present and pinned; CLI documented. PASS.
- Data Governance: Raw data ignored; only docs committed. PASS.
- Declarative Analyses: YAML config as contract. PASS.
- ERP Standards/ROIs: Component windows + ROIs; montage enforced. PASS.
- Documentation as Artifact: Writes docs/analysis page + assets. PASS.

## Project Structure

### Documentation (this feature)

```
specs/001-yaml-driven-erp/
+- plan.md
+- research.md
+- data-model.md
+- quickstart.md
+- contracts/
```

### Source Code (repository root)

```
configs/
+- electrodes.yaml
+- components.yaml
+- analyses/
   +- erp_increasing_vs_decreasing.yaml
   +- erp_from1_to_any.yaml

src/eeg/
+- __init__.py
+- config.py        # load/validate YAML
+- io.py            # epochs I/O, montage, subject id
+- select.py        # metadata filters (incl. Target.ACC)
+- erp.py           # evokeds, grand averages, SEM
+- measures.py      # mean/peak amplitude, latency
+- plots.py         # overlays, topomaps (PNG)
+- report.py        # docs page renderer

scripts/
+- run_analysis.py  # CLI: python scripts/run_analysis.py --config <yaml>

docs/
+- analysis/
+- assets/
   +- plots/<analysis_id>/
   +- tables/<analysis_id>/
```

**Structure Decision**: Single-project layout with src/eeg library + CLI, YAML in configs/**, and published site in docs/**.

## Design Details

YAML keys capturing requirements:
- dataset: {root, pattern, montage_sfp}
- selection:
  - response: ALL | ACC1  # ACC1 filters metadata Target.ACC == 1
  - min_epochs_per_set: 8
  - condition_sets: [{name, conditions: ["12", "13"]}]  # explicit numeric condition codes per set
- components: ["P1","N1","P3b"]
- preprocessing: {baseline_ms: [-100, 0]}
- roi: {min_channels: 4}
- plots:
  - topomap_peak_window_ms: 50     # ±50 ms around detected peak
  - peak_level: cohort|subject     # default cohort (aggregate across condition sets)
  - smoothing: {method: moving_average, window_ms: 10}
  - formats: [png]
  - dpi: 300
  - thumb_width_px: 320
  - colors: ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33"]
  - linestyles:
      NC: "-"           # No Change (cardinality; e.g., 11, 22, 33, 44, 55, 66)
      Decrease: ":"
      Increasing: "--"
- outputs: {page: single|by_component, plots_dir, tables_dir, page}

Website generation:
- docs/index.md is generated/updated to show a grid of thumbnails organized by
  analysis_id (alphabetical). Each row shows P1/N1/P3b thumbnails from the same
  YAML when present. Clicking a thumbnail opens a full‑size overlay (lightbox)
  using a small inline JS/CSS snippet compatible with GitHub Pages. New
  analyses insert into the correct sorted position idempotently.

Subject/condition-set logic:
- Apply response filter before selection; condition sets are explicit numeric condition lists.
- Equal-weight subject grand averages; SEM across subjects.
- Exclude subjects per-set if epochs < min threshold after filtering.

Topomap/peaks:
- Peaks within component window (N1 min; P1/P3b max); topomaps average amplitude over ±plots.topomap_peak_window_ms around the peak.
- Peak level configurable (cohort default); optional smoothing before detection.

## Milestones & Tasks

Phase 0 (Research)
- Confirm YAML schema + minimal example YAMLs.
- Validate ACC1 filtering using metadata Target.ACC on a sample.

Phase 1 (Design & Contracts)
- data-model.md: AnalysisConfig, ConditionSet, Component, ROI, SubjectResult, ConditionSetResult.
- contracts/: Document YAML schema (markdown/JSON schema excerpt).
- quickstart.md: End-to-end instructions (conda activate eeg-image; run CLI).

Phase 2 (Implementation outline)
- config.py schema + validation; load electrodes/components defaults.
- io.py read epochs; enforce montage; scalp picks; subject id; response filter.
- select.py apply explicit condition lists + metadata query helpers.
- erp.py subject evokeds, grand average, SEM, ROI aggregation per component.
- measures.py mean/peak amplitude + latency per component window.
- plots.py ERP overlays and peak-locked topomaps as PNG; composite figures (overlay + per-condition topomaps) with peak markers.
- report.py analysis page under docs/analysis/ and index grid generator that
  maintains docs/index.md with CSS thumbnails + lightbox (no separate thumb files).
- run_analysis.py CLI wiring + argument validation.

## Acceptance Criteria
- One YAML listing components [P1,N1,P3b] produces 3 distinct ERP overlays and topomaps saved as PNG.
- response: ACC1 filters Target.ACC == 1; ALL uses all data.
- Each analysis YAML explicitly lists condition codes used for its condition sets.
- docs/analysis/<analysis_id>.md generated; assets under docs/assets/plots|tables/<analysis_id>/.
- Reproducible run in = 10 minutes on 24 subjects.





