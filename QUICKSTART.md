# Quick Start Guide

## 🚀 Getting Started

### First Time Setup
1. **Run the setup script** (recommended):
   ```bash
   ./setup.sh
   ```
   This will install dependencies and set up the database.

2. **Or manual setup**:
   ```bash
   pip install -r requirements.txt
   cd src
   python Speed_Typing.py
   ```

### Running the Application
```bash
./launch.sh
```

### What to Expect
1. **Splash Screen** (3 seconds) - Shows project credits
2. **User Registration** - Create an account or login
3. **Main Menu** - Choose your typing activity:
   - **Speed Test**: Test your current typing speed
   - **Trainer**: Improve your skills with targeted practice

## 🎯 Features Overview

### Speed Test
- Type a paragraph as quickly and accurately as possible
- Get instant results: WPM, accuracy, time taken
- Both gross and net WPM calculated

### Trainer
- 60-second typing sessions
- Real-time feedback (green/red highlighting)
- Advanced error analysis
- Personalized practice modes:
  - Letter Practice (focus on problem keys)
  - Word Practice (words with your error letters)
- Detailed mistake reports

## 💡 Tips for Best Performance

### For Speed Tests
- Focus on accuracy first, speed will follow
- Don't rush - maintaining rhythm is key
- Use proper finger placement

### For Training
- Pay attention to the error analysis
- Use the specialized practice modes
- Regular practice sessions show best improvement

## 🔧 Troubleshooting

### Common Issues
- **"PIL not found"**: Run `pip install pillow`
- **Database errors**: Delete `database/userhistory.db` and restart
- **Icon not showing**: Ensure you're running from the correct directory

### Getting Help
- Check the full README.md for detailed documentation
- Review the Planning.txt in docs/ for development notes
- Ensure all files are in the correct directory structure

## 📊 Understanding Your Results

### WPM Calculation
- **Gross WPM**: Raw typing speed (includes errors)
- **Net WPM**: Adjusted for accuracy (recommended metric)
- Formula: (Characters ÷ 5) × (60 ÷ seconds) × accuracy

### Accuracy
- Percentage of correctly typed characters
- Minimum 30% accuracy required for gross WPM display
- Calculated using advanced string matching algorithms

---
**Happy Typing! 🎯**