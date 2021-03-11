import matplotlib.pyplot as plt
import data_manager as dm


def plot_dict(d, ax):
    lists = sorted(d.items())
    x, y = zip(*lists)
    ax.plot(x, y)


def scatter_3d(df, name=''):
    plt.subplot(211, projection='3d')
    plt.scatter(df['CHANNEL'], df['DISTANCE'], df['PHASE'], label=name)
    #
    # plt.subplot(212)
    # plt.scatter(df['CHANNEL'], df['DISTANCE'], df['RSSI'])

    plt.legend()
    plt.show()


def scatter_3d_multi(dfs, names):
    plt.subplot(111, projection='3d')
    for df, name in zip(dfs, names):
        plt.scatter(df['CHANNEL'], df['DISTANCE'], df['RSSI'], label=name)
    plt.legend()
    plt.show()


def plot_mr_dist(liquid, d, col='RSSI', marker='o', label=''):
    d *= 100
    df = dm.import_clean_data('mr_%s_2d_cus_unwrap.csv' % liquid, folder=dm.folder_clean_mr)
    g = df.groupby('DISTANCE').get_group(d)
    plt.scatter(g['CHANNEL'], g[col], marker=marker, label=label)


def plot_mr_freq(liquid, f, col='RSSI', marker='o', label=''):
    f /= 10**6
    df = dm.import_clean_data('mr_%s_2d_cus_unwrap.csv' % liquid, folder=dm.folder_clean_mr)
    g = df.groupby('CHANNEL').get_group(f)
    plt.scatter(g['DISTANCE'], g[col], marker=marker, label=label)


def plot_lab_freq(liquid, f, col='RSSI', marker='o', label=''):
    f /= 10**6
    df = dm.import_clean_data('nongfu_%s_2d_unwrap.csv' % liquid, folder=dm.folder_clean)
    g = df.groupby('CHANNEL').get_group(f)
    plt.scatter(g['DISTANCE'], g[col], marker=marker, label=label)
