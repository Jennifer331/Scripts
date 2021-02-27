import matplotlib.pyplot as plt

plt.figure(2)
ax2 = plt.subplot(2, 1, 1)
plt.figure(1)
ax1 = plt.subplot(2, 1, 2)

ax2.scatter([1, 2, 3], [1, 4, 6])
ax1.scatter([1, 2, 3], [1, 2, 3])

plt.show()
