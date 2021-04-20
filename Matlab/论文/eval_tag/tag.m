load('tag.mat')
load('vinegar.mat')
freqs = [902.75:0.5:927.25];

colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% 相位
figure(1)
plot(freqs, unwrap(water_phase_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, unwrap(water_phase_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(watertag_phase_f), 'x-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(watertag_phase_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('标签1-正', '标签1-反', '标签2-正', '标签2-反')
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('相位/（rad）', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\tag_phase.pdf')
%% RSSI
figure(2)
plot(freqs, water_rssi_f, 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, water_rssi_t, 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, watertag_rssi_f, 'x-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, watertag_rssi_t, 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('标签1-正', '标签1-反', '标签2-正', '标签2-反')
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('接收信号强度/（dBm）', 'FontSize', 30)
% 
% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\tag_rssi.pdf')
%% diff
figure(3)
markersize = 3;
plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, 'o', 'color', colors(1,:), 'MarkerSize', 10)
hold on
plot(unwrap(watertag_phase_f) - unwrap(watertag_phase_t), watertag_rssi_f - watertag_rssi_t, '^', 'color', colors(2,:), 'MarkerSize', 10)

plot(unwrap(v_phase_f) - unwrap(v_phase_t), v_rssi_f - v_rssi_t, '*', 'color', colors(1,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('标签1-水', '标签2-水', '标签1-醋')
xlabel('相位差/（rad）', 'FontSize', 30)
ylabel('接收信号强度差/（dB）', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\tag_feature.pdf')
%% bar
c = categorical({'水-标签1', '水-标签2'});
y = [0.98, 0.82];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('准确率', 'FontSize', 30)
ylim([0 1.1])
set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\tag_accuracy.pdf')