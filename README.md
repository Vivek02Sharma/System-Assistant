# System Assistant

A Python-based voice-controlled personal assistant inspired by JARVIS from Iron Man. This desktop application provides hands-free control of your computer through natural language voice commands, enabling users to perform various tasks such as playing media, managing to-do lists, sending communications, searching the web, and getting AI-powered responses.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Voice Commands](#voice-commands)
- [Architecture](#architecture)
- [Modules](#modules)
- [Contributing](#contributing)
- [License](#license)

## Features

- Voice Recognition: Listens and processes natural language voice commands
- Text-to-Speech: Responds audibly using the pyttsx3 engine
- AI-Powered Responses: Utilizes Groq's Mixtral-8x7b model for intelligent conversational responses
- Media Control: Plays music and videos through YouTube
- Application Launcher: Opens web applications and Windows desktop applications
- Task Management: Maintains a to-do list with add, read, and clear functionality
- Wikipedia Search: Retrieves summaries from Wikipedia
- Google Search: Performs web searches directly from voice commands
- Email Integration: Sends emails via Gmail SMTP
- WhatsApp Messaging: Schedules and sends WhatsApp messages
- Translation: Translates text to Hindi
- Secure Login System: User authentication with hashed passwords and a modern GUI

## Prerequisites

Before installing the System Assistant, ensure you have the following:

- Python 3.8 or higher
- Windows operating system (required for some features like win10toast and Windows app launching)
- Working microphone for voice input
- Internet connection for API calls and web services
- Groq API key for AI responses
- Gmail account with App Password for email functionality (optional)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Vivek02Sharma/System-Assistant.git
cd System-Assistant
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Install PyAudio (may require additional steps on Windows):

If you encounter issues installing PyAudio, download the appropriate wheel file for your Python version and architecture from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install it manually:

```bash
pip install PyAudio‑<version>‑<python_version>‑<python_version>‑<architecture>.whl
```

For example, for Python 3.10 on 64-bit Windows:
```bash
pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl
```

5. Set up the environment variables (see Environment Variables section below).

## Environment Variables

Create a `.env` file in the root directory of the project with the following variables:

```env
GROQ_API_KEY=your_groq_api_key_here
EMAIL=your_gmail_address@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

### Obtaining API Keys

**Groq API Key:**
1. Visit https://console.groq.com/
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key

**Gmail App Password:**
1. Enable 2-Factor Authentication on your Google account
2. Go to Google Account settings
3. Navigate to Security, then App passwords
4. Generate a new app password for Mail

## Project Structure

```
System-Assistant/
├── main.py              # Application entry point
├── login.py             # GUI login system with user registration
├── assistant.py         # Core JarvisAssistant class with voice and command routing
├── ai_helper.py         # Groq AI integration for conversational responses
├── app_controller.py    # Web and Windows application launcher
├── communication.py     # Email, WhatsApp, and translation services
├── media_controller.py  # YouTube media playback
├── task_manager.py      # To-do list management
├── wiki_searcher.py     # Wikipedia search functionality
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore file
└── .env                 # Environment variables (create this file)
```

## Usage

1. Start the application:

```bash
python main.py
```

2. A login window will appear. Register a new account or log in with existing credentials.

3. Upon successful login, the assistant will greet you based on the time of day and begin listening for commands.

4. Speak your commands clearly. The assistant will process your request and respond both verbally and in the console.

5. To exit the application, say "exit", "bye", or "goodbye".

## Voice Commands

### Time and Date
- "What time is it?" or "Tell me the time"
- "What is the date?" or "Tell me today's date"

### Media Control
- "Play [song name]" - Opens YouTube search for the specified song
- "Play music [genre/artist]" - Plays music on YouTube

### Task Management
- "Add task [task description]" - Adds a new task to your to-do list
- "Read tasks" or "Read to do" - Lists all current tasks
- "Clear tasks" or "Clear" - Removes all tasks from the list

### Application Control
- "Open YouTube" - Opens YouTube in browser
- "Open Google" - Opens Google in browser
- "Open WhatsApp" - Opens WhatsApp Web
- "Open Gmail" - Opens Gmail
- "Open ChatGPT" - Opens ChatGPT
- "Open GitHub" - Opens GitHub
- "Open Notepad" - Opens Windows Notepad
- "Open Calculator" - Opens Windows Calculator
- "Open Chrome" - Opens Google Chrome
- "Open VS Code" - Opens Visual Studio Code

### Web Search
- "Search [query]" - Performs a Google search
- "Wikipedia [topic]" - Searches Wikipedia for information

### Communication
- "Send email" - Initiates email composition (prompts for recipient, subject, and message)
- "WhatsApp [message]" - Schedules a WhatsApp message (prompts for phone number and message)
- "Translate [text]" - Translates the specified text to Hindi

### General Queries
- Any other query is processed by the AI assistant, which provides intelligent, context-aware responses

## Architecture

The System Assistant follows a modular architecture with clear separation of concerns:

### Core Components

**JarvisAssistant (assistant.py)**
The central orchestrator that initializes all modules and handles:
- Voice recognition using SpeechRecognition library
- Text-to-speech output using pyttsx3
- Command routing to appropriate handlers
- Conversation flow management

**Login System (login.py)**
A CustomTkinter-based GUI providing:
- User registration with password hashing (SHA-256)
- Secure login validation
- Modern dark-themed interface

**AI Helper (ai_helper.py)**
Integration with Groq's API providing:
- Natural language understanding
- Context-aware responses using chat history
- Fallback for unrecognized commands

### Support Modules

**AppController (app_controller.py)**
Manages application launching:
- Web applications via browser
- Windows desktop applications via subprocess

**Communication (communication.py)**
Handles external communications:
- Email via SMTP (Gmail)
- WhatsApp messages via pywhatkit
- Text translation via mtranslate

**MediaController (media_controller.py)**
Controls media playback:
- YouTube video/music search and playback

**TaskManager (task_manager.py)**
Manages to-do list functionality:
- File-based task persistence
- Add, read, and clear operations

**WikiSearcher (wiki_searcher.py)**
Provides Wikipedia integration:
- Topic search and summary retrieval
- Error handling for disambiguation and missing pages

## Modules

### Dependencies

| Package | Purpose |
|---------|---------|
| pyttsx3 | Text-to-speech conversion |
| speechrecognition | Voice input processing |
| wikipedia | Wikipedia API integration |
| pywhatkit | WhatsApp messaging automation |
| python-dotenv | Environment variable management |
| groq | Groq AI API client |
| win10toast | Windows toast notifications |
| pyaudio | Audio input/output handling |
| mtranslate | Text translation service |
| tkinter | GUI library (built-in) |
| customtkinter | Modern themed Tkinter widgets |

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```
3. Make your changes and commit:
```bash
git commit -m "Add your feature description"
```
4. Push to your fork:
```bash
git push origin feature/your-feature-name
```
5. Open a Pull Request with a detailed description of your changes

### Guidelines

- Follow PEP 8 coding style guidelines
- Add appropriate error handling for new features
- Update documentation for any new functionality
- Test your changes thoroughly before submitting

## License

This project is open source and available for personal and educational use.

---

For issues, questions, or feature requests, please open an issue on the GitHub repository.
