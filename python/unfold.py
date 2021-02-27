import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.mod(2*x, 2*np.pi)
y[30] -= np.pi

plt.subplot(311)
plt.scatter(x, y)

plt.subplot(312)
plt.scatter(x, 2*y)

plt.subplot(313)
plt.scatter(x, np.unwrap(2*y, np.pi)/2)
plt.show()

