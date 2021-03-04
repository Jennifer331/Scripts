import os
import pandas as pd


def to_csv(df, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)

    df.to_csv(os.path.join(folder, filename), index=False)


def import_from_file(filename, epc):
    try:
        df = pd.read_csv(filename, usecols=['CHANNEL', 'EPC', 'PHASE', 'RSSI']).groupby('EPC').get_group(epc)\
            .drop(columns=['EPC']).sort_values(by=['CHANNEL'])
    except KeyError:
        df = pd.DataFrame(columns=['CHANNEL', 'PHASE', 'RSSI'])
    return df
