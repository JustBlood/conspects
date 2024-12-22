import os
import re

def natural_sort_key(text):
    """Ключ для естественной сортировки"""
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

# Путь к папке с Markdown-файлами
folder_path = "."

# Получить список файлов в папке, отсортировать естественным образом
files = sorted(
    [f for f in os.listdir(folder_path) if f.endswith(".md")],
    key=natural_sort_key
)

for i, filename in enumerate(files):
    prev_link = f"[< Previous]({files[i-1]})" if i > 0 else ""
    next_link = f"[Next >]({files[i+1]})" if i < len(files) - 1 else ""
    
    navigation = f"{prev_link} | {next_link}".strip(" | ")

    # Прочитать содержимое файла
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Добавить или обновить навигацию
    content_lines = content.splitlines()
    if content_lines and content_lines[-1].startswith("[< Previous]"):
        content_lines = content_lines[:-1]
    content_lines.append(navigation)
    
    # Записать изменения обратно в файл
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(content_lines))

print("Ссылки успешно обновлены!")
