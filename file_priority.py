import os, time

KEYWORDS = ["elon musk", "resume", "report", "therapy", "ai", "johnny babylon"]

def get_recent_txt_and_screenshots(folder):
    now = time.time()
    results = []
    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)
        if os.path.isfile(path) and (path.endswith(".txt") or path.endswith((".png", ".jpg"))):
            age = now - os.path.getmtime(path)
            score = 1000 - age
            with open(path, 'rb') as f:
                content = f.read().lower()
                for kw in KEYWORDS:
                    if kw in str(content):
                        score += 500
                        break
            results.append((score, path))
    return sorted(results, reverse=True)
