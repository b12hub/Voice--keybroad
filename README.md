# 🗣️ Voice Command Engine

A Python-based **Voice Command Engine** that allows you to control your computer using voice commands. 
This project leverages the `speech_recognition` and `keyboard` libraries to capture voice input and simulate key presses, providing hands-free interaction with your system.

---

## 🚀 Features

- **Speech Recognition**: Recognizes voice commands through Google Web Speech API, converting speech to text.
- **Customizable Key Mappings**: Control various keyboard keys with voice commands (e.g., `esc`, `ctrl+c`, `alt+f4`).
- **System Control Commands**: Special commands like `exit`, `pause`, and `resume` to control the engine's state.
- **Aliases**: Set up custom shortcuts for common commands (e.g., `save`, `copy`, `paste`).
- **Symbol Support**: Handles special characters like `!`, `@`, `$` mapped to their respective key combinations.
- **Command History**: Keeps track of all issued voice commands for later reference.
- **Easy-to-Use**: Simple to run and interact with, no setup required once dependencies are installed.

---

## 💻 Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/b12hub/Voice-keyboard.git
pip install speech_recognition pyaudio keyboard
cd voice-command-engine
python voice_keyboard.py
pyinstaller --onefile voice_keyboard.py

```

## 🔧 Features
- 🎤 Voice-to-text using Web Speech API
- 🧠 Smart error handling for noisy input
- 💡 Minimal UI for distraction-free typing


## 🌱 Future Plans
- Add language support
- Save voice input as a file
- Change program language to Rust🦀

## 🙌 Contributing
Pull requests are welcome!
