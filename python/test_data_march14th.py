import datetime
import glob
import os
import pandas as pd
import numpy as np
import re

import data_manager as dm
import rfid_liquid_classification as classifier
import test


def format_static_test_data():
    static_test_files = 'test_*cm.csv'
    li = []
    for file in glob.glob(os.path.join(dm.folder_open, static_test_files)):
        matl = re.search('_\w*?_', file).group(0)[1:-1]
        dist = int(re.search('_\d+cm', file).group(0)[1:-2])
        epc = dm.epc[matl]

        df = dm.import_from_file(file, epc)
        df.insert(0, 'DISTANCE', dist)
        df.insert(0, 'MATERIAL', matl)
        li.append(df)

    df = pd.concat(li)
    dm.to_csv(df, dm.folder_open_test, 'open_test_data_static.csv')
    df.to_hdf(os.path.join(dm.folder_open_test, 'open_test_data.h5'), 'static')


def format_dynamic_test_data():
    dynamic_test_file = 'test_*_running_*.csv'
    li = []
    for file in glob.glob(os.path.join(dm.folder_open, dynamic_test_file)):
        matl = re.search('_\w*?_', file).group(0)[1:-1]
        epc = dm.epc[matl]

        df = dm.import_from_file(file, epc)
        df.insert(0, 'MATERIAL', matl)
        li.append(df)

    df = pd.concat(li)
    dm.to_csv(df, dm.folder_open_test, 'open_test_data_dynamic.csv')
    df.to_hdf(os.path.join(dm.folder_open_test, 'open_test_data.h5'), 'dynamic')


def test_random_batch_data(genre='static'):
    print(genre)
    ti = datetime.datetime.now().strftime('%H_%M_%S')
    folder = os.path.join(dm.folder_log, '%s_%s' % (genre, ti))
    os.makedirs(folder)
    f_log = open(os.path.join(folder, 'log_%s.txt' % ti), 'w')
    f_log.write('%s test\n' % genre)

    import_func = dm.import_static_test_data if genre == 'static' else dm.import_dynamic_test_data
    df = import_func(dm.folder_open_test, 'open_test_data_%s.csv' % genre)
    t = dm.get_templates()
    f_log.write(str(list(t.keys())))
    trial_total = 0
    trial_success = 0
    for name, group in df.groupby('MATERIAL'):
        left = len(group)
        i = 0
        while left > 0:
            iter_num = min(left, np.random.randint(100, 300))
            d = np.full(4, 0)
            log = pd.DataFrame()
            for j in range(iter_num):
                s = group.iloc[i]
                log = log.append(s)
                d = np.add(d, classifier.dist_joint_to_any(s['RSSI'], s['PHASE'], s['CHANNEL'], t))
                i += 1; left -= 1;
            result = (list(t.keys())[np.argmin(d)] == name)
            s = np.argsort(d)
            s = np.argsort(s)
            trial_total += 1
            trial_success += result

            msg = 'material: %s, iter: %d, result: %r, details: %s%s\n' % (name, iter_num, result, str(s), str(d))
            print(msg)
            f_log.write(msg)
            if not result:
                df.to_csv(os.path.join(folder, 'fail_%s_%d.csv' % (name, iter_num)))

    msg = '\n%d success in %d trials\n' % (trial_success, trial_total)
    print(msg)
    f_log.write(msg)
    f_log.close()

    with open(os.path.join(dm.folder_log, dm.file_summary), 'a') as f:
        f.write('%s,%d,%d\n' % (folder, trial_success, trial_total))
        f.close()


def test_dist_data():
    # ti = datetime.datetime.now().strftime('%H_%M_%S')
    # folder = os.path.join(dm.folder_log, 'static_%s' % ti)
    # os.makedirs(folder)
    # f_log = open(os.path.join(folder, 'log_%s.txt' % ti), 'w')

    df = dm.import_static_test_data(dm.folder_open_test, 'open_test_data_static.csv')
    t = dm.get_templates()
    keys = list(t.keys())
    print(keys)
    for name, group in df.groupby('MATERIAL'):
        print('\n----------------------------Material: %s----------------------------' % name)
        for name2, group2 in group.groupby('DISTANCE'):
            print('-----------Distance: %d, Sample: %d-----------' % (name2, len(group2)))
            d_rssi = np.full(4, 0)
            d_phase = np.full(4, 0)
            for i in range(len(group2)):
                s = group2.iloc[i]
                d_r, d_p = classifier.dist_to_any(s['RSSI'], s['PHASE'], s['CHANNEL'], t)
                d_rssi = np.add(d_rssi, d_r)
                d_phase = np.add(d_phase, d_p)

            result_r = (keys[np.argmin(d_rssi)] == name)
            rank_r = d_rssi.argsort()
            rank_r = rank_r.argsort()
            result_p = (keys[np.argmin(d_phase)] == name)
            rank_p = d_phase.argsort()
            rank_p = rank_p.argsort()

            print('d_rssi: %s%s, %r\nd_phase: %s%s, %r' % (str(rank_r), str(d_rssi), result_r, str(rank_p), str(d_phase), result_p))


def batch_test():
    g = ['dynamic', 'static']
    for i in range(100):
        test_random_batch_data(genre=g[np.random.randint(2)])


# test_dist_data()
# test_random_batch_data()


def test_dist1_data():
    # ti = datetime.datetime.now().strftime('%H_%M_%S')
    # folder = os.path.join(dm.folder_log, 'static_%s' % ti)
    # os.makedirs(folder)
    # f_log = open(os.path.join(folder, 'log_%s.txt' % ti), 'w')

    df = dm.import_static_test_data(dm.folder_open_test, 'open_test_data_static.csv')
    t = dm.get_templates()
    keys = list(t.keys())
    print(keys)
    for name, group in df.groupby('MATERIAL'):
        print('\n----------------------------Material: %s----------------------------' % name)
        all_dists = t[name]['DISTANCE'].unique()
        m = len(keys)
        n = len(all_dists)
        for name2, group2 in group.groupby('DISTANCE'):
            print('-----------Distance: %d, Sample: %d-----------' % (name2, len(group2)))
            d_rssi = np.full([m, n], 0)
            d_phase = np.full([m, n], 0)
            for i in range(len(group2)):
                s = group2.iloc[i]
                d_r, d_p = classifier.dist1_to_any(s['RSSI'], s['PHASE'], s['CHANNEL'], t)
                d_rssi = np.add(d_rssi, d_r)
                d_phase = np.add(d_phase, d_p)
                d = np.add(d_rssi, d_phase)

            d_min = np.min(d, 1)
            guess = np.argmin(d_min)
            guess_index = np.argmin(d, 1) + 30

            result = (keys[guess] == name)
            print('result: %s, distance: %s, guess index: %s' % (result, str(d_min), guess_index))
            # rank_r = d_rssi.argsort()
            # rank_r = rank_r.argsort()
            # result_p = (keys[guess] == name)
            # rank_p = d_phase.argsort()
            # rank_p = rank_p.argsort()


test_dist1_data()