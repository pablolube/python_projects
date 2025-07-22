import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Escuchando...")
    recognizer.adjust_for_ambient_noise(source)  # Esto ayuda a reducir el ruido de fondo
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language='es-ES')  # Español de España o usa 'es-AR' si estás en Argentina
    print(f'Has dicho: {text}')
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print(f"Error al conectarse al servicio de reconocimiento: {e}")

