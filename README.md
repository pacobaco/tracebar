# Re-run after kernel reset: Save the README content to a downloadable file

readme_content = """
# 🛰️ TraceBar

**TraceBar** is a lightweight, voice-activated system tray assistant that automatically scans documents and screenshots for Named Entities (NER) and Personally Identifiable Information (PII), summarizes the findings using OCR and NLP, and presents results through a simple desktop GUI.

---

## 🚀 Features

- 🎤 **Voice Activation**: Use natural voice commands to trigger document analysis.
- 🖥️ **System Tray Interface**: Runs quietly in your tray and listens for commands or manual actions.
- 🧠 **NER + PII Analysis**: Uses spaCy and pattern matching to identify names, emails, locations, and more.
- 📄 **Smart File Prioritization**: Automatically analyzes recent and semantically relevant files.
- 🖼️ **OCR for Screenshots**: Extracts text from PNG/JPG screenshots using Tesseract OCR.
- 🧾 **GUI Summary Popup**: Displays extracted entities in a clean, copyable window.
- 🔁 **Auto-Update Support**: Optional version-checking and self-updating with remote `version.json`.

---

## 📂 Folder Structure

```
TraceBar/
├── assets/               # App icon and UI assets
├── utils/                # Identity resolution, OCR, updater
├── tray.py               # System tray logic
├── gui.py                # Summary popup window
├── voice_commands.py     # Voice recognition logic
├── file_priority.py      # Smart file scanning
├── main.py               # App entry point
├── version.json          # Remote update config
├── requirements.txt      # Dependencies
└── build_and_zip.sh      # Build helper script
```

---

## 🛠️ Installation

1. **Install Python 3.9+**

2. **Clone this repository**:

```bash
git clone https://github.com/yourname/TraceBar.git
cd TraceBar
```

3. **Install requirements**:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

4. **Install Tesseract OCR**:
   - [Tesseract OCR Downloads](https://github.com/tesseract-ocr/tesseract)

5. **Run the app**:

```bash
python main.py
```

---

## 🛠️ Build as `.exe`

Make sure you have [`pyinstaller`](https://pyinstaller.org/):

```bash
pip install pyinstaller
bash build_and_zip.sh
```

This generates `TraceBar.exe` and a distributable `.zip`.

---

## 🧪 Voice Commands

Example phrases:

- `"summarize this document"`
- `"summarize screenshot"`
- `"what's in this file"`

---

## 📦 Auto-Update Setup (Optional)

1. Host a `version.json` file like this:

```json
{
  "latest_version": "1.0.0",
  "download_url": "https://yourdomain.com/TraceBar_v1.0.exe"
}
```

2. Update the URL in `utils/updater.py`.

---

## 📄 License

MIT License © 2025

---

## ✨ Credits

Built with ❤️ using Python, spaCy, Tesseract, Pystray, and OpenAI.
"""

file_path = "/mnt/data/README_TraceBar.md"
with open(file_path, "w") as f:
    f.write(readme_content)

file_path
