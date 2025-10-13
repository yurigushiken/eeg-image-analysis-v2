#!/usr/bin/env python
"""Create individual statistics config files for each analysis.

This is an optional helper script that generates separate config files
for each analysis, allowing you to customize statistical settings per analysis.

Usage:
    python scripts/create_stat_configs.py

This will create:
    - configs/statistics/landing_on_2.yaml
    - configs/statistics/increase_by_1.yaml
    - etc.

You can then edit these individually and run:
    python scripts/run_statistics.py --config configs/statistics/ANALYSIS_NAME.yaml
"""
from __future__ import annotations

import os
import sys
import yaml
from pathlib import Path

# Get repo root
REPO_ROOT = Path(__file__).parent.parent
TABLES_DIR = REPO_ROOT / "docs" / "assets" / "tables"
STATS_DIR = REPO_ROOT / "configs" / "statistics"
TEMPLATE = STATS_DIR / "default.yaml"


def main() -> int:
    """Create individual config files for each analysis."""

    # Load template
    if not TEMPLATE.exists():
        print(f"ERROR: Template not found: {TEMPLATE}")
        return 1

    with open(TEMPLATE, 'r') as f:
        template = yaml.safe_load(f)

    # Find all analyses
    if not TABLES_DIR.exists():
        print(f"ERROR: Tables directory not found: {TABLES_DIR}")
        return 1

    analyses = []
    for analysis_dir in TABLES_DIR.iterdir():
        if analysis_dir.is_dir() and (analysis_dir / "subject_measurements.csv").exists():
            analyses.append(analysis_dir.name)

    if not analyses:
        print(f"No analyses found in {TABLES_DIR}")
        return 1

    print(f"Found {len(analyses)} analyses. Creating config files...")

    # Create config for each analysis
    for analysis_id in sorted(analyses):
        config = template.copy()

        # Update paths
        config['input_csv'] = f"docs/assets/tables/{analysis_id}/subject_measurements.csv"
        config['output_dir'] = f"docs/assets/stats/{analysis_id}"

        # Save
        output_path = STATS_DIR / f"{analysis_id}.yaml"
        with open(output_path, 'w') as f:
            # Add header comment
            f.write(f"# Statistical Analysis Configuration for {analysis_id}\n")
            f.write(f"# Auto-generated from default.yaml - customize as needed\n")
            f.write("#\n")
            f.write("# Usage:\n")
            f.write(f"#   python scripts/run_statistics.py --config configs/statistics/{analysis_id}.yaml\n")
            f.write("\n")
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)

        print(f"  Created: configs/statistics/{analysis_id}.yaml")

    print(f"\n[OK] Created {len(analyses)} config files!")
    print("\nYou can now:")
    print("  1. Edit individual configs: configs/statistics/*.yaml")
    print("  2. Run specific analysis: python scripts/run_statistics.py --config configs/statistics/ANALYSIS.yaml")
    print("  3. Run all at once: python scripts/run_all_statistics.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
