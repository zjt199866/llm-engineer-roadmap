import json
from pathlib import Path

def save_json(data,filepath):
    Path(filepath).parent.mkdir(parents = True, exist_ok = True)
    with open(filepath, 'w', encoding = 'utf-8') as f:
        json.dump(data, f, indent = 2, ensure_ascii=False)

def load_json(filepath):
    if not Path(filepath).exists():
        return None
    with open(filepath,'r',encoding = 'utf-8') as f:
        return json.load(f)
if __name__ =="__main__":
    sample = {"name":"测试", "value":"42", "nested":[1, 2, 3]}
    save_json(sample, "test_output/sample.json")
    loaded = load_json("test_output/sample.json")
    print("保存并加载后相等：",loaded == sample)

    missing = load_json("nonexistent.json")
    print("文件不存在",missing)