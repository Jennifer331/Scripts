import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fake_rssi = np.random.rand(100)
fake_rssi = fake_rssi*20 - 60

fake_phase = np.random.rand(100)
fake_phase = fake_phase*2*np.pi

# print(fake_rssi)
# print(fake_phase)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('RFID Readings')

x = list(range(1, 101))

ax1.set_ylabel('RSSI')
line1, = ax1.plot(x[:20], fake_rssi[:20], 'o-')
line1.axes.set_xlim(0, 20)

ax2.set_ylabel('PHASE')
line2, = ax2.plot(x[:20], fake_phase[:20], '.-')
line2.axes.set_xlim(0, 20)


def animate(i):
    if i >= 80:
        return
    line1.set_data(x[i:20+i], fake_rssi[i:20+i])
    line2.set_data(x[i:20+i], fake_phase[i:20+i])
    line1.axes.set_xlim(i, 20+i)
    line2.axes.set_xlim(i, 20+i)
    return line1, line2


ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
