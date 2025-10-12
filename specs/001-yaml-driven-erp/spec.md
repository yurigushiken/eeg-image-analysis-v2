# Feature Specification: YAML‑Driven ERP Analysis v1 (Inc vs Dec)

**Feature Branch**: 001-yaml-driven-erp  
**Created**: 2025-10-11  
**Status**: Draft  
**Input**: User description: "YAML-driven ERP analysis pipeline that selects trials via metadata (direction, change_set, size), computes N1/P1/P3b ERPs over predefined ROIs, saves plots+tables to docs for GitHub Pages, and is configured via reusable YAML files."

## Clarifications

### Session 2025-10-11

- Q: How should we form set-level ERPs across subjects? (A equal-weight subject grand average; B epoch pooling; C weighted by epoch count) 
  A: A) Subject-level first, then equal-weight grand average; SEM across subjects.

- Q: Minimum valid epochs per subject per condition set for inclusion? (A none; B 20; C 30; D configurable)
  A: D) Configurable via YAML with default 8 epochs.
 
- Q: Baseline correction strategy? (A −100–0 ms; B whole epoch; C none; D configurable)
  A: D) Configurable via YAML with default -100 to 0 ms. Epochs span approximately -200 to 496 ms, so the default is valid.

- Q: ROI handling when some channels are missing? (A require all ROI channels; B allow partial ROI with min count; C interpolate missing)
  A: B) Allow partial ROI with a configurable minimum required channels; default 4.

- Q: Peak detection level for topomap anchoring? (A aggregate grand-average; B per-subject; C configurable)
  A: C) Configurable via YAML with default A (cohort-level peak); subject-level
  optional when deeper variability analysis is desired.

- Q: Smoothing before peak detection? (A none; B 10 ms moving average; C LPF 20 Hz; D configurable)
  A: D) Configurable via YAML with default simple moving average over 10 ms.

- Q: Enforce montage/channel mapping to E-codes via SFP? (A hard fail on mismatch; B warn and continue; C configurable)
  A: A) Enforce mapping using assets/net/AdultAverageNet128_v1.sfp; fail if labels cannot be mapped. All data now and future uses this net.

- Q: Default ROIs per component? (A N1: L, R, and combined; P1: P1; P3b: P3B; B N1 combined only; C configurable)
  A: C) Configurable via YAML with defaults as in A.

- Q: Publishing structure and formats? (A single page per analysis; B one page per component; C configurable)
  A: C) Configurable via YAML with default A (single analysis page). Figures are
  PNG only for the website; tables are CSV.

- Q: Plot styling (palette + linestyles)?
  A: Use a shared categorical palette; each plot consumes as many as needed:
    ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33"].
    Linestyles: No Change = solid; Decrease = dotted; Increasing = dashed.

- Q: Website organization for published plots?
  A: Main index shows rows per analysis (alphabetical by analysis_id). Each row
  displays P1, N1, P3b thumbnails from the same YAML (when present). Clicking a
  thumbnail opens a full‑size overlay (lightbox). New analyses insert in order.

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Plot ERP overlays from named condition sets (Priority: P1)

An analyst can point the CLI to a single YAML file that defines dataset
location, ROIs, components (P1, N1, P3b), and multiple named condition sets
specified as explicit numeric Condition codes (e.g., "12", "13"). The run
produces ERP overlays and ROI metrics for each set, and writes a Markdown page
and figures to docs/ for publishing.

**Why this priority**: Unlocks the minimal end‑to‑end value: a reproducible
first analysis published on the website.

**Independent Test**: Provide the sample YAML; run the CLI; verify figures and
tables are produced and the docs page exists with correct links.

**Acceptance Scenarios**:

1. **Given** a valid YAML that defines condition sets via explicit numeric
   Condition codes (e.g., conditions: ["12", "13", "23"] vs ["32", "31", "21"]),
   **When** the CLI runs, **Then** it saves evoked overlays with SEM and ROI
   time‑courses to docs/assets/plots/erp/increasing_vs_decreasing/ and a page
   under docs/analysis/.
2. **Given** the same YAML on a clean machine with the declared environment,
   **When** the CLI runs, **Then** outputs are identical and the page builds under
   GitHub Pages.

---

### User Story 2 - Reviewer regenerates results (Priority: P2)

A collaborator can clone the repo, activate the documented environment, and
reproduce the same outputs using the YAML without touching code.

**Why this priority**: Ensures reproducibility and trust for publication.

**Independent Test**: Fresh checkout; run the CLI with the same YAML; diff
docs/assets vs baseline.

**Acceptance Scenarios**:

1. **Given** the repo and environment, **When** the reviewer runs the provided
   command, **Then** the generated CSVs and PNGs are bit-identical to baseline
   (no tolerance).

---

### User Story 3 - Website visitor views analysis page (Priority: P3)

A visitor can navigate to the project website and see the Increasing vs
Decreasing ERP page with readable figures and a short methods summary.

**Why this priority**: Communicates results to the public and stakeholders.

**Independent Test**: After publishing, load the page URL; verify images render
and tables link to CSVs.

**Acceptance Scenarios**:

1. **Given** the published site served via localhost static server or GitHub Pages, **When** the visitor opens the analysis page,
   **Then** all figures load without errors and links to CSVs download successfully.

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right edge cases.
-->

- Missing metadata columns (Condition, Target.ACC if response=ACC1): run aborts with a clear message listing missing columns.
- Montage mapping failure: abort with a clear error listing unmatched channels and the montage path. If montage applies but ROI electrodes are partially missing, use the partial-ROI rule (roi.min_channels) and record in QC.
- No epochs matching a set filter: set is marked empty; plots suppressed; page still renders with a note.
- Files unreadable/corrupt: skip subject; record in QC; proceed with others.
- Output directories absent: created automatically.
- Subject below min_epochs_per_set: exclude from that set; include in QC with counts; keep subject for other sets where threshold is met.
- Baseline window outside available epoch range: abort with a message stating provided window and valid range (e.g., ~-200 to 496 ms).
- ROI has fewer than roi.min_channels available electrodes: exclude that subject from that ROI's metrics; continue with others; report in QC.
- Peak not found (flat/noisy signal): fall back to component window center and mark the case in QC; skip peak-locked topomap for that subject if necessary.

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: The feature MUST accept a YAML config defining dataset root,
  file pattern, montage path, components (time windows), ROIs (electrode
  labels), condition sets (explicit numeric Condition lists), plotting options, and output paths.
- **FR-002**: The system MUST load each subject’s Epochs, apply baseline
  correction (−100 to 0 ms), and compute condition‑wise evokeds per condition set.
- **FR-003**: The system MUST compute ROI time‑course averages and component
  metrics: mean amplitude, peak amplitude, and peak latency within windows.
- **FR-004**: The system MUST write subject‑level metrics CSVs and set‑level
  summary CSVs and figures (PNG) to the configured output directories.
- **FR-005**: The system MUST generate a Markdown analysis page that embeds
  figures, links CSVs, and records the YAML used.
- **FR-006**: The system MUST support declarative selection via explicit numeric Condition lists organized into named condition sets under `selection.condition_sets[]`.
  - Scope of this feature (v1): analyses use explicit two‑digit `Condition` codes (e.g., ["12","13"]).
  - Library capability: metadata‑derived filters (e.g., `direction == "I"`) are supported but considered optional patterns, not used by this feature’s YAMLs.
- **FR-007**: The system MUST validate prerequisites (required metadata
  columns, sampling rate, channel count) and fail with actionable messages.
- **FR-008**: The system MUST support the AdultAverageNet128_v1.sfp montage
  for channel locations when plotting.
- **FR-009**: The system MUST not modify raw data and MUST write only to
  docs/** and local data/outputs/**.
- **FR-010**: The CLI MUST run as python scripts/run_analysis.py --config <yaml>.
 - **FR-011**: set-level ERPs MUST be computed by first averaging within each
   subject to form subject evokeds, then taking an equal-weight mean across
   subjects. Shaded uncertainty reflects SEM across subjects. Subject-pooling of
   epochs across participants is not permitted.
- **FR-012**: Subject inclusion per condition set MUST require at least a configurable
   minimum number of valid epochs (YAML: selection.min_epochs_per_set; default
   8). Subjects below threshold for a given set are excluded from that set's
   averages and are listed in a QC table.
 - **FR-013**: Baseline correction MUST be configurable via YAML
   (preprocessing.baseline_ms: [start, end] ms relative to event) with default
   [-100, 0]. The runner MUST validate that the baseline window lies within
   each subject's epoch time range; otherwise fail with an actionable message.
 - **FR-014**: ROI aggregation MUST allow partial ROIs when some electrodes are
   unavailable; require at least a configurable minimum channel count per ROI
   (YAML: roi.min_channels; default 4). If a subject fails this threshold for
   a ROI, exclude that subject from that ROI's metrics and record in QC.
 - **FR-015**: Only scalp EEG channels MUST be used for ERP and topographic
   plots. Non‑scalp channels (EOG/ECG/EMG/STIM/MISC) are excluded by default,
   as ROIs are explicitly defined by electrode labels.
 - **FR-016**: The system MUST detect component peaks within the component time
   window (e.g., N1: local minimum; P1/P3b: local maximum). Topographic plots
   MUST summarize the mean amplitude over a symmetric window around the
   detected peak, with half‑width configurable in YAML (key:
   plots.topomap_peak_window_ms, default 50 meaning ±50 ms). Figure styling
   should mirror temp/example.py where applicable while following these
   constraints.
  - If no valid peak is found and the fallback (component window center) is used,
    the affected plots MUST include a clear on-figure annotation indicating
    the fallback (e.g., a label "fallback window" and/or an asterisk in the legend)
    and the case MUST be recorded in QC.
 - **FR-016A (Figure layout)**: Each component figure MUST place the ERP overlay panel on the top row and a row of per-condition topomap panels beneath it. Each topomap panel MUST include a visible label with the condition name (from YAML) and the detected peak time in ms (e.g., "From 3 – Peak at 108 ms").
 - **FR-017**: Peak detection level MUST be configurable via YAML
  (plots.peak_level: 'cohort'|'subject', default 'cohort').
   - If 'cohort': detect the peak on the aggregate grand-average and compute
     topomaps using the ±window around that time for all subjects.
   - If 'subject': detect peaks per subject; compute each subject's topomap
     over its own ±window; set topomap is the mean of subject topomaps.

 - **FR-018**: Smoothing prior to peak detection MUST be configurable via YAML
   (e.g., plots.smoothing: {method: 'moving_average', window_ms: 10}) with
   default method 'moving_average' and window_ms: 10. Setting method: 'none'
   disables smoothing.
- **FR-019**: Montage mapping is REQUIRED prior to ROI selection and plotting. The config MUST provide dataset.montage_sfp (default assets/net/AdultAverageNet128_v1.sfp). If the montage cannot be applied or any channel labels cannot be mapped to E-coded names expected by the montage, the run MUST fail with an actionable error listing the unmatched labels.
 - **FR-020**: Component-to-ROI defaults MUST be configurable via YAML. Provide keys like components.N1.rois, components.P1.rois, components.P3b.rois. The default mapping is: N1 -> [N1_L, N1_R, N1_bilateral]; P1 -> [P1]; P3b -> [P3B]. If N1_bilateral is not defined in electrodes.yaml, compute it as the union of N1_L and N1_R (unique channels) and average across that set.
 - **FR-021**: Publishing layout MUST be configurable via YAML (outputs.page:
   'single'|'by_component', default 'single'). Assets MUST be organized under
   docs/assets/plots/<analysis_id>/ and docs/assets/tables/<analysis_id>/, and
   the page written to docs/analysis/<analysis_id>.md.
 - **FR-022**: All published figures MUST be saved as PNG only (no SVG, PDF,
   or interactive formats) to ensure compatibility with GitHub Pages. Tables
   published to docs MUST be CSV.
 - **FR-023**: Plot styling MUST be configurable via YAML. Provide
   `plots.colors` (ordered list; default ["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00","#ffff33"]) and
   `plots.linestyles` mapping. Default line styles: `{"NC":"-","Decrease":":","Increasing":"--"}` where
   NC corresponds to No Change trials (e.g., same-number pairs like 11, 44, 55).
 - **FR-024**: Figure titles and subtitles MUST be populated from YAML. Title
   includes analysis id/name, response (ALL/ACC1), and component (e.g., P1/N1/P3b).
   Subtitle summarizes key params (baseline window, topomap ±window, ROI rule,
   condition summary). These annotations appear on ERP panels and topomaps.
 - **FR-025**: Website index MUST render a grid where each row corresponds to
   an analysis YAML (analysis_id, sorted alphabetically) and columns correspond
   to components P1/N1/P3b if generated. Thumbnails link to full‑size PNGs via
   a lightweight overlay (no external deps) suitable for GitHub Pages.
 - **FR-026**: Plots MUST be saved at high DPI (configurable). Provide
   `plots.dpi` (default 300) and thumbnail width `plots.thumb_width_px`
   (default 320). The runner generates both full PNGs and thumbnail copies for
   the index grid.
 - **FR-027**: The reporting step MUST update `docs/index.md` to include a
   sorted table/grid of thumbnails sorted by analysis with consistent styling
   and alt text. Existing entries must be updated idempotently (no duplicates).

### Key Entities *(include if feature involves data)*

- **AnalysisConfig**: dataset, montage, components, ROIs, condition sets, outputs.
- **ConditionSet**: name + list of numeric Condition codes; label for plots.
- **Component**: name, time window, default ROIs.
- **ROI**: name + list of electrode labels.
- **SubjectResult**: subject ID, per‑set metrics, QC flags.
- **ConditionSetResult**: grand average evoked, SEM, ROI time‑courses, summary table.

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: End-to-end run produces a docs page and figures within 10 minutes on the provided 24-subject dataset (on typical laptop: 16GB RAM, 4-core CPU or better).
- **SC-002**: Re-running with the same YAML yields identical CSVs and images (bit-identical outputs; no tolerance checks).
- **SC-003**: All condition sets used in the YAML have ≥8 valid epochs per subject on median; empty sets are reported with clear notices.













