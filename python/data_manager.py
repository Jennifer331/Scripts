import pandas as pd
import os
from scipy.io import savemat

folder_liquid = 'd:\\Atom\\exp\\20210218'
folder_test = 'd:\\Atom\\python\\test_data\\empty'
folder_clean = 'd:\\Atom\\python\\data\\cleaned'
file_test = 'empty_test.csv'
file_clean_wrap = 'white_empty_wrap.csv'
file_clean_unwrap = 'white_empty_unwrap.csv'
epc_liquid = '3008 33B2 DDD9 0140 0000 0000'

channels = [902.75, 903.25, 903.75, 904.25, 904.75, 905.25, 905.75, 906.25, 906.75, 907.25, 907.75, 908.25, 908.75,
            909.25, 909.75, 910.25, 910.75, 911.25, 911.75, 912.25, 912.75, 913.25, 913.75, 914.25, 914.75, 915.25,
            915.75, 916.25, 916.75, 917.25, 917.75, 918.25, 918.75, 919.25, 919.75, 920.25, 920.75, 921.25, 921.75,
            922.25, 922.75, 923.25, 923.75, 924.25, 924.75, 925.25, 925.75, 926.25, 926.75, 927.25]
dists = [12, 13, 14, 15, 18, 21, 24, 27, 30, 36, 39, 42, 78, 81, 84, 87, 90, 93]

clean_files = ['nongfu_empty', 'nongfu_water', 'nongfu_vinegar', 'nongfu_oil']


def import_test_data(convert=False):
    df = pd.read_csv(os.path.join(folder_test, file_test))
    if convert:
        df['DISTANCE'] /= 100
        df['CHANNEL'] *= 10**6
    return df


def import_clean_data(filename, convert=False):
    df = pd.read_csv(os.path.join(folder_clean, filename))
    if convert:
        df['DISTANCE'] /= 100
        df['CHANNEL'] *= 10**6
    return df


def export_mat(df, filename, folder=folder_clean):
    mat_dict = {}
    for col in df.columns:
        mat_dict[col] = list(df[col])
    savemat(os.path.join(folder, filename), mat_dict)
