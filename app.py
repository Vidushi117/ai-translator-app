# app.py
import streamlit as st
from translator import translate_text, recognize_speech, speak_text

st.set_page_config(page_title="🎤🔊 AI Translator", layout="centered")

st.title("🌐 AI Translator with Voice Input & Output")

# Initialize session state for inputs and output
if "text_input" not in st.session_state:
    st.session_state.text_input = ""
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# Text area (bound to session state)
st.session_state.text_input = st.text_area("Enter text to translate (or use microphone)", value=st.session_state.text_input)

# 🎙 Speech input
if st.button("🎙️ Use Microphone"):
    with st.spinner("Listening..."):
        recognized_text = recognize_speech()
        st.session_state.text_input = recognized_text
        st.success(f"You said: {recognized_text}")

# Language codes
language_dict = {
    "Auto Detect": "auto",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar"
}

col1, col2 = st.columns(2)
with col1:
    src_lang_name = st.selectbox("From", list(language_dict.keys()))
with col2:
    tgt_lang_name = st.selectbox("To", list(language_dict.keys())[1:])  # skip "auto"

src_lang = language_dict[src_lang_name]
tgt_lang = language_dict[tgt_lang_name]

# 🔁 Translate
if st.button("🔁 Translate"):
    if st.session_state.text_input.strip() == "":
        st.warning("Please enter or speak some text.")
    else:
        with st.spinner("Translating..."):
            translated = translate_text(st.session_state.text_input, tgt_lang, src_lang)
            st.session_state.translated_text = translated
            st.success(f"Translated Text: {translated}")

# 🔊 Speak translation
if st.session_state.translated_text:
    if st.button("🔊 Speak Translation"):
        audio_file = speak_text(st.session_state.translated_text, tgt_lang)
        st.audio(audio_file, format='audio/mp3')


