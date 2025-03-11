import speech_recognition as sr
from command_control import processCommand
from talkback import speak

recognizer = sr.Recognizer()

wakeup_word = "prime" # The word that will wake up the assistant
Assistant_name = "prime" # The name of the assistant

if __name__ == "__main__":
    speak(f"Initializing {Assistant_name}...")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            # Listening to the wakeup word
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print("You said: " + word)

            if word.lower() == wakeup_word.lower():
                speak("Yes, I'm listening...")

                # Listening to the command
                with sr.Microphone() as source:
                    print(f"{Assistant_name} listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("You said: " + command)
            
                    processCommand(command)
                    

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")
        except Exception as e:
            print("Error (main): {0}".format(e))
