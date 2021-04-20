load('oil_d678.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% PHASE
figure(1)
plot(freqs, unwrap(d6_oil_phase_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, unwrap(d6_oil_phase_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(d7_oil_phase_f), '.-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(d7_oil_phase_t), '.--', 'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(d8_oil_phase_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(d8_oil_phase_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('位置1-正', '位置1-反','位置2-正', '位置2-反', '位置3-正', '位置3-反')
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('相位/（rad）', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\dist_phase.pdf')
%% RSSI
figure(2)
plot(freqs, unwrap(d6_oil_rssi_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, unwrap(d6_oil_rssi_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(d7_oil_rssi_f), '.-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(d7_oil_rssi_t), '.--', 'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(d8_oil_rssi_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(d8_oil_rssi_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('位置1-正', '位置1-反','位置2-正', '位置2-反', '位置3-正', '位置3-反')
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('接收信号强度/（dBm）', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\dist_rssi.pdf')
%% diff
figure(3)
plot(unwrap(d6_oil_phase_f) - unwrap(d6_oil_phase_t), d6_oil_rssi_f - d6_oil_rssi_t, 's', 'color', colors(1,:), 'MarkerSize', 10)
hold on
plot(unwrap(d7_oil_phase_f) - unwrap(d7_oil_phase_t), d7_oil_rssi_f - d7_oil_rssi_t, 'o', 'color', colors(2,:), 'MarkerSize', 10)
plot(unwrap(d8_oil_phase_f) - unwrap(d8_oil_phase_t), d8_oil_rssi_f - d8_oil_rssi_t, 'x', 'color', colors(3,:), 'MarkerSize', 10)

hold off

set(gca, 'FontSize', 20)
legend('位置1', '位置2', '位置3')
xlabel('相位差/（rad）', 'FontSize', 30)
ylabel('接收信号强度差/（dB）', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])
% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\dist_feature.pdf')
%% bar
c = categorical({'位置1', '位置2', '位置3'});
c = reordercats(c, {'位置1', '位置2', '位置3'})
y = [1, 1, 0.62];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('准确率', 'FontSize', 30)
ylim([0 1.1])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\dist_accuracy.pdf')