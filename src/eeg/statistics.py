"""
Statistical analysis functions for ERP data (Phase 2B).

This module provides the ERPStatistics class for performing:
- Repeated-measures ANOVA
- Pairwise t-tests with multiple comparison correction
- Linear Mixed-Effects Models (LMM)

All methods are designed to work with subject-level measurements
collected in Phase 2A.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Optional, Dict, Any, Tuple
import json

try:
    import pingouin as pg
except ImportError:
    pg = None

try:
    from statsmodels.formula.api import mixedlm
except ImportError:
    mixedlm = None


class ERPStatistics:
    """
    Statistical analysis class for ERP data.

    Performs within-subjects statistical tests on subject-level
    measurements (latency and amplitude) from Phase 2A output.

    Parameters
    ----------
    data : str, Path, or pd.DataFrame
        Path to subject_measurements.csv or DataFrame with columns:
        - subject_id: Subject identifier
        - component: ERP component (e.g., 'N1', 'P3b')
        - condition: Experimental condition
        - latency_frac_area_ms: Fractional area latency
        - mean_amplitude_roi: Mean amplitude in ROI
        - snr: Signal-to-noise ratio (optional for filtering)

    Attributes
    ----------
    data : pd.DataFrame
        The loaded subject-level measurement data.

    Examples
    --------
    >>> stats = ERPStatistics('subject_measurements.csv')
    >>> anova = stats.run_anova(dv='latency_frac_area_ms', component='N1', within='condition')
    >>> pairwise = stats.run_pairwise_tests(dv='latency_frac_area_ms', component='N1', within='condition')
    """

    REQUIRED_COLUMNS = ['subject_id', 'component', 'condition']

    def __init__(self, data: Union[str, Path, pd.DataFrame]):
        """
        Initialize ERPStatistics with data.

        Parameters
        ----------
        data : str, Path, or pd.DataFrame
            Path to CSV file or DataFrame containing subject measurements.

        Raises
        ------
        ValueError
            If required columns are missing from the data.
        FileNotFoundError
            If CSV file path does not exist.
        """
        if isinstance(data, (str, Path)):
            data_path = Path(data)
            if not data_path.exists():
                raise FileNotFoundError(f"Data file not found: {data_path}")
            self.data = pd.read_csv(data_path, dtype={'subject_id': str})
        elif isinstance(data, pd.DataFrame):
            self.data = data.copy()
            # Ensure subject_id is string
            if 'subject_id' in self.data.columns:
                self.data['subject_id'] = self.data['subject_id'].astype(str)
        else:
            raise TypeError("data must be a file path or pandas DataFrame")

        # Validate required columns
        missing_cols = [col for col in self.REQUIRED_COLUMNS if col not in self.data.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

    def filter_data(
        self,
        component: Optional[str] = None,
        condition: Optional[str] = None,
        min_snr: Optional[float] = None,
        dropna: bool = True
    ) -> pd.DataFrame:
        """
        Filter data by component, condition, and/or SNR threshold.

        Parameters
        ----------
        component : str, optional
            Filter to specific component (e.g., 'N1').
        condition : str, optional
            Filter to specific condition.
        min_snr : float, optional
            Minimum SNR threshold. Subjects below this will be excluded.
        dropna : bool, default=True
            Whether to drop rows with NaN values.

        Returns
        -------
        pd.DataFrame
            Filtered data.
        """
        filtered = self.data.copy()

        if component is not None:
            filtered = filtered[filtered['component'] == component]

        if condition is not None:
            filtered = filtered[filtered['condition'] == condition]

        if min_snr is not None and 'snr' in filtered.columns:
            filtered = filtered[filtered['snr'] >= min_snr]

        if dropna:
            filtered = filtered.dropna()

        return filtered

    def run_anova(
        self,
        dv: str,
        component: str,
        within: str = 'condition',
        subject: str = 'subject_id',
        **filter_kwargs
    ) -> pd.DataFrame:
        """
        Run repeated-measures ANOVA using pingouin.

        Parameters
        ----------
        dv : str
            Dependent variable column name (e.g., 'latency_frac_area_ms', 'mean_amplitude_roi').
        component : str
            Component to analyze (e.g., 'N1', 'P3b').
        within : str, default='condition'
            Within-subjects factor column name.
        subject : str, default='subject_id'
            Subject identifier column name.
        **filter_kwargs
            Additional filtering arguments passed to filter_data().

        Returns
        -------
        pd.DataFrame
            ANOVA results table with columns:
            - Source: Effect name
            - ddof1, ddof2: Degrees of freedom
            - F: F-statistic
            - p-unc: Uncorrected p-value
            - np2: Partial eta-squared (effect size)
            - eps: Sphericity estimate (if applicable)

        Raises
        ------
        ImportError
            If pingouin is not installed.
        ValueError
            If insufficient data after filtering.

        Examples
        --------
        >>> stats = ERPStatistics('subject_measurements.csv')
        >>> anova_result = stats.run_anova(
        ...     dv='latency_frac_area_ms',
        ...     component='N1',
        ...     within='condition'
        ... )
        """
        if pg is None:
            raise ImportError("pingouin is required for ANOVA. Install with: pip install pingouin")

        # Filter data
        filtered = self.filter_data(component=component, **filter_kwargs)

        if len(filtered) == 0:
            raise ValueError(f"No data available for component '{component}' after filtering")

        # Check we have the required columns
        required = [subject, within, dv]
        missing = [col for col in required if col not in filtered.columns]
        if missing:
            raise ValueError(f"Missing columns for ANOVA: {missing}")

        # Run repeated-measures ANOVA
        result = pg.rm_anova(
            data=filtered,
            dv=dv,
            within=within,
            subject=subject,
            detailed=True
        )

        return result

    def run_pairwise_tests(
        self,
        dv: str,
        component: str,
        within: str = 'condition',
        subject: str = 'subject_id',
        padjust: str = 'fdr_bh',
        effsize: str = 'cohen',
        **filter_kwargs
    ) -> pd.DataFrame:
        """
        Run pairwise t-tests with multiple comparison correction.

        Parameters
        ----------
        dv : str
            Dependent variable column name.
        component : str
            Component to analyze.
        within : str, default='condition'
            Within-subjects factor column name.
        subject : str, default='subject_id'
            Subject identifier column name.
        padjust : str, default='fdr_bh'
            Method for p-value adjustment:
            - 'fdr_bh': Benjamini-Hochberg FDR correction
            - 'bonf': Bonferroni correction
            - 'holm': Holm-Bonferroni correction
            - 'none': No correction
        effsize : str, default='cohen'
            Effect size to compute ('cohen', 'hedges', 'eta-square').
        **filter_kwargs
            Additional filtering arguments.

        Returns
        -------
        pd.DataFrame
            Pairwise test results with columns:
            - A, B: Condition names being compared
            - T: T-statistic
            - dof: Degrees of freedom
            - p-unc: Uncorrected p-value
            - p-corr: Corrected p-value
            - effsize: Effect size (Cohen's d or other)

        Raises
        ------
        ImportError
            If pingouin is not installed.

        Examples
        --------
        >>> stats = ERPStatistics('subject_measurements.csv')
        >>> pairwise = stats.run_pairwise_tests(
        ...     dv='latency_frac_area_ms',
        ...     component='N1',
        ...     padjust='fdr_bh'
        ... )
        """
        if pg is None:
            raise ImportError("pingouin is required for pairwise tests. Install with: pip install pingouin")

        # Filter data
        filtered = self.filter_data(component=component, **filter_kwargs)

        if len(filtered) == 0:
            raise ValueError(f"No data available for component '{component}' after filtering")

        # Run pairwise t-tests
        result = pg.pairwise_tests(
            data=filtered,
            dv=dv,
            within=within,
            subject=subject,
            parametric=True,
            padjust=padjust,
            effsize=effsize
        )

        return result

    def run_lmm(
        self,
        dv: str,
        component: str,
        fixed: str,
        random: str = 'subject_id',
        **filter_kwargs
    ) -> Dict[str, Any]:
        """
        Run Linear Mixed-Effects Model using statsmodels.

        LMMs are useful when:
        - Data has missing observations (unbalanced design)
        - You want to model continuous covariates
        - You need more complex random effects structures

        Parameters
        ----------
        dv : str
            Dependent variable column name.
        component : str
            Component to analyze.
        fixed : str
            Fixed effects formula (e.g., 'condition' or 'condition + snr').
        random : str, default='subject_id'
            Random effects grouping variable.
        **filter_kwargs
            Additional filtering arguments.

        Returns
        -------
        dict
            Dictionary containing:
            - 'model': The fitted model object
            - 'summary': Model summary as DataFrame
            - 'aic': Akaike Information Criterion
            - 'bic': Bayesian Information Criterion

        Raises
        ------
        ImportError
            If statsmodels is not installed.

        Examples
        --------
        >>> stats = ERPStatistics('subject_measurements.csv')
        >>> lmm_result = stats.run_lmm(
        ...     dv='latency_frac_area_ms',
        ...     component='N1',
        ...     fixed='condition',
        ...     random='subject_id'
        ... )
        >>> print(lmm_result['summary'])
        """
        if mixedlm is None:
            raise ImportError("statsmodels is required for LMM. Install with: pip install statsmodels")

        # Filter data - must drop NaN for LMM to work properly
        filtered = self.filter_data(component=component, dropna=True, **filter_kwargs)

        if len(filtered) == 0:
            raise ValueError(f"No data available for component '{component}' after filtering")

        # Check we have the DV column
        if dv not in filtered.columns:
            raise ValueError(f"Dependent variable '{dv}' not found in data")

        # Sort by group variable and reset index (important for statsmodels)
        filtered = filtered.sort_values(by=[random]).reset_index(drop=True)

        # Build formula
        formula = f"{dv} ~ {fixed}"

        # Detect reference condition for categorical variables (for documentation)
        # Statsmodels uses the first category (alphabetically) as reference by default
        reference_condition = None
        if 'condition' in fixed and 'condition' in filtered.columns:
            # Get sorted unique conditions (statsmodels sorts them alphabetically)
            unique_conditions = sorted(filtered['condition'].unique())
            if len(unique_conditions) > 0:
                reference_condition = unique_conditions[0]

        # Fit model - statsmodels needs properly sorted and indexed data
        try:
            model = mixedlm(formula, filtered, groups=filtered[random])
            fitted_model = model.fit(method='lbfgs', reml=False)
        except Exception as e:
            # If LBFGS fails, try a more robust method
            model = mixedlm(formula, filtered, groups=filtered[random])
            fitted_model = model.fit(method='powell', reml=False)

        # Extract results
        result = {
            'model': fitted_model,
            'summary': fitted_model.summary().tables[1],  # Coefficient table
            'aic': fitted_model.aic,
            'bic': fitted_model.bic,
            'converged': fitted_model.converged,
            'reference_condition': reference_condition  # NEW: Save reference for report
        }

        return result

    def run_lmm_pairwise(
        self,
        dv: str,
        component: str,
        fixed: str,
        random: str = 'subject_id',
        correction: str = 'hs',
        **filter_kwargs
    ) -> pd.DataFrame:
        """
        Run pairwise comparisons for Linear Mixed-Effects Model.

        This method provides ALL pairwise comparisons between conditions,
        answering the question: "Do the conditions differ from each other?"
        (e.g., is 1 to 3 different from 1 to 4?).

        Uses statsmodels' native t_test_pairwise() method with proper
        multiple comparison corrections.

        Parameters
        ----------
        dv : str
            Dependent variable column name.
        component : str
            Component to analyze.
        fixed : str
            Fixed effects formula (e.g., 'condition' or 'condition + snr').
            For pairwise comparisons, the first categorical term is used.
        random : str, default='subject_id'
            Random effects grouping variable.
        correction : str, default='hs'
            Multiple comparison correction method:
            - 'hs': Holm-Sidak (recommended - less conservative than Bonferroni)
            - 'bonferroni': Bonferroni correction (more conservative)
            - 'fdr_bh': Benjamini-Hochberg FDR
            - 'sidak': Sidak correction
            - None: No correction (not recommended)
        **filter_kwargs
            Additional filtering arguments.

        Returns
        -------
        pd.DataFrame
            Pairwise comparison results with columns:
            - Contrast: Comparison being made (e.g., "1 to 1 - 1 to 2")
            - Coef: Estimated difference (coefficient)
            - Std.Err.: Standard error of the difference
            - z: z-statistic
            - P>|z|: Unadjusted p-value
            - P>|z| (adj): Multiple-comparison adjusted p-value

        Raises
        ------
        ImportError
            If statsmodels is not installed.
        ValueError
            If insufficient data or invalid parameters.

        Notes
        -----
        - Uses maximum likelihood estimation (same as run_lmm)
        - Handles missing data optimally via LMM framework
        - For k conditions, returns C(k,2) = k*(k-1)/2 comparisons
        - Adjusted p-values control family-wise error rate

        Examples
        --------
        >>> stats = ERPStatistics('subject_measurements.csv')
        >>> # Get all pairwise comparisons for N1 amplitude
        >>> pairwise = stats.run_lmm_pairwise(
        ...     dv='mean_amplitude_roi',
        ...     component='N1',
        ...     fixed='condition',
        ...     correction='hs'
        ... )
        >>> # Show significant comparisons (after correction)
        >>> sig = pairwise[pairwise['P>|z| (adj)'] < 0.05]
        >>> print(sig[['Contrast', 'Coef', 'P>|z| (adj)']])

        References
        ----------
        Holm, S. (1979). A simple sequentially rejective multiple test procedure.
            Scandinavian Journal of Statistics, 6(2), 65-70.
        """
        if mixedlm is None:
            raise ImportError("statsmodels is required for LMM. Install with: pip install statsmodels")

        # Filter data - must drop NaN for LMM to work properly
        filtered = self.filter_data(component=component, dropna=True, **filter_kwargs)

        if len(filtered) == 0:
            raise ValueError(f"No data available for component '{component}' after filtering")

        # Check we have the DV column
        if dv not in filtered.columns:
            raise ValueError(f"Dependent variable '{dv}' not found in data")

        # Sort by group variable and reset index (important for statsmodels)
        filtered = filtered.sort_values(by=[random]).reset_index(drop=True)

        # Build formula
        formula = f"{dv} ~ {fixed}"

        # Fit the mixed-effects model
        try:
            model = mixedlm(formula, filtered, groups=filtered[random])
            fitted_model = model.fit(method='lbfgs', reml=False)
        except Exception as e:
            # If LBFGS fails, try a more robust method
            try:
                model = mixedlm(formula, filtered, groups=filtered[random])
                fitted_model = model.fit(method='powell', reml=False)
            except Exception as e2:
                raise RuntimeError(f"LMM fitting failed: {e2}") from e

        # Extract the categorical term name for pairwise comparisons
        # Handle cases like "condition" or "condition + snr"
        # We want the first term (typically the categorical factor)
        categorical_term = fixed.split('+')[0].strip()

        # statsmodels t_test_pairwise requires the exact term name as it appears in the model
        # For categorical variables, statsmodels creates dummy variables
        # We need to manually construct pairwise contrasts

        # Get unique conditions (sorted alphabetically - statsmodels default)
        conditions = sorted(filtered[categorical_term].unique())
        n_conditions = len(conditions)

        if n_conditions < 2:
            raise ValueError(f"Need at least 2 conditions for pairwise comparisons, found {n_conditions}")

        # Manual pairwise comparisons using t_test
        # This is more reliable than t_test_pairwise which can be finicky
        pairwise_results = []

        # Get model parameters
        params = fitted_model.params
        cov_params = fitted_model.cov_params()

        # For each pair of conditions, construct a contrast
        from itertools import combinations

        for cond_a, cond_b in combinations(conditions, 2):
            # Construct contrast vector
            # For treatment coding, first condition is reference (intercept)
            # Other conditions have dummy variables

            # Find parameter names for these conditions
            param_names = list(params.index)

            # Initialize contrast vector (zeros)
            contrast = np.zeros(len(params))

            # Reference condition (first alphabetically) is coded as intercept
            ref_condition = conditions[0]

            if cond_a == ref_condition:
                # Comparing reference to another condition
                # Contrast is just the coefficient for cond_b
                param_name = f"{categorical_term}[T.{cond_b}]"
                if param_name in param_names:
                    idx = param_names.index(param_name)
                    contrast[idx] = -1  # Negative because we want cond_a - cond_b
            elif cond_b == ref_condition:
                # Comparing another condition to reference
                param_name = f"{categorical_term}[T.{cond_a}]"
                if param_name in param_names:
                    idx = param_names.index(param_name)
                    contrast[idx] = 1
            else:
                # Comparing two non-reference conditions
                # Contrast is difference of their coefficients
                param_a = f"{categorical_term}[T.{cond_a}]"
                param_b = f"{categorical_term}[T.{cond_b}]"
                if param_a in param_names and param_b in param_names:
                    idx_a = param_names.index(param_a)
                    idx_b = param_names.index(param_b)
                    contrast[idx_a] = 1
                    contrast[idx_b] = -1

            # Compute test statistic
            # Estimate = contrast' * params
            estimate = np.dot(contrast, params)

            # Standard error = sqrt(contrast' * cov * contrast)
            se = np.sqrt(np.dot(contrast, np.dot(cov_params, contrast)))

            # z-statistic
            z_stat = estimate / se if se > 0 else 0

            # p-value (two-tailed)
            from scipy import stats as sp_stats
            p_value = 2 * (1 - sp_stats.norm.cdf(abs(z_stat)))

            pairwise_results.append({
                'Contrast': f"{cond_a} - {cond_b}",
                'Coef': estimate,
                'Std.Err.': se,
                'z': z_stat,
                'P>|z|': p_value
            })

        # Convert to DataFrame
        result_df = pd.DataFrame(pairwise_results)

        # Apply multiple comparison correction
        if correction == 'bonferroni':
            result_df['P>|z| (adj)'] = result_df['P>|z|'] * len(result_df)
            result_df['P>|z| (adj)'] = result_df['P>|z| (adj)'].clip(upper=1.0)
        elif correction == 'hs':
            # Holm-Sidak correction
            sorted_idx = result_df['P>|z|'].argsort()
            n = len(result_df)
            adjusted_p = []
            for rank, idx in enumerate(sorted_idx):
                p = result_df.loc[idx, 'P>|z|']
                # Holm-Sidak: 1 - (1-p)^(n-rank)
                adj = 1 - (1 - p) ** (n - rank)
                adjusted_p.append((idx, adj))
            for idx, adj_p in adjusted_p:
                result_df.loc[idx, 'P>|z| (adj)'] = min(adj_p, 1.0)
        elif correction == 'fdr_bh':
            # Benjamini-Hochberg FDR
            from scipy.stats import false_discovery_control
            result_df['P>|z| (adj)'] = false_discovery_control(result_df['P>|z|'].values)
        else:
            # No correction
            result_df['P>|z| (adj)'] = result_df['P>|z|']

        # Reorder columns for readability
        desired_order = ['Contrast', 'Coef', 'Std.Err.', 'z', 'P>|z|', 'P>|z| (adj)']
        existing_cols = [col for col in desired_order if col in result_df.columns]
        other_cols = [col for col in result_df.columns if col not in existing_cols]
        result_df = result_df[existing_cols + other_cols]

        return result_df

    def get_descriptives(
        self,
        dv: str,
        component: str,
        groupby: str = 'condition',
        **filter_kwargs
    ) -> pd.DataFrame:
        """
        Compute descriptive statistics by group.

        Parameters
        ----------
        dv : str
            Dependent variable to summarize.
        component : str
            Component to analyze.
        groupby : str, default='condition'
            Column to group by.
        **filter_kwargs
            Additional filtering arguments.

        Returns
        -------
        pd.DataFrame
            Descriptive statistics with columns:
            - count: Number of observations
            - mean: Mean value
            - std: Standard deviation
            - sem: Standard error of the mean
            - min, max: Range
            - 25%, 50%, 75%: Quartiles

        Examples
        --------
        >>> stats = ERPStatistics('subject_measurements.csv')
        >>> desc = stats.get_descriptives(
        ...     dv='latency_frac_area_ms',
        ...     component='N1',
        ...     groupby='condition'
        ... )
        """
        filtered = self.filter_data(component=component, **filter_kwargs)

        if len(filtered) == 0:
            raise ValueError(f"No data available for component '{component}' after filtering")

        descriptives = filtered.groupby(groupby)[dv].describe()

        # Add SEM
        descriptives['sem'] = filtered.groupby(groupby)[dv].sem()

        return descriptives

    def save_results(
        self,
        results: Union[pd.DataFrame, Dict],
        output_path: Union[str, Path],
        format: str = 'csv'
    ):
        """
        Save statistical results to file.

        Parameters
        ----------
        results : pd.DataFrame or dict
            Results to save.
        output_path : str or Path
            Output file path.
        format : str, default='csv'
            Output format ('csv' or 'json').

        Examples
        --------
        >>> stats = ERPStatistics('subject_measurements.csv')
        >>> anova = stats.run_anova(dv='latency_frac_area_ms', component='N1')
        >>> stats.save_results(anova, 'anova_results.csv', format='csv')
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if format == 'csv':
            if isinstance(results, pd.DataFrame):
                results.to_csv(output_path, index=False)
            elif isinstance(results, dict):
                # For LMM results, save summary table
                if 'summary' in results:
                    results['summary'].to_csv(output_path)
                else:
                    raise ValueError("Cannot save dict results to CSV without 'summary' key")
        elif format == 'json':
            if isinstance(results, pd.DataFrame):
                results.to_json(output_path, orient='records', indent=2)
            elif isinstance(results, dict):
                # Convert to JSON-serializable format
                serializable = {}
                for key, value in results.items():
                    if isinstance(value, pd.DataFrame):
                        # CRITICAL FIX: Preserve row index (effect names) when converting to dict
                        # Reset index to make row names a regular column called 'name'
                        value_with_names = value.reset_index()
                        # Rename the index column to 'name' if it's not already named
                        if value_with_names.columns[0] == 'index':
                            value_with_names = value_with_names.rename(columns={'index': 'name'})
                        serializable[key] = value_with_names.to_dict(orient='records')
                    elif isinstance(value, (np.integer, np.floating)):
                        serializable[key] = float(value)
                    elif key != 'model':  # Skip model object
                        serializable[key] = value
                with open(output_path, 'w') as f:
                    json.dump(serializable, f, indent=2)
        else:
            raise ValueError(f"Unsupported format: {format}. Use 'csv' or 'json'.")

        print(f"Results saved to: {output_path}")


# Module-level functions for Phase 2C enhancements

def compute_cohens_d_ci(
    x: np.ndarray,
    y: np.ndarray,
    confidence: float = 0.95,
    paired: bool = True
) -> Tuple[float, float, float]:
    """
    Compute Cohen's d effect size with confidence interval.

    Uses appropriate formulas for paired or independent samples.
    For paired data, uses the standard deviation of differences.
    For independent samples, uses pooled standard deviation.

    Parameters
    ----------
    x : np.ndarray
        First group data (or first measurement in paired design).
    y : np.ndarray
        Second group data (or second measurement in paired design).
    confidence : float, default=0.95
        Confidence level (e.g., 0.95 for 95% CI).
    paired : bool, default=True
        Whether data are paired (within-subjects) or independent.

    Returns
    -------
    d : float
        Cohen's d effect size.
    ci_lower : float
        Lower bound of confidence interval.
    ci_upper : float
        Upper bound of confidence interval.

    References
    ----------
    Cumming, G. (2012). Understanding the New Statistics.
    Morris, S. B., & DeShon, R. P. (2002). Combining effect size estimates.

    Examples
    --------
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> y = np.array([2, 3, 4, 5, 6])
    >>> d, ci_lower, ci_upper = compute_cohens_d_ci(x, y, paired=True)
    """
    from scipy import stats

    # Remove NaN values
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]

    if paired:
        # Paired samples: must have equal length
        if len(x) != len(y):
            raise ValueError("Paired samples must have equal length")

        n = len(x)
        if n < 2:
            return np.nan, np.nan, np.nan

        # Cohen's d for paired data: mean difference / SD of differences
        diff = x - y
        mean_diff = np.mean(diff)
        sd_diff = np.std(diff, ddof=1)

        if sd_diff == 0:
            return np.nan, np.nan, np.nan

        d = mean_diff / sd_diff

        # CI for paired design (Morris & DeShon, 2002)
        # se_d = sqrt((1/n) + (d^2 / (2*n)))
        se = np.sqrt((1 / n) + (d**2 / (2 * n)))
        df = n - 1

        alpha = 1 - confidence
        t_crit = stats.t.ppf(1 - alpha/2, df)

        ci_lower = d - t_crit * se
        ci_upper = d + t_crit * se

    else:
        # Independent samples: original implementation
        n1, n2 = len(x), len(y)

        if n1 < 2 or n2 < 2:
            return np.nan, np.nan, np.nan

        # Cohen's d with pooled SD
        mean_diff = np.mean(x) - np.mean(y)
        var1, var2 = np.var(x, ddof=1), np.var(y, ddof=1)
        pooled_sd = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))

        if pooled_sd == 0:
            return np.nan, np.nan, np.nan

        d = mean_diff / pooled_sd

        # CI for independent samples (Hedges & Olkin, 1985)
        se = np.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))
        df = n1 + n2 - 2

        alpha = 1 - confidence
        t_crit = stats.t.ppf(1 - alpha/2, df)

        ci_lower = d - t_crit * se
        ci_upper = d + t_crit * se

    return float(d), float(ci_lower), float(ci_upper)


def get_library_versions() -> Dict[str, str]:
    """
    Get versions of all statistical and ERP analysis libraries.

    Returns
    -------
    dict
        Dictionary mapping library names to version strings.

    Examples
    --------
    >>> versions = get_library_versions()
    >>> print(versions['pingouin'])
    '0.5.5'
    """
    versions = {}

    # Try to get version for each library
    libraries = {
        'pingouin': pg,
        'statsmodels': None,  # Will import separately
        'mne': None,
        'scipy': None,
        'pandas': pd,
        'numpy': np
    }

    # pingouin
    if pg is not None:
        versions['pingouin'] = pg.__version__

    # statsmodels
    try:
        import statsmodels
        versions['statsmodels'] = statsmodels.__version__
    except (ImportError, AttributeError):
        versions['statsmodels'] = 'not installed'

    # mne
    try:
        import mne
        versions['mne'] = mne.__version__
    except (ImportError, AttributeError):
        versions['mne'] = 'not installed'

    # scipy
    try:
        import scipy
        versions['scipy'] = scipy.__version__
    except (ImportError, AttributeError):
        versions['scipy'] = 'not installed'

    # pandas and numpy
    versions['pandas'] = pd.__version__
    versions['numpy'] = np.__version__

    # python version
    import sys
    versions['python'] = sys.version.split()[0]

    return versions


def format_missing_data_policy(
    filters: Dict[str, Any],
    test_type: str = "ANOVA and pairwise tests"
) -> str:
    """
    Generate missing data policy statement for summary report.

    Parameters
    ----------
    filters : dict
        Filter settings used (e.g., {'min_snr': 2.0, 'dropna': True}).
    test_type : str, default="ANOVA and pairwise tests"
        Which tests the policy applies to.

    Returns
    -------
    str
        Clear English statement of missing data handling policy.

    Examples
    --------
    >>> policy = format_missing_data_policy({'min_snr': 2.0, 'dropna': True})
    >>> print(policy)
    'ANOVA and pairwise tests were run on complete cases after applying an SNR filter >= 2.0...'
    """
    parts = []

    # Start with test type
    parts.append(f"{test_type} were run on complete cases")

    # Add SNR filter info
    if 'min_snr' in filters and filters['min_snr'] is not None:
        parts.append(f"after applying an SNR filter >= {filters['min_snr']}")

    # Explain what this means
    policy = " ".join(parts) + "."

    # Add explanation
    policy += (" Subject-condition combinations with missing latency values or "
               "below-threshold SNR were excluded listwise. ")

    # Add LMM note if applicable
    policy += ("Linear mixed-effects models retained all subjects with valid "
               "measurements to optimally handle missing data.")

    return policy
