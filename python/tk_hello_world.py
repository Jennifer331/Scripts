import json
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
import threading
import time
import websocket

server = "ws://localhost:9092/socket"
epcs = set()
rssi_series = {}
phase_series = {}

lock = threading.Lock()


def on_message(ws, message):
    # print(message)
    data = json.loads(message)
    if data['type'] == 'readings':
        tags = data['tags']
        for tag in tags:
            e = tag['epc']
            with lock:
                if e not in epcs:
                    print('new ' + e)
                    epcs.add(e)
                    rssi_series[e] = [[], []]
                    phase_series[e] = [[], []]
                rssi_series[e][0].append(tag['channel'])
                phase_series[e][0].append(tag['channel'])
                rssi_series[e][1].append(tag['rssi'])
                phase_series[e][1].append(tag['phase'])


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


websocket.enableTrace(True)
ws = websocket.WebSocketApp(server,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
# ws.on_open = on_open


def receive_data():
    ws.run_forever()


t_receive = threading.Thread(target=receive_data)
t_receive.start()

if __name__ == "__main__":
    fig, axs = plt.subplots(2)
    axs[1].set_title('Phase')
    while True:
        plt.clf()
        # lines = []
        with lock:
            for epc in epcs:
                ax1 = plt.subplot(211)
                rssi = rssi_series[epc]
                line = plt.scatter(rssi[0], rssi[1], label=epc)
                ax1.set_title('RSSI')

                ax2 = plt.subplot(212)
                phase = phase_series[epc]
                plt.scatter(phase[0], phase[1], label=epc)
                ax2.set_title('Phase')
                # lines.append(line)
        # rax = plt.axes([0.05, 0.4, 0.1, 0.15])
        # labels = [str(line.get_label()) for line in lines]
        # visibility = [line.get_visible() for line in lines]
        # check = CheckButtons(rax, labels, visibility)
        print('loop out')
        plt.pause(0.2)
