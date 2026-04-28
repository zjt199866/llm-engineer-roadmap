import json
import yaml
from pathlib import Path

def load_config(filepath):
    path = Path(filepath)

    if not path.exists():
        print(f"[警告] 配置文件不存在: {filepath}")
        return {}

    with open(path, 'r',encoding ='utf-8') as f:
        if path.suffix in ['.yaml', '.yml']:
            try:
                return yaml.safe_load(f) or {}
            except yaml.YAMLError as e:
                print(f"[错误] YAML 解析失败：{e}")
            return {}
        
        elif path.suffix ==".json":
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                print(f"[错误] JSON解析失败{e}")
            return {}
        else:
            print(f"[警告]不支持的文件格式:{filepath}")
            return {}

if __name__ == "__main__":
    sample_json = {"exp_name":"yaml_exp" , "learing_rat":0.1, "epoch":10}
    with open("sample_config.json","w", encoding ="utf-8" ) as f:
        json.dump(sample_json , f, indent=2)
    cfg = load_config("sample_config.json")
    print("加载 JSON配置:", cfg)

    sample_yaml = {"exp_name":"yaml_exp" , "batchsize":32, "dropout":0.1}
    with open("sample_config.yaml", "w", encoding= "utf-8") as f:
        yaml.dump(sample_yaml, f )
    cfg2= load_config("sample_config.yaml")
    print("加载 YAML配置", cfg2)