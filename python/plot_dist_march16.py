import importlib
import matplotlib.pyplot as plt
import numpy as np

from time import *

import data_manager as dm
import rfid_liquid_classification as classifier

import sys
sys.path.extend(['d:\\atom\\python'])


df_test = dm.import_static_test_data(dm.folder_open_test, 'open_test_data_static.csv')
tmplts = dm.get_templates()
matls = list(tmplts.keys())
shape_tmplts = [4, 120]


##
def plot_dist(matl='empty', position=130):

    df_test_matl = df_test.groupby('MATERIAL').get_group(matl)
    df_test_matl_p = df_test_matl.groupby('DISTANCE').get_group(position)

    corr = classifier.pos_coor(df_test_matl_p, tmplts, shape_tmplts)
    plt.figure(1)
    plt.plot(corr.T)
    plt.legend([1, 2, 3, 4])
    plt.suptitle('%s-%d' % (matl, position))

    d_rssi = np.full(shape_tmplts, 0)
    d_phase = np.full(shape_tmplts, 0)

    for index, row in df_test_matl_p.iterrows():
        d_r, d_p = classifier.distance_by_position(row['RSSI'], row['PHASE'], row['CHANNEL'], tmplts, shape_tmplts)
        d_rssi = np.add(d_rssi, d_r)
        d_phase = np.add(d_phase, d_p)

    d = np.add(d_rssi, d_phase)

    fig, ax = plt.subplots(1, 4)
    plt.suptitle('%s-%d' % (matl, position))
    for i in range(4):
        ax[i].plot(d_rssi[i], label='d_rssi', alpha=0.5)
        ax[i].plot(d_phase[i], label='d_phase', alpha=0.5)
        ax[i].plot(d[i], label='d')
        ax[i].set_title(matls[i])
        ax[i].legend()
    plt.legend()
    plt.show()


plot_dist('vinegar', 61)
