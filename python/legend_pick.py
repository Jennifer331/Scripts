import numpy as np
from matplotlib.transforms import Bbox
import matplotlib.pyplot as plt


t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)

fig, ax = plt.subplots()
ax.set_title('Click on legend line to toggle line on/off')
line1, = ax.plot(t, y1, lw=2, label='1 Hz')
line2, = ax.plot(t, y2, lw=2, label='2 Hz')
leg = ax.legend(fancybox=True, shadow=True)

lines = [line1, line2]
lined = {}
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)
    lined[legline] = origline


def on_pick(event):
    print(event)
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()


# pixels to scroll per mousewheel event
d = {"down" : 30, "up" : -30}


def func(evt):
    if leg.contains(evt):
        bbox = leg.get_bbox_to_anchor()
        bbox = Bbox.from_bounds(bbox.x0, bbox.y0+d[evt.button], bbox.width, bbox.height)
        tr = leg.axes.transAxes.inverted()
        leg.set_bbox_to_anchor(bbox.transformed(tr))
        fig.canvas.draw_idle()


fig.canvas.mpl_connect("scroll_event", func)
fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()
