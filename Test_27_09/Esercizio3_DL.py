# Descrizione: Utilizza il dataset MNIST fornito da Keras per costruire 
# una semplice rete neurale feedforward (Multi-Layer Perceptron) 
# che riconosca le cifre scritte a mano.

from keras.api.datasets import mnist
from keras.api.models import Sequential
from keras.api.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.api.utils import to_categorical
from keras.api.regularizers import l2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X_train, y_train, X_test, y_test = mnist.load_data()

X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)

df = pd.DataFrame(X_train)
print(df)

X_train = X_train.values / 255

y_train = to_categorical(y_train)

model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1),kernel_regularizer='l2'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu',kernel_regularizer='l2'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs= 10, batch_size=32, validation_split=0.1)

test_loss, test_accuracy = model.evaluate(X_test, y_test)

print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')

predizione = model.predict(X_test)
classe_predetta = np.argmax(predizione, axis=1)
classe_reale = np.argmax(y_test, axis=1)

immagini = int(input('Quante immagini vuoi visualizzare? '))
plt.figure(figsize=(15, 3))
for i in range(immagini):
    image = X_test[i].reshape(28, 28)
    true_label = classe_reale[i]
    predicted_label = classe_predetta[i]
    plt.subplot(1, immagini, i + 1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(f'T:{true_label}, P:{predicted_label}')
plt.show()

