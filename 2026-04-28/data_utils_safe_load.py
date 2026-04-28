import json

def load_json_unsafe(filepath):
    with open(filepath, 'r', encoding ='utf-8') as f:
        return json.load(f)

def load_json_safe(filepath):
    try:
        with open(filepath, 'r', encoding = 'utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"警告：文件{filepath} 不存在，返回空字典")
    except json.JSONDecodeError:
        print(f"警告：文件{filepath} 不是合法的JSON，返回空字典")
    return {}

if __name__ == "__main__":
    a = load_json_safe("not_exist.json")
    print(a)
    with open("bad.json", "w", encoding="utf-8") as f:
        f.write("这不是json")
    b = load_json_safe("bad.json")
    print(b)
