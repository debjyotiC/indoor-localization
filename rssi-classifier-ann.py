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
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), metrics=['acc'])
history = model.fit(x_train, y_train, epochs=400, validation_data=(x_test, y_test))

model.save("model/save")

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

print("Training accuracy: {:.5f}".format(np.mean(acc)))
print("Validation accuracy: {:.5f}".format(np.mean(val_acc)))

epochs = range(1, len(acc) + 1)

fig, axs = plt.subplots(2, 1)
# plot loss
axs[0].plot(epochs, loss, color='Green', label="Loss")
axs[0].plot(epochs, val_loss, color='Red', label="Val. loss")
axs[0].legend()
axs[0].set_xlabel('Epoch')
axs[0].set_ylabel('Loss')
axs[0].grid(True)

# plot accuracy
axs[1].plot(epochs, acc, color='Green', label="Acc.")
axs[1].plot(epochs, val_acc, color='Red', label="Val Acc.")
axs[1].legend()
axs[1].set_xlabel('Epoch')
axs[1].set_ylabel('Accuracy')
axs[1].grid(True)

plt.show()


