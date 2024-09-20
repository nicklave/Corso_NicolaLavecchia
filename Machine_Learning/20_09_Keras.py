from keras.api.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from keras.api.datasets import mnist
from keras.api.models import Sequential
from keras.api.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.api.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report

# Caricamento del dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Pre-elaborazione dei dati
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

# Reshape per adattarsi ai layer convoluzionali
X_train = X_train.reshape(-1, 28, 28, 1)  # Aggiunta del canale per scala di grigi
X_test = X_test.reshape(-1, 28, 28, 1)

# Conversione delle etichette in formato one-hot
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)