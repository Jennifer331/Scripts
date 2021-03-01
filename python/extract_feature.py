import math
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
import pandas as pd
import clean_data
import plot_helper
import time

dists = [12, 13, 14, 15, 18, 21, 24, 27, 30, 36, 39, 42, 78, 81, 84, 87, 90, 93]


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


def extract_diff(filename1, epc1, filename2, epc2, fig, gs_outer):
    df1 = import_and_clean(filename1, epc1)
    df2 = import_and_clean(filename2, epc2)

    if df1.empty or df2.empty:
        return

    diff_phase, diff_rssi = calculate_diff([df1, df2])

    gs_sub = gs_outer.subgridspec(2, 1)
    ax1 = fig.add_subplot(gs_sub[0])
    ax2 = fig.add_subplot(gs_sub[1])

    plot_helper.plot_dict(diff_phase, ax1)
    plot_helper.plot_dict(diff_rssi, ax2)


if __name__ == '__main__':
    t_start = time.time()

    folder = 'D:\\Atom\\exp\\20210218'
    epc = '3008 33B2 DDD9 0140 0000 0000'
    cnt = len(dists)
    cols = 2
    rows = math.ceil(cnt/cols)

    fig = plt.figure(figsize=(50, 100))
    gs = gridspec.GridSpec(rows, cols, figure=fig)

    i = 0
    for dist in dists:
        extract_diff(os.path.join(folder, str(dist) + 'cm_empty.csv'), epc,
                     os.path.join(folder, str(dist) + 'cm_water.csv'), epc,
                     fig, gs[i // cols, i % cols])
        i += 1

    pdf = PdfPages('water_feature.pdf')
    pdf.savefig()
    pdf.close()

    t_end = time.time()
    print('%2fs passed' % (t_end - t_start))



