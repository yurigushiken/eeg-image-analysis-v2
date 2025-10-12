<!--
Sync Impact Report
- Version change: (none) -> 1.0.0
- Modified principles: Initial creation
- Added sections: Core Principles, Additional Constraints, Development Workflow, Governance
- Removed sections: None
- Templates requiring updates (pending):
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
- Follow-up TODOs:
  - TODO(ENV_FILE): Add environment.yml for `numbers-eeg` with exact versions
  - TODO(CONFIGS): Add configs/electrodes.yaml, components.yaml, analyses/*.yaml
  - TODO(MAPPINGS): Optional mapping from numeric event labels to descriptive names
-->

# EEG Image Analysis Constitution

## Core Principles

### I. Reproducible Environment (NON-NEGOTIABLE)
All analysis must run under a declared Python environment. The canonical
environment name is `eeg-image` (Python 3.12). Dependencies must be pinned and
captured in a shareable spec (environment.yml). Analyses and figures must be
rebuildable by running documented commands without manual steps.

### II. Data Governance and Local-Only Raw Files
Raw/participant EEG FIF files live under `data/` and are not tracked by Git.
Generated intermediates go to `data/outputs/` (ignored). Only finalized plots
and summary tables required for publication are committed to `docs/`.
No PII is allowed in the repository.

### III. Declarative, YAML‑Driven Analyses
Analyses are defined via YAML configurations under `configs/`. A small, stable
CLI loads these configs, selects trials using metadata fields (e.g.,
`direction`, `change_group`, `size`), computes ERPs/measures, and writes
results. Adding a new analysis means adding a YAML file, not new imperative
code.

### IV. ERP Component Standards and ROIs
We predefine components and time windows (e.g., N1: 125–200 ms; P3b: 300–600 ms)
and named ROIs using electrode labels. The Net montage is
`net/AdultAverageNet128_v1.sfp`. Plots use consistent baselining (−100–0 ms),
overlay style, and SEM shading for group results.

### V. Documentation as an Artifact
Every analysis writes a Markdown page under `docs/analysis/` with a brief method
summary, figure gallery, and links to CSV tables. GitHub Pages publishes from
`/docs`.

## Additional Constraints

1. Performance: Scripts must stream or batch-load subjects; avoid loading all
   data into memory at once when not required.
2. Integrity checks: Before computation, validate epochs: sample rate, channel
   count, metadata columns presence, and event_id sanity. Fail fast with clear
   messages.
3. Determinism: Random operations must set seeds recorded in outputs.
4. Paths: Use relative project paths and `Path` utilities; do not hard-code
   user-specific directories.

## Development Workflow

1. Config-first changes: propose/edit YAML in `configs/` and review diffs.
2. Small core library under `src/eeg/` with modules for I/O, selection, ERP,
   measures, plots, and reporting. Avoid proliferation of ad-hoc scripts.
3. QC then analysis: each run emits a QC summary alongside figures; CI may run
   lightweight schema checks on YAML and smoke tests (no raw data in CI).
4. Output policy: commit only items in `docs/**` needed for the website. Leave
   `data/**` outputs untracked.

## Governance

- This constitution governs analysis structure, environment, and publication
  standards. It supersedes ad-hoc conventions.
- Amendments require: a proposal PR, a version bump per semantic versioning,
  migration notes if breaking, and README/docs updates as needed.
- Compliance: PR reviewers must verify that new analyses adhere to YAML-driven
  patterns, environment reproducibility, and documentation outputs.

**Version**: 1.0.0 | **Ratified**: 2025-10-11 | **Last Amended**: 2025-10-11

