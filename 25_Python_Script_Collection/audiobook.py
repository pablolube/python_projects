from gtts import gTTS

# Abrimos el archivo de texto y leemos su contenido
with open('libro.txt', 'r', encoding='utf-8') as file:
    textBook = file.read()

# Creamos el objeto de texto a voz (idioma español)
audio = gTTS(text=textBook, lang='es')

# Guardamos el resultado en un archivo mp3
audio.save('audiobook.mp3')
