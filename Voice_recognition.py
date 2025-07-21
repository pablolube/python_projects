#Install speechrecognition with pip install speechrecognition
#Install pttsx3 with pip install pyttsx3

import speech_recognition as sr
import webbrowser
import pyttsx3

def talk():
    mic=sr.Microphone()
    with mic as source:
        audio=recognizer.listen(source)
    text=recognizer.recognize_google(audio,language='es-Ar')
    print(f'Has dicho: ')
    return text.lower()


#Inicio el objeto
recognizer =sr.Recognizer()

engine=pttsx3.init()


if 'amazon' in talk():
    engine.say('Que quieres comprar en Amazon')
    engine.runAndWait()
    text=talk()
    webbrowser.open(f'https://www.amazon.com/-/es/s?k={text}')

