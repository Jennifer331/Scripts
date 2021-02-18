import pandas as pd
from numpy.random import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from math import *

freq_cnt = 10
replicate = 5


def fake_date_generator():
    s = '['
    for i in range(freq_cnt):
        for j in range(replicate):
            s += '{"freq": %d, "dist": %d, "val": %.2f},' % (902+i, randint(150), rand())
    s += ']'
    return s


cnt = 100
df = pd.DataFrame(
    {
        "freq": randint(902, 928, cnt),
        "dist": randint(1, 150, cnt),
        "val": rand(cnt),
    }
)

grouped = df.groupby("freq")
cnt = len(grouped)
cols = 5
rows = ceil(cnt/cols)

fig = plt.figure(figsize=(40, 80), constrained_layout=True)
gs = gridspec.GridSpec(rows, cols, figure=fig)

dist_min = min(df['dist'])
dist_max = max(df['dist'])
val_min = min(df['val'])
val_max = max(df['val'])

i = 0
for name, group in grouped:
    ax = fig.add_subplot(gs[i // cols, i % cols])
    ax.set_title(name)
    ax.scatter(group['dist'], group['val'])
    ax.set_xlim(dist_min, dist_max)
    ax.set_ylim(val_min, val_max)
    i += 1

plt.show()
