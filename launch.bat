@echo off
title GPT Ultra Interactive - trhacknon
color 0A
echo === GPT Ultra Interactive - trhacknon ===
echo.

:: Vérifie Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installe. Veuillez l'installer.
    pause
    exit /b
)

:: Vérifie keys.txt
if not exist keys.txt (
    echo Aucun fichier keys.txt trouve. Creez le fichier avec vos cles OpenAI, une par ligne.
    pause
    exit /b
)

python gpt.py
pause
