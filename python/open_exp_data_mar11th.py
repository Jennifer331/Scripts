import clean_data
import data_manager as dm
import plot_raw_data
import plot_raw_data2
import test

epc = '3008 33B2 DDD9 0140 0000 0040'
folder_i = 'D:\\Atom\\exp\\20210311'
file_filter = 'open_oil_[0-9]*cm.csv'
label = 'open_oil'

folder_o = 'D:\\Atom\\python\\data\\cleaned\\open'


def open_oil_process():
    # plot_raw_data2.batch_plot_folder(folder_i, epc, file_filter, label)
    df = dm.import_from_folder(folder_i, file_filter, epc, 30)

    plot_raw_data.plot_group_by(df, grp_col='DISTANCE',
                                p1_x='CHANNEL', p1_x_label='Frequency (MHz)',
                                p2_x='CHANNEL', p2_x_label='Frequency (MHz)')
    plot_raw_data.export('%s_group_by_dist' % label)

    plot_raw_data.plot_group_by(df)
    plot_raw_data.export('%s_group_by_freq' % label)

    clean_data.clean_merge_dists(folder_i, file_filter, epc, folder_o, label, 30)
    clean_data.unwrap(folder_o, '%s_kde.csv' % label, folder_o, label)


def plot_mr():
    liquids = ['empty', 'water', 'ant_water', 'p_water', 'water2', 'oil', 'vinegar']
    for liquid in liquids:
        df = dm.import_from_folder('D:\\Atom\\exp\\20210307', 'mr_%s_[0-9]*cm.csv' % liquid, dm.epc_liquid)
        plot_raw_data.plot_group_by(df, grp_col='DISTANCE',
                                    p1_x='CHANNEL', p1_x_label='Frequency (MHz)',
                                    p2_x='CHANNEL', p2_x_label='Frequency (MHz)')
        plot_raw_data.export('mr_%s_group_by_dist' % liquid)

        plot_raw_data.plot_group_by(df)
        plot_raw_data.export('mr_%s_group_by_freq' % liquid)


def test():
    test.file_regex_test(folder_i, file_filter)


if __name__ == '__main__':
    plot_mr()
