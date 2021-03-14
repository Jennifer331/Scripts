import pandas as pd

import clean_data
import data_manager as dm


folder = 'D:\\Atom\\exp\\20210313'
file = 'open_%s_[0-9]*cm.csv'
epc_water = '3008 33B2 DDD9 0140 0000 0020'
epc_vinegar = '3008 33B2 DDD9 0140 0000 0060'
epc_empty = '3008 33B2 DDD9 0140 0000 0030'
epc_oil = '3008 33B2 DDD9 0140 0000 0040'
label = 'open_%s'

# df = dm.import_from_folder(folder, file, epc, 30)
clean_data.clean_merge_dists(folder, file % 'oil2', epc_oil, dm.folder_clean_open, label % 'oil2', 30)

