@echo off
SETLOCAL EnableDelayedExpansion

echo ===================================================
echo   Car Selling Price Predictor - Auto Starter
echo ===================================================

cd /d "%~dp0Code\mysite"

:: 1. Check for Python
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.12.0.
    pause
    exit /b
)

:: 2. Check for Virtual Environment
if not exist "venv" (
    echo [INFO] Creating Virtual Environment...
    python -m venv venv
)

:: 3. Activate Virtual Environment
echo [INFO] Activating Virtual Environment...
call venv\Scripts\activate

:: 4. Install Requirements
echo [INFO] Installing/Updating dependencies...
pip install -r requirements.txt

:: 5. Run Migrations
echo [INFO] Applying database migrations...
python manage.py migrate

:: 6. Launch Browser (Optional but helpful)
echo [INFO] Starting web browser...
start http://127.0.0.1:8000/

:: 7. Start Django Server
echo [INFO] Starting server...
echo [HINT] Press Ctrl+C to stop the server.
python manage.py runserver

pause
