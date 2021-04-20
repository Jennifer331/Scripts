% load('water.mat')
plot(water_d, water_r, 'x', 'MarkerSize', 10)
hold on
plot(waterp_d, waterp_r, 'o', 'MarkerSize', 10)
plot(waterant_d, waterant_r, '^', 'MarkerSize', 10)
plot(water2_d, water2_r, 's', 'MarkerSize', 10)
hold off
set(gca, 'FontSize', 20)
xlabel('距离/（cm）', 'FontSize', 30)
ylabel('接收信号强度/（dBm）', 'FontSize', 30)

legend('水', '水-重复', '水-天线2', '水2')

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\water_replicate.pdf')