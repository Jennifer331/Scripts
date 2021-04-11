import glob, os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import re
import seaborn as sns

import data_manager as dm
import clean_data as cleaner


folder_clean = 'D:\\Atom\\python\\data\\cleaned\\grill\\final'


def feature():
    matls = ['greentea', 'moli', 'wulong', 'water', 'vinegar', 'milk', 'oil', 'liquor', 'yogurt', 'colanosugar', 'cola']
    # matls = ['water', 'vinegar', 'milk', 'liquor']
    # matls = ['water', 'vinegar', 'oil']
    # matls = ['d1_greentea', 'd1_moli', 'd1_wulong', 'd1_water', 'd1_vinegar', 'd1_milk', 'd1_oil', 'd1_liquor',
    #          'd1_yogurt', 'd1_colanosugar', 'd1_cola', 'd3_water', 'd3_vinegar', 'd3_milk', 'd3_liquor']
    # matls = ['d1_water', 'd1_vinegar', 'd1_milk', 'd1_liquor', 'd3_water', 'd3_vinegar', 'd3_milk', 'd3_liquor']
    # matls_label = ['d1_water', '', 'd1_vinegar', '', 'd1_milk', '', 'd1_liquor', '', 'd3_water', '', 'd3_vinegar', '',
    #                'd3_milk', '', 'd3_liquor']
    colors = sns.color_palette(n_colors=len(matls))
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.set_prop_cycle('color', colors)

    i = 0
    for matl in matls:
        df_f = pd.read_csv(os.path.join(folder_clean, 'd1_%s_f_kde.csv' % matl))
        df_t = pd.read_csv(os.path.join(folder_clean, 'd1_%s_t_kde.csv' % matl))
        diff_r = df_f['RSSI'] - df_t['RSSI']
        diff_p = np.unwrap(df_f['PHASE']) - np.unwrap(df_t['PHASE'])
        # ax.scatter(diff_r, diff_p, df_f['CHANNEL'], c=colors[i])
        # plt.scatter(df_f['CHANNEL'], np.unwrap(df_f['PHASE']), c=colors[i])
        # plt.scatter(df_t['CHANNEL'], np.unwrap(df_t['PHASE']), marker='^', c=colors[i])
        i += 1

    # ax.invert_xaxis()
    plt.legend(matls)
    plt.xlabel('RSSI diff')
    plt.ylabel('phase diff')
    plt.show()


feature()