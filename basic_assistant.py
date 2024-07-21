import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()  # Initialize engine within function
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()  # Initialize recognizer within function
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

if __name__ == "__main__":
    wake_word = "hey tony"
    while True:
        text = listen()
        if text and wake_word in text.lower():
            speak("Hello there!")
