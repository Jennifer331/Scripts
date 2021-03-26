import matplotlib.pyplot as plt
import os
import pandas as pd
import sys

import data_manager as dm

df = dm.import_clean_data('nongfu_empty.csv', folder=dm.folder_clean)
df = df.groupby('DISTANCE').get_group(32)
df.sort_values(by=['CHANNEL'])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['axes.spines.right'] = False
# plt.rcParams['axes.spines.top'] = False

golden_ratio = (5**.5 - 1) / 2
w = 426.79135/72.27
h = w * golden_ratio

fig = plt.figure(figsize=(w, h))
ax1 = fig.add_subplot(121, xlabel='频率', ylabel='接收信号强度')
ax1.scatter(df['CHANNEL'], df['RSSI'])
ax2 = fig.add_subplot(122, xlabel='频率', ylabel='相位')
ax2.scatter(df['CHANNEL'], df['PHASE'])

fig.savefig('d:\\atom\\python\\plot\\change_with_freq.pdf', format='pdf', bbox_inches='tight')
