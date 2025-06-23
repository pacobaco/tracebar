import requests, subprocess, shutil

UPDATE_INFO_URL = "https://your-repo.com/version.json"
CURRENT_VERSION = "1.0.0"

def check_for_update():
    try:
        r = requests.get(UPDATE_INFO_URL, timeout=5)
        data = r.json()
        if data["latest_version"] != CURRENT_VERSION:
            dl = requests.get(data["download_url"], stream=True)
            filename = f"update_{data['latest_version']}.exe"
            with open(filename, "wb") as f:
                shutil.copyfileobj(dl.raw, f)
            subprocess.Popen([filename])
            return True
    except Exception:
        pass
    return False