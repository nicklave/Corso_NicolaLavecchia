from keras.api.models import Sequential
from keras.api.datasets import mnist
from keras.api.layers import Dense
from keras.api.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
import pandas as pd

(X_train,y_train),(X_test,y_test) = mnist.load_data()

X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)

df = pd.DataFrame(X_train)
print(df)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

lb = LabelBinarizer()
y_train = lb.fit_transform(y_train)
y_test = lb.fit_transform(y_test)

model = Sequential()

# model.add(Dense(units=64, activation='relu', input_shape=(784,)))
# model.add(Dense(units=10, activation='softmax'))


# model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy','Precision'])


# history = model.fit(X_train, y_train,
#                     epochs=5,
#                     batch_size=16,
#                     validation_split=0.15)

# Perdita sul test set: 0.0942
# Accuratezza sul test set: 0.9740

model.add(Dense(units=128, activation='relu', input_shape=(784,)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy','Precision'])

history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.1)

# Perdita sul test set: 0.1010
# Accuratezza sul test set: 0.9778

test_loss, test_accuracy, test_precision = model.evaluate(X_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')

