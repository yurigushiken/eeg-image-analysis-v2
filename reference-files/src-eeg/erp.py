from __future__ import annotations

from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

import numpy as np


def compute_grand_average(evokeds: Sequence[np.ndarray]) -> np.ndarray:
    if len(evokeds) == 0:
        raise ValueError("No evokeds provided")
    # Equal-weight mean across subjects
    stacked = np.stack(evokeds, axis=0)
    return np.mean(stacked, axis=0)


def compute_sem(evokeds: Sequence[np.ndarray]) -> np.ndarray:
    if len(evokeds) == 0:
        raise ValueError("No evokeds provided")
    stacked = np.stack(evokeds, axis=0)
    return np.std(stacked, axis=0, ddof=1) / np.sqrt(stacked.shape[0])


def aggregate_roi(curves_by_channel: Mapping[str, np.ndarray], roi_channels: Sequence[str], min_channels: int) -> np.ndarray:
    available = [ch for ch in roi_channels if ch in curves_by_channel]
    if len(available) < min_channels:
        raise ValueError(
            f"ROI aggregation failed: channels available={len(available)} < min_channels={min_channels}"
        )
    stacked = np.stack([curves_by_channel[ch] for ch in available], axis=0)
    return np.mean(stacked, axis=0)



