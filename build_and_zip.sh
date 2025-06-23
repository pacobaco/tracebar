#!/usr/bin/env bash
pyinstaller main.py --onefile --windowed --icon=assets/icon.png
cd dist
zip ../NERAssistant_v1.0.zip main.exe assets/icon.png
