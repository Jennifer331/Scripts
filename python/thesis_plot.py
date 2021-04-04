import data_manager as dm
import matplotlib.pyplot as plt


def init():
    plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
    vinegar, water, oil, empty = dm.import_all_clean_data()


for name, group in oil['outdoor'].groupby('CHANNEL'):
    plt.plot(group['DISTANCE'], group['RSSI'])
    plt.ylabel('接收信号强度(dBm)')
    plt.xlabel('位置（cm）')
    plt.title('室外-油')
    plt.savefig('outdoor_oil_rssi_all.pdf')
