import subprocess
import os
import json

# Функция для проверки пути
def check_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Путь {path} не найден.")
    return path

# Загрузка конфигурации
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Получаем путь к текущей директории скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Загружаем пути из конфигурационного файла
ue5_root = config.get("ue5_root")
uproject_path = config.get("uproject_path")
log_path = os.path.join(script_dir, config.get("log_path"))
level_path = config.get("level_path")

# Проверка пути к Unreal Engine 5
try:
    # Проверка пути к Unreal Engine 5
    program_path = check_path(os.path.join(ue5_root, "Engine", "Binaries", "Win64", "UnrealEditor.exe"))
    
    # Проверка пути к проекту
    check_path(uproject_path)

    # Лог файл будет создан автоматически, если его нет
    if not os.path.exists(log_path):
        open(log_path, 'w').close()

    print(f"✅ Все пути корректны: {program_path}")
    print(f"Проект: {uproject_path}")
    print(f"Лог: {log_path}")
    
except FileNotFoundError as e:
    print(f"❌ {e}")
    exit(1)

# Аргументы запуска
arguments = [
    uproject_path,
    f"-BaseDir={ue5_root}",
    "-Unattended",
    f"-AbsLog={log_path}",
    level_path,
    "-run=WorldPartitionBuilderCommandlet",
    "-Builder=WorldPartitionHLODsBuilder",
    "-Builder=WorldPartitionMiniMapBuilder",
    "-SetupHLODs",
    "-BuildHLODs",
    "-AllowCommandletRendering",
]

# Запуск программы
try:
    print(f"✅ Запуск: {program_path} {' '.join(arguments)}")
    subprocess.run([program_path] + arguments, check=True)
    print("✅ Программа успешно запущена.")
except subprocess.CalledProcessError as e:
    print(f"❌ Ошибка при запуске программы: {e}")
except FileNotFoundError:
    print("❌ Указанный путь к Unreal Engine 5 не найден. Проверьте его корректность.")
