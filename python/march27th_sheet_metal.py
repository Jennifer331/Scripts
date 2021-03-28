import clean_data
import data_manager as dm


folder = 'D:\\Atom\\exp\\20210327'
file = 'sheet_%s_[0-9]*cm.csv'

folder_out = dm.folder_clean_sheet

label = 'sheet_%s'
liquids = ['water', 'empty', 'vinegar', 'oil']


def step1():
    clean_data.clean_merge_dists(folder, file % 'vinegar', dm.epc_vinegar, folder_out, label % 'vinegar', 30)


def step2():
    for liquid in liquids:
        clean_data.unwrap(dm.folder_clean_open, '%s_kde.csv' % liquid, dm.folder_clean_sheet, liquid)
