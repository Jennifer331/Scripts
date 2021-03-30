import glob
import os
import re
import pandas as pd

import clean_data
import data_manager as dm

# clean_data.clean_merge_dists('D:\\Atom\\exp\\20210329\\outdoor_water', '*.csv', dm.epc_water, dm.folder_clean_outdoor, 'outdoor_water')
# clean_data.unwrap(dm.folder_clean_outdoor, 'outdoor_%s_kde.csv' % 'water', dm.folder_clean_outdoor, 'water')


def clean_folder(folder_i, file, folder_o, label='test'):
    for file in glob.glob(os.path.join(folder_i, file)):
        try:
            name = os.path.splitext(os.path.basename(file))[0]
            matl = re.search('d[0-9]_[a-z]*_', name)[0][3:-1]
            epc = dm.epc[matl]

            # print(name, matl, epc)
            df = pd.read_csv(file).groupby('EPC').get_group(epc).drop(columns=['EPC'])
            df = clean_data.kde_peak(df)
            dm.to_csv(df, folder_o, '%s_%s.csv' % (name, label))
            dm.export_mat(df, '%s_%s.mat' % (name, label), folder=folder_o)
        except KeyError:
            print('read file %s raise KeyError' % file)
        except pd.errors.EmptyDataError:
            print('read file %s raise EmptyDataError' % file)
        except:
            print('file ' + file)
            raise


clean_folder('D:\\Atom\\exp\\20210329\\outdoor_grill', '*.csv', 'D:\\Atom\\python\\data\\cleaned\\grill\\outdoor', 'kde_outdoor')