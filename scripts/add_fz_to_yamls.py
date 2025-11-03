#!/usr/bin/env python
from __future__ import annotations
import os
import glob
from typing import Any, List
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ANALYSES = os.path.join(REPO_ROOT, 'configs', 'analyses')


def ensure_fz_in_components(path: str) -> bool:
    changed = False
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        return False
    comps: List[str] = list(data.get('components') or [])
    if 'Fz' not in comps:
        comps.append('Fz')
        data['components'] = comps
        changed = True
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
    return changed


def main() -> int:
    files = sorted(glob.glob(os.path.join(ANALYSES, '*.yaml')))
    changed = 0
    for p in files:
        try:
            if ensure_fz_in_components(p):
                print(f"Updated: {os.path.relpath(p, REPO_ROOT)}")
                changed += 1
        except Exception as e:
            print(f"ERROR updating {p}: {e}")
    print(f"Done. Files changed: {changed}/{len(files)}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
