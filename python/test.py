import glob
import os


def file_regex_test(folder, file):
    for file in glob.glob(os.path.join(folder, file)):
        print(file)