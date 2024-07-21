import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()  # Convert to lowercase for comparison
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    wake_word = "hey tony"
    while True:
        text = listen()
        if text and wake_word in text:
            speak("Hello there!")
