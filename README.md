
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

# Unreal Engine script for building HLODs and MiniMap

> **Disclaimer:** This project is intended for educational and personal use only. Do not use it in production environments without appropriate testing.

**If you like this project, don't forget to leave a star.**:star2:

<p align="left">
  <a href="https://pay.cloudtips.ru/p/7249ba98" target="_blank">
    <img src="./media/buymeacoffee.png" alt="Image">
  </a>
</p>

[Donations are warmly welcomed no matter how small and thank you very much. 😌](https://pay.cloudtips.ru/p/7249ba98)

- **Bitcoin (BTC)** - `1Dbwq9EP8YpF3SrLgag2EQwGASMSGLADbh`
- **Ethereum (ERC20)** - `0x22258ea591966e830199d27dea7c542f31ed5dc5`
- **Binance Smart Chain (BEP20)** - `0x22258ea591966e830199d27dea7c542f31ed5dc5`
- **Solana (SOL)** - `yYYXsiVTzsvfvsMnBxfxSZEWTGytjAViE2ojf3hbLeF`


## Features
- Automates the process of building HLODs and mini-maps in Unreal Engine 5.  
- Allows easy configuration and setup through a GUI and path selection.  
- Logs the progress of the operation and saves logs in the same folder as the script.  

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./media/05-info-channel-del.gif">
    <img alt="Project Logo" src="./media/05-info-channel-del.gif">
  </picture>
</p>


# Installation

## Clone the Repository
```bash
git clone https://github.com/AnikBeris/automatic-calculation-of-HLOD-Unreal-Engine.git
cd Unreal-Engine-HLOD-Script
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Run the Script
```bash
python Unreal-Engine-Script.py
```

---

## 1. Configuring the Script
1. The script allows you to easily select the directory where your Unreal Engine 5 installation is located.
2. Logs will be saved in the same directory where the script is located. No need to manually set the log path.

---

## 2. Choosing the Unreal Engine 5 Directory
1. When you run the script, it will prompt you to select the folder where your Unreal Engine 5 is installed.
2. Select the root directory of Unreal Engine 5 (e.g., `F:\Epic Games\UE_5.4\`).

---

## 3. Running the Script
Once you have selected the Unreal Engine directory, the script will automatically build the HLODs and mini-map for your project.  
It will also generate a log file in the same folder as the script.

---

## License
This project is licensed under the [MIT License](https://github.com/YourUsername/Unreal-Engine-Script/blob/main/LICENSE).

---

For detailed documentation, check out the [English README](/README.md) or [Русский README](/README_ru_RU.md).
