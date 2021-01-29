import json
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

conf = {}
view_model_mapping = {}
frequency = np.linspace(902.75, 927.25, 50)
phase1 = np.random.uniform(0, 2*np.pi, 50)
phase2 = np.random.uniform(0, 2*np.pi, 50)
conf['phase1'] = True
conf['phase2'] = True

fig, ax = plt.subplots()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
ax.scatter(frequency, phase1, label='Sample 1')
ax.scatter(frequency, phase2, label='Sample 2')


leg = ax.legend(fancybox=True, shadow=True, bbox_to_anchor=(0.2, 1.2))
# leg.set_picker(True)
# for item in leg.get_lines():
#     item.set_picker(True)
# for item in leg.get_patches():
#     item.set_picker(True)
# for item in leg.get_texts():
#     item.set_picker(True)
# for item in leg.legendHandles:
#     item.set_picker(True)
for item, name in zip(leg.get_texts(), ['phase1', 'phase2']):
    view_model_mapping[item] = name
    item.set_picker(True)


def on_pick(event):
    print(type(event.artist))
    legend = event.artist
    line = view_model_mapping[legend]
    conf[line] ^= True


def update(frame_number):
    ax.clear()
    phase1[np.random.randint(49)] = np.random.uniform(0, 2*np.pi)
    plt.title('Trial ' + str(frame_number))
    # ax.scatter(frequency, phase1, label='Sample 1', alpha=conf['phase1'])
    # ax.scatter(frequency, phase2, label='Sample 2', alpha=conf['phase2'])
    line1 = ax.scatter(frequency, phase1, label='Sample 1')
    line2 = ax.scatter(frequency, phase2, label='Sample 2')
    line1.set_visible(conf['phase1'])
    line2.set_visible(conf['phase2'])

    leg = ax.legend(fancybox=True, shadow=True, bbox_to_anchor=(0.2, 1.2))
    for item, name in zip(leg.get_texts(), ['phase1', 'phase2']):
        view_model_mapping[item] = name
        item.set_picker(True)


fig.canvas.mpl_connect('pick_event', on_pick)
animation = FuncAnimation(fig, update, interval=10)
plt.show()
