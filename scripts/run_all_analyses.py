#!/usr/bin/env python
"""Run all analysis configurations sequentially.

This script discovers all YAML config files in configs/analyses/ and runs each
analysis in sequence. Useful for batch processing and ensuring all analyses
are up to date.
"""
from __future__ import annotations

import os
import sys
import glob
import subprocess
from pathlib import Path

# Get repo root
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIGS_DIR = os.path.join(REPO_ROOT, "configs", "analyses")


def main() -> int:
    """Run all analysis configurations."""
    # Find all YAML config files
    pattern = os.path.join(CONFIGS_DIR, "*.yaml")
    config_files = sorted(glob.glob(pattern))

    if not config_files:
        print(f"No configuration files found in {CONFIGS_DIR}")
        return 1

    print(f"Found {len(config_files)} analysis configurations:")
    for cfg in config_files:
        print(f"  - {os.path.basename(cfg)}")
    print()

    # Run each analysis
    failed = []
    for i, config_path in enumerate(config_files, 1):
        config_name = os.path.basename(config_path)
        print(f"[{i}/{len(config_files)}] Running: {config_name}")
        print("-" * 60)

        try:
            # Run analysis as subprocess
            result = subprocess.run(
                [sys.executable, "scripts/run_analysis.py", "--config", config_path],
                cwd=REPO_ROOT,
                check=True,
                capture_output=False,  # Show output in real-time
            )
            print(f"[OK] {config_name} completed successfully\n")
        except subprocess.CalledProcessError as e:
            print(f"[FAILED] {config_name} FAILED with exit code {e.returncode}\n")
            failed.append(config_name)
            # Continue with other analyses even if one fails

    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total analyses: {len(config_files)}")
    print(f"Successful: {len(config_files) - len(failed)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed analyses:")
        for name in failed:
            print(f"  - {name}")
        return 1

    print("\n[OK] All analyses completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
