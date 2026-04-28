from pathlib import Path

current = Path.cwd()
print(f"当前目录：{current}")

data_dir = current /"data" /"experiment"
print(f"拼接的路径：{data_dir}")

data_dir.mkdir(parents=True, exist_ok = True)
print(f"目录已创建：{data_dir.exists}")

file_path = data_dir /"test.txt"
file_path.write_text("Hello from pathlib", encoding ='utf-8')
print(f"文件已写入: {file_path}")

content = file_path.read_text(encoding ="utf-8")
print(f"读取内容：{content}")

txt_file = list(data_dir.glob("*.txt"))
print(f".txt文件列表：{txt_file}")

file_path.unlink
print("文件已删除")