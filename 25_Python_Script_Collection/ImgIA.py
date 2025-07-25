import numpy as np                  # Librería para manejo de arrays y operaciones numéricas
import streamlit as st             # Framework para crear interfaces web interactivas
from PIL import Image              # Para abrir y procesar imágenes
import tensorflow as tf            # Framework de deep learning para cargar y usar modelos entrenados

def main():
    # Título principal de la aplicación
    st.title('Clasificador de imágenes')
    
    # Instrucción para el usuario
    st.write('Cargá una imagen para predecir su clase')

    # Widget para cargar una imagen desde la computadora del usuario
    file = st.file_uploader('Cargar una imagen', type=['jpg', 'jpeg', 'png'])

    if file:
        # Abre la imagen utilizando PIL
        image = Image.open(file)

        # Muestra la imagen en la app
        st.image(image, caption='Imagen cargada', use_column_width=True)

        # Redimensiona la imagen a 32x32 píxeles, como lo espera el modelo CIFAR-10
        resized_image = image.resize((32, 32))

        # Convierte la imagen en un array NumPy y normaliza dividiendo por 255.0 (rango 0–1)
        img_array = np.array(resized_image) / 255.0

        # Ajusta la forma del array para que tenga el formato (1, 32, 32, 3)
        # 1: cantidad de imágenes, 32x32: tamaño, 3: canales RGB
        img_array = img_array.reshape((1, 32, 32, 3))

        # Carga el modelo previamente entrenado (debe estar en el mismo directorio)
        model = tf.keras.models.load_model('cifar10_model.h5')

        # Realiza la predicción
        predictions = model.predict(img_array)

        # Obtiene el índice de la clase con mayor probabilidad
        predicted_class = np.argmax(predictions)

        # Lista de clases del dataset CIFAR-10
        class_names = ['Avión', 'Automóvil', 'Pájaro', 'Gato', 'Ciervo',
                       'Perro', 'Rana', 'Caballo', 'Barco', 'Camión']

        # Muestra el resultado al usuario
        st.write(f'**Predicción:** {class_names[predicted_class]}')
        st.write(f'**Probabilidad:** {np.max(predictions)*100:.2f}%')

# Ejecuta la función principal al correr el script
if __name__ == '__main__':
    main()
