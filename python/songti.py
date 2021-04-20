import matplotlib
import matplotlib.pyplot as plt


import data_manager as dm

vinegar, water, oil, empty = dm.import_all_clean_data()

#导入字体库中的宋体
Songti = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

plt.figure(figsize=(24, 18))
# 不同环境均存在多径
for name, group in oil['lab'].groupby('CHANNEL'):
    plt.plot(group['DISTANCE'], group['RSSI'])
    plt.ylabel('接收信号强度(dBm)', fontproperties=Songti, fontsize=30)
    plt.xlabel('位置（cm）', fontproperties=Songti, fontsize=30)

    plt.tick_params(axis='both', which='major', labelsize=20)
    plt.tick_params(axis='both', which='minor', labelsize=20)
    plt.title('办公室-油', fontproperties=Songti, fontsize=30)
    # plt.savefig('oil_rssi_all_lab.pdf')
plt.show()
