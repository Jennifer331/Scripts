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

# data
epcs = set()
color = {}
rssi_series = {}
phase_series = {}

# configuration
conf = {}
view_model_mapping = {}

lock = threading.Lock()


def clear():
    with lock:
        epcs.clear()
        color.clear()
        rssi_series.clear()
        phase_series.clear()

        conf.clear()
        view_model_mapping.clear()


def on_press(key):
    try:
        if key.char == 'c':
            clear()
    except AttributeError:
        print('special key {0} pressed'.format(key))


keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()


def receive_data():
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
                                color[e] = color_names[len(epcs)]
                                rssi_series[e] = [[], []]
                                phase_series[e] = [[], []]
                                conf[e] = False
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
    ax2.set_title('Phase')
    with lock:
        for epc in epcs:
            rssi = rssi_series[epc]
            ax1.scatter(rssi[0], rssi[1], label=epc, color=color[epc], alpha=conf[epc])

            phase = phase_series[epc]
            ax2.scatter(phase[0], phase[1], label=epc, color=color[epc], alpha=conf[epc])
    legend = ax1.legend(loc="upper left", bbox_to_anchor=(1, 1), prop={'size': 6})
    for item, name in zip(legend.get_texts(), epcs):
        view_model_mapping[item] = name
        item.set_picker(True)


def on_pick(event):
    legend = event.artist
    epc = view_model_mapping[legend]
    conf[epc] ^= True


fig, axs = plt.subplots(2)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

fig.canvas.mpl_connect('pick_event', on_pick)
animation = FuncAnimation(fig, plot_update, interval=10)
fig.tight_layout()
plt.subplots_adjust(right=0.7)
plt.show()

