import numpy as np
from sklearn.svm import SVC
import esp

rssi_features = np.array([[-31, -38, -33], [-47, -45, -44], [-67, -70, -62], [-76, -73, -69],
                          [-66, -68, -64]])
rssi_label = np.array([1, 2, 3, 4, 5])

while True:
    data = esp.esp_serial()
    rssi_test = np.array([data])

    clf = SVC(kernel='linear')
    clf.fit(rssi_features, rssi_label)
    pred = clf.predict(rssi_test)
    
    if pred == [1]:
        print('My room')
    elif pred == [2]:
        print('Living room')
    elif pred == [3]:
        print('Kitchen')
    elif pred == [4]:
        print('Ma\'s room')
    elif pred == [5]:
        print('Baba\'s room')





