import json
import matplotlib.pyplot as plt
import socket
import threading
from util import epc_dtoh

HOST = 'localhost'
PORT = 8002

epcs = set()
rssi_series = {}
phase_series = {}

lock = threading.Lock()


def receive_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message = s.recv(65536)
            try:
                for line in message.splitlines():
                    tags = json.loads(line)
                    for tag in tags:
                        e = epc_dtoh(tag['epc'])
                        with lock:
                            if e not in epcs:
                                print('new ' + e)
                                epcs.add(e)
                                rssi_series[e] = [[], []]
                                phase_series[e] = [[], []]
                            rssi_series[e][0].append(tag['channelInMhz'])
                            phase_series[e][0].append(tag['channelInMhz'])
                            rssi_series[e][1].append(tag['peakRssiInDbm'])
                            phase_series[e][1].append(tag['phaseAngleInRadians'])
            except Exception as err:
                print(message)
                raise err


t_receive = threading.Thread(target=receive_data)
t_receive.start()

if __name__ == "__main__":
    fig, axs = plt.subplots(2)
    axs[1].set_title('Phase')
    while True:
        plt.clf()
        with lock:
            for epc in epcs:
                ax1 = plt.subplot(211)
                rssi = rssi_series[epc]
                plt.scatter(rssi[0], rssi[1], label=epc)
                ax1.set_title('RSSI')

                ax2 = plt.subplot(212)
                phase = phase_series[epc]
                plt.scatter(phase[0], phase[1], label=epc)
                ax2.set_title('Phase')
        print('loop out')
        plt.pause(0.2)
