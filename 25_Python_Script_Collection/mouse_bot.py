import pyautogui as botMouse  # Importa el módulo pyautogui, que permite controlar el mouse y el teclado. Se lo renombra como 'botMouse'.
import webbrowser             # Importa el módulo webbrowser, que permite abrir URLs en el navegador.
import random                 # Importa random para generar números aleatorios.
import time                   # Importa time para usar delays (esperas).

webbrowser.open('https://www.linkedin.com/feed/')  # Abre la página del feed de LinkedIn en el navegador predeterminado.
while True:  # Bucle infinito que se ejecuta continuamente.
    print(botMouse.position())
    x = random.randint(400, 900)  # Genera una coordenada X aleatoria entre 400 y 900 píxeles.
    y = random.randint(100, 700)  # Genera una coordenada Y aleatoria entre 100 y 700 píxeles.
    botMouse.moveTo(x, y, 0.5)    # Mueve el mouse a la posición (x, y) en 0.5 segundos.
    time.sleep(2)                # Espera 2 segundos antes de repetir el movimiento.
