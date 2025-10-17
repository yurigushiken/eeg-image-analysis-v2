"""
Generate comprehensive statistical reports for ERP analyses.

This module creates publication-ready narrative reports that synthesize
all statistical outputs (descriptives, ANOVA, pairwise, LMM) into a
readable format suitable for researchers and publication.
"""

from pathlib import Path
import json
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class StatisticalReportGenerator:
    """
    Generate narrative statistical reports from Phase 2B/2C outputs.

    This class reads all statistical outputs from a single analysis
    and creates a comprehensive markdown report with:
    - Analysis overview and methods
    - Descriptive statistics
    - Inferential statistics (ANOVA, pairwise, LMM)
    - Effect sizes and interpretations
    - Quality control metrics
    - Embedded visualizations
    """

    def __init__(self, stats_dir: Path, analysis_id: str):
        """
        Initialize report generator.

        Parameters
        ----------
        stats_dir : Path
            Path to stats directory (e.g., docs/assets/stats/13_31/)
        analysis_id : str
            Analysis identifier (e.g., "13_31")
        """
        self.stats_dir = Path(stats_dir)
        self.analysis_id = analysis_id
        self.components = []
        self.conditions = []
        self.summary_data = None

        # Load summary if available
        summary_path = self.stats_dir / "statistical_summary.json"
        if summary_path.exists():
            with open(summary_path, 'r') as f:
                self.summary_data = json.load(f)
                self.components = self.summary_data.get('components_tested', [])

    def _load_descriptives(self, component: str, measure: str) -> Optional[pd.DataFrame]:
        """Load descriptive statistics CSV."""
        desc_path = self.stats_dir / f"descriptives_{component}_{measure}.csv"
        if desc_path.exists():
            return pd.read_csv(desc_path)
        return None

    def _load_lmm_results(self, component: str, measure: str) -> Optional[Dict]:
        """Load LMM results JSON."""
        lmm_path = self.stats_dir / f"lmm_{component}_{measure}.json"
        if lmm_path.exists():
            with open(lmm_path, 'r') as f:
                return json.load(f)
        return None

    def _load_anova_results(self, component: str, measure: str) -> Optional[pd.DataFrame]:
        """Load ANOVA results CSV."""
        anova_path = self.stats_dir / f"anova_{component}_{measure}.csv"
        if anova_path.exists():
            return pd.read_csv(anova_path)
        return None

    def _load_pairwise_results(self, component: str, measure: str) -> Optional[pd.DataFrame]:
        """Load pairwise test results CSV."""
        pairwise_path = self.stats_dir / f"pairwise_{component}_{measure}.csv"
        if pairwise_path.exists():
            return pd.read_csv(pairwise_path)
        return None

    def _format_p_value(self, p: float) -> str:
        """Format p-value in APA style."""
        if pd.isna(p):
            return "n/a"
        if p < 0.001:
            return "< .001"
        elif p < 0.01:
            return f"= {p:.3f}"
        else:
            return f"= {p:.3f}"

    def _format_effect_size(self, d: float) -> Tuple[str, str]:
        """
        Format effect size with interpretation.

        Returns
        -------
        value : str
            Formatted effect size value
        interpretation : str
            Textual interpretation (small/medium/large)
        """
        if pd.isna(d):
            return "n/a", "n/a"

        abs_d = abs(d)
        if abs_d < 0.2:
            interp = "negligible"
        elif abs_d < 0.5:
            interp = "small"
        elif abs_d < 0.8:
            interp = "medium"
        else:
            interp = "large"

        return f"{d:.2f}", interp

    def _format_statistic(self, stat_name: str, value: float, df: Optional[float] = None) -> str:
        """Format test statistic in APA style."""
        if pd.isna(value):
            return "n/a"

        if df is not None and not pd.isna(df):
            return f"{stat_name}({df:.0f}) = {value:.2f}"
        else:
            return f"{stat_name} = {value:.2f}"

    def _generate_header(self) -> str:
        """Generate report header."""
        lines = [
            f"# Statistical Analysis Report: {self.analysis_id}",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "---",
            ""
        ]
        return "\n".join(lines)

    def _generate_overview_section(self) -> str:
        """Generate analysis overview section."""
        lines = [
            "## 1. Analysis Overview",
            ""
        ]

        if self.summary_data:
            # Sample size info
            data_summary = self.summary_data.get('data_summary', {})
            lines.extend([
                f"**Total Measurements:** {data_summary.get('n_total_measurements', 'N/A')}",
                f"**Number of Subjects:** {data_summary.get('n_subjects', 'N/A')}",
                f"**Number of Conditions:** {data_summary.get('n_conditions', 'N/A')}",
                "",
                f"**Components Analyzed:** {', '.join(self.components)}",
                # Dynamic DV names based on summary metadata
                self._format_dependent_variables_line(),
                ""
            ])

            # Analysis settings
            settings = self.summary_data.get('analysis_settings', {})
            if settings:
                # Determine human-readable latency and amplitude methods
                latency_method = settings.get('latency_measure')
                if latency_method == 'peak':
                    latency_line = "Peak latency within FWHM window"
                elif latency_method == 'fal_50':
                    latency_line = f"{settings.get('fal_fraction', 0.5)*100:.0f}% Fractional Area Latency (temporal midpoint)"
                else:
                    latency_line = f"{settings.get('fal_fraction', 0.5)*100:.0f}% Fractional Area Latency (temporal midpoint)"

                amplitude_method = settings.get('amplitude_measure')
                if amplitude_method == 'peak':
                    amplitude_line = "Peak amplitude within FWHM window"
                elif amplitude_method == 'mean':
                    amplitude_line = "Mean amplitude in ROI within FWHM window"
                else:
                    amplitude_line = "Mean amplitude in ROI within FWHM window"

                lines.extend([
                    "### 1.1 Measurement Methodology",
                    "",
                    f"- **Component Detection:** {settings.get('measurement_window_method', 'N/A')}",
                    f"- **Latency Measure:** {latency_line}",
                    f"- **Amplitude Measure:** {amplitude_line}",
                    f"- **Baseline Period:** {settings.get('baseline_period_ms', 'N/A')} ms",
                    ""
                ])

                # QC filters
                filters = settings.get('filters', {})
                if filters:
                    lines.extend([
                        "### 1.2 Quality Control Filters",
                        ""
                    ])
                    if 'min_snr' in filters:
                        lines.append(f"- **Minimum SNR:** ≥ {filters['min_snr']}")
                    if filters.get('dropna', False):
                        lines.append("- **Missing Data:** Excluded listwise for ANOVA/pairwise")
                    lines.append("")

            # Missing data policy
            missing_policy = self.summary_data.get('missing_data_policy')
            if missing_policy:
                lines.extend([
                    "### 1.3 Missing Data Policy",
                    "",
                    missing_policy,
                    ""
                ])

        lines.append("---\n")
        return "\n".join(lines)

    def _generate_descriptives_section(self) -> str:
        """Generate descriptive statistics section."""
        lines = [
            "## 2. Descriptive Statistics",
            "",
            "This section presents means, standard deviations, and sample sizes for each condition.",
            ""
        ]

        measures = self._get_declared_measures()

        for component in self.components:
            lines.extend([
                f"### 2.{self.components.index(component)+1} {component} Component",
                ""
            ])

            for measure_key, measure_name, unit in measures:
                desc_df = self._load_descriptives(component, measure_key)

                if desc_df is not None and len(desc_df) > 0:
                    lines.extend([
                        f"#### {measure_name}",
                        ""
                    ])

                    # Create formatted table
                    lines.append("| Condition | N | Mean | SD | SEM | Range |")
                    lines.append("|-----------|---|------|----|----|-------|")

                    for _, row in desc_df.iterrows():
                        condition = row['condition']
                        n = int(row['count']) if not pd.isna(row['count']) else 0
                        mean = row['mean']
                        sd = row['std']
                        sem = row['sem']
                        min_val = row['min']
                        max_val = row['max']

                        # Format values
                        mean_str = f"{mean:.2f}" if not pd.isna(mean) else "n/a"
                        sd_str = f"{sd:.2f}" if not pd.isna(sd) else "n/a"
                        sem_str = f"{sem:.2f}" if not pd.isna(sem) else "n/a"
                        range_str = f"[{min_val:.2f}, {max_val:.2f}]" if not pd.isna(min_val) else "n/a"

                        lines.append(f"| {condition} | {n} | {mean_str} {unit} | {sd_str} | {sem_str} | {range_str} |")

                    lines.append("")
                else:
                    lines.extend([
                        f"#### {measure_name}",
                        "",
                        "_No descriptive statistics available._",
                        ""
                    ])

            lines.append("")

        lines.append("---\n")
        return "\n".join(lines)

    def _generate_inferential_section(self) -> str:
        """Generate inferential statistics section (LMM-first approach)."""
        lines = [
            "## 3. Inferential Statistics",
            "",
            "This section presents the results of repeated-measures statistical tests.",
            ""
        ]

        measures = self._get_declared_measures()

        for component in self.components:
            lines.extend([
                f"### 3.{self.components.index(component)+1} {component} Component",
                ""
            ])

            for measure_key, measure_name, unit in measures:
                lines.extend([
                    f"#### {measure_name}",
                    ""
                ])

                # Load all test results
                anova_df = self._load_anova_results(component, measure_key)
                pairwise_df = self._load_pairwise_results(component, measure_key)
                lmm_result = self._load_lmm_results(component, measure_key)

                # ===================================================================
                # SECTION 1: LMM Results (PRIMARY ANALYSIS)
                # ===================================================================
                if lmm_result is not None:
                    lines.extend([
                        "**Linear Mixed-Effects Model (Primary Analysis):**",
                        ""
                    ])

                    converged = lmm_result.get('converged', False)
                    aic = lmm_result.get('aic')
                    bic = lmm_result.get('bic')

                    if converged and aic != float('-inf') and aic != float('inf'):
                        lines.append(f"- Model converged successfully")
                        lines.append(f"- AIC = {aic:.2f}, BIC = {bic:.2f}")

                        # Parse summary if available
                        summary = lmm_result.get('summary', [])
                        if summary and len(summary) > 1:
                            # Show all fixed effects (condition + covariates like SNR)
                            try:
                                # Row 0 is intercept, rows 1+ are fixed effects
                                for i, effect in enumerate(summary[1:], start=1):
                                    effect_name = effect.get('name', f'effect_{i}')
                                    coef = float(effect.get('Coef.', 0))
                                    se = effect.get('Std.Err.', '')
                                    z = effect.get('z', '')
                                    p = effect.get('P>|z|', '')

                                    if se and z and p:
                                        # Capitalize effect name nicely
                                        display_name = effect_name.replace('_', ' ').title() if effect_name != 'condition' else 'Condition'
                                        lines.append(f"- {display_name} effect: *β* = {coef:.2f}, *SE* = {se}, *z* = {z}, *p* {self._format_p_value(float(p))}")
                            except (ValueError, TypeError, KeyError):
                                # Fallback: just show condition effect (row 1)
                                try:
                                    cond_effect = summary[1]
                                    coef = float(cond_effect.get('Coef.', 0))
                                    se = cond_effect.get('Std.Err.', '')
                                    z = cond_effect.get('z', '')
                                    p = cond_effect.get('P>|z|', '')

                                    if se and z and p:
                                        lines.append(f"- Condition effect: *β* = {coef:.2f}, *SE* = {se}, *z* = {z}, *p* {self._format_p_value(float(p))}")
                                except (ValueError, TypeError, KeyError):
                                    lines.append("- _Coefficient estimates available in JSON output_")

                        lines.append("")
                        lines.append("_Note: LMM uses all available subject data via maximum likelihood estimation._")
                        lines.append("")
                    else:
                        lines.append("_LMM did not converge or had numerical issues._\n")
                else:
                    lines.append("_LMM results not available._\n")

                # ===================================================================
                # SECTION 2: ANOVA Results (SUPPLEMENTARY ANALYSIS)
                # ===================================================================
                if anova_df is not None and len(anova_df) > 0:
                    try:
                        lines.extend([
                            "**Repeated-Measures ANOVA (Supplementary Analysis):**",
                            ""
                        ])

                        # Find the condition row
                        cond_row = anova_df[anova_df['Source'] == 'condition']

                        if len(cond_row) > 0:
                            F_val = cond_row['F'].values[0]
                            p_val = cond_row['p-unc'].values[0]

                            # Check for GG correction
                            p_gg = cond_row['p-GG-corr'].values[0] if 'p-GG-corr' in cond_row.columns else None
                            epsilon = cond_row['eps'].values[0] if 'eps' in cond_row.columns else None

                            # Effect size
                            effect_size_col = 'ng2' if 'ng2' in cond_row.columns else 'np2' if 'np2' in cond_row.columns else None
                            eta_sq = cond_row[effect_size_col].values[0] if effect_size_col else None

                            # Format DFs
                            dfn = cond_row['ddof1'].values[0] if 'ddof1' in cond_row.columns else None
                            dfd = cond_row['ddof2'].values[0] if 'ddof2' in cond_row.columns else None
                            df_str = f"({dfn:.0f}, {dfd:.0f})" if dfn and dfd else ""

                            # Build ANOVA statement
                            anova_statement = f"- *F*{df_str} = {F_val:.2f}, *p* {self._format_p_value(p_val)}"

                            if eta_sq is not None:
                                anova_statement += f", η²_G = {eta_sq:.3f}"

                            lines.append(anova_statement)

                            # Add GG correction if sphericity violated
                            if p_gg is not None and epsilon is not None and epsilon < 0.75:
                                lines.append(f"- Greenhouse-Geisser corrected: *p* {self._format_p_value(p_gg)} (ε = {epsilon:.3f})")

                            # Interpretation
                            if p_val < 0.001:
                                interp = "**highly significant**"
                            elif p_val < 0.01:
                                interp = "**significant**"
                            elif p_val < 0.05:
                                interp = "**significant**"
                            elif p_val < 0.10:
                                interp = "**marginally significant trend**"
                            else:
                                interp = "**not significant**"

                            lines.append(f"- **Interpretation:** The main effect of condition was {interp}.")

                            # Add effective N warning for listwise deletion
                            if dfd is not None:
                                n_complete = int(dfd) + 1  # df_denominator = n - 1
                                lines.append(f"- _Note: ANOVA restricted to n={n_complete} subjects with complete data across all conditions (listwise deletion)._")

                            lines.append("")
                        else:
                            lines.append("_ANOVA results not available (condition row not found)._\n")
                    except Exception as e:
                        lines.append(f"_ANOVA results could not be parsed (error: {str(e)[:50]})._\n")
                else:
                    lines.append("_ANOVA results not available._\n")

                # ===================================================================
                # SECTION 3: Pairwise Comparisons (SUPPLEMENTARY ANALYSIS)
                # ===================================================================
                if pairwise_df is not None and len(pairwise_df) > 0:
                    lines.extend([
                        "**Pairwise Comparisons (Supplementary Analysis):**",
                        ""
                    ])

                    # Check if test succeeded
                    if 'T' in pairwise_df.columns:
                        # Determine correction method
                        correction = "FDR" if 'p-corr' in pairwise_df.columns else "uncorrected"

                        lines.append(f"_Post-hoc tests with {correction} correction for multiple comparisons:_")
                        lines.append("")
                        lines.append("| Comparison | *t* | *df* | *p* (corrected) | Cohen's *d* | Effect Size | Sig. |")
                        lines.append("|------------|-----|------|----------------|-------------|-------------|------|")

                        for _, row in pairwise_df.iterrows():
                            comp_a = row['A']
                            comp_b = row['B']
                            t_val = row['T']
                            df = row['dof']
                            p_corr = row['p-corr'] if 'p-corr' in pairwise_df.columns else row['p-unc']

                            # Effect size
                            d_val = row.get('cohen', row.get('hedges', np.nan))
                            d_str, d_interp = self._format_effect_size(d_val)

                            # Add CI if available
                            if 'ci_lower' in row and 'ci_upper' in row:
                                ci_lower = row['ci_lower']
                                ci_upper = row['ci_upper']
                                if not pd.isna(ci_lower) and not pd.isna(ci_upper):
                                    d_str += f" [{ci_lower:.2f}, {ci_upper:.2f}]"

                            # Significance marker
                            if p_corr < 0.001:
                                sig = "***"
                            elif p_corr < 0.01:
                                sig = "**"
                            elif p_corr < 0.05:
                                sig = "*"
                            else:
                                sig = "n.s."

                            lines.append(f"| {comp_a} vs {comp_b} | {t_val:.2f} | {df:.0f} | {self._format_p_value(p_corr)} | {d_str} | {d_interp} | {sig} |")

                        lines.append("")
                        lines.append("_Note: * p < .05, ** p < .01, *** p < .001; n.s. = not significant_")
                        lines.append("")
                    else:
                        lines.append("_Pairwise tests could not be computed (insufficient paired samples)._\n")
                else:
                    lines.append("_Pairwise test results not available._\n")

            lines.append("")

        lines.append("---\n")
        return "\n".join(lines)

    def _generate_interpretation_section(self) -> str:
        """Generate overall interpretation section."""
        lines = [
            "## 4. Overall Interpretation",
            "",
            "### Key Findings",
            ""
        ]

        # Analyze results to extract key findings
        findings = []

        # Map DV to short names for summary section
        measures = []
        for key, name, unit in self._get_declared_measures():
            short = 'latency' if 'latency' in key else 'amplitude'
            measures.append((key, short, unit))

        for component in self.components:
            for measure_key, measure_name, unit in measures:
                # Check ANOVA significance
                anova_df = self._load_anova_results(component, measure_key)
                pairwise_df = self._load_pairwise_results(component, measure_key)
                desc_df = self._load_descriptives(component, measure_key)

                if anova_df is not None and len(anova_df) > 0:
                    try:
                        cond_row = anova_df[anova_df['Source'] == 'condition']

                        if len(cond_row) > 0:
                            p_val = cond_row['p-unc'].values[0]

                            if p_val < 0.05:
                                # Significant main effect
                                finding = f"**{component} {measure_name}:** Significant main effect of condition (*p* {self._format_p_value(p_val)})"

                                # Add pairwise details if available
                                if pairwise_df is not None and len(pairwise_df) > 0 and 'T' in pairwise_df.columns:
                                    sig_pairs = pairwise_df[pairwise_df['p-corr'] < 0.05] if 'p-corr' in pairwise_df.columns else pairwise_df[pairwise_df['p-unc'] < 0.05]

                                    if len(sig_pairs) > 0:
                                        finding += ". Post-hoc tests revealed:"
                                        findings.append(finding)

                                        for _, row in sig_pairs.iterrows():
                                            comp_a = row['A']
                                            comp_b = row['B']
                                            d_val = row.get('cohen', row.get('hedges', np.nan))

                                            # Get means from descriptives
                                            if desc_df is not None:
                                                mean_a = desc_df[desc_df['condition'] == comp_a]['mean'].values[0] if len(desc_df[desc_df['condition'] == comp_a]) > 0 else None
                                                mean_b = desc_df[desc_df['condition'] == comp_b]['mean'].values[0] if len(desc_df[desc_df['condition'] == comp_b]) > 0 else None

                                                if mean_a and mean_b:
                                                    direction = "greater" if mean_a > mean_b else "smaller"
                                                    findings.append(f"  - {comp_a} showed {direction} {measure_name} than {comp_b} (*d* = {d_val:.2f})")
                                    else:
                                        findings.append(finding + " (no significant pairwise comparisons)")
                                else:
                                    findings.append(finding)

                            elif p_val < 0.10:
                                findings.append(f"**{component} {measure_name}:** Marginal trend toward condition differences (*p* {self._format_p_value(p_val)})")
                    except Exception:
                        pass

        if findings:
            for finding in findings:
                lines.append(finding)
            lines.append("")
        else:
            lines.append("No significant main effects or interactions were detected at the α = .05 level.")
            lines.append("")

        lines.append("### Research Implications")
        lines.append("")
        lines.append("_[Researchers should interpret these findings in the context of their theoretical framework and study design.]_")
        lines.append("")

        lines.append("---\n")
        return "\n".join(lines)

    def _generate_visualizations_section(self) -> str:
        """Generate visualizations section with embedded plots."""
        lines = [
            "## 5. Visualizations",
            "",
            "The following plots are available in the `plots/` subdirectory:",
            ""
        ]

        plots_dir = self.stats_dir / "plots"
        if plots_dir.exists():
            # Group by component and measure
            measures = [
                ('latency_frac_area_ms', 'Latency'),
                ('mean_amplitude_roi', 'Amplitude')
            ]

            for component in self.components:
                lines.append(f"### 5.{self.components.index(component)+1} {component} Component\n")

                for measure_key, measure_name in measures:
                    lines.append(f"#### {measure_name}\n")

                    # Check for plots
                    boxplot_path = plots_dir / f"boxplot_{component}_{measure_key}.png"
                    violin_path = plots_dir / f"violin_{component}_{measure_key}.png"

                    if boxplot_path.exists():
                        rel_path = f"plots/boxplot_{component}_{measure_key}.png"
                        lines.append(f"**Boxplot:**\n")
                        lines.append(f"![{component} {measure_name} Boxplot]({rel_path})\n")

                    if violin_path.exists():
                        rel_path = f"plots/violin_{component}_{measure_key}.png"
                        lines.append(f"**Violin Plot:**\n")
                        lines.append(f"![{component} {measure_name} Violin]({rel_path})\n")
        else:
            lines.append("_No visualization plots found._\n")

        lines.append("---\n")
        return "\n".join(lines)

    def _generate_methods_section(self) -> str:
        """Generate methods section for publication."""
        lines = [
            "## 6. Methods Summary (for Publication)",
            "",
            "### ERP Measurement",
            ""
        ]

        if self.summary_data:
            settings = self.summary_data.get('analysis_settings', {})

            lines.extend([
                "ERP components were measured using a collapsed localizer approach, where component "
                "peaks were identified from the grand average of all conditions combined to avoid "
                "circular analysis (Luck & Gaspelin, 2017). Measurement windows were defined as the "
                "full-width at half-maximum (FWHM) around each peak. Component latency was quantified "
                "using the 50% fractional area latency (FAL), which represents the time point at which "
                "the cumulative area under the curve reaches 50% of its total value within the measurement "
                "window. This metric provides a robust estimate of component timing with lower measurement "
                "error than peak latency (Kiesel et al., 2008). Mean amplitude was computed as the average "
                "voltage within the FWHM window across predefined regions of interest (ROI).",
                ""
            ])

            # QC
            filters = settings.get('filters', {})
            if filters.get('min_snr'):
                lines.append(f"Quality control filtering excluded subject-component measurements with signal-to-noise ratio (SNR) below {filters['min_snr']}.")
                lines.append("")

        lines.extend([
            "### Statistical Analysis",
            ""
        ])

        if self.summary_data and self.summary_data.get('tests_run'):
            tests = self.summary_data['tests_run']

            # LMM-first approach
            if tests.get('lmm'):
                lines.extend([
                    "Linear mixed-effects models (LMM) with random intercepts for subjects were used as the primary analysis, "
                    "as they optimally handle missing data via maximum likelihood estimation (Baayen et al., 2008). "
                ])

                # Mention SNR covariate if it appears to be used
                settings = self.summary_data.get('analysis_settings', {})
                if settings:
                    # Note: We can't directly detect SNR from tests_run, but we mention it in general
                    pass

            if tests.get('anova') or tests.get('pairwise'):
                lines.extend([
                    "For comparison with traditional approaches, repeated-measures ANOVA and pairwise t-tests were also performed on complete cases; "
                    "however, power was substantially reduced by listwise deletion. Therefore, LMM results are emphasized in interpretation.",
                    ""
                ])
        else:
            # Fallback if no tests_run metadata
            lines.extend([
                "Within-subjects repeated-measures analyses were conducted using linear mixed-effects models (LMM) as the primary test.",
                ""
            ])

        lines.extend([
            "Effect sizes are reported as Cohen's *d* for pairwise comparisons and generalized eta-squared (η²_G) for ANOVA.",
            ""
        ])

        # Library versions
        if self.summary_data and self.summary_data.get('library_versions'):
            libs = self.summary_data['library_versions']
            lines.extend([
                "### Software",
                "",
                f"- Python {libs.get('python', 'N/A')}",
                f"- MNE-Python {libs.get('mne', 'N/A')}",
                f"- Statsmodels {libs.get('statsmodels', 'N/A')}",
            ])

            if 'pingouin' in libs:
                lines.append(f"- Pingouin {libs.get('pingouin', 'N/A')}")

            lines.append("")

        lines.extend([
            "### References",
            "",
            "- Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects modeling with crossed random effects for subjects and items. *Journal of Memory and Language, 59*(4), 390-412.",
            "- Kiesel, A., Miller, J., Jolicœur, P., & Brisson, B. (2008). Measurement of ERP latency differences: A comparison of single-participant and jackknife-based scoring methods. *Psychophysiology, 45*(2), 250-274.",
            "- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology, 54*(1), 146-157.",
            ""
        ])

        lines.append("---\n")
        return "\n".join(lines)

    def generate_report(self, output_path: Optional[Path] = None) -> str:
        """
        Generate complete markdown report.

        Parameters
        ----------
        output_path : Path, optional
            Path to save report. If None, returns string only.

        Returns
        -------
        report : str
            Complete markdown report content
        """
        report_sections = [
            self._generate_header(),
            self._generate_overview_section(),
            self._generate_descriptives_section(),
            self._generate_inferential_section(),
            self._generate_interpretation_section(),
            self._generate_visualizations_section(),
            self._generate_methods_section()
        ]

        report = "\n".join(report_sections)

        # Add footer
        report += "\n---\n\n"
        report += f"*Report generated automatically by EEG Image Analysis Pipeline v2*\n"
        report += f"*For questions about this analysis, please refer to the YAML configuration and statistical output files.*\n"

        # Save if path provided
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Report saved to: {output_path}")

        return report

    # ------------------- Helpers for dynamic DV naming -------------------
    def _get_declared_measures(self):
        default_map = {
            'latency_frac_area_ms': ('Latency (50% Fractional Area)', 'ms'),
            'peak_latency_ms': ('Latency (Peak)', 'ms'),
            'mean_amplitude_roi': ('Mean Amplitude (ROI)', 'µV'),
            'peak_amplitude_roi': ('Amplitude (Peak)', 'µV'),
        }
        declared = self.summary_data.get('dependent_variables', []) if self.summary_data else []
        selected = declared or ['peak_latency_ms', 'peak_amplitude_roi']
        return [(k, default_map.get(k, (k, ''))[0], default_map.get(k, ('', ''))[1]) for k in selected]

    def _format_dependent_variables_line(self) -> str:
        human = [name for _, name, _ in self._get_declared_measures()]
        if not human:
            return "**Dependent Variables:** (not specified)"
        if len(human) == 1:
            return f"**Dependent Variable:** {human[0]}"
        return f"**Dependent Variables:** {', '.join(human)}"


def generate_report_for_analysis(stats_dir: Path, output_filename: str = "STATISTICAL_REPORT.md") -> Path:
    """
    Convenience function to generate report for a single analysis.

    Parameters
    ----------
    stats_dir : Path
        Path to stats directory (e.g., docs/assets/stats/13_31/)
    output_filename : str
        Name of output markdown file

    Returns
    -------
    output_path : Path
        Path to generated report
    """
    stats_dir = Path(stats_dir)
    analysis_id = stats_dir.name

    generator = StatisticalReportGenerator(stats_dir, analysis_id)
    output_path = stats_dir / output_filename

    generator.generate_report(output_path)

    return output_path
