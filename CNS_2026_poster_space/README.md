# CNS 2026 Poster Space

Local workspace for the CNS 2026 printed poster.

## Goal

Produce a professional 8 ft x 4 ft poster (usable board area 90 in x 42 in) with:

- banner (title, authors, affiliations, logos)
- introduction, methods, results, conclusion
- behavioral statistics and selected ERP no-topo overlays
- print-ready PDF and QC page images

## Build

From `CNS_2026_poster_space/`:

```powershell
.\build.ps1
.\build.ps1 -Clean
```

Output:

- `main.pdf` (print-ready poster)

## QC Export (PDF to PNG)

From `CNS_2026_poster_space/`:

```powershell
pdftoppm -png -r 180 .\main.pdf .\_proof_pages\page
```

This creates:

- `_proof_pages/page-1.png` (and more if multi-page)

Use these exports for margin/alignment and readability checks before final print.

## Directory Map

```text
CNS_2026_poster_space/
|-- main.tex
|-- build.ps1
|-- README.md
|-- cns_2026_poster_guidelines.txt
|-- cns_2026_submitted_abstract.txt
|-- media/
|   |-- tc-logo.png
|   |-- nyu-logo.png
|   |-- jhu-logo.png
|   |-- stimuli_presentation.png
|   `-- electrodes.png
|-- sections/
|   |-- left_column.tex
|   |-- center_column.tex
|   `-- right_column.tex
`-- _proof_pages/
```

## Figure Inputs

- Behavioral figures:
  - `../docs/assets/poster_plots/behavioral/behavior_poster_main.png`
- ERP overlays (no-topo):
  - `../docs/assets/plots/*/*-no_topo.png` for selected analyses
- Study design visuals:
  - `media/stimuli_presentation.png`
  - `media/electrodes.png`

## Notes

- `paper_space(eeg_nn)` in `reference-files/` is used as workflow reference only and is not modified.
- Keep wording tight for printed viewing distance and rely on figure captions for concise interpretation.

