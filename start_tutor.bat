@echo off
echo 🎓 AI Tutor Chatbot - Windows Launcher
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found!

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo ✅ Dependencies installed!
echo.

REM Start the application
echo 🚀 Starting AI Tutor Chatbot...
echo 📖 The application will open in your browser automatically
echo 💡 If it doesn't open, go to: http://localhost:8501
echo 🛑 Press Ctrl+C to stop the application
echo.

streamlit run app.py

echo.
echo 👋 Thanks for using AI Tutor Chatbot!
pause
