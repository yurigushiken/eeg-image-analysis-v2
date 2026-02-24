# Behavioral Analysis Results

## Data
- Subjects: 24
- Change trials used for accuracy: 5184
- Correct change trials with valid RT (150-1500 ms): 4247

## Hypothesis 1: Distance Effect on RT
- GEE model on log(RT), clustered by subject: b = -0.0261 (SE = 0.0033), p = 5.314e-15; ~-2.57% RT change per +1 distance step.
- Subject-level linear trend: mean slope = -13.60 ms/step, 95% CI [-17.56, -9.64], t(23) = -7.110, p(two-sided) = 3.048e-07.

## Hypothesis 2: Decreasing vs Increasing Accuracy
- Logistic GEE (clustered by subject): OR(D vs I) = 1.596, 95% CI [1.339, 1.904], p = 1.959e-07.
- Subject-level paired effect (D - I): mean = 0.0648, 95% CI [0.0369, 0.0927], t(23) = 4.800, p(two-sided) = 7.667e-05.

## Output Files
- `docs/assets/poster_plots/behavioral/behavior_poster_main.png` (+ SVG)
- `docs/assets/poster_plots/behavioral/behavior_rt_by_distance.png` (+ SVG)
- `docs/assets/poster_plots/behavioral/behavior_accuracy_by_direction.png` (+ SVG)
- `docs/assets/poster_plots/behavioral/behavioral_inference_summary.json`
- `docs/assets/poster_plots/behavioral/behavioral_subject_direction_distance_summary.csv`
- `docs/assets/poster_plots/behavioral/behavioral_subject_rt_summary.csv`
- `docs/analysis/behavioral_results.md`
