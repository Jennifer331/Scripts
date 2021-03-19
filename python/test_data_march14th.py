import datetime
import glob
import os
import pandas as pd
import numpy as np
import re

import data_manager as dm
import rfid_liquid_classification as classifier

w_r = classifier.w_r
w_p = classifier.w_p


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


def batch_test():
    g = ['dynamic', 'static']
    for i in range(100):
        test_random_batch_data(genre=g[np.random.randint(2)])


def test_pos_by_pos():
    df_test = dm.import_static_test_data(dm.folder_open_test, 'open_test_data_static.csv')
    tmplts = dm.get_templates()

    matls = list(tmplts.keys())
    print(matls)
    for matl_test, g_matl_test in df_test.groupby('MATERIAL'):
        print('\n----------------------------Material: %s----------------------------' % matl_test)
        pos_set = tmplts[matl_test]['DISTANCE'].unique()
        shape_tmplt = [len(matls), len(pos_set)]
        for pos_test, g_pos_test in g_matl_test.groupby('DISTANCE'):
            print('-----------Relative Position: %d, Test Data#: %d-----------' % (pos_test, len(g_pos_test)))
            d_rssi = np.full(shape_tmplt, 0)
            d_phase = np.full(shape_tmplt, 0)
            for index, row in g_pos_test.iterrows():
                d_r, d_p = classifier.distance_by_position(row['RSSI'], row['PHASE'], row['CHANNEL'], tmplts, shape_tmplt)
                d_rssi = np.add(d_rssi, d_r)
                d_phase = np.add(d_phase, d_p)

            corr = classifier.pos_coor(g_pos_test, tmplts, shape_tmplt)
            # w_r_corr = 6*(1-corr)**1.5 + 1
            w_r_corr = np.heaviside(corr-0.7, 0)*1+(1-np.heaviside(corr-0.7, 0))*10**(5*(0.85-corr))
            d_joint = np.add(w_r*w_r_corr*d_rssi, w_p*d_phase)
            d_min = np.min(d_joint, 1)

            pos_guess = np.argmin(d_joint, 1)
            pos_guess_coord = list(np.arange(len(matls))), pos_guess
            matl_guess = matls[np.argmin(d_min)]
            result = (matl_guess == matl_test)
            print('result: %s\nrelative position inferred for each material: %s\njoint distance: %s\nrssi distance: %s\nphase distance: %s\n' %
                  (result, pos_guess, str(d_min), str(d_rssi[pos_guess_coord]), str(d_phase[pos_guess_coord])))


# test_random_batch_data()
test_pos_by_pos()
# format_static_test_data()