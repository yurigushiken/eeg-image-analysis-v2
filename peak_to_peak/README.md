Peak-to-Peak (P1–N1) Analysis

Overview
- Purpose: quantify peak-to-peak amplitude between the positive P1 and negative N1 measured from the same bilateral POT (N1) electrode set, per subject and condition, and test differences across conditions.
- Electrodes: uses the N1 ROI only (bilateral POT), as defined in `configs/electrodes.yaml` under `N1_L` and `N1_R`.
- Windows: uses a collapsed ROI localizer run on the same POT ROI to derive FWHM windows for P1 (within its a priori range) and N1 (within its a priori range).

Outputs
- `peak_to_peak/output/<analysis_id>/tables/subject_peak_to_peak.csv` with columns:
  subject_id, condition, p1_peak_uv, p1_latency_ms, n1_peak_uv, n1_latency_ms, p2p_amplitude_uv, n_epochs, window_p1_start_ms, window_p1_end_ms, window_n1_start_ms, window_n1_end_ms
- `peak_to_peak/output/<analysis_id>/plots/<analysis_id>-N1.png`: ERP overlay (N1 ROI only), no topomaps.

Run
1) Generate measurements and plot from an existing analysis YAML:
   `python peak_to_peak/run_peak_to_peak.py --config configs/analyses/12_13.yaml`
2) Run statistics with the provided template (edit paths first as below):
   `python scripts/run_statistics.py --config peak_to_peak/stats.yaml`

Notes
- Peak amplitudes are signed in µV (positive for P1, negative for N1). `p2p_amplitude_uv` computes P1_peak_uv - N1_peak_uv so magnitudes add.
- Topographies are intentionally omitted.
