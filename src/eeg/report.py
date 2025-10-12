from __future__ import annotations

import os
from typing import Dict, List


def write_analysis_page(page_path: str, title: str, figure_paths: List[str] | None = None) -> None:
    os.makedirs(os.path.dirname(page_path), exist_ok=True)
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        if figure_paths:
            for p in figure_paths:
                rel = p.replace("\\", "/")
                f.write(f"![figure]({rel})\n\n")


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

    # Normalize block lines and preserve header row
    lines = [ln for ln in block.strip().splitlines() if ln.strip()]
    # Ensure header exists just once
    header = "<thead>"
    sep = "</thead>"
    rows = []
    for ln in lines:
        if ln.strip().startswith("<thead>") or ln.strip().startswith("</thead>"):
            continue
        if ln.strip().startswith("<tr>"):
            rows.append(ln.strip())

    def make_cell(comp: str) -> str:
        img = component_to_image.get(comp)
        if not img:
            return "<td></td>"
        alt = f"ERP overlay for {comp} in {analysis_id}"
        return (
          f"<td><a href='{img}' data-lightbox aria-label='{alt}'><img class='thumb' src='{img}' alt='{alt}' /></a></td>"
        )

    new_row = (
      f"<tr><td>{analysis_id}</td>{make_cell('P1')}{make_cell('N1')}{make_cell('P3b')}</tr>"
    )

    # Replace if exists, else insert
    row_map = {}
    for r in rows:
        parts = [p.strip() for p in r.strip('|').split('|')]
        if parts:
            row_map[parts[0]] = r
    row_map[analysis_id] = new_row

    # Rebuild sorted rows
    sorted_ids = sorted(row_map.keys(), key=lambda s: s.lower())
    new_rows = [row_map[k] for k in sorted_ids]
    new_block = "\n<table class=\"grid-table\">\n<thead>\n  <tr><th>Analysis</th><th>P1</th><th>N1</th><th>P3b</th></tr>\n</thead>\n<tbody>\n" + ("\n".join(new_rows) if new_rows else "") + "\n</tbody>\n</table>\n"
    new_content = pre + start_marker + new_block + end_marker + post

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)


