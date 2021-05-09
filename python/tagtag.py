import os, glob
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

folder_clean = 'D:\\Atom\\python\\data\\cleaned\\open'
df_water = pd.read_csv(os.path.join(folder_clean, 'open_empty_kde.csv'))


def extract_feature(p1, r1, p2, r2):
    t = 10 ** ((r1 - r2) / 40)
    feature = np.empty(50)
    feature.fill(np.nan)
    for k1 in range(13):
        for k2 in (k1, k1 + 1):
            phi_m = (2*np.pi*(t*k1-k2) + (t*p1-p2))/(t - 1)
            mark = (phi_m >= 0) & (phi_m <= 2*np.pi)
            feature[mark] = phi_m[mark]
            # print(k1, k2, t, m)
            # plt.plot(m)
    plt.plot(feature)
    # plt.scatter(range(50), feature)


dists = df_water['DISTANCE'].unique()

m, n = 10, 20
for d1, d2 in zip(dists[m:n], dists[m+1:n+1]):
    df_water1 = df_water.groupby('DISTANCE').get_group(d1)
    df_water2 = df_water.groupby('DISTANCE').get_group(d2)

    extract_feature(df_water1['PHASE'].values, df_water1['RSSI'].values, df_water2['PHASE'].values, df_water2['RSSI'].values)

plt.legend(dists[m:n])
plt.show()