# Research

Decisions
- ACC1 = Target.ACC == 1 (metadata filter).
- Grand averages equal-weight across subjects; SEM across subjects.
- Baseline default [-100,0] ms; YAML configurable.
- Peaks within component windows; topomaps ±50 ms around peak; aggregate (cohort) peak by default.
- Primary selection uses explicit numeric Condition codes organized into named condition sets (e.g., ["12","13"]). No use of metadata categories like iSS/dLL/direction for selection.
- Palette: #e41a1c, #377eb8, #4daf4a, #984ea3, #ff7f00, #ffff33.
- Linestyles: NC solid, Decrease dotted, Increasing dashed.

Alternatives considered
- Weighted by epoch counts; rejected to avoid bias.
- Subject-level peak topomaps as default; kept configurable.
