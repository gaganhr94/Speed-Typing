#!/bin/bash
# Speed Typing Application Setup Script
# Run this script to set up the application for first use

echo "🎯 Speed Typing Application Setup"
echo "================================="

# Check Python installation
echo "🐍 Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "✅ Python 3 found: $(python3 --version)"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    echo "✅ Python found: $(python --version)"
else
    echo "❌ Error: Python not found. Please install Python 3.6+ to continue."
    echo "Visit: https://www.python.org/downloads/"
    exit 1
fi

# Check pip installation
echo "📦 Checking pip installation..."
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
    echo "✅ pip3 found"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
    echo "✅ pip found"
else
    echo "❌ Error: pip not found. Please install pip to continue."
    exit 1
fi

# Install dependencies
echo "📥 Installing dependencies..."
$PIP_CMD install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Error installing dependencies. Please check your internet connection and try again."
    exit 1
fi

# Create database if it doesn't exist
echo "🗄️  Setting up database..."
cd src
$PYTHON_CMD -c "
import sqlite3
import os

# Create database directory if it doesn't exist
db_path = '../database/userhistory.db'
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE users (
        name text,
        username text
    )''')
    conn.commit()
    conn.close()
    print('✅ Database created successfully')
else:
    print('✅ Database already exists')
"

cd ..

echo ""
echo "🎉 Setup Complete!"
echo "==================="
echo ""
echo "To run the application:"
echo "  ./launch.sh"
echo ""
echo "Or manually:"
echo "  cd src"
echo "  $PYTHON_CMD Speed_Typing.py"
echo ""
echo "Enjoy improving your typing speed! 🚀"