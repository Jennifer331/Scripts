import glob
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import re
from scipy.stats import gaussian_kde

import data_manager as dm
import unfold as unfold_helper


def import_data():
    epc = "E280 1160 6000 0207 A652 516D"
    filename = "d:\\Atom\\exp\\20210202\\exp_0202_0165cm_2.csv"
    df = pd.read_csv(filename)
    df_filtered = df.loc[df['EPC'] == epc]
    df_filtered = df_filtered.drop(columns=['EPC'])
    return df_filtered


def import_data(filename, epc='E280 1160 6000 0207 A652 516D'):
    df = pd.read_csv(filename, usecols=['CHANNEL', 'EPC', 'PHASE', 'RSSI'])
    return df.groupby('EPC').get_group(epc).drop(columns=['EPC']).sort_values(by=['CHANNEL'])


def unfold(df):
    df['CHANNEL'], df['PHASE'] = np.unwrap([df['CHANNEL'], 2 * df['PHASE']], np.pi)
    df['Phase'] /= 2


def kde_peak(df, unwrap=False):
    grouped = df.groupby('CHANNEL')
    channel, rssi, phase = [], [], []
    for name, group in grouped:
        channel.append(name)
        rssi.append(peak(group, 'RSSI'))
        phase.append(peak(group, 'PHASE'))
    if unwrap:
        phase = np.unwrap(phase, np.pi)
        # phase = np.unwrap(2 * phase) / 2
    d = {'CHANNEL': channel, 'RSSI': rssi, 'PHASE': phase}
    return pd.DataFrame(data=d)


def mean(df):
    grouped = df.groupby('CHANNEL')
    channel, rssi, phase = [], [], []
    for name, group in grouped:
        channel.append(name)
        rssi.append(group['RSSI'].mean())
        phase.append(peak(group, 'PHASE'))
    d = {'CHANNEL': channel, 'RSSI': rssi, 'PHASE': phase}
    return pd.DataFrame(data=d)


def peak(group, col):
    variance = group.var()[col]
    if math.isnan(variance) or variance < 1e-08:
        return group[col].iloc[0]
    try:
        density = gaussian_kde(group[col])
    except np.linalg.LinAlgError:
        print(group[col])
        print(group.var()[col])
        raise
    ind = np.linspace(group[col].min(), group[col].max(), 200)
    return ind[np.argsort(density(ind))[-1]]


def clean_merge_dists(folder_i, file, epc, folder_o, label, dist_off=0):
    pattern = '\d*cm'

    li = []
    for file in glob.glob(os.path.join(folder_i, file)):
        dis_sub_str = re.search(pattern, file).group(0)
        dis = ''.join([n for n in dis_sub_str if n.isdigit()])
        try:
            df = pd.read_csv(file).groupby('EPC').get_group(epc).drop(columns=['EPC'])
            df = kde_peak(df)
            df.insert(0, 'DISTANCE', int(dis)+dist_off)
            li.append(df)
        except KeyError:
            print('read file %s raise KeyError' % file)
        except pd.errors.EmptyDataError:
            print('read file %s raise EmptyDataError' % file)
        except:
            print('file ' + file)
            raise

    df = pd.concat(li)
    dm.to_csv(df, folder_o, '%s_kde.csv' % label)
    dm.export_mat(df, '%s_kde.mat' % label, folder=folder_o)


def unwrap(folder_i, file, folder_o, label):
    df = dm.import_clean_data(file, folder=folder_i, convert=True)
    df_unwrap = unfold_helper.unfold(df)
    df_unwrap['DISTANCE'] *= 100
    df_unwrap['CHANNEL'] /= 10**6
    dm.to_csv(df_unwrap, folder_o, '%s_2d_cus_unwrap.csv' % label)
    dm.export_mat(df_unwrap, '%s_2d_cus_unwrap.mat' % label, folder=folder_o)


if __name__ == '__main__':
    data_frame = import_data()
    cleaned = kde_peak(data_frame)
    plt.subplot(211)
    plt.scatter(cleaned['CHANNEL'], cleaned['PHASE'])
    plt.subplot(212)
    plt.ylim(-72.5, -20)
    plt.scatter(cleaned['CHANNEL'], cleaned['RSSI'])
    plt.show()
