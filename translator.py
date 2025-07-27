# translator.py
import pyttsx3
from googletrans import Translator
import speech_recognition as sr

def translate_text(text, dest_lang, src_lang='auto'):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

def speak_text(text):
    engine = pyttsx3.init()
    
    # Optional: Configure voice settings
    engine.setProperty('rate', 150)     # Speed
    engine.setProperty('volume', 1.0)   # Max volume

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for female voice on some systems

    engine.say(text)
    engine.runAndWait()
