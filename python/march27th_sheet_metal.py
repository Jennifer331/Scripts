import glob
import os
import re
import pandas as pd

import clean_data
import data_manager as dm

import test

folder = 'D:\\Atom\\exp\\20210327\\grill'
file = '*.csv'

folder_clean_nosheet_grill = 'd:\\Atom\\python\\data\\cleaned\\grill\\sheet'

label = 'sheet_%s'
liquids = ['water', 'empty', 'vinegar', 'oil']


def step1():
    clean_data.clean_merge_dists(folder, file % 'vinegar', dm.epc_vinegar, folder_out, label % 'vinegar', 30)


def step2():
    for liquid in liquids:
        clean_data.unwrap(dm.folder_clean_open, '%s_kde.csv' % liquid, dm.folder_clean_sheet, liquid)


def clean_folder(folder_i, file, folder_o, label):
    for file in glob.glob(os.path.join(folder_i, file)):
        try:
            name = os.path.splitext(os.path.basename(file))[0]
            matl = re.search('_[a-z]*$', name)[0][1:]
            epc = dm.epc[matl]
            df = pd.read_csv(file).groupby('EPC').get_group(epc).drop(columns=['EPC'])
            df = clean_data.kde_peak(df)
            # dm.to_csv(df, folder_o, '%s_%s.csv' % (name, label))
            # dm.export_mat(df, '%s_%s.mat' % (name, label), folder=folder_o)
        except KeyError:
            print('read file %s raise KeyError' % file)
        except pd.errors.EmptyDataError:
            print('read file %s raise EmptyDataError' % file)
        except:
            print('file ' + file)
            raise


# test.file_regex_test(folder, file)
clean_folder(folder, file, folder_clean_nosheet_grill, 'kde_sheet')