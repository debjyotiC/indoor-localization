import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

data = np.load('data/rssi.npz', allow_pickle=True)  # load MFCCs
x, y = data['out_x'], data['out_y']  # load into np arrays

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=False, test_size=0.4)

data_select = 3
data_select_x = x_train[data_select]
data_select_y = y_train[data_select]

in_tensor = np.float32([data_select_x])

# load Keras model
load_model = tf.keras.models.load_model('model/save')
classes = load_model.predict(in_tensor)[0][0]

if classes > 0.5:
    print("other room", classes, data_select_y)
else:
    print("my room", classes, data_select_y)
