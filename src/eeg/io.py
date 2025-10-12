from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

import os
import re
import glob


def validate_montage_path(montage_sfp: str) -> None:
    if not os.path.isfile(montage_sfp):
        raise FileNotFoundError(
            f"Montage file not found: {montage_sfp}. Provide assets/net *.sfp path."
        )


def discover_epoch_files(root: str, pattern: str) -> List[str]:
    search_glob = os.path.join(root, pattern)
    return sorted(glob.glob(search_glob, recursive=True))


def read_epochs(file_path: str):
    """Read an MNE Epochs object from a FIF file (import on demand)."""
    import mne  # local import to avoid hard dependency at module import

    return mne.read_epochs(file_path, preload=False, verbose=False)


def apply_montage(epochs, montage_sfp: str) -> None:
    """Apply a custom montage; raise actionable error if labels mismatch."""
    import mne  # local import

    validate_montage_path(montage_sfp)
    montage = mne.channels.read_custom_montage(montage_sfp)
    # Compute unmatched channel names (case-insensitive)
    epoch_chs = [ch.upper() for ch in epochs.ch_names]
    montage_chs = [ch.upper() for ch in getattr(montage, "ch_names", [])]
    unmatched = [ch for ch in epoch_chs if ch not in montage_chs]
    if unmatched:
        raise ValueError(
            "Montage application failed: unmatched channel labels found. "
            f"Unmatched (sample): {unmatched[:10]} (total={len(unmatched)}); "
            f"montage={montage_sfp}"
        )
    epochs.set_montage(montage, match_case=False, on_missing="warn", verbose=False)


def pick_scalp_channel_indices(epochs) -> List[int]:
    import mne  # local import

    picks = mne.pick_types(epochs.info, eeg=True, meg=False, eog=False, stim=False, misc=False)
    return list(picks)


def extract_subject_id(epochs, file_path: str) -> str:
    # Prefer metadata column
    if getattr(epochs, "metadata", None) is not None and "SubjectID" in epochs.metadata.columns:
        vals = epochs.metadata["SubjectID"].astype(str).unique()
        if len(vals) > 0:
            return str(vals[0])
    # Fallback to filename pattern sub-<ID>_
    m = re.search(r"sub-([A-Za-z0-9]+)", os.path.basename(file_path))
    return m.group(1) if m else os.path.splitext(os.path.basename(file_path))[0]


def filter_by_response(epochs, response: str):
    """Return epochs filtered by response (ALL or ACC1 using metadata['Target.ACC'])."""
    if response.upper() == "ALL":
        return epochs
    if response.upper() == "ACC1":
        if getattr(epochs, "metadata", None) is None or "Target.ACC" not in epochs.metadata.columns:
            raise ValueError("Required metadata column missing: 'Target.ACC'")
        mask = epochs.metadata["Target.ACC"] == 1
        return epochs[mask]
    raise ValueError(f"Unknown response mode: {response}")


def select_conditions(epochs, condition_codes: Sequence[str]):
    """Subset epochs using metadata['Condition'] membership if available; else event labels."""
    if getattr(epochs, "metadata", None) is not None and "Condition" in epochs.metadata.columns:
        mask = epochs.metadata["Condition"].astype(str).isin([str(c) for c in condition_codes])
        return epochs[mask]
    # Fallback: try event label selection (if labels match codes)
    sel = None
    for code in condition_codes:
        try:
            part = epochs[str(code)]
        except Exception:
            continue
        sel = part if sel is None else sel + part
    if sel is None:
        raise ValueError("None of the requested condition codes matched epochs")
    return sel


def validate_baseline_window(epochs, baseline_ms: Tuple[int, int]) -> None:
    """Ensure baseline window lies within epoch time range; raise actionable error otherwise."""
    start_ms, end_ms = baseline_ms
    tmin_ms = int(round(epochs.tmin * 1000.0))
    tmax_ms = int(round(epochs.tmax * 1000.0))
    if start_ms < tmin_ms or end_ms > tmax_ms:
        raise ValueError(
            f"Baseline [{start_ms}, {end_ms}] ms outside epoch range [{tmin_ms}, {tmax_ms}] ms"
        )



