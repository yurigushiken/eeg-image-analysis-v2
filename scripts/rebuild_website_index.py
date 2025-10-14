#!/usr/bin/env python
"""Rebuild the website index from scratch, removing all old entries."""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Add src to path
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from eeg.report import get_stats_info, generate_stats_html


def main() -> int:
    """Rebuild the website index from scratch."""

    # Paths
    docs_dir = REPO_ROOT / "docs"
    plots_dir = docs_dir / "assets" / "plots"
    index_path = docs_dir / "index.md"

    if not plots_dir.exists():
        print(f"ERROR: Plots directory not found: {plots_dir}")
        return 1

    # Find all analysis directories with actual plot files
    analysis_data = {}
    analysis_dirs = sorted([d for d in plots_dir.iterdir() if d.is_dir()])

    for analysis_dir in analysis_dirs:
        analysis_id = analysis_dir.name

        # Find component plots
        component_to_image = {}
        for component in ['P1', 'N1', 'P3b']:
            plot_file = analysis_dir / f"{analysis_id}-{component}.png"
            if plot_file.exists():
                rel_path = f"assets/plots/{analysis_id}/{analysis_id}-{component}.png"
                component_to_image[component] = rel_path

        # Skip analyses with no plots
        if not component_to_image:
            continue

        analysis_data[analysis_id] = component_to_image

    print(f"Found {len(analysis_data)} analyses with plots\n")

    # Build HTML rows
    all_rows = []
    for analysis_id in sorted(analysis_data.keys(), key=lambda s: s.lower()):
        component_to_image = analysis_data[analysis_id]

        # Build ERP row
        cells = [f"<td>{analysis_id}</td>"]
        for component in ['P1', 'N1', 'P3b']:
            img = component_to_image.get(component)
            if img:
                alt = f"ERP overlay for {component} in {analysis_id}"
                cells.append(
                    f"<td><a href='{img}' data-lightbox aria-label='{alt}'>"
                    f"<img class='thumb' src='{img}' alt='{alt}' /></a></td>"
                )
            else:
                cells.append("<td></td>")

        erp_row = f"<tr>{''.join(cells)}</tr>"
        all_rows.append(erp_row)

        # Check for statistics
        stats_info = get_stats_info(analysis_id, str(docs_dir))
        if stats_info:
            stats_html = generate_stats_html(analysis_id, stats_info)
            stats_row = f"<tr><td colspan='4'>{stats_html}</td></tr>"
            all_rows.append(stats_row)
            print(f"[OK] {analysis_id} (with statistics)")
        else:
            print(f"[OK] {analysis_id}")

    # Read current index
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace AUTO-GENERATED section
    start_marker = "<!-- AUTO-GENERATED START -->"
    end_marker = "<!-- AUTO-GENERATED END -->"

    if start_marker not in content or end_marker not in content:
        print(f"ERROR: Markers not found in {index_path}")
        return 1

    pre, rest = content.split(start_marker, 1)
    _, post = rest.split(end_marker, 1)

    # Build new section
    new_block = (
        f"{start_marker}\n"
        '<table class="grid-table">\n'
        '<thead>\n'
        '  <tr><th>Analysis</th><th>P1</th><th>N1</th><th>P3b</th></tr>\n'
        '</thead>\n'
        '<tbody>\n'
        f"{''.join(all_rows)}\n"
        '</tbody>\n'
        '</table>\n'
        f"{end_marker}"
    )

    new_content = pre + new_block + post

    # Write back
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"\n[OK] Index rebuilt with {len(analysis_data)} analyses")
    print(f"  Index file: {index_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
