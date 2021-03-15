import numpy as np
import os
import pandas as pd
from time import time
from scipy.interpolate import Rbf

import data_manager as dm
import rfid_liquid_classification as classifier

matls = ['water', 'empty', 'oil2', 'vinegar']
frequencies = np.array(dm.channels)

folder_template = 'd:\\atom\\python\\templates'
file_template = 'open_raw_tmplt.h5'


def generate_raw_template():
    for matl in matls:
        df = dm.import_clean_data('open_%s_kde.csv' % matl, dm.folder_clean_open)
        for name, group in df.groupby('DISTANCE'):
            missing = np.setdiff1d(frequencies, group['CHANNEL'])
            for f in missing:
                df = df.append({'DISTANCE': name, 'CHANNEL': f, 'RSSI': np.NaN, 'PHASE': np.NaN}, ignore_index=True)
        df = df.sort_values(by=['DISTANCE', 'CHANNEL'])
        df.to_hdf('./templates/open_raw_tmplt.h5', key=matl)


def generate_interp_template(function='cubic'):
    for matl in matls:
        df = dm.import_clean_data('open_%s_2d_cus_unwrap.csv' % matl, dm.folder_clean_open)
        rbfi_r = Rbf(df['DISTANCE'], df['CHANNEL'], df['RSSI'], function=function)
        rbfi_p = Rbf(df['DISTANCE'], df['CHANNEL'], df['PHASE'], function=function)
        x, y = np.meshgrid(np.arange(30, 150, 1), frequencies)
        rssi = rbfi_r(x, y)
        phase = rbfi_p(x, y)
        n = np.product(x.shape)
        df = pd.DataFrame(data={'DISTANCE': np.reshape(x, n), 'CHANNEL': np.reshape(y, n), 'RSSI': np.reshape(rssi, n),
                                'PHASE': np.reshape(phase, n)})
        df.to_hdf('./templates/open_%s_tmplt.h5' % function, key=matl)


def get_templates(func='cubic'):
    templates = {}
    with pd.HDFStore('./templates/open_%s_tmplt.h5' % func) as store:
        for key in store.keys():
            templates[key[1:]] = store.get(key)
    return templates


def random_pick_validation_data_50(key='water'):
    df = pd.read_hdf(os.path.join(folder_template, file_template), key=key)
    grouped = df.groupby('DISTANCE')
    keys = list(grouped.groups.keys())
    i = np.random.randint(len(grouped))
    g = grouped.get_group(keys[i]).sort_values(by=['CHANNEL'])
    return g['RSSI'], g['PHASE']


def random_pick_validation_data_1(key='water'):
    df = pd.read_hdf(os.path.join(folder_template, file_template), key=key)
    i = np.random.randint(len(df))
    while df.iloc[i]['DISTANCE'] > 150:
        i = np.random.randint(len(df))
    return df.iloc[i]['CHANNEL'], df.iloc[i]['RSSI'], df.iloc[i]['PHASE']


def test_data():
    df = dm.import_from_file()

def test_50():
    t = get_templates()

    # r_rand = np.random.uniform(low=-70, high=-50, size=50)
    # p_rand = np.random.uniform(low=0, high=2*np.pi, size=50)
    # d = classifier.dist_to_any(r_rand, p_rand, t)
    # print("Distance of the random data: " + d)

    print('materials are: ' + str(t.keys()))
    r, p = random_pick_validation_data_50("water")
    d = classifier.dist_to_any(r, p, t)
    print("water validation data: " + str(d))

    r, p = random_pick_validation_data_50("empty")
    d = classifier.dist_to_any(r, p, t)
    print("empty validation data: " + str(d))

    r, p = random_pick_validation_data_50("vinegar")
    d = classifier.dist_to_any(r, p, t)
    print("vinegar validation data: " + str(d))

    r, p = random_pick_validation_data_50("oil2")
    d = classifier.dist_to_any(r, p, t)
    print("oil2 validation data: " + str(d))


def test_1():
    t = get_templates()

    # r_rand = np.random.uniform(low=-70, high=-50, size=50)
    # p_rand = np.random.uniform(low=0, high=2*np.pi, size=50)
    # d = classifier.dist_to_any(r_rand, p_rand, t)
    # print("Distance of the random data: " + d)

    print('materials are: ' + str(t.keys()))

    f, r, p = random_pick_validation_data_1("empty")
    d = classifier.dist_to_any(r, p, f, t)
    s = np.argsort(d)
    s = np.argsort(s)
    print("empty validation data: \t\t" + str(s) + str(d))

    f, r, p = random_pick_validation_data_1("oil2")
    d = classifier.dist_to_any(r, p, f, t)
    s = np.argsort(d)
    s = np.argsort(s)
    print("oil2 validation data: \t\t" + str(s) + str(d))

    f, r, p = random_pick_validation_data_1("vinegar")
    d = classifier.dist_to_any(r, p, f, t)
    s = np.argsort(d)
    s = np.argsort(s)
    print("vinegar validation data: \t" + str(s) + str(d))

    f, r, p = random_pick_validation_data_1("water")
    d = classifier.dist_to_any(r, p, f, t)
    s = np.argsort(d)
    s = np.argsort(s)
    print("water validation data: \t\t" + str(s) + str(d))


def test_interp(function='cubic'):
    df = pd.read_hdf('./templates/open_%s_tmplt.h5' % function, 'oil2')
    dm.export_mat(df, '%s_oil2.mat' % function, dm.folder_templates)


def test_iter(cnt=5):
    matl = matls[np.random.randint(4)]
    t = get_templates()
    d = np.full(4, 0)
    for i in range(cnt):
        f, r, p = random_pick_validation_data_1(matl)
        d = np.add(d, classifier.dist_to_any(r, p, f, t))
    s = np.argsort(d)
    s = np.argsort(s)

    result = (list(t.keys())[np.argmin(d)] == matl)
    # if not result:
    if True:
        print('materials are: ' + str(t.keys()))
        print(matl + " validation data: \t\t" + str(s) + str(d))

    return result


if __name__ == '__main__':
    t1 = time()
    # test_interp()
    # generate_interp_template()
    # test_1()
    # test_iter()
    right_cnt = 0
    for i in range(1):
        right_cnt += test_iter(100)
    print('%d times right in 50 trials' % right_cnt)

    t2 = time()
    print('consume: %fs' % (t2 - t1))