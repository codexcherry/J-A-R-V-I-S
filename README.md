# JARVIS AI Assistant

A comprehensive AI assistant with voice recognition, text-to-speech, image generation, and automation capabilities.

## 🚀 Quick Setup

### Prerequisites
- Python 3.8 or higher
- Windows 10/11 (recommended for best compatibility)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <your-repo-url>
   cd JARVIS
   ```

2. **Set up API keys:**
   ```bash
   # Copy the template and edit with your API keys
   cp config_template.py config.py
   # Edit config.py with your actual API keys
   ```

3. **Run the setup script:**
   ```bash
   python setup.py
   ```
   This will:
   - Create necessary directories
   - Install all dependencies

4. **Run JARVIS:**
   ```bash
   python app.py
   ```
   
   Or directly:
   ```bash
   python Frontend/Main.py
   ```

## ⚙️ Configuration

All configuration is now centralized in `config.py`. You can modify the following settings:

### API Keys
You need to obtain API keys from the following services:

1. **Cohere API** (for decision making and query classification)
   - Visit: https://cohere.ai/
   - Sign up and get your API key
   - Used for: Intelligent query routing and classification

2. **Groq API** (for chat responses and real-time search)
   - Visit: https://groq.com/
   - Sign up and get your API key
   - Used for: Conversational AI and web search integration

3. **Hugging Face API** (for image generation)
   - Visit: https://huggingface.co/
   - Sign up and get your API token
   - Used for: AI-powered image generation

**Important**: Copy `config_template.py` to `config.py` and add your actual API keys.

### User Settings
- `Username`: Your name
- `Assistantname`: Assistant's name (default: JARVIS)
- `InputLanguage`: Speech recognition language (default: "en")
- `AssistantVoice`: Text-to-speech voice (default: "en-CA-LiamNeural")
- `SpeechRate`: Speech rate adjustment (default: "+70%")

## 🔧 What Changed

### From .env to config.py
- **Before**: Used `.env` files with `python-dotenv`
- **After**: Centralized configuration in `config.py`
- **Benefits**: 
  - No dependency on `python-dotenv`
  - Easier to manage and modify
  - Better IDE support
  - Automatic environment variable setup

### Single Requirements File
- **Before**: Separate `requirements.txt` files in Backend and Frontend
- **After**: Single `requirements.txt` in root directory
- **Benefits**:
  - Easier dependency management
  - Single virtual environment
  - Consistent versions across modules

### Automated Setup
- **New**: `setup.py` script for one-command installation
- **Benefits**:
  - Automated virtual environment creation
  - Dependency installation
  - Directory structure setup
  - Cross-platform compatibility

## 📁 Project Structure

```
JARVIS/
├── config.py              # Central configuration file
├── requirements.txt       # All dependencies
├── setup.py              # Setup script
├── README.md             # This file
├── Backend/              # Core AI functionality
│   ├── Automation.py     # System automation
│   ├── Chatbot.py        # AI chat
│   ├── ImageGeneration.py # AI image generation
│   ├── Model.py          # Decision making model
│   ├── RealtimeSearchEngine.py # Web search
│   ├── SpeechToText.py   # Voice recognition
│   ├── TextToSpeech.py   # Text-to-speech
│   └── TestToSpeech.py   # Alternative TTS
├── Frontend/             # User interface
│   ├── Main.py           # Main application
│   ├── Graphics/         # GUI components
│   └── Files/            # Temporary files
└── Data/                 # Data storage
```

## 🎯 Features

- **Voice Recognition**: Speech-to-text with real-time processing
- **Text-to-Speech**: Natural voice synthesis
- **AI Chat**: Advanced conversation with Groq and Cohere
- **Image Generation**: AI-powered image creation
- **Web Search**: Real-time information retrieval
- **System Automation**: Open/close applications, control system
- **Modern GUI**: PyQt5-based interface with animations

## 🛠️ Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you're in the virtual environment
2. **API Errors**: Check your API keys in `config.py`
3. **Audio Issues**: Ensure your microphone and speakers are working
4. **GUI Issues**: Make sure PyQt5 is properly installed

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed: `pip list`
2. Verify your API keys are correct in `config.py`
3. Ensure you're running from the virtual environment
4. Check the console output for error messages

## 🔒 Security Notes

- **Never commit API keys to version control**
- **Use environment variables for production deployments**
- **Keep your API keys secure and private**
- **The `config.py` file is included in `.gitignore` for security**

## 📝 License

This project is for educational and personal use.

---

**Note**: Make sure to keep your API keys secure and never share them publicly!
