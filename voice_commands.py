import speech_recognition as sr

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        audio = r.listen(mic, phrase_time_limit=5)
    try:
        return r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
