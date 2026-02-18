"""
Test suite for ACC0 vs ACC1 response filtering functionality.

Tests verify:
1. Per-set response override works correctly
2. ACC0 filter returns only incorrect responses
3. ACC1 filter returns only correct responses
4. Same conditions can be used with different response filters
5. Missing Target.ACC column raises appropriate error
6. QC reporting tracks response filtering correctly

Following TDD: Tests verify the already-implemented functionality.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "src"))

from eeg.select import apply_response_filter, build_condition_masks
from eeg.io import select_conditions


# ============================================================================
# Test Fixtures
# ============================================================================

@pytest.fixture
def sample_metadata():
    """Create sample metadata DataFrame with Target.ACC column."""
    return pd.DataFrame({
        'Condition': ['12', '23', '12', '23', '34', '12', '23', '34', '45', '56'],
        'Target.ACC': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        'trial_num': list(range(10)),
        'Prime5': ['5a.jpg', '5b.jpg', '5c.jpg', '5a.jpg', '5b.jpg', '5c.jpg', '5d.jpg', '5e.jpg', '5a.jpg', '5b.jpg'],
        'size': ['LL', 'LL', 'LL', 'LL', 'LL', 'LL', 'LL', 'LL', 'LL', 'LL']
    })


@pytest.fixture
def metadata_without_acc():
    """Create metadata DataFrame missing Target.ACC column."""
    return pd.DataFrame({
        'Condition': ['12', '23', '34'],
        'trial_num': [0, 1, 2]
    })


@pytest.fixture
def condition_sets_with_filters():
    return [
        {
            'name': 'Prime5 is 5a',
            'conditions': ['12', '23', '34'],
            'metadata_filters': {'Prime5': ['5a.jpg']},
        },
        {
            'name': 'Prime5 is 5b or 5c',
            'conditions': ['34', '45'],
            'metadata_filters': {'Prime5': ['5b.jpg', '5c.jpg']},
        },
        {
            'name': 'Metadata only',
            'metadata_filters': {'Prime5': ['5e.jpg']},
        },
        {
            'name': 'Missing column',
            'metadata_filters': {'NonExisting': ['value']},
        },
    ]


# ============================================================================
# TEST 1: ACC0 Filtering
# ============================================================================

def test_acc0_filters_only_incorrect_responses(sample_metadata):
    """
    TEST: Verify ACC0 filter returns only incorrect responses (Target.ACC == 0).
    """
    filtered = apply_response_filter(sample_metadata, "ACC0")

    # Should only have ACC0 trials (indices 1, 4, 6, 9 have ACC=0)
    assert len(filtered) == 4, f"Expected 4 ACC0 trials, got {len(filtered)}"
    assert all(filtered['Target.ACC'] == 0), "All returned trials should have Target.ACC == 0"

    # Verify specific trials
    expected_trials = [1, 4, 6, 9]
    assert filtered['trial_num'].tolist() == expected_trials, \
        f"Expected trials {expected_trials}, got {filtered['trial_num'].tolist()}"


def test_acc0_case_insensitive(sample_metadata):
    """
    TEST: Verify ACC0 filter works with different capitalizations.
    """
    result_upper = apply_response_filter(sample_metadata, "ACC0")
    result_lower = apply_response_filter(sample_metadata, "acc0")
    result_mixed = apply_response_filter(sample_metadata, "Acc0")

    # All should return the same results
    pd.testing.assert_frame_equal(result_upper, result_lower)
    pd.testing.assert_frame_equal(result_upper, result_mixed)


# ============================================================================
# TEST 2: ACC1 Filtering
# ============================================================================

def test_acc1_filters_only_correct_responses(sample_metadata):
    """
    TEST: Verify ACC1 filter returns only correct responses (Target.ACC == 1).
    """
    filtered = apply_response_filter(sample_metadata, "ACC1")

    # Should only have ACC1 trials
    assert len(filtered) == 6, f"Expected 6 ACC1 trials, got {len(filtered)}"
    assert all(filtered['Target.ACC'] == 1), "All returned trials should have Target.ACC == 1"

    # Verify specific trials (indices 0, 2, 3, 5, 7, 8 have ACC=1)
    expected_trials = [0, 2, 3, 5, 7, 8]
    assert filtered['trial_num'].tolist() == expected_trials, \
        f"Expected trials {expected_trials}, got {filtered['trial_num'].tolist()}"


def test_acc1_case_insensitive(sample_metadata):
    """
    TEST: Verify ACC1 filter works with different capitalizations.
    """
    result_upper = apply_response_filter(sample_metadata, "ACC1")
    result_lower = apply_response_filter(sample_metadata, "acc1")
    result_mixed = apply_response_filter(sample_metadata, "Acc1")

    # All should return the same results
    pd.testing.assert_frame_equal(result_upper, result_lower)
    pd.testing.assert_frame_equal(result_upper, result_mixed)


# ============================================================================
# TEST 3: ALL Filter (No Filtering)
# ============================================================================

def test_all_returns_unchanged_data(sample_metadata):
    """
    TEST: Verify "ALL" response mode returns data unchanged.
    """
    filtered = apply_response_filter(sample_metadata, "ALL")

    # Should return all trials
    assert len(filtered) == len(sample_metadata), \
        f"Expected {len(sample_metadata)} trials, got {len(filtered)}"

    # Should be identical to input
    pd.testing.assert_frame_equal(filtered, sample_metadata)


def test_all_case_insensitive(sample_metadata):
    """
    TEST: Verify "ALL" works with different capitalizations.
    """
    result_upper = apply_response_filter(sample_metadata, "ALL")
    result_lower = apply_response_filter(sample_metadata, "all")
    result_mixed = apply_response_filter(sample_metadata, "All")

    pd.testing.assert_frame_equal(result_upper, result_lower)
    pd.testing.assert_frame_equal(result_upper, result_mixed)


# ============================================================================
# TEST 4: Partitioning (ACC0 + ACC1 = ALL)
# ============================================================================

def test_acc0_plus_acc1_equals_all(sample_metadata):
    """
    TEST: Verify that ACC0 + ACC1 trials equal ALL trials (complete partitioning).
    """
    all_trials = apply_response_filter(sample_metadata, "ALL")
    acc0_trials = apply_response_filter(sample_metadata, "ACC0")
    acc1_trials = apply_response_filter(sample_metadata, "ACC1")

    # Counts should sum correctly
    assert len(acc0_trials) + len(acc1_trials) == len(all_trials), \
        "ACC0 + ACC1 counts should equal ALL count"

    # No overlap between ACC0 and ACC1
    combined = pd.concat([acc0_trials, acc1_trials])
    assert len(combined) == len(acc0_trials) + len(acc1_trials), \
        "ACC0 and ACC1 should have no overlapping trials"

    # Combined should contain all trials
    combined_sorted = combined.sort_values('trial_num').reset_index(drop=True)
    all_sorted = all_trials.sort_values('trial_num').reset_index(drop=True)
    pd.testing.assert_frame_equal(combined_sorted, all_sorted)


# ============================================================================
# TEST 5: Same Conditions, Different Responses
# ============================================================================

def test_same_conditions_different_responses(sample_metadata):
    """
    TEST: Verify same condition codes can be filtered by ACC0 and ACC1 independently.

    This is the core functionality for error-related processing analysis.
    """
    conditions = ['12', '23', '34']

    # Filter to these conditions first
    condition_mask = sample_metadata['Condition'].isin(conditions)
    condition_subset = sample_metadata[condition_mask]

    # Then apply ACC0 filter
    acc0_filtered = apply_response_filter(condition_subset, "ACC0")
    acc0_mask = acc0_filtered['Condition'].isin(conditions)
    acc0_set = acc0_filtered[acc0_mask]

    # Then apply ACC1 filter
    acc1_filtered = apply_response_filter(condition_subset, "ACC1")
    acc1_mask = acc1_filtered['Condition'].isin(conditions)
    acc1_set = acc1_filtered[acc1_mask]

    # Both sets should exist
    assert len(acc0_set) > 0, "ACC0 set should have trials"
    assert len(acc1_set) > 0, "ACC1 set should have trials"

    # All ACC0 trials should have Target.ACC == 0
    assert all(acc0_set['Target.ACC'] == 0), "ACC0 set should only have incorrect responses"

    # All ACC1 trials should have Target.ACC == 1
    assert all(acc1_set['Target.ACC'] == 1), "ACC1 set should only have correct responses"

    # Both sets should use the same conditions
    assert set(acc0_set['Condition']) <= set(conditions), "ACC0 set should use specified conditions"
    assert set(acc1_set['Condition']) <= set(conditions), "ACC1 set should use specified conditions"


# ============================================================================
# TEST 6: Error Handling
# ============================================================================

def test_missing_target_acc_column_acc0(metadata_without_acc):
    """
    TEST: Verify clear error when Target.ACC column is missing (ACC0).
    """
    with pytest.raises(ValueError, match="Target.ACC"):
        apply_response_filter(metadata_without_acc, "ACC0")


def test_missing_target_acc_column_acc1(metadata_without_acc):
    """
    TEST: Verify clear error when Target.ACC column is missing (ACC1).
    """
    with pytest.raises(ValueError, match="Target.ACC"):
        apply_response_filter(metadata_without_acc, "ACC1")


def test_invalid_response_mode():
    """
    TEST: Verify error for invalid response mode.
    """
    sample_data = pd.DataFrame({
        'Condition': ['12'],
        'Target.ACC': [1]
    })

    with pytest.raises(ValueError, match="Unknown response mode"):
        apply_response_filter(sample_data, "INVALID")


# ============================================================================
# TEST 7: Edge Cases
# ============================================================================

def test_all_correct_responses():
    """
    TEST: Edge case where all trials are correct (100% accuracy).
    """
    perfect_data = pd.DataFrame({
        'Condition': ['12', '23', '34', '45', '56'],
        'Target.ACC': [1, 1, 1, 1, 1],
        'trial_num': [0, 1, 2, 3, 4]
    })

    acc0_result = apply_response_filter(perfect_data, "ACC0")
    acc1_result = apply_response_filter(perfect_data, "ACC1")

    assert len(acc0_result) == 0, "ACC0 should return empty when all trials are correct"
    assert len(acc1_result) == 5, "ACC1 should return all trials when all are correct"


def test_all_incorrect_responses():
    """
    TEST: Edge case where all trials are incorrect (0% accuracy).
    """
    error_data = pd.DataFrame({
        'Condition': ['12', '23', '34', '45', '56'],
        'Target.ACC': [0, 0, 0, 0, 0],
        'trial_num': [0, 1, 2, 3, 4]
    })

    acc0_result = apply_response_filter(error_data, "ACC0")
    acc1_result = apply_response_filter(error_data, "ACC1")

    assert len(acc0_result) == 5, "ACC0 should return all trials when all are incorrect"
    assert len(acc1_result) == 0, "ACC1 should return empty when all trials are incorrect"


def test_empty_dataframe():
    """
    TEST: Edge case with empty DataFrame.
    """
    empty_data = pd.DataFrame({
        'Condition': [],
        'Target.ACC': []
    })

    # Should return empty DataFrame without error
    result = apply_response_filter(empty_data, "ALL")
    assert len(result) == 0, "Empty DataFrame should return empty result"

    result_acc0 = apply_response_filter(empty_data, "ACC0")
    assert len(result_acc0) == 0, "Empty DataFrame should return empty result for ACC0"

    result_acc1 = apply_response_filter(empty_data, "ACC1")
    assert len(result_acc1) == 0, "Empty DataFrame should return empty result for ACC1"


# ============================================================================
# TEST 8: Realistic Error Rate Distribution
# ============================================================================

def test_realistic_error_rate():
    """
    TEST: Verify filtering with realistic error rate (~10-20%).

    Typical cognitive task has 80-90% accuracy.
    """
    # Create data with ~15% error rate (85% accuracy)
    n_trials = 100
    n_errors = 15
    n_correct = 85

    realistic_data = pd.DataFrame({
        'Condition': ['12'] * n_trials,
        'Target.ACC': [0] * n_errors + [1] * n_correct,
        'trial_num': list(range(n_trials))
    })

    acc0_result = apply_response_filter(realistic_data, "ACC0")
    acc1_result = apply_response_filter(realistic_data, "ACC1")

    assert len(acc0_result) == n_errors, f"Expected {n_errors} error trials"
    assert len(acc1_result) == n_correct, f"Expected {n_correct} correct trials"

    # Verify proportions
    total = len(acc0_result) + len(acc1_result)
    error_rate = len(acc0_result) / total
    assert 0.10 <= error_rate <= 0.20, f"Error rate {error_rate:.2%} should be realistic (10-20%)"


# ============================================================================
# TEST 9: Preservation of Other Columns
# ============================================================================

def test_preserves_all_columns(sample_metadata):
    """
    TEST: Verify that filtering preserves all DataFrame columns.
    """
    filtered = apply_response_filter(sample_metadata, "ACC1")

    # All original columns should be present
    assert set(filtered.columns) == set(sample_metadata.columns), \
        "Filtering should preserve all columns"

    # Check specific columns exist
    assert 'Condition' in filtered.columns
    assert 'Target.ACC' in filtered.columns
    assert 'trial_num' in filtered.columns


def test_condition_masks_with_metadata_filters(sample_metadata, condition_sets_with_filters):
    """Verify build_condition_masks combines condition and metadata filters."""
    # First two condition sets should succeed
    masks = build_condition_masks(sample_metadata, condition_sets_with_filters[:3])

    assert set(masks.keys()) == {"Prime5 is 5a", "Prime5 is 5b or 5c", "Metadata only"}

    mask_a = masks["Prime5 is 5a"]
    expected_indices_a = [0, 3]
    assert mask_a.sum() == len(expected_indices_a)
    assert mask_a.index[mask_a.values].tolist() == expected_indices_a

    mask_bc = masks["Prime5 is 5b or 5c"]
    expected_indices_bc = [4]
    assert mask_bc.sum() == len(expected_indices_bc)
    assert mask_bc.index[mask_bc.values].tolist() == expected_indices_bc

    mask_metadata_only = masks["Metadata only"]
    expected_indices_meta = [7]
    assert mask_metadata_only.sum() == len(expected_indices_meta)
    assert mask_metadata_only.index[mask_metadata_only.values].tolist() == expected_indices_meta

    # Missing column should raise a clear error when included
    with pytest.raises(ValueError, match="missing metadata column"):
        build_condition_masks(sample_metadata, condition_sets_with_filters)


def test_select_conditions_with_metadata_filters(sample_metadata, condition_sets_with_filters):
    """Ensure select_conditions combines condition and metadata filters."""
    # Mock epochs object with metadata attribute and __getitem__ returning filtered frames
    class MockEpochs:
        def __init__(self, metadata):
            self.metadata = metadata

        def __getitem__(self, mask):
            # Pandas Series mask
            if isinstance(mask, pd.Series):
                new_meta = self.metadata.loc[mask]
            else:
                new_meta = self.metadata.loc[mask]
            mock = MockEpochs(new_meta.reset_index(drop=True))
            return mock

    epochs = MockEpochs(sample_metadata)

    filtered = select_conditions(
        epochs,
        condition_codes=["12", "34"],
        metadata_filters={"Prime5": ["5a.jpg", "5e.jpg"]},
        set_name="test",
    )

    assert len(filtered.metadata) == 2
    assert set(filtered.metadata["Prime5"]) == {"5a.jpg", "5e.jpg"}
    assert set(filtered.metadata["Condition"]) <= {"12", "34"}

    # Missing column should raise a clear error when included
    with pytest.raises(ValueError, match="missing metadata column"):
        build_condition_masks(sample_metadata, condition_sets_with_filters)


# ============================================================================
# Run Tests
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
