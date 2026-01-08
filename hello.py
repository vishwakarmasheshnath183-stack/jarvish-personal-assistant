import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit


# --------------------------
# SPEECH SETUP
# --------------------------

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# --------------------------
# VOICE INPUT
# --------------------------

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language="en-in")
        print("You:", command)
        return command.lower()
    except:
        print("Say that again...")
        return ""


# --------------------------
# FEATURES
# --------------------------

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")


def search_wiki(query):
    speak("Searching Wikipedia...")
    result = wikipedia.summary(query, sentences=2)
    speak(result)


def open_website(site):
    websites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "github": "https://github.com",
        "stackoverflow": "https://stackoverflow.com"
    }

    for name in websites:
        if name in site:
            speak(f"Opening {name}")
            webbrowser.open(websites[name])
            return

    speak("Opening site")
    webbrowser.open("https://" + site)


def play_song(song):
    speak(f"Playing {song}")
    pywhatkit.playonyt(song)


# --------------------------
# MAIN LOOP
# --------------------------

speak("Jarvis Activated. How can I help?")

while True:
    command = listen()

    if "exit" in command or "stop" in command:
        speak("Goodbye!")
        break

    elif "time" in command:
        tell_time()

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        search_wiki(topic)

    elif "open" in command:
        site = command.replace("open", "").strip()
        open_website(site)

    elif "play" in command:
        song = command.replace("play", "").strip()
        play_song(song)

    else:
        speak("I didn't understand. Say again.")
