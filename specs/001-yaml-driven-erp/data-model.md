# Data Model

Entities
- AnalysisConfig: dataset, selection, components, preprocessing, roi, plots, outputs.
- ConditionSet: name, conditions (explicit numeric codes), exclude.
- Component: name, window_ms [start,end], rois.
- ROI: name, channels[].
- SubjectResult: subject, per-set metrics, qc.
- ConditionSetResult: evoked, sem, roi_curves, metrics_table.

Validation
- montage_sfp present; channels map to E-codes.
- required metadata columns: Condition, Target.ACC (if response=ACC1).
- Condition is a two-digit string code (e.g., "11".."66"). Selection uses explicit numeric condition sets (not metadata categories like iSS/dLL/direction).
- min_epochs_per_set >= 1.
