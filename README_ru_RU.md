[English](/README.md) | [Русский](/README_ru_RU.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./media/logo-dark.png">
    <img alt="Project Logo" src="./media/logo-light.png" width="512" height="512">
  </picture>
</p>

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-blue?style=flat&logo=github)](https://github.com/AnikBeris/automatic-calculation-of-HLOD-Unreal-Engine)
[![License](https://img.shields.io/badge/License-purple?style=flat&logo=github)](./LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/your-repo?style=flat&logo=github&label=Stars&color=orange)](https://github.com/AnikBeris/automatic-calculation-of-HLOD-Unreal-Engine)

</div>

# Скрипт Unreal Engine для создания HLOD и MiniMap

> **Отказ от ответственности:** Этот проект предназначен только для личного обучения.

**Если этот проект оказался полезным для вас, вы можете оценить его, поставив звёздочку.**:star2:

<p align="left">
  <a href="https://pay.cloudtips.ru/p/7249ba98" target="_blank">
    <img src="./media/buymeacoffe.png" alt="Image">
  </a>
</p>

[Пожертвования горячо приветствуются, какими бы маленькими они ни были, и большое спасибо. 😌](https://pay.cloudtips.ru/p/7249ba98)

- **Bitcoin (BTC)** - `1Dbwq9EP8YpF3SrLgag2EQwGASMSGLADbh`
- **Ethereum (ERC20)** - `0x22258ea591966e830199d27dea7c542f31ed5dc5`
- **Binance Smart Chain (BEP20)** - `0x22258ea591966e830199d27dea7c542f31ed5dc5`
- **Solana (SOL)** - `yYYXsiVTzsvfvsMnBxfxSZEWTGytjAViE2ojf3hbLeF`

## Возможности
- Удаление всех текстовых и голосовых каналов на сервере.
- Удаление всех ролей, кроме стандартной роли @everyone.
- Простая настройка через `config.json`.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./media/05-info-channel-del.gif">
    <img alt="Project Logo" src="./media/05-info-channel-del.gif">
  </picture>
</p>


# Установка

## Клонируем репозиторий
```bash
git clone https://github.com/AnikBeris/automatic-calculation-of-HLOD-Unreal-Engine.git
cd Unreal-Engine-HLOD-Script
```

## Устанавливаем зависимости
```bash
pip install -r requirements.txt
```
## Запускаем бота
```bash
python Unreal-Engine-Script.py
```

---


## 1. Настройка скрипта
1. Скрипт позволяет вам легко выбрать каталог, в котором находится ваша установка Unreal Engine 5.
2. Логи будут сохраняться в той же директории, где находится скрипт. Нет необходимости вручную устанавливать путь к журналу.

---

## 2. Выбор каталога Unreal Engine 5
1. Когда вы запустите скрипт, он предложит вам выбрать папку, в которой установлен ваш Unreal Engine 5.
2. Выберите корневой каталог Unreal Engine 5 (например, `F:\Epic Games\UE_5.4\`).

---

## 3. Запуск скрипта
После того, как вы выбрали каталог Unreal Engine, скрипт автоматически создаст HLOD и мини-карту для вашего проекта.  
Он также создаст файл журнала в той же папке, где находится скрипт.

---

## License
This project is licensed under the [MIT License](https://github.com/your-repo/blob/main/LICENSE).

---

For detailed documentation, check out the [English README](/README.md) or [Русский README](/README_ru_RU.md).
