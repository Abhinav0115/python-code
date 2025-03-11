


import pyttsx3
tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    print(text)
    tts.runAndWait()