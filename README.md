# Speed Typing Trainer & Test

A comprehensive Python-based typing application that helps users improve their typing speed and accuracy through various training modes and testing features.

## 🚀 Features

### Speed Typing Test
- **Accuracy Measurement**: Real-time accuracy calculation using advanced string matching
- **WPM Calculation**: Both Gross WPM and Net WPM (accounting for errors)
- **Time Tracking**: Precise timing with customizable test durations
- **Random Text Selection**: 21 different challenging paragraphs for varied practice

### Speed Typing Trainer
- **Adaptive Training**: 60-second typing sessions with instant feedback
- **Error Analysis**: Advanced algorithm identifies frequently mistyped keys
- **Personalized Practice Modes**:
  - **Letter Practice**: Focus on specific problematic keys
  - **Word Practice**: Target words containing error-prone letters
- **Detailed Reports**: Comprehensive analysis of typing mistakes
- **Real-time Scoring**: Live WPM and accuracy tracking

### User Management System
- **User Registration & Login**: SQLite database for user profiles
- **Progress Tracking**: Store and retrieve user statistics
- **User Management**: Edit, delete, and manage multiple user accounts

## 🛠️ Technology Stack

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Database**: SQLite3
- **Image Processing**: PIL (Python Imaging Library)
- **Text Analysis**: difflib for accuracy calculations

## 📁 Project Structure

```
Speed-Typing/
├── README.md                 # Project documentation
├── src/                     # Source code files
│   ├── Speed_Typing.py      # Main application entry point
│   ├── Speed_Trainer.py     # Typing trainer module
│   ├── historydatabase.py   # User management and database operations
│   └── CreateDatabase.py    # Database initialization script
├── assets/                  # Application resources
│   ├── Splash.png          # Splash screen image
│   └── TypingLOGO.ico      # Application icon
├── data/                   # Data files
│   ├── WordList.txt        # 3000+ words for training
│   └── Text_Lines.txt      # Test paragraphs (21 lines)
├── database/               # Database files
│   └── userhistory.db     # SQLite user database
```

## 🔧 Installation & Setup

### Prerequisites
```bash
# Required Python packages
pip install pillow
```

### Quick Start
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Speed-Typing
   ```

2. **Run the application**
   ```bash
   cd src
   python Speed_Typing.py
   ```

3. **First Time Setup**
   - The splash screen will display for 3 seconds
   - Register a new user account or login with existing credentials
   - Choose between Speed Test or Training modes

## 🎯 How to Use

### Speed Typing Test
1. Click "TYPING SPEED TEST" from the main menu
2. Wait for the countdown timer (3 seconds)
3. Type the displayed paragraph accurately
4. Press space after each word or Enter to submit
5. View your results:
   - **Total Time**: Time taken to complete
   - **Accuracy**: Percentage of correct characters
   - **Gross WPM**: Raw typing speed
   - **Net WPM**: Adjusted for accuracy

### Speed Typing Trainer
1. Click "TYPING TRAINER" from the main menu
2. Type the displayed words within 60 seconds
3. Words turn green (correct) or red (incorrect) in real-time
4. After completion, view your performance analysis
5. Use specialized practice modes based on your errors:
   - **Letter Practice**: Focus on problematic keys
   - **Word Practice**: Practice words with your error letters

### User Management
- **Registration**: Enter name and username to create account
- **Login**: Use existing credentials to access your profile
- **Edit Details**: Modify user information
- **View Users**: See all registered users
- **Delete Account**: Remove user profiles

## 🏗️ Architecture & Features

### Core Components

#### 1. Speed_Typing.py (Main Application)
- **Splash Screen**: Professional startup with project credits
- **Main Menu**: Navigation hub for all features
- **Speed Test Engine**:
  - Real-time word highlighting
  - Accuracy calculation using `difflib.SequenceMatcher`
  - Dynamic color coding (green/red for correct/incorrect)
  - WPM calculation: `(characters/5) * (60/time_seconds)`

#### 2. Speed_Trainer.py (Training Module)
- **Adaptive Word Generation**: Random selection from 3000+ word database
- **Error Analysis Algorithm**:
  - Tracks character-level mistakes
  - Identifies most frequent error keys
  - Generates targeted practice sessions
- **Three Training Modes**:
  - Normal practice (random words)
  - Letter practice (character-focused)
  - Word practice (contextual)

#### 3. historydatabase.py (User System)
- **SQLite Integration**: Robust user data management
- **CRUD Operations**: Complete user lifecycle management
- **Data Validation**: Input sanitization and error handling
- **Session Management**: User authentication flow

### Advanced Features

#### Real-time Visual Feedback
- **Dynamic Text Highlighting**: Current word highlighted in green
- **Immediate Error Indication**: Wrong words turn red instantly
- **Progress Tracking**: Live WPM and accuracy updates

#### Personalized Training Generation
- **Letter Practice**: Creates random character combinations using your most problematic keys
- **Word Practice**: Filters the 3000+ word database to find words containing your error letters
- **Adaptive Difficulty**: Adjusts based on your performance patterns

## 🎨 User Interface

### Design Philosophy
- **Clean, Intuitive Layout**: Easy navigation for all skill levels
- **Color-Coded Feedback**: Immediate visual confirmation
- **Responsive Design**: Scales across different screen sizes
- **Professional Aesthetics**: Modern color schemes and typography

### Key UI Elements
- **Splash Screen**: Branded startup experience
- **Main Menu**: Central navigation hub
- **Test Interface**: Distraction-free typing environment
- **Results Display**: Comprehensive performance metrics
- **Training Dashboard**: Real-time progress tracking

---

**Happy Typing! 🚀**

*Improve your typing speed and accuracy with our comprehensive training system.*