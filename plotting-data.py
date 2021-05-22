from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

data = np.load('data/rssi.npz', allow_pickle=True)  # load MFCCs
rssi_x, rssi_y = data['out_x'], data['out_y']  # load into np arrays

X, Y, Z = [], [], []

for elements in enumerate(rssi_x):
    count, element = elements
    X.append(element[0])
    Y.append(element[1])
    Z.append(element[2])

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
