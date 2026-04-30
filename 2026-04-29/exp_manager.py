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
            exp_dir = self.base_dir / f"{safe_name}_{timestamp}"
        exp_dir.mkdir(parents=True , exist_ok=True)
       
        config_path = exp_dir / "config.json"
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config_dict, f, indent=2, ensure_ascii=False)
        
        metadata = {
            "exp_name": exp_name,
            "created_at":datetime.now().isoformat(),
            "base_dir":str(exp_dir)
        }
        meta_path = exp_dir/ "metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f , indent=2, ensure_ascii=False)

        print(f"[成功] 实验目录已创建：{exp_dir}")
        return exp_dir
    
    def list_experiments(self):
        dirs = [d for d in self.base_dir.iterdir() if d.is_dir()]
        return dirs
    
if __name__ == "__main__":
    mrg = ExperimentManager()
    dummy_config = {"lr": 0.001, "batch": 32}
    mrg.create_experiment("my first exp", dummy_config)
    print("所有实验", mrg.list_experiments())