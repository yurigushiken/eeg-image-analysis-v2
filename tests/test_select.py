import os
import sys
from typing import List, Dict

import pandas as pd


# Ensure src/ is importable when running pytest from repo root
CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from eeg.select import (
    apply_response_filter,
    build_condition_masks,
    validate_required_columns,
    summarize_min_epochs,
)


def _make_metadata() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "SubjectID": ["S01"] * 8,
            "Condition": ["11", "12", "13", "21", "22", "23", "31", "32"],
            "Target.ACC": [1, 0, 1, 1, 0, 1, 0, 1],
        }
    )


def test_apply_response_filter_acc1():
    metadata = _make_metadata()
    filtered = apply_response_filter(metadata, response="ACC1")
    assert len(filtered) == (metadata["Target.ACC"] == 1).sum()
    assert (filtered["Target.ACC"] == 1).all()


def test_apply_response_filter_all_returns_all_rows():
    metadata = _make_metadata()
    filtered = apply_response_filter(metadata, response="ALL")
    assert len(filtered) == len(metadata)


def test_build_condition_masks_and_min_epochs_summary():
    metadata = _make_metadata()
    condition_sets = [
        {"name": "SetA", "conditions": ["12", "13"]},
        {"name": "SetB", "conditions": ["31", "32"]},
    ]
    masks = build_condition_masks(metadata, condition_sets)
    assert set(masks.keys()) == {"SetA", "SetB"}
    assert masks["SetA"].sum() == 2
    assert masks["SetB"].sum() == 2

    summary = summarize_min_epochs(masks, min_epochs_per_set=2)
    assert summary["SetA"].meets_threshold is True
    assert summary["SetB"].meets_threshold is True


def test_validate_required_columns_raises_on_missing():
    bad = pd.DataFrame({"Condition": ["11", "12"]})
    try:
        validate_required_columns(bad, required_columns=["Condition", "Target.ACC"])
    except ValueError as exc:
        msg = str(exc)
        assert "Target.ACC" in msg
    else:
        raise AssertionError("Expected ValueError for missing columns")


