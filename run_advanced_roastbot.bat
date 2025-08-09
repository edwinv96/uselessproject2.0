@echo off
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    🔥 RoastMaster 3000 🔥                    ║
echo ║              The Ultimate AI Roasting Experience              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo ⚠️  WARNING: This AI is designed to psychologically destroy you! ⚠️
echo.
echo Choose your preferred version:
echo.
echo 1. 🔥 Advanced RoastMaster 3000 (Psychological Warfare)
echo    - Personalized roasting based on your patterns
echo    - Irritation level tracking
echo    - Existential crisis induction
echo    - Quit encouragement system
echo.
echo 2. 😈 Basic RoastBot (Simple Sarcasm)
echo    - Standard sarcastic responses
echo    - Basic pattern recognition
echo    - Classic roasting experience
echo.
set /p choice="Enter your choice (1 or 2): "

if "%choice%"=="1" (
    echo.
    echo 🔥 Starting RoastMaster 3000 - Psychological Warfare Mode...
    echo ⚠️  The AI will now analyze your weaknesses and exploit them!
    echo.
    echo The bot will be available at: http://localhost:5000
    echo Press Ctrl+C to stop the psychological torture
    echo.
    python advanced_roast_bot.py
) else if "%choice%"=="2" (
    echo.
    echo 😈 Starting Basic RoastBot...
    echo The bot will be available at: http://localhost:5000
    echo Press Ctrl+C to stop the server
    echo.
    python roast_bot_web.py
) else (
    echo.
    echo ❌ Invalid choice! Please run the script again and choose 1 or 2.
    echo.
    pause
)
