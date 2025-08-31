import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]  
        webbrowser.open(link)
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'jarvis'...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")

            if "jarvis" in word.lower():
                speak("Yes, I'm listening...")
                with sr.Microphone() as source:
                    print("jarvis Active... Speak your command")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except sr.WaitTimeoutError:
            # No speech detected within timeout → just restart loop
            continue
        except sr.UnknownValueError:
            # Speech not understood → ignore and continue
            continue
        except Exception as e:
            print("Error:", e)
