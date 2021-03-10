import data_manager as dm
import data_generator as dg
import matplotlib.pyplot as plt
import numpy as np


def plot_theoretical_rssi():
    rssi = []
    freqs = np.array(dm.channels) * 10**6
    for freq in freqs:
        rssi.append(dg.calc_rssi(freq, 1))

    plt.scatter(freqs, rssi)
    plt.show()