#!/bin/bash

# Build script for Linux/macOS

echo "========================================"
echo "SowardBot Build Script"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

echo "[1/4] Installing build requirements..."
pip3 install -r build_requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install build requirements"
    exit 1
fi

echo "[2/4] Building React dashboard..."
cd dashboard
npm install
npm run build
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to build React dashboard"
    cd ..
    exit 1
fi
cd ..

echo "[3/4] Creating PyInstaller distribution..."
pyinstaller pyinstaller.spec
if [ $? -ne 0 ]; then
    echo "ERROR: PyInstaller failed"
    exit 1
fi

echo "[4/4] Build complete!"
echo ""
echo "Executable created at: dist/SowardBot"
echo ""
