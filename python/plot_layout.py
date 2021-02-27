import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import  PdfPages
from math import *
import numpy as np
import time

t_start = time.time()

cnt = 1
cols = 5
rows = ceil(cnt/cols)

fig = plt.figure(figsize=(40, 80), constrained_layout=True)
gs = gridspec.GridSpec(rows, cols, figure=fig)

for i in range(cnt):
    gs_outer = gs[i // cols, i % cols]
    ax_outer = fig.add_subplot(gs_outer)
    ax_outer.set_title(i, loc="left")
    ax_outer.set_facecolor("cyan")
    ax_outer.patch.set_alpha(0.3)
    ax_outer.tick_params(axis='both', which='both', bottom=0, left=0, labelbottom=0, labelleft=0)

    gs_sub = gs_outer.subgridspec(3, 1)
    ax1 = fig.add_subplot(gs_sub[1])
    ax1.set_title("Real")
    # ax1.scatter(list(range(10)), np.random.randn(10))
    ax1.plot(list(range(10)), np.random.randn(10))
    ax2 = fig.add_subplot(gs_sub[2])
    ax2.set_title("Theory")
    # ax2.scatter(list(range(10)), np.random.randn(10))
    ax2.plot(list(range(10)), np.random.randn(10))

# fig.set_constrained_layout_pads(w_pad=2./72., h_pad=2./72., hspace=0., wspace=0.)
plt.suptitle("Frequency from 902 - 928 MHz")
plt.show()
# pdf = PdfPages('longplot.pdf')
# pdf.savefig()
# pdf.close()

t_end = time.time()
print(t_end - t_start)

