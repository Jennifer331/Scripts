from collections import defaultdict
import json
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from pynput import keyboard
import socket
import threading
from util import epc_dtoh
from util import color_names

HOST = 'localhost'
PORT = 8002

frequencies = [902.75, 903.25, 903.75, 904.25, 904.75, 905.25, 905.75, 906.25, 906.75, 907.25, 907.75, 908.25, 908.75,
               909.25, 909.75, 910.25, 910.75, 911.25, 911.75, 912.25, 912.75, 913.25, 913.75, 914.25, 914.75, 915.25,
               915.75, 916.25, 916.75, 917.25, 917.75, 918.25, 918.75, 919.25, 919.75, 920.25, 920.75, 921.25, 921.75,
               922.25, 922.75, 923.25, 923.75, 924.25, 924.75, 925.25, 925.75, 926.25, 926.75, 927.25]

filters = ('3008 33b2 ddd9 0140 0000 0000', )
filter_mode = True

opacity = 0.5
marker_size = 5

# data
epcs = set()
color = {}
rssi_series = {}
phase_series = {}

# configuration
conf = defaultdict(lambda: filter_mode)
view_model_mapping = {}

lock = threading.Lock()


def clear():
    with lock:
        epcs.clear()
        color.clear()
        rssi_series.clear()
        phase_series.clear()

        # conf.clear()
        view_model_mapping.clear()


def on_press(key):
    global marker_size
    try:
        if key.char == 'c':
            clear()
        elif key.char == 'a':
            marker_size = max(1, marker_size - 1)
        elif key.char == 'f':
            marker_size += 1

    except AttributeError:
        print('special key {0} pressed'.format(key))


keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()


def receive_data():
    print("in receive_Data")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        last_msg = ''
        while True:
            message = s.recv(65536)
            buffer = []
            lines = message.splitlines()
            if lines[0][0] != ord('[') and len(last_msg) > 0:
                last_msg = last_msg + lines[0]
                lines.pop(0)
                buffer = [last_msg]
            buffer = buffer + lines
            last_msg = ''

            for line in buffer:
                if line[-1] != ord(']'):
                    last_msg = line
                    break

                try:
                    tags = json.loads(line)
                    for tag in tags:
                        e = epc_dtoh(tag['epc'])
                        with lock:
                            if e not in epcs:
                                print('new ' + e)
                                epcs.add(e)
                                color[e] = color_names[len(epcs) % len(color_names)]
                                rssi_series[e] = [[], []]
                                phase_series[e] = [[], []]
                            rssi_series[e][0].append(tag['channelInMhz'])
                            phase_series[e][0].append(tag['channelInMhz'])
                            rssi_series[e][1].append(tag['peakRssiInDbm'])
                            phase_series[e][1].append(tag['phaseAngleInRadians'])
                except Exception as err:
                    print(line)
                    raise err


t_receive = threading.Thread(target=receive_data)
t_receive.start()


def plot_update(frame_number):
    ax1.clear()
    ax2.clear()
    ax1.set_title('RSSI')
    ax1.set_xlim(min(frequencies), max(frequencies))
    ax1.set_ylim(auto=True)
    ax2.set_title('Phase')
    ax2.set_ylim(0, 7)
    ax2.set_xlim(min(frequencies), max(frequencies))
    with lock:
        for epc in epcs:
            if filter_mode and not epc.endswith(filters):
                continue
            rssi = rssi_series[epc]
            ax1.scatter(rssi[0], rssi[1], marker_size, label=epc, color=color[epc], alpha=opacity*conf[epc])

            phase = phase_series[epc]
            ax2.scatter(phase[0], phase[1], marker_size, label=epc, color=color[epc], alpha=opacity*conf[epc])
    legend = ax1.legend(loc="upper left", bbox_to_anchor=(1, 1), prop={'size': 6})
    for item, name in zip(legend.get_texts(), epcs):
        view_model_mapping[item] = name
        item.set_picker(True)


def on_pick(event):
    legend = event.artist
    epc = view_model_mapping[legend]
    with lock:
        conf[epc] ^= True


fig, axs = plt.subplots(2)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

fig.canvas.mpl_connect('pick_event', on_pick)
animation = FuncAnimation(fig, plot_update, interval=10)
fig.tight_layout()
plt.subplots_adjust(right=0.7)
plt.show()

