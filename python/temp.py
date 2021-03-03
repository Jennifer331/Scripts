import glob
import math
import matplotlib.pyplot as plt
import numpy as np
import operator
import os
import pandas as pd
import re
from scipy import constants
from scipy.optimize import curve_fit

import clean_data
import io_helper


folder_test = 'd:\\Atom\\python\\test_data\\empty'
folder_raw = "d:\\Atom\\exp\\20210202"
folder_clean = 'd:\\Atom\\python\\data\\cleaned'
file_test = 'empty_test.csv'
file_clean_wrap = 'white_empty_wrap.csv'
file_clean_unwrap = 'white_empty_unwrap.csv'


def import_test_data():
    df = pd.read_csv(os.path.join(folder_test, file_test))
    df['CHANNEL'] *= 10**6
    return df


def import_clean_data():
    df = pd.read_csv(os.path.join(folder_clean, file_clean_wrap))
    df['DISTANCE'] /= 100
    df['CHANNEL'] *= 10**6
    return df


def phase_func(X, a, b, c, d):
    freq, dist = X
    wavelength = constants.speed_of_light / freq
    return (a*dist/wavelength + b*wavelength + c*dist + d) % math.tau


def fit():
    df = import_test_data()
    # df = import_clean_data()
    popt, pcov = curve_fit(phase_func, (df['CHANNEL'], df['DISTANCE']), df['PHASE'], p0=[-2*math.tau, 0, 0, 0])
    print(popt)
    print(pcov)


def plot_theoretical_diff():
    df = import_test_data()
    grouped = df.groupby('DISTANCE')
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    last_group = None
    old_name = None
    for name, group in grouped:
        if last_group is None:
            last_group = group
            old_name = name
            continue
        ax1.set_title(str(name) + '-' + str(old_name))
        ax1.scatter(group['CHANNEL'], list(map(operator.sub, list(group['PHASE']), list(last_group['PHASE']))))
        ax2.scatter(group['CHANNEL'], list(map(operator.sub, list(group['RSSI']), list(last_group['RSSI']))))
        last_group = group
        old_name = name
    plt.show()


def plot():
    df = pd.read_csv(os.path.join(folder_clean, file_clean_unwrap))
    grouped = df.groupby('CHANNEL')
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    for name, group in grouped:
        ax1.scatter(group['DISTANCE'], group['PHASE'])
        ax2.scatter(group['DISTANCE'], group['RSSI'])

    plt.show()


def plot_3d():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    df = pd.read_csv(os.path.join(folder_test, file_test))
    ax.scatter(df['CHANNEL'], df['DISTANCE'], df['PHASE'], label='test')

    # df = pd.read_csv(os.path.join(folder_clean, file_clean_wrap))
    # ax.scatter(df['CHANNEL'], df['DISTANCE'], df['PHASE'], label='clean')

    ax.legend()
    plt.show()


def clean_white_empty():
    epc = "E280 1160 6000 0207 A652 516D"
    pattern = "_\d{4}cm"
    li = []
    for file in glob.glob(os.path.join(folder_raw, "*.csv")):
        if not file.endswith('cm.csv'):
            continue
        dis_sub_str = re.search(pattern, file).group(0)
        dis = ''.join([n for n in dis_sub_str if n.isdigit()])
        try:
            df = pd.read_csv(file).groupby('EPC').get_group(epc).drop(columns=['EPC'])
            df = clean_data.kde_peak(df, unwrap=True)
            df.insert(0, 'DISTANCE', int(dis) - 10)
            li.append(df)
        except KeyError:
            print('read file ' + file + ' raise KeyError')
    df = pd.concat(li)

    io_helper.to_csv(df, folder_clean, file_clean_unwrap)


if __name__ == '__main__':
    # plot()
    # plot_3d()
    # fit()
    # clean_white_empty()
    plot_theoretical_diff()