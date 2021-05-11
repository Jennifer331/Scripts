import glob, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder_final = 'D:\\Atom\\python\\data\\cleaned\\grill\\final'
folder_outdoor = 'D:\\Atom\\python\\data\\cleaned\\grill\\outdoor'
folder_noback = 'D:\\Atom\\python\\data\\cleaned\\grill\\noback'


NUM_COLORS = 20
cm = plt.get_cmap('gist_rainbow')


def outdoor():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    matls = ['empty', 'oil', 'vinegar', 'water']
    for matl in matls:
        df_h = pd.read_csv(os.path.join(folder_outdoor, 'outdoor_d1_%s_front_kde_outdoor.csv' % matl))
        df_t = pd.read_csv(os.path.join(folder_outdoor, 'outdoor_d1_%s_tail_kde_outdoor.csv' % matl))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        phase_diff[phase_diff < 0] += 2 * np.pi
        # ax.scatter(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])
        ax.plot(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])
    plt.legend(matls)
    ax.set_xlabel('phase diff')
    ax.set_ylabel('rssi diff')
    ax.set_zlabel('channel')

    plt.show()


def oil():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for folder, front, end in zip([folder_outdoor, folder_noback],
                                  ['outdoor_d1_oil_front_kde_outdoor.csv', 'd1_oil_front_noback.csv'],
                                  ['outdoor_d1_oil_tail_kde_outdoor.csv', 'd1_oil_tail_noback.csv']):
        df_h = pd.read_csv(os.path.join(folder, front))
        df_t = pd.read_csv(os.path.join(folder, end))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        phase_diff[phase_diff < 0] += 2 * np.pi
        ax.plot(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    matl = 'oil'
    for d in [7, 11, 1, 8]:
        df_h = pd.read_csv(os.path.join(folder_final, 'd%d_%s_f_kde.csv' % (d, matl)))
        df_t = pd.read_csv(os.path.join(folder_final, 'd%d_%s_t_kde.csv' % (d, matl)))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        phase_diff[phase_diff < 0] += 2 * np.pi
        ax.plot(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    ax.set_xlabel('phase diff')
    ax.set_ylabel('rssi diff')
    ax.set_zlabel('channel')

    plt.legend(['outdoor', 'noback', 7, 11, 1, 8])
    plt.title(matl)
    plt.show()


def vinegar():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for folder, front, end in zip([folder_outdoor, folder_noback],
                                  ['outdoor_d1_vinegar_front_kde_outdoor.csv', 'd1_vinegar_front_noback.csv'],
                                  ['outdoor_d1_vinegar_tail_kde_outdoor.csv', 'd1_vinegar_tail_noback.csv']):
        df_h = pd.read_csv(os.path.join(folder, front))
        df_t = pd.read_csv(os.path.join(folder, end))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        # phase_diff[phase_diff < 0] += 2 * np.pi
        ax.scatter(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    matl = 'vinegar'
    ds = [1, 4, 6, 7, 8, 9]
    for d in ds:
        df_h = pd.read_csv(os.path.join(folder_final, 'd%d_%s_f_kde.csv' % (d, matl)))
        df_t = pd.read_csv(os.path.join(folder_final, 'd%d_%s_t_kde.csv' % (d, matl)))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        # phase_diff[phase_diff < 0] += 2 * np.pi
        ax.scatter(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    ax.set_xlabel('phase diff')
    ax.set_ylabel('rssi diff')
    ax.set_zlabel('channel')

    plt.legend(['outdoor', 'noback'] + ds)
    plt.show()


def water():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_prop_cycle('color', [cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])

    matl = 'water'
    for folder, front, end in zip([folder_outdoor, folder_noback],
                                  ['outdoor_d1_%s_front_kde_outdoor.csv' % matl, 'd1_%s_front_noback.csv' % matl],
                                  ['outdoor_d1_%s_tail_kde_outdoor.csv' % matl, 'd1_%s_tail_noback.csv' % matl]):
        df_h = pd.read_csv(os.path.join(folder, front))
        df_t = pd.read_csv(os.path.join(folder, end))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        # phase_diff[phase_diff < 0] += 2 * np.pi
        ax.scatter(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    ds = [1, 4, 6, 7, 8, 9, 10, 11, 101, 102, 103, 104, 105]
    for d in ds:
        df_h = pd.read_csv(os.path.join(folder_final, 'd%d_%s_f_kde.csv' % (d, matl)))
        df_t = pd.read_csv(os.path.join(folder_final, 'd%d_%s_t_kde.csv' % (d, matl)))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        # phase_diff[phase_diff < 0] += 2 * np.pi
        ax.scatter(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    ax.set_xlabel('phase diff')
    ax.set_ylabel('rssi diff')
    ax.set_zlabel('channel')

    plt.legend(['outdoor', 'noback'] + ds)
    plt.show()


def empty():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    matl = 'water'
    for folder, front, end in zip([folder_outdoor, folder_noback],
                                  ['outdoor_d1_%s_front_kde_outdoor.csv' % matl, 'd1_%s_front_noback.csv' % matl],
                                  ['outdoor_d1_%s_tail_kde_outdoor.csv' % matl, 'd1_%s_tail_noback.csv' % matl]):
        df_h = pd.read_csv(os.path.join(folder, front))
        df_t = pd.read_csv(os.path.join(folder, end))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        # phase_diff[phase_diff < 0] += 2 * np.pi
        ax.scatter(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    ds = []
    for d in ds:
        df_h = pd.read_csv(os.path.join(folder_final, 'd%d_%s_f_kde.csv' % (d, matl)))
        df_t = pd.read_csv(os.path.join(folder_final, 'd%d_%s_t_kde.csv' % (d, matl)))
        phase_diff = np.unwrap(df_h['PHASE']) - np.unwrap(df_t['PHASE'])
        # phase_diff[phase_diff < 0] += 2 * np.pi
        ax.scatter(phase_diff, df_h['RSSI'] - df_t['RSSI'], df_h['CHANNEL'])

    ax.set_xlabel('phase diff')
    ax.set_ylabel('rssi diff')
    ax.set_zlabel('channel')

    plt.legend(['outdoor', 'noback'] + ds)
    plt.show()


# empty()
# vinegar()
oil()
# water()
# outdoor()

# d = 1
# matl = 'oil'
#
# df_h = pd.read_csv(os.path.join(folder_final, 'd%d_%s_f_kde.csv' % (d, matl)))
# df_t = pd.read_csv(os.path.join(folder_final, 'd%d_%s_t_kde.csv' % (d, matl)))
#
#
# plt.plot(df_h['CHANNEL'], df_h['PHASE'])
# plt.plot(df_t['CHANNEL'], df_t['PHASE'])
#
# plt.show()