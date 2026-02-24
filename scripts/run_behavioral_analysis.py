#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf


def _load_metadata(metadata_dir: Path) -> pd.DataFrame:
    files = sorted(metadata_dir.glob("sub-*_preprocessed-epo_metadata.csv"))
    if not files:
        raise FileNotFoundError(f"No metadata CSV files found in {metadata_dir}")

    frames = []
    for f in files:
        df = pd.read_csv(f)
        if "SubjectID" not in df.columns:
            raise ValueError(f"Missing SubjectID in {f}")
        if "Condition" not in df.columns:
            raise ValueError(f"Missing Condition in {f}")
        if "Target.ACC" not in df.columns:
            raise ValueError(f"Missing Target.ACC in {f}")
        if "Target.RT" not in df.columns:
            raise ValueError(f"Missing Target.RT in {f}")

        df = df.copy()
        df["subject"] = df["SubjectID"].astype(str).str.zfill(2)
        cond_numeric = df["Condition"].astype(str).str.extract(r"(\d+)")[0]
        df = df[cond_numeric.str.len() == 2].copy()
        df["condition"] = cond_numeric[cond_numeric.str.len() == 2]
        df["prime"] = df["condition"].str[0].astype(int)
        df["target"] = df["condition"].str[1].astype(int)
        df["is_change"] = df["prime"] != df["target"]
        df["distance"] = (df["target"] - df["prime"]).abs()
        df["direction_clean"] = np.where(
            df["target"] > df["prime"],
            "I",
            np.where(df["target"] < df["prime"], "D", "NC"),
        )
        df["acc"] = pd.to_numeric(df["Target.ACC"], errors="coerce")
        df["rt_ms"] = pd.to_numeric(df["Target.RT"], errors="coerce")
        frames.append(df)

    all_df = pd.concat(frames, ignore_index=True)
    return all_df


def _subject_level_accuracy_test(change_df: pd.DataFrame) -> Dict[str, float]:
    sub = (
        change_df.groupby(["subject", "direction_clean"], as_index=False)["acc"]
        .mean()
        .pivot(index="subject", columns="direction_clean", values="acc")
        .dropna(subset=["I", "D"])
    )
    diff = sub["D"] - sub["I"]
    t_stat, p_two = stats.ttest_1samp(diff, popmean=0.0)
    p_one = p_two / 2.0 if (not math.isnan(t_stat) and t_stat > 0) else 1.0 - (p_two / 2.0)
    dz = float(diff.mean() / diff.std(ddof=1))
    ci_low, ci_high = stats.t.interval(
        confidence=0.95,
        df=len(diff) - 1,
        loc=float(diff.mean()),
        scale=float(stats.sem(diff)),
    )
    return {
        "n_subjects": int(len(diff)),
        "mean_diff_D_minus_I": float(diff.mean()),
        "ci95_low": float(ci_low),
        "ci95_high": float(ci_high),
        "t": float(t_stat),
        "p_two_sided": float(p_two),
        "p_one_sided_D_gt_I": float(p_one),
        "cohens_dz": dz,
    }


def _subject_level_rt_distance_test(rt_df: pd.DataFrame) -> Dict[str, float]:
    means = (
        rt_df.groupby(["subject", "distance"], as_index=False)["rt_ms"]
        .mean()
        .pivot(index="subject", columns="distance", values="rt_ms")
    )
    means = means.dropna(subset=[1, 2, 3])
    slopes = means.apply(lambda r: np.polyfit([1, 2, 3], [r[1], r[2], r[3]], 1)[0], axis=1)
    t_stat, p_two = stats.ttest_1samp(slopes.values, popmean=0.0)
    p_one = p_two / 2.0 if (not math.isnan(t_stat) and t_stat < 0) else 1.0 - (p_two / 2.0)
    dz = float(slopes.mean() / slopes.std(ddof=1))
    ci_low, ci_high = stats.t.interval(
        confidence=0.95,
        df=len(slopes) - 1,
        loc=float(slopes.mean()),
        scale=float(stats.sem(slopes)),
    )
    return {
        "n_subjects": int(len(slopes)),
        "mean_slope_ms_per_distance": float(slopes.mean()),
        "ci95_low": float(ci_low),
        "ci95_high": float(ci_high),
        "t": float(t_stat),
        "p_two_sided": float(p_two),
        "p_one_sided_negative_slope": float(p_one),
        "cohens_dz": dz,
    }


def _fit_accuracy_gee(change_df: pd.DataFrame):
    model = smf.gee(
        "acc ~ C(direction_clean, Treatment(reference='I')) + distance",
        groups="subject",
        data=change_df,
        family=sm.families.Binomial(),
        cov_struct=sm.cov_struct.Exchangeable(),
    )
    return model.fit()


def _fit_rt_gee(rt_df: pd.DataFrame):
    rt_df = rt_df.copy()
    rt_df["log_rt"] = np.log(rt_df["rt_ms"])
    model = smf.gee(
        "log_rt ~ distance + C(direction_clean, Treatment(reference='I'))",
        data=rt_df,
        groups="subject",
        family=sm.families.Gaussian(),
        cov_struct=sm.cov_struct.Exchangeable(),
    )
    return model.fit()


def _save_plot_rt_distance(rt_df: pd.DataFrame, out_path: Path) -> None:
    subj_means = (
        rt_df.groupby(["subject", "distance"], as_index=False)["rt_ms"]
        .mean()
    )
    group = (
        subj_means.groupby("distance")["rt_ms"]
        .agg(["mean", "std", "count"])
        .reset_index()
    )
    group["sem"] = group["std"] / np.sqrt(group["count"])
    group["ci95"] = stats.t.ppf(0.975, group["count"] - 1) * group["sem"]

    fig, ax = plt.subplots(figsize=(7.4, 5.0))
    ax.errorbar(
        group["distance"],
        group["mean"],
        yerr=group["ci95"],
        color="#1f77b4",
        marker="o",
        markersize=7,
        linewidth=2.5,
        capsize=5,
        label="Group mean ± 95% CI",
    )
    ax.set_xticks([1, 2, 3])
    ax.set_xlabel("Numerical Distance |target - prime|")
    ax.set_ylabel("Reaction Time (ms)")
    ax.set_title("Distance Effect on Reaction Time")
    ax.legend(frameon=True, fontsize=9)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=300)
    fig.savefig(out_path.with_suffix(".svg"))
    plt.close(fig)


def _save_plot_accuracy_direction(change_df: pd.DataFrame, out_path: Path) -> None:
    sub_acc = (
        change_df.groupby(["subject", "direction_clean"], as_index=False)["acc"]
        .mean()
        .pivot(index="subject", columns="direction_clean", values="acc")
        .dropna(subset=["I", "D"])
    )
    means = {
        "I": float(sub_acc["I"].mean()),
        "D": float(sub_acc["D"].mean()),
    }
    sems = {
        "I": float(stats.sem(sub_acc["I"])),
        "D": float(stats.sem(sub_acc["D"])),
    }

    fig, ax = plt.subplots(figsize=(6.2, 5.0))
    x = np.array([0, 1])
    ax.errorbar(
        x,
        [means["I"], means["D"]],
        yerr=[sems["I"] * 1.96, sems["D"] * 1.96],
        fmt="o-",
        color="#d62728",
        linewidth=2.5,
        markersize=8,
        capsize=5,
        label="Group mean ± 95% CI",
    )
    ax.set_xticks(x)
    ax.set_xticklabels(["Increasing", "Decreasing"])
    ax.set_ylabel("Accuracy (Proportion Correct)")
    ax.set_ylim(0.5, 1.0)
    ax.set_title("Accuracy by Direction")
    ax.legend(frameon=True, fontsize=9)
    ax.grid(alpha=0.25, axis="y")
    fig.tight_layout()
    fig.savefig(out_path, dpi=300)
    fig.savefig(out_path.with_suffix(".svg"))
    plt.close(fig)


def _save_poster_figure(rt_df: pd.DataFrame, change_df: pd.DataFrame, out_path: Path) -> None:
    subj_rt = rt_df.groupby(["subject", "distance"], as_index=False)["rt_ms"].mean()
    rt_group = (
        subj_rt.groupby("distance")["rt_ms"]
        .agg(["mean", "std", "count"])
        .reset_index()
    )
    rt_group["sem"] = rt_group["std"] / np.sqrt(rt_group["count"])
    rt_group["ci95"] = stats.t.ppf(0.975, rt_group["count"] - 1) * rt_group["sem"]
    sub_acc = (
        change_df.groupby(["subject", "direction_clean"], as_index=False)["acc"]
        .mean()
        .pivot(index="subject", columns="direction_clean", values="acc")
        .dropna(subset=["I", "D"])
    )

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.2))

    ax = axes[0]
    ax.errorbar(
        rt_group["distance"],
        rt_group["mean"],
        yerr=rt_group["ci95"],
        color="#1f77b4",
        marker="o",
        markersize=7,
        linewidth=2.5,
        capsize=4,
    )
    ax.set_xticks([1, 2, 3])
    ax.set_xlabel("Distance |target - prime|")
    ax.set_ylabel("RT (ms)")
    ax.set_title("A. Distance Effect on RT")
    ax.grid(alpha=0.25)

    ax = axes[1]
    x = np.array([0, 1])
    means = [sub_acc["I"].mean(), sub_acc["D"].mean()]
    sems = [stats.sem(sub_acc["I"]), stats.sem(sub_acc["D"])]
    ax.errorbar(
        x,
        means,
        yerr=np.array(sems) * 1.96,
        fmt="o-",
        color="#d62728",
        linewidth=2.5,
        markersize=8,
        capsize=4,
    )
    ax.set_xticks(x)
    ax.set_xticklabels(["Increasing", "Decreasing"])
    ax.set_ylabel("Accuracy")
    ax.set_ylim(0.5, 1.0)
    ax.set_title("B. Decreasing > Increasing Accuracy")
    ax.grid(alpha=0.25, axis="y")

    fig.suptitle("Behavioral Results: Numerical Change Detection", fontsize=14, y=1.02)
    fig.tight_layout()
    fig.savefig(out_path, dpi=350, bbox_inches="tight")
    fig.savefig(out_path.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def run_analysis(
    metadata_dir: Path,
    out_dir: Path,
    rt_min_ms: float = 150.0,
    rt_max_ms: float = 1500.0,
) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float], Dict[str, float]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    analysis_dir = Path("docs/analysis")
    analysis_dir.mkdir(parents=True, exist_ok=True)

    raw = _load_metadata(metadata_dir)
    change = raw[raw["is_change"]].copy()
    change = change[change["direction_clean"].isin(["I", "D"])].copy()
    change = change[change["acc"].isin([0.0, 1.0])].copy()

    rt = change[(change["acc"] == 1.0) & change["rt_ms"].notna()].copy()
    rt = rt[(rt["rt_ms"] >= rt_min_ms) & (rt["rt_ms"] <= rt_max_ms)].copy()

    if change["subject"].nunique() < 2:
        raise ValueError("Need at least two subjects for group-level inference.")
    if rt["subject"].nunique() < 2:
        raise ValueError("Need at least two subjects with valid RT data.")

    acc_gee = _fit_accuracy_gee(change)
    rt_gee = _fit_rt_gee(rt)

    acc_subj = _subject_level_accuracy_test(change)
    rt_subj = _subject_level_rt_distance_test(rt)

    acc_gee_coef = "C(direction_clean, Treatment(reference='I'))[T.D]"
    acc_gee_b = float(acc_gee.params[acc_gee_coef])
    acc_gee_se = float(acc_gee.bse[acc_gee_coef])
    acc_gee_p = float(acc_gee.pvalues[acc_gee_coef])
    acc_gee_or = float(np.exp(acc_gee_b))
    acc_gee_or_ci = (
        float(np.exp(acc_gee_b - 1.96 * acc_gee_se)),
        float(np.exp(acc_gee_b + 1.96 * acc_gee_se)),
    )

    rt_gee_b = float(rt_gee.params["distance"])
    rt_gee_se = float(rt_gee.bse["distance"])
    rt_gee_p = float(rt_gee.pvalues["distance"])
    # Convert log-slope to percent change in RT per +1 distance step.
    rt_pct = float((np.exp(rt_gee_b) - 1.0) * 100.0)

    trial_counts = (
        change.groupby(["subject", "direction_clean", "distance"], as_index=False)
        .agg(
            n_trials=("acc", "size"),
            accuracy=("acc", "mean"),
            n_correct=("acc", "sum"),
        )
        .sort_values(["subject", "direction_clean", "distance"])
    )
    trial_counts.to_csv(out_dir / "behavioral_subject_direction_distance_summary.csv", index=False)

    rt_counts = rt.groupby(["subject", "direction_clean", "distance"])["rt_ms"].agg(
        n_rt="size",
        rt_mean_ms="mean",
        rt_sd_ms="std",
    ).reset_index()
    rt_counts.to_csv(out_dir / "behavioral_subject_rt_summary.csv", index=False)

    _save_plot_rt_distance(rt, out_dir / "behavior_rt_by_distance.png")
    _save_plot_accuracy_direction(change, out_dir / "behavior_accuracy_by_direction.png")
    _save_poster_figure(rt, change, out_dir / "behavior_poster_main.png")

    summary = {
        "dataset": {
            "n_subjects": int(change["subject"].nunique()),
            "n_change_trials_for_accuracy": int(len(change)),
            "n_correct_trials_with_valid_rt": int(len(rt)),
            "rt_min_ms": float(rt_min_ms),
            "rt_max_ms": float(rt_max_ms),
        },
        "accuracy_gee": {
            "coef_log_odds_D_vs_I": acc_gee_b,
            "se": acc_gee_se,
            "p_value": acc_gee_p,
            "odds_ratio_D_vs_I": acc_gee_or,
            "odds_ratio_ci95_low": acc_gee_or_ci[0],
            "odds_ratio_ci95_high": acc_gee_or_ci[1],
        },
        "accuracy_subject_level": acc_subj,
        "rt_gee_distance": {
            "coef_log_rt_per_distance_step": rt_gee_b,
            "se": rt_gee_se,
            "p_value": rt_gee_p,
            "percent_change_per_distance_step": rt_pct,
        },
        "rt_subject_level_distance_trend": rt_subj,
    }
    with open(out_dir / "behavioral_inference_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    report_path = analysis_dir / "behavioral_results.md"

    report_lines = [
        "# Behavioral Analysis Results",
        "",
        "## Data",
        f"- Subjects: {summary['dataset']['n_subjects']}",
        f"- Change trials used for accuracy: {summary['dataset']['n_change_trials_for_accuracy']}",
        f"- Correct change trials with valid RT ({int(rt_min_ms)}-{int(rt_max_ms)} ms): {summary['dataset']['n_correct_trials_with_valid_rt']}",
        "",
        "## Hypothesis 1: Distance Effect on RT",
        (
            "- GEE model on log(RT), clustered by subject: "
            f"b = {rt_gee_b:.4f} (SE = {rt_gee_se:.4f}), p = {rt_gee_p:.4g}; "
            f"~{rt_pct:.2f}% RT change per +1 distance step."
        ),
        (
            "- Subject-level linear trend: "
            f"mean slope = {rt_subj['mean_slope_ms_per_distance']:.2f} ms/step, "
            f"95% CI [{rt_subj['ci95_low']:.2f}, {rt_subj['ci95_high']:.2f}], "
            f"t({rt_subj['n_subjects'] - 1}) = {rt_subj['t']:.3f}, "
            f"p(two-sided) = {rt_subj['p_two_sided']:.4g}."
        ),
        "",
        "## Hypothesis 2: Decreasing vs Increasing Accuracy",
        (
            "- Logistic GEE (clustered by subject): "
            f"OR(D vs I) = {acc_gee_or:.3f}, 95% CI [{acc_gee_or_ci[0]:.3f}, {acc_gee_or_ci[1]:.3f}], "
            f"p = {acc_gee_p:.4g}."
        ),
        (
            "- Subject-level paired effect (D - I): "
            f"mean = {acc_subj['mean_diff_D_minus_I']:.4f}, "
            f"95% CI [{acc_subj['ci95_low']:.4f}, {acc_subj['ci95_high']:.4f}], "
            f"t({acc_subj['n_subjects'] - 1}) = {acc_subj['t']:.3f}, "
            f"p(two-sided) = {acc_subj['p_two_sided']:.4g}."
        ),
        "",
        "## Output Files",
        f"- `{(out_dir / 'behavior_poster_main.png').as_posix()}` (+ SVG)",
        f"- `{(out_dir / 'behavior_rt_by_distance.png').as_posix()}` (+ SVG)",
        f"- `{(out_dir / 'behavior_accuracy_by_direction.png').as_posix()}` (+ SVG)",
        f"- `{(out_dir / 'behavioral_inference_summary.json').as_posix()}`",
        f"- `{(out_dir / 'behavioral_subject_direction_distance_summary.csv').as_posix()}`",
        f"- `{(out_dir / 'behavioral_subject_rt_summary.csv').as_posix()}`",
        f"- `{report_path.as_posix()}`",
    ]
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    return summary["dataset"], summary["accuracy_gee"], summary["rt_gee_distance"], summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Run behavioral analyses for RT and accuracy.")
    parser.add_argument(
        "--metadata-dir",
        type=Path,
        default=Path("data/lab_data_original_with_primes"),
        help="Directory containing sub-*_preprocessed-epo_metadata.csv files.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("docs/assets/poster_plots/behavioral"),
        help="Directory for analysis outputs and figures.",
    )
    parser.add_argument("--rt-min-ms", type=float, default=150.0)
    parser.add_argument("--rt-max-ms", type=float, default=1500.0)
    args = parser.parse_args()

    dataset, acc_gee, rt_lmm, full = run_analysis(
        metadata_dir=args.metadata_dir,
        out_dir=args.out_dir,
        rt_min_ms=args.rt_min_ms,
        rt_max_ms=args.rt_max_ms,
    )

    print("\nBehavioral analysis completed.")
    print(f"Subjects: {dataset['n_subjects']}")
    print(f"Change trials (accuracy): {dataset['n_change_trials_for_accuracy']}")
    print(f"Valid RT trials: {dataset['n_correct_trials_with_valid_rt']}")
    print(
        "Accuracy (D vs I): "
        f"OR={acc_gee['odds_ratio_D_vs_I']:.3f}, "
        f"p={acc_gee['p_value']:.4g}"
    )
    print(
        "RT distance effect: "
        f"b={rt_lmm['coef_log_rt_per_distance_step']:.4f}, "
        f"p={rt_lmm['p_value']:.4g}, "
        f"{rt_lmm['percent_change_per_distance_step']:.2f}% per step"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
