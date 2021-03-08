import data_manager as dm
import plot_helper as plotter

# plotter.scatter_3d(dm.import_clean_data('nongfu_empty.csv'), name='empty')
# plotter.scatter_3d(dm.import_clean_data('nongfu_oil.csv'), name='oil')
# plotter.scatter_3d(dm.import_clean_data('nongfu_vinegar.csv'), name='vinegar')
# plotter.scatter_3d(dm.import_clean_data('nongfu_water.csv'), name='water')

# plotter.scatter_3d_multi([dm.import_clean_data('nongfu_empty.csv'),
#                           dm.import_clean_data('nongfu_oil.csv'),
#                           dm.import_clean_data('nongfu_vinegar.csv'),
#                           dm.import_clean_data('nongfu_water.csv')],
#                          ['empty', 'oil', 'vinegar', 'water'])


def convert_to_mat():
    for file in dm.clean_files:
        dm.export_mat(dm.import_clean_data(file + '.csv'), file + '.mat')

    dm.export_mat(dm.import_clean_data('white_empty.csv'), 'white_empty.mat')


dm.export_mat(dm.import_test_data(), 'test.mat', folder=dm.folder_test)
