import math
import numpy as np
import pandas as pd

import data_manager as dm


def unfold_acc_dist(data, res):
    col_dist_index = data.columns.get_loc('DISTANCE')
    col_freq_index = data.columns.get_loc('CHANNEL')
    col_phase_index = data.columns.get_loc('PHASE')

    for i in range(1, len(data)):
        d_delta = data.iloc[i][col_dist_index] - data.iloc[i - 1][col_dist_index]
        p_delta = data.iloc[i][col_phase_index] - data.iloc[i - 1][col_phase_index]
        wavelength_max = 0.33
        p_thred = 2*d_delta*math.tau / wavelength_max
        k = round((p_delta+p_thred) / math.tau)

        data.iloc[i, col_phase_index] -= k * math.tau

    for index, row in data.iterrows():
        res.loc[(res['CHANNEL'] == row['CHANNEL']) & (res['DISTANCE'] == row['DISTANCE']), 'PHASE'] = row['PHASE']


def unfold_numpy(data, res):
    data['PHASE'] = np.unwrap(2 * data['PHASE'].values) / 2
    for index, row in data.iterrows():
        res.loc[(res['CHANNEL'] == row['CHANNEL']) & (res['DISTANCE'] == row['DISTANCE']), 'PHASE'] = row['PHASE']


def unfold(df):
    df = df.sort_values(['DISTANCE', 'CHANNEL'])

    dists = sorted(df['DISTANCE'].unique())
    freqs = sorted(df['CHANNEL'].unique())

    g_f0 = df.groupby('CHANNEL').get_group(freqs[0]).copy()
    unfold_acc_dist(g_f0, df)

    li = []
    for name, group in df.groupby('DISTANCE'):
        p = np.unwrap(2 * group['PHASE'].values) / 2
        group = group.copy()
        group.loc[:, 'PHASE'] = p
        li.append(group)

    return pd.concat(li)


def unfold1(df):
    df = df.sort_values(['DISTANCE', 'CHANNEL'])

    dists = sorted(df['DISTANCE'].unique())
    freqs = sorted(df['CHANNEL'].unique())

    g_d0 = df.groupby('DISTANCE').get_group(dists[0]).copy()
    unfold_numpy(g_d0, df)

    for name, group in df.groupby('CHANNEL'):
        unfold_acc_dist(group.copy(), df)

    return df


if __name__ == '__main__':
    # for file in dm.clean_files:
    #     df = dm.import_clean_data(file + '.csv', convert=True)
    #     df = unfold(df)
    #     df['DISTANCE'] *= 100
    #     df['CHANNEL'] /= 10**6
    #     dm.to_csv(df, dm.folder_clean, file + '_2d_unwrap.csv')
    #     dm.export_mat(df, file + '_2d_unwrap.mat')

    df = pd.read_csv("D:\\Atom\\python\\data\\cleaned\\mr\\mr_water_kde.csv")
    df['DISTANCE'] /= 100
    df['CHANNEL'] *= 10**6
    df = unfold1(df)
    df['DISTANCE'] *= 100
    df['CHANNEL'] /= 10 ** 6
    dm.export_mat(df, 'D:\\Atom\\python\\data\\cleaned\\mr\\test.mat')

