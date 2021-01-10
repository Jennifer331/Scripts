import collections
import csv
import numpy as np
from matplotlib import pyplot as plt
filename = 'D:\\Atom\\Dependency\\tens.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    records = collections.defaultdict(dict)
    for row in reader:
        epc = row[1]
        channel = float(row[0])
        phase = float(row[2])
        rssi = float(row[3])
        records[epc].setdefault(channel, []).append([phase, rssi])

    for epc in records.keys():
        rgb = np.random.rand(3,)
        x = []
        y = []
        for channel in records[epc].keys():
            data = np.array(records[epc][channel])[:,0]
            x.extend([channel] * len(data))
            y.extend(data)
        plt.scatter(x, y, c=np.array([rgb]), label=epc)

    plt.legend(loc="upper right")
    plt.show()
