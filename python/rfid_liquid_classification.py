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