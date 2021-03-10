import glob
import numpy as np
import os
import pandas as pd
import re

import data_manager as dm
import clean_data as cleaner
import unfold


def clean_mr(liquid='water'):
    folder_in = dm.folder_mr
    folder_out = dm.folder_clean_mr
    filename = 'mr_%s_[0-9]*cm.csv' % liquid
    pattern = '\d*cm'
    epc = dm.epc_liquid

    li = []
    for file in glob.glob(os.path.join(folder_in, filename)):
        dis_sub_str = re.search(pattern, file).group(0)
        dis = ''.join([n for n in dis_sub_str if n.isdigit()])
        try:
            df = pd.read_csv(file).groupby('EPC').get_group(epc).drop(columns=['EPC'])
            df = cleaner.kde_peak(df)
            df.insert(0, 'DISTANCE', int(dis))
            li.append(df)
        except KeyError:
            print('read file' + file + ' raise KeyError')

    df = pd.concat(li)
    dm.to_csv(df, folder_out, 'mr_%s_kde.csv' % liquid)
    dm.export_mat(df, 'mr_%s_kde.mat' % liquid, folder=folder_out)


def unwrap(liquid='water'):
    df = dm.import_clean_data('mr_' + liquid + '_kde.csv', folder=dm.folder_clean_mr, convert=True)
    df_unwrap = unfold.unfold(df)
    df_unwrap['DISTANCE'] *= 100
    df_unwrap['CHANNEL'] /= 10**6
    dm.to_csv(df_unwrap, dm.folder_clean_mr, 'mr_%s_2d_cus_unwrap.csv' % liquid)
    dm.export_mat(df_unwrap, 'mr_%s_2d_cus_unwrap.mat' % liquid, folder=dm.folder_clean_mr)


if __name__ == '__main__':
    liquids = ['empty', 'water', 'ant_water', 'p_water', 'water2', 'oil', 'vinegar']
    for liquid in liquids:
        clean_mr(liquid)
        unwrap(liquid)
    unwrap()


