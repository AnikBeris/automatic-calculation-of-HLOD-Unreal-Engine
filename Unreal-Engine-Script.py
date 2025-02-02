import subprocess

# Путь к программе
program_path = r"F:\Epic Games\UE_5.4\Engine\Binaries\Win64\UnrealEditor.exe"
# путь к запуску проекта
uproject_path = r"D:/_SVN Unreal Projects/village/Villag/Village.uproject"
base_dir = r"F:/Epic Games/UE_5.4/Engine/Binaries/Win64/"
# куда сохраняем логи
log_path = r"F:/LOG_HLOD/WorldPartitionHLODsBuilder.log"
# путь до карты
level_path = r"/Game/_Games/1_Maps/1_1_GAMES_Level/L_Games_1"

# Аргументы запуска
arguments = [
    uproject_path,
    f"-BaseDir={base_dir}",
    r"-Unattended",
    f"-AbsLog={log_path}",
    level_path,
    r"-run=WorldPartitionBuilderCommandlet",
    # Билдим HLODs
    r"-Builder=WorldPartitionHLODsBuilder",
    # Билдим миникарту WorldPartition
    r"-Builder=WorldPartitionMiniMapBuilder",
    r"-SetupHLODs",
    r"-BuildHLODs",
    r"-AllowCommandletRendering",
]

# Запуск программы
try:
    subprocess.run([program_path] + arguments, check=True)
    print("Программа успешно запущена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске программы: {e}")
except FileNotFoundError:
    print("Указанный путь к программе не найден. Проверьте его корректность.")
