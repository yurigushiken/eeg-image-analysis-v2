#!/usr/bin/env python
"""
Run statistical analyses on subject-level ERP measurements (Phase 2B).

This script reads subject_measurements.csv (from Phase 2A) and performs
statistical tests according to a YAML configuration file.

Usage:
    python scripts/run_statistics.py --config configs/statistics/default.yaml

The script performs:
- Repeated-measures ANOVA
- Pairwise t-tests with multiple comparison correction
- Linear Mixed-Effects Models (LMM)
- Descriptive statistics

All results are saved to the configured output directory.
"""

import argparse
import sys
from pathlib import Path
import yaml
import json
import time

# Add src to path
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "src"))

from eeg.statistics import ERPStatistics, get_library_versions, format_missing_data_policy, compute_cohens_d_ci
from eeg.stats_plots import plot_boxplot, plot_violin, plot_effect_sizes
from eeg.summary_report import StatisticalReportGenerator
import pandas as pd


def load_config(config_path: Path) -> dict:
    """Load YAML configuration file."""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def print_header(text: str, level: int = 1):
    """Print formatted header."""
    if level == 1:
        print(f"\n{'=' * 80}")
        print(f"  {text}")
        print(f"{'=' * 80}\n")
    elif level == 2:
        print(f"\n{'-' * 80}")
        print(f"  {text}")
        print(f"{'-' * 80}\n")
    else:
        print(f"\n{text}")


def generate_plots(stats: ERPStatistics, cfg: dict, output_dir: Path):
    """Generate all enabled plots (Phase 2C)."""
    if not cfg.get('plots', {}).get('enabled', False):
        return

    print_header("Generating Plots (Phase 2C)", level=1)

    plots_cfg = cfg['plots']
    plots_dir = output_dir / plots_cfg.get('plots_subdir', 'plots')
    plots_dir.mkdir(parents=True, exist_ok=True)

    # Get plot styling
    dpi = plots_cfg.get('dpi', 300)
    figsize = tuple(plots_cfg.get('figsize', [8, 6]))

    for component in cfg['components']:
        for dv in cfg['dependent_variables']:
            print(f"  Plotting: {component} - {dv}")

            try:
                # Filter data for this component
                comp_data = stats.filter_data(component=component, **cfg.get('filters', {}))

                if len(comp_data) == 0:
                    print(f"    [SKIPPED] No data after filtering")
                    continue

                # Get measurement window info (if available)
                window_start = comp_data['window_start_ms'].iloc[0] if 'window_start_ms' in comp_data.columns else None
                window_end = comp_data['window_end_ms'].iloc[0] if 'window_end_ms' in comp_data.columns else None
                peak_lat = comp_data['peak_latency_ms'].iloc[0] if 'peak_latency_ms' in comp_data.columns else None
                fwhm = comp_data['fwhm_ms'].iloc[0] if 'fwhm_ms' in comp_data.columns else None

                # Boxplot
                if plots_cfg.get('boxplot', {}).get('enabled', True):
                    boxplot_path = plots_dir / f"boxplot_{component}_{dv}.png"
                    plot_boxplot(
                        data=comp_data,
                        dv=dv,
                        groupby='condition',
                        title=f'{component} {dv.replace("_", " ").title()}',
                        output_path=boxplot_path,
                        component=component,
                        window_start_ms=window_start,
                        window_end_ms=window_end,
                        peak_latency_ms=peak_lat,
                        fwhm_ms=fwhm,
                        include_window_context=plots_cfg.get('boxplot', {}).get('include_window_context', True),
                        show_points=plots_cfg.get('boxplot', {}).get('show_points', True),
                        show_mean=plots_cfg.get('boxplot', {}).get('show_mean', True),
                        dpi=dpi,
                        figsize=figsize
                    )

                # Violin plot
                if plots_cfg.get('violin', {}).get('enabled', True):
                    violin_path = plots_dir / f"violin_{component}_{dv}.png"
                    plot_violin(
                        data=comp_data,
                        dv=dv,
                        groupby='condition',
                        title=f'{component} {dv.replace("_", " ").title()}',
                        output_path=violin_path,
                        component=component,
                        window_start_ms=window_start,
                        window_end_ms=window_end,
                        peak_latency_ms=peak_lat,
                        fwhm_ms=fwhm,
                        include_window_context=plots_cfg.get('violin', {}).get('include_window_context', True),
                        inner=plots_cfg.get('violin', {}).get('inner', 'box'),
                        dpi=dpi,
                        figsize=figsize
                    )

            except Exception as e:
                print(f"    ERROR: {e}")

    # Effect size plots (after pairwise tests)
    if plots_cfg.get('effect_size', {}).get('enabled', True):
        print("\n  Generating effect size plots...")
        for component in cfg['components']:
            for dv in cfg['dependent_variables']:
                pairwise_csv = output_dir / f"pairwise_{component}_{dv}.csv"
                if pairwise_csv.exists():
                    try:
                        pairwise_data = pd.read_csv(pairwise_csv)

                        # Check if effect size column exists (skip if pairwise test failed)
                        if 'cohen' not in pairwise_data.columns and 'hedges' not in pairwise_data.columns:
                            print(f"    [SKIPPED] {component}-{dv}: No effect size data (insufficient paired samples)")
                            continue

                        effect_plot_path = plots_dir / f"effect_sizes_{component}_{dv}.png"

                        plot_effect_sizes(
                            pairwise_results=pairwise_data,
                            output_path=effect_plot_path,
                            title=f'{component} {dv.replace("_", " ").title()} - Effect Sizes',
                            show_ci=plots_cfg.get('effect_size', {}).get('show_ci', True),
                            threshold_lines=plots_cfg.get('effect_size', {}).get('threshold_lines'),
                            threshold_labels=plots_cfg.get('effect_size', {}).get('threshold_labels'),
                            dpi=dpi,
                            figsize=figsize
                        )
                    except Exception as e:
                        print(f"    ERROR plotting {component}-{dv}: {e}")


def add_effect_size_cis_to_pairwise(stats: ERPStatistics, result: pd.DataFrame, cfg: dict, component: str, dv: str) -> pd.DataFrame:
    """Add 95% confidence intervals to pairwise test results (Phase 2C - IA #4)."""
    reporting_cfg = cfg.get('reporting', {})

    if not reporting_cfg.get('include_effect_size_ci', True):
        return result

    # Add CI columns if they don't exist
    if 'ci_lower' not in result.columns:
        ci_lowers = []
        ci_uppers = []

        for idx, row in result.iterrows():
            # Get the two conditions being compared
            cond_a = row['A']
            cond_b = row['B']

            # Check if this is a paired test (within-subjects)
            is_paired = row.get('Paired', True)  # Default to paired for within-subjects

            # Get data for both conditions (filtered by component)
            comp_data = stats.filter_data(component=component, **cfg.get('filters', {}))

            if is_paired:
                # For paired data, we need matched pairs by subject
                # Pivot to get one row per subject with columns for each condition
                pivoted = comp_data.pivot(index='subject_id', columns='condition', values=dv)

                # Get the paired values
                if cond_a in pivoted.columns and cond_b in pivoted.columns:
                    # Drop rows where either value is missing
                    paired_data = pivoted[[cond_a, cond_b]].dropna()
                    data_a = paired_data[cond_a].values
                    data_b = paired_data[cond_b].values

                    if len(data_a) > 1:
                        d, ci_lower, ci_upper = compute_cohens_d_ci(data_a, data_b, paired=True)
                        ci_lowers.append(ci_lower)
                        ci_uppers.append(ci_upper)
                    else:
                        ci_lowers.append(float('nan'))
                        ci_uppers.append(float('nan'))
                else:
                    ci_lowers.append(float('nan'))
                    ci_uppers.append(float('nan'))
            else:
                # Independent samples (rare in ERP studies, but handle it)
                data_a = comp_data[comp_data['condition'] == cond_a][dv].dropna().values
                data_b = comp_data[comp_data['condition'] == cond_b][dv].dropna().values

                if len(data_a) > 1 and len(data_b) > 1:
                    d, ci_lower, ci_upper = compute_cohens_d_ci(data_a, data_b, paired=False)
                    ci_lowers.append(ci_lower)
                    ci_uppers.append(ci_upper)
                else:
                    ci_lowers.append(float('nan'))
                    ci_uppers.append(float('nan'))

        result['ci_lower'] = ci_lowers
        result['ci_upper'] = ci_uppers

    return result


def run_anova_tests(stats: ERPStatistics, cfg: dict, output_dir: Path):
    """Run ANOVA tests for all components and DVs."""
    print_header("Running Repeated-Measures ANOVA", level=1)

    anova_cfg = cfg['tests']['anova']
    if not anova_cfg['enabled']:
        print("  [SKIPPED] ANOVA disabled in config")
        return {}

    results = {}

    for component in cfg['components']:
        for dv in cfg['dependent_variables']:
            print(f"  Testing: {component} - {dv}")

            try:
                result = stats.run_anova(
                    dv=dv,
                    component=component,
                    within=anova_cfg['within'],
                    subject=anova_cfg['subject'],
                    **cfg.get('filters', {})
                )

                # Save result
                output_filename = f"anova_{component}_{dv}.{anova_cfg['output_format']}"
                output_path = output_dir / output_filename
                stats.save_results(result, output_path, format=anova_cfg['output_format'])

                # Store for summary
                key = f"{component}_{dv}"
                within_row = result.loc[result['Source'] == anova_cfg['within']]

                # Pingouin uses 'ng2' for generalized eta-squared (Phase 2C - IA #4)
                effect_size_col = 'ng2' if 'ng2' in result.columns else 'np2' if 'np2' in result.columns else None

                results[key] = {
                    'component': component,
                    'dv': dv,
                    'test': 'ANOVA',
                    'F': float(within_row['F'].values[0]),
                    'p_unc': float(within_row['p-unc'].values[0]),
                    'output_file': str(output_filename)
                }

                # Add Greenhouse-Geisser correction if available (Phase 2C - IA #1)
                reporting_cfg = cfg.get('reporting', {})
                if reporting_cfg.get('include_gg_correction', True):
                    if 'p-GG-corr' in within_row.columns:
                        results[key]['p_gg_corrected'] = float(within_row['p-GG-corr'].values[0])
                    if 'eps' in within_row.columns:
                        results[key]['epsilon'] = float(within_row['eps'].values[0])

                # Add effect size
                if effect_size_col:
                    results[key]['effect_size_ng2'] = float(within_row[effect_size_col].values[0])

                # Print to console if enabled
                if cfg['output']['print_to_console']:
                    print(result.to_string(index=False))
                    print()

            except Exception as e:
                print(f"    ERROR: {e}")
                results[f"{component}_{dv}"] = {'error': str(e)}

    return results


def run_pairwise_tests(stats: ERPStatistics, cfg: dict, output_dir: Path):
    """Run pairwise t-tests for all components and DVs."""
    print_header("Running Pairwise T-Tests", level=1)

    pairwise_cfg = cfg['tests']['pairwise']
    if not pairwise_cfg['enabled']:
        print("  [SKIPPED] Pairwise tests disabled in config")
        return {}

    results = {}

    for component in cfg['components']:
        for dv in cfg['dependent_variables']:
            print(f"  Testing: {component} - {dv}")

            try:
                result = stats.run_pairwise_tests(
                    dv=dv,
                    component=component,
                    within=pairwise_cfg['within'],
                    subject=pairwise_cfg['subject'],
                    padjust=pairwise_cfg['correction'],
                    effsize=pairwise_cfg['effsize'],
                    **cfg.get('filters', {})
                )

                # Add effect size CIs if enabled (Phase 2C - IA #4)
                result = add_effect_size_cis_to_pairwise(stats, result, cfg, component, dv)

                # Save result with CIs
                output_filename = f"pairwise_{component}_{dv}.{pairwise_cfg['output_format']}"
                output_path = output_dir / output_filename
                stats.save_results(result, output_path, format=pairwise_cfg['output_format'])

                # Store for summary (significant comparisons only)
                key = f"{component}_{dv}"
                alpha = cfg['advanced']['alpha']
                sig_comparisons = result[result['p-corr'] < alpha] if 'p-corr' in result.columns else result[result['p-unc'] < alpha]

                results[key] = {
                    'component': component,
                    'dv': dv,
                    'test': 'Pairwise',
                    'n_comparisons': len(result),
                    'n_significant': len(sig_comparisons),
                    'correction': pairwise_cfg['correction'],
                    'output_file': str(output_filename)
                }

                # Print to console if enabled
                if cfg['output']['print_to_console']:
                    print(result.to_string(index=False))
                    print(f"\n  Significant comparisons (alpha={alpha}): {len(sig_comparisons)}/{len(result)}\n")

            except Exception as e:
                print(f"    ERROR: {e}")
                results[f"{component}_{dv}"] = {'error': str(e)}

    return results


def run_lmm_tests(stats: ERPStatistics, cfg: dict, output_dir: Path):
    """Run Linear Mixed-Effects Models for all components and DVs."""
    print_header("Running Linear Mixed-Effects Models", level=1)

    lmm_cfg = cfg['tests']['lmm']
    if not lmm_cfg['enabled']:
        print("  [SKIPPED] LMM disabled in config")
        return {}

    results = {}

    for component in cfg['components']:
        for dv in cfg['dependent_variables']:
            print(f"  Testing: {component} - {dv}")

            try:
                # LMM handles dropna internally, so only pass min_snr
                lmm_filters = {k: v for k, v in cfg.get('filters', {}).items() if k != 'dropna'}
                result = stats.run_lmm(
                    dv=dv,
                    component=component,
                    fixed=lmm_cfg['fixed'],
                    random=lmm_cfg['random'],
                    **lmm_filters
                )

                # Save result
                output_filename = f"lmm_{component}_{dv}.{lmm_cfg['output_format']}"
                output_path = output_dir / output_filename
                stats.save_results(result, output_path, format=lmm_cfg['output_format'])

                # Store for summary
                key = f"{component}_{dv}"
                results[key] = {
                    'component': component,
                    'dv': dv,
                    'test': 'LMM',
                    'aic': float(result['aic']),
                    'bic': float(result['bic']),
                    'converged': result['converged'],
                    'output_file': str(output_filename)
                }

                # Print to console if enabled
                if cfg['output']['print_to_console']:
                    print(result['summary'])
                    print(f"\n  AIC: {result['aic']:.2f}, BIC: {result['bic']:.2f}")
                    print(f"  Converged: {result['converged']}\n")

            except Exception as e:
                print(f"    ERROR: {e}")
                results[f"{component}_{dv}"] = {'error': str(e)}

    return results


def run_descriptive_stats(stats: ERPStatistics, cfg: dict, output_dir: Path):
    """Compute descriptive statistics for all components and DVs."""
    print_header("Computing Descriptive Statistics", level=1)

    desc_cfg = cfg['descriptives']
    if not desc_cfg['enabled']:
        print("  [SKIPPED] Descriptives disabled in config")
        return

    for component in cfg['components']:
        for dv in cfg['dependent_variables']:
            print(f"  Computing: {component} - {dv}")

            try:
                result = stats.get_descriptives(
                    dv=dv,
                    component=component,
                    groupby=desc_cfg['groupby'],
                    **cfg.get('filters', {})
                )

                # Save result
                output_filename = f"descriptives_{component}_{dv}.{desc_cfg['output_format']}"
                output_path = output_dir / output_filename
                stats.save_results(result.reset_index(), output_path, format=desc_cfg['output_format'])

                # Print to console if enabled
                if cfg['output']['print_to_console']:
                    print(result.to_string())
                    print()

            except Exception as e:
                print(f"    ERROR: {e}")


def create_summary_report(all_results: dict, cfg: dict, output_dir: Path, stats: ERPStatistics):
    """Create enhanced summary report with Phase 2C refinements."""
    print_header("Creating Enhanced Summary Report (Phase 2C)", level=1)

    if not cfg['output']['create_summary']:
        print("  [SKIPPED] Summary disabled in config")
        return

    reporting_cfg = cfg.get('reporting', {})

    summary = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'analysis_id': Path(cfg['input_csv']).parent.parent.name,  # e.g., "landing_on_2"
        'config_file': str(cfg.get('_config_path', 'unknown')),
        'input_csv': cfg['input_csv'],
        'components_tested': cfg['components'],
        'dependent_variables': cfg['dependent_variables'],
    }

    # Phase 2C Enhancement: Library versions (IA #3)
    if reporting_cfg.get('include_library_versions', True):
        print("  Including library versions...")
        summary['library_versions'] = get_library_versions()

    # Phase 2C Enhancement: Analysis settings (IA #5)
    if reporting_cfg.get('document_measurement_windows', True):
        print("  Documenting measurement window methodology...")
        # Infer measurement modes from selected dependent variables (stats perspective)
        dvs = cfg.get('dependent_variables', [])
        latency_measure = (
            'peak' if 'peak_latency_ms' in dvs else
            'fal_50' if 'latency_frac_area_ms' in dvs else
            'unspecified'
        )
        amplitude_measure = (
            'peak' if 'peak_amplitude_roi' in dvs else
            'mean' if 'mean_amplitude_roi' in dvs else
            'unspecified'
        )

        summary['analysis_settings'] = {
            'measurement_window_method': 'collapsed_localizer_fwhm',
            'fal_fraction': 0.5,  # Fractional area latency: 50% = temporal midpoint
            'latency_measure': latency_measure,
            'amplitude_measure': amplitude_measure,
            'filters': cfg.get('filters', {}),
            'baseline_period_ms': '[-100, 0]',  # Standard baseline
        }

    # Phase 2C Enhancement: Correction family (IA #2)
    summary['correction_family'] = cfg.get('correction_family', 'component')

    # Phase 2C Enhancement: Missing data policy (IA #6)
    if reporting_cfg.get('document_missing_data', True):
        print("  Generating missing data policy statement...")
        summary['missing_data_policy'] = format_missing_data_policy(
            filters=cfg.get('filters', {}),
            test_type="ANOVA and pairwise tests"
        )

    # Sample size information
    summary['data_summary'] = {
        'n_total_measurements': len(stats.data),
        'n_subjects': stats.data['subject_id'].nunique() if 'subject_id' in stats.data.columns else 'unknown',
        'n_conditions': stats.data['condition'].nunique() if 'condition' in stats.data.columns else 'unknown'
    }

    # Tests run
    summary['tests_run'] = {
        'anova': cfg['tests']['anova']['enabled'],
        'pairwise': cfg['tests']['pairwise']['enabled'],
        'lmm': cfg['tests']['lmm']['enabled'],
        'descriptives': cfg['descriptives']['enabled']
    }

    # Results
    summary['results'] = all_results

    # Save enhanced summary
    summary_path = output_dir / cfg['output']['summary_filename']
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"  Enhanced summary saved to: {summary_path}\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run statistical analyses on subject-level ERP measurements",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--config',
        type=Path,
        default=Path('configs/statistics/default.yaml'),
        help='Path to YAML configuration file'
    )

    args = parser.parse_args()

    # Load configuration
    if not args.config.exists():
        print(f"ERROR: Config file not found: {args.config}")
        sys.exit(1)

    cfg = load_config(args.config)
    cfg['_config_path'] = str(args.config)  # Store for summary

    print_header("ERP Statistical Analysis (Phase 2B)", level=1)
    print(f"Config: {args.config}")
    print(f"Input:  {cfg['input_csv']}")
    print(f"Output: {cfg['output_dir']}\n")

    # Resolve paths relative to repo root
    input_csv = repo_root / cfg['input_csv']
    output_dir = repo_root / cfg['output_dir']

    # Check input file exists
    if not input_csv.exists():
        print(f"ERROR: Input CSV not found: {input_csv}")
        print("  Run Phase 2A analysis first to generate subject measurements.")
        sys.exit(1)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize statistics class
    print("Loading data...")
    stats = ERPStatistics(input_csv)
    print(f"  Loaded {len(stats.data)} subject-level measurements\n")

    # Apply filters if specified
    filters = cfg.get('filters', {})
    if filters.get('min_snr'):
        print(f"  Applying SNR filter: min_snr >= {filters['min_snr']}")

    # Run all enabled tests
    all_results = {}

    if cfg['tests']['anova']['enabled']:
        anova_results = run_anova_tests(stats, cfg, output_dir)
        all_results['anova'] = anova_results

    if cfg['tests']['pairwise']['enabled']:
        pairwise_results = run_pairwise_tests(stats, cfg, output_dir)
        all_results['pairwise'] = pairwise_results

    if cfg['tests']['lmm']['enabled']:
        lmm_results = run_lmm_tests(stats, cfg, output_dir)
        all_results['lmm'] = lmm_results

    if cfg['descriptives']['enabled']:
        run_descriptive_stats(stats, cfg, output_dir)

    # Generate plots (Phase 2C)
    if cfg.get('plots', {}).get('enabled', False):
        generate_plots(stats, cfg, output_dir)

    # Create enhanced summary report (Phase 2C)
    if cfg['output']['create_summary']:
        create_summary_report(all_results, cfg, output_dir, stats)

    # Generate narrative statistical report
    print_header("Generating Narrative Report", level=1)
    try:
        analysis_id = Path(cfg['input_csv']).parent.parent.name
        report_gen = StatisticalReportGenerator(output_dir, analysis_id)
        report_path = output_dir / "STATISTICAL_REPORT.md"
        report_gen.generate_report(report_path)
        print(f"  Narrative report saved to: {report_path}")
        print(f"  This report synthesizes all statistical outputs into a publication-ready format.\n")
    except Exception as e:
        print(f"  WARNING: Could not generate narrative report: {e}\n")

    print_header("Analysis Complete!", level=1)
    print(f"  Results saved to: {output_dir}\n")

    # Summary of outputs
    if cfg.get('plots', {}).get('enabled', False):
        plots_dir = output_dir / cfg['plots'].get('plots_subdir', 'plots')
        print(f"  Plots saved to: {plots_dir}\n")


if __name__ == "__main__":
    main()
