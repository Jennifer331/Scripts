from collections import defaultdict
import json
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from pynput import keyboard
import re
import socket
import threading
from util import epc_dtoh
from util import color_names

import configparser
import ast

HOST = 'localhost'
PORT = 8002

frequencies = [902.75, 903.25, 903.75, 904.25, 904.75, 905.25, 905.75, 906.25, 906.75, 907.25, 907.75, 908.25, 908.75,
               909.25, 909.75, 910.25, 910.75, 911.25, 911.75, 912.25, 912.75, 913.25, 913.75, 914.25, 914.75, 915.25,
               915.75, 916.25, 916.75, 917.25, 917.75, 918.25, 918.75, 919.25, 919.75, 920.25, 920.75, 921.25, 921.75,
               922.25, 922.75, 923.25, 923.75, 924.25, 924.75, 925.25, 925.75, 926.25, 926.75, 927.25]
data = defaultdict(lambda: defaultdict(lambda: {'RSSI': [], 'PHASE': []}))

lock = threading.Lock()


def reload():
    global epc, frequencies
    with lock:
        config = configparser.ConfigParser()
        config.read('config.txt')

        epc = ast.literal_eval(config.get('SHOW', 'epc'))
        frequencies = ast.literal_eval(config.get('SHOW', 'f'))


epc = ['3008 33b2 ddd9 0140 0000 0000']
frequencies = [902.75]
reload()


def clear():
    global data
    with lock:
        data = defaultdict(lambda: defaultdict(lambda: {'RSSI': [], 'PHASE': []}))


def on_press(key):
    try:
        if key.char == 'c':
            clear()
        elif key.char == 'r':
            reload()

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
            if message is None or len(message) == 0:
                print(message)
            if re.match(b'\[\{"epc"', lines[0]) is None and len(last_msg) > 0:
                last_msg = last_msg + lines[0]
                lines.pop(0)
                buffer = [last_msg]
            buffer = buffer + lines
            last_msg = ''

            for line in buffer:
                if re.match(b'.*\}\]$', line) is None:
                    last_msg = line
                    break

                try:
                    tags = json.loads(line)
                    for tag in tags:
                        e = epc_dtoh(tag['epc'])
                        f = tag['channelInMhz']
                        with lock:
                            data[e][f]['RSSI'].append(tag['peakRssiInDbm'])
                            data[e][f]['PHASE'].append(tag['phaseAngleInRadians'])
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
        for e in epc:
            for f in frequencies:
                ax1.plot(data[e][f]['RSSI'], label='-'.join([e, str(f)]))
                ax2.plot(data[e][f]['PHASE'], label='-'.join([e, str(f)]))

    ax1.legend(loc="upper left", bbox_to_anchor=(1, 1), prop={'size': 6})
    ax2.legend(loc="upper left", bbox_to_anchor=(1, 1), prop={'size': 6})


fig = plt.figure()
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

animation = FuncAnimation(fig, plot_update, interval=10)
fig.tight_layout()
plt.subplots_adjust(right=0.7)

plt.show()

