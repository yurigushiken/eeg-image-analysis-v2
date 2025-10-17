from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping

import pandas as pd


def apply_response_filter(metadata: pd.DataFrame, response: str) -> pd.DataFrame:
    """Filter rows by response.

    Args:
        metadata: DataFrame with trial metadata
        response: Response filter - "ALL", "ACC1", or "ACC0"

    Returns:
        Filtered metadata DataFrame

    Response modes:
        - "ALL": return metadata unchanged (all trials)
        - "ACC1": keep rows where Target.ACC == 1 (correct responses only)
        - "ACC0": keep rows where Target.ACC == 0 (incorrect responses only)
    """
    if response.upper() == "ALL":
        return metadata
    if response.upper() == "ACC1":
        if "Target.ACC" not in metadata.columns:
            raise ValueError("Required metadata column missing: 'Target.ACC'")
        return metadata.loc[metadata["Target.ACC"] == 1]
    if response.upper() == "ACC0":
        if "Target.ACC" not in metadata.columns:
            raise ValueError("Required metadata column missing: 'Target.ACC'")
        return metadata.loc[metadata["Target.ACC"] == 0]
    raise ValueError(f"Unknown response mode: {response}. Valid options: ALL, ACC1, ACC0")


def validate_required_columns(
    metadata: pd.DataFrame, required_columns: Iterable[str]
) -> None:
    missing = [c for c in required_columns if c not in metadata.columns]
    if missing:
        raise ValueError(f"Required metadata columns missing: {missing}")


def build_condition_masks(
    metadata: pd.DataFrame, condition_sets: List[Mapping[str, Iterable[str]]]
) -> Dict[str, pd.Series]:
    """Build boolean masks per named condition set.

    Each set is a mapping with keys: name, conditions (list of string codes).
    """
    if "Condition" not in metadata.columns:
        raise ValueError("Required metadata column missing: 'Condition'")
    masks: Dict[str, pd.Series] = {}
    condition_series = metadata["Condition"].astype(str)
    for item in condition_sets:
        name = str(item.get("name"))
        conditions = [str(c) for c in (item.get("conditions") or [])]
        mask = condition_series.isin(conditions)
        masks[name] = mask
    return masks


@dataclass
class MinEpochsSummary:
    set_name: str
    epoch_count: int
    meets_threshold: bool


def summarize_min_epochs(
    masks_by_set: Mapping[str, pd.Series], min_epochs_per_set: int
) -> Dict[str, MinEpochsSummary]:
    summary: Dict[str, MinEpochsSummary] = {}
    for set_name, mask in masks_by_set.items():
        count = int(mask.sum())
        summary[set_name] = MinEpochsSummary(
            set_name=set_name,
            epoch_count=count,
            meets_threshold=(count >= min_epochs_per_set),
        )
    return summary


