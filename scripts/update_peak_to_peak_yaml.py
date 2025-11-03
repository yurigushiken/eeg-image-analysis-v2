#!/usr/bin/env python
from __future__ import annotations

"""
Batch-add measurement.peak_to_peak block to all configs/analyses/*.yaml.
- If measurement exists, add nested peak_to_peak if missing
- If measurement missing, create it with peak_to_peak
- Preserve existing keys; do not overwrite user-provided peak_to_peak

Defaults inserted:
  enabled: true
  roi: [N1_L, N1_R]
  hline_color: "#000000"
  hline_style: ":"
"""

import os
import sys
import glob
from typing import Any, Dict

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ANALYSES_DIR = os.path.join(REPO_ROOT, "configs", "analyses")

DEFAULT_P2P: Dict[str, Any] = {
    "enabled": True,
    "roi": ["N1_L", "N1_R"],
    "hline_color": "#000000",
    "hline_style": ":",
}

def update_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        return False

    changed = False

    meas = data.get("measurement")
    if meas is None or not isinstance(meas, dict):
        data["measurement"] = {"peak_to_peak": dict(DEFAULT_P2P)}
        changed = True
    else:
        p2p = meas.get("peak_to_peak")
        if p2p is None or not isinstance(p2p, dict):
            meas["peak_to_peak"] = dict(DEFAULT_P2P)
            changed = True
        else:
            # Ensure required defaults exist but do not overwrite existing keys
            for k, v in DEFAULT_P2P.items():
                if k not in p2p:
                    p2p[k] = v
                    changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
    return changed


def main() -> int:
    pattern = os.path.join(ANALYSES_DIR, "*.yaml")
    files = sorted(glob.glob(pattern))
    if not files:
        print(f"No YAML files found in {ANALYSES_DIR}")
        return 1

    changed_count = 0
    for p in files:
        try:
            if update_file(p):
                changed_count += 1
                print(f"Updated: {os.path.relpath(p, REPO_ROOT)}")
        except Exception as e:
            print(f"ERROR updating {p}: {e}")
    print(f"Done. Files changed: {changed_count}/{len(files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
