import json
import re
from pathlib import Path
from typing import Dict, List, Any

import mne
import pandas as pd


DATA_ROOT = Path("data")
DEFAULT_PATTERN = "**/*-epo.fif"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def extract_subject_id(path: Path) -> str:
    m = re.search(r"sub-(\d+)", path.name)
    return m.group(0) if m else "unknown"


def summarize_file(path: Path) -> Dict[str, Any]:
    epochs = mne.read_epochs(str(path), preload=False, verbose=False)

    info = epochs.info
    ch_types = mne.io.pick.channel_type_count(epochs.info)
    event_id = epochs.event_id.copy() if epochs.event_id is not None else {}
    has_metadata = epochs.metadata is not None
    metadata_cols: List[str] = list(epochs.metadata.columns) if has_metadata else []

    # Compute epoch duration in seconds
    duration_s = float(epochs.tmax - epochs.tmin)

    # channel types as a stable dict (sorted keys)
    ch_types_sorted = {k: int(ch_types[k]) for k in sorted(ch_types.keys())}

    return {
        "file": str(path),
        "relative_file": str(path.as_posix()),
        "subject": extract_subject_id(path),
        "n_epochs": int(len(epochs)),
        "n_channels": int(len(info["ch_names"])),
        "sfreq": float(info["sfreq"]),
        "epoch_duration_s": duration_s,
        "channel_types": ch_types_sorted,
        "event_id_keys": sorted(list(event_id.keys())),
        "event_id": {k: int(v) for k, v in event_id.items()},
        "has_metadata": has_metadata,
        "metadata_columns": metadata_cols,
    }


def aggregate_columns(summaries: List[Dict[str, Any]]) -> Dict[str, Any]:
    all_cols: Dict[str, int] = {}
    for s in summaries:
        for c in s.get("metadata_columns", []):
            all_cols[c] = all_cols.get(c, 0) + 1

    all_event_keys: Dict[str, int] = {}
    for s in summaries:
        for k in s.get("event_id_keys", []):
            all_event_keys[k] = all_event_keys.get(k, 0) + 1

    return {
        "metadata_columns_presence": all_cols,
        "event_keys_presence": all_event_keys,
    }


def main():
    pattern = DEFAULT_PATTERN
    fif_files = sorted(DATA_ROOT.glob(pattern))
    if not fif_files:
        print(f"No FIF files found under {DATA_ROOT} with pattern {pattern}")
        return

    summaries: List[Dict[str, Any]] = []
    for p in fif_files:
        try:
            summaries.append(summarize_file(p))
        except Exception as e:
            summaries.append({
                "file": str(p),
                "subject": extract_subject_id(p),
                "error": str(e),
            })

    # Save JSON
    summary_json = OUTPUT_DIR / "data_summary.json"
    with summary_json.open("w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2)

    # Save CSV (flatten a few keys)
    rows = []
    for s in summaries:
        row = {
            "file": s.get("file"),
            "subject": s.get("subject"),
            "n_epochs": s.get("n_epochs"),
            "n_channels": s.get("n_channels"),
            "sfreq": s.get("sfreq"),
            "epoch_duration_s": s.get("epoch_duration_s"),
            "has_metadata": s.get("has_metadata"),
            "event_id_keys": ",".join(s.get("event_id_keys", [])) if s.get("event_id_keys") else None,
            "metadata_columns": ",".join(s.get("metadata_columns", [])) if s.get("metadata_columns") else None,
            "error": s.get("error"),
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_DIR / "data_summary.csv", index=False)

    # Save aggregates
    agg = aggregate_columns(summaries)
    with (OUTPUT_DIR / "aggregates.json").open("w", encoding="utf-8") as f:
        json.dump(agg, f, indent=2)

    print(f"Analyzed {len(summaries)} files. Outputs written to {OUTPUT_DIR}.")


if __name__ == "__main__":
    main()

