# LMM Pairwise Comparisons Implementation Plan

## Executive Summary

**Goal**: Add full pairwise comparison support for Linear Mixed-Effects Models (LMM) to answer the research question: *"Do the conditions differ from each other?"* (e.g., is 1 to 3 different from 1 to 4?)

**Current State**:
- ✓ LMM shows overall condition effects vs. reference (e.g., "1 to 2 vs 1 to 1")
- ✗ Missing: Direct comparisons between non-reference conditions (e.g., "1 to 3 vs 1 to 4")

**Target State**:
- ✓ LMM provides ALL pairwise comparisons with proper multiple comparison corrections
- ✓ Results integrated into analysis workflow and reports
- ✓ Uses 2025 Python best practices (statsmodels native `t_test_pairwise`)

---

## Research: 2025 Python Best Practices

### Key Findings

#### Option 1: statsmodels `t_test_pairwise()` (RECOMMENDED)
- **Status**: Native support in statsmodels 0.14.0+
- **Method**: `MixedLMResults.t_test_pairwise(term_name, method='hs')`
- **Pros**:
  - Native to statsmodels (no additional dependencies)
  - Handles mixed models correctly
  - Built-in multiple comparison corrections
  - Actively maintained
- **Cons**:
  - Less flexible than R's emmeans
  - Documentation is sparse

**Example Usage**:
```python
from statsmodels.formula.api import mixedlm

# Fit model
model = mixedlm("amplitude ~ condition", data, groups=data['subject_id'])
result = model.fit()

# Pairwise comparisons
pairwise = result.t_test_pairwise('condition', method='hs')
print(pairwise.result_frame)
```

#### Option 2: Manual Calculation via Contrasts
- **Status**: Always available
- **Method**: Manually construct contrast matrices
- **Pros**: Maximum control
- **Cons**: Complex, error-prone, requires deep statistical knowledge

#### Option 3: R via rpy2 (emmeans)
- **Status**: Available but requires R installation
- **Pros**: Gold-standard (emmeans package)
- **Cons**: Additional dependency, complexity

### Decision: Use statsmodels `t_test_pairwise()` ✓

**Rationale**:
1. Native Python solution (no R dependency)
2. Officially supported by statsmodels
3. Proper handling of LMM structure
4. Built-in multiple comparison corrections
5. Consistent with existing codebase

---

## Technical Design

### 1. New Method: `ERPStatistics.run_lmm_pairwise()`

**Location**: `src/eeg/statistics.py`

**Signature**:
```python
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

    Parameters
    ----------
    dv : str
        Dependent variable (e.g., 'mean_amplitude_roi').
    component : str
        ERP component (e.g., 'N1').
    fixed : str
        Fixed effects formula (e.g., 'condition').
    random : str, default='subject_id'
        Random effects grouping variable.
    correction : str, default='hs'
        Multiple comparison correction method:
        - 'hs': Holm-Sidak (recommended)
        - 'bonferroni': Bonferroni correction
        - 'fdr_bh': Benjamini-Hochberg FDR
    **filter_kwargs
        Additional filtering arguments.

    Returns
    -------
    pd.DataFrame
        Pairwise comparison results with columns:
        - Contrast: Comparison being made (e.g., "1 to 1 - 1 to 2")
        - Coef: Estimated difference
        - Std.Err.: Standard error
        - z: z-statistic
        - P>|z|: Unadjusted p-value
        - P>|z| (adj): Adjusted p-value

    Examples
    --------
    >>> stats = ERPStatistics('subject_measurements.csv')
    >>> pairwise = stats.run_lmm_pairwise(
    ...     dv='mean_amplitude_roi',
    ...     component='N1',
    ...     fixed='condition',
    ...     correction='hs'
    ... )
    >>> print(pairwise[pairwise['P>|z| (adj)'] < 0.05])
    """
```

**Implementation Steps**:
1. Filter data (same as `run_lmm()`)
2. Fit the LMM model
3. Call `result.t_test_pairwise()` with the categorical term
4. Extract results into DataFrame
5. Format for readability

**Algorithm**:
```python
# 1. Filter data
filtered = self.filter_data(component=component, dropna=True, **filter_kwargs)

# 2. Build and fit model
formula = f"{dv} ~ {fixed}"
model = mixedlm(formula, filtered, groups=filtered[random])
fitted_model = model.fit(method='lbfgs', reml=False)

# 3. Run pairwise comparisons
# Extract the categorical term name (e.g., "condition")
term_name = fixed.split('+')[0].strip()  # Handle "condition + snr"
pairwise_result = fitted_model.t_test_pairwise(term_name, method=correction)

# 4. Extract and format results
result_df = pairwise_result.result_frame
result_df = result_df.rename(columns={
    'P>|z| (corrected)': 'P>|z| (adj)'
})

# 5. Add readable comparison names
result_df = result_df.reset_index()
result_df = result_df.rename(columns={'index': 'Contrast'})

return result_df
```

---

### 2. Integration into `run_statistics.py`

**Location**: `scripts/run_statistics.py`

**New Function**: `run_lmm_pairwise_tests()`

```python
def run_lmm_pairwise_tests(stats: ERPStatistics, cfg: dict, output_dir: Path):
    """Run LMM pairwise comparisons for all components and DVs."""
    print_header("Running LMM Pairwise Comparisons", level=1)

    lmm_pairwise_cfg = cfg['tests'].get('lmm_pairwise', {})
    if not lmm_pairwise_cfg.get('enabled', False):
        print("  [SKIPPED] LMM pairwise tests disabled in config")
        return {}

    results = {}

    for component in cfg['components']:
        for dv in cfg['dependent_variables']:
            print(f"  Testing: {component} - {dv}")

            try:
                result = stats.run_lmm_pairwise(
                    dv=dv,
                    component=component,
                    fixed=lmm_pairwise_cfg.get('fixed', 'condition'),
                    random=lmm_pairwise_cfg.get('random', 'subject_id'),
                    correction=lmm_pairwise_cfg.get('correction', 'hs')
                )

                # Save result
                output_filename = f"lmm_pairwise_{component}_{dv}.csv"
                output_path = output_dir / output_filename
                stats.save_results(result, output_path, format='csv')

                # Store summary
                key = f"{component}_{dv}"
                alpha = cfg['advanced']['alpha']
                sig_comparisons = result[result['P>|z| (adj)'] < alpha]

                results[key] = {
                    'component': component,
                    'dv': dv,
                    'test': 'LMM_Pairwise',
                    'n_comparisons': len(result),
                    'n_significant': len(sig_comparisons),
                    'correction': lmm_pairwise_cfg.get('correction', 'hs'),
                    'output_file': str(output_filename)
                }

            except Exception as e:
                print(f"    ERROR: {e}")
                results[f"{component}_{dv}"] = {'error': str(e)}

    return results
```

**Integration Point** (in `main()` function):
```python
# After run_lmm_tests()
if cfg['tests'].get('lmm_pairwise', {}).get('enabled', False):
    lmm_pairwise_results = run_lmm_pairwise_tests(stats, cfg, output_dir)
    all_results['lmm_pairwise'] = lmm_pairwise_results
```

---

### 3. Configuration File Updates

**Location**: `configs/statistics/*.yaml`

**New Configuration Section**:
```yaml
tests:
  lmm_pairwise:
    enabled: true
    fixed: 'condition'
    random: 'subject_id'
    correction: 'hs'  # Options: 'hs', 'bonferroni', 'fdr_bh'
    output_format: 'csv'
```

---

### 4. Summary Report Updates

**Location**: `src/eeg/summary_report.py`

**New Section**: Add LMM pairwise comparisons after main LMM section

**Template**:
```markdown
#### LMM Pairwise Comparisons ({correction} correction)

All pairwise comparisons between conditions:

| Comparison | β | SE | z | p (unadj) | p (adj) | Sig |
|------------|---|----|----|-----------|---------|-----|
| 1 to 1 - 1 to 2 | -0.69 | 0.47 | -1.47 | 0.141 | 0.423 | n.s. |
| 1 to 1 - 1 to 3 | -0.89 | 0.46 | -1.92 | 0.056 | 0.224 | n.s. |
| 1 to 1 - 1 to 4 | -1.50 | 0.47 | -3.20 | 0.001 | 0.008 | ** |
| 1 to 2 - 1 to 3 | -0.20 | 0.46 | -0.43 | 0.665 | 0.665 | n.s. |
| 1 to 2 - 1 to 4 | -0.81 | 0.47 | -1.73 | 0.084 | 0.252 | n.s. |
| **1 to 3 - 1 to 4** | **-0.61** | **0.46** | **-1.33** | **0.184** | **0.368** | **n.s.** |

_Note: p-values adjusted using Holm-Sidak method for 6 comparisons._
```

---

## TDD Implementation Workflow

### Phase 1: RED (Tests Fail) ✓

1. **Write tests first** (DONE: `test_lmm_pairwise_comparisons.py`)
   - 10 comprehensive tests covering all functionality
   - Tests MUST fail initially

2. **Run tests to confirm they fail**:
   ```bash
   pytest tests/test_lmm_pairwise_comparisons.py -v
   ```
   Expected: All 10 tests FAIL ❌

---

### Phase 2: GREEN (Make Tests Pass)

3. **Implement `run_lmm_pairwise()` method**
   - Location: `src/eeg/statistics.py`
   - Use statsmodels `t_test_pairwise()`
   - Handle errors gracefully

4. **Test incrementally**:
   ```bash
   pytest tests/test_lmm_pairwise_comparisons.py::test_lmm_pairwise_method_exists -v
   ```
   Run one test at a time until all pass

5. **Integrate into workflow**
   - Add `run_lmm_pairwise_tests()` to `run_statistics.py`
   - Update configuration files
   - Update summary report generator

6. **Run full test suite**:
   ```bash
   pytest tests/test_lmm_pairwise_comparisons.py -v
   ```
   Expected: All 10 tests PASS ✓

---

### Phase 3: REFACTOR (Clean Up)

7. **Code review**:
   - Check for code duplication
   - Ensure proper documentation
   - Verify error handling

8. **Integration tests**:
   - Run on real data
   - Verify outputs match expectations
   - Check report formatting

9. **Documentation**:
   - Update README
   - Add usage examples
   - Document configuration options

---

## Validation Strategy

### Statistical Validation

1. **Comparison with R emmeans** (optional but recommended):
   - Run same data through R's emmeans package
   - Verify coefficients and p-values match (within numerical precision)

2. **Consistency checks**:
   - Verify "1 to 2 vs 1 to 1" from pairwise matches main LMM result
   - Check that C(n, 2) comparisons are generated for n conditions

3. **Edge cases**:
   - Test with missing data
   - Test with unbalanced designs
   - Test with 2 conditions (1 comparison)
   - Test with many conditions (many comparisons)

---

## Expected Outputs

### File Structure
```
docs/assets/stats/from_1_ACC1/
├── lmm_N1_mean_amplitude_roi.json          # Existing: Main LMM
├── lmm_pairwise_N1_mean_amplitude_roi.csv  # NEW: Pairwise comparisons
├── anova_N1_mean_amplitude_roi.csv         # Existing: ANOVA
├── pairwise_N1_mean_amplitude_roi.csv      # Existing: ANOVA pairwise
└── STATISTICAL_REPORT.md                    # Updated: Includes LMM pairwise
```

### Example Output CSV

**lmm_pairwise_N1_mean_amplitude_roi.csv**:
```csv
Contrast,Coef,Std.Err.,z,P>|z|,P>|z| (adj)
1 to 1 - 1 to 2,-0.69,0.467,-1.472,0.141,0.423
1 to 1 - 1 to 3,-0.89,0.462,-1.915,0.056,0.224
1 to 1 - 1 to 4,-1.50,0.469,-3.203,0.001,0.008
1 to 2 - 1 to 3,-0.20,0.456,-0.438,0.661,0.661
1 to 2 - 1 to 4,-0.81,0.471,-1.719,0.086,0.258
1 to 3 - 1 to 4,-0.61,0.465,-1.311,0.190,0.380
```

---

## Success Criteria

### Must Have ✓
- [ ] All 10 TDD tests pass
- [ ] `run_lmm_pairwise()` method implemented and working
- [ ] Integration into `run_statistics.py` complete
- [ ] CSV output files generated
- [ ] Summary report includes pairwise section

### Should Have ✓
- [ ] Multiple comparison corrections working (hs, bonferroni, fdr_bh)
- [ ] Error handling for edge cases
- [ ] Configuration options documented
- [ ] Example usage in documentation

### Nice to Have
- [ ] Comparison with R emmeans (validation)
- [ ] Effect sizes for pairwise comparisons
- [ ] Confidence intervals for differences
- [ ] Visualization of pairwise comparisons

---

## Timeline

| Phase | Task | Duration | Status |
|-------|------|----------|--------|
| 1 | Research & Planning | 1 hour | ✓ DONE |
| 2 | Write TDD Tests | 1 hour | ✓ DONE |
| 3 | Implement `run_lmm_pairwise()` | 2 hours | NEXT |
| 4 | Integration & Testing | 2 hours | Pending |
| 5 | Documentation & Cleanup | 1 hour | Pending |
| **Total** | | **~7 hours** | |

---

## References

### Python Documentation
- [statsmodels MixedLMResults.t_test_pairwise](https://www.statsmodels.org/dev/generated/statsmodels.regression.mixed_linear_model.MixedLMResults.t_test_pairwise.html)
- [statsmodels Linear Mixed Effects Models](https://www.statsmodels.org/stable/mixed_linear.html)

### Statistical Methods
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65-70.
- Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects modeling with crossed random effects for subjects and items. *Journal of Memory and Language*, 59(4), 390-412.

### R Comparison (for validation)
- Lenth, R. V. (2021). emmeans: Estimated Marginal Means. R package.

---

## Notes for Implementation

### Critical Points
1. **Contrast Coding**: statsmodels uses treatment coding by default (first level alphabetically is reference)
2. **Multiple Comparisons**: Holm-Sidak is recommended (less conservative than Bonferroni, more powerful)
3. **Missing Data**: LMM handles missing data via maximum likelihood (already implemented in `run_lmm()`)
4. **Degrees of Freedom**: LMM uses z-tests (not t-tests) because of asymptotic theory

### Common Pitfalls
- Don't forget to sort conditions alphabetically (statsmodels does this internally)
- Remember to reset index when extracting results (or contrast names get lost)
- Ensure filter settings match between `run_lmm()` and `run_lmm_pairwise()`

---

**Document Version**: 1.0
**Last Updated**: 2025-01-18
**Author**: Research Team
**Status**: Ready for Implementation 🚀
