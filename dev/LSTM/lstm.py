import tensorflow as tf
from tensorflow import keras
import numpy as np

data = [1,2,3,1,2,1,3,2,2,3,1]

x = [ data[i:i+5] for i in range(0, len(data)-5) ]
y = [ i for i in data ][5:]

x = np.array(x)
y = np.array(y)

x = x.reshape(x.shape[0], x.shape[1], 1)

print (x[:2])

model = keras.models.Sequential([
    keras.layers.LSTM(50, input_shape=(5,1)),
    keras.layers.Dense(3)
])

model.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])
model.fit(x,y,epochs=200, verbose=2)

test_data = np.array([160, 170, 180, 190, 200])
test_data = test_data.reshape((1, 5, 1))

predictNextNumber = model.predict(test_data, verbose=1)
print(predictNextNumber)
