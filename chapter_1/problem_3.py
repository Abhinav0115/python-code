import pyttsx3

engine = pyttsx3.init()


# RATE
engine.setProperty('rate', 150)     # setting up new voice rate

# VOLUME
engine.setProperty('volume', 0.9)    # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id) 


engine.say("Hi, I am a text to speech engine. I can help you to convert text to speech.")

engine.runAndWait()