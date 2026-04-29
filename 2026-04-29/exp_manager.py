import json
from pathlib import Path
from datetime import datetime

class ExperimentManager():
    def __init__(self, base_dir="experiments"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def create_experiment(self, exp_name, config_dict):
        safe_name = exp_name.replace(" ", "_")
        exp_dir = self.base_dir / safe_name
    
        if exp_dir.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            exp_dir = self.base_dir/ f"{safe_name}_{timestamp}"
        exp_dir.mkdir(parents=True , exit_ok=True)

        config_path = exp_dir / "config.json"
        with open(config.json, "w", encoding="utf-8") as f:
            json.dump(config_path, f, indent=2, ensure_ascii=false)
            