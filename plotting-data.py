from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Fixing random state for reproducibility
np.random.seed(19680801)

X = []
Y = []
Z = []
C = []
rssi_x = [[-75, -54, -58], [-72, -58, -58], [-72, -60, -54], [-76, -57, -58], [-72, -58, -58], [-72, -59, -62], [-72, -58, -62],
          [-72, -63, -64], [-72, -57, -63], [-75, -58, -62], [-57, -58, -76], [-56, -57, -72], [-54, -56, -74], [-56, -57, -76],
          [-58, -56, -72], [-56, -58, -72], [-57, -57, -72], [-56, -58, -78],
          [-58, -56, -72], [-56, -62, -76]]
rssi_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for elements in enumerate(rssi_x):
    count, element = elements
    X.append(element[0])
    Y.append(element[1])
    Z.append(element[2])
    if rssi_y[count] == 1:
        C.append('red')
    else:
        C.append('blue')

# split the data

x_0, y_0, z_0 = X[:10], Y[:10], Z[:10]
x_1, y_1, z_1 = X[10:], Y[10:], Z[10:]

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_0, y_0, z_0, color='blue', s=60, label='My room (label 0)')
ax.scatter(x_1, y_1, z_1, color='red', s=60, label='Other room (label 1)')
ax.set_xlabel('Node 1 rssi')
ax.set_ylabel('Node 2 rssi')
ax.set_zlabel('Node 3 rssi')
ax.view_init(30, 185)
plt.legend()
plt.show()
