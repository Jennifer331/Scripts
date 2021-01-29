import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2)
# method 4
# fig, axs = plt.subplots(2, constrained_layout=True)
axs[0].plot(x, y1)
axs[0].set_title('Sin')
axs[1].plot(x, y2)
axs[1].set_title('Cos')

# method 1
# fig.tight_layout()
# method 2
# plt.subplots_adjust(
#     left=0.123,
#     bottom=0.1,
#     right=0.9,
#     top=0.9,
#     wspace=0.2,
#     hspace=0.35)
# method 3
# plt.subplot_tool()
plt.show()
