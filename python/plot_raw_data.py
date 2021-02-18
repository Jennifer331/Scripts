import glob, os
from math import *
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import time


def import_data():
    epc = "E280 1160 6000 0207 A652 516D"
    folder = "d:\\Atom\\exp\\20210202"
    pattern = "_\d{4}cm"
    li = []
    for file in glob.glob(os.path.join(folder, "*.csv")):
        if not file.endswith('cm.csv'):
            continue
        dis_sub_str = re.search(pattern, file).group(0)
        dis = ''.join([n for n in dis_sub_str if n.isdigit()])
        df = pd.read_csv(file)
        df_filtered = df.loc[df['EPC'] == epc]
        df_filtered.insert(len(df_filtered.columns), 'DISTANCE', np.repeat(int(dis), len(df_filtered)))
        li.append(df_filtered)
    return pd.concat(li)


def plot_group_by(frame, genre='scatter', grp_col='CHANNEL', plt_cols=5,
                  p1_x='DISTANCE', p1_x_label='Distance (cm)', p1_y='PHASE', p1_y_label='Phase (rad)',
                  p2_x='DISTANCE', p2_x_label='Distance (MHz)', p2_y='RSSI', p2_y_label='RSSI (dBm)'):
    plt.clf()

    grouped = frame.groupby(grp_col)
    cnt = len(grouped)
    cols = plt_cols
    rows = ceil(cnt / cols)

    fig = plt.figure(figsize=(50, 100), constrained_layout=True)
    gs = gridspec.GridSpec(rows, cols, figure=fig)

    p1_x_min, p1_x_max = min(frame[p1_x]), max(frame[p1_x])
    p1_y_min, p1_y_max = min(frame[p1_y]), max(frame[p1_y])
    p2_x_min, p2_x_max = min(frame[p2_x]), max(frame[p2_x])
    p2_y_min, p2_y_max = min(frame[p2_y]), max(frame[p2_y])

    i = 0
    for name, group in grouped:
        gs_outer = gs[i // cols, i % cols]

        ax_outer = fig.add_subplot(gs_outer)
        ax_outer.set_title(str(name), loc='left')
        ax_outer.set_facecolor('cyan')
        ax_outer.patch.set_alpha(0.3)
        ax_outer.tick_params(axis='both', which='both', bottom=0, left=0, labelbottom=0, labelleft=0)

        gs_sub = gs_outer.subgridspec(3, 1)

        ax1 = fig.add_subplot(gs_sub[1])
        ax1.set_xlim(p1_x_min, p1_x_max)
        ax1.set_xlabel(p1_x_label)
        ax1.set_ylim(p1_y_min, p1_y_max)
        ax1.set_ylabel(p1_y_label)

        ax2 = fig.add_subplot(gs_sub[2])
        ax2.set_xlim(p2_x_min, p2_x_max)
        ax2.set_xlabel(p2_x_label)
        ax2.set_ylim(p2_y_min, p2_y_max)
        ax2.set_ylabel(p2_y_label)

        if genre == 'plot':
            ax1.plot(group[p1_x], group[p1_y])
            ax2.plot(group[p2_x], group[p2_y])
        else:
            ax1.scatter(group[p1_x], group[p1_y])
            ax2.scatter(group[p2_x], group[p2_y])

        i = i + 1
    plt.suptitle('Raw Data Grouped By %s' % grp_col)


def export(filename):
    pdf = PdfPages(filename + '.pdf')
    pdf.savefig()
    pdf.close()


if __name__ == '__main__':
    t_start = time.time()

    data_frame = import_data()
    plot_group_by(data_frame, genre='plot', grp_col='CHANNEL')
    export('grouped_by_freq_plot')
    plot_group_by(data_frame, genre='plot', grp_col='DISTANCE',
                  p1_x='CHANNEL', p1_x_label='Frequency (MHz)',
                  p2_x='CHANNEL', p2_x_label='Frequency (MHz)')
    export('grouped_by_dist_plot')

    t_end = time.time()
    print('%.2fs passed' % (t_end - t_start))
