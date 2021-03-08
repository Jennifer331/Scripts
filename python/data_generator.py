import math
import numpy as np
import os
import pandas as pd
from scipy import constants

import data_manager as dm
import io_helper

channels = [902.75, 903.25, 903.75, 904.25, 904.75, 905.25, 905.75, 906.25, 906.75, 907.25, 907.75, 908.25, 908.75,
            909.25, 909.75, 910.25, 910.75, 911.25, 911.75, 912.25, 912.75, 913.25, 913.75, 914.25, 914.75, 915.25,
            915.75, 916.25, 916.75, 917.25, 917.75, 918.25, 918.75, 919.25, 919.75, 920.25, 920.75, 921.25, 921.75,
            922.25, 922.75, 923.25, 923.75, 924.25, 924.75, 925.25, 925.75, 926.25, 926.75, 927.25]
dists = [12, 13, 14, 15, 18, 21, 24, 27, 30, 36, 39, 42, 78, 81, 84, 87, 90, 93]
dists = [1, 2, 3, 4, 5, 8, 11, 14, 17, 20, 26, 29, 32, 68, 71, 74, 77, 80, 83, 92, 100, 108, 135, 140, 145, 155, 165,
         175, 185, 240]


def generate():
    phase = []
    rssi = []
    f = []
    d = []
    for dist in dists:
        for channel in channels:
            f.append(channel)
            d.append(dist)
            phase.append(calc_phase(channel * 10**6, dist/100))
            rssi.append(calc_rssi(channel * 10**6, dist/100))
    df = pd.DataFrame(data={'DISTANCE': d, 'CHANNEL': f, 'PHASE': phase, 'RSSI': rssi})
    io_helper.to_csv(df, dm.folder_test, dm.file_test)


def generate_dist():
    for channel in channels:
        phase = []
        rssi = []
        for dist in dists:
            phase.append(calc_phase(902.75, dist))
            rssi.append(calc_rssi(902.75, dist))


def calc_phase(f, d):
    return -(2*d*math.tau*f/constants.speed_of_light) % math.tau


def calc_rssi(f, d, p_reader=32.5, g_reader=9, g_tag=0, bs_trans_loss=5):
    return p_reader + 2*g_reader + 2*g_tag + 40*math.log(constants.speed_of_light/(4*math.pi*d*f), 10) - bs_trans_loss


if __name__ == "__main__":
    generate()
