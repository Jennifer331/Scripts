% load('water.mat')
plot(water_d, water_r, 'x')
hold on
plot(waterp_d, waterp_r, 'x')
plot(waterant_d, waterant_r, 'x')
plot(water2_d, water2_r, 'x')
hold off
xlabel('距离/（cm）')
ylabel('接收信号强度/（dBm）')

legend('水', '水-重复', '水-天线2', '水2')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'test.pdf')