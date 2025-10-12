# Data Model

Entities
- AnalysisConfig: dataset, selection, components, preprocessing, roi, plots, outputs.
- ConditionSet: name, conditions (explicit numeric codes), exclude.
- Component: name, window_ms [start,end], rois.
- ROI: name, channels[].
- SubjectResult: subject, per-set metrics, qc.
- ConditionSetResult: evoked, sem, roi_curves, metrics_table.
 - RunMetrics: duration_seconds, num_figures, largest_png_bytes, total_png_bytes, largest_png_ok, cumulative_png_ok.

Validation
- montage_sfp present; channels map to E-codes.
- required metadata columns: Condition, Target.ACC (if response=ACC1).
- Condition is a two-digit string code (e.g., "11".."66"). Selection uses explicit numeric condition sets (not metadata categories like iSS/dLL/direction).
- min_epochs_per_set >= 1.
 - baseline_ms must lie within epoch range (e.g., ~-200..496 ms).
