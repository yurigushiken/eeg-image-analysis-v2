from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import os
import yaml


@dataclass
class AnalysisConfig:
    dataset: Dict[str, Any]
    selection: Dict[str, Any]
    components: List[str]
    preprocessing: Dict[str, Any]
    roi: Dict[str, Any]
    plots: Dict[str, Any]
    outputs: Dict[str, Any]
    # Optional measurement configuration; defaults will be applied in code paths
    # Expected keys (all optional):
    #   latency: "peak" | "fal"
    #   amplitude: "peak" | "mean"
    measurement: Dict[str, Any] = field(default_factory=dict)


def load_config(path: str) -> AnalysisConfig:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    required = [
        "dataset",
        "selection",
        "components",
        "preprocessing",
        "roi",
        "plots",
        "outputs",
    ]
    for key in required:
        if key not in data:
            raise ValueError(f"Missing required key in config: {key}")
    # Pass through optional measurement config if present; otherwise rely on default
    payload = {k: data[k] for k in required}
    if "measurement" in data and isinstance(data["measurement"], dict):
        payload["measurement"] = data["measurement"]
    return AnalysisConfig(**payload)


def load_electrodes_config(repo_root: str) -> Dict[str, List[str]]:
    """Load ROI electrode mappings from configs/electrodes.yaml."""
    path = os.path.join(repo_root, "configs", "electrodes.yaml")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Missing electrodes config: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # Expect top-level mapping of ROI name to list of channel labels
    return {str(k): list(v) for k, v in data.items() if isinstance(v, list)}


def load_components_config(repo_root: str) -> Dict[str, Dict[str, Any]]:
    """Load components config from configs/components.yaml."""
    path = os.path.join(repo_root, "configs", "components.yaml")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Missing components config: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    comps = data.get("components", {}) if isinstance(data, dict) else {}
    return comps


