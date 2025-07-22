#shutdown /s /t

import os
import platform

respuesta = input('¿Quieres apagar el ordenador? (sí/no): ').strip().lower()

if respuesta in ['si', 'sí', 's']:
    if platform.system() == 'Windows':
        print("Apagando el equipo...")
        os.system('shutdown /s /t 1')
    else:
        print("Este script está diseñado para Windows.")
else:
    print("Operación cancelada.")
