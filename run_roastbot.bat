@echo off
echo 🔥 Welcome to RoastBot Setup! 🔥
echo.
echo Choose your preferred version:
echo 1. Command Line Version (Simple text interface)
echo 2. Web Version (Modern GUI in browser)
echo.
set /p choice="Enter your choice (1 or 2): "

if "%choice%"=="1" (
    echo.
    echo Starting Command Line RoastBot...
    python roast_bot.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Web RoastBot...
    echo The bot will be available at: http://localhost:5000
    echo Press Ctrl+C to stop the server
    echo.
    python roast_bot_web.py
) else (
    echo Invalid choice! Please run the script again and choose 1 or 2.
    pause
)
