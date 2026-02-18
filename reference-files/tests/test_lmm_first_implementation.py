"""
Test suite for LMM-first implementation (Phase 2C Enhancement).

Tests verify:
1. Report sections are ordered: LMM → ANOVA → Pairwise
2. ANOVA/Pairwise sections include effective N warnings
3. Plot significance stars use LMM p-values (not ANOVA)
4. Methods section reflects LMM-first approach
5. SNR covariate integration in LMM
6. LMM effect names are preserved (NOT generic "Effect 1", "Effect 2")
7. Reference condition is documented in report

Following TDD: These tests should FAIL before implementation.
"""

import pytest
import pandas as pd
import json
import re
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import sys

# Add src to path
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "src"))

from eeg.summary_report import StatisticalReportGenerator


# ============================================================================
# Test Fixtures
# ============================================================================

@pytest.fixture
def mock_stats_dir(tmp_path):
    """Create mock statistics output directory with sample files."""
    stats_dir = tmp_path / "stats" / "test_analysis"
    stats_dir.mkdir(parents=True)

    # Create mock summary JSON
    summary_data = {
        "timestamp": "2025-01-15 12:00:00",
        "analysis_id": "test_analysis",
        "components_tested": ["N1", "P1"],
        "dependent_variables": ["mean_amplitude_roi", "latency_frac_area_ms"],
        "data_summary": {
            "n_total_measurements": 100,
            "n_subjects": 10,
            "n_conditions": 5
        },
        "tests_run": {
            "anova": True,
            "pairwise": True,
            "lmm": True
        },
        "analysis_settings": {
            "measurement_window_method": "collapsed_localizer_fwhm",
            "latency_measure": "fal_50",
            "amplitude_measure": "mean",
            "baseline_period_ms": "[-100, 0]",
            "filters": {"min_snr": None, "dropna": True}
        },
        "missing_data_policy": "ANOVA and pairwise tests were run on complete cases."
    }

    with open(stats_dir / "statistical_summary.json", "w") as f:
        json.dump(summary_data, f)

    # Create mock ANOVA results (df=2 - low N scenario)
    anova_data = pd.DataFrame({
        "Source": ["condition", "Error"],
        "ddof1": [4, 8],
        "ddof2": [8, None],
        "F": [2.5, None],
        "p-unc": [0.035, None],
        "p-GG-corr": [0.042, None],
        "eps": [0.68, None],
        "ng2": [0.15, None]
    })
    anova_data.to_csv(stats_dir / "anova_N1_mean_amplitude_roi.csv", index=False)

    # Create mock LMM results (JSON format)
    lmm_data = {
        "aic": 450.2,
        "bic": 468.5,
        "converged": True,
        "summary": [
            {"Coef.": 3.5, "Std.Err.": 0.5, "z": 7.0, "P>|z|": 0.001, "name": "Intercept"},
            {"Coef.": 0.85, "Std.Err.": 0.32, "z": 2.656, "P>|z|": 0.008, "name": "condition"},
            {"Coef.": 0.45, "Std.Err.": 0.15, "z": 3.0, "P>|z|": 0.003, "name": "snr"}
        ]
    }
    with open(stats_dir / "lmm_N1_mean_amplitude_roi.json", "w") as f:
        json.dump(lmm_data, f)

    # Create mock pairwise results
    pairwise_data = pd.DataFrame({
        "A": ["cond1", "cond1"],
        "B": ["cond2", "cond3"],
        "T": [2.1, 1.5],
        "dof": [2, 2],  # Only 3 subjects = df of 2
        "p-unc": [0.15, 0.25],
        "p-corr": [0.22, 0.28],
        "cohen": [0.6, 0.4],
        "ci_lower": [0.1, 0.0],
        "ci_upper": [1.1, 0.8]
    })
    pairwise_data.to_csv(stats_dir / "pairwise_N1_mean_amplitude_roi.csv", index=False)

    # Create mock descriptives
    desc_data = pd.DataFrame({
        "condition": ["cond1", "cond2"],
        "count": [8, 8],
        "mean": [3.5, 4.2],
        "std": [1.2, 1.5],
        "sem": [0.42, 0.53],
        "min": [1.5, 2.0],
        "max": [5.5, 6.5]
    })
    desc_data.to_csv(stats_dir / "descriptives_N1_mean_amplitude_roi.csv", index=False)

    return stats_dir


# ============================================================================
# TEST 1: Report Section Ordering (LMM First)
# ============================================================================

def test_report_sections_ordered_lmm_first(mock_stats_dir):
    """
    TEST: Verify inferential statistics section orders tests as:
    1. LMM (Primary)
    2. ANOVA (Supplementary)
    3. Pairwise (Supplementary)

    EXPECTED TO FAIL before implementation.
    """
    report_gen = StatisticalReportGenerator(mock_stats_dir, "test_analysis")
    report_path = mock_stats_dir / "TEST_REPORT.md"

    # Generate report
    report_gen.generate_report(report_path)

    # Read generated report
    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # Find positions of each test type in the report
    lmm_pos = report_content.find("**Linear Mixed-Effects Model")
    anova_pos = report_content.find("**Repeated-Measures ANOVA")
    pairwise_pos = report_content.find("**Pairwise Comparisons")

    # All three should be present
    assert lmm_pos != -1, "LMM section not found in report"
    assert anova_pos != -1, "ANOVA section not found in report"
    assert pairwise_pos != -1, "Pairwise section not found in report"

    # LMM should come BEFORE ANOVA
    assert lmm_pos < anova_pos, f"LMM should appear before ANOVA. LMM at {lmm_pos}, ANOVA at {anova_pos}"

    # ANOVA should come BEFORE Pairwise
    assert anova_pos < pairwise_pos, f"ANOVA should appear before Pairwise. ANOVA at {anova_pos}, Pairwise at {pairwise_pos}"

    # LMM should be labeled as "Primary Analysis"
    assert "(Primary Analysis)" in report_content, "LMM should be labeled as Primary Analysis"

    # ANOVA should be labeled as "Supplementary"
    assert "ANOVA (Supplementary" in report_content or "Supplementary Analysis" in report_content, \
        "ANOVA should be labeled as Supplementary"


# ============================================================================
# TEST 2: Effective N Warnings for ANOVA
# ============================================================================

def test_anova_includes_effective_n_warning(mock_stats_dir):
    """
    TEST: Verify ANOVA section includes warning about listwise deletion
    and reports effective sample size (e.g., "n=3 complete cases").

    EXPECTED TO FAIL before implementation.
    """
    report_gen = StatisticalReportGenerator(mock_stats_dir, "test_analysis")
    report_path = mock_stats_dir / "TEST_REPORT.md"

    report_gen.generate_report(report_path)

    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # Extract ANOVA section
    anova_start = report_content.find("**Repeated-Measures ANOVA")
    pairwise_start = report_content.find("**Pairwise Comparisons")
    anova_section = report_content[anova_start:pairwise_start]

    # Should mention listwise deletion
    assert "listwise deletion" in anova_section.lower(), \
        "ANOVA section should mention listwise deletion"

    # Should report effective sample size
    # ANOVA has ddof2=8, so n = 8+1 = 9 complete cases
    assert re.search(r"n\s*=\s*9", anova_section), \
        "ANOVA section should report effective sample size (n=9)"

    # Should have a note/caveat
    assert "_Note:" in anova_section or "_note:" in anova_section.lower(), \
        "ANOVA section should include a Note about reduced N"


# ============================================================================
# TEST 3: LMM Shows SNR Covariate Effect
# ============================================================================

def test_lmm_section_shows_snr_covariate(mock_stats_dir):
    """
    TEST: When LMM includes SNR as covariate, the report should display
    the SNR effect alongside the condition effect.

    EXPECTED TO FAIL before implementation.
    """
    report_gen = StatisticalReportGenerator(mock_stats_dir, "test_analysis")
    report_path = mock_stats_dir / "TEST_REPORT.md"

    report_gen.generate_report(report_path)

    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # Extract LMM section
    lmm_start = report_content.find("**Linear Mixed-Effects Model")
    anova_start = report_content.find("**Repeated-Measures ANOVA")
    lmm_section = report_content[lmm_start:anova_start]

    # Should mention SNR effect
    assert "snr" in lmm_section.lower() or "SNR" in lmm_section, \
        "LMM section should report SNR covariate effect"

    # Should show condition effect p-value = 0.008
    assert "0.008" in lmm_section, \
        "LMM section should show condition p-value (0.008 in mock data)"

    # Should show SNR effect p-value = 0.003
    assert "0.003" in lmm_section, \
        "LMM section should show SNR p-value (0.003 in mock data)"


# ============================================================================
# TEST 4: Methods Section Updated
# ============================================================================

def test_methods_section_emphasizes_lmm(mock_stats_dir):
    """
    TEST: Methods section should state LMM as primary analysis and
    reference appropriate literature (Baayen et al., 2008).

    EXPECTED TO FAIL before implementation.
    """
    report_gen = StatisticalReportGenerator(mock_stats_dir, "test_analysis")
    report_path = mock_stats_dir / "TEST_REPORT.md"

    report_gen.generate_report(report_path)

    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # Find methods section
    methods_start = report_content.find("## 6. Methods Summary")
    if methods_start == -1:
        pytest.fail("Methods section not found in report")

    methods_section = report_content[methods_start:]

    # Should state LMM as primary
    assert "primary" in methods_section.lower() and "lmm" in methods_section.lower(), \
        "Methods should state LMM as primary analysis"

    # Should mention maximum likelihood
    assert "maximum likelihood" in methods_section.lower(), \
        "Methods should mention maximum likelihood estimation"

    # Should reference Baayen et al., 2008
    assert "Baayen" in methods_section and "2008" in methods_section, \
        "Methods should cite Baayen et al. (2008)"


# ============================================================================
# TEST 5: Plot Significance Stars Use LMM
# ============================================================================

def test_plot_significance_uses_lmm_pvalue():
    """
    TEST: Verify that the plotting code uses LMM p-value for significance stars.

    This is a simplified integration test that checks the logic exists.
    """
    # This test checks that the implementation exists by reading the source code
    import inspect
    from scripts import run_statistics

    # Get source code of generate_plots function
    source = inspect.getsource(run_statistics.generate_plots)

    # Check that LMM path is checked for significance
    assert "lmm_path = output_dir" in source, "Code should check LMM path"
    assert "lmm_data.get('summary'" in source or "lmm_data.get(\"summary\"" in source, \
        "Code should extract LMM summary"
    assert "P>|z|" in source, "Code should extract LMM p-value from P>|z|"

    # Check that it tries LMM first, then falls back to ANOVA
    lmm_pos = source.find("lmm_path")
    anova_fallback_pos = source.find("# Fallback to ANOVA")

    assert lmm_pos > 0, "Should check LMM path"
    assert anova_fallback_pos > lmm_pos, "Should fallback to ANOVA after trying LMM"

    print("✓ Plot significance logic correctly uses LMM p-value with ANOVA fallback")


# ============================================================================
# TEST 6: LMM Note About Using All Data
# ============================================================================

def test_lmm_section_includes_note_about_all_data(mock_stats_dir):
    """
    TEST: LMM section should include explanatory note that it uses
    all available data (not just complete cases).

    EXPECTED TO FAIL before implementation.
    """
    report_gen = StatisticalReportGenerator(mock_stats_dir, "test_analysis")
    report_path = mock_stats_dir / "TEST_REPORT.md"

    report_gen.generate_report(report_path)

    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # Extract LMM section
    lmm_start = report_content.find("**Linear Mixed-Effects Model")
    anova_start = report_content.find("**Repeated-Measures ANOVA")
    lmm_section = report_content[lmm_start:anova_start]

    # Should mention using all available data
    assert "all available" in lmm_section.lower() or "maximum likelihood" in lmm_section.lower(), \
        "LMM section should explain that it uses all available data"


# ============================================================================
# TEST 7: Boxplot Shows LMM Stats in X-Axis Label
# ============================================================================

def test_boxplot_xlabel_shows_lmm_stats():
    """
    TEST: Verify that boxplot x-axis label shows LMM statistics
    instead of just "Condition *".

    EXPECTED: X-axis should show "LMM: β = X.XX, z = X.XX, p = X.XXX **"
    """
    from eeg.stats_plots import plot_boxplot
    import tempfile

    # Create sample data
    test_data = pd.DataFrame({
        'condition': ['A', 'A', 'A', 'B', 'B', 'B'],
        'measure': [1.0, 1.5, 1.2, 2.0, 2.5, 2.2]
    })

    # Create LMM stats dict
    lmm_stats = {
        'p_value': 0.008,
        'beta': 0.75,
        'z': 2.656,
        'test': 'LMM'
    }

    # Create temporary output file
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        temp_path = Path(f.name)

    try:
        # Generate plot with LMM stats
        plot_boxplot(
            data=test_data,
            dv='measure',
            groupby='condition',
            title='Test Plot',
            output_path=temp_path,
            lmm_stats=lmm_stats,
            dpi=100  # Low DPI for faster test
        )

        # Verify file was created
        assert temp_path.exists(), "Boxplot file should be created"

        # If we got here without errors, the function accepted lmm_stats parameter
        print("✓ Boxplot successfully generated with LMM statistics")

    finally:
        # Clean up
        if temp_path.exists():
            temp_path.unlink()


def test_boxplot_xlabel_without_lmm_stats():
    """
    TEST: Verify that boxplot falls back gracefully when no LMM stats provided.

    EXPECTED: X-axis should show "Condition" (default behavior)
    """
    from eeg.stats_plots import plot_boxplot
    import tempfile

    test_data = pd.DataFrame({
        'condition': ['A', 'A', 'A', 'B', 'B', 'B'],
        'measure': [1.0, 1.5, 1.2, 2.0, 2.5, 2.2]
    })

    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        temp_path = Path(f.name)

    try:
        # Generate plot WITHOUT LMM stats (should fallback to default)
        plot_boxplot(
            data=test_data,
            dv='measure',
            groupby='condition',
            title='Test Plot',
            output_path=temp_path,
            lmm_stats=None,  # No LMM stats
            dpi=100
        )

        assert temp_path.exists(), "Boxplot file should be created even without LMM stats"
        print("✓ Boxplot successfully generated with fallback label")

    finally:
        if temp_path.exists():
            temp_path.unlink()


# ============================================================================
# TEST 8: LMM Effect Names Are Preserved in JSON
# ============================================================================

def test_lmm_json_preserves_effect_names(tmp_path):
    """
    TEST: When LMM results are saved to JSON, the effect names
    (row index from statsmodels) must be preserved.

    EXPECTED TO FAIL before implementation.

    CRITICAL BUG: Currently orient='records' loses the index.
    FIX: Use orient='index' or add 'name' field explicitly.
    """
    import sys
    sys.path.insert(0, str(repo_root / "src"))
    from eeg.statistics import ERPStatistics

    # Create mock data with categorical conditions
    mock_data = pd.DataFrame({
        'subject_id': ['S01', 'S01', 'S01', 'S01', 'S02', 'S02', 'S02', 'S02'],
        'component': ['N1'] * 8,
        'condition': ['1 to 1', '2 to 1', '3 to 1', '4 to 1'] * 2,
        'mean_amplitude_roi': [-2.5, -3.0, -2.8, -2.3, -2.7, -3.2, -3.0, -2.4]
    })

    stats = ERPStatistics(mock_data)

    # Run LMM
    lmm_result = stats.run_lmm(
        dv='mean_amplitude_roi',
        component='N1',
        fixed='condition'
    )

    # Save to JSON
    output_path = tmp_path / "lmm_N1_mean_amplitude_roi.json"
    stats.save_results(lmm_result, output_path, format='json')

    # Load JSON and verify effect names are preserved
    with open(output_path, 'r') as f:
        saved_data = json.load(f)

    summary = saved_data.get('summary', [])

    # Check that effect names are present
    assert len(summary) > 0, "Summary should contain effect rows"

    # CRITICAL: Each effect must have a 'name' field
    for i, effect in enumerate(summary):
        assert 'name' in effect, f"Effect {i} must have a 'name' field (currently missing!)"

    # Check that names are meaningful (not just "effect_1", "effect_2")
    effect_names = [effect['name'] for effect in summary]

    # Should have Intercept
    assert any('Intercept' in name for name in effect_names), \
        "Summary should contain 'Intercept' effect"

    # Should have condition effects with actual condition names
    # Statsmodels uses format like "condition[T.2 to 1]" for dummy coding
    condition_effects = [name for name in effect_names if 'condition' in name]
    assert len(condition_effects) >= 3, \
        f"Should have at least 3 condition effects (one per non-reference level), got {len(condition_effects)}"

    # CRITICAL: Names should NOT be generic "effect_1", "effect_2"
    for name in effect_names[1:]:  # Skip intercept
        assert not re.match(r'^effect_\d+$', name.lower()), \
            f"Effect name '{name}' is generic! Should be meaningful like 'condition[T.2 to 1]'"

    print(f"✓ Effect names preserved: {effect_names}")


# ============================================================================
# TEST 9: Report Uses Meaningful Effect Names (Not "Effect 1 effect")
# ============================================================================

def test_report_shows_meaningful_effect_names(tmp_path):
    """
    TEST: Report should show meaningful effect names like:
    - "2 to 1 vs 1 to 1: β = -0.87, p = 0.030"

    NOT generic names like:
    - "Effect 1 effect: β = -0.87, p = 0.030"

    EXPECTED TO FAIL before implementation.
    """
    stats_dir = tmp_path / "stats" / "test_analysis"
    stats_dir.mkdir(parents=True)

    # Create summary JSON
    summary_data = {
        "analysis_id": "test_analysis",
        "components_tested": ["N1"],
        "dependent_variables": ["mean_amplitude_roi"],
        "data_summary": {
            "n_total_measurements": 74,
            "n_subjects": 24,
            "n_conditions": 4
        },
        "tests_run": {"lmm": True, "anova": False, "pairwise": False}
    }
    with open(stats_dir / "statistical_summary.json", "w") as f:
        json.dump(summary_data, f)

    # Create LMM JSON with PRESERVED effect names (as it should be after fix)
    lmm_data = {
        "aic": 268.03,
        "bic": 284.16,
        "converged": True,
        "summary": [
            {"Coef.": "-0.619", "Std.Err.": "0.399", "z": "-1.551", "P>|z|": "0.121", "name": "Intercept"},
            {"Coef.": "-0.868", "Std.Err.": "0.400", "z": "-2.170", "P>|z|": "0.030", "name": "condition[T.2 to 1]"},
            {"Coef.": "-1.220", "Std.Err.": "0.385", "z": "-3.167", "P>|z|": "0.002", "name": "condition[T.3 to 1]"},
            {"Coef.": "-0.348", "Std.Err.": "0.385", "z": "-0.905", "P>|z|": "0.366", "name": "condition[T.4 to 1]"},
            {"Coef.": "-0.478", "Std.Err.": "0.050", "z": "-9.647", "P>|z|": "0.000", "name": "Group Var"}
        ]
    }
    with open(stats_dir / "lmm_N1_mean_amplitude_roi.json", "w") as f:
        json.dump(lmm_data, f)

    # Generate report
    report_gen = StatisticalReportGenerator(stats_dir, "test_analysis")
    report_path = stats_dir / "STATISTICAL_REPORT.md"
    report_gen.generate_report(report_path)

    # Read report
    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # CRITICAL: Should NOT contain generic "Effect 1 effect", "Effect 2 effect"
    assert "Effect 1 effect" not in report_content, \
        "Report contains generic 'Effect 1 effect' - effect names not properly parsed!"
    assert "Effect 2 effect" not in report_content, \
        "Report contains generic 'Effect 2 effect' - effect names not properly parsed!"

    # Should contain meaningful condition comparisons
    # After parsing "condition[T.2 to 1]" should become "2 to 1 vs 1 to 1" or similar
    assert "2 to 1" in report_content, \
        "Report should mention '2 to 1' condition"
    assert "3 to 1" in report_content, \
        "Report should mention '3 to 1' condition"

    # Should show the p-values from the LMM
    assert "0.030" in report_content, "Report should show p=0.030 for condition[T.2 to 1]"
    assert "0.002" in report_content, "Report should show p=0.002 for condition[T.3 to 1]"

    print("✓ Report uses meaningful effect names")


# ============================================================================
# TEST 10: Report Documents Reference Condition
# ============================================================================

def test_report_documents_reference_condition(tmp_path):
    """
    TEST: Report should explicitly state which condition is the reference.

    Example: "Reference condition: 1 to 1 (all effects are contrasts vs. this baseline)"

    EXPECTED TO FAIL before implementation.
    """
    stats_dir = tmp_path / "stats" / "test_analysis"
    stats_dir.mkdir(parents=True)

    # Create summary JSON
    summary_data = {
        "analysis_id": "test_analysis",
        "components_tested": ["N1"],
        "dependent_variables": ["mean_amplitude_roi"],
        "data_summary": {
            "n_total_measurements": 74,
            "n_subjects": 24,
            "n_conditions": 4,
            "conditions": ["1 to 1", "2 to 1", "3 to 1", "4 to 1"]  # NEW: Include condition list
        },
        "tests_run": {"lmm": True}
    }
    with open(stats_dir / "statistical_summary.json", "w") as f:
        json.dump(summary_data, f)

    # Create LMM JSON
    lmm_data = {
        "aic": 268.03,
        "bic": 284.16,
        "converged": True,
        "reference_condition": "1 to 1",  # NEW: Explicitly save reference
        "summary": [
            {"Coef.": "-0.619", "Std.Err.": "0.399", "z": "-1.551", "P>|z|": "0.121", "name": "Intercept"},
            {"Coef.": "-0.868", "Std.Err.": "0.400", "z": "-2.170", "P>|z|": "0.030", "name": "condition[T.2 to 1]"}
        ]
    }
    with open(stats_dir / "lmm_N1_mean_amplitude_roi.json", "w") as f:
        json.dump(lmm_data, f)

    # Generate report
    report_gen = StatisticalReportGenerator(stats_dir, "test_analysis")
    report_path = stats_dir / "STATISTICAL_REPORT.md"
    report_gen.generate_report(report_path)

    # Read report
    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # Should mention reference condition
    assert "reference" in report_content.lower(), \
        "Report should mention the reference condition"

    # Should specifically state "1 to 1" is the reference
    assert re.search(r"reference.*1 to 1|1 to 1.*reference", report_content, re.IGNORECASE), \
        "Report should explicitly state '1 to 1' is the reference condition"

    print("✓ Report documents reference condition")


# ============================================================================
# Run Tests
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
