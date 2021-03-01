import math
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os
import pandas as pd
import clean_data
import plot_helper
import time

dists = [12, 13, 14, 15, 18, 21, 24, 27, 30, 36, 39, 42, 78, 81, 84, 87, 90, 93]
# dists = [12]
folder = 'D:\\Atom\\exp\\20210218'
folder_oil = 'D:\\Atom\\exp\\20210220'
epc = '3008 33B2 DDD9 0140 0000 0000'


def import_and_clean(filename, epc):
    try:
        df = pd.read_csv(filename, usecols=['CHANNEL', 'EPC', 'PHASE', 'RSSI']).groupby('EPC').get_group(epc)\
            .drop(columns=['EPC']).sort_values(by=['CHANNEL'])
        df = clean_data.kde_peak(df)
    except KeyError:
        df = pd.DataFrame(columns=['CHANNEL', 'PHASE', 'RSSI'])
    return df


def calculate_diff(dfs):
    phase = [{}, {}]
    rssi = [{}, {}]

    i = 0
    for df in dfs:
        records = df.to_dict('records')
        for record in records:
            channel = record['CHANNEL']
            phase[i][channel] = record['PHASE']
            rssi[i][channel] = record['RSSI']
        i += 1

    diff_phase, diff_rssi = {}, {}
    for channel in phase[0]:
        if channel not in phase[1]:
            continue
        diff_phase[channel] = phase[1][channel] - phase[0][channel]
        diff_rssi[channel] = rssi[1][channel] - phase[0][channel]

    return diff_phase, diff_rssi


def extract_diff(filename1, epc1, filename2, epc2, fig, gs_outer, title):
    df1 = import_and_clean(filename1, epc1)
    df2 = import_and_clean(filename2, epc2)

    if df1.empty or df2.empty:
        return

    diff_phase, diff_rssi = calculate_diff([df1, df2])

    gs_sub = gs_outer.subgridspec(2, 1)
    ax1 = fig.add_subplot(gs_sub[0])
    # ax1.set_ylim(-math.pi, math.tau)
    ax2 = fig.add_subplot(gs_sub[1])
    ax2.set_title(str(np.array(list(diff_phase.values())).var()))
    # ax2.set_ylim(-70, -20)

    plot_helper.plot_dict(diff_phase, ax1)
    plot_helper.plot_dict(diff_rssi, ax2)
    ax1.set_title(title)


def plot_liquid_empty_diff():
    cnt = len(dists)
    cols = 2
    rows = math.ceil(cnt/cols)

    fig = plt.figure(figsize=(50, 100))
    gs = gridspec.GridSpec(rows, cols, figure=fig)

    i = 0
    for dist in dists:
        extract_diff(os.path.join(folder, str(dist) + 'cm_empty.csv'), epc,
                     os.path.join(folder, str(dist) + 'cm_water.csv'), epc,
                     fig, gs[i // cols, i % cols], str(dist) + 'cm water-empty')
        i += 1

    pdf = PdfPages('.\\plot\\water_empty_diff_zoom_in.pdf')
    pdf.savefig()
    pdf.close()


def plot_diff():
    cnt = len(dists) - 1
    cols = 2
    rows = math.ceil(cnt / cols)
    fig = plt.figure(figsize=(50, 100))
    gs = gridspec.GridSpec(rows, cols, figure=fig)

    i = 0
    for d1, d2 in zip(dists, dists[1:]):
        extract_diff(os.path.join(folder_oil, str(d1) + 'cm_oil.csv'), epc,
                     os.path.join(folder_oil, str(d2) + 'cm_oil.csv'), epc,
                     fig, gs[i // cols, i % cols], str(d2) + '-' + str(d1))
        i += 1

    pdf = PdfPages('.\\plot\\oil_dist_diff_zoom_in.pdf')
    pdf.savefig()
    pdf.close()


if __name__ == '__main__':
    t_start = time.time()
    # plot_diff()
    plot_liquid_empty_diff()
    t_end = time.time()
    print('%2fs passed' % (t_end - t_start))



