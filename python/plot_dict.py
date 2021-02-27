import numpy as np
import math
import matplotlib.pyplot as plt

d = {'RSSI': {}, 'Phase': {}}

for channel in np.arange(902.75, 927.25, 0.5):
    d['RSSI'][channel] = -50 * np.random.random()
    d['Phase'][channel] = math.tau * np.random.random()

rssi = sorted(d['RSSI'].items())
x, y = zip(*rssi)
plt.subplot(211)
plt.plot(x, y)

phase = sorted(d['Phase'].items())
x, y = zip(*phase)
plt.subplot(212)
plt.plot(x, y)

plt.show()
