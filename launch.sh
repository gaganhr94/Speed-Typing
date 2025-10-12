#!/bin/bash
# Speed Typing Application Launcher
# This script launches the Speed Typing application from the correct directory

echo "🚀 Starting Speed Typing Application..."
echo "📁 Navigating to source directory..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Navigate to the src directory
cd "$SCRIPT_DIR/src"

# Check if Python is available
if command -v python3 &> /dev/null; then
    echo "🐍 Using Python 3..."
    python3 Speed_Typing.py
elif command -v python &> /dev/null; then
    echo "🐍 Using Python..."
    python Speed_Typing.py
else
    echo "❌ Error: Python not found. Please install Python to run this application."
    exit 1
fi