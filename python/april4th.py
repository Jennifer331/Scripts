import data_manager as dm
import clean_data

import glob
import os
import re
import pandas as pd
import numpy as np

folder = 'D:\\Atom\\exp\\20210403'
folder_clean = 'd:\\Atom\\python\\data\\cleaned\\outdoor\\front-tail'

f_file = '%s_%s_[0-9]*cm.csv'
matls = ['oil', 'water', 'vinegar', 'empty']
sides = ['f', 't']


def rename_file():
    for file in glob.glob(os.path.join(folder, '*.csv')):
        s = re.search('_[0-9]{2}cm', file)
        if s:
            i = s.span()[0]
            file1 = file[:i+1] + '0' + file[i+1:]
            os.rename(file, file1)


def kde():
    for side in ['f', 't']:
        for matl in matls:
            clean_data.clean_merge_dists(folder, f_file % (side, matl), dm.epc[matl], folder_clean, 'outdoor_all_%s_%s' % (side, matl))


def unwrap():
    for side in ['f', 't']:
        for matl in matls:
            clean_data.unwrap(folder_clean, 'outdoor_all_%s_%s_kde.csv' % (side, matl), folder_clean, 'outdoor_all_%s_%s' % (side, matl))


def align():
    for matl in matls:
        df_f = pd.read_csv('D:\\Atom\\python\\data\\cleaned\\outdoor\\front-tail\\outdoor_all_f_%s_unwrap.csv' % matl)
        df_t = pd.read_csv('D:\\Atom\\python\\data\\cleaned\\outdoor\\front-tail\\outdoor_all_t_%s_unwrap.csv' % matl)

        dists = np.unique(np.concatenate((df_f['DISTANCE'].unique(), df_f['DISTANCE'].unique())))
        fs = np.unique(np.concatenate((df_t['CHANNEL'].unique(), df_t['CHANNEL'].unique())))

        combined = [dists, fs]
        cols = ['DISTANCE', 'CHANNEL']

        cross_prod = pd.MultiIndex.from_product(combined, names=cols)
        appended_f = df_f.set_index(cols).reindex(cross_prod, fill_value=np.nan).reset_index()
        appended_t = df_t.set_index(cols).reindex(cross_prod, fill_value=np.nan).reset_index()

        index = (~np.isnan(appended_f['RSSI'])) & (~np.isnan(appended_t['RSSI']))

        filtered_f = appended_f[index]
        filtered_t = appended_t[index]

        folder = 'D:\\Atom\\python\\data\\cleaned\\outdoor\\front-tail'
        dm.to_csv(filtered_f, folder, 'outdoor_all_f_%s_aligned.csv' % matl)
        dm.export_mat(filtered_f, 'outdoor_all_f_%s_aligned.mat' % matl, folder=folder)

        dm.to_csv(filtered_t, folder, 'outdoor_all_t_%s_aligned.csv' % matl)
        dm.export_mat(filtered_t, 'outdoor_all_t_%s_aligned.mat' % matl, folder=folder)
