import json
from pathlib import Path
from datetime import datetime

class ExperimentManager():
    def __init__(self, base_dir="experiments"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        