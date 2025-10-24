#!/usr/bin/env python
"""Rebuild all website sections (main index + curated pages) in one pass."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional


REPO_ROOT = Path(__file__).resolve().parent.parent
SYS_SRC = REPO_ROOT / "src"
if str(SYS_SRC) not in sys.path:
    sys.path.insert(0, str(SYS_SRC))

from eeg.report import get_stats_info, generate_stats_html  # type: ignore


DEFAULT_CONFIG_PATH = REPO_ROOT / "configs" / "site_sections.yaml"


def load_config(config_path: Path) -> Dict:
    import yaml

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if not isinstance(config, dict) or "sections" not in config:
        raise ValueError("site_sections.yaml must define a top-level 'sections' list")

    return config


def ensure_page_exists(page_path: Path, layout: str = "default", title: Optional[str] = None) -> None:
    if page_path.exists():
        return

    title_text = title or page_path.stem.replace("_", " ").title()

    scaffold = (
        "---\n"
        f"layout: {layout}\n"
        f"title: {title_text}\n"
        "---\n\n"
        f"# {title_text}\n\n"
        "<!-- AUTO-GENERATED START -->\n"
        "<!-- AUTO-GENERATED END -->\n"
    )

    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(scaffold, encoding="utf-8")


def copy_assets(asset_config: List[Dict], docs_root: Path) -> None:
    for entry in asset_config:
        source = REPO_ROOT / entry["source"]
        destination = REPO_ROOT / entry["destination"]

        if not source.exists():
            print(f"[WARN] Asset missing, skipping copy: {source}")
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        print(f"[OK] Copied asset {source} -> {destination.relative_to(REPO_ROOT)}")


def gather_analysis_dirs(plots_dir: Path) -> Dict[str, Dict[str, str]]:
    analyses: Dict[str, Dict[str, str]] = {}
    for analysis_dir in sorted(d for d in plots_dir.iterdir() if d.is_dir()):
        analysis_id = analysis_dir.name
        component_to_image: Dict[str, str] = {}
        for component in ["P1", "N1", "P3b"]:
            plot_file = analysis_dir / f"{analysis_id}-{component}.png"
            if plot_file.exists():
                rel_path = f"assets/plots/{analysis_id}/{analysis_id}-{component}.png"
                component_to_image[component] = rel_path

        if component_to_image:
            analyses[analysis_id] = component_to_image
    return analyses


def build_section_html(
    section: Dict,
    analyses: Dict[str, Dict[str, str]],
    docs_root: Path,
) -> str:
    include_cfg = section.get("include", "all")

    missing_requested: List[str] = []
    if include_cfg == "all":
        selected_items = list(analyses.items())
    elif isinstance(include_cfg, list):
        selected_items = []
        for aid in include_cfg:
            if aid in analyses:
                selected_items.append((aid, analyses[aid]))
            else:
                missing_requested.append(aid)
    else:
        raise ValueError("'include' must be 'all' or a list of analysis IDs")

    start_marker = section["markers"]["start"]
    end_marker = section["markers"]["end"]

    rows: List[str] = []
    missing_components: List[str] = []

    for analysis_id, component_to_image in sorted(selected_items, key=lambda x: x[0].lower()):
        if not component_to_image:
            missing_components.append(analysis_id)
            continue

        collapsed_rel = f"assets/plots/{analysis_id}/{analysis_id}-collapsed_localizer.png"
        collapsed_abs = docs_root / f"assets/plots/{analysis_id}/{analysis_id}-collapsed_localizer.png"
        if collapsed_abs.exists():
            alt_c = f"Collapsed localizer for {analysis_id}"
            collapsed_cell = (
                f"<td><a href='{collapsed_rel}' data-lightbox aria-label='{alt_c}'>"
                f"<img class='thumb' src='{collapsed_rel}' alt='{alt_c}' /></a></td>"
            )
        else:
            collapsed_cell = "<td></td>"

        def make_cell(comp: str) -> str:
            img = component_to_image.get(comp)
            if not img:
                return "<td></td>"
            alt = f"ERP overlay for {comp} in {analysis_id}"
            return (
                f"<td><a href='{img}' data-lightbox aria-label='{alt}'>"
                f"<img class='thumb' src='{img}' alt='{alt}' /></a></td>"
            )

        erp_row = f"<tr><td>{analysis_id}</td>{collapsed_cell}{make_cell('P1')}{make_cell('N1')}{make_cell('P3b')}</tr>"
        rows.append(erp_row)

        if section.get("include_stats", False):
            stats_info = get_stats_info(analysis_id, str(docs_root))
            if stats_info:
                stats_html = generate_stats_html(analysis_id, stats_info)
                rows.append(f"<tr><td colspan='5'>{stats_html}</td></tr>")

    if missing_requested:
        print(f"[WARN] Analyses requested but not found: {', '.join(missing_requested)}")

    if missing_components:
        print(f"[WARN] Analyses missing ERP components: {', '.join(missing_components)}")

    table_html = (
        "<table class=\"grid-table\">\n"
        "<thead>\n  <tr><th>Analysis</th><th>Collapsed Localizer</th><th>P1</th><th>N1</th><th>P3b</th></tr>\n</thead>\n"
        "<tbody>\n"
        + ("\n".join(rows) if rows else "")
        + "\n</tbody>\n</table>\n"
    )

    return f"{start_marker}\n{table_html}{end_marker}"


def rewrite_section(
    page_path: Path,
    start_marker: str,
    end_marker: str,
    new_block: str,
    *,
    add_methodology: bool,
) -> None:
    content = page_path.read_text(encoding="utf-8")

    if start_marker not in content or end_marker not in content:
        raise ValueError(f"Markers not found in {page_path}: {start_marker} / {end_marker}")

    pre, rest = content.split(start_marker, 1)
    _, post = rest.split(end_marker, 1)

    if add_methodology and "methodology document" not in pre:
        methodology_link = (
            "<p><a href=\"https://github.com/yurigushiken/eeg-image-analysis-v2/blob/main/methodology.md\" target=\"_blank\">"
            "Link to methodology document explaining 'peak' amplitude and latency.</a></p>\n\n"
        )
        pre = pre.rstrip() + "\n\n" + methodology_link

    page_path.write_text(pre + new_block + post, encoding="utf-8")


def rebuild_site(config_path: Path = DEFAULT_CONFIG_PATH) -> int:
    print(f"[INFO] Loading configuration from {config_path.relative_to(REPO_ROOT)}")
    config = load_config(config_path)

    docs_root = REPO_ROOT / "docs"
    plots_dir = docs_root / "assets" / "plots"
    if not plots_dir.exists():
        print(f"[ERROR] Plots directory not found: {plots_dir}")
        return 1

    analyses = gather_analysis_dirs(plots_dir)
    print(f"[INFO] Found {len(analyses)} analyses with ERP plots")

    if config.get("assets"):
        copy_assets(config["assets"], docs_root)

    for section in config["sections"]:
        page = REPO_ROOT / section["page"]
        ensure_page_exists(page)

        new_block = build_section_html(section, analyses, docs_root)
        rewrite_section(
            page,
            section["markers"]["start"],
            section["markers"]["end"],
            new_block,
            add_methodology=section.get("add_methodology_link", True),
        )
        print(f"[OK] Updated section '{section['id']}' -> {page.relative_to(REPO_ROOT)}")

    print("[SUCCESS] Site rebuild complete")
    return 0


def main() -> int:
    try:
        return rebuild_site()
    except Exception as exc:
        print(f"[ERROR] {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())


