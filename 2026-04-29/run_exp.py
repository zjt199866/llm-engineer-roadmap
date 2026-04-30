from config_loader import load_config
from exp_manager import ExperimentManager
import sys

def main():
    if len(sys.argv) < 2:
        print("用法: python run_exp.py <config_file>")
        sys.exit(1)
    config_file = sys.argv[1]
    config = load_config(config_file)
    if not config:
        print("配置加载失败，退出")
        return
    
    exp_name = config.get("exp_name", "unnamed_exp")
    mgr = ExperimentManager()
    exp_dir = mgr.create_experiment(exp_name, config)
    print(f"实验已准备好，目录：{exp_dir}")

if __name__ == "__main__":
    main()
