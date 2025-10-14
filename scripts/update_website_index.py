#!/usr/bin/env python
"""Update the website index with all analyses and their statistics.

This script scans the docs/assets/plots directory for all analyses
and updates the docs/index.md file with links to ERP plots and
statistical results (if available).

Usage:
    python scripts/update_website_index.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Add src to path
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from eeg.report import update_index_grid


def main() -> int:
    """Update the website index with all analyses."""

    # Paths
    docs_dir = REPO_ROOT / "docs"
    plots_dir = docs_dir / "assets" / "plots"
    index_path = docs_dir / "index.md"

    if not plots_dir.exists():
        print(f"ERROR: Plots directory not found: {plots_dir}")
        return 1

    # Find all analysis directories
    analysis_dirs = sorted([d for d in plots_dir.iterdir() if d.is_dir()])

    if not analysis_dirs:
        print(f"No analysis directories found in {plots_dir}")
        return 1

    print(f"Found {len(analysis_dirs)} analyses")
    print()

    # Update index for each analysis
    success_count = 0
    failed = []

    for analysis_dir in analysis_dirs:
        analysis_id = analysis_dir.name
        print(f"Processing: {analysis_id}")

        try:
            # Find component plots
            component_to_image = {}

            for component in ['P1', 'N1', 'P3b']:
                plot_file = analysis_dir / f"{analysis_id}-{component}.png"
                if plot_file.exists():
                    # Relative path from docs/ directory
                    rel_path = f"assets/plots/{analysis_id}/{analysis_id}-{component}.png"
                    component_to_image[component] = rel_path

            # Only include analyses that have at least one component plot
            # (can be partial - P1/N1/P3b, but not completely empty)
            if not component_to_image:
                print(f"  [WARN] No component plots found, skipping")
                continue

            # Update index
            update_index_grid(
                index_path=str(index_path),
                analysis_id=analysis_id,
                component_to_image=component_to_image
            )

            print(f"  [OK] Updated ({', '.join(component_to_image.keys())} plots)")
            success_count += 1

        except Exception as e:
            print(f"  [FAILED] {e}")
            failed.append(analysis_id)

    # Summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total analyses: {len(analysis_dirs)}")
    print(f"Successfully updated: {success_count}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed analyses:")
        for name in failed:
            print(f"  - {name}")
        return 1

    print(f"\n[OK] Website index updated successfully!")
    print(f"  Index file: {index_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
