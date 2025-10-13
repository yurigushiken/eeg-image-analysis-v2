# Phase 2 Implementation Plan: Statistical Analysis Infrastructure

**Date**: October 12, 2024
**Status**: PLANNING - Ready for Implementation

---

## Executive Summary

Phase 2 extends the pipeline with **subject-level measurements** and **YAML-controlled statistical testing**. This enables reproducible, transparent statistical analysis with all parameters documented in configuration files.

**Three Statistical Tests**:
1. **Repeated-Measures ANOVA** (overall effect)
2. **Pairwise t-tests** (post-hoc comparisons with correction)
3. **Linear Mixed-Effects Models** (LMM, handles missing data)

**All configured via YAML** — no hardcoded parameters!

---

## Phase 2 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    YAML Configuration                        │
│  (analysis.yaml + statistics.yaml)                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Phase 2A: Data Collection                       │
│  • Subject-level FAL & amplitude measurements               │
│  • Output: subject_measurements.csv                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│           Phase 2B: Statistical Testing                      │
│  • Repeated-measures ANOVA (pingouin)                       │
│  • Pairwise t-tests (with FDR/Bonferroni)                   │
│  • Linear Mixed Models (statsmodels)                        │
│  • Output: statistics.json + stats_summary.txt              │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Phase 2C: Visualization                         │
│  • Boxplots, violin plots, raincloud plots                  │
│  • Condition comparison figures                             │
│  • Effect size visualizations                               │
│  • Output: stats plots in plots_dir                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 2A: Subject-Level Measurements

### Goal
Collect FAL and amplitude measurements **per subject** (not just grand average) to enable within-subjects statistical tests.

### Implementation

#### 1. Modify `run_analysis.py`

**Location**: Inside subject loop (after line 169)

**New Code**:
```python
# === Subject-level measurement collection (Phase 2A) ===
subject_measurements = []

# Inside the subject loop (line 108-180)
for fif_idx, fif in enumerate(fif_files, 1):
    # ... existing subject loading code ...

    # Process each condition set
    for item in sets:
        # ... existing condition selection ...

        evk = sub.average()  # Subject-level evoked
        subj_id = extract_subject_id(epochs, fif)

        # For each component, compute subject-level measurements
        for comp in cfg.components:
            comp_result = collapsed_results.get(comp)
            if comp_result is None:
                continue

            # Get component parameters
            window_start = comp_result['window_start_ms']
            window_end = comp_result['window_end_ms']

            # Get ROI channels
            comp_cfg = components_cfg.get(comp, {})
            roi_names = comp_cfg.get('rois', [])
            roi_channels = []
            for roi_name in roi_names:
                if roi_name in electrodes_cfg:
                    roi_channels.extend(electrodes_cfg[roi_name])

            if not roi_channels:
                continue

            try:
                # Extract subject ROI curve
                roi_data = evk.copy().pick_channels(roi_channels, ordered=False)
                roi_curve = roi_data.data.mean(axis=0) * 1e6
                times_ms_subj = evk.times * 1000.0

                # Compute subject-level mean amplitude
                subj_mean_amp = float(np.mean(
                    roi_curve[(times_ms_subj >= window_start) & (times_ms_subj <= window_end)]
                ))

                # Compute subject-level FAL
                comp_polarity = "negative" if comp.upper().startswith("N") else "positive"
                subj_fal = fractional_area_latency(
                    signal=roi_curve,
                    times_ms=times_ms_subj,
                    window_ms=(window_start, window_end),
                    fraction=0.5,
                    polarity=comp_polarity
                )

                # Record subject measurement
                subject_measurements.append({
                    "subject_id": subj_id,
                    "component": comp,
                    "condition": item['name'],
                    "latency_frac_area_ms": subj_fal,
                    "mean_amplitude_roi": subj_mean_amp,
                    "n_epochs": epoch_count,
                })

            except Exception as e:
                print(f"    Warning: Subject {subj_id} {comp} {item['name']} measurement failed: {e}")
                # Record NaN for failed measurement
                subject_measurements.append({
                    "subject_id": subj_id,
                    "component": comp,
                    "condition": item['name'],
                    "latency_frac_area_ms": float('nan'),
                    "mean_amplitude_roi": float('nan'),
                    "n_epochs": epoch_count,
                })

# After subject loop completes, save subject-level CSV
if subject_measurements:
    import csv
    subj_csv_path = os.path.join(tables_dir, "subject_measurements.csv")
    fieldnames = [
        "subject_id", "component", "condition",
        "latency_frac_area_ms", "mean_amplitude_roi", "n_epochs"
    ]
    with open(subj_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(subject_measurements)

    print(f"Saved subject-level measurements: {os.path.basename(subj_csv_path)}")
    print(f"  Recorded {len(subject_measurements)} subject-component-condition measurements\n")
```

#### 2. Expected Output

**New File**: `docs/assets/tables/{analysis_id}/subject_measurements.csv`

```csv
subject_id,component,condition,latency_frac_area_ms,mean_amplitude_roi,n_epochs
sub-02,N1,Cardinality1,171.2,-2.5,45
sub-02,N1,Cardinality2,173.8,-2.3,42
sub-02,N1,Cardinality3,175.1,-3.1,40
sub-03,N1,Cardinality1,169.5,-3.2,48
sub-03,N1,Cardinality2,172.3,-2.8,46
...
```

**Key**: One row per subject × component × condition combination.

---

## Phase 2B: Statistical Testing Module

### New File Structure

```
src/eeg/
├── statistics.py          # NEW: Statistical test implementations
└── stats_config.py        # NEW: Load statistics YAML configuration

configs/
└── statistics/            # NEW: Statistical test configurations
    ├── default.yaml       # Default settings
    ├── anova_only.yaml    # ANOVA-only tests
    └── full_suite.yaml    # All three tests

scripts/
└── run_statistics.py      # NEW: Statistical analysis CLI
```

### YAML Schema for Statistical Configuration

#### Example: `configs/statistics/default.yaml`

```yaml
# Statistical Analysis Configuration
# Controls which tests to run and how to correct for multiple comparisons

analysis_id: "cardinality_within_small"  # Must match analysis YAML

# Which dependent variables to analyze
dependent_variables:
  - name: "latency_frac_area_ms"
    label: "Fractional Area Latency"
    units: "ms"
  - name: "mean_amplitude_roi"
    label: "Mean Amplitude"
    units: "µV"

# Which components to analyze
components: ["N1", "P1", "P3b"]

# Independent variables (factors)
factors:
  - name: "condition"
    type: "categorical"
    levels: ["Cardinality1", "Cardinality2", "Cardinality3"]  # Auto-detected if null

# Statistical tests to run
tests:
  # Test 1: Repeated-Measures ANOVA
  repeated_measures_anova:
    enabled: true
    method: "pingouin"  # pingouin.rm_anova
    within: "condition"  # Within-subjects factor
    subject: "subject_id"
    correction: "auto"  # Sphericity correction (GG, HF)
    effect_size: "np2"  # Partial eta-squared

  # Test 2: Pairwise t-tests (post-hoc)
  pairwise_tests:
    enabled: true
    method: "pingouin"  # pingouin.pairwise_ttests
    parametric: true  # Use t-test (false = Wilcoxon)
    padjust: "fdr_bh"  # Multiple comparison correction
    # Options: "none", "bonf", "holm", "fdr_bh", "fdr_by"
    tail: "two-sided"
    alpha: 0.05
    effect_size: "cohen"  # Cohen's d

  # Test 3: Linear Mixed-Effects Model
  linear_mixed_model:
    enabled: true
    method: "statsmodels"  # statsmodels.MixedLM
    formula: "latency_frac_area_ms ~ C(condition)"  # R-style formula
    groups: "subject_id"  # Random effects grouping
    re_formula: "1"  # Random intercept (use "~1 + condition" for random slopes)
    method_fit: "lbfgs"  # Optimization method
    reml: true  # Use REML (vs ML)

# Output options
outputs:
  save_json: true  # statistics.json with all results
  save_txt: true  # stats_summary.txt (human-readable)
  save_csv: true  # pairwise_comparisons.csv, anova_results.csv
  plots: true  # Generate statistical plots

# Plot configurations
plots:
  boxplot:
    enabled: true
    show_points: true  # Individual subject points
    show_mean: true
  violin:
    enabled: true
    inner: "box"  # "box", "quartile", or "point"
  raincloud:
    enabled: false  # Requires ptitprince package
  effect_size:
    enabled: true  # Bar plot of effect sizes with CI

# Reporting options
reporting:
  alpha: 0.05  # Significance threshold
  report_all: true  # Report non-significant results too
  apa_style: true  # Format output in APA style
  decimal_places: 3
```

#### Minimal Example: `configs/statistics/anova_only.yaml`

```yaml
analysis_id: "landing_on_2"

dependent_variables:
  - name: "latency_frac_area_ms"
    label: "N1 Latency"
    units: "ms"

components: ["N1"]

tests:
  repeated_measures_anova:
    enabled: true
  pairwise_tests:
    enabled: false
  linear_mixed_model:
    enabled: false
```

### Implementation: `src/eeg/statistics.py`

```python
"""Statistical analysis for ERP measurements.

This module implements repeated-measures ANOVA, pairwise t-tests, and
linear mixed-effects models for subject-level ERP data.
"""
from __future__ import annotations

from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd
import pingouin as pg
import statsmodels.formula.api as smf
from pathlib import Path


class ERPStatistics:
    """Statistical analysis for ERP measurements."""

    def __init__(self, data: pd.DataFrame, config: Dict[str, Any]):
        """
        Initialize statistical analyzer.

        Args:
            data: Subject-level measurements DataFrame
                  Columns: subject_id, component, condition, latency_frac_area_ms, mean_amplitude_roi
            config: Statistical configuration from YAML
        """
        self.data = data
        self.config = config
        self.results = {}

    def run_all_tests(self) -> Dict[str, Any]:
        """
        Run all enabled statistical tests.

        Returns:
            Dictionary of test results
        """
        tests_config = self.config.get('tests', {})

        for component in self.config.get('components', []):
            for dv_config in self.config.get('dependent_variables', []):
                dv = dv_config['name']

                # Filter data for this component
                data_comp = self.data[self.data['component'] == component].copy()

                if data_comp.empty:
                    print(f"Warning: No data for {component}, skipping")
                    continue

                result_key = f"{component}_{dv}"
                self.results[result_key] = {
                    'component': component,
                    'dv': dv,
                    'dv_label': dv_config.get('label', dv),
                    'units': dv_config.get('units', ''),
                }

                # Test 1: Repeated-Measures ANOVA
                if tests_config.get('repeated_measures_anova', {}).get('enabled', False):
                    anova_results = self._run_rm_anova(data_comp, dv, tests_config['repeated_measures_anova'])
                    self.results[result_key]['rm_anova'] = anova_results

                # Test 2: Pairwise t-tests
                if tests_config.get('pairwise_tests', {}).get('enabled', False):
                    pairwise_results = self._run_pairwise_tests(data_comp, dv, tests_config['pairwise_tests'])
                    self.results[result_key]['pairwise'] = pairwise_results

                # Test 3: Linear Mixed Model
                if tests_config.get('linear_mixed_model', {}).get('enabled', False):
                    lmm_results = self._run_lmm(data_comp, dv, tests_config['linear_mixed_model'])
                    self.results[result_key]['lmm'] = lmm_results

        return self.results

    def _run_rm_anova(self, data: pd.DataFrame, dv: str, config: Dict) -> Dict[str, Any]:
        """Run repeated-measures ANOVA using pingouin."""
        try:
            # Remove NaN values
            data_clean = data[[config['subject'], config['within'], dv]].dropna()

            # Run RM-ANOVA
            aov = pg.rm_anova(
                data=data_clean,
                dv=dv,
                within=config['within'],
                subject=config['subject'],
                correction=config.get('correction', 'auto'),
                detailed=True
            )

            # Extract key statistics
            row = aov.iloc[0]  # First row is the within-subjects effect

            return {
                'F': float(row['F']),
                'df_num': int(row['ddof1']),
                'df_denom': int(row['ddof2']),
                'p_value': float(row['p-unc']),
                'effect_size_np2': float(row['np2']),
                'sphericity_W': float(row.get('W-spher', np.nan)),
                'sphericity_p': float(row.get('p-spher', np.nan)),
                'correction_used': str(row.get('eps', 'none')),
                'table': aov.to_dict('records')
            }
        except Exception as e:
            return {'error': str(e)}

    def _run_pairwise_tests(self, data: pd.DataFrame, dv: str, config: Dict) -> Dict[str, Any]:
        """Run pairwise t-tests with multiple comparison correction."""
        try:
            data_clean = data[['subject_id', 'condition', dv]].dropna()

            # Pingouin pairwise tests
            pw = pg.pairwise_tests(
                data=data_clean,
                dv=dv,
                within='condition',
                subject='subject_id',
                parametric=config.get('parametric', True),
                padjust=config.get('padjust', 'fdr_bh'),
                tail=config.get('tail', 'two-sided'),
                alpha=config.get('alpha', 0.05),
                effsize=config.get('effect_size', 'cohen')
            )

            return {
                'table': pw.to_dict('records'),
                'n_comparisons': len(pw),
                'correction_method': config.get('padjust', 'fdr_bh'),
                'alpha': config.get('alpha', 0.05)
            }
        except Exception as e:
            return {'error': str(e)}

    def _run_lmm(self, data: pd.DataFrame, dv: str, config: Dict) -> Dict[str, Any]:
        """Run linear mixed-effects model using statsmodels."""
        try:
            data_clean = data[['subject_id', 'condition', dv]].dropna()

            # Build formula
            formula = config.get('formula', f"{dv} ~ C(condition)")
            groups = data_clean[config.get('groups', 'subject_id')]

            # Fit LMM
            model = smf.mixedlm(
                formula=formula,
                data=data_clean,
                groups=groups,
                re_formula=config.get('re_formula', '1')
            )

            result = model.fit(
                method=config.get('method_fit', 'lbfgs'),
                reml=config.get('reml', True)
            )

            # Extract results
            return {
                'aic': float(result.aic),
                'bic': float(result.bic),
                'log_likelihood': float(result.llf),
                'converged': bool(result.converged),
                'parameters': result.params.to_dict(),
                'pvalues': result.pvalues.to_dict(),
                'std_errors': result.bse.to_dict(),
                'conf_int': result.conf_int().to_dict(),
                'summary': str(result.summary())
            }
        except Exception as e:
            return {'error': str(e)}

    def save_results(self, output_dir: Path):
        """Save results to JSON, TXT, and CSV files."""
        import json

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # JSON: Full results
        if self.config.get('outputs', {}).get('save_json', True):
            json_path = output_dir / "statistics.json"
            with open(json_path, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"Saved statistics JSON: {json_path}")

        # TXT: Human-readable summary
        if self.config.get('outputs', {}).get('save_txt', True):
            txt_path = output_dir / "stats_summary.txt"
            self._write_text_summary(txt_path)
            print(f"Saved statistics summary: {txt_path}")

        # CSV: Individual result tables
        if self.config.get('outputs', {}).get('save_csv', True):
            self._write_csv_tables(output_dir)

    def _write_text_summary(self, path: Path):
        """Write APA-style text summary."""
        alpha = self.config.get('reporting', {}).get('alpha', 0.05)

        with open(path, 'w') as f:
            f.write("=" * 70 + "\n")
            f.write("ERP Statistical Analysis Summary\n")
            f.write("=" * 70 + "\n\n")

            for key, result in self.results.items():
                comp = result['component']
                dv_label = result['dv_label']
                units = result['units']

                f.write(f"\n{comp}: {dv_label} ({units})\n")
                f.write("-" * 50 + "\n")

                # ANOVA results
                if 'rm_anova' in result and 'error' not in result['rm_anova']:
                    anova = result['rm_anova']
                    f.write(f"\nRepeated-Measures ANOVA:\n")
                    f.write(f"  F({anova['df_num']}, {anova['df_denom']}) = {anova['F']:.3f}, ")
                    f.write(f"p = {anova['p_value']:.4f}, ")
                    f.write(f"ηp² = {anova['effect_size_np2']:.3f}\n")

                    if anova['p_value'] < alpha:
                        f.write(f"  *** Significant at α = {alpha} ***\n")

                # Pairwise results
                if 'pairwise' in result and 'error' not in result['pairwise']:
                    pw = result['pairwise']
                    f.write(f"\nPairwise Comparisons ({pw['correction_method']}):\n")
                    for comp_row in pw['table']:
                        f.write(f"  {comp_row['A']} vs {comp_row['B']}: ")
                        f.write(f"t = {comp_row['T']:.3f}, ")
                        f.write(f"p-adj = {comp_row['p-corr']:.4f}, ")
                        f.write(f"d = {comp_row['effsize']:.3f}\n")

                f.write("\n")

    def _write_csv_tables(self, output_dir: Path):
        """Write individual CSV tables for each test."""
        for key, result in self.results.items():
            # ANOVA table
            if 'rm_anova' in result and 'table' in result['rm_anova']:
                anova_df = pd.DataFrame(result['rm_anova']['table'])
                anova_path = output_dir / f"{key}_anova.csv"
                anova_df.to_csv(anova_path, index=False)

            # Pairwise table
            if 'pairwise' in result and 'table' in result['pairwise']:
                pw_df = pd.DataFrame(result['pairwise']['table'])
                pw_path = output_dir / f"{key}_pairwise.csv"
                pw_df.to_csv(pw_path, index=False)
```

### Implementation: `scripts/run_statistics.py`

```python
#!/usr/bin/env python
"""Run statistical analysis on subject-level ERP measurements.

This script loads subject-level data and runs YAML-configured statistical tests:
- Repeated-measures ANOVA
- Pairwise t-tests (post-hoc)
- Linear mixed-effects models

All parameters controlled via YAML configuration for reproducibility.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
import pandas as pd
import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from eeg.statistics import ERPStatistics


def load_stats_config(config_path: Path) -> dict:
    """Load statistical configuration from YAML."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run ERP statistical analysis")
    parser.add_argument("--config", required=True, help="Path to statistics YAML")
    parser.add_argument("--data", help="Path to subject_measurements.csv (auto-detected if not provided)")
    args = parser.parse_args()

    # Load configuration
    config = load_stats_config(Path(args.config))
    analysis_id = config.get('analysis_id')

    if not analysis_id:
        print("ERROR: analysis_id not specified in statistics config")
        return 1

    # Find subject measurements CSV
    if args.data:
        data_path = Path(args.data)
    else:
        # Auto-detect based on analysis_id
        data_path = Path(f"docs/assets/tables/{analysis_id}/subject_measurements.csv")

    if not data_path.exists():
        print(f"ERROR: Subject measurements file not found: {data_path}")
        print("Run the analysis pipeline first to generate subject-level data.")
        return 1

    print(f"\n{'='*70}")
    print(f"ERP Statistical Analysis: {analysis_id}")
    print(f"{'='*70}\n")

    # Load subject-level data
    print(f"Loading subject data: {data_path}")
    data = pd.read_csv(data_path)
    print(f"  Loaded {len(data)} measurements")
    print(f"  Subjects: {data['subject_id'].nunique()}")
    print(f"  Components: {', '.join(data['component'].unique())}")
    print(f"  Conditions: {', '.join(data['condition'].unique())}\n")

    # Initialize statistical analyzer
    stats = ERPStatistics(data, config)

    # Run all enabled tests
    print("Running statistical tests...")
    results = stats.run_all_tests()
    print(f"  Completed {len(results)} component × DV analyses\n")

    # Save results
    output_dir = Path(f"docs/assets/tables/{analysis_id}")
    stats.save_results(output_dir)

    print(f"\n{'='*70}")
    print(f"Statistical analysis complete!")
    print(f"Results saved to: {output_dir}")
    print(f"{'='*70}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
```

---

## Phase 2C: Statistical Visualization

### New Module: `src/eeg/stats_plots.py`

```python
"""Statistical visualization for ERP measurements."""
from __future__ import annotations

from typing import Dict, Any, List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def plot_condition_comparison(
    data: pd.DataFrame,
    dv: str,
    component: str,
    title: str,
    output_path: Path,
    plot_type: str = "boxplot",
    dpi: int = 300
):
    """
    Create condition comparison plot (boxplot, violin, or raincloud).

    Args:
        data: Subject-level measurements
        dv: Dependent variable name
        component: Component name
        title: Plot title
        output_path: Save path
        plot_type: "boxplot", "violin", or "raincloud"
        dpi: Plot resolution
    """
    # Filter data
    data_plot = data[data['component'] == component].copy()

    fig, ax = plt.subplots(figsize=(10, 6))

    if plot_type == "boxplot":
        sns.boxplot(
            data=data_plot,
            x='condition',
            y=dv,
            ax=ax,
            palette='Set2'
        )
        # Overlay individual points
        sns.stripplot(
            data=data_plot,
            x='condition',
            y=dv,
            ax=ax,
            color='black',
            alpha=0.3,
            size=4
        )

    elif plot_type == "violin":
        sns.violinplot(
            data=data_plot,
            x='condition',
            y=dv,
            ax=ax,
            palette='Set2',
            inner='box'
        )

    ax.set_title(title, fontsize=14, weight='bold')
    ax.set_xlabel('Condition', fontsize=12)
    ax.set_ylabel(f'{dv} (ms)' if 'latency' in dv else f'{dv} (µV)', fontsize=12)
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    fig.savefig(output_path, dpi=dpi, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {output_path.name}")


def plot_effect_sizes(
    results: Dict[str, Any],
    output_path: Path,
    dpi: int = 300
):
    """
    Plot effect sizes (Cohen's d) for pairwise comparisons.

    Args:
        results: Statistical results dictionary
        output_path: Save path
        dpi: Plot resolution
    """
    # Extract pairwise effect sizes
    plot_data = []
    for key, result in results.items():
        if 'pairwise' not in result:
            continue

        comp = result['component']
        for row in result['pairwise']['table']:
            plot_data.append({
                'component': comp,
                'comparison': f"{row['A']} vs {row['B']}",
                'effect_size': row['effsize'],
                'significant': row['p-corr'] < 0.05
            })

    if not plot_data:
        print("  No pairwise data to plot")
        return

    df = pd.DataFrame(plot_data)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar plot with color by significance
    colors = ['#d62728' if sig else '#7f7f7f' for sig in df['significant']]

    ax.barh(df['comparison'], df['effect_size'], color=colors, alpha=0.7)
    ax.axvline(0, color='black', linestyle='-', linewidth=0.8)
    ax.axvline(0.2, color='gray', linestyle='--', linewidth=0.6, alpha=0.5)
    ax.axvline(-0.2, color='gray', linestyle='--', linewidth=0.6, alpha=0.5)
    ax.axvline(0.5, color='gray', linestyle=':', linewidth=0.6, alpha=0.5)
    ax.axvline(-0.5, color='gray', linestyle=':', linewidth=0.6, alpha=0.5)

    ax.set_xlabel("Effect Size (Cohen's d)", fontsize=12)
    ax.set_title("Pairwise Effect Sizes", fontsize=14, weight='bold')
    ax.grid(axis='x', alpha=0.3)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#d62728', alpha=0.7, label='p < 0.05'),
        Patch(facecolor='#7f7f7f', alpha=0.7, label='n.s.')
    ]
    ax.legend(handles=legend_elements, loc='lower right')

    plt.tight_layout()
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {output_path.name}")
```

---

## Phase 2: Environment Updates

### Add to `environment.yml`

```yaml
dependencies:
  - python=3.12
  - mne==1.10.1
  - numpy==2.1.*
  - pandas==2.2.*
  - matplotlib==3.8.*
  - scipy==1.12.*
  - pyyaml==6.0.*
  - pytest==8.*
  - pingouin  # NEW: For repeated-measures ANOVA
  - statsmodels  # NEW: For linear mixed models
  - seaborn  # NEW: For statistical plots
  - jupyter
  - ipython
  - pip
  - pip:
    - mne-qt-browser
```

---

## Phase 2: Testing Strategy

### Test File: `tests/test_statistics.py`

```python
"""Tests for statistical analysis module."""
import pytest
import numpy as np
import pandas as pd
from eeg.statistics import ERPStatistics


class TestERPStatistics:
    """Test suite for ERP statistical analysis."""

    @pytest.fixture
    def sample_data(self):
        """Generate sample subject-level data."""
        np.random.seed(42)
        n_subjects = 20
        conditions = ['Cond1', 'Cond2', 'Cond3']

        data = []
        for subj_id in range(1, n_subjects + 1):
            for cond in conditions:
                # Simulate latency effect: Cond3 > Cond2 > Cond1
                latency_base = 170
                if cond == 'Cond2':
                    latency_base += 3
                elif cond == 'Cond3':
                    latency_base += 6

                data.append({
                    'subject_id': f'sub-{subj_id:02d}',
                    'component': 'N1',
                    'condition': cond,
                    'latency_frac_area_ms': latency_base + np.random.randn() * 2,
                    'mean_amplitude_roi': -3.0 + np.random.randn() * 0.5,
                })

        return pd.DataFrame(data)

    @pytest.fixture
    def sample_config(self):
        """Sample statistical configuration."""
        return {
            'components': ['N1'],
            'dependent_variables': [
                {'name': 'latency_frac_area_ms', 'label': 'Latency', 'units': 'ms'}
            ],
            'tests': {
                'repeated_measures_anova': {
                    'enabled': True,
                    'within': 'condition',
                    'subject': 'subject_id'
                },
                'pairwise_tests': {
                    'enabled': True,
                    'padjust': 'fdr_bh',
                    'alpha': 0.05
                },
                'linear_mixed_model': {
                    'enabled': True,
                    'formula': 'latency_frac_area_ms ~ C(condition)',
                    'groups': 'subject_id'
                }
            },
            'outputs': {'save_json': False, 'save_txt': False, 'save_csv': False}
        }

    def test_rm_anova_detects_effect(self, sample_data, sample_config):
        """Test that RM-ANOVA detects simulated effect."""
        stats = ERPStatistics(sample_data, sample_config)
        results = stats.run_all_tests()

        # Should find significant effect (simulated data has condition differences)
        anova = results['N1_latency_frac_area_ms']['rm_anova']
        assert 'error' not in anova
        assert anova['p_value'] < 0.05, "Should detect condition effect"
        assert anova['F'] > 1.0

    def test_pairwise_tests_run(self, sample_data, sample_config):
        """Test that pairwise tests execute without error."""
        stats = ERPStatistics(sample_data, sample_config)
        results = stats.run_all_tests()

        pw = results['N1_latency_frac_area_ms']['pairwise']
        assert 'error' not in pw
        assert pw['n_comparisons'] == 3  # 3 conditions = 3 pairwise tests

    def test_lmm_runs(self, sample_data, sample_config):
        """Test that linear mixed model runs."""
        stats = ERPStatistics(sample_data, sample_config)
        results = stats.run_all_tests()

        lmm = results['N1_latency_frac_area_ms']['lmm']
        assert 'error' not in lmm
        assert lmm['converged'] is True
        assert 'aic' in lmm
        assert 'parameters' in lmm
```

---

## Phase 2: Usage Workflow

### Step 1: Run Analysis (collects subject data)
```bash
python scripts/run_analysis.py --config configs/analyses/cardinality_within_small.yaml
# Outputs: subject_measurements.csv + condition_measurements.csv
```

### Step 2: Configure Statistics
```bash
# Edit or create statistics config
cp configs/statistics/default.yaml configs/statistics/cardinality_stats.yaml
# Edit analysis_id, components, tests as needed
```

### Step 3: Run Statistical Analysis
```bash
python scripts/run_statistics.py --config configs/statistics/cardinality_stats.yaml
# Outputs: statistics.json, stats_summary.txt, anova/pairwise CSVs, plots
```

### Step 4: Review Results
```bash
# Read human-readable summary
cat docs/assets/tables/cardinality_within_small/stats_summary.txt

# Or load JSON for programmatic access
python -c "import json; print(json.load(open('docs/assets/tables/cardinality_within_small/statistics.json')))"
```

---

## Phase 2: Implementation Checklist

### Phase 2A: Subject-Level Data Collection
- [ ] Modify `run_analysis.py` to collect subject measurements
- [ ] Add CSV export for `subject_measurements.csv`
- [ ] Test on `landing_on_2` analysis
- [ ] Verify output structure

### Phase 2B: Statistical Testing
- [ ] Create `src/eeg/statistics.py` module
- [ ] Implement `ERPStatistics` class
  - [ ] Repeated-measures ANOVA
  - [ ] Pairwise t-tests with correction
  - [ ] Linear mixed-effects models
- [ ] Create `scripts/run_statistics.py` CLI
- [ ] Create default statistics YAML configs
- [ ] Write `tests/test_statistics.py`
- [ ] Add `pingouin` and `statsmodels` to environment
- [ ] Test on real data

### Phase 2C: Visualization
- [ ] Create `src/eeg/stats_plots.py`
- [ ] Implement boxplot, violin plot functions
- [ ] Implement effect size visualization
- [ ] Integrate plotting into `run_statistics.py`
- [ ] Test plot generation

### Documentation
- [ ] Update README with Phase 2 usage
- [ ] Create `STATISTICS_GUIDE.md`
- [ ] Add example YAML configurations
- [ ] Document interpretation guidelines

---

## Success Criteria

Phase 2 is complete when:
1. ✅ Subject-level measurements collected for all analyses
2. ✅ All three statistical tests run successfully
3. ✅ Results configurable via YAML
4. ✅ Output includes JSON, TXT, and CSV
5. ✅ Statistical plots generated automatically
6. ✅ All tests pass (17 existing + new stats tests)
7. ✅ Documentation updated
8. ✅ Validated on real ERP data

---

## Timeline Estimate

**Phase 2A**: 2-3 hours (subject-level collection)
**Phase 2B**: 4-6 hours (statistical module + tests)
**Phase 2C**: 2-3 hours (visualization)
**Documentation**: 1-2 hours

**Total**: ~10-14 hours of focused implementation

---

**Ready to implement Phase 2A first?**

I can start with subject-level measurement collection, which is the foundation for everything else.
