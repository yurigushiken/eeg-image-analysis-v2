import os
import sys
import numpy as np


CURRENT_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from eeg.plots import make_erp_figure


def test_make_erp_figure_with_fallback_annotation():
    times_ms = np.linspace(-100, 500, 64)
    curves = {
        "Small_Increasing": np.sin(times_ms / 100.0),
        "Small_Decreasing": np.cos(times_ms / 120.0),
    }
    fig = make_erp_figure(
        curves_by_label=curves,
        times_ms=times_ms,
        title="analysis_id: P1 (ALL)",
        subtitle="baseline [-100,0] ms; ±50 ms topomap; roi.min=4",
        annotate_fallback=True,
    )
    # Expect at least one Axes and a text annotation present
    assert len(fig.axes) >= 1
    texts = [t.get_text() for ax in fig.axes for t in ax.texts]
    assert any("fallback" in t.lower() for t in texts)


