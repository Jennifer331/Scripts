from collections import defaultdict
import numpy as np
import pandas as pd


w_r = 1
w_p = 1


def import_templates():
    return pd.DataFrame()


def distance(r1, p1, r2, p2):
    return w_r*np.sum((r1-r2)**2) + w_p*np.sum((p1-p2)**2)


def dist_to_any(r1, p1, templates):
    d = np.full(len(templates), np.Inf)
    i = -1
    for matl in templates:
        i += 1
        for name, group in templates[matl].groupby('DISTANCE'):
            t = group.sort_values(by=['CHANNEL'])
            d[i] = min(d[i], distance(r1, p1, t['RSSI'].values, t['PHASE'].values))
    return d


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


if __name__ == '__main__':
    templates = import_templates()


##
def distance_by_position(r1, p1, c1, templates):
    i = -1
    d_p = np.full([4, 120], np.Inf)
    d_r = np.full([4, 120], np.Inf)
    for matl in templates:
        try:
            i += 1
            df = templates[matl]
            df = df[df['CHANNEL'] == c1]
            # d_p[i] = min(d_p[i], np.min(np.mod(df['PHASE']-p1, 2*np.pi)**2))
            # d_p_array = (np.mod(df['PHASE'].values, 2*np.pi)-p1)**2
            d_p_array1 = np.mod(df['PHASE'].values - p1, 2*np.pi)
            d_p_array = np.fmin(d_p_array1, 2*np.pi - d_p_array1)**2

            d_r_array = (df['RSSI'].values-r1)**2
            d_array = w_p*d_p_array+w_r*d_r_array
            d_p[i,:] = d_p_array
            d_r[i,:] = d_r_array
            # d_p[i] = min(d_p[i], np.min((np.mod(df['PHASE'], 2*np.pi)-p1)**2))
            # d_r[i] = min(d_r[i], np.min((df['RSSI']-r1)**2))
        except KeyError:
            print(str(i))
            raise
    return d_r, d_p