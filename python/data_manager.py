import glob
import os
import pandas as pd
import re
from scipy.io import savemat

folder_liquid = 'd:\\Atom\\exp\\20210218'
folder_test = 'd:\\Atom\\python\\test_data\\empty'
folder_clean = 'd:\\Atom\\python\\data\\cleaned'
folder_clean_mr = 'd:\\Atom\\python\\data\\cleaned\\mr'
folder_clean_open = 'd:\\Atom\\python\\data\\cleaned\\open'
folder_clean_sheet = 'd:\\Atom\\python\\data\\cleaned\\sheet'
folder_mr = 'd:\\Atom\\exp\\20210307'
folder_open = 'd:\\Atom\\exp\\20210313'
folder_open_test = 'D:\\Atom\\python\\data\\test'
folder_templates = 'D:\\Atom\\python\\data\\templates'
folder_log = 'D:\\Atom\\python\\data\\log'
file_test = 'empty_test.csv'
file_clean_wrap = 'white_empty_wrap.csv'
file_clean_unwrap = 'white_empty_unwrap.csv'
file_summary = 'log_summary.csv'

epc = {'liquid': '3008 33B2 DDD9 0140 0000 0000',
       'water': '3008 33B2 DDD9 0140 0000 0020',
       'empty': '3008 33B2 DDD9 0140 0000 0030',
       'oil2': '3008 33B2 DDD9 0140 0000 0040',
       'vinegar': '3008 33B2 DDD9 0140 0000 0060',
       'water2': '3008 33B2 DDD9 0140 0000 0080'}

epc_liquid = '3008 33B2 DDD9 0140 0000 0000'
epc_water = '3008 33B2 DDD9 0140 0000 0020'
epc_empty = '3008 33B2 DDD9 0140 0000 0030'
epc_oil = '3008 33B2 DDD9 0140 0000 0040'
epc_vinegar = '3008 33B2 DDD9 0140 0000 0060'
epc_water2 = '3008 33B2 DDD9 0140 0000 0080'

channels = [902.75, 903.25, 903.75, 904.25, 904.75, 905.25, 905.75, 906.25, 906.75, 907.25, 907.75, 908.25, 908.75,
            909.25, 909.75, 910.25, 910.75, 911.25, 911.75, 912.25, 912.75, 913.25, 913.75, 914.25, 914.75, 915.25,
            915.75, 916.25, 916.75, 917.25, 917.75, 918.25, 918.75, 919.25, 919.75, 920.25, 920.75, 921.25, 921.75,
            922.25, 922.75, 923.25, 923.75, 924.25, 924.75, 925.25, 925.75, 926.25, 926.75, 927.25]
dists = [12, 13, 14, 15, 18, 21, 24, 27, 30, 36, 39, 42, 78, 81, 84, 87, 90, 93]
dists_mr = [2,   8,  14,  20,  26,  32,  38,  44,  50,  56,  62,  68,  74,  80,  86,  92,  98, 104, 110, 116, 122, 128,
             34, 140, 152, 158, 161]

clean_files = ['nongfu_empty', 'nongfu_water', 'nongfu_vinegar', 'nongfu_oil']


def import_static_test_data(folder, filename, convert=False):
    df = pd.read_csv(os.path.join(folder, filename), usecols=['MATERIAL', 'DISTANCE', 'CHANNEL', 'PHASE', 'RSSI'])
    if convert:
        df['DISTANCE'] /= 100
        df['CHANNEL'] *= 10**6
    return df


def import_dynamic_test_data(folder, filename, convert=False):
    df = pd.read_csv(os.path.join(folder, filename), usecols=['MATERIAL', 'CHANNEL', 'PHASE', 'RSSI'])
    if convert:
        df['DISTANCE'] /= 100
        df['CHANNEL'] *= 10**6
    return df


def import_clean_data(filename, folder=folder_clean, convert=False):
    df = pd.read_csv(os.path.join(folder, filename))
    if convert:
        df['DISTANCE'] /= 100
        df['CHANNEL'] *= 10**6
    return df


def import_from_file(filename, epc):
    try:
        df = pd.read_csv(filename, usecols=['CHANNEL', 'EPC', 'PHASE', 'RSSI']).groupby('EPC').get_group(epc)\
            .drop(columns=['EPC']).sort_values(by=['CHANNEL'])
    except KeyError:
        df = pd.DataFrame(columns=['CHANNEL', 'PHASE', 'RSSI'])
    return df


def import_from_folder(folder_i, file, epc, dist_off=0):
    pattern = '\d*cm'

    li = []
    for file in glob.glob(os.path.join(folder_i, file)):
        dis_sub_str = re.search(pattern, file).group(0)
        dis = ''.join([n for n in dis_sub_str if n.isdigit()])
        try:
            df = pd.read_csv(file).groupby('EPC').get_group(epc).drop(columns=['EPC'])
            df.insert(0, 'DISTANCE', int(dis)+dist_off)
            li.append(df)
        except KeyError:
            print('read file' + file + ' raise KeyError')

    return pd.concat(li)


def to_csv(df, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)

    df.to_csv(os.path.join(folder, filename), index=False)


def export_mat(df, filename, folder=folder_clean):
    mat_dict = {}
    for col in df.columns:
        mat_dict[col] = list(df[col])
    savemat(os.path.join(folder, filename), mat_dict)


def get_templates(func='cubic'):
    templates = {}
    with pd.HDFStore('d:\\atom\\python\\templates\\open_%s_tmplt.h5' % func) as store:
        for key in store.keys():
            templates[key[1:]] = store.get(key)
    return templates