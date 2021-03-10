import glob
import os
import re

folder = 'D:\\Atom\\exp\\20210307'
liquids = ['empty', 'water', 'ant_water', 'p_water', 'water2', 'oil', 'vinegar']

# file = 'D:\\Atom\\exp\\20210307\\mr_ant_water_000cm.csv'
# pattern = 'mr_[a-z_0-9]*_\d{3}cm.csv'
# pattern = 'mr_(empty|water|ant_water|p_water|water2|oil|vinegar)_\d{3}cm.csv'
pattern = 'mr_(' + '|'.join(scenarios) + ')_\d{3}cm.csv'

print(pattern)

for file in glob.glob(os.path.join(folder, '*.csv')):
    basename = os.path.basename(file)
    if re.match(pattern, basename) is None:
        print(file)

