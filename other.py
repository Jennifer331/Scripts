import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(1)
line, = ax.plot(x, np.sin(x))
line.axes.set_xlim(0, 2*np.pi)


def animate(i):
    global x
    x = np.append(x, x[-1] + 0.05)
    line.set_data(x, np.sin(x))
    line.axes.set_ylim(np.amin(np.sin(x)), np.amax(np.sin(x)))
    if x[-1] > 2*np.pi:
        line.axes.set_xlim(x[-1]-2*np.pi, x[-1])
    return line,


ani = animation.FuncAnimation(fig, animate, interval=1, blit=False, save_count=50)
plt.show()
