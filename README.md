#### ANI-VOICE_ASSISTANT

<div align="center">
  <img src="assets/ani_icon.gif" width="300" alt="ANI Assistant Demo">
</div>

Your personal voice-controlled AI assistant with natural language processing and animated interface.

## 🌟 Key Features

### 🗣️ Voice Interaction
- Wake phrase detection ("Hey Ani")
- Real-time speech recognition
- Offline text-to-speech response system

### 🔍 Smart Capabilities
| Category       | Commands Examples                |
|----------------|----------------------------------|
| Entertainment  | "Play [song]", "Tell me a joke"  |
| Information    | "Who is...", "What time is it?"  |
| Productivity   | "Open Chrome", "Launch VS Code"  |

### 🖥️ Interactive GUI
- Animated Tkinter interface
- Visual feedback during listening/processing
- System tray integration (planned)

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- Windows/macOS/Linux
- Microphone

```bash
# Clone repository
git clone https://github.com/ani08-git/ANI-Voice_Assistant.git
cd ANI-Voice_Assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Core dependencies (if no requirements.txt)
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes pillow PyAudioWPatch

```

## 🚀 Quick Start

```bash
python assistant.py
```

**First Interaction:**
1. Wait for the ANI popup to appear
2. Speak clearly and wait for Ani to activate after "Hey Ani".
3. After the chime, speak your command
4. Try using a headset mic for better accuracy.


## 🧩 Command Reference

### 🎵 Media Control
- "Play [song name]" → Opens YouTube
- "Play music" → Plays default playlist

### ℹ️ Information
- "What's the time?" → Current time
- "Who is [person]?" → Wikipedia summary

### 🛠️ System
- "Open Chrome" → Launches browser
- "Sleep" → Returns to standby

## 📂 Project Structure

```
ANI-Voice_Assistant/
├── assistant.py           # Main assistant script
├── assets/
│   └── ani_icon.gif       # Animated GIF for GUI
├── venv/                  # Virtual environment
└── README.md              # This file


```

## ⚠️ Troubleshooting

**Common Issues:**
1. **Microphone not detected**:
   - Check system permissions
   - Try different microphone in code:
     ```python
     # In assistant.py
     mic = sr.Microphone(device_index=1)  # Change index
     ```

2. **Dependency errors**:
   ```bash
   pip install --force-reinstall PyAudioWPatch
   ```

## 🌈 Roadmap

### Next Version (v1.1)
- [ ] Weather forecast integration
- [ ] Reminder system
- [ ] Cross-platform support

### Future Ideas
- [ ] Machine learning for better voice recognition
- [ ] Home automation integration
- [ ] Mobile app companion

## 🤝 Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
