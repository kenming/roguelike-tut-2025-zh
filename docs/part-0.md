# Part 0: Setting Up - 環境設定

## 📋 基本資訊

> **原文連結**: [RoguelikeDev Tutorial Part 0](https://rogueliketutorials.com/tutorials/tcod/v2/part-0/)

### 📄 原文重點摘要

- 檢查 Python 程式設計基礎知識需求（特別是物件和函數概念）
- 安裝 Python 3.7+ 版本和 TCOD 函式庫
- 推薦使用虛擬環境和 requirements.txt 進行套件管理
- 選擇適合的程式編輯器（推薦 PyCharm 或 VS Code）
- 建立並執行第一個 tcod 程式驗證環境設定
- 下載教學所需的字體圖片檔案

## 📚 本章學習目標

- [x] 安裝 Python 開發環境 (Python 3.13.5)
- [x] 設定虛擬環境並安裝套件管理
- [x] 安裝並驗證 python-tcod 套件 (v19.3.1)
- [x] 安裝 Pygame 支援中文顯示 (v2.6.1)
- [x] 建立基本的專案結構與文檔
- [x] 配置 VSCode 開發環境與插件
- [x] 創建第一個 tcod 程式並成功執行
- [x] 設計混合渲染架構 (TCOD + Pygame)
- [x] 建立 requirements.txt 套件管理系統
- [x] 準備中文字體支援策略

## Prior Knowledge - 先備知識

### 原文的建議
本教學假設您對程式設計有基本的了解，特別是 Python。如果您從未使用過 Python，這個教學可能會有點困難。網路上有許多免費的 Python 學習資源（太多了無法一一列舉），建議您至少學會 Python 的物件和函數概念再開始這個教學。

當然，也有人忽略這個建議仍然成功完成了教學，所以如果您感覺勇敢，也可以直接開始！

### 個人建議
> P.S. 我正是從未接觸過 Python 與相關遊戲開發的經驗，不過個人推薦最好具有下列基礎：

- **基本程式語言基礎**：變數、控制流程、函數、物件導向
- **開發環境熟悉度**：如 VSCode 開發環境
- **AI 助手運用**：如使用 Copilot 或 Claude Code 或 Cursor，最好還能應用 MCP 機制

## Installation - 安裝

### Python 安裝

**下載連結**：[Python 官方網站](https://www.python.org/downloads/)

#### 專案使用版本
- **安裝版本**：Python 3.13.5
- **安裝路徑**：`C:\Program Files\Python313`
- **驗證方式**：在終端機執行 `python --version`

### TCOD 安裝

TCOD 是本教學的核心函式庫，用於建立 roguelike 遊戲。強烈建議使用虛擬環境來安裝 TCOD，以保持專案環境的獨立性。

**官方文檔**：[TCOD 安裝說明](https://python-tcod.readthedocs.io/en/latest/installation.html)

#### 虛擬環境設定

根據 [Python 官方虛擬環境文檔](https://docs.python.org/3/library/venv.html) 建議：

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (Windows PowerShell)
venv\Scripts\Activate.ps1

# 啟動虛擬環境 (Windows Command Prompt)
venv\Scripts\activate.bat

# 確認虛擬環境已啟動 (應該看到 (venv) 前綴)
```

#### 安裝 TCOD

```bash
# 在虛擬環境中安裝 TCOD
pip install tcod

# 驗證安裝
python -c "import tcod; print(f'TCOD 版本: {tcod.__version__}')"
```

#### 專案使用版本
- **實際安裝版本**：tcod 19.3.1 (2025年最新版)
- **原教學建議**：tcod >= 11.13 (已大幅超越)
- **安裝方式**：透過 pip 在虛擬環境中安裝
- **驗證方式**：匯入 tcod 模組並檢查版本

### Pygame 安裝

Pygame 不是原教學的必需套件，但我加入它是為了增強中文支援和音效功能。Pygame 提供更好的中文字體處理能力，這對中文化 roguelike 遊戲很有幫助。

**官方文檔**：[Pygame 官方網站](https://www.pygame.org/)

#### 安裝 Pygame

```bash
# 在虛擬環境中安裝 Pygame
pip install pygame

# 驗證安裝
python -c "import pygame; print(f'Pygame 版本: {pygame.version.ver}')"
```

#### 中文支援測試

```bash
# 測試 Pygame 初始化
python -c "import pygame; pygame.init(); print('Pygame 初始化成功')"
```

#### 專案使用版本
- **安裝目的**：中文字體支援、音效處理
- **安裝方式**：透過 pip 在虛擬環境中安裝
- **驗證方式**：匯入 pygame 模組並測試初始化

### Requirements.txt 設定

雖然上述已詳細說明各套件安裝方式，但建議建立 `requirements.txt` 檔案以便：
- 快速重建開發環境
- 確保版本一致性
- 便於專案分享和部署

#### 建立 Requirements.txt

```bash
# 方法1：使用專案提供的 requirements.txt (推薦)
# 檔案已在專案根目錄：requirements.txt
```

**檔案內容**：[`requirements.txt`](../requirements.txt) (核心遊戲依賴)
```txt
# PyRogue2025 專案依賴套件
tcod>=19.0.0
pygame>=2.6.0
```

**開發工具檔案**：[`requirements-dev.txt`](../requirements-dev.txt) (開發工具)
```txt
# 程式碼格式化、檢查、測試工具
black>=24.0.0
flake8>=7.0.0  
pytest>=8.0.0
```

```bash
# 方法2：自動生成當前環境 (會包含所有已安裝套件)
pip freeze > requirements.txt
```

#### 使用 Requirements.txt

```bash
# 安裝核心遊戲依賴
pip install -r requirements.txt

# 安裝開發工具 (可選，適合開發者)
pip install -r requirements-dev.txt

# 一次安裝所有套件
pip install -r requirements.txt -r requirements-dev.txt

# 驗證安裝
pip list
```

#### 開發工具說明

**為什麼分離？**
- **requirements.txt**：遊戲運行必需的套件
- **requirements-dev.txt**：開發過程輔助工具

**開發工具用途：**
- **black**：程式碼自動格式化，統一風格
- **flake8**：程式碼品質檢查，發現潛在問題  
- **pytest**：單元測試框架，確保程式正確性

#### 專案使用版本
- **檔案位置**：專案根目錄 `requirements.txt`
- **更新方式**：手動編輯或 `pip freeze` 重新生成
- **用途**：環境重建、版本控制、專案分享

## Editors - 編輯器

### 原文說明

任何文字編輯器都可以用來撰寫 Python。如果你真的想要的話，甚至可以使用 Notepad。就個人而言，我偏愛 PyCharm 和 Visual Studio Code。無論你選擇什麼，我強烈建議使用至少能幫助捕捉 Python 語法錯誤的工具。我使用 Python 已經超過五年了，但我仍然經常犯這類錯誤！

### VSCode 設定建議

本專案使用 **Visual Studio Code** 作為主要開發環境，以下是推薦的設定和插件：

#### 必裝插件

**核心必需：**
- **Python** (Microsoft) - Python 語言支援
- **Python Debugger** (Microsoft) - Python 偵錯器，設定斷點和逐步執行
- **Pylance** (Microsoft) - Python 語言伺服器，提供類型檢查和自動完成

**AI 輔助：**
- **GitHub Copilot** (GitHub) - AI 程式碼建議

> **注意**: Black 和 Flake8 已透過 requirements-dev.txt 安裝在虛擬環境中，不需要額外的 VSCode 插件

## Making sure Python works - 確認 Python 正常運作

為了驗證 Python 和 TCOD 安裝正常，於專案根目錄創建 `main.py` 檔案並輸入以下內容：

```python
#!/usr/bin/env python3
import tcod


def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
```

執行步驟：
```bash
# 1. 啟動虛擬環境
venv\Scripts\Activate.ps1

# 2. 執行程式
python main.py
```

**預期結果**：應該看到 "Hello World!" 輸出。如果出現錯誤，檢查 Python 或 TCOD 安裝。

✅ **測試成功** - 環境設定完成，可以開始下一部分！

## Font Setup - 字體設定 (混合渲染架構)

> **註記**：與教學不同，本專案採用混合渲染架構支援中文顯示。原教學方式可參考：[https://rogueliketutorials.com/tutorials/tcod/v2/part-0/#downloading-the-image-file](https://rogueliketutorials.com/tutorials/tcod/v2/part-0/#downloading-the-image-file)

## 相關資源與社群

### 官方資源
- **原始教學**：[RoguelikeDev Tutorial 2025](https://rogueliketutorials.com/tutorials/tcod/v2/)
- **TCOD 官方文檔**：[python-tcod.readthedocs.io](https://python-tcod.readthedocs.io/)

### 社群連結
- **Reddit 社群**：[r/roguelikedev](https://www.reddit.com/r/roguelikedev/)
- **Discord 伺服器**：[RoguelikeDev Discord](https://discord.gg/9pmFGKx)
- **社群活動**：[r/RoguelikeDev Does The Complete Roguelike Tutorial](https://www.reddit.com/r/roguelikedev/wiki/python_tutorial_series/)
