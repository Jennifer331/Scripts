import glob, os
import math
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import pandas as pd
import time


def import_data(folder, epc):
    d = {}
    for filename in glob.glob(os.path.join(folder, '*.csv')):
        try:
            df = pd.read_csv(filename).groupby('EPC').get_group(epc).drop(columns=['EPC', 'TIME'])
            d[filename[:-4]] = df
        except KeyError:
            d[filename[:-4]] = {'CHANNEL': [], 'RSSI': [], 'PHASE': []}

    return d


def plot(data, cols=5):
    cnt = len(data)
    rows = math.ceil(cnt / cols)
    fig = plt.figure(figsize=(50, 100), constrained_layout=True)
    gs = gridspec.GridSpec(rows, cols, figure=fig)

    i = 0
    for k in data:
        gs_outer = gs[i // cols, i % cols]
        ax_outer = fig.add_subplot(gs_outer)
        ax_outer.set_title(k)

        gs_sub = gs_outer.subgridspec(2, 1)
        ax1 = fig.add_subplot(gs_sub[0])
        ax2 = fig.add_subplot(gs_sub[1])

        ax1.scatter(data[k]['CHANNEL'], data[k]['PHASE'])
        ax2.scatter(data[k]['CHANNEL'], data[k]['RSSI'])

        i += 1

    pdf = PdfPages('liquids_raw.pdf')
    pdf.savefig()
    pdf.close()


if __name__ == '__main__':
    t_start = time.time()

    d = import_data('D:\\Atom\\exp\\20210218', '3008 33B2 DDD9 0140 0000 0000')
    plot(d)

    t_end = time.time()
    print('%.2fs passed' % (t_end - t_start))
