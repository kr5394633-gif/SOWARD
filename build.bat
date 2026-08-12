@echo off
REM Build script for creating SowardBot.exe

echo ========================================
echo SowardBot Build Script
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [1/4] Installing build requirements...
pip install -r build_requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install build requirements
    pause
    exit /b 1
)

echo [2/4] Building React dashboard...
cd dashboard
npm install
npm run build
if errorlevel 1 (
    echo ERROR: Failed to build React dashboard
    cd ..
    pause
    exit /b 1
)
cd ..

echo [3/4] Creating PyInstaller distribution...
pyinstaller pyinstaller.spec
if errorlevel 1 (
    echo ERROR: PyInstaller failed
    pause
    exit /b 1
)

echo [4/4] Build complete!
echo.
echo Executable created at: dist/SowardBot.exe
echo.
pause
