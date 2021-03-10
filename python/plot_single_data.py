import numpy as np
import pandas as pd
from clean_data import *


def import_data(filename, epc='E280 1160 6000 0207 A652 516D'):
    df = pd.read_csv(filename, usecols=['CHANNEL', 'EPC', 'PHASE', 'RSSI'])
    return df.groupby('EPC').get_group(epc).drop(columns=['EPC']).sort_values(by=['CHANNEL'])


if __name__ == '__main__':
    # df = import_data('D:\\Atom\\exp\\20210202\\exp_0202_0052cm_long.csv')
    filenames = ['D:\\Atom\\exp\\20210202\\exp_0202_0102cm_d.csv']
    i = 1
    for filename in filenames:
        df = import_data(filename)
        plt.figure(i); i += 1

        # df['CHANNEL'], df['PHASE'] = np.unwrap([df['CHANNEL'], 2*df['PHASE']], np.pi)
        # df['PHASE'] /= 2

        plt.subplot(221)
        plt.scatter(df['CHANNEL'], df['RSSI'])

        plt.subplot(222)
        plt.scatter(df['CHANNEL'], df['PHASE'])

        cleaned_df = mean(df)

        plt.subplot(223)
        plt.scatter(cleaned_df['CHANNEL'], cleaned_df['RSSI'])

        plt.subplot(224)
        plt.scatter(cleaned_df['CHANNEL'], cleaned_df['PHASE'])

    plt.show()
