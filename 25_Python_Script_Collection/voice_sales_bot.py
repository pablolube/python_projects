# app_streamlit_voice.py

import streamlit as st
import speech_recognition as sr
import webbrowser
import pyttsx3
import threading

# Inicializo motor de texto a voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Elegí una voz que no dé error
for voice in voices:
    if "spanish" in voice.name.lower() or "es" in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break
else:
    # Si no hay voz en español, usá la primera voz disponible
    engine.setProperty('voice', voices[0].id)

# Reconocedor de voz
recognizer = sr.Recognizer()

# Función para hablar y reconocer lo que se dice
def escuchar_microfono():
    try:
        with sr.Microphone() as source:
            st.info("🎙️ Esperando que hables...")
            audio = recognizer.listen(source, timeout=5)
            texto = recognizer.recognize_google(audio, language='es-AR')
            st.success(f"✅ Has dicho: {texto}")
            return texto.lower()
    except sr.UnknownValueError:
        st.error("❌ No se entendió lo que dijiste.")
    except sr.RequestError:
        st.error("⚠️ No se pudo conectar con el servicio de reconocimiento.")
    except sr.WaitTimeoutError:
        st.warning("⏱️ No se detectó ningún sonido.")
    return ""

# Acción principal
def ejecutar_busqueda_amazon():
    engine.say("¿Qué quieres comprar en Amazon?")
    engine.runAndWait()
    texto = escuchar_microfono()
    if texto:
        url = f"https://www.amazon.com/-/es/s?k={texto}"
        st.markdown(f"[🔗 Abrir búsqueda en Amazon]({url})", unsafe_allow_html=True)
        webbrowser.open(url)

# Streamlit UI
st.set_page_config(page_title="Buscador por Voz", page_icon="🎤")

st.title("🎤 Buscador por Voz")
st.write("Probá decir algo y buscarlo directamente en Amazon.")

if st.button("🎧 Hablar y Buscar"):
    threading.Thread(target=ejecutar_busqueda_amazon).start()
