# Importamos el dataset CIFAR-10 desde TensorFlow Datasets
from tensorflow.datasets import cifar10

# Importamos las clases necesarias para construir la red neuronal
from tensorflow.keras.models import Sequential              # Para crear un modelo secuencial
from tensorflow.keras.layers import Flatten, Dense          # Flatten para aplanar imágenes, Dense para capas densas
from tensorflow.keras.utils import to_categorical           # Para convertir etiquetas a one-hot encoding

# Cargamos el dataset CIFAR-10
# x_train, y_train: datos de entrenamiento (imágenes y etiquetas)
# x_test, y_test: datos de prueba
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalizamos las imágenes dividiendo por 255 (pasan de valores 0-255 a valores 0-1)
x_train = x_train / 255
x_test = x_test / 255

# Convertimos las etiquetas en vectores one-hot
# Por ejemplo, la etiqueta "3" se convierte en [0,0,0,1,0,0,0,0,0,0]
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definimos el modelo secuencial
model = Sequential([
    # Aplanamos la imagen de entrada (32x32x3 = 3072 píxeles en un solo vector)
    Flatten(input_shape=(32, 32, 3)),
    
    # Agregamos una capa densa con 1000 neuronas y función de activación ReLU
    Dense(1000, activation='relu'),
    
    # Capa de salida con 10 neuronas (una por cada clase del dataset)
    # Softmax se usa para clasificación multiclase
    Dense(10, activation='softmax')
])

# Compilamos el modelo:
# - Función de pérdida: categorical_crossentropy (porque usamos one-hot)
# - Optimizador: Adam (ajusta los pesos de forma eficiente)
# - Métrica: precisión (accuracy)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamos el modelo:
# - batch_size: 64 imágenes por lote
# - epochs: 10 pasadas completas por los datos de entrenamiento
# - validation_data: usamos el set de prueba para validar el rendimiento durante el entrenamiento
model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_test, y_test))

# Guardamos el modelo entrenado en un archivo .h5 (formato de Keras)
# Esto nos permite reutilizarlo sin tener que volver a entrenar
model.save('cifar10_model.h5')