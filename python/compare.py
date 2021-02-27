import glob, os
import math
import matplotlib.pyplot as plt
import pandas as pd
from util import color_names


color_d = {}
epc = '3008 33B2 DDD9 0140 0000 0000'
marker_size = 3


def import_data():
    folder = 'd:\\Atom\\exp\\20210225'
    data = {}
    for file in glob.glob(os.path.join(folder, '60cm_tag_substrate_empty_[0-9]cm.csv')):
        key = file[-7:-4]
        if key not in color_d:
            color_d[key] = color_names[len(color_d)]

        df = pd.read_csv(file, usecols=['CHANNEL', 'EPC', 'PHASE', 'RSSI'])
        df_filtered = df.groupby('EPC').get_group(epc).drop(columns=['EPC'])
        data[key] = df_filtered
    return data


def plot_on_same_axes(d):
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    for key in d:
        ax1.scatter(d[key]['CHANNEL'], d[key]['RSSI'], s=marker_size, color=color_d[key], alpha=0.6)
        ax2.scatter(d[key]['CHANNEL'], d[key]['PHASE'], s=marker_size, color=color_d[key], alpha=0.5, label=key)

    ax2.legend(bbox_to_anchor=(0.98, 1.0), loc='upper left', borderaxespad=0.)
    plt.show()


fake_d = {'12cm': {'CHANNEL': [902.75, 927.25], 'RSSI': [34.2, 34.9]},
          '13cm': {'CHANNEL': [902.75, 927.25], 'RSSI': [45.2, 34.2]}}

d = import_data()
plot_on_same_axes(d)
