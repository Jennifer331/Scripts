import json
import matplotlib.pyplot as plt
from pynput import keyboard
import socket
import threading
from util import epc_dtoh
from util import color_names

HOST = 'localhost'
PORT = 8002

epcs = set()
color = {}
rssi_series = {}
phase_series = {}

lock = threading.Lock()


def clear():
    with lock:
        epcs.clear()
        color.clear()
        rssi_series.clear()
        phase_series.clear()


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
            print(message)
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
                            rssi_series[e][0].append(tag['channelInMhz'])
                            phase_series[e][0].append(tag['channelInMhz'])
                            rssi_series[e][1].append(tag['peakRssiInDbm'])
                            phase_series[e][1].append(tag['phaseAngleInRadians'])
                except Exception as err:
                    print(line)
                    raise err


t_receive = threading.Thread(target=receive_data)
t_receive.start()

if __name__ == "__main__":
    fig, axs = plt.subplots(2)
    fig.tight_layout()
    axs[1].set_title('Phase')
    while True:
        plt.clf()
        ax1 = plt.subplot(211)
        ax1.set_title('RSSI')
        ax2 = plt.subplot(212)
        ax2.set_title('Phase')
        with lock:
            for epc in epcs:
                rssi = rssi_series[epc]
                ax1.scatter(rssi[0], rssi[1], label=epc, color=color[epc])

                phase = phase_series[epc]
                ax2.scatter(phase[0], phase[1], label=epc, color=color[epc])
        plt.pause(0.2)
