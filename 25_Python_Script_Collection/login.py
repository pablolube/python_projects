import customtkinter

# Configuración de apariencia
customtkinter.set_appearance_mode('light')  # Modo oscuro
customtkinter.set_default_color_theme('green')  # Tema azul

# Ventana principal
root = customtkinter.CTk()
root.geometry('720x300')

# Función al hacer login
def login():
    print('Bienvenido')

# Frame principal
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

# Título del formulario
label = customtkinter.CTkLabel(master=frame, text='Login')
label.pack(pady=12, padx=10)

# Campo de usuario
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)

# Campo de contraseña
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)

# Botón de login
button = customtkinter.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

# Ejecutar la app
root.mainloop()
