import os
import pystray
from PIL import Image
from threading import Thread
from voice_commands import listen_for_command
from file_priority import get_recent_txt_and_screenshots
from utils.identity_builder import build_identity_profile
from gui import show_summary

WATCH_FOLDER = os.path.expanduser("~/Documents")

def summarize_top():
    files = get_recent_txt_and_screenshots(WATCH_FOLDER)
    if not files:
        return
    _, path = files[0]
    if path.lower().endswith((".png", ".jpg")):
        profile = build_identity_profile(image_path=path, use_mock=False)
    else:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f: text = f.read()
        profile = build_identity_profile(text=text, use_mock=False)

    summary = f"""
{path}
Direct PII: {profile.get('direct_pii')}
Indirect PII: {profile.get('indirect_pii')}
NER: {profile.get('ner_entities')}
Confidence: {profile.get('resolution_confidence'):.2f}
"""
    show_summary(summary, os.path.basename(path))

def voice_loop():
    while True:
        cmd = listen_for_command()
        if "summarize" in cmd or "document" in cmd or "image" in cmd:
            summarize_top()

def setup_tray():
    icon = Image.open("assets/icon.png")
    tray = pystray.Icon("NER Assistant", icon, menu=pystray.Menu(
        pystray.MenuItem("Start Voice", lambda: Thread(target=voice_loop, daemon=True).start()),
        pystray.MenuItem("Quit", lambda icon, _: icon.stop())
    ))
    tray.run()
