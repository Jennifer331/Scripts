from collections import defaultdict
import numpy as np
import pandas as pd
from time import *

import data_manager as dm


w_r = 1
w_p = 1


def dist_to_any(r1, p1, c1, templates):
    d_r = np.full(len(templates), np.Inf)
    d_p = np.full(len(templates), np.Inf)
    i = -1
    for matl in templates:
        try:
            i += 1
            df = templates[matl]
            df = df[df['CHANNEL'] == c1]
            # d_p[i] = min(d_p[i], np.min(np.mod(df['PHASE']-p1, 2*np.pi)**2))
            d_p_array = (np.mod(df['PHASE'].values, 2*np.pi)-p1)**2
            d_r_array = (df['RSSI'].values-r1)**2
            d_array = w_p*d_p_array+w_r*d_r_array
            i_min = np.argmin(d_array)
            d_p[i] = d_p_array[i_min]
            d_r[i] = d_r_array[i_min]
            # d_p[i] = min(d_p[i], np.min((np.mod(df['PHASE'], 2*np.pi)-p1)**2))
            # d_r[i] = min(d_r[i], np.min((df['RSSI']-r1)**2))
        except KeyError:
            print(str(i) + str(i_min))
            raise
    return d_r, d_p


def dist_joint_to_any(r1, p1, c1, templates):
    d = np.full(len(templates), np.Inf)
    i = -1
    for matl in templates:
        i += 1
        df = templates[matl]
        df = df[df['CHANNEL'] == c1]
        d[i] = min(d[i], np.min(w_r*((df['RSSI'] - r1)**2) + w_p*(np.mod((df['PHASE'] - p1), 2*np.pi)**2)))
    return d


def distance_by_position(r1, p1, c1, templates, shape_tmplt):
    i = -1
    d_phase = np.full(shape_tmplt, np.Inf)
    d_rssi = np.full(shape_tmplt, np.Inf)
    for matl in templates:
        try:
            i += 1
            df_tmplt = templates[matl]
            df_tmplt_c = df_tmplt[df_tmplt['CHANNEL'] == c1]

            d_p = np.mod(df_tmplt_c['PHASE'].values - p1, 2*np.pi)
            d_p = np.fmin(d_p, 2*np.pi - d_p)**2
            d_r = (df_tmplt_c['RSSI'].values-r1)**2

            d_phase[i, :] = d_p
            d_rssi[i, :] = d_r
        except KeyError:
            print(i)
            raise
    return d_rssi, d_phase


##
def batch_corr():
    t1 = time()

    df_test = dm.import_static_test_data(dm.folder_open_test, 'open_test_data_static.csv')
    tmplts = dm.get_templates()
    matls = list(tmplts.keys())

    for matl_test, g_matl_test in df_test.groupby('MATERIAL'):
        for pos_test, g_pos_test in g_matl_test.groupby('DISTANCE'):
            g_pos_test = g_pos_test.sort_values(by=['CHANNEL'])
            channel_list = ((g_pos_test['CHANNEL'].values-902.75) / 0.5).astype(int)
            rssi_test = g_pos_test['RSSI'].values
            corr = np.full([len(matls), 120], 0.0)
            i = -1
            for matl_tmplt in tmplts:
                i += 1
                j = -1
                df_matl_tmplt = tmplts[matl_tmplt]
                for pos_tmplt, g_pos_tmplt in df_matl_tmplt.groupby('DISTANCE'):
                    j += 1
                    pos_tmplt_c_r_map = g_pos_tmplt['RSSI'].values
                    rssi_tmplt = pos_tmplt_c_r_map[channel_list]
                    corr[i][j] = np.corrcoef(rssi_tmplt, rssi_test)[0, 1]
    print(corr)
    t2 = time()
    print('see ya: %s passed!' % (t2 - t1))


def pos_coor(g_pos_test, templates, shape_tmplt):
    g_pos_test = g_pos_test.sort_values(by=['CHANNEL'])
    channel_list = ((g_pos_test['CHANNEL'].values-902.75) / 0.5).astype(int)
    rssi_test = g_pos_test['RSSI'].values
    corr = np.full(shape_tmplt, 0.0)
    i = -1
    for matl_tmplt in templates:
        i += 1
        j = -1
        df_matl_tmplt = templates[matl_tmplt]
        for pos_tmplt, g_pos_tmplt in df_matl_tmplt.groupby('DISTANCE'):
            j += 1
            pos_tmplt_c_r_map = g_pos_tmplt['RSSI'].values
            rssi_tmplt = pos_tmplt_c_r_map[channel_list]
            corr[i][j] = np.corrcoef(rssi_tmplt, rssi_test)[0, 1]
    return corr