
import os
os.kill(os.getpid(),9)

import tensorflow as tf
from tensorflow import keras
print(tf.__version__)
import pandas as pd
import matplotlib as plt


(X_train_full, y_train_full), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
print(X_train_full.shape)
X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(300, activation="relu"))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(50, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))
model.compile(loss="sparse_categorical_crossentropy",optimizer="sgd", metrics=["accuracy"])
history = model.fit(X_train, y_train, epochs=30,validation_data=(X_valid, y_valid))