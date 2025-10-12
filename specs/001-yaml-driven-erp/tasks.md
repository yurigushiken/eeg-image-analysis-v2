# Tasks: YAML-Driven ERP Analysis v1 (Inc vs Dec)

**Input**: Design documents from `specs/001-yaml-driven-erp/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md

**Tests**: TDD required. Add unit/integration tests before implementation tasks; verify determinism and layout.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- Single project layout: `configs/`, `src/eeg/`, `scripts/`, `docs/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure needed by all user stories

- [X] T001 [P] Create directory structure: `configs/`, `configs/analyses/`, `src/eeg/`, `scripts/`, `docs/analysis/`, `docs/assets/plots/`, `docs/assets/tables/`
- [X] T002 [P] Ensure `environment.yml` for conda environment `eeg-image` (Python 3.12, mne==1.10.1, numpy, pandas, matplotlib, pyyaml, pytest) is present and pinned
- [X] T003 [P]  `.gitignore` exists.  additions to ensure `data/**` is ignored and only `docs/**` assets are committed
- [X] T004 [P] Create `configs/electrodes.yaml` defining ROI electrode mappings (N1_L, N1_R, P1, P3B)
- [X] T005 [P] Create `configs/components.yaml` defining component time windows (P1: 60-120ms, N1: 125-200ms, P3b: 300-600ms) and default ROI mappings

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core library modules that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Tests (TDD first)
- [X] T006 [P] Write unit tests for selection in `src/eeg/select.py` (ACC1 filter, explicit Condition sets, missing metadata errors)
- [X] T007 [P] Write unit tests for measures in `src/eeg/measures.py` (peak detection within windows, smoothing, LOPO fallback behavior)
- [X] T008 [P] Write unit tests for plotting in `src/eeg/plots.py` (ERP overlay present, topomap layout per FR-016A, fallback annotation visible)
- [X] T009 [P] Write smoke test for CLI on small sample YAML to assert deterministic CSV/PNG outputs (hash compare) and directory structure

- [X] T010 Implement `src/eeg/__init__.py` as package initializer
- [X] T011 Implement `src/eeg/config.py`: YAML schema loader/validator for AnalysisConfig (dataset, selection, components, preprocessing, roi, plots, outputs)
- [X] T012 Implement `src/eeg/io.py`: Functions to read Epochs from FIF files, enforce montage from `assets/net/AdultAverageNet128_v1.sfp`, validate sampling rate and channel count, extract subject IDs, and return scalp-only channel picks
- [X] T013 Implement `src/eeg/select.py`: Selection helpers (response: ALL vs ACC1 where ACC1 = Target.ACC==1), explicit numeric condition list filters, min_epochs_per_set validation
- [X] T014 Implement `src/eeg/erp.py`: Subject-level evoked computation, equal-weight grand averaging across subjects, SEM calculation, ROI aggregation with roi.min_channels threshold
- [X] T015 Implement `src/eeg/measures.py`: Component metrics functions (mean amplitude, peak amplitude, peak latency within windows) with optional smoothing
- [X] T016 Implement `src/eeg/plots.py`: ERP overlay plotting, peak detection (cohort/subject configurable), peak-locked topomaps, PNG output at plots.dpi, thumbnail generation; annotate plots when fallback window is used (legend/text/marker) per FR-016; enforce layout: ERP overlay on top row, per-condition topomaps below with labels "{condition} – Peak at {t} ms" per FR-016A
- [X] T017 Implement `src/eeg/report.py`: Functions to generate `docs/analysis/<analysis_id>.md` with embedded figures, CSV links, titles/subtitles from YAML; update `docs/index.md` grid with thumbnails and lightbox support
- [X] T018 Implement `scripts/run_analysis.py`: CLI entry point accepting `--config <yaml>` argument, orchestrating pipeline: load config → load data → select trials → compute ERPs → generate plots → write tables → generate reports

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Run Increasing vs Decreasing ERP from one YAML (Priority: P1) 🎯 MVP

**Goal**: From one YAML listing components [P1, N1, P3b], produce ERP overlays, topomaps, tables, and a published docs page

**Independent Test**: Provide `configs/analyses/small_increasing_vs_decreasing.yaml`; run `python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing.yaml`; verify `docs/analysis/small_increasing_vs_decreasing.md` exists with figures in `docs/assets/plots/small_increasing_vs_decreasing/` and tables in `docs/assets/tables/small_increasing_vs_decreasing/`

### Implementation for User Story 1

- [X] T101 [US1] Create sample YAML `configs/analyses/small_increasing_vs_decreasing.yaml` with:
  - dataset: {root: "data", pattern: "**/sub-*_epo.fif", montage_sfp: "assets/net/AdultAverageNet128_v1.sfp"}
  - selection:
      response: "ALL"
      min_epochs_per_set: 8
      condition_sets:
        - name: "Small_Increasing"   # increasing within small: 1..3
          conditions: ["12", "13", "23"]
        - name: "Small_Decreasing"   # decreasing within small: 3..1
          conditions: ["32", "31", "21"]
  - components: ["P1", "N1", "P3b"]
  - preprocessing: {baseline_ms: [-100, 0]}
  - roi: {min_channels: 4}
  - plots: {topomap_peak_window_ms: 50, peak_level: "cohort", smoothing: {method: "moving_average", window_ms: 10}, formats: ["png"], dpi: 300, thumb_width_px: 320, colors: ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33"], linestyles: {NC: "-", Decrease: ":", Increasing: "--"}}
  - outputs: {page: "single", plots_dir: "docs/assets/plots/small_increasing_vs_decreasing", tables_dir: "docs/assets/tables/small_increasing_vs_decreasing", page: "docs/analysis/small_increasing_vs_decreasing.md"}

- [X] T110 [US1] Create sample YAML `configs/analyses/cardinality_within_small.yaml` with:
  - dataset: {root: "data", pattern: "**/sub-*_epo.fif", montage_sfp: "assets/net/AdultAverageNet128_v1.sfp"}
  - selection:
      response: "ALL"
      min_epochs_per_set: 8
      condition_sets:
        - name: "Cardinality1"
          conditions: ["11"]
        - name: "Cardinality2"
          conditions: ["22"]
        - name: "Cardinality3"
          conditions: ["33"]
  - components: ["P1", "N1", "P3b"]
  - preprocessing: {baseline_ms: [-100, 0]}
  - roi: {min_channels: 4}
  - plots: {topomap_peak_window_ms: 50, peak_level: "cohort", smoothing: {method: "moving_average", window_ms: 10}, formats: ["png"], dpi: 300, thumb_width_px: 320}
  - outputs: {page: "single", plots_dir: "docs/assets/plots/cardinality_within_small", tables_dir: "docs/assets/tables/cardinality_within_small", page: "docs/analysis/cardinality_within_small.md"}
- [X] T102 [US1] Verify ACC1 vs ALL toggle: create alternate YAML with response: "ACC1" and confirm Target.ACC==1 filtering works
- [X] T103 [US1] Verify peak-locked topomaps render correctly with ±plots.topomap_peak_window_ms around detected peaks and that each topomap is labeled with condition and peak time per FR-016A
- [X] T104 [US1] Verify plot styling: palette assignment, linestyles (NC=solid, Decrease=dotted, Increasing=dashed)
- [X] T105 [US1] Verify titles/subtitles on figures include: analysis_id, response (ALL/ACC1), component (P1/N1/P3b), baseline window, ±topomap window, roi.min_channels, condition summary
- [X] T106 [US1] Verify `docs/index.md` grid shows one row for "erp_increasing_vs_decreasing" with P1/N1/P3b thumbnail columns; clicking thumbnail opens full-size PNG in lightbox overlay
- [X] T107 [US1] Run end-to-end on 24-subject dataset and verify completion within 10 minutes (Success Criterion SC-001)
 - [X] T108 [US1] Integration test: run sample YAML and assert figure layout (overlay + labeled topomaps), fallback annotations when applicable, and bit-identical assets on re-run

**Checkpoint**: At this point, User Story 1 should be fully functional and produce complete published analysis page

---

## Phase 4: User Story 2 - Reviewer regenerates results (Priority: P2)

**Goal**: A collaborator can clone the repo, activate the documented environment, and reproduce identical outputs using the YAML without touching code

**Independent Test**: Fresh repo clone; `conda activate eeg-image`; run same YAML from US1; verify outputs are identical (bit-identical CSVs/PNGs)

### Implementation for User Story 2

- [X] T201 [US2] Document exact reproduction steps in `specs/001-yaml-driven-erp/quickstart.md`:
  - Clone repo
  - `conda env create -f environment.yml`
  - `conda activate eeg-image`
  - `python scripts/run_analysis.py --config configs/analyses/erp_increasing_vs_decreasing.yaml`
  - Expected outputs listed
- [X] T202 [US2] Add deterministic settings to all randomized operations (set numpy random seed if any; document in config or code)
- [X] T204 [US2] Document expected output file paths in `specs/001-yaml-driven-erp/quickstart.md` (list generated CSVs/PNGs and locations)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently; reproducibility is validated

---

## Phase 5: User Story 3 - Website visitor views analysis page (Priority: P3)

**Goal**: A visitor can navigate to the project website and see the Small Increasing vs Small Decreasing ERP page with readable figures.

**Independent Test**: Serve `docs/` via GitHub Pages or local static server; load `https://<site>/analysis/small_increasing_vs_decreasing.html`; verify images render, links work, page loads quickly

### Implementation for User Story 3

- [ ] T301 [US3] Add minimal inline CSS/JS to `docs/index.md` for:
  - Responsive thumbnail grid (flexbox or grid layout)
  - Lightweight lightbox (click thumbnail → overlay with full PNG, close button, no external deps)
  - Ensure GitHub Pages compatibility (no build step required)
- [ ] T302 [US3] Add accessibility features to all generated pages:
  - Alt text for all images: "ERP overlay for {component} in {analysis_id}"
  - ARIA labels for lightbox controls
  - Semantic HTML headings (h1, h2, h3) in report.py template
- CSV table links have descriptive text: "Download {component} {set} metrics CSV"
- [ ] T303 [US3] Ensure `src/eeg/report.py` updates `docs/index.md` idempotently:
  - Alphabetical insertion by analysis_id (binary search for correct position)
  - No duplicate entries (check for existing analysis_id row, update in place)
  - Preserve manual edits outside auto-generated table region (use markers: `<!-- AUTO-GENERATED START -->` / `<!-- AUTO-GENERATED END -->`)
- [ ] T304 [US3] Verify page load performance on sample dataset:
  - All figures load without errors and render quickly on typical hardware
  - Largest PNG ≤ 2 MB (compress if needed via plots.dpi tuning)
  - Cumulative page weight ≤ 20 MB (verify sum of all assets)
- [ ] T305 [US3] Create `docs/index.md` initial template with:
  - Title: "EEG ERP Analyses"
  - Brief intro paragraph
  - Auto-generated table placeholder
  - Footer with links to GitHub repo and constitution

**Checkpoint**: All user stories should now be independently functional; website is publication-ready

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories or enhance robustness

- [ ] TX01 [P] Update root `README.md`:
  - Project overview
  - Link to constitution (`.specify/memory/constitution.md`)
  - Link to quickstart (`specs/001-yaml-driven-erp/quickstart.md`)
  - Link to published website (`docs/index.md` via GitHub Pages URL)
  - Environment setup instructions
  - CLI usage examples
- [ ] TX02 [P] Performance optimization: Implement streaming/batching for subject loading in `src/eeg/io.py` to avoid loading all epochs into memory simultaneously
- [ ] TX03 [P] QC reporting: Enhance `src/eeg/erp.py` and `report.py` to write `docs/assets/tables/<analysis_id>/qc_summary.csv` with:
  - Subject ID, set, included (yes/no), epoch_count, exclusion_reason (if any)
  - ROI availability per subject (channels available vs required)
- [ ] TX04 [P] Add baseline window validation in `src/eeg/io.py`: Check that preprocessing.baseline_ms falls within epoch time range; raise actionable error if not (e.g., "Baseline [-100, 0] ms outside epoch range [-200, 496] ms")
- [ ] TX05 [P] Add montage enforcement error handling in `src/eeg/io.py`: On montage application failure, list unmatched channel labels and montage path in error message (FR-019)
- [ ] TX06 [P] Create optional JSON schema document `specs/001-yaml-driven-erp/contracts/analysis-config-schema.json` for YAML validation (references FR-001 through FR-027)
- [ ] TX07 [P] Add peak detection fallback in `src/eeg/measures.py`: If peak not found (flat/noisy signal), fall back to component window center; log warning; mark in QC; ensure plot annotation hook is triggered
- [ ] TX08 [P] Add edge case handling for missing metadata columns: In `src/eeg/select.py`, validate required columns exist; raise error listing missing columns (e.g., "Required metadata columns missing: ['Condition', 'direction', 'Target.ACC']")
- [ ] TX09 [P] Add edge case handling for empty condition sets: In `src/eeg/erp.py` and `report.py`, detect sets with zero subjects meeting threshold; suppress plots; add note to analysis page: "Set {name}: No subjects met inclusion criteria (min_epochs_per_set={N})"
- [ ] TX10 [P] Create example YAML `configs/analyses/erp_from1_to_any.yaml` demonstrating alternate analysis (e.g., trials starting from "1" to any other number) to verify reusability
- [ ] TX11 Run end-to-end quickstart validation: Execute all commands in `specs/001-yaml-driven-erp/quickstart.md` on a clean environment; verify outputs match expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion (T001-T005) - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion (T010-T018)
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories - **This is the MVP**
- **User Story 2 (P2)**: Can start after US1 completion (needs baseline outputs from T107) - Validates US1 reproducibility
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Enhances US1 website output but independent

### Within Each User Story

- Setup → Foundational → User Story implementation
- YAML creation before end-to-end verification
- Core features before edge cases
- Functionality before performance/polish

### Parallel Opportunities

- All Setup tasks (T001-T005) marked [P] can run in parallel
- All Foundational tasks (T010-T018) can run in parallel if different developers work on different modules
- Within US1: T102-T106 can run in parallel after T101 completes
- Within US2: T201-T204 can run in parallel
- Within US3: T301-T305 can run in parallel
- All Polish tasks (TX01-TX10) marked [P] can run in parallel

---

## Parallel Example: Foundational Phase (Phase 2)

```bash
# If you have multiple developers, launch foundational modules in parallel:
# Developer A:
Task: "Implement src/eeg/__init__.py, src/eeg/config.py, src/eeg/io.py"

# Developer B:
Task: "Implement src/eeg/select.py, src/eeg/erp.py"

# Developer C:
Task: "Implement src/eeg/measures.py, src/eeg/plots.py"

# Developer D:
Task: "Implement src/eeg/report.py, scripts/run_analysis.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005)
2. Complete Phase 2: Foundational (T010-T018) - **CRITICAL - blocks all stories**
3. Complete Phase 3: User Story 1 (T101-T107)
4. **STOP and VALIDATE**: Run end-to-end on 24-subject dataset; verify figures, tables, docs page
5. Publish `docs/` to GitHub Pages; demo analysis page to stakeholders
6. **You now have a working MVP!**

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → **Deploy/Demo (MVP! Publish to GitHub Pages)**
3. Add User Story 2 → Test independently → Validate reproducibility → **Confidence in scientific rigor**
4. Add User Story 3 → Test independently → **Public-facing website polish complete**
5. Add Polish tasks → Performance, robustness, edge cases → **Production-ready**

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup (Phase 1) together (5 tasks, ~1 hour)
2. Team completes Foundational (Phase 2) in parallel by module (see parallel example above)
3. Once Foundational is done:
   - Developer A: User Story 1 (T101-T107) - **Priority! This is MVP**
   - Developer B: User Story 3 (T301-T305) - Can work in parallel with US1
   - After US1 complete:
     - Developer C: User Story 2 (T201-T204) - Validates US1
4. All developers: Polish tasks (TX01-TX11) in parallel

---

## Notes

- [P] tasks = different files/modules, no dependencies, can run in parallel
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- **No tests explicitly requested** - focus on implementation quality and constitution compliance
- Commit after each task or logical group (e.g., commit after completing each module in Foundational phase)
- Stop at any checkpoint to validate story independently
- Constitution gates enforced: Reproducible env (environment.yml), YAML-driven (no ad-hoc scripts), docs-only commits (data/ ignored)
- Success criteria tracked: SC-001 (10-min runtime), SC-002 (reproducibility), SC-004 (page performance)

---

## Task Count Summary

- **Phase 1 (Setup)**: 5 tasks
- **Phase 2 (Foundational)**: 13 tasks
- **Phase 3 (User Story 1 - MVP)**: 8 tasks
- **Phase 4 (User Story 2)**: 3 tasks
- **Phase 5 (User Story 3)**: 5 tasks
- **Phase 6 (Polish)**: 11 tasks
- **Total**: 45 tasks

**MVP Scope** (Minimum for first working version): Phase 1 + Phase 2 + Phase 3 = 21 tasks
