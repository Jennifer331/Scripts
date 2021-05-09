import glob, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder_clean = 'D:\\Atom\\python\\data\\cleaned\\grill\\final'

p_f = pd.read_csv(os.path.join(folder_clean, 'd10_water_f_kde.csv'))
p_t2 = pd.read_csv(os.path.join(folder_clean, 'd10_water_t2_kde.csv'))
p_t1 = pd.read_csv(os.path.join(folder_clean, 'd10_water_t1_kde.csv'))
p_t = pd.read_csv(os.path.join(folder_clean, 'd10_water_t_kde.csv'))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(np.unwrap(p_f['PHASE']) - np.unwrap(p_t2['PHASE']), p_f['RSSI'] - p_t2['RSSI'], p_f['CHANNEL'])
ax.scatter(np.unwrap(p_f['PHASE']) - np.unwrap(p_t1['PHASE']), p_f['RSSI'] - p_t1['RSSI'], p_f['CHANNEL'])
ax.scatter(np.unwrap(p_f['PHASE']) - np.unwrap(p_t['PHASE']), p_f['RSSI'] - p_t['RSSI'], p_f['CHANNEL'])

ax.set_xlabel('phase diff')
ax.set_ylabel('rssi diff')
ax.set_zlabel('channel')
plt.show()
