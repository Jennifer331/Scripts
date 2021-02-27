import glob, os
import matplotlib.pyplot as plt
import re
import pandas as pd


def import_data():
    folder = 'd:\\Atom\exp\\zhuyinan'
    pattern = "_\d{2}dbm"
    li = []
    for file in glob.glob(os.path.join(folder, "*.txt")):
        power_sub_str = re.search(pattern, file).group(0)
        power = ''.join([n for n in power_sub_str if n.isdigit()])
        df = pd.read_csv(file, header=None, usecols=[1, 2], names=['RSSI', 'PHASE'])
        df.insert(len(df.columns), 'POWER', power)
        li.append(df)
    return pd.concat(li)


if __name__ == '__main__':
    df = import_data()
    plt.subplot(211)
    plt.xlabel('Power (dbm)')
    plt.ylabel('RSSI (dbm)')
    plt.scatter(df['POWER'], df['RSSI'])

    plt.subplot(212)
    plt.xlabel('Power (dbm)')
    plt.ylabel('Phase (rad)')
    plt.scatter(df['POWER'], df['PHASE'])

    plt.tight_layout()
    plt.show()
