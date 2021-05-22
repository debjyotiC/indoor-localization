import tensorflow as tf

# also save as TF-lite
converter = tf.lite.TFLiteConverter.from_saved_model('model/save')
lite_model = converter.convert()
open("model/rssi-model.tflite", "wb").write(lite_model)