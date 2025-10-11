from pathlib import Path
from typing import List, Dict

import mne
import matplotlib

# Use a non-interactive backend to allow headless saves
matplotlib.use("Agg")
import matplotlib.pyplot as plt


DATA_ROOT = Path("data")
OUTPUT_DIR = Path("outputs/plots")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_evoked_for_file(fif_path: Path) -> List[Path]:
    epochs = mne.read_epochs(str(fif_path), preload=False, verbose=False)

    # If there are named conditions via event_id, average per condition
    saved: List[Path] = []
    if epochs.event_id:
        for cond in sorted(epochs.event_id.keys()):
            try:
                evoked = epochs[cond].average()
            except Exception:
                # If selection by name fails, skip
                continue

            fig = evoked.plot(spatial_colors=True, show=False)
            out = OUTPUT_DIR / f"{fif_path.stem}_evoked_{cond}.png"
            fig.savefig(out, dpi=150, bbox_inches="tight")
            plt.close(fig)
            saved.append(out)
    else:
        # No named conditions: plot grand average across all epochs
        evoked = epochs.average()
        fig = evoked.plot(spatial_colors=True, show=False)
        out = OUTPUT_DIR / f"{fif_path.stem}_evoked.png"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        plt.close(fig)
        saved.append(out)

    # Also add a sensor layout plot for quick inspection
    try:
        fig = epochs.plot_sensors(show=False)
        out = OUTPUT_DIR / f"{fif_path.stem}_sensors.png"
        fig.savefig(out, dpi=150, bbox_inches="tight")
        plt.close(fig)
        saved.append(out)
    except Exception:
        pass

    return saved


def main():
    fif_files = sorted(DATA_ROOT.glob("**/*-epo.fif"))
    if not fif_files:
        print("No FIF files found.")
        return
    # Limit to a couple by default to avoid generating too many plots
    for p in fif_files[:4]:
        saved = plot_evoked_for_file(p)
        for out in saved:
            print(f"Saved: {out}")


if __name__ == "__main__":
    main()

