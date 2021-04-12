import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

folder_clean = 'D:\\Atom\\python\\data\\cleaned\\grill\\final'

colors = ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan",
          "magenta"]
matls = ['water', 'vinegar', 'milk', 'yogurt', 'oil', 'liquor']
ds = [7, 6, 6, 6, 6, 6]
# matls = ['water', 'vinegar', 'oil']
# ds = [7, 6, 6]
# matls = ['greentea', 'moli', 'wulong', 'water', 'vinegar', 'milk', 'oil', 'liquor', 'yogurt', 'colanosugar', 'cola']
d_p = []
d_r = []
f = []
y = []
j = 0
for d, matl in zip(ds, matls):
    df_f = pd.read_csv(os.path.join(folder_clean, 'd%d_%s_f_kde.csv' % (d, matl)))
    df_t = pd.read_csv(os.path.join(folder_clean, 'd%d_%s_t_kde.csv' % (d, matl)))
    diff_p = np.unwrap(df_f['PHASE']) - np.unwrap(df_t['PHASE'])
    diff_r = df_f['RSSI'] - df_t['RSSI']

    d_p.extend(diff_p)
    d_r.extend(diff_r)
    f.extend(df_f['CHANNEL'].values)
    y.extend(np.repeat([matl], len(diff_p)))
    plt.scatter(diff_p, diff_r, c=colors[j])

    for i in range(len(diff_p)):
        if diff_p[i] < 0:
            diff_p[i] += 2 * np.pi
        else:
            diff_p[i] -= 2 * np.pi

    d_p.extend(diff_p)
    d_r.extend(diff_r)
    f.extend(df_f['CHANNEL'].values)
    y.extend(np.repeat([matl], len(diff_p)))
    plt.scatter(diff_p, diff_r, c=colors[j])

    j += 1
plt.legend(['water', 'water', 'vinegar', 'vinegar', 'milk','milk', 'yogurt', 'yogurt', 'oil',  'oil', 'liquor', 'liquor'])
# plt.legend(matls)
plt.show()
