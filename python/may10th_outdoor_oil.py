import glob, os
import pickle

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data_manager as dm

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

folder = 'D:\\Atom\\python\\data\\cleaned\\outdoor'
front = pd.read_csv(os.path.join(folder, 'outdoor_oil_kde.csv'))
tail = pd.read_csv(os.path.join(folder, 'outdoor_oil_tail_kde.csv'))

ds = sorted(list(set(front['DISTANCE'].unique()) & set(tail['DISTANCE'].unique())))

df_f_g = front.groupby('DISTANCE')
df_t_g = tail.groupby('DISTANCE')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for d in ds:
    df_h = df_f_g.get_group(d)
    df_t = df_t_g.get_group(d)

    freqs = df_h['CHANNEL'].values
    df_h = df_h.set_index('CHANNEL')
    df_t = df_t.set_index('CHANNEL')

    phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
    #     rssi_diff = df_h['RSSI'].values - df_t['RSSI'].values
    rssi_diff = df_h['RSSI'] - df_t['RSSI']
    phase_diff[phase_diff < 0] += 2 * np.pi
    ax.scatter(phase_diff, rssi_diff, freqs)

features = dm.get_features()
ax.scatter(features['oil'][0], features['oil'][1], freqs)
# ax.scatter(features['vinegar'][0], features['vinegar'][1], freqs)
# ax.scatter(features['water'][0], features['water'][1], freqs)
# ax.scatter(features['empty'][0], features['empty'][1], freqs)
# plt.legend(ds + ['标准', '醋', '水', '空瓶'])
ax.set_xlabel('phase diff')
ax.set_ylabel('rssi diff')
ax.set_zlabel('channel')
plt.legend(ds + ['标准'])
plt.show()