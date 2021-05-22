from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Fixing random state for reproducibility
np.random.seed(19680801)
# Dataset
df = pd.DataFrame({'X': range(1, 101), 'Y': np.random.randn(100) * 15 + range(1, 101),
                   'Z': (np.random.randn(100) * 15 + range(1, 101)) * 2})

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['X'], df['Y'], df['Z'], c='skyblue', s=60)
ax.view_init(30, 185)
plt.show()
