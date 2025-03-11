
'''
This file contains the function to process the command given by the user.

commands:
    - 'open <website>': Open the website in the browser.
    - 'run <application>': Run the application.
    - 'exit <application>': Exit the application.
    - 'search <query>': Search the query on Google.
    - 'play <music>': Play the music from the library.
    - 'exit' or 'quit' or 'goodbye': Exit the assistant.

'''

import os
import webbrowser
import subprocess
from talkback import speak
import library_list

def processCommand(c):
    c = c.lower()
    # Open the website
    if "open" in c:
        url = c.split("open")[1].strip()
        webbrowser.open(f"https://www.{url}.com")
        speak(f"Opening {url}...")

    # Run the application
    elif "run" in c:
        # Check if something follows 'run'
        app = c.split("run")[1].strip()
        if app:
            try:
                subprocess.Popen(app)
                speak(f"Running {app}...")
            except Exception as e:
                speak(f"Sorry, I could not run {app}.")
                print(f"Error (app): {e}")
        else:
            speak("Please specify the application to run.")

    # Exit the application
    elif "exit" in c:
        app = c.split("exit")[1].strip()
        try:
            os.system(f"taskkill /f /im {app}.exe")
            speak(f"Exiting {app}...")
        except Exception as e:
            speak(f"Sorry, I could not exit {app}.")
            print(f"Error (exit): {e}")

    # Search the query on Google
    elif "search" in c:
        query = c.split("search")[1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}...")

    # Play the music from the library
    elif c.startswith("play"):
        query = c.split("play")[1].strip()
        if query in library_list.music:
            link = library_list.music[query]
            webbrowser.open(link)
            speak(f"Playing {query}...")
        else:
            speak(f"Sorry, I could not find {query} in the music library.")
    
    else:
        speak("Sorry, I didn't understand that command.")
