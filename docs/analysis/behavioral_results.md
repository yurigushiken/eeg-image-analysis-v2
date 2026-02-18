# Behavioral Analysis Results

## Data
- Subjects: 24
- Change trials used for accuracy: 3660
- Correct change trials with valid RT (150-1500 ms): 601

## Hypothesis 1: Distance Effect on RT
- GEE model on log(RT), clustered by subject: b = -0.0228 (SE = 0.0076), p = 0.002618; ~-2.25% RT change per +1 distance step.
- Subject-level linear trend: mean slope = -13.05 ms/step, 95% CI [-20.79, -5.31], t(23) = -3.487, p(one-sided, negative slope) = 0.0009953.

## Hypothesis 2: Decreasing vs Increasing Accuracy
- Logistic GEE (clustered by subject): OR(D vs I) = 1.596, 95% CI [1.324, 1.924], p = 9.602e-07.
- Subject-level paired effect (D - I): mean = 0.0668, 95% CI [0.0369, 0.0967], t(23) = 4.617, p(one-sided, D>I) = 6.04e-05.

## Output Files
- `docs/assets/poster_plots/behavioral/behavior_poster_main.png` (+ SVG)
- `docs/assets/poster_plots/behavioral/behavior_rt_by_distance.png` (+ SVG)
- `docs/assets/poster_plots/behavioral/behavior_accuracy_by_direction.png` (+ SVG)
- `docs/assets/poster_plots/behavioral/behavioral_inference_summary.json`
- `docs/assets/poster_plots/behavioral/behavioral_subject_direction_distance_summary.csv`
- `docs/assets/poster_plots/behavioral/behavioral_subject_rt_summary.csv`
- `docs/analysis/behavioral_results.md`
