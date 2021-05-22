import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data = np.load('data/rssi.npz', allow_pickle=True)  # load MFCCs
x, y = data['out_x'], data['out_y']  # load into np arrays

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=True, test_size=0.4)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(100, activation='softmax', input_shape=x_train.shape[1:]),
    tf.keras.layers.Dense(50, activation='softmax'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss=tf.keras.losses.BinaryCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), metrics=['acc'])
history = model.fit(x_train, y_train, epochs=500, validation_data=(x_test, y_test))

model.save("model/save")

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

print("Training accuracy: {:.5f}".format(np.mean(acc)))
print("Validation accuracy: {:.5f}".format(np.mean(val_acc)))

epochs = range(1, len(acc) + 1)
plt.plot(epochs, loss, label="Loss")
plt.plot(epochs, val_loss, label="Val. loss")
plt.legend()
plt.show()

