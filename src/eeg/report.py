from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, List, Optional


def write_analysis_page(page_path: str, title: str, figure_paths: Optional[List[str]] = None, notes: Optional[List[str]] = None) -> None:
    os.makedirs(os.path.dirname(page_path), exist_ok=True)
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        if figure_paths:
            for p in figure_paths:
                rel = p.replace("\\", "/")
                f.write(f"![figure]({rel})\n\n")
        if notes:
            f.write("\n## Notes\n\n")
            for n in notes:
                f.write(f"- {n}\n")


def ensure_index_template(index_path: str) -> None:
    if os.path.exists(index_path):
        return
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(
            """
            # EEG ERP Analyses

            <style>
            .grid-table { width: 100%; border-collapse: collapse; }
            .grid-table th, .grid-table td { padding: 6px; text-align: center; }
            .thumb { width: 160px; max-width: 100%; height: auto; cursor: zoom-in; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,.15); }
            /* Lightbox */
            .lightbox-backdrop { display:none; position: fixed; inset: 0; background: rgba(0,0,0,.8); align-items: center; justify-content: center; z-index: 9999; }
            .lightbox-backdrop.active { display:flex; }
            .lightbox-content { position: relative; max-width: 96%; max-height: 90%; }
            .lightbox-content img { width: 100%; height: auto; }
            .lightbox-close { position:absolute; top:8px; right:8px; background:#fff; border:none; border-radius:3px; padding:6px 8px; cursor:pointer; }
            </style>

            <div id="lightbox" class="lightbox-backdrop" role="dialog" aria-modal="true" aria-label="Image viewer">
              <div class="lightbox-content">
                <button id="lightbox-close" class="lightbox-close" aria-label="Close image">Close</button>
                <img id="lightbox-img" alt="Full-size figure" />
              </div>
            </div>

            <script>
            (function(){
              var lb = document.getElementById('lightbox');
              var imgEl = document.getElementById('lightbox-img');
              var btn = document.getElementById('lightbox-close');
              function open(src, alt){ imgEl.src = src; imgEl.alt = alt || 'Full-size figure'; lb.classList.add('active'); }
              function close(){ lb.classList.remove('active'); imgEl.src=''; }
              btn.addEventListener('click', close);
              lb.addEventListener('click', function(e){ if(e.target===lb) close(); });
              document.addEventListener('click', function(e){
                var a = e.target.closest('a[data-lightbox]');
                if(!a) return;
                e.preventDefault();
                open(a.getAttribute('href'), a.getAttribute('aria-label'));
              });
              document.addEventListener('keydown', function(e){ if(e.key==='Escape') close(); });
            })();
            </script>

            <!-- AUTO-GENERATED START -->
            <table class="grid-table">
            <thead>
              <tr><th>Analysis</th><th>P1</th><th>N1</th><th>P3b</th></tr>
            </thead>
            <tbody>
            </tbody>
            </table>
            <!-- AUTO-GENERATED END -->
            """.strip()
        )


def get_stats_info(analysis_id: str, docs_root: str = "docs") -> Optional[Dict[str, any]]:
    """Check if statistical results exist for this analysis and gather paths.

    Args:
        analysis_id: The analysis identifier
        docs_root: Root directory for docs (default: "docs")

    Returns:
        Dictionary with stats paths if they exist, None otherwise
    """
    stats_dir = Path(docs_root) / "assets" / "stats" / analysis_id
    if not stats_dir.exists():
        return None

    # Check for statistical report
    report_path = stats_dir / "STATISTICAL_REPORT.md"
    if not report_path.exists():
        return None

    plots_dir = stats_dir / "plots"
    if not plots_dir.exists():
        return None

    # Gather plot files
    boxplots = {}
    violin_plots = {}
    effect_sizes = {}

    # Support both peak-based and window/mean-based outputs
    measure_candidates = [
        'mean_amplitude_roi',
        'latency_frac_area_ms',
        'peak_latency_ms',
        'peak_amplitude_roi',
    ]

    for component in ['N1', 'P1', 'P3b']:
        for measure_type in measure_candidates:
            # Box/violin file names are standardized on dv name
            boxplot_name = f"boxplot_{component}_{measure_type}.png"
            violin_name = f"violin_{component}_{measure_type}.png"
            effect_name = f"effect_sizes_{component}_{measure_type}.png"

            boxplot_path = plots_dir / boxplot_name
            violin_path = plots_dir / violin_name
            effect_path = plots_dir / effect_name

            if boxplot_path.exists():
                rel_path = f"assets/stats/{analysis_id}/plots/{boxplot_name}"
                if component not in boxplots:
                    boxplots[component] = []
                boxplots[component].append(rel_path)

            if violin_path.exists():
                rel_path = f"assets/stats/{analysis_id}/plots/{violin_name}"
                if component not in violin_plots:
                    violin_plots[component] = []
                violin_plots[component].append(rel_path)

            if effect_path.exists():
                rel_path = f"assets/stats/{analysis_id}/plots/{effect_name}"
                if component not in effect_sizes:
                    effect_sizes[component] = []
                effect_sizes[component].append(rel_path)

    return {
        'report': f"assets/stats/{analysis_id}/STATISTICAL_REPORT.md",
        'boxplots': boxplots,
        'violin_plots': violin_plots,
        'effect_sizes': effect_sizes,
    }


def generate_stats_html(analysis_id: str, stats_info: Dict[str, any]) -> str:
    """Generate HTML for the expandable statistics section.

    Args:
        analysis_id: The analysis identifier
        stats_info: Dictionary with stats paths from get_stats_info()

    Returns:
        HTML string for the statistics section
    """
    html_parts = []

    # Toggle button
    html_parts.append(
        f'<button class="stats-toggle" data-analysis-id="{analysis_id}" '
        f'aria-expanded="false" aria-controls="stats-{analysis_id}">Show Statistics</button>'
    )

    # Statistics content (initially hidden)
    html_parts.append(f'<div id="stats-{analysis_id}" class="stats-content">')

    # Statistical Report Link
    html_parts.append('<div class="stats-section">')
    html_parts.append('<h4>Statistical Report</h4>')
    html_parts.append(
        f'<a href="{stats_info["report"]}" class="stats-report-link" target="_blank">'
        f'View Full Report</a>'
    )
    html_parts.append('</div>')

    # Boxplots
    if stats_info['boxplots']:
        html_parts.append('<div class="stats-section">')
        html_parts.append('<h4>Boxplots</h4>')
        html_parts.append('<div class="stats-plots">')

        for component in ['P1', 'N1', 'P3b']:
            if component in stats_info['boxplots']:
                for plot_path in stats_info['boxplots'][component]:
                    alt = f"Boxplot for {component} in {analysis_id}"
                    html_parts.append(
                        f'<a href="{plot_path}" data-lightbox aria-label="{alt}">'
                        f'<img class="thumb" src="{plot_path}" alt="{alt}" /></a>'
                    )

        html_parts.append('</div>')
        html_parts.append('</div>')

    # Violin Plots
    if stats_info['violin_plots']:
        html_parts.append('<div class="stats-section">')
        html_parts.append('<h4>Violin Plots</h4>')
        html_parts.append('<div class="stats-plots">')

        for component in ['P1', 'N1', 'P3b']:
            if component in stats_info['violin_plots']:
                for plot_path in stats_info['violin_plots'][component]:
                    alt = f"Violin plot for {component} in {analysis_id}"
                    html_parts.append(
                        f'<a href="{plot_path}" data-lightbox aria-label="{alt}">'
                        f'<img class="thumb" src="{plot_path}" alt="{alt}" /></a>'
                    )

        html_parts.append('</div>')
        html_parts.append('</div>')

    # Effect Size Plots (if available)
    if stats_info.get('effect_sizes'):
        html_parts.append('<div class="stats-section">')
        html_parts.append('<h4>Effect Sizes</h4>')
        html_parts.append('<div class="stats-plots">')

        for component in ['P1', 'N1', 'P3b']:
            if component in stats_info['effect_sizes']:
                for plot_path in stats_info['effect_sizes'][component]:
                    alt = f"Effect sizes for {component} in {analysis_id}"
                    html_parts.append(
                        f'<a href="{plot_path}" data-lightbox aria-label="{alt}">'
                        f'<img class="thumb" src="{plot_path}" alt="{alt}" /></a>'
                    )

        html_parts.append('</div>')
        html_parts.append('</div>')

    html_parts.append('</div>')  # Close stats-content

    return ''.join(html_parts)


def update_index_grid(index_path: str, analysis_id: str, component_to_image: Dict[str, str]) -> None:
    """Idempotently update the AUTO-GENERATED grid with a row for analysis_id.

    - Keeps rows sorted by analysis_id
    - Updates existing row if present
    - Relative paths assumed from docs/ root
    """
    ensure_index_template(index_path)
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- AUTO-GENERATED START -->"
    end_marker = "<!-- AUTO-GENERATED END -->"
    if start_marker not in content or end_marker not in content:
        # Regenerate minimal block
        ensure_index_template(index_path)
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()

    pre, rest = content.split(start_marker, 1)
    block, post = rest.split(end_marker, 1)

    # Parse existing entries - group rows by analysis ID
    # Each analysis may have multiple <tr> rows (ERP row + stats row)
    import re

    analysis_entries = {}  # analysis_id -> list of row lines
    current_analysis = None
    current_rows = []

    lines = [ln for ln in block.strip().splitlines() if ln.strip()]

    for ln in lines:
        s = ln.strip()
        if s.startswith("<thead>") or s.startswith("</thead>") or s.startswith("<tbody>") or s.startswith("</tbody>") or s.startswith("<table"):
            continue

        if s.startswith("<tr>"):
            # Check if this is a new analysis row (starts with <td>analysis_id</td>)
            match = re.search(r"<tr><td>([^<]+)</td>", s)
            if match:
                # Save previous analysis if exists
                if current_analysis:
                    analysis_entries[current_analysis] = current_rows
                # Start new analysis
                current_analysis = match.group(1)
                current_rows = [s]
            else:
                # This is a continuation row (stats row)
                if current_analysis:
                    current_rows.append(s)

    # Save last analysis
    if current_analysis:
        analysis_entries[current_analysis] = current_rows

    def make_cell(comp: str) -> str:
        img = component_to_image.get(comp)
        if not img:
            return "<td></td>"
        alt = f"ERP overlay for {comp} in {analysis_id}"
        return (
          f"<td><a href='{img}' data-lightbox aria-label='{alt}'><img class='thumb' src='{img}' alt='{alt}' /></a></td>"
        )

    # Build main row with ERP plots
    erp_row = f"<tr><td>{analysis_id}</td>{make_cell('P1')}{make_cell('N1')}{make_cell('P3b')}</tr>"

    # Check if statistics exist for this analysis
    # Get docs root directory from index path
    index_dir = os.path.dirname(index_path)
    if not index_dir or index_dir == '.':
        docs_root = 'docs'
    elif os.path.basename(index_dir) == 'docs':
        docs_root = index_dir
    else:
        # index_path is something like "docs/index.md", so dirname gives us "docs"
        docs_root = index_dir

    stats_info = get_stats_info(analysis_id, docs_root)

    # Build the new entry for this analysis
    new_rows_for_analysis = [erp_row]

    if stats_info:
        # Add statistics row below ERP row
        stats_html = generate_stats_html(analysis_id, stats_info)
        new_rows_for_analysis.append(f"<tr><td colspan='4'>{stats_html}</td></tr>")

    # Update or insert this analysis entry
    analysis_entries[analysis_id] = new_rows_for_analysis

    # Rebuild sorted table
    sorted_ids = sorted(analysis_entries.keys(), key=lambda s: s.lower())
    all_rows = []
    for aid in sorted_ids:
        all_rows.extend(analysis_entries[aid])

    new_block = "\n<table class=\"grid-table\">\n<thead>\n  <tr><th>Analysis</th><th>P1</th><th>N1</th><th>P3b</th></tr>\n</thead>\n<tbody>\n" + ("\n".join(all_rows) if all_rows else "") + "\n</tbody>\n</table>\n"
    new_content = pre + start_marker + new_block + end_marker + post

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)


