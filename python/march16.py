import importlib
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.extend(['d:\\atom\\python'])
import data_manager as dm
import rfid_liquid_classification as classifier


##
# importlib.reload(dm)
def worker():
    df = dm.import_static_test_data(dm.folder_open_test, 'open_test_data_static.csv')
    t = dm.get_templates()
    liquid = 'empty'
    distance = 71

    df_water = df.groupby('MATERIAL').get_group(liquid)
    df_water_61 = df_water.groupby('DISTANCE').get_group(distance)
    keys = list(t.keys())

    d_rssi = np.full([4, 120], 0)
    d_phase = np.full([4, 120], 0)

    for i in range(len(df_water_61)):
        s = df_water_61.iloc[i]
        d_r, d_p = classifier.distance_by_position(s['RSSI'], s['PHASE'], s['CHANNEL'], t)
        d_rssi = np.add(d_rssi, d_r)
        d_phase = np.add(d_phase, d_p)

    d = np.add(d_rssi, d_phase)

    fig, ax = plt.subplots(1, 4)
    plt.suptitle('%s-%d' % (liquid, distance))
    for i in range(4):
        ax[i].plot(d_rssi[i], label='d_rssi', alpha=0.5)
        ax[i].plot(d_phase[i], label='d_phase', alpha=0.5)
        ax[i].plot(d[i], label='d')
        ax[i].set_title(keys[i])
        ax[i].legend()
    plt.show()

##
df = dm.import_static_test_data(dm.folder_open_test, 'open_test_data_static.csv')
t = dm.get_templates()

##
from time import *

t1 = time()

for matl, group in df.groupby('MATERIAL'):
    for dist, group2 in group.groupby('DISTANCE'):
        group2 = group2.sort_values(by=['CHANNEL'])
        # group2['RSSI'].values
        channel_list = np.rint((group2['CHANNEL'].values-902.75) / 0.5).astype(int)
        for matl_t in t:
            df_matl = t[matl_t]
            for dist_t, group3 in df_matl.groupby('DISTANCE'):
                matl_rssi_list = group3['RSSI'].values
                rssi_s = matl_rssi_list[channel_list]

t2 = time()
print('see ya: %s passed!' % (t2 - t1))
