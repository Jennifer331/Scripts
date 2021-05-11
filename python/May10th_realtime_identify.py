from datetime import datetime
import pandas as pd
import os
import numpy as np

import clean_data
import data_manager as dm

from statistics import mode

folder = f"d:\\atom\\exp\\{datetime.today().strftime('%Y%m%d')}"
epc = dm.epc_water

df_f = pd.read_csv(os.path.join(folder, 'head.csv')).groupby('EPC').get_group(epc).drop(columns=['EPC'])
df_t = pd.read_csv(os.path.join(folder, 'tail.csv')).groupby('EPC').get_group(epc).drop(columns=['EPC'])

df_f = clean_data.kde_peak(df_f)
df_t = clean_data.kde_peak(df_t)

clf = dm.get_classifier()
diff_p = np.unwrap(df_f['PHASE']) - np.unwrap(df_t['PHASE'])
diff_r = df_f['RSSI'] - df_t['RSSI']
result = clf.predict(np.column_stack((diff_p, diff_r)))

print(mode(result))
