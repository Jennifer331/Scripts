load('tag.mat')
load('vinegar.mat')
freqs = [902.75:0.5:927.25];

colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% 相位
figure(1)
plot(freqs, unwrap(water_phase_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(water_phase_t), 'o-',  'color', colors(color_t,:))

plot(freqs, unwrap(watertag_phase_f), 'x-',  'color', colors(color_f,:))
plot(freqs, unwrap(watertag_phase_t), 'x-', 'color', colors(color_t,:))
hold off

legend('标签1-正', '标签1-反', '标签2-正', '标签2-反')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'tag_phase.pdf')
%% RSSI
figure(2)
plot(freqs, water_rssi_f, 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, water_rssi_t, 'o-',  'color', colors(color_t,:))

plot(freqs, watertag_rssi_f, 'x-',  'color', colors(color_f,:))
plot(freqs, watertag_rssi_t, 'x-', 'color', colors(color_t,:))
hold off

legend('标签1-正', '标签1-反', '标签2-正', '标签2-反')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（rad）')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tag_rssi.pdf')
%% diff
figure(3)
markersize = 3;
plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, 'o', 'color', colors(1,:))
hold on
plot(unwrap(watertag_phase_f) - unwrap(watertag_phase_t), watertag_rssi_f - watertag_rssi_t, 'o', 'color', colors(2,:))

plot(unwrap(v_phase_f) - unwrap(v_phase_t), v_rssi_f - v_rssi_t, '^', 'color', colors(1,:))
hold off

legend('标签1-水', '标签2-水', '标签1-醋')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tag_feature.pdf')
%% bar
c = categorical({'水-标签1', '水-标签2'});
y = [0.98, 0.82];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('准确率')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tag_accuracy.pdf')