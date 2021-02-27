import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


def import_data():
    epc = "E280 1160 6000 0207 A652 516D"
    filename = "d:\\Atom\\exp\\20210202\\exp_0202_0165cm_2.csv"
    df = pd.read_csv(filename)
    df_filtered = df.loc[df['EPC'] == epc]
    df_filtered = df_filtered.drop(columns=['EPC'])
    return df_filtered


def kde_peak(df):
    grouped = df.groupby('CHANNEL')
    channel, rssi, phase = [], [], []
    for name, group in grouped:
        channel.append(name)
        rssi.append(peak(group, 'RSSI'))
        phase.append(peak(group, 'PHASE'))
    phase = np.unwrap(phase, np.pi)
    d = {'CHANNEL': channel, 'RSSI': rssi, 'PHASE': phase}
    return pd.DataFrame(data=d)


def peak(group, col):
    if 1 == len(group[col]):
        return group[col].iloc[0]

    density = gaussian_kde(group[col])
    ind = np.linspace(group[col].min(), group[col].max(), 200)
    return ind[np.argsort(density(ind))[-1]]


if __name__ == '__main__':
    data_frame = import_data()
    cleaned = kde_peak(data_frame)
    plt.subplot(211)
    plt.scatter(cleaned['CHANNEL'], cleaned['PHASE'])
    plt.subplot(212)
    plt.ylim(-72.5, -20)
    plt.scatter(cleaned['CHANNEL'], cleaned['RSSI'])
    plt.show()
