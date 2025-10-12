import os
import sys
import tempfile
import textwrap
import subprocess


def test_cli_smoke_runs_and_creates_dirs():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    configs_dir = os.path.join(repo_root, "configs", "analyses")
    os.makedirs(configs_dir, exist_ok=True)

    yaml_path = os.path.join(configs_dir, "sample_smoke.yaml")
    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(
            textwrap.dedent(
                """
                dataset:
                  root: "data"
                  pattern: "**/sub-*_epo.fif"
                  montage_sfp: "assets/net/AdultAverageNet128_v1.sfp"
                selection:
                  response: "ALL"
                  min_epochs_per_set: 8
                  condition_sets:
                    - name: "A"
                      conditions: ["11"]
                components: ["P1"]
                preprocessing:
                  baseline_ms: [-100, 0]
                roi:
                  min_channels: 4
                plots:
                  formats: ["png"]
                  dpi: 50
                outputs:
                  page: "single"
                  plots_dir: "docs/assets/plots/sample_smoke"
                  tables_dir: "docs/assets/tables/sample_smoke"
                  page: "docs/analysis/sample_smoke.md"
                """
            ).strip()
        )

    # Run the CLI
    cmd = [sys.executable, os.path.join(repo_root, "scripts", "run_analysis.py"), "--config", yaml_path]
    result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr

    # Check directories created
    assert os.path.isdir(os.path.join(repo_root, "docs", "assets", "plots", "sample_smoke"))
    assert os.path.isdir(os.path.join(repo_root, "docs", "assets", "tables", "sample_smoke"))
    assert os.path.isfile(os.path.join(repo_root, "docs", "analysis", "sample_smoke.md"))


