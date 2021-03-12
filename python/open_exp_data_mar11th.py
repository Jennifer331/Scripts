import clean_data
import plot_raw_data2
import test

epc = '3008 33B2 DDD9 0140 0000 0040'
folder_i = 'D:\\Atom\\exp\\20210311'
file_filter = 'open_oil_[0-9]*cm.csv'
label = 'open_oil'

folder_o = 'D:\\Atom\\python\\data\\cleaned\\open'


def worker():
    plot_raw_data2.batch_plot_folder(folder_i, epc, file_filter, label)
    clean_data.clean_merge_dists(folder_i, file_filter, epc, folder_o, label, 30)
    clean_data.unwrap(folder_o, '%s_kde.csv' % label, folder_o, label)


if __name__ == '__main__':
    test.file_regex_test(folder_i, file_filter)