from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS

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

def speak_text(text, lang_code="en"):
    tts = gTTS(text=text, lang=lang_code)
    filename = "output.mp3"
    tts.save(filename)
    return filename

