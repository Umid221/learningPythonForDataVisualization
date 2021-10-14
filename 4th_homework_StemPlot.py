import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 41)
y = np.tan(np.cos(x))
# print( x)

# x = range(0, 10, 1)
# y = range(0, 20, 2)
plt.stem(x, y)
plt.show()