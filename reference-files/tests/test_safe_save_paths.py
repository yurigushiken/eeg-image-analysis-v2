import os
from pathlib import Path
import matplotlib.pyplot as plt
import pytest


@pytest.mark.unit
def test_save_figure_handles_windows_like_paths(tmp_path: Path):
    # Build a simple figure
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])

    # Import helper
    from scripts.run_analysis import _save_figure

    # Simulate a Windows-like relative path with backslashes
    rel_dir = tmp_path / "docs" / "assets" / "plots" / "landing_on_5_any_preceding_ACC1"
    rel_path = rel_dir / "landing_on_5_any_preceding_ACC1-P3b.png"

    # Use string form with backslashes to mimic logs
    path_str = str(rel_path).replace("/", "\\")

    _save_figure(fig, path_str, dpi=80)
    assert rel_path.exists()


@pytest.mark.unit
def test_save_figure_retries_on_errno22(tmp_path: Path, monkeypatch):
    # Build a simple figure
    fig, ax = plt.subplots()
    ax.plot([0, 1], [1, 0])

    from scripts import run_analysis as ra

    calls = {"n": 0}
    orig_savefig = fig.savefig

    def flaky_savefig(fname, *args, **kwargs):
        # First call raise OSError(22); second call succeeds
        calls["n"] += 1
        if calls["n"] == 1:
            err = OSError(22, "Invalid argument")
            raise err
        return orig_savefig(fname, *args, **kwargs)

    # Patch savefig for this figure only
    monkeypatch.setattr(fig, "savefig", flaky_savefig)

    out = tmp_path / "docs" / "assets" / "plots" / "demo" / "demo-P3b.png"
    ra._save_figure(fig, out, dpi=80)
    assert out.exists()


